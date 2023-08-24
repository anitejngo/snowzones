import csv

# Read the CSV files
zipcodes_df = 'data/_zipcode_city_dc_snowload.csv'
geodata_df = 'data/georef-germany-postleitzahl.csv'


# Function to check if a zipcode exists in the English file
def zipcode_exists(zipcode, english_data):
    for row in english_data:
        if row['zipcode'] == zipcode:
            return True
    return False


# Load English data
english_data = []
with open(zipcodes_df, mode='r', encoding='utf-8') as english_csv:
    english_reader = csv.DictReader(english_csv)
    english_data = list(english_reader)


print(len(english_data))
# Load German data and update English data
new_zips = []
with open(geodata_df, mode='r', encoding='utf-8') as german_csv:
    german_reader = csv.DictReader(german_csv, delimiter=';')

    for row in german_reader:
        zipcode = row['Postleitzahl / Post code']

        if not zipcode_exists(zipcode, english_data):
            new_row = {
                'zipcode': zipcode,
                'city': row['PLZ Name (short)'],
                'dc': row['Kreis code'],
                'note': '',
                'comments': '',
                'snowzone': '',
            }
            new_zips.append(new_row)

# Write the updated English data to the CSV file
print("Found new zips", len(new_zips))
with open(zipcodes_df, mode='w', encoding='utf-8', newline='') as english_csv:
    fieldnames = ['zipcode', 'city', 'dc','snowzone','note','comments']
    english_writer = csv.DictWriter(english_csv, fieldnames=fieldnames)
    english_writer.writeheader()
    english_writer.writerows(english_data)
    english_writer.writerows(new_zips)

print("Data merged and updated successfully.")
