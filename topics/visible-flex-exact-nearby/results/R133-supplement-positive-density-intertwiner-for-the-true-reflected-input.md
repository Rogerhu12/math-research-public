# R133 supplement: a positive density intertwiner for the true reflected input

2026-11-16, phase_inverse.

**Proved analytic statement on the original selected real member.** There is an explicit invertible change of the nonmean input coordinates that transports the true conjugated Fourier sign to the ordinary Fourier sign. Its existence follows from positivity of the original primitive pairing, without a smallness condition. The already completed full sign-difference estimate then gives the same inverse in the two required Sobolev windows.

This change transports the true reflected input to a concrete constant-phase reflection model. It also transports the original high projection and its entire finite complement. It does not replace that projection by an ordinary Fourier cutoff, remove a physical mean equation, or prove a physical waist inverse. A separate model calculation at the end identifies the exact scalar Fourier blocks and explains why a free model parameter cannot be substituted by an incomplete physical coefficient.

No scientific arithmetic is executed here. The completed full sign bound is read as an existing input. Every newly displayed norm is a symbolic consequence, not a newly evaluated ball.

## WIT1. The selected maps and the complete saved input

Use the single selected pair $(\delta_*,\mathcal H)$ and the exact true waist map $X_-$ of NIF/RRF. The common density chart is
$$
 \mathcal S=U_\psi
       =U_{\mathcal H^{-1}}U_{X_-},
 \qquad \psi=X_-\circ\mathcal H^{-1},
 \qquad U_\psi f=\psi'(f\circ\psi).
 \tag{WIT.1}
$$
It is a real orientation-preserving degree-one density pullback on the circle of period $\ell=\pi/2$. The integral is normalized and the physical frequencies are $4j$. Both $\mathcal S$ and its actual inverse preserve the full integral.

Let $P=1-\Pi$ and retain the original full sign convention
$$
 Z_{\rm full}=\Pi+i\Pi_+-i\Pi_-,
 \qquad
 \mathcal J_{\rm full}=\mathcal S Z_{\rm full}\mathcal S^{-1},
 \qquad
 \Delta_{\rm full}=\mathcal J_{\rm full}-Z_{\rm full}.
 \tag{WIT.2}
$$
The positive-density mean is not replaced by a half-density convention.

The required complete estimate has already been proved in ZD and evaluated by the unique successful DZ2 run 43773671216, attempt 1:
$$
 \|\Delta_{\rm full}:H^{-4/3}\longrightarrow L^2\|
       \le C_\Delta .
 \tag{WIT.3}
$$
The exact saved source is

notes/fourth_angle_global_sign_budgets_ci/run-43773671216-1/actual-scientific-conclusion.json,

with the topic prefix understood. Its field
complete_new_strong_sign_conclusion.complete_D_Hminus4_3_to_L2_upper.ball
is, verbatim,

~~~text
[801610437995630079910860265481553017.863528954799384559423257778045727076 +/- 1.95e-37]
~~~

$C_\Delta$ means a valid outward upper endpoint of that complete record. No endpoint is recomputed in this proof. In particular it is not the saved $T_o\Delta$ subtotal, an outgoing paid subtotal, or just the nonmean Hilbert--Schmidt contribution. The record includes the independent input-mean rank and both opposite-sign blocks. Restriction to nonmean inputs below uses this same complete upper bound; no rank upper is subtracted.

The immutable references are:

| Source and role | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| NIF: exact selected $\mathcal S$, its two windows, and the corrected natural input | d606faa1ffd30c34d3487985a57dbc62a18890bc | 32942 | 8f3784473b98f9b49449b7012e4c5c919670418246fa03a7f28441aaca28b640 |
| RRF: true reflected rays and the two constant-phase selected reflections | cdb4b957f6976c7b72e974fcccc8f2a15afbee74 | 15266 | 803302f2924da51022e2aa16a36c928ee0789fde93277f5ea9fd9c2ae2a3630f |
| ZD.1--17: complete sign-difference identity, mean rank and strong norm | 82fabb439b60f6587ec5704a91d4502071c5d2c6 | 18961 | 715f28768139356001ef66840939e4defa547f953a59caea613f3fc6d6841a76 |
| DZ2 actual complete science, run43773671216/1 | 67b41ac717207f8696b637c667fb210088fca638 | 26909 | 05036749a28c55499e2ed6fe47019cd31f4438652e3e6ab1319e6f9f2f2c4dba |
| WPR: actual physical target, full mean row and same-space obstruction | 226272031762c5fcace679dd7f940a35040401dc | 22571 | 707b8269e454cab738fe70d84097087a0cf5c74026916a2f8bdc151435eca9cb |
| W.3: exact selected irrational rotation | a79a7ad7c147076b044389e98a15ab2f341d0d0c | 6138 | 1e8d001a5878da2894b4c9ab88baf00555ca8364b23f49df8c827c23a7da88c3 |

The actual DZ2 receipt identifies the same selected common chart, true fourfold density measure, original input cutoff 97 and independent physical mean coordinates. Its other retained-scope flags are not changed by this application.

## WIT2. The primitive pairing on the complete nonmean space

In WIT2--5 all operators act on the full nonmean carrier $PH^s$. In particular
$$
 Z=Z_{\rm full}|_P,\qquad
 \mathcal J=\mathcal J_{\rm full}|_P,\qquad
 \Delta=\Delta_{\rm full}|_P,\qquad
 Z^2=\mathcal J^2=-\operatorname{Id}.
 \tag{WIT.4}
$$
Density preservation gives $\Pi\mathcal S=\Pi\mathcal S^{-1}=\Pi$, so these restrictions and their inverses are well defined. Neither this carrier restriction nor the following pairing discards a physical mean port.

Let $|D|$ have multiplier $n_j=4|j|$ for $j\ne0$, and put
$$
 I=\partial_\phi^{-1}P,\qquad
 G=IZ=|D|^{-1},\qquad
 \|f\|_{\mathscr H}^2
    =\sum_{j\ne0}n_j^{-1}|\widehat f_j|^2,
 \qquad \mathscr H=\dot H^{-1/2}_0.
 \tag{WIT.5}
$$
The Hermitian inner product is
$(f,g)_{\mathscr H}=\langle f,Gg\rangle$, with the distributional duality extending the normalized $L^2$ pairing. Thus $I=-GZ$ and
$\langle f,Ig\rangle=(f,-Zg)_{\mathscr H}$.
The original qualified bounds for $\mathcal S^{\pm1}$ imply boundedness on this intermediate Hilbert space, by interpolation and equivalence of homogeneous and inhomogeneous weights away from zero. No numerical interpolation factor is used in the coercivity estimate below.

For smooth nonmean $g$, the exact primitive identity is
$$
 I\mathcal Sg=(Ig)\circ\psi-\Pi\bigl((Ig)\circ\psi\bigr).
 \tag{WIT.6}
$$
Its derivative is $\psi'(g\circ\psi)$ and its mean is zero, which proves it directly. For smooth nonmean $f,g$, density change of variables and $\Pi f=0$ therefore give
$$
 \begin{aligned}
 \langle\mathcal Sf,I\mathcal Sg\rangle
 &=\int\psi'\overline{f\circ\psi}\,(Ig)\circ\psi
       -\Pi\bigl((Ig)\circ\psi\bigr)\,
                           \overline{\Pi\mathcal Sf}\\
 &=\langle f,Ig\rangle.
 \end{aligned}
 \tag{WIT.7}
$$
The integrals have the original normalized measure. Smooth approximation extends the equality as a bounded form on $\mathscr H$.

Let $\dagger$ denote the adjoint for $(\cdot,\cdot)_{\mathscr H}$. Then
$$
 \mathcal S^\dagger Z\mathcal S=Z.
 \tag{WIT.8}
$$
Equivalently, $\mathcal S^*I\mathcal S=I$ as a form on the meanzero subspace, with any $L^2$ adjoint understood after the corresponding restriction or compression. The unrestricted $L^2$ adjoint need not preserve meanzero data. No claim that $\mathcal S$ is $L^2$-unitary is used.

## WIT3. The positive intertwiner and its Hilbert-space inverse

Set
$$
 \mathcal A=-Z\mathcal J,\qquad
 \mathcal W=\frac12(\operatorname{Id}-Z\mathcal J)
           =\frac12(\operatorname{Id}+\mathcal A).
 \tag{WIT.9}
$$
This $\mathcal W$ is an input-coordinate operator; it is distinct from the phase trial denoted by $W$ in SW.

For $f,g\in\mathscr H$, (WIT.7) gives
$$
 (f,\mathcal A g)_{\mathscr H}
  =\langle f,I\mathcal Jg\rangle
  =(\mathcal S^{-1}f,\mathcal S^{-1}g)_{\mathscr H}.
 \tag{WIT.10}
$$
Consequently
$$
 \mathcal A=\mathcal S^{-\dagger}\mathcal S^{-1}
 \quad\hbox{on }\mathscr H,\qquad
 (f,\mathcal Wf)_{\mathscr H}
   =\frac12\left(\|f\|_{\mathscr H}^2+
                     \|\mathcal S^{-1}f\|_{\mathscr H}^2\right)
       \ge\frac12\|f\|_{\mathscr H}^2 .
 \tag{WIT.11}
$$
In particular $\mathcal A$ is positive self-adjoint in this Hilbert metric. The displayed $\dagger$ cannot be replaced by the ordinary $L^2$ adjoint.

The bounded positive self-adjoint operator $\mathcal W$ is onto and invertible on $\mathscr H$, with
$$
 \boxed{\quad
 \|\mathcal W_{\mathscr H}^{-1}:
                   \mathscr H\to\mathscr H\|\le2.
 \quad}
 \tag{WIT.12}
$$
For example, the coercive form in (WIT.11) gives a unique solution for every right side by the Hilbert-space representation theorem. This supplies existence and surjectivity, not just injectivity or a formal inverse.

The exact intertwining identity is
$$
 \mathcal W\mathcal J
   =\frac12(\mathcal J+Z)
   =Z\mathcal W .
 \tag{WIT.13}
$$
It follows only from $Z^2=\mathcal J^2=-\operatorname{Id}$, without commuting $Z$ with $\mathcal J$.

## WIT4. The same inverse on $L^2_0$ and $H^{-4/3}_0$

Write
$$
 \mathcal R=\frac12Z\Delta,\qquad
 \mathcal W=\operatorname{Id}-\mathcal R,\qquad
 \|\mathcal R:H^{-4/3}_0\to L^2_0\|
                   \le\frac{C_\Delta}{2}.
 \tag{WIT.14}
$$
The complete output mean of $\Delta_{\rm full}$ is exactly zero, as in ZD. Thus the output spaces in (WIT.14) are genuine nonmean spaces.

The physical frequency factor is essential. Since $n_j=4|j|\ge4$,
$$
 \|g\|_{\mathscr H}\le\frac12\|g\|_2
       \quad(g\in L^2_0),\qquad
 \|g\|_{H^{-4/3}}\le\|g\|_{\mathscr H}
       \quad(g\in\mathscr H).
 \tag{WIT.15}
$$
The second inequality follows termwise from
$(1+n_j^2)^{-4/3}\le n_j^{-1}$ in the squared norms. Also
$\|g\|_{H^{-4/3}}\le\|g\|_2$.

For $f\in L^2_0$, first solve $u=\mathcal W_{\mathscr H}^{-1}f$ in $\mathscr H$. Equations (WIT.12) and (WIT.15) imply
$\|u\|_{\mathscr H}\le\|f\|_2$. The equation gives
$u=f+\mathcal Ru$, and (WIT.14)--(WIT.15) show $\mathcal Ru\in L^2_0$. Therefore $u\in L^2_0$ and
$$
 \|u\|_2
 \le\|f\|_2+\frac{C_\Delta}{2}\|u\|_{H^{-4/3}}
 \le\left(1+\frac{C_\Delta}{2}\right)\|f\|_2 .
 \tag{WIT.16}
$$
This is regularity of the already constructed Hilbert-space solution, rather than an assumed $L^2$ inverse.

For $f\in H^{-4/3}_0$, do not apply
$\mathcal W_{\mathscr H}^{-1}$ directly to $f$. Instead define
$$
 u=f+\mathcal W_{\mathscr H}^{-1}\mathcal Rf .
 \tag{WIT.17}
$$
Here $\mathcal Rf\in L^2_0\subset\mathscr H$, so every factor is defined. The distributional identity
$\mathcal W(\mathcal W_{\mathscr H}^{-1}\mathcal Rf)=\mathcal Rf$
gives $\mathcal Wu=f$. Moreover
$$
 \begin{aligned}
 \|\mathcal W_{\mathscr H}^{-1}\mathcal Rf\|_{H^{-4/3}}
 &\le2\|\mathcal Rf\|_{\mathscr H}\\
 &\le\|\mathcal Rf\|_2
 \le\frac{C_\Delta}{2}\|f\|_{H^{-4/3}}.
 \end{aligned}
 \tag{WIT.18}
$$
If $\mathcal Wv=0$ for $v\in H^{-4/3}_0$, then
$v=\mathcal Rv\in L^2_0\subset\mathscr H$, where (WIT.12) makes $v=0$. Thus (WIT.17) is the two-sided inverse. On the common domain it agrees with the inverse just constructed on $L^2_0$.

Put $K_{\mathcal W}=1+C_\Delta/2$. The complete conclusion is
$$
 \boxed{\quad
 \|\mathcal W\|_{H^s_0\to H^s_0},
 \ \|\mathcal W^{-1}\|_{H^s_0\to H^s_0}
       \le K_{\mathcal W},\qquad s=0,-4/3.
 \quad}
 \tag{WIT.19}
$$
The forward bounds follow directly from (WIT.14) and the stated embeddings. Both inverses are the same distributional operator. No condition $C_\Delta<2$, Neumann test, exponentiation or recomputation of $\Delta$ was required.

The strong differences, if needed in a later explicit calculation, satisfy the symbolic bounds
$$
 \|\mathcal W-\operatorname{Id}\|_{H^{-4/3}_0\to L^2_0}
       \le\frac{C_\Delta}{2},\qquad
 \|\mathcal W^{-1}-\operatorname{Id}\|_{H^{-4/3}_0\to L^2_0}
       \le K_{\mathcal W}\frac{C_\Delta}{2}.
 \tag{WIT.20}
$$
For the second, use (WIT.17) and the $L^2$ inverse on its $L^2$ argument. These are new unevaluated expressions. The old full DZ2 upper record remains unchanged.

## WIT5. Exact transport of the reflection and the original cutoff

RRF proves, for the same selected map and its unchanged lift,
$$
 \mathcal S R_*\mathcal S^{-1}=R_b,\qquad
 b=a+\Omega,\qquad R_bf(x)=f(b-x).
 \tag{WIT.21}
$$
On nonmeans, $R_b$ anticommutes with both $Z$ and $\mathcal J$:
the first is the ordinary Fourier reflection identity, and the second is the transport of $R_*Z=-ZR_*$. Hence
$$
 [\mathcal W,R_b]=0,\qquad
 \mathcal W(-\mathcal J R_b)=(-Z R_b)\mathcal W .
 \tag{WIT.22}
$$
The same identities hold for the common inverse. The operator
$J_{\rm mod}=-ZR_b$ is a self-adjoint unitary involution in each ordinary $H^s_0$.

On the full nonmean carrier, the corrected input reflection is
$J_X=-\mathcal J R_b$. Therefore $\mathcal W$ maps
$\operatorname{Fix}(J_X)$ bijectively onto
$\operatorname{Fix}(J_{\rm mod})$. This is an actual known target, not a target defined only as an unknown incoming image.

Keep the original cutoff in the same ordered map:
$$
 P_{97}^{\mathcal S}=\mathcal S P_{97}\mathcal S^{-1},
 \qquad
 \widehat P_{97}=\mathcal W P_{97}^{\mathcal S}\mathcal W^{-1}.
 \tag{WIT.23}
$$
Then the exact image of the NIF domain is
$$
 \boxed{\quad
 \mathcal W X_s^{\rm fr}
    =\operatorname{ran}(\widehat P_{97})
          \cap\operatorname{Fix}(-ZR_b),
 \qquad s=0,-4/3 .
 \quad}
 \tag{WIT.24}
$$
The projector and the involution commute because they are transports of the original commuting root objects.

A useful equivalent form makes the sign preservation explicit. Define
$$
 \mathcal C=\mathcal W\mathcal S
            =\frac12(\mathcal S-Z\mathcal S Z).
 \tag{WIT.25}
$$
It is invertible in the two windows,
$Z\mathcal C=\mathcal C Z$ and
$\mathcal C R_*=R_b\mathcal C$. Consequently
$$
 \widehat P_{97}=\mathcal C P_{97}\mathcal C^{-1}
 \quad\hbox{commutes with }Z,\ R_b,\ \hbox{and }-ZR_b .
 \tag{WIT.26}
$$
The original fixed $D_+$ also commutes with $\mathcal C$ in the corresponding root and selected coordinates. None of this says that $\mathcal C$ preserves individual Fourier frequencies.

On the full nonmean complex carrier, $1-\widehat P_{97}$ has the same finite rank 192 as the original modes $1\le|j|\le96$. Its restriction to the model reflected class has rank 96. The underlying real class has the corresponding real dimensions, since all the displayed operators preserve the original Fourier conjugacy. These are ranks of coordinate complements, not a proof that the original finite boundary equations are invertible.

In particular $\widehat P_{97}$ is not replaced by the ordinary $P_{97}$. Their difference is finite rank, but its exact columns, rows and weighted realization must be retained in a subsequent square or bordered problem. There is no claim that either transported projector is orthogonal.

## WIT6. Means and changes of a complete physical row

The positivity proof applies to the full nonmean space. An explicit identity extension on an auxiliary scalar mean is
$$
 \widehat{\mathcal W}=\Pi+\mathcal WP,\qquad
 \widehat{\mathcal W}^{-1}=\Pi+\mathcal W^{-1}P.
 \tag{WIT.27}
$$
It has the same two-window bounds because $K_{\mathcal W}\ge1$.
It is not the unqualified full-circle expression
$(1-Z_{\rm full}\mathcal J_{\rm full})/2$.

Even this explicit extension does not remove the original full-density mean column from the sign conjugation. Since
$\Pi\Delta_{\rm full}=0$, exact block multiplication gives
$$
 \widehat{\mathcal W}\mathcal J_{\rm full}
                 \widehat{\mathcal W}^{-1}
 =Z_{\rm full}
       +(\mathcal W\Delta_{\rm full}1)\otimes\Pi .
 \tag{WIT.28}
$$
The rank on the right is generally nonzero. It remains in any use involving the auxiliary scalar mean. The original two stored physical mean slots, their reflected rank-one relation when applicable, and the independent even-mean and amplitude equations are not identified with or removed by this auxiliary extension.

Likewise RRF's physical paired reflection remains
$K_{\mathcal H}=R_a-2h_{\mathcal H}\otimes\Pi$ with
$h_{\mathcal H}=U_{\mathcal H^{-1}}1$. That full mean rank is not altered by treating (WIT.22) as a nonmean input identity.

For any already qualified actual row
$\mathcal L+\mathcal E:X_{-4/3}^{\rm fr}\to\mathcal Y$, change the input by the exact right inverse:
$$
 \widehat{\mathcal L}=\mathcal L\mathcal W^{-1},\qquad
 \widehat{\mathcal E}=\mathcal E\mathcal W^{-1}.
 \tag{WIT.29}
$$
If the original error is complete and strong, its transformed bound is at most the original bound times $K_{\mathcal W}$ on the input window. The target and every independent port retain their original types. A different proposed leading row would require its complete additional difference; the factor $\mathcal W^{-1}$ is not dropped from the leading term while being retained only on the error.

This statement applies only after the original row is specified. In particular it does not turn a full-circle inverse of $T_i$ into a physical same-space inverse, or make a rough bulk Poisson map bounded by a trace-coordinate argument.

## WIT7. A separate exact Fourier model on specified source and target

The following model is useful only with its stated domain. Let $\nu$ be a free real scalar, let $b=a+\Omega$ as above, and set
$$
 \begin{aligned}
 \mathcal X_{b,97}^{s,{\rm mod}}
    &=P_{97}\operatorname{Fix}(-ZR_b),\\
 \mathcal Y_{a,97}^s&=P_{97}\operatorname{Fix}(R_a),\\
 T_\nu&=\operatorname{Id}+\nu I,\qquad
 \Pi_a^+=\frac12(\operatorname{Id}+R_a),\\
 \mathcal M_\nu&=\left.\Pi_a^+T_\nu
                   \right|_{\mathcal X_{b,97}^{s,{\rm mod}}}.
 \end{aligned}
 \tag{WIT.30}
$$
The original cutoff in (WIT.24) is $\widehat P_{97}$, not the ordinary cutoff used in (WIT.30). Their finite difference is still an obligation. Also $T_\nu$ in this model is not declared to be the complete physical waist leading row.

For $n\ge97$ and $k=4n$, normalized complex bases of the two reflection lines are
$$
 e_n^b=\frac{e^{ikx}+i e^{ikb}e^{-ikx}}{\sqrt2},
 \qquad
 f_n^a=\frac{e^{ikx}+e^{ika}e^{-ikx}}{\sqrt2}.
 \tag{WIT.31}
$$
They have the same Bessel weight $\Lambda_n^s$. Direct use of
$I e^{\pm ikx}=(\pm ik)^{-1}e^{\pm ikx}$ gives
$$
 \mathcal M_\nu e_n^b=q_n(\nu)f_n^a,\qquad
 q_n(\nu)=\frac12\left[
       1-\frac{i\nu}{k}
       +i e^{ik\Omega}\left(1+\frac{i\nu}{k}\right)\right].
 \tag{WIT.32}
$$
The two input signs have been paired once. This is one complex reflection line per $n$, with its original real form; no second norm sum is introduced.

For the exact constant-coefficient Cayley multiplier
$$
 C_\mu(k)=\frac{1+\mu/(2ik)}{1-\mu/(2ik)},
$$
the factorization and its real amplitude are
$$
 \begin{aligned}
 q_n(\nu)
   &=\frac{1-i\nu/k}{2}
                \left[1+i e^{ik\Omega}C_{-2\nu}(k)\right],\\
 q_n(\nu)
   &=e^{i\theta_n}
          \left(\cos\theta_n-\frac{\nu}{k}\sin\theta_n\right),
 \qquad
 \theta_n=\frac{k\Omega}{2}+\frac\pi4.
 \end{aligned}
 \tag{WIT.33}
$$
These are exact scalar identities, not evaluations of the trigonometric functions or a new Cayley certificate.

A valid spectral assertion must concern these complete scalar factors. For example, if an independently proved full bound is
$|q_n(\nu)|\ge\gamma/n>0$ for every $n\ge97$, division defines an inverse with one derivative of loss:
$$
 \|\mathcal M_\nu^{-1}:
       \mathcal Y_{a,97}^{s+1}
        \to\mathcal X_{b,97}^{s,{\rm mod}}\|
           \le\frac1{4\gamma}.
 \tag{WIT.34}
$$
Indeed $n/\Lambda_n\le1/4$. This is a solution operator on the more regular right-side space, not a statement that the forward order-zero map gains one derivative or is a same-order bounded isomorphism.

For an unrestricted real $\nu$, irrationality of $\Omega$ alone is insufficient. At any chosen $n\ge97$, $\sin\theta_n\ne0$ by the exact quadratic irrationality in W.3, and the real choice
$$
 \nu=k\cot\theta_n
 \tag{WIT.35}
$$
makes $q_n(\nu)=0$. Thus the actual physical coefficient needs its own complete spectral qualification. A certified same-sign scalar principal inverse does not exclude this reflected-boundary resonance.

In an application to the physical waist row, identifying $\nu$ with its complete first-coefficient mean requires the exact ordered waist identities. A possible first-order contribution from the actual off-diagonal waist normalizer must be included, or shown to vanish from its original metric definitions. Such a vanishing statement uses actual radial regularity, exact parity and the real compact perturbation support; it is not inferred from a small upper bound. This model calculation assigns no new scalar value and applies no old Cayley finite verdict. Admission of an already completed same-parameter Cayley gap is a separate exact-source step.

## WIT8. What is now available

Equations (WIT.9)--(WIT.24) give an explicit same-distributional-inverse transport from the true nonmean input reflection to the ordinary-sign reflection model, together with complete symbolic bounds in $L^2_0$ and $H^{-4/3}_0$. Its existence comes from the exact density pairing and positivity. The full sign-difference bound is used only to transfer regularity and norms to the two target windows.

The actual finite complement, full-density mean ranks and physical matching rows remain explicit. The principal model (WIT.30) is a separate typed square on an ordinary Fourier cutoff; applying it to the physical problem still requires the transported finite data, the complete physical leading coefficient and all genuine lower-order errors. The original regular Poisson graph, actual waist range, metric parameter, even mean and independent source ports are unchanged.

No saved graph, exponential, KAM map, ray, norm, sign difference, finite Cayley test, or original successful target is recomputed. The new symbolic products can be evaluated only by a separately reviewed new consumer if numerical values are later required.
