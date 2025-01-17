import json
import os

class PasswordHistory:
    def __init__(self, history_file='password_history.json'):
        self.history_file = history_file
        self.history = self.load_history()

    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r') as file:
                return json.load(file)
        return []

    def save_history(self):
        with open(self.history_file, 'w') as file:
            json.dump(self.history, file, indent=4)

    def add_password(self, password):
        self.history.append(password)
        self.save_history()

    def view_history(self):
        return self.history

# Define Password_Checking class
class Password_Checking:
    def __init__(self):
        self.password_ = []

    def check_password(self, password):
        # Add password checking logic here
        pass

# Usage in Password_Genrator class
class Password_Genrator(Password_Checking):
    def __init__(self):
        super().__init__()
        self.history = PasswordHistory()

    def Genrates_password(self):
        # Existing code...
        PP = "".join(self.password_)
        print("Password: {}".format(PP))

        # Save password to history
        self.history.add_password(PP)

        # Existing code...