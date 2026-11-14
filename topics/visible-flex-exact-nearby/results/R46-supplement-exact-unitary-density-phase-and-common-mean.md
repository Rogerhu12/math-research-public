# R46 supplement: exact unitary density phases, common mean and complete source ports

**The actual diagonal density phase is now removed without a base growth
factor.** This is the true nonconstant chronological phase on each of
the four branch/sign channels, not its scalar average and not a finite
Fourier approximation. The physical common scalar mean can also be
separated by an exact Fourier-diagonal unitary.

For \(N=2^{20}\), the same exact diagonal propagation and its inverse
have balanced \(H_N^j\) norms
\[
 G_0=1,\qquad G_1<1.287395,\qquad
 G_2<1.372688,\qquad G_3<1.399461.                         \tag{UP.1}
\]
The inequalities follow already from the previous complete real jets;
the new same-label log-jet report can only improve them. The actual
native consumer below uses those improved jets with every original
field and true-reference error retained.

The remaining cross-branch, opposite-cone, low-label and mean equations
are not solved by this phase change. They remain exact terms in
(UP.11). In particular (UP.1) is not a bound for the complete negative
propagator and does not itself replace the complete returned \(R_*\).

## 1. Same actual system and the balanced variable

Use the complete fixed-label density identity from
[the actual high-density Volterra theorem](R46-supplement-actual-fixed-label-high-density-Volterra.md).
Its physical density is
\[
 \kappa=\mathcal F/\mu,\qquad x=4\theta,\quad
 D=-i\partial_x,\quad J_\sigma=H_\sigma',\quad
 S_\sigma=H_\sigma^{-1}.
\]
The native geometry field also named kappa is \(-K_{\rm target}\);
it is not the coefficient used here.

For prescribed complete low histories the exact high equation is
\[
 X_{\sigma,H}'=\sum_\tau K_{\sigma\tau}X_{\tau,H}+F_{\sigma,H},
 \qquad
 K_{\sigma\tau}={i\sigma\over8}
 P_H\mathcal D_{H_\sigma}M_\kappa C_{S_\tau}D^{-1}P_H,
                                                               \tag{UP.2}
\]
where \(\mathcal D_H=H'C_H=(C_{H^{-1}})^*\). The left projection is
in the receiving label and the right one is in the source label.
Neither is moved through a map.

Define the balanced nonzero variable
\[
 Z_\sigma=|D|^{-1/2}X_{\sigma,H}.
\]
This changes the Sobolev index of the density by a half. It does not
assert that the original raw density L2 norm is the balanced base
norm. The corresponding physical comparison is paid in Section 7.

Let \(P_{\epsilon,N}\) project onto the entire infinite set
\(\epsilon n\ge N\), with \(\epsilon=\pm1\). In the diagonal branch,
the exact multiplication identity gives
\[
 \mathcal D_{H_\sigma}M_\kappa C_{S_\sigma}
 =M_{a_\sigma},\qquad
 a_\sigma(r,x)=J_\sigma(r,x)\kappa(r,H_\sigma(r,x)).
                                                               \tag{UP.3}
\]
All \(a_\sigma\) are real for real \(r,x\). On one fixed sign channel,
\[
 A_{\sigma,\epsilon,N}(r)
 ={\sigma\epsilon\over8}|D|^{-1/2}P_{\epsilon,N}
        M_{a_\sigma(r)}P_{\epsilon,N}|D|^{-1/2}             \tag{UP.4}
\]
is a bounded self-adjoint operator. The exact same-channel generator
is \(iA_{\sigma,\epsilon,N}\).

For every pair of times, define \(U_{\sigma,\epsilon}(t,s)\) by
\[
 \partial_tU_{\sigma,\epsilon}(t,s)
   =iA_{\sigma,\epsilon,N}(t)U_{\sigma,\epsilon}(t,s),
 \qquad U_{\sigma,\epsilon}(s,s)=I .                       \tag{UP.5}
\]
The complete actual coefficient bounds make (UP.4) integrable in
operator norm; the ordinary time-dependent bounded-operator equation
therefore defines (UP.5) on the full infinite channel. Differentiating
\(U^*U\), and applying the same argument to the reverse evolution,
gives
\[
 U(t,s)^*U(t,s)=U(t,s)U(t,s)^*=I.
\]
Thus its base norm and inverse norm equal one, for every subinterval
and both time directions. No smallness of the real phase is needed.

## 2. The exact common physical mean

The map \(H_\sigma\) is a degree-one orientation-preserving circle
diffeomorphism. Change of variables in (UP.3) gives the exact identity
\[
 \langle a_\sigma(r)\rangle
 ={1\over2\pi}\int J_\sigma(r,x)\kappa(r,H_\sigma(r,x))\,dx
 =\langle\kappa(r)\rangle.                                \tag{UP.6}
\]
The two branch means are the same before the prescribed factor
\(\sigma\epsilon\). This identity does not approximate \(a_\sigma\)
by its mean.

Put \(\Gamma(t,s)=\int_s^t\langle\kappa(r)\rangle\,dr\).
The common scalar part of the phase is exactly
\[
 E_{\sigma,\epsilon}(t,s)
 =\exp\!\left({i\sigma\epsilon\over8}\Gamma(t,s)|D|^{-1}\right).
                                                               \tag{UP.7}
\]
It is unitary in every \(H_N^s\), since it is a Fourier multiplier of
modulus one. Writing \(U=EW\), the equation for \(W\) has the exact
self-adjoint generator
\[
 E^*{\sigma\epsilon\over8}|D|^{-1/2}P_{\epsilon,N}
 M_{a_\sigma-\langle\kappa\rangle}P_{\epsilon,N}|D|^{-1/2}E.
                                                               \tag{UP.8}
\]
Every real nonmean coefficient and its time ordering remains in
(UP.8). Neither an absolute scalar growth fee nor a positive angular
strip loss is introduced by (UP.7).

The physical height/flux means \(\alpha,c\) below are distinct from
this coefficient mean. They are not transformed into (UP.7).

## 3. The full exact gauged equation

Let \(U_d\) be the direct sum of the four operators (UP.5). Write
\[
 G=|D|^{-1/2}K|D|^{1/2}
     =iA_d+G_{\rm off}
\]
on the two high density components, split into the four sign channels.
Here \(G_{\rm off}\) contains every cross-branch term and every
same-branch opposite-sign term. This is an exact subtraction, with the
original projections and adjoint density factors retained.

For a common reference time \(s\), set
\[
 W(t)=U_d(t,s)^*Z(t).
\]
Its exact equation is
\[
 \boxed{\quad
 W'=U_d^*G_{\rm off}U_dW
       +U_d^*|D|^{-1/2}F_H .
 \quad}                                                   \tag{UP.9}
\]
Consequently the diagonal real phase causes no balanced base
amplification. The remaining operator in (UP.9) still contains the
actual cross-branch oscillation and all opposite-cone interfaces;
there is no assertion here that its norm is small.

The right-hand side \(F_H\) is the original
\[
 F_{\sigma,H}={\sigma\over2}
 P_H\mathcal D_{H_\sigma}(mf-\kappa w_L),\qquad
 m=\mu^{-1/2}.                                            \tag{UP.10}
\]
It includes every complete nonzero low-label history and both
independent means. The changes (UP.4)--(UP.9) leave their equations
unchanged:
\[
 \begin{split}
 \alpha'&={1\over2}\langle mf-\kappa w\rangle,\\
 c'&=-{\alpha'\over4}\langle S_+-S_-\rangle
      -{1\over4}\sum_\sigma
       \left\langle C_{S_\sigma}\partial_x^{-1}
                     P_{\ne0}X_\sigma'\right\rangle,\\
 P_LX_\sigma'&={\sigma\over2}P_L\mathcal D_{H_\sigma}
                            (mf-\kappa w).
 \end{split}                                               \tag{UP.11}
\]
In (UP.11), the high part is reconstructed as
\(|D|^{1/2}U_dW\). Thus high-to-low and high-to-mean feedback is still
present, rather than implicitly prescribed zero.

## 4. Finite tame Sobolev bounds without a new exponent

Set
\[
 J_N=(1+D^2/N^2)^{1/2},\qquad
 \|z\|_{H_N^s}=\|J_N^sz\|_2 .
\]
For \(|n|\ge N\),
\[
 \|J_N^{1/2}|D|^{-1/2}\|\le {2^{1/4}\over\sqrt N}.
                                                               \tag{UP.12}
\]
Let \(M_j(r)\) bound multiplication by \(a_\sigma(r)\) on
\(H_N^j\), uniformly in \(\sigma\), and interpolate the integer
multipliers at half indices. From the two outer factors in (UP.4),
\[
 \|A_{\sigma,\epsilon,N}(r)\|_{H_N^{j-1}\to H_N^j}
 \le{\sqrt2\over8N}M_{j-1/2}(r).                          \tag{UP.13}
\]

All required derivative constants are explicit complete real bounds.
If \(h_j\) bounds \(H_\sigma^{(j)}\), \(h_1=C_r\), and the actual
field strip is \(s_f\), then
\[
 \begin{split}
 |a_\sigma|&\le C_rM_\kappa,\\
 |a_\sigma'|&\le(h_2+C_r^2/s_f)M_\kappa,\\
 |a_\sigma''|&\le(h_3+3C_rh_2/s_f+2C_r^3/s_f^2)M_\kappa,\\
 |a_\sigma'''|&\le
 \left[h_4+(4C_rh_3+3h_2^2)/s_f
        +12C_r^2h_2/s_f^2+6C_r^4/s_f^3\right]M_\kappa.
 \end{split}                                               \tag{UP.14}
\]
These are full chain and product derivatives, not grid samples.
The physical field variable is converted to \(x=4\theta\) before
applying \(s_f\); here \(s_f=1/160\).
All \(h_j\) concern real angles and all pairs of times. They do not
enlarge any complex-flow domain.

The existing weighted finite Leibniz matrices, with entries
\(\binom jk h_{j-k}/N^{j-k}\) for the appropriate derivative bounds,
give each complete multiplier norm. The common radial majorant has
\[
 Q_\kappa=\int M_\kappa(r)\,dr<113197.898280.
\]
Let \(k_j\) be the resulting integral of (UP.13). The exact Duhamel
identity and the base unitarity give successively
\[
 G_0=1,\qquad
 \|U-I\|_{H_N^{j-1}\to H_N^j}\le k_jG_{j-1},\qquad
 G_j=1+k_jG_{j-1}.                                       \tag{UP.15}
\]
At each level only the previously proved lower-level norm is used.
There is no high-order Gronwall exponent. Reversed time gives the
same inverse bounds. Hilbert interpolation gives every intermediate
window, including the half indices needed for physical reconstruction.

For completeness, with the earlier real jets the directed values at
\(N=2^{20}\) were
\[
 \begin{split}
 k_1&<0.287394153,&G_1&<1.287394153,\\
 k_2&<0.289489676,&G_2&<1.372687316,\\
 k_3&<0.291006303,&G_3&<1.399460661.
 \end{split}
\]
The native record uses the new same-label accepted jets and saves the
corresponding full rows also at \(N=1,4096,65536,2^{30},2^{40}\).
In particular it specifies the all-nonzero-cone case \(N=1\), although
no small norm is asserted in its higher windows.

## 5. Actual first phase, chronological ordering and the sharp cutoff edge

The first Duhamel term in (UP.5) is precisely
\[
 {i\sigma\epsilon\over8}|D|^{-1/2}P_{\epsilon,N}
 M_{\int_s^t a_\sigma(r)\,dr}
 P_{\epsilon,N}|D|^{-1/2}.                               \tag{UP.16}
\]
Thus this phase change preserves the original true first-phase
function in the earlier density theorem. It neither substitutes
\(\beta\) for \(b\) nor claims that this one strict contribution is
the entire final-circle finite part.

Put \(\rho_0=C_rQ_\kappa/(8N)\). The complete remainder after
(UP.16) satisfies
\[
 \begin{split}
 \|U-I-i\!\int A\|_{0\to0}
 &\le\min(\rho_0^2/2,\,2+\rho_0),\\
 \|U-I-i\!\int A\|_{0\to2},
 \quad\|U-I-i\!\int A\|_{-2\to0}
 &\le k_2k_1/2.                                         \tag{UP.17}
 \end{split}
\]
The exact two-Duhamel simplex has the factor one half because the
two pointwise gain bounds use the same positive majorant
\(M_\kappa(r)\). The final propagator in that identity is used only
at its exact base norm one. Its adjoint/reversed identity proves
the opposite window. Interpolation gives the two \(4/3\) windows.

The frozen exponential \(\exp(i\int A)\) is also unitary and obeys
the same tame estimates. The difference from the chronological phase
therefore has the sum of the two bounds in (UP.17). One may alternatively
use the exact base estimate
\[
 \|U(t,s)-e^{i\int_s^t A}\|
 \le{1\over2}\int_s^t\int_s^r\|[A(r),A(v)]\|\,dv\,dr,      \tag{UP.18}
\]
obtained by differentiating the exponential under its unitary integral
formula.

There is a necessary cutoff qualification to (UP.18). For complete
one-cone operators \(A,B\), with \(P=P_{\epsilon,N}\) and
\(L=\Pi_\epsilon-P\),
\[
 [PAP,PBP]
 =P[A,B]P-PALBP+PBLAP.                                   \tag{UP.19}
\]
The last two terms are exact finite-head paths. They cannot be omitted
when claiming a stronger order for the commutator.

For example, on the positive cone take the actual symmetrized
multipliers with \(a=2\cos x\) and \(b=2\sin x\). On the first retained
mode,
\[
 \langle e_N,[A_N(a),A_N(b)]e_N\rangle
   =-{2i\over N(N+1)}.                                  \tag{UP.20}
\]
This is of order \(N^{-2}\). The unprojected positive-cone expression
at \(N>1\) has the additional entering-head path and is
\(4i/[N(N^2-1)]\), of order \(N^{-3}\).
The native report consequently retains (UP.19) and makes no
uniform order-three claim for a hard-projected chronological phase.

## 6. Every ordinary source and complete low-height drive

The gauge has base norm one. Hence
\[
 \|U_d^*|D|^{-1/2}F_H\|_2
 \le N^{-1/2}\|F_H\|_2 .
\]
The original physical ordinary source norm is \(L^1(dr;H_N^j)\)
of \(f\), with \(x=4\theta\). It is not a renamed weak residual.
Let \(d_j\) be the full actual density-pullback bound and
\(M_{j,N}(m)\) the original complete multiplier bound. Then the exact
gauged forcing column has norm at most
\[
 {G_jd_jM_{j,N}(m)\over\sqrt{2N}}.                         \tag{UP.21}
\]
For the complete prescribed low-height history, measured in
\(L^\infty(dr;H_N^j)\), its integrated forcing column is at most
\[
 {G_jd_jM_{j,N}(1)Q_\kappa\over\sqrt{2N}}.                 \tag{UP.22}
\]
The factor \(\sqrt2\) is the Hilbert sum over the two branch source
rows with coefficients \(1/2\). These are norms of the exact
forcing in (UP.9), not the solution operator of its remaining
coupled problem.

The low-height reconstruction still contains all nonzero label modes
below \(N\), the independent physical flux mean \(\alpha\), and the
height integration constant \(c\). Both their input and their returned
equations (UP.11) are retained.

## 7. Physical reconstruction and scope

The unchanged physical identities are
\[
 \begin{split}
 w&=c+{\alpha\over4}(S_+-S_-)
       -{i\over4}\sum_\sigma C_{S_\sigma}D^{-1}
                      (X_\sigma-\sigma\alpha),\\
 y_\sigma&=S_\sigma'(X_\sigma\circ S_\sigma),\quad
 z=y_++y_-,\quad \zeta=y_+-y_-,\\
 u&=mw,\qquad p=\sqrt\mu\,\zeta-Tu .
 \end{split}                                               \tag{UP.23}
\]
For the high contribution \(X_H=|D|^{1/2}U_dW\),
\[
 \|u_H\|_2
 \le {M_m\sqrt{C_r}\over2\sqrt{2N}}\|W\|_2.                 \tag{UP.24}
\]
The raw high density and physical momentum require a half higher
balanced index:
\[
 \begin{split}
 \|X_H\|_2&\le\sqrt N\,G_{1/2}\|W\|_{H_N^{1/2}},\\
 \|p_H\|_2&\le
 \left[M_{\sqrt\mu}\sqrt{2C_rN}\,G_{1/2}
       +{M_TM_m\sqrt{C_r}\over2\sqrt{2N}}\right]
          \|W\|_{H_N^{1/2}}.                             \tag{UP.25}
 \end{split}
\]
Thus balanced base unitarity has not been silently relabeled as raw
Cauchy L2 unitarity. The low part of (UP.23) remains separate and exact.

All statements concern the same original actual metric and its
complete real parameter box, all real angles, every pair of strict
times and both directions. The density source, physical \(dr\),
all cutoff projections, both means, and every sign channel remain
fixed. No complete negative evolution bound, new full returned
remainder, finite-head inverse, full feedback inverse or new complex
strip is granted by this local phase result.

## 8. Reproduction

The light native consumer uses the unchanged complete 215-cell field
budget through the high-density theorem, and the new complete
550-segment real log-jet certificate. Its only arithmetic consists
of the finite derivative/multiplier triangles and the exact
unitarity-based formulas above.

~~~bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python3 scripts/fourfold_actual_density_unitary_first_phase.py \
  --out notes/2026-11-13-actual-density-unitary-first-phase.json
~~~

Source: scripts/fourfold_actual_density_unitary_first_phase.py.  
Native report: notes/2026-11-13-actual-density-unitary-first-phase.json.

The full mean/head equations and the exact cutoff commutator are
saved in the report alongside every source and reconstruction
constant, rather than inferred from a finite matrix experiment.

