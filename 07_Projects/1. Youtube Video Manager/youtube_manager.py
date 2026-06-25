import json

def load_data():
    try:
        with open('data.txt','r') as file:
            test = json.load(file)
            return test
    except:
        return []

def save_data(videos):
    with open('data.txt','w') as file:
        json.dump(videos, file) 

def display(videos):
    print("\n")
    print("*" * 50)
    for i , vid in enumerate(videos, start = 1):
        print(f"{i}. {vid['name']} | Duration: {vid['time']}")
    print("\n")
    print("*" * 50)
    

def add(videos):
    name = input("Enter the name: ")
    time = input("Enter the duration of video:")
    videos.append({'name': name,'time':time})
    save_data(videos)
    print("✅ saved sucessfully!")


def update(videos):
    display(videos)
    index = int(input("Enter the video index to be updated: "))
   
    if 1<= index <= len(videos):
        name = input("Enter the new name: ")
        time = input("Enter the new duration of video:")
        videos[index - 1] = {'name': name, 'time': time}
        save_data(videos)
        print("✅ updated successfully!")
    else:
        print("Invalid index entered! ")
   


def delete(videos):
    display(videos)
    index = int(input("Enter the video index to be deleted: "))
    if 1<= index <= len(videos):
       
        del videos[index-1]
        save_data(videos)
        print(f"✅ deleted successfully!")
    else:
        print("Invalid index entered! ")

    


def main():
    videos = load_data()
    while True:
        print("\n")
        print("Youtube Video Manager | Enter an option  ")
        print("1. List all the saved details ")
        print("2. Add Videos")
        print("3. Update Video details")
        print("4. Delete a video")
        print("5. Exit the app")
        
        choice = input("Enter the choice: ")

        match choice:
            case '1':
                display(videos)
            case '2':
                add(videos)
            case '3':
                update(videos)
            case '4':
                delete(videos)
            case '5': 
                print("bye bye !!")
                break
            case _:
                print("Invalid Choice Entered!!")

if __name__ == "__main__":
    main()

           