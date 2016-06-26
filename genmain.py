mn = open ('main.cpp','w')
code = """
#include <iostream>
#include <stdlib.h>
using std::cout;

int max(int a, int b)
{
    return a>b?a:b;
}


int main(int argc, char** argv)
{
   int x,y;
   if(argc < 3){
        cout <<" Usage: a.exe v1 v2 where Vx are integers\\n";
        return -1;
    }
   cout << max(atoi(argv[1]),atoi(argv[2]));
   return 0;
}
"""
mn.write(code)
mn.close()
