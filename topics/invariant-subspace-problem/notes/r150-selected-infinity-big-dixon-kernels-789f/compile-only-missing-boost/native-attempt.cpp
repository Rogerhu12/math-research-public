// Same original selected infinity matrix: 36 normalized Dixon kernel lifts.
// Only the already paid constant N source DAG is replayed. Every integer
// product uses the original primitive coefficients modulo 31^2.
#include "2026-11-15-r150-saturated-global-common-789f.hpp"
#include <numeric>
#include <iomanip>
#include <filesystem>
#include <boost/multiprecision/cpp_int.hpp>
#include <csignal>
using boost::multiprecision::cpp_int;
static volatile std::sig_atomic_t stop_requested=0;
static void on_signal(int){stop_requested=1;}
static int field31(const cpp_int&x){int a=(x%31).convert_to<int>();return a<0?a+31:a;}
static void write_z(std::ostream&o,const cpp_int&x){std::vector<unsigned char>b;cpp_int a=x<0?-x:x;if(a!=0)export_bits(a,std::back_inserter(b),8,false);if(b.size()>65535)throw std::runtime_error("integer output length");o.put(x<0?1:0);o.put(char(b.size()));o.put(char(b.size()>>8));o.write((char*)b.data(),b.size());}
static cpp_int read_z(std::istream&in){int sign=in.get(),l0=in.get(),l1=in.get();if(sign<0||sign>1||l0<0||l1<0)throw std::runtime_error("signed integer header");int n=l0+256*l1;if(n>4096)throw std::runtime_error("integer input length");std::vector<unsigned char>b(n);in.read((char*)b.data(),n);if(!in||(!n&&sign)||(n&&!b.back()))throw std::runtime_error("noncanonical integer");cpp_int a=0;if(n)import_bits(a,b.begin(),b.end(),8,false);return sign?-a:a;}
static void big_matrix(const std::string&file,const char*magic,int n,int rows,int cols,const std::vector<cpp_int>&v,const std::string&binding){if(v.size()!=size_t(rows)*cols)throw std::runtime_error("big matrix shape");std::string temp=file+".partial";std::ofstream o(temp,std::ios::binary);o.write(magic,8);for(uint32_t a:std::vector<uint32_t>{31,uint32_t(n),uint32_t(rows),uint32_t(cols)})for(int k=0;k<4;k++)o.put(char(a>>(8*k)));o.write(binding.data(),64);for(const auto&a:v)write_z(o,a);o.close();if(!o)throw std::runtime_error("big matrix save");std::filesystem::rename(temp,file);}

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
 if(argc!=9)throw std::runtime_error("usage native-model prepared-big-model forward backward actual-start-source selected-image-dag prefix remaining-seconds");
 auto start=std::chrono::steady_clock::now();double limit=std::stod(argv[8]);
 if(!(limit>0&&limit<=120))throw std::runtime_error("explicit <=120 second native budget");
 auto sec=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 auto beat=[&](std::string phase){std::cout<<"{\"phase\":\""<<phase<<"\",\"elapsedSeconds\":"<<sec()<<"}\n"<<std::flush;};
 std::string prefix=argv[7];std::signal(SIGTERM,on_signal);std::signal(SIGINT,on_signal);Model M(argv[1]);constexpr int NS=6188,NC=4367,NP=3333,SC=1021,NB=985,NT=36,W=(NC+31)/32,SW=(SC+31)/32;
 std::ifstream in(argv[2]);std::string magic,binding,oldBinding;int startExponent,exponent;in>>magic>>binding>>oldBinding>>startExponent>>exponent;
 if(magic!="R150_SELECTED_INFINITY_DIXON_BIG_V1"||binding.size()!=64||oldBinding.size()!=64||startExponent<4||startExponent>=exponent||exponent>32)throw std::runtime_error("exact integer Dixon model header");
 std::array<std::array<cpp_int,77>,17>A{};
 for(int e=0;e<17;e++)for(int j=0;j<77;j++){in>>A[e][j];int v=e<11?(j<11?M.L[e][j][10]:M.Q[e][j-11]):(j<11?0:M.G[e-11][j-11][5]);if(!in||field31(A[e][j])!=v)throw std::runtime_error("same exact integer constant coefficient");}
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
 auto rawrow=[&](int raw){Row x(5*W);terms(raw,[&](int c,const cpp_int&a){BitOps::set(x,W,c,field31(a));});return x;};
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
 std::ifstream gd(argv[6],std::ios::binary);if(tag(gd)!="R150IG31"||get(gd,4)!=NB)throw std::runtime_error("same paid985 source DAG");
 for(int id=1;id<=NB;id++){auto&r=G[id];r.raw=get(gd,4);r.scale=get(gd,1);int count=get(gd,4);if(r.raw!=sources[independent[id-1]]||r.scale<1||r.scale>30||count<0||count>=id)throw std::runtime_error("paid985 source row");for(int j=0;j<count;j++){Op a{int(get(gd,2)),int(get(gd,1))};if(a.id<1||a.id>=id||a.a<1||a.a>30)throw std::runtime_error("paid985 operation");r.ops.push_back(a);}imageOperations+=count;}
 tail(gd);if(imageOperations!=462972)throw std::runtime_error("same paid985 full source operation count");
 std::vector<int>gPivot(NB+1);
 for(int id=1;id<=NB;id++){
  Row x=rawrow(G[id].raw);normal(x,H[id]);Row y(5*SW);for(int c=0;c<SC;c++)BitOps::set(y,SW,c,BitOps::get(x,W,outputs[c]));
  for(auto a:G[id].ops)addmul(ops,y,image[gPivot[a.id]],SW,-a.a);
  ops.multiple(y,SW,0,G[id].scale);int c=lead(y);if(c<0||!image[c].empty()||BitOps::get(y,SW,c)!=1)throw std::runtime_error("paid985 leading unit");
  image[c]=std::move(y);imageId[c]=id;gPivot[id]=c;
 }
 std::vector<int>coker;for(int c=0;c<SC;c++)if(image[c].empty())coker.push_back(c);if(coker.size()!=NT)throw std::runtime_error("same coker36");
 beat("same4318-complete-partial-inverse-ready");

 std::ifstream kin(argv[5],std::ios::binary);auto kmagic=tag(kin);
 if(get(kin,4)!=31||get(kin,4)!=uint64_t(startExponent)||get(kin,4)!=NS||get(kin,4)!=NT)throw std::runtime_error("actual start source dimensions");
 std::vector<cpp_int>K(NS*NT);char oldtag[64];cpp_int power=1;for(int i=0;i<startExponent;i++)power*=31;
 if(kmagic=="R150DK31"){
  if(startExponent!=4||get(kin,8)!=923521)throw std::runtime_error("actual p4 source modulus");
  kin.read(oldtag,64);if(std::string(oldtag,64)!=oldBinding)throw std::runtime_error("actual p4 semantic binding");
  for(auto&a:K){uint64_t v=get(kin,8);if(v>=923521)throw std::runtime_error("actual p4 residue");a=v;}
 }else if(kmagic=="R150BK31"){
  kin.read(oldtag,64);if(std::string(oldtag,64)!=oldBinding)throw std::runtime_error("actual big source binding");
  for(auto&a:K)a=read_z(kin);
 }else throw std::runtime_error("actual start source format");
 tail(kin);
 auto checkfree=[&](){for(int j=0;j<NT;j++)for(int k=0;k<NT;k++)if(K[(sources[freeSources[j]]-1)*NT+k]!=(j==k?1:0))throw std::runtime_error("all36 original free source coordinates");for(int r=1;r<=NS;r++)if(!selectedSource.count(r))for(int k=0;k<NT;k++)if(K[(r-1)*NT+k]!=0)throw std::runtime_error("source support escaped");};
 checkfree();
 struct Term {int c;const cpp_int*a;};std::vector<std::vector<Term>>rowterms(NS+1);
 for(int raw:selectedSource){int e=(raw-1)%17;auto mult=M.multipliers[(raw-1)/17];for(int j=0;j<77;j++)if(A[e][j]!=0)rowterms[raw].push_back({M.component.at(mult+termsKeys[j]),&A[e][j]});}
 auto product=[&](const std::vector<cpp_int>&source){std::vector<cpp_int>p(NC*NT);for(int raw:selectedSource)for(auto t:rowterms[raw])for(int k=0;k<NT;k++)if(source[(raw-1)*NT+k]!=0)p[t.c*NT+k]+=(*t.a)*source[(raw-1)*NT+k];return p;};
 auto smallProduct=[&](const std::vector<uint8_t>&source){std::vector<cpp_int>p(NC*NT);for(int raw:selectedSource)for(auto t:rowterms[raw])for(int k=0;k<NT;k++){int a=source[(raw-1)*NT+k];if(a)p[t.c*NT+k]+=(*t.a)*a;}return p;};
 auto initialProduct=product(K);std::vector<cpp_int>E(NC*NT);
 for(size_t i=0;i<E.size();i++){if(initialProduct[i]%power!=0)throw std::runtime_error("full exact initial product not divisible at paid precision");E[i]=initialProduct[i]/power;}
 big_matrix(prefix+"-initial-p"+std::to_string(startExponent)+"-exact-original-product.bin","R150BX31",startExponent,NC,NT,initialProduct,binding);
 big_matrix(prefix+"-initial-p"+std::to_string(startExponent)+"-exact-residual.bin","R150BE31",startExponent,NC,NT,E,binding);
 initialProduct.clear();initialProduct.shrink_to_fit();
 beat("paid-p"+std::to_string(startExponent)+"-fresh-exact-original-product");
 int completed=startExponent,firstObstructionExponent=0,firstObstructionRank=0,firstOutsideFailureExponent=0;
 bool timed=false;std::vector<int>checkpoints;
 auto checkpoint=[&](int n){
  checkfree();auto P=product(K);for(size_t i=0;i<P.size();i++)if(P[i]!=power*E[i])throw std::runtime_error("fresh exact original product differs from complete residual recurrence");
  big_matrix(prefix+"-p"+std::to_string(n)+"-exact-source36.bin","R150BK31",n,NS,NT,K,binding);
  big_matrix(prefix+"-p"+std::to_string(n)+"-exact-original-product.bin","R150BX31",n,NC,NT,P,binding);
  big_matrix(prefix+"-p"+std::to_string(n)+"-exact-residual.bin","R150BE31",n,NC,NT,E,binding);
  std::ofstream q(prefix+"-p"+std::to_string(n)+"-receipt.json");q<<std::setprecision(17)<<"{\"status\":\"completed\",\"exponent\":"<<n<<",\"same36FreeOriginalCoordinatesIdentity\":true,\"all4367FreshExactOriginalProductsVerified\":true,\"all4367OriginalCoordinatesDivisibleByFullModulus\":true,\"exactResidualRecurrenceVerified\":true,\"allActualOriginalSourcesRetained\":true,\"inputBinding\":\""<<binding<<"\",\"elapsedSeconds\":"<<sec()<<"}\n";q.close();if(!q)throw std::runtime_error("checkpoint receipt");checkpoints.push_back(n);beat("p"+std::to_string(n)+"-exact-full-checkpoint");
 };
 auto solve=[&](const std::vector<uint8_t>&rhs,std::vector<uint8_t>&correction,std::vector<uint8_t>&remainder){
  correction.assign(NS*NT,0);remainder.assign(NT*NT,0);
  for(int k=0;k<NT;k++){
   Row x(5*W);for(int c=0;c<NC;c++)BitOps::set(x,W,c,rhs[c*NT+k]);std::vector<uint8_t>alpha;normal(x,alpha);
   Row y(5*SW);for(int c=0;c<SC;c++)BitOps::set(y,SW,c,BitOps::get(x,W,outputs[c]));
   std::vector<uint8_t>gam(NB+1),tj(NB+1);
   for(int c=0;c<SC;c++)if(!image[c].empty()){int a=BitOps::get(y,SW,c);if(a){gam[imageId[c]]=a;addmul(ops,y,image[c],SW,-a,c/32);}}
   for(int r=0;r<NT;r++)remainder[r*NT+k]=BitOps::get(y,SW,coker[r]);
   for(int id=NB;id>=1;id--){int c=gam[id]*G[id].scale%31;tj[id]=c;if(c)for(auto a:G[id].ops)gam[a.id]=posmod(int(gam[a.id])-a.a*c,31);}
   for(int id=1;id<=NB;id++)if(tj[id]){correction[(G[id].raw-1)*NT+k]=tj[id];int a=tj[id];for(int j=1;j<=NP;j++)alpha[j]=posmod(int(alpha[j])-a*H[id][j],31);}
   for(int z=NP-1;z>=0;z--){auto&r=B[z];int c=alpha[r.id];if(c)for(auto a:r.ops)alpha[a.id]=posmod(int(alpha[a.id])-a.a*c,31);}
   for(int id=NP;id>=1;id--){auto&r=F[id];int c=alpha[id]*r.scale%31;correction[(r.raw-1)*NT+k]=c;if(c)for(auto a:r.ops)alpha[a.id]=posmod(int(alpha[a.id])-a.a*c,31);alpha[id]=0;}
  }
 };
 for(int n=startExponent;n<exponent;n++){
  if(stop_requested||sec()>limit-std::min(15.0,limit/4)){timed=true;break;}
  int e=n+1;std::vector<uint8_t>rhs(NC*NT),correction,remainder;for(size_t i=0;i<E.size();i++)rhs[i]=field31(E[i]);
  solve(rhs,correction,remainder);byte_matrix(prefix+"-p"+std::to_string(e)+"-selected-obstruction36.bin",NT,NT,remainder);
  auto rr=remainder;int rank=0;for(int c=0;c<NT;c++){int r=rank;while(r<NT&&!rr[r*NT+c])r++;if(r==NT)continue;for(int j=0;j<NT;j++)std::swap(rr[r*NT+j],rr[rank*NT+j]);int inv=ops.inv[rr[rank*NT+c]];
   for(int j=c;j<NT;j++)rr[rank*NT+j]=rr[rank*NT+j]*inv%31;for(int i=0;i<NT;i++)if(i!=rank&&rr[i*NT+c]){int a=rr[i*NT+c];for(int j=c;j<NT;j++)rr[i*NT+j]=posmod(int(rr[i*NT+j])-a*rr[rank*NT+j],31);}rank++;}
  if(rank){firstObstructionExponent=e;firstObstructionRank=rank;break;}
  byte_matrix(prefix+"-p"+std::to_string(e)+"-original-correction36.bin",NS,NT,correction);
  auto AC=smallProduct(correction);bool full=true;
  for(int c=0;c<NC;c++)for(int k=0;k<NT;k++)if((E[c*NT+k]-AC[c*NT+k])%31!=0){if(selectedOutput.count(c))throw std::runtime_error("same selected full correction product failed");full=false;}
  if(!full){firstOutsideFailureExponent=e;big_matrix(prefix+"-p"+std::to_string(e)+"-unpaid-extra-row-numerator.bin","R150BE31",e,NC,NT,AC,binding);break;}
  for(size_t i=0;i<K.size();i++)if(correction[i])K[i]-=power*int(correction[i]);
  for(size_t i=0;i<E.size();i++)E[i]=(E[i]-AC[i])/31;
  power*=31;completed=e;checkfree();
  std::ofstream ledger(prefix+"-digit-ledger.json.partial");ledger<<"{\"status\":\"completed-through-digit\",\"completedExponent\":"<<completed<<",\"startExponent\":"<<startExponent<<",\"fullOriginalResidualRecurrenceVerified\":true,\"inputBinding\":\""<<binding<<"\"}\n";ledger.close();if(!ledger)throw std::runtime_error("digit ledger");std::filesystem::rename(prefix+"-digit-ledger.json.partial",prefix+"-digit-ledger.json");
  if(e==8||e==16||e==32)checkpoint(e);else beat("complete-exact-digit-p"+std::to_string(e));
 }
 if(checkpoints.empty()||checkpoints.back()!=completed)checkpoint(completed);
 std::ofstream o(prefix+"-receipt.json");o<<std::setprecision(17)<<"{\"status\":\""<<(timed?"checkpointed-time-budget":"completed")<<"\",\"nativeStatus\":\"exact-original-dixon36-big-integer\",\"inputBinding\":\""<<binding<<"\",\"startExponent\":"<<startExponent<<",\"maximumRequestedExponent\":"<<exponent<<",\"completedExponent\":"<<completed<<",\"firstObstructionExponent\":"<<firstObstructionExponent<<",\"firstObstructionRank\":"<<firstObstructionRank<<",\"firstOutsideFailureExponent\":"<<firstOutsideFailureExponent<<",\"all36FreeSourceCoordinatesIdentity\":true,\"sameSelected4354Retained\":true,\"all4367ExactOriginalProductsVerified\":true,\"allFullOriginalResidualsRetained\":true,\"arbitraryPrecisionIntegerArithmetic\":true,\"selectedImageSourceOperations\":"<<imageOperations<<",\"elapsedSeconds\":"<<sec()<<",\"savedCheckpointExponents\":";array(o,checkpoints);o<<",\"all4354SelectedOutputIndicesZeroBased\":";array(o,allOutputs);o<<",\"normalizedFreeOriginalSourceRows\":[";
 for(int j=0;j<NT;j++){if(j)o<<',';o<<sources[freeSources[j]];}o<<"]}\n";o.close();if(!o)throw std::runtime_error("final exact receipt");
 std::cout<<"{\"status\":\""<<(timed?"checkpointed-time-budget":"exact-original-dixon36-big-integer-complete")<<"\",\"completedExponent\":"<<completed<<",\"firstObstructionExponent\":"<<firstObstructionExponent<<",\"firstObstructionRank\":"<<firstObstructionRank<<",\"firstOutsideFailureExponent\":"<<firstOutsideFailureExponent<<",\"all4367ExactOriginalProductsVerified\":true}\n"<<std::flush;
 return timed?75:0;
}catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 1;}}

