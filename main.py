# main.py
from pymongo import MongoClient
import config

# Connect to MongoDB
client = MongoClient(config.MONGO_URI)
db = client[config.DB_NAME]
users = db['users']

# Create a new user
def create_user(username, email, age, friends):
    new_user = {
        "username": username,
        "email": email,
        "age": age,
        "friends": friends
    }
    users.insert_one(new_user)
    print(f"User {username} created.")

# Read a user
def read_user(username):
    user = users.find_one({"username": username})
    print(user)

# Update a user
def update_user(username, age):
    users.update_one(
        {"username": username},
        {"$set": {"age": age}}
    )
    print(f"User {username} updated.")

# Delete a user
def delete_user(username):
    users.delete_one({"username": username})
    print(f"User {username} deleted.")

if __name__ == "__main__":
    # Example usage
    create_user("johndoe", "johndoe@example.com", 30, ["janedoe", "alice", "bob"])
    read_user("johndoe")
    update_user("johndoe", 31)
    delete_user("johndoe")
