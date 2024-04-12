from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from app_config import MONGODB_URI

uri = MONGODB_URI
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='X509-cert-4588623656805667932.pem',
                     server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["Project4"]
collection = db["GrammarCheck"]

def store_results(original_passage, fixed_passage, error_analysis, api_response):
    document = {
        "original_passage": original_passage,
        "fixed_passage": fixed_passage,
        "error_analysis": error_analysis,
        "api_response": api_response
    }
    collection.insert_one(document)