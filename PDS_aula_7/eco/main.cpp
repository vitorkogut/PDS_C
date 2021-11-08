#include <iostream>
#include <fstream>
using namespace std;


int main()
{
    fstream arquivo;
    arquivo.open("impulsoun.pcm", std::ios::in | std::ios::binary);

    if(!arquivo){
        cerr << "Unable to open file datafile.txt";
        exit(1);   // call system to stop
    }

    int tamanho = 80; // tamanho definido ao gerar o impulso
    int contador = 0;
    short var, data[tamanho];


    cout<< "ENTRADA:" << endl;
    while(contador < tamanho){
        arquivo.read((char *)&var, 2 );
        data[contador] = var;
        cout << var << "|";
        contador++;
    }



    float d=2, a0=0.5, a1=0.3;


    short saida[tamanho];

    cout<< endl << "SAIDA: " << endl;
    for (int i=0; i<tamanho; i++){
        saida[i] = 0;
        saida[i] = (a0*data[i] + (a1*data[i- int(d)])) + data[i + int(d)];
        cout<<saida[i] << "|";
    }

    ofstream arq_saida;
    arq_saida.open("saida.pcm", std::ios::out | std::ios::binary);
    for(int i=0; i<tamanho;i++){
        arq_saida.write((char *)&saida[i], 2 );
    }
    arq_saida.close();

    return 0;

}
