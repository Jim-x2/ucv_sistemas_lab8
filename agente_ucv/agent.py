
from google.adk.agents.llm_agent import Agent


def explicar_concepto(concepto: str) -> dict:
    conceptos = {
        "api": "Una API permite la comunicación entre sistemas.",
        "algoritmo": "Un algoritmo es una secuencia de pasos.",
        "base de datos": "Una base de datos almacena información.",
        "inteligencia artificial": "La IA permite que las máquinas realicen tareas que requieren inteligencia.",
        "python": "Python es un lenguaje de programación."
    }

    concepto = concepto.lower().strip()

    if concepto in conceptos:
        return {
            "status": "success",
            "explicacion": conceptos[concepto]
        }

    return {
        "status": "not_found",
        "explicacion": "Concepto no registrado."
    }


root_agent = Agent(
    model="gemini-3.5-flash-lite",
    name="agente_ucv",
    description="Agente académico UCV",
    instruction="""
    Eres un asistente académico.
    Responde en español.
    Usa lenguaje simple.
    Ayuda a los estudiantes a comprender conceptos técnicos.
    """,
    tools=[explicar_concepto],
)
