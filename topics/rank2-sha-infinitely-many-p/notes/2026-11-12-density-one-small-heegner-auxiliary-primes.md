# 密度一输入的实际小辅助素数与完整迹的高度门槛

日期：2026-11-12。状态：辅助素数的选择、密度、全部局部条件和
下述条件式不可除性均已证明。尚未证明实际完整迹点非零，
也未证明其最底增广类非零。本篇不据此宣称 Sha 有限。

固定 R103、R105 的
$$
E:y^2=x^3-17x,\qquad F=\mathbb Q(\sqrt{-15}),\qquad N_E=9248,
$$
以及目标输入集合
$$
\mathcal P_F=\{p\text{ prime}:p\equiv1,17,49,53\pmod{60},\ p\ne17\}.
\tag{1.1}
$$
它恰是除去有限例外后同时在 $F$、$\mathbb Q(i)$ 分裂的素数集合。
固定任意
$$
\frac{32}{17}<L<2.
\tag{1.2}
$$

## 1. 已发表解析输入的精确量词

使用 Fouvry，*On binary cyclotomic polynomials*，
Algebra & Number Theory **7** (2013), 1207–1223，§2.6，
Lemma 6（印刷页 1212）。该处明确重述 Mikawa（2001）的定理：
给定 $L>32/17$ 和 $A,B>0$，对于
$0<|a|\le(\log R)^B$，除至多 $O(R(\log R)^{-A})$ 个
$R<q\le2R$、$(q,a)=1$ 的整数模数外，有
$$
P(q,a):=\min\{\ell\text{ prime}:\ell\equiv a\pmod q\}
\ll q^L.
\tag{1.3}
$$
常数只依赖 $L,A,B$。模数 $q$ 不要求为素数；$a=-1$ 属于允许范围。
这里所需的只是一个固定 $a$，没有对随 $q$ 任意变化的剩余类作统一假设。

直接核读的出版版是
[Fouvry 原文](https://msp.org/ant/2013/7-5/ant-v7-n5-p07-p.pdf)。
被该文准确引用的原始出处是 H. Mikawa，
*On primes in arithmetic progressions*，Tsukuba J. Math.
**25** (2001), 121–153，
[DOI](https://doi.org/10.21099/tkbjm/1496164216)。
本篇直接以已经核读的 Fouvry Lemma 6 为输入。

## 2. 密度一的合法辅助选择，自动具有 M=1

**命题 2.1。** 对每个固定 $A>1$，存在常数 $C=C(L,A)$，使除了
$O_{L,A}(X(\log X)^{-A})$ 个 $p\in\mathcal P_F\cap(X,2X]$ 外，
都能选到素数 $\ell$ 满足
$$
\ell\equiv-1\pmod{1020p},\qquad
\ell\le Cp^L.
\tag{2.1}
$$
对充分大的这些 $p$，还同时有
$$
\begin{gathered}
\ell\text{ 在 }F,\mathbb Q(i)\text{ 均惰性},\qquad
\ell\nmid2\cdot3\cdot5\cdot17,\qquad a_\ell(E)=0,\\
v_p(\ell+1)=1,\qquad
M_\ell=\min\{v_p(\ell+1),v_p(a_\ell(E))\}=1.
\end{gathered}
\tag{2.2}
$$
因此满足 (2.1) 的输入在 $\mathcal P_F$ 中具有相对密度一。

**证明。** 在 (1.3) 取 $a=-1$、$q=1020p$、$R=1020X$。
$p\mapsto1020p$ 是单射，故所有坏输入 $p$ 的数目至多为全部坏整数
模数的数目，即所述异常界。固定进程的素数定理给
$$
\#(\mathcal P_F\cap(X,2X])\sim\frac{X}{4\log X}.
\tag{2.3}
$$
取 $A>1$ 即得相对零密度的异常集；按二进区间求和也得通常的
从 $1$ 到 $X$ 的相对密度结论。

由 $60\mid1020$，有 $\ell\equiv-1\pmod{60}$。
两个虚二次域的二次特征分别为 $\chi_{-15}$、$\chi_{-4}$，
在 $-1$ 的值均为 $-1$，故两处惰性。模 $1020$ 的互素类同时排除
$2,3,5,17$；CM 在 $\mathbb Q(i)$ 的好惰性素数处给 $a_\ell(E)=0$。

最后 $p\mid\ell+1$，而由 $L<2$，
$$
0<\ell+1\le Cp^L+1<p^2
\tag{2.4}
$$
对充分大 $p$ 成立，故 $p^2\nmid\ell+1$。这证明全部 (2.2)。
特别地，不需要再施加一个模 $p^2$ 的进程。$\square$

原 R105 的 $\ell\equiv7\pmod{1020}$ 仅是另一项充分选择，
不是固定构造的必要条件。本命题改用 $-1$ 类，没有同时要求互不相容的
两个模 $1020$ 剩余类。R105 的理想 $\mathfrak r_{3,\ell}$、固定映射
$\Phi$ 和 R107 的 $\mathfrak r_{5,\ell}$ 对这些 $\ell$ 仍全部适用。

### 2.1 实际上每个典型输入有许多小辅助素数

Fouvry 同页 Lemma 7 还给更具体的形式：除 $O(X(\log X)^{-2})$
个输入外，可以在
$$
X^L<\ell\le2X^L,\qquad \ell\equiv-1\pmod{1020p}
\tag{2.5}
$$
中找到 $\gg_L X^{L-1}/\log X$ 个素数。

为核参数，固定 $1/L<K<17/32$，在该引理取 $x=X^L$、
$R=1020X$、$a=-1$。充分大时 $R<x^K$，而该引理的下界为
$\gg x/(\varphi(1020p)\log x)$。因为
$\varphi(1020p)=256(p-1)$，即得所述计数。
若使用其逆剩余类记号，$(-1)^{-1}=-1$，所以没有方向差异。
这些选择也都满足 (2.2)。该计数没有附加 Kummer Frobenius 核线之类的
另一个 Chebotarev 条件。

## 3. 完成全部 prime-to-p 迹后的准确高度界

对选定的 $p,\ell$，令
$$
q=\ell+1=pu,\qquad (p,u)=1,\qquad
G_\ell=\operatorname{Gal}(H_\ell/H_1)\simeq C_{pu}.
$$
记 $U\subset G_\ell$ 为阶 $u$ 的子群。
R105 的实际点和 R104 的完整迹准确为
$$
X_\ell=(1+\tau_{3,\ell})P[\ell],\qquad
Q_{\ell,p}=\operatorname{Tr}_U X_\ell.
\tag{3.1}
$$
它在次数 $p$ 的域
$$
L_{\ell,p}=H_\ell^{\,U\times\langle\tau_{3,\ell}\rangle}
\quad\text{之上有定义},\qquad [L_{\ell,p}:F]=p.
\tag{3.2}
$$
设 $\sigma$ 生成 $\operatorname{Gal}(L_{\ell,p}/F)$，
$N_p=1+\sigma+\cdots+\sigma^{p-1}$。原 Heegner 范数关系给
$$
N_pQ_{\ell,p}=N_{G_\ell}X_\ell=0.
\tag{3.3}
$$
以上是在实际点群中的等式。

由 R105 的固定有限映射高度界及 (2.1)，
$\widehat h(X_\ell)\ll\log p$。Galois 不变的典范高度平方根满足
三角不等式，因此
$$
\widehat h(Q_{\ell,p})
\le u^2\widehat h(X_\ell)
\ll p^{2L-2}\log p=o(p^2).
\tag{3.4}
$$
常数只依赖固定曲线、映射和 $L$。这是完整实际迹的上界，
没有用未知的迹点高度下界。

**推论 3.1。** 对以上充分大输入及任何选定的合法小 $\ell$，有
$$
Q_{\ell,p}\ne O
\quad\Longrightarrow\quad
Q_{\ell,p}\notin pE(H_\ell).
\tag{3.5}
$$

**证明。** R107 已证明 $E(F^{\rm ab})_{\rm tors}=E[2]$。
次数 $p\ge5$ 的群作用于稳定子群 $E(L_{\ell,p})[2]$；
这个子群的自同构群阶数整除 $6$，故作用平凡，
即 $E(L_{\ell,p})[2]=E(F)[2]$。故若 $Q_{\ell,p}$ 是挠点，
(3.3) 便给 $0=N_pQ=pQ=Q$。因此 (3.5) 的前提使 $Q$ 非挠。

若 $Q=pR$、$R\in E(H_\ell)$，那么 $R$ 也是 $F^{\rm ab}$ 中非挠点。
R102 已核的 Baker 定理给固定 $c_{E,F}>0$，所以
$\widehat h(Q)=p^2\widehat h(R)\ge p^2c_{E,F}$，与 (3.4) 矛盾。
$\square$

### 3.1 条件式的实际增广长度

令 $\Delta=\sigma-1$。在 $Q\ne O$ 的同一前提下，
所有 $\Delta^kQ$ 都非挠：在特征零的循环表示中，
$N_pQ=0$ 排除平凡表示，$\Delta$ 在其余部分可逆。
又有 $\widehat h(\Delta^kQ)\le4^k\widehat h(Q)$。
因此存在固定 $C_0$，使
$$
0\le k\le
\left\lfloor(2-L)\log_2p-\tfrac12\log_2\log p-C_0\right\rfloor
\quad\Longrightarrow\quad
\Delta^kQ\notin pE(H_\ell).
\tag{3.6}
$$
证明只需将 (3.4) 代入，并选择 $C_0$ 使
$4^k\widehat h(Q)<p^2c_{E,F}$。
这里的点已经经过全部 $U$ 迹，区别于 R107、R109 对未完成该迹的
$X_\ell$ 所给的无条件长度；(3.6) 仍以这个真实 $Q$ 非零为前提。

## 4. 留下的全局条件

本篇把合法辅助素数减小到 $o(p^2)$，并把完整迹的
“非零且不可 $p$ 除”拆成了唯一尚未支付的非零条件。
没有证明在 (2.1) 或 (2.5) 的任何一个小区间中存在 $Q_{\ell,p}\ne O$。
很多可选素数本身不提供这样的非消失。

即使 (3.5) 已适用，R104 的单素数导出类仍要求
$Q_{\ell,p}\notin\Delta\ker N_p$；
普通的不可 $p$ 除和 (3.6) 的部分增广长度都不等价于这个最底层条件。
本篇没有消去此区别，也没有将当前短区间选择与
R106 的任意指定 Kummer 核线 Chebotarev 选择合并。

## 使用的本课题已证输入

- [R103：固定辅助域与输入进程](2026-11-12-explicit-minus15-heegner-field.md)。
- [R105：固定类群和、范数关系与对数高度](2026-11-12-minus15-classgroup-trace-primitivity.md)。
- [R102：Baker 固定正高度下界](2026-11-12-heegner-height-and-augmentation-primitivity.md)。
- [R107：精确阿贝尔挠点及实际额外二阶迹](2026-11-12-heegner-orbits-and-logarithmic-augmentation-depth.md)。
- [R104：完整实际迹与最底增广条件](2026-11-12-cyclic-heegner-augmentation-and-complete-reduction.md)。
