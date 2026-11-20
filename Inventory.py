# Solicita al usuario el nombre del producto y lo guarda como texto
nombre_producto = str(input("Ingrese el nombre del producto: "))

# Variables booleanas que controlan los ciclos de validación
verifica_cantidad = True
verifica_precio = True


# -----------------------------
# VALIDACIÓN DE LA CANTIDAD
# -----------------------------
# Este ciclo se repite hasta que el usuario ingrese una cantidad válida
while verifica_cantidad:

    # Se solicita la cantidad del producto (se guarda como texto para validarlo)
    cantidad_producto = input("Ingrese la cantidad del producto: ")

    # Se verifica que el valor ingresado sea un número entero positivo
    if cantidad_producto.isdigit() and int(cantidad_producto) > 0:
        
        # Si es válido, se convierte a entero
        cantidad_producto = int(cantidad_producto)
        
        # Se cambia la variable de control para salir del ciclo
        verifica_cantidad = False

    else:
        # Si no es válido, se muestra un mensaje de error
        print(f"ven aca, cuando has visto tu que una cantidad sea '{cantidad_producto}', colocame un numero entero valido")


# -----------------------------
# VALIDACIÓN DEL PRECIO
# -----------------------------
# Este ciclo se repite hasta que el usuario ingrese un precio válido
while verifica_precio:

    # Se solicita el precio del producto (se guarda como texto para validarlo)
    precios_producto = input("Ingrese el precio del producto: ")

    # Se verifica que el valor sea un número válido (permite un punto decimal)
    # replace('.', '', 1) elimina un solo punto para validar si el resto son dígitos
    if precios_producto.replace('.', '', 1).isdigit() and float(precios_producto) > 0:
        
        # Si es válido, se convierte a número decimal (float)
        precios_producto = float(precios_producto)
        
        # Se cambia la variable de control para salir del ciclo
        verifica_precio = False

    else:
        # Si el valor no es válido, se muestra un mensaje de error
        print(f"ven aca, cuando has visto tu que un precio sea '{precios_producto}', colocame un numero valido")


# -----------------------------
# CÁLCULO DEL COSTO TOTAL
# -----------------------------
# Se multiplica la cantidad del producto por su precio
costo_total = cantidad_producto * precios_producto


# -----------------------------
# SALIDA DE RESULTADOS
# -----------------------------
# Se muestra un resumen con el producto, precio, cantidad y total a pagar
print(f"Producto: {nombre_producto} | Precio: {precios_producto} | Cantidad: {cantidad_producto} | Total: {costo_total}")
