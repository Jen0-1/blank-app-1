import streamlit as st

# Título
st.title("🌱 ¡Bienvenido al Cuidado del Planeta!")

# Mensaje de bienvenida
st.write("""
    ¡Hola! Gracias por unirte al movimiento de cuidado del planeta. 💚
    En esta aplicación te ayudaremos a realizar pequeños cambios que, sumados, pueden tener un gran impacto en nuestro entorno.
    Cada decisión cuenta, desde reducir el uso de plástico hasta ahorrar agua y energía. 🌍
""")

# Opciones para aprender más
st.write("### ¿Sabías que...? 🤔")
st.write("""
    - Si cada persona redujera su consumo de plástico en un 50%, se evitarían miles de toneladas de basura plástica en el océano.
    - Reciclar una sola botella de plástico puede ahorrar suficiente energía para encender una bombilla durante 3 horas.
    - Si ahorráramos agua en nuestras casas, podríamos ayudar a evitar sequías y proteger nuestros ecosistemas acuáticos.
""")

# Interacción: Selección de acciones para ayudar al planeta
st.write("### ¿Qué acciones te gustaría comenzar a tomar para ayudar al planeta? 🌍")

acciones = st.multiselect(
    "Selecciona las acciones que te gustaría implementar:",
    ["Reducir el uso de plástico",
     "Reutilizar productos",
     "Reciclar correctamente",
     "Ahorrar agua",
     "Usar energías renovables",
     "Plantar árboles",
     "Comer productos locales y de temporada"]
)

# Mostrar las acciones seleccionadas por el usuario
if acciones:
    st.write("### ¡Gracias por tomar estas acciones! 🌱")
    st.write("Estas son las acciones que seleccionaste para ayudar al planeta:")
    for accion in acciones:
        st.write(f"- {accion}")
    st.write("""
        Recuerda que cada pequeña acción puede marcar una gran diferencia. ¡Tú estás contribuyendo a un planeta más limpio y saludable! 💧🌳
    """)

    # Consejos adicionales según las acciones seleccionadas
    st.write("### Consejos para llevar a cabo tus acciones:")
    if "Reducir el uso de plástico" in acciones:
        st.write("- Usa bolsas reutilizables, evita plásticos de un solo uso y opta por productos empaquetados sin plástico.")
    if "Reutilizar productos" in acciones:
        st.write("- Reutiliza botellas, frascos y otros artículos en lugar de desecharlos.")
    if "Reciclar correctamente" in acciones:
        st.write("- Separa los materiales reciclables como vidrio, papel, plástico y metal de la basura común.")
    if "Ahorrar agua" in acciones:
        st.write("- Instala dispositivos de ahorro de agua como regaderas eficientes y no dejes el grifo abierto innecesariamente.")
    if "Usar energías renovables" in acciones:
        st.write("- Si es posible, cambia a energía solar o busca opciones de energía limpia.")
    if "Plantar árboles" in acciones:
        st.write("- Participa en campañas locales de reforestación o planta árboles en tu propio jardín.")
    if "Comer productos locales y de temporada" in acciones:
        st.write("- Apoya a los productores locales y elige frutas y verduras de temporada para reducir la huella de carbono.")

else:
    st.write("Selecciona alguna acción para saber cómo puedes empezar a contribuir al cuidado del planeta.")
    
# Botón interactivo para dar más información
if st.button("¡Estoy listo para empezar! 🌍"):
    st.write("¡Genial! Recuerda que pequeños cambios pueden generar un gran impacto. 🌱")
    st.write("Gracias por tomar la iniciativa de cuidar nuestro planeta. ¡Juntos podemos marcar la diferencia!")

# Mensaje final
st.write("""
    **Recuerda**: Cada acción cuenta, por pequeña que sea. ¡Cuidemos juntos el futuro de nuestro planeta! 💧🌳
""")