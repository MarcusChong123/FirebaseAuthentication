import pyrebase

config = {
    "apiKey": "yourapikey",
    "authDomain": "yourauthdomain",
    "databaseURL": "yourdatabaseURL",
    "projectId": "yourprojectid",
    "storageBucket": "yourstoragebucket",
    "messagingSenderId": "yourmessagingsenderid",
    "appId": "yourappID"

}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# Create user
email = "youremail@gmail.com"
password = "yourpassword"
auth.create_user_with_email_and_password(email, password)

# Sign in
user = auth.sign_in_with_email_and_password(email, password)
# print(user)
# print(user['idToken'])

# Get account information
info = auth.get_account_info(user['idToken'])

# Verify email
auth.send_email_verification(user['idToken'])

# Reset email
auth.send_password_reset_email(email)

# Delete account
auth.delete_user_account(user['idToken'])

# # Before 1 hour expiry
user = auth.refresh(user['refreshToken'])
print(user['idToken'])