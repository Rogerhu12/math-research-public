// Same integer kernel representatives modulo31^3; full original17 local product.
// Jet coefficient lifts of the specific global q change delta2 by A0*c only.
#include "2026-11-14-r150-second-bockstein-jet-common-789f.hpp"
#include <filesystem>
struct Term {uint64_t monomial; jt::Co a;};
static int inverse(int a,int m){int r0=m,r1=a,s0=0,s1=1;while(r1){int q=r0/r1,t=r0-q*r1;r0=r1;r1=t;t=s0-q*s1;s0=s1;s1=t;}if(r0!=1)throw std::runtime_error("original fixed row unit");return sb::mod(s0,m);}
int main(int argc,char**argv){try{
 if(argc!=7)return 2;std::signal(SIGTERM,jt::signal);std::signal(SIGINT,jt::signal);
 auto start=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 constexpr int modulus=29791;sb::Model model(argv[1]);model.higher(argv[2]);auto lab=jt::labels(argv[3]);std::string prefix=argv[5],binding=argv[6];
 auto q=jt::readPacked(argv[4],6188,model,lab,binding);if(q.kind!=2||q.done!=6188||q.bound!=177)throw std::runtime_error("actual global q original6188 jets required");auto pw=jt::powers(modulus,256);
 std::array<std::vector<Term>,17>terms;
 auto polyJet=[&](const auto&p){jt::Co a{};for(int d=0;d<int(p.size());d++)if(p[d])for(int k=0;k<8;k++)a[k]=(a[k]+int64_t(p[d])*pw[d][k])%modulus;return a;};
 for(int e=0;e<17;e++){
  if(e<11){for(int k=0;k<66;k++)if(model.Qh[e][k]){auto[x,y]=model.quadratic[k];jt::Co a{};a[0]=a[3]=model.Qh[e][k];terms[e].push_back({model.var[x]+model.var[y],a});}for(int v=0;v<11;v++){auto a=polyJet(model.Lh[e][v]);if(std::any_of(a.begin(),a.end(),[](int c){return c!=0;}))terms[e].push_back({model.var[v],a});}}
  else for(int k=0;k<66;k++){auto a=polyJet(model.Gh[e-11][k]);if(std::any_of(a.begin(),a.end(),[](int c){return c!=0;})){auto[x,y]=model.quadratic[k];terms[e].push_back({model.var[x]+model.var[y],a});}}
 }
 const size_t cells=size_t(4367)*8*198;std::vector<uint64_t>product(cells);int completed=0;std::string checkpoint=prefix+"-product-checkpoint.bin";
 {std::ifstream in(checkpoint,std::ios::binary);if(in){if(sb::tag(in)!="R150JC31")throw std::runtime_error("local original product checkpoint magic");for(int v:{31,29791,6188,198,8,4367})if(sb::get(in,4)!=uint64_t(v))throw std::runtime_error("local product checkpoint dimensions");completed=sb::get(in,4);if(completed<0||completed>6188)throw std::runtime_error("local product checkpoint prefix");std::string old(64,' ');in.read(old.data(),64);if(old!=binding)throw std::runtime_error("local product checkpoint binding");in.read(reinterpret_cast<char*>(product.data()),product.size()*8);if(!in)throw std::runtime_error("actual partial original product array");sb::tail(in);}}
 auto save=[&](int done){std::ofstream out(checkpoint+".tmp",std::ios::binary);out.write("R150JC31",8);for(int v:{31,29791,6188,198,8,4367,done})u32(out,v);out.write(binding.data(),64);out.write(reinterpret_cast<const char*>(product.data()),product.size()*8);out.close();if(!out||std::rename((checkpoint+".tmp").c_str(),checkpoint.c_str()))throw std::runtime_error("atomic original product checkpoint");std::ofstream meta(prefix+"-product-checkpoint.json");meta<<"{\"status\":\"checkpointed\",\"completedOriginalRows\":"<<done<<",\"nextOriginalRowOneBased\":"<<done+1<<",\"actualPartialProductArraySaved\":true,\"bindingSHA256\":\""<<binding<<"\"}\n";};
 const size_t headerBytes=8+6*4+198*2,rowBytes=15+198*8*2;
 const std::string primitive=prefix+"-primitive-k2-jets-mod29791.bin",original=prefix+"-original-seventeen-k2-jets-mod29791.bin";
 std::ofstream po,oo;
 auto openSource=[&](std::ofstream&out,const std::string&file,const char*magic){
  if(completed){if(!std::filesystem::exists(file)||std::filesystem::file_size(file)<headerBytes+rowBytes*completed)throw std::runtime_error("missing actual source prefix at product checkpoint");std::filesystem::resize_file(file,headerBytes+rowBytes*completed);out.open(file,std::ios::binary|std::ios::app);}
  else{out.open(file,std::ios::binary);out.write(magic,8);for(int v:{31,29791,6188,198,8,177})u32(out,v);for(int j=0;j<198;j++)u16(out,lab[j].head);}if(!out)throw std::runtime_error("actual original jet source output");
 };
 openSource(po,primitive,"R150KJ31");openSource(oo,original,"R150OJ31");
 std::ifstream in(argv[3],std::ios::binary);if(sb::tag(in)!="R150KK31")throw std::runtime_error("same original kernel magic");for(int v:{31,6188,200,85})if(sb::get(in,4)!=uint64_t(v))throw std::runtime_error("same original200 kernels");
 for(int j=0;j<200;j++){if(sb::get(in,4)!=uint64_t(lab[j].graph)||sb::get(in,2)!=uint64_t(lab[j].head)||sb::get(in,2)!=uint64_t(lab[j].cost)||sb::get(in,4)!=uint64_t(lab[j].source)||sb::get(in,4)!=uint64_t(lab[j].raw))throw std::runtime_error("same integer kernel representative labels");}
 uint64_t products=0,nonzero=0;int resumed=completed;std::vector<uint16_t>k2(8*198);
 int denominatorInverse=inverse(model.denominator,modulus);std::array<int,17>units{},returnUnits{};for(int e=0;e<17;e++){units[e]=int64_t(model.denominator)*inverse(model.contents[e],modulus)%modulus;returnUnits[e]=int64_t(model.contents[e])*denominatorInverse%modulus;if(int64_t(units[e])*returnUnits[e]%modulus!=1)throw std::runtime_error("exact original/primitive row unit transport");}
 for(int r=1;r<=6188;r++){
  model.rowHeader(in,r);int delta=model.delta(r);std::fill(k2.begin(),k2.end(),0);
  for(int j=0;j<200;j++){
   int n=sb::get(in,2);if(n>lab[j].cost-delta+1)throw std::runtime_error("actual integer original kernel degree bound");jt::Co a{};int last=0;
   for(int d=0;d<n;d++){last=sb::get(in,1);if(last>30)throw std::runtime_error("same canonical integer kernel coefficient");if(r>completed&&j<198&&last)for(int k=0;k<8;k++)a[k]=(a[k]+int64_t(last)*pw[d][k])%modulus;}if(n&&!last)throw std::runtime_error("canonical original kernel polynomial");
   if(r>completed&&j<198)for(int k=0;k<8;k++)k2[k*198+j]=sb::mod(a[k]-31*BitOps::get(q.rows[r-1],jt::S,k*jt::W*32+j),modulus);
  }
  if(r<=completed)continue;model.rowHeader(po,r);model.rowHeader(oo,r);int e=(r-1)%17;
  for(int j=0;j<198;j++)for(int k=0;k<8;k++){int a=k2[k*198+j],b=int64_t(a)*units[e]%modulus;u16(po,a);u16(oo,b);if(int64_t(b)*returnUnits[e]%modulus!=a)throw std::runtime_error("original rational source row transport identity");nonzero+=a!=0;}
  uint64_t mult=model.multipliers[(r-1)/17];
  for(const auto&t:terms[e]){
   int component=model.component.at(mult+t.monomial);uint64_t*dest=product.data()+size_t(component)*8*198;
   for(auto[start,length]:{std::pair<int,int>{0,3},{3,5}})for(int i=0;i<length;i++)if(int a=t.a[start+i])for(int j=0;j<length-i;j++){
    const uint16_t*src=k2.data()+(start+j)*198;uint64_t*out=dest+(start+i+j)*198;
    for(int z=0;z<198;z++)out[z]+=uint64_t(a)*src[z];products+=198;
   }
  }
  if(r%500==0||r==6188||jt::stopped)std::cout<<"{\"phase\":\"all-original17-integer-jet-product\",\"completedOriginalRows\":"<<r<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
  if(jt::stopped){po.flush();oo.flush();if(!po||!oo)throw std::runtime_error("actual source prefix flush");save(r);return 124;}
 }
 sb::tail(in);po.close();oo.close();if(!po||!oo)throw std::runtime_error("full source jet write");
 std::ofstream out(prefix+"-divided-original-delta-jets.bin",std::ios::binary);out.write("R150DJ31",8);for(int v:{31,198,4367,8})u32(out,v);for(int j=0;j<198;j++)u16(out,lab[j].head);uint64_t nonzeroDelta=0;
 for(int c=0;c<4367;c++){sb::put(out,model.keys[c],8);for(int k=0;k<8;k++)for(int j=0;j<198;j++){int a=product[(size_t(c)*8+k)*198+j]%modulus;if(a%961)throw std::runtime_error("same global source integer product not divisible by961 in a retained Taylor coefficient");int d=a/961;out.put(char(d));nonzeroDelta+=d!=0;}}
 out.close();if(!out)throw std::runtime_error("full local original delta output");
 std::ofstream meta(prefix+"-original-product.json");meta<<"{\"format\":\"r150-same-integer198-kernel-original17-Taylor-product-v1\",\"status\":\"completed\",\"prime\":31,\"modulus\":29791,\"divisor\":961,\"targetCount\":198,\"TaylorRings\":[{\"root\":1,\"length\":3},{\"root\":2,\"length\":5}],\"allOriginalRows\":6188,\"allOriginalOutputComponents\":4367,\"sameOriginalIntegerKernelRepresentative\":true,\"qJetsFromSameGlobalVQAndOriginalDAG\":true,\"allOriginalProductJetCoefficientsDivisible\":true,\"originalRowScaleTransportVerified\":true,\"globalQSourceCostBound\":177,\"jetLiftCarryIsOriginalImage\":true,\"globalPolynomialDeltaSourcesExpanded\":false,\"fullOriginalGlobalMod29791IdentityVerified\":false,\"resumedOriginalRows\":"<<resumed<<",\"processedIntegerScalarProducts\":"<<products<<",\"processedNonzeroSourceJets\":"<<nonzero<<",\"nonzeroDeltaJets\":"<<nonzeroDelta<<",\"bindingSHA256\":\""<<binding<<"\",\"elapsedSeconds\":"<<elapsed()<<"}\n";meta.close();if(!meta)throw std::runtime_error("original jet product receipt");std::cout<<"{\"status\":\"all198-original17-integer-jet-products-divided\",\"elapsedSeconds\":"<<elapsed()<<"}\n";return 0;
}catch(const std::exception&e){std::cerr<<"ALL198_ORIGINAL_INTEGER_JET_PRODUCT_FAILED "<<e.what()<<"\n";return 1;}}
