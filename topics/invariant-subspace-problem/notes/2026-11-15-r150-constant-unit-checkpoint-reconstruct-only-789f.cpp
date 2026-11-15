// Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
// One reconstruction attempt at an already complete original Dixon checkpoint.
// The included native source is frozen and SHA-pinned by the Python launcher.
// No digit(), inverse(), or write to the original checkpoint directory occurs.
#define main frozen_constant_unit_digit_main
#include "2026-11-15-r150-constant-unit-multiple-rhs-dixon-checkpoint-789f.cpp"
#undef main
static bool same_meta(const Meta&a,const Meta&b){
 return a.slot==b.slot&&a.digits==b.digits&&a.p==b.p&&a.bytes==b.bytes&&a.hash==b.hash;
}
int main(int argc,char**argv){
 if(argc!=9){
  std::cerr<<"usage: reconstruct input.bin original-native-directory new-output-directory binding seconds expected-digits expected-checkpoint-sha expected-input-sha\n";
  return 1;
 }
 std::signal(SIGTERM,sigstop);std::signal(SIGINT,sigstop);
 fs::path oldout=argv[2],out=argv[3];fs::create_directories(out);
 auto start=Clock::now();
 std::string binding=argv[4],inputsha=argv[8],oldhash=argv[7];
 uint32_t expected=0;double budget=0;
 try{
  expected=std::stoul(argv[6]);budget=std::stod(argv[5]);
  need(binding.size()==64&&inputsha.size()==64&&oldhash.size()==64,"complete identity strings");
  need(std::isfinite(budget)&&budget>0&&budget<=7200,"finite reconstruction-only budget");
  need(fs::weakly_canonical(oldout)!=fs::weakly_canonical(out),"separate reconstruction output directory");
  need(fs::exists(oldout/"checkpoint-active.txt"),"existing complete original active manifest is required");
  Meta before=read_meta(oldout/"checkpoint-active.txt",binding);
  need(before.digits==expected&&before.hash==oldhash&&(before.slot==0||before.slot==1),
       "same expected last complete original checkpoint");
  Input input(argv[1],binding);need(input.sha==inputsha,"same complete original native input");
  double consumed=std::chrono::duration<double>(Clock::now()-start).count();
  need(consumed<budget,"original input read exhausted reconstruction budget");
  Solver solver(input,oldout,budget-consumed);
  // restore() needs the recorded prime but no inverse or modular matrix.
  solver.p=before.p;
  solver.restore();
  need(solver.haveState&&solver.digits==expected&&solver.startdigits==expected
       &&solver.checkpointHash==oldhash&&!solver.haveInv,
       "complete source/residual restoration without a new inverse or digit");
  const uint32_t oldattempts=solver.attempts,oldnext=solver.nextrec;
  // All subsequent checkpoint/receipt/solution writes are isolated.
  solver.out=out;
  std::ostringstream restored;
  restored<<"{\"format\":\"isp-constant-unit-reconstruct-restored-v1\",\"binding\":\""<<binding
    <<"\",\"completedDigits\":"<<expected<<",\"originalCheckpointSHA256\":\""<<oldhash
    <<"\",\"originalAttempts\":"<<oldattempts<<",\"originalNextScheduledAttempt\":"<<oldnext
    <<",\"inverseLoaded\":false,\"newDigitsComputed\":0,\"completeOriginalStateVerified\":true}";
  atomic_text(out/"reconstruct-restored-receipt.json",restored.str());
  if(solver.timeup())throw BudgetExpired("time after complete checkpoint restore; no reconstruction started");
  bool ok=solver.reconstruct();
  need(solver.digits==expected&&solver.startdigits==expected&&solver.attempts==oldattempts+1,
       "exactly one current-precision attempt and no new digit");
  need(same_meta(before,read_meta(oldout/"checkpoint-active.txt",binding)),
       "original active checkpoint metadata unchanged");
  std::string native;
  int code=0;
  if(ok)native=solver.receipt("completed","constant-unit-multiple-rhs-rational-solution-complete");
  else if(solver.timeup()){
   native=solver.receipt("budget-exhausted","current-checkpoint-reconstruction-unfinished");code=75;
  }else native=solver.receipt("completed-prefix","current-checkpoint-reconstruction-not-verified");
  std::ostringstream result;
  result<<"{\"format\":\"isp-constant-unit-checkpoint-reconstruct-only-v1\",\"status\":\""
    <<(ok?"completed":code==75?"budget-exhausted":"completed")
    <<"\",\"outcome\":\""<<(ok?"verified-original-unit-solution":code==75?"checkpoint-reconstruction-unfinished":"no-verified-unit-solution-at-this-checkpoint")
    <<"\",\"binding\":\""<<binding<<"\",\"completedDigits\":"<<expected
    <<",\"newDigitsComputed\":0,\"newInverseComputed\":false,\"inverseLoaded\":false"
    <<",\"originalActiveManifestUnchanged\":true,\"exactlyOneAdditionalReconstructionAttempt\":true"
    <<",\"allOriginalUnitRowsVerified\":"<<(ok?"true":"false")
    <<",\"originalUnitProductCoordinates\":"<<(ok?uint64_t(input.n)*input.m:0)
    <<",\"fullOriginal4354VerificationComplete\":false"
    <<",\"nativeElapsedSeconds\":"<<std::setprecision(17)<<std::chrono::duration<double>(Clock::now()-start).count()
    <<",\"parameters\":{\"originalCheckpointSHA256\":\""<<oldhash
    <<"\",\"originalCheckpointBytes\":"<<before.bytes<<",\"originalCheckpointSlot\":"<<before.slot
    <<",\"originalAttempts\":"<<oldattempts<<",\"originalNextScheduledAttempt\":"<<oldnext
    <<",\"inputBytes\":"<<input.bytes<<",\"inputSHA256\":\""<<input.sha
    <<"\",\"solutionBytes\":"<<solver.solutionBytes<<",\"solutionSHA256\":\""<<solver.solutionHash
    <<"\",\"reconstructionCheckpointBytes\":"<<solver.checkpointBytes
    <<",\"reconstructionCheckpointSHA256\":\""<<solver.checkpointHash
    <<"\",\"runtimeFlintVersion\":\""<<esc(flint_version)<<"\",\"headerFlintVersion\":\""<<esc(FLINT_VERSION)
    <<"\"}}";
  atomic_text(out/"constant-unit-reconstruct-only-native-receipt.json",result.str());
  std::cout<<result.str()<<"\n";return code;
 }catch(const BudgetExpired&e){
  std::ostringstream r;
  r<<"{\"format\":\"isp-constant-unit-checkpoint-reconstruct-only-v1\",\"status\":\"budget-exhausted\""
   <<",\"binding\":\""<<esc(binding)<<"\",\"newDigitsComputed\":0,\"newInverseComputed\":false"
   <<",\"allOriginalUnitRowsVerified\":false,\"error\":\""<<esc(e.what())<<"\"}";
  atomic_text(out/"constant-unit-reconstruct-only-native-receipt.json",r.str());
  std::cout<<r.str()<<"\n";return 75;
 }catch(const std::exception&e){
  std::ostringstream r;
  r<<"{\"format\":\"isp-constant-unit-checkpoint-reconstruct-only-v1\",\"status\":\"failed\""
   <<",\"binding\":\""<<esc(binding)<<"\",\"newDigitsComputed\":0,\"newInverseComputed\":false"
   <<",\"allOriginalUnitRowsVerified\":false,\"error\":\""<<esc(e.what())<<"\"}";
  atomic_text(out/"constant-unit-reconstruct-only-native-receipt.json",r.str());
  std::cout<<r.str()<<"\n";return 1;
 }
}
