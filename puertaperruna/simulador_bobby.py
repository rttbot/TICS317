import time
from sistema_puerta_perruna import SistemaPuertaPerruna
#import pdb; pdb.set_trace()


def main():
    puerta = SistemaPuertaPerruna()

    print("Bobby ladra dos veces para salir y espera atentamente a que se abra la puerta...")
 

    if puerta.procesar_ladrido("Guau Guau"):
        print("\nBobby ya está en el patio haciendo sus cosas....")
        time.sleep(10)

        print("\nBobby termina de hacer sus cosas y vuelve a la puerta.")
        print("Bobby ladra dos veces para entrar...")
        time.sleep(1)
        contador = 0   
        volvio = True
        while not puerta.procesar_ladrido("Guau Guau"):
            time.sleep(1)
            contador += 1
            if contador > 10:
                print("Parece que Bobby no volverá.")
                volvio = False
                break
        if volvio:
            print("\nBobby ha vuelto.") 
    else:
        print("La puerta se abrió, pero parece que Bobby se arrepintió.")


if __name__ == "__main__":
    main()
