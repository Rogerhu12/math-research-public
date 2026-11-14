// Actual periodic development and induced metric from the full R16 identities.
// The supplied two-jets must come from one height and one radial material metric.
// This uses the pi-antiperiodic canonical gauge gamma=0 and center=0, justified
// for the even cosine Fourier family. It retains mean/period numerical errors.
function fft(re,im,inverse=false){
 const n=re.length;if((n&(n-1))!==0)throw Error('power-of-two angular grid required');
 for(let i=1,j=0;i<n;i++){let bit=n>>1;for(;j&bit;bit>>=1)j^=bit;j^=bit;if(i<j){[re[i],re[j]]=[re[j],re[i]];[im[i],im[j]]=[im[j],im[i]];}}
 for(let len=2;len<=n;len*=2){const a=(inverse?2:-2)*Math.PI/len,wr=Math.cos(a),wi=Math.sin(a);for(let start=0;start<n;start+=len){let ur=1,ui=0;for(let j=0;j<len/2;j++){const p=start+j,q=p+len/2,vr=re[q]*ur-im[q]*ui,vi=re[q]*ui+im[q]*ur,ar=re[p],ai=im[p];re[p]=ar+vr;im[p]=ai+vi;re[q]=ar-vr;im[q]=ai-vi;const nr=ur*wr-ui*wi;ui=ur*wi+ui*wr;ur=nr;}}}
 if(inverse)for(let i=0;i<n;i++){re[i]/=n;im[i]/=n;}
}
export function periodicPrimitiveReal(values){
 const n=values.length,re=Float64Array.from(values),im=new Float64Array(n);fft(re,im);re[0]=im[0]=0;
 for(let j=1;j<n;j++){if(j===n/2){re[j]=im[j]=0;continue;}const k=j<=n/2?j:j-n,a=re[j],b=im[j];re[j]=b/k;im[j]=-a/k;}
 fft(re,im,true);return re;
}
export function actualMetricFromDarbouxJets(geometry,perAngle,{returnCoordinates=false}={}){
 const {r,E}=geometry,n=perAngle.length,omega=new Float64Array(n),Omega=new Float64Array(n),rho=new Float64Array(n),alpha=new Float64Array(n),beta=new Float64Array(n);
 let phi=0,omegaRMean=0,minDelta=Infinity;
 for(let j=0;j<n;j++){const v=perAngle[j],S=r*r-v.ut*v.ut,Delta=E*S-r*r*v.ur*v.ur,sd=Math.sqrt(Delta),C=r+v.ur*v.utt-v.ut*v.ut/r;
 if(!(S>0&&Delta>0))throw Error('actual development projection failed');rho[j]=Math.sqrt(S);alpha[j]=sd/rho[j];beta[j]=-v.ur*v.ut/rho[j];omega[j]=r*r*C/(S*sd);phi+=omega[j]/n;omegaRMean+=r*r*v.ur*(v.urt-v.ut/r)/(S*sd)/n;Omega[j]=v.darboux*E*E*r**4/(Delta*sd);minDelta=Math.min(minDelta,Delta/(r*r));}
 const pOmega=periodicPrimitiveReal(Omega),pOmegaTheta=periodicPrimitiveReal(omega),ax=new Float64Array(n),ay=new Float64Array(n),tx=new Float64Array(n),ty=new Float64Array(n),cx=new Float64Array(n),cy=new Float64Array(n),zeta=phi-1;let mx=0,my=0,maX=0,maY=0;
 for(let j=0;j<n;j++){const psi=2*Math.PI*j/n+pOmegaTheta[j],c=Math.cos(psi),s=Math.sin(psi);ax[j]=alpha[j]*c-beta[j]*s;ay[j]=alpha[j]*s+beta[j]*c;tx[j]=-rho[j]*s;ty[j]=rho[j]*c;cx[j]=-rho[j]*pOmega[j]*c-zeta*ay[j];cy[j]=-rho[j]*pOmega[j]*s+zeta*ax[j];mx+=tx[j]/n;my+=ty[j]/n;maX+=ax[j]/n;maY+=ay[j]/n;}
 const pcx=periodicPrimitiveReal(cx),pcy=periodicPrimitiveReal(cy),px=returnCoordinates?periodicPrimitiveReal(tx):null,py=returnCoordinates?periodicPrimitiveReal(ty):null;
 let metric=0,metricRR=0,metricRT=0,metricTT=0,maxRadialError=0;
 for(let j=0;j<n;j++){const v=perAngle[j],rx=ax[j]+pcx[j],ry=ay[j]+pcy[j],sx=tx[j]-mx,sy=ty[j]-my,A=(rx*rx+ry*ry+v.ur*v.ur)/E-1,B=(rx*sx+ry*sy+v.ur*v.ut)/(r*Math.sqrt(E)),C=(sx*sx+sy*sy+v.ut*v.ut)/(r*r)-1;metricRR=Math.max(metricRR,Math.abs(A));metricRT=Math.max(metricRT,Math.abs(B));metricTT=Math.max(metricTT,Math.abs(C));metric=Math.max(metric,Math.abs((A+C+Math.hypot(A-C,2*B))/2),Math.abs((A+C-Math.hypot(A-C,2*B))/2));maxRadialError=Math.max(maxRadialError,Math.hypot(pcx[j],pcy[j]));}
 return {actualMetricRelativeOperatorError:metric,actualMetricRelativeRR:metricRR,actualMetricRelativeRT:metricRT,actualMetricRelativeTT:metricTT,angularHolonomyResidual:Math.abs(zeta),translationPeriod:2*Math.PI*Math.hypot(mx,my),radialGaugeMeanError:Math.hypot(maX,maY),angularPhaseMeanDerivative:omegaRMean,minProjectedDelta:minDelta,maximumRadialCurlCorrection:maxRadialError,...(returnCoordinates?{coordinates:Array.from({length:n},(_,j)=>[px[j],py[j],perAngle[j].height]),radialDerivatives:Array.from({length:n},(_,j)=>[ax[j]+pcx[j],ay[j]+pcy[j],perAngle[j].ur]),angularDerivatives:Array.from({length:n},(_,j)=>[tx[j]-mx,ty[j]-my,perAngle[j].ut])}:{}),scope:'R16 actual periodic development, evaluated angularly; numerical derivative identities assume the supplied jets arise from the same radial solution.'};
}
