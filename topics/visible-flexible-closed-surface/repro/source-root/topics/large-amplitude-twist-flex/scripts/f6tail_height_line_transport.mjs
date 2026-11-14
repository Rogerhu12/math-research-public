// Projective propagation in physical (f,f') variables; no large transfer matrix.
// Selected finite ideal deep line only. Not an exact nonlinear infinite DN.
export function idealMomentumGraph(mode,R,a){if(mode===2)return 0;const nu=mode*mode*(mode*mode-1)/12,rho=2**a,alpha=1+1/R,t00=1-alpha*nu*R,t10=(-nu*(1+R)+alpha*nu*nu*R)/rho,t11=(1-alpha*nu)/rho,tr=t00+t11,det=1/rho,lambda=.5*(tr-Math.sqrt(tr*tr-4*det));return t10/(lambda-t11);}
export function propagatePhysicalHeightLine(tail,{mode=6,linearFar=40,steps=1024,referenceRadius=tail.parameters.rCut,retainNodes=false}={}){
 const sigma=tail.parameters.orientation,a=tail.parameters.a,R=tail.parameters.R,rho=2**a,farCell=tail.cells[linearFar-1],far=farCell.profiles[0](0),wFar=Math.exp(far.logw),graph=idealMomentumGraph(mode,R,a),slope=mode*mode/far.r+sigma*Math.sqrt(12)*farCell.mu*graph/(far.r**8*wFar),scale=mode*mode/referenceRadius;
 let y=[1,slope/scale],logNorm=0;const norm0=Math.hypot(...y);y=y.map(v=>v/norm0);logNorm+=Math.log(norm0);const nodes=[];
 function node(n,g){const w=Math.exp(g.logw),frOverF=scale*y[1]/y[0],mu=n===0?rho*tail.cells[0].mu:tail.cells[n-1].mu,canonicalGraph=sigma*g.r**8*w*(frOverF-mode*mode/g.r)/(Math.sqrt(12)*mu);return {n,r:g.r,w,slope:frOverF,second:g.dlogwdx/g.drdx*(mode*mode/g.r-frOverF),canonicalGraph,unitDirection:[...y],logHeightGain:logNorm+Math.log(Math.abs(y[0])),heightGainSign:Math.sign(y[0])};}
 nodes[linearFar]=node(linearFar,far);
 function rhs(v,g){return [g.drdx*scale*v[1],-g.dlogwdx*(v[1]-mode*mode*v[0]/(g.r*scale))];}
 for(let n=linearFar-1;n>=0;n--){const cell=tail.cells[n];for(const profile of cell.profiles)for(let k=0;k<steps;k++){const x=k/steps,h=1/steps,g0=profile(x),gm=profile(x+h/2),g1=profile(x+h),a=rhs(y,g0),b=rhs(y.map((v,j)=>v+h*a[j]/2),gm),c=rhs(y.map((v,j)=>v+h*b[j]/2),gm),d=rhs(y.map((v,j)=>v+h*c[j]),g1);y=y.map((v,j)=>v+h*(a[j]+2*b[j]+2*c[j]+d[j])/6);const norm=Math.hypot(...y);if(!(norm>0&&Number.isFinite(norm)))throw Error('physical line propagation overflow');y=y.map(v=>v/norm);logNorm+=Math.log(norm);}nodes[n]=node(n,cell.profiles.at(-1)(1));}
 return {mode,linearFar,steps,...nodes[0],...(retainNodes?{nodes}:{}),scope:'Finite actual-profile projective physical-height line with selected ideal far condition.'};
}

export function buildProjectivePhysicalTailGraph(tail,{modes=4,spacing=6,linearFar=40,linearSteps=1024}={}){
 const lines=Array.from({length:modes},(_,j)=>propagatePhysicalHeightLine(tail,{mode:spacing*(j+1),linearFar,steps:linearSteps,retainNodes:true})),graphs=Array.from({length:linearFar+1},()=>new Float64Array(modes)),gains=Array.from({length:linearFar},()=>new Float64Array(modes));
 for(let j=0;j<modes;j++)for(let n=0;n<=linearFar;n++){const a=lines[j].nodes[n];graphs[n][j]=a.canonicalGraph;if(n<linearFar){const b=lines[j].nodes[n+1],log=a.logHeightGain-b.logHeightGain+4*Math.log(b.r/a.r),sign=a.heightGainSign*b.heightGainSign;gains[n][j]=sign*Math.exp(log);if(!(Number.isFinite(gains[n][j])&&Math.abs(gains[n][j])>1e-250))throw Error('projective Dirichlet height chart vertical');}}
 return {graphs,gains,lines,parameters:{modes,spacing,linearFar,linearSteps,scope:'Actual physical normalized-vector finite tail lines; selected ideal far condition remains.'}};
}
