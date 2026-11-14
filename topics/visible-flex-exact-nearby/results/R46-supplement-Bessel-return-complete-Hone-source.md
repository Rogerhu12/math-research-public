# R46 supplement: Bessel-coordinate budget for the complete returned H1 source

**Proved for the original complete return at the actual R101 parameter.**
The improved complete density-coordinate norms and the same-model word
bound from [the complete returned rebudget](R46-supplement-complete-return-Bessel-rebudget-and-explicit-cutoff.md)
now act on every ordinary source, weak positive load and independent
regular flux in
[the complete H1 source theorem](R46-supplement-complete-returned-Hone-source-and-high-particular.md).
No source map, background, final label, phase or projection is changed.

The final unscaled H1 constants are:

| Physical source column | Complete final H1 bound |
|---|---:|
| Strict-core ordinary source | \(1.386178\,10^{226}\) |
| Either canonical-root ordinary source | \(1.690577\,10^{228}\) |
| Either correctly transformed graph source | \(1.582836\,10^{214}\) |
| Five negative spaces, Euclidean direct sum | \(2.390877\,10^{228}\) |
| Paired positive ordinary loads | \(9.346752\,10^{140}\) |
| Paired positive weak loads | \(4.672905\,10^{140}\) |
| Two independent physical regular fluxes | \(3.746021\,10^{138}\) |

The same specified high inverse is now
\[
 \|A_H^{-1}\|_{P_HH^1\longrightarrow P_HL^2}
 <15.928899573,\qquad N_H=2^{1682}.                         \tag{BHS.1}
\]
Applying (BHS.1) to the complete H1 right-hand side gives a high
particular with prescribed zero final head. It does not solve the
remaining head equations.

## 1. Identical operator, source units and norm scale

The comparison scale is still \(N_0=2^{20}\):
\[
 \|u\|_{H_{N_0}^s}
 =\|(1+D_x^2/N_0^2)^{s/2}u\|_2 .
\]
It is distinct from the high projection cutoff \(N_H\).
A scalar regular port has weight one in every boundary direct sum.

The underlying metric is the same original affine family, with
\(p_5=-7789843107295549/4611686018427387904\) and
\(|p-p_5|\le10^{-9}\). The geometric/source bounds are uniform on that
entire box. The final rotation and arithmetic high inverse are used at
the actual point \(p_\infty\); no all-parameter inverse is inferred.

The negative sources keep the following exact units.

| Region | Complete stronger physical source norm |
|---|---|
| Whole strict core | \(L^1(dr;H_{N_0}^{1/2})\) of the original scalar source, \(x=4\theta\) |
| Either canonical root | \(L^1(d\xi;H_{N_0}^{2/3})\) of the exact canonical scalar |
| Either tilted graph | \(L^1(dt;H_{N_0}^{1/2})\) of \(f_t=(L-\chi)f_c/q\) |

The two root/graph descriptions of a single physical source must use
the same permitted extension. These anisotropic norms are not freely
interchanged by the foliation map. Splitting the core at \(r=0\) is
exact: the two resulting radial L1 norms sum to the original norm.

The positive ordinary norm is the paired Euclidean norm of
\(L^2(dy;H_\phi^{1/3})\) collar sources. The positive weak norm is the
paired Euclidean norm of
\((F_y,F_\phi/\sqrt y)\) in
\(L^2(dy;(H_\phi^1)^2)\), with the original weak load convention.
Each solution uses its complete original positive cap. The Piola
density, height-gradient correction, mean charge and both independent
physical normalized regular fluxes are retained. An independent boundary
vector trace is not bounded by the displayed bulk weak-source norm.
Each stronger norm dominates its previously proved base source norm
with constant one.

## 2. Updated norms on the identical complete model

Let \(\mathscr S\) be the complete onto-unitary negative scattering and
\(\mathscr S_0=\left(\begin{smallmatrix}0&U\\V&0\end{smallmatrix}\right)\)
the exact same model used in the complete word theorem. The new
factor-by-factor estimate, including every mean, gives
\[
 \|\mathscr S_0\|_{H_{N_0}^1\to H_{N_0}^1}
 \le T_*<2.281912542\,10^{23}.                              \tag{BHS.2}
\]
This follows from a bound valid on the entire interval \(|s|\le2\).
It is not an inference from the actual scattering's L2 unitarity.
The actual strong error is unchanged:
\[
 \|\mathscr S-\mathscr S_0\|_{L^2\to H_{N_0}^{4/3}},
 \quad
 \|\mathscr S-\mathscr S_0\|_{H_{N_0}^{-4/3}\to L^2}
 \le R_S<2.983108914\,10^{130}.                            \tag{BHS.3}
\]
All first-root and second-root model mean corrections remain inside
these complete statements. The old full positive-cap remainder is
also unchanged:
\[
 C_{\rm cap}<769807285232.                                \tag{BHS.4}
\]

The Bessel trace-energy proof gives bounds on the original
\(\Lambda_n=\max(1,|n|)\) density coordinates; the auxiliary Bessel
weight has already been changed back, with its \(2^{1/4}\) fee paid.
For the final actual label \(Q_C\), its inverse and the required
adjoints,
\[
 q_0<3.099734290,\qquad q_2<326.440786040.
\]
Interpolation on the same full realization gives
\[
 \|Q_C\|_{H_{N_0}^1\to H_{N_0}^1}
 \le q_1=\sqrt{q_0q_2}<31.810056554.                        \tag{BHS.5}
\]
No mean is removed in (BHS.5). The unscaled conversion satisfies
\[
 \|Q_Cu\|_{H^1}\le N_0q_1\|u\|_{H_{N_0}^1},
 \qquad N_0q_1<33355261.861.                              \tag{BHS.6}
\]
On the augmented regular slots the identity is bounded by the same
constant, since it exceeds one.

## 3. Complete affine scattering source

For an actual particular with both Cauchy rows \(g=(g_+,g_-)\) at the
near root, its exact affine source is respectively
\[
 s=(g_-,0)-\mathscr S(g_+,0),\qquad
 s=(0,g_-)-\mathscr S(0,g_+).                              \tag{BHS.7}
\]
The exact physical radial reflection preserves the angular label and
the full canonical angle. Its conormal sign and constant branch
permutation remain part of (BHS.7).

In the first formula, replacing \(\mathscr S\) by \(\mathscr S_0\)
sends \(g\) to \((g_-,-Vg_+)\); the second formula is analogous.
Thus the Hilbert direct-sum norm uses the single factor
\(\max(1,T_*)\), without an extra triangle factor:
\[
 \|s\|_{H_{N_0}^1}
 \le\max(1,T_*)\|g\|_{H_{N_0}^1}+R_S\|g\|_{L^2}.          \tag{BHS.8}
\]
The second term uses \(H_{N_0}^{4/3}\hookrightarrow H_{N_0}^1\).

The old complete source proof already supplies the true near-endpoint
columns \(G_{0,j},G_{1,j}\) in those two norms. They include all strict
215 cells, both root/graph connectors, both Airy rows and means.
They are reused without recomputation:
\[
 S_{1,j}=\max(1,T_*)G_{1,j}+R_SG_{0,j}.                    \tag{BHS.9}
\]
The stronger positive columns and regular columns are likewise the
existing full source maps. Their independent base bounds \(S_{0,j}\)
are retained, rather than re-estimated by the large strong bound.

## 4. Ordered actual triangular and cap map

The final affine source is obtained in precisely the order
\[
 \mathcal U_{\rm cone}\,
 \operatorname{diag}(Q_C,I,I_{\rm reg})\,L_eR_{\rm cap}^*
 \bigl[(s_{\rm neg},\,i\sqrt{\pi c_A/\ell}\lambda)-h_{\rm cap}\bigr],
                                                               \tag{BHS.10}
\]
where \(\mathcal U_{\rm cone}\) consists of the same unitary rotation
and complex-linear reflection. It does not discard either Fourier
cone.

The exact expansion
\[
 L_eR_{\rm cap}^*
 =L_m[-I+(R_{\rm cap}^*+I)]
   +(L_e-L_m)R_{\rm cap}^*                                \tag{BHS.11}
\]
keeps the order of every factor. Here \(L_m\) has H1 norm at most
\(1+T_*\). The middle remainder in the first term is base-to-H1
bounded by \(C_{\rm cap}\). The last factor \(R_{\rm cap}^*\) in
the second term uses only its full base unitarity, and \(L_e-L_m\)
uses \(R_S\). Consequently
\[
 \|L_eR_{\rm cap}^*h\|_{H_{N_0}^1}
 \le (1+T_*)\|h\|_{H_{N_0}^1}
   +[(1+T_*)C_{\rm cap}+R_S]\|h\|_{L^2}.                 \tag{BHS.12}
\]
Neither the actual cap nor the actual triangular map has been assumed
unitary in H1.

Combining (BHS.6) and (BHS.12), the complete final source column is
\[
 C_{1,j}=N_0\sqrt{q_0q_2}
 \left[(1+T_*)S_{1,j}
       +\bigl((1+T_*)C_{\rm cap}+R_S\bigr)S_{0,j}\right].
                                                               \tag{BHS.13}
\]
The independent base column remains \(C_{0,j}=2q_0S_{0,j}\).
For the five negative inputs, Cauchy--Schwarz gives
\[
 C_{\rm neg}=
 \sqrt{C_{\rm core}^2+2C_{\rm root}^2+2C_{\rm graph}^2}.
                                                               \tag{BHS.14}
\]
This is the Euclidean direct sum of the actual source spaces, not the
sum of five unrelated extensions.

The table at the beginning is (BHS.13)--(BHS.14), evaluated with
directed Arb arithmetic. Relative to the old complete H1 theorem,
every negative column improves by a factor greater than
\(6.009712942\,10^{38}\); every positive and regular column improves
by a factor greater than \(4863.617682\). The remaining large
negative bound explicitly contains the unchanged true \(R_S\).
This update does not claim to have improved that propagation error.

## 5. Exact high particular and the remaining head

The new complete return certificate proves (BHS.1) for the actual
high projection. A source column \(C_{1,j}\) therefore has
zero-final-head high-particular L2 bound
\(15.928899573\,C_{1,j}\). For example, the negative five-space bound is
less than \(3.808403\,10^{229}\).

The physical boundary amplitude reconstruction retains every low-mode
path and costs at most
\[
 2q_0<6.199468579.
\]
These factors are recorded separately in the native report. Prescribing
zero final head does not prescribe zero physical head after the exact
coordinate and triangular maps.

For an arbitrary head value the equation is still
\[
 u_H=A_H^{-1}(P_Hg-A_{HL}u_L),
\]
and the full low equation includes its exact Schur complement and
ordinary affine source. The head has complex dimension \(2^{1684}\).
No head inverse, numerically tractable cutoff, complete feedback
inverse, final C2 surface, fixed positive angular weight, or transfer
to the new deep-tail profile is asserted here.

## 6. Reproduction and scope

The light consumer uses the complete prior H1 source report, the new
complete return report, and the proved v2 Bessel-coordinate report.
It checks their actual family, parameter scope, scale and shared
input identities; every source norm is copied verbatim. No original
geometry or complete coefficient field is rerun.

~~~bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python3 scripts/fourfold_actual_return_Bessel_Hone_source.py \
  --out notes/2026-11-13-actual-return-Bessel-Hone-source.json
~~~

Source: scripts/fourfold_actual_return_Bessel_Hone_source.py.  
Native report: notes/2026-11-13-actual-return-Bessel-Hone-source.json.

All six consistency/improvement gates passed. The record preserves
every complete physical source column, both means, both regular
slots, both Fourier cones, and all exact head/high crossings.

