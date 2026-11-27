# Full $X_{\rm ns}^+(47)$: the eight actual CM tangent rows at $4513$

Status: **proved method; new public computation prepared, not yet executed**.

Date: 2026-11-27. Session: Astra-serre-24b8836b-20261126, O2 continuation.

Consumer: [full_p47_eight_CM_tangents.py](../scripts/full_p47_eight_CM_tangents.py).

This is a new finite input for the original full curve at $p=47$, at the good prime $q=4513$. It computes the tangent of $x-y$ at each of the eight already identified rational CM points, in the **same sixteen linear Hecke coordinates** as the certified Gaussian logarithm. It neither reruns that high logarithm nor repeats the complete auxiliary-point scan.

The output is only
$$
b_{y,i}=\frac{e_{y,i}}{\lambda_{4,i}}\in\mathbb F_{4513},
\qquad
\omega_i=e_{y,i}\,d(j-j(y))+\text{higher terms}.
\tag{T8.1}
$$
Here
$$
\lambda_{4,i}=4513^{-1}\log(B_{4513}u_{1728})(\omega_i)\pmod{4513}
$$
is consumed, with its original normalized eigenform hash, from
`notes/full-p47-CM-height-move-request.json`.
No period, CM factor, $23$, or $B_{4513}$ factor is silently removed. In particular, the tangent of $x-y$ has no extra factor $23$.

## 1. Exact finite scope and inputs

The eight old candidate ids and rational $j$-values are:

| Candidate | $j$ |
|---|---:|
| 0 | $0$ |
| 76 | $-3375$ |
| 77 | $-12288000$ |
| 100 | $16581375$ |
| 108 | $8000$ |
| 141 | $1728$ |
| 196 | $287496$ |
| 220 | $54000$ |

The original 235-label input is reconstructed by the existing
`original_p47_ell4513_cuspidal_transfer.py::candidate_input` and checked against its original character and coarse-point hashes. This is input reconstruction only. The consumer then calls `consume_known_cm` on exactly the eight already certified CM records. It does not enumerate the complete $4513$-point image, rescan all $j$-values, or infer a new global sieve result.

For each of these eight $j$-values it chooses one explicit short model
$$
E:\ y^2=x^3+Ax+B
$$
over $\mathbb F_q$. For generic $j$, the model is
$$
A=3j/(1728-j),\qquad B=2j/(1728-j).
$$
For $j=0$, it uses $A=0,B=1$. The Gaussian point uses the **already fixed original model and basis**
$$
A=343,\ B=0,\quad
P=(653,525),\ Q=(3860,232),\quad
i=95,\quad Q=iP,\quad e_{47}(P,Q)=2.
\tag{T8.2}
$$
The Gaussian case therefore does not enumerate its scalar Frobenius fiber of 1081 necklaces.

For the other seven models, a point count on that one model determines its trace. The existing exact Frobenius-matrix routine gives one necklace in an ordinary nonsplit fiber, or 25 necklaces in each of the two supersingular fibers. The original whole-label tag selects **exactly one** necklace. A zero or multiple match is a failed certificate, not permission to choose an arbitrary necklace. In particular, the supersingular discriminants $-7$ and $-28$ retain their actual distinct target tags.

The current request must pin:

- this script and this method;
- both root and topic README files;
- the original CM-height-move and auxiliary-transfer requests;
- the original Hodge, transfer, and 235-input scripts.

The direct original input scripts are additionally compared with their hashes in the consumed original requests. Historical result documents that have subsequently acquired new sections are not executed or used as arithmetic inputs.

## 2. Exact original Hodge and Hecke coordinates

The consumer calls
`full_p47_weight_one_Hodge_certificate.py::build_source`
with the certified 95 descriptors and the complete existing certificate. Thus it reconstructs and checks the original 95 logarithmic forms, all 23 cusp residue rows, the 73-dimensional holomorphic kernel, and the original $q$-jets. It does not repeat a candidate-basis search.

It reconstructs $T_2,T_3,T_5$ through that source's actual Tate formulas, and checks every original matrix hash together with
$$
H_2=T_2+2T_3+4T_5.
$$
For each of the sixteen certified roots of $H_2$, the one-dimensional left eigenspace is normalized by its first nonzero coordinate. The resulting vector must have exactly the old eigenform-coordinate SHA-256. Only then is the stored nonzero $\lambda_{4,i}$ attached to it.

If $K_{\rm hol}$ is the original $73\times95$ kernel matrix and $V_{\rm eig}$ is the resulting $16\times73$ matrix, the evaluated tangent vector is
$$
(e_{y,i})_i=V_{\rm eig}K_{\rm hol}(e_{y,\lambda})_{\lambda=1}^{95}.
\tag{T8.3}
$$
This uses the original full-curve Hodge lattice. No transported $X_0(47^2)$ integral basis is inserted.

## 3. Actual necklace, Weil pairing, and field conversion

The old transfer source writes the nonsplit Cartan as $\mathbb F_{47}[\sqrt5]$. The original Hodge source uses real/imaginary coordinates with $i^2=-1$. These are related by
$$
I=13J,\qquad 13^2\cdot5=-1\pmod{47}.
\tag{T8.4}
$$
Given a native basis $P_0,Q_0$ and the actual selected matrix
$$
J=\begin{pmatrix}a&b\\d&-a\end{pmatrix},
$$
the consumer sets $P=P_0$, $IP=13aP_0+13dQ_0$. It computes the actual Weil pairing, not a determinant-only surrogate. It then chooses $r,s\in\mathbb F_{47}$ with the required norm and replaces
$$
P\longmapsto rP+sIP,\qquad
IP\longmapsto -sP+rIP
$$
so that the actual Weil root is exactly $2$. This stays in the same Cartan necklace.

The old tag comparison retains its actual native Weil root. For each $J$, it uses the determinant $d$, the original $\psi_5$-orbit products, the original smoothing factor $\kappa_\chi$, and the full character root-change factor. It compares the resulting fixed-root tag with the certified old vector times the original circular-unit label. This is done before the Hodge $I=13J$ normalization.

All extension-field arithmetic uses the pinned python-flint field and its own modulus in a newly executed Python child process that never imports Sage. The parent process imports Sage only for the prime-field Hodge matrices. No process loads both native FLINT implementations. The sole conversion routine first checks
$$
a^q=a
$$
and then checks that every nonconstant coordinate in the actual flint basis is zero. Only its constant integer coordinate is converted to $\mathbb F_q$. There is no byte or coordinate reinterpretation between unrelated extension fields.

## 4. The actual weight-one values and short heat jets

The original short-model weight-one Eisenstein value $e(P)$ is computed from the same Khuri-Makdisi addition chain as the certified Gaussian source:
$$
1,2,4,5,10,11,22,23,46.
$$
The exact addition law is
$$
e(P+Q)=e(P)+e(Q)+m(P,Q).
$$
Since $46P=-P$, accumulated slopes determine $47e(P)$. Thus no arbitrary additive constant or CM period is chosen.

The consumer builds all 2208 nonzero torsion points and their $e$-values. It verifies distinctness, $e(-P)=-e(P)$, and compatibility of the complete grid with the actual Frobenius. The Gaussian and cubic stabilizers are additionally checked on this very grid.

The original heat flow is the full three-parameter flow. In particular,
$\partial e=A_2e/12-xe-y$ before specialization. At $A_2=0$, its relevant values are
$$
\partial A=6B,\qquad
\partial B=-\frac43A^2,\qquad
\partial A_2=4A,
$$
$$
\partial e=-xe-y,\quad
\partial x=2ey+2x^2+\frac43A,\quad
\partial y=3xy+e(3x^2+A).
$$
Consequently
$$
\partial^2e=-2e^2y-4x^2e-2Ae-2xy.
\tag{T8.5}
$$
The $A_2$ variable is not frozen when differentiating: the derivative of
$A_2e/12$ contributes $Ae/3$ to (T8.5). The script stores actual derivatives of orders $0,1,2$, not divided Taylor coefficients. Product derivatives therefore use the factor $2(\partial e)(\partial e')$.

For a certified descriptor $(a,c,d)$, with $\rho=d+ci$, the evaluated form is exactly
$$
G_{a,\rho}=
\sum_{x\ne0}
\left(
2^{aN(x)}e_xe_{\rho x}
+2^{-aN(x)}e_xe_{\bar\rho x}
\right).
\tag{T8.6}
$$
The two phases are kept separately. There are 46 norm classes and 24 half-vectors in each class; doubling the half-vector sum is valid because the product is even. Purely imaginary $\rho$ is retained. The point labels in the script are explicitly $(\operatorname{Re}x,\operatorname{Im}x)$, matching the existing Gaussian consumer.

Generic points need only order zero, the Gaussian point order one, and the cubic point order two. No high logarithmic moment is computed.

## 5. The coarse parameter and its exact constants

The actual parameter is
$$
z=j-j_{\rm CM}
$$
on the smooth coarse model at $q=4513$. At $j=0,1728$, the selected canonical CM Cartan contains the full elliptic stabilizer. The coarse $j$-map at this point has the normalization used below; one must not add a further stabilizer factor after the calculation.

Put $D=4A^3+27B^2$. The original Kodaira--Spencer formulas are
$$
{\rm KS}=\frac{9B\,dA-6A\,dB}{2D},
\qquad
dj=\frac{124416A^2B}{D}{\rm KS},
\qquad
\omega_F=F\,{\rm KS}.
\tag{T8.7}
$$

At a generic point this gives
$$
e_F=\frac{D}{124416A^2B}F.
\tag{T8.8}
$$

At the Gaussian point, hold $A$ fixed and write $F=f_1B+\cdots$. The original stabilizer forces $F=0$ at $B=0$. Directly from (T8.7),
$$
e_F=\frac{Af_1}{31104}
=-\frac{\partial F}{41472A}.
\tag{T8.9}
$$
The consumer verifies the constant term is zero for every one of the 95 descriptors before using this equation.

At the cubic point, hold $B$ fixed and write $F=f_2A^2+\cdots$. Here the stabilizer forces $F=\partial F=0$. Thus
$$
e_F=\frac{Bf_2}{4608}
=\frac{\partial^2F}{331776B}.
\tag{T8.10}
$$
The consumer verifies both vanishing conditions. These formulas include the actual coarse ramification. They are the same scale as R1103's tangent in $z=j-j(y)$, not a separate fine-level tangent.

## 6. Request, budget, and receipts

The new request has:

| Field | Value |
|---|---|
| execution_id | `full-p47-eight-CM-tangents-v2` |
| prime | $47$ |
| coefficient_prime | $4513$ |
| sage_version | `10.6` |
| python_flint_version | `0.9.0` |
| total_seconds | $600$ |
| reserve_seconds | $30$ |
| CM_candidate_ids | `[0,76,77,100,108,141,196,220]` |

It executes only in this public repository's Actions, under the request SHA-256 supplied by the workflow. The timer begins before arithmetic-source reconstruction and reserves the final 30 seconds. The Gaussian point is processed first, but the declared request always consists of all eight points.

Every completed point immediately prints a compact receipt containing:

- its exact CM id and rational $j$;
- selected model, extension-field degree and modulus, actual basis/Weil/root data, original tag and orbit hashes;
- original grid/heat-jet/tangent hashes;
- all sixteen $e_{y,i}$, consumed $\lambda_{4,i}$, and $b_{y,i}$.

The parent reconstructs the pinned Hodge/Hecke input, then starts a fresh interpreter with `sys.executable` and the same pinned script's `--field-worker` entry point. This is exec isolation, not a forked interpreter continuing to use the parent's loaded libraries. The child repeats the public-Actions and source/request gates, checks the parent pid, source commit and descriptor hash, and verifies the Linux loader map contains one wheel FLINT library and no Sage FLINT library before creating its first field. It imports no Sage module.

Only standard JSON crosses the pipe. The parent sends the original 95 descriptors, exact request/source pins and the shared absolute deadline. The child performs the original 235-input reconstruction and actual field calculations. Each completed point returns its 95 integer coordinates together with the unchanged marking/grid/heat hashes. The parent checks every coordinate is an integer in $[0,4512]$, checks the vector hash, projects immediately to the original 73 Hodge coordinates and 16 linear blocks, and prints that point's final receipt. It rejects duplicate, out-of-order or unsolicited points. The raw 95-vector is transmitted only through the runner pipe.

Both processes use the same monotonic absolute deadline, equal to the parent's start plus 570 seconds. The child cannot obtain a second 570-second budget. On timeout or failure the parent kills and reaps any surviving child within the reserved cleanup period. Child runtime metadata uses `field_worker_seconds` when forwarded, leaving the parent's `worker_seconds` key unambiguous.

The final receipt hashes the ordered eight completed records. A timeout or source mismatch preserves only the explicitly completed records. The emitter reserves `worker_seconds`, so imported payloads using `elapsed_seconds` cannot collide with that keyword.

The source, request, run/job ids and output hashes should be registered after the public execution. Reconstructible matrices, torsion grids and raw data are not committed.

## 7. What this calculation will and will not conclude

A successful run certifies only (T8.1) for these original eight points and sixteen original linear Hecke blocks. It does not compute the finite-field third-kind coefficient $\alpha$, the complete QC height polynomial, or a common-zero exclusion. Those require the separately specified sources and hypotheses of R1103, including the actual non-$q$ local-height terms.

No new numerical conclusion is asserted in this method before the public run.


## 8. The first run's native failure and the isolated retry

The first public run was `45965927561`, job `140394474708`, at source
`c24a2dd1f433f8fa459e1f9a13cde41d6c028d04`. It completed the original
Hodge/Hecke and 235-label input checks, then exited with code 139 before
printing any completed CM point. Its native stack shows
`flint/types/fq_default.abi3.so` calling Sage's
`/home/sage/sage/local/lib/libflint.so.19` at
`gr_generic_randtest_not_zero` during the first
`fq_default_ctx(4513,1)` construction. This identifies a collision between
the wheel's field extension and Sage's already loaded native FLINT runtime.

That run supplies no tangent value. The v2 retry changes only native-runtime
placement and the JSON protocol. The original mathematical field/grid/heat
functions, all eight target tags, the consumed 16 Gaussian logarithms and
the 600/30-second scope remain unchanged. The two native runtimes now live
in different processes; integer JSON is the only arithmetic bridge.
