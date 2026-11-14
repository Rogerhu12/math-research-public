// Exact R235 octic CM trace, actual companion decomposition, and original degree-bound restoration.

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

const checks={},must=(b,n)=>{if(!b)throw Error("FAIL "+n);checks[n]=true;};
const octicAt=t=>{
 const f=ps(N,pscale(Q,C(t))),inverse=inverseLinear(f),inv=modpow(inverse,19,f),out=[];
 must(ceq(mod(pm([C(1),cn(B)],inverse),f)[0],C(1)),"linear_inverse_"+t);
 for(let j=0;j<4;j++){
  let num=pm(pm(pp([C(1),cn(BB)],15-4*j),pp([PIB,I],4*j+2)),pp([PI,cn(I)],2));
  num=[...Array.from({length:j+1},()=>C()),...num];
  out.push(cd(traceP(mod(pm(mod(num,f),inv),f),f),C(t)));
 }
 return out;
};
const vals=Array.from({length:5},(_,j)=>octicAt(j+1));
const V=Array.from({length:4},(_,t)=>Array.from({length:4},(_,j)=>String(BigInt(t+1)**BigInt(j))));
const matrix=Array.from({length:4},()=>[]);
for(let j=0;j<4;j++){
 const real=rsolve(V,vals.slice(0,4).map(row=>rstr(row[j][0]))).x,imag=rsolve(V,vals.slice(0,4).map(row=>rstr(row[j][1]))).x;
 for(let k=0;k<4;k++)matrix[k].push([real[k],imag[k]]);
}
const RR=[[-62,-4,-18,-16],[232,58,44,54],[-318,-136,-154,-140],[44,42,56,158]],II=[[-21,43,31,7],[331,39,-73,-53],[-59,-83,33,65],[-43,1,-7,-51]];
must(matrix.every((row,j)=>row.every((v,k)=>ceq(v,[R(RR[j][k],64),R(II[j][k],64)]))),"entire_octic_trace_matrix");
must(Array.from({length:4},(_,j)=>peval(matrix.map(row=>row[j]),C(5))).every((v,j)=>ceq(v,vals[4][j])),"extra_fiber_at_five");
const cmm=(a,b)=>a.map(row=>b[0].map((_,k)=>row.reduce((sum,v,j)=>ca(sum,cm(v,b[j][k])),C())));
const SS=matrix.map(row=>row.map(v=>cd(v,C(-1,2)))),SS2=cmm(SS,SS),SS4=cmm(SS2,SS2);
must(SS4.every((row,j)=>row.every((v,k)=>ceq(v,C(j===k?-1:0)))),"normalized_trace_fourth_power_minus_identity");

const Q2=(a=0,b=0)=>[rr(a),rr(b)],qadd=(x,y)=>[ra(x[0],y[0]),ra(x[1],y[1])],qneg=x=>x.map(rn),qsub=(x,y)=>qadd(x,qneg(y));
const qmul=(x,y)=>[ra(rm(x[0],y[0]),rm(R(2),rm(x[1],y[1]))),ra(rm(x[0],y[1]),rm(x[1],y[0]))];
const qscale=(x,r)=>x.map(v=>rm(v,rr(r))),qeq=(x,y)=>rstr(x[0])===rstr(y[0])&&rstr(x[1])===rstr(y[1]),qstr=x=>x.map(rstr);
const polys=[
 [Q2(1),Q2(-5,2),Q2(11,-4),Q2(-15,10)],
 [Q2(1),Q2("63/17","-70/17"),Q2("-77/17","44/17"),Q2("5/17","2/17")],
 [Q2(1),Q2(-5,-2),Q2(11,4),Q2(-15,-10)],
 [Q2(1),Q2("63/17","70/17"),Q2("-77/17","-44/17"),Q2("5/17","-2/17")]
];
const signs=[[1,1],[-1,1],[-1,-1],[1,-1]];
for(let e=0;e<4;e++){
 const [x,y]=signs[e],lre=Q2(0,String(-x-2*y)+"/2"),lim=Q2(0,String(2*x-y)+"/2"),P=polys[e];
 for(let j=0;j<4;j++){
  const re=matrix[j].reduce((t,m,k)=>qadd(t,qscale(P[k],m[0])),Q2()),im=matrix[j].reduce((t,m,k)=>qadd(t,qscale(P[k],m[1])),Q2());
  must(qeq(re,qmul(lre,P[j]))&&qeq(im,qmul(lim,P[j])),"primitive_eigen_"+[1,3,5,7][e]+"_row_"+j);
 }
}
const qdiv=(x,y)=>{const n=rs(rm(y[0],y[0]),rm(R(2),rm(y[1],y[1])));return qscale(qmul(x,[y[0],rn(y[1])]),rd(R(1),n));};
const qdet=a=>{a=a.map(row=>row.map(v=>v.map(rr)));let d=Q2(1);for(let k=0;k<a.length;k++){let j=k;while(j<a.length&&qeq(a[j][k],Q2()))j++;if(j===a.length)return Q2();if(j!==k){[a[j],a[k]]=[a[k],a[j]];d=qneg(d);}const p=a[k][k];d=qmul(d,p);for(let l=k+1;l<a.length;l++){const c=qdiv(a[l][k],p);for(let m=k;m<a.length;m++)a[l][m]=qsub(a[l][m],qmul(c,a[k][m]));}}return d;};
const eigenBasisDet=qdet(Array.from({length:4},(_,j)=>polys.map(P=>P[j])));
must(qeq(eigenBasisDet,Q2("32768/17")),"octic_eigenbasis_determinant");
const aa=[Q2("-39797/14784000","-8177/4224000"),Q2("-2091/448000","-2669/1971200"),Q2("-39797/14784000","8177/4224000"),Q2("-2091/448000","2669/1971200")];
const bb=[Q2("224494093/56229888000","4237163/1363148800"),Q2("-6031447/3748659200","-202405417/62977474560"),Q2("224494093/56229888000","-4237163/1363148800"),Q2("-6031447/3748659200","202405417/62977474560")];
const av=["-17/1155","-53/61600","1/66000","-1/16800"].map(rr),bv=["33505597/7028736000","2806381/108134400","2225101/114688000","144691/68812800"].map(rr);
for(const[label,co,actual]of[["A",aa,av],["Bplus",bb,bv]]){
 for(let j=0;j<4;j++)must(qeq(co.reduce((a,c,k)=>qadd(a,qmul(c,polys[k][j])),Q2()),Q2(actual[j])),"actual_"+label+"_eigen_decomposition_"+j);
 must(co.every(x=>x[0][0]!==0n&&x[1][0]!==0n),"all_four_"+label+"_sources_nonzero");
}
const mat=a=>a.map(row=>row.map(rr)),rmm=(a,b)=>a.map(row=>b[0].map((_,k)=>row.reduce((s,v,j)=>ra(s,rm(v,b[j][k])),R(0))));
const rsub=(a,b)=>a.map((row,j)=>row.map((v,k)=>rs(v,b[j][k]))),req=(a,b)=>a.length===b.length&&a.every((row,j)=>row.length===b[j].length&&row.every((v,k)=>rstr(v)===rstr(b[j][k])));
const rdet=a=>{a=a.map(row=>row.map(rr));let d=R(1);for(let k=0;k<a.length;k++){let j=k;while(j<a.length&&!a[j][k][0])j++;if(j===a.length)return R(0);if(j!==k){[a[j],a[k]]=[a[k],a[j]];d=rn(d);}const p=a[k][k];d=rm(d,p);for(let l=k+1;l<a.length;l++){const c=rd(a[l][k],p);for(let m=k;m<a.length;m++)a[l][m]=rs(a[l][m],rm(c,a[k][m]));}}return d;};
const DD=mat([["-13/8","-5/8","3/8","11/8"],["-39/2","15/2","-11/2","11/2"],[91,-37,35,-77],[26,94,-126,198],[-520,-120,280,-88],[728,40,-392,-312],[-304,80,336,464],[-32,-96,-160,-224],[32,32,32,32]]);
const EE=mat([["-17/8","-9/8","-1/8","7/8","15/8"],[-68,3,2,-7,40],[-238,30,-14,14,-14],[544,-180,56,36,-432],[340,388,-140,-220,660],[-1088,-368,224,432,0],[544,96,-224,-416,-480],[0,64,128,192,256],[-32,-32,-32,-32,-32]]);
const Cbase=mat([[1,0],[12,-20],[-10,28],[-20,-12],[1,4]]),PP=mat([[0,1,1],[1,0,-7],["3/5",-18,21],["-1/5",16,-5],["1/5",1,-2]]),CC=rmm(EE,Cbase);
const TT=mat([["1/16","1/16","1/16","1/16"],["7/32","5/32","3/32","1/32"]]),UU=mat([["-1/10",0,"-1/2"],["-1/4",1,"-5/4"]]);
must(rstr(rdet(CC.slice(7)))==="-524288","two_actual_CM_top_coefficient_rows_invertible");
const DR=rsub(DD,rmm(CC,TT)),ER=rsub(rmm(EE,PP),rmm(CC,UU));
must([...DR.slice(7),...ER.slice(7)].every(row=>row.every(v=>!v[0])),"all_seven_regularized_sources_have_degree_at_most_six");
const frame=DR.slice(0,7).map((row,j)=>[...row,...ER[j]]),frameDet=rdet(frame);
must(rstr(frameDet)==="4398046511104/5","complete_regularized_seven_dimensional_basis");
const ap=mat([["323168419/14994636800"],["244224499/1574436864000"],["133022909/121110528000"]]),acm=mat([["-16942549/30277632000"],["-197627103/524812288000"]]);
const bcol=bv.map(v=>[v]);
must(req(rsub(rsub(mat([[0],[0]]),rmm(TT,bcol)),rmm(UU,ap)),acm),"actual_CM_coefficients_forced_by_regularization");
const actualPB=rmm(DR,bcol).map((row,j)=>[ra(row[0],rmm(ER,ap)[j][0])]);
must(req(actualPB,mat([["-2261/81920"],["953/102400"],["-2887/192000"],["1501/22400"],["-49/600"],["101/2310"],["-4/455"],[0],[0]])),"actual_full_CB_polynomial_recovered");
const mass=polys.map(P=>DR[0].reduce((s,c,j)=>qadd(s,qscale(P[j],rm(R(2),c))),Q2()));
must(qeq(bb.reduce((sum,b,j)=>qadd(sum,qmul(b,mass[j])),Q2()),Q2("-2261/40960")),"full_CB_mass_equals_minus_twice_beta");
must(qeq(aa.reduce((sum,a)=>qadd(sum,qscale(a,R(4))),Q2()),Q2("-68/1155")),"full_CA_mass_equals_minus_twice_beta");
console.log(JSON.stringify({status:"PASS",arithmetic:"exact rational traces over Q(i) and eigenvectors over Q(sqrt2)",target_prime_scan:false,checks,trace_real_times64:RR,trace_imag_times64:II,eigen_polynomials:polys.map(P=>P.map(qstr)),eigen_basis_determinant:qstr(eigenBasisDet),CA_coefficients:aa.map(qstr),CBplus_coefficients:bb.map(qstr),regularized_octic_matrix:DR.map(row=>row.map(rstr)),regularized_quartic_matrix:ER.map(row=>row.map(rstr)),CM_correction_octic:TT.map(row=>row.map(rstr)),CM_correction_quartic:UU.map(row=>row.map(rstr)),complete_basis_determinant:rstr(frameDet),regularized_octic_masses:mass.map(qstr)},null,2));
