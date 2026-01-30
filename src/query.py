import os
from endee_client import EndeeClient
from groq_client import ask_groq

DOCS_FOLDER = "data/docs"


def load_documents_into_endee():
    client = EndeeClient()

    for filename in os.listdir(DOCS_FOLDER):
        file_path = os.path.join(DOCS_FOLDER, filename)
        if not os.path.isfile(file_path):
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        client.add_document(
            text=content,
            metadata={"source": filename}
        )

    return client


if __name__ == "__main__":
    question = input("Ask a question: ")

    endee_client = load_documents_into_endee()
    result = endee_client.search(question)

    if not result:
        print("No relevant information found.")
    else:
        answer = ask_groq(result["text"], question)
        print("\nAnswer:")
        print(answer)
        print("\nSource:", result["metadata"]["source"])
