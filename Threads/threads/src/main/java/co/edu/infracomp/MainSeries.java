package co.edu.infracomp;

public class MainSeries {

    public static void main(String[] args) {

        Thread primos = new Thread(new PrimosThread());
        Thread fibonacci = new Thread(new FibonacciThread());
        Thread triangulares = new Thread(new TriangularesThread());

        primos.start();
        fibonacci.start();
        triangulares.start();
    }
}