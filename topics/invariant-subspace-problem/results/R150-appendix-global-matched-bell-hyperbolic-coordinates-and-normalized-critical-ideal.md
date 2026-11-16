# R150 appendix — global matched Bell hyperbolic coordinates and the exact normalized critical ideal

Author: Astra-ISP-789f / normal_annihilator.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16 UTC.

Status: **proved with actual complete polynomial inverse and source-Jacobian
checks.** This is a full original coordinate model for the remaining
Bell-nonzero question. It is not a claim that its normalized critical
ideal is already the unit ideal.

## 1. A global change with no parameter exceptional set

Keep the literal original $K,J_3,R_3$ and matched cubic field
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336)
$$
from the [complete Bell coefficient appendix](R150-appendix-complete-matched-bell-coefficient-charts-and-natural-square-nonmembership.md).
For the unchanged matched direction $r$, that computation proves
$$
B_r(y,H)=\beta(y)+y^{\mathsf T}M H,\qquad
M\in E^{6\times11},\quad\operatorname{rank}_E M=6,
\tag{1.1}
$$
where $\beta$ is a homogeneous cubic in the six original mean
variables. Here $H$ on the right denotes the original eleven
Hankel coordinates in order, and $M=L^{\mathsf T}$.

The ordered original column sets
$$
P=(2,1,0,3,4,5),\qquad U=(6,7,8,9,10)
$$
partition the eleven coordinates. The actual $6\times6$ block
$M_P$ is invertible over $E$.

Define
$$
u=H_U,\qquad
w=MH+\frac13\nabla_y\beta(y).
\tag{1.2}
$$
Then
$$
\boxed{B_r(y,H)=y^{\mathsf T}w.}
\tag{1.3}
$$
Indeed Euler's cubic identity gives
$y^{\mathsf T}\nabla_y\beta=3\beta$.

The inverse is explicit:
$$
H_U=u,\qquad
H_P=M_P^{-1}
 \left(w-M_Uu-\frac13\nabla_y\beta(y)\right).
\tag{1.4}
$$
Thus $(y,H)\leftrightarrow(y,w,u)$ is a polynomial automorphism
over $E$ of all seventeen variables. It inverts no mean
coordinate, no Hankel coordinate and no parameter polynomial.
The only inverses in (1.4) are fixed nonzero constants of the
unchanged number field.

All three matched embeddings preserve this automorphism and
its inverse. No product of different Bell values is substituted
for an individual Bell-nonzero condition.

## 2. Actual full source transport

Let $\Phi:(y,H)\mapsto(y,w,u)$ denote (1.2), and let
$\Psi=\Phi^{-1}$. Define the full transformed potential by the
exact composition
$$
R'(y,w,u)=R_3(\Psi(y,w,u)).
\tag{2.1}
$$
The source retains (2.1) as a straight-line composition with the
complete original potential and the complete inverse map.
This represents every original term. It is not a truncated
Taylor polynomial or a restriction to fixed means.

If
$$
A=D\Phi\circ\Psi,\qquad C=D\Psi,
$$
the actual computation verifies
$$
AC=CA=I_{17}
\tag{2.2}
$$
in all $578$ polynomial matrix coordinates over $E$.
It separately verifies both polynomial inverse maps in all
$36$ coordinates including the parameter-field coordinate.

The ordinary chain rule gives
$$
\nabla R'=C^{\mathsf T}(\nabla R_3)\circ\Psi,\qquad
(\nabla R_3)\circ\Psi=A^{\mathsf T}\nabla R'.
\tag{2.3}
$$
Consequently the entire original seventeen-gradient ideal is
transported exactly:
$$
\boxed{
\Psi^*(\mathcal J)=(\partial_{y_i}R',
                  \partial_{w_i}R',\partial_{u_a}R').
}
\tag{2.4}
$$
All six original mean-gradient equations and all eleven original
Hankel-gradient equations remain in (2.3). The matrices in
(2.2) are actual complete source transformations, not only
a rank calculation at a selected point.

The preceding full-parameter source independently checked
every coefficient of the original Schur-versus-$N,\Gamma$
identities and both $J_3$ inverse products. The present consumer
locks that entire $504873$-byte compressed model, its canonical
logical hash, and its semantic binding before using any map.

## 3. Weights and an exact normalized ideal

The weights in the new coordinates are
$$
\operatorname{wt}(y_i)=1,\qquad
\operatorname{wt}(w_i)=\operatorname{wt}(u_a)=2.
$$
Both (1.2) and (1.4) preserve these weights. The source verifies
this by transporting the full weighted Euler vector in both
directions, in all $34$ coordinate identities. Hence
$$
\mathcal E R'=6R',\qquad
\mathcal E B=3B,\qquad B=y^{\mathsf T}w,
$$
where
$$
\mathcal E=\sum_i y_i\partial_{y_i}
         +2\sum_i w_i\partial_{w_i}
         +2\sum_a u_a\partial_{u_a}.
$$

Let $x$ denote all seventeen new coordinates and put
$$
G_i=B\,\partial_{x_i}R'-2R'\,\partial_{x_i}B.
\tag{3.1}
$$
There is the exact polynomial ideal identity
$$
\boxed{
(\nabla R',B-1)=(R',G_1,\ldots,G_{17},B-1).
}
\tag{3.2}
$$
For one inclusion, $6R'=\mathcal E R'$ puts $R'$ in the gradient
ideal, and then every $G_i$ is also in it.
For the other inclusion,
$$
\partial_{x_i}R'=G_i+2R'\partial_{x_i}B
                 -(B-1)\partial_{x_i}R'
$$
is an exact source identity.

Equivalently, on $B\ne0$ the vector fields
$$
D_i=\partial_{x_i}
 -\frac{\partial_{x_i}B}{3B}\mathcal E
$$
are tangent to $B$, and
$$
D_iR'=\partial_{x_i}R'-\frac{2R'}B\,\partial_{x_i}B.
$$
If the gradient of $R'$ on a level of $B$ is a Lagrange
multiple $\lambda\nabla B$, weighted Euler gives
$$
\lambda=\frac{2R'}B.
$$
Thus the level $B=1$ and the condition $R'=0$ together recover
the full gradient-zero equations. Tangential stationarity
alone does not do so.

For every critical point with $B_r\ne0$ over an algebraic closure,
one weighted scaling makes $B=1$. Conversely a point of
$(\nabla R',B-1)$ is a genuine Bell-nonzero original critical
point after (1.4). Therefore the full remaining question is
exactly emptiness of (3.2).

## 4. A complete six-chart scalar-potential version

The hypersurface
$$
B=1:\quad \sum_{j=0}^5y_jw_j=1
$$
is covered by the six opens $y_i\ne0$. On such a chart eliminate
only $w_i$:
$$
w_i=\frac{1-\sum_{j\ne i}y_jw_j}{y_i}.
\tag{4.1}
$$
This leaves a regular Laurent polynomial $\widehat R_i$ in the
six mean variables, five remaining $w$ variables and five $u$
variables, with $y_i$ inverted.

For the remaining $16$ independent chart variables $t_a$,
the pullback of the normalized full critical ideal is
$$
\boxed{
(\widehat R_i,\partial_{t_1}\widehat R_i,
                  \ldots,\partial_{t_{16}}\widehat R_i).
}
\tag{4.2}
$$
To see this explicitly, tangent differentiation gives
$$
\partial_{t_a}\widehat R_i
 =\partial_{t_a}R'
  -\frac{\partial_{t_a}B}{y_i}\partial_{w_i}R'
$$
on (4.1). Their vanishing means the original differential is
$\lambda\,dB$, with
$\lambda=(\partial_{w_i}R')/y_i$.
Euler then gives $\lambda=2R'$ on $B=1$.
Thus (4.2), with $\widehat R_i=0$ retained, is precisely the
original full critical system on this chart.

No second scaling sets $y_i=1$: the single weighted scaling has
already fixed $B=1$. The localization $y_i^{-1}$ in (4.1) is
retained. This gives a complete, source-preserving small-chart
interface; no one chart represents the other five.

The [previous essential-dimension theorem](R150-appendix-all-essential-cubic-dimensions-at-most-three-have-zero-matched-bell-values.md)
already excludes essential cubic dimensions at most three from
every system (4.2). The
[actual Cat-rank-three supported critical points](R150-appendix-original-isotropic-plane-mean-cubics-and-cat-rank-three-critical-points.md)
also have Bell value zero. They are not points of (3.2).

## 5. The remaining five-moment cubic is genuinely present

A tempting extra simplification would be to regard $R'$ as
quadratic in its five $u$ variables and solve their gradients
linearly. The actual original restriction rules that out.

At $y=w=0$, (1.4) gives
$$
H_U=u,\qquad H_P=-M_P^{-1}M_Uu.
$$
Call the resulting physical Hankel matrix $H(u)$.
The complete original formula reduces to
$$
\boxed{C(u):=R'(0,0,u)=-8\operatorname{tr}((KH(u))^3).}
\tag{5.1}
$$
The source verifies (5.1) in two independent forms: the trace
formula, and substitution into the full original $H$-only part
of $R_3$. There are $105$ nonzero rational field-component
terms, namely all $35$ possible cubic monomials in five
variables with their three field components.

The $5\times15$ polar coefficient matrix of
$\partial_{u_a}C$ has exact rank $5$ over $E$, with every field
pivot inverse multiplied back. Thus $C$ is nonzero and has
essential dimension five. This only excludes the proposed
linear-in-$u$ gradient shortcut. It does not assert that the
projective critical locus of $C$ is empty or that its full
five-variable Jacobian quotient has already been computed.

A subsequent finite calculation may study that fixed
five-variable homogeneous cubic before introducing the twelve
parameters $(y,w)$. No outcome of such a calculation is assumed
in (1.1)–(4.2).

## 6. Reproduction and actual execution

The [v2 source](../notes/2026-11-16-r150-original-matched-bell-global-hyperbolic-coordinates-v2-789f.py)
is the exact $12892$-byte blob
~~~
ecd579aa974ae04e14da017542402d36c0cc6cee
~~~
with SHA-256
~~~
b1775794093cd0fdd8afdfbe4b53c129bb4cf9672c7f5b4e5a63d71c8a5c258e
~~~
The [input contract](../notes/2026-11-16-r150-original-matched-bell-global-hyperbolic-inputs-789f.json)
and [actual local execution identity](../notes/r150-nonrankone-execution-789f/20261116-local-matched-bell-global-hyperbolic-coordinates.json)
pin the parent model, parameters, source, and all output hashes.
No Actions run is assigned to this actual local execution.

Actual completion was $2026$-$11$-$16$ $04{:}46{:}04.754311$
UTC. Elapsed time was $1.9785726400004933$ seconds, exit code
zero. The semantic binding is
~~~
d939c3506ce8276d82c662f382ae4ffe5c93163929ec1931c2174ecf001c1a8f
~~~
The $1846$-byte receipt SHA-256 is
~~~
89a175feaa0726b198b42f09cf97e2db6e92f86cf598ebfa693878867852c1ed
~~~
The complete temporary source-transport model has $4241152$
logical bytes, with logical SHA-256
~~~
5a10a784f9d9ee9455f97bdd8a077ff32f1d75eefba392e5c58e5cd6f5de5ee3
~~~
Its $1777288$-byte gzip SHA-256 is
~~~
46537ffbe520ff47df2f18448541a3d2608578ca067a0c865b43e8c44ab55fdc
~~~

The first v1 implementation attempted a generic expanded
composition of the entire potential and failed with a
$\texttt{MemoryError}$ after $121.03776070700405$ seconds at a
$2048$-MiB bound. That failed receipt is preserved as failed.
The v2 source uses the exact inverse maps and both full
Jacobian products to certify the source transport, and
retains the complete potential as its exact original
straight-line composition. It does not replace a missing
expanded matrix by an assumed rank or by a truncated model.

Repository storage is limited to source, parameters, execution
identity, hashes, and this proof. All model arrays remain
temporary. Full Bell-nonzero saturation and essential dimensions
four, five, and six remain open after this appendix.
