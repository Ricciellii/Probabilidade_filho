while True:
 
#Instruções 

 print('Para os tipos de cabelo, digite: Crespo, Ondulado ou liso')
 print('Para os tipos de olhos, digite: Castanho, Verde ou Azul')
 print('Para as cores de cabelo, digite: Preto, Loiro, Ruivo,')

#dados

 cabelo_pai = input(str('Qual é o tipo do cabelo do pai? ')).lower()
 cabelo_mae = input(str('Qual é o tipo de cabelo da mãe? ')).lower()
 cc_pai = input(str ('Qual a cor do cabelo do pai: ')).lower
 cc_mae = input(str('Qual a cor do cabelo da mão? ')).lower
 mae = input(str("Qual é a cor dos olhos da mãe? ")).lower()
 pai = input(str("Qual é a cor dos olhos do pai? ")).lower()
 ordem = input('Voce deseja que o sobrenome da mãe sejam os ultimos? (digite, sim ou não)').lower()

#nome

 if ordem == 'sim':
  nome_completo = nome_f +' '+ nome_p +' '+ nome_m +' '
  nome_f = input(str('Digite o primeiro nome da filha(o): ')).lower()
  nome_p = input(str('Digite o sobrenome do pai: ')).lower()
  nome_m = input(str('Digite o sobrenome da mãe: ')).lower()

 else:
  nome_f = input(str('Digite o primeiro nome da filha(o): ')).lower()
  nome_m = input(str('Digite o sobrenome da mãe: ')).lower()
  nome_p = input(str('Digite o sobrenome do pai: ')).lower()
  nome_completo = nome_f +' '+ nome_m +' '+ nome_p +' '

#cabelo

 if cabelo_pai == "crespo" and cabelo_mae == "crespo".lower():
    print("As probabilidades do cabelo da sua filha(o) são: 100% crespo.")

 elif cabelo_pai == "crespo" and cabelo_mae == "liso" or cabelo_pai == "liso" and cabelo_mae == "crespo".lower():
    print("As probabilidades do cabelo da sua filha(o) são: 50% Crespo, 40% Liso, 10% Misturado.")

 elif cabelo_pai == "crespo" and cabelo_mae == "cacheado" or cabelo_pai == "cacheado" and cabelo_mae == "crespo".lower(): 
    print("As probabilidades do cabelo da sua filha(o) são: 50% Crespo, 40% cacheado, 10% Misturado.")

 elif cabelo_pai == "crespo" and cabelo_mae == "ondulado" or cabelo_pai == "ondulado" and cabelo_mae == "crespo".lower():
    print("As probabilidades do cabelo da sua filha(o) são: 50% Crespo, 40% ondulado, 10% Misturado.")

 elif cabelo_pai == "cacheado" and cabelo_mae == "cacheado".lower():
    print("As probabilidades do cabelo da sua filha(o) são: 100% ondulado.")

 elif cabelo_pai == "cacheado" and cabelo_mae == "liso" or cabelo_pai == "liso" and cabelo_mae == "cacheado".lower():
    print("As probabilidades do cabelo da sua filha(o) são: 50% Cacheado, 40% Liso, 10% Misturado.")

 elif cabelo_pai == "cacheado" and cabelo_mae == "ondulado" or cabelo_pai == "ondulado" and cabelo_mae == "cacheado".lower(): 
    print("As probabilidades do cabelo da sua filha(o) são: 50% Cacheado, 40% ondulado, 10% Misturado.")

 elif cabelo_pai == "liso" and cabelo_mae == "liso".lower():
    print("As probabilidades do cabelo da sua filha(o) são: 100% liso.")

 elif cabelo_pai == "liso" and cabelo_mae == "ondulado" or cabelo_pai == "ondulado" and cabelo_mae == "liso".lower(): 
    print("As probabilidades do cabelo da sua filha(o) são: 50% ondulados, 40% liso, 10% Misturado.")

#cor do cabelo

 if cc_pai == "preto" and cc_mae == "preto".lower():
    print("Seu filho tera cabelos castanhos.")

 elif cc_pai == "preto" and cc_mae == "loiro" or cc_pai == "loiro" and cc_mae == "preto".lower():
    print("as probabilidades da cor do cabelo da sua filha(o) são: 60% castanho, 40%.")

 elif cc_pai == "preto" and cc_mae == "ruivo" or cc_pai == "ruivo" and cc_mae == "preto".lower(): 
    print("As probabilidades dos olhos são: 60% Azul, 40% castanho (lembrando que a cor do cabelo do pai prevalece).")

 elif cc_pai == "verde" and cc_mae == "verde".lower():
   print("Seu filho provavelmente terá olhos verdes.")

 elif cc_pai == "verde" and cc_mae == "castanho" or cc_pai == "castanho" and cc_mae == "verde".lower():
    print("As probabilidades dos olhos são: 50% marron, 50% Verde (lembrando que a cor dos olhos da mãe prevalece).")

 elif cc_pai == "castanho" and cc_mae == "castanho".lower():
    print("Seu filho provavelmente terá olhos castanhos.")

#cor dos olhos

 if pai == "azul" and mae == "azul".lower():
    print("Seu filho provavelmente terá olhos azuis.")

 elif pai == "azul" and mae == "verde" or pai == "verde" and mae == "azul".lower():
    print("As probabilidades dos olhos são: 50% Azul, 50% Verde (lembrando que a cor dos olhos da mãe prevalece).")

 elif pai == "azul" and mae == "castanho" or pai == "castanho" and mae == "azul".lower(): 
    print("As probabilidades dos olhos são: 50% Azul, 50% Marron (lembrando que a cor dos olhos da mãe prevalece).")

 elif pai == "verde" and mae == "verde".lower():
   print("Seu filho provavelmente terá olhos verdes.")

 elif pai == "verde" and mae == "castanho" or pai == "castanho" and mae == "verde".lower():
    print("As probabilidades dos olhos são: 50% marron, 50% Verde (lembrando que a cor dos olhos da mãe prevalece).")

 elif pai == "castanho" and mae == "castanho".lower():
    print("Seu filho provavelmente terá olhos castanhos.")

 print ('O nome da filha(o) sera: ', nome_completo)
    
 sair = input('Calcular outra possibilidade?(sim ou não) ').lower().startswith('s')
 if sair is True:
        continue
 break