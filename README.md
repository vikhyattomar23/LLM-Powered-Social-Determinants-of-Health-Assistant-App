# 🧠 LLM-Powered-Social-Determinants-of-Health-Assistant-App

This project is an AI-powered web application that allows social workers and care managers to assess **Social Determinants of Health (SDoH)** risk levels from clinical notes using OpenAI’s GPT-4o. It also recommends **real-world service referrals** based on high-risk SDoH factors.

I developed a **Streamlit-based web application** that allows social workers to paste a patient’s case note, optionally provide ZIP code and demographics, and then get:

1. Risk scores (0–100) for six SDoH domains: Housing, Employment, Food, Transportation, Family, Financial
2. Local referrals (e.g., shelters, food banks, NGOs) for domains with high risk, tailored to the ZIP code
3. Visualizations: risk heatmap, bar chart, and a structured results table

The assistant is designed to be lightweight and interactive, requiring no backend database. Everything is computed live using **GPT-4o through OpenAI’s API**.

<img width="1467" alt="Screenshot 2025-07-01 at 4 46 48 AM" src="https://github.com/user-attachments/assets/2e58ce81-3490-4811-b4bc-f2299c502e53" />
<img width="1467" alt="Screenshot 2025-07-01 at 4 47 06 AM" src="https://github.com/user-attachments/assets/d4009831-22b1-4200-9d69-66de91834d5d" />
<img width="1467" alt="Screenshot 2025-07-01 at 4 47 24 AM" src="https://github.com/user-attachments/assets/8c7204f8-75fc-4df1-b5a2-c84ff7162717" />
<img width="1467" alt="Screenshot 2025-07-01 at 4 47 36 AM" src="https://github.com/user-attachments/assets/ce2bd8dd-f004-4e6a-b6ff-e0aa27ab196d" />
<img width="1467" alt="Screenshot 2025-07-01 at 4 47 50 AM" src="https://github.com/user-attachments/assets/4e301681-3500-42d5-83c6-9ae9565cc5a1" />
<img width="1467" alt="Screenshot 2025-07-01 at 4 48 01 AM" src="https://github.com/user-attachments/assets/fdb528c0-2483-4fbc-9565-e157cebd0ef2" />


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


## 🧪 Sample Clinical Notes

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

## Conclusion

I’m passionate about—healthcare and social equity. The assistant I built might be small in scale, but it demonstrates how powerful and accessible LLM-based systems have become.

By translating a free-text note into structured risk signals and then linking those to local interventions, this prototype shows the potential of AI to amplify the work of social workers, not replace them.

