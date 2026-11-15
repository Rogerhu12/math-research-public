// Original s=2 complete normal3/4/5 high block, one fixed prime17.
// Author: Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro.
// Only the constant rational block is row-primitive normalized by the producer.
// All5100 source rows and all3762 target columns are kept. No field kernel lift.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
namespace fs=std::filesystem;
using Clock=chrono::steady_clock;
static constexpr unsigned P=17,NR=5100,NC=3762,NB=5,NW=(NC+63)/64;
static constexpr unsigned INV[17]={0,1,9,6,13,7,3,5,15,2,12,14,10,4,11,8,16};
static Clock::time_point started;static double budget;
static void need(bool x,const string&s){if(!x)throw runtime_error(s);}
static double elapsed(){return chrono::duration<double>(Clock::now()-started).count();}
static void deadline(){if(elapsed()>budget)throw runtime_error("budget-exhausted");}
static uint8_t rd8(istream&f){char c;need(bool(f.get(c)),"Truncated input");return uint8_t(c);}
static uint16_t rd16(istream&f){unsigned a=rd8(f),b=rd8(f);return uint16_t(a|(b<<8));}
static uint32_t rd32(istream&f){uint32_t z=0;for(unsigned k=0;k<4;++k)z|=uint32_t(rd8(f))<<(8*k);return z;}
static void wr8(ostream&f,unsigned v){f.put(char(v));}
static void wr16(ostream&f,unsigned v){for(unsigned k=0;k<2;++k)wr8(f,(v>>(8*k))&255);}
static void wr32(ostream&f,uint32_t v){for(unsigned k=0;k<4;++k)wr8(f,(v>>(8*k))&255);}
static void wr64(ostream&f,uint64_t v){for(unsigned k=0;k<8;++k)wr8(f,unsigned((v>>(8*k))&255));}
using Packed=array<uint64_t,NB*NW>;
static unsigned get(const Packed&r,unsigned c){
 unsigned v=0;for(unsigned k=0;k<NB;++k)v|=unsigned((r[k*NW+(c>>6)]>>(c&63))&1)<<k;return v;
}
static void put(Packed&r,unsigned c,unsigned v){
 need(c<NC&&v<P,"Bad packed field coordinate");
 for(unsigned k=0;k<NB;++k)if(v&(1u<<k))r[k*NW+(c>>6)]|=uint64_t(1)<<(c&63);
}
static void add(Packed&r,const Packed&q,unsigned w0){
 for(unsigned w=w0;w<NW;++w){
  uint64_t s[NB+1],d[NB],carry=0;
  for(unsigned k=0;k<NB;++k){
   uint64_t a=r[k*NW+w],b=q[k*NW+w],x=a^b;
   s[k]=x^carry;carry=(a&b)|(x&carry);
  }
  s[NB]=carry;uint64_t borrow=0;
  for(unsigned k=0;k<NB;++k){
   if(P&(1u<<k)){d[k]=~(s[k]^borrow);borrow=~s[k]|borrow;}
   else{d[k]=s[k]^borrow;borrow=~s[k]&borrow;}
  }
  uint64_t take=~(~s[NB]&borrow);
  for(unsigned k=0;k<NB;++k)r[k*NW+w]=s[k]^(take&(s[k]^d[k]));
 }
}
static void test_add(){
 for(unsigned a=0;a<P;++a)for(unsigned b=0;b<P;++b){
  Packed x{},y{};
  for(unsigned c=0;c<NC;++c){put(x,c,(a+c)%P);put(y,c,(b+3*c)%P);}
  add(x,y,0);
  for(unsigned c=0;c<NC;++c)need(get(x,c)==((a+c)%P+(b+3*c)%P)%P,"All289 field addition identities");
  for(unsigned c=NC;c<NW*64;++c){
   uint64_t v=0;for(unsigned k=0;k<NB;++k)v|=x[k*NW+(c>>6)];
   need(!(v&(uint64_t(1)<<(c&63))),"Padding remains zero");
  }
 }
 for(unsigned a=1;a<P;++a)need(a*INV[a]%P==1,"All field inverses verified");
}
struct Term{uint16_t col;uint8_t value;};
struct Pivot{array<Packed,P-1> multiples;uint16_t source;};
static unique_ptr<Pivot> make_pivot(const Packed&r,unsigned col,unsigned f,unsigned source){
 auto out=make_unique<Pivot>();out->source=uint16_t(source);
 array<Packed,P-1> all;all[0]=r;
 for(unsigned k=1;k<P-1;++k){all[k]=all[k-1];add(all[k],r,col>>6);}
 for(unsigned k=1;k<P;++k){
  out->multiples[k-1]=all[(k*INV[f])%P-1];
  need(get(out->multiples[k-1],col)==k,"Normalized pivot multiple");
 }
 return out;
}
static void header(ostream&f,const char*magic,const vector<unsigned>&dims,const string&binding){
 f.write(magic,8);for(unsigned x:dims)wr32(f,x);f.write(binding.data(),64);
}
int main(int argc,char**argv){
 started=Clock::now();
 try{
  need(argc==4,"Usage: high-rank-native input.bin out-directory remaining-seconds");
  budget=stod(argv[3]);need(budget>0&&budget<=1800,"Actual finite positive budget");
  fs::path out=argv[2];fs::create_directories(out);
  ifstream input(argv[1],ios::binary);need(bool(input),"Cannot open input");
  char magic[8];input.read(magic,8);need(string(magic,8)=="R15H4517","Original high block magic");
  need(rd32(input)==P&&rd32(input)==NR&&rd32(input)==NC,"Actual complete high dimensions");
  string binding(64,' ');input.read(binding.data(),64);
  need(bool(input)&&binding.find_first_not_of("0123456789abcdef")==string::npos,"Exact binding");
  vector<vector<Term>> rows(NR);unsigned nnz=0;
  for(unsigned i=0;i<NR;++i){
   unsigned n=rd16(input);need(n<=77,"Original quadratic polynomial row support");
   int prev=-1;
   for(unsigned k=0;k<n;++k){
    unsigned c=rd16(input),v=rd8(input);
    need(c<NC&&int(c)>prev&&v>0&&v<P,"Ordered complete primitive original row");
    rows[i].push_back({uint16_t(c),uint8_t(v)});prev=int(c);++nnz;
   }
  }
  need(input.peek()==char_traits<char>::eof(),"No trailing original input bytes");
  test_add();deadline();
  vector<unique_ptr<Pivot>> piv(NC);unsigned rank=0,zeros=0,dependent=0;
  uint64_t operations=0;double last=elapsed();
  fs::path dagtmp=out/"complete-high-row-operations.bin.tmp";
  ofstream dag(dagtmp,ios::binary);need(bool(dag),"Create actual row-operation DAG");
  header(dag,"R15HDG17",{P,NR,NC},binding);
  for(unsigned i=0;i<NR;++i){
   Packed row{};for(auto t:rows[i])put(row,t.col,t.value);
   if(rows[i].empty())++zeros;
   vector<pair<uint16_t,uint8_t>> ops;int newcol=-1;unsigned first=0;
   for(unsigned w=0;w<NW&&newcol<0;++w){
    uint64_t mask=(w==NC/64&&NC%64)?((uint64_t(1)<<(NC%64))-1):~uint64_t(0);
    uint64_t nz=0;for(unsigned k=0;k<NB;++k)nz|=row[k*NW+w];nz&=mask;
    while(nz){
     unsigned c=64*w+unsigned(__builtin_ctzll(nz)),f=get(row,c);
     need(c<NC&&f>0&&f<P,"Actual high pivot value");
     if(!piv[c]){
      for(unsigned z=0;z<c;++z)need(!get(row,z),"Full echelon prefix zero");
      piv[c]=make_pivot(row,c,f,i);newcol=int(c);first=f;++rank;break;
     }
     unsigned factor=P-f;add(row,piv[c]->multiples[factor-1],w);
     ops.emplace_back(uint16_t(c),uint8_t(factor));++operations;
     if((operations&16383)==0)deadline();
     nz=0;for(unsigned k=0;k<NB;++k)nz|=row[k*NW+w];nz&=mask;
    }
   }
   wr32(dag,uint32_t(ops.size()));
   for(auto [c,f]:ops){wr16(dag,c);wr8(dag,f);}
   wr16(dag,newcol<0?65535:unsigned(newcol));wr8(dag,first);
   if(newcol<0){
    for(unsigned c=0;c<NC;++c)need(!get(row,c),"All complete dependent original row coordinates zero");
    ++dependent;
   }
   if(elapsed()-last>=10){
    cerr<<"{\"phase\":\"complete-high-constant-rank\",\"processedOriginalRows\":"<<i+1
        <<",\"rank\":"<<rank<<",\"rowAdditions\":"<<operations<<",\"seconds\":"<<elapsed()<<"}\n";
    last=elapsed();
   }
   deadline();
  }
  dag.close();need(bool(dag),"Actual DAG complete");need(rank+dependent==NR,"Every original row retained");
  fs::rename(dagtmp,out/"complete-high-row-operations.bin");
  fs::path ptmp=out/"complete-high-normalized-pivots.bin.tmp";
  ofstream pf(ptmp,ios::binary);need(bool(pf),"Create actual normalized pivots");
  header(pf,"R15HPV17",{P,rank,NC,NB,NW},binding);
  for(unsigned c=0;c<NC;++c)if(piv[c]){
   need(get(piv[c]->multiples[0],c)==1,"Actual independent pivot");
   for(unsigned j=0;j<c;++j)need(!get(piv[c]->multiples[0],j),"Actual triangular unit minor");
   wr16(pf,c);wr16(pf,piv[c]->source);
   for(uint64_t word:piv[c]->multiples[0])wr64(pf,word);
  }
  pf.close();need(bool(pf),"Actual pivot output complete");
  fs::rename(ptmp,out/"complete-high-normalized-pivots.bin");
  deadline();
  fs::path rtmp=out/"native-complete-high-rank-receipt.json.tmp";
  ofstream receipt(rtmp);need(bool(receipt),"Create final native receipt");
  receipt<<setprecision(17)
   <<"{\"format\":\"r150-two-complete-high-constant-rank-field17-v1\",\"status\":\"completed\","
   <<"\"binding\":\""<<binding<<"\",\"prime\":17,\"originalSourceRows\":5100,"
   <<"\"originalTargetCoordinates\":3762,\"rank\":"<<rank
   <<",\"nullity\":"<<NC-rank<<",\"dependentOriginalRows\":"<<dependent
   <<",\"originalZeroRowsModulo17\":"<<zeros<<",\"nonzeroFieldInputEntries\":"<<nnz
   <<",\"rowAdditions\":"<<operations<<",\"all5100OriginalSourceRowsRetained\":true,"
   <<"\"all3762OriginalHighColumnsRetained\":true,\"allDependentOriginalRowsReducedToZero\":true,"
   <<"\"independentOriginalPivotMinorVerified\":true,\"all289BitPlaneAdditionIdentitiesVerified\":true,"
   <<"\"all16FieldInversesVerified\":true,\"primePredeterminedNoScan\":true,"
   <<"\"noRationalKernelInferredFromFieldKernel\":true,\"temporaryOnly\":true,"
   <<"\"mathSeconds\":"<<elapsed()<<"}\n";
  receipt.close();need(bool(receipt),"Complete final native receipt");
  fs::rename(rtmp,out/"native-complete-high-rank-receipt.json");
  ifstream done(out/"native-complete-high-rank-receipt.json");cout<<done.rdbuf();return 0;
 }catch(const exception&e){
  cerr<<"complete-high-rank-error: "<<e.what()<<"\n";
  return string(e.what())=="budget-exhausted"?124:1;
 }
}
