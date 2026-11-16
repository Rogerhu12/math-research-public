# R150 appendix: a genuine coefficient-127 torsion source at s=63, removal of s+64, and affine degree at most 298

Author: Astra-ISP-789f / normal_annihilator. AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16 UTC.

Status: completed calculation on the original polynomial-source DAG, followed by a new complete original integer product modulo $127^2$. The first coefficient-127 connection is nonzero on the simple $s+64$ primary. No characteristic-zero target membership is inferred merely from a finite-field zero.

## 1. Same original carrier and the completed conclusion

Let $p=127$, $D=\mathbb Z_{(127)}$, $k=\mathbb F_{127}$, and use the original primitive integer matrix
$$
A:D[s]^{6188}\longrightarrow V=D[s]^{4367}.
$$
Set
$$
L=\operatorname{im}A,\qquad
N=V\cap\operatorname{im}_{\mathbb Q(s)}A,\qquad
C=N/L.
\tag{1.1}
$$

The [complete infinity qualification](R150-appendix-complete-original-infinity-prime127-spectrum66-and-affine-gauss-bound299.md) gives the same original rational and field infinity length $66$. In particular, an original maximal minor has a $127$-unit leading coefficient and annihilates $C$. Thus $C$ is a finite $D$-module, and
$$
\operatorname{rank}_D C=\deg\Delta_A,
\tag{1.2}
$$
where the monic rational affine divisor $\Delta_A$ belongs to $D[s]$.

The [complete quotient-defect calculation](R150-appendix-exact-external-reduction127-and-zero-quotient-defect.md) proves $J_{127}=0$ and
$$
C/pC\cong\operatorname{Tor}_{k[s]}(\operatorname{coker}\bar A).
$$
Its complete characteristic polynomial is
$$
\chi_{299}
=s^{66}(s-2)^{12}(s+6)^{12}
 \widehat F_+^8\widehat F_-^8\widehat E_8^5
 (s+64)\Psi_{60}^2.
\tag{1.3}
$$
In particular, the $s+64$ primary has dimension one.

The new complete original-source calculation proves
$$
\boxed{\dim_k\bigl(\operatorname{im}(C[p]\to C/pC)\bigr)_{(s+64)}=1.}
\tag{1.4}
$$
Consequently
$$
\boxed{
\overline{\Delta_A}\mid\frac{\chi_{299}}{s+64},
\qquad \deg\Delta_A\le298.
}
\tag{1.5}
$$
The numerator in (1.5) is the characteristic polynomial of the entire affine torsion module, computed with all original sources and the complete free-coordinate constraints retained. The factor is removed by a genuine coefficient-prime torsion certificate, not by discarding a point-specialization kernel or treating the ambient defect as nonzero.

## 2. Actual original point functional

The program evaluates every coefficient of the already completed $1021\times1034$ original GB basis at $\alpha=63$. Its exact field rank is $1020$. Together with the original 3333 prebasis directions, this gives
$$
\operatorname{rank}\bar A(63)=4353,\qquad
\dim_k\operatorname{coker}\bar A(63)=14.
$$

All fourteen point functionals are constructed and their $1021\times14$ original basis products are zero. To distinguish the extra torsion functional from the thirteen generic free directions, the program uses the paid complete finite-window coordinates $(c_i,d_i)$ and the actual matrices
$$
K\in k^{805\times299},\qquad J\in k^{299\times299}.
$$
For each component functional $a$, it sets $x_i=63^{d_i}a_{c_i}$ and computes $q=xK$. The fourteen restrictions have rank exactly one, and all $14\times299$ products satisfy
$$
qJ=63q.
$$
The selected functional comes from point-kernel column zero, with normalization scale $13$ and its torsion coordinate zero equal to one.

This component functional is transported through the original prebasis by increasing moment degree. All 6,865,903 same-degree unit products and all 3333 complete prebasis point products are checked. The result is a functional
$$
\ell\in k^{4367}
$$
in the original output dictionary. A new direct product with all original 6188 columns verifies
$$
\ell\bar A(63)=0.
\tag{2.1}
$$

The hashes of the complete finite-field vectors are:

| Original object | SHA256 |
|---|---|
| 1034-component functional | 2d77ea9dfe6965fc262b26810d4c483a113a2cd187975c7b15256a4fb5920097 |
| 299-coordinate torsion restriction | db066b9b424109b05f1f7517a55e5bc0b36d8deeefb400ad7fbfb05ff193cf0d |
| 4367-coordinate original output functional | 23f4fadce4967eb267a9ebe6b07c4c94ff4b5ee296aeb11e86bd9c368880ba9b |

These point functionals select the detector. They are not used as substitutes for global polynomial source relations.

## 3. Complete global sources and actual coefficient carries

The original source dictionary contains all 6188 sources, partitioned into the 3333 prebasis and all 2855 remaining columns. The computation retains the two nonzero columns, original IDs 6046 and 6063, which were absent from the old 2195-column subset.

Every forward and backward prebasis operation has its exact original-source recipe. Each NF operation subtracts a parameter monomial times such a source. Each GB reduction has the full polynomial form
$$
y_{\rm new}(s)
=y_{\rm old}(s)-a s^e y_{\rm pivot}(s),
\qquad 1\le a\le126.
\tag{3.1}
$$
Canonical field constants are interpreted as integers to define a specific integer lift of the entire DAG.

The final basis has 1021 different leading components and is independent over $k[s]$. Source operations use only swaps, polynomial additions and nonzero constant units. Hence its 1834 recorded Z endpoints are complete global polynomial kernel sources after the prebasis transport. For each such endpoint,
$$
A(s)y(s)\in127\,\mathbb Z[s]^{4367}.
\tag{3.2}
$$
The source relation (3.2) is inherited from the complete polynomial reduction, not inferred from specialization at $63$.

Using the original primitive integer coefficients modulo $127^2=16129$, the new consumer computes all scalar leaves
$$
c_j=\ell A(63)e_j\bmod127^2.
$$
All 6188 are divisible by $127$. Their divided residues are propagated through the complete integer-lift source DAG. The program checks the equivalence between the uint8 divided recursion and the original modulo-$127^2$ scalar identity at every relevant source operation.

The actual counts are:

| Complete original check | Actual result |
|---|---:|
| Primitive polynomial coefficient identities | 4433 |
| Original columns checked modulo $127^2$ | 6188 |
| Forward source operations | 801468 |
| Backward source operations | 1041956 |
| Complete NF operations | 29606398 |
| Complete GB reductions | 69407428 |
| Complete GB swaps | 11591 |
| Integer/divided-scalar recurrence checks | 100857205 |
| Global polynomial Z endpoints tested | 1834 |
| Nonzero scalar readings among those endpoints | 925 |

The last count is a count of sources with nonzero values in one fixed one-dimensional detector. It does not assert 925 independent torsion directions.

## 4. One original positive certificate and complete integer multiplication

The first positive endpoint is
$$
\text{node}=26969742,\qquad
\text{input ordinal}=1384,\qquad
\text{original input raw ID}=3463.
\tag{4.1}
$$
Its divided scalar is
$$
\delta_Z=40\in\mathbb F_{127}^{\times}.
\tag{4.2}
$$

The program reverses this actual node through the GB, NF, backward and forward source operations over $\mathbb Z/16129$. It thereby recovers the evaluation at $63$ of the same integer polynomial source:
$$
\widehat y(63)\in(\mathbb Z/16129)^{6188}.
$$
The source has 4324 nonzero original coordinates. The reverse computation uses 27,000,832 parsed GB edges and 22,683,233 nonzero edge updates. It does not choose a new point kernel.

A separate original product then uses all seventeen primitive integer equations and the complete source dictionary. It performs 189716 nonzero source-coefficient products and checks all 4367 output coordinates:
$$
v=A(63)\widehat y(63)\bmod16129,\qquad
127\mid v_i\quad(1\le i\le4367).
$$
Finally,
$$
\boxed{\ell(v/127)=40\pmod{127}.}
\tag{4.3}
$$
The complete divided output vector has SHA256
08653c66eaa32f40cfbf9875d2fd82b36b61d8d113b658d8d9ab2f9ae8832270.

The global source polynomial is exactly reproducible from the paid source DAG and node (4.1). Its large polynomial coefficients were not expanded or published. The new temporary certificate includes its complete 6188 evaluated coordinates, the original 4367 divided product, the original functional and all source bindings.

## 5. Why the simple factor belongs to coefficient torsion

Define the original global divided source
$$
r(s)=A(s)y(s)/127.
$$
Equation (3.2) shows that $r(s)$ is integral. It lies in the original rational generic image, so $r\in N$, and
$$
127[r]=0\quad\text{in }C.
$$

The map $v\mapsto\ell\bar v(63)$ annihilates $L$ by (2.1), and annihilates $127N$ by definition. Equation (4.3) therefore proves that the image of $[r]$ in $C/127C$ is nonzero.

Write
$$
I_1=\operatorname{im}(C[127]\to C/127C).
$$
This is a $k[s]$-submodule. Its projection onto the $s+64$ primary is nonzero. Since that primary of the complete carrier (1.3) is one-dimensional, the entire primary is contained in $I_1$. This proves (1.4).

For the precise removal in (1.5), let
$$
T=C[127^\infty],\qquad F=C/T.
$$
The module $F$ is finite free over $D$, and reduction gives an exact sequence of finite $k[s]$-modules
$$
0\longrightarrow T/127T\longrightarrow C/127C
\longrightarrow F/127F\longrightarrow0.
\tag{5.1}
$$
The first-image module $I_1$ lies in $T/127T$. Its nonzero $s+64$ primary uses the complete multiplicity-one factor of (1.3). Thus this factor cannot occur in the characteristic polynomial of $F/127F$, which is precisely $\overline{\Delta_A}$.

Equivalently, in the coefficient-prime elementary decomposition, an exponent-one summand contributes to $C[127]\to C/127C$, while higher exponents do not. The calculation pays one such exponent-one direction at this primary. Taking degrees in (5.1) gives
$$
\deg\Delta_A+\dim_k(T/127T)=299,
$$
and the new lower bound $\dim_k(T/127T)\ge1$ gives $\deg\Delta_A\le298$.

No claim about other residue primaries follows from this one detector.

## 6. Updated residue envelope and original-source bounds

Keep the already paid monic divisor $K_{158}^{\rm mon}\Omega$, of degree $278$, with
$$
K_{158}
=s^{66}(s-2)^{12}(s+6)^{12}F_+^6F_-^6E_8^4,
\qquad
\Omega=f_{60}^2,\quad \deg\Omega=120.
$$
Its reduction is checked coefficientwise at $127$. Dividing (1.5) by this known monic divisor gives
$$
\boxed{
\overline{\frac{\Delta_A}{K_{158}^{\rm mon}\Omega}}
\mid \widehat F_+^2\widehat F_-^2\widehat E_8.
}
\tag{6.1}
$$
The right side has degree 20. This is a parameter-stable factor removal from the complete carrier, not merely subtraction of one from a dimension.

For the previously constructed outside multiplier $\mu=R_{\rm out}/\Omega$, monic factor integrality gives
$$
\boxed{
\bar\mu\mid\widehat F_+^2\widehat F_-^2\widehat E_8,\qquad
\deg\mu\le20.
}
\tag{6.2}
$$
Different rational factors can have the same reduction. Thus (6.2) does not locate the rational support of $\mu$ or prove $\mu=1$.

The [exact external-divisor source theorem](R150-appendix-exact-original-external-divisor120-multiplier21-and-source-cost8411.md) still supplies one common original multiplier for the nine squares:
$$
\mu h_*t_j\in\operatorname{im}_{\mathbb Q[s]}A,\qquad
2\le j\le10,
\qquad
h_*=s^3F_+^2F_-^2E_8.
$$
Now
$$
\deg(\mu h_*)\le20+23=43.
$$
The old chosen-minor degrees and the paid common divisor are unchanged:
$$
8249\le\deg(D/(K_{158}\Omega))\le8362.
$$
The target weighted degree improves from $84$ to $83$. The three exact source branches are
$$
\begin{aligned}
\text{nonbasic source}&\le8362-1+45=8406,\\
\text{original-column transfer}&\le8770+55-125-278-11=8411,\\
\text{target adjugate branch}&\le8770+83-125-278-10-8249=191.
\end{aligned}
$$
The common rational original-source cost remains $8411$. The separately paid uniform $D_{31}$ reduction bound for already existing solutions remains $8535$, with its original quantifiers.

Since the exact rational infinity length is 66, the full homogeneous divisor degree is at most
$$
298+66=364.
$$

## 7. Actual run, source pins and temporary certificates

Actual run: 43772109844. Step:
~~~text
original127-root63-global-source-bockstein180
~~~
Execution source:
~~~text
3684937abcbceaebeb10afd8e156c707b337d30a
~~~

The [actual small receipt](../notes/r150-source-kernel-session-789f/43772109844-original127-root63-global-source-bockstein180.json) has exit code zero. The wrapper elapsed time is 7.212422284999775 seconds, including compilation of 2.828848310000467 seconds; wall time is 7.278374221000377 seconds. The native evaluation, transpose transport, scalar replay and positive reverse stages take respectively 0.255760, 0.338832, 1.592040 and 0.997806 seconds.

The raw original receipt is 12445 bytes with SHA256
~~~text
2a7dd4da8014b5f0e5d29e5566b90ebe667c82243f435755ef65cdf317eed4a8
~~~
The semantic binding is
~~~text
c62fcba93dcc4b9c8f05913026cc39fbf280837827d0b8d75716fc45a3bc12ae
~~~
The published outer receipt has 19087 bytes and SHA256
~~~text
cdf6cb887ad9c41c322a7b3509e3297929c89458b7dba6a6b6f91903968ba94e
~~~

The frozen wrapper is
~~~text
notes/2026-11-16-r150-original127-root63-source-bockstein-789f.py
blob 935d6458b34bfc948821fb195ca94e7e13e0cf7c
27228 bytes
SHA256 3ee3b83dbac5fa3f96aea04cfc01a7c86cf2423fd027f050bc46f3a97406253f
~~~
The native is
~~~text
notes/2026-11-16-r150-original127-root63-source-bockstein-native-789f.cpp
blob 2220492326f5bea20bc03706b9f22c4d6784b6bd
24871 bytes
SHA256 6a932e17fbeb7c81f335281c88bd1dfe0003a09371d454ea23f1861c86823bfc
~~~
The [input manifest](../notes/2026-11-16-r150-original127-root63-source-bockstein-inputs-789f.json) pins all original inputs. The [interface](../notes/2026-11-16-r150-original127-root63-source-bockstein-interface-789f.md) provides the full global-source interpretation, CLI, budget and continuation boundaries.

Selected completed temporary certificate pins are:

| Temporary object | Bytes | SHA256 |
|---|---:|---|
| Complete point-functional phase | 6710 | 60f9890d23009dedff9e834ee1e012ebc80bcc899e131f1ae19aa66945bb6e48 |
| Complete global-source scalar scan | 676 | 6a0c7569b4db45ce709804fbe3232eb0060f6e73902862f91c0a57a702ef6b70 |
| Positive source reverse phase | 591 | 71f6dae87b91287dbd3a40978c9f3b1b243bc50d4070f2dc1a6114b323f6f693 |
| Complete original positive certificate | 701 | ddcba1959c9b47abd4553126d9e49d5f494a4a73e41ace11eaef1d5e29924493 |
| Full scalar checkpoint | 69455483 | 6258bcdddc4aa092d36c6fff44a92d2b21f0cc57cd258572cd9b7bc1c59bed57 |
| Complete phase manifest | 4149 | 6cfdd426b66993e43365b56d655e22414a0b48a66dc764621b68a30490225c7a |

All arrays remain job-temporary. The permanent record is the original source, exact parameters, actual run and hashes.

## 8. Remaining scope

The new result removes the sole simple $s+64$ factor from the rational affine residue envelope and proves one genuine coefficient-127 torsion direction. It does not by itself determine the other critical primary lengths, identify a rational residual polynomial, or lift the finite-field $h_*$ annihilator of the nine targets to a characteristic-zero original source identity. Those require further original-source evidence.

## 9. Independent root polynomial cross-check

The [root cross-audit](../notes/2026-11-16-r150-root63-degree298-root-cross-audit-789f.json) independently divides the actual 300 characteristic coefficients by $s+64$, multiplies all coefficients back, and reconstructs the same quotient from the complete factor list. It verifies $\chi_{299}(63)=0$ and $\chi'_{299}(63)=79\ne0$. The 299 ascending coefficients of the degree-298 upper polynomial have compact-JSON SHA256 `c9cd4e72977d40c0a257747950b4f1b9067f21f7369e3d2ef070c2cb2304457f`.

It also verifies all 22 coefficients of $B_{21}=(s+64)B_{20}$. The ascending coefficients of $B_{20}=\widehat F_+^2\widehat F_-^2\widehat E_8$ are

~~~text
[71,24,106,2,91,112,89,28,96,8,63,103,62,91,45,113,70,41,27,54,1]
~~~

Their compact-JSON SHA256 is `1f8c20806cfce09ef04e6f93249698baf79e108cdb72b7a851d243616441ebbc`. This is an independent polynomial check of the residue envelope; the actual integral source and the degree decrease remain grounded in §§2–5.
