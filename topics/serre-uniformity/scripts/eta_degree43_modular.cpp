#include <bits/stdc++.h>
using namespace std; using U=uint64_t;
const vector<string> gs={"-351643330","-181634213","26972100150","13843605713","-615241450575","-314344985758","6597209427096","3358230515416","-40542627535269","-20568043093764","159411803435470","80633423316371","-429721377031810","-216820614311075","831849342428810","418862136280342","-1194244952187508","-600343727043585","1300653911277333","652960441564111","-1091448273129748","-547342458917037","712705416840667","357097929861227","-363930604369013","-182217408061576","145335749598988","72727111706911","-45159020373021","-22587509701367","10792866388653","5396336469305","-1944212323820","-971797090418","255172444283","127514905483","-23015414551","-11499057732","1274935920","636891359","-32688421","-16327464"};
const vector<long long> fe={-43,3311,-76153,826804,-5167525,20764055,-57500460,115000920,-171655785,195747825,-173376645,120609840,-66335412,28915436,-9970840,2701776,-567987,90687,-10621,860,-43,1};
const vector<int> ee={1,29,24,8,17,20,21,7,31,39,13,33,11,18,6,2,15,5,16,34,40,42,14,19,35,26,23,22,36,12,4,30,10,32,25,37,41,28,38,27,9,3};

U pp;
U add(U a,U b){U x=a+b;return x>=pp?x-pp:x;}
U mul(U a,U b){return a*b%pp;}
U pw(U a,U n){U s=1;for(;n;n>>=1,a=mul(a,a))if(n&1)s=mul(s,a);return s;}
U inv(U a){if(!a)throw runtime_error("inverse 0");return pw(a,pp-2);}
U smod(string s){bool neg=s[0]=='-';U a=0;for(size_t i=neg;i<s.size();i++)a=(a*10+s[i]-'0')%pp;return neg&&a?pp-a:a;}
U signedmod(long long a){long long r=a%(long long)pp;return r<0?r+pp:r;}
bool prime(U n){if(n<2)return false;for(U a:{2,3,5,7,11,13,17,19,23,29,31,37}){if(n==a)return true;if(n%a==0)return false;}U old=pp;pp=n;U d=n-1,s=0;while(!(d&1)){d>>=1;s++;}for(U a:{2,3,5,7,11}){U x=pw(a,d);if(x==1||x==n-1)continue;bool ok=false;for(U j=1;j<s;j++){x=mul(x,x);if(x==n-1){ok=true;break;}}if(!ok){pp=old;return false;}}pp=old;return true;}
U eval(const vector<U>&a,U x){U s=0;for(int j=(int)a.size()-1;j>=0;j--)s=add(mul(s,x),a[j]);return s;}
vector<U> ringmul(const vector<U>&a,const vector<U>&b,U aa){vector<U> c(85);for(int i=0;i<43;i++)if(a[i])for(int j=0;j<43;j++)if(b[j])c[i+j]=add(c[i+j],mul(a[i],b[j]));for(int j=84;j>=43;j--)c[j-43]=add(c[j-43],mul(c[j],aa));c.resize(43);return c;}
vector<U> polynomial(U p){pp=p;U xi=0;for(U b=2;;b++){U x=pw(b,(p-1)/172);if(pw(x,86)!=1&&pw(x,4)!=1){xi=x;break;}}
vector<U> gg;for(auto&s:gs)gg.push_back(smod(s));vector<U> ff(43);for(int j=0;j<22;j++)ff[2*j]=signedmod(fe[j]);
vector<U> rr(42),h(42),aa(42),ww(42);rr[0]=add(xi,inv(xi));for(int l=0;l<42;l++){if(eval(ff,rr[l]))throw runtime_error("f root");h[l]=mul(eval(gg,rr[l]),pw(add(2,rr[l]?p-rr[l]:0),22));if(!h[l])throw runtime_error("h zero");U next=add(mul(3,rr[l]),p-mul(mul(rr[l],rr[l]),rr[l]));if(l<41)rr[l+1]=next;else if(next!=rr[0])throw runtime_error("r period");}
if(set<U>(rr.begin(),rr.end()).size()!=42)throw runtime_error("r distinct");
for(int l=0;l<42;l++){aa[l]=ww[l]=1;for(int j=0;j<42;j++){aa[l]=mul(aa[l],pw(h[(l+j)%42],ee[j]));int dd=(ee[(j+41)%42]-3*ee[j])/43;if(dd>0||dd<-2||43*dd!=ee[(j+41)%42]-3*ee[j])throw runtime_error("weight");ww[l]=mul(ww[l],pw(inv(h[(l+j)%42]),-dd));}}
for(int l=0;l<42;l++)if(aa[(l+1)%42]!=mul(pw(aa[l],3),pw(ww[l],43)))throw runtime_error("a sigma");
vector<U> cc(42,1),tt(43),cn(42);int k=1;for(int j=0;j<42;j++){if(tt[k])throw runtime_error("trace duplicate");tt[k]=cc[0];for(int l=0;l<42;l++)cn[l]=mul(mul(cc[(l+1)%42],pw(ww[l],k)),pw(aa[l],3*k/43));cc.swap(cn);k=3*k%43;}
if(k!=1||any_of(cc.begin(),cc.end(),[](U a){return a!=1;}))throw runtime_error("lift period");
vector<U> power(43),tr(44),out(44);power[0]=1;out[0]=1;for(int j=1;j<=43;j++){power=ringmul(power,tt,aa[0]);tr[j]=mul(43,power[0]);U s=0;for(int i=1;i<=j;i++)s=add(s,mul(out[j-i],tr[i]));out[j]=s?mul(p-s,inv(j)):0;}
if(out[1])throw runtime_error("trace nonzero");return out;}
int main(int argc,char**argv){int n=argc>1?stoi(argv[1]):1000;U start=argc>2?stoull(argv[2]):1000000000ULL;U p=start+(172-(start-1)%172)%172;for(int j=0;j<n;p+=172){if(!prime(p))continue;auto v=polynomial(p);cout<<p;for(U a:v)cout<<" "<<a;cout<<"\n";j++;}return 0;}
