// Complete original critical first coefficient-127 Bockstein over extension jets.
// Author: Astra-ISP-789f / normal_annihilator.
// AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
// Reuse only binary/source-DAG readers from the already paid scalar consumer.
#define main paid_root63_program_not_called
#include "2026-11-16-r150-original127-root63-source-bockstein-native-789f.cpp"
#undef main
#include <numeric>
#include <cstring>
struct GConfig{
 uint32_t d=0,r=0,n=0,L=0,T=0;
 std::vector<uint32_t>h;
 std::vector<uint8_t>component;
};
static GConfig GC;
static void greceipt(const std::string&p,const std::string&fields){
 std::ofstream o(p+".tmp");o<<"{\"format\":\"r150-original127-generalized-source-bockstein-native-v1\",\"binding\":"<<quote(BIND)<<",\"elapsedSeconds\":"<<secs()<<","<<fields<<"}\n";
 o.close();need(bool(o),"generalized receipt flush");fs::rename(p+".tmp",p);
}
template<class T> static void gstep(const T*x,T*y,uint32_t mod,uint32_t channels){
 for(uint32_t v=0;v<channels;v++)for(uint32_t k=0;k<GC.r;k++){
  const size_t off=size_t(v)*GC.L+k*GC.d;int64_t last=x[off+GC.d-1];
  for(uint32_t e=0;e<GC.d;e++){
   int64_t z=(e?int64_t(x[off+e-1]):0)-int64_t(GC.h[e])*last+(k?int64_t(x[off-GC.d+e]):0);
   z%=int64_t(mod);if(z<0)z+=mod;y[off+e]=T(z);
  }
 }
}
template<class T> static std::vector<T> gshifts(const T*x,uint32_t mod,uint32_t channels){
 const size_t size=size_t(channels)*GC.L;std::vector<T>a(46*size);std::copy_n(x,size,a.data());
 for(size_t k=1;k<46;k++)gstep(a.data()+(k-1)*size,a.data()+k*size,mod,channels);return a;
}
static void gsub(uint8_t*x,const uint8_t*y,uint32_t c,size_t n,uint64_t&checks){
 need(c>0&&c<P,"actual field source multiplier");
 for(size_t j=0;j<n;j++){
  uint32_t z=(uint32_t(x[j])+P-c*uint32_t(y[j])%P)%P;
  uint32_t zz=(P*uint32_t(x[j])+M-(c*P*uint32_t(y[j]))%M)%M;
  need(zz==P*z,"every divided integer coefficient recurrence");x[j]=uint8_t(z);checks++;
 }
}
static void gread_config(const std::string&p){
 Reader r(p);r.magic("R15GX127");r.bind(BIND);r.bind(NFB);r.bind(GBB);
 need(r.le(4)==P,"exact generalized prime");GC.d=r.le(4);GC.r=r.le(4);GC.n=r.le(4);
 need(GC.d>=2&&GC.d<=4&&GC.r>=1&&GC.r<=5&&GC.n>=1&&GC.n<=8,"actual bounded extension and complete detector count");
 GC.L=GC.d*GC.r;GC.T=GC.n*GC.L;GC.h.resize(GC.d+1);
 for(auto&x:GC.h){x=r.byte();need(x<P,"canonical irreducible relation");}
 need(GC.h.back()==1,"monic extension relation");GC.component.resize(size_t(Q)*GC.T);r.read(GC.component.data(),GC.component.size());
 need(std::all_of(GC.component.begin(),GC.component.end(),[](auto x){return x<P;}),"all original component jet coefficients canonical");
 r.magic("ENDGX127");r.eof();
 uint64_t verified=0;
 for(uint32_t j=0;j<GC.L;j++){
  std::vector<uint8_t>x(GC.L);std::vector<uint16_t>y(GC.L);x[j]=1;y[j]=P;
  auto xp=gshifts(x.data(),P,1);auto ym=gshifts(y.data(),M,1);
  for(size_t z=0;z<xp.size();z++){need(ym[z]==P*xp[z],"unramified shift commutes with division by127 at every basis coordinate");verified++;}
 }
 need(verified==uint64_t(46)*GC.L*GC.L,"complete ring shift identities");
}
static void gwrite_dims(std::ostream&o){for(uint32_t v:{P,GC.d,GC.r,GC.n})le(o,v,4);}
static void gcheck_dims(Reader&r){need(r.le(4)==P&&r.le(4)==GC.d&&r.le(4)==GC.r&&r.le(4)==GC.n,"exact complete generalized geometry");}
struct GEll{std::vector<uint64_t>keys;std::vector<uint8_t>values;std::unordered_map<uint64_t,uint32_t>index;};
static GEll gread_ell(const std::string&p){
 Reader r(p);r.magic("R15GL127");r.bind(BIND);gcheck_dims(r);need(r.le(4)==4367,"all original outputs in generalized functional");
 GEll e;e.keys.resize(4367);e.values.resize(size_t(4367)*GC.T);uint32_t i=0;
 for(int d=1;d<=5;d++)for(uint64_t k:mons(d)){
  need(r.le(8)==k,"same original output monomial order");e.keys[i]=k;need(e.index.emplace(k,i).second,"distinct original output");
  r.read(e.values.data()+size_t(i)*GC.T,GC.T);i++;
 }
 need(i==4367&&std::all_of(e.values.begin(),e.values.end(),[](auto x){return x<P;}),"whole original canonical functional");
 r.magic("ENDGL127");r.eof();return e;
}
static int gtransport(const std::vector<std::string>&a){
 need(a.size()==3,"transport: original prebasis, component dictionary, output");
 std::array<std::vector<uint64_t>,6>mon;std::array<std::unordered_map<uint64_t,int>,6>idx;
 std::array<std::vector<uint8_t>,6>ell,seen;
 for(int d=1;d<=5;d++){mon[d]=mons(d);ell[d].resize(mon[d].size()*GC.T);seen[d].resize(mon[d].size());for(int j=0;j<int(mon[d].size());j++)idx[d][mon[d][j]]=j;}
 {Reader r(a[1]);r.magic("R15CD127");r.bind(NFB);need(r.le(4)==Q,"complete original component dictionary");
  for(int c=0;c<int(Q);c++){uint64_t k=r.le(8);int d=degree(k);need(d>=1&&d<=5&&idx[d].count(k),"actual component monomial");int j=idx[d].at(k);
   need(!seen[d][j],"distinct component");seen[d][j]=1;std::copy_n(GC.component.data()+size_t(c)*GC.T,GC.T,ell[d].data()+size_t(j)*GC.T);
  }r.eof();
 }
 struct R{int c,id;std::vector<uint32_t>w;};std::vector<bool>ids(3334,false);
 Reader input(a[0]);input.magic("R15PC127");input.bind(NFB);need(input.le(4)==P&&input.le(4)==3333,"whole original prebasis");
 need(input.le(8)==801468&&input.le(8)==1041956&&input.le(8)==243,"actual prebasis counts");
 uint64_t same=0,products=0;int total=0;
 for(int d=2;d<=5;d++){
  size_t hw=(mon[d].size()+31)/32,lw=(mon[d-1].size()+31)/32,nw=hw+11*lw;
  need(input.le(4)==uint64_t(d)&&input.le(4)==nw,"same original degree geometry");int count=input.le(4);std::vector<R>rows;std::vector<int>piv;int prev=-1;
  for(int j=0;j<count;j++){R x;x.c=input.le(4);x.id=input.le(4);need(x.c>prev&&x.c<int(mon[d].size())&&x.id>=1&&x.id<=3333&&!ids[x.id]&&!seen[d][x.c],"same original prebasis source labels");
   prev=x.c;ids[x.id]=true;seen[d][x.c]=1;x.w=words(input,7*nw);piv.push_back(x.c);rows.push_back(std::move(x));total++;
  }
  size_t nl=mon[d-1].size();std::vector<uint8_t>low(11*nl*GC.T);
  for(size_t c=0;c<nl;c++){
   std::copy_n(ell[d-1].data()+c*GC.T,GC.T,low.data()+c*GC.T);
   for(int k=1;k<=10;k++)gstep(low.data()+((k-1)*nl+c)*GC.T,low.data()+(k*nl+c)*GC.T,P,GC.n);
  }
  auto sums=[&](const R&x,bool include_pivot){
   std::vector<uint64_t>sum(GC.T);
   for(int c=0;c<int(mon[d].size());c++)if(include_pivot||c!=x.c){
    uint32_t v=field_get(x.w,nw,c);if(v)for(size_t e=0;e<GC.T;e++)sum[e]+=uint64_t(v)*ell[d][size_t(c)*GC.T+e];
   }
   for(int k=0;k<=10;k++)for(size_t c=0;c<nl;c++){
    uint32_t v=field_get(x.w,nw,(hw+k*lw)*32+c);if(v)for(size_t e=0;e<GC.T;e++)sum[e]+=uint64_t(v)*low[(k*nl+c)*GC.T+e];
   }return sum;
  };
  for(const auto&x:rows){
   for(int c:piv){need(field_get(x.w,nw,c)==uint32_t(c==x.c),"all same-degree original pivot identities");same++;}
   auto sum=sums(x,false);for(size_t e=0;e<GC.T;e++)ell[d][size_t(x.c)*GC.T+e]=uint8_t((P-sum[e]%P)%P);
  }
  for(const auto&x:rows){auto sum=sums(x,true);for(auto z:sum){need(z%P==0,"all original prebasis local jet products");products++;}}
  if(out_of_time())throw std::runtime_error("generalized transpose budget before complete phase");
 }
 input.magic("ENDPC127");input.eof();need(total==3333&&products==uint64_t(3333)*GC.T,"all original prebasis rows and detector coefficients transported");
 std::ofstream o(a[2]+".tmp",std::ios::binary);head(o,"R15GL127",BIND);gwrite_dims(o);le(o,4367,4);int count=0;
 for(int d=1;d<=5;d++)for(size_t j=0;j<mon[d].size();j++){need(seen[d][j],"whole original output coverage");le(o,mon[d][j],8);o.write(reinterpret_cast<const char*>(ell[d].data()+j*GC.T),GC.T);count++;}
 need(count==4367,"all original output jets retained");finish(o,"ENDGL127",a[2]+".tmp",a[2]);
 greceipt(a[2]+".json","\"status\":\"completed\",\"phase\":\"whole-original-output-generalized-transport\",\"sameDegreeUnitProducts\":"+std::to_string(same)+",\"originalPrebasisJetProducts\":"+std::to_string(products)+",\"all4367OriginalOutputsRetained\":true");return 0;
}
struct GTerm{uint64_t moment;std::vector<uint16_t>coefficient;};
using GPrimitive=std::array<std::vector<GTerm>,17>;
static GPrimitive gprimitive(const std::string&p){
 Reader r(p);r.magic("R15GI127");r.bind(BIND);need(r.le(4)==M&&r.le(4)==17&&r.le(4)==77,"original integer polynomial model modulus and dimensions");
 std::vector<uint64_t>mon;for(int j=0;j<11;j++)mon.push_back(uint64_t(1)<<(3*j));
 for(int j=0;j<11;j++)for(int k=j;k<11;k++)mon.push_back((uint64_t(1)<<(3*j))+(uint64_t(1)<<(3*k)));
 GPrimitive out;
 for(int i=0;i<17;i++)for(int j=0;j<77;j++){
  uint32_t len=r.byte();need(len<=11,"original parameter degree");GTerm t;t.moment=mon[j];bool nonzero=false;
  for(uint32_t k=0;k<len;k++){uint16_t c=r.le(2);need(c<M,"canonical original integer coefficient");t.coefficient.push_back(c);nonzero|=c!=0;}
  if(nonzero)out[i].push_back(std::move(t));
 }
 r.magic("ENDGI127");r.eof();return out;
}
static int gleaves(const std::vector<std::string>&a){
 need(a.size()==3,"leaves: integer primitive model, original functional, output");
 auto primitive=gprimitive(a[0]);auto ell=gread_ell(a[1]);
 std::vector<uint16_t>lift(size_t(4367)*11*GC.T);
 for(size_t row=0;row<4367;row++){
  auto*base=lift.data()+row*11*GC.T;for(size_t j=0;j<GC.T;j++)base[j]=ell.values[row*GC.T+j];
  for(int k=1;k<=10;k++)gstep(base+(k-1)*GC.T,base+k*GC.T,M,GC.n);
 }
 std::ofstream out(a[2]+".tmp",std::ios::binary);head(out,"R15GS127",BIND);gwrite_dims(out);le(out,6188,4);
 uint64_t checks=0,terms=0;int raw=0;uint32_t nonzero=0;
 for(int degree=0;degree<=3;degree++)for(uint64_t multiplier:mons(degree))for(int eq=0;eq<17;eq++){
  std::vector<uint64_t>sum(GC.T);raw++;
  for(const auto&t:primitive[eq]){
   auto it=ell.index.find(multiplier+t.moment);need(it!=ell.index.end(),"every original source output is present");
   for(size_t k=0;k<t.coefficient.size();k++)if(t.coefficient[k]){
    auto*point=lift.data()+(size_t(it->second)*11+k)*GC.T;
    for(size_t j=0;j<GC.T;j++)sum[j]+=uint64_t(t.coefficient[k])*point[j];terms++;
   }
  }
  for(size_t j=0;j<GC.T;j++){uint32_t z=sum[j]%M;need(z%P==0,"all original6188 generalized scalar coefficients exactly divide127");
   le(out,z,2);out.put(char(z/P));checks++;nonzero+=z!=0;
  }
  if((raw%256)==0&&out_of_time())throw std::runtime_error("original generalized leaf budget before complete phase");
 }
 need(raw==6188&&checks==uint64_t(6188)*GC.T,"whole original source leaf coverage");finish(out,"ENDGS127",a[2]+".tmp",a[2]);
 greceipt(a[2]+".json","\"status\":\"completed\",\"phase\":\"original-integer-generalized-source-leaves\",\"all6188OriginalScalarColumnsDivisible\":true,\"originalDivisibleCoefficientCount\":"+std::to_string(checks)+",\"originalPolynomialTermProducts\":"+std::to_string(terms)+",\"nonzeroDividedCoefficients\":"+std::to_string(nonzero));return 0;
}
struct GNF{std::vector<uint8_t>values;std::vector<uint32_t>raw;};
static GNF gread_nf(const std::string&p){
 Reader r(p);r.magic("R15GN127");r.bind(BIND);gcheck_dims(r);need(r.le(4)==NS,"all original NF complement");
 GNF x;x.values.resize(size_t(NS+1)*GC.T);x.raw.resize(NS+1);
 for(uint32_t j=1;j<=NS;j++){x.raw[j]=r.le(4);need(x.raw[j]>=1&&x.raw[j]<=6188,"original NF raw label");r.read(x.values.data()+size_t(j)*GC.T,GC.T);}
 need(std::all_of(x.values.begin(),x.values.end(),[](auto v){return v<P;}),"canonical whole generalized NF");
 r.magic("ENDGN127");r.eof();return x;
}
static int gnf(const std::vector<std::string>&a){
 need(a.size()==5,"NF: generalized leaves, forward, backward, original reduction, output");
 std::vector<uint8_t>leaf(size_t(6189)*GC.T),pre(size_t(3334)*GC.T);
 {Reader r(a[0]);r.magic("R15GS127");r.bind(BIND);gcheck_dims(r);need(r.le(4)==6188,"all original generalized leaf labels");
  for(int j=1;j<=6188;j++)for(size_t e=0;e<GC.T;e++){uint32_t z=r.le(2),v=r.byte();need(z<M&&v<P&&z==P*v,"whole divided original integer leaf");leaf[size_t(j)*GC.T+e]=v;}
  r.magic("ENDGS127");r.eof();
 }
 std::vector<uint32_t>raw(3334);std::vector<bool>seen(6189,false);uint64_t checks=0,nforward=0,nback=0,nnf=0;
 auto grade=[](uint32_t raw){uint32_t v=(raw-1)/17;return v<1?0:v<12?1:v<78?2:3;};
 {Reader r(a[1]);r.magic("R15PF127");need(r.le(4)==3333,"complete original forward");r.bind(NFB);
  for(uint32_t j=1;j<=3333;j++){uint32_t source=r.le(4),scale=r.byte(),count=r.le(4);need(source>=1&&source<=6188&&!seen[source]&&scale>0&&scale<P&&count<=3333,"original forward source and unit");
   seen[source]=true;raw[j]=source;auto*x=pre.data()+size_t(j)*GC.T;std::copy_n(leaf.data()+size_t(source)*GC.T,GC.T,x);
   for(uint32_t k=0;k<count;k++){uint32_t id=r.le(2),c=r.byte();need(id>=1&&id<j&&grade(raw[id])==grade(source),"original forward same-grade source");
    gsub(x,pre.data()+size_t(id)*GC.T,c,GC.T,checks);nforward++;}
   for(size_t e=0;e<GC.T;e++)x[e]=uint8_t(scale*x[e]%P);
  }r.eof();need(nforward==801468,"all original forward operations");
 }
 {Reader r(a[2]);r.magic("R15PB127");need(r.le(4)==3333,"complete original backward");r.bind(NFB);std::vector<bool>done(3334,false);
  for(int j=0;j<3333;j++){uint32_t id=r.le(2),count=r.le(4);need(id>=1&&id<=3333&&!done[id]&&count<=3333,"original backward source");
   done[id]=true;for(uint32_t k=0;k<count;k++){uint32_t ref=r.le(2),c=r.byte();need(ref>=1&&ref<=3333&&ref!=id&&done[ref]&&grade(raw[ref])==grade(raw[id]),"complete backward same-grade dependency");
    gsub(pre.data()+size_t(id)*GC.T,pre.data()+size_t(ref)*GC.T,c,GC.T,checks);nback++;}
  }r.eof();need(nback==1041956,"all original backward operations");
 }
 std::vector<uint8_t>cache(size_t(3334)*46*GC.T);
 for(int id=1;id<=3333;id++){auto c=gshifts(pre.data()+size_t(id)*GC.T,P,GC.n);std::copy(c.begin(),c.end(),cache.begin()+size_t(id)*46*GC.T);}
 std::ofstream out(a[4]+".tmp",std::ios::binary);head(out,"R15GN127",BIND);gwrite_dims(out);le(out,NS,4);
 {Reader r(a[3]);r.magic("R15NR127");r.bind(NFB);need(r.le(4)==NS+9,"all original NF sources and targets");
  for(uint32_t j=1;j<=NS+9;j++){
   uint32_t source=r.le(4),target=r.le(2),count=r.le(4);std::vector<uint8_t>x(GC.T);
   if(j<=NS){need(source>=1&&source<=6188&&!seen[source]&&target==0,"complete original NF source partition");seen[source]=true;std::copy_n(leaf.data()+size_t(source)*GC.T,GC.T,x.data());}
   else need(source==0&&target==j-NS+1,"all target records retained outside source kernel");
   for(uint32_t k=0;k<count;k++){uint32_t id=r.le(2),e=r.byte(),c=r.byte();need(id>=1&&id<=3333&&e<=45&&c>0&&c<P,"whole original NF recipe");
    if(j<=NS)gsub(x.data(),cache.data()+(size_t(id)*46+e)*GC.T,c,GC.T,checks);nnf++;}
   if(j<=NS){le(out,source,4);out.write(reinterpret_cast<const char*>(x.data()),GC.T);}
   if(out_of_time())throw std::runtime_error("generalized NF budget before complete phase");
  }r.eof();
 }
 need(nnf==29606398&&std::count(seen.begin(),seen.end(),true)==6188,"all original NF operations and source labels");
 finish(out,"ENDGN127",a[4]+".tmp",a[4]);greceipt(a[4]+".json","\"status\":\"completed\",\"phase\":\"complete-original-generalized-NF-values\",\"forwardOperations\":801468,\"backwardOperations\":1041956,\"normalOperations\":29606398,\"all6188OriginalSourcesExactlyOnce\":true,\"integerDividedCoefficientRecurrences\":"+std::to_string(checks));return 0;
}

struct GZero{uint32_t ordinal=0,raw=0,node=0;std::vector<uint8_t>v;};
struct GScan{
 uint64_t generation=0,red=0,offset=81;
 uint32_t inputs=0,insertions=0,swaps=0,finals=0,current=0,last=0,lastFinal=0;bool active=false;
 std::vector<uint8_t>currentValue,pivotValue;
 std::vector<uint32_t>pivot=std::vector<uint32_t>(Q);
 std::vector<GZero>zero;std::vector<Block>blocks={{0,81}};
};
static void gsave_scan(const std::string&dir,GScan&s){
 uint64_t next=s.generation+1;int slot=next%2;std::string path=dir+"/generalized-checkpoint-"+std::to_string(slot)+".bin";
 std::ofstream o(path+".tmp",std::ios::binary);head(o,"R15GT127",BIND);o.write(NFB.data(),64);o.write(GBB.data(),64);gwrite_dims(o);le(o,next,8);
 le(o,s.red,8);le(o,s.offset,8);for(uint32_t x:{s.inputs,s.insertions,s.swaps,s.finals,s.current,s.last,s.lastFinal})le(o,x,4);o.put(char(s.active));
 o.write(reinterpret_cast<const char*>(s.currentValue.data()),GC.T);for(auto x:s.pivot)le(o,x,4);
 o.write(reinterpret_cast<const char*>(s.pivotValue.data()),s.pivotValue.size());le(o,s.zero.size(),4);
 for(const auto&z:s.zero){le(o,z.ordinal,4);le(o,z.raw,4);le(o,z.node,4);o.write(reinterpret_cast<const char*>(z.v.data()),GC.T);}
 le(o,s.blocks.size(),4);for(auto b:s.blocks){le(o,b.reductions,8);le(o,b.offset,8);}
 finish(o,"ENDGT127",path+".tmp",path);
 std::string selector=dir+"/generalized-active.bin";std::ofstream a(selector+".tmp",std::ios::binary);head(a,"R15GVACT",BIND);le(a,next,8);le(a,slot,4);
 finish(a,"ENDGVACT",selector+".tmp",selector);s.generation=next;
}
static GScan gread_scan(const std::string&dir){
 Reader a(dir+"/generalized-active.bin");a.magic("R15GVACT");a.bind(BIND);uint64_t generation=a.le(8);uint32_t slot=a.le(4);
 need(slot==generation%2,"actual generalized checkpoint slot");a.magic("ENDGVACT");a.eof();
 Reader r(dir+"/generalized-checkpoint-"+std::to_string(slot)+".bin");r.magic("R15GT127");r.bind(BIND);r.bind(NFB);r.bind(GBB);gcheck_dims(r);
 GScan s;s.generation=r.le(8);need(s.generation==generation,"exact complete generalized generation");s.red=r.le(8);s.offset=r.le(8);
 s.inputs=r.le(4);s.insertions=r.le(4);s.swaps=r.le(4);s.finals=r.le(4);s.current=r.le(4);s.last=r.le(4);s.lastFinal=r.le(4);s.active=r.byte();
 need(s.red<=PAID_R&&s.inputs<=NS&&s.insertions<=1021&&s.swaps<=PAID_S&&s.finals<=1021&&s.current<=NS+s.red&&s.last<=NS,"whole committed source counters");
 s.currentValue.resize(GC.T);r.read(s.currentValue.data(),GC.T);for(auto&x:s.pivot){x=r.le(4);need(x<=NS+s.red,"saved original pivot node");}
 s.pivotValue.resize(size_t(Q)*GC.T);r.read(s.pivotValue.data(),s.pivotValue.size());
 need(std::all_of(s.currentValue.begin(),s.currentValue.end(),[](auto x){return x<P;})&&std::all_of(s.pivotValue.begin(),s.pivotValue.end(),[](auto x){return x<P;}),"canonical complete saved scalar vectors");
 uint32_t nz=r.le(4);need(nz<=1834,"whole saved zero endpoint count");
 for(uint32_t j=0;j<nz;j++){GZero z;z.ordinal=r.le(4);z.raw=r.le(4);z.node=r.le(4);z.v.resize(GC.T);r.read(z.v.data(),GC.T);
  need(z.ordinal>=1&&z.ordinal<=NS&&z.raw>=1&&z.raw<=6188&&z.node<=NS+s.red&&std::all_of(z.v.begin(),z.v.end(),[](auto x){return x<P;}),"same saved original zero source");s.zero.push_back(std::move(z));}
 uint32_t nb=r.le(4);need(nb>=1&&nb<=PAID_R/65536+2,"bounded complete reverse index");s.blocks.clear();
 for(uint32_t j=0;j<nb;j++){Block b;b.reductions=r.le(8);b.offset=r.le(8);need((j==0&&b.reductions==0&&b.offset==81)||(j&&b.reductions==s.blocks.back().reductions+65536&&b.offset>s.blocks.back().offset),"actual complete reverse block boundaries");s.blocks.push_back(b);}
 r.magic("ENDGT127");r.eof();return s;
}
static std::string gscan_fields(const GScan&s,bool resumed,const char*status){
 size_t nonzero=0;for(const auto&z:s.zero)nonzero+=std::any_of(z.v.begin(),z.v.end(),[](auto x){return x!=0;});
 return "\"status\":"+quote(status)+",\"phase\":\"complete-original-generalized-Z-scan\",\"generation\":"+std::to_string(s.generation)+
 ",\"processedOriginalSources\":"+std::to_string(s.inputs)+",\"GBReductions\":"+std::to_string(s.red)+",\"GBSwaps\":"+std::to_string(s.swaps)+
 ",\"originalGlobalZeroSources\":"+std::to_string(s.zero.size())+",\"nonzeroZeroEndpointsNotDimension\":"+std::to_string(nonzero)+
 ",\"detectorCount\":"+std::to_string(GC.n)+",\"coefficientsPerDetector\":"+std::to_string(GC.L)+
 ",\"integerDividedCoefficientRecurrences\":"+std::to_string(s.red*GC.T)+",\"allSourceRoutesVerified\":true,\"onlyCurrentAndActualPivotsStored\":true,\"resumed\":"+(resumed?"true":"false");
}
static int gscan(const std::vector<std::string>&a){
 need(a.size()==3,"scan: complete NF values, originalGB DAG, out-directory");
 auto nf=gread_nf(a[0]);fs::create_directories(a[2]);bool reused=fs::exists(a[2]+"/generalized-active.bin");
 GScan s;if(reused)s=gread_scan(a[2]);else{s.currentValue.resize(GC.T);s.pivotValue.resize(size_t(Q)*GC.T);}
 for(auto z:s.zero)need(z.raw==nf.raw[z.ordinal],"saved Z source and exact NF labels");
 std::unordered_map<uint32_t,uint32_t>position;position.reserve(2048);std::vector<uint8_t>cache(size_t(Q)*46*GC.T);
 auto refresh=[&](uint32_t c){auto v=gshifts(s.pivotValue.data()+size_t(c)*GC.T,P,GC.n);std::copy(v.begin(),v.end(),cache.begin()+size_t(c)*46*GC.T);};
 for(uint32_t c=0;c<Q;c++)if(s.pivot[c]){need(position.emplace(s.pivot[c],c).second,"distinct actual source pivot nodes");refresh(c);}
 Reader r(a[1]);r.magic("R15GO127");r.bind(GBB);need(r.le(4)==NS&&r.le(4)==Q&&r.byte()==45,"complete original polynomial source DAG");
 need(s.offset<=fs::file_size(a[1]),"actual committed source offset");r.seek(s.offset);double last=secs();
 while(true){
  int event=r.next();if(event<0)break;
  if(event=='I'){
   uint32_t ordinal=r.le(4),raw=r.le(4);need(!s.active&&ordinal==s.inputs+1&&ordinal<=NS&&raw==nf.raw[ordinal]&&s.finals==0,"all original source input identities");
   s.inputs++;s.current=s.last=ordinal;s.active=true;std::copy_n(nf.values.data()+size_t(ordinal)*GC.T,GC.T,s.currentValue.data());
  }else if(event=='B'){
   uint32_t c=r.le(2),node=r.le(4);need(s.active&&c>=1&&c<=Q&&!s.pivot[c-1]&&node==s.current,"actual source basis insertion");c--;
   need(position.emplace(node,c).second,"new original pivot source");s.pivot[c]=node;std::copy(s.currentValue.begin(),s.currentValue.end(),s.pivotValue.begin()+size_t(c)*GC.T);refresh(c);s.insertions++;s.active=false;
  }else if(event=='S'){
   uint32_t c=r.le(2),current=r.le(4),pivot=r.le(4);need(s.active&&c>=1&&c<=Q&&current==s.pivot[c-1]&&pivot==s.current,"actual original source swap");c--;
   need(position.erase(current)==1&&position.emplace(pivot,c).second,"exact complete pivot map update");
   for(size_t j=0;j<GC.T;j++)std::swap(s.currentValue[j],s.pivotValue[size_t(c)*GC.T+j]);
   s.current=current;s.pivot[c]=pivot;refresh(c);s.swaps++;
  }else if(event=='R'){
   uint32_t old=r.le(4),pivot=r.le(4),exponent=r.byte(),c=r.byte();
   auto found=position.find(pivot);need(s.active&&old==s.current&&old<=NS+s.red&&pivot<=NS+s.red&&found!=position.end()&&exponent<=45&&c>0&&c<P&&s.red<PAID_R,"every R reads only the actual current and present pivot");
   uint64_t checks=0;gsub(s.currentValue.data(),cache.data()+(size_t(found->second)*46+exponent)*GC.T,c,GC.T,checks);need(checks==GC.T,"all generalized recurrence coordinates checked");
   s.red++;s.current=NS+s.red;if(s.red%65536==0)s.blocks.push_back({s.red,r.at});
  }else if(event=='Z'){
   uint32_t node=r.le(4);need(s.active&&node==s.current,"complete global polynomial zero source");s.zero.push_back({s.last,nf.raw[s.last],node,s.currentValue});s.active=false;
  }else if(event=='F'){
   uint32_t c=r.le(2),node=r.le(4),scale=r.byte();need(!s.active&&s.inputs==NS&&c>s.lastFinal&&c<=Q&&node==s.pivot[c-1]&&scale>0&&scale<P,"all normalized final original source identities");
   s.finals++;s.lastFinal=c;
  }else throw std::runtime_error("unknown original source DAG event");
  s.offset=r.at;
  if((event!='R'||s.red%65536==0)&&(out_of_time()||secs()-last>=30)){
   gsave_scan(a[2],s);last=secs();if(out_of_time()){greceipt(a[2]+"/generalized-scan-native.json",gscan_fields(s,reused,"budget-checkpoint"));return 75;}
  }
 }
 s.offset=r.at;need(s.inputs==NS&&s.insertions==1021&&s.red==PAID_R&&s.swaps==PAID_S&&s.finals==1021&&s.zero.size()==1834&&!s.active,"complete all2855 source,1021 basis and1834 original polynomial Z identities");
 gsave_scan(a[2],s);
 std::string path=a[2]+"/all-original-Z-generalized-values.bin";std::ofstream out(path+".tmp",std::ios::binary);head(out,"R15GZ127",BIND);gwrite_dims(out);le(out,s.zero.size(),4);
 for(const auto&z:s.zero){le(out,z.ordinal,4);le(out,z.raw,4);le(out,z.node,4);out.write(reinterpret_cast<const char*>(z.v.data()),GC.T);}
 finish(out,"ENDGZ127",path+".tmp",path);
 greceipt(a[2]+"/generalized-scan-native.json",gscan_fields(s,reused,"completed")+",\"all1834OriginalPolynomialZeroSourcesCovered\":true,\"noPointKernelSubstituted\":true");return 0;
}

static std::vector<std::vector<std::pair<uint16_t,uint16_t>>> gtheta_matrix(uint32_t exponent,uint32_t mod){
 std::vector<std::vector<std::pair<uint16_t,uint16_t>>> rows(GC.L);
 for(uint32_t j=0;j<GC.L;j++){
  std::vector<uint16_t>x(GC.L);x[j]=1;auto all=gshifts(x.data(),mod,1);
  for(uint32_t i=0;i<GC.L;i++)if(all[size_t(exponent)*GC.L+i])rows[i].push_back({uint16_t(j),all[size_t(exponent)*GC.L+i]});
 }return rows;
}
static int greverse(const std::vector<std::string>&a){
 need(a.size()==7,"reverse: forward, backward, originalNF, GBDAG, scan-dir, zero-index, output");
 GScan scan=gread_scan(a[4]);need(scan.red==PAID_R&&scan.inputs==NS&&scan.zero.size()==1834&&scan.finals==1021,"complete all-Z scan before any positive reversal");
 size_t zi=std::stoull(a[5]);need(zi<scan.zero.size(),"actual selected source index");const GZero&chosen=scan.zero[zi];
 need(std::any_of(chosen.v.begin(),chosen.v.end(),[](auto x){return x!=0;}),"positive source selected from complete generalized scan");
 uint64_t witnessR=chosen.node>NS?chosen.node-NS:0;
 std::vector<uint16_t>weight((size_t(chosen.node)+1)*GC.L);weight[size_t(chosen.node)*GC.L]=1;
 std::vector<std::vector<std::vector<std::pair<uint16_t,uint16_t>>>> shift(46);
 for(uint32_t e=0;e<=45;e++)shift[e]=gtheta_matrix(e,M);
 Reader dag(a[3]);uint64_t applied=0,parsed=0;std::vector<uint16_t>scaled(GC.L);
 for(size_t bi=scan.blocks.size();bi-->0;){
  Block begin=scan.blocks[bi];if(begin.reductions>=witnessR)continue;
  uint64_t endOffset=bi+1<scan.blocks.size()?scan.blocks[bi+1].offset:scan.offset;std::vector<Red>edges;dag.seek(begin.offset);uint64_t count=begin.reductions;
  while(dag.at<endOffset){
   int event=dag.next();need(event>=0,"complete reverse source block");
   if(event=='I'){dag.le(4);dag.le(4);}else if(event=='B'){dag.le(2);dag.le(4);}else if(event=='S'){dag.le(2);dag.le(4);dag.le(4);}
   else if(event=='R'){Red x;x.old=dag.le(4);x.pivot=dag.le(4);x.exponent=dag.byte();x.c=dag.byte();x.node=NS+(++count);
    need(x.old<x.node&&x.pivot<x.node&&x.exponent<=45&&x.c>0&&x.c<P,"original integer reverse source edge");if(count<=witnessR)edges.push_back(x);parsed++;}
   else if(event=='Z')dag.le(4);else if(event=='F'){dag.le(2);dag.le(4);dag.byte();}else throw std::runtime_error("unknown complete reverse DAG event");
  }
  need(dag.at==endOffset,"complete original reverse block boundary");
  for(size_t k=edges.size();k-->0;){
   const auto&x=edges[k];auto*w=weight.data()+size_t(x.node)*GC.L;
   if(std::any_of(w,w+GC.L,[](auto v){return v!=0;})){
    for(uint32_t i=0;i<GC.L;i++){uint64_t z=0;for(auto [j,c]:shift[x.exponent][i])z+=uint64_t(c)*w[j];scaled[i]=uint16_t(z%M);}
    for(uint32_t i=0;i<GC.L;i++){
     auto&old=weight[size_t(x.old)*GC.L+i];auto&pivot=weight[size_t(x.pivot)*GC.L+i];
     old=addM(old,w[i]);pivot=subM(pivot,uint64_t(x.c)*scaled[i]);w[i]=0;
    }applied++;
   }
  }
  if(out_of_time())throw std::runtime_error("positive reverse budget before completion; full generalized scan checkpoint remains reusable");
 }
 need(std::all_of(weight.begin()+std::min(weight.size(),size_t(NS+1)*GC.L),weight.end(),[](auto v){return v==0;}),"all internal original source nodes reversed");
 std::vector<uint16_t>original(size_t(6189)*GC.L),pre(size_t(3334)*GC.L);
 {Reader nf(a[2]);nf.magic("R15NR127");nf.bind(NFB);need(nf.le(4)==NS+9,"all original NF recipes during reversal");
  for(uint32_t j=1;j<=NS+9;j++){
   uint32_t raw=nf.le(4),target=nf.le(2),count=nf.le(4);
   std::vector<uint16_t>w(GC.L);bool nonzero=false;
   if(j<=NS){need(raw>=1&&raw<=6188&&target==0,"original source NF label");if(size_t(j)*GC.L<weight.size())std::copy_n(weight.data()+size_t(j)*GC.L,GC.L,w.data());
    for(uint32_t i=0;i<GC.L;i++){original[size_t(raw)*GC.L+i]=addM(original[size_t(raw)*GC.L+i],w[i]);nonzero|=w[i]!=0;}}
   else need(raw==0&&target==j-NS+1,"all target recipes retained without treating them as kernel sources");
   std::vector<uint16_t>cache;if(nonzero)cache=gshifts(w.data(),M,1);
   for(uint32_t k=0;k<count;k++){
    uint32_t id=nf.le(2),e=nf.byte(),c=nf.byte();need(id>=1&&id<=3333&&e<=45&&c>0&&c<P,"whole original NF integer edge");
    if(nonzero)for(uint32_t i=0;i<GC.L;i++)pre[size_t(id)*GC.L+i]=subM(pre[size_t(id)*GC.L+i],uint64_t(c)*cache[size_t(e)*GC.L+i]);
   }
   if(out_of_time())throw std::runtime_error("positive NF reversal budget before completion; complete Z scan is retained");
  }nf.eof();
 }
 std::vector<Fwd>forward(3334);std::vector<Back>back;uint64_t fc=0,bc=0;std::vector<bool>seen(6189,false);
 {Reader f(a[0]);f.magic("R15PF127");need(f.le(4)==3333,"all forward original sources");f.bind(NFB);
  for(uint32_t j=1;j<=3333;j++){auto&v=forward[j];v.raw=f.le(4);v.scale=f.byte();uint32_t count=f.le(4);
   need(v.raw>=1&&v.raw<=6188&&!seen[v.raw]&&v.scale>0&&v.scale<P,"original forward normalized source identity");seen[v.raw]=true;
   for(uint32_t k=0;k<count;k++){uint16_t id=f.le(2);uint8_t c=f.byte();need(id>=1&&id<j&&c>0&&c<P,"actual forward original dependency");v.ops.push_back({id,c});fc++;}
  }f.eof();need(fc==801468,"all forward source edges recovered");
 }
 {Reader f(a[1]);f.magic("R15PB127");need(f.le(4)==3333,"all backward sources");f.bind(NFB);std::vector<bool>done(3334,false);
  for(uint32_t j=0;j<3333;j++){Back v;v.id=f.le(2);uint32_t count=f.le(4);need(v.id>=1&&v.id<=3333&&!done[v.id],"original backward source identity");done[v.id]=true;
   for(uint32_t k=0;k<count;k++){uint16_t id=f.le(2);uint8_t c=f.byte();need(id>=1&&id<=3333&&id!=v.id&&done[id]&&c>0&&c<P,"actual backward dependency");v.ops.push_back({id,c});bc++;}
   back.push_back(std::move(v));
  }f.eof();need(bc==1041956,"all backward source edges recovered");
 }
 for(size_t j=back.size();j-->0;){const auto&v=back[j];auto*w=pre.data()+size_t(v.id)*GC.L;
  for(auto [id,c]:v.ops)for(uint32_t i=0;i<GC.L;i++)pre[size_t(id)*GC.L+i]=subM(pre[size_t(id)*GC.L+i],uint64_t(c)*w[i]);}
 for(int j=3333;j>=1;j--){const auto&v=forward[j];std::vector<uint16_t>w(GC.L);
  for(uint32_t i=0;i<GC.L;i++){w[i]=uint16_t(uint64_t(pre[size_t(j)*GC.L+i])*v.scale%M);original[size_t(v.raw)*GC.L+i]=addM(original[size_t(v.raw)*GC.L+i],w[i]);}
  for(auto [id,c]:v.ops)for(uint32_t i=0;i<GC.L;i++)pre[size_t(id)*GC.L+i]=subM(pre[size_t(id)*GC.L+i],uint64_t(c)*w[i]);
  std::fill_n(pre.data()+size_t(j)*GC.L,GC.L,0);
 }
 need(std::all_of(pre.begin(),pre.end(),[](auto v){return v==0;}),"all original prebasis reverse weights exhausted");
 size_t support=0;for(int j=1;j<=6188;j++)support+=std::any_of(original.begin()+size_t(j)*GC.L,original.begin()+size_t(j+1)*GC.L,[](auto v){return v!=0;});
 std::ofstream out(a[6]+".tmp",std::ios::binary);head(out,"R15GY127",BIND);gwrite_dims(out);le(out,6188,4);
 for(uint32_t v:{uint32_t(zi),chosen.node,chosen.ordinal,chosen.raw})le(out,v,4);out.write(reinterpret_cast<const char*>(chosen.v.data()),GC.T);
 for(int j=1;j<=6188;j++)for(uint32_t i=0;i<GC.L;i++)le(out,original[size_t(j)*GC.L+i],2);
 finish(out,"ENDGY127",a[6]+".tmp",a[6]);
 greceipt(a[6]+".json","\"status\":\"completed\",\"phase\":\"positive-original-generalized-source-reversal\",\"zeroIndex\":"+std::to_string(zi)+",\"originalGlobalZeroNode\":"+std::to_string(chosen.node)+
 ",\"originalInputOrdinal\":"+std::to_string(chosen.ordinal)+",\"originalRawSource\":"+std::to_string(chosen.raw)+",\"sourceSupport\":"+std::to_string(support)+
 ",\"parsedOriginalReverseEdges\":"+std::to_string(parsed)+",\"nonzeroReverseEdgeUpdates\":"+std::to_string(applied)+",\"integerModulus\":16129,\"allOriginal4367ProductsStillRequired\":true");return 0;
}
static int gproducts(const std::vector<std::string>&a){
 need(a.size()==5,"products: original integer primitive, full functional, complete original source, leaves, output");
 auto primitive=gprimitive(a[0]);auto ell=gread_ell(a[1]);
 std::vector<uint16_t>source(size_t(6189)*GC.L);std::vector<uint8_t>expected(GC.T);uint32_t zi,node,ordinal,rawSource;
 {Reader r(a[2]);r.magic("R15GY127");r.bind(BIND);gcheck_dims(r);need(r.le(4)==6188,"all original source coordinates");
  zi=r.le(4);node=r.le(4);ordinal=r.le(4);rawSource=r.le(4);r.read(expected.data(),GC.T);
  for(int j=1;j<=6188;j++)for(uint32_t i=0;i<GC.L;i++){auto v=r.le(2);need(v<M,"actual original integer source coefficient");source[size_t(j)*GC.L+i]=v;}
  r.magic("ENDGY127");r.eof();
 }
 std::vector<uint64_t>accum(size_t(4367)*GC.L);uint64_t termProducts=0;int raw=0;
 for(int degree=0;degree<=3;degree++)for(uint64_t multiplier:mons(degree))for(int eq=0;eq<17;eq++){
  raw++;auto*y=source.data()+size_t(raw)*GC.L;if(!std::any_of(y,y+GC.L,[](auto v){return v!=0;}))continue;
  auto cache=gshifts(y,M,1);
  for(const auto&t:primitive[eq]){
   auto it=ell.index.find(multiplier+t.moment);need(it!=ell.index.end(),"complete original source product output");
   for(size_t k=0;k<t.coefficient.size();k++)if(t.coefficient[k]){
    for(uint32_t e=0;e<GC.L;e++)accum[size_t(it->second)*GC.L+e]+=uint64_t(t.coefficient[k])*cache[k*GC.L+e];termProducts++;
   }
  }
  if((raw%256)==0&&out_of_time())throw std::runtime_error("all original generalized product budget before completion");
 }
 need(raw==6188,"all original source product rows used");std::vector<uint8_t>divided(accum.size());
 for(size_t i=0;i<accum.size();i++){auto z=accum[i]%M;need(z%P==0,"all4367 original integer source product coefficients divide127");divided[i]=uint8_t(z/P);}
 std::vector<std::vector<uint32_t>>alpha(2*GC.d-1,std::vector<uint32_t>(GC.d));alpha[0][0]=1;
 for(size_t j=1;j<alpha.size();j++){
  auto&v=alpha[j];auto&w=alpha[j-1];uint32_t last=w.back();
  for(uint32_t e=0;e<GC.d;e++)v[e]=(P+(e?w[e-1]:0)-GC.h[e]*last%P)%P;
 }
 auto multiply_accumulate=[&](std::vector<uint64_t>&sum,const uint8_t*x,const uint8_t*y,size_t offset){
  for(uint32_t a=0;a<GC.r;a++)for(uint32_t b=0;a+b<GC.r;b++)for(uint32_t i=0;i<GC.d;i++)if(x[a*GC.d+i])
   for(uint32_t j=0;j<GC.d;j++)if(y[b*GC.d+j]){
    uint64_t c=uint64_t(x[a*GC.d+i])*y[b*GC.d+j];
    for(uint32_t e=0;e<GC.d;e++)sum[offset+(a+b)*GC.d+e]+=c*alpha[i+j][e];
   }
 };
 std::vector<uint64_t>answer(GC.T);
 for(size_t row=0;row<4367;row++)for(uint32_t v=0;v<GC.n;v++)
  multiply_accumulate(answer,ell.values.data()+row*GC.T+size_t(v)*GC.L,divided.data()+row*GC.L,size_t(v)*GC.L);
 for(size_t e=0;e<GC.T;e++)need(answer[e]%P==expected[e],"all complete generalized detector products on original4367 divided source");
 // An independent all6188 source-coordinate contraction checks the reverse DAG.
 std::vector<uint64_t>answer2(GC.T);
 {Reader r(a[3]);r.magic("R15GS127");r.bind(BIND);gcheck_dims(r);need(r.le(4)==6188,"same original divided leaves");
  std::vector<uint8_t>leaf(GC.T),y(GC.L);
  for(int j=1;j<=6188;j++){
   for(size_t e=0;e<GC.T;e++){auto z=r.le(2);auto v=r.byte();need(z==P*v&&v<P,"exact original integer scalar leaf");leaf[e]=v;}
   for(uint32_t e=0;e<GC.L;e++)y[e]=source[size_t(j)*GC.L+e]%P;
   for(uint32_t v=0;v<GC.n;v++)multiply_accumulate(answer2,leaf.data()+size_t(v)*GC.L,y.data(),size_t(v)*GC.L);
  }r.magic("ENDGS127");r.eof();
 }
 for(size_t e=0;e<GC.T;e++)need(answer2[e]%P==expected[e],"all6188 independent source-coordinate generalized products");
 need(std::any_of(expected.begin(),expected.end(),[](auto v){return v!=0;}),"verified nonzero complete generalized source detector");
 std::ofstream out(a[4]+".tmp",std::ios::binary);head(out,"R15GP127",BIND);gwrite_dims(out);
 for(uint32_t v:{4367u,zi,node,ordinal,rawSource})le(out,v,4);out.write(reinterpret_cast<const char*>(expected.data()),GC.T);
 out.write(reinterpret_cast<const char*>(divided.data()),divided.size());finish(out,"ENDGP127",a[4]+".tmp",a[4]);
 greceipt(a[4]+".json","\"status\":\"completed\",\"phase\":\"all-original4367-generalized-positive-products\",\"zeroIndex\":"+std::to_string(zi)+",\"originalGlobalZeroNode\":"+std::to_string(node)+
 ",\"all4367IntegerProductsDivisible\":true,\"originalIntegerProductCoordinates\":"+std::to_string(uint64_t(4367)*GC.L)+",\"allDetectorPairingsVerified\":true,\"all6188IndependentSourceContractionsVerified\":true,\"originalPolynomialTermProducts\":"+std::to_string(termProducts)+",\"positiveOriginalGlobalPolynomialSource\":true");return 0;
}
int main(int argc,char**argv){
 try{
  need(argc>=7,"usage: phase child-binding NF-binding GB-binding seconds config paths...");
  const std::string phase=argv[1];BIND=argv[2];NFB=argv[3];GBB=argv[4];
  need(BIND.size()==64&&NFB.size()==64&&GBB.size()==64,"complete source bindings");
  BUDGET=std::stod(argv[5]);need(BUDGET>0&&BUDGET<=7200,"bounded generalized consumer");
  START=std::chrono::steady_clock::now();std::signal(SIGTERM,stop_signal);std::signal(SIGINT,stop_signal);gread_config(argv[6]);
  std::vector<std::string>a;for(int j=7;j<argc;j++)a.push_back(argv[j]);
  if(phase=="transport")return gtransport(a);
  if(phase=="leaves")return gleaves(a);
  if(phase=="nf")return gnf(a);
  if(phase=="scan")return gscan(a);
  if(phase=="reverse")return greverse(a);
  if(phase=="products")return gproducts(a);
  throw std::runtime_error("unknown generalized source phase");
 }catch(const std::exception&e){
  std::cerr<<"generalized-bockstein-error: "<<e.what()<<"\n";
  return std::string(e.what()).find("budget")!=std::string::npos?75:1;
 }
}
