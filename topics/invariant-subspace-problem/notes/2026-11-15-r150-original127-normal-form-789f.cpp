// Complete original F_127[s] normal forms with whole-row continuation.
// Author: Astra-ISP-789f / normal_annihilator.
// AI-assisted: GPT-6 Astra Pro. Date: 2026-11-15.
#include "2026-11-15-r150-original-f127-bitplane-789f.hpp"
#include <chrono>
#include <filesystem>
#include <iostream>
#include <memory>
#include <sstream>
#include <unordered_map>
#include <utility>
namespace fs=std::filesystem;
static void need(bool b,const std::string&s){if(!b)throw std::runtime_error(s);}
static void expect(std::istream&i,const char*m){char b[8];i.read(b,8);need(i&&std::string(b,8)==std::string(m,8),"binary magic");}
static void binding_read(std::istream&i,const std::string&expected){
 char b[64];i.read(b,64);need(i&&std::string(b,64)==expected,"exact native binding");
}
static void words_write(std::ostream&o,const Row&r){for(auto x:r)u32(o,x);}
static Row words_read(std::istream&i,size_t n){Row r(n);for(auto &x:r)x=uint32_t(read_le(i,4));return r;}
static void atomic_rename(const std::string&tmp,const std::string&path){fs::rename(tmp,path);}
struct NFProgress{
 uint32_t sources=0,targets=0;
 uint64_t normalOperations=0,normalBytes=0,operationBytes=0,textBytes=0;
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
   levels[d]=pd+10*(top-d)+1;stride[d]=(mon[d].size()+31)/32;nw[d]=levels[d]*stride[d];row[d].resize(7*nw[d]);
  }
 }
};
struct NormalOp {uint16_t basis;uint8_t exponent,coefficient;};

int main(int argc,char **argv){try{
 if(argc!=5)return 2;
 const std::string inputPath=argv[1],prefix=argv[2],binding=argv[3];
 const double budget=std::stod(argv[4]);
 need(binding.size()==64&&binding.find_first_not_of("0123456789abcdef")==std::string::npos,"SHA256 binding");
 need(budget>0&&budget<=1800,"finite native budget");
 const auto started=std::chrono::steady_clock::now();
 auto seconds=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count();};
 BitOps ops;const uint64_t arithmeticChecks=ops.verify();
 std::ifstream in(inputPath);std::string magic;in>>magic;
 need(magic=="R150_NATIVE_NF127_V1","exact original127 model header");
 std::array<std::array<int,66>,11> Q{};
 std::array<std::array<std::array<int,11>,11>,11> L{};
 for(int e=0;e<11;e++){for(auto &v:Q[e])in>>v;for(auto &v:L[e])for(auto &a:v)in>>a;}
 int count;in>>count;need(count==3333,"all3333 original prebasis inputs");
 std::vector<Source> selected(count);
 for(auto &s:selected)in>>s.e>>s.mult>>s.pivot>>s.raw;
 std::array<std::array<std::array<int,6>,66>,6> G{};
 for(auto &g:G)for(auto &v:g)for(auto &a:v)in>>a;
 int ns,nt;in>>ns>>nt;need(ns==2195&&nt==9,"all original remaining sources and targets");
 std::vector<Source> sources(ns);for(auto &s:sources)in>>s.e>>s.mult>>s.raw;
 std::vector<int> targets(nt);for(auto &x:targets)in>>x;
 need(bool(in),"complete original127 model");
 std::string trailing;need(!(in>>trailing),"original model EOF");
 for(const auto&r:Q)for(int v:r)need(v>=0&&v<127,"canonical N head");
 for(const auto&r:L)for(const auto&v:r)for(int a:v)need(a>=0&&a<127,"canonical N tail");
 for(const auto&r:G)for(const auto&v:r)for(int a:v)need(a>=0&&a<127,"canonical Gamma");
 for(int j=0;j<nt;j++)need(targets[j]==j+2,"original target labels");
 std::array<uint64_t,11> var{};var[0]=1;for(int i=1;i<11;i++)var[i]=8*var[i-1];
 std::vector<std::vector<uint64_t>> mon(6);
 auto enumerate=[&](auto&&self,int left,int lo,uint64_t key,int d)->void{
  if(!left){mon[d].push_back(key);return;}
  for(int i=lo;i<11;i++)self(self,left-1,i,key+var[i],d);
 };
 for(int d=0;d<=5;d++)enumerate(enumerate,d,0,0,d);
 std::array<std::unordered_map<uint64_t,int>,6> local;
 for(int d=1;d<=5;d++)for(int j=0;j<int(mon[d].size());j++)local[d][mon[d][j]]=j;
 std::array<Phase,6> phases;
 for(int d=2;d<=5;d++){
  auto &P=phases[d];P.d=d;P.hi=mon[d].size();P.lo=mon[d-1].size();
  P.hw=(P.hi+31)/32;P.lw=(P.lo+31)/32;P.nw=P.hw+11*P.lw;
  P.basis.resize(P.hi);P.id.resize(P.hi);P.highIndex=local[d];P.lowIndex=local[d-1];
 }
 std::vector<std::pair<int,int>> quadratic;
 for(int a=0;a<11;a++)for(int b=a;b<11;b++)quadratic.push_back({a,b});
 const std::string cachePath=prefix+"-prebasis.bin",statePath=prefix+"-progress.bin";
 const std::string fwdPath=prefix+"-forward.bin",backPath=prefix+"-backward.bin";
 const std::string nfPath=prefix+"-normal-forms.bin",tracePath=prefix+"-reduction.bin",textPath=prefix+"-normal-forms.sing";
 uint64_t forwardCount=0,backwardCount=0,changedPivots=0;
 int generated=0;bool reusedPrebasis=false,resumedRows=false;
 auto verifyPrebasis=[&](){
  uint64_t tests=0;
  std::vector<bool> seen(3334,false);
  for(int d=2;d<=5;d++){
   auto &P=phases[d];
   need(std::is_sorted(P.pivots.begin(),P.pivots.end()),"prebasis pivot order");
   for(int c:P.pivots){
    need(P.basis[c]&&P.id[c]>=1&&P.id[c]<=3333&&!seen[P.id[c]],"distinct original prebasis nodes");
    seen[P.id[c]]=true;
    for(int q:P.pivots){
     need(BitOps::get((*P.basis[c])[0],P.nw,q)==int(c==q),"all same-degree unit products");
     tests++;
    }
   }
  }
  need(std::count(seen.begin(),seen.end(),true)==3333,"complete3333 source basis");
  return tests;
 };
 if(fs::exists(cachePath)){
  std::ifstream cache(cachePath,std::ios::binary);expect(cache,"R15PC127");binding_read(cache,binding);
  need(read_le(cache,4)==127&&read_le(cache,4)==3333,"original127 cache dimensions");
  forwardCount=read_le(cache,8);backwardCount=read_le(cache,8);changedPivots=read_le(cache,8);
  for(int d=2;d<=5;d++){
   auto &P=phases[d];need(read_le(cache,4)==uint64_t(d)&&read_le(cache,4)==uint64_t(P.nw),"same prebasis geometry");
   int n=read_le(cache,4);need(n>=0&&n<=P.hi,"prebasis cache count");
   for(int j=0;j<n;j++){
    int c=read_le(cache,4),id=read_le(cache,4);
    need(c>=0&&c<P.hi&&!P.basis[c],"cache unique pivot");
    auto t=std::make_unique<Triple>();(*t)[0]=words_read(cache,7*P.nw);
    BitOps::refresh(*t,P.nw,c/32);P.basis[c]=std::move(t);
    P.id[c]=id;P.pivots.push_back(c);generated++;
   }
  }
  expect(cache,"ENDPC127");need(cache.get()==EOF,"prebasis cache EOF");
  need(fs::exists(fwdPath)&&fs::exists(backPath),"prebasis original operations retained");
  reusedPrebasis=true;
 }else{
  need(!fs::exists(statePath),"normal-form continuation without its prebasis is forbidden");
  std::ofstream fwd(fwdPath,std::ios::binary),back(backPath,std::ios::binary);
  need(bool(fwd)&&bool(back),"prebasis source DAG outputs");
  fwd.write("R15PF127",8);u32(fwd,3333);fwd.write(binding.data(),64);
  back.write("R15PB127",8);u32(back,3333);back.write(binding.data(),64);
  for(int d=2;d<=5;d++){
   auto &P=phases[d];
   for(const auto &s:selected){
    if(degree(s.mult)+2!=d)continue;
    need(s.e>=0&&s.e<11&&s.raw>=1&&s.raw<=6188,"original prebasis source");
    Row row(7*P.nw);
    for(int k=0;k<66;k++){
     auto [a,b]=quadratic[k];
     BitOps::set(row,P.nw,P.highIndex.at(s.mult+var[a]+var[b]),Q[s.e][k]);
    }
    for(int v=0;v<11;v++)for(int k=0;k<11;k++)
     BitOps::set(row,P.nw,(P.hw+k*P.lw)*32+P.lowIndex.at(s.mult+var[v]),L[s.e][v][k]);
    std::vector<std::pair<uint16_t,uint8_t>> reductions;int pivot=-1,value=0;
    for(int c=0;c<P.hi;c++){
     int a=BitOps::get(row,P.nw,c);if(!a)continue;
     if(!P.basis[c]){pivot=c;value=a;break;}
     reductions.push_back({uint16_t(P.id[c]),uint8_t(a)});const auto R=ops.rep[127-a];
     int w=c/32;BitOps::add(row,P.nw,w,(*P.basis[c])[R.c],P.nw,w,P.nw-w,R.rot,R.neg);forwardCount++;
    }
    need(pivot>=0,"fixed3333 original source family not independent at127");
    changedPivots+=mon[d][pivot]!=s.pivot;
    int scale=ops.inv[value];if(value!=1)ops.multiple(row,P.nw,pivot/32,scale);
    need(BitOps::get(row,P.nw,pivot)==1,"actual127 prebasis unit pivot");
    generated++;P.id[pivot]=generated;P.pivots.push_back(pivot);
    u32(fwd,s.raw);fwd.put(char(scale));u32(fwd,reductions.size());
    for(auto [id,a]:reductions){u16(fwd,id);fwd.put(char(a));}
    auto t=std::make_unique<Triple>();(*t)[0]=std::move(row);
    BitOps::refresh(*t,P.nw,pivot/32);P.basis[pivot]=std::move(t);
   }
   std::sort(P.pivots.begin(),P.pivots.end());
   std::cout<<"{\"phase\":\"original127-forward-prebasis\",\"mDegree\":"<<d<<",\"rank\":"<<P.pivots.size()<<",\"elapsedSeconds\":"<<seconds()<<"}\n"<<std::flush;
   for(int ii=int(P.pivots.size())-1;ii>=0;ii--){
    int c=P.pivots[ii];auto &t=*P.basis[c];std::vector<std::pair<uint16_t,uint8_t>> reductions;
    for(int jj=ii+1;jj<int(P.pivots.size());jj++){
     int q=P.pivots[jj],a=BitOps::get(t[0],P.nw,q);if(!a)continue;
     reductions.push_back({uint16_t(P.id[q]),uint8_t(a)});auto R=ops.rep[127-a];int w=q/32;
     BitOps::add(t[0],P.nw,w,(*P.basis[q])[R.c],P.nw,w,P.nw-w,R.rot,R.neg);backwardCount++;
    }
    BitOps::refresh(t,P.nw,c/32);u16(back,P.id[c]);u32(back,reductions.size());
    for(auto [id,a]:reductions){u16(back,id);back.put(char(a));}
   }
   std::cout<<"{\"phase\":\"original127-same-degree-rref\",\"mDegree\":"<<d<<",\"elapsedSeconds\":"<<seconds()<<"}\n"<<std::flush;
  }
  fwd.close();back.close();need(bool(fwd)&&bool(back),"complete original prebasis DAG flush");
  need(generated==3333,"actual original127 constant rank3333");
  verifyPrebasis();
  std::string tmp=cachePath+".tmp";std::ofstream cache(tmp,std::ios::binary);
  cache.write("R15PC127",8);cache.write(binding.data(),64);u32(cache,127);u32(cache,3333);
  u64(cache,forwardCount);u64(cache,backwardCount);u64(cache,changedPivots);
  for(int d=2;d<=5;d++){
   const auto &P=phases[d];u32(cache,d);u32(cache,P.nw);u32(cache,P.pivots.size());
   for(int c:P.pivots){u32(cache,c);u32(cache,P.id[c]);words_write(cache,(*P.basis[c])[0]);}
  }
  cache.write("ENDPC127",8);cache.close();need(bool(cache),"complete prebasis checkpoint");
  atomic_rename(tmp,cachePath);
 }
 need(generated==3333,"complete prebasis cache count");
 const uint64_t prebasisProducts=verifyPrebasis();
 std::unordered_map<uint64_t,int> component;std::vector<uint64_t> componentKeys;
 for(int d=5;d>=1;d--)for(int j=0;j<int(mon[d].size());j++)
  if(d==1||!phases[d].basis[j]){component[mon[d][j]]=int(componentKeys.size())+1;componentKeys.push_back(mon[d][j]);}
 need(componentKeys.size()==1034,"actual quotient dimension1034");
 {
  std::string path=prefix+"-component-dictionary.bin",tmp=path+".tmp";
  std::ofstream dict(tmp,std::ios::binary);dict.write("R15CD127",8);dict.write(binding.data(),64);
  u32(dict,1034);for(auto key:componentKeys)u64(dict,key);dict.close();need(bool(dict),"component dictionary");
  atomic_rename(tmp,path);
 }
 NFProgress progress;
 if(fs::exists(statePath)){
  std::ifstream st(statePath,std::ios::binary);expect(st,"R15NS127");binding_read(st,binding);
  progress.sources=read_le(st,4);progress.targets=read_le(st,4);
  progress.normalOperations=read_le(st,8);progress.normalBytes=read_le(st,8);
  progress.operationBytes=read_le(st,8);progress.textBytes=read_le(st,8);
  expect(st,"ENDNS127");need(st.get()==EOF&&progress.sources<=uint32_t(ns)&&progress.targets<=uint32_t(nt),"complete row checkpoint");
  need(!progress.targets||progress.sources==uint32_t(ns),"target stage follows all original sources");
  for(auto pair:{std::make_pair(nfPath,progress.normalBytes),std::make_pair(tracePath,progress.operationBytes),std::make_pair(textPath,progress.textBytes)}){
   need(fs::exists(pair.first)&&fs::file_size(pair.first)>=pair.second,"retained exact committed prefix");
   fs::resize_file(pair.first,pair.second);
  }
  resumedRows=true;
 }
 std::ofstream nfops(tracePath,std::ios::binary|(resumedRows?std::ios::app:std::ios::trunc));
 std::ofstream out(nfPath,std::ios::binary|(resumedRows?std::ios::app:std::ios::trunc));
 std::ofstream sing(textPath,resumedRows?std::ios::app:std::ios::trunc);
 need(bool(nfops)&&bool(out)&&bool(sing),"normal form outputs");
 if(!resumedRows){
  nfops.write("R15NR127",8);nfops.write(binding.data(),64);u32(nfops,ns+nt);
  out.write("R15NF127",8);out.write(binding.data(),64);u32(out,ns);u32(out,nt);u32(out,1034);
  sing<<"// Complete original source dictionary and source operations are retained.\nmodule Reduced; module Target;\n";
 }
 auto commit=[&](const char *status){
  nfops.flush();out.flush();sing.flush();need(bool(nfops)&&bool(out)&&bool(sing),"whole-row flush");
  progress.operationBytes=uint64_t(nfops.tellp());progress.normalBytes=uint64_t(out.tellp());progress.textBytes=uint64_t(sing.tellp());
  std::string tmp=statePath+".tmp";std::ofstream st(tmp,std::ios::binary);
  st.write("R15NS127",8);st.write(binding.data(),64);u32(st,progress.sources);u32(st,progress.targets);
  u64(st,progress.normalOperations);u64(st,progress.normalBytes);u64(st,progress.operationBytes);u64(st,progress.textBytes);
  st.write("ENDNS127",8);st.close();need(bool(st),"complete normal-form state");atomic_rename(tmp,statePath);
  const std::string receipt=prefix+"-native-receipt.json";
  std::ofstream r(receipt+".tmp");
  r<<"{\"format\":\"r150-original127-normal-forms-native-v1\",\"status\":\""<<status<<"\",\"prime\":127,\"binding\":\""<<binding
   <<"\",\"completedSources\":"<<progress.sources<<",\"completedTargets\":"<<progress.targets<<",\"fullSourceCount\":2195,\"fullTargetCount\":9"
   <<",\"prebasisRank\":3333,\"components\":1034,\"sameDegreeUnitProducts\":"<<prebasisProducts
   <<",\"actualChangedPivotPositions\":"<<changedPivots<<",\"forwardOperations\":"<<forwardCount<<",\"backwardOperations\":"<<backwardCount
   <<",\"normalOperations\":"<<progress.normalOperations<<",\"exhaustiveScalarArithmeticChecks\":"<<arithmeticChecks
   <<",\"prebasisReused\":"<<(reusedPrebasis?"true":"false")<<",\"wholeRowPrefixResumed\":"<<(resumedRows?"true":"false")
   <<",\"allOriginalRowsCompleted\":"<<((progress.sources==uint32_t(ns)&&progress.targets==uint32_t(nt))?"true":"false")
   <<",\"noOriginalSourceDropped\":true,\"oldField31OperationsReused\":false,\"elapsedSeconds\":"<<seconds()<<"}\n";
  r.close();need(bool(r),"small native receipt");atomic_rename(receipt+".tmp",receipt);
 };
 commit("prefix-ready");
 auto coefficient=[&](PolynomialRow &r,int d,uint64_t key,int k,int a){
  need(k>=0&&k<r.levels[d],"original parameter degree bound");
  BitOps::set(r.row[d],r.nw[d],k*r.stride[d]*32+local[d].at(key),a);
 };
 auto normal=[&](PolynomialRow &r,int source,int target,int ordinal){
  std::vector<NormalOp> trace;
  for(int d=r.top;d>=2;d--){
   const auto &P=phases[d];
   for(int c:P.pivots)for(int k=0;k<r.levels[d];k++){
    int a=BitOps::get(r.row[d],r.nw[d],k*r.stride[d]*32+c);if(!a)continue;
    trace.push_back({uint16_t(P.id[c]),uint8_t(k),uint8_t(a)});
    const auto R=ops.rep[127-a];const auto &b=(*P.basis[c])[R.c];int w=c/32;
    BitOps::add(r.row[d],r.nw[d],k*r.stride[d]+w,b,P.nw,w,P.hw-w,R.rot,R.neg);
    need(k+11<=r.levels[d-1],"retained complete lower-degree tail");
    BitOps::add(r.row[d-1],r.nw[d-1],k*r.stride[d-1],b,P.nw,P.hw,11*P.lw,R.rot,R.neg);
   }
   for(int c:P.pivots)for(int k=0;k<r.levels[d];k++)
    need(BitOps::get(r.row[d],r.nw[d],k*r.stride[d]*32+c)==0,"every original normal-form pivot cancelled");
  }
  progress.normalOperations+=trace.size();u32(nfops,source);u16(nfops,target);u32(nfops,trace.size());
  for(auto a:trace){u16(nfops,a.basis);nfops.put(char(a.exponent));nfops.put(char(a.coefficient));}
  struct Entry{int component;std::vector<uint8_t> coefficient;};
  std::vector<Entry> entries;int maximum=-1;uint64_t nonzero=0;
  for(int d=r.top;d>=1;d--)for(int c=0;c<int(mon[d].size());c++){
   auto ix=component.find(mon[d][c]);if(ix==component.end())continue;
   std::vector<uint8_t> co(r.levels[d]);
   for(int k=0;k<r.levels[d];k++)co[k]=BitOps::get(r.row[d],r.nw[d],k*r.stride[d]*32+c);
   while(!co.empty()&&!co.back())co.pop_back();if(co.empty())continue;
   maximum=std::max(maximum,int(co.size())-1);for(auto a:co)nonzero+=a!=0;
   entries.push_back({ix->second,std::move(co)});
  }
  need(maximum<=45,"complete univariate parameter degree45");
  u32(out,source);u16(out,target);u32(out,entries.size());
  for(auto &e:entries){u16(out,e.component);out.put(char(e.coefficient.size()));out.write(reinterpret_cast<const char*>(e.coefficient.data()),e.coefficient.size());}
  sing<<(target?"Target[":"Reduced[")<<ordinal<<"]=";bool first=true;
  for(auto &e:entries){
   if(!first)sing<<"+";first=false;sing<<"(";bool term=true;
   for(int k=0;k<int(e.coefficient.size());k++){
    int a=e.coefficient[k];if(!a)continue;if(!term)sing<<"+";term=false;sing<<a;
    if(k)sing<<"*s"<<(k>1?"^"+std::to_string(k):"");
   }
   sing<<")*gen("<<e.component<<")";
  }
  if(first)sing<<"0";sing<<";\n";
  if(target||ordinal%25==0||ordinal==1||ordinal==ns)
   std::cout<<"{\"phase\":\"original127-normal-form\",\"sourceRow\":"<<source<<",\"target\":"<<target<<",\"ordinal\":"<<ordinal
    <<",\"parameterDegree\":"<<maximum<<",\"nonzeroCoefficients\":"<<nonzero<<",\"elapsedSeconds\":"<<seconds()<<"}\n"<<std::flush;
 };
 for(int index=progress.sources;index<ns;index++){
  if(seconds()>=budget){commit("budget-checkpoint");return 75;}
  const auto&s=sources[index];need(s.e>=0&&s.e<17&&s.raw>=1&&s.raw<=6188,"original source identity");
  int top=degree(s.mult)+2;need(top>=2&&top<=5,"source multiplier degree");
  PolynomialRow r(top,s.e<11?0:5,mon);
  for(int k=0;k<66;k++){
   auto [a,b]=quadratic[k];uint64_t key=s.mult+var[a]+var[b];
   if(s.e<11)coefficient(r,top,key,0,Q[s.e][k]);
   else for(int j=0;j<6;j++)coefficient(r,top,key,j,G[s.e-11][k][j]);
  }
  if(s.e<11)for(int v=0;v<11;v++)for(int j=0;j<11;j++)
   coefficient(r,top-1,s.mult+var[v],j,L[s.e][v][j]);
  normal(r,s.raw,0,index+1);progress.sources=index+1;commit("normal-form-source-prefix");
 }
 auto binomial=[](int n,int k){int x=1;for(int j=1;j<=k;j++)x=x*(n-j+1)/j;return x;};
 for(int index=progress.targets;index<nt;index++){
  if(seconds()>=budget){commit("budget-checkpoint");return 75;}
  int j=targets[index];PolynomialRow r(2,2*j,mon);
  for(int a=0;a<=j;a++)for(int b=a;b<=j;b++){
   int k=2*j-a-b,c=binomial(j,a)*binomial(j,b)*(a==b?1:2)*(k%2?-1:1);
   coefficient(r,2,var[a]+var[b],k,c%127);
  }
  normal(r,0,j,index+1);progress.targets=index+1;commit("normal-form-target-prefix");
 }
 commit("completed");std::cout<<"{\"status\":\"original127-normal-forms-complete\",\"completedSources\":2195,\"completedTargets\":9,\"elapsedSeconds\":"<<seconds()<<"}\n"<<std::flush;
 return 0;
}catch(const std::exception&e){std::cerr<<"ORIGINAL127_NORMAL_FORM_FAILED "<<e.what()<<"\n";return 1;}}
