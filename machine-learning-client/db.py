from pymongo import MongoClient
from app_config import MONGODB_URI

client = MongoClient(MONGODB_URI)
db = client["Project4"]
collection = db["GrammarCheck"]

def store_results(original_passage, fixed_passage, error_analysis):
    document = {
        "original_passage": original_passage,
        "fixed_passage": fixed_passage,
        "error_analysis": error_analysis,
    }
    collection.insert_one(document)