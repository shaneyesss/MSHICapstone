
# 🧠 Layman Summarizer Dashboard

This is a lightweight Flask-based web application that translates radiology or pathology reports into plain language using OpenAI's GPT API. It is intended for educational and patient-facing use cases. Developed for UT Southwestern's MSHI Capstone Project. 

## 🚀 Features
- Simplify complex medical reports into lay terms.
- Local Flask dashboard with editable front-end.
- Secure API key integration (server-side only).
- Built with Python, HTML, and Flask.

## 🛠 Technologies
- Python 3.x
- Flask
- OpenAI API (requires API key)
- HTML/CSS

## 💻 Usage Instructions

### 1. Install Dependencies
```bash
pip install flask openai
```

### 2. Add Your OpenAI Key
Open `app.py` and insert your key:
```python
client = OpenAI(api_key="sk-...")
```

### 3. Run the App
```bash
python app.py
```
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to view the dashboard.

---

## 🧾 Disclaimer
This tool is for educational and demo purposes only. It does not provide clinical advice.

