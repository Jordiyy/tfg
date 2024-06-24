import variables


def gender_dependant(profiles, column, check_percentage_women, check_percentage_men):
    women_count = 0
    women_total = 0
    men_count = 0
    men_total = 0
    
    for profile in profiles:
        if profile['gender'] == 0:
            women_total += 1
            if profile[column] == 1:
                women_count += 1
        else:
            men_total += 1
            if profile[column] == 1:
                men_count += 1
            
    men_percentage = men_count / men_total * 100
    women_percentage = women_count / women_total * 100
    
    print(f"Porcentaje {column} mujeres ({check_percentage_women}%):", f"{women_percentage:.2f}%")
    print(f"Porcentaje {column} hombres ({check_percentage_men}%):", f"{men_percentage:.2f}%")
    if ((check_percentage_men - variables.TOLERANCE) <= men_percentage <= (check_percentage_men + variables.TOLERANCE)) and ((check_percentage_women - variables.TOLERANCE) <= women_percentage <= (check_percentage_women + variables.TOLERANCE)):
        print('OK')
        return 0
    else:
        print('ERROR')
        return 1


def non_gender_dependant(profiles, column, check_percentage):
    count = 0
    
    for profile in profiles:
        if profile[column] == 1:
            count = count + 1
            
    count_percentage = count / len(profiles) * 100
    
    print(f"Porcentaje {column} ({check_percentage}%):", f"{count_percentage:.2f}%")
    if (check_percentage - variables.TOLERANCE) <= count_percentage <= (check_percentage + variables.TOLERANCE):
        print('OK')
        return 0
    else:
        print('ERROR')
        return 1


def check_gender(profiles):
    men = 0
    women = 0
    
    for profile in profiles:
        if profile['gender'] == 0:
            women = women + 1
        else:
            men = men + 1
            
    women_percentage = women / len(profiles) * 100
    men_percentage = men / len(profiles) * 100
    
    print(f"Porcentaje mujer ({100 - variables.MENS_PERCENTAGE}%):", f"{women_percentage:.2f}%")
    print(f"Porcentaje hombre ({variables.MENS_PERCENTAGE}%):", f"{men_percentage:.2f}%")
    if ((variables.MENS_PERCENTAGE - variables.TOLERANCE) <= men_percentage <= (variables.MENS_PERCENTAGE + variables.TOLERANCE)) and ((100 - variables.MENS_PERCENTAGE - variables.TOLERANCE) <= women_percentage <= (100 - variables.MENS_PERCENTAGE + variables.TOLERANCE)):
        print('OK')
        return 0
    else:
        print('ERROR')
        return 1
    

def check_ethnic(profiles):
    caucasian = 0
    african = 0
    asian = 0
    
    for profile in profiles:
        if profile['ethnic'] == 0:
            caucasian = caucasian + 1
        elif profile['ethnic'] == 1:
            african = african + 1
        else:
            asian = asian + 1
            
    caucasian_percentage = caucasian / len(profiles) * 100
    african_percentage = african / len(profiles) * 100
    asian_percentage = asian / len(profiles) * 100
    
    print(f"Porcentaje caucásico ({variables.CAUCASIAN_ETHNIC_PERCENTAGE}%):", f"{caucasian_percentage:.2f}%")
    print(f"Porcentaje africano ({variables.AFRICAN_ETHNIC_PERCENTAGE}%):", f"{african_percentage:.2f}%")
    print(f"Porcentaje asiático ({variables.ASIAN_ETHNIC_PERCENTAGE}%):", f"{asian_percentage:.2f}%")
    if ((variables.CAUCASIAN_ETHNIC_PERCENTAGE - variables.TOLERANCE) <= caucasian_percentage <= (variables.CAUCASIAN_ETHNIC_PERCENTAGE + variables.TOLERANCE)) and ((variables.AFRICAN_ETHNIC_PERCENTAGE - variables.TOLERANCE) <= african_percentage <= (variables.AFRICAN_ETHNIC_PERCENTAGE + variables.TOLERANCE)) and ((variables.ASIAN_ETHNIC_PERCENTAGE - variables.TOLERANCE) <= asian_percentage <= (variables.ASIAN_ETHNIC_PERCENTAGE + variables.TOLERANCE)):
        print('OK')
        return 0
    else:
        print('ERROR')
        return 1
    
    
def check_poverty(profiles):
    return gender_dependant(profiles, 'poverty', variables.WOMEN_POVERTY_PERCENTAGE, variables.MEN_POVERTY_PERCENTAGE)


def check_smoke(profiles):
    return non_gender_dependant(profiles, 'smoke', variables.SMOKER_PERCENTAGE)


def check_ascvd(profiles):
    return non_gender_dependant(profiles, 'ascvd', variables.ASCVD_PERCENTAGE)


def check_icm(profiles):
    less_25 = 0
    between_25_30 = 0
    more_30 = 0
    
    for profile in profiles:
        if profile['icm'] < 25:
            less_25 = less_25 + 1
        elif profile['icm'] >= 25 and profile['icm'] <= 30:
            between_25_30 = between_25_30 + 1
        else:
            more_30 = more_30 + 1
            
    percentage_less_25 = less_25 / len(profiles) * 100
    percentage_between_25_30 = between_25_30 / len(profiles) * 100
    percentage_more_30 = more_30 / len(profiles) * 100
    
    print(f"Porcentaje icm menor 25 (32%):", f"{percentage_less_25:.2f}%")
    print(f"Porcentaje icm ente 25 y 30 (39%):", f"{percentage_between_25_30:.2f}%")
    print(f"Porcentaje icm mayor 30 (29%):", f"{percentage_more_30:.2f}%")
    
    if ((32 - variables.TOLERANCE) <= percentage_less_25 <= (32 + variables.TOLERANCE)) and ((39 - variables.TOLERANCE) <= percentage_between_25_30 <= (39 + variables.TOLERANCE)) and ((29 - variables.TOLERANCE) <= percentage_more_30 <= (29 + variables.TOLERANCE)):
        print('OK')
        return 0
    else:
        print('ERROR')
        return 1
    

def check_mellitus_diabetis(profiles):
    return non_gender_dependant(profiles, 'mellitus_diabetis', variables.MELLITUS_DIABETIS_PERCENTAGE)


def check_hypertension(profiles):
    return gender_dependant(profiles, 'hypertension', variables.WOMEN_HYPERTENSION_PERCENTAGE, variables.MEN_HYPERTENSION_PERCENTAGE)
    

def check_dyslipidemia(profiles):
    return non_gender_dependant(profiles, 'dyslipidemia', variables.DYSLIPIDEMIA_PERCENTAGE)
    

def check_familial_hypercholesterolemia(profiles):
    return non_gender_dependant(profiles, 'familial_hypercholesterolemia', variables.FAMILIAL_HYPERCHOLESTEROLEMIA)


def check_alco(profiles):
    return non_gender_dependant(profiles, 'alco', variables.ALCOHOLIC_PERCENTAGE)


def check_atrial_fibrillation(profiles):
    atrial_less_40 = 0
    age_less_40 = 0
    atrial_more_40 = 0
    age_more_40 = 0
    
    for profile in profiles:
        if profile['age'] / 365 < 40:
            age_less_40 = age_less_40 + 1
            if profile['atrial_fibrillation'] == 1:
                atrial_less_40 = atrial_less_40 + 1
        else:
            age_more_40 = age_more_40 + 1
            if profile['atrial_fibrillation'] == 1:
                atrial_more_40 = atrial_more_40 + 1
            
    atrial_less_40_percentage = atrial_less_40 / age_less_40 * 100
    atrial_more_40_percentage = atrial_more_40 / age_more_40 * 100
    
    print(f"Porcentaje atrial ({variables.ATRIAL_FIBRILLATION_PERCENTAGE}%):", f"{atrial_less_40_percentage:.2f}%")
    print(f"Porcentaje atrial age dependant ({variables.ATRIAL_FIBRILLATION_AGE_DEPENDANT_PERCENTAGE}%):", f"{atrial_more_40_percentage:.2f}%")
    if ((variables.ATRIAL_FIBRILLATION_PERCENTAGE - variables.TOLERANCE) <= atrial_less_40_percentage <= (variables.ATRIAL_FIBRILLATION_PERCENTAGE + variables.TOLERANCE)) and ((variables.ATRIAL_FIBRILLATION_AGE_DEPENDANT_PERCENTAGE - variables.TOLERANCE) <= atrial_more_40_percentage <= (variables.ATRIAL_FIBRILLATION_AGE_DEPENDANT_PERCENTAGE + variables.TOLERANCE)):
        print('OK')
        return 0
    else:
        print('ERROR')
        return 1  


def check_anxiety_disorder(profiles):
    return gender_dependant(profiles, 'anxiety_disorder', variables.WOMEN_ANXIETY_DISORDER_PERCENTAGE, variables.MEN_ANXIETY_DISORDER_PERCENTAGE)


def check_depressive_disorder(profiles):
    return gender_dependant(profiles, 'depressive_disorder', variables.WOMEN_DEPRESSIVE_DISORDER_PERCENTAGE, variables.MEN_DEPRESSIVE_DISORDER_PERCENTAGE)


def check_psychosis(profiles):
    return non_gender_dependant(profiles, 'psychosis', variables.PSYCHOSIS_PERCENTAGE)


def check_colt(profiles):
    colt = 0
    
    for profile in profiles:
        if profile['colt'] >= 200:
            colt = colt + 1
            
    colt_percentage = colt / len(profiles) * 100
    
    print(f"Porcentaje colt mayor a 200 mg/dL ({variables.COLT_PERCENTAGE}%):", f"{colt_percentage:.2f}%")
    if (variables.COLT_PERCENTAGE - variables.TOLERANCE) <= colt_percentage <= (variables.COLT_PERCENTAGE + variables.TOLERANCE):
        print('OK')
        return 0
    else:
        print('ERROR')
        return 1


def check_ldl(profiles):
    ldl = 0
    
    for profile in profiles:
        if profile['ldl'] >= 130:
            ldl = ldl + 1
            
    ldl_percentage = ldl / len(profiles) * 100
    
    print(f"Porcentaje colesterol ldl mayor a 130 mg/dL ({variables.LDL_PERCENTAGE}%):", f"{ldl_percentage:.2f}%")
    if (variables.LDL_PERCENTAGE - variables.TOLERANCE) <= ldl_percentage <= (variables.LDL_PERCENTAGE + variables.TOLERANCE):
        print('OK')
        return 0
    else:
        print('ERROR')
        return 1


def check_tg(profiles):
    women_tg = 0
    women = 0
    men_tg = 0
    men = 0
    
    for profile in profiles:
        if profile['gender'] == 0:
            women = women + 1
            if profile['tg'] >= 150:
                women_tg = women_tg + 1
        else:
            men = men + 1
            if profile['tg'] >= 150:
                men_tg = men_tg + 1
            
    men_tg_percentage = men_tg / men * 100
    women_tg_percentage = women_tg / women * 100
    
    print(f"Porcentaje triglicéridos mujeres mayor 150 mg/dL ({variables.WOMEN_TG_PERCENTAGE}%):", f"{women_tg_percentage:.2f}%")
    print(f"Porcentaje triglicéridos hombres mayor 150 mg/dL ({variables.MEN_TG_PERCENTAGE}%):", f"{men_tg_percentage:.2f}%")
    
    if ((variables.MEN_TG_PERCENTAGE - variables.TOLERANCE) <= men_tg_percentage <= (variables.MEN_TG_PERCENTAGE + variables.TOLERANCE)) and ((variables.WOMEN_TG_PERCENTAGE - variables.TOLERANCE) <= women_tg_percentage <= (variables.WOMEN_TG_PERCENTAGE + variables.TOLERANCE)):
        print('OK')
        return 0
    else:
        print('ERROR')
        return 1


def check_antidepressants(profiles):
    return non_gender_dependant(profiles, 'antidepressants', variables.ANTIDEPRESSANTS_PERCENTAGE)


def check_antidiabetic_treatment(profiles):
    return gender_dependant(profiles, 'antidiabetic_treatment', variables.WOMEN_ANTIDIABETIC_TREATMENT_PERCENTAGE, variables.MEN_ANTIDIABETIC_TREATMENT_PERCENTAGE)


def check_antihypertensive_treatment(profiles):
    return gender_dependant(profiles, 'antihypertensive_treatment', variables.WOMEN_ANTIHYPERTENSIVE_TREATMENT_PERCENTAGE, variables.MEN_ANTIHYPERTENSIVE_TREATMENT_PERCENTAGE)


def check_lipid_lowering_treatment(profiles):
    return gender_dependant(profiles, 'lipid_lowering_treatment', variables.WOMEN_LIPID_LOWERING_TREATMENT_PERCENTAGE, variables.MEN_LIPID_LOWERING_TREATMENT_PERCENTAGE)


def check_chronic_renal_failure(profiles):
    return gender_dependant(profiles, 'chronic_renal_failure', variables.WOMEN_CHRONIC_RENAL_FAILURE_PERCENTAGE, variables.MEN_CHRONIC_RENAL_FAILURE_PERCENTAGE)


def check_renal_replacement_therapy(profiles):
    return non_gender_dependant(profiles, 'renal_replacement_therapy', variables.RENAL_REPLACEMENT_THERAPY)


def check_kidney_transplant(profiles):
    return non_gender_dependant(profiles, 'kidney_transplant', variables.KIDNEY_TRANSPLANT_PERCENTAGE)


def check_covid(profiles):
    return non_gender_dependant(profiles, 'COVID_history', variables.COVID_HISTORY_PERCENTAGE)


def check_anemima(profiles):
    return non_gender_dependant(profiles, 'anemima', variables.ANEMIMA_PERCENTAGE)


def check_chronic_obstructive(profiles):
    return gender_dependant(profiles, 'chronic_obstructive', variables.WOMEN_CHRONIC_OBSTRUCTIVE_PERCENTAGE, variables.MEN_CHRONIC_OBSTRUCTIVE_PERCENTAGE)


def check_severe_obstructive_sleep_apnea(profiles):
    return gender_dependant(profiles, 'severe_obstructive_sleep_apnea', variables.WOMEN_SEVERE_OBSTRUCTIVE_SLEEP_APNEA_PERCENTAGE, variables.MEN_SEVERE_OBSTRUCTIVE_SLEEP_APNEA_PERCENTAGE)


def check_fatty_liver(profiles):
    return non_gender_dependant(profiles, 'fatty_liver', variables.FATTY_LIVER_PERCENTAGE)


def check_erectile_dysfunction(profiles):
    return gender_dependant(profiles, 'erectile_dysfunction', 0, variables.ERECTILE_DYSFUNCTION)


def check_rheumatoid_arthritis(profiles):
    return non_gender_dependant(profiles, 'rheumatoid_arthritis', variables.RHEUMATOID_PERCENTAGE)


def check_migraines(profiles):
    return gender_dependant(profiles, 'migraines', variables.WOMEN_MIGRAINES_PERCENTAGE, variables.MEN_MIGRAINES_PERCENTAGE)


def check_systemic_lupus_erythematosus(profiles):
    return non_gender_dependant(profiles, 'systemic_lupus_erythematosus', variables.SYSTEMIC_ERYTHEMATOSUS_PERCENTAGE)


def check_alzheimer(profiles):
    alzheimer_more_65 = 0
    age_more_65 = 0
    
    for profile in profiles:
        if profile['age'] / 365 > 65:
            age_more_65 = age_more_65 + 1
            if profile['alzheimer'] == 1:
                alzheimer_more_65 = alzheimer_more_65 + 1
            
    alzheimer_more_65_percentage = alzheimer_more_65 / age_more_65 * 100
    
    print(f"Porcentaje alzheimer ({variables.LOW_ALZHEIMER_PERCENTAGE}%):", f"{alzheimer_more_65_percentage:.2f}%")
    if (variables.LOW_ALZHEIMER_PERCENTAGE - variables.TOLERANCE) <= alzheimer_more_65_percentage <= (variables.LOW_ALZHEIMER_PERCENTAGE + variables.TOLERANCE):
        print('OK')
        return 0
    else:
        print('ERROR')
        return 1


def check_systolic_blood_pressure(profiles):
    women_systolic_count = 0
    women_total = 0
    men_systolic_count = 0
    men_total = 0
    
    for profile in profiles:
        if profile['gender'] == 0:
            women_total = women_total + 1
            if profile['systolic_blood_pressure'] > variables.SYSTOLIC_BLOOD_PRESSURE_LIMIT_VALUE:
                women_systolic_count = women_systolic_count + 1
        else:
            men_total = men_total + 1
            if profile['systolic_blood_pressure'] > variables.SYSTOLIC_BLOOD_PRESSURE_LIMIT_VALUE:
                men_systolic_count = men_systolic_count + 1
            
    men_percentage = men_systolic_count / men_total * 100
    women_percentage = women_systolic_count / women_total * 100
    
    print(f"Porcentaje systolic_blood_pressure mujeres ({variables.WOMEN_SYSTOLIC_BLOOD_PRESSURE_PERCENTAGE}%):", f"{women_percentage:.2f}%")
    print(f"Porcentaje systolic_blood_pressure hombres ({variables.MEN_SYSTOLIC_BLOOD_PRESSURE_PERCENTAGE}%):", f"{men_percentage:.2f}%")
    if ((variables.MEN_SYSTOLIC_BLOOD_PRESSURE_PERCENTAGE - variables.TOLERANCE) <= men_percentage <= (variables.MEN_SYSTOLIC_BLOOD_PRESSURE_PERCENTAGE + variables.TOLERANCE)) and ((variables.WOMEN_SYSTOLIC_BLOOD_PRESSURE_PERCENTAGE - variables.TOLERANCE) <= women_percentage <= (variables.WOMEN_SYSTOLIC_BLOOD_PRESSURE_PERCENTAGE + variables.TOLERANCE)):
        print('OK')
        return 0
    else:
        print('ERROR')
        return 1



