# R185：慢加性符号的边界无限核与实际非标准闭主理想

日期：2026-11-12（UTC）。作者：l2_moments；根与 critical_kernel 已独立核验核心构造。
状态：完整证明。本文证明实际负整数边界非 unicellular，并在原实际范数代数中构造不包含任何 $A^n$ 的非零闭主理想。它没有构造原 $H$ 上的坏向量或解决完整 ISP。

## 1. 结论

沿用
$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},\qquad
N_j=A^{2^j}/d_j,\qquad d_j=\|A^{2^j}\|.
$$
取固定慢系数
$$
a_j=\frac1{(j+1)^2},\qquad
M=\sum_{j\ge0}a_j\le2,
$$
并定义实际范数收敛级数
$$
\boxed{S=\sum_{j\ge0}a_jN_j\in\mathcal A.}
\tag{1.1}
$$

R174 的负整数边界表示 $\pi_-$ 作用于
$\mathscr H_-=\ell^2(\mathbb N_0)$，且
$$
B=\pi_-(A),\qquad
Be_0=0,\qquad
Be_n=\alpha_{v_2(n)}e_{n-1}\quad(n\ge1).
$$
置
$$
\mathsf N_j=\pi_-(N_j)=B^{2^j}/d_j,\qquad
T=\pi_-(S)=\sum_ja_j\mathsf N_j.
\tag{1.2}
$$

**主定理。**

1. 存在明确递归构造的 $g\in\mathscr H_-$，满足
   $$
   Tg=0,\qquad g\perp e_0,\qquad g\ne0.
   $$
   其 $e_{16}$、$e_{32}$ 系数已在初始步骤固定，之后永久保留。
2. $g$ 有无限支持。因而 $\ker T$ 是真无限维闭 $B$ 不变子空间；$B$ 及 $B^*$ 都非 unicellular。
3. 原实际范数代数中的闭主理想
   $$
   J=\overline{S\mathcal A}^{\|\cdot\|}
   $$
   非零、具有无限余维，且
   $$
   \boxed{
   J\subsetneq I_1,\qquad A^n\notin J\quad(n=0,1,2,\ldots),
   }
   \tag{1.3}
   $$
   其中 $I_r=\overline{A^r\mathcal A}$。因此 $J$ 不含任何标准理想 $I_n$，且本身非标准。
4. 与此相容，原 $H=L^2(\mathbb Z_2)$ 上的同一个 $S$ 仍单射、值域稠密，$S1$ 循环。边界核并不通过 R174 所排除的有界交织传回原空间。

证明的核心是“有限头残差—远处有限块纠错—更小真实残差”的严格迭代。所有纠错只用有限维线性代数。

## 2. 边界的实际进位公式与有限头

在 $\mathscr H_-$ 中，将 $n$ 的二进位1视为相对于全物理1真空的孔。定义纯孔消灭算子
$$
\mathsf E_je_n=
\begin{cases}
e_{n-2^j},&n_j=1,\\
0,&n_j=0.
\end{cases}
$$
其通常伴随 $\mathsf E_j^*$ 创建第 $j$ 个孔。

R44/R174 的实际递推在该表示中为
$$
\boxed{
\mathsf N_j
=\mathsf E_j+\eta_j\mathsf E_j^*\mathsf N_{j+1},
\qquad
\|\mathsf N_j\|=1,\qquad
\eta_j=\alpha_{j+1}/\alpha_j
\le e^{-770\,16^j}.
}
\tag{2.1}
$$
不同位的纯算子交换。特别
$$
\|\mathsf N_j-\mathsf E_j\|\le\eta_j.
\tag{2.2}
$$

将 (2.1) 展开至整数位 $K>i$，得到真正算子恒等式
$$
\begin{aligned}
\mathsf N_i={}&
\sum_{\ell=i}^{K-1}
\frac{\alpha_\ell}{\alpha_i}
\mathsf E_i^*\cdots\mathsf E_{\ell-1}^*\mathsf E_\ell\\
&+\frac{\alpha_K}{\alpha_i}
\mathsf E_i^*\cdots\mathsf E_{K-1}^*\mathsf N_K.
\end{aligned}
\tag{2.3}
$$
空乘积取 $I$。下文的空坐标间隔估计直接来自此式，而非仅用固定低位的全局 $\eta_i$ 误差。

记有限头空间
$$
\mathscr F_m=\operatorname{span}\{e_n:0\le n<2^m\}.
$$
它对 $B$、$T$ 不变。若 $i<m$，用 $\mathsf N_i^{[m]}$ 表示 (2.3) 在 $K=m$ 时的有限和。
尾全真空使余项严格为零，因此
$$
T|_{\mathscr F_m}=T_m
=\sum_{i<m}a_i\mathsf N_i^{[m]},
\qquad \|T_m\|\le M\le2.
\tag{2.4}
$$
这里没有近似。

置 $d=2^m$。$T_m$ 是 $B|_{\mathscr F_m}$ 的一个无常数项多项式，所以
$$
\boxed{T_m^d=0.}
\tag{2.5}
$$
其最低项为 $(a_0/d_0)B|_{\mathscr F_m}$，系数非零。
因此它是这个单 Jordan 链加权后移乘一个可逆的有限解析因子，从而
$$
\boxed{\ker T_m=\operatorname{span}\{e_0\}.}
\tag{2.6}
$$
具体地，写 $T_m=B_mU_m(B_m)$，$U_m(0)=a_0/d_0\ne0$；
$U_m(B_m)$ 可逆且与 $B_m$ 交换，故核与 $\ker B_m$ 相同。

## 3. 远处纯块的逐次数右逆

固定 $m\ge2$，置
$$
d=2^m,\qquad L=64d.
\tag{3.1}
$$
使用恰含 $L$ 位的新块
$$
\mathcal B=[L,2L).
$$
该块的纯消灭算子为
$$
D_{\mathcal B}=\sum_{i=L}^{2L-1}a_i\mathsf E_i,
\qquad
C_{\mathcal B}=D_{\mathcal B}^*
=\sum_{i=L}^{2L-1}a_i\mathsf E_i^*.
$$
各 $a_i$ 为正实数。按块内孔数分成齐次空间 $\mathscr K_q$。

令
$$
\sigma^2=\sum_{i=L}^{2L-1}a_i^2.
$$
因为 $i+1\le2L$，
$$
\sigma^2\ge\frac{L}{(2L)^4}=\frac1{16L^3},
\qquad
\max_{i\in\mathcal B}a_i^2\le L^{-4}.
\tag{3.2}
$$

一位关系给
$$
D_{\mathcal B}C_{\mathcal B}
-C_{\mathcal B}D_{\mathcal B}
=\sigma^2I-2\sum_{i\in\mathcal B}a_i^2P_i,
\tag{3.3}
$$
其中 $P_i$ 投影到第 $i$ 位有孔的空间。
若 $v\in\mathscr K_q$，则 $\sum_i\|P_iv\|^2=q\|v\|^2$。
因此
$$
\begin{aligned}
\|C_{\mathcal B}v\|^2
&=\|D_{\mathcal B}v\|^2
+\sigma^2\|v\|^2-2\sum_i a_i^2\|P_iv\|^2\\
&\ge(\sigma^2-2qL^{-4})\|v\|^2.
\end{aligned}
$$
对 $0\le q\le d$，由 $L=64d$，
$$
\sigma^2-2qL^{-4}
\ge\frac1{16L^3}-\frac{2d}{L^4}
=\frac1{32L^3}.
$$
置
$$
\boxed{\delta=(32L^3)^{-1/2}.}
\tag{3.4}
$$
于是 $C_{\mathcal B}:\mathscr K_q\to\mathscr K_{q+1}$
在这些次数上有左界 $\delta$。

在有限维空间中，其伴随
$D_{\mathcal B}:\mathscr K_{q+1}\to\mathscr K_q$ 满射，
且存在范数不超过 $\delta^{-1}$ 的右逆。可明确取
$$
R_q=C_q(C_q^*C_q)^{-1},
\qquad C_q=C_{\mathcal B}|_{\mathscr K_q}.
\tag{3.5}
$$
这给 $D_{\mathcal B}R_q=I$ 和 $\|R_q\|\le\delta^{-1}$。

令 $h_0$ 是新块的全真空单位向量，并递归
$$
h_k=R_{k-1}h_{k-1}\qquad(1\le k\le d-1).
$$
则
$$
\boxed{
h_k\in\mathscr K_k,\qquad
D_{\mathcal B}h_k=h_{k-1},\qquad
\|h_k\|\le\delta^{-k}.
}
\tag{3.6}
$$
不同 $k$ 的 $h_k$ 正交。
所有对象均在有限块内；没有使用无限纯消灭算子的全空间有界右逆。

## 4. 精确模型纠错及放大常数

把 $\mathscr F_m$ 放在低位 $[0,m)$，让间隔 $[m,L)$ 全部无孔，再使用新块 $[L,2L)$。所有更高位也无孔。
所得有限维子空间记为 $\mathscr U_{m,L}\subseteq\mathscr F_{2L}$。

在这个空间中考虑纯块模型
$$
\mathcal L=T_m\otimes I+I\otimes D_{\mathcal B}.
\tag{4.1}
$$
对给定 $v\in\mathscr F_m$，定义实际有限向量
$$
\boxed{
V=\sum_{k=0}^{d-1}(-1)^k T_m^kv\otimes h_k,
}
\tag{4.2}
$$
其中所有未写出的位取无孔真空。

由 (3.6)，$I\otimes D_{\mathcal B}$ 项从 $k=1$ 开始，
恰与 $T_m\otimes I$ 项逐项抵消；
最后剩下的 $T_m^dv\otimes h_{d-1}$ 由 (2.5) 为零。所以
$$
\boxed{\mathcal L V=0.}
\tag{4.3}
$$

记 $\varepsilon=\|T_mv\|$。由 $\|T_m\|\le2$，
$$
\|T_m^kv\|\le2^{k-1}\varepsilon\qquad(k\ge1).
$$
$k=0$ 项正是原来的 $v$。其余项按新块孔数正交，故
$$
\begin{aligned}
\|V-v\|^2
&\le\varepsilon^2
\sum_{k=1}^{d-1}2^{2(k-1)}\delta^{-2k}\\
&\le\varepsilon^2 d\,\delta^{-2}
(2\delta^{-1})^{2(d-2)}.
\end{aligned}
\tag{4.4}
$$
这里将 $v$ 与它的全真空延拓视为同一个边界向量。

又
$$
\delta^{-1}=\sqrt{32}(64d)^{3/2}
=2^{23/2}d^{3/2}<2^{12}d^{3/2}.
$$
因此对 $m\ge2$，
$$
\sqrt d\,\delta^{-1}(2\delta^{-1})^{d-2}
\le (2^{13}d^{3/2})^d
\le \exp(8m2^m).
$$
最终得到统一的一步放大界
$$
\boxed{
\|V-v\|\le e^{8m2^m}\|T_mv\|.
}
\tag{4.5}
$$

每个 $k\ge1$ 项在新块至少有一个孔。
于是这次修正的所有整数支持指标均至少为 $2^L$，严格保留原来低于 $2^L$ 的全部系数，特别不改变 $e_0$ 系数。
这比仅有范数近似更强。

## 5. 空间隔使真实误差超小

现在比较真实 $T$ 与模型 $\mathcal L$。以下估计对整个 $\mathscr U_{m,L}$ 统一成立。

### 5.1 低位与空白间隔

若 $i<m$，把 (2.3) 展开到 $K=L$。
中间 $m\le\ell<L$ 的每项均含 $\mathsf E_\ell$，它在空白间隔上严格杀掉输入。
因此在 $\mathscr U_{m,L}$ 上，
$$
\|(\mathsf N_i-\mathsf N_i^{[m]})|_{\mathscr U_{m,L}}\|
\le\frac{\alpha_L}{\alpha_i}.
\tag{5.1}
$$
若 $m\le i<L$，有限和的全部消灭位都在空白间隔内，因而
$$
\|\mathsf N_i|_{\mathscr U_{m,L}}\|
\le\frac{\alpha_L}{\alpha_i}.
\tag{5.2}
$$
因 $\alpha_i$ 随 $i$ 递减，对全部 $i<L$，
$$
\frac{\alpha_L}{\alpha_i}\le\eta_{L-1}.
$$
所以低位加间隔的总误差至多 $M\eta_{L-1}$。

这里没有对固定低位 $i$ 直接使用全局误差 $\eta_i$；
所有有效 borrow 必须跨过空白间隔，到达至少第 $L$ 位，才可能非零。

### 5.2 新块与块后

对 $L\le i<2L$，直接用 (2.2)：
$$
\|\mathsf N_i-\mathsf E_i\|\le\eta_i\le\eta_L.
$$
相应总误差至多 $M\eta_L$。

对 $i\ge2L$，$\mathsf N_i=B^{2^i}/d_i$ 在
$\mathscr F_{2L}$ 上严格为零，因而没有未支付的块后尾项。

综上，
$$
\boxed{
\|(T-\mathcal L)|_{\mathscr U_{m,L}}\|
\le M(\eta_{L-1}+\eta_L)
\le2M\eta_{L-1}\le4\eta_{L-1}.
}
\tag{5.3}
$$
结合模型零等式 (4.3)，
$$
\boxed{\|TV\|\le4\eta_{L-1}\|V\|.}
\tag{5.4}
$$

## 6. 一步残差改善与全程数值预算

对 $m\ge2$ 设
$$
\epsilon_m=e^{-40\,4^m}.
$$
假设
$$
v\in\mathscr F_m,\qquad
\|v\|\le2,\qquad
\|Tv\|\le\epsilon_m.
\tag{6.1}
$$
因 $Tv=T_mv$ 精确成立，(4.5) 给
$$
\|V-v\|
\le\exp(-40\,4^m+8m2^m)
\le e^{-20\,4^m}.
\tag{6.2}
$$
最后一步仅用 $8m2^m\le20\,4^m$。

令
$$
m'=2L=128\,2^m.
\tag{6.3}
$$
则 $V\in\mathscr F_{m'}$，并由 (6.2) 有 $\|V\|\le3$。
由 (5.4) 及实际 $\eta$ 上界，
$$
\begin{aligned}
\|TV\|
&\le12\eta_{L-1}\\
&\le\exp\left(\log12-\frac{770}{16}\,4^{m'}\right)\\
&\le e^{-40\,4^{m'}}=\epsilon_{m'}.
\end{aligned}
\tag{6.4}
$$
因为 $770/16=48.125>40$，有固定且巨大的余量。

所以该有限维纠错把残差预算从 $\epsilon_m$
提升为对应更大真实头窗口的 $\epsilon_{m'}$，
同时只移动至多 $e^{-20\,4^m}$。
下一步的放大常数虽很大，却始终被新的预算压住。

## 7. 一个具体非零初始向量

取 $j=4$、$k=5$，记
$$
a_4=\frac1{25},\qquad a_5=\frac1{36},
$$
并设
$$
\boxed{
v_0=\frac{a_5e_{16}-a_4e_{32}}
{\sqrt{a_4^2+a_5^2}},\qquad m_0=6.
}
\tag{7.1}
$$
则 $v_0\in\mathscr F_6$、$\|v_0\|=1$、$v_0\perp e_0$。
纯消灭和 $\sum_i a_i\mathsf E_i$ 在 $v_0$ 上恰好抵消。

对单孔向量，实际递推 (2.3) 给
$$
\mathsf N_ie_{2^j}=
\begin{cases}
(\alpha_j/\alpha_i)e_{2^j-2^i},&i<j,\\
e_0,&i=j,\\
0,&i>j.
\end{cases}
\tag{7.2}
$$
因此
$$
\left\|\left(T-\sum_i a_i\mathsf E_i\right)e_{2^j}\right\|
\le\sum_{i<j}a_i\frac{\alpha_j}{\alpha_i}
\le M\eta_{j-1}.
$$
在 (7.1) 中两个标量系数模长都至多1，所以
$$
\boxed{
\|Tv_0\|\le M(\eta_3+\eta_4)
\le4\eta_3
\le4e^{-770\,16^3}
<e^{-40\,4^6}.
}
\tag{7.3}
$$
数值指数分别为 $770\cdot16^3=3153920$ 和 $40\cdot4^6=163840$，
故最后一个严格不等式无临界常数问题。

## 8. 无限纠错收敛到真实核

递归定义
$$
m_{n+1}=128\,2^{m_n},
$$
并用 §§3–6 的有限维公式把 $v_n$ 变为 $v_{n+1}$。
每次右逆均按 (3.5) 固定，所以这不是仅靠选择公理存在的序列。

由 (6.2)，
$$
\|v_{n+1}-v_n\|\le e^{-20\,4^{m_n}}.
\tag{8.1}
$$
$m_n$ 严格增长，且 $m_n\ge m_0+n$，因而
$$
\sum_{n\ge0}e^{-20\,4^{m_n}}
\le\sum_{n\ge0}e^{-20\,4^{m_0+n}}
<\frac14.
\tag{8.2}
$$
从 $\|v_0\|=1$ 出发，全部 $\|v_n\|<5/4<2$。
所以 (6.1) 中用于下一步的范数假设始终保持；
由 (6.4) 同时归纳得到
$$
\|Tv_n\|\le e^{-40\,4^{m_n}}\longrightarrow0.
\tag{8.3}
$$

式 (8.1)—(8.2) 说明 $v_n$ 在 $\mathscr H_-$ 中强收敛到某个 $g$。
$T$ 有界，故
$$
Tg=\lim_nTv_n=0.
$$
每次修正均包含一个新块孔，严格保留先前的低头系数。
特别
$$
\boxed{
\langle g,e_{16}\rangle
=\frac{a_5}{\sqrt{a_4^2+a_5^2}}\ne0,\quad
\langle g,e_{32}\rangle
=-\frac{a_4}{\sqrt{a_4^2+a_5^2}},\quad
\langle g,e_0\rangle=0.
}
\tag{8.4}
$$
因此 $g\ne0$ 且 $g\perp e_0$。
此外 $\|g-v_0\|<1/4$，所以非零性也有独立范数保证。

若 $g$ 有有限支持，则它属于某个 $\mathscr F_m$，
而 $Tg=T_mg=0$ 与 (2.6) 会迫 $g\in\mathbb Ce_0$，矛盾。
所以
$$
\boxed{g\text{ 有无限支持，且 }B^ng\ne0\text{ 对所有 }n\ge0.}
\tag{8.5}
$$
最后一句也直接来自所有权非零、$\ker B^n=\operatorname{span}\{e_0,\ldots,e_{n-1}\}$。

## 9. 边界真无限维闭不变空间

由于 $T$ 与 $B$ 交换，$M_-=\ker T$ 是闭 $B$ 不变空间。
它包含 $e_0$ 和 (8.4) 的无限支持 $g$，但
$$
Te_1=a_0e_0=e_0\ne0,
$$
所以 $M_-\ne\mathscr H_-$。

该空间不可能有限维。
否则 $B|_{M_-}$ 是有限维拟幂零算子，从而某个幂为零，
将迫 $g\in\ker B^n$，与 (8.5) 矛盾。
因此
$$
\boxed{0<\dim M_-=\infty,\qquad M_-\subsetneq\mathscr H_-.}
\tag{9.1}
$$

更直接地，$M_-$ 与标准二维根旗
$\operatorname{span}\{e_0,e_1\}$ 不可比较：
$e_1\notin M_-$，而无限支持 $g$ 不在该旗中。
所以边界 $B$ 的闭不变格不全序，即 $B$ 非 unicellular。
取正交补便得到 $B^*$ 也非 unicellular。

这是真正的实际权构造，没有套用单调 Donoghue 条件，
也不依赖此前“非 strictly cyclic”这个较弱障碍。

## 10. 原实际范数代数的非标准闭主理想

回到原实际 $S$，令
$$
J=\overline{S\mathcal A}^{\|\cdot\|}.
$$
$S$ 的形式首项是 $(a_0/d_0)A$，故 $S\ne0$、$\operatorname{ord}S=1$，
且 $0\ne J\subseteq I_1$。

$\pi_-$ 是连续含幺表示。对每个 $Q\in\mathcal A$，
$$
\pi_-(SQ)g=\pi_-(Q)Tg=0.
$$
取范数闭包后，
$$
\pi_-(J)g=0.
\tag{10.1}
$$
若某个 $A^n\in J$，则 (10.1) 给 $B^ng=0$，
与 (8.5) 矛盾。因此所有 $n\ge0$ 都有
$$
\boxed{A^n\notin J.}
\tag{10.2}
$$

特别 $A\notin J$，所以 $J\subsetneq I_1$。
又任何标准 $I_n$ 都包含 $A^n$，故 $J$ 不含任何标准 $I_n$。
由于 $S$ 首阶1，$J$ 也不可能等于别的标准理想。

$J$ 还具有无限余维。若 $\mathcal A/J$ 有限维，
其中 $A+J$ 的谱半径不超过 $A$ 的零谱半径，
故它是有限维拟幂零元，某个幂为零。
这会给 $A^n\in J$，再次矛盾。

结合 R179，可以明确得到
$$
\boxed{J\cap\mathcal T=\{0\},}
\tag{10.3}
$$
其中 $\mathcal T$ 是实际快尾子代数：
若有非零 $F\in J\cap\mathcal T$，R179 的标准闭主理想结论会给
$A^{\operatorname{ord}F}\in J$。
因此本例实际实现了“稠密快子代数与某个非零闭理想只有零交”，
并否定“每个非零范数闭理想都含一个 $A^n$”的猜想。

## 11. 为什么原 Hilbert 空间的核仍为零

对任意 dyadic 根 $\zeta$，设其阶为 $2^m$。
则
$$
\gamma_\zeta S-S
=\sum_{j<m}a_j(\zeta^{2^j}-1)N_j
$$
是有限真解析多项式。
当 $\zeta\ne1$ 时，其最低项为
$$
\frac{a_0(\zeta-1)}{d_0}A,
$$
所以差为 $A$ 乘一个真正解析单位。

R122 的实际加性 gauge 排核定理因而适用：
$$
\boxed{
\ker_H S=0,\qquad \overline{SH}=H,\qquad S1\text{ 对 }A\text{ 循环}.
}
\tag{11.1}
$$
也可先由 R122 得单射，再用实际 $C$ 对称得到稠密像。

(11.1) 与边界 (9.1) 不矛盾。R174 已证明原非零闭 $A$ 不变限制与负整数边界之间不存在非零有界交织；C* 忠实表示本身不要求两个表示中同一元素具有相同的核。

本稿完成的是边界无限维不变空间和原范数代数非标准闭理想的具体构造。
原 $H$ 的一般闭不变格、慢 Bell 共振核及完整 Hilbert 不变子空间问题仍然开放。

## 12. 使用的输入

- R44/R174：真实进位递推、负整数边界、归一化范数及 $\eta_j$ 的超快上界。
- R32：实际范数代数的形式首阶与字符。
- R122：原 $H$ 上有限解析 gauge 差的单射稠密结论。
- R179：仅用于推论 (10.3)；主构造、非标准理想及不含任何幂的结论不依赖 R179。

有限块右逆、全部放大常数、空坐标间隔误差及无限纠错收敛已在本文自含证明。
