import streamlit as st

# Set page config
st.set_page_config(page_title="RDH Window Tool", layout="wide")

# Inject custom CSS for font and button styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Outfit', sans-serif !important;
    }
    .custom-nav-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 180px;
        width: 100%;
        font-size: 2rem;
        font-family: 'Outfit', sans-serif;
        font-weight: 400;
        border: none;
        border-radius: 18px;
        margin: 0 10px;
        color: white;
        cursor: pointer;
        transition: box-shadow 0.2s;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    .custom-nav-btn:active {
        box-shadow: 0 1px 4px rgba(0,0,0,0.12);
    }
    .btn-building-info {
        background: #0061C2;
    }
    .btn-assembly-info {
        background: #215721;
    }
    .btn-retrofit-info {
        background: #DB5E21;
    }
    .custom-btn-row {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        gap: 32px;
        margin-top: 32px;
        margin-bottom: 32px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Helper to get current value or default for dropdowns
def get_dropdown_value(key, options):
    val = st.session_state.get(key, "Select...")
    return val if val in options else "Select..."

# Initialize session state for page
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# Temporary key to store navigation intent
if "nav" not in st.session_state:
    st.session_state["nav"] = None

# Home page navigation buttons (Streamlit-native, button centered in colored column)
if st.session_state["page"] == "Home":
    st.title("Welcome to the Info Portal")
    cols = st.columns(3, gap="large")
    with cols[0]:
        st.markdown(
            '<div style="background-color: #0061C2; border-radius: 18px; height: 180px; display: flex; align-items: center; justify-content: center; margin: 0 10px;">',
            unsafe_allow_html=True
        )
        st.write("")  # Spacer
        if st.button("Building Info", key="btn_building_info", help="Go to Building Info", use_container_width=True):
            st.session_state["nav"] = "Building Info"
        st.markdown('</div>', unsafe_allow_html=True)
    with cols[1]:
        st.markdown(
            '<div style="background-color: #215721; border-radius: 18px; height: 180px; display: flex; align-items: center; justify-content: center; margin: 0 10px;">',
            unsafe_allow_html=True
        )
        st.write("")  # Spacer
        if st.button("Assembly Info", key="btn_assembly_info", help="Go to Assembly Info", use_container_width=True):
            st.session_state["nav"] = "Assembly Info"
        st.markdown('</div>', unsafe_allow_html=True)
    with cols[2]:
        st.markdown(
            '<div style="background-color: #DB5E21; border-radius: 18px; height: 180px; display: flex; align-items: center; justify-content: center; margin: 0 10px;">',
            unsafe_allow_html=True
        )
        st.write("")  # Spacer
        if st.button("Retrofit Info", key="btn_retrofit_info", help="Go to Retrofit Info", use_container_width=True):
            st.session_state["nav"] = "Retrofit Info"
        st.markdown('</div>', unsafe_allow_html=True)

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
    ("Home", "Building Info", "Assembly Info", "Retrofit Info", "Summary"),
    key="page"
)

# Display content based on st.session_state["page"]
if st.session_state["page"] == "Home":
    st.title("Welcome to the Deep Energy Retrofit Window Tool")
    st.write("Use the buttons above or the sidebar to navigate.")
elif st.session_state["page"] == "Building Info":
    st.title("Building Info")
    st.write("This is the Building Info page.")
    # Dropdowns for Building Info
    # Define options for each dropdown
    building_type_options = [
        "Select...",
        "Townhouses",
        "up to 6 stories (low-mid rise)",
        "more than 6 stories"
    ]
    building_structure_options = [
        "Select...",
        "Concrete",
        "Wood Frame"
    ]
    heating_system_options = [
        "Select...",
        "Electric baseboards",
        "Natural gas baseboards"
    ]
    dhw_system_options = [
        "Select...",
        "Electric",
        "Natural gas"
    ]
    window_wall_ratio_options = [
        "Select...",
        "Low (<20%)",
        "Medium (20%<x<30%)",
        "High (>30%)"
    ]

    # Render selectboxes with value from session_state
    building_type = st.selectbox(
        "Building Type",
        building_type_options,
        index=building_type_options.index(get_dropdown_value("building_type", building_type_options)),
        key="building_type_selectbox"
    )
    if building_type != "Select...":
        st.session_state["building_type"] = building_type

    building_structure = st.selectbox(
        "Building Structure",
        building_structure_options,
        index=building_structure_options.index(get_dropdown_value("building_structure", building_structure_options)),
        key="building_structure_selectbox"
    )
    if building_structure != "Select...":
        st.session_state["building_structure"] = building_structure

    heating_system = st.selectbox(
        "Heating System",
        heating_system_options,
        index=heating_system_options.index(get_dropdown_value("heating_system", heating_system_options)),
        key="heating_system_selectbox"
    )
    if heating_system != "Select...":
        st.session_state["heating_system"] = heating_system

    dhw_system = st.selectbox(
        "DHW System",
        dhw_system_options,
        index=dhw_system_options.index(get_dropdown_value("dhw_system", dhw_system_options)),
        key="dhw_system_selectbox"
    )
    if dhw_system != "Select...":
        st.session_state["dhw_system"] = dhw_system

    window_wall_ratio = st.selectbox(
        "Window-Wall-Ratio",
        window_wall_ratio_options,
        index=window_wall_ratio_options.index(get_dropdown_value("window_wall_ratio", window_wall_ratio_options)),
        key="window_wall_ratio_selectbox"
    )
    if window_wall_ratio != "Select...":
        st.session_state["window_wall_ratio"] = window_wall_ratio

elif st.session_state["page"] == "Assembly Info":
    st.title("Assembly Info")
    st.write("This is the Assembly Info page.")

    # Get Building Structure selection from session state if available
    building_structure = st.session_state.get("building_structure", None)

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

    # Ensure the session state value is always valid for the current options
    current_walls_value = st.session_state.get("assembly_walls", walls_options[0])
    if current_walls_value not in walls_options:
        if "assembly_walls" in st.session_state:
            del st.session_state["assembly_walls"]
        current_walls_value = walls_options[0]

    walls = st.selectbox(
        walls_label,
        walls_options,
        index=walls_options.index(current_walls_value),
        key="assembly_walls_selectbox"
    )
    if walls != "Select..." and walls != "Please select building structure first":
        st.session_state["assembly_walls"] = walls

    window_door_frame_options = [
        "Select...",
        "Aluminum (no thermal break)",
        "Aluminum (w/ thermal break)",
        "Wood",
        "Vinyl"
    ]
    window_door_frame = st.selectbox(
        "Window / Door Frame",
        window_door_frame_options,
        index=window_door_frame_options.index(get_dropdown_value("window_door_frame", window_door_frame_options)),
        key="window_door_frame_selectbox"
    )
    if window_door_frame != "Select...":
        st.session_state["window_door_frame"] = window_door_frame

    # Assembly Info page window glazing options
    assembly_window_glazing_options = [
        "Select...",
        "Single Glazing",
        "Double (no low-e)",
        "Double (low-e)"
    ]
    window_glazing = st.selectbox(
        "Window Glazing",
        assembly_window_glazing_options,
        index=assembly_window_glazing_options.index(get_dropdown_value("window_glazing", assembly_window_glazing_options)),
        key="window_glazing_selectbox"
    )
    if window_glazing != "Select...":
        st.session_state["window_glazing"] = window_glazing

    # Glazing Cavity only appears for certain glazing types
    if window_glazing in ["Double (no low-e)", "Double (low-e)"]:
        glazing_cavity_options = ["Select...", "1/4\"", "1/8\""]
        glazing_cavity = st.selectbox(
            "Glazing Cavity",
            glazing_cavity_options,
            index=glazing_cavity_options.index(get_dropdown_value("glazing_cavity", glazing_cavity_options)),
            key="glazing_cavity_selectbox"
        )
        if glazing_cavity != "Select...":
            st.session_state["glazing_cavity"] = glazing_cavity

    thermal_bridging_options = ["Select...", "Good", "Typical", "Bad"]
    thermal_bridging = st.selectbox(
        "Thermal Bridging",
        thermal_bridging_options,
        index=thermal_bridging_options.index(get_dropdown_value("thermal_bridging", thermal_bridging_options)),
        key="thermal_bridging_selectbox"
    )
    if thermal_bridging != "Select...":
        st.session_state["thermal_bridging"] = thermal_bridging

    airtightness_options = ["Select...", "Good", "Typical", "Bad"]
    airtightness = st.selectbox(
        "Airtightness",
        airtightness_options,
        index=airtightness_options.index(get_dropdown_value("airtightness", airtightness_options)),
        key="airtightness_selectbox"
    )
    if airtightness != "Select...":
        st.session_state["airtightness"] = airtightness

elif st.session_state["page"] == "Retrofit Info":
    st.title("Retrofit Info")
    st.write("This is the Retrofit Info page.")

    # Define options for each dropdown
    window_frame_options = [
        "Select...",
        "Aluminum (no thermal break)",
        "Aluminum (w/ thermal break)",
        "Wood",
        "Vinyl"
    ]
    window_glazing_options = [
        "Select...",
        "Double",
        "Triple, typical",
        "Triple, high performance"
    ]
    wall_exterior_insulation_options = [
        "Select...",
        "None",
        "2\"",
        "4\"",
        "6\"",
        "8\""
    ]
    roof_upgrade_options = [
        "Select...",
        "None",
        "Improved"
    ]

    window_frame = st.selectbox(
        "Window Frame",
        window_frame_options,
        index=window_frame_options.index(get_dropdown_value("retrofit_window_frame", window_frame_options)),
        key="retrofit_window_frame_selectbox"
    )
    if window_frame != "Select...":
        st.session_state["retrofit_window_frame"] = window_frame

    window_glazing = st.selectbox(
        "Window Glazing",
        window_glazing_options,
        index=window_glazing_options.index(get_dropdown_value("retrofit_window_glazing", window_glazing_options)),
        key="retrofit_window_glazing_selectbox"
    )
    if window_glazing != "Select...":
        st.session_state["retrofit_window_glazing"] = window_glazing

    wall_exterior_insulation = st.selectbox(
        "Wall Exterior Insulation",
        wall_exterior_insulation_options,
        index=wall_exterior_insulation_options.index(get_dropdown_value("retrofit_wall_exterior_insulation", wall_exterior_insulation_options)),
        key="retrofit_wall_exterior_insulation_selectbox"
    )
    if wall_exterior_insulation != "Select...":
        st.session_state["retrofit_wall_exterior_insulation"] = wall_exterior_insulation

    roof_upgrade = st.selectbox(
        "Roof Upgrade",
        roof_upgrade_options,
        index=roof_upgrade_options.index(get_dropdown_value("retrofit_roof_upgrade", roof_upgrade_options)),
        key="retrofit_roof_upgrade_selectbox"
    )
    if roof_upgrade != "Select...":
        st.session_state["retrofit_roof_upgrade"] = roof_upgrade

elif st.session_state["page"] == "Summary":
    st.title("Summary of Selections")
    st.write("Below is a summary table of all your selections. This is the data that will be exported.")

    import pandas as pd
    summary_data = [
        ["Building Type", st.session_state.get("building_type", "")],
        ["Building Structure", st.session_state.get("building_structure", "")],
        ["Heating System", st.session_state.get("heating_system", "")],
        ["DHW System", st.session_state.get("dhw_system", "")],
        ["Window-Wall-Ratio", st.session_state.get("window_wall_ratio", "")],
        ["Walls", st.session_state.get("assembly_walls", "")],
        ["Window / Door Frame", st.session_state.get("window_door_frame", "")],
        ["Window Glazing", st.session_state.get("window_glazing", "")],
        ["Glazing Cavity", st.session_state.get("glazing_cavity", "")],
        ["Thermal Bridging", st.session_state.get("thermal_bridging", "")],
        ["Airtightness", st.session_state.get("airtightness", "")],
        ["Retrofit Window Frame", st.session_state.get("retrofit_window_frame", "")],
        ["Retrofit Window Glazing", st.session_state.get("retrofit_window_glazing", "")],
        ["Wall Exterior Insulation", st.session_state.get("retrofit_wall_exterior_insulation", "")],
        ["Roof Upgrade", st.session_state.get("retrofit_roof_upgrade", "")],
    ]
    df = pd.DataFrame(summary_data, columns=["Dropdown Title", "Selection"])
    st.table(df)

    # List of required keys (excluding Glazing Cavity)
    required_keys = [
        "building_type",
        "building_structure",
        "heating_system",
        "dhw_system",
        "window_wall_ratio",
        "assembly_walls",
        "window_door_frame",
        "window_glazing",
        "thermal_bridging",
        "airtightness",
        "retrofit_window_frame",
        "retrofit_window_glazing",
        "retrofit_wall_exterior_insulation",
        "retrofit_roof_upgrade",
    ]
    # Check if all required fields are filled (not empty and not 'Select...' or 'Please select building structure first')
    all_filled = all(
        st.session_state.get(k, "").strip() not in ["", "Select...", "Please select building structure first"]
        for k in required_keys
    )

    # CSV export logic
    import io
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_data = csv_buffer.getvalue()

    st.download_button(
        label="Download CSV",
        data=csv_data,
        file_name="summary.csv",
        mime="text/csv",
        disabled=not all_filled
    )
