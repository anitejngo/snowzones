import csv

def updateSnowload(input_filename, snowload_filename, output_filename):
    print("Start importing SN14")

    snowload_data = []

    # Read the snowzone data from the snowzone file
    with open(snowload_filename, 'r', newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            snowload_data.append({
                **row,
                'snowzone': row['Schneelastzone'],
                'comments': row['comments']
            })

    print("Snowzone data loaded:", len(snowload_data))

    result = []

    # Read the input data and update snowzone values
    with open(input_filename, 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            # search by zipcode
            found_by_zip = [obj for obj in snowload_data if obj.get('ZIP') == row['zipcode']]
            if found_by_zip and found_by_zip[0]:
                row['snowzone'] = found_by_zip[0]['snowzone']
                row['comments'] = found_by_zip[0]['comments']
            else:
                # search by DC and city name
                found_by_dc = [obj for obj in snowload_data if obj.get('DC') == row['dc']]
                if found_by_dc:
                    found_by_city_name = [obj for obj in found_by_dc if obj.get('Gemeinde') == row['city']]
                    if found_by_city_name and found_by_city_name[0]:
                        row['snowzone'] = found_by_city_name[0]['snowzone']
                        row['comments'] = found_by_city_name[0]['comments']
                    else:
                        # if not found by city name fall back to DC
                        row['snowzone'] = found_by_dc[0]['snowzone']
                        row['comments'] = found_by_dc[0]['comments']
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
_snowload_data = "googleSheetData/Snow load zones 2023-02-07 - SN (14).csv"

# Call the function to update the snowzone values
updateSnowload(_zipcode_city_dc_snowload, _snowload_data, _zipcode_city_dc_snowload)
