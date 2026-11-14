# Finite actual-body consumer for raw independent three-field data

## Scope and execution status

The entry scripts/fd2d-metric-raw-body-screen.py consumes an explicitly selected
field array packet and its actual solver report. It uses the recovered native
reader of R129 and the fixed-material 24-state reconstruction of R124.

It is a finite floating postprocessor, not a new BVP solve, continuous interval
consumer, seam proof, or completed closed-surface certificate. A completed
diagnostic may show arbitrarily poor metric, curvature, or cut agreement.
Such values are retained. There is no threshold that silently marks a bad
field geometrically acceptable.

The first source draft was created as a Git blob before the local executor
returned. The current local source additionally permits 8 or 16 angles for
a small implementation smoke run; the default actual finite screen uses 32
angles, with 64 available. Exact current source bytes are bound by every run
report. The first-draft blob is not assigned to a revised local source.

Execution receipts and measured values belong to the actual run reports.
Until a run completes, none is inferred from this note or from an earlier
reader check.

## 1. Inputs and definition

The required command is:

~~~
python scripts/fd2d-metric-raw-body-screen.py \
  --field <actual-field.npz-or-npz.gz> \
  --report <actual-solver-report.json> \
  --out-prefix notes/<fresh-output-stem> \
  --angles 32
~~~

The field packet contains the binary nodes, all independent n/m/l correction
coefficients, and the complete parameter vector. The selected file SHA256
must occur as an identity in the supplied report, for example field,
initial_checkpoint, or latest_checkpoint. This prevents silently associating
a field with an unrelated report.

The report supplies candidate_input with its SHA, radial_chart.reference_T,
angular_chart.blend_interval, and the explicit profile_kind and tail_kind.
The physical coast length used by this postprocessor is the saved field's
last parameter. A report's recorded radial actual_T can refer to its initial
checkpoint, so that value is recorded without substituting it for the selected
field's actual parameter.

Historical v1 reports have the explicit documented legacy-coast/signed-bubble/
balanced-seed schema contract. Historical v2 reports already select the
profile and tail; their fixed central base was balanced_seed. These limited
compatibility mappings are recorded in the output. Unknown missing factory
choices cause an input error; a missing choice is never guessed to be positive.

When exact central moment/mean packets are bound in the report, those packets
are resolved by SHA and used. Otherwise the current published fixed geometry
defaults are explicitly selected and bound in the new definition, with a note
that the source report did not supply that closure. No absent provenance is
invented. The selected field coefficients, not another checkpoint's central
parameters, define the central curve.

Candidate paths from a previous executor can be relocated by basename into
the local topic notes directory only when the bytes match the stated SHA.
No change to physical g or the field is made while resolving a path.

## 2. What is integrated

The native reader defines piecewise-linear shared-node Fourier corrections
plus the full central and developable liftings. It preserves independent l
and does not reconstruct l by dividing by n.

At fixed physical material angle u, write the frame columns as (e1,e2,N) and
\[
 A=\begin{pmatrix}0&0&-l\\0&0&-m\\l&m&0\end{pmatrix},
 \qquad \alpha=(m,-l,0).
\]
The actual map satisfies
\[
 F_s=FA,\qquad X_s=Fe_1^{\rm coord}.
\]
Here the last e1 is the constant first coordinate vector. The material angle
is held fixed while the computational angle is inverted through the recorded
moving chart. All radial right-hand sides in the computational variable x
are multiplied by J=S_x.

The state contains
\[
 [X_3,F_9,r_3,b_3,v_3,q_3],
\]
where r=vee(F^T F_u), b=F^T X_u, v=r_u, and q=b_u. Besides the frame and
position equations, it integrates
\[
\begin{aligned}
 r_s&=r\times\alpha+\alpha_u,&
 b_s&=-\alpha\times b+r\times e_1,\\
 v_s&=v\times\alpha+r\times\alpha_u+\alpha_{uu},&
 q_s&=-\alpha\times q-\alpha_u\times b+v\times e_1.
\end{aligned}
\]
The actual saved central curve supplies the initial position and frame,
with r=(a0*n_core,0,0), b=(0,a0,0), v=(a0*(n_core)_u,0,0), and q=0.

The implementation uses DOP853 separately on every span in the union of
actual P1 nodes, physical scalar-profile breaks, angular blend endpoints,
and lifting transition endpoints. It takes the final state of one span
as the initial state of the next. No frame orthogonalization, projection
of the correction, or deletion of modes modifies the ODE.

The default tolerances are numerical solver settings only. They are not
rigorous error bounds for the continuous ODE. The finite RHS allocation is
also an execution setting; exhausting it records an incomplete diagnostic,
not a mathematical obstruction.

## 3. Actual Cartesian two-jets and metric

The state gives
\[
\begin{aligned}
 X_s&=Fe_1,&X_u&=Fb,&X_{ss}&=F(0,0,l)^T,\\
 X_{su}&=F(r\times e_1),&
 X_{uu}&=F(r\times b+q).
\end{aligned}
\]
The normal is computed from the actual Cartesian cross product,
\[
 N_X=\frac{X_s\times X_u}{|X_s\times X_u|}.
\]
It is not replaced by the auxiliary frame normal. The difference from that
frame normal and the numerical frame orthogonality defect are both reported.

Use target-scaled tangent vectors t1=X_s, t2=X_u/a. The actual normalized
Gram matrix is
\[
 I=\begin{pmatrix}
 \langle t_1,t_1\rangle&\langle t_1,t_2\rangle\\
 \langle t_1,t_2\rangle&\langle t_2,t_2\rangle
 \end{pmatrix}.
\]
Its relative metric error is the spectral norm of I-Id. The sampled minimum
Gram eigenvalue is retained as a diagnostic. No target-metric equality is
inserted into the computation.

The second form in this target-scaled coordinate basis is
\[
 II=\begin{pmatrix}
 \langle N_X,X_{ss}\rangle&
 \langle N_X,X_{su}\rangle/a\\
 \langle N_X,X_{su}\rangle/a&
 \langle N_X,X_{uu}\rangle/a^2
 \end{pmatrix}.
\]
It must be normalized by the actual first form before taking principal
curvatures. Simply taking the eigenvalues of II, or of the auxiliary
independent matrix (l,m,n), would be incorrect for a residual-bearing map.

## 4. Stable actual principal-curvature computation

Let E1=t1/|t1| and E2=N_X cross E1. Then
\[
 [t_1,t_2]=[E_1,E_2]R,\qquad
 R=\begin{pmatrix}r_{11}&r_{12}\\0&r_{22}\end{pmatrix},
\]
where
\[
 r_{11}=|t_1|,\quad r_{12}=\langle E_1,t_2\rangle,\quad
 r_{22}=\langle E_2,t_2\rangle>0
\]
at an immersed oriented point. Thus I=R^T R and the actual shape matrix
in the induced orthonormal tangent basis is
\[
 S_X=R^{-T}II R^{-1}.
\]
Its two eigenvalues are the actual principal curvatures.

This follows from the bilinear-form change of basis
II=R^T S_X R. Computing R from actual tangent vectors avoids the cancellation
in a scalar determinant of a nearly singular Gram matrix. If the actual
tangent or oriented area vanishes numerically, the diagnostic records that
failure instead of fabricating a normal or curvature.

The output separately records the auxiliary formal eigenvalues of
\[
 \begin{pmatrix}n&m\\m&l\end{pmatrix}.
\]
Those values are useful to compare a finite branch merit with the reconstructed
map; they are not substituted for the actual curvatures.

Outward support is also measured as -X dot N_X about the original coordinate
origin, with that origin explicitly stated. This sampled number is not a
reach or global-star-shapedness certificate.

## 5. One cut registration, then all Cartesian jets

At the final cut, the postprocessor evaluates its own selected tail family
with the saved tail coefficients and the same physical material u values.
Tail positions are quadrature evaluations of the stated generating integrals;
that quadrature is recorded but not interval-certified here.

A single position-only proper Kabsch fit sends the tail cut toward the prefix
cut. If centered tail and body rows are A and B and
\[
 A^TB=U\Sigma V^T,
\]
put
\[
 Q=V\,\operatorname{diag}(1,1,\operatorname{sign}\det(VU^T))\,U^T,
 \qquad t=\overline X_{\rm body}-Q\overline X_{\rm tail}.
\]
It minimizes the sampled position least-squares objective over proper
rotations. The determinant correction excludes a reflection. The source
centered singular values and a finite rank diagnostic are retained.

The same Q and t are then used for every cut comparison:
\[
 X_{\rm tail}^{\rm reg}=QX_{\rm tail}+t,\qquad
 (\partial^\gamma X_{\rm tail})^{\rm reg}
   =Q\partial^\gamma X_{\rm tail}\quad(1\le|\gamma|\le2).
\]
There is no separate derivative fit, per-angle rigid motion, material-angle
shift, or phase optimization.

The comparison includes X, X_s, X_u, X_ss, X_su, and X_uu, plus the oriented
actual normal. Absolute vector maxima, RMS errors, the worst sampled material
angles, and target-scaled derivative errors are retained. Upper-prefix s and
tail s both point toward decreasing radius at this cut; the reader already
converts the computational derivative to that physical meridian coordinate.

A nonzero horizontal translation or a tilted Q e_z is neither deleted nor
declared zero by symmetry. Both oriented z-axis tilt and unoriented vertical
axis tilt are reported. A fitted position match does not imply agreement of
first or second derivatives. The same-u jet errors reveal what remains unpaid.

The auxiliary cut n/m/l difference and the actual saved cut correction are
also reported separately. An exact lifting function does not by itself force
a nonzero saved correction to vanish.

## 6. Outputs, failures, and resumption evidence

The output stem creates:

* a report JSON with source/input hashes, explicit choices, finite sample
  totals and per-radius rows, solver status, and any actual exception;
* a native-field definition JSON binding the selected mathematical field;
* a progress JSONL with closed span endpoints and running diagnostic extrema;
* a small atomically replaced endpoint-current NPZ identifying the last fully
  integrated endpoint and the exact input field/report hashes;
* a complete samples archive containing the 24-state samples, actual Cartesian
  jets, Gram and second form, normals, principal curvatures, and auxiliary fields;
* on successful arrival at the cut, a cut archive containing original,
  registered, and difference arrays for every Cartesian jet.

The archive helper applies the repository's existing lossless compression
and sharding rules. Saved samples are approximate values of the ODE map;
they are not a complete solver dense polynomial and do not define a replacement
physical surface.

A process exit of zero means only that the requested finite diagnostic and
its output completed. It does not imply small metric, acceptable curvature,
or a matched seam. A numerical/input failure produces an honest failed or
partial report and preserves completed samples whenever output remains possible.
No missing interval is silently filled.

The minimal smoke run may use --angles 8 or --angles 16 on a known bad old
initializer solely to exercise data binding, the actual frame path, the Gram/
curvature calculation, and the cut comparison. Such an initializer is not
promoted to a research candidate. A later actual K15 field is consumed with
its own identity and a new output stem.

## 7. Actual local execution after recovery

The independently constructed R128 fixture was run with 64 offset material
angles, a positive-Bernstein tail with eight equal .9 controls, and the declared
proper rotation Qz(.23) Qy(.37) Qx(-.17) plus translation (.13,-.2,.7).
It naturally completed with exit 0 in session 26063, chunk 52259c.
The report is
notes/2026-11-12-fd2d-metric-raw-body-geometry-check-02-report.json.

Its actual metric error was 6.66e-16, actual principal-curvature error
1.78e-15, fitted rotation error 4.44e-16, translation error 2.22e-16,
and the maximum error among all six Cartesian jets was 1.30e-15.
The deliberately nonzero tilt and horizontal translation were retained.
An independent R128 implementation agreed on all Cartesian jets to 3.34e-14.
These are floating implementation checks, not continuous geometric bounds.

The first checker invocation failed before numerical evaluation because of
a Python syntax typo. Its actual exit 1, source snapshot, and failure record
are preserved; it produced no numerical result.

The known bad old jac01/M3 initializer was then genuinely consumed with
8 material angles over all 105 integration spans and 211 radial samples.
Session 86835, chunk af544b, naturally completed with exit 0 in 635.01 seconds.
Its complete report is
notes/2026-11-12-fd2d-metric-raw-body-jac01-smoke-01-report.json.

This old initializer remains decisively unsuitable: the finite actual metric
error reached 31.0444 and the actual curvature reached 2118.8167. Its cut
position error after the one fitted proper rigid transformation was .43816,
and the maximum X_u, X_su, X_uu errors were about 4.775, 61.34, and 280.04.
The report records these values rather than treating a completed program
as successful geometry. The complete sample and cut arrays, final endpoint
checkpoint, actual definition, progress log, and real exit receipt are saved.

The successfully exercised body source has SHA256
27abc54c5c170ac2074428c2726e4077a3d57e25d15ea0e0a5f1606c56185827.
No further integration of this bad old initializer is needed. A later
candidate is to be consumed under its own field/report identity and fresh
output stem.


