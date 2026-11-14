# R196 strong gap 0.8: explicit zero initialization, eight actual accepts, and N128 check

This is a finite design search with the complete R190/R191 metric and actual principal-curvature objective. It is not a solution or a continuous certificate. The radius spline is still a design variable, so these steps are not refinement on one already frozen physical metric.

## Inputs and initialization

The nonuniform basis has 30 radial functions, 7 angular modes, 16 parameters per radial block, and one global cut-height coefficient: 481 parameters in total. Its exact rational knots are stored in every checkpoint. They came from the earlier R196 injection of 7/60, 9/60 and 11/60 into the 27-function uniform basis.

Changing the requested central gap from 0.05 to 0.8 produces a new central seed. The stored raw ellipse semiaxes are A=1.3620341722637315 and B=0.5620341722637314, binary64 bits 3ff5cae4581e83b7 and 3fe1fc2f16a36dd4. The precise numerical normalization and material-curve semantics are retained in centralSeed, rather than treating a floating normalization of 1 as an exact perimeter statement.

The old small-gap coefficient vector was first tried as an explicitly new strong-gap baseline. Its initial squared objective was 36334.9564259789 with sampled minimum immersion 0.0000452961092930102 and maximum curvature 310182.12507704814. After two actual accepted steps it still had objective 789.189898337535 and curvature 12938.92412763849. Those calculations remain in strong-gap08-branch-00/01; they are not discarded or relabelled as iterations of the zero branch.

The all-zero coefficient vector with the same new central seed was then evaluated independently. Its objective was 3.795231031769102, minimum immersion 0.04847186579573192, and maximum curvature 219.30067081025177. This much better new baseline was explicitly selected and its acceptance counter reset to zero. The baseline switch is not an Armijo acceptance.

## Eight actual accepted steps

All eight steps used the frozen R195 v2 band solver with half-bandwidth 4 and its original Armijo policy. The guide was 9.5, curvature weight 0.01, and nodeShare 0.5. Each trial used the full current value; no parameter projection, omitted curvature derivative, tiny off-band deletion, or reused trial value was introduced.

| Accepted step | Armijo alpha | Complete squared objective | Maximum metric residual on metric grid | Maximum actual sampled curvature | Minimum sampled immersion |
| --- | --- | --- | --- | --- | --- |
| 1 | 0.5 | 2.54892570861 | 2.896200286 | 137.2687637 | 0.05427537703 |
| 2 | 1 | 1.20287053791 | 2.813289394 | 88.47238556 | 0.02488911039 |
| 3 | 1 | 0.411408816368 | 1.528476807 | 37.16751780 | 0.02527911696 |
| 4 | 1 | 0.319459378727 | 1.430959915 | 71.85058923 | 0.05199542707 |
| 5 | 1 | 0.118389103948 | 1.121563429 | 26.45656208 | 0.1954582510 |
| 6 | 0.5 | 0.0712061575343 | 0.6998836670 | 24.74616223 | 0.4475863737 |
| 7 | 1 | 0.0453314043966 | 0.3545042086 | 31.74373663 | 0.6881930701 |
| 8 | 0.5 | 0.0311397658721 | 0.3093018930 | 26.95243725 | 0.8005677533 |

The actual JavaScript computation time reported by the eight steps totals 70349 ms. These calculations ran in pure V8. Their execution records intentionally have no operating-system exit code. The subsequent file writes were separate real Python subprocesses with exit 0.

The N64 final objective is 0.031139765872066787, consisting of metric part 0.02022903104860773 and curvature penalty 0.010910734823459054. Its radius coefficient maximum is 0.01820516343090281, within the original 0.4 parameter bound. The stored sufficient radius lower bound is 0.7817948365690972. This does not establish metric accuracy, reach, or held displacement.

## Same complete field at N128

The required verification copied the entire final coefficient vector, exact radial knots, central seed, and K=7 unchanged, then changed only the angular evaluation setting from N64 to N128. It performed one fresh value evaluation, without a normal matrix or another solve. The call was:

```javascript
const probe = {...state, options: {...state.options, angles: 128}};
const value = runtime.providers(probe).curvature.value(state.z);
```

The actual evaluation took 1589 ms. The metric and curvature radial grids respectively retained 184 and 277 points; the quarter-period angular grid increased from 17 to 33 nodes.

At N128 the objective is 0.031166618356033543; metric part 0.020229037291237557 and curvature part 0.010937581064795986. The maximum metric-grid residual is 0.31758394687125724, at s=0.5297330249894753 and u=0.5399612373357456. The curvature grid sees residual 0.31876913951133634. The largest principal-curvature magnitude is 26.952437247803694 at s=0.28452183830339467, u=pi/2, a physical knot. The metric residual at that curvature peak is only 0.011181090528084914, so the two dominant defects occur at different locations. Minimum sampled immersion is 0.800567753336584.

The finite cut-height offset is -0.2036853172019306; the B32 finite background height gives the numerical cut height 0.5398516720542774. This is a numerical endpoint evaluation, not an accurate-bound certificate and not a paid fixed-cap window.

## Scope and resumption

The selected checkpoint is strong-gap08-zero-04.json, SHA256 145f72e8facb8b1f7d9f962d0d7e1f63f952625ab423a76bcf76cc156d408f16. It includes all 481 coefficients, explicit rational knots, raw seed bits, source Git blobs, objective options, backend identity, damping, and every actual trial record. Earlier zero-01/02/03 checkpoints contain the states after 2/4/6 accepts. The N128 report binds the exact final file.

The source runtime is scripts/fd2d-nonuniform-refined-branch-R196.cjs. Its providers(checkpoint) and runBatch(checkpoint,count,onCheckpoint) are the actual APIs used. The same frozen metric/curvature sources have already passed the R196 full-value, parameter-JVP and position-two-jet comparison.

The strict central-ellipse consumer being closed by metric_closure is independent evidence about this fixed raw seed. It must not be substituted for bounds on the rest of this surface. No whole-core held ball, full metric certificate, global reach, fixed-cap graft, or strong completion is asserted here.
