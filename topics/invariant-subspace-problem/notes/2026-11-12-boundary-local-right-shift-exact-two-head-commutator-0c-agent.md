# 边界标准右移的精确两头交换子与慢核的尾行关系

日期：2026-11-12（UTC）。作者：l2_moments。状态：完整实际接口，不另占结果编号。

本文给出边界低位标准右移与 $T_N=\sum_j a_jN_j^-$ 的精确交换子。真实高位进位在此交换子中完全抵消，不需要 $\eta$ 近似。它把右移破坏核的部分限制到两个头方向，但没有给出所余尾除法的有界逆，也没有解决 R200 的 $N=M$。

## 1. 边界、低头右移与尾算子

在 $\mathcal H_-=\ell^2(\mathbb N_0)$ 上，
$$
Be_0=0,\qquad Be_n=\alpha_{v_2(n)}e_{n-1}\quad(n\ge1),
$$
其中 $\alpha_j>0$ 严格递减。记
$$
d_j=\|B^{2^j}\|,\qquad N_j^-=B^{2^j}/d_j.
$$
取任意 $a\in\ell^1$，定义真实范数收敛级数
$$
T_N=\sum_{j\ge0}a_jN_j^-.
\tag{1.1}
$$
主应用为 $a_j=(j+1)^{-2}$；以下交换子公式不需要正性。

固定整数 $m\ge1$，置 $D=2^m$，按
$$
e_{Dq+r}=e_r\otimes e_q,\qquad 0\le r<D,
$$
识别 $\mathcal H_-=\mathbb C^D\otimes\mathcal H_-^{(m)}$。低头截断为
$$
B_m e_0=0,\qquad
B_m e_r=\alpha_{v_2(r)}e_{r-1}\quad(1\le r<D).
$$
真正的尾移位为
$$
B^{(m)}e_0=0,\qquad
B^{(m)}e_q=\alpha_{m+v_2(q)}e_{q-1}\quad(q\ge1).
$$
于是
$$
\boxed{B=B_m\otimes I+|D-1\rangle\langle0|\otimes B^{(m)}.}
\tag{1.2}
$$
这是每个基向量上的准确块分解。

定义有界的低头标准右移
$$
J^{[m]}e_r=
\begin{cases}
\alpha_{v_2(r+1)}^{-1}e_{r+1},&0\le r<D-1,\\
0,&r=D-1,
\end{cases}
\qquad
\mathcal J_m=J^{[m]}\otimes I.
\tag{1.3}
$$
它不是整个 $B$ 的有界逆。因为 $1\le r+1<D$ 中最大 $v_2(r+1)$ 为 $m-1$，
$$
\boxed{\|\mathcal J_m\|=\alpha_{m-1}^{-1}.}
\tag{1.4}
$$
令 $\Pi_{0,m}=|0\rangle\langle0|\otimes I$、
$\Pi_{-,m}=|D-1\rangle\langle D-1|\otimes I$。由 (1.2)，两个尾角项分别被右移的首行、末列消去，故
$$
\boxed{
B\mathcal J_m=I-\Pi_{-,m},\qquad
\mathcal J_mB=I-\Pi_{0,m}.
}
\tag{1.5}
$$
特别 $[B,\mathcal J_m]=\Pi_{0,m}-\Pi_{-,m}$。

边界中 $\Pi_{-,m}\to0$ 强，而 $\Pi_{0,m}\to|e_0\rangle\langle e_0|$ 强，所以
$$
B\mathcal J_m\to I,\qquad
\mathcal J_mB\to I-|e_0\rangle\langle e_0|
\quad{\rm SOT}.
\tag{1.6}
$$
(1.6) 没有说明 $\mathcal J_m$ 保持任何给定核，其范数也不一致有界。

## 2. 真实进位项与低头右移精确交换

固定 $j<m$，写 $s=2^j$，定义低头矩阵
$$
R_{j,m}=\sum_{r=0}^{s-1}|D-s+r\rangle\langle r|.
\tag{2.1}
$$
实际进位链，或者直接按“头内减去 $s$”与“向尾借位”两种情况逐基计算，给
$$
\boxed{
N_j^-=
\frac{B_m^s}{d_j}\otimes I
+\frac1{\alpha_j}R_{j,m}\otimes B^{(m)}.
}
\tag{2.2}
$$
等价地，第二项是 $(\alpha_m/\alpha_j)R_{j,m}\otimes N_m^{(m)}$，
其中 $N_m^{(m)}=B^{(m)}/\alpha_m$。因此 (2.2) 没有遗漏向尾借位的实际系数。

现在证明
$$
\boxed{R_{j,m}J^{[m]}=J^{[m]}R_{j,m}.}
\tag{2.3}
$$
若 $0\le r<s-1$，两边都把 $e_r$ 送到 $e_{D-s+r+1}$；两系数相等，因为
$$
v_2(D-s+r+1)=v_2(r+1)
$$
在 $0<r+1<s$ 时成立。若 $r=s-1$，先右移后已离开 $R_{j,m}$ 的初始空间，先作用 $R_{j,m}$ 则到达被右移杀掉的末列，两边都为零。其他 $r$ 两边也均为零。$j=0$ 时没有内部区间，端点论证仍直接成立。

所以 (2.2) 中的全部真实进位项与 $\mathcal J_m$ 精确交换。不能把这一特殊抵消替换为一般的“有限头算子不影响进位”说法。

## 3. 每个位与整个慢符号的精确交换子

有限头的两端恒等式为
$$
[B_m,J^{[m]}]=|0\rangle\langle0|-|D-1\rangle\langle D-1|.
$$
由有限幂交换子求和，
$$
[B_m^s,J^{[m]}]
=
|0\rangle\langle0|B_m^{s-1}
-B_m^{s-1}|D-1\rangle\langle D-1|.
\tag{3.1}
$$
中间项为零：$B_m|0\rangle=0$，而
$\langle D-1|B_m=0$。

两端权积相同，均为 $W_{s-1}=d_j/\alpha_j$。后一端可由
$v_2(D-t)=v_2(t)$（$1\le t<s$）逐项核对。因此 (2.2)—(3.1) 得
$$
\boxed{
[N_j^-,\mathcal J_m]
=
\frac1{\alpha_j}
\bigl(|0\rangle\langle2^j-1|
-|D-2^j\rangle\langle D-1|\bigr)\otimes I,
\quad j<m.
}
\tag{3.2}
$$

对 $j\ge m$，$N_j^-$ 仅作用尾位，和 $\mathcal J_m$ 精确交换。
由于 (1.1) 范数收敛，对固定 $m$ 可合法交换取和与有界交换子，得到
$$
\boxed{
[T_N,\mathcal J_m]
=
\left(
|0\rangle\sum_{j<m}\frac{a_j}{\alpha_j}\langle2^j-1|
-
\sum_{j<m}\frac{a_j}{\alpha_j}|D-2^j\rangle\langle D-1|
\right)\otimes I.
}
\tag{3.3}
$$

这里 $\sum c_j\langle r_j|$ 表示坐标线性行 $x\mapsto\sum c_jx_{r_j}$，
不对 $c_j$ 额外取复共轭。公式对任意复系数成立。

记
$$
q_m=\left(\sum_{j<m}|a_j/\alpha_j|^2\right)^{1/2},\qquad
v_m=\sum_{j<m}(a_j/\alpha_j)e_{D-2^j}.
$$
第一项的输入位于头的前半部、输出在 $e_0$；
第二项输入在 $e_{D-1}$、输出位于头的后半部。
两组初始空间互相正交，两组值域也互相正交；
两个非零块的范数均为 $q_m$。所以
$$
\boxed{\|[T_N,\mathcal J_m]\|=q_m.}
\tag{3.4}
$$
零系数情形包括在内。主慢列中
$q_m\ge m^{-2}/\alpha_{m-1}$，这个范数增长极快。
(3.3) 的价值是实际局部性和两头结构，不是交换子很小。

## 4. 任意核向量的准确尾行

令 $M=\ker T_N$。对 $g\in M$，按上述头尾分解写
$$
g=\sum_{r=0}^{D-1}e_r\otimes g_r^{(m)},\qquad
g_r^{(m)}\in\mathcal H_-^{(m)}.
$$
置
$$
u_m(g)=\sum_{j<m}\frac{a_j}{\alpha_j}\,
g_{2^j-1}^{(m)}.
\tag{4.1}
$$
这是有限个尾向量之和，不是尚未证明收敛的无限尾除法。

由 $T_Ng=0$ 和 (3.3)，
$$
\boxed{
T_N\mathcal J_mg
=e_0\otimes u_m(g)-v_m\otimes g_{D-1}^{(m)}.
}
\tag{4.2}
$$
两项正交，所以
$$
\boxed{
\|T_N\mathcal J_mg\|^2
=\|u_m(g)\|^2+q_m^2\|g_{D-1}^{(m)}\|^2.
}
\tag{4.3}
$$

令
$$
T_{\ge m}^{(m)}=\sum_{j\ge m}a_jN_j^{(m)}
$$
为真实尾符号，其中 $I\otimes N_j^{(m)}=N_j^-$。
它满足 $\|T_{\ge m}^{(m)}\|\le\sum_{j\ge m}|a_j|$。
取 $T_Ng=0$ 的最高头行 $D-1$：
有限头严格下三角部分没有这一输出行；尾符号给
$T_{\ge m}^{(m)}g_{D-1}^{(m)}$；(2.2) 的借位部分给
$B^{(m)}u_m(g)$。故
$$
\boxed{
B^{(m)}u_m(g)
=-T_{\ge m}^{(m)}g_{D-1}^{(m)}.
}
\tag{4.4}
$$
从而
$$
\|B^{(m)}u_m(g)\|
\le\left(\sum_{j\ge m}|a_j|\right)
\|g_{D-1}^{(m)}\|.
\tag{4.5}
$$

对每个固定 $g$，$\|g_{D-1}^{(m)}\|=\|\Pi_{-,m}g\|\to0$。
但 $B^{(m)}$ 既有 $e_0$ 核，也没有正下界，故 (4.4)—(4.5)
不给 $\|u_m(g)\|$ 一个相应的小量估计。即使指定其垂直于 $e_0$ 的预像，
所需尾右移仍是无界算子。不能在这里形式地约掉 $B^{(m)}$。

(4.2) 和 (1.5) 还准确给
$$
B\,T_N\mathcal J_mg=-T_N\Pi_{-,m}g\longrightarrow0.
\tag{4.6}
$$
这是“右移误差的 $B$ 像很小”，不是右移误差本身趋零。

## 5. 与真正无界标准右移的关系

R200 的标准右移逆记为
$$
J_1x=\sum_{n\ge0}
\frac{x_n}{\alpha_{v_2(n+1)}}e_{n+1},
\qquad
\operatorname{Dom}J_1=
\left\{x:\sum_{n\ge0}\frac{|x_n|^2}
{\alpha_{v_2(n+1)}^2}<\infty\right\}.
$$
对每个 $x$，$\mathcal J_mx$ 正好保留上式中
$v_2(n+1)<m$ 的项。这些指标集递增并耗尽全部 $n\ge0$，所以
$$
\boxed{
x\in\operatorname{Dom}J_1
\iff \sup_m\|\mathcal J_mx\|<\infty.
}
\tag{5.1}
$$
在该域上，
$$
\mathcal J_mx\to J_1x\quad\text{强}.
\tag{5.2}
$$

若 $g\in M\cap\operatorname{Dom}J_1$，则
$$
BT_NJ_1g=T_Ng=0.
$$
因此 $T_NJ_1g=\ell_{T_N}(g)e_0$，其中 $\ell_{T_N}$ 正是 R200 的缺失行泛函。
由 (5.2) 与 $T_N$ 有界，(4.2) 的两项满足
$$
\boxed{
\|u_m(g)-\ell_{T_N}(g)e_0^{(m)}\|\to0,\qquad
q_m\|g_{D-1}^{(m)}\|\to0.
}
\tag{5.3}
$$
这里 $e_0^{(m)}$ 为该尾空间的真空；嵌入后
$e_0\otimes e_0^{(m)}$ 始终是整个边界的 $e_0$。
(5.3) 可由两项正交直接读出，未对未知域外向量使用它。

## 6. Cayley 版的准确保留形式

若改取
$$
T_Y=\sum_j a_jY_j^-,\qquad
Y_j^-=N_j^-(I+N_j^-)^{-1},\qquad
R_j=(I+N_j^-)^{-1},
$$
则 $\|R_j\|<3$。真实逆交换子恒等式给
$$
\boxed{[Y_j^-,\mathcal J_m]
=R_j[N_j^-,\mathcal J_m]R_j.}
\tag{6.1}
$$
因此
$$
[T_Y,\mathcal J_m]
=\sum_{j<m}\frac{a_j}{\alpha_j}
R_j\left[
\bigl(|0\rangle\langle2^j-1|
-|D-2^j\rangle\langle D-1|\bigr)\otimes I
\right]R_j.
\tag{6.2}
$$
所有 $j\ge m$ 项仍精确交换，并有有限界
$$
\|[T_Y,\mathcal J_m]\|
\le9\sum_{j<m}|a_j|/\alpha_j.
\tag{6.3}
$$

不能把 (6.2) 的 $R_j$ 删除：它们含真实尾进位。
所以本文只对 $T_N$ 声称 (3.3) 的局部两头公式及 (4.4) 的简单尾行；
Cayley 版保留的是带真实逆因子的准确有限和。

## 7. 当前的饱和缺口

对主慢列，R200 已证明
$$
N=\overline{BM}
=\overline{M\cap\operatorname{Dom}J_1}.
$$
本稿补充了 $\mathcal J_m$ 的完全实际块作用，以及它破坏 $M$ 的确切两头残量。
虽然 $B\mathcal J_mg\to g$ 对每个 $g\in M$ 成立，
$\mathcal J_mg$ 一般不在 $M$；(4.2) 正记录了这一点。

要从这里证明 $N=M$，仍需在适当的 $B$ 图尺度中消除 (4.2) 的残量，
或者证明 $M$ 内有足够多满足 (5.1) 的向量。
(4.4) 的尾方程及全空间 $\operatorname{Dom}J_1$ 的稠密性都没有自动提供这一步。
本文没有把极快增长的 $q_m$ 当作一致常数，也没有假设未知核向量的尾速率。
