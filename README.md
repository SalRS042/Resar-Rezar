# Rosario

Programa en Python para rezar el Rosario en valenciano o castellano, con selección del día de la semana y de los misterios correspondientes.

## Descripción

Este proyecto consiste en un programa desarrollado en Python que permite al usuario seleccionar el idioma en el que desea rezar y, posteriormente, elegir entre el Rosario y el Via Crucis.

Actualmente, la opción del Rosario está implementada para los siete días de la semana. En función del día seleccionado, el programa determina automáticamente los misterios correspondientes:

| Día       | Misterios |
| --------- | --------- |
| Lunes     | Gozosos   |
| Martes    | Dolorosos |
| Miércoles | Gloriosos |
| Jueves    | Luminosos |
| Viernes   | Dolorosos |
| Sábado    | Gozosos   |
| Domingo   | Gloriosos |

El programa está disponible en valenciano y castellano.

La opción correspondiente al Via Crucis se encuentra actualmente en proceso de desarrollo.

## Características

* Selección entre valenciano y castellano.
* Selección entre Rosario y Via Crucis.
* Selección del día de la semana.
* Determinación automática de los misterios correspondientes.
* Presentación progresiva de las oraciones.
* Pausas entre las diferentes partes del Rosario.
* Limpieza de la pantalla entre las distintas etapas.
* Los textos de las oraciones y de los misterios se almacenan en archivos CSV independientes del código principal.
* Admite la introducción de los días con o sin tilde.

## Estructura del proyecto

El proyecto está organizado de la siguiente manera:

```text
Rosario/
├── resar.py
├── Oracions_Valencia.csv
├── Oraciones_Castellano.csv
├── Misteris_Valencia.csv
├── Misterios_Castellano.csv
└── README.md
```

### `resar.py`

Contiene el código principal del programa y controla la interacción con el usuario, la selección del idioma, el día de la semana y los misterios correspondientes.

### `Oracions_Valencia.csv`

Contiene las oraciones utilizadas por el programa en valenciano.

### `Oraciones_Castellano.csv`

Contiene las oraciones utilizadas por el programa en castellano.

### `Misteris_Valencia.csv`

Contiene los misterios del Rosario en valenciano.

### `Misterios_Castellano.csv`

Contiene los misterios del Rosario en castellano.

## Requisitos

El programa requiere Python 3 y las siguientes bibliotecas:

```text
pandas
ipython
```

Se pueden instalar mediante:

```bash
pip install pandas ipython
```

## Ejecución

Todos los archivos CSV deben encontrarse en la misma carpeta que `rosario.py`.

Una vez instalados los requisitos, el programa puede ejecutarse mediante:

```bash
python rosario.py
```

Al iniciar el programa, se solicitará el idioma:

```text
Idioma: Valencià o Castellano
```

A continuación, el usuario podrá seleccionar qué desea rezar y, en el caso del Rosario, indicar el día de la semana.

## Funcionamiento

El flujo principal del programa es:

```text
Idioma
   │
   ├── Valencià
   │      │
   │      ├── Rosari
   │      │      └── Día de la semana
   │      │              └── Misterios correspondientes
   │      │
   │      └── Via Crucis
   │
   └── Castellano
          │
          ├── Rosario
          │      └── Día de la semana
          │              └── Misterios correspondientes
          │
          └── Via Crucis
```

Una vez seleccionados los misterios, el programa muestra progresivamente cada uno de ellos junto con las oraciones correspondientes.

## Estado del proyecto

El Rosario se encuentra implementado en valenciano y castellano.

La opción del Via Crucis está actualmente en desarrollo y se incorporará en una futura actualización.

## Fuente de los textos

Los textos utilizados por el programa se encuentran almacenados en los archivos CSV incluidos en el proyecto.

Los archivos de datos se mantienen separados del código para facilitar su consulta, modificación y mantenimiento.

## Referencias

Para la elaboración, revisión y adaptación de los textos utilizados en el programa se han consultado las siguientes fuentes:

1. Cofradía del Rosario de Torrent. *Rosario en valenciano*.
   https://cofradiarosariotorrent.org/paginas_val/rosario_val.html

2. El Santo Rosario. *Cómo rezar el Rosario*.
   https://www.elsantorosario.es/como-rezar-el-rosario/

3. Lo Rat Penat.
   https://loratpenat.org

4. Valencian.org. *Oracions en valencià*.
   http://www.valencian.org/angles/oracions.htm

Estas referencias se incluyen como fuentes de consulta de los contenidos religiosos y lingüísticos empleados en el proyecto.

## Licencia

La licencia del código de este proyecto se especificará de forma independiente de los textos y materiales contenidos en los archivos CSV.

En caso de reutilizar o modificar este proyecto, debe tenerse en cuenta que la licencia aplicable al código no implica necesariamente derechos adicionales sobre los textos contenidos en los archivos de datos.

## Autor

Proyecto desarrollado como iniciativa personal.

## Agradecimientos

Gracias de todo corazón a mis padres.

Nostre Senyor ens ampare.

Salva.
