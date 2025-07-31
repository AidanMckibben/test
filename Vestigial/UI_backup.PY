import streamlit as st

# Set page config
st.set_page_config(page_title="Info Portal", layout="wide")

# Initialize session state for page
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# Temporary key to store navigation intent
if "nav" not in st.session_state:
    st.session_state["nav"] = None

# Home page navigation buttons
if st.session_state["page"] == "Home":
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Building Info"):
            st.session_state["nav"] = "Building Info"
    with col2:
        if st.button("Assembly Info"):
            st.session_state["nav"] = "Assembly Info"
    with col3:
        if st.button("Retrofit Info"):
            st.session_state["nav"] = "Retrofit Info"

# Back to Home buttons
elif st.session_state["page"] in ["Building Info", "Assembly Info", "Retrofit Info"]:
    if st.button("Back to Home"):
        st.session_state["nav"] = "Home"

# Apply navigation if needed
if st.session_state["nav"]:
    st.session_state["page"] = st.session_state["nav"]
    st.session_state["nav"] = None
    st.rerun()

# Sidebar navigation (now uses session state)
page = st.sidebar.radio(
    "Go to",
    ("Home", "Building Info", "Assembly Info", "Retrofit Info"),
    key="page"
)

# Display content based on st.session_state["page"]
if st.session_state["page"] == "Home":
    st.title("Welcome to the Info Portal")
    st.write("Use the buttons above or the sidebar to navigate.")
elif st.session_state["page"] == "Building Info":
    st.title("Building Info")
    st.write("This is the Building Info page.")
    # Dropdowns for Building Info
    building_type = st.selectbox(
        "Building Type",
        [
            "Select...",
            "Townhouses",
            "up to 6 stories (low-mid rise)",
            "more than 6 stories"
        ]
    )
    building_structure = st.selectbox(
        "Building Structure",
        [
            "Select...",
            "Concrete",
            "Wood Frame"
        ]
    )
    heating_system = st.selectbox(
        "Heating System",
        [
            "Select...",
            "Electric baseboards",
            "Natural gas baseboards"
        ]
    )
    dhw_system = st.selectbox(
        "DHW System",
        [
            "Select...",
            "Electric",
            "Natural gas"
        ]
    )
    window_wall_ratio = st.selectbox(
        "Window-Wall-Ratio",
        [
            "Select...",
            "Low (<20%)",
            "Medium (20%<x<30%)",
            "High (>30%)"
        ]
    )
elif st.session_state["page"] == "Assembly Info":
    st.title("Assembly Info")
    st.write("This is the Assembly Info page.")

    # Get Building Structure selection from session state if available
    building_structure = st.session_state.get("Building Structure", None)

    # Determine Walls dropdown label and options
    if building_structure == "Wood Frame":
        walls_label = "Walls (wood)"
        walls_options = ["Select...", "2x4 studs w/ batt", "2x6 studs w/ batt"]
    elif building_structure == "Concrete":
        walls_label = "Walls (concrete)"
        walls_options = ["Select...", "Interior stud wall w/ batt", "Continuous rigid insulation", "Uninsulated"]
    else:
        walls_label = "Walls"
        walls_options = ["Please select building structure first"]

    walls = st.selectbox(walls_label, walls_options, key="assembly_walls")

    window_door_frame = st.selectbox(
        "Window / Door Frame",
        [
            "Select...",
            "Aluminum (no thermal break)",
            "Aluminum (w/ thermal break)",
            "Wood",
            "Vinyl"
        ],
        key="window_door_frame"
    )

    window_glazing = st.selectbox(
        "Window Glazing",
        [
            "Select...",
            "Single Glazing",
            "Double (no low-e)",
            "Double (low-e)"
        ],
        key="window_glazing"
    )

    # Glazing Cavity only appears for certain glazing types
    if window_glazing in ["Double (no low-e)", "Double (low-e)"]:
        glazing_cavity = st.selectbox(
            "Glazing Cavity",
            ["Select...", "1/4\"", "1/8\""] ,
            key="glazing_cavity"
        )
    
    thermal_bridging = st.selectbox(
        "Thermal Bridging",
        ["Select...", "Good", "Typical", "Bad"],
        key="thermal_bridging"
    )

    airtightness = st.selectbox(
        "Airtightness",
        ["Select...", "Good", "Typical", "Bad"],
        key="airtightness"
    )

elif st.session_state["page"] == "Retrofit Info":
    st.title("Retrofit Info")
    st.write("This is the Retrofit Info page.")