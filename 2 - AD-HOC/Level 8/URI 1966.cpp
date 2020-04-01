#include <iostream>
#include <math.h>
#include <tuple>
#include <array>
#include <string>
#include <boost/algorithm/string.hpp>

using namespace std;


float ignoraDivisao0(int volume, int preco);
int calcularBase(int n);
int AVoltaParaCasa(int orcamento);
vector<int> converteInteiros(string v);

vector<tuple<float, int, int>> pecas;

bool sortbyfirst(const tuple<float, int, int>& a,  
               const tuple<float, int, int>& b) 
{ 
    return (get<0>(a) < get<0>(b)); 
} 

int main()
{
    tuple<float, int, int> peca; 

    int n, orcamento, quantPecas;
    float razao;
    string entrada;

    scanf("%d %d", &n, &orcamento);   

    vector<int> pecasVolume;
    vector<int> pecasPrecos;


    cin >> entrada;

    pecasPrecos = converteInteiros(entrada);

    cin >> entrada;

    pecasPrecos = converteInteiros(entrada);

    for (int i = 0; i < n; i++)
    {
        razao = ignoraDivisao0(pecasVolume[i], pecasPrecos[i]);

        peca = make_tuple(razao, pecasVolume[i], pecasPrecos[i]); 

        pecas.push_back(peca);
    }

    sort(pecas.begin(), pecas.end(), sortbyfirst); 

    quantPecas = AVoltaParaCasa(orcamento)
    
    int r =  calculaBase(quantPecas);
    cout << r << endl;

    return 0;
}

int AVoltaParaCasa(int orcamento)
{
    int quantVolume = 0;

    int fracaoRestante;

    for(tuple<float, int, int> i : pecas)
    {
        if (get<2>(i) <= orcamento)
        {   
            quantVolume += get<1>(i);
            orcamento -= get<2>(i);
        }
        else
        {
            fracaoRestante = get<2>(i) /  get<1>(i);

            quantVolume += orcamento * fracaoRestante;

            orcamento -= orcamento;

            break;
        }
    
    }    
    return quantVolume;
}

int calcularBase(int n)
{
   //formula do tringulo da com base N que tem nElementos = n(n+1)/2 entao ao resolver a equaçao do segundo grau
   //com a = c = 1 nos da o numero da base na raiz positiva (x1)

   int a, b, c, x1;

   a = 1;
   b = 1;
   c = -(2 * n);

   x1 = (-1 + floor(sqrt(1 + (-4 * c))))/ 2;

   return x1;

}

float ignoraDivisao0(int volume, int preco)
{
    if (volume == 0) return 0;

    else if (preco == 0) return INFINITY;

    else return preco /volume;
               
}


vector<int> converteInteiros(string v)
{   
    vector<int> v;
    char a =  string[0];;
    int number;
    string aux;
    for (int i = 1; i < string.length(); i++)
    {
        a = string[i];

        if (a == " " || a == ' ')
        {
            stringstream transfere(aux);
            transfere >> number;
            v.push_back(number);
            aux = "";
            continue
        }
        else
            aux += a; 
    }

    return v;
         
}