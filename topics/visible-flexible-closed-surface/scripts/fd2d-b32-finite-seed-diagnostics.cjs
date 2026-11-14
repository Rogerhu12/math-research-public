/* B32 finite nonzero initializer diagnostics. Pure JavaScript numerical
 * functions; no BVP, actual surface reconstruction or continuous certificate.
 * Uses the new R181 B32 scalar metric via the independent R187 reader.
 * The packaged functions were evaluated in V8 while the OS executor was
 * unavailable. The optional Node CLI is provided for reproduction.
 */
"use strict";
function createB32SeedDiagnostics(){
function run(input) {
  const a0=input.a0, mu=input.mu, p=input.parameters;
  const nodes=[-.9602898564975363,-.7966664774136267,-.5255324099163290,-.1834346424956498,.1834346424956498,.5255324099163290,.7966664774136267,.9602898564975363];
  const weights=[.1012285362903763,.2223810344533745,.3137066458778873,.3626837833783620,.3626837833783620,.3137066458778873,.2223810344533745,.1012285362903763];
  const density=x=>p.r+p.D*(1-Math.tanh(p.k*(Math.cos(2*x)-p.c)))/2+input.u0+input.u2*Math.cos(2*x)+input.u4*Math.cos(4*x);
  const gl=(left,right)=>{
    let r=0,c=0;
    for(let j=0;j<8;j++){const x=(left+right)/2+(right-left)*nodes[j]/2,w=(right-left)*weights[j]/2,rho=density(x);r+=w*rho;c+=w*rho*Math.cos(2*x);}
    return [r,c];
  };
  const cases=[];
  for(const panels of input.panels){
    const tab=[];let R=0,C=0;const step=Math.PI/(2*panels);
    for(let i=0;i<panels;i++){
      const left=i*step,right=(i+1)*step;
      for(let j=0;j<8;j++){
        const x=(left+right)/2+step*nodes[j]/2,w=step*weights[j]/2;
        const [r,c]=gl(left,x);const u=(R+r)/a0,Q=C+c-mu*(R+r);
        tab.push({u,Q,weight:w*density(x)});
      }
      const [dr,dc]=gl(left,right);R+=dr;C+=dc;
    }
    const axes=alpha=>{
      let A=a0,B=a0,dgap=0;
      for(const {u,Q,weight} of tab){
        const t=alpha*Q,ss=Math.sin(t),cm1=-2*Math.sin(t/2)**2;
        const ds=Math.sin(u)*cm1+Math.cos(u)*ss;
        const dc=Math.cos(u)*cm1-Math.sin(u)*ss;
        A+=weight*ds;B+=weight*dc;
        dgap+=weight*Q*(Math.cos(u+t)+Math.sin(u+t));
      }
      return {A,B,gap:A-B,gap_derivative:dgap};
    };
    const roots=[];
    for(const target of input.targets){
      let left=0,right=.4;
      const br=axes(right);
      if(br.gap<target){roots.push({target,bracket_failed:true,upper:br});continue;}
      for(let it=0;it<64;it++){const mid=(left+right)/2;if(axes(mid).gap<target)left=mid;else right=mid;}
      const alpha=(left+right)/2;
      roots.push({target,alpha,...axes(alpha),
        exact_sufficient_central_lower_numeric:200/201-2*Math.abs(alpha),
        extrema_n:[1/a0+alpha*(-1-mu),1/a0+alpha*(1-mu)],
        tail_constant:.4*target,
        tail_curvature_uniform_upper:315*(.4*target)/(128*.46),
        terminal_full_reference_kappa_upper:7+315*(.4*target)/(128*.46)});
    }
    cases.push({panels,quadrature_nodes:tab.length,
      quarter_arc_defect:R-a0*Math.PI/2,
      quarter_basis_primitive_defect:C-mu*R,
      zero_gap_derivative:axes(0).gap_derivative,
      maximum_first_mode_gap_in_point_four_bracket:axes(.4).gap,roots});
  }
  return {schema:'fd2d-B32-independent-JavaScript-finite-central-seed-screen-v1',
    input,cases,formula:'rho(phi), U=int rho/a0, Q=int rho*(cos2phi-mu1); A=a0+int rho*(sin(U+alphaQ)-sinU), B=a0+int rho*(cos(U+alphaQ)-cosU)',
    floating_evaluation_only:true,quadrature_difference_is_not_interval_error_bound:true,
    Python_B32_provider_executed:false,BVP_started:false,wholebody_run:false};
}

function compare(r187,bundle,input){
  const base=r187.candidate(bundle),L=base.segments.at(-1).L,phase0=base.segments.at(-1).p0,d=Math.PI/2+phase0;
  const width=.46,amp=input.tail_amplitude,N=input.angles;
  const step=(x,a,b)=>{const t=Math.max(0,Math.min(1,(x-a)/(b-a)));return [t*t*t*(10+t*(-15+6*t)),30*t*t*(1-t)*(1-t)/(b-a)];};
  const rows=[];
  for(const requested of input.tau){
    const tau=requested,s=base.end-tau,a=base.at(s).a,t=tau/L;
    const eps=d*t*t*(3-2*t),ep=6*d*t*(1-t)/L,epp=6*d*(1-2*t)/(L*L);
    const v=-Math.cos(eps),vplus=2*Math.sin(eps/2)**2,c=v/a,n0=Math.sin(eps)/a,l0=ep;
    const ns=c*(l0-n0),ls=-epp,K=n0*l0,Ks=ns*l0+n0*ls;
    const [eta,etas]=step(s,.42*base.end,base.end);
    const [chi,chis]=step(s,base.end-L,base.end-L/2);
    const summary={tau,s,a,K,n0,l0,eta,chi,round_plus_tail:{G:0,Cn:0,Cm:0,matrix_norm:0,max_shift:0},tail_plus_isotropic:{G:0,Cn:0,Cm:0,matrix_norm:0,max_shift:0}};
    for(let j=0;j<N;j++){
      const u=2*Math.PI*j/N,sn=Math.sin(u),cs=Math.cos(u),y=a*sn,q=(Math.abs(y)-.34)/width;
      let k=0,ky=0;
      if(q>0&&q<1){k=630*amp*q**4*(1-q)**4/width;ky=Math.sign(y)*2520*amp*q**3*(1-q)**3*(1-2*q)/(width*width);}
      const kt=eta*k,kt_s=etas*k+eta*ky*v*sn,kt_u=eta*ky*a*cs;
      const CnT=etas*k*cs*cs+eta*vplus*(ky*sn*cs*cs+k*(cs*cs-sn*sn)/a);
      const CmT=-etas*k*sn*cs-eta*vplus*(ky*sn*sn*cs+2*k*sn*cs/a);
      const fn=n0+kt*cs*cs,fm=-kt*sn*cs,fl=l0+kt*sn*sn;
      const ds0=ns-ls;
      const dd=n0-l0+kt*(cs*cs-sn*sn),mm=fm;
      const dds=ds0+kt_s*(cs*cs-sn*sn),mms=-kt_s*sn*cs;
      const ddu=kt_u*(cs*cs-sn*sn)-4*kt*sn*cs;
      const mmu=-kt_u*sn*cs+kt*(sn*sn-cs*cs);
      const hh=Math.sqrt(dd*dd+4*mm*mm+4*K);
      const hs=(dd*dds+4*mm*mms+2*Ks)/hh,hu=(dd*ddu+4*mm*mmu)/hh;
      const B=n0*sn*sn+l0*cs*cs,Bs=ns*sn*sn+ls*cs*cs,Bu=2*(n0-l0)*sn*cs;
      const C=kt*B,Cs=kt_s*B+kt*Bs,Cu=kt_u*B+kt*Bu;
      const den=hh+n0+l0+kt,dens=hs+ns+ls+kt_s,denu=hu+kt_u;
      const E=-2*C/den,Es=-2*(Cs*den-C*dens)/(den*den),Eu=-2*(Cu*den-C*denu)/(den*den);
      const H=Math.hypot(kt,2*Math.sqrt(K));
      const b=H===0?0:2*K/(H+kt);
      // At the left endpoint chi=chi_s=0; only their weighted products
      // occur in this complete field. Do not assign an unneeded b_s trace.
      const weighted_bs=chi===0?0:chi*(Ks-b*kt_s)/H;
      const weighted_bu=chi===0?0:-chi*b*kt_u/H;
      const variants=[
        ['round_plus_tail',fn+chi*E,fm,fl+chi*E,CnT+chis*E+chi*Es,CmT-chi*Eu/a,Math.abs(chi*E)],
        ['tail_plus_isotropic',(1-chi)*n0+kt*cs*cs+chi*b,fm,(1-chi)*l0+kt*sn*sn+chi*b,CnT+chis*(b-n0)+weighted_bs,CmT-weighted_bu/a,Math.max(Math.abs(chi*(b-n0)),Math.abs(chi*(b-l0)))]
      ];
      for(const [name,n,m,l,Cn,Cm,shift] of variants){
        const out=summary[name],G=n*l-m*m-K,rad=Math.hypot(n-l,2*m),kn=Math.max(Math.abs(n+l+rad),Math.abs(n+l-rad))/2;
        if(Math.abs(Cn)>out.Cn){out.Cn=Math.abs(Cn);out.Cn_at=u;}
        out.Cm=Math.max(out.Cm,Math.abs(Cm));out.G=Math.max(out.G,Math.abs(G));out.matrix_norm=Math.max(out.matrix_norm,kn);out.max_shift=Math.max(out.max_shift,shift);
        out.angular_mean_square=(out.angular_mean_square||0)+(G*G+Cn*Cn+Cm*Cm)/N;
      }
    }
    rows.push(summary);
  }
  return {schema:'fd2d-B32-finite-terminal-reference-comparison-JavaScript-v2',input,base:{end:base.end,L,deepCoast:base.deepCoast},rows,
    actual_runtime:'pure JavaScript/V8; no OS child process',
    object:'Complete analytic preprojection initializer, evaluated in physical material u',
    P1_or_Fourier_projection_performed:false,Gauss_Codazzi_solution_claimed:false,continuous_bound_claimed:false};
}


function compareGraded(r187,bundle,input){
  const base=r187.candidate(bundle),seg=base.segments.at(-1),L=seg.L,d=Math.PI/2+seg.p0,N=input.angles;
  const S5=t=>t<=0?[0,0]:t>=1?[1,0]:[t*t*t*(10+t*(-15+6*t)),30*t*t*(1-t)*(1-t)];
  const out=[];
  for(const tau of input.tau){
    const s=base.end-tau,a=base.at(s).a,t=tau/L,eps=d*t*t*(3-2*t),l0=6*d*t*(1-t)/L,ls=-6*d*(1-2*t)/(L*L);
    const v=-Math.cos(eps),c=v/a,n0=Math.sin(eps)/a,ns=c*(l0-n0),K=n0*l0,Ks=ns*l0+n0*ls;
    const [eta,e0]=S5((s-.42*base.end)/(.58*base.end)),etas=e0/(.58*base.end);
    const variants=input.transition_widths.map(delta=>({delta,G:0,Cn:0,Cm:0,matrix_norm:0,angular_mean_square:0}));
    for(let j=0;j<N;j++){
      const u=2*Math.PI*j/N,sn=Math.sin(u),cs=Math.cos(u),y=a*sn,z=(Math.abs(y)-.34)/.46;
      let k=0,ky=0;
      if(z>0&&z<1){k=630*input.tail_amplitude*z**4*(1-z)**4/.46;ky=Math.sign(y)*2520*input.tail_amplitude*z**3*(1-z)**3*(1-2*z)/(.46*.46);}
      const kt=eta*k,kts=etas*k+eta*ky*v*sn,ktu=eta*ky*a*cs,cos2=cs*cs-sn*sn;
      for(const row of variants){
        const [q,qx]=S5(tau/row.delta),qs=-qx/row.delta;
        const dd=q*(n0-l0)+kt*cos2,mm=-kt*sn*cs;
        const dds=qs*(n0-l0)+q*(ns-ls)+kts*cos2,mms=-kts*sn*cs;
        const ddu=ktu*cos2-4*kt*sn*cs,mmu=-ktu*sn*cs-kt*cos2;
        const h=Math.sqrt(dd*dd+4*mm*mm+4*K);
        const hs=(dd*dds+4*mm*mms+2*Ks)/h,hu=(dd*ddu+4*mm*mmu)/h;
        const n=(h+dd)/2,l=(h-dd)/2,nu=(hu+ddu)/2,lu=(hu-ddu)/2,n_s=(hs+dds)/2;
        const Cn=n_s-mmu/a-c*(l-n),Cm=mms-lu/a+2*c*mm,G=n*l-mm*mm-K;
        row.G=Math.max(row.G,Math.abs(G));row.Cn=Math.max(row.Cn,Math.abs(Cn));row.Cm=Math.max(row.Cm,Math.abs(Cm));
        row.matrix_norm=Math.max(row.matrix_norm,(Math.abs(h)+Math.hypot(dd,2*mm))/2);
        row.angular_mean_square+=(G*G+Cn*Cn+Cm*Cm)/N;
      }
    }
    out.push({tau,s,variants});
  }
  return {schema:"fd2d-B32-Gauss-preserving-terminal-layer-seed-screen-v1",input,base:{end:base.end,L,deepCoast:base.deepCoast},rows:out,
    object:"Analytic full function on positive-K final half-brake, before P1/Fourier projection",finite_evaluation_only:true,BVP_started:false};
}



function integrateReferences(r187,bundle,input){
  const xs=[-.9602898564975363,-.7966664774136267,-.5255324099163290,-.1834346424956498,.1834346424956498,.5255324099163290,.7966664774136267,.9602898564975363];
  const ws=[.1012285362903763,.2223810344533745,.3137066458778873,.3626837833783620,.3626837833783620,.3137066458778873,.2223810344533745,.1012285362903763];
  const tau=[],weights=[];
  for(let i=0;i+1<input.edges.length;i++){
    const lo=input.edges[i],hi=input.edges[i+1];
    for(let j=0;j<8;j++){tau.push((lo+hi)/2+(hi-lo)*xs[j]/2);weights.push((hi-lo)*ws[j]/2);}
  }
  const orig=compare(r187,bundle,{tail_amplitude:input.tail_amplitude,angles:input.angles,tau});
  const half=orig.base.L/2,idx=[];
  for(let i=0;i<tau.length;i++)if(tau[i]<half)idx.push(i);
  const graded=compareGraded(r187,bundle,{tail_amplitude:input.tail_amplitude,angles:input.angles,transition_widths:input.transition_widths,tau:idx.map(i=>tau[i])});
  const result={},names=["round_plus_tail","tail_plus_isotropic",...input.transition_widths.map(x=>"graded_"+x)];
  for(const name of names)result[name]={unnormalized_radial_integral_angular_mean_square:0,sample_maximum_Cn:0,sample_maximum_Cm:0,sample_maximum_G:0,sample_maximum_matrix_norm:0};
  let g=0;
  for(let i=0;i<tau.length;i++){
    const rows={round_plus_tail:orig.rows[i].round_plus_tail,tail_plus_isotropic:orig.rows[i].tail_plus_isotropic};
    for(let j=0;j<input.transition_widths.length;j++)rows["graded_"+input.transition_widths[j]]=tau[i]<half?graded.rows[g].variants[j]:orig.rows[i].round_plus_tail;
    if(tau[i]<half)g++;
    for(const name of names){
      const x=rows[name],r=result[name];
      r.unnormalized_radial_integral_angular_mean_square+=weights[i]*x.angular_mean_square;
      r.sample_maximum_Cn=Math.max(r.sample_maximum_Cn,x.Cn);r.sample_maximum_Cm=Math.max(r.sample_maximum_Cm,x.Cm);
      r.sample_maximum_G=Math.max(r.sample_maximum_G,x.G);r.sample_maximum_matrix_norm=Math.max(r.sample_maximum_matrix_norm,x.matrix_norm);
    }
  }
  return {schema:"fd2d-B32-terminal-completed-seed-finite-integral-v2",input,radial_points:tau.length,base:orig.base,integration:result,
    actual_runtime:"pure JavaScript/V8; no OS child process",finite_quadrature_only:true,not_a_continuous_error_certificate:true,no_BVP_or_body:true,
    graded_definition:"d=q(tau/delta)*(n0-l0)+eta*kappa*cos(2u), m=-eta*kappa*sin(u)*cos(u); n,l=(sqrt(d*d+4*m*m+4*K)+/-d)/2; q=S5. Unchanged original initializer for tau>=L/2."};
}

  return {central:run,terminal:compare,graded:compareGraded,integrate:integrateReferences};
}
if(typeof module!=="undefined"&&module.exports){
  module.exports={createB32SeedDiagnostics};
  if(require.main===module){
    const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
    const [inputFile,outputFile]=process.argv.slice(2);
    if(!inputFile||!outputFile)throw Error("Usage: node this.cjs input.json new-report.json");
    if(fs.existsSync(outputFile))throw Error("Choose a new output path");
    const input=JSON.parse(fs.readFileSync(inputFile,"utf8"));
    const topic=path.resolve(__dirname,"..");
    const candidateFile=path.resolve(topic,input.candidate_path);
    const scalarFile=path.resolve(topic,input.scalar_reader_path);
    const bundle=JSON.parse(fs.readFileSync(candidateFile,"utf8"));
    const r187=require(scalarFile).createR187(),api=createB32SeedDiagnostics();
    const report={
      schema:"fd2d-B32-finite-seed-diagnostics-packaged-v1",
      central:api.central(input.central),
      terminal:api.terminal(r187,bundle,input.terminal),
      integrals:input.integrals.map(q=>api.integrate(r187,bundle,q)),
      no_BVP_or_body:true,continuous_certificate:false,
      reproduction_runtime:"Node CLI",
      source_sha256:crypto.createHash("sha256").update(fs.readFileSync(__filename)).digest("hex"),
      scalar_sha256:crypto.createHash("sha256").update(fs.readFileSync(scalarFile)).digest("hex"),
      candidate_sha256:crypto.createHash("sha256").update(fs.readFileSync(candidateFile)).digest("hex"),
      input_sha256:crypto.createHash("sha256").update(fs.readFileSync(inputFile)).digest("hex")
    };
    fs.mkdirSync(path.dirname(outputFile),{recursive:true});
    fs.writeFileSync(outputFile,JSON.stringify(report,null,2)+"\n");
    console.log(JSON.stringify({outputFile,finite_evaluation_only:true}));
  }
}
