#Se preguntan las notas
nota1=float(input("Escriba su nota: "))
nota2=float(input("Escriba su segunda nota: "))
nota3=float(input("Escriba su tercera nota: "))

#Cálculo del promedio
prome=(nota1+nota2+nota3) /3

#Se dice si pasa con el promedio o no
if prome >= 70:
    print(f"Usted ha sido aprobado, su nota es de {prome}")
else:
    print(f"Usted ha sido reprobado, su nota es de {prome}")