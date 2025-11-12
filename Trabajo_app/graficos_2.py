import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
import numpy as np # Importamos numpy para el manejo de índices

# --- CONFIGURACIÓN DE ESTILO EVA-01 ---
# Paleta de colores Evangelion: Púrpura y Verde Neón (usaremos Púrpura y Naranja/Lima para contraste)
EVA_PURPLE = '#4A0080' # Púrpura profundo para Sin App / Ahorro
EVA_LIME = '#90EE90'   # Verde Lima Neón para Con App / Crédito

# 1. Configurar el tema oscuro de Matplotlib
plt.style.use('dark_background') 
# 2. Configurar el estilo de Seaborn (sin la paleta global)
sns.set_theme(style="darkgrid") 

def generar_graficos_esteticos(resultados_sin_app: dict, resultados_con_app: dict):
    
    # -----------------------------------------------------------
    # 1. PREPARACIÓN DE DATOS
    # -----------------------------------------------------------
    
    # Etiquetas de los escenarios para los ejes X
    labels_escenarios = ['Sin App (Tradicional)', 'Con App (Estrategia BNT)']
    x_indices = np.arange(len(labels_escenarios)) # [0, 1]

    # Datos para el Gráfico 2 (Beneficio Financiero)
    # El valor de Ahorro es el que determina la altura de la barra NARANJA/PÚRPURA
    ahorro_total = [resultados_sin_app['Ahorro_Financiero_Total'], resultados_con_app['Ahorro_Financiero_Total']]
    
    # La Tasa de Crédito es el valor de la barra AZUL/VERDE
    # Usamos 10% simulado para Sin App. El valor debe ser consistente en ambos archivos.
    tasa_credito = [10.00, resultados_con_app['Tasa_Credito']] 
    
    ancho_barra = 0.40
    
    # -----------------------------------------------------------
    # 2. GRÁFICO 2: IMPACTO FINANCIERO CON DOBLE EJE Y ESTILO EVA
    # -----------------------------------------------------------
    
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Eje 1 (Izquierda): Ahorro Financiero Total (Bs.)
    color_ahorro = EVA_PURPLE # Púrpura EVA para Ahorro
    barras_ahorro = ax1.bar(x_indices, ahorro_total, ancho_barra, label='Ahorro Financiero Total (Bs.)', color=color_ahorro)
    
    ax1.set_xlabel('Escenario de Compra', fontsize=12, color='white')
    ax1.set_ylabel('Ahorro Financiero Total (Bs.)', color=color_ahorro, fontsize=12)
    ax1.tick_params(axis='y', labelcolor=color_ahorro)
    
    # Eje 2 (Derecha): Tasa de Crédito Aprobado (%)
    ax2 = ax1.twinx()  # Crea un segundo eje Y
    color_credito = EVA_LIME # Verde Neón EVA para Crédito
    barras_credito = ax2.bar(x_indices + ancho_barra, tasa_credito, ancho_barra, label='Tasa de Crédito Aprobado (%)', color=color_credito)
    
    ax2.set_ylabel('Tasa de Crédito Aprobado (%)', color=color_credito, fontsize=12)
    ax2.tick_params(axis='y', labelcolor=color_credito)
    ax2.set_ylim(0, max(tasa_credito) * 1.2) # Asegurar que el eje derecho tenga margen

    # --- ANOTACIONES DE DATOS (TEXTOS SOBRE LAS BARRAS) ---
    
    # Anotaciones para Ahorro Financiero (EVA PURPLE)
    for bar in barras_ahorro:
        height = bar.get_height()
        ax1.annotate(f'Bs. {height:,.0f}', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), # Offset vertical
                    textcoords="offset points", 
                    ha='center', va='bottom',
                    fontsize=10, color='white') # Usamos blanco para visibilidad

    # Anotaciones para Tasa de Crédito (EVA NEÓN)
    for bar in barras_credito:
        height = bar.get_height()
        ax2.annotate(f'{height:.2f}%', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), # Offset vertical
                    textcoords="offset points", 
                    ha='center', va='bottom',
                    fontsize=10, color='#FFFF00') # Amarillo Neón para destacar sobre el verde

    # Configuración de Ejes X
    ax1.set_xticks(x_indices + ancho_barra / 2, labels_escenarios)
    
    # Título y Leyendas (Ajustes para el fondo oscuro)
    plt.title('💰 Impacto Financiero: Ahorro y Acceso a Crédito B2B (Estilo EVA-01)', fontsize=14, color='white')
    
    # Combinar leyendas de ambos ejes
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc='upper center', bbox_to_anchor=(0.5, 1.15), 
            facecolor='black', edgecolor='white', title_fontsize=10)


    fig.tight_layout() # Asegura que nada se superponga
    plt.show()