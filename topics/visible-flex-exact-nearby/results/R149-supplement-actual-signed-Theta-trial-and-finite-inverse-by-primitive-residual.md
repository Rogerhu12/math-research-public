# R149 ASQ18. The original 96 signed rows, their trial, and the finite inverse

On the original selected member, with the entire original OT trial and UACT dyadic inverse, one has
\[
 \|\Theta-\widehat\Theta\|<.26,\qquad
 \|\Theta E_{96}^a-\widehat\Theta E_{96}^a\|<.025,\qquad
 \|(\Theta E_{96}^a)^{-1}\|<2.694.                         \tag{ASQ18.1}
\]
All three are operator norms. The first is on the whole reflected target including every mode beyond the finite support of the trial. The last two are for the target-to-source real 96-coordinate map. The physical PDE columns and their independent border remain in the original coupled square.

## A low and a primitive residual on the true map

Use the original [WMT.1](R149-supplement-complete-weighted-model-Theta-receiver.md) notation \(R=C^\dagger Y-B,\ Z=(C^\dagger)^{-1}B,\ E=Z-Y,\ G=|\partial_x|^{-1}\), with all 96 trial columns simultaneously. The complete [WMA actual](R149-supplement-actual-complete-weighted-model-Theta-receiver.md) has 12593 bytes, SHA256 **587ec4c28e521c8b04a85d42fad02bd5a53b4468ac9fdf217206ef40f231e3ae**. Its first, second, fifth and sixth whole records give respectively
\[
 \|Y\|_2<386.351,\quad\|Y'\|_2<150107,\quad
 g_{R,1}<1.05\,10^{-8},\quad t_1<.001216 .
\]
Here \(g_{R,1},t_1\) bound the derivative of the full finite-compound residual on frequencies \(1\le n\le2048\) and \(n\ge2049\) respectively. Set \(D_0=4\cdot2049\). Thus its full ordinary residual norm is bounded by \(g_{R,1}/4+t_1/D_0\), and its primitive norm by \(g_{R,1}/16+t_1/D_0^2\). The finite-compound head includes the whole original \(B\).

The actual \(C^\dagger\) is the same-sign compression of \(U_p,\ U_pf=p'(f\circ p)\). Along \(p_t=\widehat p+t\delta,\ \delta=p-\widehat p\), [SDI.2–4](R149-supplement-actual-small-density-inverse-constants-and-Theta-errors.md) gives \(\|\delta\|_\infty<E_p=2.211\,10^{-7},\ \|\delta'\|_\infty<256E_p,\ .9749<p_t'<1.0251\). Differentiating \(U_{p_t}Y\) in \(t\) gives \(\delta'(Y\circ p_t)+p_t'\delta(Y'\circ p_t)\). Changing variables costs at most \(1.013\) in \(L^2\). For its primitive, use \(U_pf=\partial_x[(If)\circ p]\) with the genuine mean removed by \(I\); the lift difference contributes at most \(1.013 E_p\|Y\|_2\), using \(\partial_t[(IY)\circ p_t]=\delta(Y\circ p_t)\). In this last estimate \(G\) and \(I\) differ by a unitary sign on the nonzero angular modes. Each same-sign block is bounded by the corresponding uncompressed operator and both sign inputs and outputs are orthogonal. All bounds therefore apply to the complete joint maps.

[ASQ13](R149-supplement-opposite-density-inverse-on-original-high-frequency-inputs.md) gives \(\|(C^\dagger)^{-1}\|_2<1.12\). The defining energy adjoint satisfies \(G C^\dagger=C^*G\) and [ASQ12](R149-supplement-all-positive-i-safe-modes-in-the-physical-waist-square.md) gives \(\|(C^*)^{-1}\|_2<1.11\). From \(C^\dagger E=-R\) it follows that
\[
 \begin{split}
 \|E\|_2 &<1.12\big[g_{R,1}/4+t_1/D_0+
       1.013 E_p(256\cdot386.351+1.0251\cdot150107)\big]<.064,\\
 \|GE\|_2 &<1.11\big[g_{R,1}/16+t_1/D_0^2+1.013 E_p\,386.351\big]<.000097 .
 \end{split}                                                \tag{ASQ18.2}
\]
The same adjoint identity gives \(GZ=(C^*)^{-1}GB\), where \(GB=D_+E_{96}\) is an isometry. Hence \(\|GY\|_2<1.111\) for all original columns jointly. This estimate uses their true residual, without a new numerical norm evaluation.

## Both original coefficient products supply genuine coefficient budgets

The complete [UACT actual](R149-supplement-actual-original-finite-Theta-coordinate-inverse.md) has 42477 bytes, SHA256 **17c721993bb6488ec48918c50caf70c84785ca54cb004fbc51d11de1c6eb14bc**. Write \(d_\alpha=\alpha-\widehat\alpha\). The [actual accumulator](../scripts/fourfold_codazzi_trial_primitive_operator_norm.py) independently saved its original products 4 and 7, retaining all 2048 head modes, both signs, and both original tail bounds. Specifically product 4 dominates \(J(2\sum_n\Delta_n+T_\infty)\) with the selected *fixed budget* \(J>2.677\) (UACT record 3). Product 7 dominates \((S/3)(2\sum_n\Delta_n^2+T_2^2)^{1/2}\), where its *fixed budget* \(S=(51/50)(\epsilon_0+10\epsilon_H/9)>.6\) by the original whole IR balls. Consequently the directed recorded products give
\[
 \|d_\alpha\|_\infty\le \|d_\alpha\|_{A^0}
    < .929368/2.677<.348,\qquad
 \|d_\alpha\|_2<3(.013047)/.6<.06524.                      \tag{ASQ18.3}
\]
The absolute Fourier tail in the first inequality is established in [ASQ10.3](R149-supplement-practical-high-cut-with-paid-coordinate-errors.md). These are estimates by the arithmetic that defined the two records, valid independently of the actual size of \(GY\) and \(E\). The earlier signed original trial and the original coefficient are identical to those used here.

The joint dual row error has the exact regrouping
\[
 \Delta r=GE+I\mathcal T_\alpha GE+I\mathcal T_{d_\alpha}GY,\qquad
       \mathcal T_f=\Pi_+M_f\Pi_++\Pi_-M_f\Pi_- .
\]
For each fixed output frequency, the coefficient of \(f\,v_\pm\) is at most \(\|f\|_2\|v_\pm\|_2\) by Cauchy–Schwarz. Sum squares with the original \(I\) weight using \((\sum_{n>0}(4n)^{-2})^{1/2}=\pi/(4\sqrt6)<.322\), then combine the two orthogonal input signs. This proves \(\|I\mathcal T_fv\|_2\le.322\|f\|_2\|v\|_2\). In particular
\[
 \begin{split}
 \|\Delta r\|_2&<.000097(1+1.43/4)+.322(.06524)(1.111),\\
 \|\partial_x\Delta r\|_2&<.064+1.43(.000097)+.348(1.111).
 \end{split}                                                 \tag{ASQ18.4}
\]
The derivative on \(I\mathcal T_f\) is the nonmean projection, and \(\|\partial_x GE\|_2=\|E\|_2\). This argument never differentiates a fitted coefficient or removes its true error on the inverse tail.

## Finite and full model application

On the exact \(E_{96}^a\) the normalized real model is isometric. Add the whole UACT low-model radius \(<.001449\) (record 11) to the first line of (ASQ18.4); the result is \(<.025\). With the original trial inverse \(X\), UACT records 15 and 19 give \(\|X\|<2.523,\ \|Id-X\widehat T\|<10^{-15}\). The square is therefore invertible with norm less than \(2.523/[1-10^{-15}-2.523(.025)]<2.694\). In particular the numerically recorded large old global row error is unnecessary in this finite solve.

On every mode \(1\le n\le2^{20}\) the original head weight \(|\gamma_n|/(4n)<.573\) follows from [ASQ14](R149-supplement-original-WMA-head-on-the-true-signed-waist-inverse.md), including its unit low reference. Here the model-applied row difference costs at most .573 times the second line of (ASQ18.4), plus the entire OT model rounding and true-phase radius \(<.001457\) copied by WMA. On \(n>2^{20}\) the original dyadic trial is exactly zero because its complete extent is 2240. [ASQ17.5](R149-supplement-fast-true-Theta-series-and-complete-original-high-row-tail.md) bounds the actual row there by .0000162. The sum of these two whole estimates is \(<.26\), proving (ASQ18.1). This last bound pays the true tail at every higher frequency. It can replace the old global error in the CFC/BFP/DCP receivers multiplying their whole target-norm errors. In the constrained coordinate reconstruction the finite inverse uses 2.694 while all actual signed \(\Theta H_c r\) and the original physical scalar rows still act on the same reconstructed state.
