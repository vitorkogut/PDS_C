#include <iostream>
#include <fstream>
#define T 5

using namespace std;

short int* lesweep(){
    std::fstream f_in;
        short speech, value[10000];


        f_in.open ("sweep_100_3k4.pcm", std::ios::in | std::ios::binary);


        int i = 0;
        while (i < 10000) {
            f_in.read((char *)&speech, 2);
                   value[i] = speech;
            cout << speech << std::endl;
            i++;
        }

        return value;
}
int main(void) {

    int i = 0;
	short int vetor[T] = lesweep();
	double mediaMovel[T], media = 0.0;
	printf("Valor:\n");
	while(i<5) {
        cin >> (vetor[i]);
		if (vetor[i]<0)
		{
			break;
		}
		else
		{
			mediaMovel[i] += (double)vetor[i];
			media += mediaMovel[i];
		}
		i++;
		if (i==T)
		{
			cout<<"Media Movel:"<< (media/T);
		}
	}
	return (0);
}
