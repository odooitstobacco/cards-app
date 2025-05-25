dataInicial = {
  1: 1,  
  2: 2,  
  3: 3,  
  4: 4,  
  5: 5,  
  6: 6,  
  7: 7,  
  8: 8,  
  9: 9,  
  10: 10, 
}

dataBasico = {
  1: "Se va armar 🔥",  
  2: "Estoy living 😍",  
  3: "Modo diablo 😈",  
  4: "No estoy sad 🌑",
  5: "Se tenía que decir 💬",
  6: "Con flow 🚀",
  7: "Literal yo 😅",
  8: "Esto es cine 🎬",
  9: "Te amo pero ... 😬",
  10: "Me representa 😂"

}

dataAvanzado = {
  1: "😀",  # Cara feliz
  2: "🐶",  # Perro
  3: "🍎",  # Manzana
  4: "🚗",  # Auto
  5: "🌟",  # Estrella
  6: "🎈",  # Globo
  7: "📚",  # Libros
  8: "🎵",  # Nota musical
  9: "🌍",  # Globo terráqueo
  10: "⚽", # Balón de fútbol
}


def obtenerNivelJuego(nivel):
  if nivel == 1:
     return dataInicial
  elif nivel == 2:
     return dataBasico
  elif nivel == 3:
     return dataAvanzado
  else:
     return None
