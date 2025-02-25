import streamlit as st

st.set_page_config(page_title= "Growth mindset project", project_icon= " ★")
st.title("Growth Mindset AI Project")

st.header("🚀Welcome to your Growth journey")
st.write( "🌱 With hard work, dedication, and a passion for learning, nothing is impossible. Failure is just a phase; the real defeat happens only when we stop learning!")
 
st.header("💡Today's Growth Mindset Quote")
st.write("🌟 Success is not just about luck it comes through hard work and dedication.Those who face challenges instead of fearing them are the ones who truly achieve victory. Every mistake is a new lesson, and every new day brings new opportunities. The one who never stops is the one who truly reaches the destination of success! 🚀")

st.header(" what's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success("you're facing: {user_input}. Keep pushing forward towards your goal!🚀")
else:
    st.warning("Tell us about your challenge to get started!")

st.success("Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"✨Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")

st.header("💫 Celebrate Your Wins!")
acheivment = st.text_input("Share something you've recently accomplished:")

if acheivment:
    st.success(f"🌠 Amazing! You achieved: {acheivment}")
else:
    st.info("Big or Small, every acheivment counts! Share one now 😍")

    st.write("- - - ")
    st.write("🌸 Keep believing in yourself. Growth is s jouney, not a destination! ✨")
    st.write("⛔ Created by Sumaira Naveed")
