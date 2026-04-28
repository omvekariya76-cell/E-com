import requests
import time
import random

# Your endpoint
url = "http://127.0.0.1:5000/api/admin/add"
auth = ("Om", "om")

def generate_products():
    """Generate 1000 realistic products with proper images"""
    products = []
    
    # Electronics (150 products)
    electronics = [
        ("Headphones", 29.99, 399.99),
        ("Smartphone", 199.99, 1499.99),
        ("Laptop", 499.99, 2999.99),
        ("Tablet", 199.99, 1199.99),
        ("Smart Watch", 99.99, 899.99),
        ("Wireless Earbuds", 39.99, 299.99),
        ("Computer Monitor", 149.99, 1299.99),
        ("Keyboard", 19.99, 249.99),
        ("Mouse", 9.99, 149.99),
        ("Webcam", 29.99, 199.99),
        ("USB Hub", 14.99, 89.99),
        ("External Hard Drive", 49.99, 299.99),
        ("Power Bank", 19.99, 79.99),
        ("Phone Case", 9.99, 49.99),
        ("Screen Protector", 4.99, 29.99),
        ("Charging Cable", 5.99, 39.99),
        ("Bluetooth Speaker", 24.99, 399.99),
        ("Gaming Mouse", 29.99, 179.99),
        ("Mechanical Keyboard", 49.99, 299.99),
        ("Laptop Stand", 19.99, 99.99),
        ("Wireless Charger", 14.99, 79.99),
        ("Camera Lens", 199.99, 1999.99),
        ("Tripod", 19.99, 299.99),
        ("Ring Light", 24.99, 149.99),
        ("Microphone", 39.99, 399.99),
        ("Audio Interface", 79.99, 599.99),
        ("Studio Monitors", 149.99, 999.99),
        ("DJ Controller", 199.99, 1299.99),
        ("Graphics Tablet", 49.99, 499.99),
        ("VR Headset", 299.99, 999.99),
    ]
    
    brands_electronics = ["Sony", "Apple", "Samsung", "LG", "Dell", "HP", "Logitech", "Razer", "Corsair", "Asus", "Acer", "Lenovo", "Microsoft", "Google", "Anker", "Belkin", "JBL", "Bose", "Sennheiser", "Audio-Technica"]
    
    for i in range(150):
        item = random.choice(electronics)
        brand = random.choice(brands_electronics)
        model = f"{random.choice(['Pro', 'Ultra', 'Elite', 'Plus', 'Max', 'Air', 'Mini', 'Lite', 'Premium', 'Studio'])} {random.randint(1, 15)}"
        
        products.append({
            "name": f"{brand} {item[0]} {model}",
            "price": round(random.uniform(item[1], item[2]), 2),
            "image_url": f"https://picsum.photos/seed/{1000+i}/800/600",
            "description": f"High-quality {item[0].lower()} from {brand} featuring advanced technology, premium build quality, and excellent performance for professional and personal use."
        })
    
    # Home & Kitchen (150 products)
    home_kitchen = [
        ("Blender", 29.99, 399.99),
        ("Coffee Maker", 39.99, 599.99),
        ("Air Fryer", 59.99, 299.99),
        ("Pressure Cooker", 49.99, 249.99),
        ("Stand Mixer", 149.99, 599.99),
        ("Food Processor", 49.99, 399.99),
        ("Toaster", 19.99, 149.99),
        ("Microwave Oven", 79.99, 499.99),
        ("Vacuum Cleaner", 79.99, 799.99),
        ("Iron", 19.99, 149.99),
        ("Knife Set", 29.99, 399.99),
        ("Cookware Set", 49.99, 799.99),
        ("Dinnerware Set", 39.99, 299.99),
        ("Cutting Board", 9.99, 79.99),
        ("Storage Containers", 14.99, 89.99),
        ("Baking Sheet", 9.99, 49.99),
        ("Dutch Oven", 49.99, 399.99),
        ("Wok", 24.99, 199.99),
        ("Slow Cooker", 29.99, 199.99),
        ("Rice Cooker", 24.99, 299.99),
        ("Electric Kettle", 19.99, 129.99),
        ("Juicer", 39.99, 399.99),
        ("Can Opener", 9.99, 49.99),
        ("Measuring Cups", 7.99, 39.99),
        ("Mixing Bowls", 14.99, 89.99),
        ("Colander", 9.99, 49.99),
        ("Grater", 7.99, 39.99),
        ("Peeler", 4.99, 24.99),
        ("Whisk", 5.99, 29.99),
        ("Spatula Set", 9.99, 49.99),
    ]
    
    brands_home = ["KitchenAid", "Cuisinart", "Ninja", "Instant Pot", "Breville", "Hamilton Beach", "Black+Decker", "Oster", "Philips", "Dyson", "Shark", "Hoover", "Bissell", "Vitamix", "Blendtec", "All-Clad", "Le Creuset", "Lodge", "Pyrex", "OXO"]
    
    for i in range(150):
        item = random.choice(home_kitchen)
        brand = random.choice(brands_home)
        model = f"{random.choice(['Deluxe', 'Professional', 'Classic', 'Modern', 'Premium', 'Elite', 'Essential', 'Ultimate', 'Advanced', 'Signature'])}"
        
        products.append({
            "name": f"{brand} {model} {item[0]}",
            "price": round(random.uniform(item[1], item[2]), 2),
            "image_url": f"https://picsum.photos/seed/{2000+i}/800/600",
            "description": f"Premium {item[0].lower()} designed for modern kitchens. Durable construction, easy to clean, and perfect for everyday cooking and meal preparation."
        })
    
    # Fashion & Apparel (150 products)
    fashion = [
        ("T-Shirt", 9.99, 79.99),
        ("Jeans", 29.99, 199.99),
        ("Jacket", 49.99, 399.99),
        ("Sweater", 24.99, 199.99),
        ("Hoodie", 29.99, 149.99),
        ("Dress", 29.99, 299.99),
        ("Skirt", 19.99, 149.99),
        ("Shorts", 14.99, 99.99),
        ("Pants", 24.99, 179.99),
        ("Blazer", 59.99, 399.99),
        ("Coat", 79.99, 599.99),
        ("Sneakers", 39.99, 299.99),
        ("Boots", 49.99, 399.99),
        ("Sandals", 19.99, 149.99),
        ("Loafers", 39.99, 249.99),
        ("Heels", 29.99, 299.99),
        ("Belt", 14.99, 149.99),
        ("Hat", 14.99, 99.99),
        ("Scarf", 12.99, 149.99),
        ("Gloves", 9.99, 79.99),
        ("Socks", 5.99, 39.99),
        ("Underwear", 7.99, 49.99),
        ("Watch", 29.99, 999.99),
        ("Sunglasses", 19.99, 399.99),
        ("Backpack", 24.99, 199.99),
        ("Handbag", 39.99, 799.99),
        ("Wallet", 14.99, 199.99),
        ("Tie", 14.99, 99.99),
        ("Swimsuit", 19.99, 149.99),
        ("Activewear Set", 29.99, 199.99),
    ]
    
    brands_fashion = ["Nike", "Adidas", "Puma", "Under Armour", "Levi's", "Gap", "H&M", "Zara", "Uniqlo", "Tommy Hilfiger", "Calvin Klein", "Ralph Lauren", "Lacoste", "The North Face", "Patagonia", "Columbia", "Vans", "Converse", "New Balance", "Reebok"]
    
    for i in range(150):
        item = random.choice(fashion)
        brand = random.choice(brands_fashion)
        size = random.choice(["XS", "S", "M", "L", "XL", "XXL"])
        color = random.choice(["Black", "White", "Blue", "Red", "Green", "Gray", "Navy", "Khaki", "Brown", "Beige"])
        
        products.append({
            "name": f"{brand} {color} {item[0]} - Size {size}",
            "price": round(random.uniform(item[1], item[2]), 2),
            "image_url": f"https://picsum.photos/seed/{3000+i}/800/600",
            "description": f"Stylish and comfortable {item[0].lower()} in {color.lower()}. Made with premium materials for durability and style. Perfect for casual and active wear."
        })
    
    # Sports & Fitness (100 products)
    sports = [
        ("Yoga Mat", 14.99, 99.99),
        ("Dumbbells", 19.99, 299.99),
        ("Kettlebell", 19.99, 149.99),
        ("Resistance Bands", 9.99, 49.99),
        ("Jump Rope", 5.99, 39.99),
        ("Foam Roller", 14.99, 79.99),
        ("Exercise Ball", 14.99, 59.99),
        ("Yoga Block", 7.99, 29.99),
        ("Pull-up Bar", 19.99, 99.99),
        ("Weight Bench", 79.99, 499.99),
        ("Treadmill", 299.99, 2999.99),
        ("Exercise Bike", 149.99, 1999.99),
        ("Rowing Machine", 199.99, 1499.99),
        ("Elliptical Machine", 299.99, 2499.99),
        ("Protein Powder", 19.99, 99.99),
        ("Protein Bars", 14.99, 49.99),
        ("Shaker Bottle", 7.99, 29.99),
        ("Gym Bag", 19.99, 99.99),
        ("Water Bottle", 9.99, 49.99),
        ("Fitness Tracker", 29.99, 399.99),
        ("Heart Rate Monitor", 39.99, 199.99),
        ("Running Shoes", 49.99, 299.99),
        ("Training Shoes", 39.99, 249.99),
        ("Compression Shorts", 19.99, 79.99),
        ("Sports Bra", 19.99, 89.99),
        ("Workout Gloves", 9.99, 39.99),
        ("Knee Sleeves", 14.99, 59.99),
        ("Elbow Sleeves", 12.99, 49.99),
        ("Wrist Wraps", 9.99, 39.99),
        ("Lifting Straps", 9.99, 39.99),
    ]
    
    brands_sports = ["Nike", "Adidas", "Under Armour", "Reebok", "Puma", "Bowflex", "NordicTrack", "Peloton", "TRX", "Fitbit", "Garmin", "Polar", "Optimum Nutrition", "MuscleTech", "BSN", "Cellucor", "Hydroflask", "Yeti", "Manduka", "Lululemon"]
    
    for i in range(100):
        item = random.choice(sports)
        brand = random.choice(brands_sports)
        
        products.append({
            "name": f"{brand} {item[0]} {random.choice(['Pro', 'Elite', 'Performance', 'Training', 'Essential', 'Premium'])}",
            "price": round(random.uniform(item[1], item[2]), 2),
            "image_url": f"https://picsum.photos/seed/{4000+i}/800/600",
            "description": f"Professional-grade {item[0].lower()} designed for serious athletes and fitness enthusiasts. Durable, comfortable, and built to enhance your workout performance."
        })
    
    # Beauty & Personal Care (100 products)
    beauty = [
        ("Face Moisturizer", 12.99, 149.99),
        ("Face Wash", 7.99, 49.99),
        ("Serum", 14.99, 199.99),
        ("Sunscreen", 9.99, 59.99),
        ("Face Mask", 4.99, 79.99),
        ("Toner", 9.99, 69.99),
        ("Eye Cream", 14.99, 149.99),
        ("Lip Balm", 3.99, 24.99),
        ("Shampoo", 7.99, 49.99),
        ("Conditioner", 7.99, 49.99),
        ("Hair Mask", 9.99, 79.99),
        ("Hair Oil", 9.99, 69.99),
        ("Body Lotion", 9.99, 59.99),
        ("Body Wash", 7.99, 39.99),
        ("Hand Cream", 5.99, 39.99),
        ("Perfume", 29.99, 299.99),
        ("Cologne", 29.99, 299.99),
        ("Deodorant", 4.99, 29.99),
        ("Toothpaste", 3.99, 14.99),
        ("Toothbrush", 2.99, 199.99),
        ("Electric Shaver", 39.99, 399.99),
        ("Hair Dryer", 24.99, 449.99),
        ("Straightener", 29.99, 299.99),
        ("Curling Iron", 24.99, 199.99),
        ("Makeup Brush Set", 14.99, 149.99),
        ("Foundation", 14.99, 79.99),
        ("Lipstick", 7.99, 49.99),
        ("Mascara", 7.99, 39.99),
        ("Eyeshadow Palette", 14.99, 99.99),
        ("Nail Polish", 4.99, 24.99),
    ]
    
    brands_beauty = ["CeraVe", "Cetaphil", "Neutrogena", "L'Oreal", "Olay", "The Ordinary", "Paula's Choice", "La Roche-Posay", "Dove", "Nivea", "Garnier", "Maybelline", "MAC", "NYX", "Urban Decay", "Fenty Beauty", "Dyson", "Philips", "Braun", "Gillette"]
    
    for i in range(100):
        item = random.choice(beauty)
        brand = random.choice(brands_beauty)
        
        products.append({
            "name": f"{brand} {item[0]} {random.choice(['Advanced', 'Hydrating', 'Nourishing', 'Revitalizing', 'Gentle', 'Deep Cleansing', 'Anti-Aging', 'Brightening', 'Repair', 'Smooth'])}",
            "price": round(random.uniform(item[1], item[2]), 2),
            "image_url": f"https://picsum.photos/seed/{5000+i}/800/600",
            "description": f"Premium {item[0].lower()} formulated with high-quality ingredients. Dermatologist-tested, suitable for all skin types, and delivers visible results."
        })
    
    # Home Decor & Furniture (100 products)
    home_decor = [
        ("Table Lamp", 19.99, 299.99),
        ("Floor Lamp", 39.99, 499.99),
        ("Ceiling Light", 29.99, 799.99),
        ("Wall Art", 14.99, 499.99),
        ("Photo Frame", 7.99, 99.99),
        ("Mirror", 24.99, 599.99),
        ("Rug", 39.99, 999.99),
        ("Curtains", 19.99, 199.99),
        ("Throw Pillow", 9.99, 79.99),
        ("Throw Blanket", 19.99, 149.99),
        ("Vase", 12.99, 199.99),
        ("Plant Pot", 7.99, 99.99),
        ("Candle", 7.99, 79.99),
        ("Clock", 14.99, 299.99),
        ("Bookshelf", 49.99, 799.99),
        ("Coffee Table", 79.99, 1299.99),
        ("Side Table", 39.99, 599.99),
        ("TV Stand", 99.99, 1499.99),
        ("Desk", 99.99, 1999.99),
        ("Office Chair", 79.99, 1299.99),
        ("Dining Table", 199.99, 2999.99),
        ("Dining Chair", 49.99, 599.99),
        ("Bed Frame", 149.99, 2499.99),
        ("Mattress", 199.99, 2999.99),
        ("Nightstand", 49.99, 699.99),
        ("Dresser", 149.99, 1999.99),
        ("Wardrobe", 199.99, 2999.99),
        ("Storage Cabinet", 79.99, 1299.99),
        ("Coat Rack", 19.99, 149.99),
        ("Shoe Rack", 24.99, 199.99),
    ]
    
    brands_decor = ["IKEA", "West Elm", "Pottery Barn", "Crate & Barrel", "CB2", "Wayfair", "Ashley Furniture", "La-Z-Boy", "Herman Miller", "Steelcase", "Philips", "GE", "Hampton Bay", "Safavieh", "Uttermost", "Art3d", "Ambesonne", "Madison Park", "Hotel Collection", "Threshold"]
    
    for i in range(100):
        item = random.choice(home_decor)
        brand = random.choice(brands_decor)
        
        products.append({
            "name": f"{brand} {random.choice(['Modern', 'Contemporary', 'Classic', 'Rustic', 'Industrial', 'Scandinavian', 'Minimalist', 'Traditional', 'Mid-Century', 'Farmhouse'])} {item[0]}",
            "price": round(random.uniform(item[1], item[2]), 2),
            "image_url": f"https://picsum.photos/seed/{6000+i}/800/600",
            "description": f"Stylish {item[0].lower()} that adds character to any room. Quality construction with attention to detail, designed to complement modern interior design."
        })
    
    # Books & Media (75 products)
    books = [
        ("Fiction Novel", 9.99, 29.99),
        ("Non-Fiction Book", 12.99, 39.99),
        ("Biography", 14.99, 34.99),
        ("Cookbook", 14.99, 49.99),
        ("Self-Help Book", 12.99, 29.99),
        ("Business Book", 14.99, 39.99),
        ("Science Book", 14.99, 49.99),
        ("History Book", 14.99, 39.99),
        ("Art Book", 19.99, 79.99),
        ("Photography Book", 24.99, 99.99),
        ("Children's Book", 5.99, 24.99),
        ("Comic Book", 4.99, 29.99),
        ("Graphic Novel", 12.99, 39.99),
        ("Poetry Collection", 9.99, 24.99),
        ("Travel Guide", 14.99, 34.99),
        ("Textbook", 39.99, 299.99),
        ("Dictionary", 14.99, 79.99),
        ("Atlas", 19.99, 99.99),
        ("Calendar", 9.99, 29.99),
        ("Journal", 7.99, 39.99),
        ("Planner", 12.99, 49.99),
        ("Notebook", 4.99, 29.99),
        ("Coloring Book", 7.99, 24.99),
        ("Puzzle Book", 7.99, 19.99),
        ("Magazine Subscription", 19.99, 99.99),
    ]
    
    for i in range(75):
        item = random.choice(books)
        author = f"{random.choice(['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer', 'Michael', 'Linda', 'William', 'Elizabeth'])} {random.choice(['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez'])}"
        
        products.append({
            "name": f"{item[0]} by {author}",
            "price": round(random.uniform(item[1], item[2]), 2),
            "image_url": f"https://picsum.photos/seed/{7000+i}/800/600",
            "description": f"Engaging {item[0].lower()} that captivates readers from start to finish. Well-written, thought-provoking, and highly recommended by critics and readers alike."
        })
    
    # Toys & Games (75 products)
    toys = [
        ("Building Blocks", 14.99, 199.99),
        ("Action Figure", 9.99, 99.99),
        ("Doll", 12.99, 149.99),
        ("Board Game", 14.99, 99.99),
        ("Card Game", 7.99, 49.99),
        ("Puzzle", 9.99, 79.99),
        ("Remote Control Car", 19.99, 299.99),
        ("Stuffed Animal", 9.99, 79.99),
        ("Play-Doh Set", 9.99, 49.99),
        ("Art Set", 14.99, 99.99),
        ("Science Kit", 19.99, 149.99),
        ("Robot Kit", 39.99, 299.99),
        ("Musical Instrument", 19.99, 399.99),
        ("Sports Equipment", 14.99, 199.99),
        ("Outdoor Toy", 19.99, 299.99),
        ("Water Toy", 9.99, 99.99),
        ("Bath Toy", 5.99, 39.99),
        ("Educational Toy", 14.99, 129.99),
        ("Baby Toy", 7.99, 59.99),
        ("Toddler Toy", 9.99, 79.99),
        ("Pretend Play Set", 19.99, 149.99),
        ("Video Game", 29.99, 69.99),
        ("Gaming Console", 199.99, 599.99),
        ("Game Controller", 39.99, 199.99),
        ("Gaming Headset", 39.99, 299.99),
    ]
    
    brands_toys = ["LEGO", "Mattel", "Hasbro", "Fisher-Price", "Melissa & Doug", "VTech", "LeapFrog", "Playmobil", "Hot Wheels", "Barbie", "Nerf", "Play-Doh", "Crayola", "Ravensburger", "Spin Master", "Nintendo", "PlayStation", "Xbox", "Funko", "Disney"]
    
    for i in range(75):
        item = random.choice(toys)
        brand = random.choice(brands_toys)
        
        products.append({
            "name": f"{brand} {item[0]} {random.choice(['Set', 'Collection', 'Pack', 'Bundle', 'Edition', 'Series', 'Deluxe', 'Ultimate', 'Premium', 'Classic'])}",
            "price": round(random.uniform(item[1], item[2]), 2),
            "image_url": f"https://picsum.photos/seed/{8000+i}/800/600",
            "description": f"Fun and engaging {item[0].lower()} perfect for kids of all ages. Encourages creativity, imagination, and learning through play. Safe, durable, and high-quality."
        })
    
    # Outdoor & Garden (50 products)
    outdoor = [
        ("Garden Hose", 19.99, 99.99),
        ("Sprinkler", 9.99, 79.99),
        ("Garden Tool Set", 24.99, 199.99),
        ("Lawn Mower", 149.99, 1999.99),
        ("Trimmer", 49.99, 399.99),
        ("Leaf Blower", 49.99, 499.99),
        ("Pressure Washer", 99.99, 799.99),
        ("Grill", 99.99, 1999.99),
        ("Smoker", 149.99, 1499.99),
        ("Fire Pit", 79.99, 999.99),
        ("Patio Furniture Set", 199.99, 2999.99),
        ("Hammock", 29.99, 299.99),
        ("Camping Tent", 49.99, 799.99),
        ("Sleeping Bag", 29.99, 299.99),
        ("Camping Chair", 19.99, 149.99),
        ("Cooler", 24.99, 499.99),
        ("Hiking Backpack", 39.99, 399.99),
        ("Trekking Poles", 19.99, 149.99),
        ("Bike", 199.99, 3999.99),
        ("Bike Helmet", 24.99, 199.99),
        ("Bike Lock", 14.99, 99.99),
        ("Skateboard", 49.99, 299.99),
        ("Scooter", 39.99, 599.99),
        ("Fishing Rod", 29.99, 499.99),
        ("Tackle Box", 19.99, 149.99),
    ]
    
    brands_outdoor = ["Weber", "Traeger", "Coleman", "Yeti", "Igloo", "Black+Decker", "Greenworks", "Sun Joe", "Ryobi", "DeWalt", "Craftsman", "Toro", "Husqvarna", "Honda", "Trek", "Schwinn", "Mongoose", "Osprey", "Deuter", "REI"]
    
    for i in range(50):
        item = random.choice(outdoor)
        brand = random.choice(brands_outdoor)
        
        products.append({
            "name": f"{brand} {item[0]} {random.choice(['Pro', 'Elite', 'Deluxe', 'Premium', 'Heavy-Duty', 'Portable', 'Compact', 'Professional', 'Advanced', 'Ultimate'])}",
            "price": round(random.uniform(item[1], item[2]), 2),
            "image_url": f"https://picsum.photos/seed/{9000+i}/800/600",
            "description": f"Durable {item[0].lower()} built for outdoor enthusiasts. Weather-resistant, reliable, and designed to withstand harsh conditions while delivering exceptional performance."
        })
    
    # Baby & Kids (50 products)
    baby = [
        ("Baby Stroller", 99.99, 1299.99),
        ("Car Seat", 79.99, 599.99),
        ("High Chair", 49.99, 399.99),
        ("Baby Monitor", 39.99, 399.99),
        ("Baby Carrier", 29.99, 299.99),
        ("Diaper Bag", 24.99, 199.99),
        ("Crib", 149.99, 1499.99),
        ("Changing Table", 79.99, 599.99),
        ("Baby Swing", 79.99, 299.99),
        ("Bouncer", 39.99, 199.99),
        ("Play Mat", 29.99, 199.99),
        ("Baby Bathtub", 14.99, 99.99),
        ("Bottle Set", 14.99, 79.99),
        ("Breast Pump", 79.99, 499.99),
        ("Baby Blanket", 12.99, 79.99),
        ("Pacifier Set", 5.99, 29.99),
        ("Teething Toy", 7.99, 39.99),
        ("Baby Clothes Set", 19.99, 99.99),
        ("Baby Shoes", 14.99, 59.99),
        ("Nursery Decor", 14.99, 199.99),
        ("Night Light", 9.99, 79.99),
        ("Sound Machine", 19.99, 99.99),
        ("Thermometer", 9.99, 79.99),
        ("Humidifier", 24.99, 199.99),
        ("Baby Gate", 29.99, 199.99),
    ]
    
    brands_baby = ["Graco", "Chicco", "Baby Jogger", "UPPAbaby", "Britax", "Evenflo", "Fisher-Price", "Skip Hop", "Pampers", "Huggies", "Johnson's", "Aveeno Baby", "Gerber", "Carter's", "OshKosh", "Philips Avent", "Medela", "NoseFrida", "Owlet", "Halo"]
    
    for i in range(50):
        item = random.choice(baby)
        brand = random.choice(brands_baby)
        
        products.append({
            "name": f"{brand} {item[0]} {random.choice(['Deluxe', 'Premium', 'Safety', 'Comfort', 'Travel', 'Convertible', 'All-in-One', 'Essential', 'Complete', 'Advanced'])}",
            "price": round(random.uniform(item[1], item[2]), 2),
            "image_url": f"https://picsum.photos/seed/{10000+i}/800/600",
            "description": f"Safe and reliable {item[0].lower()} designed with baby's comfort in mind. Meets all safety standards and provides parents peace of mind with quality construction."
        })
    
    return products

def add_products_to_database(products):
    """Add all products to the database with progress tracking"""
    successful = 0
    failed = 0
    
    print(f"{'='*80}")
    print(f"Starting to add {len(products)} products to your database...")
    print(f"{'='*80}\n")
    
    start_time = time.time()
    
    for i, product in enumerate(products, 1):
        try:
            response = requests.post(url, data=product, auth=auth, timeout=10)
            
            if response.status_code in [200, 201]:
                successful += 1
                status = "✓"
            else:
                failed += 1
                status = f"✗ ({response.status_code})"
            
            # Print progress every 50 products
            if i % 50 == 0:
                elapsed = time.time() - start_time
                rate = i / elapsed
                remaining = (len(products) - i) / rate
                print(f"[{i}/{len(products)}] {status} | Success: {successful} | Failed: {failed} | ETA: {int(remaining)}s")
            
            # Small delay to avoid overwhelming server
            time.sleep(0.05)
            
        except Exception as e:
            failed += 1
            if i % 50 == 0:
                print(f"[{i}/{len(products)}] ✗ Error: {str(e)[:50]}")
    
    elapsed = time.time() - start_time
    
    print(f"\n{'='*80}")
    print(f"COMPLETED IN {int(elapsed)} SECONDS!")
    print(f"{'='*80}")
    print(f"✓ Successfully added: {successful} products")
    print(f"✗ Failed: {failed} products")
    print(f"📊 Success rate: {(successful/len(products)*100):.1f}%")
    print(f"{'='*80}\n")
    
    if failed > 0:
        retry = input("Would you like to retry failed products? (y/n): ")
        if retry.lower() == 'y':
            print("Retry functionality would go here...")

if __name__ == "__main__":
    print("\n🚀 Product Database Populator")
    print("="*80)
    
    # Generate all products
    print("📦 Generating 1000 realistic products...")
    all_products = generate_products()
    print(f"✓ Generated {len(all_products)} products across multiple categories\n")
    
    # Confirm before proceeding
    print("Categories included:")
    print("  - Electronics (150)")
    print("  - Home & Kitchen (150)")
    print("  - Fashion & Apparel (150)")    
    print("  - Sports & Fitness (100)")
    print("  - Beauty & Personal Care (100)")
    print("  - Home Decor & Furniture (100)")
    print("  - Books & Media (75)")
    print("  - Toys & Games (75)")
    print("  - Outdoor & Garden (50)")
    print("  - Baby & Kids (50)")
    print(f"\nTotal: {len(all_products)} products\n")
    
    proceed = input("Ready to add all products to database? (y/n): ")
    
    if proceed.lower() == 'y':
        add_products_to_database(all_products)
    else:
        print("\n❌ Operation cancelled.")

