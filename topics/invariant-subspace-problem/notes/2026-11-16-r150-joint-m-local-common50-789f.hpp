// Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.
// Runtime Taylor/CRT field transport for the exact original R150 source dictionary.
// Independent joint-M fork: pure root2 lengths up to50; CRT8 unchanged.
#include "2026-11-14-r150-ninth-first-common-789f.hpp"
#include <array>
#include <csignal>
#include <cstdio>
#include <cstring>
#include <filesystem>
#include <map>
namespace jt {
inline int NT=0,W=0,L=0,S=0,RING=0;
constexpr int NB=3333,NS=2195,NR=6188;
inline volatile std::sig_atomic_t stopped=0;
inline void signal(int){stopped=1;}
using Co=std::array<int,50>;
struct Spec{std::vector<int> target;int ring=0,length=0;};
inline Spec labels(const std::string&file){
 std::ifstream in(file);std::string magic,extra;int prime,n,l,ring;
 in>>magic>>prime>>n>>l>>ring;
 if(magic!="R150_S2_LOCAL_JET_SPEC_V1"||prime!=31||n<1||n>256||l<1||l>50||(ring!=2&&ring!=12)||(ring==12&&l!=8))throw std::runtime_error("runtime exact Taylor spec");
 Spec a;a.length=l;a.ring=ring;a.target.resize(n);std::set<int>seen;
 for(int&v:a.target){in>>v;if(v<1||v>65535||!seen.insert(v).second)throw std::runtime_error("unique source labels");}
 if(!in||in>>extra)throw std::runtime_error("complete runtime source spec");
 NT=n;L=l;W=(n+31)/32;S=W*L;RING=ring;return a;
}
inline int label(const Spec&a,int j){return a.target.at(j);}
struct KernelLabel{int graph=0,head=0,cost=0,source=0,raw=0;};
inline std::vector<KernelLabel> kernelLabels(const std::string&file){
 std::ifstream in(file,std::ios::binary);if(sb::tag(in)!="R150KK31")throw std::runtime_error("original K200 magic");
 for(int v:{31,6188,200,85})if(sb::get(in,4)!=uint64_t(v))throw std::runtime_error("original K200 dimensions");
 std::vector<KernelLabel>a(200);
 for(auto&x:a){x.graph=sb::get(in,4);x.head=sb::get(in,2);x.cost=sb::get(in,2);x.source=sb::get(in,4);x.raw=sb::get(in,4);}
 for(int j=0;j<200;j++)if(a[j].cost!=(j<160?80:j<198?81:85)||a[j].head<1035||a[j].source<1||a[j].source>2195||a[j].raw<1||a[j].raw>6188)throw std::runtime_error("original K200 labels");
 return a;
}
inline std::vector<Co> powers(int modulus,int maximum){
 std::vector<Co>p(maximum+1);std::array<int,50>bin{};bin[0]=1;int two=1;
 for(int d=0;d<=maximum;d++){
  if(d){for(int k=49;k>=1;k--)bin[k]=(int64_t(bin[k])+bin[k-1])%modulus;two=int64_t(two)*2%modulus;}
  if(RING==2){int v=two;for(int k=0;k<L;k++){p[d][k]=k<=d?int64_t(bin[k])*v%modulus:0;v=int64_t(v)*((modulus+1)/2)%modulus;}}
  else{for(int k=0;k<3;k++)p[d][k]=k<=d?bin[k]:0;int v=two;for(int k=0;k<5;k++){p[d][3+k]=k<=d?int64_t(bin[k])*v%modulus:0;v=int64_t(v)*((modulus+1)/2)%modulus;}}
 }return p;
}
inline void muladd(Row&dest,const Triple&src,const Co&a,BitOps&ops,int sign=1){
 auto part=[&](int start,int length){
  for(int k=0;k<length;k++){int c=sign>0?a[start+k]:sb::mod(-a[start+k]);if(!c)continue;auto r=ops.rep[c];
   BitOps::add(dest,S,(start+k)*W,src[r.c],S,start*W,(length-k)*W,r.rot,r.neg);}
 };
 if(RING==2)part(0,L);else{part(0,3);part(3,5);}
}
inline Co evaluate(const std::vector<uint8_t>&p,const std::vector<Co>&pw,int modulus=31){
 Co a{};if(p.size()>pw.size())throw std::runtime_error("Taylor polynomial exceeds declared range");
 for(size_t d=0;d<p.size();d++)if(p[d])for(int k=0;k<L;k++)a[k]=(a[k]+int64_t(p[d])*pw[d][k])%modulus;
 return a;
}
inline void padding(const Row&r){
 if(r.size()!=size_t(5*S))throw std::runtime_error("packed Taylor row length");
 if(NT%32)for(int k=0;k<L;k++){uint32_t v=0;for(int b=0;b<5;b++)v|=r[b*S+k*W+W-1];if(v>>(NT%32))throw std::runtime_error("packed Taylor target padding");}
}
struct Packed{int kind=0,done=0,bound=0;std::vector<Row>rows;};
inline void writePacked(const std::string&file,const Packed&p,const sb::Model&m,const Spec&lab,const std::string&binding){
 if(binding.size()!=64||int(lab.target.size())!=NT||lab.length!=L||lab.ring!=RING)throw std::runtime_error("packed Taylor scope");
 std::ofstream out(file+".tmp",std::ios::binary);out.write("R150SP31",8);
 for(int v:{31,int(p.rows.size()),NT,L,S,p.kind,p.done,p.bound})u32(out,v);out.write(binding.data(),64);
 for(int j=0;j<NT;j++)u16(out,label(lab,j));
 for(int i=0;i<int(p.rows.size());i++){int r=p.rows.size()==NS?m.sources[i].raw:i+1;u32(out,i+1);u32(out,r);u16(out,m.delta(r));padding(p.rows[i]);out.write(reinterpret_cast<const char*>(p.rows[i].data()),5*S*4);}
 out.close();if(!out||std::rename((file+".tmp").c_str(),file.c_str()))throw std::runtime_error("atomic packed Taylor save");
}
inline Packed readPacked(const std::string&file,int count,const sb::Model&m,const Spec&lab,const std::string&binding){
 std::ifstream in(file,std::ios::binary);if(sb::tag(in)!="R150SP31")throw std::runtime_error("runtime packed Taylor magic");
 for(int v:{31,count,NT,L,S})if(sb::get(in,4)!=uint64_t(v))throw std::runtime_error("runtime packed Taylor dimensions");
 Packed p;p.kind=sb::get(in,4);p.done=sb::get(in,4);p.bound=sb::get(in,4);std::string b(64,' ');in.read(b.data(),64);if(b!=binding)throw std::runtime_error("same packed Taylor semantic binding");
 for(int j=0;j<NT;j++)if(sb::get(in,2)!=uint64_t(label(lab,j)))throw std::runtime_error("runtime packed Taylor label");
 p.rows.assign(count,Row(5*S));
 for(int i=0;i<count;i++){int r=count==NS?m.sources[i].raw:i+1;
  if(sb::get(in,4)!=uint64_t(i+1)||sb::get(in,4)!=uint64_t(r)||sb::get(in,2)!=uint64_t(m.delta(r)))throw std::runtime_error("original source dictionary");
  in.read(reinterpret_cast<char*>(p.rows[i].data()),5*S*4);if(!in)throw std::runtime_error("complete packed Taylor array");padding(p.rows[i]);}
 sb::tail(in);return p;
}
struct Buffer{
 std::vector<uint8_t>b;size_t pos=0;
 explicit Buffer(const std::string&file){std::ifstream in(file,std::ios::binary|std::ios::ate);if(!in)throw std::runtime_error("provenance input");auto n=in.tellg();in.seekg(0);b.resize(n);in.read(reinterpret_cast<char*>(b.data()),n);if(!in)throw std::runtime_error("complete provenance input");}
 uint64_t get(int n){if(pos+n>b.size())throw std::runtime_error("truncated provenance");uint64_t v=0;for(int i=0;i<n;i++)v|=uint64_t(b[pos++])<<(8*i);return v;}
 void magic(const char*s){if(b.size()<8||std::memcmp(b.data(),s,8))throw std::runtime_error("provenance magic");pos=8;}
 void tail(){if(pos!=b.size())throw std::runtime_error("provenance trailing bytes");}
};
// Read-only comparison with a completed prior R1503P31 source. New precision may increase.
inline void compareOldPrefix(const std::string&file,const Packed&p,const sb::Model&m,const Spec&lab){
 if(file=="-")return;
 std::ifstream in(file,std::ios::binary);if(sb::tag(in)!="R1503P31")throw std::runtime_error("old complete197 packed source");
 int prime=sb::get(in,4),n=sb::get(in,4),nt=sb::get(in,4),l=sb::get(in,4),s=sb::get(in,4),kind=sb::get(in,4),done=sb::get(in,4),bound=sb::get(in,4);
 if(prime!=31||n!=int(p.rows.size())||nt!=197||l!=10||s!=70||kind!=p.kind||done!=p.done||bound!=p.bound||L<10||RING!=2)throw std::runtime_error("same old completed ten-jet scope");
 std::string old(64,' ');in.read(old.data(),64);std::vector<int>targets(nt);std::map<int,int>index;
 for(int j=0;j<nt;j++){targets[j]=sb::get(in,2);if(!index.emplace(targets[j],j).second)throw std::runtime_error("old unique source label");}
 Row row(5*s);
 for(int i=0;i<n;i++){int r=n==NS?m.sources[i].raw:i+1;
  if(sb::get(in,4)!=uint64_t(i+1)||sb::get(in,4)!=uint64_t(r)||sb::get(in,2)!=uint64_t(m.delta(r)))throw std::runtime_error("old source dictionary");
  in.read(reinterpret_cast<char*>(row.data()),row.size()*4);if(!in)throw std::runtime_error("old source array");
  for(int j=0;j<NT;j++){int oj=index.at(label(lab,j));for(int k=0;k<10;k++)
   if(BitOps::get(row,s,k*7*32+oj)!=BitOps::get(p.rows[i],S,k*W*32+j))throw std::runtime_error("new extension changed paid canonical Taylor prefix");}
 }sb::tail(in);
}
} // namespace jt
