import requests

def fetch_random_user_api():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        city = user_data["location"]["city"]

        return username, city
    else:
        raise Exception("failed to fetch user data")
    


def main():
    try:
        username, city = fetch_random_user_api()
        print(f"Username: {username} \ncity: {city}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

