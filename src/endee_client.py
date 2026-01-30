# endee_client.py

class EndeeClient:
    def __init__(self):
       
        self.documents = []

    def add_document(self, text, metadata):
        self.documents.append({
            "text": text,
            "metadata": metadata
        })

    def search(self, query):
        # Simulated semantic match (placeholder)
        for doc in self.documents:
            return doc
        return None
