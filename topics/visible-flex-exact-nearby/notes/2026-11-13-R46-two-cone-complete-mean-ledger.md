# Complete mean ledger for the two-cone normal form

This is an explicit audit of the already frozen complete mean contribution
in R46-supplement-actual-two-cone-density-normal-form-and-base-Rstar.md.
It does not change any of that theorem's three frozen files:

- proof: 94ac567a760c8a742c58764ed89f3e6446b0669d714382ace05d0dc4732eb083;
- producer: c61cd60cb84fce467d86a985576875ca9dcccb7fc0a43538b094250270adc299;
- native: 59635a09f6ae38758cdf226902178b4fdcdf80f336ae1e36a99d06fdf03e149d.

## 1. Original PDE mean versus the purified complete word

The exact root-to-cut operator has the original two-row Airy mean,
$D_\pm=c(1\pm iL/\pi)$ and $D_\pm'=\pm ic/\pi$, and the physical
mean matrix $D_{4,0}=(5,-3;-3,5)/2$.
The earlier strong-word theorem, (F.10)--(F.12), changed only its model
to $2I$ and
$\Phi_{{\rm p},0}=\gamma_0\operatorname{diag}(e^{i\pi/4},e^{-i\pi/4})$.
Its complete finite-mean fee $M_*+4\Phi_*$ was included in $R'_K$,
then in the full scattering error $R_S$.
The new theorem uses that same $R_S$ in (D.8)--(D.14).
Thus the genuine PDE mean has not been replaced for free.

## 2. The purified word still has a nontrivial mean loop

Write $M_R=2\gamma_0(0,p;q,0)$, exactly as in (D.25), and let $e_0=1$.
The actual factors of this model satisfy

$$
B_{\rm original}e_0=0,\quad
W_g e_0=e_0,\quad Q_He_0=e_0,\quad
p e_0=e^{-i\pi/4}e_0,\quad q e_0=e^{i\pi/4}e_0.
$$

Both strict amplitude blocks and their adjoints fix the mean exactly,
because their nonzero parts are compressed on both sides.
Hence, for $U=p^*W_-^*q$ and $V=p^*W_+q$,

$$
\Pi_0U\Pi_0=\Pi_0V\Pi_0=i\Pi_0 .
$$

This does **not** assert $\Pi_0UV\Pi_0=-\Pi_0$. Its exact identity is

$$
\boxed{\Pi_0UV\Pi_0=-\Pi_0+\Pi_0U\Pi_{\ne0}V\Pi_0.}
$$

The second term is the complete mean-to-nonmean-to-mean loop.
It is not assumed zero.

In the original word, only the four physical angle factors
$Q_H,Q_H^*$ can start or end such a mean path:
the graph and strict models, original root phase and fixed-section
Airy multiplier are all block diagonal for the decomposition
$(\Pi_+,\Pi_-,\Pi_0)$.
The first projection step in the proof of (D.24) replaces these four
physical factors by their full three-block diagonals.
After this replacement the mean word is exactly $i\,i=-1$.

Every removed mean row or column has the full gain-two estimate (D.19).
The finite telescoping error of these four replacements is bounded by
$4P e_H$, using the common product $P$ of (D.24).
It is contained in the larger allocated fee $8P\sum_i e_i$.
In particular the entire boxed loop is in the actual complete remainder.
The first scalar model mean is therefore $1-(-1)=2$ with a paid error,
not an assertion about the exact unprojected mean diagonal.

## 3. Circle change and artificial constant-phase extensions

The subsequent two factors $Q_C,Q_C^{-1}$ may also create mean-output
paths from nonzero inputs. Their own mean rows and columns are included
in the two circle-factor fees $e_C$ in (D.24).
They both fix $e_0$ exactly; they are not assumed to preserve the
orthogonal nonzero complement.

The full operator $A(f)=\Lambda^{-1/2}M_f\Lambda^{-1/2}$ is introduced
only inside each externally compressed nonzero-cone word.
The mean block is kept separately at its original model value at every
projection step. For a constant $f$, the artificial value of $A(f)$ on
the mean does not replace that separate block.
If a nonzero-cone path visits the mean while the internal projections
are removed, its entry and exit require a nonconstant map or phase;
those are paid by (D.19) or (D.22). A constant phase is diagonal and
creates no such entry or exit. This is why its own cross and ordering
fees are zero without deleting an actual finite-rank mean-diagonal term.

The first-root mean, the complete second-root block, both independent
regular means, and every cross column remain in the final full-space
remainder and in the exact source/reconstruction formulas (D.39)--(D.40).
