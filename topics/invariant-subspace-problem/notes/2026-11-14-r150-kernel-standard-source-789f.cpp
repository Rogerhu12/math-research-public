// Canonical weighted source representatives using the ACTUAL full T96 kernel.
// This is a new F31 representation step, not a characteristic-zero lift.
#include "2026-11-14-r150-f31-bitplane-789f.hpp"
#include <sys/resource.h>
static uint32_t ks_u32(std::istream &in){uint32_t a=0;for(int k=0;k<4;k++){int c=in.get();if(c<0)throw std::runtime_error("truncated u32");a|=uint32_t(c)<<(8*k);}return a;}
static uint16_t ks_u16(std::istream &in){int a=in.get(),b=in.get();if(a<0||b<0)throw std::runtime_error("truncated u16");return a|(b<<8);}
struct KSGroup {int shift=0,delta=0,count=0,words=0,layers=0,componentOffset=0,accOffset=0;};
struct KSSource {int group=-1,local=-1,raw=0,delta=0,coordinate=-1;};
struct KSKernel {Row row;int cost=0,coefficient=0,stride=0;std::array<int,6> offset{},layers{};};

int main(int argc,char **argv){try{
 if(argc!=5)return 2;constexpr int ns=2195,nt=9,q=1034,T=96,D=8,B=146,hd=24;
 uint32_t endian=1;if(*reinterpret_cast<uint8_t*>(&endian)!=1)throw std::runtime_error("little endian required");
 auto start=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 BitOps ops;std::ifstream graph(argv[1],std::ios::binary),coeff(argv[2],std::ios::binary),input(argv[3],std::ios::binary);if(!graph||!coeff||!input)throw std::runtime_error("input open");
 char magic[8];graph.read(magic,8);if(std::string(magic,8)!="R150GG31")throw std::runtime_error("graph magic");
 std::vector<int> dims;for(int i=0;i<9;i++)dims.push_back(ks_u32(graph));if(dims!=std::vector<int>{2195,1034,2195,96,8,2195,2195,6,1})throw std::runtime_error("complete T96 graph required");
 std::vector<KSGroup> groups(6);std::vector<KSSource> sources(ns);std::array<int,6> counts{1034,6,66,396,11,1716},deltas{0,15,25,35,40,45};int accWords=0,componentCount=0,graphWords=0;
 for(int g=0;g<6;g++){
  auto &G=groups[g];G.shift=int32_t(ks_u32(graph));G.count=ks_u32(graph);G.words=ks_u32(graph);G.layers=ks_u32(graph);int wordOffset=ks_u32(graph);G.componentOffset=ks_u32(graph);G.delta=deltas[g];
  if(G.shift!=(g?G.delta-T:0)||G.count!=counts[g]||G.words!=(G.count+31)/32||G.layers!=D-G.shift+1||wordOffset!=graphWords||G.componentOffset!=componentCount)throw std::runtime_error("source-group dictionary");
  graphWords+=G.layers*G.words;componentCount+=G.count;
  if(g){G.accOffset=accWords;accWords+=(B-G.delta+1)*G.words;for(int c=0;c<G.count;c++){int i=ks_u32(graph)-1,raw=ks_u32(graph);if(i<0||i>=ns||sources[i].group>=0||raw<1||raw>6188)throw std::runtime_error("source identity");sources[i]={g,c,raw,G.delta,G.componentOffset-q+c};}}
 }
 if(accWords!=7569||graphWords!=4842||componentCount!=3229)throw std::runtime_error("fixed complete group dimensions");for(const auto &s:sources)if(s.group<1)throw std::runtime_error("incomplete source identities");
 std::vector<std::unique_ptr<KSKernel>> kernel(ns);std::vector<bool> seen(3229);std::array<int,105> kernelCostHistogram{};int outputRows=0,kernelRows=0,outputDegreeSum=0,kernelCostSum=0;
 for(int row=0;row<ns;row++){
  int component=ks_u16(graph)-1,d=int32_t(ks_u32(graph)),lc=graph.get();if(component<0||component>=3229||seen[component]||d<-81||d>D||lc<1||lc>30)throw std::runtime_error("graph row header");seen[component]=true;bool isKernel=component>=q;
  std::unique_ptr<KSKernel> K;if(isKernel){K=std::make_unique<KSKernel>();K->cost=d+T;K->coefficient=lc;if(K->cost<15||K->cost>104)throw std::runtime_error("kernel weighted cost");for(int g=1;g<6;g++){K->offset[g]=K->stride;K->layers[g]=std::max(0,K->cost-groups[g].delta+1);K->stride+=K->layers[g]*groups[g].words;}K->row.resize(5*K->stride);}
  for(int g=0;g<6;g++){
   const auto &G=groups[g];int layers=ks_u16(graph),expected=std::max(0,d-G.shift+1),words=layers*G.words;if(layers!=expected)throw std::runtime_error("graph row layer count");
   if(isKernel&&g==0){Row output(5*words);graph.read(reinterpret_cast<char*>(output.data()),size_t(output.size())*4);for(auto w:output)if(w)throw std::runtime_error("source-leading row is not an actual zero-output kernel row");}
   else if(isKernel){for(int b=0;b<5;b++)graph.read(reinterpret_cast<char*>(K->row.data()+b*K->stride+K->offset[g]),size_t(words)*4);}
   else graph.seekg(size_t(5)*words*4,std::ios::cur);
   if(!graph)throw std::runtime_error("truncated complete graph");
  }
  if(isKernel){
   int actualCost=-1,actualCoordinate=-1;
   for(int cost=K->cost;cost>=15&&actualCoordinate<0;cost--)for(int g=1;g<6&&actualCoordinate<0;g++){const auto &G=groups[g];int layer=cost-G.delta;if(layer<0||layer>=K->layers[g])continue;
    for(int w=0;w<G.words;w++){uint32_t nz=0;for(int b=0;b<5;b++)nz|=K->row[b*K->stride+K->offset[g]+layer*G.words+w];if(nz){int c=32*w+__builtin_ctz(nz);if(c>=G.count)throw std::runtime_error("kernel padding");actualCost=cost;actualCoordinate=G.componentOffset-q+c;if(BitOps::get(K->row,K->stride,32*(K->offset[g]+layer*G.words)+c)!=lc)throw std::runtime_error("kernel leading coefficient");break;}}
   }
   if(actualCost!=K->cost||actualCoordinate!=component-q)throw std::runtime_error("kernel leading identity");
   kernelCostSum+=K->cost;kernelCostHistogram[K->cost]++;kernel[component-q]=std::move(K);kernelRows++;
  }else{if(d<0)throw std::runtime_error("negative output degree");outputRows++;outputDegreeSum+=d;}
 }
 if(graph.get()!=EOF||outputRows!=1021||kernelRows!=1174||outputDegreeSum!=716||kernelCostSum!=60050)throw std::runtime_error("actual complete original graph profile");
 coeff.read(magic,8);if(std::string(magic,8)!="R150TC31"||ks_u32(coeff)!=ns||ks_u32(coeff)!=nt||ks_u32(coeff)!=hd)throw std::runtime_error("complete original source coefficient input");
 std::vector<int> h(hd+1);for(auto &a:h){a=coeff.get();if(a<0||a>30)throw std::runtime_error("h31 coefficient");}if(h.back()!=1)throw std::runtime_error("h31 not monic");std::vector<Row> canonical(nt,Row(5*accWords));
 for(int i=0;i<ns;i++){int number=ks_u32(coeff),raw=ks_u32(coeff),delta=ks_u16(coeff);const auto &S=sources[i];const auto &G=groups[S.group];if(number!=i+1||raw!=S.raw||delta!=S.delta)throw std::runtime_error("coefficient original source mapping");
  for(int j=0;j<nt;j++){int len=ks_u16(coeff);if(len>B-delta+1)throw std::runtime_error("input source cost bound");int last=0;for(int k=0;k<len;k++){last=coeff.get();if(last<0||last>30)throw std::runtime_error("coefficient field");BitOps::set(canonical[j],accWords,32*(G.accOffset+k*G.words)+S.local,last);}if(len&&!last)throw std::runtime_error("noncanonical polynomial tail");}
 }
 if(coeff.get()!=EOF)throw std::runtime_error("trailing source coefficients");
 uint64_t reductions=0,wordCalls=0;
 for(int j=0;j<nt;j++){
  for(int cost=B;cost>=15;cost--)for(int g=1;g<6;g++){
   const auto &G=groups[g];int layer=cost-G.delta;if(layer<0)continue;
   for(int c=0;c<G.count;c++){int coordinate=G.componentOffset-q+c;if(!kernel[coordinate]||kernel[coordinate]->cost>cost)continue;int a=BitOps::get(canonical[j],accWords,32*(G.accOffset+layer*G.words)+c);if(!a)continue;
    const auto &K=*kernel[coordinate];int shift=cost-K.cost,factor=a*ops.inv[K.coefficient]%31;auto rep=ops.rep[31-factor];
    for(int gg=1;gg<6;gg++){const auto &H=groups[gg];int words=K.layers[gg]*H.words;if(!words)continue;if(shift+K.layers[gg]>B-H.delta+1)throw std::runtime_error("kernel reduction increased source cost");
     int destination=H.accOffset+shift*H.words;BitOps::add(canonical[j],accWords,destination,K.row,K.stride,K.offset[gg],words,rep.rot,rep.neg);wordCalls+=words;
     if(rep.c){BitOps::add(canonical[j],accWords,destination,K.row,K.stride,K.offset[gg],words,(rep.rot+(rep.c==1?1:2))%5,rep.neg);wordCalls+=words;}
    }reductions++;
   }
  }
  std::cout<<"{\"phase\":\"canonical-kernel-source\",\"target\":"<<j+2<<",\"reductions\":"<<reductions<<",\"additionWordCalls\":"<<wordCalls<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 }
 const int productWords=q*(B+1);Row product(5*productWords);input.read(magic,8);if(std::string(magic,8)!="R150NF31"||ks_u32(input)!=ns||ks_u32(input)!=nt||ks_u32(input)!=q)throw std::runtime_error("original NF input");
 std::string prefix=argv[4];std::ofstream out(prefix+"-canonical-coefficients.bin",std::ios::binary),meta(prefix+"-canonical-coefficients.json");if(!out||!meta)throw std::runtime_error("canonical output open");out.write("R150TC31",8);u32(out,ns);u32(out,nt);u32(out,hd);for(int a:h)out.put(char(a));
 int maximumDegree=-1,nonzeroSources=0,standardColumns=0;uint64_t nonzeroCoefficients=0,products=0;std::array<int,nt> targetCosts;targetCosts.fill(-1);std::vector<std::array<int,6>> sourceStats;
 for(int i=0;i<ns;i++){
  const auto &S=sources[i];const auto &G=groups[S.group];int cutoff=kernel[S.coordinate]?kernel[S.coordinate]->cost-S.delta:-1;
  if(cutoff<0&&kernel[S.coordinate])throw std::runtime_error("negative kernel leading exponent");
  standardColumns+=cutoff<0?B-S.delta+1:std::min(cutoff,B-S.delta+1);
  std::vector<std::vector<uint8_t>> polys(nt);int degree=-1,nnz=0;for(int j=0;j<nt;j++){polys[j].resize(B-S.delta+1);for(int k=0;k<int(polys[j].size());k++){int a=BitOps::get(canonical[j],accWords,32*(G.accOffset+k*G.words)+S.local);if(a){if(cutoff>=0&&k>=cutoff)throw std::runtime_error("retained reducible kernel monomial");nnz++;targetCosts[j]=std::max(targetCosts[j],k+S.delta);}polys[j][k]=a;}while(!polys[j].empty()&&!polys[j].back())polys[j].pop_back();degree=std::max(degree,int(polys[j].size())-1);}
  maximumDegree=std::max(maximumDegree,degree);if(nnz)nonzeroSources++;nonzeroCoefficients+=nnz;sourceStats.push_back({i+1,S.raw,S.delta,cutoff,degree,nnz});
  u32(out,i+1);u32(out,S.raw);u16(out,S.delta);for(const auto &p:polys){u16(out,p.size());out.write(reinterpret_cast<const char*>(p.data()),p.size());}
  Triple packed;int stride=degree+1;packed[0].resize(5*stride);if(degree>=0){for(int j=0;j<nt;j++)for(int k=0;k<int(polys[j].size());k++)BitOps::set(packed[0],stride,k*32+j,polys[j][k]);BitOps::refresh(packed,stride,0);}
  int raw=ks_u32(input),target=ks_u16(input),entries=ks_u32(input),observedDegree=-1;if(raw!=S.raw||target)throw std::runtime_error("verification original NF source");
  for(int e=0;e<entries;e++){int c=ks_u16(input)-1,len=input.get();if(c<0||c>=q||len<1||len>46)throw std::runtime_error("verification NF term");observedDegree=std::max(observedDegree,len-1);for(int d=0;d<len;d++){int a=input.get();if(a<0||a>30)throw std::runtime_error("verification NF coefficient");if(a&&degree>=0){if(d+degree>B)throw std::runtime_error("canonical identity degree overflow");auto rep=ops.rep[a];BitOps::add(product,productWords,c*(B+1)+d,packed[rep.c],stride,0,stride,rep.rot,rep.neg);products++;}}}
  if(observedDegree!=S.delta)throw std::runtime_error("actual source degree changed");
  if((i+1)%500==0||i+1==ns)std::cout<<"{\"phase\":\"verify-canonical-original-source-identity\",\"sources\":"<<i+1<<",\"maximumCoefficientDegree\":"<<maximumDegree<<",\"nonzeroCoefficients\":"<<nonzeroCoefficients<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 }
 auto addAt=[&](int c,int d,int j,int a){int bit=(c*(B+1)+d)*32+j,v=(BitOps::get(product,productWords,bit)+a)%31;if(v<0)v+=31;uint32_t mask=uint32_t(1)<<j;for(int b=0;b<5;b++)product[b*productWords+bit/32]&=~mask;BitOps::set(product,productWords,bit,v);};
 for(int j=0;j<nt;j++){int raw=ks_u32(input),target=ks_u16(input),entries=ks_u32(input);if(raw||target!=j+2)throw std::runtime_error("original target mapping");for(int e=0;e<entries;e++){int c=ks_u16(input)-1,len=input.get();if(c<0||c>=q||len<1||len>27)throw std::runtime_error("original target NF term");for(int k=0;k<len;k++){int a=input.get();if(a<0||a>30)throw std::runtime_error("original target NF coefficient");for(int d=0;d<=hd;d++)if(a&&h[d])addAt(c,k+d,j,-a*h[d]);}}}
 if(input.get()!=EOF)throw std::runtime_error("trailing original NF matrix");for(auto w:product)if(w)throw std::runtime_error("complete canonical R*C=h31*T identity failed");
 if(standardColumns!=116877)throw std::runtime_error("fixed standard-source dimension");
 meta<<"{\"format\":\"r150-canonical-original-kernel-source-v1\",\"status\":\"completed\",\"field\":31,\"weightedSourceBudget\":146,\"standardSourceColumns\":116877,\"kernelRows\":1174,\"kernelWeightedDegreeSum\":60050,\"originalSourceDegreeSum\":93260,\"fullNormalFormSourceIdentity\":true,\"standardKernelNormalForm\":true,\"minimalWeightedSourceCost\":true,\"maximumCoefficientDegree\":"<<maximumDegree<<",\"nonzeroSources\":"<<nonzeroSources<<",\"nonzeroCoefficients\":"<<nonzeroCoefficients<<",\"targetCosts\":[";
 for(int j=0;j<nt;j++){if(j)meta<<",";meta<<targetCosts[j];}meta<<"],\"kernelCostHistogram\":[";for(int k=0;k<=104;k++){if(k)meta<<",";meta<<kernelCostHistogram[k];}
 meta<<"],\"sourceStats\":[";for(size_t i=0;i<sourceStats.size();i++){if(i)meta<<",";meta<<"[";for(int j=0;j<6;j++){if(j)meta<<",";meta<<sourceStats[i][j];}meta<<"]";}
 meta<<"],\"sourceIdentity\":\"Only the actual complete zero-output T96 kernel is used. Every subtraction preserves the same original R image and cannot increase cost deg(c_j)+delta_j. No reducible source monomial remains; the representative and its weighted cost minimum are unique. The full original NF identity is verified for all 2195 original sources and all nine targets. Characteristic-zero lifting is still open.\",\"elapsedSeconds\":"<<elapsed()<<"}\n";
 out.close();meta.close();if(!out||!meta)throw std::runtime_error("canonical output failed");struct rusage usage{};getrusage(RUSAGE_SELF,&usage);
 std::cout<<"{\"status\":\"canonical-original-source-complete\",\"field\":31,\"standardSourceColumns\":116877,\"maximumCoefficientDegree\":"<<maximumDegree<<",\"nonzeroSources\":"<<nonzeroSources<<",\"nonzeroCoefficients\":"<<nonzeroCoefficients<<",\"fullNormalFormSourceIdentity\":true,\"standardKernelNormalForm\":true,\"minimalWeightedSourceCost\":true,\"targetCosts\":[";
 for(int j=0;j<nt;j++){if(j)std::cout<<",";std::cout<<targetCosts[j];}std::cout<<"],\"reductions\":"<<reductions<<",\"additionWordCalls\":"<<wordCalls<<",\"peakRSSKiB\":"<<usage.ru_maxrss<<",\"elapsedSeconds\":"<<elapsed()<<"}\n";
 return 0;
}catch(const std::exception &e){std::cerr<<"KERNEL_STANDARD_SOURCE_FAILED "<<e.what()<<"\n";return 1;}}
