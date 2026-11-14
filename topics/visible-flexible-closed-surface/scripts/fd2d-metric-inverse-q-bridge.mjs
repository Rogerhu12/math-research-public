/** Thin physical-factory interface; no source-profile mutation. */
import {createInverseQBuffer} from './fd2d-metric-inverse-q-buffer.mjs';

export function createInverseQBridge(candidate,options={}) {
  const port={};
  for(const key of ['left','w0','wr0','right','outer_w','outer_logarithmic_radial_derivative'])
    if(options[key]!==undefined)port[key]=options[key];
  if(options.r0!==undefined)port.left=options.r0;
  const buffer=createInverseQBuffer(candidate,{port,grid:options.grid??1024,calibrate:options.calibrate});
  function point(t) {
    const z=buffer.evaluate(t);
    return {r:z.r,drdx:z.drdx,d2rdx2:z.d2rdx2,
      logw:z.logw,dlogwdx:z.logwx,d2logwdx2:z.logwxx,
      w:z.w,wx:z.wx,wxx:z.wxx,wr:z.wr,wrr:z.wrr,E:z.E};
  }
  return {point,diagnostics:buffer.evaluate,metadata:buffer.metadata,coefficients:buffer.coefficients};
}
