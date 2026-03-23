package co.edu.infracomp;

public class PrimosThread implements Runnable {

    @Override
    public void run() {

        int contador = 0;
        int numero = 2;

        System.out.println("Primeros 100 números primos:");

        while (contador < 100) {

            if (esPrimo(numero)) {
                System.out.print(numero + " ");
                contador++;
            }

            numero++;
        }

        System.out.println("\nFin cálculo primos\n");
    }

    private boolean esPrimo(int n) {

        if (n <= 1)
            return false;

        for (int i = 2; i <= Math.sqrt(n); i++) {

            if (n % i == 0)
                return false;
        }

        return true;
    }
}
