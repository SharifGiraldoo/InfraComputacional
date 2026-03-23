public class Liquidacion {

    public static void main(String[] args) {

        float salarioBase = 2000000;
        float diasLaborados = 300;
        float prima = (salarioBase * diasLaborados) /360;
        float cesantias = (salarioBase * diasLaborados) / 360;
        float vacaciones = (salarioBase * diasLaborados) / 720;
        float interesesCesantias = (float) (((cesantias * 0.12)*diasLaborados)/360);
        float total = prima + cesantias+vacaciones+interesesCesantias;
        System.out.println("El salario total es: " + Math.round(total));
    }

}
