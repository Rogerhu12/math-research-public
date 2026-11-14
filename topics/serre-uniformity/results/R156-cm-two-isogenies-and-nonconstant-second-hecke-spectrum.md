# R156：CM 二同源对应迫使第二 Hecke 特征值变化

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：完整证明。** 对原始三次环类周期，本文证明一般 $p$ 的 $M<p/2$ 范围，以及实际小惯性所满足的更宽范围
$$
\boxed{p\equiv2\pmod3,\quad M<p\quad\Longrightarrow\quad
\{a_2(f):L(1/2,\pi_{f,K}\otimes\eta)\ne0\}\text{ 不为单点}.}
$$
因而实际小惯性分支在这个范围内无须另加中心值非消失假设，即可使用 R150 的三次分母整除。证明把同一个真实 Brandt 周期的 $T_2$ 作用准确写成导子 $c$、$2c$ 的周期，处理二处的分裂、惰性、分歧、导子二部及单位权；再用同取向混合 CM 嵌入的奇偶性排除支撑相交。

一般 $p$ 的 $M<4p/7$ 范围内，第二特征值恒定只能出现在明确的剩余分支：$2\nmid c$、$2$ 在 $K$ 分裂、$\eta(\mathfrak q)\ne1$，且该恒值为零。当 $p\equiv2\pmod3$ 时，本文再用二同源图连通性及超奇异 $j=0$ 的准确加权邻域，排除一切坐标为零或三次单位根的 $T_2$ 特征向量。这把实际结论扩到整个 $M<p$，而不仅是前述混合碰撞范围。不证明一般三色共同理想为单位，也未完成主问题。

## 1. 设定及结论

沿用 R153 的记号。设 $p>37$，$K$ 为虚二次域，$p$ 在 $K$ 惰性；$\eta$ 为精确导子 $c$、阶恰为三的原始环类字符。置
$$
\mathcal O_c=\mathbb Z+c\mathcal O_K,\qquad
M=|D_K|c^2,\qquad p\nmid M.
\tag{156.1}
$$
固定 $K\hookrightarrow B_{p,\infty}$、极大序 $R$ 且 $R\cap K=\mathcal O_c$。在除子 Brandt 模 $\mathscr X=\mathbb Z[\mathrm{Cls}(R)]$ 中定义
$$
P_c=P_\eta=\sum_{[\mathfrak a]\in\operatorname{Pic}(\mathcal O_c)}
\eta(\mathfrak a)^{-1}[\mathfrak aR].
\tag{156.2}
$$
令 $\mathcal F_\eta$ 为所有满足 $L(1/2,\pi_{f,K}\otimes\eta)\ne0$ 的水平 $p$、权二、平凡 nebentype 归一化新形式，仍按复特征形式计数。

**定理 156.1。**

1. 若 $M<p/2$，则 $P_c\ne0$，且 $a_2(f)$ 在 $\mathcal F_\eta$ 上不恒定。
2. 若 $M<4p/7$，而 $a_2(f)$ 在 $\mathcal F_\eta$ 上恒定，则必有
   $$
   \boxed{2\nmid c,\quad 2\mathcal O_K=\mathfrak q\bar{\mathfrak q},
   \quad\eta(\mathfrak q)\ne1,\quad a_2(f)=0\text{ 对全部 }f\in\mathcal F_\eta.}
   \tag{156.3}
   $$
   此时 $P_c\ne0$ 仍自动成立。
3. 若 $p\equiv2\pmod3$ 且 $M<p$，则 $a_2(f)$ 在 $\mathcal F_\eta$ 上不恒定。这个结论包含第 2 项实际剩余分支的排除，并进一步放宽判别式范围。

这里 $\eta(\mathfrak q)$ 指 $\mathfrak q$ 收缩到 $\mathcal O_c$ 的可逆理想类值，因 $2\nmid c$ 定义无歧义。

**实际推论 156.2。** 若上述数据来自 R66 的真实小惯性完整非分裂正规化子分支，则已有 $p\equiv2\pmod3$。当 $M<p$ 时，对实际 $F[p]\simeq E[p]$，记
$$\operatorname{den}j(F)=D_F^p,$$
有
$$
\boxed{D_F^3\mid N(J_p),}
\qquad
\boxed{\log\operatorname{den}j(F)
\le\frac{p(p-1)}{12}
\log\left(\frac{2p}{9}-\frac4{9(p-1)}\right).}
\tag{156.4}
$$
$J_p$ 为 R137 的实圆分三色共同理想。这个推论不在全中心值零的未知范围使用 R150。

## 2. 谱恒定等价于真实周期的 Hecke 方程

R76 §6 及 R153 §2 给完整有理、自伴 Brandt 谱分解和精确中心值判据
$$
\mathscr X^0\otimes\mathbb C=\bigoplus_fV_f,
\qquad
e_fP_c\ne0\Longleftrightarrow f\in\mathcal F_\eta.
\tag{156.5}
$$
所以在 $P_c\ne0$ 时，
$$
a_2(f)=a\ \text{对全部 }f\in\mathcal F_\eta
\quad\Longleftrightarrow\quad T_2P_c=aP_c.
\tag{156.6}
$$
这使用所有非零投影，而不是先挑选一个有理形式。R153 已证明这个集合 Galois 稳定；若共同值 $a$ 存在，它是有理代数整数，故 $a\in\mathbb Z$。Ramanujan 界 $|a_2(f)|\le2\sqrt2$ 进一步给
$$a\in\{-2,-1,0,1,2\}.\tag{156.7}$$
所需的已发表主来源为 Deligne (1974), Theorem (8.2)，印刷 p. 302。主范围 $M<p/2$ 的排除其实只用 (156.6)，无需 (156.7)；(156.7) 仅在更宽范围排除 $a=3$。

## 3. 二处的格及所有二同源方向

令 $n=v_2(c)$，局部记
$$\mathcal O_n=\mathbb Z_2+2^n\mathcal O_{K,2}.$$
在 $B_2\simeq M_2(\mathbb Q_2)$ 中，将二维空间识别为 $K_2$。R83 §3.2 的局部格分类表明，乘子环为 $\mathcal O_n$ 的格在 $K_2^\times$ 缩放后可取 $\Lambda_n=\mathcal O_n$。

$T_2$ 在除子 Brandt 模上的作用是对每个源理想类，计数该格的三个指数二子格；目标理想类即二同源目标。若不同子格给同一目标类，保留其重数。

### 3.1 二不整除导子

若 $n=0$，三个子格对应 $\mathcal O_{K,2}/2\mathcal O_{K,2}$ 的三条 $\mathbb F_2$ 直线。

| $2$ 在 $K$ 中的类型 | 乘子环仍为 $\mathcal O_0$ 的方向 | 乘子环为 $\mathcal O_1$ 的方向 |
|---|---:|---:|
| 分裂 | $2$ | $1$ |
| 惰性 | $0$ | $3$ |
| 分歧 | $1$ | $2$ |

证明可直接在三个剩余代数中检验。分裂时两个坐标轴稳定；惰性时 $\mathbb F_4$ 没有一维 $\mathbb F_2$ 理想；分歧时 $\mathbb F_2[\epsilon]/(\epsilon^2)$ 只有一条稳定理想直线。稳定方向是对应的范数二 $\mathcal O_K$ 理想，其余方向的乘子环恰为 $\mathcal O_1$。

### 3.2 二整除导子

若 $n\ge1$，以 $1,2^n\theta$ 为 $\Lambda_n$ 的基，其中 $1,\theta$ 为 $\mathcal O_{K,2}$ 的整基。三个指数二子格中，一个为
$$2\mathbb Z_2+2^n\mathbb Z_2\theta=2\mathcal O_{n-1},$$
其乘子环为 $\mathcal O_{n-1}$；另外两个在 $K_2^\times$ 缩放后乘子环为 $\mathcal O_{n+1}$。后者的代表可取
$$
\mathbb Z_2+2^{n+1}\mathbb Z_2\theta,
\qquad
\mathbb Z_2(1+2^n\theta)+2^{n+1}\mathbb Z_2\theta.
$$
因此每个源有唯一上行方向和两个下行方向。这一分类也包含二分歧及二分裂的局部代数，不依赖三次角色。

## 4. 原始三次角色的二部及单位指数

$\eta$ 阶三迫 $h(\mathcal O_c)\ge3$，故 $\mathcal O_c^\times=\{\pm1\}$；有额外单位的两个最大序类数均为一。下一级 $\mathcal O_{2c}$ 的单位也为 $\{\pm1\}$。

环类映射
$$\pi_+:\operatorname{Pic}(\mathcal O_{2c})\twoheadrightarrow\operatorname{Pic}(\mathcal O_c)$$
的核，由二处单位商给出，阶数为
$$
e=\frac{h(\mathcal O_{2c})}{h(\mathcal O_c)}
=\begin{cases}
2-\chi_K(2),&2\nmid c,\\
2,&2\mid c.
\end{cases}
\tag{156.8}
$$
这里 $\chi_K(2)\in\{1,-1,0\}$ 分别对应分裂、惰性、分歧。源、目标单位指数均为一，故 (156.8) 没有漏掉单位分母。

若 $n=v_2(c)\ge1$，也有上行环类映射 $\pi_-:\operatorname{Pic}(\mathcal O_c)\to\operatorname{Pic}(\mathcal O_{c/2})$。精确导子为 $c$ 意味着 $\eta$ 在 $\ker\pi_-$ 上非平凡。

若 $n\ge2$，此核为二群，阶三角色必平凡，矛盾。若 $n=1$，其阶数为
$$
\frac{2-\chi_K(2)}{[\mathcal O_{c/2}^\times:\mathcal O_c^\times]}.
$$
所以原始三次角色而 $2\mid c$ 时，必有
$$
\boxed{v_2(c)=1,\quad\chi_K(2)=-1,
\quad[\mathcal O_{c/2}^\times:\mathcal O_c^\times]=1,}
\tag{156.9}
$$
且 $\ker\pi_-$ 的阶恰为三。特别 $K=\mathbb Q(\sqrt{-3}),c=2$ 的单位指数三例外不产生原始三次角色，不能当作一个额外分支。

## 5. 同一个 Brandt 模中的精确周期关系

先选一个基准下行二邻居 $J$，作为局部主右 $R$ 理想，使 $J_q=R_q$ 对 $q\ne2$，特别 $J_p=R_p$。其左序 $R'=\mathcal O_L(J)$ 满足 $R'\cap K=\mathcal O_{2c}$。令
$$
\eta_+=\eta\circ\pi_+,
\qquad
P_{2c}=\sum_{[\mathfrak b]\in\operatorname{Pic}(\mathcal O_{2c})}
\eta_+(\mathfrak b)^{-1}[\mathfrak bJ]\in\mathscr X^0\otimes\mathbb Q(\zeta_3).
\tag{156.10}
$$
这里 $\eta_+$ 仍阶三，但不声称它在导子 $2c$ 原始。使用 $(R',R)$ 双模 $J$ 的 Morita 对应，它就是通常 $R'$ 的真实环类周期，输运到当前同一个 Brandt 模中。

下行二邻居对的集合，即“一个 $\mathcal O_c$ 类加一个下行方向”，与 $\operatorname{Pic}(\mathcal O_{2c})$ 双射。具体而言，局部单位商 $\mathcal O_{c,2}^\times/\mathcal O_{2c,2}^\times$ 在下行方向上单纯传递；其阶为 (156.8) 的 $e$。用局部主理想和 CRT 将其拼成全局环类映射的各个纤维，即得双射。权重恰为 $\eta(\pi_+\mathfrak b)^{-1}$，没有另乘任意三次相位。

这也解释了单位权：Brandt 除子算子按三个实际子格计数，源 CM 序的单位 $\pm1$ 保持全部子格。目标超奇异曲线即使有额外自同构，只会使若干子格在同一个目标坐标合并，重数仍保留。$|\operatorname{Aut}|/2$ 出现在自伴配对中，不在 (156.10) 或以下邻居计数中另除一次。

若 $2\nmid c$，水平邻居分别由范数二的可逆 $\mathcal O_c$ 理想相乘。对一个这样的 $\mathfrak q$，换元 $\mathfrak a\mathfrak q=\mathfrak d$ 给
$$
\sum_{[\mathfrak a]}\eta(\mathfrak a)^{-1}[\mathfrak a\mathfrak qR]
=\eta(\mathfrak q)P_c.
$$
分歧时 $\mathfrak q^2=(2)$，而 $\eta$ 阶三，所以 $\eta(\mathfrak q)=1$。由 §3 的全方向分类，
$$
\boxed{T_2P_c=P_{2c}+b_2P_c,}
\tag{156.11}
$$
其中
$$
b_2=
\begin{cases}
\eta(\mathfrak q)+\eta(\mathfrak q)^{-1}\in\{2,-1\},
&2\nmid c,\ 2\text{ 分裂},\\
0,&2\nmid c,\ 2\text{ 惰性},\\
1,&2\nmid c,\ 2\text{ 分歧},\\
0,&2\mid c.
\end{cases}
\tag{156.12}
$$
最后一行中，上行目标只依赖 $\pi_-([\mathfrak a])$；按每个上行环类纤维求和，其权重为一个三次角色在核上的总和，因原始性而等于零。因此上行项确实消失；不是将它忽略，也不以形式上的“坏 Euler 因子”替代真实方向计数。

## 6. 不同导子的同取向混合碰撞必须满足 $M\ge p/2$

设一个 $\mathcal O_c$ 类和一个 $\mathcal O_{2c}$ 类在 (156.2)、(156.10) 中落到同一个右 $R$ 理想类。用 R76 §2 的输运，将相应最优嵌入放到同一左极大序 $S$。

由于两类代表都可在 $p$ 处规范为单位理想，且 $J_p=R_p$，输运元在 $p$ 为单位。因此两个嵌入的 $K_p$ 剩余取向一致，不能单独翻转其中之一。

写
$$
\mathcal O_c=\mathbb Z[\omega],\qquad
\omega=(t+\sqrt{-M})/2,
\qquad t\in\{0,1\}.
$$
则 $\mathcal O_{2c}=\mathbb Z[\sqrt{-M}]$。令
$$
\alpha=2\iota_c(\omega)-t,
\qquad
\beta=\iota_{2c}(\sqrt{-M}).
$$
两者都是 $S$ 中的纯元素，范数同为 $M$。共同取向给
$$\beta-\alpha\in\mathfrak P,$$
其中 $\mathfrak P$ 为 $S$ 的 $p$ 两边素理想。

二者不相等：若相等，两个 $K$ 嵌入相同；该分数域与 $S$ 的交已包含 $\mathcal O_c$，就不可能同时恰为真子序 $\mathcal O_{2c}$，与第二嵌入最优性矛盾。

因此
$$0<N(\beta-\alpha)\in p\mathbb Z.$$
又因纯部的范数恒等式，
$$
N(\beta-\alpha)=2M+\operatorname{Tr}(\alpha\beta)
=2M+2\operatorname{Tr}(\iota_c(\omega)\beta),
$$
其中用了 $\operatorname{Tr}\beta=0$。所以该正整数还是偶数。两点都在平方半径 $M$ 的球面上，故
$$
\boxed{0<N(\beta-\alpha)\in2p\mathbb Z,
\qquad N(\beta-\alpha)\le4M.}
\tag{156.13}
$$
由此混合碰撞必有 $M\ge p/2$。于是
$$
\boxed{M<p/2\Longrightarrow
\operatorname{im}\varphi_c\cap\operatorname{im}\varphi_{2c}=\varnothing.}
\tag{156.14}
$$
这里的奇偶性使用 $\alpha=2\omega-t$，是比一般不同序碰撞的粗范数界多出的信息。

## 7. 主范围内排除 $T_2$ 单一特征值

在 $M<p/2$ 时，$\varphi_c$ 单射，故 $P_c\ne0$。同时 $\mathcal O_{2c}$ 的判别式绝对值为 $4M<2p<16p/7$。R76 定理 76.1 只要求序和共同取向，不要求角色原始，因此它同样适用于 $\varphi_{2c}$：每个纤维至多两个类。

一项或两项三次单位根的和不为零。因此 $P_{2c}$ 的非零坐标恰为全部非空纤维，特别
$$P_{2c}\ne0.\tag{156.15}$$
若 $T_2P_c=aP_c$，则 (156.11) 给
$$P_{2c}=(a-b_2)P_c.$$
但右侧支撑包含于 $\operatorname{im}\varphi_c$，左侧非零且由 (156.14) 支撑与它不交，矛盾。结合 (156.6)，定理 156.1 第 1 项得证。

## 8. $M<4p/7$ 时的全部剩余分支

先证明一个混合三点界。设同一 Brandt 类包含一个 $\mathcal O_c$ 类及两个不同的 $\mathcal O_{2c}$ 类，且 $M<4p/7$。如 §6 在同一 $S$ 中取纯元素 $\alpha,\beta_1,\beta_2$，各自范数 $M$，取向一致。

两个混合边由 (156.13) 为正的 $2p$ 倍数，又不超过 $4M<16p/7$，故
$$N(\beta_1-\alpha)=N(\beta_2-\alpha)=2p.$$
两个不同 $\mathcal O_{2c}$ 类的嵌入不被 $S^\times$ 共轭，特别元素不同；第三边为正的 $p$ 倍数且小于 $16p/7$。所以三边长平方只可能是
$$ (2p,2p,p)\quad\text{或}\quad(2p,2p,2p).$$
三个不同球面点不共线。若边长平方为 $kp,lp,mp$，Heron 公式给外接圆平方半径
$$
R_{\rm circ}^2=\frac{klm\,p}{4kl-(k+l-m)^2}.
$$
上面两型分别为 $4p/7$ 和 $2p/3$。三个点所在平面与原球的交圆半径不大于原球半径 $\sqrt M$，与 $M<4p/7$ 矛盾。因此
$$
\boxed{\text{在 }M<4p/7\text{ 时，每个被 }\varphi_c\text{ 占用的类，
至多承载一个 }\varphi_{2c}\text{ 类}.}
\tag{156.16}
$$

现在假定第二谱恒值为 $a$。因 $M<p$，$\varphi_c$ 单射且 $P_c\ne0$；因 $4M<16p/7$，$\varphi_{2c}$ 每纤维至多二，所以 (156.15) 仍成立。由
$$P_{2c}=(a-b_2)P_c$$
可知 $a-b_2\ne0$，两个周期支撑相同，并且每个 $\varphi_c$ 类都被 $\varphi_{2c}$ 占用。由 (156.16)，每个这样的类恰承载一个 $\mathcal O_{2c}$ 类，故
$$h(\mathcal O_{2c})=h(\mathcal O_c).$$
(156.8) 迫 $2\nmid c$ 且二分裂。

现在每个非零坐标的 $P_c$、$P_{2c}$ 都是单个三次单位根，其比值属于 $\mu_3$；但这个比值是整数 $a-b_2$。所以
$$a-b_2=1.$$
若 $\eta(\mathfrak q)=1$，则 $b_2=2$、$a=3$，与 (156.7) 矛盾。否则 $b_2=-1$，得到 $a=0$。这恰为 (156.3)，定理第 2 项得证。

这个最后分支有严格的颜色含义：导子 $2c$ 的唯一下降类，在每个被占用的 Brandt 坐标上，与导子 $c$ 的唯一类颜色相同。它本身不是一般 Picard 作用可下降的证明。下一节使用完整二同源作用，而非只使用这个颜色相合，排除实际的 $p\equiv2\pmod3$ 分支。

### 8.1 实际 $p\equiv2\pmod3$ 时，闭合支撑与 $j=0$ 给矛盾

继续反设 (156.3) 成立，记
$$S_c=\operatorname{im}\varphi_c=\operatorname{im}\varphi_{2c}.$$
这是 $P_c$ 的非零支撑，而且两个映射均单射。因二分裂且不整除导子，每个源 $\mathcal O_c$ 类的全部三个二邻居由两个水平邻居和唯一的下行邻居组成。水平邻居仍来自 $\operatorname{Pic}(\mathcal O_c)$，所以下行邻居以外的两个目标在 $S_c$ 内；下行目标也在 $\operatorname{im}\varphi_{2c}=S_c$ 内。因此 $S_c$ 对完整 $T_2$ 邻居作用闭合。

这里需要图连通性，可从已经使用的完整谱直接证明。标准配对满足
$$\langle[x],[y]\rangle=w_x\delta_{x,y},\qquad w_x>0.$$
每个基向量的 $T_2$ 像的系数总和为三，因此表示次数泛函的正向量
$$\mathcal E=\sum_xw_x^{-1}[x]$$
满足 $T_2\mathcal E=3\mathcal E$。自伴性使邻接关系双向：若 $y$ 是 $x$ 的邻居，则 $x$ 也是 $y$ 的邻居。若图有两个或更多连通分量，将 $\mathcal E$ 限制在各分量，便得到两个或更多独立的特征值三向量。但整个 Brandt 模除了唯一 Eisenstein 线外就是 (156.5) 的尖点谱；Deligne 界使其全部 $T_2$ 特征值绝对值至多 $2\sqrt2<3$，矛盾。因此二同源图连通，非空闭合子集只能是全部右理想类：
$$S_c=\mathrm{Cls}(R).\tag{156.17}$$
这一步没有遗漏自同构权，也没有把“存在一条相邻路径”当作未经证明的输入。

若 $p\equiv2\pmod3$，曲线
$$E_0/\mathbb F_p:\ y^2=x^3+1$$
超奇异。确实，立方映射在 $\mathbb F_p$ 上为双射，故点数的二次角色和为零、$a_p(E_0)=0$。因此 $j=0$ 给一个实际 Brandt 类 $x_0$。

几何自同构 $(x,y)\mapsto(\zeta_3x,y)$ 在三个非零二挠点上作三循环，所以三个阶二子群的商椭圆曲线两两同构。存在一个 Brandt 类 $y_0$，使
$$T_2[x_0]=3[y_0].\tag{156.18}$$
它可以与 $x_0$ 相同；这不影响论证。现在 (156.3) 给 $T_2P_c=0$，而自伴性给
$$
0=\langle T_2P_c,[x_0]\rangle
=\langle P_c,T_2[x_0]\rangle
=3w_{y_0}(P_c)_{y_0}.
$$
由于特征零且 $w_{y_0}>0$，得到 $(P_c)_{y_0}=0$，与 (156.17) 的满支撑矛盾。这先排除了实际 $M<4p/7$ 的剩余分支。

最后这个排除适用于全部满足条件的素数，不需要任何水平扫描或小类数表。一般 $p\equiv1\pmod3$ 时本文保留 (156.3) 的分类，不将 $j=0$ 擅自视为超奇异。

### 8.2 三次单位根坐标不能组成特征向量：扩大到整个 $M<p$

下面证明一个独立的加权图引理，它不要求导子 $2c$ 的周期无零坐标。

**引理 156.3。** 设 $p>37$ 且 $p\equiv2\pmod3$。在标准除子 Brandt 基中，不存在非零 $T_2$ 特征向量
$$v=\sum_xv_x[x],\qquad v_x\in\{0,1,\zeta_3,\zeta_3^2\}.$$

**证明。** 假设 $T_2v=av$。自伴性使 $a$ 为实数。记非零支撑为 $S$。

先考察一个 $v_x=0$ 而邻接 $S$ 的顶点。将 $T_2[x]$ 按三个实际二子群列为 $[y_1]+[y_2]+[y_3]$，允许目标重合。自伴性给
$$
0=\langle T_2v,[x]\rangle
=\sum_{j=1}^3w_{y_j}v_{y_j}.
\tag{156.19}
$$
至少一项非零。若至多两项非零，正实数倍的两个三次单位根不能相消。故三项均非零。将三种颜色的总权重记为 $A_0,A_1,A_2\ge0$；$A_0+A_1\zeta_3+A_2\zeta_3^2=0$ 迫 $A_0=A_1=A_2>0$。这里只有三个邻居槽位，所以恰是三种不同颜色各一次，而且三个权重相等。

因此每个零坐标而邻接 $S$ 的顶点，其全部邻居都在 $S$。于是 $S\cup N(S)$ 对邻居作用闭合；其中 $N(S)$ 只指支撑外但邻接支撑的顶点。由 §8.1 已完整证明的图连通性，$S\cup N(S)$ 为全部顶点。特别，每个零坐标顶点都必须邻接 $S$。

令 $x_0$ 是超奇异 $j=0$ 类。仍有 $T_2[x_0]=3[y_0]$。若 $v_{x_0}=0$，则自伴性迫 $v_{y_0}=0$，而 $x_0$ 的全部邻居都是这个零坐标顶点，违反上一段。因此
$$v_{x_0}\ne0.\tag{156.20}$$

还需要准确识别邻居的单位权。对 $y^2=x^3+1$ 选择二挠点 $(-1,0)$，平移 $u=x+1$ 得
$$y^2=u^3-3u^2+3u.$$
其二同源商可写成
$$Y^2=X^3+6X^2-3X,$$
由二同源公式 $X=y^2/u^2$、$Y=y(1-3/u^2)$ 可直接检验。这个商的 $j$ 值为 $54000$。另外两个子群由三阶自同构相连，故商同构。所以
$$j(y_0)=54000\pmod p.$$
因为
$$54000=2^4\cdot3^3\cdot5^3,
\qquad54000-1728=2^4\cdot3^3\cdot11^2,$$
在 $p>37$ 时 $y_0$ 既不是 $j=0$ 也不是 $j=1728$，故
$$w_{x_0}=3,\qquad w_{y_0}=1.\tag{156.21}$$

若 $a=0$，$x_0$ 方程迫 $v_{y_0}=0$。但 $y_0$ 邻接非零的 $x_0$，由 (156.19) 的结论，它的三个邻居应有相同权重三且颜色各异。几何超奇异类中权重三的顶点只有 $j=0$ 一个，不可能具有三个不同颜色。因此 $a\ne0$。

现在 $x_0$ 方程及 (156.21) 给
$$a v_{x_0}=v_{y_0}.$$
两边非零坐标都是三次单位根，且 $a$ 实，所以
$$a=1,\qquad v_{y_0}=v_{x_0}.\tag{156.22}$$

自伴性和 (156.21) 还表明 $[x_0]$ 在 $T_2[y_0]$ 中的重数准确为一：它乘 $w_{x_0}$ 等于 $T_2[x_0]$ 中 $[y_0]$ 的重数三乘 $w_{y_0}$。故可写
$$T_2[y_0]=[x_0]+[z_1]+[z_2],$$
其中 $z_1,z_2$ 允许重合。将 (156.22) 代入 $y_0$ 的特征方程，得到
$$
w_{z_1}v_{z_1}+w_{z_2}v_{z_2}=-2v_{x_0}.
\tag{156.23}
$$
两个左项都必须非零。除以 $v_{x_0}$，正整数权重乘三次单位根之和等于负实数 $-2$，唯一可能是两个颜色分别为 $\zeta_3,\zeta_3^2$，两个权重均为二。但权重二的几何类至多只有 $j=1728$ 一个；若两个槽位指向它，颜色也相同，不可能分别为两个颜色。矛盾，证明引理。

最后，$M<p$ 时 R76 的同取向差范数使 $\varphi_c$ 单射；所以 $P_c$ 非零，并且每个坐标正好为零或一个三次单位根。引理 156.3 证明它不是 $T_2$ 特征向量。由 (156.6)，这完成定理 156.1 第 3 项的整个 $M<p$ 范围。

这一加强使用唯一权重三顶点及唯一权重二顶点的实际邻域，不能把配对换成无权图后照搬。它不假定 $P_{2c}$ 单射，也没有用尚未证明的环类作用全局下降。

## 9. 实际商、共同原始根与三次分母整除

定理范围内 $P_c\ne0$ 已由几何直接证明。R76 的已发表中心值公式给非零谱，R153 的有理 Hecke 论证给完整 Galois 稳定性。在实际 R66 数据下，R69、R72 于是给同一扭曲曲线的真实最优秩零商及饱和整微分格。

定理保证该完整非零谱上 $a_2$ 不恒定时，R150 使用两个实际微分消去第二项，并在同一尖点、同一原始圆分根及同一实际素理想处比较积分；得到 $D_F^3\mid N(J_p)$。没有任意更换谱线后重新选择点或尖点。R137 的 Parseval 界再给 (156.4)。

这新增的是“何时可无须额外 Fourier 系数条件使用 R150 的三次加强”。它不是 $M$ 的上界，不处理 $M$ 超出范围时的谱恒定问题，也没有把共同中心值为零的缺口消去。

## 10. 参考接口

- R76 §§2–3、定理 76.1、§6：真实右理想类、同 $p$ 取向、最优嵌入及每纤维至多二；已发表 Cai–Shu–Tian Theorem 1.2 的中心值接口。
- R83 §3.2：二次局部格在乘子序固定后的 $K_2^\times$ 轨道分类。
- R153 §§2、7：有理 Brandt 谱及 Galois 稳定性；环类 exact sequence、二次序单位指数。本文 §§3–5 自含给出全部二邻居与角色权重。
- P. Deligne, *La conjecture de Weil : I*, Publications mathématiques de l'IHÉS **43** (1974), pp. 273–307，Theorem (8.2)，p. 302：[原刊 PDF](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf)。仅用 $|a_2(f)|\le2\sqrt2$，其余碰撞和周期关系均在正文证明。
- R69、R72、R137、R150：实际秩零商、饱和整微分格、共同圆分根及三次分母整除。

