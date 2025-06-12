import streamlit as st

# App title
st.set_page_config(page_title="Agent Profile", layout="centered")
st.title("Meet Our Sales Agent")

# Profile section
st.subheader("👤 Agent Profile")
st.markdown("""
**Name:** Shawn  
**Role:** Senior Sales Representative  
**Expertise:** NEPQ-Trained Closer  
**Specialty:** Sells our proprietary Network Marketing Training Program  
""")

# NEPQ section
st.subheader("🎯 What Makes Shawn Different?")
st.markdown("""
Shawn isn't your average sales rep. He's trained in the **Neuro-Emotional Persuasion Questioning (NEPQ)** method—
a revolutionary framework that helps potential clients lower their guard and open up through emotionally intelligent questions.

Rather than using high-pressure tactics, Shawn guides conversations with empathy, clarity, and purpose.
""")

# Program section
st.subheader("📘 What He Sells")
st.markdown("""
Shawn represents our **Network Marketing Training Program**, designed specifically for:
- Dads who want to rank up without feeling like a scammer
- Disruptors tired of outdated upline tactics
- People ready to build systems that actually scale

With Shawn, prospects don’t feel sold to—they feel understood.
""")

# Call to action
st.success("✅ Want to see how Shawn can help you or your team? Reach out to book a free strategy call!")

