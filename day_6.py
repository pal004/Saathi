# Day6_Physical.py
import streamlit as st

def run():
    st.set_page_config(page_title="SAATHI — Part 6 Physical Well-being", layout="centered")
    st.title("SAATHI — Day 6: Physical Well-being")
    st.write("Monitor astronaut vitals & provide adaptive health support.")

    # ---------------- Inputs ----------------
    st.subheader("Enter Vital Details")

    bp_sys = st.number_input("Blood Pressure (Systolic mmHg)", 80, 200, 120)
    bp_dia = st.number_input("Blood Pressure (Diastolic mmHg)", 50, 120, 80)
    spo2 = st.slider("Oxygen Saturation (%)", 70, 100, 97)
    hr = st.slider("Heart Rate (bpm)", 40, 180, 75)
    sleep = st.slider("Sleep Duration (hours)", 0, 12, 7)
    weight = st.number_input("Weight (kg)", 30.0, 150.0, 70.0)
    height = st.number_input("Height (cm)", 100.0, 220.0, 175.0)

    # BMI calculation
    bmi = round(weight / ((height / 100) ** 2), 2)
    st.metric("BMI", f"{bmi} kg/m²")

    # ---------------- Emergency Check ----------------
    emergency = False
    alerts = []

    if spo2 < 90:
        emergency = True
        alerts.append("⚠️ Oxygen critically low (<90%). Use emergency O₂ support immediately.")

    if hr > 120 or hr < 50:
        emergency = True
        alerts.append("⚠️ Abnormal heart rate detected. Rest & medical check required.")

    if bp_sys > 160 or bp_dia > 100:
        emergency = True
        alerts.append("⚠️ High blood pressure risk. Avoid exertion, consult medic.")

    if bp_sys < 90 or bp_dia < 60:
        emergency = True
        alerts.append("⚠️ Low blood pressure risk. Hydrate & rest immediately.")

    if sleep < 4:
        alerts.append("⚠️ Sleep deprivation. This may affect cognition & mood.")

    # ---------------- Responses ----------------
    st.subheader("SAATHI Health Response")

    if emergency:
        st.error("🚨 EMERGENCY CASE DETECTED 🚨")
        for a in alerts:
            st.write(a)
        st.warning("Remedial First Aid: Sit/lie down, regulate breathing, hydrate. "
                   "Alert medical officer / Ground Control immediately.")
    else:
        st.success("✅ Vitals are stable. No emergency detected.")
        for a in alerts:
            st.info(a)

        # Exercise recommendation
        st.subheader("🏋️ Exercise Recommendation")
        if hr < 100 and spo2 >= 95:
            st.write("✅ Fit for light resistance training: 20 min cycle + stretches.")
        elif hr > 100:
            st.write("⚠️ Elevated HR → Only light stretching & breathing exercises today.")
        else:
            st.write("⚠️ Oxygen not optimal → Focus on breathing exercises, skip heavy workouts.")

        # Nutrition recommendation
        st.subheader("🥗 Health & Nutrition Advice")
        if bmi < 18.5:
            st.write("Underweight → Add protein & calorie-rich food (nuts, pulses, protein shakes).")
        elif 18.5 <= bmi <= 24.9:
            st.write("Normal BMI → Maintain balanced diet with proteins, greens, and hydration.")
        elif 25 <= bmi <= 29.9:
            st.write("Overweight → Reduce simple carbs, add fiber, focus on cardio workouts.")
        else:
            st.write("Obese → Strict calorie control, lean proteins, daily exercise needed.")

        if sleep < 6:
            st.write("💤 Low sleep detected → Add 30–60 min nap cycle to restore focus.")
