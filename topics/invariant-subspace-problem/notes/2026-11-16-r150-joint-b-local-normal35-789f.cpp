// Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.
// Complete original-prebasis and G normal forms in the two actual Taylor rings.
// All197 targets are packed, and both local source identities are multiplied back.
#include "2026-11-16-r150-joint-b-local-common35-789f.hpp"
#include <filesystem>
struct Phase {int hi=0,lo=0,hw=0,lw=0,nw=0;std::vector<std::unique_ptr<Triple>>basis;std::vector<int>id,pivots;std::unordered_map<uint64_t,int>high,low;};
struct Cell {int degree,component,a;};
int main(int argc,char**argv){try{
 if(argc!=7)return 2;std::signal(SIGTERM,jt::signal);std::signal(SIGINT,jt::signal);
 auto started=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count();};
 sb::Model model(argv[1]);auto lab=jt::labels(argv[4]);std::string prefix=argv[5],binding=argv[6];BitOps ops;auto pw=jt::powers(31,256);
 std::array<Phase,6>phases;std::ofstream fwd(prefix+"-forward.bin",std::ios::binary),back(prefix+"-backward.bin",std::ios::binary);fwd.write("R150PB31",8);u32(fwd,3333);back.write("R150RJ31",8);u32(back,3333);int generated=0;uint64_t fops=0,bops=0;
 for(int d=2;d<=5;d++){
  auto&P=phases[d];P.hi=model.mon[d].size();P.lo=model.mon[d-1].size();P.hw=(P.hi+31)/32;P.lw=(P.lo+31)/32;P.nw=P.hw+11*P.lw;P.basis.resize(P.hi);P.id.resize(P.hi);
  for(int i=0;i<P.hi;i++)P.high[model.mon[d][i]]=i;for(int i=0;i<P.lo;i++)P.low[model.mon[d-1][i]]=i;
  for(auto&s:model.pre){if(degree(s.mult)+2!=d)continue;Row row(5*P.nw);
   for(int k=0;k<66;k++){auto[a,b]=model.quadratic[k];BitOps::set(row,P.nw,P.high.at(s.mult+model.var[a]+model.var[b]),model.Q[s.e][k]);}
   for(int v=0;v<11;v++)for(int k=0;k<11;k++)BitOps::set(row,P.nw,(P.hw+k*P.lw)*32+P.low.at(s.mult+model.var[v]),model.L[s.e][v][k]);
   std::vector<std::pair<int,int>>steps;int pivot=-1,value=0;
   for(int c=0;c<P.hi;c++){int a=BitOps::get(row,P.nw,c);if(!a)continue;if(!P.basis[c]){pivot=c;value=a;break;}steps.push_back({P.id[c],a});auto r=ops.rep[31-a];BitOps::add(row,P.nw,c/32,(*P.basis[c])[r.c],P.nw,c/32,P.nw-c/32,r.rot,r.neg);fops++;}
   if(pivot<0||model.mon[d][pivot]!=s.pivot)throw std::runtime_error("same original constant pivot profile");int scale=ops.inv[value];if(value!=1)ops.multiple(row,P.nw,pivot/32,scale);if(BitOps::get(row,P.nw,pivot)!=1)throw std::runtime_error("original unit pivot");P.id[pivot]=++generated;P.pivots.push_back(pivot);
   u32(fwd,s.raw);fwd.put(char(scale));u32(fwd,steps.size());for(auto[i,a]:steps){u16(fwd,i);fwd.put(char(a));}
   auto t=std::make_unique<Triple>();(*t)[0]=std::move(row);BitOps::refresh(*t,P.nw,pivot/32);P.basis[pivot]=std::move(t);
  }
  std::sort(P.pivots.begin(),P.pivots.end());
  for(int i=int(P.pivots.size())-1;i>=0;i--){int c=P.pivots[i];auto&t=*P.basis[c];std::vector<std::pair<int,int>>steps;for(int j=i+1;j<int(P.pivots.size());j++){int q=P.pivots[j],a=BitOps::get(t[0],P.nw,q);if(!a)continue;steps.push_back({P.id[q],a});auto r=ops.rep[31-a];BitOps::add(t[0],P.nw,q/32,(*P.basis[q])[r.c],P.nw,q/32,P.nw-q/32,r.rot,r.neg);bops++;}BitOps::refresh(t,P.nw,c/32);u16(back,P.id[c]);u32(back,steps.size());for(auto[j,a]:steps){u16(back,j);back.put(char(a));}}
  for(int c:P.pivots)for(int q:P.pivots)if(BitOps::get((*P.basis[c])[0],P.nw,q)!=(c==q))throw std::runtime_error("same original constant-block RREF");
  std::cout<<"{\"phase\":\"same-original-local-prebasis\",\"mDegree\":"<<d<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 }
 fwd.close();back.close();if(!fwd||!back||generated!=3333||fops!=782976||bops!=1010703)throw std::runtime_error("complete unchanged original prebasis DAG");
 std::vector<Row>raw(4367,Row(5*jt::S));std::ifstream rhs(argv[2],std::ios::binary);if(sb::tag(rhs)!="R150SD31")throw std::runtime_error("actual original delta jet file");for(int v:{31,jt::NT,4367,jt::L})if(sb::get(rhs,4)!=uint64_t(v))throw std::runtime_error("actual original delta jet dimensions");for(int j=0;j<jt::NT;j++)if(sb::get(rhs,2)!=uint64_t(jt::label(lab,j)))throw std::runtime_error("same197 delta labels");
 for(int c=0;c<4367;c++){if(sb::get(rhs,8)!=model.keys[c])throw std::runtime_error("all4367 original delta monomials");for(int k=0;k<jt::L;k++)for(int j=0;j<jt::NT;j++){int a=sb::get(rhs,1);if(a>30)throw std::runtime_error("actual delta field jet");BitOps::set(raw[c],jt::S,k*jt::W*32+j,a);}}sb::tail(rhs);auto original=raw;
 std::vector<std::pair<int,int>>order;std::vector<uint64_t>freeKeys;for(int d=5;d>=1;d--)for(int c=0;c<int(model.mon[d].size());c++){if(d>=2&&phases[d].basis[c])order.push_back({d,c});else freeKeys.push_back(model.mon[d][c]);}if(order.size()!=3333||freeKeys.size()!=1034)throw std::runtime_error("same original quotient monomial dictionary");
 int completed=0;std::string checkpoint=prefix+"-normal-checkpoint.bin",trace=prefix+"-local-prebasis-source-jets.bin";
 {std::ifstream in(checkpoint,std::ios::binary);if(in){if(sb::tag(in)!="R150SM31")throw std::runtime_error("local normal checkpoint magic");for(int v:{31,jt::NT,jt::L,4367})if(sb::get(in,4)!=uint64_t(v))throw std::runtime_error("local normal checkpoint dimensions");completed=sb::get(in,4);if(completed<0||completed>3333)throw std::runtime_error("local normal checkpoint prefix");std::string old(64,' ');in.read(old.data(),64);if(old!=binding)throw std::runtime_error("local normal checkpoint input binding");for(auto&r:raw){in.read(reinterpret_cast<char*>(r.data()),r.size()*4);if(!in)throw std::runtime_error("actual local normal checkpoint array");jt::padding(r);}sb::tail(in);}}
 auto save=[&](int done){std::ofstream out(checkpoint+".tmp",std::ios::binary);out.write("R150SM31",8);for(int v:{31,jt::NT,jt::L,4367,done})u32(out,v);out.write(binding.data(),64);for(auto&r:raw)out.write(reinterpret_cast<const char*>(r.data()),r.size()*4);out.close();if(!out||std::rename((checkpoint+".tmp").c_str(),checkpoint.c_str()))throw std::runtime_error("atomic actual local normal checkpoint");};
 std::ofstream tr;if(completed){size_t n=8+4*4+jt::NT*2+size_t(completed)*(2+5*jt::S*4);if(!std::filesystem::exists(trace)||std::filesystem::file_size(trace)<n)throw std::runtime_error("actual completed local source trace missing");std::filesystem::resize_file(trace,n);tr.open(trace,std::ios::binary|std::ios::app);}else{tr.open(trace,std::ios::binary);tr.write("R150SN31",8);for(int v:{31,3333,jt::NT,jt::L})u32(tr,v);for(int j=0;j<jt::NT;j++)u16(tr,jt::label(lab,j));}if(!tr)throw std::runtime_error("local prebasis trace open");
 auto basisAdd=[&](std::vector<Row>&dest,const Triple&current,int d,int pivot,int sign,bool includePivot){
  auto&P=phases[d];const Row&b=(*P.basis[pivot])[0];
  for(int c=0;c<P.hi;c++){if(c==pivot&&!includePivot)continue;int a=BitOps::get(b,P.nw,c);if(!a)continue;auto r=ops.rep[sign>0?a:31-a];int ix=model.component.at(model.mon[d][c]);BitOps::add(dest[ix],jt::S,0,current[r.c],jt::S,0,jt::S,r.rot,r.neg);}
  for(int c=0;c<P.lo;c++){jt::Co a{};for(int e=0;e<=10;e++){int v=BitOps::get(b,P.nw,(P.hw+e*P.lw)*32+c);if(v)for(int k=0;k<jt::L;k++)a[k]=(a[k]+v*pw[e][k])%31;}if(std::any_of(a.begin(),a.end(),[](int v){return v!=0;}))jt::muladd(dest[model.component.at(model.mon[d-1][c])],current,a,ops,sign);}
 };
 for(int z=completed;z<3333;z++){
  auto[d,c]=order[z];int i=model.component.at(model.mon[d][c]);Triple current;current[0]=raw[i];BitOps::refresh(current,jt::S,0);u16(tr,phases[d].id[c]);tr.write(reinterpret_cast<const char*>(current[0].data()),current[0].size()*4);std::fill(raw[i].begin(),raw[i].end(),0);basisAdd(raw,current,d,c,-1,false);
  if((z+1)%500==0||z==3332||jt::stopped){tr.flush();if(!tr)throw std::runtime_error("actual local NF source trace flush");save(z+1);std::cout<<"{\"phase\":\"all197-local-prebasis-normal-form\",\"completedPivots\":"<<z+1<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;if(jt::stopped)return 124;}
 }
 tr.close();if(!tr)throw std::runtime_error("complete local source trace write");
 for(auto[d,c]:order)for(auto a:raw[model.component.at(model.mon[d][c])])if(a)throw std::runtime_error("local NF retained a pivot");
 // Multiply the saved local prebasis cochain back in all4367 original slots.
 auto verify=raw;{std::ifstream in(trace,std::ios::binary);if(sb::tag(in)!="R150SN31")throw std::runtime_error("local trace readback");for(int v:{31,3333,jt::NT,jt::L})if(sb::get(in,4)!=uint64_t(v))throw std::runtime_error("local trace readback dimensions");for(int j=0;j<jt::NT;j++)if(sb::get(in,2)!=uint64_t(jt::label(lab,j)))throw std::runtime_error("local trace readback labels");for(auto[d,c]:order){if(sb::get(in,2)!=uint64_t(phases[d].id[c]))throw std::runtime_error("same local prebasis trace identity");Triple current;current[0].resize(5*jt::S);in.read(reinterpret_cast<char*>(current[0].data()),current[0].size()*4);if(!in)throw std::runtime_error("complete local cochain");BitOps::refresh(current,jt::S,0);basisAdd(verify,current,d,c,1,true);}sb::tail(in);}if(verify!=original)throw std::runtime_error("full original local prebasis source identity failed");verify.clear();verify.shrink_to_fit();original.clear();original.shrink_to_fit();

if(jt::RING==2){
 // Full ten-jet RHS and its exact cochain, before ANY G/Smith solution.
 std::ofstream nf(prefix+"-original1034-root2.bin",std::ios::binary);nf.write("R150SF31",8);
 for(int v:{31,1034,jt::NT,jt::L})u32(nf,v);nf.write(binding.data(),64);for(int j=0;j<jt::NT;j++)u16(nf,jt::label(lab,j));for(auto key:freeKeys)sb::put(nf,key,8);
 for(int k=0;k<jt::L;k++)for(int c=0;c<1034;c++)for(int j=0;j<jt::NT;j++)nf.put(char(BitOps::get(raw[model.component.at(freeKeys[c])],jt::S,k*jt::W*32+j)));
 nf.close();if(!nf)throw std::runtime_error("complete original1034 ten-jet RHS");
 std::ofstream meta(prefix+"-local-normal.json");meta<<"{\"status\":\"completed\",\"targets\":"<<jt::NT<<",\"TaylorCenter\":2,\"TaylorPrecision\":"<<jt::L<<",\"originalOutputComponents\":4367,\"originalQuotientComponents\":1034,\"sameOriginalConstantPrebasis\":true,\"forwardOperations\":782976,\"backwardOperations\":1010703,\"fullLocalPrebasisSourceIdentity\":true,\"localSmithSolutionClaimed\":false,\"bindingSHA256\":\""<<binding<<"\",\"resumedLocalPivots\":"<<completed<<",\"elapsedSeconds\":"<<elapsed()<<"}\n";meta.close();if(!meta)throw std::runtime_error("original ten-jet NF receipt");
 std::cout<<"{\"status\":\"saturated-runtime-root2-normal-form-complete\",\"elapsedSeconds\":"<<elapsed()<<"}\n";return 0;
}else{
 // Exact CRT: jet order is (1,0..2), (2,0..4); polynomial degree is <8.
 int aug[8][16]{};for(int k=0;k<jt::L;k++){for(int d=0;d<8;d++)aug[k][d]=pw[d][k];aug[k][8+k]=1;}
 for(int c=0;c<8;c++){int r=c;while(r<8&&!aug[r][c])r++;if(r==8)throw std::runtime_error("two genuine Taylor rings CRT singular");for(int j=0;j<16;j++)std::swap(aug[r][j],aug[c][j]);int v=ops.inv[aug[c][c]];for(int j=0;j<16;j++)aug[c][j]=aug[c][j]*v%31;for(int r2=0;r2<8;r2++)if(r2!=c){v=aug[r2][c];for(int j=0;j<16;j++)aug[r2][j]=sb::mod(aug[r2][j]-v*aug[c][j]);}}
 std::vector<Row>X(1034,Row(5*jt::S));
 for(int c=0;c<1034;c++){const Row&source=raw[model.component.at(freeKeys[c])];for(int d=0;d<8;d++)for(int k=0;k<jt::L;k++)if(int a=aug[d][8+k])sb::scalar(ops,X[c],jt::S,d*jt::W,source,jt::S,k*jt::W,jt::W,a);}
 auto beforeG=X;auto G=sb::graphImage(argv[3],ops);std::vector<std::vector<Cell>>sparse(1034);std::vector<Row>quotients(1034);int heads=0,sum=0;
 for(int c=0;c<1034;c++)if(G[c]){heads++;sum+=G[c]->degree;quotients[c].resize(5*jt::S);for(int d=0;d<=G[c]->degree;d++)for(int k=0;k<1034;k++)if(int a=BitOps::get(G[c]->row,G[c]->stride,d*33*32+k))sparse[c].push_back({d,k,a});}if(heads!=1021||sum!=716)throw std::runtime_error("same complete global G");
 auto addG=[&](std::vector<Row>&dest,int c,int shift,const Triple&co,int sign){for(auto&e:sparse[c]){int d=shift+e.degree;if(d>7)throw std::runtime_error("global degree order increased a degree7 representative");auto r=ops.rep[sign>0?e.a:31-e.a];BitOps::add(dest[e.component],jt::S,d*jt::W,co[r.c],jt::W,0,jt::W,r.rot,r.neg);}};
 for(int d=7;d>=0;d--)for(int c=0;c<1034;c++)if(G[c]&&G[c]->degree<=d){Triple co;co[0].resize(5*jt::W);for(int b=0;b<5;b++)std::copy_n(X[c].begin()+b*jt::S+d*jt::W,jt::W,co[0].begin()+b*jt::W);BitOps::refresh(co,jt::W,0);int shift=d-G[c]->degree;BitOps::add(quotients[c],jt::S,shift*jt::W,co[0],jt::W,0,jt::W,0,0);addG(X,c,shift,co,-1);}
 for(int c=0;c<1034;c++)if(G[c])for(int d=G[c]->degree;d<8;d++)for(int b=0;b<5;b++)for(int w=0;w<jt::W;w++)if(X[c][b*jt::S+d*jt::W+w])throw std::runtime_error("nonstandard local G remainder");
 auto checkG=X;for(int c=0;c<1034;c++)if(G[c])for(int shift=0;shift+G[c]->degree<8;shift++){Triple co;co[0].resize(5*jt::W);for(int b=0;b<5;b++)std::copy_n(quotients[c].begin()+b*jt::S+shift*jt::W,jt::W,co[0].begin()+b*jt::W);BitOps::refresh(co,jt::W,0);addG(checkG,c,shift,co,1);}if(checkG!=beforeG)throw std::runtime_error("full local G quotient identity failed");
 std::ofstream qo(prefix+"-local-G-quotient-jets.bin",std::ios::binary);qo.write("R150SL31",8);for(int v:{31,1034,1021,jt::NT,8})u32(qo,v);for(int j=0;j<jt::NT;j++)u16(qo,jt::label(lab,j));for(int c=0;c<1034;c++)if(G[c]){u16(qo,c+1);qo.put(char(G[c]->degree));qo.put(char(G[c]->originalLC));qo.write(reinterpret_cast<const char*>(quotients[c].data()),quotients[c].size()*4);}qo.close();if(!qo)throw std::runtime_error("actual complete local G cochain save");
 std::vector<std::pair<int,int>>coordinates;for(int d=0;d<8;d++)for(int c=0;c<1034;c++)if(!G[c]||d<G[c]->degree)coordinates.push_back({c+1,d});if(coordinates.size()!=820)throw std::runtime_error("full820 standard dictionary");
 std::ofstream out(prefix+"-standard-state.bin",std::ios::binary);out.write("R150SE31",8);for(int v:{31,820,jt::NT,8})u32(out,v);for(int j=0;j<jt::NT;j++)u16(out,jt::label(lab,j));for(auto[c,d]:coordinates){u16(out,c);out.put(char(d));}for(auto[c,d]:coordinates)for(int j=0;j<jt::NT;j++)out.put(char(BitOps::get(X[c-1],jt::S,d*jt::W*32+j)));out.close();if(!out)throw std::runtime_error("actual all197 standard states save");
 std::ofstream meta(prefix+"-local-normal.json");meta<<"{\"format\":\"r150-complete197-two-ring-original-and-G-normal-form-v1\",\"status\":\"completed\",\"targets\":"<<jt::NT<<",\"originalOutputComponents\":4367,\"standardStateDimension\":820,\"sameOriginalConstantPrebasis\":true,\"forwardOperations\":782976,\"backwardOperations\":1010703,\"fullLocalPrebasisSourceIdentity\":true,\"fullLocalGQuotientIdentity\":true,\"allRemaindersStandard\":true,\"all104LocalFreeChecksDone\":false,\"bindingSHA256\":\""<<binding<<"\",\"resumedLocalPivots\":"<<completed<<",\"elapsedSeconds\":"<<elapsed()<<"}\n";meta.close();if(!meta)throw std::runtime_error("actual local NF receipt");std::cout<<"{\"status\":\"saturated-runtime-two-ring-state-complete\",\"elapsedSeconds\":"<<elapsed()<<"}\n";return 0;
}
}catch(const std::exception&e){std::cerr<<"R150_SATURATED_RUNTIME_NORMAL_FAILED "<<e.what()<<"\n";return 1;}}
