// Exact integer root2 ten-jets, canonical carries, all original17 equations.
// first: A(K-p*q1)/p^2 modp^2; bases: actual b1..b7 modp^2;
// subtract: T=R2-b*C; third: (T-A*q2)/p after truncating to five coefficients.
#include "2026-11-14-r150-197-third-local-common-789f.hpp"
struct Term{uint64_t monomial;jt::Co a;};
static int inverse(int a,int m){int64_t r0=m,r1=a,s0=0,s1=1;while(r1){int64_t q=r0/r1,t=r0-q*r1;r0=r1;r1=t;t=s0-q*s1;s0=s1;s1=t;}if(r0!=1)throw std::runtime_error("original fixed row unit");return sb::mod(s0,m);}
struct Family{std::string path;int count=0,mod=0,bound=0,width=0;std::vector<int>labels;std::vector<std::pair<int,int>>selected;std::unique_ptr<std::ifstream>in;};
int main(int argc,char**argv){try{
 if(argc!=9)return 2;std::signal(SIGTERM,jt::signal);std::signal(SIGINT,jt::signal);
 auto start=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 std::string mode=argv[1],prefix=argv[7],binding=argv[8];sb::Model model(argv[2]);model.higher(argv[3]);auto lab=jt::labels(argv[4]);
 if(binding.size()!=64)throw std::runtime_error("frozen local integer binding");
 if(mode=="subtract"){
  std::ifstream recipe(argv[6]);std::string rfile,cfile,extra;recipe>>rfile>>cfile;if(!recipe||recipe>>extra)throw std::runtime_error("actual subtract file contract");
  std::ifstream r(rfile,std::ios::binary),b(argv[5],std::ios::binary),co(cfile,std::ios::binary);
  if(sb::tag(r)!="R1503R31"||sb::tag(b)!="R1503B31"||sb::tag(co)!="R1503C31")throw std::runtime_error("actual complete integer R2/b/C inputs");
  for(int v:{31,961,4367,197,10})if(sb::get(r,4)!=uint64_t(v))throw std::runtime_error("actual R2 ten-jet dimensions");
  for(int v:{31,961,4367,7,10})if(sb::get(b,4)!=uint64_t(v))throw std::runtime_error("actual seven b ten-jet dimensions");
  for(int v:{31,7,197})if(sb::get(co,4)!=uint64_t(v))throw std::runtime_error("actual seven cancellation dimensions");
  for(auto*in:{&r,&b}){std::string old(64,' ');in->read(old.data(),64);if(old!=binding)throw std::runtime_error("same R2/b input binding");}
  for(int j=0;j<197;j++)if(sb::get(r,2)!=uint64_t(jt::label(lab,j))||sb::get(co,2)!=uint64_t(jt::label(lab,j)))throw std::runtime_error("same original K2..K198");
  std::array<std::array<int,197>,7>C{};for(auto&row:C)for(auto&a:row){a=sb::get(co,1);if(a>30)throw std::runtime_error("canonical C");}sb::tail(co);
  std::ofstream out(prefix+"-T-mod961-root2-ten.bin",std::ios::binary),field(prefix+"-T-field-root2-ten.bin",std::ios::binary);
  out.write("R1503R31",8);for(int v:{31,961,4367,197,10})u32(out,v);out.write(binding.data(),64);for(int j=0;j<197;j++)u16(out,jt::label(lab,j));
  field.write("R150DJ31",8);for(int v:{31,197,4367,10})u32(field,v);for(int j=0;j<197;j++)u16(field,jt::label(lab,j));
  uint64_t nz=0;for(int c=0;c<4367;c++){uint64_t key=model.keys[c];if(sb::get(r,8)!=key||sb::get(b,8)!=key)throw std::runtime_error("all original4367 R2/b monomials");sb::put(out,key,8);sb::put(field,key,8);
   std::array<std::array<int,7>,10>B{};for(int k=0;k<10;k++)for(int i=0;i<7;i++){B[k][i]=sb::get(b,2);if(B[k][i]>960)throw std::runtime_error("actual b mod961 coefficient");}
   for(int k=0;k<10;k++)for(int j=0;j<197;j++){int a=sb::get(r,2);if(a>960)throw std::runtime_error("actual R2 mod961 coefficient");for(int i=0;i<7;i++)a=sb::mod(a-B[k][i]*C[i][j],961);u16(out,a);field.put(char(a%31));nz+=a!=0;}
  }sb::tail(r);sb::tail(b);out.close();field.close();if(!out||!field)throw std::runtime_error("integer T ten-jet write");
  std::ofstream meta(prefix+"-subtraction.json");meta<<"{\"status\":\"completed\",\"targets\":197,\"TaylorPrecision\":10,\"actualIntegerTEqualsR2MinusTrueSevenB\":true,\"canonicalCancellationCoefficientsRetained\":true,\"nonzeroTJets\":"<<nz<<",\"elapsedSeconds\":"<<elapsed()<<"}\n";
  std::cout<<"{\"status\":\"197-integer-ten-jet-subtraction-complete\",\"elapsedSeconds\":"<<elapsed()<<"}\n";return 0;
 }
 bool first=mode=="first",bases=mode=="bases",third=mode=="third";if(!first&&!bases&&!third)throw std::runtime_error("integer local product mode");
 const int nt=bases?7:197,modulus=third?961:923521;auto pw=jt::powers(modulus,256);BitOps ops;
 jt::Packed q;if(!bases){q=jt::readPacked(argv[5],6188,model,lab,binding);if(q.kind!=2||q.done!=6188||q.bound!=(first?177:0))throw std::runtime_error("same completed q source");}
 std::vector<Family>families;std::ifstream kin;
 if(first){
  kin.open(argv[4],std::ios::binary);if(sb::tag(kin)!="R150KK31")throw std::runtime_error("same K200 source");for(int v:{31,6188,200,85})if(sb::get(kin,4)!=uint64_t(v))throw std::runtime_error("same K200 dimensions");
  for(int j=0;j<200;j++)if(sb::get(kin,4)!=uint64_t(lab[j].graph)||sb::get(kin,2)!=uint64_t(lab[j].head)||sb::get(kin,2)!=uint64_t(lab[j].cost)||sb::get(kin,4)!=uint64_t(lab[j].source)||sb::get(kin,4)!=uint64_t(lab[j].raw))throw std::runtime_error("same canonical original K labels");
 }
 if(bases){
  std::ifstream recipe(argv[5]);std::string magic;int n;recipe>>magic>>n;if(magic!="R150_197_TRUE_SEVEN_SOURCE_JETS_V1"||n!=3)throw std::runtime_error("true seven source recipe");
  families.resize(3);const std::array<int,3>counts{4,4,9};const std::array<std::vector<int>,3>expected{{{2275,2276,2277,2278},{4001,4002,4003,4004},{2,3,4,5,6,7,8,9,10}}};
  for(int f=0;f<3;f++){auto&v=families[f];recipe>>v.path;v.count=counts[f];v.labels=expected[f];v.in=std::make_unique<std::ifstream>(v.path,std::ios::binary);auto&in=*v.in;auto tag=sb::tag(in);v.width=tag=="R150PS31"?2:4;
   if(tag!="R150PS31"&&tag!="R150P431"&&tag!="R150P531"&&tag!="R150P631")throw std::runtime_error("true kappa source format");
   if(sb::get(in,4)!=31)throw std::runtime_error("source prime");v.mod=sb::get(in,4);if(v.mod!=31&&v.mod!=29791&&v.mod!=923521&&v.mod!=28629151&&v.mod!=887503681)throw std::runtime_error("true source modulus");
   if(sb::get(in,4)!=6188||sb::get(in,4)!=uint64_t(v.count))throw std::runtime_error("true source count");v.bound=sb::get(in,4);for(int x:v.labels)if(sb::get(in,2)!=uint64_t(x))throw std::runtime_error("true kappa labels");
  }if(recipe>>magic)throw std::runtime_error("true source recipe tail");
 }
 std::array<std::vector<Term>,17>terms;auto polyJet=[&](const auto&p){jt::Co a{};for(int d=0;d<int(p.size());d++)if(p[d])for(int k=0;k<10;k++)a[k]=(a[k]+int64_t(p[d]%modulus)*pw[d][k])%modulus;return a;};
 for(int e=0;e<17;e++){
  if(e<11){for(int k=0;k<66;k++)if(model.Qh[e][k]%modulus){auto[x,y]=model.quadratic[k];jt::Co a{};a[0]=model.Qh[e][k]%modulus;terms[e].push_back({model.var[x]+model.var[y],a});}for(int v=0;v<11;v++){auto a=polyJet(model.Lh[e][v]);if(std::any_of(a.begin(),a.end(),[](int c){return c!=0;}))terms[e].push_back({model.var[v],a});}}
  else for(int k=0;k<66;k++){auto a=polyJet(model.Gh[e-11][k]);if(std::any_of(a.begin(),a.end(),[](int c){return c!=0;})){auto[x,y]=model.quadratic[k];terms[e].push_back({model.var[x]+model.var[y],a});}}
 }
 std::vector<uint64_t>product(size_t(4367)*10*nt);int completed=0;std::string checkpoint=prefix+"-product-checkpoint.bin";
 {std::ifstream in(checkpoint,std::ios::binary);if(in){if(sb::tag(in)!="R1503X31")throw std::runtime_error("actual product checkpoint");for(int v:{31,modulus,6188,nt,10,4367,first?1:bases?2:3})if(sb::get(in,4)!=uint64_t(v))throw std::runtime_error("actual product checkpoint scope");completed=sb::get(in,4);if(completed<0||completed>6188)throw std::runtime_error("actual completed row count");std::string b(64,' ');in.read(b.data(),64);if(b!=binding)throw std::runtime_error("actual product binding");in.read(reinterpret_cast<char*>(product.data()),product.size()*8);if(!in)throw std::runtime_error("actual partial product array");sb::tail(in);}}
 auto save=[&](int done){std::ofstream out(checkpoint+".tmp",std::ios::binary);out.write("R1503X31",8);for(int v:{31,modulus,6188,nt,10,4367,first?1:bases?2:3,done})u32(out,v);out.write(binding.data(),64);out.write(reinterpret_cast<const char*>(product.data()),product.size()*8);out.close();if(!out||std::rename((checkpoint+".tmp").c_str(),checkpoint.c_str()))throw std::runtime_error("atomic actual original product checkpoint");std::ofstream meta(prefix+"-product-checkpoint.json");meta<<"{\"completedOriginalRows\":"<<done<<",\"actualPartialProductArraySaved\":true,\"mode\":\""<<mode<<"\",\"bindingSHA256\":\""<<binding<<"\"}\n";};
 std::vector<uint32_t>source(10*nt);uint64_t products=0,nonzero=0;int resumed=completed;
 // Bound: each cell receives <=6188*11*10 terms below923521^2; uint64 accumulation is safe.
 for(int r=1;r<=6188;r++){
  std::fill(source.begin(),source.end(),0);int delta=model.delta(r),e=(r-1)%17;
  if(first){model.rowHeader(kin,r);for(int j=0;j<200;j++){int n=sb::get(kin,2),last=0;if(n>lab[j].cost-delta+1)throw std::runtime_error("same original K coefficient cost");jt::Co a{};
    for(int d=0;d<n;d++){last=sb::get(kin,1);if(last>30)throw std::runtime_error("same canonical K coefficient");if(r>completed&&j>=1&&j<=197&&last)for(int k=0;k<10;k++)a[k]=(a[k]+int64_t(last)*pw[d][k])%modulus;}if(n&&!last)throw std::runtime_error("K trailing zero");
    if(r>completed&&j>=1&&j<=197)for(int k=0;k<10;k++)source[k*nt+j-1]=sb::mod(a[k]-31*BitOps::get(q.rows[r-1],jt::S,k*jt::W*32+j-1),modulus);
   }}
  else if(bases){for(int f=0;f<3;f++){auto&v=families[f];auto&in=*v.in;model.rowHeader(in,r);
    for(int j=0;j<v.count;j++){int n=sb::get(in,2),last=0;if(n>v.bound-delta+1)throw std::runtime_error("actual kappa source cost");int dest=f==0?(j<2?j:-1):f==1?j+2:j==0?6:-1;
     for(int d=0;d<n;d++){last=sb::get(in,v.width);if(last>=v.mod)throw std::runtime_error("actual kappa integer coefficient");if(r>completed&&dest>=0&&last)for(int k=0;k<10;k++)source[k*nt+dest]=(source[k*nt+dest]+int64_t(last%modulus)*pw[d][k])%modulus;}if(n&&!last)throw std::runtime_error("kappa trailing zero");
    }
   }}
  else if(r>completed)for(int k=0;k<10;k++)for(int j=0;j<nt;j++)source[k*nt+j]=BitOps::get(q.rows[r-1],jt::S,k*jt::W*32+j);
  if(r<=completed)continue;for(auto x:source)nonzero+=x!=0;
  uint64_t mult=model.multipliers[(r-1)/17];
  for(const auto&t:terms[e]){int c=model.component.at(mult+t.monomial);uint64_t*dest=product.data()+size_t(c)*10*nt;
   for(int k=0;k<10;k++)if(int a=t.a[k])for(int z=0;z<10-k;z++){const uint32_t*src=source.data()+z*nt;uint64_t*out=dest+(z+k)*nt;for(int j=0;j<nt;j++)out[j]+=uint64_t(a)*src[j];products+=nt;}
  }
  if(r%500==0||r==6188||jt::stopped){std::cout<<"{\"phase\":\"197-original17-root2-integer-product\",\"mode\":\""<<mode<<"\",\"completedOriginalRows\":"<<r<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;}
  if(jt::stopped){save(r);return 124;}
 }
 if(first)sb::tail(kin);for(auto&v:families)sb::tail(*v.in);
 std::array<int,17>units{},returnUnits{};for(int e=0;e<17;e++){units[e]=int64_t(model.denominator%modulus)*inverse(model.contents[e]%modulus,modulus)%modulus;returnUnits[e]=int64_t(model.contents[e]%modulus)*inverse(model.denominator%modulus,modulus)%modulus;if(int64_t(units[e])*returnUnits[e]%modulus!=1)throw std::runtime_error("original primitive row transport");}
 std::ifstream old;if(first){old.open(argv[6],std::ios::binary);if(sb::tag(old)!="R150DJ31")throw std::runtime_error("old actual first-five R2");for(int v:{31,198,4367,8})if(sb::get(old,4)!=uint64_t(v))throw std::runtime_error("old actual R2 dimensions");for(int j=0;j<198;j++)if(sb::get(old,2)!=uint64_t(lab[j].head))throw std::runtime_error("old R2 labels");}
 std::ifstream T;if(third){T.open(argv[6],std::ios::binary);if(sb::tag(T)!="R1503R31")throw std::runtime_error("exact integer T mod961");for(int v:{31,961,4367,197,10})if(sb::get(T,4)!=uint64_t(v))throw std::runtime_error("actual T dimensions");std::string b(64,' ');T.read(b.data(),64);if(b!=binding)throw std::runtime_error("actual T binding");for(int j=0;j<197;j++)if(sb::get(T,2)!=uint64_t(jt::label(lab,j)))throw std::runtime_error("actual T labels");}
 const std::string outfile=prefix+(bases?"-true-seven-b-mod961-root2-ten.bin":first?"-R2-mod961-root2-ten.bin":"-third-projected-original-delta-jets.bin");
 std::ofstream out(outfile,std::ios::binary);out.write(bases?"R1503B31":first?"R1503R31":"R150DJ31",8);
 if(third){for(int v:{31,197,4367,8})u32(out,v);for(int j=0;j<197;j++)u16(out,jt::label(lab,j));}
 else{for(int v:{31,961,4367,nt,10})u32(out,v);out.write(binding.data(),64);if(first)for(int j=0;j<197;j++)u16(out,jt::label(lab,j));}
 uint64_t nonzeroOut=0,verified=0;std::vector<int>oldvalues(8*198);
 for(int c=0;c<4367;c++){
  uint64_t key=model.keys[c];sb::put(out,key,8);if(first){if(sb::get(old,8)!=key)throw std::runtime_error("same old4367 original monomial");for(auto&a:oldvalues){a=sb::get(old,1);if(a>30)throw std::runtime_error("old R2 coefficient");}}
  if(third){if(sb::get(T,8)!=key)throw std::runtime_error("same T4367 monomial");for(int k=0;k<3;k++)for(int j=0;j<197;j++)out.put(0);}
  for(int k=0;k<10;k++)for(int j=0;j<nt;j++){
   int a=product[(size_t(c)*10+k)*nt+j]%modulus;
   if(third){int t=sb::get(T,2);if(t>960)throw std::runtime_error("canonical integer T");int diff=sb::mod(t-a,961);if(diff%31)throw std::runtime_error("whole original17 ten-jet q2 identity failed");verified++;if(k<5){int v=diff/31;out.put(char(v));nonzeroOut+=v!=0;}}
   else{int divisor=first||j>=2?961:31;if(a%divisor)throw std::runtime_error("actual original integer division failed");int v=(a/divisor)%961;u16(out,v);nonzeroOut+=v!=0;verified++;
    if(first&&k<5&&v%31!=oldvalues[(k+3)*198+j+1])throw std::runtime_error("new integer carry changed paid first-five R2 class representative");}
  }
 }
 if(first)sb::tail(old);if(third)sb::tail(T);out.close();if(!out)throw std::runtime_error("actual local original divided output");
 std::ofstream meta(prefix+"-original-product.json");meta<<"{\"status\":\"completed\",\"mode\":\""<<mode<<"\",\"targetCount\":"<<nt<<",\"allOriginalRows\":6188,\"allOriginalOutputComponents\":4367,\"TaylorCenter\":2,\"TaylorPrecision\":10,\"integerProductModulus\":"<<modulus<<",\"allOriginalProductJetCoefficientsDivisible\":true,\"originalRowScaleTransportVerified\":true,\"sameCanonicalIntegerSourcesRetained\":true,\"oldFirstFiveR2Compared\":"<<(first?"true":"false")<<",\"fullOriginalTenJetQ2IdentityVerified\":"<<(third?"true":"false")<<",\"thirdTruncatedIntegerFiveBeforeDivision\":"<<(third?"true":"false")<<",\"root1SlotsAreExplicitProjectionZeros\":"<<(third?"true":"false")<<",\"globalPolynomialSourceIdentityClaimed\":false,\"verifiedOriginalJetCoordinates\":"<<verified<<",\"nonzeroOutputJets\":"<<nonzeroOut<<",\"processedIntegerScalarProducts\":"<<products<<",\"processedNonzeroSourceJets\":"<<nonzero<<",\"resumedOriginalRows\":"<<resumed<<",\"bindingSHA256\":\""<<binding<<"\",\"elapsedSeconds\":"<<elapsed()<<"}\n";meta.close();if(!meta)throw std::runtime_error("integer local product receipt");
 std::cout<<"{\"status\":\"197-original17-local-integer-product-complete\",\"mode\":\""<<mode<<"\",\"elapsedSeconds\":"<<elapsed()<<"}\n";return 0;
}catch(const std::exception&e){std::cerr<<"R150_197_LOCAL_INTEGER_PRODUCT_FAILED "<<e.what()<<"\n";return 1;}}
