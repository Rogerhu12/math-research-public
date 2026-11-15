# R133 supplement: actual genuine radial columns and the complete old-circle inverse

2026-11-15, visible-exact / phase_inverse.

**Actual public computation completed.** Run
[43688459733/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43688459733)
returned scientific exit code 0 and passed all 16 gates. It pays the scalar
constants for both genuine radial reference columns and the complete
complex old-circle inverse matrix on the whole original physical root piece.
It does not select the actual positive boundary condition or prove the
full high-frequency boundary inverse.

The analytic statements consumed are
[the genuine two-column reference and two physical sources](R133-supplement-genuine-common-radial-reference-columns-and-two-source-ports.md)
and
[the complete old-circle determinant, derivatives and Wiener conversion](R133-supplement-complete-old-circle-gap-for-genuine-common-reference-columns.md).
The potential is the complete one from
[the actual common radial potential](R133-supplement-actual-complete-common-radial-potential-and-root-piece-image.md).
Every decimal inequality below is rounded outward from the saved actual
directed ball. No new numerical enclosure was computed while writing this report.

## 1. Actual process and immutable inputs

The exact runnable source is
[scripts/fourfold_codazzi_common_reference_columns_old_circle.py](../scripts/fourfold_codazzi_common_reference_columns_old_circle.py).
Its command is

~~~text
python -u scripts/fourfold_codazzi_common_reference_columns_old_circle.py \
  --repo IMMUTABLE_REPOSITORY \
  --manifest MANIFEST \
  --manifest-sha 1869212f28702ae915787a6b5189406b13e6824b93e436a8650fa83e86b11f99 \
  --out-dir TEMPORARY_OUTPUT
~~~

The public wrapper supplied the topic-qualified source and manifest paths.
The exact input manifest is
[2026-11-15-R133-common-reference-columns-old-circle-CI-inputs.json](../notes/2026-11-15-R133-common-reference-columns-old-circle-CI-inputs.json).
It contains nine immutable input files. The actual routing was four current
text inputs, two current files identical to their original legacy bytes,
and three exact historical blobs. Historical recovery used public commit
a3d84d905ce72e3a854874bbe98d119623f3f8de, only inside the temporary scientific tree.

The actual runtime was Python 3.12.14, python-flint 0.9.0, NumPy 2.3.5,
SciPy 1.17.0 and 320-bit Arb. Both Python files in the immutable closure
passed AST parsing before the mathematical subprocess.

| Identity | SHA256 |
| --- | --- |
| New scalar source | 9596ebee08e95939cf1b8a9d46a9f32053bd4706cc77e2263a80d09ede99294c |
| Input manifest | 1869212f28702ae915787a6b5189406b13e6824b93e436a8650fa83e86b11f99 |
| Public worker | 8f8a81a7364b80bc75331303015da745f8d71e7d5930d76f3e83c375def24352 |
| Nine verified input receipts | b0a1706eac780925333f07e19a64da137dbd73e20f48611ac8f3bee0d542c5d7 |
| Complete immutable Python AST inventory | ff1e858860cf883b6cdfdd11af60b8a9647ce678249a8744806b96c35a89eae4 |
| Original successful potential execution | d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9 |

The original full fold stage retains its own accepted source, helper,
manifest, runtime and payload identities. It was not relabelled as a new
stage. The potential value and its first two T derivatives were read from
the complete original successful execution, without re-evaluation.

The mathematical subprocess took 0.004610519999999951 seconds; its parent's
measured wall time was 0.4145359369999966 seconds. There was one new scalar
subprocess. Old target evaluations, FFTs, intrinsic derivatives, phase
coefficients, accepted Fourier norms, potential enclosures and fold
majorants were all recomputed **zero** times. No reference column samples
were computed: the run evaluates the new complete Volterra and matrix
bounds proved in the two cited analytic contracts.

## 2. Both genuine columns on the whole real reference interval

The family is the same explicit repaired family, with fixed original
intrinsic parameter $\eta_0$, the complete allowed complex $\delta$ box,
all $|j|\ge97$ and both carrier signs. Set
$$
 n=4|j|\ge388,\qquad \lambda=n^{2/3},\qquad
 L=\frac1{2000},\qquad M=276 .
$$
The actual common potential disk contains $|T|\le L$, and its full modulus
is less than M. The newly proved column bounds apply on the **real**
interval $[-L,L]$, with the complex family parameters retained.

Let f be the true potential solution whose two data at $T=L$ equal the
free Ai data, and let g be the true solution whose two root data equal the
free Bi data. If the root coefficient of f in the free Ai direction is a,
put $\widehat f=f/a$. The actual root normalization is nonzero.

| Complete quantity | Actual directed consequence |
| --- | --- |
| Minimum $\lambda$ | $>53.19708277$ |
| Positive Volterra exponent | $<0.020753018$ |
| Negative Volterra exponent | $<0.065197528$ |
| $|a-1|$ | $<0.010594103$ |
| $|a|$ | $>0.9894058972$ |
| Positive $\widehat f$ height and derivative factor in its free Ai weights | $<1.031902$ |
| Positive g height and derivative factor in its free Bi weights | $<1.020970$ |
| Negative relative basis and its inverse | $<1.104867$ |
| Negative complete relative propagator and its inverse | $<1.067370$ |

The two-column matrix and its root relative matrix retain the exact identities
$$
 \Psi_n(T)=
 \begin{pmatrix}\widehat f_n(T)&g_n(T)\\
                 \widehat f_{n,T}(T)&g_{n,T}(T)\end{pmatrix},
 \qquad
 \det\Psi_n=\frac{n^{2/3}}{\pi},
$$
$$
 F_n(0)^{-1}\Psi_n(0)=
 \begin{pmatrix}1&0\\ \beta_n&1\end{pmatrix},\qquad
 |\beta_n|<99.415677\,n^{-4/3}<0.035131 .
$$
The displayed shear is retained. It is not replaced by zero or silently
absorbed into a previously chosen root phase.

The positive bounds are weighted bounds for **two** independent columns.
The growing column has not been discarded. The terminal Ai data define a
useful reference basis; they are not the actual positive-region boundary
row. The physical boundary row and all its head, mean and source inputs
must still be applied to this basis.

The two-source transformation remains exactly that of the cited common
reference: ordinary $g_2$ is not differentiated radially, the $A_j\sim n$
factor in the other row is kept, and the measure is $dT=\kappa\,dr$.
The original physical $j=0$ mean is not a $z=0$ or $j\to\infty$ substitute.

## 3. The entire original root piece fits the old-circle product

The actual old radial product is
$$
 |\rho|\le\frac1{20000},\qquad |\operatorname{Im}\phi|\le\frac1{64}.
$$
It comes from the original fold majorants on radius $3/8000$ and strip
$3/128$. The exact worst root-bracket cover of the whole original physical
piece2549 is
$$
 h_*=\frac{893368603925465506687}
           {21990232555520000000000000}<\frac1{20000}.
$$
Both uncertain-root sides are included. The auxiliary analytic extension
is identified with the physical family on that original piece only;
neighbouring physical cubics have not been replaced by this extension.

The actual image and potential disk give
$$
 |T(\rho,\phi)|<0.000231998
 <\frac1{2000}
 <0.0007429560501680
 <\text{the certified common-potential image radius}.
$$
For complex $\phi$, this certifies the domain of the potential and the
old-circle matrix. The real-axis column estimate in Section 2 is not
thereby promoted to a uniform complex-angle column norm.

The rescaled $T_\phi$ majorant uses its previously proved quadratic
radial zero. It does not scale down a generic supremum bound without a
vanishing-order identity.

## 4. Full determinant, ordered derivatives and Wiener conversion

Write
$$
 x=X_\phi,\quad y=T_\phi,\quad
 B_+=x^2+Ty^2,\quad
 H_j^V=i\epsilon x\,I+
 \begin{pmatrix}0&y(T-V_j/n^2)\\y&0\end{pmatrix},
 \quad B_j=(H_j^V)^{-1}.
$$
The complete Bplus factor is used throughout. The leading-height Bminus
is a different expression and is not substituted for this determinant.

The actual full complex product gives
$$
 |B_+|>0.9999880505123,\qquad
 |\det H_j^V|>0.9999880505123,\qquad
 \left|\frac{y^2V_j}{n^2B_+}\right|
     <3.897059143547\,10^{-20}.
$$
These gates include every $|j|\ge97$ and both signs, rather than a finite
sample of input labels. The adjugate and ordered rank-one inverse formulas
are separately valid bounds for the same matrix.

On the strip $1/64$, the complete matrix derivative suprema satisfy

| Quantity | Order 0 | First angular derivative | Second angular derivative |
| --- | ---: | ---: | ---: |
| $H_j^V$ | $<1.000005980$ | $<0.000765356$ | $<0.195931117$ |
| $B_j$ | $<1.000017930$ | $<0.000765384$ | $<0.195939315$ |

The composed potential derivatives retain both chain-rule terms:
$V_{j,\phi}=V_{j,T}y$ and
$V_{j,\phi\phi}=V_{j,TT}y^2+V_{j,T}y_\phi$.
The actual respective bounds are
$$
 |V_j|\le275.19610691070556640625,\quad
 |V_{j,\phi}|<0.000122035,\quad
 |V_{j,\phi\phi}|<0.015620413 .
$$
No scalar commutation was inserted into the ordered inverse derivative
$B_{\phi\phi}=2BH_\phi BH_\phi B-BH_{\phi\phi}B$.

For the complete Wiener algebra on the narrower strip $1/128$, the actual
two-signed-frequency conversion factor, including the zero output, is
less than 64.005209. The exact constant matrix $-i\epsilon I$ is subtracted
before converting the remaining zeroth-order matrix. Consequently
$$
 \boxed{\quad
 \|B_j\|_{\mathcal A_{1/128}}<1.000382716,\qquad
 \|B_{j,\phi}\|_{\mathcal A_{1/128}}<0.048988522,\qquad
 \|B_{j,\phi\phi}\|_{\mathcal A_{1/128}}<12.541136604 .
 \quad}
$$
Only the two stated angular derivatives have been paid. This does not
assign an infinite symbol expansion or extra derivatives for free.

The exact old-circle primitive, every nonmean projection, the full
operator J in its already certified parity and function space, and the
independent even mean remain as in
[the complete primitive/mean interface](R133-supplement-common-radial-reference-old-circle-primitive-and-mean-interface.md).
Physical reference seams retain their full two-row matching and any
distributional primitive or radial-source jump. There is no new jump
at an artificial cut inside the same original analytic piece.

## 5. Actual receipts, publication and the next mathematical gap

The complete small actual conclusions are in
[actual-result.md](../notes/common_reference_columns_old_circle_ci/run-43688459733-1/actual-result.md)
and the genuine process is
[execution.json](../notes/common_reference_columns_old_circle_ci/run-43688459733-1/execution.json).

| Receipt | Bytes | SHA256 |
| --- | ---: | --- |
| Actual result | 8437 | 1d619b1a5edd7baacbc6df6c8d8909c20fe3d377afaaca4ab667f83a972109eb |
| Execution | 16120 | fabe59eed2174e92352f71b8a0e9d80ce8c127580806f5dab917345b05337f57 |
| Temporary scalar process, hash only | 8593 | 1d900a3b9e8ff9031bde33106205be7c66903cde5b960db614ea1b76106f1008 |
| Temporary native, hash only | 3570 | 4d7f5654ae7bab79640fdd0e2596a66a706e89b02eb340796ed3b68c5269701e |

The workflow event commit was
6a4d4b5f361e9c855d6dffd73032e73850254ede. Its actual scientific checkout
was e4544af41ac8076402ec2eb82d7a448e58bbcc24. Two real pulls at
2026-11-15 07:07:17.936647 UTC and 07:07:23.486571 UTC both checked the
root and topic READMEs; both recorded empty diffs.
The reviewed rule receipt SHA is
f2661bd5cf5cb006c1f78c64126b3ac065e6bc26a50790545ac443efb5e372bd.

No new reproducible data were retained in Git, Releases or an Actions
artifact. Only the scripts, exact parameters and small necessary actual
conclusions/process were published.

The newly paid matrix inverse does not by itself bound the genuine
reference columns after complex-angle composition. The full nonradial
trial residual must use the original primitive, J, projections and mean;
the complete radial two-state reference is not automatically the Fourier
diagonal of a nonlinear scalarized inverse. The genuine positive
boundary/Poisson row, all physical seams, the strong return remainder and
the full low/high coupled inverse remain separate obligations.
