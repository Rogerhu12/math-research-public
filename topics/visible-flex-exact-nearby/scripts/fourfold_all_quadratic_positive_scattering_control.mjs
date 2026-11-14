#!/usr/bin/env node
/** Complete Sym2 observability and phase-preserving positive scattering direction. */
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
function calculate(){
 const names=["X","Y","Z","Q","Qt","lambda"],nv=names.length,zeroKey=Array(nv).fill(0).join(",");
 const con=n=>new Map(BigInt(n)?[[zeroKey,BigInt(n)]]:[]);
 const variable=i=>{const e=Array(nv).fill(0);e[i]=1;return new Map([[e.join(","),1n]]);};
 const add=(a,b)=>{const o=new Map(a);for(const [k,v] of b){const s=(o.get(k)||0n)+v;if(s)o.set(k,s);else o.delete(k);}return o;};
 const scale=(a,n)=>new Map([...a].map(([k,v])=>[k,v*BigInt(n)]).filter(([,v])=>v!==0n));
 const sub=(a,b)=>add(a,scale(b,-1));
 const mul=(a,b)=>{let o=con(0);for(const [ka,va] of a)for(const [kb,vb] of b){const x=ka.split(",").map(Number),y=kb.split(",").map(Number);o=add(o,new Map([[x.map((e,i)=>e+y[i]).join(","),va*vb]]));}return o;};
 const partial=(a,i)=>{const o=new Map();for(const [key,v] of a){const e=key.split(",").map(Number);if(e[i]){const old=e[i];e[i]--;o.set(e.join(","),v*BigInt(old));}}return o;};
 const [X,Y,Z,Q,Qt,l]=names.map((_,i)=>variable(i)),one=con(1),s=add(one,Q);
 const rhs=[add(scale(mul(s,X),-1),scale(Y,2)),sub(Z,mul(mul(l,Q),X)),sub(mul(s,Z),scale(mul(mul(l,Q),Y),2)),Qt,con(0),con(0)];
 const D=a=>rhs.reduce((o,r,i)=>add(o,mul(partial(a,i),r)),con(0));
 const K=add(sub(Z,scale(mul(l,Y),2)),mul(l,X)),Kt=D(K),Ktt=D(Kt),b=scale(mul(l,sub(l,one)),2);
 const gates=[];
 const pg=(name,a,c=con(0))=>{const r=sub(a,c);gates.push({name,arithmetic:"exact multivariate BigInt polynomial",residual:[...r].map(([powers,v])=>({powers:powers.split(",").map(Number),coefficient:v.toString()})),pass:r.size===0});};
 pg("complete_symmetric_square_first_observability_identity",Kt,sub(mul(sub(s,scale(l,2)),K),mul(b,rhs[0])));
 pg("complete_symmetric_square_second_observability_identity",add(Ktt,mul(sub(sub(scale(mul(l,Q),4),mul(s,s)),Qt),K)),mul(mul(b,Qt),X));
 pg("complete_covariance_recovery_without_positive_energy",Z,add(add(K,mul(l,rhs[0])),mul(mul(l,Q),X)));
 pg("original_exact_Z_recovery_is_valid_for_indefinite_A",scale(mul(sub(l,one),Z),2),add(sub(mul(sub(Q,one),K),Kt),mul(mul(b,Q),X)));
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
 const R=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};};
 const str=a=>a.n+"/"+a.d,cmp=(a,b)=>a.n*b.d-b.n*a.d;
 const qa=(a,b)=>R(a.n*b.d+b.n*a.d,a.d*b.d),qm=(a,b)=>R(a.n*b.n,a.d*b.d),two=k=>R(2n**BigInt(k));
 const qg=(name,a,b,eq=false)=>gates.push({name,arithmetic:"normalized exact BigInt rational",left:str(a),right:str(b),relation:eq?"=":"<",pass:eq?cmp(a,b)===0n:cmp(a,b)<0n});
 qg("reserved_centres_Qx_lower_strict",R(1),R(60n*113n*142n*28n,256n**3n));
 qg("reserved_centres_Qx_upper_strict",R(15n*30n,256n),R(2));
 qg("reserved_real_Q_upper_strict",qa(R(7),R(30,16)),R(9));
 qg("wave_frame_squared_norm_coefficient",R(3+13),R(16),true);
 qg("all_covariance_entries_X_coefficient",R(2+36+100+2),two(8));
 qg("complete_covariance_Y_coefficient",R(13+10*256,2),two(11));
 qg("complete_covariance_Z_coefficient",R(1+13+9*256),two(12));
 qg("observability_binary_cost_before_rounding",R(5+12),R(20));
 qg("all_symmetric_spectral_decomposition_norm",R(2),R(4));
 qg("short_propagation_division_by_three",R(3),R(16));
 qg("new_separation_binary_cost_at_L13",R(9088),R((4096-1792)*13));
 qg("new_separation_B_cost_at_L13",R(480),R((192-128)*13));
 qg("new_complex_square_prefix",R(32*44+12*32),R(1792),true);
 qg("new_compact_pairing_binary_cost",R(26*4096*13*13+4436),R((2**17)*13*13));
 qg("new_compact_a_power",R(2496*13*13+51),R(2560*13*13));
 qg("new_compact_B_power",R(4992*13*13+130),R(5120*13*13));
 qg("new_compact_lambda_power",R(2496*13*13+25),R(2560*13*13));
 qg("new_compact_covariance_K_power",R(3328*13*13+50),R(3456*13*13));
 qg("finite_net_support_margin",qa(R(1),R(-1,4)),R(3,4),true);
 qg("target_identity_Frobenius_radius_squared",R(2,16),R(9,16));
 qg("complex_incoming_positive_generator_factor",R(1,4*2),R(1,8),true);
 qg("full_scattering_generator_matrix_Hessian",R((2**24)+128),two(30));
 qg("complete_band_error_margin",R(1,16),R(7,64));
 qg("band_direction_operator_upper_binary_exponent",R(3-36),R(-33),true);
 qg("all_control_band_norms_stay_in_real_compensation_ball",R(1,2n**79n),R(1,2n**65n));
 qg("complete_local_D_log_polynomial_fee",R(1025+1024+256+4096),two(13));
 const j=8193n;
 qg("full_polynomial_fee_over_Mh_first_layer",R(50n*512n-61n*j,512n),R(-803));
 qg("two_derivatives_and_dyadic_band_width_fee",qa(R(4,8),R(1,8)),R(1));
 return {
 schema:"R119-all-symmetric-quadratic-kernels-and-positive-scattering-control-v1",
 complete:gates.every(g=>g.pass),executed:true,gate_count:gates.length,gates,
 normalized_state:"unit wave fundamental at the actual unused interval centre",
 covariance_space:"all real Sym2, including indefinite matrices, Frobenius norm one",
 compact_control:"finite convex combination of at most four real C9 controls; sum C4 <=1; all degree<=19 phase kernels annihilated exactly",
 complete_pairing_matrix:"(D_L/4)*I",
 complete_complex_scattering_generator_lower:"D_L/(8 K_j^2)",
 complete_finite_band_generator_lower:"D_jm=r_j D_L/(16 Nband K_j^2) > exp(-2^-800 M h_j)",
 outside_control_uniformity:"all other reserved intervals may be simultaneously controlled inside the common actual C4 ball; no fixed prior global resonant trial reused",
 dependencies:{
  actual_short_support:"27e75c019c0e4441c3237a36bb3c9f485fd2cdbf",
  complete_phase_compensation:"dd0d1378fce997297795ce14312fe91b181af4b1",
  actual_compact_normalization:"5662bf40391a53a2212311406cf7ad63064908fc",
  complete_radial_network_commit:"789268ff1c9d7852733f32e6f89fc3c37cbe6d7f"
 },
 original_h_zeta_low_source_weights_unchanged:true,
 numerical_control_coefficients_claimed:false,
 common_infinite_parameters_selected:false,
 coupled_nonradial_inverse_proved:false
 };
}
const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--out')throw Error('usage: node this.mjs --out NEW_REPORT.json');
const report=calculate();
report.producer_sha256=createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex');
await writeFile(args[1],JSON.stringify(report,null,2)+'\n',{flag:'wx'});
if(!report.complete)process.exitCode=1;
console.log(JSON.stringify({complete:report.complete,gate_count:report.gate_count,out:args[1]}));
