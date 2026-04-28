import requests
import time

url = "http://127.0.0.1:500 0/api/admin/add"
auth = ("Om", "om")

products = [
    {"name": "Sony WH-1000XM5 Wireless Headphones", "price": 349.99, "image_url": "https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb", "description": "Industry-leading noise cancellation with premium sound quality and 30-hour battery life."},
    {"name": "Apple AirPods Pro 2nd Gen", "price": 249.00, "image_url": "https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7", "description": "Active noise cancellation, spatial audio, and sweat-resistant design."},
    {"name": "Samsung Galaxy S24 Ultra", "price": 1199.99, "image_url": "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c", "description": "Flagship smartphone with 200MP camera, S Pen, and powerful AI features."},
    {"name": "iPad Air 11-inch M2", "price": 599.00, "image_url": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0", "description": "Powerful tablet with M2 chip, perfect for creativity and productivity."},
    {"name": "MacBook Air M3 15-inch", "price": 1299.00, "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8", "description": "Thin, lightweight laptop with breakthrough performance and all-day battery."},
    {"name": "Dell XPS 13 Plus", "price": 1099.00, "image_url": "https://images.unsplash.com/photo-1593642632823-8f785ba67e45", "description": "Premium ultrabook with stunning InfinityEdge display."},
    {"name": "Logitech MX Master 3S", "price": 99.99, "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46", "description": "Advanced wireless mouse with ultra-fast scrolling."},
    {"name": "Mechanical Keyboard RGB", "price": 79.99, "image_url": "https://images.unsplash.com/photo-1595225476474-87563907a212", "description": "Gaming keyboard with Cherry MX switches and RGB lighting."},
    {"name": "LG 27-inch 4K Monitor", "price": 449.00, "image_url": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf", "description": "Ultra HD IPS display with HDR10 support."},
    {"name": "Anker PowerBank 20000mAh", "price": 45.99, "image_url": "https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5", "description": "High-capacity portable charger with fast charging."},
    {"name": "Instant Pot Duo 7-in-1", "price": 89.99, "image_url": "https://images.unsplash.com/photo-1585515320310-259814833e62", "description": "Multi-functional pressure cooker and slow cooker."},
    {"name": "Ninja Air Fryer Pro", "price": 119.99, "image_url": "https://images.unsplash.com/photo-1634506963038-167c1da66d99", "description": "Large capacity air fryer with 6 cooking functions."},
    {"name": "Dyson V15 Detect Vacuum", "price": 649.99, "image_url": "https://images.unsplash.com/photo-1558317374-067fb5f30001", "description": "Powerful cordless vacuum with laser detection."},
    {"name": "KitchenAid Stand Mixer", "price": 379.99, "image_url": "https://images.unsplash.com/photo-1578991171710-f5c6e4e98ac3", "description": "Professional-grade stand mixer with 10 speeds."},
    {"name": "Breville Barista Express", "price": 699.95, "image_url": "https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6", "description": "All-in-one espresso machine with built-in grinder."},
    {"name": "Nespresso Vertuo Next", "price": 179.00, "image_url": "https://images.unsplash.com/photo-1556740749-887f6717d7e4", "description": "Smart coffee maker with one-touch brewing."},
    {"name": "Cuisinart Food Processor", "price": 199.99, "image_url": "https://images.unsplash.com/photo-1621261207758-5f585ce09fc1", "description": "Powerful 14-cup food processor for chopping and slicing."},
    {"name": "Le Creuset Dutch Oven", "price": 379.95, "image_url": "https://images.unsplash.com/photo-1584990347449-7c386a426b4f", "description": "Enameled cast iron cookware for braising and roasting."},
    {"name": "All-Clad Cookware Set", "price": 599.99, "image_url": "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136", "description": "Professional 10-piece stainless steel cookware set."},
    {"name": "Philips Hue Smart Bulbs", "price": 149.99, "image_url": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64", "description": "Color-changing smart light bulbs 4-pack."},
    {"name": "Levi's 501 Original Jeans", "price": 69.50, "image_url": "https://images.unsplash.com/photo-1542272604-787c3835535d", "description": "Classic straight-leg jeans with button fly."},
    {"name": "Nike Air Max 270", "price": 150.00, "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff", "description": "Iconic running shoes with Max Air cushioning."},
    {"name": "Adidas Ultraboost 22", "price": 190.00, "image_url": "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa", "description": "High-performance running shoes with Boost cushioning."},
    {"name": "North Face Thermoball Jacket", "price": 199.00, "image_url": "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3", "description": "Lightweight insulated jacket for cold weather."},
    {"name": "Patagonia Better Sweater", "price": 139.00, "image_url": "https://images.unsplash.com/photo-1556821840-3a63f95609a7", "description": "Cozy fleece jacket made from recycled polyester."},
    {"name": "Ray-Ban Aviator Sunglasses", "price": 168.00, "image_url": "https://images.unsplash.com/photo-1511499767150-a48a237f0083", "description": "Timeless aviator sunglasses with gold frames."},
    {"name": "Casio G-Shock Watch", "price": 99.00, "image_url": "https://images.unsplash.com/photo-1523170335258-f5ed11844a49", "description": "Shock-resistant sport watch with 200m water resistance."},
    {"name": "Tommy Hilfiger Polo Shirt", "price": 59.50, "image_url": "https://images.unsplash.com/photo-1586363104862-3a5e2ab60d99", "description": "Classic cotton polo with signature flag logo."},
    {"name": "Columbia Hiking Boots", "price": 129.99, "image_url": "https://images.unsplash.com/photo-1520639888713-7851133b1ed0", "description": "Waterproof hiking boots with advanced traction."},
    {"name": "Carhartt Work Jacket", "price": 89.99, "image_url": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea", "description": "Durable canvas work jacket with quilted lining."},
    {"name": "Yoga Mat Premium", "price": 34.99, "image_url": "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f", "description": "Extra thick non-slip yoga mat with eco-friendly materials."},
    {"name": "Bowflex Adjustable Dumbbells", "price": 349.00, "image_url": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438", "description": "Space-saving adjustable dumbbells up to 52.5 lbs."},
    {"name": "Peloton Bike+", "price": 2495.00, "image_url": "https://images.unsplash.com/photo-1594737626072-90dc274bc2bc", "description": "Premium indoor cycling bike with rotating touchscreen."},
    {"name": "TRX Suspension Training", "price": 169.95, "image_url": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438", "description": "Complete bodyweight training system for home workouts."},
    {"name": "Fitbit Charge 6", "price": 159.95, "image_url": "https://images.unsplash.com/photo-1557935728-e6d1eaabe558", "description": "Advanced fitness tracker with heart rate and GPS."},
    {"name": "Resistance Bands Set", "price": 24.99, "image_url": "https://images.unsplash.com/photo-1598289431512-b97b0917affc", "description": "5-piece resistance band set for strength training."},
    {"name": "Foam Roller Pro", "price": 29.99, "image_url": "https://images.unsplash.com/photo-1611672585731-fa10603fb9e0", "description": "High-density foam roller for muscle recovery."},
    {"name": "Jump Rope Speed Pro", "price": 19.99, "image_url": "https://images.unsplash.com/photo-1611672585731-fa10603fb9e0", "description": "Professional speed rope with ball bearings."},
    {"name": "Whey Protein Powder 5lbs", "price": 54.99, "image_url": "https://images.unsplash.com/photo-1579722820308-d74e571900a9", "description": "Premium whey protein isolate with 25g protein per serving."},
    {"name": "Hydro Flask 32oz", "price": 44.95, "image_url": "https://images.unsplash.com/photo-1602143407151-7111542de6e8", "description": "Insulated stainless steel water bottle."},
    {"name": "Atomic Habits Book", "price": 16.99, "image_url": "https://images.unsplash.com/photo-1544947950-fa07a98d237f", "description": "Bestselling book on building good habits by James Clear."},
    {"name": "Psychology of Money", "price": 14.99, "image_url": "https://images.unsplash.com/photo-1592496431122-2349e0fbc666", "description": "Timeless lessons on wealth and happiness by Morgan Housel."},
    {"name": "Kindle Paperwhite", "price": 139.99, "image_url": "https://images.unsplash.com/photo-1592496431122-2349e0fbc666", "description": "Waterproof e-reader with glare-free display."},
    {"name": "Blue Yeti USB Microphone", "price": 129.99, "image_url": "https://images.unsplash.com/photo-1590602847861-f357a9332bbc", "description": "Professional USB mic for podcasting and streaming."},
    {"name": "Bose SoundLink Speaker", "price": 149.00, "image_url": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1", "description": "Portable Bluetooth speaker with 12-hour battery."},
    {"name": "Dyson Supersonic Hair Dryer", "price": 429.99, "image_url": "https://images.unsplash.com/photo-1522338242992-e1a54906a8da", "description": "Fast-drying hair dryer with intelligent heat control."},
    {"name": "Philips Sonicare Toothbrush", "price": 99.95, "image_url": "https://images.unsplash.com/photo-1607613009820-a29f7bb81c04", "description": "Rechargeable electric toothbrush with pressure sensor."},
    {"name": "Braun Series 9 Shaver", "price": 329.99, "image_url": "https://images.unsplash.com/photo-1621607512214-68297480165e", "description": "Premium electric shaver with 5 shaving elements."},
    {"name": "CeraVe Moisturizing Cream", "price": 18.99, "image_url": "https://images.unsplash.com/photo-1556229010-aa9e79e46cc1", "description": "Dermatologist-recommended moisturizer with ceramides."},
    {"name": "The Ordinary Niacinamide", "price": 12.90, "image_url": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be", "description": "High-strength vitamin serum for clear skin."},
    {"name": "Himalayan Salt Lamp", "price": 39.99, "image_url": "https://images.unsplash.com/photo-1513506003901-1e6a229e2d15", "description": "Natural pink salt lamp for warm ambient lighting."},
    {"name": "Canvas Wall Art 3-Piece", "price": 79.99, "image_url": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38", "description": "Modern abstract artwork set for home decor."},
    {"name": "Succulent Plants Set", "price": 29.99, "image_url": "https://images.unsplash.com/photo-1459156212016-c812468e2115", "description": "6 assorted live succulents in decorative pots."},
    {"name": "Chunky Knit Throw Blanket", "price": 49.99, "image_url": "https://images.unsplash.com/photo-1582735689369-4fe89db7114c", "description": "Cozy hand-knitted blanket from soft chenille yarn."},
    {"name": "Bamboo Cutting Board", "price": 34.99, "image_url": "https://images.unsplash.com/photo-1566842600175-97dca489844f", "description": "Eco-friendly bamboo cutting board with juice groove."},
    {"name": "Knife Set 15-Piece", "price": 89.99, "image_url": "https://images.unsplash.com/photo-1593618998160-e34014e67546", "description": "Professional chef knife set with wooden block."},
    {"name": "Non-Stick Pan Set", "price": 59.99, "image_url": "https://images.unsplash.com/photo-1585515320310-259814833e62", "description": "PFOA-free non-stick frying pans in 3 sizes."},
    {"name": "Glass Storage Containers", "price": 39.99, "image_url": "https://images.unsplash.com/photo-1584308972272-9e4e7685e80f", "description": "10-piece glass container set with airtight lids."},
    {"name": "Ceramic Dinnerware Set", "price": 69.99, "image_url": "https://images.unsplash.com/photo-1610701596007-11502861dcfa", "description": "16-piece modern dinnerware set for 4 people."},
    {"name": "Stainless Utensil Set", "price": 24.99, "image_url": "https://images.unsplash.com/photo-1616486029423-aaa4789e8c9a", "description": "5-piece kitchen utensil set with holder."},
    {"name": "Weber Kettle Charcoal Grill", "price": 139.00, "image_url": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1", "description": "22-inch charcoal grill with ash catcher."},
    {"name": "Yeti Rambler 30oz", "price": 37.99, "image_url": "https://images.unsplash.com/photo-1602143407151-7111542de6e8", "description": "Vacuum insulated tumbler for hot or cold drinks."},
    {"name": "Coleman Camping Tent 6-Person", "price": 169.99, "image_url": "https://images.unsplash.com/photo-1478131143081-80f7f84ca84d", "description": "Spacious weatherproof family tent with easy setup."},
    {"name": "Sleeping Bag 0°F", "price": 79.99, "image_url": "https://images.unsplash.com/photo-1504851149312-7a075b496cc7", "description": "Mummy sleeping bag for extreme cold weather."},
    {"name": "Backpacking Backpack 65L", "price": 149.99, "image_url": "https://images.unsplash.com/photo-1622260614927-58c1e52d1d4e", "description": "Large hiking backpack with adjustable suspension."},
    {"name": "LED Camping Lantern", "price": 34.99, "image_url": "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d", "description": "Bright 1000 lumen rechargeable camping lantern."},
    {"name": "Portable Camping Stove", "price": 29.99, "image_url": "https://images.unsplash.com/photo-1504280390367-361c6d9f38f4", "description": "Compact propane stove with windscreen."},
    {"name": "Hammock with Stand", "price": 119.99, "image_url": "https://images.unsplash.com/photo-1559827260-dc66d52bef19", "description": "Double hammock with steel stand for backyard."},
    {"name": "Expandable Garden Hose", "price": 44.99, "image_url": "https://images.unsplash.com/photo-1416879595882-3373a0480b5b", "description": "100ft lightweight expanding hose with spray nozzle."},
    {"name": "Cordless Electric Mower", "price": 399.99, "image_url": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64", "description": "Battery-powered lawn mower with 20-inch cutting width."},
    {"name": "Baby Monitor with Camera", "price": 129.99, "image_url": "https://images.unsplash.com/photo-1519340333755-56e9c1d6a8b4", "description": "HD video baby monitor with night vision."},
    {"name": "Graco Convertible Car Seat", "price": 179.99, "image_url": "https://images.unsplash.com/photo-1617258683320-61900b281ced", "description": "3-in-1 car seat from infant to booster."},
    {"name": "Fisher-Price Baby Swing", "price": 149.99, "image_url": "https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4", "description": "Motorized baby swing with music and multiple speeds."},
    {"name": "Wooden Puzzle Set", "price": 24.99, "image_url": "https://images.unsplash.com/photo-1587654780291-39c9404d746b", "description": "Educational wooden puzzles for toddlers set of 3."},
    {"name": "LEGO Classic Creative Bricks", "price": 59.99, "image_url": "https://images.unsplash.com/photo-1587654780291-39c9404d746b", "description": "790-piece LEGO set with endless building possibilities."},
    {"name": "Kids Scooter 3-Wheel", "price": 1200.99, "image_url": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e", "description": "Stable kick scooter with LED light-up wheels."},
    {"name": "Children's Bookshelf", "price": 69.99, "image_url": "https://images.unsplash.com/photo-1495446815901-a7297e633e8d", "description": "Sling bookshelf with storage bins for toys."},
    {"name": "Play Kitchen Set Wooden", "price": 149.99, "image_url": "https://images.unsplash.com/photo-1566576721346-d4a3b4eaeb55", "description": "Pretend play kitchen with realistic features."},
    {"name": "Crayola Art Kit 140-Piece", "price": 34.99, "image_url": "https://images.unsplash.com/photo-1513364776144-60967b0f800f", "description": "Complete art set with crayons, markers, and pencils."},
    {"name": "Kids Digital Camera", "price": 39.99, "image_url": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32", "description": "Durable child-friendly camera with 1080p video."},
    {"name": "Samsonite Hardside Luggage", "price": 199.99, "image_url": "https://images.unsplash.com/photo-1565026057447-bc90a3dceb87", "description": "28-inch spinner suitcase with TSA lock."},
    {"name": "Swiss Army Multi-Tool", "price": 34.99, "image_url": "https://images.unsplash.com/photo-1599481238640-4c1288750d7a", "description": "15-function pocket knife with scissors and screwdrivers."},
    {"name": "Thermos Food Jar", "price": 24.99, "image_url": "https://images.unsplash.com/photo-1610824352934-c10d87b700cc", "description": "Vacuum insulated food container for hot or cold meals."},
    {"name": "Moleskine Notebook Large", "price": 22.95, "image_url": "https://images.unsplash.com/photo-1531346878377-a5be20888e57", "description": "Premium hardcover notebook with dotted pages."},
    {"name": "Pilot G2 Gel Pens 12-Pack", "price": 14.99, "image_url": "https://images.unsplash.com/photo-1585366119957-e9730b6d0f60", "description": "Smooth-writing retractable gel pens in assorted colors."},
    {"name": "Scotch Thermal Laminator", "price": 39.99, "image_url": "https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6", "description": "Fast laminating machine for documents up to 9 inches."},
    {"name": "Brother Wireless Printer", "price": 199.99, "image_url": "https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6", "description": "Color inkjet all-in-one printer with mobile printing."},
    {"name": "Ergonomic Office Chair", "price": 249.99, "image_url": "https://images.unsplash.com/photo-1580480055273-228ff5388ef8", "description": "Adjustable mesh office chair with lumbar support."},
    {"name": "Standing Desk Adjustable", "price": 349.99, "image_url": "https://images.unsplash.com/photo-1595515106969-1ce29566ff1c", "description": "Electric sit-stand desk with memory presets."},
    {"name": "Dual Monitor Mount Arm", "price": 89.99, "image_url": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf", "description": "Fully adjustable dual monitor stand for ergonomic viewing."},
    {"name": "Brita Water Filter Pitcher", "price": 34.99, "image_url": "https://images.unsplash.com/photo-1582098461444-fc46d8a51aec", "description": "Large capacity water pitcher with filter indicator."},
    {"name": "Rubbermaid Food Storage Set", "price": 29.99, "image_url": "https://images.unsplash.com/photo-1584308972272-9e4e7685e80f", "description": "42-piece BPA-free plastic container set with lids."},
    {"name": "OXO Good Grips Can Opener", "price": 24.99, "image_url": "https://images.unsplash.com/photo-1616486029423-aaa4789e8c9a", "description": "Smooth edge can opener with comfortable grip."},
    {"name": "Pyrex Glass Mixing Bowl Set", "price": 39.99, "image_url": "https://images.unsplash.com/photo-1610701596007-11502861dcfa", "description": "8-piece nesting mixing bowl set with lids."},
    {"name": "Joseph Joseph Cutting Board Set", "price": 49.99, "image_url": "https://images.unsplash.com/photo-1566842600175-97dca489844f", "description": "Color-coded cutting board set with storage case."},
    {"name": "Lodge Cast Iron Skillet 12-inch", "price": 39.99, "image_url": "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136", "description": "Pre-seasoned cast iron skillet for stovetop and oven."},
    {"name": "Calphalon Nonstick Bakeware Set", "price": 79.99, "image_url": "https://images.unsplash.com/photo-1585515320310-259814833e62", "description": "10-piece baking pan set with nonstick coating."},
    {"name": "Zojirushi Rice Cooker", "price": 189.99, "image_url": "https://images.unsplash.com/photo-1585515320310-259814833e62", "description": "Fuzzy logic rice cooker with multiple settings."},
]

print(f"Starting to add {len(products)} products...\n")

successful = 0
failed = 0

for i, product in enumerate(products, 1):
    try:
        response = requests.post(url, data=product, auth=auth, timeout=10)
        
        if response.status_code in [200, 201]:
            successful += 1
            print(f"✓ {i}/{len(products)}: {product['name'][:50]}")
        else:
            failed += 1
            print(f"✗ {i}/{len(products)}: {product['name'][:50]} - Status: {response.status_code}")
        
        time.sleep(0.05)  # Small delay to avoid overwhelming server
        
    except Exception as e:
        failed += 1
        print(f"✗ {i}/{len(products)}: {product['name'][:50]} - Error: {str(e)[:50]}")

print(f"\n{'='*70}")
print(f"COMPLETE: {successful} successful | {failed} failed out of {len(products)} total")
print(f"{'='*70}")
