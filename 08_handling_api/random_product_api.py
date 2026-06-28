import requests

def get_random_products():
    response = requests.get(
    "https://api.freeapi.app/api/v1/public/randomproducts",
    params={
      "page": "1",
      "limit": "10",
      "inc": "category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid",
      "query": "mens-watches"
    }
)
    
    all_data = response.json()

    if all_data["success"] and "data" in all_data:
        product_data = all_data["data"]
        product = product_data["data"][0]["category"]
        price = product_data["data"][0]["price"]
        return product, price
    else:
        raise Exception("failed to fetch data")
    
def main():
    try:
        product_name,product_price = get_random_products()
        print(f"\nProduct name: {product_name}\n Price: {product_price}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()