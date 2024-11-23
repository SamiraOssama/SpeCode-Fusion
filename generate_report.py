def generate_report(matches, compatibility_percentage):
    report_lines = []
    report_lines.append("Requirement to Code Traceability Report\n")
    
    for requirement, matched_functions in matches.items():
        report_lines.append(f"Requirement: {requirement}")
        if matched_functions:
            report_lines.append(f"Matching Functions: {', '.join(matched_functions)}")
        else:
            report_lines.append("Matching Functions: No matching function found")
        report_lines.append("")  # Add a blank line for separation
    
    # Add compatibility percentage to the report
    report_lines.append(f"Compatibility Percentage: {compatibility_percentage:.2f}%")
    
    return "\n".join(report_lines)
