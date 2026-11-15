// 2026-11-15. Author: ChatGPT (AI), literature_audit.
// Complete original polynomial I_2(A), bounded packed batches; no mathematics is claimed by this source.
// Actual original polynomial source transport, wide trace, restartable bitplanes.
// Fork of 2026-11-14-r150-ninth-first-transport-789f.cpp (2f6efa7911d854c487dc86d5757e441bbbf27ee8).
// No change to ninth-first-common. No mathematical run is implied by this source.
// Usage: PROGRAM completed-source model normal forward backward mix out-prefix
//                checkpoint-dir runner-sha256 remaining-seconds
#include "2026-11-15-r150-global197-i2-common-789f.hpp"
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
constexpr const char *VERSION="r150-global197-i2-original-source-checkpoint-v1-789f";
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
class Checkpoint{
 fs::path dir;std::string binding,runner;int nt,B,PW;std::unique_ptr<Lock> lock;int active=-1;
 void validateRows(const std::vector<Row>&v)const{uint32_t allowed=nt==32?UINT32_MAX:(uint32_t(1)<<nt)-1;for(const auto&r:v){if(r.size()!=size_t(5*PW))throw std::runtime_error("checkpoint row stride");for(int d=0;d<PW;d++){uint32_t all=UINT32_MAX,nz=0;for(int b=0;b<5;b++){all&=r[b*PW+d];nz|=r[b*PW+d];}if(all||(nz&~allowed))throw std::runtime_error("checkpoint noncanonical field/padding");}}}
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
struct SBack {int basis;std::vector<std::pair<uint16_t,uint8_t>> steps;};
struct SFront {int raw,scale;std::vector<std::pair<uint16_t,uint8_t>> steps;};
int main(int argc,char **argv){try{
 if(argc!=11){std::cerr<<"usage: PROGRAM completed-source model normal forward backward mix out-prefix checkpoint-dir runner-sha256 remaining-seconds\n";return 2;}
 cp::digestSelfCheck();std::string runner=argv[9];if(!cp::shaOK(runner))throw std::runtime_error("runner binding must be lowercase SHA256");
 size_t pos=0;double budget=std::stod(argv[10],&pos);if(pos!=std::strlen(argv[10])||!std::isfinite(budget)||budget<=0)throw std::runtime_error("remaining_seconds must be finite and positive");
 std::signal(SIGTERM,cp::requestStop);std::signal(SIGINT,cp::requestStop);const double reserve=std::min(30.0,budget/4.0);
 auto start=std::chrono::steady_clock::now();auto seconds=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};double savedAt=0;
 sb::Model model(argv[2]);sb::Mix mix(argv[6]);const int nt=mix.count,ns=2195,nb=3333,nraw=6188;BitOps ops;
 std::ifstream cin(argv[1],std::ios::binary);if(!cin||sb::tag(cin)!="R150SC31"||sb::get(cin,4)!=2195||sb::get(cin,4)!=uint64_t(nt))throw std::runtime_error("completed original source dimensions");
 int B=sb::get(cin,4),N=sb::get(cin,4),requested=sb::get(cin,4);if(N!=mix.bound||B!=N+96||requested!=N||B>1345||B<136)throw std::runtime_error("proved original source bound");int P=B-10,PW=P+1;
 std::string mixAuditSHA=cp::hashFile(argv[6]);std::vector<std::pair<std::string,std::string>> hashes;for(int a=1;a<=5;a++)hashes.push_back({"input-"+std::to_string(a),cp::hashFile(argv[a])});
 std::ostringstream semantic;semantic<<"R150_CANONICAL_MIX_V1 "<<mix.count<<" "<<mix.bound<<" "<<mix.families.size()<<"\n";for(int x:mix.labels)semantic<<x<<" ";semantic<<"\n";
 for(size_t i=0;i<mix.families.size();i++){const auto &f=mix.families[i];semantic<<f.count<<"\n";for(int x:f.labels)semantic<<x<<" ";semantic<<"\n";for(const auto &row:f.poly)for(const auto &p:row){semantic<<p.size();for(int x:p)semantic<<" "<<x;semantic<<"\n";}hashes.push_back({"family-nf-"+std::to_string(i),cp::hashFile(f.nf)});hashes.push_back({"family-quot-"+std::to_string(i),cp::hashFile(f.quot)});hashes.push_back({"family-rem-"+std::to_string(i),cp::hashFile(f.rem)});hashes.push_back({"family-trace-"+std::to_string(i),cp::hashFile(f.trace)});}
 hashes.push_back({"canonical-mix",cp::hashText(semantic.str())});
 std::ostringstream fingerprint;fingerprint<<cp::VERSION<<"\n"<<runner<<"\n"<<nt<<" "<<B<<" "<<N<<"\n";for(auto &h:hashes)fingerprint<<h.first<<" "<<h.second<<"\n";
 std::string binding=cp::hashText(fingerprint.str());std::vector<Row>raw(nraw,Row(5*PW)),beta(nb,Row(5*PW));cp::State st;cp::Checkpoint checkpoint(argv[8],binding,runner,nt,B,PW);
 bool resumed=checkpoint.load(st,raw,beta);std::vector<bool>occupied(nraw);for(auto&s:model.sources){if(occupied[s.raw-1])throw std::runtime_error("duplicate original source");occupied[s.raw-1]=true;}
 auto report=[&](const char *status){std::cout<<"{\"status\":"<<cp::quoted(status)<<",\"phase\":"<<st.phase<<",\"nextRow\":"<<st.next<<",\"family\":"<<st.family<<",\"generation\":"<<st.generation<<",\"binding\":"<<cp::quoted(binding)<<",\"elapsedSeconds\":"<<seconds()<<"}\n"<<std::flush;};
 auto save=[&](){checkpoint.save(st,raw,beta);savedAt=seconds();report("transport-checkpoint");};
 auto tick=[&](bool force=false){bool stop=cp::stopRequested||seconds()>budget-reserve;if(force||stop||seconds()-savedAt>=120)save();if(stop)throw std::string("CHECKPOINT_TIMEOUT");};
 if(!resumed){
  for(int i=0;i<ns;i++){int index=sb::get(cin,4),r=sb::get(cin,4),delta=sb::get(cin,2);if(index!=i+1||r!=model.sources[i].raw||delta!=model.delta(r))throw std::runtime_error("actual2195 source map");
   for(int j=0;j<nt;j++){int len=sb::get(cin,2),last=0;if(len>B-delta+1)throw std::runtime_error("source degree bound");for(int d=0;d<len;d++){last=sb::get(cin,1);if(last>30)throw std::runtime_error("source field coefficient");BitOps::set(raw[r-1],PW,d*32+j,last);if(last)st.sourceCost=std::max(st.sourceCost,delta+d);}if(len&&!last)throw std::runtime_error("source polynomial trailing zero");}
  }sb::tail(cin);st.phase=1;st.next=0;st.offset=12;save();
 }else report("transport-resumed");
 auto actualDegree=[&](const Row&r){for(int d=P;d>=0;d--){uint32_t nz=0;for(int b=0;b<5;b++)nz|=r[b*PW+d];if(nz){if(nz>>nt)throw std::runtime_error("original transport packed padding");return d;}}return -1;};
 if(st.phase==1){
  std::ifstream in(argv[3],std::ios::binary);int sw=cp::traceWidth(in,2204);if(st.next>2204)throw std::runtime_error("normal resume row");in.seekg(st.offset);if(!in)throw std::runtime_error("normal resume offset");
  for(int i=st.next;i<2204;i++){
   int r=sb::get(in,4),target=sb::get(in,2),steps=sb::get(in,4),d=-1;Triple current;
   if(i<ns){if(r!=model.sources[i].raw||target)throw std::runtime_error("normal source trace dictionary");d=actualDegree(raw[r-1]);if(d>=0){current[0]=raw[r-1];BitOps::refresh(current,PW,0);}}
   else if(r||target!=i-ns+2)throw std::runtime_error("original nine trailing trace labels");
   for(int k=0;k<steps;k++){int b=sb::get(in,2)-1,s=sb::get(in,sw),a=sb::get(in,1);if(b<0||b>=nb||a<1||a>30)throw std::runtime_error("actual source normal operation");if(d>=0){if(d+s>P)throw std::runtime_error("prebasis source compensation degree");auto rep=ops.rep[31-a];BitOps::add(beta[b],PW,s,current[rep.c],PW,0,d+1,rep.rot,rep.neg);st.activeOps++;}st.normalOps++;}
   st.next=i+1;auto at=in.tellg();if(at<0)throw std::runtime_error("normal stream position");st.offset=uint64_t(at);tick();
  }sb::tail(in);if(st.normalOps!=25305683)throw std::runtime_error("complete original normal operation count");st.phase=2;st.family=0;st.next=0;st.offset=12;tick(true);
 }
 if(st.phase==2){
  if(st.family>int(mix.families.size()))throw std::runtime_error("RHS resume family");
  for(int fi=st.family;fi<int(mix.families.size());fi++){
   const auto &f=mix.families[fi];std::ifstream in(f.trace,std::ios::binary);int sw=cp::traceWidth(in,f.count);if(st.next>f.count)throw std::runtime_error("RHS resume row");in.seekg(st.offset);if(!in)throw std::runtime_error("RHS resume offset");
   for(int i=st.next;i<f.count;i++){
    int r=sb::get(in,4),label=sb::get(in,2),steps=sb::get(in,4);if(r||label!=f.labels[i])throw std::runtime_error("actual combined RHS trace label");int length=0;for(auto&p:f.poly[i])length=std::max(length,int(p.size()));Triple multiplier;if(length){multiplier[0].resize(5*length);for(int j=0;j<nt;j++)for(int d=0;d<int(f.poly[i][j].size());d++)BitOps::set(multiplier[0],length,d*32+j,f.poly[i][j][d]);BitOps::refresh(multiplier,length,0);}
    for(int k=0;k<steps;k++){int b=sb::get(in,2)-1,s=sb::get(in,sw),a=sb::get(in,1);if(b<0||b>=nb||a<1||a>30)throw std::runtime_error("actual combined RHS trace coefficient");if(length){if(s+length>PW)throw std::runtime_error("actual RHS trace source cost");auto rep=ops.rep[a];BitOps::add(beta[b],PW,s,multiplier[rep.c],length,0,length,rep.rot,rep.neg);}st.rhsOps++;}
    st.family=fi;st.next=i+1;auto at=in.tellg();if(at<0)throw std::runtime_error("RHS stream position");st.offset=uint64_t(at);tick();
   }sb::tail(in);st.family=fi+1;st.next=0;st.offset=12;tick(true);
  }st.phase=3;st.next=0;st.offset=0;tick(true);
 }
 if(st.phase==3){
  std::ifstream in(argv[5],std::ios::binary);if(sb::tag(in)!="R150RJ31"||sb::get(in,4)!=3333)throw std::runtime_error("backward prebasis dimensions");std::vector<SBack>back(nb);std::vector<bool>seen(nb);
  for(auto&r:back){r.basis=sb::get(in,2)-1;int n=sb::get(in,4);if(r.basis<0||r.basis>=nb||seen[r.basis])throw std::runtime_error("backward actual prebasis map");seen[r.basis]=true;r.steps.resize(n);for(auto&x:r.steps){x.first=sb::get(in,2);x.second=sb::get(in,1);if(x.first<1||x.first>nb||x.first==r.basis+1||x.second<1||x.second>30)throw std::runtime_error("backward operation");}}sb::tail(in);if(st.next>nb)throw std::runtime_error("backward resume row");
  for(int done=st.next;done<nb;done++){auto&r=back[nb-1-done];int d=actualDegree(beta[r.basis]);Triple current;if(d>=0){current[0]=beta[r.basis];BitOps::refresh(current,PW,0);}for(auto[basis,a]:r.steps){if(d>=0){auto rep=ops.rep[31-a];BitOps::add(beta[basis-1],PW,0,current[rep.c],PW,0,d+1,rep.rot,rep.neg);}st.bops++;}st.next=done+1;tick();}
  if(st.bops!=1010703)throw std::runtime_error("complete backward DAG operation count");st.phase=4;st.next=0;tick(true);
 }
 if(st.phase==4){
  std::ifstream in(argv[4],std::ios::binary);if(sb::tag(in)!="R150PB31"||sb::get(in,4)!=3333)throw std::runtime_error("forward prebasis dimensions");std::vector<SFront>front(nb);
  for(int i=0;i<nb;i++){auto&r=front[i];r.raw=sb::get(in,4);r.scale=sb::get(in,1);int n=sb::get(in,4);if(r.raw!=model.pre[i].raw||r.scale<1||r.scale>30)throw std::runtime_error("forward original source map");r.steps.resize(n);for(auto&x:r.steps){x.first=sb::get(in,2);x.second=sb::get(in,1);if(x.first<1||x.first>i||x.second<1||x.second>30)throw std::runtime_error("forward original dependency");}}sb::tail(in);if(st.next>nb)throw std::runtime_error("forward resume row");
  for(int done=st.next;done<nb;done++){int i=nb-1-done;auto&r=front[i];int d=actualDegree(beta[i]);Triple current;if(d>=0){current[0]=beta[i];ops.multiple(current[0],PW,0,r.scale);BitOps::refresh(current,PW,0);BitOps::add(raw[r.raw-1],PW,0,current[0],PW,0,d+1,0,0);}for(auto[basis,a]:r.steps){if(d>=0){auto rep=ops.rep[31-a];BitOps::add(beta[basis-1],PW,0,current[rep.c],PW,0,d+1,rep.rot,rep.neg);}st.fops++;}st.next=done+1;tick();}
  if(st.fops!=782976)throw std::runtime_error("complete forward DAG operation count");st.phase=5;st.next=0;tick(true);
 }
 if(st.phase!=5||st.normalOps!=25305683||st.bops!=1010703||st.fops!=782976)throw std::runtime_error("completed transport phase/counters");
 for(auto&s:model.pre){if(occupied[s.raw-1])throw std::runtime_error("prebasis source overlap");occupied[s.raw-1]=true;}if(std::count(occupied.begin(),occupied.end(),true)!=5528)throw std::runtime_error("complete selected source set");
 std::string prefix=argv[7],output=prefix+"-primitive-source-mod31.bin",temporary=output+".tmp";std::ofstream out(temporary,std::ios::binary|std::ios::trunc);out.write("R150PS31",8);for(int a:{31,31,6188,nt,B})u32(out,a);for(int a:mix.labels)u16(out,a);std::vector<int>costs(nt,-1);uint64_t nonzero=0;int maxdegree=-1,rows=0;
 for(int r=1;r<=nraw;r++){model.rowHeader(out,r);int delta=model.delta(r),rd=-1;for(int j=0;j<nt;j++){int d=P;while(d>=0&&!BitOps::get(raw[r-1],PW,d*32+j))d--;u16(out,d+1);for(int k=0;k<=d;k++){int a=BitOps::get(raw[r-1],PW,k*32+j);u16(out,a);if(a){if(!occupied[r-1]||k+delta>B)throw std::runtime_error("restored original source cost");costs[j]=std::max(costs[j],k+delta);nonzero++;}}rd=std::max(rd,d);}rows+=rd>=0;maxdegree=std::max(maxdegree,rd);}
 out.close();if(!out)throw std::runtime_error("full primitive source output failure");cp::fs::rename(temporary,output);std::string outputSHA=cp::hashFile(output);
 std::ostringstream meta;meta<<"{\"format\":\"r150-actual-prebasis-original-source-transport-v3\",\"status\":\"completed\",\"prime\":31,\"targetCount\":"<<nt<<",\"provedSourceCostBound\":"<<B<<",\"actualNormalSourceMaximumCost\":"<<st.sourceCost<<",\"originalRows\":6188,\"selectedOriginalRows\":5528,\"normalOperations\":"<<st.normalOps<<",\"activeNormalOperations\":"<<st.activeOps<<",\"combinedRHSOperations\":"<<st.rhsOps<<",\"backwardOperations\":"<<st.bops<<",\"forwardOperations\":"<<st.fops<<",\"fullActualPrebasisTransport\":true,\"higherModulusProductVerified\":false,\"nonzeroRawRows\":"<<rows<<",\"nonzeroCoefficients\":"<<nonzero<<",\"maximumCoefficientDegree\":"<<maxdegree<<",\"sourceCosts\":";sb::array(meta,costs);
 meta<<",\"rawMixAuditSHA256\":"<<cp::quoted(mixAuditSHA)<<",\"runnerBinding\":"<<cp::quoted(runner)<<",\"effectiveBinding\":"<<cp::quoted(binding)<<",\"outputSHA256\":"<<cp::quoted(outputSHA)<<",\"outputBytes\":"<<cp::fs::file_size(output)<<",\"checkpointPhase\":5,\"checkpointGeneration\":"<<st.generation<<",\"inputSHA256\":{";
 for(size_t i=0;i<hashes.size();i++){if(i)meta<<",";meta<<cp::quoted(hashes[i].first)<<":"<<cp::quoted(hashes[i].second);}meta<<"},\"elapsedSeconds\":"<<seconds()<<"}\n";cp::atomicText(prefix+"-original-transport.json",meta.str());report("original-source-transport-complete");return 0;
}catch(const std::string&e){if(e=="CHECKPOINT_TIMEOUT"){std::cout<<"{\"status\":\"checkpointed-time-limit\",\"exitCode\":75}\n"<<std::flush;return 75;}std::cerr<<"ORIGINAL_TRANSPORT_FAILED "<<e<<"\n";return 1;
}catch(const std::exception&e){std::cerr<<"ORIGINAL_TRANSPORT_FAILED "<<e.what()<<"\n";return 1;}}
