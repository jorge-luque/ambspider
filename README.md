# Install a virtual environment
```sh
virtualenv venv
```

# Set the virtual environment as source
```sh
source venv/bin/activate
```

# Install dependencies
```sh
pip install -r requirements.txt
````

You need to create the file firebase_config.json in the root of the project.
In that file, you need to configure the credentials to connect to firebase
I.e.

```json
{
  "type": "service_account",
  "project_id": "your_project_id",
  "private_key_id": "your_private_key_id",
  "private_key": "the_encrypted_key",
  "client_email": "client_email",
  "client_id": "your_client_id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "your_client_x509_cert_url"
}
```

# Run program
```sh
python main.pu
```

You may want to configure some environment variables:
- DELAY_SECONDS (default: 30000 seconds - 5 minutes)
- MAX_RETRIES (default: 10)