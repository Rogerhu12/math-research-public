// Evaluate the SAME global VQ of all198 old beta-zero directions in two rings.
// No arbitrary local q is chosen. Original monic-G/source-LC pairing is paid.
#include "2026-11-14-r150-second-bockstein-jet-common-789f.hpp"
struct VEntry {uint16_t source;std::array<uint8_t,8> coefficient;};
struct VRow {int degree=0,lc=0;std::vector<VEntry> entries;};
int main(int argc,char**argv){try{
 if(argc!=7)return 2;std::signal(SIGTERM,jt::signal);std::signal(SIGINT,jt::signal);
 auto start=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 sb::Model model(argv[1]);auto lab=jt::labels(argv[4]);std::string prefix=argv[5],binding=argv[6];BitOps ops;auto pw=jt::powers(31,256);
 std::ifstream graph(argv[2],std::ios::binary);if(sb::tag(graph)!="R150GG31")throw std::runtime_error("same actual T96 graph");
 for(int v:{2195,1034,2195,96,8,2195,2195,6,1})if(sb::get(graph,4)!=uint64_t(v))throw std::runtime_error("same T96 graph dimensions");
 std::array<int,6> counts{1034,6,66,396,11,1716},shifts{0,-81,-71,-61,-56,-51},words{};std::array<std::vector<int>,6> dictionary;
 int offset=0,components=0;std::vector<bool> seenSources(2195);
 for(int g=0;g<6;g++){
  int s=int32_t(sb::get(graph,4)),c=sb::get(graph,4),w=sb::get(graph,4),l=sb::get(graph,4),o=sb::get(graph,4),cc=sb::get(graph,4);
  if(s!=shifts[g]||c!=counts[g]||w!=(c+31)/32||l!=9-s||o!=offset||cc!=components)throw std::runtime_error("actual six T96 groups");words[g]=w;offset+=w*l;components+=c;
  if(g)for(int j=0;j<c;j++){int i=sb::get(graph,4)-1,r=sb::get(graph,4);if(i<0||i>=2195||seenSources[i]||r!=model.sources[i].raw||model.delta(r)-96!=s)throw std::runtime_error("actual V original source map");seenSources[i]=true;dictionary[g].push_back(i);}
 }
 if(offset!=4842||components!=3229)throw std::runtime_error("actual graph width");
 std::vector<std::unique_ptr<VRow>> V(1034);std::vector<bool> seen(3229);int outputs=0,kernels=0,sum=0,ksum=0;uint64_t sourceEntries=0;
 for(int r=0;r<2195;r++){
  int c=sb::get(graph,2)-1,d=int32_t(sb::get(graph,4)),lc=sb::get(graph,1);if(c<0||c>=3229||seen[c]||lc<1||lc>30||d<-81||d>8)throw std::runtime_error("actual graph row");seen[c]=true;
  std::unique_ptr<VRow> v;if(c<1034){if(d<0)throw std::runtime_error("negative image degree");v=std::make_unique<VRow>();v->degree=d;v->lc=lc;}
  for(int g=0;g<6;g++){
   int layers=sb::get(graph,2),stride=layers*words[g];if(layers!=std::max(0,d-shifts[g]+1))throw std::runtime_error("actual graph row layers");Row raw(5*stride);graph.read(reinterpret_cast<char*>(raw.data()),raw.size()*4);if(!graph)throw std::runtime_error("graph full source block");
   if(!g){if(v){int hd=-1,hc=-1;for(int z=d;z>=0&&hc<0;z--)for(int w=0;w<words[0];w++){uint32_t nz=0;for(int b=0;b<5;b++)nz|=raw[b*stride+z*words[0]+w];if(nz){hd=z;hc=32*w+__builtin_ctz(nz);break;}}if(hd!=d||hc!=c||BitOps::get(raw,stride,d*words[0]*32+c)!=lc)throw std::runtime_error("actual image leading identity");}else for(auto a:raw)if(a)throw std::runtime_error("source-leading row not genuine kernel");continue;}
   if(!v)continue;
   const int js=8*words[g];Row jets(5*js);
   for(int k=0;k<8;k++)for(int z=0;z<layers;z++){int a=pw[z][k]*ops.inv[lc]%31;if(a)sb::scalar(ops,jets,js,k*words[g],raw,stride,z*words[g],words[g],a);}
   for(int i=0;i<counts[g];i++){VEntry e{};e.source=dictionary[g][i];bool nonzero=false;for(int k=0;k<8;k++){e.coefficient[k]=BitOps::get(jets,js,k*words[g]*32+i);nonzero|=e.coefficient[k]!=0;}if(nonzero){v->entries.push_back(e);sourceEntries++;}}
  }
  if(v){V[c]=std::move(v);outputs++;sum+=d;}else{kernels++;ksum+=d+96;}
 }
 sb::tail(graph);if(outputs!=1021||kernels!=1174||sum!=716||ksum!=60050)throw std::runtime_error("full original graph certificate profile");
 jt::Packed C;C.kind=1;C.bound=177;C.rows.assign(2195,Row(5*jt::S));std::string checkpoint=prefix+"-vq-checkpoint.bin";{std::ifstream in(checkpoint);if(in)C=jt::readPacked(checkpoint,2195,model,lab,binding);}
 if(C.kind!=1||C.bound!=177||C.done<0||C.done>1021)throw std::runtime_error("VQ checkpoint scope");int resumed=C.done;
 std::ifstream q(argv[3],std::ios::binary);if(sb::tag(q)!="R150IQ31")throw std::runtime_error("same original200 image quotients");for(int v:{1034,1021,200,85})if(sb::get(q,4)!=uint64_t(v))throw std::runtime_error("same original200 quotient dimensions");
 int previous=0;uint64_t products=0;
 for(int r=0;r<1021;r++){
  int c=sb::get(q,2),d=sb::get(q,1),lc=sb::get(q,1);if(c<=previous||c>1034||!V[c-1]||d!=V[c-1]->degree||lc!=V[c-1]->lc)throw std::runtime_error("monic G / actual V quotient pairing");previous=c;Triple packed;packed[0].resize(5*jt::S);
  for(int j=0;j<200;j++){int n=sb::get(q,2);if(n>lab[j].cost-d+1)throw std::runtime_error("per-target actual global quotient degree bound");std::vector<uint8_t>poly(n);for(auto &a:poly){a=sb::get(q,1);if(a>30)throw std::runtime_error("actual Q coefficient");}if(n&&!poly.back())throw std::runtime_error("actual Q canonical polynomial");if(j<jt::NT&&r>=resumed){auto a=jt::evaluate(poly,pw);for(int k=0;k<8;k++)BitOps::set(packed[0],jt::S,k*jt::W*32+j,a[k]);}}
  if(r<resumed)continue;BitOps::refresh(packed,jt::S,0);
  for(auto &e:V[c-1]->entries){jt::Co a{};for(int k=0;k<8;k++)a[k]=e.coefficient[k];jt::muladd(C.rows[e.source],packed,a,ops);products++;}
  if((r+1)%100==0||r+1==1021||jt::stopped){C.done=r+1;jt::writePacked(checkpoint,C,model,lab,binding);std::cout<<"{\"phase\":\"same-global-VQ-two-ring-checkpoint\",\"completedImageRows\":"<<r+1<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;}
  if(jt::stopped)return 124;
 }
 sb::tail(q);jt::writePacked(prefix+"-original2195-source-jets.bin",C,model,lab,binding);
 std::ofstream meta(prefix+"-vq.json");meta<<"{\"format\":\"r150-same-global198-VQ-two-ring-source-v1\",\"status\":\"completed\",\"targets\":198,\"TaylorJetCount\":8,\"sourceRows\":2195,\"completeImageRows\":1021,\"sameOriginalGlobalQuotients\":true,\"sameActualMonicGSourcePairing\":true,\"globalSourceCostBound\":177,\"actual198MaximumRHSWeightedCost\":81,\"localSolutionChosenIndependently\":false,\"resumedImageRows\":"<<resumed<<",\"nonzeroEvaluatedSourceEntries\":"<<sourceEntries<<",\"processedJetProducts\":"<<products<<",\"bindingSHA256\":\""<<binding<<"\",\"elapsedSeconds\":"<<elapsed()<<"}\n";meta.close();if(!meta)throw std::runtime_error("VQ receipt write");
 std::cout<<"{\"status\":\"same-global198-VQ-jets-complete\",\"elapsedSeconds\":"<<elapsed()<<"}\n";return 0;
}catch(const std::exception&e){std::cerr<<"SAME_GLOBAL_JET_VQ_FAILED "<<e.what()<<"\n";return 1;}}
