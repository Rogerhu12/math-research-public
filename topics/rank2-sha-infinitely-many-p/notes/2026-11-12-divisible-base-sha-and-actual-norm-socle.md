# 基曲线可除 Sha 在实际范数核中的像

日期：2026-11-12。状态：下述正合列和配对恒等式已证明。
固定 R126 的实际 $L/F$、$\Gamma=C_p$、范数一阿贝尔簇 $A$，
及 $B=\operatorname{Res}_{L/F}E$。记 $j:A\hookrightarrow B$、
$N:B\to E$，并沿用 R113 的整规范
$\lambda_A=j^\vee j=\iota\delta$。

本篇使用 R126 的**固定 Mordell--Weil 点**分别检测两个局部符号，
而非仅知道通常 Selmer 局部像的 $r_+=r_-=1$。这一区别决定下列
满射确实由 $E(F)$ 实现。

## 1. 全局范数核的实际短正合列

在唯一分歧位 $\lambda\mid\ell$，$L_\lambda/F_\lambda$ 是
剩余特征不为 $p$ 的全分歧 tame 次数 $p$ 扩张。
形式群范数满射，剩余点的范数是乘 $p$，所以
$$
 E(F_\lambda)/N E(L_\lambda)
      \simeq E(\mathbf F_{\ell^2})/pE(\mathbf F_{\ell^2})
      \simeq\mathbf F_p^2.                                  \tag{1}
$$
其 $c$ 两符号各一维。R126 所选固定有理点之一和固定负扭曲点
的实际局部像均非零，故
$$
 E(F)\longrightarrow E(F_\lambda)/N E(L_\lambda)
                         \text{ 满射}.                       \tag{2}
$$
在其余位，R113 已证通常范数满射：$p$ 处是不分歧扩张与好约化，
坏位 $2,17$ 的组件阶与本篇的充分大 $p$ 互素，其他有限位同样
是不分歧好约化；无穷位没有奇数 $p$ 的障碍。

令
$$
 V=\{R\in E(F):R\text{ 在每个位都是局部范数}},\qquad
 C=V/N E(L).
$$
对 $0\to A\xrightarrow jB\xrightarrow NE\to0$ 的全局及局部长
正合列作比较，得到准确的 $p$ 初级短正合列
$$
 0\longrightarrow C\longrightarrow S
  \xrightarrow{j_*}
  \ker\!\left(N:\Sha(E/L)[p^\infty]\to\Sha(E/F)[p^\infty]\right)
  \longrightarrow0,
 \qquad S=\Sha(A/F)[p^\infty].                              \tag{3}
$$
**满射证明。** 对右边的类，先取一个全局 $H^1(F,A)$ 提升。
它在 $v\ne\lambda$ 自动局部为零；在 $\lambda$ 的值来自 (1)。
用 (2) 中的一个真实 $F$-有理点的连接类减去它，即得到 Sha 中的
提升。核恰为处处局部范数的 $F$-点模全局范数，即 $C$。
$pE(F)\subset N E(L)$，故 $C$ 被 $p$ 杀掉。连接映射的
$\Gamma$ 函子性还给 $\delta C=0$。

## 2. 可除部分只向这一范数核贡献一个 p 层

记 $D_F,D_L$ 分别为
$\Sha(E/F)[p^\infty]$、$\Sha(E/L)[p^\infty]$ 的最大可除子群。
这些群的 $p$-余秩有限，因为相应有限 $p$-Selmer 群有限。
R119 已证 $S$ 有限，而 $B$ 与 $E\times A$ 之间的实际同源给
$$
 \operatorname{res}:D_F\longrightarrow D_L
       \text{ 是满射且核有限},\qquad N\operatorname{res}=[p].
 \tag{4}
$$
这里没有假设 $D_F=0$。满射也可直接从同源对可除部分的作用看出：
对可除群的有限余核必为零，而 $A$ 的可除 Sha 已为零。

由 (4) 得到实际恒等式
$$
 \boxed{\ker(N|D_L)=\operatorname{res}(D_F[p]).}              \tag{5}
$$
证明只需写 $x=\operatorname{res}(y)$：$Nx=0$ 恰给 $py=0$。
特别地该核被 $p$ 杀掉。若 $d=\operatorname{corank}_{\mathbf Z_p}D_F$，
$k=\dim\ker(\operatorname{res}|D_F)$，则
$$
 \ker(N|D_L)\simeq(\mathbf Z/p)^{d-k};                       \tag{6}
$$
限制核被 $p$ 杀掉也是 (4) 的直接后果。

令 $S_D=j_*^{-1}(D_L)\subset S$。式 (3)、(5) 给
$$
 0\longrightarrow C\longrightarrow S_D
     \longrightarrow\operatorname{res}(D_F[p])
     \longrightarrow0.                                     \tag{7}
$$
而且
$$
                            S_D\subset S[\delta].           \tag{8}
$$
确实，$j^\vee_*$ 将可除 $D_L$ 映入有限
$\Sha(A^\vee/F)[p^\infty]$，所以为零。于是对 $x\in S_D$，
$\lambda_Ax=j^\vee_*j_*x=0$；整同构 $\iota$ 将此化成
$\delta x=0$。

因此，不能把基曲线的全部可除 $D_F[p^n]$ 逐层塞进同一个有限
$S$ 来制造随 $p$ 增长的长度。其实际范数零来源恰为 (5)，
不是 $\operatorname{res}(D_F[p^n])$（$n>1$）。当然 (8) 也不
说明相应 socle 所在的循环块很短；要证明长块，仍须控制它在
$\delta^mS$ 中的实际提升深度。

## 3. 第二层配对确由 L 上的有限 Sha 商承担

R122 的配对为
$B_A(x,y)=\langle x,\iota y\rangle_{\rm CT}$。
对 $z,z'\in S[\delta^2]$，其第二原始层的配对有准确比较
$$
 \begin{aligned}
 \beta_2(z,z')
 &=B_A(z,\delta z')
   =\langle z,\lambda_Az'\rangle_{\rm CT}\\
 &=\langle j_*z,j_*z'\rangle_{{\rm CT},E/L}.
 \end{aligned}                                               \tag{9}
$$
最后一步是 Cassels--Tate 配对对 $j$ 与 $j^\vee$ 的函子性，
并采用 Weil 限制与 $E/L$ 的标准配对比较。

当 $\delta z,\delta z'\in S_D$ 时，(8) 和函子性给
$\delta j_*z,\delta j_*z'\in D_L$。因此 (9) 真正配对的是
$$
 (\Sha(E/L)[p^\infty]/D_L)^\Gamma
$$
中的相应有限商类。可除部分是普通 Cassels--Tate 配对的 radical，
但 $j_*z$ 本身并未因此成为可除类；故不能把 (9) 判为零。

更一般地，$n\ge2$ 时
$$
 \beta_n(z,z')
 =\langle j_*z,\delta^{n-2}j_*z'\rangle_{{\rm CT},E/L}.       \tag{10}
$$
这给下一步可实际追踪的对象：有限商中的指定提升及其导出配对，
而不是只利用基曲线 $D_F$ 已经可除这一事实。

## 4. 相邻层的准确限制

本篇的辅助位满足 $v_p(\ell+1)=1$，所以同一个 $\ell$ 的反循环
tame 类群方向没有次数 $p^2$ 的延长。不能把 (3) 当成该方向的
某个未构造 $\mathbf Z_p$ 塔的第一层。
R120 构造的真正反循环 $p$-塔在 $p$ 处分歧，是另一个已标记
的实际塔；它提供完整 Heegner norm 族，但没有凭这一点消去
(9) 的有限商类。本篇未证明指定 $Q$ 的 $\delta$ 指数为零。

## 已证接口与来源

R113 给实际同源、限制极化、所有局部范数及完整 Kummer 条件；
R119 使用 Nekovář（2007）Theorem 3.2、§3.5.1 给 $S$ 有限，
[原文](https://webusers.imj-prg.fr/~jan.nekovar/pu/euler.pdf)。
R122 证明全部 $\beta_n$ 的良定义及原始商配对；R126 用真实
固定全局点支付 (2)。式 (3)--(10) 是这些实际对象的长正合列
与同源函子性的直接推论，不另假设基曲线 Sha 有限。
