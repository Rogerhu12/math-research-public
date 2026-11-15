// 2026-11-15. Author: ChatGPT (AI), literature_audit.
// Complete original polynomial I_2(A), bounded packed batches; no mathematics is claimed by this source.
// Saturated positive continuation: full original R identities, actual T96 VQ.
// Explicit source mode raw preserves the paid unnormalized section for q1.
// Mode standard may use all 1174 actual kernel rows for later source costs.
// No original6188 transport is claimed by this helper.
#include "2026-11-14-r150-f31-bitplane-789f.hpp"
#include <sys/resource.h>
#include <csignal>
#include <cstdio>
static volatile std::sig_atomic_t ps_stop=0;
static void ps_signal(int){ps_stop=1;}
static uint32_t ps_u32(std::istream &in){uint32_t x=0;for(int k=0;k<4;k++){int a=in.get();if(a<0)throw std::runtime_error("truncated u32");x|=uint32_t(a)<<(8*k);}return x;}
static uint16_t ps_u16(std::istream &in){int a=in.get(),b=in.get();if(a<0||b<0)throw std::runtime_error("truncated u16");return a|(b<<8);}
static void ps_words(std::istream &in,uint32_t *p,size_t n){in.read(reinterpret_cast<char*>(p),n*4);if(!in)throw std::runtime_error("truncated bitplanes");}
struct PSGroup {int shift=0,delta=0,count=0,words=0,layers=0,component=0,accOffset=0;};
struct PSSource {int group=-1,local=-1,raw=0,delta=0,coordinate=-1;};
struct PSRow {Row output,source;int degree=0,cost=0,lc=0,originalLC=0,outWords=0,sourceWords=0;std::array<int,6> offsets{},layers{};};

int main(int argc,char **argv){try{
 if(argc!=9)return 2;
 const std::string sourceMode=argv[8];if(sourceMode!="raw"&&sourceMode!="standard")throw std::runtime_error("source mode must be raw or standard");const bool normalizeKernel=sourceMode=="standard";
 std::signal(SIGTERM,ps_signal);std::signal(SIGINT,ps_signal);
 std::string prefix=argv[6],binding=argv[7];if(binding.size()!=64||binding.find_first_not_of("0123456789abcdef")!=std::string::npos)throw std::runtime_error("checkpoint input binding must be a SHA256");
 #ifndef R150_TARGETS
#define R150_TARGETS 9
#endif
 constexpr int ns=2195,nt=R150_TARGETS,q=1034,T=96,W=33;
 static_assert(nt>=1 && nt<=31);
 auto label=[&](int j){return j+2;};
 uint32_t endian=1;if(*reinterpret_cast<uint8_t*>(&endian)!=1)throw std::runtime_error("little endian required");
 auto start=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 std::ifstream graph(argv[1],std::ios::binary),input(argv[2],std::ios::binary),rhs(argv[3],std::ios::binary),quot(argv[4],std::ios::binary),rem(argv[5],std::ios::binary);
 if(!graph||!input||!rhs||!quot||!rem)throw std::runtime_error("source-convolution input open");
 BitOps ops;char magic[8];quot.read(magic,8);
 if(std::string(magic,8)!="R150IQ31"||ps_u32(quot)!=q||ps_u32(quot)!=1021||ps_u32(quot)!=nt)throw std::runtime_error("all packed actual complete image quotients required");
 const int N=ps_u32(quot),B=N+T,nwRHS=(N+1)*W;
 if(N<40||N>1249||B>1345)throw std::runtime_error("proved saturated continuation RHS40..1249 and source<=1345");
 graph.read(magic,8);if(std::string(magic,8)!="R150GG31")throw std::runtime_error("graph magic");
 std::vector<int> dimensions;for(int i=0;i<9;i++)dimensions.push_back(ps_u32(graph));
 if(dimensions!=std::vector<int>{2195,1034,2195,96,8,2195,2195,6,1})throw std::runtime_error("complete original T96 graph required");
 std::array<PSGroup,6> groups;std::array<int,6> counts{1034,6,66,396,11,1716},deltas{0,15,25,35,40,45};
 std::vector<PSSource> sources(ns);std::vector<int> sourceIndexByCoordinate(ns,-1);int accWords=0,components=0,graphWords=0;
 for(int g=0;g<6;g++){
  auto &G=groups[g];G.shift=int32_t(ps_u32(graph));G.count=ps_u32(graph);G.words=ps_u32(graph);G.layers=ps_u32(graph);int offset=ps_u32(graph);G.component=ps_u32(graph);G.delta=deltas[g];
  if(G.shift!=(g?G.delta-T:0)||G.count!=counts[g]||G.words!=(G.count+31)/32||G.layers!=9-G.shift||offset!=graphWords||G.component!=components)throw std::runtime_error("exact original graph groups");
  graphWords+=G.words*G.layers;components+=G.count;
  if(g){G.accOffset=accWords;accWords+=(B-G.delta+1)*G.words;
   for(int c=0;c<G.count;c++){int i=ps_u32(graph)-1,r=ps_u32(graph),coordinate=G.component-q+c;
    if(i<0||i>=ns||sources[i].group>=0||r<1||r>6188||sourceIndexByCoordinate[coordinate]>=0)throw std::runtime_error("actual source dictionary");
    sources[i]={g,c,r,G.delta,coordinate};sourceIndexByCoordinate[coordinate]=i;
   }
  }
 }
 if(graphWords!=4842||components!=3229)throw std::runtime_error("complete graph dimensions");
 for(const auto &S:sources)if(S.group<1)throw std::runtime_error("complete original source dictionary");
 std::vector<std::unique_ptr<PSRow>> image(q),kernel(ns);std::vector<bool> seen(3229);
 int outputRows=0,kernelRows=0,outputDegreeSum=0,kernelCostSum=0;
 for(int r=0;r<ns;r++){
  int component=ps_u16(graph)-1,d=int32_t(ps_u32(graph)),lc=graph.get();
  if(component<0||component>=3229||seen[component]||d<-81||d>8||lc<1||lc>30)throw std::runtime_error("actual graph row header");
  seen[component]=true;bool isOutput=component<q;auto row=std::make_unique<PSRow>();
  row->degree=d;row->cost=d+T;row->lc=lc;row->originalLC=lc;
  if(isOutput){if(d<0)throw std::runtime_error("negative output degree");row->outWords=(d+1)*W;row->output.resize(5*row->outWords);}
  for(int g=1;g<6;g++){row->offsets[g]=row->sourceWords;row->layers[g]=std::max(0,d-groups[g].shift+1);row->sourceWords+=row->layers[g]*groups[g].words;}
  row->source.resize(5*row->sourceWords);
  for(int g=0;g<6;g++){
   int layers=ps_u16(graph),words=layers*groups[g].words;
   if(layers!=std::max(0,d-groups[g].shift+1))throw std::runtime_error("actual graph layers");
   if(g==0){if(isOutput)ps_words(graph,row->output.data(),row->output.size());else{Row output(5*words);ps_words(graph,output.data(),output.size());for(auto v:output)if(v)throw std::runtime_error("source-leading row is not genuine kernel");}}
   else for(int b=0;b<5;b++)ps_words(graph,row->source.data()+b*row->sourceWords+row->offsets[g],words);
  }
  if(isOutput){
   int ad=-1,ac=-1;for(int z=d;z>=0&&ac<0;z--)for(int w=0;w<W;w++){uint32_t nz=0;for(int b=0;b<5;b++)nz|=row->output[b*row->outWords+z*W+w];if(nz){ad=z;ac=32*w+__builtin_ctz(nz);break;}}
   if(ad!=d||ac!=component||BitOps::get(row->output,row->outWords,d*W*32+component)!=lc)throw std::runtime_error("actual image leading identity");
   if(lc!=1){ops.multiple(row->output,row->outWords,0,ops.inv[lc]);ops.multiple(row->source,row->sourceWords,0,ops.inv[lc]);row->lc=1;}
   image[component]=std::move(row);outputRows++;outputDegreeSum+=d;
  }else{
   int ad=-1,ac=-1;
   for(int cost=row->cost;cost>=15&&ac<0;cost--)for(int g=1;g<6&&ac<0;g++){
    const auto &G=groups[g];int layer=cost-G.delta;if(layer<0||layer>=row->layers[g])continue;
    for(int w=0;w<G.words;w++){uint32_t nz=0;for(int b=0;b<5;b++)nz|=row->source[b*row->sourceWords+row->offsets[g]+layer*G.words+w];
     if(nz){int c=32*w+__builtin_ctz(nz);if(c>=G.count)throw std::runtime_error("kernel padding");ad=cost;ac=G.component-q+c;
      if(BitOps::get(row->source,row->sourceWords,32*(row->offsets[g]+layer*G.words)+c)!=lc)throw std::runtime_error("actual kernel leading coefficient");break;}
    }
   }
   if(ac!=component-q||ad!=row->cost)throw std::runtime_error("actual kernel leading identity");
   kernelCostSum+=row->cost;kernel[component-q]=std::move(row);kernelRows++;
  }
 }
 if(graph.get()!=EOF||outputRows!=1021||kernelRows!=1174||outputDegreeSum!=716||kernelCostSum!=60050)throw std::runtime_error("complete original graph profile");
 auto readNF=[&](std::istream &in,bool irreducible){
  char header[8];in.read(header,8);bool wide=std::string(header,8)=="R150NX31";if((!wide&&std::string(header,8)!="R150NF31")||ps_u32(in)!=0||ps_u32(in)!=nt||ps_u32(in)!=q)throw std::runtime_error("complete nine-RHS NF header");
  std::vector<Row> out(nt,Row(5*nwRHS));
  for(int j=0;j<nt;j++){int raw=ps_u32(in),number=ps_u16(in),n=ps_u32(in),previous=0;
   if(raw||number!=label(j)||n<0||n>q)throw std::runtime_error("original nine-target RHS labels");
   for(int e=0;e<n;e++){int c=ps_u16(in),length=wide?ps_u16(in):in.get();if(c<=previous||c>q||length<1||length>N+1)throw std::runtime_error("RHS entry dictionary");previous=c;int last=0;
    for(int d=0;d<length;d++){last=in.get();if(last<0||last>30||(last&&irreducible&&image[c-1]&&d>=image[c-1]->degree))throw std::runtime_error("invalid or reducible saved remainder");BitOps::set(out[j],nwRHS,d*W*32+c-1,last);}
    if(!last)throw std::runtime_error("noncanonical RHS entry");
   }
  }
  if(in.get()!=EOF)throw std::runtime_error("trailing nine-RHS NF");return out;
 };
 auto target=readNF(rhs,false),remainder=readNF(rem,true);
 std::vector<Row> parallel(ns);std::vector<int> strides(ns);
 for(int i=0;i<ns;i++){strides[i]=B-sources[i].delta+1;parallel[i].resize(5*strides[i]);}
 uint64_t quotientCoefficients=0,sourceMonomialProducts=0;int previousHead=0,completedImageRows=0;
 auto put64=[&](std::ostream &o,uint64_t a){for(int k=0;k<8;k++)o.put(char(a>>(8*k)));};
 auto get64=[&](std::istream &in){uint64_t a=0;for(int k=0;k<8;k++){int c=in.get();if(c<0)throw std::runtime_error("truncated checkpoint integer");a|=uint64_t(c)<<(8*k);}return a;};
 const std::string checkpoint=prefix+"-vq-checkpoint.bin";
 {
  std::ifstream saved(checkpoint,std::ios::binary);
  if(saved){
   saved.read(magic,8);if(std::string(magic,8)!="R150VQ31"||ps_u32(saved)!=1||ps_u32(saved)!=N||ps_u32(saved)!=B||ps_u32(saved)!=ns||ps_u32(saved)!=nt||ps_u32(saved)!=q)throw std::runtime_error("actual source checkpoint dimensions");
   completedImageRows=ps_u32(saved);if(completedImageRows<0||completedImageRows>1021)throw std::runtime_error("checkpoint row boundary");
   quotientCoefficients=get64(saved);sourceMonomialProducts=get64(saved);std::string oldBinding(64,' ');saved.read(oldBinding.data(),64);if(oldBinding!=binding)throw std::runtime_error("checkpoint belongs to different frozen inputs");
   for(int i=0;i<ns;i++){if(ps_u32(saved)!=i+1||ps_u32(saved)!=sources[i].raw||ps_u32(saved)!=sources[i].delta||ps_u32(saved)!=strides[i])throw std::runtime_error("checkpoint actual original source dictionary");ps_words(saved,parallel[i].data(),parallel[i].size());}
   if(saved.get()!=EOF)throw std::runtime_error("trailing source checkpoint");
   std::cout<<"{\"phase\":\"restore-packed-source-checkpoint\",\"completedImageRows\":"<<completedImageRows<<",\"sourceMonomialProducts\":"<<sourceMonomialProducts<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
  }
 }
 const int resumedImageRows=completedImageRows;
 auto saveCheckpoint=[&](int done){
  const std::string temporary=checkpoint+".tmp";std::ofstream o(temporary,std::ios::binary);if(!o)throw std::runtime_error("source checkpoint open");
  o.write("R150VQ31",8);for(int a:{1,N,B,ns,nt,q,done})u32(o,a);put64(o,quotientCoefficients);put64(o,sourceMonomialProducts);o.write(binding.data(),64);
  for(int i=0;i<ns;i++){for(int a:{i+1,sources[i].raw,sources[i].delta,strides[i]})u32(o,a);o.write(reinterpret_cast<const char*>(parallel[i].data()),parallel[i].size()*4);}
  o.close();if(!o||std::rename(temporary.c_str(),checkpoint.c_str())!=0)throw std::runtime_error("atomic source checkpoint save");
  completedImageRows=done;
  std::ofstream m(prefix+"-vq-checkpoint.json");m<<"{\"format\":\"r150-packed-source-checkpoint-v1\",\"phase\":\"VQ-only-before-kernel-normalization\",\"completedImageRows\":"<<done<<",\"nextImageRowOneBased\":"<<done+1<<",\"fullNormalFormSourceIdentityVerified\":false,\"bindingSHA256\":\""<<binding<<"\",\"sourceMonomialProducts\":"<<sourceMonomialProducts<<",\"elapsedSeconds\":"<<elapsed()<<"}\n";m.close();if(!m)throw std::runtime_error("checkpoint metadata write");
 };
 for(int row=0;row<1021;row++){
  int c=ps_u16(quot),d=quot.get(),lc=quot.get();
  if(c<=previousHead||c>q||!image[c-1]||d!=image[c-1]->degree||lc!=image[c-1]->originalLC)throw std::runtime_error("actual quotient and source image basis mismatch");
  previousHead=c;const auto &G=*image[c-1];int maximum=-1;uint64_t rowQuotientCoefficients=0;std::array<std::vector<uint8_t>,nt> polys;
  for(int j=0;j<nt;j++){int n=ps_u16(quot);if(n>N-d+1)throw std::runtime_error("image quotient degree bound");polys[j].resize(n);
   for(int k=0;k<n;k++){int a=quot.get();if(a<0||a>30)throw std::runtime_error("quotient field coefficient");polys[j][k]=a;rowQuotientCoefficients+=a!=0;}
   if(n&&!polys[j].back())throw std::runtime_error("noncanonical quotient polynomial");maximum=std::max(maximum,n-1);
  }
  if(row<resumedImageRows)continue;quotientCoefficients+=rowQuotientCoefficients;
  if(maximum>=0){int stride=maximum+1;Triple packed;packed[0].resize(5*stride);
  for(int j=0;j<nt;j++)for(int k=0;k<int(polys[j].size());k++)BitOps::set(packed[0],stride,k*32+j,polys[j][k]);
  BitOps::refresh(packed,stride,0);
  for(int g=1;g<6;g++){const auto &H=groups[g];
   for(int exponent=0;exponent<G.layers[g];exponent++)for(int w=0;w<H.words;w++){
    int offset=G.offsets[g]+exponent*H.words+w;uint32_t nz=0;for(int b=0;b<5;b++)nz|=G.source[b*G.sourceWords+offset];
    while(nz){int bit=__builtin_ctz(nz);nz&=nz-1;int local=32*w+bit;if(local>=H.count)throw std::runtime_error("source image padding");
     int i=sourceIndexByCoordinate[H.component-q+local],a=BitOps::get(G.source,G.sourceWords,32*offset+bit);
     if(i<0||a<1||a>30||exponent+stride>strides[i])throw std::runtime_error("exact VQ source cost");
     auto rep=ops.rep[a];BitOps::add(parallel[i],strides[i],exponent,packed[rep.c],stride,0,stride,rep.rot,rep.neg);sourceMonomialProducts++;
    }
   }
  }
  }
  if((row+1)%100==0||row+1==1021||ps_stop){saveCheckpoint(row+1);std::cout<<"{\"phase\":\"packed-source-VQ-checkpoint\",\"completedImageRows\":"<<row+1<<",\"sourceMonomialProducts\":"<<sourceMonomialProducts<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;}
  if(ps_stop){std::cout<<"{\"status\":\"packed-image-source-convolution-checkpointed\",\"completedImageRows\":"<<completedImageRows<<",\"fullNormalFormDecompositionIdentity\":false,\"originalSeventeenEquationTransported\":false,\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;return 124;}
 }
 if(quot.get()!=EOF)throw std::runtime_error("trailing complete image quotients");
 std::vector<Row> coefficients(nt,Row(5*accWords));
 for(int i=0;i<ns;i++){const auto &S=sources[i];const auto &H=groups[S.group];
  for(int d=0;d<strides[i];d++){uint32_t padding=0;for(int b=0;b<5;b++)padding|=parallel[i][b*strides[i]+d];if(padding>>nt)throw std::runtime_error("packed-column padding");
   for(int j=0;j<nt;j++)BitOps::set(coefficients[j],accWords,32*(H.accOffset+d*H.words)+S.local,BitOps::get(parallel[i],strides[i],d*32+j));
  }
 }
 parallel.clear();parallel.shrink_to_fit();
 auto addScalar=[&](Row &dest,int stride,int offset,const Row &source,int sourceStride,int sourceOffset,int words,int a){auto rep=ops.rep[a];BitOps::add(dest,stride,offset,source,sourceStride,sourceOffset,words,rep.rot,rep.neg);if(rep.c)BitOps::add(dest,stride,offset,source,sourceStride,sourceOffset,words,(rep.rot+(rep.c==1?1:2))%5,rep.neg);};
 uint64_t kernelReductions=0;
 if(normalizeKernel)for(int j=0;j<nt;j++){
  for(int cost=B;cost>=15;cost--)for(int g=1;g<6;g++){
   const auto &H=groups[g];int layer=cost-H.delta;if(layer<0)continue;
   for(int c=0;c<H.count;c++){int coordinate=H.component-q+c;if(!kernel[coordinate]||kernel[coordinate]->cost>cost)continue;
    int a=BitOps::get(coefficients[j],accWords,32*(H.accOffset+layer*H.words)+c);if(!a)continue;const auto &K=*kernel[coordinate];int shift=cost-K.cost,factor=a*ops.inv[K.lc]%31;
    for(int gg=1;gg<6;gg++){const auto &F=groups[gg];int words=K.layers[gg]*F.words;if(!words)continue;
     if(shift+K.layers[gg]>B-F.delta+1)throw std::runtime_error("kernel cost increase");addScalar(coefficients[j],accWords,F.accOffset+shift*F.words,K.source,K.sourceWords,K.offsets[gg],words,31-factor);}
    kernelReductions++;
   }
  }
  std::cout<<"{\"phase\":\"canonical-original-source\",\"target\":"<<j+2<<",\"kernelReductions\":"<<kernelReductions<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 }
 std::ofstream out(prefix+"-standard-coefficients.bin",std::ios::binary),meta(prefix+"-source-certificate.json");if(!out||!meta)throw std::runtime_error("source certificate output open");
 out.write("R150SC31",8);for(int a:{ns,nt,B,N,N})u32(out,a);
 const int productWords=q*(B+1);Row product(5*productWords);std::array<uint64_t,nt> remainderCount{};std::array<int,nt> targetCosts;targetCosts.fill(-1);
 for(int j=0;j<nt;j++)for(int c=0;c<q;c++)for(int d=0;d<=N;d++){
  int r=BitOps::get(remainder[j],nwRHS,d*W*32+c),t=BitOps::get(target[j],nwRHS,d*W*32+c);remainderCount[j]+=r!=0;BitOps::set(product,productWords,(c*(B+1)+d)*32+j,(r-t+31)%31);
 }
 input.read(magic,8);if(std::string(magic,8)!="R150NF31"||ps_u32(input)!=ns||ps_u32(input)!=9||ps_u32(input)!=q)throw std::runtime_error("original R source input");
 int maximumDegree=-1,nonzeroSources=0;uint64_t nonzeroCoefficients=0,verificationProducts=0;
 for(int i=0;i<ns;i++){
  const auto &S=sources[i];const auto &H=groups[S.group];int cutoff=kernel[S.coordinate]?kernel[S.coordinate]->cost-S.delta:-1,degree=-1,count=0;std::array<std::vector<uint8_t>,nt> polys;
  for(int j=0;j<nt;j++){polys[j].resize(B-S.delta+1);
   for(int d=0;d<int(polys[j].size());d++){int a=BitOps::get(coefficients[j],accWords,32*(H.accOffset+d*H.words)+S.local);polys[j][d]=a;
    if(a){if(normalizeKernel&&cutoff>=0&&d>=cutoff)throw std::runtime_error("retained reducible source monomial");targetCosts[j]=std::max(targetCosts[j],d+S.delta);count++;}}
   while(!polys[j].empty()&&!polys[j].back())polys[j].pop_back();degree=std::max(degree,int(polys[j].size())-1);
  }
  maximumDegree=std::max(maximumDegree,degree);nonzeroCoefficients+=count;nonzeroSources+=count!=0;
  u32(out,i+1);u32(out,S.raw);u16(out,S.delta);for(const auto &poly:polys){u16(out,poly.size());out.write(reinterpret_cast<const char*>(poly.data()),poly.size());}
  Triple packed;int stride=degree+1;packed[0].resize(5*stride);
  if(degree>=0){for(int j=0;j<nt;j++)for(int d=0;d<int(polys[j].size());d++)BitOps::set(packed[0],stride,d*32+j,polys[j][d]);BitOps::refresh(packed,stride,0);}
  int raw=ps_u32(input),number=ps_u16(input),entries=ps_u32(input),observedDegree=-1,previous=0;
  if(raw!=S.raw||number||entries<0||entries>q)throw std::runtime_error("complete original R source identity");
  for(int e=0;e<entries;e++){int c=ps_u16(input),length=input.get();if(c<=previous||c>q||length<1||length>46)throw std::runtime_error("original R entry");previous=c;observedDegree=std::max(observedDegree,length-1);
   for(int d=0;d<length;d++){int a=input.get();if(a<0||a>30)throw std::runtime_error("original R field");
    if(a&&degree>=0){if(d+degree>B)throw std::runtime_error("full original R product bound");auto rep=ops.rep[a];BitOps::add(product,productWords,(c-1)*(B+1)+d,packed[rep.c],stride,0,stride,rep.rot,rep.neg);verificationProducts++;}}
  }
  if(observedDegree>S.delta)throw std::runtime_error("actual source degree exceeds original weighted bound");
  if((i+1)%500==0||i+1==ns)std::cout<<"{\"phase\":\"full-original-R-source-identity\",\"sources\":"<<i+1<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 }
 for(int j=0;j<9;j++){int raw=ps_u32(input),number=ps_u16(input),entries=ps_u32(input);if(raw||number!=j+2||entries<0||entries>q)throw std::runtime_error("trailing original target identity");
  for(int e=0;e<entries;e++){int c=ps_u16(input),length=input.get();if(c<1||c>q||length<1||length>27)throw std::runtime_error("trailing original target entry");input.seekg(length,std::ios::cur);}}
 if(input.get()!=EOF)throw std::runtime_error("trailing original R input");for(auto a:product)if(a)throw std::runtime_error("full original R*C+remainder=RHS identity failed");
 bool allImage=true,allBudget=true;for(int j=0;j<nt;j++){allImage&=remainderCount[j]==0;allBudget&=targetCosts[j]<=N;}
 auto writeArray=[&](std::ostream &o,const auto &a){o<<"[";for(int j=0;j<nt;j++){if(j)o<<",";o<<a[j];}o<<"]";};
 meta<<"{\"format\":\"r150-saturated-mode-selected-source-convolution-v1\",\"status\":\"completed\",\"field\":31,\"inputParameterBound\":"<<N<<",\"provedTemporarySourceCost\":"<<B<<",\"sourceRows\":2195,\"imageRows\":1021,\"kernelRows\":1174,\"fullNormalFormDecompositionIdentity\":true,\"standardKernelNormalForm\":"<<(normalizeKernel?"true":"false")<<",\"rawPaidVQSectionPreserved\":"<<(normalizeKernel?"false":"true")<<",\"sourceMode\":\""<<sourceMode<<"\",\"completeRHSInImage\":"<<(allImage?"true":"false")<<",\"allSourceCostsWithinRHSBound\":"<<(allBudget?"true":"false")<<",\"allStandardSourceCostsWithinInputBound\":"<<(normalizeKernel&&allBudget?"true":"false")<<",\"originalSeventeenEquationTransported\":false,\"maximumCoefficientDegree\":"<<maximumDegree<<",\"nonzeroSources\":"<<nonzeroSources<<",\"nonzeroCoefficients\":"<<nonzeroCoefficients<<",\"sourceMonomialProducts\":"<<sourceMonomialProducts<<",\"kernelReductions\":"<<kernelReductions<<",\"independentVerificationProducts\":"<<verificationProducts<<",\"targetStandardSourceCosts\":";writeArray(meta,targetCosts);meta<<",\"remainderNonzeroCoefficients\":";writeArray(meta,remainderCount);
 meta<<",\"sourceIdentity\":\"The complete actual T96 image row source V is paired with its saved monic G quotient. All requested RHS are packed during VQ convolution. Only sourceMode=standard applies the complete actual zero-output kernel. sourceMode=raw preserves VQ exactly and does not assert a canonical minimum-cost source. Every original2195 R row is then used for the independent full R*C+savedRemainder=RHS identity. This is not yet the original6188-row transport.\",\"elapsedSeconds\":"<<elapsed()<<"}\n";
 out.close();meta.close();if(!out||!meta)throw std::runtime_error("source certificate output failure");struct rusage usage{};getrusage(RUSAGE_SELF,&usage);
 std::cout<<"{\"status\":\"packed-image-source-convolution-complete\",\"fullNormalFormDecompositionIdentity\":true,\"standardKernelNormalForm\":"<<(normalizeKernel?"true":"false")<<",\"rawPaidVQSectionPreserved\":"<<(normalizeKernel?"false":"true")<<",\"sourceMode\":\""<<sourceMode<<"\",\"completeRHSInImage\":"<<(allImage?"true":"false")<<",\"originalSeventeenEquationTransported\":false,\"targetStandardSourceCosts\":";writeArray(std::cout,targetCosts);std::cout<<",\"sourceMonomialProducts\":"<<sourceMonomialProducts<<",\"kernelReductions\":"<<kernelReductions<<",\"peakRSSKiB\":"<<usage.ru_maxrss<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 return 0;
}catch(const std::exception &e){std::cerr<<"PACKED_IMAGE_SOURCE_CONVOLUTION_FAILED "<<e.what()<<"\n";return 1;}}
