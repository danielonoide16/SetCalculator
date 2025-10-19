import re

def is_valid_format(s):
    #pattern = r'^[A-Za-z0-9]+(,[A-Za-z0-9]+)*$' #sin aceptar espacios
    pattern = r'^[A-Za-z0-9]+(\s*,\s*[A-Za-z0-9]+)*$' #verifica el formato texto,texto, texto 
    return bool(re.match(pattern, s))

def is_valid_format_tuple(s):
    pattern = r'^\(([a-zA-Z0-9]+),([0-9]+),([a-zA-Z0-9]+)\)(,\(([a-zA-Z0-9]+),([0-9]+),([a-zA-Z0-9]+)\))*$'
    return bool(re.match(pattern, s))

def text_to_list(string: str):
    return [x.strip() for x in string.split(',') if x.strip()] #lista de elementos

def text_to_tuples(string: str):
    pattern = r'\(\s*([a-zA-Z0-9]+)\s*,\s*([0-9]+)\s*,\s*([a-zA-Z0-9]+)\s*\)'
    return re.findall(pattern, string)

#(a,1,b)