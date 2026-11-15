// Full original s=2 field11 Schur through order3, reusing the paid constant DAG.
// Author: Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro.
// No constant Gaussian elimination is performed here.
#ifndef R150_FIRST_NATIVE_SOURCE
#error Compile with R150_FIRST_NATIVE_SOURCE set to the pinned first-native file.
#endif
#define main r150_paid_first_native_main
#include R150_FIRST_NATIVE_SOURCE
#undef main

static constexpr unsigned ORDER=3,NDEP=NR-(NC-NH);
using Flat=vector<uint8_t>;
struct SStep{vector<pair<uint16_t,uint8_t>> ops;uint16_t pivot;uint8_t divisor;};
static string series_read_binding(istream&f){
 string s(64,' ');f.read(s.data(),64);
 need(bool(f)&&s.find_first_not_of("0123456789abcdef")==string::npos,"Series binding");
 return s;
}
static void series_magic(istream&f,const string&s){
 char a[8];f.read(a,8);need(bool(f)&&string(a,8)==s,"Series file magic "+s);
}
static vector<vector<Term>> series_read_rows(istream&f){
 vector<vector<Term>> rows(NR);
 for(unsigned r=0;r<NR;++r){
  unsigned n=rd16(f);need(n<=77,"Original series support");int prev=-1;
  for(unsigned j=0;j<n;++j){
   unsigned c=rd16(f),v=rd8(f);
   need(c<NC&&int(c)>prev&&v>0&&v<11,"Original series ordered term");
   rows[r].push_back({uint16_t(c),uint8_t(v)});prev=int(c);
  }
 }
 return rows;
}
static Flat series_force(unsigned k,const vector<vector<vector<Term>>>&a,
                         const vector<Flat>&l){
 Flat f(NR*NH);
 for(unsigned r=0;r<NR;++r){
  array<uint32_t,NH> v{};
  for(unsigned i=1;i<=k;++i)for(auto t:a[i][r])
   for(unsigned j=0;j<NH;++j)v[j]+=unsigned(t.value)*l[k-i][t.col*NH+j];
  for(unsigned j=0;j<NH;++j)f[r*NH+j]=uint8_t(v[j]%11);
  if((r&255)==0)deadline();
 }
 return f;
}
static pair<Flat,Flat> series_replay(const Flat&f,const vector<SStep>&steps){
 Flat prhs(NC*NH),res(NDEP*NH);unsigned dep=0;
 for(unsigned r=0;r<NR;++r){
  array<uint32_t,NH> v{};for(unsigned j=0;j<NH;++j)v[j]=f[r*NH+j];
  for(auto [c,factor]:steps[r].ops)
   for(unsigned j=0;j<NH;++j)v[j]+=unsigned(factor)*prhs[c*NH+j];
  if(steps[r].pivot!=65535){
   unsigned c=steps[r].pivot,iv=INV[steps[r].divisor];
   for(unsigned j=0;j<NH;++j)prhs[c*NH+j]=uint8_t((v[j]%11)*iv%11);
  }else{
   need(dep<NDEP,"Residual row count");
   for(unsigned j=0;j<NH;++j)res[dep*NH+j]=uint8_t(v[j]%11);
   ++dep;
  }
  if((r&127)==0)deadline();
 }
 need(dep==NDEP,"All original dependent rows in replay");
 return {move(prhs),move(res)};
}
static Flat series_backsub(const Flat&rhs,const vector<unique_ptr<Packed>>&piv){
 Flat x(NC*NH);
 for(int c=int(NC)-1;c>=0;--c)if(piv[c]){
  array<uint32_t,NH> v{};for(unsigned j=0;j<NH;++j)v[j]=rhs[c*NH+j];
  for(unsigned z=unsigned(c)+1;z<NC;++z){
   unsigned f=get(*piv[c],z);
   if(f)for(unsigned j=0;j<NH;++j)v[j]+=f*x[z*NH+j];
  }
  for(unsigned j=0;j<NH;++j)x[c*NH+j]=uint8_t((11-v[j]%11)%11);
  if((c&127)==0)deadline();
 }
 return x;
}
static void series_verify(const Flat&x,const Flat&f,const Flat&s,
                          const vector<vector<Term>>&a0,const vector<SStep>&steps){
 unsigned dep=0;
 for(unsigned r=0;r<NR;++r){
  array<uint32_t,NH> v{};for(unsigned j=0;j<NH;++j)v[j]=f[r*NH+j];
  for(auto t:a0[r])for(unsigned j=0;j<NH;++j)v[j]+=unsigned(t.value)*x[t.col*NH+j];
  if(steps[r].pivot!=65535){
   for(unsigned j=0;j<NH;++j)need(v[j]%11==0,"Original constant-unit row residual");
  }else{
   for(unsigned j=0;j<NH;++j)need(v[j]%11==s[dep*NH+j],"ALL original dependent residual coordinates");
   ++dep;
  }
  if((r&255)==0)deadline();
 }
 need(dep==NDEP,"Full original series verification row count");
}
static void series_save_stage(const fs::path&path,unsigned k,const string&binding,
                              const Flat&x,const Flat&s){
 fs::path tmp=path;tmp+=".tmp";ofstream f(tmp,ios::binary);
 need(bool(f),"Stage output");raw_header(f,"R15SG311",{11,k,NC,NDEP,NH},binding);
 f.write(reinterpret_cast<const char*>(x.data()),streamsize(x.size()));
 f.write(reinterpret_cast<const char*>(s.data()),streamsize(s.size()));
 f.close();need(bool(f),"Stage output completion");fs::rename(tmp,path);
}
static pair<Flat,Flat> series_load_stage(const fs::path&path,unsigned k,const string&binding){
 ifstream f(path,ios::binary);series_magic(f,"R15SG311");
 need(rd32(f)==11&&rd32(f)==k&&rd32(f)==NC&&rd32(f)==NDEP&&rd32(f)==NH,"Stage dimensions");
 need(series_read_binding(f)==binding,"Stage exact binding");
 Flat x(NC*NH),s(NDEP*NH);
 for(auto&v:x){v=rd8(f);need(v<11,"Stage field cochain coordinate");}
 for(auto&v:s){v=rd8(f);need(v<11,"Stage field residual coordinate");}
 need(f.peek()==char_traits<char>::eof(),"Stage trailing bytes");
 return {move(x),move(s)};
}
int main(int argc,char**argv){
 started=Clock::now();
 try{
  need(argc==8,"Usage: series-native coefficient-input old-original-input old-pivots old-DAG old-residual out seconds");
  budget=stod(argv[7]);need(budget>0&&budget<=3600,"Series positive budget");
  fs::path out=argv[6];fs::create_directories(out);
  ifstream nf(argv[1],ios::binary);series_magic(nf,"R15SJ311");
  need(rd32(nf)==11&&rd32(nf)==NR&&rd32(nf)==NC&&rd32(nf)==NH&&rd32(nf)==ORDER,"New series dimensions");
  string binding=series_read_binding(nf),parent=series_read_binding(nf);
  vector<vector<vector<Term>>> a;
  for(unsigned k=0;k<=ORDER;++k)a.push_back(series_read_rows(nf));
  need(nf.peek()==char_traits<char>::eof(),"New series trailing bytes");

  ifstream old(argv[2],ios::binary);series_magic(old,"R150FJ11");
  need(rd32(old)==11&&rd32(old)==NR&&rd32(old)==NC&&rd32(old)==NH,"Old original dimensions");
  need(series_read_binding(old)==parent,"Old original binding");
  Flat paid_rhs(NR*NH);
  for(unsigned r=0;r<NR;++r){
   unsigned n=rd16(old);need(n==a[0][r].size(),"Original A0 row support unchanged");
   for(unsigned j=0;j<n;++j){
    unsigned c=rd16(old),v=rd8(old);
    need(c==a[0][r][j].col&&v==a[0][r][j].value,"Every original A0 term unchanged");
   }
   for(unsigned j=0;j<NH;++j){unsigned v=rd8(old);need(v<11,"Paid RHS value");paid_rhs[r*NH+j]=uint8_t(v);}
  }
  Flat lambda(NC*NH);
  for(auto&v:lambda){v=rd8(old);need(v<11,"Original22 constant head coordinate");}
  for(unsigned j=0;j<NH;++j)need(rd16(old)<NC,"Paid free coordinate");
  need(old.peek()==char_traits<char>::eof(),"Old input trailing bytes");

  ifstream pf(argv[3],ios::binary);series_magic(pf,"R15P1F11");
  need(rd32(pf)==11&&rd32(pf)==NC-NH&&rd32(pf)==NC&&rd32(pf)==NH&&rd32(pf)==NW,"Paid pivot dimensions");
  need(series_read_binding(pf)==parent,"Paid pivot binding");
  vector<unique_ptr<Packed>> piv(NC);vector<unsigned> pivot_source(NC,NR);
  int previous=-1;
  for(unsigned i=0;i<NC-NH;++i){
   unsigned c=rd16(pf),r=rd16(pf);need(c<NC&&int(c)>previous&&r<NR,"Paid pivot position");previous=int(c);
   piv[c]=make_unique<Packed>();
   for(auto&w:*piv[c]){w=0;for(unsigned b=0;b<8;++b)w|=uint64_t(rd8(pf))<<(8*b);}
   need(get(*piv[c],c)==1,"Paid pivot normalized");
   for(unsigned z=0;z<c;++z)need(get(*piv[c],z)==0,"Paid echelon prefix");
   for(unsigned z=c;z<TOTAL;++z)need(get(*piv[c],z)<11,"Paid field echelon entries");
   pivot_source[c]=r;
  }
  need(pf.peek()==char_traits<char>::eof(),"Paid pivot trailing bytes");
  vector<unsigned> free;
  for(unsigned c=0;c<NC;++c)if(!piv[c])free.push_back(c);
  need(free.size()==NH,"All22 original free target coordinates");
  vector<vector<uint8_t>> fblock(NH,vector<uint8_t>(NH));
  for(unsigned i=0;i<NH;++i)for(unsigned j=0;j<NH;++j)fblock[i][j]=lambda[free[i]*NH+j];
  need(rref(fblock,NH).size()==NH,"Original22 head normalization on actual unit free coordinates");

  ifstream dg(argv[4],ios::binary);series_magic(dg,"R15DAG11");
  need(rd32(dg)==11&&rd32(dg)==NR&&rd32(dg)==NC&&rd32(dg)==NH,"Paid DAG dimensions");
  need(series_read_binding(dg)==parent,"Paid DAG binding");
  vector<SStep> steps(NR);vector<bool> created(NC);vector<unsigned> dep_rows;
  uint64_t operations=0;unsigned rank=0;
  for(unsigned r=0;r<NR;++r){
   unsigned n=rd32(dg);need(n<=NC,"Paid DAG row length");int prior=-1;
   for(unsigned j=0;j<n;++j){
    unsigned c=rd16(dg),v=rd8(dg);
    need(c<NC&&int(c)>prior&&created[c]&&v>0&&v<11,"Paid ordered source operations");
    steps[r].ops.emplace_back(uint16_t(c),uint8_t(v));prior=int(c);
   }
   operations+=n;steps[r].pivot=rd16(dg);steps[r].divisor=rd8(dg);
   unsigned c=steps[r].pivot;
   if(c==65535){need(steps[r].divisor==0,"Dependent DAG normalization");dep_rows.push_back(r);}
   else{
    need(c<NC&&int(c)>prior&&!created[c]&&piv[c]&&pivot_source[c]==r
         &&steps[r].divisor>0&&steps[r].divisor<11,"Actual source unit DAG normalization");
    created[c]=true;++rank;
   }
  }
  need(dg.peek()==char_traits<char>::eof()&&rank==NC-NH&&dep_rows.size()==NDEP,"Complete constant DAG retained");

  ifstream rf(argv[5],ios::binary);series_magic(rf,"R15R1F11");
  need(rd32(rf)==11&&rd32(rf)==NDEP&&rd32(rf)==NH,"Paid full first residual dimensions");
  need(series_read_binding(rf)==parent,"Paid full first residual binding");
  Flat paid_s1(NDEP*NH);
  for(unsigned i=0;i<NDEP;++i){
   need(rd16(rf)==dep_rows[i],"Paid dependent original source order");
   for(unsigned j=0;j<NH;++j){unsigned v=rd8(rf);need(v<11,"Paid first residual");paid_s1[i*NH+j]=uint8_t(v);}
  }
  need(rf.peek()==char_traits<char>::eof(),"Paid first residual trailing bytes");

  Flat zeros(NR*NH),s0(NDEP*NH);
  series_verify(lambda,zeros,s0,a[0],steps);
  vector<Flat> l{lambda},s{s0};vector<bool> reused;
  for(unsigned k=1;k<=ORDER;++k){
   Flat forcing=series_force(k,a,l);
   if(k==1)need(forcing==paid_rhs,"All136136 actual A1^T Lambda coordinates match the paid first input");
   fs::path stage=out/("original-unit-graph-order"+to_string(k)+"-"+binding+".bin");
   Flat x,sk;bool old_stage=fs::exists(stage);
   if(old_stage){
    auto v=series_load_stage(stage,k,binding);x=move(v.first);sk=move(v.second);
    series_verify(x,forcing,sk,a[0],steps);
   }else{
    auto v=series_replay(forcing,steps);
    if(k==1)for(unsigned c=0;c<NC;++c)if(piv[c])for(unsigned j=0;j<NH;++j)
      need(v.first[c*NH+j]==get(*piv[c],NC+j),"Actual first pivot RHS matches all paid normalized rows");
    x=series_backsub(v.first,piv);sk=move(v.second);
    series_verify(x,forcing,sk,a[0],steps);
    series_save_stage(stage,k,binding,x,sk);
   }
   for(unsigned c:free)for(unsigned j=0;j<NH;++j)need(x[c*NH+j]==0,"Same zero-free-coordinate unit section");
   if(k==1)need(sk==paid_s1,"All40546 first Schur entries equal the paid residual");
   l.push_back(move(x));s.push_back(move(sk));reused.push_back(old_stage);
   cerr<<"{\"phase\":\"original-series-unit-graph\",\"verifiedOrder\":"<<k
       <<",\"allOriginalResidualCoordinates\":"<<NR*NH<<",\"seconds\":"<<elapsed()<<"}\n";
   deadline();
  }
  ofstream sf(out/"complete-original-schur-through-three.bin",ios::binary);
  raw_header(sf,"R15SC311",{11,NDEP,NH,ORDER},binding);
  for(unsigned r:dep_rows)wr16(sf,r);
  for(auto&v:s)sf.write(reinterpret_cast<const char*>(v.data()),streamsize(v.size()));
  sf.close();need(bool(sf),"Complete Schur output");
  ofstream lf(out/"complete-original-unit-graph-through-three.bin",ios::binary);
  raw_header(lf,"R15LC311",{11,NC,NH,ORDER},binding);
  for(auto&v:l)lf.write(reinterpret_cast<const char*>(v.data()),streamsize(v.size()));
  lf.close();need(bool(lf),"Complete unit-graph output");
  ofstream outrec(out/"native-original-schur-through-three-receipt.json");
  outrec<<setprecision(17)
   <<"{\"format\":\"r150-original-full-field11-schur-through-three-v1\",\"status\":\"completed\","
   <<"\"binding\":\""<<binding<<"\",\"parentBinding\":\""<<parent
   <<"\",\"prime\":11,\"constantRank\":4345,\"originalSources\":6188,\"targets\":4367,"
   <<"\"originalHeadColumns\":22,\"remainingOriginalSourceRows\":1843,\"throughOrder\":3,"
   <<"\"constantDAGRowOperations\":"<<operations
   <<",\"constantGaussianEliminationRepeated\":false,"
   <<"\"allOriginalA0TermsEqualPaidInput\":true,\"allActualA1LambdaEntriesEqualPaidInput\":true,"
   <<"\"allFirstSchurEntriesEqualPaidResidual\":true,\"allOriginalConstantProductsVerified\":true,"
   <<"\"allOriginalResidualIdentitiesVerified\":true,\"unitSourceResidualsAllZero\":true,"
   <<"\"originalResidualCoordinatesVerified\":"<<(ORDER+1)*NR*NH
   <<",\"unitGraphNotClaimedToBe22KernelJets\":true,\"zeroFreeSectionFixed\":true,"
   <<"\"temporaryOnly\":true,\"stages\":[";
  for(unsigned k=1;k<=ORDER;++k){
   if(k>1)outrec<<",";
   outrec<<"{\"order\":"<<k<<",\"verified\":true,\"reused\":"<<(reused[k-1]?"true":"false")<<"}";
  }
  outrec<<"],\"mathSeconds\":"<<elapsed()<<"}\n";outrec.close();need(bool(outrec),"Native series receipt");
  ifstream done(out/"native-original-schur-through-three-receipt.json");cout<<done.rdbuf();return 0;
 }catch(const exception&e){
  cerr<<"native-original-series-error: "<<e.what()<<"\n";
  return string(e.what())=="budget-exhausted"?124:1;
 }
}
