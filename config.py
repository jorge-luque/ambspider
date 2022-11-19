import firebase_admin

def init_firebase():
    cred = firebase_admin.credentials.Certificate("firebase_config.json")
    app = firebase_admin.initialize_app(cred)
