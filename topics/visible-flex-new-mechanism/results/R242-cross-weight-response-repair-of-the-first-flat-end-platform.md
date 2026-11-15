# R242：跨权 pure 零响应支付首平端平台并保持一次、二次层

日期：2026-11-15。**完整纸面证明；没有新的研究计算、profile 求积、原目标恢复或平台数值评价。**

本稿接 [R234](R234-weight-zero-first-endpoint-layer-cancelled-by-a-zero-pure-response.md)、[R240](R240-weight-zero-quadratic-endpoint-principal-part-vanishes.md) 的同一个 $H_{\mathrm E}$，利用 R217/R219 已证明的完整响应，把它在首个原矩形 $f$ 上升端的两个真实平台二次系数同时消掉。R226 的整条响应链又保证：这次平台修正不重开已支付的一次与二次平端层。

这是一条全 $U$ 中的真实函数空间结论。新代表不再限于真权零，但仍 whole pure 零、$\lambda_+=1$；在选定的同一个合法圆上，两个 mixed 目标都通过这个首左端的完整局部光滑门。没有宣称八个退化通量、全部平台、其他端点、完整 period 或实际成本半群已经支付。

## 1. 固定圆与必须选对的局部端点

固定 [R225](R225-complete-period-range-flat-end-germs-and-finite-observation-quotient.md) 第 2 节构造的一个合法解析导数包圆

$$
\phi_\theta=\cos\theta\,f+\sin\theta\,g.
\tag{1}
$$

它满足原三矩、完整二阶与第三 ruling，以及 hook 消去；所有原函数使用同一个右锚。各活动包的有限退化前提也已由该文支付。

特别选择**最左侧完整基本 packet 中，原矩形第一次 $f$ 上升 step**的左端为 $a_*$。它左方还有用于三矩的补偿包。因此，本文所用的平台必须是 $a_*$ 前方的那个共同零 gap，不能直接把全圆最左 collar 的观测与它混同。

在这个 gap 有 $f=g=0$，且在 $a_*$ 两个输入的全部 jets 为零。靠右有

$$
g=0,\qquad
f(a_*)=0,\qquad
p(t)=f'(a_*+t)=e^{-c/t}a(t),
\quad c>0,\quad a\in C^\infty,\quad a>0.
\tag{2}
$$

R225 的 $\psi P$、最终正幅度和真实坐标缩放给这种形式；$c$ 是实际宽度参数，不暗设为一。

对 whole pure 零的 $V\in U$，记完整相位输出为

$$
V_\theta=\sin^2\theta\,V_d+2\sin\theta\cos\theta\,V_e.
\tag{3}
$$

在 $a_*$ 前方的共同零 gap，$V_d,V_e$ 各有一个唯一的二次以下原多项式尾。定义

$$
\mathcal L_{a_*}(V)
=\bigl([x^2]V_d,\ [x^2]V_e\bigr)
\quad\text{在该局部零 gap 上取系数}.
\tag{4}
$$

这里 $x$ 是最终固定的原 profile 坐标。换为 $t=x-a_*$ 不改变二次项系数。式 (4) 为零准确等价于该 gap 上两个原目标的二阶导数都为零；常数及一次尾仍保留。

## 2. R225 与 R217 非零行列式确在同一合法圆上兼容

[R217](R217-two-left-tail-invariants-independent-on-pure-zero-responses.md) 使用

$$
J_*=\int g\,f''(f''')^2.
\tag{5}
$$

在基本矩形的 $f$ 下降包，$g=1$、$f'=-\rho_3$，所以相关原量是

$$
J_*^{\rm rect}=-\int \rho_3'(\rho_3'')^2,
\tag{6}
$$

不是 $\int(\rho_3')^3$。

R217 先给具有非零式 (6) 的非对称光滑 bump。R225 第 2.2–2.3 节用正的

$$
\psi(t)P(t),\qquad
\psi(t)=\exp\left(-\frac1t-\frac1{1-t}\right),
\tag{7}
$$

在足够高的有限 $C^r$ 范数中逼近它。式 (6) 是 $C^2$ 连续泛函，故足够小的逼近保留其非零值。

改变 profile 后，R225 重新解真实三个左矩补偿，重新作共同正幅度归一化，并重新使用原八 packet 的完整有限差分构造。这里不沿用旧 profile 的矩值：

- 每个左补偿仍为 $f$-only 或 $g$-only；
- $f$-only 左补偿处 $g=0$，$g$-only 左补偿处 $f''=0$，所以它们对式 (5) 均无贡献；
- 八个完整 packet 的贡献按四次幅度相加，乘子为 $\sum_j a_j^4>0$，不发生第三阶所用的交错抵消；
- 共同正幅度与正仿射坐标变换只给式 (5) 乘非零正因子。

因此这同一个合法解析圆满足

$$
J_{\rm total}:=\int_\ell^r g\,f''(f''')^2\ne0.
\tag{8}
$$

其首上升包的局部 germ 是式 (2)，而 R217 的两响应非退化前提仍成立。没有把一个不满足原三矩的近似 profile 当成最终圆。

## 3. 把两左尾公式准确搬到 $a_*$ 的零 gap

为计算式 (4)，仅在证明中定义截后的输入：

$$
f^+(x)=
\begin{cases}
0,&x\le a_*,\\
f(x),&x\ge a_*,
\end{cases}
\qquad
g^+(x)=
\begin{cases}
0,&x\le a_*,\\
g(x),&x\ge a_*.
\end{cases}
\tag{9}
$$

原 gap 和全部平端 jets 使它们是真正光滑的双 collar profiles。按 R56 的同右锚因果性，在这个 gap 及其右侧，原输入和截后输入给出完全相同的输出：全部查询 jets 与全部右侧积分相同。没有重置任何右尾常数。

截后 pair 不必另满足圆的三矩条件。它只用于读取原圆已有的同一个输出，不替换实际第一圆。R217 第 3–5 节推导响应左尾所用的是任意双 collar 输入的原式身份及导数轴性质；这些条件对式 (9) 仍成立。

取 R217/R219 的完整响应链

$$
P(u,v)=J(u''v''),\qquad
R(u,v)=u'v'+xJ(u''v''),\qquad
K=K_{P,[P,R]},
\tag{10}
$$

$$
\mathscr D=x^2\partial_x-2x,\qquad
\delta A=\mathscr D_{\rm out}A
-\sum_{\text{全部输入槽}}A(\ldots,\mathscr D_{\rm in},\ldots),
$$

$$
K_1=\delta K,\qquad K_3=\delta^3K.
\tag{11}
$$

R217 的 E8 导子表、R71 完整交换子和 R83 完整响应给

$$
K_1,K_3\in\mathcal R\cap\ker\pi.
\tag{12}
$$

这不是把 $\mathscr D$ 当成实际几何的坐标变换；它只是具有上述真实响应来源的代数运算。

设

$$
A_a=\int_{a_*}^{r}(f'')^2(f''')^2,\qquad
J_a=\int_{a_*}^{r}g\,f''(f''')^2.
\tag{13}
$$

首个非零平端上升 bump 已使 $A_a>0$。若该非负密度恒零，在 $f''\ne0$ 的每个连通小区间将有 $f'''=0$，从而 $f''$ 为常数且无法平滑接到两端零值；这与非零平端 bump 矛盾。

由于 $a_*$ 属于**第一个完整 packet**，它左侧被删掉的只有该 packet 的三矩补偿。按第 2 节，这些补偿对式 (5) 的贡献全为零。因此

$$
\boxed{A_a>0,\qquad J_a=J_{\rm total}\ne0.}
\tag{14}
$$

现在对截后输入直接使用 R217(21)、(25)，得到

$$
\boxed{
\mathcal L_{a_*}(K_1)=(8A_a,0),\qquad
\mathcal L_{a_*}(K_3)=(B_a,-96J_a).
}
\tag{15}
$$

$B_a$ 是 R217 的完整左尾公式在式 (9) 上定义的有限实数，不需要先求其数值。所有 $\delta$ 都在同一个最终 $x$ 坐标中定义，没有把原算子换为局部平移坐标下另一算子。

于是

$$
\boxed{
\det
\begin{pmatrix}
8A_a&B_a\\
0&-96J_a
\end{pmatrix}
=-768A_aJ_a\ne0.
}
\tag{16}
$$

式 (16) 是所需的**局部平台**满射，而不是未经证明地把 global 左尾观测搬到内部 gap。

## 4. 为什么这两个响应不会重开端点奇异层

[R219](R219-eight-packet-fluxes-independent-on-pure-zero-responses.md) 第 3 节证明整条有限 $\delta^nK$ 链具有完整形式：局部四次微分多项式，加有限个

$$
c(x)J(F_4)
\tag{17}
$$

之和。$F_4$ 是同一点 profile jets 的四次多项式，无嵌套原函数；各 $c(x)$ 为多项式。这来自 R83 的三个完整响应项，包括真实第三历史，不是只计算某个领先项。

在式 (2) 的 germ 中，每个局部 profile jet 都属于

$$
p\mathscr A,\qquad
\mathscr A=\bigcup_{N\ge0}t^{-N}C^\infty.
$$

因此局部四次项与 $F_4$ 均属于 $p^4\mathscr A$。真实正右积分准确为

$$
J(F_4)(a_*+t)
=J(F_4)(a_*)-\int_0^tF_4(a_*+s)\,ds.
\tag{18}
$$

R226 的精确衰减积分定理使第二项仍为 $p^4\mathscr A$。所有第一项的和保留完整真实右尾；它在前方零 gap 是一个二次以下多项式。因为式 (17) 中 $c(x)$ 均为多项式，这个多项式身份延续到右侧 germ。由此，[R226](R226-exact-flat-end-layers-and-remainder-germs-of-the-response-chain.md) 第 6 节的完整结论在同一个 $a_*$ 上给

$$
(K_n)_j(a_*+t)
=P_{2,n,j}(a_*+t)+p(t)^4C_{n,j}(t),
\quad C_{n,j}\in\mathscr A,
\quad j=d,e.
\tag{19}
$$

它特别适用于 $n=1,3$。故这两列的局部一次层恒零，二次主部也恒零；它们可以改变的最低局部数据只有**真实平台多项式**。

这里把平台和光滑 germ 分开：式 (19) 不声称 $P_{2,n,j}''=0$，恰恰是它们的非零平台二阶系数提供式 (16) 的控制。扣去各自真实平台后，剩余 $p^4\mathscr A$ 的零通量逆解由 R226 自动光滑。

## 5. 同一个 $H_{\mathrm E}$ 的明确平台修正

沿用 R234 的准确原式

$$
H_{\mathrm E}
=C_2-\frac18R_0-\frac1{64}R_1
+\frac{13}{32}R_2+\frac1{48}R_3
+\frac5{64}R_4-\frac1{32}R_{10}.
\tag{20}
$$

已付

$$
\pi H_{\mathrm E}=0,\qquad
\lambda_+(H_{\mathrm E})=1,
\tag{21}
$$

以及本文首 $f$-up/$g=0$ 左端的 universal 一次层零和二次主部零。

令

$$
(\ell_d,\ell_e)=\mathcal L_{a_*}(H_{\mathrm E}),
$$

并按式 (15) 定义固定实数

$$
\boxed{
\beta=-\frac{\ell_e}{96J_a},\qquad
\alpha=\frac{\ell_d-\beta B_a}{8A_a}.
}
\tag{22}
$$

这些是同一个固定圆的真实函数值所确定的数，不把尾值独立赋值。分母由式 (14) 严格非零。令

$$
\boxed{H_*=H_{\mathrm E}-\alpha K_1-\beta K_3.}
\tag{23}
$$

直接由式 (15)、(22) 得

$$
\boxed{\mathcal L_{a_*}(H_*)=(0,0).}
\tag{24}
$$

不需要先知道 $\ell_d,\ell_e,B_a$ 的具体数值，式 (22) 已是准确的存在性与构造公式。因而无需为这项平台可修性再运行一个单 $H_{\mathrm E}$ 平台求值。

由式 (12) 和真实正字符杀完整响应空间，

$$
\boxed{
H_*\in U\cap\ker\pi,\qquad
\lambda_+(H_*)=1.
}
\tag{25}
$$

这不是 $H_*$ 为零，也不是把 $H_*$ 宣称为一条实际可取得的有符号成本。

## 6. 权范围与两个 mixed 目标全部保留

### 6.1 修正跨越真权，不能偷做权零投影

R219 使用的

$$
\mathcal H=\mathscr L_{x\partial_x-1}
$$

在四线性算子上满足

$$
\mathcal H\text{ 的特征值}
=\text{真 profile 权}+3.
\tag{26}
$$

因为减去四个输入槽的 $-1$，再加输出槽的 $-1$，净产生 $+3$。R219 已给

$$
\mathcal HK=-5K,\qquad[\mathcal H,\delta]=\delta.
$$

所以

$$
\operatorname{wt}K=-8,\qquad
\boxed{\operatorname{wt}K_1=-7,\quad
\operatorname{wt}K_3=-5.}
\tag{27}
$$

式 (23) 因此一般包含真权 $0,-7,-5$，不再属于单一真权零块。所有项却同属真实全 $U$，在同一个原右锚、同一个固定合法圆的完整输出中可以相加。没有规则要求固定圆目标的补偿必须保持真权。

$\lambda_+$ 是 R196 在全 $U$ 上的权零字符，并杀全部 $\mathcal R$；式 (25) 用的是这个完整事实，不只是一张权零矩阵的消去。

在谈式 (23) 的端层时，应使用**不再先作真权零投影**的 canonical mixed $-2$ 局部观测。R234/R240 对 $H_{\mathrm E}$ 的真权零计算适用，是因为它本身就只有真权零；两条新响应的全部权分量则由式 (19) 直接支付。没有把新增的奇权分量投掉后再声称端层仍为零。

### 6.2 mixed $-2$ 与两个真实目标的关系

对 whole pure 零成本，[R230](R230-first-flat-end-layer-as-an-exact-cubic-tail-operator.md) 第 8 节以及 R213/R159 给准确身份

$$
\boxed{
V_d=-4\operatorname{Re}V_{-2},\qquad
V_e=4\operatorname{Im}V_{-2}.
}
\tag{28}
$$

式 (28) 是完整输出的身份，不限于 $H_{\mathrm E}$ 的权零分量。R234/R240 对它的 mixed $-2$ 原根所证零，因而同时支付它的两个实目标的相应端层。式 (19) 又对 $K_1,K_3$ 的两个实目标分别成立；$\alpha,\beta$ 为实数，故这些层在式 (23) 中全部保持。

准确地，记本端局部一次映射为 $\mathfrak T^\uparrow_{-2}$，在其核上记 R236 二次主部为 $\mathfrak B^\uparrow_{-2}$；此处下标不含真权零投影。则

$$
\boxed{
\mathfrak T^\uparrow_{-2}(H_*)=0,\qquad
\mathfrak B^\uparrow_{-2}(H_*)=0.
}
\tag{29}
$$

式 (29) 对本端允许的真实平端 germ 和共同尾函数保持 universal 身份；式 (24) 的平台消去则是针对已经固定的同一个合法圆。没有把这两个范围混同。

## 7. 首左端的两个真实零通量方程均光滑

对 $j=d,e$，式 (24)、(29) 给

$$
(H_*)_j=P_{1,j}+p^2B_j+p^3C_j,
\quad
P_{1,j}''=0,\qquad
t^4B_j\in C^\infty,\qquad
B_j,C_j\in\mathscr A.
\tag{30}
$$

两响应所添的 $p^4$ 余项已经吸收在高层中，没有改变二次主部。由 [R236](R236-quadratic-endpoint-principal-part-criterion.md) 定理 2，对于

$$
\mathcal M_fu_j=((6pp''-2(p')^2)u_j')'
-6(p'p'')'u_j=(H_*)_j'',
\tag{31}
$$

其所有零端通量分支均可在 $a_*$ 光滑延拓，不同分支只差 $C_jp$。这里不要求 $u_j(a_*)=0$，也没有把非零通量支路纳入结论。

R225 的 hook period 右端只是对两个实目标分别乘非零常数。因此相同局部结论适用于它的两个相位源；不需要改变第一圆、种子、右锚或把两个相位分别任意指定。

综合得到本稿的完整新结论：

$$
\boxed{
\begin{gathered}
\pi H_*=0,\qquad\lambda_+(H_*)=1,\\
\mathcal L_{a_*}(H_*)=0,\qquad
\text{首 }f\text{-up 左端的两个完整零通量 germ 均光滑。}
\end{gathered}}
\tag{32}
$$

因此把本端的两平台二次系数、一次层和二次主部联合起来，仍不能在所述真实函数空间上读出那个非零正字符。该联合局部观测的核已经包含式 (23) 的明确非零函数。

## 8. 对主线的准确作用与尚未支付的范围

式 (32) 省掉的是一个没有决定性的单代表平台求值，不是省掉完整 range。

- 只修复 $a_*$ 所在 gap。其他内部平台、其他 packet 和另一侧端点没有在本文处理。
- $K_1,K_3$ 的八个修正退化通量可能非零。本文没有保持 R219/R222 的全部八条通量，也没有把两尾满射与八通量满射拼成未证明的十元组满射。
- R225 的每包总通量、全部内部 Laurent 条件和右锚整体匹配仍须支付。
- 式 (23) 是 $U$ 内的真实原函数线性组合。R217 的有限配对词说明响应的真实来源，但其公共基准仍存在；本文没有把任意有符号组合冒作实际负成本或一条闭 hook。
- 因而也未取得同一个实际 $w_\theta$ 的完整 period/ruling 联立，更未得到 README 的有限等距族、同一固定度量、嵌入或 reach 结论。

没有新增科学运行。下一目标应进入这些尚未支付的完整兼容门，而不再重算已经光滑的 $p^3\mathscr A$ 以上局部层。
