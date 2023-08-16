import csv

def updateSnowload(input_filename, snowload_filename, output_filename):
    print("Start importing SH01")

    snowload_data = {}

    # Read the snowzone data from the snowzone file
    with open(snowload_filename, 'r', newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            snowload_data[row['DC']] = {
                'snowzone': row['Schneelastzone'],
                'note': row['Fußnote(n)'],
                'comments': row['comments'],
            }

    print("Snowzone data loaded:", len(snowload_data))

    result = []

    # Read the input data and update snowzone values
    with open(input_filename, 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            dc = row['dc']
            if dc in snowload_data:
                snowload_info = snowload_data[dc]
                row['snowzone'] = snowload_info['snowzone']
                row['note'] = snowload_info['note']
                row['comments'] = snowload_info['comments']
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
_snowload_data = "csvData/Snow load zones 2023-02-07 - SH (01).csv"
_result = "_zipcode_city_dc_snowload.csv"

# Call the function to update the snowzone values
updateSnowload(_zipcode_city_dc_snowload, _snowload_data, _result)
