
import time
from sistema_puerta_perruna import SistemaPuertaPerruna


def main():
    sistema = SistemaPuertaPerruna()

    print("Bobby ladra dos veces para salir...")
    sistema.procesar_ladrido("Guau Guau")

    print("\nBobby está en el patio...")
    time.sleep(10)

    print("\nBobby termina de hacer sus cosas y vuelve a la puerta.")
    print("Bobby ladra dos veces para entrar...")
    time.sleep(1)
    sistema.procesar_ladrido("Guau Guau")

    print("\nBobby ha vuelto.")


if __name__ == "__main__":
    main()
