import json

SUCCESS = "you signed in successfully!"
FAILURE = "This user are not exist! \n\n Please check your details."


class SignIn:
    with open('signup_data_base.json') as f:
        currentData = json.load(f)

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def checkIfExist(self):
        """
        Checks if the user exist in the system.
        :return: bool(True/False)
        """
        for user in self.currentData["users"]:
            if user["userName"] == self.user:
                return True

        return False

    def setUserActive(self):
        """
        Set the user in activate mode.
        :return: None
        """
        if not self.checkIfExist():
            return FAILURE

        with open('sign_in_data_base.json') as f:
            currentData = json.load(f)

        data = {
            "userName": self.user
        }

        currentData["active"].append(data)

        with open('sign_in_data_base.json', 'w') as f:
            json.dump(currentData, f, indent=2)

        return SUCCESS
