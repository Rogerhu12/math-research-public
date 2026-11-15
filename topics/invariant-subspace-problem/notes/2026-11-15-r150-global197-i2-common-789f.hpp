// 2026-11-15. Author: ChatGPT (AI), literature_audit.
// Complete original polynomial I_2(A), bounded packed batches; no mathematics is claimed by this source.
// Readers use the original seventeen equations modulo31^3.
#include "2026-11-14-r150-f31-bitplane-789f.hpp"
#include <sys/resource.h>
#include <sstream>
#include <limits>
#include <set>
namespace sb {
static uint64_t get(std::istream &in,int bytes){uint64_t a=0;for(int k=0;k<bytes;k++){int c=in.get();if(c<0)throw std::runtime_error("truncated integer");a|=uint64_t(c)<<(8*k);}return a;}
static void put(std::ostream &out,uint64_t a,int bytes){for(int k=0;k<bytes;k++)out.put(char(a>>(8*k)));}
static std::string tag(std::istream &in){char s[8];in.read(s,8);if(!in)throw std::runtime_error("truncated magic");return std::string(s,8);}
static void tail(std::istream &in){if(in.get()!=EOF)throw std::runtime_error("trailing data");}
static int mod(int64_t a,int p=31){a%=p;return a<0?a+p:a;}
static void scalar(BitOps &ops,Row &dest,int stride,int offset,const Row &src,int ss,int so,int length,int a){if(!a||!length)return;auto r=ops.rep[a];BitOps::add(dest,stride,offset,src,ss,so,length,r.rot,r.neg);if(r.c)BitOps::add(dest,stride,offset,src,ss,so,length,(r.rot+(r.c==1?1:2))%5,r.neg);}
static void assign(Row &r,int stride,int bit,int a){for(int b=0;b<5;b++)r[b*stride+bit/32]&=~(uint32_t(1)<<(bit%32));BitOps::set(r,stride,bit,a);}
static void array(std::ostream &out,const std::vector<int> &v){out<<"[";for(size_t i=0;i<v.size();i++){if(i)out<<",";out<<v[i];}out<<"]";}
struct Model {
 std::array<std::array<int,66>,11> Q{},Qh{};
 std::array<std::array<std::array<int,11>,11>,11> L{},Lh{};
 std::array<std::array<std::array<int,6>,66>,6> G{},Gh{};
 std::vector<Source> pre,sources;std::vector<std::vector<uint64_t>> mon;
 std::vector<uint64_t> multipliers,keys;std::array<uint64_t,11> var{};
 std::unordered_map<uint64_t,int> component;std::vector<std::pair<int,int>> quadratic;
 std::array<int,17> contents{};int denominator=0;std::vector<int> H0;
 explicit Model(const std::string &file){
  std::ifstream in(file);std::string magic;in>>magic;if(magic!="R150_NATIVE_NF_V1")throw std::runtime_error("original model magic");
  auto read=[&](int &a){in>>a;if(!in||a<0||a>30)throw std::runtime_error("model coefficient");};
  for(int e=0;e<11;e++){for(auto &a:Q[e])read(a);for(auto &r:L[e])for(auto &a:r)read(a);}
  int n;in>>n;if(n!=3333)throw std::runtime_error("original prebasis size");pre.resize(n);for(auto &x:pre)in>>x.e>>x.mult>>x.pivot>>x.raw;
  for(auto &r:G)for(auto &p:r)for(auto &a:p)read(a);
  int ns,nt;in>>ns>>nt;if(ns!=2195||nt!=9)throw std::runtime_error("original source count");sources.resize(ns);for(auto &x:sources)in>>x.e>>x.mult>>x.raw;
  for(int j=2;j<=10;j++){in>>n;if(n!=j)throw std::runtime_error("original target label");}if(!in||in>>magic)throw std::runtime_error("original model tail");
  var[0]=1;for(int i=1;i<11;i++)var[i]=8*var[i-1];mon.resize(6);
  auto enumerate=[&](auto&&self,int left,int lower,uint64_t key,int d)->void{if(!left){mon[d].push_back(key);return;}for(int i=lower;i<11;i++)self(self,left-1,i,key+var[i],d);};
  for(int d=0;d<=5;d++)enumerate(enumerate,d,0,0,d);
  for(int d=0;d<=3;d++)multipliers.insert(multipliers.end(),mon[d].begin(),mon[d].end());
  for(int d=5;d>=1;d--)for(auto key:mon[d]){component[key]=keys.size();keys.push_back(key);}
  if(multipliers.size()!=364||keys.size()!=4367)throw std::runtime_error("original monomial dictionary");
  for(int i=0;i<11;i++)for(int j=i;j<11;j++)quadratic.push_back({i,j});
  auto check=[&](const Source &s){if(s.raw<1||s.raw>6188||s.e!=(s.raw-1)%17||s.mult!=multipliers[(s.raw-1)/17])throw std::runtime_error("original row map");};for(auto &s:pre)check(s);for(auto &s:sources)check(s);
 }
 int delta(int raw)const{return 10*(degree(multipliers[(raw-1)/17])+1)+((raw-1)%17<11?0:5);}
 void higher(const std::string &file){
  std::ifstream in(file);std::string magic;in>>magic;if(magic!="R150_ORIGINAL_MOD29791_V1")throw std::runtime_error("original integer model modulo29791");
  in>>denominator;for(auto &a:contents){in>>a;if(a<0||a>=29791||a%31==0)throw std::runtime_error("integer row content unit");}if(denominator<0||denominator>=29791||denominator%31==0)throw std::runtime_error("integer fixed denominator unit");
  auto read=[&](int &a,int b){in>>a;if(!in||a<0||a>=29791||a%31!=b)throw std::runtime_error("integer model exact residue");};
  for(int e=0;e<11;e++){for(int k=0;k<66;k++)read(Qh[e][k],Q[e][k]);for(int v=0;v<11;v++)for(int k=0;k<=10;k++)read(Lh[e][v][k],L[e][v][k]);}
  for(int e=0;e<6;e++)for(int k=0;k<66;k++)for(int d=0;d<=5;d++)read(Gh[e][k][d],G[e][k][d]);
  H0.resize(26);for(auto &a:H0){in>>a;if(!in||a<0||a>=29791)throw std::runtime_error("integer H0 coefficient");}if(in>>magic||H0.back()!=3125)throw std::runtime_error("exact H0 tail");
 }
 void rowHeader(std::istream &in,int r)const{if(get(in,4)!=uint64_t(r)||get(in,1)!=uint64_t((r-1)%17)||get(in,8)!=multipliers[(r-1)/17]||get(in,2)!=uint64_t(delta(r)))throw std::runtime_error("full original6188 source dictionary");}
 void rowHeader(std::ostream &out,int r)const{put(out,r,4);put(out,(r-1)%17,1);put(out,multipliers[(r-1)/17],8);put(out,delta(r),2);}
};
struct NF {int count=0,bound=0;std::vector<int> labels;std::vector<std::vector<std::vector<uint8_t>>> rows;};
static NF readNF(const std::string &file){
 std::ifstream in(file,std::ios::binary);auto t=tag(in);bool wide=t=="R150NX31";if(!wide&&t!="R150NF31")throw std::runtime_error("NF magic");if(get(in,4))throw std::runtime_error("RHS-only NF required");NF n;n.count=get(in,4);if(n.count<1||n.count>202||get(in,4)!=1034)throw std::runtime_error("NF dimensions");n.rows.resize(n.count,std::vector<std::vector<uint8_t>>(1034));
 for(int j=0;j<n.count;j++){if(get(in,4))throw std::runtime_error("RHS raw mapping");n.labels.push_back(get(in,2));int count=get(in,4),previous=0;if(count<0||count>1034)throw std::runtime_error("NF entry count");for(int e=0;e<count;e++){int c=get(in,2),len=get(in,wide?2:1);if(c<=previous||c>1034||len<1||len>800)throw std::runtime_error("NF polynomial dictionary");previous=c;auto &p=n.rows[j][c-1];p.resize(len);for(auto &a:p){a=get(in,1);if(a>30)throw std::runtime_error("NF field coefficient");}if(!p.back())throw std::runtime_error("NF trailing zero");n.bound=std::max(n.bound,len-1);}}
 tail(in);return n;
}
static void writeNF(const std::string &file,const std::vector<Row> &v,const std::vector<int> &labels,int N){
 constexpr int W=33;int stride=(N+1)*W;bool wide=N>=255;std::ofstream out(file,std::ios::binary);out.write(wide?"R150NX31":"R150NF31",8);put(out,0,4);put(out,v.size(),4);put(out,1034,4);
 for(size_t j=0;j<v.size();j++){std::vector<std::pair<int,std::vector<uint8_t>>> entries;for(int c=0;c<1034;c++){std::vector<uint8_t> p(N+1);for(int d=0;d<=N;d++)p[d]=BitOps::get(v[j],stride,d*W*32+c);while(!p.empty()&&!p.back())p.pop_back();if(!p.empty())entries.push_back({c+1,std::move(p)});}put(out,0,4);put(out,labels[j],2);put(out,entries.size(),4);for(auto &e:entries){put(out,e.first,2);put(out,e.second.size(),wide?2:1);out.write(reinterpret_cast<const char*>(e.second.data()),e.second.size());}}
 out.close();if(!out)throw std::runtime_error("NF write failed");
}
struct MixFamily {std::string nf,quot,rem,trace;int count=0;std::vector<int> labels;std::vector<std::vector<std::vector<int>>> poly;};
struct Mix {
 int count=0,bound=0;std::vector<int> labels;std::vector<MixFamily> families;
 explicit Mix(const std::string &file){
  std::ifstream in(file);std::string magic;int nf;in>>magic>>count>>bound>>nf;if(magic!="R150_RHS_MIX_V1"||count<1||count>31||bound<40||bound>700||nf<1||nf>8)throw std::runtime_error("RHS mixture header");labels.resize(count);for(auto &a:labels){in>>a;if(a<1||a>65535)throw std::runtime_error("mixture output label");}
  families.resize(nf);for(auto &f:families){in>>f.nf>>f.quot>>f.rem>>f.trace>>f.count;if(f.count<1||f.count>202)throw std::runtime_error("mixture family count");f.labels.resize(f.count);for(auto &a:f.labels)in>>a;f.poly.resize(f.count,std::vector<std::vector<int>>(count));for(auto &row:f.poly)for(auto &p:row){int n;in>>n;if(n<0||n>316)throw std::runtime_error("mixture coefficient degree");p.resize(n);for(auto &a:p){int64_t b;in>>b;a=mod(b);}if(n&&!p.back())throw std::runtime_error("noncanonical mixture polynomial");}}
  if(!in||in>>magic)throw std::runtime_error("RHS mixture tail");
 }
};
struct ImageRow {Row row;int degree=0,stride=0,originalLC=0;};
static std::vector<std::unique_ptr<ImageRow>> graphImage(const std::string &file,BitOps &ops){
 std::ifstream in(file,std::ios::binary);if(tag(in)!="R150GG31")throw std::runtime_error("graph magic");std::vector<int> dims;for(int i=0;i<9;i++)dims.push_back(get(in,4));if(dims!=std::vector<int>{2195,1034,2195,96,8,2195,2195,6,1})throw std::runtime_error("complete T96 graph dimensions");
 const std::array<int,6> count{1034,6,66,396,11,1716},shift{0,-81,-71,-61,-56,-51};std::array<int,6> words{};int off=0,comp=0;std::vector<bool> dictionary(2195);
 for(int g=0;g<6;g++){int s=int32_t(get(in,4)),c=get(in,4),w=get(in,4),l=get(in,4),o=get(in,4),cc=get(in,4);if(s!=shift[g]||c!=count[g]||w!=(c+31)/32||l!=9-s||o!=off||cc!=comp)throw std::runtime_error("actual graph groups");words[g]=w;off+=w*l;comp+=c;if(g)for(int j=0;j<c;j++){int ix=get(in,4)-1,raw=get(in,4);if(ix<0||ix>=2195||dictionary[ix]||raw<1||raw>6188)throw std::runtime_error("graph original dictionary");dictionary[ix]=true;}}
 if(off!=4842||comp!=3229)throw std::runtime_error("graph profile");std::vector<std::unique_ptr<ImageRow>> piv(1034);std::vector<bool> seen(3229);int outputs=0,kernels=0,sum=0,ksum=0;
 for(int r=0;r<2195;r++){int c=get(in,2)-1,d=int32_t(get(in,4)),lc=get(in,1);if(c<0||c>=3229||seen[c]||d<-81||d>8||lc<1||lc>30)throw std::runtime_error("graph row header");seen[c]=true;std::unique_ptr<ImageRow> p;if(c<1034){if(d<0)throw std::runtime_error("negative output degree");p=std::make_unique<ImageRow>();p->degree=d;p->stride=(d+1)*33;p->originalLC=lc;p->row.resize(5*p->stride);}
  for(int g=0;g<6;g++){int l=get(in,2);if(l!=std::max(0,d-shift[g]+1))throw std::runtime_error("graph actual row layer");size_t bytes=size_t(5)*l*words[g]*4;if(g==0){if(p)in.read(reinterpret_cast<char*>(p->row.data()),bytes);else{Row zero(bytes/4);in.read(reinterpret_cast<char*>(zero.data()),bytes);for(auto a:zero)if(a)throw std::runtime_error("source-leading nonkernel");}}else in.seekg(bytes,std::ios::cur);if(!in)throw std::runtime_error("truncated complete graph");}
  if(p){int hd=-1,hc=-1;for(int dd=d;dd>=0&&hc<0;dd--)for(int w=0;w<33;w++){uint32_t nz=0;for(int b=0;b<5;b++)nz|=p->row[b*p->stride+dd*33+w];if(nz){hd=dd;hc=32*w+__builtin_ctz(nz);break;}}if(hd!=d||hc!=c||BitOps::get(p->row,p->stride,d*33*32+c)!=lc)throw std::runtime_error("actual image head");if(lc!=1)ops.multiple(p->row,p->stride,0,ops.inv[lc]);piv[c]=std::move(p);outputs++;sum+=d;}else{kernels++;ksum+=d+96;}
 }
 tail(in);if(outputs!=1021||kernels!=1174||sum!=716||ksum!=60050)throw std::runtime_error("complete graph image certificate profile");return piv;
}
}
