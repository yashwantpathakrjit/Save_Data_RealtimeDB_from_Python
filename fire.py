import firebase_admin
from firebase_admin import credentials, db

# Initialize the Firebase Admin SDK
cred = credentials.Certificate('homeweather-ca8b9-firebase-adminsdk-1m5lo-31af22121a.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://homeweather-ca8b9-default-rtdb.firebaseio.com/'
})

# Reference to the database
ref = db.reference('/')

# Data to be saved
data = {
    'users': {
        'user_1': {
            'first_name': 'Yashwant',
            'last_name': 'Pathak',
            'age': 30
        },
        'user_2': {
            'first_name': 'Nidhi',
            'last_name': 'Pathak',
            'age': 30
        }
    }
}

# Save data to Firebase Realtime Database
ref.set(data)

print("Data saved successfully!")
