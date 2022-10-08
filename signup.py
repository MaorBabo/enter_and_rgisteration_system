import json

# Username errors:
USERLENGTHERROR = "not enough characters.\n\nPlease enter at least 4 characters."
USERALREADYEXISTERROR = "This username is taken.\n\nPlease enter a new one."
USERINVALIDCHARSERROR = "Invalid user characters.\n\nPlease use English letters/numbers/signs like '!, @, $, ...'"
NOTEXISTMESSAGE = "This user is not exist.\n\nPlease try aging."

# Password errors:
PASSLENGTHERROR = "not enough characters.\n\nPlease enter at least 8 characters."
PASSALREADYEXISTERROR = "This password is taken.\n\nPlease enter a new one."
PASSINVALIDCHARSERROR = "Invalid password characters.\n\nPlease use English letters/numbers/signs like '!, @, $, ...'"
NUMBERSERROR = "Password need to contain at least 4 numbers.\n\nPlease enter the password correctly."

# Success message:
SUCCESS = "Registration complete successfully!"
DELETED = "Your account has ben deleted."


class UserNamePassword:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def checkUser(self):
        """
        This method checks that the user is valid.
        :return: str
        """

        with open('signup_data_base.json') as f:
            currentData = json.load(f)

        # Checks the length
        if len(self.username) < 4:
            return USERLENGTHERROR

        # Checks if already exist
        for user in currentData["users"]:
            if user["userName"] == self.username:
                return USERALREADYEXISTERROR

        # Checks if characters are valid
        for char in self.username:
            if ord(char) < 48 or 90 < ord(char) < 65 or 90 < ord(char) < 97 or ord(char) > 122:
                return USERINVALIDCHARSERROR

        return True

    def checkPassword(self):
        """
        This method checks that the password is valid.
        :return: str
        """
        # Count the digits:
        counter = 0

        # Open json file:
        with open('signup_data_base.json') as f:
            currentData = json.load(f)

        # Checks the length
        if len(self.password) < 8:
            return PASSLENGTHERROR

        # Checks if already exist
        for user in currentData["users"]:
            if user["password"] == self.password:
                return PASSALREADYEXISTERROR

        # Checks if characters are valid
        for char in self.password:
            if ord(char) < 48 or 90 < ord(char) < 65 or 90 < ord(char) < 97 or ord(char) > 122:
                return PASSINVALIDCHARSERROR

            if 48 <= ord(char) <= 57:
                counter += 1

        if counter < 4:
            return NUMBERSERROR

        return True

    def setUserAndPassword(self):
        """
        this method load the data to a json file
        :return: None
        """
        if self.checkUser() is not True:
            return self.checkUser()

        elif self.checkPassword() is not True:
            return self.checkPassword()

        else:
            with open('signup_data_base.json') as f:
                currentData = json.load(f)

            data = {
                "userName": self.username,
                "password": self.password
            }

            currentData["users"].append(data)

            with open('signup_data_base.json', 'w') as f:
                json.dump(currentData, f, indent=2)

            return SUCCESS

    def delete(self, username, password):
        """
        Deleting the user and password.
        :return: None
        """

        with open('signup_data_base.json') as f:
            currentData = json.load(f)

        for index, user in enumerate(currentData["users"]):

            if user["userName"] == username and user["password"] == password:
                currentData["users"].pop(index)

                with open('signup_data_base.json', 'w') as f:
                    json.dump(currentData, f, indent=2)
                return DELETED

        return NOTEXISTMESSAGE

    def changeUserAndPassword(self, username, password):
        self.username = username
        self.password = password


