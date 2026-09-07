# from pydantic import BaseModel

# class items(BaseModel):
#     name : str
#     id : int


# users = []  
# #  [ { "name" : asd , "id" : }]

# def add(item : items):
#     users.append(item)
    
# def delete(id : int):
#     for item in users : 
#         if item.id == id : 
#             users.remove(item)

# def find(id : int) : 
#     for item in users : 
#             if item.id == id : 
#                return item
           
           
# a = input(" hey please enter the desired operation that you want to do")


from dataclasses import asdict, dataclass


# 1. Dataclass for structured User objects
@dataclass
class User:
    id: int
    name: str
    email: str


# 2. In-Memory User Manager using list[dict]
class UserManager:

    def __init__(self) -> None:
        # In-memory storage using list[dict]
        self.users: list[dict] = []

    def create_user(self, name: str, email: str) -> dict:
        # Auto-increment ID based on existing users
        new_id = max([u["id"] for u in self.users], default=0) + 1

        # Create user instance and convert to dict
        user_obj = User(id=new_id, name=name, email=email)
        user_dict = asdict(user_obj)

        self.users.append(user_dict)
        return user_dict

    def list_users(self) -> list[dict]:
        return self.users

    def find_user(self, user_id: int) -> dict | None:
        # List comprehension to find matching user dict
        matching = [u for u in self.users if u["id"] == user_id]
        return matching[0] if matching else None

    def delete_user(self, user_id: int) -> bool:
        initial_length = len(self.users)
        # Re-assign list excluding the target user
        self.users = [u for u in self.users if u["id"] != user_id]
        return len(self.users) < initial_length


# 3. Interactive CLI Interface
def main() -> None:
    manager = UserManager()

    while True:
        print("\n=== IN-MEMORY CLI USER MANAGER ===")
        print("1. Create User")
        print("2. List Users")
        print("3. Find User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("\nSelect an option (1-5): ").strip()

        try:
            if choice == "1":
                name = input("Enter name: ").strip()
                email = input("Enter email: ").strip()
                if not name or not email:
                    raise ValueError("Name and email cannot be empty.")
                user = manager.create_user(name, email)
                print(f"User created: {user}")

            elif choice == "2":
                users = manager.list_users()
                if not users:
                    print("No users in memory.")
                else:
                    print("\n--- Current Users ---")
                    for u in users:
                        print(
                            f"ID: {u['id']} | Name: {u['name']} | Email: {u['email']}"
                        )

            elif choice == "3":
                user_id = int(input("Enter User ID to find: "))
                user = manager.find_user(user_id)
                if user:
                    print(
                        f"\nFound User: ID {user['id']} | {user['name']} ({user['email']})"
                    )
                else:
                    print("User not found.")

            elif choice == "4":
                user_id = int(input("Enter User ID to delete: "))
                if manager.delete_user(user_id):
                    print("User deleted successfully.")
                else:
                    print("User ID not found.")

            elif choice == "5":
                print("Exiting application...")
                break

            else:
                print("Invalid choice. Please select between 1 and 5.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
