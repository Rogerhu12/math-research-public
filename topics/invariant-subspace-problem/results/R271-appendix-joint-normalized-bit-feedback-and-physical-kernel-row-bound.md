# R271 附录：真实归一二进位联合伴随的核内距离控制与原物理核反馈行

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：下面的联合算子不等式和原物理核反馈行下界已证明。** 全部列使用同一个原头、同一个完整 bosonic 核 Gram 和同一个投影。结论避免单独反解 $B_m$ 的最小权；它没有将原 $W$ 对每个固定列的强收敛升级为移动全行的统一速率。

依赖：[三列硬核角度](R271-appendix-three-collective-columns-hardcore-angle-and-bosonic-wandering.md)、[完整零占据](../notes/2026-11-14-full-boolean-kernel-bosonic-zero-occupation-and-head-only-budget-789f-next.md)及[移动头投影](../notes/2026-11-14-moving-true-head-bosonic-projections-and-inverse-gram-strong-limit-789f-next.md)。原归一权也见[首bit物理 Schur](R271-appendix-first-binary-bit-uniform-physical-schur-and-exact-top-source.md) §1。

## 1. 原归一二进位行的完整物理下界

固定 $m\ge5$，$d=2^m$。原权为
$$
B_m e_n=\alpha_{v_2(n)}e_{n-1},\qquad
W_n=\prod_{\ell=1}^n\alpha_{v_2(\ell)},\qquad
d_i=W_{2^i}.
$$
定义原头算子
$$
N_{i,m}=\frac{B_m^{2^i}}{d_i},\qquad 0\le i<m.
\tag{1.1}
$$
这些是原物理归一幂，不是把高位 carry 删掉后的独立 Boolean 删除。

原权的二进位乘积身份为
$$
W_n=\prod_{\substack{j\ge0\\\text{$n$ 的第 $j$ 位为 $1$}}}d_j.
\tag{1.2}
$$
可由 $W_{2^j-1}=\prod_{\ell<j}d_\ell$ 及区间 $[2^j+1,2^j+r]$ 的低位权与 $[1,r]$ 相同归纳得到。

若 $0\le n<d$ 的第 $i$ 位为零，则 $n+2^i<d$，且 (1.2) 给
$$
N_{i,m}^*e_n
=\frac{W_{n+2^i}}{W_n d_i}e_{n+2^i}
=e_{n+2^i}.
\tag{1.3}
$$
每个 $N_{i,m}N_{i,m}^*$ 在物理头基下为非负对角矩阵。每个 $n<d-1$ 至少有一个零位，而 $n=d-1$ 的全部这些 adjoint 输出为零。因此
$$
\boxed{
\sum_{i=0}^{m-1}N_{i,m}N_{i,m}^*
\ \succeq\
I-|e_{d-1}\rangle\langle e_{d-1}|.
}
\tag{1.4}
$$
所有其余进位贡献只是保留的非负对角项。这里没有以逐项绝对值取代任何非交换 Gram。

## 2. 在同一个完整 bosonic 核内取伴随

取原 $A_m$ 和纯尾 bosonic annihilator，沿用
$$
\mathcal K_m^{\rm B}=\ker(A_m+\sqrt{S_m}a_m),
\qquad P_m^{\rm B}=P_{\mathcal K_m^{\rm B}}.
$$
完整零占据同构 $\mathcal R_m$ 满足
$$
\mathcal R_m^*\mathcal R_m=H_m\otimes I,\qquad
I\le H_m\le C_mI,
\tag{2.1}
$$
$$
H_m=\sum_{j<d}\frac{(A_m^j)^*A_m^j}{S_m^j j!}.
$$
由于 $N_{i,m}$ 与 $A_m$ 对易，
$$
N_{i,m}\mathcal R_m=\mathcal R_mN_{i,m}.
\tag{2.2}
$$
故 $N_{i,m}$ 保持整个 $\mathcal K_m^{\rm B}$。记
$$
\widehat N_{i,m}=N_{i,m}|_{\mathcal K_m^{\rm B}}.
$$
其核内真实伴随准确为
$$
\boxed{
\widehat N_{i,m}^{\,*}\mathcal R_mh
=\mathcal R_mH_m^{-1}N_{i,m}^*H_mh
=P_m^{\rm B}N_{i,m}^*\mathcal R_mh.
}
\tag{2.3}
$$
全部 $H_m$ 因子及其顺序不可省。

令
$$
\mathcal W_m^{\rm B}
=\mathcal K_m^{\rm B}\ominus B_m\mathcal K_m^{\rm B},
\qquad Q_m^{\rm B}=P_{\mathcal W_m^{\rm B}}.
$$
已付精确式为
$$
\mathcal W_m^{\rm B}
=\mathcal R_m\big(H_m^{-1}e_{d-1}\otimes\ker a_m\big).
\tag{2.4}
$$
对任意 $v=\mathcal R_mh$，置 $u=H_mh$ 并以 $P_\perp$ 表示头上
$I-|e_{d-1}\rangle\langle e_{d-1}|$。使用同一个候选
$\mathcal R_mH_m^{-1}(I-P_\perp)u\in\mathcal W_m^{\rm B}$，
$$
\begin{aligned}
\operatorname{dist}(v,\mathcal W_m^{\rm B})^2
&\le\|\mathcal R_mH_m^{-1}P_\perp u\|^2\\
&=\langle P_\perp u,H_m^{-1}P_\perp u\rangle
\le\|P_\perp u\|^2.
\end{aligned}
\tag{2.5}
$$
另一方面，由 (2.3)、$H_m^{-1}\ge C_m^{-1}I$ 和 (1.4)，
$$
\begin{aligned}
\sum_{i<m}\|\widehat N_{i,m}^{\,*}v\|^2
&=\sum_{i<m}
\langle N_{i,m}^*u,H_m^{-1}N_{i,m}^*u\rangle\\
&\ge C_m^{-1}\sum_{i<m}\|N_{i,m}^*u\|^2\\
&\ge C_m^{-1}\|P_\perp u\|^2.
\end{aligned}
\tag{2.6}
$$
合得
$$
\boxed{
\operatorname{dist}(v,\mathcal W_m^{\rm B})^2
\le
C_m\sum_{i<m}\|P_m^{\rm B}N_{i,m}^*v\|^2
\qquad(v\in\mathcal K_m^{\rm B}).
}
\tag{2.7}
$$
等价的核内算子不等式为
$$
\boxed{
\sum_{i<m}\widehat N_{i,m}\widehat N_{i,m}^{\,*}
\succeq C_m^{-1}(I-Q_m^{\rm B}).
}
\tag{2.8}
$$
这不是由各个度量不等式相减得到，而是直接保留完整同源 $H_m$ 后的正平方和。

## 3. 原物理核向量的真实反馈行下界

现在令 $M=\ker T$ 为原全局 N/Y 模型的核，$w\in M$。置
$$
v=P_m^{\rm B}w,\qquad
\epsilon=\|(I-P_m^{\rm B})w\|.
$$
$w$ 在原全硬核空间，因此
$$
\|(I-Q_{\rm hc})v\|\le\epsilon.
\tag{3.1}
$$
三列硬核角度稿给
$$
\|(I-Q_{\rm hc})z\|\ge\vartheta_m\|z\|
\quad(z\in\mathcal W_m^{\rm B}),
$$
$$
\vartheta_m=
\frac{3e^{-1070}}{20(m+4)C_m^{3/2}}\le1.
\tag{3.2}
$$
写 $v=z+y$，其中 $z=Q_m^{\rm B}v$，$y\perp\mathcal W_m^{\rm B}$。由 (3.1)--(3.2)，
$$
\vartheta_m\|z\|
\le\epsilon+\|y\|.
$$
又 $\|z\|\ge\|w\|-\epsilon-\|y\|$，所以
$$
\boxed{
\|y\|\ge
\left(\frac{\vartheta_m}{1+\vartheta_m}\|w\|-\epsilon\right)_+.
}
\tag{3.3}
$$
式中 $(a)_+=\max(a,0)$。

因为 $N_{i,m}$ 保持 $\mathcal K_m^{\rm B}$，
$$
P_m^{\rm B}N_{i,m}^*v
=P_m^{\rm B}N_{i,m}^*w.
\tag{3.4}
$$
把 (3.3)--(3.4) 代入 (2.7)，得到同一实际物理 $w$ 的整行结论
$$
\boxed{
\sum_{i<m}\|P_m^{\rm B}N_{i,m}^*w\|^2
\ge\frac1{C_m}
\left(
\frac{\vartheta_m}{1+\vartheta_m}\|w\|
-\|(I-P_m^{\rm B})w\|
\right)_+^2.
}
\tag{3.5}
$$

已付移动头界为
$$
\epsilon\le\Delta_m\|w\|,
\qquad
\Delta_m=26R_m\eta_{m-1},
$$
$$
R_m\le e^{22m^2},\qquad
\eta_{m-1}\le e^{-80\,16^m},\qquad C_m\le e^{40m^2}.
$$
对全部 $m\ge5$，
$$
\Delta_m\le\frac{\vartheta_m}{4}.
\tag{3.6}
$$
例如只需检查
$$
80\,16^m
\ge1070+82m^2+\log\!\left(\frac{2080(m+4)}3\right).
$$
它在 $m=5$ 已有严格裕量；之后右边的增长小于左边。因
$\vartheta_m/(1+\vartheta_m)\ge\vartheta_m/2$，(3.5) 遂给
$$
\boxed{
\sum_{i<m}\|P_m^{\rm B}N_{i,m}^*w\|^2
\ge
\frac{9e^{-2140}}{6400(m+4)^2C_m^4}\|w\|^2
\qquad(w\in M,\ m\ge5).
}
\tag{3.7}
$$
这条原物理核下界的损失为 $\exp[O(m\log(m+1))]$，不包含单独反解最小二进位权的 $e^{c\,2^{4m}}$ 成本。

## 4. 原 $W$ 的固定列极限和移动全行仍是不同量词

若进一步 $w\in W=M\ominus\overline{BM}$，则对每个固定 $i$，
$$
N_i=\frac{B^{2^i}}{d_i}
$$
保持 $M$ 且 $N_iM\subseteq\overline{BM}$。故
$$
N_i^*w\perp M.
\tag{4.1}
$$
对固定 $i$，原真实 carry 给 $N_{i,m}\to N_i$ 于物理空间的算子范数；这里可从 $B_m\to B$ 的真实全局 carry 及固定次幂差公式直接得到。结合
$P_m^{\rm B}\to P_M$ 强收敛，严格有
$$
\boxed{
P_m^{\rm B}N_{i,m}^*w\longrightarrow0
\qquad(\text{每个固定 }i,\ w\in W).
}
\tag{4.2}
$$

式 (4.2) 没有给 $i<m$ 的移动全行速率，因而不与 (3.7) 矛盾。尤其不能把逐个固定 $i$ 的极限移进一个长度随 $m$ 增加的和，也不能先在该和上除以 (3.7) 的小常数。

因此当前可用的准确入口是：原非零 $w\in W$ 若存在，其 $m$ 个真实归一 bit 反馈列必须共同满足 (3.7)，同时每个固定列满足 (4.2)。接下来的任务是用同一个 $w$、实际核投影及共同返回结构控制该移动行；本文未提供这一统一上界，也未证明 $N=M$。
