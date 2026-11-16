// Full original weight-ten F127 Macaulay, one bit-plane copy and source DAG.
// Author: Astra-ISP-789f / literature_audit, with /root. 2026-11-16.
// AI-assisted: GPT-6 Astra Pro.
// No conclusion is accepted until the separate ordinary-scalar/source verifier.
#include "2026-11-15-r150-original-f127-bitplane-789f.hpp"
#include <chrono>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <filesystem>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numeric>
#include <sstream>
#include <unordered_map>
#include <fcntl.h>
#include <sys/resource.h>
#include <unistd.h>
namespace fs=std::filesystem;
using Clock=std::chrono::steady_clock;
static constexpr uint32_t M0=77276,N0=13808,G0=200;
static constexpr uint64_t TERMS0=8037189,TARGET0=2604,INPUT_BYTES=73145375;
static const char* FORMAT="r150-original-weight10-full-macaulay127-native-v1";
static const std::array<int,10> RW={0,2,2,2,2,2,4,4,4,4};
static const std::array<int,12> VW={1,1,1,1,1,1,2,2,2,2,2,2};
struct Budget:std::runtime_error{using std::runtime_error::runtime_error;};
static void need(bool b,const std::string&s){if(!b)throw std::runtime_error(s);}
static std::string fixed(std::istream&f,size_t n){
 std::string s(n,'\0');f.read(s.data(),std::streamsize(n));
 need(size_t(f.gcount())==n,"whole fixed field");return s;
}
static void magic(std::istream&f,const char*s){need(fixed(f,8)==std::string(s,8),"exact complete protocol");}
static bool hex64(const std::string&s){return s.size()==64&&s.find_first_not_of("0123456789abcdef")==std::string::npos;}
static void host(){
 uint32_t a=1;need(sizeof(uint32_t)==4&&reinterpret_cast<uint8_t*>(&a)[0]==1,"explicit little-endian uint32 host");
}
static std::string quote(const std::string&s){
 std::ostringstream o;o<<'"';for(unsigned char c:s){
  if(c=='"'||c=='\\')o<<'\\'<<char(c);
  else if(c=='\n')o<<"\\n";else if(c=='\r')o<<"\\r";else if(c=='\t')o<<"\\t";
  else if(c<32)o<<"\\u"<<std::hex<<std::setw(4)<<std::setfill('0')<<unsigned(c)<<std::dec;
  else o<<char(c);
 }o<<'"';return o.str();
}
static void sync_finish(std::ofstream&f,const fs::path&tmp,const fs::path&dest){
 f.flush();need(bool(f),"complete output stream");f.close();
 int fd=open(tmp.c_str(),O_RDONLY);need(fd>=0,"open complete temporary output for fsync");
 int rc=fsync(fd);close(fd);need(rc==0,"whole temporary output fsync");
 need(!fs::exists(dest),"new generation never overwrites a prior complete output");
 fs::rename(tmp,dest);
 int dd=open(dest.parent_path().c_str(),O_RDONLY|O_DIRECTORY);
 if(dd>=0){int z=fsync(dd);close(dd);need(z==0,"output directory fsync");}
}
static std::string name(const std::string&stem,uint32_t gen,const std::string&ext){
 std::ostringstream z;z<<stem<<'-'<<std::setw(4)<<std::setfill('0')<<gen<<ext;return z.str();
}
static int pweight(uint64_t code){
 need((code>>60)==0,"all twelve exponent lanes retained");int w=0;
 for(int i=0;i<12;i++){int e=(code>>(5*i))&31;need(e<=10,"full literal exponent bound");w+=VW[i]*e;}
 return w;
}
static int degree(uint64_t code,bool shifted){
 uint32_t r=code&15;need(r<10,"all ten original components");
 return pweight(code>>4)+(shifted?RW[r]:0);
}
static void mon_rec(int i,int left,uint64_t code,std::vector<uint64_t>&v){
 if(i==12){if(left==0)v.push_back(code);return;}
 for(int e=0;e*VW[i]<=left;e++)mon_rec(i+1,left-e*VW[i],code|(uint64_t(e)<<(5*i)),v);
}
static std::array<std::vector<uint64_t>,11> monomials(){
 std::array<std::vector<uint64_t>,11> a;
 const std::array<size_t,11> count={1,6,27,92,273,714,1715,3816,8007,15938,30381};
 for(int k=0;k<=10;k++){mon_rec(0,k,0,a[k]);std::sort(a[k].begin(),a[k].end());
  need(a[k].size()==count[k]&&std::adjacent_find(a[k].begin(),a[k].end())==a[k].end(),"complete weighted monomial dictionary");
 }return a;
}
struct Term{uint64_t code;uint8_t coefficient;};
struct Label{uint32_t source;uint64_t multiplier;};
struct Input{
 fs::path path;std::ifstream f;std::string binding;uint32_t m,n,g;
 uint64_t totalTerms,targetTerms,targetOffset;
 std::array<std::vector<uint64_t>,11> monos;
 std::vector<uint64_t> rows,offsets,counts;
 std::vector<uint32_t> weights;
 std::vector<Label> labels;
 std::unordered_map<uint64_t,uint32_t> rowIndex;
 int loaded=-1;std::vector<Term> terms,target;
 explicit Input(const fs::path&p):path(p),f(p,std::ios::binary),monos(monomials()){
  need(bool(f),"open full original sparse input");magic(f,"R15WM101");
  need(read_le(f,4)==1&&read_le(f,4)==127,"version and exact prime");
  m=read_le(f,4);n=read_le(f,4);g=read_le(f,4);need(read_le(f,4)==10,"literal target weight10");
  totalTerms=read_le(f,8);targetTerms=read_le(f,8);binding=fixed(f,64);
  need(m==M0&&n==N0&&g==G0&&totalTerms==TERMS0&&targetTerms==TARGET0&&hex64(binding),"complete original fixed dimensions and source count");
  for(int x:RW)need(read_le(f,1)==uint64_t(x),"every original row shift");
  for(int x:VW)need(read_le(f,1)==uint64_t(x),"every original parameter weight");
  rows.reserve(m);rowIndex.reserve(m*2);
  for(uint32_t r=0;r<10;r++)for(uint64_t e:monos[10-RW[r]]){
   uint64_t k=(e<<4)|r;need(read_le(f,8)==k,"complete literal output dictionary order");
   need(rowIndex.emplace(k,rows.size()).second,"distinct full output coordinate");rows.push_back(k);
  }
  need(rows.size()==m,"all77276 output coordinates");
  labels.resize(n);
  for(auto&l:labels){l.source=read_le(f,4);l.multiplier=read_le(f,8);}
  weights.resize(g);counts.resize(g);offsets.resize(g);std::array<uint32_t,11> wc{};
  uint64_t sum=0;
  for(uint32_t i=0;i<g;i++){
   need(read_le(f,4)==i,"all200 original source labels in order");weights[i]=read_le(f,4);counts[i]=read_le(f,8);
   need(weights[i]>=5&&weights[i]<=10&&counts[i]<=M0,"complete source weight and bounded full vector");
   wc[weights[i]]++;sum+=counts[i];
  }
  need(wc[5]==6&&wc[6]==20&&wc[7]==30&&wc[8]==40&&wc[9]==24&&wc[10]==80&&sum==totalTerms,"whole Gamma200 weight profile");
  uint32_t j=0;
  for(uint32_t i=0;i<g;i++)for(uint64_t e:monos[10-weights[i]]){
   need(j<n&&labels[j].source==i&&labels[j].multiplier==e,"every original multiplied source, including zero and duplicate columns");j++;
  }need(j==n,"all13808 original multiplier labels");
  uint64_t cursor=uint64_t(f.tellg());
  need(cursor==112+22+uint64_t(m)*8+uint64_t(n)*12+uint64_t(g)*16,"whole sparse header byte layout");
  for(uint32_t i=0;i<g;i++){offsets[i]=cursor;cursor+=9*counts[i];}
  targetOffset=cursor;cursor+=9*targetTerms;
  need(cursor==INPUT_BYTES&&fs::file_size(path)==cursor,"whole exact sparse input and EOF");
 }
 std::vector<Term> read_terms(uint64_t offset,uint64_t count,int wt){
  f.clear();f.seekg(offset);need(bool(f),"literal source seek");std::string raw=fixed(f,count*9);
  std::vector<Term> a;a.reserve(count);uint64_t previous=0;bool first=true;
  for(uint64_t j=0;j<count;j++){
   uint64_t k=0;std::memcpy(&k,raw.data()+9*j,8);uint8_t c=uint8_t(raw[9*j+8]);
   need(c>0&&c<127&&(first||k>previous)&&degree(k,true)==wt,"all source terms canonical, unique, complete and correctly weighted");
   first=false;previous=k;a.push_back({k,c});
  }return a;
 }
 void validate_all(){
  uint64_t seen=0;
  for(uint32_t i=0;i<g;i++){auto z=read_terms(offsets[i],counts[i],weights[i]);seen+=z.size();}
  need(seen==totalTerms,"all original source coefficients read");
  target=read_terms(targetOffset,targetTerms,10);
  for(const auto&t:target)need((t.code&15)==0&&rowIndex.count(t.code),"literal e0 target with every original output coordinate");
  loaded=-1;terms.clear();
 }
 const std::vector<Term>& source(uint32_t i){
  need(i<g,"original source index");
  if(loaded!=int(i)){terms=read_terms(offsets[i],counts[i],weights[i]);loaded=i;}
  return terms;
 }
 Row column(uint32_t j){
  need(j<n,"original input column index");const auto&l=labels[j];const auto&t=source(l.source);
  Row a(7*((m+31)/32),0);const int nw=(m+31)/32;
  need(pweight(l.multiplier)==10-int(weights[l.source]),"entire source multiplier weight");
  for(const auto&z:t){
   // Each lane sum is at most the total weight10, so no base32 carry is possible.
   uint64_t key=(((z.code>>4)+l.multiplier)<<4)|(z.code&15);
   auto at=rowIndex.find(key);need(at!=rowIndex.end(),"every multiplied term remains in the full original output dictionary");
   BitOps::set(a,nw,at->second,z.coefficient);
  }return a;
 }
 Row target_row()const{
  Row a(7*((m+31)/32),0);const int nw=(m+31)/32;
  for(const auto&t:target){auto i=rowIndex.find(t.code);need(i!=rowIndex.end(),"target coordinate");BitOps::set(a,nw,i->second,t.coefficient);}
  return a;
 }
};
struct Counts{
 uint64_t cancellations=0,passes=0,words=0,normalizations=0;
 void add(const Counts&x){cancellations+=x.cancellations;passes+=x.passes;words+=x.words;normalizations+=x.normalizations;}
};
struct Scaled{
 const BitOps&ops;Counts&attempt;
 explicit Scaled(const BitOps&o,Counts&a):ops(o),attempt(a){}
 void add(Row&r,int rw,int ro,const Row&q,int qw,int qo,int len,int scalar,Counts&local)const{
  need(scalar>0&&scalar<127&&(&r!=&q),"literal nonzero scalar and distinct input");
  static constexpr int length[9]={1,2,2,2,2,3,3,3,3};
  static constexpr int shifts[9][3]={{0,0,0},{0,1,0},{0,2,0},{3,0,0},{0,3,0},{0,1,3},{0,2,3},{0,1,4},{0,2,4}};
  static constexpr int signs[9][3]={{0,0,0},{0,0,0},{0,0,0},{0,1,0},{0,0,0},{0,0,0},{0,0,0},{0,0,0},{0,0,0}};
  auto v=ops.rep[scalar];
  for(int k=0;k<length[v.c];k++){
   BitOps::add(r,rw,ro,q,qw,qo,len,(v.rot+shifts[v.c][k])%7,v.neg^signs[v.c][k]);
   local.passes++;local.words+=len;attempt.passes++;attempt.words+=len;
  }
 }
 void normalize(Row&r,int nw,int first,int scalar,Counts&local)const{
  need(scalar>0&&scalar<127,"normalization scalar");
  local.normalizations++;attempt.normalizations++;if(scalar==1)return;
  Row original=r;for(int b=0;b<7;b++)std::fill(r.begin()+b*nw+first,r.begin()+(b+1)*nw,0);
  add(r,nw,first,original,nw,first,nw-first,scalar,local);
 }
};
struct Basis{uint32_t pivot=0,source=0;uint8_t factor=0;Row row;std::vector<uint8_t> dag;};
struct State{
 uint32_t m,n,g,next=0;int nw;std::string binding,inputSHA;
 std::vector<Basis> basis;std::vector<int> at;std::vector<uint8_t> classification;Counts committed;
 State(uint32_t mm,uint32_t nn,uint32_t gg,std::string b,std::string ih):
  m(mm),n(nn),g(gg),nw((mm+31)/32),binding(std::move(b)),inputSHA(std::move(ih)),at(mm,-1),classification(nn,0){basis.reserve(nn);}
};
static void valid_row(const Row&r,const State&s,uint32_t p){
 need(r.size()==size_t(7*s.nw)&&p<s.m&&BitOps::get(r,s.nw,p)==1,"whole normalized original output pivot");
 for(int b=0;b<7;b++){
  for(uint32_t w=0;w<p/32;w++)need(r[b*s.nw+w]==0,"all earlier complete output words zero");
  if(p%32)need((r[b*s.nw+p/32]&((uint32_t(1)<<(p%32))-1))==0,"all earlier output lanes zero");
 }
 for(int w=0;w<s.nw;w++){
  uint32_t all=UINT32_MAX;for(int b=0;b<7;b++)all&=r[b*s.nw+w];
  need(all==0,"canonical field entries, no redundant127");
 }
 if(s.m%32)for(int b=0;b<7;b++)need((r[b*s.nw+s.nw-1]>>(s.m%32))==0,"all original output padding zero");
}
static uint32_t first_nonzero(const Row&r,const State&s,uint32_t start){
 if(start>=s.m)return s.m;
 for(uint32_t w=start/32;w<uint32_t(s.nw);w++){
  uint32_t z=0;for(int b=0;b<7;b++)z|=r[b*s.nw+w];
  if(w==start/32)z&=UINT32_MAX<<(start%32);
  if(z){uint32_t q=32*w+__builtin_ctz(z);need(q<s.m,"no nonzero output padding");return q;}
 }return s.m;
}
static void tick(const Clock::time_point&deadline){
 if(Clock::now()>=deadline)throw Budget("stop before another incomplete column; reserve complete state write");
}
static void insert_column(State&s,Row r,uint32_t j,const Scaled&scaled,const Clock::time_point&deadline){
 need(j==s.next&&j<s.n&&s.classification[j]==0,"next whole original column only");
 Counts local;std::vector<uint8_t> dag(s.basis.size(),0);uint32_t p=0;uint64_t steps=0;
 while((p=first_nonzero(r,s,p))<s.m){
  if((steps++&31)==0)tick(deadline);
  int v=BitOps::get(r,s.nw,p),bi=s.at[p];
  if(bi>=0){
   need(dag[bi]==0,"one exact cancellation for each preceding pivot");
   int d=127-v;dag[bi]=d;
   scaled.add(r,s.nw,p/32,s.basis[bi].row,s.nw,p/32,s.nw-p/32,d,local);
   need(BitOps::get(r,s.nw,p)==0,"actual whole original pivot canceled");
   local.cancellations++;scaled.attempt.cancellations++;p++;continue;
  }
  scaled.normalize(r,s.nw,p/32,scaled.ops.inv[v],local);valid_row(r,s,p);
  Basis b;b.pivot=p;b.source=j;b.factor=v;b.row=std::move(r);b.dag=std::move(dag);
  s.at[p]=s.basis.size();s.basis.push_back(std::move(b));s.classification[j]=1;
  s.next++;s.committed.add(local);return;
 }
 s.classification[j]=2;s.next++;s.committed.add(local);
}
static uint64_t state_size(const State&s){
 uint64_t r=s.basis.size();
 return 200+uint64_t(s.n)+r*(16+uint64_t(7*s.nw)*4)+r*(r-1)/2;
}
static void save_state(const fs::path&p,const State&s){
 auto t=p;t+=".tmp";std::ofstream f(t,std::ios::binary);need(bool(f),"new full checkpoint temporary file");
 f.write("R15WS101",8);
 for(uint32_t v:{1u,127u,s.m,s.n,s.g,s.next,uint32_t(s.basis.size()),uint32_t(s.nw)})u32(f,v);
 f.write(s.binding.data(),64);f.write(s.inputSHA.data(),64);
 for(uint64_t v:{s.committed.cancellations,s.committed.passes,s.committed.words,s.committed.normalizations})u64(f,v);
 f.write(reinterpret_cast<const char*>(s.classification.data()),s.classification.size());
 for(uint32_t k=0;k<s.basis.size();k++){
  const auto&b=s.basis[k];need(b.dag.size()==k,"all preceding DAG coefficients retained");valid_row(b.row,s,b.pivot);
  u32(f,b.pivot);u32(f,b.source);u32(f,b.factor);u32(f,k);
  f.write(reinterpret_cast<const char*>(b.row.data()),b.row.size()*4);
  f.write(reinterpret_cast<const char*>(b.dag.data()),b.dag.size());
 }
 sync_finish(f,t,p);need(fs::file_size(p)==state_size(s),"whole checkpoint byte count and EOF");
}
static void load_state(const fs::path&p,State&s){
 need(s.next==0&&s.basis.empty(),"load into fresh original state");
 std::ifstream f(p,std::ios::binary);need(bool(f),"open verified prior checkpoint");magic(f,"R15WS101");
 need(read_le(f,4)==1&&read_le(f,4)==127&&read_le(f,4)==s.m&&read_le(f,4)==s.n&&read_le(f,4)==s.g,"same checkpoint version and all dimensions");
 s.next=read_le(f,4);uint32_t rank=read_le(f,4);need(read_le(f,4)==uint64_t(s.nw)&&s.next<=s.n&&rank<=s.next,"complete prior column/rank bounds");
 need(fixed(f,64)==s.binding&&fixed(f,64)==s.inputSHA,"same source semantic and complete sparse input SHA");
 s.committed.cancellations=read_le(f,8);s.committed.passes=read_le(f,8);s.committed.words=read_le(f,8);s.committed.normalizations=read_le(f,8);
 auto c=fixed(f,s.n);s.classification.assign(c.begin(),c.end());
 uint32_t indep=0;
 for(uint32_t j=0;j<s.n;j++){
  need(j<s.next?(s.classification[j]==1||s.classification[j]==2):(s.classification[j]==0),"every original prefix column classified, no future column");
  indep+=s.classification[j]==1;
 }need(indep==rank,"all independent prefix labels retained");
 uint32_t previousSource=0;
 for(uint32_t k=0;k<rank;k++){
  Basis b;b.pivot=read_le(f,4);b.source=read_le(f,4);uint32_t v=read_le(f,4);
  need(read_le(f,4)==k&&b.pivot<s.m&&s.at[b.pivot]<0&&b.source<s.next&&
       s.classification[b.source]==1&&(k==0||b.source>previousSource)&&v>0&&v<127,"unique original source/pivot and complete DAG shape");
  previousSource=b.source;b.factor=v;b.row.resize(7*s.nw);
  f.read(reinterpret_cast<char*>(b.row.data()),b.row.size()*4);need(size_t(f.gcount())==b.row.size()*4,"whole bit-plane basis payload");
  auto d=fixed(f,k);b.dag.assign(d.begin(),d.end());
  for(uint8_t z:b.dag)need(z<127,"all DAG coefficients canonical");
  valid_row(b.row,s,b.pivot);s.at[b.pivot]=k;s.basis.push_back(std::move(b));
 }
 need(f.peek()==EOF&&fs::file_size(p)==state_size(s),"whole checkpoint EOF");
}
struct Certificate{
 uint32_t kind=0,pivotRow=UINT32_MAX,readout=0,residualNonzero=0;
 std::vector<uint32_t> pivots;std::vector<uint8_t> values;
};
static Certificate certificate(const State&s,Row r,const Scaled&scaled,const Clock::time_point&deadline){
 need(s.next==s.n,"no target certificate before all original columns");
 std::vector<uint8_t> d(s.basis.size(),0);Counts local;uint32_t p=0;uint64_t steps=0;
 while((p=first_nonzero(r,s,p))<s.m){
  if((steps++&31)==0)tick(deadline);
  int bi=s.at[p];
  if(bi>=0){
   need(d[bi]==0,"one complete target pivot cancellation");int a=127-BitOps::get(r,s.nw,p);d[bi]=a;
   scaled.add(r,s.nw,p/32,s.basis[bi].row,s.nw,p/32,s.nw-p/32,a,local);
   need(BitOps::get(r,s.nw,p)==0,"whole target pivot zero");local.cancellations++;scaled.attempt.cancellations++;
  }p++;
 }
 Certificate c;
 for(const auto&b:s.basis){need(BitOps::get(r,s.nw,b.pivot)==0,"all full target pivot coordinates vanish");c.pivots.push_back(b.pivot);}
 std::sort(c.pivots.begin(),c.pivots.end());
 uint32_t q0=s.m;
 for(uint32_t j=0;j<s.m;j++)if(BitOps::get(r,s.nw,j)){if(q0==s.m)q0=j;c.residualNonzero++;}
 if(q0<s.m){
  need(s.at[q0]<0,"literal residual coordinate is not a pivot");c.kind=1;c.pivotRow=q0;c.values.assign(s.m,0);c.values[q0]=1;
  std::vector<uint32_t> active{q0};uint64_t k=0;
  for(auto it=c.pivots.rbegin();it!=c.pivots.rend();it++){
   if((k++&63)==0)tick(deadline);uint32_t pp=*it;const auto&b=s.basis[s.at[pp]];uint64_t sum=0;
   for(uint32_t q:active)if(q>pp)sum+=uint64_t(c.values[q])*BitOps::get(b.row,s.nw,q);
   uint8_t z=(127-sum%127)%127;c.values[pp]=z;if(z)active.push_back(pp);
  }
  uint32_t value=BitOps::get(r,s.nw,q0);need(value>0,"nonzero original target residual");
  int inv=scaled.ops.inv[value];for(auto&z:c.values)z=int(z)*inv%127;c.readout=1;
  // Independently of arrival order, the constructed row kills every saved basis.
  for(uint32_t k=0;k<s.basis.size();k++){
   if((k&63)==0)tick(deadline);uint64_t z=0;
   for(uint32_t q:active)z+=uint64_t(c.values[q])*BitOps::get(s.basis[k].row,s.nw,q);
   need(z%127==0,"complete constructed left row kills every basis column");
  }
 }else{
  c.kind=2;c.values.assign(s.n,0);std::vector<uint8_t> beta(d.size());
  for(size_t k=0;k<d.size();k++)beta[k]=(127-d[k])%127;
  for(size_t kk=s.basis.size();kk>0;kk--){
   size_t k=kk-1;if((k&63)==0)tick(deadline);const auto&b=s.basis[k];
   int gamma=int(beta[k])*scaled.ops.inv[b.factor]%127;
   c.values[b.source]=(c.values[b.source]+gamma)%127;
   if(gamma)for(size_t j=0;j<k;j++)beta[j]=(beta[j]+gamma*int(b.dag[j]))%127;
  }
 }
 return c;
}
static void save_certificate(const fs::path&p,const State&s,const Certificate&c){
 need((c.kind==1&&c.values.size()==s.m&&c.readout==1)||(c.kind==2&&c.values.size()==s.n&&c.readout==0),"whole certificate vector shape");
 auto t=p;t+=".tmp";std::ofstream f(t,std::ios::binary);f.write("R15WC101",8);
 for(uint32_t v:{1u,127u,s.m,s.n,c.kind,uint32_t(s.basis.size()),s.next,c.pivotRow,c.readout,uint32_t(c.values.size())})u32(f,v);
 f.write(s.binding.data(),64);f.write(s.inputSHA.data(),64);
 for(uint32_t q:c.pivots)u32(f,q);
 f.write(reinterpret_cast<const char*>(c.values.data()),c.values.size());sync_finish(f,t,p);
 need(fs::file_size(p)==176+4ull*c.pivots.size()+c.values.size(),"complete certificate EOF");
}
static uint64_t scaled_test(const BitOps&ops){
 Counts attempt;Scaled sc(ops,attempt);uint64_t tests=0;
 for(int scalar=1;scalar<127;scalar++)for(int a=0;a<127;a++)for(int start=0;start<127;start+=32){
  Row r(21),q(28);Counts local;
  for(int lane=0;lane<32;lane++){BitOps::set(r,3,32+lane,a);BitOps::set(q,4,64+lane,(start+lane)%127);BitOps::set(r,3,lane,17);BitOps::set(r,3,64+lane,29);}
  sc.add(r,3,1,q,4,2,1,scalar,local);
  for(int lane=0;lane<32;lane++){
   need(BitOps::get(r,3,32+lane)==(a+scalar*((start+lane)%127))%127&&
        BitOps::get(r,3,lane)==17&&BitOps::get(r,3,64+lane)==29,"all independent signed-scalar, stride and padding products");tests++;
  }
 }
 return tests;
}
static Row scalar_row(const std::vector<int>&v,int nw){Row r(7*nw,0);for(size_t i=0;i<v.size();i++)BitOps::set(r,nw,i,v[i]);return r;}
static std::vector<uint8_t> expand_basis(const State&s,size_t which,const BitOps&ops){
 std::vector<uint8_t> beta(s.basis.size(),0),out(s.n,0);beta[which]=1;
 for(size_t kk=which+1;kk>0;kk--){
  size_t k=kk-1;const auto&b=s.basis[k];int a=int(beta[k])*ops.inv[b.factor]%127;
  out[b.source]=(out[b.source]+a)%127;
  for(size_t j=0;j<k;j++)beta[j]=(beta[j]+a*int(b.dag[j]))%127;
 }return out;
}
static uint64_t tiny_test(const BitOps&ops,const fs::path&out){
 std::vector<std::vector<int>> a={
  {0,0,1,4,0,0,2},{1,0,2,0,3,0,1},{2,0,5,4,6,0,4},
  {0,1,0,4,5,2,1},{0,0,0,0,0,0,0},{0,0,0,0,1,2,0},
  {0,1,3,16,6,4,7}};
 Counts count;Scaled sc(ops,count);auto dl=Clock::now()+std::chrono::hours(1);
 State full(7,7,0,std::string(64,'0'),std::string(64,'1'));
 for(uint32_t j=0;j<7;j++)insert_column(full,scalar_row(a[j],full.nw),j,sc,dl);
 need(full.basis.size()==4,"known independent tiny rank");
 uint64_t tests=0;
 for(size_t k=0;k<full.basis.size();k++){
  auto c=expand_basis(full,k,ops);
  for(int i=0;i<7;i++){int z=0;for(int j=0;j<7;j++)z=(z+c[j]*a[j][i])%127;
   need(z==BitOps::get(full.basis[k].row,full.nw,i),"all original tiny basis-source coordinates");tests++;}
 }
 State prefix(7,7,0,std::string(64,'0'),std::string(64,'1'));
 for(uint32_t j=0;j<4;j++)insert_column(prefix,scalar_row(a[j],prefix.nw),j,sc,dl);
 fs::create_directories(out);auto cp=out/"tiny-whole-column-checkpoint.bin";
 need(!fs::exists(cp),"fresh self-test output directory");save_state(cp,prefix);
 State resumed(7,7,0,std::string(64,'0'),std::string(64,'1'));load_state(cp,resumed);
 for(uint32_t j=4;j<7;j++)insert_column(resumed,scalar_row(a[j],resumed.nw),j,sc,dl);
 need(resumed.classification==full.classification&&resumed.basis.size()==full.basis.size(),"same complete resumed tiny classification");
 for(size_t k=0;k<full.basis.size();k++){
  const auto&x=full.basis[k];const auto&y=resumed.basis[k];
  need(x.pivot==y.pivot&&x.source==y.source&&x.factor==y.factor&&x.row==y.row&&x.dag==y.dag,"same whole resumed tiny source and bitplanes");
 }
 std::vector<int> pos(7),neg(7,0);neg[6]=1;
 for(int i=0;i<7;i++)pos[i]=(a[0][i]+3*a[3][i]+5*a[5][i])%127;
 auto c=certificate(full,scalar_row(pos,full.nw),sc,dl);need(c.kind==2,"true tiny positive");
 for(int i=0;i<7;i++){int z=0;for(int j=0;j<7;j++)z=(z+c.values[j]*a[j][i])%127;need(z==pos[i],"all tiny positive original products");tests++;}
 c=certificate(full,scalar_row(neg,full.nw),sc,dl);need(c.kind==1,"true tiny negative");
 for(int j=0;j<7;j++){int z=0;for(int i=0;i<7;i++)z=(z+c.values[i]*a[j][i])%127;need(z==0,"all tiny left original columns");tests++;}
 need(c.values[6]==1,"tiny normalized target readout");tests++;
 return tests;
}
int main(int argc,char**argv){
 auto started=Clock::now();int code=1;std::string error,status="failed",binding,inputSHA,stateFile,certFile,resume;
 uint32_t initial=0,complete=0,rank=0,generation=0,kind=0,residual=0;Counts attempt,committed;
 uint64_t oldChecks=0,scaledChecks=0,tinyChecks=0;bool allInput=false,stateWritten=false,certWritten=false;
 fs::path out;double seconds=0;
 try{
  host();BitOps ops;oldChecks=ops.verify();scaledChecks=scaled_test(ops);
  if(argc==3&&std::string(argv[1])=="--selftest"){
   out=argv[2];tinyChecks=tiny_test(ops,out);
   std::cout<<"{\"format\":\""<<FORMAT<<"-selftest\",\"allComplete\":true,\"oldExhaustiveChecks\":"<<oldChecks
    <<",\"signedScalarChecks\":"<<scaledChecks<<",\"tinyOriginalProducts\":"<<tinyChecks
    <<",\"checkpointRoundtrip\":true}"<<std::endl;return 0;
  }
  need(argc==7,"input out seconds inputSHA generation verified-resume-state-or-dash");
  fs::path input=argv[1];out=argv[2];seconds=std::stod(argv[3]);inputSHA=argv[4];generation=std::stoul(argv[5]);resume=argv[6];
  need(seconds>=120&&seconds<=1800&&hex64(inputSHA)&&generation>0&&generation<10000,"bounded full-column execution and exact identities");
  fs::create_directories(out);
  auto deadline=started+std::chrono::duration_cast<Clock::duration>(std::chrono::duration<double>(seconds-60));
  Input original(input);binding=original.binding;original.validate_all();allInput=true;
  State s(original.m,original.n,original.g,binding,inputSHA);
  if(resume!="-")load_state(resume,s);initial=s.next;complete=initial;rank=s.basis.size();committed=s.committed;
  Scaled sc(ops,attempt);bool paused=false;
  try{
   while(s.next<s.n){tick(deadline);auto r=original.column(s.next);insert_column(s,std::move(r),s.next,sc,deadline);}
  }catch(const Budget&){paused=true;}
  complete=s.next;rank=s.basis.size();committed=s.committed;
  if(s.next>initial){
   stateFile=name("whole-column-state",generation,".bin");save_state(out/stateFile,s);stateWritten=true;
  }
  if(!paused&&s.next==s.n){
   try{
    tick(deadline);auto c=certificate(s,original.target_row(),sc,deadline);kind=c.kind;residual=c.residualNonzero;
    certFile=name("whole-original-certificate",generation,".bin");save_certificate(out/certFile,s,c);certWritten=true;
   }catch(const Budget&){paused=true;}
  }
  code=certWritten?0:75;status=certWritten?"completed-candidate":"budget-checkpoint";
 }catch(const std::exception&e){error=e.what();code=1;status="failed";}
 struct rusage ru{};getrusage(RUSAGE_SELF,&ru);
 std::ostringstream z;z<<std::setprecision(17);
 z<<"{\"format\":"<<quote(FORMAT)<<",\"binding\":"<<quote(binding)<<",\"inputSHA256\":"<<quote(inputSHA)
  <<",\"status\":"<<quote(status)<<",\"exitCode\":"<<code<<",\"generation\":"<<generation
  <<",\"all77276OutputsRetained\":"<<(allInput?"true":"false")<<",\"all13808SourceLabelsRetained\":"<<(allInput?"true":"false")
  <<",\"allOriginalSparseInputTermsVerified\":"<<(allInput?"true":"false")
  <<",\"initialCompleteColumns\":"<<initial<<",\"completeColumns\":"<<complete<<",\"rank\":"<<rank
  <<",\"newCompleteColumns\":"<<(complete>=initial?complete-initial:0)<<",\"allColumnsProcessed\":"<<(complete==N0?"true":"false")
  <<",\"stateWritten\":"<<(stateWritten?"true":"false")<<",\"stateFile\":"<<quote(stateFile)
  <<",\"certificateWritten\":"<<(certWritten?"true":"false")<<",\"certificateFile\":"<<quote(certFile)
  <<",\"certificateKind\":"<<kind<<",\"targetResidualNonzeroCoordinates\":"<<residual
  <<",\"committedCancellations\":"<<committed.cancellations<<",\"committedScalarPasses\":"<<committed.passes
  <<",\"committedWordPasses\":"<<committed.words<<",\"attemptCancellations\":"<<attempt.cancellations
  <<",\"attemptScalarPasses\":"<<attempt.passes<<",\"attemptWordPasses\":"<<attempt.words
  <<",\"oldExhaustiveChecks\":"<<oldChecks<<",\"signedScalarChecks\":"<<scaledChecks
  <<",\"positiveOriginalSourceClaimed\":false,\"originalIdealNonmembershipClaimed\":false"
  <<",\"elapsedSeconds\":"<<std::chrono::duration<double>(Clock::now()-started).count()
  <<",\"peakRssKiB\":"<<ru.ru_maxrss<<",\"error\":"<<quote(error)<<"}";
 if(!out.empty()&&generation){
  try{auto p=out/name("native-receipt",generation,".json"),t=p;t+=".tmp";std::ofstream f(t);f<<z.str();sync_finish(f,t,p);}
  catch(const std::exception&e){std::cerr<<"receipt persistence: "<<e.what()<<std::endl;return 1;}
 }
 std::cout<<z.str()<<std::endl;return code;
}
