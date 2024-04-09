from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["grammar_checker"]
collection = db["results"]

def store_results(original_passage, fixed_passage, error_analysis):
    document = {
        "original_passage": original_passage,
        "fixed_passage": fixed_passage,
        "error_analysis": error_analysis,
    }
    collection.insert_one(document)