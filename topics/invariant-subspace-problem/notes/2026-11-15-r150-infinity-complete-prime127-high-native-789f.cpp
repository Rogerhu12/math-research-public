// Complete original infinity high block over F_127, with one actual RHS.
// Author: Astra-ISP-789f / literature_audit. AI-assisted: GPT-6 Astra Pro.
// Date: 2026-11-15. All 5100 rows and 3762 columns are retained.
#include "2026-11-15-r150-original-f127-bitplane-789f.hpp"
#include <chrono>
#include <filesystem>
#include <iomanip>
#include <iostream>
#include <memory>
#include <sstream>
using namespace std;
namespace fs=std::filesystem;
using Clock=chrono::steady_clock;
static constexpr int NR=5100,NC=3762,NW=(NC+31)/32;
static Clock::time_point begun;
static double limit_seconds;
static void need(bool b,const string&s){if(!b)throw runtime_error(s);}
static double elapsed(){return chrono::duration<double>(Clock::now()-begun).count();}
static void deadline(){if(elapsed()>limit_seconds)throw runtime_error("budget-exhausted");}
struct Term{uint16_t c;uint8_t v;};
struct Pivot{Triple t;int source=-1;int rhs=0;};
int main(int argc,char**argv){
 begun=Clock::now();
 try{
  need(argc==4,"Usage: native original-high-with-one-rhs.bin out-directory seconds");
  limit_seconds=stod(argv[3]);need(limit_seconds>0&&limit_seconds<=1800,"Finite native budget");
  fs::path out=argv[2];fs::create_directories(out);
  ifstream in(argv[1],ios::binary);need(bool(in),"Open actual high input");
  char magic[8];in.read(magic,8);need(string(magic,8)=="R15H7127","Actual independent input version");
  need(read_le(in,4)==127&&read_le(in,4)==NR&&read_le(in,4)==NC&&read_le(in,4)==1,
       "All original high rows, columns and one RHS");
  string binding(64,' ');in.read(binding.data(),64);
  need(bool(in)&&binding.find_first_not_of("0123456789abcdef")==string::npos,"Binding");
  vector<vector<Term>> rows(NR);vector<int> right(NR);uint64_t nnz=0;
  for(int i=0;i<NR;i++){
   int k=int(read_le(in,2));need(k<=77,"Original quadratic row support");
   int prev=-1;
   for(int j=0;j<k;j++){
    int c=int(read_le(in,2)),v=int(read_le(in,1));
    need(c>prev&&c<NC&&v>0&&v<127,"Ordered original field coefficients");
    rows[i].push_back({uint16_t(c),uint8_t(v)});prev=c;nnz++;
   }
   right[i]=int(read_le(in,1));need(right[i]<127,"Actual RHS coefficient");
  }
  need(in.peek()==char_traits<char>::eof(),"No omitted or trailing original source rows");
  BitOps ops;uint64_t arithmetic=ops.verify();deadline();
  vector<unique_ptr<Pivot>> piv(NC);vector<int> dependentResiduals;
  int rk=0,dependent=0,zeros=0,first_bad=-1;uint64_t additions=0;
  double last=elapsed();
  for(int i=0;i<NR;i++){
   Row row(7*NW);for(auto z:rows[i])BitOps::set(row,NW,z.c,z.v);
   int rhs=right[i],newcol=-1;if(rows[i].empty())zeros++;
   for(int w=0;w<NW&&newcol<0;w++){
    uint32_t mask=(w==NC/32&&NC%32)?((uint32_t(1)<<(NC%32))-1):UINT32_MAX;
    uint32_t nz=0;for(int b=0;b<7;b++)nz|=row[b*NW+w];nz&=mask;
    while(nz){
     int c=32*w+__builtin_ctz(nz),v=BitOps::get(row,NW,c);
     need(c<NC&&v>0&&v<127,"Canonical actual pivot coefficient");
     if(!piv[c]){
      ops.multiple(row,NW,w,ops.inv[v]);rhs=rhs*ops.inv[v]%127;
      need(BitOps::get(row,NW,c)==1,"Normalized actual pivot");
      auto p=make_unique<Pivot>();p->t[0]=move(row);
      BitOps::refresh(p->t,NW,w);p->source=i;p->rhs=rhs;
      piv[c]=move(p);newcol=c;rk++;break;
     }
     int a=127-v;auto r=ops.rep[a];
     BitOps::add(row,NW,w,piv[c]->t[r.c],NW,w,NW-w,r.rot,r.neg);
     rhs=(rhs+a*piv[c]->rhs)%127;additions++;
     if((additions&16383)==0)deadline();
     nz=0;for(int b=0;b<7;b++)nz|=row[b*NW+w];nz&=mask;
    }
   }
   if(newcol<0){
    for(int c=0;c<NC;c++)need(BitOps::get(row,NW,c)==0,"Every dependent original row is zero");
    dependent++;dependentResiduals.push_back(rhs);
    if(rhs&&first_bad<0)first_bad=i;
   }
   if(elapsed()-last>10){
    cerr<<"{\"processedOriginalRows\":"<<i+1<<",\"rank\":"<<rk
        <<",\"rowAdditions\":"<<additions<<",\"seconds\":"<<elapsed()<<"}\n";
    last=elapsed();
   }
   deadline();
  }
  need(rk+dependent==NR,"Every original source row processed");
  bool compatible=first_bad<0;vector<int>x(NC);
  uint64_t products=0;
  if(compatible){
   for(int c=NC-1;c>=0;c--)if(piv[c]){
    int v=piv[c]->rhs;
    for(int j=c+1;j<NC;j++)v=(v-BitOps::get(piv[c]->t[0],NW,j)*x[j])%127;
    x[c]=(v+127)%127;
   }
   for(int i=0;i<NR;i++){
    int v=0;for(auto z:rows[i])v=(v+z.v*x[z.c])%127;
    need(v==right[i],"All 5100 original high products of the actual particular");products++;
   }
   fs::path tmp=out/"actual-high-particular.json.tmp";ofstream p(tmp);
   need(bool(p),"Open temporary actual particular");p<<"{\"binding\":\""<<binding
      <<"\",\"prime\":127,\"rows\":3762,\"columns\":1,\"values\":[";
   for(int i=0;i<NC;i++){if(i)p<<",";p<<x[i];}p<<"],\"all5100OriginalProductsVerified\":true}\n";
   p.close();need(bool(p),"Actual particular complete");fs::rename(tmp,out/"actual-high-particular.json");
  }
  fs::path rt=out/"native-high-field127-receipt.json.tmp";ofstream r(rt);
  need(bool(r),"Native receipt");
  r<<setprecision(17)<<"{\"format\":\"r150-original-high-field127-with-one-rhs-v1\","
   <<"\"status\":\"completed\",\"binding\":\""<<binding<<"\",\"prime\":127,"
   <<"\"originalSourceRows\":5100,\"originalTargetCoordinates\":3762,"
   <<"\"rank\":"<<rk<<",\"nullity\":"<<NC-rk<<",\"dependentOriginalRows\":"<<dependent
   <<",\"originalZeroRowsModulo127\":"<<zeros<<",\"nonzeroInputEntries\":"<<nnz
   <<",\"rowAdditions\":"<<additions<<",\"exhaustiveBitPlaneChecks\":"<<arithmetic
   <<",\"all5100OriginalRowsRetained\":true,\"all3762OriginalColumnsRetained\":true,"
   <<"\"allDependentOriginalCoefficientRowsZero\":true,\"actualUnitMinorVerified\":true,"
   <<"\"rhsCompatible\":"<<(compatible?"true":"false")<<",\"augmentedRank\":"<<rk+(compatible?0:1)
   <<",\"firstIncompatibleOriginalRow\":"<<first_bad
   <<",\"particularOriginalProductCoordinates\":"<<products
   <<",\"arithmeticPrimeFixedBeforeExecution\":true,\"temporaryOnly\":true,\"mathSeconds\":"<<elapsed()<<"}\n";
  r.close();need(bool(r),"Complete native receipt");fs::rename(rt,out/"native-high-field127-receipt.json");
  ifstream done(out/"native-high-field127-receipt.json");cout<<done.rdbuf();return 0;
 }catch(const exception&e){cerr<<"original-high-field127: "<<e.what()<<"\n";return string(e.what())=="budget-exhausted"?124:1;}
}
