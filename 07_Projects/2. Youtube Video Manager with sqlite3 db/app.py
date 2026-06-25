
# ====================== DATABASE SETUP =======================================================================================
#creating db if not exist and then connection to it

import sqlite3
conn = sqlite3.connect("videos.db")

# creating cursor object

cursor = conn.cursor()

# creating database table with name videos

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

# ====================== HELPER FUNCTIONS ====================================================================================

def display():
    cursor.execute("SELECT * FROM videos") 
    for row in cursor.fetchall():
        print("Displaying all saved video details: ")
        print(row)

#-----------------------------------------------------------------------------------------------------------------------------

def add(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print(f"✅ Video added successfully!")

#-----------------------------------------------------------------------------------------------------------------------------


def update(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name,new_time,video_id))
    conn.commit()
    print(f"✅ Video updated successfully!")

#-----------------------------------------------------------------------------------------------------------------------------


def delete(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()
    print(f"🗑️  Video deleted successfully!")
    

# ====================== MAIN MENU ========================================================================================

def main():
    
    while True:
        print("\n")
        print("Youtube Video Manager | sqlite3 db | Enter an option  ")
        print("1. List all the saved details ")
        print("2. Add Videos")
        print("3. Update Video details")
        print("4. Delete a video")
        print("5. Exit the app")
        
        choice = input("Enter the choice: ")

        match choice:
            case '1':
                display()
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter the video duration: ")
                add(name, time)
            case '3':
                video_id = input("Enter the video id to UPDATE: ")
                name = input("Enter the video name (new): ")
                time = input("Enter the video duration (new): ")
                update(video_id, name, time)
            case '4':
                video_id = input("Enter the video id to DELETE: ")
                delete(video_id)
            case '5': 
                print("bye bye !!")
                break
            case _:
                print("Invalid Choice Entered!!")
    conn.close()

if __name__ == "__main__":
    main()




