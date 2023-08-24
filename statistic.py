import csv


def checkSnowloadData(input_filename):
    cities_with_snowload = 0
    cities_without_snowload = []

    with open(input_filename, 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if row['snowzone']:
                cities_with_snowload += 1
            else:
                cities_without_snowload.append(row)

    return cities_with_snowload, cities_without_snowload


# Provide the input filename
_zipcode_city_dc_snowload = "data/_zipcode_city_dc_snowload.csv"

# Call the function to check snowload data
with_snowload, without_snowload = checkSnowloadData(_zipcode_city_dc_snowload)

print("Cities with snowload data:", with_snowload)
print("Cities without snowload data:", len(without_snowload))
print(without_snowload)
