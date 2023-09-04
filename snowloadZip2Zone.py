import csv

def is_within_range(number, range_string):
    start, end = map(str, range_string.split('-'))
    return start <= number <= end

def is_within_comma_separated_range(number, range_string):
    ranges = range_string.split(',')
    for r in ranges:
        if '-' in r:
            sub_ranges = r.split('-')
            start, end = int(sub_ranges[0]), int(sub_ranges[-1])
            if start <= int(number) <= end:
                return True
        elif r == number:
            return True
    return False

def updateSnowload(input_filename, snowload_filename, output_filename):
    print("Start imporintg zip2zone")

    snowload_data = []

    # Read the snowzone data from the snowzone file
    with open(snowload_filename, 'r', newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            snowload_data.append(row)

    print("Snowzone data loaded:", len(snowload_data))


    result = []

    # Read the input data and update snowzone values
    with open(input_filename, 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            zipcode = row['zipcode']
            for zipRow in snowload_data:
                zipCodeInData = zipRow['ZIP code']
                # cover all , cases and , and - cases together
                if ',' in zipCodeInData:
                    if is_within_comma_separated_range(zipcode, zipCodeInData):
                        row['snowzone'] = zipRow['snow zone']
                # cover only - range
                elif '-' in zipCodeInData and ',' not in zipCodeInData:
                    if is_within_range(zipcode,zipCodeInData):
                        row['snowzone'] = zipRow['snow zone']
                # cover all other cases
                else:
                    if zipcode == zipRow['ZIP code']:
                        row['snowzone'] = zipRow['snow zone']

            result.append(row)

    print(len(result), "rows processed")

    # Write the updated data back to the output file
    with open(output_filename, 'w', newline='', encoding="utf-8") as csvfile:
        fieldnames = result[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        writer.writerows(result)


# Provide the input and output filenames
_zipcode_city_dc_snowload = "data/_zipcode_city_dc_snowload.csv"
_snowload_data = "googleSheetData/Snow load zones 2023-02-07 - zip2zone.csv"

# Call the function to update the snowzone values
updateSnowload(_zipcode_city_dc_snowload, _snowload_data, _zipcode_city_dc_snowload)
