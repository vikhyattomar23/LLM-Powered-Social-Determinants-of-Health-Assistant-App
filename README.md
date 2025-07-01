# 🧠 LLM-Powered-Social-Determinants-of-Health-Assistant-App

This project is an AI-powered web application that allows social workers and care managers to assess **Social Determinants of Health (SDoH)** risk levels from clinical notes using OpenAI’s GPT-4o. It also recommends **real-world service referrals in Minnesota** based on high-risk areas.

## 🚀 Features

- 📋 Upload or type patient case notes
- 🔎 GPT-4o assesses SDoH risk across 6 domains:
  - Housing
  - Employment
  - Transportation
  - Food
  - Family
  - Financial
- 🧑🏽‍⚕️ Demographics input: gender, race, education, profession, etc.
- 📍 Zip code contextualization (city/county lookup)
- 📊 Risk score table + bar chart visualization
- 🏥 Auto-recommendations for interventions
- 🌍 Free real-time referral search (via OpenStreetMap API) in Minnesota
- ➕ Extended support categories: therapy, fitness, wellness, eldercare

## 🧱 Tech Stack

- `Python`
- `Streamlit` for interactive UI
- `OpenAI GPT-4o` for risk scoring
- `Pandas` & `Matplotlib` for visualization
- `pgeocode` for ZIP code resolution


🧪 Sample Prompt

Patient is a 45-year-old single mother recently evicted from her apartment. 
She has three children, works two part-time jobs, and struggles with groceries and transportation.

📍 Future Enhancements
Embedding-based RAG for local policy matching

Custom training for clinical-style notes

Audit logs for LLM decisions

Map-based resource navigation

Support for multi-state referrals
