import requests
import time

base_url = "http://127.0.0.1:5000"
auth = ("Om", "om")

def get_all_products():
    """Fetch all products from the database"""
    print("📋 Fetching all products...")
    
    all_products = []
    page = 1
    
    while True:
        try:
            response = requests.get(
                f"{base_url}/api/products",
                params={'page': page, 'per_page': 100},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                products = data.get('products', [])
                
                if not products:
                    break
                
                all_products.extend(products)
                
                if page >= data.get('pages', 1):
                    break
                
                page += 1
            else:
                print(f"❌ Error fetching products: {response.status_code}")
                break
                
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            break
    
    return all_products

def show_products_by_id_range(products):
    """Show products grouped by ID ranges"""
    if not products:
        print("No products found!")
        return
    
    # Sort by ID
    products_sorted = sorted(products, key=lambda x: x['id'])
    
    min_id = products_sorted[0]['id']
    max_id = products_sorted[-1]['id']
    
    print(f"\n{'='*80}")
    print(f"📊 PRODUCT DATABASE OVERVIEW")
    print(f"{'='*80}")
    print(f"Total Products: {len(products)}")
    print(f"ID Range: {min_id} to {max_id}")
    print(f"{'='*80}\n")
    
    # Show first 10 products
    print("📌 FIRST 10 PRODUCTS (Your original products):")
    print("-" * 80)
    for p in products_sorted[:10]:
        print(f"  ID {p['id']:4d} | ${p['price']:8.2f} | {p['name'][:55]}")
    
    print("\n...")
    
    # Show last 10 products
    print("\n📌 LAST 10 PRODUCTS (Recently added):")
    print("-" * 80)
    for p in products_sorted[-10:]:
        print(f"  ID {p['id']:4d} | ${p['price']:8.2f} | {p['name'][:55]}")
    
    print(f"\n{'='*80}\n")
    
    return products_sorted

def delete_by_id_range(start_id, end_id):
    """Delete products within a specific ID range"""
    product_ids = list(range(start_id, end_id + 1))
    
    batch_size = 50
    total_deleted = 0
    failed = 0
    
    print(f"\n🗑️  Deleting products from ID {start_id} to {end_id}...")
    print(f"Total to delete: {len(product_ids)} products\n")
    
    start_time = time.time()
    
    for i in range(0, len(product_ids), batch_size):
        batch = product_ids[i:i+batch_size]
        
        try:
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
                failed += len(batch) - deleted
                
                progress = min(100, ((i + len(batch)) / len(product_ids)) * 100)
                print(f"  [{progress:5.1f}%] Batch {i//batch_size + 1}: ✓ Deleted {deleted}/{len(batch)}")
            else:
                failed += len(batch)
                print(f"  Batch {i//batch_size + 1}: ✗ Failed ({response.status_code})")
            
            time.sleep(0.1)
            
        except Exception as e:
            failed += len(batch)
            print(f"  Batch {i//batch_size + 1}: ✗ Error - {str(e)[:50]}")
    
    elapsed = time.time() - start_time
    
    print(f"\n{'='*80}")
    print(f"✓ Deletion Complete!")
    print(f"{'='*80}")
    print(f"Successfully deleted: {total_deleted} products")
    print(f"Failed: {failed} products")
    print(f"Time taken: {int(elapsed)} seconds")
    print(f"{'='*80}\n")

def main():
    print("\n" + "="*80)
    print("🛡️  SAFE PRODUCT DELETION TOOL")
    print("="*80)
    print("This tool helps you delete only the products you want to remove.")
    print("Your existing products will NOT be touched unless you specify them.")
    print("="*80 + "\n")
    
    # Fetch all products
    products = get_all_products()
    
    if not products:
        print("❌ No products found or error fetching products")
        return
    
    # Show overview
    products_sorted = show_products_by_id_range(products)
    
    # Interactive menu
    while True:
        print("\n📋 OPTIONS:")
        print("1. Show products in a specific ID range")
        print("2. Delete products by ID range")
        print("3. Show all product IDs and names")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            # Show specific range
            try:
                start = int(input("Enter start ID: ").strip())
                end = int(input("Enter end ID: ").strip())
                
                print(f"\n📋 Products from ID {start} to {end}:")
                print("-" * 80)
                
                filtered = [p for p in products_sorted if start <= p['id'] <= end]
                
                if filtered:
                    for p in filtered:
                        print(f"  ID {p['id']:4d} | ${p['price']:8.2f} | {p['name'][:55]}")
                    print(f"\nTotal: {len(filtered)} products")
                else:
                    print("No products found in this range")
                    
            except ValueError:
                print("❌ Invalid input. Please enter numbers only.")
        
        elif choice == "2":
            # Delete by range
            print("\n⚠️  DELETE PRODUCTS BY ID RANGE")
            print("-" * 80)
            print("❗ This will permanently delete products!")
            print("❗ Make sure you've verified the ID range first (use option 1)")
            print("-" * 80)
            
            try:
                start = int(input("\nEnter START ID to delete: ").strip())
                end = int(input("Enter END ID to delete: ").strip())
                
                # Show what will be deleted
                to_delete = [p for p in products_sorted if start <= p['id'] <= end]
                
                if not to_delete:
                    print(f"\n❌ No products found in ID range {start} to {end}")
                    continue
                
                print(f"\n⚠️  You are about to delete {len(to_delete)} products:")
                print("-" * 80)
                
                # Show first 5 and last 5
                for p in to_delete[:5]:
                    print(f"  ID {p['id']:4d} | {p['name'][:60]}")
                
                if len(to_delete) > 10:
                    print(f"  ... and {len(to_delete) - 10} more ...")
                
                if len(to_delete) > 5:
                    for p in to_delete[-5:]:
                        print(f"  ID {p['id']:4d} | {p['name'][:60]}")
                
                print("-" * 80)
                confirm = input(f"\nType 'DELETE {len(to_delete)}' to confirm: ").strip()
                
                if confirm == f"DELETE {len(to_delete)}":
                    delete_by_id_range(start, end)
                    
                    # Refresh product list
                    print("\n🔄 Refreshing product list...")
                    products = get_all_products()
                    products_sorted = sorted(products, key=lambda x: x['id'])
                else:
                    print("\n❌ Deletion cancelled")
                    
            except ValueError:
                print("❌ Invalid input. Please enter numbers only.")
        
        elif choice == "3":
            # Show all products
            print(f"\n📋 ALL PRODUCTS ({len(products_sorted)} total):")
            print("=" * 80)
            
            for i, p in enumerate(products_sorted, 1):
                print(f"{i:4d}. ID {p['id']:4d} | ${p['price']:8.2f} | {p['name'][:52]}")
                
                # Pause every 20 products
                if i % 20 == 0 and i < len(products_sorted):
                    more = input(f"\nShowing {i}/{len(products_sorted)}. Press Enter to continue or 'q' to stop: ")
                    if more.lower() == 'q':
                        break
            
            print("\n" + "=" * 80)
        
        elif choice == "4":
            print("\n👋 Goodbye!")
            break
        
        else:
            print("\n❌ Invalid choice")



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
