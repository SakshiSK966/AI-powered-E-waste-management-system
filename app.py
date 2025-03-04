import streamlit as st


st.markdown(
    "<h1 style='text-align: center; font-size: 30px;'>AI Powered E-Waste Management System</h1>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://th.bing.com/th/id/OIP.G25u4JEV04OqPvdGQ9suaAHaG5?w=208&h=194&c=7&r=0&o=5&dpr=1.3&pid=1.7" width="150">
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; font-size:20px; font-weight:bold;'>🌱 Welcome to the Future of E-Waste Management! 🌍</p>",
    unsafe_allow_html=True
)


st.markdown(
    "<p style='text-align: center; font-size:18px; font-weight:bold;'>♻️ Dispose | 🔄 Recycle | 🌱 Sustain</p>", 
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Upload your e-waste details and let AI guide you! 🚀</p>", 
    unsafe_allow_html=True
)

st.subheader("📤 Upload Your E-Waste Details")  
uploaded_file = st.file_uploader("Choose an image or document", type=["jpg", "png", "pdf", "txt"])
if uploaded_file:
    st.success("File uploaded successfully!")

if st.button("Analyze E-Waste"):
    st.info("🔍 AI is analyzing the uploaded file...")
    # Call your ML model here
    st.success("✅ Analysis Complete! Your e-waste category: [Category Name]")

st.subheader("♻️ Recommended Recycling Centers")
st.write("🔹 Nearest recycling facility: **XYZ Recycling Center**")  
st.write("📍 Location: [Google Maps Link]")  
st.write("📞 Contact: +91 XXXXXXXXXX")  

st.subheader("🏆 Your Sustainability Score")
score = 56
st.progress(score / 100)
st.write(f"🌱 You have saved **{score} kg of e-waste** from landfills!")

st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ for a greener future 🌍</p>", unsafe_allow_html=True)



