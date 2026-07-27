import ollama
from prompt import PROMPT_BASE
from ejercicios import *

# ==========================================
# EJERCICIOS DISPONIBLES
# ==========================================

ejercicios_disponibles = f"""
PECHO:
{chr(10).join("- " + e for e in PECHO)}

ESPALDA:
{chr(10).join("- " + e for e in ESPALDA)}

PIERNA:
{chr(10).join("- " + e for e in PIERNA)}

HOMBROS:
{chr(10).join("- " + e for e in HOMBROS)}

BÍCEPS:
{chr(10).join("- " + e for e in BICEPS)}

TRÍCEPS:
{chr(10).join("- " + e for e in TRICEPS)}
"""

# ==========================================
# DIVISIÓN SEMANAL
# ==========================================

def obtener_division(dias):

    if dias == 2:
        return """
Día 1 - Full Body
Día 2 - Full Body
"""

    elif dias == 3:
        return """
Día 1 - Push
Día 2 - Pull
Día 3 - Pierna
"""

    elif dias == 4:
        return """
Día 1 - Pecho + Tríceps
Día 2 - Espalda + Bíceps
Día 3 - Pierna
Día 4 - Hombros + Abdomen
"""

    elif dias == 5:
        return """
Día 1 - Pecho
Día 2 - Espalda
Día 3 - Pierna
Día 4 - Hombros
Día 5 - Brazos
"""

    else:
        return """
Día 1 - Push
Día 2 - Pull
Día 3 - Pierna
Día 4 - Push
Día 5 - Pull
Día 6 - Pierna
"""

# ==========================================
# IA
# ==========================================

def generar_rutina(objetivo, nivel, dias, tiempo):

    division = obtener_division(dias)

    respuesta = ollama.chat(
        model="gemma3:12b",
        messages=[
            {
                "role": "user",
                "content": f"""
{PROMPT_BASE}

# DIVISIÓN OBLIGATORIA

{division}

La rutina DEBE seguir exactamente esta división.

No cambies los grupos musculares.

# EJERCICIOS DISPONIBLES

{ejercicios_disponibles}

Utiliza únicamente ejercicios de estas listas.

No pongas ejercicios de un grupo muscular dentro de otro.

# DATOS DEL USUARIO

Objetivo: {objetivo}
Nivel: {nivel}
Días por semana: {dias}
Tiempo por sesión: {tiempo}
""",
            }
        ],
     options={
        "think": False,
        "num_ctx": 8192,
        "num_predict": 500,
        }
    )

    return respuesta["message"]["content"]