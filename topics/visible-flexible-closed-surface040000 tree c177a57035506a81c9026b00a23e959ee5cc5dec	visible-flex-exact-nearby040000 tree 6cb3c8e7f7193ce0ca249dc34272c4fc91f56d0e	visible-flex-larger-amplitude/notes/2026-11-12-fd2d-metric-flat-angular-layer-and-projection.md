# Flat-cut angular layers and finite correction projection

## Status and recovered scope

The mathematical expansions below follow from the explicit flat-prefix
phase bridge and the exact R128 tail. The finite screens concern an
initial guess, not a solution of Gauss--Codazzi or a completed surface.

After the executor became unavailable, the diagnostic sources were
reconstructed with new identities:

* scripts/fd2d-metric-flat-initializer-angular-screen.py,
  Git blob b96c0f0b72f8e72c9f73f1a550314f032100db9e;
* scripts/fd2d-metric-flat-initializer-fixed-angle-screen.py,
  Git blob 52d3e9eeb7d0e5bf81f8504ff3b85d0e5049e1a2.

The old numerical results in section 5 are a historical execution record.
They must be recovered from a published commit or genuinely rerun before
their arrays/JSON can be cited as available artifacts. The reconstructed
programs do not write these old numbers into a report. They recalculate
from the actual stored trajectory and bind the resulting source/input
bytes and new output identities.

The physical candidate is
notes/2026-11-12-fd2d-flat-cut-prefix-v1-coast-compatible-candidate.json,
SHA256 a92b552f70bcc26c97f16261fbc78fac10c1daad6d72eafc8063dcb093cdd147.
The initial-function source is the accepted partial trajectory
notes/2026-11-12-fd2d-flat-prefix-balanced-ivp-01-trajectory.npz.gz,
SHA256 db7614138c5f55b77e23f04849af02c75db36a277064b64f684a8da574c68c51.
That source reaches approximately physical s=.809. Its explicit continuation
to the cut is an initial guess only. It is not a solved whole prefix.

## 1. Actual radial orders at the flat endpoint

The final phase_bridge in this candidate is cubic, with length \(L=.04\),
initial phase \(-1.45\), final phase \(-\pi/2\), and zero phase derivatives
at both ends. It is not a quintic phase bridge.

Let \(d=s_c-s\), \(t=d/L\), and
\(\Delta=\pi/2-1.45>0\). The exact cubic phase is
\[
 \phi(s)=-\pi/2+\epsilon(d),\qquad
 \epsilon(d)=\Delta(3t^2-2t^3).
\]
For the rotational reference,
\[
 a_s=\sin\phi=-\cos\epsilon,\qquad
 a=a_c+d+O(d^5).
\]
The inward normal curvatures satisfy
\[
\begin{aligned}
 l_{\rm ref}&=-\phi_s
   =\frac{6\Delta}{L^2}d+O(d^2),\\
 n_{\rm ref}&=\frac{\cos\phi}{a}
   =\frac{3\Delta}{a_cL^2}d^2+O(d^3),\\
 K_g&=l_{\rm ref}n_{\rm ref}
   =\frac{18\Delta^2}{a_cL^4}d^3+O(d^4).
\end{aligned}
\]
For \(a_c=.8\), the three leading coefficients are approximately
452.9862, 283.1164, and 128247.8 respectively. The formulas, rather than
those rounded decimals, specify the coefficients.

Proof: differentiate the displayed cubic. Since
\(\cos\epsilon=1+O(d^4)\), integration of \(a_s=-1+O(d^4)\) gives
\(a=a_c+d+O(d^5)\). Also
\(\cos\phi=\sin\epsilon=\epsilon+O(d^6)\).
Multiplication gives the stated Gaussian-curvature order.

Consequently the relevant orders are \(l=O(d)\), \(n=O(d^2)\),
\(K_g=O(d^3)\). The earlier informal expectation
\(l=O(d^2),n=O(d^3),K_g=O(d^5)\) came from a different phase order
and is not applicable to this actual candidate.

These orders are compatible with a flat cut. They do not make \(n>0\)
a required coordinate condition for the three-field system of R129.

## 2. The exact developable tail's angular edges

For the R128 tail, put \(c_0=.34\), \(a_c=.8\),
\(w=a_c-c_0=.46\), and
\[
 \alpha(y)=\operatorname{sgn}(y) A
 S_9\!\left(\frac{|y|-c_0}{w}\right),
 \qquad S_9'(q)=630q^4(1-q)^4
\]
on the active transition, with the stated constant extensions.
With physical material angle \(u\),
\[
 (n,m,l)=\kappa(a_c\sin u)
       (\cos^2u,-\sin u\cos u,\sin^2u),\quad
 \kappa=\alpha'.
\]
This is a full analytic function. Projecting its three entries separately
does not preserve its rank-one Gauss identity. The actual lifting keeps
the function intact.

At the first unbent edge
\[
 u_c=\arcsin(c_0/a_c)=\arcsin(.425),
\]
let \(\eta=u-u_c>0\). Taylor expansion gives
\[
 n_{\rm tail}(u)=C_4\eta^4+O(\eta^5),\qquad
 C_4=\frac{630A\,a_c^4\cos^6u_c}{w^5}.
\]
For the screened value \(A=.9\), \(C_4\) is approximately 6203.0.
Indeed \(a_c\sin(u_c+\eta)-c_0=a_c\cos u_c\,\eta+O(\eta^2)\);
the four powers come from \(q^4\), and the other two cosine factors
come from the \(n\) component.

At \(u=\pi/2\), by contrast,
\(a_c-a_c\sin u=O((u-\pi/2)^2)\). The factor \((1-q)^4\)
makes \(\kappa=O((u-\pi/2)^8)\), and the extra \(\cos^2u\)
makes \(n_{\rm tail}=O((u-\pi/2)^{10})\).

Neither zero set is a singularity of the independent \((l,m,n)\)
Gauss--Codazzi interface.

## 3. The initial guess has a thin angular layer

The initializer transports the last accepted central shape by the
rotational \(n\) scale, then blends the exact cut tail. Near the cut,
\[
 n_{\rm init}(d,u)=N_2(u)d^2+\beta(d)n_{\rm tail}(u)+O(d^3),
 \qquad \beta(d)=1+O(d^3).
\]
Here \(N_2(u)\) includes the actual transported angular shape, so it is
not silently replaced by the rotational constant.

Where \(N_2(u_c)>0\), balance of the two leading terms at an unbent
edge gives
\[
 |\eta|\asymp
 \left(\frac{N_2(u_c)}{C_4}\right)^{1/4}\sqrt d .
\]
For the pure rotational coefficient the prefactor would be approximately
.4622. The actual transported function supplies its own prefactor.

The Gauss-compatible initialization
\(l_{\rm init}=(K_g+m_{\rm init}^2)/n_{\rm init}\)
contains a \(K_g/n_{\rm init}\) contribution of the form
\[
 d\,f(\eta/\sqrt d)
\]
to leading order at this edge. Its angular derivative is of order
\(\sqrt d\), whereas its second angular derivative can remain of order
one on shrinking angular neighborhoods. Thus small pointwise amplitude
near the cut does not imply that a fixed finite Fourier order resolves
all angular derivatives there.

At the \(\pi/2\) zero, the analogous balance
\(d^2\asymp\eta^{10}\) has width \(d^{1/5}\). These scaling statements
describe this particular initial function, not an obstruction to a
compatible immersion.

The unprojected initial function and its finite correction representation
are different objects. The piecewise-linear finite correction with shared
radial nodes has continuous angular derivatives across those nodes and
gives the \(C^2\) ODE map proved in the raw-native definition note.
One must not transfer any unproved uniform differentiability at a shrinking
layer from the unprojected guess to a claimed exact solution.

## 4. What the screens actually compute

At \(T=.02,A=.9\), each screen uses the actual stored prefix on its
stored interval. Beyond that interval, it uses precisely the explicit
extension of the raw initializer:
\[
 n=n_{\rm last}(u)\frac{n_{\rm ref}(s)}{n_{\rm ref}(s_{\rm last})}
        +\beta(s)n_{\rm tail}(u),\qquad
 m=(1-\beta)m_{\rm last}(u)+\beta m_{\rm tail}(u).
\]
The initial \(l\) is the corresponding Gauss-compatible value, with the
same explicit zero convention used at the fully flat endpoint.

The full lifting evaluates the tail formula at the current radius
\(a(s)\), whereas the continuation guess blends its cut port at radius
\(a_c\). Subtracting the lifting therefore leaves a genuine angular
correction; the analytic lifting does not automatically remove all sharp
features of this particular initial guess.

For each \(K=7,15,31\), the correction is projected in the actual raw
solver work grid into \(K+1\) even cosine entries for \(n,l\) and \(K\)
odd sine entries for \(m\). The central and cut correction values of this
initializer are explicitly zero. The complete lifting is then restored.

At every actual radial node, 2048 equally spaced computational angles
are used to measure
\[
 G=nl-m^2-K_g.
\]
The even modes through \(2K\) are separately retained from the sampled
Fourier transform, and the difference from the full sampled function is
reported. This measures omitted modes; it does not bound the unsampled
angular continuum.

The second screen holds \(u=U_*(\xi)\) at every radius, instead of the
radially moving chart. It retains the identical physical initial
function and the same radial mesh, including the former blend knots.
This is a change of computational coordinate, not a change of physical
metric. Its saved coefficient arrays have that explicit fixed chart;
reading them as moving-chart arrays would define a different field.

## 5. Historical observations before environment loss

The moving-chart screen actually completed as session 71246, chunk
885d7f, exit 0, approximately 70.45 seconds. Its old output stem was
notes/2026-11-12-fd2d-metric-flat-initializer-angular-screen-01.
At 113 actual radial nodes and 2048 angular points, the observed values
were:

| K | sampled minimum n | sampled max absolute G | retained low-mode max | omitted-mode max |
| --- | ---: | ---: | ---: | ---: |
| 7 | -.1054748433 | 6.6888533364 | 2.0576568188 | 5.6398138495 |
| 15 | 0 | 1.3333187377 | .4595090676 | 1.1099889122 |
| 31 | 0 | .3590407798 | .0663055096 | .3449026511 |

The \(K=7\) reconstructed correction differed from the then-saved root
initializer by at most \(5.33\times10^{-15}\), with identical nodes
and parameters. On the root solver's own work grid, the screen reproduced
minimum \(n=-.0966573599\) and maximum \(|G|=6.6491132318\).
This located the reported negative initial \(n\) in the finite projection,
rather than in the complete initial formula.

The dense \(K=7\) negative point occurred at approximately
\[
 x=s=1.26360320099,\quad a=.88017987475,\quad
 a_s=-.98040329073,\quad K_g=1.52196923238,
\]
with \(u=\xi=5.81992310924\). The projected \((n,m,l)\) was
approximately \((-.105475,-.191588,8.47088)\), whereas the complete
initial value at that point was
\((.147729,.0223915,10.30583)\).

The largest observed Gauss error for all three orders occurred earlier,
near
\[
 x=s=1.14614490990,\quad a=.97471709869,\quad
 a_s=-.54281219596,\quad K_g=5.85914408471 .
\]
At this radial point and \(u=\pi/2\), even the complete, unprojected
initial function had \(n\approx .2420609602\), \(m\approx0\),
\(l\approx24.2052418515\). Thus the formal curvature problem of this
initial function is not explained entirely by angular truncation.
Raising the angular order can reduce projection defects while leaving
an unsuitable branch geometry.

The fixed-seed-angle screen actually completed as session 57325,
chunk 1ce3c9, exit 0, approximately 72.21 seconds. The observed comparison
was worse for this initial function:

| K | sampled minimum n | sampled max absolute G |
| --- | ---: | ---: |
| 7 | -.0549711894 | 8.8275731183 |
| 15 | -.2937737211 | 6.7806508821 |
| 31 | 0 | 1.2462927524 |

These observations support keeping the moving chart for the present
branch search. They do not establish an optimal coordinate theorem.
The old source/report identities are deliberately not assigned to the
reconstructed sources or to future rerun outputs.

## 6. Practical consequence and reproducible commands

The three-field equations permit the flat angular zeros without a
division by \(n\). Their finite search still needs enough angular
resolution to expose the full Gauss residual. A finite formal curvature
merit can help choose a branch whose actual curvature has a plausible
posterior budget. Neither step changes the original residual equations,
and neither creates a new final acceptance gate.

The recovered screens can be genuinely rerun from the topic directory:

~~~
python scripts/fd2d-metric-flat-initializer-angular-screen.py
python scripts/fd2d-metric-flat-initializer-fixed-angle-screen.py
~~~

Their default output stems end in recovery01. They perform no new
physical ODE or BVP solve. A completed rerun should be recorded with its
real exit, source hashes, report hashes, and array hashes by the publishing
process. Until that happens, the numerical table above remains an honest
historical record, not a substitute for missing files.
