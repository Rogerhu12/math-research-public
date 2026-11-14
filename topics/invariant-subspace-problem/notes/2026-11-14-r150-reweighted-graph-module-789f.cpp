// Reweight the COMPLETE original graph basis once, from T=64 to T=96.
// All 2195 graph vectors are kept, including the 972 already pure-source rows.
// A distinct-component output basis is certified by total output degree 716,
// the known complete original R module degree, not by pure-source tails.
#include "2026-11-14-r150-f31-bitplane-789f.hpp"
#include <sys/resource.h>
static uint32_t rg_u32(std::istream &in){uint32_t a=0;for(int k=0;k<4;k++){int c=in.get();if(c<0)throw std::runtime_error("truncated u32");a|=uint32_t(c)<<(8*k);}return a;}
static uint16_t rg_u16(std::istream &in){int a=in.get(),b=in.get();if(a<0||b<0)throw std::runtime_error("truncated u16");return a|(b<<8);}
struct RGSource {int raw=0,degree=0,group=-1,local=-1;};
struct RGGroup {int shift=0,oldShift=0,count=0,words=0,layers=0,wordOffset=0,componentOffset=0;std::vector<int> originalSources;};
struct RGLead {int degree=-1000,component=-1,coefficient=0;};
struct RGPivot {std::unique_ptr<Row> row;int degree=-1000,coefficient=0;};
int main(int argc,char **argv){try{
 if(argc!=4)return 2;double soft=std::stod(argv[3]);if(soft<=0)throw std::runtime_error("positive explicit soft bound required");
 uint32_t endian=1;if(*reinterpret_cast<uint8_t*>(&endian)!=1)throw std::runtime_error("little-endian bit-plane reader required");
 auto start=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 constexpr int ns=2195,qout=1034,T=96,D=8,minDegree=-81,oldT=64,oldD=45;
 std::ifstream in(argv[1],std::ios::binary);if(!in)throw std::runtime_error("old graph open");char magic[8];in.read(magic,8);
 if(std::string(magic,8)!="R150GG31")throw std::runtime_error("old graph magic");
 std::vector<int> dims;for(int j=0;j<9;j++)dims.push_back(rg_u32(in));
 if(dims!=std::vector<int>{2195,1034,2195,64,45,2195,2195,6,1})throw std::runtime_error("complete T64 original graph required");
 const std::array<int,6> expectedCounts{1034,6,66,396,11,1716};
 const std::array<int,6> originalDegrees{0,15,25,35,40,45};
 std::vector<RGGroup> groups(6);std::vector<RGSource> sources(ns);int nw=0,ncomponents=0,oldWords=0;
 for(int g=0;g<6;g++){
  auto &G=groups[g];G.oldShift=int32_t(rg_u32(in));G.count=rg_u32(in);G.words=rg_u32(in);
  int oldLayers=rg_u32(in),oldOffset=rg_u32(in),oldComponent=rg_u32(in);
  if(G.count!=expectedCounts[g]||G.words!=(G.count+31)/32||G.oldShift!=(g?originalDegrees[g]-oldT:0)||oldLayers!=oldD-G.oldShift+1||oldOffset!=oldWords||oldComponent!=ncomponents)throw std::runtime_error("old graph six-group dictionary");
  oldWords+=oldLayers*G.words;G.shift=g?originalDegrees[g]-T:0;G.layers=D-G.shift+1;G.wordOffset=nw;G.componentOffset=ncomponents;nw+=G.layers*G.words;ncomponents+=G.count;
  if(g)for(int c=0;c<G.count;c++){
   int index=rg_u32(in)-1,raw=rg_u32(in);
   if(index<0||index>=ns||sources[index].group>=0||raw<1||raw>6188)throw std::runtime_error("old graph source dictionary");
   sources[index]={raw,originalDegrees[g],g,c};G.originalSources.push_back(index);
  }
 }
 if(oldWords!=6423||nw!=4842||ncomponents!=3229)throw std::runtime_error("exact T96 storage profile");
 for(const auto &s:sources)if(s.group<1)throw std::runtime_error("incomplete original-source dictionary");
 BitOps ops;std::vector<RGPivot> piv(ncomponents);int processed=0,stored=0,outputPivots=0,sourcePivots=0,previousInputComponent=-1,inputNonzeroSourceOutputs=0;
 uint64_t reductions=0,swaps=0,wordCalls=0;
 auto lead=[&](const Row &row,int upper,bool oldOrder)->RGLead{
  int lower=oldOrder?-49:minDegree;
  for(int d=upper;d>=lower;d--)for(const auto &G:groups){
   int layer=d-(oldOrder?G.oldShift:G.shift);if(layer<0||layer>=G.layers)continue;int base=G.wordOffset+layer*G.words;
   for(int w=0;w<G.words;w++){uint32_t nonzero=0;for(int b=0;b<5;b++)nonzero|=row[b*nw+base+w];if(nonzero){
    int c=32*w+__builtin_ctz(nonzero);if(c>=G.count)throw std::runtime_error("nonzero group padding");
    return {d,G.componentOffset+c,BitOps::get(row,nw,32*base+c)};
   }}
  }return {};
 };
 const uint64_t rowBytes=uint64_t(5)*nw*4;
 std::cout<<"{\"phase\":\"reweighted-graph-ready\",\"oldShift\":64,\"newShift\":96,\"maximumWeightedDegree\":8,\"wordsPerPlane\":"<<nw<<",\"fullSingleCopyBasisBytes\":"<<rowBytes*ns<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 for(int index=0;index<ns;index++){
  int oldComponent=rg_u16(in)-1,oldDegree=int32_t(rg_u32(in)),oldCoefficient=in.get();
  if(oldComponent<=previousInputComponent||oldComponent>=ncomponents||oldDegree<-49||oldDegree>D||oldCoefficient<1||oldCoefficient>30)throw std::runtime_error("old graph pivot header or degree bound");previousInputComponent=oldComponent;
  Row current(5*nw);
  for(const auto &G:groups){
   int layers=rg_u16(in),expected=std::max(0,oldDegree-G.oldShift+1);
   if(layers!=expected||layers>G.layers)throw std::runtime_error("old serialized row layer count");
   for(int b=0;b<5;b++){in.read(reinterpret_cast<char*>(current.data()+b*nw+G.wordOffset),size_t(layers)*G.words*4);if(!in)throw std::runtime_error("truncated old graph row");}
  }
  auto original=lead(current,D,true);
  if(original.component!=oldComponent||original.degree!=oldDegree||original.coefficient!=oldCoefficient)throw std::runtime_error("old graph leading identity");
  if(oldComponent>=qout){bool nonzero=false;for(int b=0;b<5;b++)for(int w=0;w<groups[0].layers*groups[0].words;w++)nonzero|=current[b*nw+w]!=0;if(nonzero)inputNonzeroSourceOutputs++;}
  RGLead L=lead(current,D,false);if(L.component<0)throw std::runtime_error("zero old graph basis vector");
  while(L.component>=0){
   auto &P=piv[L.component];
   if(!P.row){P.row=std::make_unique<Row>(std::move(current));P.degree=L.degree;P.coefficient=L.coefficient;stored++;if(L.component<qout)outputPivots++;else sourcePivots++;break;}
   if(P.degree>L.degree){std::swap(current,*P.row);std::swap(L.degree,P.degree);std::swap(L.coefficient,P.coefficient);swaps++;}
   int shift=L.degree-P.degree,a=L.coefficient*ops.inv[P.coefficient]%31;if(shift<0||!a)throw std::runtime_error("reweighted Euclidean reduction");
   auto rep=ops.rep[31-a];
   for(const auto &G:groups){
    int layers=P.degree-G.shift+1;if(layers<=0)continue;if(layers>G.layers||shift+layers>G.layers)throw std::runtime_error("T96 weighted-degree capacity exceeded");
    int words=layers*G.words,destination=G.wordOffset+shift*G.words;
    BitOps::add(current,nw,destination,*P.row,nw,G.wordOffset,words,rep.rot,rep.neg);wordCalls+=words;
    if(rep.c){BitOps::add(current,nw,destination,*P.row,nw,G.wordOffset,words,(rep.rot+(rep.c==1?1:2))%5,rep.neg);wordCalls+=words;}
   }
   reductions++;auto next=lead(current,L.degree,false);
   if(next.component<0)throw std::runtime_error("independent old graph row reduced to zero");
   if(next.degree>L.degree||(next.degree==L.degree&&next.component<=L.component))throw std::runtime_error("reweighted leading monomial did not decrease");L=next;
  }
  processed++;if(stored!=processed)throw std::runtime_error("graph rank is not processed count");
  if(processed==1||processed%25==0||processed==ns){struct rusage usage{};getrusage(RUSAGE_SELF,&usage);
   std::cout<<"{\"phase\":\"reweighted-graph-prefix\",\"processedSources\":"<<processed<<",\"storedRows\":"<<stored<<",\"outputLeadingRows\":"<<outputPivots<<",\"sourceLeadingRows\":"<<sourcePivots<<",\"reductions\":"<<reductions<<",\"swaps\":"<<swaps<<",\"additionWordCalls\":"<<wordCalls<<",\"peakRSSKiB\":"<<usage.ru_maxrss<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
  }
  if(elapsed()>=soft)break;
 }
 bool allSources=processed==ns;if(allSources&&in.get()!=EOF)throw std::runtime_error("trailing old graph data");
 int nonzeroSourceOutputs=0,maxSourceOutputDegree=-1,maxOutputDegree=-1,maxSourceCoefficientDegree=-1,outputDegreeSum=0;
 std::vector<int> histogram(D-minDegree+1),outputHistogram(D+1);std::vector<std::pair<int,int>> outputProfile;
 std::string prefix=argv[2];std::ofstream out(prefix+"-basis.bin",std::ios::binary),meta(prefix+"-metadata.json");if(!out||!meta)throw std::runtime_error("reweighted output open");
 out.write("R150GG31",8);for(int value:{ns,qout,ns,T,D,processed,stored,6,int(allSources)})u32(out,value);
 for(const auto &G:groups){for(int value:{G.shift,G.count,G.words,G.layers,G.wordOffset,G.componentOffset})u32(out,uint32_t(value));for(int index:G.originalSources){u32(out,index+1);u32(out,sources[index].raw);}}
 for(int c=0;c<ncomponents;c++)if(piv[c].row){
  const auto &P=piv[c];const Row &row=*P.row;auto L=lead(row,D,false);
  if(L.component!=c||L.degree!=P.degree||L.coefficient!=P.coefficient)throw std::runtime_error("final T96 pivot identity");
  histogram[P.degree-minDegree]++;int outputDegree=-1;
  for(int d=D;d>=0&&outputDegree<0;d--)for(int w=0;w<groups[0].words;w++){uint32_t v=0;for(int b=0;b<5;b++)v|=row[b*nw+d*groups[0].words+w];if(v){outputDegree=d;break;}}
  if(c<qout){if(outputDegree!=P.degree||P.degree<0)throw std::runtime_error("output-leading degree mismatch");outputDegreeSum+=P.degree;maxOutputDegree=std::max(maxOutputDegree,P.degree);outputHistogram[P.degree]++;outputProfile.push_back({c+1,P.degree});}
  else if(outputDegree>=0){nonzeroSourceOutputs++;maxSourceOutputDegree=std::max(maxSourceOutputDegree,outputDegree);}
  for(int g=1;g<6;g++){const auto &G=groups[g];for(int d=G.layers-1;d>=0;d--){bool any=false;for(int b=0;b<5;b++)for(int w=0;w<G.words;w++)any|=row[b*nw+G.wordOffset+d*G.words+w]!=0;if(any){maxSourceCoefficientDegree=std::max(maxSourceCoefficientDegree,d);break;}}}
  u16(out,c+1);u32(out,uint32_t(P.degree));out.put(char(P.coefficient));
  for(const auto &G:groups){int layers=std::max(0,P.degree-G.shift+1);u16(out,layers);for(int b=0;b<5;b++)for(int word=0;word<layers*G.words;word++)u32(out,row[b*nw+G.wordOffset+word]);}
 }
 bool projection=allSources&&outputPivots==1021&&sourcePivots==1174&&outputDegreeSum==716;
 std::string status=allSources?(projection?"complete-reweighted-graph-projection-basis":"complete-reweighted-graph-projection-not-certified"):"reweighted-graph-prefix-only";
 meta<<"{\"format\":\"r150-reweighted-complete-graph-v1\",\"field\":31,\"status\":\""<<status<<"\",\"sourceShiftRule\":\"degree(R_j)-96\",\"maximumWeightedRowDegree\":8,\"processedSources\":"<<processed<<",\"storedRows\":"<<stored<<",\"outputLeadingRows\":"<<outputPivots<<",\"sourceLeadingRows\":"<<sourcePivots<<",\"inputSourceLeadingRowsWithNonzeroOutput\":"<<inputNonzeroSourceOutputs<<",\"sourceLeadingRowsWithNonzeroOutput\":"<<nonzeroSourceOutputs<<",\"maximumSourceLeadingOutputDegree\":"<<maxSourceOutputDegree<<",\"maximumOutputLeadingDegree\":"<<maxOutputDegree<<",\"maximumSourceCoefficientDegree\":"<<maxSourceCoefficientDegree<<",\"outputDegreeSum\":"<<outputDegreeSum<<",\"referenceOutputDegreeSum\":716,\"projectionSpanCertified\":"<<(projection?"true":"false")<<",\"wordsPerPlane\":"<<nw<<",\"rowBytes\":"<<rowBytes<<",\"completeSourceDictionary\":[";
 for(int i=0;i<ns;i++){if(i)meta<<",";const auto &S=sources[i];meta<<"["<<i+1<<","<<S.raw<<","<<S.degree<<","<<S.group<<","<<S.local<<"]";}meta<<"],\"outputLeadingProfile\":[";
 for(size_t i=0;i<outputProfile.size();i++){if(i)meta<<",";meta<<"["<<outputProfile[i].first<<","<<outputProfile[i].second<<"]";}meta<<"],\"outputDegreeHistogram\":[";
 for(size_t i=0;i<outputHistogram.size();i++){if(i)meta<<",";meta<<outputHistogram[i];}meta<<"],\"degreeHistogram\":[";
 for(size_t i=0;i<histogram.size();i++){if(i)meta<<",";meta<<histogram[i];}
 meta<<"],\"sourceIdentity\":\"Every input is one actual vector of the complete T64 original graph basis. All 2195 vectors, including all pure-source vectors, are processed. Constant multiples of s powers and swaps act on every group. A certified projection uses inclusion in the original image, 1021 distinct output leading components, and equality of the degree sum 716 with the prior complete original GB. Source-leading vectors with nonzero output are reported and never called kernel vectors.\",\"elapsedSeconds\":"<<elapsed()<<"}\n";
 out.close();meta.close();if(!out||!meta)throw std::runtime_error("reweighted output failure");struct rusage usage{};getrusage(RUSAGE_SELF,&usage);
 std::cout<<"{\"status\":\""<<status<<"\",\"processedSources\":"<<processed<<",\"outputLeadingRows\":"<<outputPivots<<",\"sourceLeadingRows\":"<<sourcePivots<<",\"sourceLeadingRowsWithNonzeroOutput\":"<<nonzeroSourceOutputs<<",\"maximumOutputLeadingDegree\":"<<maxOutputDegree<<",\"maximumSourceCoefficientDegree\":"<<maxSourceCoefficientDegree<<",\"outputDegreeSum\":"<<outputDegreeSum<<",\"projectionSpanCertified\":"<<(projection?"true":"false")<<",\"reductions\":"<<reductions<<",\"swaps\":"<<swaps<<",\"additionWordCalls\":"<<wordCalls<<",\"peakRSSKiB\":"<<usage.ru_maxrss<<",\"elapsedSeconds\":"<<elapsed()<<"}\n";
 return 0;
}catch(const std::exception &e){std::cerr<<"REWEIGHTED_GRAPH_FAILED "<<e.what()<<"\n";return 1;}}
