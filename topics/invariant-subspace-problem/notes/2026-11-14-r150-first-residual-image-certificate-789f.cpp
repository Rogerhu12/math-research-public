// Complete image-normal-form certificate for the actual original first residual.
// Uses only the output blocks of the already certified complete original graph.
// Saves every G quotient and remainder and verifies G*Q+remainder=RHS in full.
#include "2026-11-14-r150-f31-bitplane-789f.hpp"
#include <sys/resource.h>
static uint32_t im_u32(std::istream &in){uint32_t v=0;for(int k=0;k<4;k++){int a=in.get();if(a<0)throw std::runtime_error("truncated u32");v|=uint32_t(a)<<(8*k);}return v;}
static uint16_t im_u16(std::istream &in){int a=in.get(),b=in.get();if(a<0||b<0)throw std::runtime_error("truncated u16");return a|(b<<8);}
struct IMGroup {int shift=0,count=0,words=0,layers=0,offset=0,component=0;};
struct IMPivot {Row row;int degree=0,stride=0,originalLC=0;};

int main(int argc,char **argv){try{
 if(argc!=4)return 2;constexpr int q=1034,nt=9,N=85,W=33,nw=(N+1)*W;
 uint32_t endian=1;if(*reinterpret_cast<uint8_t*>(&endian)!=1)throw std::runtime_error("little endian required");
 auto start=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 BitOps ops;std::ifstream graph(argv[1],std::ios::binary),rhs(argv[2],std::ios::binary);if(!graph||!rhs)throw std::runtime_error("input open");char magic[8];graph.read(magic,8);if(std::string(magic,8)!="R150GG31")throw std::runtime_error("graph header");std::vector<int> dims;for(int k=0;k<9;k++)dims.push_back(im_u32(graph));if(dims!=std::vector<int>{2195,1034,2195,96,8,2195,2195,6,1})throw std::runtime_error("actual complete T96 graph required");
 std::array<IMGroup,6> groups;std::array<int,6> counts{1034,6,66,396,11,1716},shifts{0,-81,-71,-61,-56,-51};int off=0,comp=0;std::vector<bool> dictionary(2195);
 for(int g=0;g<6;g++){auto &G=groups[g];G.shift=int32_t(im_u32(graph));G.count=im_u32(graph);G.words=im_u32(graph);G.layers=im_u32(graph);G.offset=im_u32(graph);G.component=im_u32(graph);if(G.shift!=shifts[g]||G.count!=counts[g]||G.words!=(G.count+31)/32||G.layers!=9-G.shift||G.offset!=off||G.component!=comp)throw std::runtime_error("exact original graph groups");off+=G.layers*G.words;comp+=G.count;
  if(g)for(int c=0;c<G.count;c++){int i=im_u32(graph)-1,raw=im_u32(graph);if(i<0||i>=2195||dictionary[i]||raw<1||raw>6188)throw std::runtime_error("original source dictionary");dictionary[i]=true;}
 }
 if(off!=4842||comp!=3229||std::count(dictionary.begin(),dictionary.end(),true)!=2195)throw std::runtime_error("complete source dictionary");
 std::vector<std::unique_ptr<IMPivot>> piv(q);std::vector<bool> seen(3229);int imageRows=0,kernelRows=0,degreeSum=0,kernelCostSum=0;
 for(int row=0;row<2195;row++){
  int c=im_u16(graph)-1,d=int32_t(im_u32(graph)),lc=graph.get();if(c<0||c>=3229||seen[c]||d<-81||d>8||lc<1||lc>30)throw std::runtime_error("actual graph row header");seen[c]=true;bool isOutput=c<q;std::unique_ptr<IMPivot> P;if(isOutput){if(d<0)throw std::runtime_error("output degree");P=std::make_unique<IMPivot>();P->degree=d;P->stride=(d+1)*W;P->originalLC=lc;P->row.resize(5*P->stride);}
  for(int g=0;g<6;g++){const auto &G=groups[g];int layers=im_u16(graph),words=layers*G.words;if(layers!=std::max(0,d-G.shift+1))throw std::runtime_error("graph row layers");if(g==0){if(isOutput)graph.read(reinterpret_cast<char*>(P->row.data()),size_t(P->row.size())*4);else{Row out(5*words);graph.read(reinterpret_cast<char*>(out.data()),size_t(out.size())*4);for(auto a:out)if(a)throw std::runtime_error("source-leading row is not true kernel");}}else graph.seekg(size_t(5)*words*4,std::ios::cur);if(!graph)throw std::runtime_error("truncated graph row");}
  if(isOutput){int ad=-1,ac=-1;for(int k=d;k>=0&&ac<0;k--)for(int w=0;w<W;w++){uint32_t nz=0;for(int b=0;b<5;b++)nz|=P->row[b*P->stride+k*W+w];if(nz){ad=k;ac=32*w+__builtin_ctz(nz);break;}}if(ad!=d||ac!=c||BitOps::get(P->row,P->stride,d*W*32+c)!=lc)throw std::runtime_error("true image leading term");if(lc!=1)ops.multiple(P->row,P->stride,0,ops.inv[lc]);piv[c]=std::move(P);imageRows++;degreeSum+=d;}
  else{kernelRows++;kernelCostSum+=d+96;}
 }
 if(graph.get()!=EOF||imageRows!=1021||kernelRows!=1174||degreeSum!=716||kernelCostSum!=60050)throw std::runtime_error("complete actual image/kernel profile");
 rhs.read(magic,8);if(std::string(magic,8)!="R150NF31"||im_u32(rhs)!=0||im_u32(rhs)!=nt||im_u32(rhs)!=q)throw std::runtime_error("all nine original RHS normal forms required");
 std::vector<Row> target(nt,Row(5*nw)),remainder,quotient(nt,Row(5*nw));
 for(int j=0;j<nt;j++){int raw=im_u32(rhs),number=im_u16(rhs),count=im_u32(rhs),previous=0;if(raw||number!=j+2||count<0||count>q)throw std::runtime_error("original RHS mapping");for(int e=0;e<count;e++){int c=im_u16(rhs),len=rhs.get();if(c<=previous||c>q||len<1||len>N+1)throw std::runtime_error("original RHS entry");previous=c;int last=0;for(int d=0;d<len;d++){last=rhs.get();if(last<0||last>30)throw std::runtime_error("original RHS field element");BitOps::set(target[j],nw,d*W*32+c-1,last);}if(!last)throw std::runtime_error("noncanonical RHS polynomial");}}
 if(rhs.get()!=EOF)throw std::runtime_error("trailing original RHS");remainder=target;uint64_t reductions=0;
 std::array<uint64_t,nt> remainderCount{};std::array<int,nt> remainderDegree;remainderDegree.fill(-1);std::array<std::array<int,3>,nt> first{};
 for(int j=0;j<nt;j++){
  for(int d=N;d>=0;d--)for(int c=0;c<q;c++)if(piv[c]&&d>=piv[c]->degree){int a=BitOps::get(remainder[j],nw,d*W*32+c);if(!a)continue;const auto &P=*piv[c];int shift=d-P.degree;auto R=ops.rep[31-a];BitOps::add(remainder[j],nw,shift*W,P.row,P.stride,0,P.stride,R.rot,R.neg);if(R.c)BitOps::add(remainder[j],nw,shift*W,P.row,P.stride,0,P.stride,(R.rot+(R.c==1?1:2))%5,R.neg);if(BitOps::get(quotient[j],nw,shift*W*32+c))throw std::runtime_error("repeated image quotient position");BitOps::set(quotient[j],nw,shift*W*32+c,a);reductions++;}
  for(int c=0;c<q;c++)for(int d=0;d<=N;d++){int a=BitOps::get(remainder[j],nw,d*W*32+c);if(a){if(piv[c]&&d>=piv[c]->degree)throw std::runtime_error("retained reducible image monomial");if(!remainderCount[j])first[j]={c+1,d,a};remainderCount[j]++;remainderDegree[j]=std::max(remainderDegree[j],d);}}
  std::cout<<"{\"phase\":\"complete-original-residual-image-NF\",\"target\":"<<j+2<<",\"reductions\":"<<reductions<<",\"remainderNonzeroCoefficients\":"<<remainderCount[j]<<",\"maximumRemainderDegree\":"<<remainderDegree[j]<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 }
 constexpr int productWords=q*(N+1);Row product(5*productWords);
 for(int j=0;j<nt;j++)for(int c=0;c<q;c++)for(int d=0;d<=N;d++){int a=BitOps::get(remainder[j],nw,d*W*32+c)-BitOps::get(target[j],nw,d*W*32+c);BitOps::set(product,productWords,(c*(N+1)+d)*32+j,(a+31)%31);}
 std::string prefix=argv[3];std::ofstream qout(prefix+"-image-quotients.bin",std::ios::binary),rout(prefix+"-image-remainders.bin",std::ios::binary),meta(prefix+"-image-certificate.json");if(!qout||!rout||!meta)throw std::runtime_error("certificate output open");qout.write("R150IQ31",8);for(int a:{q,1021,nt,N})u32(qout,a);uint64_t products=0,quotientNonzero=0;
 for(int c=0;c<q;c++)if(piv[c]){
  const auto &P=*piv[c];int bound=N-P.degree,stride=bound+1;Triple packed;packed[0].resize(5*stride);u16(qout,c+1);qout.put(char(P.degree));qout.put(char(P.originalLC));
  for(int j=0;j<nt;j++){std::vector<uint8_t> cp(stride);for(int d=0;d<=bound;d++){int a=BitOps::get(quotient[j],nw,d*W*32+c);cp[d]=a;if(a){BitOps::set(packed[0],stride,d*32+j,a);quotientNonzero++;}}while(!cp.empty()&&!cp.back())cp.pop_back();u16(qout,cp.size());qout.write(reinterpret_cast<const char*>(cp.data()),cp.size());}BitOps::refresh(packed,stride,0);
  for(int k=0;k<=P.degree;k++)for(int out=0;out<q;out++){int a=BitOps::get(P.row,P.stride,k*W*32+out);if(!a)continue;auto R=ops.rep[a];BitOps::add(product,productWords,out*(N+1)+k,packed[R.c],stride,0,stride,R.rot,R.neg);products++;}
 }
 for(auto a:product)if(a)throw std::runtime_error("full G*Q+remainder=original RHS certificate failed");
 rout.write("R150NF31",8);u32(rout,0);u32(rout,nt);u32(rout,q);for(int j=0;j<nt;j++){struct Entry{int c;std::vector<uint8_t> cp;};std::vector<Entry> entries;for(int c=0;c<q;c++){std::vector<uint8_t> cp(N+1);for(int d=0;d<=N;d++)cp[d]=BitOps::get(remainder[j],nw,d*W*32+c);while(!cp.empty()&&!cp.back())cp.pop_back();if(!cp.empty())entries.push_back({c+1,std::move(cp)});}u32(rout,0);u16(rout,j+2);u32(rout,entries.size());for(const auto &e:entries){u16(rout,e.c);rout.put(char(e.cp.size()));rout.write(reinterpret_cast<const char*>(e.cp.data()),e.cp.size());}}
 bool allImage=true;for(auto n:remainderCount)allImage&=n==0;
 meta<<"{\"format\":\"r150-first-residual-complete-image-certificate-v1\",\"status\":\"completed\",\"prime\":31,\"fixedOriginalSourceBudget\":85,\"completeImageBasisRows\":1021,\"completeImageDegreeSum\":716,\"fullImageQuotientIdentity\":true,\"everyRemainderIsIrreducible\":true,\"completeRHSInImage\":"<<(allImage?"true":"false")<<",\"fixedOriginalIntegerColumnSpaceLiftObstructed\":"<<(allImage?"false":"true")<<",\"imageReductions\":"<<reductions<<",\"quotientNonzeroCoefficients\":"<<quotientNonzero<<",\"fullVerificationMonomialProducts\":"<<products<<",\"remainderNonzeroCoefficients\":[";
 for(int j=0;j<nt;j++){if(j)meta<<",";meta<<remainderCount[j];}meta<<"],\"maximumRemainderDegrees\":[";for(int j=0;j<nt;j++){if(j)meta<<",";meta<<remainderDegree[j];}meta<<"],\"firstNonzeroCoordinates\":[";for(int j=0;j<nt;j++){if(j)meta<<",";meta<<"["<<first[j][0]<<","<<first[j][1]<<","<<first[j][2]<<"]";}
 meta<<"],\"sourceIdentity\":\"The image basis is the normalized output of the actual complete original T96 graph. The full graph proves each G row lies in im(R), and its distinct-head degree sum716 proves it spans im(R). Every quotient and complete remainder is saved. G*Q+remainder=RHS is accumulated independently in all1034 components and all9 RHS. A nonzero irreducible remainder proves that the actual first residual is not in the full F31[s] R image. It excludes h0*t only from the fixed original217374 integer columns, whose mod31 independence fixes x0. It does not exclude a different initial mod31 kernel part, higher-budget sources, or global characteristic-zero ideal membership.\",\"elapsedSeconds\":"<<elapsed()<<"}\n";
 qout.close();rout.close();meta.close();if(!qout||!rout||!meta)throw std::runtime_error("certificate output failure");struct rusage usage{};getrusage(RUSAGE_SELF,&usage);
 std::cout<<"{\"status\":\"first-residual-complete-image-certificate\",\"fullImageQuotientIdentity\":true,\"everyRemainderIsIrreducible\":true,\"completeRHSInImage\":"<<(allImage?"true":"false")<<",\"fixedOriginalIntegerColumnSpaceLiftObstructed\":"<<(allImage?"false":"true")<<",\"remainderNonzeroCoefficients\":[";for(int j=0;j<nt;j++){if(j)std::cout<<",";std::cout<<remainderCount[j];}std::cout<<"],\"firstNonzeroCoordinates\":[";for(int j=0;j<nt;j++){if(j)std::cout<<",";std::cout<<"["<<first[j][0]<<","<<first[j][1]<<","<<first[j][2]<<"]";}std::cout<<"],\"peakRSSKiB\":"<<usage.ru_maxrss<<",\"elapsedSeconds\":"<<elapsed()<<"}\n";
 return 0;
}catch(const std::exception &e){std::cerr<<"FIRST_RESIDUAL_IMAGE_CERTIFICATE_FAILED "<<e.what()<<"\n";return 1;}}
