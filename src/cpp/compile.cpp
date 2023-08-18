#include <ctime>
#include <iomanip>
#include <filesystem>
#include <iostream>
using namespace std;


string to_4digit(int n) {
    string s = to_string(n);
    while (s.size() < 4) {
        s = "0" + s;
    }
    return s;
}


int main(){
    string s;
    int k, task_id;
    double mx_time, time_taken;
    clock_t start, end;
    #ifdef _WIN32
        system("g++ -o application main.cpp");
    #else
        system("g++ -o application.o main.cpp");
    #endif
    int i = 1;
    string input = "tests/" + to_4digit(i) + ".in";
    string output = "tests/" + to_4digit(i) + ".out";
    while(filesystem::exists(input)){
        #ifdef _WIN32
            s = ".\\application.exe < " + input + " > " + output;
        #else 
            s = "./application.o < " + input + " > " + output;
        #endif
        const char *arr = s.c_str();

        start = clock();
        int k = system(arr);
        end = clock();

        double time_taken = double(end - start)/double(CLOCKS_PER_SEC);

        if(k == 0){
            cout << "Test " << to_4digit(i) << " OK Time " << fixed << time_taken << setprecision(5) << " sec\n";

            if(mx_time < time_taken){
                task_id = i;
                mx_time = time_taken;
            }

        } else {
            cout << "Test " << to_4digit(i) << " ERROR Code " << k << endl;
        }
        ++i;
        input = "tests/" + to_4digit(i) + ".in";
        output = "tests/" + to_4digit(i) + ".out";
    }
    cout << "\nThe slowest task is " << to_4digit(task_id) << " Time: " << fixed << mx_time << setprecision(5) << " sec\n";
}