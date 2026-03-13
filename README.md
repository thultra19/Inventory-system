# 🧾 Calculadora de Costo de Producto (Python)

Este programa en **Python** permite ingresar información de un producto y calcular su costo total.
El sistema valida que la **cantidad** y el **precio** ingresados sean valores numéricos válidos antes de realizar el cálculo.

---

# 📁 Archivos del Proyecto

El proyecto solo necesita un archivo principal:

```
📦 calculadora-producto
 ┣ 📜 main.py
 ┗ 📜 README.md
```

### Descripción

| Archivo     | Descripción                               |
| ----------- | ----------------------------------------- |
| `main.py`   | Contiene el código principal del programa |
| `README.md` | Documentación del proyecto                |

---

# ⚙️ Requisitos

Para ejecutar este programa necesitas:

* **Python 3.8 o superior**
* Un intérprete de Python instalado en el sistema
* Terminal o consola para ejecutar el programa

Puedes verificar tu versión de Python con:

```bash
python --version
```

o

```bash
python3 --version
```

---

# ▶️ Cómo Ejecutar el Programa

1. Descarga o clona el repositorio.

```bash
git clone https://github.com/tu-usuario/calculadora-producto.git
```

2. Entra en la carpeta del proyecto.

```bash
cd calculadora-producto
```

3. Ejecuta el archivo principal.

```bash
python main.py
```

---

# 📌 Características

* Solicita al usuario:

  * Nombre del producto
  * Cantidad del producto
  * Precio del producto
* Valida que:

  * La **cantidad** sea un número entero positivo.
  * El **precio** sea un número positivo (permite decimales).
* Calcula automáticamente el **costo total**.
* Muestra un resumen con la información ingresada.

---

# 🛡️ Validaciones Implementadas

## Validación de Cantidad

Se usa `.isdigit()` para asegurar que el valor ingresado sea un número entero positivo.

```python
if cantidad_producto.isdigit() and int(cantidad_producto) > 0:
```

Esto evita que el usuario ingrese:

* letras
* números negativos
* valores vacíos

---

# 💻 Ejemplo de Ejecución

```
Ingrese el nombre del producto: Manzana
Ingrese la cantidad del producto: 3
Ingrese el precio del producto: 2.5

Producto: Manzana | Precio: 2.5 | Cantidad: 3 | Total: 7.5
```

---

# 🧠 Autor

**Luis  Guerrero** <br>
**Julio Ariza** <br>
**Edward Barrios**
