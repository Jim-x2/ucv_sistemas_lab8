
from agente_ucv.agent import explicar_concepto


def test_explicar_api():
    resultado = explicar_concepto("api")
    assert resultado["status"] == "success"
    assert "API" in resultado["explicacion"]


def test_explicar_algoritmo():
    resultado = explicar_concepto("algoritmo")
    assert resultado["status"] == "success"


def test_explicar_base_datos():
    resultado = explicar_concepto("base de datos")
    assert resultado["status"] == "success"


def test_concepto_no_registrado():
    resultado = explicar_concepto("redes")
    assert resultado["status"] == "not_found"


def test_mayusculas_y_espacios():
    resultado = explicar_concepto("  API  ")
    assert resultado["status"] == "success"
