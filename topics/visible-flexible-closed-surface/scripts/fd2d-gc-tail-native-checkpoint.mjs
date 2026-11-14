// Lossless native zero signs alongside ordinary JSON state arrays.
// Numerical maps/roots are not called or altered by this module.
import {createHash} from 'node:crypto';
import {endianness} from 'node:os';

const SCHEMA='fd2d-native-shooting-state-identity-v1';
function packed(states){
 const width=states[0]?.length;
 if(!Number.isInteger(width)||width<1||states.some(s=>s.length!==width||!Array.from(s).every(Number.isFinite)))
  throw Error('Native checkpoint states must be finite and rectangular');
 return {width,values:Float64Array.from(states.flatMap(s=>Array.from(s)))};
}
function bytes(values,order=endianness()){
 const out=Buffer.from(values.buffer,values.byteOffset,values.byteLength);
 if(order===endianness())return out;
 if(!['LE','BE'].includes(order))throw Error('Invalid native checkpoint byte order');
 return Buffer.from(out).swap64();
}
const sha=value=>createHash('sha256').update(value).digest('hex');

export function nativeCheckpointIdentity(states){
 const {width,values}=packed(states),negativeZeroIndices=[];
 for(let i=0;i<values.length;i++)if(Object.is(values[i],-0))negativeZeroIndices.push(i);
 return {schema:SCHEMA,width,nodeCount:states.length,byteOrder:endianness(),
  packedStatesSHA256:sha(bytes(values)),packedInputSHA256:sha(bytes(values.subarray(width))),
  negativeZeroIndices,scope:'Native IEEE-754 state identity; zero signs are storage metadata, not a change to the real-valued finite equations.'};
}

export function restoreNativeCheckpoint(checkpoint){
 const id=checkpoint?.nativeStateIdentity;
 if(!id)return checkpoint; // Historical JSON remains a labelled legacy input.
 if(id.schema!==SCHEMA||!Array.isArray(id.negativeZeroIndices))throw Error('Invalid native checkpoint identity');
 const states=checkpoint.states.map(row=>Array.from(row)),{width,values}=packed(states);
 if(width!==id.width||states.length!==id.nodeCount)throw Error('Native checkpoint dimensions differ');
 for(const i of id.negativeZeroIndices){
  if(!Number.isInteger(i)||i<0||i>=values.length||values[i]!==0)throw Error('Native checkpoint sign applies to a nonzero or missing coordinate');
  values[i]=-0;states[Math.floor(i/width)][i%width]=-0;
 }
 if(sha(bytes(values,id.byteOrder))!==id.packedStatesSHA256||sha(bytes(values.subarray(width),id.byteOrder))!==id.packedInputSHA256)
  throw Error('Native checkpoint bit identity differs after zero-sign restoration');
 return {...checkpoint,states,...(checkpoint.rawNode?{rawStates:checkpoint.rawNode.map(n=>states[n])}:{})};
}
