

def getBondPrice_Z(face, couponRate, times, yc):
    cf = couponRate * face

    bondPrice = 0
    for t, y in zip(times, yc):
        pvcf = cf / ((1 + y) ** t)
        bondPrice += pvcf
    pv_face = face / ((1 + yc[-1]) ** times[-1])
    bondPrice += pv_face

    return(bondPrice)
