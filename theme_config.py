import streamlit as st

def apply_vibrant_light_theme():
    """Apply vibrant light theme with colorful elements"""
    
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Global styles */
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Main app background - Light gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Main content container - Light theme */
    .main .block-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 2rem;
        margin-top: 2rem;
        box-shadow: 
            0 20px 40px rgba(0,0,0,0.1),
            0 0 0 1px rgba(255,255,255,0.2);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Sidebar - Vibrant gradient */
    .css-1d391kg {
        background: linear-gradient(180deg, 
            #FF6B6B 0%, 
            #4ECDC4 25%, 
            #45B7D1 50%, 
            #96CEB4 75%, 
            #FECA57 100%);
        background-size: 100% 400%;
        animation: gradientShift 20s ease infinite;
    }
    
    /* Sidebar content styling */
    .css-1d391kg .stMarkdown {
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    /* Headers with rainbow effects */
    h1 {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FECA57, #FF9FF3);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientShift 10s ease infinite;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        font-size: 3.5rem !important;
    }
    
    h2 {
        color: #2c3e50;
        font-weight: 600;
        margin: 1.5rem 0 1rem 0;
        position: relative;
        padding-left: 1rem;
    }
    
    h2::before {
        content: '';
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 4px;
        height: 100%;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        border-radius: 2px;
    }
    
    h3 {
        color: #34495e;
        font-weight: 600;
        margin: 1rem 0;
    }
    
    h4 {
        color: #7f8c8d;
        font-weight: 500;
    }
    
    /* Vibrant metric containers */
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(255,107,107,0.1), rgba(78,205,196,0.1));
        border: 2px solid transparent;
        background-clip: padding-box;
        border-radius: 20px;
        padding: 1.5rem;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
    }
    
    div[data-testid="metric-container"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4);
        background-size: 400% 400%;
        animation: gradientShift 8s ease infinite;
        z-index: -1;
        opacity: 0.1;
    }
    
    /* Enhanced info/success/warning/error boxes */
    .stInfo {
        background: linear-gradient(135deg, rgba(69,183,209,0.15), rgba(78,205,196,0.15));
        border-left: 5px solid #45B7D1;
        border-radius: 15px;
        padding: 1rem;
        box-shadow: 0 8px 25px rgba(69,183,209,0.2);
    }
    
    .stSuccess {
        background: linear-gradient(135deg, rgba(150,206,180,0.15), rgba(78,205,196,0.15));
        border-left: 5px solid #96CEB4;
        border-radius: 15px;
        padding: 1rem;
        box-shadow: 0 8px 25px rgba(150,206,180,0.2);
    }
    
    .stWarning {
        background: linear-gradient(135deg, rgba(254,202,87,0.15), rgba(255,107,107,0.15));
        border-left: 5px solid #FECA57;
        border-radius: 15px;
        padding: 1rem;
        box-shadow: 0 8px 25px rgba(254,202,87,0.2);
    }
    
    .stError {
        background: linear-gradient(135deg, rgba(255,107,107,0.15), rgba(255,159,243,0.15));
        border-left: 5px solid #FF6B6B;
        border-radius: 15px;
        padding: 1rem;
        box-shadow: 0 8px 25px rgba(255,107,107,0.2);
    }
    
    /* Vibrant buttons */
    .stButton > button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(0,0,0,0.2);
        background: linear-gradient(45deg, #4ECDC4, #FF6B6B);
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    /* Enhanced input styling */
    .stTextInput > div > div > input {
        border: 2px solid transparent;
        background: linear-gradient(white, white) padding-box,
                   linear-gradient(45deg, #FF6B6B, #4ECDC4) border-box;
        border-radius: 15px;
        padding: 0.75rem 1rem;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    
    .stTextInput > div > div > input:focus {
        outline: none;
        box-shadow: 0 8px 25px rgba(78,205,196,0.3);
        transform: translateY(-2px);
    }
    
    /* Select box styling */
    .stSelectbox > div > div {
        border: 2px solid transparent;
        background: linear-gradient(white, white) padding-box,
                   linear-gradient(45deg, #96CEB4, #45B7D1) border-box;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background: rgba(255,255,255,0.1);
        padding: 0.5rem;
        border-radius: 20px;
        backdrop-filter: blur(10px);
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0 1.5rem;
        background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1));
        border-radius: 15px;
        color: #333;
        font-weight: 600;
        border: 1px solid rgba(255,255,255,0.2);
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255,107,107,0.3);
    }
    
    /* Progress bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #FF6B6B, #FECA57, #4ECDC4, #96CEB4);
        background-size: 200% 100%;
        animation: progressShine 2s ease infinite;
    }
    
    @keyframes progressShine {
        0% { background-position: 200% 0; }
        100% { background-position: -200% 0; }
    }
    
    /* Custom card class */
    .custom-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(20px);
        padding: 1.5rem;
        border-radius: 20px;
        box-shadow: 
            0 15px 35px rgba(0,0,0,0.1),
            0 0 0 1px rgba(255,255,255,0.3);
        margin-bottom: 1rem;
        border: 1px solid rgba(255,255,255,0.2);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .custom-card:hover {
        transform: translateY(-5px);
        box-shadow: 
            0 20px 45px rgba(0,0,0,0.15),
            0 0 0 1px rgba(255,255,255,0.4);
    }
    
    .custom-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FECA57);
        background-size: 200% 100%;
        animation: gradientShift 5s ease infinite;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, rgba(78,205,196,0.1), rgba(150,206,180,0.1));
        border-radius: 15px;
        border: 2px solid rgba(78,205,196,0.2);
        transition: all 0.3s ease;
    }
    
    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, rgba(78,205,196,0.2), rgba(150,206,180,0.2));
        transform: translateY(-2px);
    }
    
    /* Dataframe styling */
    .stDataFrame {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    
    /* Text area styling */
    .stTextArea > div > div > textarea {
        border: 2px solid transparent;
        background: linear-gradient(white, white) padding-box,
                   linear-gradient(45deg, #96CEB4, #45B7D1) border-box;
        border-radius: 15px;
        padding: 1rem;
        font-family: 'Poppins', sans-serif;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    
    .stTextArea > div > div > textarea:focus {
        outline: none;
        box-shadow: 0 8px 25px rgba(150,206,180,0.3);
    }
    
    /* Slider styling */
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
        border-radius: 10px;
    }
    
    /* Toggle styling */
    .stCheckbox > label {
        font-weight: 500;
        color: #2c3e50;
    }
    
    /* Radio button styling */
    .stRadio > label {
        font-weight: 500;
        color: #2c3e50;
    }
    
    /* Multi-select styling */
    .stMultiSelect > div > div {
        border: 2px solid transparent;
        background: linear-gradient(white, white) padding-box,
                   linear-gradient(45deg, #FECA57, #FF9FF3) border-box;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
        background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
        border-radius: 20px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        border-radius: 10px;
        border: 2px solid rgba(255,255,255,0.2);
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(45deg, #4ECDC4, #FF6B6B);
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem;
            margin-top: 1rem;
        }
        
        h1 {
            font-size: 2.5rem !important;
        }
        
        .stButton > button {
            padding: 0.5rem 1.5rem;
            font-size: 0.9rem;
        }
    }
    
    /* Animation for elements */
    .animate-fade-in {
        animation: fadeIn 0.8s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Pulse animation for important elements */
    .pulse {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(255,107,107,0.7); }
        70% { box-shadow: 0 0 0 10px rgba(255,107,107,0); }
        100% { box-shadow: 0 0 0 0 rgba(255,107,107,0); }
    }
    
    /* Glow effect for special elements */
    .glow {
        box-shadow: 0 0 20px rgba(78,205,196,0.5);
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { box-shadow: 0 0 20px rgba(78,205,196,0.5); }
        to { box-shadow: 0 0 30px rgba(78,205,196,0.8); }
    }
    </style>
    """, unsafe_allow_html=True)
