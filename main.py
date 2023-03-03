import random

t1 = 0
t2 = 0
ep = 0
L1 = 0
L2 = 0
Lep = 0

while True:
  mt1 = float(input("Insira o valor do multiplicador do Time 1: "))
  mt2 = float(input("Insira o valor do multiplicador do Time 2: "))
  mep = float(input("Insira o valor do multiplicador do empate: "))
  min = int(input("Insira o valor minimo a ser apostado: "))
  max = int(input("Insira o valor maximo a ser apostado: "))

  while True:
    t1 = random.randint(min, max)
    t2 = random.randint(min, max)
    ep = random.randint(min, max)

    G1 = mt1 * t1
    G2 = mt2 * t2
    Gep = mep * ep
    
   # deBugg
   # print("t1: {}".format(t1))
   # print("t2: {}".format(t2))
   # print("ep: {}".format(ep))

    T1 = t2 + ep
    T2 = t1 + ep
    Tep = t1 + t2

    if G1 > T1 and G2 > T2 and Gep > Tep:
      break

  L1 = mt1 * t1 - (t2 + ep)
  L2 = mt2 * t2 - (t1 + ep)
  Lep = mep * ep - (t1 + t2)

  print("\n\n  Valores a apostar:")
  print("Vitória do Time 1: {}".format(t1))
  print("Vitória do Time 2: {}".format(t2))
  print("Empate dos times: {}\n".format(ep))
  
  print("  Ganhos caso:")
  print("Vitória do Time 1: {}".format(G1))
  print("Vitória do Time 2: {}".format(G2))
  print("Empate dos times: {}\n".format(Gep))
  
  print("  Lucros caso:")
  print("Vitória do Time 1: {}".format(L1))
  print("Vitória do Time 2: {}".format(L2))
  print("Empate dos times: {}\n".format(Lep))


  opcao = int(input("\n\nDe novo? (1-Sim | 2-Nao)"))

  if opcao == 1:
    continue
  else:
    break
