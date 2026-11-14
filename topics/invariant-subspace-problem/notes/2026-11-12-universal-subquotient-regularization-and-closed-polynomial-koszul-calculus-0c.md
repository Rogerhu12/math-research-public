# R184：所有有限放大不变子商上的共同正则器、闭多项式演算与规范化 Koszul 证书

日期：2026-11-12（UTC）。作者：root。

状态：完整证明。共同正则器在每个不变子商上仍单射、稠密，因而给出无需原空间共轭的最大闭多项式演算。一般子商上的自然幂未被断言本来闭；结论准确为自然多项式的闭包。有限无界多项式恒等式经同一正则器变成真正有界的 Koszul 证书。

## 1. 输入与陈述范围

设实际算子 $A$ 作用于 $H=L^2(\mathbb Z_2)$，并记
$$
\mathfrak C=\{A\}',\qquad
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}.
$$
R88 已证明 $\mathfrak C$ 交换且等于 $\mathbb C[A]$ 的强算子闭包。

取任意实际第一阶闭乘子 $X=X_u$，系数属于复杂 $\ell^2$。
也允许
$$
Y=X+H_0,\qquad H_0\in\mathfrak C
$$
为有界交换扰动。此处不要求 $H_0$ 的 gauge 增量快；有关代数证书另列为假设。

R128/R140 给一族有界正则器
$$
R(t)\in\mathfrak C,\qquad \|R(t)\|\le1,\qquad
R(t)\longrightarrow I\quad\text{强},
\tag{1.1}
$$
每个 $R(t)$ 单射且像稠密，
$$
R(t)H\subseteq\operatorname{Dom}Y,\qquad
S(t):=YR(t)\in\mathfrak C,
\tag{1.2}
$$
并且对 $s,t>0$ 有
$$
R(s)=R(t)U(s,t),\qquad
S(s)=S(t)U(s,t),
\tag{1.3}
$$
其中 $U(s,t)$ 及其逆均在 $\mathfrak C$。
所有有界因子彼此交换。第二个等式由第一个等式和 $Y$ 的域交换得到。

本稿研究任意有限放大 $A^{(d)}$ 的闭不变子商
$$
\mathscr Q=\mathcal M/\mathcal N,\qquad
\mathcal N\subseteq\mathcal M\subseteq H^{\oplus d}.
\tag{1.4}
$$
所有原有界交换子的对角放大都保持 $\mathcal M,\mathcal N$，因而可诱导到 $\mathscr Q$。
用下标 $\mathscr Q$ 表示诱导算子。

以下证明：

1. $R(t)_{\mathscr Q}^n$ 对每个 $n$ 都单射、像稠密，并具有强主理想单位；
2. $Y_{\mathscr Q}=R(t)_{\mathscr Q}^{-1}S(t)_{\mathscr Q}$ 的最大图闭、稠密定义，参数无关，并与限制、再次商掉不变空间相容；
3. 任意有界交换系数多项式 $P$ 的最大实现等于自然 $P(Y_{\mathscr Q})$ 的闭包，有固定原分母图核心，闭包加乘与多项式加乘相容；
4. 若有限多项式族具有非零快 Bézout 证书，则其有界正则化的 Koszul 复形在每个这样的子商上约化正合。

不把这些结论改写成所有非零 $P(Y_{\mathscr Q})$ 的单射或稠密值域，也不在一般子商上声称 $C$ 自伴。

## 2. 有界交换子下降及强主理想单位

### 2.1 对所有有限放大不变空间的保持

固定 $B\in\mathfrak C$。在有限多个坐标上同时用同一个多项式逼近 $B$，说明 $B^{(d)}$ 保持每个闭 $A^{(d)}$ 不变空间。
因此 $B_{\mathscr Q}$ 有定义，且
$$
\|B_{\mathscr Q}\|\le\|B\|.
$$

同一有限向量逼近还说明
$$
B_{\mathscr Q}\in\overline{\mathbb C[A_{\mathscr Q}]}^{\rm SOT}.
\tag{2.1}
$$
这里在 $\mathcal M$ 中为每个有限组商向量选取代表即可；
商范数不会放大逼近误差。
所以 $B_{\mathscr Q}$ 不仅与其他下降算子交换，还与 $\{A_{\mathscr Q}\}'$ 中每个有界算子交换。

### 2.2 固定正则器的强主理想

固定 $t>0$ 与整数 $n\ge0$。由 (1.3)，
$$
R(s)^n=R(t)^nU(s,t)^n.
$$
先以多项式强逼近固定的 $U(s,t)^n$，再令 $s\downarrow0$，得到
$$
\boxed{I\in\overline{R(t)^n\mathbb C[A]}^{\rm SOT}.}
\tag{2.2}
$$
这是有限向量、任意误差的两层逼近；没有要求一个未经证明的一致算子范数上界。

同一多项式在有限坐标和选定商代表上作用，给
$$
\boxed{I_{\mathscr Q}\in
\overline{R(t)_{\mathscr Q}^n\mathbb C[A_{\mathscr Q}]}^{\rm SOT}.}
\tag{2.3}
$$

因此每个固定 $R(t)_{\mathscr Q}^n$ 单射、像稠密。
例如若 $R(t)_{\mathscr Q}^nx=0$，所有近似单位都杀掉 $x$，极限给 $x=0$；
而每个近似单位的像包含于 $\operatorname{Ran}R(t)_{\mathscr Q}^n$，给稠密性。

也可直接用单位比率核对：$R(t)_{\mathscr Q}x=0$ 迫使全部 $R(s)_{\mathscr Q}x=0$，再用强极限；
所有 $R(s)_{\mathscr Q}^n$ 的像相同，且趋于恒等。

### 2.3 饱和性及有限放大图中的稠密性

对任意闭 $A_{\mathscr Q}$ 不变空间 $L\subseteq\mathscr Q$，
$$
\overline{R(t)_{\mathscr Q}^nL}=L,
\qquad
R(t)_{\mathscr Q}^ny\in L\Longrightarrow y\in L.
\tag{2.4}
$$
第一式由多项式近似单位保持 $L$；
第二式对 $R(t)_{\mathscr Q}^ny$ 施加同一多项式近似单位即得。

这些结论也适用于 $\mathscr Q$ 的任意有限放大中的闭不变空间。
后面取这样的空间为某个最大闭图。

若 $0\ne D\in\mathcal G$，R151 给
$$
I\in\overline{D\mathbb C[A]}^{\rm SOT}.
$$
与 (2.2) 两次使用强闭包得到
$$
\boxed{
I\in\overline{D R(t)^n\mathbb C[A]}^{\rm SOT},
\qquad
I_{\mathscr Q}\in
\overline{(D R(t)^n)_{\mathscr Q}\mathbb C[A_{\mathscr Q}]}^{\rm SOT}.
}
\tag{2.5}
$$
具体地，先把每个 $R(t)^np(A)$ 放入 $DR(t)^n\mathbb C[A]$ 的强闭包，再用 (2.2)。
$D R(t)^n$ 一般只属于 $\mathfrak C$，这里不声称它仍属于 $\mathcal G$、$\mathcal A$ 或 UHF。

## 3. 子商上第一阶的规范最大闭图

固定 $t$，简写
$$
R=R(t)_{\mathscr Q},\qquad S=S(t)_{\mathscr Q}.
$$
定义
$$
\boxed{
\operatorname{Graph}Y_{\mathscr Q}
=\{(x,y)\in\mathscr Q^2:Sx=Ry\}.
}
\tag{3.1}
$$
$R$ 单射，所以这是单值闭图。
有界因子交换，故所有 $(Rh,Sh)$ 都属于此图；
定义域包含稠密的 $\operatorname{Ran}R$。

更换 $t$ 后，$R,S$ 同乘一个有界交换单位，故最大图不变。
所有 $L\in\{A_{\mathscr Q}\}'$ 都与 $R,S$ 交换，由最大方程立即得到
$$
L\operatorname{Dom}Y_{\mathscr Q}\subseteq\operatorname{Dom}Y_{\mathscr Q},
\qquad Y_{\mathscr Q}Lx=LY_{\mathscr Q}x.
\tag{3.2}
$$

### 3.1 原参数图是完整核心

若 $Sx=Ry$，则对任意 $s>0$，
$$
R\,S(s)_{\mathscr Q}x
=S\,R(s)_{\mathscr Q}x
=R(s)_{\mathscr Q}Sx
=R\,R(s)_{\mathscr Q}y.
$$
消去 $R$，得
$$
S(s)_{\mathscr Q}x=R(s)_{\mathscr Q}y.
$$
所以
$$
(R(s)_{\mathscr Q}x,S(s)_{\mathscr Q}x)
=(R(s)_{\mathscr Q}x,R(s)_{\mathscr Q}y)
\longrightarrow(x,y).
$$
而由单位比率，该对属于固定参数图 $\{(Rh,Sh)\}$。
故
$$
\boxed{\operatorname{Graph}Y_{\mathscr Q}
=\overline{\{(Rh,Sh):h\in\mathscr Q\}}.}
\tag{3.3}
$$

在原空间上，(3.1) 确实恢复原来的 $Y$：若 $S(t)x=R(t)y$，上述逼近给 $R(s)x\in\operatorname{Dom}Y$ 且 $YR(s)x=R(s)y$；利用原 $Y$ 闭和两坐标极限，得到 $Yx=y$。反向由域交换立即成立。有限放大逐坐标同理。

### 3.2 正则化给真实自然幂域

由 (3.1)，$Y_{\mathscr Q}R=S$。
再用有界 $R,S$ 的域交换归纳，得到
$$
\boxed{
R^n\mathscr Q\subseteq\operatorname{Dom}Y_{\mathscr Q}^n,\qquad
Y_{\mathscr Q}^kR^n=S^kR^{n-k}\quad(0\le k\le n).
}
\tag{3.4}
$$
因此全部自然幂域稠密。
本式不声称这些自然幂本身闭。

## 4. 任意有界交换系数多项式的最大实现

取 $E_0,\ldots,E_p\in\mathfrak C$，允许最高系数不可逆甚至下降后为零。
记
$$
P(y)=\sum_{k=0}^pE_ky^k.
$$
定义有界算子
$$
F_{P,t}^{[p]}
=\sum_{k=0}^p E_k S(t)^kR(t)^{p-k}\in\mathfrak C.
\tag{4.1}
$$
在 $\mathscr Q$ 上令 $F=(F_{P,t}^{[p]})_{\mathscr Q}$，并定义
$$
\boxed{
\operatorname{Graph}\mathsf P_{\mathscr Q}
=\{(x,y):Fx=R^py\}.
}
\tag{4.2}
$$
$R^p$ 单射，给闭单值图；其域包含稠密的 $R^p\mathscr Q$。

更换参数 $t$ 时两边共同乘以有界单位 $U(s,t)_{\mathscr Q}^p$。
把填充次数从 $p$ 增到 $p+n$ 时两边共同乘以单射 $R^n$。
所以 (4.2) 与参数和填充次数无关。
常数或零多项式仍给原有界算子或全域零算子。

### 4.1 固定原分母图核心

最大图是闭 $A_{\mathscr Q}\oplus A_{\mathscr Q}$ 不变空间。
对图向量 $(x,y)$，
$$
(R^px,R^py)=(R^px,Fx)
$$
属于原参数图。
由 (2.4) 的有限放大版本，
$$
\boxed{
\operatorname{Graph}\mathsf P_{\mathscr Q}
=\overline{\{(R^ph,Fh):h\in\mathscr Q\}}.
}
\tag{4.3}
$$
故
$$
\ker\mathsf P_{\mathscr Q}=\ker F,\qquad
\overline{\operatorname{Ran}\mathsf P_{\mathscr Q}}
=\overline{F\mathscr Q}.
\tag{4.4}
$$
第一式直接来自最大方程；第二式由两坐标图逼近，不能再把右边未经证明替换为 $\mathscr Q$。

### 4.2 最大图恰为自然多项式闭包

将自然多项式定义在共同最高幂域：
$$
P_{\rm nat}(Y_{\mathscr Q})
=\sum_{k=0}^p(E_k)_{\mathscr Q}Y_{\mathscr Q}^k,
\qquad
\operatorname{Dom}P_{\rm nat}=\operatorname{Dom}Y_{\mathscr Q}^p.
$$
对该域中的 $x$，域交换及 (3.4) 给
$$
Fx=R^pP_{\rm nat}(Y_{\mathscr Q})x.
\tag{4.5}
$$
所以自然图包含于闭图 (4.2)，自然实现可闭。
另一方面，(3.4) 说明 (4.3) 的每个参数图向量都属于自然图。
于是
$$
\boxed{\mathsf P_{\mathscr Q}
=\overline{P_{\rm nat}(Y_{\mathscr Q})}.}
\tag{4.6}
$$

自然域若大于某个多项式实际所需的次数，也不改变这个闭包；
额外的 $R$ 幂参数图仍为核心。

这给包括 $\overline{Y_{\mathscr Q}^p}$ 在内的规范闭实现，
但没有把 R172 在原空间利用通常伴随及自交换形式得到的自然幂闭性搬到未知子商。

## 5. 闭包加乘与多项式一致

设 $P,Q$ 分别使用填充次数 $p,q$，有界分子记为 $F_P,F_Q$。

自然和的交域包含 $R^{p+q}\mathscr Q$。
如果 $\mathsf P x=y,\mathsf Q x=z$，则
$$
R^{p+q}(y+z)=(R^qF_P+R^pF_Q)x.
$$
右边是 $P+Q$ 填充至 $p+q$ 的有界分子。
故自然和包含于 $\mathsf{P+Q}$ 的最大图。
在 $R^{p+q}h$ 上自然和值就是
$$
(R^qF_P+R^pF_Q)h.
$$
这构成该最大图的原参数核心，所以
$$
\boxed{\overline{\mathsf P_{\mathscr Q}+\mathsf Q_{\mathscr Q}}
=\mathsf{P+Q}_{\mathscr Q}.}
\tag{5.1}
$$

自然乘积的域也包含 $R^{p+q}\mathscr Q$，因为
$$
\mathsf Q R^{p+q}h=F_QR^ph\in\operatorname{Ran}R^p.
$$
其值为 $F_PF_Qh$。
若一般地 $y=\mathsf Qx,z=\mathsf Py$，则
$$
F_PF_Qx=F_PR^qy=R^qF_Py=R^{p+q}z.
$$
这正是 $PQ$ 的最大方程。
原参数核心再次给
$$
\boxed{
\overline{\mathsf P_{\mathscr Q}\mathsf Q_{\mathscr Q}}
=\mathsf{PQ}_{\mathscr Q}
=\overline{\mathsf Q_{\mathscr Q}\mathsf P_{\mathscr Q}}.
}
\tag{5.2}
$$
不同原始乘积的域未被声称相等；这里是闭包相等。
系数有实际关系时演算也可能有核，不预设在任意 $\mathscr Q$ 上忠实。

## 6. 限制及再次取商的准确相容性

令 $L\subseteq\mathscr Q$ 闭且 $A_{\mathscr Q}$ 不变。

若 $(x,y)\in\operatorname{Graph}\mathsf P_{\mathscr Q}$ 且 $x\in L$，
则 $Fx\in L$，从而 $R^py\in L$。
(2.4) 的饱和性给 $y\in L$。
因此
$$
\mathsf P_{\mathscr Q}
(\operatorname{Dom}\mathsf P_{\mathscr Q}\cap L)\subseteq L.
$$
最大方程的限制与直接在 $L$ 上构造的方程完全相同，所以
$$
\boxed{
\mathsf P_L
=\mathsf P_{\mathscr Q}|_{\operatorname{Dom}\mathsf P_{\mathscr Q}\cap L}.
}
\tag{6.1}
$$
它闭、稠密定义，并由 (4.3) 得固定 $R^pL$ 图核心。

设 $\rho:\mathscr Q\to\mathscr Q/L$ 为商映射。
原图的每个投影对满足商上的最大方程。
原图中的参数对
$$
(R^ph,F_Ph)
$$
投影成商上的全部原参数对，因为 $\rho$ 满射。
所以
$$
\boxed{
\operatorname{Graph}\mathsf P_{\mathscr Q/L}
=\overline{(\rho\oplus\rho)\operatorname{Graph}\mathsf P_{\mathscr Q}}.
}
\tag{6.2}
$$
这是图的闭包相容性；图的投影本身未必闭。

从原有限放大空间先限制到 $\mathcal M$，再商掉 $\mathcal N$，
与直接在 $\mathcal M/\mathcal N$ 使用 (4.2) 完全一致。
一般商上没有自然的同一个 $C$，因而本稿不附加 $C$ 自伴断言。

## 7. 将有限无界恒等式变为有界证书

设 $P_1(y),\ldots,P_m(y)$ 的系数在 $\mathfrak C$，
次数不超过 $p$；设 $U_1(y),\ldots,U_m(y)$ 次数不超过 $k$。
假定已经证明有限实际多项式恒等式
$$
\boxed{\sum_{i=1}^m U_i(Y)P_i(Y)=D,\qquad
0\ne D\in\mathcal G}
\tag{7.1}
$$
在 $\operatorname{Dom}Y^{p+k}$ 上成立。
例如 R166/R173 的有限清分母 gauge Bézout 恒等式在完成实际域说明后符合这个假设。

固定原空间正则器 $R(t)$，定义
$$
T_i=P_i(Y)R(t)^p,\qquad
B_i=U_i(Y)R(t)^k.
\tag{7.2}
$$
它们按 (4.1) 都是真正有界交换子。
正则器已提供足够幂域，有限乘法合法，所以
$$
\boxed{\sum_iB_iT_i=DR(t)^{p+k}=:E.}
\tag{7.3}
$$
没有直接让可能无界的 $U_i(Y)$ 作用于任意未知核或最大图向量。

由 (2.5)，
$$
I\in\overline{E\mathbb C[A]}^{\rm SOT}.
\tag{7.4}
$$
全部有界恒等式下降到每个 $\mathscr Q$，并保留同一强主理想性质。

对原空间上已证明自然闭的 monic $P_i$，有
$$
\ker T_i=\ker P_i(Y).
$$
对一般多项式和一般子商，准确结论始终为
$$
\ker(T_i)_{\mathscr Q}=\ker\mathsf P_{i,\mathscr Q},
\tag{7.5}
$$
其中右边使用最大闭包实现。

## 8. 所有子商上的约化 Koszul 正合

在 $\mathscr Q\otimes\Lambda^\bullet\mathbb C^m$ 上，
令 $\varepsilon_i$ 为外乘第 $i$ 个标准基，$\iota_i$ 为相应缩并。
定义有界微分与同伦
$$
d=\sum_i(T_i)_{\mathscr Q}\varepsilon_i,\qquad
h=\sum_i(B_i)_{\mathscr Q}\iota_i.
$$
有界系数交换，外代数恒等式给
$$
d^2=0,\qquad dh+hd=E_{\mathscr Q}I.
\tag{8.1}
$$

若 $v\in\ker d$，则
$$
E_{\mathscr Q}v=dhv.
$$
取 (7.4) 下降后的多项式近似单位，
同一多项式与全部微分系数交换，所以
$$
p_\alpha(A_{\mathscr Q})E_{\mathscr Q}v
=d\,p_\alpha(A_{\mathscr Q})hv
\longrightarrow v.
$$
由此在每个次数得到
$$
\boxed{\ker d_j=\overline{\operatorname{Ran}d_{j-1}}.}
\tag{8.2}
$$
在最低次数，$d_{-1}=0$，所以共同核为零；
在最高次数，上一微分像稠密。
中间的像只取闭包，不声称它们本来闭。

特别，
$$
\bigcap_i\ker\mathsf P_{i,\mathscr Q}=0.
\tag{8.3}
$$
同时有共同参数图核心：
$$
\boxed{
\{(x_1,\ldots,x_m):
(T_i)_{\mathscr Q}x_j=(T_j)_{\mathscr Q}x_i\ \forall i,j\}
=
\overline{\{((T_1)_{\mathscr Q}z,\ldots,(T_m)_{\mathscr Q}z):z\in\mathscr Q\}}.
}
\tag{8.4}
$$
当 $m=1$，左边是全部 $\mathscr Q$，右边稠密正是最高次数结论。

(8.4) 对两算子给闭关系的原参数核心；
如果某个指定分母另外已知单射，则它是单值闭图。
这里不预设各单个 $T_i$ 在未知限制上像稠密，
也不把有界 Koszul 正合未经定义域说明改写成原无界算子的自然 Koszul 复形。

## 9. 此结果关闭和保留的接口

已经关闭的是共同正则器在子商上可能失去单射性或参数核心的疑问；
所有有限放大子商都具有同一规范闭多项式演算。
有限无界轨道恒等式也能有界化为真实强主理想证书，而不混用不同 gauge 核作为同一个配对目标。

保留的问题包括：

- 一般 $X_{u,M}$ 或一般非零多项式在未知不变 $M$ 上是否值域稠密；
- 单个 Bell 或多个慢方向多项式的核是否为零；
- 子商上的自然高幂是否无需闭包就闭；
- 原 $H$ 的普通不变格及完整 Hilbert 不变子空间问题。

核心区别是：正则分母 $R(t)^n$ 具有普遍强主理想单位，任意正则化分子没有被自动赋予这一性质。

## 10. 依赖

- [R88：交换子及强多项式闭包](../results.md)：仅调用已证有界交换子保持和有限同时强逼近。
- [R128：第一阶不变限制与正分量正则化](../results/R128-first-chaos-invariant-parts-and-resolvent-regularization.md)。
- [R140：固定正则参数单位比率及不变子商](../results/R140-invariant-subquotient-type-and-fixed-first-regularization.md)。
- [R151：快系数的普遍强主理想单位](../results/R151-quartic-analytic-approximation-gauge-stability.md)。
- [R169：有限快证书的有界 Koszul 机制](../results/R169-finite-gauge-koszul-cores-and-two-slow-mode-separation.md)。
- [R176：原空间自然多项式的完整闭图](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md)。

本稿已直接给出所需子商、图核心、自然闭包、加乘相容性和 Koszul 证明，不以这些引用代替新增论证。
