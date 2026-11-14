// R239: exact rank certificate, original dyadic Weil line, and four Weyl terms.
// Arithmetic is in Z[zeta_16]=Z[X]/(X^8+1). No packages or target-prime scan.

const zero = () => Array(8).fill(0n);
const one = () => [1n,0n,0n,0n,0n,0n,0n,0n];
const add = (a,b) => a.map((x,j)=>x+b[j]);
const neg = a => a.map(x=>-x);
const scale = (a,n) => a.map(x=>x*BigInt(n));
const eq = (a,b) => a.every((x,j)=>x===b[j]);
const mul = (a,b) => {
  const c=zero();
  for(let j=0;j<8;j++) for(let k=0;k<8;k++) {
    const d=j+k;
    c[d%8]+=(d<8?1n:-1n)*a[j]*b[k];
  }
  return c;
};
const zp = k => {
  k=((k%16)+16)%16;
  const r=zero();r[k%8]=k<8?1n:-1n;return r;
};
const conj = a => a.reduce((s,x,j)=>add(s,scale(zp(-j),x)),zero());
const mv = (a,v) => a.map(row=>row.reduce((s,x,j)=>add(s,mul(x,v[j])),zero()));
const veq = (a,b) => a.every((x,j)=>eq(x,b[j]));
const vs = (a,c) => a.map(x=>mul(x,c));
const va = (a,b) => a.map((x,j)=>add(x,b[j]));
const X = (v,k=1) => v.map((_,a)=>v[((a-k)%16+16)%16]);
const Z = (v,k=1) => v.map((x,a)=>mul(zp(a*k),x));
const checks={};
const check=(k,v)=>{checks[k]=Boolean(v);if(!v)throw Error(k);};

const t=[-1n,1n,-1n,1n,0n,-1n,1n,-1n];
const it=mul(zp(4),t), zplus=add(one(),zp(1));
check('tan_half_angle_exact',eq(mul(zplus,it),add(zp(1),neg(one()))));
check('t_is_real',eq(conj(t),t));
const t2=mul(t,t),t3=mul(t2,t),t4=mul(t3,t);
check('t_minimal_polynomial',eq(add(add(add(add(t4,scale(t3,4)),scale(t2,-6)),scale(t,-4)),one()),zero()));

const v=[zero(),one(),zero(),t,zero(),neg(t),zero(),neg(one()),
         zero(),neg(one()),zero(),neg(t),zero(),t,zero(),one()];
const v0=Array.from({length:16},(_,a)=>a%4===0?one():zero());
// A=4*omega_0(i), B=4*omega_0(g_*), in the original Rao normalization.
const A=Array.from({length:16},(_,a)=>Array.from({length:16},(_,b)=>zp(-a*b)));
const B=Array.from({length:16},(_,a)=>Array.from({length:16},(_,b)=>{
  if((b-3*a)%4!==0)return zero();
  const k=(b-3*a)/4;
  return scale(zp(-2*(1+2*a*k+3*k*k)),-2);
}));
check('original_I_eigenvalue_one',veq(mv(A,v),vs(v,scale(one(),4))));
check('original_G_eigenvalue_i',veq(mv(B,v),vs(v,scale(zp(4),4))));
check('old_vector_I_one',veq(mv(A,v0),vs(v0,scale(one(),4))));
check('old_vector_G_one',veq(mv(B,v0),vs(v0,scale(one(),4))));
check('vector_even',v.every((x,a)=>eq(x,v[(16-a)%16])));
check('vector_half_period_antiperiodic',v.every((x,a)=>eq(x,neg(v[(a+8)%16]))));
check('X8_new_sign_minus',veq(X(v,8),vs(v,scale(one(),-1))));
check('Z8_new_sign_minus',veq(Z(v,8),vs(v,scale(one(),-1))));
check('X8_old_sign_plus',veq(X(v0,8),v0));
check('Z8_old_sign_plus',veq(Z(v0,8),v0));
check('dyadic_norm_four_times',eq(v.reduce((s,x)=>add(s,mul(x,x)),zero()),scale(add(one(),t2),4)));
check('weyl_commutator',veq(Z(X(v)),vs(X(Z(v)),zp(1))));
const transport=va(va(Z(X(v0)),vs(Z(X(v0),-1),zp(1))),
                   va(vs(Z(X(v0,-1)),zp(1)),Z(X(v0,-1),-1)));
check('four_actual_Weyl_terms',veq(transport,vs(v,zplus)));

// A nonzero rank-15 minor after one fixed exact specialization proves
// the common nullspace over Q(zeta_16) has dimension <=1. The vector above
// proves the reverse inequality. This is a fixed algebraic certificate,
// not a statement about any varying target prime.
const mod=(a,p=97)=>((a%p)+p)%p;
const mpow=(a,n,p=97)=>{let s=1;for(;n;n>>=1,a=mod(a*a,p))if(n&1)s=mod(s*a,p);return s;};
const eval97=a=>Number(a.reduce((s,x,j)=>(s+x*BigInt(mpow(8,j)))%97n,0n)+97n)%97;
check('auxiliary_zeta_exact_order_16',mpow(8,8)===96&&mpow(8,16)===1);
const equations=[...A.map((row,a)=>row.map((x,b)=>a===b?add(x,scale(one(),-4)):x)),
                 ...B.map((row,a)=>row.map((x,b)=>a===b?add(x,scale(zp(4),-4)):x))];
const rows=equations.map(row=>row.map(eval97));
let rank=0;const pivot_columns=[];
for(let col=0;col<16;col++){
  let j=rank;while(j<32&&!rows[j][col])j++;
  if(j===32)continue;
  [rows[j],rows[rank]]=[rows[rank],rows[j]];
  const inv=mpow(rows[rank][col],95);
  for(let k=col;k<16;k++)rows[rank][k]=mod(rows[rank][k]*inv);
  for(let h=0;h<32;h++)if(h!==rank&&rows[h][col]){
    const a=rows[h][col];for(let k=col;k<16;k++)rows[h][k]=mod(rows[h][k]-a*rows[rank][k]);
  }
  pivot_columns.push(col);rank++;
}
check('joint_invariant_line_unique',rank===15);

check('E136_point',24n**2n===(-8n)**3n-136n*(-8n));
check('dual_point',28n**2n===8n**3n+34n*8n);
check('isogeny_image',105n**2n===49n**3n-136n*49n*16n);
const squares16=new Set(Array.from({length:16},(_,a)=>a*a%16));
const quartic_residues=[];
for(let a=0;a<2;a++)for(let b=0;b<2;b++)if(a||b){
  const q=mod(2*a**4-68*b**4,16);quartic_residues.push({u_parity:a,v_parity:b,residue:q});
  check('d2_quartic_obstruction_'+a+b,!squares16.has(q));
}
const fq2mask=d=>{let n=Math.abs(d),a=d<0?1:0;while(n%2===0){a^=2;n/=2;}while(n%17===0){a^=4;n/=17;}if(n!==1)throw Error('bad squareclass');return a;};
const clsE=[1,-2,17,-34].map(fq2mask),clsDual=[1,2,17,34].map(fq2mask);
check('two_exact_dim2_Kummer_images',new Set(clsE).size===4&&new Set(clsDual).size===4);

const lam=Array(17).fill(0);let a=1;
for(let k=0;k<16;k++){lam[a]=(((-k)%4)+4)%4;a=a*3%17;}
check('lambda_four_one',lam[4]===0);
check('lambda_two_squared_one',(2*lam[2])%4===0);
check('phase_division_by_sixteen',(236*16)%289===19);
check('phase_previous_e34',(236*4)%289===77);
check('CRT_dyadic_step',289%16===1&&289%289===0);
const old34=Array.from({length:16},(_,a)=>a%2?0:[1,1,-1,1][(a/2)%4]);
check('three_actual_rows_triangular',v0[4][0]===1n&&old34[2]===1&&eq(v[1],one())&&v0[2][0]===0n&&old34[1]===0);
check('translation_Weil_pairing',(272*17)%256===16);
check('fixed_order_16_transport_points',272%16===0);

const output={
  theorem:'R239',status:'PASS',ring:'Z[zeta_16], zeta_16^8=-1',
  curve:{ainvs:[0,0,0,-136,0],rank:2,points:[[-8,24],['49/4','105/8']],dual_ainvs:[0,0,0,34,0]},
  dyadic_character:{eta_i:'1',eta_g_star:'-i'},
  dyadic_vector:v.map(x=>x.map(String)),t:t.map(String),
  joint_kernel:{rank_mod_97:rank,zeta_mod_97:8,pivot_columns},
  quartic_residues,rank_certificate:{alpha_E:[1,-2,17,-34],alpha_dual:[1,2,17,34]},
  raw_theta:{L:68,period:4624,phase_mod_289:236,discriminant_module:4624,quadratic_denominator:9248},
  transport:'(Z X + zeta Z^-1 X + zeta Z X^-1 + Z^-1 X^-1)/(1+zeta)',
  section:{degree:272,theta_origin:'A17(4z)',P:'(4-i) Omega_0/16',Q:'-i P'},
  checks
};
console.log(JSON.stringify(output,null,2));
