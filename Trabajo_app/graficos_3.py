import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd # Necesario si usas el segundo gráfico de barras agrupadas

# --- COLORES DE EVANGELION PARA TEMA CLARO ---
# Púrpura profundo para el riesgo (Sin App)
COLOR_RIESGO = '#4A0080' 
# Verde Neón/Lima para la solución (Con App)
COLOR_SOLUCION = '#90EE90' 

# Configuración de estilo (quitamos el tema oscuro)
sns.set_theme(style="whitegrid")

def generar_graficos_comparativos(resultados_sin_app: dict, resultados_con_app: dict):
    """
    Genera dos gráficos clave comparando la ineficiencia (Viajes en Vano) 
    y el impacto financiero (Ahorro y Crédito) entre los escenarios.
    """
    
    # -----------------------------------------------------------
    # 1. PREPARACIÓN DE DATOS Y ETIQUETAS
    # -----------------------------------------------------------
    
    labels_escenarios = ['Sin App (Tradicional)', 'Con App (Estrategia BNT)']
    
    # Datos para el Gráfico 1 (Riesgo Operativo)
    tasa_vano = [resultados_sin_app['Tasa_Vano'], resultados_con_app['Tasa_Vano']]
    
    # Datos para el Gráfico 2 (Beneficio Financiero)
    ahorro_total = [resultados_sin_app['Ahorro_Financiero_Total'], resultados_con_app['Ahorro_Financiero_Total']]
    # Usamos 10% simulado para Sin App para que el gráfico sea comparable
    tasa_credito = [10.00, resultados_con_app['Tasa_Credito']] 
    
    # -----------------------------------------------------------
    # 2. GRÁFICO 1: RIESGO OPERATIVO Y SATISFACCIÓN (Viajes en Vano)
    # -----------------------------------------------------------
    
    plt.figure(figsize=(8, 6))
    
    # Asignamos los colores EVA-01: Púrpura para Sin App, Verde Neón para Con App
    barras = plt.bar(labels_escenarios, tasa_vano, color=[COLOR_RIESGO, COLOR_SOLUCION])
    
    # Añadir el porcentaje sobre cada barra
    for bar in barras:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.2f}%', ha='center', va='bottom', fontsize=12)

    plt.title('📉 Reducción de Ineficiencia: Tasa de Viajes en Vano por Fallo (%)', fontsize=14)
    plt.ylabel('Tasa de Viajes en Vano (%)')
    plt.ylim(0, max(tasa_vano) * 1.2)
    plt.grid(axis='y', linestyle='--')
    plt.show() 
    
    # -----------------------------------------------------------
    # 3. GRÁFICO 2: BENEFICIO FINANCIERO Y LIQUIDEZ (Doble Eje Y)
    # -----------------------------------------------------------
    
    fig, ax1 = plt.subplots(figsize=(10, 6))
    x = [0, 1]
    ancho_barra = 0.35
    
    # Barra 1: Ahorro Financiero Total (Eje Izquierdo - Color Naranja/Púrpura)
    # Usaremos el Púrpura para el Ahorro
    color_ahorro = COLOR_RIESGO 
    ax1.bar(x, ahorro_total, ancho_barra, label='Ahorro Financiero Total (Bs.)', color=color_ahorro)
    ax1.set_xlabel('Escenario de Compra', fontsize=12)
    ax1.set_ylabel('Ahorro Financiero Total (Bs.)', color=color_ahorro)
    ax1.tick_params(axis='y', labelcolor=color_ahorro)
    
    # Barra 2: Tasa de Crédito Aprobado (Eje Derecho - Color Azul/Verde Neón)
    ax2 = ax1.twinx()  # Crea un segundo eje Y
    # Usaremos el Verde Neón para el Crédito
    color_credito = COLOR_SOLUCION 
    barras_credito = ax2.bar([i + ancho_barra for i in x], tasa_credito, ancho_barra, label='Tasa de Crédito Aprobado (%)', color=color_credito)
    ax2.set_ylabel('Tasa de Crédito Aprobado (%)', color=color_credito)
    ax2.tick_params(axis='y', labelcolor=color_credito)
    
    # Añadir el porcentaje sobre las barras de crédito
    for bar in barras_credito:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval:.2f}%', ha='center', va='bottom', fontsize=10)

    plt.title('💰 Impacto Financiero: Ahorro y Acceso a Crédito B2B', fontsize=14)
    ax1.set_xticks([i + ancho_barra/2 for i in x], labels_escenarios)
    fig.tight_layout()
    plt.show()

# -----------------------------------------------------------
# 4. INSTRUCCIONES PARA USAR EN OTRO ARCHIVO
# -----------------------------------------------------------

if __name__ == '__main__':
    print("Este archivo debe ser llamado desde el archivo de simulación (bosquejo_2.py).")