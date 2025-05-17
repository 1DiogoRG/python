votos = {"A": 0, "B": 0, "C": 0}
while True:
    voto = input("Vote [A/B/C] ou FIM: ").upper()
    if voto == "FIM":
        break
    if voto in votos:
        votos[voto] += 1

total = sum(votos.values())
for candidato, qtd in votos.items():
    print(f"{candidato}: {qtd} voto - {qtd / total:.0%}")
