#include <iostream>
#include <fstream>
using namespace std;
#include <vector>



int main() {
    int tamanho = 80000;
    int tamanho_coef = 100;
    //int k = 32;

// LEITURA DO ARQUIVO
    fstream arquivo;
    arquivo.open("sweep_20_3600.pcm", std::ios::in | std::ios::binary);
    if(!arquivo){
        cerr << "Unable to open file datafile.txt";
        exit(1);   // call system to stop
    }

    int contador = 0;
    float var, data[tamanho];
    while(contador < tamanho){
        arquivo.read((char *)&var, 2 );
        data[contador] = var;
        //cout << var << endl;
        contador++;
    }
    arquivo.close();


// LEITURA DOS COEFS
   float data_coef[tamanho_coef] = {
        #include "Coef_PB.dat"
        };



// FAZ A MEDIA
    vector<float> vals_media;
    float media[tamanho];

    for(int i = 0; i<tamanho_coef; i++){
        vals_media.push_back(0);
    }

    for( int i = 0; i < tamanho; i++){

        float media_atual = 0.0;
        for(int j=0; j<tamanho_coef; j++){
            media_atual = media_atual + ( float(vals_media[j]) * float(data_coef[j]) );
            if(media_atual>0){
                //cout<<"MED: " << media_atual << "  " << vals_media[j] << " * " << data_coef[j]<<endl;
            }
        }
        //cout<<"ESSA MEDIA: " << media_atual<<endl;

        media[i] = media_atual;

        vals_media.erase( vals_media.begin() );
        vals_media.push_back(data[i]);


    }


    ofstream arq_saida;
    arq_saida.open("saida.pcm", std::ios::out | std::ios::binary);
    for(int i=0; i<tamanho;i++){
        arq_saida.write( (char *)&media[i],sizeof(float));
    }
    arq_saida.close();

    return 0;
}
