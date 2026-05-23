Markdown
# 🐾 Waflle - Tu Mascota Virtual en Python

¡Bienvenido a **Waflle**, un juego interactivo de consola basado en texto donde podrás cuidar, alimentar y jugar con tu propia mascota virtual escrita en Python!

Este es un proyecto ideal para aprender los fundamentos de la programación como bucles (`while`), condicionales (`if-elif-else`) y manejo de estados.

---

## 🚀 Características

* **Sistema de Estado Dinámico:** Controla la `Energía` y `Felicidad` de Waflle en tiempo real.
* **Interacciones Variadas:** Elige entre alimentarlo, jugar con él o dejarlo descansar (¡pero cuidado, que se aburre!).
* **Gráficos ASCII:** Visualiza a tu mascota directamente en la terminal gracias al arte ASCII incluido.

---

## 🎮 Mecánicas del Juego

Cada acción que tomas afecta las estadísticas de Waflle de la siguiente manera:

| Acción | ⚡ Energía | ❤️ Felicidad | Descripción |
| :--- | :---: | :---: | :--- |
| **1. Alimentar** | +20 | +1 | Le das comida deliciosa a Waflle. |
| **2. Jugar** | -15 | +20 | Te diviertes con él, pero gasta energía. |
| **3. Ver Estado** | 0 | 0 | Muestra el arte ASCII y sus estadísticas actuales. |
| **4. No hacer nada** | -5 | -10 | Waflle se aburre y pierde un poco de todo. |

> ⚠️ **Game Over:** Si la energía de Waflle llega a **0 o menos**, el bucle terminará y el juego finalizará. ¡Manténlo saludable!

---

## 🛠️ Requisitos e Instalación

Para ejecutar este juego, solo necesitas tener **Python 3** instalado en tu computadora.

1. **Clona este repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/Waflle.git](https://github.com/TU_USUARIO/Waflle.git)
Navega al directorio del proyecto:

Bash
cd Waflle
Ejecuta el script:

Bash
python main.py
