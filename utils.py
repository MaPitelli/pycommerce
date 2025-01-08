import re

def validar_email(email):
    """
    Valida un correo electrónico usando una expresión regular.

    Args:
        email (str): Correo electrónico a validar.

    Returns:
        bool: True si es válido, False si no lo es.
    """
    patron = r"[^@]+@[^@]+\.[^@]+"
    return re.match(patron, email) is not None
