// Complete original outside202 primitive left mapper from paid1603 unit.
// Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
// All1632 Koszul equations and all1834 outside coordinates retained.
#include "2026-11-15-r150-saturated-global-common-789f.hpp"
#include <filesystem>
#include <csignal>
#include <cstring>
#include <iomanip>
#include <numeric>
#include <cmath>
using namespace sb;
namespace fs=std::filesystem;
static volatile std::sig_atomic_t stopping=0;
static void stop_signal(int){stopping=1;}
static void need(bool b,const std::string&s){if(!b)throw std::runtime_error(s);}
struct SHA {
 uint32_t h[8]={0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19};
 unsigned char buf[64];size_t used=0;uint64_t bytes=0;
 static uint32_t ro(uint32_t x,int n){return (x>>n)|(x<<(32-n));}
 void block(const unsigned char*b){
  static const uint32_t k[64]={0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2};
  uint32_t w[64];for(int i=0;i<16;i++)w[i]=(uint32_t(b[4*i])<<24)|(uint32_t(b[4*i+1])<<16)|(uint32_t(b[4*i+2])<<8)|b[4*i+3];
  for(int i=16;i<64;i++){uint32_t a=ro(w[i-15],7)^ro(w[i-15],18)^(w[i-15]>>3),c=ro(w[i-2],17)^ro(w[i-2],19)^(w[i-2]>>10);w[i]=w[i-16]+a+w[i-7]+c;}
  uint32_t a=h[0],b0=h[1],c=h[2],d=h[3],e=h[4],f=h[5],g=h[6],v=h[7];
  for(int i=0;i<64;i++){uint32_t s1=ro(e,6)^ro(e,11)^ro(e,25),ch=(e&f)^(~e&g),t1=v+s1+ch+k[i]+w[i],s0=ro(a,2)^ro(a,13)^ro(a,22),maj=(a&b0)^(a&c)^(b0&c),t2=s0+maj;v=g;g=f;f=e;e=d+t1;d=c;c=b0;b0=a;a=t1+t2;}
  h[0]+=a;h[1]+=b0;h[2]+=c;h[3]+=d;h[4]+=e;h[5]+=f;h[6]+=g;h[7]+=v;
 }
 void add(const void*p,size_t n){const auto*b=(const unsigned char*)p;bytes+=n;while(n){size_t z=std::min(n,64-used);memcpy(buf+used,b,z);used+=z;b+=z;n-=z;if(used==64){block(buf);used=0;}}}
 std::string finish(){uint64_t bits=bytes*8;unsigned char x=0x80;add(&x,1);x=0;while(used!=56)add(&x,1);unsigned char q[8];for(int i=0;i<8;i++)q[7-i]=(bits>>(8*i))&255;add(q,8);std::ostringstream s;s<<std::hex<<std::setfill('0');for(auto v:h)s<<std::setw(8)<<v;return s.str();}
};
static std::string file_sha(const std::string&p){
 std::ifstream f(p,std::ios::binary);need(bool(f),"open complete checkpoint");
 SHA h;char b[65536];while(f){f.read(b,sizeof b);auto n=f.gcount();if(n)h.add(b,size_t(n));}
 need(f.eof(),"read complete checkpoint");return h.finish();
}
static constexpr int NR=1834,NC=1632,NU=1603,NT=202,NH=231;
static int m31(int64_t x){x%=31;return x<0?int(x+31):int(x);}
static void save_field(const std::string&p,const char*magic,int d,int nr,int nc,const std::vector<uint8_t>&v,const std::string&binding){
 need(v.size()==size_t(nr)*nc&&binding.size()==64,"bound full matrix shape");
 std::ofstream o(p+".partial",std::ios::binary);o.write(magic,8);put(o,31,4);put(o,d,4);put(o,nr,4);put(o,nc,4);o.write(binding.data(),64);o.write((char*)v.data(),v.size());o.close();
 need(bool(o),"save complete field array");fs::rename(p+".partial",p);
}
static std::vector<uint8_t>load_field(const std::string&p,const char*magic,int d,int nr,int nc,const std::string&binding,const std::string&hash){
 need(file_sha(p)==hash,"complete layer SHA256");
 std::ifstream f(p,std::ios::binary);
 need(tag(f)==magic&&get(f,4)==31&&get(f,4)==uint64_t(d)&&get(f,4)==uint64_t(nr)&&get(f,4)==uint64_t(nc),"complete layer dimensions");
 char b[64];f.read(b,64);need(std::string(b,64)==binding,"complete layer semantic binding");
 std::vector<uint8_t>v(size_t(nr)*nc);f.read((char*)v.data(),v.size());need(bool(f),"complete layer payload");tail(f);
 need(std::all_of(v.begin(),v.end(),[](auto a){return a<31;}),"complete layer canonical field");return v;
}
struct Term{int row;uint8_t a;};
int main(int argc,char**argv){try{
 need(argc==7,"usage original-O-coefficients constant-inverse left-tail-heads prefix inclusive-degree remaining-seconds");
 auto started=std::chrono::steady_clock::now();
 auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count();};
 const std::string prefix=argv[4];int maximum=std::stoi(argv[5]);double limit=std::stod(argv[6]);
 need(maximum>=0&&maximum<=21&&std::isfinite(limit)&&limit>0&&limit<=1200,"finite complete original outside-left budget");
 std::signal(SIGTERM,stop_signal);std::signal(SIGINT,stop_signal);
 auto beat=[&](const std::string&s){std::cout<<std::setprecision(17)<<"{\"phase\":\""<<s<<"\",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;};
 std::ifstream h(argv[3],std::ios::binary);
 need(tag(h)=="R15OLH31"&&get(h,4)==31&&get(h,4)==1,"original outside-left heads magic/version");
 need(get(h,4)==uint64_t(maximum)&&get(h,4)==NH&&get(h,4)==NT,"complete231 by202 left head extent");
 char bb[64],pb[64];h.read(bb,64);h.read(pb,64);
 need(bool(h),"complete outside-left binding");std::string binding(bb,64),parentBinding(pb,64);
 std::vector<int>pr(NU),pc(NU),tr(NH),free(NT);std::set<int>rs,cs,fs0;
 for(auto&i:pr){i=get(h,2);need(i>=0&&i<NR&&rs.insert(i).second,"actual1603 original outside unit rows");}
 for(auto&i:pc){i=get(h,2);need(i>=0&&i<NC&&cs.insert(i).second,"actual1603 original Koszul unit columns");}
 for(auto&i:tr){i=get(h,2);need(i>=0&&i<NR&&rs.insert(i).second,"actual231 original outside tail rows");}
 need(rs.size()==NR,"whole1834 original outside row partition");
 for(auto&i:free){i=get(h,2);need(i>=0&&i<NH&&fs0.insert(i).second,"actual202 original outside free coordinates");}
 std::vector<std::vector<uint8_t>>heads(maximum+1,std::vector<uint8_t>(size_t(NH)*NT));
 for(int k=0;k<=maximum;k++){
  h.read((char*)heads[k].data(),heads[k].size());need(bool(h),"complete outside-left head payload");
  need(std::all_of(heads[k].begin(),heads[k].end(),[](auto v){return v<31;}),"canonical outside-left heads");
  for(int i=0;i<NT;i++)for(int j=0;j<NT;j++)
   need(heads[k][size_t(free[i])*NT+j]==int(k==0&&i==j),"all202 actual free left heads");
 }
 tail(h);
 const std::string headsSHA=file_sha(argv[3]),coeffSHA=file_sha(argv[1]),invSHA=file_sha(argv[2]);
 auto inverse=load_field(argv[2],"R15OIV31",0,NU,NU,parentBinding,invSHA);
 std::vector<uint8_t>inverseTranspose(inverse.size());
 for(int i=0;i<NU;i++)for(int j=0;j<NU;j++)inverseTranspose[size_t(i)*NU+j]=inverse[size_t(j)*NU+i];
 inverse.clear();inverse.shrink_to_fit();
 std::ifstream f(argv[1],std::ios::binary);
 need(tag(f)=="R15OAC31"&&get(f,4)==31&&get(f,4)==10&&get(f,4)==NR&&get(f,4)==NC,"complete original natural outside coefficients");
 char cb[64];f.read(cb,64);need(bool(f)&&std::string(cb,64)==parentBinding,"same original outside parent binding");
 std::vector<std::vector<std::vector<Term>>>O(11,std::vector<std::vector<Term>>(NC));
 uint64_t count=0;
 for(int k=0;k<=10;k++){
  uint64_t n=get(f,4);need(n<=uint64_t(NR)*NC,"bounded complete outside coefficient count");
  int previous=-1;
  for(uint64_t z=0;z<n;z++){
   int i=get(f,2),j=get(f,2),a=get(f,1);
   need(i>=0&&i<NR&&j>=0&&j<NC&&a>0&&a<31&&i*NC+j>previous,"complete unique original sparse outside coefficient order");
   previous=i*NC+j;O[k][j].push_back({i,uint8_t(a)});
  }count+=n;
 }
 tail(f);
 auto product=[&](const std::vector<uint8_t>&x,int k){
  need(x.size()==size_t(NR)*NT&&k>=0&&k<=10,"whole outside left product");
  std::vector<uint8_t>y(size_t(NC)*NT);
  for(int j=0;j<NC;j++){
   uint32_t q[NT]={0};
   for(auto t:O[k][j]){
    const auto*v=x.data()+size_t(t.row)*NT;
    for(int c=0;c<NT;c++)q[c]+=uint32_t(t.a)*v[c];
   }
   for(int c=0;c<NT;c++)y[size_t(j)*NT+c]=q[c]%31;
  }return y;
 };
 auto validate=[&](const std::vector<uint8_t>&x,int k){
  need(x.size()==size_t(NR)*NT,"complete1834 by202 original outside left mapper");
  for(int i=0;i<NH;i++)for(int j=0;j<NT;j++)
   need(x[size_t(tr[i])*NT+j]==heads[k][size_t(i)*NT+j],"all231 tail coordinates are the actual regular small mapper");
 };
 std::vector<std::vector<uint8_t>>L;
 struct Hashes{std::string l,r;};std::vector<Hashes>hashes;
 int completed=-1,restored=-1;const auto ledger=prefix+"-ledger.txt";
 if(fs::exists(ledger)){
  std::ifstream a(ledger);std::string lm,lb,lh,lc,li,lp;a>>lm>>lb>>lh>>lc>>li>>lp>>completed;
  need(lm=="R15OLLEDGER1"&&lb==binding&&lh==headsSHA&&lc==coeffSHA&&li==invSHA&&lp==parentBinding
       &&completed>=0&&completed<=maximum,"complete portable outside-left ledger");
  for(int k=0;k<=completed;k++){
   Hashes q;a>>q.l>>q.r;need(q.l.size()==64&&q.r.size()==64,"whole outside-left layer hashes");
   auto x=load_field(prefix+"-left-"+std::to_string(k)+".bin","R15OLX31",k,NR,NT,binding,q.l);validate(x,k);
   auto r=load_field(prefix+"-product-"+std::to_string(k)+".bin","R15OLR31",k,NC,NT,binding,q.r);
   need(std::all_of(r.begin(),r.end(),[](auto v){return v==0;}),"all restored original outside kernel products zero");
   L.push_back(std::move(x));hashes.push_back(q);
  }need(bool(a)&&!(a>>lm),"complete outside-left ledger tail");restored=completed;
 }
 auto commit=[&](int k,const std::vector<uint8_t>&x,const std::vector<uint8_t>&r){
  const auto lp=prefix+"-left-"+std::to_string(k)+".bin",rp=prefix+"-product-"+std::to_string(k)+".bin";
  save_field(lp,"R15OLX31",k,NR,NT,x,binding);save_field(rp,"R15OLR31",k,NC,NT,r,binding);
  hashes.push_back({file_sha(lp),file_sha(rp)});L.push_back(x);completed=k;
  std::ofstream a(ledger+".partial");
  a<<"R15OLLEDGER1 "<<binding<<" "<<headsSHA<<" "<<coeffSHA<<" "<<invSHA<<" "<<parentBinding<<" "<<completed<<"\n";
  for(auto q:hashes)a<<q.l<<" "<<q.r<<"\n";a.close();need(bool(a),"whole atomic outside-left ledger");fs::rename(ledger+".partial",ledger);
 };
 beat("actual-original-outside-left202-inputs-ready");
 for(int k=completed+1;k<=maximum;k++){
  if(stopping||elapsed()>limit-std::min(15.0,limit/5))break;
  std::vector<uint32_t>acc(size_t(NC)*NT);
  for(int d=1;d<=std::min(10,k);d++){
   auto r=product(L[k-d],d);for(size_t q=0;q<acc.size();q++)acc[q]+=r[q];
  }
  std::vector<uint8_t>x(size_t(NR)*NT);
  for(int i=0;i<NH;i++)for(int j=0;j<NT;j++)x[size_t(tr[i])*NT+j]=heads[k][size_t(i)*NT+j];
  auto rhs=product(x,0);for(size_t q=0;q<rhs.size();q++)rhs[q]=(rhs[q]+acc[q])%31;
  for(int a=0;a<NU;a++){
   int64_t q[NT]={0};
   for(int b=0;b<NU;b++)if(int v=inverseTranspose[size_t(a)*NU+b]){
    const auto*z=rhs.data()+size_t(pc[b])*NT;
    for(int j=0;j<NT;j++)q[j]-=int64_t(v)*z[j];
   }
   for(int j=0;j<NT;j++)x[size_t(pr[a])*NT+j]=m31(q[j]);
  }
  validate(x,k);auto r=product(x,0);
  for(size_t q=0;q<r.size();q++)r[q]=(r[q]+acc[q])%31;
  need(std::all_of(r.begin(),r.end(),[](auto v){return v==0;}),"all1632 original Koszul equations for complete outside-left202");
  commit(k,x,r);beat("complete-original-outside-left202-degree-"+std::to_string(k));
 }
 std::ofstream a(prefix+"-receipt.json");
 a<<std::setprecision(17)<<"{\"format\":\"isp-original-outside202-left-transport-v1\",\"status\":\""<<(completed==maximum?"completed":"checkpointed-time-budget")
  <<"\",\"inputBinding\":\""<<binding<<"\",\"parentOutsideBinding\":\""<<parentBinding
  <<"\",\"inputHeadsSHA256\":\""<<headsSHA<<"\",\"inputCoefficientsSHA256\":\""<<coeffSHA<<"\",\"inputInverseSHA256\":\""<<invSHA
  <<"\",\"field\":31,\"requestedMaximumDegree\":"<<maximum<<",\"completedDegree\":"<<completed<<",\"restoredCompletedDegree\":"<<restored
  <<",\"originalOutsideRows\":1834,\"originalKoszulColumns\":1632,\"leftKernelColumns\":202,\"actualConstantUnitRank\":1603"
  <<",\"all202OriginalFreeCoordinatesVerified\":"<<(completed>=0?"true":"false")
  <<",\"all1834OriginalOutsideCoordinatesRetained\":true"
  <<",\"all1632OriginalKoszulProductsZeroThroughCompletedDegree\":"<<(completed>=0?"true":"false")
  <<",\"originalProductCoordinatesVerified\":"<<uint64_t(completed+1)*NC*NT
  <<",\"allOriginalNaturalOutsideCoefficientCount\":"<<count
  <<",\"characteristicZeroOutsideLeftKernelComputed\":false,\"selectedLeadingCoefficientUnitProved\":false"
  <<",\"freeOriginalOutsideRowPositionsZeroBased\":[";
 for(int i=0;i<NT;i++){if(i)a<<",";a<<tr[free[i]];}
 a<<"],\"nativeSeconds\":"<<elapsed()<<"}\n";a.close();need(bool(a),"complete outside-left native receipt");
 beat(completed==maximum?"complete-original-outside202-left-mapper":"checkpointed-original-outside202-left-mapper");
 return completed==maximum?0:75;
}catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 1;}}
