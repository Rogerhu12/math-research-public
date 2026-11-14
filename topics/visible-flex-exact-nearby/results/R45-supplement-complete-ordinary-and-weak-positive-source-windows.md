# R45 supplement: complete ordinary and weak positive-cap source windows

**Proved for the same full original cap and whole parameter box as the
exact positive-cap Airy/contact certificate.** Let \(h_{f,F}\) be its
actual affine outgoing wave with zero incoming wave. The root mean and
the independent balanced regular scalar belong to this wave. For
\(0\le s\le4/3\), the complete source operators satisfy

\[
 \begin{split}
 \|h_{f,0}\|_{H_\phi^s\oplus\mathbb C}
   &\le T_s\|f\|_{L^2(dy;H_\phi^{\,s-2/3})},\\
 \|h_{0,F}\|_{H_\phi^s\oplus\mathbb C}
   &\le W_s
       \|(F_y,F_\phi/\sqrt y)\|_{L^2(dy;(H_\phi^s)^2)}.
 \end{split}                                                   \tag{S.1}
\]

The source is supported in the same exact canonical collar
\(0\le y\le H=1/4000\). The solution remains on the entire actual cap,
including its true infinite-tail Robin realization. No boundary is
inserted at \(y=H\). In particular,

\[
 \begin{array}{c|cc}
 s&T_s&W_s\\ \hline
 0&377.600482&188.781182\\
 1/2&12602704.653&6300716.207\\
 1&420624899727&210291219076\\
 4/3&436029417813618&217992700711235 .
 \end{array}                                                   \tag{S.2}
\]

All table entries are upward roundings. Thus the ordinary source needed
for a full \(H^1\) outgoing wave is \(L^2_yH_\phi^{1/3}\), and the weak
source pair needed for that wave is \(L^2_y(H_\phi^1)^2\). A source in
only the older \(L^2_yH_\phi^{-2/3}\) norm has not acquired a free
\(H^1\) output.

The theorem uses the old original full cap. It does not transfer the
cap realization or source reconstruction to a newly changed deep tail.
It does not solve the final mean/regular compatibility equations,
the complete finite head, or the full returned inverse.

## 1. Fixed realization, units, and already proved inputs

Use [the exact positive-cap Airy/contact theorem](R45-supplement-actual-exact-positive-cap-Airy-contact-and-four-thirds.md),
including its equations (A.3), (A.12), (A.17)–(A.19), and (A.28)–(A.30).
The parameter is the same exact affine family,

\[
 p_5=-7789843107295549/4611686018427387904,\qquad
 |p-p_5|\le10^{-9}.                                           \tag{S.3}
\]

The true canonical operator is
\[
 P_+=-\partial_y^2-y\partial_\phi^2-V(-y,\phi).
\]
Set \(\mathcal L=\operatorname{diag}(\langle D_\phi\rangle,1)\)
on the root-circle wave and independent regular scalar.
All root Sobolev norms initially use the actual physical root measure
\(d\phi\), with frequencies \(\lambda_n=q_c|n|\). The scalar regular
normalization is exactly the one in (A.29). The coefficient period
satisfies
\[
 38.8838516058692<q_c<38.8838516230918.                         \tag{S.4}
\]

The following constants are complete full-cap inputs, including every
generated Fourier mode and both finite slots:
\[
 \begin{gathered}
 C_s<140.771774805,\quad C_w<70.378781910,\quad
 d=1-GH>.96558155908957,\\
 c_A=-\operatorname{Ai}'(0)/\operatorname{Ai}(0),\qquad
 c=c_A^{-1/2},\qquad N=\pi/(2c)<1.341179657,\\
 R=R_+\ \hbox{onto unitary},\qquad E=R+I,\\
 \|\mathcal L^{4/3}E\|,\ \|E\mathcal L^{4/3}\|
     \le C_E<769807285232 .
 \end{gathered}                                               \tag{S.5}
\]
Here \(N\) bounds contact-to-one-wave on all root frequencies, including
the actual mean, and on the regular scalar. The full ordinary Ai trial
residual has
\[
 \|F_{\rm tr}\mathcal L^{4/3}\|_{L^2\oplus\mathbb C
                 \longrightarrow X}\le F_*<2038681950,
 \qquad X=L^2_yH_\phi^{-2/3}.                                 \tag{S.6}
\]
It is zero on the root-mean and regular input slots. Its other columns
include the full potential, both cutoff terms, all opposite-sign
outputs, and the complete infinite Fourier tail.

No change of operator, parameter, frame, or boundary graph occurs in
the argument below.

## 2. Complete incoming Poisson and zero-incoming Green operators

Let \(P\) be the homogeneous solution on the full cap whose incoming
wave is \(a\) and outgoing wave is \(Ra\). For every nonzero frequency
the root height coefficient of either wave has \(H^{1/3}\) multiplier
bounded by
\[
 2c\operatorname{Ai}(0)
       (1+q_{c,-}^{-2})^{1/6}<c.
\]
The actual root-mean coefficient is \(c\). The regular height
coefficient is \(1/\sqrt{\pi c_A}<c\). These are the exact original
columns: the nonzero assertion uses
\(\operatorname{Bi}(0)=\sqrt3\operatorname{Ai}(0)\).
Since \(\|Ra\|=\|a\|\), the full height trace of \(Pa\) obeys
\[
 \|\operatorname{trace}(Pa)\|_{H_\phi^{1/3}\oplus\mathbb C}
       \le2c\|a\|.                                         \tag{S.7}
\]
The earlier complete Poisson estimates therefore give
\[
 \|P\|_{L^2\oplus\mathbb C\to Y_0}\le P_0:=2cC_s,\qquad
 \|\nabla_{C_0}P\|_{L^2\oplus\mathbb C\to L^2}
       \le P_{w0}:=2cC_w,                                  \tag{S.8}
\]
where
\[
 Y_0=L^2_yH_\phi^{2/3},\qquad
 \nabla_{C_0}u=(u_y,\sqrt y\,u_\phi).
\]
The actual bounds are \(P_0<329.745215\) and \(P_{w0}<164.855964\).

Let \(G_D\) be the same full-cap Dirichlet Green operator with zero
root height and zero independent regular height. Its energy is the
original full grounded form. The root-zero trace inequalities of
(A.13) and (A.16), followed by the full variational identity, give
\[
 \begin{split}
 \|G_Df\|_{Y_0}
    &\le \sqrt{4+H^2}\,d^{-1}\sqrt{\mathfrak b(G_Df,G_Df)},\\
 \mathfrak b(G_Df,G_Df)
    &=\langle f,G_Df\rangle
      \le\|f\|_X\|G_Df\|_{Y_0}.
 \end{split}
\]
Thus, with \(C_D=\sqrt{4+H^2}/d\),
\[
 \sqrt{\mathfrak b(G_Df,G_Df)}\le C_D\|f\|_X,\quad
 \|G_Df\|_{Y_0}\le C_D^2\|f\|_X,\quad
 \|\nabla_{C_0}G_Df\|_2\le(C_D/d)\|f\|_X.                   \tag{S.9}
\]
In particular \(C_D^2<4.290245\). This full Green operator is not the
inverse of a problem cut off at the end of the local collar.

The incoming wave of \(G_Df\), which has zero height traces, is bounded
by \(NC_s\|f\|_X\), using the complete contact theorem. Subtract the
homogeneous solution with precisely that incoming wave. The result
\(Zf\) is the actual forced solution with incoming zero, so
\[
 \begin{split}
 \|Z\|_{X\to Y_0}
   &\le Z_0:=C_D^2+P_0NC_s<62260.266078,\\
 \|\nabla_{C_0}Z\|_{X\to L^2}
   &\le Z_w:=C_D/d+P_{w0}NC_s<31126.990652 .
 \end{split}                                                \tag{S.10}
\]
This construction retains both full mean contacts. In particular it
does not replace the regular height/flux equation by a homogeneous
condition when a nonzero source is present.

## 3. Exact incoming identity and the negative Poisson window

Let \(\Pi_{\ne0}\) project only the incoming root circle onto its nonzero
frequencies; let \(\Pi_f=I-\Pi_{\ne0}\) retain the root mean and regular
scalar. The trial from (A.21) has incoming \(\Pi_{\ne0}\), outgoing
\(-\Pi_{\ne0}\), and full source \(F_{\rm tr}\). Consequently
\[
 \boxed{\quad P\Pi_{\ne0}=U_{\rm tr}-ZF_{\rm tr}.\quad}        \tag{S.11}
\]
Both sides solve the same full problem and have exactly the same
incoming data. This is an identity, not an approximate inverse of the
trial's incoming trace. The independent column \(P\Pi_f\) is kept, with
all its infinite output rows.

Put \(r_q=(1+q_{c,-}^{-2})^{1/3}\). The Airy identities
\[
 \int_0^\infty\operatorname{Ai}(z)^2\,dz
       =\operatorname{Ai}'(0)^2,\qquad
 \int_0^\infty
       [\operatorname{Ai}'(z)^2+z\operatorname{Ai}(z)^2]\,dz
       =-\operatorname{Ai}(0)\operatorname{Ai}'(0)           \tag{S.12}
\]
follow by integrating respectively
\((z\operatorname{Ai}^2-\operatorname{Ai}'^2)'\) and
\((\operatorname{Ai}\operatorname{Ai}')'\). The actual positive-axis
Airy decay already proved in R96 justifies the endpoints at infinity.

For the exact cutoff trial,
\[
 U_{\rm tr}=2ic\lambda^{-1/3}
          \operatorname{Ai}(y\lambda^{2/3})\chi(y),
 \qquad 0\le\chi\le1,\quad \|\chi'\|_\infty\le15000.
\]
Integrating in \(y\) before taking the uniform frequency bound gives
\[
 \|U_{\rm tr}\|_{H^{-4/3}\oplus\mathbb C
                   \to L^2_yH_\phi^{-2/3}}
       \le T_{\rm Ai}:=2c|\operatorname{Ai}'(0)|r_q
       <.606394793.                                       \tag{S.13}
\]
For the complete energy gradient, the uncut terms use the second
identity in (S.12). The derivative of the cutoff gives one additional
radial component. Therefore
\[
 \begin{split}
 \|\nabla_{C_0}U_{\rm tr}\|_{H^{-4/3}\oplus\mathbb C
                   \to L^2_y(H_\phi^{-4/3})^2}
 &\le T_{w,\rm Ai}\\
 &:=2c\left[
       \sqrt{\operatorname{Ai}(0)|\operatorname{Ai}'(0)|}
       +\|\chi'\|_\infty|\operatorname{Ai}'(0)|q_{c,-}^{-2/3}
       \right]<793.037725.
 \end{split}                                                \tag{S.14}
\]
The \(\lambda^{-2/3}\) cutoff term was bounded at the true smallest
nonzero physical frequency. No angular differentiation of the full
cap coefficients is invoked.

Combining (S.6), (S.10) and (S.11), and using the norm-one embeddings
\(Y_0\subset L^2H^{-2/3}\) and \(L^2\subset L^2H^{-4/3}\), yields
\[
 \begin{split}
 \|P\|_{H^{-4/3}\oplus\mathbb C\to L^2H^{-2/3}}
    &\le P_{\rm top}
       :=[(T_{\rm Ai}+Z_0F_*)^2+P_0^2]^{1/2},\\
 \|\nabla_{C_0}P\|_{H^{-4/3}\oplus\mathbb C
                         \to L^2(H^{-4/3})^2}
    &\le P_{w,\rm top}
       :=[(T_{w,\rm Ai}+Z_wF_*)^2+P_{w0}^2]^{1/2}.
 \end{split}                                                \tag{S.15}
\]
The sums of squares concern the orthogonal incoming decomposition
\(\Pi_{\ne0}\oplus\Pi_f\). They do not assert orthogonality of the
generated outputs. All low and opposite-sign output rows remain.
The native bounds are
\[
 P_{\rm top}<1.269288807\,10^{14},\qquad
 P_{w,\rm top}<6.345803400\,10^{13}.                         \tag{S.16}
\]

## 4. Full Green pairing and the strong outgoing source

Take a homogeneous \(Pa\) with waves \((a,Ra)\), and a forced solution
\(Z(f,F)\) with waves \((0,h_{f,F})\). Green's formula on the actual
full cap uses precisely the original root and regular frame identity
\[
 F_*^*\left[\frac{\pi c_A}{2i}J_0\right]F_*
      =\operatorname{diag}(I,-I).
\]
Together with the complete ordinary/weak bulk pairing, this gives
\[
 R^*h_{f,F}
       =\varepsilon\,\gamma P^*(f,F),\qquad
 \gamma=\pi c_A/2,\qquad|\varepsilon|=1,                    \tag{S.17}
\]
where \(\varepsilon\) is the fixed sign/phase determined by the same
outward-normal and sesquilinear conventions. No estimate below changes
that convention or redefines \(h_{f,F}\). In \(P^*(f,F)\), the weak
part is the adjoint of \(\nabla_{C_0}P\) paired with
\((F_y,F_\phi/\sqrt y)\). The modulus \(\gamma\) is fixed by the
displayed exact frame form, not chosen by a norm comparison.

Initially (S.17) holds on smooth data and tests. Equations (S.8) and
(S.15) extend the full pairings by density. In particular,
\[
 \begin{array}{c|cc}
  &L^2\text{ output}&H^{4/3}\text{ output}\\ \hline
 \text{ordinary }P^*
     &P_0\|f\|_{L^2H^{-2/3}}&
       P_{\rm top}\|f\|_{L^2H^{2/3}}\\
 \text{weak }P^*
     &P_{w0}\|F\|_{L^2}&
       P_{w,\rm top}\|F\|_{L^2(H^{4/3})^2}.
 \end{array}                                               \tag{S.18}
\]
Here each entry bounds the norm of the corresponding \(P^*\) output,
including the regular scalar.

Since \(R\) is onto unitary, set \(g=P^*(f,F)\) and use
\[
 h_{f,F}=\varepsilon\gamma Rg
      =\varepsilon\gamma(-g+Eg).
\]
The complete gain \(\|\mathcal L^{4/3}E\|\le C_E\) in (S.5)
acts only on the already available base norm of \(g\). Thus
\[
 \begin{split}
 T_{4/3}&=\gamma(P_{\rm top}+C_EP_0),\\
 W_{4/3}&=\gamma(P_{w,\rm top}+C_EP_{w0}).
 \end{split}                                               \tag{S.19}
\]
This proves the last row of (S.2). The argument does not assume an
unproved high-order bound for \(R\), or apply its \(L^2\) unitarity in
a different Sobolev norm.

At order zero retain the independently stronger original complete
bounds \(T_0<377.600482\) and \(W_0<188.781182\).
Complex interpolation of the same actual affine operators between
their two endpoint Bochner spaces gives, for \(0\le s\le4/3\),
\[
 T_s=T_0^{\,1-3s/4}T_{4/3}^{\,3s/4},\qquad
 W_s=W_0^{\,1-3s/4}W_{4/3}^{\,3s/4}.                        \tag{S.20}
\]
The regular scalar has weight one at both endpoints. Equation (S.20)
therefore interpolates the whole augmented operator, including every
finite-input/infinite-output mean column.

## 5. Exact physical load, charge, and averaged-root conversion

The full physical source is still (A.18):
\[
 F_g=\frac{J_+}{\tau}(D\Psi_+)^{-1}F\circ\Psi_+,\qquad
 f_g=\frac{J_+}{\tau}
       [f-\nabla\log\tau\cdot F]\circ\Psi_+.                 \tag{S.21}
\]
The height-gradient scalar correction has not been discarded.
The theorem concerns these canonical source norms and this exact
Piola/height conversion. It does not assert that an untransformed
physical anisotropic Bochner norm is equal to them.

The full grounded constant is canonical \(\tau^{-1}\). The old charge
identity remains
\[
 \left\langle K_c(f,F),
      (\tau_0^{-1},\sqrt{\ell_\theta})\right\rangle
   =-\int[f\tau^{-1}+F\cdot\nabla(\tau^{-1})].               \tag{S.22}
\]
It records the root mean, regular contact, and physical total charge.
Higher source regularity has not solved this independent scalar
compatibility condition.

The weak-source convention is the original complete variational load.
If an independent boundary vector load is prescribed in addition to
the bulk weak field, it must retain its own exact conormal density and
norm. A bare boundary trace is not bounded by the bulk \(L^2\) norm in
(S.1). The Ai residual used in (S.11) is ordinary and has no such
separate boundary load.

For the averaged-root-plus-regular convention used in the central
scattering/return theorems, let \(\ell=2\pi/q_c\). The regular scalar
is rescaled with the same Green normalization. The common conversion
factor is
\[
 \ell^{-1/2}<2.487681088.                                   \tag{S.23}
\]
Hence the averaged complete \(H^1\) source bounds are
\[
 T_1^{\rm av}<1046380607912,\qquad
 W_1^{\rm av}<523137488525.                                 \tag{S.24}
\]
The two physical caps form an orthogonal direct sum, so their common
operator bound does not acquire a factor \(\sqrt2\).
For \(s\ge0\), the normalized angle \(x=q_c\phi\) has
\(\langle n\rangle^s\le\langle q_cn\rangle^s\); similarly for
\(H_N^s\) with \(N\ge1\). Consequently (S.23) also pays the output
comparison to those normalized source windows. The source itself
continues to carry the physical \(\phi\) Sobolev index stated in
(S.1).

## 6. Actual execution, input identity, and scope

The new 320-bit directed consumer reads the already complete cap
certificate, checks its producer, dependencies and all input hashes,
and requires its full augmented means, uncompressed true tail,
all Fourier crossings, and true height/Piola flags. It reuses the
existing full native geometry; it computes no replacement finite
geometry. It evaluates every displayed constant with Arb endpoints.

From this topic directory, reproduce with a fresh output:
~~~sh
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python3 scripts/fourfold_actual_cap_stronger_source_window.py \
  --out notes/2026-11-13-actual-cap-stronger-source-window.json
~~~

The input is
notes/2026-11-13-exact-positive-cap-Airy-contact-v2.json,
SHA-256
f61369e1e740269a11c271efb5cfd9a27df5b1aa91a275ae40e01edee4402649.
The report stores the exact producer/input/dependency identities, both
physical and averaged constants at \(s=0,1/2,1,4/3\), and the full
ordinary/weak source units.

The result grants exactly (S.1) for the old full realization and this
collar support. Orders above \(4/3\), a fixed positive angular weight,
a different deep-tail realization, the finite returned head, and the
full nonlinear surface remain separate obligations.

