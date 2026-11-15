#!/usr/bin/env node
"use strict";
// R692. Run only in the repository's public Actions workflow.
// No input data files, network or third-party packages.
// Ephemeral certificate goes to stdout, SHA256 to stderr. Do not commit it.
const crypto=require("crypto");
const K=(a,b=0)=>[BigInt(a),BigInt(b)],ka=(x,y)=>K(x[0]+y[0],x[1]+y[1]),
kn=x=>K(-x[0],-x[1]),ks=(x,y)=>ka(x,kn(y)),
km=(x,y)=>K(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1]),
eq=(x,y)=>x[0]===y[0]&&x[1]===y[1],
norm=x=>x[0]*x[0]-x[0]*x[1]+x[1]*x[1];
const checks=[];function check(name,ok){if(!ok)throw new Error(name);checks.push(name);}
const R=[[1n,0n,0n],[0n,0n,1n],[0n,1n,0n]],
T=[[0n,1n,-1n],[1n,0n,-1n],[0n,0n,-1n]],
I=[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]];
const mm=(a,b)=>a.map(row=>b[0].map((_,j)=>row.reduce((s,x,k)=>s+x*b[k][j],0n))),
mv=(a,v)=>a.map(row=>row.reduce((s,x,k)=>s+x*v[k],0n)),
rowm=(v,a)=>a[0].map((_,j)=>v.reduce((s,x,i)=>s+x*a[i][j],0n)),
same=(a,b)=>JSON.stringify(a,(_,x)=>typeof x==="bigint"?x.toString():x)===JSON.stringify(b,(_,x)=>typeof x==="bigint"?x.toString():x);
check("R_square",same(mm(R,R),I));
check("K_square",same(mm(T,T),I));
const TR=mm(T,R),TR2=mm(TR,TR);
check("KR_fourth",same(mm(TR2,TR2),I));
const states=[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n],[-1n,-1n,-1n]];
for(let i=0;i<4;i++)for(const [tag,M] of [["R",R],["K",T]])
 check("state_orbit_"+tag+"_"+i,states.some(x=>same(x,mv(M,states[i]))));
const trow=[1n,1n,-1n],nrow=[0n,1n,-1n];
check("T_row_fixed_K",same(rowm(trow,T),trow));
check("new_reference_row_negative_R",same(rowm(nrow,R),nrow.map(x=>-x)));
check("new_reference_K_row",same(rowm(nrow,T),[1n,0n,0n]));
for(let i=0;i<4;i++){const v=states[i].reduce((s,x,j)=>s+x*trow[j],0n);check("word_T_coefficient_unit_sign_"+i,v===1n||v===-1n);}
const labels=[];for(let m=0;m<4;m++)for(let n=0;n<4;n++)labels.push([m,n]);
const e0=labels.map(([m,n])=>m===0&&n===0?4n:0n),
e1=labels.map(([m,n])=>m%2===0&&n%2===0?-1n:1n),
e2=labels.map(()=>-1n),
diag=labels.map(([m,n])=>m%2===0&&n%2===0?1n:-1n);
const bd=v=>v.map((x,i)=>x*diag[i]);
check("full16_B2_e0",same(bd(e0),e0));
check("full16_B2_e1",same(bd(e1),e2));
check("full16_B2_e2",same(bd(e2),e1));
const echeck=(v,w)=>v.every((x,i)=>x===w[i]);
const gi=(a,b=0)=>[BigInt(a),BigInt(b)],
ga=(x,y)=>gi(x[0]+y[0],x[1]+y[1]),
gm=(x,y)=>gi(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]),
ipow=n=>{n=((n%4)+4)%4;return [gi(1),gi(0,1),gi(-1),gi(0,-1)][n];};
function k16(v){
 return labels.map(([rm,rn])=>{
  let z=gi(0);
  labels.forEach(([tm,tn],j)=>{
   const um=(rm+tm)%4,un=(rn+tn)%4;
   const ar=(um%2===0&&un%2===0)?-1n:1n;
   const det=tm*rn-tn*rm;
   z=ga(z,gm(gi(ar*v[j]),ipow(-det)));
  });
  check("K16_real_integral_"+rm+"_"+rn+"_"+v[0],z[1]===0n&&z[0]%4n===0n);
  return z[0]/4n;
 });
}
check("full16_K_e0",echeck(k16(e0),e1));
check("full16_K_e1",echeck(k16(e1),e0));
check("full16_K_e2",echeck(k16(e2),e0.map((x,i)=>-x-e1[i]-e2[i])));
for(const [m,n] of labels){
 const j=((4-m)%4)*4+(4-n)%4,ii=m*4+n;
 check("minus_label_e1_"+ii,e1[ii]===e1[j]);
 check("minus_label_e2_"+ii,e2[ii]===e2[j]);
}
check("canonical_period_phase_even",18n%2n===0n);
const aa=K(17,-3),bb=K(20,3);
check("bY_numerator_conjugate_norm",eq(km(aa,bb),K(349)));
check("plane_inverse_349_plus263",eq(ka(km(aa,bb),K(263)),K(612)));
const rows={Y:[K(1),K(0)],Z:[K(0),K(1)],W17:[bb,K(17)],V17:[K(263),km(K(-17),aa)]};
const det=(v,w)=>ks(km(v[0],w[1]),km(v[1],w[0]));
const expected=[
 ["Y","Z",K(1)],
 ["Y","W17",K(17)],
 ["Y","V17",km(K(-17),aa)],
 ["Z","W17",kn(bb)],
 ["Z","V17",K(-263)],
 ["W17","V17",K(-10404)]
];
const determinants={};
for(const [a,b,d] of expected){const got=det(rows[a],rows[b]);check("projective_lines_"+a+"_"+b,eq(got,d));determinants[a+"_"+b]={value:got,norm:norm(got)};}
const raw={
 result:"R692 same-source four-axis three-state identities",
 scope:"Exact original finite labels and algebraic geometry; no claim of central nonvanishing.",
 parameters:{ordinary_ray:"R686 existing ray",N:"a positive multiple of four",extra_good_primes:[2,3,17,263,349]},
 source_column_matrices:{R,K:T},
 source_orbit:states,
 W_marginal_row:trow,
 new_reference_row:nrow,
 full16:{labels,e0,e1,e2,B2_diagonal:diag},
 projective_rows:rows,determinants,
 physical_maps:{Y:"R_Y P_Y(kappa)",Z:"R_Y P_Z(kappa)",W:"P_W(kappa)",V:"P_V(kappa)"},
 retained:[
  "All four original common companions.",
  "Y reflection inside every mixed W/V cut.",
  "q_sharp is unchanged; q_cd is not assumed to have W marginal T.",
  "The full first-axis CM fibre family and its moving unit cuts.",
  "Mass column uses transposes of the displayed source matrices.",
  "No inverse on all continuous tests is claimed."
 ],
 checks,number_of_checks:checks.length
};
const output=JSON.stringify(raw,(_,x)=>typeof x==="bigint"?x.toString():x,2)+"\n";
process.stdout.write(output);
process.stderr.write("SHA256 "+crypto.createHash("sha256").update(output).digest("hex")+"\n");
