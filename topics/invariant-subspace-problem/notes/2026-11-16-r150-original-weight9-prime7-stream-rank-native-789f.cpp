// Original weighted9 matrix: complete prime7 row stream and whole-row checkpoints.
// Author: Astra-ISP-789f / normal_annihilator.
// AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
// No external arithmetic library. Every field operation is tested against scalar F7.
#include <algorithm>
#include <array>
#include <chrono>
#include <csignal>
#include <cstdint>
#include <cstring>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <memory>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
namespace fs=std::filesystem;
using U=uint64_t;
static volatile std::sig_atomic_t stopping=0;
static void stopped(int){stopping=1;}
static void need(bool ok,const std::string& s){if(!ok)throw std::runtime_error(s);}
static double seconds(){using C=std::chrono::steady_clock;return std::chrono::duration<double>(C::now().time_since_epoch()).count();}
static uint32_t rotr(uint32_t x,unsigned n){return (x>>n)|(x<<(32-n));}
struct SHA {
 std::array<uint32_t,8> h{0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19};
 std::array<unsigned char,64> b{};U total=0;size_t used=0;
 void block(const unsigned char* p){
  static const uint32_t k[64]={
   0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
   0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
   0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
   0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
   0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
   0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
   0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
   0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2};
  uint32_t w[64];
  for(int i=0;i<16;i++)w[i]=(uint32_t(p[4*i])<<24)|(uint32_t(p[4*i+1])<<16)|(uint32_t(p[4*i+2])<<8)|p[4*i+3];
  for(int i=16;i<64;i++){uint32_t a=rotr(w[i-15],7)^rotr(w[i-15],18)^(w[i-15]>>3),c=rotr(w[i-2],17)^rotr(w[i-2],19)^(w[i-2]>>10);w[i]=w[i-16]+a+w[i-7]+c;}
  uint32_t a=h[0],c=h[1],d=h[2],e=h[3],f=h[4],g=h[5],j=h[6],l=h[7];
  for(int i=0;i<64;i++){
   uint32_t s1=rotr(f,6)^rotr(f,11)^rotr(f,25),ch=(f&g)^((~f)&j),t1=l+s1+ch+k[i]+w[i];
   uint32_t s0=rotr(a,2)^rotr(a,13)^rotr(a,22),maj=(a&c)^(a&d)^(c&d),t2=s0+maj;
   l=j;j=g;g=f;f=e+t1;e=d;d=c;c=a;a=t1+t2;
  }
  h[0]+=a;h[1]+=c;h[2]+=d;h[3]+=e;h[4]+=f;h[5]+=g;h[6]+=j;h[7]+=l;
 }
 void update(const void* raw,size_t n){
  const auto* p=static_cast<const unsigned char*>(raw);total+=n;
  while(n){size_t take=std::min(n,64-used);std::memcpy(b.data()+used,p,take);used+=take;p+=take;n-=take;
   if(used==64){block(b.data());used=0;}}
 }
 std::string finish(){
  U bits=total*8;b[used++]=0x80;
  if(used>56){while(used<64)b[used++]=0;block(b.data());used=0;}
  while(used<56)b[used++]=0;
  for(int i=7;i>=0;i--)b[used++]=static_cast<unsigned char>(bits>>(8*i));
  block(b.data());std::ostringstream s;s<<std::hex<<std::setfill('0');
  for(auto v:h)s<<std::setw(8)<<v;return s.str();
 }
};
static std::string hash_file(const fs::path& p){
 std::ifstream f(p,std::ios::binary);need(bool(f),"open file for complete SHA");
 std::array<char,1048576> buf;SHA h;
 while(f){f.read(buf.data(),buf.size());auto n=f.gcount();if(n)h.update(buf.data(),size_t(n));}
 need(f.eof(),"complete SHA read");return h.finish();
}
static std::string hash_text(const std::string& s){SHA h;h.update(s.data(),s.size());return h.finish();}
static void hex64(const std::string& s){need(s.size()==64 && s.find_first_not_of("0123456789abcdef")==std::string::npos,"canonical SHA/binding");}
static void write32(std::ostream& f,uint32_t n){char b[4];for(int i=0;i<4;i++)b[i]=char(n>>(8*i));f.write(b,4);}
static void write64(std::ostream& f,U n){char b[8];for(int i=0;i<8;i++)b[i]=char(n>>(8*i));f.write(b,8);}
static uint32_t read32(std::istream& f){unsigned char b[4];f.read(reinterpret_cast<char*>(b),4);need(bool(f),"complete u32");uint32_t n=0;for(int i=0;i<4;i++)n|=uint32_t(b[i])<<(8*i);return n;}
static U read64(std::istream& f){unsigned char b[8];f.read(reinterpret_cast<char*>(b),8);need(bool(f),"complete u64");U n=0;for(int i=0;i<8;i++)n|=U(b[i])<<(8*i);return n;}
static std::string read_string(std::istream& f,size_t n){std::string s(n,' ');f.read(s.data(),n);need(bool(f),"complete fixed string");return s;}
static void atomic_text(const fs::path& p,const std::string& s){
 fs::path t=p;t+=".tmp";{std::ofstream f(t,std::ios::binary);need(bool(f),"open text transaction");f<<s;f.flush();need(bool(f),"complete text transaction");}
 fs::rename(t,p);
}
static std::array<U,3> scaled(U a,U b,U c,unsigned q){
 U x=a,y=b,z=c;bool neg=false;
 switch(q){
  case 0:return {0,0,0};
  case 1:break;
  case 2:x=c;y=a;z=b;break;
  case 3:x=b;y=c;z=a;neg=true;break;
  case 4:x=b;y=c;z=a;break;
  case 5:x=c;y=a;z=b;neg=true;break;
  case 6:neg=true;break;
  default:throw std::runtime_error("scalar outside F7");
 }
 if(neg){U nz=a|b|c;x=(~x)&nz;y=(~y)&nz;z=(~z)&nz;}
 return {x,y,z};
}
static std::array<U,3> plus(U a0,U a1,U a2,U b0,U b1,U b2){
 U c0=a0&b0,s0=a0^b0;
 U x1=a1^b1,s1=x1^c0,c1=(a1&b1)|(x1&c0);
 U x2=a2^b2,s2=x2^c1,c2=(a2&b2)|(x2&c1);
 U t0=s0^c2,d0=s0&c2;
 U t1=s1^d0,d1=s1&d0;
 U t2=s2^d1;
 U seven=t0&t1&t2;
 return {t0&~seven,t1&~seven,t2&~seven};
}
using Vec=std::vector<U>;
struct Pivot{uint32_t original_row=0,column=0,coefficient=0;Vec v;};
struct Engine {
 uint32_t cols,words;std::vector<int> at;std::vector<Pivot> piv;U reductions=0;unsigned determinant=1;
 explicit Engine(uint32_t c):cols(c),words((c+63)/64),at(c,-1){}
 unsigned get(const Vec& v,uint32_t c)const{
  U bit=U(1)<<(c%64);size_t w=c/64;
  return unsigned(bool(v[w]&bit))+2*unsigned(bool(v[words+w]&bit))+4*unsigned(bool(v[2*words+w]&bit));
 }
 void canonical(const Vec& v)const{
  need(v.size()==3*words,"complete three planes");
  for(uint32_t w=0;w<words;w++)need((v[w]&v[words+w]&v[2*words+w])==0,"canonical coefficients0..6");
  if(cols%64){U invalid=~((U(1)<<(cols%64))-1);
   need(((v[words-1]|v[2*words-1]|v[3*words-1])&invalid)==0,"all unused tail bits zero");}
 }
 int first(const Vec& v,uint32_t begin=0)const{
  for(uint32_t w=begin;w<words;w++){U z=v[w]|v[words+w]|v[2*words+w];
   if(z)return int(64*w+__builtin_ctzll(z));}return -1;
 }
 void multiply(Vec& v,unsigned q,uint32_t begin=0)const{
  for(uint32_t w=begin;w<words;w++){auto s=scaled(v[w],v[words+w],v[2*words+w],q);
   v[w]=s[0];v[words+w]=s[1];v[2*words+w]=s[2];}
 }
 void add_multiple(Vec& v,const Vec& b,unsigned q,uint32_t begin)const{
  for(uint32_t w=begin;w<words;w++){
   auto s=scaled(b[w],b[words+w],b[2*words+w],q);
   auto t=plus(v[w],v[words+w],v[2*words+w],s[0],s[1],s[2]);
   v[w]=t[0];v[words+w]=t[1];v[2*words+w]=t[2];
  }
 }
 bool row(Vec v,uint32_t original_row){
  canonical(v);uint32_t begin=0;
  static const unsigned inverse[7]={0,1,4,5,2,3,6};
  while(true){
   int column=first(v,begin);if(column<0)return false;
   need(uint32_t(column)<cols,"leading column in original dictionary");
   unsigned c=get(v,column);need(c>0 && c<7,"nonzero actual leading coefficient");
   int j=at[column];
   if(j<0){
    multiply(v,inverse[c],uint32_t(column)/64);canonical(v);
    need(first(v)==column && get(v,column)==1,"normalized actual original pivot");
    determinant=(determinant*c)%7;
    at[column]=int(piv.size());piv.push_back({original_row,uint32_t(column),c,std::move(v)});return true;
   }
   add_multiple(v,piv[size_t(j)].v,7-c,uint32_t(column)/64);reductions++;
   need(get(v,column)==0,"every actual pivot cancellation");
   begin=uint32_t(column)/64;
  }
 }
 Vec packed(const std::vector<unsigned>& row)const{
  need(row.size()==cols,"scalar row width");Vec v(3*words,0);
  for(uint32_t c=0;c<cols;c++){need(row[c]<7,"scalar test input");
   for(unsigned k=0;k<3;k++)if(row[c]&(1u<<k))v[k*words+c/64]|=U(1)<<(c%64);}
  return v;
 }
};
static unsigned scalar_rank(std::vector<std::vector<unsigned>> a){
 if(a.empty())return 0;size_t r=0,n=a[0].size();static const unsigned inv[7]={0,1,4,5,2,3,6};
 for(size_t c=0;c<n && r<a.size();c++){
  size_t p=r;while(p<a.size() && a[p][c]==0)p++;if(p==a.size())continue;
  std::swap(a[r],a[p]);unsigned q=inv[a[r][c]];
  for(size_t j=c;j<n;j++)a[r][j]=(a[r][j]*q)%7;
  for(size_t i=r+1;i<a.size();i++)if(a[i][c]){
   unsigned d=a[i][c];for(size_t j=c;j<n;j++)a[i][j]=(a[i][j]+7-(d*a[r][j])%7)%7;
  }r++;
 }return unsigned(r);
}
static unsigned scalar_det(std::vector<std::vector<unsigned>> a){
 unsigned d=1;size_t n=a.size();static const unsigned inv[7]={0,1,4,5,2,3,6};
 for(size_t c=0;c<n;c++){
  size_t p=c;while(p<n && !a[p][c])p++;if(p==n)return 0;
  if(p!=c){std::swap(a[p],a[c]);d=(7-d)%7;}d=(d*a[c][c])%7;
  unsigned q=inv[a[c][c]];
  for(size_t i=c+1;i<n;i++){unsigned z=a[i][c]*q%7;
   for(size_t j=c;j<n;j++)a[i][j]=(a[i][j]+7-z*a[c][j]%7)%7;}
 }return d;
}
static void selftest(){
 need(hash_text("")=="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","SHA empty fixture");
 need(hash_text("abc")=="ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad","SHA abc fixture");
 for(unsigned a=0;a<7;a++)for(unsigned b=0;b<7;b++){
  auto z=plus(U(a&1),U((a>>1)&1),U((a>>2)&1),U(b&1),U((b>>1)&1),U((b>>2)&1));
  need(z[0]+2*z[1]+4*z[2]==(a+b)%7,"all49 independent scalar field additions");
  auto t=scaled(U(a&1),U((a>>1)&1),U((a>>2)&1),b);
  need(t[0]+2*t[1]+4*t[2]==(a*b)%7,"all49 independent scalar field products");
 }
 U random=0x789f3e887d7c01ULL;
 auto next=[&](){random^=random<<13;random^=random>>7;random^=random<<17;return random;};
 for(unsigned fixture=0;fixture<8;fixture++){
  unsigned nr=21+fixture,nc=(fixture&1)?79:27;Engine e(nc);
  std::vector<std::vector<unsigned>> a(nr,std::vector<unsigned>(nc));
  for(unsigned i=0;i<nr;i++)for(unsigned j=0;j<nc;j++)a[i][j]=unsigned(next()%7);
  // Force leading gaps and dependencies, and later introduce earlier pivots.
  for(unsigned i=0;i<nr;i++)for(unsigned j=0;j<4;j++)a[i][j]=0;
  if(nr>5)a[5]=a[2];
  if(fixture%2==0){a[nr-1][0]=1;a[nr-2][2]=3;}
  for(unsigned i=0;i<nr;i++)e.row(e.packed(a[i]),i);
  need(e.piv.size()==scalar_rank(a),"independent small rectangular scalar rank");
  std::vector<std::vector<unsigned>> minor(e.piv.size(),std::vector<unsigned>(e.piv.size()));
  for(size_t i=0;i<e.piv.size();i++)for(size_t j=0;j<e.piv.size();j++)
   minor[i][j]=a[e.piv[i].original_row][e.piv[j].column];
  need(scalar_det(minor)==e.determinant && e.determinant!=0,"actual insertion-order original minor determinant");
 }
}
struct Shape{uint32_t rows=49368,cols=16445,source=16442,targets=3,words=257,limit=16047;};
static void write_shape(std::ostream& f,const Shape& s){
 for(uint32_t v:{1u,7u,s.rows,s.cols,s.source,s.targets,s.words,s.limit})write32(f,v);
}
static void read_shape(std::istream& f,const Shape& s){
 for(uint32_t v:{1u,7u,s.rows,s.cols,s.source,s.targets,s.words,s.limit})need(read32(f)==v,"same complete original shape and prime");
}
static std::string checkpoint(Engine& e,const Shape& s,U next,U generation,const fs::path& root,
                              const std::string& binding,const std::string& inputsha){
 std::string name="complete-row-state-slot-"+std::to_string(generation%2)+".bin";
 fs::path p=root/name,t=p;t+=".tmp";
 {std::ofstream f(t,std::ios::binary);need(bool(f),"open whole-row state transaction");
  f.write("R15M9S71",8);write_shape(f,s);write64(f,generation);write64(f,next);
  write64(f,U(e.piv.size()));write64(f,e.reductions);write32(f,e.determinant);
  f.write(binding.data(),64);f.write(inputsha.data(),64);
  for(const auto& v:e.piv){
   write32(f,v.original_row);write32(f,v.column);write32(f,v.coefficient);
   f.write(reinterpret_cast<const char*>(v.v.data()),std::streamsize(v.v.size()*sizeof(U)));
  }f.flush();need(bool(f),"complete whole-row state write");
 }
 fs::rename(t,p);U bytes=fs::file_size(p);std::string digest=hash_file(p);
 U expected=204+U(e.piv.size())*(12+U(3)*s.words*8);need(bytes==expected,"complete checkpoint byte count");
 std::ostringstream m;
 m<<"{\"format\":\"r150-original-m9-prime7-row-state-v1\",\"binding\":\""<<binding
  <<"\",\"inputSHA256\":\""<<inputsha<<"\",\"generation\":"<<generation
  <<",\"nextRow\":"<<next<<",\"rank\":"<<e.piv.size()<<",\"reductionCount\":"<<e.reductions
  <<",\"selectedInsertionMinorDeterminant7\":"<<e.determinant
  <<",\"file\":{\"path\":\""<<name<<"\",\"bytes\":"<<bytes<<",\"sha256\":\""<<digest
  <<"\"},\"completeOriginalRowsOnly\":true}\n";
 atomic_text(root/"native-state-manifest.json",m.str());return digest;
}
static void restore(Engine& e,const Shape& s,const fs::path& file,const std::string& expected_sha,
                    const std::string& binding,const std::string& inputsha,U& next,U& generation){
 hex64(expected_sha);need(hash_file(file)==expected_sha,"full previous whole-row state SHA");
 std::ifstream f(file,std::ios::binary);need(read_string(f,8)=="R15M9S71","same state magic");
 read_shape(f,s);generation=read64(f);next=read64(f);U rank=read64(f);e.reductions=read64(f);
 unsigned determinant=read32(f);
 need(read_string(f,64)==binding && read_string(f,64)==inputsha,"same original input and source binding");
 need(next<=s.rows && rank<=s.cols && rank<=next && generation>0,"whole-row checkpoint dimensions");
 uint32_t last=0;e.determinant=1;
 for(U i=0;i<rank;i++){
  uint32_t original=read32(f),column=read32(f),c=read32(f);
  need(original<next && (i==0 || original>last) && column<s.cols && e.at[column]<0 &&
       c>0 && c<7,"distinct true pivot indices and coefficient");
  last=original;Vec v(3*s.words);f.read(reinterpret_cast<char*>(v.data()),std::streamsize(v.size()*sizeof(U)));
  need(bool(f),"all prior pivot coefficients retained");e.canonical(v);
  need(e.first(v)==int(column) && e.get(v,column)==1,"complete prior normalized pivot");
  e.at[column]=int(e.piv.size());e.piv.push_back({original,column,c,std::move(v)});
  e.determinant=e.determinant*c%7;
 }
 need(e.determinant==determinant && determinant>0,"prior insertion-order unit determinant");
 char tail;need(!f.read(&tail,1) && f.eof(),"no hidden or truncated checkpoint bytes");
}
int main(int argc,char**argv){
 try{
  U endian=1;need(*reinterpret_cast<unsigned char*>(&endian)==1,"little-endian input platform");
  std::string input,binding,inputsha,resume,resumesha,out;double budget=600;bool test=false;
  for(int i=1;i<argc;i++){
   std::string k=argv[i];if(k=="--selftest-only"){test=true;continue;}
   need(i+1<argc,"paired native argument");std::string v=argv[++i];
   if(k=="--input")input=v;else if(k=="--binding")binding=v;else if(k=="--input-sha")inputsha=v;
   else if(k=="--out")out=v;else if(k=="--resume")resume=v;else if(k=="--resume-sha")resumesha=v;
   else if(k=="--seconds")budget=std::stod(v);else throw std::runtime_error("unknown native argument");
  }
  selftest();
  if(test){std::cout<<"{\"status\":\"completed-selftest\",\"all49FieldAdds\":true,\"all49FieldProducts\":true,"
      "\"independentSmallRectangularFixtures\":8,\"allOriginalSelectedMinorDeterminantsVerified\":true,"
      "\"SHAKnownFixtures\":true}\n";return 0;}
  need(!input.empty() && !out.empty() && budget>20 && budget<=3600,"bounded native stream inputs");
  hex64(binding);hex64(inputsha);double begin=seconds();need(hash_file(input)==inputsha,"all original input bytes SHA");
  Shape shape;Engine engine(shape.cols);fs::path root(out);fs::create_directories(root);
  U next=0,generation=0;
  if(!resume.empty()){need(!resumesha.empty(),"prior actual state SHA");restore(engine,shape,resume,resumesha,binding,inputsha,next,generation);}
  std::ifstream f(input,std::ios::binary);need(read_string(f,8)=="R15M9071","complete original matrix input magic");
  read_shape(f,shape);need(read_string(f,64)==binding,"actual source binding in input");
  U expected=104+U(shape.rows)*3*shape.words*8;
  need(fs::file_size(input)==expected,"all original matrix rows present");
  f.seekg(std::streamoff(104+next*3*shape.words*8));need(bool(f),"resume at exact whole original row");
  U before=next;double lastsave=seconds(),lastprogress=lastsave;
  std::signal(SIGTERM,stopped);std::signal(SIGINT,stopped);
  while(next<shape.rows && engine.piv.size()<shape.limit){
   Vec row(3*shape.words);f.read(reinterpret_cast<char*>(row.data()),std::streamsize(row.size()*8));
   need(bool(f),"complete next original row");engine.row(std::move(row),uint32_t(next));next++;
   if(seconds()-lastprogress>=30){
    std::cout<<"{\"phase\":\"original-row-elimination\",\"nextOriginalRow\":"<<next<<",\"rank\":"
     <<engine.piv.size()<<",\"reductions\":"<<engine.reductions<<"}\n"<<std::flush;lastprogress=seconds();
   }
   if(stopping || seconds()-begin>=budget-12)break;
   if(seconds()-lastsave>=60){checkpoint(engine,shape,next,++generation,root,binding,inputsha);lastsave=seconds();}
  }
  unsigned sourcepivots=0,targetpivots=0;
  for(const auto& v:engine.piv){if(v.column<shape.source)sourcepivots++;else targetpivots++;}
  need(sourcepivots<=16046,"original source prefix obeys the paid rational rank ceiling");
  bool reached=engine.piv.size()>=shape.limit,allrows=next==shape.rows;
  if(reached)need(targetpivots>0,"strict augmented rank uses an original target column");
  std::string finalsha=checkpoint(engine,shape,next,++generation,root,binding,inputsha);
  std::ostringstream result;
  result<<"{\"format\":\"r150-original-m9-prime7-native-v1\",\"binding\":\""<<binding
   <<"\",\"status\":\""<<(reached?"rank-threshold-reached":(allrows?"all-rows-complete":"budget-checkpoint"))
   <<"\",\"inputSHA256\":\""<<inputsha<<"\",\"generation\":"<<generation
   <<",\"firstOriginalRowThisInvocation\":"<<before<<",\"nextOriginalRow\":"<<next
   <<",\"completeInputRows\":"<<shape.rows<<",\"completeSourceColumns\":"<<shape.source
   <<",\"completeTargetColumns\":"<<shape.targets<<",\"rankOfProcessedOriginalRows\":"<<engine.piv.size()
   <<",\"sourcePivotCount\":"<<sourcepivots<<",\"targetPivotCount\":"<<targetpivots
   <<",\"allOriginalRowsProcessed\":"<<(allrows?"true":"false")
   <<",\"rank16047ThresholdReached\":"<<(reached?"true":"false")
   <<",\"selectedInsertionMinorDeterminant7\":"<<engine.determinant
   <<",\"reductionCount\":"<<engine.reductions<<",\"fullStateSHA256\":\""<<finalsha
   <<"\",\"elapsedSeconds\":"<<std::setprecision(17)<<seconds()-begin
   <<",\"allFieldArithmeticSelftestsVerified\":true,\"allEightIndependentSmallRankAndMinorTestsVerified\":true,"
   <<"\"everyActualPivotCancellationVerified\":true,\"allProcessedOriginalRowsHaveCanonicalPrime7Coefficients\":true,"
   <<"\"checkpointContainsOnlyWholeOriginalRows\":true}\n";
  atomic_text(root/"original-m9-prime7-native-receipt.json",result.str());std::cout<<result.str()<<std::flush;
  return (reached || allrows)?0:75;
 }catch(const std::exception&e){
  std::string msg=e.what();for(char& c:msg)if(c=='"' || c=='\\' || c=='\n' || c=='\r')c=' ';
  std::cerr<<"{\"format\":\"r150-original-m9-prime7-native-v1\",\"status\":\"failed\",\"error\":\""<<msg<<"\"}\n";
  return 1;
 }
}
