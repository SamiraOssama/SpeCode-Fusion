import spacy
import re
def extract_requirements(srs_text):
    """
    Extract valid requirements from the SRS text using NLP.
    Extracted requirements must contain the keyword 'shall' and belong to the "Requirements" section.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(srs_text)

    requirements = []
    in_requirements_section = False

    for sent in doc.sents:
        sentence_text = sent.text.strip()
        print(f"Processing sentence: {sentence_text}")  

      
        if re.match(r'^\d+\.\s*Requirements', sentence_text, re.IGNORECASE):
            in_requirements_section = True
            continue

        
        if in_requirements_section and re.match(r'^\d+\.\s*\w+', sentence_text) and not sentence_text.lower().startswith("requirements"):
            print("End of Requirements section reached.")  
            break

     
        if in_requirements_section and "shall" in sentence_text.lower():
            
            requirement = re.sub(r"\s*\d+\.$", "", sentence_text)  
            requirements.append(requirement)
            print(f"Extracted Requirement: {requirement}")  

    return requirements
