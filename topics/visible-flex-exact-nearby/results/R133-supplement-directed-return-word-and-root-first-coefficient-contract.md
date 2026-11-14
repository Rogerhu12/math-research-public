# R133 supplement: directed return word and the root first-coefficient contract

Date: 2026-11-14. Scope: the current repaired moving $M=32$ centre at
$\eta=\eta_0$, and the explicit parameter family wherever the stated
certificates apply. **已证明：** the directed operator identities and the conditional matching
contract below. It does not identify the complete return coefficient with a
strict-region integral.

This text was reconstructed after the temporary execution environment
became unavailable. Its mathematical statements retain the reviewed
W.1--W.14 ledger. It is not represented as the original 7,842-byte file
whose SHA256 was
`73fb91f64b6e113d4443b6da583de4d29c1281fa59382bd8f29a527e2b5c0e30`.

## 1. Fix the directed maps before taking a phase

Write $b=\beta_{\mathrm{metric}}$, $q=\sqrt{-K}>0$,
$\eta=-\gamma m>0$, and
$$
 S_0=u^2+Kv^2,\qquad d=-bI S_0.
$$
The subscript on $S_0$ here denotes the scalar quadratic density; it
does not denote a ray map. The two already certified phase velocities are
$$
 F_\pm=bI S_0\pm\eta q=-d\pm\eta q.                 \tag{W.1}
$$
Let $S_\pm(r,\phi)$ be their footpoint maps, with
$$
 (S_\pm)_r+F_\pm(S_\pm)_\phi=0,\qquad S_\pm(0,\phi)=\phi,
 \qquad X_\pm(r,\cdot)=S_\pm(r,\cdot)^{-1}.          \tag{W.2}
$$
The particular return map used by the complete 169-germ transport and by
the subsequent R31 certificate is
$$
                 P_r=S_-(r,\cdot)\circ X_+(r,\cdot). \tag{W.3}
$$
One must keep this order. Squaring this map, exchanging the two rays, or
changing the direction of the word changes the phase problem.

For any orientation preserving angle map $f$, put
$$
 (U_fh)(\phi)=f'(\phi)h(f(\phi)).
$$
Then the ordinary chain rule gives the exact anti-homomorphism identity
$$
                 U_fU_g=U_{g\circ f},\qquad
                 U_f^{-1}=U_{f^{-1}}.              \tag{W.4}
$$
It includes the complete density Jacobian. Replacing $U_f$ by a bare
composition operator would change the subprincipal calculation.

The diagonal principal velocities of the strict Jacobi system are
$$
                 c_\sigma=d+\sigma\eta q=-F_{-\sigma}.
$$
Consequently the principal density propagators from the waist satisfy
$$
 V_\sigma(r)=U_{S_{-\sigma}(r)},\qquad
 V_\sigma(0)=\mathrm{Id}.
$$
Indeed, differentiating the right hand side and using (W.2) gives
$(V_\sigma h)_r=\partial_\phi(c_\sigma V_\sigma h)$.
Thus
$$
 \boxed{V_-^{-1}V_+
   =U_{X_+}U_{S_-}
   =U_{S_-\circ X_+}
   =U_{P_r}.}                                      \tag{W.5}
$$
This proves the direction and normalization of the ray word without an
interpretation based on a finite matrix. The opposite word is its inverse.

## 2. The rotation normalization and the factor $4j$

Suppose the actual certified map has a true angle conjugacy
$$
 G\circ P\circ G^{-1}=R_\Omega,\qquad R_\Omega(x)=x+\Omega.
$$
By (W.4),
$$
 U_{G^{-1}}U_PU_G=U_{G\circ P\circ G^{-1}}
                =U_{R_\Omega}.                     \tag{W.6}
$$
On the fourfold Fourier mode $e^{4ijx}$, $j\ne0$, the last operator has
eigenvalue $e^{4ij\Omega}$. In the current quadratic target,
$\Omega=\pi\rho_{15}/2$, so this eigenvalue is $e^{2\pi ij\rho_{15}}$.
The angular primitive $I=\partial_x^{-1}(1-\Pi)$ has multiplier
$1/(4ij)$, not $1/(ij)$.

The complete strict first-symbol calculation uses the physical angular
derivative and this same primitive. If its directed relative coefficient
is $\int\langle\Xi\rangle\,dr$, its scalar contribution to the phase is
therefore
$$
       -\frac{1}{4j}\int\langle\Xi(r,\cdot)\rangle\,dr. \tag{W.7}
$$
Changing the return word to its inverse reverses both the principal phase
and the directed first coefficient. One cannot retain the old sign of
either term after that change.

The invariant mean used in (W.7) is the complete density mean. Under a
true ray map $\Phi$, the order $-1$ coefficient transforms as
$(a/\Phi')\circ\Phi^{-1}$, and its mean remains $\langle a\rangle$ by
$dx=\Phi' d\phi$. The exact primitive identity retains its separate
mean and finite-rank terms. This is the content of the density-mean
supplement, not permission to suppress the independent even mean in the
full Jacobi system. Passing to a half-density normalization contributes
the known $c_\sigma''$ term at this order; its angular mean is zero.
Its nonmean operator and the order $-2$ remainder still belong to the
complete operator estimate.

## 3. The actual root graph is a separate operator

Fix a genuine strict cut $r_c<r_*$. After the specified strict
normalizer, denote the two components at the cut by $y_+(r_c)$ and
$y_-(r_c)$. The complete regular problem beyond that cut, if it has been
solved with the required source and high-input estimates, supplies a graph
$$
               y_-(r_c)=\mathcal R_c y_+(r_c)+g_c.  \tag{W.8}
$$
Here $\mathcal R_c$ is the actual two-row root/positive connector. It
includes its density principal map, Maslov factor, lower terms, all
couplings to retained low modes and mean, and the regular outer
condition. A local Airy model alone does not supply this graph.

At the exact waist the homogeneous condition $h_1(0)=0$ gives
$y_-(0)=-y_+(0)$, with the current waist normalizer equal to the identity.
The principal propagation of (W.8) back to the waist therefore gives
$$
 \bigl(\mathrm{Id}+V_-^{-1}\mathcal R_cV_+\bigr)y_+(0)
                    =-V_-^{-1}g_c.                \tag{W.9}
$$
The actual equation also retains the complete strict off-diagonal
remainder, all source propagation and the independent mean equation.
Formula (W.9) fixes the homogeneous word inside that larger equation.
It does not discard those terms.

In particular, replacing $\mathcal R_c$ by the identity without a
proved root normalization changes the operator in (W.9). Only after the
principal root connector and its Maslov normalization have been
explicitly accounted for can (W.5) be used as the corresponding principal
ray word of the full return.

## 4. The finite root constant that must be paid

Set $\rho=r_*-r$. The complete strict symbol has the root expansion
$$
 \langle\Xi\rangle
  =g_0\rho^{-5/2}+g_1\rho^{-3/2}+O(\rho^{-1/2}).
$$
The already executed finite-part consumer defines
$$
 X=\lim_{\epsilon\downarrow0}
 \left\{\int_0^{r_*-\epsilon}\langle\Xi\rangle\,dr
       -\frac{2g_0}{3\epsilon^{3/2}}
       -\frac{2g_1}{\sqrt\epsilon}\right\}.          \tag{W.10}
$$
Its output is a complete signed interval for this specified scalar
quantity at the specified centre. The $\delta=0$ public result is
$$
 -73.913337474667<X(0)<-73.913314715519.
$$
These outward rounded endpoints summarize the full native interval from
public run 43591721337; the native remains authoritative.

Suppose a genuine two-row calculation of the normalized root graph
provides its directed scalar coefficient $b_c$, in the same $I$
convention as (W.7). Its finite remainder is then the quantity
$$
 b_{\mathrm{root}}^{\mathrm{fin}}
 =\lim_{\epsilon\downarrow0}
 \left\{\langle b_{r_*-\epsilon}\rangle
       +\frac{2g_0}{3\epsilon^{3/2}}
       +\frac{2g_1}{\sqrt\epsilon}\right\}.          \tag{W.11}
$$
This equality is a definition of the required matching datum. It is not
an assertion that the limit has already been certified for the current
nonlocal operator. Once that matching and the strong remainder are paid,
the contribution of these two pieces is
$$
       -\frac{X+b_{\mathrm{root}}^{\mathrm{fin}}}{4j}. \tag{W.12}
$$
Any other interface or positive-region contribution in the chosen
normalization must be retained as well. In particular, the numerical
interval for $-X/4$ is not by itself a certificate for the full return
coefficient $\beta$.

For the exact scalar Airy comparison $q=\sqrt{\rho}$, $\eta=1$,
$b=0$, one has $g_0=1/16$, $g_1=0$, and the correctly normalized
two-row root coefficient is $-1/(24\epsilon^{3/2})$. Hence (W.11) is
zero in that model. This consistency check explains the cancellation of
the divergent term. It is not a replacement of the actual moving,
nonlocal root problem by the Airy model.

## 5. A finite symmetric root gauge cannot be silently deleted

The current strict normalizer contains at the root the finite matrix
$$
 S_{\mathrm{fin}}
   =s\begin{pmatrix}0&1\\1&0\end{pmatrix},
       \qquad s=(buv/\eta)|_{r=r_*}.                 \tag{W.13}
$$
Its scalar mean is zero by the actual sine/cosine parity, but its full
operator is generally nonzero. To see precisely what has to be tracked,
write $y=(\mathrm{Id}+S_{\mathrm{fin}}I)z$ and let
$y_-=\mathcal R y_+$. On any declared space or high-frequency window where
$\mathrm{Id}-\mathcal R M_sI$ is invertible, the transformed graph is exactly
$$
 \mathcal R_{\mathrm{new}}
   =(\mathrm{Id}-\mathcal R M_sI)^{-1}
      (\mathcal R-M_sI)
   =\mathcal R+\mathcal R M_sI\mathcal R-M_sI
      +O(I^2).                                    \tag{W.14}
$$
For the order $-1$ calculation alone, the second equality is also the formal
symbol expansion of this graph relation; it does not assert a global low-mode
inverse. That inverse and its mean block remain part of the full connector.
For a scalar principal reflection $\mathcal R=r\,\mathrm{Id}$, the
displayed correction is $(r^2-1)M_sI$. For a nontrivial density
pullback, both compositions in (W.14) must be conjugated with the actual
map. The statement $\langle s\rangle=0$ alone does not remove this
correction.

## 6. Exact remaining contract

The ledger has fixed the directed word, its density convention, the
$4j$ normalization, the strict finite-part subtraction, and the root
coefficient needed for matching. Completing the full return now requires
the actual two-row connector (W.8), its finite scalar in (W.11), and a
strong remainder in the Sobolev window required by the high-frequency
inverse. The whole positive region must include high-input feedback,
mean and source ports. The explicit $\delta_*$ family requires its own
parameter-transfer payment for $X$, the connector and all strong
constants. Finally, transferring from this explicit family to the true
PDE branch still requires the full inverse and parameter Schur argument.

No statement here grants any of those unpaid terms a zero value. The
principal arithmetic gap for the current target remains $1/(68|j|)$;
the older $1/(36|j|)$ constant is not transferred to $\rho_{15}$.
