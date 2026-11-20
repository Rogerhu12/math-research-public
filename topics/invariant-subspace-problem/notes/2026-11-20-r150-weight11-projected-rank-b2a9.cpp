// Exact F127 row-projected original weight-eleven augmented rank.
// Author: Astra-ISP-b2a9acde-20261120 / root. AI-assisted GPT-6 Astra Pro.
// Input retains all original Gamma200 vectors; projection is a fixed linear
// map on all 150646 original coordinates, used only for rank LOWER bounds.
// All arrays and pivot records are temporary; only run identities/hashes persist.
#include "2026-11-15-r150-original-f127-bitplane-789f.hpp"
#include <chrono>
#include <cstring>
#include <filesystem>
#include <iostream>
#include <numeric>
#include <random>
#include <stdexcept>
#include <unordered_map>
using Clock=std::chrono::steady_clock;
static void need(bool b,const std::string&s){if(!b)throw std::runtime_error(s);}
static constexpr int RW[10]={0,2,2,2,2,2,4,4,4,4};
static constexpr int VW[12]={1,1,1,1,1,1,2,2,2,2,2,2};
static uint64_t mix64(uint64_t z){
 z+=UINT64_C(0x9e3779b97f4a7c15);z=(z^(z>>30))*UINT64_C(0xbf58476d1ce4e5b9);
 z=(z^(z>>27))*UINT64_C(0x94d049bb133111eb);return z^(z>>31);
}
static void recmono(int i,int left,uint64_t code,std::vector<uint64_t>&v){
 if(i==12){if(!left)v.push_back(code);return;}
 for(int e=0;e*VW[i]<=left;++e)recmono(i+1,left-e*VW[i],code|(uint64_t(e)<<(5*i)),v);
}
static int wt(uint64_t code){
 need((code>>60)==0,"all twelve exponent lanes");
 int t=0;for(int i=0;i<12;i++){int e=(code>>(5*i))&31;need(e<=11,"weight-eleven exponent");t+=VW[i]*e;}return t;
}
struct Counts{
 uint64_t cancellations=0,passes=0,words=0,normalizations=0;
 void add(const Counts&x){cancellations+=x.cancellations;passes+=x.passes;words+=x.words;normalizations+=x.normalizations;}
};
struct Scaled{
 const BitOps&ops;Counts&attempt;
 explicit Scaled(const BitOps&o,Counts&a):ops(o),attempt(a){}
 void add(Row&r,int rw,int ro,const Row&q,int qw,int qo,int len,int scalar,Counts&local)const{
  need(scalar>0&&scalar<127&&(&r!=&q),"literal nonzero scalar and distinct input");
  static constexpr int length[9]={1,2,2,2,2,3,3,3,3};
  static constexpr int shifts[9][3]={{0,0,0},{0,1,0},{0,2,0},{3,0,0},{0,3,0},{0,1,3},{0,2,3},{0,1,4},{0,2,4}};
  static constexpr int signs[9][3]={{0,0,0},{0,0,0},{0,0,0},{0,1,0},{0,0,0},{0,0,0},{0,0,0},{0,0,0},{0,0,0}};
  auto v=ops.rep[scalar];
  for(int k=0;k<length[v.c];k++){
   BitOps::add(r,rw,ro,q,qw,qo,len,(v.rot+shifts[v.c][k])%7,v.neg^signs[v.c][k]);
   local.passes++;local.words+=len;attempt.passes++;attempt.words+=len;
  }
 }
 void normalize(Row&r,int nw,int first,int scalar,Counts&local)const{
  need(scalar>0&&scalar<127,"normalization scalar");
  local.normalizations++;attempt.normalizations++;if(scalar==1)return;
  Row original=r;for(int b=0;b<7;b++)std::fill(r.begin()+b*nw+first,r.begin()+(b+1)*nw,0);
  add(r,nw,first,original,nw,first,nw-first,scalar,local);
 }
};

struct Pivot{uint32_t row,id;uint8_t factor;Row data;};
struct Elimination{
 int m,nw;BitOps ops;Counts count;Scaled scaled;
 std::vector<Pivot> pivots;std::vector<int> at;int determinant=1;
 Clock::time_point deadline;
 explicit Elimination(int mm,double seconds):m(mm),nw((mm+31)/32),scaled(ops,count),at(mm,-1),
  deadline(Clock::now()+std::chrono::duration_cast<Clock::duration>(std::chrono::duration<double>(seconds))){}
 int first(const Row&r,int start)const{
  if(start>=m)return m;
  for(int w=start/32;w<nw;w++){
   uint32_t z=0;for(int b=0;b<7;b++)z|=r[b*nw+w];
   if(w==start/32)z&=UINT32_MAX<<(start%32);
   if(z){int p=w*32+__builtin_ctz(z);need(p<m,"zero unused output bits");return p;}
  }return m;
 }
 bool insert(Row r,uint32_t id){
  int p=0,iterations=0;Counts local;
  while((p=first(r,p))<m){
   if((iterations++&31)==0)need(Clock::now()<deadline,"arithmetic time budget exhausted");
   int value=BitOps::get(r,nw,p),k=at[p];
   if(k>=0){
    scaled.add(r,nw,p/32,pivots[k].data,nw,p/32,nw-p/32,127-value,local);
    need(BitOps::get(r,nw,p)==0,"exact physical projected pivot cancellation");
    ++count.cancellations;++p;continue;
   }
   scaled.normalize(r,nw,p/32,ops.inv[value],local);
   need(first(r,0)==p&&BitOps::get(r,nw,p)==1,"complete normalized pivot");
   determinant=determinant*value%127;at[p]=int(pivots.size());
   pivots.push_back({uint32_t(p),id,uint8_t(value),std::move(r)});return true;
  }return false;
 }
};
struct Term{uint64_t code;uint8_t value;};
struct Vector{uint32_t weight;std::vector<Term> terms;};
struct Projection{
 int rows,hashes,nw;uint64_t seed;uint32_t epoch=0;
 std::vector<uint8_t> values;std::vector<uint32_t> seen,touched;
 Projection(int rr,int hh,uint64_t ss):rows(rr),hashes(hh),nw((rr+31)/32),seed(ss),values(rr),seen(rr){}
 std::pair<uint32_t,int> slot(uint64_t code,int h)const{
  uint64_t z=mix64(code^seed^(UINT64_C(0xd1b54a32d192ed03)*uint64_t(h+1)));
  return {uint32_t(z%rows),1+int((z>>32)%126)};
 }
 Row apply(const std::vector<Term>&v,uint64_t multiplier=0){
  need(++epoch!=0,"bounded projection epoch");touched.clear();
  for(auto t:v){
   uint64_t key=(((t.code>>4)+multiplier)<<4)|(t.code&15);
   for(int h=0;h<hashes;h++){
    auto [row,a]=slot(key,h);
    if(seen[row]!=epoch){seen[row]=epoch;values[row]=0;touched.push_back(row);}
    values[row]=(int(values[row])+a*int(t.value))%127;
   }
  }
  Row out(7*nw);for(uint32_t r:touched)if(values[r])BitOps::set(out,nw,r,values[r]);
  return out;
 }
};
static int scalar_rank(std::vector<std::vector<int>> a){
 if(a.empty())return 0;int k=0;
 for(int j=0;j<int(a[0].size())&&k<int(a.size());j++){
  int p=k;while(p<int(a.size())&&!a[p][j])p++;if(p==int(a.size()))continue;
  std::swap(a[k],a[p]);int iv=1;while(iv*a[k][j]%127!=1)iv++;
  for(int q=j;q<int(a[0].size());q++)a[k][q]=a[k][q]*iv%127;
  for(int i=k+1;i<int(a.size());i++){int b=a[i][j];for(int q=j;q<int(a[0].size());q++)a[i][q]=(a[i][q]-b*a[k][q]%127+127)%127;}k++;
 }return k;
}
static int scalar_det(std::vector<std::vector<int>> a){
 int out=1;
 for(int j=0;j<int(a.size());j++){
  int p=j;while(p<int(a.size())&&!a[p][j])p++;if(p==int(a.size()))return 0;
  if(p!=j){std::swap(a[p],a[j]);out=127-out;}int q=a[j][j];out=out*q%127;
  int iv=1;while(iv*q%127!=1)iv++;
  for(int i=j+1;i<int(a.size());i++){int b=a[i][j]*iv%127;for(int k=j;k<int(a.size());k++)a[i][k]=(a[i][k]-b*a[j][k]%127+127)%127;}
 }return out;
}
static void selftest(){
 std::mt19937 rng(1729);uint64_t checked=0;
 for(int rows:{63,96,129}){
  Projection projection(rows,5,UINT64_C(0x4252414e43483131));Elimination e(rows,30);
  std::vector<std::vector<int>> matrix(rows,std::vector<int>(37));
  for(int j=0;j<37;j++){
   std::vector<Term> v;for(uint64_t k=0;k<113;k++)if(rng()%4)v.push_back({(k<<4)|uint64_t(k%10),uint8_t(1+rng()%126)});
   Row row=projection.apply(v);
   std::vector<int> ordinary(rows);
   for(auto t:v)for(int h=0;h<5;h++){auto [i,c]=projection.slot(t.code,h);ordinary[i]=(ordinary[i]+c*t.value)%127;}
   for(int i=0;i<rows;i++){need(BitOps::get(row,e.nw,i)==ordinary[i],"new full projection/scalar comparison");matrix[i][j]=ordinary[i];checked++;}
   e.insert(std::move(row),j);
  }
  need(int(e.pivots.size())==scalar_rank(matrix),"new bitplane rank versus ordinary scalar rank");
  int r=e.pivots.size();std::vector<std::vector<int>> unit(r,std::vector<int>(r));
  for(int i=0;i<r;i++)for(int j=0;j<r;j++)unit[i][j]=matrix[e.pivots[i].row][e.pivots[j].id];
  need(scalar_det(unit)==e.determinant,"new selected unit determinant in arrival order");checked++;
 }
 std::cout<<"{\"kind\":\"new_projection_controls\",\"passed\":true,\"scalar_coordinates\":"<<checked<<"}\n";
}
int main(int argc,char**argv){
 try{
  if(argc==2&&std::string(argv[1])=="--selftest"){selftest();return 0;}
  need(argc==4,"input pivot-records seconds");
  auto start=Clock::now();std::ifstream f(argv[1],std::ios::binary);need(bool(f),"input open");
  char magic[8];f.read(magic,8);need(std::memcmp(magic,"ISP11P01",8)==0,"input protocol");
  uint32_t version=read_le(f,4),prime=read_le(f,4),weight=read_le(f,4),fullRows=read_le(f,4),sourceCols=read_le(f,4),generators=read_le(f,4),targets=read_le(f,4),projectedRows=read_le(f,4),hashes=read_le(f,4);
  uint64_t seed=read_le(f,8);
  need(version==1&&prime==127&&weight==11&&fullRows==150646&&sourceCols==37568&&generators==200&&targets==4,"complete original weight-eleven dimensions");
  need(projectedRows==40000&&hashes==5&&seed==UINT64_C(0x4252414e43483131),"fixed linear projection parameters");
  std::array<std::vector<uint64_t>,12> mono;for(int w=0;w<=11;w++){recmono(0,w,0,mono[w]);std::sort(mono[w].begin(),mono[w].end());}
  size_t totalRows=0;for(int k=0;k<10;k++)totalRows+=mono[11-RW[k]].size();need(totalRows==fullRows,"all original output coordinates counted");
  std::vector<Vector> vectors;std::array<int,12> profile{};uint64_t terms=0;size_t labels=0;
  for(uint32_t g=0;g<generators+targets;g++){
   need(read_le(f,4)==g,"all source and target labels");uint32_t w=read_le(f,4);uint64_t n=read_le(f,8);
   need(n<=150646&&((g<200&&w>=5&&w<=10)||(g>=200&&w==11)),"source or exact target weight");
   Vector v{w,{}};v.terms.reserve(n);uint64_t prev=0;
   for(uint64_t j=0;j<n;j++){
    uint64_t code=read_le(f,8);uint8_t a=read_le(f,1);uint32_t axis=code&15;
    need(axis<10&&a>0&&a<127&&(!j||code>prev)&&wt(code>>4)+RW[axis]==int(w),"complete canonical original coefficient");
    if(g>=200)need(axis==0,"canonical q*b^3 e0 target");
    v.terms.push_back({code,a});prev=code;
   }
   if(g<200){profile[w]++;labels+=mono[11-w].size();terms+=n;}vectors.push_back(std::move(v));
  }
  need(f.peek()==EOF&&labels==sourceCols&&terms==8037189,"entire original source coefficient stream and EOF");
  need(profile[5]==6&&profile[6]==20&&profile[7]==30&&profile[8]==40&&profile[9]==24&&profile[10]==80,"full original Gamma200 profile");
  Projection projection(projectedRows,hashes,seed);Elimination elimination(projectedRows,std::stod(argv[3]));elimination.pivots.reserve(sourceCols+4);
  uint32_t col=0;
  for(int g=0;g<200;g++)for(uint64_t multiplier:mono[11-vectors[g].weight]){
   elimination.insert(projection.apply(vectors[g].terms,multiplier),col++);
   if(col%512==0)std::cout<<"{\"kind\":\"weight11_progress\",\"columns\":"<<col<<",\"rank\":"<<elimination.pivots.size()<<",\"seconds\":"<<std::chrono::duration<double>(Clock::now()-start).count()<<"}"<<std::endl;
  }
  need(col==sourceCols,"all complete original source columns processed");
  size_t sourceRank=elimination.pivots.size();need(sourceRank<=36782,"independent original characteristic-zero ceiling");
  std::array<size_t,4> augmented{};
  for(int t=0;t<4;t++){elimination.insert(projection.apply(vectors[200+t].terms),col++);augmented[t]=elimination.pivots.size();}
  std::ofstream out(argv[2],std::ios::binary);need(bool(out),"temporary selected projected minor records");
  out.write("ISP11U01",8);u32(out,elimination.pivots.size());
  for(const auto&v:elimination.pivots){u32(out,v.row);u32(out,v.id);out.put(char(v.factor));}
  out.close();need(bool(out),"whole temporary minor records");
  std::cout<<"{\"kind\":\"weight11_projected_augmented_result\",\"complete_original_sources\":true,\"source_rank_lower_bound\":"<<sourceRank
   <<",\"augmented_rank_lower_bounds\":["<<augmented[0]<<","<<augmented[1]<<","<<augmented[2]<<","<<augmented[3]<<"],\"selected_projected_minor_det127\":"<<elimination.determinant
   <<",\"original_source_columns\":"<<sourceCols<<",\"projection_rows\":"<<projectedRows<<",\"hashes_per_original_row\":"<<hashes
   <<",\"cancellations\":"<<elimination.count.cancellations<<",\"elapsed_seconds\":"<<std::chrono::duration<double>(Clock::now()-start).count()
   <<",\"four_class_threshold_reached\":"<<(augmented[3]>=36786?"true":"false")<<"}"<<std::endl;
  return 0;
 }catch(const std::exception&e){std::cerr<<"weight11_exact_error: "<<e.what()<<std::endl;return 1;}
}
