#include <bits/stdc++.h>
using namespace std;
#define Boost                         \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL)

void Boom()
{
    int a = 1024;

    int x = a >> 1; // It means (a/2^1)
    int y = a >> 4; // It means (a/2^4)
    int z = a >> 6; // It means (a/2^6)
    int n = a >> 8; // It means (a/2^8)

    cout << x << ' ' << y << ' ' << z << ' ' << n << ' ' << endl;
}

int main()
{
    Boost;
    Boom();
    return 0;
}
