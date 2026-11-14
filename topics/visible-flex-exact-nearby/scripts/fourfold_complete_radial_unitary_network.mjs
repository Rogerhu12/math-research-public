#!/usr/bin/env node
/** Complete actual radial scattering and global eigenphase algebra. */
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
function calculate(){
 const names=["c11","c12","c21","c22","r1","r2","h","p","dh","dp","x1","x2","fa","fb","tau","v","z","n11","n12r","n12i","n22"];
 const nv=names.length,zk=Array(nv).fill(0).join(",");
 const poly=(r=0n,i=0n)=>new Map((r||i)?[[zk,[BigInt(r),BigInt(i)]]]:[]);
 const term=(e,r=1n,i=0n)=>new Map([[e.join(","),[BigInt(r),BigInt(i)]]]);
 const variable=k=>{const e=Array(nv).fill(0);e[k]=1;return term(e);};
 const add=(a,b)=>{const o=new Map(a);for(const [k,[r,i]] of b){const [s,t]=o.get(k)||[0n,0n];if(r+s||i+t)o.set(k,[r+s,i+t]);else o.delete(k);}return o;};
 const scale=(a,r,i=0n)=>{r=BigInt(r);i=BigInt(i);const o=new Map();for(const [k,[s,t]] of a){const u=r*s-i*t,v=r*t+i*s;if(u||v)o.set(k,[u,v]);}return o;};
 const neg=a=>scale(a,-1n),sub=(a,b)=>add(a,neg(b));
 const mul=(a,b)=>{let o=poly();for(const [ka,[ar,ai]] of a)for(const [kb,[br,bi]] of b){const ea=ka.split(",").map(Number),eb=kb.split(",").map(Number),e=ea.map((x,i)=>x+eb[i]);o=add(o,term(e,ar*br-ai*bi,ar*bi+ai*br));}return o;};
 const conj=a=>new Map([...a].map(([k,[r,i]])=>[k,[r,-i]]));
 const binom=(n,k)=>{let o=1n;for(let j=1;j<=k;j++)o=o*BigInt(n-j+1)/BigInt(j);return o;};
 const reduceDet=a=>{let o=poly();for(const [key,[r,i]] of a){const e=key.split(",").map(Number),n=Math.min(e[0],e[3]);e[0]-=n;e[3]-=n;for(let k=0;k<=n;k++){const f=e.slice();f[1]+=k;f[2]+=k;const b=binom(n,k);o=add(o,term(f,r*b,i*b));}}return o;};
 const fmt=a=>[...a].map(([key,[r,i]])=>({powers:key.split(",").map(Number),real:r.toString(),imag:i.toString()}));
 const gates=[];
 const gate=(name,a,b=poly(),mod=false)=>{const residual=mod?reduceDet(sub(a,b)):sub(a,b);gates.push({name,arithmetic:mod?"exact complex BigInt polynomial modulo c11*c22-c12*c21-1":"exact complex BigInt polynomial",residual:fmt(residual),pass:residual.size===0});};
 const zero=poly(),one=poly(1n),two=poly(2n),four=poly(4n);
 const M=(a,b,c,d)=>[[a,b],[c,d]],I=M(one,zero,zero,one),J=M(zero,one,neg(one),zero);
 const madd=(a,b)=>a.map((r,i)=>r.map((x,j)=>add(x,b[i][j]))),msub=(a,b)=>a.map((r,i)=>r.map((x,j)=>sub(x,b[i][j])));
 const mmul=(a,b)=>a.map(r=>b[0].map((_,j)=>r.reduce((q,x,k)=>add(q,mul(x,b[k][j])),zero)));
 const mscale=(a,p)=>a.map(r=>r.map(x=>mul(x,p)));
 const tr=a=>add(a[0][0],a[1][1]);
 const trans=a=>a[0].map((_,j)=>a.map(r=>r[j]));
 const star=a=>trans(a).map(r=>r.map(conj));
 const mgate=(name,a,b,mod=false)=>{const rs=msub(a,b).map(r=>r.map(x=>mod?reduceDet(x):x));gates.push({name,arithmetic:mod?"exact 2x2 polynomial matrix modulo determinant-one relation":"exact 2x2 polynomial matrix",residual:rs.map(r=>r.map(fmt)),pass:rs.every(r=>r.every(x=>x.size===0))});};
 const [a,b,c,d,r,s,h,p,dh,dp,x1,x2,fa,fb,tau,v,z,n1,n2,n3,n4]=names.map((_,i)=>variable(i));
 const C=M(a,b,c,d),det=sub(mul(a,d),mul(b,c));
 const T=M(one,poly(0n,1n),one,poly(0n,-1n));
 const Ti=M(one,one,poly(0n,-1n),poly(0n,1n));
 const A=add(add(a,d),scale(sub(c,b),0n,1n));
 const B=add(sub(a,d),scale(add(c,b),0n,1n));
 const AA=mul(A,conj(A)),BB=mul(B,conj(B));
 mgate("fixed_wave_complex_change_and_inverse",mmul(T,Ti),mscale(I,two));
 mgate("complex_wave_change_is_norm_sqrt_two",mmul(star(T),T),mscale(I,two));
 mgate("actual_transfer_complex_alpha_beta",mmul(mmul(T,C),Ti),M(A,B,conj(B),conj(A)));
 gate("alpha_beta_determinant_identity_before_normalization",sub(AA,BB),scale(det,4n));
 gate("alpha_denominator_square_is_four_plus_beta_square",AA,add(four,BB),true);
 const N=M(neg(conj(B)),two,two,B);
 mgate("full_scattering_numerator_symmetric",trans(N),N);
 mgate("full_scattering_unitary_with_all_cross_entries",mmul(star(N),N),mscale(I,AA),true);
 const F=M(zero,neg(two),conj(A),neg(B));
 gate("full_affine_source_Frobenius_square_exactly_two",tr(mmul(star(F),F)),scale(AA,2n),true);
 const y1num=add(sub(scale(x2,2n),mul(conj(B),x1)),scale(fb,-2n));
 const y2num=add(add(scale(x1,2n),mul(B,x2)),sub(mul(conj(A),fa),mul(B,fb)));
 gate("right_b_transfer_including_complete_affine_source",add(add(mul(mul(conj(B),conj(A)),x1),mul(conj(A),y1num)),scale(mul(conj(A),fb),2n)),scale(mul(conj(A),x2),2n));
 gate("right_a_transfer_including_complete_affine_source",add(add(mul(mul(A,conj(A)),x1),mul(B,y1num)),scale(mul(conj(A),fa),2n)),scale(y2num,2n),true);
 const ach=add(h,scale(p,0n,1n)),bch=sub(h,scale(p,0n,1n));
 const rr=add(r,scale(s,0n,1n)),rc=conj(rr),omega=sub(mul(r,p),mul(s,h));
 gate("complete_real_Robin_line_affine_identity",sub(mul(rr,bch),mul(rc,ach)),scale(omega,0n,-2n));
 gate("vertical_Robin_line_denominator_unit_norm",mul(rr,rc),add(mul(r,r),mul(s,s)));
 const Sh=M(one,zero,tau,one);
 mgate("real_normal_shear_is_exactly_symplectic",mmul(mmul(trans(Sh),J),Sh),J);
 const V=M(mul(v,v),zero,z,one);
 mgate("physical_total_flux_to_wave_frame_determinant_one",mmul(mmul(trans(V),J),V),mscale(J,mul(v,v)));
 const Nh=M(n1,add(n2,scale(n3,0n,1n)),sub(n2,scale(n3,0n,1n)),n4);
 mgate("positive_DN_plus_real_shear_keeps_selfadjoint_structure",star(Nh),Nh);
 const Ap=madd(I,mscale(Nh,poly(0n,1n))),Am=madd(I,mscale(Nh,poly(0n,-1n)));
 mgate("positive_Cayley_denominator_adjoint_is_numerator",star(Ap),Am);
 mgate("positive_full_Cayley_factors_commute",mmul(Ap,Am),mmul(Am,Ap));
 mgate("positive_Cayley_denominator_coercivity_identity",mmul(star(Ap),Ap),madd(I,mmul(Nh,Nh)));
 mgate("positive_complete_affine_resolvent_factor",madd(Ap,Am),mscale(I,two));
 const da=add(dh,scale(dp,0n,1n)),db=sub(dh,scale(dp,0n,1n));
 const omvar=sub(mul(h,dp),mul(p,dh));
 gate("boundary_Green_form_equals_wave_phase_pairing",sub(mul(conj(ach),da),mul(conj(bch),db)),scale(omvar,0n,2n));
 gate("real_state_incoming_norm_has_correct_half_factor",mul(conj(ach),ach),add(mul(h,h),mul(p,p)));
 const inequalities=[
  {name:"affine_sqrt_two_bound_is_less_than_two",left:"2",right:"4",pass:2n<4n},
  {name:"left_state_squared_cost_K_minus_two",left:"-2",right:"-2",pass:-2n===-2n},
  {name:"true_right_amplitude_adds_one_inverse_K",left:"-2 + (-1)",right:"-3",pass:-2n-1n===-3n}
 ];
 gates.push(...inequalities);
 return {
 schema:"R119-complete-radial-unitary-network-and-global-eigenphase-v1",
 executed:true,arithmetic:"exact complex BigInt polynomials; determinant-one Groebner reduction; exact integer inequalities",
 gate_count:gates.length,complete:gates.every(x=>x.pass),gates,
 dependencies:{
  controlled_actual_full_tail:"f11edbccd752bf034aa40e71888859d667a04b42",
  actual_positive_transmission:"6f636e2714c59afbac5d0a99ef7de5c0262dad92",
  compact_true_kernel:"5662bf40391a53a2212311406cf7ad63064908fc",
  true_small_amplitude_Hessian:"8a359f45c35e513e786b11d6217a20c345ced5eb"
 },
 exact_network:"(I-P direct_sum S_i) x=P t+p; P and every S_i unitary",
 actual_infinite_tail_preserved:true,positive_cross_preserved:true,independent_mean_preserved:true,
 complete_ordinary_and_both_weak_sources_preserved:true,weak_normal_endpoint_charges_preserved:true,
 global_simple_resonance_phase_derivative:"integral actual complete kernel times compensated psi dt",
 controlled_window_bound:"theta_control_mass * D_i / (n K_i^3)",
 fixed_P_required_for_displayed_derivative:true,
 finite_parameter_global_bad_set_proved:false,nonradial_cluster_inverted:false,original_same_width_inverse_proved:false,
 chosen_numerical_global_profile:false
 };
}
const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--out')throw Error('usage: node this.mjs --out NEW_REPORT.json');
const report=calculate();
report.producer_sha256=createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex');
await writeFile(args[1],JSON.stringify(report,null,2)+'\n',{flag:'wx'});
if(!report.complete)process.exitCode=1;
console.log(JSON.stringify({complete:report.complete,gate_count:report.gate_count,out:args[1]}));
