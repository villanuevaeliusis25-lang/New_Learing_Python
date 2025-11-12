import random

# --- SECCIÓN 1: CONFIGURACIÓN Y MODELO DE DATOS ---

NUM_USUARIOS = 100
COMPRAS_POR_USUARIO = 6 
CANTIDAD_DESEADA_PROMEDIO = 1000  # Unidades a comprar
DINERO_PERDIDO = 50.0  # Costo de un "Viaje en Vano" o disputa (Bs.)

# BASE DE DATOS DE MAYORISTAS (Simulación)
data_mayoristas = [
    {
        "id": 1, "nombre": "Mayorista A (Riesgo)",
        "precio": 4.50, "costo_logistica": 10.0,
        "garantia_digital": 0.70, # 30% de riesgo de fallo
        "descuento": 0.0, "plazo_credito_dias": 7
    },
    {
        "id": 2, "nombre": "Mayorista B (Recomendado)",
        "precio": 4.60, "costo_logistica": 0.0, # Entrega Gratis
        "garantia_digital": 0.98, # 2% de riesgo de fallo
        "descuento": 0.03, "plazo_credito_dias": 60
    },
    {
        "id": 3, "nombre": "Mayorista C (Descartado)",
        "precio": 4.75, "costo_logistica": 30.0,
        "garantia_digital": 0.90,
        "descuento": 0.01, "plazo_credito_dias": 30
    }
]

# --- SECCIÓN 2: LÓGICA DEL BNT (Algoritmo de Valoración) ---

def calcular_bnt_y_cot(mayorista, cantidad, credibilidad_comprador):
    """Calcula el Costo Neto Real y el Puntaje BNT para un mayorista."""
    
    # 1. Costo Total de Oferta (COT = Precio + Logística)
    costo_producto = mayorista["precio"] * cantidad
    costo_total_oferta = costo_producto + mayorista["costo_logistica"]

    # 2. Ahorro Financiero (Bonificación por Credibilidad)
    ahorro_financiero = 0.0
    aprobacion_credito = 0
    # Condición de Aprobación: Alta Credibilidad (>= 80) Y el mayorista ofrece plazo extendido (> 30 días)
    if credibilidad_comprador >= 80 and mayorista["plazo_credito_dias"] > 30:
        ahorro_financiero = costo_producto * mayorista["descuento"]
        aprobacion_credito = 1
        
    # 3. Costo de Riesgo (Penalización por Baja Garantía Digital)
    probabilidad_fallo = 1.0 - mayorista["garantia_digital"]
    costo_riesgo = probabilidad_fallo * DINERO_PERDIDO
    
    # 4. Cálculo del Costo Neto Real y el Puntaje BNT
    # Costo Neto Real = COT - Ahorro Financiero + Costo de Riesgo
    costo_neto_real = costo_total_oferta - ahorro_financiero + costo_riesgo
    
    # El menor costo neto real da el mayor puntaje BNT
    bnt_puntaje = 10000 / costo_neto_real 

    return {
        "id": mayorista["id"],
        "nombre": mayorista["nombre"],
        "costo_neto_real": costo_neto_real,
        "bnt_puntaje": bnt_puntaje,
        "ahorro_financiero": ahorro_financiero,
        "aprobacion_credito": aprobacion_credito,
        "riesgo_fallo": probabilidad_fallo
    }

# --- SECCIÓN 3: FUNCIÓN DE SIMULACIÓN DE MOVIMIENTOS ---

def simular_movimientos(escenario="con_app"):
    """
    Simula las decisiones de compra de 100 usuarios en 600 transacciones, 
    usando lógica ponderada (Sin App) o adopción progresiva (Con App).
    """
    
    # Inicialización de KPIs
    viajes_en_vano = 0
    credito_aprobado_count = 0
    ahorro_financiero_total = 0.0
    conteo_mayoristas = {1: 0, 2: 0, 3: 0} 
    
    # Generación de Usuarios (con Credibilidad y contador de éxito)
    usuarios = []
    for i in range(NUM_USUARIOS):
        # 60% de probabilidad de tener Credibilidad Alta (>= 80)
        credibilidad = random.randint(80, 95) if random.random() < 0.6 else random.randint(60, 79)
        usuarios.append({"id": i, "credibilidad": credibilidad, "compras_exitosas": 0})

    # --- SIMULACIÓN DE TRANSACCIONES ---
    total_transacciones = NUM_USUARIOS * COMPRAS_POR_USUARIO

    for i in range(total_transacciones):
        usuario = random.choice(usuarios)
        
        # Calcular el valor BNT de cada oferta para este usuario
        ofertas_calculadas = [
            calcular_bnt_y_cot(m, CANTIDAD_DESEADA_PROMEDIO, usuario["credibilidad"]) 
            for m in data_mayoristas
        ]

        if escenario == "sin_app":
            # LÓGICA SIN APP: Selección Ponderada (60% al más barato/riesgoso, ID 1)
            mayoristas_ids = [1, 2, 3]
            pesos_seleccion = [0.60, 0.20, 0.20] 
            
            id_elegido = random.choices(mayoristas_ids, weights=pesos_seleccion, k=1)[0]
            oferta_elegida = next(o for o in ofertas_calculadas if o['id'] == id_elegido)
            
            # Registrar el fallo
            if random.random() < oferta_elegida["riesgo_fallo"]:
                viajes_en_vano += 1
                
        elif escenario == "con_app":
            # LÓGICA CON APP: Adopción Progresiva de Confianza en el BNT
            
            sugerencia_bnt = max(ofertas_calculadas, key=lambda x: x["bnt_puntaje"])
            opcion_tradicional = next(o for o in ofertas_calculadas if o['id'] == 1) 

            # Probabilidad de Confianza en la App (Sube 5% por cada éxito)
            prob_confianza_app = min(0.95, 0.50 + usuario["compras_exitosas"] * 0.05)
            
            if random.random() < prob_confianza_app:
                oferta_elegida = sugerencia_bnt
            else:
                oferta_elegida = opcion_tradicional
            
            # Registrar el éxito o el fallo para la confianza
            if random.random() >= oferta_elegida["riesgo_fallo"]:
                 usuario["compras_exitosas"] += 1
            else:
                 viajes_en_vano += 1 

        # **REGISTRO FINAL DE KPIS Y MOVIMIENTO**
        conteo_mayoristas[oferta_elegida["id"]] += 1
        ahorro_financiero_total += oferta_elegida["ahorro_financiero"]
        credito_aprobado_count += oferta_elegida["aprobacion_credito"]


    # --- Retorno de Resultados ---
    total_transacciones = NUM_USUARIOS * COMPRAS_POR_USUARIO
    
    resultados = {
        "Total_Transacciones": total_transacciones,
        "Viajes_Vano": viajes_en_vano,
        "Tasa_Vano": round(viajes_en_vano / total_transacciones * 100, 2),
        "Credito_Aprobado": credito_aprobado_count,
        "Tasa_Credito": round(credito_aprobado_count / total_transacciones * 100, 2),
        "Ahorro_Financiero_Total": round(ahorro_financiero_total, 2),
        "Conteo_Mayoristas": conteo_mayoristas 
    }
    return resultados

# --- EJECUCIÓN DEL SCRIPT ---

if __name__ == '__main__':
    
    # 1. Ejecutar ambas simulaciones
    resultados_sin_app = simular_movimientos(escenario="sin_app")
    resultados_con_app = simular_movimientos(escenario="con_app")

    # 2. Impresión de resultados (LIMPIA Y ORDENADA)
    print("=" * 70)
    print("  SIMULACIÓN INTEGRADA: IMPACTO DE LA APP BNT EN MOVIMIENTOS B2B")
    print("=" * 70)
    
    print("\n🚨 ESCENARIO 1: SIN APP (Tradicional y Riesgoso)")
    print(f"  > Tasa de Viajes en Vano (Pérdida Operativa): {resultados_sin_app['Tasa_Vano']}%")
    print(f"  > Ahorro Financiero Total: Bs. {resultados_sin_app['Ahorro_Financiero_Total']:.2f}")
    print(f"  > Tasa de Crédito Aprobado (Bajo Credibilidad): {resultados_sin_app['Tasa_Credito']:.2f}%")
    print(f"  > Movimiento de Compra (Conteo): {resultados_sin_app['Conteo_Mayoristas']}")
    
    print("\n✅ ESCENARIO 2: CON APP (Estrategia BNT y Confianza Progresiva)")
    print(f"  > Tasa de Viajes en Vano (Pérdida Operativa): {resultados_con_app['Tasa_Vano']}%")
    print(f"  > Ahorro Financiero Total: Bs. {resultados_con_app['Ahorro_Financiero_Total']:.2f}")
    print(f"  > Tasa de Crédito Aprobado (Avalado por Credibilidad): {resultados_con_app['Tasa_Credito']:.2f}%")
    print(f"  > Movimiento de Compra (Conteo): {resultados_con_app['Conteo_Mayoristas']}")
    
    # 3. CONCLUSIÓN MEJORADA DEL VALOR
    
    # Cálculo de las mejoras
    reduccion_vano = resultados_sin_app['Tasa_Vano'] - resultados_con_app['Tasa_Vano']
    aumento_ahorro = resultados_con_app['Ahorro_Financiero_Total'] - resultados_sin_app['Ahorro_Financiero_Total']
    aumento_credito = resultados_con_app['Tasa_Credito'] - resultados_sin_app['Tasa_Credito']
    
    print("\n\n" + "=" * 70)
    print("⭐ VALOR AGREGADO DEL ALGORITMO BNT (RESUMEN EJECUTIVO)")
    print("=" * 70)
    print(f"📉 Reducción Operativa (Viajes en Vano): **{reduccion_vano:.2f}** puntos porcentuales.")
    print(f"   (Impacto directo en la **SATISFACCIÓN** y tiempo perdido del empresario)")
    print("-" * 70)
    print(f"💰 Aumento de Rentabilidad (Ahorro Neto): **Bs. {aumento_ahorro:.2f}** acumulados por la comunidad de 100 usuarios.")
    print(f"   (Impacto directo en la **RENTABILIDAD** y reducción de costos)")
    print("-" * 70)
    print(f"🏦 Aumento en Acceso a Liquidez (Crédito): **{aumento_credito:.2f}** puntos porcentuales.")
    print(f"   (Impacto directo en la **LIQUIDEZ** y crecimiento B2B por la **Credibilidad**)")
    print("=" * 70)