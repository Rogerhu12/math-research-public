// Exact modular search in the actual square three-block evaluation.
// This finds finite test objects; it is not evidence for infinitely many primes.
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;
using Vec = vector<int>;

struct Series {
    int n, p;
    Vec one;
    Series(int n_, int p_) : n(n_), p(p_), one(n,0) { one[0]=1; }
    int mod(long long x) const { x%=p; return x<0 ? x+p : x; }
    int invc(int x) const {
        int a=mod(x), e=p-2, out=1;
        while(e) { if(e&1) out=mod(1LL*out*a); a=mod(1LL*a*a); e>>=1; }
        return out;
    }
    Vec add(const Vec&a,const Vec&b) const {
        Vec c(n); for(int i=0;i<n;i++)c[i]=mod(a[i]+b[i]); return c;
    }
    Vec scale(const Vec&a,int x) const {
        Vec c(n); for(int i=0;i<n;i++)c[i]=mod(1LL*a[i]*x); return c;
    }
    Vec mul(const Vec&a,const Vec&b) const {
        Vec c(n,0);
        for(int i=0;i<n;i++)if(a[i])for(int j=0;j<n-i;j++)
            c[i+j]=mod(c[i+j]+1LL*a[i]*b[j]);
        return c;
    }
    Vec inverse(const Vec&a) const {
        Vec c(n,0); c[0]=invc(a[0]);
        for(int i=1;i<n;i++) {
            long long z=0; for(int j=1;j<=i;j++)z=(z+1LL*a[j]*c[i-j])%p;
            c[i]=mod(-z*c[0]);
        }
        return c;
    }
    Vec power(Vec a,int e) const {
        if(e<0) { a=inverse(a); e=-e; }
        Vec c=one;
        while(e) { if(e&1)c=mul(c,a); e>>=1; if(e)a=mul(a,a); }
        return c;
    }
    Vec logarithm(const Vec&a) const {
        Vec d(n,0); for(int i=0;i<n-1;i++)d[i]=mod(1LL*(i+1)*a[i+1]);
        d=mul(d,inverse(a)); Vec c(n,0);
        for(int i=1;i<n;i++)c[i]=mod(1LL*d[i-1]*invc(i));
        return c;
    }
    Vec exponential(const Vec&a) const {
        Vec c=one;
        for(int i=1;i<n;i++) {
            long long z=0; for(int j=1;j<=i;j++)z=(z+1LL*j*a[j]%p*c[i-j])%p;
            c[i]=mod(z*invc(i));
        }
        return c;
    }
};

int angle_bound(int n) {
    int m=n+1;
    return 3*((3*m+3)/4)+2*((m+1)/2)+(2*m+2)/3-2;
}
int source_rank(int D,int J) {
    int N=0; for(int n=0;n<=D;n++)N+=angle_bound(n)+1;
    return N*(J+1);
}
bool prime(int p) {
    if(p<2)return false;
    for(int d=2;d*d<=p;d++)if(p%d==0)return false;
    return true;
}
int rank_mod(vector<Vec> a,int p) {
    Series S(1,p);
    int nr=a.size(),nc=a[0].size(),r=0;
    for(int c=0;c<nc && r<nr;c++) {
        int pos=r; while(pos<nr && a[pos][c]==0)pos++;
        if(pos==nr)continue;
        swap(a[pos],a[r]); int ip=S.invc(a[r][c]);
        for(int i=r+1;i<nr;i++)if(a[i][c]) {
            int f=S.mod(1LL*a[i][c]*ip);
            for(int j=c;j<nc;j++)a[i][j]=S.mod(a[i][j]-1LL*f*a[r][j]);
        }
        r++;
    }
    return r;
}

int check(int p,int D,int J,int ell) {
    int s=(p+1)/6, L=2*s+ell, N=source_rank(D,J);
    Series A(s+1,p);
    Vec X=A.one; X[1]=A.mod(-A.invc(7));
    for(int n=2;n<=s;n++) {
        long long c=0; for(int i=1;i<n;i++)c=(c+1LL*X[i]*X[n-i])%p;
        X[n]=A.mod(c*A.invc((6*n+1)*(n-1)%p));
    }
    Vec F(s+1,0);
    for(int n=1;n<s;n++)F[n]=A.mod(-1LL*X[n]*A.invc(6*n*(6*n-1)%p));
    int ap=A.mod(-34LL*X[s]*A.invc(6*s));
    Vec t(s+1,0),ix=A.power(X,-3);
    for(int n=1;n<=s;n++)t[n]=A.mod(-ix[n-1]);
    Vec theta=A.exponential(A.add(A.logarithm(X),A.scale(F,2)));
    Vec d=A.add(A.one,A.scale(t,8)),tm1=A.add(t,A.scale(A.one,-1));
    Vec h=A.add(A.add(A.scale(A.one,7),A.scale(t,4)),A.scale(A.power(t,2),16));
    Vec f=A.scale(A.mul(A.mul(A.mul(t,tm1),h),d),A.invc(7));
    Vec V=A.mul(
        A.mul(A.add(A.one,A.scale(t,-4)),A.add(A.add(A.one,A.scale(t,-20)),A.scale(A.power(t,2),-8))),
        A.add(A.add(A.add(A.one,A.scale(t,96)),A.scale(A.power(t,2),48)),A.scale(A.power(t,3),-64)));
    Vec R=A.mul(A.power(theta,17),d),T=A.mul(A.power(theta,36),A.mul(f,V));
    Vec S=A.mul(A.power(theta,17),f);
    vector<Vec> rp(D+1,A.one),tp(J+1,A.one);
    for(int n=1;n<=D;n++)rp[n]=A.mul(rp[n-1],R);
    for(int j=1;j<=J;j++)tp[j]=A.mul(tp[j-1],T);
    vector<Vec> mat(L,Vec(N,0)); int col=0;
    int alpha=A.mod(36LL*A.invc(17));
    for(int n=0;n<=D;n++) {
        int aa=(n+1)/4,bb=(n+1)/3,cc=n/2;
        Vec q=A.mul(A.mul(A.power(A.mul(t,h),aa),A.power(tm1,bb)),A.power(d,-cc));
        Vec base=A.mul(rp[n],q);
        for(int k=0;k<=angle_bound(n);k++) {
            for(int j=0;j<=J;j++,col++) {
                Vec H=A.mul(base,tp[j]);
                int charge=A.mod(n+1LL*alpha*j),gauss=A.mod(1LL*charge*ap);
                int gauss2=A.mod(1LL*gauss*gauss*A.invc(2));
                for(int r=0;r<s;r++) {
                    mat[r][col]=H[r];
                    mat[s+r][col]=A.mod(1LL*H[r]*gauss);
                    if(r<ell)mat[2*s+r][col]=A.mod(1LL*H[r]*gauss2);
                }
            }
            base=A.mul(base,t);
        }
    }
    int rank=rank_mod(mat,p);
    if(rank<N) {
        cout<<"{\"p\":"<<p<<",\"D\":"<<D<<",\"J\":"<<J<<",\"ell\":"<<ell
            <<",\"N\":"<<N<<",\"rank_bar_J\":"<<rank<<",\"S_first\":"<<S[s]
            <<",\"T_first\":"<<T[s]<<"}"<<endl;
    }
    return N-rank;
}

int main(int argc,char**argv) {
    if(argc==6 && string(argv[1])=="--one") {
        int p=atoi(argv[2]),D=atoi(argv[3]),J=atoi(argv[4]),ell=atoi(argv[5]);
        int s=(p+1)/6;
        if(!prime(p) || p<=83 || p%6!=5 || ell<1 || ell>=s-13 || source_rank(D,J)!=2*s+ell)
            return 2;
        int defect=check(p,D,J,ell);
        cerr<<"p="<<p<<" D="<<D<<" J="<<J<<" ell="<<ell<<" defect="<<defect<<endl;
        return 0;
    }
    int maxD=argc>1?atoi(argv[1]):5, maxJ=argc>2?atoi(argv[2]):2;
    int stopAfter=argc>3?atoi(argv[3]):1, checked=0,found=0;
    int minD=argc>4?atoi(argv[4]):2, minJ=argc>5?atoi(argv[5]):0;
    for(int D=minD;D<=maxD;D++)for(int J=minJ;J<=maxJ;J++) {
        int N=source_rank(D,J);
        for(int p=max(89,2*N+26);p<=3*N-4;p++)if(p%6==5 && prime(p)) {
            int s=(p+1)/6,ell=N-2*s;
            if(!(1<=ell && ell<s-13))continue;
            checked++;
            if(check(p,D,J,ell)) {
                found++;
                if(found>=stopAfter) { cerr<<"checked="<<checked<<" defects="<<found<<endl; return 0; }
            }
        }
        cerr<<"completed D="<<D<<" J="<<J<<" checked="<<checked<<" defects="<<found<<endl;
    }
    cerr<<"checked="<<checked<<" defects="<<found<<endl;
}
