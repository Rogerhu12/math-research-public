# R271 附录：占据交换子、已知立方尾源的最小能量与连续出生桥

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_1cf；AI 辅助：GPT-6 Astra Pro。
状态：已证明。根已核全部交换子、实际像域、Chebyshev 常数及连续桥投影。

本文给出一个不依赖孔数的准确最小能量界：连续 $D_3^k$ 源在 $D^k$ 或完整 $L^k$ 下有一个有界的最小原像组合。它不是 $D_3^k$ 的右逆界。最后把该界接到旧正交出生层，精确消去连续桥中的固定层逆；实际两桥之间的 Schur 逆仍不能省略。

## 1. 对象与去重范围

使用两个实际边界的同一有限子集尾模型，真空为无孔向量。在固定头 $m$ 下置
$$
D=\sum_{j\ge m}b_jE_j,\qquad
C=D_3=\sum_{j\ge m}b_j^3E_j,\qquad
W_2=\sum_{j\ge m}b_j^2n_j,\qquad
S_m=\sum_{j\ge m}b_j^2,
\quad b_j=(j+1)^{-2}.
$$
这里 $n_j=E_j^*E_j$。所有级数均按算子范数收敛，且
$$
0\le W_2\le S_m I,\qquad
S_m\le\frac1{3m^3}.
\tag{1.1}
$$
同位矩阵计算给
$$
[D,W_2]=C,\qquad [D,C]=0.
\tag{1.2}
$$
完整纯边界 $L=A_m+D$ 也满足
$$
[L,W_2]=C,\qquad [L,C]=0,
\tag{1.3}
$$
因为有限头 $A_m$ 与这些纯尾算子交换。

旧 [环境联合能量稿](R239-appendix-all-hole-environment-energy-gap-and-actual-tail-stability.md) 已使用 $W_2$ 隔离单个位；本文不重新登记其环境下界。旧 [出生层笔记](../notes/2026-11-13-low-kernel-birth-layer-double-schur-bridge-1cf.md) 给 $D^*$ 的两带结构与带 $J_h$ 的第二下降式。新增的是下面的实际最小原像公式、孔数一致的能量界，以及连续桥消逆后的原 Hilbert 范数估计。

## 2. Moore--Penrose 逆只放在实际像域上

本节 $Q$ 可取 $D$ 或 $L$。记
$$
\mathcal E_s(Q)=\ker Q^s,\qquad
\mathcal U_s(Q)=\mathcal E_s(Q)\ominus\mathcal E_{s-1}(Q),
\qquad \mathcal E_0(Q)=0.
$$
对 $k\ge1$ 考察有界算子
$$
Q^k:\mathcal E_{k+1}(Q)\longrightarrow\ker Q.
$$
其核为 $\mathcal E_k(Q)$。令 $\mathfrak R_k^Q$ 表示该算子在实际像
$$
\operatorname{Dom}\mathfrak R_k^Q
=\operatorname{Ran}\bigl(Q^k|_{\mathcal E_{k+1}(Q)}\bigr)
\tag{2.1}
$$
上的最小范数逆：输出属于 $\mathcal U_{k+1}(Q)$。不把 (2.1) 偷换成整个 $\ker Q$，也不假设该像闭。

这确实是闭逆：若 $h_\nu\to h$、$\mathfrak R_k^Qh_\nu\to u$，则闭子空间条件给 $u\in\mathcal U_{k+1}(Q)$，而 $Q^ku=h$；因此 $h$ 属于 (2.1)，且 $u=\mathfrak R_k^Qh$。

**定理 2.1。** 对每个 $f\in\ker Q$，
$$
C^kf\in\operatorname{Dom}\mathfrak R_k^Q
$$
并且
$$
\boxed{
\mathfrak R_k^Q C^k f
=\frac1{k!}P_{\mathcal U_{k+1}(Q)}W_2^k f.
}
\tag{2.2}
$$
这个在全部 $\ker Q$ 上定义的组合有界，而且
$$
\boxed{
\|\mathfrak R_k^Q C^k f\|
\le \frac{2}{k!}\left(\frac{S_m}{4}\right)^k\|f\|
\le\frac{2}{k!(12m^3)^k}\|f\|.
}
\tag{2.3}
$$
所以相应的真正最小能量满足
$$
\boxed{
\inf_{\substack{u\in\ker Q^{k+1}\\Q^ku=C^kf}}\|u\|^2
\le\frac{4}{(k!)^2}\left(\frac{S_m}{4}\right)^{2k}\|f\|^2.
}
\tag{2.4}
$$

### 证明

写 $\delta(X)=[Q,X]$。由 (1.2) 或 (1.3)，
$$
\delta(W_2)=C,\qquad \delta(C)=0.
$$
Leibniz 规则给
$$
\delta^k(W_2^k)=k!C^k,\qquad
\delta^{k+1}(W_2^k)=0.
\tag{2.5}
$$
第一式中，非零项必须恰好在每一个 $W_2$ 因子上作用一次。故所有因子最后都是 $C$；这里完全不要求 $W_2$ 与 $C$ 交换。

一般的有限展开式
$$
Q^nX=\sum_{r=0}^n\binom nr\delta^r(X)Q^{n-r}
\tag{2.6}
$$
由归纳得到。对 $Qf=0$ 使用它，(2.5) 给
$$
Q^kW_2^kf=k!C^kf,\qquad
Q^{k+1}W_2^kf=0.
\tag{2.7}
$$
因此已知源确在实际像域中；把 $W_2^kf/k!$ 减去其在 $\ker Q^k$ 上的正交投影，恰得唯一最小原像 (2.2)。

还可用低阶多项式改善范数。对每个 $\ell<k$，
$$
W_2^\ell f\in\ker Q^{\ell+1}\subset\ker Q^k,
$$
所以 (2.2) 中可把 $W_2^k$ 换成任意首一 $k$ 次多项式 $p_k(W_2)$。

令 $T_k$ 为第一类 Chebyshev 多项式，按 $T_k(\cos\theta)=\cos(k\theta)$ 定义。其递推式
$T_{k+1}(x)=2xT_k(x)-T_{k-1}(x)$ 给 $k\ge1$ 时首项系数 $2^{k-1}$。因此
$$
p_k(x)=2\left(\frac{S_m}{4}\right)^k
T_k\!\left(\frac{2x}{S_m}-1\right)
\tag{2.8}
$$
为首一多项式，且在 $[0,S_m]$ 上绝对值至多 $2(S_m/4)^k$。
由 $W_2$ 自伴及 (1.1)，
$$
\|p_k(W_2)\|\le2(S_m/4)^k.
$$
结合正交投影的收缩性即得 (2.3) 和 (2.4)。证毕。

### 固定孔层与全直和

对 $Q=D$，若 $f\in\ker D\cap\mathcal H_p$，则 $C^kf$ 在第 $p-k$ 孔层，(2.2) 的最小原像仍在第 $p$ 孔层。$W_2$ 保孔数，所有 $\ker D^s$ 的正交投影也保孔数。故 (2.2) 可逐层使用；(2.3) 的常数不依赖 $p$，平方求和后准确给整个 $\ker D$ 上的有界组合。全直和逆本身是否有界不参与这一步。

对 $Q=L$，同一公式和范数仍是原 Hilbert 范数中的结论，无需把头相似变换称为等距。若 $f$ 有有限孔数支撑，则构造原像 $p_k(W_2)f/k!$ 保持该支撑；它的全空间最小原像可能再经正交投影，本文不宣称这个投影保持同一个有限窗，也不直接把它送入原 $\Lambda$。

## 3. 更高起始核：准确消去一类中间逆

对 $s\ge1$、$k\ge1$ 和 $f\in\mathcal E_s(Q)$，同样有
$$
W_2^kf\in\mathcal E_{s+k}(Q).
$$
在 (2.6) 中取 $n=s+k-1$：$r<k$ 的项被 $Q^sf=0$ 杀掉，$r>k$ 的项被 $\delta^{k+1}(W_2^k)=0$ 杀掉。唯一留下的项是
$$
Q^{s+k-1}W_2^kf
=\frac{(s+k-1)!}{(s-1)!}\,C^kQ^{s-1}f.
\tag{3.1}
$$
令 $\mathfrak J_{s+k}^Q$ 为
$Q^{s+k-1}:\mathcal E_{s+k}(Q)\to\ker Q$
在实际像上的最小范数逆，则
$$
\boxed{
\mathfrak J_{s+k}^Q C^kQ^{s-1}f
=\frac{(s-1)!}{(s+k-1)!}
P_{\mathcal U_{s+k}(Q)}W_2^kf.
}
\tag{3.2}
$$
所有低于 $k$ 次的多项式项落在 $\mathcal E_{s+k-1}(Q)$，故 (2.8) 再给
$$
\boxed{
\|\mathfrak J_{s+k}^Q C^kQ^{s-1}f\|
\le
\frac{2(s-1)!}{(s+k-1)!}
\left(\frac{S_m}{4}\right)^k\|f\|.
}
\tag{3.3}
$$
源中必须保留准确的 $C^kQ^{s-1}$ 次序和输入核；这里没有给任意源上的 $\mathfrak J_{s+k}^Q$ 一个新范数界。

## 4. 受限伴随与旧两带的准确相对式

本节固定 $Q=D$；约定负孔层为零，$h>p+1$ 时 $U_{h,p}=0$，相应零空间间的逆按零映射理解。记
$$
E_{h,p}=\ker D^h\cap\mathcal H_p,\qquad
U_{h,p}=E_{h,p}\ominus E_{h-1,p},\qquad K_p=E_{1,p}.
$$
第一下降和第二下降分别记为
$$
A_{h,p}=P_{U_{h-1,p-1}}D|_{U_{h,p}},\qquad
B_{h,p}=P_{U_{h-2,p-1}}D|_{U_{h,p}}.
$$
这里 $A_{h,p}$ 是尾部第一下降块，不是有限头 $A_m$。

### 4.1 Primitive 层

因为 $DW_2f=Cf$、$D^2W_2f=0$ 对 $f\in K_{p+1}$ 成立，
$$
C|_{K_{p+1}}
=A_{2,p+1}\,P_{U_{2,p+1}}W_2|_{K_{p+1}}.
\tag{4.1}
$$
取伴随时，左边是 $C:K_{p+1}\to K_p$ 的真实受限伴随：
$$
C_K^*f
=P_{K_{p+1}}W_2|_{U_{2,p+1}}\,A_{2,p+1}^*f.
\tag{4.2}
$$
对两个正交子空间间的 $W_2$ 块，减去 $(S_m/2)I$ 不改变该块。因此
$$
\|P_{K_{p+1}}W_2|_{U_{2,p+1}}\|\le S_m/2,
$$
从而
$$
\boxed{
\|C_K^*f\|
\le\frac{S_m}{2}
\left\|\left(D:E_{2,p+1}\to K_p\right)^*f\right\|.
}
\tag{4.3}
$$
右侧是 $P_{E_{2,p+1}}D^*f=A_{2,p+1}^*f$，没有换成环境 $D^*f$。这给相对上界，不给受限伴随的新正下界。

### 4.2 全高度的消逆式

以下第一下降相容式取 $h\ge2$；涉及第二下降 $B_{h,p}^*$ 的公式取 $h\ge3$。

固定层旧相容原像使
$D^{h-1}:U_{h,p}\to K_{p-h+1}$ 为有界双射，记逆为 $J_{h,p}$。第一下降也为有界双射，并准确满足
$$
A_{h,p}J_{h,p}=J_{h-1,p-1}.
\tag{4.4}
$$
证明是将左侧再作用 $D^{h-2}$：第二下降部分落在 $E_{h-2,p-1}$，被杀掉，余下为恒等；再用 $U_{h-1,p-1}$ 上的唯一性。

旧两带式对 $f\in U_{h-2,p-1}$ 给
$$
B_{h,p}^*f
=-(h-2)(h-1)J_{h,p}CD^{h-3}f.
$$
使用 (4.4) 及 (3.2) 中 $s=h-2,k=1$，得到
$$
\boxed{
A_{h,p}B_{h,p}^*
=-(h-1)P_{U_{h-1,p-1}}W_2|_{U_{h-2,p-1}}.
}
\tag{4.5}
$$
因此
$$
\|A_{h,p}B_{h,p}^*\|\le (h-1)S_m/2.
\tag{4.6}
$$
这确实消掉了这个乘积中的 $J_h$，但没有单独界住 $B_h$ 的逆，也没有略去高度因子。

## 5. 连续多桥在原范数中的统一界

令 $D^{(0)}$ 和 $D^{(1)}$ 为旧两带分解中的第一、第二下降；两者在全尾空间上均有界。对 $f\in U_{s,p}$，
$$
D^*f\in U_{s+1,p+1}\oplus U_{s+2,p+1}.
$$
因此 $(D^{(1)*})^kf$ 恰为 $(D^*)^kf$ 的最高高度 $U_{s+2k,p+k}$ 分量。

又由
$$
\operatorname{ad}_D^2(D^*)=-2C,\qquad
\operatorname{ad}_D^3(D^*)=0,
$$
完全展开后只有在每个 $D^*$ 因子上作用两次的项能贡献最高阶，故
$$
\operatorname{ad}_D^{2k}\bigl((D^*)^k\bigr)
=(-1)^k(2k)!C^k.
$$
再用 (2.6) 和 $D^sf=0$，准确得到
$$
(D^{(1)*})^kf
=(-1)^k\frac{(s+2k-1)!}{(s-1)!}
J_{s+2k,p+k}C^kD^{s-1}f.
\tag{5.1}
$$
连续施加 $k$ 次第一下降把 $J_{s+2k,p+k}$ 变成 $J_{s+k,p}$。将 (3.2) 代入即得
$$
\boxed{
(D^{(0)})^k(D^{(1)*})^kf
=(-1)^k\frac{(s+2k-1)!}{(s+k-1)!}
P_{U_{s+k,p}}W_2^kf.
}
\tag{5.2}
$$
因此同一个原 Hilbert 范数中
$$
\boxed{
\|(D^{(0)})^k(D^{(1)*})^k|_{U_{s,p}}\|
\le
\frac{2(s+2k-1)!}{(s+k-1)!}
\left(\frac{S_m}{4}\right)^k.
}
\tag{5.3}
$$
常数不依赖孔数 $p$，但保留 $s,k$ 的真实成本。

特别，primitive 起点 $s=1$ 的两次连续桥给
$$
\boxed{
\|(D^{(0)})^2(D^{(1)*})^2|_{K_p}\|
\le\frac32S_m^2\le\frac1{6m^6}.
}
\tag{5.4}
$$
取伴随只能得到相应的
$P_{K_p}(D^{(1)})^2(D^{(0)*})^2$
的界；这个受限投影不能删掉。

## 6. 与当前真实 Schur 源的准确接口

完整内部链为
$$
S=S^{(0)}+S^{(1)},\qquad
\mathcal G=SS^*,
$$
其中 $S^{(1)}$ 来自尾部第二下降。旧上升出生块是
$S^{(1)}S^{(0)*}$。新消元顺序的真实有效源仍为
$$
\sigma=V_2Q_1^{-1}V_1B_0^{-1}g_0,\qquad
z_2=\mathcal H_{2,q}^{-1}\sigma.
$$
上述结论有两个已付范围：

- 对一个确实写成 $C^kQ^{s-1}f$、$f\in\ker Q^s$ 的已知源，(3.2)--(3.3) 给真正最小原像和原范数能量；
- 对没有额外中间算子的连续出生桥，(5.2)--(5.4) 给孔数一致的原范数界。

实际 $\sigma$ 中有 $Q_1^{-1}$，并且 $S^{(0)*}$ 同时含有限头 $A_m^*$。式 (4.5) 只直接处理尾部第一下降与第二下降的乘积；它没有处理余下的 $D^{(1)}A_m^*$ 项。本文没有证明 $Q_1^{-1}$ 与 $C$、$D$ 或各 $J_h$ 交换，也没有把两个上升桥改写成一个已付的连续 $C^2$ 源。

同样，$Q=L$ 的 (2.2) 不能替代原 $M=\ker T$ 上的投影。接入 [完整核补全和合法 $M$ 测试](R239-appendix-full-l-kernel-completion-and-legal-m-tests.md) 后，当前仍须控制实际 $\widetilde C_{\rm tot}(h(z))$ 的合成范数，或在正确 $\mathcal H_{2,q}$ 度量中支付上述 $\sigma$。本文的最小能量界不等于该缺口已经闭合，也不推出无权 $N=M$。
