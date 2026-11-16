// Independent ordinary-scalar verifier for the full original weight10 matrix.
// Author: Astra-ISP-789f / literature_audit, with /root. 2026-11-16.
// AI-assisted: GPT-6 Astra Pro.
// No bit-plane header, elimination implementation or source-DAG code is used.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
#include <fcntl.h>
#include <sys/resource.h>
#include <unistd.h>
namespace fs=std::filesystem;
using Clock=std::chrono::steady_clock;
static constexpr uint32_t M=77276,N=13808,G=200;
static constexpr uint64_t NT=8037189,TT=2604,IB=73145375;
static constexpr std::array<int,10> RW={0,2,2,2,2,2,4,4,4,4};
static constexpr std::array<int,12> VW={1,1,1,1,1,1,2,2,2,2,2,2};
static const char* FORMAT="r150-original-weight10-full-ordinary-verifier127-v1";
struct Budget:std::runtime_error{using std::runtime_error::runtime_error;};
static void require(bool v,const std::string&s){if(!v)throw std::runtime_error(s);}
static std::string bytes(std::istream&f,size_t n){
 std::string b(n,'\0');f.read(b.data(),n);require(size_t(f.gcount())==n,"complete independent fixed field");return b;
}
static uint64_t integer(std::istream&f,int n){
 uint64_t r=0;for(int k=0;k<n;k++){int c=f.get();require(c>=0,"complete independent integer");r|=uint64_t(c)<<(8*k);}return r;
}
static void put(std::ostream&f,uint64_t x,int n){for(int k=0;k<n;k++)f.put(char(x>>(8*k)));}
static uint64_t unpack(const char*p,int n){uint64_t x=0;for(int k=0;k<n;k++)x|=uint64_t(uint8_t(p[k]))<<(8*k);return x;}
static bool sha(const std::string&s){return s.size()==64&&s.find_first_not_of("0123456789abcdef")==std::string::npos;}
static std::string quoted(const std::string&s){
 std::ostringstream z;z<<'"';
 for(unsigned char c:s){if(c=='"'||c=='\\')z<<'\\'<<char(c);else if(c=='\n')z<<"\\n";else if(c=='\r')z<<"\\r";
  else if(c<32)z<<"\\u"<<std::hex<<std::setw(4)<<std::setfill('0')<<unsigned(c)<<std::dec;else z<<char(c);}
 z<<'"';return z.str();
}
static void finish(std::ofstream&f,const fs::path&tmp,const fs::path&p){
 f.flush();require(bool(f),"complete independent output");f.close();
 int fd=open(tmp.c_str(),O_RDONLY);require(fd>=0,"independent fsync open");int rc=fsync(fd);close(fd);require(rc==0,"independent fsync");
 require(!fs::exists(p),"new independent generation never overwrites a complete file");fs::rename(tmp,p);
 int dd=open(p.parent_path().c_str(),O_RDONLY|O_DIRECTORY);if(dd>=0){rc=fsync(dd);close(dd);require(rc==0,"independent directory fsync");}
}
static std::string filename(const std::string&s,uint32_t g,const std::string&e){
 std::ostringstream o;o<<s<<'-'<<std::setw(4)<<std::setfill('0')<<g<<e;return o.str();
}
static int weight(uint64_t k){
 require((k>>60)==0,"all independent twelve lanes");int z=0;
 for(int j=0;j<12;j++){int e=(k>>(5*j))&31;require(e<=10,"independent exponent bound");z+=VW[j]*e;}return z;
}
static uint64_t multiply_code(uint64_t original,uint64_t multiplier){
 uint64_t out=original&15;require(out<10,"independent original component");
 for(int j=0;j<12;j++){
  int e=((original>>(4+5*j))&31)+((multiplier>>(5*j))&31);
  require(e<=10,"independent lane-by-lane multiplication without exponent carry");
  out|=uint64_t(e)<<(4+5*j);
 }return out;
}
static std::array<std::vector<uint64_t>,11> dictionaries(){
 // Iterative product of twelve finite geometric series, independent of the
 // producer's recursive monomial enumeration.
 std::array<std::vector<uint64_t>,11> a;a[0].push_back(0);
 for(int j=0;j<12;j++){
  std::array<std::vector<uint64_t>,11> next;
  for(int w=0;w<=10;w++)for(uint64_t old:a[w])for(int e=0;w+VW[j]*e<=10;e++)
   next[w+VW[j]*e].push_back(old|(uint64_t(e)<<(5*j)));
  a=std::move(next);
 }
 const std::array<size_t,11> expected={1,6,27,92,273,714,1715,3816,8007,15938,30381};
 for(int w=0;w<=10;w++){
  std::sort(a[w].begin(),a[w].end());
  require(a[w].size()==expected[w]&&std::adjacent_find(a[w].begin(),a[w].end())==a[w].end(),"independent full weighted dictionary count");
  for(uint64_t e:a[w])require(weight(e)==w,"independent full monomial weight");
 }return a;
}
struct Term{uint64_t key;uint8_t coefficient;};
struct Original{
 std::ifstream f;std::string binding;std::array<std::vector<uint64_t>,11> mono;
 std::vector<uint64_t> rows,count;std::vector<uint32_t> weights;
 std::unordered_map<uint64_t,uint32_t> position;uint64_t readTerms=0;
 explicit Original(const fs::path&p):f(p,std::ios::binary),mono(dictionaries()){
  require(bool(f)&&fs::file_size(p)==IB,"complete independently bounded original input");
  require(bytes(f,8)=="R15WM101","literal original sparse protocol");
  require(integer(f,4)==1&&integer(f,4)==127&&integer(f,4)==M&&integer(f,4)==N&&integer(f,4)==G&&integer(f,4)==10,"every original fixed dimension");
  require(integer(f,8)==NT&&integer(f,8)==TT,"all original coefficient counts");binding=bytes(f,64);require(sha(binding),"original binding");
  for(int w:RW)require(integer(f,1)==uint64_t(w),"all ten output shifts");
  for(int w:VW)require(integer(f,1)==uint64_t(w),"all twelve original parameter weights");
  rows.reserve(M);position.reserve(2*M);
  for(uint32_t row=0;row<10;row++)for(uint64_t mon:mono[10-RW[row]]){
   uint64_t key=(mon<<4)|row;require(integer(f,8)==key,"independent entire row dictionary in original order");
   require(position.emplace(key,rows.size()).second,"distinct complete output coordinate");rows.push_back(key);
  }require(rows.size()==M,"all77276 independent output coordinates");
  std::vector<std::pair<uint32_t,uint64_t>> labels(N);
  for(auto&l:labels){l.first=integer(f,4);l.second=integer(f,8);}
  weights.resize(G);count.resize(G);std::array<uint32_t,11> profile{};uint64_t total=0;
  for(uint32_t g=0;g<G;g++){
   require(integer(f,4)==g,"every original source label retained");weights[g]=integer(f,4);count[g]=integer(f,8);
   require(weights[g]>=5&&weights[g]<=10&&count[g]<=M,"complete source degree and bounded coefficients");
   profile[weights[g]]++;total+=count[g];
  }
  require(profile[5]==6&&profile[6]==20&&profile[7]==30&&profile[8]==40&&profile[9]==24&&profile[10]==80&&total==NT,"complete Gamma200 input profile");
  uint32_t j=0;
  for(uint32_t g=0;g<G;g++)for(uint64_t mon:mono[10-weights[g]]){
   require(j<N&&labels[j].first==g&&labels[j].second==mon,"independent every13808 multiplied source label");j++;
  }
  require(j==N&&uint64_t(f.tellg())==112+22+8ull*M+12ull*N+16ull*G,"whole independent dictionary/header EOF");
 }
 std::vector<Term> terms(uint64_t n,int w){
  auto raw=bytes(f,n*9);std::vector<Term> a;a.reserve(n);uint64_t previous=0;bool first=true;
  for(uint64_t j=0;j<n;j++){
   uint64_t key=unpack(raw.data()+9*j,8);uint8_t c=uint8_t(raw[9*j+8]);uint32_t row=key&15;
   require(row<10&&c>0&&c<127&&(first||key>previous)&&weight(key>>4)+RW[row]==w,"independent complete canonical source coefficient");
   first=false;previous=key;a.push_back({key,c});
  }return a;
 }
};
struct Certificate{
 uint32_t kind,rank,q0;std::string binding,inputSHA;
 std::vector<uint32_t> pivots;std::vector<uint8_t> value;uint32_t support=0;
 Certificate(const fs::path&p,const std::string&b,const std::string&ih){
  std::ifstream f(p,std::ios::binary);require(bool(f),"open full original certificate");
  require(bytes(f,8)=="R15WC101"&&integer(f,4)==1&&integer(f,4)==127&&integer(f,4)==M&&integer(f,4)==N,"same full certificate protocol");
  kind=integer(f,4);rank=integer(f,4);require(integer(f,4)==N,"certificate after every original column");
  q0=integer(f,4);uint32_t readout=integer(f,4),n=integer(f,4);
  binding=bytes(f,64);inputSHA=bytes(f,64);
  require(binding==b&&inputSHA==ih&&rank<=N,"same whole original binding/input");
  require((kind==1&&q0<M&&readout==1&&n==M)||(kind==2&&q0==UINT32_MAX&&readout==0&&n==N),"full independent certificate type and dimensions");
  pivots.resize(rank);uint32_t prev=0;std::vector<uint8_t> allowed(M,0);
  for(uint32_t k=0;k<rank;k++){
   pivots[k]=integer(f,4);require(pivots[k]<M&&(k==0||pivots[k]>prev),"literal distinct sorted original pivot coordinates");
   prev=pivots[k];allowed[pivots[k]]=1;
  }
  auto raw=bytes(f,n);value.assign(raw.begin(),raw.end());
  require(f.peek()==EOF&&fs::file_size(p)==176+4ull*rank+n,"entire independent certificate EOF");
  if(kind==1){require(!allowed[q0],"separating coordinate outside all pivots");allowed[q0]=1;require(value[q0]!=0,"nonzero original separating coordinate");}
  for(uint32_t i=0;i<n;i++){require(value[i]<127,"all certificate entries canonical");if(value[i]){support++;if(kind==1)require(allowed[i],"left support only pivot rows plus the original separating row");}}
 }
};
struct Progress{
 uint32_t next=0;uint64_t products=0;std::vector<uint64_t> accum;
 explicit Progress(uint32_t kind){if(kind==2)accum.assign(M,0);}
};
static uint64_t progress_size(const Progress&p){return 244+8ull*p.accum.size();}
static void save_progress(const fs::path&p,const Progress&s,const Certificate&c,const std::string&cs){
 auto tmp=p;tmp+=".tmp";std::ofstream f(tmp,std::ios::binary);require(bool(f),"independent whole-column progress stream");f.write("R15WV101",8);
 for(uint32_t x:{1u,127u,M,N,c.kind,c.rank,s.next,c.q0})put(f,x,4);
 f.write(c.binding.data(),64);f.write(c.inputSHA.data(),64);f.write(cs.data(),64);put(f,s.products,8);put(f,s.accum.size(),4);
 for(uint64_t x:s.accum)put(f,x,8);finish(f,tmp,p);require(fs::file_size(p)==progress_size(s),"whole independent progress EOF");
}
static void load_progress(const fs::path&p,Progress&s,const Certificate&c,const std::string&cs){
 std::ifstream f(p,std::ios::binary);require(bool(f),"open independently verified progress");
 require(bytes(f,8)=="R15WV101"&&integer(f,4)==1&&integer(f,4)==127&&integer(f,4)==M&&integer(f,4)==N&&integer(f,4)==c.kind&&integer(f,4)==c.rank,"same independent progress protocol");
 s.next=integer(f,4);require(s.next<=N&&integer(f,4)==c.q0,"whole independent column cursor");
 require(bytes(f,64)==c.binding&&bytes(f,64)==c.inputSHA&&bytes(f,64)==cs,"all exact independent progress identities");
 s.products=integer(f,8);require(s.products<=uint64_t(N)*M&&integer(f,4)==s.accum.size(),"bounded complete independent products and accumulator");
 for(auto&x:s.accum){x=integer(f,8);require(x<=uint64_t(N)*126*126,"ordinary complete product accumulator bound");}
 require(f.peek()==EOF&&fs::file_size(p)==progress_size(s),"whole independent progress payload EOF");
}
static void tick(const Clock::time_point&d){if(Clock::now()>=d)throw Budget("complete ordinary-column budget");}
static uint64_t controls(){
 auto d=dictionaries();uint64_t checks=0;
 for(int a=0;a<127;a++)for(int b=0;b<127;b++){
  uint64_t z=uint64_t(a)*b;require(z%127==uint64_t((a*b)%127),"independent ordinary field product");checks++;
 }
 for(int row=0;row<10;row++)for(uint64_t e:d[10-RW[row]]){
  require(multiply_code((e<<4)|row,0)==((e<<4)|row),"all literal full output encodings");checks++;
 }
 std::vector<std::vector<int>> a={
  {0,0,1,4,0,0,2},{1,0,2,0,3,0,1},{2,0,5,4,6,0,4},
  {0,1,0,4,5,2,1},{0,0,0,0,0,0,0},{0,0,0,0,1,2,0},{0,1,3,16,6,4,7}};
 const std::array<int,7> c={1,0,0,3,0,5,0};
 for(int i=0;i<7;i++){uint64_t z=0;for(int j=0;j<7;j++)z+=uint64_t(c[j])*a[j][i];
  require(z%127==uint64_t((a[0][i]+3*a[3][i]+5*a[5][i])%127),"independent source product control");checks++;}
 return checks;
}
int main(int argc,char**argv){
 auto begun=Clock::now();fs::path out;uint32_t generation=0,initial=0,complete=0,kind=0,rank=0,support=0;
 uint64_t products=0,checks=0,readTerms=0;bool allInput=false,completeProof=false,stateWritten=false;
 std::string binding,ih,ch,stateFile,error,status="failed";int code=1;
 try{
  if(argc==2&&std::string(argv[1])=="--selftest"){
   checks=controls();std::cout<<"{\"format\":\""<<FORMAT<<"-selftest\",\"allComplete\":true,\"ordinaryChecks\":"<<checks<<"}"<<std::endl;return 0;
  }
  require(argc==9,"input certificate out seconds inputSHA certificateSHA generation verified-progress-or-dash");
  fs::path input=argv[1],cert=argv[2];out=argv[3];double seconds=std::stod(argv[4]);ih=argv[5];ch=argv[6];generation=std::stoul(argv[7]);std::string prior=argv[8];
  require(seconds>=30&&seconds<=1800&&sha(ih)&&sha(ch)&&generation>0&&generation<10000,"bounded independent verification and all identities");
  fs::create_directories(out);auto deadline=begun+std::chrono::duration_cast<Clock::duration>(std::chrono::duration<double>(seconds-8));
  Original original(input);binding=original.binding;Certificate certificate(cert,binding,ih);kind=certificate.kind;rank=certificate.rank;support=certificate.support;
  Progress p(kind);if(prior!="-")load_progress(prior,p,certificate,ch);initial=p.next;complete=initial;products=p.products;bool paused=false;
  try{
   uint32_t column=0;
   for(uint32_t g=0;g<G;g++){
    auto terms=original.terms(original.count[g],original.weights[g]);readTerms+=terms.size();
    for(uint64_t mon:original.mono[10-original.weights[g]]){
     require(column<N,"independent source multiplier index");
     if(column<p.next){column++;continue;}
     require(column==p.next,"only complete consecutive original verification columns");tick(deadline);
     uint64_t sum=0;std::vector<std::pair<uint32_t,uint32_t>> updates;if(kind==2)updates.reserve(terms.size());
     for(size_t k=0;k<terms.size();k++){
      if((k&16383)==0)tick(deadline);
      const auto&t=terms[k];uint64_t key=multiply_code(t.key,mon);auto pos=original.position.find(key);
      require(pos!=original.position.end(),"every original multiplied coefficient in full77276 dictionary");
      if(kind==1)sum+=uint64_t(certificate.value[pos->second])*t.coefficient;
      else updates.emplace_back(pos->second,uint32_t(certificate.value[column])*t.coefficient);
     }
     if(kind==1)require(sum%127==0,"left witness annihilates this complete original multiplied column");
     else for(const auto&z:updates)p.accum[z.first]+=z.second;
     p.products+=terms.size();p.next++;column++;
    }
   }
   require(column==N&&p.next==N&&readTerms==NT,"all13808 original products and every200 coefficient frame");
   auto target=original.terms(TT,10);require(original.f.peek()==EOF,"independent full sparse EOF");std::vector<uint8_t> dense(M,0);
   for(const auto&t:target){
    require((t.key&15)==0,"literal original e0 target");auto z=original.position.find(t.key);
    require(z!=original.position.end(),"all original target coordinates");dense[z->second]=t.coefficient;
   }allInput=true;
   if(kind==1){
    uint64_t value=0;for(uint32_t j=0;j<M;j++)value+=uint64_t(certificate.value[j])*dense[j];
    require(value%127==1,"normalized nonzero readout on full literal original target");
   }else for(uint32_t j=0;j<M;j++)require(p.accum[j]%127==dense[j],"all77276 ordinary original source products equal target");
   completeProof=true;
  }catch(const Budget&){paused=true;}
  complete=p.next;products=p.products;
  if(p.next>initial){stateFile=filename("ordinary-column-state",generation,".bin");save_progress(out/stateFile,p,certificate,ch);stateWritten=true;}
  code=completeProof?0:75;status=completeProof?"completed-full-original-products":"budget-checkpoint";
  require(completeProof||paused,"independent status requires actual completion or budget stop");
 }catch(const std::exception&e){error=e.what();code=1;status="failed";}
 struct rusage ru{};getrusage(RUSAGE_SELF,&ru);std::ostringstream r;r<<std::setprecision(17);
 r<<"{\"format\":"<<quoted(FORMAT)<<",\"binding\":"<<quoted(binding)<<",\"inputSHA256\":"<<quoted(ih)<<",\"certificateSHA256\":"<<quoted(ch)
  <<",\"status\":"<<quoted(status)<<",\"exitCode\":"<<code<<",\"generation\":"<<generation<<",\"certificateKind\":"<<kind
  <<",\"initialVerifiedColumns\":"<<initial<<",\"verifiedOriginalColumns\":"<<complete<<",\"newVerifiedColumns\":"<<(complete>=initial?complete-initial:0)
  <<",\"literalScalarProducts\":"<<products<<",\"originalTermsReadThisAttempt\":"<<readTerms
  <<",\"allOriginalDictionariesAndCoefficientsVerified\":"<<(allInput?"true":"false")
  <<",\"all13808OriginalColumnProductsVerified\":"<<(completeProof?"true":"false")
  <<",\"all77276TargetCoordinatesVerified\":"<<(completeProof?"true":"false")
  <<",\"certificateSupport\":"<<support<<",\"observedNativePivotCount\":"<<rank
  <<",\"stateWritten\":"<<(stateWritten?"true":"false")<<",\"stateFile\":"<<quoted(stateFile)
  <<",\"leftOriginalTargetReadout\":"<<((completeProof&&kind==1)?1:0)
  <<",\"positiveOriginalSourceClaimed\":false,\"originalIdealNonmembershipClaimed\":false"
  <<",\"elapsedSeconds\":"<<std::chrono::duration<double>(Clock::now()-begun).count()<<",\"peakRssKiB\":"<<ru.ru_maxrss<<",\"error\":"<<quoted(error)<<"}";
 if(!out.empty()&&generation){
  try{auto p=out/filename("ordinary-verifier-receipt",generation,".json"),tmp=p;tmp+=".tmp";std::ofstream f(tmp);f<<r.str();finish(f,tmp,p);}
  catch(const std::exception&e){std::cerr<<"independent receipt persistence: "<<e.what()<<std::endl;return 1;}
 }
 std::cout<<r.str()<<std::endl;return code;
}
