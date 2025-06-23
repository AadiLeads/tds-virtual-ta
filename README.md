# TDS Virtual TA Project

A FastAPI-based AI assistant for the IIT Madras Online BS in Data Science, designed to answer student queries using course content and forum discussions.

---

## Features

- Accepts student questions via a REST API (supports both text and optional image input)
- Utilizes Gemini (Google Generative AI) for embeddings and answer generation
- Employs a local vector store (ChromaDB/SQLite) for efficient semantic search
- Returns answers with citations and links to relevant course materials and Discourse posts
- Secure API key management using environment variables
- Automated evaluation with Promptfoo for robust, rubric-aligned responses

---

## Tech Stack

- **Python 3.9+**
- **FastAPI** for API endpoints
- **Gemini (Google Generative AI)** for embeddings and LLM responses
- **ChromaDB** and **SQLite** for vector storage and retrieval
- **aiohttp**, **requests** for async HTTP requests
- **python-dotenv** for environment management
- **Promptfoo** for YAML-based automated evaluation
- **Docker** and virtual environments for reproducibility

---

## Setup Instructions

1. **Clone the repository**
git clone https://github.com/your-username/tds-virtual-ta.git

cd tds-virtual-ta



3. **Install dependencies**

pip install -r requirements.txt



3. **Set up environment variables**

Create a `.env` file in the project root with your  API key(AIPIPE preffered)


4. **Prepare the knowledge base**
- Place your markdown course files in the `markdown_files/` directory.
- (Optional) Add Discourse data if available.

5. **Generate embeddings**
   
python embed.py


7. **Insert embeddings into the database**
   
python insert_embeddings.py



8. **Start the API server**
   
uvicorn app:app --reload --port 8000



8. **Test the API**
- Visit [http://localhost:8000/docs](http://localhost:8000/docs) for the Swagger UI.
- Or use `curl`/Postman to send POST requests to `/query`.

---

## Demo

A live demo video is available, showing real-time question answering through the Render deployment.

- **GitHub Repository:** https://github.com/AadiLeads/tds-virtual-ta
- **Live API (Render):** https://tds-virtual-ta-1-aufz.onrender.com 

---

## License

This project is licensed under the MIT License.

---

**For questions or contributions, feel free to open an issue or pull request!**
