from flask import Flask
from azure.storage.blob import BlobServiceClient
import os

app = Flask(__name__)

# Azure Storage Account connection string
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = os.getenv("AZURE_CONTAINER_NAME")

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

@app.route("/")
def home():
    blobs = container_client.list_blobs()
    return f"Blobs in the container: {[blob.name for blob in blobs]}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
