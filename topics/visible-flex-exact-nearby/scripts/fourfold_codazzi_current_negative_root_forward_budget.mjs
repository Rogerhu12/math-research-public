#!/usr/bin/env node
// Current ac1d... moving negative-root complete forward four-state contract.
// Pure normalized rational arithmetic. Inputs are proved outward text bounds;
// no binary native reports or sampled candidate coefficients are read.
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;}
class Q{
 constructor(n=0n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
 add(b){return new Q(this.n*b.d+b.n*this.d,this.d*b.d);}
 sub(b){return new Q(this.n*b.d-b.n*this.d,this.d*b.d);}
 mul(b){return new Q(this.n*b.n,this.d*b.d);}
 div(b){return new Q(this.n*b.d,this.d*b.n);}
 pow(n){if(n<0)return new Q(this.d**BigInt(-n),this.n**BigInt(-n));return new Q(this.n**BigInt(n),this.d**BigInt(n));}
 lt(b){return this.n*b.d<b.n*this.d;}
 le(b){return this.n*b.d<=b.n*this.d;}
 str(){return this.d===1n?String(this.n):String(this.n)+"/"+String(this.d);}
}
const q=(n,d=1)=>new Q(BigInt(n),BigInt(d));
function dec(s){const[a,b=""]=s.split(".");const d=10n**BigInt(b.length);return new Q(BigInt(a)*d+BigInt(b),d);}

function zeros(n){return Array.from({length:n},()=>Array.from({length:n},()=>q(0)));}
function mmul(A,B){const C=zeros(A.length);for(let i=0;i<A.length;i++)for(let j=0;j<A.length;j++)for(let k=0;k<A.length;k++)C[i][j]=C[i][j].add(A[i][k].mul(B[k][j]));return C;}
function madd(A,B){return A.map((row,i)=>row.map((x,j)=>x.add(B[i][j])));}
function mscale(A,c){return A.map(row=>row.map(x=>x.mul(c)));}
function eye(n){const a=zeros(n);for(let i=0;i<n;i++)a[i][i]=q(1);return a;}
function rows(A){return A.map(row=>row.reduce((a,b)=>a.add(b),q(0)));}
function upward(x,digits=12){const t=10n**BigInt(digits);return new Q((x.n*t+x.d-1n)/x.d,t);}
function runNegativeBudget(){
 const gates=[],g=(name,pass,values={})=>{gates.push({name,passed:!!pass,...values});if(!pass)throw Error(name);};
 const rlo=dec("0.2383968742994"),rhi=dec("0.2383968743003"),ra=dec("0.2383878742994");
 const R=q(1,100000),ell=rhi.sub(ra),h=R;
 const left=q(2147184947341121n,9007199254740992n),right=q(4295308144604611n,18014398509481984n);
 g("same_current_candidate_piece_and_joint_domain",left.lt(ra)&&ra.lt(rlo)&&rhi.lt(right)&&rlo.sub(R).lt(ra)&&ell.lt(R));
 g("left_is_exact_root_lower_minus_nine_micro",rlo.sub(q(9,1000000)).le(ra)&&ra.le(rlo.sub(q(9,1000000))));
 const be=q(9,5),ga=q(9,5),ma=q(28,25),em=q(201,100),qq=q(1,40),K=q(61,100000);
 const u=q(8,5),v=q(9,5),u1=q(27),v1=q(86),u1A=q(216),v1A=q(86);
 const Rs=q(13,8),Ls=q(28),L2=q(28000),S=q(13,5);
 g("negative_type_from_same_strict_Kprime",q(59).lt(dec("59.74380437"))&&dec("60.465470").mul(ell).lt(K)&&K.lt(qq.pow(2)));
 g("S_oscillation_and_absolute_bound",u.pow(2).add(K.mul(v.pow(2))).lt(S));
 g("R_bound_without_q_inverse",S.lt(Rs.pow(2)));
 g("L_bound_without_q_inverse",u1.pow(2).add(qq.pow(2).mul(v1.pow(2))).lt(Ls.pow(2)));
 g("L2_from_complete_finite_derivative_sums",q(128).mul(u1A).add(qq.mul(q(128)).mul(v1A)).lt(L2));
 g("complete_d_phi_sup_5",be.mul(S).lt(q(5)));
 g("first_local_energy_diagonal_16",be.mul(q(1).add(q(3).mul(u.pow(2))).add(K.mul(v.pow(2)))).lt(q(16)));
 g("second_local_energy_diagonal_3",be.mul(q(1).add(q(3).mul(K).mul(v.pow(2)))).lt(q(3))&&be.mul(u.pow(2).sub(q(1))).lt(q(3)));
 g("E0_diagonal_60",q(16).add(q(5,2)).add(be.mul(Rs).mul(Ls).div(q(2))).lt(q(60)));
 g("E0_mean_column_13_over_10",ga.mul(qq).mul(Ls).lt(q(13,10)));
 g("true_mean_E0_column_7",q(2).mul(be).mul(ma).mul(Rs).lt(q(7)));
 g("true_mean_diagonal_7",be.mul(q(1).add(S)).lt(q(7)));
 g("E1_E0_column_41800",be.mul(Rs).mul(q(10).mul(Ls).add(L2.div(q(2)))).lt(q(41800)));
 g("E1_mean_column_1260",ga.mul(qq).mul(L2).le(q(1260)));
 g("E1_diagonal_19",q(16).add(q(5,2)).lt(q(19)));
 g("Y_E0_column_137",q(2).mul(be).mul(u).mul(v).add(be.mul(Rs).mul(v1).div(q(2))).lt(q(137)));
 g("Y_mean_column_49",ga.mul(u1).lt(q(49)));
 g("Y_E1_column_201_over_100",em.le(q(201,100)));
 g("Y_diagonal_6",q(3).add(q(5,2)).lt(q(6)));
 const A=[
  [q(60),q(13,10),q(0),q(0)],
  [q(7),q(7),q(0),q(0)],
  [q(41800),q(1260),q(19),q(0)],
  [q(137),q(49),q(201,100),q(6)]
 ];
 const B=mscale(A,h),z=rows(B).reduce((a,b)=>a.lt(b)?b:a,q(0)),degree=12;
 let term=eye(4),sum=eye(4),factorial=1n;
 for(let k=1;k<=degree;k++){term=mscale(mmul(term,B),q(1,k));sum=madd(sum,term);factorial*=BigInt(k);}
 const fac13=factorial*13n;
 const tail=z.pow(13).div(new Q(fac13)).div(q(1).sub(z.div(q(14))));
 g("complete_matrix_exponential_tail_valid",z.lt(q(1))&&z.div(q(14)).lt(q(1)));
 g("full_matrix_tail_below_1e_minus_14",tail.lt(q(1,100000000000000n)),{exact_tail_upper:tail.str()});
 const P=sum.map(row=>row.map(x=>upward(x.add(tail),12))),rr=rows(P);
 g("outward_rounding_keeps_every_positive_matrix_entry",P.every((row,i)=>row.every((x,j)=>sum[i][j].add(tail).le(x))));
 g("ordinary_state_gain_below_142",rr[0].pow(2).add(rr[3].pow(2)).lt(q(71,50).pow(2)));
 const room=q(8,5).pow(2).sub(rr[3].pow(2));
 g("complete_root_Airy_gain_below_16_by_interpolation",q(0).lt(room)&&rr[0].pow(4).mul(rr[0].pow(2).add(rr[2].pow(2))).lt(room.pow(3)));
 g("independent_true_mean_gain_below_1001",rr[1].lt(q(1001,1000)));
 g("independent_second_state_gain_below_1003",rr[3].lt(q(1003,1000)));
 g("L2_radial_source_to_state_below_0045",q(71,50).pow(2).mul(h).lt(q(9,2000).pow(2)));
 g("L2_radial_source_to_Airy_below_0051",q(8,5).pow(2).mul(h).lt(q(51,10000).pow(2)));
 g("same_positive_reference_root_input_below_8_and_0026",q(5).mul(q(8,5)).le(q(8))&&q(5).mul(q(51,10000)).lt(q(13,500)));
 return{
  kind:"actual_current_moving_negative_inner_germ_full_forward_Cauchy",
  complete:true,arithmetic:"normalized BigInt rational matrix exponential with complete tail",
  source:"scripts/fourfold_codazzi_current_negative_root_forward_budget.mjs",
  candidate_sha256:"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
  domain:{left:ra.str(),right:"the actual root r*(eta)",whole_original_eta:true,max_length:ell.str(),exponential_budget_length:h.str(),actual_piece:2549,joins_inside:false},
  matrix_state_order:["E0=||(h1,sqrt(-K)h2)||2","M=|mean(h2)|","E1=||(h1_phi,sqrt(-K)h2_phi)||2","Y=||h2||2"],
  exact_constant_comparison_matrix:A.map(row=>row.map(x=>x.str())),
  complete_outward_forward_matrix:P.map(row=>row.map(x=>x.str())),
  forward_matrix_decimal_scale:12,
  complete_row_sums:rr.map(x=>x.str()),
  source_vector:["integral ||f||2","integral ||f||2","integral ||f_phi||2","integral ||f||2"],
  coefficients_paid:{Kprime_over_K:"nonpositive on the exact negative interval; discarded only forward",q_inverse_used:false,all_means_retained:true,all_fourier_modes:true,complete_nonlocal_and_mean_rank:true},
  norms:{initial:"ordinary moving H1",source:"ordinary L2_r H1_phi",ordinary_state_Linfinity_L2_initial:"71/50",ordinary_state_Linfinity_L2_source:"9/2000",complete_root_Airy_initial:"8/5",complete_root_Airy_source:"51/10000",positive_reference_root_pair_initial:"8",positive_reference_root_pair_source:"13/500"},
  endpoint_limit:{h1:"strong Hs for every s<1; bounded H1",h2:"strong L2 via its actual transport equation",mean:"the true mean limit, independent row retained"},
  permissions:{complete_forward_Cauchy:true,backward_Cauchy:false,negative_one_incoming_BVP:false,physical_theta_variation_bridge:false,previous_piece_left_to_this_left:false,global_return_inverse:false,whole_nonlinear_BVP:false},
  gates
 };
}
export {runNegativeBudget};
// NODE CLI.
if(typeof process!=="undefined"&&process.versions?.node&&process.argv[1]?.endsWith("fourfold_codazzi_current_negative_root_forward_budget.mjs")){
 const r=runNegativeBudget(),j=JSON.stringify(r,null,2)+"\n",k=process.argv.indexOf("--out");
 if(k>=0){const fs=await import("node:fs");fs.writeFileSync(process.argv[k+1],j);process.stdout.write(JSON.stringify({complete:r.complete,gates:r.gates.length,out:process.argv[k+1]})+"\n");}
 else process.stdout.write(j);
}
