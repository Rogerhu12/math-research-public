// Root: smooth logarithmic three-pulse cells with transition width eta=c*delta.
// Pure JavaScript, deterministic. No array/grid printing.
// This is a linear finite-cell experiment, NOT an infinite nonlinear tail theorem.
// State (V,pi), (V,pi)_s=[[k,1/P],[-nu*P,-k]](V,pi).
// P: 1 -> R/delta -> delta/alpha -> 1/delta -> exp(A).
// Four quintic log transitions plus two port collars, each length c*delta.
// Each of the three plateaux has length delta. Overall P scale cancels linearly.
function cellSmooth(x){return x*x*x*(10+x*(-15+6*x));}
function cellSmoothDerivative(x){return 30*x*x*(1-x)*(1-x);}
function cellSegments(delta,R,alpha,A,c){
  if(!(delta>0&&R>0&&alpha>0&&c>0))throw new Error("positive cell parameters required");
  const ld=Math.log(delta),v=[ld,Math.log(R),2*ld-Math.log(alpha),0,ld+A],da=[0,0,-1/alpha,0,0];
  const segs=[];
  const port=(j)=>segs.push({lengthRatio:c,lo:v[j],hi:v[j],alo:da[j],ahi:da[j],transition:false});
  const transition=(j)=>segs.push({lengthRatio:c,lo:v[j],hi:v[j+1],alo:da[j],ahi:da[j+1],transition:true});
  const plateau=(j)=>segs.push({lengthRatio:1,lo:v[j],hi:v[j],alo:da[j],ahi:da[j],transition:false});
  port(0);transition(0);plateau(1);transition(1);plateau(2);transition(2);plateau(3);transition(3);port(4);
  return segs;
}
function smoothCellTransfer(options={}){
  const {delta=.08,R=16,alpha=1+1/R,A=3*Math.log(2),c=.05,mode=2,direction=1,steps=256}=options;
  const k=direction*(mode*mode-4)/Math.sqrt(12),nu=mode*mode*(mode*mode-1)/12;
  let state=new Float64Array([1,0,0,1,0,0,0,0]);
  let maxState=1;
  const segments=cellSegments(delta,R,alpha,A,c);
  function rhs(y,seg,x){
    const s=seg.transition?cellSmooth(x):0,lp=seg.lo+(seg.hi-seg.lo)*s,ap=seg.alo+(seg.ahi-seg.alo)*s;
    const p=Math.exp(lp),u=delta*delta/p*seg.lengthRatio,v=-nu*p*seg.lengthRatio,z=k*delta*seg.lengthRatio;
    const du=-ap*u,dv=ap*v,o=new Float64Array(8);
    for(let j=0;j<2;j++){
      o[j]=z*y[j]+u*y[j+2];o[j+2]=v*y[j]-z*y[j+2];
      o[j+4]=z*y[j+4]+u*y[j+6]+du*y[j+2];
      o[j+6]=v*y[j+4]-z*y[j+6]+dv*y[j];
    }return o;
  }
  for(const seg of segments){
    if(!seg.transition){
      const P=Math.exp(seg.lo)/delta,L=seg.lengthRatio*delta,rho=Math.sqrt(Math.max(0,nu-k*k));
      const cc=Math.cos(rho*L),ss=rho?Math.sin(rho*L)/rho:L;
      const m=[cc+k*ss,ss/P,-nu*P*ss,cc-k*ss],dm=[0,-seg.alo*ss/P,seg.alo*(-nu*P*ss),0];
      const y=new Float64Array(8);
      for(let j=0;j<2;j++){
        y[j]=m[0]*state[j]+m[1]*state[j+2];y[j+2]=m[2]*state[j]+m[3]*state[j+2];
        y[j+4]=m[0]*state[j+4]+m[1]*state[j+6]+dm[0]*state[j]+dm[1]*state[j+2];
        y[j+6]=m[2]*state[j+4]+m[3]*state[j+6]+dm[2]*state[j]+dm[3]*state[j+2];
      }state=y;
    }else{
      const h=1/steps;
      for(let n=0;n<steps;n++){
        const x=n*h,a=rhs(state,seg,x),tmp=new Float64Array(8);
        for(let j=0;j<8;j++)tmp[j]=state[j]+h*a[j]/2;
        const b=rhs(tmp,seg,x+h/2);
        for(let j=0;j<8;j++)tmp[j]=state[j]+h*b[j]/2;
        const cc=rhs(tmp,seg,x+h/2);
        for(let j=0;j<8;j++)tmp[j]=state[j]+h*cc[j];
        const d=rhs(tmp,seg,x+h);
        for(let j=0;j<8;j++)state[j]+=h*(a[j]+2*b[j]+2*cc[j]+d[j])/6;
      }
    }
    maxState=Math.max(maxState,...Array.from(state.slice(0,4),Math.abs));
  }
  const t=Array.from(state.slice(0,4)),dt=Array.from(state.slice(4));
  return {matrix:t,alphaDerivative:dt,determinant:t[0]*t[3]-t[1]*t[2],maxState,parameters:{delta,R,alpha,A,c,mode,direction,steps}};
}
function calibrateSmoothCell(options={}){
  const R=options.R??16;let alpha=options.initialAlpha??(1+1/R),last=null,it=0;
  for(;it<24;it++){
    last=smoothCellTransfer({...options,alpha});
    const f=last.matrix[2],df=last.alphaDerivative[2];
    if(Math.abs(f)<2e-12*Math.max(1,Math.abs(last.matrix[0])))break;
    if(!(Math.abs(df)>1e-18&&Number.isFinite(df)))throw new Error("singular alpha derivative");
    let step=-f/df,accepted=false;
    for(let back=0;back<20;back++){
      const candidate=alpha+step;
      if(candidate>0){
        const v=smoothCellTransfer({...options,alpha:candidate});
        if(Math.abs(v.matrix[2])<Math.abs(f)){alpha=candidate;last=v;accepted=true;break;}
      }step*=.5;
    }
    if(!accepted)throw new Error("alpha line search failed");
  }
  if(it>=24)throw new Error("alpha Newton failed");
  return {...last,alpha,iterations:it,gain:-last.matrix[0],targetLowerEntry:last.matrix[2]};
}
function smoothCellScalarAudit(options={}){
  const Rlist=options.Rlist??[4,16,64],nlist=options.nlist??[0,1,2,4,8,16,32,64,100],delta0=options.delta0??.08,a=options.a??3,c=options.c??.05;
  const levels=options.levels??[128,256,512],rows=[];
  for(const R of Rlist)for(const n of nlist){
    const delta=delta0*Math.pow(2,-n),A=a*Math.log(2),runs=[];
    for(const steps of levels){
      const v=calibrateSmoothCell({delta,R,A,c,steps});
      runs.push({steps,alpha:v.alpha,gain:v.gain,lower:v.targetLowerEntry,detError:Math.abs(v.determinant-1),alphaDerivative:v.alphaDerivative[2],iterations:v.iterations});
    }
    rows.push({R,n,delta,log10Delta:Math.log10(delta),A,c,totalCellLength:(3+6*c)*delta,
      runs,alphaLastDifference:Math.abs(runs.at(-1).alpha-runs.at(-2).alpha),
      gainLastDifference:Math.abs(runs.at(-1).gain-runs.at(-2).gain),
      gainOverPortScale:runs.at(-1).gain/Math.exp(A)});
  }
  return {scope:"Finite smooth actual-profile linear cell calibration only. No nonlinear tail, no uniform inverse, no C2 infinite-tail certificate, no visible closed solution.",
    parameters:{delta0,a,c,Rlist,nlist,levels,outerPortScale:"epsilon * delta_n^a",innerOuterPortRatio:"exp(A)=2^a"},
    rows};
}

if(typeof module!=="undefined")module.exports={cellSmooth,cellSmoothDerivative,cellSegments,smoothCellTransfer,calibrateSmoothCell,smoothCellScalarAudit};
if(typeof require==="function"&&typeof module!=="undefined"&&require.main===module){
 const fs=require("node:fs");const i=process.argv.indexOf("--out");
 if(i<0||!process.argv[i+1])throw new Error("Usage: node general_root_smooth_tail_cells.cjs --out report.json");
 const result=smoothCellScalarAudit({Rlist:[16,32,64],levels:[256,512,1024]});
 fs.writeFileSync(process.argv[i+1],JSON.stringify(result,null,2)+"\n");
 process.stdout.write(JSON.stringify({rows:result.rows.length,output:process.argv[i+1],scope:result.scope})+"\n");
}
