import streamlit as st
from experta import *

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
    
    /* Selection summary */
    .selection-item {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 1rem 1.5rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        border-left: 4px solid #a8edea;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    /* Rules fired section */
    .rule-fired {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            
        padding: 1rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        border-left: 4px solid #fc8181;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# EXPERTA EXPERT SYSTEM DEFINITION
# ============================================================================

# Define Facts
class UserRequirements(Fact):
    """User's requirements for IoT module"""
    pass

class ModuleRecommendation(Fact):
    """Module recommendation with score"""
    pass

# Define the Expert System
class QuectelExpertSystem(KnowledgeEngine):
    """Expert System for Quectel Module Selection using Experta"""
    
    def __init__(self):
        super().__init__()
        self.recommendations = {}
        self.rules_fired = []
        
    # Module Database
    module_db = {
        'RG500Q': {
            'type': '5G',
            'power': 'high',
            'dataRate': 'very_high',
            'gnss': True,
            'temp': 'industrial',
            'cost': 'high',
            'applications': ['automotive', 'industrial', 'smart_city'],
            'features': ['5G Sub-6GHz', 'Up to 2.5 Gbps DL', 'LTE fallback', 'Multi-GNSS'],
            'certifications': ['automotive', 'standard']
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
    
    # RULE 1: Connectivity Match - 5G (Weight: 40)
    @Rule(UserRequirements(connectivity='5g'))
    def recommend_5g_modules(self):
        self.rules_fired.append("RULE 1: 5G connectivity requirement detected")
        for module, data in self.module_db.items():
            if data['type'] == '5G':
                self._add_score(module, 40, "Matches required 5G connectivity")
    
    # RULE 2: Connectivity Match - LTE Cat 1
    @Rule(UserRequirements(connectivity='lte_cat1'))
    def recommend_lte_cat1_modules(self):
        self.rules_fired.append("RULE 2: LTE Cat 1 connectivity requirement detected")
        for module, data in self.module_db.items():
            if data['type'] == 'lte_cat1':
                self._add_score(module, 40, "Matches required LTE Cat 1 connectivity")
    
    # RULE 3: Connectivity Match - LTE Cat 4
    @Rule(UserRequirements(connectivity=L('lte_cat4') | L('lte_cat6')))
    def recommend_lte_cat4_modules(self):
        self.rules_fired.append("RULE 3: LTE Cat 4/6 connectivity requirement detected")
        for module, data in self.module_db.items():
            if data['type'] == 'lte_cat4':
                self._add_score(module, 40, "Matches required LTE Cat 4 connectivity")
    
    # RULE 4: Connectivity Match - NB-IoT
    @Rule(UserRequirements(connectivity='nbiot'))
    def recommend_nbiot_modules(self):
        self.rules_fired.append("RULE 4: NB-IoT connectivity requirement detected")
        for module, data in self.module_db.items():
            if data['type'] == 'nbiot':
                self._add_score(module, 40, "Matches required NB-IoT connectivity")
    
    # RULE 5: Connectivity Match - LTE-M
    @Rule(UserRequirements(connectivity='lte_m'))
    def recommend_lte_m_modules(self):
        self.rules_fired.append("RULE 5: LTE-M connectivity requirement detected")
        for module, data in self.module_db.items():
            if data['type'] == 'lte_m':
                self._add_score(module, 40, "Matches required LTE-M connectivity")
    
    # RULE 6: Connectivity Match - GSM
    @Rule(UserRequirements(connectivity='gsm'))
    def recommend_gsm_modules(self):
        self.rules_fired.append("RULE 6: GSM connectivity requirement detected")
        for module, data in self.module_db.items():
            if data['type'] == 'gsm':
                self._add_score(module, 40, "Matches required GSM connectivity")
    
    # RULE 7: Application Match - Automotive
    @Rule(UserRequirements(application='automotive'))
    def automotive_application(self):
        self.rules_fired.append("RULE 7: Automotive application requirement")
        for module, data in self.module_db.items():
            if 'automotive' in data['applications']:
                self._add_score(module, 25, "Optimized for automotive applications")
    
    # RULE 8: Application Match - Industrial
    @Rule(UserRequirements(application='industrial'))
    def industrial_application(self):
        self.rules_fired.append("RULE 8: Industrial IoT application requirement")
        for module, data in self.module_db.items():
            if 'industrial' in data['applications']:
                self._add_score(module, 25, "Optimized for industrial IoT applications")
    
    # RULE 9: Application Match - Smart Metering
    @Rule(UserRequirements(application='smart_metering'))
    def smart_metering_application(self):
        self.rules_fired.append("RULE 9: Smart metering application requirement")
        for module, data in self.module_db.items():
            if 'smart_metering' in data['applications']:
                self._add_score(module, 25, "Optimized for smart metering applications")
    
    # RULE 10: Application Match - Wearable
    @Rule(UserRequirements(application='wearable'))
    def wearable_application(self):
        self.rules_fired.append("RULE 10: Wearable application requirement")
        for module, data in self.module_db.items():
            if 'wearable' in data['applications']:
                self._add_score(module, 25, "Optimized for wearable applications")
    
    # RULE 11: Application Match - Others
    @Rule(UserRequirements(application=L('asset_tracking') | L('smart_city') | L('medical') | L('agriculture')))
    def other_applications(self, application):
        self.rules_fired.append(f"RULE 11: {application} application requirement")
        for module, data in self.module_db.items():
            if application in data['applications']:
                self._add_score(module, 25, f"Optimized for {application.replace('_', ' ')} applications")
    
    # RULE 12: Ultra-low Power Requirement
    @Rule(UserRequirements(power='ultra_low'))
    def ultra_low_power(self):
        self.rules_fired.append("RULE 12: Ultra-low power requirement")
        for module, data in self.module_db.items():
            if data['type'] in ['nbiot', 'lte_m', 'gsm']:
                self._add_score(module, 15, "Power consumption suits ultra-low power requirement")
    
    # RULE 13: Low Power Requirement
    @Rule(UserRequirements(power='low'))
    def low_power(self):
        self.rules_fired.append("RULE 13: Low power requirement")
        for module, data in self.module_db.items():
            if data['type'] in ['nbiot', 'lte_m', 'gsm', 'lte_cat1']:
                self._add_score(module, 15, "Power consumption suits low power requirement")
    
    # RULE 14: Moderate Power Requirement
    @Rule(UserRequirements(power='moderate'))
    def moderate_power(self):
        self.rules_fired.append("RULE 14: Moderate power requirement")
        for module, data in self.module_db.items():
            if data['type'] in ['lte_cat1', 'lte_cat4']:
                self._add_score(module, 15, "Power consumption suits moderate power requirement")
    
    # RULE 15: High Power (High Performance)
    @Rule(UserRequirements(power='high'))
    def high_power(self):
        self.rules_fired.append("RULE 15: High performance power requirement")
        for module, data in self.module_db.items():
            if data['type'] in ['5G', 'lte_cat4']:
                self._add_score(module, 15, "Power consumption suits high performance requirement")
    
    # RULE 16: GNSS Required
    @Rule(UserRequirements(gnss=L('yes_high_accuracy') | L('yes_standard')))
    def gnss_required(self):
        self.rules_fired.append("RULE 16: GNSS positioning required")
        for module, data in self.module_db.items():
            if data['gnss']:
                self._add_score(module, 5, "Includes integrated GNSS positioning")
    
    # RULE 17: Extreme Temperature Environment
    @Rule(UserRequirements(environment='extreme'))
    def extreme_environment(self):
        self.rules_fired.append("RULE 17: Extreme temperature environment")
        for module, data in self.module_db.items():
            if data['temp'] == 'extreme':
                self._add_score(module, 3, "Temperature rating supports extreme environment")
    
    # RULE 18: Industrial Temperature Environment
    @Rule(UserRequirements(environment=L('industrial') | L('standard') | L('indoor')))
    def industrial_environment(self):
        self.rules_fired.append("RULE 18: Industrial/Standard environment")
        for module, data in self.module_db.items():
            if data['temp'] in ['extreme', 'industrial']:
                self._add_score(module, 3, "Temperature rating supports required environment")
    
    # RULE 19: Low Budget
    @Rule(UserRequirements(budget='low'))
    def low_budget(self):
        self.rules_fired.append("RULE 19: Low budget constraint")
        for module, data in self.module_db.items():
            if data['cost'] == 'low':
                self._add_score(module, 2, "Price point fits low budget")
    
    # RULE 20: Medium Budget
    @Rule(UserRequirements(budget='medium'))
    def medium_budget(self):
        self.rules_fired.append("RULE 20: Medium budget constraint")
        for module, data in self.module_db.items():
            if data['cost'] in ['low', 'medium']:
                self._add_score(module, 2, "Price point fits medium budget")
    
    # RULE 21: High Budget
    @Rule(UserRequirements(budget='high'))
    def high_budget(self):
        self.rules_fired.append("RULE 21: High budget - performance priority")
        for module, data in self.module_db.items():
            self._add_score(module, 2, "Price within budget range")
    
    # RULE 22: Automotive Certification Required
    @Rule(UserRequirements(certifications='automotive'))
    def automotive_cert(self):
        self.rules_fired.append("RULE 22: Automotive certification required")
        for module, data in self.module_db.items():
            if 'automotive' in data['certifications']:
                self._add_score(module, 5, "Has required automotive certifications")
    
    # RULE 23: Medical Certification Required
    @Rule(UserRequirements(certifications='medical'))
    def medical_cert(self):
        self.rules_fired.append("RULE 23: Medical certification required")
        for module, data in self.module_db.items():
            if 'medical' in data['certifications']:
                self._add_score(module, 5, "Has required medical certifications")
    
    # Helper method to add scores
    def _add_score(self, module, points, reason):
        if module not in self.recommendations:
            self.recommendations[module] = {
                'score': 0,
                'reasons': [],
                'data': self.module_db[module]
            }
        self.recommendations[module]['score'] += points
        if reason not in self.recommendations[module]['reasons']:
            self.recommendations[module]['reasons'].append(reason)
    
    def get_recommendations(self):
        """Return top 3 recommendations sorted by score"""
        sorted_recs = sorted(
            self.recommendations.items(),
            key=lambda x: x[1]['score'],
            reverse=True
        )
        return sorted_recs[:3]

# ============================================================================
# STREAMLIT APPLICATION
# ============================================================================

# Initialize session state
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'recommendation' not in st.session_state:
    st.session_state.recommendation = None
if 'rules_fired' not in st.session_state:
    st.session_state.rules_fired = []

# Questions database
questions = [
    {
        'id': 'application',
        'question': 'What is your primary application?',
        'emoji': '',
        'options': [
            ('automotive', '', 'Automotive & Vehicle Tracking'),
            ('industrial', '', 'Industrial IoT & M2M'),
            ('smart_metering', '', 'Smart Metering & Utilities'),
            ('wearable', '', 'Wearables & Consumer IoT'),
            ('asset_tracking', '', 'Asset Tracking & Logistics'),
            ('smart_city', '', 'Smart City Infrastructure'),
            ('medical', '', 'Medical & Healthcare'),
            ('agriculture', '', 'Agriculture & Environment')
        ]
    },
    {
        'id': 'connectivity',
        'question': 'What connectivity type do you need?',
        'emoji': '',
        'options': [
            ('5g', '', '5G (High speed, low latency)'),
            ('lte_cat1', '', 'LTE Cat 1 (Voice & data balance)'),
            ('lte_cat4', '', 'LTE Cat 4 (High throughput)'),
            ('lte_cat6', '', 'LTE Cat 6 (Very high throughput)'),
            ('nbiot', '', 'NB-IoT (Low power, low data)'),
            ('lte_m', '', 'LTE-M (Balanced power & mobility)'),
            ('gsm', '', 'GSM/GPRS (Legacy 2G)')
        ]
    },
    {
        'id': 'power',
        'question': 'What are your power requirements?',
        'emoji': '',
        'options': [
            ('ultra_low', '', 'Ultra-low power (10+ years battery)'),
            ('low', '', 'Low power (2-5 years battery)'),
            ('moderate', '', 'Moderate (powered with battery backup)'),
            ('high', '', 'High performance (continuous power)')
        ]
    },
    {
        'id': 'data_rate',
        'question': 'What data rate do you require?',
        'emoji': '',
        'options': [
            ('very_low', '', 'Very Low (<100 kbps) - sensor data'),
            ('low', '', 'Low (100 kbps - 1 Mbps) - telemetry'),
            ('medium', '', 'Medium (1-10 Mbps) - images, audio'),
            ('high', '', 'High (10-150 Mbps) - video streaming'),
            ('very_high', '', 'Very High (150+ Mbps) - HD video')
        ]
    },
    {
        'id': 'gnss',
        'question': 'Do you need GNSS/GPS positioning?',
        'emoji': '',
        'options': [
            ('yes_high_accuracy', '', 'Yes, high accuracy required'),
            ('yes_standard', '', 'Yes, standard accuracy'),
            ('no', '', 'No positioning needed')
        ]
    },
    {
        'id': 'environment',
        'question': 'What is your operating environment?',
        'emoji': '',
        'options': [
            ('extreme', '', 'Extreme (-40°C to +85°C)'),
            ('industrial', '', 'Industrial (-40°C to +75°C)'),
            ('standard', '', 'Standard (-20°C to +60°C)'),
            ('indoor', '', 'Indoor controlled environment')
        ]
    },
    {
        'id': 'budget',
        'question': 'What is your budget constraint?',
        'emoji': '',
        'options': [
            ('low', '', 'Low cost priority'),
            ('medium', '', 'Balanced cost/performance'),
            ('high', '', 'Performance priority')
        ]
    },
    {
        'id': 'certifications',
        'question': 'What certifications do you need?',
        'emoji': '',
        'options': [
            ('automotive', '', 'Automotive (IATF 16949, AEC-Q100)'),
            ('medical', '', 'Medical (FDA, CE Medical)'),
            ('standard', '', 'Standard (CE, FCC, PTCRB)'),
            ('none', '', 'No specific requirements')
        ]
    }
]

def run_expert_system(user_answers):
    """Run the Experta expert system with user answers"""
    engine = QuectelExpertSystem()
    engine.reset()
    
    # Declare user requirements as facts
    engine.declare(UserRequirements(**user_answers))
    
    # Run the inference engine
    engine.run()
    
    # Get recommendations and rules fired
    recommendations = engine.get_recommendations()
    rules_fired = engine.rules_fired
    
    return recommendations, rules_fired

def handle_answer(question_id, value):
    """Handle user answer and advance to next question"""
    st.session_state.answers[question_id] = value
    
    if st.session_state.current_step < len(questions) - 1:
        st.session_state.current_step += 1
    else:
        # Run Experta expert system
        recommendations, rules_fired = run_expert_system(st.session_state.answers)
        st.session_state.recommendation = recommendations
        st.session_state.rules_fired = rules_fired
    st.rerun()

def reset():
    """Reset the expert system"""
    st.session_state.current_step = 0
    st.session_state.answers = {}
    st.session_state.recommendation = None
    st.session_state.rules_fired = []
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
    <p style='font-size: 1.2rem; color: #718096;'>Smart module selection powered by Experta AI</p>
    <p style='font-size: 0.9rem; color: #a0aec0;'>Rule-Based Expert System with Inference Engine</p>
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
            <span class='score-badge'>✨ {module_info['score']} Points Match</span>
            <span class='badge badge-info' style='margin-left: 1rem;'>{module_info['data']['type'].upper()}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Main content in two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='card'>
            <h2 style="color: black;"> Key Features</h2>
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
            <h2 style="color: black">Why This Module?</h2>
        </div>
        """, unsafe_allow_html=True)
        
        for reason in module_info['reasons']:
            st.markdown(f"<div class='reason-item'>{reason}</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Experta Rules Fired Section
    with st.expander("Expert System Rules Fired (Experta Inference)", expanded=True):
        st.markdown("""
        <div class='card'>
            <h3 style="color: #2d3748;">Inference Engine Execution</h3>
            <p style='color: #718096;'>These are the expert rules that were fired by the Experta inference engine:</p>
        </div>
        """, unsafe_allow_html=True)
        
        for idx, rule in enumerate(st.session_state.rules_fired, 1):
            st.markdown(f"""
            <div class='rule-fired'>
            <strong style = "color: #2d3748;">Rule {idx}:</strong> <strong style = "color: #2d3748;">{rule} </strong>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown(
    f"""
    <div style='margin-top: 1rem; padding: 1rem; background: #f0f9ff; border-radius: 8px; 
                border-left: 4px solid #3b82f6; color: #1e3a8a;'>
        <strong>Total Rules Fired:</strong> {len(st.session_state.rules_fired)}
    </div>
    """,
    unsafe_allow_html=True
)

    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Alternative options
    st.markdown("""
    <div class='card'>
        <h2 style="color:#2d3748">🔀 Alternative Options</h2>
        <p style='color: #718096;'>Here are other modules that might suit your needs</p>
    </div>
    """, unsafe_allow_html=True)
    
    if len(st.session_state.recommendation) > 1:
        cols = st.columns(2)
        for idx, (alt_module, alt_info) in enumerate(st.session_state.recommendation[1:]):
            with cols[idx % 2]:
                st.markdown(f"""
                <div class='alternative-card'>
                    <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
                        <h3 style='margin: 0;'>{alt_module}</h3>
                        <span class='badge badge-success'>{alt_info['score']} pts</span>
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
                            <span style='color: #2d3748;'>{option_data[1]} {option_data[2]}</span>
                        </div>
                        """, unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 2rem; color: #a0aec0; font-size: 0.9rem;'>
    <p>Powered by <strong>Experta Expert System</strong> | Quectel IoT Solutions</p>
    <p style='font-size: 0.8rem; margin-top: 0.5rem;'>Rule-Based AI with Forward Chaining Inference Engine</p>
</div>
""", unsafe_allow_html=True)
