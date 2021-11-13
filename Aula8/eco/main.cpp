#include <iostream>
#include <fstream>
using namespace std;


int main()
{
    fstream arquivo;
    arquivo.open("impulsoun.pcm", std::ios::in | std::ios::binary);

    if(!arquivo){
        cerr << "Não conseguiu abrir o arquivo";
        exit(1);
    }

    int tamanho = 80;
    int i = 0;
    short var, data[tamanho];
    float d, a0, a1;
    short saida[tamanho];


    while(i < tamanho){
        arquivo.read((char *)&var, 2 );
        data[i] = var;
        i++;
    }


    cout<<"D: "<<endl;
    cin>>d;
    cout<<"A0: "<<endl;
    cin>>a0;
    cout<<"A1: "<<endl;
    cin>>a1;


    for (int i=0; i<tamanho; i++){
        saida[i] = 0;
        saida[i] = (a0*data[i] + (a1*data[i- int(d)])) + data[i + int(d)];
    }

    ofstream arq_saida;
    arq_saida.open("saida.pcm", std::ios::out | std::ios::binary);
    for(int i=0; i<tamanho;i++){
        arq_saida.write((char *)&saida[i], 2 );
    }
    arq_saida.close();

    return 0;

}
