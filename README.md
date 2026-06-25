# Technify_internship_program

## 👤 Author
AI Internship Submission — Task 01: AI Interview Question Generator

# 🎯 AI Interview Question Generator

An AI-based Streamlit application that generates **technical** and **HR**
interview questions tailored to a chosen **job role**, **skills**, and
**difficulty level** (Easy / Medium / Hard).

This was built for the **AI Internship – Task 01** assignment.

## 📌 Features
<img width="639" height="332" alt="image" src="https://github.com/user-attachments/assets/ae10bb94-b680-4188-ae24-9763b6fd9d26" />


- ✅ Job Role input
- ✅ Skills input (comma-separated, supports any number of skills)
- ✅ Generates **Technical Questions** and **HR Questions** in separate tabs
- ✅ Three Difficulty Levels: Easy, Medium, Hard
- ✅ **Regenerate** button for a fresh set of questions instantly
- ✅ Clean, simple Streamlit UI
- ✅ Works fully **offline** (built-in question bank + smart templates) —
  no API key required
- ✅ **Optional** OpenAI / Gemini API integration for fully dynamic,
  AI-generated questions
- ✅ Download generated questions as a `.txt` file

## 🛠️ Tech Stack

| Component        | Technology              |
|-------------------|--------------------------|
| Language          | Python 3.9+              |
| UI Framework      | Streamlit                |
| AI (optional)     | OpenAI API / Gemini API  |


## 📂 Project Structure

interview_question_generator/
│
├── app.py                  # Streamlit UI — main entry point
├── question_generator.py   # Core logic: question bank + generators
├── requirements.txt        # Python dependencies
└── README.md                # Project documentation (this file)
```

## ⚙️ How It Works

1. **User Input**: The user enters a Job Role (e.g. "Data Scientist"),
   a comma-separated list of Skills (e.g. "Python, SQL, Machine Learning"),
   and picks a Difficulty level.
2. **Generation Engine** (`question_generator.py`):
   - **Offline mode (default)**: Looks up each skill in a curated question
     bank (`TECHNICAL_BANK`). If a skill isn't in the bank, it falls back to
     smart templates (`GENERIC_TEMPLATES`) that plug the skill/role into a
     realistic question structure — so *any* skill works.
   - **HR questions** come from a separate bank (`HR_BANK`) of
     behavioral/situational questions scaled by difficulty.
   - **LLM mode (optional)**: If the user supplies an OpenAI or Gemini API
     key in the sidebar, the app instead sends a prompt to that model and
     parses a JSON response containing both question sets.
3. **Display**: Questions are shown in two tabs — Technical and HR — each
   numbered and easy to read.
4. **Regenerate**: Clicking "Regenerate Questions" re-runs the generator
   (re-shuffling the offline bank, or re-calling the LLM) to produce a new
   set without changing your inputs.
5. **Download**: Users can export the generated question set as a `.txt`
   file for offline practice.


## 🚀 Setup & Run Instructions

### 1. Clone / copy the project folder
```bash
cd interview_question_generator
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt


> Note: `openai` and `google-generativeai` are only required if you plan to
> use the optional LLM mode. The app runs fine without them in Offline mode.

### 4. Run the app
```bash
streamlit run app.py

The app will open automatically in your browser at `http://localhost:8501`.

### 5. (Optional) Use OpenAI or Gemini
- In the sidebar, change "Question Generation Mode" to **OpenAI API** or
  **Gemini API**.
- Paste your API key into the field that appears (it is used only for that
  session and is never saved to disk).
- Click **Generate Interview Questions** as usual.

## 🧩 Extending the Project

- **Add more roles/skills**: Add entries to `TECHNICAL_BANK` in
  `question_generator.py` — the structure is
  `TECHNICAL_BANK[skill][difficulty] = [list of questions]`.
- **Add more HR questions**: Extend the `HR_BANK` dictionary per difficulty.
- **Persist history**: Hook up a database (e.g. SQLite) to save past
  generated question sets per user.
- **Export to PDF**: Add a PDF export option alongside the existing `.txt`
  download using a library like `fpdf2`.
- **User accounts**: Add login so each user can save and revisit their own
  generated question sets.


## 📋 Example Usage

| Job Role        | Skills                      | Difficulty | Output                                            |
|------------------|------------------------------|------------|----------------------------------------------------|
| Data Scientist   | Python, SQL, Machine Learning | Medium     | 6 technical + 5 HR questions tailored to the role |
| Frontend Developer | JavaScript, React           | Hard       | Advanced React/JS architecture & debugging questions |

