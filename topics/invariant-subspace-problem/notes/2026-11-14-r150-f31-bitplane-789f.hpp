// Exact F_31[s] normal forms for the original finite degree-five Macaulay module.
// The fixed m-degree constant leading blocks are reduced backwards, but their
// lower-degree parameter tails are never reduced while constructing the basis.
// All transformations and all normal-form reductions have replayable sources.
// Usage: PROGRAM INPUT OUT_PREFIX [forward|rref]
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
using Row = std::vector<uint32_t>;
using Triple = std::array<Row,3>;
struct Rep {int c=0,rot=0,neg=0;};
struct Source {int e=0,raw=0; uint64_t mult=0,pivot=0;};
static void u32(std::ostream &o,uint32_t x){for(int j=0;j<4;j++)o.put(char(x>>(8*j)));}
static void u16(std::ostream &o,uint16_t x){o.put(char(x));o.put(char(x>>8));}
static int degree(uint64_t k){int d=0;while(k){d+=k%8;k/=8;}return d;}
struct BitOps {
 std::array<Rep,31> rep;
 std::array<int,31> inv{};
 BitOps(){
  for(int c=0;c<3;c++)for(int r=0;r<5;r++)for(int n=0;n<2;n++){
   int v=((std::array<int,3>{1,3,5}[c]*(1<<r)*(n?-1:1))%31+31)%31;
   rep[v]={c,r,n};
  }
  for(int i=1;i<31;i++)for(int j=1;j<31;j++)if(i*j%31==1)inv[i]=j;
 }
 static int get(const Row &r,int nw,int bit){
  int v=0;for(int b=0;b<5;b++)v|=((r[b*nw+bit/32]>>(bit%32))&1)<<b;return v;
 }
 static void set(Row &r,int nw,int bit,int v){
  v=(v%31+31)%31;for(int b=0;b<5;b++)if(v&(1<<b))r[b*nw+bit/32]|=uint32_t(1)<<(bit%32);
 }
 // The source and destination blocks may have different strides. Offsets and
 // lengths are in 32-entry words, so polynomial-degree shifts remain exact.
 static void add(Row &r,int rw,int ro,const Row &q,int qw,int qo,int len,int rot,int neg){
  int off[5];for(int j=0;j<5;j++)off[j]=((j-rot+5)%5)*qw+qo;
  const uint32_t mask=neg?UINT32_MAX:0;
  for(int w=0;w<len;w++){
   const int z=ro+w;
   uint32_t a0=r[z],a1=r[rw+z],a2=r[2*rw+z],a3=r[3*rw+z],a4=r[4*rw+z];
   uint32_t b0=q[off[0]+w]^mask,b1=q[off[1]+w]^mask,b2=q[off[2]+w]^mask,b3=q[off[3]+w]^mask,b4=q[off[4]+w]^mask;
   uint32_t s0=a0^b0,c=a0&b0,x=a1^b1,s1=x^c;c=(a1&b1)|(x&c);
   x=a2^b2;uint32_t s2=x^c;c=(a2&b2)|(x&c);x=a3^b3;uint32_t s3=x^c;c=(a3&b3)|(x&c);
   x=a4^b4;uint32_t s4=x^c;c=(a4&b4)|(x&c);
   uint32_t t=s0^c;c&=s0;s0=t;t=s1^c;c&=s1;s1=t;t=s2^c;c&=s2;s2=t;t=s3^c;c&=s3;s3=t;s4^=c;
   uint32_t keep=~(s0&s1&s2&s3&s4);
   r[z]=s0&keep;r[rw+z]=s1&keep;r[2*rw+z]=s2&keep;r[3*rw+z]=s3&keep;r[4*rw+z]=s4&keep;
  }
 }
 void multiple(Row &r,int nw,int first,int a) const {
  const Rep R=rep[a];
  if(R.c){Row tmp=r;add(r,nw,first,tmp,nw,first,nw-first,R.c==1?1:2,0);}
  for(int w=first;w<nw;w++){
   uint32_t x[5],nz=0;for(int b=0;b<5;b++){x[b]=r[((b-R.rot+5)%5)*nw+w];nz|=x[b];}
   for(int b=0;b<5;b++)r[b*nw+w]=x[b]^(R.neg?nz:0);
  }
 }
 static void refresh(Triple &t,int nw,int first){
  t[1]=t[0];t[2]=t[0];add(t[1],nw,first,t[0],nw,first,nw-first,1,0);add(t[2],nw,first,t[0],nw,first,nw-first,2,0);
 }
};
