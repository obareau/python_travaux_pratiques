def cube(n):
    "mets au cube"
    return n**3


def volumeSphere(r):
    "calcule le volume de la sphére"
    return 4 * 3.1416 * cube(r) / 3


r = input('Entrez la valeur du rayon : ')
radius_int = int(r)
print ('Le volume de cette sphère vaut', volumeSphere(radius_int))
