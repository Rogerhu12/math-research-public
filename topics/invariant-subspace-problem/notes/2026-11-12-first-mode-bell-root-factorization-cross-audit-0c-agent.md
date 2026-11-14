# 一模式 Bell 多项式分裂与有限例外循环性：R142 独立交叉核验

日期：2026-11-12。作者：l2_moments。
状态：根代理提出的 R142 机制已经独立逐式核验通过。本文是独占审稿记录，不另占正式结果号，也不修改根主稿。

## 1. 精确输入及 Banach 系数分裂

设
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2,\quad a\ne0,
$$
记
$$
j_0=\min\{j:a_j\ne0\},\qquad
h=2^{j_0},\qquad a=a_{j_0},\qquad d=d_{j_0}=W_h.
$$
此处仅本记录中以标量 $a$ 表示首个非零系数。$X=X_u$ 是 R125 的闭乘子。

R134 给有界 Bell 修正 $B_k=B^{(k)}(0)$，满足
$$
B_0=I,\qquad B_1=0,\qquad
u^p=\sum_{k=0}^p\binom pk B_kX^{p-k}1,
\qquad1\in\operatorname{Dom}X^p.
\tag{1.1}
$$
其有限生成函数为
$$
B_N(t)=\prod_{j<N}
e^{-ta_jV_j}\bigl(\cosh(ta_j)I+V_j\sinh(ta_j)\bigr).
$$
它在紧圆盘上一致算子范数收敛。因为所有非零系数的指标至少为 $j_0$，
$$
B_k\in\mathcal A_h=\overline{\mathbb C[I,A^h]},\qquad
\chi(B_k)=0\quad(k\ge1).
\tag{1.2}
$$
后一个等式来自每个有限因子的常数特征恒为 $1$，故 $\chi(B(t))=1$。

令 $q$ 是次数 $p\ge1$、根全部简单的首一标量多项式，根集合记为
$\{\rho_1,\ldots,\rho_p\}$。定义真正的算子系数多项式
$$
\mathcal P(w)=\sum_{k=0}^p B_k\frac{q^{(k)}(w)}{k!}.
\tag{1.3}
$$
它对 $w$ 首一，且在唯一特征上退化为 $q(w)$。

考虑有限个复变量 $b_2,\ldots,b_p$。对每个简单根 $\rho$，通常复解析隐函数定理给零点附近收敛的芽
$$
y_\rho(b_2,\ldots,b_p),\qquad y_\rho(0)=\rho,
$$
使
$$
q(w)+\sum_{k=2}^pb_k\frac{q^{(k)}(w)}{k!}
=\prod_{\rho}(w-y_\rho(b)).
\tag{1.4}
$$

这些芽可以真实地在 $(B_2,\ldots,B_p)$ 上求值，不需要它们的算子范数本身小。事实上各 $B_k$ 拟幂零；对任意 $\varepsilon>0$，存在固定 $C_k$ 使
$$
\|B_k^n\|\le C_k\varepsilon^n\quad(n\ge0).
$$
一个收敛多变量芽的系数至多按总次数指数增长。取足够小 $\varepsilon$，使用交换性，
$$
\left\|\prod_{k=2}^pB_k^{\nu_k}\right\|
\le\left(\prod_{k=2}^pC_k\right)\varepsilon^{|\nu|},
$$
其全部 Taylor 项按算子范数绝对可和。解析恒等式和乘法也因此可逐项求值。

所以
$$
Y_\rho:=y_\rho(B_2,\ldots,B_p)\in\mathcal A_h,\qquad
\chi(Y_\rho)=\rho,
$$
并有真实的有界系数因式分解
$$
\boxed{\mathcal P(w)=\prod_\rho(w-Y_\rho).}
\tag{1.5}
$$
$p=1$ 时没有 $b$ 变量，$Y_\rho=\rho I$，同一结论直接成立。

## 2. 首个形式系数：所有抵消的核验

以 $c_h(T)$ 表示 $\mathcal A_h$ 中 $A^h$ 的普通形式系数，不作 $W_h$ 归一化。置 $x=z^h/d$，最低局部因子为
$$
v(z)=\frac{1-x}{1+x}=1-2x+O(x^2).
$$
在 $v=1$ 处对
$$
e^{-tav}(\cosh(ta)+v\sinh(ta))
$$
作一阶展开，得到 $z^h$ 的系数
$$
\frac{e^{-2at}-1+2at}{d}.
\tag{2.1}
$$
其余局部因子的首正阶至少为 $2h$，而所有因子的常数特征为 $1$。
因此
$$
\boxed{c_h(B_k)=\frac{(-2a)^k}{d}\quad(k\ge2).}
\tag{2.2}
$$
$B_1=0$ 与 (2.1) 的一阶导数为零一致。

由 Taylor 恒等式，
$$
c_h(\mathcal P(w))
=\frac{q(w-2a)-q(w)+2a q'(w)}d.
\tag{2.3}
$$
在根 $w=\rho$ 处，隐函数的一阶系数满足
$$
q'(\rho)c_h(Y_\rho)
+\frac{q(\rho-2a)+2a q'(\rho)}d=0.
$$
因此
$$
\boxed{
c_h(Y_\rho)
=-\frac{q(\rho-2a)+2a q'(\rho)}
{d\,q'(\rho)}.
}
\tag{2.4}
$$

这里使用的是 $\mathcal A_h$ 的首正阶。两个零特征元的乘积首阶至少为
$2h$，所以隐函数的二次及更高 $B_k$ 项不会混入 $c_h$。没有对可能无界的 $X$ 赋予一个不存在的全局常数特征。

## 3. 闭第一阶因子的真实 gauge 差

设
$$
T_\rho=X-Y_\rho,\qquad
\operatorname{Dom}T_\rho=\operatorname{Dom}X.
$$
有界 $C$ 对称扰动使 $T_\rho$ 仍 $C$ 自伴，以有限柱为图核心，并与全部有界交换子域交换。

对 dyadic $\zeta$，R125 给
$$
\gamma_\zeta(X)-X=F_\zeta(A),
$$
其中 $F_\zeta$ 为真正解析芽，且属于 $z^h\mathbb C\{z^h\}$；当
$\zeta^h=1$ 时它为零。若 $\zeta^h\ne1$，它的首阶系数为
$$
c_h(F_\zeta(A))=-\frac{2a}{d}(\zeta^h-1).
\tag{3.1}
$$

R139 的尾余数引理适用于 $Y_\rho\in\mathcal A_h$：
$$
\gamma_\zeta(Y_\rho)-Y_\rho=A^hC_{\zeta,\rho},
\qquad C_{\zeta,\rho}\in\mathcal A_h.
\tag{3.2}
$$
当 $h=1$ 时也合法：若 $\zeta$ 非平凡，零余数投影消失，
R124 的正余数有限和仍可提取 $A$；当 $\zeta=1$ 时差为零。
故不应把 R139 原稿为说明方便写的 $H\ge2$ 当作禁止 $h=1$ 的条件。

用 (2.4)、(3.1)，真实差可写为
$$
\gamma_\zeta(T_\rho)-T_\rho=A^hU_{\zeta,\rho},
$$
且
$$
\boxed{
\chi(U_{\zeta,\rho})
=(\zeta^h-1)
\frac{q(\rho-2a)}{d\,q'(\rho)}.
}
\tag{3.3}
$$
因此若
$$
q(\rho-2a)\ne0,
\tag{3.4}
$$
则对每个 $\zeta^h\ne1$，$U_{\zeta,\rho}$ 为 $\mathcal A$ 单位。
所有域等式合法，因为 $F_\zeta(A)$、$Y_\rho$ 和其 gauge 差都是有界算子。

R122/R125 的闭同域跨核论证于是适用：对
$M=\ker(T_\rho-\lambda I)$，该差在 $M$ 上有稠密像，有限例外群为
$\mu_h$，Fourier 乘积及总支撑论证迫 $M=0$。故
$$
\ker(T_\rho-\lambda I)=0,\qquad
\overline{\operatorname{Ran}(T_\rho-\lambda I)}=H
\quad(\lambda\in\mathbb C).
\tag{3.5}
$$
这一使用只要求有界差为 $A^h$ 乘实际单位；没有把 (3.2) 称作一个真正标量解析芽。

## 4. 同一个有界正则化可用于所有因子

取 R128 对 $X$ 的四正分量正则化 $R=R(t)$，固定任意 $t>0$。它单射、
有界、属于 $\{A\}'$，像包含于 $\operatorname{Dom}X$，并使 $XR$ 有界。
因此
$$
S_\rho:=T_\rho R=XR-Y_\rho R
$$
是有界交换子。由 $T_\rho$、$R$ 单射，$S_\rho$ 单射；由 R88 的
$C$ 对称性，它的像稠密。

若 $v\in\operatorname{Dom}T_\rho$ 对 $A$ 循环，则 $S_\rho v$ 循环，
因为 $S_\rho$ 与 $A$ 交换且全空间像稠密。又真实域交换给
$$
S_\rho v=RT_\rho v.
$$
R88 使 $R$ 保持 $\operatorname{cyc}_A(T_\rho v)$，故该循环空间含循环向量
$S_\rho v$，必为全 $H$。所以
$$
\boxed{v\text{ 循环且 }v\in\operatorname{Dom}T_\rho
\ \Longrightarrow\ T_\rho v\text{ 循环}.}
\tag{4.1}
$$
这是 R132 传递机制的合法应用；没有从全空间稠密像推断未知不变限制的稠密像。

## 5. 全部乘积的定义域与点态输出

R134 已对任意复 $\ell^2$ 系数严格证明 $1\in\operatorname{Dom}X^p$。
每个有界 $Y_\rho$ 与 $X$ 域交换，故也保持所有
$\operatorname{Dom}X^k$ 并与 $X^k$ 交换。于是
$$
T_\rho(\operatorname{Dom}X^k)\subseteq\operatorname{Dom}X^{k-1}
\quad(k\ge1).
$$
因此从 $1$ 开始可以按任意次序合法地施加全部 $p$ 个因子；每一步的输入均处于下一因子的真实定义域。

如果 (3.4) 对全部根成立，则由 $1$ 循环和 (4.1) 逐步得到
$\prod_\rho T_\rho1$ 循环。在 $\operatorname{Dom}X^p$ 上， bounded 系数的通常有限代数展开合法，结合 (1.1)、(1.3)、(1.5) 得
$$
\prod_\rho T_\rho1
=\mathcal P(X)1=q(u).
\tag{5.1}
$$
所以 $q(u)$ 循环。证明无需先构造或证明一个次数 $p$ 的全域 $C$ 自伴闭乘子，也不依赖 $X$ 是否具有空谱。

## 6. 每个固定多项式的有限例外集合

对任意固定非恒定标量多项式 $q$，令 $p=\deg q$。将
$q(z)-\lambda$ 除以其非零首系数变成首一多项式，不改变根或相关非零条件。

若 $\lambda$ 不在
$$
\mathcal E_q(a)=
\{q(c):q'(c)=0\}
\ \cup\
\{q(c):q(c)=q(c-2a)\},
\tag{6.1}
$$
则 $q(z)-\lambda$ 的根全部简单，并且每个根 $\rho$ 都满足
$q(\rho-2a)-\lambda\ne0$。前述定理适用，故
$$
\boxed{\lambda\notin\mathcal E_q(a)
\quad\Longrightarrow\quad q(u)-\lambda\text{ 循环}.}
\tag{6.2}
$$

$q'$ 的次数为 $p-1$。因 $a\ne0$，差多项式
$q(z)-q(z-2a)$ 的次数也恰为 $p-1$，首系数为首系数$(q)\cdot2ap$。
所以
$$
|\mathcal E_q(a)|\le2p-2.
$$
$p=1$ 时两个条件集都为空，恢复全部第一阶结论。

例如 $q(z)=z^2$ 时
$$
\mathcal E_q(a)\subseteq\{0,a^2\},
$$
从而对任意非常数复 $\ell^2$ 第一模式 $u$，$u^2-\lambda$ 在
$\lambda\notin\{0,a^2\}$ 时循环，不要求相位缺陷可和。这个例子没有断言两个候选参数真的产生非循环向量；它们只是不被本次 simple-root 与首阶单位判据处理。

## 7. 审核结论

全部关键链条已闭合：

- Bell 系数的算子范数收敛、所属尾代数与零特征；
- simple-root 解析分裂在有限个交换拟幂零系数上的真实求值；
- $c_h(B_k)$、隐函数根首系数及 gauge 单位字符的完整抵消；
- 有界扰动后的闭域、$C$ 自伴和同域 gauge；
- 固定第一阶正则化对每个闭因子的循环性传递；
- 所有中间乘积的幂定义域与真实点态输出；
- 有限例外集的准确次数计数。

尚未通过本机制排除的是 (6.1) 中的候选参数，以及一般多模式或无限秩二阶向量。不能把“有限例外”改写成“所有参数”。
