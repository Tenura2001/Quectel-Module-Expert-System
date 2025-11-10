import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Quectel Module Expert System",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced Custom CSS with light, modern design
st.markdown("""
<style>
    /* Main background */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Card styles */
    .card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.08);
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255,255,255,0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 50px rgba(0,0,0,0.12);
    }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        text-align: left;
        border: 2px solid #e8ecef;
        border-radius: 15px;
        padding: 1.2rem 1.5rem;
        background: white;
        color: #2d3748;
        font-weight: 500;
        font-size: 1.05rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    .stButton>button:hover {
        border-color: #667eea;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        transform: translateX(5px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
    }
    
    /* Progress bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    /* Top recommendation card */
    .top-recommendation {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        border-radius: 25px;
        padding: 2.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 15px 50px rgba(168, 237, 234, 0.3);
        border: 3px solid #a8edea;
        position: relative;
        overflow: hidden;
    }
    
    .top-recommendation::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, transparent 70%);
        border-radius: 50%;
        transform: translate(50%, -50%);
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
        padding: 0.5rem 1.2rem;
        border-radius: 25px;
        font-weight: 600;
        font-size: 0.9rem;
        margin: 0.3rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .badge-success {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
    }
    
    .badge-info {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
    }
    
    .badge-feature {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        color: white;
    }
    
    /* Explanation box */
    .explanation-box {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(252, 182, 159, 0.3);
    }
    
    /* Alternative card */
    .alternative-card {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        border-radius: 20px;
        padding: 1.8rem;
        margin-bottom: 1.2rem;
        border: 2px solid #f0f4f8;
        box-shadow: 0 8px 25px rgba(0,0,0,0.06);
        transition: all 0.3s ease;
    }
    
    .alternative-card:hover {
        border-color: #667eea;
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(102, 126, 234, 0.2);
    }
    
    /* Question header */
    .question-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
    }
    
    /* Section headers */
    h1, h2, h3 {
        color: #2d3748;
        font-weight: 700;
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: #2d3748;
        font-weight: 500;
        box-shadow: 0 8px 25px rgba(142, 197, 252, 0.3);
    }
    
    /* Emoji styling */
    .emoji {
        font-size: 1.5rem;
        margin-right: 0.5rem;
    }
    
    /* Score badge */
    .score-badge {
        display: inline-flex;
        align-items: center;
        padding: 0.8rem 1.5rem;
        border-radius: 30px;
        font-size: 1.1rem;
        font-weight: 700;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        box-shadow: 0 8px 20px rgba(240, 147, 251, 0.4);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    /* Feature tags */
    .feature-tag {
        background: white;
        border: 2px solid #e8ecef;
        padding: 0.6rem 1rem;
        border-radius: 12px;
        display: inline-block;
        margin: 0.3rem;
        font-size: 0.9rem;
        color: #4a5568;
        transition: all 0.3s ease;
    }
    
    .feature-tag:hover {
        border-color: #667eea;
        background: #f7fafc;
        transform: translateY(-2px);
    }
    
    /* Reason list */
    .reason-item {
        padding: 0.8rem 1rem;
        background: rgba(255,255,255,0.5);
        border-radius: 12px;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
        font-size: 0.95rem;
        transition: all 0.3s ease;
    }
    
    .reason-item:hover {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        transform: translateX(5px);
    }
    
    /* Navigation buttons */
    .nav-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.8rem 2rem;
        border-radius: 15px;
        border: none;
        font-weight: 600;
        cursor: pointer;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
    }
    
    .nav-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
    }
    
    /* Divider */
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        margin: 2rem 0;
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 6px 20px rgba(0,0,0,0.06);
        border: 2px solid #f0f4f8;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Selection summary */
    .selection-item {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 1rem 1.5rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        border-left: 4px solid #a8edea;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'recommendation' not in st.session_state:
    st.session_state.recommendation = None

# Questions database
questions = [
    {
        'id': 'application',
        'question': 'What is your primary application?',
        'emoji': '🎯',
        'options': [
            ('automotive', '🚗', 'Automotive & Vehicle Tracking'),
            ('industrial', '🏭', 'Industrial IoT & M2M'),
            ('smart_metering', '⚡', 'Smart Metering & Utilities'),
            ('wearable', '⌚', 'Wearables & Consumer IoT'),
            ('asset_tracking', '📦', 'Asset Tracking & Logistics'),
            ('smart_city', '🏙️', 'Smart City Infrastructure'),
            ('medical', '🏥', 'Medical & Healthcare'),
            ('agriculture', '🌾', 'Agriculture & Environment')
        ]
    },
    {
        'id': 'connectivity',
        'question': 'What connectivity type do you need?',
        'emoji': '📡',
        'options': [
            ('5g', '🚀', '5G (High speed, low latency)'),
            ('lte_cat1', '📶', 'LTE Cat 1 (Voice & data balance)'),
            ('lte_cat4', '📡', 'LTE Cat 4 (High throughput)'),
            ('lte_cat6', '🔝', 'LTE Cat 6 (Very high throughput)'),
            ('nbiot', '🔋', 'NB-IoT (Low power, low data)'),
            ('lte_m', '⚖️', 'LTE-M (Balanced power & mobility)'),
            ('gsm', '📞', 'GSM/GPRS (Legacy 2G)')
        ]
    },
    {
        'id': 'power',
        'question': 'What are your power requirements?',
        'emoji': '⚡',
        'options': [
            ('ultra_low', '🔋', 'Ultra-low power (10+ years battery)'),
            ('low', '🔋🔋', 'Low power (2-5 years battery)'),
            ('moderate', '🔌', 'Moderate (powered with battery backup)'),
            ('high', '⚡', 'High performance (continuous power)')
        ]
    },
    {
        'id': 'data_rate',
        'question': 'What data rate do you require?',
        'emoji': '📊',
        'options': [
            ('very_low', '🐌', 'Very Low (<100 kbps) - sensor data'),
            ('low', '🚶', 'Low (100 kbps - 1 Mbps) - telemetry'),
            ('medium', '🚴', 'Medium (1-10 Mbps) - images, audio'),
            ('high', '🚗', 'High (10-150 Mbps) - video streaming'),
            ('very_high', '✈️', 'Very High (150+ Mbps) - HD video')
        ]
    },
    {
        'id': 'gnss',
        'question': 'Do you need GNSS/GPS positioning?',
        'emoji': '🗺️',
        'options': [
            ('yes_high_accuracy', '🎯', 'Yes, high accuracy required'),
            ('yes_standard', '📍', 'Yes, standard accuracy'),
            ('no', '❌', 'No positioning needed')
        ]
    },
    {
        'id': 'environment',
        'question': 'What is your operating environment?',
        'emoji': '🌡️',
        'options': [
            ('extreme', '🔥', 'Extreme (-40°C to +85°C)'),
            ('industrial', '🏭', 'Industrial (-40°C to +75°C)'),
            ('standard', '🏢', 'Standard (-20°C to +60°C)'),
            ('indoor', '🏠', 'Indoor controlled environment')
        ]
    },
    {
        'id': 'budget',
        'question': 'What is your budget constraint?',
        'emoji': '💰',
        'options': [
            ('low', '💵', 'Low cost priority'),
            ('medium', '💳', 'Balanced cost/performance'),
            ('high', '💎', 'Performance priority')
        ]
    },
    {
        'id': 'certifications',
        'question': 'What certifications do you need?',
        'emoji': '✅',
        'options': [
            ('automotive', '🚗', 'Automotive (IATF 16949, AEC-Q100)'),
            ('medical', '🏥', 'Medical (FDA, CE Medical)'),
            ('standard', '✓', 'Standard (CE, FCC, PTCRB)'),
            ('none', '➖', 'No specific requirements')
        ]
    }
]

# Module database
module_database = {
    'RG500Q': {
        'type': '5G',
        'power': 'high',
        'dataRate': 'very_high',
        'gnss': True,
        'temp': 'industrial',
        'cost': 'high',
        'applications': ['automotive', 'industrial', 'smart_city'],
        'features': ['5G Sub-6GHz', 'Up to 2.5 Gbps DL', 'LTE fallback', 'Multi-GNSS'],
        'certifications': ['automotive']
    },
    'AG550Q': {
        'type': '5G',
        'power': 'high',
        'dataRate': 'very_high',
        'gnss': True,
        'temp': 'extreme',
        'cost': 'high',
        'applications': ['automotive'],
        'features': ['Automotive grade', '5G + LTE', 'IATF 16949', 'AEC-Q100'],
        'certifications': ['automotive']
    },
    'EG912Y': {
        'type': 'lte_cat1',
        'power': 'moderate',
        'dataRate': 'medium',
        'gnss': True,
        'temp': 'industrial',
        'cost': 'medium',
        'applications': ['industrial', 'smart_metering', 'asset_tracking'],
        'features': ['LTE Cat 1', '10 Mbps DL', 'Voice support', 'Cost effective'],
        'certifications': ['standard']
    },
    'EC200U': {
        'type': 'lte_cat1',
        'power': 'low',
        'dataRate': 'medium',
        'gnss': True,
        'temp': 'industrial',
        'cost': 'low',
        'applications': ['asset_tracking', 'wearable', 'smart_city'],
        'features': ['Compact', 'LCC package', 'Ultra-compact', 'Low cost'],
        'certifications': ['standard']
    },
    'BG95': {
        'type': 'nbiot',
        'power': 'ultra_low',
        'dataRate': 'very_low',
        'gnss': True,
        'temp': 'industrial',
        'cost': 'low',
        'applications': ['smart_metering', 'agriculture', 'asset_tracking'],
        'features': ['NB-IoT + LTE-M', 'PSM mode', '10 year battery', 'Global bands'],
        'certifications': ['standard']
    },
    'BG77': {
        'type': 'nbiot',
        'power': 'ultra_low',
        'dataRate': 'very_low',
        'gnss': False,
        'temp': 'industrial',
        'cost': 'low',
        'applications': ['smart_metering', 'agriculture'],
        'features': ['NB-IoT only', 'Ultra-low power', 'Cost optimized', 'Compact'],
        'certifications': ['standard']
    },
    'BG600L': {
        'type': 'lte_m',
        'power': 'low',
        'dataRate': 'low',
        'gnss': True,
        'temp': 'industrial',
        'cost': 'medium',
        'applications': ['asset_tracking', 'wearable', 'medical'],
        'features': ['LTE-M', 'Voice capable', 'Mobility support', 'PSM/eDRX'],
        'certifications': ['standard', 'medical']
    },
    'EC25': {
        'type': 'lte_cat4',
        'power': 'moderate',
        'dataRate': 'high',
        'gnss': True,
        'temp': 'industrial',
        'cost': 'medium',
        'applications': ['industrial', 'smart_city', 'asset_tracking'],
        'features': ['LTE Cat 4', '150 Mbps DL', 'Reliable', 'Proven design'],
        'certifications': ['standard']
    },
    'EG915U': {
        'type': 'lte_cat4',
        'power': 'moderate',
        'dataRate': 'high',
        'gnss': True,
        'temp': 'industrial',
        'cost': 'medium',
        'applications': ['industrial', 'automotive', 'smart_city'],
        'features': ['LTE Cat 4', 'North America optimized', 'Industrial grade'],
        'certifications': ['standard']
    },
    'MC60': {
        'type': 'gsm',
        'power': 'low',
        'dataRate': 'very_low',
        'gnss': True,
        'temp': 'industrial',
        'cost': 'low',
        'applications': ['asset_tracking', 'smart_metering'],
        'features': ['GSM/GPRS', 'Compact', 'Legacy support', 'Ultra-low cost'],
        'certifications': ['standard']
    }
}

def expert_rules(user_answers):
    """Apply expert system rules to recommend modules"""
    scores = {}
    
    connectivity_map = {
        '5g': '5G',
        'lte_cat1': 'lte_cat1',
        'lte_cat4': 'lte_cat4',
        'lte_cat6': 'lte_cat4',
        'nbiot': 'nbiot',
        'lte_m': 'lte_m',
        'gsm': 'gsm'
    }
    
    power_map = {
        'ultra_low': ['nbiot', 'lte_m', 'gsm'],
        'low': ['nbiot', 'lte_m', 'gsm', 'lte_cat1'],
        'moderate': ['lte_cat1', 'lte_cat4'],
        'high': ['5G', 'lte_cat4', 'lte_cat6']
    }
    
    data_rate_score = {
        'very_low': {'nbiot': 10, 'gsm': 10, 'lte_m': 8},
        'low': {'lte_m': 10, 'lte_cat1': 10, 'nbiot': 5},
        'medium': {'lte_cat1': 10, 'lte_cat4': 10},
        'high': {'lte_cat4': 10, 'lte_cat6': 10, '5G': 8},
        'very_high': {'5G': 10, 'lte_cat6': 8}
    }
    
    temp_match = {
        'extreme': ['extreme'],
        'industrial': ['extreme', 'industrial'],
        'standard': ['extreme', 'industrial', 'standard'],
        'indoor': ['extreme', 'industrial', 'standard', 'indoor']
    }
    
    budget_match = {
        'low': ['low'],
        'medium': ['low', 'medium'],
        'high': ['low', 'medium', 'high']
    }
    
    for module, data in module_database.items():
        score = 0
        reasons = []
        
        # Rule 1: Connectivity match (40 points)
        if data['type'] == connectivity_map.get(user_answers.get('connectivity')):
            score += 40
            reasons.append(f"✨ Matches required {user_answers['connectivity'].upper()} connectivity")
        
        # Rule 2: Application match (25 points)
        if user_answers.get('application') in data['applications']:
            score += 25
            reasons.append(f"🎯 Optimized for {user_answers['application'].replace('_', ' ')} applications")
        
        # Rule 3: Power requirements (15 points)
        if data['type'] in power_map.get(user_answers.get('power'), []):
            score += 15
            reasons.append(f"⚡ Power consumption suits {user_answers['power'].replace('_', ' ')} requirement")
        
        # Rule 4: Data rate match (10 points)
        rate_score = data_rate_score.get(user_answers.get('data_rate'), {}).get(data['type'], 0)
        score += rate_score
        if rate_score > 0:
            reasons.append(f"📊 Data rate matches {user_answers['data_rate'].replace('_', ' ')} requirement")
        
        # Rule 5: GNSS requirement (5 points)
        if user_answers.get('gnss') == 'no' or data['gnss']:
            score += 5
            if user_answers.get('gnss') != 'no' and data['gnss']:
                reasons.append('📍 Includes integrated GNSS positioning')
        
        # Rule 6: Temperature rating (3 points)
        if data['temp'] in temp_match.get(user_answers.get('environment'), []):
            score += 3
            reasons.append(f"🌡️ Temperature rating supports {user_answers['environment']} environment")
        
        # Rule 7: Budget constraint (2 points)
        if data['cost'] in budget_match.get(user_answers.get('budget'), []):
            score += 2
            reasons.append(f"💰 Price point fits {user_answers['budget']} budget")
        
        # Rule 8: Certifications bonus (5 points)
        if user_answers.get('certifications') != 'none' and \
           user_answers.get('certifications') in data['certifications']:
            score += 5
            reasons.append(f"✅ Has required {user_answers['certifications']} certifications")
        
        scores[module] = {
            'score': score,
            'reasons': reasons,
            'data': data
        }
    
    # Sort by score and return top 3
    sorted_modules = sorted(scores.items(), key=lambda x: x[1]['score'], reverse=True)[:3]
    return sorted_modules

def handle_answer(question_id, value):
    """Handle user answer and advance to next question"""
    st.session_state.answers[question_id] = value
    
    if st.session_state.current_step < len(questions) - 1:
        st.session_state.current_step += 1
    else:
        # Calculate recommendation
        st.session_state.recommendation = expert_rules(st.session_state.answers)
    st.rerun()

def reset():
    """Reset the expert system"""
    st.session_state.current_step = 0
    st.session_state.answers = {}
    st.session_state.recommendation = None
    st.rerun()

def go_back():
    """Go back to previous question"""
    if st.session_state.current_step > 0:
        st.session_state.current_step -= 1
        st.rerun()

# Main application
st.markdown("""
<div style='text-align: center; padding: 2rem 0;'>
    <h1 style='font-size: 3rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
        📡 Quectel Module Expert System
    </h1>
    <p style='font-size: 1.2rem; color: #718096;'>Smart module selection powered by AI reasoning</p>
</div>
""", unsafe_allow_html=True)

# Show recommendation if available
if st.session_state.recommendation:
    # Header with reset button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Start New Assessment", use_container_width=True, type="primary"):
            reset()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Top recommendation
    top_module = st.session_state.recommendation[0]
    module_name = top_module[0]
    module_info = top_module[1]
    
    st.markdown(f"""
    <div class="top-recommendation">
        <div style='display: flex; align-items: center; margin-bottom: 1rem;'>
            <span style='font-size: 3rem; margin-right: 1rem;'>🏆</span>
            <div>
                <h1 style='margin: 0; color: #2d3748;'>{module_name}</h1>
                <p style='margin: 0; font-size: 1.1rem; color: #4a5568;'>Your Perfect Match</p>
            </div>
        </div>
        <div style='margin-top: 1.5rem;'>
            <span class='score-badge'>✨ {module_info['score']}% Confidence Match</span>
            <span class='badge badge-info' style='margin-left: 1rem;'>{module_info['data']['type'].upper()}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Main content in two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='card'>
            <h2 style="color: black;">🎨 Key Features</h2>
        </div>
        """, unsafe_allow_html=True)
        
        features_html = "<div style='display: flex; flex-wrap: wrap; gap: 0.5rem;'>"
        for feature in module_info['data']['features']:
            features_html += f"<span class='feature-tag'>✓ {feature}</span>"
        features_html += "</div>"
        st.markdown(features_html, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='card'>
            <h2 style="color: black">💡 Why This Module?</h2>
        </div>
        """, unsafe_allow_html=True)
        
        for reason in module_info['reasons']:
            st.markdown(f"<div class='reason-item'>{reason}</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Alternative options
    st.markdown("""
    <div class='card'>
        <h2 style="color:#718096">🔀 Alternative Options</h2>
        <p style='color: #718096;'>Here are other modules that might suit your needs</p>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(2)
    for idx, (alt_module, alt_info) in enumerate(st.session_state.recommendation[1:]):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class='alternative-card'>
                <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
                    <h3 style='margin: 0;'>{alt_module}</h3>
                    <span class='badge badge-success'>{alt_info['score']}%</span>
                </div>
                <div style='margin-bottom: 1rem;'>
                    <span class='badge badge-info'>{alt_info['data']['type'].upper()}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander("📋 View Details", expanded=False):
                st.markdown("**Features:**")
                for feature in alt_info['data']['features']:
                    st.markdown(f"• {feature}")
                st.markdown("<br>**Matching Reasons:**", unsafe_allow_html=True)
                for reason in alt_info['reasons'][:3]:
                    st.markdown(f"• {reason}")

else:
    # Show current question
    current_q = questions[st.session_state.current_step]
    
    # Progress section
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        progress = (st.session_state.current_step + 1) / len(questions)
        st.progress(progress)
        
        st.markdown(f"""
        <div style='text-align: center; margin-top: 0.5rem;'>
            <p style='color: #718096; font-size: 0.9rem;'>
                Question {st.session_state.current_step + 1} of {len(questions)}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Question card
    st.markdown(f"""
    <div class='question-header'>
        <div style='text-align: center;'>
            <span style='font-size: 3rem;'>{current_q['emoji']}</span>
            <h2 style='color: white; margin-top: 1rem;'>{current_q['question']}</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Options in a centered container
    col1, col2, col3 = st.columns([0.5, 3, 0.5])
    
    with col2:
        for value, emoji, label in current_q['options']:
            if st.button(f"{emoji}  {label}", key=value, use_container_width=True):
                handle_answer(current_q['id'], value)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Navigation and selections
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.session_state.current_step > 0:
            if st.button("← Previous Question", use_container_width=True):
                go_back()
    
    # Show current selections
    if st.session_state.answers:
        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander("📝 Your Selections Summary", expanded=False):
            for q_id, answer in st.session_state.answers.items():
                q = next((q for q in questions if q['id'] == q_id), None)
                if q:
                    option_data = next(((val, emoji, label) for val, emoji, label in q['options'] if val == answer), None)
                    if option_data:
                        st.markdown(f"""
                        <div class='selection-item'>
                            <strong>{q['emoji']} {q['question']}</strong><br>
                            <span style='color: #718096;'>{option_data[1]} {option_data[2]}</span>
                        </div>
                        """, unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 2rem; color: #a0aec0; font-size: 0.9rem;'>
    <p>Powered by Expert System AI | Quectel IoT Solutions</p>
</div>
""", unsafe_allow_html=True)
