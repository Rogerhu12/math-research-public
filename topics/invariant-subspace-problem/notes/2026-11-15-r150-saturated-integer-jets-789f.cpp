// Exact integer Taylor source combinations and all original17 products modulo31^6.
// Every source row is materialized, and every p division is checked before exporting jets.
#include "2026-11-15-r150-saturated-local-common-789f.hpp"
#include <cmath>
constexpr int MOD=887503681;
static int power31(int n){int z=1;while(n--)z*=31;return z;}
struct Edge{int out=0;std::vector<int>c;};
struct Family{
 std::string file,magic;int n=0,l=0,mod=0,width=0,bound=0,stride=0,words=0,kind=0,done=0;
 std::vector<int>labels,exponents,costs;std::vector<std::vector<Edge>>edges;std::ifstream in;
 std::vector<uint32_t>row;Row packed;
 void open(const std::string&path,const std::vector<int>&expected,const sb::Model&m){
  file=path;in.open(path,std::ios::binary);magic=sb::tag(in);
  if(magic=="R150KK31"){
   for(int v:{31,6188,200,85})if(sb::get(in,4)!=uint64_t(v))throw std::runtime_error("original K200 family dimensions");
   n=200;mod=31;width=1;costs.resize(n);labels.resize(n);
   for(int j=0;j<n;j++){int graph=sb::get(in,4);labels[j]=sb::get(in,2);costs[j]=sb::get(in,2);int source=sb::get(in,4),raw=sb::get(in,4);
    if(source<1||source>2195||raw<1||raw>6188||costs[j]!=(j<160?80:j<198?81:85))throw std::runtime_error("same K200 family source map");}
  }else if(magic=="R150PS31"||magic=="R150P431"||magic=="R150P531"||magic=="R150P631"){
   if(sb::get(in,4)!=31)throw std::runtime_error("primitive source prime");mod=sb::get(in,4);
   if(mod!=31&&mod!=961&&mod!=29791&&mod!=923521&&mod!=28629151&&mod!=MOD)throw std::runtime_error("primitive source modulus");
   if(sb::get(in,4)!=6188)throw std::runtime_error("all6188 primitive source rows");n=sb::get(in,4);bound=sb::get(in,4);
   if(n<1||n>256||bound<1||bound>796)throw std::runtime_error("bounded actual source family");
   width=magic=="R150PS31"?2:4;labels.resize(n);for(int&v:labels)v=sb::get(in,2);
  }else if(magic=="R150SP31"){
   if(sb::get(in,4)!=31||sb::get(in,4)!=6188)throw std::runtime_error("packed actual original source rows");
   n=sb::get(in,4);l=sb::get(in,4);stride=sb::get(in,4);kind=sb::get(in,4);done=sb::get(in,4);bound=sb::get(in,4);
   words=(n+31)/32;if(n<1||n>256||l<jt::L||l>20||stride!=words*l||kind!=2||done!=6188)throw std::runtime_error("complete original packed source family");
   std::string b(64,' ');in.read(b.data(),64);labels.resize(n);for(int&v:labels)v=sb::get(in,2);packed.resize(5*stride);mod=31;
  }else if(magic=="R150SJ61"){
   for(int v:{31,MOD,6188})if(sb::get(in,4)!=uint64_t(v))throw std::runtime_error("integer Taylor source family dimensions");
   n=sb::get(in,4);l=sb::get(in,4);int ring=sb::get(in,4);
   if(n<1||n>256||l<jt::L||l>20||ring!=2)throw std::runtime_error("integer Taylor source family precision");
   std::string b(64,' ');in.read(b.data(),64);labels.resize(n);exponents.resize(n);for(int&v:labels)v=sb::get(in,2);for(int&v:exponents){v=sb::get(in,1);if(v<1||v>5)throw std::runtime_error("integer Taylor source divisor");}mod=MOD;
  }else throw std::runtime_error("unsupported exact source family magic");
  if(labels!=expected)throw std::runtime_error("exact whole source family label dictionary");
  row.resize(jt::L*n);
 }
 void next(int r,const sb::Model&m,const std::vector<jt::Co>&powers,bool use){
  std::fill(row.begin(),row.end(),0);
  if(magic=="R150SP31"){
   if(sb::get(in,4)!=uint64_t(r)||sb::get(in,4)!=uint64_t(r)||sb::get(in,2)!=uint64_t(m.delta(r)))throw std::runtime_error("packed original row dictionary");
   in.read(reinterpret_cast<char*>(packed.data()),packed.size()*4);if(!in)throw std::runtime_error("complete packed original source row");
   if(n%32)for(int k=0;k<l;k++){uint32_t nz=0;for(int b=0;b<5;b++)nz|=packed[b*stride+k*words+words-1];if(nz>>(n%32))throw std::runtime_error("packed source padding");}
   if(use)for(int k=0;k<jt::L;k++)for(int j=0;j<n;j++)row[k*n+j]=BitOps::get(packed,stride,k*words*32+j);
  }else if(magic=="R150SJ61"){
   m.rowHeader(in,r);
   for(int k=0;k<l;k++)for(int j=0;j<n;j++){int a=sb::get(in,4);if(a<0||a>=MOD)throw std::runtime_error("canonical integer Taylor source coefficient");if(use&&k<jt::L)row[k*n+j]=a;}
  }else{
   m.rowHeader(in,r);
   for(int j=0;j<n;j++){
    int size=sb::get(in,2),last=0,cap=(magic=="R150KK31"?costs[j]:bound)-m.delta(r)+1;
    if(size>std::max(0,cap)||size>int(powers.size()))throw std::runtime_error("actual global source degree bound");
    for(int d=0;d<size;d++){last=sb::get(in,width);if(last<0||last>=mod)throw std::runtime_error("canonical primitive source coefficient");
     if(use&&last)for(int k=0;k<jt::L;k++)row[k*n+j]=(row[k*n+j]+int64_t(last)*powers[d][k])%MOD;}
    if(size&&!last)throw std::runtime_error("primitive source trailing zero");
   }
  }
 }
};
struct Term{uint64_t monomial=0;jt::Co coefficient{};};
static void header(std::ostream&out,const char*magic,int rows,const jt::Spec&spec,const std::vector<int>&exponents,const std::string&binding){
 out.write(magic,8);for(int v:{31,MOD,rows,jt::NT,jt::L,2})u32(out,v);out.write(binding.data(),64);
 for(int x:spec.target)u16(out,x);for(int x:exponents)out.put(char(x));
}
int main(int argc,char**argv){try{
 if(argc!=10)return 2;
 std::signal(SIGTERM,jt::signal);std::signal(SIGINT,jt::signal);
 auto began=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-began).count();};
 sb::Model model(argv[1]);model.higher(argv[2]);auto spec=jt::labels(argv[3]);
 if(jt::RING!=2)throw std::runtime_error("integer source operations require the same root2 Taylor lift");
 std::string prefix=argv[5],binding=argv[6],oldcheck=argv[7];int retained=std::stoi(argv[8]);double seconds=std::stod(argv[9]);
 if(binding.size()!=64||retained<5||retained>jt::L||!std::isfinite(seconds)||seconds<=0)throw std::runtime_error("exact integer stage contract");
 const double reserve=std::min(20.0,seconds/4),soft=seconds-reserve;auto due=[&](){return jt::stopped||elapsed()>=soft;};
 std::ifstream mix(argv[4]);std::string magic,extra;int n,l,nf;mix>>magic>>n>>l>>nf;
 if(magic!="R150_S2_INTEGER_JET_MIX_V1"||n!=jt::NT||l!=jt::L||nf<1||nf>12)throw std::runtime_error("integer source mixture dimensions");
 std::vector<int>exponents(n),divisors(n);for(int j=0;j<n;j++){mix>>exponents[j];if(exponents[j]<1||exponents[j]>5)throw std::runtime_error("actual p division exponent");divisors[j]=power31(exponents[j]);}
 auto powers=jt::powers(MOD,800);std::vector<std::unique_ptr<Family>>families;
 uint64_t edges=0;
 for(int f=0;f<nf;f++){
  auto v=std::make_unique<Family>();std::string path;int count,ne;mix>>path>>count>>ne;if(count<1||count>256||ne<0||ne>100000)throw std::runtime_error("source mixture family size");
  std::vector<int>expected(count);for(int&x:expected)mix>>x;v->open(path,expected,model);v->edges.resize(count);
  for(int i=0;i<ne;i++){int in,target,len;mix>>in>>target>>len;if(in<0||in>=count||target<0||target>=n||len<1||len>jt::L)throw std::runtime_error("source mixture sparse edge");
   Edge e;e.out=target;e.c.resize(len);for(int&a:e.c){int64_t x;mix>>x;a=sb::mod(x,MOD);}if(!e.c.back())throw std::runtime_error("source multiplier trailing zero");
   v->edges[in].push_back(std::move(e));edges++;}
  families.push_back(std::move(v));
 }
 if(!mix||mix>>extra)throw std::runtime_error("complete source combination recipe");
 std::array<std::vector<Term>,17>terms;
 auto eval=[&](const auto&p){jt::Co a{};for(int d=0;d<int(p.size());d++)if(p[d])for(int k=0;k<jt::L;k++)a[k]=(a[k]+int64_t(p[d])*powers[d][k])%MOD;return a;};
 for(int e=0;e<17;e++){
  if(e<11){
   for(int z=0;z<66;z++)if(model.Qh[e][z]){auto[x,y]=model.quadratic[z];jt::Co a{};a[0]=model.Qh[e][z];terms[e].push_back({model.var[x]+model.var[y],a});}
   for(int v=0;v<11;v++){auto a=eval(model.Lh[e][v]);if(std::any_of(a.begin(),a.begin()+jt::L,[](int x){return x!=0;}))terms[e].push_back({model.var[v],a});}
  }else for(int z=0;z<66;z++){auto a=eval(model.Gh[e-11][z]);if(std::any_of(a.begin(),a.begin()+jt::L,[](int x){return x!=0;})){auto[x,y]=model.quadratic[z];terms[e].push_back({model.var[x]+model.var[y],a});}}
 }
 const size_t cells=size_t(4367)*jt::L*n;std::vector<uint64_t>product(cells);int completed=0;
 const std::string checkpoint=prefix+"-integer-product-checkpoint.bin",sourcefile=prefix+"-original6188-integer-jets.bin";
 {std::ifstream in(checkpoint,std::ios::binary);if(in){
  if(sb::tag(in)!="R150SX61")throw std::runtime_error("integer product checkpoint magic");
  for(int v:{31,MOD,6188,4367,n,jt::L})if(sb::get(in,4)!=uint64_t(v))throw std::runtime_error("integer product checkpoint dimensions");
  completed=sb::get(in,4);if(completed<0||completed>6188)throw std::runtime_error("integer product checkpoint cursor");
  std::string b(64,' ');in.read(b.data(),64);if(b!=binding)throw std::runtime_error("integer product checkpoint exact input binding");
  for(int x:spec.target)if(sb::get(in,2)!=uint64_t(x))throw std::runtime_error("integer checkpoint target labels");
  for(int x:exponents)if(sb::get(in,1)!=uint64_t(x))throw std::runtime_error("integer checkpoint divisors");
  in.read(reinterpret_cast<char*>(product.data()),product.size()*8);if(!in)throw std::runtime_error("complete actual partial original product");sb::tail(in);
  for(auto x:product)if(x>=uint64_t(MOD))throw std::runtime_error("canonical checkpoint accumulator");
 }}
 const size_t sourceHeader=8+24+64+3*n,rowBytes=15+size_t(jt::L)*n*4;
 std::ofstream source;
 if(completed){
  if(!std::filesystem::exists(sourcefile)||std::filesystem::file_size(sourcefile)<sourceHeader+size_t(completed)*rowBytes)throw std::runtime_error("actual source prefix missing at checkpoint");
  std::ifstream check(sourcefile,std::ios::binary);if(sb::tag(check)!="R150SJ61")throw std::runtime_error("checkpoint source magic");
  for(int v:{31,MOD,6188,n,jt::L,2})if(sb::get(check,4)!=uint64_t(v))throw std::runtime_error("checkpoint source shape");std::string b(64,' ');check.read(b.data(),64);if(b!=binding)throw std::runtime_error("checkpoint source binding");
  for(int v:spec.target)if(sb::get(check,2)!=uint64_t(v))throw std::runtime_error("checkpoint source label");for(int v:exponents)if(sb::get(check,1)!=uint64_t(v))throw std::runtime_error("checkpoint source divisor");
  check.close();std::filesystem::resize_file(sourcefile,sourceHeader+size_t(completed)*rowBytes);source.open(sourcefile,std::ios::binary|std::ios::app);
 }else{source.open(sourcefile,std::ios::binary);header(source,"R150SJ61",6188,spec,exponents,binding);}
 if(!source)throw std::runtime_error("original integer source output");
 auto save=[&](int done){
  source.flush();if(!source)throw std::runtime_error("flush actual original source prefix");
  std::ofstream out(checkpoint+".tmp",std::ios::binary);out.write("R150SX61",8);for(int v:{31,MOD,6188,4367,n,jt::L,done})u32(out,v);out.write(binding.data(),64);
  for(int v:spec.target)u16(out,v);for(int v:exponents)out.put(char(v));out.write(reinterpret_cast<const char*>(product.data()),product.size()*8);out.close();
  if(!out||std::rename((checkpoint+".tmp").c_str(),checkpoint.c_str()))throw std::runtime_error("atomic complete original product checkpoint");
  std::ofstream meta(prefix+"-integer-checkpoint.json");meta<<"{\"status\":\"checkpointed\",\"completedOriginalRows\":"<<done<<",\"actualFullPartialProductSaved\":true,\"actualOriginalSourcePrefixSaved\":true,\"sourcePrefixBytes\":"<<sourceHeader+size_t(done)*rowBytes<<",\"bindingSHA256\":\""<<binding<<"\",\"elapsedSeconds\":"<<elapsed()<<"}\n";
  if(!meta)throw std::runtime_error("integer checkpoint receipt");
 };
 std::vector<uint32_t>row(size_t(jt::L)*n);uint64_t nonzeroSource=0,scalarProducts=0;int resumed=completed;
 for(int r=1;r<=6188;r++){
  bool use=r>completed;std::fill(row.begin(),row.end(),0);
  for(auto&v:families){v->next(r,model,powers,use);if(!use)continue;
   for(int input=0;input<v->n;input++)for(const auto&e:v->edges[input])for(int k=0;k<int(e.c.size());k++)if(int a=e.c[k])
    for(int z=0;z+k<jt::L;z++)if(uint32_t x=v->row[z*v->n+input])row[(z+k)*n+e.out]=(row[(z+k)*n+e.out]+uint64_t(a)*x)%MOD;
  }
  if(!use)continue;model.rowHeader(source,r);source.write(reinterpret_cast<const char*>(row.data()),row.size()*4);if(!source)throw std::runtime_error("actual integer source row write");
  for(auto x:row)nonzeroSource+=x!=0;
  int equation=(r-1)%17;uint64_t monomial=model.multipliers[(r-1)/17];
  for(const auto&t:terms[equation]){
   int c=model.component.at(monomial+t.monomial);uint64_t*dest=product.data()+size_t(c)*jt::L*n;
   // At most20 products below MOD^2 plus a reduced accumulator: <2^64.
   for(int k=0;k<jt::L;k++)if(int a=t.coefficient[k])for(int z=0;z+k<jt::L;z++){
    const uint32_t*src=row.data()+z*n;uint64_t*out=dest+(z+k)*n;for(int j=0;j<n;j++)out[j]+=uint64_t(a)*src[j];scalarProducts+=n;}
   for(int k=0;k<jt::L*n;k++)dest[k]%=MOD;
  }
  if(r%250==0||r==6188||due())std::cout<<"{\"phase\":\"saturated-original17-integer-jets\",\"completedOriginalRows\":"<<r<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
  if(due()){save(r);std::cout<<"{\"status\":\"checkpointed-deadline\",\"completedOriginalRows\":"<<r<<",\"elapsedSeconds\":"<<elapsed()<<"}\n";return 75;}
 }
 for(auto&v:families)sb::tail(v->in);save(6188);source.close();if(!source)throw std::runtime_error("full original source close");
 // Source scaling by each actual primitive-row unit is invertible modulo p6.
 auto inv=[](int a){int64_t r0=MOD,r1=a,s0=0,s1=1;while(r1){int64_t q=r0/r1,x=r0-q*r1;r0=r1;r1=x;x=s0-q*s1;s0=s1;s1=x;}if(r0!=1)throw std::runtime_error("original row scale not a unit");return sb::mod(s0,MOD);};
 for(int e=0;e<17;e++){int u=int64_t(model.denominator)*inv(model.contents[e])%MOD,v=int64_t(model.contents[e])*inv(model.denominator)%MOD;if(int64_t(u)*v%MOD!=1)throw std::runtime_error("primitive/original row scale transport");}
 std::ofstream out(prefix+"-divided-original-jets.bin",std::ios::binary);header(out,"R150SR61",4367,spec,exponents,binding);
 std::ofstream field(prefix+"-field-root2-jets.bin",std::ios::binary),project(prefix+"-field-projected-crt8-jets.bin",std::ios::binary);
 for(auto*p:{&field,&project}){p->write("R150SD31",8);for(int v:{31,n,4367,p==&field?jt::L:8})u32(*p,v);for(int v:spec.target)u16(*p,v);}
 std::ifstream old;int oldKind=0,oldN=0,oldL=0;std::vector<int>oldLabels;
 if(oldcheck!="-"){
  old.open(oldcheck,std::ios::binary);auto tag=sb::tag(old);
  if(tag=="R1503R31"){oldKind=1;for(int v:{31,961,4367,197,10})if(sb::get(old,4)!=uint64_t(v))throw std::runtime_error("old integerT prefix dimensions");std::string b(64,' ');old.read(b.data(),64);oldN=197;oldL=10;}
  else if(tag=="R150DJ31"){oldKind=2;for(int v:{31,197,4367,8})if(sb::get(old,4)!=uint64_t(v))throw std::runtime_error("old197 third prefix dimensions");oldN=197;oldL=8;}
  else throw std::runtime_error("old original-jet comparison magic");
  oldLabels.resize(oldN);for(int&x:oldLabels)x=sb::get(old,2);if(oldLabels!=spec.target)throw std::runtime_error("same old original-jet comparison labels");
 }
 uint64_t verified=0,nonzero=0,compared=0;std::vector<int>oldrow(oldN*oldL);
 for(int c=0;c<4367;c++){
  uint64_t key=model.keys[c];sb::put(out,key,8);sb::put(field,key,8);sb::put(project,key,8);
  for(int z=0;z<3*n;z++)project.put(0);
  if(oldKind){if(sb::get(old,8)!=key)throw std::runtime_error("old original output dictionary");for(int&a:oldrow){a=sb::get(old,oldKind==1?2:1);if(a>(oldKind==1?960:30))throw std::runtime_error("old canonical divided jet");}}
  for(int k=0;k<jt::L;k++)for(int j=0;j<n;j++){
   int a=product[(size_t(c)*jt::L+k)*n+j];if(a%divisors[j])throw std::runtime_error("original17 Taylor coefficient not divisible by required p power");
   int v=a/divisors[j];u32(out,v);field.put(char(v%31));if(k<5)project.put(char(v%31));verified++;nonzero+=v!=0;
   if(oldKind==1&&k<10){if(v%961!=oldrow[k*n+j])throw std::runtime_error("new precision changed actual old integerT carry");compared++;}
   if(oldKind==2&&k<5){if(v%31!=oldrow[(k+3)*n+j])throw std::runtime_error("new prefix changed paid actual197 D3");compared++;}
  }
 }
 if(oldKind)sb::tail(old);out.close();field.close();project.close();if(!out||!field||!project)throw std::runtime_error("all original divided jets write");
 std::ofstream meta(prefix+"-integer-product.json");
 meta<<"{\"status\":\"completed\",\"format\":\"r150-saturated-original-integer-jets-v1\",\"prime\":31,\"integerModulus\":"<<MOD<<",\"targetCount\":"<<n<<",\"targetLabels\":";sb::array(meta,spec.target);
 meta<<",\"divisorExponents\":";sb::array(meta,exponents);
 meta<<",\"TaylorCenter\":2,\"computedTaylorPrecision\":"<<jt::L<<",\"retainedFormalPrecision\":"<<retained<<",\"allOriginalSourceRows\":6188,\"allOriginalOutputRows\":4367,\"allOriginal17CoefficientsDivisible\":true,\"originalRowScaleTransportVerified\":true,\"allOriginalIntegerSourceJetsSaved\":true,\"allDividedIntegerJetsSaved\":true,\"root1ProjectionSlotsExplicitlyZero\":true,\"oldPrefixComparisons\":"<<compared<<",\"verifiedOriginalJetCoordinates\":"<<verified<<",\"nonzeroDividedJetCoefficients\":"<<nonzero<<",\"nonzeroOriginalSourceJetCoefficientsProcessed\":"<<nonzeroSource<<",\"sourceMixtureEdges\":"<<edges<<",\"processedIntegerScalarProducts\":"<<scalarProducts<<",\"resumedOriginalRows\":"<<resumed<<",\"globalPolynomialIdentityClaimed\":false,\"bindingSHA256\":\""<<binding<<"\",\"elapsedSeconds\":"<<elapsed()<<"}\n";
 meta.close();if(!meta)throw std::runtime_error("integer original product receipt");
 std::cout<<"{\"status\":\"saturated-original-integer-jets-complete\",\"allOriginal17CoefficientsDivisible\":true,\"targetCount\":"<<n<<",\"computedTaylorPrecision\":"<<jt::L<<",\"retainedFormalPrecision\":"<<retained<<",\"elapsedSeconds\":"<<elapsed()<<"}\n";return 0;
}catch(const std::exception&e){std::cerr<<"R150_SATURATED_INTEGER_JETS_FAILED "<<e.what()<<"\n";return 1;}}
