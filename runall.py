# Import the necessary libraries
import os
from importlib import import_module

# List of script filenames in the order you want them to run
script_filenames = [
    "snowloadSH01",
    "snowloadHH02",
    "snowloadNI03",
    "snowloadHB04",
    "snowloadNW05",
    "snowloadHE06",
    "snowloadRP07",
    "snowloadBW08",
    "snowloadBY09",
    "snowloadSL10",
    "snowloadBE11",
    "snowloadBB12",
    "snowloadMV13",
    "snowloadSN14",
    "snowloadST15",
    "snowloadTH16",
    "snowloadZip2Zone",
    "snowloadAmbiguousZIP",
]

# Iterate through the script filenames and execute each script
for script_filename in script_filenames:
    # Construct the full path to the script file
    script_path = os.path.join(os.path.dirname(__file__), f"{script_filename}.py")

    # Use import_module to dynamically import the script module and run it
    script_module = import_module(script_filename)

