import re 


text = "esta es una  oracion larga para pode probar si puedo capturar una palabra"

comando = re.search( r"oracion", text)
print(comando)
print(comando.group(0))
