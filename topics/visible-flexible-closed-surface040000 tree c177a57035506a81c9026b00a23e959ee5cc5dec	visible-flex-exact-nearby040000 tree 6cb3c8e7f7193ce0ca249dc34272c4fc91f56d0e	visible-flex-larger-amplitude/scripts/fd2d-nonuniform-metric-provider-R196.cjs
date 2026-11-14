/* R196 nonuniform factory. R190 value/J/primitive formulas are retained.
 * Formula parent Git blob 8c017c1efeca08ed7f2a1cd66f03c6f007488c14;
 * basis parent Git blob 4afea695a78f2dce85bcbc30242a12bc1b07a687.
 * This new implementation must save radialBasisDefinition with every state.
 */
/* Actual C2 two-angle direct-position metric-design objective after R190.
 * Variable B32 radius and exact symmetric boundary lift. Complete angular
 * trigonometric functions are integrated by explicitly stated quadrature.
 */
"use strict";
function createR196MetricProvider(engine,bundle,options={},splines){
  if(!splines){
    if(typeof require==="undefined")throw Error("Supply createR196CubicSplines() in a pure V8 call");
    splines=require("./fd2d-cubic-spline-refinement-R196.cjs").createR196CubicSplines();
  }
  if(!Array.isArray(options.radialKnots))throw Error("Explicit exact normalized radialKnots required");
  const radialBasis=splines.createBasis(options.radialKnots);
  if(options.radialBasisCount!==undefined&&options.radialBasisCount!==radialBasis.count)
    throw Error("radialBasisCount disagrees with explicit knots");
  const J=radialBasis.count,K=options.modes||7;
  const N=options.angles||64;
  if(N%4||N<16)throw Error("Angular count must be a multiple of four");
  const nq=N/4,A=Math.PI/2,du=A/nq;
  const base=engine.candidate(bundle),c=base.centralLength,S=base.end;
  const oldDimension=2*J*K+J+1,cutIndex=oldDimension-1,n=oldDimension+J;
  const radiusCoefficientBound=options.radiusCoefficientBound===undefined?.4:options.radiusCoefficientBound;
  if(!(radiusCoefficientBound>0&&radiusCoefficientBound<.8))throw Error("Require 0<radiusCoefficientBound<.8");
  let lo=.05,hi=2,curve;
  const gap=options.gap===undefined?.05:options.gap;
  if(gap===0)curve=engine.ellipse(1,1);
  else{
    for(let k=0;k<55;k++){
      const B=(lo+hi)/2,q=engine.ellipse(B+gap,B);
      if(q.a0>base.a0)hi=B;else lo=B;
    }
    const B=(lo+hi)/2;curve=engine.ellipse(B+gap,B);
  }
  const G8=engine.gauss(8),G2=engine.gauss(2);
  function shape(s){
    if(s<=c)return {value:0,first:0,second:0};
    if(s>=S)return {value:1,first:0,second:0};
    const t=(s-c)/(S-c),L=S-c;
    return {value:t*t*t*(10+t*(-15+6*t)),
      first:30*t*t*(1-t)*(1-t)/L,second:60*t*(1-t)*(1-2*t)/(L*L)};
  }
  function angularRecord(u){
    const g=curve.at(u),modes=[];
    for(let k=1;k<=K;k++)modes.push(Math.sin(2*k*u));
    return {u,g,modes,ex:-Math.sin(u),ey:Math.cos(u)};
  }
  const nodes=[],quads=[];
  for(let j=0;j<=nq;j++)nodes.push(angularRecord(j*du));
  for(let j=0;j<nq;j++){
    const row=[];
    for(let k=0;k<8;k++)row.push({...angularRecord((j+G8.x[k])*du),weight:du*G8.w[k]});
    quads.push(row);
  }
  function seed(w,q){
    const dx=q.g.v[0]-q.ex,dy=q.g.v[1]-q.ey;
    const tx=q.ex+w.q*dx,ty=q.ey+w.q*dy,tz=w.r*q.g.h;
    const tsx=w.qs*dx,tsy=w.qs*dy,tsz=w.rs*q.g.h;
    const cp2=tx*tx+ty*ty;
    if(!(cp2>1e-15))throw Error("The explicit reference has a singular angle chart");
    return [q.u+Math.atan2(q.ex*ty-q.ey*tx,q.ex*tx+q.ey*ty),
      Math.asin(Math.max(-1,Math.min(1,tz))),
      (tx*tsy-ty*tsx)/cp2,tsz/Math.sqrt(cp2)];
  }
  function makeSlice(s,weight){
    const p=base.at(s),w=engine.profileWeights(s,c,S),angles=[],centers=[],radii=[];
    const radialJets=radialBasis.physicalJets(s,c,S);
    for(let rj=0;rj<radialJets.indices.length;rj++){
      const j=radialJets.indices[rj],b=radialJets.value[rj],bp=radialJets.first[rj],bpp=radialJets.second[rj];
      if(b!==0||bp!==0){
        for(let k=0;k<K;k++){
          angles.push({index:j*K+k,kind:0,k,b,bp,bpp});
          angles.push({index:J*K+j*K+k,kind:1,k,b,bp,bpp});
        }
      }
      if(bp!==0)centers.push({index:2*J*K+j,b,bp,bpp});
      if(b!==0||bp!==0)radii.push({index:oldDimension+j,b,bp,bpp});
    }
    const sh=shape(s);if(sh.first!==0)centers.push({index:cutIndex,b:sh.value,bp:sh.first,bpp:sh.second});
    return {s,weight,p,w,angles,centers,radii,
      nodeSeed:nodes.map(q=>seed(w,q)),quadSeed:quads.map(row=>row.map(q=>seed(w,q)))};
  }
  let cuts=[0,S,...base.segments.map(p=>p.s0),...base.segments.map(p=>p.s1)];
  for(let j=0;j<radialBasis.knotNumbers.length;j++)
    cuts.push(j===0?c:j+1===radialBasis.knotNumbers.length?S:c+(S-c)*radialBasis.knotNumbers[j]);
  cuts.sort((a,b)=>a-b);
  cuts=cuts.filter((x,i)=>i===0||x-cuts[i-1]>2e-14);
  cuts[0]=0;cuts[cuts.length-1]=S;
  const slices=[];
  for(let j=1;j<cuts.length;j++){
    const left=cuts[j-1],width=cuts[j]-left;
    for(let k=0;k<2;k++)slices.push(makeSlice(left+width*G2.x[k],width*G2.w[k]/S));
  }
  function fill(slc,q,sd,z,withJac,out){
    let th=sd[0],ph=sd[1],ths=sd[2],phs=sd[3];
    for(const col of slc.angles){
      const v=z[col.index]*q.modes[col.k];
      if(col.kind===0){th+=col.b*v;ths+=col.bp*v;}
      else{ph+=col.b*v;phs+=col.bp*v;}
    }
    const st=Math.sin(th),ct=Math.cos(th),sp=Math.sin(ph),cp=Math.cos(ph);
    const T=[-st*cp,ct*cp,sp],Dt=[-ct*cp,-st*cp,0],Dp=[st*sp,-ct*sp,cp];
    const Dtt=[st*cp,-ct*cp,0],Dtp=[ct*sp,st*sp,0];
    for(let k=0;k<3;k++){out[k]=T[k];out[3+k]=Dt[k]*ths+Dp[k]*phs;}
    if(!withJac)return;
    for(let j=0;j<slc.angles.length;j++){
      const col=slc.angles[j],v=col.b*q.modes[col.k],vs=col.bp*q.modes[col.k],off=6+6*j;
      for(let k=0;k<3;k++){
        const D=col.kind===0?Dt[k]:Dp[k];
        const Ds=col.kind===0?Dtt[k]*ths+Dtp[k]*phs:Dtp[k]*ths-T[k]*phs;
        out[off+k]=D*v;out[off+3+k]=Ds*v+D*vs;
      }
    }
  }
  function sliceValues(slc,z,withJac){
    const m=slc.angles.length,channels=6*(withJac?m+1:1);
    const total=new Float64Array(channels),moment=new Float64Array(channels);
    const prefix=new Float64Array((nq+1)*channels),out=new Float64Array(channels);
    for(let j=0;j<nq;j++){
      prefix.set(total,j*channels);
      for(let k=0;k<8;k++){
        const q=quads[j][k];fill(slc,q,slc.quadSeed[j][k],z,withJac,out);
        for(let d=0;d<channels;d++){
          const inc=q.weight*out[d];total[d]+=inc;moment[d]+=(A-q.u)*inc;
        }
      }
    }
    prefix.set(total,nq*channels);
    function primitive(node,off,k){
      const value=prefix[node*channels+off+k];
      return k===0?value-total[off+k]:k===1?value:value-moment[off+k]/A;
    }
    let zs=slc.p.zs;
    for(const col of slc.centers)zs+=z[col.index]*col.bp;
    let actualA=slc.p.a,actualAs=slc.p.as;
    for(const col of slc.radii){actualA+=z[col.index]*col.b;actualAs+=z[col.index]*col.bp;}
    const rows=[];
    for(let j=0;j<=nq;j++){
      fill(slc,nodes[j],slc.nodeSeed[j],z,withJac,out);
      const V=[],T=[out[0],out[1],out[2]];
      for(let k=0;k<3;k++)V.push(actualAs*primitive(j,0,k)+actualA*primitive(j,3,k)+(k===2?zs:0));
      const rE=V[0]*V[0]+V[1]*V[1]+V[2]*V[2]-1;
      const rF=V[0]*T[0]+V[1]*T[1]+V[2]*T[2];
      const angularWeight=(j===0||j===nq?.5:1)/nq;
      const row={s:slc.s,u:nodes[j].u,rE,rF,weight:slc.weight*angularWeight,
        relativeMetric:Math.abs(rE)/2+Math.hypot(rE/2,rF),
        immersion:1+rE-rF*rF};
      if(withJac){
        const indices=[],e=[],f=[];
        for(let a=0;a<m;a++){
          const off=6+6*a,dV=[];
          for(let k=0;k<3;k++)dV.push(actualAs*primitive(j,off,k)+actualA*primitive(j,off+3,k));
          indices.push(slc.angles[a].index);
          e.push(2*(V[0]*dV[0]+V[1]*dV[1]+V[2]*dV[2]));
          f.push(dV[0]*T[0]+dV[1]*T[1]+dV[2]*T[2]+V[0]*out[off]+V[1]*out[off+1]+V[2]*out[off+2]);
        }
        for(const col of slc.centers){indices.push(col.index);e.push(2*V[2]*col.bp);f.push(T[2]*col.bp);}
        for(const col of slc.radii){
          const dV=[];for(let k=0;k<3;k++)dV.push(col.bp*primitive(j,0,k)+col.b*primitive(j,3,k));
          indices.push(col.index);e.push(2*(V[0]*dV[0]+V[1]*dV[1]+V[2]*dV[2]));
          f.push(dV[0]*T[0]+dV[1]*T[1]+dV[2]*T[2]);
        }
        row.indices=indices;row.e=e;row.f=f;
      }
      rows.push(row);
    }
    return rows;
  }

  function evaluate(z,config={}){
    if(z.length!==n||Array.from(z).some(x=>!Number.isFinite(x)))throw Error("Wrong/nonfinite complete parameter vector");
    const maxRadiusCoefficient=Math.max(0,...Array.from(z).slice(oldDimension).map(Math.abs));
    if(maxRadiusCoefficient>radiusCoefficientBound)throw Error("Outside the declared sufficient positive-radius coefficient box");
    const jac=!!config.jacobian,need=jac||!!config.direction;
    const H=jac?new Float64Array(n*n):null,g=jac?new Float64Array(n):null;
    const residual=[],jvp=[];
    let squaredNorm=0,maxRelativeMetric=0,minImmersion=Infinity,worst=null,rowCount=0;
    for(const slc of slices){
      for(const row of sliceValues(slc,z,need)){
        const {rE,rF,weight:w}=row;
        squaredNorm+=w*(rE*rE+2*rF*rF);rowCount+=2;
        if(row.relativeMetric>maxRelativeMetric){maxRelativeMetric=row.relativeMetric;worst={s:row.s,u:row.u,rE,rF};}
        minImmersion=Math.min(minImmersion,row.immersion);
        if(config.residuals){residual.push(Math.sqrt(w)*rE,Math.sqrt(2*w)*rF);}
        if(config.direction){
          let de=0,df=0;
          for(let j=0;j<row.indices.length;j++){const v=config.direction[row.indices[j]];de+=row.e[j]*v;df+=row.f[j]*v;}
          jvp.push(Math.sqrt(w)*de,Math.sqrt(2*w)*df);
        }
        if(jac){
          for(let i=0;i<row.indices.length;i++){
            const ii=row.indices[i],ei=row.e[i],fi=row.f[i];
            g[ii]+=w*(ei*rE+2*fi*rF);
            for(let j=0;j<=i;j++){
              const jj=row.indices[j],value=w*(ei*row.e[j]+2*fi*row.f[j]);
              H[ii*n+jj]+=value;if(ii!==jj)H[jj*n+ii]+=value;
            }
          }
        }
      }
    }
    const out={squaredNorm,norm:Math.sqrt(squaredNorm),maxRelativeMetric,minImmersion,
      worst,rowCount,radialPoints:slices.length,quarterNodes:nq+1,fullEquivalentAngles:N,
      fixedPhysicalMetric:false,physicalMetricIsDesignVariable:true,maxRadiusCoefficient,conservativeRadiusLowerBound:.8-maxRadiusCoefficient,newNonlinearAcceptedState:false};
    if(jac){out.H=H;out.g=g;out.diagonal=Float64Array.from({length:n},(_,i)=>H[i*n+i]);}
    if(config.residuals)out.residuals=Float64Array.from(residual);
    if(config.direction)out.jvp=Float64Array.from(jvp);
    return out;
  }
  return {dimension:n,initialVector:()=>new Float64Array(n),
    normal:z=>evaluate(z,{jacobian:true}),value:z=>evaluate(z),
    evaluate,base,curve,radialBasis,radialCuts:Object.freeze(Array.from(cuts)),
    metricRows:(s,z,config={})=>{
      if(!Number.isFinite(s)||s<0||s>S||z.length!==n||Array.from(z).some(x=>!Number.isFinite(x)))throw Error("Invalid complete state/physical point");
      if(Math.max(0,...Array.from(z).slice(oldDimension).map(Math.abs))>radiusCoefficientBound)throw Error("Outside radius coefficient box");
      return sliceValues(makeSlice(s,1),z,!!config.jacobian);
    },
    definition:{
      schema:"fd2d-R190-C2-direct-position-designed-radius-finite-provider-v1",
      implementation:"R196 explicit shared nonuniform cubic basis; frozen R190 formulas",
      radialBasisDefinition:{schema:"fd2d-R196-shared-simple-cubic-radial-basis-v1",degree:3,
        knots:radialBasis.knots,count:J,coordinate:"q=(s-c)/(S-c)",physicalInterval:{c,S},
        endpointExtension:"zero C2",evaluation:"binary64; exact rational definition retained",
        quadratureCutMergeTolerance:2e-14,knotsThemselvesMerged:false},
      radialBlockLayout:{J,K,width:2*K+2,channelOrder:["theta[0:K]","phi[0:K]","height","radius"],globalIndices:[cutIndex]},
      radialBasisCount:J,angularModes:K,fullEquivalentAngles:N,dimension:n,
      angularPrimitive:"complete quarter-cell Gauss8 with actual first moment; no Fourier projection",
      angularMetric:"exactly a^2 in mathematical complete definition",
      radialMetric:"R181 B32 plus complete C2 radius B-spline design; changing rho changes g",radiusCoefficientBound,oldDimension,
      boundary:"complete central ellipse cylinder and zero-tail round flat cut two jets",
      stateLayout:{theta:[0,J*K],phi:[J*K,2*J*K],height:[2*J*K,2*J*K+J],cutHeight:cutIndex,radius:[oldDimension,n]},
      centralGap:base.a0*(curve.A-curve.B)/curve.a0,
      centralA:base.a0*curve.A/curve.a0,centralB:base.a0*curve.B/curve.a0,
      radiusGrid:"R196 explicit simple nonuniform cubic B-splines, at most four active radial blocks, C2 zero endpoint extension",
      residual:"rE=|Xs|^2-1 and rF=Xs dot T, weighted squared rE^2+2*rF^2",
      radialQuadrature:"Gauss2 on union of original phase/Hermite breaks and spline knots",
      derivative:"complete state and primitive first-moment derivatives, fixed physical s and u",
      continuousMetricOrGeometryCertified:false,strongTargetComplete:false}
  };
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR196MetricProvider};
