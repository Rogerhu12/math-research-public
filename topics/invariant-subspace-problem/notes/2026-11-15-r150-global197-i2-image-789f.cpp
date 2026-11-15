// 2026-11-15. Author: ChatGPT (AI), literature_audit.
// Complete original polynomial I_2(A), bounded packed batches; no mathematics is claimed by this source.
// Same complete original image G and exact monic V pairing, finite RHS<=1249.
// Reuse the saved original G quotients; reduce only the combined old remainders.
// Independently multiply the complete G*Q+remainder identity in every component.
#include "2026-11-15-r150-global197-i2-common-789f.hpp"
int main(int argc,char **argv){try{
 if(argc!=4)return 2;auto start=std::chrono::steady_clock::now();auto seconds=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 sb::Mix mix(argv[2]);BitOps ops;auto piv=sb::graphImage(argv[1],ops);const int nt=mix.count,N=mix.bound,W=33,nw=(N+1)*W,q=1034;
 std::vector<Row> target(nt,Row(5*nw)),remainder(nt,Row(5*nw)),quotient(nt,Row(5*nw));uint64_t seedCoefficients=0;
 auto addNF=[&](std::vector<Row> &destination,const sb::NF &nf,const sb::MixFamily &f,bool mustBeIrreducible){
  if(nf.count!=f.count||nf.labels!=f.labels)throw std::runtime_error("frozen RHS mixture labels");
  std::vector<int> bounds(f.count,-1),strides(f.count);std::vector<Row> packed(f.count);
  for(int i=0;i<f.count;i++){for(const auto &p:nf.rows[i])bounds[i]=std::max(bounds[i],int(p.size())-1);strides[i]=(bounds[i]+1)*W;packed[i].resize(5*strides[i]);}
  for(int i=0;i<f.count;i++)for(int c=0;c<q;c++)for(int d=0;d<int(nf.rows[i][c].size());d++){int a=nf.rows[i][c][d];if(a&&mustBeIrreducible&&piv[c]&&d>=piv[c]->degree)throw std::runtime_error("old remainder not reduced");BitOps::set(packed[i],strides[i],d*W*32+c,a);}
  for(int i=0;i<f.count;i++)for(int j=0;j<nt;j++)for(int s=0;s<int(f.poly[i][j].size());s++)if(int a=f.poly[i][j][s]){if(bounds[i]<0)continue;if(bounds[i]+s>N)throw std::runtime_error("mixture actual degree exceeds declared bound");sb::scalar(ops,destination[j],nw,s*W,packed[i],strides[i],0,strides[i],a);}
 };
 for(const auto &f:mix.families){
  auto original=sb::readNF(f.nf);addNF(target,original,f,false);
  if(f.quot=="-"){if(f.rem!="-")throw std::runtime_error("unpaired fresh NF");addNF(remainder,original,f,false);continue;}
  auto oldrem=sb::readNF(f.rem);addNF(remainder,oldrem,f,true);
  std::ifstream in(f.quot,std::ios::binary);if(sb::tag(in)!="R150IQ31"||sb::get(in,4)!=1034||sb::get(in,4)!=1021||sb::get(in,4)!=uint64_t(f.count))throw std::runtime_error("saved complete image quotient dimensions");int bound=sb::get(in,4),previous=0;
  for(int row=0;row<1021;row++){int c=sb::get(in,2),d=sb::get(in,1),lc=sb::get(in,1);if(c<=previous||c>q||!piv[c-1]||piv[c-1]->degree!=d||piv[c-1]->originalLC!=lc)throw std::runtime_error("saved quotient actual G dictionary");previous=c;
   for(int i=0;i<f.count;i++){int length=sb::get(in,2);if(length>bound-d+1)throw std::runtime_error("saved quotient degree");int last=0;for(int k=0;k<length;k++){last=sb::get(in,1);if(last>30)throw std::runtime_error("saved quotient field");if(!last)continue;seedCoefficients++;for(int j=0;j<nt;j++)for(int s=0;s<int(f.poly[i][j].size());s++)if(int a=f.poly[i][j][s]){if(k+s+d>N)throw std::runtime_error("seed quotient degree increased");int bit=(k+s)*W*32+c-1;sb::assign(quotient[j],nw,bit,(BitOps::get(quotient[j],nw,bit)+a*last)%31);}}if(length&&!last)throw std::runtime_error("saved quotient trailing zero");}
  }sb::tail(in);
 }
 uint64_t reductions=0;std::vector<int> remainderCount(nt),maximum(nt,-1);
 for(int j=0;j<nt;j++){
  for(int d=N;d>=0;d--)for(int c=0;c<q;c++)if(piv[c]&&d>=piv[c]->degree){int a=BitOps::get(remainder[j],nw,d*W*32+c);if(!a)continue;auto &p=*piv[c];int s=d-p.degree;sb::scalar(ops,remainder[j],nw,s*W,p.row,p.stride,0,p.stride,31-a);int bit=s*W*32+c;sb::assign(quotient[j],nw,bit,(BitOps::get(quotient[j],nw,bit)+a)%31);reductions++;}
  for(int c=0;c<q;c++)for(int d=0;d<=N;d++)if(int a=BitOps::get(remainder[j],nw,d*W*32+c)){if(piv[c]&&d>=piv[c]->degree)throw std::runtime_error("retained reducible remainder");remainderCount[j]++;maximum[j]=std::max(maximum[j],d);}
  std::cout<<"{\"phase\":\"old-quotient-mixture-image\",\"label\":"<<mix.labels[j]<<",\"additionalReductions\":"<<reductions<<",\"remainderNonzero\":"<<remainderCount[j]<<",\"elapsedSeconds\":"<<seconds()<<"}\n"<<std::flush;
 }
 int pw=q*(N+1);Row product(5*pw);for(int j=0;j<nt;j++)for(int c=0;c<q;c++)for(int d=0;d<=N;d++)BitOps::set(product,pw,(c*(N+1)+d)*32+j,sb::mod(BitOps::get(remainder[j],nw,d*W*32+c)-BitOps::get(target[j],nw,d*W*32+c)));
 std::string prefix=argv[3];std::ofstream qo(prefix+"-image-quotients.bin",std::ios::binary);qo.write("R150IQ31",8);for(int a:{q,1021,nt,N})u32(qo,a);uint64_t products=0,qcount=0;
 for(int c=0;c<q;c++)if(piv[c]){
  const auto &p=*piv[c];int bound=N-p.degree,stride=bound+1;Triple packed;packed[0].resize(5*stride);u16(qo,c+1);qo.put(char(p.degree));qo.put(char(p.originalLC));
  for(int j=0;j<nt;j++){std::vector<uint8_t> cp(stride);for(int d=0;d<=bound;d++){int a=BitOps::get(quotient[j],nw,d*W*32+c);cp[d]=a;if(a){BitOps::set(packed[0],stride,d*32+j,a);qcount++;}}while(!cp.empty()&&!cp.back())cp.pop_back();u16(qo,cp.size());qo.write(reinterpret_cast<const char*>(cp.data()),cp.size());}BitOps::refresh(packed,stride,0);
  for(int k=0;k<=p.degree;k++)for(int out=0;out<q;out++)if(int a=BitOps::get(p.row,p.stride,k*W*32+out)){auto r=ops.rep[a];BitOps::add(product,pw,out*(N+1)+k,packed[r.c],stride,0,stride,r.rot,r.neg);products++;}
 }
 for(auto a:product)if(a)throw std::runtime_error("full combined original GQ+remainder identity failed");qo.close();if(!qo)throw std::runtime_error("quotient write failed");
 sb::writeNF(prefix+"-normal-forms.bin",target,mix.labels,N);sb::writeNF(prefix+"-image-remainders.bin",remainder,mix.labels,N);
 bool all=std::all_of(remainderCount.begin(),remainderCount.end(),[](int a){return a==0;});std::ofstream meta(prefix+"-image-certificate.json");
 meta<<"{\"format\":\"r150-actual-saved-quotient-mixture-v1\",\"status\":\"completed\",\"targets\":"<<nt<<",\"originalRightHandSideCostBound\":"<<N<<",\"fullImageQuotientIdentity\":true,\"everyRemainderIsIrreducible\":true,\"completeRHSInImage\":"<<(all?"true":"false")<<",\"allOldQuotientsReused\":true,\"oldQuotientNonzeroCoefficientsRead\":"<<seedCoefficients<<",\"additionalImageReductions\":"<<reductions<<",\"quotientNonzeroCoefficients\":"<<qcount<<",\"verificationMonomialProducts\":"<<products<<",\"labels\":";sb::array(meta,mix.labels);meta<<",\"remainderNonzeroCoefficients\":";sb::array(meta,remainderCount);meta<<",\"maximumRemainderDegrees\":";sb::array(meta,maximum);meta<<",\"originalSeventeenEquationSourceRestored\":false,\"elapsedSeconds\":"<<seconds()<<"}\n";meta.close();if(!meta)throw std::runtime_error("image metadata failure");
 std::cout<<"{\"status\":\"saved-quotient-mixture-complete\",\"fullImageQuotientIdentity\":true,\"completeRHSInImage\":"<<(all?"true":"false")<<",\"targets\":"<<nt<<",\"elapsedSeconds\":"<<seconds()<<"}\n";return 0;
}catch(const std::exception &e){std::cerr<<"SECOND_BOCKSTEIN_IMAGE_FAILED "<<e.what()<<"\n";return 1;}}
