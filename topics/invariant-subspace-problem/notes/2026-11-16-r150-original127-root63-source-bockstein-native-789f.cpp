// Scalar first coefficient-127 Bockstein on the complete original source DAG.
// Author: Astra-ISP-789f / normal_annihilator.
// AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
#include <algorithm>
#include <array>
#include <chrono>
#include <csignal>
#include <cstdint>
#include <cstdio>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>
namespace fs=std::filesystem;
static constexpr uint32_t P=127,M=16129,ALPHA=63,NS=2855,Q=1034;
static constexpr uint64_t PAID_R=69407428,PAID_S=11591;
static volatile std::sig_atomic_t stopped=0;
static void stop_signal(int){stopped=1;}
static void need(bool b,const std::string&s){if(!b)throw std::runtime_error(s);}
static void need(bool b,const char*s){if(!b)throw std::runtime_error(s);}
struct Reader{
 FILE*f=nullptr;std::vector<uint8_t>b;size_t p=0,n=0;uint64_t at=0;
 explicit Reader(const std::string&path):b(1<<20){f=fopen(path.c_str(),"rb");need(f,"open binary "+path);}
 ~Reader(){if(f)fclose(f);}
 int next(){if(p==n){n=fread(b.data(),1,b.size(),f);p=0;if(!n){need(!ferror(f),"binary read");return -1;}}at++;return b[p++];}
 uint8_t byte(){int v=next();need(v>=0,"complete binary prefix");return uint8_t(v);}
 uint64_t le(int k){uint64_t v=0;for(int j=0;j<k;j++)v|=uint64_t(byte())<<(8*j);return v;}
 void read(void*out,size_t k){auto*t=static_cast<uint8_t*>(out);while(k){if(p==n){n=fread(b.data(),1,b.size(),f);p=0;need(n,"complete bulk binary record");}size_t z=std::min(k,n-p);std::copy_n(b.data()+p,z,t);p+=z;at+=z;t+=z;k-=z;}}
 void magic(const char*s){char z[8];read(z,8);need(std::string(z,8)==std::string(s,8),"binary magic");}
 void bind(const std::string&s){char z[64];read(z,64);need(std::string(z,64)==s,"binary source binding");}
 void seek(uint64_t z){need(fseeko(f,off_t(z),SEEK_SET)==0,"seek complete DAG block");p=n=0;at=z;}
 void eof(){need(next()==-1,"complete binary EOF");}
};
static void le(std::ostream&o,uint64_t v,int k){for(int j=0;j<k;j++)o.put(char(v>>(8*j)));}
static void head(std::ostream&o,const char*m,const std::string&b){o.write(m,8);o.write(b.data(),64);}
static void finish(std::ofstream&o,const char*end,const std::string&tmp,const std::string&path){o.write(end,8);o.close();need(bool(o),"complete atomic binary flush");fs::rename(tmp,path);}
static std::string BIND,NFB,GBB;
static std::chrono::steady_clock::time_point START;
static double BUDGET=0;
static double secs(){return std::chrono::duration<double>(std::chrono::steady_clock::now()-START).count();}
static bool out_of_time(){return stopped||secs()>=BUDGET;}
static std::array<uint32_t,46> powP{},powM{};
static std::string quote(const std::string&s){std::string o="\"";for(unsigned char c:s){if(c=='"'||c=='\\'){o+='\\';o+=c;}else if(c=='\n')o+="\\n";else if(c>=32)o+=c;}return o+"\"";}
static void receipt(const std::string&path,const std::string&fields){
 std::ofstream o(path+".tmp");o<<"{\"format\":\"r150-original127-global-source-bockstein-native-v1\",\"binding\":"<<quote(BIND)<<",\"elapsedSeconds\":"<<secs()<<","<<fields<<"}\n";o.close();need(bool(o),"native receipt");fs::rename(path+".tmp",path);
}
static std::vector<uint64_t> mons(int d){
 std::vector<uint64_t>v;auto rec=[&](auto&&self,int left,int lo,uint64_t key)->void{if(!left){v.push_back(key);return;}for(int j=lo;j<11;j++)self(self,left-1,j,key+(uint64_t(1)<<(3*j)));};rec(rec,d,0,0);return v;
}
static int degree(uint64_t k){int d=0;for(int j=0;j<11;j++)d+=(k>>(3*j))&7;return d;}
static uint32_t field_get(const std::vector<uint32_t>&w,size_t nw,size_t coordinate){
 size_t off=coordinate/32;int bit=coordinate%32;need(off<nw,"packed coordinate");
 uint32_t v=0;for(int b=0;b<7;b++)v|=((w[size_t(b)*nw+off]>>bit)&1)<<b;need(v<P,"canonical packed F127 entry");return v;
}
static std::vector<uint32_t> words(Reader&r,size_t n){std::vector<uint32_t>v(n);for(auto&x:v)x=r.le(4);return v;}
static int evaluate(const std::vector<std::string>&a){
 need(a.size()==2,"evaluate path arity");Reader r(a[0]);r.magic("R15GB127");r.bind(GBB);
 need(r.le(4)==P&&r.le(4)==Q&&r.le(4)==45&&r.le(4)==1021&&r.le(4)==9,"paid complete GB geometry");
 const size_t W=(Q+31)/32,nw=46*W;std::vector<uint8_t>matrix(1021*Q);uint32_t prev=0;uint64_t checks=0;
 for(int row=0;row<1021;row++){
  int component=r.le(2),d=r.byte();uint32_t node=r.le(4);int scale=r.byte();
  need(component>int(prev)&&component<=int(Q)&&d<=8&&node>0&&node<=NS+PAID_R&&scale>0&&scale<int(P),"paid final source row");prev=component;
  auto w=words(r,7*nw);
  for(int c=0;c<int(Q);c++){
   uint32_t v=0;
   for(int k=45;k>=0;k--){uint32_t x=field_get(w,nw,size_t(k)*W*32+c);need(k<=d||x==0,"whole original polynomial row degree");v=(ALPHA*v+x)%P;checks++;}
   matrix[size_t(row)*Q+c]=v;
  }
  need(field_get(w,nw,size_t(d)*W*32+component-1)==1,"original monic GB source row");
  if(out_of_time())throw std::runtime_error("evaluate budget before its completed phase");
 }
 for(int j=0;j<9;j++){auto w=words(r,7*nw);(void)w;}
 r.magic("ENDGB127");r.eof();
 std::ofstream o(a[1]+".tmp",std::ios::binary);head(o,"R15EV127",BIND);o.write(GBB.data(),64);
 for(uint32_t v:{P,ALPHA,1021u,Q})le(o,v,4);o.write(reinterpret_cast<const char*>(matrix.data()),matrix.size());finish(o,"ENDEV127",a[1]+".tmp",a[1]);
 receipt(a[1]+".json","\"status\":\"completed\",\"phase\":\"evaluate-original-polynomial-basis\",\"rows\":1021,\"columns\":1034,\"evaluatedAllOriginalPolynomialEntries\":"+std::to_string(checks)+",\"allFinalSourceNodesRetained\":true");
 return 0;
}
static int transport(const std::vector<std::string>&a){
 need(a.size()==4,"transport path arity");std::vector<uint8_t>comp(Q);
 {Reader r(a[2]);r.magic("R15CF127");r.bind(BIND);need(r.le(4)==P&&r.le(4)==ALPHA&&r.le(4)==Q,"component functional geometry");r.read(comp.data(),comp.size());r.magic("ENDCF127");r.eof();}
 std::array<std::vector<uint64_t>,6>mon;std::array<std::unordered_map<uint64_t,int>,6>idx;std::array<std::vector<uint8_t>,6>ell,seen;
 for(int d=1;d<=5;d++){mon[d]=mons(d);ell[d].resize(mon[d].size());seen[d].resize(mon[d].size());for(int j=0;j<int(mon[d].size());j++)idx[d][mon[d][j]]=j;}
 {Reader r(a[1]);r.magic("R15CD127");r.bind(NFB);need(r.le(4)==Q,"whole component dictionary");for(int c=0;c<int(Q);c++){uint64_t k=r.le(8);int d=degree(k);need(d>=1&&d<=5&&idx[d].count(k)&&comp[c]<P,"exact original component key");int j=idx[d].at(k);need(!seen[d][j],"distinct component");seen[d][j]=1;ell[d][j]=comp[c];}r.eof();}
 struct Row{int c,id;std::vector<uint32_t>w;};std::vector<bool>ids(3334,false);
 Reader r(a[0]);r.magic("R15PC127");r.bind(NFB);need(r.le(4)==P&&r.le(4)==3333,"whole prebasis geometry");
 uint64_t forward=r.le(8),backward=r.le(8),changed=r.le(8),same=0,full=0;int total=0;
 need(forward==801468&&backward==1041956&&changed==243,"actual complete original127 prebasis counters");
 for(int d=2;d<=5;d++){
  const size_t hw=(mon[d].size()+31)/32,lw=(mon[d-1].size()+31)/32,nw=hw+11*lw;
  need(r.le(4)==uint64_t(d)&&r.le(4)==nw,"original prebasis degree geometry");int count=r.le(4);std::vector<Row>rows;std::vector<int>piv;int previous=-1;
  for(int j=0;j<count;j++){
   Row x;x.c=r.le(4);x.id=r.le(4);need(x.c>previous&&x.c<int(mon[d].size())&&x.id>=1&&x.id<=3333&&!ids[x.id]&&!seen[d][x.c],"actual distinct original prebasis pivot");previous=x.c;ids[x.id]=true;seen[d][x.c]=1;piv.push_back(x.c);x.w=words(r,7*nw);rows.push_back(std::move(x));total++;
  }
  for(auto &x:rows){
   for(int c:piv){need(field_get(x.w,nw,c)==uint32_t(c==x.c),"all3333 same-degree identity before transpose transport");same++;}
   uint64_t sum=0;
   for(int c=0;c<int(mon[d].size());c++)if(c!=x.c)sum+=field_get(x.w,nw,c)*ell[d][c];
   for(int k=0;k<=10;k++)for(int c=0;c<int(mon[d-1].size());c++)sum+=uint64_t(field_get(x.w,nw,(hw+k*lw)*32+c))*powP[k]*ell[d-1][c];
   ell[d][x.c]=uint8_t((P-sum%P)%P);
  }
  for(auto &x:rows){
   uint64_t sum=0;for(int c=0;c<int(mon[d].size());c++)sum+=field_get(x.w,nw,c)*ell[d][c];
   for(int k=0;k<=10;k++)for(int c=0;c<int(mon[d-1].size());c++)sum+=uint64_t(field_get(x.w,nw,(hw+k*lw)*32+c))*powP[k]*ell[d-1][c];
   need(sum%P==0,"every complete original prebasis point product");full++;
  }
  if(out_of_time())throw std::runtime_error("transpose transport budget before completed phase");
 }
 r.magic("ENDPC127");r.eof();need(total==3333&&full==3333,"all original prebasis rows transported");
 std::ofstream o(a[3]+".tmp",std::ios::binary);head(o,"R15LF127",BIND);for(uint32_t v:{P,ALPHA,4367u})le(o,v,4);int n=0;
 for(int d=1;d<=5;d++)for(size_t j=0;j<mon[d].size();j++){need(seen[d][j],"all original output monomials exactly covered");le(o,mon[d][j],8);o.put(char(ell[d][j]));n++;}
 need(n==4367,"complete original output functional");finish(o,"ENDLF127",a[3]+".tmp",a[3]);
 receipt(a[3]+".json","\"status\":\"completed\",\"phase\":\"original-output-transpose-transport\",\"sameDegreeUnitProducts\":"+std::to_string(same)+",\"all3333OriginalPrebasisProducts\":true,\"all4367OriginalCoordinatesRetained\":true,\"transportOrder\":\"increasing-moment-degree\"");
 return 0;
}
struct Fwd{uint32_t raw=0;uint8_t scale=0;std::vector<std::pair<uint16_t,uint8_t>>ops;};
struct Back{uint16_t id=0;std::vector<std::pair<uint16_t,uint8_t>>ops;};
struct OpsData{std::vector<uint8_t>leaf,pre,nf;std::vector<uint32_t>raw;uint64_t checks=0,nfOps=0;std::vector<Fwd>f;std::vector<Back>b;};
static uint8_t subtract_carry(uint8_t x,uint8_t y,uint32_t c,int exponent,uint64_t &checks){
 need(c>0&&c<P&&exponent>=0&&exponent<=45,"canonical original source operation");
 uint32_t z=(x+P-uint32_t(uint64_t(c)*powP[exponent]*y%P))%P;
 uint32_t zz=(uint64_t(P)*x+M-uint64_t(c)*powM[exponent]*(P*y)%M)%M;
 need(zz==P*z,"integer mod127-square scalar agrees with exact divided carry");checks++;return uint8_t(z);
}
static OpsData load_ops(const std::vector<std::string>&a){
 OpsData o;o.leaf.resize(6189);o.pre.resize(3334);o.nf.resize(NS+1);o.raw.resize(NS+1);o.f.resize(3334);std::vector<bool>seen(6189,false);
 {Reader r(a[0]);r.magic("R15SC127");r.bind(BIND);need(r.le(4)==P&&r.le(4)==ALPHA&&r.le(4)==6188,"original scalar leaves");for(int j=1;j<=6188;j++){uint32_t scalar=r.le(2);o.leaf[j]=r.byte();need(scalar<M&&o.leaf[j]<P&&scalar==P*o.leaf[j],"all6188 original columns exact divisible scalars");}r.magic("ENDSC127");r.eof();}
 auto source_degree=[](uint32_t raw){uint32_t m=(raw-1)/17;return m<1?0:m<12?1:m<78?2:3;};
 {Reader r(a[1]);r.magic("R15PF127");need(r.le(4)==3333,"forward whole source count");r.bind(NFB);uint64_t n=0;
  for(int i=1;i<=3333;i++){
   auto &v=o.f[i];v.raw=r.le(4);v.scale=r.byte();uint32_t count=r.le(4);
   need(v.raw>=1&&v.raw<=6188&&!seen[v.raw]&&v.scale>0&&v.scale<P&&count<=3333,"forward original raw source and scale");seen[v.raw]=true;uint8_t x=o.leaf[v.raw];
   for(uint32_t k=0;k<count;k++){uint16_t id=r.le(2);uint8_t c=r.byte();need(id>=1&&id<i&&source_degree(o.f[id].raw)==source_degree(v.raw),"forward only same-grade earlier original sources");x=subtract_carry(x,o.pre[id],c,0,o.checks);v.ops.push_back({id,c});n++;}
   o.pre[i]=uint8_t(v.scale*x%P);need((uint64_t(v.scale)*P*x)%M==P*o.pre[i],"integer normalized forward-source scalar");
  }r.eof();need(n==801468,"all actual forward operations");
 }
 {Reader r(a[2]);r.magic("R15PB127");need(r.le(4)==3333,"backward whole source count");r.bind(NFB);std::vector<bool>done(3334,false);uint64_t n=0;
  for(int j=0;j<3333;j++){
   Back v;v.id=r.le(2);uint32_t count=r.le(4);need(v.id>=1&&v.id<=3333&&!done[v.id]&&count<=3333,"whole backward source identity");done[v.id]=true;uint8_t x=o.pre[v.id];
   for(uint32_t k=0;k<count;k++){uint16_t id=r.le(2);uint8_t c=r.byte();need(id>=1&&id<=3333&&id!=v.id&&done[id]&&source_degree(o.f[id].raw)==source_degree(o.f[v.id].raw),"backward uses completed same-grade pivots");x=subtract_carry(x,o.pre[id],c,0,o.checks);v.ops.push_back({id,c});n++;}
   o.pre[v.id]=x;o.b.push_back(std::move(v));
  }r.eof();need(n==1041956,"all actual backward operations");
 }
 {Reader r(a[3]);r.magic("R15NR127");r.bind(NFB);need(r.le(4)==NS+9,"whole NF original sources and targets");
  for(int i=1;i<=int(NS+9);i++){
   uint32_t raw=r.le(4);uint16_t target=r.le(2);uint32_t count=r.le(4);bool source=i<=int(NS);uint8_t x=0;
   if(source){need(raw>=1&&raw<=6188&&!seen[raw]&&target==0,"whole distinct original NF complement");seen[raw]=true;o.raw[i]=raw;x=o.leaf[raw];}
   else need(raw==0&&target==i-int(NS)+1,"all nine target records retained while not used as syzygies");
   for(uint32_t k=0;k<count;k++){uint16_t id=r.le(2);uint8_t exponent=r.byte(),c=r.byte();need(id>=1&&id<=3333&&exponent<=45&&c>0&&c<P,"complete original NF recipe");if(source)x=subtract_carry(x,o.pre[id],c,exponent,o.checks);o.nfOps++;}
   if(source)o.nf[i]=x;
  }r.eof();need(o.nfOps==29606398,"all paid original NF operations");
 }
 need(std::count(seen.begin(),seen.end(),true)==6188,"all original6188 sources present exactly once");return o;
}
struct Zero{uint32_t ordinal,raw,node;uint8_t value;};
struct Block{uint64_t reductions,offset;};
struct Replay{
 uint64_t red=0,offset=81;uint32_t inputs=0,insertions=0,swaps=0,finals=0,current=0,last=0;bool active=false;
 std::vector<uint8_t>value;std::vector<uint32_t>piv=std::vector<uint32_t>(Q);std::vector<Zero>zero;std::vector<Block>blocks={{0,81}};
};
static void save_replay(const std::string&path,const Replay&s){
 std::ofstream o(path+".tmp",std::ios::binary);head(o,"R15DP127",BIND);o.write(NFB.data(),64);o.write(GBB.data(),64);
 le(o,s.red,8);le(o,s.offset,8);for(uint32_t x:{s.inputs,s.insertions,s.swaps,s.finals,s.current,s.last})le(o,x,4);o.put(char(s.active));le(o,s.value.size(),4);o.write(reinterpret_cast<const char*>(s.value.data()),s.value.size());
 for(uint32_t x:s.piv)le(o,x,4);le(o,s.zero.size(),4);for(auto z:s.zero){le(o,z.ordinal,4);le(o,z.raw,4);le(o,z.node,4);o.put(char(z.value));}
 le(o,s.blocks.size(),4);for(auto b:s.blocks){le(o,b.reductions,8);le(o,b.offset,8);}finish(o,"ENDDP127",path+".tmp",path);
}
static Replay read_replay(const std::string&path,const OpsData&o,bool values){
 Reader r(path);r.magic("R15DP127");r.bind(BIND);r.bind(NFB);r.bind(GBB);Replay s;s.red=r.le(8);s.offset=r.le(8);s.inputs=r.le(4);s.insertions=r.le(4);s.swaps=r.le(4);s.finals=r.le(4);s.current=r.le(4);s.last=r.le(4);s.active=r.byte();uint32_t n=r.le(4);
 need(s.red<=PAID_R&&n==NS+s.red+1&&s.inputs<=NS&&s.insertions<=1021&&s.swaps<=PAID_S&&s.finals<=1021,"whole saved scalar prefix counters");
 if(values){s.value.resize(n);r.read(s.value.data(),n);need(std::equal(o.nf.begin(),o.nf.end(),s.value.begin()),"same complete original NF scalar seeds");}
 else {std::vector<uint8_t>buffer(1<<20);uint32_t left=n;while(left){uint32_t z=std::min<uint32_t>(left,buffer.size());r.read(buffer.data(),z);left-=z;}}
 for(auto &x:s.piv)x=r.le(4);uint32_t nz=r.le(4);need(nz<=1834,"saved global zero endpoints");
 for(uint32_t j=0;j<nz;j++){Zero z;z.ordinal=r.le(4);z.raw=r.le(4);z.node=r.le(4);z.value=r.byte();need(z.ordinal>=1&&z.ordinal<=NS&&z.raw==o.raw[z.ordinal]&&z.node<=NS+s.red&&z.value<P,"saved original global zero-source record");s.zero.push_back(z);}
 uint32_t nb=r.le(4);need(nb>=1&&nb<=PAID_R/65536+2,"bounded scalar replay block index");s.blocks.clear();
 for(uint32_t j=0;j<nb;j++){Block b;b.reductions=r.le(8);b.offset=r.le(8);need((j==0&&b.reductions==0&&b.offset==81)||(j&&b.reductions==s.blocks.back().reductions+65536&&b.offset>s.blocks.back().offset),"actual reverse-block source order");s.blocks.push_back(b);}
 r.magic("ENDDP127");r.eof();return s;
}
static std::string replay_fields(const Replay&s,const char*status,const OpsData&o,bool reused){
 size_t positive=std::count_if(s.zero.begin(),s.zero.end(),[](auto z){return z.value!=0;});
 return "\"status\":"+quote(status)+",\"phase\":\"global-source-divided-scalar-replay\",\"allOriginal6188ScalarLeavesDivisible\":true,\"forwardOperations\":801468,\"backwardOperations\":1041956,\"normalOperations\":"+std::to_string(o.nfOps)+",\"processedOriginalSources\":"+std::to_string(s.inputs)+",\"GBReductions\":"+std::to_string(s.red)+",\"GBSwaps\":"+std::to_string(s.swaps)+",\"globalZeroEndpoints\":"+std::to_string(s.zero.size())+",\"nonzeroBocksteinEndpoints\":"+std::to_string(positive)+",\"integerScalarRecurrenceChecks\":"+std::to_string(o.checks+s.red)+",\"allGlobalPolynomialRelationsInheritedFromCompletePaidDAG\":true,\"pointOnlyKernelUsedAsSource\":false,\"resumedCommittedPrefix\":"+(reused?"true":"false");
}
static int replay(const std::vector<std::string>&a){
 need(a.size()==6,"replay path arity");auto o=load_ops(a);fs::create_directories(a[5]);const std::string state=a[5]+"/scalar-checkpoint.bin",rp=a[5]+"/scalar-replay-native.json";Replay s;bool reused=fs::exists(state);
 if(reused)s=read_replay(state,o,true);else s.value=o.nf;
 Reader r(a[4]);r.magic("R15GO127");r.bind(GBB);need(r.le(4)==NS&&r.le(4)==Q&&r.byte()==45,"whole source DAG header");
 need(s.offset<=fs::file_size(a[4]),"valid committed scalar prefix");r.seek(s.offset);s.value.reserve(NS+PAID_R+1);double last=secs();
 while(true){
  int event=r.next();if(event<0)break;
  if(event=='I'){
   uint32_t ordinal=r.le(4),raw=r.le(4);need(!s.active&&ordinal==s.inputs+1&&ordinal<=NS&&raw==o.raw[ordinal]&&s.finals==0,"whole original source input order");s.inputs++;s.current=s.last=ordinal;s.active=true;
  }else if(event=='B'){
   uint32_t c=r.le(2),node=r.le(4);need(s.active&&c>=1&&c<=Q&&s.piv[c-1]==0&&node==s.current,"complete original basis insertion");s.piv[c-1]=node;s.insertions++;s.active=false;
  }else if(event=='S'){
   uint32_t c=r.le(2),current=r.le(4),pivot=r.le(4);need(s.active&&c>=1&&c<=Q&&current==s.piv[c-1]&&pivot==s.current,"whole source swap routing");s.current=current;s.piv[c-1]=pivot;s.swaps++;
  }else if(event=='R'){
   uint32_t old=r.le(4),pivot=r.le(4);int exponent=r.byte(),c=r.byte();
   need(s.active&&old==s.current&&old<s.value.size()&&pivot>=1&&pivot<s.value.size()&&s.red<PAID_R,"complete original reduction source nodes");
   uint64_t local=0;uint8_t v=subtract_carry(s.value[old],s.value[pivot],c,exponent,local);s.value.push_back(v);s.red++;s.current=NS+s.red;
   if(s.red%65536==0)s.blocks.push_back({s.red,r.at});
  }else if(event=='Z'){
   uint32_t node=r.le(4);need(s.active&&node==s.current&&node<s.value.size(),"whole polynomial zero-source endpoint");s.zero.push_back({s.last,o.raw[s.last],node,s.value[node]});s.active=false;
  }else if(event=='F'){
   uint32_t c=r.le(2),node=r.le(4),scale=r.byte();need(!s.active&&s.inputs==NS&&c>=1&&c<=Q&&node==s.piv[c-1]&&scale>0&&scale<P,"all final original basis source nodes");s.finals++;
  }else throw std::runtime_error("unknown whole original source DAG event");
  s.offset=r.at;
  if((s.red%65536==0||event!='R')&&(out_of_time()||secs()-last>=30)){
   save_replay(state,s);last=secs();if(out_of_time()){receipt(rp,replay_fields(s,"budget-checkpoint",o,reused));return 75;}
  }
 }
 s.offset=r.at;need(s.inputs==NS&&s.insertions==1021&&s.zero.size()==1834&&s.red==PAID_R&&s.swaps==PAID_S&&s.finals==1021&&!s.active,"all2855 input sources and1834 global zero endpoints completed");
 save_replay(state,s);receipt(rp,replay_fields(s,"completed",o,reused)+",\"all1834GlobalZeroEndpointsCovered\":true,\"allGlobalSourceRoutesVerified\":true");
 return 0;
}
struct Red{uint32_t old,pivot,node;uint8_t exponent,c;};
static uint16_t addM(uint16_t x,uint64_t y){return uint16_t((x+y)%M);}
static uint16_t subM(uint16_t x,uint64_t y){return uint16_t((x+M-y%M)%M);}
static int witness(const std::vector<std::string>&a){
 need(a.size()==6,"witness path arity");auto o=load_ops(a);const std::string state=a[5]+"/scalar-checkpoint.bin",rp=a[5]+"/witness-reverse-native.json";
 Replay s=read_replay(state,o,false);need(s.inputs==NS&&s.red==PAID_R&&s.zero.size()==1834&&s.finals==1021,"completed full global scalar scan before witness");
 auto it=std::find_if(s.zero.begin(),s.zero.end(),[](auto z){return z.value!=0;});need(it!=s.zero.end(),"positive global source witness requested only after a nonzero endpoint");Zero chosen=*it;
 const uint64_t witnessR=chosen.node>NS?chosen.node-NS:0;std::vector<uint16_t>weight(size_t(chosen.node)+1);weight[chosen.node]=1;Reader r(a[4]);uint64_t applied=0,parsed=0;
 for(size_t bi=s.blocks.size();bi-->0;){
  Block begin=s.blocks[bi];if(begin.reductions>=witnessR)continue;
  uint64_t endOffset=bi+1<s.blocks.size()?s.blocks[bi+1].offset:s.offset;std::vector<Red>red;r.seek(begin.offset);uint64_t count=begin.reductions;
  while(r.at<endOffset){
   int event=r.next();need(event>=0,"complete indexed source block");
   if(event=='I'){r.le(4);r.le(4);}else if(event=='B'){r.le(2);r.le(4);}else if(event=='S'){r.le(2);r.le(4);r.le(4);}
   else if(event=='R'){Red x;x.old=r.le(4);x.pivot=r.le(4);x.exponent=r.byte();x.c=r.byte();x.node=NS+(++count);need(x.old<x.node&&x.pivot<x.node&&x.exponent<=45&&x.c>0&&x.c<P,"reverse original DAG edge");if(count<=witnessR)red.push_back(x);parsed++;}
   else if(event=='Z'){r.le(4);}else if(event=='F'){r.le(2);r.le(4);r.byte();}else throw std::runtime_error("reverse block event");
  }
  need(r.at==endOffset,"exact whole-event reverse block boundary");
  for(size_t j=red.size();j-->0;){auto x=red[j];uint16_t w=weight[x.node];if(w){weight[x.old]=addM(weight[x.old],w);weight[x.pivot]=subM(weight[x.pivot],uint64_t(w)*x.c*powM[x.exponent]);weight[x.node]=0;applied++;}}
  if(out_of_time())throw std::runtime_error("reverse source witness budget; complete scalar checkpoint remains reusable");
 }
 need(std::all_of(weight.begin()+std::min<size_t>(NS+1,weight.size()),weight.end(),[](auto v){return v==0;}),"all internal witness nodes reversed");
 std::vector<uint16_t>original(6189),pre(3334);
 {Reader nf(a[3]);nf.magic("R15NR127");nf.bind(NFB);need(nf.le(4)==NS+9,"reverse complete NF records");
  for(int i=1;i<=int(NS+9);i++){
   uint32_t raw=nf.le(4);uint16_t target=nf.le(2);uint32_t count=nf.le(4);uint16_t w=(i<=int(NS)&&size_t(i)<weight.size())?weight[i]:0;
   if(i<=int(NS)){need(raw==o.raw[i]&&target==0,"reverse original source ordinal");original[raw]=addM(original[raw],w);}else need(raw==0&&target==i-int(NS)+1,"reverse retained target labels");
   for(uint32_t j=0;j<count;j++){uint16_t id=nf.le(2);uint8_t exponent=nf.byte(),c=nf.byte();if(w)pre[id]=subM(pre[id],uint64_t(w)*c*powM[exponent]);}
  }nf.eof();
 }
 for(size_t j=o.b.size();j-->0;){const auto&v=o.b[j];uint16_t w=pre[v.id];if(w)for(auto [id,c]:v.ops)pre[id]=subM(pre[id],uint64_t(w)*c);}
 for(int i=3333;i>=1;i--){const auto&v=o.f[i];uint16_t w=uint16_t(uint64_t(pre[i])*v.scale%M);original[v.raw]=addM(original[v.raw],w);if(w)for(auto [id,c]:v.ops)pre[id]=subM(pre[id],uint64_t(w)*c);pre[i]=0;}
 need(std::all_of(pre.begin(),pre.end(),[](auto v){return !v;}),"all original prebasis recipes reversed");
 uint64_t check=0;size_t support=0;for(int j=1;j<=6188;j++){check+=uint64_t(original[j])*o.leaf[j];support+=original[j]!=0;}
 need(check%P==chosen.value,"independent full6188 source-coordinate divided scalar");
 const std::string path=a[5]+"/positive-original-source-evaluated.bin";std::ofstream out(path+".tmp",std::ios::binary);head(out,"R15YV127",BIND);for(uint32_t v:{P,ALPHA,6188u,chosen.node,chosen.ordinal,chosen.raw})le(out,v,4);out.put(char(chosen.value));for(int j=1;j<=6188;j++)le(out,original[j],2);finish(out,"ENDYV127",path+".tmp",path);
 receipt(rp,"\"status\":\"completed\",\"phase\":\"positive-global-source-reverse-certificate\",\"originalGlobalZeroNode\":"+std::to_string(chosen.node)+",\"inputOrdinal\":"+std::to_string(chosen.ordinal)+",\"inputOriginalRawSource\":"+std::to_string(chosen.raw)+",\"bocksteinResidue\":"+std::to_string(chosen.value)+",\"sourceEvaluationModulus\":16129,\"nonzeroOriginalSourceCoordinates\":"+std::to_string(support)+",\"parsedGBReverseEdges\":"+std::to_string(parsed)+",\"nonzeroReverseEdgeUpdates\":"+std::to_string(applied)+",\"all6188EvaluatedSourceScalarProductsVerified\":true,\"full4367OriginalProductsLeftToWrapper\":true");
 return 0;
}
int main(int argc,char**argv){
 try{
  need(argc>=8,"mode bindings seconds and exact paths");const std::string mode=argv[1];BIND=argv[2];NFB=argv[3];GBB=argv[4];BUDGET=std::stod(argv[5]);START=std::chrono::steady_clock::now();
  for(const auto&s:{BIND,NFB,GBB})need(s.size()==64&&s.find_first_not_of("0123456789abcdef")==std::string::npos,"frozen SHA256 binding");need(BUDGET>0&&BUDGET<=600,"finite native phase budget");
  std::signal(SIGTERM,stop_signal);powP[0]=powM[0]=1;for(int k=1;k<=45;k++){powP[k]=uint64_t(powP[k-1])*ALPHA%P;powM[k]=uint64_t(powM[k-1])*ALPHA%M;}
  std::vector<std::string>a;for(int j=6;j<argc;j++)a.emplace_back(argv[j]);
  if(mode=="evaluate")return evaluate(a);if(mode=="transport")return transport(a);if(mode=="replay")return replay(a);if(mode=="witness")return witness(a);throw std::runtime_error("unknown bounded source consumer mode");
 }catch(const std::exception&e){std::cerr<<"ORIGINAL127_BOCKSTEIN_FAILED "<<e.what()<<"\n";return 1;}
}
