#include <iostream>
#include <random>
using namespace std;

int randint(int start, int end) {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dis(start, end);
    return dis(gen);
}

int main(){
    
}