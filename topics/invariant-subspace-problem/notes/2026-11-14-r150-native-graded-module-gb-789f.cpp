// Streaming univariate module GB over F_31[s], order (dp,c).
// All vector degrees remain <=45. Source transformations never divide by s.
// Reuse the already checked F31 bit-sliced arithmetic, without changing it.
#define main r150_frozen_normal_form_main
#include "2026-11-14-r150-native-normal-form-789f.cpp"
#undef main

struct GBLead {int degree=-1,component=-1,coefficient=0;};
struct GBPivot {std::unique_ptr<Triple> data;int degree=0,coefficient=0;uint32_t node=0;};
static uint32_t gb_u32(std::istream &s){uint32_t v=0;for(int j=0;j<4;j++){int c=s.get();if(c<0)throw std::runtime_error("truncated u32");v|=uint32_t(c)<<(8*j);}return v;}
static uint16_t gb_u16(std::istream &s){uint16_t v=0;for(int j=0;j<2;j++){int c=s.get();if(c<0)throw std::runtime_error("truncated u16");v|=uint16_t(c)<<(8*j);}return v;}
static int gb_byte(std::istream &s){int c=s.get();if(c<0)throw std::runtime_error("truncated byte");return c;}

int main(int argc,char **argv){try{
 if(argc!=6)return 2;
 const int maxSources=std::stoi(argv[4]);const double softSeconds=std::stod(argv[5]);
 if(maxSources<0||softSeconds<=0)throw std::runtime_error("invalid bounds");
 auto start=std::chrono::steady_clock::now();auto seconds=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 std::ifstream in(argv[1],std::ios::binary),headerIn(argv[2]);if(!in||!headerIn)throw std::runtime_error("input open");
 std::string header((std::istreambuf_iterator<char>(headerIn)),std::istreambuf_iterator<char>());
 if(header.rfind("98 ",0)!=0||header.find("\n15 ")==std::string::npos)throw std::runtime_error("runtime SSI header missing");
 char magic[8];in.read(magic,8);if(std::string(magic,8)!="R150NF31")throw std::runtime_error("wrong NF binary");
 const int ns=gb_u32(in),nt=gb_u32(in),q=gb_u32(in),D=45,W=(q+31)/32,nw=(D+1)*W;
 if(ns!=2195||nt!=9||q!=1034)throw std::runtime_error("not the full original finite module");
 std::string prefix=argv[3];std::ofstream dag(prefix+"-operations.bin",std::ios::binary);if(!dag)throw std::runtime_error("DAG open");
 dag.write("R150GBO1",8);u32(dag,ns);u32(dag,q);dag.put(char(D));
 BitOps ops;std::vector<GBPivot> piv(q);int rank=0,processed=0;uint64_t reductions=0,swaps=0;int maxInputDegree=-1;bool stopped=false;
 auto lead=[&](const Row &r,int upper=45)->GBLead{
  for(int d=upper;d>=0;d--)for(int w=0;w<W;w++){
   const int off=d*W+w;uint32_t nz=r[off]|r[nw+off]|r[2*nw+off]|r[3*nw+off]|r[4*nw+off];
   if(nz){int c=32*w+__builtin_ctz(nz);if(c>=q)throw std::runtime_error("nonzero padding");return {d,c,BitOps::get(r,nw,d*W*32+c)};}
  }return {};
 };
 auto readRow=[&](int &raw,int &target)->Row{
  raw=gb_u32(in);target=gb_u16(in);int count=gb_u32(in),previous=0;Row r(5*nw);
  if(count<0||count>q)throw std::runtime_error("component count");
  for(int a=0;a<count;a++){
   int c=gb_u16(in),len=gb_byte(in);if(c<=previous||c>q||len<1||len>D+1)throw std::runtime_error("component/exponent order");previous=c;
   int last=0;for(int k=0;k<len;k++){int v=gb_byte(in);if(v>=31)throw std::runtime_error("noncanonical F31 coefficient");BitOps::set(r,nw,k*W*32+c-1,v);last=v;}
   if(!last)throw std::runtime_error("trailing zero coefficient");
  }return r;
 };
 for(int index=0;index<ns;index++){
  int raw,target;Row current=readRow(raw,target);if(raw<1||raw>6188||target!=0)throw std::runtime_error("original source identity");
  if(stopped)continue;
  uint32_t node=index+1;GBLead L=lead(current);maxInputDegree=std::max(maxInputDegree,L.degree);
  dag.put('I');u32(dag,index+1);u32(dag,raw);
  while(L.degree>=0){
   auto &P=piv[L.component];
   if(!P.data){
    P.data=std::make_unique<Triple>();(*P.data)[0]=std::move(current);BitOps::refresh(*P.data,nw,0);P.degree=L.degree;P.coefficient=L.coefficient;P.node=node;rank++;
    dag.put('B');u16(dag,L.component+1);u32(dag,node);break;
   }
   if(P.degree>L.degree){
    std::swap(current,(*P.data)[0]);std::swap(node,P.node);std::swap(L.degree,P.degree);std::swap(L.coefficient,P.coefficient);
    BitOps::refresh(*P.data,nw,0);swaps++;dag.put('S');u16(dag,L.component+1);u32(dag,node);u32(dag,P.node);
   }
   const int shift=L.degree-P.degree,a=L.coefficient*ops.inv[P.coefficient]%31;
   if(shift<0||shift>D||!a)throw std::runtime_error("invalid Euclidean reduction");
   auto R=ops.rep[31-a];BitOps::add(current,nw,shift*W,(*P.data)[R.c],nw,0,(P.degree+1)*W,R.rot,R.neg);
   dag.put('R');u32(dag,node);u32(dag,P.node);dag.put(char(shift));dag.put(char(a));
   reductions++;if(reductions+ns>UINT32_MAX)throw std::runtime_error("DAG node overflow");node=uint32_t(ns+reductions);
   GBLead next=lead(current,L.degree);
   if(next.degree>L.degree||(next.degree==L.degree&&next.component<=L.component))throw std::runtime_error("leading monomial did not decrease");
   L=next;
  }
  if(L.degree<0){dag.put('Z');u32(dag,node);}
  processed++;
  if(processed==1||processed%25==0||processed==ns)std::cout<<"{\"phase\":\"streaming-graded-gb\",\"processedSources\":"<<processed<<",\"basisRows\":"<<rank<<",\"reductions\":"<<reductions<<",\"swaps\":"<<swaps<<",\"elapsedSeconds\":"<<seconds()<<"}\n"<<std::flush;
  if((maxSources&&processed>=maxSources)||seconds()>=softSeconds)stopped=true;
 }
 std::vector<Row> targets;for(int j=0;j<nt;j++){int raw,target;targets.push_back(readRow(raw,target));if(raw!=0||target!=j+2)throw std::runtime_error("original target identity");}
 if(in.get()!=EOF)throw std::runtime_error("trailing NF data");
 const bool complete=processed==ns;if(complete&&rank!=1021)throw std::runtime_error("complete source module rank is not 1021");
 std::ofstream out(prefix+"-basis.ssi"),meta(prefix+"-basis-metadata.json");if(!out||!meta)throw std::runtime_error("basis output open");out<<header<<"10 "<<q<<" "<<rank<<"\n";
 meta<<"{\"format\":\"r150-native-graded-module-basis-v1\",\"moduleOrder\":\"dp,c\",\"field\":31,\"components\":1034,\"fullSourceCount\":2195,\"processedSources\":"<<processed<<",\"complete\":"<<(complete?"true":"false")<<",\"basis\":[";
 auto writeVector=[&](const Row &r,int scale){
  uint32_t terms=0;for(int w=0;w<nw;w++)terms+=__builtin_popcount(r[w]|r[nw+w]|r[2*nw+w]|r[3*nw+w]|r[4*nw+w]);
  out<<terms<<" ";for(int k=D;k>=0;k--)for(int c=0;c<q;c++){int a=BitOps::get(r,nw,k*W*32+c);if(a)out<<(a*scale%31)<<" "<<(c+1)<<" "<<k<<" ";}out<<"\n";
 };
 int column=0,maxBasisDegree=-1;
 for(int c=0;c<q;c++)if(piv[c].data){const auto &P=piv[c];GBLead L=lead((*P.data)[0]);if(L.component!=c||L.degree!=P.degree||L.coefficient!=P.coefficient)throw std::runtime_error("stored pivot identity");
  const int scale=ops.inv[P.coefficient];writeVector((*P.data)[0],scale);if(column++)meta<<",";
  meta<<"{\"column\":"<<column<<",\"pivotComponent\":"<<c+1<<",\"degree\":"<<P.degree<<",\"sourceNode\":"<<P.node<<",\"normalization\":"<<scale<<"}";
  dag.put('F');u16(dag,c+1);u32(dag,P.node);dag.put(char(scale));maxBasisDegree=std::max(maxBasisDegree,P.degree);
 }
 meta<<"],\"targets\":[2,3,4,5,6,7,8,9,10]}\n";out<<"10 "<<q<<" "<<nt<<"\n";for(const auto &t:targets)writeVector(t,1);
 out.close();meta.close();dag.close();if(!out||!meta||!dag)throw std::runtime_error("output failed");
 std::cout<<"{\"status\":\""<<(complete?"native-univariate-gb-complete":"native-univariate-gb-prefix-only")<<"\",\"processedSources\":"<<processed<<",\"fullSourceCount\":2195,\"basisRows\":"<<rank<<",\"maximumInputDegree\":"<<maxInputDegree<<",\"maximumBasisDegree\":"<<maxBasisDegree<<",\"reductions\":"<<reductions<<",\"swaps\":"<<swaps<<",\"elapsedSeconds\":"<<seconds()<<"}\n";
 return 0;
}catch(const std::exception &e){std::cerr<<"NATIVE_UNIVARIATE_GB_FAILED "<<e.what()<<"\n";return 1;}}
