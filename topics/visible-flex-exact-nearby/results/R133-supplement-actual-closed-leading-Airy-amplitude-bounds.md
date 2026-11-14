# R133 supplement: actual closed leading Airy amplitudes and full complex bounds

2026-11-14, phase_inverse. **Actual public computation completed.**

Public Actions run [43612196888, attempt 1](https://github.com/Rogerhu12/math-research-public/actions/runs/43612196888)
ran the frozen closed-amplitude consumer with actual return code zero.
All **22 gates passed** in **0.564666270999993 seconds**. Both the event
commit and the actual scientific checkout were
$8bb6346674fb4f2cbbfa98b89cb0b68801088208$.
This is an independent computation from two completed process records;
it reran none of the original scalar germs, response cubics or ray transports.

## 1. Exact original objects and execution identity

The background is the repaired explicit family $Q^\delta=Q^0+\delta Z$
at intrinsic $\eta_0$, on the whole complex disk $|\delta|\le10^{-8}$.
Its background and direction definitions remain respectively
$440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47$
and
$6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04$.
The independent even mean and every original angular primitive/source row
remain. No nonlinear PDE branch is inferred.

The immutable execution files are in
[the actual consumer directory](../notes/closed_leading_airy_amplitudes_ci/run-43612196888-1/consumers/).
The small process record was read in full after checking its directory
size, 14413 bytes. It preserves all gate results and all directed bounds.

| Executed item | SHA-256 |
|---|---|
| Mathematical producer | $dc343805acfdae67302ae2501517955eb88eef706daff17711feaf7457fb9919$ |
| Public CI driver | $c67d48104692a01637b5cc757cee8f6c586cf0c74e6a6c53c0257ab27a226b10$ |
| Complete 13-file input manifest | $9f6c60a2395c11ec04d9fbc69aadc6fcd0be6717ebdead8ba9d76d7c371cf5a8$ |
| Actual process, 14413 bytes | $35e3935f5a039731b2d3c71dfb0c323b51f3fb1afa912695a48d8beb96ace331$ |
| Fresh native, 3154 bytes | $1c00bf9f6d80343b96bdabf2ce2b07f1f3461851ad0783b9a2a59a495d141cdd$ |
| Original actual fold native | $9300be45949cba94115511bf77d025a82e39c78d491ba77de916d7a96902fffd$ |
| Original actual negative Cauchy native | $8f165ccf9dee6e622060b4fc269908ef322f0b0fea15b82dc4b223a2fb4c122d$ |

The producer used Python 3.12.14, python-flint 0.9.0 and Sympy 1.14.0.
The manifest pinned each of its 13 input files and all original producer
semantics. The process contains both the actual command and its true
completion code; success is not inferred from a workflow title.

## 2. The complete leading amplitudes now have paid bounds

Use the exact formulas and signs proved in
[the closed leading-amplitude theorem](R133-supplement-closed-leading-Airy-amplitudes-and-exact-seam-transmission.md).
With $q^2=\rho k$, $\rho=r_*-r$, $T=-\rho A^{2/3}$, write
$$
 E=\exp\left[-2\int_{r_*}^r b\langle u^2+Kv^2\rangle\,ds\right],
 \qquad
 G=(k_*/\eta_*)^{1/6}A^{1/6}k^{-1/4}E .
$$
For physical frequency $n=4|j|$ and $\epsilon=\operatorname{sgn}j$,
$$
 a_0=G(X_\phi^2-TT_\phi^2),\qquad
 b_0=-2i\epsilon G X_\phi T_\phi .
$$
The convention is
$$
 e^{i\epsilon nX}\left[
 a_0\operatorname{Ai}(n^{2/3}T)+
 b_0 n^{-1/3}\operatorname{Ai}'(n^{2/3}T)\right].
$$
Both original curvature rows give exactly this normalization.
In particular $a_0(0,X)=1$ and $b_0=O(T^2)$.

The whole canonical outer rectangle is
$$
 |T|\le81/4000000,\qquad |\Im X|\le1/128 .
$$
The following displayed decimals are rounded outward from the actual
directed native bounds.

| Complete norm or scalar bound | Certified strict bound |
|---|---:|
| Root quotient real-part gap | $k_->59.743804372436$ |
| Root quotient modulus | $k_+<60.843321458870$ |
| Absolute exponent defining $E$ | $h_E<1.510878545344\cdot10^{-6}$ |
| Both $E$ and $E^{-1}$ | $1.000001510880$ |
| $G$ | $1.004576486079$ |
| $G^{-1}$ | $1.004602199361$ |
| $a_0$ | $1.004641504569$ |
| $a_0^{-1}$ | $1.004667223723$ |
| Both branch-amplitude inverses | $1.004667221675$ |
| $b_0/T^2$ | $5.287642787676$ |

Consequently the proposed rational thresholds
$\|a_0\|,\|a_0^{-1}\|,\|(G\Phi_{\pm,\phi}^2)^{-1}\|<51/50$
and $\|b_0/T^2\|<6$ have actually passed.
The quotient bound uses its true root divisibility, not division of a
fixed error ball by a vanishing $T$.

The two true oscillatory phase branches satisfy the exact identities
$$
 a_0\mp i\epsilon\sqrt{-T}\,b_0
 =G(X_\phi\mp\sqrt{-T}\,T_\phi)^2
 =G\Phi_{\pm,\phi}^2 .
$$
The symbolic gates checked both signs, the complete principal Jacobian
factor, the original two-row local diagonal and off-diagonal terms,
the cancellation of the entire $\eta_r/\eta$ leading contribution,
and the sign of the fold chain term $-1/(2T)$.
The mean in $E$ is the original normalized mean at fixed $r$.

## 3. Derivative domain and exact transmission scope

On the strictly smaller rectangle
$$
 |T|\le19/10^6,\qquad |\Im X|\le1/256 ,
$$
the actual radial and angular Cauchy margins are $1/800000$ and
$1/256$. The full mixed derivative bounds are
$$
 \|\partial_T^p\partial_X^q a_0\|_\infty
 \le p!q!(1.004641504569)\,800000^p256^q,
$$
with $5.287642787676$ in place of the leading constant for
$b_0/T^2$. The native separately retains all requested derivative
orders, rather than differentiating an interval error.

It also gives
$$
 \|b_0\|<1.908839046351\cdot10^{-9},\quad
 \|\partial_Tb_0\|<0.001728001663013,\quad
 \|\partial_T^2b_0\|<2775.377946396 .
$$
These Cauchy bounds are valid and may be much larger than a useful
strong-return budget. They are not presented as that budget.

The companion theorem proves exact leading transmission at an original
strict seam whenever the same complete inverse $J$ is available:
$$
 [h_2]=[f],\qquad
 [h_1]=J\{[f_r]-d\partial_\phi[f]-B[f]\}.
$$
The true leading trial is $C^1$ in the old radial coordinate, so its
two reconstructed value jumps vanish. This algebraic consequence of
the continuous repair is distinct from a replay of original seam
bytes: this consumer did not replay those bytes and explicitly records
that fact. Higher-amplitude forcing and all resulting nonzero jumps
must still be supplied to the genuine propagation maps.

The successful native explicitly leaves false the claims that complete
next amplitudes have been evaluated, a milliscale piecewise fold domain
has been certified, every higher jump fee has been paid, numerical
$C_E,C_s$ and a sufficient strong-return cutoff have been established,
or a cutoff-97 inverse or a true PDE branch has been proved.
