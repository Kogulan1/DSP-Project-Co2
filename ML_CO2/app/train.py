import pandas as pd
from app.preprocessing import preprocess

def train(train_filepath, MODELS_DIR, training_mode):
    df = pd.read_csv(train_filepath)

    X_Preprocess = preprocess(df, MODELS_DIR, training_mode)
    dictionary = X_Preprocess.to_dict();

    return X_Preprocess





