#include <iostream>
#include <filesystem>

using namespace std;

#define int long long

string to_4digit(int n) {
    string s = to_string(n);
    while (s.size() < 4) {
        s = "0" + s;
    }
    return s;
}

signed main() {

    string s;
    int k;
    #ifdef _WIN32
        system("g++ -o application input.cpp");
    #else
        system("g++ -o application.o input.cpp");
    #endif


    int starting_test, ending_test;
    cout << "Starting test: "; cin >> starting_test;
    if(starting_test < 1){
        return cout << "Error of number starting test" << endl, 0;
    }
    cout << "Ending test: "; cin >> ending_test;
    if(ending_test > 200){
        return cout << "Error of number ending test" << endl, 0;
    }


    string input_file;
    for(int i = starting_test; i <= ending_test; ++i){
        input_file = "tests/" + to_4digit(i) + ".in";

        #ifdef _WIN32
            s = ".\\application.exe > " + input_file;
        #else 
            s = "./application.o > " + input_file;
        #endif

        const char *arr = s.c_str();
        int k = system(arr);

        if(k == 0){
            cout << "Test " << to_4digit(i) << " OK" << endl;
        } else {
            cout << "Test " << to_4digit(i) << " ERROR Code " << k << endl;
        }
    }
}
