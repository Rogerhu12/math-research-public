# 原 Y carry 的首缺位行和主项、准确平方域与真实总孔核心

日期：2026-11-27（台北时间）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：以下原 Y carry 的分解、指定平方源空间中的最大域、额外对角权的充要条件及整个平方源空间上的条件总孔核心已证明；尚未将真实未知 $W$ 的规范来源放入此平方源空间，未证明 $N=M$。**

本稿接 [规范来源 carry 范数](../results/R271-appendix-canonical-source-carry-norm-total-hole-core.md) 和 [N 型最大 carry 域](../results/R271-appendix-maximal-n-carry-domain-triangular-reconstruction.md)。N 型降首缺位列的正交平方和已支付，不能直接搬给 Y 型。本稿准确提取 Y 型多出的一个行和算子；其余全部真实 Cayley 项在原平方源空间上有界。这个行和主项恰好升一个物理孔，故把它与纯创建合并后，**整个原 $b_q$ 平方源空间已足够给 Y 型的完整总孔图核心**，无需先要求单独 carry 输出属于 $\mathcal H$。此外，保留行内相消也得到比此前加权 $\ell^1$ 条件更大的单独 Y carry 域。

## 1. 原源空间与新主项

仍用 $S=B^*$、$N_i=B^{2^i}/d_i$、$Y_i=N_i(I+N_i)^{-1}$、$a_i=(i+1)^{-2}$，以及纯创建
$$
D^*=\sum_{i\ge0}a_iE_i^*,\qquad
K_N=T_N^*-D^*,\qquad K_Y=T_Y^*-D^*.
$$
$P_q$ 投到首零位恰为 $q$ 的坐标；$\mathsf P_p$ 投到总物理孔数恰为 $p$。两种分级继续区分。

置
$$
\eta_i=\alpha_{i+1}/\alpha_i,\qquad
b_0=\eta_0,\qquad b_q=a_{q-1}\eta_{q-1}\quad(q\ge1),
$$
$$
\mathcal C_2=
\left\{h:\|h\|_{\mathcal C_2}^2
=\sum_{q\ge0}b_q^2\|P_qh\|^2<\infty\right\}.
\tag{1.1}
$$
这是加权 Hilbert 空间；每个 $P_qh$ 均为整个首零位块上的 Hilbert 向量，不限总孔数。

原精确权给
$$
\eta_0=e^{-1070}<1/64,\qquad
\eta_{i+1}\le\eta_i/4,\qquad
\eta_{i+1}\le\eta_i^2.
\tag{1.2}
$$
末一个不等式也可直接核：若
$A_i=-\log\eta_i=1400\,16^i-630\,8^i+300\,2^i$，则
$$
A_{i+1}-2A_i=19600\,16^i-3780\,8^i>0.
$$
因此 $b_0=b_1$，且 $b_{q+1}\le b_q/4$ 对 $q\ge1$ 成立。

在有限支撑上定义
$$
\boxed{V_bh=\sum_{q\ge1}b_qE_q^*P_qh.}
\tag{1.3}
$$
它填入输入的首缺位，故恰增加一个物理孔。这里没有 $q=0$ 项。

**定理 1.1。** 存在有界算子 $R_b:\mathcal C_2\to\mathcal H$，满足
$$
\boxed{K_Yh=-V_bh+R_bh,\qquad \|R_b\|\le12.}
\tag{1.4}
$$
式 (1.4) 首先在有限支撑上成立，其后在全部 $\mathcal C_2$ 的形式坐标层成立。$R_b$ 保留全部真实 Cayley 逆；不是将 Y 模型换成 N 模型。

## 2. 全 Cayley 分解与有界余项的逐块账本

以下所有推导先作用于有限支撑。由 $(N_i^*)^2=\eta_iN_{i+1}^*$ 及真实恒等式
$$
(I+N_i^*)^{-1}=I-N_i^*+(N_i^*)^2(I+N_i^*)^{-1},
$$
准确得到
$$
K_Y=K_N-L_1+L_2-L_3,
\tag{2.1}
$$
其中
$$
L_1=\sum_{i\ge0}a_i\eta_iN_{i+1}^*
=\sum_{j\ge1}b_jN_j^*,
$$
$$
L_2=\sum_{i\ge0}a_i\eta_iN_i^*N_{i+1}^*,
$$
$$
L_3=\sum_{i\ge0}a_i\eta_i^2\eta_{i+1}
        (I+N_i^*)^{-1}N_{i+2}^*.
\tag{2.2}
$$
所有原因子交换；每个剩余逆仍按 $\|(I+N_i^*)^{-1}\|\le3$ 支付。

沿用已付的正交 carry 列
$$
N_i^*P_q=\frac{\alpha_q}{\alpha_i}V_{iq}\quad(i<q),
\qquad
c_q^2=\sum_{i<q}a_i^2\left(\frac{\alpha_q}{\alpha_i}\right)^2.
$$
所有 $(i,q)$ 的 $V_{iq}$ 输出范围正交，且 $c_q\le3b_q$。已有结论给
$$
\|K_Nh\|\le3\sqrt2\,\|h\|_{\mathcal C_2}.
\tag{2.3}
$$

### 2.1 $L_1$ 只有填首缺位部分需要保留

$j=q$ 时 $N_j^*P_q=E_q^*P_q$，这正是 $V_b$。
$j>q$ 时 $N_j^*$ 保持 $P_q$，其整块范数至多 $\sum_{j>q}b_j$。这个和在 $q=0$ 时至多 $4b_0/3$，在 $q\ge1$ 时至多 $b_q/3$。

$1\le j<q$ 时，全部输出仍是上述正交降首缺位列。由于
$$
\frac{b_j}{a_j}=\frac{(j+1)^2}{j^2}\eta_{j-1}\le4\eta_0,
$$
这一部分的范数至多 $12\eta_0\|h\|_{\mathcal C_2}$。所以
$$
\boxed{\|(L_1-V_b)h\|\le2\|h\|_{\mathcal C_2}.}
\tag{2.4}
$$
这里分别使用整块直和与全部降首缺位列的正交性，没有按无依据的列平方和估计 $V_b$。

### 2.2 $L_2$ 的四种输入位置

固定第 $i$ 项，再按来源首零位 $q$ 分为四种情况。

1. **$q<i$。** 两个前移均保持 $P_q$。对固定 $q$ 求和的块范数至多 $\sum_{i>q}b_{i+1}\le b_q/3$；整个这一部分的范数至多 $\|h\|_{\mathcal C_2}/3$。

2. **$q=i$。** 不假定不同 $q$ 的像正交。第 $q$ 列的归一系数为 $\gamma_q=b_{q+1}/b_q$。有 $\gamma_0=1$，而对 $q\ge1$，(1.2) 给 $\gamma_q\le\eta_{q-1}$。故
   $$
   \sum_{q\ge0}\gamma_q^2\le1+\frac{16}{15}\eta_0^2,
   $$
   三角不等式后用来源块的 Cauchy--Schwarz，得该部分范数至多
   $\sqrt{1+16\eta_0^2/15}\,\|h\|_{\mathcal C_2}$。

3. **$q=i+1$。** $N_{i+1}^*$ 先填首零位，随后 $N_i^*$ 必须至少跨过 $i$、$i+1$ 两个边界。因此
   $$
   \|N_i^*N_{i+1}^*P_{i+1}\|\le\eta_i\eta_{i+1}.
   $$
   输出首零位是 $i$，不同 $i$ 的范围正交；连同 $a_i\eta_i=b_{i+1}$，这一部分范数至多 $\eta_0\eta_1\|h\|_{\mathcal C_2}$。

4. **$q>i+1$。** 准确系数为
   $$
   N_i^*N_{i+1}^*P_q
   =\frac{\alpha_q}{\alpha_i}\widetilde V_{iq}.
   $$
   输出首零位为 $i$，其后第一、第二个占据位依次为 $i+1,q$；全部 $(i,q)$ 的这些范围正交。因此连同外系数 $a_i\eta_i$，这一部分范数至多 $3\eta_0\|h\|_{\mathcal C_2}$。

所有加法仍是真实二进位前移。合并四项及 $\eta_0<1/64$，得
$$
\boxed{\|L_2h\|\le2\|h\|_{\mathcal C_2}.}
\tag{2.5}
$$

### 2.3 $L_3$ 的全部剩余逆

令 $t_i=a_i\eta_i^2\eta_{i+1}$。保留逆的因子 $3$，对其右边的 $N_{i+2}^*$ 分块。

当 $q\le i+1$ 时，$b_q\ge b_{i+1}$，故第 $i$ 项在整个这些来源块上的范数至多
$$
3t_i/b_{i+1}=3\eta_i\eta_{i+1}.
\tag{2.6}
$$
当 $q=i+2$ 时，相应归一范数至多
$$
3t_i/b_{i+2}
=3(a_i/a_{i+1})\eta_i^2\le12\eta_i^2.
\tag{2.7}
$$
当 $q>i+2$ 时，固定 $i$ 的 $N_{i+2}^*P_q$ 输出范围正交，且
$$
\frac{t_i\alpha_q}{\alpha_{i+2}b_q}
=\left(\frac q{i+1}\right)^2
  \eta_i\frac{\alpha_{q-1}}{\alpha_i}
\le9\eta_i^2\eta_{i+1}.
\tag{2.8}
$$
最后一步写 $q=i+3+s$，使用 $\eta_j<1/16$ 及
$(3+s)^2\,16^{-s}\le9$。所以这一部分连逆的范数至多 $27\eta_i^2\eta_{i+1}$。

对 $i$ 作算子范数求和，(1.2) 于是给
$$
\begin{aligned}
\|L_3\|_{\mathcal C_2\to\mathcal H}
&\le3\sum_i\eta_i\eta_{i+1}
 +12\sum_i\eta_i^2+27\sum_i\eta_i^2\eta_{i+1}\\
&\le\frac{68}{5}\eta_0^2+\frac{48}{7}\eta_0^3<1.
\end{aligned}
\tag{2.9}
$$
这里 $68/5=13.6$；立方项的更精确值为 $48/7$。没有把原 Y 级数截断后留下未计的逆尾。

结合 (2.1)、(2.3)--(2.5)、(2.9)，取
$$
R_b=K_N-(L_1-V_b)+L_2-L_3,
$$
即可得 (1.4)，事实上这些上界之和已小于 $10$。采用 $12$ 只为保留余量。
有界延拓与每个固定坐标的连续性使该身份对全部 $\mathcal C_2$ 在形式坐标层成立。

## 3. 行内相消保留后的准确最大域

对输出整数 $n$，令 $r(n)$ 为其首零位。输入首零位为 $q\ge1$ 的一个基向量，经 $E_q^*$ 只能到达**唯一**输出；反过来，输出 $n$ 的全部来源恰为
$$
n-2^q,\qquad 1\le q<r(n).
$$
所以在形式坐标层
$$
\boxed{(V_bh)_n
=\sum_{q=1}^{r(n)-1}b_qh_{n-2^q}.}
\tag{3.1}
$$
每行有限。不同输出的输入纤维不交，不能在一个纤维内部删除交叉项。

令 $\mathcal D(V_b)$ 为 $\mathcal C_2$ 中使 (3.1) 的完整输出平方可和的来源。由 (1.4)，准确有
$$
\boxed{
\{h\in\mathcal C_2:K_Yh\in\mathcal H\}
=\mathcal D(V_b)
=\left\{h\in\mathcal C_2:
\sum_n\left|\sum_{1\le q<r(n)}b_qh_{n-2^q}\right|^2<\infty
\right\}.
}
\tag{3.2}
$$
这只是**在指定 $\mathcal C_2$ 内**的准确最大域，不声称所有形式 $K_Yh\in\mathcal H$ 的来源已自动属于 $\mathcal C_2$。

$V_b:\mathcal D(V_b)\subset\mathcal C_2\to\mathcal H$ 闭：图收敛时，每个有限行的极限仍是 (3.1)。有限坐标向量是图核心：先保留有限个完整输出纤维，再加有限个 $q=0$ 来源坐标。纤维互不相交且每个纤维有限，故输入与输出同时按各自平方和收敛。由于 $R_b$ 有界，$K_Y$ 在 (3.2) 的最大域上同样闭，具有同一个有限坐标图核心。

## 4. 额外对角平方权的准确充要条件

给定任意有限实数 $\omega_q\ge1$（$q\ge1$），定义
$$
\|h\|_{\mathcal C_{2,\omega}}^2
=b_0^2\|P_0h\|^2
 +\sum_{q\ge1}\omega_qb_q^2\|P_qh\|^2.
\tag{4.1}
$$
由 (3.1) 的互不相交有限纤维，行 Cauchy--Schwarz 的常数准确给
$$
\boxed{
\|V_b\|_{\mathcal C_{2,\omega}\to\mathcal H}^2
=\sup_{r\ge2}\sum_{q=1}^{r-1}\omega_q^{-1}
=\sum_{q\ge1}\omega_q^{-1},
}
\tag{4.2}
$$
允许右端为 $+\infty$。下界在单个输出 $n=2^r-1$ 的纤维上取
$b_qh_{n-2^q}=\omega_q^{-1}$ 后归一即可达到相应有限和。

因此，对**原真实 $K_Y$** 有充要条件
$$
\boxed{
K_Y:\mathcal C_{2,\omega}\longrightarrow\mathcal H
\text{ 有界}\quad\Longleftrightarrow\quad
\sum_{q\ge1}\omega_q^{-1}<\infty.
}
\tag{4.3}
$$
充分性由 (1.4)、(4.2) 给范数上界
$12+(\sum\omega_q^{-1})^{1/2}$。必要性也保全部余项：上述单纤维归一来源满足 $\|R_bh\|\le12$，故其 $K_Y$ 输出范数至少为
$(\sum_{q<r}\omega_q^{-1})^{1/2}-12$，发散时不能被有界余项抵消。

特别，$\omega_q=q(\log(q+2))^{1+\delta}$ 在 $\delta>0$ 时可用，而 $\delta=0$ 的这一对角权不可用。该结论仅是这些无条件对角源权的准确边界，不能用来排除真实 $W$ 的特殊行内相消。

## 5. 行和域严格大于旧加权 $\ell^1$ 条件

旧条件 $\sum_qb_q\|P_qh\|<\infty$ 保证 $h\in\mathcal C_2$，且由三角不等式保证 $V_bh\in\mathcal H$，所以包含在 (3.2) 中。

严格性可直接在原坐标中见到。对 $j\ge1$，置 $n_j=2^{2j+2}-1$，仅令
$$
b_{2j}h_{n_j-2^{2j}}=j^{-1},\qquad
b_{2j+1}h_{n_j-2^{2j+1}}=-j^{-1},
\tag{5.1}
$$
其余坐标为零。两项首零位分别为 $2j,2j+1$，并经 (1.3) 到达同一输出 $n_j$。因此
$$
\|h\|_{\mathcal C_2}^2=2\sum_{j\ge1}j^{-2}<\infty,
\qquad V_bh=0,
\qquad K_Yh=R_bh\in\mathcal H,
$$
但
$$
\sum_qb_q\|P_qh\|=2\sum_{j\ge1}j^{-1}=\infty.
$$
这个例子只证明实际 carry 域严格扩大；没有宣称该 $h$ 是未知 $W$ 的规范来源，也没有宣称其 $T_Y^*h$ 属于 $\mathcal H$。

## 6. 整个 $\mathcal C_2$ 已给完整实际总孔图核心

定义原 Hilbert 空间上的有界算子
$$
\mathcal A_Y=D^*-V_b.
\tag{6.1}
$$
这里 $V_b$ 在未加逆权的 $\mathcal H$ 上有界，范数平方是 $\sum_{q\ge1}b_q^2$，由 §3 的同一纤维计算得到。$\mathcal A_Y$ 严格升一个总物理孔，并且
$$
\boxed{T_Y^*=\mathcal A_Y+R_b,\qquad R_b:\mathcal C_2\to\mathcal H\text{ 有界}.}
\tag{6.2}
$$
这是本稿用于完整图核心的分解；它与先要求 $K_Yh\in\mathcal H$ 的路线不同。

现只设 $h\in\mathcal C_2$ 且形式 $T_Y^*h=f\in\mathcal H$，**不加** $V_bh\in\mathcal H$ 或 $D^*h\in\mathcal H$ 的分别条件。令
$$
h^{[p]}=\mathsf P_{\le p}h.
$$
由于 $P_q\mathsf P_{\le p}=0$ 对 $q>p$ 成立，只有有限个首零位块参与，故 $h^{[p]}\in\mathcal H$。同时 $h^{[p]}\to h$ 于 $\mathcal C_2$。

由 (6.2)，形式 $\mathcal A_Yh=f-R_bh$ 已属于 $\mathcal H$。保留 $D^*h$ 与 $V_bh$ 的同次数相消，准确有
$$
\mathcal A_Yh^{[p]}
=\mathsf P_{\le p+1}\mathcal A_Yh\longrightarrow\mathcal A_Yh,
\qquad R_bh^{[p]}\longrightarrow R_bh.
$$
因此
$$
\boxed{T_Y^*h^{[p]}\longrightarrow f.}
\tag{6.3}
$$
此外 $S:\mathcal C_2\to\mathcal H$ 有界，因为在 $P_q$ 上其范数是 $\alpha_q$，且
$$
\sup_q\alpha_q/b_q<\infty
\quad\left(\alpha_q/b_q=q^2\alpha_{q-1}\ (q\ge1),
\quad \alpha_0/b_0<\infty\right).
$$
所以 $Sh^{[p]}\to Sh$，这给完整原除法图收敛。等价地，最大形式算子
$$
T_{Y,\max}^*:\{h\in\mathcal C_2:T_Y^*h\in\mathcal H\}\to\mathcal H
$$
是闭算子，$\mathcal H$ 是其图核心：闭性来自逐坐标形式唯一性，核心来自刚才的实际总孔截断。对每个 $h^{[p]}\in\mathcal H$，随后还可在普通 $\mathcal H$ 中用有限坐标向量逼近；原 $S,T_Y^*$ 均有界，故有限坐标向量也给上述三项范数中的核心。

若 $f=w\in W$ 且 $h=h(w)$ 是同一规范来源，(6.3) 与 $Tw=0$ 迫
$$
\|w\|^2=\lim_p\langle T_Y^*h^{[p]},w\rangle=0.
$$
因此，N 型既有结论与本稿 Y 型结论合起来：**原两模型都只需同一个 $\mathcal C_2$ 规范来源条件，便可排除该 $w$。** 本稿没有从 $\Gamma(u)$ 的闭包来源条件、每个固定总孔层在 $\mathcal H$、或普通 $Sh\in\mathcal H$ 中免费得到 $h\in\mathcal C_2$。§4 的额外对角权是控制单独 $K_Yh$ 的准确条件，不能再称为本节整个 $T_Y^*$ 图核心必需的条件。
