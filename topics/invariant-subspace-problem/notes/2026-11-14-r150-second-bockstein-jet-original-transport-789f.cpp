// The actual global B(J_beta-H*VQ) source transport, evaluated in both rings.
// Every checkpoint contains the true raw and prebasis coefficient arrays.
#include "2026-11-14-r150-second-bockstein-jet-common-789f.hpp"
struct Back {int basis;std::vector<std::pair<uint16_t,uint8_t>> steps;};
struct Front {int raw,scale;std::vector<std::pair<uint16_t,uint8_t>> steps;};
int main(int argc,char**argv){try{
 if(argc!=10)return 2;std::signal(SIGTERM,jt::signal);std::signal(SIGINT,jt::signal);
 auto start=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 sb::Model model(argv[1]);auto lab=jt::labels(argv[2]);std::string prefix=argv[8],binding=argv[9];BitOps ops;auto pw=jt::powers(31,256);
 auto C=jt::readPacked(argv[3],2195,model,lab,binding);if(C.kind!=1||C.done!=1021||C.bound!=177)throw std::runtime_error("complete same-global VQ jets required");
 std::vector<Row>raw(6188,Row(5*jt::S)),beta(3333,Row(5*jt::S));std::vector<bool>occupied(6188);
 for(int i=0;i<2195;i++){int r=model.sources[i].raw-1;if(occupied[r])throw std::runtime_error("actual original source collision");occupied[r]=true;raw[r]=C.rows[i];}
 for(auto &s:model.pre){if(occupied[s.raw-1])throw std::runtime_error("actual prebasis/source collision");occupied[s.raw-1]=true;}if(std::count(occupied.begin(),occupied.end(),true)!=5528)throw std::runtime_error("actual selected5528 sources");
 int phase=1,next=0;std::string checkpoint=prefix+"-transport-checkpoint.bin";
 {std::ifstream in(checkpoint,std::ios::binary);if(in){if(sb::tag(in)!="R150JT31")throw std::runtime_error("transport checkpoint magic");for(int v:{31,6188,3333,198,8,jt::S})if(sb::get(in,4)!=uint64_t(v))throw std::runtime_error("transport checkpoint dimensions");phase=sb::get(in,4);next=sb::get(in,4);if(phase<1||phase>5||next<0||next>3333)throw std::runtime_error("transport checkpoint stage");std::string old(64,' ');in.read(old.data(),64);if(old!=binding)throw std::runtime_error("transport checkpoint binding");for(int j=0;j<198;j++)if(sb::get(in,2)!=uint64_t(lab[j].head))throw std::runtime_error("transport checkpoint labels");for(auto *v:{&raw,&beta})for(auto &r:*v){in.read(reinterpret_cast<char*>(r.data()),r.size()*4);if(!in)throw std::runtime_error("transport checkpoint arrays");jt::padding(r);}sb::tail(in);}}
 auto save=[&](int ph,int nx){
  phase=ph;next=nx;std::ofstream out(checkpoint+".tmp",std::ios::binary);out.write("R150JT31",8);for(int v:{31,6188,3333,198,8,jt::S,phase,next})u32(out,v);out.write(binding.data(),64);for(int j=0;j<198;j++)u16(out,lab[j].head);for(auto *v:{&raw,&beta})for(auto&r:*v)out.write(reinterpret_cast<const char*>(r.data()),r.size()*4);out.close();if(!out||std::rename((checkpoint+".tmp").c_str(),checkpoint.c_str()))throw std::runtime_error("atomic transport checkpoint save");std::ofstream meta(prefix+"-transport-checkpoint.json");meta<<"{\"phase\":"<<phase<<",\"nextRecordZeroBased\":"<<next<<",\"actualSourceAndPrebasisArraysSaved\":true,\"bindingSHA256\":\""<<binding<<"\",\"elapsedSeconds\":"<<elapsed()<<"}\n";std::cout<<"{\"phase\":\"original-source-jet-transport-checkpoint\",\"stage\":"<<phase<<",\"nextRecord\":"<<next<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 };
 int resumedPhase=phase,resumedNext=next;uint64_t normalOps=0,rhsOps=0,bops=0,fops=0;
 {jt::Buffer in(argv[4]);in.magic("R150NR31");if(in.get(4)!=2204)throw std::runtime_error("complete original normal trace");int from=phase==1?next:2204;
  for(int i=0;i<2204;i++){
   int r=in.get(4),label=in.get(2),steps=in.get(4);if(i<2195?(r!=model.sources[i].raw||label):(r||label!=i-2195+2))throw std::runtime_error("original full source H mapping");
   std::vector<Triple> shifted;if(i>=from&&i<2195){Triple base;base[0]=C.rows[i];BitOps::refresh(base,jt::S,0);shifted.resize(46);for(int d=0;d<46;d++){shifted[d][0].resize(5*jt::S);jt::muladd(shifted[d][0],base,pw[d],ops);BitOps::refresh(shifted[d],jt::S,0);}}
   for(int k=0;k<steps;k++){
    int b=in.get(2)-1,s=in.get(1),a=in.get(1);if(b<0||b>=3333||s>45||a<1||a>30)throw std::runtime_error("actual normal trace step");
    if(i<2195&&s+model.delta(model.pre[b].raw)>model.delta(r))throw std::runtime_error("global prebasis compensation cost");
    if(i>=from&&i<2195){auto rep=ops.rep[31-a];BitOps::add(beta[b],jt::S,0,shifted[s][rep.c],jt::S,0,jt::S,rep.rot,rep.neg);}normalOps++;
   }
   if(i>=from&&((i+1)%100==0||i+1==2204||jt::stopped)){save(1,i+1);if(jt::stopped)return 124;}
  }in.tail();if(normalOps!=25305683)throw std::runtime_error("complete original H operation count");
  if(phase==1)save(2,0);
 }
 {jt::Buffer in(argv[5]);in.magic("R150NR31");if(in.get(4)!=200)throw std::runtime_error("complete old200 beta trace");int from=phase==2?next:200;
  std::vector<std::array<int,8>> sum(3333);
  for(int j=0;j<200;j++){
   int r=in.get(4),label=in.get(2),steps=in.get(4);if(r||label!=lab[j].head)throw std::runtime_error("same original beta trace labels");if(j>=from&&j<198)std::fill(sum.begin(),sum.end(),std::array<int,8>{});
   for(int k=0;k<steps;k++){int b=in.get(2)-1,s=in.get(1),a=in.get(1);if(b<0||b>=3333||s>85||a<1||a>30||s+model.delta(model.pre[b].raw)>lab[j].cost)throw std::runtime_error("actual beta trace cost/source");if(j>=from&&j<198)for(int z=0;z<8;z++)sum[b][z]+=a*pw[s][z]%31;rhsOps++;}
   if(j>=from&&j<198){for(int b=0;b<3333;b++)for(int z=0;z<8;z++){int a=sum[b][z]%31;if(a)sb::assign(beta[b],jt::S,z*jt::W*32+j,(BitOps::get(beta[b],jt::S,z*jt::W*32+j)+a)%31);}if((j+1)%10==0||j==197||jt::stopped){save(2,j+1);if(jt::stopped)return 124;}}
  }in.tail();if(phase==2)save(3,0);
 }
 {jt::Buffer in(argv[7]);in.magic("R150RJ31");if(in.get(4)!=3333)throw std::runtime_error("same full backward DAG");std::vector<Back>back(3333);std::vector<bool>seen(3333);
  for(auto&r:back){r.basis=in.get(2)-1;int n=in.get(4);if(r.basis<0||r.basis>=3333||seen[r.basis])throw std::runtime_error("backward actual prebasis map");seen[r.basis]=true;r.steps.resize(n);for(auto&x:r.steps){x.first=in.get(2);x.second=in.get(1);if(x.first<1||x.first>3333||x.first==r.basis+1||x.second<1||x.second>30)throw std::runtime_error("backward actual step");}bops+=n;}in.tail();if(bops!=1010703)throw std::runtime_error("complete backward operation count");
  int from=phase==3?next:3333;for(int i=from;i<3333;i++){auto&r=back[3332-i];Triple current;current[0]=beta[r.basis];BitOps::refresh(current,jt::S,0);for(auto[b,a]:r.steps){auto rep=ops.rep[31-a];BitOps::add(beta[b-1],jt::S,0,current[rep.c],jt::S,0,jt::S,rep.rot,rep.neg);}if((i+1)%100==0||i+1==3333||jt::stopped){save(3,i+1);if(jt::stopped)return 124;}}if(phase==3)save(4,0);
 }
 {jt::Buffer in(argv[6]);in.magic("R150PB31");if(in.get(4)!=3333)throw std::runtime_error("same full forward DAG");std::vector<Front>front(3333);
  for(int i=0;i<3333;i++){auto&r=front[i];r.raw=in.get(4);r.scale=in.get(1);int n=in.get(4);if(r.raw!=model.pre[i].raw||r.scale<1||r.scale>30)throw std::runtime_error("same original forward source");r.steps.resize(n);for(auto&x:r.steps){x.first=in.get(2);x.second=in.get(1);if(x.first<1||x.first>i||x.second<1||x.second>30)throw std::runtime_error("forward actual step");}fops+=n;}in.tail();if(fops!=782976)throw std::runtime_error("complete forward operation count");
  int from=phase==4?next:3333;for(int z=from;z<3333;z++){int i=3332-z;auto&r=front[i];Triple current;current[0]=beta[i];ops.multiple(current[0],jt::S,0,r.scale);BitOps::refresh(current,jt::S,0);BitOps::add(raw[r.raw-1],jt::S,0,current[0],jt::S,0,jt::S,0,0);for(auto[b,a]:r.steps){auto rep=ops.rep[31-a];BitOps::add(beta[b-1],jt::S,0,current[rep.c],jt::S,0,jt::S,rep.rot,rep.neg);}if((z+1)%100==0||z+1==3333||jt::stopped){save(4,z+1);if(jt::stopped)return 124;}}if(phase==4)save(5,0);
 }
 if(phase!=5)throw std::runtime_error("incomplete original jet source transport");
 for(int r=0;r<6188;r++){jt::padding(raw[r]);if(!occupied[r])for(auto a:raw[r])if(a)throw std::runtime_error("unselected original row acquired a jet");}
 jt::Packed result;result.kind=2;result.done=6188;result.bound=177;result.rows=std::move(raw);jt::writePacked(prefix+"-original6188-q-jets.bin",result,model,lab,binding);
 std::ofstream meta(prefix+"-transport.json");meta<<"{\"format\":\"r150-actual-global-prebasis-198-source-jet-transport-v1\",\"status\":\"completed\",\"targets\":198,\"sourceRows\":6188,\"selectedOriginalSources\":5528,\"globalSourceCostBound\":177,\"sameActualGlobalVQAndOriginalPrebasisTransport\":true,\"localArbitrarySolutionChosen\":false,\"normalOperations\":"<<normalOps<<",\"old200RHSOperationsRead\":"<<rhsOps<<",\"backwardOperations\":"<<bops<<",\"forwardOperations\":"<<fops<<",\"resumedStage\":"<<resumedPhase<<",\"resumedNextRecord\":"<<resumedNext<<",\"fullOriginalGlobalMod29791IdentityVerified\":false,\"bindingSHA256\":\""<<binding<<"\",\"elapsedSeconds\":"<<elapsed()<<"}\n";meta.close();if(!meta)throw std::runtime_error("transport receipt save");std::cout<<"{\"status\":\"actual-global198-source-jet-transport-complete\",\"elapsedSeconds\":"<<elapsed()<<"}\n";return 0;
}catch(const std::exception&e){std::cerr<<"ACTUAL_GLOBAL_JET_SOURCE_TRANSPORT_FAILED "<<e.what()<<"\n";return 1;}}
