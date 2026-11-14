# R226：局部真实右移的一致像逼近、爆炸核残量与稳定缺陷距离

日期：2026-11-13（Asia/Taipei）。作者：boundary。状态：已证明。

本文把新的统一前缀估计用于原先的两头右移接口，准确区分它在环境空间和 $B$ 图尺度中的作用。两个真实慢模型都满足：$B\mathcal J_m$ 在整个 $M$ 上按算子范数趋于恒等，$BT\mathcal J_m$ 也按算子范数趋零；但 $T\mathcal J_m|_M$ 的范数事实上爆炸。最后给出真正未知缺陷 $W=M\ominus N$ 上的精确距离恒等式。本文不把环境伴随下界转换成尚未证明的压缩下界。

## 1. 对象

固定前两稿中的实际 $T_N$ 或 $T_Y$，并置
$$
M=\ker T,\qquad N=\overline{BM},\qquad W=M\ominus N.
$$
令 $D_m=2^m$，按低头和高尾分解整数坐标。低头右移为
$$
J^{[m]}e_r=
\begin{cases}
\alpha_{v_2(r+1)}^{-1}e_{r+1},&0\le r<D_m-1,\\
0,&r=D_m-1,
\end{cases}
\qquad \mathcal J_m=J^{[m]}\otimes I.
$$
其真实范数及精确像公式为
$$
\|\mathcal J_m\|=\alpha_{m-1}^{-1},\qquad
B\mathcal J_m=I-Q_m,
\tag{1.1}
$$
其中 $Q_m$ 投影到 $n\equiv-1\pmod{2^m}$。这正是此前两头交换子稿的 $\Pi_{-,m}$。

## 2. 新估计给算子范数层面的一致像逼近

统一前缀稿已对任意 $\gamma<1$ 证明
$$
\|Q_m|_M\|\le C_\gamma e^{-\gamma m}.
$$
故
$$
\boxed{
\|B\mathcal J_m|_M-I_M\|\le C_\gamma e^{-\gamma m}.
}
\tag{2.1}
$$
这里 $I_M:M\to\mathcal H_-$ 是实际包含映射，不把 $B\mathcal J_mM$ 预先视为 $M$ 的子空间。

因为 $B$ 与 $T$ 交换且 $Tf=0$，
$$
BT\mathcal J_m f=TB\mathcal J_mf=-TQ_mf\quad(f\in M).
$$
从而
$$
\boxed{
\|BT\mathcal J_m|_M\|\le6C_\gamma e^{-\gamma m}.
}
\tag{2.2}
$$
原稿只有逐向量强收敛；(2.1)—(2.2) 是对整个核单位球的一致加强。

## 3. 同一核上的未乘 B 误差仍爆炸

**定理 3.1。** 两个实际模型均满足，对所有充分大 $m$，
$$
\boxed{
\|T\mathcal J_m|_M\|
\ge\frac{a_{m-1}}{8\alpha_{m-1}}
\exp(-8m2^m)\longrightarrow\infty.
}
\tag{3.1}
$$
因此不能用 (2.2) 形式取消 $B$。

### 3.1. 同一有限头的真正核延拓

令 $v=e_{D_m-1}$，取原标准块 $L=64D_m$。R185/R188 的有限纯块构造给
$$
V=\sum_{k=0}^{D_m-1}(-1)^kT_m^kv\otimes h_k,
$$
其中 $T_m=T|_{\mathcal F_m}$，间隔 $[m,L)$ 真空，$h_k$ 位于 $[L,2L)$ 的 $k$ 孔层。既有算子预算给
$$
\|V\|\le H_m:=e^{8m2^m},\qquad
\|TV\|\le26\eta_{L-1}\|V\|.
$$
先按其真实范数归一化，再应用标准修复，得到 $f_m\in M$，满足
$$
\|f_m-V\|\le2H_me^{-20\,16^L},\qquad
\|f_m\|\le2H_m.
\tag{3.2}
$$
原低头严格保留为 $P_mf_m=v$。

### 3.2. 有限头交换子的一个确切大系数

置 $j=m-1$。由于 $J^{[m]}v=0$，
$$
[T_m,J^{[m]}]v=-J^{[m]}T_mv.
$$
考察输出头坐标 $D_m-2^j=2^j$。在 $T_N$ 情形，该系数的绝对值准确是 $a_j/\alpha_j$。

Cayley 情形，$T_mv$ 在头坐标 $D_m-1-2^j$ 的系数为
$$
b_j=a_j-\sum_{i<j}a_i\frac{d_j}{d_i^{2^{j-i}}}.
\tag{3.3}
$$
这是有限头矩阵的一条固定下降对角线：$j$ 项提供一次下降，其余只有 $i<j$ 的偶数次 Cayley 项能够达到同一整数增量，符号为负。

真实递推 $N_i^2=\eta_iN_{i+1}$ 给
$$
\frac{d_j}{d_i^{2^{j-i}}}
=\eta_i^{2^{j-i-1}}\eta_{i+1}^{2^{j-i-2}}\cdots\eta_{j-1}
\le\eta_{j-1}.
$$
所以 $b_j\ge a_j-2\eta_{j-1}\ge a_j/2$（$j\ge1$）。再经 $J^{[m]}$，除以的权正是 $\alpha_j$。因此两种模型统一满足
$$
\|[T_m,J^{[m]}]v\|\ge\frac{a_j}{2\alpha_j}.
\tag{3.4}
$$

### 3.3. 实际尾贡献不抵消这个低头系数

在 $V$ 所在的低头、空白间隔和新块空间上，低位实际项与其有限头项的差，对 $T_N$ 不超过 $2\eta_{L-1}$，对 $T_Y$ 不超过 $18\eta_{L-1}$。右移 $\mathcal J_m$ 保持该空间，范数为 $\alpha_j^{-1}$；所有索引 $i\ge m$ 的实际项均只作用尾坐标，与 $\mathcal J_m$ 精确交换。因此
$$
\|[T,\mathcal J_m]V-([T_m,J^{[m]}]\otimes I)V\|
\le36\alpha_j^{-1}\eta_{L-1}H_m.
\tag{3.5}
$$
投到整个有限头 $\mathcal F_m$ 时，$V$ 的 $k\ge1$ 项由于新块有孔而消失，所以
$$
P_m([T_m,J^{[m]}]\otimes I)V=[T_m,J^{[m]}]v.
$$
最后
$$
\|[T,\mathcal J_m](f_m-V)\|
\le24\alpha_j^{-1}H_me^{-20\,16^L},
\tag{3.6}
$$
因为 $\|T\|\le6$ 并使用 (3.2)。

结合 (3.4)—(3.6)，且 $Tf_m=0$，得到
$$
\|T\mathcal J_m f_m\|
\ge\frac{a_j}{2\alpha_j}
-\alpha_j^{-1}H_m\left(36\eta_{L-1}+24e^{-20\,16^L}\right)
\ge\frac{a_j}{4\alpha_j}
$$
对充分大 $m$ 成立。最后一个误差比较有巨大余量：$H_m=e^{8m2^m}$，而 $L=64\,2^m$，负指数为 $-c16^L$。
除以 $\|f_m\|\le2H_m$，得到 (3.1)。

实际 $-\log\alpha_{m-1}\asymp16^{m-1}$ 压倒 $8m2^m+2\log m$，所以右侧趋于无穷。
同时
$$
\operatorname{dist}(\mathcal J_m f,M)\ge\frac{\|T\mathcal J_mf\|}{\|T\|}
$$
说明在整个 $M$ 上也不存在对这些右移误差的一致小范数修正。
此证明使用的 $f_m$ 是标准构造类，事实上可属于稳定部分 $N$；故本节**没有**声称在未知 $W$ 上也已证明同样的范数爆炸。

## 4. 真正缺陷空间上的 B 图距离

定义仅测量后移输出的半范数距离
$$
\operatorname{dist}_B(x,M)=\inf_{y\in M}\|B(x-y)\|.
$$
由于 $N=\overline{BM}$，对每个 $f\in M$ 精确有
$$
\boxed{
\operatorname{dist}_B(\mathcal J_mf,M)
=\operatorname{dist}((I-Q_m)f,N).
}
\tag{4.1}
$$
故
$$
\left|
\operatorname{dist}_B(\mathcal J_mf,M)-\|P_Wf\|
\right|
\le C_\gamma e^{-\gamma m}\|f\|.
\tag{4.2}
$$
这里使用 $f\in M$，所以 $\operatorname{dist}(f,N)=\|P_Wf\|$。

特别，对单位 $w\in W$，由 $w\perp N$，
$$
\begin{aligned}
\operatorname{dist}((I-Q_m)w,N)
&\ge|\langle(I-Q_m)w,w\rangle|\\
&=1-\|Q_mw\|^2.
\end{aligned}
$$
上界则是 $\|(I-Q_m)w\|\le1$。因此
$$
\boxed{
1-C_\gamma^2e^{-2\gamma m}
\le\operatorname{dist}_B(\mathcal J_mw,M)\le1.
}
\tag{4.3}
$$
若 $W$ 非零，(2.2) 与 (4.3) 可以同时成立：右移误差经过 $B$ 后趋零，但右移向量在 $B$ 半范数中仍离真正核至少约为 1。
这准确指出所缺的闭值域/核逼近输入，而不是矛盾。

## 5. 由此排除和保留的路线

- 新的占满前缀估计确实把原强逼近加强为整个 $M$ 上的算子范数逼近。
- 原右移交换子在整个 $M$ 上并不小，反而有 (3.1) 的实际下界；真实 Cayley 逆也已计入。
- $N=M$ 等价于 (4.1) 对全部 $f\in M$ 趋零。若某个非零缺陷向量存在，它必满足明确的 (4.3)，并不被目前的前缀估计排除。
- 要从这里继续，必须证明真实核的 $B$ 图逼近性质，或取得适用于 $W$ 的额外控制；不能用环境空间 $(B^*)^k|_M$ 的下界直接替换其压缩，也不能形式约去 (2.2) 中的 $B$。
