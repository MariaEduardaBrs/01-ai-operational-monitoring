import runpy
from pathlib import Path

from gerar_matriz import gerar


def test_gerar_conta_total_e_publicas(tmp_path, monkeypatch):
    (tmp_path / "rotas.txt").write_text(
        "GET /b PUBLICA\nPOST /a LOGIN\n", encoding="utf-8"
    )
    monkeypatch.chdir(tmp_path)

    resultado = gerar()

    assert "Total: 2. Públicas: 1." in resultado
    assert resultado.index("/a") < resultado.index("/b")


def test_executa_como_script(tmp_path, monkeypatch):
    (tmp_path / "rotas.txt").write_text("GET /a PUBLICA\n", encoding="utf-8")
    monkeypatch.chdir(tmp_path)
    script = Path(__file__).parent / "gerar_matriz.py"

    runpy.run_path(str(script), run_name="__main__")

    assert (tmp_path / "MATRIZ_ROTAS.md").exists()
