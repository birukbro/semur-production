import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Semur Production | Global Standard Studio",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Dark Luxury Cinematic Theme with Gold Accents)
st.markdown("""
    <style>
    .main {
        background-color: #0b0b0b;
        color: #f0f0f0;
        font-family: 'Helvetica Neue', sans-serif;
    }
    h1, h2, h3 {
        color: #ffffff;
        letter-spacing: 1px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #d4af37 0%, #aa820a 100%);
        color: #000000;
        font-weight: bold;
        border: none;
        padding: 0.6rem 1.5rem;
        border-radius: 4px;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #f3c643 0%, #d4af37 100%);
        color: #000;
    }
    .metric-card {
        background-color: #141414;
        border: 1px solid #333333;
        padding: 20px;
        border-radius: 8px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation & Branding
st.sidebar.markdown("<h2 style='text-align: center; color: #d4af37;'>SEMUR PRODUCTION</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; font-style: italic;'>\"Bring Narration to Life\"</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigation Menu", 
    ["🏠 Home / Profile", "🎥 Services & Pricing", "🤝 Trusted Clients", "💼 Careers & Sales Partners", "📥 Contact & Inquiry"]
)

# Studio Details
LOCATION = "Ayat Meri, Addis Ababa, Ethiopia"
EMAIL = "birukbelachew1921@gmail.com / zeamantshome@gmail.com"
PHONE = "+251 92 725 6139 / +251 90 877 2421"

# --- 1. HOME / PROFILE ---
if menu == "🏠 Home / Profile":
    col_logo, col_title = st.columns([1, 2])
    with col_logo:
        # Placeholder or text representing the Gold Film Strip Logo
        st.markdown("### 🎞️ [ SEMUR LOGO ]")
        st.caption("Gold Cinematic S-Film Strip")
    with col_title:
        st.title("SEMUR PRODUCTION")
        st.subheader("Global Standard Creative Studio & Media Production")
        st.write(f"📍 **Location:** {LOCATION}")
    
    st.markdown("---")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### **Who We Truly Are**")
        st.write("""
        Whether it's a feature film that captivates audiences, a high-impact TV commercial, a documentary that inspires change, or a seamless online brand presence, **Semur Production** is a full-service creative studio committed to bringing ideas to life across all media platforms with uncompromising global standards.
        """)
    with c2:
        st.markdown("### **Our Mission & Vision**")
        st.info("**Mission:** To craft authentic, visually compelling stories across film, commercial, digital, and live experiences helping global brands connect with their audiences in meaningful ways.")
        st.success("**Vision:** To become the most trusted creative partner in the region, transforming bold ideas into cultural moments.")

    st.markdown("---")
    st.markdown("### **The Executive Team**")
    t1, t2 = st.columns(2)
    with t1:
        st.markdown("**Biruk Belachew**")
        st.write("Founder & Production Designer")
    with t2:
        st.markdown("**Eyob Tewodros**")
        st.write("Division of Marketing & Director of Photography")

# --- 2. SERVICES & PRICING ---
elif menu == "🎥 Services & Pricing":
    st.title("Our Cinematic Services & Pricing")
    st.write("Explore our high-end production categories structured for corporate clients, banks, and global brands.")
    st.markdown("---")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Film", "TV Commercials (TVCs)", "Documentaries", "Social Media", "Event Production"])
    
    with tab1:
        st.markdown("### 🎬 Film Production")
        st.write("From development to the final cut, we produce compelling narratives that resonate on the big screen and beyond.")
        st.markdown("- Script Development & Casting\n- Full-Scale Cinematic Production\n- Post-Production & Color Grading")
        
    with tab2:
        st.markdown("### 📺 TV Commercials (TVCs)")
        st.write("Commercials that stop thumbs and drive market dominance (30-60 sec).")
        st.markdown("**Pricing Range:** 80,000 ETB to 3,500,000+ ETB (Depending on scale)")
        
    with tab3:
        st.markdown("### 🎥 Corporate Documentaries")
        st.write("Deep storytelling with empathy and cinematic craft.")
        st.markdown("**Pricing Range:** 100,000 ETB to 4,000,000+ ETB")
        
    with tab4:
        st.markdown("### 📱 Social Media & Reels")
        st.write("High-frequency digital content for TikTok, Instagram, and YouTube.")
        st.markdown("**Pricing Range:** 3,000 ETB to 120,000+ ETB")
        
    with tab5:
        st.markdown("### 🎤 Event Production")
        st.write("Comprehensive event production for corporate galas and international summits.")
        st.markdown("**Pricing Range:** 15,000 ETB to 250,000+ ETB per day")

# --- 3. TRUSTED CLIENTS ---
elif menu == "🤝 Trusted Clients":
    st.title("Trusted Clients & Strategic Partners")
    st.write("We are honored to have collaborated with industry leaders and visionary institutions.")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("🏦 **Awash Bank S.C.**[cite: 11]")
        st.markdown("🛡️ **Hibret Insurance**[cite: 11]")
    with col2:
        st.markdown("🌍 **Save the Children International**[cite: 11]")
        st.markdown("🌿 **MSI Reproductive Choices**[cite: 10, 11]")
    with col3:
        st.markdown("📺 **Canal+**[cite: 10]")
        st.markdown("🏛️ **Ministry of Labor and Skills**[cite: 10]")

# --- 4. CAREERS & SALES PARTNERS ---
elif menu == "💼 Careers & Sales Partners":
    st.title("Careers & Partnership Portal")
    st.write("Join our network of elite creative professionals, production crew, or commission-based sales partners.")
    st.markdown("---")
    
    with st.form("hiring_form"):
        st.markdown("### **Application Form**")
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        position = st.selectbox("Applying For", ["Remote Sales Partner", "Cinematographer / DP", "Video Editor", "Production Assistant"])
        portfolio_link = st.text_input("Portfolio / CV Link (Google Drive, LinkedIn, Website)")
        cover_letter = st.text_area("Why should we work with you?")
        
        submitted = st.form_submit_button("Submit Application")
        if submitted:
            if full_name and email and phone:
                st.success(f"Thank you, {full_name}! Your application for '{position}' has been successfully submitted to Semur Production.")
            else:
                st.error("Please fill in all required fields (Name, Email, Phone).")

# --- 5. CONTACT & INQUIRY ---
elif menu == "📥 Contact & Inquiry":
    st.title("Get in Touch")
    st.write("Let's bring your vision to life. Send us a project brief or business inquiry.")
    st.markdown("---")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### **Contact Details**")
        st.write(f"📍 **Location:** {LOCATION}")
        st.write(f"📧 **Email:** {EMAIL}")
        st.write(f"📞 **Phone:** {PHONE}")
        
    with c2:
        with st.form("contact_form"):
            st.markdown("### **Project Inquiry**")
            client_name = st.text_input("Your Name / Organization")
            client_email = st.text_input("Email")
            project_type = st.selectbox("Project Type", ["TV Commercial (TVC)", "Corporate Documentary", "Social Media Content", "Event Production", "Other"])
            message = st.text_area("Project Details & Budget")
            
            send_inquiry = st.form_submit_button("Send Inquiry")
            if send_inquiry:
                if client_name and client_email:
                    st.success("Thank you! Your project inquiry has been sent to our team. We will get back to you shortly.")
                else:
                    st.error("Please provide your name and email.")
