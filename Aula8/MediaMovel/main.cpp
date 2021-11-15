#include <stdio.h>
#include <fcntl.h>
#include <io.h>
#define tamanho_coef 1764

int main() {
    FILE *in_file, *out_file;
    int i, n, amostras;

    short entrada, saida;
    short data[tamanho_coef] = {0x0};
    float y = 0;

    float coef[tamanho_coef] = {
        #include "Coef_RF.dat" // Coeficiente
    };


    if ((in_file = fopen("RDI.wav", "rb")) == NULL){ // Sinal de entrada
        printf("\nErro: Não abriu o arquivo de entrada\n");
        return 0;
    }

    if ((out_file = fopen("saida.pcm", "wb")) == NULL){ // Sinal de saida
        printf("\nErro: Não abriu o arquivo de saida\n");
        return 0;
    }

    for (i = 0; i < tamanho_coef; i++){
        data[i] = 0;
    }

    do {
        y = 0;
        amostras = fread(&entrada, sizeof(short), 1, in_file);
        data[0] = entrada;
        for (n = 0; n < tamanho_coef; n++){
                y += coef[n] * data[n];
        }
        for (n = tamanho_coef - 1; n > 0; n--){
                data[n] = data[n - 1];
        }
        saida = (short)y;

        fwrite(&saida, sizeof(short), 1, out_file);
    } while (amostras);

    fclose(out_file);
    fclose(in_file);

    return 0;
}
