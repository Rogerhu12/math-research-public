# R28. 固定中心差分算子不存在代数形式逆像

**状态：已证明。** 日期：2026-11-12。会话：Astra-rank2-Sha。

本结果加强 R22：原始固定函数 $\Phi$ 不仅没有所述有理函数逆像，
而且没有代数形式函数逆像。因此，若以后能对相应形式解证明任何
适用的代数化定理，已经足以产生矛盾，无须再证明该解在 $E$ 上有理。
**这里没有证明所需形式解满足代数化定理的算术假设，也没有完成无穷素数目标。**

## 1. 一般命题

设 $k$ 为特征零代数闭域，$E/k$ 为椭圆曲线，$O$ 为原点，
$a>1$ 为整数。设 $R\in k(E)^\times$ 非常数，在 $O$ 有限非零。
假定存在有限集 $S\subset E(k)$，满足
$$
\operatorname{supp}(\operatorname{div}R)\subseteq S,
\qquad [a]|_S:S\longrightarrow S\text{ 为双射}.
\tag{1.1}
$$
取 $O$ 处形式参数 $t$，令 $\sigma$ 作用于 $k((t))$，定义为
$$
\sigma F=F\circ[a].
$$
因为 $[a]^*t=at+O(t^2)$，它确实是 $k((t))$ 的一个域自同构。
对非零乘法形式函数定义
$$
\mathcal D_a F=\frac{\sigma F}{F^a}.
$$

**命题。** 对任意 $m\ge1$、$N\in\mathbb Z\setminus\{0\}$
及 $C\in k^\times$，不存在在 $k(E)$ 上代数的
$F\in k[[t]]^\times$，使
$$
\mathcal D_a^mF=C R^N.
\tag{1.2}
$$
其中重复算子按乘法群解释，即
$$
\mathcal D_a^mF
=\prod_{j=0}^m(\sigma^jF)^{\binom mj(-a)^{m-j}}.
\tag{1.3}
$$

## 2. 从代数形式解构造稳定的有限覆盖

反设存在这样的 $F$。在 $k((t))$ 内令
$$
L=k(E)(F,\sigma F,\ldots,\sigma^{m-1}F).
\tag{2.1}
$$
$L/k(E)$ 是有限扩张。式 (1.2) 中 $\sigma^mF$ 的指数为一，
所以可解出 $\sigma^mF\in L$；又 $\sigma(k(E))=[a]^*k(E)\subset k(E)$，
因此
$$
\sigma L\subseteq L.
\tag{2.2}
$$

令 $C_0$ 为函数域 $L$ 的光滑射影曲线。域包含与域嵌入分别给出有限态射
$$
\pi:C_0\longrightarrow E,
\qquad \alpha:C_0\longrightarrow C_0,
\qquad \pi\alpha=[a]\pi.
\tag{2.3}
$$
记 $d=[L:k(E)]$。两个域塔给出
$$
[L:\sigma k(E)]=d\,[k(E):\sigma k(E)]=d a^2,
$$
以及
$$
[L:\sigma k(E)]=[L:\sigma L]\,[\sigma L:\sigma k(E)]
=[L:\sigma L]d.
$$
故
$$
\deg\alpha=[L:\sigma L]=a^2>1.
\tag{2.4}
$$

嵌入 $L\subset k((t))$ 所给的 $t$-进赋值确定 $Q\in C_0(k)$。
基域参数 $t\in k(E)$ 在此赋值为一，$L$ 的值群又包含于 $\mathbb Z$，
所以该分支的分歧指数恰为一，且 $\pi(Q)=O$。
对任意 $f\in L^\times$，形式代入 $t\mapsto at+O(t^2)$ 保持首项阶数，
故 $v_Q(\sigma f)=v_Q(f)$。这说明 $\alpha(Q)=Q$，并且该自映射在
此形式分支也无分歧。这里的固定性来自同一个形式域嵌入，
不是从覆盖中任意选择一个 $O$ 的逆像。

## 3. 覆盖曲线必为椭圆曲线，自映射必为乘以 $a$

由于 $\pi$ 非常数，Riemann–Hurwitz 给
$$
2g(C_0)-2=\deg(\pi)(2g(E)-2)+\deg\operatorname{Ram}(\pi)
\ge0,
$$
所以 $g(C_0)\ge1$。另一方面，应用于度数 $a^2$ 的 $\alpha$，有
$$
2g(C_0)-2=a^2(2g(C_0)-2)+\deg\operatorname{Ram}(\alpha).
$$
这排除 $g(C_0)\ge2$。于是 $g(C_0)=1$，且 $\pi,\alpha$ 均 étale。

以 $Q$ 为原点，把 $C_0$ 看作椭圆曲线。$\pi$ 和 $\alpha$ 都保持原点，
故为群同态；$\pi$ 是同源。由 (2.3)，同态
$\alpha-[a]_{C_0}$ 的像包含于有限群 $\ker\pi$。
连通曲线在有限群中的像为一点，因此
$$
\alpha=[a]_{C_0}.
\tag{3.1}
$$

令 $D=\operatorname{div}_{C_0}(F)$。对 (1.2) 取除子得到
$$
([a]^*-a)^mD=N\pi^*(\operatorname{div}_E R).
\tag{3.2}
$$
右端非零，因为 $R$ 非常数、$N\ne0$，而有限态射的除子拉回是单射。

## 4. 消除覆盖核中与 $a$ 有关的部分

不能立即断言 $[a]$ 在 $\pi^{-1}S$ 上双射：如果 $\deg\pi$ 与 $a$
有公因子，该断言可能不成立。以下下降专门处理这个问题。

设
$$
K_0=\{Q'\in\ker\pi:\ [a]^nQ'=0\text{ 对某个 }n\ge0\}.
$$
这是 $\ker\pi$ 中所有阶数的素因子均整除 $a$ 的部分。
选 $n_0$ 使 $[a]^{n_0}K_0=0$。令
$$
W=\operatorname{Div}(C_0)_{\mathbb Q},\qquad
W^{K_0}=\{D':\tau_{Q'}^*D'=D'\text{ 对所有 }Q'\in K_0\},
$$
其中 $\tau_{Q'}$ 为平移。记 $A=[a]^*$。
恒等式
$$
\tau_{Q'}^* A=A\tau_{aQ'}^*
\tag{4.1}
$$
说明 $A$ 保持 $W^{K_0}$，所以在商空间 $W/W^{K_0}$ 上诱导算子。
又对任意 $D'\in W$ 和 $Q'\in K_0$，有
$$
\tau_{Q'}^*A^{n_0}D'
=A^{n_0}\tau_{a^{n_0}Q'}^*D'=A^{n_0}D',
$$
因此 $A^{n_0}=0$ 作用于该商。由于 $a\ne0$，
$A-a=-a(1-A/a)$ 在该商上可逆，其逆由有限几何级数给出。

式 (3.2) 的右端来自 $\pi$ 的拉回，故属于 $W^{K_0}$。
在商空间中于是有 $(A-a)^m\overline D=0$，可逆性强迫
$\overline D=0$。即 $D$ 对全部 $K_0$ 平移不变。

令
$$
q:C_0\longrightarrow C_1=C_0/K_0,
\qquad \pi=\pi_1q.
$$
因为 $q$ 是 étale 的有限群商，平移不变的除子在每个纤维上系数相同，
所以存在 $D_1\in\operatorname{Div}(C_1)_{\mathbb Q}$，使
$$
D=q^*D_1.
\tag{4.2}
$$
**这里只要求除子下降；没有要求 $F$ 本身下降，也没有要求 $D_1$ 主。**
由于 $q$ 与 $[a]$ 交换，并且拉回 $q^*$ 单射，式 (3.2) 下降为
$$
([a]^*-a)^mD_1=N\pi_1^*(\operatorname{div}_E R).
\tag{4.3}
$$

现在 $\ker\pi_1\simeq\ker\pi/K_0$ 的阶与 $a$ 互素。
令 $S_1=\pi_1^{-1}S$。由 (1.1)，$[a]$ 将 $S_1$ 映入自身。
在各个纤维上，乘以 $a$ 在 $\ker\pi_1$ 中为自同构；同时它双射置换
底空间的 $S$。因此 $[a]|_{S_1}$ 为双射。

置 $D_2=([a]^*-a)^{m-1}D_1$。则 (4.3) 成为
$$
([a]^*-a)D_2=N\pi_1^*(\operatorname{div}R),
$$
其右边是非零、支撑于 $S_1$ 的有限除子。
这与 R22 §1 的有限不变支撑引理矛盾：$[a]:C_1\to C_1$ étale、
度为 $a^2>1$，且在 $S_1$ 上双射。命题得证。$\square$

## 5. 本课题中的应用

取 $E:y^2=x^3-17x$、$R=\Phi$、$a=69$。
R19–R22 已证明 $\Phi$ 非常数、$\Phi(O)=1$，其零极点支撑为固定
$\mathfrak f$-除法点集 $S$，其中 $\mathfrak f=(34(1+i))$。
因为 $69\equiv1\pmod{68}$，$[69]$ 固定 $S$ 的每一点。
故上面的命题适用。

更明确地，令 $z=\log_E(t)$，并写
$$
\log\Phi(\exp_E z)=\sum_{k\ge2}b_kz^k.
$$
R19 已证明常数项和一次项均为零。对任意 $m\ge1$、$c\in\overline K$，
形式函数
$$
F_{m,c}(t)=\exp\!\left(
c\log_E(t)+
\sum_{k\ge2}\frac{b_k\log_E(t)^k}{(69^k-69)^m}
\right)
\tag{5.1}
$$
在特征零形式级数意义下良好定义，且满足
$\mathcal D_{69}^mF_{m,c}=\Phi$。因此
$$
\boxed{\ F_{m,c}\text{ 在 }\overline K(E)\text{ 上超越。}\ }
\tag{5.2}
$$
这个结论对所有 $m\ge1$ 成立。它不依赖 $\Sha$ 的有限性假设，
也不把局部 Iwasawa 模中的合法除法等同于固定全局函数的代数除法。

## 依赖与用途

- R19、R22：原始 $\Phi$ 的零极点与不变支撑，以及有限除子引理。
- 一般基础事实：光滑射影曲线与一变量函数域的对应、Riemann–Hurwitz、
  保持原点的椭圆曲线态射为同态、有限群商的除子下降。
- 新增证明为 §§2–4 的稳定覆盖、去除覆盖核的 $a$-primary 部分及除子下降。

若要用反设“几乎所有目标 $p$ 的中心阶数至少四”与 (5.2) 矛盾，
仍必须独立证明某个 $F_{m,c}$ 满足代数化判据的完整假设。
逐 $p$ 的一个字符分量可除，不等于这个固定形式函数的整体整性。
