package co.edu.infracomp;

public class Main {

    public static void main(String[] args) {
        Thread hilo = new Thread(new MiTarea());
        hilo.start();
    }
}
