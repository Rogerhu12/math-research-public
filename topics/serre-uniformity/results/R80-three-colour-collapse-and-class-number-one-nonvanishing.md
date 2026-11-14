# R80：三颜色全塌缩、唯一 Brandt 类与类数一的 $M<3p$ 非消失

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明。** 本文接 R76 的三点结构，证明：在 $p>37$、$p\equiv2\pmod3$、$M<3p$ 时，三次环类周期若全消失，环类数必须恰为 $3$。进一步，当底域类数 $h_K=1$ 时，全部残余情况均可严格排除，因此这个分支在整个 $M<3p$ 范围有非零中心值。唯一 Brandt 类的论证显式处理了 $p$ 两边理想造成的两类歧义；最后两个数值候选有纯整数复算证书。

这里没有给 $M$ 上界，没有排除 exceptional 分母，也没有处理完整 $p$ 惯性。主问题仍未完成。

## 1. 设置与结论

沿用 R76：$\mathcal O=\mathbb Z+c\mathcal O_K$ 是虚二次序，判别式为 $-M$，其中
$$M=|D_K|c^2.$$
设
$$
p>37,\qquad p\equiv2\pmod3,\qquad
p\nmid M,\qquad p\text{ 在 }K\text{ 惰性},\qquad M<3p.
\tag{80.1}
$$
取 $B=B_{p,\infty}$、极大序 $R$ 及 $K\hookrightarrow B$，满足 $R\cap K=\mathcal O$。对原始、阶恰为 $3$ 的环类字符 $\eta$，记
$$
\varphi:\operatorname{Pic}(\mathcal O)\to\mathrm{Cls}(R),
\qquad[\mathfrak a]\mapsto[\mathfrak aR],
$$
$$
P_\eta=\sum_{[\mathfrak a]}
\eta(\mathfrak a)^{-1}[\varphi(\mathfrak a)].
\tag{80.2}
$$

**定理 80.1（不要求 $h_K=1$ 的塌缩结构）。** 在 (80.1) 下，$\varphi$ 的每个纤维至多含三个类。如果 $P_\eta=0$，则
$$
\boxed{h(\mathcal O)=3,\qquad
\#\operatorname{im}\varphi=1,\qquad
\left(\frac{-7}{p}\right)=-1.}
\tag{80.3}
$$
唯一像类所对应的超奇异 $j$ 为 $-3375\bmod p$。因此按固定素理想作 CM 约化时，环类多项式满足
$$
\boxed{H_{-M}(Y)\equiv(Y+3375)^3\pmod p.}
\tag{80.4}
$$

**定理 80.2（类数一非消失）。** 在 (80.1) 下，再设 $h_K=1$。则存在水平 $p$、权 $2$、平凡 nebentype 的归一化新形式 $g$，使
$$
\boxed{L\!\left(\tfrac12,\pi_{g,K}\otimes\eta\right)\ne0.}
\tag{80.5}
$$
这里是酉自守归一化。证明不调用完整的虚二次类数一分类，也不把有限范围的检索当成一般论证：先由结构严格压到两个具体候选，再用一个精确多项式系数排除它们。

## 2. 三点类型与四点不可能

R76 §§2–3 已证明，一个纤维的每个类可给出同一极大序 $S$ 中的最优嵌入，且：

- 不同类给不被 $S^\times$ 共轭的嵌入；
- 所有嵌入在 $p$ 处同取向；
- 若 $\mathcal O=\mathbb Z[\omega]$，$\omega=(t+\sqrt{-M})/2$，则纯部
  $$v_i=\iota_i(\omega)-t/2$$
  位于平方半径 $M/4$ 的球面；
- 两点距离平方是正的 $p$ 倍数。

因 $M<3p$，每条边长平方为 $p$ 或 $2p$。R76 §4 的整单位共轭排除 $(p,p,p)$ 和 $(p,p,2p)$。R76 (76.29) 又表明 $(2p,2p,2p)$ 必须满足 $3M-8p$ 为整数平方；而
$$3M-8p\equiv p\equiv2\pmod3,$$
不可能。故任何三点碰撞都只能具有边长平方
$$
\boxed{(p,2p,2p).}
\tag{80.6}
$$
同时 R76 已给其必要条件
$$7M-16p=n^2,\qquad
\mathbb Q(\sqrt{-7})\hookrightarrow S\otimes\mathbb Q
\tag{80.7}
$$
及实际整元素 $\beta\in S$，满足
$$\beta^2-\beta+2=0.$$

现在反设同一纤维含四个类，取相应 $v_0,v_1,v_2,v_3$。把平方长度为 $p$ 的边标作短边。每个三角形恰有一条短边；四个三角形共计四次，而每条短边被计两次，故共有两条短边。两条短边不能有共同顶点，否则某个三角形含两条短边。因此它们构成完美匹配。

重标号使短边为 $01$ 和 $23$。向量
$$a=v_1-v_0,\quad b=v_2-v_0,\quad d=v_3-v_0$$
的 Gram 矩阵除以 $p$ 为
$$
\begin{pmatrix}
1&1/2&1/2\\
1/2&2&3/2\\
1/2&3/2&2
\end{pmatrix},
\qquad\det=\frac32>0.
\tag{80.8}
$$
所以四点仿射张成整个三维空间。

置 $r^2=M/4$、$w=v_0+v_1+v_2+v_3$。从每个顶点发出的三条边，其平方长度之和均为 $5p$。于是
$$
5p=\sum_{j=0}^3\|v_i-v_j\|^2
=8r^2-2\langle v_i,w\rangle.
$$
右边使所有 $\langle v_i,w\rangle$ 相同，所以 $w$ 垂直全部差向量。由 (80.8)，$w=0$，从而
$$8r^2=5p,\qquad 2M=5p.$$
这与 $M\in\mathbb Z$、$p$ 为奇数矛盾。因此
$$
\boxed{\text{每个纤维的大小至多为 }3.}
\tag{80.9}
$$

## 3. 含 $\mathcal O_{-7}$ 的唯一 Brandt 类

以下引理是把“每个纤维最多三点”变成全局类数结论的关键。仅证明左序同构或共轭还不够：一般确有来自 $p$ 两边理想的两类歧义。这里用范数为 $p$ 的实际 Frobenius 把这两类主化。

**引理 80.3。** 设 $p>7$ 且 $(\frac{-7}{p})=-1$。在任意极大序 $R\subset B_{p,\infty}$ 的右理想类集合中，恰有一个类，其左序包含一个 $\mathcal O_{-7}$ 的嵌入。这个类对应的超奇异 $j$ 为 $-3375\bmod p$。

### 3.1 一个含范数 $p$ 元素的基准极大序

令 $K_0=\mathbb Q(\sqrt{-7})$、$\mathcal O_0=\mathcal O_{K_0}$。它的类数为 $1$：约化正定二元型的首系数满足 $a\le\sqrt{7/3}<2$，唯一类由 $(1,1,2)$ 给出。

经典 CM 值为 $j(\mathcal O_0)=-3375$。例如
$$A_0:\ y^2=x^3-35x-98$$
具有该 $j$、CM 环 $\mathcal O_0$，且判别式为 $-2^{12}7^3$；所以在本节的 $p$ 好约化。因为 $p$ 在 $K_0$ 惰性，其约化 $\widetilde A_0/\mathbb F_p$ 超奇异。CM 端同态经好约化注入，且
$$
S_0=\operatorname{End}_{\overline{\mathbb F}_p}(\widetilde A_0)
$$
是 $B_{p,\infty}$ 的极大序，含 $\mathcal O_0$。这里使用已发表的 Deuring 理论；所需超奇异端同态与理想对应见 Gross (1987), §2，亦可逐项核对 Voight (2021), Theorem 42.1.9、Theorem 42.3.2、Remark 42.3.3 和 Corollary 42.3.7。$j$ 值及上述 CM 模型可见 Zagier 的已发表章节 §6.1、§6.4。

由于模型在 $\mathbb F_p$ 上，$p$ 次 Frobenius 是实际端同态 $\pi\in S_0$，且
$$\operatorname N(\pi)=p.$$
设 $\mathfrak P_0$ 是 $S_0$ 上的 $p$ 两边素理想。逐素数比较：

- 在 $p$ 处，范数赋值为 $1$，故 $\pi S_{0,p}$ 就是除法极大序的根理想；
- 在 $q\ne p$ 处，$\operatorname N(\pi)=p$ 为单位，故 $\pi\in S_{0,q}^\times$。

因此有**全球右理想等式**
$$
\boxed{\mathfrak P_0=\pi S_0.}
\tag{80.10}
$$
特别是 $\mathfrak P_0$ 的右理想类平凡。这里不只使用它的左序等于 $S_0$。

### 3.2 对所有右 $S_0$ 理想类的分类

取一个局部主右 $S_0$ 理想 $J$，其左序含某个 $\mathcal O_0$ 嵌入。Skolem–Noether 允许左乘某个 $b\in B^\times$，使这个嵌入变成固定的 $K_0\subset B$；不改变右理想类。因此可假设
$$\mathcal O_0J\subset J.$$

对 $q\ne p$，$B_q\simeq M_2(\mathbb Q_q)$。右极大序理想对应二维 $\mathbb Z_q$ 格；左 $\mathcal O_{0,q}$ 稳定意味着该格为 $K_{0,q}$ 中的分式 $\mathcal O_{0,q}$ 理想。因 $\mathcal O_{0,q}$ 为极大二次序，它是 DVR 或两个 DVR 的乘积，局部理想皆主。基准格也如此。因此
$$J_q=t_qS_{0,q},\qquad t_q\in K_{0,q}^\times.$$
这也涵盖 $q=7$ 的二次分歧位置。

在 $p$，局部右理想是 $\Pi^nS_{0,p}$，其中 $\Pi$ 的 reduced norm 赋值为 $1$。而 $K_{0,p}/\mathbb Q_p$ 不分歧，来自 $K_{0,p}^\times$ 的范数赋值为偶数。故可唯一保留一个奇偶量 $e\in\{0,1\}$，使
$$J_p=t_p\mathfrak P_{0,p}^{\,e},\qquad t_p\in K_{0,p}^\times.$$
将 $t_q\mathcal O_{0,q}$ 拼成分式 $\mathcal O_0$ 理想 $\mathfrak a$，得到
$$
J=\mathfrak a\mathfrak P_0^{\,e}.
\tag{80.11}
$$
$h(\mathcal O_0)=1$ 使 $\mathfrak a$ 主，而 (80.10) 又使 $\mathfrak P_0$ 主。因此 $J$ 只有基准类。

这恰好说明两个局部取向所容许的 $e=0,1$ 为什么在本例合并。对一般虚二次序，不能省略 (80.10) 就宣称“左序含这个 CM 域，所以只有一个右理想类”。

### 3.3 更换基准极大序

任意两个极大序局部共轭，因此存在局部主的 $(S_0,R)$ 双模理想 $I$，其左序为 $S_0$、右序为 $R$。乘以 $I$ 给右理想类集合的双射
$$
\mathrm{Cls}(S_0)\longrightarrow\mathrm{Cls}(R),
\qquad[J]\longmapsto[JI].
$$
逆由可逆双模 $I^{-1}$ 给出，局部等式 $II^{-1}=S_0$、$I^{-1}I=R$ 保证左序也相应保持。于是 §3.2 的唯一性对任意 $R$ 成立。

在超奇异椭圆曲线—理想类对应下，基准类就是 $\widetilde A_0$，故其 $j=-3375\bmod p$。引理证毕。

## 4. 周期为零强迫环类数恰为三

假设 $P_\eta=0$。R76 (76.22) 的特征零三颜色计数表明：每个非空纤维中的三种颜色出现次数相等。由 (80.9)，纤维只能恰有三个类，每种颜色一次。

每个这种纤维含三点，故由 (80.7) 其左序含
$$\mathbb Z[\beta]\simeq\mathcal O_{-7},\qquad\beta^2-\beta+2=0.$$
因为 $-7$ 是基本判别式，这个嵌入自动最优。嵌入 $\mathbb Q(\sqrt{-7})\hookrightarrow B$ 又要求 $p$ 在其中不分裂；$p>37$ 排除 $p=7$，故 $(\frac{-7}{p})=-1$。

引理 80.3 于是使所有非空纤维的像都是同一个 Brandt 类。唯一非空纤维大小为 $3$，所以
$$h(\mathcal O)=3.$$
这证明 (80.3)，不要求 $h_K=1$。

### 4.1 理想类映射与 CM 约化相容

为把最后的有限候选接到精确类多项式，说明这里需要的约化相容性，不把取向遗漏成一个因子二。

若最初的 $R$ 不是下面选用的 CM 约化端同态环，先由已发表的 Cai–Shu–Tian 公式从 $P_\eta=0$ 得到全部相关中心值为零。对下面的 CM 约化序再次使用同一公式，正定性和完整尖点谱分解又给它的 $P_\eta=0$。因此可以在这一步更换相容序，而不假设任意指定嵌入已经带有一个选好的 CM 提升。

可选一个 CM 环恰为 $\mathcal O$ 的椭圆曲线 $A$，固定 $\overline{\mathbb Q}\hookrightarrow\overline{\mathbb Q}_p$，并在有限扩张后取得好约化。其 CM $j$ 为代数整数；$p$ 惰性使约化超奇异。因 $p\nmid c$，原来的 $K$ 嵌入与约化端同态环相交仍为 $\mathcal O$：

- 对每个 $q\ne p$，好约化给相同的 $q$ 进 Tate 模。$K_q$ 中保持该格的元素正是 $\mathcal O_q$；
- 在 $p$ 处，$\mathcal O_p=\mathcal O_{K_p}$ 已经极大，任何整端同态中来自 $K_p$ 的元素都在此环。

因此可以用 $R=\operatorname{End}(\widetilde A)$ 及这个最优嵌入应用上面的证明。每个 $\operatorname{Pic}(\mathcal O)$ 类可选范数素于 $pc$ 的代表；其 CM 理想同源约化后仍是同次数的可分同源。Deuring 理想对应把它送到 (80.2) 的右理想类映射。若采用相反的 Hom 约定，会把全部理想类同时求逆；这只把 $\eta$ 换为 $\eta^{-1}$，不影响“所有约化同为一个 $j$”及周期是否为零。

所有 CM 类在这里使用同一个 $p$ 进嵌入及同一取向。故 (80.3) 意味着环类多项式的全部三个根，按这个固定素理想约化，都等于 $-3375$。其系数在 $\mathbb Z$ 中，因而确得 (80.4)。

这个论证只用已发表的 CM 约化/理想对应。R76 的投影—中心值公式可选择这个由 CM 约化得到的 $R$；无需额外声称任意最优嵌入都来自一个未经指定的提升。

## 5. 当 $h_K=1$：用类数公式压缩全部可能

现在假设 $h_K=1$，并反设不存在 (80.5) 的新形式。R76 §6 的完整尖点谱分解和 Cai–Shu–Tian Theorem 1.2 使 $P_\eta=0$。于是第 4 节给
$$h(\mathcal O_c)=3.$$
特别 $c>1$。

记 $D=|D_K|$、$\chi(q)=(\frac{D_K}{q})$，
$$u=[\mathcal O_K^\times:\mathcal O_c^\times].$$
R66 (4.1) 的序类数公式化为
$$
3u=\prod_{q^e\parallel c}q^{e-1}(q-\chi(q)).
\tag{80.12}
$$
其每个因子是正整数。

### 5.1 一个避免完整类数一分类的小引理

若 $3$ 在类数一的 $K$ 中分裂或分歧，一个范数 $3$ 的素理想必为 $(\alpha)$，故
$$N_{K/\mathbb Q}(\alpha)=3.$$
$\alpha$ 不可能有理，因为有理整数的二次范数是平方。令 $t=\operatorname{Tr}(\alpha)$，则
$$
0<12-t^2=D[\mathcal O_K:\mathbb Z[\alpha]]^2,
$$
因而 $D\le12$。

所以
$$
\boxed{h_K=1,\ D>12\quad\Longrightarrow\quad
3\text{ 在 }K\text{ 惰性}\quad\Longrightarrow\quad D\equiv1\pmod3.}
\tag{80.13}
$$
此外，基本负判别式 $-D$ 在 $D\le12$ 时仅有 $-3,-4,-7,-8,-11$。因此类数一且 $3$ 分歧只能是 $K=\mathbb Q(\sqrt{-3})$。这里只枚举了五个小基本判别式，未使用完整 Heegner–Baker–Stark 分类。

### 5.2 单位只有 $\{\pm1\}$ 的情形

排除 $K=\mathbb Q(i),\mathbb Q(\sqrt{-3})$ 后，$u=1$，(80.12) 的右边为 $3$。

若奇素数 $q$ 在 $K$ 不分歧，$q-\chi(q)$ 是正偶数，不可能整除 $3$。若奇素数分歧，其局部因子为 $q^e$，只能是 $q=3,e=1$；但上一节已排除这个域。若 $2$ 分歧，其局部因子为正的 $2$ 次幂，也不可能。

因此只有 $q=2$ 不分歧的可能。其指数必须为 $1$；要使乘积为 $3$，必须
$$
c=2,\qquad\chi(2)=-1,\qquad M=4D.
\tag{80.14}
$$

若 $D>12$，则由 (80.13) 有 $M\equiv1\pmod3$，已被 R76 推论 76.1a 排除。若 $D\le12$，非单位例外的基本判别式只有 $-7,-8,-11$；其中 $2$ 惰性的仅 $-11$，所以只剩
$$M=44.$$
但 $p>37$ 时 $44<16p/7$，由 R76 的主界又被排除。

### 5.3 $K=\mathbb Q(i)$

此时 $u=2$，(80.12) 的右边应为 $6$。奇素数 $q$ 不分歧；要使 $q-\chi(q)$ 整除 $6$，只能为 $2$ 或 $6$。

对应的可能是 $q=3$ 且 $\chi(3)=1$，或 $q=5$ 且 $\chi(5)=-1$，或 $q=7$ 且 $\chi(7)=1$；但在 $\mathbb Q(i)$ 中这三个符号分别为 $-1,1,-1$，全部不符。只剩分歧素数 $2$，其因子是 $2^e$，不能等于 $6$。所以此域没有解。

### 5.4 $K=\mathbb Q(\sqrt{-3})$

此时 $u=3$，(80.12) 的右边为 $9$。所有 $q\ge5$ 的局部因子为偶数，不能出现。$2$ 惰性，因子为 $3\cdot2^{e_2-1}$，故 $e_2=0$ 或 $1$；$3$ 分歧，因子为 $3^{e_3}$。于是
$$
e_2+e_3=2,\qquad e_2\in\{0,1\},
$$
给出恰好两种：
$$
c=6,\ M=108;\qquad c=9,\ M=243.
\tag{80.15}
$$

对于 $M=243$，R76 的三点必要条件要求 $7M-16p$ 为平方，但
$$7\cdot243-16p\equiv5\pmod{16},$$
不可能。最后只剩 $M=108$。

### 5.5 唯一剩余判别式的两个素数

R76 给三点碰撞的必要条件 $M\ge16p/7$。结合 $p>37$、$p\equiv2\pmod3$ 及 $108<3p$，得到
$$
37<p\le\frac{7\cdot108}{16}=47.25,
\qquad p\equiv2\pmod3.
$$
这个闭合有限区间中仅剩
$$
(p,M)=(41,108),\quad(47,108).
\tag{80.16}
$$
它们确满足平方必要条件，分别有 $7M-16p=100,4$，因此不能仅用三点格筛就宣布已排除。下一节使用严格的全塌缩条件 (80.4)。

## 6. 两个候选的精确类多项式证书

### 6.1 从 $\Phi_3$ 得到 $H_{-108}$

令 $\tau=\sqrt{-3}$。序 $\mathcal O_2=\mathbb Z[\tau]$ 的判别式为 $-12$，类数 $1$，其 CM 值为
$$J=j(\mathcal O_2)=54000.$$
$\mathcal O_2$ 的四个指数 $3$ 子格可取
$$
3\mathbb Z+\tau\mathbb Z,\qquad
\mathbb Z+3\tau\mathbb Z,\qquad
3\mathbb Z+(1+\tau)\mathbb Z,\qquad
3\mathbb Z+(2+\tau)\mathbb Z.
$$
第一个等于 $\tau\mathcal O_2$，故其 $j$ 仍为 $54000$。其余三个的乘子环均为判别式 $-108$ 的序；相应的约化二元型是
$$
(1,0,27),\qquad(4,-2,7),\qquad(4,2,7).
$$
它们两两不等价，并穷尽这个类数为 $3$ 的序。因此经典模多项式的定义给精确整数恒等式
$$
\boxed{\Phi_3(54000,Y)=(Y-54000)H_{-108}(Y).}
\tag{80.17}
$$
这一步在特征零进行；没有用模 $p$ 的重根计算反向猜测 CM 导子。

$\Phi_3(X,Y)$ 的 $Y^3$ 系数为
$$-X^3+2232X^2-1069956X+36864000.$$
因此 (80.17) 给 $H_{-108}$ 的根迹
$$
T=54000^3-2232\cdot54000^2+1069955\cdot54000-36864000
=151013228706000.
\tag{80.18}
$$
完整整数除法还给
$$
\begin{aligned}
H_{-108}(Y)={}&Y^3-151013228706000Y^2\\
&+224179462188000000Y\\
&-1879994705688000000000.
\end{aligned}
\tag{80.19}
$$

所用 $\Phi_3$ 的全部非零系数来自 Andrew Sutherland 的作者数据，与 Bröker–Lauter–Sutherland 已发表算法配套；小规模的具体系数是无条件的精确整数，不把该算法的 GRH 运行时间分析当作数学假设。

### 6.2 迹已排除全塌缩

若 (80.4) 成立，三个根均为 $-3375$，故必须
$$T\equiv-3\cdot3375=-10125\pmod p.$$
实际结果为：

| $p$ | $T\bmod p$ | $-10125\bmod p$ |
|---|---:|---:|
| $41$ | $6$ | $2$ |
| $47$ | $28$ | $27$ |

两行都不相等，所以两个候选均不能满足 (80.4)。这排除了 $h_K=1$ 时所有的 $P_\eta=0$ 情形。R76 §6 的已发表谱分解及 Cai–Shu–Tian 公式遂证明 (80.5)。

### 6.3 可复算文件

[纯整数证书](../scripts/r80_small_fibre_trace_certificate.py) 只依赖 Python 标准库，包含：

- (80.8) 的有理 Gram 行列式；
- 作者表中 $\Phi_3$ 的十个非对称重复系数及完整对称恢复；
- (80.17) 的整数除法、零余数及完整 (80.19)；
- (80.16) 的闭区间素数核对和两行迹模数；
- $M=243$ 的模 $16$ 平方排除。

复算命令：

~~~sh
python topics/serre-uniformity/scripts/r80_small_fibre_trace_certificate.py
~~~

已执行，所有精确等式成立。该脚本验证最后的有理数与整数证书；前面的纤维、理想和 CM 解释由正文证明，不能由数值输出替代。

## 7. 对实际小惯性分支的作用与边界

在 R66 的实际设置中，$\rho_{E,p}$ 的完整像为非分裂 Cartan 正规化子，且 $p$ 惯性严格小于 Cartan。于是
$$p\equiv2,5\pmod9,\quad p\equiv2\pmod3,$$
三次商字符 $\eta$ 为原始环类字符，$p$ 在商域 $K$ 惰性、$p\nmid M$。如果再有 $h_K=1$，则本文将 R76 的有附加同余或平方条件的范围提升为
$$
\boxed{M<3p\quad\Longrightarrow\quad
\exists g:\ L(\tfrac12,\pi_{g,K}\otimes\eta)\ne0.}
\tag{80.20}
$$

R69 的实际秩零商和 R72 的最优商形式浸入因此适用。对任意 $F/\mathbb Q$ 满足 $F[p]\simeq E[p]$，每个 $j(F)$ 分母素数 $\ell$ 都必须 exceptional，且
$$\ell\equiv\chi_K(\ell)\pmod p.$$
特别，如果实际 $E$ 有一个非 exceptional 分母素数，则本节的类数一小惯性分支必满足
$$\boxed{M\ge3p.}\tag{80.21}$$

这个结果仍未给变化环类导子 $c$ 的上界。不能把 $M\ge3p$ 与 R66 的导子形状一起误读成矛盾；R66 §4 已给出任意大导子的实际类域字符。那些字符是否来自本题的真实异常椭圆曲线，是仍需控制的全局问题。

定理 80.1 本身对一般 $K$ 成立；从其 $h(\mathcal O)=3$ 再分析底域类数 $3$ 是另一个可独立完成的接口，本文定理 80.2 明确仅登记 $h_K=1$。本文也没有把固定的 $M/p$ 范围扩大为 $p\gg\sqrt M$。

## 8. 来源与证明归属

- [R76](R76-three-point-fibres-and-cubic-nonvanishing.md)，§§2–6：同取向嵌入注入、三点类型、整格平方条件、三次颜色计数及已发表周期公式。
- B. H. Gross, *Heights and the special values of L-series*, CMS Conference Proceedings **7** (1987), 115–187，§2（超奇异曲线、极大序与理想类），§5（谱分解）。[原文](https://wstein.org/papers/bib/Gross-Heights_and_the_Special_Values_of_L-series.pdf)。本文 §3 额外独立证明唯一 Brandt 类，不从极大序共轭直接推出理想类唯一。
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics **288**, Springer, 2021，Chapter 42, pp.783–797，[原刊全文](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_42)。Theorem 42.1.9 给超奇异端同态极大序，§42.2.4 给唯一 $p$ 两边理想与 Frobenius，Theorem 42.3.2、Remark 42.3.3、Corollary 42.3.7 分别给范畴对应、左右交换和理想类对应；本轮逐条核准。
- Don Zagier, *Elliptic Modular Forms and Their Applications*, in **The 1-2-3 of Modular Forms**, Springer, 2008, 1–103，§6.1 的 CM 值表（p.71）及 §6.4 的 CM 椭圆曲线模型。[作者原文](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/978-3-540-74119-0_1/fulltext.pdf)，[DOI](https://doi.org/10.1007/978-3-540-74119-0_1)。
- Reinier Bröker, Kristin Lauter, Andrew V. Sutherland, *Modular polynomials via isogeny volcanoes*, **Mathematics of Computation 81** (2012), 1201–1231，[DOI](https://doi.org/10.1090/S0025-5718-2011-02508-1)，[作者全文版本](https://arxiv.org/html/1001.0402v2)。所用精确 $\Phi_3$ 表为[作者数据](https://math.mit.edu/~drew/modpolys/jfiles/phi_j_3.txt)，[格式说明](https://math.mit.edu/~drew/ClassicalModPolys.html)。
- Cai–Shu–Tian (2014), Theorem 1.2 的完整条件和中心归一化已在 R76 §6.2 核准，本篇直接沿用，没有引入未发表的非消失或整性定理。

本文新增的完整证明为：四点图及四面体矛盾；用 Frobenius 主化 $p$ 两边理想的唯一 Brandt 类；$P_\eta=0\Rightarrow h(\mathcal O)=3$；无需完整类数一分类的导子压缩；最后两例的精确迹排除。
