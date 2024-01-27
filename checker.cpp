#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <set>

#define ac 0xAC
#define wa 0xAD
#define pe 0xAE
#define tl 0xAF

using namespace std;

ifstream user("user.txt");
ifstream author("author.txt");
ifstream input("input.txt");


string nextToken(){
    string s;
    if(user >> s) return s;
    exit(pe);
}

long long nextLong(){
    long long n;
    if(user >> n) return n;
    exit(pe);
}

int nextInt(){
    int n;
    if(user >> n) return n;
    exit(pe);
}


void read(){
    // write code here ...
}

void write(){
    // write code here ...
}

int main(){
    input.tie(nullptr)->sync_with_stdio(false);
    user.tie(nullptr)->sync_with_stdio(false);
    author.tie(nullptr)->sync_with_stdio(false);
    read();
    write();
    return 0;
}