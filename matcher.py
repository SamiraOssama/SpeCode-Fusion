import spacy
def match_requirements_to_code(requirements, code_functions):
    matches = {}

    for req in requirements:
        matched_functions = []
        print(f"Matching for requirement: '{req}'")  
        
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(req)
        keywords = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]

        print(f"Keywords: {keywords}")  

        for function in code_functions:
            cleaned_function = function.lower()
            print(f"Checking function: '{cleaned_function}' against keywords: {keywords}")  # Debug print

            # Match any keyword
            if any(keyword in cleaned_function for keyword in keywords):
                matched_functions.append(function)
                print(f"Matched '{function}' with '{req}'")  # Debug print

        if not matched_functions:
            print(f"No matches found for '{req}'")  # Debug print
            matched_functions.append("No matching function found")

        matches[req] = matched_functions

    return matches
