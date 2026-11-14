# R183：非首一快系数多项式的最大闭实现与整个 $K(Y)$ 分式场

日期：2026-11-12（UTC）。作者：literature。根代理预留 R183。

状态：完整证明。保留非首一多项式的最大域与自然域之区别；通过固定正则器在实际不变闭图中的稠密性，完成最大图、自然多项式闭包、完整 $C$ 伴随域及原分母图核心。非零多项式排核只使用核内足够高次幂域的稠密子集，不声称整个核预先属于自然幂域。全部分式结论在原 $H$ 上陈述，不自动下降为任意未知限制上的稠密像。

## 1. 设置与结论

沿用
$$
\mathcal G\subseteq\mathcal A,\qquad
K=\operatorname{Frac}\iota(\mathcal G)\subseteq\mathbb C((z)).
$$
取
$$
X=X_u,\qquad
u=a_*+\sum_ja_j\chi_j,\qquad
a\in\ell^2\setminus\ell^1,
$$
以及有界加性模式
$$
H\in\mathcal A,\qquad
\gamma_\zeta H-H\in\mathcal G
\quad(\zeta\in\Gamma=\mu_{2^\infty}).
$$
令
$$
Y=X+H,\qquad \operatorname{Dom}Y=\operatorname{Dom}X.
\tag{1.1}
$$

R180 已证明：$Y$ 的形式增量原函数
$$
\beta_Y=\beta_a+\iota(H)
$$
超越于 $K$。相应一变量半线性作用
$$
\Lambda_\zeta P(t)
=(\alpha_\zeta P)(t+d_\zeta),\qquad
d_\zeta=\iota(U_\zeta YU_\zeta^*-Y)\in\iota(\mathcal G)
\tag{1.2}
$$
使 $K[t]$ 没有非零真稳定理想。
$\beta_Y$ 只用来证明该纯代数事实，本稿不把它直接求值于 $A$。

对
$$
P(t)=\sum_{j=0}^p g_jt^j\in\mathcal G[t]
$$
的自然实现
$$
P_{\rm nat}(Y)=\sum_{j=0}^p g_jY^j,\qquad
\operatorname{Dom}P_{\rm nat}(Y)=\operatorname{Dom}Y^p,
\tag{1.3}
$$
不要求最高系数为单位。

**定理1.1。** $P_{\rm nat}(Y)$ 可闭，其闭包 $\mathsf P$ 有下文 (3.2) 的规范最大图。它满足：

- $\mathsf P$ 闭、稠密定义、$C$ 自伴；
- 原正则分母参数图是完整图核心；
- 有限柱空间本身是 $\mathsf P$ 的图核心；
- 若 $P\ne0$，则 $\mathsf P$ 单射且值域稠密；
- 若 $\deg P\ge1$，则 $\mathsf P$ 无界；
- 不声称 $\operatorname{Dom}\mathsf P=\operatorname{Dom}Y^p$。

**定理1.2。** 上述实现延拓为整个
$$
K(t)=\operatorname{Frac}(\mathcal G[t])
$$
的忠实最大闭分式演算，记为 $f\mapsto T_f$，并以 $t$ 对应 $Y$。
每个 $T_f$ 都闭、稠密定义、$C$ 自伴，且
$$
\boxed{
\overline{T_f+T_g}=T_{f+g},\qquad
\overline{T_fT_g}=T_{fg},\qquad
(T_f)^{-1}=T_{1/f}\quad(f\ne0).
}
\tag{1.4}
$$
每个非零 $T_f$ 单射且值域稠密。
若 $f$ 不是复常数，全部 $T_f-\lambda I$ 都单射且值域稠密。
对 $f\ne0$、$x\in\operatorname{Dom}T_f$，
$$
\boxed{
x\text{ 对 }A\text{ 循环}
\iff T_fx\text{ 对 }A\text{ 循环}.
}
\tag{1.5}
$$

这里可将该实际闭分式场称为 $K(Y)$。
这不是先把每个 $K$ 系数当成有界算子，再在一个不明共同域上无限求值。

## 2. 固定正则器在所有有限放大不变图中稠密

### 2.1. 正则器与参数单位比率

沿用 R128/R140 对基础第一阶 $X$ 的正分量正则器。
对 $s,t>0$，
$$
R(t)\in\{A\}',\qquad R(t)\to I\text{ 强},\qquad
\|R(t)\|\le1,
$$
且每个 $R(t)$ 单射、稠密像，并满足
$$
R(s)=R(t)U(s,t),\qquad
U(s,t),U(s,t)^{-1}\in\{A\}'.
\tag{2.1}
$$
全部有界交换子彼此交换。

设
$$
S(t)=YR(t)=XR(t)+HR(t)\in\{A\}'.
\tag{2.2}
$$
这是有界算子。
由于 $Y$ 与有界交换子域交换，
$$
S(s)=S(t)U(s,t).
\tag{2.3}
$$

对 $N\ge k\ge0$，逐次域交换给
$$
\boxed{
R(t)^NH\subseteq\operatorname{Dom}Y^N,\qquad
Y^kR(t)^N=S(t)^kR(t)^{N-k}.
}
\tag{2.4}
$$

### 2.2. 有限放大中的固定幂密度

令 $\mathcal L\subset H^{\oplus d}$ 是任意闭
$A^{(d)}$ 不变空间。
R88 的强多项式闭包说明，
每个有界交换子 $B$ 的对角放大 $B^{(d)}$ 都保持 $\mathcal L$：
同一个多项式网在有限个坐标上强收敛即可。

因此 $U(s,t)^{(d)}$ 及其逆保持 $\mathcal L$，
由 (2.1) 得
$$
(R(s)^N)^{(d)}\mathcal L
=(R(t)^N)^{(d)}\mathcal L.
$$
而对每个固定 $N$，
$R(s)^N\to I$ 强。
故
$$
\boxed{
\overline{(R(t)^N)^{(d)}\mathcal L}=\mathcal L.
}
\tag{2.5}
$$
这里只需要 $N$ 固定，不让正则器幂次随测试向量的极限过程不受控地增长。

同样，R151 给对每个 $0\ne D\in\mathcal G$，
$$
\overline{D^{(d)}\mathcal L}=\mathcal L.
$$
两个有界映射都保持 $\mathcal L$ 且各有稠密像，
其乘积也有稠密像。
因此
$$
\boxed{
\overline{(D R(t)^N)^{(d)}\mathcal L}=\mathcal L.
}
\tag{2.6}
$$

(2.5)—(2.6) 是后面闭图核心的准确输入。
本稿不需要假设原空间的共轭保持 $\mathcal L$。

## 3. 非首一多项式的规范最大图

固定一个 $t>0$，简记
$$
R=R(t),\qquad S=S(t).
$$
对于 $P=\sum_{j=0}^p g_jt^j$，定义有界正则化
$$
\boxed{
B_P^{[p]}
=\sum_{j=0}^p g_j S^jR^{p-j}\in\{A\}'.
}
\tag{3.1}
$$
定义最大图
$$
\boxed{
\operatorname{Graph}\mathsf P
=\{(x,y)\in H\oplus H:
B_P^{[p]}x=R^py\}.
}
\tag{3.2}
$$
因 $R^p$ 单射，这是单值闭图。
交换性使
$$
(R^ph,B_P^{[p]}h)
$$
总属于图中，所以定义域包含稠密的 $R^pH$。

### 3.1. 参数与填充次数无关

由 (2.1)、(2.3)，改用 $s$ 时，
$$
B_P^{[p]}(s)=B_P^{[p]}(t)U(s,t)^p,\qquad
R(s)^p=R(t)^pU(s,t)^p.
$$
因为 $U(s,t)^p$ 可逆并与全部因子交换，最大图不变。

也允许使用任意填充次数 $N\ge p$：
$$
B_P^{[N]}=\sum_{j=0}^p g_j S^jR^{N-j}
=R^{N-p}B_P^{[p]}.
\tag{3.3}
$$
将 (3.2) 的两边同乘单射 $R^{N-p}$，不会改变最大图。
这允许后面对不同次数多项式使用同一个有界分母。

常数多项式得到原来的有界 $\mathcal G$ 算子；
零多项式得到全域零算子，不依赖所选填充次数。

### 3.2. 自然域包含于最大域

对 $x\in\operatorname{Dom}Y^p$，
域交换给
$$
B_P^{[p]}x=R^pP_{\rm nat}(Y)x.
\tag{3.4}
$$
所以自然图包含于最大图。
最大图闭，故自然实现可闭。

### 3.3. 最大图没有多出无法逼近的部分

设 $(x,y)$ 满足 (3.2)。
令
$$
x_s=R(s)^px\in\operatorname{Dom}Y^p.
$$
全部有界正则因子交换，故
$$
\begin{aligned}
R^pP_{\rm nat}(Y)x_s
&=B_P^{[p]}R(s)^px\\
&=R(s)^pB_P^{[p]}x
=R^pR(s)^py.
\end{aligned}
$$
消去单射的 $R^p$，得到
$$
P_{\rm nat}(Y)x_s=R(s)^py.
$$
当 $s\downarrow0$，两个图坐标趋于 $(x,y)$。
因此
$$
\boxed{\mathsf P=\overline{P_{\rm nat}(Y)}.}
\tag{3.5}
$$
证明没有要求 $P_{\rm nat}(Y)$ 本来闭，也没有要求 $g_p$ 有界可逆。

## 4. 原参数图核心与完整 $C$ 伴随域

### 4.1. 固定分母的图核心

$\mathcal L=\operatorname{Graph}\mathsf P$ 是闭
$A\oplus A$ 不变空间。
对 $(x,y)\in\mathcal L$，
$$
(R^px,R^py)=(R^px,B_P^{[p]}x)
$$
属于原参数图。
(2.5) 在 $\mathcal L$ 上给
$$
\boxed{
\operatorname{Graph}\mathsf P
=\overline{\{(R^ph,B_P^{[p]}h):h\in H\}}.
}
\tag{4.1}
$$
参数 $h$ 可缩为任何在 $H$ 中稠密的集合，
例如有限柱或 $\mathbb C[A]1$。
准确的域核心先是 $R^p\mathcal D_c$，不能仅从 (4.1) 删除前面的 $R^p$。

### 4.2. 整个伴随域

令 $T_0(R^ph)=B_P^{[p]}h$。
(4.1) 给 $\overline{T_0}=\mathsf P$。
其通常伴随的图条件准确为
$$
(v,w)\in\operatorname{Graph}T_0^*
\iff (B_P^{[p]})^*v=(R^p)^*w.
\tag{4.2}
$$
两个有界系数都属于 $\{A\}'$，
R88 给它们 $C$ 对称。
共轭 (4.2) 后得到
$$
B_P^{[p]}Cv=R^pCw,
$$
正是最大图 (3.2)。
因此
$$
\boxed{\mathsf P^*=C\mathsf PC.}
\tag{4.3}
$$
这证明整个伴随域，不只是在一个稠密核心上对称。

### 4.3. 有限柱本身确实为图核心

R176 已证明有限柱 $\mathcal D_c$ 是自然闭幂 $Y^p$ 的图核心。
低次幂的插值估计给
$$
\|P_{\rm nat}(Y)x\|
\le C_P(\|x\|+\|Y^px\|).
\tag{4.4}
$$
所以在 $Y^p$ 图范数中用有限柱逼近，
同时也在自然 $P$ 的图范数中逼近。
结合 (3.5)，得到
$$
\boxed{
\overline{P_{\rm nat}(Y)|_{\mathcal D_c}}=\mathsf P.
}
\tag{4.5}
$$
这一步依赖原 $H$ 上已经证明的高次柱核心。
没有把它自动下降到未知子商。

### 4.4. 有界交换子保持最大域

若 $B\in\{A\}'$，则它与 (3.2) 的两个有界系数交换。
所以
$$
B\operatorname{Dom}\mathsf P\subseteq\operatorname{Dom}\mathsf P,
\qquad \mathsf P Bx=B\mathsf Px.
\tag{4.6}
$$

## 5. 非首一核内足够高幂的稠密测试空间

对非零 $P$，置
$$
M=\ker\mathsf P.
$$
由 (3.2)，
$$
\boxed{M=\ker B_P^{[p]}.}
\tag{5.1}
$$
所以 $M$ 是闭 $A$ 不变空间，且被全部有界交换子保持。

一般不知 $M\subseteq\operatorname{Dom}Y^p$。
本稿不使用这个断言。
代之以：对每个固定 $N$，
$$
\boxed{
R^NM\subseteq M\cap\operatorname{Dom}Y^N,\qquad
\overline{R^NM}=M.
}
\tag{5.2}
$$
第一式由 $R$ 与 $B_P^{[p]}$ 交换及 (2.4)；
第二式由 (2.5)。

此外，若 $f\in M\cap\operatorname{Dom}Y$，
因为 $B_P^{[p]}\in\{A\}'$ 与 $Y$ 域交换，
$$
B_P^{[p]}Yf=YB_P^{[p]}f=0.
$$
所以
$$
Y(M\cap\operatorname{Dom}Y)\subseteq M.
\tag{5.3}
$$
因此对 $f\in R^NM$，只要剩余幂数足够，
对它施加任何有限 $Y$ 多项式仍留在相应核中。

这正是跨核配对所需的替代。
无需把非首一核上的 $Y$ 限制先证明为有界算子。

## 6. gauge 共轭与非首一多项式排核

### 6.1. 共轭由自然闭包确定

R180/R176 给
$$
U_\zeta YU_\zeta^*=Y+D_\zeta,\qquad
D_\zeta\in\mathcal G,
$$
连同全部自然幂域相等。
所以在 $\operatorname{Dom}Y^p$ 上，
$$
U_\zeta P_{\rm nat}(Y)U_\zeta^*
=(\Lambda_\zeta P)_{\rm nat}(Y).
$$
取双方闭包并用 (3.5)，得到
$$
\boxed{
U_\zeta\mathsf P U_\zeta^*
=\mathsf{\Lambda_\zeta P}.
}
\tag{6.1}
$$
因此 $M_\zeta:=\ker\mathsf{\Lambda_\zeta P}=U_\zeta M$，
并具有 §5 的所有高幂稠密测试空间。

无需假设 gauge 后的正则器等于原来的 $R$。
自然闭包已经给出 (6.1)。

### 6.2. 有限例外的快 Bézout 恒等式

R180 给 $\beta_Y$ 超越于 $K$。
R166 的纯形式论证使一变量作用 (1.2) 为 $\Gamma$ 单环。
有限不可约分解、Prüfer 真子群有限和因子相遇的陪集论证，
给一个有限 dyadic 子群 $H_0$，使
$$
\gcd_{K[t]}(P,\Lambda_\zeta P)=1
\qquad(\zeta\notin H_0).
$$
清 Euclidean 算法中的有限个 $\mathcal G$ 分母后，得到
$$
\boxed{
D=UP+V\Lambda_\zeta P,\qquad
0\ne D\in\mathcal G,\quad U,V\in\mathcal G[t].
}
\tag{6.2}
$$

### 6.3. 只在已合法的有限高幂域上配对

固定这样的 $\zeta$。
取整数
$$
N\ge\max\{\deg U+\deg P,\ \deg V+\deg P\}.
$$
对
$$
f\in R^NM,\qquad k\in R^NM_\zeta,
$$
所有 (6.2) 中需要的多项式和跨 $B$ 移项都具有足够自然幂域。

第一项 $P_{\rm nat}(Y)f$ 为零：
它与最大实现相同，而 $f\in M\cap\operatorname{Dom}Y^p$。

第二项经 $B$ 对称性移到 $k$：
$V_{\rm nat}(Y)k$ 由 (5.3) 仍在 $M_\zeta$，
且因选定 $N$ 仍在 $\operatorname{Dom}Y^p$。
所以 $(\Lambda_\zeta P)_{\rm nat}(Y)V_{\rm nat}(Y)k=0$。
得到
$$
B(Df,k)=0.
$$

(5.2) 及 $D$ 有界允许两端取闭包，得
$$
B(DM,M_\zeta)=0.
$$
R151 的 $\overline{DM}=M$ 再给
$$
B(M,U_\zeta M)=0\qquad(\zeta\notin H_0).
\tag{6.3}
$$

R180 §9 已重述的有限 Fourier 支撑、满本质支撑和柱限制秩论证
使 $M$ 有限维；
实际 $A$ 单射拟幂零迫使 $M=0$。
因此
$$
\boxed{
\ker\mathsf P=0,\qquad
\ker B_P^{[p]}=0
\qquad(P\ne0).
}
\tag{6.4}
$$
由 (4.3)，$\mathsf P$ 值域稠密；
由有界 $C$ 对称性，$B_P^{[p]}$ 也值域稠密。
任何更高填充次数的 $B_P^{[N]}$ 同样单射稠密。

定理1.1 的单射稠密结论得证。

### 6.4. 正次数多项式仍然无界

若 $\deg P=p\ge1$，将 $Y=X+H$ 有限展开。
其最高 $X^p$ 系数是 $g_p\in\mathcal G\setminus\{0\}\subseteq\mathfrak U$，
其余系数有界。
R171 说明该算子在有限柱上无界。
$\mathsf P$ 延拓这个实际作用，因此也无界。

这不要求证明 $g_p$ 有界可逆。

## 7. 整个分式的规范最大实现

给
$$
f=P/Q\in K(t),\qquad P,Q\in\mathcal G[t],\quad Q\ne0.
$$
有限清分母总可得到这种表示。
取
$$
N\ge\max\{\deg P,\deg Q\}
$$
并记
$$
A_f=B_P^{[N]},\qquad B_f=B_Q^{[N]}.
$$
当 $P\ne0$ 时两者都单射稠密；
分母 $B_f$ 始终单射稠密。

定义
$$
\boxed{
\operatorname{Dom}T_f=\{x:A_fx\in\operatorname{Ran}B_f\},
\qquad B_fT_fx=A_fx.
}
\tag{7.1}
$$
这是单值闭图，域包含 $B_fH$，因而稠密。

填充次数变化由额外单射 $R$ 幂取消。
正则参数变化由 (2.1)—(2.3) 的有界单位共同因子取消。
所以 (7.1) 不依赖这些选择。

当 $Q=1$，$B_f=R^N$，
该实现恰为 §§3–6 的 $\mathsf P$。

## 8. 有限 gcd 与有界化 Bézout

本节证明原分母参数图是完整核心，这是闭场构造的关键。

### 8.1. 在 $K[t]$ 中分离共同因子

先假定 $P\ne0$。
在 $K[t]$ 中取首一 gcd，
再有限清分母，得到
$$
dP=G P_1,\qquad dQ=G Q_1,
\tag{8.1}
$$
其中
$$
0\ne d\in\mathcal G,\qquad
G,P_1,Q_1\in\mathcal G[t]\setminus\{0\},
\qquad \gcd_{K[t]}(P_1,Q_1)=1.
$$
这里可以先将 gcd、互素商各自乘一个非零 $\mathcal G$ 分母；
两分母的乘积就是 $d$。
未把 $K$ 系数提前作为有界算子求值。

Euclidean 算法再给
$$
\boxed{
U P_1+V Q_1=D,\qquad
U,V\in\mathcal G[t],\quad
0\ne D\in\mathcal G.
}
\tag{8.2}
$$

### 8.2. 用正则器把所有 Bézout 系数变成有界算子

选
$$
m\ge\max(\deg P_1,\deg Q_1),\qquad
k\ge\max(\deg U,\deg V).
$$
置
$$
A_1=B_{P_1}^{[m]},\quad B_1=B_{Q_1}^{[m]},
\qquad \widehat U=B_U^{[k]},\quad \widehat V=B_V^{[k]}.
$$
有限正则化多项式的乘法恒等式给
$$
\boxed{
\widehat U A_1+\widehat V B_1=D R^{k+m}=:E.
}
\tag{8.3}
$$
所有因子都是真正有界交换子。
由 (2.6)，$E\oplus E$ 在每个闭
$A\oplus A$ 不变空间上像稠密。

令
$$
\mathcal L_1=\{(x,y):A_1x=B_1y\}.
$$
若 $(x,y)\in\mathcal L_1$，取
$$
h=\widehat Vx+\widehat Uy.
$$
利用 (8.3) 及 $A_1x=B_1y$，直接得到
$$
B_1h=Ex,\qquad A_1h=Ey.
$$
于是
$$
(E\oplus E)\mathcal L_1
\subseteq\{(B_1h,A_1h):h\in H\}
\subseteq\mathcal L_1.
$$
取闭包得
$$
\boxed{
\mathcal L_1
=\overline{\{(B_1h,A_1h):h\in H\}}.
}
\tag{8.4}
$$

这里没有把无界 $U(Y),V(Y)$ 直接作用于未知最大图向量；
正则器已在 (8.3) 前把它们全部有界化。

### 8.3. 恢复原分母，不能只停在互素分母

令 $g=\deg G$，把原 $P,Q$ 填充到 $g+m$ 次，
并令 $\widehat G=B_G^{[g]}$。
(8.1) 变为实际有界恒等式
$$
dA_f=\widehat G A_1,\qquad
dB_f=\widehat G B_1.
\tag{8.5}
$$
$d$ 和 $\widehat G$ 都单射稠密。
所以对任意 $x,y$，
$$
A_fx=B_fy
\iff A_1x=B_1y.
\tag{8.6}
$$
而由两个共同因子的全空间稠密像，
$$
\begin{aligned}
\overline{\{(B_fh,A_fh):h\in H\}}
&=\overline{\{(B_fdh,A_fdh):h\in H\}}\\
&=\overline{\{(\widehat G B_1h,\widehat G A_1h):h\in H\}}\\
&=\overline{\{(B_1h,A_1h):h\in H\}}.
\end{aligned}
\tag{8.7}
$$
结合 (8.4)—(8.6)，得到
$$
\boxed{
\operatorname{Graph}T_f
=\overline{\{(B_fh,A_fh):h\in H\}}.
}
\tag{8.8}
$$

$\widehat G$ 在此只用全 $H$ 上的单射稠密。
没有宣称它在任意未知不变限制上也像稠密。

若 $P=0$，最大实现是全域零算子；
(8.8) 直接由 $B_fH$ 稠密成立。

## 9. 伴随、表示无关性与忠实性

### 9.1. 完整 $C$ 自伴

由 (8.8)，参数核心 $T_0(B_fh)=A_fh$ 的伴随条件是
$$
A_f^*v=B_f^*w.
$$
有界交换子均 $C$ 对称，
该等式经 $C$ 共轭正是最大图条件。
所以
$$
\boxed{T_f^*=CT_fC.}
\tag{9.1}
$$

有限柱或 $\mathbb C[A]1$ 可作为 (8.8) 的参数空间，
因为 $(B_f,A_f):H\to H\oplus H$ 有界。
域核心是 $B_f\mathcal D_c$ 或 $B_f\mathbb C[A]1$；
不能一般删除 $B_f$。

### 9.2. 分式表达无关

若 $P/Q=P'/Q'$，则 $PQ'=P'Q$。
将两组表示分别以足够次数正则化，得到
$$
A_fB_f'=A_f'B_f.
\tag{9.2}
$$
若 $A_fx=B_fy$，
则乘另一分子分母并利用交换性得
$$
B_f(A_f'x-B_f'y)=0.
$$
$B_f$ 单射给另一最大图条件。
反向同理，所以最大实现只依赖分式。

反之，若两个最大实现相同，
在 $B_fB_f'h$ 上比较它们的值，
得到 (9.2) 对所有 $h$ 成立。
这等价于某个足够高次数正则化的
$PQ'-P'Q$ 为零。
§6 已证明非零多项式的正则化单射，
故只能有 $PQ'=P'Q$。
演算忠实。

### 9.3. 有界交换子保持最大分式域

因 $A_f,B_f\in\{A\}'$ 且该代数交换，
对任何 $L\in\{A\}'$，
$$
L\operatorname{Dom}T_f\subseteq\operatorname{Dom}T_f,\qquad
T_fLx=LT_fx.
\tag{9.3}
$$

这不是所有未知不变子空间的图都自动由该分母饱和；
后者需要额外的限制稠密性，见 §13。

## 10. 自然和、积、逆的闭包

写两个分式的有界表示为
$$
T_f=B^{-1}A,\qquad T_g=D^{-1}C,
$$
其中 $A,B,C,D$ 都有界、交换，
$B,D$ 单射稠密。
若分式非零，相应分子也单射稠密。

自然和与自然乘积的域都包含稠密的 $BDH$，且
$$
(T_f+T_g)(BDh)=(AD+BC)h,
\tag{10.1}
$$
$$
T_fT_g(BDh)=AC h.
\tag{10.2}
$$
这些有界分子分母正是 $f+g$、$fg$ 的更高填充次数表示。

(8.8) 说明 (10.1)、(10.2) 的核心图闭包分别为
$T_{f+g}$、$T_{fg}$。
反向，在自然和的任意域向量上乘 $BD$，直接得对应最大图等式。
在自然乘积域上，若 $y=T_gx$、$z=T_fy$，则
$$
BDz=ACx.
$$
所以两个自然图都包含在相应最大闭图内。
由两向包含，
$$
\boxed{
\overline{T_f+T_g}=T_{f+g},\qquad
\overline{T_fT_g}=T_{fg}.
}
\tag{10.3}
$$
若结果分子为零，最大图为全域零算子，结论仍成立。

对 $f\ne0$，交换最大图两个坐标即得
$$
\boxed{(T_f)^{-1}=T_{1/f}.}
\tag{10.4}
$$

特别，$P/Q$ 也等于
$$
\overline{\mathsf Q^{-1}\mathsf P},
$$
其中乘积域按通常自然乘积定义。
本稿没有声称未经闭包的自然乘积本来闭，
也没有声称相反顺序的原始乘积域相同。

## 11. 核、范围与实际有界除法

若 $f=P/Q\ne0$，则 $A_f$ 单射，
故 $T_f$ 单射。
又
$$
T_f(B_fh)=A_fh
$$
说明其像包含稠密的 $A_fH$。
因此
$$
\boxed{\ker T_f=0,\qquad
\overline{\operatorname{Ran}T_f}=H.}
\tag{11.1}
$$

当 $f\notin\mathbb C$，对每个 $\lambda\in\mathbb C$，
$f-\lambda\ne0$。
由闭算子加有界标量的同域性，
$$
T_f-\lambda I=T_{f-\lambda}.
\tag{11.2}
$$
所以它没有点谱或剩余谱。

对固定有界表示 $T_f=B_f^{-1}A_f$，
准确判据为
$$
\boxed{
T_f\text{ 有界}
\iff \exists L\in B(H):B_fL=A_f,
}
\tag{11.3}
$$
以及
$$
\boxed{
\lambda\in\rho(T_f)
\iff \exists L\in B(H):(A_f-\lambda B_f)L=B_f.
}
\tag{11.4}
$$
成立时相应 $L$ 自动与 $A$ 交换：
比较等式的左乘与右乘 $A$，
再消去单射的 $B_f$ 或 $A_f-\lambda B_f$。

(11.3) 的右边使最大图恰为全域有界 $L$ 的图。
(11.4) 的右边给右逆；用分子单射性再给左逆。
反向均由有界算子或有界预解式立即得到。

这些是实际有界除法判据，
不是仅凭分式在某个形式点是否有极点作完整有界性分类。

## 12. 正无穷次数的一个严格无界障碍

对非零 $f=P/Q\in K(t)$，定义
$$
\deg_\infty f=\deg P-\deg Q.
$$
这个整数不依赖分式表示。

**命题12.1。**
若
$$
\deg_\infty f>0,
$$
则 $T_f$ 无界。

证明：若 $T_f=L$ 有界，则 (10.3) 在自然乘积域上给
$$
\mathsf P x=L\mathsf Qx.
$$
特别对每个有限柱 $x$，两边均等于各自自然多项式的实际作用，故
$$
P_{\rm nat}(Y)x-LQ_{\rm nat}(Y)x=0.
\tag{12.1}
$$
$L$ 自动属于有界交换子；
即便不使用其交换性，R171 也允许低阶系数只是有界算子。

因为 $\deg P>\deg Q$，
把 $Y=X+H$ 展开后，
(12.1) 的最高 $X$ 系数仍是 $P$ 的非零最高系数
$g_p\in\mathcal G\subseteq\mathfrak U$。
全部其他项只有较低次数和有界系数。
这与 R171 矛盾。证毕。

因此，对 $P-\lambda Q\ne0$，如果
$$
\deg Q>\deg(P-\lambda Q),
$$
则逆分式 $Q/(P-\lambda Q)$ 不能有界，
从而 $\lambda\in\sigma(T_f)$。

本稿不把 $\deg_\infty f\le0$ 作为有界性的充分条件，
也不由该次数判据替代 R182 对纯标量有理函数的更精细谱分类。

## 13. 循环性与限制范围的准确边界

### 13.1. 循环性双向传递

设 $f\ne0$、$x\in\operatorname{Dom}T_f$，
写 $y=T_fx$。
则
$$
A_fx=B_fy.
$$
有界 $A_f,B_f$ 都稠密像且与 $A$ 交换。

若 $x$ 循环，则 $A_fx$ 循环。
又 $B_fy$ 属于 $[y]_A$，
因为 R88 保证有界交换子保持每个闭 $A$ 不变空间。
所以 $y$ 循环。

若 $y$ 循环，同理 $B_fy$ 循环，
而 $A_fx\in[x]_A$，故 $x$ 循环。
这证明 (1.5)。

### 13.2. 多项式本身在不变空间上的域保持

对多项式实现 $\mathsf P$，
其分母是 $R^p$，确有额外的普遍饱和性。
若 $x\in M\cap\operatorname{Dom}\mathsf P$，$M$ 闭且 $A$ 不变，
则
$$
R^p\mathsf Px=B_P^{[p]}x\in M.
$$
固定 $R^p$ 的强主理想近似可由 (2.5) 的有限放大版本得到；
因而 $R^py\in M$ 迫使 $y\in M$。
所以 $\mathsf P$ 的域内向量仍被送入其闭循环空间。

也可直接用 §3.3 的 $R(s)^px\in M$：
其自然 $P$ 像在 $M$，且趋于 $\mathsf Px$。
这里自然 $Y$ 的限制像保持来自 R128，
有界 $H$ 及全部系数保持 $M$。
同样得到 $\mathsf Px\in M$。

这只给像保持，不给 $\overline{\mathsf P(\operatorname{Dom}\mathsf P\cap M)}=M$。

### 13.3. 一般分式的限制密度仍未自动成立

一般分母 $B_Q^{[N]}$ 只已证明全 $H$ 单射稠密。
本稿没有证明它在每个未知不变限制上像稠密，
所以不能把纯 $K$ 的所有子商结论全部搬到 $K(Y)$。

尤其不能声称对任意域向量都有
$$
[T_fx]_A=[x]_A.
$$
本稿证明的是全空间循环性的等价 (1.5)。

对于 $f=t$，任意复杂第一阶在未知不变空间上是否总有稠密值域，
仍是此前的真实缺口。
本稿没有借非首一闭图或全空间 $C$ 自伴性绕过该问题。

## 14. 依赖与新增内容

- [R128：第一阶域交换与正分量正则器](../results/R128-first-chaos-invariant-parts-and-resolvent-regularization.md)。
- [R140：固定参数正则器的单位比率](../results/R140-invariant-subquotient-type-and-fixed-first-regularization.md)。
- [R151：非零快系数在有限放大不变图中的稠密性](../results/R151-quartic-analytic-approximation-gauge-stability.md)。
- [R171：UHF 最高系数多项式的真实无界障碍](../results/R171-uhf-leading-polynomials-of-unbounded-first-multipliers.md)。
- [R176：自然幂闭性、有限柱核心与最高系数单位的多项式](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md)。
- [R180：无界第一阶的独立形式类与快 Bézout 跨核机制](../results/R180-unbounded-first-class-independence-and-l2-polynomial-gauge-cyclicity.md)。

本稿新增的是：非首一 $\mathcal G[Y]$ 的最大闭实现及完整 $C$ 自伴性；
不预设核包含自然幂域的排核证明；
以正则器有界化 Bézout 后恢复整个 $K(Y)$ 的原分母图核心；
忠实闭分式场、域内循环性双向传递，以及正无穷次数的实际无界障碍。

完整 Hilbert 不变子空间问题及一般未知限制的像稠密性仍未解决。
