// Whole original F127 torsion from complete standard forms and all free leakage.
// Author: Astra-ISP-789f / normal_annihilator.
// AI-assisted: GPT-6 Astra Pro. Date: 2026-11-15.
#include "2026-11-15-r150-original-f127-bitplane-789f.hpp"
#include <chrono>
#include <filesystem>
#include <iomanip>
#include <iostream>
#include <memory>
#include <utility>
namespace fs=std::filesystem;
using Bytes=std::vector<uint8_t>;
static void need(bool b,const std::string&s){if(!b)throw std::runtime_error(s);}
static void expect(std::istream&i,const char*m){char b[8];i.read(b,8);need(i&&std::string(b,8)==std::string(m,8),"exact binary magic");}
static void check_binding(std::istream&i,const std::string&s){char b[64];i.read(b,64);need(i&&std::string(b,64)==s,"exact source binding");}
static void write_words(std::ostream&o,const Row&r){for(auto x:r)u32(o,x);}
static Row read_words(std::istream&i,size_t n){Row r(n);for(auto&x:r)x=uint32_t(read_le(i,4));return r;}
static void write_bytes(std::ostream&o,const Bytes&b){if(!b.empty())o.write(reinterpret_cast<const char*>(b.data()),b.size());}
static Bytes read_bytes(std::istream&i,size_t n){Bytes b(n);if(n)i.read(reinterpret_cast<char*>(b.data()),n);need(bool(i),"complete byte array");return b;}
struct Pivot{std::unique_ptr<Triple> rows;int degree=-1,column=-1;uint32_t originalNode=0;};
struct Operation{uint16_t column;uint8_t shift,coefficient;};
int main(int argc,char**argv){try{
 if(argc!=6)return 2;
 const std::string input=argv[1],prefix=argv[2],parent=argv[3],binding=argv[4];
 const double budget=std::stod(argv[5]);
 need(parent.size()==64&&binding.size()==64&&budget>0&&budget<=1800,"bounded whole torsion arguments");
 auto started=std::chrono::steady_clock::now();
 auto seconds=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count();};
 BitOps ops;const uint64_t arithmeticChecks=ops.verify();
 std::ifstream in(input,std::ios::binary);expect(in,"R15GB127");check_binding(in,parent);
 int prime=read_le(in,4),q=read_le(in,4),D=read_le(in,4),rank=read_le(in,4),nt=read_le(in,4);
 need(prime==127&&q==1034&&D==45&&rank>=0&&rank<=q&&nt==9,"complete original127 graded basis");
 const int W=(q+31)/32,nw=(D+1)*W;
 std::vector<Pivot> piv(q);int B=0,totalDegrees=0,previous=-1;
 auto lead=[&](const Row&r){
  for(int d=D;d>=0;d--)for(int c=0;c<q;c++){int a=BitOps::get(r,nw,d*W*32+c);if(a)return std::array<int,3>{d,c,a};}
  return std::array<int,3>{-1,-1,0};
 };
 for(int j=0;j<rank;j++){
  int c=int(read_le(in,2))-1,d=read_le(in,1);uint32_t node=read_le(in,4);int scale=read_le(in,1);
  need(previous<c&&c<q&&d<=D&&node>0&&scale>0&&scale<127,"all monic basis original source records");previous=c;
  auto&P=piv[c];P.degree=d;P.column=j;P.originalNode=node;P.rows=std::make_unique<Triple>();
  (*P.rows)[0]=read_words(in,7*nw);auto L=lead((*P.rows)[0]);
  need(L[0]==d&&L[1]==c&&L[2]==1,"actual distinct monic leading components");
  BitOps::refresh(*P.rows,nw,0);B=std::max(B,d);totalDegrees+=d;
 }
 std::vector<Row> originalTargets(nt);
 for(auto&t:originalTargets)t=read_words(in,7*nw);
 expect(in,"ENDGB127");need(in.get()==EOF,"complete original basis/target EOF");
 std::vector<int> freeComponents,freeIndex(q,-1),coordinateIndex(q*B,-1);
 std::vector<std::pair<int,int>> coordinates;
 for(int c=0;c<q;c++)if(!piv[c].rows){freeIndex[c]=freeComponents.size();freeComponents.push_back(c);}
 for(int d=0;d<B;d++)for(int c=0;c<q;c++)if(!piv[c].rows||d<piv[c].degree){
  coordinateIndex[d*q+c]=coordinates.size();coordinates.push_back({c,d});
 }
 const int n=coordinates.size(),nf=freeComponents.size(),gw=(n+31)/32;
 need(n==totalDegrees+B*nf&&nf==q-rank,"complete finite window dimension, including all free directions");
 need(n<=8192,"finite window exceeds this bounded allocation gate; no torsion conclusion");
 Bytes A(size_t(n)*n),C(size_t(nf)*n),targetStates(size_t(nt)*n),targetBounded(nt,0);
 Bytes current,next,kernel,action,targetCoordinates,targetInTorsion(nt,0);
 std::vector<std::unique_ptr<Triple>> observed(n);
 std::vector<std::pair<int,int>> selected;
 std::vector<int> rankHistory,freeState,pivotState;
 int phase=0,columnsDone=0,targetsDone=0,layer=0,observationRow=0,beforeRank=0,multiplyRow=0;
 int observationRank=0,stableAt=-1,verifiedKernelColumns=0,verifiedTargets=0,tdim=-1;
 uint64_t generation=0,traceBytes=0,normalOperations=0,linearReductions=0;
 uint64_t kernelOriginalLeakageProducts=0,kernelInvarianceProducts=0,kernelObservedProducts=0;
 bool resumed=false;
 const std::string selector=prefix+"-active.bin",tracePath=prefix+"-normal-operations.bin",receiptPath=prefix+"-native-receipt.json";
 auto restore_lists=[&](){
  freeState.clear();pivotState.clear();
  for(int c=0;c<n;c++)(observed[c]?pivotState:freeState).push_back(c);
 };
 if(fs::exists(selector)){
  std::ifstream sel(selector,std::ios::binary);expect(sel,"R15TA127");check_binding(sel,binding);
  generation=read_le(sel,8);int slot=read_le(sel,4);need(slot==int(generation%2),"whole torsion active slot");
  expect(sel,"ENDTA127");need(sel.get()==EOF,"torsion selector EOF");
  std::ifstream st(prefix+"-checkpoint-"+std::to_string(slot)+".bin",std::ios::binary);
  expect(st,"R15TC127");check_binding(st,binding);check_binding(st,parent);
  need(read_le(st,8)==generation,"whole torsion generation");
  for(int v:{127,q,D,rank,B,totalDegrees,n,nf,nt})need(read_le(st,4)==uint64_t(v),"identical dynamic torsion geometry");
  phase=read_le(st,4);columnsDone=read_le(st,4);targetsDone=read_le(st,4);
  layer=read_le(st,4);observationRow=read_le(st,4);beforeRank=read_le(st,4);multiplyRow=read_le(st,4);
  observationRank=read_le(st,4);stableAt=int(read_le(st,4))-1;
  verifiedKernelColumns=read_le(st,4);verifiedTargets=read_le(st,4);
  traceBytes=read_le(st,8);normalOperations=read_le(st,8);linearReductions=read_le(st,8);
  kernelOriginalLeakageProducts=read_le(st,8);kernelInvarianceProducts=read_le(st,8);kernelObservedProducts=read_le(st,8);
  need(phase>=0&&phase<=5&&columnsDone<=n&&targetsDone<=nt&&layer<=n&&observationRow<=nf&&multiplyRow<=nf&&observationRank<=n,"saved complete torsion counters");
  A=read_bytes(st,size_t(n)*n);C=read_bytes(st,size_t(nf)*n);
  targetStates=read_bytes(st,size_t(nt)*n);targetBounded=read_bytes(st,nt);targetInTorsion=read_bytes(st,nt);
  if(phase>=1){current=read_bytes(st,size_t(nf)*n);next=read_bytes(st,phase==2?size_t(nf)*n:0);}
  int count=read_le(st,4);need(count>=0&&count<=n+1,"saved observation history");
  for(int i=0;i<count;i++)rankHistory.push_back(read_le(st,4));
  count=read_le(st,4);need(count==observationRank,"all selected observation rows");
  for(int i=0;i<count;i++)selected.push_back({int(read_le(st,4)),int(read_le(st,4))});
  int actual=0;
  for(int p=0;p<n;p++){
   int present=read_le(st,1);need(present<=1,"saved observed pivot");
   if(!present)continue;
   auto t=std::make_unique<Triple>();(*t)[0]=read_words(st,7*gw);
   need(BitOps::get((*t)[0],gw,p)==1,"saved observed unit");
   for(int c=0;c<p;c++)need(BitOps::get((*t)[0],gw,c)==0,"saved observed echelon position");
   BitOps::refresh(*t,gw,p/32);observed[p]=std::move(t);actual++;
  }
  need(actual==observationRank,"complete saved observation rank");restore_lists();
  if(phase>=4){
   tdim=n-observationRank;kernel=read_bytes(st,size_t(tdim)*n);action=read_bytes(st,size_t(tdim)*tdim);
   targetCoordinates=read_bytes(st,size_t(nt)*tdim);
   need(verifiedKernelColumns<=tdim&&verifiedTargets<=nt,"saved verified candidate prefix");
  }
  expect(st,"ENDTC127");need(st.get()==EOF,"complete torsion checkpoint EOF");
  need(fs::exists(tracePath)&&fs::file_size(tracePath)>=traceBytes,"retained complete original state-operation prefix");
  fs::resize_file(tracePath,traceBytes);resumed=true;
 }else need(!fs::exists(tracePath),"unbound existing whole-torsion operation file");
 std::ofstream trace(tracePath,std::ios::binary|(resumed?std::ios::app:std::ios::trunc));
 need(bool(trace),"original state normal-form operation output");
 if(!resumed){trace.write("R15TW127",8);trace.write(binding.data(),64);for(int v:{q,n,nt,rank})u32(trace,v);}
 auto writeReceipt=[&](const char*status){
  std::ofstream r(receiptPath+".tmp");r<<std::setprecision(17);
  r<<"{\"format\":\"r150-original127-whole-torsion-native-v1\",\"status\":\""<<status<<"\",\"binding\":\""<<binding
   <<"\",\"parentGBBinding\":\""<<parent<<"\",\"prime\":127,\"generation\":"<<generation<<",\"activeSlot\":"<<int(generation%2)
   <<",\"phase\":"<<phase<<",\"components\":"<<q<<",\"basisRank\":"<<rank<<",\"maximumBasisDegree\":"<<B
   <<",\"sumBasisDegrees\":"<<totalDegrees<<",\"stateDimension\":"<<n<<",\"freeModuleRank\":"<<nf
   <<",\"stateColumnsComplete\":"<<columnsDone<<",\"originalTargetsNormalized\":"<<targetsDone
   <<",\"observationRank\":"<<observationRank<<",\"currentObservationPower\":"<<layer<<",\"stableAtPower\":"<<stableAt
   <<",\"torsionDimension\":"<<(phase>=3?n-observationRank:-1)<<",\"verifiedKernelColumns\":"<<verifiedKernelColumns
   <<",\"verifiedTargets\":"<<verifiedTargets<<",\"normalOperations\":"<<normalOperations<<",\"linearReductions\":"<<linearReductions
   <<",\"committedSourceTraceBytes\":"<<traceBytes<<",\"kernelOriginalLeakageProducts\":"<<kernelOriginalLeakageProducts
   <<",\"kernelInvarianceProducts\":"<<kernelInvarianceProducts<<",\"kernelObservedProducts\":"<<kernelObservedProducts
   <<",\"completeStateAndFreeLeakageVerified\":"<<(phase>=1?"true":"false")
   <<",\"actualObservationStableRowReductionVerified\":"<<(phase>=3?"true":"false")
   <<",\"allKernelAndActionProductsVerified\":"<<(phase==5?"true":"false")
   <<",\"wholeTorsionNotOnlyTargets\":true,\"allPolynomialFreeTailsRetained\":true,\"originalTargetBoundedFlags\":[";
  for(int j=0;j<nt;j++){if(j)r<<",";r<<int(targetBounded[j]);}
  r<<"],\"originalTargetInTorsionFlags\":[";
  for(int j=0;j<nt;j++){if(j)r<<",";r<<int(targetInTorsion[j]);}
  r<<"],\"rankHistory\":[";
  for(size_t j=0;j<rankHistory.size();j++){if(j)r<<",";r<<rankHistory[j];}
  r<<"],\"exhaustiveScalarArithmeticChecks\":"<<arithmeticChecks<<",\"checkpointResumed\":"<<(resumed?"true":"false")
   <<",\"old315Or820ProfileUsed\":false,\"elapsedSeconds\":"<<seconds()<<"}\n";
  r.close();need(bool(r),"whole torsion small receipt");fs::rename(receiptPath+".tmp",receiptPath);
 };
 double lastCheckpoint=seconds();
 auto checkpoint=[&](const char*status){
  trace.flush();need(bool(trace),"whole original-operation flush");traceBytes=uint64_t(trace.tellp());
  uint64_t nextGeneration=generation+1;int slot=nextGeneration%2;
  std::string path=prefix+"-checkpoint-"+std::to_string(slot)+".bin";
  std::ofstream st(path+".tmp",std::ios::binary);st.write("R15TC127",8);st.write(binding.data(),64);st.write(parent.data(),64);u64(st,nextGeneration);
  for(int v:{127,q,D,rank,B,totalDegrees,n,nf,nt})u32(st,v);
  for(int v:{phase,columnsDone,targetsDone,layer,observationRow,beforeRank,multiplyRow,observationRank,stableAt+1,verifiedKernelColumns,verifiedTargets})u32(st,v);
  for(uint64_t v:{traceBytes,normalOperations,linearReductions,kernelOriginalLeakageProducts,kernelInvarianceProducts,kernelObservedProducts})u64(st,v);
  for(const auto*b:{&A,&C,&targetStates,&targetBounded,&targetInTorsion})write_bytes(st,*b);
  if(phase>=1){write_bytes(st,current);if(phase==2)write_bytes(st,next);}
  u32(st,rankHistory.size());for(int v:rankHistory)u32(st,v);
  u32(st,selected.size());for(auto [k,r]:selected){u32(st,k);u32(st,r);}
  for(int p=0;p<n;p++){st.put(char(bool(observed[p])));if(observed[p])write_words(st,(*observed[p])[0]);}
  if(phase>=4){write_bytes(st,kernel);write_bytes(st,action);write_bytes(st,targetCoordinates);}
  st.write("ENDTC127",8);st.close();need(bool(st),"whole torsion state flush");fs::rename(path+".tmp",path);
  std::ofstream a(selector+".tmp",std::ios::binary);a.write("R15TA127",8);a.write(binding.data(),64);u64(a,nextGeneration);u32(a,slot);a.write("ENDTA127",8);
  a.close();need(bool(a),"whole torsion selector");fs::rename(selector+".tmp",selector);generation=nextGeneration;lastCheckpoint=seconds();writeReceipt(status);
 };
 auto budget_stop=[&](){if(seconds()<budget)return false;checkpoint("budget-checkpoint");return true;};
 if(phase==5){need(fs::exists(prefix+"-whole-state.bin"),"completed whole torsion certificate retained");writeReceipt("completed");return 0;}
 if(!resumed)checkpoint("state-ready");
 auto normal=[&](Row&v,char kind,int index){
  std::vector<Operation> steps;
  for(int d=D;d>=0;d--)for(int c=0;c<q;c++){
   const auto&P=piv[c];if(!P.rows||d<P.degree)continue;
   int a=BitOps::get(v,nw,d*W*32+c);if(!a)continue;need(a<127,"canonical original normal coefficient");
   int shift=d-P.degree;const auto r=ops.rep[127-a];
   BitOps::add(v,nw,shift*W,(*P.rows)[r.c],nw,0,(P.degree+1)*W,r.rot,r.neg);
   need(BitOps::get(v,nw,d*W*32+c)==0,"actual complete standard-form cancellation");
   steps.push_back({uint16_t(P.column+1),uint8_t(shift),uint8_t(a)});
  }
  trace.put(kind);u32(trace,index);u32(trace,steps.size());
  for(auto e:steps){u16(trace,e.column);trace.put(char(e.shift));trace.put(char(e.coefficient));}
  normalOperations+=steps.size();
 };
 while(phase==0&&columnsDone<n){
  if(budget_stop())return 75;
  int j=columnsDone;Row v(7*nw);auto[c,d]=coordinates[j];
  BitOps::set(v,nw,(d+1)*W*32+c,1);normal(v,'A',j);
  for(int k=0;k<=D;k++)for(int a=0;a<q;a++){
   int value=BitOps::get(v,nw,k*W*32+a);if(!value)continue;need(value<127,"canonical full state normal form");
   if(k<B){int ix=coordinateIndex[k*q+a];need(ix>=0,"no divisible monomial in complete state");A[size_t(ix)*n+j]=value;}
   else if(k==B&&freeIndex[a]>=0)C[size_t(freeIndex[a])*n+j]=value;
   else throw std::runtime_error("state normal form outside complete finite window and all free leakage");
  }
  columnsDone++;
  if(seconds()-lastCheckpoint>=5)checkpoint("complete-state-column-prefix");
 }
 while(phase==0&&targetsDone<nt){
  if(budget_stop())return 75;
  int j=targetsDone;Row v=originalTargets[j];normal(v,'T',j);bool bounded=true;
  for(int d=0;d<=D;d++)for(int c=0;c<q;c++){
   int value=BitOps::get(v,nw,d*W*32+c);if(!value)continue;need(value<127,"canonical full target normal form");
   if(d<B){int ix=coordinateIndex[d*q+c];need(ix>=0,"target retains no divisible monomial");targetStates[size_t(j)*n+ix]=value;}
   else {need(freeIndex[c]>=0,"high target normal form is a true free polynomial tail");bounded=false;}
  }
  targetBounded[j]=bounded;
  std::string p=prefix+"-target-"+std::to_string(j+2)+".bin";
  std::ofstream t(p+".tmp",std::ios::binary);t.write("R15TN127",8);t.write(binding.data(),64);u32(t,j+2);u32(t,q);u32(t,D);write_words(t,v);
  t.write("ENDTN127",8);t.close();need(bool(t),"entire original target polynomial tail");fs::rename(p+".tmp",p);
  targetsDone++;checkpoint("complete-original-target-prefix");
 }
 if(phase==0){phase=1;current=C;beforeRank=observationRank;checkpoint("complete-state-and-all-free-leakage");}
 auto insert=[&](const uint8_t*source,int power,int output){
  Row v(7*gw);for(int j=0;j<n;j++)BitOps::set(v,gw,j,source[j]);
  for(int p=0;p<n;p++){
   int a=BitOps::get(v,gw,p);if(!a)continue;need(a<127,"canonical complete observation row");
   if(observed[p]){
    const auto r=ops.rep[127-a];BitOps::add(v,gw,p/32,(*observed[p])[r.c],gw,p/32,gw-p/32,r.rot,r.neg);linearReductions++;
   }else{
    ops.multiple(v,gw,p/32,ops.inv[a]);auto t=std::make_unique<Triple>();(*t)[0]=std::move(v);BitOps::refresh(*t,gw,p/32);
    observed[p]=std::move(t);observationRank++;selected.push_back({power,output});return;
   }
  }
  for(int j=0;j<n;j++)need(BitOps::get(v,gw,j)==0,"whole new observation row lies in the saved row span");
 };
 while(phase==1||phase==2){
  need(layer<=n,"whole observability dimension stopping bound");
  if(phase==1){
   while(observationRow<nf){
    if(budget_stop())return 75;
    insert(n?current.data()+size_t(observationRow)*n:nullptr,layer,observationRow);observationRow++;
    if(seconds()-lastCheckpoint>=5)checkpoint("complete-observation-row-prefix");
   }
   rankHistory.push_back(observationRank);
   std::cout<<"{\"phase\":\"complete-free-observability\",\"power\":"<<layer<<",\"rank\":"<<observationRank<<",\"elapsedSeconds\":"<<seconds()<<"}\n"<<std::flush;
   if(observationRank==beforeRank){stableAt=layer;phase=3;checkpoint("whole-observation-space-stable");break;}
   phase=2;multiplyRow=0;next.assign(size_t(nf)*n,0);checkpoint("whole-observation-layer-complete");
  }
  while(phase==2&&multiplyRow<nf){
   if(budget_stop())return 75;
   std::vector<uint32_t>sums(n);const int row=multiplyRow;
   for(int k=0;k<n;k++){uint32_t a=current[size_t(row)*n+k];if(a)for(int col=0;col<n;col++)sums[col]+=a*A[size_t(k)*n+col];}
   for(int col=0;col<n;col++)next[size_t(row)*n+col]=sums[col]%127;
   multiplyRow++;if(seconds()-lastCheckpoint>=5)checkpoint("complete-next-observation-row-prefix");
  }
  if(phase==2){
   current.swap(next);next.clear();layer++;observationRow=0;beforeRank=observationRank;phase=1;
   if(seconds()-lastCheckpoint>=5)checkpoint("next-observation-layer-ready");
  }
 }
 if(phase==3){
  if(budget_stop())return 75;
  restore_lists();tdim=n-observationRank;need(int(freeState.size())==tdim,"complete torsion kernel dimension");
  kernel.assign(size_t(tdim)*n,0);action.assign(size_t(tdim)*tdim,0);targetCoordinates.assign(size_t(nt)*tdim,0);
  for(int j=0;j<tdim;j++){
   uint8_t*v=kernel.data()+size_t(j)*n;v[freeState[j]]=1;
   for(int p=n-1;p>=0;p--)if(observed[p]){
    uint32_t sum=0;for(int c=p+1;c<n;c++)sum+=BitOps::get((*observed[p])[0],gw,c)*v[c];
    v[p]=(127-sum%127)%127;
   }
   for(int k=0;k<tdim;k++){
    uint32_t sum=0;int row=freeState[k];for(int a=0;a<n;a++)sum+=A[size_t(row)*n+a]*v[a];
    action[size_t(k)*tdim+j]=sum%127;
   }
  }
  for(int j=0;j<nt;j++)if(targetBounded[j])for(int k=0;k<tdim;k++)targetCoordinates[size_t(j)*tdim+k]=targetStates[size_t(j)*n+freeState[k]];
  phase=4;checkpoint("complete-kernel-and-action-candidates-saved");
 }
 while(phase==4&&verifiedKernelColumns<tdim){
  if(budget_stop())return 75;
  int j=verifiedKernelColumns;const uint8_t*v=kernel.data()+size_t(j)*n;
  for(int k=0;k<tdim;k++)need(v[freeState[k]]==int(k==j),"entire torsion free-coordinate identity");
  for(int p:pivotState){
   uint32_t sum=0;for(int c=0;c<n;c++)sum+=BitOps::get((*observed[p])[0],gw,c)*v[c];
   need(sum%127==0,"all complete observation rows annihilate kernel");kernelObservedProducts++;
  }
  for(int row=0;row<nf;row++){
   uint32_t sum=0;for(int k=0;k<n;k++)sum+=C[size_t(row)*n+k]*v[k];
   need(sum%127==0,"all original free leakage products");kernelOriginalLeakageProducts++;
  }
  for(int row=0;row<n;row++){
   uint32_t av=0,kv=0;
   for(int k=0;k<n;k++)av+=A[size_t(row)*n+k]*v[k];
   for(int k=0;k<tdim;k++)kv+=kernel[size_t(k)*n+row]*action[size_t(k)*tdim+j];
   need(av%127==kv%127,"all full finite-state invariance products");kernelInvarianceProducts++;
  }
  verifiedKernelColumns++;if(seconds()-lastCheckpoint>=5)checkpoint("verified-whole-torsion-column-prefix");
 }
 while(phase==4&&verifiedTargets<nt){
  if(budget_stop())return 75;
  int j=verifiedTargets;bool member=targetBounded[j];
  if(member)for(int row=0;row<n;row++){
   uint32_t sum=0;for(int k=0;k<tdim;k++)sum+=kernel[size_t(k)*n+row]*targetCoordinates[size_t(j)*tdim+k];
   if(sum%127!=targetStates[size_t(j)*n+row])member=false;
  }
  targetInTorsion[j]=member;verifiedTargets++;checkpoint("verified-original-target-torsion-test");
 }
 if(phase==4){
  need(stableAt>=0&&verifiedKernelColumns==tdim&&verifiedTargets==nt,"entire torsion verification complete");
  const std::string path=prefix+"-whole-state.bin";std::ofstream out(path+".tmp",std::ios::binary);
  out.write("R15TS127",8);out.write(binding.data(),64);out.write(parent.data(),64);
  for(int v:{127,q,D,rank,B,totalDegrees,n,nf,tdim,nt,observationRank,stableAt})u32(out,v);
  for(auto[c,d]:coordinates){u16(out,c+1);out.put(char(d));}for(int c:freeComponents)u16(out,c+1);
  for(const auto*b:{&A,&C,&targetStates,&targetBounded,&targetInTorsion,&kernel,&action,&targetCoordinates})write_bytes(out,*b);
  for(int p:pivotState){u32(out,p);for(int c=0;c<n;c++)out.put(char(BitOps::get((*observed[p])[0],gw,c)));}
  for(auto[k,r]:selected){u32(out,k);u32(out,r);}
  out.write("ENDTS127",8);out.close();need(bool(out),"complete whole torsion certificate");fs::rename(path+".tmp",path);
  phase=5;checkpoint("completed");
 }
 need(phase==5,"completed whole torsion phase");return 0;
}catch(const std::exception&e){std::cerr<<"ORIGINAL127_WHOLE_TORSION_FAILED "<<e.what()<<"\n";return 1;}}
