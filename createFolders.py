import os

# Define the folder structure
folder_structure = {
    "Python Foundation": [
        "Introduction to Python",
        "Python for Data Science",
        "Python for Visualization",
        "Exploratory Data Analysis"
    ],
    "Machine Learning": [
        "Linear Regression",
        "Decision Trees",
        "Clustering"
    ],
    "Advanced Machine Learning": [
        "Bagging and random forest",
        "Boosting",
        "Model Tuning"
    ],
    "Computer vision": [
        "Introduction to computer vision",
        "Transfer learning"
    ],
    "Introduction to Natural Language Processing": [
        "Introduction to Natural Language Processing",
        "Word embeddings",
        "Attention Mechanism and Transformers",
        "Large language Models and Prompt Engineering"
    ],
    "Introduction to neural networks": [
        "Introduction to Neural Networks",
        "Optimizing Neural Networks"
    ]
}

# Create folders, subfolders, and a day1.py file in each
for parent, subfolders in folder_structure.items():
    for subfolder in subfolders:
        path = os.path.join(parent, subfolder)

        # Create the directory if it doesn't exist
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created folder: {path}")
        else:
            print(f"Folder already exists: {path}")

        # Create day1.py with print("hello world")
        day1_path = os.path.join(path, "day1.py")
        if not os.path.exists(day1_path):
            with open(day1_path, "w", encoding="utf-8") as f:
                f.write('print("hello world")\n')
            print(f"Created file: {day1_path}")
        else:
            print(f"File already exists: {day1_path}")
