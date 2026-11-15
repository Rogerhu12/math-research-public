# R150 补篇：$s=2$ 纯三次正常高核的唯一性及真实一阶首项未增

日期：2026-11-15。作者：Astra-ISP-789f / literature_audit；AI 辅助：GPT-6 Astra Pro。

## 1. 同一原来源中的三次校正

沿用[十五条真实一阶左 jet](R150-appendix-two-directed-fifteen-first-left-heads-and-zero-original-square-readings.md)的全部 $6188$ 原来源、$4367$ 原目标和真实 $s=2+t$ 共动坐标。常数方程的正常部分写为
$$
F_e(c,d,z)=\ell_e(z)+c\,r_e(z)+d\,q_e(z)+Q_e(z),
\qquad 1\le e\le17,
\tag{1.1}
$$
其中 $z=(n_2,\ldots,n_{10})$，$\ell_e,r_e,q_e$ 为线性式，$Q_e$ 为二次式。因为 $g(2)=0$，此处没有纯 $c,d$ 项。式 (1.1) 是原式的正常次数分解，不是在参数邻域删去非零的 $g'(2)t$ 项；求 jet 时仍保留全部真实参数系数。

令 $\mathcal L$ 为十七个 $\ell_e$ 的 $17\times9$ 系数矩阵。原线性秩定理和本次原乘回给
$$
\operatorname{rank}\mathcal L=8,\qquad
\ker\mathcal L=\mathbb Q w.
\tag{1.2}
$$
定义一个只读纯正常三次项的泛函 $\nu$：
$$
\nu(n_i n_j n_k)=w_iw_jw_k,
$$
并令它在所有带 $c,d$ 或不同正常次数的坐标上为零。这里下标 $i,j,k$ 运行于九个正常变量。

对每个允许的正常二次来源乘子 $n_i n_j$，
$$
\nu(n_i n_jF_e)=w_iw_j\,\ell_e(w)=0.
$$
再乘 $c$ 或 $d$ 后仍为零，因为 $\nu$ 不读切向因子。正常三次来源乘子与 $F_e$ 的乘积至少含四个正常变量，也被 $\nu$ 杀掉。因此 $\nu$ 在全部 $2295+2805=5100$ 个高来源行上为零；其作用只留在原 $1088$ 个低来源行，记为 $C_{\rm cub}$。

## 2. 纯三次切片恰为一维

设 $\eta$ 是任意只支撑在无 $c,d$ 的正常三次目标上的泛函，并在全部高来源行上为零。记
$$
T_{ijk}=\eta(n_i n_j n_k).
$$
对每个固定的 $i,j$，正常二次来源行给
$$
\mathcal L\,(T_{ijk})_k=0.
$$
由 (1.2)，存在 $a_{ij}$ 使 $T_{ijk}=a_{ij}w_k$。选择 $w_{k_0}\ne0$，再用 $T$ 的全部对称性，可逐指标得到
$$
T_{ijk}=\kappa w_iw_jw_k
$$
对某个 $\kappa\in\mathbb Q$ 成立。所以
$$
\boxed{\text{无切向因子的纯正常三次高核}=\mathbb Q\nu.}
\tag{2.1}
$$
这不是对允许 $c,d$ 因子或正常次数四、五的完整高核的维数断言。

记旧低校正矩阵为 $B\in\mathbb Q^{1088\times585}$，旧首项强迫为 $C\in\mathbb Q^{1088\times22}$。$C_{\rm cub}\notin\operatorname{im}B$：否则用某个低校正减去 $\nu$ 会得到含非零三次部分的完整常数左核，而已付的全部二十二维常数左核都支撑在正常次数至多一。这也说明新列是合法的实质新增校正，不是旧低校正的重命名。

## 3. 实际新增一列的完整结果

本次只新增求解 $C_{\rm cub}$ 对原 $583$ 阶单位块的一个真实右端。旧二十二个右端、其单位解和完整 $1088$ 行 Schur 全部按原输入身份继承；没有重新作旧常数 RREF 或重复旧右端求解。

对原列次序 $[B,C,C_{\rm cub}]$，实际结果为
$$
\boxed{
\operatorname{rank}[B,C,C_{\rm cub}]=591,\qquad
\dim\ker[B,C,C_{\rm cub}]=17.}
\tag{3.1}
$$
相对于 $B$ 的完整 Schur 秩为八。向二十二个首项参数的投影仍准确为十五维，且等于旧首项空间；没有新增首项。

由于 $C_{\rm cub}\notin\operatorname{im}B$，零首项纤维仍恰为旧 $\ker B$ 的二维。因此
$$
17-2=15
$$
与实际首项投影的秩一致。甚至每个相容一阶 jet 的纯三次系数都必须为零：若某个旧首项有非零该系数，与其旧低支撑代表相减会给出具有非零三次部分的完整常数左核，矛盾。

十五条真实代表仍通过全部 $185640=2\cdot6188\cdot15$ 个原坐标核验，九个平方的 $9\times15$ 读数仍全零。故本次排完了 (2.1) 这整个纯三次切片；它没有支付完整一阶或第二连接，也没有证明原 $h_0$ 目标局部成员性。

## 4. 下一条切向耦合三次列的精确来源

已有两条常数一次正常泛函中的第二条只支撑在 $z,c z,d z$。在选定 $w$ 后可写为
$$
\lambda(z_i)=v_i,\qquad
\lambda(cz_i)=a w_i,\qquad
\lambda(dz_i)=b w_i.
\tag{4.1}
$$
这是原已付常数核的真实支撑：对原常数核乘子 $c,d$ 的方程分别给出 $\mathcal L\lambda(cz)=\mathcal L\lambda(dz)=0$，再用 (1.2) 即得这种比例。因为它独立于纯 $w$ 泛函，$a,b$ 不会同时为零。未乘子的十七式给
$$
\ell_e(v)+a\,r_e(w)+b\,q_e(w)=0
\quad(1\le e\le17).
\tag{4.2}
$$

据此定义另一个真实三次高核泛函 $\widetilde\nu$：
$$
\widetilde\nu(n_i n_j n_k)
=v_iw_jw_k+w_iv_jw_k+w_iw_jv_k,
$$
$$
\widetilde\nu(cn_i n_j n_k)=a w_iw_jw_k,\qquad
\widetilde\nu(dn_i n_j n_k)=b w_iw_jw_k,
\tag{4.3}
$$
其余坐标为零。对无切向因子的正常二次来源行，原乘积准确等于
$$
w_iw_j\bigl[\ell_e(v)+a r_e(w)+b q_e(w)\bigr]
+(v_iw_j+w_iv_j)\ell_e(w)=0.
$$
对带 $c$ 或 $d$ 的正常二次来源行则分别为 $a w_iw_j\ell_e(w)$ 或 $b w_iw_j\ell_e(w)$，也为零。正常三次来源行仍由 $F_e$ 没有纯项而全零。因此 (4.3) 是全部 $5100$ 高行的合法齐次校正，且因其非零切向部分而独立于 $\nu$。

这提供了另一个确定的原低列，可沿相同单位块只新增一个右端。是否扩大首项空间或产生非零目标读数，须由该新增列的实际完整低行 Schur 决定。本篇没有预填其数值结果，也没有称这两个列穷尽全部含切向因子的三次高核。

## 5. 实际证据

实际运行：run $43736746064$，步骤 `two-one-weak-cubic-first-jet-extension`；执行来源 `596dfe6321c7c1296efae70c10d9de2d9bf10723`。数学时间 $12.338020447$ 秒，退出码零。

- [实际小回执](../notes/r150-local-projection-session-789f/43736746064-two-one-weak-cubic-first-jet-extension.json)完整保留父子输入绑定、原乘回与各临时阶段身份。
- 实际源码为 `notes/2026-11-15-r150-two-one-weak-cubic-first-jet-extension-789f.py`，SHA256：`b529d51efeb7195f3783576035f7c5e32e9a94a3bb1f8c44582177ba9dc51843`。
- 原始数学回执 $15796$ 字节，SHA256：`ec321dbfff578676c8ca8ecb7b83ce15cc5fbf10b2854fe9cd6fbea5aeb43de4`。
- 唯一纯三次列逻辑 SHA256：`e1dd76784833bdd14ce91fc72d740633038a6578e0b17df4036297cde966251e`。
- 完整 $608\times17$ 核逻辑 SHA256：`fa2a33c180477bbedc444c21e6725a93b222498610e4f5d0956089f3033b0b82`。
- 九平方零读数逻辑 SHA256 仍为 `9985902de39ff67fb9a99762640bef9e7ec0b18ce2e567c211f8e7aee6e1f76b`。

第 4 节只使用[原 $s=2$ 常数秩证书](../notes/2026-11-14-rank-one-physical-mean-two-rank-certificate-receipt.json)中的真实第二核支撑及原式恒等式，没有新增数值运行。所有可重算大数组仅留在同一临时任务中。
