import os
from endee_client import EndeeClient

DOCS_FOLDER = "data/docs"
TRACK_FILE = "uploaded_docs.txt"


def get_uploaded_docs():
    if not os.path.exists(TRACK_FILE):
        return set()
    with open(TRACK_FILE, "r") as f:
        return set(line.strip() for line in f)


def mark_doc_uploaded(filename):
    with open(TRACK_FILE, "a") as f:
        f.write(filename + "\n")


def ingest_documents():
    uploaded_docs = get_uploaded_docs()
    client = EndeeClient()

    for filename in os.listdir(DOCS_FOLDER):

        if filename in uploaded_docs:
            print(f"Skipping: {filename}")
            continue

        file_path = os.path.join(DOCS_FOLDER, filename)
        if not os.path.isfile(file_path):
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Store document in Endee (vector DB abstraction)
        client.add_document(
            text=content,
            metadata={"source": filename}
        )

        mark_doc_uploaded(filename)
        print(f"Stored in Endee: {filename}")


if __name__ == "__main__":
    ingest_documents()
