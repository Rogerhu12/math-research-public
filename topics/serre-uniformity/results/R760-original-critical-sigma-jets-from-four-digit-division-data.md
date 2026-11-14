# R760：原点临界 sigma 系数的除法多项式四位精度接口

日期：2026-11-14。状态：**已证明的准确接口。**
本篇在原 $O$ 点、原 $c=0$ sigma 规范下，从同一 $\psi_p$ 的最高
$N+1$ 个系数模 $p^4$，精确恢复原 $A_p,A_{p-3}$，以及每个正本原
标签 $h$ 的两个临界 Cartier 系数的单位判据。
全部除 $p^3$ 的操作先证明整除性；全部截断、普通导数阶乘和
Legendre 范数因子保留。

这给出了 R757 的完整除法多项式模 $p^2$ 结论与原临界截面的精确关系：
前者的精度尚未包含需要的 $T$ 项，后者首次出现在原最高系数的
$p^3$ 修正中。本篇没有证明两个临界系数对同一真本原 $h$ 同时为单位。

## 1. 原规范和截断

固定
$$
E_0:y^2=x^3-1,\qquad dz=dx/(2y),\qquad
p=6N+5\ge41,\qquad M=(p^2-1)/6.
\tag{760.1}
$$
$\psi_p$ 是 R753/R757 的标准原除法多项式，首项 $p x^{3M}$。
$\sigma$ 始终是原 Weierstrass sigma，
$$
D_z^2\log\sigma=-x,\qquad
\sigma(z)=z+O(z^7).
\tag{760.2}
$$
原三次 CM 协变性是 $\sigma(\zeta z)=\zeta\sigma(z)$。

保留 R698 的
$$
u=x^{-1/2}=z+O(z^7),\qquad w=u^6,
$$
$$
C(w)=\sum_{j\ge0}\frac{\binom{2j}{j}}{4^j}w^j,\qquad
Z(w)=\sum_{j\ge0}\frac{\binom{2j}{j}}{4^j(6j+1)}w^j,
\tag{760.3}
$$
$$
L(w)=\log T(w)=\sum_{j\ge1}\frac{h_j}{j}w^j,\qquad
h_0=1,\quad h_j=\frac{6j-4}{6j-1}h_{j-1}.
\tag{760.4}
$$
于是
$$
z=uZ(w),\qquad \frac{dz}{du}=C(w),\qquad
\sigma(z)^6=u^6T(w),
\tag{760.5}
$$
以及两个原截面
$$
F(z)=x(z)\sigma(z)^6=u^4T(w),\qquad
G(z)=-x(z)y(z)\sigma(z)^6=uT(w)/C(w).
\tag{760.6}
$$

本篇只在
$$
R_N=\mathbf Z_p[w]/(w^{N+1}),\qquad
\overline R_N=\mathbf F_p[w]/(w^{N+1})
\tag{760.7}
$$
中作低阶抽取。此范围内 $C,Z,L,T$ 的每个系数都整：
各分母 $j,6j-1,6j+1$ 均为单位，且 $N<p$。
所有有限指数、对数、倒数和幂的常数项规范都由
$C(0)=Z(0)=T(0)=1$、$L(0)=0$ 固定。

## 2. 原最高系数的首个 sigma 修正

令
$$
Q_p(w)=u^{p^2-1}\psi_p(u^{-2})
=\sum_{j=0}^M q_jw^j,
\qquad q_0=p.
\tag{760.8}
$$
因此 $q_j$ 就是原 $\psi_p$ 的 $x^{3(M-j)}$ 系数。
下面只保留 $q_0,\ldots,q_N$，不需要重新生成全部约 $p^2/6$ 个系数。

**定理 760.1。** 在 $R_N$ 中，
$$
\boxed{
Q_p(w)\equiv pZ(w)-\frac{p^3}{6}Z(w)L(w)\pmod{p^5}.
}
\tag{760.9}
$$
特别有系数逐项的整除性
$$
pZ(w)-Q_p(w)\in p^3wR_N,
\tag{760.10}
$$
并可定义实际的整多项式截断
$$
\boxed{
D_p(w)=\frac{6}{p^3}Z(w)^{-1}\bigl(pZ(w)-Q_p(w)\bigr)
\in wR_N,\qquad
D_p(w)\equiv L(w)\pmod{p^2}.
}
\tag{760.11}
$$

证明。由 (760.5)，$z(u)$、其组合逆 $u(z)$、
$\sigma(z(u))/u=\exp(L(u^6)/6)$ 在这里涉及的所有次数
都 $p$ 整。相应 $z$ 次数至多 $6N+1=p-4<p$，
所以组合反演与有限指数中的所有整数分母也是单位。
原 sigma 在这个范围的系数因此都 $p$ 整。
又因为 (760.2) 的首个可能高项为 $z^7$，
$$
\frac{\sigma(pz(u))}{u}\equiv pZ(w)\pmod{p^7}
\quad\text{于 }R_N.
\tag{760.12}
$$
这里 $z(u)$ 的全部所需系数整，故代入 $pz(u)$ 的任何
$z^{6j+1}$ 高项都有至少 $p^{6j+1}$，$j\ge1$。

同一个原 sigma 乘法恒等式给
$$
Q_p(w)=\frac{\sigma(pz(u))}{u}\exp(-p^2L(w)/6).
\tag{760.13}
$$
$L\in wR_N$，而有限指数的各阶乘指标至多 $N<p$，故
$$
\exp(-p^2L/6)\equiv1-p^2L/6\pmod{p^4R_N}.
\tag{760.14}
$$
乘上 (760.12) 的 $pZ$，二次指数项已在 $p^5R_N$ 中；
分子误差在 $p^7R_N$ 中。于是得到 (760.9)。
常数项两边均恰为 $p$，故 (760.10) 没有非零常数项。
$Z$ 的常数为一，逆仍整，因而 (760.11) 的除 $p^3$ 合法；
(760.9) 的 $p^5$ 余项除去 $p^3$ 后给模 $p^2$ 的结论。$\square$

因此实际恢复 $\overline D_p$ 所需的有限输入是：

- 原 $q_j$，$0\le j\le N$，各保留模 $p^4$；
- 原有理 $Z_j$，$0\le j\le N$，保留模 $p^3$；
- 系数差的已证明 $p^3$ 整除性，再作一次除法；
- 最后的 $Z^{-1}$ 只需模 $p$。

原 $q_j$ 若只保留模 $p^2$，不能除 $p^3$ 后猜一个模 $p$ 值。
R757 的结论恰在这个更浅精度将 $L$ 项消掉，二者没有矛盾。

## 3. 原两个端点临界系数的完整桥接

定义
$$
\mathcal T_p(w)=\exp(\overline D_p(w))
\quad\text{于 }\overline R_N.
\tag{760.15}
$$
因为 $N<p$，有限指数每个非零阶乘都是单位。
(760.11) 证明
$$
\mathcal T_p=\overline T
\quad\text{于 }\overline R_N.
\tag{760.16}
$$
令 $\ell_2=(2/p)\in\{\pm1\}$。于是同一原 R697 的算术平方根满足
$$
\boxed{
A_p=-\ell_2[w^N]\mathcal T_p C,\qquad
A_{p-3}=\frac23\ell_2[w^N]\mathcal T_p Z^3
\pmod p.
}
\tag{760.17}
$$
相应原 Kronecker/Cartier 数为
$$
\boxed{
C_p=-3\bigl([w^N]\mathcal T_p C\bigr)^2,\qquad
C_{p-3}=-\frac43\bigl([w^N]\mathcal T_p Z^3\bigr)^2
\pmod p.
}
\tag{760.18}
$$
这些不是新定义，而是原 $A_k,C_k$ 的等式。
原 $C_p$ 与 $C_{p-3}$ 的完整六挠逆 sigma 因子已由 R697 的
截面平方公式固定，本篇不省略或重归一它。

为使该接口不只依赖一个形式代换，下面给直接系数证明。
由形式留数的精确换参，对于 $d\ge0$，
$$
\begin{aligned}
[z^{6d+4}]F(z)
&=\operatorname{Res}_{u=0}
  u^4T(w)\,(uZ(w))^{-(6d+5)}C(w)\,du\\
&=[w^d]T(w)C(w)Z(w)^{-(6d+5)},\\
[z^{6d+1}]G(z)
&=\operatorname{Res}_{u=0}
  \frac{uT(w)}{C(w)}(uZ(w))^{-(6d+2)}C(w)\,du\\
&=[w^d]T(w)Z(w)^{-(6d+2)}.
\end{aligned}
\tag{760.19}
$$
特别这里没有增加一个可能不可除的 $6d+1$ 或 $6d+4$ 因子。

在 $\overline R_N$ 中 $Z^p=1$，因为 $Z$ 的常数为一且 $N<p$。
对第一式取 $d=N$，其指数 $6N+5=p$；
对第二式取 $d=N$，其指数 $6N+2=p-3$。
于是相应普通 Taylor 系数分别为 $[w^N]TC$、$[w^N]TZ^3$。
原 R697 使用的都是普通导数：
$$
A_p=2^{-(p-1)/2}(p-1)![z^{p-1}]F,
$$
$$
A_{p-3}=2^{-(p-5)/2}(p-4)![z^{p-4}]G.
$$
由
$$
(p-1)!\equiv-1,\quad (p-4)!\equiv1/6,\quad
2^{-(p-1)/2}=\ell_2,\quad 2^{-(p-5)/2}=4\ell_2
$$
得到 (760.17)。
最后用原平方式 $C_p\equiv-3A_p^2$、
$C_{p-3}\equiv-3A_{p-3}^2$，得到 (760.18)。

## 4. 同一正本原 h 的两个低权通道

现在取
$$
h=6a+1,\qquad 1\le a\le N,\qquad \gcd(h,p+1)=1.
\tag{760.20}
$$
这正是 R727 的全部非端点正本原标签；
$h=1$ 的端点已由 §3 单独保留，不能写一个不存在的 $C_{-1}$。

置
$$
k_1=h-2=6a-1,\qquad
k_2=p-h-2=6(N-a)+2.
\tag{760.21}
$$
二者都在 $2,\ldots,p-1$ 中，且分别属于原 $F$ 与 $G$ 支。
定义两个完全有限的原剩余系数
$$
\boxed{
U_h=[w^{a-1}]\mathcal T_p C Z^{\,2-h},\qquad
V_h=[w^{N-a}]\mathcal T_p Z^{\,h+2}.
}
\tag{760.22}
$$
所有负整数幂都以常数一的 $Z$ 作有限逆幂，
不涉及一个未知代数数的除法。

由 (760.19)，
$$
[z^{k_1-1}]F
=[w^{a-1}]TCZ^{-k_1},
$$
$$
[z^{k_2-1}]G
=[w^{N-a}]TZ^{-k_2}
=[w^{N-a}]TZ^{h+2}\pmod p,
$$
最后一步只用 $k_2=p-h-2$、$Z^p=1$。
所以原普通导数规范是
$$
\boxed{
A_{k_1}
=2^{-(h-3)/2}(h-3)!\,U_h,\qquad
A_{k_2}
=2^{-(p-h-4)/2}(p-h-3)!\,V_h
\pmod p.
}
\tag{760.23}
$$
所有阶乘指标都严格小于 $p$；两个幂指数均为整数；
这些显示因子都是单位。再由 R697 的两个原平方公式，
$$
\boxed{
C_{h-2}\in\mathbf Z_p^\times\iff U_h\ne0,\qquad
C_{p-h-2}\in\mathbf Z_p^\times\iff V_h\ne0.
}
\tag{760.24}
$$

保留同一个有限原向量与原环面，R727 证明其范数为
$$
\overline N_h
=-P_{h-1}(1/s)^2,\qquad s^2=-3,
\tag{760.25}
$$
其中 $P_d$ 是标准 Legendre 多项式。
$h-1$ 为六的倍数，故 $P_{h-1}(1/s)$ 只含 $s$ 的偶次幂，
实际属于 $\mathbf F_p$；选取 $s$ 的另一平方根不改变该值。
于是同一真本原标签的三个单位条件精确等价于
$$
\boxed{
P_{h-1}(1/s)\,U_h\,V_h\ne0.
}
\tag{760.26}
$$
该式的 $N_h$、两个 $C$ 和 $h$ 同时固定，不能把不同标签的非零值拼合。

当 (760.26) 成立时，原 R727 的完整规范给
$v_p(M_{2,h})=-2$，并给该原 scalar primitive 在 $v_p(a-1)>3$
只在中心为零的完整尾结论。这个推论仍不是正秩有理点或真实高度排除。

端点 $h=1$ 的范数值为 $\overline N_1=-1$；
其两个相应有限系数是 §3 的
$[w^N]\mathcal T_p C$ 和 $[w^N]\mathcal T_p Z^3$。
因此 §3 与 (760.22)–(760.26) 共同覆盖全部原正本原标签。

## 5. 原 Gaussian 规范为何必须保留

对任何特征零常数 $c$，令
$$
\sigma_c(z)=e^{cz^2/2}\sigma(z).
$$
那么对每个整数 $n$，
$$
\frac{\sigma_c(nz)}{\sigma_c(z)^{n^2}}
=\frac{e^{cn^2z^2/2}\sigma(nz)}
       {e^{cn^2z^2/2}\sigma(z)^{n^2}}
=\frac{\sigma(nz)}{\sigma(z)^{n^2}}.
\tag{760.27}
$$
所以全部除法多项式在此修改下保持不变，不仅是模 $p^2$ 不变。

原截面却会变成
$$
F_c=e^{3cz^2}F,\qquad G_c=e^{3cz^2}G.
\tag{760.28}
$$
比如 $F=z^4+\cdots$，故
$$
[z^{p-1}]F_c
=\sum_{r=0}^{(p-5)/2}\frac{(3c)^r}{r!}
 [z^{p-1-2r}]F
\tag{760.29}
$$
是关于 $c$ 的非恒定多项式，
最高项为
$$
\frac{3^{(p-5)/2}}{((p-5)/2)!}c^{(p-5)/2}.
$$
其系数在 $p$ 处为单位；因此不能把保持所有 $\psi_n$ 的这个修改
视为不改变临界导数。

本篇不允许这种自由修改。原条件
$D_z^2\log\sigma=-x$ 及 $\sigma=z+O(z^7)$ 已固定 $c=0$；
原 $\mu_3$ 协变性也独立迫使 $c=0$，
因为 $\sigma_c(\zeta z)/(\zeta\sigma_c(z))
=e^{c(\zeta^2-1)z^2/2}$。
若错误地改用 $\sigma_c$，(760.12) 便会出现新的
$p^3cz(u)^3/(2u)$ 项，恰与分母的 Gaussian 修正抵消。
所以 (760.11) 提取的是**已固定的原 $c=0$ sigma**，
不是从 division 数据自动选择任意 Gaussian。

(760.29) 的其他参数根不构成原 $C_p$ 的反例，
因为它们已经离开原 CM theta 截面。

## 6. 可复用旧除法多项式的具体换模型式

若输入来自 R735 已完成的 $E_{27}:Y^2=X^3+16$，
不必重算另一条 $p$-除法多项式。
原同构方向为
$$
(X,Y)=(v^2x,v^3y),\qquad v^6=-16,
$$
所以标准权的除法多项式满足
$$
\psi_p^{(27)}(v^2x)=v^{p^2-1}\psi_p^{(0)}(x)
=(-16)^M\psi_p^{(0)}(x).
\tag{760.30}
$$
令
$$
U=64/X^3,\qquad
Q_{27}(U)=X^{-(p^2-1)/2}\psi_p^{(27)}(X).
$$
其最高 $U^M$ 系数为
$$
\psi_p^{(27)}(0)/64^M=-1,
$$
因为 R753 的三挠点原递推在 $b=16$ 给
$\psi_p^{(27)}(0)=-(4\cdot16)^M=-64^M$。
因此 R735 的首一 $U$ 模数准确为
$$
P_{27}(U)=-Q_{27}(U),\qquad P_{27}(0)=-p.
\tag{760.31}
$$
若 $P_{27}(U)=\sum_{j=0}^M d_jU^j$，则原 $E_0$ 的最高系数为
$$
\boxed{
q_j=-(-4)^j d_j\qquad(0\le j\le M).
}
\tag{760.32}
$$
证明是将第 $j$ 项的 $64^j$ 坐标因子与 (760.30) 的
$(-16)^{-j}$ 相乘，得到 $(-4)^j$，再保留 (760.31) 的负号。
这特别给 $q_0=p$，与 (760.8) 一致。

因此已保存的 R735 首一模数可直接供应本接口的 $q_0,\ldots,q_N$；
若做新算法校验，只需读取既有文件及 SHA，
不应重算 R735 的原 280 维除法代数、模型迹或原挠点乘积。
本篇没有声称已运行该复用抽取，也没有把一个未执行脚本当成实际结果。

## 7. 已关闭与仍开放的准确边界

已证明的是一个保持原点、原微分、原二次指数、原六挠截面、
全部阶乘和同一原本原标签的有限精度接口：

1. 原 $\psi_p$ 的最高 $N+1$ 个系数模 $p^4$ 决定
   $\overline D_p$，除 $p^3$ 有完整整除证明。
2. 它恢复同一个 $\overline T$，并通过 (760.17)、(760.23)
   给原 $A_k,C_k$，无需丢弃 inverse-sigma 或换成移位权。
3. 与 Legendre 原范数一起，(760.26) 是逐个真实本原标签的完整三单位判据。
4. 已完成的 R735 原除法模数可按 (760.32) 复用，不需重新求除法多项式。

仍未证明：对每个充分大的允许 $p$，存在同一个真本原 $h$
使 (760.26) 非零。
R757 的非恒定 Frobenius 常数单位不自动决定上述较深精度的
指数系数；Legendre 范数单位也不自动决定 $U_hV_h$。
此接口不替代这一非零机制，更不改变原高度问题的完成标准。

## 依赖

- [R757](R757-full-original-division-polynomial-mod-p2-and-Frobenius-constant-units.md)：
  原 $\psi_p$、sigma 乘法方向及完整高端点控制。
- [R698](R698-two-actual-square-roots-at-one-low-degree.md)、
  [R697](R697-original-sigma-six-sections-and-integral-square-roots.md)：
  原 $F,G,T,Z,C$、算术平方根、全部普通导数规范。
- [R727](R727-other-primitive-embeddings-toric-norm-and-original-M2.md)：
  同时运输原向量与环面的范数、同标签两个通道及完整尾。
- [R735](R735-exact-original-p41-CM-model-and-Neron-input.md)：
  已完成并可复用的原 $U$ 模数。

