

def getBondPrice(y, face, couponRate, m, ppy=1):
    cf = couponRate * face / ppy
    n = m * ppy
    y_adj = y / ppy

    pvcf = 0
    for t in range(1, n+1):
        pvcf += cf / ((1 + y_adj) ** t)

    pv_face = face / ((1 + y_adj) ** n)

    bondPrice = pvcf + pv_face

    return(bondPrice)
