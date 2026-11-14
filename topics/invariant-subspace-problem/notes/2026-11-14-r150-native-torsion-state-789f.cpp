// Exact finite normal-form state space from the COMPLETE original F31[s] GB.
// This computes the whole torsion submodule, not merely nine annihilators.
// Its input completeness and hashes are checked by the accompanying runner.
#define main r150_frozen_normal_form_main
#include "2026-11-14-r150-native-normal-form-789f.cpp"
#undef main

struct StatePivot {std::unique_ptr<Triple> rows;int degree=-1,column=-1;};
struct StateOp {uint16_t column;uint8_t shift,coefficient;};
using Bytes=std::vector<uint8_t>;

int main(int argc,char **argv){try{
 if(argc!=3)return 2;
 auto start=std::chrono::steady_clock::now();auto seconds=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 const int q=1034,D=45,W=(q+31)/32,nw=(D+1)*W,expectedRank=1021;
 std::ifstream in(argv[1]);if(!in)throw std::runtime_error("input open");
 std::string first,second;std::getline(in,first);std::getline(in,second);
 if(first.rfind("98 ",0)!=0||second.rfind("15 ",0)!=0)throw std::runtime_error("SSI runtime header");
 int tag,rank,columns;in>>tag>>rank>>columns;
 if(tag!=10||rank!=q||columns!=expectedRank)throw std::runtime_error("not the complete basis dimensions");
 BitOps ops;std::vector<StatePivot> piv(q);int B=0,totalDegrees=0;
 auto readVector=[&](int &leadDegree,int &leadComponent,int &leadCoefficient){
  uint32_t count;in>>count;if(!in||count>uint32_t(q*(D+1)))throw std::runtime_error("term count");
  Row row(5*nw);int lastDegree=D+1,lastComponent=-1;leadDegree=-1;leadComponent=-1;leadCoefficient=0;
  for(uint32_t z=0;z<count;z++){
   int a,c,k;in>>a>>c>>k;c--;
   if(!in||a<1||a>30||c<0||c>=q||k<0||k>D||k>lastDegree||(k==lastDegree&&c<=lastComponent))throw std::runtime_error("SSI graded monomial order or coefficient");
   if(!z){leadDegree=k;leadComponent=c;leadCoefficient=a;}
   BitOps::set(row,nw,k*W*32+c,a);lastDegree=k;lastComponent=c;
  }return row;
 };
 for(int j=0;j<columns;j++){
  int d,c,a;Row row=readVector(d,c,a);if(d<0||a!=1||piv[c].rows)throw std::runtime_error("basis must have distinct monic leading components");
  auto &P=piv[c];P.rows=std::make_unique<Triple>();(*P.rows)[0]=std::move(row);BitOps::refresh(*P.rows,nw,0);P.degree=d;P.column=j;
  B=std::max(B,d);totalDegrees+=d;
 }
 if(B!=8||totalDegrees!=716)throw std::runtime_error("complete basis degree profile mismatch");
 int nt;in>>tag>>rank>>nt;if(tag!=10||rank!=q||nt!=9)throw std::runtime_error("original nine targets");
 std::vector<Row> targets;for(int j=0;j<nt;j++){int d,c,a;targets.push_back(readVector(d,c,a));}
 std::string extra;if(in>>extra)throw std::runtime_error("trailing SSI object");
 std::vector<int> freeComponents,freeIndex(q,-1),coordinateIndex(q*B,-1);
 std::vector<std::pair<int,int>> coordinates;
 for(int c=0;c<q;c++)if(!piv[c].rows){freeIndex[c]=freeComponents.size();freeComponents.push_back(c);}
 for(int d=0;d<B;d++)for(int c=0;c<q;c++)if(!piv[c].rows||d<piv[c].degree){coordinateIndex[d*q+c]=coordinates.size();coordinates.push_back({c,d});}
 const int n=coordinates.size(),nf=freeComponents.size();if(n!=820||nf!=13)throw std::runtime_error("finite state dimensions");
 std::string prefix=argv[2];std::ofstream trace(prefix+"-normal-operations.bin",std::ios::binary);
 if(!trace)throw std::runtime_error("operation output open");trace.write("R150FWOP",8);u32(trace,q);u32(trace,n);u32(trace,nt);
 uint64_t normalOperations=0;
 auto normal=[&](Row &v,char kind,int index){
  std::vector<StateOp> steps;
  for(int d=D;d>=0;d--)for(int c=0;c<q;c++){
   const auto &P=piv[c];if(!P.rows||d<P.degree)continue;int a=BitOps::get(v,nw,d*W*32+c);if(!a)continue;
   int shift=d-P.degree;auto rep=ops.rep[31-a];BitOps::add(v,nw,shift*W,(*P.rows)[rep.c],nw,0,(P.degree+1)*W,rep.rot,rep.neg);
   if(BitOps::get(v,nw,d*W*32+c))throw std::runtime_error("normal-form pivot failed");
   steps.push_back({uint16_t(P.column+1),uint8_t(shift),uint8_t(a)});
  }
  trace.put(kind);u16(trace,index+1);u32(trace,steps.size());for(auto e:steps){u16(trace,e.column);trace.put(char(e.shift));trace.put(char(e.coefficient));}normalOperations+=steps.size();
 };
 Bytes A(n*n),C(nf*n),targetStates(nt*n);
 auto extract=[&](const Row &v,Bytes &dest,int column,bool allowLeakage){
  for(int d=0;d<=D;d++)for(int c=0;c<q;c++){
   int a=BitOps::get(v,nw,d*W*32+c);if(!a)continue;
   if(d<B){int ix=coordinateIndex[d*q+c];if(ix<0)throw std::runtime_error("retained divisible monomial");dest[ix*n+column]=a;}
   else if(allowLeakage&&d==B&&freeIndex[c]>=0)C[freeIndex[c]*n+column]=a;
   else throw std::runtime_error("normal form outside certified finite state or leakage");
  }
 };
 for(int j=0;j<n;j++){
  Row v(5*nw);auto [c,d]=coordinates[j];BitOps::set(v,nw,(d+1)*W*32+c,1);normal(v,'A',j);extract(v,A,j,true);
  if((j+1)%100==0||j+1==n)std::cout<<"{\"phase\":\"state-columns\",\"completed\":"<<j+1<<",\"total\":"<<n<<",\"normalOperations\":"<<normalOperations<<",\"elapsedSeconds\":"<<seconds()<<"}\n"<<std::flush;
 }
 for(int j=0;j<nt;j++){
  normal(targets[j],'T',j);
  for(int d=0;d<=D;d++)for(int c=0;c<q;c++){
   int a=BitOps::get(targets[j],nw,d*W*32+c);if(!a)continue;
   int ix=d<B?coordinateIndex[d*q+c]:-1;if(ix<0)throw std::runtime_error("original target is not a degree-bounded normal form");targetStates[j*n+ix]=a;
  }
 }
 trace.close();if(!trace)throw std::runtime_error("operation output failed");
 std::cout<<"{\"phase\":\"complete-state-built\",\"stateDimension\":"<<n<<",\"leakageDimension\":"<<nf<<",\"normalOperations\":"<<normalOperations<<",\"elapsedSeconds\":"<<seconds()<<"}\n"<<std::flush;

 // Row space of C, CA, ... . Each block is multiplied exactly, with no
 // truncation of quotient normal forms before checking the leakage.
 const int gw=(n+31)/32;std::vector<std::unique_ptr<Triple>> observed(n);
 std::vector<std::pair<int,int>> selected;std::vector<int> rankHistory;Bytes current=C;
 int observationRank=0,stableAt=-1;uint64_t linearReductions=0;
 auto insert=[&](const uint8_t *source,int layer,int output){
  Row v(5*gw);for(int j=0;j<n;j++)BitOps::set(v,gw,j,source[j]);
  for(int p=0;p<n;p++){
   int a=BitOps::get(v,gw,p);if(!a)continue;
   if(observed[p]){auto rep=ops.rep[31-a];BitOps::add(v,gw,p/32,(*observed[p])[rep.c],gw,p/32,gw-p/32,rep.rot,rep.neg);linearReductions++;}
   else{ops.multiple(v,gw,p/32,ops.inv[a]);auto t=std::make_unique<Triple>();(*t)[0]=std::move(v);BitOps::refresh(*t,gw,p/32);observed[p]=std::move(t);observationRank++;selected.push_back({layer,output});return;}
  }
 };
 for(int layer=0;layer<=n;layer++){
  int before=observationRank;for(int row=0;row<nf;row++)insert(current.data()+row*n,layer,row);
  rankHistory.push_back(observationRank);
  std::cout<<"{\"phase\":\"observability\",\"power\":"<<layer<<",\"rank\":"<<observationRank<<",\"elapsedSeconds\":"<<seconds()<<"}\n"<<std::flush;
  if(observationRank==before){stableAt=layer;break;}
  Bytes next(nf*n);for(int row=0;row<nf;row++){
   std::vector<uint32_t> sums(n);for(int k=0;k<n;k++){uint32_t a=current[row*n+k];if(a)for(int col=0;col<n;col++)sums[col]+=a*A[k*n+col];}
   for(int col=0;col<n;col++)next[row*n+col]=sums[col]%31;
  }current.swap(next);
 }
 if(stableAt<0)throw std::runtime_error("observability failed to stabilize within dimension bound");
 const int tdim=n-observationRank;std::vector<int> freeState,pivotState;
 for(int p=0;p<n;p++)(observed[p]?pivotState:freeState).push_back(p);
 Bytes kernel(tdim*n);
 for(int j=0;j<tdim;j++){
  auto *v=kernel.data()+j*n;v[freeState[j]]=1;
  for(int p=n-1;p>=0;p--)if(observed[p]){uint32_t sum=0;for(int c=p+1;c<n;c++)sum+=BitOps::get((*observed[p])[0],gw,c)*v[c];v[p]=(31-sum%31)%31;}
 }
 Bytes action(tdim*tdim),targetCoordinates(nt*tdim);
 for(int j=0;j<tdim;j++){
  const auto *v=kernel.data()+j*n;Bytes av(n);
  for(int row=0;row<n;row++){uint32_t sum=0;for(int k=0;k<n;k++)sum+=A[row*n+k]*v[k];av[row]=sum%31;}
  for(int row=0;row<nf;row++){uint32_t sum=0;for(int k=0;k<n;k++)sum+=C[row*n+k]*v[k];if(sum%31)throw std::runtime_error("kernel retained leakage");}
  for(int k=0;k<tdim;k++)action[k*tdim+j]=av[freeState[k]];
  for(int row=0;row<n;row++){uint32_t sum=0;for(int k=0;k<tdim;k++)sum+=kernel[k*n+row]*action[k*tdim+j];if(sum%31!=av[row])throw std::runtime_error("finite torsion kernel is not invariant");}
 }
 for(int j=0;j<nt;j++){
  for(int k=0;k<tdim;k++)targetCoordinates[j*tdim+k]=targetStates[j*n+freeState[k]];
  for(int row=0;row<n;row++){uint32_t sum=0;for(int k=0;k<tdim;k++)sum+=kernel[k*n+row]*targetCoordinates[j*tdim+k];if(sum%31!=targetStates[j*n+row])throw std::runtime_error("original target not in entire torsion space");}
 }
 // Binary dense exact certificate: all scalar entries are canonical F31 bytes.
 std::ofstream out(prefix+"-state.bin",std::ios::binary),meta(prefix+"-state.json");if(!out||!meta)throw std::runtime_error("state output open");
 out.write("R150FW31",8);for(int v:{q,B,n,nf,tdim,nt,observationRank,stableAt})u32(out,v);
 for(auto [c,d]:coordinates){u16(out,c+1);out.put(char(d));}for(int c:freeComponents)u16(out,c+1);
 auto writeBytes=[&](const Bytes &v){out.write(reinterpret_cast<const char*>(v.data()),v.size());};
 writeBytes(A);writeBytes(C);writeBytes(targetStates);writeBytes(kernel);writeBytes(action);writeBytes(targetCoordinates);
 for(int p:pivotState){u16(out,p+1);for(int j=0;j<n;j++)out.put(char(BitOps::get((*observed[p])[0],gw,j)));}
 for(auto [layer,row]:selected){u16(out,layer);u16(out,row+1);}
 meta<<"{\"format\":\"r150-whole-torsion-state-v1\",\"field\":31,\"components\":"<<q<<",\"basisRank\":1021,\"maximumBasisDegree\":"<<B<<",\"sumBasisDegrees\":"<<totalDegrees<<",\"stateDimension\":"<<n<<",\"leakageDimension\":"<<nf<<",\"observabilityRank\":"<<observationRank<<",\"torsionDimension\":"<<tdim<<",\"stableAtPower\":"<<stableAt<<",\"rankHistory\":[";
 for(int i=0;i<int(rankHistory.size());i++){if(i)meta<<",";meta<<rankHistory[i];}meta<<"],\"targets\":[2,3,4,5,6,7,8,9,10],\"allTargetsInTorsion\":true,\"normalOperations\":"<<normalOperations<<",\"linearReductions\":"<<linearReductions<<",\"sourceIdentity\":\"Each state column is the full normal form of s times a recorded standard monomial. Each target is the full normal form of its original saved target. Recorded steps subtract coefficient*s^shift times a numbered complete GB row.\"}\n";
 out.close();meta.close();if(!out||!meta)throw std::runtime_error("state output failed");
 std::cout<<"{\"status\":\"whole-torsion-state-complete\",\"stateDimension\":"<<n<<",\"observabilityRank\":"<<observationRank<<",\"torsionDimension\":"<<tdim<<",\"stableAtPower\":"<<stableAt<<",\"allTargetsInTorsion\":true,\"normalOperations\":"<<normalOperations<<",\"linearReductions\":"<<linearReductions<<",\"elapsedSeconds\":"<<seconds()<<"}\n";
 return 0;
}catch(const std::exception &e){std::cerr<<"NATIVE_TORSION_STATE_FAILED "<<e.what()<<"\n";return 1;}}
