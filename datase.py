# dataset_update.py

def update_dataset():
    new_data = [
        {"age": 45, "cholesterol": 230, "heart_disease": 0},
        {"age": 54, "cholesterol": 250, "heart_disease": 1},
        {"age": 60, "cholesterol": 210, "heart_disease": 0},
    ]
    print("Dataset updated with new entries:", new_data)
    return new_data

if __name__ == "__main__":
    updated_data = update_dataset()
