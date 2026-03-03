from generate_data import generate_database
from data_processing import process_data
from train_model import train_model

def run_pipeline():
    print("Step 1: Generating Database")
    generate_database()

    print("Step 2: Processing Data")
    process_data()

    print("Step 3: Training Model")
    train_model()

    print("Pipeline Complete.")

if __name__ == "__main__":
    run_pipeline()