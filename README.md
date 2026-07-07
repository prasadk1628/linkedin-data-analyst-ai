#LinkedIn Content Automation Engine 

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)
[![Gemini API](https://img.shields.io/badge/Google-Gemini%202.5%20Flash-4285F4?logo=google&logoColor=white)](https://ai.google.dev/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://sqlite.org)
[![GitHub Actions](https://img.shields.io/badge/GitHub-Automated-181717?logo=github&logoColor=white)](https://github.com/features/actions)
[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> An AI-powered content automation system that generates professional LinkedIn posts for aspiring Data Analysts using Google Gemini, automatically schedules topics, validates AI output, stores generated content, and delivers LinkedIn-ready posts directly to email.

---

# The Problem

Maintaining a consistent LinkedIn presence is one of the best ways to build a professional brand, yet creating high-quality technical content every day is time-consuming.

For aspiring Data Analysts, the challenge is even bigger:

- Choosing a valuable topic every day
- Writing technically correct content
- Maintaining consistent formatting
- Creating engaging CTAs
- Producing image ideas
- Posting consistently

The result is inconsistent posting habits and missed opportunities for networking and personal branding.

---

# The Solution

LinkedIn Content Automation Engine  automates the entire content generation workflow.

Every execution performs the complete pipeline automatically:

1. Selects the next pending topic
2. Generates an AI-powered LinkedIn post using Gemini
3. Validates the generated JSON response
4. Stores the post in SQLite
5. Saves the post locally
6. Delivers a LinkedIn-ready email

The project focuses on **automation**, **reliability**, and **content consistency** rather than simply generating text.

---

# Workflow

```
topics.csv
      │
      ▼
Topic Scheduler
      │
      ▼
Gemini AI
      │
      ▼
JSON Validation
      │
      ▼
SQLite Database
      │
      ├────────► Local Storage
      │
      └────────► HTML Email
```

---

# Features

- AI-powered LinkedIn post generation
- Automatic topic scheduling
- JSON response validation
- SQLite content database
- CSV topic queue management
- Local post storage
- HTML email delivery
- GitHub Actions automation
- Environment variable support
- Modular Python architecture

---

# Tech Stack

| Layer | Technology |
|---|---|
| Programming Language | Python 3.12 |
| AI Model | Google Gemini 2.5 Flash |
| Database | SQLite |
| Automation | GitHub Actions |
| Dashboard | Streamlit |
| Configuration | dotenv |
| Storage | CSV + SQLite |

---

# Project Structure

```text
linkedin-data-analyst-ai/
│
├── .github/
│   └── workflows/
│       └── daily.yml
│
├── data/
│   ├── posts.db
│   └── topics.csv
│
├── generated_posts/
│
├── prompts/
│
├── src/
│   ├── ai_generator.py
│   ├── config.py
│   ├── database.py
│   ├── email_sender.py
│   ├── file_manager.py
│   ├── json_parser.py
│   ├── pipeline.py
│   ├── topic_manager.py
│   └── validators.py
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

# How It Works

The pipeline executes in the following order:

1. Read the next pending topic from `topics.csv`
2. Generate structured JSON using Gemini
3. Validate required fields
4. Save generated content
5. Insert record into SQLite
6. Send HTML email containing:
   - LinkedIn-ready post
   - Image prompt
7. Mark the topic as completed

---

# Sample Email Output

Every generated email contains:

- ✅ LinkedIn-ready post
- ✅ CTA
- ✅ Hashtags
- ✅ AI-generated image prompt

The content is immediately ready for publishing on LinkedIn.

---

# Run Locally

### Clone Repository

```bash
git clone https://github.com/prasadk1628/linkedin-data-analyst-ai.git

cd linkedin-data-analyst-ai
```

### Create Virtual Environment

```bash
python -m venv .venv

source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create `.env`

```env
GEMINI_API_KEY=YOUR_API_KEY

EMAIL_ADDRESS=YOUR_EMAIL

EMAIL_APP_PASSWORD=YOUR_APP_PASSWORD
```

### Run

```bash
python main.py
```

---

# Automation

GitHub Actions runs the project automatically.

Current workflow:

```
GitHub Actions
        │
        ▼
Generate Post
        │
        ▼
Store in SQLite
        │
        ▼
Send HTML Email
```

---

# Limitations

- Uses Gemini API rate limits.
- LinkedIn posting is intentionally manual due to LinkedIn API restrictions.
- Image generation currently uses AI-generated prompts rather than automatic image creation.

---

# Roadmap

- [ ] Automatic AI image generation
- [ ] LinkedIn API integration (if publicly available)
- [ ] Content analytics dashboard
- [ ] Multiple social media platform support
- [ ] AI-powered topic recommendation engine

---

# License

MIT License

---

# Author

**Vara Prasad K**

B.Tech CSE  
Aspiring Data Analyst

[![Email](https://img.shields.io/badge/Email-kavalivaraprasad16@gmail.com-D14836?logo=gmail&logoColor=white)](mailto:kavalivaraprasad16@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-vara--prasad--k-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vara-prasad-kavali/)
[![GitHub](https://img.shields.io/badge/GitHub-prasadk1628-181717?logo=github&logoColor=white)](https://github.com/prasadk1628)

---

*Built to automate professional LinkedIn content creation for aspiring Data Analysts using AI and workflow automation.*
