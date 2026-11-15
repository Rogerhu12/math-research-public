// Same original selected infinity matrix: 36 normalized Dixon kernel lifts.
// Only the already paid constant N source DAG is replayed. Every integer
// product uses the original primitive coefficients modulo 31^2.
#include "2026-11-15-r150-saturated-global-common-789f.hpp"
#include <numeric>
#include <iomanip>
#include <filesystem>
using namespace sb;
struct Op {int id=0,a=0;};
struct Forward {int raw=0,scale=0;std::vector<Op> ops;};
struct Backward {int id=0;std::vector<Op> ops;};
static int posmod(int x,int p){x%=p;return x<0?x+p:x;}
static bool iszero(const Row &x){for(auto a:x)if(a)return false;return true;}
static void addmul(BitOps &ops,Row &a,const Row &b,int W,int f,int first=0){
 f=posmod(f,31);if(!f)return;auto r=ops.rep[f];
 BitOps::add(a,W,first,b,W,first,W-first,r.rot,r.neg);
 if(r.c)BitOps::add(a,W,first,b,W,first,W-first,(r.rot+(r.c==1?1:2))%5,r.neg);
}
static void byte_matrix(const std::string &file,int rows,int cols,const std::vector<uint8_t>& data,int p=31){
 if(data.size()!=size_t(rows)*cols)throw std::runtime_error("matrix output size");
 std::ofstream o(file,std::ios::binary);o.write("R150BC31",8);put(o,p,4);put(o,rows,4);put(o,cols,4);o.write((char*)data.data(),data.size());if(!o)throw std::runtime_error("matrix write");
}

static void u64_matrix(const std::string&file,const char *magic,int n,int rows,int cols,uint64_t modulus,const std::vector<uint64_t>&v,const std::string&binding){
 if(v.size()!=size_t(rows)*cols)throw std::runtime_error("u64 matrix shape");
 std::ofstream o(file,std::ios::binary);o.write(magic,8);put(o,31,4);put(o,n,4);put(o,rows,4);put(o,cols,4);put(o,modulus,8);o.write(binding.data(),64);
 for(auto a:v)put(o,a,8);o.close();if(!o)throw std::runtime_error("u64 matrix output");
}
int main(int argc,char**argv){try{
 if(argc!=8)throw std::runtime_error("usage native-model prepared-dixon-model forward backward original-kernel36 prefix remaining-seconds");
 auto start=std::chrono::steady_clock::now();double limit=std::stod(argv[7]);
 if(!(limit>0&&limit<=60))throw std::runtime_error("explicit <=60 second native budget");
 auto sec=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 auto beat=[&](std::string phase){std::cout<<"{\"phase\":\""<<phase<<"\",\"elapsedSeconds\":"<<sec()<<"}\n"<<std::flush;if(sec()>limit-1)throw std::runtime_error("shared time budget at "+phase);};
 std::string prefix=argv[6];Model M(argv[1]);constexpr int NS=6188,NC=4367,NP=3333,SC=1021,NB=985,NT=36,W=(NC+31)/32,SW=(SC+31)/32;
 std::ifstream in(argv[2]);std::string magic,binding;int exponent;uint64_t maxmod;in>>magic>>binding>>exponent>>maxmod;
 uint64_t checkmod=1;for(int e=0;e<exponent;e++)checkmod*=31;
 if(magic!="R150_SELECTED_INFINITY_DIXON_V1"||binding.size()!=64||exponent<2||exponent>4||maxmod!=checkmod)throw std::runtime_error("Dixon model header");
 std::array<std::array<uint64_t,77>,17>A{};
 for(int e=0;e<17;e++)for(int j=0;j<77;j++){in>>A[e][j];int v=e<11?(j<11?M.L[e][j][10]:M.Q[e][j-11]):(j<11?0:M.G[e-11][j-11][5]);if(!in||A[e][j]>=maxmod||A[e][j]%31!=uint64_t(v))throw std::runtime_error("same integer constant coefficient");}
 int n;in>>n;if(n!=SC)throw std::runtime_error("selected source count");std::vector<int>sources(n);std::set<int>selectedSource;
 for(auto&r:sources){in>>r;if(r<1||r>NS||!selectedSource.insert(r).second)throw std::runtime_error("selected sources");}
 in>>n;if(n!=SC)throw std::runtime_error("selected output count");std::vector<int>outputs(n);std::set<int>selectedOutput;
 for(auto&c:outputs){in>>c;if(c<0||c>=NC||!selectedOutput.insert(c).second)throw std::runtime_error("selected outputs");}
 in>>n;if(n!=NB)throw std::runtime_error("985 unit sources");std::vector<int>independent(n);std::set<int>independentSet;
 for(auto&j:independent){in>>j;if(j<0||j>=SC||!independentSet.insert(j).second)throw std::runtime_error("independent source index");}
 in>>n;if(n!=NT)throw std::runtime_error("36 normalized free sources");std::vector<int>freeSources(n);std::set<int>freeSet;
 for(auto&j:freeSources){in>>j;if(j<0||j>=SC||independentSet.count(j)||!freeSet.insert(j).second)throw std::runtime_error("free source dictionary");}
 if(!in||in>>magic)throw std::runtime_error("Dixon model tail");
 std::array<int,NP+1>pivot{};std::unordered_map<int,uint64_t>prePivot;
 for(auto&s:M.pre){prePivot[s.raw]=s.pivot;if(!selectedSource.insert(s.raw).second)throw std::runtime_error("source support overlap");int c=M.component.at(s.pivot);if(!selectedOutput.insert(c).second)throw std::runtime_error("output support overlap");}
 if(selectedSource.size()!=4354||selectedOutput.size()!=4354)throw std::runtime_error("same square selected4354");
 std::vector<int>allOutputs(selectedOutput.begin(),selectedOutput.end());
 std::vector<uint64_t>termsKeys(M.var.begin(),M.var.end());for(auto[a,b]:M.quadratic)termsKeys.push_back(M.var[a]+M.var[b]);
 auto terms=[&](int raw,auto action){int e=(raw-1)%17;auto mult=M.multipliers[(raw-1)/17];for(int j=0;j<77;j++)if(A[e][j])action(M.component.at(mult+termsKeys[j]),A[e][j]);};
 auto rawrow=[&](int raw){Row x(5*W);terms(raw,[&](int c,uint64_t a){BitOps::set(x,W,c,a%31);});return x;};
 std::ifstream f(argv[3],std::ios::binary),b(argv[4],std::ios::binary);
 if(tag(f)!="R150PB31"||get(f,4)!=NP||tag(b)!="R150RJ31"||get(b,4)!=NP)throw std::runtime_error("paid basis DAG");
 std::vector<Forward>F(NP+1);uint64_t forwardCount=0,backCount=0;
 for(int id=1;id<=NP;id++){auto&r=F[id];r.raw=get(f,4);r.scale=get(f,1);int nc=get(f,4);if(!prePivot.count(r.raw)||r.scale<1||r.scale>30||nc<0||nc>NP)throw std::runtime_error("forward row");
  pivot[id]=M.component.at(prePivot.at(r.raw));for(int j=0;j<nc;j++){Op a{int(get(f,2)),int(get(f,1))};if(a.id<1||a.id>=id||a.a<1||a.a>30)throw std::runtime_error("forward operation");r.ops.push_back(a);}forwardCount+=nc;}
 tail(f);std::vector<Backward>B(NP);std::set<int>backSeen;
 for(auto&r:B){r.id=get(b,2);int nc=get(b,4);if(r.id<1||r.id>NP||!backSeen.insert(r.id).second||nc<0||nc>NP)throw std::runtime_error("backward row");
  for(int j=0;j<nc;j++){Op a{int(get(b,2)),int(get(b,1))};if(a.id<1||a.id>NP||a.id==r.id||a.a<1||a.a>30)throw std::runtime_error("backward operation");r.ops.push_back(a);}backCount+=nc;}
 tail(b);if(forwardCount!=782976||backCount!=1010703)throw std::runtime_error("complete paid DAG counts");
 BitOps ops;std::vector<Row>phi(NP+1);
 for(int id=1;id<=NP;id++){Row x=rawrow(F[id].raw);for(auto a:F[id].ops)addmul(ops,x,phi[a.id],W,-a.a);ops.multiple(x,W,0,F[id].scale);if(BitOps::get(x,W,pivot[id])!=1)throw std::runtime_error("actual prebasis unit");phi[id]=std::move(x);}
 for(auto&r:B)for(auto a:r.ops)addmul(ops,phi[r.id],phi[a.id],W,-a.a);
 std::vector<int>order(NP);std::iota(order.begin(),order.end(),1);std::sort(order.begin(),order.end(),[&](int a,int b){return pivot[a]<pivot[b];});
 auto normal=[&](Row&x,std::vector<uint8_t>&co){co.assign(NP+1,0);for(int id:order){int a=BitOps::get(x,W,pivot[id]);if(a){co[id]=a;addmul(ops,x,phi[id],W,-a,pivot[id]/32);}}for(int id:order)if(BitOps::get(x,W,pivot[id]))throw std::runtime_error("full prebasis normal identity");};
 beat("same4318-prebasis-restored");
 auto lead=[&](const Row&x){for(int w=0;w<SW;w++){uint32_t z=0;for(int bit=0;bit<5;bit++)z|=x[bit*SW+w];if(z){int c=32*w+__builtin_ctz(z);if(c>=SC)throw std::runtime_error("padding");return c;}}return -1;};
 std::vector<Row>image(SC);std::vector<int>imageId(SC);std::vector<Forward>G(NB+1);std::vector<std::vector<uint8_t>>H(NB+1);
 uint64_t imageOperations=0;
 for(int id=1;id<=NB;id++){
  int raw=sources[independent[id-1]];Row x=rawrow(raw);normal(x,H[id]);Row y(5*SW);
  for(int c=0;c<SC;c++)BitOps::set(y,SW,c,BitOps::get(x,W,outputs[c]));
  G[id].raw=raw;
  while(true){int c=lead(y);if(c<0)throw std::runtime_error("selected985 independence");int a=BitOps::get(y,SW,c);
   if(image[c].empty()){G[id].scale=ops.inv[a];ops.multiple(y,SW,0,G[id].scale);image[c]=std::move(y);imageId[c]=id;break;}
   G[id].ops.push_back({imageId[c],a});imageOperations++;addmul(ops,y,image[c],SW,-a,c/32);
  }
 }
 std::vector<int>coker;for(int c=0;c<SC;c++)if(image[c].empty())coker.push_back(c);if(coker.size()!=NT)throw std::runtime_error("same coker36");
 // Complete Gaussian source operations are persisted, not just their count.
 {std::ofstream o(prefix+"-selected-image-source-dag.bin",std::ios::binary);o.write("R150IG31",8);put(o,NB,4);
  for(int id=1;id<=NB;id++){put(o,G[id].raw,4);put(o,G[id].scale,1);put(o,G[id].ops.size(),4);for(auto a:G[id].ops){put(o,a.id,2);put(o,a.a,1);}}
  o.close();if(!o)throw std::runtime_error("selected source DAG output");}
 beat("same4318-complete-partial-inverse-ready");
 std::ifstream kin(argv[5],std::ios::binary);
 if(tag(kin)!="R150BC31"||get(kin,4)!=31||get(kin,4)!=NS||get(kin,4)!=NT)throw std::runtime_error("actual original36 source matrix");
 std::vector<uint64_t>K(NS*NT);for(auto&a:K){a=get(kin,1);if(a>30)throw std::runtime_error("initial kernel coefficients");}tail(kin);
 auto checkfree=[&](){for(int j=0;j<NT;j++)for(int k=0;k<NT;k++)if(K[(sources[freeSources[j]]-1)*NT+k]!=uint64_t(j==k))throw std::runtime_error("all36 original free coordinates not I");for(int r=1;r<=NS;r++)if(!selectedSource.count(r))for(int k=0;k<NT;k++)if(K[(r-1)*NT+k])throw std::runtime_error("selected source support escaped");};
 checkfree();
 auto product=[&](const std::vector<uint64_t>&source,uint64_t modulus){
  std::vector<uint64_t>p(NC*NT);for(int raw=1;raw<=NS;raw++)if(selectedSource.count(raw))terms(raw,[&](int c,uint64_t a){a%=modulus;for(int k=0;k<NT;k++){uint64_t v=source[(raw-1)*NT+k];if(v)p[c*NT+k]=(p[c*NT+k]+uint64_t((__uint128_t(a)*v)%modulus))%modulus;}});return p;};
 auto p0=product(K,31);for(int c:allOutputs)for(int k=0;k<NT;k++)if(p0[c*NT+k])throw std::runtime_error("selected original initial kernel invalid");
 bool allFullInitial=true;for(auto a:p0)if(a)allFullInitial=false;if(!allFullInitial)throw std::runtime_error("saved full original initial kernel identity changed");
 int completedExponent=1,firstObstructionExponent=0,obstructionRank=0;std::vector<int>fullFlags;uint64_t modulus=31;
 for(int e=2;e<=exponent;e++){
  uint64_t nextmod=modulus*31;auto before=product(K,nextmod);
  std::vector<uint8_t>rhs(NC*NT);bool allFullDivisible=true;
  for(auto a:before)if(a%modulus)allFullDivisible=false;
  for(int c:allOutputs)for(int k=0;k<NT;k++){auto v=before[c*NT+k];if(v%modulus)throw std::runtime_error("selected previous precision lost");rhs[c*NT+k]=v/modulus;}
  if(allFullDivisible)for(int c=0;c<NC;c++)if(!selectedOutput.count(c))for(int k=0;k<NT;k++)rhs[c*NT+k]=before[c*NT+k]/modulus;
  u64_matrix(prefix+"-p"+std::to_string(e)+"-before-original-product.bin","R150DP31",e,NC,NT,nextmod,before,binding);
  std::vector<uint8_t>correction(NS*NT),remainder(NT*NT);
  for(int k=0;k<NT;k++){
   Row x(5*W);for(int c=0;c<NC;c++)BitOps::set(x,W,c,rhs[c*NT+k]);std::vector<uint8_t>alpha;normal(x,alpha);
   Row y(5*SW);for(int c=0;c<SC;c++)BitOps::set(y,SW,c,BitOps::get(x,W,outputs[c]));
   std::vector<uint8_t>gam(NB+1),tj(NB+1);
   for(int c=0;c<SC;c++)if(!image[c].empty()){int a=BitOps::get(y,SW,c);if(a){gam[imageId[c]]=a;addmul(ops,y,image[c],SW,-a,c/32);}}
   for(int r=0;r<NT;r++)remainder[r*NT+k]=BitOps::get(y,SW,coker[r]);
   for(int id=NB;id>=1;id--){int c=gam[id]*G[id].scale%31;tj[id]=c;if(c)for(auto a:G[id].ops)gam[a.id]=posmod(int(gam[a.id])-a.a*c,31);}
   for(int id=1;id<=NB;id++)if(tj[id]){
    correction[(G[id].raw-1)*NT+k]=tj[id];int a=tj[id];for(int j=1;j<=NP;j++)alpha[j]=posmod(int(alpha[j])-a*H[id][j],31);
   }
   for(int z=NP-1;z>=0;z--){auto&r=B[z];int c=alpha[r.id];if(c)for(auto a:r.ops)alpha[a.id]=posmod(int(alpha[a.id])-a.a*c,31);}
   for(int id=NP;id>=1;id--){auto&r=F[id];int c=alpha[id]*r.scale%31;correction[(r.raw-1)*NT+k]=c;if(c)for(auto a:r.ops)alpha[a.id]=posmod(int(alpha[a.id])-a.a*c,31);alpha[id]=0;}
  }
  byte_matrix(prefix+"-p"+std::to_string(e)+"-selected-obstruction36.bin",NT,NT,remainder);
  auto rr=remainder;int rank=0;
  for(int c=0;c<NT;c++){int r=rank;while(r<NT&&!rr[r*NT+c])r++;if(r==NT)continue;for(int j=0;j<NT;j++)std::swap(rr[r*NT+j],rr[rank*NT+j]);int inv=ops.inv[rr[rank*NT+c]];
   for(int j=c;j<NT;j++)rr[rank*NT+j]=rr[rank*NT+j]*inv%31;for(int i=0;i<NT;i++)if(i!=rank&&rr[i*NT+c]){int a=rr[i*NT+c];for(int j=c;j<NT;j++)rr[i*NT+j]=posmod(int(rr[i*NT+j])-a*rr[rank*NT+j],31);}rank++;}
  if(rank){firstObstructionExponent=e;obstructionRank=rank;beat("first-nonzero-selected-obstruction-p"+std::to_string(e));break;}
  byte_matrix(prefix+"-p"+std::to_string(e)+"-original-correction36.bin",NS,NT,correction);
  std::vector<uint64_t>lift=K;
  for(size_t i=0;i<lift.size();i++)lift[i]=(K[i]+nextmod-modulus*uint64_t(correction[i]))%nextmod;
  K.swap(lift);checkfree();auto after=product(K,nextmod);bool allFullZero=true;uint64_t outsideNonzero=0;
  for(int c=0;c<NC;c++)for(int k=0;k<NT;k++)if(after[c*NT+k]){allFullZero=false;if(selectedOutput.count(c))throw std::runtime_error("all4354 original selected product failed");outsideNonzero++;}
  u64_matrix(prefix+"-p"+std::to_string(e)+"-original-kernel36.bin","R150DK31",e,NS,NT,nextmod,K,binding);
  u64_matrix(prefix+"-p"+std::to_string(e)+"-after-original-product.bin","R150DP31",e,NC,NT,nextmod,after,binding);
  completedExponent=e;modulus=nextmod;fullFlags.push_back(allFullZero);
  std::ofstream step(prefix+"-p"+std::to_string(e)+"-receipt.json");
  step<<"{\"status\":\"completed\",\"exponent\":"<<e<<",\"modulus\":"<<nextmod<<",\"selectedOriginalKernelIdentityVerified\":true,\"all36FreeSourceCoordinatesIdentity\":true,\"onlySame4318SourceUnitBasisUsed\":true,\"full4367OriginalKernelIdentityVerified\":"<<(allFullZero?"true":"false")<<",\"full4367PreviousProductDivisible\":"<<(allFullDivisible?"true":"false")<<",\"outsideSelected13NonzeroCoordinates\":"<<outsideNonzero<<",\"selectedObstructionRank\":0,\"inputBinding\":\""<<binding<<"\",\"elapsedSeconds\":"<<std::setprecision(17)<<sec()<<"}\n";step.close();if(!step)throw std::runtime_error("step receipt");
  beat("p"+std::to_string(e)+"-selected-kernel36-complete");
 }
 std::ofstream o(prefix+"-receipt.json");o<<std::setprecision(17)<<"{\"status\":\"completed\",\"nativeStatus\":\"selected-original-kernel36-dixon-complete\",\"inputBinding\":\""<<binding<<"\",\"maximumRequestedExponent\":"<<exponent<<",\"completedExponent\":"<<completedExponent<<",\"firstObstructionExponent\":"<<firstObstructionExponent<<",\"firstObstructionRank\":"<<obstructionRank<<",\"selectedBaseRank\":4318,\"completeKernelDimension\":36,\"all36FreeSourceCoordinatesIdentity\":true,\"sameSelected4354Retained\":true,\"allSelectedOriginalProductsVerified\":true,\"allFullOriginalProductsSaved\":true,\"rationalKernelIdentityNotClaimed\":true,\"selectedImageSourceOperations\":"<<imageOperations<<",\"elapsedSeconds\":"<<sec()<<",\"all4354SelectedOutputIndicesZeroBased\":";array(o,allOutputs);o<<",\"normalizedFreeOriginalSourceRows\":[";
 for(int i=0;i<NT;i++){if(i)o<<',';o<<sources[freeSources[i]];}o<<"],\"full4367KernelFlagsByCompletedExponent\":";array(o,fullFlags);o<<"}\n";o.close();if(!o)throw std::runtime_error("Dixon receipt output");
 std::cout<<"{\"status\":\"selected-original-kernel36-dixon-complete\",\"completedExponent\":"<<completedExponent<<",\"firstObstructionExponent\":"<<firstObstructionExponent<<",\"firstObstructionRank\":"<<obstructionRank<<",\"allSelectedOriginalProductsVerified\":true}\n"<<std::flush;
 return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 1;}}

