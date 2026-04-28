import locale
import stripe  
from datetime import datetime 
from collections import Counter
from functools import wraps 
from flask import Flask, render_template, redirect, url_for, request, flash, session, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_super_secret_key_123'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'shop.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- STRIPE CONFIGURATION ---
app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51SwJE0CQlnqjfmn3YWsk8RsKA3ab95zDhOqKXjNf9bBchzOQiEqRe4jlsAUOXrVuZDJ5w9f4VRLK2mzDtH3GRZy300meuAenWg' 
app.config['STRIPE_SECRET_KEY'] = 'sk_test_51SwJE0CQlnqjfmn3FBFgw9IVewvEiaeTUsUfzxYojLmJ1XBJ886de9UX08P8hBSf1XaX2Vdh7JNs2wuKt5YSIIRY00FADoOAAR'
stripe.api_key = app.config['STRIPE_SECRET_KEY']

db = SQLAlchemy(app)

# --- 1. LOCALE SETTING ---
try:
    locale.setlocale(locale.LC_ALL, 'en_IN')
except Exception:
    locale.setlocale(locale.LC_ALL, '') 

@app.template_filter('inr')
def format_inr(value):
    try:
        return locale.currency(value, symbol=True, grouping=True)
    except:
        return f"₹ {value}"

# --- 2. LOGIN MANAGEMENT ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- 3. DATABASE MODELS ---
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(10), default='buyer') 
    orders = db.relationship('Order', backref='customer', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(500))
    description = db.Column(db.Text, nullable=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_ordered = db.Column(db.DateTime, default=datetime.utcnow)
    total_amount = db.Column(db.Float, nullable=False)
    items = db.relationship('OrderItem', backref='order', lazy=True)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# --- 4. CUSTOM DECORATOR ---
def seller_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'seller':
            flash("You need a Seller account to access this page.")
            return redirect(url_for('index')) 
        return f(*args, **kwargs)
    return decorated_function

# --- 5. PRODUCT ROUTES ---

@app.route('/')
def index():
    query = request.args.get('search')
    if query:
        products = Product.query.filter(Product.name.contains(query)).all()
    else:
        products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/admin/add', methods=['GET', 'POST'])
@login_required 
@seller_required 
def add_product():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            price = float(request.form.get('price'))
            image = request.form.get('image_url')
            desc = request.form.get('description')
            
            new_prod = Product(name=name, price=price, image_url=image, description=desc)
            db.session.add(new_prod)
            db.session.commit()
            flash('Product added successfully!')
            return redirect(url_for('index'))
        except ValueError:
            flash('Invalid price. Please enter a number.')
            
    return render_template('add_product.html')

# --- THIS IS THE MISSING FUNCTION THAT CAUSED THE ERROR ---
@app.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
@login_required
@seller_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == 'POST':
        product.name = request.form.get('name')
        product.price = float(request.form.get('price'))
        product.image_url = request.form.get('image_url')
        product.description = request.form.get('description')

        db.session.commit()
        flash('Product updated successfully!')
        return redirect(url_for('product_detail', product_id=product.id))

    return render_template('edit_product.html', product=product)
# ---------------------------------------------------------

@app.route('/delete_product/<int:product_id>')
@login_required 
@seller_required 
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted!')
    return redirect(url_for('index'))

# --- 6. AUTHENTICATION ROUTES ---

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uname = request.form.get('username')
        pwd = request.form.get('password')
        role = request.form.get('role') 
        
        if role not in ['buyer', 'seller']:
            role = 'buyer'

        if User.query.filter_by(username=uname).first():
            flash('Username already exists!')
            return redirect(url_for('register'))
            
        hashed_pwd = generate_password_hash(pwd, method='pbkdf2:sha256')
        new_user = User(username=uname, password=hashed_pwd, role=role)
        
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form.get('username')
        pwd = request.form.get('password')
        user = User.query.filter_by(username=uname).first()
        
        if user and check_password_hash(user.password, pwd):
            login_user(user)
            return redirect(url_for('index'))
        
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# --- 7. SHOPPING CART LOGIC ---

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session: 
        session['cart'] = []
    
    cart = session['cart']
    cart.append(product_id)
    session['cart'] = cart
    
    flash('Added to cart!')
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    cart_ids = session.get('cart', [])
    full_cart = []
    total = 0
    for p_id in cart_ids:
        p = Product.query.get(p_id)
        if p:
            full_cart.append(p)
            total += p.price

    return render_template('cart.html', display_cart=full_cart, total=total)

@app.route('/clear_cart') 
def clear_cart():
    session.pop('cart', None)
    flash('Cart cleared!')
    return redirect(url_for('view_cart'))

# --- 8. STRIPE & ORDER LOGIC ---

@app.route('/create-checkout-session', methods=['POST'])
@login_required 
def create_checkout_session():
    cart_ids = session.get('cart', [])
    if not cart_ids:
        flash('Your cart is empty!')
        return redirect(url_for('index'))

    item_counts = Counter(cart_ids)
    line_items = []
    
    for p_id, qty in item_counts.items():
        product = Product.query.get(p_id)
        if product:
            amount_in_paise = int(product.price * 100)
            line_items.append({
                'price_data': {
                    'currency': 'inr',
                    'product_data': {'name': product.name},
                    'unit_amount': amount_in_paise,
                },
                'quantity': qty,
            })

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=url_for('success', _external=True),
            cancel_url=url_for('view_cart', _external=True), 
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        flash(f'Error: {str(e)}')
        return redirect(url_for('view_cart'))

@app.route('/success')
@login_required
def success():
    cart_ids = session.get('cart', [])
    if not cart_ids:
        return redirect(url_for('index'))
    
    item_counts = Counter(cart_ids)
    total_order_amount = 0
    
    new_order = Order(user_id=current_user.id, total_amount=0)
    
    for p_id, qty in item_counts.items():
        product = Product.query.get(p_id)
        if product:
            order_item = OrderItem(
                product_name=product.name,
                product_price=product.price,
                quantity=qty,
                order=new_order 
            )
            db.session.add(order_item)
            total_order_amount += (product.price * qty)
    
    new_order.total_amount = total_order_amount
    db.session.add(new_order)
    db.session.commit()
    
    session.pop('cart', None)
    
    flash('Payment Successful! Order saved.')
    return redirect(url_for('my_orders'))

@app.route('/my_orders')
@login_required
def my_orders():
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.date_ordered.desc()).all()
    return render_template('my_orders.html', orders=orders)




# _______________________
"""
Custom API Endpoint to add poroducts via api server rather then the html context.

This help's when we want to schedule a auto upload as part of the testing, which saves time and effors and even check
the load of the server and error possiablities. 

This approach is currently setup for the temprory basisis, as the testing purpose, but can be fixed for
getting better outcomes.

"""
@app.route('/api/admin/add', methods=['POST'])
def api_add_product():
    auth = request.authorization
    
    # Verify Basic Auth
    if not auth or auth.username != 'Om' or auth.password != 'om':
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Verify user is a seller
    user = User.query.filter_by(username=auth.username).first()
    if not user or user.role != 'seller':
        return jsonify({'error': 'Seller access required'}), 403
    
    try:
        name = request.form.get('name')
        price = float(request.form.get('price'))
        image = request.form.get('image_url')
        desc = request.form.get('description')
        
        new_prod = Product(name=name, price=price, image_url=image, description=desc)
        db.session.add(new_prod)
        db.session.commit()
        
        return jsonify({
            'message': 'Product added successfully!',
            'product_id': new_prod.id
        }), 201
    except ValueError:
        return jsonify({'error': 'Invalid price. Please enter a number.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

# Single product deletion endpoint
@app.route('/api/admin/delete/<int:product_id>', methods=['DELETE'])
def api_delete_product(product_id):
    auth = request.authorization
    
    # Verify Basic Auth
    if not auth or auth.username != 'Om' or auth.password != 'om':
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Verify user is a seller
    user = User.query.filter_by(username=auth.username).first()
    if not user or user.role != 'seller':
        return jsonify({'error': 'Seller access required'}), 403
    
    try:
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        
        return jsonify({
            'message': 'Product deleted successfully!',
            'product_id': product_id
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500




# Delete all products endpoint (use with caution!)
@app.route('/api/admin/delete_all', methods=['POST'])
def api_delete_all():
    auth = request.authorization
    
    # Verify Basic Auth
    if not auth or auth.username != 'Om' or auth.password != 'om':
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Verify user is a seller
    user = User.query.filter_by(username=auth.username).first()
    if not user or user.role != 'seller':
        return jsonify({'error': 'Seller access required'}), 403
    
    try:
        # Require confirmation token in request
        data = request.get_json() or {}
        confirmation = data.get('confirm')
        
        if confirmation != 'DELETE_ALL_PRODUCTS':
            return jsonify({
                'error': 'Confirmation required',
                
                'message': 'Send {"confirm": "DELETE_ALL_PRODUCTS"} to confirm deletion'
            }), 400
        
        count = Product.query.count()
        Product.query.delete()
        db.session.commit()

        return jsonify({
            'message': f'All {count} products deleted successfully!',
            'deleted_count': count
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# Get all products (for listing)
@app.route('/api/products', methods=['GET'])
def api_get_products():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 1000, type=int)
        
        pagination = Product.query.paginate(page=page, per_page=per_page, error_out=False)
        
        products = [{
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'image_url': p.image_url,
            'description': p.description
        } for p in pagination.items]
        
        return jsonify({
            'products': products,
            'total': pagination.total,
            'page': page,
            'per_page': per_page,
            'pages': pagination.pages
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Delete multiple products at once
@app.route('/api/admin/delete_bulk', methods=['POST'])
def api_delete_bulk():
    auth = request.authorization
    
    if not auth or auth.username != 'Om' or auth.password != 'om':
        return jsonify({'error': 'Unauthorized'}), 401
    
    user = User.query.filter_by(username=auth.username).first()
    if not user or user.role != 'seller':
        return jsonify({'error': 'Seller access required'}), 403
    
    try:
        data = request.get_json()
        product_ids = data.get('product_ids', [])
        
        if not product_ids:
            return jsonify({'error': 'No product IDs provided'}), 400
        
        deleted_count = 0
        
        for product_id in product_ids:
            product = Product.query.get(product_id)
            if product:
                db.session.delete(product)
                deleted_count += 1
        
        db.session.commit()
        
        return jsonify({
            'message': f'Deleted {deleted_count} products',
            'deleted_count': deleted_count
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# --- 9. DATABASE INITIALIZATION ---

with app.app_context():
    db.create_all()
    # Updated sample products with description
    if not Product.query.first():
        db.session.add(Product(name="Sample Watch", price=1500.0, image_url="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500", description="A classic analog watch."))
        db.session.add(Product(name="Headphones", price=2500.0, image_url="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500", description="Noise cancelling headphones."))
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)