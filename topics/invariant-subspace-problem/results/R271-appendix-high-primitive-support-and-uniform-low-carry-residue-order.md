# R271 补录：最高 carry 新核约束的高 primitive 支撑与统一低 carry 缩放的残余阶

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / r271_cost，根复核；AI-assisted GPT-6 Astra Pro。

## 0. 范围

本条证明两件事：

1. 任意有限幂零头的最高 carry 退化，若与完整强 Boolean 尾相加，
   新增核兼容性只可能出现在足够短的尾链，等价于足够高的 primitive 起始孔级。
2. 对原 N 型有限头，把全部低 carry 同时乘一个参数 $s$，最高 carry 单独用 $t$，
   则完整 Galerkin 的最高 $t$ 极点系数有一个随固定强段长度增长的 $s$ 消失阶界。

所有 Galerkin 和 MP 都在完整物理内积中；强权变换后的 primitive 分块一般非正交，
本条只用它构造可行比较向量，不把它当成正交 Galerkin 分块。
本条的渐近常数依赖固定的头、强段、基准低 carry 和 $S$；
它没有给出原移动 $m$ 的统一费用，亦不闭合普通 Hilbert ISP。

## 1. 双参数真实 N 族

固定 $m\ge3$、$n=2^{m-1}$、$d=2n=2^m$。
固定 $d_0>0$ 及一组正的基准低 carry $\bar\kappa_i$，
$0\le i\le m-3$。
为便于统一范数，可令这些基准 carry 至多 $1$；一般固定正值只改变常数。

递归定义基准旧权 $\bar d_i$，使
$\bar d_{i+1}/\bar d_i^2=\bar\kappa_i$，并对 $0<s,t\le1$ 置
$$
d_i(s)=s^{2^i-1}\bar d_i\quad(0\le i\le m-2),
$$
$$
d_{m-1}(s,t)=t\,d_{m-2}(s)^2.
\tag{1.1}
$$
于是低相邻 carry 为 $s\bar\kappa_i$，最高相邻 carry 为 $t$。

用 (1.1) 代入原 N 型有限头
$$
A_m(s,t)=\sum_{i<m}b_i B_m(s,t)^{2^i}/d_i(s,t),
\qquad b_i=(i+1)^{-2}.
\tag{1.2}
$$
在 $t=0$ 处按最高块的连续公式定义：
$$
A_m(s,t)=
\begin{pmatrix}
A_{m-1}(s)&b_{m-1}I+tV(s)\\
0&A_{m-1}(s)
\end{pmatrix}.
\tag{1.3}
$$
这里包含全部低 carry。矩阵元是 $s,t$ 的多项式，零点处有良好连续延拓。

加入固定偶数 $R\ge0$ 个完整强位，正权 $c_1,\ldots,c_R$ 固定，
$$
C(s,t)=A_m(s,t)+D_R,\qquad D_R=\sum_{\ell=1}^R c_\ell E_\ell.
$$
固定奇高度 $r\ge1$ 和 $S>0$，令
$$
X(s,t)=C(s,t)^r,\qquad
H(s,t)=\sum_{j=0}^{r-1}\frac{(C(s,t)^*)^jC(s,t)^j}{j!S^j}.
\tag{1.4}
$$
原源 $f=f_1$ 是物理一孔向量。
所有后面的 $O(\cdot)$ 都是 $s\to0^+$ 的固定参数渐近。

### 1.1 物理孔齐次性

以全部 $m+R$ 个物理位的孔数分级为 $\mathcal H_g$，
令 $\mathcal R_\lambda|_{\mathcal H_g}=\lambda^gI$。
同时缩放全部相邻 carry 时，
$$
C(\lambda s,\lambda t)
=\lambda\mathcal R_\lambda C(s,t)\mathcal R_\lambda^{-1}.
\tag{1.5}
$$
可直接核对：从第 $j$ 位向第 $i<j$ 位借位的系数是
$j-i$ 个相邻 carry 的乘积，而物理孔数变化为 $j-i-1$；
纯删除的孔数变化为 $-1$。
也可由真实权
$W_k(\lambda s,\lambda t)=\lambda^{k-\operatorname{popcount}(k)}W_k(s,t)$
逐项证明 (1.5)。

特别地
$$
C(s,0)=s\mathcal R_s C(1,0)\mathcal R_s^{-1}.
\tag{1.6}
$$
$C(s,0)$ 的 $s^a$ 系数把物理孔级 $g$ 送到 $g+a-1$；
因此 $H(s,0)$ 的 $s^b$ 系数只连接相差至多 $b$ 的孔级。

## 2. 完整退化核与最高极点

固定 $s>0$，记
$$
K(s)=\ker X(s,0),\qquad
F_0(s)=\lim_{t\to0^+}\ker X(s,t).
$$
偶 $R$、奇 $r$ 的最高 carry 完整 MP 定理给出：$t$ 的 MP 至多简单极点，
并且全部新增秩在一阶打开。
因此 $F_0(s)\subset K(s)$ 是完整真核的解析极限。

定义两个完整物理 Galerkin 解：
$$
a_{\rm full}(s)=
(P_{K(s)}H(s,0)|_{K(s)})^{-1}P_{K(s)}f,
$$
$$
a_0(s)=
(P_{F_0(s)}H(s,0)|_{F_0(s)})^{-1}P_{F_0(s)}f.
\tag{2.1}
$$
$a_0(s)$ 是原 $t>0$ Galerkin 解的 $t\to0$ 极限。
它也是 $a_{\rm full}(s)$ 在 $H(s,0)$ 内积下到 $F_0(s)$ 的正交投影；
这是两条完整 Galerkin 方程相减的直接结果。

原完整 MP 解 $q(s,t)$ 的最高极点系数为
$$
q_{-1}(s)=\lim_{t\to0}tq(s,t).
\tag{2.2}
$$
若
$$
\mathscr P(s)=\lim_{t\to0}t(X(s,t)^*)^\dagger,
\tag{2.3}
$$
则
$$
q_{-1}(s)=\mathscr P(s)\,[f-H(s,0)a_0(s)].
$$
并且 $\mathscr P(s)$ 杀掉 $\operatorname{Ran}X(s,0)^*$。
后一断言也可不依赖 Schur 公式：
将
$$
t(X(s,t)^*)^\dagger X(s,t)^*
=tP_{\operatorname{Ran}X(s,t)}
$$
取极限即得
$\mathscr P(s)X(s,0)^*=0$。
因此
$$
q_{-1}(s)
=\mathscr P(s)P_{K(s)}H(s,0)
\bigl(a_{\rm full}(s)-a_0(s)\bigr).
\tag{2.4}
$$
这里被估计的是实际极点系数，不是整个 $q(s,t)$。

## 3. 新核约束只在高 primitive 起始孔级

强尾在加权对角相似后作完整 Boolean Lefschetz 分解。
每条尾链有 primitive 起始孔数 $j$ 与链长
$$
l=R-2j+1,
$$
其物理尾孔数从 $j$ 到 $R-j$。
加权对角相似保持孔级，所以还原后的各链仍是分级子空间，
但彼此一般不在物理内积下正交。

### 引理 3.1

在一条尾链上，若
$$
l\ge d+r-1,
\tag{3.1}
$$
则最高 $t$ 退化不损失核：
$$
F_0(s)|_{\rm chain}=K(s)|_{\rm chain}.
\tag{3.2}
$$

**证明。** 更一般地，令任意 $d$ 维幂零头的 Jordan 块长为
$h_1,\ldots,h_q$，$\sum h_i=d$。
$J_{h_i}+J_l$ 的链长为
$h_i+l-1,h_i+l-3,\ldots,l-h_i+1$，因为 $l\ge d\ge h_i$。
在 (3.1) 下，每条长度至少为 $l-d+1\ge r$。
故 $r$ 次幂的核维数恰为 $rh_i$，全部头块相加为 $rd$，
与头的 Jordan 类型无关。
因此 $X(s,t)$ 在该完整块上的秩在 $t=0$ 不下降，
真核连续极限就是整个退化核。证毕。

所以只有
$l\le d+r-2$ 的短尾链可能产生新约束。
令
$$
J_*=\max\left(0,\left\lceil\frac{R-d-r+3}{2}\right\rceil\right).
\tag{3.3}
$$
这些链的 primitive 起始孔数全部至少为 $J_*$。

设 $Q_{\rm hi}$ 为所有 $j\ge J_*$ 尾链的固定代数投影，
再张量完整有限头。它与 $D_R$ 及所有 $X(s,t)$ 交换，
保持物理孔数，并杀掉所有物理总孔数小于 $J_*$ 的向量。

这个投影不被当成物理正交投影。
具体若 $D_R=T^{-1}D_{\rm unweighted}T$，可取
$$
Q_{\rm hi}=T^{-1}P_{\rm hi}T,
$$
其中 $P_{\rm hi}$ 是未加权正交链分解的相应投影。
因而
$$
\|Q_{\rm hi}\|,\ \|I-Q_{\rm hi}\|\le\kappa(T).
\tag{3.4}
$$
对原 $0<c_i\le1$，可用
$\kappa(T)=\prod_i c_i^{-1}$；
这是后续常数中的真实物理费用。

由 (3.2)，对每个 $s>0$，
$$
(I-Q_{\rm hi})a_{\rm full}(s)\in F_0(s).
\tag{3.5}
$$
本条没有断言 $H(s,0)$ 保持这些链。

## 4. 真核掉秩时仍成立的解析性与孔传播

### 引理 4.1

完整 $a_{\rm full}(s)$ 在 $s=0$ 解析，并可写
$$
a_{\rm full}(s)=\sum_{\nu\ge0}s^\nu a_\nu,\qquad
a_\nu\in\bigoplus_{g\le1+\nu}\mathcal H_g.
\tag{4.1}
$$

**证明。** 由 (1.6)，
$$
K(s)=\mathcal R_sK(1).
$$
按嵌套过滤
$K(1)\cap\bigoplus_{g\ge a}\mathcal H_g$ 选取适配基。
若一个基向量最低非零孔级为 $a$，将
$\mathcal R_s v$ 除以 $s^a$。
这些列组成多项式框架 $Z(s)$，其常数列按级独立，
所以 $Z(0)$ 满列秩。
每个 $Z_\ell$ 把列的初始级 $g$ 送入物理级 $g+\ell$。

必须区分：
$\operatorname{Ran}Z(0)=\lim_{s\to0}K(s)$，
不一定等于更大的 $\ker X(0,0)$。
本证明从未把两者混同，也不要求退化核维数不变。

完整 Galerkin 方程为
$$
a_{\rm full}(s)=Z(s)v(s),\quad
G(s)v(s)=Z(s)^*f,\quad
G(s)=Z(s)^*H(s,0)Z(s).
$$
$G(0)$ 严格正定，故 $v(s)$、$a_{\rm full}(s)$ 解析。
由 (1.6)，$H$ 的 $s^b$ 系数只改变孔级至多 $b$；
于是 $G_b$ 只连接初始级之差至多 $b$ 的列，$G_0$ 按级分块。
因为 $f$ 为一孔，$(Z(s)^*f)_b$ 只在初始级 $1-b$。
逐阶解正定方程，得到 $v_\nu$ 的初始级至多 $1+\nu$；
再乘 $Z(s)$ 即得 (4.1)。

这一步始终使用原物理 $Z^*HZ$，全部 primitive 链的混合项都在其中。证毕。

令
$$
\nu_*=\max(J_*-1,0).
$$
由 $Q_{\rm hi}$ 的孔支撑性质及 (4.1)，
$$
Q_{\rm hi}a_{\rm full}(s)=O(s^{\nu_*}).
\tag{4.2}
$$
当 $J_*=0$ 时这只是有界性；当 $J_*\ge1$ 时，
所有 $\nu<J_*-1$ 的系数均被精确杀掉。

由 (3.5)，用
$\widetilde a=(I-Q_{\rm hi})a_{\rm full}(s)$
作为 $F_0(s)$ 中的可行比较向量。
因为 $a_0$ 是真实 $H$-正交投影且 $H\ge I$，
$$
\begin{aligned}
\|a_{\rm full}(s)-a_0(s)\|
&\le\|a_{\rm full}(s)-a_0(s)\|_{H(s,0)}\\
&\le\|Q_{\rm hi}a_{\rm full}(s)\|_{H(s,0)}\\
&\le\sqrt{\|H(s,0)\|}\,
\|Q_{\rm hi}a_{\rm full}(s)\|.
\end{aligned}
\tag{4.3}
$$
固定参数下 $H(s,0)$ 在零点附近有界，故
$$
\boxed{a_{\rm full}(s)-a_0(s)=O(s^{\nu_*}).}
\tag{4.4}
$$
这是实际完整 Galerkin 的核损失界，不是代数分块上的替代方程。

## 5. 最高 pole operator 的 $s$ 次数成本

### 引理 5.1

固定 $m,R,r$ 及全部基准数据时，
$$
\|\mathscr P(s)\|=O(s^{-(2d-6)}).
\tag{5.1}
$$

**证明。** 先准确计旧头与最高参考头的真实 Jordan 相似次数。

N 型旧函数满足
$$
F_s(z)=sF_1(z/s),\qquad
\psi_s(w)=F_s^{-1}(w)=s\psi_1(w/s).
$$
旧物理权为
$$
W_j(s)=s^{j-\operatorname{popcount}(j)}\bar W_j.
$$
真实伴随链矩阵的逆元素因此为
$$
(K_s^{-1})_{kj}
=s^{\operatorname{popcount}(j)-k}
\frac{[w^k]\psi_1(w)^j}{\bar W_j},
\qquad0\le j\le k<n.
\tag{5.2}
$$
$j=0$ 列只有 $k=0$ 非零；其余 $j\ge1$ 时
$\operatorname{popcount}(j)\ge1,\ k\le n-1$。
所以
$$
\|K_s^{-1}\|=O(s^{-(n-2)}).
$$
旧头矩阵在 $s=0$ 连续且有界，故链矩阵 $K_s$ 本身有界；
于是
$$
\kappa(V_{\rm old}(s))=O(s^{-(n-2)}).
\tag{5.3}
$$

再取最高参考 $t=1$，删除最高 Boolean 项，
即 $\widehat A_s=F_s(B_m(s,1))$，维数为 $d=2n$。
其最高位物理权的 $s$ 指数为 $n-2$，比全体 carry 同缩放时少一次。
因此
$$
W_j^{\rm ref}(s)
=s^{j-\operatorname{popcount}(j)-\varepsilon(j)}
\bar W_j^{\rm ref},
$$
其中 $\varepsilon(j)$ 是最高位是否占据。
同一个旧逆芽给
$$
(\widehat K_s^{-1})_{kj}
=s^{\operatorname{popcount}(j)+\varepsilon(j)-k}
\frac{[w^k]\psi_1(w)^j}{\bar W_j^{\rm ref}}.
\tag{5.4}
$$
对非零的 $j\ge1$ 项，指数至少为 $1-(d-1)=2-d$；
$j=0$ 列仍只有常数项。
参考头矩阵在零点连续有界，故
$$
\kappa(\widehat V_s)=O(s^{-(d-2)}).
\tag{5.5}
$$

现在使用完整奇高度最高 carry 的物理剪切界。
把旧头、参考头分别变成标准 sl2 链，强尾费用、阶乘与固定 $r$ 全部计入常数；
两次剪切各支付至多一次旧头条件数，参考 MP 支付一次参考头条件数。
于是对全部 $0<t\le1$，
$$
\|(X(s,t)^*)^\dagger\|
\le C\,t^{-1}
s^{-2(n-2)-(d-2)}
=C\,t^{-1}s^{-(2d-6)}.
$$
这里 $C$ 依赖固定的完整物理强尾、基准权、$m,r$，不依赖 $s,t$。
乘 $t$ 后取极限即得 (5.1)。证毕。

## 6. 真实最高极点系数的残余阶

由 (2.4)、(4.4)、(5.1)，且固定参数下 $H(s,0)$ 有界，
得到：

### 定理 6.1

对上述原 N 型双参数族，
$$
\boxed{
q_{-1}(s)
=O\!\left(s^{\nu_*-(2d-6)}\right),\qquad
\nu_*=\max(J_*-1,0).
}
\tag{6.1}
$$
若 $J_*\ge1$，并使用偶 $R$、偶 $d$、奇 $r$ 的整数奇偶关系，
则
$$
\boxed{
q_{-1}(s)
=O\!\left(s^{(R-5d-r+13)/2}\right).
}
\tag{6.2}
$$
这是最高 $t^{-1}$ 系数的阶数，不是整个 $q(s,t)$ 的同阶结论。

### 原两级 N 头的特例

新 $m=3,d=8,r=3$ 时，只有一个低 carry $s$，基准可取 $1$；
最高为独立 $t$。
对固定偶 $R\ge10$，
$$
\boxed{q_{-1}(s)=O_{R,c,S}(s^{(R-30)/2}).}
\tag{6.3}
$$
例如 $R=32$ 给至少 $s^1$，$R=64$ 给至少 $s^{17}$。
对 $R=8$，同一个较弱的指数写法也成立，但仅给负幂上界。
该特例与无强段时的真实 $m=3$ 大费用不矛盾；
增长强段把最高新约束推到更高的 primitive 起始孔级。

本条没有给出使原 $s=e^{-1070}$ 落入某个统一有效邻域的数值常数；
不能把固定 $R$ 的 $O$ 估计直接当成该有限值的显式费用。

## 7. 原移动参数仍未支付的两种尺度问题

(6.1)–(6.3) 是固定基准数据的严格消失阶。
它们没有自动变成原 $m\to\infty$ 的预算：

1. 若取统一缩放 $s$ 为最大的低 carry，例如固定
   $\kappa_0=e^{-1070}$，其余基准设为原 $\kappa_i/s$，
   则所有基准不超过 $1$，但依赖 $m$ 的常数可能包含其越来越小的逆权。
   即使暂略常数，$s^{c d}$ 也只有 $O(d)$ 的负对数，
   不能压过最高 $t$ 的 $O(d^4)$ 逆损失。
2. 若取 $s$ 为最小旧 carry，使其自身负对数达到 $O(d^4)$，
   较低层的基准 carry $\kappa_i/s$ 便非常大。
   固定基准的 $O$ 常数与有效邻域可能吃掉形式消失阶，
   本条没有证明这种选择可用。

仅由 primitive 支撑得到的粗门，在 $R=d$ 且 $r\ge3$ 时没有正阶余量。
取 $R$ 约为 $6d$、$Q$ 约为 $8d$ 是可继续检查的候选尺度，强段的对数条件数为 $O(d\log d)$；同一个 $Q$ 的全部几何、nilpotence cut 和分离高度带仍须按原接口逐项设定。单纯改善形式阶数不解决上述真实多尺度问题。

下一步需要逐 carry 的多参数分级，
或证明原源传播中的强位权因子能与相似成本抵消。
本条没有用单参数形式阶数替代这项未完成的实际估计。
