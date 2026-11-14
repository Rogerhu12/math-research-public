// Read-only diagnostic for an already exported integrated-Fr tail.
// Samples the explicit finite map; this is not a continuous certificate.
import fs from 'node:fs';
import path from 'node:path';
import {gunzipSync} from 'node:zlib';
import {pathToFileURL,fileURLToPath} from 'node:url';
import {parseArgs} from 'node:util';
const {values,positionals}=parseArgs({allowPositionals:true,options:{'source-root':{type:'string'},'raw-cell':{type:'string',default:'0'},'angles':{type:'string',default:'64'},'out':{type:'string'}}});
if(positionals.length!==1||!values['source-root'])throw Error('manifest --source-root ROOT required');
const manifest=positionals[0],meta=JSON.parse(fs.readFileSync(manifest,'utf8')),root=path.resolve(values['source-root']);
process.env.VISIBLE_FLEX_SOURCE_ROOT=root;process.env.CLOSING_TAIL_CACHE=path.join(root,'topics/large-amplitude-twist-flex/scripts');
const here=path.dirname(fileURLToPath(import.meta.url));
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(here,'closing_weighted_tail.mjs')));
const {subdividePhysical}=await import(pathToFileURL(path.join(here,'950f-tail-subdivision.mjs')));
const {createFastSplitFluxMomentumTailEngine}=await import(pathToFileURL(path.join(process.env.CLOSING_TAIL_CACHE,'f6tail_fast_split_flux_engine.mjs')));
const {relativeSurfaceGeometry}=await import(pathToFileURL(path.join(process.env.CLOSING_TAIL_CACHE,'f6tail_relative_development.mjs')));
const p=meta.parameters,physical=createRecalibrationFactory(p).assemble(),stages=subdividePhysical(physical,meta.settings.depth,p.shootingParts??1),raw=+values['raw-cell'];
const info=meta.files.find(v=>v.rawCell===raw),file=fs.existsSync(info.path)?info.path:path.join(path.dirname(manifest),path.basename(info.path));
const buf=gunzipSync(fs.readFileSync(file)),data=new Float64Array(buf.buffer,buf.byteOffset,buf.byteLength/8),C=meta.format.coefficientCount,stride=meta.format.stride;
const pm=meta.format.planarModes,hm=meta.format.heightModes,P=pm.length,N=+values.angles;
const angles=Array.from({length:N},(_,j)=>{const t=2*Math.PI*j/N;return {theta:t,p:pm.map(m=>[Math.cos(m*t),Math.sin(m*t)]),h:hm.map(m=>[Math.cos(m*t),Math.sin(m*t)])};});
function combine(a,b,L,t){
 const out=new Float64Array(3*C);for(let k=0;k<C;k++){
  const u0=a[2+C+k],u1=b[2+C+k],v0=L*a[2+2*C+k],v1=L*b[2+2*C+k],mid=b[2+3*C+k],A=16*mid-8*(u0+u1)-2*(v0-v1);
  const z0=u0,z1=v0,z2=-3*u0+3*u1-2*v0-v1+A,z3=2*u0-2*u1+v0+v1-2*A,z4=A;
  out[k]=a[2+k]+L*t*(z0+t*(z1/2+t*(z2/3+t*(z3/4+t*z4/5))));
  out[C+k]=z0+t*(z1+t*(z2+t*(z3+t*z4)));
  out[2*C+k]=(z1+t*(2*z2+t*(3*z3+t*4*z4)))/L;
 }return out;
}
function vectors(c,q){
 const v=Array.from({length:5},()=>[0,0,0]);
 for(let k=0;k<P;k++){const m=pm[k],[co,si]=q.p[k],a=c[k],b=c[C+k],d=c[2*C+k];v[0][0]+=b*co;v[0][1]+=b*si;v[1][0]-=m*a*si;v[1][1]+=m*a*co;v[2][0]+=d*co;v[2][1]+=d*si;v[3][0]-=m*b*si;v[3][1]+=m*b*co;v[4][0]-=m*m*a*co;v[4][1]-=m*m*a*si;}
 for(let k=0;k<hm.length;k++){const m=hm[k],[co,si]=q.h[k],a=c[P+k],b=c[C+P+k],d=c[2*C+P+k];v[0][2]+=b*co;v[1][2]-=m*a*si;v[2][2]+=d*co;v[3][2]-=m*b*si;v[4][2]-=m*m*a*co;}return v;
}
const cells=stages.cells.map((c,n)=>({...c,n,low:c.profiles[0](0).r,high:c.profiles[0](1).r})).filter(c=>c.rawCell===raw).sort((a,b)=>a.low-b.low);
const report={scope:'sampled diagnostic of an explicit finite map only',manifest:path.resolve(manifest),rawCell:raw,angles:N,metric:0,fullTensor:0,curvature:0,worstMetric:null,worstTensor:null,top:[]};
let ix=0;
for(let j=0;j<info.rows-1;j++){
 const a=data.subarray(j*stride,(j+1)*stride),b=data.subarray((j+1)*stride,(j+2)*stride),L=b[0]-a[0],mid=(a[0]+b[0])/2;
 while(ix<cells.length-1&&mid>cells[ix].high)ix++;const cell=cells[ix],profile=cell.profiles[0];
 const engine=createFastSplitFluxMomentumTailEngine({modes:p.modes,spacing:p.spacing,quadrature:Math.max(256,meta.settings.angularNodes),mu:cell.mu,orientation:p.orientation,projectionFloor:p.projectionFloor});
 let best=0,details=null;
 for(const t of [.125,.25,.5,.75,.875]){
  const r=a[0]+t*L;let lo=0,hi=1;for(let q=0;q<48;q++){const xm=(lo+hi)/2;if(profile(xm).r<r)lo=xm;else hi=xm;}const x=(lo+hi)/2,g=engine.geometry(profile,x),coef=combine(a,b,L,t);
  for(const q of angles){const v=vectors(coef,q),z=relativeSurfaceGeometry(g,q.theta,...v);const d={row:j,stage:cell.n,x,t,r,L,theta:q.theta,metric:z.metric,fullTensor:z.fullTensorFrobeniusBound,curvature:z.actualCurvature,backgroundDrDx:g.drdx,backgroundWr:g.w*g.dlogwdx/g.drdx,firstNorm:Math.hypot(...v[0]),secondNorm:Math.hypot(...v[2]),nodeFrDifference:Math.max(...pm.map((_,k)=>Math.abs(b[2+C+k]-a[2+C+k])))};
   if(z.metric>report.metric){report.metric=z.metric;report.worstMetric=d;}if(z.fullTensorFrobeniusBound>report.fullTensor){report.fullTensor=z.fullTensorFrobeniusBound;report.worstTensor=d;}report.curvature=Math.max(report.curvature,z.actualCurvature);if(z.fullTensorFrobeniusBound>best){best=z.fullTensorFrobeniusBound;details=d;}
  }
 }
 report.top.push(details);
}
report.top.sort((a,b)=>b.fullTensor-a.fullTensor);report.top=report.top.slice(0,10);
if(values.out)fs.writeFileSync(values.out,JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
