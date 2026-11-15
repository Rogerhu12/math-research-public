# R244：十一维真实响应模同时支付首平台双尾与八个退化通量

日期：2026-11-15。**完整纸面证明；没有执行新的研究计算、profile 求积、符号编译、原函数消元或采样。** 下文的有限多项式展开均给出可逐项手核的公式。

[R242](R242-cross-weight-response-repair-of-the-first-flat-end-platform.md) 分别支付了首个原矩形 f 上升端的两个平台系数，并保持已付的一次、二次平端层。[R219](R219-eight-packet-fluxes-independent-on-pure-zero-responses.md) 则给八个退化通量的满射。这两个结论本身不能推出十个条件可以同时支付。

本稿在一个明确可选的 R225 合法解析圆上，证明同一条完整响应链的十一维空间对这十个观测满射。关键是：首端平台位于第一包左补偿的右方，其观测是全左尾减去这段实际补偿的尾。这个减项提供了与八个通量条件独立的方向，不能删除。

结论仍限于这十个有限观测和首端两项 germ。它没有宣称完整 period、所有平台、全部内部退化条件、所有端点或第四逐 ruling 已经支付，也没有把一个响应的实线性组合当成一个已实现的有符号成本。

## 1. 观测和圆的准确选择

先在辅助实坐标 x 上选择一个 R183/R225 的完整基本 pair
$(f_*,g_*)$，包括矩形四个 step 及其三个左矩补偿。所有原函数使用同一右锚。在每个活动包上只有 f 或 g 变化；矩形的三个中间平台仍分别为
$(1,0),(1,1),(0,1)$，故其值平面不能由常数 GL2 变为支撑分离平面。

记第一段原矩形 f 上升包为 $(a,b)$，在其左侧的共同零 gap 上，三个左补偿已经结束。按 R215/R219 取包内一点 $x_*$，使

$$
p_*=f_*',\qquad
A_*=6p_*p_*''-2(p_*')^2,\qquad
A_*(x_*)=0,\quad p_*(x_*)>0,\quad p_*'(x_*)>0.
\tag{1}
$$

这里的 $A_*$ 只在式 (1) 表示微分系数；下文的积分常数另用 $\mathsf A$，避免混淆。

把这个完整基本 pair 作八个不交等距平移：

$$
t_j=jL,\qquad
a_j=(-1)^j\binom7j^{1/3},\qquad
(f,g)=\sum_{j=0}^7a_j(f_*,g_*)(x-t_j).
\tag{2}
$$

先取充分大的有限 L，最后共同作正仿射变换与正幅度归一化，放入任意已选定的合法物理区间 I，保留双 collar。第 7 节支付全部兼容性及一个必要的补偿非零条件。

对 whole pure 为零的真实算子 V，写其完整相位输出为

$$
V_\theta=\sin^2\theta\,V_d+
2\sin\theta\cos\theta\,V_e.
\tag{3}
$$

八个观测采用 R219 原来的、带平台减项的 d 目标通量：

$$
\begin{aligned}
\mathcal F_j(V)
={}&\int_{a+t_j}^{x_*+t_j}
 f'(x)V_d''(x)\,dx\\
&-\{f(x_*+t_j)-f(a+t_j)\}
 V_d''(a+t_j).
\end{aligned}
\tag{4}
$$

这八个数不是两个 mixed 目标各八个通量的缩写。e 目标的其他退化通量没有在本稿中自动支付。

令 $a_*=a$ 为第一个完整 packet 中的原矩形 f 上升端。其左方还有第一个 packet 的矩补偿，因此定义局部平台双尾

$$
\mathcal L_a(V)=
\bigl([x^2]V_d,\ [x^2]V_e\bigr)
\quad\text{在 }a_*\text{ 左侧共同零 gap 取系数}.
\tag{5}
$$

完整十观测为

$$
\mathscr O(V)=
\bigl(\mathcal F_0(V),\ldots,\mathcal F_7(V),
\mathcal L_{a,d}(V),\mathcal L_{a,e}(V)\bigr).
\tag{6}
$$

在本稿所用算子上，gap 中的真实尾均至多二次，故式 (5) 有准确意义。它不是全圆最左 collar 的双尾。

## 2. δ 链准确是十一维模

沿用 R217/R219：

$$
P(u,v)=J(u''v''),\qquad
R(u,v)=u'v'+xJ(u''v''),\qquad
K=K_{P,[P,R]},
\quad J(F)(x)=\int_x^rF.
\tag{7}
$$

令 $\mathscr L_X$ 表示输出 X 减去全部输入槽上的 X，置

$$
N=\mathscr L_{\partial_x},\qquad
H=\mathscr L_{x\partial_x-1},\qquad
\delta=\mathscr L_{x^2\partial_x-2x}.
\tag{8}
$$

R217 的完整原式表和 R219(16)–(18) 给

$$
[N,\delta]=2H,\qquad [H,\delta]=\delta,\qquad
NK=0,\quad HK=-5K,
$$

$$
N\delta^nK=n(n-11)\delta^{n-1}K.
\tag{9}
$$

这些是同右锚的原函数身份，不是由一组评价数据猜得的表示。

### 2.1 有限终止与准确维数

R217 第 2 节的 E8 变换表给 $\delta^5E=0$，对每个 $E\in E_8$ 都成立。最长链的层次为

$$
r_0\longrightarrow(r_1,s_0)
\longrightarrow(p_0,s_1)
\longrightarrow(p_1,t_1)
\longrightarrow p_2\longrightarrow0.
\tag{10}
$$

完整响应 $K_{E,[F,G]}$ 对三个 E8 方向 E、F、G 分别线性，且 δ 对其原组合满足 Leibniz 法则。对 K 施十三次 δ，每个 Leibniz 项在至少一个方向上施了五次 δ，故

$$
\delta^{13}K=0.
$$

用式 (9) 的 $n=13,12$，依次得到

$$
0=26\delta^{12}K,\qquad
0=12\delta^{11}K.
$$

于是

$$
\delta^{11}K=0.
\tag{11}
$$

另一方面，R219(15) 给 $\mathcal F_*(K)\ne0$，所以 $K\ne0$。对 $n\le10$，式 (9) 连乘的各因子均非零；若 $\delta^nK=0$，再作用 $N^n$ 就会迫 $K=0$。因此这些十一个向量均非零。它们的 H 特征值为 $-5+n$，互不相同，故

$$
\mathcal M=\operatorname{span}_{\mathbb R}
 \{\delta^nK:0\le n\le10\},\qquad
\dim\mathcal M=11.
\tag{12}
$$

每个向量都在真实响应空间 $\mathcal R$ 中，且 whole pure 为零。这里使用 R217 的真实 R71/R83 响应闭性；没有把非仿射 profile 变换当成实际几何控制。

### 2.2 归一符号

定义

$$
c_n=(-1)^n\frac{10!}{(10-n)!},\qquad
e_n=\frac{\delta^nK}{c_n},\qquad 0\le n\le10.
\tag{13}
$$

则准确有

$$
Ne_n=ne_{n-1},\qquad
He_n=(n-5)e_n,\qquad
\delta e_n=-(10-n)e_{n+1},
\tag{14}
$$

最后一式在 $n=10$ 的右侧为零。因而 $e_n\leftrightarrow z^n$ 把这个模识别为次数至多十的多项式空间，其中

$$
N=D_z,\qquad H=zD_z-5,\qquad
\delta=z^2D_z-10z.
\tag{15}
$$

该识别只用于已付真实原函数空间的线性代数。

## 3. 八个通量等价于八点多项式评价

对基本 pair 定义 R219 的单包读出

$$
\mathcal F_*(V)=
\int_a^{x_*} f_*'(x)V_d''(x)\,dx
-\{f_*(x_*)-f_*(a)\}V_d''(a).
\tag{16}
$$

记

$$
F_m=\mathcal F_*(e_m),\qquad
F_0=-\frac8{45}\bigl(f_*''(x_*)\bigr)^5\ne0.
\tag{17}
$$

取任意 $A=\sum_{n=0}^{10}u_ne_n$，令
$p_A(z)=\sum u_nz^n$。实际平移算子为
$\mathcal T_t=e^{tN}$。式 (14) 给

$$
\mathcal F_*(\mathcal T_tA)
=\left(\sum_{m=0}^{10}\frac{F_m}{m!}D_t^m\right)p_A(t)
=:P_A(t).
\tag{18}
$$

由于常数项 $F_0\ne0$，括号内的算子在
$\operatorname{Pol}_{\le10}$ 上可逆。因此

$$
A\longmapsto P_A
\quad\text{是 }\mathcal M\simeq\operatorname{Pol}_{\le10}
\text{ 的准确线性同构}.
\tag{19}
$$

R219 已证明每个 $\delta^nK$ 是局部四次密度加有限个
$c(x)J(F_4)$，没有嵌套原函数，左尾至多二次。由完整 packet 支撑不交及式 (4) 的真实平台减项，

$$
\boxed{\mathcal F_j(A)=a_j^5P_A(jL).}
\tag{20}
$$

不把一般 U 声称为这种单层结构。

八个节点互异，所以八行在 $\mathcal M$ 上秩八，其共同核为

$$
P_A(t)=Q_L(t)R(t),\qquad
Q_L(t)=\prod_{j=0}^7(t-jL),\qquad
\deg R\le2.
\tag{21}
$$

因此还剩三个真实响应方向。以下直接计算两个局部平台行在这个共同核上的秩，不以分别满射替代联合证明。

## 4. 局部截左补偿如何进入双尾

### 4.1 单基本 pair 的全左尾

令 $\ell_d(A),\ell_e(A)$ 为一个完整基本 pair 的全左 collar 中二次尾系数。记

$$
\mathsf A=\int (f_*'')^2(f_*''')^2>0,\qquad
\mathsf J=\int g_*f_*''(f_*''')^2\ne0.
\tag{22}
$$

R217(15)–(25) 给

$$
\ell_d(e_0)=\ell_e(e_0)=0,\qquad
\ell_d(e_1)=-\frac45\mathsf A,\qquad
\ell_e(e_1)=0,
$$

$$
\ell_e(e_3)=\frac{2}{15}\mathsf J.
\tag{23}
$$

还需明确中间的

$$
\ell_e(e_2)=0.
\tag{24}
$$

证明如下。若 K 的原左尾为 $b_0+xb_1$，R217(18) 给

$$
[x^2]\delta^2K=2b_0+2\mathfrak v b_1,
\tag{25}
$$

其中 $\mathfrak v$ 是全部输入槽的真实向量场变分。R217(15)–(16) 中的 $b_0,b_1$ 在轴导数包上没有 $cs$ 项。对 $b_1$ 作一次变分时，只出现 f、φ 的二阶和三阶 jets；在 f-active 包上 g 为常数，

$$
(\mathscr Dg)''=(\mathscr Dg)'''=0,\qquad
\mathscr D=x^2D_x-2x,
$$

所以变分后的这些 jets 仍没有来自 g 的 $s$ 分量。在 g-active 包上，f 的相关 jets 及其第一次变分为零。故
$[cs]\mathfrak v b_1=0$，式 (25) 证明 (24)。没有把第二次变分也错误地当成零：R217 的 $\mathfrak v^2g''=4g$ 正是式 (23) 最后一项非零的来源。

### 4.2 真实左补偿的尾

记 $f_{\rm c},g_{\rm c}$ 为三个左补偿组成的 pair，并令
$\ell_{\rm c}(A)$ 为它们的 d 二次尾。令

$$
\mathsf A_{\rm c}
=\int(f_{\rm c}'')^2(f_{\rm c}''')^2.
\tag{26}
$$

第 7 节选择保证 $\mathsf A_{\rm c}>0$。同样由 R217，

$$
\ell_{\rm c}(e_0)=0,\qquad
\ell_{\rm c}(e_1)=-\frac45\mathsf A_{\rm c}\ne0.
\tag{27}
$$

这组左补偿的 e 输出对整个 $\mathcal M$ 恒零。理由必须在完整相位层说明：各补偿包的值支撑互不相交且为 f-only 或 g-only。whole pure 零算子有
$V_\theta=\mathcal B(f^2,f^2-\phi_\theta^2)$ 的真实双线性表示。f-only 包给纯 $\sin^2\theta$，g-only 包因 $f=0$ 给零。再用本链的局部密度和单层右积分分解，所有包间交叉项确为零。因此没有 e 尾可减。

设

$$
w_j=a_j^4=\binom7j^{4/3},\qquad w_0=1.
$$

在首原矩形 f 上升端前的 gap，第一包左补偿已经位于查询点左方，实际输出为零；其他部分在其左侧留下原二次尾。故准确有

$$
\boxed{\begin{aligned}
\mathcal L_{a,d}(A)
&=\sum_{j=0}^7w_j\,\ell_d(\mathcal T_{jL}A)
-\ell_{\rm c}(A),\\
\mathcal L_{a,e}(A)
&=\sum_{j=0}^7w_j\,\ell_e(\mathcal T_{jL}A).
\end{aligned}}
\tag{28}
$$

式 (28) 是同右锚因果分解，不把已结束的补偿尾继续当成实际函数，也不把这个局部 gap 当成全左 collar。二次尾在坐标平移下的二次系数不变，故没有漏掉平移基点常数。

### 4.3 把任意尾行写成对 $P_A$ 的有限微分算子

对 $\mathcal M$ 上任意线性泛函 $\ell$，设

$$
L_\ell(z)=\sum_{m=0}^{10}\ell(e_m)\frac{z^m}{m!},
\qquad
F(z)=\sum_{m=0}^{10}F_m\frac{z^m}{m!}.
$$

在 $\mathbb R[z]/(z^{11})$ 中定义

$$
D_\ell(z)=L_\ell(z)/F(z).
\tag{29}
$$

因 $F_0\ne0$，此除法唯一。式 (18) 直接给

$$
\ell(\mathcal T_tA)=D_\ell(D_t)P_A(t).
\tag{30}
$$

由式 (23)–(27)，其低阶项为

$$
D_{\ell_d}(z)=\alpha z+O(z^2),\qquad
D_{\ell_{\rm c}}(z)=\beta z+O(z^2),\qquad
D_{\ell_e}(z)=\gamma z^3+O(z^4),
\tag{31}
$$

其中

$$
\alpha=-\frac{4\mathsf A}{5F_0},\qquad
\boxed{\beta=-\frac{4\mathsf A_{\rm c}}{5F_0}\ne0,\qquad
\gamma=\frac{\mathsf J}{45F_0}\ne0.}
\tag{32}
$$

$O(z^k)$ 在这里仅表示有限多项式中次数至少 k 的项，不是未控制的函数余项。

## 5. flux 核中两个明确方向的非零子式

令

$$
Q(s)=\prod_{j=0}^7(s-j),\qquad m=\frac72,
$$

并在式 (19) 的多项式坐标中取

$$
P^{(0)}_L(t)=L^8Q(t/L),\qquad
P^{(1)}_L(t)=L^8Q(t/L)(t/L-m).
\tag{33}
$$

两者次数分别为八、九，且在 $t=jL$ 全为零。因此它们唯一对应
$A_0(L),A_1(L)\in\mathcal M$，并且八个 $\mathcal F_j$ 同时为零。

对任一固定 $r(s)\in\operatorname{Pol}_{\le2}$，取
$P_L(t)=L^8Q(t/L)r(t/L)$。式 (28)–(31) 给准确有限 Laurent 展开

$$
\begin{aligned}
\mathcal L_{a,d}(A_L)
={}&L^7\left\{
\alpha\sum_jw_j(Qr)'(j)-\beta(Qr)'(0)
\right\}+O(L^6),\\
\mathcal L_{a,e}(A_L)
={}&\gamma L^5\sum_jw_j(Qr)'''(j)+O(L^4).
\end{aligned}
\tag{34}
$$

全部系数只由固定基本 pair 和有限微分算子决定，与 L 无关。因此这里的大 L 论证只是在选择一个有限间距，不使用数值极限或无限 profile。

### 5.1 第一个方向由补偿尾独立留下

Q 关于 $m=7/2$ 为偶多项式，而 $w_j=w_{7-j}$。故

$$
\sum_jw_jQ'(j)=0,\qquad
\sum_jw_jQ'''(j)=0.
$$

又 $Q'(0)=-7!=-5040$。于是对 $r=1$，

$$
\mathcal L_{a,d}(A_0)=5040\beta L^7+O(L^6),\qquad
\mathcal L_{a,e}(A_0)=O(L^4).
\tag{35}
$$

若删除式 (28) 的真实补偿减项，式 (35) 的首项就会被错误地删掉；这正是分别满射不能直接拼接的原因。

### 5.2 第二个方向的准确正系数

令

$$
\mathsf V=\sum_{j=0}^7
w_j\{Q(s)(s-m)\}'''_{s=j}.
\tag{36}
$$

对 $r=s-m$，式 (34) 给

$$
\mathcal L_{a,e}(A_1)=\gamma\mathsf V L^5+O(L^4),
\qquad
\mathcal L_{a,d}(A_1)=O(L^7).
\tag{37}
$$

下面完全手工展开 $\mathsf V$。置 $u=2s-7$，则

$$
Q(s)=2^{-8}
(u^2-1)(u^2-9)(u^2-25)(u^2-49)
$$

$$
=2^{-8}
\bigl(u^8-84u^6+1974u^4-12916u^2+11025\bigr).
$$

因此

$$
\{Q(s)(s-m)\}'''
=\frac{63u^6-2205u^4+14805u^2-9687}{8}.
\tag{38}
$$

在四对对称节点上的准确值为：

| j | $u^2$ | $\{Q(s)(s-m)\}'''_{s=j}$ | $w_j$ |
|---|---:|---:|---:|
| 0、7 | 49 | 354180 | 1 |
| 1、6 | 25 | −4164 | $7^{4/3}$ |
| 2、5 | 9 | −1140 | $21^{4/3}$ |
| 3、4 | 1 | 372 | $35^{4/3}$ |

逐项合并即得

$$
\begin{aligned}
\mathsf V
&=2\{354180-4164\,7^{4/3}
-1140\,21^{4/3}+372\,35^{4/3}\}\\
&=24\{29515-2429\sqrt[3]7
-1995\sqrt[3]{21}+1085\sqrt[3]{35}\}\\
&>24\{29515-2429\cdot2-1995\cdot3\}\\
&=24\cdot18672>0.
\end{aligned}
\tag{39}
$$

这里仅用 $\sqrt[3]7<2$、$\sqrt[3]{21}<3$ 及最后一项严格为正；不需要任何积分值或浮点评价。

### 5.3 联合秩

由式 (35)、(37)，

$$
\det
\begin{pmatrix}
\mathcal L_{a,d}(A_0)&\mathcal L_{a,d}(A_1)\\
\mathcal L_{a,e}(A_0)&\mathcal L_{a,e}(A_1)
\end{pmatrix}
=
5040\,\beta\gamma\mathsf V\,L^{12}
+O(L^{11}).
\tag{40}
$$

式 (32)、(39) 使首系数非零，所以存在充分大的有限 L，使式 (40) 非零。此时两平台行在八通量共同核上的秩恰为二。

结合式 (20) 的八行满秩，得到

$$
\boxed{\operatorname{rank}(\mathscr O|_{\mathcal M})=10,\qquad
\dim\ker(\mathscr O|_{\mathcal M})=1.}
\tag{41}
$$

这是十个真实函数观测在同一个十一维响应模上的联合结论。没有重算 R219 的旧八列、旧 profile 或任何原式目标。

## 6. 全链保持首端一次、二次层

[R226](R226-exact-flat-end-layers-and-remainder-germs-of-the-response-chain.md) 第 6 节已对每个有限 $\delta^nK$ 证明：在首 f 上升端 $a_*$，截掉左方补偿后同右锚输出不变，其两个真实 mixed 目标分别有

$$
G_n(x)=P_{2,n}(x)+p(x-a_*)^4R_n(x-a_*),
\qquad R_n\in\mathscr A,
\tag{42}
$$

其中 $P_{2,n}$ 是真实右尾组成的二次以下多项式，
$p(t)=e^{-c/t}a(t)$，$c>0,a>0$ 光滑，$\mathscr A$ 是有限极点光滑因子类。

式 (42) 保全部右方包、原尾常数和 s 历史；不是把每个原函数独立设为常数。由于 R219 的外系数 $c(x)$ 是多项式，gap 中的二次恒等式准确延续到右 germ。

因此整空间 $\mathcal M$ 都保持 R230 的一次层 T 和 R236 的二次主部 B 为零。这里的 B 指 R236 的有限负幂主部，不是其他文献中的 profile 二次算子。

当式 (5) 同时为零时，$P_{2,n}''$ 的真实常数平台已被支付。再由 R226 的零左通量充分式，响应的剩余 $p^4\mathscr A$ 项不会产生新的端点发散。没有因此声称它在其他端点或整个区间都属于 $L_f$ 的像。

## 7. 所需合法圆确可选择，并可压回任意 I

本节支付前面使用的 $\mathsf J\ne0$、
$\mathsf A_{\rm c}>0$、解析包、三矩、八复制与大 L 的共同兼容。

### 7.1 正确的非对称量保持非零

先选 f 上升、下降两个平端 step。下降导数取 R225 的正解析
$\rho_3=\psi P/\int\psi P$，使

$$
-\int\rho_3'(\rho_3'')^2\ne0,\qquad
\psi(t)=\exp\left(-\frac1t-\frac1{1-t}\right).
\tag{43}
$$

R225 第 2.2–2.3 节已经用高有限阶逼近和这个正确积分的连续性证明这种选择存在。原矩形中 g 在 f 下降包恒为 1，所以式 (43) 就给 $\mathsf J\ne0$。这里不使用另一个非对称积分代替它。

### 7.2 用原三矩第一行强迫 f-only 补偿非零

保持这两个 f step 不变，把两个 g step 的导数包取得足够窄，仍与 f 的活动区间不交并保矩形次序。若一个归一化导数 bump 宽度为 $\varepsilon$，则其对应 step 的

$$
\int(g'')^2=\varepsilon^{-3}
\int(\rho')^2.
\tag{44}
$$

故矩形的原零阶复矩可取严格负值：

$$
M_0(f_0+ig_0)
=\int(f_0'')^2-\int(g_0'')^2<0.
\tag{45}
$$

g 在 f 下降包的常值仍为 1，所以这不改变式 (43) 的非零性。

按 R183/R225，在矩形左方放三个不交同形实偶补偿 bump
$\eta_j(x)=\eta(x-c_j)$，选择 $\eta=\psi P$ 型，使其解析有限退化性质成立。三个原矩为

$$
M_0(q)=\int(q'')^2,\quad
M_1(q)=\int x(q'')^2,\quad
M_2(q)=\int x^2(q'')^2+2\int(q')^2.
\tag{46}
$$

轴导数使矩形的这三个复数全为实数。令
$a_0=\int(\eta'')^2>0$、
$a_2=\int x^2(\eta'')^2+2\int(\eta')^2$，解准确实 Vandermonde 系统

$$
\sum_jz_j(a_0,a_0c_j,a_2+a_0c_j^2)^T
=-(M_0,M_1,M_2)^T.
\tag{47}
$$

第一行与式 (45) 给 $\sum_jz_j>0$，所以至少一个 $z_j>0$。取
$\beta_j^2=z_j$，正 $z_j$ 的平方根为非零实数，负者为纯虚数。于是至少一个左补偿是非零 f-only bump，其他仍是 f-only 或 g-only。

对任何非零实 compact 光滑 bump η，

$$
\int(\eta'')^2(\eta''')^2>0.
\tag{48}
$$

否则连续非负被积函数恒零，故
$((\eta'')^2)'=2\eta''\eta'''=0$；由外 collar 得
$\eta''=0$，再由 compact 支撑得 $\eta=0$，矛盾。由各补偿支撑不交，式 (48) 正好给

$$
\mathsf A_{\rm c}>0.
\tag{49}
$$

补偿的 g-only 包有 $f''=0$，f-only 包有 $g=0$，所以它们不改 $\mathsf J$。没有增加第四个补偿或改变原三矩模型。

### 7.3 完整二、三阶与解析有限退化

式 (47) 支付三个复平方矩，正能量给 f、g 的相同非零范数与交叉正交；用共同正幅度归一化。原矩形三个取值平台保留，故仍不可分离。

每个 f step 的导数为非零常数乘 $\psi P$；每个 f-only 补偿的导数为 $\psi$ 乘非零有理函数。R225 第 2.4 节证明 p 和 $A=6pp''-2(p')^2$ 在每个活动区间内只有有限个有限阶零点，靠端点无零。首 f 上升端具有 R230/R236 使用的真实
$e^{-c/t}a(t)$ 形式。

三个复矩使每个完整基本 packet 的二阶 fields 在包外全零。八个幅度满足
$a_j^3=(-1)^j\binom7j$，第七有限差分准确消掉四条完整第三 ruling 的平移次数至多六多项式。轴导数条件则使原 hook 在全部三次槽中为零。这里直接使用 R183/R52 的完整二阶局域和第三原式证明，不把第四一般成本擅自分包。

选择 L 大于包络宽度并满足式 (40)，就得到一个有限的合法圆。它是新选定的 R225 子类实例；不声称任何此前冻结圆都自动满足 $\mathsf A_{\rm c}>0$ 或式 (41)。

### 7.4 大 L 后的物理区间与归一化

最后把辅助变量 y 通过 $x=b+sy$、$s>0$ 放入任意已选定的合法 I，并令新 profiles 为
$C f((x-b)/s),C g((x-b)/s)$，$C>0$。

在 $\mathcal M$ 上，平移由 $e^{bN}$ 给出，纯坐标伸缩的生成元为
$\mathscr L_{xD_x}=H-3\,\mathrm{id}$。因此正仿射原变量变换在 $\mathcal M$ 上给可逆线性变换 $\mathcal S_{b,s}$。所有实际右锚同时换元，零右 collar 不产生新积分常数。

直接换元给

$$
\mathcal F_j^{\rm new}(A)
=\frac{C^5}{s^2}
\mathcal F_j^{\rm old}(\mathcal S_{b,s}A),
\qquad
\mathcal L_a^{\rm new}(A)
=\frac{C^4}{s^2}
\mathcal L_a^{\rm old}(\mathcal S_{b,s}A).
\tag{50}
$$

第二式只取二次系数，所以平移不混入常数、一次尾；第一式两个真实项具有同一因子。两因子均非零，式 (41) 的联合秩不变。

共同正幅度重新归一化，正仿射变换保持三个复零矩、轴导数、非零 $\mathsf J$、补偿非零及双 collar。因而“大 L”不要求最终物理 I 任意大，也没有改变实际几何的合法区间。

## 8. 对同一个 $H_{\mathrm E}$ 的准确后果

R234/R240 已给一个明确真权零的真实算子

$$
\begin{aligned}
H_{\mathrm E}={}&C_2-\frac18R^{(0)}
-\frac1{64}R^{(1)}
+\frac{13}{32}R^{(2)}
+\frac1{48}R^{(3)}\\
&+\frac5{64}R^{(4)}
-\frac1{32}R^{(10)},
\end{aligned}
\tag{51}
$$

满足

$$
\pi H_{\mathrm E}=0,\qquad
\lambda_+(H_{\mathrm E})=1,
\tag{52}
$$

以及首 f-up/g=0 平端的 universal 一次层 T=0、二次主部 B=0。这里继承已有原式证书和公开实际结论，不恢复或重算式 (51) 的七根。

R230 第 8 节和 whole pure 零身份给

$$
V_{-2}=-\frac14(V_d-iV_e).
\tag{53}
$$

所以 R234/R240 对 canonical mixed −2 根的两个零身份，同时支付这两个真实 mixed 目标在该端的相应层；不是只支付一个实投影。

固定第 7 节最终圆，式 (41) 允许取 $A_{\rm corr}\in\mathcal M$，使

$$
\mathscr O(A_{\rm corr})=\mathscr O(H_{\mathrm E}).
$$

令

$$
H_\dagger=H_{\mathrm E}-A_{\rm corr}.
\tag{54}
$$

因为 $\mathcal M\subset\mathcal R\cap\ker\pi$，
$\lambda_+$ 消掉整个真实响应空间，故

$$
\boxed{
\pi H_\dagger=0,\qquad
\lambda_+(H_\dagger)=1,\qquad
\mathcal F_j(H_\dagger)=0\ (0\le j\le7),\qquad
\mathcal L_a(H_\dagger)=(0,0).
}
\tag{55}
$$

式 (42) 又保证 $A_{\rm corr}$ 不重开首端 T、B。结合已付真实平台和 R226/R236 的零左通量判据，两个目标在该首左端均有光滑的局部解 germ。

这里 $H_\dagger$ 一般跨多个真权，不再是权零根。有限 sl2 模是原函数空间中的真实响应模，式 (54) 没有偷偷要求它保持同权。结论表明：$\lambda_+$ 不能只经这十个观测连同已付首 T/B 的联合零条件读出。

它仍没有证明以下任何事项：

- 八个 packet 的所有 e 通量、全部总通量或其他内部 Laurent 条件为零；
- 全部平台和两端 germ 都满足完整 R225 像判据；
- 同一个 gauge 同时支付完整 period 和逐 ruling；
- $H_\dagger$ 是一个有符号实际成本，或已实现其精确全函数值。

剩余问题仍是固定合法圆上完整 period 观测商与 whole pure 零响应像的比较。式 (41) 是一个准确的联合十观测接口，不把该有限接口冒成完整商。

