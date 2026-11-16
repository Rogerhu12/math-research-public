// Recover the full critical residue kernel from already verified pivots.
// Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro,2026-11-16.
// No new elimination. All6018 original input rows are multiplied back.
#include <array>
#include <chrono>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
namespace fs=std::filesystem;
using Clock=chrono::steady_clock;
constexpr unsigned NR=6018,NC=4266,NB=5,NW=67;
using Packed=array<uint64_t,NB*NW>;
static Clock::time_point started;static double budget;
static void need(bool v,const string&s){if(!v)throw runtime_error(s);}
static double elapsed(){return chrono::duration<double>(Clock::now()-started).count();}
static void check_time(){need(elapsed()<budget,"budget-exhausted");}
static uint8_t r8(istream&f){char c;need(bool(f.get(c)),"Truncated binary");return uint8_t(c);}
static uint16_t r16(istream&f){unsigned a=r8(f),b=r8(f);return uint16_t(a|(b<<8));}
static uint32_t r32(istream&f){uint32_t a=0;for(unsigned i=0;i<4;i++)a|=uint32_t(r8(f))<<(8*i);return a;}
static uint64_t r64(istream&f){uint64_t a=0;for(unsigned i=0;i<8;i++)a|=uint64_t(r8(f))<<(8*i);return a;}
static void w8(ostream&f,unsigned v){f.put(char(v));}
static void w16(ostream&f,unsigned v){for(unsigned i=0;i<2;i++)w8(f,(v>>(8*i))&255);}
static void w32(ostream&f,uint32_t v){for(unsigned i=0;i<4;i++)w8(f,(v>>(8*i))&255);}
static string exact_string(istream&f,unsigned n){string s(n,' ');f.read(s.data(),n);need(bool(f),"Truncated string");return s;}
static unsigned get(const Packed&a,unsigned j){unsigned v=0;for(unsigned k=0;k<NB;k++)v|=unsigned((a[k*NW+(j>>6)]>>(j&63))&1)<<k;return v;}
struct Term{uint16_t col;uint8_t val;};
int main(int argc,char**argv){
 started=Clock::now();
 try{
  need(argc==6,"Usage: recover input.bin pivots.bin out-dir seconds child-binding");
  budget=stod(argv[4]);need(budget>0&&budget<=1800,"Explicit finite budget");
  string child=argv[5];need(child.size()==64&&child.find_first_not_of("0123456789abcdef")==string::npos,"Child binding");
  ifstream in(argv[1],ios::binary);need(bool(in),"Original input exists");
  need(exact_string(in,8)=="R15CH601","Original input magic");
  unsigned p=r32(in);need(p==17||p==19,"Pinned actual prime");
  need(r32(in)==NR&&r32(in)==NC,"All original dimensions");
  string parent=exact_string(in,64);
  need(parent.find_first_not_of("0123456789abcdef")==string::npos,"Parent binding");
  vector<vector<Term>> rows(NR);unsigned nnz=0;
  for(unsigned i=0;i<NR;i++){
   unsigned n=r16(in);need(n<=77,"Original quadratic row support");
   int prev=-1;
   for(unsigned j=0;j<n;j++){
    unsigned c=r16(in),v=r8(in);need(c<NC&&int(c)>prev&&v>0&&v<p,"Original ordered row");
    rows[i].push_back({uint16_t(c),uint8_t(v)});prev=int(c);++nnz;
   }
  }
  need(in.peek()==char_traits<char>::eof(),"Input complete EOF");
  ifstream pf(argv[2],ios::binary);need(bool(pf),"Paid pivots exist");
  need(exact_string(pf,8)=="R15CHPV1","Paid pivot magic");
  need(r32(pf)==p,"Same actual prime");
  unsigned rank=r32(pf);need(rank<=NC,"Actual rank range");
  need(r32(pf)==NC&&r32(pf)==NB&&r32(pf)==NW,"Paid packed dimensions");
  need(exact_string(pf,64)==parent,"Same original binding");
  vector<Packed> piv(rank);vector<unsigned> pc(rank),ps(rank);
  vector<bool> used(NC,false),used_source(NR,false);int prev=-1;
  for(unsigned i=0;i<rank;i++){
   unsigned c=r16(pf),s=r16(pf);need(c<NC&&int(c)>prev&&s<NR&&!used_source[s],"Actual ordered independent pivots");
   pc[i]=c;ps[i]=s;used[c]=true;used_source[s]=true;prev=int(c);
   for(auto &v:piv[i])v=r64(pf);
   need(get(piv[i],c)==1,"Normalized pivot equals one");
   for(unsigned j=0;j<NC;j++){
    unsigned v=get(piv[i],j);need(v<p,"Canonical field coefficients");
    if(j<c)need(v==0,"Full triangular prefix zero");
   }
   for(unsigned j=NC;j<NW*64;j++)need(get(piv[i],j)==0,"All padding zero");
   if((i&255)==0)check_time();
  }
  need(pf.peek()==char_traits<char>::eof(),"Paid pivots complete EOF");
  vector<unsigned> freec;for(unsigned c=0;c<NC;c++)if(!used[c])freec.push_back(c);
  unsigned nf=freec.size();need(nf+rank==NC&&nf>0&&nf<=64,"Actual finite nullity");
  vector<vector<uint8_t>> K(NC,vector<uint8_t>(nf,0));
  for(unsigned k=0;k<nf;k++)K[freec[k]][k]=1;
  for(unsigned z=rank;z>0;z--){
   unsigned i=z-1,c=pc[i];vector<uint64_t> sum(nf,0);
   for(unsigned j=c+1;j<NC;j++){
    unsigned v=get(piv[i],j);if(!v)continue;
    for(unsigned k=0;k<nf;k++)sum[k]+=uint64_t(v)*K[j][k];
   }
   for(unsigned k=0;k<nf;k++)K[c][k]=uint8_t((p-sum[k]%p)%p);
   if((i&127)==0)check_time();
  }
  for(unsigned k=0;k<nf;k++)for(unsigned j=0;j<nf;j++)need(K[freec[k]][j]==unsigned(k==j),"Original free-coordinate identity");
  uint64_t verified=0;
  for(unsigned i=0;i<NR;i++){
   vector<uint64_t> sum(nf,0);
   for(auto q:rows[i])for(unsigned k=0;k<nf;k++)sum[k]+=uint64_t(q.val)*K[q.col][k];
   for(unsigned k=0;k<nf;k++){need(sum[k]%p==0,"Full original high product must vanish");++verified;}
   if((i&255)==0)check_time();
  }
  fs::path out=argv[3];fs::create_directories(out);
  fs::path tmp=out/"complete-high-free-kernel.bin.tmp",done=out/"complete-high-free-kernel.bin";
  ofstream f(tmp,ios::binary);need(bool(f),"Create temporary complete kernel");
  f.write("R15CKR01",8);w32(f,p);w32(f,NR);w32(f,NC);w32(f,nf);
  f.write(child.data(),64);f.write(parent.data(),64);
  for(unsigned c:freec)w16(f,c);
  for(auto&r:K)for(unsigned v:r)w8(f,v);
  f.close();need(bool(f),"Complete original kernel saved");fs::rename(tmp,done);
  check_time();
  fs::path rt=out/"native-kernel-recovery-receipt.json.tmp";
  ofstream r(rt);need(bool(r),"Create native receipt");
  r<<setprecision(17)<<"{\"format\":\"r150-critical-paid-high-kernel-recovery-v1\",\"status\":\"completed\","
   <<"\"binding\":\""<<child<<"\",\"parentBinding\":\""<<parent<<"\",\"prime\":"<<p
   <<",\"originalSourceRows\":"<<NR<<",\"originalTargetCoordinates\":"<<NC<<",\"rank\":"<<rank<<",\"nullity\":"<<nf
   <<",\"freeHighColumnsZeroBased\":[";
  for(unsigned k=0;k<nf;k++){if(k)r<<",";r<<freec[k];}
  r<<"],\"originalInputNonzeroEntries\":"<<nnz<<",\"originalProductCoordinates\":"<<verified
   <<",\"allOriginalHighProductsZero\":true,\"freeCoordinateBlockIsIdentity\":true,"
   <<"\"allPivotPrefixesAndPaddingVerified\":true,\"allInputAndPivotEOFVerified\":true,"
   <<"\"noNewGaussianElimination\":true,\"noRationalKernelClaim\":true,\"temporaryOnly\":true,"
   <<"\"mathSeconds\":"<<elapsed()<<"}\n";
  r.close();need(bool(r),"Complete native receipt");fs::rename(rt,out/"native-kernel-recovery-receipt.json");
  ifstream result(out/"native-kernel-recovery-receipt.json");cout<<result.rdbuf();return 0;
 }catch(const exception&e){cerr<<"kernel-recovery-error: "<<e.what()<<"\n";return string(e.what())=="budget-exhausted"?124:1;}
}
