# 全正一阶的全部幂域仍不保证通常系数截断收敛

日期：2026-11-12（UTC）。作者：critical_kernel。

状态：实际算子反障碍；不编号。本稿补充先前“全自然幂而系数截断发散”的有符号例子：这里一阶系数全部非负，并可让同一向量处于两个不交正行的全部混合幂域。它不构造未知不变核，也不否定任何已证的固定正则器图核心。

## 1. 使用的统一实际估计

令 $S_j=I-2E_j$，$V_j=(I-N_j)(I+N_j)^{-1}$。
R181 第2—3节给出如下真实接口。

对任意 $a\in\ell^2$ 及任意有限乘积单位参考态 $h$，置
$$
\beta_h=\sum_j a_j\langle S_jh_j,h_j\rangle,
$$
其中充分高位 $h_j=\Omega$，故该和实际有限。
若 $\Lambda_h$ 为以这些 $h_j$ 作真空的激发次数加1，则
$$
\|\Lambda_h^s(X_a-\beta_h)v\|
\le D_s\|a\|_2\|\Lambda_h^{s+1}v\|,
\qquad s=0,1,\ldots,
\tag{1.1}
$$
常数与改变参考态的位数无关。该式在真实闭域成立，并给
$$
h\in\bigcap_{p\ge1}\operatorname{Dom}X_a^p,\qquad
\|(X_a-\beta_h)^ph\|
\le C_p\|a\|_2^p.
\tag{1.2}
$$

这里不是忽略进位：实际差
$$
K(a)=\sum_j a_j(V_j-S_j)
$$
由支撑于有限区间 $[j,\ell]$ 的局部项组成，其范数至多
$18|a_j|\alpha_\ell/\alpha_j$。
对任意乘积参考态，局部支撑长度估计给
$$
\|\Lambda_h^sK(a)v\|
\le\kappa_s\|a\|_2\|\Lambda_h^sv\|.
\tag{1.3}
$$
任意局部乘积酉变换都不改变这些项的支撑长度和算子范数，所以
$\kappa_s$ 不含参考态所用位数。
此外，任意普通系数截断满足
$$
\left\|\sum_{j<m}a_j(V_j-S_j)\right\|
\le k_a:=8\|a\|_2\|\eta\|_2.
\tag{1.4}
$$

## 2. 全正系数与两个相反虚中心的参考块

对 $n\ge1$ 取
$$
R_n=2^{2n},\qquad
A_n=\frac{1+R_n^2}{2},\qquad
b_n=2^{-8n},\qquad
L_n=\frac{A_n}{b_n}
=(1+2^{4n})2^{8n-1}\in\mathbb N.
\tag{2.1}
$$
按物理指标递增排列互不相交的有限块
$$
\{q_n\},\quad J_n^+,\quad J_n^-,
\qquad |J_n^+|=|J_n^-|=L_n.
$$
$q_n$ 是本块的标记位。不同 $n$ 的全部这些集合不交；
可插入任意长度的零系数间隔。

定义非负系数
$$
a_j=b_n\quad(j\in J_n^+\cup J_n^-),\qquad
a_{q_n}=0,
$$
其余未使用位也取0。
于是
$$
\sum_j a_j^2
=\sum_{n\ge1}2A_nb_n
=\sum_{n\ge1}(2^{-8n}+2^{-4n})<\infty,
\qquad
\sum_j a_j=2\sum_n A_n=\infty.
\tag{2.2}
$$
因此 $X=X_a$ 为真实非负不可和一阶，最大增生且空谱。

在一位 Walsh 基 $(\Omega,\chi)$ 中，
$$
S=\begin{pmatrix}0&-1\\1&2\end{pmatrix}.
$$
采用内积对第一变量线性的约定，置
$$
z_n^\pm=\frac{R_n\Omega\mp i\chi}{\sqrt{1+R_n^2}}.
$$
直接计算得
$$
\langle Sz_n^\pm,z_n^\pm\rangle
=\frac{2(1\pm iR_n)}{1+R_n^2}
=\frac{1\pm iR_n}{A_n}.
\tag{2.3}
$$
这两个数都在 $S$ 的数值域圆盘 $\overline D(1,1)$ 的边界上。

定义有限乘积单位向量 $h_n$：

- 在 $q_n$ 取 $\chi$；
- 在 $J_n^+$ 取每位 $z_n^+$；
- 在 $J_n^-$ 取每位 $z_n^-$；
- 其余全部位取 $\Omega$。

每个 $h_n$ 的纯一阶中心恰为
$$
\sum_j a_j\langle S_j(h_n)_j,(h_n)_j\rangle
=A_n\frac{1+iR_n}{A_n}
+A_n\frac{1-iR_n}{A_n}=2.
\tag{2.4}
$$
标记位系数为0，不增加中心。

不同 $h_n$ 正交：在 $q_n$，$h_n$ 取 $\chi$，其他 $h_k$ 取 $\Omega$。
更强地，任何只作用于非标记位的算子都不混合它们的标记配置。

## 3. 同一个向量属于全部真实自然幂域

(1.2) 与共同中心2给
$$
\sup_n\|X^ph_n\|\le
H_p:=\sum_{\ell=0}^p\binom p\ell
2^{p-\ell}C_\ell\|a\|_2^\ell<\infty.
\tag{3.1}
$$
置
$$
x=\sum_{n\ge1}2^{-n}h_n.
\tag{3.2}
$$
由正交性，$\|x\|^2=1/3$，所以 $x\ne0$。
对每个固定 $p$，级数
$\sum_n2^{-n}X^ph_n$ 按范数绝对收敛。
R172 已证真实自然幂 $X^p$ 闭，故
$$
\boxed{
x\in\bigcap_{p\ge1}\operatorname{Dom}X^p,\qquad
X^px=\sum_{n\ge1}2^{-n}X^ph_n.
}
\tag{3.3}
$$
不需要由任意形式级数定义 $X^p$。

## 4. 普通系数截断仍然发散

令 $m_n$ 位于 $J_n^+$ 结束之后、$J_n^-$ 开始之前，定义
$$
X_{<m}=\sum_{j<m}a_jV_j,\qquad
X^0_{<m}=\sum_{j<m}a_jS_j.
$$
所有标记位的系数都为0，所以 $X^0_{<m}$ 完全不作用于标记位。
因此
$$
\langle X^0_{<m_n}h_k,h_n\rangle=0\quad(k\ne n).
\tag{4.1}
$$
在 $h_n$ 上，前面所有其他块的参考态都是 $\Omega$，
其一位中心为0；本块只包含正虚中心的一半。
由 (2.3)，
$$
\langle X^0_{<m_n}h_n,h_n\rangle=1+iR_n.
$$
故
$$
\langle X^0_{<m_n}x,h_n\rangle
=2^{-n}(1+iR_n).
\tag{4.2}
$$

实际进位可以混合标记位，但其全部截断扰动已经由 (1.4) 统一支付：
$$
\begin{aligned}
\|X_{<m_n}x\|
&\ge|\langle X_{<m_n}x,h_n\rangle|\\
&\ge 2^{-n}R_n-k_a\|x\|\\
&=2^n-k_a/\sqrt3\longrightarrow\infty.
\end{aligned}
\tag{4.3}
$$
所以全正系数、最大增生、空谱以及全部自然幂域，都不能单独保证通常的
一阶系数截断收敛。

## 5. 两个不交正行的共同全部混合域

还可在每个上述块之后保留一个全新位 $r_n$，
使它与全部标记位和 $J_n^\pm$ 不交。
定义第二条非负行
$$
c_{r_n}=\frac1{n+1},\qquad c_j=0\quad\text{其余位},
$$
并令 $T=X_c$。则 $c\in\ell^2\setminus\ell^1$，$T$ 也最大增生且空谱；
两条系数行的支撑不交。

每个 $h_n$ 在 $c$ 支撑上都取 $\Omega$，所以相对于同一个乘积参考态，
$X$ 的中心为2，$T$ 的中心为0。
(1.1) 对这两行均成立，使用同一个 $\Lambda_{h_n}$。
因此对每个固定长度 $p$，所有由 $X,T$ 组成的有序词 $W$ 都满足
$$
h_n\in\operatorname{Dom}W,\qquad
\sup_n\|Wh_n\|\le H'_p<\infty.
\tag{5.1}
$$
具体地，可取各步加权界
$\max(2+D_s\|a\|_2,D_s\|c\|_2)$ 的有限乘积。
(1.1) 同时保证每一步的真实域，不是先假设强可交换。

于是 (3.2) 的同一个 $x$ 属于每个有限有序词的域。
为避免依赖“混合自然多项式本身闭”，逐个词长归纳即可：
有限部分和及每个前缀词的像均收敛；
在最后一个闭一阶上取图极限，得到下一词的真实域与作用。
因此
$$
\boxed{x\text{ 属于 }X,T\text{ 的全部有序混合幂域。}}
\tag{5.2}
$$
但是 (4.3) 不变。

若令 $Z=X-T$ 为对应有符号系数的真实闭一阶，则其系数有两条
不可和的相反射线，故 $Z$ 属于全平面谱分支。
在 $\operatorname{Dom}X\cap\operatorname{Dom}T$ 上，
通常伴随有限柱核心的弱式给出真实等式 $Z=X-T$。
由 (5.2) 逐步应用，$x$ 也属于全部 $\operatorname{Dom}Z^p$。

这直接说明：R196 的共同正域结论，即使再加强为全部混合幂域，
仍不足以允许在一个指定向量上无条件取通常坐标系数尾极限。

## 6. 可选的循环性安排与准确边界

如果希望反例向量本身循环，可将每个有限块整体递归远移。
令 $F_n=\{q_n\}\cup J_n^+\cup J_n^-$。
$h_n$ 为这个有限块上的零均值柱函数，因为标记位为 $\chi$。
其 Walsh 系数满足明确的有限加权和
$$
\sum_{F\subseteq F_n}|\widehat h_n(F)|8^{|F|}
=
8\left(\frac{R_n+8}{\sqrt{1+R_n^2}}\right)^{2L_n}.
\tag{6.1}
$$
因此选块的最小物理位足够大，可使
$$
2^{-n}\sum_F|\widehat h_n(F)|8^{|F|}
\sum_{j\in F}\eta_j\le2^{-n}.
\tag{6.2}
$$
每步只需压住一个已知有限常数，实际 $\eta_j\to0$ 保证可行。
插入这些零系数间隔不改变第2—5节的质量、中心与截断计算。
R136 的不交有限块定理随即给 $x$ 循环。

这一可选安排也强调本稿的边界：$x$ 不是未知非零有界分支
$M$ 中的反例。它不能用于宣称慢平方核存在。
本稿只排除一种证明补法——从共同正域或全幂域直接推出普通系数截断收敛。
固定正则器 $R(t)$ 的图逼近、有限柱图核心及 R196 的真实闭域等式
均未受影响。

内部来源：R181 §§2–3、R172 自然幂闭性、R136 不交有限块的可检查 carry 条件。
