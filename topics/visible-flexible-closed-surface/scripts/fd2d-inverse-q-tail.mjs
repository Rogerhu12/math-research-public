/**
 * One new finite physical tail: replace the first N old cells by a single
 * inverse-Q bridge and keep all cells N,...,159 and the exact deep source.
 *
 * The original factory/configuration is not modified.  Old cell mu values
 * are retained only as canonical momentum scales; they impose no extra
 * physical condition on the new profile.  All displayed quadratures are
 * floating evaluations of the integral-defined metric, not certificates.
 */
import fs from 'node:fs';
import crypto from 'node:crypto';
import {createRecalibrationFactory as createBaseFactory} from './closing_weighted_tail.mjs';
import {boundTailPointCaches} from './fd2d-bounded-tail-point-cache.mjs';
import {createInverseQBridge} from './fd2d-metric-inverse-q-bridge.mjs';

const digest=x=>crypto.createHash('sha256').update(x).digest('hex');
const clone=x=>JSON.parse(JSON.stringify(x));
const sourceFiles=['fd2d-inverse-q-tail.mjs','fd2d-metric-inverse-q-bridge.mjs',
  'fd2d-metric-inverse-q-buffer.mjs','closing_weighted_tail.mjs',
  'closing_recalibrated_tail.mjs','fd2d-bounded-tail-point-cache.mjs'];
const sources=Object.fromEntries(sourceFiles.map(name=>[name,
  digest(fs.readFileSync(new URL('./'+name,import.meta.url)))]));
const GX=[.095012509837637440185,.28160355077925891323,.45801677765722738634,
  .61787624440264374845,.75540440835500303390,.86563120238783174388,
  .94457502307323257608,.98940093499164993260];
const GW=[.18945061045506849629,.18260341504492358887,.16915651939500253819,
  .14959598881657673208,.12462897125553387205,.095158511682492784810,
  .062253523938647892863,.027152459411754094852];
function rational(s,fallback){
  if(s===undefined)return fallback;
  if(typeof s==='number')return s;
  const p=s.split('/').map(Number);
  if(p.length>2||p.some(v=>!Number.isFinite(v))||p[1]===0)throw Error('Invalid rational endpoint');
  return p.length===1?p[0]:p[0]/p[1];
}
function integratePair(point,a,b,steps){
  const z=[0,0];
  for(let j=0;j<steps;j++){
    const lo=a+(b-a)*j/steps,hi=a+(b-a)*(j+1)/steps,c=(lo+hi)/2,h=(hi-lo)/2;
    for(let k=0;k<8;k++)for(const sign of [-1,1]){
      const g=point(c+sign*h*GX[k]),w=Math.exp(g.logw),weight=h*GW[k]*Math.abs(g.drdx);
      z[0]+=weight*Math.hypot(1,w);z[1]+=weight*w;
    }
  }
  return z;
}
function critical(point,grid){
  const zeros=[];let a=0,fa=point(0).dlogwdx;
  for(let j=1;j<=grid;j++){
    const b=j/grid,fb=point(b).dlogwdx;
    if(fa*fb<0){
      let lo=a,hi=b,fl=fa;
      for(let k=0;k<48;k++){
        const mid=(lo+hi)/2,fm=point(mid).dlogwdx;
        if(fl*fm<=0)hi=mid;else{lo=mid;fl=fm;}
      }
      zeros.push((lo+hi)/2);
    }
    if(fb===0&&fa!==0&&b<1)zeros.push(b);
    a=b;fa=fb;
  }
  return [...new Set(zeros)];
}

export function createRecalibrationFactory(config={}){
  if(config.schema!=='fd2d-inverse-q-full-tail-v1'||!config.baseConfig||!config.inverseQCandidate)
    throw Error('An explicit inverse-Q full-tail configuration is required');
  const baseConfig=clone(config.baseConfig),candidate=clone(config.inverseQCandidate),
    exact=candidate.exact_definition??{},N=exact.replace_outer_cells??config.replaceOuterCells,
    pieces=config.inverseQPiecesPerCell??9,grid=config.inverseQQuadratureGrid??1024;
  if(!(Number.isInteger(N)&&N>0&&N<baseConfig.protectCell&&baseConfig.orientation===1))
    throw Error('Replacement must leave at least one unchanged orientation +1 finite cell');
  if(!(Number.isInteger(pieces)&&pieces>0&&Number.isInteger(grid)&&grid>0))
    throw Error('Positive numerical subdivision and quadrature grids required');
  const inner=createBaseFactory(baseConfig);
  boundTailPointCaches(inner,baseConfig,{pointsPerEntry:config.pointCachePerEntry??8});
  const definition={schema:'fd2d-inverse-q-physical-definition-v1',baseConfig,candidate,
    suppliedFileBindings:clone(config.definitionFileBindings??{}),sources,
    replaceOuterCells:N,piecesPerCell:pieces,quadratureGrid:grid,
    innerPort:'Actual unchanged old cell N outer port; its r,w,w_r define the bridge inner data',
    metricDefinition:'Original finite profile for n>=N; positive-k inverse-Q bridge on the outer interval; exact source n>=protectCell unchanged',
    momentumConvention:'Old mu per labelled cell is a coordinate scale only; physical canonical momentum is continuous',
    endpointCalibration:'Integral-defined log w plus c S5, with c chosen for the prescribed outer w'};
  const definitionSHA=digest(JSON.stringify(definition));
  let cached=null;
  function assemble(controls=baseConfig.valleyControls,overrideAlpha=null){
    if(overrideAlpha!==null||JSON.stringify(controls)!==JSON.stringify(baseConfig.valleyControls))
      throw Error('This frozen inverse-Q metric has no beta/alpha mutation interface');
    if(cached)return cached;
    const old=inner.assemble(),oldPort=old.cells[N].profiles.at(-1)(1),
      left=oldPort.r,w0=Math.exp(oldPort.logw),wr0=w0*oldPort.dlogwdx/oldPort.drdx,
      numerical=candidate.numerical_port??candidate,
      right=rational(exact.right_rational,numerical.right),
      outer_w=rational(exact.outer_w_rational,numerical.outer_w),
      outerLog=exact.outer_logarithmic_radial_derivative==='-7/right'?-7/right:numerical.outer_logarithmic_radial_derivative;
    if(config.rCut!==right||config.wCut!==outer_w||Math.abs(config.width-(right-old.parameters.rCuff))>1e-15)
      throw Error('Top-level physical cut metadata disagree with the inverse-Q definition');
    const bridge=createInverseQBridge(candidate,{left,w0,wr0,right,outer_w,
      outer_logarithmic_radial_derivative:outerLog,grid});
    const zeros=critical(bridge.point,grid),cells=old.cells.slice();
    let newLength=0,newHeight=0,oldLength=0,oldHeight=0;
    for(let n=0;n<N;n++){
      const ta=(N-1-n)/N,tb=(N-n)/N,profiles=[];
      for(let j=0;j<pieces;j++){
        const a=ta+(tb-ta)*j/pieces,b=ta+(tb-ta)*(j+1)/pieces,h=b-a;
        const profile=x=>{
          const t=x===0?a:x===1?b:a+h*x,g=bridge.point(t);
          return {...g,drdx:h*g.drdx,d2rdx2:h*h*g.d2rdx2,
            dlogwdx:h*g.dlogwdx,d2logwdx2:h*h*g.d2logwdx2,
            wx:h*g.wx,wxx:h*h*g.wxx,inverseQT:t};
        };
        profile.integrationBreakpoints=zeros.filter(t=>t>a&&t<b).map(t=>(t-a)/h);
        profiles.push(profile);
      }
      const [meridianLength,heightSpan]=integratePair(bridge.point,ta,tb,Math.max(8,Math.ceil(grid/N/4)));
      newLength+=meridianLength;newHeight+=heightSpan;
      oldLength+=old.cells[n].meridianLength;oldHeight+=old.cells[n].heightSpan;
      const rStart=bridge.point(ta).r,rEnd=bridge.point(tb).r;
      cells[n]={...old.cells[n],profiles,beta:null,rStart,rEnd,localWidth:rEnd-rStart,
        meridianLength,heightSpan,profileKind:'inverse-Q-bridge',inverseQInterval:[ta,tb],
        sourceCalibrationReused:false};
    }
    const cut=cells[0].profiles.at(-1)(1),join=cells[N-1].profiles[0](0),
      joinWr=Math.exp(join.logw)*join.dlogwdx/join.drdx,cutWr=Math.exp(cut.logw)*cut.dlogwdx/cut.drdx,
      deep=cells.at(-1).profiles[0](0),baseStats=old.stats,
      stats={...baseStats,rCut:right,wCut:outer_w,width:right-old.parameters.rCuff,
        actualWidth:cut.r-deep.r,meridianLength:baseStats.meridianLength-oldLength+newLength,
        heightSpan:baseStats.heightSpan-oldHeight+newHeight,
        cutRadiusError:cut.r-right,cutSlopeError:Math.exp(cut.logw)-outer_w,
        cutSecondError:cutWr-outer_w*outerLog,
        minimumWarpWidth:null,baseMinimumWarpWidth:baseStats.minimumWarpWidth,
        alphaScope:'Only the unchanged original finite physical cells; the inverse-Q bridge uses affine radius',
        inverseQ:{definitionSHA,replaceOuterCells:N,metadata:bridge.metadata,
          actualInnerPort:{r:left,w:w0,wr:wr0},
          joinError:{r:join.r-left,w:Math.exp(join.logw)-w0,wr:joinWr-wr0},
          criticalPoints:zeros,criticalPointScope:'Sign-change roots of the smooth bridge log derivative, isolated numerically; not an interval root count',
          replacedMeridianLength:oldLength,replacedHeightSpan:oldHeight,
          bridgeMeridianLength:newLength,bridgeHeightSpan:newHeight,
          quadratureScope:'Floating 16-point composite Gauss; no continuous enclosure asserted'},
        originalBaseStats:baseStats};
    cached={...old,cells,stats,parameters:{...old.parameters,rCut:right,wCut:outer_w,
      width:right-old.parameters.rCuff,constructor:'fd2d_inverse_q_full_tail_v1',
      inverseQDefinition:definition,inverseQDefinitionSHA256:definitionSHA},
      sourceDefinition:'Original source and finite cells n>=N preserved; first N physical cells replaced by an integral-defined inverse-Q bridge.',
      inverseQBridge:bridge};
    return cached;
  }
  return {...inner,parameters:{...inner.parameters,inverseQDefinitionSHA256:definitionSHA},assemble,
    physicalCell(){throw Error('This frozen inverse-Q factory does not recalibrate individual physical cells');}};
}
