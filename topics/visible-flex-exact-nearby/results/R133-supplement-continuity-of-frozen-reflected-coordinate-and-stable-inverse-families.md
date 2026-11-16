# R133 supplement NIFC: continuity on the corrected fixed physical input spaces

2026-11-16. Analytic corollary; no new numerical evaluation.

This note closes the fixed-chart continuity qualification at the end of RNI7 for the explicit frozen realization constructed in NIF. It retains the distinction between operator-norm continuity of the coordinate and normalized-root factors and strong continuity of the genuine global Riccati factor. It proves no continuity or invertibility statement for a complete physical incoming map whose actual domain and range have not yet been matched.

## NIFC1. Fixed spaces and exact hypotheses

Keep the same original real reference family
$$
 I_\delta=[-10^{-8},10^{-8}],\qquad Q_\delta=Q_0+\delta Z,
 \qquad \nu_\delta=\nu_0+\delta,
 \qquad \eta_{\rm intrinsic}=\eta_0 .
 \tag{NIFC.1}
$$
The intrinsic parameter is fixed; the positive moving speed at the root is a different coefficient. The physical period is $\pi/2$, angular measure is normalized, the physical frequency is $n=4|j|$, and the original natural high cutoff is $|j|\ge97$. Use the original reflected natural spaces $\mathcal H_{\rm nat}^q$, with their inherited Bessel norms. They are not enlarged to the whole signed carrier.

Choose the single original selected member $\delta_*$ and its map $\mathcal S_*$ exactly as in NIF1. Set
$$
 D_+=e^{-i\pi/4}\Pi_++e^{i\pi/4}\Pi_-,
 \qquad
 \mathcal X_s^{\rm fr}=\mathcal S_*D_+\mathcal H_{\rm nat}^s,
 \qquad
 \mathcal Y_s=\mathcal H_{\rm nat}^{s-1/6},
 \qquad s=0,-4/3 .
 \tag{NIFC.2}
$$
The norm on $\mathcal X_s^{\rm fr}$ is the inherited physical $H^s$ norm, as in NIF.7. These are fixed closed spaces. Write
$L_s=\mathcal S_*D_+:\mathcal H_{\rm nat}^s\to\mathcal X_s^{\rm fr}$.
It and its inverse are fixed bounded maps. We do not replace this domain by the old SE8 shorthand $\mathcal S_*\mathcal H_{\rm nat}^s$.

Use the exact NIF maps
$$
 N_\delta:=N_{i,\delta}^{\rm fr}
   =\Lambda_{+,\delta}^{-1}T_{F,\delta}^{-1}\mathcal S_*^{-1},
 \qquad
 N_\delta^{-1}=\mathcal S_*T_{F,\delta}\Lambda_{+,\delta},
 \qquad \Lambda_{+,\delta}=a_\delta D_+,\quad a_\delta>0 .
 \tag{NIFC.3}
$$
All products here and below retain their original order and natural domains. In particular, no sign phase is moved through $\mathcal S_*$. The exact relation NIF.18a is
$$
 N_\delta L_s=a_\delta^{-1}T_{F,\delta}^{-1},
 \qquad N_\delta^{-1}=a_\delta L_sT_{F,\delta}
       \quad\hbox{on }\mathcal H_{\rm nat}^s .
 \tag{NIFC.4}
$$
The second identity uses only the already proved commutation of $T_F$ with $D_+$.

The strict natural-root certificate is the actual successful R97 recovery, not the original conditional RNI recipe. The actual RNE success supplies the same natural inverse and uniform bounds in the two windows $t=-7/6,-5/2$. NIF gives uniform coordinate bounds in $s=0,-4/3$ and the compatible stable-map inverse. Its separate actual new scalar computation is not needed to repeat or reevaluate any bound for this analytic corollary.

For the genuine global factor $\mathcal M_\delta$, retain the premise expressly stated in RNI7: for each fixed physical frequency, the actual Riccati problem has continuously varying coefficients and endpoint datum and the corresponding solution depends continuously on $\delta$. The original bound $0<\widetilde p_{j,\delta}<66$ is also retained. A family specified solely by that bound, with no fixed-frequency continuity, does not satisfy the continuity hypotheses of this note.

## NIFC2. Operator-norm continuity of the root coordinate maps

The actual normalizer is
$$
 T_{F,\delta}=1+P_{1024}M_{F_\delta}IP_{1024},
 \qquad \deg F_\delta\le192,\qquad
 F_\delta=\frac{\beta_*u_*v_*}{\eta_*}.
 \tag{NIFC.5}
$$
Its coefficients are continuous in $\delta$ in the common root realization. Here the original B section 1 is stronger than a general moving-root argument: the compact intrinsic bump vanishes on the genuine root neighbourhood, so the intrinsic root and $K,b,\gamma$ there are independent of $\nu_\delta$. Thus $r_*$ is the same fixed simple root throughout the present family. The finite coefficients of $Q_0+\delta Z$, evaluated at that root with the original positive denominator gaps, give the asserted continuity. RNI7 retains these same coefficient domains. The full means and the scalar-mean convention of the primitive retain their original meanings.

For any fixed Sobolev exponent $s$, multiplication by a fixed finite Fourier polynomial is bounded on $H^s$. More explicitly, if
$F_\delta=\sum_{|m|\le192}f_m(\delta)e^{i4m\theta}$, then
$$
 \|M_{F_\delta-F_{\delta'}}\|_{H^s\to H^s}
 \le \sum_{|m|\le192}
       |f_m(\delta)-f_m(\delta')|\,b_{s,m},
 \quad
 b_{s,m}:=
 \sup_{j\in\mathbb Z}
 \frac{(1+16(j+m)^2)^{s/2}}{(1+16j^2)^{s/2}}<\infty .
 \tag{NIFC.6}
$$
This finite sum tends to zero. No numerical value of $b_{s,m}$ is calculated. The actual primitive $I$, zero on its scalar mean, and the fixed projections in (NIFC.5) are bounded in each of the two qualified windows. Hence
$$
 \|T_{F,\delta}-T_{F,\delta'}\|_{H^s\to H^s}\longrightarrow0,
 \qquad s=0,-4/3 .
 \tag{NIFC.7}
$$
This is a difference estimate for a fixed finite-band family, with no assertion about operator-norm continuity of varying pullback operators.

NIF.10a proves that these maps and their same inverse preserve the actual natural reflection. NIF.10 separately proves their high-carrier and sign commutations. Their uniform inverse bounds from the original TFA receipt therefore apply to the same fixed natural domains. The genuine resolvent identity gives
$$
 T_{F,\delta}^{-1}-T_{F,\delta'}^{-1}
 =T_{F,\delta}^{-1}(T_{F,\delta'}-T_{F,\delta})
       T_{F,\delta'}^{-1}.
 \tag{NIFC.8}
$$
Its norm is bounded by the norm in (NIFC.7) times the square of the original uniform inverse bound for that window. Thus $T_{F,\delta}^{-1}$ is also operator-norm continuous in the two stated windows.

The common modulus is the exact correlated KL expression
$$
 a_\delta=
 \frac{n_g(0)}{\sqrt{2\pi}}
 \left(\frac{k_*}{\eta_*}\right)^{1/6}
 k_{\rm root}(0),
 \qquad
 k_{\rm root}(0)=
 \exp\!\left(\int_{r_*}^0\ell_{0,\delta}(r)\,dr\right),
 \quad
 \ell_{0,\delta}=-2\beta\langle u^2+Kv^2\rangle .
 \tag{NIFC.9}
$$
All complete means are retained. The original continuous parameter dependence and positive denominators give continuity of the positive factors in this formula. For the integral, use the original common finite radial partition, continuity in $\delta$ on its pieces and a common integrable bound on the compact parameter-radius domain. Dominated convergence gives continuity of the ordinary $dr$ integral between the fixed endpoints $r_*$ and $0$. Possible seam values occupy a set of measure zero, and no radial derivative across a seam is used. No old integral or exponential is evaluated here. The positivity and the original common inverse bound give a common positive lower bound for $a_\delta$; alternatively, positivity and continuity on the compact parameter interval suffice. Thus both $a_\delta$ and $a_\delta^{-1}$ are continuous.

Combining these facts with the fixed maps $L_s^{\pm1}$ in (NIFC.4) proves
$$
 \delta\longmapsto N_\delta
 \in\mathcal B(\mathcal X_s^{\rm fr},\mathcal H_{\rm nat}^s),
 \qquad
 \delta\longmapsto N_\delta^{-1}
 \in\mathcal B(\mathcal H_{\rm nat}^s,\mathcal X_s^{\rm fr})
 \quad\hbox{are operator-norm continuous}.
 \tag{NIFC.10}
$$
The limits are one-sided at the endpoints of $I_\delta$. All inverses remain compatible on the common distributional core.

## NIFC3. Normalized-root continuity and the true global factor

RNI7 already establishes, on each of the two fixed natural windows,
$$
 \delta\longmapsto\widehat S_\delta,\quad
 \delta\longmapsto\widehat S_\delta^{-1}
 \quad\hbox{in the operator norm of }\mathcal B(\mathcal H_{\rm nat}^t),
 \qquad t=-7/6,-5/2 .
 \tag{NIFC.11}
$$
Its proof uses the complete ordered root expression: the actual finite coefficients, the genuine Ai input diagonals, the actual old-circle inverse and all retained mean-rank terms. The high-frequency tail estimate for the normalized Ai diagonal is combined with fixed-frequency continuity. The resolvent is used with its original one-gain types. This note inherits that full argument; it does not infer (NIFC.11) from the numerical strict margin alone.

The true natural factorization remains
$$
 S_{{\rm nat},\delta}=\mathcal M_\delta\widehat S_\delta,
 \qquad
 \mathcal M_\delta e_j=(1+\widetilde p_{j,\delta})^{-1/2}e_j,
 \quad
 \|\mathcal M_\delta\|\le1,\qquad
 \|\mathcal M_\delta^{-1}\|\le\sqrt{67}.
 \tag{NIFC.12}
$$
For each fixed Fourier coefficient, the retained Riccati continuity premise gives continuity of both symbols in (NIFC.12). For a fixed $f\in\mathcal H_{\rm nat}^t$, the squared weighted Fourier coefficients of the difference applied to $f$ are bounded by a constant times the summable squared weighted coefficients of $f$. Dominated convergence therefore proves
$$
 \mathcal M_\delta f\longrightarrow\mathcal M_{\delta'}f,
 \qquad
 \mathcal M_\delta^{-1}f\longrightarrow
       \mathcal M_{\delta'}^{-1}f
 \quad(\delta\longrightarrow\delta').
 \tag{NIFC.13}
$$
This argument uses the actual paired symbols and reflection realization already present in RNI. It does not extend the natural inverse to another unproved reflection sector.

Uniformly bounded strongly continuous operator families have strongly continuous products. For $A_\delta:X\to Y$ and $B_\delta:Y\to Z$ of the declared fixed types,
$$
 \|(B_\delta A_\delta-B_{\delta'}A_{\delta'})x\|
 \le \|B_\delta\|\,\|(A_\delta-A_{\delta'})x\|
      +\|(B_\delta-B_{\delta'})A_{\delta'}x\|.
 \tag{NIFC.14}
$$
In (NIFC.14), the first factor needs a locally uniform bound and each applied difference tends to zero. Applying this elementary identity in the original order to (NIFC.11)--13 proves strong continuity of both
$$
 S_{{\rm nat},\delta}
       =\mathcal M_\delta\widehat S_\delta,\qquad
 S_{{\rm nat},\delta}^{-1}
       =\widehat S_\delta^{-1}\mathcal M_\delta^{-1}
 \quad\hbox{on }\mathcal H_{\rm nat}^t.
 \tag{NIFC.15}
$$
No uniform-in-frequency limit for $\widetilde p_{j,\delta}$ has been used. In particular, no operator-norm continuity of $\mathcal M_\delta$, $S_{{\rm nat},\delta}$ or their inverses is concluded.

## NIFC4. Strong and joint continuity of the fixed-space stable inverse

For each $s=0,-4/3$, put $t=s-7/6$. Use the exact maps and types
$$
 C_\delta=C_{s,\delta}^{\rm fr}
  =N_{\rm out}^{-1}S_{{\rm nat},\delta}N_{\rm in}^{7/6}N_\delta
  :\mathcal X_s^{\rm fr}\longrightarrow\mathcal Y_s ,
 \tag{NIFC.16}
$$
$$
 C_\delta^{-1}
  =N_\delta^{-1}N_{\rm in}^{-7/6}
        S_{{\rm nat},\delta}^{-1}N_{\rm out}
  :\mathcal Y_s\longrightarrow\mathcal X_s^{\rm fr}.
 \tag{NIFC.17}
$$
The fixed frequency weights have the bounded cross-window types in NIF.24--25. They act on the nonmean high spaces only. No frequency inverse acts on either independent physical mean.

The coordinate factors are operator-norm continuous by (NIFC.10), the natural factors are strongly continuous by (NIFC.15), and all factors are uniformly bounded in their declared types by the original NIF/RNI/RNE bounds. The product argument (NIFC.14) proves strong continuity of $C_\delta$ and $C_\delta^{-1}$ between these fixed spaces.

These statements also imply joint continuity of the evaluation maps
$$
 (\delta,x)\longmapsto C_\delta x,\qquad
 (\delta,y)\longmapsto C_\delta^{-1}y.
 \tag{NIFC.18}
$$
For example, if $\delta_n\to\delta$ and $y_n\to y$ in $\mathcal Y_s$, then
$$
 \|C_{\delta_n}^{-1}y_n-C_\delta^{-1}y\|
 \le K_s\|y_n-y\|
      +\|(C_{\delta_n}^{-1}-C_\delta^{-1})y\|\longrightarrow0,
 \quad
 K_s=\sup_{\lambda\in I_\delta}\|C_\lambda^{-1}\|<\infty .
 \tag{NIFC.19}
$$
The forward case uses its own complete uniform bound, which NIF.27 supplies symbolically. This argument needs no new printed scalar.

For every compact set $K\subset\mathcal Y_s$, strong continuity and the common bound also give
$$
 \sup_{y\in K}
 \|(C_\delta^{-1}-C_{\delta'}^{-1})y\|\longrightarrow0
 \quad(\delta\longrightarrow\delta').
 \tag{NIFC.20}
$$
To see this, take a finite epsilon-net in $K$, apply pointwise strong continuity to its finitely many centers, and use the uniform bound for the error between a point and its center. The analogous statement holds for compact input subsets of $\mathcal X_s^{\rm fr}$ and the forward maps. Compactness of the parameter interval further gives uniform continuity of each evaluation map on the corresponding compact parameter-times-data set. None of these compact-data statements is operator-norm continuity on the whole unit ball.

The two windows still describe the same compatible inverse on their common distributional core. Extending the coordinate change by the identity on genuinely independent ports leaves those ports and their topology unchanged. This extension alone supplies no inverse for the full coupled physical operator.

## NIFC5. A finite-dimensional consequence with its exact limitation

Let $L:\mathbb C^d\to\mathcal Y_s$ be any fixed bounded finite collection of actual data columns, and let $V:\mathcal X_s^{\rm fr}\to\mathbb C^r$ be any fixed bounded row map. Then
$$
 \delta\longmapsto V C_\delta^{-1}L
       \in\mathcal B(\mathbb C^d,\mathbb C^r)
 \quad\hbox{is operator-norm continuous}.
 \tag{NIFC.21}
$$
This follows either from the compact image of the finite-dimensional unit ball or by checking the finitely many columns. The same statement holds for $V C_\delta L$ when its domain and range types are correspondingly reversed. No numerical matrix is formed here.

If such columns or rows vary, their own suitably typed norm continuity must be established; it is not inferred from (NIFC.21). In particular, (NIFC.21) does not identify the still uncomputed actual physical incoming matrix, show a finite Schur determinant is nonzero, supply a monotonicity or derivative statement, or give a lower bound for any true parameter-column pairing.

## NIFC6. What has and has not been closed

The last qualification of RNI7 is now resolved for the explicit NIF frozen spaces: the chart identification $L_s$ is fixed and the actual $N_\delta^{\pm1}$ are operator-norm continuous. Under RNI7's stated fixed-frequency Riccati continuity premise, the corresponding genuine stable map and its inverse are strongly and jointly continuous, uniformly on compact data sets.

The domain correction in NIF9 remains essential. None of these continuity statements turns a full-circle principal or Cayley inverse into an inverse on an unidentified physical range. The actual two-port waist relation, independent mean equations, low/radial head spaces, any independent second reference datum, complete strong remainder, full incoming inverse, remaining finite Schur rows and the true $\nu$ column retain their own obligations.

This note claims neither a varying selected KAM conjugacy nor operator-norm continuity of arbitrary varying density pullbacks. It proves no parameter derivative, $C^1$ family, nonlinear-background estimate, tame inverse for the full operator, exact PDE branch, geometric matching, or final flexible surface. A bounded discontinuous Riccati symbol family is expressly outside its continuity premise. No old successful scientific computation or new scalar computation is performed.

## NIFC7. Primary identity and scope record

The proofs used here are the complete small primary texts already read, with immutable identities:

| Primary | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| NIF fixed reflected coordinate theorem and SE8 correction boundary | d606faa1ffd30c34d3487985a57dbc62a18890bc | 32942 | 8f3784473b98f9b49449b7012e4c5c919670418246fa03a7f28441aaca28b640 |
| B actual same real reference family and fixed intrinsic root | e561b822673bbce15c1391ee851fb93d4143d43e | 15703 | f5f980a1fb085103f548d7bbdf6fe0124dda176276fa1b8bac6783b6b22a150c |
| RNI natural-window inverse and parameter continuity | ce0a46c75360850479333534cf096fd61f412168 | 19405 | d771cf43faa0d5351851168f9f1567e21f8b7e0be27480b6bd67880a4eb69a81 |
| Actual R97 strict root inverse and prefix recovery | dee5dc9a0092d8c90ade09b0a6f0994adc6a2163 | 67984 | b2d4bb5605021b9b20589a8d16350a7e7747d7e51de5f774c85900f70b3844ca |
| Actual RNE explicit natural negative-window constants | 9d39a3b43b7e8c17bf5284a7f52b8fb1327d1461 | 62469 | 257644a49ff387fa7907eefeea12579725d2f3fa14e1cef28d3e63bbb4f7ba4e |

These are [NIF](R133-supplement-uniform-frozen-selected-input-coordinates-for-the-real-reference-family.md), [RNI](R133-supplement-conditional-cutoff97-faithfulness-and-uniform-natural-window-inverses.md), [R97A](R133-supplement-actual-root-cutoff97-stable-injectivity-and-exact-prefix-recovery.md), and [RNEA](R133-supplement-actual-explicit-uniform-natural-negative-window-inverse-constants.md). The B/TF/KL/WX objects used to define the finite coefficients, means, root and frozen chart retain the full qualifications and immutable primary table in NIF8. This corollary does not replace any original numerical receipt or widen its scope.
