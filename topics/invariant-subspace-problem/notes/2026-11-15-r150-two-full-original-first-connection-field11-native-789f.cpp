// Exact full original F_11 first connection.  AI-assisted GPT-6 Astra Pro.
// Author: Astra-ISP-789f / literature_audit, 2026-11-15.
// The producer supplies the original A0^T rows and A1^T Lambda, without
// row-content division.  All constant columns are retained.  No mathematical
// computation occurs until main is invoked by the authorized runner.
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
static constexpr unsigned P=11,NR=6188,NC=4367,NH=22,TOTAL=NC+NH,NW=(TOTAL+63)/64;
static constexpr unsigned INV[11]={0,1,6,4,3,9,2,8,7,5,10};
static Clock::time_point started;
static double budget;
static void need(bool b,const string&s){if(!b)throw runtime_error(s);}
static double elapsed(){return chrono::duration<double>(Clock::now()-started).count();}
static void deadline(){if(elapsed()>budget)throw runtime_error("budget-exhausted");}
static uint8_t rd8(istream&f){char c;need(bool(f.get(c)),"Truncated input");return uint8_t(c);}
static uint16_t rd16(istream&f){unsigned a=rd8(f),b=rd8(f);return uint16_t(a|(b<<8));}
static uint32_t rd32(istream&f){uint32_t z=0;for(unsigned i=0;i<4;++i)z|=uint32_t(rd8(f))<<(8*i);return z;}
static void wr8(ostream&f,unsigned x){f.put(char(x));}
static void wr16(ostream&f,unsigned x){for(unsigned i=0;i<2;++i)wr8(f,(x>>(8*i))&255);}
static void wr32(ostream&f,uint32_t x){for(unsigned i=0;i<4;++i)wr8(f,(x>>(8*i))&255);}
static void wr64(ostream&f,uint64_t x){for(unsigned i=0;i<8;++i)wr8(f,unsigned((x>>(8*i))&255));}
struct Term{uint16_t col;uint8_t value;};
struct OriginalRow{vector<Term> terms;array<uint8_t,NH> rhs;};
using Packed=array<uint64_t,4*NW>;
static unsigned get(const Packed&r,unsigned c){
 unsigned w=c>>6,b=c&63;
 return unsigned((r[w]>>b)&1)+2*unsigned((r[NW+w]>>b)&1)
       +4*unsigned((r[2*NW+w]>>b)&1)+8*unsigned((r[3*NW+w]>>b)&1);
}
static void put(Packed&r,unsigned c,unsigned v){
 need(c<TOTAL&&v<11,"Bad packed coordinate");
 for(unsigned k=0;k<4;++k)if(v&(1u<<k))r[k*NW+(c>>6)]|=uint64_t(1)<<(c&63);
}
static void add(Packed&r,const Packed&q,unsigned w0){
 for(unsigned w=w0;w<NW;++w){
  uint64_t a0=r[w],a1=r[NW+w],a2=r[2*NW+w],a3=r[3*NW+w];
  uint64_t b0=q[w],b1=q[NW+w],b2=q[2*NW+w],b3=q[3*NW+w];
  uint64_t s0=a0^b0,c=a0&b0,x1=a1^b1,s1=x1^c;
  c=(a1&b1)|(x1&c);
  uint64_t x2=a2^b2,s2=x2^c;c=(a2&b2)|(x2&c);
  uint64_t x3=a3^b3,s3=x3^c,s4=(a3&b3)|(x3&c);
  uint64_t d0=~s0,borrow=~s0,d1=~(s1^borrow);borrow=~s1|borrow;
  uint64_t d2=s2^borrow;borrow=~s2&borrow;
  uint64_t d3=~(s3^borrow);borrow=~s3|borrow;
  uint64_t take=~(~s4&borrow);
  r[w]=s0^(take&(s0^d0));r[NW+w]=s1^(take&(s1^d1));
  r[2*NW+w]=s2^(take&(s2^d2));r[3*NW+w]=s3^(take&(s3^d3));
 }
}
static void test_add(){
 for(unsigned a=0;a<11;++a)for(unsigned b=0;b<11;++b){
  Packed x{},y{};for(unsigned c=0;c<TOTAL;++c){put(x,c,a);put(y,c,b);}
  add(x,y,0);
  for(unsigned c=0;c<TOTAL;++c)need(get(x,c)==(a+b)%11,"Bit-plane field-addition test");
  for(unsigned c=TOTAL;c<NW*64;++c){
   unsigned w=c>>6,bit=c&63;
   need(((x[w]|x[NW+w]|x[2*NW+w]|x[3*NW+w])&(uint64_t(1)<<bit))==0,"Padding test");
  }
 }
}
struct Pivot{array<Packed,10> multiples;uint16_t source;};
static unique_ptr<Pivot> make_pivot(const Packed&r,unsigned col,unsigned f,unsigned source){
 auto p=make_unique<Pivot>();p->source=uint16_t(source);
 array<Packed,10> all;all[0]=r;
 for(unsigned k=1;k<10;++k){all[k]=all[k-1];add(all[k],r,col>>6);}
 for(unsigned k=1;k<=10;++k){
  p->multiples[k-1]=all[(k*INV[f])%11-1];
  need(get(p->multiples[k-1],col)==k,"Normalized pivot multiple");
 }
 return p;
}
static vector<unsigned> rref(vector<vector<uint8_t>>&a,unsigned cols){
 vector<unsigned> piv;unsigned row=0;
 for(unsigned c=0;c<cols&&row<a.size();++c){
  unsigned p=row;while(p<a.size()&&!a[p][c])++p;if(p==a.size())continue;
  swap(a[p],a[row]);unsigned iv=INV[a[row][c]];
  for(unsigned j=c;j<cols;++j)a[row][j]=uint8_t(a[row][j]*iv%11);
  for(unsigned i=0;i<a.size();++i)if(i!=row&&a[i][c]){
   unsigned f=a[i][c];for(unsigned j=c;j<cols;++j)a[i][j]=uint8_t((a[i][j]+11-f*a[row][j]%11)%11);
  }
  piv.push_back(c);++row;
 }
 return piv;
}
static vector<vector<uint8_t>> kernel(const vector<vector<uint8_t>>&a,const vector<unsigned>&piv,unsigned cols){
 vector<bool> used(cols);for(unsigned c:piv)used[c]=true;
 vector<unsigned> free;for(unsigned c=0;c<cols;++c)if(!used[c])free.push_back(c);
 vector<vector<uint8_t>> h(cols,vector<uint8_t>(free.size()));
 for(unsigned j=0;j<free.size();++j){
  h[free[j]][j]=1;
  for(unsigned i=0;i<piv.size();++i)h[piv[i]][j]=uint8_t((11-a[i][free[j]])%11);
 }
 return h;
}
static void raw_header(ostream&f,const char*magic,const vector<unsigned>&dims,const string&binding){
 f.write(magic,8);for(unsigned x:dims)wr32(f,x);f.write(binding.data(),64);
}
int main(int argc,char**argv){
 started=Clock::now();
 try{
  need(argc==4,"Usage: native input.bin out-directory remaining-seconds");
  budget=stod(argv[3]);need(budget>0&&budget<=3600,"Finite positive native budget <=3600");
  fs::path out=argv[2];fs::create_directories(out);
  ifstream input(argv[1],ios::binary);need(bool(input),"Cannot open input");
  char magic[8];input.read(magic,8);need(string(magic,8)=="R150FJ11","Original input magic");
  need(rd32(input)==11&&rd32(input)==NR&&rd32(input)==NC&&rd32(input)==NH,"Original dimensions");
  string binding(64,' ');input.read(binding.data(),64);
  need(binding.find_first_not_of("0123456789abcdef")==string::npos,"Binding hexadecimal");
  vector<OriginalRow> original(NR);
  for(unsigned i=0;i<NR;++i){
   unsigned n=rd16(input);need(n<=77,"Original polynomial row support");
   int prev=-1;for(unsigned j=0;j<n;++j){
    unsigned c=rd16(input),v=rd8(input);need(c<NC&&int(c)>prev&&v>0&&v<11,"Ordered original row");
    original[i].terms.push_back({uint16_t(c),uint8_t(v)});prev=int(c);
   }
   for(unsigned j=0;j<NH;++j){unsigned v=rd8(input);need(v<11,"Original RHS coordinate");original[i].rhs[j]=uint8_t(v);}
  }
  vector<array<uint8_t,NH>> lambda(NC);
  for(unsigned i=0;i<NC;++i)for(unsigned j=0;j<NH;++j){
   unsigned v=rd8(input);need(v<11,"Constant head field coordinate");lambda[i][j]=uint8_t(v);
  }
  vector<unsigned> normalization(NH);
  vector<vector<uint8_t>> free_block(NH,vector<uint8_t>(NH));
  for(unsigned i=0;i<NH;++i){
   normalization[i]=rd16(input);need(normalization[i]<NC,"Constant head normalization index");
   for(unsigned j=0;j<NH;++j)free_block[i][j]=lambda[normalization[i]][j];
  }
  need(input.peek()==char_traits<char>::eof(),"Trailing input bytes");
  need(rref(free_block,NH).size()==NH,"Complete constant head unit block");
  for(unsigned i=0;i<NR;++i){
   array<uint32_t,NH> v{};
   for(auto t:original[i].terms)for(unsigned j=0;j<NH;++j)v[j]+=unsigned(t.value)*lambda[t.col][j];
   for(unsigned j=0;j<NH;++j)need(v[j]%11==0,"Full original constant-head product");
  }
  test_add();deadline();
  vector<unique_ptr<Pivot>> piv(NC);vector<vector<uint8_t>> residual;
  vector<unsigned> dependent_sources;
  uint64_t operations=0;unsigned rank_a=0;double last=elapsed();
  fs::path dagpath=out/"constant-source-row-operations.bin";
  ofstream dag(dagpath,ios::binary);need(bool(dag),"Cannot create original operations");
  raw_header(dag,"R15DAG11",{11,NR,NC,NH},binding);
  for(unsigned i=0;i<NR;++i){
   Packed row{};for(auto t:original[i].terms)put(row,t.col,t.value);
   for(unsigned j=0;j<NH;++j)put(row,NC+j,original[i].rhs[j]);
   vector<pair<uint16_t,uint8_t>> ops;int newcol=-1;unsigned first=0;
   for(unsigned w=0;w<(NC+63)/64&&newcol<0;++w){
    uint64_t mask=(w==NC/64&&NC%64)?((uint64_t(1)<<(NC%64))-1):~uint64_t(0);
    uint64_t nz=(row[w]|row[NW+w]|row[2*NW+w]|row[3*NW+w])&mask;
    while(nz){
     unsigned c=64*w+unsigned(__builtin_ctzll(nz));unsigned f=get(row,c);
     need(c<NC&&f>0&&f<11,"Actual constant pivot coordinate");
     if(!piv[c]){
      for(unsigned z=0;z<c;++z)need(get(row,z)==0,"Echelon prefix zero");
      piv[c]=make_pivot(row,c,f,i);newcol=int(c);first=f;++rank_a;break;
     }
     unsigned factor=11-f;add(row,piv[c]->multiples[factor-1],w);
     ops.emplace_back(uint16_t(c),uint8_t(factor));++operations;
     if((operations&16383)==0)deadline();
     nz=(row[w]|row[NW+w]|row[2*NW+w]|row[3*NW+w])&mask;
    }
   }
   wr32(dag,uint32_t(ops.size()));
   for(auto [c,f]:ops){wr16(dag,c);wr8(dag,f);}
   wr16(dag,newcol<0?65535:unsigned(newcol));wr8(dag,first);
   if(newcol<0){
    for(unsigned c=0;c<NC;++c)need(get(row,c)==0,"All dependent constant coordinates zero");
    vector<uint8_t> v(NH);for(unsigned j=0;j<NH;++j){unsigned x=get(row,NC+j);need(x<11,"Canonical residual");v[j]=uint8_t(x);}
    residual.push_back(move(v));dependent_sources.push_back(i);
   }
   if(elapsed()-last>=10){cerr<<"{\"phase\":\"original-constant-elimination\",\"sourceRows\":"<<i+1
       <<",\"constantRank\":"<<rank_a<<",\"rowAdditions\":"<<operations<<",\"seconds\":"<<elapsed()<<"}\n";last=elapsed();}
   deadline();
  }
  dag.close();need(bool(dag),"Operations write completion");
  need(rank_a+residual.size()==NR,"Every original source accounted");
  need(rank_a==NC-NH,"Constant rank is not4345; supplied22 heads are not a certified full field kernel");
  auto rr=residual;auto rp=rref(rr,NH);auto h=kernel(rr,rp,NH);
  unsigned rank_c=unsigned(rp.size()),nhead=NH-rank_c;
  for(auto &row:residual)for(unsigned j=0;j<nhead;++j){
   unsigned v=0;for(unsigned k=0;k<NH;++k)v+=unsigned(row[k])*h[k][j];
   need(v%11==0,"Complete residual kernel product");
  }
  vector<vector<uint8_t>> x(NC,vector<uint8_t>(nhead));
  for(int c=int(NC)-1;c>=0;--c)if(piv[c]){
   const Packed&r=piv[c]->multiples[0];array<uint32_t,NH> v{};
   for(unsigned k=0;k<NH;++k){unsigned f=get(r,NC+k);for(unsigned j=0;j<nhead;++j)v[j]+=f*h[k][j];}
   for(unsigned z=unsigned(c)+1;z<NC;++z){
    unsigned f=get(r,z);if(f)for(unsigned j=0;j<nhead;++j)v[j]+=f*x[z][j];
   }
   for(unsigned j=0;j<nhead;++j)x[c][j]=uint8_t((11-v[j]%11)%11);
   if((c&127)==0)deadline();
  }
  for(unsigned i=0;i<NR;++i){
   array<uint32_t,NH> v{};
   for(auto t:original[i].terms)for(unsigned j=0;j<nhead;++j)v[j]+=unsigned(t.value)*x[t.col][j];
   for(unsigned k=0;k<NH;++k)for(unsigned j=0;j<nhead;++j)v[j]+=unsigned(original[i].rhs[k])*h[k][j];
   for(unsigned j=0;j<nhead;++j)need(v[j]%11==0,"ALL ORIGINAL first-jet products");
  }
  deadline();
  ofstream lf(out/"field-original-first-lifts.bin",ios::binary);
  raw_header(lf,"R15B1F11",{11,NC,NH,nhead,rank_a,rank_c},binding);
  for(auto &row:h)for(unsigned v:row)wr8(lf,v);
  for(auto &row:x)for(unsigned v:row)wr8(lf,v);
  lf.close();need(bool(lf),"Lift output completion");
  ofstream rf(out/"field-complete-connection-residual.bin",ios::binary);
  raw_header(rf,"R15R1F11",{11,unsigned(residual.size()),NH},binding);
  for(unsigned i=0;i<residual.size();++i){wr16(rf,dependent_sources[i]);for(unsigned v:residual[i])wr8(rf,v);}
  rf.close();need(bool(rf),"Residual output completion");
  ofstream pf(out/"constant-normalized-pivot-rows.bin",ios::binary);
  raw_header(pf,"R15P1F11",{11,rank_a,NC,NH,NW},binding);
  for(unsigned c=0;c<NC;++c)if(piv[c]){
   wr16(pf,c);wr16(pf,piv[c]->source);
   for(uint64_t word:piv[c]->multiples[0])wr64(pf,word);
  }
  pf.close();need(bool(pf),"Pivot output completion");
  ofstream receipt(out/"native-first-connection-receipt.json");
  need(bool(receipt),"Native receipt output");
  receipt<<setprecision(17)
   <<"{\"format\":\"r150-full-original-first-connection-field11-v1\",\"status\":\"completed\","
   <<"\"binding\":\""<<binding<<"\",\"prime\":11,\"originalSourceRows\":6188,"
   <<"\"originalTargetCoordinates\":4367,\"constantKernelColumns\":22,"
   <<"\"constantRank\":"<<rank_a<<",\"dependentSourceRows\":"<<residual.size()
   <<",\"completeFirstConnectionRank\":"<<rank_c<<",\"fieldFirstHeadDimension\":"<<nhead
   <<",\"augmentedRank\":"<<rank_a+rank_c<<",\"rowAdditions\":"<<operations
   <<",\"allOriginalSourcesRetained\":true,\"allConstantColumnsRetained\":true,"
   <<"\"constantHeadFreeBlockUnit\":true,\"allOriginalConstantKernelProductsVerified\":true,"
   <<"\"constantKernelProductCoordinates\":"<<NR*NH
   <<",\"completeResidualKernelVerified\":true,\"allOriginalFirstJetProductsVerified\":true,"
   <<"\"firstJetFirstCoefficientProductCoordinates\":"<<NR*nhead
   <<",\"constantPivotOnly\":true,\"bitPlaneAll121AdditionIdentitiesVerified\":true,"
   <<"\"fieldCochaineOnlyNotRationalLifts\":true,\"temporaryOnly\":true,"
   <<"\"mathSeconds\":"<<elapsed()<<"}\n";
  receipt.close();need(bool(receipt),"Native receipt complete");
  ifstream done(out/"native-first-connection-receipt.json");cout<<done.rdbuf();
  return 0;
 }catch(const exception&e){
  cerr<<"native-first-connection-error: "<<e.what()<<"\n";
  return string(e.what())=="budget-exhausted"?124:1;
 }
}
