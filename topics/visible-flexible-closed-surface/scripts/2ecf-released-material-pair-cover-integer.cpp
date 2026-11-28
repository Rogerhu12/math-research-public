#include <algorithm>
#include <array>
#include <bit>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

// Exhaust the continuous material rectangles exported by the directed builder.
// All decisions are integer inequalities; the binary file contains interval
// bounds, never point samples.  The only floating point operation is timing.
using I = std::int64_t;
using Wide = __int128_t;
struct Node {
  int i,j,k,l,kind,left=-1,right=-1;
  std::array<I,3> lo,hi;
};
struct Failure { Node a,b; I gap; Wide path; };
std::string decimal(Wide x) {
  if(!x)return "0";
  std::string s;
  while(x){s+=char('0'+x%10);x/=10;}
  std::reverse(s.begin(),s.end());return s;
}
template<class T> void read(std::ifstream& f,std::vector<T>& v,std::size_t n) {
  v.resize(n);f.read(reinterpret_cast<char*>(v.data()),n*sizeof(T));
  if(!f)throw std::runtime_error("Incomplete directed box file");
}
int main(int argc,char** argv) {
  if(argc!=3)throw std::runtime_error("arguments: complete-boxes.bin report.json");
  static_assert(std::endian::native==std::endian::little);
  const auto start=std::chrono::steady_clock::now();
  std::ifstream in(argv[1],std::ios::binary);std::vector<I> h;
  read(in,h,13);assert(h[0]==0x52503239380001);
  const int ns=h[1],nu=h[2];
  assert(0<ns&&ns<=20000&&0<nu&&nu<=32768);
  const I pi=h[3],twolo=h[4],twohi=h[5],chord=h[6],gapcap=h[7];
  const I pn=h[8],pd=h[9],gp=h[10],mp=h[11],mg=h[12];
  assert(gp==(I(1)<<30)&&mp==(I(1)<<20)&&mg==(I(1)<<20));
  assert(0<pn&&pn<10000000000LL&&0<pd&&pd<10000000000LL);
  assert(0<chord&&chord<1000000000000000000LL&&0<gapcap&&gapcap<1000000000LL);
  std::vector<I> box,sgrid,angles,kind;std::vector<std::array<I,3>> gram;
  read(in,box,std::size_t(ns)*nu*6);read(in,gram,ns);
  read(in,sgrid,2*ns);read(in,angles,2*(nu+1));read(in,kind,ns);
  char extra;assert(!in.read(&extra,1));
  for(auto& g:gram)for(I x:g)assert(0<=x&&x<1000000000LL);
  for(I x:sgrid)assert(std::abs(x)<(I(1)<<24));
  for(I x:angles)assert(0<=x&&x<(I(1)<<24));
  std::vector<std::vector<std::array<I,3>>> rmq{gram};
  for(int jump=1;jump*2<=ns;jump*=2) {
    std::vector<std::array<I,3>> next(ns-2*jump+1);
    for(std::size_t j=0;j<next.size();++j)for(int d=0;d<3;++d)
      next[j][d]=std::max(rmq.back()[j][d],rmq.back()[j+jump][d]);
    rmq.push_back(std::move(next));
  }
  std::vector<Node> nodes;nodes.reserve(std::size_t(ns)*nu*2);
  auto make=[&](int i,int j,int k,int l) {
    Node n;n.i=i;n.j=j;n.k=k;n.l=l;n.kind=kind[i];
    n.lo.fill(std::numeric_limits<I>::max());n.hi.fill(std::numeric_limits<I>::min());
    for(int s=i;s<j;++s){
      if(kind[s]!=n.kind)n.kind=0;
      for(int u=k;u<l;++u){const I* b=&box[(std::size_t(s)*nu+u)*6];
        for(int d=0;d<3;++d){n.lo[d]=std::min(n.lo[d],b[2*d]);n.hi[d]=std::max(n.hi[d],b[2*d+1]);}
      }
    }
    const int id=nodes.size();nodes.push_back(n);return id;
  };
  auto children=[&](int id) {
    const Node n=nodes[id];
    if(n.left>=0)return std::pair(n.left,n.right);
    if(n.j-n.i==1&&n.l-n.k==1)return std::pair(-1,-1);
    int left,right;
    if(n.j-n.i>1&&(n.l-n.k==1||
        (sgrid[2*(n.j-1)+1]-sgrid[2*n.i])*11>(angles[2*n.l+1]-angles[2*n.k])*10)) {
      const int mid=(n.i+n.j)/2;left=make(n.i,mid,n.k,n.l);right=make(mid,n.j,n.k,n.l);
    } else {
      const int mid=(n.k+n.l)/2;left=make(n.i,n.j,n.k,mid);right=make(n.i,n.j,mid,n.l);
    }
    nodes[id].left=left;nodes[id].right=right;return std::pair(left,right);
  };
  const Wide bound=Wide(pn)*mg*mp*mp;
  auto path=[&](const Node& p,const Node& q) -> Wide {
    const I ds=std::max(std::abs(sgrid[2*p.i]-sgrid[2*(q.j-1)+1]),
                        std::abs(sgrid[2*(p.j-1)+1]-sgrid[2*q.i]));
    if(ds>mp)return bound+1; // Conservative: decline this local certificate.
    const I x0=angles[2*p.k],x1=angles[2*p.l+1];
    const I y0=angles[2*q.k],y1=angles[2*q.l+1];
    const I da=std::min({pi,std::max(std::abs(x0-y1),std::abs(x1-y0)),
      std::max(std::abs(x0-y1-twohi),std::abs(x1-y0-twolo)),
      std::max(std::abs(x0-y1+twolo),std::abs(x1-y0+twohi))});
    const int l=std::min(p.i,q.i),r=std::max(p.j,q.j),level=std::bit_width(unsigned(r-l))-1;
    std::array<I,3> g;
    for(int d=0;d<3;++d)g[d]=std::max(rmq[level][l][d],rmq[level][r-(1<<level)][d]);
    return (Wide(g[0])*ds*ds+2*Wide(g[2])*ds*da+Wide(g[1])*da*da)*pd;
  };
  const int root=make(0,ns,0,nu);
  std::vector<std::pair<int,int>> work{{root,root}};
  std::array<std::uint64_t,4> counts{};std::uint64_t visits=0,failures=0;
  std::vector<Failure> first;
  while(!work.empty()) {
    auto [ia,ib]=work.back();work.pop_back();const Node p=nodes[ia],q=nodes[ib];++visits;
    if(visits%10000000==0)std::cout<<"COVER "<<visits<<" "<<work.size()<<" "<<nodes.size()<<" "<<failures<<std::endl;
    if(p.kind&&p.kind==q.kind&&p.kind<=3){++counts[p.kind==1?0:1];continue;}
    I distance=0;
    for(int d=0;d<3;++d){I g=std::clamp(std::max(p.lo[d]-q.hi[d],q.lo[d]-p.hi[d]),I(0),gapcap);distance+=g*g;}
    if(distance>=chord){++counts[2];continue;}
    const Wide pathbound=path(p,q);
    if(pathbound<bound){++counts[3];continue;}
    if(ia==ib){
      auto [l,r]=children(ia);
      if(l>=0){work.emplace_back(l,l);work.emplace_back(l,r);work.emplace_back(r,r);continue;}
    } else {
      auto a=children(ia),b=children(ib);
      if(a.first>=0||b.first>=0) {
        I sa=0,sb=0;for(int d=0;d<3;++d){sa+=p.hi[d]-p.lo[d];sb+=q.hi[d]-q.lo[d];}
        if(a.first>=0&&(b.first<0||sa>=sb)){work.emplace_back(a.first,ib);work.emplace_back(a.second,ib);}
        else{work.emplace_back(ia,b.first);work.emplace_back(ia,b.second);}
        continue;
      }
    }
    ++failures;if(first.size()<32)first.push_back({p,q,distance,pathbound});
  }
  std::ofstream out(argv[2]);
  if(!out)throw std::runtime_error("Cannot create final report");
  out<<"{\n  \"schema\": \"complete-material-pair-integer-cover-v2\",\n"
     <<"  \"allMaterialPairsCovered\": "<<(failures?"false":"true")<<",\n"
     <<"  \"pairVisits\": "<<visits<<",\n  \"unresolvedPairs\": "<<failures<<",\n"
     <<"  \"physicalClosedBoxes\": "<<std::uint64_t(ns)*nu<<",\n  \"treeNodes\": "<<nodes.size()<<",\n"
     <<"  \"countsKnownPrefixFlatFarShort\": ["<<counts[0]<<","<<counts[1]<<","<<counts[2]<<","<<counts[3]<<"],\n"
     <<"  \"shortPathIntegerRightHandSide\": \""<<decimal(bound)<<"\",\n"
     <<"  \"firstUnresolved\": [";
  for(std::size_t n=0;n<first.size();++n){
    if(n)out<<",";const auto& f=first[n];
    out<<"\n    {\"a\":["<<f.a.i<<","<<f.a.j<<","<<f.a.k<<","<<f.a.l<<"],"
       <<"\"b\":["<<f.b.i<<","<<f.b.j<<","<<f.b.k<<","<<f.b.l<<"],"
       <<"\"squaredGap\":"<<f.gap<<",\"shortPathLeft\":\""<<decimal(f.path)<<"\"}";
  }
  const double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
  out<<"\n  ],\n  \"seconds\": "<<seconds<<"\n}\n";out.close();
  std::cout<<"DONE "<<visits<<" unresolved="<<failures<<" seconds="<<seconds<<std::endl;
}
