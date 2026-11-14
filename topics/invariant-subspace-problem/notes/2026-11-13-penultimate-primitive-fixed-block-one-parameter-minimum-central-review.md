# 任意异权头的倒数第二出生层：单参数完整最小逆

- 日期：2026-11-13
- 作者：AI 辅助研究；central_review
- 状态：已证明；root 已独立核验 primitive 递推、有限差分、完整最小逆、端点及积分公式
- 范围：任意多个正异权头位加等权池的置换固定 primitive 块；一般相邻上界仍未由本稿证明

## 1. 模型与真正的 primitive 块

取若干个独立头位和等权池：
$$
q\ge2,\qquad L\ge q,\qquad
D=\sum_{i=1}^q a_iE_i+D_{\rm w},
\qquad a_i>0.
$$
池有
$$
L
$$
个位，权均为一。池的未归一对称向量记为
$$
w_j=\sum_{|J|=j}e_J,\qquad
\|w_j\|^2=\binom Lj,\qquad
D_{\rm w}w_j=(L-j+1)w_{j-1}.
$$
本稿固定出生与最高合法阶
$$
s=q-1,\qquad N=L+q,\qquad h=N-2s=L-q+2.
$$

对头的缺失集合，写
$$
R\subseteq[q],\qquad r=|R|,\qquad
a_R=\prod_{i\in R}a_i.
$$
固定坐标向量为
$$
f=(f_1,\ldots,f_q)\in\mathbb C^q,\qquad
s_R(f)=\sum_{i\in R}\frac{f_i}{a_i},\qquad s_\varnothing(f)=0.
$$
定义 primitive 源
$$
\mathcal E f=
\sum_{\varnothing\ne R\subseteq[q]}
(-1)^{r-1}
\frac{a_R}{\binom L{r-1}}\,
s_R(f)\,e_{[q]\setminus R}w_{r-1}.
\tag{1.1}
$$
其中缺失单个位时的顶层系数恰为相应坐标。删除一位的递推给
$$
D\mathcal E f=0.
$$
具体地，固定一个输出头集合。池删除乘上
$$
L-r+2,
$$
而全部头删除项合并为相应的缺失头和；使用
$$
\binom L{r-1}
=\frac{L-r+2}{r-1}\binom L{r-2}
$$
即得相消。也可从下节有限差分公式在零阶及一次删除的特例直接核验。

池置换固定的第出生层有全部非满头集合（这里第出生层指物理孔数为 $s=q-1$ 的整层固定块），共
$$
2^q-1
$$
维。其 primitive 核准确为
$$
q
$$
维，由 (1.1) 参数化：满到只缺一个头的系数任意，较低头系数被非零池删除逐次唯一决定。因此没有把固定 primitive 块当成全体 primitive 空间。

对合法阶，仍按完整空间定义
$$
F_n=\frac{D^n(D^*)^n|_{\mathcal H_s}}{(n!)^2},
\qquad
\Gamma_n=P_{\ker D\cap\mathcal H_s}F_n^{-1}
\big|_{\ker D\cap\mathcal H_s},
\qquad 0\le n\le h.
\tag{1.2}
$$
有限正权 incidence 的满射保证所有完整逆存在。该满射也可由有限等权 Lefschetz 链及正对角去权直接证明。池置换群同时约化完整 Gram、完整逆和 primitive 压缩。

本稿计算的矩阵是
$$
H_n=\mathcal E^*F_n^{-1}\mathcal E.
\tag{1.3}
$$
源坐标一般非正交；实际压缩算子的坐标是
$$
H_0^{-1}H_n,
$$
不能将这个因子省掉。

## 2. 内部各阶的全部解只差一个复参数

先取
$$
1\le n<h.
$$
此时输入的池固定空间包含全部头集合，因为
$$
0\le n+r-1\le L\qquad(0\le r\le q).
$$
定义带一个自由复参数的向量
$$
u_n(f,z)=
\sum_{R\subseteq[q]}
(-1)^{r-1}
\frac{a_R}{\binom L{n+r-1}}\,
\bigl(s_R(f)-z\bigr)
e_{[q]\setminus R}w_{n+r-1}.
\tag{2.1}
$$
空集合项准确解读为
$$
\frac{z}{\binom L{n-1}}\ e_{[q]}w_{n-1}.
$$
因此并未使用负阶乘或负占据数。

**引理 1。** 对全部参数，
$$
\boxed{
\frac{D^n}{n!}u_n(f,z)=\mathcal E f.
}
\tag{2.2}
$$

给出完整逐集合核验。固定目标缺失集合，初始缺失集合必须包含于它。若初始缺失集合的大小为若干整数，则删除头的数目是两者大小之差。头权合并为目标缺失集合的乘积。弱池二项式与 (2.1) 相消后，目标系数是
$$
\frac{a_R}{L^{\underline{r-1}}}
\sum_{T\subseteq R}
(-1)^{|T|-1}
(n+|T|-1)^{\underline{r-1}}
\bigl(s_T(f)-z\bigr).
\tag{2.3}
$$
下降阶乘为零的项准确对应不合法的删除次数。

关于子集大小的多项式
$$
P(\ell)=(n+\ell-1)^{\underline{r-1}}
$$
是首一的次数为目标缺失数减一的多项式。对全部子集求和时，常数参数项被高一阶有限差分杀掉：
$$
\sum_{\ell=0}^r
(-1)^\ell\binom r\ell P(\ell)=0.
$$
对于线性和中的固定头指标，只求含该指标的子集，得到
$$
\sum_{\ell=0}^{r-1}
(-1)^\ell\binom{r-1}\ell P(\ell+1)
=(-1)^{r-1}(r-1)!.
$$
所以 (2.3) 恰为 (1.1)，证明 (2.2)。

该族也是池固定空间中的全部解。完整映射满射，故置换平均使其固定部分仍满射。输入固定空间维数为
$
2^q,
$
目标固定空间维数为
$$
2^q-1.
$$
核只有一维，而空集合项随参数非平凡变化，所以 (2.1) 穷尽整个仿射解空间。

最后，全 Hilbert 空间的唯一最小解必被池置换群固定：对任何可行解作正交平均，输出不变且范数不增加。其他孔层的无用分量也可先删去。因此在参数上取真正的最小值，所得就是完整空间的 Moore–Penrose 解，不是某个预先限制的试探上界。

## 3. 精确单参数 Gram 公式及两端

不同头集合和池占据向量相互正交。利用未归一池向量的真实范数，(2.1) 给
$$
\boxed{
f^*H_nf
=
\min_{z\in\mathbb C}
\sum_{R\subseteq[q]}
\frac{a_R^2}{\binom L{n+|R|-1}}
\left|s_R(f)-z\right|^2,
\qquad 1\le n<h.
}
\tag{3.1}
$$
全部分母严格为正。

零阶直接是源的实际 Gram：
$$
\boxed{
f^*H_0f=
\sum_{\varnothing\ne R\subseteq[q]}
\frac{a_R^2}{\binom L{|R|-1}}|s_R(f)|^2.
}
\tag{3.2}
$$
这里没有可优化的常数参数。

最高阶的输入中，只有全缺失头的那一项不合法，因为其池占据数会超过池的大小。准确的唯一解是，在 (2.1) 中取
$$
z=s_{[q]}(f)
$$
并删去全缺失集合项。也就是
$$
\boxed{
f^*H_hf=
\sum_{R\subsetneq[q]}
\frac{a_R^2}{\binom L{h+|R|-1}}
\left|s_R(f)-s_{[q]}(f)\right|^2.
}
\tag{3.3}
$$
所有保留项的池占据数都合法。

这条最高阶公式仍可直接按 (2.3) 验证。对全缺失目标，有限差分和中唯一被删的项恰乘零；其余目标从不读取该项。固定输入、输出维数此时同为
$$
2^q-1.
$$
完整满射经过置换平均后仍满射，因此这个固定解唯一，进而是完整空间的最小解。

## 4. 准确的秩一 Schur 形式

对内部阶，记
$$
\omega_R=\frac{a_R^2}{\binom L{n+|R|-1}},
\qquad
v_R=\left(\frac{1_{i\in R}}{a_i}\right)_{i=1}^q,
$$
$$
M_n=\sum_R\omega_R,\qquad
b_n=\sum_R\omega_Rv_R,\qquad
A_n=\sum_R\omega_Rv_Rv_R^*.
$$
完成平方得到
$$
\boxed{
H_n=A_n-\frac{b_nb_n^*}{M_n}.
}
\tag{4.1}
$$
全部头权为正，所以这是一个真实非退化的正 Gram。

在源坐标中，任何相邻算子序必须按
$$
\boxed{
\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n
\le c\,\Gamma_{n-1}
\quad\Longleftrightarrow\quad
H_nH_{n+1}^{-1}H_n\le c\,H_{n-1}
}
\tag{4.2}
$$
读取。这里使用实际坐标算子在复合后准确消去的源 Gram，而不是把非正交坐标直接当成正交坐标。

因此对任意多个头位，这个出生层的相邻问题已经化为显式的小维矩阵族。它无需再求一个维数指数增长的完整逆，但仍保留一般非交换矩阵乘积。

## 5. Beta 积分与逐头 Bernoulli 恒等式

内部阶的权有准确积分：
$$
\frac1{\binom L{n+r-1}}
=
(L+1)\int_0^\infty
\frac{t^{n+r-1}}{(1+t)^{L+2}}\,dt.
\tag{5.1}
$$
合法内部区间保证两端可积，包括最大缺失集合。

置
$$
x_i=f_i/a_i,\qquad
P(t)=\prod_{i=1}^q(1+a_i^2t),\qquad
p_i(t)=\frac{a_i^2t}{1+a_i^2t}.
$$
对固定正参数，把头指标视为相互独立的 Bernoulli 变量，直接展开均值与方差：
$$
\begin{aligned}
&\sum_{R\subseteq[q]}a_R^2t^{|R|}
\left|\sum_{i\in R}x_i-z\right|^2\\
&\quad=
P(t)\left[
\sum_{i=1}^qp_i(t)(1-p_i(t))|x_i|^2
+\left|\sum_{i=1}^qp_i(t)x_i-z\right|^2
\right].
\end{aligned}
\tag{5.2}
$$
因此
$$
\boxed{
\begin{aligned}
f^*H_nf
=(L+1)\min_{z\in\mathbb C}
\int_0^\infty \frac{t^{n-1}P(t)}{(1+t)^{L+2}}
\left[
\sum_i p_i(t)(1-p_i(t))|x_i|^2
+\left|\sum_i p_i(t)x_i-z\right|^2
\right]dt.
\end{aligned}
}
\tag{5.3}
$$
还保留特殊的微分恒等式
$$
p_i(t)(1-p_i(t))=t\,p_i'(t).
\tag{5.4}
$$
这是后续若要积分分部时可使用的真实结构，并非一个已完成的相邻序证明。

## 6. 已支付范围与禁止的外推

本稿证明的是完整最小逆的精确公式，包含全部内部阶、零阶和最高阶；池固定块中的原维数为头位数的 primitive 空间完整保留。

正的积分表示经过参数极小化，不会自动保持相邻对数凸性。例如两个原子的正测度，以原子坐标分别为零和一，乘质量的最小方差序列为
$$
H_n=\frac{2^n}{1+2^n}.
$$
它满足
$$
H_1^2=\frac49>\frac25=H_0H_2.
$$
因此仅凭正矩块作秩一 Schur 仍不足以证明 (4.2)。本模型若能进一步闭合，必须实际使用 (5.1)—(5.4) 的特殊 Beta 权、出生阶乘及逐头结构。

这份化简没有宣布任意异权的一般相邻常数成立，也没有将纯有限矩阵结论直接运输到原无限尾的返回能量。

## 7. 与既有结论和开放接口的关系

本稿沿用 [R239 两异权全出生证明](../results/R239-appendix-two-exceptional-weights-full-birth-one-primitive-gram-bound.md) 的完整逆后压核约定；其 §8 已处理相对出生 $q$ 的饱和固定一维线。本稿给相对出生 $q-1$ 的整个 $q$ 维池固定 primitive 块，包含最高合法阶；不把这一个约化块当作任意权模型的全体 primitive。

[R239 全出生倒数权对偶](../results/R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md) 仍可在此使用，但没有提供一般相邻算子序。三异权模型已另由[完整全出生证明](../results/R239-appendix-three-exceptional-weights-full-primitive-gram-bound.md)支付。一般头数的下一实质缺口仍是从本稿的特殊积分/逐头结构证明 (4.2)，再按实际边界的全部头算子及 Schur 补支付返回能量；本附录不预设这两步已经完成。


## 8. 任意头归一化多项式的全部外实根与倒数正矩

本节处理 §5 积分中真正出现的标量归一化因子。结论适用于任意头数，不靠固定维数的符号展开；它尚不等同于矩阵 $H_n$ 的相邻序或完整 Hankel 正性。

### 8.1 准确归一化与两端

仍取 $A_i=a_i^2>0$、$h=L-q+2\ge2$，定义上升阶乘 $(x)_j=x(x+1)\cdots(x+j-1)$ 及
$$
P_A(x)=\sum_{R\subseteq[q]}A_R(x)_{|R|}(h-x)_{q-|R|},
\qquad
Z_A(x)=\frac{P_A(x)}{(h)_q}.
\tag{8.1}
$$
这是关于实变量 $x$ 的多项式。对 $0<x<h$，令 $U_x\sim\operatorname{Beta}(x,h-x)$。逐项积分给
$$
Z_A(x)=\mathbb E\prod_{i=1}^q(1-U_x+A_iU_x).
\tag{8.2}
$$
因此 $Z_A(x)>0$，且多项式两端准确为
$$
Z_A(0)=1,\qquad Z_A(h)=A_{[q]}.
\tag{8.3}
$$

在原内部阶 $1\le n<h$，令
$$
\omega_R(n)=\frac{A_R}{\binom L{n+|R|-1}},\qquad
W_n=\sum_R\omega_R(n).
$$
把 §5 的变量 $t$ 换成 $u=t/(1+t)$，得到
$$
\boxed{W_n=(L+1)B(n,h-n)Z_A(n).}
\tag{8.4}
$$
原权在零阶/最高阶有不合法状态，故不将 (8.4) 的发散 Beta 因子代作端点定义；端点仍用 §3 的准确有限式。

若某个 $A_i=1$，合并包含或不包含该指标的两个子集项，得到
$$
P_{(A',1)}(x)=(h+q-1)P_{A'}(x).
$$
所以归一化 $Z_A=Z_{A'}$ 完全不变。删掉所有等于一的头，设剩余头数为 $q_0$，其中 $p$ 个大于一、$r$ 个小于一，$p+r=q_0$。最高系数是
$$
[x^{q_0}]P_{A'}(x)=\prod_{i=1}^{q_0}(A_i-1)\ne0.
\tag{8.5}
$$

### 8.2 完整生成恒等式与正离散正交

对任意 $|t|<1$，准确有
$$
\boxed{
\sum_{k=0}^{\infty}P_A(-k)\frac{(h)_k}{k!}t^k
=(h)_q\,\frac{\prod_{i=1}^q(1-A_it)}{(1-t)^{h+q}}.
}
\tag{8.6}
$$
给出逐项证明。固定 $R$、$j=|R|$，使用
$$
(-k)_j=(-1)^j k^{\underline j}.
$$
当 $k<j$ 时该项为零；置 $k=j+\ell$，则
$$
(h)_k(h+k)_{q-j}=(h)_{\ell+q}=(h)_q(h+q)_\ell.
$$
因此该子集对左侧的贡献恰为
$$
A_R(h)_q(-t)^j\sum_{\ell\ge0}\frac{(h+q)_\ell}{\ell!}t^\ell
=A_R(h)_q(-t)^j(1-t)^{-h-q}.
$$
对所有子集求和即得 (8.6)。绝对收敛允许有限次求导。

若 $A>1$ 在头权平方中出现 $m$ 次，则 $c=1/A\in(0,1)$ 是右侧的 $m$ 重零。用 $(t\partial_t)^j$，$0\le j<m$，得到
$$
\boxed{
\sum_{k=0}^{\infty}
P_A(-k)\,k^j c^k\,\frac{(h)_k}{k!}=0,
\qquad 0\le j<m.
}
\tag{8.7}
$$
权 $(h)_k/k!$ 严格为正；这些级数绝对收敛。重复头已付相应的全部多项式次数，不能只算不同权的个数。

还有完整反射恒等式
$$
\boxed{P_A(x)=A_{[q]}P_{1/A}(h-x).}
\tag{8.8}
$$
这是将求和子集换成补集。对 $A_i<1$ 应用 (8.7) 于倒数权，得到 $P_A(h+k)$ 在右侧整数射线上的同类正正交关系。

### 8.3 所用变号论证的自含证明

令 $c_1,\ldots,c_\ell$ 为不同的 $(0,1)$ 中的实数，重数为 $m_i$，总数 $d_0=\sum_i m_i$。实函数族
$$
k^j c_i^k,\qquad 0\le j<m_i
\tag{8.9}
$$
在实轴上是扩展 Chebyshev 族：任何非零实线性组合至多有 $d_0-1$ 个实零点，按重数计。

这可对 $d_0$ 直接归纳。先除以一个 $c_i^k$ 再求导；该组多项式的次数降一，其余组仍是同次数多项式乘不同实指数，所属空间的总维数降一。Rolle 定理和归纳假设给原函数的零点数上界；导数恒零时原函数是非零常数。相同归纳也给这些函数的线性独立性。按组排列并在每组按次数排列的任意完整前缀，满足相同结论。

现在，若一个非零实多项式 $Q(k)$ 对 (8.9) 的全部函数在权 $(h)_k/k!$ 下正交，则非零序列 $Q(0),Q(1),\ldots$ 至少有 $d_0$ 次变号（零值跳过）。否则设只有 $b<d_0$ 次变号；在每一对相邻异号的非零项之间选一个实点。取 (8.9) 的长度 $b+1$ 的完整前缀，解这 $b$ 个齐次插值条件，得到非零函数 $g$。上述零点数上界使它恰有这 $b$ 个简单零点而无其他实零点。因此整体换号后，所有非零 $Q(k)g(k)$ 都为正，且至少一项严格为正。这与
$$
\sum_{k\ge0}Q(k)g(k)\frac{(h)_k}{k!}=0
$$
矛盾。收敛由 $g$ 的指数衰减和 $Q$ 的多项式增长保证。

将此论证用于 (8.7)，$P_A(-k)$ 至少有 $p$ 次变号，所以 $P_A$ 有至少 $p$ 个不同的负实根。由 (8.8)，另有至少 $r$ 个不同的、严格大于 $h$ 的实根。两端 (8.3) 均非零；而 (8.5) 的次数恰为 $p+r$。因此计数已满，没有其他根，也没有重根。

**定理。** 删去 $A_i=1$ 后，$Z_A$ 的全部根均为单实根：准确有 $p$ 个在 $(-\infty,0)$，$r$ 个在 $(h,\infty)$。

### 8.4 倒数的明确独立 Beta 乘积矩

将负根写成 $-\lambda_1,\ldots,-\lambda_p$，右根写成 $\nu_1,\ldots,\nu_r$。于是
$$
\lambda_i>0,\qquad \nu_j>h,
$$
且由 $Z_A(0)=1$，
$$
\boxed{
Z_A(x)=
\prod_{i=1}^p\left(1+\frac{x}{\lambda_i}\right)
\prod_{j=1}^r\left(1-\frac{x}{\nu_j}\right).
}
\tag{8.10}
$$
取相互独立的随机变量
$$
U_i\sim\operatorname{Beta}(\lambda_i,1),\qquad
V_j\sim\operatorname{Beta}(\nu_j,1),
\qquad
Y=\frac{\prod_iU_i}{\prod_jV_j}.
$$
空乘积取一。逐个积分给
$$
\mathbb E U_i^x=\frac{\lambda_i}{\lambda_i+x},
\qquad
\mathbb E V_j^{-x}=\frac{\nu_j}{\nu_j-x}.
$$
所以在包含整个 $[0,h]$ 的共同实矩区间中，
$$
\boxed{\frac1{Z_A(x)}=\mathbb E Y^x.}
\tag{8.11}
$$
若两侧之一为空，相应的区间端点没有限制。特别，所有合法非负整数矩均有限。

因此对任意非负整数 $d_0,\ldots,d_v$，只要全部 $d_i+d_j\le h$，
$$
\left[\frac1{Z_A(d_i+d_j)}\right]_{i,j}\succeq0.
\tag{8.12}
$$
证明就是把其二次型写成 $\mathbb E|\sum_i c_iY^{d_i}|^2$。若有至少一个非单位头权且指数互不相同，这个矩阵严格正定：$Y$ 有连续、非退化的区间支持，非零多项式不能在该支持上消失。所有头权等于一时 $Y=1$，此矩阵只需声明半正定。

### 8.5 文献字典与尚未支付的矩阵部分

(8.6) 的多项式在全部 $A_i>1$ 且权互异时，与多重 Meixner 第一类的多重指标 $(1,\ldots,1)$ 一致；重复权可合并重数，或按所列有限和连续延拓。准确地，取其参数 $\beta=h,c_i=A_i^{-1}$，则
$$
P_A(x)=\left[\prod_i(1-A_i)\right]
M^{(1)}_{(1,\ldots,1)}(-x;\beta=h,c_i=A_i^{-1}).
$$
命名和显式有限和可参照 F. Ndayiragije 与 W. Van Assche，*Multiple Meixner polynomials and non-Hermitian oscillator Hamiltonians*，式 (3)，[作者原文](https://wis.kuleuven.be/analyse/members/walter/mmeixner.pdf) / [arXiv:1310.0982](https://arxiv.org/abs/1310.0982)。本文上面的生成式、两侧变号和矩表示均已自行证明，混合大小权不依赖把不合法的概率参数代入该文。

(8.11)—(8.12) 只证明标量归一化倒数的正矩。完整 $H_n$ 仍有协方差分子和首尾的源 Gram。特别，若逐对展开
$$
H_n=\frac1{W_n}\sum_{R<T}\omega_R(n)\omega_T(n)
(b_R-b_T)(b_R-b_T)^*,
$$
两个非空集合的单独项在零阶延拓可为零、其余阶为正，不能各自当作已有正矩测度。仍须对完整矩阵分子给出实际正表示或相邻算子序；本节没有由标量分母的正性替代该步骤。


## 9. 任意头数、含两端的相邻粗界

这里仍取 §§1—8 的相对出生 $s=q-1$、$q\ge2$、$h=L-q+2\ge2$。对全部合法相邻阶 $1\le n<h$，准确有
$$
\boxed{
H_nH_{n+1}^{-1}H_n
\preceq C_{q,h,n}H_{n-1},\qquad
C_{q,h,n}=
\left(1+\frac{q-1}{n}\right)
\left(1+\frac{q-1}{h-n}\right)\le q^2.
}
\tag{9.1}
$$
这不是一般系数一结论；新增覆盖包括 $n=1$ 和 $n=h-1$。内部已有 [R271 双复制正矩界](../results/R271-appendix-penultimate-primitive-interior-adjacent-uniform-bound.md) 给常数不超过四，可与 (9.1) 取较小者，不重复计作内部常数改进。

**证明。** 使用 §3 的同一仿射函数 $s_R(f)-z$。对全部同时合法的状态，
$$
\frac{\omega_R(n)}{\omega_R(n-1)}
=\frac{n+r-1}{h+q-n-r}.
\tag{9.2}
$$
右侧随 $r$ 递增。因此置
$$
M=\frac{n+q-1}{h-n},\qquad
m=\frac{n}{h+q-n-1},
$$
内部各阶通过同一参数逐项比较再取最小值，得到
$$
H_n\preceq M H_{n-1},\qquad
H_{n+1}\succeq m H_n.
\tag{9.3}
$$

第一个端点不能代入不合法的空集合权。准确做法是在 $H_1$ 的最小化中选 $z=0$，则空集合项为零，剩余非空集合的 (9.2) 都合法，给 $H_1\preceq M H_0$。第二个端点用最高阶强制参数 $z=s_{[q]}(f)$：全缺失集合的函数值为零，其他状态逐项满足后一比较，再允许 $H_{h-1}$ 对全部参数最小化，即得 $H_h\succeq m H_{h-1}$。当 $h=2$ 时这两个论证同时使用，仍无遗漏状态。

各 $H_j$ 严格正定。由第二个不等式取逆并作合同，
$$
H_nH_{n+1}^{-1}H_n
\preceq m^{-1}H_n
\preceq (M/m)H_{n-1}.
$$
而 $M/m$ 恰为 (9.1) 的常数。两分母都至少为一，故不超过 $q^2$。这证明整个非交换矩阵序，未将源基当成正交基。由 (4.2)，同一结论准确运输到本固定块的 $\Gamma$。证毕。

若 $n,h-n\ge q$，本节常数还不超过 $(2-1/q)^2<4$；此处仍只是上述逐项粗界。它没有给与头数无关的全部端点常数，也没有处理其他出生层或原无限尾。

## 10. 任意出生层的精确多重仿射最小化

本节重新允许全部相对出生，仍保持 $q\ge1$ 个正异权头和 $L\ge q$ 个单位权池位。记
$$
0\le s\le q,\qquad
\delta=q-s,\qquad
h=L+q-2s=L-q+2\delta.
\tag{10.1}
$$
$\delta$ 是固定的多项式次数。以下关于阶数的断言仅在 $0\le n\le h$ 使用；若讨论相邻序，还须 $1\le n<h$。

### 10.1 完整的固定 primitive 源坐标

对每个 $\delta$ 元头子集 $I$ 取任意复坐标 $x_I$，定义齐次多重仿射多项式
$$
f(X)=\sum_{\substack{I\subseteq[q]\\|I|=\delta}}x_I\prod_{i\in I}X_i,
\qquad
f(R)=f(1_R)=\sum_{\substack{I\subseteq R\\|I|=\delta}}x_I.
\tag{10.2}
$$
当 $\delta=0$，这就是任意常数。定义源嵌入
$$
\boxed{
\mathcal E_\delta x=
\sum_{\substack{R\subseteq[q]\\r=|R|\ge\delta}}
(-1)^{r-\delta}
\frac{a_R}{\binom L{r-\delta}}f(R)\,
e_{[q]\setminus R}w_{r-\delta}.
}
\tag{10.3}
$$
每一项都处于物理孔数 $s$ 的整层。

对 $r>\delta$，齐次性逐单项式给
$$
\sum_{i\in R} f(R\setminus\{i\})=(r-\delta)f(R).
\tag{10.4}
$$
头删除和池删除的系数利用
$$
\frac{L-r+\delta+1}{\binom L{r-\delta}}
=\frac{r-\delta}{\binom L{r-\delta-1}}
$$
准确相消，故 $D\mathcal E_\delta x=0$。当 $r=\delta$，顶层系数 $a_Rx_R$ 独立任意；所有更大缺失集合的系数由同一非零池删除递推唯一决定。因此 (10.3) 正好参数化整个池置换固定 primitive 块，其维数为 $\binom q\delta=\binom qs$。

依旧令 $F_n=D^n(D^*)^n/(n!)^2$ 在完整 $\mathcal H_s$ 上先取逆，并定义
$$
H_n^{(\delta)}=\mathcal E_\delta^*F_n^{-1}\mathcal E_\delta.
\tag{10.5}
$$
本节没有把池固定块误作全体 primitive 空间；其他池表示仍可有自己的约化块。

### 10.2 所有固定解及非法状态约束

合法头状态集合准确为
$$
\mathcal A_n=\{R\subseteq[q]:0\le n+|R|-\delta\le L\}.
\tag{10.6}
$$
令 $P$ 遍历所有次数至多 $\delta-1$ 的多重仿射多项式；$\delta=0$ 时只取 $P=0$。置
$$
F=f+P,\qquad
F(R)=0\quad(R\notin\mathcal A_n).
\tag{10.7}
$$
这里非法状态上的等式是实际线性约束，不能以零分母或形式延拓代替。

**定理。** 方程 $D^nu/n!=\mathcal E_\delta x$ 的全部池置换固定解，恰为
$$
\boxed{
u_n(F)=
\sum_{R\in\mathcal A_n}
(-1)^{|R|-\delta}
\frac{a_R}{\binom L{n+|R|-\delta}}F(R)\,
e_{[q]\setminus R}w_{n+|R|-\delta},
}
\tag{10.8}
$$
其中 $F$ 满足 (10.7)。全 Hilbert 空间还可以有非固定零源解；其唯一最小范数解由池置换平均落在 (10.8) 中。

先核方程。固定目标缺失集合 $R$，其大小 $r\ge\delta$。池二项式相消后，输出系数为
$$
\frac{a_R}{L^{\underline{r-\delta}}}
\sum_{T\subseteq R}
(-1)^{|T|-\delta}
(n+|T|-\delta)^{\underline{r-\delta}}F(T).
\tag{10.9}
$$
非法输入满足 $F(T)=0$，故可安全扩和至所有子集。合法输入若所需删除次数为负，则非负整数的下降阶乘恰为零；因此公式没有添加不合法的物理项。

对 $f$ 中一个次数 $\delta$ 的单项式 $X_I$，只需对 $I\subseteq T\subseteq R$ 求和。剩余子集数为 $r-\delta$，所作用的下降阶乘是同次数首一多项式，故有限差分恰为
$$
(-1)^{r-\delta}(r-\delta)!.
$$
对 $P$ 中一个次数 $j<\delta$ 的单项式，差分阶 $r-j$ 严格高于多项式次数 $r-\delta$，贡献为零。于是 (10.9) 恰等于 (10.3) 的系数。

再证穷尽性。完整 incidence 在 $n\le N-2s$ 时满射；置换平均保此满射，故固定部分的解空间维数等于固定输入维数减固定目标维数。固定目标维数为
$$
\sum_{r=\delta}^q\binom qr.
\tag{10.10}
$$
由于 $L\ge q$，低端和高端的非法状态不会同时出现。分别核算：

1. 若 $0\le n<\delta$，非法状态为 $r<\delta-n$。$f$ 在这些状态本来为零；多重仿射值与系数的三角反演表明，约束恰为 $P$ 的所有次数小于 $\delta-n$ 的系数为零。自由维数是 $\sum_{j=\delta-n}^{\delta-1}\binom qj$，正好等于输入、目标维数之差。
2. 若 $\delta\le n\le h-\delta$，所有头状态合法；$P$ 的自由维数为 $\sum_{j=0}^{\delta-1}\binom qj$，同样等于维数之差。
3. 若 $h-\delta<n\le h$，置 $j_0=n-(h-\delta)\in\{1,\ldots,\delta\}$。非法状态为 $r>q-j_0$。在补变量 $Y_i=1-X_i$ 中，$F(1-Y)$ 的最高齐次部分已经固定；对 $|Y|<j_0$ 的布尔点取零，准确固定其次数小于 $j_0$ 的系数为零。剩余低次自由维数为 $\sum_{j=j_0}^{\delta-1}\binom qj$。由 $\binom qr=\binom q{q-r}$，这又正好是输入、目标维数之差。

这些约束都可解。参数到 (10.8) 的映射也单射：若两个参数给同一输入，则其差在合法状态为零，在非法状态也为零；多重仿射多项式由全部布尔点的值唯一确定。因此已构造的仿射解空间维数准确，穷尽全部固定解。

最后，对任何全空间可行解先删去无用孔层，再作池置换群的正交平均，输出不变且范数不增。唯一最小解遂固定。完整空间的 Moore–Penrose 最小化确实由此有限多项式族实现。

### 10.3 真正的最小范数、源 Gram 与两端

直接使用 $\|w_j\|^2=\binom Lj$，得到
$$
\boxed{
x^*H_n^{(\delta)}x=
\min_{\substack{\deg P\le\delta-1\\
(f+P)(R)=0\ (R\notin\mathcal A_n)}}
\ \sum_{R\in\mathcal A_n}
\frac{a_R^2}{\binom L{n+|R|-\delta}}\,
|f(R)+P(R)|^2.
}
\tag{10.11}
$$
最小化在复多重仿射系数上进行；$\delta=0$ 仍无低次参数。这是全 Hilbert 最小解的准确范数，而非试探原像的上界。

$n=0$ 时，所有次数小于 $\delta$ 的布尔状态必须为零，唯一允许 $P=0$，所以 $H_0^{(\delta)}$ 正是 (10.3) 的实际源 Gram。$n=h$ 时，补变量中全部低次系数被迫为零，唯一允许
$$
\boxed{F(X)=(-1)^\delta f(1-X).}
\tag{10.12}
$$
最高齐次部分正好仍为 $f(X)$；若非法状态的补集大小小于 $\delta$，该式自动为零。两端均已付清。

$\delta=1$ 在坐标 $x_i=f_i/a_i$ 下恢复 §§1—3 的一参数公式（把常数 $P$ 写成 $-z$）；$\delta=0$ 恢复相对出生 $q$ 的饱和固定一维线；$\delta=q$ 则是相对真空出生 $s=0$ 的完整最小逆。它们是同一个公式的实际端点，不需改变物理池大小。

源坐标一般非正交，压缩算子的坐标为 $(H_0^{(\delta)})^{-1}H_n^{(\delta)}$。因此与 (4.2) 相同，完整相邻 $\Gamma$ 序准确等价于 $H_n^{(\delta)}(H_{n+1}^{(\delta)})^{-1}H_n^{(\delta)}$ 的序，不能先在 primitive 上倒置压缩 Gram。

### 10.4 所有出生的合法中段粗界

对同时满足
$$
1\le n<h,\qquad \delta\le n\le h-\delta
\tag{10.13}
$$
的阶数，(10.11) 还直接给
$$
\boxed{
H_n^{(\delta)}(H_{n+1}^{(\delta)})^{-1}H_n^{(\delta)}
\preceq
\left(1+\frac{q-1}{n+1-\delta}\right)
\left(1+\frac{q-1}{h+1-\delta-n}\right)
H_{n-1}^{(\delta)}
\preceq q^2H_{n-1}^{(\delta)}.
}
\tag{10.14}
$$

证明仍是完整最小化的逐项比较。权比
$$
\frac{\omega_R(n)}{\omega_R(n-1)}
=\frac{n+r-\delta}{h+q-\delta-n-r+1}
$$
随 $r$ 递增，故
$$
M=\frac{n+q-\delta}{h+1-\delta-n},\qquad
m=\frac{n+1-\delta}{h+q-\delta-n}
$$
分别给 $H_n^{(\delta)}\preceq M H_{n-1}^{(\delta)}$ 及
$H_{n+1}^{(\delta)}\succeq mH_n^{(\delta)}$。在 $n=\delta\ge1$，前一阶只新出现空集合约束 $F(\varnothing)=0$，选前一阶最小参数即可使新空项为零；在 $n=h-\delta$ 且后一阶合法时，后一阶只强制 $F([q])=0$，同理保后一比较。$\delta=0$ 的整个合法相邻区间没有这些缺失状态。取逆、合同及相乘给 (10.14)。

本节不将 (10.14) 推到 $n<\delta$ 或 $n>h-\delta$：在那里低次参数的可行仿射空间逐阶改变，原逐项比较并不直接成立。把一般有限权模型补入很弱的等权池，也不会自动避开这些边段。任意全 primitive 的统一相邻常数、真实连续尾及边界返回比较仍须继续证明。


## 11. 任意短池、两端同时缺失与任意有限正权的完整参数化

本节由 Astra-ISP-0c 推导、central_review 全文独立核验。去掉 §10 的 $L\ge q$ 假设。结论仍是准确的完整最小逆公式，不增加一般相邻不等式的已证范围。短池中，源本身也须满足额外线性条件，输入的低端和高端缺失可同时出现。

### 11.1 源多项式的准确约束

取 $q\ge1$ 个正头权和任意 $L\ge0$ 个单位池位，令 $N=q+L$。先考虑
$$
0\le s\le q,\qquad s\le N/2,\qquad
\delta=q-s,\qquad h=N-2s=L-q+2\delta\ge0.
\tag{11.1}
$$
所有二项式约定在下标不属于 $0,\ldots,q$ 时为零。源坐标空间现在是
$$
\boxed{
\mathcal V_\delta^{(L)}
=\left\{f=\sum_{|I|=\delta}x_I X_I:
f(R)=0\ \text{当 }|R|>L+\delta\right\}.
}
\tag{11.2}
$$
仍是齐次多重仿射多项式，只是最高系数不再全部独立。源嵌入为
$$
\boxed{
\mathcal E_\delta f=
\sum_{\substack{R\subseteq[q]\\\delta\le r\le L+\delta}}
(-1)^{r-\delta}\frac{a_R}{\binom L{r-\delta}}
f(R)e_{[q]\setminus R}w_{r-\delta}.
}
\tag{11.3}
$$
所有保留的池占据数合法。

(10.4) 的齐次递推仍逐项证明 $D\mathcal E_\delta f=0$。但此处还要检查新的最高输出层：若 $r=L+\delta+1\le q$，池删除项已不存在，全部头删除项正比于
$$
\sum_{i\in R}f(R\setminus\{i\})=(L+1)f(R)=0.
$$
这正是 (11.2) 的额外源条件；不能省去它。反过来，primitive 递推从 $r=\delta$ 的最高系数唯一决定所有合法源系数，并在这个末层迫使上述条件。更大的缺失集合条件由同一次齐次计数推出。因此 (11.3) 穷尽池固定 primitive 块，且源坐标单射。

准确维数为
$$
\boxed{
\dim\mathcal V_\delta^{(L)}
=\binom q\delta-\binom q{L+\delta+1}.
}
\tag{11.4}
$$
它也等于完整固定层的维数差：
$$
\sum_{r=\delta}^{\min(q,L+\delta)}\binom qr
-
\sum_{r=\delta+1}^{\min(q,L+\delta+1)}\binom qr.
$$
相邻删除在此范围满射，完整等权 Boolean 的有限 Lefschetz 链和正对角去权给出该事实，再作池置换平均。下节还会在源多项式中直接核对 (11.4)。

若 $s>q$ 且仍 $s\le N/2$，整个固定层包含全部头状态，池占据数严格为正；固定删除有非零池对角元及三角头删除部分，故没有 primitive。因而 (11.1) 已涵盖所有可能非零的固定 primitive 块。

### 11.2 只用于参数计数的无权头分解

这里引入辅助的无权 $q$ 位头空间，绝不把它当作实际异权模型的正交分解。令 $\mathcal H_j^0$ 为其次数 $j$ 的 primitive 多项式系数空间：
$$
0\le j\le\lfloor q/2\rfloor,\qquad
d_j^0:=\dim\mathcal H_j^0=\binom qj-\binom q{j-1}.
$$
记无权删除、创建为 $D^0,U^0$。直接有
$$
[D^0,U^0]|_{\text{次数 }r}=(q-2r)I.
$$
对 $v\in\mathcal H_j^0$，逐次交换给
$$
\|(U^0)^k v\|^2=k!(q-2j)^{\underline k}\|v\|^2,
\qquad 0\le k\le q-2j.
$$
不同 primitive 向量及不同出生的这些链正交；在未覆盖的最小次数上重复取核，有限过程穷尽全部头空间。这给以下自含的多项式描述。

把 $v$ 本身视为齐次多重仿射函数，记它在布尔点 $R$ 的值为 $v(R)$。逐次计数得到
$$
\boxed{
\bigl((U^0)^k v\bigr)(R)
=(|R|-j)^{\underline k}v(R).
}
\tag{11.5}
$$
而 $v(R)=0$ 除非 $j\le|R|\le q-j$；在该合法区间的每一个整数层，求值映射在 $\mathcal H_j^0$ 上单射，不同 $j$ 的像相互独立。这些断言也由上述非零链范数直接得到。

所以次数至多 $\delta$ 的全部多重仿射函数，在每个 $\mathcal H_j^0$ 分量上，就是
$$
p_j(r)v(R),\qquad
\deg p_j\le\min(\delta-j,q-2j),
\tag{11.6}
$$
不满足非负次数上界的分量不存在。一个齐次次数 $\delta$ 的源，只有
$$
j\le j_{\max}:=\min(\delta,q-\delta)
$$
的分量；其对应多项式是固定向量系数乘 $(r-j)^{\underline{\delta-j}}$。

源的额外条件 (11.2) 正好删去
$$
j<j_{\min}:=\max(0,q-L-\delta)
$$
的分量：若 $q-j>L+\delta$，在第一个非法层上下降阶乘非零，且该层各 $j$ 的像独立，故该分量必须为零；若 $q-j\le L+\delta$，则其高层值本来为零。由 $h\ge0$，$j_{\min}\le j_{\max}$。因此
$$
\dim\mathcal V_\delta^{(L)}
=\sum_{j=j_{\min}}^{j_{\max}}d_j^0
=\binom q\delta-\binom q{L+\delta+1},
$$
再次核对 (11.4)。这些头分量只用来证明线性参数空间的完整性；实际范数仍含全部 $a_R^2$，没有被正交化掉。

### 11.3 全部固定解的统一公式

对任意 $0\le n\le h$，定义
$$
a_n=\delta-n,\qquad b_n=L+\delta-n,\qquad
\mathcal A_n=\{R:a_n\le|R|\le b_n\}.
$$
给定 $f\in\mathcal V_\delta^{(L)}$，允许
$$
\boxed{
F=f+P,\qquad \deg P\le\delta-1,\qquad
F(R)=0\quad(R\notin\mathcal A_n).
}
\tag{11.7}
$$
$\delta=0$ 时 $P=0$。低、高非法状态同时存在时，(11.7) 的两组约束必须一起解。

**定理。** 全部池固定解 $D^nu/n!=\mathcal E_\delta f$ 恰由
$$
\boxed{
u_n(F)=\sum_{R\in\mathcal A_n}
(-1)^{r-\delta}
\frac{a_R}{\binom L{n+r-\delta}}F(R)
e_{[q]\setminus R}w_{n+r-\delta}
}
\tag{11.8}
$$
给出。

可行式确实解方程：目标只含 $\delta\le r\le L+\delta$，所以
$L^{\underline{r-\delta}}>0$。沿 (10.9) 的完整有限差分，
$$
\frac{a_R}{L^{\underline{r-\delta}}}
\sum_{T\subseteq R}
(-1)^{|T|-\delta}
(n+|T|-\delta)^{\underline{r-\delta}}F(T)
$$
正好恢复 (11.3)。两边非法输入均由 $F(T)=0$ 删去，未加负阶乘项；次数小于 $\delta$ 的部分仍被有限差分杀掉。

剩下须证明可行参数存在且穷尽解，不能只沿用长池的单边计数。以下给出完整证明。

在第 $j$ 个辅助头 primitive 分量上，可能非零的秩为
$j,\ldots,q-j$。其中合法秩个数为
$$
t_j(n)=\max\{0,\min(q-j,b_n)-\max(j,a_n)+1\},
$$
非法秩个数为
$$
z_j(n)=q-2j+1-t_j(n).
\tag{11.9}
$$
每个非法整数秩都是多项式 $p_j$ 的一个准确零点条件；该层求值单射使其作用在整个向量系数上。

对有源的 $j_{\min}\le j\le j_{\max}$，$a_n\le\delta\le q-j$ 且
$b_n\ge q-\delta\ge j$，因此合法区间非空。此时
$$
z_j(n)=(\delta-n-j)_+
+(q-j-L-\delta+n)_+\le\delta-j.
\tag{11.10}
$$
最后一个不等式逐情形可核：两项都正时用
$j\ge q-L-\delta$；只有第一项正时用 $n\ge0$；
只有第二项正时用 $n\le h$。所以可取所有非法秩的一次因子乘积，再乘一个次数 $\delta-j-z_j(n)$ 的多项式，使最高系数等于给定源的最高系数。它与原源的差次数更低，正是允许的 $P$。无源分量先取零。这构造了 (11.7) 的解。

再计数齐次差空间。次数至多 $\delta-1$ 的第 $j$ 分量可用多项式维数为
$$
\gamma_j=\max\{0,\min(\delta-j,q-2j+1)\}.
$$
强制其在所有非法秩上为零后，自由维数为
$$
(\gamma_j-z_j(n))_+\,d_j^0.
\tag{11.11}
$$
这准确等于 $(t_j(n)-t_j(0))d_j^0$，分下列三种情况核验：

- 若 $j<j_{\min}$，整个秩带在每个 $0\le n\le h$ 都严格留在 $j,\ldots,q-j$ 之内，所以 $t_j(n)=t_j(0)=L+1$。此时 $z_j(n)>\delta-j$，没有自由低次参数。
- 若 $j_{\min}\le j\le j_{\max}$，有
  $t_j(0)=q-j-\delta+1$、$\gamma_j=\delta-j$；(11.10) 使
  $(\gamma_j-z_j(n))_+=t_j(n)-t_j(0)$。
- 若 $j>j_{\max}$：当 $j>\delta$ 时，整个头秩区间始终合法，前后 $t_j$ 相同且没有低次参数；当 $j>q-\delta$ 时，目标分量为空，而次数至多 $\delta-1$ 已包含该分量的全部多项式，故自由维数恰为 $t_j(n)d_j^0$。在 $j\le\lfloor q/2\rfloor$ 内这两种情况互斥，覆盖全部剩余分量。

对全部 $j$ 求和，(11.11) 正好是固定输入维数减固定目标维数。完整 incidence 满射经池平均后仍满射，因此这就是全部固定解的正确仿射维数。参数到 (11.8) 单射，因为函数在合法和非法的全部布尔点都已确定。故构造穷尽所有固定解。

### 11.4 完整 MP、首尾与无池模型

全空间可行解作池置换正交平均，源不变且范数不增；唯一全 Hilbert 最小解属于上述固定族。因此
$$
\boxed{
\begin{aligned}
H_n^{(\delta,L)}(f,f)
&=\min_{\substack{\deg P\le\delta-1\\
(f+P)(R)=0\ (R\notin\mathcal A_n)}}
\sum_{R\in\mathcal A_n}
\frac{a_R^2}{\binom L{n+|R|-\delta}}|f(R)+P(R)|^2,\\
&\hspace{30mm} f\in\mathcal V_\delta^{(L)}.
\end{aligned}
}
\tag{11.12}
$$
依旧是完整层的逆后压到实际 primitive，源内积为 $H_0$。

$n=0$ 时低端约束迫 $P=0$。$n=h$ 时，唯一可行式仍为
$$
\boxed{F(X)=(-1)^\delta f(1-X).}
\tag{11.13}
$$
其高端零来自齐次次数，其低端零来自 (11.2)；输入、目标固定维数由补集相同，完整 Lefschetz 同构保证唯一性。因此两端同时缺失时也没有遗漏条件。

当 $L=0$ 时池置换群平凡，模型就是任意 $q$ 个正权的完整有限 Boolean 删除。此时 $s\le q/2$、$\delta=q-s$，
$$
\dim\mathcal V_\delta^{(0)}
=\binom qs-\binom q{s-1},
$$
并且 $\mathcal A_n$ 只含单一秩 $r=\delta-n$。(11.12) 因而给任意有限正权模型整个 $K_s$ 的准确多项式插值最小化。它没有把维数或条件数免费变小，也没有证明一般相邻序；新增的是短池和无池时仍完全正确的参数化与端点。
