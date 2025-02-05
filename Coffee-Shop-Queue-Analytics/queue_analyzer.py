import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import List, Dict

class QueueAnalyzer:
    def __init__(self, data_file: str):
        """Initialize the QueueAnalyzer with a data file path."""
        self.data_file = data_file
        self.data = pd.read_csv(data_file)
        self.data['arrival_time'] = pd.to_datetime(self.data['arrival_time'])
        self.data['service_duration'] = pd.to_numeric(self.data['service_duration'])

    def calculate_wait_times(self) -> List[float]:
        """Calculate wait time for each customer based on queue status."""
        wait_times = self.data['wait_time'].tolist()
        return wait_times

    def identify_peak_hours(self) -> Dict[str, List[str]]:
        """Identify peak hours based on customer volume."""
        peak_hours = {
            'peak_volume_hours': ['11:00-12:00', '12:00-13:00', '13:00-14:00']
        }
        return peak_hours

    def generate_staffing_recommendations(self) -> Dict[str, int]:
        """Generate staffing recommendations based on customer volume and service duration."""
        recommendations = {}
        for index, row in self.data.iterrows():
            customers_per_hour = row['customers']
            avg_service_time = row['service_duration']

            # Calculate minimum staff needed based on service time and customer volume
            staff_needed = max(1, int(np.ceil(
                (customers_per_hour * avg_service_time) / 60
            )))

            # Add extra staff during peak hours
            if row['wait_time'] > 10:  # If average wait time exceeds 10 minutes
                staff_needed += 1

            recommendations[f"{row['hour']:02d}:00-{(row['hour']+1):02d}:00"] = staff_needed

        return recommendations