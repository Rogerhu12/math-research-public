// Full coefficient certificate h31*T = G*Q for all nine original NF targets.
// G is the completed 1021-row polynomial basis. No large GB DAG is expanded.
#define main r150_frozen_normal_form_main
#include "2026-11-14-r150-native-normal-form-789f.cpp"
#undef main
using ByteVector=std::vector<uint8_t>;
static uint32_t qc_u32(std::istream &in){uint32_t a=0;for(int k=0;k<4;k++){int c=in.get();if(c<0)throw std::runtime_error("truncated u32");a|=uint32_t(c)<<(8*k);}return a;}
static uint16_t qc_u16(std::istream &in){int a=in.get(),b=in.get();if(a<0||b<0)throw std::runtime_error("truncated u16");return a|(b<<8);}
static ByteVector qc_bytes(std::istream &in,size_t count){ByteVector data(count);in.read(reinterpret_cast<char*>(data.data()),count);if(!in)throw std::runtime_error("truncated matrix");return data;}
struct QTerm {int component,exponent,coefficient;};
int main(int argc,char **argv){try{
 if(argc!=6)return 2;auto start=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 const int n=820,nt=9,q=1034,r=1021,hd=24,QD=50,RD=58;
 std::ifstream state(argv[1],std::ios::binary),trace(argv[2],std::ios::binary),ssi(argv[3]),hin(argv[4]);if(!state||!trace||!ssi||!hin)throw std::runtime_error("input open");
 char magic[8];state.read(magic,8);if(std::string(magic,8)!="R150FW31")throw std::runtime_error("state magic");
 std::vector<int> dims;for(int i=0;i<8;i++)dims.push_back(qc_u32(state));if(dims!=std::vector<int>{q,8,n,13,315,9,505,57})throw std::runtime_error("state dimensions");
 state.seekg(3*n+2*13,std::ios::cur);auto A=qc_bytes(state,n*n),C=qc_bytes(state,13*n),Tstate=qc_bytes(state,nt*n);
 std::vector<int> h(hd+1);for(auto &a:h){hin>>a;if(a<0||a>30)throw std::runtime_error("noncanonical h");}int extra;if(!hin||hin>>extra||h[hd]!=1)throw std::runtime_error("h degree");
 std::vector<uint8_t> z(size_t(hd)*n*nt);for(int row=0;row<n;row++)for(int j=0;j<nt;j++)z[((hd-1)*n+row)*nt+j]=Tstate[j*n+row];
 auto action=[&](int degree,std::vector<uint32_t> &sum){std::fill(sum.begin(),sum.end(),0);for(int row=0;row<n;row++)for(int k=0;k<n;k++){int a=A[row*n+k];if(a)for(int j=0;j<nt;j++)sum[row*nt+j]+=a*z[(degree*n+k)*nt+j];}};
 std::vector<uint32_t> sums(n*nt);
 for(int degree=hd-1;degree>=0;degree--){
  for(int row=0;row<13;row++)for(int j=0;j<nt;j++){uint32_t sum=0;for(int k=0;k<n;k++)sum+=C[row*n+k]*z[(degree*n+k)*nt+j];if(sum%31)throw std::runtime_error("Horner state has leakage");}
  action(degree,sums);
  for(int row=0;row<n;row++)for(int j=0;j<nt;j++){int value=(sums[row*nt+j]+h[degree]*Tstate[j*n+row])%31;if(degree)z[((degree-1)*n+row)*nt+j]=value;else if(value)throw std::runtime_error("h does not kill all full states");}
 }
 std::vector<uint32_t> coefficientSums(size_t(r)*nt*(QD+1));
 trace.read(magic,8);if(std::string(magic,8)!="R150FWOP"||qc_u32(trace)!=q||qc_u32(trace)!=n||qc_u32(trace)!=nt)throw std::runtime_error("trace header");uint64_t operations=0;
 for(int index=0;index<n+nt;index++){
  int kind=trace.get(),number=qc_u16(trace),count=qc_u32(trace);bool isTarget=index>=n;
  if(kind!=(isTarget?'T':'A')||number!=(isTarget?index-n+1:index+1))throw std::runtime_error("trace source identity");
  for(int step=0;step<count;step++){
   int b=qc_u16(trace)-1,shift=trace.get(),a=trace.get();if(b<0||b>=r||shift<0||a<1||a>30)throw std::runtime_error("trace operation");
   if(isTarget){int j=index-n;if(shift+hd>QD)throw std::runtime_error("target coefficient degree bound");for(int k=0;k<=hd;k++)coefficientSums[(b*nt+j)*(QD+1)+shift+k]+=a*h[k];}
   else{if(shift+hd-1>QD)throw std::runtime_error("state coefficient degree bound");for(int k=0;k<hd;k++)for(int j=0;j<nt;j++)coefficientSums[(b*nt+j)*(QD+1)+shift+k]+=a*z[(k*n+index)*nt+j];}
  }operations+=count;
 }
 if(trace.get()!=EOF)throw std::runtime_error("trailing trace");
 ByteVector coefficients(coefficientSums.size());for(size_t i=0;i<coefficients.size();i++)coefficients[i]=coefficientSums[i]%31;coefficientSums.clear();coefficientSums.shrink_to_fit();
 std::vector<int> degrees(r*nt,-1);int maximum=-1;uint64_t nonzero=0;for(int b=0;b<r;b++)for(int j=0;j<nt;j++)for(int k=0;k<=QD;k++)if(coefficients[(b*nt+j)*(QD+1)+k]){degrees[b*nt+j]=k;maximum=std::max(maximum,k);nonzero++;}
 std::cout<<"{\"phase\":\"gb-coefficients-built\",\"maximumDegree\":"<<maximum<<",\"nonzeroCoefficients\":"<<nonzero<<",\"sourceOperations\":"<<operations<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;

 // Check the entire polynomial identity against the saved original G and T.
 std::string head1,head2;std::getline(ssi,head1);std::getline(ssi,head2);int tag,rows,cols;ssi>>tag>>rows>>cols;if(tag!=10||rows!=q||cols!=r)throw std::runtime_error("basis SSI dimensions");
 std::vector<int> components(r),basisDegrees(r);std::vector<uint32_t> product(size_t(q)*(RD+1)*nt);
 auto readTerms=[&](){int count;ssi>>count;if(count<0||count>q*46)throw std::runtime_error("term count");std::vector<QTerm> terms(count);int pd=46,pc=-1;for(auto &e:terms){ssi>>e.coefficient>>e.component>>e.exponent;e.component--;if(!ssi||e.coefficient<1||e.coefficient>30||e.component<0||e.component>=q||e.exponent<0||e.exponent>45||e.exponent>pd||(e.exponent==pd&&e.component<=pc))throw std::runtime_error("SSI exact order");pd=e.exponent;pc=e.component;}return terms;};
 for(int b=0;b<r;b++){
  auto terms=readTerms();if(terms.empty()||terms[0].coefficient!=1||terms[0].exponent>8)throw std::runtime_error("monic completed GB");components[b]=terms[0].component;basisDegrees[b]=terms[0].exponent;
  for(auto e:terms)for(int k=0;k<=maximum;k++)for(int j=0;j<nt;j++)product[(e.component*(RD+1)+e.exponent+k)*nt+j]+=e.coefficient*coefficients[(b*nt+j)*(QD+1)+k];
 }
 ssi>>tag>>rows>>cols;if(tag!=10||rows!=q||cols!=nt)throw std::runtime_error("original target SSI dimensions");
 for(int j=0;j<nt;j++)for(auto e:readTerms())for(int k=0;k<=hd;k++){if(e.exponent+k>RD)throw std::runtime_error("target degree bound");auto &v=product[(e.component*(RD+1)+e.exponent+k)*nt+j];v=(v+31-(e.coefficient*h[k])%31)%31;}
 for(auto a:product)if(a%31)throw std::runtime_error("full polynomial GQ=hT identity failed");std::string trailing;if(ssi>>trailing)throw std::runtime_error("trailing SSI");
 std::ofstream out(std::string(argv[5])+"-gb-coefficients.bin",std::ios::binary),meta(std::string(argv[5])+"-gb-coefficients.json");if(!out||!meta)throw std::runtime_error("output open");
 out.write("R150GQ31",8);u32(out,r);u32(out,nt);u32(out,hd);for(int a:h)out.put(char(a));
 for(int b=0;b<r;b++){u16(out,components[b]+1);out.put(char(basisDegrees[b]));for(int j=0;j<nt;j++){int len=degrees[b*nt+j]+1;u16(out,len);out.write(reinterpret_cast<const char*>(coefficients.data()+(b*nt+j)*(QD+1)),len);}}
 meta<<"{\"format\":\"r150-nine-target-gb-coefficients-v1\",\"field\":31,\"basisRows\":1021,\"targets\":[2,3,4,5,6,7,8,9,10],\"commonAnnihilatorDegree\":24,\"maximumCoefficientDegree\":"<<maximum<<",\"nonzeroCoefficients\":"<<nonzero<<",\"normalOperationsReplayed\":"<<operations<<",\"fullPolynomialIdentity\":true,\"sourceIdentity\":\"For the original saved 1034-component target matrix T and complete monic GB G, G*Q=h31*T coefficientwise. Q=h31*u+H*z, where (s-A)z=h31*v and C*z=0.\"}\n";
 out.close();meta.close();if(!out||!meta)throw std::runtime_error("output failure");std::cout<<"{\"status\":\"all-nine-gb-coefficients-complete\",\"maximumCoefficientDegree\":"<<maximum<<",\"nonzeroCoefficients\":"<<nonzero<<",\"fullPolynomialIdentity\":true,\"elapsedSeconds\":"<<elapsed()<<"}\n";
 return 0;
}catch(const std::exception &e){std::cerr<<"TARGET_GB_COEFFICIENTS_FAILED "<<e.what()<<"\n";return 1;}}
