// Shifted weak-Popov basis of the exact graph columns (R_j,e_j).
// Six blocks: output shift 0; source shift deg(R_j)-64, grouped by degree.
// One bit-plane copy per row. Scalars 3 and 5 use two additions, not caches.
#include "2026-11-14-r150-f31-bitplane-789f.hpp"
#include <sys/resource.h>

static uint32_t sg_u32(std::istream &in){uint32_t a=0;for(int k=0;k<4;k++){int c=in.get();if(c<0)throw std::runtime_error("truncated u32");a|=uint32_t(c)<<(8*k);}return a;}
static uint16_t sg_u16(std::istream &in){int a=in.get(),b=in.get();if(a<0||b<0)throw std::runtime_error("truncated u16");return a|(b<<8);}
struct SGSource {uint64_t offset=0;int raw=0,degree=0,group=0,local=0;};
struct SGGroup {int degree=0,shift=0,count=0,words=0,layers=0,wordOffset=0,componentOffset=0;std::vector<int> originalSources;};
struct SGLead {int degree=-1000,component=-1,coefficient=0;};
struct SGPivot {std::unique_ptr<Row> row;int degree=-1000,coefficient=0;};

int main(int argc,char **argv){try{
 if(argc!=4)return 2;const double soft=std::stod(argv[3]);if(soft<=0)throw std::runtime_error("positive explicit soft bound required");
 auto start=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 const int ns=2195,nt=9,qout=1034,T=64,D=45,minDegree=-49;
 std::ifstream in(argv[1],std::ios::binary);char magic[8];in.read(magic,8);if(std::string(magic,8)!="R150NF31"||sg_u32(in)!=ns||sg_u32(in)!=nt||sg_u32(in)!=qout)throw std::runtime_error("full original normal-form input required");
 std::vector<SGSource> sources(ns);std::vector<SGGroup> groups(6);groups[0].count=qout;
 const std::array<int,5> sourceDegrees{15,25,35,40,45};for(int g=1;g<6;g++){groups[g].degree=sourceDegrees[g-1];groups[g].shift=sourceDegrees[g-1]-T;}
 for(int index=0;index<ns+nt;index++){
  uint64_t offset=in.tellg();int raw=sg_u32(in),target=sg_u16(in),count=sg_u32(in),previous=0,degree=-1;
  if(count<0||count>qout)throw std::runtime_error("component count");
  for(int k=0;k<count;k++){int c=sg_u16(in),len=in.get(),last=-1;if(c<=previous||c>qout||len<1||len>D+1)throw std::runtime_error("component or polynomial degree");previous=c;degree=std::max(degree,len-1);for(int a=0;a<len;a++){last=in.get();if(last<0||last>30)throw std::runtime_error("field coefficient");}if(!last)throw std::runtime_error("trailing zero polynomial coefficient");}
  if(index<ns){if(raw<1||raw>6188||target)throw std::runtime_error("original source identity");int g=0;for(int j=1;j<6;j++)if(groups[j].degree==degree)g=j;if(!g)throw std::runtime_error("unexpected actual source degree");auto &G=groups[g];sources[index]={offset,raw,degree,g,int(G.originalSources.size())};G.originalSources.push_back(index);G.count++;}
  else if(raw||target!=index-ns+2)throw std::runtime_error("original target identity");
 }
 if(in.get()!=EOF)throw std::runtime_error("trailing NF binary");
 const std::array<int,6> expectedCounts{1034,6,66,396,11,1716};int nw=0,ncomponents=0;
 for(int g=0;g<6;g++){auto &G=groups[g];if(G.count!=expectedCounts[g])throw std::runtime_error("actual source-degree group changed");G.words=(G.count+31)/32;G.layers=D-G.shift+1;G.wordOffset=nw;G.componentOffset=ncomponents;nw+=G.words*G.layers;ncomponents+=G.count;}
 if(nw!=6423||ncomponents!=3229)throw std::runtime_error("six-block storage identity");
 const uint64_t rowBytes=uint64_t(5)*nw*4;
 BitOps ops;std::vector<SGPivot> piv(ncomponents);int processed=0,stored=0,outputPivots=0,sourcePivots=0;uint64_t reductions=0,swaps=0,additionWordCalls=0;
 auto lead=[&](const Row &row,int upper)->SGLead{
  for(int d=upper;d>=minDegree;d--)for(const auto &G:groups){int layer=d-G.shift;if(layer<0||layer>=G.layers)continue;int base=G.wordOffset+layer*G.words;
   for(int w=0;w<G.words;w++){int off=base+w;uint32_t nonzero=row[off]|row[nw+off]|row[2*nw+off]|row[3*nw+off]|row[4*nw+off];if(nonzero){int c=32*w+__builtin_ctz(nonzero);if(c>=G.count)throw std::runtime_error("nonzero group padding");return {d,G.componentOffset+c,BitOps::get(row,nw,32*base+c)};}}
  }return {};
 };
 auto readSource=[&](int index){const auto &S=sources[index];in.clear();in.seekg(S.offset);int raw=sg_u32(in),target=sg_u16(in),count=sg_u32(in);if(raw!=S.raw||target)throw std::runtime_error("source reread identity");Row row(5*nw);for(int k=0;k<count;k++){int c=sg_u16(in)-1,len=in.get();for(int d=0;d<len;d++){int a=in.get();BitOps::set(row,nw,d*groups[0].words*32+c,a);}}
  const auto &G=groups[S.group];BitOps::set(row,nw,32*G.wordOffset+S.local,1);return row;
 };
 std::cout<<"{\"phase\":\"six-shift-input-ready\",\"sources\":2195,\"components\":3229,\"wordsPerPlane\":"<<nw<<",\"bytesPerStoredRow\":"<<rowBytes<<",\"fullSingleCopyBasisBytes\":"<<rowBytes*ns<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 for(int index=0;index<ns;index++){
  Row current=readSource(index);SGLead L=lead(current,D);if(L.degree!=sources[index].degree||L.component<0||L.component>=qout)throw std::runtime_error("graph input leading identity");
  while(L.component>=0){auto &P=piv[L.component];
   if(!P.row){P.row=std::make_unique<Row>(std::move(current));P.degree=L.degree;P.coefficient=L.coefficient;stored++;if(L.component<qout)outputPivots++;else sourcePivots++;break;}
   if(P.degree>L.degree){std::swap(current,*P.row);std::swap(L.degree,P.degree);std::swap(L.coefficient,P.coefficient);swaps++;}
   int shift=L.degree-P.degree,a=L.coefficient*ops.inv[P.coefficient]%31;if(shift<0||!a)throw std::runtime_error("weighted Euclidean reduction");auto rep=ops.rep[31-a];
   for(const auto &G:groups){int layers=P.degree-G.shift+1;if(layers<=0)continue;if(layers>G.layers||shift+layers>G.layers)throw std::runtime_error("weighted source-degree overflow");int words=layers*G.words,destination=G.wordOffset+shift*G.words;
    BitOps::add(current,nw,destination,*P.row,nw,G.wordOffset,words,rep.rot,rep.neg);additionWordCalls+=words;
    if(rep.c){int secondRotation=(rep.rot+(rep.c==1?1:2))%5;BitOps::add(current,nw,destination,*P.row,nw,G.wordOffset,words,secondRotation,rep.neg);additionWordCalls+=words;}
   }
   reductions++;SGLead next=lead(current,L.degree);if(next.component<0)throw std::runtime_error("independent graph source reduced to zero");if(next.degree>L.degree||(next.degree==L.degree&&next.component<=L.component))throw std::runtime_error("shifted leading monomial did not decrease");L=next;
  }
  processed++;if(stored!=processed)throw std::runtime_error("graph rank is not source count");
  if(processed==1||processed%25==0||processed==ns){struct rusage usage{};getrusage(RUSAGE_SELF,&usage);std::cout<<"{\"phase\":\"shifted-graph-prefix\",\"processedSources\":"<<processed<<",\"storedRows\":"<<stored<<",\"outputLeadingRows\":"<<outputPivots<<",\"sourceLeadingRows\":"<<sourcePivots<<",\"reductions\":"<<reductions<<",\"swaps\":"<<swaps<<",\"additionWordCalls\":"<<additionWordCalls<<",\"basisPayloadBytes\":"<<rowBytes*stored<<",\"peakRSSKiB\":"<<usage.ru_maxrss<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;}
  if(elapsed()>=soft)break;
 }
 bool allSources=processed==ns;int nonzeroSourceOutputs=0,maxSourceOutputDegree=-1,maxOutputLeadingDegree=-1,maxSourceCoefficientDegree=-1;std::vector<int> histogram(D-minDegree+1);
 std::string prefix=argv[2];std::ofstream out(prefix+"-basis.bin",std::ios::binary),meta(prefix+"-metadata.json");if(!out||!meta)throw std::runtime_error("graph output open");
 out.write("R150GG31",8);for(int value:{ns,qout,ns,T,D,processed,stored,6,int(allSources)})u32(out,value);
 for(int g=0;g<6;g++){const auto &G=groups[g];for(int value:{G.shift,G.count,G.words,G.layers,G.wordOffset,G.componentOffset})u32(out,uint32_t(value));if(g)for(int index:G.originalSources){u32(out,index+1);u32(out,sources[index].raw);}}
 for(int c=0;c<ncomponents;c++)if(piv[c].row){const auto &P=piv[c];const Row &row=*P.row;auto L=lead(row,D);if(L.component!=c||L.degree!=P.degree||L.coefficient!=P.coefficient)throw std::runtime_error("final shifted pivot identity");histogram[P.degree-minDegree]++;
  bool outputNonzero=false;int outputDegree=-1;for(int d=D;d>=0;d--){int base=d*groups[0].words;for(int w=0;w<groups[0].words;w++){uint32_t v=0;for(int plane=0;plane<5;plane++)v|=row[plane*nw+base+w];if(v){outputNonzero=true;outputDegree=d;break;}}if(outputNonzero)break;}
  if(c>=qout&&outputNonzero){nonzeroSourceOutputs++;maxSourceOutputDegree=std::max(maxSourceOutputDegree,outputDegree);}if(c<qout)maxOutputLeadingDegree=std::max(maxOutputLeadingDegree,P.degree);
  for(int g=1;g<6;g++){const auto &G=groups[g];for(int d=G.layers-1;d>=0;d--){int base=G.wordOffset+d*G.words;bool any=false;for(int w=0;w<G.words;w++){uint32_t v=0;for(int plane=0;plane<5;plane++)v|=row[plane*nw+base+w];if(v){any=true;break;}}if(any){maxSourceCoefficientDegree=std::max(maxSourceCoefficientDegree,d);break;}}}
  u16(out,c+1);u32(out,uint32_t(P.degree));out.put(char(P.coefficient));
  for(const auto &G:groups){int layers=std::max(0,P.degree-G.shift+1);u16(out,layers);for(int plane=0;plane<5;plane++)for(int word=0;word<layers*G.words;word++)u32(out,row[plane*nw+G.wordOffset+word]);}
 }
 bool elimination=allSources&&outputPivots==1021&&sourcePivots==1174&&nonzeroSourceOutputs==0;
 std::string status=allSources?(elimination?"complete-graph-elimination-basis":"complete-graph-basis-elimination-condition-failed"):"shifted-graph-prefix-only";
 meta<<"{\"format\":\"r150-shifted-source-graph-v1\",\"field\":31,\"status\":\""<<status<<"\",\"sourceShiftRule\":\"degree(R_j)-64\",\"outputShift\":0,\"completeSourceDictionary\":[";for(int i=0;i<ns;i++){if(i)meta<<",";const auto &S=sources[i];meta<<"["<<i+1<<","<<S.raw<<","<<S.degree<<","<<S.group<<","<<S.local<<"]";}meta<<"],\"processedSources\":"<<processed<<",\"storedRows\":"<<stored<<",\"outputLeadingRows\":"<<outputPivots<<",\"sourceLeadingRows\":"<<sourcePivots<<",\"sourceLeadingRowsWithNonzeroOutput\":"<<nonzeroSourceOutputs<<",\"maximumSourceLeadingOutputDegree\":"<<maxSourceOutputDegree<<",\"maximumOutputLeadingDegree\":"<<maxOutputLeadingDegree<<",\"maximumSourceCoefficientDegree\":"<<maxSourceCoefficientDegree<<",\"wordsPerPlane\":"<<nw<<",\"rowBytes\":"<<rowBytes<<",\"reductions\":"<<reductions<<",\"swaps\":"<<swaps<<",\"additionWordCalls\":"<<additionWordCalls<<",\"degreeHistogram\":[";for(size_t i=0;i<histogram.size();i++){if(i)meta<<",";meta<<histogram[i];}meta<<"],\"sourceIdentity\":\"Every input is the actual original normal-form column R_j together with its correctly mapped source unit e_j. Every operation is a constant-field multiple of s^k subtraction or a swap, applied to all six groups. Prefix rows span only the processed graph inputs. A full original-source output basis requires all 2195 inputs, 1021 output-leading rows, and all 1174 source-leading rows with exactly zero output.\"}\n";
 out.close();meta.close();if(!out||!meta)throw std::runtime_error("graph output failed");struct rusage usage{};getrusage(RUSAGE_SELF,&usage);
 std::cout<<"{\"status\":\""<<status<<"\",\"processedSources\":"<<processed<<",\"outputLeadingRows\":"<<outputPivots<<",\"sourceLeadingRows\":"<<sourcePivots<<",\"sourceLeadingRowsWithNonzeroOutput\":"<<nonzeroSourceOutputs<<",\"maximumOutputLeadingDegree\":"<<maxOutputLeadingDegree<<",\"maximumSourceCoefficientDegree\":"<<maxSourceCoefficientDegree<<",\"reductions\":"<<reductions<<",\"swaps\":"<<swaps<<",\"additionWordCalls\":"<<additionWordCalls<<",\"basisPayloadBytes\":"<<rowBytes*stored<<",\"peakRSSKiB\":"<<usage.ru_maxrss<<",\"elapsedSeconds\":"<<elapsed()<<"}\n";
 return 0;
}catch(const std::exception &e){std::cerr<<"SHIFTED_GRAPH_MODULE_FAILED "<<e.what()<<"\n";return 1;}}
