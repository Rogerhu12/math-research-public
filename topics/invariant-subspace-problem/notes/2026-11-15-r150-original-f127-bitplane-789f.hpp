// Fixed F_127 Mersenne bit-plane arithmetic; independent from all F_31 data.
// Author: Astra-ISP-789f / normal_annihilator.
// AI-assisted: GPT-6 Astra Pro. Date: 2026-11-15.
#ifndef R150_ORIGINAL_F127_BITPLANE_789F_HPP
#define R150_ORIGINAL_F127_BITPLANE_789F_HPP
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <stdexcept>
#include <string>
#include <vector>
using Row=std::vector<uint32_t>;
using Triple=std::array<Row,9>;
struct Rep {int c=0,rot=0,neg=0;};
struct Source {int e=0,raw=0;uint64_t mult=0,pivot=0;};
static void u16(std::ostream&o,uint16_t x){o.put(char(x));o.put(char(x>>8));}
static void u32(std::ostream&o,uint32_t x){for(int j=0;j<4;j++)o.put(char(x>>(8*j)));}
static void u64(std::ostream&o,uint64_t x){for(int j=0;j<8;j++)o.put(char(x>>(8*j)));}
static uint64_t read_le(std::istream&i,int n){
 uint64_t v=0;for(int j=0;j<n;j++){int c=i.get();if(c<0)throw std::runtime_error("truncated integer");v|=uint64_t(c)<<(8*j);}return v;
}
static int degree(uint64_t k){int d=0;while(k){d+=k%8;k/=8;}return d;}
struct BitOps {
 static constexpr int prime=127,planes=7,classes=9;
 static constexpr std::array<int,9> bases={1,3,5,7,9,11,13,19,21};
 std::array<Rep,127> rep{};
 std::array<int,127> inv{};
 BitOps(){
  std::array<bool,127> covered{};
  for(int c=0;c<9;c++)for(int r=0;r<7;r++)for(int n=0;n<2;n++){
   int v=((bases[c]*(1<<r)*(n?-1:1))%127+127)%127;
   if(!v||covered[v])throw std::runtime_error("F127 coset partition");
   covered[v]=true;rep[v]={c,r,n};
  }
  for(int i=1;i<127;i++){
   if(!covered[i])throw std::runtime_error("F127 missing scalar");
   for(int j=1;j<127;j++)if(i*j%127==1)inv[i]=j;
   if(!inv[i])throw std::runtime_error("F127 inverse");
  }
 }
 static int get(const Row&r,int nw,int bit){
  int v=0;for(int b=0;b<7;b++)v|=((r[b*nw+bit/32]>>(bit%32))&1)<<b;
  return v;
 }
 static void set(Row&r,int nw,int bit,int v){
  v=(v%127+127)%127;uint32_t mask=uint32_t(1)<<(bit%32);
  for(int b=0;b<7;b++){
   auto &word=r[b*nw+bit/32];word=(word&~mask)|((v&(1<<b))?mask:0);
  }
 }
 static void add(Row&r,int rw,int ro,const Row&q,int qw,int qo,int len,int rot,int neg){
  int off[7];for(int b=0;b<7;b++)off[b]=((b-rot+7)%7)*qw+qo;
  const uint32_t mask=neg?UINT32_MAX:0;
  for(int w=0;w<len;w++){
   uint32_t sum[7],carry=0;
   for(int b=0;b<7;b++){
    uint32_t a=r[b*rw+ro+w],v=q[off[b]+w]^mask,x=a^v;
    sum[b]=x^carry;carry=(a&v)|(x&carry);
   }
   for(int b=0;b<7;b++){
    uint32_t old=sum[b];sum[b]^=carry;carry&=old;
   }
   uint32_t full=UINT32_MAX;for(int b=0;b<7;b++)full&=sum[b];
   for(int b=0;b<7;b++)r[b*rw+ro+w]=sum[b]&~full;
  }
 }
 void multiple(Row&r,int nw,int first,int a)const{
  if(a<1||a>=127)throw std::runtime_error("F127 nonzero multiplication");
  Row original=r;
  for(int b=0;b<7;b++)std::fill(r.begin()+b*nw+first,r.begin()+(b+1)*nw,0);
  for(int k=0;k<7;k++)if(a&(1<<k))add(r,nw,first,original,nw,first,nw-first,k,0);
 }
 static void refresh(Triple&t,int nw,int first){
  for(int c=1;c<9;c++){
   t[c]=t[0];
   for(int k=1;k<7;k++)if(bases[c]&(1<<k))
    add(t[c],nw,first,t[0],nw,first,nw-first,k,0);
  }
 }
 uint64_t verify()const{
  uint64_t count=0;
  // Exhaustively compare independent scalar arithmetic at every field value,
  // including distinct strides, offsets, rotations, signs and padding words.
  for(int a=0;a<127;a++)for(int start=0;start<127;start+=32)
   for(int rot=0;rot<7;rot++)for(int neg=0;neg<2;neg++){
    Row r(21),q(28);
    for(int lane=0;lane<32;lane++){
     set(r,3,32+lane,a);set(q,4,64+lane,(start+lane)%127);
     set(r,3,lane,17);set(r,3,64+lane,29);
    }
    add(r,3,1,q,4,2,1,rot,neg);
    for(int lane=0;lane<32;lane++){
     int b=(start+lane)%127;
     int expected=(a+(neg?-1:1)*b*(1<<rot))%127;if(expected<0)expected+=127;
     if(get(r,3,32+lane)!=expected||get(r,3,lane)!=17||get(r,3,64+lane)!=29)
      throw std::runtime_error("F127 exhaustive scalar addition test");
     count++;
    }
   }
  Row original(28);
  for(int i=0;i<128;i++)set(original,4,i,i%127);
  for(int a=1;a<127;a++){
   Row r=original;multiple(r,4,0,a);
   for(int i=0;i<128;i++){if(get(r,4,i)!=(i%127)*a%127)throw std::runtime_error("F127 scalar multiplication test");count++;}
  }
  Triple cached;cached[0]=original;refresh(cached,4,0);
  for(int c=0;c<9;c++)for(int i=0;i<128;i++){
   if(get(cached[c],4,i)!=(i%127)*bases[c]%127)throw std::runtime_error("F127 cached scalar test");
   count++;
  }
  for(int a=1;a<127;a++){
   const auto v=rep[a];
   int represented=bases[v.c]*(1<<v.rot)*(v.neg?-1:1);
   if((represented%127+127)%127!=a||a*inv[a]%127!=1)throw std::runtime_error("F127 exact scalar table test");
   count++;
  }
  return count;
 }
};
#endif
