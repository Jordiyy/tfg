import pandas as pd
import random
import csv
import io
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
    #final_profile = update_profile_dependency.get_score(kidney_transplant_profile)
    #final_profile = update_profile_dependency.fake_score(kidney_transplant_profile)
    final_profile = update_profile_dependency.fake_score_manual(kidney_transplant_profile)
    return final_profile


def check_values(profile):
    results = []
    controller = 0
    counter = 0
    value = 0
    value1 = 0
    value2 = 0
    
    controller, value, value1 = check_profile.check_gender(profile)
    counter += controller
    results.append({
        "nombre": "gender_women",
        "percentage": 100 - variables.MENS_PERCENTAGE,
        "result": value1
    })
    results.append({
        "nombre": "gender_men",
        "percentage": variables.MENS_PERCENTAGE,
        "result": value
    })
    
    controller, value, value1 = check_profile.check_ethnic(profile)
    counter += controller
    results.append({
        "nombre": "caucassian_ethnic",
        "percentage": variables.CAUCASIAN_ETHNIC_PERCENTAGE,
        "result": value
    })
    results.append({
        "nombre": "african_ethnic",
        "percentage": variables.AFRICAN_ETHNIC_PERCENTAGE,
        "result": value1
    })
    results.append({
        "nombre": "asian_ethnic",
        "percentage": variables.ASIAN_ETHNIC_PERCENTAGE,
        "result": round(100 - value - value1, 2)
    })
    
    controller, value, value1 = check_profile.check_poverty(profile)
    counter += controller
    results.append({
        "nombre": "women_poverty",
        "percentage": variables.WOMEN_POVERTY_PERCENTAGE,
        "result": value1
    })
    results.append({
        "nombre": "men_poverty",
        "percentage": variables.MEN_POVERTY_PERCENTAGE,
        "result": value
    })
    
    controller, value = check_profile.check_smoke(profile)
    counter += controller
    results.append({
        "nombre": "smoke",
        "percentage": variables.SMOKER_PERCENTAGE,
        "result": value
    })
    

    controller, value = check_profile.check_ascvd(profile)
    counter += controller
    results.append({
        "nombre": "ascvd",
        "percentage": variables.ASCVD_PERCENTAGE,
        "result": value
    })
    
    controller, value, value1, value2 = check_profile.check_icm(profile)
    counter += controller
    results.append({
        "nombre": "icm_less_25",
        "percentage": 32,
        "result": value
    })
    results.append({
        "nombre": "icm_between_25_30",
        "percentage": 39,
        "result": value1
    })
    results.append({
        "nombre": "icm_more_30",
        "percentage": 29,
        "result": value2
    })
    
    controller, value = check_profile.check_mellitus_diabetis(profile)
    counter += controller
    results.append({
        "nombre": "mellitus_diabetis",
        "percentage": variables.MELLITUS_DIABETIS_PERCENTAGE,
        "result": value2
    })
    
    controller, value, value1  = check_profile.check_hypertension(profile)
    counter += controller
    results.append({
        "nombre": "women_hypertension",
        "percentage": variables.WOMEN_HYPERTENSION_PERCENTAGE,
        "result": value1
    })
    results.append({
        "nombre": "men_hypertension",
        "percentage": variables.MEN_HYPERTENSION_PERCENTAGE,
        "result": value
    })
    
    controller, value = check_profile.check_dyslipidemia(profile)
    counter += controller
    results.append({
        "nombre": "dyslipidemia",
        "percentage": variables.DYSLIPIDEMIA_PERCENTAGE,
        "result": value
    })
    
    controller, value = check_profile.check_familial_hypercholesterolemia(profile)
    counter += controller
    results.append({
        "nombre": "familial_hypercholesterolemia",
        "percentage": variables.FAMILIAL_HYPERCHOLESTEROLEMIA,
        "result": value
    })
    
    controller, value = check_profile.check_alco(profile)
    counter += controller
    results.append({
        "nombre": "alco",
        "percentage": variables.ALCOHOLIC_PERCENTAGE,
        "result": value
    })
    
    controller, value, value1 = check_profile.check_atrial_fibrillation(profile)
    counter += controller
    results.append({
        "nombre": "atrial_fibrillation",
        "percentage": variables.ATRIAL_FIBRILLATION_PERCENTAGE,
        "result": value
    })
    results.append({
        "nombre": "age_dependant_atrial_fibrillation",
        "percentage": variables.ATRIAL_FIBRILLATION_AGE_DEPENDANT_PERCENTAGE,
        "result": value1
    })
    
    controller, value, value1 = check_profile.check_anxiety_disorder(profile)
    counter += controller
    results.append({
        "nombre": "women_anxiety_disorder",
        "percentage": variables.WOMEN_ANXIETY_DISORDER_PERCENTAGE,
        "result": value1
    })
    results.append({
        "nombre": "men_anxiety_disorder",
        "percentage": variables.MEN_ANXIETY_DISORDER_PERCENTAGE,
        "result": value
    })
    
    controller, value, value1 = check_profile.check_depressive_disorder(profile)
    counter += controller
    results.append({
        "nombre": "women_depressive_disorder",
        "percentage": variables.WOMEN_DEPRESSIVE_DISORDER_PERCENTAGE,
        "result": value1
    })
    results.append({
        "nombre": "men_depressive_disorder",
        "percentage": variables.MEN_DEPRESSIVE_DISORDER_PERCENTAGE,
        "result": value
    })
    
    controller, value = check_profile.check_psychosis(profile)
    counter += controller
    results.append({
        "nombre": "men_depressive_disorder",
        "percentage": variables.PSYCHOSIS_PERCENTAGE,
        "result": value
    })
    
    controller, value = check_profile.check_colt(profile)
    counter += controller
    results.append({
        "nombre": "colt_more_200_mg/dL",
        "percentage": variables.COLT_PERCENTAGE,
        "result": value
    })
    
    controller, value = check_profile.check_ldl(profile)
    counter += controller
    results.append({
        "nombre": "ldl_more_130_mg/dL",
        "percentage": variables.LDL_PERCENTAGE,
        "result": value
    })
    
    controller, value, value1 = check_profile.check_tg(profile)
    counter += controller
    results.append({
        "nombre": "women_tg_more_150_mg/dL",
        "percentage": variables.WOMEN_TG_PERCENTAGE,
        "result": value1
    })
    results.append({
        "nombre": "men_tg_more_150_mg/dL",
        "percentage": variables.MEN_TG_PERCENTAGE,
        "result": value
    })
    
    controller, value = check_profile.check_antidepressants(profile)
    counter += controller
    results.append({
        "nombre": "antidepressants",
        "percentage": variables.ANTIDEPRESSANTS_PERCENTAGE,
        "result": value
    })
    
    controller, value, value1 = check_profile.check_antidiabetic_treatment(profile)
    counter += controller
    results.append({
        "nombre": "antidiabetic_treatment",
        "percentage": variables.WOMEN_ANTIDIABETIC_TREATMENT_PERCENTAGE,
        "result": value1
    })
    results.append({
        "nombre": "antidiabetic_treatment",
        "percentage": variables.MEN_ANTIDIABETIC_TREATMENT_PERCENTAGE,
        "result": value
    })
    
    controller, value, value1 = check_profile.check_antihypertensive_treatment(profile)
    counter += controller
    results.append({
        "nombre": "women_antihypertensive_treatment",
        "percentage": variables.WOMEN_ANTIHYPERTENSIVE_TREATMENT_PERCENTAGE,
        "result": value1
    })
    results.append({
        "nombre": "men_antihypertensive_treatment",
        "percentage": variables.MEN_ANTIHYPERTENSIVE_TREATMENT_PERCENTAGE,
        "result": value
    })
    
    controller, value, value1 = check_profile.check_lipid_lowering_treatment(profile)
    counter += controller
    results.append({
        "nombre": "women_lipid_lowering_treatment",
        "percentage": variables.WOMEN_LIPID_LOWERING_TREATMENT_PERCENTAGE,
        "result": value1
    })
    results.append({
        "nombre": "men_lipid_lowering_treatment",
        "percentage": variables.MEN_LIPID_LOWERING_TREATMENT_PERCENTAGE,
        "result": value
    })
    
    controller, value, value1 = check_profile.check_chronic_renal_failure(profile)
    counter += controller
    results.append({
        "nombre": "women_chronic_renal_failure",
        "percentage": variables.WOMEN_CHRONIC_RENAL_FAILURE_PERCENTAGE,
        "result": value1
    })
    results.append({
        "nombre": "men_chronic_renal_failure",
        "percentage": variables.MEN_CHRONIC_RENAL_FAILURE_PERCENTAGE,
        "result": value
    })
    
    controller, value = check_profile.check_renal_replacement_therapy(profile)
    counter += controller
    results.append({
        "nombre": "renal_replacement_therapy",
        "percentage": variables.RENAL_REPLACEMENT_THERAPY,
        "result": value
    })
    
    controller, value = check_profile.check_kidney_transplant(profile)
    counter += controller
    results.append({
        "nombre": "kidney_transplant",
        "percentage": variables.KIDNEY_TRANSPLANT_PERCENTAGE,
        "result": value
    })
    
    controller, value = check_profile.check_covid(profile)
    counter += controller
    results.append({
        "nombre": "covid",
        "percentage": variables.COVID_HISTORY_PERCENTAGE,
        "result": value
    })
    
    controller, value = check_profile.check_anemima(profile)
    counter += controller
    results.append({
        "nombre": "anemima",
        "percentage": variables.ANEMIMA_PERCENTAGE,
        "result": value
    })
    
    controller, value, value1 = check_profile.check_chronic_obstructive(profile)
    counter += controller
    results.append({
        "nombre": "women_chronic_obstructive",
        "percentage": variables.WOMEN_CHRONIC_OBSTRUCTIVE_PERCENTAGE,
        "result": value1
    })
    results.append({
        "nombre": "men_chronic_obstructive",
        "percentage": variables.MEN_CHRONIC_OBSTRUCTIVE_PERCENTAGE,
        "result": value
    })
    
    controller, value, value1 = check_profile.check_severe_obstructive_sleep_apnea(profile)
    counter += controller
    results.append({
        "nombre": "women_severe_obstructive_sleep_apnea",
        "percentage": variables.WOMEN_SEVERE_OBSTRUCTIVE_SLEEP_APNEA_PERCENTAGE,
        "result": value1
    })
    results.append({
        "nombre": "men_severe_obstructive_sleep_apnea",
        "percentage": variables.MEN_SEVERE_OBSTRUCTIVE_SLEEP_APNEA_PERCENTAGE,
        "result": value
    })
    
    controller, value = check_profile.check_fatty_liver(profile)
    counter += controller
    results.append({
        "nombre": "fatty_liver",
        "percentage": variables.FATTY_LIVER_PERCENTAGE,
        "result": value
    })
    
    controller, value, value1 = check_profile.check_erectile_dysfunction(profile)
    counter += controller
    results.append({
        "nombre": "women_erectile_dysfunction",
        "percentage": 0,
        "result": value1
    })
    results.append({
        "nombre": "men_erectile_dysfunction",
        "percentage": variables.ERECTILE_DYSFUNCTION,
        "result": value
    })
    
    controller, value = check_profile.check_rheumatoid_arthritis(profile)
    counter += controller
    results.append({
        "nombre": "rheumatoid_arthritis",
        "percentage": variables.RHEUMATOID_PERCENTAGE,
        "result": value
    })
    
    controller, value, value1 = check_profile.check_migraines(profile)
    counter += controller
    results.append({
        "nombre": "women_migraines",
        "percentage": variables.WOMEN_MIGRAINES_PERCENTAGE,
        "result": value1
    })
    results.append({
        "nombre": "men_migraines",
        "percentage": variables.MEN_MIGRAINES_PERCENTAGE,
        "result": value
    })
    
    controller, value = check_profile.check_systemic_lupus_erythematosus(profile)
    counter += controller
    results.append({
        "nombre": "systemic_lupus_erythematosus",
        "percentage": variables.SYSTEMIC_ERYTHEMATOSUS_PERCENTAGE,
        "result": value
    })
    
    controller, value = check_profile.check_alzheimer(profile)
    counter += controller
    results.append({
        "nombre": "alzheimer_more_65",
        "percentage": variables.LOW_ALZHEIMER_PERCENTAGE,
        "result": value
    })
    
    controller, value, value1 = check_profile.check_systolic_blood_pressure(profile)
    counter += controller
    results.append({
        "nombre": "women_systolic_blood_pressure",
        "percentage": variables.WOMEN_SYSTOLIC_BLOOD_PRESSURE_PERCENTAGE,
        "result": value1
    })
    results.append({
        "nombre": "men_systolic_blood_pressure",
        "percentage": variables.MEN_SYSTOLIC_BLOOD_PRESSURE_PERCENTAGE,
        "result": value
    })
    
    return counter, results



controller = 1
count = 0

while controller:
    controller = 0
    count += 1
    # Creates profiles
    newCSV = [generate_profile() for _ in range(variables.NUM_PROFILES)]

    controller, res = check_values(newCSV)

print('TERMINADO SIN PROBLEMAS')
print(f'Nº repeticiones hasta satisfacer los requisitos: {count}')


# Saves generated profile to CSV
with open('./compare/score_manual.csv', 'w', newline='') as file:
    writer_to_csv = csv.writer(file, delimiter=';')
    writer_to_csv.writerow(newCSV[0])
    for line in newCSV:
        writer_to_csv.writerow(line.values())
        

with open('./generate/validation.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(["variable", "porcentaje_esperado (%)", "resultado (%)"])
    for line in res:
        variable = line["nombre"]
        porcentaje = line["percentage"]
        resultado = line["result"]
        writer.writerow([variable, porcentaje, resultado])