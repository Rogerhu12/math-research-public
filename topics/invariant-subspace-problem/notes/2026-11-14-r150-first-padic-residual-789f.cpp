// Restore the canonical primitive source and compute its FIRST mod-31^2 residual.
// No characteristic-zero membership or corrected mod-961 identity is asserted.
#include "2026-11-14-r150-f31-bitplane-789f.hpp"
static uint32_t ol_u32(std::istream &in){uint32_t a=0;for(int k=0;k<4;k++){int c=in.get();if(c<0)throw std::runtime_error("truncated u32");a|=uint32_t(c)<<(8*k);}return a;}
static uint16_t ol_u16(std::istream &in){int a=in.get(),b=in.get();if(a<0||b<0)throw std::runtime_error("truncated u16");return a|(b<<8);}
static void ol_u64(std::ostream &out,uint64_t a){for(int k=0;k<8;k++)out.put(char(a>>(8*k)));}
struct OLStep {uint16_t basis;uint8_t coefficient;};
struct OLBack {int basis=0;std::vector<OLStep> steps;};
struct OLForward {int raw=0,scale=0;std::vector<OLStep> steps;};

int main(int argc,char **argv){try{
 if(argc!=8)return 2;auto start=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 const int ns=2195,nb=3333,nraw=6188,nt=9,P=75,PW=P+1,productDegree=85,hd=24;
 std::ifstream cin(argv[1],std::ios::binary),model(argv[2]),normal(argv[3],std::ios::binary),forward(argv[4],std::ios::binary),backward(argv[5],std::ios::binary),higher(argv[6]);if(!cin||!model||!normal||!forward||!backward||!higher)throw std::runtime_error("input open");
 BitOps ops;std::string marker;model>>marker;if(marker!="R150_NATIVE_NF_V1")throw std::runtime_error("original model header");
 std::array<std::array<int,66>,11> Q{};std::array<std::array<std::array<int,11>,11>,11> L{};auto readCoefficient=[&](int &a){model>>a;if(!model||a<0||a>30)throw std::runtime_error("model field coefficient");};
 for(int e=0;e<11;e++){for(auto &a:Q[e])readCoefficient(a);for(auto &row:L[e])for(auto &a:row)readCoefficient(a);}
 int count;model>>count;if(count!=nb)throw std::runtime_error("prebasis size");std::vector<Source> pre(nb);for(auto &s:pre)model>>s.e>>s.mult>>s.pivot>>s.raw;
 std::array<std::array<std::array<int,6>,66>,6> G{};for(auto &row:G)for(auto &poly:row)for(auto &a:poly)readCoefficient(a);
 int sourcesCount,targetsCount;model>>sourcesCount>>targetsCount;if(sourcesCount!=ns||targetsCount!=nt)throw std::runtime_error("complete source count");std::vector<Source> sources(ns);for(auto &s:sources)model>>s.e>>s.mult>>s.raw;for(int j=0;j<nt;j++){int target;model>>target;if(target!=j+2)throw std::runtime_error("original target indices");}if(!model||model>>marker)throw std::runtime_error("model tail");
 std::array<uint64_t,11> variable;variable[0]=1;for(int i=1;i<11;i++)variable[i]=8*variable[i-1];std::vector<std::vector<uint64_t>> mon(6);
 auto enumerate=[&](auto &&self,int left,int lower,uint64_t key,int d)->void{if(!left){mon[d].push_back(key);return;}for(int i=lower;i<11;i++)self(self,left-1,i,key+variable[i],d);};for(int d=0;d<=5;d++)enumerate(enumerate,d,0,0,d);
 std::vector<uint64_t> multipliers;for(int d=0;d<=3;d++)multipliers.insert(multipliers.end(),mon[d].begin(),mon[d].end());if(multipliers.size()!=364)throw std::runtime_error("original multiplier count");
 auto checkSource=[&](const Source &s){if(s.raw<1||s.raw>nraw||s.e!=(s.raw-1)%17||s.mult!=multipliers[(s.raw-1)/17])throw std::runtime_error("raw original seventeen-row mapping");};for(const auto &s:pre){checkSource(s);if(s.e>=11)throw std::runtime_error("constant prebasis is not original N");}for(const auto &s:sources)checkSource(s);
 std::unordered_map<uint64_t,int> component;int nc=0;for(int d=5;d>=1;d--)for(auto key:mon[d])component[key]=nc++;if(nc!=4367)throw std::runtime_error("original nonconstant component count");
 std::vector<std::pair<int,int>> quadratic;for(int i=0;i<11;i++)for(int j=i;j<11;j++)quadratic.push_back({i,j});
 std::string highMagic;higher>>highMagic;if(highMagic!="R150_ORIGINAL_MOD961_V1")throw std::runtime_error("original integer mod961 model");int D2;higher>>D2;std::array<int,17> contents2{};for(auto &a:contents2){higher>>a;if(a<0||a>960||a%31==0)throw std::runtime_error("original integer row normalization");}if(D2<0||D2>960||D2%31==0)throw std::runtime_error("original fixed denominator mod961");
 std::array<std::array<int,66>,11> Q2{};std::array<std::array<std::array<int,11>,11>,11> L2{};std::array<std::array<std::array<int,6>,66>,6> G2{};
 auto readHigher=[&](int &a,int residue){higher>>a;if(!higher||a<0||a>960||a%31!=residue)throw std::runtime_error("original integer coefficient residue mismatch");};
 for(int e=0;e<11;e++){for(int k=0;k<66;k++)readHigher(Q2[e][k],Q[e][k]);for(int v=0;v<11;v++)for(int d=0;d<=10;d++)readHigher(L2[e][v][d],L[e][v][d]);}
 for(int e=0;e<6;e++)for(int k=0;k<66;k++)for(int d=0;d<=5;d++)readHigher(G2[e][k][d],G[e][k][d]);
 std::vector<int> h0(hd+1);for(auto &a:h0){higher>>a;if(a<0||a>960)throw std::runtime_error("h0 mod961 coefficient");}int highExtra;if(!higher||higher>>highExtra||h0.back()!=3125%961)throw std::runtime_error("integer h0 degree or tail");
 char magic[8];cin.read(magic,8);if(std::string(magic,8)!="R150TC31"||ol_u32(cin)!=ns||ol_u32(cin)!=nt||ol_u32(cin)!=hd)throw std::runtime_error("complete target coefficient format");std::vector<int> h(hd+1);for(auto &a:h){a=cin.get();if(a<0||a>30)throw std::runtime_error("h coefficient");}if(h.back()!=1)throw std::runtime_error("monic h31");for(int k=0;k<=hd;k++)if(h0[k]%31!=25*h[k]%31)throw std::runtime_error("h0 mod31 scale");
 std::vector<Row> raw(nraw,Row(5*PW)),beta(nb,Row(5*PW));std::vector<bool> occupied(nraw);
 for(int index=0;index<ns;index++){int number=ol_u32(cin),r=ol_u32(cin),delta=ol_u16(cin);const auto &S=sources[index];int expectedDelta=10*(degree(S.mult)+1)+(S.e<11?0:5);if(number!=index+1||r!=S.raw||delta!=expectedDelta||occupied[r-1])throw std::runtime_error("complete normal-form source identity");occupied[r-1]=true;for(int j=0;j<nt;j++){int len=ol_u16(cin);if(len>86-delta)throw std::runtime_error("source coefficient bound");int last=0;for(int d=0;d<len;d++){last=cin.get();if(last<0||last>30)throw std::runtime_error("coefficient field");BitOps::set(raw[r-1],PW,d*32+j,last);}if(len&&!last)throw std::runtime_error("trailing coefficient zero");}}
 if(cin.get()!=EOF)throw std::runtime_error("trailing completed coefficients");
 auto actualDegree=[&](const Row &row){for(int d=P;d>=0;d--){uint32_t a=0;for(int plane=0;plane<5;plane++)a|=row[plane*PW+d];if(a){if(a>>9)throw std::runtime_error("nonzero target padding");return d;}}return -1;};
 normal.read(magic,8);if(std::string(magic,8)!="R150NR31"||ol_u32(normal)!=ns+nt)throw std::runtime_error("complete normal-form source trace");uint64_t normalOperations=0,activeNormalOperations=0;
 for(int index=0;index<ns+nt;index++){int r=ol_u32(normal),target=ol_u16(normal),steps=ol_u32(normal);Triple current;int degreeCurrent;
  if(index<ns){if(r!=sources[index].raw||target)throw std::runtime_error("source normal trace mapping");current[0]=raw[r-1];degreeCurrent=actualDegree(current[0]);}
  else{int j=index-ns;if(r||target!=j+2)throw std::runtime_error("target normal trace mapping");current[0].resize(5*PW);for(int d=0;d<=hd;d++)BitOps::set(current[0],PW,d*32+j,h[d]);degreeCurrent=hd;}
  if(degreeCurrent>=0)BitOps::refresh(current,PW,0);
  for(int k=0;k<steps;k++){int basis=ol_u16(normal)-1,shift=normal.get(),a=normal.get();if(basis<0||basis>=nb||shift<0||a<1||a>30)throw std::runtime_error("normal source operation");if(degreeCurrent>=0){if(degreeCurrent+shift>P)throw std::runtime_error("B(hJ-HC) degree bound");auto rep=ops.rep[index<ns?31-a:a];BitOps::add(beta[basis],PW,shift,current[rep.c],PW,0,degreeCurrent+1,rep.rot,rep.neg);activeNormalOperations++;}normalOperations++;}
  if((index+1)%250==0||index+1==ns+nt)std::cout<<"{\"phase\":\"restore-constant-prebasis-coefficients\",\"normalSources\":"<<index+1<<",\"operations\":"<<normalOperations<<",\"activeOperations\":"<<activeNormalOperations<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 }
 if(normal.get()!=EOF||normalOperations!=25305683)throw std::runtime_error("normal trace not complete");
 backward.read(magic,8);if(std::string(magic,8)!="R150RJ31"||ol_u32(backward)!=nb)throw std::runtime_error("backward constant prebasis trace");std::vector<OLBack> back(nb);std::vector<bool> backSeen(nb);
 for(auto &record:back){record.basis=ol_u16(backward)-1;int steps=ol_u32(backward);if(record.basis<0||record.basis>=nb||backSeen[record.basis])throw std::runtime_error("backward prebasis row identity");backSeen[record.basis]=true;record.steps.resize(steps);for(auto &step:record.steps){step.basis=ol_u16(backward);step.coefficient=backward.get();if(step.basis<1||step.basis>nb||step.basis==record.basis+1||step.coefficient<1||step.coefficient>30)throw std::runtime_error("backward operation");}}
 if(backward.get()!=EOF)throw std::runtime_error("trailing backward trace");uint64_t backwardOperations=0,forwardOperations=0;
 for(auto it=back.rbegin();it!=back.rend();it++){int d=actualDegree(beta[it->basis]);Triple current;if(d>=0){current[0]=beta[it->basis];BitOps::refresh(current,PW,0);}for(auto step:it->steps){if(d>=0){auto rep=ops.rep[31-step.coefficient];BitOps::add(beta[step.basis-1],PW,0,current[rep.c],PW,0,d+1,rep.rot,rep.neg);}backwardOperations++;}}
 forward.read(magic,8);if(std::string(magic,8)!="R150PB31"||ol_u32(forward)!=nb)throw std::runtime_error("forward original prebasis trace");std::vector<OLForward> front(nb);
 for(int index=0;index<nb;index++){auto &record=front[index];record.raw=ol_u32(forward);record.scale=forward.get();int steps=ol_u32(forward);if(record.raw!=pre[index].raw||record.scale<1||record.scale>30)throw std::runtime_error("forward raw source or scale");record.steps.resize(steps);for(auto &step:record.steps){step.basis=ol_u16(forward);step.coefficient=forward.get();if(step.basis<1||step.basis>index||step.coefficient<1||step.coefficient>30)throw std::runtime_error("forward dependency is not an earlier basis row");}}
 if(forward.get()!=EOF)throw std::runtime_error("trailing forward trace");
 for(int index=nb-1;index>=0;index--){auto &record=front[index];int d=actualDegree(beta[index]);Triple current;if(d>=0){current[0]=beta[index];ops.multiple(current[0],PW,0,record.scale);BitOps::refresh(current,PW,0);BitOps::add(raw[record.raw-1],PW,0,current[0],PW,0,d+1,0,0);}for(auto step:record.steps){if(d>=0){auto rep=ops.rep[31-step.coefficient];BitOps::add(beta[step.basis-1],PW,0,current[rep.c],PW,0,d+1,rep.rot,rep.neg);}forwardOperations++;}}
 if(backwardOperations!=1010703||forwardOperations!=782976)throw std::runtime_error("constant prebasis trace count");

 // Work with the primitive INTEGER equations. Their scalar reduction is 25*h31.
 for(const auto &s:pre){if(occupied[s.raw-1])throw std::runtime_error("prebasis/source overlap");occupied[s.raw-1]=true;}
 if(std::count(occupied.begin(),occupied.end(),true)!=5528)throw std::runtime_error("fixed original source set");
 for(auto &r:raw)ops.multiple(r,PW,0,25);
 std::vector<uint64_t> keys(nc);std::vector<int> widths(nc),offset(nc);int total=0;
 for(int d=5;d>=1;d--)for(auto key:mon[d]){int c=component.at(key);keys[c]=key;widths[c]=86-10*(d-1);offset[c]=total;total+=widths[c];}
 if(total!=219032)throw std::runtime_error("fixed weighted output dimension");
 std::vector<uint32_t> product(size_t(total)*nt);
 auto binomial=[](int n,int k){int a=1;for(int j=1;j<=k;j++)a=a*(n-j+1)/j;return a;};
 for(int target=0;target<nt;target++){int j=target+2;for(int a=0;a<=j;a++)for(int b=a;b<=j;b++){
  int exponent=2*j-a-b,c=component.at(variable[a]+variable[b]);int coefficient=binomial(j,a)*binomial(j,b)*(a==b?1:2)*(exponent%2?-1:1);coefficient=(coefficient%961+961)%961;
  for(int k=0;k<=hd;k++){if(exponent+k>=widths[c])throw std::runtime_error("original h0 target outside fixed budget");int value=coefficient*h0[k]%961;product[size_t(offset[c]+exponent+k)*nt+target]+=(961-value)%961;}
 }}
 std::string prefix=argv[7];std::ofstream xout(prefix+"-initial-standard-source.bin",std::ios::binary),rout(prefix+"-first-residual.bin",std::ios::binary),meta(prefix+"-first-residual.json");if(!xout||!rout||!meta)throw std::runtime_error("first lift output open");
 xout.write("R150P031",8);for(int value:{nraw,nt,85,217374,hd})u32(xout,value);for(int a:h0)u16(xout,a);
 uint64_t coefficientCount=0,integerProducts=0;int maximum=-1,maxCost=-1,nonzeroRows=0;
 for(int r=0;r<nraw;r++){
  int d=actualDegree(raw[r]),equation=r%17;uint64_t multiplier=multipliers[r/17];int delta=10*(degree(multiplier)+1)+(equation<11?0:5);
  if(d>=0){if(!occupied[r]||d+delta>85)throw std::runtime_error("initial source violates fixed original weighted budget");maximum=std::max(maximum,d);maxCost=std::max(maxCost,d+delta);nonzeroRows++;}
  u32(xout,r+1);xout.put(char(equation));ol_u64(xout,multiplier);u16(xout,delta);
  std::vector<uint8_t> packed(size_t(d+1)*nt);
  for(int j=0;j<nt;j++){std::vector<uint8_t> polynomial(d+1);for(int k=0;k<=d;k++){int a=BitOps::get(raw[r],PW,k*32+j);packed[size_t(k)*nt+j]=a;polynomial[k]=a;coefficientCount+=a!=0;}while(!polynomial.empty()&&!polynomial.back())polynomial.pop_back();u16(xout,polynomial.size());xout.write(reinterpret_cast<const char*>(polynomial.data()),polynomial.size());}
  if(d>=0){
   auto addTerm=[&](uint64_t monomial,int exponent,int a){if(!a)return;int c=component.at(multiplier+monomial);if(d+exponent>=widths[c])throw std::runtime_error("integer product exceeds fixed output budget");
    for(int k=0;k<=d;k++){uint32_t *destination=product.data()+size_t(offset[c]+k+exponent)*nt;const uint8_t *source=packed.data()+size_t(k)*nt;
     for(int j=0;j<nt;j++){uint32_t value=destination[j]+uint32_t(a)*source[j];destination[j]=value>=(uint32_t(1)<<30)?value%961:value;}
    }integerProducts++;
   };
   if(equation<11){for(int v=0;v<11;v++)for(int k=0;k<=10;k++)addTerm(variable[v],k,L2[equation][v][k]);for(int k=0;k<66;k++){auto [a,b]=quadratic[k];addTerm(variable[a]+variable[b],0,Q2[equation][k]);}}
   else for(int k=0;k<66;k++){auto [a,b]=quadratic[k];for(int e=0;e<=5;e++)addTerm(variable[a]+variable[b],e,G2[equation-11][k][e]);}
  }
  if((r+1)%1000==0||r+1==nraw)std::cout<<"{\"phase\":\"original-integer-mod961-product\",\"originalRows\":"<<r+1<<",\"maximumCoefficientDegree\":"<<maximum<<",\"maximumSourceCost\":"<<maxCost<<",\"integerMonomialProducts\":"<<integerProducts<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 }
 rout.write("R150RH31",8);for(int value:{85,nt,nc,total})u32(rout,value);std::array<uint64_t,nt> residualNonzero{};uint64_t nonzeroResidual=0;int residualMaxCost=-1;
 for(int c=0;c<nc;c++){ol_u64(rout,keys[c]);u16(rout,widths[c]);int weight=10*(degree(keys[c])-1);
  for(int j=0;j<nt;j++)for(int k=0;k<widths[c];k++){int a=product[size_t(offset[c]+k)*nt+j]%961;if(a%31)throw std::runtime_error("initial primitive source does not solve the exact original model mod31");int digit=(31-a/31)%31;rout.put(char(digit));if(digit){nonzeroResidual++;residualNonzero[j]++;residualMaxCost=std::max(residualMaxCost,k+weight);}}
 }
 meta<<"{\"format\":\"r150-first-original-padic-residual-v1\",\"status\":\"completed\",\"prime\":31,\"modulusUsed\":961,\"fixedSourceBudget\":85,\"integerSourceColumns\":217374,\"integerOutputCoordinates\":219032,\"originalEquations\":17,\"originalRawRows\":6188,\"targets\":[2,3,4,5,6,7,8,9,10],\"h0Mod31Scale\":25,\"initialOriginalPrimitiveIdentityMod31\":true,\"allWeightedBoundsVerified\":true,\"maximumInitialCoefficientDegree\":"<<maximum<<",\"maximumInitialSourceCost\":"<<maxCost<<",\"nonzeroInitialRows\":"<<nonzeroRows<<",\"nonzeroInitialCoefficients\":"<<coefficientCount<<",\"nonzeroResidualCoefficients\":"<<nonzeroResidual<<",\"maximumResidualCost\":"<<residualMaxCost<<",\"residualNonzeroByTarget\":[";
 for(int j=0;j<nt;j++){if(j)meta<<",";meta<<residualNonzero[j];}
 meta<<"],\"sourceIdentity\":\"The source is the unique original primitive standard representative of h0*t modulo31, with h0=25*h31 mod31. Original integer coefficients are computed modulo961 and agree with every frozen primitive model coefficient modulo31. Every coefficient of A*x0-h0*t is checked divisible by31. The output is exactly (h0*t-A*x0)/31 mod31. No correction, mod961 target identity, or characteristic-zero membership is asserted.\",\"elapsedSeconds\":"<<elapsed()<<"}\n";
 xout.close();rout.close();meta.close();if(!xout||!rout||!meta)throw std::runtime_error("first residual output failed");
 std::cout<<"{\"status\":\"first-original-padic-residual-complete\",\"prime\":31,\"modulusUsed\":961,\"initialOriginalPrimitiveIdentityMod31\":true,\"allWeightedBoundsVerified\":true,\"maximumInitialCoefficientDegree\":"<<maximum<<",\"maximumInitialSourceCost\":"<<maxCost<<",\"nonzeroResidualCoefficients\":"<<nonzeroResidual<<",\"maximumResidualCost\":"<<residualMaxCost<<",\"correctionComputed\":false,\"elapsedSeconds\":"<<elapsed()<<"}\n";
 return 0;
}catch(const std::exception &e){std::cerr<<"FIRST_PADIC_RESIDUAL_FAILED "<<e.what()<<"\n";return 1;}}
