# Proyecto N#1 - Programación con Python

Una empresa que organiza competiciones le ha contratado a usted para que desarrolle una aplicación que le permite **analizar los resultados** de su última competencia. Los datos de la competencia serán suministrados en un **archivo .txt**, el cual contendrá en cada línea los datos separados **por coma** de cada participante.

Para dar cumplimiento al requerimiento, se desea desarrollar una aplicación que implementará la siguiente funcionalidad:

1. Lógica funcional (_reglas del negocio_) que permitirán **analizar los datos** y **suministrar resultados**.

2. Lógica del modelo de datos (_obtenida mediante el archivo txt suministrado_)

3. Manejo de excepciones

## Instrucciones

- Usar una estructura de carpetas (paquetes) que permita la separación de las diferentes partes de la aplicación: Una para la **vista**, otra para la **obtención de datos**, una para el **manejo de excepciones** y una para su **procesamiento (_controlador_)**.

- El archivo suministrado (_.txt_) contiene en cada línea la siguiente información separada por comas: CI, 1er Apellido, 2do Apellido, Nombre, Inicial 2do Nombre, Sexo, Edad, Horas,
  Minutos y Segundos.

## Requerimientos

- La ventana principal del proyecto debe contener un menú para manejar las opciones y acciones de la aplicación: **Archivo** y **Acciones**:

  - <ins>_**Menú Archivo**_</ins>: Se podrá seleccionar **Cargar Archivo** para escoger el archivo que contendrá los datos y **Salir** para salirse de la aplicación.

  - <ins>_**Menú Acciones**_</ins>: Se mostrarán diversas acciones de acuerdo a los resultados que el usuario desee ver.

    - Los resultados serán mostrados de dos formas:

      - Si el resultado solicitado es de **una línea**, se presentará en una sola línea

      - Si el resultado involucra **varios datos** se debe presentar en una **tabla formateada**.

    - Los participantes se dividen en **grupos etarios** (_por edad_) y por **sexo**. Los grupos etarios son:

      - Juniors, iguales o menores a 25 años,

      - Seniors, mayores de 25 y menores o iguales a 40 años y

      - Masters, mayores de 40 años

    - Los resultados a mostrar, usando diversos menús de selección en la opción **Acciones** son:

      - Lista con la totalidad de participantes (_tabla_)

      - Cantidad total de participantes (_una línea_)

      - Cantidad de participantes por grupo etario (_tabla, solo el grupo y la cantidad_)

      - Cantidad de participantes por sexo (_línea, sólo el grupo y la cantidad_)

      - Ganadores por grupo etario (_tabla_)

      - Ganadores por sexo (_tabla_)

      - Ganadores por grupo etario y sexo (_tabla_)

      - Ganador general (_línea_)

      - Histograma de participante por grupo etario. Representado de la siguiente forma:

      ```
      	Juniors (x): | ***********
      	Masters (y): | ********************
      	Seniors (z): | ********

      	# Donde x, y y z representan a la cantidad de participantes por grupo etario
      ```

      _Nota_: Se considera **ganador** al participante que ha empleado **menos tiempo** en ejecutar la competencia

- Después de presentar cada acción del menú debe existir una opción para retornar al menú principal

- La aplicación debe estar activa mientras el usuario no seleccione la opción de salir del menú Archivos

## Las excepciones y mensajes

La aplicación debe ser capaz de suministrar información al usuario cuando cargue un archivo que **no sea el correcto**, es decir que no sea un archivo .txt. Las excepciones que debe manejar el sistema, con sus respectivos mensajes son:

- Tipo de archivo incorrecto (_para validar que sea txt_)

- Cantidad de columnas incorrecto (_las líneas tienen la información indicada anteriormente_)

Al producirse cualquier de los fallos mencionados debe notificar al usuario con un mensaje y permitiéndole repetir la acción de forma correcta.
