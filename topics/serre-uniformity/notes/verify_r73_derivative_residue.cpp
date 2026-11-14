// Exact finite-field computation for R73; no external number-theory library.
// g++ -std=c++17 -O3 verify_r73_derivative_residue.cpp -o /tmp/verify_r73
// /tmp/verify_r73 > /tmp/r73-certificate.json
// Optional integer argument limits the number of lines (partial diagnostic only).
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <string>
#ifdef NDEBUG
#error "Compile without NDEBUG: this computation includes mathematical certificate checks."
#endif
constexpr int Q=49019, P=43, R=859, D=33;

// Only positive powers of q and division by small integers are needed.
// This minimal radix-2^32 integer keeps the program standard-library-only.
struct Big {
    std::vector<uint32_t> v;
    explicit Big(uint32_t n=0):v{n}{}
    void trim(){while(v.size()>1&&v.back()==0)v.pop_back();}
    void mul_small(uint32_t n){
        uint64_t carry=0;for(auto& a:v){uint64_t t=uint64_t(a)*n+carry;a=uint32_t(t);carry=t>>32;}
        if(carry)v.push_back(uint32_t(carry));
    }
    void add_one(){
        for(size_t i=0;;++i){if(i==v.size()){v.push_back(1);break;}if(++v[i]!=0)break;}
    }
    void sub_one(){
        size_t i=0;while(v[i]==0){v[i]=UINT32_MAX;++i;assert(i<v.size());}--v[i];trim();
    }
    uint32_t div_small(uint32_t n){
        uint64_t rem=0;for(size_t i=v.size();i-->0;){uint64_t t=(rem<<32)|v[i];v[i]=uint32_t(t/n);rem=t%n;}
        trim();return uint32_t(rem);
    }
    uint32_t mod(uint32_t n)const{Big t=*this;return t.div_small(n);}
    std::string bits()const{
        std::string s;bool started=false;
        for(size_t i=v.size();i-->0;)for(int j=31;j>=0;--j){bool b=(v[i]>>j)&1;if(b)started=true;if(started)s.push_back(b?'1':'0');}
        return s.empty()?"0":s;
    }
};

template<int M> struct F2 {
    int a=0,b=0;
    F2(long long x=0,long long y=0):a((x%M+M)%M),b((y%M+M)%M){}
    static F2 raw(int x,int y){F2 z;z.a=x;z.b=y;return z;}
    bool operator==(const F2& z)const{return a==z.a&&b==z.b;}
    bool operator!=(const F2& z)const{return !(*this==z);}
    bool zero()const{return a==0&&b==0;}
    F2 operator+(const F2& z)const{
        int x=a+z.a,y=b+z.b;if(x>=M)x-=M;if(y>=M)y-=M;return raw(x,y);
    }
    F2 operator-()const{return raw(a?M-a:0,b?M-b:0);}
    F2 operator-(const F2& z)const{return *this+(-z);}
    F2 operator*(const F2& z)const{
        long long x=(1LL*a*z.a-1LL*b*z.b)%M;
        long long y=(1LL*a*z.b+1LL*b*z.a)%M;
        if(x<0)x+=M;return raw(int(x),int(y));
    }
    static int power_int(int a,uint64_t n){
        int z=1;while(n){if(n&1)z=1LL*z*a%M;a=1LL*a*a%M;n>>=1;}return z;
    }
    F2 inv()const{
        int norm=(1LL*a*a+1LL*b*b)%M;assert(norm);
        int z=power_int(norm,M-2);
        return raw(1LL*a*z%M,b?M-int(1LL*b*z%M):0);
    }
    F2 operator/(const F2& z)const{return *this*z.inv();}
};
using C=F2<Q>; using Coeff=F2<P>; using RC=F2<R>;

template<class T,class N> T power(T a,N n){
    T z(1);while(n!=0){if((n&1)!=0)z=z*a;a=a*a;n>>=1;}return z;
}
template<class T> T power_bits(T a,const std::string& n){
    T z(1);for(char b:n){z=z*z;if(b=='1')z=z*a;}return z;
}
using Poly=std::vector<C>;
void trim(Poly& a){while(!a.empty()&&a.back().zero())a.pop_back();}
Poly psub(Poly a,const Poly& b){
    a.resize(std::max(a.size(),b.size()));
    for(size_t i=0;i<b.size();++i)a[i]=a[i]-b[i];trim(a);return a;
}
Poly pmul(const Poly& a,const Poly& b){
    if(a.empty()||b.empty())return {};
    Poly z(a.size()+b.size()-1);
    for(size_t i=0;i<a.size();++i)for(size_t j=0;j<b.size();++j)
        z[i+j]=z[i+j]+a[i]*b[j];trim(z);return z;
}
std::pair<Poly,Poly> pdiv(Poly a,const Poly& b){
    assert(!b.empty());trim(a);if(a.size()<b.size())return {{},a};
    Poly quotient(a.size()-b.size()+1);C inv=b.back().inv();
    while(a.size()>=b.size()){
        size_t k=a.size()-b.size();C t=a.back()*inv;quotient[k]=t;
        for(size_t j=0;j<b.size();++j)a[k+j]=a[k+j]-t*b[j];trim(a);
    }
    trim(quotient);return {quotient,a};
}
Poly pgcd(Poly a,Poly b){
    trim(a);trim(b);while(!b.empty()){auto qr=pdiv(a,b);a=b;b=qr.second;}return a;
}

// F_(q^2)[X]/(X^33+X+c), c in F_q.  The chosen polynomial is proved
// irreducible over F_q, hence also over F_(q^2), since gcd(33,2)=1.
int modulus_c=1;
struct Elt {
    std::array<C,D> a{};
    Elt(long long n=0){a[0]=C(n);}
    Elt(C n){a[0]=n;}
    static Elt x(){Elt z;z.a[1]=C(1);return z;}
    bool operator==(const Elt& z)const{return a==z.a;}
    bool operator!=(const Elt& z)const{return !(*this==z);}
    bool zero()const{for(auto z:a)if(!z.zero())return false;return true;}
    Elt operator+(const Elt& z)const{
        Elt r;for(int i=0;i<D;++i)r.a[i]=a[i]+z.a[i];return r;
    }
    Elt operator-()const{Elt r;for(int i=0;i<D;++i)r.a[i]=-a[i];return r;}
    Elt operator-(const Elt& z)const{return *this+(-z);}
    Elt operator*(const C& z)const{
        Elt r;for(int i=0;i<D;++i)r.a[i]=a[i]*z;return r;
    }
    Elt operator*(const Elt& z)const{
        std::array<C,2*D-1> t{};
        for(int i=0;i<D;++i)if(!a[i].zero())
            for(int j=0;j<D;++j)if(!z.a[j].zero())t[i+j]=t[i+j]+a[i]*z.a[j];
        C c(modulus_c);
        for(int k=2*D-2;k>=D;--k){t[k-D+1]=t[k-D+1]-t[k];t[k-D]=t[k-D]-t[k]*c;}
        Elt r;for(int i=0;i<D;++i)r.a[i]=t[i];return r;
    }
    Poly poly()const{Poly z(a.begin(),a.end());trim(z);return z;}
    static Poly modulus(){Poly f(D+1);f[0]=C(modulus_c);f[1]=C(1);f[D]=C(1);return f;}
    static Elt reduce(Poly t){
        if(t.size()>D){auto qr=pdiv(t,modulus());t=qr.second;}
        Elt z;for(size_t i=0;i<t.size();++i)z.a[i]=t[i];return z;
    }
    Elt inv()const{
        assert(!zero());Poly r0=modulus(),r1=poly(),s0{},s1{C(1)};
        while(!r1.empty()){
            auto qr=pdiv(r0,r1);Poly ns=psub(s0,pmul(qr.first,s1));
            r0=r1;r1=qr.second;s0=s1;s1=ns;
        }
        assert(r0.size()==1);C z=r0[0].inv();for(auto& v:s0)v=v*z;
        return reduce(s0);
    }
    Elt operator/(const Elt& z)const{return *this*z.inv();}
    C trace()const{return C(33)*a[0]-C(32)*a[32];}
};

bool irreducible(){
    Elt x=Elt::x(),h=x;
    for(int k=1;k<=33;++k){
        h=power(h,uint64_t(Q));
        if(k==3||k==11){auto g=pgcd((h-x).poly(),Elt::modulus());if(g.size()!=1)return false;}
    }
    return h==x;
}

template<class T> struct Point {
    T x{},y{};bool inf=true;
    Point()=default;Point(T a,T b):x(a),y(b),inf(false){}
    bool operator==(const Point& z)const{
        return inf==z.inf&&(inf||(x==z.x&&y==z.y));
    }
};
template<class T> struct Curve {
    T A,B;
    bool on(const Point<T>& p)const{
        return p.inf||p.y*p.y==p.x*p.x*p.x+A*p.x+B;
    }
    Point<T> add(const Point<T>& p,const Point<T>& r)const{
        if(p.inf)return r;if(r.inf)return p;T slope;
        if(p.x==r.x){
            if((p.y+r.y).zero())return {};
            assert(p.y==r.y);slope=(T(3)*p.x*p.x+A)/(T(2)*p.y);
        }else slope=(r.y-p.y)/(r.x-p.x);
        T x=slope*slope-p.x-r.x,y=slope*(p.x-x)-p.y;return {x,y};
    }
    template<class N> Point<T> mul(N n,Point<T> p)const{
        Point<T> z;while(n!=0){if((n&1)!=0)z=add(z,p);p=add(p,p);n>>=1;}return z;
    }
    Point<T> mul_bits(const std::string& n,const Point<T>& p)const{
        Point<T> z;for(char b:n){z=add(z,z);if(b=='1')z=add(z,p);}return z;
    }
};

bool square_root(const Elt& a,const Big& field_size,Elt& answer){
    if(a.zero()){answer=Elt();return true;}
    Big d=field_size;d.sub_one();uint32_t rem=d.div_small(8);assert(rem==0&&d.v[0]%2==1);
    Elt t=power_bits(a,d.bits());if(power(t,uint64_t(4))!=Elt(1))return false;
    Big e=d;e.add_one();rem=e.div_small(2);assert(rem==0);Elt x=power_bits(a,e.bits());
    uint64_t cexp=d.mod(uint32_t(1ULL*Q*Q-1));
    Elt c(power(C(1,1),cexp));int m=3;
    while(t!=Elt(1)){
        int i=0;Elt z=t;while(z!=Elt(1)&&i<m){z=z*z;++i;}assert(i<m);
        Elt b=power(c,uint64_t(1)<<(m-i-1));x=x*b;c=b*b;t=t*c;m=i;
    }
    assert(x*x==a);answer=x;return true;
}

struct IsogenyData {Curve<C> curve;std::array<Point<C>,3> images;};
IsogenyData velu(const std::vector<Point<Elt>>& orbit_representatives,
                 const std::array<Point<C>,3>& inputs){
    C sum_t,sum_w;std::array<C,3> sx{},sy{};
    for(const auto& point:orbit_representatives){
        assert(!point.inf);Elt u=point.x,uu=u*u,uuu=uu*u;
        Elt t=uu*C(6)-Elt(2),v2=uuu-u,w=uuu*C(10)-u*C(6);
        sum_t=sum_t+t.trace();sum_w=sum_w+w.trace();
        for(int j=0;j<3;++j){
            Elt d=(Elt(inputs[j].x)-u).inv(),d2=d*d;
            sx[j]=sx[j]+(t*d+(v2*d2)*C(4)).trace();
            sy[j]=sy[j]+(t*d2+((v2*d2)*d)*C(8)).trace();
        }
    }
    IsogenyData z{{C(-1)-C(5)*sum_t,-C(7)*sum_w},{}};
    for(int j=0;j<3;++j){
        z.images[j]={inputs[j].x+sx[j],inputs[j].y*(C(1)-sy[j])};
        assert(z.curve.on(z.images[j]));
    }
    assert(z.curve.mul(P,z.images[1]).inf&&z.curve.mul(P,z.images[2]).inf);
    assert(z.curve.mul(4,z.images[0]).inf&&!z.curve.mul(2,z.images[0]).inf);
    return z;
}

C psi11(const Curve<C>& e,const Point<C>& point){
    C x=point.x,y=point.y,x2=x*x,x3=x2*x,x4=x2*x2,x6=x3*x3;
    C A=e.A,B=e.B,A2=A*A;
    C H=x6+C(5)*A*x4+C(20)*B*x3-C(5)*A2*x2-C(4)*A*B*x-C(8)*B*B-A2*A;
    C p2=C(2)*y,p3=C(3)*x4+C(6)*A*x2+C(12)*B*x-A2,p4=C(2)*p2*H;
    C p5=p4*p2*p2*p2-p3*p3*p3;
    C p6=p2*p3*(p5-C(4)*H*H);
    C p7=p5*p3*p3*p3-p2*p4*p4*p4;
    return p7*p5*p5*p5-p4*p6*p6*p6;
}

struct PsiValues {
    const Curve<C>& e;Point<C> point;std::array<C,13> v{};std::array<bool,13> set{};
    PsiValues(const Curve<C>& ee,Point<C> pp):e(ee),point(pp){
        C x=pp.x,y=pp.y,A=e.A,B=e.B,x2=x*x,x3=x2*x,x4=x2*x2,x6=x3*x3;
        v[0]=C();v[1]=C(1);v[2]=C(2)*y;
        v[3]=C(3)*x4+C(6)*A*x2+C(12)*B*x-A*A;
        v[4]=C(4)*y*(x6+C(5)*A*x4+C(20)*B*x3-C(5)*A*A*x2-C(4)*A*B*x-C(8)*B*B-A*A*A);
        for(int i=0;i<=4;++i)set[i]=true;
    }
    C get(int n){
        if(set[n])return v[n];int m=n/2;C z;
        if(n&1)z=get(m+2)*power(get(m),uint64_t(3))-get(m-1)*power(get(m+1),uint64_t(3));
        else z=get(m)*(get(m+2)*power(get(m-1),uint64_t(2))-get(m-2)*power(get(m+1),uint64_t(2)))/get(2);
        set[n]=true;return v[n]=z;
    }
};

uint32_t key(C z){return uint32_t(z.a)+uint32_t(Q)*z.b;}
uint64_t point_key(const Point<C>& z){
    return uint64_t(z.x.a)|(uint64_t(z.x.b)<<16)|(uint64_t(z.y.a)<<32)|(uint64_t(z.y.b)<<48);
}
std::array<std::array<Coeff,P>,P> weights;
std::unordered_map<uint32_t,int> log_q;
Coeff character_sum(const IsogenyData& iso){
    const auto& e=iso.curve;
    std::array<Point<C>,P> a,b,trans;
    for(int j=1;j<P;++j){a[j]=e.add(a[j-1],iso.images[1]);b[j]=e.add(b[j-1],iso.images[2]);}
    for(int j=0;j<P;++j)trans[j]=e.add(iso.images[0],a[j]);
    Coeff total;std::unordered_set<uint64_t> seen;seen.reserve(P*P*2);
    for(int u=0;u<P;++u)for(int v=0;v<P;++v){
        if(u==0&&v==0)continue;auto point=e.add(trans[u],b[v]);
        assert(!point.inf&&e.on(point)&&seen.insert(point_key(point)).second);
        C value=psi11(e,point);assert(!value.zero());
        C residue=power(value,uint64_t((1ULL*Q*Q-1)/P));
        auto it=log_q.find(key(residue));assert(it!=log_q.end());
        total=total+weights[u][v]*Coeff(it->second);
        if((u==0&&v==1)||(u==1&&v==0)||(u==1&&v==1)){
            PsiValues psi(e,point);assert(psi.get(11)==value);
            auto npoint=e.mul(11,point);assert(!npoint.inf);
            assert(npoint.x==point.x-psi.get(10)*psi.get(12)/(value*value));
        }
    }
    assert(seen.size()==P*P-1);return total;
}

void print_c(C z){std::cout<<'['<<z.a<<','<<z.b<<']';}
void print_f(const Elt& z){
    std::cout<<'[';for(int i=0;i<D;++i){if(i)std::cout<<',';print_c(z.a[i]);}std::cout<<']';
}
bool prime(int n){if(n<2)return false;for(int j=2;1LL*j*j<=n;++j)if(n%j==0)return false;return true;}

int main(int argc,char** argv){
    int limit=argc>1?std::stoi(argv[1]):R+1;assert(limit>0&&limit<=R+1);
    assert(prime(Q)&&prime(P)&&prime(R)&&Q%(4*P)==4*P-1&&R%(4*P)==4*P-1);
    auto start=std::chrono::steady_clock::now();
    while(!irreducible()){++modulus_c;assert(modulus_c<Q);}
    std::cerr<<"irreducible X^33+X+"<<modulus_c<<"\n";
    Elt test=Elt::x()+Elt(C(2,3));assert(test*test.inv()==Elt(1));
    Big n(1),field_size(1);for(int i=0;i<D;++i)n.mul_small(Q);
    for(int i=0;i<2*D;++i)field_size.mul_small(Q);n.add_one();Big cofactor=n;
    uint32_t cofactor_remainder=cofactor.div_small(R);assert(cofactor_remainder==0);
    Curve<Elt> extension_curve{Elt(-1),Elt(0)};Point<Elt> rr;int seed_shift=0;
    for(;;++seed_shift){
        Elt x=Elt::x()+Elt(seed_shift),y;
        if(!square_root(x*x*x-x,field_size,y))continue;
        rr=extension_curve.mul_bits(cofactor.bits(),Point<Elt>(x,y));
        if(!rr.inf)break;
    }
    assert(extension_curve.on(rr)&&extension_curve.mul(R,rr).inf);
    Point<Elt> sr(-rr.x,rr.y*C(0,1));assert(extension_curve.on(sr));
    int lambda=(R-Q%R)%R;
    auto fr=extension_curve.mul(lambda,rr);
    assert(power(rr.x,uint64_t(1ULL*Q*Q))==fr.x&&power(rr.y,uint64_t(1ULL*Q*Q))==fr.y);
    std::cerr<<"r-torsion point found, seed shift "<<seed_shift<<"\n";
    std::vector<int> subgroup;int t=1;
    do{subgroup.push_back(t);subgroup.push_back(R-t);t=1LL*t*lambda%R;}while(t!=1);
    assert(subgroup.size()==66);std::array<bool,R> covered{};std::vector<int> reps;
    for(int k=1;k<R;++k)if(!covered[k]){
        reps.push_back(k);for(int h:subgroup)covered[1LL*k*h%R]=true;
    }
    assert(reps.size()==13);
    std::vector<Point<Elt>> rows,steps;
    for(int k:reps){rows.push_back(extension_curve.mul(k,rr));steps.push_back(extension_curve.mul(k,sr));}
    auto initial=rows;
    Curve<C> original{C(-1),C(0)};
    std::array<Point<C>,3> inputs={Point<C>(C(0,1),C(1,-1)),
        Point<C>(C(11536),C(29305)),Point<C>(C(-11536),C(0,29305))};
    for(auto z:inputs)assert(original.on(z));assert(original.mul(P,inputs[1]).inf);
    C zeta=power(C(2,1),uint64_t((1ULL*Q*Q-1)/P));assert(zeta!=C(1));
    C z=C(1);for(int j=0;j<P;++j){assert(!log_q.count(key(z)));log_q[key(z)]=j;z=z*zeta;}assert(z==C(1));
    for(int u=0;u<P;++u)for(int v=0;v<P;++v)if(u||v)weights[u][v]=Coeff(u,v)/Coeff(u*u+v*v);
    RC zeta_r=power(RC(2,1),uint64_t((1ULL*R*R-1)/P));assert(zeta_r!=RC(1));
    std::unordered_map<int,int> log_r;RC zr(1);
    for(int j=0;j<P;++j){log_r[zr.a+R*zr.b]=j;zr=zr*zeta_r;}assert(zr==RC(1)&&log_r.size()==P);
    Coeff weighted,unweighted;std::vector<std::array<int,4>> line_values;
    for(int s=0;s<limit;++s){
        RC line=s==R?RC(0,1):RC(1,s);
        RC character=power(line,uint64_t((1ULL*R*R-1)/P));
        auto it=log_r.find(character.a+R*character.b);assert(it!=log_r.end());int j=it->second;
        auto iso=velu(s==R?steps:rows,inputs);Coeff value=character_sum(iso);
        weighted=weighted+Coeff(j)*value;unweighted=unweighted+value;
        line_values.push_back({s,j,value.a,value.b});
        if(s<R)for(size_t k=0;k<rows.size();++k)rows[k]=extension_curve.add(rows[k],steps[k]);
        if((s+1)%20==0||s+1==limit){
            auto elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
            std::cerr<<"lines "<<s+1<<" partial "<<weighted.a<<','<<weighted.b<<" seconds "<<elapsed<<"\n";
        }
    }
    if(limit==R+1){assert(rows==initial);assert(unweighted.zero());}
    Coeff scaled=Coeff(8)/Coeff(7)*weighted;
    std::cout<<"{\"p\":"<<P<<",\"q\":"<<Q<<",\"r\":"<<R
             <<",\"complete\":"<<(limit==R+1?"true":"false")
             <<",\"modulus_c\":"<<modulus_c<<",\"seed_shift\":"<<seed_shift
             <<",\"lambda\":"<<lambda<<",\"torsion_x\":";print_f(rr.x);
    std::cout<<",\"torsion_y\":";print_f(rr.y);
    std::cout<<",\"scalar_orbit_representatives\":[";
    for(size_t k=0;k<reps.size();++k){if(k)std::cout<<',';std::cout<<reps[k];}
    std::cout<<"],\"zeta_q\":";print_c(zeta);
    std::cout<<",\"zeta_r\":["<<zeta_r.a<<','<<zeta_r.b<<"],\"Z\":["<<weighted.a<<','<<weighted.b
             <<"],\"R65_raw_derivative_coordinate\":["<<scaled.a<<','<<scaled.b
             <<"],\"unweighted_sum\":["<<unweighted.a<<','<<unweighted.b<<"],\"lines\":[";
    for(size_t k=0;k<line_values.size();++k){
        if(k)std::cout<<',';auto row=line_values[k];std::cout<<'['<<row[0]<<','<<row[1]<<','<<row[2]<<','<<row[3]<<']';
    }
    std::cout<<"]}\n";
}
