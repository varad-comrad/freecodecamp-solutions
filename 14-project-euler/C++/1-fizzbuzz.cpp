#include <iostream>
#include <cstdlib>
#include <map>

using namespace std;

int main(int argc, char **argv){
    map<int, string> mp;
    mp[3] = "Fizz";
    mp[5] = "Buzz";

    // if i%3 = 0 or i%5 = 0:
    // mp[i%15]

    for(int i=1; i<=stoi(argv[1]); i++){
        string aux = "";
        for(auto x: mp){
            if(i%x.first == 0) 
                aux+=x.second;
        }
        if(aux.empty())
            aux += to_string(i);
        cout << aux << endl;
    }
}