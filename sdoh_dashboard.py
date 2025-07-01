import streamlit as st
import matplotlib.pyplot as plt
import json
import pandas as pd
import pgeocode
import requests
from openai import OpenAI

# === Authenticate OpenAI Client ===
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# === Function: Score SDoH Risks ===
def score_sdoh_risks(note, zip_code=None, demographics=None):
    zip_context = f"The patient lives in ZIP code {zip_code}, which may reflect local economic or resource constraints." if zip_code else ""
    demo_context = ""
    if demographics:
        demo_context = "Patient demographics:\n"
        for k, v in demographics.items():
            if v:
                demo_context += f"- {k}: {v}\n"
    prompt = f"""
You are an AI assistant helping social workers assess patient needs.

{zip_context}
{demo_context}

Given the following case note, evaluate the **risk level** (from 0 to 100) for each Social Determinant of Health (SDoH) domain. A higher score means higher risk or concern in that area.

Return the result as a JSON dictionary with these fields:
- Housing
- Employment
- Transportation
- Food
- Family
- Financial

Note:
\"\"\"
{note}
\"\"\"

Respond only with the JSON object.
"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=300
    )
    raw = response.choices[0].message.content.strip()
    try:
        cleaned = raw.strip("```").replace("json", "").strip()
        return json.loads(cleaned)
    except json.JSONDecodeError:
        st.error("⚠️ GPT response was not valid JSON.")
        st.text_area("Raw Output", value=raw)
        return None

# === Function: ZIP to Location Info ===
def get_zip_info(zip_code):
    nomi = pgeocode.Nominatim('us')
    location = nomi.query_postal_code(zip_code)
    if pd.isna(location.place_name):
        return None
    return {
        "city": location.place_name,
        "state": location.state_name,
        "county": location.county_name
    }

# === Function: GPT-Suggested Referrals ===
def get_gpt_referrals(domain, zip_code=None, location=None):
    location_context = ""
    if location:
        location_context = f"The patient is located in ZIP code {zip_code}, in {location['city']}, {location['county']} County."

    prompt = f"""
You are a helpful assistant for social workers.

{location_context}

For the social need domain of **{domain}**, list 3 real-world local resources such as support groups, therapy centers, NGOs, or community services that are available nearby.

For each resource, return:
- Name
- Address
- Phone Number (if known)
- Google Maps or website link (if available)

Present the information as a bullet-point list, grouped by domain.
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=500
    )

    return response.choices[0].message.content.strip()

# === Streamlit UI ===
st.title("LLM-Powered SDoH Assistant: Risk Scoring with Real-Time Local Referrals")
st.markdown("Enter a patient case note and demographics to assess SDoH risk and connect with real-world services.")

note = st.text_area("📋 Patient Case Note", height=200)
zip_code = st.text_input("📍 ZIP Code", max_chars=10)

# Location context
zip_info = get_zip_info(zip_code) if zip_code else None
if zip_info:
    st.markdown(f"**📍 Location Info:** {zip_info['city']}, {zip_info['state']} ({zip_info['county']} County)")
elif zip_code:
    st.warning("⚠️ Could not resolve location from ZIP code.")

# Demographics
st.markdown("### 👤 Demographics")
age = st.number_input("Age", min_value=0, max_value=120, step=1)
gender = st.selectbox("Gender", ["", "Male", "Female", "Non-binary", "Other"])
race = st.selectbox("Race", ["", "White", "Black or African American", "Asian", "Native American", "Pacific Islander", "Other"])
ethnicity = st.selectbox("Ethnicity", ["", "Hispanic or Latino", "Not Hispanic or Latino", "Other"])
education = st.selectbox("Education Level", ["", "Less than High School", "High School Graduate", "Some College", "Bachelor's Degree", "Graduate Degree"])
income = st.selectbox("Annual Income", ["", "<$25K", "$25K–$50K", "$50K–$75K", "$75K–$100K", ">$100K"])
relationship = st.selectbox("Relationship Status", ["", "Single", "Married", "Divorced", "Widowed", "Domestic Partnership"])
job = st.selectbox("Job Status", ["", "Unemployed", "Employed", "Self-Employed", "Student", "Laid-Off", "Other"])

demographics = {
    "Age": int(age) if age else "",
    "Gender": gender,
    "Race": race,
    "Ethnicity": ethnicity,
    "Education": education,
    "Income": income,
    "Relationship Status": relationship,
    "Job Status": job
}

# === Run LLM + Show Outputs ===
if st.button("🔍 Score Risk"):
    if note.strip():
        with st.spinner("Scoring..."):
            results = score_sdoh_risks(note, zip_code, demographics)
            if results:
                st.success("✅ Risk scores generated!")

                # Table view
                df_scores = pd.DataFrame(list(results.items()), columns=["SDoH Domain", "Risk Score"])
                st.dataframe(
                    df_scores.sort_values("Risk Score", ascending=False)
                        .style.background_gradient(cmap="Reds", subset=["Risk Score"]),
                    use_container_width=True
                )

                # Chart view
                fig, ax = plt.subplots()
                ax.bar(results.keys(), results.values(), color='salmon')
                ax.set_ylim(0, 100)
                ax.set_ylabel("Risk Level")
                ax.set_title("SDoH Risk Assessment")
                plt.xticks(rotation=30, ha="right")
                st.pyplot(fig)

                # GPT Referral Suggestions
                if zip_code:
                    st.markdown("### 🏥 Suggested Local Referrals")
                    for domain, score in results.items():
                        if score >= 60:
                            st.markdown(f"**{domain}:**")
                            gpt_refs = get_gpt_referrals(domain, zip_code, zip_info)
                            st.markdown(gpt_refs)
    else:
        st.warning("⚠️ Please enter a case note to proceed.")
