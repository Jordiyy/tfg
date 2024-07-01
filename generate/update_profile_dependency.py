import generate_values
import variables
import score_steps
import random
import math


def update_gender_dependant(profile):
    if profile['gender'] == 0: # WOMEN
        profile['poverty'] = generate_values.two_options_value(variables.WOMEN_POVERTY_PERCENTAGE)
        profile['hypertension'] = generate_values.two_options_value(variables.WOMEN_HYPERTENSION_PERCENTAGE)
        profile['anxiety_disorder'] = generate_values.two_options_value(variables.WOMEN_ANXIETY_DISORDER_PERCENTAGE)
        profile['depressive_disorder'] = generate_values.two_options_value(variables.WOMEN_DEPRESSIVE_DISORDER_PERCENTAGE)
        profile['tg'] = generate_values.generate_ranged_value(variables.TG_MIN_VALUE,
                                          variables.TG_MAX_VALUE,
                                          variables.TG_LIMIT_VALUE,
                                          variables.WOMEN_TG_PERCENTAGE)
        profile['antidiabetic_treatment'] = generate_values.two_options_value(variables.WOMEN_ANTIDIABETIC_TREATMENT_PERCENTAGE)
        profile['antihypertensive_treatment'] = generate_values.two_options_value(variables.WOMEN_ANTIHYPERTENSIVE_TREATMENT_PERCENTAGE)
        profile['lipid_lowering_treatment'] = generate_values.two_options_value(variables.WOMEN_LIPID_LOWERING_TREATMENT_PERCENTAGE)
        profile['chronic_renal_failure'] = generate_values.two_options_value(variables.WOMEN_CHRONIC_RENAL_FAILURE_PERCENTAGE)
        profile['chronic_obstructive'] = generate_values.two_options_value(variables.WOMEN_CHRONIC_OBSTRUCTIVE_PERCENTAGE)
        profile['severe_obstructive_sleep_apnea'] = generate_values.two_options_value(variables.WOMEN_SEVERE_OBSTRUCTIVE_SLEEP_APNEA_PERCENTAGE)
        profile['migraines'] = generate_values.two_options_value(variables.WOMEN_MIGRAINES_PERCENTAGE)
        #profile['diastolic_blood_pressure'] = generate_ranged_value(variables.DIASTOLIC_BLOOD_PRESSURE_MIN_VALUE, variables.DIASTOLIC_BLOOD_PRESSURE_MAX_VALUE, variables.DIASTOLIC_BLOOD_PRESSURE_LIMIT_VALUE, variables.WOMEN_DIASTOLIC_BLOOD_PRESSURE_PERCENTAGE)
        profile['systolic_blood_pressure'] = generate_values.generate_ranged_value(variables.SYSTOLIC_BLOOD_PRESSURE_MIN_VALUE,
                                                                   variables.SYSTOLIC_BLOOD_PRESSURE_MAX_VALUE,
                                                                   variables.SYSTOLIC_BLOOD_PRESSURE_LIMIT_VALUE,
                                                                   variables.WOMEN_SYSTOLIC_BLOOD_PRESSURE_PERCENTAGE)
        
        return profile
    else: # MEN
        profile['poverty'] = generate_values.two_options_value(variables.MEN_POVERTY_PERCENTAGE)
        profile['hypertension'] = generate_values.two_options_value(variables.MEN_HYPERTENSION_PERCENTAGE)
        profile['anxiety_disorder'] = generate_values.two_options_value(variables.MEN_ANXIETY_DISORDER_PERCENTAGE)
        profile['depressive_disorder'] = generate_values.two_options_value(variables.MEN_DEPRESSIVE_DISORDER_PERCENTAGE)
        profile['tg'] = generate_values.generate_ranged_value(variables.TG_MIN_VALUE, 
                                              variables.TG_MAX_VALUE, 
                                              variables.TG_LIMIT_VALUE, 
                                              variables.MEN_TG_PERCENTAGE)
        profile['antidiabetic_treatment'] = generate_values.two_options_value(variables.MEN_ANTIDIABETIC_TREATMENT_PERCENTAGE)
        profile['antihypertensive_treatment'] = generate_values.two_options_value(variables.MEN_ANTIHYPERTENSIVE_TREATMENT_PERCENTAGE)
        profile['lipid_lowering_treatment'] = generate_values.two_options_value(variables.MEN_LIPID_LOWERING_TREATMENT_PERCENTAGE)
        profile['chronic_renal_failure'] = generate_values.two_options_value(variables.MEN_CHRONIC_RENAL_FAILURE_PERCENTAGE)
        profile['chronic_obstructive'] = generate_values.two_options_value(variables.MEN_CHRONIC_OBSTRUCTIVE_PERCENTAGE)
        profile['severe_obstructive_sleep_apnea'] = generate_values.two_options_value(variables.MEN_SEVERE_OBSTRUCTIVE_SLEEP_APNEA_PERCENTAGE)
        profile['erectile_dysfunction'] = generate_values.two_options_value(variables.ERECTILE_DYSFUNCTION) 
        profile['migraines'] = generate_values.two_options_value(variables.MEN_MIGRAINES_PERCENTAGE) 
        #profile['diastolic_blood_pressure'] = generate_values.generate_ranged_value(variables.DIASTOLIC_BLOOD_PRESSURE_MIN_VALUE, variables.DIASTOLIC_BLOOD_PRESSURE_MAX_VALUE, variables.DIASTOLIC_BLOOD_PRESSURE_LIMIT_VALUE, variables.MEN_DIASTOLIC_BLOOD_PRESSURE_PERCENTAGE)
        profile['systolic_blood_pressure'] = generate_values.generate_ranged_value(variables.SYSTOLIC_BLOOD_PRESSURE_MIN_VALUE,
                                                                   variables.SYSTOLIC_BLOOD_PRESSURE_MAX_VALUE,
                                                                   variables.SYSTOLIC_BLOOD_PRESSURE_LIMIT_VALUE,
                                                                   variables.MEN_SYSTOLIC_BLOOD_PRESSURE_PERCENTAGE)
        
        return profile


def update_age_dependant(profile):
    if (profile['age'] / 365) > 40:
        profile['atrial_fibrillation'] = generate_values.two_options_value(variables.ATRIAL_FIBRILLATION_AGE_DEPENDANT_PERCENTAGE)
    else:
        profile['atrial_fibrillation'] = generate_values.two_options_value(variables.ATRIAL_FIBRILLATION_PERCENTAGE)
    
    if (profile['age'] / 365) > 65:
        profile['alzheimer'] = generate_values.two_options_value(variables.LOW_ALZHEIMER_PERCENTAGE)
        #profile['alzheimer'] = generate_values.two_options_value(variables.HIGH_ALZHEIMER_PERCENTAGE)
        
    return profile


def update_renal_therapy_dependant(profile):
    #if profile['chronic_renal_failure'] == 1:
    #    profile['renal_replacement_therapy'] = generate_values.two_options_value(variables.RENAL_REPLACEMENT_THERAPY)
    profile['renal_replacement_therapy'] = generate_values.two_options_value(variables.RENAL_REPLACEMENT_THERAPY)
    
    return profile
        

def update_kidney_transplant_dependant(profile):
    #if profile['renal_replacement_therapy'] == 1:
    #    profile['kidney_transplant'] = generate_values.two_options_value(variables.KIDNEY_TRANSPLANT_PERCENTAGE)
    profile['kidney_transplant'] = generate_values.two_options_value(variables.KIDNEY_TRANSPLANT_PERCENTAGE)
    
    return profile


def get_score(profile):
    age = int(profile['age'] / 365)
    
    if profile['gender'] == 0:
        chd_risk = score_steps.get_risk_value(age,
                                              profile['colt'], 
                                              profile['systolic_blood_pressure'], 
                                              profile['smoke'], 
                                              variables.ALPHA_CHD_WOMEN, 
                                              variables.CHOLESTEROL_CHD,
                                              variables.SYSTOLIC_CHD, 
                                              variables.SMOKER_CHD, 
                                              variables.P_CHD_WOMEN)
        non_chd_risk = score_steps.get_risk_value(age,
                                              profile['colt'], 
                                              profile['systolic_blood_pressure'], 
                                              profile['smoke'], 
                                              variables.ALPHA_NONCHD_WOMEN, 
                                              variables.CHOLESTEROL_NONCHD,
                                              variables.SYSTOLIC_NONCHD, 
                                              variables.SMOKER_NONCHD, 
                                              variables.P_NONCHD_WOMEN)
    else:
        chd_risk = score_steps.get_risk_value(age,
                                              profile['colt'], 
                                              profile['systolic_blood_pressure'], 
                                              profile['smoke'], 
                                              variables.ALPHA_CHD_MEN, 
                                              variables.CHOLESTEROL_CHD,
                                              variables.SYSTOLIC_CHD, 
                                              variables.SMOKER_CHD, 
                                              variables.P_CHD_MEN)
        non_chd_risk = score_steps.get_risk_value(age,
                                              profile['colt'], 
                                              profile['systolic_blood_pressure'], 
                                              profile['smoke'], 
                                              variables.ALPHA_NONCHD_MEN, 
                                              variables.CHOLESTEROL_NONCHD,
                                              variables.SYSTOLIC_NONCHD, 
                                              variables.SMOKER_NONCHD, 
                                              variables.P_NONCHD_MEN)
    
    profile['score'] = score_steps.get_final_risk(chd_risk, non_chd_risk)
    
    return profile 


def fake_score(profile):
    if int(profile['age'] / 365) < 50:
        profile['score'] = round(random.gauss(5, 1.6667), 2)
    elif 50 <= int(profile['age'] / 365) <= 69:
        profile['score'] = round(random.gauss(7.5, 3.3333), 2)
    else:
        profile['score'] = round(random.gauss(11.25, 4.1667), 2)
        
    if profile['score'] < 0:
        profile['score'] = 0
    
    return profile


def fake_score_manual(profile):
    profile['score'] = (int(profile['age'] / 365) / 80) * ((profile['ldl'] / profile['colt']) * (profile['systolic_blood_pressure'] / 50) * (1.5 * profile['smoke']))
    profile['score'] = math.exp(profile['score'])
        
    return profile