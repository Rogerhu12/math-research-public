// Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.
// Runtime original-source transport for complete p²-envelope local pages.
// Fork of 2026-11-14-r150-197-third-local-transport-789f.cpp.
// No mathematical run or compile result is claimed by this source.
// Required common: 3fb7910935f46592c3f22cb3c2c727e8c25fdb0b34e7c8d65d1c558dca6e402c.
#include "2026-11-16-r150-joint-m-local-common50-789f.hpp"
#include <memory>
#include <chrono>
#include <filesystem>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <csignal>
#include <fcntl.h>
#include <unistd.h>
#include <sys/file.h>
namespace cp {
namespace fs=std::filesystem;
constexpr uint64_t MAX_FILE_BYTES=4500000, COMPRESS_AT=1000000;
constexpr size_t CHUNK_WORDS=1000000; // 4,000,000 decoded bytes, RLE worst case <4,500,000.
static volatile std::sig_atomic_t stopRequested=0;
static void requestStop(int){stopRequested=1;}
constexpr const char *VERSION="r150-root2-fourth-local-original-transport-v1-portable-runtime-789f";
class SHA256 {
 std::array<uint32_t,8> h{{0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19}};
 std::array<uint8_t,64> b{}; size_t used=0; uint64_t bytes=0;
 static uint32_t rr(uint32_t x,int n){return(x>>n)|(x<<(32-n));}
 void block(){
  static const uint32_t k[64]={
   0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
   0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
   0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
   0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
   0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
   0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
   0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
   0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2};
  uint32_t w[64];for(int i=0;i<16;i++)w[i]=(uint32_t(b[4*i])<<24)|(uint32_t(b[4*i+1])<<16)|(uint32_t(b[4*i+2])<<8)|b[4*i+3];
  for(int i=16;i<64;i++){uint32_t x=w[i-15],y=w[i-2];w[i]=w[i-16]+(rr(x,7)^rr(x,18)^(x>>3))+w[i-7]+(rr(y,17)^rr(y,19)^(y>>10));}
  uint32_t a=h[0],c=h[1],d=h[2],e=h[3],f=h[4],g=h[5],j=h[6],l=h[7];
  for(int i=0;i<64;i++){uint32_t t1=l+(rr(f,6)^rr(f,11)^rr(f,25))+((f&g)^((~f)&j))+k[i]+w[i];uint32_t t2=(rr(a,2)^rr(a,13)^rr(a,22))+((a&c)^(a&d)^(c&d));l=j;j=g;g=f;f=e+t1;e=d;d=c;c=a;a=t1+t2;}
  h[0]+=a;h[1]+=c;h[2]+=d;h[3]+=e;h[4]+=f;h[5]+=g;h[6]+=j;h[7]+=l;
 }
public:
 void add(const void *v,size_t n){const auto *p=static_cast<const uint8_t*>(v);bytes+=n;while(n){size_t q=std::min(n,64-used);std::memcpy(b.data()+used,p,q);used+=q;p+=q;n-=q;if(used==64){block();used=0;}}}
 std::string finish(){uint64_t bits=bytes*8;uint8_t x=128;add(&x,1);x=0;while(used!=56)add(&x,1);uint8_t len[8];for(int i=0;i<8;i++)len[i]=uint8_t(bits>>(56-8*i));add(len,8);std::ostringstream o;o<<std::hex<<std::setfill('0');for(auto a:h)o<<std::setw(8)<<a;return o.str();}
};
static bool shaOK(const std::string &s){return s.size()==64&&std::all_of(s.begin(),s.end(),[](char c){return(c>='0'&&c<='9')||(c>='a'&&c<='f');});}
static std::string hashText(const std::string &s){SHA256 h;h.add(s.data(),s.size());return h.finish();}
static std::string hashFile(const std::string &p){std::ifstream in(p,std::ios::binary);if(!in)throw std::runtime_error("hash input unavailable: "+p);SHA256 h;std::array<char,65536>b;while(in){in.read(b.data(),b.size());h.add(b.data(),size_t(in.gcount()));}if(!in.eof())throw std::runtime_error("hash input read failure");return h.finish();}
static void digestSelfCheck(){if(hashText("")!="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"||hashText("abc")!="ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")throw std::runtime_error("SHA256 known-vector mismatch");}
static void atomicText(const fs::path &p,const std::string &s){auto t=p;t+=".tmp";{std::ofstream o(t,std::ios::binary|std::ios::trunc);o.write(s.data(),s.size());o.close();if(!o)throw std::runtime_error("atomic text write");}fs::rename(t,p);}
static int traceWidth(std::istream &in,uint64_t count){auto t=sb::tag(in);int width=t=="R150NR31"?1:t=="R150NW31"?2:0;if(!width||sb::get(in,4)!=count)throw std::runtime_error("normal trace magic/dimensions");return width;}
struct State{
 int phase=0,next=0,family=0,sourceCost=-1;uint64_t offset=0,normalOps=0,activeOps=0,rhsOps=0,bops=0,fops=0,generation=0;
};
struct Chunk{int kind=0;uint64_t offset=0,words=0;std::string file,sha;};
static void encode(const fs::path &file,const Row &v){
 std::ofstream o(file,std::ios::binary|std::ios::trunc);o.write("R150CP32",8);sb::put(o,v.size(),8);
 size_t i=0;while(i<v.size()){
  size_t e=i+1;while(e<v.size()&&v[e]==v[i]&&e-i<0x7fffffffu)e++;
  if(e-i>=3){sb::put(o,0x80000000u|uint32_t(e-i),4);sb::put(o,v[i],4);i=e;continue;}
  size_t start=i;i=e;
  while(i<v.size()&&i-start<16384){size_t r=i+1;while(r<v.size()&&v[r]==v[i]&&r-i<3)r++;if(r-i>=3)break;i=std::min(r,start+size_t(16384));}
  sb::put(o,i-start,4);for(size_t k=start;k<i;k++)sb::put(o,v[k],4);
 }
 o.close();if(!o||fs::file_size(file)>MAX_FILE_BYTES)throw std::runtime_error("checkpoint chunk write/size");
}
static Row decode(const fs::path &file,uint64_t n){
 if(n>CHUNK_WORDS||fs::file_size(file)>MAX_FILE_BYTES)throw std::runtime_error("checkpoint decoded/encoded limit");
 std::ifstream in(file,std::ios::binary);if(sb::tag(in)!="R150CP32"||sb::get(in,8)!=n)throw std::runtime_error("checkpoint chunk header");
 Row v;v.reserve(n);while(v.size()<n){uint32_t token=sb::get(in,4);uint64_t count=token&0x7fffffffU;if(!count||count>n-v.size())throw std::runtime_error("checkpoint run bounds");if(token>>31){uint32_t a=sb::get(in,4);v.insert(v.end(),count,a);}else for(uint64_t k=0;k<count;k++)v.push_back(sb::get(in,4));}sb::tail(in);return v;
}
struct Lock{int fd=-1;explicit Lock(const fs::path&p){fd=::open(p.c_str(),O_CREAT|O_RDWR,0600);if(fd<0||::flock(fd,LOCK_EX|LOCK_NB))throw std::runtime_error("checkpoint already in use");}~Lock(){if(fd>=0){::flock(fd,LOCK_UN);::close(fd);}}};

static void validateJetRow(const Row&r,int nt,int length,int stride){
 const int words=(nt+31)/32;
 if(nt<1||nt>256||length<1||length>50||stride!=words*length||r.size()!=size_t(5*stride))throw std::runtime_error("actual jet row dimensions");
 const uint32_t last=nt%32?((uint32_t(1)<<(nt%32))-1):UINT32_MAX;
 for(int d=0;d<stride;d++){
  uint32_t all=UINT32_MAX,nz=0;for(int b=0;b<5;b++){all&=r[b*stride+d];nz|=r[b*stride+d];}
  const uint32_t allowed=d%words==words-1?last:UINT32_MAX;
  if(all||(nz&~allowed))throw std::runtime_error("noncanonical F31 value or Taylor padding");
 }
}

class Checkpoint{
 fs::path dir;std::string binding,runner;int nt,B,PW;std::unique_ptr<Lock> lock;int active=-1;
 void validateRows(const std::vector<Row>&v)const{for(const auto&r:v)validateJetRow(r,nt,B,PW);}
public:
 Checkpoint(const std::string &d,const std::string &b,const std::string &r,int t,int cost,int stride):dir(d),binding(b),runner(r),nt(t),B(cost),PW(stride){
  fs::create_directories(dir);lock=std::make_unique<Lock>(dir/"run.lock");auto p=dir/"binding.txt";
  if(fs::exists(p)){std::ifstream in(p);std::string a,c;std::getline(in,a);std::getline(in,c);if(a!=VERSION||c!=binding)throw std::runtime_error("checkpoint input binding mismatch; choose an empty directory");}
  else{for(auto &e:fs::directory_iterator(dir))if(e.path().filename()!="run.lock")throw std::runtime_error("nonempty unbound checkpoint directory");atomicText(p,std::string(VERSION)+"\n"+binding+"\n"+runner+"\n");}
 }
 bool load(State &s,std::vector<Row>&raw,std::vector<Row>&beta){
  auto pointer=dir/"active.txt";if(!fs::exists(pointer))return false;
  std::ifstream pi(pointer);std::string sha;pi>>active>>sha;if(!pi||active<0||active>1||!shaOK(sha))throw std::runtime_error("checkpoint active pointer");std::string extra;if(pi>>extra)throw std::runtime_error("checkpoint pointer tail");
  auto base=dir/("slot"+std::to_string(active));auto mf=base/"manifest.txt";if(hashFile(mf.string())!=sha)throw std::runtime_error("checkpoint manifest digest");
  std::ifstream in(mf);std::string magic,b,r;std::getline(in,magic);std::getline(in,b);std::getline(in,r);
  int n,c,w;in>>n>>c>>w;if(magic!=VERSION||b!=binding||r!=runner||n!=nt||c!=B||w!=PW)throw std::runtime_error("checkpoint manifest context");
  in>>s.phase>>s.next>>s.family>>s.sourceCost>>s.offset>>s.normalOps>>s.activeOps>>s.rhsOps>>s.bops>>s.fops>>s.generation;
  if(!in||s.phase<1||s.phase>5||s.next<0||s.family<0||s.sourceCost>B)throw std::runtime_error("checkpoint phase");
  size_t nc;in>>nc;if(!in||nc>10000)throw std::runtime_error("checkpoint chunk count");std::array<uint64_t,2>position{{0,0}};
  for(size_t i=0;i<nc;i++){Chunk c;in>>c.kind>>c.offset>>c.words>>c.file>>c.sha;if(!in||c.kind<0||c.kind>1||c.offset!=position[c.kind]||!c.words||c.words>CHUNK_WORDS||c.file.find_first_not_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.")!=std::string::npos||!shaOK(c.sha))throw std::runtime_error("checkpoint chunk dictionary");
   if(c.file!=(c.kind?"beta-":"raw-")+std::to_string(c.offset/CHUNK_WORDS)+".rle32")throw std::runtime_error("checkpoint chunk filename");auto &v=c.kind?beta:raw;uint64_t limit=uint64_t(v.size())*5*PW;if(c.offset+c.words>limit)throw std::runtime_error("checkpoint chunk overflow");auto p=base/c.file;if(hashFile(p.string())!=c.sha)throw std::runtime_error("checkpoint chunk digest");Row decoded=decode(p,c.words);for(uint64_t k=0;k<c.words;k++){uint64_t j=c.offset+k;v[j/(5*PW)][j%(5*PW)]=decoded[k];}position[c.kind]+=c.words;
  }
  if(in>>extra)throw std::runtime_error("checkpoint manifest tail");if(position[0]!=uint64_t(raw.size())*5*PW||position[1]!=uint64_t(beta.size())*5*PW)throw std::runtime_error("checkpoint incomplete arrays");
  validateRows(raw);validateRows(beta);return true;
 }
 void save(State &s,const std::vector<Row>&raw,const std::vector<Row>&beta){
  int slot=active==0?1:0;auto base=dir/("slot"+std::to_string(slot));auto temp=dir/("slot"+std::to_string(slot)+".tmp");if(fs::exists(temp))fs::remove_all(temp);fs::create_directory(temp);
  std::vector<Chunk> cs;
  for(int kind=0;kind<2;kind++){const auto &v=kind?beta:raw;uint64_t total=uint64_t(v.size())*5*PW;
   for(uint64_t off=0;off<total;off+=CHUNK_WORDS){uint64_t n=std::min<uint64_t>(CHUNK_WORDS,total-off);Row part(n);for(uint64_t k=0;k<n;k++){uint64_t j=off+k;part[k]=v[j/(5*PW)][j%(5*PW)];}Chunk c{kind,off,n,(kind?"beta-":"raw-")+std::to_string(off/CHUNK_WORDS)+".rle32",""};encode(temp/c.file,part);c.sha=hashFile((temp/c.file).string());cs.push_back(std::move(c));}
  }
  s.generation++;std::ostringstream m;m<<VERSION<<"\n"<<binding<<"\n"<<runner<<"\n"<<nt<<" "<<B<<" "<<PW<<"\n"<<s.phase<<" "<<s.next<<" "<<s.family<<" "<<s.sourceCost<<" "<<s.offset<<" "<<s.normalOps<<" "<<s.activeOps<<" "<<s.rhsOps<<" "<<s.bops<<" "<<s.fops<<" "<<s.generation<<"\n"<<cs.size()<<"\n";
  for(auto &c:cs)m<<c.kind<<" "<<c.offset<<" "<<c.words<<" "<<c.file<<" "<<c.sha<<"\n";atomicText(temp/"manifest.txt",m.str());std::string sha=hashFile((temp/"manifest.txt").string());
  if(fs::exists(base))fs::remove_all(base);fs::rename(temp,base);atomicText(dir/"active.txt",std::to_string(slot)+" "+sha+"\n");active=slot;
 }
};
static std::string quoted(const std::string &s){std::ostringstream o;o<<'"';for(unsigned char c:s){if(c=='"'||c=='\\')o<<'\\'<<char(c);else if(c<32)o<<"\\u00"<<std::hex<<std::setw(2)<<std::setfill('0')<<int(c)<<std::dec;else o<<char(c);}o<<'"';return o.str();}
} // namespace cp
// Mathematical stages are identical to 8258b730f05698b8bc3c182809fac3f05670b8ed.
// Only target/ring dimensions, semantic binding, and true restart state are generalized.
struct LocalBack {int basis;std::vector<std::pair<uint16_t,uint8_t>>steps;};
struct LocalFront {int raw,scale;std::vector<std::pair<uint16_t,uint8_t>>steps;};

int main(int argc,char**argv){try{
 if(argc!=15){
  std::cerr<<"usage: PROGRAM model oldK200 VQ normal RHS forward backward outPrefix pipelineBinding mode old197TenOrDash spec checkpointDir remainingSeconds\n";return 2;
 }
 auto start=std::chrono::steady_clock::now();
 auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 size_t consumed=0;double budget=std::stod(argv[14],&consumed);
 if(consumed!=std::strlen(argv[14])||!std::isfinite(budget)||budget<=0)throw std::runtime_error("remainingSeconds must be finite and positive");
 const double reserve=std::min(30.0,budget/4.0);
 std::signal(SIGTERM,cp::requestStop);std::signal(SIGINT,cp::requestStop);
 cp::digestSelfCheck();
 const std::string prefix=argv[8],pipeline=argv[9],mode=argv[10];
 const bool first=mode=="q1";
 if(!first&&mode!="q2"&&mode!="q3"&&mode!="q4"&&mode!="q5")throw std::runtime_error("mode must be q1, q2, q3, q4, or q5");
 if(!cp::shaOK(pipeline))throw std::runtime_error("pipeline binding must be lowercase SHA256");
 if(!first&&std::string(argv[11])!="-")throw std::runtime_error("prior197 prefix comparison is a q1-only input");
 sb::Model model(argv[1]);const auto spec=jt::labels(argv[12]);
 const int nt=jt::NT,length=jt::L,stride=jt::S;
 BitOps ops;auto pw=jt::powers(31,256);
 std::vector<jt::KernelLabel>klab;
 std::vector<int>targetAtOld(200,-1);
 if(first){
  klab=jt::kernelLabels(argv[2]);std::map<int,int>oldIndex;
  for(int i=0;i<200;i++)if(!oldIndex.emplace(klab[i].head,i).second)throw std::runtime_error("duplicate old200 head label");
  for(int j=0;j<nt;j++){
   auto it=oldIndex.find(jt::label(spec,j));if(it==oldIndex.end())throw std::runtime_error("q1 target absent from actual old200");
   if(klab[it->second].cost>81)throw std::runtime_error("q1 cost177 scope excludes old cost85 columns");
   targetAtOld[it->second]=j;
  }
 }
 std::vector<std::pair<std::string,std::string>> hashes;
 for(int a:{1,3,4,5,6,7})hashes.push_back({"input-"+std::to_string(a),cp::hashFile(argv[a])});
 if(first)hashes.push_back({"oldK200",cp::hashFile(argv[2])});
 if(std::string(argv[11])!="-")hashes.push_back({"prior197Ten",cp::hashFile(argv[11])});
 std::ostringstream canonical;
 canonical<<"R150_S2_LOCAL_JET_SPEC_V1\n31 "<<nt<<" "<<length<<" "<<spec.ring<<"\n";
 for(int j=0;j<nt;j++)canonical<<jt::label(spec,j)<<"\n";
 hashes.push_back({"semanticSpec",cp::hashText(canonical.str())});
 const std::string specAudit=cp::hashFile(argv[12]);
 std::ostringstream signature;
 signature<<cp::VERSION<<"\ncommonAPI 3fb7910935f46592c3f22cb3c2c727e8c25fdb0b34e7c8d65d1c558dca6e402c\n"<<pipeline<<"\n"<<mode<<"\n"<<nt<<" "<<length<<" "<<stride<<" "<<spec.ring<<"\n";
 for(const auto&h:hashes)signature<<h.first<<" "<<h.second<<"\n";
 const std::string checkpointBinding=cp::hashText(signature.str());
 auto C=jt::readPacked(argv[3],2195,model,spec,pipeline);
 if(C.kind!=1||C.done!=1021||C.bound!=(first?177:0))throw std::runtime_error("complete same-global VQ scope required");
 for(const auto&r:C.rows)cp::validateJetRow(r,nt,length,stride);
 std::vector<Row>raw(6188,Row(5*stride)),beta(3333,Row(5*stride));
 std::vector<bool>occupied(6188);
 for(int i=0;i<2195;i++){
  int r=model.sources[i].raw-1;if(r<0||r>=6188||occupied[r])throw std::runtime_error("actual original source collision");occupied[r]=true;
 }
 for(const auto&s:model.pre){
  int r=s.raw-1;if(r<0||r>=6188||occupied[r])throw std::runtime_error("actual prebasis/source collision");occupied[r]=true;
 }
 if(std::count(occupied.begin(),occupied.end(),true)!=5528)throw std::runtime_error("actual selected5528 sources");
 cp::State st;cp::Checkpoint checkpoint(argv[13],checkpointBinding,pipeline,nt,length,stride);
 bool resumed=checkpoint.load(st,raw,beta);
 if(resumed){
  const int limit=st.phase==1?2204:st.phase==2?(first?200:3333):st.phase==5?0:3333;
  if(st.next>limit||st.family!=0||st.sourceCost!=-1)throw std::runtime_error("actual local checkpoint phase/cursor");
 }else{
  for(int i=0;i<2195;i++)raw[model.sources[i].raw-1]=C.rows[i];
  st.phase=1;st.next=0;st.offset=12;
 }
 const int resumedPhase=st.phase,resumedNext=st.next;
 double savedAt=elapsed();
 auto report=[&](const char*status){
  std::cout<<"{\"status\":"<<cp::quoted(status)<<",\"mode\":"<<cp::quoted(mode)<<",\"targets\":"<<nt<<",\"precision\":"<<length<<",\"ring\":"<<spec.ring<<",\"phase\":"<<st.phase<<",\"nextRecord\":"<<st.next<<",\"generation\":"<<st.generation<<",\"checkpointBindingSHA256\":"<<cp::quoted(checkpointBinding)<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 };
 auto save=[&](){checkpoint.save(st,raw,beta);savedAt=elapsed();report("local-original-transport-checkpoint");};
 auto tick=[&](bool force=false){
  bool stop=cp::stopRequested||elapsed()>=budget-reserve;
  if(force||stop||elapsed()-savedAt>=120)save();
  if(stop)throw std::string("CHECKPOINT_TIMEOUT");
 };
 if(!resumed)tick(true);else{report("local-original-transport-resumed");tick();}
 if(st.phase==1){
  std::ifstream in(argv[4],std::ios::binary);
  if(!in||sb::tag(in)!="R150NR31"||sb::get(in,4)!=2204)throw std::runtime_error("same complete original H trace");
  if(st.offset<12)throw std::runtime_error("normal checkpoint stream offset");
  in.seekg(st.offset);if(!in)throw std::runtime_error("normal checkpoint seek");
  for(int i=st.next;i<2204;i++){
   int r=sb::get(in,4),label=sb::get(in,2),steps=sb::get(in,4);
   if(i<2195?(r!=model.sources[i].raw||label):(r||label!=i-2195+2))throw std::runtime_error("original full source H mapping");
   if(steps<0)throw std::runtime_error("normal trace negative steps");
   std::vector<Triple>shifted;
   if(i<2195){
    Triple base;base[0]=C.rows[i];BitOps::refresh(base,stride,0);shifted.resize(46);
    for(int d=0;d<46;d++){
     shifted[d][0].resize(5*stride);jt::muladd(shifted[d][0],base,pw[d],ops);BitOps::refresh(shifted[d],stride,0);
    }
   }
   for(int k=0;k<steps;k++){
    int b=sb::get(in,2)-1,s=sb::get(in,1),a=sb::get(in,1);
    if(b<0||b>=3333||s>45||a<1||a>30)throw std::runtime_error("actual normal trace step");
    if(i<2195){
     if(s+model.delta(model.pre[b].raw)>model.delta(r))throw std::runtime_error("global prebasis compensation cost");
     auto rep=ops.rep[31-a];BitOps::add(beta[b],stride,0,shifted[s][rep.c],stride,0,stride,rep.rot,rep.neg);st.activeOps++;
    }
    st.normalOps++;
   }
   st.next=i+1;auto pos=in.tellg();if(pos<0)throw std::runtime_error("normal trace stream position");st.offset=uint64_t(pos);tick();
  }
  sb::tail(in);if(st.normalOps!=25305683)throw std::runtime_error("complete original H operation count");
  st.phase=2;st.next=0;st.offset=first?12:uint64_t(24+2*nt);tick(true);
 }
 if(st.phase==2){
  if(first){
   std::ifstream in(argv[5],std::ios::binary);
   if(!in||sb::tag(in)!="R150NR31"||sb::get(in,4)!=200)throw std::runtime_error("complete old200 beta trace");
   if(st.offset<12)throw std::runtime_error("RHS checkpoint stream offset");
   in.seekg(st.offset);if(!in)throw std::runtime_error("RHS checkpoint seek");
   std::vector<jt::Co>sum(3333);
   for(int j=st.next;j<200;j++){
    int r=sb::get(in,4),label=sb::get(in,2),steps=sb::get(in,4);
    if(r||label!=klab[j].head||steps<0)throw std::runtime_error("same original old200 beta labels");
    int target=targetAtOld[j];if(target>=0)std::fill(sum.begin(),sum.end(),jt::Co{});
    for(int k=0;k<steps;k++){
     int b=sb::get(in,2)-1,s=sb::get(in,1),a=sb::get(in,1);
     if(b<0||b>=3333||s>85||a<1||a>30||s+model.delta(model.pre[b].raw)>klab[j].cost)throw std::runtime_error("actual original beta source cost");
     if(target>=0)for(int z=0;z<length;z++)sum[b][z]=(sum[b][z]+a*pw[s][z])%31;
     st.rhsOps++;
    }
    if(target>=0)for(int b=0;b<3333;b++)for(int z=0;z<length;z++){
     int a=sum[b][z];if(a){int bit=z*jt::W*32+target;sb::assign(beta[b],stride,bit,(BitOps::get(beta[b],stride,bit)+a)%31);}
    }
    st.next=j+1;auto pos=in.tellg();if(pos<0)throw std::runtime_error("RHS trace stream position");st.offset=uint64_t(pos);tick();
   }sb::tail(in);
  }else{
   std::ifstream in(argv[5],std::ios::binary);
   if(!in||sb::tag(in)!="R150SN31")throw std::runtime_error("actual runtime local prebasis cochain");
   for(int v:{31,3333,nt,length})if(sb::get(in,4)!=uint64_t(v))throw std::runtime_error("actual runtime cochain dimensions");
   for(int j=0;j<nt;j++)if(sb::get(in,2)!=uint64_t(jt::label(spec,j)))throw std::runtime_error("same actual cochain labels");
   const uint64_t dataStart=24+2*uint64_t(nt),recordBytes=2+20*uint64_t(stride);
   if(st.offset!=dataStart+recordBytes*uint64_t(st.next))throw std::runtime_error("cochain checkpoint row/offset");
   std::vector<bool>seen(3333);Row coefficient(5*stride);
   const int from=st.next;
   for(int z=0;z<3333;z++){
    int b=sb::get(in,2)-1;if(b<0||b>=3333||seen[b])throw std::runtime_error("all3333 actual cochain sources");seen[b]=true;
    in.read(reinterpret_cast<char*>(coefficient.data()),coefficient.size()*4);if(!in)throw std::runtime_error("complete actual cochain array");
    cp::validateJetRow(coefficient,nt,length,stride);
    if(z>=from){
     BitOps::add(beta[b],stride,0,coefficient,stride,0,stride,0,0);st.rhsOps++;
     st.next=z+1;st.offset=dataStart+recordBytes*uint64_t(st.next);tick();
    }
   }sb::tail(in);
   if(st.rhsOps!=3333)throw std::runtime_error("complete cochain actual source count");
  }
  st.phase=3;st.next=0;st.offset=0;tick(true);
 }
 if(st.phase==3){
  jt::Buffer in(argv[7]);in.magic("R150RJ31");
  if(in.get(4)!=3333)throw std::runtime_error("same full backward DAG");
  std::vector<LocalBack>back(3333);std::vector<bool>seen(3333);uint64_t count=0;
  for(auto&r:back){
   r.basis=in.get(2)-1;int n=in.get(4);
   if(r.basis<0||r.basis>=3333||seen[r.basis]||n<0)throw std::runtime_error("backward actual prebasis map");seen[r.basis]=true;r.steps.resize(n);
   for(auto&x:r.steps){x.first=in.get(2);x.second=in.get(1);if(x.first<1||x.first>3333||x.first==r.basis+1||x.second<1||x.second>30)throw std::runtime_error("backward actual step");}
   count+=n;
  }in.tail();if(count!=1010703)throw std::runtime_error("complete backward operation dictionary");
  for(int i=st.next;i<3333;i++){
   const auto&r=back[3332-i];Triple current;current[0]=beta[r.basis];BitOps::refresh(current,stride,0);
   for(auto[b,a]:r.steps){auto rep=ops.rep[31-a];BitOps::add(beta[b-1],stride,0,current[rep.c],stride,0,stride,rep.rot,rep.neg);st.bops++;}
   st.next=i+1;tick();
  }
  if(st.bops!=1010703)throw std::runtime_error("complete backward actual operations");
  st.phase=4;st.next=0;st.offset=0;tick(true);
 }
 if(st.phase==4){
  jt::Buffer in(argv[6]);in.magic("R150PB31");
  if(in.get(4)!=3333)throw std::runtime_error("same full forward DAG");
  std::vector<LocalFront>front(3333);uint64_t count=0;
  for(int i=0;i<3333;i++){
   auto&r=front[i];r.raw=in.get(4);r.scale=in.get(1);int n=in.get(4);
   if(r.raw!=model.pre[i].raw||r.scale<1||r.scale>30||n<0)throw std::runtime_error("same original forward source");r.steps.resize(n);
   for(auto&x:r.steps){x.first=in.get(2);x.second=in.get(1);if(x.first<1||x.first>i||x.second<1||x.second>30)throw std::runtime_error("forward actual step");}count+=n;
  }in.tail();if(count!=782976)throw std::runtime_error("complete forward operation dictionary");
  for(int z=st.next;z<3333;z++){
   int i=3332-z;const auto&r=front[i];Triple current;current[0]=beta[i];ops.multiple(current[0],stride,0,r.scale);BitOps::refresh(current,stride,0);
   BitOps::add(raw[r.raw-1],stride,0,current[0],stride,0,stride,0,0);
   for(auto[b,a]:r.steps){auto rep=ops.rep[31-a];BitOps::add(beta[b-1],stride,0,current[rep.c],stride,0,stride,rep.rot,rep.neg);st.fops++;}
   st.next=z+1;tick();
  }
  if(st.fops!=782976)throw std::runtime_error("complete forward actual operations");
  st.phase=5;st.next=0;st.offset=0;tick(true);
 }
 if(st.phase!=5)throw std::runtime_error("incomplete original local source transport");
 for(int r=0;r<6188;r++){
  cp::validateJetRow(raw[r],nt,length,stride);
  if(!occupied[r])for(auto word:raw[r])if(word)throw std::runtime_error("unselected original row acquired a jet");
 }
 jt::Packed result;result.kind=2;result.done=6188;result.bound=first?177:0;result.rows=raw;
 const bool checkedOld=first&&std::string(argv[11])!="-";
 if(first)jt::compareOldPrefix(argv[11],result,model,spec);
 jt::writePacked(prefix+"-original6188-q-jets.bin",result,model,spec,pipeline);
 std::ostringstream receipt;
 receipt<<"{\"format\":\"r150-saturated-actual-local-original-source-transport-v1\",\"status\":\"completed\",\"mode\":"<<cp::quoted(mode)
 <<",\"targets\":"<<nt<<",\"ring\":"<<spec.ring<<",\"TaylorPrecision\":"<<length
 <<",\"sourceRows\":6188,\"selectedOriginalSources\":5528,\"sameActualVQAndOriginalPrebasisTransport\":true"
 <<",\"oldFirstTenOriginalQJetsCompared\":"<<(checkedOld?"true":"false")
 <<",\"globalSourceCostBound\":"<<result.bound<<",\"globalSourceBoundApplies\":"<<(first?"true":"false")
 <<",\"normalOperations\":"<<st.normalOps<<",\"activeNormalOperations\":"<<st.activeOps<<",\"RHSOperationsRead\":"<<st.rhsOps
 <<",\"backwardOperations\":"<<st.bops<<",\"forwardOperations\":"<<st.fops
 <<",\"resumed\":"<<(resumed?"true":"false")<<",\"resumedStage\":"<<resumedPhase<<",\"resumedNextRecord\":"<<resumedNext
 <<",\"bindingSHA256\":"<<cp::quoted(pipeline)<<",\"checkpointBindingSHA256\":"<<cp::quoted(checkpointBinding)
 <<",\"specAuditSHA256\":"<<cp::quoted(specAudit)<<",\"elapsedSeconds\":"<<elapsed()<<",\"inputByteHashes\":{";
 for(size_t i=0;i<hashes.size();i++){if(i)receipt<<",";receipt<<cp::quoted(hashes[i].first)<<":"<<cp::quoted(hashes[i].second);}
 receipt<<"}}\n";cp::atomicText(prefix+"-transport.json",receipt.str());
 report("runtime-local-original-source-transport-complete");return 0;
}catch(const std::string&e){
 if(e=="CHECKPOINT_TIMEOUT"){std::cout<<"{\"status\":\"checkpointed-time-budget-or-signal\",\"exitCode\":75}\n";return 75;}
 std::cerr<<"R150_SATURATED_LOCAL_SOURCE_TRANSPORT_FAILED "<<e<<"\n";return 1;
}catch(const std::exception&e){std::cerr<<"R150_SATURATED_LOCAL_SOURCE_TRANSPORT_FAILED "<<e.what()<<"\n";return 1;}}
