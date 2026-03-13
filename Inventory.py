# Solicita al usuario el nombre del producto y lo guarda como texto
nombre_producto = str(input("Ingrese el nombre del producto: "))

# Variables booleanas que controlan los ciclos de validación
# Se usan para repetir la pregunta hasta que el usuario ingrese un dato válido
verifica_cantidad = True
verifica_precio = True


# ==============================
# VALIDACIÓN DE LA CANTIDAD
# ==============================
while verifica_cantidad:

    # Solicita la cantidad del producto
    cantidad_producto = input("Ingrese la cantidad del producto: ")

    # Verifica que el valor ingresado sea un número entero positivo
    # isdigit() verifica que solo tenga números
    # int(cantidad_producto) > 0 verifica que sea mayor que 0
    if cantidad_producto.isdigit() and int(cantidad_producto) > 0:
        cantidad_producto = int(cantidad_producto)  # Convierte el valor a entero
        verifica_cantidad = False  # Sale del ciclo porque el dato es válido
    else:
        # Mensaje de error si el valor no es un número válido
        print(f"ven aca, cuando has visto tu que una cantidad sea '{cantidad_producto}', colocame un numero entero valido")


# ==============================
# VALIDACIÓN DEL PRECIO
# ==============================
while verifica_precio:

    # Solicita el precio del producto
    precios_producto = input("Ingrese el precio del producto: ")

    # replace('.', '', 1) permite que el número tenga un punto decimal
    # isdigit() valida que el resto sean números
    # float(precios_producto) > 0 valida que el precio sea mayor que 0
    if precios_producto.replace('.', '', 1).isdigit() and float(precios_producto) > 0:
        precios_producto = float(precios_producto)  # Convierte el valor a número decimal
        verifica_precio = False  # Sale del ciclo porque el dato es válido
    else:
        # Mensaje de error si el precio no es válido
        print(f"ven aca, cuando has visto tu que un precio sea '{precios_producto}', colocame un numero valido")


# ==============================
# CÁLCULO DEL COSTO TOTAL
# ==============================

# Multiplica la cantidad por el precio para obtener el costo total
costo_total = cantidad_producto * precios_producto


# ==============================
# SALIDA DE INFORMACIÓN
# ==============================

# Muestra toda la información del producto ingresado
print(f"Producto: {nombre_producto} | Precio: {precios_producto} | Cantidad: {cantidad_producto} | Total: {costo_total}")
