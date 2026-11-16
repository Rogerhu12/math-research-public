# R133 supplement: rigidity of the true paired reflections in the selected principal angle

2026-11-16, phase_inverse.

**Proved analytic consequence of the original true rays and the already certified selected conjugacy.** The two geometric reflections in the selected angle are constant-phase reflections. In particular the nonmean block of the physical paired-waist reflection is an exact isometry in every fixed Sobolev window. Its full mean column remains a nontrivial density rank. The phase-transported natural input space remains the different space specified in NIF.

This note performs no new scientific arithmetic and changes no completed source, receipt or bound. It identifies a concrete coordinate realization of the prescribed physical waist target; it does not prove that the actual waist map is onto that target, or turn a full-circle principal inverse into an inverse on the same reflected input space.

## RRF1. Original objects and immutable evidence

Use the same continuously repaired real family as NIF,
$$
 Q_\delta=Q_0+\delta Z_{\rm can},\qquad
 \nu_\delta=\nu_0+\delta,\qquad
 \eta_{\rm intrinsic}=\eta_0,\qquad |\delta|\le10^{-8}.
 \tag{RRF.1}
$$
For the rigidity statement fix exactly the selected pair
$(\delta_*,\mathcal H)$ supplied by the physical strip theorem W, from run 43588332723, attempt 1 and loss $1/250$. No other selected parameter or bookkeeping loss is identified with it.

All circles have physical period $\ell=\pi/2$, normalized measure and frequencies $4j$. The raw waist reflection and the root reflection act by the same formula in their respective coordinates:
$$
 Rf(\phi)=f(-\phi),\qquad R_*f(x)=f(-x).
 \tag{RRF.2}
$$
Write $\Pi$ for the full mean projection, $P=1-\Pi$, and
$\Lambda_j=(1+16j^2)^{1/2}$. The two physical mean entries of a state remain separate; a relation proved on a reflected homogeneous subclass does not remove them from the complete port problem.

The exact primary inputs are the following complete small texts.

| Primary and use | Immutable Git blob | Bytes | SHA256 |
|---|---|---:|---|
| N.2--3: actual parity and complete moving drift | 8a57ec851fc9029e4319650b87360b9867d22a97 | 15539 | 0645cf460507ea587056b6969b01dc532b6623179db5598e2bffe4f53a8275af |
| PF.3, PF.17 and PF.27: true root initial identities, actual rays and original waist lifts | e384f8711a44e1ad16dd05804faf65d62bf016c2 | 20413 | 5856c8cf5fac8c75997a6e3d8c9aba1ad88cb136d1ae184985164d1745aab026 |
| W.3, W.7 and W.12: the exact selected conjugacy, exact irrational rotation and its real degree-one lift | a79a7ad7c147076b044389e98a15ab2f341d0d0c | 6138 | 1e8d001a5878da2894b4c9ab88baf00555ca8364b23f49df8c827c23a7da88c3 |
| MS.3 and MS.13--19: the same selected density chart and exact outgoing order | 10fdaddc0114e25ad349f1f411e80baf4f98fe26 | 19522 | 44038eaed377863961aad7f0c74caa2bf498d6a689812f05933111777c191161 |
| NIF.5--13 and NIF9: corrected phase-transported natural input domain | d606faa1ffd30c34d3487985a57dbc62a18890bc | 32942 | 8f3784473b98f9b49449b7012e4c5c919670418246fa03a7f28441aaca28b640 |
| WPR.11--21 and WPR.22--28: complete paired reflection, physical waist row and non-preservation of the frozen input space | 226272031762c5fcace679dd7f940a35040401dc | 22571 | 707b8269e454cab738fe70d84097087a0cf5c74026916a2f8bdc151435eca9cb |

These identities concern the true original maps. No approximate finite ray, a newly centred lift or an estimated endpoint map is substituted.

## RRF2. Reflection of the true root-based rays

In the original moving convention, $u$ is odd, $v$ is even and the intrinsic coefficients are radial. N.2--3 give
$$
 d=-\beta I(u^2+Kv^2),\qquad I=\partial_\phi^{-1}P,
 \qquad d(r,-\phi)=-d(r,\phi).
 \tag{RRF.3}
$$
The full mean of $v$ and the mean subtraction inside $I$ are retained. The assertion follows because $I$ sends even functions to odd functions and kills their mean.

Use PF's root coordinate $\rho=r_*-r$, with
$q=\sqrt{\rho k(\rho)}$, and let
$H_\sigma(\rho,\cdot)=\Phi_\sigma(\rho,\cdot)^{-1}$. PF.17 is the actual initial-value problem
$$
 \partial_\rho H_\sigma(\rho,x)
   =d\bigl(\rho,H_\sigma(\rho,x)\bigr)
     +\sigma\eta(\rho)\sqrt{\rho k(\rho)},\qquad
 H_\sigma(0,x)=x.
 \tag{RRF.4}
$$
Here $\eta=-\gamma\langle v\rangle$ is the characteristic coefficient, not the fixed intrinsic parameter $\eta_0$.

The function $-H_{-\sigma}(\rho,-x)$ solves the same equation and has the same initial value as $H_\sigma$. Uniqueness therefore gives the exact lift identities
$$
 H_\sigma(\rho,-x)=-H_{-\sigma}(\rho,x),\qquad
 \Phi_\sigma(\rho,-\phi)=-\Phi_{-\sigma}(\rho,\phi).
 \tag{RRF.5}
$$
This is uniqueness for the actual characteristic equation, whose angular velocity is locally Lipschitz in the angular variable. Its radial coefficients are continuous across the original repaired interfaces; their higher radial derivatives need not agree there. No derivative matching or omitted jump assumption is needed for (RRF.5).

The initial identity is fixed by PF.3 and PF.17, not chosen to make (RRF.5) hold. PF.27 also fixes the original waist-based lifts $S_\pm(0)=\operatorname{id}$, with $X_\pm=S_\pm(r_*)^{-1}$, and identifies the root-normalized phase at the waist by
$$
 \Phi_\sigma(r=0,\cdot)=X_{-\sigma}.
 \tag{RRF.6}
$$
Consequently, at that same waist,
$$
 X_-( -\phi)=-X_+(\phi),\qquad
 X_-'(-\phi)=X_+'(\phi).
 \tag{RRF.7}
$$
The derivatives are positive. For the original positive density pullback
$U_F f=F'(f\circ F)$ on orientation-preserving maps, (RRF.7) proves
$$
 \boxed{\quad R\,U_{X_-}=U_{X_+}R_*.\quad}
 \tag{RRF.8}
$$
All these ray-reflection identities apply to every real family member for which the original true rays are defined. Only the next conjugacy and rigidity statements are restricted to $\delta_*$.

## RRF3. Two positive density involutions and their exact product

For an orientation-reversing map, use the pullback of an unsigned density:
$$
 \mathfrak U_F f=|F'|\,(f\circ F).
 \tag{RRF.9}
$$
It equals $U_F$ for orientation-preserving $F$. It preserves the normalized integral in either orientation and satisfies
$\mathfrak U_F\mathfrak U_G=\mathfrak U_{G\circ F}$.
In particular $\mathfrak U_{\phi\mapsto-\phi}=R$. The negative derivative of a reversing map must not be inserted into the positive-orientation formula for $U_F$.

Freeze the original selected chart
$$
 \mathcal S=U_{\mathcal H^{-1}}U_{X_-},
 \qquad
 J_0=U_{\mathcal H^{-1}}R U_{\mathcal H},
 \qquad
 J_1=\mathcal S R_*\mathcal S^{-1}.
 \tag{RRF.10}
$$
They are bounded conjugations on each fixed qualified distributional window, and $J_0^2=J_1^2=\operatorname{Id}$. Each $J_i$ is the positive density pullback of an orientation-reversing circle diffeomorphism. The map underlying $J_0$ is
$$
 \rho_0=\mathcal H\circ(\phi\mapsto-\phi)\circ\mathcal H^{-1}.
 \tag{RRF.11}
$$
For $T_\Omega(x)=x+\Omega$, the exact selected MS identity is
$$
 U_{\mathcal H^{-1}}U_{X_+}=U_{T_\Omega}\mathcal S.
 \tag{RRF.12}
$$
Combining this with (RRF.8), in the stated order, yields
$$
 \begin{aligned}
 J_0J_1
 &=U_{\mathcal H^{-1}}R U_{X_-}R_*U_{X_-}^{-1}U_{\mathcal H}\\
 &=U_{\mathcal H^{-1}}U_{X_+}U_{X_-}^{-1}U_{\mathcal H}\\
 &=\boxed{\,U_{T_\Omega}\,}.
 \end{aligned}
 \tag{RRF.13}
$$
No multiplier, sign operator, moving projection or mean rank was commuted through another factor in this calculation. Equivalently, PF.27 writes the actual return as $P=X_-^{-1}\circ X_+$; (RRF.7) gives $r_0\circ P\circ r_0=P^{-1}$ for the point reflection $r_0(\phi)=-\phi$. Thus the reverser in (RRF.13) belongs to exactly the same directed return as W.3.

The same selected rotation is fixed exactly by W.3:
$$
 \Omega=\frac{\pi}{2}\,
       \frac{5831714953207175+\sqrt5}{21212218271020390}.
 \tag{RRF.14}
$$
Thus $\Omega/\ell$ is irrational. This uses only the displayed exact expression and irrationality of $\sqrt5$. It does not evaluate a new Diophantine constant or replace the actual selected rotation by a rounded angle.

## RRF4. Rigidity and the surviving phase

Since $J_0$ and $J_1$ are involutions, (RRF.13) implies
$$
 J_0U_{T_\Omega}J_0=U_{T_{-\Omega}}.
 \tag{RRF.15}
$$
Positive density pullbacks determine their underlying circle maps: applying them to $1$ identifies their positive density factors, and applying them to the Fourier functions then identifies the maps modulo $\ell$. Therefore (RRF.15) implies
$\rho_0\circ T_\Omega\circ\rho_0=T_{-\Omega}$ on the circle.

Choose the actual lift
$\rho_0(x)=\mathcal H(-\mathcal H^{-1}(x))$. It has degree $-1$ and satisfies $\rho_0^2=\operatorname{id}$ as a lift. For some fixed integer $m$, the circle relation gives
$$
 \rho_0(x+\Omega)=\rho_0(x)-\Omega+m\ell.
 \tag{RRF.16}
$$
The function $p_0(x)=\rho_0(x)+x$ is continuous and $\ell$-periodic. Iterating (RRF.16) gives
$p_0(x+n\Omega)-p_0(x)=nm\ell$. Boundedness of $p_0$ forces $m=0$. Irrationality in (RRF.14) and continuity then force $p_0$ to be constant.

For $R_a f(x)=f(a-x)$, the exact conclusion is
$$
 \boxed{\quad
 \rho_0(x)=a-x,\qquad J_0=R_a,\qquad
 J_1=R_{a+\Omega}.
 \quad}
 \tag{RRF.17}
$$
The last equality follows from $J_1=J_0U_{T_\Omega}$, since
$R_aU_{T_\Omega}=R_{a+\Omega}$ with this pullback convention.
Both $R_a$ and $R_{a+\Omega}$ are isometries on every fixed Bessel $H^s$ and preserve the full mean. There is no additional Jacobian bound in their norms.

The surviving phase is determined by the original chosen lift:
$$
 \mathcal H(-\phi)+\mathcal H(\phi)=a,\qquad
 a=2\mathcal H(0)
   =2\langle\mathcal H(\phi)-\phi\rangle.
 \tag{RRF.18}
$$
Its circle action depends only on $a$ modulo $\ell$. Formula (RRF.18) also gives
$\mathcal H'(-\phi)=\mathcal H'(\phi)$. If that same lift were separately known to satisfy
$\langle\mathcal H-\operatorname{id}\rangle=0$, then $a=0$. The cited W.12 constructs the lift but does not explicitly impose that zero-mean normalization on its final physical composition. Accordingly this note retains $a$ and makes no unproved identification with zero.

## RRF5. The complete physical paired reflection and the actual waist target

WPR.15--16 gives the exact selected paired-state map
$$
 K_{\mathcal H}
  =U_{\mathcal H^{-1}}(R-2\Pi)U_{\mathcal H}.
 \tag{RRF.19}
$$
Set
$$
 h=U_{\mathcal H^{-1}}1=(\mathcal H^{-1})',
 \qquad h>0,\qquad \Pi h=1.
 \tag{RRF.20}
$$
Using (RRF.17) but preserving the full mean term,
$$
 \boxed{\quad
 K_{\mathcal H}=R_a-2h\otimes\Pi,\qquad R_a h=h.
 \quad}
 \tag{RRF.21}
$$
The identity $R_a h=h$ also follows by applying $J_0$ to $U_{\mathcal H^{-1}}1$. Hence $K_{\mathcal H}^2=\operatorname{Id}$ and
$\Pi K_{\mathcal H}=-\Pi$, as in the original paired relation.

On the nonmean space, the restriction is exactly $R_a$. On the full orthogonal decomposition $H^s=PH^s\oplus\mathbb C$, it is the triangular map
$$
 K_{\mathcal H}
   =
 \begin{pmatrix}
  R_a|_{PH^s} & -2(h-1)\\
  0&-1
 \end{pmatrix}.
 \tag{RRF.22}
$$
In particular the full operator is not asserted to be unitary. The column $-2(h-1)$ is retained and is not replaced by zero. The two stored physical mean entries and the original independent matching rows are retained in the ambient port realization. Writing their reflected-subclass relation does not solve those matching equations or claim two independent state means within that subclass.

Let $\mathcal W_{\rm raw}^{\rm ne}$ denote the actual primitive waist row of WPR.20--21, with all its original factors, sources and low modes retained. Its prescribed raw output space is
$P\operatorname{Fix}(R)$, because the raw $h_1$ is odd and its original primitive is even and meanzero. The selected coordinate image of this prescribed target is exactly
$$
 U_{\mathcal H^{-1}}\bigl(P\operatorname{Fix}(R)\bigr)
   =P\operatorname{Fix}(R_a).
 \tag{RRF.23}
$$
Indeed the density pullback preserves the mean and conjugates $R$ to $R_a$. The inverse $U_{\mathcal H}$ proves the reverse inclusion.

Equation (RRF.23) identifies the target coordinate space. It asserts neither that the actual waist row is onto this space nor that its kernel is zero. It includes the full low and high output; no new output cutoff is inserted. The separate raw mean row remains exactly the one in WPR.

## RRF6. The natural input reflection still contains the Maslov sign operator

Retain NIF's fixed phase on the nonmean carrier,
$$
 D_+=e^{-i\pi/4}\Pi_+ + e^{i\pi/4}\Pi_-,
 \qquad
 Z=\Pi+i\Pi_+-i\Pi_-,
 \qquad Z^{\mathcal S}=\mathcal S Z\mathcal S^{-1}.
 \tag{RRF.24}
$$
The corrected input space is
$$
 X_s^{\rm fr}=\mathcal S D_+\mathcal H_{\rm nat}^s,
 \qquad
 \mathcal H_{\rm nat}^s=P_{97}\operatorname{Fix}(R_*),
 \qquad
 P_{97}^{\mathcal S}=\mathcal S P_{97}\mathcal S^{-1}.
 \tag{RRF.25}
$$
On the nonmean carrier, reflection interchanges the two Fourier signs. Thus
$$
 D_+R_*D_+^{-1}=-Z R_*,
 \qquad
 J_X:=\mathcal S D_+R_*D_+^{-1}\mathcal S^{-1}
       =-Z^{\mathcal S}R_{a+\Omega}.
 \tag{RRF.26}
$$
This is an involution on that carrier. Its actual reflected projector is
$$
 Q_{\rm nat}^{\rm fr}
   =\frac12P_{97}^{\mathcal S}
               \bigl(\operatorname{Id}-Z^{\mathcal S}R_{a+\Omega}\bigr).
 \tag{RRF.27}
$$
The factors commute where required because they are the transported root projector and root involution. Formula (RRF.27) does not say that
$P_{97}^{\mathcal S}$ is a selected Fourier cutoff or an orthogonal projection.

For completeness, if $D_+$ is extended by the identity on the auxiliary scalar mean, then $D_+R_*D_+^{-1}=(2\Pi-Z)R_*$. Its full conjugated involution is
$$
 J_X^{\rm full}
  =-Z^{\mathcal S}R_{a+\Omega}
         +2(\mathcal S1)\otimes\Pi.
 \tag{RRF.28}
$$
The ambient physical mean ports retain their original extension; they are not identified with this auxiliary scalar mean.

The rigidity of the two geometric involutions does not set
$Z^{\mathcal S}=Z$, commute it through the selected rotation, or replace
$J_X$ by $R_a$. Therefore the input $X_s^{\rm fr}$ is not identified with the target in (RRF.23). WPR's full-circle non-preservation argument and its distinction between the actual image and the same frozen input space remain in force.

## RRF7. Consequence and limits

The new exact information is (RRF.17), the complete mean-column statement (RRF.21)--(RRF.22), and the target identification (RRF.23). It can be used in a subsequent correctly typed physical waist construction without charging a nonmean reflection by a product of two coordinate norm bounds. No new scalar value is needed to establish that nonmean isometry.

The complete waist row still has its actual ordered normalizer, primitives, two-state reconstruction, leading amplitudes, source and interface terms, and independent mean rows. The common input still has the exact $D_+$ phase, the transported natural projector and any independently declared rest inputs. The already completed NIF inverse transports the original stable map in its qualified spaces; it supplies no missing physical waist surjectivity, auxiliary full-circle restriction, finite Schur inverse or nonlinear-background result.

All selected-angle conclusions in RRF3--7 concern the single certified $\delta_*$. The raw characteristic-reflection proof RRF2 is a family identity, but no family of selected conjugacies or rotation normal forms is thereby constructed. No old successful calculation is repeated, and no completed numerical receipt is edited.
