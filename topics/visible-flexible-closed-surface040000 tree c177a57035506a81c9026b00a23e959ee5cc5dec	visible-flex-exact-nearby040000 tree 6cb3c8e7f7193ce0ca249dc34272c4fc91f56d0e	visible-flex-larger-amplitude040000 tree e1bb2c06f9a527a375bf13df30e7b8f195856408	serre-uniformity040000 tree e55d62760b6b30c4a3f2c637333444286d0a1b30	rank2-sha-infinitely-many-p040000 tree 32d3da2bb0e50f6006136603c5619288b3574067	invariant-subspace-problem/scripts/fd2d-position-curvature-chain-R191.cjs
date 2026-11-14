/* R191: actual Gram/II chain and spectral curvature hinge.
 * The residual has three symmetric-matrix rows. Its squared norm is
 * sum_i max(0,abs(kappa_i)-guide)^2 exactly in real arithmetic.
 */
"use strict";
function createR191Algebra(){
  const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
  const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
  const add=(a,b)=>a.map((x,j)=>x+b[j]);
  function curvature(j){
    const U=j.Xs,V=j.Xu,W=cross(U,V),w2=dot(W,W),E=dot(U,U),F=dot(U,V),G=dot(V,V);
    if(!(E>0&&w2>0))throw Error("Actual position is not immersed at a curvature point");
    const w=Math.sqrt(w2),N=W.map(x=>x/w);
    const L=dot(N,j.Xss),M=dot(N,j.Xsu),NN=dot(N,j.Xuu),r=F/E,P=w2/E;
    const A=L/E,B=(M-r*L)/w,C=(NN-2*r*M+r*r*L)/P;
    if([A,B,C].some(x=>!Number.isFinite(x)))throw Error("Nonfinite actual second form");
    const h=(A+C)/2,d=(A-C)/2,R=Math.hypot(d,B),eigenvalues=[h+R,h-R];
    return {E,F,G,W,w2,w,N,L,M,NN,r,P,S:[A,B,C],eigenvalues,kappa:Math.max(...eigenvalues.map(Math.abs))};
  }
  function variation(j,p,v){
    const dW=add(cross(v.Xs,j.Xu),cross(j.Xs,v.Xu)),dw=dot(p.N,dW);
    const dN=dW.map((x,k)=>(x-p.N[k]*dw)/p.w);
    const dE=2*dot(j.Xs,v.Xs),dF=dot(v.Xs,j.Xu)+dot(j.Xs,v.Xu);
    const dL=dot(dN,j.Xss)+dot(p.N,v.Xss),dM=dot(dN,j.Xsu)+dot(p.N,v.Xsu),dNN=dot(dN,j.Xuu)+dot(p.N,v.Xuu);
    const dr=(dF-p.r*dE)/p.E,dP=p.P*(2*dw/p.w-dE/p.E);
    const dA=(dL-p.S[0]*dE)/p.E;
    const dB=(dM-dr*p.L-p.r*dL-p.S[1]*dw)/p.w;
    const dnum=dNN-2*dr*p.M-2*p.r*dM+2*p.r*dr*p.L+p.r*p.r*dL;
    const dC=(dnum-p.S[2]*dP)/p.P;
    return [dA,dB,dC];
  }
  function hinge(S,guide){
    if(!(Number.isFinite(guide)&&guide>0))throw Error("Positive finite numerical curvature guide required");
    const [A,B,C]=S,h=(A+C)/2,d=(A-C)/2,r=Math.hypot(d,B),lp=h+r,lm=h-r;
    const scalar=x=>x>guide?[x-guide,1]:x< -guide?[x+guide,1]:[0,0];
    const [fp,sp]=scalar(lp),[fm,sm]=scalar(lm),SQ2=Math.SQRT2;
    let Q,apply;
    if(sp===sm&&((lp>guide&&lm>guide)||(lp< -guide&&lm< -guide)||(lp>=-guide&&lp<=guide&&lm>=-guide&&lm<=guide))){
      const slope=sp,offset=slope?(lp>guide?-guide:guide):0;
      Q=[slope*A+offset,slope*B,slope*C+offset];
      apply=H=>[slope*H[0],SQ2*slope*H[1],slope*H[2]];
    }else{
      if(!(r>0))throw Error("Unexpected spectral branch at a repeated eigenvalue");
      const alpha=(fp-fm)/(2*r),u=d/r,v=B/r,bar=(fp+fm)/2;
      Q=[bar+alpha*d,alpha*B,bar-alpha*d];
      apply=H=>{
        const dh=(H[0]+H[2])/2,dd=(H[0]-H[2])/2;
        const hp=dh+u*dd+v*H[1],hm=dh-u*dd-v*H[1];
        const xp=(sp-alpha)*hp,xm=(sm-alpha)*hm;
        return [alpha*H[0]+xp*(1+u)/2+xm*(1-u)/2,
          SQ2*(alpha*H[1]+(xp-xm)*v/2),
          alpha*H[2]+xp*(1-u)/2+xm*(1+u)/2];
      };
    }
    const residual=[Q[0],SQ2*Q[1],Q[2]];
    return {residual,squared:dot(residual,residual),eigenvalues:[lp,lm],apply,
      threshold:lp===guide||lp===-guide||lm===guide||lm===-guide,
      threshold_derivative_convention:"inactive slope zero at exact +/-guide; generalized derivative, not a false smoothness claim"};
  }
  return {curvature,variation,hinge};
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR191Algebra};
