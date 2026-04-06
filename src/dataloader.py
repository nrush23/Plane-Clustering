from traffic.data import opensky
import torch
import pandas as pd
class DataLoader:
    flights = torch.empty(1,1)
    def __init__(self):
        return
    
    def getData(self):
        """
        Tensor of our training data
        Returns:
            tensor: Nx8 flight features
        """
        #opensky.history requires account access, pending approval
        # raw_flights = opensky.history(start="2024-06-01", stop="2024-06-02", airport="KJFK", bounds=(40.4, -74.2, 40.9, -73.5))
        
        #this kaggle dataset is one snapshot of the opensky data, will have to do for now
        raw_flights = pd.read_csv("../data/opensky_states_snapshot.csv")

        #features we will focus on for training
        extracted_features = raw_flights[["time_position", "longitude", "latitude", "baro_altitude", "geo_altitude", "velocity", "true_track", "vertical_rate"]].dropna()
        print(extracted_features.head(5))
        self.flights = torch.tensor(extracted_features.values, dtype=torch.float32)

        #return a tensor of our features
        return self.flights
    