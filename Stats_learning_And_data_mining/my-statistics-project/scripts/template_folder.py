import os

def create_project_structure(project_name="statistics-project"):
    folders = [
        "data/raw",
        "data/processed",
        "notebooks",
        "scripts",
        "reports",
        "figures",
        "results"
    ]
    
    files = {
        "README.md": "# {}\n\nProject description goes here.".format(project_name),
        "requirements.txt": "# List dependencies here",
        "scripts/data_cleaning.py": "# Script for data cleaning",
        "scripts/analysis.py": "# Main statistical analysis script",
        "scripts/visualization.py": "# Script for data visualization",
        "reports/report.md": "# Project Report\n\nSummary of findings and analysis.",
        ".gitignore": "__pycache__/\n*.csv\n*.xlsx\n*.log\n.DS_Store"
    }
    
    # Create project root directory
    os.makedirs(project_name, exist_ok=True)
    
    # Create subdirectories
    for folder in folders:
        os.makedirs(os.path.join(project_name, folder), exist_ok=True)
    
    # Create files with initial content
    for file, content in files.items():
        with open(os.path.join(project_name, file), "w") as f:
            f.write(content)
    
    print(f"Project '{project_name}' structure created successfully!")

# Call it here
create_project_structure("my-statistics-project")