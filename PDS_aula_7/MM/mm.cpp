#include <iostream>
#include <fstream>
using namespace std;
#include <vector>



int main() {
    int tamanho = 80000;
    int k = 32;

// LEITURA DO ARQUIVO
    fstream arquivo;
    arquivo.open("sweep_20_3600.pcm", std::ios::in | std::ios::binary);
    if(!arquivo){
        cerr << "Unable to open file datafile.txt";
        exit(1);   // call system to stop
    }

    int contador = 0;
    short var, data[tamanho];
    while(contador < tamanho){
        arquivo.read((char *)&var, 2 );
        data[contador] = var;
        //cout << var << endl;
        contador++;
    }
    arquivo.close();

// FAZ A MEDIA
    vector<short> vals_media;
    short media[tamanho];

    for(int i = 0; i<k; i++){
        vals_media.push_back(0);
    }

    for( int i = 0; i < tamanho; i++){

        short media_atual = 0;
        for(int j=0; j<k; j++){
            media_atual = media_atual + vals_media[j];
        }

        media_atual = media_atual / k;
        media[i] = media_atual;

        vals_media.erase( vals_media.begin() );
        vals_media.push_back(data[i]);
    }


    ofstream arq_saida;
    arq_saida.open("saida.pcm", std::ios::out | std::ios::binary);
    for(int i=0; i<tamanho;i++){
        arq_saida.write((char *)&media[i], 2 );
    }
    arq_saida.close();

    return 0;
}
