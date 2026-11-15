// Complete original202 high-source back-substitution from the paid4340 constant DAG.
// Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
// Reverse transposeSolve exactly; all4367 original products retained at every degree.
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
static constexpr int NS=6188,NC=4367,NP=3333,SC=1034,NB=1007,NT=202,NR=1848,W=(NC+31)/32,SW=(SC+31)/32;
struct Op{int id=0,a=0;};
struct Forward{int raw=0,scale=1,pivot=-1,ordinal=0;std::vector<Op>ops;};
struct Backward{int id=0;std::vector<Op>ops;};
struct Term{int c=0;uint8_t a=0;};
static int m31(int64_t x){x%=31;return x<0?int(x+31):int(x);}
static void addmul(BitOps&ops,Row&a,const Row&b,int words,int f){
 f=m31(f);if(!f)return;auto r=ops.rep[f];
 BitOps::add(a,words,0,b,words,0,words,r.rot,r.neg);
 if(r.c)BitOps::add(a,words,0,b,words,0,words,(r.rot+(r.c==1?1:2))%5,r.neg);
}
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
int main(int argc,char**argv){try{
 need(argc==10,"usage model prepared-full-profile forward backward full-operations high-heads prefix inclusive-degree remaining-seconds");
 auto started=std::chrono::steady_clock::now();
 auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count();};
 int maximum=std::stoi(argv[8]);double limit=std::stod(argv[9]);
 need(maximum>=1&&maximum<=21&&std::isfinite(limit)&&limit>0&&limit<=1200,"finite original dual-jet budget");
 std::signal(SIGTERM,stop_signal);std::signal(SIGINT,stop_signal);
 const std::string prefix=argv[7];
 auto beat=[&](const std::string&s){std::cout<<std::setprecision(17)<<"{\"phase\":\""<<s<<"\",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;};
 Model M(argv[1]);
 std::ifstream profile(argv[2]);std::string magic,binding;int n;
 profile>>magic>>binding>>n;need(magic=="R150_FULL_NATURAL_U_DUAL31_V2"&&binding.size()==64&&n==NB,"complete original full profile");
 std::array<std::array<int,4>,SC>paid{};
 for(int k=0;k<NB;k++){int c,i,r,a;profile>>c>>i>>r>>a;need(c>=1&&c<=SC&&!paid[c-1][0]&&i>=1&&i<=2855&&r>=1&&r<=NS&&a>0&&a<31,"paid full pivot dictionary");paid[c-1]={c,i,r,a};}
 profile>>n;need(n==4,"paid full connecting rank");
 std::array<std::array<int,4>,SC>paidConn{};
 for(int k=0;k<4;k++){int c,i,r,a;profile>>c>>i>>r>>a;need(c>=1&&c<=SC&&!paid[c-1][0]&&!paidConn[c-1][0]&&a>0&&a<31,"paid connecting dictionary");paidConn[c-1]={c,i,r,a};}
 need(bool(profile)&&!(profile>>magic),"complete prepared profile tail");
 std::set<int>preRaw,preOut;
 std::unordered_map<int,uint64_t>prePivot;
 for(const auto&r:M.pre){need(preRaw.insert(r.raw).second&&preOut.insert(M.component.at(r.pivot)).second,"unique original prebasis");prePivot[r.raw]=r.pivot;}
 need(preRaw.size()==NP&&preOut.size()==NP,"complete3333 prebasis");
 std::vector<int>components,remainingOriginal;
 for(int c=0;c<NC;c++)if(!preOut.count(c))components.push_back(c);
 for(int r=1;r<=NS;r++)if(!preRaw.count(r))remainingOriginal.push_back(r);
 need(components.size()==SC&&remainingOriginal.size()==2855,"full original source/output complements");
 std::vector<uint64_t>termkeys(M.var.begin(),M.var.end());
 for(auto[i,j]:M.quadratic)termkeys.push_back(M.var[i]+M.var[j]);
 std::vector<std::vector<std::vector<Term>>>A(11,std::vector<std::vector<Term>>(NS+1));
 uint64_t coefficientCount=0;
 for(int raw=1;raw<=NS;raw++){
  int e=(raw-1)%17;auto mul=M.multipliers[(raw-1)/17];
  for(int j=0;j<77;j++)for(int d=0;d<=10;d++){
   int a=0;
   if(e<11){if(j<11)a=M.L[e][j][10-d];else if(d==0)a=M.Q[e][j-11];}
   else if(j>=11&&d<=5)a=M.G[e-11][j-11][5-d];
   if(a){A[d][raw].push_back({M.component.at(mul+termkeys[j]),uint8_t(a)});coefficientCount++;}
  }
 }
 auto rawrow=[&](int raw){Row x(5*W);for(auto t:A[0][raw])BitOps::set(x,W,t.c,t.a);return x;};
 std::ifstream f(argv[3],std::ios::binary),b(argv[4],std::ios::binary);
 need(tag(f)=="R150PB31"&&get(f,4)==NP&&tag(b)=="R150RJ31"&&get(b,4)==NP,"paid prebasis DAG headers");
 std::vector<Forward>F(NP+1);std::array<int,NP+1>pivot{};
 uint64_t fc=0,bc=0;
 std::set<int>seenPre;
 for(int id=1;id<=NP;id++){
  auto&r=F[id];r.raw=get(f,4);r.scale=get(f,1);int count=get(f,4);
  need(preRaw.count(r.raw)&&seenPre.insert(r.raw).second&&r.scale>0&&r.scale<31&&count>=0&&count<NP,"paid prebasis source record");
  pivot[id]=M.component.at(prePivot.at(r.raw));
  for(int j=0;j<count;j++){Op a{int(get(f,2)),int(get(f,1))};need(a.id>0&&a.id<id&&a.a>0&&a.a<31,"paid forward source operation");r.ops.push_back(a);}fc+=count;
 }
 tail(f);std::vector<Backward>B(NP);std::set<int>seenBackward;
 for(auto&r:B){
  r.id=get(b,2);int count=get(b,4);need(r.id>0&&r.id<=NP&&seenBackward.insert(r.id).second&&count>=0&&count<NP,"paid backward source record");
  for(int j=0;j<count;j++){Op a{int(get(b,2)),int(get(b,1))};need(a.id>0&&a.id<=NP&&a.id!=r.id&&a.a>0&&a.a<31,"paid backward operation");r.ops.push_back(a);}bc+=count;
 }
 tail(b);need(fc==782976&&bc==1010703,"all paid prebasis operations");
 BitOps ops;std::vector<Row>phi(NP+1);
 for(int id=1;id<=NP;id++){
  Row x=rawrow(F[id].raw);for(auto a:F[id].ops)addmul(ops,x,phi[a.id],W,-a.a);ops.multiple(x,W,0,F[id].scale);phi[id]=std::move(x);
 }
 for(const auto&r:B)for(auto a:r.ops)addmul(ops,phi[r.id],phi[a.id],W,-a.a);
 std::vector<int>preOrder(NP);std::iota(preOrder.begin(),preOrder.end(),1);
 std::sort(preOrder.begin(),preOrder.end(),[&](int i,int j){return pivot[i]<pivot[j];});
 uint64_t preTailNonzeros=0;int largestPreDegreeDrop=0;
 for(int i=1;i<=NP;i++)for(int j=1;j<=NP;j++){
  int v=BitOps::get(phi[i],W,pivot[j]);
  if(i==j)need(v==1,"all3333 original prebasis diagonal units");
  else if(v){
   need(pivot[j]>pivot[i],"full natural prebasis principal block is unit upper triangular");
   int drop=degree(M.keys[pivot[i]])-degree(M.keys[pivot[j]]);
   need(drop>0,"all natural prebasis offdiagonal tails strictly lower moment degree");
   preTailNonzeros++;largestPreDegreeDrop=std::max(largestPreDegreeDrop,drop);
  }
 }
 std::vector<std::vector<std::pair<int,uint8_t>>>phiFull(NP+1);
 for(int id=1;id<=NP;id++)for(int c=0;c<NC;c++){int a=BitOps::get(phi[id],W,c);if(a)phiFull[id].push_back({c,uint8_t(a)});}
 auto normal=[&](Row&x,std::vector<uint8_t>&co){
  co.assign(NP+1,0);
  for(int id:preOrder){int a=BitOps::get(x,W,pivot[id]);if(a){co[id]=a;addmul(ops,x,phi[id],W,-a);}}
  for(int id=1;id<=NP;id++)need(!BitOps::get(x,W,pivot[id]),"all original prebasis output cancellations");
 };
 std::ifstream dag(argv[5],std::ios::binary);
 need(tag(dag)=="R150IJ31"&&get(dag,4)==2855&&get(dag,4)==SC,"paid full1007 operations header");
 std::vector<Forward>G(1);std::array<int,SC>componentId{};
 std::vector<std::pair<int,int>>zeroRows;uint64_t gc=0,pc=0,qc=0;
 for(int idx=1;idx<=2855;idx++){
  need(dag.get()=='I'&&get(dag,2)==uint64_t(idx)&&get(dag,2)==uint64_t(remainingOriginal[idx-1]),"all2855 original paid source records");
  Forward r;r.raw=remainingOriginal[idx-1];r.ordinal=idx;
  while(true){
   int c=dag.get();
   if(c=='R'){int p=int(get(dag,2))-1,a=dag.get();need(p>=0&&p<SC&&componentId[p]&&a>0&&a<31,"available full constant source reduction");r.ops.push_back({componentId[p],a});gc++;}
   else if(c=='B'){
    int p=int(get(dag,2))-1;
    need(p>=0&&p<SC&&!componentId[p]&&paid[p][0]&&paid[p][1]==idx&&paid[p][2]==r.raw,"same full constant source witness");
    r.pivot=p;r.scale=paid[p][3];componentId[p]=G.size();G.push_back(std::move(r));break;
   }else if(c=='Z'){zeroRows.push_back({idx,r.raw});break;}
   else throw std::runtime_error("invalid full constant DAG opcode");
  }
 }
 need(G.size()==NB+1&&zeroRows.size()==NR&&gc==1203382,"complete full constant source DAG counts");
 std::set<int>connSeen;
 for(auto[idx,raw]:zeroRows){
  need(dag.get()=='J'&&get(dag,2)==uint64_t(idx)&&get(dag,2)==uint64_t(raw),"paid full connecting original record");
  while(true){
   int op=dag.get();
   if(op=='P'||op=='Q'){int c=int(get(dag,2))-1,a=dag.get();need(c>=0&&c<SC&&a>0&&a<31,"paid connecting reduction coefficient");
    if(op=='P'){need(componentId[c]!=0,"paid connecting original coker projection");pc++;}
    else{need(connSeen.count(c),"available connecting pivot");qc++;}
   }else if(op=='C'){int c=int(get(dag,2))-1;need(c>=0&&c<SC&&paidConn[c][0]&&paidConn[c][1]==idx&&paidConn[c][2]==raw&&connSeen.insert(c).second,"paid connecting witness");break;}
   else if(op=='0')break;
   else throw std::runtime_error("invalid paid connecting opcode");
  }
 }
 tail(dag);need(pc==925214&&qc==926&&connSeen.size()==4,"complete paid connecting DAG audit");
 std::vector<Row>P(NB+1);std::vector<std::vector<uint8_t>>H(NB+1);
 std::vector<std::vector<std::pair<int,uint8_t>>>psparse(NB+1);
 std::set<int>unitSource=preRaw,unitOutput=preOut;
 for(int id=1;id<=NB;id++){
  const auto&r=G[id];need(unitSource.insert(r.raw).second&&unitOutput.insert(components[r.pivot]).second,"distinct full unit sources/outputs");
  Row x=rawrow(r.raw);normal(x,H[id]);Row y(5*SW);
  for(int c=0;c<SC;c++)BitOps::set(y,SW,c,BitOps::get(x,W,components[c]));
  for(auto a:r.ops)addmul(ops,y,P[a.id],SW,-a.a);
  for(int c=0;c<r.pivot;c++)need(!BitOps::get(y,SW,c),"paid full basis original leading component");
  need(BitOps::get(y,SW,r.pivot)==r.scale,"all1007 original constant pivot coefficients");
  for(int c=r.pivot;c<SC;c++){int a=BitOps::get(y,SW,c);if(a)psparse[id].push_back({c,uint8_t(a)});}
  P[id]=std::move(y);
 }
 need(unitSource.size()==4340&&unitOutput.size()==4340,"actual full4340 original unit extent");
 std::vector<int>freeOutput,tailSource;
 for(int c=0;c<NC;c++)if(!unitOutput.count(c))freeOutput.push_back(c);
 for(int r=1;r<=NS;r++)if(!unitSource.count(r))tailSource.push_back(r);
 need(freeOutput.size()==27&&tailSource.size()==NR,"full original27/1848 complements");
 beat("actual-full4340-source-DAG-unit-ready");
 const std::string parentBinding=binding;
 std::ifstream head(argv[6],std::ios::binary);
 need(tag(head)=="R15HKS31"&&get(head,4)==31&&get(head,4)==1,"original high-head input magic/version");
 int headDegree=get(head,4),nh=get(head,4),nt=get(head,4);
 need(headDegree==maximum&&nh==216&&nt==NT,"complete216 by202 supplied high kernel through requested degree");
 char hb[64],pb[64];head.read(hb,64);head.read(pb,64);
 need(bool(head)&&std::string(pb,64)==parentBinding,"same parent full constant profile binding");
 binding=std::string(hb,64);
 need(binding.size()==64&&std::all_of(binding.begin(),binding.end(),[](char c){return(c>='0'&&c<='9')||(c>='a'&&c<='f');}),
      "high original source semantic binding");
 std::vector<int>headRows(nh),freeHead(NT);std::set<int>headSet,freeSet;
 for(int&i:headRows){i=get(head,2);need(i>=1&&i<=NS&&!unitSource.count(i)&&headSet.insert(i).second,"actual216 tail original source rows");}
 for(int&i:freeHead){i=get(head,2);need(i>=0&&i<nh&&freeSet.insert(i).second,"actual202 original free head positions");}
 std::vector<std::vector<uint8_t>>heads(maximum+1,std::vector<uint8_t>(size_t(nh)*NT));
 for(int d=0;d<=maximum;d++){
  head.read((char*)heads[d].data(),heads[d].size());need(bool(head),"complete high-head coefficient payload");
  need(std::all_of(heads[d].begin(),heads[d].end(),[](auto x){return x<31;}),"canonical high-head field coefficients");
  for(int i=0;i<NT;i++)for(int j=0;j<NT;j++)
   need(heads[d][size_t(freeHead[i])*NT+j]==int(d==0&&i==j),"all202 primitive high free coordinates");
 }
 tail(head);const auto inputSHA=file_sha(argv[6]);
 auto sourceProduct=[&](const std::vector<uint8_t>&x,int degree){
  need(x.size()==size_t(NS)*NT&&degree>=0&&degree<=10,"complete original source product shape/degree");
  std::vector<uint32_t>acc(size_t(NC)*NT);
  for(int raw=1;raw<=NS;raw++){
   const auto*v=x.data()+size_t(raw-1)*NT;
   for(auto t:A[degree][raw]){
    auto*y=acc.data()+size_t(t.c)*NT;
    for(int j=0;j<NT;j++)y[j]+=uint32_t(t.a)*v[j];
   }
  }
  std::vector<uint8_t>r(acc.size());
  for(size_t i=0;i<acc.size();i++)r[i]=acc[i]%31;
  return r;
 };
 auto sourceSolve=[&](const std::vector<uint8_t>&v){
  // This is the exact transpose of the already verified transposeSolve.
  // Its input may have all4367 rows; the unselected27 output coordinates are projected away.
  need(v.size()==size_t(NC)*NT,"whole original output RHS for constant source solve");
  std::vector<int64_t>w(v.begin(),v.end()),a(size_t(NP+1)*NT),g(size_t(NB+1)*NT),l(size_t(SC)*NT);
  for(int id:preOrder){
   int64_t q[NT];for(int j=0;j<NT;j++)q[j]=m31(w[size_t(pivot[id])*NT+j]);
   for(int j=0;j<NT;j++)a[size_t(id)*NT+j]+=q[j];
   for(auto[c,factor]:phiFull[id])if(c!=pivot[id])
    for(int j=0;j<NT;j++)w[size_t(c)*NT+j]-=int64_t(factor)*q[j];
   for(int j=0;j<NT;j++)w[size_t(pivot[id])*NT+j]=0;
  }
  for(int c=0;c<SC;c++)for(int j=0;j<NT;j++)l[size_t(c)*NT+j]=w[size_t(components[c])*NT+j];
  for(int c=0;c<SC;c++)if(int id=componentId[c]){
   int64_t q[NT];for(int j=0;j<NT;j++)q[j]=m31(l[size_t(c)*NT+j]*ops.inv[G[id].scale]);
   for(int j=0;j<NT;j++)g[size_t(id)*NT+j]+=q[j];
   for(auto[k,factor]:psparse[id])if(k!=c)
    for(int j=0;j<NT;j++)l[size_t(k)*NT+j]-=int64_t(factor)*q[j];
   for(int j=0;j<NT;j++)l[size_t(c)*NT+j]=0;
  }
  std::vector<uint8_t>x(size_t(NS)*NT);
  for(int id=NB;id>=1;id--){
   int64_t q[NT];for(int j=0;j<NT;j++)q[j]=m31(g[size_t(id)*NT+j]);
   for(int j=0;j<NT;j++)x[size_t(G[id].raw-1)*NT+j]=uint8_t(q[j]);
   for(int i=1;i<=NP;i++)if(H[id][i])
    for(int j=0;j<NT;j++)a[size_t(i)*NT+j]-=int64_t(H[id][i])*q[j];
   for(auto op:G[id].ops)for(int j=0;j<NT;j++)g[size_t(op.id)*NT+j]-=int64_t(op.a)*q[j];
  }
  for(int z=NP-1;z>=0;z--){
   const auto&r=B[z];int64_t q[NT];
   for(int j=0;j<NT;j++)q[j]=m31(a[size_t(r.id)*NT+j]);
   for(int j=0;j<NT;j++)a[size_t(r.id)*NT+j]=q[j];
   for(auto op:r.ops)for(int j=0;j<NT;j++)a[size_t(op.id)*NT+j]-=int64_t(op.a)*q[j];
  }
  for(int id=NP;id>=1;id--){
   int64_t q[NT];for(int j=0;j<NT;j++)q[j]=m31(a[size_t(id)*NT+j]*F[id].scale);
   for(int j=0;j<NT;j++)x[size_t(F[id].raw-1)*NT+j]=uint8_t(q[j]);
   for(auto op:F[id].ops)for(int j=0;j<NT;j++)a[size_t(op.id)*NT+j]-=int64_t(op.a)*q[j];
  }
  for(int raw:tailSource)for(int j=0;j<NT;j++)need(!x[size_t(raw-1)*NT+j],"whole sourceSolve support lies in same4340 original unit columns");
  return x;
 };
 std::unordered_map<int,int>headPosition;
 for(int i=0;i<nh;i++)headPosition[headRows[i]]=i;
 auto validate=[&](const std::vector<uint8_t>&x,int degree){
  need(x.size()==size_t(NS)*NT,"complete original202-source layer");
  for(int raw:tailSource){
   auto it=headPosition.find(raw);
   for(int j=0;j<NT;j++){
    int expected=it==headPosition.end()?0:heads[degree][size_t(it->second)*NT+j];
    need(x[size_t(raw-1)*NT+j]==expected,"all1848 original tail source coordinates equal actual high mapper");
   }
  }
 };
 std::vector<std::vector<uint8_t>>K;
 struct Hashes{std::string k,r;};std::vector<Hashes>hashes;
 int completed=-1,restored=-1;const auto ledger=prefix+"-ledger.txt";
 if(fs::exists(ledger)){
  std::ifstream f(ledger);std::string lm,lb,li,lp;f>>lm>>lb>>li>>lp>>completed;
  need(lm=="R15HKLEDGER1"&&lb==binding&&li==inputSHA&&lp==parentBinding
       &&completed>=0&&completed<=maximum,"complete original high-source ledger binding");
  for(int d=0;d<=completed;d++){
   Hashes h;f>>h.k>>h.r;need(h.k.size()==64&&h.r.size()==64,"complete high-source layer hashes");
   auto x=load_field(prefix+"-source-"+std::to_string(d)+".bin","R15HKX31",d,NS,NT,binding,h.k);validate(x,d);
   auto r=load_field(prefix+"-product-"+std::to_string(d)+".bin","R15HKR31",d,NC,NT,binding,h.r);
   need(std::all_of(r.begin(),r.end(),[](auto v){return v==0;}),"all restored original high-source products zero");
   K.push_back(std::move(x));hashes.push_back(h);
  }
  need(bool(f)&&!(f>>lm),"complete original high-source ledger tail");restored=completed;
 }
 auto commit=[&](int d,const std::vector<uint8_t>&x,const std::vector<uint8_t>&r){
  auto kp=prefix+"-source-"+std::to_string(d)+".bin",rp=prefix+"-product-"+std::to_string(d)+".bin";
  save_field(kp,"R15HKX31",d,NS,NT,x,binding);save_field(rp,"R15HKR31",d,NC,NT,r,binding);
  hashes.push_back({file_sha(kp),file_sha(rp)});K.push_back(x);completed=d;
  std::ofstream f(ledger+".partial");f<<"R15HKLEDGER1 "<<binding<<" "<<inputSHA<<" "<<parentBinding<<" "<<completed<<"\n";
  for(auto q:hashes)f<<q.k<<" "<<q.r<<"\n";f.close();need(bool(f),"complete atomic original high-source ledger");fs::rename(ledger+".partial",ledger);
 };
 beat("actual202-high-heads-and-whole-original-source-adjoint-ready");
 for(int d=completed+1;d<=maximum;d++){
  if(stopping||elapsed()>limit-std::min(15.0,limit/5))break;
  std::vector<uint32_t>acc(size_t(NC)*NT);
  for(int k=1;k<=std::min(10,d);k++){
   auto r=sourceProduct(K[d-k],k);for(size_t i=0;i<acc.size();i++)acc[i]+=r[i];
  }
  std::vector<uint8_t>seed(size_t(NS)*NT);
  for(int i=0;i<nh;i++)for(int j=0;j<NT;j++)seed[size_t(headRows[i]-1)*NT+j]=heads[d][size_t(i)*NT+j];
  auto rhs=sourceProduct(seed,0);for(size_t i=0;i<rhs.size();i++)rhs[i]=(rhs[i]+acc[i])%31;
  auto x=sourceSolve(rhs);for(size_t i=0;i<x.size();i++)x[i]=m31(int(seed[i])-x[i]);validate(x,d);
  auto r=sourceProduct(x,0);for(size_t i=0;i<r.size();i++)r[i]=(r[i]+acc[i])%31;
  for(int c:unitOutput)for(int j=0;j<NT;j++)need(!r[size_t(c)*NT+j],"all4340 original unit sourceSolve products");
  need(std::all_of(r.begin(),r.end(),[](auto v){return v==0;}),"all4367 original high-kernel products at actual degree");
  commit(d,x,r);beat("complete202-original-source-degree-"+std::to_string(d));
 }
 std::ofstream o(prefix+"-receipt.json");
 o<<std::setprecision(17)<<"{\"format\":\"isp-full-original-high202-source-transport-v1\",\"status\":\""<<(completed==maximum?"completed":"checkpointed-time-budget")
  <<"\",\"inputBinding\":\""<<binding<<"\",\"parentFullBinding\":\""<<parentBinding<<"\",\"inputHeadsSHA256\":\""<<inputSHA
  <<"\",\"field\":31,\"requestedMaximumDegree\":"<<maximum<<",\"completedDegree\":"<<completed<<",\"restoredCompletedDegree\":"<<restored
  <<",\"actualConstantUnitRank\":4340,\"originalSourceRows\":6188,\"originalOutputRows\":4367,\"highKernelColumns\":202"
  <<",\"all3333OriginalPrebasisTriangularUnitProductsVerified\":true,\"prebasisNaturalTailNonzeros\":"<<preTailNonzeros
  <<",\"prebasisNaturalTailMaximumMomentDegreeDrop\":"<<largestPreDegreeDrop
  <<",\"all1007OriginalFullPivotProductsVerified\":true"
  <<",\"all202OriginalFreeSourceCoordinatesVerified\":"<<(completed>=0?"true":"false")
  <<",\"all1848OriginalTailMapperCoordinatesVerified\":"<<(completed>=0?"true":"false")
  <<",\"all4340OriginalUnitSourceSolveProductsVerified\":"<<(completed>=0?"true":"false")
  <<",\"all4367OriginalHigherKernelProductsVerifiedThroughCompletedDegree\":"<<(completed>=0?"true":"false")
  <<",\"originalProductCoordinatesVerified\":"<<uint64_t(completed+1)*NC*NT
  <<",\"characteristicZeroSourceKernelComputed\":false,\"selectedLeadingCoefficientUnitProved\":false"
  <<",\"prebasisForwardOperations\":"<<fc<<",\"prebasisBackwardOperations\":"<<bc<<",\"fullConstantSourceOperations\":"<<gc
  <<",\"completeSourceDerivativeCoefficients\":"<<coefficientCount
  <<",\"highHeadOriginalSourceRowsOneBased\":[";
 for(int i=0;i<nh;i++){if(i)o<<",";o<<headRows[i];}o<<"],\"freeOriginalSourceRowsOneBased\":[";
 for(int i=0;i<NT;i++){if(i)o<<",";o<<headRows[freeHead[i]];}o<<"],\"nativeSeconds\":"<<elapsed()<<"}\n";
 o.close();need(bool(o),"save full original high-source receipt");
 beat(completed==maximum?"complete-original202-high-source-mapper":"checkpointed-original202-high-source-mapper");
 return completed==maximum?0:75;
}catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 1;}}
