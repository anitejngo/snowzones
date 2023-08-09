import csv

def updateSnowload(input_filename, snowload_filename, output_filename):
    print("Start")

    snowload_data = {}

    # Read the snowload data from the snowload file
    with open(snowload_filename, 'r', newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            snowload_data[row['DC']] = {
                'snowload': row['Schneelastzone nach DIN EN 1991 Teil 1-3 '],
                'comment': row['comments'] if 'comments' in row else '',
                'note': row['Fußnote(n)'] if 'Fußnote(n)' in row else ''
            }

    print("Snowload data loaded:", len(snowload_data))

    result = []

    # Read the input data and update snowload values
    with open(input_filename, 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            dc = row['dc']
            if dc in snowload_data:
                snowload_info = snowload_data[dc]
                row['snowload'] = snowload_info['snowload']
                row['comment'] = snowload_info['comment']
                row['note'] = snowload_info['note']
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
_snowload_data = "csvData/BY09.csv"
_result = "_zipcode_city_dc_snowload.csv"

# Call the function to update the snowload values
updateSnowload(_zipcode_city_dc_snowload, _snowload_data, _result)
