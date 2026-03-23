package co.edu.infracomp;

public class TriangularesThread implements Runnable {

    @Override
    public void run() {

        System.out.println("Primeros 100 números triangulares:");

        for (int n = 1; n <= 100; n++) {

            int triangular = (n * (n + 1)) / 2;

            System.out.print(triangular + " ");
        }

        System.out.println("\nFin cálculo triangulares\n");
    }
}
