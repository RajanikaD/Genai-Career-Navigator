# 🚀 GenAI Career Navigator

An interactive web app to guide your **GenAI career** based on your resume!  
It extracts your technical skills from a PDF resume, visualizes your current skill landscape, and suggests **advanced AI/LLM/GenAI skills** to learn next.

<p align="center"> <img src="Screenshot 2025-06-24 195326.png" width="800"/> </p>

---

## 🧠 Features

✅ **Drag & Drop Resume (PDF)**  
✅ **Skill Extraction** from resume (using NLP + PyMuPDF)  
✅ **GenAI Skill Recommendations** tailored to your background  
✅ **GPT-Powered Career Q&A** (e.g., “What job roles fit my skills?”)  
✅ **Skill Chart Visualization** (bar chart comparing current vs. future skills)  
✅ **No model training required** – lightweight, fast, and browser-friendly!

---

## 📸 App Screenshots

### 🎯 Full Resume Skill Extraction and Career Insights
<p align="center"> <img src="Screenshot 2025-06-24 195326.png" width="800"/> </p>

### 📝 Fresh Start Interface
<p align="center"> <img src="Screenshot 2025-06-24 195308.png" width="600"/> </p>

---

## 🔧 Tech Stack

| Tool        | Purpose                              |
|-------------|--------------------------------------|
| Streamlit   | Web UI                               |
| PyMuPDF     | Resume PDF parsing                   |
| Regex       | NLP-based skill extraction           |
| Matplotlib  | Skill chart visualization            |
| OpenAI API  | GPT-based career guidance            |
| Ngrok       | Temporary public link (optional)     |

---

## 🗂️ Folder Structure

📁 GenAI-Career-Navigator

├── app.py # Main Streamlit app

├── utils.py # Resume parser + skill extractor

├── requirements.txt # All Python dependencies

├── assets/

│ ├── genai_dashboard_with_skills.png

│ └── genai_dashboard_blank.png

└── README.md


---

## 💡 Example Skills Parsed

- ✅ Snowflake  
- ✅ SQL  
- ✅ Python  
- ✅ NLP  
- ✅ TensorFlow

You’ll then receive **personalized learning goals**, such as:

- 🧠 Reinforcement Learning (RL)  
- 🎨 Generative Adversarial Networks (GANs)  
- 🔍 Transformer Architecture  
- 🧾 RAG & Retrieval-Augmented Generation  
- ⚙️ Prompt Engineering

---

## ▶️ How to Run

1. Clone the repo:

```bash
git clone https://github.com/your-username/genai-career-navigator.git
cd genai-career-navigator
