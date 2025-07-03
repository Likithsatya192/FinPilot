# 🌍 FinBot Financial Assistant

A Streamlit-based AI-powered financial assistant that provides real-time stock prices, mutual fund information, currency conversion, and more. The backend is powered by FastAPI and custom tools for financial data retrieval.

## Features
- Real-time stock price lookup
- Mutual fund information retrieval
- Currency conversion
- Real-time cryptocurrency prices
- Interactive chat interface

## Project Structure
```
FinPilotProject/
├── app.py                  # Streamlit frontend
├── main.py                 # FastAPI backend entry point
├── requirements.txt        # Python dependencies
├── setup.py                # Project setup
├── pyproject.toml          # Project metadata
├── agents/                 # Agent logic
├── config/                 # Configuration files
├── logger/                 # Logging utilities
├── prompt_library/         # Prompt templates
├── tools/                  # Tool implementations (stock, currency, etc.)
├── utils/                  # Utility modules
└── ...
```

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/Likithsatya192/FinPilot
cd FinPilot
```

### 2. Create and Activate a Virtual Environment (Recommended)
```sh
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
- Copy `.env.example` to `.env` and fill in any required API keys or configuration values.

### 5. Run the Backend (FastAPI)
```sh
python main.py
```
- The backend will start at `http://localhost:8000` by default.


### 6. Run the Frontend (HTML Web UI)

You can use the beautiful HTML/JS/CSS chat UI located at `templates/index.html`:

1. Start the backend (FastAPI):
   ```sh
   python main.py
   ```
2. Open `templates/frontend.html` in your web browser.
3. Interact with the chatbot for a modern, responsive experience.

#### (Optional) Streamlit UI
You can still use the Streamlit app if you prefer:
```sh
streamlit run app.py
```
The Streamlit app will open in your browser.

## Usage Workflow
1. **Start the backend**: `python main.py`
2. **Start the frontend**: `streamlit run app.py`
3. **Interact with the app**: Enter your financial queries (e.g., "What is the current stock price of AAPL?") in the chat interface.
4. **View results**: The AI assistant will respond with real-time data and analysis.

## Requirements
- Python 3.10+
- See `requirements.txt` for all Python dependencies

---
*This project was created by Likith's FinBot Financial Assistant.*
