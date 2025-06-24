#
import numpy as np
import pandas as pd
import google.genai as genai
import os

#Generate transcripts
n = 10  # Set the number of conversations you want to generate
client = 

for i in range(1, n + 1):
        
    prompt = f'Return a 10 minute conversation between a doctor and a patient about the patient symptoms. There should be three different problems addressed. There should be a robust HPI obtained with difficulty by the physician from a meandering patient. There should be a diagnosis if HPI lends itself to a confident dx and there should be discussion of a plan.'
    
    response = client.models.generate_content(
        model='gemini-2.5-flash-preview-05-20', contents = prompt
    )
    
    # Save the conversation to a variable with dynamic name
    globals()[f'encounter_transcript_{i}'] = response.text
    
    print(f"Generated encounter_transcript_{i}")

for i in range(1, n + 1):
    # Print the generated conversation
    print(f"Encounter Transcript {i}:\n{globals()[f'encounter_transcript_{i}']}\n")

#Save the transcripts

# Create directory if it doesn't exist
save_dir = 
os.makedirs(save_dir, exist_ok=True)
for i in range(1, n + 1):
    filename = f'encounter_transcript_{i}.txt'
    filepath = os.path.join(save_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"Encounter Transcript {i}:\n\n")
        f.write(globals()[f'encounter_transcript_{i}'])
    print(f"Saved {filepath}")

###################################### Generate note#################################################################################################
import numpy as np
import pandas as pd
import google.genai as genai
client = 
# Load transcripts and save as global variables
save_dir = 
n =10
for i in range(1, n + 1):
    filename = f'encounter_transcript_{i}.txt'
    filepath = os.path.join(save_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            globals()[f'encounter_transcript_{i}'] = f.read()
        print(f"Loaded {filepath} into variable encounter_transcript_{i}")
    else:
        print(f"File {filepath} not found.")
#Use the encounter_transcript_n files to generate a document with the following fields: History of Present Illness, Visit Diagnoses, Assessment and Plan, Orders by making a call to api
model_name='gemini-2.5-flash-preview-05-20'
#Revised prompting
for i in range(1, n + 1):
    
    # Get the transcript content for this encounter
    transcript_content = globals()[f'encounter_transcript_{i}']
    
    prompt = f"""You are a medical documentation assistant. Based on the following doctor-patient conversation, create a structured medical note with the following sections:

1. History of Present Illness (HPI): should be in format of a list of problems with details for each problem in a short paragraph. Do not add other subheadings to organize the information.
Problem 1: HPI Details
Problem 2: HPI Details
Problem n: HPI details
2. Visit Diagnoses
-Problem 1
-Problem 2
-Problem n  
3. Assessment and Plan
Problem 1
-Assessment:
-Plan:
Problem 2
-Assessment:
-Plan:
Problem n
-Assessment:
-Plan:
4. Orders #This section should only include orders that would need to be placed in the EMR system. Include medications, labs, imaging, referrals, etc. Do not include any other information such as counseling.
Problem 1
-Order 1
-Order 2
-Order n
Problem 2
-Order 1
-Order 2
-Order n
Problem n
-Order 1
-Order 2
-Order n

Transcript:
{transcript_content}


Please format the output with clear section headers as detailed above without addition of other subheadings/sections and professional medical documentation style.\n"""


    response = client.models.generate_content(
        model=model_name, contents = prompt
    )
    
    # Save the conversation to a variable with dynamic name
    globals()[f'encounter_summary_{i}_{model_name}'] = response.text
    
    print(f"Generated encounter_summary_{i}_{model_name}")

#for i in range(1, n + 1):
    # Print the Summary
#    print(f"Encounter Summary {i}:\n{globals()[f'encounter_summary_{i}_{model_name}']}\n")

save_dir_summ = 
os.makedirs(save_dir_summ, exist_ok=True)
for i in range(1, n+1):
    # Save the summary to a file
    filename = f'encounter_summary_{i}_{model_name}.txt'
    filepath = os.path.join(save_dir_summ, filename)
    
    # Delete existing file if it exists
    if os.path.exists(filepath):
        os.remove(filepath)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"Encounter Summary {i}_{model_name}:\n\n")
        f.write(globals()[f'encounter_summary_{i}_{model_name}'])
    print(f"Saved {filepath}")

###############################################################################################################################################
