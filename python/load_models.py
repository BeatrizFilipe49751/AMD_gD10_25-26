import pickle    

def load_models(oner_path: str, id3_path: str, nb_path: str, feature_encoders_path: str, target_encoder_path: str):
    # Load models
    with open(oner_path, "rb") as f:
        oner_model = pickle.load(f)
    with open(id3_path, "rb") as f:
        id3_model = pickle.load(f)
    with open(nb_path, "rb") as f:
        nb_model = pickle.load(f)
    
    # Load encoders
    with open(feature_encoders_path, "rb") as f:
        feature_encoders = pickle.load(f)
    with open(target_encoder_path, "rb") as f:
        target_encoder = pickle.load(f)
    
    return oner_model, id3_model, nb_model, feature_encoders, target_encoder
