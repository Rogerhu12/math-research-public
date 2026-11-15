// Same original I,J: complete finite-field natural-u Schur jets.
// Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
// Replays paid source operations; no new large Gaussian elimination.
#include "2026-11-15-r150-saturated-global-common-789f.hpp"
#include <numeric>
#include <iomanip>
#include <filesystem>
#include <csignal>
using namespace sb;
static volatile std::sig_atomic_t stopping=0;
static void stop_signal(int){stopping=1;}
struct Op{int id=0,a=0;};
struct Forward{int raw=0,scale=0;std::vector<Op>ops;};
struct Backward{int id=0;std::vector<Op>ops;};
static int mod31(int x){x%=31;return x<0?x+31:x;}
static void addmul(BitOps&ops,Row&a,const Row&b,int W,int f,int first=0){
 f=mod31(f);if(!f)return;auto r=ops.rep[f];
 BitOps::add(a,W,first,b,W,first,W-first,r.rot,r.neg);
 if(r.c)BitOps::add(a,W,first,b,W,first,W-first,(r.rot+(r.c==1?1:2))%5,r.neg);
}
static std::vector<uint8_t>read_field(const std::string&path,int rows,int cols){
 std::ifstream f(path,std::ios::binary);
 if(tag(f)!="R150BC31"||get(f,4)!=31||get(f,4)!=uint64_t(rows)||get(f,4)!=uint64_t(cols))throw std::runtime_error("paid field input header");
 std::vector<uint8_t>v(size_t(rows)*cols);f.read((char*)v.data(),v.size());if(!f)throw std::runtime_error("truncated complete field array");tail(f);
 if(std::any_of(v.begin(),v.end(),[](auto a){return a>=31;}))throw std::runtime_error("noncanonical paid field input");
 return v;
}
static void save_bound(const std::string&file,const char*magic,int degree,int rows,int cols,const std::vector<uint8_t>&v,const std::string&binding){
 if(v.size()!=size_t(rows)*cols||binding.size()!=64)throw std::runtime_error("complete bound matrix size");
 std::ofstream o(file+".partial",std::ios::binary);o.write(magic,8);put(o,31,4);put(o,degree,4);put(o,rows,4);put(o,cols,4);o.write(binding.data(),64);o.write((char*)v.data(),v.size());o.close();
 if(!o)throw std::runtime_error("complete bound matrix save");std::filesystem::rename(file+".partial",file);
}
static std::vector<uint8_t>load_bound(const std::string&file,const char*magic,int degree,int rows,int cols,const std::string&binding){
 std::ifstream f(file,std::ios::binary);
 if(tag(f)!=magic||get(f,4)!=31||get(f,4)!=uint64_t(degree)||get(f,4)!=uint64_t(rows)||get(f,4)!=uint64_t(cols))throw std::runtime_error("actual checkpoint dimensions");
 char b[64];f.read(b,64);if(std::string(b,64)!=binding)throw std::runtime_error("actual checkpoint binding");
 std::vector<uint8_t>v(size_t(rows)*cols);f.read((char*)v.data(),v.size());if(!f)throw std::runtime_error("truncated complete field array");tail(f);
 if(std::any_of(v.begin(),v.end(),[](auto a){return a>=31;}))throw std::runtime_error("actual checkpoint field");
 return v;
}
int main(int argc,char**argv){try{
 if(argc!=11)throw std::runtime_error("usage native-model prepared-selected-model forward backward image-source-dag paid-kernel36 paid-first-product prefix maximum-jet remaining-seconds");
 const auto start=std::chrono::steady_clock::now();int maximum=std::stoi(argv[9]);double limit=std::stod(argv[10]);
 if(maximum<1||maximum>32||!(limit>0&&limit<=600))throw std::runtime_error("explicit finite jet and clock");
 auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 const std::string prefix=argv[8];std::signal(SIGTERM,stop_signal);std::signal(SIGINT,stop_signal);
 auto beat=[&](const std::string&phase){std::cout<<std::setprecision(17)<<"{\"phase\":\""<<phase<<"\",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;};
 Model M(argv[1]);constexpr int NS=6188,NC=4367,NP=3333,SC=1021,NB=985,NT=36,W=(NC+31)/32,SW=(SC+31)/32;
 std::ifstream p(argv[2]);std::string magic,binding;p>>magic>>binding;
 if(magic!="R150_SELECTED_NATURAL_U_SCHUR31_V1"||binding.size()!=64)throw std::runtime_error("same original natural-u input");
 int n;p>>n;if(n!=SC)throw std::runtime_error("same selected1021 sources");std::vector<int>sources(n);std::set<int>selectedSources;
 for(auto&r:sources){p>>r;if(r<1||r>NS||!selectedSources.insert(r).second)throw std::runtime_error("same original source dictionary");}
 p>>n;if(n!=SC)throw std::runtime_error("same selected1021 outputs");std::vector<int>outputs(n);std::set<int>selectedOutputs;
 for(auto&c:outputs){p>>c;if(c<0||c>=NC||!selectedOutputs.insert(c).second)throw std::runtime_error("same original output dictionary");}
 p>>n;if(n!=NB)throw std::runtime_error("same independent985");std::vector<int>independent(n);std::set<int>independentSet;
 for(auto&i:independent){p>>i;if(i<0||i>=SC||!independentSet.insert(i).second)throw std::runtime_error("same independent source indices");}
 p>>n;if(n!=NT)throw std::runtime_error("same free36");std::vector<int>freeSources(n);std::set<int>freeSet;
 for(auto&i:freeSources){p>>i;if(i<0||i>=SC||independentSet.count(i)||!freeSet.insert(i).second)throw std::runtime_error("same36 free source indices");}
 if(!p||p>>magic)throw std::runtime_error("same selected model tail");
 std::unordered_map<int,uint64_t>prePivot;std::array<int,NP+1>pivot{};
 for(auto&r:M.pre){prePivot[r.raw]=r.pivot;if(!selectedSources.insert(r.raw).second)throw std::runtime_error("prebasis/source overlap");if(!selectedOutputs.insert(M.component.at(r.pivot)).second)throw std::runtime_error("prebasis/output overlap");}
 if(selectedSources.size()!=4354||selectedOutputs.size()!=4354)throw std::runtime_error("same original square4354");
 std::vector<uint64_t>termkeys(M.var.begin(),M.var.end());for(auto[a,b]:M.quadratic)termkeys.push_back(M.var[a]+M.var[b]);
 struct Term{int c;uint8_t a;};std::vector<std::vector<std::vector<Term>>>A(11,std::vector<std::vector<Term>>(NS+1));
 for(int raw:selectedSources){
  int e=(raw-1)%17;auto mul=M.multipliers[(raw-1)/17];
  for(int j=0;j<77;j++)for(int k=0;k<=10;k++){
   int a=0;
   if(e<11){if(j<11)a=M.L[e][j][10-k];else if(k==0)a=M.Q[e][j-11];}
   else if(j>=11&&k<=5)a=M.G[e-11][j-11][5-k];
   if(a)A[k][raw].push_back({M.component.at(mul+termkeys[j]),uint8_t(a)});
  }
 }
 auto rawrow=[&](int raw){Row x(5*W);for(auto t:A[0][raw])BitOps::set(x,W,t.c,t.a);return x;};
 std::ifstream f(argv[3],std::ios::binary),b(argv[4],std::ios::binary);
 if(tag(f)!="R150PB31"||get(f,4)!=NP||tag(b)!="R150RJ31"||get(b,4)!=NP)throw std::runtime_error("paid constant source-DAG headers");
 std::vector<Forward>F(NP+1);uint64_t fc=0,bc=0;
 for(int id=1;id<=NP;id++){
  auto&r=F[id];r.raw=get(f,4);r.scale=get(f,1);int count=get(f,4);
  if(!prePivot.count(r.raw)||r.scale<1||r.scale>30||count<0||count>NP)throw std::runtime_error("paid prebasis source");
  pivot[id]=M.component.at(prePivot.at(r.raw));
  for(int j=0;j<count;j++){Op a{int(get(f,2)),int(get(f,1))};if(a.id<1||a.id>=id||a.a<1||a.a>30)throw std::runtime_error("paid forward operation");r.ops.push_back(a);}fc+=count;
 }
 tail(f);std::vector<Backward>B(NP);std::set<int>seen;
 for(auto&r:B){
  r.id=get(b,2);int count=get(b,4);if(r.id<1||r.id>NP||!seen.insert(r.id).second||count<0||count>NP)throw std::runtime_error("paid backward source");
  for(int j=0;j<count;j++){Op a{int(get(b,2)),int(get(b,1))};if(a.id<1||a.id>NP||a.id==r.id||a.a<1||a.a>30)throw std::runtime_error("paid backward operation");r.ops.push_back(a);}bc+=count;
 }
 tail(b);if(fc!=782976||bc!=1010703)throw std::runtime_error("complete paid prebasis operation counts");
 BitOps ops;std::vector<Row>phi(NP+1);
 for(int id=1;id<=NP;id++){
  Row x=rawrow(F[id].raw);for(auto a:F[id].ops)addmul(ops,x,phi[a.id],W,-a.a);ops.multiple(x,W,0,F[id].scale);
  if(BitOps::get(x,W,pivot[id])!=1)throw std::runtime_error("same actual infinity prebasis unit");
  phi[id]=std::move(x);
 }
 for(auto&r:B)for(auto a:r.ops)addmul(ops,phi[r.id],phi[a.id],W,-a.a);
 std::vector<int>order(NP);std::iota(order.begin(),order.end(),1);std::sort(order.begin(),order.end(),[&](int a,int b){return pivot[a]<pivot[b];});
 auto normal=[&](Row&x,std::vector<uint8_t>&co){
  co.assign(NP+1,0);
  for(int id:order){int a=BitOps::get(x,W,pivot[id]);if(a){co[id]=a;addmul(ops,x,phi[id],W,-a,pivot[id]/32);}}
  for(int id:order)if(BitOps::get(x,W,pivot[id]))throw std::runtime_error("complete original prebasis identity");
 };
 auto lead=[&](const Row&x){for(int w=0;w<SW;w++){uint32_t z=0;for(int bit=0;bit<5;bit++)z|=x[bit*SW+w];if(z){int c=32*w+__builtin_ctz(z);if(c>=SC)throw std::runtime_error("image padding");return c;}}return -1;};
 std::vector<Row>image(SC);std::vector<int>imageId(SC),gPivot(NB+1);std::vector<Forward>G(NB+1);std::vector<std::vector<uint8_t>>H(NB+1);
 std::ifstream gd(argv[5],std::ios::binary);
 if(tag(gd)!="R150IG31"||get(gd,4)!=NB)throw std::runtime_error("paid985 source DAG");
 uint64_t gc=0;
 for(int id=1;id<=NB;id++){
  auto&r=G[id];r.raw=get(gd,4);r.scale=get(gd,1);int count=get(gd,4);
  if(r.raw!=sources[independent[id-1]]||r.scale<1||r.scale>30||count<0||count>=id)throw std::runtime_error("same985 source normalization");
  for(int j=0;j<count;j++){Op a{int(get(gd,2)),int(get(gd,1))};if(a.id<1||a.id>=id||a.a<1||a.a>30)throw std::runtime_error("same985 source operation");r.ops.push_back(a);}gc+=count;
 }
 tail(gd);if(gc!=462972)throw std::runtime_error("complete paid985 operation count");
 for(int id=1;id<=NB;id++){
  Row x=rawrow(G[id].raw);normal(x,H[id]);Row y(5*SW);for(int c=0;c<SC;c++)BitOps::set(y,SW,c,BitOps::get(x,W,outputs[c]));
  for(auto a:G[id].ops)addmul(ops,y,image[gPivot[a.id]],SW,-a.a);
  ops.multiple(y,SW,0,G[id].scale);int c=lead(y);
  if(c<0||!image[c].empty()||BitOps::get(y,SW,c)!=1)throw std::runtime_error("same985 unit source replay");
  image[c]=std::move(y);imageId[c]=id;gPivot[id]=c;
 }
 std::vector<int>coker;std::set<int>cokerOriginal;
 for(int c=0;c<SC;c++)if(image[c].empty()){coker.push_back(c);cokerOriginal.insert(outputs[c]);}
 if(coker.size()!=NT||cokerOriginal.size()!=NT)throw std::runtime_error("same complete36 complement outputs");
 std::vector<int>unitOutput;
 for(int c:selectedOutputs)if(!cokerOriginal.count(c))unitOutput.push_back(c);
 if(unitOutput.size()!=4318)throw std::runtime_error("same complete4318 unit outputs");
 auto solve=[&](const std::vector<uint8_t>&rhs,std::vector<uint8_t>&correction,std::vector<uint8_t>&remainder){
  if(rhs.size()!=size_t(NC)*NT)throw std::runtime_error("complete original RHS");
  correction.assign(NS*NT,0);remainder.assign(NT*NT,0);
  for(int k=0;k<NT;k++){
   Row x(5*W);for(int c=0;c<NC;c++)BitOps::set(x,W,c,rhs[c*NT+k]);std::vector<uint8_t>alpha;normal(x,alpha);
   Row y(5*SW);for(int c=0;c<SC;c++)BitOps::set(y,SW,c,BitOps::get(x,W,outputs[c]));
   std::vector<uint8_t>gam(NB+1),tj(NB+1);
   for(int c=0;c<SC;c++)if(!image[c].empty()){int a=BitOps::get(y,SW,c);if(a){gam[imageId[c]]=a;addmul(ops,y,image[c],SW,-a,c/32);}}
   for(int r=0;r<NT;r++)remainder[r*NT+k]=BitOps::get(y,SW,coker[r]);
   for(int id=NB;id>=1;id--){int c=gam[id]*G[id].scale%31;tj[id]=c;if(c)for(auto a:G[id].ops)gam[a.id]=mod31(int(gam[a.id])-a.a*c);}
   for(int id=1;id<=NB;id++)if(tj[id]){correction[(G[id].raw-1)*NT+k]=tj[id];int a=tj[id];for(int j=1;j<=NP;j++)alpha[j]=mod31(int(alpha[j])-a*H[id][j]);}
   for(int z=NP-1;z>=0;z--){auto&r=B[z];int c=alpha[r.id];if(c)for(auto a:r.ops)alpha[a.id]=mod31(int(alpha[a.id])-a.a*c);}
   for(int id=NP;id>=1;id--){auto&r=F[id];int c=alpha[id]*r.scale%31;correction[(r.raw-1)*NT+k]=c;if(c)for(auto a:r.ops)alpha[a.id]=mod31(int(alpha[a.id])-a.a*c);alpha[id]=0;}
  }
 };
 auto validate_source=[&](const std::vector<uint8_t>&x,int degree){
  if(x.size()!=size_t(NS)*NT)throw std::runtime_error("full source shape");
  for(int r=1;r<=NS;r++)if(!selectedSources.count(r))for(int k=0;k<NT;k++)if(x[(r-1)*NT+k])throw std::runtime_error("source escaped sameJ");
  for(int j=0;j<NT;j++)for(int k=0;k<NT;k++)
   if(x[(sources[freeSources[j]]-1)*NT+k]!=(degree==0&&j==k?1:0))throw std::runtime_error("complete fixed free source coordinates");
 };
 auto product=[&](const std::vector<uint8_t>&x,int degree){
  std::vector<uint64_t>v(NC*NT);
  for(int raw:selectedSources)for(auto t:A[degree][raw]){
   auto*dst=v.data()+t.c*NT;auto*src=x.data()+(raw-1)*NT;
   for(int k=0;k<NT;k++)dst[k]+=uint64_t(t.a)*src[k];
  }
  std::vector<uint8_t>r(v.size());for(size_t i=0;i<v.size();i++)r[i]=v[i]%31;return r;
 };
 auto initial=read_field(argv[6],NS,NT);validate_source(initial,0);
 auto paidFirst=read_field(argv[7],NC,NT);
 std::vector<std::vector<uint8_t>>X;X.push_back(initial);
 int completed=0;uint64_t restored=0;
 std::string ledger=prefix+"-ledger.txt";
 if(std::filesystem::exists(ledger)){
  std::ifstream l(ledger);std::string lb;l>>lb>>completed;if(!l||lb!=binding||completed<0||completed>maximum)throw std::runtime_error("same complete source-jet ledger");
  for(int k=0;k<=completed;k++){
   auto v=load_bound(prefix+"-source-"+std::to_string(k)+".bin","R150US31",k,NS,NT,binding);validate_source(v,k);
   if(k==0){if(v!=initial)throw std::runtime_error("actual start kernel changed");}
   else X.push_back(std::move(v));
   load_bound(prefix+"-schur-"+std::to_string(k)+".bin","R150UJ31",k,NT,NT,binding);
   load_bound(prefix+"-residual-"+std::to_string(k)+".bin","R150UR31",k,NC,NT,binding);
  }
  restored=completed;
 }else{
  auto c0=product(initial,0);if(std::any_of(c0.begin(),c0.end(),[](auto a){return a!=0;}))throw std::runtime_error("complete original constant source identity");
  std::vector<uint8_t>z(NT*NT);
  save_bound(prefix+"-source-0.bin","R150US31",0,NS,NT,initial,binding);
  save_bound(prefix+"-schur-0.bin","R150UJ31",0,NT,NT,z,binding);
  save_bound(prefix+"-residual-0.bin","R150UR31",0,NC,NT,c0,binding);
  std::ofstream l(ledger+".partial");l<<binding<<" 0\n";l.close();if(!l)throw std::runtime_error("initial actual ledger");std::filesystem::rename(ledger+".partial",ledger);
 }
 beat("paid-source-inverse-ready");
 for(int degree=completed+1;degree<=maximum;degree++){
  if(stopping||elapsed()>limit-std::min(10.0,limit/5)){break;}
  std::vector<uint8_t>rhs;
  if(degree==1)rhs=paidFirst;
  else{
   std::vector<uint64_t>v(NC*NT);
   for(int j=1;j<=std::min(10,degree);j++){
    const auto&x=X[degree-j];
    for(int raw:selectedSources)for(auto t:A[j][raw]){
     auto*dst=v.data()+t.c*NT;auto*src=x.data()+(raw-1)*NT;
     for(int k=0;k<NT;k++)dst[k]+=uint64_t(t.a)*src[k];
    }
   }
   static_assert(uint64_t(10)*6188*77*30*30<UINT64_MAX,"exact finite coefficient accumulator");
   rhs.resize(v.size());for(size_t i=0;i<v.size();i++)rhs[i]=v[i]%31;
  }
  std::vector<uint8_t>correction,rem;solve(rhs,correction,rem);
  for(auto&a:correction)if(a)a=31-a;
  validate_source(correction,degree);
  auto residual=product(correction,0);for(size_t i=0;i<residual.size();i++)residual[i]=(residual[i]+rhs[i])%31;
  for(int c:unitOutput)for(int k=0;k<NT;k++)if(residual[c*NT+k])throw std::runtime_error("actual original4318 unit rows not cancelled");
  for(int r=0;r<NT;r++)for(int k=0;k<NT;k++)if(residual[outputs[coker[r]]*NT+k]!=rem[r*NT+k])throw std::runtime_error("actual sameI complete36 Schur residual");
  save_bound(prefix+"-source-"+std::to_string(degree)+".bin","R150US31",degree,NS,NT,correction,binding);
  save_bound(prefix+"-schur-"+std::to_string(degree)+".bin","R150UJ31",degree,NT,NT,rem,binding);
  save_bound(prefix+"-residual-"+std::to_string(degree)+".bin","R150UR31",degree,NC,NT,residual,binding);
  X.push_back(std::move(correction));completed=degree;
  std::ofstream l(ledger+".partial");l<<binding<<" "<<completed<<"\n";l.close();if(!l)throw std::runtime_error("complete actual source ledger");std::filesystem::rename(ledger+".partial",ledger);
  beat("complete-original-natural-jet-"+std::to_string(degree));
 }
 std::ofstream o(prefix+"-receipt.json");o<<std::setprecision(17)
  <<"{\"status\":\""<<(completed==maximum?"completed":"checkpointed-time-budget")<<"\",\"inputBinding\":\""<<binding
  <<"\",\"field\":31,\"maximumRequestedDegree\":"<<maximum<<",\"completedDegree\":"<<completed
  <<",\"restoredCompletedDegrees\":"<<restored<<",\"all4354SelectedJetIdentitiesVerified\":true"
  <<",\"all4367OriginalResidualCoordinatesRetained\":true,\"all36FreeSourceCoordinatesVerified\":true"
  <<",\"sameSelectedSourceSupportVerified\":true,\"constantSourceOperationsReplayedOnly\":true"
  <<",\"newLargeGaussianEliminations\":0,\"forwardOperations\":"<<fc<<",\"backwardOperations\":"<<bc
  <<",\"selectedImageSourceOperations\":"<<gc<<",\"elapsedSeconds\":"<<elapsed()
  <<",\"oldCokerOriginalOutputIndices\":[";
 for(int i=0;i<NT;i++){if(i)o<<',';o<<outputs[coker[i]];}o<<"],\"unitOriginalOutputIndices\":";array(o,unitOutput);o<<"}\n";o.close();
 if(!o)throw std::runtime_error("actual native Schur receipt");
 beat("actual-natural-source-Schur-stage-ended");return completed==maximum?0:75;
}catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 1;}}
