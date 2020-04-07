#include <iostream>
#include <cmath>

using namespace std;

double f(double x);

int main()
{
    double x;
    cin >> x;
    cout << f(x) << endl;

    return 0;
}

double f(double x)
{
    return 2*sin(x);
}