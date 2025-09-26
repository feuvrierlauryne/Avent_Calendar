#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
    int g,d;
    long long res1=0, res2=0;
    vector<int> ColG, ColD; 

    ifstream f("input1.txt"); // ouvre le fichier

    if (!f.is_open())
        cout << "Impossible d'ouvrir le fichier en lecture !" << endl;
    else
        while(f >> g >> d){
            ColG.push_back(g);
            ColD.push_back(d);
        }
    
    sort(ColG.begin(), ColG.end());
    sort(ColD.begin(), ColD.end());

    for(int i = 0; i < ColG.size();i++){
        res1+= abs(ColG[i]-ColD[i]);

        // Partie 2 
        int Counted_inD = count(ColD.begin(), ColD.end(), ColG[i]);
        res2+= ColG[i]*Counted_inD;
        
    }

    cout << res1 << endl;
    cout << res2 << endl;

    return 0;
}