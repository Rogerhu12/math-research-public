// Exact original-source target lift from the complete fixed T=96 reweighted graph.
// Nonzero outputs of source-leading graph rows are reported, not called kernel rows.
// Reduces all nine h31*T and simultaneously accumulates the actual source rows.
// Finally verifies R*C=h31*T coefficientwise in every original NF component.
#include "2026-11-14-r150-f31-bitplane-789f.hpp"
#include <cstdio>
static uint32_t gl_u32(std::istream &in){uint32_t a=0;for(int k=0;k<4;k++){int c=in.get();if(c<0)throw std::runtime_error("truncated u32");a|=uint32_t(c)<<(8*k);}return a;}
static uint16_t gl_u16(std::istream &in){int a=in.get(),b=in.get();if(a<0||b<0)throw std::runtime_error("truncated u16");return a|(b<<8);}
static void gl_words(std::istream &in,uint32_t *destination,size_t count){in.read(reinterpret_cast<char*>(destination),4*count);if(!in)throw std::runtime_error("truncated bit planes");}
struct GLGroup {int shift=0,count=0,words=0,layers=0,wordOffset=0,componentOffset=0,accOffset=0;};
struct GLSource {int group=-1,local=-1,raw=0,degree=0;};
struct GLPivot {Row output,source;int degree=-1,outWords=0,sourceWords=0;std::array<int,6> offsets{};};

int main(int argc,char **argv){try{
 if(argc!=5)return 2;uint32_t endian=1;if(*reinterpret_cast<uint8_t*>(&endian)!=1)throw std::runtime_error("native bit-plane reader requires little endian");
 auto start=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 const int ns=2195,nt=9,q=1034,Tshift=96,N=50,hd=24,W=(q+31)/32,nwTarget=(N+1)*W,productDegree=146,productWords=q*(productDegree+1);
 std::ifstream graph(argv[1],std::ios::binary),input(argv[2],std::ios::binary),hin(argv[3]);if(!graph||!input||!hin)throw std::runtime_error("input open");char magic[8];graph.read(magic,8);if(std::string(magic,8)!="R150GG31")throw std::runtime_error("graph magic");
 std::vector<int> dims;for(int j=0;j<9;j++)dims.push_back(gl_u32(graph));if(dims!=std::vector<int>{2195,1034,2195,96,8,2195,2195,6,1})throw std::runtime_error("graph is not the complete original input");
 BitOps ops;std::vector<GLGroup> groups(6);std::vector<GLSource> sources(ns);int accWords=0;
 for(int g=0;g<6;g++){auto &G=groups[g];G.shift=int32_t(gl_u32(graph));G.count=gl_u32(graph);G.words=gl_u32(graph);G.layers=gl_u32(graph);G.wordOffset=gl_u32(graph);G.componentOffset=gl_u32(graph);if(G.words!=(G.count+31)/32||G.layers!=9-G.shift)throw std::runtime_error("group storage");if(g){G.accOffset=accWords;accWords+=(N-G.shift+1)*G.words;for(int c=0;c<G.count;c++){int index=gl_u32(graph)-1,raw=gl_u32(graph);if(index<0||index>=ns||sources[index].group>=0||raw<1||raw>6188)throw std::runtime_error("source dictionary");sources[index]={g,c,raw,Tshift+G.shift};}}}
 if(groups[0].shift||groups[0].count!=q||accWords!=7569)throw std::runtime_error("source shift profile");for(const auto &s:sources)if(s.group<1)throw std::runtime_error("incomplete source dictionary");
 std::vector<std::unique_ptr<GLPivot>> piv(q);int outputRows=0,sourceRows=0,nonzeroSourceOutputs=0,outputDegreeSum=0;std::array<int,9> outputDegreeHistogram{};
 for(int b=0;b<ns;b++){
  int component=gl_u16(graph)-1,degree=int32_t(gl_u32(graph)),lc=graph.get();if(component<0||component>=3229||degree<-81||degree>8||lc<1||lc>30)throw std::runtime_error("graph pivot header");bool isOutput=component<q;
  std::unique_ptr<GLPivot> P;if(isOutput){if(degree<0||degree>8||piv[component])throw std::runtime_error("complete output basis degree or component");P=std::make_unique<GLPivot>();P->degree=degree;P->outWords=(degree+1)*W;P->output.resize(5*P->outWords);for(int g=1;g<6;g++){P->offsets[g]=P->sourceWords;P->sourceWords+=(degree-groups[g].shift+1)*groups[g].words;}P->source.resize(5*P->sourceWords);}
  for(int g=0;g<6;g++){const auto &G=groups[g];int layers=gl_u16(graph),expected=std::max(0,degree-G.shift+1);if(layers!=expected)throw std::runtime_error("shifted row layer count");int words=layers*G.words;
   if(isOutput){for(int plane=0;plane<5;plane++)gl_words(graph,g==0?P->output.data()+plane*P->outWords:P->source.data()+plane*P->sourceWords+P->offsets[g],words);}
   else if(g==0){Row out(5*words);gl_words(graph,out.data(),out.size());bool nonzero=false;for(auto v:out)nonzero|=v!=0;if(nonzero)nonzeroSourceOutputs++;}
   else graph.seekg(uint64_t(5)*words*4,std::ios::cur);
  }
  if(!graph)throw std::runtime_error("truncated graph row");
  if(isOutput){
   int actualDegree=-1,actualComponent=-1;
   for(int d=degree;d>=0&&actualComponent<0;d--)for(int w=0;w<W;w++){uint32_t nz=0;for(int plane=0;plane<5;plane++)nz|=P->output[plane*P->outWords+d*W+w];if(nz){actualDegree=d;actualComponent=32*w+__builtin_ctz(nz);break;}}
   if(actualDegree!=degree||actualComponent!=component||BitOps::get(P->output,P->outWords,degree*W*32+component)!=lc)throw std::runtime_error("recorded output leading monomial");
   int scale=ops.inv[lc];if(scale!=1){ops.multiple(P->output,P->outWords,0,scale);ops.multiple(P->source,P->sourceWords,0,scale);}
   piv[component]=std::move(P);outputRows++;outputDegreeSum+=degree;outputDegreeHistogram[degree]++;
  }else sourceRows++;
 }
 if(graph.get()!=EOF||outputRows!=1021||sourceRows!=1174)throw std::runtime_error("complete reweighted graph row counts");
 const bool projectionSpanCertified=outputDegreeSum==716;
 std::vector<int> h(hd+1);for(auto &a:h){hin>>a;if(a<0||a>30)throw std::runtime_error("h coefficient");}int extra;if(!hin||hin>>extra||h.back()!=1)throw std::runtime_error("common h degree");
 input.read(magic,8);if(std::string(magic,8)!="R150NF31"||gl_u32(input)!=ns||gl_u32(input)!=nt||gl_u32(input)!=q)throw std::runtime_error("original NF input");
 for(int index=0;index<ns;index++){int raw=gl_u32(input),target=gl_u16(input),count=gl_u32(input),degree=-1,previous=0;if(raw!=sources[index].raw||target||count<0||count>q)throw std::runtime_error("original NF source mapping");for(int j=0;j<count;j++){int c=gl_u16(input),len=input.get();if(c<=previous||c>q||len<1||len>46)throw std::runtime_error("NF entry");previous=c;degree=std::max(degree,len-1);input.seekg(len,std::ios::cur);}if(degree!=sources[index].degree)throw std::runtime_error("source degree mapping");}
 std::vector<uint32_t> targetSums(size_t(nt)*q*(N+1));
 for(int j=0;j<nt;j++){int raw=gl_u32(input),target=gl_u16(input),count=gl_u32(input);if(raw||target!=j+2||count<0||count>q)throw std::runtime_error("original target mapping");for(int e=0;e<count;e++){int c=gl_u16(input)-1,len=input.get();if(c<0||c>=q||len<1||len>27)throw std::runtime_error("target degree exceeds observed bound");for(int k=0;k<len;k++){int a=input.get();if(a<0||a>30)throw std::runtime_error("target coefficient");for(int d=0;d<=hd;d++)targetSums[(j*q+c)*(N+1)+k+d]+=a*h[d];}}}
 if(input.get()!=EOF)throw std::runtime_error("trailing NF input");for(auto &a:targetSums)a%=31;
 std::vector<Row> coefficients(nt,Row(5*accWords));uint64_t reductions=0,sourceWordAdditions=0;
 auto addScalar=[&](Row &destination,int stride,int offset,const Row &source,int sourceStride,int sourceOffset,int words,int a){auto rep=ops.rep[a];BitOps::add(destination,stride,offset,source,sourceStride,sourceOffset,words,rep.rot,rep.neg);if(rep.c)BitOps::add(destination,stride,offset,source,sourceStride,sourceOffset,words,(rep.rot+(rep.c==1?1:2))%5,rep.neg);};
 for(int j=0;j<nt;j++){
  Row current(5*nwTarget);for(int c=0;c<q;c++)for(int d=0;d<=N;d++)BitOps::set(current,nwTarget,d*W*32+c,targetSums[(j*q+c)*(N+1)+d]);
  for(int d=N;d>=0;d--)for(int c=0;c<q;c++)if(piv[c]&&d>=piv[c]->degree){int a=BitOps::get(current,nwTarget,d*W*32+c);if(!a)continue;const auto &P=*piv[c];int shift=d-P.degree;addScalar(current,nwTarget,shift*W,P.output,P.outWords,0,P.outWords,31-a);
   for(int g=1;g<6;g++){const auto &G=groups[g];int words=(P.degree-G.shift+1)*G.words;addScalar(coefficients[j],accWords,G.accOffset+shift*G.words,P.source,P.sourceWords,P.offsets[g],words,a);sourceWordAdditions+=words*(ops.rep[a].c?2:1);}reductions++;
  }
  for(auto a:current)if(a)throw std::runtime_error("h31 original target does not reduce to zero");std::cout<<"{\"phase\":\"graph-source-target-lift\",\"target\":"<<j+2<<",\"reductions\":"<<reductions<<",\"sourceWordAdditions\":"<<sourceWordAdditions<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 }
 std::string prefix=argv[4];
 // Atomic small checkpoint before the potentially longer full polynomial check.
 // It contains ALL original source coefficients, not a partial graph prefix.
 {
  std::ofstream checkpoint(prefix+"-lift-checkpoint.tmp",std::ios::binary);if(!checkpoint)throw std::runtime_error("lift checkpoint open");checkpoint.write("R150LC31",8);for(int a:{ns,nt,accWords,N,productDegree,hd})u32(checkpoint,a);for(int a:h)checkpoint.put(char(a));
  for(const auto &G:groups)for(int a:{G.shift,G.count,G.words,G.accOffset})u32(checkpoint,uint32_t(a));
  for(const auto &S:sources){u16(checkpoint,S.group);u16(checkpoint,S.local);u32(checkpoint,S.raw);u16(checkpoint,S.degree);}
  for(const auto &row:coefficients)for(auto word:row)u32(checkpoint,word);checkpoint.close();if(!checkpoint||std::rename((prefix+"-lift-checkpoint.tmp").c_str(),(prefix+"-lift-checkpoint.bin").c_str()))throw std::runtime_error("atomic lift checkpoint failed");
  std::cout<<"{\"phase\":\"all-target-coefficients-checkpointed\",\"sources\":2195,\"targets\":9,\"verificationPending\":true,\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 }
 std::ofstream out(prefix+"-original-coefficients.bin",std::ios::binary),meta(prefix+"-original-coefficients.json");if(!out||!meta)throw std::runtime_error("coefficient output");out.write("R150TC31",8);u32(out,ns);u32(out,nt);u32(out,hd);for(int a:h)out.put(char(a));
 Row product(5*productWords);for(int j=0;j<nt;j++)for(int c=0;c<q;c++)for(int d=0;d<=N;d++)BitOps::set(product,productWords,(c*(productDegree+1)+d)*32+j,31-targetSums[(j*q+c)*(N+1)+d]);
 input.clear();input.seekg(20);int maximum=-1,nonzeroSources=0;uint64_t nonzeroCoefficients=0,verificationProducts=0;std::vector<std::array<int,5>> sourceStats;
 for(int index=0;index<ns;index++){
  const auto &S=sources[index];const auto &G=groups[S.group];const int bound=N-G.shift;std::vector<std::vector<uint8_t>> cp(nt);int degree=-1,nnz=0;
  for(int j=0;j<nt;j++){cp[j].resize(bound+1);for(int d=0;d<=bound;d++){int a=BitOps::get(coefficients[j],accWords,32*(G.accOffset+d*G.words)+S.local);cp[j][d]=a;nnz+=a!=0;}while(!cp[j].empty()&&!cp[j].back())cp[j].pop_back();degree=std::max(degree,int(cp[j].size())-1);}
  if(degree>146-S.degree)throw std::runtime_error("original-source coefficient degree bound failed");maximum=std::max(maximum,degree);nonzeroCoefficients+=nnz;if(nnz)nonzeroSources++;sourceStats.push_back({index+1,S.raw,S.degree,degree,nnz});
  u32(out,index+1);u32(out,S.raw);u16(out,S.degree);for(auto &polynomial:cp){u16(out,polynomial.size());out.write(reinterpret_cast<const char*>(polynomial.data()),polynomial.size());}
  Triple packed;int packedWords=degree+1;packed[0].resize(5*packedWords);for(int j=0;j<nt;j++)for(int d=0;d<int(cp[j].size());d++)BitOps::set(packed[0],packedWords,d*32+j,cp[j][d]);if(degree>=0)BitOps::refresh(packed,packedWords,0);
  int raw=gl_u32(input),target=gl_u16(input),count=gl_u32(input);if(raw!=S.raw||target)throw std::runtime_error("verification original source identity");for(int e=0;e<count;e++){int c=gl_u16(input)-1,len=input.get();if(c<0||c>=q||len<1||len>46)throw std::runtime_error("verification source entry");for(int d=0;d<len;d++){int a=input.get();if(a<0||a>30)throw std::runtime_error("verification source coefficient");if(a&&degree>=0){if(d+degree>productDegree)throw std::runtime_error("product degree overflow");auto rep=ops.rep[a];BitOps::add(product,productWords,c*(productDegree+1)+d,packed[rep.c],packedWords,0,packedWords,rep.rot,rep.neg);verificationProducts++;}}}
  if((index+1)%250==0||index+1==ns)std::cout<<"{\"phase\":\"verify-original-source-polynomial-identity\",\"sources\":"<<index+1<<",\"maximumCoefficientDegree\":"<<maximum<<",\"nonzeroCoefficients\":"<<nonzeroCoefficients<<",\"monomialProducts\":"<<verificationProducts<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 }
 for(auto a:product)if(a)throw std::runtime_error("full original R*C=h31*T coefficient identity failed");
 meta<<"{\"format\":\"r150-reweighted-graph-original-target-lift-v2\",\"status\":\"completed\",\"field\":31,\"originalSources\":2195,\"targets\":[2,3,4,5,6,7,8,9,10],\"commonAnnihilatorDegree\":24,\"maximumCoefficientDegree\":"<<maximum<<",\"sourceCoefficientDegreeBound\":\"146-degree(R_j)\",\"allDegreeBoundsVerified\":true,\"nonzeroSources\":"<<nonzeroSources<<",\"nonzeroCoefficients\":"<<nonzeroCoefficients<<",\"fullNormalFormSourceIdentity\":true,\"maximumProductDegree\":146,\"graphOutputRows\":1021,\"graphSourceLeadingRows\":1174,\"sourceLeadingRowsWithNonzeroOutput\":"<<nonzeroSourceOutputs<<",\"outputDegreeSum\":"<<outputDegreeSum<<",\"referenceOutputDegreeSum\":716,\"projectionSpanCertified\":"<<(projectionSpanCertified?"true":"false")<<",\"allGraphRowsRetained\":true,\"normalReductions\":"<<reductions<<",\"verificationMonomialProducts\":"<<verificationProducts<<",\"sourceStats\":[";for(size_t i=0;i<sourceStats.size();i++){if(i)meta<<",";auto a=sourceStats[i];meta<<"["<<a[0]<<","<<a[1]<<","<<a[2]<<","<<a[3]<<","<<a[4]<<"]";}meta<<"],\"sourceIdentity\":\"The output coefficients are indexed by all 2195 original normal-form sources and their exact raw 6188 row numbers. R*C=h31*T is verified coefficientwise for all 1034 components and all nine original targets. The 1174 source-leading graph rows are not assumed to be kernel rows. The original complete-image basis follows if the actual output degree sum is 716; the final target certificate in any case rests on all nine complete polynomial identities. Constant-prebasis recovery to the original seventeen equations remains a separate exact finite source transformation.\",\"elapsedSeconds\":"<<elapsed()<<"}\n";
 out.close();meta.close();if(!out||!meta)throw std::runtime_error("output failed");std::cout<<"{\"status\":\"original-nine-targets-low-degree-lift-complete\",\"maximumCoefficientDegree\":"<<maximum<<",\"nonzeroSources\":"<<nonzeroSources<<",\"nonzeroCoefficients\":"<<nonzeroCoefficients<<",\"fullNormalFormSourceIdentity\":true,\"allDegreeBoundsVerified\":true,\"sourceLeadingRowsWithNonzeroOutput\":"<<nonzeroSourceOutputs<<",\"outputDegreeSum\":"<<outputDegreeSum<<",\"projectionSpanCertified\":"<<(projectionSpanCertified?"true":"false")<<",\"elapsedSeconds\":"<<elapsed()<<"}\n";
 return 0;
}catch(const std::exception &e){std::cerr<<"REWEIGHTED_GRAPH_TARGET_LIFT_FAILED "<<e.what()<<"\n";return 1;}}
