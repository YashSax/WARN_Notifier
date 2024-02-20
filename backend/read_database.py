# export GOOGLE_APPLICATION_CREDENTIALS="./firebase_service_key.json"
import os
from google.cloud import firestore

def get_documents_from_firebase():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./firebase_service_key.json"
    project_id = 'warn-notices-ff163'
    db = firestore.Client(project=project_id)
    collection_name = 'users'
    collection_ref = db.collection(collection_name)
    documents = collection_ref.stream()
    return documents

if __name__ == "__main__":
    documents = get_documents_from_firebase()
    for d in documents:
        print("Example row:", d._data)