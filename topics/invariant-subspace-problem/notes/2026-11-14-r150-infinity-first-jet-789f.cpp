// Exact constant rank and first connecting map of the original infinity jet.
// Input is the frozen native NF format, with L reversed at weight 10 and
// Gamma reversed at weight 5 before truncation modulo u^2. No target is used.
#define main r150_frozen_normal_form_main
#include "2026-11-14-r150-native-normal-form-789f.cpp"
#undef main

static uint32_t jet32(std::istream &s){uint32_t v=0;for(int j=0;j<4;j++){int c=s.get();if(c<0)throw std::runtime_error("truncated u32");v|=uint32_t(c)<<(8*j);}return v;}
static uint16_t jet16(std::istream &s){int a=s.get(),b=s.get();if(a<0||b<0)throw std::runtime_error("truncated u16");return a+256*b;}
struct JetPivot {std::unique_ptr<Triple> rows;int coefficient=0,index=0,raw=0;};
struct JetKernel {Row row;int index=0,raw=0;};
int main(int argc,char **argv){try{
 if(argc!=3)return 2;
 auto start=std::chrono::steady_clock::now();
 auto seconds=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();};
 std::ifstream in(argv[1],std::ios::binary);char magic[8];in.read(magic,8);
 if(std::string(magic,8)!="R150NF31")throw std::runtime_error("wrong normal form header");
 int ns=jet32(in),nt=jet32(in),q=jet32(in),W=(q+31)/32,nw=2*W;
 if(ns!=2855||nt!=0||q!=1034)throw std::runtime_error("wrong infinity source dimensions");
 std::string prefix=argv[2];std::ofstream dag(prefix+"-operations.bin",std::ios::binary);
 if(!dag)throw std::runtime_error("cannot write operations");
 dag.write("R150IJ31",8);u32(dag,ns);u32(dag,q);
 BitOps ops;std::vector<JetPivot> base(q),conn(q);std::vector<JetKernel> kernels;
 int rank0=0,rank1=0;uint64_t reductions0=0,projections=0,reductions1=0;
 auto lead=[&](const Row &r,int stride)->int{
  for(int w=0;w<W;w++){uint32_t v=r[w]|r[stride+w]|r[2*stride+w]|r[3*stride+w]|r[4*stride+w];
   if(v){int c=32*w+__builtin_ctz(v);if(c>=q)throw std::runtime_error("nonzero padding");return c;}}
  return -1;
 };
 for(int index=0;index<ns;index++){
  int raw=jet32(in),target=jet16(in),count=jet32(in),previous=0;Row current(5*nw);
  if(raw<1||raw>6188||target!=0||count>q)throw std::runtime_error("bad original source");
  for(int j=0;j<count;j++){
   int c=jet16(in),len=in.get();if(c<=previous||c>q||len<1||len>46)throw std::runtime_error("bad coefficient format");previous=c;
   int last=0;for(int k=0;k<len;k++){int a=in.get();if(a<0||a>=31)throw std::runtime_error("bad field coefficient");if(k<2)BitOps::set(current,nw,k*W*32+c-1,a);last=a;}
   if(!last)throw std::runtime_error("trailing zero coefficient");
  }
  dag.put('I');u16(dag,index+1);u16(dag,raw);
  int c=lead(current,nw);
  while(c>=0){
   int a=BitOps::get(current,nw,c);auto &P=base[c];
   if(!P.rows){P.rows=std::make_unique<Triple>();(*P.rows)[0]=std::move(current);BitOps::refresh(*P.rows,nw,0);P.coefficient=a;P.index=index+1;P.raw=raw;rank0++;dag.put('B');u16(dag,c+1);break;}
   a=a*ops.inv[P.coefficient]%31;auto R=ops.rep[31-a];
   BitOps::add(current,nw,0,(*P.rows)[R.c],nw,0,nw,R.rot,R.neg);
   dag.put('R');u16(dag,c+1);dag.put(char(a));reductions0++;c=lead(current,nw);
  }
  if(c<0){Row tail(5*W);for(int b=0;b<5;b++)for(int w=0;w<W;w++)tail[b*W+w]=current[b*nw+W+w];kernels.push_back({std::move(tail),index+1,raw});dag.put('Z');}
  if((index+1)%250==0)std::cout<<"{\"phase\":\"constant-jet-rank\",\"sources\":"<<index+1<<",\"rank\":"<<rank0<<",\"elapsedSeconds\":"<<seconds()<<"}\n"<<std::flush;
 }
 if(in.get()!=EOF)throw std::runtime_error("trailing normal form data");
 for(auto &K:kernels){
  Row current=std::move(K.row);dag.put('J');u16(dag,K.index);u16(dag,K.raw);
  // Project onto the true cokernel of the complete constant source matrix.
  for(int c=0;c<q;c++)if(base[c].rows){int a=BitOps::get(current,W,c);if(!a)continue;
   auto &P=base[c];a=a*ops.inv[P.coefficient]%31;auto R=ops.rep[31-a];
   BitOps::add(current,W,0,(*P.rows)[R.c],nw,0,W,R.rot,R.neg);
   dag.put('P');u16(dag,c+1);dag.put(char(a));projections++;
  }
  int c=lead(current,W);
  while(c>=0){
   if(base[c].rows)throw std::runtime_error("connecting row is not a cokernel normal form");
   int a=BitOps::get(current,W,c);auto &P=conn[c];
   if(!P.rows){P.rows=std::make_unique<Triple>();(*P.rows)[0]=std::move(current);BitOps::refresh(*P.rows,W,0);P.coefficient=a;P.index=K.index;P.raw=K.raw;rank1++;dag.put('C');u16(dag,c+1);break;}
   a=a*ops.inv[P.coefficient]%31;auto R=ops.rep[31-a];
   BitOps::add(current,W,0,(*P.rows)[R.c],W,0,W,R.rot,R.neg);
   dag.put('Q');u16(dag,c+1);dag.put(char(a));reductions1++;c=lead(current,W);
  }
  if(c<0)dag.put('0');
 }
 std::ofstream out(prefix+"-summary.json");if(!out)throw std::runtime_error("summary output");
 out<<"{\"format\":\"r150-infinity-first-jet-v1\",\"field\":31,\"components\":"<<q<<",\"sources\":"<<ns<<",\"constantRank\":"<<rank0<<",\"kernelRows\":"<<kernels.size()<<",\"connectingRank\":"<<rank1<<",\"constantReductions\":"<<reductions0<<",\"cokernelProjections\":"<<projections<<",\"connectingReductions\":"<<reductions1<<",\"elapsedSeconds\":"<<seconds()<<",\"constantPivots\":[";
 bool first=true;for(int c=0;c<q;c++)if(base[c].rows){if(!first)out<<',';first=false;auto &P=base[c];out<<"["<<c+1<<','<<P.index<<','<<P.raw<<','<<P.coefficient<<"]";}
 out<<"],\"connectingPivots\":[";first=true;for(int c=0;c<q;c++)if(conn[c].rows){if(!first)out<<',';first=false;auto &P=conn[c];out<<"["<<c+1<<','<<P.index<<','<<P.raw<<','<<P.coefficient<<"]";}
 out<<"]}\n";
 std::cout<<"{\"status\":\"infinity-first-jet-completed\",\"constantRank\":"<<rank0<<",\"connectingRank\":"<<rank1<<",\"elapsedSeconds\":"<<seconds()<<"}\n";
 return 0;
}catch(const std::exception &e){std::cerr<<e.what()<<'\n';return 1;}}
