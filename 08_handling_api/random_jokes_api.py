import requests

def get_random_jokes():
    response = requests.get("https://api.freeapi.app/api/v1/public/randomjokes/100")
    data = response.json()

    if data["success"] and "data" in data:
        joke_data = data["data"]
        joke = joke_data["content"]
        return joke
    
    else:
        raise Exception("failed to fetch data!")
    

def main():
    try:
        joke_sentence = get_random_jokes()
        print(f"\n {joke_sentence}")
    except Exception as e:
        print(str(e))
      



if __name__ == "__main__":
    main()

