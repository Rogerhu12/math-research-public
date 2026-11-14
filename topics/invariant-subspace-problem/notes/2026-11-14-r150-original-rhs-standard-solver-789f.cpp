// Solve the actual original residual NF with the complete T96 image and kernel.
// Always preserves all nine RHS and verifies R*C + remainder = RHS in full.
// A nonzero remainder or minimal source cost >85 is a FIXED-SPACE obstruction.
#include "2026-11-14-r150-f31-bitplane-789f.hpp"
#include <sys/resource.h>
static uint32_t rs_u32(std::istream &in){uint32_t x=0;for(int j=0;j<4;j++){int a=in.get();if(a<0)throw std::runtime_error("truncated u32");x|=uint32_t(a)<<(8*j);}return x;}
static uint16_t rs_u16(std::istream &in){int a=in.get(),b=in.get();if(a<0||b<0)throw std::runtime_error("truncated u16");return a|(b<<8);}
static void rs_words(std::istream &in,uint32_t *p,size_t n){in.read(reinterpret_cast<char*>(p),n*4);if(!in)throw std::runtime_error("truncated bit planes");}
struct RSGroup {int shift=0,delta=0,count=0,words=0,layers=0,componentOffset=0,accOffset=0;};
struct RSSource {int group=-1,local=-1,raw=0,delta=0,coordinate=-1;};
struct RSRow {Row output,source;int degree=0,cost=0,lc=0,outWords=0,sourceWords=0;std::array<int,6> offsets{},layers{};};

int main(int argc,char **argv){try{
 if(argc!=5)return 2;constexpr int ns=2195,nt=9,q=1034,T=96,N=85,B=181,finalBudget=85,W=33,nwRHS=(N+1)*W;
 uint32_t endian=1;if(*reinterpret_cast<uint8_t*>(&endian)!=1)throw std::runtime_error("little endian required");
 auto start=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 std::ifstream graph(argv[1],std::ios::binary),rhs(argv[2],std::ios::binary),input(argv[3],std::ios::binary);if(!graph||!rhs||!input)throw std::runtime_error("input open");BitOps ops;char magic[8];
 graph.read(magic,8);if(std::string(magic,8)!="R150GG31")throw std::runtime_error("graph magic");std::vector<int> dims;for(int i=0;i<9;i++)dims.push_back(rs_u32(graph));if(dims!=std::vector<int>{2195,1034,2195,96,8,2195,2195,6,1})throw std::runtime_error("complete original T96 graph required");
 std::vector<RSGroup> groups(6);std::vector<RSSource> sources(ns);std::array<int,6> counts{1034,6,66,396,11,1716},deltas{0,15,25,35,40,45};int accWords=0,components=0,graphWords=0;
 for(int g=0;g<6;g++){
  auto &G=groups[g];G.shift=int32_t(rs_u32(graph));G.count=rs_u32(graph);G.words=rs_u32(graph);G.layers=rs_u32(graph);int offset=rs_u32(graph);G.componentOffset=rs_u32(graph);G.delta=deltas[g];
  if(G.shift!=(g?G.delta-T:0)||G.count!=counts[g]||G.words!=(G.count+31)/32||G.layers!=9-G.shift||offset!=graphWords||G.componentOffset!=components)throw std::runtime_error("exact original source-group dictionary");
  graphWords+=G.words*G.layers;components+=G.count;
  if(g){G.accOffset=accWords;accWords+=(B-G.delta+1)*G.words;for(int c=0;c<G.count;c++){int i=rs_u32(graph)-1,raw=rs_u32(graph);if(i<0||i>=ns||sources[i].group>=0||raw<1||raw>6188)throw std::runtime_error("source dictionary");sources[i]={g,c,raw,G.delta,G.componentOffset-q+c};}}
 }
 if(accWords!=10089||graphWords!=4842||components!=3229)throw std::runtime_error("complete graph storage profile");for(const auto &s:sources)if(s.group<1)throw std::runtime_error("incomplete original sources");
 std::vector<std::unique_ptr<RSRow>> image(q),kernel(ns);std::vector<bool> seen(3229);int outputRows=0,kernelRows=0,outputDegreeSum=0,kernelCostSum=0;
 for(int row=0;row<ns;row++){
  int component=rs_u16(graph)-1,d=int32_t(rs_u32(graph)),lc=graph.get();if(component<0||component>=3229||seen[component]||d<-81||d>8||lc<1||lc>30)throw std::runtime_error("original graph row header");seen[component]=true;bool isOutput=component<q;
  auto R=std::make_unique<RSRow>();R->degree=d;R->cost=d+T;R->lc=lc;if(isOutput){if(d<0)throw std::runtime_error("negative output leading degree");R->outWords=(d+1)*W;R->output.resize(5*R->outWords);}
  for(int g=1;g<6;g++){R->offsets[g]=R->sourceWords;R->layers[g]=std::max(0,d-groups[g].shift+1);R->sourceWords+=R->layers[g]*groups[g].words;}R->source.resize(5*R->sourceWords);
  for(int g=0;g<6;g++){
   const auto &G=groups[g];int layers=rs_u16(graph),words=layers*G.words;if(layers!=std::max(0,d-G.shift+1))throw std::runtime_error("original graph row layer count");
   if(g==0){if(isOutput)rs_words(graph,R->output.data(),R->output.size());else{Row out(5*words);rs_words(graph,out.data(),out.size());for(auto a:out)if(a)throw std::runtime_error("purported full kernel row has nonzero output");}}
   else for(int b=0;b<5;b++)rs_words(graph,R->source.data()+b*R->sourceWords+R->offsets[g],words);
  }
  if(isOutput){
   int ad=-1,ac=-1;for(int z=d;z>=0&&ac<0;z--)for(int w=0;w<W;w++){uint32_t nz=0;for(int b=0;b<5;b++)nz|=R->output[b*R->outWords+z*W+w];if(nz){ad=z;ac=32*w+__builtin_ctz(nz);break;}}
   if(ad!=d||ac!=component||BitOps::get(R->output,R->outWords,d*W*32+component)!=lc)throw std::runtime_error("image leading identity");
   int scale=ops.inv[lc];if(scale!=1){ops.multiple(R->output,R->outWords,0,scale);ops.multiple(R->source,R->sourceWords,0,scale);R->lc=1;}image[component]=std::move(R);outputRows++;outputDegreeSum+=d;
  }else{
   int ac=-1,ad=-1;for(int cost=R->cost;cost>=15&&ac<0;cost--)for(int g=1;g<6&&ac<0;g++){const auto &G=groups[g];int layer=cost-G.delta;if(layer<0||layer>=R->layers[g])continue;for(int w=0;w<G.words;w++){uint32_t nz=0;for(int b=0;b<5;b++)nz|=R->source[b*R->sourceWords+R->offsets[g]+layer*G.words+w];if(nz){int c=32*w+__builtin_ctz(nz);if(c>=G.count)throw std::runtime_error("kernel padding");ad=cost;ac=G.componentOffset-q+c;if(BitOps::get(R->source,R->sourceWords,32*(R->offsets[g]+layer*G.words)+c)!=lc)throw std::runtime_error("kernel leading coefficient");break;}}}
   if(ac!=component-q||ad!=R->cost)throw std::runtime_error("kernel leading identity");kernelCostSum+=R->cost;kernel[component-q]=std::move(R);kernelRows++;
  }
 }
 if(graph.get()!=EOF||outputRows!=1021||kernelRows!=1174||outputDegreeSum!=716||kernelCostSum!=60050)throw std::runtime_error("complete original image/kernel profile");
 rhs.read(magic,8);if(std::string(magic,8)!="R150NF31"||rs_u32(rhs)!=0||rs_u32(rhs)!=nt||rs_u32(rhs)!=q)throw std::runtime_error("original RHS NF header");
 std::vector<Row> target(nt,Row(5*nwRHS)),remainders;std::vector<Row> coefficients(nt,Row(5*accWords));
 for(int j=0;j<nt;j++){int raw=rs_u32(rhs),number=rs_u16(rhs),count=rs_u32(rhs),previous=0;if(raw||number!=j+2||count<0||count>q)throw std::runtime_error("all original RHS target mapping");for(int e=0;e<count;e++){int c=rs_u16(rhs),len=rhs.get();if(c<=previous||c>q||len<1||len>N+1)throw std::runtime_error("original RHS NF entry");previous=c;int last=0;for(int d=0;d<len;d++){last=rhs.get();if(last<0||last>30)throw std::runtime_error("original RHS field element");BitOps::set(target[j],nwRHS,d*W*32+c-1,last);}if(!last)throw std::runtime_error("noncanonical RHS polynomial");}}
 if(rhs.get()!=EOF)throw std::runtime_error("trailing RHS NF");remainders=target;
 auto addScalar=[&](Row &dest,int stride,int offset,const Row &source,int sourceStride,int sourceOffset,int words,int a){auto rep=ops.rep[a];BitOps::add(dest,stride,offset,source,sourceStride,sourceOffset,words,rep.rot,rep.neg);if(rep.c)BitOps::add(dest,stride,offset,source,sourceStride,sourceOffset,words,(rep.rot+(rep.c==1?1:2))%5,rep.neg);};
 uint64_t imageReductions=0,kernelReductions=0;std::array<uint64_t,nt> remainderNonzero{};std::array<int,nt> targetCosts;targetCosts.fill(-1);
 for(int j=0;j<nt;j++){
  auto &current=remainders[j];for(int d=N;d>=0;d--)for(int c=0;c<q;c++)if(image[c]&&d>=image[c]->degree){int a=BitOps::get(current,nwRHS,d*W*32+c);if(!a)continue;const auto &G=*image[c];int shift=d-G.degree;addScalar(current,nwRHS,shift*W,G.output,G.outWords,0,G.outWords,31-a);
   for(int g=1;g<6;g++){const auto &H=groups[g];if(shift+G.layers[g]>B-H.delta+1)throw std::runtime_error("temporary image source budget");addScalar(coefficients[j],accWords,H.accOffset+shift*H.words,G.source,G.sourceWords,G.offsets[g],G.layers[g]*H.words,a);}imageReductions++;
  }
  for(int c=0;c<q;c++)for(int d=0;d<=N;d++){int a=BitOps::get(current,nwRHS,d*W*32+c);if(a){if(image[c]&&d>=image[c]->degree)throw std::runtime_error("retained reducible image term");remainderNonzero[j]++;}}
  std::cout<<"{\"phase\":\"original-rhs-image-normal-form\",\"target\":"<<j+2<<",\"imageReductions\":"<<imageReductions<<",\"remainderNonzeroCoefficients\":"<<remainderNonzero[j]<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
  for(int cost=B;cost>=15;cost--)for(int g=1;g<6;g++){
   const auto &H=groups[g];int layer=cost-H.delta;if(layer<0)continue;for(int c=0;c<H.count;c++){int coordinate=H.componentOffset-q+c;if(!kernel[coordinate]||kernel[coordinate]->cost>cost)continue;int a=BitOps::get(coefficients[j],accWords,32*(H.accOffset+layer*H.words)+c);if(!a)continue;const auto &K=*kernel[coordinate];int shift=cost-K.cost,factor=a*ops.inv[K.lc]%31;
    for(int gg=1;gg<6;gg++){const auto &F=groups[gg];int words=K.layers[gg]*F.words;if(!words)continue;if(shift+K.layers[gg]>B-F.delta+1)throw std::runtime_error("kernel source cost increased");addScalar(coefficients[j],accWords,F.accOffset+shift*F.words,K.source,K.sourceWords,K.offsets[gg],words,31-factor);}kernelReductions++;
   }
  }
  std::cout<<"{\"phase\":\"original-rhs-kernel-standard-source\",\"target\":"<<j+2<<",\"kernelReductions\":"<<kernelReductions<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 }
 std::string prefix=argv[4];std::ofstream cout(prefix+"-standard-coefficients.bin",std::ios::binary),rout(prefix+"-image-remainders.bin",std::ios::binary),meta(prefix+"-standard-source.json");if(!cout||!rout||!meta)throw std::runtime_error("output open");
 cout.write("R150SC31",8);for(int a:{ns,nt,B,N,finalBudget})u32(cout,a);rout.write("R150NF31",8);u32(rout,0);u32(rout,nt);u32(rout,q);
 const int productWords=q*(B+1);Row product(5*productWords);
 for(int j=0;j<nt;j++){
  struct Entry {int component;std::vector<uint8_t> co;};std::vector<Entry> entries;
  for(int c=0;c<q;c++){std::vector<uint8_t> cp(N+1);for(int d=0;d<=N;d++){int r=BitOps::get(remainders[j],nwRHS,d*W*32+c),t=BitOps::get(target[j],nwRHS,d*W*32+c);cp[d]=r;BitOps::set(product,productWords,(c*(B+1)+d)*32+j,(r-t+31)%31);}while(!cp.empty()&&!cp.back())cp.pop_back();if(!cp.empty())entries.push_back({c+1,std::move(cp)});}
  u32(rout,0);u16(rout,j+2);u32(rout,entries.size());for(const auto &e:entries){u16(rout,e.component);rout.put(char(e.co.size()));rout.write(reinterpret_cast<const char*>(e.co.data()),e.co.size());}
 }
 input.read(magic,8);if(std::string(magic,8)!="R150NF31"||rs_u32(input)!=ns||rs_u32(input)!=nt||rs_u32(input)!=q)throw std::runtime_error("full original R input");int maximumDegree=-1,nonzeroSources=0;uint64_t nonzeroCoefficients=0;
 for(int i=0;i<ns;i++){
  const auto &S=sources[i];const auto &H=groups[S.group];int cutoff=kernel[S.coordinate]?kernel[S.coordinate]->cost-S.delta:-1,degree=-1,nnz=0;std::vector<std::vector<uint8_t>> polys(nt);
  for(int j=0;j<nt;j++){polys[j].resize(B-S.delta+1);for(int d=0;d<int(polys[j].size());d++){int a=BitOps::get(coefficients[j],accWords,32*(H.accOffset+d*H.words)+S.local);polys[j][d]=a;if(a){if(cutoff>=0&&d>=cutoff)throw std::runtime_error("retained reducible kernel monomial");targetCosts[j]=std::max(targetCosts[j],d+S.delta);nnz++;}}while(!polys[j].empty()&&!polys[j].back())polys[j].pop_back();degree=std::max(degree,int(polys[j].size())-1);}
  maximumDegree=std::max(maximumDegree,degree);nonzeroCoefficients+=nnz;if(nnz)nonzeroSources++;u32(cout,i+1);u32(cout,S.raw);u16(cout,S.delta);for(const auto &p:polys){u16(cout,p.size());cout.write(reinterpret_cast<const char*>(p.data()),p.size());}
  Triple packed;int stride=degree+1;packed[0].resize(5*stride);if(degree>=0){for(int j=0;j<nt;j++)for(int d=0;d<int(polys[j].size());d++)BitOps::set(packed[0],stride,d*32+j,polys[j][d]);BitOps::refresh(packed,stride,0);}
  int raw=rs_u32(input),number=rs_u16(input),count=rs_u32(input),observedDegree=-1,previous=0;if(raw!=S.raw||number||count<0||count>q)throw std::runtime_error("original R source mapping");for(int e=0;e<count;e++){int c=rs_u16(input),len=input.get();if(c<=previous||c>q||len<1||len>46)throw std::runtime_error("original R entry");previous=c;observedDegree=std::max(observedDegree,len-1);for(int d=0;d<len;d++){int a=input.get();if(a<0||a>30)throw std::runtime_error("original R coefficient");if(a&&degree>=0){if(d+degree>B)throw std::runtime_error("full R product budget");auto rep=ops.rep[a];BitOps::add(product,productWords,(c-1)*(B+1)+d,packed[rep.c],stride,0,stride,rep.rot,rep.neg);}}}
  if(observedDegree!=S.delta)throw std::runtime_error("original R source degree");
  if((i+1)%500==0||i+1==ns)std::cout<<"{\"phase\":\"verify-complete-rhs-source-decomposition\",\"sources\":"<<i+1<<",\"maximumCoefficientDegree\":"<<maximumDegree<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 }
 for(int j=0;j<nt;j++){int raw=rs_u32(input),number=rs_u16(input),count=rs_u32(input);if(raw||number!=j+2||count<0||count>q)throw std::runtime_error("original input trailing target");for(int e=0;e<count;e++){int c=rs_u16(input),len=input.get();if(c<1||c>q||len<1||len>27)throw std::runtime_error("original input trailing target entry");input.seekg(len,std::ios::cur);}}
 if(input.get()!=EOF)throw std::runtime_error("trailing full original R input");for(auto a:product)if(a)throw std::runtime_error("full R*C+remainder=original RHS identity failed");
 bool allImage=true,allBudget=true;for(int j=0;j<nt;j++){allImage&=remainderNonzero[j]==0;allBudget&=targetCosts[j]<=finalBudget;}
 meta<<"{\"format\":\"r150-original-rhs-standard-source-v1\",\"status\":\"completed\",\"prime\":31,\"temporarySourceBudget\":181,\"fixedOriginalSourceBudget\":85,\"sourceRows\":2195,\"imageBasisRows\":1021,\"kernelBasisRows\":1174,\"outputDegreeSum\":716,\"kernelCostSum\":60050,\"fullNormalFormDecompositionIdentity\":true,\"standardKernelNormalForm\":true,\"completeRHSInImage\":"<<(allImage?"true":"false")<<",\"allStandardSourceCostsWithinBudget\":"<<(allBudget?"true":"false")<<",\"fixedSourceImageTestPassed\":"<<(allImage&&allBudget?"true":"false")<<",\"originalCorrectionTransported\":false,\"maximumCoefficientDegree\":"<<maximumDegree<<",\"nonzeroSources\":"<<nonzeroSources<<",\"nonzeroCoefficients\":"<<nonzeroCoefficients<<",\"targetStandardSourceCosts\":[";
 for(int j=0;j<nt;j++){if(j)meta<<",";meta<<targetCosts[j];}meta<<"],\"imageRemainderNonzeroCoefficients\":[";for(int j=0;j<nt;j++){if(j)meta<<",";meta<<remainderNonzero[j];}
 meta<<"],\"sourceIdentity\":\"All nine actual original first residual NFs are reduced by the complete original image GB and actual zero-output kernel. The complete R*C+remainder=RHS identity is independently accumulated from all original R sources. Costs describe unique kernel standard representatives of RHS minus its image remainder. Fixed-budget failure excludes only these fixed original integer standard columns; no global characteristic-zero nonmembership is asserted. Original seventeen-equation correction transport remains separate.\",\"elapsedSeconds\":"<<elapsed()<<"}\n";
 cout.close();rout.close();meta.close();if(!cout||!rout||!meta)throw std::runtime_error("output failure");struct rusage usage{};getrusage(RUSAGE_SELF,&usage);
 std::cout<<"{\"status\":\"original-rhs-standard-source-test-complete\",\"fullNormalFormDecompositionIdentity\":true,\"standardKernelNormalForm\":true,\"completeRHSInImage\":"<<(allImage?"true":"false")<<",\"allStandardSourceCostsWithinBudget\":"<<(allBudget?"true":"false")<<",\"fixedSourceImageTestPassed\":"<<(allImage&&allBudget?"true":"false")<<",\"targetStandardSourceCosts\":[";
 for(int j=0;j<nt;j++){if(j)std::cout<<",";std::cout<<targetCosts[j];}std::cout<<"],\"imageRemainderNonzeroCoefficients\":[";for(int j=0;j<nt;j++){if(j)std::cout<<",";std::cout<<remainderNonzero[j];}std::cout<<"],\"imageReductions\":"<<imageReductions<<",\"kernelReductions\":"<<kernelReductions<<",\"peakRSSKiB\":"<<usage.ru_maxrss<<",\"elapsedSeconds\":"<<elapsed()<<"}\n";
 return 0;
}catch(const std::exception &e){std::cerr<<"ORIGINAL_RHS_STANDARD_SOLVER_FAILED "<<e.what()<<"\n";return 1;}}
