# R8：二生成元模型的拟幂零线性组合、单射稠密值域与支集不变性的排除

日期：2026-11-12（北京时间）。分工：`literature_audit`。

**状态：已证明的中间结论。** §2—§7 是对明确系数模型的完整初等证明；不使用外部论文中尚待本仓库核验的纤维不变格分类或超不变子空间主定理。§8 的标量加权 odometer 是一个已证的充分性约化，不是其不变子空间存在定理。依赖的是 §1 中重新写出的模型定义；后续所需的正性、可测性、归一化有限性与估计全部在本文件证明。

## 1. 模型、来源与记号

来源：OpenAI, *Backward intertwiners and a transitive commutant*, 2026-09-27，[固定原文目录](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026)，特别是 §3、§4 中的系数定义。以下重新给出后续所需的定义与估计。

令 $X=\mathbb Z_2$，$\mu$ 为 Haar 概率，$\theta x=x+1$，

$$
H=L^2(X,\mu;\ell^2(\mathbb Z)).
$$

设 $N_m=2^m$、$T_m(x)=x\bmod N_m\in\{0,\ldots,N_m-1\}$，$c=10,D=100$。取 $\ell_0=1$、$\ell_m=8^m$，$I_m=\{k:\ell_{m-1}\le k<\ell_m\}$，$J_m=D(N_m-2)$。定义

$$
a_0^+=a_0^-=c,
\qquad
a_k^+(x)=c(k+1)+J_m+DT_m(x),\quad k\in I_m,
$$

$$
a_k^-(x)=c(k+1)+J_m+D(N_m-1-T_m(x)),\quad k\in I_m.
$$

再令 $a_j=a_j^+$（$j\ge0$），$a_j=a_{-j-1}^-$（$j<0$），$\beta_j=e^{-a_j}$。后向系数由

$$
\widetilde b_0(x)=1,
\qquad
\widetilde b_{j+1}(x)
=\widetilde b_j(x)\frac{\beta_{j-1}(x+1)}{\beta_j(x)}
\tag{1.1}
$$

定义。令 $L(x)=\sup_j\widetilde b_j(x)$，在 $L(x)<\infty$ 的不变满测集上置 $b_j=\widetilde b_j/L$，在其零测补集上置零。算子为

$$
(Sf)(x,j)=\beta_{j-1}(x)f(x,j-1),
\qquad
(Vf)(x,j)=b_{j+1}(x-1)f(x-1,j+1).
\tag{1.2}
$$

后文记 $T_\lambda=S+\lambda V$。

## 2. 后向系数合法性与偶基底上的统一估计

### 2.1 权函数的双边估计

若 $k\in I_m$，则 $N_m\le2k^{1/3}$，从定义立即得到

$$
0\le a_k^\pm(x)-c(k+1)\le4Dk^{1/3}\qquad(k\ge1).
\tag{2.1}
$$

因此 $0<\beta_j\le e^{-c}$，并且对所有整数 $j$，

$$
\beta_j(x)\ge
\exp\{-10(|j|+1)-400(|j|+1)^{1/3}\}.
\tag{2.2}
$$

每个固定 $j$ 的 $\beta_j$ 只取有限个正值。

### 2.2 $L(x)$ 几乎处处有限

写 $\Delta a_j(x)=a_j(x+1)-a_j(x)$。在块 $I_m$ 上，

$$
\Delta a_k^+(x)=D-DN_m\mathbf1_{\{T_m=N_m-1\}}(x),
\qquad \Delta a_k^-(x)=-\Delta a_k^+(x).
$$

由于 $\sum_m\mu\{T_m=N_m-1\}=\sum_m2^{-m}<\infty$，Borel–Cantelli 保证几乎处处只有有限个例外块。与全部整数平移后的满测集相交，取到不变满测集 $X_*$。对 $x\in X_*$ 可取有限常数

$$
C(x)=D+D\sum_{m:T_m(x)=N_m-1}N_m|I_m|.
$$

于是

$$
\sum_{k=0}^{n-1}\Delta a_k(x)\ge Dn-C(x),
\qquad
\sum_{k=-q}^{-1}\Delta a_k(x)\le-Dq+C(x).
$$

对 (1.1) 分别向正负方向求和给出

$$
\log\widetilde b_n
=-\sum_{k=0}^{n-1}\Delta a_k+a_{n-1}(x+1)-c,
$$

$$
\log\widetilde b_{-q}
=\sum_{k=-q}^{-1}\Delta a_k+a_{-q-1}(x+1)-c.
$$

结合 (2.1)，得

$$
\log\widetilde b_n\le-90n+C(x)-10+400(n-1)^{1/3},
\tag{2.3}
$$

$$
\log\widetilde b_{-q}\le-90q+C(x)+400q^{1/3}.
\tag{2.4}
$$

两端都趋于负无穷，因此 $1\le L(x)<\infty$，$0<b_j(x)\le1$，且各 $b_j$ 可测。共同归一化不改变 (1.1)。这证明了 (1.2) 定义有界算子，且 $\|V\|\le1$。

### 2.3 偶基底估计

**引理。** 若 $x\in X_*$ 为偶的 $2$-进整数，则对所有 $j\in\mathbb Z$，

$$
\log b_j(x)\le600-40|j|.
\tag{2.5}
$$

**证明。** 偶数 $x$ 不属于任何例外块，故上面的 $C(x)$ 可取 $D=100$。又 $L\ge1$，所以 $\log b_j\le\log\widetilde b_j$。标量不等式

$$
400t^{1/3}\le50t+500\qquad(t\ge0)
$$

可令 $u=t^{1/3}$ 后计算 $400u-50u^3$ 的最大值得到，该最大值小于 $500$。代入 (2.3)—(2.4)，正指数得到 $\log b_n\le-40n+540$，负指数得到 $\log b_{-q}\le-40q+600$；$j=0$ 由 $b_0\le1$ 直接成立。证毕。

## 3. $V$ 也范数拟幂零；所有 $T_\lambda$ 范数拟幂零

**命题。** 令 $m=\lfloor n/2\rfloor$，则

$$
\|V^n\|\le
\min\left(1,\exp\{600m-40\lfloor m^2/2\rfloor\}\right).
\tag{3.1}
$$

特别地 $\|V^n\|^{1/n}\to0$。

**证明。** 从输入坐标 $(x,j)$ 出发，$V^n$ 的唯一输出为 $(x+n,j-n)$，系数是

$$
\prod_{r=0}^{n-1}b_{j-r}(x+r).
$$

其中至少 $m$ 个基底 $x+r$ 为偶数；选取恰好 $m$ 个，其指标 $j-r$ 构成公差 $2$ 的整数等差数列。任意 $m$ 个公差 $2$ 的整数的绝对值之和至少 $\lfloor m^2/2\rfloor$：中心尽量靠近零时取得最小值，偶数项数为 $m^2/2$，奇数项数为 $(m^2-1)/2$。对这些因子使用 (2.5)，其余因子使用 $b\le1$，得到 (3.1)。变换 $(x,j)\mapsto(x+n,j-n)$ 保持底测度，故同一估计给算子范数界。证毕。

$S$ 的拟幂零性也只需系数下界。定义 $d(j)=j+1$（$j\ge0$），$d(j)=-j$（$j<0$）。有 $a_j\ge10d(j)$，而

$$
\min_{j\in\mathbb Z}\sum_{r=0}^{n-1}d(j+r)
=\left\lfloor\frac{(n+1)^2}{4}\right\rfloor.
$$

于是

$$
\|S^n\|\le
\exp\left\{-10\left\lfloor\frac{(n+1)^2}{4}\right\rfloor\right\}.
\tag{3.2}
$$

归一化递推给出 $b_j(x)\beta_{j-1}(x+1)=\beta_j(x)b_{j+1}(x)$，逐坐标计算即得 $SV=VS$。

任给 $\varepsilon>0$，(3.1)—(3.2) 保证有有限 $C_\varepsilon\ge1$，使

$$
\|S^k\|,\|V^k\|\le C_\varepsilon\varepsilon^k\qquad(k\ge0).
$$

利用二项式展开及交换性，

$$
\|T_\lambda^n\|
\le C_\varepsilon^2\varepsilon^n(1+|\lambda|)^n.
$$

先取 $n$ 次根，再令 $n\to\infty$、$\varepsilon\to0$，得 $r(T_\lambda)=0$，即每个线性组合 $S+\lambda V$ 都范数拟幂零。

还可保留显式高斯界。由 (3.2) 有 $\|S^k\|\le e^{-(5/2)k^2}$。在 (3.1) 中用 $m\ge(l-1)/2$、$m\le l/2$，得对所有 $l\ge0$，

$$
\|V^l\|\le e^{-5l^2+310l+35}.
$$

二项式展开后，利用

$$
\frac52k^2+5(n-k)^2\ge\frac53n^2,
$$

得到

$$
\boxed{\displaystyle
\|T_\lambda^n\|\le
\exp\left\{-\frac53n^2+
\bigl(310+\log(1+|\lambda|)\bigr)n+35\right\}.}
\tag{3.3}
$$

因此 $\sum_{n\ge0}z^nT_\lambda^n=(I-zT_\lambda)^{-1}$ 是算子值整函数，且其范数最大值的对数为 $O_\lambda((\log r)^2)$。证明是把各项指数中的 $-\frac53n^2+n\log r+O_\lambda(n)$ 配方，再估计平移高斯级数。乘上固定向量泛函或额外因子 $z$ 后，所得非多项式标量整函数的增长阶仍为零。这个估计本身没有构造任何保持拟幂零的非零秩一扰动。

## 4. 每个 $T_\lambda$ 都单射

$\lambda=0$ 时由所有 $\beta_j>0$ 直接知道 $S$ 单射。以下设 $\lambda\ne0$。

若 $T_\lambda f=0$，对 $\epsilon\in\{0,1\}$ 设

$$
g_k(z)=f(z-k,2k+\epsilon),\qquad k\in\mathbb Z.
$$

Haar 平移保持测度，所以 Fubini 给出几乎每个 $z$ 满足 $(g_k(z))_{k\in\mathbb Z}\in\ell^2(\mathbb Z)$。在输出坐标 $(x,2k+\epsilon+1)$ 的零方程给

$$
g_{k+1}(z)=
-\frac{\beta_{2k+\epsilon}(z-k)}
{\lambda b_{2k+\epsilon+2}(z-k-1)}g_k(z).
\tag{4.1}
$$

可以去掉一个零测集，使所有整数 $k$ 的递推及正系数条件同时成立。

记 $\delta_k(z)=1$ 当 $z-k-1$ 为偶数，否则为零。$\delta_k$ 在 $k$ 中交替取零、一。对 $k\ge0$，由 (2.1)、$b\le1$ 和 (2.5)，(4.1) 中比值绝对值的对数至少为

$$
-|\log|\lambda||
-10(2k+\epsilon+1)-400(2k+\epsilon+1)^{1/3}
+\delta_k[40(2k+\epsilon+2)-600].
$$

任何交替零一序列满足

$$
\sum_{k=0}^{N-1}k\delta_k\ge \frac{N^2}{4}-\frac N2.
$$

因此，把前 $N$ 个比值相乘，得到统一于 $z,\epsilon$ 的下界

$$
\log\left|\frac{g_N(z)}{g_0(z)}\right|
\ge
10N^2-(650+|\log|\lambda||)N
-400N(2N+1)^{1/3},
\tag{4.2}
$$

这里在 $g_0\ne0$ 时书写比值；它等价于对乘法系数的估计，不需要预先除以零。右侧趋于正无穷。故若 $g_0(z)\ne0$，则 $g_N(z)$ 甚至不趋零，与 $\ell^2$ 性矛盾。所以 $g_0=0$ 几乎处处，再用正系数递推向两端延拓，得所有 $g_k=0$。对两种奇偶分别应用即得 $f=0$。

这完整证明每个 $T_\lambda$ 单射；并非仅仅有限截断没有核。

## 5. 共同的反射共轭与稠密值域

令 $\iota x=-x-1$。残数恒等式

$$
T_m(\iota x)=N_m-1-T_m(x)
$$

给出

$$
\beta_j(x)=\beta_{-j-1}(\iota x).
\tag{5.1}
$$

令 $\tau x=-x-2$。由两个中心权重都等于 $e^{-c}$ 知 $\widetilde b_1=1$。把 $c_j(x)=\widetilde b_{1-j}(\tau x)$ 代入 (1.1)，借助 (5.1) 可验证 $c_0=1$，且

$$
\frac{c_{j+1}(x)}{c_j(x)}
=\frac{\beta_{j-1}(x+1)}{\beta_j(x)}.
$$

递推唯一性给 $\widetilde b_j(x)=\widetilde b_{1-j}(\tau x)$，取上确界得 $L(x)=L(\tau x)$。于是归一化后几乎处处

$$
b_j(x)=b_{1-j}(-x-2).
\tag{5.2}
$$

定义线性酉对合

$$
(Uf)(x,j)=f(-x-1,-j).
$$

由 (5.1)—(5.2) 逐坐标计算得

$$
USU=S^*,\qquad UVU=V^*.
$$

设 $Jf=\overline f$ 为逐坐标复共轭。系数为实数，故 $J$ 与 $S,V,U$ 交换。反线性等距对合 $C=UJ$ 满足

$$
CT_\lambda C=T_\lambda^*.
\tag{5.3}
$$

所以 $\ker T_\lambda^*=C\ker T_\lambda=0$。由 Hilbert 空间恒等式 $\overline{\operatorname{ran}T_\lambda}=(\ker T_\lambda^*)^\perp$，每个 $T_\lambda$ 都有稠密值域。

又 $T_\lambda$ 非零且范数拟幂零，不能可逆。具体非零性：$T_\lambda(1\otimes e_0)$ 的 $e_1$ 坐标恒为 $e^{-c}$，不会被后向项抵消。结合单射和有界逆定理可知其值域为真稠密子空间。

## 6. $\lambda\ne0$ 时没有任何非平凡支集不变子空间

把 $H$ 看作 $L^2(X\times\mathbb Z,\mu\times\#)$。对可测集合 $E\subseteq X\times\mathbb Z$，令

$$
H_E=\{f:\ f=0\text{ a.e. on }E^c\}.
$$

**命题。** 若 $\lambda\ne0$ 且 $T_\lambda H_E\subseteq H_E$，则 $H_E=0$ 或 $H$。同样，$S,V$ 没有非平凡共同不变的这种子空间。

**证明。** 写 $E_j=\{x:(x,j)\in E\}$。测试只支集于第 $j$ 个坐标的向量，其 $S$ 和 $\lambda V$ 输出坐标分别为 $j+1,j-1$，故不能相互抵消。利用系数正性，$T_\lambda$ 不变性迫使

$$
E_j\subseteq E_{j+1},\qquad
\theta E_j\subseteq E_{j-1}
\quad\text{mod null sets}.
\tag{6.1}
$$

处理可数个指标后可同时取代表。由第一组包含关系，定义可测阈值 $h:X\to\mathbb Z\cup\{-\infty,+\infty\}$，使 $x\in E_j$ 当且仅当 $j\ge h(x)$；$-\infty$ 表示全坐标，$+\infty$ 表示空集。第二组包含关系给出

$$
h(\theta x)\le h(x),
\qquad
h(\theta x)\le h(x)-1\quad\text{若 }h(x)\in\mathbb Z.
$$

取严格递增的有界函数 $\varphi$ 定义在扩充整数集上，例如 $\varphi(t)=\frac12+\pi^{-1}\arctan t$，端点取 $0,1$。概率保持意味着 $\varphi(h\circ\theta)$ 与 $\varphi(h)$ 积分相等，而前者逐点不大于后者，所以二者几乎处处相等。严格递增性排除有限阈值。

因此阈值仅为正、负无穷，且相应两部分在 $\theta$ 下不变。最后，$\theta$ 遍历：若可测 $A$ 不变，$\theta$ 在模 $2^m$ 剩余类上传递，所以 $\mu(A\cap\{T_m=r\})=\mu(A)/2^m$；剩余类生成 Borel sigma 代数，单调类论证给 $\mu(A)=\mu(A)^2$。故只有空集或全空间。证毕。

这说明 $S+\lambda V$ 确实消除了 $S$ 原有的固定尾部，以及所有以可测支集描述的候选。然而一般闭线性子空间不必由支集描述；这一命题绝不能升级成完整 ISP 反例。

## 7. 其他直接结构

### 7.1 相位化归

令 $(D_t f)(x,j)=e^{itj}f(x,j)$。有 $D_tSD_t^{-1}=e^{it}S$，$D_tVD_t^{-1}=e^{-it}V$。对 $\lambda=|\lambda|e^{i\alpha}$，取 $t=\alpha/2$，得

$$
e^{-it}D_tT_\lambda D_t^{-1}=T_{|\lambda|}.
$$

所以研究非零参数的普通不变格只需研究 $\lambda>0$。

### 7.2 共同的加一坐标

$S$ 的支集移动 $(x,j)\mapsto(x,j+1)$ 与 $V$ 的支集移动 $(x,j)\mapsto(x+1,j-1)$ 都使

$$
w=2x+j\in\mathbb Z_2
$$

增加 $1$。因而对任意连续特征标 $\chi:\mathbb Z_2\to\mathbb T$，乘子 $G_\chi f(x,j)=\chi(2x+j)f(x,j)$ 满足

$$
G_\chi T_\lambda=\chi(1)T_\lambda G_\chi.
$$

该关系是协变关系，不是交换关系；不能将这些乘子当作保留所有 $T_\lambda$-不变子空间的算子。

### 7.3 非紧性

取 $L^2(X)$ 中任意无限正交单位序列 $\varphi_n$。$T_\lambda(\varphi_n\otimes e_0)$ 在第 $1$ 坐标的投影是 $e^{-c}\varphi_n\otimes e_1$，无范数收敛子列。因此所有 $T_\lambda$ 均非紧。

## 8. 一个标量加权 odometer 的不变格嵌入共同不变格

定义 $w_0(x)=1$，$w_{j+1}/w_j=\beta_j$。每个固定 $j$，$w_j$ 只取有限个正值，所以乘法算子 $D_j=M_{w_j}$ 在 $L^2(X)$ 上有界可逆。这里不主张 $D_j$ 的范数和逆范数对 $j$ 一致有界。

递推 (1.1) 等价于

$$
b_j(x)=e^{-c}b_0(x)\frac{w_{j-1}(x+1)}{w_j(x)}.
\tag{8.1}
$$

这由在 $j=0$ 验证（$w_{-1}=e^c$）并比较递推得到。令 $h(x)=e^{-c}b_0(x)>0$ 几乎处处，定义标量加权 odometer

$$
(Af)(x+1)=h(x)f(x).
\tag{8.2}
$$

设 $\iota_j:L^2(X)\to H$ 是第 $j$ 坐标嵌入。则

$$
S\iota_jD_j=\iota_{j+1}D_{j+1},
\qquad
V\iota_jD_j=\iota_{j-1}D_{j-1}A.
\tag{8.3}
$$

特别地 $SV$ 保持每个坐标空间，其第 $j$ 个限制与 $A$ 相似：

$$
(SV)|_{\iota_jL^2(X)}\simeq D_jAD_j^{-1}.
$$

$A$ 单射且值域稠密，由正权和基底变换可逆直接得到。它范数拟幂零，因为在第零坐标上它等于 $SV$ 的限制，且

$$
\|(SV)^n\|\le\|S^n\|\|V^n\|\longrightarrow0
$$

并由上述次根估计得谱半径为零。

**命题。** 若 $N\subseteq L^2(X)$ 为 $A$ 的闭不变子空间，则

$$
\mathcal M_N=
\bigoplus_{j\in\mathbb Z}\iota_jD_jN
\tag{8.4}
$$

是 $S,V$ 的共同闭不变子空间。若 $N$ 非零且真，则 $\mathcal M_N$ 也非零且真。

**证明。** 各 $D_jN$ 闭，正交直和闭。(8.3) 保证每个有限坐标向量被 $S,V$ 送入该和；利用 $S,V$ 有界和有限坐标向量稠密，推广到整个和。第零坐标为 $N$，所以非零性和真性直接传递。证毕。

所以，证明这个具体 $A$ 有非平凡普通不变子空间，就同时排除所有 $S+\lambda V$ 作为 ISP 反例。反过来，任何 $T_\lambda$ 若真是完整 ISP 反例，必迫使 $A$ 也是一个反例。这里只证明这个必要条件与充分构造，没有证明二者等价。

## 9. 尚未解决的核心

1. 对具体 $A$ 构造非零真闭不变子空间，或证明不存在。
2. 不依赖标量乘子共同不变性的前提，分析一般 $S,V$-共同不变子空间。
3. 对 $T_\lambda$ 的任意闭线性不变子空间给出结构。无支集不变子空间、单射稠密值域、拟幂零、复对称均不自动完成这一任务。

本笔记排除了“加一个后向项后仍有明显尾部”“产生特征向量”“值域闭包是真子空间”“算子变紧”等直接路线，同时把共同不变子空间的一条充分构造集中到 (8.2) 的标量模型。它仍是中间进展，不满足课题完成标准。
