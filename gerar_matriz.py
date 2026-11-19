"""Gera MATRIZ_ROTAS.md a partir de rotas.txt."""
from pathlib import Path


def gerar():
    linhas = Path("rotas.txt").read_text(encoding="utf-8").splitlines()
    rotas = [linha.split() for linha in linhas if linha.strip()]
    publicas = [r for r in rotas if r[2] == "PUBLICA"]

    saida = ["# Matriz de rotas", ""]
    saida.append(f"Total: {len(rotas)}. Públicas: {len(publicas)}.")
    saida.append("")
    saida.append("| Método | Rota | Proteção |")
    saida.append("|---|---|---|")
    for metodo, rota, protecao in sorted(rotas, key=lambda r: (r[1], r[0])):
        saida.append(f"| {metodo} | `{rota}` | {protecao} |")
    return "\n".join(saida) + "\n"


if __name__ == "__main__":
    Path("MATRIZ_ROTAS.md").write_text(gerar(), encoding="utf-8")
    print("MATRIZ_ROTAS.md gerada")
