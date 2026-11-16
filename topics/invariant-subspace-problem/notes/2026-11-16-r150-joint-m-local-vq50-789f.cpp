// Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.
// Same actual G/V source pairing. q1 extends the saved global Q; q2..q5 transport fully verified field-jet solutions.
#include "2026-11-16-r150-joint-m-local-common50-789f.hpp"
struct VEntry{uint16_t source;std::array<uint8_t,50>coefficient;};
struct VRow{int degree=0,lc=0;std::vector<VEntry>entries;std::vector<uint8_t>g;};
int main(int argc,char**argv){try{
 if(argc!=10)return 2;std::signal(SIGTERM,jt::signal);std::signal(SIGINT,jt::signal);
 auto start=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 sb::Model model(argv[1]);auto lab=jt::labels(argv[9]);auto originalLabels=jt::kernelLabels(argv[4]);std::map<int,int>targetIndex;for(int j=0;j<jt::NT;j++)targetIndex.emplace(jt::label(lab,j),j);if(jt::RING!=2)throw std::runtime_error("VQ is pure root2");std::string prefix=argv[6],binding=argv[7],mode=argv[8];
 bool first=mode=="q1";if(!first&&mode!="q2"&&mode!="q3"&&mode!="q4"&&mode!="q5")throw std::runtime_error("mode must be q1..q5");BitOps ops;auto pw=jt::powers(31,256);
 std::vector<std::unique_ptr<VRow>>V(1034);uint64_t entries=0;
 if(first){
  std::ifstream graph(argv[2],std::ios::binary);if(sb::tag(graph)!="R150GG31")throw std::runtime_error("same actual T96 graph");
  for(int v:{2195,1034,2195,96,8,2195,2195,6,1})if(sb::get(graph,4)!=uint64_t(v))throw std::runtime_error("actual T96 graph dimensions");
  std::array<int,6>counts{1034,6,66,396,11,1716},shifts{0,-81,-71,-61,-56,-51},words{};std::array<std::vector<int>,6>dict;
  int offset=0,components=0;std::vector<bool>seenSources(2195);
  for(int g=0;g<6;g++){int s=int32_t(sb::get(graph,4)),c=sb::get(graph,4),w=sb::get(graph,4),l=sb::get(graph,4),o=sb::get(graph,4),cc=sb::get(graph,4);
   if(s!=shifts[g]||c!=counts[g]||w!=(c+31)/32||l!=9-s||o!=offset||cc!=components)throw std::runtime_error("six original T96 groups");words[g]=w;offset+=w*l;components+=c;
   if(g)for(int j=0;j<c;j++){int i=sb::get(graph,4)-1,r=sb::get(graph,4);if(i<0||i>=2195||seenSources[i]||r!=model.sources[i].raw||model.delta(r)-96!=s)throw std::runtime_error("actual V source dictionary");seenSources[i]=true;dict[g].push_back(i);}
  }
  if(offset!=4842||components!=3229)throw std::runtime_error("original graph width");std::vector<bool>seen(3229);int outputs=0,kernels=0,sum=0,ksum=0,constant=0;
  for(int r=0;r<2195;r++){int c=sb::get(graph,2)-1,d=int32_t(sb::get(graph,4)),lc=sb::get(graph,1);if(c<0||c>=3229||seen[c]||lc<1||lc>30||d<-81||d>8)throw std::runtime_error("actual graph row");seen[c]=true;
   std::unique_ptr<VRow>v;if(c<1034){if(d<0)throw std::runtime_error("negative image degree");v=std::make_unique<VRow>();v->degree=d;v->lc=lc;}
   for(int g=0;g<6;g++){int layers=sb::get(graph,2),stride=layers*words[g];if(layers!=std::max(0,d-shifts[g]+1))throw std::runtime_error("actual graph row layers");Row raw(5*stride);graph.read(reinterpret_cast<char*>(raw.data()),raw.size()*4);if(!graph)throw std::runtime_error("graph full source block");
    if(!g){if(v){int hd=-1,hc=-1;for(int z=d;z>=0&&hc<0;z--)for(int w=0;w<words[0];w++){uint32_t nz=0;for(int b=0;b<5;b++)nz|=raw[b*stride+z*words[0]+w];if(nz){hd=z;hc=32*w+__builtin_ctz(nz);break;}}
      if(hd!=d||hc!=c||BitOps::get(raw,stride,d*words[0]*32+c)!=lc)throw std::runtime_error("original image leading identity");
      v->g.resize(1034*jt::L);for(int k=0;k<jt::L;k++)for(int i=0;i<1034;i++){int a=0;for(int z=0;z<=d;z++)a=(a+pw[z][k]*BitOps::get(raw,stride,z*words[0]*32+i))%31;v->g[k*1034+i]=a*ops.inv[lc]%31;}
     }else for(auto a:raw)if(a)throw std::runtime_error("source-leading row not a kernel");continue;}
    if(!v)continue;int js=jt::L*words[g];Row jets(5*js);
    for(int k=0;k<jt::L;k++)for(int z=0;z<layers;z++){int a=pw[z][k]*ops.inv[lc]%31;if(a)sb::scalar(ops,jets,js,k*words[g],raw,stride,z*words[g],words[g],a);}
    for(int i=0;i<counts[g];i++){VEntry e{};e.source=dict[g][i];bool nz=false;for(int k=0;k<jt::L;k++){e.coefficient[k]=BitOps::get(jets,js,k*words[g]*32+i);nz|=e.coefficient[k]!=0;}if(nz){v->entries.push_back(e);entries++;}}
   }
   if(v){V[c]=std::move(v);outputs++;sum+=d;constant+=d==0;}else{kernels++;ksum+=d+96;}
  }
  sb::tail(graph);if(outputs!=1021||kernels!=1174||sum!=716||ksum!=60050||constant!=573)throw std::runtime_error("complete G/V profile");
  std::ofstream go(prefix+"-actual-G-root2.bin",std::ios::binary),vo(prefix+"-actual-V-root2.bin",std::ios::binary);
  go.write("R150SG31",8);for(int v:{31,1034,1021,jt::L})u32(go,v);go.write(binding.data(),64);
  vo.write("R150SV31",8);for(int v:{31,1034,1021,2195,jt::L})u32(vo,v);vo.write(binding.data(),64);
  for(int c=0;c<1034;c++)if(V[c]){auto&v=*V[c];u16(go,c+1);go.put(char(v.degree));go.put(char(v.lc));u16(vo,c+1);vo.put(char(v.degree));vo.put(char(v.lc));u32(vo,v.entries.size());for(auto&e:v.entries){u16(vo,e.source+1);vo.write(reinterpret_cast<const char*>(e.coefficient.data()),jt::L);}}
  for(int k=0;k<jt::L;k++)for(int i=0;i<1034;i++)for(int c=0;c<1034;c++)if(V[c])go.put(char(V[c]->g[k*1034+i]));
  go.close();vo.close();if(!go||!vo)throw std::runtime_error("actual normalized G/V cache save");
 }else{
  std::ifstream in(argv[2],std::ios::binary);if(sb::tag(in)!="R150SV31")throw std::runtime_error("actual V ten-jet cache");
  for(int v:{31,1034,1021,2195})if(sb::get(in,4)!=uint64_t(v))throw std::runtime_error("V cache dimensions");int cacheLength=sb::get(in,4);if(cacheLength<jt::L||cacheLength>50)throw std::runtime_error("V cache Taylor precision");
  std::string old(64,' ');in.read(old.data(),64);if(old!=binding)throw std::runtime_error("same whole local input binding");int previous=0,sum=0;
  for(int r=0;r<1021;r++){int c=sb::get(in,2),d=sb::get(in,1),lc=sb::get(in,1),n=sb::get(in,4);if(c<=previous||c>1034||d>8||lc<1||lc>30||n>2195)throw std::runtime_error("actual cached V column");previous=c;sum+=d;auto v=std::make_unique<VRow>();v->degree=d;v->lc=lc;v->entries.resize(n);std::vector<bool>seen(2195);
   for(auto&e:v->entries){int i=sb::get(in,2)-1;if(i<0||i>=2195||seen[i])throw std::runtime_error("cached V original source");seen[i]=true;e.source=i;for(int k=0;k<cacheLength;k++){int a=sb::get(in,1);if(a>30)throw std::runtime_error("cached V coefficient");e.coefficient[k]=a;}}entries+=n;V[c-1]=std::move(v);
  }sb::tail(in);if(sum!=716)throw std::runtime_error("cached image row degree sum");
 }
 jt::Packed C;C.kind=1;C.bound=first?177:0;C.rows.assign(2195,Row(5*jt::S));std::string checkpoint=prefix+"-vq-checkpoint.bin";{std::ifstream in(checkpoint);if(in)C=jt::readPacked(checkpoint,2195,model,lab,binding);}
 if(C.kind!=1||C.bound!=(first?177:0)||C.done<0||C.done>1021)throw std::runtime_error("VQ checkpoint scope");int resumed=C.done;uint64_t products=0;
 std::ifstream q(argv[3],std::ios::binary);auto magic=sb::tag(q);
 if(first){if(magic!="R150IQ31")throw std::runtime_error("same full global200 Q");for(int v:{1034,1021,200,85})if(sb::get(q,4)!=uint64_t(v))throw std::runtime_error("same global200 Q dimensions");}
 else{if(magic!="R150SQ31")throw std::runtime_error("complete local G solution");for(int v:{31,1021,jt::NT,jt::L})if(sb::get(q,4)!=uint64_t(v))throw std::runtime_error("full ten-jet Q dimensions");std::string b(64,' ');q.read(b.data(),64);if(b!=binding)throw std::runtime_error("local Q source binding");for(int j=0;j<jt::NT;j++)if(sb::get(q,2)!=uint64_t(jt::label(lab,j)))throw std::runtime_error("local Q labels");}
 int previous=0;
 for(int r=0;r<1021;r++){
  int c=sb::get(q,2),d=sb::get(q,1),lc=sb::get(q,1);if(c<=previous||c>1034||!V[c-1]||d!=V[c-1]->degree||lc!=V[c-1]->lc)throw std::runtime_error("actual monic G/V pairing");previous=c;Triple packed;packed[0].resize(5*jt::S);
  if(first){for(int j=0;j<200;j++){int n=sb::get(q,2);if(n>originalLabels[j].cost-d+1)throw std::runtime_error("same global Q degree");std::vector<uint8_t>poly(n);for(auto&a:poly){a=sb::get(q,1);if(a>30)throw std::runtime_error("global Q coefficient");}if(n&&!poly.back())throw std::runtime_error("global Q trailing zero");
    if(targetIndex.count(originalLabels[j].head)&&r>=resumed){int target=targetIndex.at(originalLabels[j].head);auto a=jt::evaluate(poly,pw);for(int k=0;k<jt::L;k++)BitOps::set(packed[0],jt::S,k*jt::W*32+target,a[k]);}
   }}else for(int k=0;k<jt::L;k++)for(int j=0;j<jt::NT;j++){int a=sb::get(q,1);if(a>30)throw std::runtime_error("local Q field coefficient");if(r>=resumed)BitOps::set(packed[0],jt::S,k*jt::W*32+j,a);}
  if(r<resumed)continue;BitOps::refresh(packed,jt::S,0);
  for(auto&e:V[c-1]->entries){jt::Co a{};for(int k=0;k<jt::L;k++)a[k]=e.coefficient[k];jt::muladd(C.rows[e.source],packed,a,ops);products++;}
  if((r+1)%100==0||r+1==1021||jt::stopped){C.done=r+1;jt::writePacked(checkpoint,C,model,lab,binding);std::cout<<"{\"phase\":\"saturated-runtime-jet-VQ-checkpoint\",\"mode\":\""<<mode<<"\",\"completedImageRows\":"<<r+1<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;if(jt::stopped)return 124;}
 }
 sb::tail(q);if(first)jt::compareOldPrefix(argv[5],C,model,lab);
 jt::writePacked(prefix+"-original2195-source-jets.bin",C,model,lab,binding);
 std::ofstream meta(prefix+"-vq.json");meta<<"{\"status\":\"completed\",\"mode\":\""<<mode<<"\",\"targets\":"<<jt::NT<<",\"TaylorCenter\":2,\"TaylorPrecision\":"<<jt::L<<",\"sourceRows\":2195,\"completeImageRows\":1021,\"actualMonicGSourcePairingVerified\":true,\"oldTenSourceJetsCompared\":"<<((first&&std::string(argv[5])!="-")?"true":"false")<<",\"globalSourceCostBound\":"<<C.bound<<",\"globalSourceBoundApplies\":"<<(first?"true":"false")<<",\"resumedImageRows\":"<<resumed<<",\"cachedVEntries\":"<<entries<<",\"processedJetProducts\":"<<products<<",\"bindingSHA256\":\""<<binding<<"\",\"elapsedSeconds\":"<<elapsed()<<"}\n";meta.close();if(!meta)throw std::runtime_error("VQ receipt");
 std::cout<<"{\"status\":\"saturated-runtime-jet-VQ-complete\",\"mode\":\""<<mode<<"\",\"elapsedSeconds\":"<<elapsed()<<"}\n";return 0;
}catch(const std::exception&e){std::cerr<<"R150_SATURATED_RUNTIME_VQ_FAILED "<<e.what()<<"\n";return 1;}}
