// Two actual Taylor rings, 198 original high-kernel directions, seven words.
#include "2026-11-14-r150-second-bockstein-common-789f.hpp"
#include <csignal>
#include <cstdio>
#include <cstring>
namespace jt {
constexpr int NT=198,W=7,L=8,S=W*L,NB=3333,NS=2195,NR=6188;
static volatile std::sig_atomic_t stopped=0;
static void signal(int){stopped=1;}
using Co=std::array<int,L>;
struct Label {int graph=0,head=0,cost=0,source=0,raw=0;};
static std::vector<Label> labels(const std::string &file){
 std::ifstream in(file,std::ios::binary);if(sb::tag(in)!="R150KK31")throw std::runtime_error("same original kernel file");
 for(int v:{31,6188,200,85})if(sb::get(in,4)!=uint64_t(v))throw std::runtime_error("same original200 kernel dimensions");
 std::vector<Label>a(200);for(auto &x:a){x.graph=sb::get(in,4);x.head=sb::get(in,2);x.cost=sb::get(in,2);x.source=sb::get(in,4);x.raw=sb::get(in,4);}
 for(int j=0;j<NT;j++)if(a[j].cost!=(j<160?80:81)||a[j].head<1035||a[j].source<1||a[j].source>2195||a[j].raw<1||a[j].raw>6188)throw std::runtime_error("actual198 high-kernel labels");
 return a;
}
static std::vector<Co> powers(int modulus,int maximum){
 std::vector<Co> p(maximum+1);std::array<int,5> bin{};bin[0]=1;int two=1;
 for(int d=0;d<=maximum;d++){
  if(d){for(int k=4;k>=1;k--)bin[k]=(bin[k]+bin[k-1])%modulus;two=int64_t(two)*2%modulus;}
  for(int k=0;k<3;k++)p[d][k]=k<=d?bin[k]:0;
  int pow=two;for(int k=0;k<5;k++){p[d][3+k]=k<=d?int64_t(bin[k])*pow%modulus:0;pow=int64_t(pow)*((modulus+1)/2)%modulus;}
 }
 return p;
}
static void muladd(Row &dest,const Triple &src,const Co &a,BitOps &ops,int sign=1){
 for(auto [start,length]:{std::pair<int,int>{0,3},{3,5}})for(int k=0;k<length;k++){
  int c=sign>0?a[start+k]:sb::mod(-a[start+k]);if(!c)continue;auto r=ops.rep[c];
  BitOps::add(dest,S,(start+k)*W,src[r.c],S,start*W,(length-k)*W,r.rot,r.neg);
 }
}
static Co evaluate(const std::vector<uint8_t>&p,const std::vector<Co>&pw,int modulus=31){
 Co a{};if(p.size()>pw.size())throw std::runtime_error("jet polynomial degree");
 for(size_t d=0;d<p.size();d++)if(p[d])for(int k=0;k<L;k++)a[k]=(a[k]+int64_t(p[d])*pw[d][k])%modulus;
 return a;
}
static void padding(const Row&r){for(int k=0;k<L;k++){uint32_t v=0;for(int b=0;b<5;b++)v|=r[b*S+k*W+W-1];if(v>>(NT%32))throw std::runtime_error("198 target padding");}}
struct Packed {int kind=0,done=0,bound=0;std::vector<Row> rows;};
static void writePacked(const std::string&file,const Packed&p,const sb::Model&m,const std::vector<Label>&lab,const std::string&binding){
 if(binding.size()!=64)throw std::runtime_error("jet SHA binding");std::ofstream out(file+".tmp",std::ios::binary);
 out.write("R150JP31",8);for(int v:{31,int(p.rows.size()),NT,L,S,p.kind,p.done,p.bound})u32(out,v);out.write(binding.data(),64);
 for(int j=0;j<NT;j++)u16(out,lab[j].head);
 for(int i=0;i<int(p.rows.size());i++){int r=p.rows.size()==NS?m.sources[i].raw:i+1;u32(out,i+1);u32(out,r);u16(out,m.delta(r));padding(p.rows[i]);out.write(reinterpret_cast<const char*>(p.rows[i].data()),5*S*4);}
 out.close();if(!out||std::rename((file+".tmp").c_str(),file.c_str()))throw std::runtime_error("atomic actual jet source save");
}
static Packed readPacked(const std::string&file,int count,const sb::Model&m,const std::vector<Label>&lab,const std::string&binding){
 std::ifstream in(file,std::ios::binary);if(sb::tag(in)!="R150JP31")throw std::runtime_error("actual jet packed magic");
 for(int v:{31,count,NT,L,S})if(sb::get(in,4)!=uint64_t(v))throw std::runtime_error("actual jet packed dimensions");
 Packed p;p.kind=sb::get(in,4);p.done=sb::get(in,4);p.bound=sb::get(in,4);std::string b(64,' ');in.read(b.data(),64);if(b!=binding)throw std::runtime_error("jet checkpoint frozen input binding");
 for(int j=0;j<NT;j++)if(sb::get(in,2)!=uint64_t(lab[j].head))throw std::runtime_error("jet actual kernel labels");p.rows.assign(count,Row(5*S));
 for(int i=0;i<count;i++){int r=count==NS?m.sources[i].raw:i+1;if(sb::get(in,4)!=uint64_t(i+1)||sb::get(in,4)!=uint64_t(r)||sb::get(in,2)!=uint64_t(m.delta(r)))throw std::runtime_error("jet original source dictionary");in.read(reinterpret_cast<char*>(p.rows[i].data()),5*S*4);if(!in)throw std::runtime_error("truncated packed jet");padding(p.rows[i]);}sb::tail(in);return p;
}
struct Buffer {
 std::vector<uint8_t> b;size_t pos=0;
 explicit Buffer(const std::string&file){std::ifstream in(file,std::ios::binary|std::ios::ate);if(!in)throw std::runtime_error("jet provenance input");auto n=in.tellg();in.seekg(0);b.resize(n);in.read(reinterpret_cast<char*>(b.data()),n);if(!in)throw std::runtime_error("jet provenance read");}
 uint64_t get(int n){if(pos+n>b.size())throw std::runtime_error("truncated jet provenance");uint64_t v=0;for(int i=0;i<n;i++)v|=uint64_t(b[pos++])<<(8*i);return v;}
 void magic(const char*s){if(b.size()<8||std::memcmp(b.data(),s,8))throw std::runtime_error("jet provenance magic");pos=8;}
 void tail(){if(pos!=b.size())throw std::runtime_error("jet provenance tail");}
};
}
