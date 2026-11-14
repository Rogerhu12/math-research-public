# R186：多一阶的共同混合域、最大多项式闭图与有限模式联合循环

日期：2026-11-12（UTC）。作者：critical_kernel。根代理预留 R186。

状态：完整证明。本稿建立有限多个真实闭第一阶乘子的共同混合域与最大多项式实现，并据此完成任意有限模式点态多项式乘平方可和指数权的有限 gauge 联合循环。自然混合多项式的原定义域不被默认视为闭域；一般单个多模式多项式的核仍未排除。

## 1. 设置、结论及准确输入

记
$$
\mathfrak C=\{A\}',\qquad
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},\qquad
B(f,g)=\langle f,Cg\rangle,
\quad
(Cf)(y)=\overline{f(-1-y)}.
$$
R88 给：$\mathfrak C$ 交换，每个成员均为有界 $C$ 对称算子，且
$\mathfrak C=\overline{\mathbb C[A]}^{\rm SOT}$。
特别，它的所有成员保持每个闭 $A$ 不变空间；同一个多项式网还证明其对角放大保持每个有限放大的闭不变空间。

取有限个第一阶符号
$$
u_i=a_{i,*}+\sum_{j\ge0}a_{ij}\chi_j,\qquad
a_i=(a_{ij})_j\in\ell^2,\qquad 1\le i\le d,
\tag{1.1}
$$
令 $X_i=X_{u_i}$ 为 R125 的真实闭实现。
也允许先加任意有界交换子：
$$
Y_i=X_i+H_i,\qquad H_i\in\mathfrak C,\qquad
\operatorname{Dom}Y_i=\operatorname{Dom}X_i.
\tag{1.2}
$$
每个 $Y_i$ 是闭、稠密定义、$C$ 自伴的算子；全部 $\mathfrak C$ 保持其域并与其域交换。
有界扰动的伴随公式及 $H_i^*=CH_iC$ 证明这里的完整 $C$ 自伴，不只是核心上的对称性。

R125/R128 还给每个一阶乘子的正分量正则器。
R145 的多模式幂域结论给 $1$ 属于全部有限混合词的域；§10 将用共同整函数再独立证明这一点，并同时处理任意平方可和指数权。

本稿的域结论允许全部 $H_i\in\mathfrak C$、全部有界交换多项式系数。
只有 §8 以后的有限轨道结论才另外要求
$$
H_i\in\mathcal A,\qquad
\gamma_\zeta H_i-H_i\in\mathcal G
\quad(\zeta\in\Gamma=\mu_{2^\infty}),
\tag{1.3}
$$
并使用 R151 的快速解析逼近代数 $\mathcal G$ 和
$$
K=\operatorname{Frac}\iota(\mathcal G)\subset\mathbb C((z)).
$$

主要结论如下：

1. 存在一个共同的 $R(t)\in\mathfrak C$，对全部有限混合词提供真实有界正则化。
2. 对任意 $P\in\mathfrak C[t_1,\ldots,t_d]$，自然混合实现可闭；其闭包由一个规范最大闭图给出，并且是 $C$ 自伴的。
3. 原正则分母参数图、有限柱及任意循环域向量的多项式轨道，都是准确的图核心。
4. 对任意有限族这样的多项式核，每个固定阶数都存在核内稠密的共同高阶测试空间；不要求整个核先属于自然混合域。
5. 对满足 (1.3) 的有限模式及快系数多项式，非零实际实现有有限 gauge 族共同核为零。若独立形式增量类的总秩为 $n>0$，至多 $n$ 个 gauge 足够；秩零时单个算子已单射。
6. 因而任意非零
$$
F(u_1,\ldots,u_d)e^w,\qquad
w=b_*+\sum_jb_j\chi_j,\quad b\in\ell^2,
$$
其中 $F$ 是有限多项式，都有有限个 gauge 像联合循环。这里不声称该向量本身已循环。

## 2. 一个同时适用于全部模式的正则器

将全部行 $a_i$ 的实部、虚部分别拆成正负部。
得到有限个非负平方可和行及其实际闭第一阶乘子 $T_\nu$。
零行可删去。
R128 给
$$
R_\nu(t)=(I+tT_\nu)^{-1}\in\mathfrak C,\qquad
\|R_\nu(t)\|\le1,\qquad R_\nu(t)\to I\ {\rm SOT}.
$$
每个 $R_\nu(t)$ 单射、稠密像。
定义
$$
R(t)=\prod_\nu R_\nu(t).
\tag{2.1}
$$
因子有限且交换，故 $R(t)$ 是单射、稠密像的收缩，且强趋于 $I$。

正分量的域等式
$$
T_\nu R_\nu(t)=t^{-1}(I-R_\nu(t))
$$
及 R128 的一阶域识别给
$$
R(t)H\subseteq\bigcap_{i=1}^d\operatorname{Dom}Y_i,\qquad
S_i(t):=Y_iR(t)\in\mathfrak C.
\tag{2.2}
$$
常数 $a_{i,*}$ 和有界 $H_i$ 只贡献有界项。
在 $\operatorname{Dom}Y_i$ 上还有
$$
R(t)Y_i x=S_i(t)x.
\tag{2.3}
$$

### 2.1 参数比率是实际有界单位

对 $s,t>0$，
$$
R_\nu(s)=R_\nu(t)U_\nu(s,t),
\qquad
U_\nu(s,t)=\frac ts I+\left(1-\frac ts\right)R_\nu(s).
\tag{2.4}
$$
其实际有界逆为
$$
U_\nu(s,t)^{-1}
=\frac st I+\left(1-\frac st\right)R_\nu(t).
$$
这些等式来自预解恒等式，未使用无界算子的形式约分。
有限相乘给
$$
R(s)=R(t)U(s,t),\qquad
U(s,t),U(s,t)^{-1}\in\mathfrak C.
\tag{2.5}
$$
并且
$$
S_i(s)=S_i(t)U(s,t).
\tag{2.6}
$$

### 2.2 固定幂在实际闭不变图上稠密

设 $\mathcal L\subset H^{\oplus m}$ 是闭 $A^{(m)}$ 不变空间。
$U(s,t)^{(m)}$ 及其逆都保持 $\mathcal L$。
故对每个固定整数 $N\ge0$，
$$
(R(s)^N)^{(m)}\mathcal L=(R(t)^N)^{(m)}\mathcal L.
$$
由 $R(s)^N\to I$ 强，
$$
\boxed{\overline{(R(t)^N)^{(m)}\mathcal L}=\mathcal L.}
\tag{2.7}
$$
这包括未知核、闭图及其有限交。

也可以把它写成固定正则器的强主理想单位：
$$
\boxed{I\in\overline{R(t)^N\mathbb C[A]}^{\rm SOT}.}
\tag{2.8}
$$
确实，对固定 $s$，用 R88 把 $U(s,t)^N$ 强逼近为多项式，再令 $s\downarrow0$。
这里使用的是网与有限组向量的强逼近，不需要统一有界的多项式逼近序列。

## 3. 共同混合词域及其完备图范数

对一个有序词 $I=(i_1,\ldots,i_k)$，记
$$
Y_I=Y_{i_1}\cdots Y_{i_k}
$$
为逐次作用的自然复合，最右端先作用。
空词为 $I$。
定义
$$
\mathcal D_p
=\bigcap_{0\le |I|\le p}\operatorname{Dom}Y_I.
\tag{3.1}
$$
交中保留全部词序，因而没有预先假设两个无界算子强交换。
给它范数
$$
\|x\|_{(p)}^2=\sum_{|I|\le p}\|Y_Ix\|^2.
\tag{3.2}
$$

### 3.1 共同图完备

若 $x_n$ 在 (3.2) 下 Cauchy，各 $Y_Ix_n$ 都有极限。
先由各 $Y_i$ 的闭性识别长度一的极限。
随后逐词长度归纳：若右侧子词的极限已识别，应用左端 $Y_i$ 的闭性，即识别更长词的极限。
因此
$$
(\mathcal D_p,\|\cdot\|_{(p)})\text{ 完备}.
\tag{3.3}
$$
这只证明同时记录所有低阶词的共同图闭；不声称某一个混合词的自然复合本身闭。

每个 $B\in\mathfrak C$ 保持 $\mathcal D_p$，且
$$
Y_I Bx=B Y_Ix
\quad(x\in\mathcal D_p,\ |I|\le p).
\tag{3.4}
$$
这是第一阶域交换的有限归纳。

### 3.2 真正的混合词正则化

固定 $t$，简记 $R=R(t)$、$S_i=S_i(t)$。
对 $N\ge k$，(2.2)—(2.3) 的逐次应用给
$$
\boxed{
R^NH\subseteq\mathcal D_N,\qquad
Y_{i_1}\cdots Y_{i_k}R^N
=S_{i_1}\cdots S_{i_k}R^{N-k}.
}
\tag{3.5}
$$
归纳时右侧除已作用的 $S_i$ 外仍有足够的 $R$ 因子，下一步输入因此属于所需第一阶域。
全部 $S_i$ 是有界交换子，所以右侧与词序无关。

对 $x\in\mathcal D_k$，也有
$$
R^kY_Ix=\prod_{\ell=1}^kS_{i_\ell}\,x.
\tag{3.6}
$$
若两个词有同样的指标重数，右侧相同；消去单射 $R^k$ 后，它们在 $\mathcal D_k$ 上的值相同。
因此在这个已明确的共同域上，可用多重指标 $Y^\alpha$ 记相应值。

### 3.3 固定共同图核心

若 $x\in\mathcal D_p$，则
$$
Y_I R(s)^px=R(s)^pY_Ix\longrightarrow Y_Ix
\quad(|I|\le p).
$$
另一方面，(2.5) 给
$$
R(s)^pH=R(t)^pH.
$$
所以
$$
\boxed{R(t)^pH\text{ 是 }\mathcal D_p\text{ 的共同图核心}.}
\tag{3.7}
$$
这里“共同图核心”指 (3.2) 的范数，而非只指 $H$ 中稠密。
特别 $\mathcal D_p$ 稠密。

有界交换扰动 $Y_i\mapsto Y_i+D_i$ 不改变 $\mathcal D_p$：
有限词的逐次展开证明一个包含，再写 $Y_i=(Y_i+D_i)-D_i$ 证明反向包含。
这也说明 (1.2) 的共同域与原来 $X_i$ 的共同域相同。

## 4. 任意有界交换系数多项式的规范最大图

取
$$
P(t_1,\ldots,t_d)
=\sum_{|\alpha|\le p}E_\alpha t^\alpha,
\qquad E_\alpha\in\mathfrak C.
\tag{4.1}
$$
自然实现定义于整个 $\mathcal D_p$：
$$
P_{\rm nat}(Y)x=\sum_{|\alpha|\le p}E_\alpha Y^\alpha x.
\tag{4.2}
$$
不要求某个最高系数为单位，也不假设这个自然域已经给出闭算子。

定义有界正则化
$$
F_P^{[p]}(t)
=\sum_{|\alpha|\le p}
E_\alpha S(t)^\alpha R(t)^{p-|\alpha|}
\in\mathfrak C.
\tag{4.3}
$$
固定一个 $t>0$，简记 $F_P=F_P^{[p]}(t)$。
定义
$$
\boxed{
\operatorname{Graph}\mathsf P
=\{(x,y)\in H\oplus H:F_Px=R^py\}.
}
\tag{4.4}
$$
因 $R^p$ 单射，这是单值闭图。
又因全部有界因子交换，
$$
(R^ph,F_Ph)\in\operatorname{Graph}\mathsf P
\quad(h\in H),
\tag{4.5}
$$
故定义域稠密。

### 4.1 自然实现的闭包准确等于最大图

(3.6) 给
$$
F_Px=R^pP_{\rm nat}(Y)x
\quad(x\in\mathcal D_p).
\tag{4.6}
$$
自然图包含于最大图，所以可闭。

反向设 $F_Px=R^py$，取
$$
x_s=R(s)^px\in\mathcal D_p.
$$
利用 (4.6) 及有界因子交换，
$$
R^pP_{\rm nat}(Y)x_s
=F_PR(s)^px
=R(s)^pF_Px
=R^pR(s)^py.
$$
消去单射 $R^p$，得到
$$
P_{\rm nat}(Y)x_s=R(s)^py.
$$
两个图坐标随 $s\downarrow0$ 分别趋于 $x,y$。
因此
$$
\boxed{\mathsf P=\overline{P_{\rm nat}(Y)|_{\mathcal D_p}}.}
\tag{4.7}
$$
这一步没有证明、也不需要证明 $P_{\rm nat}(Y)$ 自然域本身闭。

### 4.2 参数、填充次数及正则器的选择

由 (2.5)—(2.6)，改用 $s$ 时，
$$
F_P^{[p]}(s)=F_P^{[p]}(t)U(s,t)^p,\qquad
R(s)^p=R(t)^pU(s,t)^p.
$$
所以 (4.4) 不依赖参数。

对任意填充次数 $N\ge p$，
$$
F_P^{[N]}=R^{N-p}F_P^{[p]}.
\tag{4.8}
$$
增加相同的单射因子不改变最大图。
零多项式得到全域零算子，常数多项式得到原有有界算子。

若采用另一个满足 §§2—3 性质的共同正则器，
(4.7) 仍把图识别为同一个自然实现的闭包，故结果也与这种选择无关。

### 4.3 原参数图是完整图核心

最大图是闭 $A\oplus A$ 不变空间。
对其中的 $(x,y)$，
$$
(R^px,R^py)=(R^px,F_Px)
$$
属于 (4.5)。
由 (2.7)，
$$
\boxed{
\operatorname{Graph}\mathsf P
=\overline{\{(R^ph,F_Ph):h\in H\}}.
}
\tag{4.9}
$$
任意更大固定 $R^NH$，$N\ge p$，也给参数图核心。

### 4.4 最大域的交换性与闭包演算

每个 $B\in\mathfrak C$ 与 (4.4) 两侧的有界算子交换，因此
$$
B\operatorname{Dom}\mathsf P\subseteq\operatorname{Dom}\mathsf P,\qquad
\mathsf P Bx=B\mathsf Px.
\tag{4.10}
$$

若 $P,Q$ 是两个这样的多项式，则
$$
\boxed{
\overline{\mathsf P+\mathsf Q}=\mathsf{P+Q},
\qquad
\overline{\mathsf P\mathsf Q}=\mathsf{PQ}.
}
\tag{4.11}
$$
证明：取共同填充次数，(4.4) 的有界等式先证明自然和、自然复合的图包含于右侧最大图。
另一方面，对足够大固定 $N$，
$R^NH\subset\mathcal D_N$，且自然代数的所有中间词均有定义；
在 $R^NH$ 上实际和、积恰为对应多项式。
这个固定空间是右侧的图核心，所以取闭包得到等号。

(4.11) 是多项式闭包演算，不是分式场断言。
一般多变量多项式可能有未排除的核，不能据此构造其逆。

## 5. 完整 C 自伴、共同核高阶测试及限制边界

### 5.1 整个通常伴随域

在原参数图上定义
$$
T_0(R^ph)=F_Ph.
$$
由 (4.9)，$\overline{T_0}=\mathsf P$。
通常伴随的图条件为
$$
(v,w)\in\operatorname{Graph}T_0^*
\iff F_P^*v=(R^p)^*w.
$$
$F_P,R^p\in\mathfrak C$ 均为 $C$ 对称。
共轭此等式恰得
$$
F_P Cv=R^p Cw.
$$
所以
$$
\boxed{\mathsf P^*=C\mathsf PC.}
\tag{5.1}
$$
这里识别了完整伴随域，而非只在有限柱上验证形式对称。

### 5.2 任意有限共同核的真实高阶稠密空间

由 (4.4)，
$$
\ker\mathsf P=\ker F_P.
\tag{5.2}
$$
令 $M$ 为任意有限个此类核的交。
这是闭 $A$ 不变空间，被全部 $\mathfrak C$ 保持。
对每个固定 $N$，
$$
\boxed{
R(t)^NM\subseteq M\cap\mathcal D_N,\qquad
\overline{R(t)^NM}=M.
}
\tag{5.3}
$$
第一式来自有界核算子与 $R$ 交换，第二式来自 (2.7)。

如果 $x\in M\cap\operatorname{Dom}Y_i$，每个核算子 $F_P$ 与 $Y_i$ 域交换，故
$$
F_PY_ix=Y_iF_Px=0.
$$
因此
$$
Y_i(M\cap\operatorname{Dom}Y_i)\subseteq M.
\tag{5.4}
$$
在 (5.3) 中选择足够大的有限 $N$，即可合法测试任何给定的有限多项式恒等式及全部中间词。

一般没有证明 $M\subseteq\mathcal D_p$，更没有证明 $Y_i|_M$ 有界。
不同 $N$ 的稠密性也没有被偷换成可数交自动稠密。

### 5.3 闭不变限制的准确范围

对任意闭 $A$ 不变 $M$，每个 $Y_i$ 将
$\operatorname{Dom}Y_i\cap M$ 送入 $M$。
确实，
$$
Y_iR(s)x=S_i(s)x\in M,\qquad
Y_iR(s)x=R(s)Y_ix\to Y_ix.
$$
同样，每个 $\mathsf P$ 将 $\operatorname{Dom}\mathsf P\cap M$ 送入 $M$：
用 $\mathsf P R(s)^p=F_P^{[p]}(s)$ 及强极限即可。

所以限制的最大图等于
$$
\{(x,y)\in M\oplus M:F_Px=R^py\}
=\overline{\{(R^ph,F_Ph):h\in M\}}.
\tag{5.5}
$$
它也是自然混合多项式在 $\mathcal D_p\cap M$ 上的闭包。
定义域在 $M$ 中稠密；**值域稠密并未由此得到**。
$C$ 自伴结论只在原 $H$ 上陈述，不假设 $CM=M$。
本稿也不把这些结论自动提升为任意未知子商上的多变量分式场。

## 6. 图循环与有限柱核心

设 $\xi\in\operatorname{Dom}\mathsf P$ 对 $A$ 循环。
对每个 $D\in\mathfrak C$，R88 的强多项式逼近同时作用于 $\xi,\mathsf P\xi$，给
$$
(D\xi,\mathsf P D\xi)
=(D\xi,D\mathsf P\xi)
\in\overline{\{(p(A)\xi,p(A)\mathsf P\xi):p\in\mathbb C[z]\}}.
$$
固定 $R^p$，将这一点用于 $D=R^pp(A)$。
因 $\xi$ 循环，$R^p\mathbb C[A]\xi$ 在原参数图中图稠密。
由 (4.9)，
$$
\boxed{
\mathbb C[A]\xi\text{ 是 }\mathsf P\text{ 的图核心},
\qquad
[\mathsf P\xi]_A=\overline{\operatorname{Ran}\mathsf P}.
}
\tag{6.1}
$$
于是
$$
\mathsf P\xi\text{ 循环}\iff\ker\mathsf P=0.
\tag{6.2}
$$

特别，$1$ 属于全部混合词域，见 R145 或 §10 的 $w=0$ 特例。
把同一论证用于有限个全部词同时组成的图，结合 (3.7)，得到
$$
\mathbb C[A]1\text{ 是 }\mathcal D_p\text{ 的共同图核心}.
\tag{6.3}
$$
R176 已给真实范数密度
$$
\overline{\operatorname{span}\{X_f:f\in\mathcal D_c\}}^{\|\cdot\|}
=\mathcal A,
\qquad X_f1=f.
\tag{6.4}
$$
用 $X_f$ 在范数中逼近固定 $p(A)$，同时作用于有限组向量
$\{Y_I1:|I|\le p\}$，便得到
$$
\boxed{
\mathcal D_c\text{ 是 }\mathcal D_p\text{ 的共同图核心，
也是 }\mathsf P\text{ 的图核心}.
}
\tag{6.5}
$$
所有有限柱均在相应共同域中，因为其真实柱乘子属于 $\mathfrak C$。

因此若 $h=\mathsf P1$，规范初始乘子
$$
\mathcal X_{h,0}f=X_fh,\qquad f\in\mathcal D_c
$$
满足
$$
\boxed{\overline{\mathcal X_{h,0}}=\mathsf P.}
\tag{6.6}
$$
这里识别的是最大闭包，不把 $\mathcal D_p$ 误称为其准确全域。

## 7. gauge 协变来自共同自然域

现在假设各 $H_i$ 满足 (1.3)。
由 R125 的有限低位差与 (1.3)，
$$
U_\zeta Y_iU_\zeta^*=Y_i+D_{\zeta,i},
\qquad D_{\zeta,i}\in\mathcal G,
\tag{7.1}
$$
是同域闭算子等式。

§3 的有界交换扰动结论给
$$
U_\zeta\mathcal D_p=\mathcal D_p.
\tag{7.2}
$$
对具有有界交换系数的 $P$，在 $\mathcal D_p$ 上作有限词展开，再由 (4.7) 取闭包，得到
$$
\boxed{
U_\zeta\mathsf P U_\zeta^*
=\mathsf{\Lambda_\zeta P},\qquad
\Lambda_\zeta P(t)
=(\gamma_\zeta P)(t+D_\zeta).
}
\tag{7.3}
$$
不需要 gauge 后的共同正则器恰好等于原来的 $R(t)$。

因此 $\ker\mathsf{\Lambda_\zeta P}=U_\zeta\ker\mathsf P$。
每个这样的核及其有限交都可使用 (5.3) 的高混合阶稠密测试。

## 8. 有限增量类的归约：先真实有限关系，再形式消元

本节取 $H_i$ 满足 (1.3)，另允许有限个有界加性模式
$$
B_1,\ldots,B_\ell\in\mathcal A,\qquad
\gamma_\zeta B_j-B_j\in\mathcal G.
\tag{8.1}
$$
考虑
$$
P\in\mathcal G[t_1,\ldots,t_d,s_1,\ldots,s_\ell],
$$
在 $t_i=Y_i,\ s_j=B_j$ 处的最大实现。
有界 $B_j$ 可并入系数；§§2—7 全部适用。

### 8.1 先按真正的一阶行取商

在有限维行空间中，选取 $a_1,\ldots,a_s$，使其在
$\ell^2/\ell^1$ 中的类组成全部原行的基。
重新编号后，对于 $i>s$，
$$
a_i-\sum_{\nu=1}^s c_{i\nu}a_\nu\in\ell^1.
$$
于是存在真实有界加性模式 $Z_i\in\mathcal A$，使
$$
Y_i=\sum_{\nu=1}^s c_{i\nu}Y_\nu+Z_i
\quad\text{在共同第一阶域上}.
\tag{8.2}
$$
$Z_i$ 包括常数项、上述 $\ell^1$ 行的真实有界第一阶乘子，以及
$H_i-\sum c_{i\nu}H_\nu$。
在有限柱上 (8.2) 由定义成立；§6 的共同第一阶图核心把它延到整个共同域。
因此有限词的展开也在所有所需共同高阶域上成立。

所有 $Z_i$ 的 gauge 增量属于 $\mathcal G$：
$\ell^1$ 第一阶的增量只改变有限低位，$H_i$ 的增量由假设给出。
从此只保留 $s$ 个独立的无界行模式，并把全部 $Z_i$ 加入有界模式表。

### 8.2 形式原函数的常数要与实际归约一致

对选中的 $Y_\nu$，取形式原函数
$$
\sigma_\nu(z)
=\sum_j a_{\nu j}(v_j(z)-1)+\iota(H_\nu),
\qquad
v_j(z)=\frac{d_j-z^{2^j}}{d_j+z^{2^j}}.
\tag{8.3}
$$
它只记录 gauge 增量，不是对无界 $Y_\nu$ 的形式演算定义。
加任意复常数不改变增量或模 $K$ 的类。

若某个组合行 $a'$ 属于 $\ell^1$，其实际有界第一阶 $X_{a'}$ 满足
$$
\sum_j a'_j(v_j-1)
=\iota(X_{a'})-\chi(X_{a'}),
\tag{8.4}
$$
其中把实际常数项计入 $\chi(X_{a'})$。
所以不得在实际有限关系中漏掉这个常数。

一种不含歧义的选择是：对没有保留的模式，直接按照 (8.2) 定义其原函数
$$
\sigma_i=\sum_\nu c_{i\nu}\sigma_\nu+\iota(Z_i).
$$
它与原来的逐项原函数只相差复常数，并与真实有限关系准确一致。
下文只使用这种已经校正的有限变量归约。

### 8.3 有界依赖用有限 G 分母清除

在剩余有界模式中，选取 $B'_1,\ldots,B'_r$，使
$$
[\iota(B'_1)],\ldots,[\iota(B'_r)]
$$
是它们在 $\mathbb C((z))/K$ 中类空间的一组 $\mathbb C$ 基。

对每个未保留的有界模式 $B$，存在复常数 $c_\nu$ 及
$a,b\in\mathcal G,\ b\ne0$，使
$$
\iota(B)-\sum_\nu c_\nu\iota(B'_\nu)=\frac{\iota(a)}{\iota(b)}.
$$
由于 $\iota$ 在 $\mathcal A$ 上忠实，这给真实有界恒等式
$$
\boxed{b\left(B-\sum_\nu c_\nu B'_\nu\right)=a.}
\tag{8.5}
$$
对有限多项式使用有限次 (8.5)，并乘足够高但有限的分母幂，得到
$$
D\,P(Y,B)=\widetilde P(Y_1,\ldots,Y_s,B'_1,\ldots,B'_r)
\tag{8.6}
$$
在足够高的共同自然域上成立，其中
$$
0\ne D\in\mathcal G,\qquad
\widetilde P\in\mathcal G[t_1,\ldots,t_s,s_1,\ldots,s_r].
$$
没有把 $a/b$ 当成有界系数后直接代入；(8.5)—(8.6) 始终是有限清分母恒等式。

取足够大的共同填充次数 $N$，(8.6) 在 $R^NH$ 上给
$$
D F_P^{[N]}=F_{\widetilde P}^{[N]}.
\tag{8.7}
$$
$D$ 单射，故
$$
\boxed{\ker\mathsf P=\ker\mathsf{\widetilde P}.}
\tag{8.8}
$$
对每个 gauge，共轭 (8.7)，$\gamma_\zeta D$ 仍是非零 $\mathcal G$ 元素并单射，因此
$$
\boxed{
\ker\gamma_\zeta\mathsf P
=\ker\gamma_\zeta\mathsf{\widetilde P}.
}
\tag{8.9}
$$

如果 $\widetilde P$ 是零形式多项式，(8.7) 与单射性迫 $F_P=0$，所以 $\mathsf P$ 是全域零算子。
因此，**实际非零的 $\mathsf P$ 保证归约后的 $\widetilde P\ne0$**。
这没有预先假定多模式多项式求值忠实。

### 8.4 剩余形式类确实独立

设
$$
\sum_{\nu=1}^s c_\nu\sigma_\nu
+\sum_{j=1}^r e_j\iota(B'_j)\in K.
\tag{8.10}
$$
若某个 $c_\nu\ne0$，按 $\ell^2/\ell^1$ 中的选基，
$\sum_\nu c_\nu a_\nu\notin\ell^1$。
R180 的闭差标量化与 UHF 左乘障碍，应用于这个实际第一阶组合和全部剩余有界加性项，排除 (8.10)。

因此全部 $c_\nu=0$。
再用有界模式的选基，得到全部 $e_j=0$。
所以
$$
\boxed{
[\sigma_1],\ldots,[\sigma_s],
[\iota(B'_1)],\ldots,[\iota(B'_r)]
\text{ 在 }\mathbb C((z))/K\text{ 中对 }\mathbb C\text{ 线性无关}.
}
\tag{8.11}
$$

记
$$
n=s+r.
\tag{8.12}
$$
R166 的纯形式引理遂给这 $n$ 个原函数在 $K$ 上代数无关，并给相应半线性平移作用下的
$$
K[z_1,\ldots,z_n]
$$
没有非零真稳定理想。
该引理只使用固定域 $\mathbb C((z))^\Gamma=\mathbb C$、增量属于 $K$ 以及 (8.11)，不要求各原函数来自有界算子。

## 9. 至多 n 个 gauge 的实际共同核分离

先设 $n\ge1$ 且归约后 $\widetilde P\ne0$。
半线性作用为
$$
\Lambda_\zeta Q(z)
=(\alpha_\zeta Q)(z+h_\zeta),
\qquad
h_\zeta=\alpha_\zeta\sigma-\sigma\in K^n.
\tag{9.1}
$$
各坐标的增量都有真实 $\mathcal G$ 实现，(7.3) 正是对应的闭算子协变。

### 9.1 有限坏参数与降维

R173 的有限轨道引理适用于这里的形式原函数，具体理由如下。
固定多项式次数后，所有 $\Lambda_\zeta\widetilde P$ 都在一个有限维 $K$ 系数空间中。
若一个 $K$ 线性子空间不含整个轨道，取一个消去它而不消去某个轨道点的线性泛函。
所得形式 Laurent 级数的每个固定 $z$ 系数都是 $\zeta$ 的有限 Laurent 多项式：
所有系数只有有限负阶，且每个固定阶的卷积是有限和。
其中某个系数不恒零，故只有有限个 $\zeta$ 使其为零。

因此，每个不含全部轨道的真素理想，只含有限个轨道成员。
Γ-单纯性保证任何真素理想都不含整个非零轨道。
从 $\widetilde P$ 本身开始，逐次避开当前有限个最小素分支的有限坏集合，每次严格降低最大分支的超越维数。
至多 $n$ 个轨道成员
$$
\widetilde P_1=\widetilde P,\ \widetilde P_2,\ldots,\widetilde P_m,
\qquad m\le n,
\tag{9.2}
$$
生成的理想 $I$ 已是单位理想，或商代数 $K[z_1,\ldots,z_n]/I$ 是零维的。
第一项可固定为原多项式，后续每步仅需避开有限坏参数。
不声称所有参数元组的坏集合有限。

### 9.2 零维商产生一元消去式

若 $I$ 为单位理想，有限等式
$$
1=\sum_{j=1}^m U_j\widetilde P_j,\qquad U_j\in K[z]
$$
清除全部有限 $\mathcal G$ 分母后，给
$$
0\ne D_0=\sum_j V_j\widetilde P_j,\qquad
D_0\in\mathcal G,\quad V_j\in\mathcal G[z].
\tag{9.3}
$$

若商代数零维且非零，它在 $K$ 上有限维。
这一点不要求 $K$ 代数闭：有限个最小素商都是有限代数扩域；约化商嵌入它们的有限乘积。
Noether 性给幂零根理想的有限过滤，各层是约化商上的有限生成模，故整个商仍有限维。

在这个有限维商上，对任意一个坐标 $z_\nu$ 的乘法矩阵应用 Cayley–Hamilton，得到
$$
0\ne q(z_\nu)\in I,\qquad q\in K[t]\text{ 首一}.
$$
有限清分母给
$$
\boxed{
0\ne Q(z_\nu)=\sum_{j=1}^m V_j\widetilde P_j,
\qquad Q\in\mathcal G[t],\quad V_j\in\mathcal G[z].
}
\tag{9.4}
$$

对应的一元实际算子已知单射：

- 若选的是无界行坐标 $Y_\nu$，R183 对非首一 $\mathcal G[Y_\nu]$ 最大实现证明单射；它允许这里的有界加性扰动 $H_\nu$。
- 若选的是有界坐标 $B'_\nu$，其类非零，R152 对全部非零 $\mathcal G[B'_\nu]$ 多项式证明单射。

所以 (9.4) 的左侧具有真实单射实现。
这是把轨道数从一般单位证书的 $n+1$ 减少到 $n$ 的准确依据；不能仅靠多元“互素”得到单位理想。

### 9.3 在真正高阶核内执行有限恒等式

令
$$
M=\bigcap_{j=1}^m\ker\mathsf{\widetilde P_j}.
$$
取任意 $x\in M$。
选固定有限 $N$，大于 (9.3) 或 (9.4) 中全部多项式乘积所需的混合词长度。
则
$$
f=R(t)^Nx\in M\cap\mathcal D_N.
$$
所有实际代入及中间词都有定义，而且每个
$\widetilde P_j(Y,B')f=0$。
因此 (9.3) 给 $D_0 f=0$，或 (9.4) 给
$$
Q(Y_\nu)f=0\quad\text{或}\quad Q(B'_\nu)f=0.
$$
左侧相应算子单射，故 $f=0$。
$R(t)^N$ 单射，再得 $x=0$。
于是
$$
\boxed{
\bigcap_{j=1}^m\ker\gamma_{\zeta_j}\mathsf P=0,
\qquad m\le n,\quad \zeta_1=1.
}
\tag{9.5}
$$
原多项式由 (8.9) 恢复。
证明只在一个足够高的有限共同域上执行恒等式，未把整个未知核强行置入全部混合幂域。

若 $n=0$，归约后只是一个非零 $\mathcal G$ 元素。
由 (8.7) 直接得到 $\ker\mathsf P=0$，无需附加 gauge。

### 9.4 总值域和联合循环

每个 $\gamma_{\zeta_j}\mathsf P$ 均为 $C$ 自伴。
这可直接由 (7.3)、(5.1) 得到，也可用
$CU_\zeta C=\zeta U_\zeta$ 共轭后常数相消验证。
因此 (9.5) 等价于
$$
\boxed{
\overline{\sum_{j=1}^m
\operatorname{Ran}(\gamma_{\zeta_j}\mathsf P)}=H.
}
\tag{9.6}
$$

若 $\xi\in\operatorname{Dom}\mathsf P$ 对 $A$ 循环，则
$U_{\zeta_j}\xi$ 对 $A$ 仍循环，属于相应共轭域。
由 (6.1)，
$$
[\;U_{\zeta_j}\mathsf P\xi\;]_A
=\overline{\operatorname{Ran}(\gamma_{\zeta_j}\mathsf P)}.
$$
所以
$$
\boxed{
\mathsf P\xi,\ U_{\zeta_2}\mathsf P\xi,\ldots,
U_{\zeta_m}\mathsf P\xi
\text{ 联合循环}.
}
\tag{9.7}
$$
这不是关于每个单独向量循环性的结论。

## 10. 任意指数权下的共同整向量与混合 Bell 恒等式

取
$$
w=b_*+\sum_j b_j\chi_j,\qquad b\in\ell^2,\qquad
\xi_w=e^w.
\tag{10.1}
$$
R16 的真实乘积结论给 $\xi_w\ne0$ 且对 $A$ 循环。

定义
$$
R_j(b_j)
=(V_j\cosh b_j+I\sinh b_j)
  (I\cosh b_j+V_j\sinh b_j)^{-1}
=\frac{I-e^{-2b_j}N_j}{I+e^{-2b_j}N_j}.
\tag{10.2}
$$
所有逆都是实际 $\mathcal A$ 单位。
分母字符为 $e^{b_j}\ne0$。
有限低位用实际单位的有限范数界，高位因 $b_j\to0$ 用同一小圆估计，得
$$
\sup_j\|R_j(b_j)\|<\infty,\qquad
R_j(b_j)-V_j=b_jK_j,\quad \sup_j\|K_j\|<\infty.
\tag{10.3}
$$
因此
$$
H_{i,b}:=\sum_j a_{ij}(R_j(b_j)-V_j)\in\mathcal A
\tag{10.4}
$$
按范数绝对收敛，由 $\sum_j|a_{ij}b_j|<\infty$ 保证。
其字符为零。
对固定 dyadic gauge，高位全部固定，所以 $\delta_\zeta H_{i,b}$ 是有限个真实有理解析项，属于 $\mathcal G$。

令
$$
Y_{i,b}=X_i+H_{i,b}.
\tag{10.5}
$$
它们满足前面全部域结论与有限增量条件。
不同位的实际有限恒等式为
$$
\boxed{
\left(\prod_{j\in J}R_j(b_j)\right)\xi_w
=\chi_J\xi_w
\quad(J\text{ 有限且无重复位}).
}
\tag{10.6}
$$
这里没有声称 $R_j(b_j)^2\xi_w=\xi_w$。

### 10.1 联合归一化乘积

对 $t=(t_1,\ldots,t_d)\in\mathbb C^d$，置
$$
z_j(t)=\sum_{i=1}^d t_i a_{ij}
$$
以及
$$
\mathcal B_b(t)
=\prod_{j\ge0}
e^{-z_j(t)R_j(b_j)}
\bigl(\cosh z_j(t)+R_j(b_j)\sinh z_j(t)\bigr).
\tag{10.7}
$$
在任意紧参数集上，$z(t)\in\ell^2$ 一致有界且尾范数一致趋零。
每个高位局部因子为 $I+O(|z_j(t)|^2)$，逆也同样。
有限低位因子对全部参数均为实际单位。
因此 (10.7) 及其逆按范数局部一致收敛，定义整个 $\mathcal A$ 值解析函数，且
$$
\mathcal B_b(0)=I,\qquad
\chi(\mathcal B_b(t))=1.
\tag{10.8}
$$

$e^{\sum_i t_i u_i+w}$ 是整个 $H$ 值解析函数。
例如，Rademacher 指数矩界控制其在每个紧参数集上的 $L^4$ 范数，
而平方可和尾保证有限截断在 $L^2$ 中局部一致收敛；
Banach 值 Cauchy 公式继而给全部有限阶导数的局部一致收敛。

定义
$$
\mathcal V_b(t)
=\mathcal B_b(t)^{-1}
 e^{\sum_i t_i u_i+w}.
\tag{10.9}
$$
它是整个 $H$ 值函数，$\mathcal V_b(0)=\xi_w$。

### 10.2 每个混合导数都在真实闭域

令
$$
Y_{i,b,N}=a_{i,*}I+\sum_{j<N}a_{ij}R_j(b_j).
$$
截断 (10.7)—(10.9)，只截 $u_i$ 与归一化乘积，保留完整 $\xi_w$。
由 (10.6)，有精确有限恒等式
$$
\mathcal V_{b,N}(t)
=\exp\left(\sum_i t_iY_{i,b,N}\right)\xi_w.
\tag{10.10}
$$
所以对每个多重指标 $\alpha$，
$$
Y_{i,b,N}\,\partial^\alpha\mathcal V_{b,N}(t)
=\partial^{\alpha+e_i}\mathcal V_{b,N}(t).
\tag{10.11}
$$

R125 的有限柱双图核心及 (10.4) 的范数收敛给
$$
Y_{i,b,N}^*h\longrightarrow Y_{i,b}^*h
\qquad(h\in\mathcal D_c).
\tag{10.12}
$$
(10.9) 的局部一致收敛给全部导数强收敛。
把 (10.11) 与 $h\in\mathcal D_c$ 配对并取极限，再用
$\mathcal D_c$ 是 $Y_{i,b}^*$ 的图核心，得到完整域结论
$$
\boxed{
\partial^\alpha\mathcal V_b(t)\in\operatorname{Dom}Y_{i,b},
\qquad
Y_{i,b}\partial^\alpha\mathcal V_b(t)
=\partial^{\alpha+e_i}\mathcal V_b(t).
}
\tag{10.13}
$$
这一步证明真实闭域，不能用形式指数记号取代。

重复 (10.13)，得 $\xi_w$ 属于任意有限混合词的自然域，且
$$
Y_{1,b}^{\alpha_1}\cdots Y_{d,b}^{\alpha_d}\xi_w
=\partial^\alpha\mathcal V_b(0)
\tag{10.14}
$$
与作用顺序无关。
取 $b=0,w=0$，即独立得到原 $X_i$ 的全部混合词作用于 $1$ 的结论。
加任意有界交换扰动后，有限词展开仍给 (1.2) 中 $1$ 的全部混合域。

### 10.3 全部高阶累积量是有界加性模式

定义标量多项式
$$
L_k(v)=\left.\frac{d^k}{dz^k}\log(\cosh z+v\sinh z)\right|_{z=0},
\qquad k\ge2.
$$
$L_k(1)=0$。
对 $|\alpha|=k\ge2$，置
$$
K_\alpha
=\sum_{j\ge0}
\left(\prod_i a_{ij}^{\alpha_i}\right)L_k(R_j(b_j)).
\tag{10.15}
$$
此级数按范数绝对收敛。
确实，选择乘积中的任意两个 $\ell^2$ 因子，用 Cauchy–Schwarz；
其余有限个因子用 $\ell^\infty$ 界，再用 (10.3) 对固定多项式 $L_k$ 的统一界。

所以 $K_\alpha\in\mathcal A$、$\chi(K_\alpha)=0$。
固定 gauge 后，只有有限低位项改变，故
$$
\gamma_\zeta K_\alpha-K_\alpha\in\mathcal G.
\tag{10.16}
$$
这些是实际有界加性模式。

在原点邻域，
$$
\log\mathcal B_b(t)
=\sum_{|\alpha|\ge2}K_\alpha\,\frac{t^\alpha}{\alpha!}.
\tag{10.17}
$$
对任意固定有限次数只需有限 jet。
记
$$
B_\alpha=\partial^\alpha\mathcal B_b(0).
$$
则 $B_0=I$、$B_{e_i}=0$；一般 $B_\alpha$ 是有限组
$\{K_\beta:2\le|\beta|\le|\alpha|\}$ 的有限 Bell 多项式。
没有把点态乘法与实际算子乘法混同。

### 10.4 点态多项式的真实闭实现

令 $F\in\mathbb C[t_1,\ldots,t_d]$，总次数为 $p$。
对
$$
e^{\sum_i t_i u_i+w}
=\mathcal B_b(t)\mathcal V_b(t)
$$
作有限次 Leibniz 求导，得到
$$
\boxed{
F(u_1,\ldots,u_d)e^w
=
P_F(Y_b,K)\xi_w,
}
\tag{10.18}
$$
其中右侧在共同自然域中有定义，且
$$
\boxed{
P_F(Y_b,K)
=\sum_{|\alpha|\le p}
\frac{B_\alpha}{\alpha!}\,
(\partial^\alpha F)(Y_{1,b},\ldots,Y_{d,b}).
}
\tag{10.19}
$$
最大闭实现 $\mathsf P_F$ 由 §§4—5 给出，并满足
$$
\mathsf P_F\xi_w=F(u)e^w.
$$
因为 $\xi_w$ 循环，(6.1) 给
$$
\boxed{
[F(u)e^w]_A=\overline{\operatorname{Ran}\mathsf P_F}.
}
\tag{10.20}
$$
这里的闭算子是相对于循环基向量 $\xi_w$ 识别的实际实现。
不从 (10.18) 自动推断以 $1$ 为基向量的另一个初始乘子具有相同全域。

## 11. 有限模式点态多项式的有限 gauge 联合循环

假设
$$
f=F(u_1,\ldots,u_d)e^w\ne0.
$$
由 (10.18)，$\mathsf P_F$ 是非零实际闭实现。
它只涉及：

- $d$ 个平方可和第一阶模式及有界加性倾斜；
- 至多
$$
\#\{\alpha\in\mathbb N^d:2\le|\alpha|\le p\}
=\binom{d+p}{p}-d-1
$$
个有界加性累积量。

按 §8 进行真实仿射归约和有限清分母。
设剩余独立增量类的总秩为 $n$。
这是一个明确的代数秩：先按原行在 $\ell^2/\ell^1$ 的类取基，再对所有剩余真实有界加性模式的类模 $K$ 取基。
其满足
$$
n\le \binom{d+p}{p}-1.
\tag{11.1}
$$

由 §9：

- 若 $n=0$，$f$ 本身循环。
- 若 $n\ge1$，存在 $\zeta_1=1,\zeta_2,\ldots,\zeta_m\in\Gamma$，
  $m\le n$，使
$$
\boxed{
\overline{\operatorname{span}
\{A^kU_{\zeta_j}f:k\ge0,\ 1\le j\le m\}}=H.
}
\tag{11.2}
$$

特别，当 $p\ge1,d\ge1$ 时，总共至多
$$
\boxed{\binom{d+p}{p}-1}
\tag{11.3}
$$
个 gauge 像足够；这一粗界可由实际类秩减小。
$p=0$ 的非零常数倍 $e^w$ 已单独循环。
$d=1$ 时 (11.3) 为 $p$，与 R180 的一模式界一致；本稿的新增范围是任意有限个独立或相关平方可和模式。

选择可以包含原向量，并按步骤避开有限坏参数。
本稿不声称所有 gauge 参数元组都泛型同样，也不声称一般 $f$ 的单个核已经排除。

## 12. 结论的边界及新接口

本稿完成的是：

1. 有限多个真实闭一阶乘子的共同混合词图；
2. 任意有界交换系数多项式的规范最大闭实现、自然闭包及完整 $C$ 自伴；
3. 核内每个固定高阶的共同稠密测试空间；
4. 任意有限平方可和模式的点态多项式乘任意平方可和指数权的有限 gauge 联合循环。

没有得到以下断言：

- 一般混合自然多项式的原域 $\mathcal D_p$ 已是最大闭域；
- 一般多变量多项式单射，或其分母构成多变量闭分式场；
- 全 $H$ 的值域稠密性自动传到未知不变限制；
- 任意未知子商具有同一多变量最大域、共轭或分式演算；
- 单个慢 Bell 共振向量已经循环。

实际的新增用途在于：今后所有有限模式恒等式、gauge 消元及有限证书，都可以在 (5.3) 的真正高混合阶核内执行，而不必假设未知核向量预先具有混合自然域正则性。
