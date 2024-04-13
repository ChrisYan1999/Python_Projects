
def getBondDuration(y, face, couponRate, m, ppy=1):
    cf = couponRate * face / ppy 
    n = m * ppy
    y_adj = y / ppy 

    total_pv = 0 
    weighted_pv_sum = 0 

    for t in range(1, n+1):
        pv_cf_t = cf / ((1 + y_adj) ** t)
        weighted_pv_sum += pv_cf_t * t 
        total_pv += pv_cf_t 

    pv_face = face / ((1 + y_adj) ** n)
    total_pv += pv_face 
    weighted_pv_sum += pv_face * n 

    bondDuration = weighted_pv_sum / total_pv

    return(bondDuration)
