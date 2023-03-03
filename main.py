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

  while True:
    t1 = random.randint(5, 30)
    t2 = random.randint(5, 30)
    ep = random.randint(5, 30)

    G1 = mt1 * t1
    G2 = mt2 * t2
    Gep = mep * ep

    T1 = t2 + ep
    T2 = t1 + ep
    Tep = t1 + t2

    if G1 > T1 and G2 > T2 and Gep > Tep:
      break

  L1 = mt1 * t1 - (t2 + ep)
  L2 = mt2 * t2 - (t1 + ep)
  Lep = mep * ep - (t1 + t2)

  print("Time 1!")
  print("Valor Ganho Total: {}\n".format(G1))
  print("t1: {}".format(t1))
  print("t2: {}".format(t2))
  print("ep: {}".format(ep))
  print("L: {}".format(L1))

  print("Time 2!")
  print("Valor Ganho Total: {}\n".format(G2))
  print("t1: {}".format(t1))
  print("t2: {}".format(t2))
  print("ep: {}".format(ep))
  print("L: {}".format(L2))

  print("Empate!")
  print("Valor Ganho Total: {}\n".format(Gep))
  print("t1: {}".format(t1))
  print("t2: {}".format(t2))
  print("ep: {}".format(ep))
  print("L: {}".format(Lep))

  opcao = int(input("\n\nDe novo? (1-Sim | 2-Nao)"))

  if opcao == 1:
    continue
  else:
    break
