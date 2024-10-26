'''
Calculer IMC
IMC = poids(kg)/taille2 (m)

'''

poids = float(input('Saisir votre poids : '))

taille =  float(input('Saisir votre taille : '))

imc = poids / taille ** 2

print(f'Votre IMC :{imc}')

if imc >= 40.4 :
    print('Extrêmement élevé')

if imc < 18.5 :
    print('Risque de développerdes problèmes de santé')