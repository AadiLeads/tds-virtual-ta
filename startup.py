from init_db import populate_database
from insert_embeddings import insert_embeddings

if __name__ == "__main__":
    print("🌱 Populating DB...")
    populate_database()
    print("✅ Done.")

    print("⚙️ Inserting embeddings...")
    insert_embeddings()
    print("✅ Embeddings ready.")

