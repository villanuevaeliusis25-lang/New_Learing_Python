import matplotlib.pyplot as plt
import seaborn as sns 

# Configuración de estilo de gráficos (opcional, pero se ve más profesional)
sns.set_theme(style="whitegrid")

def generar_graficos_comparativos(resultados_sin_app: dict, resultados_con_app: dict):
    """
    Genera dos gráficos clave para comparar la ineficiencia (Viajes en Vano) 
    y el impacto financiero (Ahorro y Crédito) entre los escenarios.
    """
    labels_escenarios = ['Sin App (Tradicional)', 'Con App (Estrategia BNT)']
    
    tasa_vano = [resultados_sin_app['Tasa_Vano'], resultados_con_app['Tasa_Vano']]
    
    # Datos para el Gráfico 2 (Beneficio Financiero)
    ahorro_total = [resultados_sin_app['Ahorro_Financiero_Total'], resultados_con_app['Ahorro_Financiero_Total']]
    tasa_credito = [10.00, resultados_con_app['Tasa_Credito']] # 10.00% es la tasa simulada para 'Sin App'


    plt.figure(figsize=(8, 6))
    
    barras = plt.bar(labels_escenarios, tasa_vano, color=['salmon', 'mediumseagreen'])
    
    for bar in barras:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.2f}%', ha='center', va='bottom', fontsize=12)

    plt.title('📉 Reducción de Ineficiencia: Tasa de Viajes en Vano por Fallo (%)', fontsize=14)
    plt.ylabel('Tasa de Viajes en Vano (%)')
    plt.ylim(0, max(tasa_vano) * 1.3) # Ajustar el eje Y para que los textos no se corten
    plt.show() 
    
    fig, ax1 = plt.subplots(figsize=(10, 6))
    x = [0, 1]
    
    
    color_ahorro = 'darkorange'
    ax1.bar(x, ahorro_total, 0.4, label='Ahorro Financiero Total (Bs.)', color=color_ahorro)
    ax1.set_xlabel('Escenario de Compra', fontsize=12)
    ax1.set_ylabel('Ahorro Financiero Total (Bs.)', color=color_ahorro)
    ax1.tick_params(axis='y', labelcolor=color_ahorro)
    
    
    ax2 = ax1.twinx()  # Crea un segundo eje Y que comparte el mismo Eje X
    color_credito = 'steelblue'
    barras_credito = ax2.bar([i + 0.4 for i in x], tasa_credito, 0.4, label='Tasa de Crédito Aprobado (%)', color=color_credito)
    ax2.set_ylabel('Tasa de Crédito Aprobado (%)', color=color_credito)
    ax2.tick_params(axis='y', labelcolor=color_credito)
    
    for bar in barras_credito:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval:.2f}%', ha='center', va='bottom', fontsize=10)

    plt.title('💰 Impacto Financiero: Ahorro y Acceso a Crédito B2B', fontsize=14)
    ax1.set_xticks([i + 0.2 for i in x], labels_escenarios)
    fig.tight_layout()
    plt.show()