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
- `OpenStreetMap Nominatim API` for referrals

## 📸 Demo Screenshot

![Screenshot](screenshots/sdoh_dashboard.png)

## 🔐 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/sdoh-risk-dashboard.git
cd sdoh-risk-dashboard
