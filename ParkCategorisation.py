import pandas as pd
from rapidfuzz import fuzz

# File paths
tours_path = "tours_rows.csv"    # replace with your actual file path
parks_path = "parks_rows.csv"    # replace with your actual file path
output_path = "tour_park_mapping.csv"

# Load CSVs
tours_df = pd.read_csv(tours_path)
parks_df = pd.read_csv(parks_path)

# Columns from tours to search
text_columns = ["title", "description", "itinerary", "accommodationType", "included", "excluded"]

# Collect results
results = []

# Similarity threshold (0–100). You can adjust this:
THRESHOLD = 85

# Iterate through each tour
for _, tour_row in tours_df.iterrows():
    # Combine all relevant text fields into one string
    tour_text = " ".join(str(tour_row[col]).lower() for col in text_columns if pd.notnull(tour_row[col]))
    
    # Check each park keyword
    for _, park_row in parks_df.iterrows():
        keyword = str(park_row["keyword"]).lower()
        
        # Exact or fuzzy match
        if keyword in tour_text or fuzz.partial_ratio(keyword, tour_text) >= THRESHOLD:
            results.append({
                "TourId": tour_row["id"],   # tour id column
                "ParkId": park_row["id"]    # park id column
            })

# Convert to DataFrame
mapping_df = pd.DataFrame(results)

# Save mapping to CSV
mapping_df.to_csv(output_path, index=False)

print(f"Mapping file created with fuzzy matching: {output_path}")
