// Complete original F_127[s] streaming module basis with resumable whole state.
// Author: Astra-ISP-789f / normal_annihilator.
// AI-assisted: GPT-6 Astra Pro. Date: 2026-11-15.
#include "2026-11-15-r150-original-f127-bitplane-789f.hpp"
#include <chrono>
#include <filesystem>
#include <iostream>
#include <memory>
#include <utility>
namespace fs=std::filesystem;
static void need(bool b,const std::string&s){if(!b)throw std::runtime_error(s);}
static void expect(std::istream&i,const char*m){char b[8];i.read(b,8);need(i&&std::string(b,8)==std::string(m,8),"exact binary magic");}
static void check_binding(std::istream&i,const std::string&binding){char b[64];i.read(b,64);need(i&&std::string(b,64)==binding,"exact original127 binding");}
static void write_words(std::ostream&o,const Row&r){for(auto x:r)u32(o,x);}
static Row read_words(std::istream&i,size_t n){Row r(n);for(auto &x:r)x=uint32_t(read_le(i,4));return r;}
struct Lead{int degree=-1,component=-1,coefficient=0;};
struct Pivot{std::unique_ptr<Triple> data;int degree=-1,coefficient=0;uint32_t node=0;};
int main(int argc,char**argv){try{
 if(argc!=6)return 2;
 const std::string input=argv[1],prefix=argv[2],parent=argv[3],binding=argv[4];
 const double budget=std::stod(argv[5]);
 need(parent.size()==64&&binding.size()==64&&budget>0&&budget<=7200,"bounded original127 GB arguments");
 auto started=std::chrono::steady_clock::now();
 auto seconds=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count();};
 BitOps ops;const uint64_t arithmeticChecks=ops.verify();
 std::ifstream in(input,std::ios::binary);expect(in,"R15NF127");check_binding(in,parent);
 const int ns=read_le(in,4),nt=read_le(in,4),q=read_le(in,4),D=45,W=(q+31)/32,nw=(D+1)*W;
 need(ns>0&&ns+3333==6188&&nt==9&&q==1034,"complete newly computed original6188-source NF");
 std::vector<Pivot> piv(q);
 int rank=0,processed=0,maxInput=-1,currentRaw=0;bool inRow=false,resumed=false,finalized=false;
 uint32_t currentNode=0;Row current;
 uint64_t reductions=0,swaps=0,generation=0,dagBytes=0,inputOffset=uint64_t(in.tellg());
 const std::string dagPath=prefix+"-operations.bin",selector=prefix+"-active.bin",nativeReceipt=prefix+"-native-receipt.json";
 auto lead=[&](const Row&r,int upper=45)->Lead{
  for(int d=upper;d>=0;d--)for(int w=0;w<W;w++){
   int off=d*W+w;uint32_t nonzero=0;
   for(int b=0;b<7;b++)nonzero|=r[b*nw+off];
   if(nonzero){
    int c=32*w+__builtin_ctz(nonzero);need(c<q,"zero padding in complete127 module row");
    int a=BitOps::get(r,nw,d*W*32+c);need(a>0&&a<127,"canonical leading field value");
    return {d,c,a};
   }
  }
  return {};
 };
 auto readRow=[&](int&raw,int&target)->Row{
  raw=read_le(in,4);target=read_le(in,2);int count=read_le(in,4),previous=0;Row r(7*nw);
  need(count>=0&&count<=q,"complete NF component count");
  for(int i=0;i<count;i++){
   int c=read_le(in,2),len=read_le(in,1);
   need(c>previous&&c<=q&&len>=1&&len<=D+1,"original NF component/degree order");previous=c;
   int last=0;for(int k=0;k<len;k++){
    int a=read_le(in,1);need(a<127,"canonical original127 coefficient");
    BitOps::set(r,nw,k*W*32+c-1,a);last=a;
   }
   need(last!=0,"no zero NF polynomial tail");
  }
  return r;
 };
 if(fs::exists(selector)){
  std::ifstream s(selector,std::ios::binary);expect(s,"R15GA127");check_binding(s,binding);
  generation=read_le(s,8);int slot=read_le(s,4);need(slot==int(generation%2),"whole checkpoint slot");
  expect(s,"ENDGA127");need(s.get()==EOF,"active checkpoint EOF");
  std::ifstream st(prefix+"-state-"+std::to_string(slot)+".bin",std::ios::binary);
  expect(st,"R15GC127");check_binding(st,binding);check_binding(st,parent);
  need(read_le(st,8)==generation&&read_le(st,4)==127&&read_le(st,4)==uint64_t(q)&&read_le(st,4)==uint64_t(D),"complete checkpoint geometry");
  processed=read_le(st,4);rank=read_le(st,4);maxInput=int(read_le(st,4))-1;inRow=read_le(st,1);finalized=read_le(st,1);
  currentRaw=read_le(st,4);currentNode=read_le(st,4);
  reductions=read_le(st,8);swaps=read_le(st,8);inputOffset=read_le(st,8);dagBytes=read_le(st,8);
  need(processed>=0&&processed<=ns&&rank>=0&&rank<=q&&(!inRow||processed<ns)&&(!finalized||(processed==ns&&!inRow)),"saved complete GB counters");
  int actualRank=0;
  for(int c=0;c<q;c++){
   int present=read_le(st,1);need(present<=1,"saved pivot presence");
   if(!present)continue;
   auto&P=piv[c];P.degree=read_le(st,1);P.coefficient=read_le(st,1);P.node=read_le(st,4);
   need(P.degree>=0&&P.degree<=D&&P.coefficient>=1&&P.coefficient<127&&P.node>=1,"saved original pivot");
   P.data=std::make_unique<Triple>();(*P.data)[0]=read_words(st,7*nw);
   Lead L=lead((*P.data)[0]);
   need(L.component==c&&L.degree==P.degree&&L.coefficient==P.coefficient,"complete saved pivot identity");
   BitOps::refresh(*P.data,nw,0);actualRank++;
  }
  if(inRow){current=read_words(st,7*nw);need(currentNode>=1&&currentRaw>=1&&currentRaw<=6188,"saved active original row");}
  expect(st,"ENDGC127");need(st.get()==EOF&&actualRank==rank,"whole GB checkpoint rank and EOF");
  need(fs::exists(dagPath)&&fs::file_size(dagPath)>=dagBytes&&inputOffset<=fs::file_size(input),"complete original input and operation prefix");
  fs::resize_file(dagPath,dagBytes);in.clear();in.seekg(inputOffset);need(bool(in),"resume exact original input offset");
  resumed=true;
 }else need(!fs::exists(dagPath),"unbound existing original127 GB DAG");
 std::ofstream dag(dagPath,std::ios::binary|(resumed?std::ios::app:std::ios::trunc));
 need(bool(dag),"original source expression DAG");
 if(!resumed){dag.write("R15GO127",8);dag.write(binding.data(),64);u32(dag,ns);u32(dag,q);dag.put(char(D));}
 auto writeReceipt=[&](const char*status){
  std::ofstream r(nativeReceipt+".tmp");
  r<<"{\"format\":\"r150-original127-graded-gb-native-v2\",\"status\":\""<<status<<"\",\"prime\":127,\"binding\":\""<<binding
   <<"\",\"parentNFBinding\":\""<<parent<<"\",\"generation\":"<<generation<<",\"activeSlot\":"<<int(generation%2)
   <<",\"processedSources\":"<<processed<<",\"fullSourceCount\":"<<ns<<",\"basisRank\":"<<rank
   <<",\"finalized\":"<<(finalized?"true":"false")<<",\"currentSourceActive\":"<<(inRow?"true":"false")<<",\"currentOriginalRawSource\":"<<currentRaw
   <<",\"maximumInputDegree\":"<<maxInput<<",\"reductions\":"<<reductions<<",\"swaps\":"<<swaps
   <<",\"committedInputOffset\":"<<inputOffset<<",\"committedDAGBytes\":"<<dagBytes
   <<",\"allOriginalComplementSourcesCompleted\":"<<(processed==ns&&!inRow?"true":"false")
   <<",\"sourceCheckpointResumed\":"<<(resumed?"true":"false")<<",\"exhaustiveScalarArithmeticChecks\":"<<arithmeticChecks
   <<",\"oldField31BasisReused\":false,\"elapsedSeconds\":"<<seconds()<<"}\n";
  r.close();need(bool(r),"small GB receipt");fs::rename(nativeReceipt+".tmp",nativeReceipt);
 };
 if(finalized){
  std::ifstream saved(prefix+"-basis.bin",std::ios::binary);expect(saved,"R15GB127");check_binding(saved,binding);
  need(fs::exists(prefix+"-basis-metadata.json"),"complete basis metadata before finalized checkpoint");
  writeReceipt("completed");
  std::cout<<"{\"status\":\"complete-original127-basis-reused\",\"mathematicsRecomputed\":false}\n"<<std::flush;
  return 0;
 }
 double lastCheckpoint=seconds();
 auto checkpoint=[&](const char*status){
  dag.flush();need(bool(dag),"complete expression DAG flush");
  dagBytes=uint64_t(dag.tellp());inputOffset=uint64_t(in.tellg());
  need(inputOffset<=fs::file_size(input),"exact checkpoint input offset");
  uint64_t next=generation+1;int slot=next%2;
  const std::string statePath=prefix+"-state-"+std::to_string(slot)+".bin",tmp=statePath+".tmp";
  std::ofstream st(tmp,std::ios::binary);st.write("R15GC127",8);st.write(binding.data(),64);st.write(parent.data(),64);
  u64(st,next);u32(st,127);u32(st,q);u32(st,D);u32(st,processed);u32(st,rank);u32(st,maxInput+1);st.put(char(inRow));st.put(char(finalized));
  u32(st,currentRaw);u32(st,currentNode);u64(st,reductions);u64(st,swaps);u64(st,inputOffset);u64(st,dagBytes);
  for(int c=0;c<q;c++){
   const auto&P=piv[c];st.put(char(bool(P.data)));if(!P.data)continue;
   st.put(char(P.degree));st.put(char(P.coefficient));u32(st,P.node);write_words(st,(*P.data)[0]);
  }
  if(inRow)write_words(st,current);
  st.write("ENDGC127",8);st.close();need(bool(st),"whole GB state flush");fs::rename(tmp,statePath);
  std::ofstream a(selector+".tmp",std::ios::binary);a.write("R15GA127",8);a.write(binding.data(),64);u64(a,next);u32(a,slot);a.write("ENDGA127",8);
  a.close();need(bool(a),"active GB checkpoint");fs::rename(selector+".tmp",selector);generation=next;lastCheckpoint=seconds();
  writeReceipt(status);
 };
 if(!resumed)checkpoint("prefix-ready");
 while(processed<ns){
  if(!inRow){
   if(seconds()>=budget){checkpoint("budget-checkpoint");return 75;}
   int target;current=readRow(currentRaw,target);
   need(currentRaw>=1&&currentRaw<=6188&&target==0,"complete original source row identity");
   currentNode=processed+1;inRow=true;
   Lead L=lead(current);maxInput=std::max(maxInput,L.degree);
   dag.put('I');u32(dag,processed+1);u32(dag,currentRaw);
  }
  Lead L=lead(current);
  while(L.degree>=0){
   if(seconds()>=budget){checkpoint("budget-checkpoint");return 75;}
   auto &P=piv[L.component];
   if(!P.data){
    P.data=std::make_unique<Triple>();(*P.data)[0]=std::move(current);BitOps::refresh(*P.data,nw,0);
    P.degree=L.degree;P.coefficient=L.coefficient;P.node=currentNode;rank++;
    dag.put('B');u16(dag,L.component+1);u32(dag,currentNode);break;
   }
   if(P.degree>L.degree){
    std::swap(current,(*P.data)[0]);std::swap(currentNode,P.node);
    std::swap(L.degree,P.degree);std::swap(L.coefficient,P.coefficient);
    BitOps::refresh(*P.data,nw,0);swaps++;
    dag.put('S');u16(dag,L.component+1);u32(dag,currentNode);u32(dag,P.node);
   }
   int shift=L.degree-P.degree,a=L.coefficient*ops.inv[P.coefficient]%127;
   need(shift>=0&&shift<=D&&a>0,"actual Euclidean cancellation");
   const auto R=ops.rep[127-a];
   BitOps::add(current,nw,shift*W,(*P.data)[R.c],nw,0,(P.degree+1)*W,R.rot,R.neg);
   dag.put('R');u32(dag,currentNode);u32(dag,P.node);dag.put(char(shift));dag.put(char(a));
   reductions++;need(reductions+uint64_t(ns)<=UINT32_MAX,"exact source DAG node range");
   currentNode=uint32_t(ns+reductions);Lead next=lead(current,L.degree);
   need(next.degree<L.degree||(next.degree==L.degree&&next.component>L.component),"strict original module leading-term decrease");
   L=next;
   if(seconds()-lastCheckpoint>=30)checkpoint("active-original-source-checkpoint");
  }
  if(L.degree<0){dag.put('Z');u32(dag,currentNode);}
  inRow=false;current.clear();processed++;
  if(processed==1||processed%25==0||processed==ns)
   std::cout<<"{\"phase\":\"original127-streaming-gb\",\"processedSources\":"<<processed<<",\"basisRank\":"<<rank
    <<",\"reductions\":"<<reductions<<",\"swaps\":"<<swaps<<",\"elapsedSeconds\":"<<seconds()<<"}\n"<<std::flush;
  if(seconds()-lastCheckpoint>=30)checkpoint("whole-original-source-prefix");
 }
 checkpoint("all-original-sources-complete");
 std::vector<Row> targets;
 for(int j=0;j<nt;j++){
  int raw,target;targets.push_back(readRow(raw,target));need(raw==0&&target==j+2,"all original target identities");
 }
 need(in.peek()==EOF,"full original NF EOF");in.clear();in.seekg(0,std::ios::end);
 const std::string basisPath=prefix+"-basis.bin",tmp=basisPath+".tmp";
 std::ofstream basis(tmp,std::ios::binary);basis.write("R15GB127",8);basis.write(binding.data(),64);
 for(int n:{127,q,D,rank,nt})u32(basis,n);
 int maxDegree=-1,totalDegrees=0,column=0;
 for(int c=0;c<q;c++)if(piv[c].data){
  const auto&P=piv[c];Lead L=lead((*P.data)[0]);
  need(L.component==c&&L.degree==P.degree&&L.coefficient==P.coefficient,"complete final distinct-leading-component basis");
  Row normalized=(*P.data)[0];int scale=ops.inv[P.coefficient];ops.multiple(normalized,nw,0,scale);
  need(lead(normalized).coefficient==1,"monic complete final basis");
  u16(basis,c+1);basis.put(char(P.degree));u32(basis,P.node);basis.put(char(scale));write_words(basis,normalized);
  dag.put('F');u16(dag,c+1);u32(dag,P.node);dag.put(char(scale));
  maxDegree=std::max(maxDegree,P.degree);totalDegrees+=P.degree;column++;
 }
 need(column==rank,"every final basis source retained");
 for(const auto&row:targets)write_words(basis,row);
 basis.write("ENDGB127",8);basis.close();need(bool(basis),"complete original basis flush");fs::rename(tmp,basisPath);
 std::ofstream meta(prefix+"-basis-metadata.json.tmp");
 meta<<"{\"format\":\"r150-original127-complete-graded-basis-v1\",\"binding\":\""<<binding
  <<"\",\"prime\":127,\"components\":1034,\"processedOriginalSources\":"<<ns<<",\"basisRank\":"<<rank
  <<",\"maximumBasisDegree\":"<<maxDegree<<",\"sumBasisDegrees\":"<<totalDegrees<<",\"freeModuleRank\":"<<q-rank
  <<",\"originalTargetCount\":9,\"allOriginalSourceDAGRetained\":true,\"noParameterPolynomialInverted\":true}\n";
 meta.close();need(bool(meta),"basis metadata");fs::rename(prefix+"-basis-metadata.json.tmp",prefix+"-basis-metadata.json");
 finalized=true;checkpoint("completed");
 std::cout<<"{\"status\":\"original127-graded-module-basis-complete\",\"basisRank\":"<<rank<<",\"maximumBasisDegree\":"<<maxDegree
  <<",\"sumBasisDegrees\":"<<totalDegrees<<",\"elapsedSeconds\":"<<seconds()<<"}\n"<<std::flush;
 return 0;
}catch(const std::exception&e){std::cerr<<"ORIGINAL127_GB_FAILED "<<e.what()<<"\n";return 1;}}
