// Restore the H0=(s-2)h0 correction from its actual original2195 source.
// Read the frozen original traces and verify ALL original17 equations modulo961.
#include "2026-11-14-r150-f31-bitplane-789f.hpp"
static uint32_t ol_u32(std::istream &in){uint32_t a=0;for(int k=0;k<4;k++){int c=in.get();if(c<0)throw std::runtime_error("truncated u32");a|=uint32_t(c)<<(8*k);}return a;}
static uint16_t ol_u16(std::istream &in){int a=in.get(),b=in.get();if(a<0||b<0)throw std::runtime_error("truncated u16");return a|(b<<8);}
static void ol_u64(std::ostream &out,uint64_t a){for(int k=0;k<8;k++)out.put(char(a>>(8*k)));}
struct OLStep {uint16_t basis;uint8_t coefficient;};
struct OLBack {int basis=0;std::vector<OLStep> steps;};
struct OLForward {int raw=0,scale=0;std::vector<OLStep> steps;};

int main(int argc,char **argv){try{
 if(argc!=12)return 2;auto start=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 const int ns=2195,nb=3333,nraw=6188,nt=9,P=172,PW=P+1,productDegree=182,hd=24;
 std::ifstream cin(argv[1],std::ios::binary),model(argv[2]),normal(argv[3],std::ios::binary),forward(argv[4],std::ios::binary),backward(argv[5],std::ios::binary),higher(argv[6]),initial(argv[7],std::ios::binary),kernels(argv[8],std::ios::binary),firstTrace(argv[9],std::ios::binary),betaTrace(argv[10],std::ios::binary);if(!cin||!model||!normal||!forward||!backward||!higher||!initial||!kernels||!firstTrace||!betaTrace)throw std::runtime_error("original H0 recovery input open");
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

 char magic[8];cin.read(magic,8);
 if(std::string(magic,8)!="R150SC31"||ol_u32(cin)!=ns||ol_u32(cin)!=nt||ol_u32(cin)!=productDegree||ol_u32(cin)!=86||ol_u32(cin)!=86)throw std::runtime_error("completed H0 canonical normal-source format");
 const std::array<int,9> c1{2,23,3,6,7,19,24,2,14},c2{3,22,14,20,15,28,11,18,7};
 std::vector<Row> raw(nraw,Row(5*PW)),beta(nb,Row(5*PW));std::vector<bool> occupied(nraw);
 int normalSourceMaximumCost=-1;
 for(int index=0;index<ns;index++){
  int number=ol_u32(cin),r=ol_u32(cin),delta=ol_u16(cin);const auto &S=sources[index];int expectedDelta=10*(degree(S.mult)+1)+(S.e<11?0:5);
  if(number!=index+1||r!=S.raw||delta!=expectedDelta||occupied[r-1])throw std::runtime_error("complete normal-form source identity");occupied[r-1]=true;
  for(int j=0;j<nt;j++){int len=ol_u16(cin);if(len>productDegree+1-delta)throw std::runtime_error("actual canonical source cost bound");int last=0;
   for(int d=0;d<len;d++){last=cin.get();if(last<0||last>30)throw std::runtime_error("source coefficient field");BitOps::set(raw[r-1],PW,d*32+j,last);if(last)normalSourceMaximumCost=std::max(normalSourceMaximumCost,d+delta);}
   if(len&&!last)throw std::runtime_error("noncanonical original source polynomial");
  }
 }
 if(cin.get()!=EOF)throw std::runtime_error("trailing complete H0 source coefficients");
 auto actualDegree=[&](const Row &row){for(int d=P;d>=0;d--){uint32_t a=0;for(int plane=0;plane<5;plane++)a|=row[plane*PW+d];if(a){if(a>>9)throw std::runtime_error("nonzero target padding");return d;}}return -1;};
 normal.read(magic,8);if(std::string(magic,8)!="R150NR31"||ol_u32(normal)!=ns+nt)throw std::runtime_error("complete normal-form source trace");uint64_t normalOperations=0,activeNormalOperations=0;
 for(int index=0;index<ns+nt;index++){int r=ol_u32(normal),target=ol_u16(normal),steps=ol_u32(normal);Triple current;int degreeCurrent;
  if(index<ns){if(r!=sources[index].raw||target)throw std::runtime_error("source normal trace mapping");current[0]=raw[r-1];degreeCurrent=actualDegree(current[0]);}
  else{int j=index-ns;if(r||target!=j+2)throw std::runtime_error("unused original target trace mapping");degreeCurrent=-1;}
  if(degreeCurrent>=0)BitOps::refresh(current,PW,0);
  for(int k=0;k<steps;k++){int basis=ol_u16(normal)-1,shift=normal.get(),a=normal.get();if(basis<0||basis>=nb||shift<0||a<1||a>30)throw std::runtime_error("normal source operation");if(degreeCurrent>=0){if(degreeCurrent+shift>P)throw std::runtime_error("B(hJ-HC) degree bound");auto rep=ops.rep[31-a];BitOps::add(beta[basis],PW,shift,current[rep.c],PW,0,degreeCurrent+1,rep.rot,rep.neg);activeNormalOperations++;}normalOperations++;}
  if((index+1)%250==0||index+1==ns+nt)std::cout<<"{\"phase\":\"restore-H0-source-prebasis-compensation\",\"normalSources\":"<<index+1<<",\"operations\":"<<normalOperations<<",\"activeOperations\":"<<activeNormalOperations<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 }
 if(normal.get()!=EOF||normalOperations!=25305683)throw std::runtime_error("normal trace not complete");

 // Add J_v=(s-2)(J_r-c1*J_beta1-c2*J_beta2) to the already accumulated -H*C.
 auto restoreRhsTrace=[&](std::istream &in,int count,bool isFirst){
  in.read(magic,8);if(std::string(magic,8)!="R150NR31"||ol_u32(in)!=count)throw std::runtime_error("actual complete original RHS trace");
  uint64_t operations=0,selectedOperations=0;
  for(int index=0;index<count;index++){
   int r=ol_u32(in),target=ol_u16(in),steps=ol_u32(in);if(r)throw std::runtime_error("RHS trace has an unexpected raw source");
   bool selected=true;
   if(isFirst&&target!=index+2)throw std::runtime_error("original nine residual trace labels");
   if(!isFirst&&target!=2275+index)throw std::runtime_error("actual two original Bockstein trace labels");
   Triple current;
   if(selected){current[0].resize(5*PW);
    for(int j=0;j<nt;j++){
     int a=isFirst?(j==index?1:0):(index==0?31-c1[j]:31-c2[j]);a%=31;
     BitOps::set(current[0],PW,j,(31-2*a%31)%31);BitOps::set(current[0],PW,32+j,a);
    }
    BitOps::refresh(current,PW,0);
   }
   for(int k=0;k<steps;k++){
    int basis=ol_u16(in)-1,shift=in.get(),a=in.get();
    if(basis<0||basis>=nb||shift<0||shift+1>P||a<1||a>30)throw std::runtime_error("original RHS trace coefficient or bound");
    if(selected){auto rep=ops.rep[a];BitOps::add(beta[basis],PW,shift,current[rep.c],PW,0,2,rep.rot,rep.neg);selectedOperations++;}operations++;
   }
  }
  if(in.get()!=EOF)throw std::runtime_error("trailing original RHS trace");
  std::cout<<"{\"phase\":\"restore-combined-original-RHS-prebasis\",\"firstResidualTrace\":"<<(isFirst?"true":"false")<<",\"operations\":"<<operations<<",\"selectedOperations\":"<<selectedOperations<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
  return std::make_pair(operations,selectedOperations);
 };
 auto firstOperations=restoreRhsTrace(firstTrace,9,true),betaOperations=restoreRhsTrace(betaTrace,2,false);
 backward.read(magic,8);if(std::string(magic,8)!="R150RJ31"||ol_u32(backward)!=nb)throw std::runtime_error("backward constant prebasis trace");std::vector<OLBack> back(nb);std::vector<bool> backSeen(nb);
 for(auto &record:back){record.basis=ol_u16(backward)-1;int steps=ol_u32(backward);if(record.basis<0||record.basis>=nb||backSeen[record.basis])throw std::runtime_error("backward prebasis row identity");backSeen[record.basis]=true;record.steps.resize(steps);for(auto &step:record.steps){step.basis=ol_u16(backward);step.coefficient=backward.get();if(step.basis<1||step.basis>nb||step.basis==record.basis+1||step.coefficient<1||step.coefficient>30)throw std::runtime_error("backward operation");}}
 if(backward.get()!=EOF)throw std::runtime_error("trailing backward trace");uint64_t backwardOperations=0,forwardOperations=0;
 for(auto it=back.rbegin();it!=back.rend();it++){int d=actualDegree(beta[it->basis]);Triple current;if(d>=0){current[0]=beta[it->basis];BitOps::refresh(current,PW,0);}for(auto step:it->steps){if(d>=0){auto rep=ops.rep[31-step.coefficient];BitOps::add(beta[step.basis-1],PW,0,current[rep.c],PW,0,d+1,rep.rot,rep.neg);}backwardOperations++;}}
 forward.read(magic,8);if(std::string(magic,8)!="R150PB31"||ol_u32(forward)!=nb)throw std::runtime_error("forward original prebasis trace");std::vector<OLForward> front(nb);
 for(int index=0;index<nb;index++){auto &record=front[index];record.raw=ol_u32(forward);record.scale=forward.get();int steps=ol_u32(forward);if(record.raw!=pre[index].raw||record.scale<1||record.scale>30)throw std::runtime_error("forward raw source or scale");record.steps.resize(steps);for(auto &step:record.steps){step.basis=ol_u16(forward);step.coefficient=forward.get();if(step.basis<1||step.basis>index||step.coefficient<1||step.coefficient>30)throw std::runtime_error("forward dependency is not an earlier basis row");}}
 if(forward.get()!=EOF)throw std::runtime_error("trailing forward trace");
 for(int index=nb-1;index>=0;index--){auto &record=front[index];int d=actualDegree(beta[index]);Triple current;if(d>=0){current[0]=beta[index];ops.multiple(current[0],PW,0,record.scale);BitOps::refresh(current,PW,0);BitOps::add(raw[record.raw-1],PW,0,current[0],PW,0,d+1,0,0);}for(auto step:record.steps){if(d>=0){auto rep=ops.rep[31-step.coefficient];BitOps::add(beta[step.basis-1],PW,0,current[rep.c],PW,0,d+1,rep.rot,rep.neg);}forwardOperations++;}}
 if(backwardOperations!=1010703||forwardOperations!=782976)throw std::runtime_error("constant prebasis trace count");

 for(const auto &S:pre){if(occupied[S.raw-1])throw std::runtime_error("actual prebasis and source overlap");occupied[S.raw-1]=true;}
 if(std::count(occupied.begin(),occupied.end(),true)!=5528)throw std::runtime_error("complete original selected source set");
 auto get64=[&](std::istream &in){uint64_t a=0;for(int k=0;k<8;k++){int c=in.get();if(c<0)throw std::runtime_error("truncated original multiplier");a|=uint64_t(c)<<(8*k);}return a;};
 initial.read(magic,8);if(std::string(magic,8)!="R150P031"||ol_u32(initial)!=nraw||ol_u32(initial)!=nt||ol_u32(initial)!=85||ol_u32(initial)!=217374||ol_u32(initial)!=hd)throw std::runtime_error("actual original first source header");
 for(int a:h0)if(ol_u16(initial)!=a)throw std::runtime_error("same original integer h0 in first source");
 kernels.read(magic,8);if(std::string(magic,8)!="R150KK31"||ol_u32(kernels)!=31||ol_u32(kernels)!=nraw||ol_u32(kernels)!=2||ol_u32(kernels)!=85)throw std::runtime_error("selected actual original cost85 kernel source header");
 for(int i=0;i<2;i++){
  int row=ol_u32(kernels),head=ol_u16(kernels),cost=ol_u16(kernels),source=ol_u32(kernels),r=ol_u32(kernels);
  if(row<1||row>2195||head<1035||head>3229||cost<80||cost>85||source<1||source>2195||r<1||r>nraw)throw std::runtime_error("selected actual original cost85 kernel label");
  if(i==0&&std::array<int,5>{row,head,cost,source,r}!=std::array<int,5>{2192,2275,85,1241,3485})throw std::runtime_error("first genuine original cost85 kernel");
  if(i==1&&std::array<int,5>{row,head,cost,source,r}!=std::array<int,5>{2193,2276,85,1242,3497})throw std::runtime_error("second genuine original cost85 kernel");
 }
 auto inverse961=[](int a){for(int b=1;b<961;b++)if(a*b%961==1)return b;throw std::runtime_error("missing original mod961 unit");};
 std::array<int,17> toOriginal{},originalScale{};int invD=inverse961(D2);
 for(int e=0;e<17;e++){toOriginal[e]=D2*inverse961(contents2[e])%961;originalScale[e]=contents2[e]*invD%961;if(toOriginal[e]*originalScale[e]%961!=1)throw std::runtime_error("original row unit transport modulo961");}
 std::vector<int> H0(26);for(int d=0;d<=24;d++){H0[d]=(H0[d]+2*(961-h0[d]))%961;H0[d+1]=(H0[d+1]+h0[d])%961;}
 if(H0.back()!=3125%961)throw std::runtime_error("exact fixed-root degree25 multiplier");
 std::vector<uint64_t> keys(nc);std::vector<int> widths(nc),offset(nc);int total=0;
 for(int d=5;d>=1;d--)for(auto key:mon[d]){int c=component.at(key);keys[c]=key;widths[c]=productDegree+1-10*(d-1);offset[c]=total;total+=widths[c];}
 std::vector<uint32_t> product(size_t(total)*nt);
 auto binomial=[](int n,int k){int a=1;for(int j=1;j<=k;j++)a=a*(n-j+1)/j;return a;};
 for(int target=0;target<nt;target++){
  int j=target+2;
  for(int a=0;a<=j;a++)for(int b=a;b<=j;b++){
   int exponent=2*j-a-b,c=component.at(variable[a]+variable[b]);int coefficient=binomial(j,a)*binomial(j,b)*(a==b?1:2)*(exponent%2?-1:1);coefficient=(coefficient%961+961)%961;
   for(int k=0;k<=25;k++){if(exponent+k>=widths[c])throw std::runtime_error("original H0 target outside proved bound");int value=coefficient*H0[k]%961;product[size_t(offset[c]+exponent+k)*nt+target]+=(961-value)%961;}
  }
 }
 std::string prefix=argv[11];
 std::ofstream zout(prefix+"-original-correction-mod31.bin",std::ios::binary),pout(prefix+"-primitive-source-mod961.bin",std::ios::binary),oout(prefix+"-original-seventeen-source-mod961.bin",std::ios::binary),meta(prefix+"-original-seventeen-mod961.json");
 if(!zout||!pout||!oout||!meta)throw std::runtime_error("actual original H0 output open");
 zout.write("R150Z031",8);for(int a:{31,nraw,nt,productDegree})u32(zout,a);
 auto writeHeader=[&](std::ostream &o,const char *tag){o.write(tag,8);for(int a:{31,961,nraw,nt,productDegree,25})u32(o,a);for(int a:H0)u16(o,a);u16(o,D2);for(int a:contents2)u16(o,a);};
 writeHeader(pout,"R150P961");writeHeader(oout,"R150O961");
 uint64_t zcount=0,coefficientCount=0,integerProducts=0;int zmaximum=-1,zmaxCost=-1,maximum=-1,maxCost=-1,nonzeroRows=0;
 std::array<int,nt> targetCosts{},correctionCosts{};targetCosts.fill(-1);correctionCosts.fill(-1);
 for(int r=0;r<nraw;r++){
  int equation=r%17;uint64_t multiplier=multipliers[r/17];int delta=10*(degree(multiplier)+1)+(equation<11?0:5);
  auto checkRaw=[&](std::istream &in){if(ol_u32(in)!=r+1||in.get()!=equation||get64(in)!=multiplier||ol_u16(in)!=delta)throw std::runtime_error("actual original6188 row mapping");};
  checkRaw(initial);checkRaw(kernels);
  std::vector<uint16_t> base(size_t(P+1)*nt),packed(size_t(P+1)*nt),primitive(size_t(P+1)*nt);
  for(int j=0;j<nt;j++){
   int len=ol_u16(initial);if(len>86-delta)throw std::runtime_error("actual initial source budget85");int last=0;
   for(int d=0;d<len;d++){last=initial.get();if(last<0||last>30)throw std::runtime_error("actual initial source canonical digit");base[size_t(d)*nt+j]=last;}
   if(len&&!last)throw std::runtime_error("initial source trailing zero");
  }
  for(int i=0;i<2;i++){
   int len=ol_u16(kernels);if(len>86-delta)throw std::runtime_error("actual old kernel cost85");
   int last=0;
   for(int d=0;d<len;d++){
    last=kernels.get();if(last<0||last>30)throw std::runtime_error("actual kernel canonical digit");
    for(int j=0;j<nt;j++){int c=i==0?c1[j]:c2[j];auto &value=base[size_t(d)*nt+j];value=(value+c*last)%961;}
   }
   if(len&&!last)throw std::runtime_error("original kernel trailing zero");
  }
  int dmax=-1,zd=actualDegree(raw[r]);if(zd>=0&&(!occupied[r]||zd+delta>productDegree))throw std::runtime_error("restored correction source cost");
  for(int d=0;d<=P;d++)for(int j=0;j<nt;j++){
   int z=BitOps::get(raw[r],PW,d*32+j);if(z){zcount++;zmaximum=std::max(zmaximum,d);zmaxCost=std::max(zmaxCost,d+delta);correctionCosts[j]=std::max(correctionCosts[j],d+delta);}
   int current=(d?base[size_t(d-1)*nt+j]:0)-2*base[size_t(d)*nt+j]+31*z;current=(current%961+961)%961;
   primitive[size_t(d)*nt+j]=current;int original=current*toOriginal[equation]%961;
   if(original*originalScale[equation]%961!=current)throw std::runtime_error("coefficientwise original row transport");packed[size_t(d)*nt+j]=original;
   if(current){if(!occupied[r]||d+delta>productDegree)throw std::runtime_error("full original H0 source cost");dmax=std::max(dmax,d);coefficientCount++;targetCosts[j]=std::max(targetCosts[j],d+delta);}
  }
  if(dmax>=0){nonzeroRows++;maximum=std::max(maximum,dmax);maxCost=std::max(maxCost,dmax+delta);}
  auto rowHeader=[&](std::ostream &o){u32(o,r+1);o.put(char(equation));ol_u64(o,multiplier);u16(o,delta);};rowHeader(zout);rowHeader(pout);rowHeader(oout);
  for(int j=0;j<nt;j++){
   int dz=zd;while(dz>=0&&!BitOps::get(raw[r],PW,dz*32+j))dz--;u16(zout,dz+1);for(int d=0;d<=dz;d++)zout.put(char(BitOps::get(raw[r],PW,d*32+j)));
   int d=dmax;while(d>=0&&!primitive[size_t(d)*nt+j])d--;u16(pout,d+1);u16(oout,d+1);
   for(int k=0;k<=d;k++){u16(pout,primitive[size_t(k)*nt+j]);u16(oout,packed[size_t(k)*nt+j]);}
  }
  if(dmax>=0){
   auto addTerm=[&](uint64_t monomial,int exponent,int a){a=a*originalScale[equation]%961;if(!a)return;int c=component.at(multiplier+monomial);if(dmax+exponent>=widths[c])throw std::runtime_error("actual original integer product exceeds weighted budget");
    for(int k=0;k<=dmax;k++){uint32_t *destination=product.data()+size_t(offset[c]+k+exponent)*nt;const uint16_t *value=packed.data()+size_t(k)*nt;
     for(int j=0;j<nt;j++){uint32_t next=destination[j]+uint32_t(a)*value[j];destination[j]=next>=(uint32_t(1)<<30)?next%961:next;}}
    integerProducts++;
   };
   if(equation<11){for(int v=0;v<11;v++)for(int k=0;k<=10;k++)addTerm(variable[v],k,L2[equation][v][k]);for(int k=0;k<66;k++){auto [a,b]=quadratic[k];addTerm(variable[a]+variable[b],0,Q2[equation][k]);}}
   else for(int k=0;k<66;k++){auto [a,b]=quadratic[k];for(int e=0;e<=5;e++)addTerm(variable[a]+variable[b],e,G2[equation-11][k][e]);}
  }
  if((r+1)%1000==0||r+1==nraw)std::cout<<"{\"phase\":\"full-original-H0-integer-mod961-product\",\"originalRows\":"<<r+1<<",\"maximumCoefficientDegree\":"<<maximum<<",\"maximumSourceCost\":"<<maxCost<<",\"integerMonomialProducts\":"<<integerProducts<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 }
 if(initial.get()!=EOF||kernels.get()!=EOF)throw std::runtime_error("trailing actual original source data");
 uint64_t nonzero=0;for(auto a:product)nonzero+=a%961!=0;if(nonzero)throw std::runtime_error("FULL ORIGINAL H0 identity modulo961 failed: "+std::to_string(nonzero)+" coefficients");
 auto writeArray=[&](std::ostream &o,const auto &a){o<<"[";for(int j=0;j<nt;j++){if(j)o<<",";o<<a[j];}o<<"]";};
 meta<<"{\"format\":\"r150-h25-full-original-seventeen-mod961-v1\",\"status\":\"completed\",\"prime\":31,\"modulus\":961,\"originalEquations\":17,\"originalRawRows\":6188,\"originalComponents\":4367,\"targetMultiplier\":\"H0=(s-2)*h0\",\"targetMultiplierDegree\":25,\"provedSourceCostBound\":182,\"actualNormalSourceCost\":"<<normalSourceMaximumCost<<",\"actualCorrectionSourceCost\":"<<zmaxCost<<",\"actualFullSourceCost\":"<<maxCost<<",\"maximumCorrectionCoefficientDegree\":"<<zmaximum<<",\"maximumFullCoefficientDegree\":"<<maximum<<",\"fullOriginalSeventeenEquationIdentityMod961\":true,\"fullOriginalMacaulayIdentityMod961\":true,\"originalRowScaleTransportVerified\":true,\"allWeightedBoundsVerified\":true,\"characteristicZeroIdentityAsserted\":false,\"integerOutputCoordinatesPerTarget\":"<<total<<",\"nonzeroCorrectionCoefficients\":"<<zcount<<",\"nonzeroFullCoefficients\":"<<coefficientCount<<",\"nonzeroFullRawRows\":"<<nonzeroRows<<",\"normalSourceOperations\":"<<normalOperations<<",\"firstResidualTraceOperations\":"<<firstOperations.first<<",\"selectedOriginalBetaTraceOperations\":"<<betaOperations.first<<",\"selectedBetaTraceOperations\":"<<betaOperations.second<<",\"backwardPrebasisOperations\":"<<backwardOperations<<",\"forwardPrebasisOperations\":"<<forwardOperations<<",\"integerMonomialProducts\":"<<integerProducts<<",\"targetSourceCosts\":";writeArray(meta,targetCosts);meta<<",\"correctionSourceCosts\":";writeArray(meta,correctionCosts);
 meta<<",\"sourceIdentity\":\"C is transported by the actual original traces Jv-HC and the complete original prebasis DAG. The final primitive source is (s-2)(x0+c1*kappa2275+c2*kappa2276)+31*z, with the existing canonical original kernel digits lifted as integers before arithmetic modulo961. Original rational-equation coefficients are explicitly D/content_i times primitive coefficients modulo961. All6188 original rows and every original output coefficient are multiplied back modulo961. No characteristic-zero claim is made.\",\"elapsedSeconds\":"<<elapsed()<<"}\n";
 zout.close();pout.close();oout.close();meta.close();if(!zout||!pout||!oout||!meta)throw std::runtime_error("complete original H0 output failure");
 std::cout<<"{\"status\":\"h25-full-original-seventeen-mod961-complete\",\"prime\":31,\"modulus\":961,\"fullOriginalSeventeenEquationIdentityMod961\":true,\"fullOriginalMacaulayIdentityMod961\":true,\"originalRowScaleTransportVerified\":true,\"allWeightedBoundsVerified\":true,\"actualNormalSourceCost\":"<<normalSourceMaximumCost<<",\"actualCorrectionSourceCost\":"<<zmaxCost<<",\"actualFullSourceCost\":"<<maxCost<<",\"maximumFullCoefficientDegree\":"<<maximum<<",\"characteristicZeroIdentityAsserted\":false,\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 return 0;
}catch(const std::exception &e){std::cerr<<"H25_ORIGINAL_SEVENTEEN_MOD961_FAILED "<<e.what()<<"\n";return 1;}}
