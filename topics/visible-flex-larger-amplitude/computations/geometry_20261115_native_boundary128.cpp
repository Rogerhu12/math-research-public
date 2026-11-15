// Undamped complete far-to-cut response using all 112 homogeneous modes.
// Inputs are the explicitly bound finite-trace stage maps at one binary128
// current state.  No fixed64 or R273 matrix is accepted by the launcher.
#include "geometry_20261115_native_shared_trace128.hpp"
using namespace shared_trace128;

struct ThinQR {V Qthin,R,reflectors,tau;int rows,columns;};
static ThinQR full_thin_qr(const V &input,int rows,int columns){
  if(rows<columns||input.size()!=size_t(rows)*columns)throw std::runtime_error("QR-shape");
  V A=input,Vh(size_t(rows)*columns,0),tau(columns),R(size_t(columns)*columns,0);
  for(int k=0;k<columns;++k){
    time_check();Q scale=0;
    for(int i=k;i<rows;++i){finite(A[size_t(i)*columns+k],"QR-input");scale=qmax(scale,fabsq(A[size_t(i)*columns+k]));}
    if(scale==0)throw std::runtime_error("exact-zero-QR-column-no-rank-truncation");
    Q sum=0;
    for(int i=k;i<rows;++i){const Q v=A[size_t(i)*columns+k]/scale;sum+=v*v;}
    const Q length=scale*sqrtq(sum),x0=A[size_t(k)*columns+k],
      alpha=x0>=0?-length:length,denominator=x0-alpha;
    if(denominator==0||alpha==0)throw std::runtime_error("zero-Householder-denominator");
    tau[k]=(alpha-x0)/alpha;Vh[size_t(k)*columns+k]=1;
    finite(tau[k],"Householder-tau");
    for(int i=k+1;i<rows;++i)Vh[size_t(i)*columns+k]=A[size_t(i)*columns+k]/denominator;
    for(int j=k;j<columns;++j){
      Q dot=0;for(int i=k;i<rows;++i)dot+=Vh[size_t(i)*columns+k]*A[size_t(i)*columns+j];
      dot*=tau[k];
      for(int i=k;i<rows;++i){A[size_t(i)*columns+j]-=Vh[size_t(i)*columns+k]*dot;finite(A[size_t(i)*columns+j],"QR-update");}
    }
    // Retain the computed upper triangle.  Eliminated entries are structural
    // zeros in the stored triangular factor; readback uses the full input.
    for(int j=k;j<columns;++j)R[size_t(k)*columns+j]=A[size_t(k)*columns+j];
    if(R[size_t(k)*columns+k]==0)throw std::runtime_error("exact-zero-R-diagonal");
  }
  V Qthin(size_t(rows)*columns,0);
  for(int i=0;i<columns;++i)Qthin[size_t(i)*columns+i]=1;
  for(int k=columns-1;k>=0;--k){
    time_check();
    for(int j=0;j<columns;++j){
      Q dot=0;for(int i=k;i<rows;++i)dot+=Vh[size_t(i)*columns+k]*Qthin[size_t(i)*columns+j];
      dot*=tau[k];
      for(int i=k;i<rows;++i)Qthin[size_t(i)*columns+j]-=Vh[size_t(i)*columns+k]*dot;
    }
  }
  for(Q x:Qthin)finite(x,"orthogonal-frame");
  return {std::move(Qthin),std::move(R),std::move(Vh),std::move(tau),rows,columns};
}
static V multiply(const V &A,const V &B,int rows,int inner,int columns){
  if(A.size()!=size_t(rows)*inner||B.size()!=size_t(inner)*columns)throw std::runtime_error("matrix-product-shape");
  V C(size_t(rows)*columns,0);
  for(int i=0;i<rows;++i){
    if((i&7)==0)time_check();
    for(int k=0;k<inner;++k)for(int j=0;j<columns;++j)
      C[size_t(i)*columns+j]+=A[size_t(i)*inner+k]*B[size_t(k)*columns+j];
  }
  for(Q x:C)finite(x,"matrix-product");return C;
}
static V upper_solve(const V &R,const V &B,int n,int columns){
  if(R.size()!=size_t(n)*n||B.size()!=size_t(n)*columns)throw std::runtime_error("triangular-shape");
  V X=B;
  for(int i=n-1;i>=0;--i){
    time_check();
    if(R[size_t(i)*n+i]==0)throw std::runtime_error("exact-zero-triangular-pivot");
    for(int j=0;j<columns;++j){
      Q v=X[size_t(i)*columns+j];
      for(int k=i+1;k<n;++k)v-=R[size_t(i)*n+k]*X[size_t(k)*columns+j];
      X[size_t(i)*columns+j]=v/R[size_t(i)*n+i];finite(X[size_t(i)*columns+j],"triangular-solution");
    }
  }
  return X;
}
static V square_qr_solve(const ThinQR &qr,const V &B,int columns){
  if(qr.rows!=qr.columns||B.size()!=size_t(qr.rows)*columns)throw std::runtime_error("square-QR-shape");
  const int n=qr.rows;V QtB(size_t(n)*columns,0);
  for(int i=0;i<n;++i)for(int k=0;k<n;++k)for(int j=0;j<columns;++j)
    QtB[size_t(i)*columns+j]+=qr.Qthin[size_t(k)*n+i]*B[size_t(k)*columns+j];
  return upper_solve(qr.R,QtB,n,columns);
}
static Q difference_max(const V &A,const V &B){
  if(A.size()!=B.size())throw std::runtime_error("readback-shape");
  Q m=0;for(size_t i=0;i<A.size();++i){const Q v=fabsq(A[i]-B[i]);finite(v,"readback");m=qmax(m,v);}return m;
}

int main(int argc,char **argv){
  fs::path out;int inward_completed=0,outward_completed=0,row_stages_completed=0;
  try{
    action_guard();
    if(argc!=7)throw std::runtime_error(
      "usage: packet complete-stage-map-directory cut-Q-per-height.f128 out seconds keep-full-readback");
    const int seconds=std::stoi(argv[5]);
    if(seconds<1||seconds>20000||std::string(argv[6])!="yes")
      throw std::runtime_error("explicit-complete-readback-required");
    deadline=Clock::now()+std::chrono::seconds(seconds);
    const auto started=Clock::now();Problem p(argv[1]);const fs::path stage_root=argv[2];
    // The caller must declare the actual local extension H -> Q_cut.  We do
    // not silently infer it from the rounded frozen H/r^4 target words.
    const V forcing=read128(argv[3],size_t(p.M)*p.M);
    out=argv[4];if(fs::exists(out))throw std::runtime_error("fresh-output-required");
    fs::create_directories(out/"large-arrays");
    const fs::path arrays=out/"large-arrays";
    const int m=p.M,k=p.K,d=p.depth;
    V far(size_t(k)*m,0);
    for(int j=0;j<m;++j){far[size_t(j)*m+j]=1;far[size_t(m+j)*m+j]=p.far[j];}
    auto fq=full_thin_qr(far,k,m);
    raw128(arrays/"far-original-frame.f128",far);
    raw128(arrays/"far-R.f128",fq.R);
    raw128(arrays/("frame-"+std::to_string(d)+".f128"),fq.Qthin);
    Q max_factor_readback=difference_max(multiply(fq.Qthin,fq.R,k,m,m),far);
    V next=std::move(fq.Qthin);
    for(int n=d-1;n>=0;--n){
      time_check();
      const V T=read128(stage_root/"large-arrays"/("stage-"+std::to_string(n))/"shape-columns-after-port.f128",size_t(k)*k);
      const V mapped=multiply(T,next,k,k,m);auto qr=full_thin_qr(mapped,k,m);
      const V reconstructed=multiply(qr.Qthin,qr.R,k,m,m);
      max_factor_readback=qmax(max_factor_readback,difference_max(reconstructed,mapped));
      raw128(arrays/("frame-"+std::to_string(n)+".f128"),qr.Qthin);
      raw128(arrays/("R-"+std::to_string(n)+".f128"),qr.R);
      raw128(arrays/("mapped-frame-"+std::to_string(n)+".f128"),mapped);
      next=std::move(qr.Qthin);++inward_completed;
    }
    V cutQ(size_t(m)*m);
    for(int i=0;i<m;++i)for(int j=0;j<m;++j)cutQ[size_t(i)*m+j]=next[size_t(i)*m+j];
    auto cutqr=full_thin_qr(cutQ,m,m);
    raw128(arrays/"cut-Q-block.f128",cutQ);
    raw128(arrays/"cut-Q-block-orthogonal.f128",cutqr.Qthin);
    raw128(arrays/"cut-Q-block-R.f128",cutqr.R);
    V unit(size_t(m)*m,0),cutP(size_t(m)*m);
    for(int i=0;i<m;++i)unit[size_t(i)*m+i]=1;
    for(int i=0;i<m;++i)for(int j=0;j<m;++j)cutP[size_t(i)*m+j]=next[size_t(m+i)*m+j];
    const V chart_inverse=square_qr_solve(cutqr,unit,m);
    raw128(arrays/"cut-Q-block-inverse-numeric.f128",chart_inverse);
    raw128(arrays/"cut-Pi-graph-per-Q.f128",multiply(cutP,chart_inverse,m,m,m));
    V coeff=square_qr_solve(cutqr,forcing,m);
    raw128(arrays/"cut-forcing.f128",forcing);
    raw128(arrays/"coeff-0.f128",coeff);
    raw128(arrays/"response-0.f128",multiply(next,coeff,k,m,m));
    outward_completed=1;
    for(int n=0;n<d;++n){
      time_check();
      const V R=read128(arrays/("R-"+std::to_string(n)+".f128"),size_t(m)*m);
      coeff=upper_solve(R,coeff,m,m);
      raw128(arrays/("coeff-"+std::to_string(n+1)+".f128"),coeff);
      const V frame=read128(arrays/("frame-"+std::to_string(n+1)+".f128"),size_t(k)*m);
      raw128(arrays/("response-"+std::to_string(n+1)+".f128"),multiply(frame,coeff,k,m,m));
      ++outward_completed;
    }
    const size_t rows=size_t(d+1)*k;
    // Full [129248,112] readback is retained in original cut/stage/far order,
    // streamed to disk.  No top-row reduction, truncation or threshold gate.
    std::ofstream ledger(arrays/"complete-linear-readback.f128",std::ios::binary|std::ios::trunc);
    if(!ledger)throw std::runtime_error("readback-open");
    Q max_absolute=0,max_sigma_normalized=0;size_t worst_row=0;int worst_column=0;
    const auto write_rows=[&](const V &block,size_t first_row,Q sigma){
      if(block.size()%m)throw std::runtime_error("readback-block-shape");
      for(size_t i=0;i<block.size();++i){
        finite(block[i],"boundary-readback");const Q a=fabsq(block[i]),scaled=a/sigma;
        finite(scaled,"boundary-normalized-readback");max_absolute=qmax(max_absolute,a);
        if(scaled>max_sigma_normalized){max_sigma_normalized=scaled;worst_row=first_row+i/m;worst_column=i%m;}
      }
      if(!ledger.write(reinterpret_cast<const char*>(block.data()),block.size()*sizeof(Q)))
        throw std::runtime_error("readback-write");
    };
    V current=read128(arrays/"response-0.f128",size_t(k)*m),cut_defect(size_t(m)*m);
    for(int i=0;i<m;++i)for(int j=0;j<m;++j)
      cut_defect[size_t(i)*m+j]=current[size_t(i)*m+j]-forcing[size_t(i)*m+j];
    write_rows(cut_defect,0,p.scales[0]);
    V mean_response(m,0);
    for(int n=0;n<d;++n){
      time_check();
      V following=read128(arrays/("response-"+std::to_string(n+1)+".f128"),size_t(k)*m);
      const V T=read128(stage_root/"large-arrays"/("stage-"+std::to_string(n))/"shape-columns-after-port.f128",size_t(k)*k);
      V defect=multiply(T,following,k,k,m);
      for(size_t i=0;i<defect.size();++i)defect[i]-=current[i];
      write_rows(defect,p.M+size_t(n)*k,p.scales[n]);
      const V means=read128(stage_root/"large-arrays"/("stage-"+std::to_string(n))/"mean-columns.f128",size_t(2)*k);
      const V dm=multiply(means,following,2,k,m);
      raw128(arrays/("stage-mean-response-"+std::to_string(n)+".f128"),dm);
      for(int j=0;j<m;++j)mean_response[j]+=dm[j]+dm[m+j];
      current=std::move(following);++row_stages_completed;
    }
    V far_defect(size_t(m)*m);
    for(int i=0;i<m;++i)for(int j=0;j<m;++j)
      far_defect[size_t(i)*m+j]=current[size_t(m+i)*m+j]-p.far[i]*current[size_t(i)*m+j];
    write_rows(far_defect,p.M+size_t(d)*k,p.scales[d]);
    ledger.flush();if(!ledger)throw std::runtime_error("readback-flush");
    raw128(arrays/"complete-mean-height-response.f128",mean_response);
    std::ostringstream s;
    s<<"{\"schema\":\"native-persistent128-complete-boundary-response-v1\",\"complete\":true"
      <<",\"M\":"<<m<<",\"K\":"<<k<<",\"depth\":"<<d<<",\"height_columns\":"<<m
      <<",\"node_response_shape\":["<<d+1<<','<<k<<','<<m<<']'
      <<",\"full_original_row_count\":"<<rows<<",\"full_original_row_readback_shape\":["<<rows<<','<<m<<']'
      <<",\"far_and_stage_thin_QR_count\":"<<d+1<<",\"cut_square_QR_count\":1"
      <<",\"all_112_modes_retained\":true,\"SVD_or_rank_truncation\":false"
      <<",\"normal_matrix_formed\":false,\"R273_or_fixed64_used\":false"
      <<",\"node_n_plus_1_maps_to_node_n\":true,\"caller_declared_cut_forcing\":true"
      <<",\"cut_and_far_readback_complete\":true,\"both_stage_mean_rows_retained\":true"
      <<",\"factorization_readback_max_absolute_decimal\":"<<quoted(qstr(max_factor_readback))
      <<",\"linear_readback_max_absolute_decimal\":"<<quoted(qstr(max_absolute))
      <<",\"linear_readback_max_sigma_normalized_decimal\":"<<quoted(qstr(max_sigma_normalized))
      <<",\"linear_readback_worst_row\":"<<worst_row<<",\"linear_readback_worst_height_column\":"<<worst_column
      <<",\"numeric_readback_not_verified_error_bound\":true,\"linear_readback_is_not_acceptance_gate\":true"
      <<",\"cut_chart_nonsingularity_proved_over_reals\":false"
      <<",\"endpoint338x112_supplied\":false,\"physical_audit_supplied\":false,\"native_accepted\":false"
      <<",\"seconds_budget\":"<<seconds<<",\"elapsed_seconds\":"<<std::setprecision(17)
      <<std::chrono::duration<double>(Clock::now()-started).count()<<'}';
    json_file(out/"summary.json",s.str());
    std::cout<<s.str()<<'\n';return 0;
  }catch(const std::exception &e){
    std::ostringstream s;
    s<<"{\"schema\":\"native-persistent128-complete-boundary-response-v1\",\"complete\":false"
      <<",\"inward_stages_completed\":"<<inward_completed<<",\"outward_nodes_completed\":"<<outward_completed
      <<",\"original_stage_row_blocks_read_back\":"<<row_stages_completed
      <<",\"unvisited_stages_or_rows_present\":true,\"native_accepted\":false"
      <<",\"resource_partial\":"<<(std::string(e.what())=="explicit-experiment-time-budget"?"true":"false")
      <<",\"error\":"<<quoted(e.what())<<'}';
    std::cerr<<s.str()<<'\n';
    if(!out.empty()&&fs::is_directory(out))try{json_file(out/"summary.json",s.str());}catch(...){}
    return 2;
  }
}
