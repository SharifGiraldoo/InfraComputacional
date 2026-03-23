package co.edu.infracomp;

public class MiTarea implements Runnable {

    @Override
    public void run() {
        System.out.println("Ejecutando tarea en hilo");
    }
}
