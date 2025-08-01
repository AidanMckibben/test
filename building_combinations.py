import pandas as pd
import itertools

def generate_building_combinations():
    building_types = ["Townhouses", "Up to 6 stories", "More than 6 stories"]
    building_structures = {
        "Townhouses": ["Wood Frame"],
        "Up to 6 stories": ["Concrete", "Wood Frame"],
        "More than 6 stories": ["Concrete"],
    }
    wwr_options = ["Low (<20%)", "Medium (20%<x<30%)", "High (>30%)"]
    heating_systems = ["Electric Baseboards", "Natural Gas Baseboards"]
    dhw_systems = ["Electric", "Natural Gas"]
    wall_types = {
        "Concrete": [
            "Interior stud wall w/ batt",
            "Continuous rigid insulation",
            "Uninsulated",
        ],
        "Wood Frame": [
            "2x4 studs w/ batt",
            "2x6 studs w/ batt",
        ]
    }
    window_door_frames = ["Fiberglass", "Vinyl", "Aluminum (no thermal break)", "Aluminum (w/ thermal break)"]
    window_door_glass = ["Single Glazing", "Double (no low-e)", "Double (low-e)"]
    glazing_cavity = ["1/4\"", "1/8\""]
    thermal_bridging = ["Good", "Typical", "Bad"]
    airtightness = ["Good", "Typical", "Bad"]
    retrofit_window_frame = ["Fiberglass", "Vinyl", "Aluminum"]
    retrofit_window_glazing = ["Double", "Triple, typical", "Triple, high performance"]
    wall_exterior_insulation = ["None", "2\"", "4\"", "6\"", "8\""]
    roofs_retrofit = ["None", "Improved"]

    header = [
        "Building Type", "Building Structure", "Window-to-Wall-Ratio", "Heating System", "DHW System", "Walls",
        "Window / Door Frame", "Window Glazing", "Glazing Cavity", "Thermal Bridging", "Airtightness",
        "Retrofit Window Frame", "Retrofit Window Glazing", "Wall Exterior Insulation", "Roof Upgrade", "Data Set"
    ]

    rows = []
    row_count = 1

    for building_type in building_types:
        for building_structure in building_structures[building_type]:
            for wwr, heating, dhw in itertools.product(wwr_options, heating_systems, dhw_systems):
                for wall in wall_types[building_structure]:
                    for frame in window_door_frames:
                        for glass in window_door_glass:
                            # Handle Glazing Cavity logic
                            if glass == "Single Glazing":
                                glazing_cavity_list = ["n/a"]
                            else:
                                glazing_cavity_list = glazing_cavity
                            for cavity in glazing_cavity_list:
                                for t_bridging, airtight in itertools.product(thermal_bridging, airtightness):
                                    for r_frame in retrofit_window_frame:
                                        for r_glazing in retrofit_window_glazing:
                                            for wall_ext_ins in wall_exterior_insulation:
                                                for roof in roofs_retrofit:
                                                    row = [
                                                        building_type,
                                                        building_structure,
                                                        wwr,
                                                        heating,
                                                        dhw,
                                                        wall,
                                                        frame,
                                                        glass,
                                                        cavity,
                                                        t_bridging,
                                                        airtight,
                                                        r_frame,
                                                        r_glazing,
                                                        wall_ext_ins,
                                                        roof,
                                                        f"Dataset #{row_count}"
                                                    ]
                                                    rows.append(row)
                                                    row_count += 1

    df = pd.DataFrame(rows, columns=header)
    return df