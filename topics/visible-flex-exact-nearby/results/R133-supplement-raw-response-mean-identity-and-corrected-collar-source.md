# R133 supplement: raw-response mean identity correction and the minimal collar fee

2026-11-15. Exact correction of a source identification, with a new
read-only scalar-consumer contract. The old scientific files, their
successful process statuses and all 91 scalar records remain unchanged.
A successful historical process is not by itself a proof that its
input was identified with the intended mathematical source.

## 1. Three different response objects

Keep the repaired M32 centre $Q_0$, the original physical 193-state
cubic trial $q$, and the exact piecewise-constant continuity repair
$e_{\rm cont}$. The parameter direction used throughout the selected
family is
$$
 Z=q+e_{\rm cont},\qquad
 \partial_r e_{\rm cont}=0\ \hbox{a.e.},\qquad
 \|e_{\rm cont}\|_{A^0,\mathrm{pair}}\le E_Z=2.292\,10^{-16}.
 \tag{MC.1}
$$
This is the definition with hash
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04,
from [the continuous direction](R133-supplement-explicit-continuous-response-direction-and-true-strip-norms.md).
It includes the original even mean. No amplitude factor is applied to
the physical trial $q$.

A different earlier construction completed the scalar mean equation.
On each original open radial piece it used
$$
                    q^\sharp=q+e_{\rm mean}(r)e_2 .
 \tag{MC.2}
$$
The radial function $e_{\rm mean}$ is the solution of a scalar
inhomogeneous ODE with the true outer mean condition and all original
mean jumps. It is not the tiny piecewise-constant correction in (MC.1).

Let $A^{\rm raw}$ and $F_\nu^{\rm raw}$ denote the linearized
operator and parameter source at the original uncorrected background.
The original complete polynomial row stores
$$
 R^{\rm raw}=(\partial_r-A^{\rm raw})q-F_\nu^{\rm raw},
 \quad r_i^0=\langle(R^{\rm raw})_2\rangle_\phi,\quad
 R^{\rm raw}_{\ne0}.
 \tag{MC.3}
$$
In the actual reflection class the first component is odd, so its mean
is exactly zero. The second mean $r_i^0$ is independently retained.
This reflection fact does not authorize removal of an even mean.

The exact primary entry points are:

| Item | Path relative to this topic | Git blob | Bytes / SHA256 |
|---|---|---|---|
| Original correlated rows | scripts/fourfold_codazzi_correlated_head_residual_rows.py | 3af195a36ccb30630dbfcab0caef3564738ab169 | 13043 / 1651f6cf73af9f3c16061767cc5acff0c452ada183422f7efb983ec8a6d4eb07 |
| Scalar mean completion | scripts/fourfold_codazzi_correlated_mean_error_consumer.py | 6e831d759c53d07e93ad24277aa7b022b05ee5b4 | 10587 / 8d151648278cc122e27383ff3e5de88fe6695b983d11a57d27e74f6325ce6cbb |
| Subsequent centre repair | scripts/fourfold_codazzi_complete_response_repair_source.py | 5e8c9311cab02eb88abdec135f26326610aee91e | source SHA 6e4e8f1a3f69fdc06c15a0471cedb62abce0740b4825ddf5a0d04de4b984d7ad |

The first producer stores `response_mean_residual` as a
complete signed scalar range on the actual closed row. Its
`uncorrected_response_nonmean` fields are norms of the
nonmean vector in (MC.3), including complete intrinsic errors.

## 2. What the accepted old summary actually bounds

For each original row $I_i$, the mean-completion producer constructs
the nonnegative bound
$$
 N_i^\sharp=N_i^{\rm raw}
       +\|e_{\rm mean}\|_{L^\infty(I_i)}
                         C_i,\qquad
 N_i^\sharp\ge N_i^{\rm raw}.
 \tag{MC.4}
$$
Here $C_i$ is the corresponding complete norm of
$(A^{\rm raw}e_2)_{\ne0}$. It writes this quantity to
`response_complete_nonmean_residual`.
The corrected mean equation for $q^\sharp$ has zero residual; this
does not assert $r_i^0=0$ for $q$.

The later centre-repair producer reads that nonmean field. Its operator
repair budget has the form
$$
 \mathcal E_i=M_{1,i}H_{1,i}+M_{0,i}H_{0,i}
                                      +\mathcal E_{\nu,i},
 \tag{MC.5}
$$
where all coefficients are nonnegative,
$$
 H_{0,i}=H_{0,i}^{\rm raw}+\|e_{\rm mean}\|_\infty
              \ge\|q\|_{A^0,\mathrm{pair}},\qquad
 H_{1,i}\ge\|q_\phi\|_{A^0,\mathrm{pair}} .
$$
The mean correction has no angular derivative. Consequently the
*same displayed nonnegative budget* (MC.5) also bounds
$$
              (A_0-A^{\rm raw})q+(F_{\nu,0}-F_\nu^{\rm raw}).
 \tag{MC.6}
$$
This use is valid by monotonicity in $H_0,H_1$; it is not an
identification of $q^\sharp$ with $q$.

Let $B_{\rm old}$ be the accepted whole-body scalar
`complete_repaired_response_residual_L2_radial.L2`
from summary SHA
7c43eeed609006195893d6ceee5003887e533ac6222515171d27b624e47115ec.
The old summary's actual value, approximately $0.00128406968$, is
left unchanged. The precise valid consequence needed here is
$$
 \bigl\|-R^{\rm raw}_{\ne0}
       +(A_0-A^{\rm raw})q+(F_{\nu,0}-F_\nu^{\rm raw})\bigr\|_{2,I}
                                \le B_{\rm old}
 \tag{MC.7}
$$
for every subinterval $I\subset[0,25/8]$. This follows from
(MC.4), (MC.5), rowwise triangle and the old whole-body sum.

The ordinary complete raw source additionally contains
$-r^0e_2$. Thus the statement in the former residual note that the
old summary is already the full residual of $q_{\rm raw}$ is
incorrect. Its use as such in the first collar consumer omitted this
independent mean fee.

No additional term $(A_0-A^{\rm raw})e_{\rm mean}e_2$ is required
when using (MC.7): the proof discards the extra positive term in
(MC.4) and uses (MC.5) directly on $q$.
If instead one subtracts the vector equations for $q^\sharp$ and
$q$, the full $(\partial_r-A_0)(e_{\rm mean}e_2)$ must be kept.
That different subtraction is not performed here.

## 3. Exact corrected decomposition

Retain $C_0,C_1$ from (R.12)--(R.14) of
[the selected-centre residual identity](R133-supplement-selected-centre-complete-residual-and-collar-source-bounds.md).
The continuous repair satisfies
$$
 \|A_0e_{\rm cont}\|_{L^2_\phi}
                          \le E_Z(384C_1+C_0).
 \tag{MC.8}
$$
Define the actual function
$$
 \begin{split}
 b_0={}&-R^{\rm raw}_{\ne0}
       +(A_0-A^{\rm raw})q+(F_{\nu,0}-F_\nu^{\rm raw})
                                           +A_0e_{\rm cont},\\
 s_0={}&F_{\nu,0}-(\partial_r-A_0)Z
                                      =b_0-r^0e_2 .
 \end{split}
 \tag{MC.9}
$$
The existing collar number formerly labelled $S_0$ is a valid bound
for $\|Pb_0\|_{2,I}$. It need not be a bound for $\|Ps_0\|_{2,I}$.
In particular $b_0$ itself may have a small mean coming from the
centre and continuity repairs; that mean is already paid by (MC.8)
and the full pair budget (MC.5).

On the bump-free positive collar the exact polynomial identity is
therefore
$$
 f_\delta=f_0-\delta b_0+\delta r^0e_2
                         -\delta^2T_2-\delta^3T_3.
 \tag{MC.10}
$$
Here $f_0$ is the residual of the degree-32 repaired centre, while
the selected centre has degree 96. The complete angular support bounds
are
$$
 \deg f_0\le96,\quad \deg b_0\le160,\quad
 \deg(r^0e_2)=0,\quad\deg T_2\le224,\quad\deg T_3\le288 .
 \tag{MC.11}
$$
The signs in (MC.10) follow the ordinary residual convention
$f=Q_r-\mathcal F(Q)$. All parameter and repair identities in
(R.1)--(R.22) remain correct when this source identification is used.

Set
$$
 M_I\ge\|P(r)r^0(r)e_2\|_{L^2(I;L^2_\phi)},\qquad
 P=\operatorname{diag}(K^{-1/4},K^{1/4}).
 \tag{MC.12}
$$
If $F_{\rm val}^{\rm old},F_{\rm ang}^{\rm old},
F_{\rm fact}^{\rm old}$ are the three retained scalar expressions
of the first collar consumer, the corrected complete source bounds are
$$
 \begin{split}
 F_{\rm val}^{\rm new}&=F_{\rm val}^{\rm old}+dM_I,\\
 F_{\rm ang}^{\rm new}&=F_{\rm ang}^{\rm old},\\
 F_{\rm fact}^{\rm new}&=F_{\rm fact}^{\rm old}+dM_I,
                          \qquad d=10^{-10}.
 \end{split}
 \tag{MC.13}
$$
The third equality holds for every finite factorial order: the added
source is angularly constant, and every positive angular derivative
vanishes exactly. There is no extra $e^{640\sigma}$ factor on it.
There is also no factor $\alpha$, $1/2$, or $\sqrt2$ on its
normalized-circle mean.

## 4. A minimal new read-only restriction

The original 40 natural parts cover all 7,721 rows with the identities
already checked by actual run 43713242980/1. Restore those exact
historical bytes only into the new public runner's temporary directory.
Read the original interval and signed
`response_mean_residual` fields; do not evaluate the
old target, cubic trial, residual polynomial, scalar mean flow or
Fourier transform again.

For each old row meeting $I$, put
$$
 \lambda_i=|I\cap I_i|,\quad
 R_i\ge\sup_{I_i}|r_i^0|,\quad
 K_i^+\ge\sup_{I_i}K,\qquad
 M_I^2=\sum_i\lambda_i\sqrt{K_i^+}\,R_i^2 .
 \tag{MC.14}
$$
The complete $K_i^+$ comes from the same row's
`intrinsic_whole_third_jets.K`, and $K_i^->0$ is
checked. This is the exact second component of $P^*P$.
The old scalar range is valid on every closed subinterval, so using
the true intersection length in (MC.14) is valid. It does not scale
a saved integral as though its integrand were constant.

The smallest consumer needs only two domains: the complete published
intrinsic collar $[17/20,19/20]$, and each distinct interval among
the five retained complete cases. Those five cases currently share
$[589819/655360,589829/655360]$, with $\ell=2^{-18}$.
The larger domain gives an independently useful complete mean-source
supremum; the narrow domain supplies (MC.13).
All original row seams and the signed mean enclosures are retained in
the temporary audit; the small conclusion saves the interval, exact
measure, row count, full scalar sums and hashes.

This new scalar restriction is a new fee. It does not recompute any
old residual or alter the successful 91-case report.

## 5. Reevaluating only the retained five cases

For each retained complete case, copy the old coefficient bounds,
$C_E,c_2,c_3,p_+,\ell$, the raw $C^0$ radius and every identity
byte. Its start and linear gates are independent of the source
amplitude and remain unchanged. Set
$$
 A_N^{\rm new}=A_N^{\rm old}+dM_I .
 \tag{MC.15}
$$
Only the affected nonlinear and readout expressions need new directed
evaluation:
$$
 \begin{split}
 \mathfrak n^{\rm new}
  &=2C_E^2c_2 A_N^{\rm new}
                         +4C_E^3c_3(A_N^{\rm new})^2,\\
 \mathfrak p^{\rm new}
  &=2p_+C_E\sqrt\ell\, A_N^{\rm new}.
 \end{split}
 \tag{MC.16}
$$
The old thresholds are unchanged. A new passing case restores the
conditional high-trace conclusion for its stated radius and collar
only. The other ten formerly passing cases are not reauthorized by
a computation on these five cases.

For completeness the low $H^1$ diagnostic can be increased by its
exact positive source sensitivity. Put
$$
 c_p=2/a_-,\quad c_r=1+2d_+/a_-,\quad
 A_1^+=\alpha_++5b_+M^2,\quad
 G_{\rm val}=p_+\left\{\ell^{-1/2}c_p+
       \sqrt\ell\,c_r[1+c_p(A_1^++L+2/\ell)]\right\}.
 \tag{MC.17}
$$
Here $M=M_0+\eta$ from that same retained case. The corrected
diagnostic is bounded by the old complete diagnostic plus
$G_{\rm val}dM_I$. Its old false low-entry verdict is preserved;
an added positive source does not turn it into a passing gate.

Until the new directed evaluation succeeds, the old 15/91 success
count is a historical scalar result with this source-identity
qualification. It is not an authorization for the intended selected
centre's complete high gate. The energy lemmas, exact support
identities, old raw data and old process receipts are unaffected.

## 6. An independent high projection that remains usable

Let $\Pi$ be the full physical moving Fourier projector through
quarter-index 96, including the true even mean, and $H=1-\Pi$.
Radial $P$ commutes with both projectors. Equations (MC.10)--(MC.11)
give
$$
 H(Pf_\delta)=-\delta H(Pb_0)
                   -\delta^2H(PT_2)-\delta^3H(PT_3).
 \tag{MC.18}
$$
Both $H(Pf_0)$ and $H(Pr^0e_2)$ are exactly zero. Thus the old
positive quantities bound this *high-projected* ordinary source and
its first angular derivative:
$$
 \begin{split}
 \|H(Pf_\delta)\|_2
  &\le dS_0^{\rm old}+d^2T_2^\#+d^3T_3^\#,\\
 \|\partial_\phi H(Pf_\delta)\|_2
  &\le640dS_0^{\rm old}+896d^2T_2^\#+1152d^3T_3^\# .
 \end{split}
 \tag{MC.19}
$$
This conclusion uses the monotone scalar argument of Section 2.
It does not need a false equality of the two mean-completed response
objects. Equivalently, for the degree-32 centre the column $A_0e_2$
has angular degree at most 64, so its complete scalar-mean correction
cannot reach this high projection. Neither observation permits
removing the mean from the full ordinary equation.

A future approximate state retains its own high ordinary residual
and the speed contribution $\langle f_2\rangle/m$. A future true
solution may set its own residual to zero only after it exists.
These statements do not construct the core, close the unknown high
feedback, or match two independently constructed one-sided states.
