import pandas as pd
from IPython.display import clear_output
import unicodedata

Oracions_Valencia = pd.read_csv('Oracions_Valencia.csv')
Oraciones_Castellano = pd.read_csv('Oracions_Castellano.csv')

Misteris_Valencia = pd.read_csv('Misteris_Valencia.csv')
Misterios_Castellano = pd.read_csv('Misterios_Castellano.csv')

def normalizar(texto):
    texto = texto.strip().lower()
    return ''.join(
        caracter
        for caracter in unicodedata.normalize('NFD', texto)
        if unicodedata.category(caracter) != 'Mn'
    )

def continuar_cas():
    input("Pulsa Enter para continuar...")
    clear_output(wait=True)

def continuar_val():
    input("Apreta Enter par a continuar...")
    clear_output(wait=True)

# Rosari

def resar_rosari(
    oracions,
    misteris,
    columna_misteris,
    nom_misteris,
    nom_misteri,
    idioma
):
    
    if idioma == 'valencià':
        print("Perfecte! Anem a resar! Sols has de seguir les instruccions.\n")

        print("Comencem amb la senyal de la creu i l'acte de constricció:\n",Oracions_Valencia['Oracions'][0],"\n")
        print(oracions['Oracions'][1], "\n")
        print(oracions['Oracions'][2], "\n")
        print(oracions['Oracions'][3], "\n")
        print(oracions['Oracions'][4], "\n")
        continuar_val()
        clear_output(wait=True)

        print(f"Ara anem a resar els misteris " f"{nom_misteris}.\n")
        for i in range(5):
            print(misteris['Orden'][i],nom_misteri,": ", misteris[columna_misteris][i],"\n")
    
            print("Pare nostre: ",oracions['Oracions'][5],"\n")
            print("10 voltes l'Ave Maria: ",oracions['Oracions'][6],"\n")
            print("Gloria: ",oracions['Oracions'][4],"\n")
            print("Jaculatòria: ",oracions['Oracions'][7],"\n")
            print("Oh, Jesús meu: ",oracions['Oracions'][8],"\n")
            continuar_val()
            clear_output(wait=True)

        print("Anem a resar les Letanies a la Santíssima Verge:\n", oracions['Oracions'][9],"\n")
        continuar_val()
        clear_output(wait=True)

        print("Invoquem al Corder de Déu:\n",oracions['Oracions'][10],"\n")
        continuar_val()
        clear_output(wait=True)

        print("Demane'm:\n",oracions['Oracions'][11],"\n")
        continuar_val()
        clear_output(wait=True)

        print("Per les intencions del Sant Pare: ",oracions['Oracions'][5],"\n")
        continuar_val()
        clear_output(wait=True)

        print("Un Ave Maria: ",oracions['Oracions'][6],"\n")
        continuar_val()
        clear_output(wait=True)

        print("Un gloria: ",oracions['Oracions'][4],"\n")
        continuar_val()
        clear_output(wait=True)

        print("Una Salve a la Verge:\n",oracions['Oracions'][12],"\n")
        continuar_val()
        clear_output(wait=True)

        print("Jaculatòria:\n",oracions['Oracions'][13],"\n")
        continuar_val()
        clear_output(wait=True)

    elif idioma == 'castellano':
        print("¡Perfecto! ¡Vamos a rezar! Sólo tienes que seguir las instrucciones.\n")

        print("Empezamos con la señal de la cruz y el acto de contrición:\n", oracions['Oraciones'][0],"\n")
        print(oracions['Oraciones'][1], "\n")
        print(oracions['Oraciones'][2], "\n")
        print(oracions['Oraciones'][3], "\n")
        print(oracions['Oraciones'][4], "\n")
        continuar_cas()
        clear_output(wait=True)

        print(f"Ahora vamos a rezar los misterios " f"{nom_misteris}.\n")
        for i in range(5):
            print(misteris['Orden'][i],nom_misteri,": ", misteris[columna_misteris][i],"\n")
    
            print("Padre nuestro: ",oracions['Oraciones'][5],"\n")
            print("10 veces el Ave Maria: ",oracions['Oraciones'][6],"\n")
            print("Gloria: ",oracions['Oraciones'][4],"\n")
            print("Jaculatoria: ",oracions['Oraciones'][7],"\n")
            print("Oh, Jesús mío: ",oracions['Oraciones'][8],"\n")
        continuar_cas()
        clear_output(wait=True)

        print("Vamos a rezar las Letanías a la Santísima Virgen:\n", oracions['Oraciones'][9],"\n")
        continuar_cas()
        clear_output(wait=True)

        print("Invocamos al Cordero de Dios:\n",oracions['Oraciones'][10],"\n")
        continuar_cas()
        clear_output(wait=True)

        print("Pedimos:\n",oracions['Oraciones'][11],"\n")
        continuar_cas()
        clear_output(wait=True)

        print("Por las intenciones del Santo Padre: ",oracions['Oraciones'][5],"\n")
        continuar_cas()
        clear_output(wait=True)

        print("Un Ave María: ",oracions['Oraciones'][6],"\n")
        continuar_cas()
        clear_output(wait=True)

        print("Un Gloria: ",oracions['Oraciones'][4],"\n")
        continuar_cas()
        clear_output(wait=True)

        print("Una Salve a la Virgen:\n",oracions['Oraciones'][12],"\n")
        continuar_cas()
        clear_output(wait=True)

        print("Jaculatoria:\n",oracions['Oraciones'][13],"\n")
        continuar_cas()
        clear_output(wait=True)

    else:
        pass

def rosari_valencia():
    que_resar = normalizar(input('\nQuè vols resar?: Rosari o Via Crucis '))

    if que_resar == 'rosari':
        dia = normalizar(input('\nQuin dia és hui?: Dilluns, Dimarts, Dimecres, Dijous, Divendres, Dissabte o Diumenge. '))

        misteris = {
            'dilluns': (
                'Misteris Gojosos',
                'Gojós',
                'Gojosos'
            ),
            'dissabte': (
                'Misteris Gojosos',
                'Gojós',
                'Gojosos'
            ),
            'dimecres': (
                'Misteris Gloriosos',
                'Gloriós',
                'Gloriosos'
            ),
            'diumenge': (
                'Misteris Gloriosos',
                'Gloriós',
                'Gloriosos'
            ),
            'dimarts': (
                'Misteris Dolorosos',
                'Dolorós',
                'Dolorosos'
            ),
            'divendres': (
                'Misteris Dolorosos',
                'Dolorós',
                'Dolorosos'
            ),
            'dijous': (
                'Misteris Lluminosos',
                'Luminós',
                'Lluminosos'
            )
        }

        if dia not in misteris:
            print("No has introduït un dia correcte. Torna a començar el programa i introdueix un dia correcte.")
            return

        columna, nombre_misteri, nombre_misterios = misteris[dia]

        resar_rosari(
            Oracions_Valencia,
            Misteris_Valencia,
            columna,
            nombre_misterios,
            nombre_misteri,
            'valencià'
        )

    elif que_resar == 'via crucis':
        print('En procés de desenvolupament. Esta opció estarà disponible a la pròxima actualització del programa.')

    else:
        print("No has introduït una opció correcta. Torna a començar el programa i introdueix una opció correcta.")

def rosario_castellano():
    que_rezar = normalizar(input('\n¿Qué quieres rezar?: Rosario o Via Crucis '))

    if que_rezar == 'rosario':

        dia = normalizar(input('\n¿Qué día es hoy?: Lunes, Martes, Miércoles, Jueves, Viernes, Sábado o Domingo. '))

        misterios = {
            'lunes': (
                'Misterios Gozosos',
                'Gozoso',
                'Gozosos'
            ),
            'sabado': (
                'Misterios Gozosos',
                'Gozoso',
                'Gozosos'
            ),
            'miercoles': (
                'Misterios Gloriosos',
                'Glorioso',
                'Gloriosos'
            ),
            'domingo': (
                'Misterios Gloriosos',
                'Glorioso',
                'Gloriosos'
            ),
            'martes': (
                'Misterios Dolorosos',
                'Doloroso',
                'Dolorosos'
            ),
            'viernes': (
                'Misterios Dolorosos',
                'Doloroso',
                'Dolorosos'
            ),
            'jueves': (
                'Misterios Luminosos',
                'Luminoso',
                'Luminosos'
            )
        }

        if dia not in misterios:
            print("No has introducido un día correcto. Vuelve a empezar el programa e introduce un día correcto.")
            return

        columna, nombre_misterio, nombre_misterios = misterios[dia]

        resar_rosari(
            Oraciones_Castellano,
            Misterios_Castellano,
            columna,
            nombre_misterios,
            nombre_misterio,
            'castellano'
        )

    elif que_rezar == 'via crucis':
        print('En proceso de desarrollo. Esta opción estará disponible en la próxima actualización del programa.')

    else:
        print("No has introducido una opción correcta. Vuelve a empezar el programa e introduce una opción correcta.")


idioma = normalizar(input('\nIdioma: Valencià o Castellano '))

if idioma == 'valencia':
    rosari_valencia()

elif idioma == 'castellano':
    rosario_castellano()

else:
    print("No has introducido un idioma correcto. Vuelve a empezar el programa e introduce un idioma correcto.")

# Gràcies de tot cor als meus pares.
# Nostre Senyor ens ampare.
# Salva.
