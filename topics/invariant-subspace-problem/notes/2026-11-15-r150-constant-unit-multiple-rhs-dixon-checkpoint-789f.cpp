// Astra-ISP-789f / literature_audit + normal_annihilator; AI-assisted, GPT-6 Astra Pro.
// Independent constant-unit, multiple-RHS fork; exact sparse rational-RHS Dixon.
// 1 <= n <= 5000, 1 <= m <= 40. Every complete digit is retained.
// Input/checkpoint/inverse/solution magic and receipt format are distinct from Q7.
// The wrapper binds this protocol/version, all input bytes, row/source labels and scales.
// Only the square unit equations diag(g) A' Z = E are verified here.
// Recover x = diag(h)^(-1) Z and verify all original source/cochain equations externally.
// No unused dense CRT copies of the integer matrix are allocated.
#include <gmp.h>
#include <flint/flint.h>
#include <flint/fmpz.h>
#include <flint/fmpz_mat.h>
#include <flint/fmpq.h>
#include <flint/fmpq_mat.h>
#include <flint/nmod_mat.h>
#include <flint/ulong_extras.h>
#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <csignal>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
#include <unistd.h>
namespace fs=std::filesystem;
using Clock=std::chrono::steady_clock;
static volatile sig_atomic_t stopped=0;
static void sigstop(int){stopped=1;}
struct BudgetExpired:std::runtime_error {using std::runtime_error::runtime_error;};
static void need(bool b,const std::string&s){if(!b)throw std::runtime_error(s);}
static std::string esc(const std::string&s){std::string t;for(char c:s){if(c=='"'||c=='\\'){t+='\\';t+=c;}else if(c=='\n')t+="\\n";else if(static_cast<unsigned char>(c)>=32)t+=c;}return t;}
struct SHA {
 uint32_t h[8]={0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19};
 unsigned char buf[64];size_t used=0;uint64_t bytes=0;
 static uint32_t ro(uint32_t x,int n){return (x>>n)|(x<<(32-n));}
 void block(const unsigned char*b){
  static const uint32_t k[64]={0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2};
  uint32_t w[64];for(int i=0;i<16;i++)w[i]=(uint32_t(b[4*i])<<24)|(uint32_t(b[4*i+1])<<16)|(uint32_t(b[4*i+2])<<8)|b[4*i+3];
  for(int i=16;i<64;i++){uint32_t a=ro(w[i-15],7)^ro(w[i-15],18)^(w[i-15]>>3),c=ro(w[i-2],17)^ro(w[i-2],19)^(w[i-2]>>10);w[i]=w[i-16]+a+w[i-7]+c;}
  uint32_t a=h[0],b0=h[1],c=h[2],d=h[3],e=h[4],f=h[5],g=h[6],v=h[7];
  for(int i=0;i<64;i++){uint32_t s1=ro(e,6)^ro(e,11)^ro(e,25),ch=(e&f)^(~e&g),t1=v+s1+ch+k[i]+w[i],s0=ro(a,2)^ro(a,13)^ro(a,22),maj=(a&b0)^(a&c)^(b0&c),t2=s0+maj;v=g;g=f;f=e;e=d+t1;d=c;c=b0;b0=a;a=t1+t2;}
  h[0]+=a;h[1]+=b0;h[2]+=c;h[3]+=d;h[4]+=e;h[5]+=f;h[6]+=g;h[7]+=v;
 }
 void add(const void*p,size_t n){const auto*b=(const unsigned char*)p;bytes+=n;while(n){size_t z=std::min(n,64-used);memcpy(buf+used,b,z);used+=z;b+=z;n-=z;if(used==64){block(buf);used=0;}}}
 std::string finish(){uint64_t bits=bytes*8;unsigned char x=0x80;add(&x,1);x=0;while(used!=56)add(&x,1);unsigned char q[8];for(int i=0;i<8;i++)q[7-i]=(bits>>(8*i))&255;add(q,8);std::ostringstream s;s<<std::hex<<std::setfill('0');for(auto v:h)s<<std::setw(8)<<v;return s.str();}
};
struct Z {
 fmpz_t v;
 Z(){fmpz_init(v);}~Z(){fmpz_clear(v);}
 Z(Z&&o)noexcept{fmpz_init(v);fmpz_swap(v,o.v);}
 Z&operator=(Z&&o)noexcept{fmpz_swap(v,o.v);return *this;}
 Z(const Z&)=delete;Z&operator=(const Z&)=delete;
};
struct Writer {
 FILE*f;SHA sh;uint64_t count=0;mpz_t tmp;std::vector<unsigned char>b;
 explicit Writer(const fs::path&p){f=fopen(p.c_str(),"wb");need(f,"open writer");mpz_init(tmp);}
 ~Writer(){if(f)fclose(f);mpz_clear(tmp);}
 void raw(const void*p,size_t n){need(fwrite(p,1,n,f)==n,"write complete bytes");sh.add(p,n);count+=n;}
 void u32(uint32_t v){unsigned char q[4];for(int i=0;i<4;i++)q[i]=(v>>(8*i))&255;raw(q,4);}
 void z(const fmpz_t v){int sg=fmpz_sgn(v);if(!sg){u32(0);return;}fmpz_get_mpz(tmp,v);size_t n=(mpz_sizeinbase(tmp,2)+7)/8;b.resize(n);size_t actual=0;mpz_export(b.data(),&actual,1,1,1,0,tmp);need(actual<0x7fffffff,"bounded integer record");u32(sg<0?uint32_t(-int32_t(actual)):uint32_t(actual));raw(b.data(),actual);}
 std::pair<uint64_t,std::string> close(){need(fflush(f)==0,"flush");need(fsync(fileno(f))==0,"fsync");need(fclose(f)==0,"close");f=nullptr;return {count,sh.finish()};}
};
struct Reader {
 FILE*f;SHA sh;uint64_t count=0;mpz_t tmp;std::vector<unsigned char>b;
 explicit Reader(const fs::path&p){f=fopen(p.c_str(),"rb");need(f,"open reader");mpz_init(tmp);}
 ~Reader(){fclose(f);mpz_clear(tmp);}
 void raw(void*p,size_t n){need(fread(p,1,n,f)==n,"complete input bytes");sh.add(p,n);count+=n;}
 uint32_t u32(){unsigned char q[4];raw(q,4);return uint32_t(q[0])|(uint32_t(q[1])<<8)|(uint32_t(q[2])<<16)|(uint32_t(q[3])<<24);}
 void z(fmpz_t v){int32_t k=int32_t(u32());need(k!=INT32_MIN,"integer length");if(!k){fmpz_zero(v);return;}uint32_t n=k<0?-int64_t(k):k;need(n<100000000,"bounded integer bytes");b.resize(n);raw(b.data(),n);mpz_import(tmp,n,1,1,1,0,b.data());if(k<0)mpz_neg(tmp,tmp);fmpz_set_mpz(v,tmp);}
 std::pair<uint64_t,std::string> finish(){need(fgetc(f)==EOF,"no unbound trailing data");return {count,sh.finish()};}
};
struct Term {uint32_t c=0;Z a;};
struct Row {uint32_t original=0;Z g;std::vector<Term>terms;};
struct Input {
 uint32_t n=0,m=0;std::string binding,sha;uint64_t bytes=0;std::vector<Row>rows;std::vector<Z>h;std::vector<uint32_t>source;
 fmpz_mat_t E;
 explicit Input(const fs::path&p,const std::string&bound){
  Reader r(p);char magic[8];r.raw(magic,8);need(std::string(magic,8)==std::string("R15CUM01",8),"native input magic");
  need(r.u32()==1,"native input version");n=r.u32();m=r.u32();uint32_t nz=r.u32();
  need(n>0&&n<=5000&&m>=1&&m<=40,"constant-unit dimensions: 1<=n<=5000, 1<=targets<=40");char bs[64];r.raw(bs,64);binding=std::string(bs,64);need(binding==bound,"native input binding");
  source.resize(n);h.resize(n);rows.resize(n);fmpz_mat_init(E,n,m);
  for(uint32_t j=0;j<n;j++){source[j]=r.u32();r.z(h[j].v);need(fmpz_sgn(h[j].v)>0,"positive source scale");}
  uint64_t count=0;
  for(uint32_t i=0;i<n;i++){
   auto&rw=rows[i];rw.original=r.u32();r.z(rw.g.v);need(fmpz_sgn(rw.g.v)>0,"positive row scale");
   for(uint32_t j=0;j<m;j++)r.z(fmpz_mat_entry(E,i,j));
   uint32_t k=r.u32();need(k>0&&k<=n,"nonzero square row");rw.terms.resize(k);uint32_t last=0;
   for(uint32_t t=0;t<k;t++){auto&v=rw.terms[t];v.c=r.u32();need(v.c<n&&(!t||last<v.c),"ordered actual source positions");last=v.c;r.z(v.a.v);need(!fmpz_is_zero(v.a.v),"nonzero coefficient");}
   count+=k;
  }
  need(count==nz,"complete nnz count");auto x=r.finish();bytes=x.first;sha=x.second;
 }
 ~Input(){fmpz_mat_clear(E);}
};
static void atomic_text(const fs::path&p,const std::string&s){auto t=p;t+=".tmp";{std::ofstream f(t);need(bool(f),"text temp");f<<s;f.flush();need(bool(f),"complete text");}fs::rename(t,p);}
struct Meta {int slot=0;uint32_t digits=0,p=0;uint64_t bytes=0;std::string hash;};
static Meta read_meta(const fs::path&p,const std::string&b){std::ifstream f(p);std::string magic,b0;Meta m;f>>magic>>b0>>m.slot>>m.digits>>m.p>>m.bytes>>m.hash;need(bool(f)&&magic=="R150CUMMETA1"&&b0==b&&m.hash.size()==64,"complete portable checkpoint manifest");return m;}
static void write_meta(const fs::path&p,const std::string&b,const Meta&m){std::ostringstream s;s<<"R150CUMMETA1\n"<<b<<"\n"<<m.slot<<" "<<m.digits<<" "<<m.p<<" "<<m.bytes<<" "<<m.hash<<"\n";atomic_text(p,s.str());}
struct Solver {
 Input&A;fs::path out;Clock::time_point start;double seconds;std::string binding;
 uint32_t p=0,digits=0,startdigits=0,attempts=0,nextrec=1;int activeSlot=-1;bool haveInv=false,haveState=false,solved=false;
 fmpz_mat_t X,N,Nnext,Num;fmpz_t power; nmod_mat_t inv,dm,ym;
 std::vector<ulong>ginv;std::string inverseHash,checkpointHash,solutionHash;uint64_t inverseBytes=0,checkpointBytes=0,solutionBytes=0;
 Z sum,tmp,checkval;std::vector<Z>D;
 Solver(Input&a,const fs::path&o,double s):A(a),out(o),start(Clock::now()),seconds(s),binding(a.binding),D(a.m){
  fs::create_directories(out);fmpz_mat_init(X,A.n,A.m);fmpz_mat_init_set(N,A.E);fmpz_mat_init(Nnext,A.n,A.m);fmpz_mat_init(Num,A.n,A.m);fmpz_init(power);fmpz_one(power);
 }
 ~Solver(){if(haveInv){nmod_mat_clear(inv);nmod_mat_clear(dm);nmod_mat_clear(ym);}fmpz_mat_clear(X);fmpz_mat_clear(N);fmpz_mat_clear(Nnext);fmpz_mat_clear(Num);fmpz_clear(power);}
 double elapsed()const{return std::chrono::duration<double>(Clock::now()-start).count();}
 bool timeup()const{return stopped||elapsed()>=seconds-std::min(15.0,seconds/8.0);}
 std::string receipt(const std::string&status,const std::string&phase,const std::string&err=""){
  std::ostringstream s;s<<"{\"format\":\"isp-constant-unit-multiple-rhs-dixon-native-v1\",\"status\":\""<<esc(status)<<"\",\"phase\":\""<<esc(phase)
   <<"\",\"binding\":\""<<binding<<"\",\"unitSize\":"<<A.n<<",\"targets\":"<<A.m<<",\"internalPrime\":"<<p
   <<",\"completedDigits\":"<<digits<<",\"resumedFromDigits\":"<<startdigits<<",\"precisionBits\":"<<fmpz_bits(power)
   <<",\"allCompletedDigitIntegerDivisionsVerified\":true,\"unitSolutionExactVerified\":"<<(solved?"true":"false")
   <<",\"verificationScope\":\"square-unit-only\",\"protocolVersion\":1,\"allOriginalUnitRowsVerified\":"<<(solved?"true":"false")
   <<",\"originalUnitProductCoordinates\":"<<(solved?uint64_t(A.n)*A.m:0)
   <<",\"allOriginalSourceEquationsVerified\":false,\"fullOriginal4367VerificationComplete\":false,\"reconstructionAttempts\":"<<attempts
   <<",\"nativeElapsedSeconds\":"<<std::setprecision(17)<<elapsed()<<",\"parameters\":{\"runtimeFlintVersion\":\""<<esc(flint_version)
   <<"\",\"headerFlintVersion\":\""<<esc(FLINT_VERSION)<<"\",\"inputBytes\":"<<A.bytes<<",\"inputSHA256\":\""<<A.sha
   <<"\",\"inverseBytes\":"<<inverseBytes<<",\"inverseSHA256\":\""<<inverseHash
   <<"\",\"checkpointBytes\":"<<checkpointBytes<<",\"checkpointSHA256\":\""<<checkpointHash
   <<"\",\"activeCheckpointSlot\":"<<activeSlot<<",\"solutionBytes\":"<<solutionBytes<<",\"solutionSHA256\":\""<<solutionHash<<"\"}";
  if(!err.empty())s<<",\"error\":\""<<esc(err)<<"\"";s<<"}";
  atomic_text(out/"constant-unit-dixon-native-receipt.json",s.str());return s.str();
 }
 void initmods(uint32_t prime){
  p=prime;nmod_mat_init(inv,A.n,A.n,p);nmod_mat_init(dm,A.n,A.m,p);nmod_mat_init(ym,A.n,A.m,p);haveInv=true;ginv.resize(A.n);
  for(uint32_t i=0;i<A.n;i++){ulong x=fmpz_fdiv_ui(A.rows[i].g.v,p);need(x!=0,"internal prime avoids row denominator");ginv[i]=n_invmod(x,p);need(fmpz_fdiv_ui(A.h[i].v,p)!=0,"internal prime avoids source scale");}
 }
 void inverse(){
  auto mf=out/"inverse-meta.txt",bf=out/"inverse.bin";
  if(fs::exists(mf)){
   auto m=read_meta(mf,binding);initmods(m.p);Reader r(bf);char magic[8],b[64];r.raw(magic,8);r.raw(b,64);
   need(std::string(magic,8)==std::string("R15CUINV",8)&&std::string(b,64)==binding&&r.u32()==A.n&&r.u32()==p,"inverse shape/binding");
   for(uint32_t i=0;i<A.n;i++)for(uint32_t j=0;j<A.n;j++){uint32_t v=r.u32();need(v<p,"inverse canonical field");nmod_mat_entry(inv,i,j)=v;}
   auto x=r.finish();need(x.first==m.bytes&&x.second==m.hash,"inverse actual SHA");inverseBytes=x.first;inverseHash=x.second;
   return;
  }
  uint32_t candidate=1U<<29;bool ok=false;
  for(int trial=0;trial<32;trial++){
   if(timeup())throw BudgetExpired("time before internal inverse");candidate=uint32_t(n_nextprime(candidate,1));
   bool good=true;for(uint32_t i=0;i<A.n;i++)if(!fmpz_fdiv_ui(A.rows[i].g.v,candidate)||!fmpz_fdiv_ui(A.h[i].v,candidate)){good=false;break;}
   if(!good)continue;
   initmods(candidate);nmod_mat_t am;nmod_mat_init(am,A.n,A.n,p);
   for(uint32_t i=0;i<A.n;i++)for(auto&t:A.rows[i].terms)nmod_mat_entry(am,i,t.c)=fmpz_fdiv_ui(t.a.v,p);
   ok=nmod_mat_inv(inv,am);nmod_mat_clear(am);
   if(ok)break;
   nmod_mat_clear(inv);nmod_mat_clear(dm);nmod_mat_clear(ym);haveInv=false;
  }
  need(ok,"bounded internal prime search did not obtain a unit");
  auto t=bf;t+=".tmp";Writer w(t);w.raw("R15CUINV",8);w.raw(binding.data(),64);w.u32(A.n);w.u32(p);
  for(uint32_t i=0;i<A.n;i++)for(uint32_t j=0;j<A.n;j++)w.u32(nmod_mat_entry(inv,i,j));
  auto x=w.close();fs::rename(t,bf);inverseBytes=x.first;inverseHash=x.second;Meta m;m.p=p;m.bytes=x.first;m.hash=x.second;write_meta(mf,binding,m);
 }
 void checkpoint(){
  int slot=activeSlot<0?0:1-activeSlot;fs::path file=out/("checkpoint-"+std::to_string(slot)+".bin"),t=file;t+=".tmp";
  Writer w(t);w.raw("R15CUST1",8);w.raw(binding.data(),64);w.u32(A.n);w.u32(A.m);w.u32(p);w.u32(digits);w.u32(nextrec);w.u32(attempts);w.z(power);
  for(uint32_t i=0;i<A.n;i++)for(uint32_t j=0;j<A.m;j++)w.z(fmpz_mat_entry(X,i,j));
  for(uint32_t i=0;i<A.n;i++)for(uint32_t j=0;j<A.m;j++)w.z(fmpz_mat_entry(N,i,j));
  auto z=w.close();fs::rename(t,file);Meta m;m.slot=slot;m.digits=digits;m.p=p;m.bytes=z.first;m.hash=z.second;
  write_meta(out/"checkpoint-active.txt",binding,m);activeSlot=slot;checkpointBytes=z.first;checkpointHash=z.second;haveState=true;
 }
 void restore(){
  auto f=out/"checkpoint-active.txt";if(!fs::exists(f)){checkpoint();return;}
  auto m=read_meta(f,binding);need(m.slot==0||m.slot==1,"two checkpoint slots");need(m.p==p,"same internal prime");
  Reader r(out/("checkpoint-"+std::to_string(m.slot)+".bin"));char magic[8],b[64];r.raw(magic,8);r.raw(b,64);
  need(std::string(magic,8)=="R15CUST1"&&std::string(b,64)==binding&&r.u32()==A.n&&r.u32()==A.m&&r.u32()==p,"checkpoint original input binding");
  digits=r.u32();nextrec=r.u32();attempts=r.u32();need(digits==m.digits,"checkpoint exact digit cursor");r.z(power);
  for(uint32_t i=0;i<A.n;i++)for(uint32_t j=0;j<A.m;j++)r.z(fmpz_mat_entry(X,i,j));
  for(uint32_t i=0;i<A.n;i++)for(uint32_t j=0;j<A.m;j++)r.z(fmpz_mat_entry(N,i,j));
  auto z=r.finish();need(z.first==m.bytes&&z.second==m.hash,"checkpoint actual full bytes SHA");
  fmpz_ui_pow_ui(tmp.v,p,digits);need(fmpz_equal(tmp.v,power),"checkpoint exact p power");
  for(uint32_t i=0;i<A.n;i++)for(uint32_t j=0;j<A.m;j++)need(fmpz_sgn(fmpz_mat_entry(X,i,j))>=0&&fmpz_cmp(fmpz_mat_entry(X,i,j),power)<0,"canonical full source residues");
  activeSlot=m.slot;checkpointBytes=m.bytes;checkpointHash=m.hash;startdigits=digits;haveState=true;
 }
 void digit(){
  for(uint32_t i=0;i<A.n;i++)for(uint32_t j=0;j<A.m;j++){
   ulong v=fmpz_fdiv_ui(fmpz_mat_entry(N,i,j),p);
   nmod_mat_entry(dm,i,j)=ulong((uint64_t(v)*ginv[i])%p);
  }
  nmod_mat_mul(ym,inv,dm);
  // Build an entirely new residual. The old X,N remain a complete state.
  for(uint32_t i=0;i<A.n;i++)for(uint32_t j=0;j<A.m;j++){
   fmpz_zero(sum.v);for(auto&t:A.rows[i].terms)fmpz_addmul_ui(sum.v,t.a.v,nmod_mat_entry(ym,t.c,j));
   fmpz_mul(sum.v,sum.v,A.rows[i].g.v);fmpz_sub(fmpz_mat_entry(Nnext,i,j),fmpz_mat_entry(N,i,j),sum.v);
   ulong rem=fmpz_fdiv_ui(fmpz_mat_entry(Nnext,i,j),p);
   need(rem==0,"actual digit division failed at original output "+std::to_string(A.rows[i].original)+" target "+std::to_string(j));
   fmpz_divexact_ui(fmpz_mat_entry(Nnext,i,j),fmpz_mat_entry(Nnext,i,j),p);
  }
  for(uint32_t i=0;i<A.n;i++)for(uint32_t j=0;j<A.m;j++)fmpz_addmul_ui(fmpz_mat_entry(X,i,j),power,nmod_mat_entry(ym,i,j));
  fmpz_mat_swap(N,Nnext);fmpz_mul_ui(power,power,p);digits++;checkpoint();
 }
 bool reconstruct(){
  attempts++;nextrec=std::max(digits+1,uint32_t((uint64_t(digits)*3)/2));checkpoint();
  fmpq_mat_t q;fmpq_mat_init(q,A.n,A.m);
  bool ok=fmpq_mat_set_fmpz_mat_mod_fmpz(q,X,power);
  if(ok){
   for(uint32_t j=0;j<A.m;j++){
    fmpz_one(D[j].v);
    for(uint32_t i=0;i<A.n;i++)fmpz_lcm(D[j].v,D[j].v,fmpq_denref(fmpq_mat_entry(q,i,j)));
    for(uint32_t i=0;i<A.n;i++){fmpz_divexact(tmp.v,D[j].v,fmpq_denref(fmpq_mat_entry(q,i,j)));fmpz_mul(fmpz_mat_entry(Num,i,j),tmp.v,fmpq_numref(fmpq_mat_entry(q,i,j)));}
   }
   for(uint32_t i=0;i<A.n&&ok;i++){
    if(timeup()){ok=false;break;}
    for(uint32_t j=0;j<A.m;j++){
     fmpz_zero(sum.v);for(auto&t:A.rows[i].terms)fmpz_addmul(sum.v,t.a.v,fmpz_mat_entry(Num,t.c,j));
     fmpz_mul(sum.v,sum.v,A.rows[i].g.v);fmpz_mul(tmp.v,D[j].v,fmpz_mat_entry(A.E,i,j));
     if(!fmpz_equal(sum.v,tmp.v)){ok=false;break;}
    }
   }
  }
  fmpq_mat_clear(q);
  if(!ok)return false;
  auto file=out/"active-unit-rational-solution.bin",t=file;t+=".tmp";Writer w(t);
  w.raw("R15CUSL1",8);w.raw(binding.data(),64);w.u32(A.n);w.u32(A.m);w.u32(p);w.u32(digits);
  for(uint32_t j=0;j<A.m;j++)w.z(D[j].v);
  for(uint32_t i=0;i<A.n;i++)for(uint32_t j=0;j<A.m;j++)w.z(fmpz_mat_entry(Num,i,j));
  auto z=w.close();fs::rename(t,file);solutionBytes=z.first;solutionHash=z.second;solved=true;return true;
 }
};
int main(int argc,char**argv){
 if(argc!=6){std::cerr<<"usage: native input.bin output-directory binding remaining-seconds maximum-digits\n";return 1;}
 std::signal(SIGTERM,sigstop);std::signal(SIGINT,sigstop);
 fs::path out=argv[2];fs::create_directories(out);auto allstart=Clock::now();
 try{
  std::string binding=argv[3];need(binding.size()==64,"64 byte input binding");double budget=std::stod(argv[4]);uint32_t maxdigits=std::stoul(argv[5]);
  need(std::isfinite(budget)&&budget>0&&budget<=7200&&maxdigits>0&&maxdigits<=100000,"explicit bounded native budget");
  Input a(argv[1],binding);double consumed=std::chrono::duration<double>(Clock::now()-allstart).count();
  need(consumed<budget,"input decoding exhausted native budget");Solver s(a,out,budget-consumed);
  try{
   s.inverse();s.restore();s.receipt("running","exact-digits");
   while(s.digits<maxdigits&&!s.timeup()){
    s.digit();
    if(s.digits>=s.nextrec&&s.reconstruct()){std::cout<<s.receipt("completed","constant-unit-multiple-rhs-rational-solution-complete")<<"\n";return 0;}
    if(s.digits%8==0)std::cout<<s.receipt("running","exact-digits")<<"\n"<<std::flush;
   }
   s.checkpoint();std::cout<<s.receipt("budget-exhausted","complete-digit-checkpoint")<<"\n";return 75;
  }catch(const BudgetExpired&e){if(s.haveInv&&!s.haveState)s.checkpoint();std::cout<<s.receipt("budget-exhausted","bounded-native-step",e.what())<<"\n";return 75;}
  catch(const std::exception&e){std::cout<<s.receipt("failed","exact-native-exception",e.what())<<"\n";return 1;}
 }catch(const std::exception&e){
  std::ostringstream s;s<<"{\"format\":\"isp-constant-unit-multiple-rhs-dixon-native-v1\",\"status\":\"failed\",\"error\":\""<<esc(e.what())<<"\",\"verificationScope\":\"square-unit-only\",\"protocolVersion\":1,\"allOriginalUnitRowsVerified\":false,\"allOriginalSourceEquationsVerified\":false,\"fullOriginal4367VerificationComplete\":false}";
  atomic_text(out/"constant-unit-dixon-native-receipt.json",s.str());std::cout<<s.str()<<"\n";return 1;
 }
}
