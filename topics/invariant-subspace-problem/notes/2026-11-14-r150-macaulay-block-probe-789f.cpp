// Exact F_31 discovery only.  No characteristic-zero inference is made here.
// Input: 17 rows, each with 11 linear then 66 quadratic coefficients in F_31.
// The original generator and all original coefficients are exported separately.
// Usage: probe DEG GENERATOR_COUNT DROP_LINEAR < input.txt
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <memory>
#include <unordered_map>
#include <vector>
using Row=std::vector<uint32_t>;
struct Rep { int c=0,rot=0,neg=0; };
int main(int argc,char**argv){
 if(argc!=4&&argc!=5)return 2;
 int D=std::stoi(argv[1]),ng=std::stoi(argv[2]),drop=std::stoi(argv[3]);
 if(D<2||D>5||(ng!=11&&ng!=17)||(drop!=0&&drop!=1))return 2;
 auto began=std::chrono::steady_clock::now();
 std::array<uint64_t,11> var;var[0]=1;for(int i=1;i<11;i++)var[i]=var[i-1]*8;
 std::vector<std::vector<uint64_t>> deg(D+1);
 auto rec=[&](auto&& self,int left,int lo,uint64_t key,int d)->void{
  if(!left){deg[d].push_back(key);return;}for(int i=lo;i<11;i++)self(self,left-1,i,key+var[i],d);
 };
 for(int d=0;d<=D;d++)rec(rec,d,0,0,d);
 std::vector<uint64_t> cols;std::vector<int> cdeg;
 for(int d=D;d>=1;d--)for(auto k:deg[d]){cols.push_back(k);cdeg.push_back(d);}
 std::unordered_map<uint64_t,int> ix;for(int j=0;j<(int)cols.size();j++)ix[cols[j]]=j;
 int nw=(cols.size()+31)/32;
 std::vector<std::vector<std::pair<uint64_t,int>>> eq(ng);
 for(int e=0;e<17;e++){
  for(int j=0;j<11;j++){int v;if(!(std::cin>>v))return 3;v=(v%31+31)%31;if(e<ng&&!drop&&v)eq[e].push_back({var[j],v});}
  for(int i=0;i<11;i++)for(int j=i;j<11;j++){int v;if(!(std::cin>>v))return 3;v=(v%31+31)%31;if(e<ng&&v)eq[e].push_back({var[i]+var[j],v});}
 }
 std::array<Rep,31> rep;std::array<int,31> inv;
 for(int c=0;c<3;c++)for(int rot=0;rot<5;rot++)for(int neg=0;neg<2;neg++){
  int v=((std::array<int,3>{1,3,5}[c]*(1<<rot)*(neg?-1:1))%31+31)%31;rep[v]={c,rot,neg};
 }
 for(int i=1;i<31;i++)for(int j=1;j<31;j++)if(i*j%31==1)inv[i]=j;
 auto addRot=[&](Row&r,const Row&q,int start,int rot,int neg){
  std::array<int,5> off;for(int i=0;i<5;i++)off[i]=((i-rot+5)%5)*nw;
  uint32_t mask=neg?UINT32_MAX:0;
  for(int w=start;w<nw;w++){
   uint32_t a0=r[w],a1=r[nw+w],a2=r[2*nw+w],a3=r[3*nw+w],a4=r[4*nw+w];
   uint32_t b0=q[off[0]+w]^mask,b1=q[off[1]+w]^mask,b2=q[off[2]+w]^mask,b3=q[off[3]+w]^mask,b4=q[off[4]+w]^mask;
   uint32_t s0=a0^b0,carry=a0&b0,x=a1^b1,s1=x^carry;carry=(a1&b1)|(x&carry);
   x=a2^b2;uint32_t s2=x^carry;carry=(a2&b2)|(x&carry);
   x=a3^b3;uint32_t s3=x^carry;carry=(a3&b3)|(x&carry);
   x=a4^b4;uint32_t s4=x^carry;carry=(a4&b4)|(x&carry);
   uint32_t t=s0^carry;carry&=s0;s0=t;t=s1^carry;carry&=s1;s1=t;t=s2^carry;carry&=s2;s2=t;t=s3^carry;carry&=s3;s3=t;s4^=carry;
   uint32_t keep=~(s0&s1&s2&s3&s4);r[w]=s0&keep;r[nw+w]=s1&keep;r[2*nw+w]=s2&keep;r[3*nw+w]=s3&keep;r[4*nw+w]=s4&keep;
  }
 };
 std::vector<std::unique_ptr<std::array<Row,3>>> piv(cols.size());
 std::vector<std::array<uint64_t,3>> chosen;
 int currentGenerator=0;uint64_t currentMultiplier=0;
 uint64_t ops=0;int rank=0,processed=0;
 auto reduce=[&](Row&r,bool insert){
  for(int w=0;w<nw;w++){
   uint32_t nz=r[w]|r[nw+w]|r[2*nw+w]|r[3*nw+w]|r[4*nw+w];
   while(nz){int bit=__builtin_ctz(nz),c=32*w+bit;if(c>=(int)cols.size())return -1;
    int f=0;for(int b=0;b<5;b++)f|=((r[b*nw+w]>>bit)&1)<<b;
    if(!piv[c]){
     if(insert){
      if(f!=1){auto R=rep[inv[f]];if(R.c){auto temp=r;addRot(r,temp,w,R.c==1?1:2,0);}
       for(int v=w;v<nw;v++){std::array<uint32_t,5>a;uint32_t u=0;for(int b=0;b<5;b++){a[b]=r[((b-R.rot+5)%5)*nw+v];u|=a[b];}for(int b=0;b<5;b++)r[b*nw+v]=a[b]^(R.neg?u:0);}
      }
      auto p=std::make_unique<std::array<Row,3>>();(*p)[0]=r;(*p)[1]=r;(*p)[2]=r;addRot((*p)[1],r,w,1,0);addRot((*p)[2],r,w,2,0);piv[c]=std::move(p);rank++;
      chosen.push_back({uint64_t(currentGenerator),currentMultiplier,cols[c]});
     }return c;
    }
    auto R=rep[31-f];addRot(r,(*piv[c])[R.c],w,R.rot,R.neg);ops++;
    nz=r[w]|r[nw+w]|r[2*nw+w]|r[3*nw+w]|r[4*nw+w];
   }
  }return -1;
 };
 for(int d=0;d<=D-2;d++)for(int e=0;e<ng;e++)for(auto mult:deg[d]){
  currentGenerator=e;currentMultiplier=mult;
  Row r(5*nw);for(auto [key,v]:eq[e]){int c=ix.at(key+mult),w=c/32;uint32_t b=uint32_t(1)<<(c%32);for(int k=0;k<5;k++)if(v&(1<<k))r[k*nw+w]|=b;}
  reduce(r,true);processed++;
 }
 if(argc==5){std::ofstream out(argv[4]);if(!out)return 4;
  out<<"{\"format\":\"r150-graded-pivot-profile-v1\",\"field\":31,\"D\":"<<D<<",\"generators\":"<<ng<<",\"dropLinear\":"<<drop<<",\"keyEncoding\":\"sum exponent_i*8^i; original m coordinates; generators indexed 0..16\",\"selectedRows\":[";
  for(size_t i=0;i<chosen.size();i++){auto a=chosen[i];out<<(i?",":"")<<"["<<a[0]<<","<<a[1]<<","<<a[2]<<"]";}out<<"]}\n";
 }
 std::vector<int> counts(D+1);for(int c=0;c<(int)cols.size();c++)if(piv[c])counts[cdeg[c]]++;
 std::cout<<"{\"field\":31,\"D\":"<<D<<",\"generators\":"<<ng<<",\"dropLinear\":"<<drop<<",\"rows\":"<<processed<<",\"columns\":"<<cols.size()<<",\"rank\":"<<rank<<",\"ops\":"<<ops<<",\"pivotsByDegree\":[";
 for(int d=1;d<=D;d++)std::cout<<(d>1?",":"")<<counts[d];
 std::cout<<"],\"linearMembership\":[";for(int i=0;i<11;i++){Row r(5*nw);int c=ix.at(var[i]);r[c/32]|=uint32_t(1)<<(c%32);std::cout<<(i?",":"")<<(reduce(r,false)<0?"true":"false");}
 std::cout<<"],\"squareMembership\":[";for(int i=0;i<11;i++){Row r(5*nw);int c=ix.at(2*var[i]);r[c/32]|=uint32_t(1)<<(c%32);std::cout<<(i?",":"")<<(reduce(r,false)<0?"true":"false");}
 std::cout<<"],\"elapsedSeconds\":"<<std::chrono::duration<double>(std::chrono::steady_clock::now()-began).count()<<"}\n";
}
