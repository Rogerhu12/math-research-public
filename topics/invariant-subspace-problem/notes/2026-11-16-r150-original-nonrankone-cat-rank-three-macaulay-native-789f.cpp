// Original non-rank-one Cat-rank-three Macaulay rank, fixed F_127.
// Author: Astra-ISP-789f / normal_annihilator.
// AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
// All 17 exact equations and every ordinary multiplier of degree <=3 are
// reconstructed from the original rational model, INCLUDING all constants.
// Targets have degrees 0 through 5. No old NF source subset is used.
// A proper-prefix rank is not a completed-rank result. Atomic whole-row
// checkpoints retain the complete normalized echelon basis. If rank is not
// full, a complete free-I right kernel is recovered and multiplied back against
// ALL 6188 original rows before it is called a complete field cokernel.

#include "2026-11-15-r150-original-f127-bitplane-789f.hpp"
#include <chrono>
#include <cctype>
#include <csignal>
#include <filesystem>
#include <iostream>
#include <memory>
#include <numeric>
#include <set>
#include <sstream>
#include <unordered_map>
using namespace std;
namespace fs = std::filesystem;
using Clock = chrono::steady_clock;
static constexpr int P=127, NV=11, NE=17, NS=6188, NT=4368;
static constexpr int NW=(NT+31)/32, WORDS=7*NW;
static volatile sig_atomic_t stop_requested=0;
static void stop_handler(int){stop_requested=1;}
static void need(bool ok,const string&s){if(!ok)throw runtime_error(s);}
static string escaped(const string&s){
 string o;for(unsigned char c:s){
  if(c=='"'||c=='\\'){o+='\\';o+=char(c);}
  else if(c=='\n')o+="\\n";
  else if(c=='\r')o+="\\r";
  else if(c=='\t')o+="\\t";
  else if(c>=32)o+=char(c);
 }return o;
}
static void write_text(const fs::path&p,const string&s){
 fs::path q=p;q+=".tmp";ofstream o(q,ios::binary);
 need(bool(o),"open text temporary");o.write(s.data(),s.size());o.close();
 need(bool(o),"complete text write");fs::rename(q,p);
}
static void monomials_rec(int remain,int first,uint64_t code,vector<uint64_t>&v){
 if(!remain){v.push_back(code);return;}
 for(int j=first;j<NV;j++)monomials_rec(remain-1,j,code+(uint64_t(1)<<(3*j)),v);
}
static vector<uint64_t> monomials(int lo,int hi){
 vector<uint64_t> v;
 for(int d=lo;d<=hi;d++)monomials_rec(d,0,0,v);
 return v;
}
struct Term{uint64_t code;uint8_t value;};
struct Model{
 vector<vector<Term>> eq;
 vector<uint64_t> multipliers,targets,quadratics;
 unordered_map<uint64_t,int> index;
 uint64_t inputOriginalCoefficientCount=0;
 explicit Model(const fs::path&path){
  multipliers=monomials(0,3);targets=monomials(0,5);quadratics=monomials(0,2);
  need(multipliers.size()==364&&targets.size()==NT&&quadratics.size()==78,
       "complete ordinary monomial counts");
  for(int j=0;j<NT;j++)need(index.emplace(targets[j],j).second,
                            "unique original output monomial");
  ifstream f(path,ios::binary);need(bool(f),"open original equation input");
  char magic[8];f.read(magic,8);
  need(f.gcount()==8&&string(magic,8)=="R15N3M01","original input magic");
  const vector<uint32_t> expected={1,P,NV,NE,3,5,NS,NT,78};
  for(uint32_t x:expected)need(read_le(f,4)==x,"original input dimensions");
  eq.resize(NE);
  for(int i=0;i<NE;i++){
   need(read_le(f,4)==uint64_t(i),"all seventeen original equation labels");
   need(read_le(f,4)==78,"all seventy-eight original coefficient positions");
   for(int j=0;j<78;j++){
    uint64_t key=read_le(f,8),value=read_le(f,1);
    need(key==quadratics[j]&&value<P,"whole original coefficient dictionary");
    eq[i].push_back({key,uint8_t(value)});inputOriginalCoefficientCount++;
   }
  }
  need(f.peek()==EOF,"original input exact EOF");
 }
 vector<pair<int,int>> sparse_row(int row)const{
  need(row>=0&&row<NS,"original source index");
  int multiplier=row/NE,equation=row%NE;
  vector<pair<int,int>> ans;ans.reserve(78);
  for(const auto&t:eq[equation])if(t.value){
   auto it=index.find(multipliers[multiplier]+t.code);
   need(it!=index.end(),"every original product retained through degree five");
   ans.push_back({it->second,int(t.value)});
  }
  return ans;
 }
};
static int leading(const Row&r,int firstWord=0){
 for(int w=firstWord;w<NW;w++){
  uint32_t v=0;for(int b=0;b<7;b++)v|=r[b*NW+w];
  if(v){int j=32*w+__builtin_ctz(v);need(j<NT,"zero unused output padding");return j;}
 }
 return -1;
}
static int small_linear_rank(const Model&m,const BitOps&ops){
 int A[NE][NV]={};
 for(int i=0;i<NE;i++)for(int j=0;j<NV;j++)A[i][j]=m.eq[i][j+1].value;
 int r=0;
 for(int j=0;j<NV;j++){
  int v=r;while(v<NE&&!A[v][j])v++;
  if(v==NE)continue;
  for(int k=0;k<NV;k++)swap(A[r][k],A[v][k]);
  int u=ops.inv[A[r][j]];
  for(int k=j;k<NV;k++)A[r][k]=A[r][k]*u%P;
  for(int i=r+1;i<NE;i++)if(A[i][j]){
   int x=A[i][j];
   for(int k=j;k<NV;k++)A[i][k]=(A[i][k]+P-x*A[r][k]%P)%P;
  }
  r++;
 }
 return r;
}
struct State{
 uint64_t generation=0,reductions=0,rowsConstructed=0;
 int phase=0,cursor=0,rank=0,backCursor=NT-1,verifyCursor=0;
 vector<unique_ptr<Triple>> basis;
 vector<int> pivotSource,pivotValue;
 vector<int> freeColumns;
 vector<uint8_t> kernel;
 State():basis(NT),pivotSource(NT,-1),pivotValue(NT,0){}
};
static void validate_basis(const State&s){
 need(0<=s.phase&&s.phase<=3&&0<=s.cursor&&s.cursor<=NS,"state phase and cursor");
 need(0<=s.rank&&s.rank<=NT,"state rank");
 set<int> sources;int found=0;
 for(int j=0;j<NT;j++)if(s.basis[j]){
  found++;
  need(leading((*s.basis[j])[0])==j&&BitOps::get((*s.basis[j])[0],NW,j)==1,
       "every stored basis row has its true monic leading position");
  need(0<=s.pivotSource[j]&&s.pivotSource[j]<s.cursor
       &&sources.insert(s.pivotSource[j]).second
       &&0<s.pivotValue[j]&&s.pivotValue[j]<P,"true distinct original pivot sources");
 }
 need(found==s.rank,"complete stored rank profile");
 if(s.phase){
  need(s.cursor==NS,"kernel phases require all original source rows");
  vector<int> free;
  for(int j=0;j<NT;j++)if(!s.basis[j])free.push_back(j);
  need(free==s.freeColumns,"complete original free columns");
  uint64_t k=free.size();
  need(s.kernel.size()==uint64_t(NT)*k,"complete kernel shape");
  for(size_t i=0;i<k;i++)for(size_t j=0;j<k;j++)
   need(s.kernel[uint64_t(free[i])*k+j]==uint8_t(i==j),"stored exact free identity");
  need(-1<=s.backCursor&&s.backCursor<NT
       &&0<=s.verifyCursor&&s.verifyCursor<=NS,"whole kernel progress cursors");
 }
}
static void save_state(State&s,const fs::path&out,const string&binding){
 s.generation++;
 int slot=int(s.generation%2);
 fs::path path=out/("state-slot-"+to_string(slot)+".bin"),temp=path;temp+=".tmp";
 ofstream o(temp,ios::binary);need(bool(o),"open atomic native checkpoint");
 o.write("R15N3C01",8);u32(o,1);u32(o,P);u32(o,NS);u32(o,NT);u32(o,NW);
 o.write(binding.data(),64);u64(o,s.generation);
 u32(o,s.phase);u32(o,s.cursor);u32(o,s.rank);u32(o,uint32_t(s.backCursor+1));
 u32(o,s.verifyCursor);u64(o,s.reductions);u64(o,s.rowsConstructed);
 for(int j=0;j<NT;j++){
  o.put(s.basis[j]?1:0);
  if(s.basis[j]){
   u32(o,s.pivotSource[j]);u32(o,s.pivotValue[j]);
   for(uint32_t x:(*s.basis[j])[0])u32(o,x);
  }
 }
 u32(o,s.freeColumns.size());for(int j:s.freeColumns)u32(o,j);
 u64(o,s.kernel.size());
 if(!s.kernel.empty())o.write(reinterpret_cast<const char*>(s.kernel.data()),s.kernel.size());
 o.write("R15N3CEND",9);o.flush();need(bool(o),"all native checkpoint bytes flushed");
 o.close();need(bool(o),"whole native checkpoint close");fs::rename(temp,path);
 write_text(out/"checkpoint-index.txt","R150_NONRANKONE_CAT3_INDEX1\n"+
            to_string(s.generation)+" "+to_string(slot)+"\n");
}
static bool load_state(State&s,const fs::path&out,const string&binding,const BitOps&ops){
 fs::path index=out/"checkpoint-index.txt";if(!fs::exists(index))return false;
 ifstream ix(index);string magic;uint64_t gen;int slot;
 need(bool(ix>>magic>>gen>>slot)&&magic=="R150_NONRANKONE_CAT3_INDEX1"
      &&slot==int(gen%2)&&gen>0,"atomic checkpoint index");
 string extra;need(!(ix>>extra),"checkpoint index exact EOF");
 ifstream f(out/("state-slot-"+to_string(slot)+".bin"),ios::binary);
 need(bool(f),"active native checkpoint");
 char b[64];f.read(b,8);need(f.gcount()==8&&string(b,8)=="R15N3C01","checkpoint magic");
 for(uint32_t x:vector<uint32_t>{1,P,NS,NT,NW})need(read_le(f,4)==x,"checkpoint dimensions");
 f.read(b,64);need(f.gcount()==64&&string(b,64)==binding,"same complete mathematical binding");
 s.generation=read_le(f,8);need(s.generation==gen,"checkpoint generation");
 s.phase=read_le(f,4);s.cursor=read_le(f,4);s.rank=read_le(f,4);
 s.backCursor=int(read_le(f,4))-1;s.verifyCursor=read_le(f,4);
 s.reductions=read_le(f,8);s.rowsConstructed=read_le(f,8);
 for(int j=0;j<NT;j++){
  int present=read_le(f,1);need(present<=1,"basis presence bit");
  if(present){
   s.pivotSource[j]=read_le(f,4);s.pivotValue[j]=read_le(f,4);
   auto t=make_unique<Triple>();(*t)[0].resize(WORDS);
   for(auto &x:(*t)[0])x=read_le(f,4);
   BitOps::refresh(*t,NW,j/32);s.basis[j]=move(t);
  }
 }
 uint64_t k=read_le(f,4);need(k<=NT,"complete free count");s.freeColumns.resize(k);
 for(int &j:s.freeColumns)j=read_le(f,4);
 uint64_t n=read_le(f,8);need(n<=uint64_t(NT)*NT,"bounded complete kernel bytes");
 s.kernel.resize(n);if(n)f.read(reinterpret_cast<char*>(s.kernel.data()),n);
 need(!n||uint64_t(f.gcount())==n,"complete stored kernel bytes");
 f.read(b,9);need(f.gcount()==9&&string(b,9)=="R15N3CEND","checkpoint exact end marker");
 need(f.peek()==EOF,"checkpoint exact EOF");validate_basis(s);
 return true;
}
static int profile_det(const State&s){
 vector<pair<int,int>> selected;
 int det=1;
 for(int j=0;j<NT;j++)if(s.basis[j]){
  selected.push_back({s.pivotSource[j],j});
  det=det*s.pivotValue[j]%P;
 }
 sort(selected.begin(),selected.end());
 int parity=0;
 for(size_t i=0;i<selected.size();i++)for(size_t j=i+1;j<selected.size();j++)
  parity^=int(selected[i].second>selected[j].second);
 return parity?(P-det)%P:det;
}
static void write_profile(const State&s,const Model&m,const fs::path&out,const string&binding){
 vector<pair<int,int>> selected;
 for(int j=0;j<NT;j++)if(s.basis[j])selected.push_back({s.pivotSource[j],j});
 sort(selected.begin(),selected.end());
 ostringstream o;
 o<<"{\"format\":\"r150-original-nonrankone-cat3-complete-field-profile-v1\","
  <<"\"binding\":\""<<binding<<"\",\"prime\":127,\"sourceRows\":6188,\"targetColumns\":4368,"
  <<"\"rank\":"<<s.rank<<",\"originalSourceRows\":[";
 for(size_t i=0;i<selected.size();i++){if(i)o<<',';o<<selected[i].first;}
 o<<"],\"leadingOriginalOutputColumns\":[";
 for(size_t i=0;i<selected.size();i++){if(i)o<<',';o<<selected[i].second;}
 o<<"],\"sortedOriginalMinorDeterminant\":"<<profile_det(s)<<",\"freeOriginalColumns\":[";
 for(size_t i=0;i<s.freeColumns.size();i++){if(i)o<<',';o<<s.freeColumns[i];}
 o<<"],\"freeOriginalMonomialCodes\":[";
 for(size_t i=0;i<s.freeColumns.size();i++){if(i)o<<',';o<<m.targets[s.freeColumns[i]];}
 o<<"]}\n";write_text(out/"complete-original-field-profile.json",o.str());
}
static void write_kernel(const State&s,const fs::path&out,const string&binding){
 fs::path p=out/"complete-original-field-kernel.bin",q=p;q+=".tmp";
 ofstream o(q,ios::binary);need(bool(o),"kernel output");
 o.write("R15N3K01",8);u32(o,1);u32(o,P);u32(o,NT);u32(o,s.freeColumns.size());
 o.write(binding.data(),64);
 for(int j:s.freeColumns)u32(o,j);
 if(!s.kernel.empty())o.write(reinterpret_cast<const char*>(s.kernel.data()),s.kernel.size());
 o.close();need(bool(o),"complete field kernel output");fs::rename(q,p);
}
int main(int argc,char**argv){
 Clock::time_point begin=Clock::now(),lastSave=begin;
 State state;bool resumed=false;uint64_t arithmetic=0;int linearRank=-1;
 string binding,outcome="failed",error;int exitCode=1;
 fs::path out;
 try{
  need(argc==5,"usage: native INPUT OUT SECONDS BINDING");
  out=argv[2];fs::create_directories(out);
  double seconds=stod(argv[3]);
  binding=argv[4];
  need(seconds>=5&&seconds<=1800&&binding.size()==64
       &&all_of(binding.begin(),binding.end(),[](char c){return isxdigit(c);}),
       "bounded native budget and complete binding");
  signal(SIGTERM,stop_handler);signal(SIGINT,stop_handler);
  Model model(argv[1]);BitOps ops;arithmetic=ops.verify();
  linearRank=small_linear_rank(model,ops);
  need(0<=linearRank&&linearRank<=NV,"actual linear rank recorded without a prescribed value");
  resumed=load_state(state,out,binding,ops);
  auto now_seconds=[&](){return chrono::duration<double>(Clock::now()-begin).count();};
  auto boundary=[&](){
   if(stop_requested||now_seconds()>=seconds-2){
    save_state(state,out,binding);outcome="budget-checkpoint";exitCode=75;return false;
   }
   if(chrono::duration<double>(Clock::now()-lastSave).count()>=12){
    save_state(state,out,binding);lastSave=Clock::now();
   }
   return true;
  };
  bool proceed=true;
  while(state.phase==0&&state.cursor<NS){
   if(!boundary()){proceed=false;break;}
   Row r(WORDS,0);
   for(auto [j,v]:model.sparse_row(state.cursor))BitOps::set(r,NW,j,v);
   state.rowsConstructed++;
   int p=leading(r);
   while(p>=0){
    int value=BitOps::get(r,NW,p);
    need(value>0&&value<P,"true original leading coefficient");
    if(!state.basis[p]){
     ops.multiple(r,NW,p/32,ops.inv[value]);
     need(BitOps::get(r,NW,p)==1&&leading(r)==p,"new original monic pivot");
     auto t=make_unique<Triple>();(*t)[0]=move(r);
     BitOps::refresh(*t,NW,p/32);
     state.basis[p]=move(t);state.pivotSource[p]=state.cursor;
     state.pivotValue[p]=value;state.rank++;
     break;
    }
    const auto rep=ops.rep[P-value];
    BitOps::add(r,NW,p/32,(*state.basis[p])[rep.c],NW,p/32,NW-p/32,rep.rot,rep.neg);
    state.reductions++;
    int next=leading(r,p/32);
    need(next<0||next>p,"strict original leading reduction and complete tail");
    p=next;
   }
   state.cursor++;
  }
  if(proceed&&state.phase==0){
   need(state.cursor==NS&&state.rowsConstructed==NS,"all 6188 original source rows constructed");
   for(int j=0;j<NT;j++)if(!state.basis[j])state.freeColumns.push_back(j);
   int k=state.freeColumns.size();
   state.kernel.assign(uint64_t(NT)*k,0);
   for(int i=0;i<k;i++)state.kernel[uint64_t(state.freeColumns[i])*k+i]=1;
   state.backCursor=NT-1;state.verifyCursor=0;state.phase=1;
   save_state(state,out,binding);lastSave=Clock::now();
  }
  while(proceed&&state.phase==1&&state.backCursor>=0){
   if(!boundary()){proceed=false;break;}
   int p=state.backCursor,k=state.freeColumns.size();
   if(state.basis[p]&&k){
    vector<uint32_t> acc(k,0);
    for(int j=p+1;j<NT;j++){
     int value=BitOps::get((*state.basis[p])[0],NW,j);
     if(value){
      uint32_t factor=P-value;uint64_t start=uint64_t(j)*k;
      for(int a=0;a<k;a++)acc[a]+=factor*state.kernel[start+a];
     }
    }
    // At most 4368*126^2 < 2^32 in each exact accumulator.
    for(int a=0;a<k;a++)state.kernel[uint64_t(p)*k+a]=acc[a]%P;
   }
   state.backCursor--;
  }
  if(proceed&&state.phase==1){
   need(state.backCursor==-1,"all original pivot rows back-substituted");
   state.phase=2;save_state(state,out,binding);lastSave=Clock::now();
  }
  while(proceed&&state.phase==2&&state.verifyCursor<NS){
   if(!boundary()){proceed=false;break;}
   int k=state.freeColumns.size();
   vector<uint32_t> acc(k,0);
   for(auto [j,v]:model.sparse_row(state.verifyCursor)){
    uint64_t start=uint64_t(j)*k;
    for(int a=0;a<k;a++)acc[a]+=uint32_t(v)*state.kernel[start+a];
   }
   for(int a=0;a<k;a++)need(acc[a]%P==0,"all original 6188 field kernel products");
   state.verifyCursor++;
  }
  if(proceed&&state.phase==2){
   need(state.verifyCursor==NS,"all original source kernel products completed");
   state.phase=3;validate_basis(state);
   write_profile(state,model,out,binding);write_kernel(state,out,binding);
   save_state(state,out,binding);outcome="completed";exitCode=0;
  }else if(proceed&&state.phase==3){
   validate_basis(state);
   need(state.verifyCursor==NS,"completed checkpoint retains full source verification");
   write_profile(state,model,out,binding);write_kernel(state,out,binding);
   outcome="completed";exitCode=0;
  }
 }catch(const exception&e){error=e.what();outcome="failed";exitCode=1;}
 catch(...){error="unknown native exception";outcome="failed";exitCode=1;}
 double elapsed=chrono::duration<double>(Clock::now()-begin).count();
 if(!out.empty()){
  ostringstream r;
  int k=state.freeColumns.size();
  r<<"{\"format\":\"r150-original-nonrankone-cat3-macaulay-field-native-v1\","
   <<"\"status\":\""<<outcome<<"\",\"binding\":\""<<escaped(binding)<<"\","
   <<"\"parameters\":{\"prime\":127,\"originalEquationCount\":17,"
   <<"\"originalSourceCount\":6188,\"originalOutputCount\":4368,"
   <<"\"originalLinearFieldRank\":"<<linearRank<<",\"rank\":"<<state.rank
   <<",\"sourceRowsCompleted\":"<<state.cursor
   <<",\"allOriginalSourceRowsProcessed\":"<<(state.cursor==NS?"true":"false")
   <<",\"completeRankObtained\":"<<(state.cursor==NS?"true":"false")
   <<",\"fullOriginalRowRank\":"<<((state.cursor==NS&&state.rank==NT)?"true":"false")
   <<",\"fieldCokernelDimension\":"<<(state.cursor==NS?NT-state.rank:-1)
   <<",\"allOriginalSourceKernelProductsVerified\":"<<(state.phase==3?"true":"false")
   <<",\"originalKernelProductCoordinates\":"<<(state.phase==3?uint64_t(NS)*k:0)
   <<",\"freeIdentityCoordinates\":"<<(state.phase==3?uint64_t(k)*k:0)
   <<",\"normalizedBasisCount\":"<<state.rank
   <<",\"fieldReductions\":"<<state.reductions
   <<",\"bitPlaneArithmeticChecks\":"<<arithmetic
   <<",\"checkpointGeneration\":"<<state.generation
   <<",\"checkpointPhase\":"<<state.phase
   <<",\"backSubstitutionNextOriginalRow\":"<<state.backCursor
   <<",\"originalKernelVerificationRows\":"<<state.verifyCursor
   <<",\"resumed\":"<<(resumed?"true":"false")
   <<",\"sortedOriginalMinorDeterminant\":"<<(state.rank?profile_det(state):1)
   <<",\"elapsedSeconds\":"<<elapsed;
  if(!error.empty())r<<",\"error\":{\"type\":\"native-exception\",\"message\":\""<<escaped(error)<<"\"}";
  r<<"}}\n";
  try{write_text(out/"original-nonrankone-cat3-macaulay-native-receipt.json",r.str());}
  catch(...){cerr<<"unable to write bounded native receipt\n";exitCode=1;}
  cout<<r.str();
 }else cerr<<error<<"\n";
 return exitCode;
}
