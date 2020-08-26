# Strings Parte 02

texto = "Curso de Python"
palavra = "python"

resposta = palavra.upper() in texto.upper()
print(resposta)

resposta = palavra not in texto
print(resposta)

curso = "Python"
canal = "CFB Cursos"
resultado = curso + " do canal " + canal
print(resultado)

dia = 26
mes = "Agosto"
ano = 2020
cidade = "Belo Horizonte"
dataResposta = "{}, {} de {} de {}\n \"{}\""    
nome = "Daniel Paiva"

print(dataResposta.format(cidade, dia, mes, ano, nome))

# \' \"" \n \r \t \b