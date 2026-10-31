/*

string author;
author = Hafiz_Sakib;

*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
#define endl "\n"
#define ll long long int
#define ignore cin.ignore(numeric_limits<streamsize>::max(), '\n')
#define Boost                         \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL)

#define debug(x) cerr << x << endl;
#define here fprintf(stderr, "====I am Here====\n");

void Boom()
{
    ll n;
    cin >> n;
    if (n == 2)
    {
        cout << "YaaY ! Prime Number" << endl;
    }
    for (ll i = 3; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            cout << "OPPS ! Not a Prime Number" << endl;
            return;
        }
    }
    cout << "YaaY ! Prime Number" << endl;
}

int main()
{
    Boost;

    int t = 1;
    while (t--)
    {
        Boom();
    }

    return 0;
}
