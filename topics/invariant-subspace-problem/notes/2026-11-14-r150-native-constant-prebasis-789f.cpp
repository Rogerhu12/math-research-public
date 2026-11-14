// Original constant-Q block Gaussian elimination over F_31.
// Payload is the complete original parameter-linear part (degree <=10 in s).
// No reduction by lower m-degree pivots: each output vector has m-degrees d,d-1.
// Usage: native-prebasis INPUT BASIS.sing SOURCE_OPERATIONS.bin
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <memory>
#include <unordered_map>
#include <vector>
using Row=std::vector<uint32_t>;
struct Rep {int c=0,rot=0,neg=0;};
struct Source {int e,raw;uint64_t mult,pivot;};
static void u32(std::ostream&o,uint32_t x){for(int j=0;j<4;j++)o.put(char((x>>(8*j))&255));}
static void u16(std::ostream&o,uint16_t x){o.put(char(x&255));o.put(char(x>>8));}
int main(int argc,char**argv){
 if(argc!=4)return 2;auto start=std::chrono::steady_clock::now();
 std::ifstream in(argv[1]);std::ofstream out(argv[2]),opsout(argv[3],std::ios::binary);if(!in||!out||!opsout)return 3;
 std::array<std::array<int,66>,11> Q;std::array<std::array<std::array<int,11>,11>,11>L;
 for(int e=0;e<11;e++){for(int j=0;j<66;j++)if(!(in>>Q[e][j]))return 4;for(int v=0;v<11;v++)for(int k=0;k<11;k++)if(!(in>>L[e][v][k]))return 4;}
 int ns;if(!(in>>ns)||ns!=3333)return 4;std::vector<Source> sources(ns);
 for(auto &a:sources)if(!(in>>a.e>>a.mult>>a.pivot>>a.raw)||a.e<0||a.e>=11||a.raw<1||a.raw>6188)return 4;
 std::array<uint64_t,11> var;var[0]=1;for(int i=1;i<11;i++)var[i]=8*var[i-1];
 std::vector<std::vector<uint64_t>> degree(6);
 auto rec=[&](auto&&self,int left,int lo,uint64_t key,int d)->void{if(!left){degree[d].push_back(key);return;}for(int j=lo;j<11;j++)self(self,left-1,j,key+var[j],d);};
 for(int d=0;d<=5;d++)rec(rec,d,0,0,d);
 std::unordered_map<uint64_t,int> global;int gi=1;for(int d=5;d>=1;d--)for(auto key:degree[d])global[key]=gi++;
 auto getdeg=[](uint64_t k){int d=0;while(k){d+=k%8;k/=8;}return d;};
 std::vector<std::pair<int,int>> qm;for(int i=0;i<11;i++)for(int j=i;j<11;j++)qm.push_back({i,j});
 std::array<Rep,31> rep;std::array<int,31> inv;
 for(int c=0;c<3;c++)for(int rot=0;rot<5;rot++)for(int neg=0;neg<2;neg++){int v=((std::array<int,3>{1,3,5}[c]*(1<<rot)*(neg?-1:1))%31+31)%31;rep[v]={c,rot,neg};}
 for(int i=1;i<31;i++)for(int j=1;j<31;j++)if(i*j%31==1)inv[i]=j;
 out<<"// F31[s], original m-monomial component order; replayable source operations accompany this file.\nmodule B0;\n";
 opsout.write("R150PB31",8);u32(opsout,3333);uint64_t operations=0,nonzeroCoefficients=0;int generated=0;
 for(int d=2;d<=5;d++){
  const int hi=degree[d].size(),lo=degree[d-1].size(),width=hi+11*lo,nw=(width+31)/32;
  std::unordered_map<uint64_t,int> highIndex,lowIndex;for(int j=0;j<hi;j++)highIndex[degree[d][j]]=j;for(int j=0;j<lo;j++)lowIndex[degree[d-1][j]]=j;
  std::vector<std::unique_ptr<std::array<Row,3>>> piv(hi);std::vector<int> basisIndex(hi);int phaseCount=0;
  auto addRot=[&](Row&r,const Row&q,int first,int rot,int neg){
   int off[5];for(int j=0;j<5;j++)off[j]=((j-rot+5)%5)*nw;uint32_t mask=neg?UINT32_MAX:0;
   for(int w=first;w<nw;w++){
    uint32_t a0=r[w],a1=r[nw+w],a2=r[2*nw+w],a3=r[3*nw+w],a4=r[4*nw+w],b0=q[off[0]+w]^mask,b1=q[off[1]+w]^mask,b2=q[off[2]+w]^mask,b3=q[off[3]+w]^mask,b4=q[off[4]+w]^mask;
    uint32_t s0=a0^b0,carry=a0&b0,x=a1^b1,s1=x^carry;carry=(a1&b1)|(x&carry);x=a2^b2;uint32_t s2=x^carry;carry=(a2&b2)|(x&carry);x=a3^b3;uint32_t s3=x^carry;carry=(a3&b3)|(x&carry);x=a4^b4;uint32_t s4=x^carry;carry=(a4&b4)|(x&carry);
    uint32_t t=s0^carry;carry&=s0;s0=t;t=s1^carry;carry&=s1;s1=t;t=s2^carry;carry&=s2;s2=t;t=s3^carry;carry&=s3;s3=t;s4^=carry;uint32_t keep=~(s0&s1&s2&s3&s4);
    r[w]=s0&keep;r[nw+w]=s1&keep;r[2*nw+w]=s2&keep;r[3*nw+w]=s3&keep;r[4*nw+w]=s4&keep;
   }
  };
  auto value=[&](const Row&r,int c){int v=0;for(int b=0;b<5;b++)v|=((r[b*nw+c/32]>>(c%32))&1)<<b;return v;};
  for(const auto&src:sources){if(getdeg(src.mult)+2!=d)continue;Row r(5*nw);
   auto set=[&](int c,int v){v=(v%31+31)%31;for(int b=0;b<5;b++)if(v&(1<<b))r[b*nw+c/32]|=uint32_t(1)<<(c%32);};
   for(int k=0;k<66;k++){auto [a,b]=qm[k];set(highIndex.at(src.mult+var[a]+var[b]),Q[src.e][k]);}
   for(int v=0;v<11;v++)for(int k=0;k<11;k++)set(hi+k*lo+lowIndex.at(src.mult+var[v]),L[src.e][v][k]);
   std::vector<std::pair<uint16_t,uint8_t>> reduction;int pivot=-1,pivotValue=0;
   for(int w=0;w<(hi+31)/32;w++){
    uint32_t nz=r[w]|r[nw+w]|r[2*nw+w]|r[3*nw+w]|r[4*nw+w];
    while(nz){int bit=__builtin_ctz(nz),c=32*w+bit;if(c>=hi)break;int f=value(r,c);
     if(!piv[c]){pivot=c;pivotValue=f;break;}
     reduction.push_back({uint16_t(basisIndex[c]),uint8_t(f)});auto R=rep[31-f];addRot(r,(*piv[c])[R.c],w,R.rot,R.neg);operations++;nz=r[w]|r[nw+w]|r[2*nw+w]|r[3*nw+w]|r[4*nw+w];
    }if(pivot>=0)break;
   }
   if(pivot<0||degree[d][pivot]!=src.pivot){std::cerr<<"PROFILE_PIVOT_MISMATCH d="<<d<<" raw="<<src.raw<<"\n";return 5;}
   const int scale=inv[pivotValue],first=pivot/32;
   if(pivotValue!=1){auto R=rep[scale];if(R.c){auto temp=r;addRot(r,temp,first,R.c==1?1:2,0);}for(int w=first;w<nw;w++){uint32_t a[5],u=0;for(int b=0;b<5;b++){a[b]=r[((b-R.rot+5)%5)*nw+w];u|=a[b];}for(int b=0;b<5;b++)r[b*nw+w]=a[b]^(R.neg?u:0);}}
   if(value(r,pivot)!=1)return 6;generated++;phaseCount++;basisIndex[pivot]=generated;
   // b_generated = scale * (raw original row - sum f * b_previous).
   u32(opsout,src.raw);opsout.put(char(scale));u32(opsout,reduction.size());for(auto [b,f]:reduction){u16(opsout,b);opsout.put(char(f));}
   out<<"B0["<<generated<<"]=";bool firstTerm=true;
   for(int j=pivot;j<hi;j++){int v=value(r,j);if(v){if(!firstTerm)out<<"+";out<<v<<"*gen("<<global.at(degree[d][j])<<")";firstTerm=false;nonzeroCoefficients++;}}
   for(int j=0;j<lo;j++){bool nz=false;for(int k=0;k<11;k++)if(value(r,hi+k*lo+j)){nz=true;break;}if(!nz)continue;if(!firstTerm)out<<"+";out<<"(";bool fp=true;for(int k=0;k<11;k++){int v=value(r,hi+k*lo+j);if(v){if(!fp)out<<"+";out<<v;if(k)out<<"*s"<<(k>1?"^"+std::to_string(k):"");fp=false;nonzeroCoefficients++;}}out<<")*gen("<<global.at(degree[d-1][j])<<")";firstTerm=false;}
   out<<";\n";
   auto p=std::make_unique<std::array<Row,3>>();(*p)[0]=std::move(r);(*p)[1]=(*p)[0];(*p)[2]=(*p)[0];addRot((*p)[1],(*p)[0],first,1,0);addRot((*p)[2],(*p)[0],first,2,0);piv[pivot]=std::move(p);
  }
  std::cout<<"{\"phase\":\"native-constant-prebasis\",\"mDegree\":"<<d<<",\"augmentedColumns\":"<<width<<",\"phasePivots\":"<<phaseCount<<",\"totalPivots\":"<<generated<<",\"operations\":"<<operations<<",\"elapsedSeconds\":"<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"}\n"<<std::flush;
 }
 if(generated!=3333)return 7;out<<"attrib(B0,\"isSB\",1);\n";out.close();opsout.close();
 if(!out||!opsout)return 8;
 std::cout<<"{\"status\":\"native-prebasis-complete\",\"field\":31,\"parameterDegreeAtMost\":10,\"pivots\":3333,\"operations\":"<<operations<<",\"nonzeroScalarCoefficients\":"<<nonzeroCoefficients<<",\"elapsedSeconds\":"<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"}\n";
}
