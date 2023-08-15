import csv

def filterAndExport(input_filename, prefix):
    no_snow_results = []

    # Read the input data and filter rows
    with open(input_filename, 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if row['dc'].startswith(prefix):
                if not row['snowzone']:
                    no_snow_results.append(row)

    # Export rows without snowzone to a new CSV file
    output_filename = "_no_snow_results.csv"

    if no_snow_results:
        with open(output_filename, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = no_snow_results[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
            writer.writeheader()
            writer.writerows(no_snow_results)

        print("Rows without snowzone exported to:", output_filename)
    else:
        print("No rows without snowzone found")

# Provide the input filename and prefix
_zipcode_city_dc_snowload = "_zipcode_city_dc_snowload.csv"
prefix = input("Enter the prefix for 'dc' value: ")

# Call the function to filter and export
filterAndExport(_zipcode_city_dc_snowload, prefix)
