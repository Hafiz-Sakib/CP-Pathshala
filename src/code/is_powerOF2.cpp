#include <bits/stdc++.h>
using namespace std;
#define Boost                         \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL)
bool isPowerOFTwo(int x)
{
    return (x && (!(x & (x - 1))));
    // Time Complexity O(1)!
}
void Boom()
{
    int a = 512;

    if (isPowerOFTwo(a))
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
    }
}

int main()
{
    Boost;
    Boom();
    return 0;
}
