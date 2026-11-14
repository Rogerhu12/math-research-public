"use strict";
/* Consume the actual saved binary axes. No seed search, ODE or full chart. */
const fs=require("fs"),path=require("path"),crypto=require("crypto");
const base=require("./fd2d_R187_saved_ellipse_normalization_exact.cjs");
const sha=x=>crypto.createHash("sha256").update(x).digest("hex");
function arg(k){const i=process.argv.indexOf(k);if(i<0||i+1===process.argv.length)throw Error("missing "+k);return process.argv[i+1];}
function frac(x){return [BigInt(x[0]),BigInt(x[1])];}
function cmp(a,b){const x=a[0]*b[1]-b[0]*a[1];return x<0n?-1:x>0n?1:0;}
function boundLe(x,b){return cmp(frac(x.upper),b)<=0;}
function boundGe(x,b){return cmp(frac(x.lower),b)>=0;}
function display(x){return {lower:Number(x.lower[0])/Number(x.lower[1]),upper:Number(x.upper[0])/Number(x.upper[1])};}
const inputPath=arg("--input"),checkpointPath=arg("--checkpoint"),out=arg("--out");
const inputBytes=fs.readFileSync(inputPath),checkpointBytes=fs.readFileSync(checkpointPath);
const input=JSON.parse(inputBytes),checkpoint=JSON.parse(checkpointBytes);
const evidence=input.bindings.actual_axis_evidence;
if(sha(checkpointBytes)!==evidence.sha256||checkpointBytes.length!==evidence.bytes)throw Error("actual checkpoint identity mismatch");
for(const key of ["A","B"])if(input.axes[key+"_bits"].replace(/^0x/,"")!==checkpoint.centralSeed.binary64["raw"+key])throw Error("saved axis bits mismatch");
if(checkpoint.bindings.candidateSHA256!==input.bindings.source_and_candidate.candidate_sha256)throw Error("accurate a0 candidate mismatch");
const sourcePath=path.join(__dirname,"fd2d_R187_saved_ellipse_normalization_exact.cjs"),sourceBytes=fs.readFileSync(sourcePath);
if(sha(sourceBytes)!=="efdd34fd43db8da8b11e3cd0a319b04e11d068a36931b99cf0d8adb124a3ed45")throw Error("frozen exact consumer mismatch");
const started=process.hrtime.bigint(),actual=base.certifySavedEllipseNormalization(input),elapsed=Number(process.hrtime.bigint()-started)/1e9;
const checks={
 central_A_ge_32_over_25:boundGe(actual.normalized_A,[32n,25n]),
 central_B_positive:cmp(frac(actual.normalized_B.lower),[0n,1n])>0,
 central_axis_gap_ge_4_over_5:boundGe(actual.normalized_axis_gap,[4n,5n]),
 central_axis_gap_le_4_over_5:boundLe(actual.normalized_axis_gap,[4n,5n]),
 entire_central_curve_kappa_max_le_5:boundLe(actual.entire_central_curve_curvature_maximum,[5n,1n])
};
const result={schema:"fd2d-R197-actual-strong-gap08-saved-axis-consumption-v1",completed:true,
 execution:{runtime:process.version,OS_subprocess_started:true,arithmetic_seconds:elapsed},
 identities:{source:{path:"scripts/fd2d_R187_saved_ellipse_normalization_exact.cjs",bytes:sourceBytes.length,sha256:sha(sourceBytes)},
 driver:{path:"scripts/"+path.basename(__filename),bytes:fs.statSync(__filename).size,sha256:sha(fs.readFileSync(__filename))},
 input:{path:"notes/"+path.basename(inputPath),bytes:inputBytes.length,sha256:sha(inputBytes)},
 checkpoint:evidence},
 actual_input:input,actual_result:actual,exact_comparisons:checks,
 scope:"Actual R196 gap .8 branch central saved-axis ellipse, accurately normalized by the fixed B32 a0; entire central-curve curvature only.",
 material_angle_chart_recomputed:false,full_surface_or_visible_motion_certified:false,
 unchanged_finite_field_claimed:false,
 note:"The accurate definition uses the exact dyadic saved A/B and the exact perimeter; finite displayed normalization is only an observation."};
fs.writeFileSync(out,JSON.stringify(result,null,2)+"\n");
console.log(JSON.stringify({completed:true,arithmetic_seconds:elapsed,comparisons:checks,
 mean_radius:display(actual.perimeter_mean_radius),normalized_A:display(actual.normalized_A),normalized_B:display(actual.normalized_B),
 gap:display(actual.normalized_axis_gap),gap_minus_requested:display(actual.gap_minus_requested),
 curvature_min:display(actual.entire_central_curve_curvature_minimum),curvature_max:display(actual.entire_central_curve_curvature_maximum)}));
