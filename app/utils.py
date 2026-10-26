import numpy as np
from app.model_loader import scaler

def preprocess(features):
    data = np.array(features).reshape(1, -1)
    data = scaler.transform(data)
    return data