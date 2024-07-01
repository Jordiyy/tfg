import math


def get_risk_value(age, cholesterol, systolic, smoker, alpha, beta_cholesterol, beta_systolic, beta_smoker, p):
    # Step 1
    internal = math.exp(alpha)
    external = math.exp(-internal)
    s0 = external * (age - 20) * p
    s0_10 = external * (age - 10) * p
    
    # Step 2
    w = (beta_cholesterol * (cholesterol - 6)) + (beta_systolic * (systolic - 120)) + (beta_smoker * smoker)
    
    # Step 3
    w_value = math.exp(w)
    s0 = s0 * w_value
    s0_10 = s0_10 * w_value
    
    # Step 4
    if s0 != 0:
        s10 = s0_10 / s0
    else:
        print(s0)
        s10 = s0_10 
    
    # Step 5
    risk = 1 - s10
    
    return risk


def get_final_risk(chd_risk, non_chd_risk):
    return chd_risk - non_chd_risk