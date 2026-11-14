// Exact F31 normal form of the actual second original H0 residual, B=86.
// The original constant prebasis and replayable operations are reconstructed unchanged.
// The fixed m-degree constant leading blocks are reduced backwards, but their
// lower-degree parameter tails are never reduced while constructing the basis.
// All transformations and all normal-form reductions have replayable sources.
// Usage: PROGRAM ORIGINAL_MODEL ORIGINAL_RHS OUT_PREFIX
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
#include <sys/resource.h>
using Row = std::vector<uint32_t>;
using Triple = std::array<Row,3>;
struct Rep {int c=0,rot=0,neg=0;};
struct Source {int e=0,raw=0; uint64_t mult=0,pivot=0;};
static void u32(std::ostream &o,uint32_t x){for(int j=0;j<4;j++)o.put(char(x>>(8*j)));}
static void u16(std::ostream &o,uint16_t x){o.put(char(x));o.put(char(x>>8));}
static int degree(uint64_t k){int d=0;while(k){d+=k%8;k/=8;}return d;}
struct BitOps {
 std::array<Rep,31> rep;
 std::array<int,31> inv{};
 BitOps(){
  for(int c=0;c<3;c++)for(int r=0;r<5;r++)for(int n=0;n<2;n++){
   int v=((std::array<int,3>{1,3,5}[c]*(1<<r)*(n?-1:1))%31+31)%31;
   rep[v]={c,r,n};
  }
  for(int i=1;i<31;i++)for(int j=1;j<31;j++)if(i*j%31==1)inv[i]=j;
 }
 static int get(const Row &r,int nw,int bit){
  int v=0;for(int b=0;b<5;b++)v|=((r[b*nw+bit/32]>>(bit%32))&1)<<b;return v;
 }
 static void set(Row &r,int nw,int bit,int v){
  v=(v%31+31)%31;for(int b=0;b<5;b++)if(v&(1<<b))r[b*nw+bit/32]|=uint32_t(1)<<(bit%32);
 }
 // The source and destination blocks may have different strides. Offsets and
 // lengths are in 32-entry words, so polynomial-degree shifts remain exact.
 static void add(Row &r,int rw,int ro,const Row &q,int qw,int qo,int len,int rot,int neg){
  int off[5];for(int j=0;j<5;j++)off[j]=((j-rot+5)%5)*qw+qo;
  const uint32_t mask=neg?UINT32_MAX:0;
  for(int w=0;w<len;w++){
   const int z=ro+w;
   uint32_t a0=r[z],a1=r[rw+z],a2=r[2*rw+z],a3=r[3*rw+z],a4=r[4*rw+z];
   uint32_t b0=q[off[0]+w]^mask,b1=q[off[1]+w]^mask,b2=q[off[2]+w]^mask,b3=q[off[3]+w]^mask,b4=q[off[4]+w]^mask;
   uint32_t s0=a0^b0,c=a0&b0,x=a1^b1,s1=x^c;c=(a1&b1)|(x&c);
   x=a2^b2;uint32_t s2=x^c;c=(a2&b2)|(x&c);x=a3^b3;uint32_t s3=x^c;c=(a3&b3)|(x&c);
   x=a4^b4;uint32_t s4=x^c;c=(a4&b4)|(x&c);
   uint32_t t=s0^c;c&=s0;s0=t;t=s1^c;c&=s1;s1=t;t=s2^c;c&=s2;s2=t;t=s3^c;c&=s3;s3=t;s4^=c;
   uint32_t keep=~(s0&s1&s2&s3&s4);
   r[z]=s0&keep;r[rw+z]=s1&keep;r[2*rw+z]=s2&keep;r[3*rw+z]=s3&keep;r[4*rw+z]=s4&keep;
  }
 }
 void multiple(Row &r,int nw,int first,int a) const {
  const Rep R=rep[a];
  if(R.c){Row tmp=r;add(r,nw,first,tmp,nw,first,nw-first,R.c==1?1:2,0);}
  for(int w=first;w<nw;w++){
   uint32_t x[5],nz=0;for(int b=0;b<5;b++){x[b]=r[((b-R.rot+5)%5)*nw+w];nz|=x[b];}
   for(int b=0;b<5;b++)r[b*nw+w]=x[b]^(R.neg?nz:0);
  }
 }
 static void refresh(Triple &t,int nw,int first){
  t[1]=t[0];t[2]=t[0];add(t[1],nw,first,t[0],nw,first,nw-first,1,0);add(t[2],nw,first,t[0],nw,first,nw-first,2,0);
 }
};
struct Phase {
 int d=0,hi=0,lo=0,hw=0,lw=0,nw=0;
 std::vector<std::unique_ptr<Triple>> basis;
 std::vector<int> id,pivots;
 std::unordered_map<uint64_t,int> highIndex,lowIndex;
};
struct PolynomialRow {
 int top=0,initialParameterDegree=0;
 std::array<int,6> levels{},stride{},nw{};
 std::array<Row,6> row;
 PolynomialRow(int t,int pd,const std::vector<std::vector<uint64_t>> &mon):top(t),initialParameterDegree(pd){
  for(int d=1;d<=top;d++){
   levels[d]=pd+10*(top-d)+1;stride[d]=(mon[d].size()+31)/32;nw[d]=levels[d]*stride[d];row[d].resize(5*nw[d]);
  }
 }
};
struct NormalOp {uint16_t basis;uint8_t exponent,coefficient;};
int main(int argc,char **argv){try{
 if(argc!=4)return 2;const bool rref=true;
 auto start=std::chrono::steady_clock::now();auto seconds=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 std::ifstream in(argv[1]);std::string magic;in>>magic;if(magic!="R150_NATIVE_NF_V1")throw std::runtime_error("input header");
 std::array<std::array<int,66>,11> Q{};std::array<std::array<std::array<int,11>,11>,11> L{};
 for(int e=0;e<11;e++){for(auto &v:Q[e])in>>v;for(auto &v:L[e])for(auto &a:v)in>>a;}
 int count;in>>count;if(count!=3333)throw std::runtime_error("prebasis count");std::vector<Source> selected(count);
 for(auto &s:selected)in>>s.e>>s.mult>>s.pivot>>s.raw;
 std::array<std::array<std::array<int,6>,66>,6> G{};for(auto &g:G)for(auto &p:g)for(auto &a:p)in>>a;
 int ns,nt;in>>ns>>nt;if(ns<0||ns>2195||nt<0||nt>9)throw std::runtime_error("source count");
 std::vector<Source> sources(ns);for(auto &s:sources)in>>s.e>>s.mult>>s.raw;
 std::vector<int> targets(nt);for(auto &j:targets){in>>j;if(j<2||j>10)throw std::runtime_error("target number");}if(!in||ns!=2195||nt!=9)throw std::runtime_error("truncated or incomplete original input");
 ns=0;
 std::string prefix=argv[3];std::ofstream fwd(prefix+"-forward.bin",std::ios::binary),back(prefix+"-backward.bin",std::ios::binary),nfops(prefix+"-reduction.bin",std::ios::binary),out(prefix+"-normal-forms.bin",std::ios::binary);
 if(!fwd||!back||!nfops||!out)throw std::runtime_error("output open");
 fwd.write("R150PB31",8);u32(fwd,3333);back.write("R150RJ31",8);u32(back,rref?3333:0);
 nfops.write("R150NR31",8);u32(nfops,ns+nt);out.write("R150NF31",8);u32(out,ns);u32(out,nt);u32(out,1034);
 std::array<uint64_t,11> var;var[0]=1;for(int i=1;i<11;i++)var[i]=8*var[i-1];
 std::vector<std::vector<uint64_t>> mon(6);
 auto enumerate=[&](auto&&self,int left,int lo,uint64_t key,int d)->void{if(!left){mon[d].push_back(key);return;}for(int i=lo;i<11;i++)self(self,left-1,i,key+var[i],d);};
 for(int d=0;d<=5;d++)enumerate(enumerate,d,0,0,d);
 std::array<std::unordered_map<uint64_t,int>,6> local;std::unordered_map<uint64_t,int> component;
 for(int d=1;d<=5;d++)for(int j=0;j<int(mon[d].size());j++)local[d][mon[d][j]]=j;
 std::array<Phase,6> phases;BitOps ops;int generated=0;uint64_t forwardCount=0,backwardCount=0,normalCount=0;
 std::vector<std::pair<int,int>> quadratic;for(int i=0;i<11;i++)for(int j=i;j<11;j++)quadratic.push_back({i,j});
 for(int d=2;d<=5;d++){
  auto &P=phases[d];P.d=d;P.hi=mon[d].size();P.lo=mon[d-1].size();P.hw=(P.hi+31)/32;P.lw=(P.lo+31)/32;P.nw=P.hw+11*P.lw;P.basis.resize(P.hi);P.id.resize(P.hi);P.highIndex=local[d];P.lowIndex=local[d-1];
  for(const auto &s:selected){if(degree(s.mult)+2!=d)continue;if(s.e<0||s.e>=11)throw std::runtime_error("not an N source");
   Row row(5*P.nw);for(int k=0;k<66;k++){auto [a,b]=quadratic[k];BitOps::set(row,P.nw,P.highIndex.at(s.mult+var[a]+var[b]),Q[s.e][k]);}
   for(int v=0;v<11;v++)for(int k=0;k<11;k++)BitOps::set(row,P.nw,(P.hw+k*P.lw)*32+P.lowIndex.at(s.mult+var[v]),L[s.e][v][k]);
   std::vector<std::pair<uint16_t,uint8_t>> reduction;int pivot=-1,value=0;
   for(int c=0;c<P.hi;c++){
    const int a=BitOps::get(row,P.nw,c);if(!a)continue;if(!P.basis[c]){pivot=c;value=a;break;}
    reduction.push_back({uint16_t(P.id[c]),uint8_t(a)});auto R=ops.rep[31-a];const int w=c/32;BitOps::add(row,P.nw,w,(*P.basis[c])[R.c],P.nw,w,P.nw-w,R.rot,R.neg);forwardCount++;
   }
   if(pivot<0||mon[d][pivot]!=s.pivot)throw std::runtime_error("original profile pivot mismatch");
   int scale=ops.inv[value];if(value!=1)ops.multiple(row,P.nw,pivot/32,scale);if(BitOps::get(row,P.nw,pivot)!=1)throw std::runtime_error("unit pivot failed");
   generated++;P.id[pivot]=generated;P.pivots.push_back(pivot);
   u32(fwd,s.raw);fwd.put(char(scale));u32(fwd,reduction.size());for(auto [i,a]:reduction){u16(fwd,i);fwd.put(char(a));}
   auto t=std::make_unique<Triple>();(*t)[0]=std::move(row);BitOps::refresh(*t,P.nw,pivot/32);P.basis[pivot]=std::move(t);
  }
  std::sort(P.pivots.begin(),P.pivots.end());
  std::cout<<"{\"phase\":\"forward-prebasis\",\"mDegree\":"<<d<<",\"pivots\":"<<P.pivots.size()<<",\"operations\":"<<forwardCount<<",\"elapsedSeconds\":"<<seconds()<<"}\n"<<std::flush;
  if(rref){
   for(int ii=int(P.pivots.size())-1;ii>=0;ii--){int c=P.pivots[ii];auto &t=*P.basis[c];std::vector<std::pair<uint16_t,uint8_t>> reduction;
    for(int jj=ii+1;jj<int(P.pivots.size());jj++){int q=P.pivots[jj],a=BitOps::get(t[0],P.nw,q);if(!a)continue;reduction.push_back({uint16_t(P.id[q]),uint8_t(a)});auto R=ops.rep[31-a];int w=q/32;BitOps::add(t[0],P.nw,w,(*P.basis[q])[R.c],P.nw,w,P.nw-w,R.rot,R.neg);backwardCount++;}
    BitOps::refresh(t,P.nw,c/32);u16(back,P.id[c]);u32(back,reduction.size());for(auto [j,a]:reduction){u16(back,j);back.put(char(a));}
   }
   for(int c:P.pivots)for(int q:P.pivots)if(BitOps::get((*P.basis[c])[0],P.nw,q)!=(c==q))throw std::runtime_error("constant block RREF failed");
   std::cout<<"{\"phase\":\"same-degree-rref\",\"mDegree\":"<<d<<",\"operations\":"<<backwardCount<<",\"elapsedSeconds\":"<<seconds()<<"}\n"<<std::flush;
  }
 }
 if(generated!=3333)throw std::runtime_error("incomplete prebasis");int nc=0;
 for(int d=5;d>=1;d--)for(int j=0;j<int(mon[d].size());j++)if(d==1||!phases[d].basis[j])component[mon[d][j]]=++nc;
 if(nc!=1034)throw std::runtime_error("quotient components");
 auto coefficient=[&](PolynomialRow &r,int d,uint64_t key,int k,int a){if(k<0||k>=r.levels[d])throw std::runtime_error("parameter degree overflow");BitOps::set(r.row[d],r.nw[d],(k*r.stride[d])*32+local[d].at(key),a);};
 auto normal=[&](PolynomialRow &r,int source,int target,int ordinal){
  std::vector<NormalOp> trace;
  for(int d=r.top;d>=2;d--){auto &P=phases[d];
   for(int c:P.pivots)for(int k=0;k<r.levels[d];k++){
    int a=BitOps::get(r.row[d],r.nw[d],k*r.stride[d]*32+c);if(!a)continue;
    trace.push_back({uint16_t(P.id[c]),uint8_t(k),uint8_t(a)});auto R=ops.rep[31-a];const auto &b=(*P.basis[c])[R.c];int w=c/32;
    BitOps::add(r.row[d],r.nw[d],k*r.stride[d]+w,b,P.nw,w,P.hw-w,R.rot,R.neg);
    if(k+11>r.levels[d-1])throw std::runtime_error("lower degree overflow");
    BitOps::add(r.row[d-1],r.nw[d-1],k*r.stride[d-1],b,P.nw,P.hw,11*P.lw,R.rot,R.neg);
   }
   for(int c:P.pivots)for(int k=0;k<r.levels[d];k++)if(BitOps::get(r.row[d],r.nw[d],k*r.stride[d]*32+c))throw std::runtime_error("normal form retained a pivot");
  }
  normalCount+=trace.size();u32(nfops,source);u16(nfops,target);u32(nfops,trace.size());for(auto a:trace){u16(nfops,a.basis);nfops.put(char(a.exponent));nfops.put(char(a.coefficient));}
  struct Entry {int component;std::vector<uint8_t> coefficients;};std::vector<Entry> entries;int maxdegree=-1;uint64_t ncoeff=0;
  for(int d=r.top;d>=1;d--)for(int c=0;c<int(mon[d].size());c++){
   auto ix=component.find(mon[d][c]);if(ix==component.end())continue;std::vector<uint8_t> co(r.levels[d]);
   for(int k=0;k<r.levels[d];k++)co[k]=BitOps::get(r.row[d],r.nw[d],k*r.stride[d]*32+c);
   while(!co.empty()&&!co.back())co.pop_back();if(co.empty())continue;maxdegree=std::max(maxdegree,int(co.size())-1);for(auto a:co)ncoeff+=a!=0;entries.push_back({ix->second,std::move(co)});
  }
  u32(out,source);u16(out,target);u32(out,entries.size());for(auto &e:entries){u16(out,e.component);out.put(char(e.coefficients.size()));out.write(reinterpret_cast<const char*>(e.coefficients.data()),e.coefficients.size());}
  std::cout<<"{\"phase\":\"normal-form\",\"sourceRow\":"<<source<<",\"target\":"<<target<<",\"mDegree\":"<<r.top<<",\"parameterDegree\":"<<maxdegree<<",\"nonzeroComponents\":"<<entries.size()<<",\"nonzeroCoefficients\":"<<ncoeff<<",\"rowReductions\":"<<trace.size()<<",\"elapsedSeconds\":"<<seconds()<<"}\n"<<std::flush;
 };
 std::ifstream rhs(argv[2],std::ios::binary);if(!rhs)throw std::runtime_error("RHS input open");
 auto readUnsigned=[&](int bytes)->uint64_t{uint64_t x=0;for(int k=0;k<bytes;k++){int a=rhs.get();if(a<0)throw std::runtime_error("truncated original RHS");x|=uint64_t(a)<<(8*k);}return x;};
 char rmagic[8];rhs.read(rmagic,8);if(std::string(rmagic,8)!="R150RH31"||readUnsigned(4)!=86||readUnsigned(4)!=9||readUnsigned(4)!=4367||readUnsigned(4)!=223399)throw std::runtime_error("original weighted RHS dimensions");
 std::vector<PolynomialRow> right;for(int j=0;j<9;j++)right.emplace_back(5,46,mon);
 uint64_t inputNonzero=0;int coordinates=0,components=0;
 for(int d=5;d>=1;d--)for(uint64_t key:mon[d]){
  uint64_t actualKey=readUnsigned(8);int width=readUnsigned(2);if(actualKey!=key||width!=87-10*(d-1))throw std::runtime_error("original RHS monomial dictionary or weight");coordinates+=width;components++;
  for(int j=0;j<9;j++)for(int k=0;k<width;k++){int a=rhs.get();if(a<0||a>30)throw std::runtime_error("original RHS field coefficient");if(a){coefficient(right[j],d,key,k,a);inputNonzero++;}}
 }
 if(rhs.get()!=EOF||coordinates!=223399||components!=4367)throw std::runtime_error("incomplete original RHS");
 for(int j=0;j<9;j++)normal(right[j],0,j+2,j+1);
 fwd.close();back.close();nfops.close();out.close();if(!fwd||!back||!nfops||!out)throw std::runtime_error("output failure");
 struct rusage usage{};getrusage(RUSAGE_SELF,&usage);
 std::cout<<"{\"status\":\"h25-second-original-rhs-normal-forms-complete\",\"sources\":"<<ns<<",\"targets\":"<<nt<<",\"components\":1034,\"forwardOperations\":"<<forwardCount<<",\"backwardOperations\":"<<backwardCount<<",\"normalOperations\":"<<normalCount<<",\"originalRHSCost\":86,\"originalRHSNonzeroCoefficients\":"<<inputNonzero<<",\"peakRSSKiB\":"<<usage.ru_maxrss<<",\"elapsedSeconds\":"<<seconds()<<"}\n";
 return 0;
}catch(const std::exception &e){std::cerr<<"ORIGINAL_RHS_NORMAL_FORM_FAILED "<<e.what()<<"\n";return 1;}}
