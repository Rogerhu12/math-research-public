'use strict';
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const {createR187}=require('./fd2d-direct-position-tangent-lift-baseline-R187.cjs');
const {createR187Provider}=require('./fd2d-direct-position-metric-provider-R187.cjs');
const {createR190Provider}=require('./fd2d-direct-position-designed-metric-provider-R190.cjs');
const sha=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const [input,out]=process.argv.slice(2);if(!input||!out||fs.existsSync(out))throw Error('Use input state and new output report');
const t0=process.hrtime.bigint(),state=JSON.parse(fs.readFileSync(input));
const candidate=path.join(__dirname,'../notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json');
const bundle=JSON.parse(fs.readFileSync(candidate)),engine=createR187();
const old=createR187Provider(engine,bundle,state.options),p=createR190Provider(engine,bundle,state.options);
const z=Float64Array.from([...state.z,...Array(state.options.radialBasisCount).fill(0)]);
const d=Float64Array.from(z,(_,i)=>.003*Math.sin((i+1)*1.37));
const zeroOld=old.evaluate(state.z,{residuals:true,direction:d.slice(0,old.dimension)});
const zeroNew=p.evaluate(z,{residuals:true,direction:Float64Array.from(d,(_,i)=>i<old.dimension?d[i]:0)});
let embeddingF=0,embeddingJ=0;
for(let i=0;i<zeroOld.residuals.length;i++){embeddingF=Math.max(embeddingF,Math.abs(zeroOld.residuals[i]-zeroNew.residuals[i]));embeddingJ=Math.max(embeddingJ,Math.abs(zeroOld.jvp[i]-zeroNew.jvp[i]));}
for(let j=old.dimension;j<z.length;j++)z[j]=.003*Math.sin(j*.73);
const e=1e-6,a=p.evaluate(z,{residuals:true,direction:d});
const plus=p.evaluate(Float64Array.from(z,(v,i)=>v+e*d[i]),{residuals:true});
const minus=p.evaluate(Float64Array.from(z,(v,i)=>v-e*d[i]),{residuals:true});
let err2=0,norm2=0,max=0;
for(let i=0;i<a.jvp.length;i++){const fd=(plus.residuals[i]-minus.residuals[i])/(2*e),v=fd-a.jvp[i];err2+=v*v;norm2+=a.jvp[i]*a.jvp[i];max=Math.max(max,Math.abs(v));}
const report={schema:'R190-actual-designed-metric-provider-check-v1',input:{path:input,sha256:sha(input)},source:{path:__filename,sha256:sha(__filename)},providerSHA256:sha(path.join(__dirname,'fd2d-direct-position-designed-metric-provider-R190.cjs')),candidateSHA256:sha(candidate),runtime:'Node actual terminal execution',dimension:p.dimension,originalDimension:old.dimension,zeroEmbedding:{completeResidualMaximumDifference:embeddingF,oldDirectionMaximumDifference:embeddingJ},allColumnsNonzeroDirection:{eps:e,relativeL2:Math.sqrt(err2/Math.max(norm2,1e-300)),maximumAbsolute:max},sufficientRadiusLowerBound:a.conservativeRadiusLowerBound,seconds:Number(process.hrtime.bigint()-t0)/1e9,continuousCertificate:false,strongTargetComplete:false};
fs.writeFileSync(out,JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
if(embeddingF!==0||embeddingJ!==0||report.allColumnsNonzeroDirection.relativeL2>1e-6)throw Error('New complete derivative check failed');
