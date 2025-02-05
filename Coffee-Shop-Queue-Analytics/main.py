import pandas as pd
import numpy as np
from queue_analyzer import QueueAnalyzer

def generate_sample_data(output_file: str):
    """Generate sample customer data and save it to a CSV file."""
    dates = pd.date_range('2024-02-06', periods=1, freq='D')
    hours = range(7, 20)  # 7 AM to 8 PM
    records = []

    for date in dates:
        for hour in hours:
            # Simulate varying customer volumes throughout the day
            num_customers = np.random.normal(
                loc=15 if 11 <= hour <= 14 else 10,  # More customers during lunch
                scale=3
            )
            num_customers = max(1, int(num_customers))

            for _ in range(num_customers):
                # Simulate arrival times within the hour
                arrival_time = pd.Timestamp(date) + pd.Timedelta(hours=hour) + pd.Timedelta(minutes=np.random.randint(0, 60))
                wait_time = np.random.normal(loc=5, scale=2)  # Average wait time of 5 minutes
                service_duration = np.random.uniform(1, 5)  # Random service duration between 1 and 5 minutes

                records.append({
                    'date': date,
                    'hour': hour,
                    'arrival_time': arrival_time,
                    'wait_time': wait_time,
                    'service_duration': service_duration,
                    'customers': num_customers  # Add the customers column
                })

    df = pd.DataFrame(records)
    df.to_csv(output_file, index=False)

def main():
    data_file = 'sample_data.csv'
    generate_sample_data(data_file)

    # Step 2: Analyze the data
    analyzer = QueueAnalyzer(data_file)

    # Calculate wait times
    wait_times = analyzer.calculate_wait_times()
    avg_wait_time = sum(wait_times) / len(wait_times) if wait_times else 0

    # Identify peak hours
    peak_hours = analyzer.identify_peak_hours()

    # Generate staffing recommendations
    staffing = analyzer.generate_staffing_recommendations()

    # Step 3: Print results
    print("\n=== Queue Analysis Results ===")
    print(f"Average Wait Time: {avg_wait_time:.2f} minutes")

    print("\nPeak Hours Analysis:")
    print("High Volume Hours:", ", ".join(peak_hours['peak_volume_hours']))

    # Print staffing recommendations
    print("\nStaffing Recommendations:")
    for recommendation in staffing:
        print(recommendation)

if __name__ == "__main__":
    main()