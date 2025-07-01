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
- 🌍 Free real-time referral search

## 🧱 Tech Stack

- `Python`
- `Streamlit` for interactive UI
- `OpenAI GPT-4o` for risk scoring
- `Pandas` & `Matplotlib` for visualization
- `pgeocode` for ZIP code resolution


🧪 Sample Prompts

🏠 Housing + 🍲 Food Insecurity
"Patient was recently evicted and reports not having enough groceries to feed her children regularly."

🚗 Transportation + 🏥 Access to Care
"Patient missed several medical appointments due to lack of reliable transportation options."

💼 Employment + 💸 Financial Strain
"Patient works two unstable part-time jobs and still struggles to cover monthly expenses."

👩‍👧 Family Stress + 🏠 Housing
"Single parent with three children currently living in overcrowded temporary housing after eviction."

🍲 Food Insecurity + 💸 Financial Strain
"Patient reports skipping meals due to limited income and inability to afford groceries consistently."

🚗 Transportation + 💼 Employment
"Patient lacks a car and often arrives late to work, putting her part-time job at risk."

👩‍👧 Family Support + 💼 Employment
"Patient is a single parent working two jobs without any family or social support for childcare."

