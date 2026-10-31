#include <bits/stdc++.h>
using namespace std;
#define Boost                         \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL)

void Boom()
{
    int a = 100;

    if (a & 1)
    {
        cout << "Odd Number" << endl;
    }
    else
    {
        cout << "Even Number" << endl;
    }
}

int main()
{
    Boost;
    Boom();
    return 0;
}
