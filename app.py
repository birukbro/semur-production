import streamlit as st
import os

# Page Configuration (Zero Symbols / No Page Icons)
st.set_page_config(
    page_title="Semur Production | Global Standard Studio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Styling (Dark Luxury Cinematic Theme: Zero Icons/Symbols, Transparent Logo Integration, Professional Opacity Styling)
st.markdown("""
    <style>
    .main {
        background-color: #050505;
        color: #ffffff;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #ffffff !important;
    }
    
    /* Luxury Header Navigation Bar (Zero Icons) */
    .top-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #0b0b0b;
        padding: 15px 30px;
        border-bottom: 1px solid #222222;
        border-radius: 4px;
        margin-bottom: 30px;
    }
    .brand-title {
        color: #d4af37 !important;
        font-size: 22px;
        font-weight: 800;
        letter-spacing: 2px;
        margin: 0;
    }
    .nav-links {
        display: flex;
        gap: 25px;
        font-size: 13px;
        font-weight: 600;
        letter-spacing: 1px;
    }
    .nav-links span {
        color: #cccccc !important;
        cursor: pointer;
        transition: 0.3s;
    }
    .nav-links span:hover {
        color: #d4af37 !important;
    }
    .quote-btn {
        background: transparent;
        color: #d4af37 !important;
        border: 1px solid #d4af37;
        padding: 8px 18px;
        font-size: 12px;
        font-weight: bold;
        letter-spacing: 1px;
        border-radius: 4px;
    }

    /* Streamlit Tabs Customization */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: #0b0b0b;
        padding: 10px;
        border-radius: 6px;
        border-bottom: 2px solid #d4af37;
    }
    .stTabs [data-baseweb="tab"] {
        height: 40px;
        background-color: transparent;
        color: #ffffff !important;
        font-weight: 600;
        font-size: 14px;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #d4af37 0%, #aa820a 100%) !important;
        color: #000000 !important;
        border-radius: 4px;
    }

    /* Luxury Gold Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #d4af37 0%, #aa820a 100%);
        color: #000000;
        font-weight: bold;
        border: none;
        padding: 0.6rem 1.8rem;
        border-radius: 4px;
        letter-spacing: 1px;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #f3c643 0%, #d4af37 100%);
        color: #000;
    }
    
    /* Cinematic Card Boxes */
    .cinematic-box {
        background-color: #0f0f0f;
        border: 1px solid #222222;
        padding: 20px;
        border-radius: 6px;
        border-left: 3px solid #d4af37;
        margin-bottom: 15px;
    }
    
    /* Transparent Logo & Professional Image Styling */
    .client-logo-card {
        background-color: #0f0f0f;
        padding: 25px;
        border-radius: 6px;
        border: 1px solid #222222;
        margin-bottom: 20px;
        text-align: center;
    }
    .client-logo-card img {
        mix-blend-mode: screen;
        max-width: 130px;
        height: auto;
    }
    
    /* Founder Cinematic Art Styling with Opacity & Blending */
    .founder-art-container {
        position: relative;
        text-align: center;
    }
    .founder-art-container img {
        opacity: 0.92;
        filter: contrast(1.05);
        border-radius: 4px;
        border: 1px solid #222222;
    }
    </style>
""", unsafe_allow_html=True)

# Contact & Profile Info
LOCATION = "Addis Ababa, Ethiopia"
EMAIL = "birukbelachew1921@gmail.com"
PHONE_1 = "+251 927 256 139"
PHONE_2 = "+251 711 256 139"
WEB_URL = "semur-production.streamlit.app"

# Top Luxury Navigation Header (Zero Icons)
st.markdown("""
    <div class="top-nav">
        <div>
            <h3 class="brand-title">SEMUR PRODUCTION</h3>
        </div>
        <div class="nav-links">
            <span>SERVICES</span>
            <span>PORTFOLIO</span>
            <span>TEAM</span>
            <span>CAREERS</span>
            <span>CONTACT</span>
        </div>
        <div>
            <button class="quote-btn">REQUEST QUOTE</button>
        </div>
    </div>
""", unsafe_allow_html=True)

# Navigation Menu Tabs
menu_tabs = [
    "Home / Profile", 
    "Mission & Vision", 
    "Services & Pricing", 
    "Trusted Clients", 
    "Careers & Partners", 
    "Contact & Inquiry"
]

tab_home, tab_mission, tab_services, tab_clients, tab_careers, tab_contact = st.tabs(menu_tabs)

# --- 1. HOME / PROFILE ---
with tab_home:
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.markdown("<h1 style='color: #d4af37; font-size: 42px; font-weight: 800; line-height: 1.1; letter-spacing: 1px;'>EMPOWERING CINEMATIC ENTERPRISES</h1>", unsafe_allow_html=True)
        st.write("Bring Narration to Life. We deliver premier executive film production, advanced commercial art direction, and strategic media solutions to market leaders.")
        st.markdown(f"<p style='color: #cccccc;'><b>Location:</b> {LOCATION}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #cccccc;'><b>Official Web Link:</b> <code>{WEB_URL}</code></p>", unsafe_allow_html=True)
        
        btn_col1, btn_col2 = st.columns([1, 1])
        with btn_col1:
            if st.button("GET STARTED"):
                st.success("Welcome to Semur Production Studio!")
        with btn_col2:
            st.markdown("<div style='padding-top: 10px;'><a href='#services' style='color: #d4af37; text-decoration: none; font-weight: bold; letter-spacing: 1px;'>LEARN MORE &rarr;</a></div>", unsafe_allow_html=True)
            
    with col2:
        st.markdown("<div class='founder-art-container'>", unsafe_allow_html=True)
        if os.path.exists("image_6561ba.png"):
            st.image("image_6561ba.png", use_container_width=True)
        else:
            st.warning("Please upload your cropped professional founder photo and name it 'image_6561ba.png' in GitHub.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<hr style='border-color: #222222; margin: 40px 0;'>", unsafe_allow_html=True)
    
    # Impact Metrics Section (Zero Icons)
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown("<h3 style='color: #d4af37; margin:0; font-size: 26px;'>3+ Years</h3><p style='color:#888; font-size:11px; letter-spacing: 1px;'>Industry Excellence</p>", unsafe_allow_html=True)
    with m2:
        st.markdown("<h3 style='color: #d4af37; margin:0; font-size: 26px;'>26 Projects</h3><p style='color:#888; font-size:11px; letter-spacing: 1px;'>Completed Successfully</p>", unsafe_allow_html=True)
    with m3:
        st.markdown("<h3 style='color: #d4af37; margin:0; font-size: 26px;'>100%</h3><p style='color:#888; font-size:11px; letter-spacing: 1px;'>Client Satisfaction</p>", unsafe_allow_html=True)
    with m4:
        st.markdown("<h3 style='color: #d4af37; margin:0; font-size: 26px;'>Hollywood</h3><p style='color:#888; font-size:11px; letter-spacing: 1px;'>Standard Quality</p>", unsafe_allow_html=True)
        
    st.markdown("<hr style='border-color: #222222; margin: 40px 0;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #d4af37; letter-spacing: 1px;'>FOUNDER PROFILE</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 16px; font-weight: 600;'>Biruk Belachew &mdash; Company Founder and Producer</p>", unsafe_allow_html=True)

# --- 2. MISSION & VISION ---
with tab_mission:
    st.markdown("<h2 style='color: #d4af37; letter-spacing: 1px;'>Mission, Vision & Core Values</h2>", unsafe_allow_html=True)
    st.write("The guiding principles and cinematic philosophy behind Semur Production.")
    st.markdown("<hr style='border-color: #222222; margin: 20px 0;'>", unsafe_allow_html=True)
    
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.markdown("<div class='cinematic-box'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #d4af37;'>Our Mission</h3>", unsafe_allow_html=True)
        st.write("To empower global and local brands by connecting them with their audiences through meaningful, high-impact, and cinematic storytelling.")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='cinematic-box'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #d4af37;'>Our Vision</h3>", unsafe_allow_html=True)
        st.write("To become the most trusted and premier creative production partner in the region, known for uncompromising quality and artistic innovation.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_m2:
        st.markdown("<div class='cinematic-box'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #d4af37;'>Core Values</h3>", unsafe_allow_html=True)
        st.write("- Quality: Executing every frame with Hollywood-grade standards.")
        st.write("- Perfection: Meticulous attention to detail in set design, art direction, and post-production.")
        st.write("- Innovation: Pushing creative boundaries with advanced production techniques.")
        st.write("- Cultural Authenticity: Honoring local narratives with international appeal.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- 3. SERVICES & PRICING ---
with tab_services:
    st.markdown("<h2 style='color: #d4af37; letter-spacing: 1px;'>Services & Production Packages</h2>", unsafe_allow_html=True)
    st.write("Elite production quality tailored to commercial brands, filmmakers, and digital creators.")
    st.markdown("<hr style='border-color: #222222; margin: 20px 0;'>", unsafe_allow_html=True)
    
    s1, s2, s3, s4, s5 = st.tabs([
        "TV Commercials", 
        "Documentaries", 
        "Event Production", 
        "Film Production",
        "Social Media Content"
    ])
    
    with s1:
        st.markdown("<div class='cinematic-box'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #d4af37;'>TV Commercials & Brand Campaigns</h3>", unsafe_allow_html=True)
        st.write("Concept development, scriptwriting, high-end camera & lighting setup, professional voiceover, and full cinematic grading.")
        st.markdown("<p style='color: #d4af37; font-weight: bold; margin-top: 15px;'>Estimated Investment: 400,000 ETB – 3,500,000 ETB</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
            
    with s2:
        st.markdown("<div class='cinematic-box'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #d4af37;'>Corporate Documentaries</h3>", unsafe_allow_html=True)
        st.write("In-depth storytelling, interview stage design, professional field recording, and documentary editing.")
        st.markdown("<p style='color: #d4af37; font-weight: bold; margin-top: 15px;'>Estimated Investment: 350,000 ETB – 4,000,000 ETB</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with s3:
        st.markdown("<div class='cinematic-box'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #d4af37;'>Event Production</h3>", unsafe_allow_html=True)
        st.write("Full-scale event cinematic coverage, set construction, prop fabrication, and professional execution.")
        st.markdown("<p style='color: #d4af37; font-weight: bold; margin-top: 15px;'>Estimated Investment: 50,000 ETB – 350,000 ETB per day</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with s4:
        st.markdown("<div class='cinematic-box'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #d4af37;'>Film Production</h3>", unsafe_allow_html=True)
        st.write("Feature and short film production, artistic direction, and end-to-end cinematic execution.")
        st.markdown("<p style='color: #d4af37; font-weight: bold; margin-top: 15px;'>Estimated Investment: Pricing upon consultation (Depends on film scale and scope)</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
            
    with s5:
        st.markdown("<div class='cinematic-box'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #d4af37;'>Social Media Content & Movie Recaps</h3>", unsafe_allow_html=True)
        st.write("High-retention editing, thumbnail conceptualization, dynamic motion graphics, and audio mixing.")
        st.markdown("<p style='color: #d4af37; font-weight: bold; margin-top: 15px;'>Estimated Investment: 60,000 ETB – 120,000 ETB</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# --- 4. TRUSTED CLIENTS (Transparent PNG Logos Only, Zero Text Names) ---
with tab_clients:
    st.markdown("<h2 style='color: #d4af37; letter-spacing: 1px;'>Client Success & Trusted Partners</h2>", unsafe_allow_html=True)
    st.write("We take pride in partnering with leading organizations, institutions, and corporations.")
    st.markdown("<hr style='border-color: #222222; margin: 20px 0;'>", unsafe_allow_html=True)
    
    client_logos = [
        "save_the_children.png",
        "canal_plus.png",
        "awash_bank.png",
        "msi_ethiopia.png",
        "hibret_insurance.png",
        "abay_bank.png",
        "mols_ethiopia.png",
        "africom.png",
        "acufada.png"
    ]
    
    cols = st.columns(3)
    for idx, logo_file in enumerate(client_logos):
        with cols[idx % 3]:
            st.markdown("<div class='client-logo-card'>", unsafe_allow_html=True)
            if os.path.exists(logo_file):
                st.image(logo_file, width=130)
            else:
                st.markdown(f"<p style='color: #666; font-size: 11px; margin: 0;'>[ Logo: {logo_file} ]</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

# --- 5. CAREERS & PARTNERS ---
with tab_careers:
    st.markdown("<h2 style='color: #d4af37; letter-spacing: 1px;'>Careers & Partnership Portal</h2>", unsafe_allow_html=True)
    st.write("Join our professional management, production crew, creative departments, or sales partner network.")
    st.markdown("<hr style='border-color: #222222; margin: 20px 0;'>", unsafe_allow_html=True)
    
    with st.form("hiring_form"):
        st.markdown("<h3 style='color: #d4af37;'>Professional Application Form</h3>", unsafe_allow_html=True)
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        
        categorized_roles = [
            "Chief Executive Officer (CEO)",
            "Operations Manager",
            "Accountant / Financial Officer",
            "Marketing Specialist",
            "Remote Sales Partner",
            "Director",
            "Producer",
            "Production Manager",
            "Cinematographer / Director of Photography (DP)",
            "Video Editor",
            "Soundman / Audio Engineer",
            "Gaffer / Lighting Technician",
            "Makeup Artist",
            "Production Assistant",
            "Logistics Coordinator",
            "Catering Specialist",
            "Driver / Transportation",
            "Computer Science Expert / Developer",
            "Graphics Designer"
        ]
        
        position = st.selectbox("Applying For / Role", categorized_roles)
        portfolio_link = st.text_input("Portfolio / CV Link (Google Drive, LinkedIn, Website)")
        cover_letter = st.text_area("Why should we work with you?")
        
        submitted = st.form_submit_button("Submit Application")
        if submitted:
            if full_name and email and phone:
                st.success(f"Thank you, {full_name}! Your application for '{position}' has been successfully submitted to Semur Production.")
            else:
                st.error("Please fill in all required fields (Name, Email, Phone).")

# --- 6. CONTACT & INQUIRY ---
with tab_contact:
    st.markdown("<h2 style='color: #d4af37; letter-spacing: 1px;'>Get in Touch</h2>", unsafe_allow_html=True)
    st.write("Let's bring your vision to life. Send us a project brief or business inquiry.")
    st.markdown("<hr style='border-color: #222222; margin: 20px 0;'>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='cinematic-box'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #d4af37;'>Contact Details</h3>", unsafe_allow_html=True)
        st.write(f"**Location:** {LOCATION}")
        st.write(f"**Phone 1:** `{PHONE_1}`")
        st.write(f"**Phone 2:** `{PHONE_2}`")
        st.write(f"**Email:** `{EMAIL}`")
        st.write(f"**Web Link:** `{WEB_URL}`")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='cinematic-box'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #d4af37;'>Social Media Channels</h3>", unsafe_allow_html=True)
        st.markdown("""
        - Telegram: @SemurProduction
        - TikTok: @SemurProduction
        - Instagram: @SemurProduction
        - Facebook: Semur Production
        - LinkedIn: Semur Production
        - WhatsApp: +251 927 256 139
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with c2:
        with st.form("contact_form"):
            st.markdown("<h3 style='color: #d4af37;'>Project Inquiry</h3>", unsafe_allow_html=True)
            client_name = st.text_input("Your Name / Organization")
            client_email = st.text_input("Email")
            project_type = st.selectbox("Project Type", ["TV Commercial (TVC)", "Corporate Documentary", "Event Production", "Film Production", "Social Media Content"])
            message = st.text_area("Project Details & Budget")
            
            send_inquiry = st.form_submit_button("Send Inquiry")
            if send_inquiry:
                if client_name and client_email:
                    st.success("Thank you! Your project inquiry has been sent to our team. We will get back to you shortly.")
                else:
                    st.error("Please provide your name and email.")