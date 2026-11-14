// The actual second original residual (H0*T-A*X)/31^2 modulo31.
// Input X is the saved primitive source modulo961, never an NF-only source.
#include "2026-11-14-r150-f31-bitplane-789f.hpp"
#include <sys/resource.h>
static uint32_t sr_u32(std::istream &in){uint32_t x=0;for(int k=0;k<4;k++){int a=in.get();if(a<0)throw std::runtime_error("truncated u32");x|=uint32_t(a)<<(8*k);}return x;}
static uint16_t sr_u16(std::istream &in){int a=in.get(),b=in.get();if(a<0||b<0)throw std::runtime_error("truncated u16");return a|(b<<8);}
static uint64_t sr_u64(std::istream &in){uint64_t x=0;for(int k=0;k<8;k++){int a=in.get();if(a<0)throw std::runtime_error("truncated u64");x|=uint64_t(a)<<(8*k);}return x;}
static void sr_put64(std::ostream &out,uint64_t x){for(int k=0;k<8;k++)out.put(char(x>>(8*k)));}
int main(int argc,char **argv){try{
 if(argc!=5)return 2;
 constexpr int ns=2195,nb=3333,nraw=6188,nt=9,modulus=29791,divisor=961;
 auto start=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 std::ifstream model(argv[1]),higher(argv[2]),source(argv[3],std::ios::binary);if(!model||!higher||!source)throw std::runtime_error("original second residual input open");
 std::string marker;model>>marker;if(marker!="R150_NATIVE_NF_V1")throw std::runtime_error("original model header");
 std::array<std::array<int,66>,11> Q{},Q3{};std::array<std::array<std::array<int,11>,11>,11> L{},L3{};
 auto readCoefficient=[&](int &a){model>>a;if(!model||a<0||a>30)throw std::runtime_error("actual original F31 coefficient");};
 for(int e=0;e<11;e++){for(auto &a:Q[e])readCoefficient(a);for(auto &row:L[e])for(auto &a:row)readCoefficient(a);}
 int count;model>>count;if(count!=nb)throw std::runtime_error("original prebasis count");std::vector<Source> pre(nb);for(auto &S:pre)model>>S.e>>S.mult>>S.pivot>>S.raw;
 std::array<std::array<std::array<int,6>,66>,6> G{},G3{};for(auto &row:G)for(auto &poly:row)for(auto &a:poly)readCoefficient(a);
 int sc,tc;model>>sc>>tc;if(sc!=ns||tc!=nt)throw std::runtime_error("original source dimensions");std::vector<Source> rows(ns);for(auto &S:rows)model>>S.e>>S.mult>>S.raw;
 for(int j=0;j<nt;j++){int target;model>>target;if(target!=j+2)throw std::runtime_error("original nine target dictionary");}if(!model||model>>marker)throw std::runtime_error("original model tail");
 higher>>marker;if(marker!="R150_ORIGINAL_MOD29791_V1")throw std::runtime_error("exact original mod31^3 model required");
 int D;higher>>D;std::array<int,17> content{};for(auto &a:content)higher>>a;
 for(int a:content)if(a<0||a>=modulus||a%31==0)throw std::runtime_error("original row unit");if(D<0||D>=modulus||D%31==0)throw std::runtime_error("original denominator unit");
 auto readHigher=[&](int &a,int residue){higher>>a;if(!higher||a<0||a>=modulus||a%31!=residue)throw std::runtime_error("same complete original coefficient modulo31");};
 for(int e=0;e<11;e++){for(int k=0;k<66;k++)readHigher(Q3[e][k],Q[e][k]);for(int v=0;v<11;v++)for(int d=0;d<=10;d++)readHigher(L3[e][v][d],L[e][v][d]);}
 for(int e=0;e<6;e++)for(int k=0;k<66;k++)for(int d=0;d<=5;d++)readHigher(G3[e][k][d],G[e][k][d]);
 std::array<int,26> H0{};for(auto &a:H0){higher>>a;if(a<0||a>=modulus)throw std::runtime_error("exact H0 coefficient");}int tail;if(!higher||higher>>tail||H0.back()!=3125)throw std::runtime_error("exact degree25 H0");
 std::array<uint64_t,11> variable;variable[0]=1;for(int i=1;i<11;i++)variable[i]=8*variable[i-1];std::vector<std::vector<uint64_t>> mon(6);
 auto enumerate=[&](auto &&self,int left,int lower,uint64_t key,int d)->void{if(!left){mon[d].push_back(key);return;}for(int i=lower;i<11;i++)self(self,left-1,i,key+variable[i],d);};for(int d=0;d<=5;d++)enumerate(enumerate,d,0,0,d);
 std::vector<uint64_t> multipliers;for(int d=0;d<=3;d++)multipliers.insert(multipliers.end(),mon[d].begin(),mon[d].end());if(multipliers.size()!=364)throw std::runtime_error("original multiplier count");
 std::unordered_map<uint64_t,int> component;int nc=0;for(int d=5;d>=1;d--)for(auto key:mon[d])component[key]=nc++;if(nc!=4367)throw std::runtime_error("all original output monomials");
 std::vector<std::pair<int,int>> quadratic;for(int i=0;i<11;i++)for(int j=i;j<11;j++)quadratic.push_back({i,j});
 char magic[8];source.read(magic,8);if(std::string(magic,8)!="R150P961"||sr_u32(source)!=31||sr_u32(source)!=961||sr_u32(source)!=nraw||sr_u32(source)!=nt)throw std::runtime_error("actual original primitive source modulo961 required");
 int declaredBound=sr_u32(source);if(declaredBound<55||declaredBound>254||sr_u32(source)!=25)throw std::runtime_error("explicit source/target bound");
 for(int a:H0)if(sr_u16(source)!=a%961)throw std::runtime_error("same original target multiplier in actual source");
 if(sr_u16(source)!=D%961)throw std::runtime_error("same original fixed denominator");for(int a:content)if(sr_u16(source)!=a%961)throw std::runtime_error("same original equation normalization");
 std::vector<std::vector<uint16_t>> coefficients(nraw);std::vector<int> degrees(nraw,-1);int sourceCost=-1,maximum=-1;uint64_t coefficientCount=0;
 for(int r=0;r<nraw;r++){
  int equation=r%17,delta=10*(degree(multipliers[r/17])+1)+(equation<11?0:5);
  if(sr_u32(source)!=r+1||source.get()!=equation||sr_u64(source)!=multipliers[r/17]||sr_u16(source)!=delta)throw std::runtime_error("actual original6188 source dictionary");
  std::array<std::vector<uint16_t>,nt> polys;int dmax=-1;
  for(int j=0;j<nt;j++){int length=sr_u16(source);if(length>declaredBound+1-delta)throw std::runtime_error("actual source weighted bound");polys[j].resize(length);
   for(int d=0;d<length;d++){int a=sr_u16(source);if(a>=961)throw std::runtime_error("source is not canonical modulo961");polys[j][d]=a;coefficientCount+=a!=0;}
   if(length&&!polys[j].back())throw std::runtime_error("source trailing zero");dmax=std::max(dmax,length-1);
  }
  if(dmax>=0){sourceCost=std::max(sourceCost,dmax+delta);maximum=std::max(maximum,dmax);degrees[r]=dmax;coefficients[r].resize(size_t(dmax+1)*nt);for(int j=0;j<nt;j++)for(int d=0;d<int(polys[j].size());d++)coefficients[r][size_t(d)*nt+j]=polys[j][d];}
 }
 if(source.get()!=EOF)throw std::runtime_error("trailing complete original primitive source");
 const int B=std::max(55,sourceCost);std::vector<uint64_t> keys(nc);std::vector<int> widths(nc),offset(nc);int total=0;
 for(int d=5;d>=1;d--)for(auto key:mon[d]){int c=component.at(key);keys[c]=key;widths[c]=B+1-10*(d-1);offset[c]=total;total+=widths[c];}
 std::vector<uint64_t> product(size_t(total)*nt);
 auto binomial=[](int n,int k){int a=1;for(int j=1;j<=k;j++)a=a*(n-j+1)/j;return a;};
 for(int target=0;target<nt;target++){int j=target+2;for(int a=0;a<=j;a++)for(int b=a;b<=j;b++){
  int exponent=2*j-a-b,c=component.at(variable[a]+variable[b]);int coefficient=binomial(j,a)*binomial(j,b)*(a==b?1:2)*(exponent%2?-1:1);coefficient=(coefficient%modulus+modulus)%modulus;
  for(int k=0;k<=25;k++){if(exponent+k>=widths[c])throw std::runtime_error("H0 target weighted bound");int value=int(int64_t(coefficient)*H0[k]%modulus);product[size_t(offset[c]+exponent+k)*nt+target]+=(modulus-value)%modulus;}
 }}
 uint64_t products=0;
 for(int r=0;r<nraw;r++){
  int d=degrees[r],equation=r%17;if(d>=0){const auto &packed=coefficients[r];uint64_t multiplier=multipliers[r/17];
   auto addTerm=[&](uint64_t monomial,int exponent,int a){if(!a)return;int c=component.at(multiplier+monomial);if(d+exponent>=widths[c])throw std::runtime_error("complete original integer product bound");
    for(int k=0;k<=d;k++){uint64_t *dest=product.data()+size_t(offset[c]+k+exponent)*nt;const uint16_t *value=packed.data()+size_t(k)*nt;for(int j=0;j<nt;j++){uint64_t next=dest[j]+uint64_t(a)*value[j];dest[j]=next>=(uint64_t(1)<<60)?next%modulus:next;}}products++;
   };
   if(equation<11){for(int v=0;v<11;v++)for(int k=0;k<=10;k++)addTerm(variable[v],k,L3[equation][v][k]);for(int k=0;k<66;k++){auto [a,b]=quadratic[k];addTerm(variable[a]+variable[b],0,Q3[equation][k]);}}
   else for(int k=0;k<66;k++){auto [a,b]=quadratic[k];for(int e=0;e<=5;e++)addTerm(variable[a]+variable[b],e,G3[equation-11][k][e]);}
  }
  if((r+1)%1000==0||r+1==nraw)std::cout<<"{\"phase\":\"actual-second-original-residual\",\"rawRows\":"<<r+1<<",\"originalSourceCost\":"<<sourceCost<<",\"products\":"<<products<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 }
 std::string prefix=argv[4];std::ofstream out(prefix+"-second-residual.bin",std::ios::binary),meta(prefix+"-second-residual.json");if(!out||!meta)throw std::runtime_error("actual second residual output open");
 out.write("R150RH31",8);for(int a:{B,nt,nc,total})u32(out,a);std::array<uint64_t,nt> counts{};int residualCost=-1;uint64_t nonzero=0;
 for(int c=0;c<nc;c++){sr_put64(out,keys[c]);u16(out,widths[c]);int weight=10*(degree(keys[c])-1);
  for(int j=0;j<nt;j++)for(int k=0;k<widths[c];k++){int value=product[size_t(offset[c]+k)*nt+j]%modulus;if(value%divisor)throw std::runtime_error("actual original source fails full identity modulo961");int digit=(31-value/divisor)%31;out.put(char(digit));if(digit){counts[j]++;nonzero++;residualCost=std::max(residualCost,k+weight);}}
 }
 meta<<"{\"format\":\"r150-h25-second-original-padic-residual-v1\",\"status\":\"completed\",\"prime\":31,\"inputSourceModulus\":961,\"integerModelModulus\":29791,\"divisor\":961,\"targetMultiplier\":\"H0=(s-2)*h0\",\"originalRawRows\":6188,\"originalEquations\":17,\"actualFullOriginalIdentityMod961\":true,\"residualDefinition\":\"(H0*T-A*X)/961 mod31 with the actual canonical saved primitive X\",\"allOriginalWeightedBoundsVerified\":true,\"actualSourceCost\":"<<sourceCost<<",\"declaredSourceCostBound\":"<<declaredBound<<",\"residualOutputCostBound\":"<<B<<",\"actualResidualCost\":"<<residualCost<<",\"maximumInputCoefficientDegree\":"<<maximum<<",\"inputNonzeroCoefficients\":"<<coefficientCount<<",\"residualNonzeroCoefficients\":"<<nonzero<<",\"residualNonzeroByTarget\":[";
 for(int j=0;j<nt;j++){if(j)meta<<",";meta<<counts[j];}meta<<"],\"sourceCorrectionComputed\":false,\"characteristicZeroIdentityAsserted\":false,\"elapsedSeconds\":"<<elapsed()<<"}\n";
 out.close();meta.close();if(!out||!meta)throw std::runtime_error("actual second residual output failed");
 std::cout<<"{\"status\":\"h25-second-original-padic-residual-complete\",\"actualFullOriginalIdentityMod961\":true,\"allOriginalWeightedBoundsVerified\":true,\"actualSourceCost\":"<<sourceCost<<",\"actualResidualCost\":"<<residualCost<<",\"sourceCorrectionComputed\":false,\"characteristicZeroIdentityAsserted\":false,\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 return 0;
}catch(const std::exception &e){std::cerr<<"H25_SECOND_ORIGINAL_RESIDUAL_FAILED "<<e.what()<<"\n";return 1;}}
