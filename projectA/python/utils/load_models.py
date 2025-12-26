import pickle
from . import config

def load_1R():
    with open(config.ONER_MODEL_PATH, "rb") as f:
        oner_model = pickle.load(f)
        
    return oner_model


def load_id3_nb():
    with open(config.ID3_MODEL_PATH, "rb") as f:
        id3_model = pickle.load(f)
    with open(config.NB_MODEL_PATH, "rb") as f:
        nb_model = pickle.load(f)
        
    return id3_model, nb_model


def load_encoders():
    with open(config.FEATURE_ENCODERS_PATH, "rb") as f:
        feature_encoders = pickle.load(f)
    with open(config.TARGET_ENCODER_PATH, "rb") as f:
        target_encoder = pickle.load(f)
    
    return feature_encoders, target_encoder