import re

def is_valid_format(s):
    #pattern = r'^[A-Za-z0-9]+(,[A-Za-z0-9]+)*$' #sin aceptar espacios

    
    pattern = r'^\s*[A-Za-z0-9]+(\s*,\s*[A-Za-z0-9]+)*\s*$' #verifica el formato Str,Str, Str...  Aceptando espacios
    return bool(re.match(pattern, s))

def is_valid_format_tuple(s):
    #pattern = r'^\([a-zA-Z0-9]+,[0-9]+,[a-zA-Z0-9]+\)(,\([a-zA-Z0-9]+,[0-9]+,[a-zA-Z0-9]+\))*$' #formato (Str,Int,Str),(Str,Int,Str)... #formato (Str,Int,Str),(Str,Int,Str)... No acepta espacios

    pattern = r'^\s*\(\s*[a-zA-Z0-9]+\s*,\s*[0-9]+\s*,\s*[a-zA-Z0-9]+\s*\)(\s*,\s*\(\s*[a-zA-Z0-9]+\s*,\s*[0-9]+\s*,\s*[a-zA-Z0-9]+\s*\))*\s*$' #formato (Str,Int,Str), (Str,Int,Str)...  Acepta espacios
    return bool(re.match(pattern, s))

def text_to_list(string: str):
    """
    convierte el texto en una lista de strings, usando la , como separador
    """
    return [x.strip() for x in string.split(',') if x.strip()] 

def text_to_tuples(string: str):
    """
    convierte el texto en una lista de tuplas, usando la , como separador
    """
    pattern = r'\(\s*([a-zA-Z0-9]+)\s*,\s*([0-9]+)\s*,\s*([a-zA-Z0-9]+)\s*\)'
    return re.findall(pattern, string)
