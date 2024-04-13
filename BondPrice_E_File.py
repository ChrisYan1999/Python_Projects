

def getBondPrice_E(face, couponRate, m, yc):
    cf = (couponRate * face)
    
    bondPrice = 0
    for t, y in enumerate(yc, start=1):
        pvcf = cf / ((1 + y) ** t)
        bondPrice += pvcf
    pv_face = face / ((1 + yc[-1]) ** m)

    bondPrice += pv_face

    return(bondPrice)
