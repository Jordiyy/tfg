import pandas as pd
import random
import csv
from scipy.stats import skewnorm
import variables
import generate_values
import update_profile_dependency
import check_profile


def generate_basic_profile():
    return {
        #'age': random.randint(6570, 29200),         # age as days, value between 18 years and 80 years
        'age': random.randint(7665, 29200),     # 21 years to 80 years
        'gender': generate_values.two_options_value(variables.MENS_PERCENTAGE),   # 0 = women, 1 = men
        'ethnic': generate_values.three_option_value(variables.CAUCASIAN_ETHNIC_PERCENTAGE, 
                                     variables.AFRICAN_ETHNIC_PERCENTAGE, 
                                     variables.ASIAN_ETHNIC_PERCENTAGE),
        'poverty': 0,
        'smoke': generate_values.two_options_value(variables.SMOKER_PERCENTAGE),   # 0 = no smoker, 1 = smoker
        'ascvd': generate_values.two_options_value(variables.ASCVD_PERCENTAGE),
        'icm': round(skewnorm.rvs(variables.ICM_SKEW, variables.ICM_MEAN, variables.ICM_STANDARD_DEVIATION), 2),
        'mellitus_diabetis': generate_values.two_options_value(variables.MELLITUS_DIABETIS_PERCENTAGE),
        'hypertension': 0,
        'dyslipidemia': generate_values.two_options_value(variables.DYSLIPIDEMIA_PERCENTAGE),
        'familial_hypercholesterolemia': generate_values.two_options_value(variables.FAMILIAL_HYPERCHOLESTEROLEMIA),
        'alco': generate_values.two_options_value(variables.ALCOHOLIC_PERCENTAGE), # 0 = no alcoholic, 1 = alcoholic
        'atrial_fibrillation': 0,
        'anxiety_disorder': 0,
        'depressive_disorder': 0,
        'psychosis': generate_values.two_options_value(variables.PSYCHOSIS_PERCENTAGE),
        'colt': generate_values.generate_ranged_value(variables.COLT_MIN_VALUE, 
                                      variables.COLT_MAX_VALUE, 
                                      variables.COLT_LIMIT_VALUE, 
                                      variables.COLT_PERCENTAGE),
        'ldl': generate_values.generate_ranged_value(variables.LDL_MIN_VALUE, 
                                     variables.LDL_MAX_VALUE, 
                                     variables.LDL_LIMIT_VALUE, 
                                     variables.LDL_PERCENTAGE),
        'tg': 0,
        'antidepressants': generate_values.two_options_value(variables.ANTIDEPRESSANTS_PERCENTAGE),
        'antidiabetic_treatment': 0,
        'antihypertensive_treatment': 0,
        'lipid_lowering_treatment': 0,
        'chronic_renal_failure': 0,
        'renal_replacement_therapy': 0,
        'kidney_transplant': 0,
        'COVID_history': generate_values.two_options_value(variables.COVID_HISTORY_PERCENTAGE),
        'anemima': generate_values.two_options_value(variables.ANEMIMA_PERCENTAGE),
        'chronic_obstructive': 0,
        'severe_obstructive_sleep_apnea': 0,
        'fatty_liver': generate_values.two_options_value(variables.FATTY_LIVER_PERCENTAGE),
        'erectile_dysfunction': 0,
        'rheumatoid_arthritis': generate_values.two_options_value(variables.RHEUMATOID_PERCENTAGE),
        'migraines': 0,
        'systemic_lupus_erythematosus': generate_values.two_options_value(variables.SYSTEMIC_ERYTHEMATOSUS_PERCENTAGE),
        'alzheimer': 0,
        #'diastolic_blood_pressure': 0,
        'systolic_blood_pressure': 0,
        'score': 0
    }


def generate_profile():
    basic_profile = generate_basic_profile()
    gender_dependant_profile = update_profile_dependency.update_gender_dependant(basic_profile)
    age_dependant_profile = update_profile_dependency.update_age_dependant(gender_dependant_profile)
    renal_therapy_profile = update_profile_dependency.update_renal_therapy_dependant(age_dependant_profile)
    kidney_transplant_profile = update_profile_dependency.update_kidney_transplant_dependant(renal_therapy_profile)
    final_profile = update_profile_dependency.get_score(kidney_transplant_profile)
    return final_profile

def check_values(profile, controller):
    controller += check_profile.check_gender(profile)
    controller += check_profile.check_ethnic(profile)
    controller += check_profile.check_poverty(profile)
    controller += check_profile.check_smoke(profile)
    controller += check_profile.check_ascvd(profile)
    controller += check_profile.check_icm(profile)
    controller += check_profile.check_mellitus_diabetis(profile)
    controller += check_profile.check_hypertension(profile)
    controller += check_profile.check_dyslipidemia(profile)
    controller += check_profile.check_familial_hypercholesterolemia(profile)
    controller += check_profile.check_alco(profile)
    controller += check_profile.check_atrial_fibrillation(profile)
    controller += check_profile.check_anxiety_disorder(profile)
    controller += check_profile.check_depressive_disorder(profile)
    controller += check_profile.check_psychosis(profile)
    controller += check_profile.check_colt(profile)
    controller += check_profile.check_ldl(profile)
    controller += check_profile.check_tg(profile)
    controller += check_profile.check_antidepressants(profile)
    controller += check_profile.check_antidiabetic_treatment(profile)
    controller += check_profile.check_antihypertensive_treatment(profile)
    controller += check_profile.check_lipid_lowering_treatment(profile)
    controller += check_profile.check_chronic_renal_failure(profile)
    controller += check_profile.check_renal_replacement_therapy(profile)
    controller += check_profile.check_kidney_transplant(profile)
    controller += check_profile.check_covid(profile)
    controller += check_profile.check_anemima(profile)
    controller += check_profile.check_chronic_obstructive(profile)
    controller += check_profile.check_severe_obstructive_sleep_apnea(profile)
    controller += check_profile.check_fatty_liver(profile)
    controller += check_profile.check_erectile_dysfunction(profile)
    controller += check_profile.check_rheumatoid_arthritis(profile)
    controller += check_profile.check_migraines(profile)
    controller += check_profile.check_systemic_lupus_erythematosus(profile)
    controller += check_profile.check_alzheimer(profile)
    controller += check_profile.check_systolic_blood_pressure(profile)
    
    return controller


controller = 1
count = 0

while controller:
    controller = 0
    count += 1
    # Creates profiles
    newCSV = [generate_profile() for _ in range(variables.NUM_PROFILES)]

    controller = check_values(newCSV, controller)

print('TERMINADO SIN PROBLEMAS')
print(f'Nº repeticiones hasta satisfacer los requisitos: {count}')

# Saves generated profile to CSV
#with open('./profiles/tfg.csv', 'w', newline='') as file:
#    writer_to_csv = csv.writer(file, delimiter=';')
#    writer_to_csv.writerow(newCSV[0])
#    for line in newCSV:
#        writer_to_csv.writerow(line.values())