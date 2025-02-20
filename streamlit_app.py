import streamlit as st

# Título
st.title("🌍 Calculadora de Huella de Carbono")

# Introducción
st.write("""
    Bienvenido a la calculadora de huella de carbono. Con esta herramienta puedes estimar tu huella de carbono diaria
    según diferentes actividades que realizas en tu vida cotidiana, como el transporte y el uso de energía.
    Al final te mostraremos tu huella total y algunas recomendaciones para reducirla.
""")

# Entrada de transporte (km recorridos al día en coche, bus, bicicleta)
km_auto = st.number_input("¿Cuántos kilómetros recorres al día en automóvil?", min_value=0.0, step=1.0)
km_bus = st.number_input("¿Cuántos kilómetros recorres al día en bus o transporte público?", min_value=0.0, step=1.0)
km_bici = st.number_input("¿Cuántos kilómetros recorres al día en bicicleta?", min_value=0.0, step=1.0)

# Entrada de consumo energético en el hogar (kWh de electricidad al día)
energia_hogar = st.number_input("¿Cuántos kWh de electricidad consumes al día en tu hogar?", min_value=0.0, step=0.1)

# Factor de emisión para cada actividad (en kg de CO2 por unidad)
emision_auto = 0.24  # kg CO2 por km en automóvil
emision_bus = 0.05   # kg CO2 por km en bus
emision_bici = 0.0   # kg CO2 por km en bicicleta (cero emisiones)
emision_energia = 0.92  # kg CO2 por kWh de electricidad

# Cálculo de huella de carbono por cada actividad
huella_auto = km_auto * emision_auto
huella_bus = km_bus * emision_bus
huella_bici = km_bici * emision_bici
huella_energia = energia_hogar * emision_energia

# Huella total
huella_total = huella_auto + huella_bus + huella_bici + huella_energia

# Mostrar resultados
if st.button("Calcular Huella de Carbono"):
    st.write(f"### Tu huella de carbono diaria es:")
    st.write(f"- Transporte en automóvil: {huella_auto:.2f} kg CO2")
    st.write(f"- Transporte en bus: {huella_bus:.2f} kg CO2")
    st.write(f"- Transporte en bicicleta: {huella_bici:.2f} kg CO2")
    st.write(f"- Consumo de electricidad en el hogar: {huella_energia:.2f} kg CO2")
    st.write(f"**Total de huella de carbono diaria**: {huella_total:.2f} kg CO2")

    # Recomendaciones para reducir la huella de carbono
    st.write("### ¿Cómo puedes reducir tu huella de carbono?")
    if huella_auto > 0:
        st.write("- Opta por utilizar transporte público o compartir coche con otras personas.")
    if huella_bus > 0:
        st.write("- Intenta usar transporte público más ecológico, como autobuses eléctricos.")
    if huella_bici > 0:
        st.write("- ¡Genial! Andar en bicicleta es una opción sin emisiones.")
    if huella_energia > 0:
        st.write("- Considera instalar paneles solares o reducir el consumo eléctrico utilizando bombillas LED y electrodomésticos eficientes.")
    
    st.write("Recuerda que cada pequeña acción ayuda a reducir el impacto ambiental y a cuidar nuestro planeta.")
