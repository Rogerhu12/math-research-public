# R133 supplement: the exact normalized-weight physical-mean forcing

2026-11-16, phase_inverse.

**Proved here:** the complete physical-mean forcing of N, WUA and WEJ has an exact representation with one common normalized angular weight. Two internal mean identities remove the nonlocal term in the transpose kernel before any norm is taken. This is an identity for the same forcing and the same physical mean. It does not set the state mean, a background residual, or an external matching row to zero.

The 42 successful WMR scalar targets and all earlier complete scientific graphs are retained unchanged. No new scientific value, exponential, angular inverse, source integral or bound has been evaluated for this note. In particular, the identity below does not by itself assert that a new numerical bound improves the saved complete forcing constant.

## WMF1. The original real operator and the same forcing

Use the normalized angular measure on the circle of period $\pi/2$:
$$
 \Pi f=\langle f\rangle,\qquad P=Id-\Pi,\qquad
 \partial=\partial_\phi,\qquad I=\partial^{-1}P.
 \tag{WMF.1}
$$
Thus $\partial$ has multiplier $4ij$, $\partial I=I\partial=P$, and the complete primitive satisfies $I^*=-I$ in the angular pairing. Every identity in this note uses that complete primitive, including its zero-mean convention.

All background coefficients are those of the same actual real repaired family and the same negative strict/local domains admitted in N, JI, WEJ and WMR. The reflection class is $u$ odd and $v$ even. Write
$$
 \begin{gathered}
 m=\Pi v,\qquad \eta=-\gamma m,\qquad
 \beta=a_{\rm phys}'/a_{\rm phys},\qquad S=u^2+Kv^2,\\
 d=-\beta IS,\qquad
 D=\partial_r-d\partial_\phi,\qquad
 L_{22}=\beta(1-u^2-3Kv^2),\qquad
 b_0=\beta(1-\Pi S).
 \end{gathered}
 \tag{WMF.2}
$$
The symbol $\beta$ is the metric coefficient denoted $b$ in N.2, not a reference-column or phase parameter. The radial scalar $b_0$ is not the angular function $b_2$ of N.5. The original characteristic coefficient $\eta$ is distinct from the fixed intrinsic parameter $\eta_0$.

In particular, the exact definition of the drift gives
$$
                 d_\phi=-\beta(S-\Pi S).
 \tag{WMF.3}
$$
This identity does not assume that any radial background equation has zero residual.

Let $A$ and $B$ be the complete original N.4--5 operators:
$$
 \begin{split}
 A&=P\{\eta\partial-2\beta M_{uv}
                         -2\beta M_{v_\phi}IM_u\}P,\\
 B&=P\{M_{L_{22}}-2\beta K M_{v_\phi}IM_v\}P,\\
 H_2&=PM_d\partial P+B,\qquad D_0-B=\partial_r-H_2 .
 \end{split}
 \tag{WMF.4}
$$
The inverse $J=A^{-1}$ is the same reflected realization, from even mean-zero input to odd output. It is not an inverse on an artificially enlarged signed carrier.

For the same even mean-zero height $f=Ph_2$ used in WUA and WEJ, define
$$
 h_{10}=J(D_0-B)f,\qquad
 F_{\rm mean}=2\beta m\,\Pi\{u h_{10}+K(v-m)f\}.
 \tag{WMF.5}
$$
This is precisely WUA.40 and WEJ.22--24. With $k=Jb_2$, its physical mean is still determined by
$$
 \begin{split}
 z_{\rm ph}'&=a_{\rm eff}z_{\rm ph}-F_{\rm mean},
                      &z_{\rm ph}(r_*)&=0,\\
 h_1&=h_{10}-z_{\rm ph}k,
                      &h_2&=f+z_{\rm ph}.
 \end{split}
 \tag{WMF.6}
$$
The complete original $a_{\rm eff}$ is unchanged. The present lemma neither replaces this ordinary radial equation by an angular mean condition nor changes the genuine root normalization.

## WMF2. Normalize the one common angular weight

Set
$$
 \alpha=\frac{2\beta}{\eta},\qquad
 a_J=\exp\{-\alpha I(uv)\},\qquad
 w_J=1-\alpha uIv,\qquad
 D_J=\Pi(a_Jw_J),\qquad p_J=\frac{a_J}{D_J}.
 \tag{WMF.7}
$$
These are the JI.5 denominator and the WMR.5 common weight. The function $a_J$ is not the physical metric radius. The normalized weight $p_J$ is not the internal primitive called $p$ in JI.7 and is not the physical state mean.

On the real strict and local patches WMR.7--15 establish $w_J\geq\delta>0$, with the separately justified choices
$$
           \delta_{\rm strict}=\frac{79}{128},
           \qquad \delta_{\rm local}=\frac34 .
 \tag{WMF.8}
$$
The local conclusion has its own original local-germ qualification; the strict lower is not transported to the root. Consequently $D_J>0$, $p_J>0$, and
$$
 \Pi(p_Jw_J)=1,\qquad
 (p_J)_\phi=-\alpha uvp_J,\qquad
 \Pi(p_Ju)=0 .
 \tag{WMF.9}
$$
The derivative is JI.6 divided by the radial scalar $D_J$. The last identity uses the actual parity: $p_J$ is even and $u$ is odd.

The normalized measure $p_Jw_J\,d\phi$ has mass one. The function $p_J$ alone need not have mean one. In particular,
$$
                \Pi p_J\leq\delta^{-1}.
 \tag{WMF.10}
$$
No separate upper bound for $a_J$, lower bound for $D_J$ or norm of $J$ is used in (WMF.9)--10. The pointwise hypothesis $w_J\geq\delta$ is substantive; a general positive lower for $D_J$ would not imply it.

## WMF3. The complete transpose kernel, before simplification

The exact scalar identity JI.10 gives, for even mean-zero $q$,
$$
 2\beta m\,\Pi(uJq)=\Pi(eq),\qquad
                 e=-\alpha m I(p_Ju).
 \tag{WMF.11}
$$
Indeed, JI.10 first gives
$\Pi(uJq)=\eta^{-1}\Pi(p_JuIq)$, and $I^*=-I$ moves the primitive to the actual full test. By (WMF.9), the kernel $e$ is even and mean zero, with
$$
                         e_\phi=-\alpha m p_Ju.
 \tag{WMF.12}
$$
There is no omitted mean in this derivative.

The full N.5 operator in (WMF.4) has transpose
$$
 H_2^*e=-\partial(de)+P(L_{22}e)
                    +2\beta K P\{vI(v_\phi e)\}.
 \tag{WMF.13}
$$
The derivative acts on the whole product $de$. Both outer projections and the complete inner primitive are retained. The sign of the last term follows from $I^*=-I$; the multiplier order reverses under the transpose.

Thus (WMF.5) is exactly
$$
 \begin{split}
 F_{\rm mean}&=\Pi(e f_r+e_\kappa f),\\
 e_\kappa&=-H_2^*e+2\beta mK(v-m).
 \end{split}
 \tag{WMF.14}
$$
The kernel $e_\kappa$ is also even and mean zero. Equation (WMF.14) is the original WEJ.13--15 kernel formula, not a norm estimate.

There is no $e_r$ term in (WMF.14): its first object is the pairing $\Pi(e f_r)$, not the radial derivative $\partial_r\Pi(ef)$. If a later argument integrates in $r$ or uses the normal form $z_{\rm ph}+\Pi(ef)$, it must restore the actual $e_r$ and the full root, endpoint and jump contributions.

## WMF4. Two internal mean identities

The normalization in (WMF.9) gives
$$
                  \alpha\Pi(p_JuIv)=\Pi p_J-1.
 \tag{WMF.15}
$$
Using the complete skew primitive in (WMF.11), this proves the first identity
$$
 \boxed{\qquad \Pi(ve)=m(\Pi p_J-1).\qquad}
 \tag{WMF.16}
$$
No division by $\alpha$, $\beta$ or $m$ is involved.

For the second identity, differentiate the proposed right-hand side:
$$
 \begin{split}
 \partial\{ve-m(p_J-1)\}
 &=v_\phi e+ve_\phi-m(p_J)_\phi\\
 &=v_\phi e-\alpha mvp_Ju+\alpha muv p_J\\
 &=v_\phi e .
 \end{split}
$$
Its mean is zero by (WMF.16):
$\Pi(ve)-m(\Pi p_J-1)=0$. The unique mean-zero primitive is therefore
$$
 \boxed{\qquad I(v_\phi e)=ve-m(p_J-1).\qquad}
 \tag{WMF.17}
$$
Equivalently, one may start from
$I(v_\phi e)=P(ve)-I(ve_\phi)$ and use
$\alpha I(p_Juv)=-Pp_J$. The constant term $m$ in (WMF.17) is essential. Dropping it before substitution would change the complete transpose kernel.

Both identities remain valid where $\beta=0$: then $\alpha=0$, $a_J=D_J=p_J=1$, and $e=0$. This observation is only an algebraic consistency check and does not set $z_{\rm ph}$ to zero.

## WMF5. Exact collapse of the nonlocal forcing kernel

Substitute (WMF.17) into (WMF.13)--14. Since
$v-m=Pv$, the two complete copies of $2\beta mKPv$ cancel in that operator identity:
$$
 e_\kappa=\partial(de)
       -P\{(L_{22}+2\beta Kv^2)e\}
       +2\beta mK P(vp_J).
 \tag{WMF.18}
$$
This is an equality of functions with all their mean conventions, not a subtraction of independently estimated positive quantities.

Now
$$
 L_{22}+2\beta Kv^2=\beta(1-S),\qquad
 d_\phi-(L_{22}+2\beta Kv^2)=-b_0.
 \tag{WMF.19}
$$
The second identity follows from the exact drift derivative (WMF.3). Because $\Pi e=0$ and $b_0$ is radial, (WMF.12) and (WMF.18) give
$$
 \boxed{\qquad
 e_\kappa=-b_0e
             +2\beta mP\!\left[
                  p_J\left(Kv-\frac{du}{\eta}\right)\right].
 \qquad}
 \tag{WMF.20}
$$
This identity includes the whole original $H_2^*$, not merely its differential principal part. It does not discard the nonlocal term from N.5: that term was evaluated exactly using (WMF.16)--17. The projection in the last term remains part of the kernel.

The coefficient $b_0$ in (WMF.20) retains $\Pi S$. Neither the full mean $m$ nor the physical even mean $z_{\rm ph}$ has disappeared. No radial equation for $u$, $v$, $m$ or $a_{\rm phys}$ was used to obtain (WMF.20).

## WMF6. The exact primitive representation of the same forcing

Put
$$
                    g=If,\qquad g_\phi=f,\qquad \Pi g=0 .
 \tag{WMF.21}
$$
For smooth periodic data, $\partial_rg=If_r$ on every actual open radial piece. Apply angular integration by parts to (WMF.14), using (WMF.12) and (WMF.20):
$$
 \begin{split}
 \Pi(e f_r)&=-\Pi(e_\phi g_r)
                         =\alpha m\Pi(p_Ju g_r),\\
 -b_0\Pi(ef)&=b_0\Pi(e_\phi g)
                         =-\alpha m b_0\Pi(p_Ju g).
 \end{split}
 \tag{WMF.22}
$$
For the last term of (WMF.20), $f$ is mean zero, so its complete outer projection may be removed in this pairing, with no change to the independent state mean. Hence
$$
 \boxed{\qquad
 F_{\rm mean}
   =2\beta m\,\Pi\!\left\{
      p_J\left[
       \frac{u}{\eta}(Dg-b_0g)+Kv\,g_\phi
      \right]\right\},
 \qquad D=\partial_r-d\partial_\phi .
 \qquad}
 \tag{WMF.23}
$$
In particular, the drift contribution is
$-(du/\eta)g_\phi$. The derivation has not commuted $D$ with $I$; doing so without its commutator would change this term.

Equations (WMF.14), (WMF.20) and (WMF.23) are three exact descriptions of the same full linear functional of the actual height and its radial derivative. They use the same background, input normalization and primitive. They are not three different choices of the physical mean.

The proof is first pointwise on each original smooth radial piece. The same identities extend to the admitted weak realization whenever the displayed pairings are defined, by the original angular density argument and continuity of the complete primitive. This extension does not assert a new numerical norm or an additional regularity class for the incoming data. At the root the already admitted local/germ interpretation supplies the same coefficient limits; no division by $T$, $q$, or a vanishing curvature has been introduced.

## WMF7. What the identity changes and what still needs an estimate

The exact common weight now occurs once, in (WMF.23). Its positive mass bound (WMF.10) is available on the same real patch, and its angular logarithmic derivative is the explicit complete product $-\alpha uv$. These facts allow a future complete estimate of the forcing to avoid independently multiplying an $a_J$ upper by a $D_J^{-1}$ upper or differentiating the latter in a formula that contains no such radial derivative.

A new estimate must still control the entire expression in (WMF.23), or equivalently the whole kernel in (WMF.20), on the actual WUA trial. It must retain the complete genuine profile, both reflected input signs, the actual first amplitude, all primitive terminals and internal means arising in any finite expansion. The old CF/N6 upper cannot be reduced by subtracting fees from its saved scalar. A proposed replacement must be a new full positive bound for the same functional.

This note supplies no new forcing constant, no new propagation exponent and no new complete-error comparison. The successful WMR 42 records, its original complete choices and all preceding saved graphs remain immutable inputs. Any later scientific consumer must give its new target and complete input qualification separately.

The independent physical mean equation (WMF.6) remains present. The full first source
$$
 g_1=J\mathscr Q f+F_{\rm mean}k-z_{\rm ph}R_{\rm mean},
 \qquad g_2=0
 \tag{WMF.24}
$$
retains the original $k$, $R_{\rm mean}$ and all required $J_r$ and coefficient radial derivatives. Simplifying $e_\kappa$ does not simplify every other occurrence of those derivatives. The genuine root term, both stored waist mean coordinates, the parameter row, the actual 96 physical columns and their matching constraints, and all independent radial/head/source ports are unchanged. No finite inverse or full incoming inverse follows from (WMF.23).

## WMF8. Immutable primary evidence and verification boundary

The complete primary text objects below fix the operator and normalization used in the proof. They were read as text. No old or new scientific producer was called.

| Complete primary | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| N, complete moving root scalarization | 8a57ec851fc9029e4319650b87360b9867d22a97 | 15539 | 0645cf460507ea587056b6969b01dc532b6623179db5598e2bffe4f53a8275af |
| JI, exact reflected angular inverse and denominator | 839fa641fe9ce3758ee69cfe3cb4299f59a3a239 | 11769 | 01e4a33be5d895ccbfc949310a86bf561c8dccdfe1c1eff973fa1298fcc91cf1 |
| WEJ, complete physical-mean and transpose-kernel recipes | da9d8461ca406a1c6f4b829a91147a860133567f | 59644 | 6b7644a978915550b5835b3492eda3bffde872b8e92f16c2db6c4538e405be8f |
| WUA, same genuine trial and full mean completion | 7b89251dcd51e8cb78fd3e8e42905114ef982ebf | 40111 | 9cd778ec8c97904b29524ae8b8252c14304eedfdc67d4ffec48affa79ae18bad |
| WMR, same positive-weight and patch qualification | a7b23dea9a96dfab74475d382ca2d1df8edd5b8e | 31643 | 550866c05d9a07d3e4b037e5840a4f75b66a7f3a9304c5cd0d52e4f2b7e729a6 |

The exact local source positions are N.2--7 for (WMF.2)--6, JI.5--10 for (WMF.7)--12, WEJ.13--15 and WEJ.22--24 for (WMF.13)--14, and WMR.5--15 for the complete real positive-weight qualification. The two internal identities (WMF.16)--17 and their use in (WMF.20)--23 are the new conclusion of this note.

The N and JI paths are
results/R133-supplement-complete-moving-root-scalarization.md and
results/R133-supplement-complete-real-interval-angular-inverse-and-physical-mean.md.
The WUA path is
results/R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md.
The WMR path is
results/R133-supplement-positive-weight-physical-mean-propagation-and-complete-error-reassembly.md.
These are relative to topics/visible-flex-exact-nearby/.

The already successful WMR science remains
notes/positive_weight_physical_mean_refinement_ci/run-43840219992-1/actual-scientific-conclusion.json,
Git blob 5fdb01ed62008489bca34a4b6231519af4f60793, 51030 bytes,
SHA256 39a2d96accdbe1b4a8073674cabeda97878876f11fc24a055b910ed61567b432.
It is cited to identify the frozen previous target, not as a computation of (WMF.23).

Newton and Tail independently checked the two internal means, the full transpose substitution and the material-direction sign in the new identity. The author also checked the displayed derivation against the complete primary formulas. No claim of a newly evaluated bound, successful high gate, finite determinant or removed independent mean is made.
