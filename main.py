from srs_extraction import extract_requirements
from code_parser import parse_source_code
from matcher import match_requirements_to_code
from generate_report import generate_report

def calculate_compatibility_percentage(requirements, matches):
    total_requirements = len(requirements)
    matched_requirements = sum(1 for req in requirements if matches[req] and "No matching function found" not in matches[req])

    if total_requirements == 0:
        return 0.0  # To avoid division by zero

    compatibility_percentage = (matched_requirements / total_requirements) * 100
    return compatibility_percentage




# Read requirements from srs.txt
with open("srs.txt", "r") as file:
    requirements_text = file.read()

# Read the sample source code from sample_source_code.py
with open("sample_source_code.py", "r") as file:
    source_code = file.read()

# Main execution
extracted_requirements = extract_requirements(requirements_text)
source_code_functions = parse_source_code(source_code)

# Match requirements to source code
matches = match_requirements_to_code(extracted_requirements, source_code_functions)


compatibility_percentage = calculate_compatibility_percentage(extracted_requirements, matches)

# Generate the report
report = generate_report(matches, compatibility_percentage)

# Output results
print("Extracted Requirements:", extracted_requirements)
print("Source Code Functions:", source_code_functions)
print(report)

# Save the report to a text file
with open("traceability_report.txt", "w") as report_file:
    report_file.write(report)
