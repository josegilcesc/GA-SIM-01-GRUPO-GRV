# ISR-401 · Grupo GRV

Repositorio del equipo GRV (Gilces Carranza José Ignacio, Robinson Espinoza Jeanpierre, Vélez Vinces Jostin Gustavo) para Ingeniería de Requerimientos (ISR-401), 4.º nivel, paralelo B, SPA 2026–2027.

## Actividad Formativa: FORM-SIM-01 (GA-SIM-01 — Priorización de Requisitos)

- **Carpeta:** `FORM-SIM-01/`
- **Dominio asignado (N.º 6):** Asociación de productores de cacao: acopio y pagos
- **Archivo principal:** `FORM-SIM-01/main.tex`
- **PDF generado:** `FORM-SIM-01/main.pdf`

### Dependencias de compilación
- **Compilador LaTeX:** `pdflatex` (TeX Live 2024+ o MiKTeX actualizado)
- **Gestor bibliográfico:** `biber` (`biblatex` con estilo `ieee`)
- **Paquetes LaTeX requeridos:** `lmodern`, `babel` (spanish), `geometry`, `microtype`, `amsmath`, `array`, `tabularx`, `booktabs`, `colortbl`, `xcolor`, `enumitem`, `fancyhdr`, `lastpage`, `tcolorbox`, `csquotes`, `biblatex`, `hyperref`
- **Reproducción de cálculos (opcional):** Python 3.10+ con `pandas` y `scipy` (`FORM-SIM-01/datos/calculos_priorizacion.py`)

### Orden exacto de comandos para reproducir `main.pdf`
```bash
cd FORM-SIM-01
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

### Reproducción de cálculos de Kano y Spearman
```bash
cd FORM-SIM-01/datos
python calculos_priorizacion.py
```
