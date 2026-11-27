import pandas as pd
from scipy.stats import spearmanr

# 1. Procesamiento de Kano
df_kano = pd.read_csv('kano_respuestas.csv')
print("=== Conteo Kano por caracteristica ===")
tabla_kano = pd.crosstab(df_kano['caracteristica_id'], df_kano['categoria_kano'])
for col in ['M', 'O', 'A', 'I', 'R', 'Q']:
    if col not in tabla_kano.columns:
        tabla_kano[col] = 0
tabla_kano = tabla_kano[['M', 'O', 'A', 'I', 'R', 'Q']]
denom = tabla_kano[['A', 'O', 'M', 'I']].sum(axis=1)
tabla_kano['Better'] = ((tabla_kano['A'] + tabla_kano['O']) / denom).round(2)
tabla_kano['Worse'] = (-1 * (tabla_kano['O'] + tabla_kano['M']) / denom).round(2)
print(tabla_kano)

# 2. Procesamiento de Votacion Ponderada y Spearman
df_vot = pd.read_csv('votacion_ponderada.csv')
moscow_map = {
    'RF-01': 1, 'RF-02': 1, 'RF-03': 1, 'RF-04': 1, 'RF-05': 1,
    'RF-06': 1, 'RF-07': 1, 'RF-08': 1, 'RNF-01': 1, 'RNF-02': 1,
    'RF-09': 2, 'RF-10': 2, 'RNF-03': 2, 'RNF-04': 2, 'RNF-05': 2,
    'RF-11': 3, 'RNF-06': 3, 'RNF-07': 3,
    'RF-12': 4, 'RNF-08': 4
}
df_vot['Rango_MoSCoW'] = df_vot['ID'].map(moscow_map).rank(ascending=True, method='average')
df_vot['Rango_Votacion'] = df_vot['Total_Puntos'].rank(ascending=False, method='average')
rho, p_val = spearmanr(df_vot['Rango_MoSCoW'], df_vot['Rango_Votacion'])
print(f"\nCorrelacion de Spearman (con correccion por empates): rho = {rho:.4f} (p = {p_val:.6f})")
