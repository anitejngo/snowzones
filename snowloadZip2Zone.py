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
            if start <= number <= end:
                return True
        elif int(r) == number:
            return True
    return False

def updateSnowload(input_filename, snowload_filename, output_filename):
    print("Start")

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
                if ',' in zipCodeInData:
                    if is_within_comma_separated_range(int(zipcode), zipCodeInData):
                        row['snowzone'] = zipRow['snow zone']
                        break  # Break after finding a match in comma-separated ranges
                elif '-' in zipCodeInData:
                    if is_within_range(zipcode,zipCodeInData):
                        row['snowzone'] = zipRow['snow zone']
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
_zipcode_city_dc_snowload = "_zipcode_city_dc_snowload.csv"
_snowload_data = "csvData/zip2zone.csv"
_result = "_zipcode_city_dc_snowload.csv"

# Call the function to update the snowzone values
updateSnowload(_zipcode_city_dc_snowload, _snowload_data, _result)
