# R270 第四附录：任意快系数多项式的最大闭包与循环性

日期：2026-11-13（UTC）。作者：kernel；Astra-ISP-1cf8c51d 复核。
状态：已证明。本文接 [R270 第三附录](R270-appendix-closed-first-fast-polynomials-and-all-order-resonant-cyclicity.md)，去掉首一及可逆最高系数条件。
自然多项式域不一定已经闭；本文证明其准确最大闭包，再对全部实际非零求值排核。

**范围订正（2026-11-13）：** 本文的排核范围已有 [R183](R183-fast-coefficient-nonmonic-polynomials-and-closed-fraction-field.md) 和 [R152](R152-fast-gauge-increments-analytic-germs-and-closed-quotients.md)，应定位为独立重证及域范围整理。无界主行 $a\in\ell^2\setminus\ell^1$ 的实际倾斜 $X_b=X+H_{a,b}$ 满足 R183 的 $H_{a,b}\in\mathcal A$ 及快 dyadic 增量条件，故其 §§2–6 已给非首一最大闭包和高阶核内排核，§13.1 已给全空间循环性双向传递。有界主行 $a\in\ell^1$ 由 R152 定理 1.3、§7 覆盖，需保留实际求值非零。没有把任意有界 $A'$ 扰动都纳入这个排核前提。

## 1. 结论

令 $X=X_b$ 为任意复 $\ell^2$ 主 first 在任意复 $\ell^2$ 指数权下的真实闭实现。
取任意多项式
$$
P(t)=\sum_{k=0}^p E_k t^k,\qquad E_k\in\mathcal G.
$$
当 $p\ge1$，其自然求值定义在 $\operatorname{Dom}X^p$：
$$
P_{\rm nat}(X)x=\sum_{k=0}^p E_kX^kx.
\tag{1.1}
$$
$p=0$ 就是有界算子 $E_0$，非零时结论直接来自 R151，以下可设 $p\ge1$。

**定理。** 若 (1.1) 在其实际域上不是零作用，则它可闭，
其闭包单射且值域稠密，并为原空间上的 $C_0$ 自伴闭算子。
自然求值本身也单射且像稠密。
对闭包的任意域向量 $x$，有
$$
\boxed{
x\text{ 对 }A\text{ 循环}
\iff
\overline{P_{\rm nat}(X)}\,x\text{ 对 }A\text{ 循环}.
}
\tag{1.2}
$$
特别，若 $\xi$ 循环且属于 $\operatorname{Dom}X^p$，
则 $P_{\rm nat}(X)\xi$ 循环。

最高系数 $E_p$ 只须是非零 $\mathcal G$ 元素，允许零字符及无有界逆。
定理不把原 $\operatorname{Dom}X^p$ 自动识别为闭包的全部域。

## 2. 实际正则器与非首一多项式最大闭包

固定 R140/R176 的 first 正则器 $R=R(t)$，令 $S=XR$。
两者为有界交换子，$R$ 单射，
$$
R^pH\subset\operatorname{Dom}X^p,\qquad
X^kR^p=S^kR^{p-k}\quad(0\le k\le p).
$$
定义
$$
Z=R^p,\qquad
Q=P_{\rm nat}(X)R^p
=\sum_{k=0}^pE_kS^kR^{p-k}\in\{A\}'.
\tag{2.1}
$$
在自然域上还准确有
$$
ZP_{\rm nat}(X)x=Qx.
\tag{2.2}
$$

R270 闭 first 附录 §2 已证明：对每个有限放大及每个闭
$A^{(d)}$ 不变空间 $\mathcal M$，
$$
\overline{R^{(d)}\mathcal M}=\mathcal M.
$$
迭代同一有界限制，得 $Z^{(d)}$ 也有该性质。

考虑最大图
$$
\mathscr G=\{(x,y)\in H\oplus H:Qx=Zy\}.
\tag{2.3}
$$
$Z$ 单射使它单值、闭；它包含
$$
\{(Zh,Qh):h\in H\},
$$
因此稠密定义。
图在 $A\oplus A$ 下不变。
将 $Z^{(2)}$ 的普遍稠密性用于这张闭图，得到
$$
\overline{Z^{(2)}\mathscr G}=\mathscr G.
$$
又
$$
Z^{(2)}(x,y)=(Zx,Zy)=(Zx,Qx).
$$
所以
$$
\boxed{
\mathscr G=
\overline{\{(Zh,Qh):h\in H\}}.
}
\tag{2.4}
$$

自然 (1.1) 由 (2.2) 包含于 (2.3)，且包含 (2.4) 的原分母核心。
因此自然求值可闭，并且
$$
\boxed{
\widetilde P:=\overline{P_{\rm nat}(X)}
=Z^{-1}Q,\qquad
\operatorname{Dom}\widetilde P
=\{x:Qx\in\operatorname{Ran}Z\}.
}
\tag{2.5}
$$
这在一般有界交换系数情形也成立；这里只在后续排核用 $\mathcal G$。

所有有界交换子对同一个 $C_0$ 对称。
对核心 $T_0(Zh)=Qh$ 取通常伴随，得
$$
Q^*v=Z^*w
\iff
Q(C_0v)=Z(C_0w).
$$
由 (2.4)，
$$
\boxed{\widetilde P=C_0\widetilde P^*C_0.}
\tag{2.6}
$$
(2.5) 作为自然作用的闭包与正则器参数无关。

此外，
$$
Q=0\iff P_{\rm nat}(X)=0.
\tag{2.7}
$$
一方向显然。反向可由 (2.5) 得到：
若 $Q=0$，最大图为全域零算子，自然作用也为零。
也可使用 $R^pH$ 是 $X^p$ 的图核心及低阶相对图界直接证明。
所以主定理的实际非零条件准确等价于 $Q\ne0$。

## 3. Gauge 后同一正则器给同一个核

R270 已完整证明
$$
\gamma_\zeta(X)=X+D_\zeta,\qquad
\operatorname{Dom}\gamma_\zeta(X)^k=\operatorname{Dom}X^k,
\quad D_\zeta\in\mathcal G.
$$
令
$$
P_\zeta(t)=(\alpha_\zeta P)(t+D_\zeta).
$$
$\gamma_\zeta(Q)$ 是用 $\gamma_\zeta(R)$ 正则化 $P_\zeta(X)$ 的有界算子：
$$
\gamma_\zeta(Q)
=P_\zeta(X)\,\gamma_\zeta(R)^p.
$$
而
$$
Q_{\zeta,R}=P_\zeta(X)R^p
$$
也有界。全部域与二项式界由 $D_\zeta$ 有界且完整交换得到。

在实际共同域上先计算，再延拓为有界恒等式：
$$
\boxed{
Q_{\zeta,R}\gamma_\zeta(R)^p
=\gamma_\zeta(Q)R^p.
}
\tag{3.1}
$$
这些因子均为有界交换子，因此彼此交换。
两个正则器 $R^p,\gamma_\zeta(R)^p$ 都单射。
若一边的多项式因子杀掉 $x$，(3.1) 消去另一个单射正则器即可。
所以
$$
\boxed{
\ker Q_{\zeta,R}
=\ker\gamma_\zeta(Q)
=U_\zeta\ker Q.
}
\tag{3.2}
$$
没有把一个非闭自然核直接识别成 gauge 闭核。

## 4. 快分式分支

若 $X=T_{a/e}$、$a,e\in\mathcal G$、$e\ne0$，
在自然域上
$$
e^pP_{\rm nat}(X)=F,\qquad
F=\sum_{k=0}^pE_k a^k e^{p-k}\in\mathcal G.
$$
因此在全 $H$ 上
$$
\boxed{e^pQ=FR^p.}
\tag{4.1}
$$
若 $F=0$，由 $e^p$ 单射有 $Q=0$，与前提矛盾。
故 $F\ne0$。
$F$ 与 $R$ 都单射，(4.1) 使 $Q$ 单射。
$Q\in\{A\}'$ 的 $C_0$ 对称性给它值域稠密。

本分支没有将 $e^{-1}$ 当有界算子，也没有要求 $E_p$ 可逆。

## 5. 非快分式分支：有限代数证书

若实际 $X$ 不是 $\mathbb K=\operatorname{Frac}\mathcal G$ 的闭实现，
R270 的闭图稳定因子引理说明：
对
$$
\mathcal T_\zeta f(t)=(\alpha_\zeta f)(t+D_\zeta)
$$
的作用，每个首一正次数多项式的全 $\Gamma$ 稳定子都不可能为 $\Gamma$。
Prüfer 群的真子群有限。

对本稿的任意非零 $P\in\mathcal G[t]$，
先只在抽象域 $\mathbb K$ 内除以最高系数并作有限不可约分解。
这一步不作实际算子除法。
同一个有限因子陪集论证给某个有限 dyadic 群 $\mu_H$，
使
$$
\gcd_{\mathbb K[t]}(P,\mathcal T_\zeta P)=1
\quad(\zeta\notin\mu_H).
$$
有限 Euclidean 算法再清全部有限个快分母，得到
$$
\boxed{
D=U P+V\mathcal T_\zeta P,\quad
0\ne D\in\mathcal G,\quad U,V\in\mathcal G[t].
}
\tag{5.1}
$$
所有需要实际求值的系数现已是有界 $\mathcal G$ 元素。

## 6. 在有限深图核心上配对

令
$$
M=\ker Q,\qquad M_\zeta=U_\zeta M=\ker Q_{\zeta,R}.
$$
它们都是闭 $A$ 不变空间。
本稿不声称 $M$ 全包含于 $\operatorname{Dom}X^p$，
也不声称 $X_M$ 有界。

对当前固定 $\zeta$ 的有限证书 (5.1)，
选整数
$$
L\ge p+\max(\deg U,\deg V).
$$
可进一步增大 $L$，但不需它随其他参数一致。
则
$$
R^LM\subset\operatorname{Dom}X^L,\qquad
R^LM_\zeta\subset\operatorname{Dom}X^L,
$$
$$
\boxed{
P_{\rm nat}(X)R^LM=0,\qquad
P_{\zeta,\rm nat}(X)R^LM_\zeta=0.
}
\tag{6.1}
$$
例如第一式由
$P(X)R^L=QR^{L-p}$ 及交换性得到。
两类正则化向量分别在 $M,M_\zeta$ 中稠密，
因为 $R$ 在全部闭不变限制上的像稠密。

(5.1) 在 $\operatorname{Dom}X^L$ 上的全部词都有实际定义。
对
$$
f\in R^LM,\qquad g\in R^LM_\zeta
$$
和原双线性配对 $\mathcal B$，
第一项 $UP$ 因 $Pf=0$ 消失；
第二项的有限 $X$ 字母及有界交换系数可逐个移至右端。
所有中间词总阶不超过 $L$，所以没有域缺口：
$$
\mathcal B(V(X)P_\zeta(X)f,g)
=\mathcal B(f,P_\zeta(X)V(X)g)=0.
$$
故
$$
\mathcal B(DR^LM,R^LM_\zeta)=0.
$$
先用两个核心在各自闭核中的稠密性，再用 $D$ 有界，
得到 $\mathcal B(DM,M_\zeta)=0$。
R151 的 $\overline{DM}=M$ 于是给
$$
\boxed{\mathcal B(M,U_\zeta M)=0\quad(\zeta\notin\mu_H).}
\tag{6.2}
$$

R152/R270 的原 Haar Fourier 与全本质支撑论证现在完全适用：
每个乘积 $f(y)g(-1-y)$ 仅有有限群 Fourier 支撑，
逐柱限制秩至多一，故 $M$ 有限维；
原 $A$ 单射拟幂零不允许非零有限维不变空间。
因此 $M=0$，即 $Q$ 单射。
有界 $C_0$ 对称性再给 $Q$ 稠密值域。

这个证明用的是有限词所需的有限深正则化；
没有给未知核补一个未经证明的全自然幂域。

## 7. 闭包、自然像与循环性

两分支已经证明实际非零 $Q$ 单射稠密。
由 (2.5)，
$$
\ker\widetilde P=\ker Q=0.
$$
且
$$
\widetilde P(Zh)=Qh,
$$
故闭包的像包含稠密的 $QH$。
自然多项式也在 $ZH$ 上给同样的像，所以其自然像本身稠密，
自然核也为零。

取 $x\in\operatorname{Dom}\widetilde P$，令 $y=\widetilde P x$。
准确图方程为
$$
Zy=Qx.
\tag{7.1}
$$
有界交换子 $Z,Q$ 都单射稠密，
所以它们都把全空间循环向量送成循环向量。

若 $x$ 循环，则 $Qx$ 循环。
$Z$ 属于完整交换子，R88 说明它保持 $y$ 的闭循环空间；
因此 $Qx=Zy$ 属于 $[y]_A$，迫 $y$ 循环。
反之若 $y$ 循环，则 $Zy$ 循环，
而 $Qx\in[x]_A$，迫 $x$ 循环。
这证明 (1.2)。

这里仅断言全空间循环性等价；
没有声称一般 $Q$ 在每个未知不变限制上稠密，
也没有据 (7.1) 推出所有向量的两个闭循环空间相等。

## 8. 既有范围与未闭接口

按上述 R152/R183 既有范围，本稿重证例如
$$
E_pX^p+E_{p-1}X^{p-1}+\cdots+E_0
$$
中的非零最高系数 $E_p\in\mathcal G$ 有任意正形式阶，
不要求有界可逆，也不作有界除法。
实际求值非零时，其准确最大闭包和所有循环域向量的结论均成立。

对于自然域是否已经等于最大域，
R176 的可逆最高系数定理仍是相应充分条件；
本稿没有取消这个域等式所需的假设。

对 $X=X_b$ 无界的情形，[R171](R171-uhf-leading-polynomials-of-unbounded-first-multipliers.md) 还说明：
只要最高系数是非零 UHF 元素而其余系数有界，
自然多项式在有限柱上已经无界；
这里对倾斜 $X_b=X_0+B_b$ 先作有限二项式展开；$B_b$ 为有界交换子并保持全部自然幂域，最高系数不变、其余系数仍有界，所以 R171 的原无倾斜结论确实适用。因此这里最高系数非零的 $\mathcal G$ 多项式不会实际求值为零。
有界 $X$ 则仍需保留实际非零条件。

本稿不处理多个独立慢方向的一般单个多项式核，
也不把所有有界交换系数都称作 $\mathcal G$。
