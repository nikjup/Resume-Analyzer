# 🚀 AI Resume Analyzer

A modern AI-powered Resume Analyzer web application built using Flask, Python, and Google Gemini integration.

This project analyzes resumes against job descriptions and generates intelligent feedback, matching insights, and improvement suggestions using Prompt Engineering and Large Language Model (LLM) integration.

The application is designed with a modern AI startup-style user interface and deployed publicly on Render.

---

# 🌐 Live Demo

🔗 https://resume-analyzer-1-h70l.onrender.com

---

# 📌 Features

✅ Resume vs Job Description Analysis  
✅ Google Gemini LLM Integration  
✅ Prompt Engineering Support  
✅ Modern AI Startup UI  
✅ Flask Backend Architecture  
✅ Public Deployment using Render  
✅ Simulation Mode Support  
✅ Download Report Feature  
✅ Responsive Web Interface  
✅ Environment Variable Security  
✅ Git & GitHub Integration  

---

# 🧠 Technologies Used

## Frontend
- HTML5
- CSS3
- Bootstrap 5

## Backend
- Python
- Flask

## GenAI / AI
- Google Gemini API
- Prompt Engineering

## Deployment & DevOps
- Render
- Gunicorn
- Git
- GitHub

---

# 📂 Project Structure

```bash
AI_Resume_Project/
│
├── webapp.py
├── genai.py
├── requirements.txt
├── Procfile
├── README.md
│
├── static/
│   └── robot.png
│
└── templates/
    └── index.html

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/Resume-Analyzer.git

This downloads the project to your local machine.

2️⃣ Move Into Project Directory
cd AI_Resume_Project

Moves terminal into the project folder.

3️⃣ Install Dependencies
pip install -r requirements.txt

Installs all required Python libraries for the application.

4️⃣ Set Environment Variable

Create an environment variable:

GEMINI_API_KEY=your_gemini_api_key

This securely stores the API key without exposing it inside source code.

5️⃣ Run Application
python webapp.py

Starts the Flask development server locally.

🚀 Deployment

This application is deployed using Render with:

Gunicorn WSGI Server
Python Runtime
GitHub Continuous Deployment

Deployment configuration files such as Procfile and runtime.txt are used for production hosting.

🧠 How the Application Works
Step 1

User enters:

Resume
Job Description
Prompt

through the web interface.

Step 2

Flask backend receives the request using POST method.

Step 3

Prompt is processed and sent to Google Gemini API.

Step 4

LLM generates intelligent analysis and matching insights.

Step 5

Generated response is returned to Flask backend and displayed in the UI.

Step 6

If API quota is unavailable, the application switches to Simulation Mode gracefully.

🎨 UI Highlights
Modern AI Startup Theme
Responsive Layout
Glassmorphism Design
AI Robot Visual Integration
Gradient Background
Styled Result Panel
Interactive Buttons
Loading Indicators

The UI is designed to resemble modern AI SaaS products with responsive and visually appealing styling.

🔒 Security Practices
API keys managed using Environment Variables
.gitignore used to prevent sensitive file uploads
Clean repository structure maintained

These practices help in preventing accidental exposure of sensitive credentials and unnecessary files.

📚 Learning Outcomes

This project helped in understanding:

GenAI Application Development
Prompt Engineering
Flask Web Development
API Integration
Git & GitHub Workflow
Environment Variables
Cloud Deployment
Production Debugging
Gunicorn Configuration
Modern UI Design

🚧 Current Status

✅ Frontend Completed
✅ Backend Completed
✅ GitHub Integration Completed
✅ Deployment Completed
✅ Public Hosting Completed
⚠️ AI Features depend on active API quota

The project is fully functional and publicly deployed.

🔮 Future Improvements

PDF Resume Upload
ATS Match Percentage
Resume Skill Highlighting
AI Streaming Responses
Authentication System
User Dashboard
Resume History Tracking
Database Integration
Real-Time Feedback System

These improvements can help transform the application into a production-grade AI SaaS platform.

📸 Screenshots

<img width="1900" height="905" alt="AI Resume Match Tool - Google Chrome 25-05-2026 21_23_24" src="https://github.com/user-attachments/assets/ecb154be-d3d1-465f-9e1e-b30f8ab86a16" />

<img width="1886" height="909" alt="AI Resume Match Tool - Google Chrome 25-05-2026 21_20_52" src="https://github.com/user-attachments/assets/d9a28c11-77c7-4489-9409-17513d79e46e" />


👨‍💻 Author

Nikhil Kumar

⭐ Project Goal

The goal of this project is to combine:

Generative AI
Prompt Engineering
Backend Engineering
Deployment Practices
Modern UI/UX

into a production-style AI web application.

📄 License

This project is developed for educational and portfolio purposes.
