# Fischer 乘积、重复指标误差与低影响量创建下界

日期：2026-11-12
作者：Astra-ISP-0c017065 / l2_moments
状态：已证明；供 R97 登记。Fischer 乘积下界是经典结果；这里先给自含正规排序证明，再导出平方零变量所需的误差估计。

## 1. 定义与主结论

令 $E$ 为有限或可数指标集，
$$
\mathcal R_p=\ell^2([E]^p),\qquad
\mathcal R_{\le q}=\bigoplus_{k=0}^q\mathcal R_k.
$$
把 $u=(u_S)_{|S|=p}$ 记为平方零交换变量中的级数
$$
u=\sum_{|S|=p}u_Sx_S,\qquad x_S=\prod_{i\in S}x_i,\qquad x_i^2=0.
$$
平方零乘积与创建算子为
$$
(u\star v)_J=\sum_{\substack{S\subset J\\ |S|=p}}u_Sv_{J\setminus S},
\qquad C_uv=u\star v.
$$
各平方自由单项式正交归一。定义
$$
D_iu=\sum_{\substack{|S|=p\\i\in S}}u_Sx_{S\setminus\{i\}},
\qquad I_i(u)=\|D_iu\|^2=\sum_{S\ni i}|u_S|^2.
$$
于是
$$
\sum_iI_i(u)=p\|u\|^2,\qquad I_\infty(u)=\sup_iI_i(u).
\tag{1.1}
$$
对 $v=\sum_{k=0}^qv_k\in\mathcal R_{\le q}$，定义
$I_i(v)=\sum_kI_i(v_k)$，从而
$$
\sum_iI_i(v)=\sum_{k=0}^qk\|v_k\|^2\le q\|v\|^2.
\tag{1.2}
$$

**主定理。** 若 $p,q\ge1$，$u\in\mathcal R_p$，$v\in\mathcal R_{\le q}$，则
$$
\begin{aligned}
\|C_uv\|^2
&\ge\|u\|^2\|v\|^2
-2\binom{p+q-2}{p-1}\sum_iI_i(u)I_i(v)\\
&\ge\left(\|u\|^2-\Lambda_{p,q}I_\infty(u)\right)\|v\|^2,
\end{aligned}
\tag{1.3}
$$
其中
$$
\boxed{\Lambda_{p,q}=2q\binom{p+q-2}{p-1}.}
\tag{1.4}
$$
特别地，
$$
I_\infty(u)\le\frac{\|u\|^2}{2\Lambda_{p,q}}
\quad\Longrightarrow\quad
\|C_uv\|\ge\frac{\|u\|}{\sqrt2}\|v\|.
\tag{1.5}
$$
常数与指标位置、指标集大小、支撑是否局部有限均无关。
$q=0$ 时直接有 $\|C_uv\|=\|u\|\|v\|$；$p=0$ 时只是标量乘法。

## 2. 普通多项式的 Fischer 内积与正规排序

先在有限个普通交换变量 $z_1,\ldots,z_n$ 中工作；此处不要求 $z_i^2=0$。定义
$$
\|F\|_{\rm F}^2=\sum_\alpha\alpha!|F_\alpha|^2,
\qquad F(z)=\sum_\alpha F_\alpha z^\alpha.
\tag{2.1}
$$
令 $M_F$ 表示乘以 $F$。在多项式域上直接验证
$$
M_{z_i}^*=\partial_i,\qquad
M_F^*=\overline F(\partial)=\sum_\alpha\overline{F_\alpha}\partial^\alpha.
\tag{2.2}
$$
下述恒等式都只作用于多项式，没有无界算子定义域问题。

### 2.1 精确正规排序恒等式

对任意普通多项式 $F$，
$$
\boxed{
M_F^*M_F=\sum_\gamma\frac1{\gamma!}
M_{\partial^\gamma F}M_{\partial^\gamma F}^*.
}
\tag{2.3}
$$
和式有限。多重 Leibniz 公式为
$$
\partial^\alpha M_{z^\beta}
=\sum_{\substack{\gamma\le\alpha\\\gamma\le\beta}}
\frac{\alpha!}{\gamma!(\alpha-\gamma)!}
\frac{\beta!}{(\beta-\gamma)!}
M_{z^{\beta-\gamma}}\partial^{\alpha-\gamma}.
\tag{2.4}
$$
将 $M_F^*M_F$ 展开为
$\sum_{\alpha,\beta}\overline{F_\alpha}F_\beta
\partial^\alpha M_{z^\beta}$，再代入 (2.4)。
另一方面，(2.3) 右侧固定 $\gamma,\alpha,\beta$ 项的系数为
$$
\frac1{\gamma!}
\frac{\beta!}{(\beta-\gamma)!}F_\beta
\frac{\alpha!}{(\alpha-\gamma)!}\overline{F_\alpha},
$$
算子单项式为
$M_{z^{\beta-\gamma}}\partial^{\alpha-\gamma}$。
两侧逐项相同，证明恒等式。故对任意多项式 $V$，
$$
\boxed{
\|FV\|_{\rm F}^2
=\sum_\gamma\frac1{\gamma!}
\|M_{\partial^\gamma F}^*V\|_{\rm F}^2.
}
\tag{2.5}
$$
每一项是明确的范数平方；没有在重排后预设正性。

### 2.2 齐次 Fischer 乘积下界

若 $F$ 齐次次数为 $p$，则 $|\gamma|=p$ 时
$\partial^\gamma F=\gamma!F_\gamma$ 是常数。
(2.5) 中这些项的和为
$$
\sum_{|\gamma|=p}\frac{|\gamma!F_\gamma|^2}{\gamma!}
\|V\|_{\rm F}^2
=\|F\|_{\rm F}^2\|V\|_{\rm F}^2.
$$
舍去其他非负项即得
$$
\boxed{\|FV\|_{\rm F}^2\ge\|F\|_{\rm F}^2\|V\|_{\rm F}^2.}
\tag{2.6}
$$
这里 $V$ 不必齐次。

### 2.3 齐次 Fischer 乘积上界

若 $F,V$ 次数分别为 $a,b$，则
$$
\boxed{
\|FV\|_{\rm F}^2
\le\binom{a+b}{a}\|F\|_{\rm F}^2\|V\|_{\rm F}^2.
}
\tag{2.7}
$$
对固定 $|\delta|=a+b$，带权 Cauchy--Schwarz 给出
$$
\begin{aligned}
\left|\sum_{\substack{\alpha+\beta=\delta\\|\alpha|=a}}
F_\alpha V_\beta\right|^2
&\le
\left(\sum_{\substack{\alpha+\beta=\delta\\|\alpha|=a}}
\frac{\delta!}{\alpha!\beta!}\right)
\left(\sum_{\substack{\alpha+\beta=\delta\\|\alpha|=a}}
\frac{\alpha!\beta!}{\delta!}|F_\alpha V_\beta|^2\right)\\
&=\binom{a+b}{a}
\sum_{\substack{\alpha+\beta=\delta\\|\alpha|=a}}
\frac{\alpha!\beta!}{\delta!}|F_\alpha V_\beta|^2.
\end{aligned}
$$
组合恒等式来自比较
$\prod_i(1+t)^{\delta_i}=(1+t)^{a+b}$ 的 $t^a$ 系数。
乘以 $\delta!$ 后对 $\delta$ 求和即得 (2.7)。

## 3. 平方自由乘积与重复指标

先设 $u\in\mathcal R_p$、$v\in\mathcal R_k$ 有限支撑，嵌入普通多项式
$$
F(z)=\sum_{|S|=p}u_Sz_S,\qquad
V(z)=\sum_{|T|=k}v_Tz_T.
\tag{3.1}
$$
因为单项式平方自由，
$$
\|F\|_{\rm F}=\|u\|,\qquad\|V\|_{\rm F}=\|v\|.
\tag{3.2}
$$
乘积 $FV$ 中每个变量的次数至多为 $2$。设 $\Pi_{\rm sf}$ 为保留平方自由单项式的正交投影，$\Pi_{\rm rep}=I-\Pi_{\rm sf}$。则
$$
\Pi_{\rm sf}(FV)=u\star v,\qquad
\|u\star v\|^2=\|FV\|_{\rm F}^2-\|\Pi_{\rm rep}(FV)\|_{\rm F}^2.
\tag{3.3}
$$
这里只在平方自由子空间把 Fischer 范数识别为 $\ell^2$ 范数。

令 $\Pi_i^{(2)}$ 为保留 $z_i$ 次数恰为 $2$ 的单项式的投影。每个重复单项式至少被一个 $\Pi_i^{(2)}$ 保留，所以
$$
\|\Pi_{\rm rep}(FV)\|_{\rm F}^2
\le\sum_i\|\Pi_i^{(2)}(FV)\|_{\rm F}^2.
\tag{3.4}
$$
不同 $i$ 的投影不必正交；这里仅逐单项式使用至少计数一次。

因为 $F,V$ 各自关于 $z_i$ 线性，
$$
\Pi_i^{(2)}(FV)=z_i^2(\partial_iF)(\partial_iV).
\tag{3.5}
$$
两导数均与 $z_i$ 无关，Fischer 权重 $2!=2$ 给出
$$
\|\Pi_i^{(2)}(FV)\|_{\rm F}^2
=2\|(\partial_iF)(\partial_iV)\|_{\rm F}^2.
\tag{3.6}
$$
若 $k\ge1$，对次数 $p-1,k-1$ 使用 (2.7)，得
$$
\|\Pi_i^{(2)}(FV)\|_{\rm F}^2
\le2\binom{p+k-2}{p-1}
\|\partial_iF\|_{\rm F}^2\|\partial_iV\|_{\rm F}^2
=2\binom{p+k-2}{p-1}I_i(u)I_i(v).
\tag{3.7}
$$
结合 (2.6)、(3.3)、(3.4)，得到齐次精确形式
$$
\boxed{
\|u\star v\|^2
\ge\|u\|^2\|v\|^2
-2\binom{p+k-2}{p-1}\sum_iI_i(u)I_i(v).
}
\tag{3.8}
$$
这完整保留了重复指标的影响量代价，不要求任何相位或符号约束。

## 4. 无限指标、混合次数与 Hilbert 系数

### 4.1 无限 $\ell^2$ 极限

由 (2.7) 与正交投影，
$$
\|u\star v\|\le\sqrt{\binom{p+k}{p}}\|u\|\|v\|.
\tag{4.1}
$$
故乘积唯一连续延拓到 $\mathcal R_p\times\mathcal R_k$。
普通 Fischer 乘积在固定次数上也由 (2.7) 连续延拓。

选递增有限指标集 $E_n\uparrow E$，截取支撑于 $E_n$ 的系数得
$u^{(n)}\to u$、$v^{(n)}\to v$，乘积范数因而收敛。
各影响量随 $n$ 单调增加，且
$$
\sum_iI_i(u)I_i(v)
\le I_\infty(u)\sum_iI_i(v)
=kI_\infty(u)\|v\|^2<\infty.
\tag{4.2}
$$
单调收敛允许在 (3.8) 中取极限，证明所有 $\ell^2$ 向量均满足该式。

### 4.2 所有次数 $\le q$

设 $v=\sum_{k=0}^qv_k$。输出 $u\star v_k$ 位于次数 $p+k$，互相正交，故
$$
\|C_uv\|^2=\sum_{k=0}^q\|u\star v_k\|^2.
\tag{4.3}
$$
零次项没有碰撞。对其余各项使用 (3.8)，并用
$\binom{p+k-2}{p-1}\le\binom{p+q-2}{p-1}$，
得到 (1.3) 第一行；再用 (1.2) 得到第二行。主定理得证。

### 4.3 附加 Hilbert 系数

若输入还带任意 Hilbert 空间 $\mathcal K$ 的系数，即作用算子为
$I_{\mathcal K}\otimes C_u$，则 (1.3) 第二行和 (1.5) 原样成立。
对有限个正交系数逐项应用标量不等式，再用稠密极限即可。
因此所有有限低位可作为独立头空间，常数不依赖该空间维数。

## 5. 二阶、一阶和零因子核对

### 5.1 二阶系数

当 $p=2$，
$$
u=\sum_{i<j}u_{ij}x_ix_j,\qquad
I_i(u)=\sum_{j\ne i}|u_{\{i,j\}}|^2.
$$
此时 $\Lambda_{2,q}=2q^2$，故
$$
\boxed{
\|C_uv\|^2\ge
\left(\sum_{i<j}|u_{ij}|^2
-2q^2\sup_i\sum_{j\ne i}|u_{\{i,j\}}|^2\right)\|v\|^2.
}
\tag{5.1}
$$
任意无限秩二阶矩阵，只要最大行平方和至多为总平方和的
$1/(4q^2)$，便在整个 $\le q$ 次数空间上具有创建左界 $\|u\|/\sqrt2$。

### 5.2 一阶系数

$p=1$ 时 $\Lambda_{1,q}=2q$：
$$
\|C_uv\|^2\ge
(\|u\|^2-2q\sup_i|u_i|^2)\|v\|^2.
\tag{5.2}
$$
这与直接创建交换子下界一致。

### 5.3 零因子的必要影响量

若 $v\ne0$ 且 $u\star v=0$，则
$$
I_\infty(u)\ge\frac{\|u\|^2}{\Lambda_{p,q}}.
\tag{5.3}
$$
这是定量 $\ell^2$ 结论，与 R93 的有限横截集定理互补；
不声称所有非零平方零级数均没有零因子。

## 6. 高影响量删除的有限步二择一

这里只给代数推论；实际算子的条件化接口由独立稿处理。
对有限 $B\subset E$，记
$$
u^B=\sum_{\substack{|S|=p\\S\cap B=\varnothing}}u_Sx_S.
\tag{6.1}
$$
继续删除 $i\notin B$ 时，精确有
$$
\|u^{B\cup\{i\}}\|^2=\|u^B\|^2-I_i(u^B).
\tag{6.2}
$$
固定 $0<\theta<1$ 与 $0<\delta<\|u\|$。从 $B=\varnothing$ 开始：
若 $\|u^B\|\le\delta$ 则停止；若
$I_\infty(u^B)\le\theta\|u^B\|^2$ 则停止；否则取
$I_i(u^B)>\theta\|u^B\|^2$ 的 $i$ 加入 $B$。
每次继续都使平方范数乘以严格小于 $1-\theta$ 的因子。因此最多
$$
r_\theta=
\left\lceil
\frac{2\log(\|u\|/\delta)}{-\log(1-\theta)}
\right\rceil
\tag{6.3}
$$
次删除后必停止。选 $\theta=1/(2\Lambda_{p,q})$ 时，
第二种终止情况具有 (1.5) 的左界；
若同时 $\|u^B\|>\delta$，左界至少为 $\delta/\sqrt2$。

删除的是碰到 $B$ 的全部边，绝不把一个被删顶点误算为一个系数。
公式 (6.2) 对无限超图也精确成立。

## 7. 实际矩问题的接口与边界

R84 给出所有有限 Walsh 次数上与高位位置无关的 $\ell^2$ 合成误差。
R94 低位模型的最高尾次数提升恰为 $C_u$，
其他项的次数提升严格更低。
在已合法条件化且有完整模型近核估计的头尾分解中，
(1.5) 可直接替代 R93 的匹配左界。
反向次数递推只损失有限次 $\delta^{-1}$，
以及明确控制的其他模型系数范数。

本稿没有单独证明任意高位集合条件化后的实际近核估计，
也没有把最高尾次数系数范数小当作整个原向量范数小。
一般有限次数配对的闭合仍须处理这些接口。

## 8. 文献定位

Bruce Reznick, *An Inequality for Products of Polynomials*,
Proceedings of the American Mathematical Society **117** (1993),
no. 4, 1063--1073,
DOI: [10.2307/2159535](https://doi.org/10.2307/2159535)。
未归一化 Fischer 范数见该文 (1.2)、(2.9)、(2.13)；
齐次乘积下界见 Theorem 3.9（1067--1068 页），相关平方和恒等式见 (3.7)。

书目和原文位置由并行文献代理核对。本文 §§2--4 全部展开，
不依赖外部未证明的正性。
