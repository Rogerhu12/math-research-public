# R823 — Every nonzero original primitive Hom direction is unramified at the original CM point

Date: 2026-11-15. Status: **proved, conditional on the displayed original $M_{2,1}\ne0$ for an individual prime and unconditional for every sufficiently large allowed prime by R729**.

The new assertion concerns every nonzero actual $L$-Hom direction, rather than only the separate coefficient embeddings of the modular Hodge space. The statement that R682's common order is one was already proved in R729; it is recalled below solely to specify the original logarithmic interface.

## 1. Objects, premise and the original coarse coordinate

Use the original positive factor, fields and curve of R725/R728/R819:
$$
p\ge41,\quad p\equiv2,5\pmod9,\quad
n=p+1,\quad K=\mathbf Q(\zeta_3),\quad E=\mathbf Q(\zeta_n),
$$
$$
q:J_X\longrightarrow A=A_{\theta,1},\qquad
C/L:y^2=x^3+b,\qquad
V=\operatorname{Hom}_L(A_L,C)\otimes_{\mathbf Z}\mathbf Q.
\tag{823.1}
$$
The original curve is $j=6912a^3(1-a^3)$. Keep the actual rational points
$c_0:a=0$ and $c_1:a=1$ from R616, with their original CM necklace. In particular
$$
c_1\in X(\mathbf Q),\qquad s=a-1
\tag{823.2}
$$
is the original rational coarse local parameter at $c_1$.

For this individual prime suppose
$$
M_{2,1}\ne0
\tag{823.3}
$$
in the original flat-jet normalization of R588/R717/R729. We do not change the tame conductor-six character, Cartan average, positive twist or $p$-adic embedding.

R730(730.2) gives the complete original scalar increment
$$
\mathcal I_h(s)
=\sum_{j\ge1}\frac{M_{3j-1,h}}{(3j)!}\,z_{\rm f}(s)^{3j},
\qquad
z_{\rm f}(s)^3=\frac38s+O(s^2).
$$
Consequently, with its original constants,
$$
\mathcal I_h(s)=\frac{M_{2,h}}{16}s+O(s^2),\qquad
J_h(s)=c_h\mathcal I_h(s),\qquad c_h\ne0.
\tag{823.4}
$$
The factor $1/16$ is $(1/3!)\cdot(3/8)$. The fixed Kodaira–Spencer/isogeny comparison factor $c_h$ is retained; no assertion about its valuation is made.

By R730(730.16), premise (823.3) makes every original primitive $M_{2,h}$ nonzero. For the present proof it already suffices that the $h=1$ component in (823.4) is nonzero. Thus the actual original Hodge space $q^*H^0(A,\Omega^1)$ does not vanish identically under evaluation at $c_1$.

## 2. The actual semilinear action preserves the CM evaluation kernel

Use R819's operator with its original normalization:
$$
\mathcal T(v)=D_{\rho^{-1}}\circ{}^\sigma v,
\qquad
\rho=g(r)/r\in L^\times,\qquad \sigma=g|_L.
$$
Here $g$ is the chosen generator of the actual $\operatorname{Gal}(H/K)$ and
$D_u(x,y)=(u^2x,u^3y)$. R819 proves
$$
K[\mathcal T]\simeq E,\qquad
\operatorname{rank}_{K[\mathcal T]}V=1,
$$
$$
\omega_{\mathcal T v}=\rho\,{}^\sigma\omega_v,\qquad
\omega_v=q^*(v^*\omega_C),\qquad \omega_C=dx/(2y).
\tag{823.5}
$$
These facts use the original primitive summand of the Weil restriction; the imprimitive summands are not in $V$.

Define
$$
\lambda_{c_1}:V\longrightarrow L,\qquad
\lambda_{c_1}(v)
=\left.\frac{\omega_v}{ds}\right|_{c_1}.
\tag{823.6}
$$
This is $K$-linear. Since both $c_1$ and $s$ are defined over $\mathbf Q$, (823.5) gives the exact identity
$$
\lambda_{c_1}(\mathcal T v)
=\rho\,\sigma(\lambda_{c_1}(v)).
\tag{823.7}
$$
Hence $\ker\lambda_{c_1}$ is a $K[\mathcal T]$-submodule of $V$, so it is either $0$ or $V$.

The second possibility is excluded by the actual Hodge realization, not by a claim that arbitrary $L$-linear combinations are homomorphisms. Specifically, R725 proves $A_L\sim_L C^{\dim A}$, and R818 constructs an $L$-basis of $H^0(A_L,\Omega^1)$ by pulling back $\omega_C$ through the coordinate projections of an actual $L$-isogeny. These projections are members of $V$. Thus if all $\lambda_{c_1}(v)$ were zero, the entire original Hodge space would vanish at $c_1$, including the nonzero first coefficient in (823.4). This is a contradiction. Therefore
$$
\boxed{\ker\lambda_{c_1}=0.}
\tag{823.8}
$$

**Theorem 823.1.** At every prime satisfying (823.1) and (823.3), every nonzero original primitive $L$-Hom direction has nonzero differential at the original $c_1$. Every corresponding nonzero actual integral curve map, with the original $c_0$ normalization, is unramified there.

This includes the full original integral lattice of R821. If a member of that lattice factors through the chosen $q$ only after a rational denominator, clear it, apply (823.8), and use that multiplication by a nonzero integer on $C$ is étale in characteristic zero.

## 3. Uniform scope inherited from the original nonvanishing theorem

R729 Theorem 729.1 proves (823.3) for all sufficiently large primes
$p\equiv2,5\pmod9$. Its proof retains both original weight-five and weight-seven central characters and their exact finite CM sums, and transfers the two nonzero primitive averages to the same original label.

Accordingly there exists the same eventual nonvanishing threshold supplied by R729 such that Theorem 823.1 holds for every allowed prime above it. This result neither supplies a numerical value for that threshold nor changes R729's hypotheses. At a smaller individual prime, Theorem 823.1 applies whenever its displayed premise has been established in the original normalization.

The field and kernel argument itself needs no Mordell–Weil rank premise and no nonzero value of a canonical height. The additional R726/R616 premise is needed only when making the original normalized-logarithm statements recalled in the next section.

## 4. The fixed base point and the actual local logarithm

For an actual integral map $u:J_X\to C$ in the original primitive lattice, keep
$$
f_u(x)=u([x-c_0]).
\tag{823.9}
$$
Let $\beta_u=f_u(c_1)$. The local subtraction
$f_u(c_1+s)-\beta_u$ is a point of the formal group at $O$; it does not change the global normalization $f_u(c_0)=O$. The invariant-differential logarithm satisfies
$$
\log_C\bigl(f_u(c_1+s)-\beta_u\bigr)
=\lambda_{c_1}(u)\,s+O(s^2),\qquad
\lambda_{c_1}(u)\ne0.
\tag{823.10}
$$
For a lattice member written through $q$ with a rational denominator, $\lambda_{c_1}(u)$ means the corresponding rational Hom value after this pullback. The equality follows directly by differentiating the formal logarithm normalized by $\omega_C$.

At a chosen $p$-adic place, the logarithm of the actual map is the sum of its fixed value $\log_C\beta_u$ and (823.10). Neither that constant nor a comparison scalar is set to one or discarded.

For comparison with the already registered R682/R729 statement, write the original map into $A$ as
$$
f=q[x-c_0],\qquad \beta=f(c_1),\qquad
\log_A f(c_1+s)=\log_A\beta+U(s).
\tag{823.11}
$$
The nonzero first coefficient in (823.4) implies $U'(0)\ne0$, hence its common first order is one. R729 §6 already drew this conclusion. When the R726/R616 non-torsion and rank hypotheses also hold, R682 gives, in its same real-multiplication coordinates,
$$
t_i(s)=1+T_i s+O(s^2),\qquad
t_i(s)^2-t_j(s)^2=2(T_i-T_j)s+O(s^2),
$$
$$
T_i\ne0,\qquad T_i\ne T_j\quad(i\ne j).
\tag{823.12}
$$
This is a reuse of that result, not a new assertion of common order or a new application of the analytic subgroup theorem.

## 5. Limits and sources

Nonzero differential in characteristic zero does not give a $p$-adic unit, a bound for its valuation, or an inverse on the original depth-four candidate disc. The result does not decide the same-$h$ primitive/Legendre/Cartier unit condition, the actual point $\beta_u$, a Néron comparison factor, or the first nonzero height exterior coefficient. In particular it does not upgrade the known divisibility of a same-target height exterior by $s^2$ to exact order two.

- [R729](R729-uniform-full-Abel-nonvanishing-and-valuation-bound.md), Theorem 729.1 and §6: the original sufficiently-large nonvanishing and the already registered common-order-one conclusion.
- [R730](R730-fixed-depth-original-Abel-isometry-by-all-embedding-norm.md), (730.2), (730.16), §5: the actual coarse parameter, factor $1/16$, nonzero fixed $c_h$ and original coefficient embeddings.
- [R725](R725-original-CM-elliptic-model-and-splitting-field.md), [R728](R728-original-Weil-restriction-primitive-projector-and-Neron-lattice.md), [R818](R818-original-primitive-cusp-coefficients-and-unramified-Hom-existence.md), and [R819](R819-original-primitive-Hom-field-and-all-cusp-nonramification.md): actual Hom realization, original primitive field and semilinear operator.
- [R616](R616-original-CM-point-difference-and-explicit-height-basis.md) and [R682](R682-common-CM-Abel-order-and-saturated-QC-jets.md): actual rational $c_0,c_1$, fixed logarithmic constant and normalized coordinates.

No mathematical computation was run for this proof.
