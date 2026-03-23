package co.edu.infracomp;

public class FibonacciThread implements Runnable {

    @Override
    public void run() {

        System.out.println("Primeros 100 números de Fibonacci:");

        long a = 0;
        long b = 1;

        for (int i = 0; i < 100; i++) {

            System.out.print(a + " ");

            long siguiente = a + b;
            a = b;
            b = siguiente;
        }

        System.out.println("\nFin cálculo Fibonacci\n");
    }
}
