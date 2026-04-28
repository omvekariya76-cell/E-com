import requests

base_url = "http://127.0.0.1:5000"
auth = ("Om", "om")

print("="*80)
print("🗑️  SAFE DELETE - Remove Recently Added Products")
print("="*80)

# Get all products
print("\n📋 Fetching all products from database...")
response = requests.get(f"{base_url}/api/products?per_page=10000", timeout=10)

if response.status_code != 200:
    print(f"❌ Error fetching products: {response.status_code}")
    exit()

products = response.json()['products']
products_sorted = sorted(products, key=lambda x: x['id'])

print(f"✓ Found {len(products)} total products")
print(f"✓ ID Range: {products_sorted[0]['id']} to {products_sorted[-1]['id']}")

# Show first 10 (old products)
print("\n" + "="*80)
print("📌 FIRST 10 PRODUCTS (Your Original Products):")
print("="*80)
for p in products_sorted[:10]:
    print(f"  ID {p['id']:4d} | ${p['price']:8.2f} | {p['name'][:50]}")

# Show last 10 (recent products)
print("\n" + "="*80)
print("📌 LAST 10 PRODUCTS (Recently Added):")
print("="*80)
for p in products_sorted[-10:]:
    print(f"  ID {p['id']:4d} | ${p['price']:8.2f} | {p['name'][:50]}")

# Ask for starting ID
print("\n" + "="*80)
print("💡 Enter the ID from where you want to START deleting")
print("   (All products with this ID and higher will be deleted)")
print("="*80)

start_id = input("\nDelete from ID: ").strip()

try:
    start_id = int(start_id)
    
    # Get products to delete
    ids_to_delete = [p['id'] for p in products_sorted if p['id'] >= start_id]
    products_to_delete = [p for p in products_sorted if p['id'] >= start_id]
    
    if not ids_to_delete:
        print(f"\n❌ No products found with ID >= {start_id}")
        exit()
    
    # Show what will be deleted
    print(f"\n" + "="*80)
    print(f"⚠️  PREVIEW: {len(ids_to_delete)} products will be DELETED")
    print("="*80)
    print(f"ID Range: {min(ids_to_delete)} to {max(ids_to_delete)}")
    print("\nFirst 5 to be deleted:")
    for p in products_to_delete[:5]:
        print(f"  ✗ ID {p['id']:4d} | {p['name'][:60]}")
    
    if len(products_to_delete) > 10:
        print(f"\n  ... and {len(products_to_delete) - 10} more ...")
    
    if len(products_to_delete) > 5:
        print("\nLast 5 to be deleted:")
        for p in products_to_delete[-5:]:
            print(f"  ✗ ID {p['id']:4d} | {p['name'][:60]}")
    
    # Confirm
    print("\n" + "="*80)
    confirm = input(f"Type 'DELETE {len(ids_to_delete)}' to confirm deletion: ").strip()
    
    if confirm == f"DELETE {len(ids_to_delete)}":
        print(f"\n🗑️  Deleting {len(ids_to_delete)} products...")
        
        # Delete in batches of 100
        batch_size = 100
        total_deleted = 0
        
        for i in range(0, len(ids_to_delete), batch_size):
            batch = ids_to_delete[i:i+batch_size]
            
            response = requests.post(
                f"{base_url}/api/admin/delete_bulk",
                auth=auth,
                json={'product_ids': batch},
                headers={'Content-Type': 'application/json'},
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                deleted = result.get('deleted_count', 0)
                total_deleted += deleted
                progress = min(100, ((i + len(batch)) / len(ids_to_delete)) * 100)
                print(f"  [{progress:5.1f}%] Deleted {deleted} products")
            else:
                print(f"  ❌ Batch failed: {response.status_code}")
        
        print("\n" + "="*80)
        print(f"✅ SUCCESS! Deleted {total_deleted} products")
        print("="*80)
        
        # Show remaining products
        remaining = len(products) - total_deleted
        print(f"\n📊 Remaining products in database: {remaining}")
        
    else:
        print("\n❌ Deletion cancelled - No products were deleted")
        
except ValueError:
    print("\n❌ Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"\n❌ Error: {str(e)}")
