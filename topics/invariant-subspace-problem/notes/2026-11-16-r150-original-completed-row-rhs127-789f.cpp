// Read-only right-hand sides in a complete original, source-certified F127 row state.
// Author: Astra-ISP-789f / literature_audit, with /root. AI-assisted GPT-6 Astra Pro.
// The included producer is frozen and unchanged. Its main is never invoked.
#define main frozen_complete_parameter_seed_main
#include "2026-11-16-r150-original-parameter-seed-compression-rank127-789f.cpp"
#undef main
struct RhsBudget {};
int main(int argc,char**argv){
 auto started=Clock::now();
 try{
  need(argc==6,"original input, completed state, literal RHS input, new out, seconds");
  fs::path ip=argv[1],sp=argv[2],tp=argv[3],out=argv[4];double seconds=std::stod(argv[5]);
  need(seconds>0&&seconds<=300,"bounded read-only RHS consumption");fs::create_directories(out);
  auto tick=[&](){if(std::chrono::duration<double>(Clock::now()-started).count()>seconds)throw RhsBudget();};
  BitOps ops;uint64_t bitchecks=ops.verify(),tinychecks=tiny(ops);
  std::ifstream f(ip,std::ios::binary);magic(f,"R15PCI01");need(read_le(f,4)==1,"original input version");
  State s;s.no=read_le(f,4);s.ni=read_le(f,4);s.first=read_le(f,4);need(read_le(f,4)==127,"same exact field");s.binding=fixed(f,64);
  need(s.no>0&&s.no<=20000&&s.ni>0&&s.ni<=2000&&s.first<=s.ni,"whole original dimensions");
  need(fs::file_size(ip)==92ull+uint64_t(s.no)*s.ni,"complete original input length");
  s.nw=(s.no+s.ni+31)/32;s.at.assign(s.no,-1);load_state(sp,s,ops);
  need(s.next==s.ni,"never consume an incomplete original state");tick();
  std::ifstream t(tp,std::ios::binary);magic(t,"R15RHI01");
  need(read_le(t,4)==1&&read_le(t,4)==s.no&&read_le(t,4)==s.ni,"same original RHS dimensions");
  uint32_t nt=read_le(t,4);need(nt>0&&nt<=16&&read_le(t,4)==127,"literal bounded RHS count and field");
  need(read_le(t,4)==s.basis.size(),"same actual full original rank");
  need(fixed(t,64)==s.binding,"same completed parent binding");std::string binding=fixed(t,64);
  need(binding.find_first_not_of("0123456789abcdef")==std::string::npos,"complete child SHA256 binding");
  need(fs::file_size(tp)==160ull+uint64_t(nt)*s.no,"entire literal RHS input");
  std::vector<std::vector<uint8_t>> targets(nt),residual(nt),coeff(nt);
  std::vector<uint32_t> nonzero(nt,0);uint64_t cancellations=0;
  for(uint32_t k=0;k<nt;k++){
   tick();std::string z=fixed(t,s.no);targets[k].assign(z.begin(),z.end());Row r(7*s.nw,0);
   for(uint32_t j=0;j<s.no;j++){need(targets[k][j]<127,"canonical complete RHS");if(targets[k][j])BitOps::set(r,s.nw,j,targets[k][j]);}
   for(uint32_t p=0;p<s.no;p++){
    int v=BitOps::get(r,s.nw,p),bi=s.at[p];if(!v||bi<0)continue;
    const auto a=ops.rep[127-v];const Basis&b=s.basis[bi];
    BitOps::add(r,s.nw,p/32,b.row[a.c],s.nw,p/32,s.nw-p/32,a.rot,a.neg);
    need(BitOps::get(r,s.nw,p)==0,"whole original unit cancellation");cancellations++;
   }
   residual[k].resize(s.no);coeff[k].resize(s.ni);
   for(uint32_t j=0;j<s.no;j++){int v=BitOps::get(r,s.nw,j);need(v<127,"canonical complete residual");residual[k][j]=v;nonzero[k]+=v!=0;if(s.at[j]>=0)need(v==0,"every original pivot residual zero");}
   for(uint32_t i=0;i<s.ni;i++){int v=BitOps::get(r,s.nw,s.no+i);need(v<127,"canonical full source recipe");coeff[k][i]=v?127-v:0;}
  }
  need(t.peek()==EOF,"RHS exact EOF");
  // Check every output coordinate against the literal original input, not
  // merely against the normalized checkpoint rows. Bound: 2000*126^2<2^25.
  need(uint64_t(s.ni)*126*126<UINT32_MAX,"whole unmodded dot-product bound");
  std::vector<std::vector<uint32_t>> sums(nt,std::vector<uint32_t>(s.no,0));
  std::vector<uint8_t> a(s.no);
  for(uint32_t i=0;i<s.ni;i++){
   tick();f.read(reinterpret_cast<char*>(a.data()),s.no);need(uint32_t(f.gcount())==s.no,"whole original source row");
   for(uint32_t j=0;j<s.no;j++)need(a[j]<127,"all original scalar coefficients canonical");
   for(uint32_t k=0;k<nt;k++)if(coeff[k][i])for(uint32_t j=0;j<s.no;j++)sums[k][j]+=uint32_t(coeff[k][i])*a[j];
  }
  need(f.peek()==EOF,"original input exact EOF");
  for(uint32_t k=0;k<nt;k++)for(uint32_t j=0;j<s.no;j++)need((sums[k][j]+residual[k][j])%127==targets[k][j],"all original target=source+residual products");
  auto op=out/"complete-original-rhs-result.bin",tmp=out/"complete-original-rhs-result.bin.tmp";
  std::ofstream of(tmp,std::ios::binary);of.write("R15RHO01",8);u32(of,1);u32(of,s.no);u32(of,s.ni);u32(of,nt);u32(of,127);u32(of,s.basis.size());
  of.write(s.binding.data(),64);of.write(binding.data(),64);
  for(uint32_t k=0;k<nt;k++){u32(of,nonzero[k]);of.write(reinterpret_cast<const char*>(residual[k].data()),s.no);of.write(reinterpret_cast<const char*>(coeff[k].data()),s.ni);}
  finish(of,tmp,op);
  std::ostringstream q;q<<"{\"format\":\"r150-completed-original-row-rhs127-native-v1\",\"binding\":\""<<binding
   <<"\",\"parentBinding\":\""<<s.binding<<"\",\"status\":\"completed\",\"originalInputRows\":"<<s.ni
   <<",\"allOutputCoordinates\":"<<s.no<<",\"actualParentRank\":"<<s.basis.size()<<",\"rightHandSides\":"<<nt
   <<",\"allOriginalScalarProducts\":"<<uint64_t(nt)*s.no<<",\"unitCancellations\":"<<cancellations
   <<",\"exhaustiveBitplaneChecks\":"<<bitchecks<<",\"independentTinyProducts\":"<<tinychecks
   <<",\"parentMutated\":false,\"newGaussianEliminationPerformed\":false,\"elapsedSeconds\":"<<std::chrono::duration<double>(Clock::now()-started).count()<<",\"residualNonzeroCounts\":[";
  for(uint32_t k=0;k<nt;k++){if(k)q<<",";q<<nonzero[k];}q<<"]}";
  auto rp=out/"complete-original-rhs-native-receipt.json",rt=out/"complete-original-rhs-native-receipt.json.tmp";std::ofstream rf(rt);rf<<q.str();finish(rf,rt,rp);std::cout<<q.str()<<std::endl;return 0;
 }catch(const RhsBudget&){std::cerr<<"bounded read-only RHS budget; no incomplete result adopted"<<std::endl;return 75;}
 catch(const std::exception&e){std::cerr<<e.what()<<std::endl;return 1;}
}
