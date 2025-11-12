# Variables del Comprador (Simulación del usuario con NIT)
SCORE_COMPRADOR_B2B = 85  # Alto score crediticio B2B (0-100)
CANTIDAD_DESEADA = 1000   # Unidades de producto X

# Variables de Penalización (Costo de Riesgo en Bs.)
COSTO_DISPUTA_ESTIMADO = 50.0  # Costo promedio de una disputa o viaje en vano

# Simulación de la Base de Datos de Mayoristas
data_mayoristas = [
    {
        "nombre": "Mayorista A (Bajo Precio/Alto Riesgo)",
        "pnn_base": 4.50,         # Precio Net-Net (Bs./Ud.)
        "costo_logistica": 10.0,
        "garantia_digital": 0.70, # Bajo: Solo 70% de probabilidad de cumplir con la oferta digital
        "descuento_credito": 0.0, # No ofrece descuento por crédito
        "plazo_credito_dias": 7   # Plazo de pago corto
    },
    {
        "nombre": "Mayorista B (Sugerencia/Alto Crédito)",
        "pnn_base": 4.60,
        "costo_logistica": 0.0,   # ¡Entrega Gratis!
        "garantia_digital": 0.98, # Alto: 98% de probabilidad de cumplir (Avalado por App)
        "descuento_credito": 0.03, # Alto: Ofrece 3% de descuento por buen score B2B
        "plazo_credito_dias": 60  # Plazo de pago extendido
    },
    {
        "nombre": "Mayorista C (Precio Alto/Logística Difícil)",
        "pnn_base": 4.75,
        "costo_logistica": 30.0,
        "garantia_digital": 0.90,
        "descuento_credito": 0.01,
        "plazo_credito_dias": 30
    }
]


def calcular_bnt_y_cot(mayorista, cantidad, score_comprador):
    
    # --- 1. Cálculo del Costo Total (CT) ---
    costo_producto = mayorista["pnn_base"] * cantidad
    costo_total_oferta = costo_producto + mayorista["costo_logistica"]
    
    # --- 2. Cálculo del Beneficio / Ahorro Financiero ---
    # Solo se aplica si el comprador tiene un buen Score (>80)
    ahorro_financiero = 0
    if score_comprador >= 80 and mayorista["plazo_credito_dias"] > 30:
        # El valor del descuento por usar el Score B2B
        ahorro_financiero = costo_producto * mayorista["descuento_credito"]
        
    # --- 3. Cálculo del Costo de Riesgo (Penalización) ---
    # Costo de Riesgo = Probabilidad de Fallo * Costo de Disputa
    probabilidad_fallo = 1.0 - mayorista["garantia_digital"]
    costo_riesgo = probabilidad_fallo * COSTO_DISPUTA_ESTIMADO
    
    # --- 4. Cálculo del Beneficio Neto por Transacción (BNT) ---
    # Se utiliza el Costo Total Mínimo como la base comparativa
    
    # Calculamos el costo final con los beneficios
    costo_neto_real = costo_total_oferta - ahorro_financiero + costo_riesgo
    
    # Para la sugerencia, el menor 'costo_neto_real' gana.
    # El BNT (Puntaje de Valor) será el INVERSO del costo neto real.
    bnt_puntaje = 10000 / costo_neto_real 

    return {
        "nombre": mayorista["nombre"],
        "costo_total_oferta": round(costo_total_oferta, 2),
        "ahorro_financiero": round(ahorro_financiero, 2),
        "costo_riesgo_simulado": round(costo_riesgo, 2),
        "costo_neto_real": round(costo_neto_real, 2),
        "bnt_puntaje": round(bnt_puntaje, 2)
    }
    
    
resultados_simulacion = []
for mayorista in data_mayoristas:
    resultados_simulacion.append(
        calcular_bnt_y_cot(mayorista, CANTIDAD_DESEADA, SCORE_COMPRADOR_B2B)
    )

# Ordenar por el mejor BNT (Puntaje más alto)
sugerencia_final = sorted(resultados_simulacion, key=lambda x: x["bnt_puntaje"], reverse=True)

# Imprimir el análisis clave
print("=" * 60)
print(f"ANÁLISIS DE GARANTÍA Y FINANCIAMIENTO PARA {CANTIDAD_DESEADA} UNIDADES (Score B2B: {SCORE_COMPRADOR_B2B})")
print("=" * 60)

for r in sugerencia_final:
    print(f"\nMAYORISTA: {r['nombre']}")
    print(f"  > Costo Total (Oferta Inicial): Bs. {r['costo_total_oferta']}")
    print(f"  > Ahorro Financiero (Crédito): - Bs. {r['ahorro_financiero']}")
    print(f"  > Riesgo de Disputa (Costo): + Bs. {r['costo_riesgo_simulado']}")
    print(f"  > COSTO NETO REAL: Bs. {r['costo_neto_real']}")
    print(f"  > PUNTAJE BNT: {r['bnt_puntaje']}")

print("\n" + "-" * 60)
print(f"🏆 SUGERENCIA DE LA APP: {sugerencia_final[0]['nombre']}")
print(f"Justificación: Aunque el Costo Total Inicial es más alto que A, el BNT es superior debido al Ahorro Financiero (3% de descuento) y la Alta Garantía Digital (bajo Costo de Riesgo).")
print("-" * 60)