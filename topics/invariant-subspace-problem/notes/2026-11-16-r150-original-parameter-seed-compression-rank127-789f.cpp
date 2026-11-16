// Complete F127 row relations for original parameter seeds; no point sampling.
// Author: Astra-ISP-789f / normal_annihilator, with /root.
// AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
#include "2026-11-15-r150-original-f127-bitplane-789f.hpp"
#include <chrono>
#include <cstdio>
#include <filesystem>
#include <iostream>
#include <memory>
#include <sstream>
namespace fs=std::filesystem;
using Clock=std::chrono::steady_clock;
static void need(bool b,const std::string&s){if(!b)throw std::runtime_error(s);}
static std::string fixed(std::istream&f,size_t n){std::string s(n,'\0');f.read(&s[0],n);need(size_t(f.gcount())==n,"complete fixed field");return s;}
static void magic(std::istream&f,const char*s){need(fixed(f,8)==std::string(s,8),"exact independent protocol");}
static void finish(std::ofstream&f,const fs::path&t,const fs::path&p){
 f.flush();need(bool(f),"complete checkpoint flush");f.close();need(std::rename(t.c_str(),p.c_str())==0,"atomic whole-row checkpoint");
}
struct Basis {uint32_t pivot,source;Triple row;};
struct Relation {uint32_t source;std::vector<uint8_t> q;};
struct State {
 uint32_t no=0,ni=0,first=0,next=0;int nw=0;std::string binding;
 std::vector<Basis> basis;std::vector<Relation> dep;std::vector<int> at;
 uint64_t reductions=0,unitChecks=0;
};
static void validrow(const Row&r,const State&s,uint32_t p,uint32_t source){
 need(r.size()==size_t(7*s.nw),"complete normalized row shape");
 need(BitOps::get(r,s.nw,p)==1,"normalized original output pivot");
 for(uint32_t j=0;j<p;j++)need(BitOps::get(r,s.nw,j)==0,"no earlier output coordinate");
 for(uint32_t j=source+1;j<s.ni;j++)need(BitOps::get(r,s.nw,s.no+j)==0,"no future original source in recipe");
 for(int w=0;w<s.nw;w++){
  uint32_t all=UINT32_MAX;for(int b=0;b<7;b++)all&=r[b*s.nw+w];
  need(all==0,"all field entries canonical, not redundant127");
 }
 int rem=(s.no+s.ni)%32;
 if(rem)for(int b=0;b<7;b++)need((r[b*s.nw+s.nw-1]>>rem)==0,"all augmented padding bits zero");
}
static void save_state(const fs::path&out,const State&s){
 auto p=out/"complete-row-state.bin",t=out/"complete-row-state.bin.tmp";
 std::ofstream f(t,std::ios::binary);f.write("R15PCS01",8);u32(f,1);u32(f,s.no);u32(f,s.ni);u32(f,s.first);u32(f,s.next);
 u32(f,s.basis.size());u32(f,s.dep.size());f.write(s.binding.data(),64);u64(f,s.reductions);u64(f,s.unitChecks);
 for(const auto&b:s.basis){u32(f,b.pivot);u32(f,b.source);for(uint32_t x:b.row[0])u32(f,x);}
 for(const auto&d:s.dep){u32(f,d.source);f.write(reinterpret_cast<const char*>(d.q.data()),d.q.size());}
 finish(f,t,p);
}
static void save_result(const fs::path&out,const State&s){
 auto p=out/"complete-row-result.bin",t=out/"complete-row-result.bin.tmp";
 std::ofstream f(t,std::ios::binary);f.write("R15PCR01",8);u32(f,1);u32(f,s.no);u32(f,s.ni);u32(f,s.first);u32(f,s.next);
 u32(f,s.basis.size());u32(f,s.dep.size());f.write(s.binding.data(),64);u64(f,s.reductions);u64(f,s.unitChecks);
 for(const auto&b:s.basis){u32(f,b.pivot);u32(f,b.source);}
 for(const auto&d:s.dep){u32(f,d.source);f.write(reinterpret_cast<const char*>(d.q.data()),d.q.size());}
 finish(f,t,p);
}
static void load_state(const fs::path&p,State&s,const BitOps&ops){
 std::ifstream f(p,std::ios::binary);magic(f,"R15PCS01");
 need(read_le(f,4)==1&&read_le(f,4)==s.no&&read_le(f,4)==s.ni&&read_le(f,4)==s.first,"same complete original dimensions");
 s.next=read_le(f,4);uint32_t rank=read_le(f,4),nd=read_le(f,4);
 need(fixed(f,64)==s.binding&&s.next<=s.ni&&rank<=s.next&&nd<=s.ni-s.first,"same bound complete-row state");
 s.reductions=read_le(f,8);s.unitChecks=read_le(f,8);
 for(uint32_t k=0;k<rank;k++){
  Basis b;b.pivot=read_le(f,4);b.source=read_le(f,4);
  need(b.pivot<s.no&&b.source<s.next&&s.at[b.pivot]<0,"unique original normalized unit");
  b.row[0].resize(7*s.nw);for(auto&x:b.row[0])x=read_le(f,4);validrow(b.row[0],s,b.pivot,b.source);
  BitOps::refresh(b.row,s.nw,b.pivot/32);s.at[b.pivot]=s.basis.size();s.basis.push_back(std::move(b));
 }
 std::vector<uint8_t> seen(s.ni,0);
 for(uint32_t k=0;k<nd;k++){
  Relation d;d.source=read_le(f,4);need(d.source>=s.first&&d.source<s.next&&!seen[d.source],"complete literal target relation prefix");seen[d.source]=1;
  std::string z=fixed(f,s.ni);d.q.assign(z.begin(),z.end());
  need(d.q[d.source]==1,"target coefficient exactly one");
  for(uint32_t j=0;j<s.ni;j++)need(d.q[j]<127&&(j<=d.source||d.q[j]==0),"canonical preceding-source relation");
  s.dep.push_back(std::move(d));
 }
 need(f.peek()==EOF,"no extra checkpoint payload");
 std::vector<uint8_t> used(s.ni,0);for(const auto&b:s.basis){need(!used[b.source],"distinct independent original input rows");used[b.source]=1;}
 for(uint32_t j=s.first;j<s.next;j++)need(bool(used[j])!=bool(seen[j]),"every processed target wholly classified");
}
static void insert(State&s,Row&&r,uint32_t source,const BitOps&ops){
 for(uint32_t p=0;p<s.no;p++){
  int v=BitOps::get(r,s.nw,p);if(!v)continue;
  int bi=s.at[p];
  if(bi>=0){
   const auto t=ops.rep[127-v];const Basis&b=s.basis[bi];
   BitOps::add(r,s.nw,p/32,b.row[t.c],s.nw,p/32,s.nw-p/32,t.rot,t.neg);
   need(BitOps::get(r,s.nw,p)==0,"whole original pivot cancellation");s.reductions++;continue;
  }
  ops.multiple(r,s.nw,p/32,ops.inv[v]);validrow(r,s,p,source);s.unitChecks++;
  Basis b;b.pivot=p;b.source=source;b.row[0]=std::move(r);BitOps::refresh(b.row,s.nw,p/32);
  s.at[p]=s.basis.size();s.basis.push_back(std::move(b));return;
 }
 if(source>=s.first){
  Relation d;d.source=source;d.q.resize(s.ni);
  for(uint32_t j=0;j<s.ni;j++)d.q[j]=BitOps::get(r,s.nw,s.no+j);
  need(d.q[source]==1,"full dependent row has unit original target coefficient");
  for(uint32_t j=source+1;j<s.ni;j++)need(d.q[j]==0,"dependent recipe never uses future rows");
  s.dep.push_back(std::move(d));
 }
}
static uint64_t tiny(const BitOps&ops){
 const std::vector<std::vector<int>> a={{1,0,2,3,0},{2,1,0,4,1},{3,1,2,7,1},{0,0,0,0,0},{0,1,123,125,1}};
 State s;s.no=5;s.ni=a.size();s.first=0;s.nw=(s.no+s.ni+31)/32;s.at.assign(s.no,-1);
 for(uint32_t i=0;i<s.ni;i++){Row r(7*s.nw,0);for(uint32_t j=0;j<s.no;j++)BitOps::set(r,s.nw,j,a[i][j]);BitOps::set(r,s.nw,s.no+i,1);insert(s,std::move(r),i,ops);s.next=i+1;}
 std::vector<std::vector<int>> ga=a;int rank=0;
 for(int j=0;j<5;j++){
  int k=rank;while(k<int(a.size())&&!ga[k][j])k++;if(k==int(a.size()))continue;std::swap(ga[k],ga[rank]);int z=ops.inv[ga[rank][j]];
  for(int c=0;c<5;c++)ga[rank][c]=ga[rank][c]*z%127;
  for(int i=rank+1;i<int(a.size());i++){z=ga[i][j];for(int c=0;c<5;c++)ga[i][c]=(ga[i][c]-z*ga[rank][c]%127+127)%127;}rank++;
 }
 need(rank==int(s.basis.size()),"independent ordinary scalar elimination tiny rank");
 uint64_t count=0;
 for(const auto&d:s.dep)for(int j=0;j<5;j++){
  int z=0;for(int i=0;i<int(a.size());i++)z=(z+int(d.q[i])*a[i][j])%127;need(z==0,"all original tiny source relation products");count++;
 }
 for(const auto&b:s.basis)for(int j=0;j<5;j++){
  int z=0;for(int i=0;i<int(a.size());i++)z=(z+BitOps::get(b.row[0],s.nw,s.no+i)*a[i][j])%127;
  need(z==BitOps::get(b.row[0],s.nw,j),"all normalized tiny original source products");count++;
 }
 return count;
}
int main(int argc,char**argv){
 auto start=Clock::now();int code=1;
 try{
  need(argc==4,"input out seconds");fs::path input=argv[1],out=argv[2];double seconds=std::stod(argv[3]);need(seconds>0&&seconds<=900,"bounded whole-row solve");
  fs::create_directories(out);BitOps ops;uint64_t scalarChecks=ops.verify(),tinyChecks=tiny(ops);
  std::ifstream f(input,std::ios::binary);magic(f,"R15PCI01");need(read_le(f,4)==1,"source input version");
  State s;s.no=read_le(f,4);s.ni=read_le(f,4);s.first=read_le(f,4);need(read_le(f,4)==127,"exact original field");
  s.binding=fixed(f,64);need(s.no>0&&s.no<=20000&&s.ni>0&&s.ni<=2000&&s.first<=s.ni,"complete original bounds");
  need(s.binding.find_first_not_of("0123456789abcdef")==std::string::npos,"full semantic SHA256 binding");
  need(fs::file_size(input)==92ull+uint64_t(s.no)*s.ni,"all original scalar input rows retained");
  s.nw=(s.no+s.ni+31)/32;s.at.assign(s.no,-1);
  auto cp=out/"complete-row-state.bin";if(fs::exists(cp))load_state(cp,s,ops);
  const uint32_t initial=s.next;std::vector<uint8_t> values(s.no);
  for(;s.next<s.ni;){
   if(std::chrono::duration<double>(Clock::now()-start).count()>seconds-2)break;
   f.seekg(92ull+uint64_t(s.next)*s.no);f.read(reinterpret_cast<char*>(values.data()),s.no);need(uint32_t(f.gcount())==s.no,"whole next original input row");
   Row r(7*s.nw,0);for(uint32_t j=0;j<s.no;j++){need(values[j]<127,"all original coefficients canonical");if(values[j])BitOps::set(r,s.nw,j,values[j]);}
   BitOps::set(r,s.nw,s.no+s.next,1);insert(s,std::move(r),s.next,ops);s.next++;
  }
  save_state(out,s);save_result(out,s);code=s.next==s.ni?0:75;
  std::ostringstream z;z<<"{\"format\":\"r150-original-parameter-seed-row-relations127-native-v1\",\"binding\":\""<<s.binding
   <<"\",\"status\":\""<<(code==0?"completed":"budget-checkpoint")<<"\",\"initialWholeRows\":"<<initial
   <<",\"completeWholeRows\":"<<s.next<<",\"inputRows\":"<<s.ni<<",\"allOutputCoordinates\":"<<s.no
   <<",\"rank\":"<<s.basis.size()<<",\"wholeTargetRelations\":"<<s.dep.size()<<",\"pivotCancellations\":"<<s.reductions
   <<",\"wholeUnitRows\":"<<s.unitChecks<<",\"exhaustiveBitplaneChecks\":"<<scalarChecks<<",\"independentTinyProducts\":"<<tinyChecks
   <<",\"elapsedSeconds\":"<<std::chrono::duration<double>(Clock::now()-start).count()<<"}";
  auto p=out/"parameter-seed-native-receipt.json",t=out/"parameter-seed-native-receipt.json.tmp";std::ofstream rf(t);rf<<z.str();finish(rf,t,p);
  std::cout<<z.str()<<std::endl;
 }catch(const std::exception&e){std::cerr<<e.what()<<std::endl;return 1;}
 return code;
}
