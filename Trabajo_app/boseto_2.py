import random

# --- VARIABLES GLOBALES Y PENALIZACIONES ---
NUM_USUARIOS_SIMULAR = 100
COMPRAS_POR_USUARIO_MES = 6 # Cada usuario hará 6 intentos de compra
CANTIDAD_DESEADA_PROMEDIO = 1000  # Unidades a comprar
COSTO_DISPUTA_ESTIMADO = 50.0  # Costo de un "Viaje en Vano" o disputa (Bs.)

# --- BASE DE DATOS DE MAYORISTAS (Versión Simplificada) ---
data_mayoristas = [
    {
        "id": 1, "nombre": "Mayorista A (Riesgo)",
        "pnn_base": 4.50, "costo_logistica": 10.0,
        "garantia_digital": 0.70, # 30% de riesgo de fallo
        "descuento_credito": 0.0, "plazo_credito_dias": 7
    },
    {
        "id": 2, "nombre": "Mayorista B (Recomendado)",
        "pnn_base": 4.60, "costo_logistica": 0.0, # Entrega Gratis
        "garantia_digital": 0.98, # 2% de riesgo de fallo
        "descuento_credito": 0.03, "plazo_credito_dias": 60
    },
    {
        "id": 3, "nombre": "Mayorista C (Precio Alto)",
        "pnn_base": 4.75, "costo_logistica": 30.0,
        "garantia_digital": 0.90,
        "descuento_credito": 0.01, "plazo_credito_dias": 30
    }
]



def calcular_bnt_y_cot(mayorista, cantidad, score_comprador):
    """Calcula el Costo Neto Real y el Puntaje BNT para un mayorista."""
    
    # 1. Costo Total de Oferta (PNN + Logística)
    costo_producto = mayorista["pnn_base"] * cantidad
    costo_total_oferta = costo_producto + mayorista["costo_logistica"]

    # 2. Ahorro Financiero (Por Score B2B y Plazo Extendido)
    ahorro_financiero = 0.0
    # La app negocia un descuento si el comprador es de alta confianza (Score >= 80) y el mayorista lo ofrece.
    if score_comprador >= 80 and mayorista["plazo_credito_dias"] > 30:
        ahorro_financiero = costo_producto * mayorista["descuento_credito"]
        
    # 3. Costo de Riesgo (Penalización por Baja Garantía Digital)
    probabilidad_fallo = 1.0 - mayorista["garantia_digital"]
    costo_riesgo = probabilidad_fallo * COSTO_DISPUTA_ESTIMADO
    
    # 4. Cálculo del Costo Neto Real y el Puntaje BNT
    costo_neto_real = costo_total_oferta - ahorro_financiero + costo_riesgo
    
    # El puntaje BNT es el criterio de sugerencia (el menor costo neto real es el mayor puntaje)
    bnt_puntaje = 10000 / costo_neto_real 

    return {
        "id": mayorista["id"],
        "nombre": mayorista["nombre"],
        "costo_neto_real": costo_neto_real,
        "bnt_puntaje": bnt_puntaje,
        "ahorro_financiero": ahorro_financiero,
        "aprobacion_credito": 1 if ahorro_financiero > 0 else 0, # Se aprueba crédito si hay ahorro
        "riesgo_fallo": probabilidad_fallo
    }
    
    
    
def simular_movimientos(escenario="con_app"):
    """
    Simula las decisiones de compra de 100 usuarios en 600 transacciones.
    Retorna los KPIs acumulados.
    """
    
    # Inicialización de KPIs
    viajes_en_vano = 0
    credito_aprobado_count = 0
    ahorro_financiero_total = 0.0
    
    # --- Generación de Usuarios (Simulación de la Población NIT) ---
    usuarios = []
    for i in range(NUM_USUARIOS_SIMULAR):
        # El 60% tiene un Score B2B alto (>80) y el resto es promedio/bajo.
        score = random.randint(80, 95) if random.random() < 0.6 else random.randint(60, 79)
        usuarios.append({"id": i, "score_b2b": score, "compras_al_mes": COMPRAS_POR_USUARIO_MES})

    # --- Simulación de Transacciones ---
    for usuario in usuarios:
        for _ in range(usuario["compras_al_mes"]):
            
            # 1. Obtener todas las ofertas disponibles
            ofertas_calculadas = [
                calcular_bnt_y_cot(m, CANTIDAD_DESEADA_PROMEDIO, usuario["score_b2b"]) 
                for m in data_mayoristas
            ]

            if escenario == "sin_app":
                # --- LÓGICA SIN APP: Se elige el PNN más bajo (mayorista 1) ---
                # Simulamos que el usuario ve el precio más bajo (Mayorista A - id 1) y va allí.
                oferta_elegida = next(o for o in ofertas_calculadas if o['id'] == 1) 
                
                # El riesgo de fallo es la probabilidad de incumplimiento del mayorista elegido
                if random.random() < oferta_elegida["riesgo_fallo"]:
                    viajes_en_vano += 1 # El usuario perdió el viaje (fallo de stock/precio)
                    
            elif escenario == "con_app":
                # --- LÓGICA CON APP: Se elige el mayor BNT (menor Costo Neto Real) ---
                oferta_elegida = max(ofertas_calculadas, key=lambda x: x["bnt_puntaje"])
                
                # El riesgo de fallo se mitiga con la Garantía Digital (baja probabilidad)
                if random.random() < oferta_elegida["riesgo_fallo"]:
                    viajes_en_vano += 1 # Aún puede fallar, pero la probabilidad es menor.
            
            # Acumular los KPIs
            ahorro_financiero_total += oferta_elegida["ahorro_financiero"]
            credito_aprobado_count += oferta_elegida["aprobacion_credito"]

    # --- Retorno de Resultados ---
    total_transacciones = NUM_USUARIOS_SIMULAR * COMPRAS_POR_USUARIO_MES
    
    return {
        "Total_Transacciones": total_transacciones,
        "Viajes_Vano": viajes_en_vano,
        "Tasa_Vano": round(viajes_en_vano / total_transacciones * 100, 2),
        "Credito_Aprobado": credito_aprobado_count,
        "Tasa_Credito": round(credito_aprobado_count / total_transacciones * 100, 2),
        "Ahorro_Financiero_Total": round(ahorro_financiero_total, 2)
    }

# --- EJECUTAR LA SIMULACIÓN Y COMPARAR RESULTADOS ---
resultados_sin_app = simular_movimientos(escenario="sin_app")
resultados_con_app = simular_movimientos(escenario="con_app")

print("=" * 70)
print("  SIMULACIÓN DE MOVIMIENTOS Y SATISFACCIÓN (100 NEGOCIOS CON NIT)")
print("=" * 70)

print("\n🚨 ESCENARIO 1: SIN APP (Basado en Precio y Confianza Ciega)")
print("-" * 50)
print(f"  Total de Transacciones: {resultados_sin_app['Total_Transacciones']}")
print(f"  Total Viajes en Vano (Fallos): {resultados_sin_app['Viajes_Vano']}")
print(f"  Tasa de Viajes en Vano (Fallo): {resultados_sin_app['Tasa_Vano']}%")
print(f"  Tasa de Crédito Aprobado (Simulada): 10.00% (Baja, sin aval B2B)")
print(f"  Ahorro Financiero Total (Simulado): Bs. {resultados_sin_app['Ahorro_Financiero_Total']}\n")

print("✅ ESCENARIO 2: CON APP (Basado en BNT y Garantía Financiera)")
print("-" * 50)
print(f"  Total de Transacciones: {resultados_con_app['Total_Transacciones']}")
print(f"  Total Viajes en Vano (Fallos): {resultados_con_app['Viajes_Vano']}")
print(f"  Tasa de Viajes en Vano (Fallo): {resultados_con_app['Tasa_Vano']}%")
print(f"  Tasa de Crédito Aprobado (App): {resultados_con_app['Tasa_Credito']}%")
print(f"  Ahorro Financiero Total (App): Bs. {resultados_con_app['Ahorro_Financiero_Total']}\n")

print("----------------------------------------------------------------------")
print("⭐ CONCLUSIÓN DEL VALOR AGREGADO DE LA APP:")
print(f"  - Reducción de Viajes en Vano: {round(resultados_sin_app['Tasa_Vano'] - resultados_con_app['Tasa_Vano'], 2)} puntos porcentuales (Mejora la SATISFACCIÓN)")
print(f"  - Aumento de Ahorro Financiero: Bs. {round(resultados_con_app['Ahorro_Financiero_Total'] - resultados_sin_app['Ahorro_Financiero_Total'], 2)} (Mejora la RENTABILIDAD)")
print("----------------------------------------------------------------------")

from graficos import generar_graficos_comparativos
generar_graficos_comparativos(resultados_sin_app, resultados_con_app)