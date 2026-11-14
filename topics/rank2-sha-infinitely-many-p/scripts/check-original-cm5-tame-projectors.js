// Exact R231 norm-five CM trace certificate. No numerical approximation or target primes.

const rgcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a;};
const R=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=rgcd(a,b);return[a/g,b/g];};
const rr=s=>{if(Array.isArray(s))return s;const[a,b="1"]=String(s).split("/");return R(a,b);};
const ra=(x,y)=>R(x[0]*y[1]+y[0]*x[1],x[1]*y[1]);
const rn=x=>[-x[0],x[1]],rs=(x,y)=>ra(x,rn(y));
const rm=(x,y)=>R(x[0]*y[0],x[1]*y[1]),rd=(x,y)=>R(x[0]*y[1],x[1]*y[0]);
const rstr=x=>x[1]===1n?String(x[0]):x[0]+"/"+x[1];
const rsolve=(A,b)=>{
 A=A.map((r,j)=>[...r.map(rr),rr(b[j])]);const cols=A[0].length-1;let row=0;const piv=[];
 for(let k=0;k<cols;k++){let j=row;while(j<A.length&&!A[j][k][0])j++;if(j===A.length)continue;[A[j],A[row]]=[A[row],A[j]];
 const v=A[row][k];A[row]=A[row].map(x=>rd(x,v));
 for(let l=0;l<A.length;l++)if(l!==row&&A[l][k][0]){const u=A[l][k];A[l]=A[l].map((x,t)=>rs(x,rm(u,A[row][t])));}
 piv.push(k);row++;}
 for(let j=row;j<A.length;j++)if(A[j][cols][0])throw Error("inconsistent");
 const x=Array.from({length:cols},()=>R(0));for(let j=0;j<row;j++)x[piv[j]]=A[j][cols];
 return{x,rank:row,piv,A};
};

const CI=()=>[R(0),R(1)], C=(a=0,b=0)=>[rr(a),rr(b)];
const ca=(x,y)=>[ra(x[0],y[0]),ra(x[1],y[1])],cn=x=>[rn(x[0]),rn(x[1])],cs=(x,y)=>ca(x,cn(y));
const cm=(x,y)=>[rs(rm(x[0],y[0]),rm(x[1],y[1])),ra(rm(x[0],y[1]),rm(x[1],y[0]))];
const cd=(x,y)=>{const n=ra(rm(y[0],y[0]),rm(y[1],y[1]));const z=cm(x,[y[0],rn(y[1])]);return[rd(z[0],n),rd(z[1],n)];};
const cp=(x,n)=>{let r=C(1);for(let j=0;j<n;j++)r=cm(r,x);return r;},cz=x=>!x[0][0]&&!x[1][0];
const cscale=(x,n)=>cm(x,C(n)),ceq=(x,y)=>cz(cs(x,y)),cstr=x=>[rstr(x[0]),rstr(x[1])],cdes=x=>[rr(x[0]),rr(x[1])];
const clean=p=>{while(p.length>1&&cz(p[p.length-1]))p.pop();return p;};
const pa=(p,q)=>clean(Array.from({length:Math.max(p.length,q.length)},(_,j)=>ca(p[j]||C(),q[j]||C())));
const pn=p=>p.map(cn),ps=(p,q)=>pa(p,pn(q)),pscale=(p,c)=>clean(p.map(x=>cm(x,c)));
const pm=(p,q)=>{const r=Array.from({length:p.length+q.length-1},()=>C());for(let j=0;j<p.length;j++)for(let k=0;k<q.length;k++)r[j+k]=ca(r[j+k],cm(p[j],q[k]));return clean(r);};
const pp=(p,n)=>{let r=[C(1)];for(let j=0;j<n;j++)r=pm(r,p);return r;};
const peval=(p,x)=>{let r=C();for(let j=p.length-1;j>=0;j--)r=ca(cm(r,x),p[j]);return r;};
const pdiv=(p,q)=>{p=p.map(x=>[...x]);const r=Array.from({length:Math.max(1,p.length-q.length+1)},()=>C());while(p.length>=q.length&&!cz(p[p.length-1])){const j=p.length-q.length,v=cd(p[p.length-1],q[q.length-1]);r[j]=v;for(let k=0;k<q.length;k++)p[j+k]=cs(p[j+k],cm(v,q[k]));clean(p);}return{q:clean(r),r:clean(p)};};
const mod=(p,f)=>pdiv(p,f).r;
const modpow=(p,n,f)=>{let r=[C(1)];while(n>0){if(n%2)r=mod(pm(r,p),f);p=mod(pm(p,p),f);n=Math.floor(n/2);}return r;};
const PI=C(2,1),PIB=C(2,-1),B=C(1,-2),BB=C(1,2),I=CI();
const N=pm([C(),C(1)],pp([PI,cn(I)],4)),Q=pp([C(1),cn(B)],4);
const inverseLinear=(f)=>{
 const s0=cd(C(1),B),v=peval(f,s0),fp=f.map(x=>[...x]);fp[0]=cs(fp[0],v);
 const div=pdiv(fp,[cn(s0),C(1)]);if(div.r.some(x=>!cz(x)))throw Error("linear division");
 return pscale(div.q,cd(C(1),cm(B,v)));
};
const traceP=(p,f)=>{
 const deg=f.length-1,lead=f[deg],mon=f.map(x=>cd(x,lead)),tr=[C(deg)];
 for(let k=1;k<deg;k++){let s=cscale(mon[deg-k],k);for(let j=1;j<k;j++)s=ca(s,cm(mon[deg-j],tr[k-j]));tr[k]=cn(s);}
 p=mod(p,f);let out=C();for(let k=0;k<p.length;k++)out=ca(out,cm(p[k],tr[k]));return out;
};
const traceBasisAt=t=>{
 const f=ps(N,pscale(Q,C(t))),inv=modpow(inverseLinear(f),17,f),out=[];
 for(let j=0;j<5;j++){
  let num=pm(pp([C(1),cn(BB)],17-4*j),pp([PIB,I],4*j));num=[...Array.from({length:j},()=>C()),...num];
  out.push(traceP(mod(pm(mod(num,f),inv),f),f));
 }
 return out;
};
const checks={},must=(b,label)=>{if(!b)throw Error("FAIL "+label);checks[label]=true;};
const vals=[];for(let t=0;t<5;t++){
 const f=ps(N,pscale(Q,C(t))),inverse=inverseLinear(f),product=mod(pm([C(1),cn(B)],inverse),f);
 must(product.length===1&&ceq(product[0],C(1)),"linear_inverse_at_"+t);
 vals.push(traceBasisAt(t));
}
must(ceq(vals[0][0],[R(127,128),R(1,128)]),"direct_trace_at_zero");
// Phi(X,0)=X(X-eta)^4: finite-flat trace keeps multiplicity four.
const directRow=Array.from({length:5},(_,j)=>ca(j===0?C(1):C(),cm([R(-1,128),R(1,128)],cp(B,j))));
must(vals[0].every((x,j)=>ceq(x,directRow[j])),"independent_full_ramified_fiber_row");
const V=Array.from({length:5},(_,t)=>Array.from({length:5},(_,j)=>String(BigInt(t)**BigInt(j))));
const matrix=Array.from({length:5},()=>[]);
for(let j=0;j<5;j++){
 const real=rsolve(V,vals.map(row=>rstr(row[j][0]))).x,imag=rsolve(V,vals.map(row=>rstr(row[j][1]))).x;
 for(let k=0;k<5;k++)matrix[k].push([rstr(real[k]),rstr(imag[k])]);
}
const R128=[[127,1,7,9,-17],[-1156,-224,-108,-56,108],[1326,54,70,-66,-1314],[884,-32,-68,-40,580],[-221,-23,-29,-7,-61]];
const I128=[[1,3,1,-13,-31],[102,38,-114,-98,-586],[2448,-228,40,132,768],[-2958,114,106,90,-670],[-153,-39,-17,-31,87]];
must(matrix.every((row,j)=>row.every((x,k)=>ceq(cdes(x),[R(R128[j][k],128),R(I128[j][k],128)]))),"all_exact_trace_matrix_entries");
const act=v=>matrix.map(row=>row.reduce((s,x,j)=>ca(s,cm(cdes(x),v[j])),C()));
const eigs={
 CMbeta:{v:[[1,0],[12,-20],[-10,28],[-20,-12],[1,4]].map(([a,b])=>C(a,b)),e:C(-1,2)},
 CMbetabar:{v:[[1,0],[12,20],[-10,-28],[-20,12],[1,-4]].map(([a,b])=>C(a,b)),e:C(-1,2)},
 E17:{v:["0","1","3/5","-1/5","1/5"].map(x=>C(x)),e:C(-2,-1)},
 E289:{v:["1","0","-18","16","1"].map(x=>C(x)),e:C(1,-2)},
 E4913:{v:["1","-7","21","-5","-2"].map(x=>C(x)),e:C(2,1)}
};
for(const[name,{v,e}]of Object.entries(eigs))must(act(v).every((x,j)=>ceq(x,cm(e,v[j]))),"eigen_"+name);
const basis={
 CMre:["1","12","-10","-20","1"],CMim:["0","-20","28","-12","4"],
 E17:["0","1","3/5","-1/5","1/5"],E289:["1","0","-18","16","1"],E4913:["1","-7","21","-5","-2"]
};
const names=Object.keys(basis),AA=Array.from({length:5},(_,j)=>names.map(n=>basis[n][j]));
let DD=AA.map(row=>row.map(rr)),det=R(1);
for(let k=0;k<5;k++){let row=k;while(row<5&&!DD[row][k][0])row++;if(row===5)throw Error("singular basis");if(row!==k){[DD[row],DD[k]]=[DD[k],DD[row]];det=rn(det);}
 const piv=DD[k][k];det=rm(det,piv);for(let j=k+1;j<5;j++){const a=rd(DD[j][k],piv);for(let l=k;l<5;l++)DD[j][l]=rs(DD[j][l],rm(a,DD[k][l]));}
}
must(rstr(det)==="65536/5","basis_determinant");
const target=["19509103/28114944000","10318337/702873600","777767/27525120","721667/86016000","55879/275251200"];
const sol=rsolve(AA,target);must(sol.rank===5,"actual_CBminus_complete_decomposition");
const coeff=Object.fromEntries(names.map((n,j)=>[n,rstr(sol.x[j])]));
const a=rr(coeff.CMre),b=rr(coeff.CMim),r1=rr(coeff.E17),r2=rr(coeff.E289),r3=rr(coeff.E4913);
const L=rs(rm(R(15),a),rm(R(8),b)),M=ra(rm(R(8),a),rm(R(15),b));
const mass=rs(rs(ra(rm(R(-2),r1),rm(R(32),r2)),rm(R(10),r3)),rm(R(4),L));
must(rstr(mass)==="-2261/81920","full_arithmetic_decomposition_mass");
must(Object.values(coeff).every(v=>rr(v)[0]!==0n),"all_five_fixed_coefficients_nonzero");
const report={
 status:"PASS",arithmetic:"exact rational function-field trace over Q(i); five exact values determine degree<=4",
 target_prime_scan:false,checks,
 matrix_real_times128:R128,matrix_imag_times128:I128,
 ramified_fiber_row:directRow.map(cstr),
 eigenvalues:Object.fromEntries(Object.entries(eigs).map(([k,v])=>[k,cstr(v.e)])),
 basis_determinant:rstr(det),
 actual_CBminus_coefficients:coeff,
 CM_mass_L:rstr(L),CM_antisymmetric_M:rstr(M),mass:rstr(mass)
};
console.log(JSON.stringify(report,null,2));
