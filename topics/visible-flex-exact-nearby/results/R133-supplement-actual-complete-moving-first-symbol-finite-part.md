# R133 supplement: the actual complete moving first-symbol finite part

2026-11-14, visible-exact-astra-0df / phase_inverse.

**Proved by an actual successful public Actions computation:** for the
exact continuous M32 centre, at the single original intrinsic parameter
$\eta_0$ and the explicit-family parameter $\delta=0$,

$$
 \boxed{-73.913337474666793
       <\mathfrak X<-73.913314715519692.}               \tag{F.1}
$$

Here $\mathfrak X$ is exactly the complete strict-symbol finite part
(S.18) of
[the moving first-symbol theorem](R133-supplement-complete-moving-first-symbol-and-root-subtractions.md).
In particular all nonlocal primitive terms, all finite Fourier modes,
the true even mean and both divergent root subtractions are included.
This is not a finite-frequency fit.

The corresponding arithmetic multiple satisfies

$$
 18.478328678879919< -\mathfrak X/4
                         <18.478334368666702.          \tag{F.2}
$$

Equation (F.2) is stated as this multiple of the proved integral. It
is not identified with the coefficient of the complete returned PDE
boundary equation. The exact return word, both actual root rows,
positive graph, and parameter/background transfer must be paid before
making that identification.

## 1. Actual execution and immutable scientific object

The public run is
[43591721337, attempt 1](https://github.com/Rogerhu12/math-research-public/actions/runs/43591721337).
Its event and actual scientific checkout were both
`9111a12e4566feb5db33efcef3174133518f645c`. It returned zero; the
mathematical producer recorded 285.857982 seconds, and all six final
gates passed. The original output was published in commit
`3e996f1a16b16bfec61f834cf6678490649c7c17`.

The full native is

`notes/first_symbol_resume_v2_ci/run-43591721337-1/consumers/first-symbol-resumed-v2.json.gz`

with SHA-256
`cd9ffed6d8c9e107eaac2b50f1846219d8ec90a130555bb91859d465c9bab202`
and compressed size 1,136,949 bytes. The final prefix has exactly the
same bytes and hash. The actual `process.json`, original standard
output, worker process, and publication record accompany it. The
manifest verifies 237 original scientific inputs; it has SHA
`d2f3d184f95e1652008274bfee1a4cb0588874ee1c0524d593255252570f7c2c`.

The numerical environment was Python 3.12.14, numpy 2.3.5,
scipy 1.17.0, python-flint 0.9.0, sympy 1.14.0 and mpmath 1.3.0.
Arb precision was 256 bits, with 192-bit complete exponential tails.
This report consumes those actual records; it does not describe a
local rerun as an Actions execution.

The fixed centre and parameters are

| Object | Exact identity |
|---|---|
| Original full M32 candidate | `ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413` |
| Exact continuous centre definition | `440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47` |
| Physical amplitude | $6890507429876859/9007199254740992$ |
| Original compact metric parameter | $-2572625729470897/72057594037927936$ |
| Intrinsic family parameter | $\eta_0$, exact affine offset zero |
| Explicit phase-family parameter | $\delta=0$ |

The computation does not claim uniformity over the old nonzero
intrinsic parameter box, over the R31 parameter enclosure, or over a
true nonlinear solution ball.

## 2. Complete strict symbol and exact root subtraction

Write $q=\sqrt{-K}$, $\eta=-\gamma m$, $b=a_{\rm phys}'/a_{\rm phys}$
and $r_\sigma=u+\sigma qv$. The proved strict symbol is

$$
 \Xi=\frac{B_+B_-}{\eta q}
                -2bq(uv_\phi-vu_\phi),\qquad
 B_\sigma=-\frac{q_r}{2q}-b(1+r_\sigma^2).              \tag{F.3}
$$

Its angular moments include $u^2,v^2,u^4,u^2v^2,v^4$ and
$uv_\phi-vu_\phi$. The full Laurent products compute these exact
finite-polynomial moments. There is no output Fourier projection in
that operation, and the zero coefficient is not discarded.

At the actual root put $\rho=r_*-r$, $q^2=\rho k(\rho)$, and

$$
 a_0=\frac{k_\rho}{4k}-b(1+u^2+\rho kv^2).
$$

After angular averaging the integrand is exactly

$$
 \langle\Xi\rangle
  =A\rho^{-5/2}+B\rho^{-3/2}
                       +C\rho^{-1/2}-D\rho^{1/2},      \tag{F.4}
$$

where

$$
\begin{split}
 A&=(16\eta\sqrt k)^{-1},\qquad
 B=\langle a_0\rangle/(2\eta\sqrt k),\qquad
 C=\langle a_0^2\rangle/(\eta\sqrt k),\\
 D&=4b^2\sqrt k\,\langle u^2v^2\rangle/\eta
       +2b\sqrt k\,\langle uv_\phi-vu_\phi\rangle.
                                                               \tag{F.5}
\end{split}
$$

Thus $g_0=A(0)$, $g_1=A_\rho(0)+B(0)$, and the exact object in
(F.1) is

$$
 \mathfrak X=\lim_{\epsilon\downarrow0}
 \left\{\int_0^{r_*-\epsilon}\langle\Xi\rangle\,dr
      -\frac{2g_0}{3\epsilon^{3/2}}
      -\frac{2g_1}{\sqrt\epsilon}\right\}.             \tag{F.6}
$$

The true root is first isolated independently by the complete
intrinsic scalar provider. The identity $K(r_*)=0$ then justifies
the analytic factor $k$. It is not obtained by overwriting a
numerical ball containing a small nonzero value with zero.

## 3. The successful prefix was genuinely reused

The previous public run 43589646508 had returned one. Its complete
native, SHA
`5167e64ff6076e0100fa1c643b7168ce889b2fe4f6dab034631ce8d7115f0e1d`,
contains 2,838 accepted integral rows, ending at

$$
 r_{\rm resume}=136414032713052333/576460752303423488.
                                                               \tag{F.7}
$$

The successful complete integral on that prefix was

$$
 [67.9066009326317399946891607653525,
    67.9066009818620474364391038745963].                \tag{F.8}
$$

That original aggregate, all 2,838 rows, and both already completed
root Newton steps are retained without recomputation. Its 15 rejected
subcells and original failure remain separately recorded. The previous
failure is not relabelled as success.

The failed local gate had an interval floor in the original scalar
midpoint values. After fourteen binary subdivisions the Taylor
remainder was already about $6.37\,10^{-47}$; further subdivision
could not remove that floor. The v2 continuation therefore allocates
the remaining width budget to the actual remaining original cells.
Only when the midpoint floor needs it does it obtain a new rigorous
complete scalar evaluation at that midpoint. It retains the original
whole-cell sixth-derivative bounds.

The actual continuation made 248 such new strict midpoint evaluations
and two root finite-part jet evaluations. The 169 original scalar
germs were consumed, not regenerated. The final record has 3,146
accepted strict rows and 120 new rejected subdivision proposals.
Every accepted row is retained with its exact interval, original
candidate piece, scalar native hash, directed integral and remainder.

## 4. Root finite part and directed arithmetic

The strict integration ends at the exact unchanged cut

$$
 r_c=76285779072683/320000000000000.                    \tag{F.9}
$$

The two reused directed root iterations enclose the unique actual
$\eta_0$ root in an interval of width less than $2^{-140}$. Its
two exact endpoints are retained in `actual_eta0_root_enclosure`.
The cut-to-root length satisfies the wider displayed enclosure

$$
 3.81469773098795\,10^{-6}<H=r_*-r_c
                            <3.81469773098796\,10^{-6}. \tag{F.10}
$$

For the analytic coefficients in (F.5), the producer integrates the
normalized point Taylor coefficients through orders 5, 4, 3 and 2,
respectively. The complete whole-interval next normalized derivatives
are those of orders 6, 5, 4 and 3. Since all four omitted integrands
start at power $\rho^{7/2}$, one common directed tail is

$$
 \left(\sup|A^{[6]}|+\sup|B^{[5]}|
            +\sup|C^{[4]}|+\sup|D^{[3]}|\right)
                 \frac{H^{9/2}}{9/2},                         \tag{F.11}
$$

where $f^{[j]}=f^{(j)}/j!$. This was actually bounded by
$6.683362301756\,10^{-14}$.

The complete factor jets use

$$
 k^{[j]}(\rho)
 =\frac{(-1)^j}{j!}\int_0^1t^jK^{(j+1)}(r_*-t\rho)\,dt.
                                                               \tag{F.12}
$$

Consequently each whole-interval coefficient is enclosed by
$(-1)^jK^{(j+1)}([r_c,r_*])/(j+1)!$. These are true derivatives
from the complete Arb Laurent exponential provider, not derivatives
of a fitted error ball. The complete mean gives a positive $\eta$,
and the proved intrinsic simple-root derivative gives positive $k$.
Both divisions in (F.5) are thereby justified on the whole collar.

Here are the principal actual directed components, displayed with
outward rounding:

| Component | Complete enclosure or upper bound |
|---|---:|
| $g_0$ | $[0.0064302534174105249,\ 0.0064302534174105250]$ |
| $g_1$ | $[1.3928130890539420,\ 1.3928130890539422]$ |
| Strict integral $[0,r_c]$ | $[576722.3455853574881241104312262257,\ 576722.3456081166350822616086129791]$ |
| Complete root finite part | $[-576796.2589228321549124683903452632,\ -576796.2589228321547788011439996507]$ |
| Final interval width | $<2.275914710027\,10^{-5}$ |
| Requested width | $10^{-3}$ |

The large strict and root contributions are added as directed Arb
intervals. Their cancellation is paid by the retained precisions and
the two remainder calculations; binary64 values do not decide any
acceptance gate.

## 5. Precisely what the actual success proves

The six final gates certify the complete strict coverage, all 65
continuous-centre coefficients and their true root piece, the refined
unique root, a finite complete root contribution, finite total
integral, and the requested total interval width. The ordinary source
and mean terms belong to the operator from which (F.3) was derived;
no assumption $R_0=0$ was used to select its first symbol.

The source implementing the continuation is
`scripts/fourfold_codazzi_current_first_symbol_resume_v2.py`, SHA
`851a86d3b7745d45246adbc52060287126e1eb99733e73c498c2ba01b0547a4c`.
It imports the unchanged original mathematical integrator, SHA
`c866d7d0f75a36d969d291c4379be34df1b1634a5234875d40819baf555c9a7f`.
The prior input and both execution histories therefore remain visible.

The proved [density ray mean identity](R133-supplement-first-symbol-mean-through-true-rays.md)
identifies the mean of a specified strict two-ray word with the integral
of $\Xi$. The
[two-row Airy audit](R133-supplement-two-row-Airy-audit-and-exact-waist-normalizer.md)
shows why an Airy height coefficient cannot replace its two curvature
rows. The finite symmetric root normalizer, actual positive graph,
the precise full returned word and its strong remainder are still
required. In addition this actual integral has only been computed at
$\delta=0$. The nearby R31 explicit-family parameter, and later the
true PDE background, each require their own transfer estimate.
