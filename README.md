# Vaccination Center Simulator

This Python program simulates a vaccination center where patients and their vaccination status are managed. The program includes classes representing patients, a medical studio, and functions to simulate patient vaccination and basic patient data analysis.
Files Included

    studioMedico.py: Contains the class definitions for Paziente (Patient) and Studio (Medical Studio).
    main.py: The main script that generates patient data, creates a medical studio, performs vaccinations, and analyzes patient data.
    README.md: This file.

Description

    The Paziente class represents an individual patient, storing their name, gender, age, and vaccination status. It provides methods to check vaccination status and simulate vaccination.

    The Studio class represents a medical studio and maintains a dictionary of patients. It includes methods to calculate the percentage of vaccinated patients, perform random vaccinations, and smart vaccinations based on unvaccinated patients.

Usage

    Run main.py to simulate a medical studio with patient data.
    The script generates a dictionary of patients with random names, genders, ages, and initial vaccination status.
    It creates a Studio object using the patient dictionary and performs various operations:
        Prints the list of patients.
        Calculates the percentage of vaccinated patients.
        Performs smart vaccinations on unvaccinated patients.
        Searches for patients with names starting with a specific letter.
        Identifies the oldest and youngest patients.

Functions

    nomeCasuale(): Generates a random name for a patient.
    genereCasuale(): Generates a random gender for a patient.
    cercanomeperlettera(Sdict, lettera): Searches for patients with names starting with a specific letter.
    etàmaggiore(Sdict): Finds the patient with the highest age.
    etàminore(Sdict): Finds the patient with the lowest age.
    Studio.percentualeVaccinati(): Calculates the percentage of vaccinated patients.

How to Run

Execute the main.py script to observe the simulation results and patient data analysis.
Note

This program is a simplified simulation and does not involve real-world patient data. It's meant for educational purposes to demonstrate basic patient management and analysis in a medical setting.
