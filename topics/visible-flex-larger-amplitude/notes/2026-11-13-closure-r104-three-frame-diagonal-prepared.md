# Prepared third fixed frame for the R104 diagonal source kernels

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

Status: complete comparison argument and prepared independent Python
entry only. No AST/Python/Arb execution or improved numerical kernel
has been obtained for this version. The old v2 file is unchanged.

## Exact input and comparison

The input is the completed R104 tensor with SHA256
62156ade93e31729c7500e79dbc01c3f4267d1a89a2b7730af7fe1c6440df45a,
its actual exit-zero resource packet, the same 10793 true source
leaves in all 18 segments, and the original positive R68 frames.
Modes are exactly 94 and 96. Source materials remain
c_bg V_I^p, p=2,1,0, with c_bg=s+abs(ell).
Output is the physical strong norm with the two component
suprema added after each is taken, and with the factor 1+m.
There is no target V divisor in these diagonal rows.

On one source segment choose an exact constant b>=1 and set
u=(P,K/b). The original linear system in mode m is
$$
u_x=
\begin{pmatrix}
-s-\ell&imsb\\
-im\ell/b&-2\ell
\end{pmatrix}u
+\begin{pmatrix}0\\f/b\end{pmatrix}.
$$
Its Hermitian part is bounded above by
$$
\alpha_b(x)=\max(-s-\ell,-2\ell)
                 +\frac m2|sb+\ell/b|.
$$
Consequently q=||u||_2 is bounded by the scalar comparison
q_x<=alpha_b q+|f|/b. This remains true for complex mode amplitudes.
The source-only diagonal response starts from q=0 at the actual
source-segment boundary. It is not a bound for an arbitrarily
renormalized initial trace.

For exact outward frame changes the norm costs
max(1,b_previous/b_next). Both constant-segment strategies have
unit jumps inside their own source segment. The original R68
leafwise strategy continues to pay every actual frame change.

On each original true leaf the code uses an upper scalar alpha,
a nonnegative upper density d=c_bg V_I^p/b and the true source
width Delta. With z=alpha Delta, the exact comparison endpoint is
$$
q_1=e^z q_0+d\,\Delta\,\psi(z),\qquad
\psi(z)=\int_0^1 e^{tz}\,dt.
$$
The positive integral definition covers z=0 and negative z.
The constant-coefficient scalar solution can increase or decrease;
its maximum over the leaf is max(q_0,q_1).
The physical component bounds are P<=q and K<=bq. Their
whole-segment suprema are taken separately and multiplied by
1+m once.

These statements and all source densities are identical to v2.

## Why add a phase-only constant

Let the same complete source segment provide strict upper sums
$$
S\ge\int s\,dx>0,\qquad L\ge\int|\ell|\,dx\ge0.
$$
The old constant candidate minimizes only
$$
\log b+\frac m2(bS+L/b),\qquad b\ge1.
$$
It is useful for a particular homogeneous norm conversion, but
that log(b) factor is not intrinsic to the zero-initial source
response.

For a fixed b the source input has factor 1/b, whereas the
two physical output component bounds have combined factor 1+b.
For example the coarse full-segment forced upper bound is
$$
(1+1/b)\exp\left\{
 H+\frac m2(bS+L/b)
\right\}\int |f|\,dx,
$$
where H may be any certified integral upper bound for
max(0,-s-ell,-2ell). The use of a positive H and the full S,L
makes this a bound for every correctly ordered subinterval.
This displayed bound is an explanation of the scaling only;
the code does not substitute it for the actual leafwise kernel.

A natural independent candidate is therefore
$$
b_{\rm phase}=\max(1,\sqrt{L/S}).
$$
It minimizes the triangle phase bS+L/b on b>=1:
differentiate to obtain S-L/b^2, and include the endpoint b=1.
For L=0 the minimum is also b=1.

The implementation chooses an exact dyadic upper approximation
to this candidate. It then re-evaluates, on every actual leaf,
the signed quantity |sb+ell/b|, the diagonal coefficient, the
source factor 1/b, and the physical output factors. An upper
dyadic choice need not remain an optimizer; it is nevertheless
a valid fixed positive frame. No assertion that this candidate
optimizes the full forced comparison is needed or made.

Three independent valid bounds are therefore available:

1. The original R68 leaf frames.
2. The v2 constant candidate from its homogeneous surrogate.
3. The new constant phase candidate.

The old R104 signed-propagator bound is a fourth valid bound.
Taking the minimum separately for the P and K component
suprema is legitimate, since all candidates bound the same
response to the same source class. The two selected component
bounds are then added. This does not mix separate source
normalizations or evaluate different unknown fields.

## Preservation and execution contract

The new entry is
closure_middle_three_frame_diagonal_materials_v3.py.
It was obtained from the frozen v2 SHA256
3f7f4bb7bd26bbdb83b9df7a40e7fd9ca52cf0b6652f89e94978872cfb272ca7
using eleven unique text anchors. Those anchor checks were
actually performed in V8; they are not a Python syntax check.

The v3 adds one strategy and its exact dyadic provenance.
Both earlier strategies keep the same mathematical statements
and traversal order. All three material powers, all 18
diagonal blocks and the two current modes remain required.
The complete original off-diagonal source rows and both
initial-trace columns stay in the R104 package and are not
changed by this consumer.

There is no new Taylor flow, radial/source quadrature or ODE.
The source leaves are scanned twice as in v2. The declared
RSS observation stop is 98304 KiB, not an operating-system
memory limit. Each complete segment is saved under a fresh
prefix; any interruption or failed input identity remains
explicitly incomplete.

Before execution, the complete R68 primary SHA must be read
from the actual file and supplied with --frame-sha256. It is
not guessed from a producer SHA. Any restored path aliases
must resolve to the same files and pass their original hashes.
An unavailable old path is an input recovery issue, not a
failed mathematical inequality.

No nonlinear contraction, no smaller actual kernel, and no
coverage of modes beyond 94 and 96 follows from this prepared
entry alone. On execution, its completed diagonal rows can
replace only the corresponding old diagonal bounds, while
the original R104 off-diagonal and two initial-trace budgets
remain present.
