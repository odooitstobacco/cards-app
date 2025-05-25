import streamlit as st
import random


st.title("🎈 Juego de Memoria ")
st.write("Demostrar el Manejo de Secciones y Botones")

# Inicializar el estado si no existe
if "mostrar" not in st.session_state:
    st.session_state.numeros = random.sample(range(1, 10),5)
    st.session_state.objetivo = random.choice(st.session_state.numeros)
    st.session_state.mostrar = True
    st.session_state.errores = 0
    st.session_state.encontrado = False
    st.session_state.resultado = ""
    st.session_state.btn_jugar = True


# Mostrar la sección si el estado lo indica
if st.session_state.mostrar:
    st.subheader("🕒 Memoriza los números:")
    # Botón para alternar visibilidad
    cols = st.columns(5)
    for i, numero in enumerate(st.session_state.numeros):
      with cols[i % 5]:
         st.button(f"🎴 {numero}", disabled=True)
    if st.button("Ocultar Números"):
        st.session_state.mostrar = not st.session_state.mostrar
        st.rerun()
else:
    st.subheader(f"🔍 Encuentra el número: **{st.session_state.objetivo}**")
    cols = st.columns(5)
    for i, numero in enumerate(st.session_state.numeros):
        with cols[i % 5]:
            if st.button("🎴", key=f"btn_{numero}"):
                print(numero, st.session_state.objetivo, numero == st.session_state.objetivo)
                if numero == st.session_state.objetivo:
                    st.session_state.resultado = f"✅ ¡Correcto! "
                    st.session_state.encontrado = True
                else:
                    st.session_state.errores += 1
                    st.session_state.resultado = f"❌ Incorrecto [Error # {st.session_state.errores}] Era {st.session_state.objetivo}"

# Mostrar resultado
if st.session_state.resultado:
   st.markdown(f"### {st.session_state.resultado}")
   st.toast(f"🔁 Errores cometidos: **{st.session_state.errores}**")

# Mostrar errores si ya encontró el número
if st.session_state.encontrado:
   st.warning(f"🔁 Errores cometidos: **{st.session_state.errores}**")
   st.session_state.btn_jugar = True
   # Botón para reiniciar
   if st.session_state.btn_jugar:
       if st.button("🔄 Jugar de nuevo"):
           st.session_state.numeros = random.sample(range(1, 10), 5)
           st.session_state.objetivo = random.choice(st.session_state.numeros)
           st.session_state.mostrar = True
           st.session_state.resultado = ""
           st.session_state.errores = 0
           st.session_state.encontrado = False
           st.session_state.btn_jugar = False
           st.rerun() # <- Esto fuerza la recarga inmediata   