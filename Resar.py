import pandas as pd
from IPython.display import clear_output

Oracions_Valencia = pd.read_csv('Oracions_Valencia.csv')
Oraciones_Castellano = pd.read_csv('Oracions_Castellano.csv')
Misteris_Valencia = pd.read_csv('Misteris_Valencia.csv')
Misterios_Castellano = pd.read_csv('Misterios_Castellano.csv')

idioma = input('\n Idioma: Valencià o Castellano ').strip().lower()

#dia_cas = input('\n ¿Qué día es hoy? ').strip().lower()

#que_rezar_cas = input('\n ¿Qué quieres rezar? ').strip().lower()

# ----------- VALENCIÀ ------------

if idioma == 'valencià':
    que_resar_val = input('\n Què vols resar?: Rosari o Via Crucis').strip().lower()
    if que_resar_val == 'rosari':
        dia_val = input('\n Quin dia és hui?: Dilluns, Dimarts, Dimecres, Dijous, Divendres, Dissabte o Diumenge.').strip().lower()
        if dia_val == 'dilluns' or dia_val == 'dissabte':
            print("Perfecte! Anem a resar! Sols has de seguir les instruccions. \n")
            print("Comencem amb la senyal de la creu i l'acte de constricció: \n", Oracions_Valencia['Oracions'][0], "\n")
            print(Oracions_Valencia['Oracions'][1], "\n")

            print(Oracions_Valencia['Oracions'][2], "\n")
            print(Oracions_Valencia['Oracions'][3], "\n")
            print(Oracions_Valencia['Oracions'][4], "\n")

            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Ara anem a resar els misteris Gojosos. \n")

            for i in range(5):
                print(Misteris_Valencia['Orden'][i], " Gojós: ", Misteris_Valencia['Misteris Gojosos'][i], "\n")

                print("Pare nostre: ", Oracions_Valencia['Oracions'][5], "\n")
                print("10 voltes l'Ave Maria: ", Oracions_Valencia['Oracions'][6], "\n")
                print("Gloria: ", Oracions_Valencia['Oracions'][4], "\n")
                print("Jaculatòria: ", Oracions_Valencia['Oracions'][7], "\n")
                print("Oh, Jesús meu: ", Oracions_Valencia['Oracions'][8], "\n")

                pausa = input("Apreta Enter per continuar amb el Rosari. \n")
                clear_output(True)

            print("Anem a resar les Letanies a la Santíssima Verge: \n", Oracions_Valencia['Oracions'][9], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Invoquem al Corder de Déu: \n", Oracions_Valencia['Oracions'][10], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Demane'm: \n", Oracions_Valencia['Oracions'][11], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Per les intencions del Sant Pare: ", Oracions_Valencia['Oracions'][5], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)
            
            print("Un Ave Maria: ", Oracions_Valencia['Oracions'][6], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Un gloria: ", Oracions_Valencia['Oracions'][4], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Una Salve a la Verge: \n", Oracions_Valencia['Oracions'][12], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Jacaculatòria: \n", Oracions_Valencia['Oracions'][13], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

        elif dia_val == 'dimecres' or dia_val == 'diumenge':
            print("Perfecte! Anem a resar! Sols has de seguir les instruccions. \n")
            print("Comencem amb la senyal de la creu i l'acte de constricció: \n", Oracions_Valencia['Oracions'][0], "\n")
            print(Oracions_Valencia['Oracions'][1], "\n")

            print(Oracions_Valencia['Oracions'][2], "\n")
            print(Oracions_Valencia['Oracions'][3], "\n")
            print(Oracions_Valencia['Oracions'][4], "\n")

            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Ara anem a resar els misteris Gloriosos. \n")

            for i in range(5):
                print(Misteris_Valencia['Orden'][i], " Glorios: ", Misteris_Valencia['Misteris Gloriosos'][i], "\n")

                print("Pare nostre: ", Oracions_Valencia['Oracions'][5], "\n")
                print("10 voltes l'Ave Maria: ", Oracions_Valencia['Oracions'][6], "\n")
                print("Gloria: ", Oracions_Valencia['Oracions'][4], "\n")
                print("Jaculatòria: ", Oracions_Valencia['Oracions'][7], "\n")
                print("Oh, Jesús meu: ", Oracions_Valencia['Oracions'][8], "\n")

                pausa = input("Apreta Enter per continuar amb el Rosari. \n")
                clear_output(True)

            print("Anem a resar les Letanies a la Santíssima Verge: \n", Oracions_Valencia['Oracions'][9], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Invoquem al Corder de Déu: \n", Oracions_Valencia['Oracions'][10], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Demane'm: \n", Oracions_Valencia['Oracions'][11], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Per les intencions del Sant Pare: ", Oracions_Valencia['Oracions'][5], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)
            
            print("Un Ave Maria: ", Oracions_Valencia['Oracions'][6], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Un gloria: ", Oracions_Valencia['Oracions'][4], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Una Salve a la Verge: \n", Oracions_Valencia['Oracions'][12], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Jacaculatòria: \n", Oracions_Valencia['Oracions'][13], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

        elif dia_val == 'dimarts' or dia_val == 'divendres':
            print("Perfecte! Anem a resar! Sols has de seguir les instruccions. \n")
            print("Comencem amb la senyal de la creu i l'acte de constricció: \n", Oracions_Valencia['Oracions'][0], "\n")
            print(Oracions_Valencia['Oracions'][1], "\n")

            print(Oracions_Valencia['Oracions'][2], "\n")
            print(Oracions_Valencia['Oracions'][3], "\n")
            print(Oracions_Valencia['Oracions'][4], "\n")

            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Ara anem a resar els misteris Dolorosos. \n")

            for i in range(5):
                print(Misteris_Valencia['Orden'][i], " Dolorós: ", Misteris_Valencia['Misteris Dolorosos'][i], "\n")

                print("Pare nostre: ", Oracions_Valencia['Oracions'][5], "\n")
                print("10 voltes l'Ave Maria: ", Oracions_Valencia['Oracions'][6], "\n")
                print("Gloria: ", Oracions_Valencia['Oracions'][4], "\n")
                print("Jaculatòria: ", Oracions_Valencia['Oracions'][7], "\n")
                print("Oh, Jesús meu: ", Oracions_Valencia['Oracions'][8], "\n")

                pausa = input("Apreta Enter per continuar amb el Rosari. \n")
                clear_output(True)

            print("Anem a resar les Letanies a la Santíssima Verge: \n", Oracions_Valencia['Oracions'][9], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Invoquem al Corder de Déu: \n", Oracions_Valencia['Oracions'][10], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Demane'm: \n", Oracions_Valencia['Oracions'][11], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Per les intencions del Sant Pare: ", Oracions_Valencia['Oracions'][5], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)
            
            print("Un Ave Maria: ", Oracions_Valencia['Oracions'][6], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Un gloria: ", Oracions_Valencia['Oracions'][4], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Una Salve a la Verge: \n", Oracions_Valencia['Oracions'][12], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Jacaculatòria: \n", Oracions_Valencia['Oracions'][13], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

        elif dia_val == 'dijous':
            print("Perfecte! Anem a resar! Sols has de seguir les instruccions. \n")
            print("Comencem amb la senyal de la creu i l'acte de constricció: \n", Oracions_Valencia['Oracions'][0], "\n")
            print(Oracions_Valencia['Oracions'][1], "\n")

            print(Oracions_Valencia['Oracions'][2], "\n")
            print(Oracions_Valencia['Oracions'][3], "\n")
            print(Oracions_Valencia['Oracions'][4], "\n")

            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Ara anem a resar els misteris Lluminosos. \n")

            for i in range(5):
                print(Misteris_Valencia['Orden'][i], " Lluminos: ", Misteris_Valencia['Misteris Lluminosos'][i], "\n")

                print("Pare nostre: ", Oracions_Valencia['Oracions'][5], "\n")
                print("10 voltes l'Ave Maria: ", Oracions_Valencia['Oracions'][6], "\n")
                print("Gloria: ", Oracions_Valencia['Oracions'][4], "\n")
                print("Jaculatòria: ", Oracions_Valencia['Oracions'][7], "\n")
                print("Oh, Jesús meu: ", Oracions_Valencia['Oracions'][8], "\n")

                pausa = input("Apreta Enter per continuar amb el Rosari. \n")
                clear_output(True)

            print("Anem a resar les Letanies a la Santíssima Verge: \n", Oracions_Valencia['Oracions'][9], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Invoquem al Corder de Déu: \n", Oracions_Valencia['Oracions'][10], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Demane'm: \n", Oracions_Valencia['Oracions'][11], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Per les intencions del Sant Pare: ", Oracions_Valencia['Oracions'][5], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)
            
            print("Un Ave Maria: ", Oracions_Valencia['Oracions'][6], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Un gloria: ", Oracions_Valencia['Oracions'][4], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Una Salve a la Verge: \n", Oracions_Valencia['Oracions'][12], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

            print("Jacaculatòria: \n", Oracions_Valencia['Oracions'][13], "\n")
            pausa = input("Apreta Enter per continuar amb el Rosari. \n")
            clear_output(True)

        else:
            print("No has introduït un dia correcte. Torna a començar el programa i introdueix un dia correcte.")
            exit()

    elif que_resar_val == 'via crucis':
            print('En procés de desenvolupament. Esta opció estarà disponible a la pròxima actualització del programa.')

    else:
        print("No has introduït una opció correcta. Torna a començar el programa i introdueix una opció correcta.")
        exit()
else:
    print("No has introduït un idioma correcte. Torna a començar el programa i introdueix un idioma correcte.")
    exit()

#----------- CASTELLANO ----------

if idioma == 'castellano':
    que_rezar_cas = input('\n ¿Qué quieres rezar?: Rosario o Via Crucis').strip().lower()
    if que_rezar_cas == 'rosario':
        dia_cas = input('\n ¿Que día es hoy?: Lunes, Martes, Miercoles, Jueves, Viernes, Sábado o Domingo.').strip().lower()
        if dia_cas == 'lunes' or dia_cas == 'sabado':
            print("¡Perfecto! ¡Vamos a rezar! Sólo tienes que seguir las instrucciones.\n")
            print("Empezamos con la señal de la creu y el acto de contricción: \n", Oraciones_Castellano['Oraciones'][0], "\n")
            print(Oraciones_Castellano['Oraciones'][1], "\n")

            print(Oraciones_Castellano['Oraciones'][2], "\n")
            print(Oraciones_Castellano['Oraciones'][3], "\n")
            print(Oraciones_Castellano['Oraciones'][4], "\n")

            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Ahora vamos a rezar los misterios Gozosos. \n")

            for i in range(5):
                print(Misterios_Castellano['Orden'][i], " Gozoso: ", Misterios_Castellano['Misterios Gozosos'][i], "\n")

                print("Padre nuestro: ", Oraciones_Castellano['Oraciones'][5], "\n")
                print("10 veces el Ave Maria: ", Oraciones_Castellano['Oraciones'][6], "\n")
                print("Gloria: ", Oraciones_Castellano['Oraciones'][4], "\n")
                print("Jaculatoria: ", Oraciones_Castellano['Oraciones'][7], "\n")
                print("Oh, Jesús mío: ", Oraciones_Castellano['Oraciones'][8], "\n")

                pausa = input("Aprieta para continuar con el Rosario. \n")
                clear_output(True)

            print("Vamos a rezar las Letanías a la Santísima Virgen: \n", Oraciones_Castellano['Oraciones'][9], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Invocamos al Cordero de Dios: \n", Oraciones_Castellano['Oraciones'][10], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Pedimos: \n", Oraciones_Castellano['Oraciones'][11], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Por las intenciones del Santo Padre: ", Oraciones_Castellano['Oraciones'][5], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)
            
            print("Un Ave Maria: ", Oraciones_Castellano['Oraciones'][6], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Un gloria: ", Oraciones_Castellano['Oraciones'][4], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Una Salve a la Virgen: \n", Oraciones_Castellano['Oraciones'][12], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Jaculatoria: \n", Oraciones_Castellano['Oraciones'][13], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

        elif dia_cas == 'miercoles' or dia_cas == 'domingo':
            print("¡Perfecto! ¡Vamos a rezar! Sólo tienes que seguir las instrucciones.\n")
            print("Empezamos con la señal de la creu y el acto de contricción: \n", Oraciones_Castellano['Oraciones'][0], "\n")
            print(Oraciones_Castellano['Oraciones'][1], "\n")

            print(Oraciones_Castellano['Oraciones'][2], "\n")
            print(Oraciones_Castellano['Oraciones'][3], "\n")
            print(Oraciones_Castellano['Oraciones'][4], "\n")

            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Ahora vamos a rezar los misterios Gloriosos. \n")

            for i in range(5):
                print(Misterios_Castellano['Orden'][i], " Glorioso: ", Misterios_Castellano['Misterios Gloriosos'][i], "\n")

                print("Padre nuestro: ", Oraciones_Castellano['Oraciones'][5], "\n")
                print("10 veces el Ave Maria: ", Oraciones_Castellano['Oraciones'][6], "\n")
                print("Gloria: ", Oraciones_Castellano['Oraciones'][4], "\n")
                print("Jaculatoria: ", Oraciones_Castellano['Oraciones'][7], "\n")
                print("Oh, Jesús mío: ", Oraciones_Castellano['Oraciones'][8], "\n")

                pausa = input("Aprieta para continuar con el Rosario. \n")
                clear_output(True)

            print("Vamos a rezar las Letanías a la Santísima Virgen: \n", Oraciones_Castellano['Oraciones'][9], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Invocamos al Cordero de Dios: \n", Oraciones_Castellano['Oraciones'][10], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Pedimos: \n", Oraciones_Castellano['Oraciones'][11], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Por las intenciones del Santo Padre: ", Oraciones_Castellano['Oraciones'][5], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)
            
            print("Un Ave Maria: ", Oraciones_Castellano['Oraciones'][6], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Un gloria: ", Oraciones_Castellano['Oraciones'][4], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Una Salve a la Virgen: \n", Oraciones_Castellano['Oraciones'][12], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Jaculatoria: \n", Oraciones_Castellano['Oraciones'][13], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

        elif dia_cas == 'martes' or dia_cas == 'viernes':
            print("¡Perfecto! ¡Vamos a rezar! Sólo tienes que seguir las instrucciones.\n")
            print("Empezamos con la señal de la creu y el acto de contricción: \n", Oraciones_Castellano['Oraciones'][0], "\n")
            print(Oraciones_Castellano['Oraciones'][1], "\n")

            print(Oraciones_Castellano['Oraciones'][2], "\n")
            print(Oraciones_Castellano['Oraciones'][3], "\n")
            print(Oraciones_Castellano['Oraciones'][4], "\n")

            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Ahora vamos a rezar los misterios Dolorosos. \n")

            for i in range(5):
                print(Misterios_Castellano['Orden'][i], " Doloroso: ", Misterios_Castellano['Misterios Dolorosos'][i], "\n")

                print("Padre nuestro: ", Oraciones_Castellano['Oraciones'][5], "\n")
                print("10 veces el Ave Maria: ", Oraciones_Castellano['Oraciones'][6], "\n")
                print("Gloria: ", Oraciones_Castellano['Oraciones'][4], "\n")
                print("Jaculatoria: ", Oraciones_Castellano['Oraciones'][7], "\n")
                print("Oh, Jesús mío: ", Oraciones_Castellano['Oraciones'][8], "\n")

                pausa = input("Aprieta para continuar con el Rosario. \n")
                clear_output(True)

            print("Vamos a rezar las Letanías a la Santísima Virgen: \n", Oraciones_Castellano['Oraciones'][9], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Invocamos al Cordero de Dios: \n", Oraciones_Castellano['Oraciones'][10], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Pedimos: \n", Oraciones_Castellano['Oraciones'][11], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Por las intenciones del Santo Padre: ", Oraciones_Castellano['Oraciones'][5], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)
            
            print("Un Ave Maria: ", Oraciones_Castellano['Oraciones'][6], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Un gloria: ", Oraciones_Castellano['Oraciones'][4], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Una Salve a la Virgen: \n", Oraciones_Castellano['Oraciones'][12], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Jaculatoria: \n", Oraciones_Castellano['Oraciones'][13], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

        elif dia_cas == 'jueves':
            print("¡Perfecto! ¡Vamos a rezar! Sólo tienes que seguir las instrucciones.\n")
            print("Empezamos con la señal de la creu y el acto de contricción: \n", Oraciones_Castellano['Oraciones'][0], "\n")
            print(Oraciones_Castellano['Oraciones'][1], "\n")

            print(Oraciones_Castellano['Oraciones'][2], "\n")
            print(Oraciones_Castellano['Oraciones'][3], "\n")
            print(Oraciones_Castellano['Oraciones'][4], "\n")

            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Ahora vamos a rezar los misterios Luminosos. \n")

            for i in range(5):
                print(Misterios_Castellano['Orden'][i], " Luminoso: ", Misterios_Castellano['Misterios Luminosos'][i], "\n")

                print("Padre nuestro: ", Oraciones_Castellano['Oraciones'][5], "\n")
                print("10 veces el Ave Maria: ", Oraciones_Castellano['Oraciones'][6], "\n")
                print("Gloria: ", Oraciones_Castellano['Oraciones'][4], "\n")
                print("Jaculatoria: ", Oraciones_Castellano['Oraciones'][7], "\n")
                print("Oh, Jesús mío: ", Oraciones_Castellano['Oraciones'][8], "\n")

                pausa = input("Aprieta para continuar con el Rosario. \n")
                clear_output(True)

            print("Vamos a rezar las Letanías a la Santísima Virgen: \n", Oraciones_Castellano['Oraciones'][9], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Invocamos al Cordero de Dios: \n", Oraciones_Castellano['Oraciones'][10], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Pedimos: \n", Oraciones_Castellano['Oraciones'][11], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Por las intenciones del Santo Padre: ", Oraciones_Castellano['Oraciones'][5], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)
            
            print("Un Ave Maria: ", Oraciones_Castellano['Oraciones'][6], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Un gloria: ", Oraciones_Castellano['Oraciones'][4], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Una Salve a la Virgen: \n", Oraciones_Castellano['Oraciones'][12], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

            print("Jaculatoria: \n", Oraciones_Castellano['Oraciones'][13], "\n")
            pausa = input("Aprieta para continuar con el Rosario. \n")
            clear_output(True)

        else:
            print("No has introducido un día correcto. Vuelve a empezar el programa e introduce un día correcto.")
            exit()

    elif que_rezar_cas == 'via crucis':
        print('En proceso de desarrollo. Esta opción estará disponible en la próxima actualización del programa.')

    else:
        print("No has introducido una opción correcta. Vuelve a empezar el programa e introduce una opción correcta.")
        exit()
else:
    print("No has introducido un idioma correcto. Vuelve a empezar el programa e introduce un idioma correcto.")
    exit()
            



# Gràcies de tot cor als meus pares.
# Nostre Senyor ens ampare.
# Salva.