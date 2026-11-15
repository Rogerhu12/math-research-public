// Original selected constant infinity matrix: a complete 36-source Bockstein.
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
int main(int argc,char**argv){try{
 if(argc!=7)throw std::runtime_error("usage native-model prepared-model forward backward out-prefix remaining-seconds");
 auto start=std::chrono::steady_clock::now();double limit=std::stod(argv[6]);
 if(!(limit>0&&limit<=300))throw std::runtime_error("explicit small positive budget");
 auto sec=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 std::string prefix=argv[5];
 auto beat=[&](const std::string&s){std::cout<<"{\"phase\":\""<<s<<"\",\"elapsedSeconds\":"<<sec()<<"}\n"<<std::flush;
  if(sec()>limit-1)throw std::runtime_error("remaining mathematical budget exhausted after "+s);};
 Model M(argv[1]);constexpr int NT=36,NC=4367,NS=6188,NP=3333,SC=1021;
 constexpr int W=(NC+31)/32,SW=(SC+31)/32;
 std::ifstream in(argv[2]);std::string magic,binding;in>>magic>>binding;
 if(magic!="R150_SELECTED_INFINITY_CONSTANT_961_V1"||binding.size()!=64)throw std::runtime_error("prepared constant model");
 std::array<std::array<int,77>,17> P2{};
 for(int e=0;e<17;e++)for(int j=0;j<77;j++){
  in>>P2[e][j];if(!in||P2[e][j]<0||P2[e][j]>=961)throw std::runtime_error("primitive mod961 value");
  int expected=e<11?(j<11?M.L[e][j][10]:M.Q[e][j-11]):(j<11?0:M.G[e-11][j-11][5]);
  if(P2[e][j]%31!=expected)throw std::runtime_error("same primitive infinity coefficient");
 }
 int n;in>>n;if(n!=1021)throw std::runtime_error("selected original sources");
 std::vector<int> sources(n);std::set<int> selectedSet;
 for(auto&r:sources){in>>r;if(r<1||r>NS||!selectedSet.insert(r).second)throw std::runtime_error("original selected source dictionary");}
 in>>n;if(n!=1021)throw std::runtime_error("selected original outputs");std::vector<int> outputs(n);std::set<int> outputSet;
 for(auto&c:outputs){in>>c;if(c<0||c>=NC||!outputSet.insert(c).second)throw std::runtime_error("selected output dictionary");}
 in>>n;if(n!=985)throw std::runtime_error("actual paid selected rank");std::vector<int> independent(n);std::set<int> independentSet;
 for(auto&i:independent){in>>i;if(i<0||i>=SC||!independentSet.insert(i).second)throw std::runtime_error("independent source indices");}
 in>>n;if(n!=NT)throw std::runtime_error("complete selected kernel dimension");
 std::vector<uint8_t> K(NT*SC);for(auto&a:K){int v;in>>v;if(v<0||v>=31)throw std::runtime_error("source kernel residue");a=v;}
 if(!in||in>>magic)throw std::runtime_error("prepared constant tail");
 std::array<int,NP+1> rawById{},pivotById{};std::unordered_map<int,uint64_t> prePivot;
 for(auto&s:M.pre){prePivot[s.raw]=s.pivot;if(selectedSet.count(s.raw))throw std::runtime_error("prebasis and selected nonbasis overlap");selectedSet.insert(s.raw);}
 if(selectedSet.size()!=4354)throw std::runtime_error("same selected4354 support");
 std::vector<uint64_t> termkeys;termkeys.insert(termkeys.end(),M.var.begin(),M.var.end());
 for(auto[a,b]:M.quadratic)termkeys.push_back(M.var[a]+M.var[b]);
 auto terms=[&](int raw,auto action){
  int e=(raw-1)%17;auto mult=M.multipliers[(raw-1)/17];
  for(int j=0;j<77;j++)if(P2[e][j])action(M.component.at(mult+termkeys[j]),P2[e][j]);
 };
 auto rawrow=[&](int raw){Row x(5*W);terms(raw,[&](int c,int a){BitOps::set(x,W,c,a%31);});return x;};
 std::ifstream f(argv[3],std::ios::binary),b(argv[4],std::ios::binary);
 if(tag(f)!="R150PB31"||get(f,4)!=NP||tag(b)!="R150RJ31"||get(b,4)!=NP)throw std::runtime_error("same prebasis DAG headers");
 std::vector<Forward> F(NP+1);uint64_t forwardCount=0,backCount=0;
 for(int id=1;id<=NP;id++){
  auto &r=F[id];r.raw=get(f,4);r.scale=get(f,1);int count=get(f,4);
  if(!prePivot.count(r.raw)||r.scale<1||r.scale>=31||count<0||count>NP)throw std::runtime_error("forward original source");
  rawById[id]=r.raw;pivotById[id]=M.component.at(prePivot.at(r.raw));
  for(int j=0;j<count;j++){Op a{int(get(f,2)),int(get(f,1))};if(a.id<1||a.id>=id||a.a<1||a.a>=31)throw std::runtime_error("forward operation");r.ops.push_back(a);}forwardCount+=count;
 }
 tail(f);std::vector<Backward>B(NP);std::set<int> seenBack;
 for(auto&r:B){r.id=get(b,2);int count=get(b,4);if(r.id<1||r.id>NP||!seenBack.insert(r.id).second||count<0||count>NP)throw std::runtime_error("backward row");
  for(int j=0;j<count;j++){Op a{int(get(b,2)),int(get(b,1))};if(a.id<1||a.id>NP||a.id==r.id||a.a<1||a.a>=31)throw std::runtime_error("backward operation");r.ops.push_back(a);}backCount+=count;}
 tail(b);if(forwardCount!=782976||backCount!=1010703)throw std::runtime_error("same complete paid operation counts");
 BitOps ops;std::vector<Row> phi(NP+1);
 for(int id=1;id<=NP;id++){
  Row x=rawrow(F[id].raw);for(auto a:F[id].ops)addmul(ops,x,phi[a.id],W,-a.a);
  ops.multiple(x,W,0,F[id].scale);if(BitOps::get(x,W,pivotById[id])!=1)throw std::runtime_error("actual infinity unit pivot");
  phi[id]=std::move(x);
  if(id%500==0)beat("forward-prebasis-"+std::to_string(id));
 }
 for(size_t i=0;i<B.size();i++){
  const auto&r=B[i];for(auto a:r.ops)addmul(ops,phi[r.id],phi[a.id],W,-a.a);
  if(i%500==499)beat("backward-prebasis-"+std::to_string(i+1));
 }
 std::vector<int> order(NP);std::iota(order.begin(),order.end(),1);std::sort(order.begin(),order.end(),[&](int a,int b){return pivotById[a]<pivotById[b];});
 for(int id:order)if(BitOps::get(phi[id],W,pivotById[id])!=1)throw std::runtime_error("retained prebasis leading1");
 auto normal=[&](Row &x,std::vector<uint8_t>*coeff){
  if(coeff)coeff->assign(NP+1,0);
  for(int id:order){int a=BitOps::get(x,W,pivotById[id]);if(a){addmul(ops,x,phi[id],W,-a,pivotById[id]/32);if(coeff)(*coeff)[id]=a;}}
  for(int id:order)if(BitOps::get(x,W,pivotById[id]))throw std::runtime_error("normal form retained original prebasis component");
 };
 beat("actual-infinity-prebasis-restored");
 std::vector<uint8_t> kernels(NS*NT),beta((NP+1)*NT);
 for(int k=0;k<NT;k++){
  Row x(5*W);
  for(int j=0;j<SC;j++){int a=K[k*SC+j];if(!a)continue;int raw=sources[j];kernels[(raw-1)*NT+k]=a;terms(raw,[&](int c,int v){int w=BitOps::get(x,W,c);assign(x,W,c,(w+a*(v%31))%31);});}
  std::vector<uint8_t> coeff;normal(x,&coeff);
  if(!iszero(x))throw std::runtime_error("paid selected K is not full original quotient kernel");
  for(int id=1;id<=NP;id++)beta[id*NT+k]=coeff[id];
 }
 for(int z=NP-1;z>=0;z--){auto&r=B[z];for(int k=0;k<NT;k++){int c=beta[r.id*NT+k];if(c)for(auto a:r.ops)beta[a.id*NT+k]=posmod(int(beta[a.id*NT+k])-a.a*c,31);}}
 for(int id=NP;id>=1;id--){auto&r=F[id];for(int k=0;k<NT;k++){int c=beta[id*NT+k]*r.scale%31;kernels[(r.raw-1)*NT+k]=posmod(int(kernels[(r.raw-1)*NT+k])-c,31);
   if(c)for(auto a:r.ops)beta[a.id*NT+k]=posmod(int(beta[a.id*NT+k])-a.a*c,31);beta[id*NT+k]=0;}}
 if(std::any_of(beta.begin(),beta.end(),[](auto a){return a!=0;}))throw std::runtime_error("original coefficient transpose not complete");
 for(int raw=1;raw<=NS;raw++)if(!selectedSet.count(raw))for(int k=0;k<NT;k++)if(kernels[(raw-1)*NT+k])throw std::runtime_error("kernel escaped same selected4354 sources");
 byte_matrix(prefix+"-original-kernel36.bin",NS,NT,kernels);
 beat("complete-original-selected-kernels-restored");
 std::vector<uint16_t> product(NC*NT);
 for(int raw=1;raw<=NS;raw++)if(selectedSet.count(raw))terms(raw,[&](int c,int a){for(int k=0;k<NT;k++){int v=kernels[(raw-1)*NT+k];if(v)product[c*NT+k]=(product[c*NT+k]+a*v)%961;}});
 std::vector<uint8_t> quotient(NC*NT);
 for(size_t z=0;z<product.size();z++){if(product[z]%31)throw std::runtime_error("full original4367 integer product not divisible31 at "+std::to_string(z));quotient[z]=product[z]/31;}
 std::ofstream prod(prefix+"-original-product-mod961.bin",std::ios::binary);prod.write("R150BP31",8);put(prod,961,4);put(prod,NC,4);put(prod,NT,4);for(auto a:product)put(prod,a,2);prod.close();if(!prod)throw std::runtime_error("full original product save");
 byte_matrix(prefix+"-original-product-div31.bin",NC,NT,quotient);
 beat("full-original-integer-product-verified");
 std::vector<Row> image(SC);std::vector<int> imageSources(SC,-1);std::vector<uint8_t> originalBasis;
 int imageRank=0;
 auto lead=[&](const Row &x,int WW,int NN){for(int w=0;w<WW;w++){uint32_t z=0;for(int bit=0;bit<5;bit++)z|=x[bit*WW+w];if(z){int c=w*32+__builtin_ctz(z);if(c>=NN)throw std::runtime_error("nonzero padding");return c;}}return -1;};
 for(int j:independent){
  Row x=rawrow(sources[j]);normal(x,nullptr);Row y(5*SW);
  for(int j=0;j<SC;j++){int a=BitOps::get(x,W,outputs[j]);originalBasis.push_back(a);BitOps::set(y,SW,j,a);}
  while(true){int c=lead(y,SW,SC);if(c<0)throw std::runtime_error("paid independent source became dependent");
   int a=BitOps::get(y,SW,c);if(image[c].empty()){ops.multiple(y,SW,0,ops.inv[a]);image[c]=std::move(y);imageSources[c]=sources[j];imageRank++;break;}
   addmul(ops,y,image[c],SW,-a,c/32);
  }
  if(imageRank%200==0)beat("selected-image-basis-"+std::to_string(imageRank));
 }
 if(imageRank!=985||originalBasis.size()!=size_t(985)*SC)throw std::runtime_error("actual selected985 image");
 byte_matrix(prefix+"-actual-selected-basis985.bin",985,SC,originalBasis);
 std::vector<int> free;for(int c=0;c<SC;c++)if(image[c].empty())free.push_back(c);
 if(free.size()!=NT)throw std::runtime_error("same selected coker36");
 std::vector<uint8_t> nf(NC*NT),residue(NT*NT);
 for(int k=0;k<NT;k++){
  Row x(5*W);for(int c=0;c<NC;c++)BitOps::set(x,W,c,quotient[c*NT+k]);normal(x,nullptr);
  Row y(5*SW);for(int c=0;c<NC;c++)nf[c*NT+k]=BitOps::get(x,W,c);
  for(int j=0;j<SC;j++)BitOps::set(y,SW,j,nf[outputs[j]*NT+k]);
  for(int c=0;c<SC;c++)if(!image[c].empty()){int a=BitOps::get(y,SW,c);if(a)addmul(ops,y,image[c],SW,-a,c/32);}
  for(int c=0;c<SC;c++)if(!image[c].empty()&&BitOps::get(y,SW,c))throw std::runtime_error("selected quotient retained image coordinate");
  for(int r=0;r<NT;r++)residue[r*NT+k]=BitOps::get(y,SW,free[r]);
 }
 byte_matrix(prefix+"-full-prebasis-normal-product.bin",NC,NT,nf);
 byte_matrix(prefix+"-selected-coker36-bockstein.bin",NT,NT,residue);
 auto a=residue;int rank=0;std::vector<int> pivots;
 for(int c=0;c<NT;c++){int r=rank;while(r<NT&&!a[r*NT+c])r++;if(r==NT)continue;
  for(int j=0;j<NT;j++)std::swap(a[r*NT+j],a[rank*NT+j]);int inv=ops.inv[a[rank*NT+c]];
  for(int j=c;j<NT;j++)a[rank*NT+j]=a[rank*NT+j]*inv%31;
  for(int i=0;i<NT;i++)if(i!=rank&&a[i*NT+c]){int v=a[i*NT+c];for(int j=c;j<NT;j++)a[i*NT+j]=posmod(int(a[i*NT+j])-v*a[rank*NT+j],31);}
  pivots.push_back(c);rank++;
 }
 if(rank>22)throw std::runtime_error("Bockstein exceeds proven characteristic-zero rank upper bound");
 byte_matrix(prefix+"-selected-coker36-bockstein-rref.bin",NT,NT,a);
 std::ofstream o(prefix+"-receipt.json");
 o<<std::setprecision(17)<<"{\"status\":\"completed\",\"nativeStatus\":\"original-selected-constant-bockstein-complete\",\"inputBinding\":\""<<binding<<"\",\"field\":31,\"integerModulus\":961,\"selectedSourceCount\":4354,\"originalSourceCount\":6188,\"fullOriginalOutputCount\":4367,\"completeKernelDimension\":36,\"selectedBaseRank\":4318,\"bocksteinRank\":"<<rank<<",\"characteristicZeroSelectedRankLowerBound\":"<<4318+rank<<",\"characteristicZeroSelectedRankUpperBound\":4340,\"characteristicZeroSelectedRankProved\":"<<(rank==22?"true":"false")<<",\"fullOriginalIntegerProductVerified\":true,\"allOriginalCoordinatesDivisible31\":true,\"sameSelectedSourceSupportVerified\":true,\"onlySelectedImageQuotiented\":true,\"all36KernelDirectionsRetained\":true,\"originalProductCoordinates\":"<<NC*NT<<",\"forwardOperations\":"<<forwardCount<<",\"backwardOperations\":"<<backCount<<",\"elapsedSeconds\":"<<sec()<<",\"selectedCokerOutputIndicesZeroBased\":";
 array(o,free);o<<",\"selectedCokerOriginalOutputIndicesZeroBased\":[";for(int i=0;i<NT;i++){if(i)o<<',';o<<outputs[free[i]];}o<<"],\"bocksteinPivotSourceIndicesZeroBased\":";array(o,pivots);o<<"}\n";o.close();if(!o)throw std::runtime_error("native receipt write");
 beat("selected-constant-bockstein-complete");
 std::cout<<"{\"status\":\"original-selected-constant-bockstein-complete\",\"bocksteinRank\":"<<rank<<",\"fullOriginalIntegerProductVerified\":true,\"sameSelectedSourceSupportVerified\":true,\"onlySelectedImageQuotiented\":true,\"all36KernelDirectionsRetained\":true,\"characteristicZeroSelectedRankLowerBound\":"<<4318+rank<<",\"characteristicZeroSelectedRankUpperBound\":4340}\n"<<std::flush;
 return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 1;}}
