# Create sample context files with placeholder content for testing the MCP client script

# Define the sample content for each file
context_files = {
    "otto_aviation_overview.txt": """Otto Aviation is an aerospace company focused on developing innovative aircraft designs. Their flagship model, the Celera, aims to revolutionize private air travel with improved fuel efficiency and aerodynamic performance.""",
    "celera_technical_specs.txt": """The Celera aircraft features a laminar flow fuselage, a single pusher propeller configuration, and a highly efficient diesel engine. It is designed to achieve a cruise speed of 460 mph and a range of 4,500 miles while consuming significantly less fuel than traditional jets.""",
    "market_analysis_summary.txt": """Market analysis indicates a growing demand for cost-effective and environmentally friendly private air travel solutions. Otto Aviation's Celera is positioned to capture market share by offering lower operating costs and reduced carbon emissions."""
}

# Write each file to disk
for filename, content in context_files.items():
    with open(filename, "w") as file:
        file.write(content)

# Confirm creation of files
print("Sample context files created successfully:")
for filename in context_files:
    print(f"- {filename}")