#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

// R409: exact first residues for the two actual six-sigma sources, b=1.
// Build: g++ -O3 -std=c++17 check-r409-joint-first-diagonal.cpp -o /tmp/r409
// Run: /tmp/r409 10000 > /tmp/r409.csv
// All arithmetic is in F_p, p=5 mod 6, p>7, through q^((p+1)/6-1).
// No coefficient through this order has a p denominator.
static std::pair<int, int> first_diagonals(int p) {
    const int nmax = (p + 1) / 6 - 1;
    std::vector<int64_t> inv(p, 0), x(nmax+1), a(nmax+1), b(nmax+1);
    std::vector<int64_t> c(nmax+1), d(nmax+1);
    inv[1] = 1;
    for (int i=2; i<p; ++i) inv[i] = (p-(p/i)*inv[p%i]%p)%p;
    x[0]=1; x[1]=(p-inv[7])%p;
    c[0]=d[0]=1;
    int64_t z1=1, z2=1, z3=1, z4=1, z5=1;
    int64_t tm2=2, tm1=(p-286%p)%p;
    auto pos=[p](int64_t v) { v%=p; return v<0?v+p:v; };
    for (int n=1; n<=nmax; ++n) {
        if (n>1) {
            int64_t sum=0;
            for (int i=1;i<n;++i) sum+=x[i]*x[n-i];
            x[n]=(sum%p)*inv[6*n+1]%p*inv[n-1]%p;
        }
        int64_t f=pos(-x[n]*inv[6*n]%p*inv[6*n-1]%p);
        z1=pos(-27*z1); z2=pos(-1728*z2); z3=64*z3%p;
        z4=pos(-19683*z4); z5=4096*z5%p;
        int64_t tn;
        if(n==1) tn=tm1;
        else { tn=pos(-286*tm1-117649*tm2); tm2=tm1; tm1=tn; }
        a[n]=n*f%p*pos(z1+z2+tn+1+z3)%p;
        b[n]=n*f%p*pos(z1+z2+tn+z4+z5)%p;
        int64_t cs=0, ds=0;
        for(int i=1;i<=n;++i) { cs+=a[i]*c[n-i]; ds+=b[i]*d[n-i]; }
        c[n]=(cs%p)*inv[n]%p; d[n]=(ds%p)*inv[n]%p;
    }
    return {int(c[nmax]),int(d[nmax])};
}

int main(int argc,char**argv) {
    int bound=argc>1?std::atoi(argv[1]):10000;
    if(bound<11 || bound>100000) return 2;
    std::vector<bool> prime(bound+1,true); prime[0]=prime[1]=false;
    for(int i=2;i*i<=bound;++i) if(prime[i])
        for(int j=i*i;j<=bound;j+=i) prime[j]=false;
    int total=0, both=0, szeros=0,tzeros=0;
    std::cout<<"p,S34,T72\n";
    for(int p=11;p<=bound;++p) if(prime[p] && p%6==5) {
        auto [a,b]=first_diagonals(p); ++total;
        if(a==0)++szeros; if(b==0)++tzeros;
        if(a==0 && b==0)++both;
        std::cout<<p<<','<<a<<','<<b<<'\n';
    }
    std::cerr<<"total="<<total<<" szeros="<<szeros<<" tzeros="<<tzeros<<" both="<<both<<"\n";
}
