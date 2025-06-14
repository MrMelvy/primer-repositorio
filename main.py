diccionario = {
  "lol": "una respuesta a algo gracioso",
  "cringe": "pena ajena",
  "rofl": "una respuesta a una broma",
  "sheesh": "ligera desabrobacion",
  "creepy": "algo turbio",
  "camellar": "trabajar",
  "oe": "oye",
  "wow": "sorprendido",
  "parry": "bloqueo perfecto en videojuego",
  "bot": "alguien que no sabe jugar",
  "tryhard": "alguien que sabe jugar",
  "spoiler": "te adelanta una pelicula",
  "banear": "expulsar a una persona del servidor"
  
}
pregunta = input("escribe una palabra que no entiendas")
if pregunta in diccionario.keys():
  print(diccionario[pregunta])
else:
  print("esa palabra no existe")
