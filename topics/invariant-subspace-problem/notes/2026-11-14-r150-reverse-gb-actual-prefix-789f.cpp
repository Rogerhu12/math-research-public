// One bounded exact reverse replay, with a full live-slot checkpoint.
// It uses the complete GQ=hT certificate and the unchanged original GB DAG.
#define main r150_frozen_reverse_bound_main
#include "2026-11-14-r150-reverse-gb-bound-789f.cpp"
#undef main
#define main r150_frozen_normal_form_main
#include "2026-11-14-r150-native-normal-form-789f.cpp"
#undef main
struct RevPolynomial {Row data;int words=0,degree=-1;};
static void rv_u64(std::ostream &out,uint64_t a){for(int k=0;k<8;k++)out.put(char(a>>(8*k)));}

int main(int argc,char **argv){try{
 if(argc!=5)return 2;auto start=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};const double soft=std::stod(argv[4]);if(soft<=0||soft>50)throw std::runtime_error("soft bound must be at most 50 seconds");
 ReverseBytes file(argv[1]);std::string magic;for(int i=0;i<8;i++)magic.push_back(file.at(i));if(magic!="R150GBO1"||file.u32(8)!=2195||file.u32(12)!=1034||file.at(16)!=45)throw std::runtime_error("original complete GB DAG");
 BitOps ops;std::ifstream qfile(argv[2],std::ios::binary);char qm[8];qfile.read(qm,8);if(std::string(qm,8)!="R150GQ31"||bound_u32(qfile)!=1021||bound_u32(qfile)!=9||bound_u32(qfile)!=24)throw std::runtime_error("GB coefficient input");std::vector<uint8_t> h(25);qfile.read(reinterpret_cast<char*>(h.data()),25);
 std::vector<RevPolynomial> initial(1034);std::vector<bool> present(1034);
 for(int b=0;b<1021;b++){
  int c=bound_u16(qfile)-1,bd=qfile.get();if(c<0||c>=1034||bd<0||bd>8||present[c])throw std::runtime_error("coefficient component");present[c]=true;
  std::vector<std::vector<uint8_t>> coefficients(9);int maximum=-1;for(auto &co:coefficients){int len=bound_u16(qfile);if(len>51)throw std::runtime_error("coefficient length");co.resize(len);qfile.read(reinterpret_cast<char*>(co.data()),len);for(auto a:co)if(a>30)throw std::runtime_error("coefficient field");if(len&&!co.back())throw std::runtime_error("trailing zero");maximum=std::max(maximum,len-1);}
  auto &P=initial[c];P.words=maximum+1;P.degree=maximum;P.data.resize(5*P.words);for(int j=0;j<9;j++)for(int k=0;k<int(coefficients[j].size());k++)BitOps::set(P.data,P.words,k*32+j,coefficients[j][k]);
 }
 if(qfile.get()!=EOF)throw std::runtime_error("trailing coefficient data");
 std::vector<std::pair<uint64_t,int>> special;uint64_t count=0,pos=17;
 while(pos<file.size){int tag=file.at(pos),len=recordLength(tag);if(pos+len>file.size)throw std::runtime_error("truncated record");if(tag=='R')count++;else special.push_back({pos+len,len});pos+=len;}
 if(count!=67860206)throw std::runtime_error("complete reduction count");
 std::string prefix=argv[3];std::ofstream output(prefix+"-original-source-coefficients.bin",std::ios::binary);if(!output)throw std::runtime_error("output open");output.write("R150OC31",8);u32(output,2195);u32(output,9);u32(output,24);output.write(reinterpret_cast<const char*>(h.data()),25);
 auto writePolynomial=[&](std::ostream &out,const RevPolynomial &P){u32(out,uint32_t(P.degree+1));for(int plane=0;plane<5;plane++)for(int k=0;k<=P.degree;k++)u32(out,P.data[plane*P.words+k]);};
 std::vector<RevPolynomial> saved(1034);std::vector<uint32_t> node(1034);std::unordered_map<uint32_t,int> component;RevPolynomial current;Triple cached;bool cacheValid=false;uint32_t currentNode=0;
 uint64_t active=0,wordWork=0,reversed=count,recordCounter=0,liveWords=0,peakLiveWords=0,nonzeroOriginalCoefficients=0;int processed=0,maxIntermediate=-1,maxSource=-1,nonzeroSources=0,si=int(special.size())-1;std::vector<std::array<int,4>> sourceStats;
 bool stopped=false;std::string stopReason="complete";pos=file.size;
 auto actualDegree=[](RevPolynomial &P,int upper){while(upper>=0){uint32_t a=0;for(int plane=0;plane<5;plane++)a|=P.data[plane*P.words+upper];if(a){if(a>>9)throw std::runtime_error("nonzero target padding");return upper;}upper--;}return -1;};
 auto refresh=[&](){cached[0]=current.data;BitOps::refresh(cached,current.words,0);cacheValid=true;};
 std::cout<<"{\"phase\":\"actual-reverse-indexed\",\"reductions\":"<<count<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 while(pos>17){
  if((recordCounter&16383)==0&&elapsed()>=soft){stopped=true;stopReason="soft-time-bound";break;}
  int len=11;if(si>=0&&special[si].first==pos)len=special[si].second;uint64_t p=pos-len;int tag=file.at(p);if(recordLength(tag)!=len)throw std::runtime_error("reverse record alignment");
  if(tag=='F'){
   int c=file.u16(p+1)-1;uint32_t id=file.u32(p+3);int scale=file.at(p+7);if(c<0||c>=1034||node[c]||!present[c]||scale<1||scale>30||component.count(id))throw std::runtime_error("final normalization identity");saved[c]=std::move(initial[c]);if(saved[c].degree>=0)ops.multiple(saved[c].data,saved[c].words,0,scale);node[c]=id;component[id]=c;liveWords+=saved[c].words;
  }else if(tag=='R'){
   uint32_t old=file.u32(p+1),id=file.u32(p+5);int shift=file.at(p+9),a=file.at(p+10);if(currentNode!=2195+reversed||a<1||a>30)throw std::runtime_error("reverse node identity");auto found=component.find(id);if(found==component.end())throw std::runtime_error("saved live source missing");
   if(current.degree>=0){
    auto &P=saved[found->second];int upper=std::max(P.degree,current.degree+shift),required=upper+1;
    if(required>P.words){int words=required+std::min(256,required/8);if((liveWords-P.words+words+current.words)*20>430ull*1024*1024){stopped=true;stopReason="live-polynomial-memory-bound";break;}
     Row expanded(5*words);for(int plane=0;plane<5;plane++)std::copy(P.data.begin()+plane*P.words,P.data.begin()+(plane+1)*P.words,expanded.begin()+plane*words);liveWords+=words-P.words;P.words=words;P.data.swap(expanded);
    }
    if(!cacheValid)refresh();auto rep=ops.rep[31-a];BitOps::add(P.data,P.words,shift,cached[rep.c],current.words,0,current.degree+1,rep.rot,rep.neg);P.degree=actualDegree(P,upper);
    active++;wordWork+=current.degree+1;maxIntermediate=std::max(maxIntermediate,P.degree);peakLiveWords=std::max(peakLiveWords,liveWords+current.words);
   }currentNode=old;reversed--;
  }else if(tag=='S'){
   int c=file.u16(p+1)-1;uint32_t afterCurrent=file.u32(p+3),afterSaved=file.u32(p+7);if(currentNode!=afterCurrent||node[c]!=afterSaved)throw std::runtime_error("swap identity");component.erase(afterSaved);std::swap(currentNode,node[c]);liveWords=liveWords-saved[c].words+current.words;std::swap(current,saved[c]);component[node[c]]=c;cacheValid=false;
  }else if(tag=='B'){
   int c=file.u16(p+1)-1;uint32_t id=file.u32(p+3);if(currentNode||node[c]!=id)throw std::runtime_error("store identity");currentNode=id;current=std::move(saved[c]);saved[c]=RevPolynomial{};liveWords-=current.words;component.erase(id);node[c]=0;cacheValid=false;
  }else if(tag=='Z'){
   if(currentNode)throw std::runtime_error("zero identity");currentNode=file.u32(p+1);current=RevPolynomial{};cacheValid=false;
  }else if(tag=='I'){
   int index=file.u32(p+1)-1,raw=file.u32(p+5);if(index<0||index>=2195||currentNode!=uint32_t(index+1)||raw<1||raw>6188)throw std::runtime_error("original source identity");
   u32(output,index+1);u32(output,raw);writePolynomial(output,current);int nnz=0;for(int k=0;k<=current.degree;k++){uint32_t bits=0;for(int plane=0;plane<5;plane++)bits|=current.data[plane*current.words+k];nnz+=__builtin_popcount(bits);}
   sourceStats.push_back({index+1,raw,current.degree,nnz});nonzeroOriginalCoefficients+=nnz;if(nnz)nonzeroSources++;maxSource=std::max(maxSource,current.degree);current=RevPolynomial{};currentNode=0;cacheValid=false;processed++;
   if(processed%50==0||processed==2195)std::cout<<"{\"phase\":\"actual-reverse-prefix\",\"processedSources\":"<<processed<<",\"remainingArithmeticRecords\":"<<reversed<<",\"maximumSourceDegree\":"<<maxSource<<",\"maximumIntermediateDegree\":"<<maxIntermediate<<",\"activeArithmeticRecords\":"<<active<<",\"coefficientWordWork\":"<<wordWork<<",\"liveCoefficientBytes\":"<<(liveWords*20)<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
  }
  if(si>=0&&special[si].first==pos)si--;pos=p;recordCounter++;
 }
 bool complete=pos==17;if(complete&&(reversed||si!=-1||processed!=2195||currentNode||!component.empty()))throw std::runtime_error("complete replay state mismatch");output.close();if(!output)throw std::runtime_error("coefficient output failed");
 std::ofstream checkpoint(prefix+"-checkpoint.bin",std::ios::binary),metadata(prefix+"-replay.json");if(!checkpoint||!metadata)throw std::runtime_error("checkpoint output open");
 checkpoint.write("R150RV31",8);u32(checkpoint,1);rv_u64(checkpoint,pos);rv_u64(checkpoint,reversed);u32(checkpoint,si+1);u32(checkpoint,processed);u32(checkpoint,component.size());
 for(int c=0;c<1034;c++)if(node[c]){u16(checkpoint,c+1);u32(checkpoint,node[c]);writePolynomial(checkpoint,saved[c]);}u32(checkpoint,currentNode);writePolynomial(checkpoint,current);checkpoint.close();if(!checkpoint)throw std::runtime_error("checkpoint write failed");
 metadata<<"{\"format\":\"r150-exact-reverse-live-slot-v1\",\"status\":\""<<(complete?"completed":"prefix-only")<<"\",\"field\":31,\"originalSources\":2195,\"completedSources\":"<<processed<<",\"stopReason\":\""<<stopReason<<"\",\"remainingArithmeticRecords\":"<<reversed<<",\"maximumOriginalCoefficientDegree\":"<<maxSource<<",\"maximumActualIntermediateDegree\":"<<maxIntermediate<<",\"nonzeroOriginalCoefficients\":"<<nonzeroOriginalCoefficients<<",\"nonzeroCompletedSources\":"<<nonzeroSources<<",\"activeArithmeticRecords\":"<<active<<",\"coefficientWordWork\":"<<wordWork<<",\"peakLiveCoefficientBytes\":"<<peakLiveWords*20<<",\"sourceStats\":[";
 for(size_t i=0;i<sourceStats.size();i++){if(i)metadata<<",";auto a=sourceStats[i];metadata<<"["<<a[0]<<","<<a[1]<<","<<a[2]<<","<<a[3]<<"]";}metadata<<"],\"meaning\":\"An exact reverse transpose of the saved unit row operations. A prefix retains both all processed original coefficients and the complete remaining live coefficient state; only completed spans all 2195 original sources. The recorded degree and nonzero counts are actual F31 coefficients after all cancellations in the processed prefix.\",\"elapsedSeconds\":"<<elapsed()<<"}\n";metadata.close();if(!metadata)throw std::runtime_error("metadata write failed");
 std::cout<<"{\"status\":\""<<(complete?"original-source-coefficients-complete":"original-source-reverse-prefix-only")<<"\",\"completedSources\":"<<processed<<",\"maximumOriginalCoefficientDegree\":"<<maxSource<<",\"maximumActualIntermediateDegree\":"<<maxIntermediate<<",\"nonzeroOriginalCoefficients\":"<<nonzeroOriginalCoefficients<<",\"activeArithmeticRecords\":"<<active<<",\"coefficientWordWork\":"<<wordWork<<",\"peakLiveCoefficientBytes\":"<<peakLiveWords*20<<",\"stopReason\":\""<<stopReason<<"\",\"elapsedSeconds\":"<<elapsed()<<"}\n";
 return 0;
}catch(const std::exception &e){std::cerr<<"ACTUAL_REVERSE_PREFIX_FAILED "<<e.what()<<"\n";return 1;}}
