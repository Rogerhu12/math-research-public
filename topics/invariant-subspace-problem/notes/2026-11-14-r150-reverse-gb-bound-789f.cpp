// Degree/work bound for reverse transposition of the saved GB row operations.
// This never expands the 67-million-node DAG. At most 1034 live row slots.
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
struct ReverseBytes {
 static constexpr uint64_t length=4*1024*1024;
 std::ifstream file;uint64_t size=0,start=UINT64_MAX;std::vector<uint8_t> block;
 explicit ReverseBytes(const std::string &path):file(path,std::ios::binary),block(length){if(!file)throw std::runtime_error("DAG open");file.seekg(0,std::ios::end);size=file.tellg();}
 uint8_t at(uint64_t pos){if(pos>=size)throw std::runtime_error("DAG boundary");uint64_t wanted=pos/length*length;if(wanted!=start){file.clear();file.seekg(wanted);file.read(reinterpret_cast<char*>(block.data()),std::min(length,size-wanted));if(!file)throw std::runtime_error("DAG read");start=wanted;}return block[pos-start];}
 uint32_t u32(uint64_t pos){uint32_t a=0;for(int k=0;k<4;k++)a|=uint32_t(at(pos+k))<<(8*k);return a;}
 uint16_t u16(uint64_t pos){return at(pos)|(at(pos+1)<<8);}
};
static int recordLength(int tag){switch(tag){case'I':return 9;case'B':return 7;case'S':return 11;case'R':return 11;case'Z':return 5;case'F':return 8;default:throw std::runtime_error("unknown GB tag");}}
static uint32_t bound_u32(std::istream &in){uint32_t a=0;for(int k=0;k<4;k++){int c=in.get();if(c<0)throw std::runtime_error("truncated u32");a|=uint32_t(c)<<(8*k);}return a;}
static uint16_t bound_u16(std::istream &in){int a=in.get(),b=in.get();if(a<0||b<0)throw std::runtime_error("truncated u16");return a|(b<<8);}
int main(int argc,char **argv){try{
 if(argc!=4)return 2;auto start=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 ReverseBytes file(argv[1]);std::string magic;for(int i=0;i<8;i++)magic.push_back(file.at(i));if(magic!="R150GBO1"||file.u32(8)!=2195||file.u32(12)!=1034||file.at(16)!=45)throw std::runtime_error("not complete original GB DAG");
 std::ifstream qfile(argv[2],std::ios::binary);char qm[8];qfile.read(qm,8);if(std::string(qm,8)!="R150GQ31"||bound_u32(qfile)!=1021||bound_u32(qfile)!=9||bound_u32(qfile)!=24)throw std::runtime_error("coefficient input");qfile.seekg(25,std::ios::cur);
 std::vector<int> initial(1034,-2);for(int b=0;b<1021;b++){int c=bound_u16(qfile)-1,d=qfile.get();if(c<0||c>=1034||d<0||d>8||initial[c]!=-2)throw std::runtime_error("coefficient component");int maximum=-1;for(int j=0;j<9;j++){int len=bound_u16(qfile),last=0;if(len>51)throw std::runtime_error("coefficient length");for(int k=0;k<len;k++){int a=qfile.get();if(a<0||a>30)throw std::runtime_error("coefficient residue");last=a;}if(len&&!last)throw std::runtime_error("coefficient trailing zero");maximum=std::max(maximum,len-1);}initial[c]=maximum;}
 if(qfile.get()!=EOF)throw std::runtime_error("trailing coefficients");
 std::vector<std::pair<uint64_t,int>> special;uint64_t count=0,pos=17;
 while(pos<file.size){int tag=file.at(pos),len=recordLength(tag);if(pos+len>file.size)throw std::runtime_error("truncated GB record");if(tag=='R')count++;else special.push_back({pos+len,len});pos+=len;}
 if(count!=67860206)throw std::runtime_error("complete reduction count");
 std::cout<<"{\"phase\":\"reverse-indexed\",\"reductions\":"<<count<<",\"nonReductionRecords\":"<<special.size()<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
 std::vector<int> degree(1034,-2),sourceBound(2195,-2),sourceRaw(2195);std::vector<uint32_t> node(1034);std::unordered_map<uint32_t,int> component;
 int currentDegree=-2,processed=0,maxIntermediate=-1;uint32_t currentNode=0;uint64_t active=0,wordWork=0,reverseCount=count;int si=int(special.size())-1;
 pos=file.size;
 while(pos>17){int len=11;if(si>=0&&special[si].first==pos){len=special[si].second;si--;}uint64_t p=pos-len;int tag=file.at(p);if(recordLength(tag)!=len)throw std::runtime_error("reverse record alignment");
  if(tag=='F'){
   int c=file.u16(p+1)-1;uint32_t id=file.u32(p+3);int scale=file.at(p+7);if(c<0||c>=1034||degree[c]!=-2||initial[c]==-2||scale<1||scale>30||component.count(id))throw std::runtime_error("final basis identity");degree[c]=initial[c];node[c]=id;component[id]=c;
  }else if(tag=='R'){
   uint32_t old=file.u32(p+1),saved=file.u32(p+5);int shift=file.at(p+9),a=file.at(p+10);if(currentNode!=2195+reverseCount||currentDegree<-1||a<1||a>30)throw std::runtime_error("reverse arithmetic node");auto it=component.find(saved);if(it==component.end())throw std::runtime_error("saved live node missing");
   if(currentDegree>=0){int c=it->second;degree[c]=std::max(degree[c],currentDegree+shift);maxIntermediate=std::max(maxIntermediate,degree[c]);active++;wordWork+=currentDegree+1;}currentNode=old;reverseCount--;
  }else if(tag=='S'){
   int c=file.u16(p+1)-1;uint32_t afterCurrent=file.u32(p+3),afterSaved=file.u32(p+7);if(currentNode!=afterCurrent||node[c]!=afterSaved||degree[c]<-1)throw std::runtime_error("reverse swap identity");component.erase(afterSaved);std::swap(currentNode,node[c]);std::swap(currentDegree,degree[c]);component[node[c]]=c;
  }else if(tag=='B'){
   int c=file.u16(p+1)-1;uint32_t id=file.u32(p+3);if(currentNode||currentDegree!=-2||node[c]!=id||degree[c]<-1)throw std::runtime_error("reverse store identity");currentNode=id;currentDegree=degree[c];component.erase(id);node[c]=0;degree[c]=-2;
  }else if(tag=='Z'){
   if(currentNode||currentDegree!=-2)throw std::runtime_error("reverse zero identity");currentNode=file.u32(p+1);currentDegree=-1;
  }else if(tag=='I'){
   int index=file.u32(p+1)-1,raw=file.u32(p+5);if(index<0||index>=2195||currentNode!=uint32_t(index+1)||sourceBound[index]!=-2||raw<1||raw>6188)throw std::runtime_error("reverse source identity");sourceBound[index]=currentDegree;sourceRaw[index]=raw;currentNode=0;currentDegree=-2;processed++;
   if(processed%250==0||processed==2195)std::cout<<"{\"phase\":\"reverse-degree-bound\",\"processedSources\":"<<processed<<",\"maximumIntermediateBound\":"<<maxIntermediate<<",\"activeArithmeticRecords\":"<<active<<",\"coefficientWordWorkBound\":"<<wordWork<<",\"elapsedSeconds\":"<<elapsed()<<"}\n"<<std::flush;
  }
  pos=p;
 }
 if(reverseCount||si!=-1||processed!=2195||currentNode||!component.empty())throw std::runtime_error("reverse replay not complete");int maxSource=-1,nonzeroSources=0;uint64_t denseBytes=0;for(int d:sourceBound){if(d<-1)throw std::runtime_error("unprocessed source");if(d>=0){nonzeroSources++;maxSource=std::max(maxSource,d);denseBytes+=uint64_t(d+1)*9;}}
 std::ofstream out(argv[3]);out<<"{\"format\":\"r150-reverse-gb-degree-bound-v1\",\"status\":\"completed-bound-only\",\"field\":31,\"originalSourceCount\":2195,\"reductionRecords\":"<<count<<",\"activeArithmeticRecordUpperBound\":"<<active<<",\"coefficientWordWorkUpperBound\":"<<wordWork<<",\"maximumIntermediateDegreeUpperBound\":"<<maxIntermediate<<",\"maximumOriginalCoefficientDegreeUpperBound\":"<<maxSource<<",\"potentiallyNonzeroSources\":"<<nonzeroSources<<",\"denseNineTargetCoefficientByteUpperBound\":"<<denseBytes<<",\"sourceBounds\":[";
 for(int i=0;i<2195;i++){if(i)out<<",";out<<"["<<i+1<<","<<sourceRaw[i]<<","<<sourceBound[i]<<"]";}out<<"],\"meaning\":\"These are exact bounds for uncancelled reverse row-operation propagation, not the actual polynomial degrees after coefficient cancellation. Only 1034 live slots and one current slot are used; no DAG tree is expanded.\",\"elapsedSeconds\":"<<elapsed()<<"}\n";out.close();if(!out)throw std::runtime_error("bound output failed");
 std::cout<<"{\"status\":\"completed-bound-only\",\"maximumOriginalCoefficientDegreeUpperBound\":"<<maxSource<<",\"maximumIntermediateDegreeUpperBound\":"<<maxIntermediate<<",\"activeArithmeticRecordUpperBound\":"<<active<<",\"coefficientWordWorkUpperBound\":"<<wordWork<<",\"denseNineTargetCoefficientByteUpperBound\":"<<denseBytes<<",\"elapsedSeconds\":"<<elapsed()<<"}\n";
 return 0;
}catch(const std::exception &e){std::cerr<<"REVERSE_GB_BOUND_FAILED "<<e.what()<<"\n";return 1;}}
