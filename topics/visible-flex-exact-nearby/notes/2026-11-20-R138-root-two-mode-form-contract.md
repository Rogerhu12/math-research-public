# Complete actual-root signed 96/97 form

2026-11-20, global_route. Scientific source:
`fourfold_codazzi_root_two_mode_form.py`. This is one new finite signed-form target;
it neither proves nor disproves invertibility of the actual boundary problem.

## Scope and accepted inputs

Use the same repaired candidate, same actual root interval, fixed physical
eta, fixed point `(0,0,1/2)`, full original circle, mean and reflection class
as R138 U, W, X and F. The modes are the original j=96 and j=97. The
computational subspace does not alter the original low1..96/high97..infinity
root condition. All other entries of this particular test direction are
zero; none of the equations of the full operator is deleted.

Read the whole completed axis conclusion/execution from 44730968113/1,
the whole mean conclusion/execution from 44733403315/1, and the whole X
physical conclusion/execution from 44737045152/1. Every source hash, true
root interval, original candidate/germ identity and successful complete
execution is admitted. In particular, X's false sufficient body gates
remain false whole-object references. No axis, mean, X or old geometry
target is invoked. Original candidate shards and the original root germ
are restored only as the exact definition consumed by the already fixed
axis helper; that helper's numerical axis entry is not called.

The complete saved nominal q and s balls are each enlarged by the entire
saved axis error upper. This rectangular enclosure includes the original
Euclidean error ball. It is not clipped using q<0 or s>0. The coarse display
`true_root_support_coordinates` is not used. The complete actual D ball,
not its midpoint or Boolean flag, must satisfy D>17/20. Its full reciprocal
is retained in the two new mean functionals.

## Exact finite form

Use normalized L2 and z1=sqrt(2)sin(384 phi), z2=sqrt(2)sin(388 phi).
For f=S z with S=P_low N+P_high N^(1/3), put

    f_i=F_i sqrt(2)sin(n_i phi),
    q_i=Q_i sqrt(2)sin(n_i phi),
    R_i=Rweight_i sqrt(2)cos(n_i phi),
    T_i=Tweight_i sqrt(2)cos(n_i phi),

where

    n=(384,388), F=(384,388^(1/3)), Q=(0,388^(-1/3)),
    Rweight=(1,388^(-2/3)), Tweight=(0,388^(-4/3)).

For the actual periodic frame define

    rho=a/m, Tvec=X-uY, Avec=X'-uY',
    k=rho*Tvec/v, b=rho*Y, c=-rho*Avec/v,
    e_i=b' R_i+c' T_i, y_i=k q_i-b R_i-c T_i,
    ell_i=D^(-1)<e_i> dot local_ez,
    v_i=e_i-gm ell_i, V_i=I v_i.

The actual mean vector is computed from the exact U.4 coefficient formula,
not from an ideal-frame mean certificate:

    q0=-I(v-m)/m,
    A0=1/v-q0*v'/v^2, B0=-u*A0-q0*u'/v,
    gm=rho*(A0 X+B0 Y).

D is the prior actual saved denominator. The original symmetry and mean
compatibility prove <v_i>=0, <y_i>=0 and I Rf_i=y_i+V_i. The new primitive
enclosures must also contain the exact zero full integrals of v_i in all
three environment components; this is a consistency check of the new
columns, not a new computation of D.

Here is the derivative-free identity used below. Since R'=-f and T'=-q,
put p=bR+cT and e=b'R+c'T. The uncorrected curvature column is
(kq)'+bf+cq=(kq-p)'+e=y'+e. Thus the mean-eliminated column is y'+v
and its zero-mean primitive is y+Iv. Expanding the original U.15 energy
and integrating only the (Iv) cross y' term by parts gives exactly

    <G dot[y cross y'+2y cross v+(Iv) cross v]
          -G' dot[(Iv) cross y]>.

Substitute y=kq-bR-cT and v=e-gm ell. In the k/b terms, integration of
q' gives 2<G dot(k cross b) f q> plus
<-G' dot(k cross b) Rq-2G dot(k cross b') Rq>. The last term cancels
the corresponding term from 2<G dot(y cross e)>. Expanding the k/c
and b/c terms in the same ordered cross products gives the following
seven coefficients (and the full mean rank and primitive terms below):

    a0=2G dot(k cross b),
    Aqq=G dot(k cross k'+2k cross c),
    ARR=-G dot(b cross b'), ATT=-G dot(c cross c'),
    ARq=-G' dot(k cross b)-2G dot(b cross c),
    AqT=-G' dot(k cross c),
    ART=G' dot(b cross c)+2G dot(b' cross c).

The local polynomial is

    a0*f*q+Aqq*q^2+ARR*R^2+ATT*T^2
           +ARq*R*q+AqT*q*T+ART*R*T.

Its full bilinear polarization is integrated before taking any sign.
The remaining matrix entries are exactly

    -ell_i <G dot(y_j cross gm)>-ell_j <G dot(y_i cross gm)>
    +1/2 <G dot(V_i cross v_j+V_j cross v_i)>
    -1/2 <G' dot(V_i cross y_j+V_j cross y_i)>.

There is no omission of the independent mean, whole-circle primitive,
off-diagonal term, actual frame defect, or inverse-angle term already
encoded in U.4. All derivatives are moving-angle derivatives. Since G is
G_inc+q_axis*local_ez+s_axis*local_ex and G' is independent of the two axis
coordinates, the entire matrix is evaluated affinely in those coordinates.
This calculation needs no positivity assumption at artificial vertices.

## Complete angular enclosures and actual-frame transfer

Use 32768 closed cells covering [0,2*pi], with 320-bit Arb. On every whole
cell evaluate all 32 original sine/cosine modes and their derivatives, with
the complete Qrepair coefficient errors from the fixed definition helper.
Keep signed m<0 and v<0. Let s=v/m and

    Omega=Omega(b0*v/m,a*u/m,a/m), f=(0,a*v/m,0).

A private nominal frame uses the exact exponential of the midpoint skew
matrix on each cell. The complete local frame error is the old error plus
h*||Omega-Omega_mid||. The true ideal frame is orthogonal, so this error is
additive; rounding of the nominal matrix is paid by its full Frobenius
radius before its midpoint becomes the next nominal matrix. No midpoint
has been declared an exact true coefficient.

The nominal position increment uses the exact integral of that same skew
exponential applied to f_mid. The local error is at most

    h*(local_frame_error*|f_mid|+|f-f_mid|),

in addition to the incoming position error. The source uses |f|_upper in
place of |f_mid|, which is a safe larger number. It also pays the complete
rounding radius. Whole-cell times [0,h], not only endpoints, are enclosed.

W supplies the separate actual periodic-frame fee 11/10^7 and position
fee 1/25000. For derivatives use the exact actual equations and the prior
whole X root bounds z=||Z||, z1=||Z_theta||, p=||P||:

    O'=O Omega+s Z,
    O''=O' Omega+O Omega'+s' Z+s^2 Z_theta,
    G'=O f+s P.

Each unknown defect matrix/vector entry is enclosed by its entire norm
bound; no C0 bound is promoted to C1. Thus c' uses an actual paid second
frame derivative. No actual third frame derivative is required. The same
W bounds apply to G_inc independently of q_axis,s_axis because the
position difference equation has zero initial difference and depends
only on the frame and position defect. A nonclosed ideal ODE trajectory
is never asserted to be the actual periodic frame.

## Exact trigonometric cell integrals

For a scalar coefficient C whose complete cell ball has midpoint Cc and
radius r, and any explicitly known scalar wave w, use

    integral C*w in Cc*integral w + [-r,r]*h*sup|w|.

This formula remains valid when w changes sign. Merely multiplying the
coefficient ball by the signed integral of w would be invalid, and is not
used. All sine/cosine integrals are exact directed elementary expressions.
Products of the normalized sine/cosine basis use the sum/difference
identities, paying the complete remainder with sup at most 2. Consequently
oscillation at frequencies 384,388 and their sum is not replaced by
sampling or by an unjustified quadrature rule.

The two response primitives are integrated through complete cell source
integrals. For a cosine source the weighted cell integral is exactly

    integral_a^b (b-t)cos(n t)dt
       =(cos(n a)-cos(n b))/n^2 -(b-a)sin(n a)/n.

The coefficient remainder is bounded by r*h^2/2 times the amplitude. This
gives both the cumulative primitive and its complete circle average.
Subtracting that average yields the original zero-mean I v_i. Complete
within-cell partial integrals and the cumulative error enclose V_i at every
angle. The nonlocal form then uses the same coefficient-times-exact-wave
formula, with the entire V_i enclosure included in the coefficient ball.

All stored private cell and response-prefix values are mid64/rad64 pairs.
Every pair is reconstructed as a directed Arb ball and explicitly checked
to contain its entire original source ball before writing. The cache is
about 27 MB, used only inside this scientific process, and is not saved to
the repository, an Artifact, a Release, or a public array. Later passes
consume those complete enclosing balls. The only public cache data are
byte counts and hashes.

## Saved conclusions and strict scope

The three affine symmetric matrices (constant, axis_q, axis_s), the three
actual signed entries, and the few necessary scalar enclosure records are
written as complete decimal balls. Every record is read back and checked
to contain its entire original ball. The actual matrix is composed from
read-back affine and axis balls; signs are checked only after that actual
matrix has itself been saved and read back.

A strictly negative determinant proves that the true symmetric two-mode
form has a negative direction. An additional exact rational direction is
selected from a finite deterministic list and a midpoint-suggested rational
slope, but its value is always evaluated against the complete saved matrix
and must have a strictly negative upper endpoint. The suggestion is never
the proof. A failed strict comparison is retained as inconclusive.

A proven negative direction excludes only a nonnegative root form on all
original root data, and hence the sufficient unconditional homogeneous-root
coercivity route. It does not prove that such a root trace is attained by a
global homogeneous interior solution, does not prove a kernel or singular
boundary problem, and does not replace the existing true193/high inverse
route. If neither comparison separates, this target reports that fact and
does not claim positivity. No tail positivity or full inverse is asserted.
