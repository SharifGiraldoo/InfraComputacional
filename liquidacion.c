

#include <stdio.h>

int main() {

    double salario_base = 2000000.0;
    double dias_laborados = 200.0;

    double prima = (salario_base * dias_laborados) / 360.0;
    double cesantias = (salario_base * dias_laborados) / 360.0;
    double vacaciones = (salario_base * dias_laborados) / 720.0;
    double intereses_cesantias = cesantias * 0.12 * (dias_laborados / 360.0);

    double total = prima + cesantias + vacaciones + intereses_cesantias;

    printf("Prima: %.2f\n", prima);
    printf("Cesantías: %.2f\n", cesantias);
    printf("Vacaciones: %.2f\n", vacaciones);
    printf("Intereses Cesantías: %.2f\n", intereses_cesantias);
    printf("Total Liquidación: %.2f\n", total);

    return 0;
}