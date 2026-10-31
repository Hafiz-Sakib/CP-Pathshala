#include <bits/stdc++.h>
using namespace std;

const int mx = 1e6 + 123;
vector<bool> is_prime(mx, 1);
vector<int> prime;

void Sieve(int n)
{
    is_prime[1] = 0;

    for (int i = 2; i <= n; i++)
    {
        for (int j = i + i; j <= n; j += i)
        {
            is_prime[j] = 0;
        }
    }
    for (int i = 1; i <= n; i++)
    {
        if (is_prime[i])
        {
            prime.push_back(i);
        }
    }
}

int main()
{

    // Time Complexity : O(n log n)

    Sieve(20);

    for (auto u : prime)
    {
        cout << u << ' ';
    }
    cout << endl;

    return 0;
}
