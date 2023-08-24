import csv

def updateSnowload(input_filename, snowload_filename, output_filename):
    print("Start importing AmbiguousZIP")

    snowload_data = {}

    # Read the snowzone data from the snowzone file
    with open(snowload_filename, 'r', newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            snowload_data[row['ZIP']] = {
                'snowzone': row['SNOWZONE'],
            }

    print("Snowzone data loaded:", len(snowload_data))

    result = []

    # Read the input data and update snowzone values
    with open(input_filename, 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            zipcode = row['zipcode']
            if zipcode in snowload_data:
                snowload_info = snowload_data[zipcode]
                row['snowzone'] = snowload_info['snowzone']
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
_snowload_data = "googleSheetData/Snow load zones 2023-02-07 - AmbiguousZIP.csv"

# Call the function to update the snowzone values
updateSnowload(_zipcode_city_dc_snowload, _snowload_data, _zipcode_city_dc_snowload)
