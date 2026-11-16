// Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.
// Original joint-M raw-target combinations minus the original 17-equation sources modulo31^12.
// All 6188/4367 rows remain. Empty source mixtures encode the actual zero source.
// Independent format: uint64 coefficients and __uint128_t products; no p6 padding.
#include "2026-11-16-r150-joint-m-local-common50-789f.hpp"
#include <cmath>
#include <limits>
using U64=uint64_t;
using U128=__uint128_t;
using I128=__int128_t;
constexpr U64 MOD=787662783788549761ULL;
using Co12=std::array<U64,50>;
static U64 pow31(int n){U64 z=1;while(n--)z*=31;return z;}
static U64 norm(I128 x){x%=I128(MOD);if(x<0)x+=MOD;return U64(x);}
static U64 mul(U64 a,U64 b){return U64(U128(a)*b%MOD);}
static U64 inverse(U64 a){
 I128 r0=MOD,r1=a,s0=0,s1=1;
 while(r1){I128 q=r0/r1,x=r0-q*r1;r0=r1;r1=x;x=s0-q*s1;s0=s1;s1=x;}
 if(r0!=1)throw std::runtime_error("primitive row scale is not a31-unit");
 return norm(s0);
}
struct IntegerModel{
 std::array<std::array<U64,66>,11>Q{};
 std::array<std::array<std::array<U64,11>,11>,11>L{};
 std::array<std::array<std::array<U64,6>,66>,6>G{};
 std::array<U64,17>contents{};U64 denominator=0;
 IntegerModel(const std::string&file,const sb::Model&m){
  std::ifstream in(file);std::string magic,extra;U64 prime,mod;int equations,count;
  in>>magic>>prime>>mod>>equations>>count;
  if(magic!="R150_ORIGINAL_EQUATIONS_P12_V1"||prime!=31||mod!=MOD||equations!=17||count!=4433)throw std::runtime_error("exact p12 equation model header");
  auto unit=[&](U64&a){in>>a;if(!in||a>=MOD||a%31==0)throw std::runtime_error("original p12 row units");};
  unit(denominator);for(auto&a:contents)unit(a);
  uint64_t checked=0;
  auto read=[&](U64&a,int residue){in>>a;if(!in||a>=MOD||a%31!=U64(residue))throw std::runtime_error("all original4433 p12/field coefficients");checked++;};
  for(int e=0;e<11;e++){for(int j=0;j<66;j++)read(Q[e][j],m.Q[e][j]);for(int j=0;j<11;j++)for(int d=0;d<11;d++)read(L[e][j][d],m.L[e][j][d]);}
  for(int e=0;e<6;e++)for(int j=0;j<66;j++)for(int d=0;d<6;d++)read(G[e][j][d],m.G[e][j][d]);
  if(checked!=4433||!in||in>>extra)throw std::runtime_error("complete p12 original equation EOF");
  for(auto c:contents)if(mul(mul(denominator,inverse(c)),mul(c,inverse(denominator)))!=1)throw std::runtime_error("original/primitive two-way unit transport");
 }
};
static std::vector<Co12> powers(int maximum){
 std::vector<Co12>p(maximum+1);Co12 bin{};bin[0]=1;U64 two=1,half=(MOD+1)/2;
 for(int d=0;d<=maximum;d++){
  if(d){for(int k=49;k>=1;k--)bin[k]=(bin[k]+bin[k-1])%MOD;two=mul(two,2);}
  U64 v=two;for(int k=0;k<jt::L;k++){p[d][k]=k<=d?mul(bin[k],v):0;v=mul(v,half);}
 }return p;
}
struct Edge{int out=0;std::vector<U64>c;};
struct Family{
 std::string file,magic;int n=0,l=0,width=0,bound=0,stride=0,words=0,kind=0,done=0;
 U64 modulus=0;std::vector<int>labels,exponents,costs;
 std::vector<std::vector<Edge>>edges;std::ifstream in;std::vector<U64>row;Row packed;
 void open(const std::string&path,const std::vector<int>&expected,const sb::Model&m,const std::string&binding){
  file=path;in.open(path,std::ios::binary);if(!in)throw std::runtime_error("source family unavailable");magic=sb::tag(in);
  if(magic=="R150KK31"){
   for(int v:{31,6188,200,85})if(sb::get(in,4)!=U64(v))throw std::runtime_error("original K200 family dimensions");
   n=200;modulus=31;width=1;costs.resize(n);labels.resize(n);
   for(int j=0;j<n;j++){
    (void)sb::get(in,4);labels[j]=sb::get(in,2);costs[j]=sb::get(in,2);int source=sb::get(in,4),raw=sb::get(in,4);
    if(source<1||source>2195||raw<1||raw>6188||costs[j]!=(j<160?80:j<198?81:85))throw std::runtime_error("complete K200 source map");
   }
  }else if(magic=="R150PS31"||magic=="R150P431"||magic=="R150P531"||magic=="R150P631"){
   if(sb::get(in,4)!=31)throw std::runtime_error("primitive family prime");modulus=sb::get(in,4);
   if(modulus!=31&&modulus!=961&&modulus!=29791&&modulus!=923521&&modulus!=28629151&&modulus!=887503681)throw std::runtime_error("paid canonical primitive family modulus");
   if(sb::get(in,4)!=6188)throw std::runtime_error("all6188 original family rows");n=sb::get(in,4);bound=sb::get(in,4);
   if(n<1||n>256||bound<1||bound>796)throw std::runtime_error("primitive family size or actual cost");
   width=magic=="R150PS31"?2:4;labels.resize(n);for(int&x:labels)x=sb::get(in,2);
  }else if(magic=="R150SP31"){
   if(sb::get(in,4)!=31||sb::get(in,4)!=6188)throw std::runtime_error("complete packed original source frame");
   n=sb::get(in,4);l=sb::get(in,4);stride=sb::get(in,4);kind=sb::get(in,4);done=sb::get(in,4);bound=sb::get(in,4);words=(n+31)/32;
   if(n<1||n>256||l<jt::L||l>50||stride!=words*l||kind!=2||done!=6188)throw std::runtime_error("completed actual packed source precision");
   std::string b(64,' ');in.read(b.data(),64);if(b!=binding)throw std::runtime_error("same packed source pipeline binding");
   labels.resize(n);for(int&x:labels)x=sb::get(in,2);packed.resize(5*stride);modulus=31;
  }else if(magic=="R150SJ12"){
   if(sb::get(in,4)!=31||sb::get(in,8)!=MOD||sb::get(in,4)!=6188)throw std::runtime_error("actual p12 integer source frame");
   n=sb::get(in,4);l=sb::get(in,4);int ring=sb::get(in,4);
   if(n<1||n>256||l<jt::L||l>50||ring!=2)throw std::runtime_error("actual p12 integer source precision");
   std::string b(64,' ');in.read(b.data(),64);if(b!=binding)throw std::runtime_error("same integer source pipeline binding");
   labels.resize(n);exponents.resize(n);for(int&x:labels)x=sb::get(in,2);
   for(int&x:exponents){x=sb::get(in,1);if(x<1||x>11)throw std::runtime_error("p12 source divisor metadata");}modulus=MOD;
  }else throw std::runtime_error("unsupported true source family format");
  if(labels!=expected)throw std::runtime_error("complete original family label dictionary");
  if(std::set<int>(labels.begin(),labels.end()).size()!=labels.size())throw std::runtime_error("duplicate original family labels");
  row.resize(size_t(jt::L)*n);
 }
 void next(int r,const sb::Model&m,const std::vector<Co12>&pw,bool use){
  std::fill(row.begin(),row.end(),0);
  if(magic=="R150SP31"){
   if(sb::get(in,4)!=U64(r)||sb::get(in,4)!=U64(r)||sb::get(in,2)!=U64(m.delta(r)))throw std::runtime_error("packed full original row dictionary");
   in.read(reinterpret_cast<char*>(packed.data()),packed.size()*4);if(!in)throw std::runtime_error("complete packed source row");
   if(n%32)for(int k=0;k<l;k++){uint32_t nz=0;for(int b=0;b<5;b++)nz|=packed[b*stride+k*words+words-1];if(nz>>(n%32))throw std::runtime_error("source packed padding");}
   if(use)for(int k=0;k<jt::L;k++)for(int j=0;j<n;j++)row[k*n+j]=BitOps::get(packed,stride,k*words*32+j);
  }else if(magic=="R150SJ12"){
   m.rowHeader(in,r);
   for(int k=0;k<l;k++)for(int j=0;j<n;j++){U64 a=sb::get(in,8);if(a>=MOD)throw std::runtime_error("canonical p12 source coefficient");if(use&&k<jt::L)row[k*n+j]=a;}
  }else{
   m.rowHeader(in,r);
   for(int j=0;j<n;j++){
    int size=sb::get(in,2),cap=(magic=="R150KK31"?costs[j]:bound)-m.delta(r)+1;U64 last=0;
    if(size>std::max(0,cap)||size>int(pw.size()))throw std::runtime_error("actual global source degree bound");
    for(int d=0;d<size;d++){
     last=sb::get(in,width);if(last>=modulus)throw std::runtime_error("canonical paid integer source coefficient");
     if(use&&last)for(int k=0;k<jt::L;k++)row[k*n+j]=(row[k*n+j]+mul(last,pw[d][k]))%MOD;
    }
    if(size&&!last)throw std::runtime_error("primitive source trailing zero");
   }
  }
 }
};
struct Term{U64 monomial=0;Co12 coefficient{};};

struct OriginalTargets{
 std::vector<U64> polynomial;
 std::vector<int> labels;
 struct TargetEdge{int input=0,output=0;std::vector<U64> coefficient;};
 std::vector<TargetEdge> edges;
 explicit OriginalTargets(const std::string&file,const jt::Spec&spec){
  std::ifstream in(file);std::string magic,extra;U64 p,m;int degreeCount,seedCount,n,ne;
  in>>magic>>p>>m>>degreeCount>>seedCount>>n>>ne;
  if(magic!="R150_JOINT_M_ORIGINAL_NINE_TARGETS_P12_V1"||p!=31||m!=MOD||degreeCount!=1||seedCount!=9||n!=jt::NT||ne<0||ne>9*n)
   throw std::runtime_error("original joint-B target model dimensions");
  polynomial.resize(1);for(auto&a:polynomial){in>>a;if(!in||a>=MOD)throw std::runtime_error("canonical raw-square multiplier coefficient");}
  for(int j=2;j<=10;j++){int a;in>>a;if(!in||a!=j)throw std::runtime_error("all nine original square labels");}
  labels.resize(n);for(int&a:labels)in>>a;
  if(!in||labels!=spec.target)throw std::runtime_error("same actual target-combination labels");
  if(polynomial!=std::vector<U64>{1})throw std::runtime_error("the actual unmultiplied nine original squares are required");
  std::set<std::pair<int,int>>seen;
  for(int k=0;k<ne;k++){
   TargetEdge e;int size;in>>e.input>>e.output>>size;
   if(e.input<0||e.input>=9||e.output<0||e.output>=n||size<1||size>3||!seen.emplace(e.input,e.output).second)
    throw std::runtime_error("unique original target Taylor edge");
   e.coefficient.resize(size);
   for(auto&a:e.coefficient){int64_t v;in>>v;if(!in)throw std::runtime_error("target edge integer");a=norm(v);}
   if(!e.coefficient.back())throw std::runtime_error("target edge trailing zero");
   edges.push_back(std::move(e));
  }
  if(!in||in>>extra)throw std::runtime_error("original target model complete EOF");
 }
 std::vector<U64>jets(const sb::Model&m,const jt::Spec&spec,int targetPower,const std::vector<Co12>&pw)const{
  if(targetPower<0||targetPower>6||spec.target!=labels)throw std::runtime_error("declared scalar target power and labels");
  U64 choose[11][11]{};for(int n=0;n<=10;n++){choose[n][0]=choose[n][n]=1;for(int k=1;k<n;k++)choose[n][k]=choose[n-1][k-1]+choose[n-1][k];}
  std::vector<U64>seeds(size_t(4367)*jt::L*9),result(size_t(4367)*jt::L*jt::NT);
  for(int slot=0;slot<9;slot++){
   const int j=slot+2;
   for(int a=0;a<=j;a++)for(int b=a;b<=j;b++){
    int shift=2*j-a-b,c=m.component.at(m.var[a]+m.var[b]);
    U64 scalar=mul(pow31(targetPower),choose[j][a]*choose[j][b]*(a==b?1:2));
    if(shift%2)scalar=(MOD-scalar)%MOD;
    for(int d=0;d<int(polynomial.size());d++)if(polynomial[d])for(int k=0;k<jt::L;k++)
     seeds[(size_t(c)*jt::L+k)*9+slot]=(seeds[(size_t(c)*jt::L+k)*9+slot]+mul(mul(scalar,polynomial[d]),pw[d+shift][k]))%MOD;
   }
  }
  // Edge polynomials are in the actual Taylor parameter x=s-2, not in s.
  for(const auto&e:edges)for(int k=0;k<int(e.coefficient.size());k++)if(U64 a=e.coefficient[k])
   for(int c=0;c<4367;c++)for(int z=0;z+k<jt::L;z++)
    result[(size_t(c)*jt::L+z+k)*jt::NT+e.output]=(result[(size_t(c)*jt::L+z+k)*jt::NT+e.output]+mul(a,seeds[(size_t(c)*jt::L+z)*9+e.input]))%MOD;
  return result;
 }
};

static void header(std::ostream&out,const char*magic,int rows,const jt::Spec&spec,const std::vector<int>&exponents,const std::string&binding){
 out.write(magic,8);sb::put(out,31,4);sb::put(out,MOD,8);
 for(int v:{rows,jt::NT,jt::L,2})u32(out,v);out.write(binding.data(),64);
 for(int x:spec.target)u16(out,x);for(int x:exponents)out.put(char(x));
}
int main(int argc,char**argv){try{
 if(argc!=11){std::cerr<<"usage: PROGRAM fieldModel p12Model spec mix outPrefix binding retainedPrecision remainingSeconds targetModel targetPower\n";return 2;}
 std::signal(SIGTERM,jt::signal);std::signal(SIGINT,jt::signal);
 const auto began=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-began).count();};
 sb::Model model(argv[1]);IntegerModel integral(argv[2],model);auto spec=jt::labels(argv[3]);
 if(jt::RING!=2)throw std::runtime_error("integer carries use actual root2 Taylor parameter");
 std::string prefix=argv[5],binding=argv[6];int retained=std::stoi(argv[7]);double seconds=std::stod(argv[8]);
 if(binding.size()!=64||binding.find_first_not_of("0123456789abcdef")!=std::string::npos||retained<5||retained>jt::L||!std::isfinite(seconds)||seconds<=0)throw std::runtime_error("p12 exact stage contract");
 const double soft=seconds-std::min(20.0,seconds/4);auto due=[&](){return jt::stopped||elapsed()>=soft;};
 std::ifstream mix(argv[4]);std::string magic,extra;int n,l,nf;mix>>magic>>n>>l>>nf;
 if(magic!="R150_JOINT_M_INTEGER_MIX_P12_V1"||n!=jt::NT||l!=jt::L||nf<0||nf>16)throw std::runtime_error("p12 source mixture dimensions");
 std::vector<int>exponents(n);std::vector<U64>divisors(n);
 for(int j=0;j<n;j++){mix>>exponents[j];if(exponents[j]<1||exponents[j]>11)throw std::runtime_error("true p division exponent");divisors[j]=pow31(exponents[j]);}
 auto pw=powers(800);std::vector<std::unique_ptr<Family>>families;U64 edges=0;
 for(int f=0;f<nf;f++){
  auto v=std::make_unique<Family>();std::string path;int count,ne;mix>>path>>count>>ne;
  if(count<1||count>256||ne<0||ne>100000)throw std::runtime_error("p12 source family edge count");
  std::vector<int>expected(count);for(int&x:expected)mix>>x;v->open(path,expected,model,binding);v->edges.resize(count);
  for(int k=0;k<ne;k++){
   int input,target,len;mix>>input>>target>>len;
   if(input<0||input>=count||target<0||target>=n||len<1||len>jt::L)throw std::runtime_error("p12 source sparse edge");
   Edge e;e.out=target;e.c.resize(len);
   for(auto&a:e.c){int64_t x;mix>>x;if(!mix)throw std::runtime_error("signed edge coefficient");a=norm(x);}
   if(!e.c.back())throw std::runtime_error("p12 multiplier trailing zero");v->edges[input].push_back(std::move(e));edges++;
  }families.push_back(std::move(v));
 }
 if(!mix||mix>>extra)throw std::runtime_error("complete source combination recipe");
 std::array<std::vector<Term>,17>terms;
 auto eval=[&](const auto&p){Co12 a{};for(int d=0;d<int(p.size());d++)if(p[d])for(int k=0;k<jt::L;k++)a[k]=(a[k]+mul(p[d],pw[d][k]))%MOD;return a;};
 for(int e=0;e<17;e++){
  if(e<11){
   for(int z=0;z<66;z++)if(integral.Q[e][z]){auto[x,y]=model.quadratic[z];Co12 a{};a[0]=integral.Q[e][z];terms[e].push_back({model.var[x]+model.var[y],a});}
   for(int v=0;v<11;v++){auto a=eval(integral.L[e][v]);if(std::any_of(a.begin(),a.begin()+jt::L,[](U64 x){return x!=0;}))terms[e].push_back({model.var[v],a});}
  }else for(int z=0;z<66;z++){
   auto a=eval(integral.G[e-11][z]);if(std::any_of(a.begin(),a.begin()+jt::L,[](U64 x){return x!=0;})){auto[x,y]=model.quadratic[z];terms[e].push_back({model.var[x]+model.var[y],a});}
  }
 }
 OriginalTargets targetModel(argv[9],spec);int targetPower=std::stoi(argv[10]);
 const auto target=targetModel.jets(model,spec,targetPower,pw);
 const size_t cells=size_t(4367)*jt::L*n;std::vector<U128>product(cells);int completed=0;
 const std::string checkpoint=prefix+"-integer-product-checkpoint.bin",sourcefile=prefix+"-original6188-integer-jets.bin";
 {
  std::ifstream in(checkpoint,std::ios::binary);if(in){
   if(sb::tag(in)!="R150TX12"||sb::get(in,4)!=31||sb::get(in,8)!=MOD)throw std::runtime_error("p12 product checkpoint version");
   for(int v:{6188,4367,n,jt::L})if(sb::get(in,4)!=U64(v))throw std::runtime_error("p12 product checkpoint shape");
   completed=sb::get(in,4);if(completed<0||completed>6188)throw std::runtime_error("p12 product checkpoint cursor");
   std::string b(64,' ');in.read(b.data(),64);if(b!=binding)throw std::runtime_error("p12 checkpoint exact input binding");
   for(int x:spec.target)if(sb::get(in,2)!=U64(x))throw std::runtime_error("checkpoint target labels");
   for(int x:exponents)if(sb::get(in,1)!=U64(x))throw std::runtime_error("checkpoint p divisors");
   for(auto&x:product){U64 a=sb::get(in,8);if(a>=MOD)throw std::runtime_error("canonical checkpoint accumulator");x=a;}sb::tail(in);
  }
 }
 const size_t sourceHeader=8+28+64+3*n,rowBytes=15+size_t(jt::L)*n*8;
 std::ofstream source;
 if(completed){
  if(!std::filesystem::exists(sourcefile)||std::filesystem::file_size(sourcefile)<sourceHeader+size_t(completed)*rowBytes)throw std::runtime_error("actual source prefix missing at checkpoint");
  std::ifstream check(sourcefile,std::ios::binary);
  if(sb::tag(check)!="R150SJ12"||sb::get(check,4)!=31||sb::get(check,8)!=MOD)throw std::runtime_error("checkpoint source version");
  for(int v:{6188,n,jt::L,2})if(sb::get(check,4)!=U64(v))throw std::runtime_error("checkpoint source shape");
  std::string b(64,' ');check.read(b.data(),64);if(b!=binding)throw std::runtime_error("checkpoint source binding");
  for(int x:spec.target)if(sb::get(check,2)!=U64(x))throw std::runtime_error("checkpoint source labels");
  for(int x:exponents)if(sb::get(check,1)!=U64(x))throw std::runtime_error("checkpoint source divisor");
  check.close();std::filesystem::resize_file(sourcefile,sourceHeader+size_t(completed)*rowBytes);source.open(sourcefile,std::ios::binary|std::ios::app);
 }else{source.open(sourcefile,std::ios::binary);header(source,"R150SJ12",6188,spec,exponents,binding);}
 if(!source)throw std::runtime_error("p12 source output unavailable");
 auto save=[&](int done){
  source.flush();if(!source)throw std::runtime_error("flush actual p12 source prefix");
  std::ofstream out(checkpoint+".tmp",std::ios::binary);out.write("R150TX12",8);sb::put(out,31,4);sb::put(out,MOD,8);
  for(int v:{6188,4367,n,jt::L,done})u32(out,v);out.write(binding.data(),64);
  for(int x:spec.target)u16(out,x);for(int x:exponents)out.put(char(x));
  for(auto x:product){if(x>=MOD)throw std::runtime_error("checkpoint product must be reduced");sb::put(out,U64(x),8);}
  out.close();if(!out||std::rename((checkpoint+".tmp").c_str(),checkpoint.c_str()))throw std::runtime_error("atomic original p12 product checkpoint");
  std::ofstream meta(prefix+"-integer-checkpoint.json");
  meta<<"{\"status\":\"checkpointed\",\"completedOriginalRows\":"<<done<<",\"actualFullPartialProductSaved\":true,\"actualOriginalSourcePrefixSaved\":true,\"sourcePrefixBytes\":"<<sourceHeader+size_t(done)*rowBytes<<",\"bindingSHA256\":\""<<binding<<"\",\"elapsedSeconds\":"<<elapsed()<<"}\n";
  if(!meta)throw std::runtime_error("p12 checkpoint receipt");
 };
 std::vector<U64>row(size_t(jt::L)*n);U64 nonzeroSource=0,scalarProducts=0;int resumed=completed;
 for(int r=1;r<=6188;r++){
  bool use=r>completed;std::fill(row.begin(),row.end(),0);
  for(auto&v:families){
   v->next(r,model,pw,use);if(!use)continue;
   for(int input=0;input<v->n;input++)for(const auto&e:v->edges[input])for(int k=0;k<int(e.c.size());k++)if(U64 a=e.c[k])
    for(int z=0;z+k<jt::L;z++)if(U64 x=v->row[z*v->n+input])row[(z+k)*n+e.out]=(row[(z+k)*n+e.out]+mul(a,x))%MOD;
  }
  if(!use)continue;model.rowHeader(source,r);for(U64 x:row)sb::put(source,x,8);if(!source)throw std::runtime_error("actual p12 source row write");
  for(U64 x:row)nonzeroSource+=x!=0;
  int equation=(r-1)%17;U64 monomial=model.multipliers[(r-1)/17];
  for(const auto&t:terms[equation]){
   int c=model.component.at(monomial+t.monomial);U128*dest=product.data()+size_t(c)*jt::L*n;
   // At most50 products <31^24 each, plus one reduced accumulator; safely <2^125.
   // Reduction occurs after every original equation term, never after all6188 sources.
   for(int k=0;k<jt::L;k++)if(U64 a=t.coefficient[k])for(int z=0;z+k<jt::L;z++){
    const U64*src=row.data()+z*n;U128*out=dest+(z+k)*n;
    for(int j=0;j<n;j++)out[j]+=U128(a)*src[j];scalarProducts+=n;
   }
   for(int k=0;k<jt::L*n;k++)dest[k]%=MOD;
  }
  if(r%250==0||r==6188||due())std::cout<<"{\"phase\":\"joint-m-original17-p12-jets\",\"completedOriginalRows\":"<<r<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
  if(due()){save(r);std::cout<<"{\"status\":\"checkpointed-deadline\",\"completedOriginalRows\":"<<r<<",\"elapsedSeconds\":"<<elapsed()<<"}\n";return 75;}
 }
 for(auto&v:families)sb::tail(v->in);save(6188);source.close();if(!source)throw std::runtime_error("complete p12 source close");
 std::ofstream divided(prefix+"-divided-original-jets.bin",std::ios::binary);header(divided,"R150TR12",4367,spec,exponents,binding);
 std::ofstream field(prefix+"-field-root2-jets.bin",std::ios::binary),project(prefix+"-field-projected-crt8-jets.bin",std::ios::binary);
 for(auto*p:{&field,&project}){p->write("R150SD31",8);for(int v:{31,n,4367,p==&field?jt::L:8})u32(*p,v);for(int x:spec.target)u16(*p,x);}
 U64 verified=0,nonzero=0;
 for(int c=0;c<4367;c++){
  U64 key=model.keys[c];sb::put(divided,key,8);sb::put(field,key,8);sb::put(project,key,8);
  for(int z=0;z<3*n;z++)project.put(0);
  for(int k=0;k<jt::L;k++)for(int j=0;j<n;j++){
   U64 a=(target[(size_t(c)*jt::L+k)*n+j]+MOD-U64(product[(size_t(c)*jt::L+k)*n+j]))%MOD;
   if(a%divisors[j])throw std::runtime_error("original p12 Taylor coefficient not divisible by required p power");
   U64 v=a/divisors[j];sb::put(divided,v,8);field.put(char(v%31));if(k<5)project.put(char(v%31));verified++;nonzero+=v!=0;
  }
 }
 divided.close();field.close();project.close();if(!divided||!field||!project)throw std::runtime_error("complete original divided jet output");
 std::ofstream meta(prefix+"-integer-product.json");
 meta<<"{\"status\":\"completed\",\"format\":\"r150-joint-m-raw-target-integer-p12-jets-v1\",\"prime\":31,\"integerModulus\":"<<MOD<<",\"targetCount\":"<<n<<",\"targetLabels\":";sb::array(meta,spec.target);
 meta<<",\"targetScalarPower\":"<<targetPower<<",\"sameOriginalUnmultipliedNineSquaresVerified\":true,\"residualIsTargetMinusOriginalAProduct\":true,\"targetCombinationEdges\":"<<targetModel.edges.size();
 meta<<",\"divisorExponents\":";sb::array(meta,exponents);
 meta<<",\"TaylorCenter\":2,\"computedTaylorPrecision\":"<<jt::L<<",\"retainedFormalPrecision\":"<<retained<<",\"allOriginalSourceRows\":6188,\"allOriginalOutputRows\":4367,\"all4433OriginalFieldResiduesMatched\":true,\"allOriginal17CoefficientsDivisible\":true,\"originalRowScaleTransportVerified\":true,\"allOriginalIntegerSourceJetsSaved\":true,\"allDividedIntegerJetsSaved\":true,\"root1ProjectionSlotsExplicitlyZero\":true,\"verifiedOriginalJetCoordinates\":"<<verified<<",\"nonzeroDividedJetCoefficients\":"<<nonzero<<",\"nonzeroOriginalSourceJetCoefficientsProcessed\":"<<nonzeroSource<<",\"sourceMixtureEdges\":"<<edges<<",\"processedIntegerScalarProducts\":"<<scalarProducts<<",\"resumedOriginalRows\":"<<resumed<<",\"coefficientStorageBits\":64,\"productArithmeticBits\":128,\"globalPolynomialIdentityClaimed\":false,\"bindingSHA256\":\""<<binding<<"\",\"elapsedSeconds\":"<<elapsed()<<"}\n";
 meta.close();if(!meta)throw std::runtime_error("p12 original product receipt");
 std::cout<<"{\"status\":\"joint-m-raw-target-integer-p12-jets-complete\",\"allOriginal17CoefficientsDivisible\":true,\"targetCount\":"<<n<<",\"computedTaylorPrecision\":"<<jt::L<<",\"retainedFormalPrecision\":"<<retained<<",\"targetScalarPower\":"<<targetPower<<",\"sameOriginalUnmultipliedNineSquaresVerified\":true,\"residualIsTargetMinusOriginalAProduct\":true,\"elapsedSeconds\":"<<elapsed()<<"}\n";return 0;
}catch(const std::exception&e){std::cerr<<"R150_JOINT_M_TARGET_INTEGER_P12_FAILED "<<e.what()<<"\n";return 1;}}

