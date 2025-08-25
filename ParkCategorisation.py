import pandas as pd

file_path = "C:\\Users\\v-henryn\\Downloads\\Parks.csv"
df = pd.read_csv(file_path)

# #Define the columns to search
# text_columns = ["title", "description", "itinerary", "accommodationType", "included", "excluded"]

# #Define national parks and their keywords
# safari_parks = {
# "Serengeti National Park": ["serengeti"],
# "Ngorongoro Conservation Area": ["ngorongoro"],
# "Lake Manyara National Park": ["manyara"],
# "Tarangire National Park": ["tarangire"],
# "Arusha National Park": ["arusha"],
# "Ruaha National Park": ["ruaha"],
# "Nyerere National Park": ["nyerere", "selous"],
# "Katavi National Park": ["katavi"],
# "Mahale Mountains National Park": ["mahale"],
# "Gombe Stream National Park": ["gombe"],
# "Mikumi National Park": ["mikumi"],
# "Udzungwa Mountains National Park": ["udzungwa"],
# "Saadani National Park": ["saadani"]
# }

# #Function to determine which parks are mentioned
# def find_parks(row):
# text = " ".join(str(row[col]).lower() for col in text_columns if pd.notnull(row[col]))
# matched = [park for park, keywords in safari_parks.items() if any(k in text for k in keywords)]
# return ", ".join(matched)

# #Apply the function to each row
# df["covered_parks"] = df.apply(find_parks, axis=1)

# #Show results: tour title + covered parks
# for index, row in df.iterrows():
# print(f"{row['title']}: {row['covered_parks']}")
