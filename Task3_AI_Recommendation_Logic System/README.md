
# decodelabs_tasks
This repository contains my completed tasks for the DecodeLabs Industrial Training Program. It includes AI and Machine Learning projects focused on data classification, model training, testing, and evaluation using Python and related libraries.
=======
# 🎬 AI Recommendation Logic System

## 📌 Project Overview

The **AI Recommendation Logic System** is a beginner-level Artificial Intelligence project developed during the DecodeLabs Industrial Training Program (Batch 2026).

The project demonstrates how recommendation systems work by matching user preferences with item attributes using rule-based similarity logic.

Instead of random suggestions, the system analyzes user interests such as genre, mood, and language to recommend the most relevant movies.

---

## 🎯 Project Objective

The main goal of this project is to build a simple recommendation engine that:

* Accepts user preferences.
* Compares preferences with available movies.
* Calculates similarity scores.
* Provides personalized movie recommendations.

---

# ✨ Features

✅ User preference input system
✅ Content-based recommendation logic
✅ Similarity score calculation
✅ Movie ranking based on matching preferences
✅ Rating-based sorting
✅ Input validation
✅ Interactive command-line interface
✅ Multiple recommendation searches

---

# 🛠️ Technologies Used

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python        | Core programming language |
| Pandas        | Dataset handling          |
| CSV           | Data storage              |
| Rule-Based AI | Recommendation logic      |

---

# 📂 Project Structure

```
AI_Recommendation_Logic/

│
├── data/
│   └── movies.csv
│
├── src/
│   ├── dataset.py
│   └── recommender.py
│
├── screenshots/
│
├── main.py
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone <repository-link>
```

## 2. Navigate to Project Folder

```bash
cd AI_Recommendation_Logic
```

## 3. Create Virtual Environment

```bash
python -m venv .venv
```

## 4. Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

## 5. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

Run the application:

```bash
python main.py
```

---

# 🧠 Recommendation Logic

The system uses a weighted similarity algorithm.

Each matching preference contributes points:

| Preference     | Score |
| -------------- | ----: |
| Genre Match    |    +3 |
| Mood Match     |    +2 |
| Language Match |    +1 |

Example:

User Preference:

```
Genre: Sci-Fi
Mood: Adventure
Language: English
```

Movie:

```
Avatar
```

Calculation:

```
Genre Match      = +3
Mood Match       = +2
Language Match   = +1

Total Score = 6
```

Movies with higher scores are recommended first.

---

# 📊 Sample Output

```
AI MOVIE RECOMMENDATION SYSTEM

Enter Genre:
Sci-Fi

Enter Mood:
Adventure

Enter Language:
English


Recommended Movies

Interstellar
Avatar
The Matrix
Inception
```

---

# 📸 Screenshots

(Add project screenshots here)

Example:

```
screenshots/
│
├── project_running.png
├── recommendation_output.png
├── invalid_input.png
```

---

# 🚀 Future Improvements

Future versions can include:

* Machine Learning recommendation models.
* Collaborative filtering.
* User rating system.
* Web-based interface.
* Deep learning recommendation models.
* Database integration.

---

# 👨‍💻 Author

**Muhammad Ramzan**

Artificial Intelligence Engineering Intern
DecodeLabs Industrial Training Program
Batch 2026

---

# 📚 References

* Pandas Documentation
  https://pandas.pydata.org/docs/

* Scikit-learn Documentation
  https://scikit-learn.org/stable/

---

## ⭐ Project Status

Completed ✅

This project demonstrates the fundamentals of Artificial Intelligence recommendation systems using similarity-based pattern matching.
(Completed AI Recommendation Logic)
