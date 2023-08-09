import csv

def checkSnowloadData(input_filename):
    cities_with_snowload = 0
    cities_without_snowload = 0

    cities_with_comment = 0
    cities_without_comment = 0

    cities_with_note = 0
    cities_without_note = 0

    with open(input_filename, 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if row['snowload']:
                cities_with_snowload += 1
            else:
                cities_without_snowload += 1
            if row['comment']:
                cities_with_comment += 1
            else:
                cities_without_comment += 1
            if row['note']:
                cities_with_note += 1
            else:
                cities_without_note += 1

    return cities_with_snowload, cities_without_snowload,cities_with_comment,cities_without_comment,cities_with_note,cities_without_note

# Provide the input filename
_zipcode_city_dc_snowload = "_zipcode_city_dc_snowload.csv"

# Call the function to check snowload data
with_snowload, without_snowload,cities_with_comment,cities_without_comment,cities_with_note,cities_without_note = checkSnowloadData(_zipcode_city_dc_snowload)

print("Cities with snowload data:", with_snowload)
print("Cities without snowload data:", without_snowload)
print("Cities with comment data:", cities_with_comment)
print("Cities without comment data:", cities_without_comment)
print("Cities with note data:", cities_with_note)
print("Cities without note data:", cities_without_note)
