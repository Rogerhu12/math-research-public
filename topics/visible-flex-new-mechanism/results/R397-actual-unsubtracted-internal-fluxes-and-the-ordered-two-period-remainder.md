# R397：原内部累计通量的实际联调与两个 period 的有序余差

日期：2026-11-15。**原 source 只读与纸面证明；没有执行符号、求积、数值、人工测试或研究运行。**

本稿接
[R396](R396-actual-joint-response-E-two-natural-and-selected-internal-fluxes.md)
的真实截面，但不把其“扣平台 partial”当作原周期方程的未扣平台累计量。第一项新结论是：同一响应库可直接实际支付后者。第二项是完整的条件性归约：在原 whole-$E=0$ 前提下，两条 period 在同一点的剩余组合消掉全部 self，只留下明确的真实右侧三矩通道。对下文指定的完整副本边界微包，该通道准确为零。

直接来源：
[R184](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md)、
[R345](R345-local-whole-E-kernel-orbit-and-eleven-corresponding-degenerate-fluxes.md)、
[R389](R389-ordered-total-fluxes-and-complete-flat-end-germs-for-the-rational-port.md)、
[R391](R391-analytic-simple-degeneracies-and-complete-selected-inverse-germs-on-the-rational-circle.md)、
[R394](R394-conditional-complete-period-and-finite-same-gauge-interface.md)、
[R395](R395-independent-internal-fluxes-in-the-joint-pure-self-and-natural-kernel.md)。

## 1. 三个不同的原量

固定同一 R391 profiles、同右锚及一个实际简单点
$x_j\in J_i=(\ell_i,r_i)$：
$$
A_f(x_j)=0,\qquad f'(x_j)\ne0.
$$
仍令 $\phi_\theta=f\cos\theta+g\sin\theta$，以
$$
V_\theta=V(f^2,\phi_\theta)
$$
记未添二阶 gauge 的原完整第四 period。

先不假设 $\pi V=0$，定义两个真实相位读出
$$
\mathsf V_d(V)=V(f^2,g),\qquad
\mathsf V_e(V)=\frac12\left.\partial_\theta V_\theta\right|_{\theta=0}.
\tag{1}
$$
只有在 whole pure 零以后，才由 R159/R389 得
$V_\theta=\sin^2\theta\,\mathsf V_d+2\sin\theta\cos\theta\,\mathsf V_e$。
没有 pure 零时，(1)仍是两个准确原读出，但不能代表全部相位。

对 $b=d,e$ 定义
$$
H_{b,j}(V)=\int_{\ell_i}^{x_j}f'(x)\,\mathsf V_b(V)''(x)\,dx,
\qquad
B_{b,i}(V)=\mathsf V_b(V)''(\ell_i).
\tag{2}
$$
R345/R396 已用的读出则为
$$
\mathfrak F_j(V)
=H_{d,j}(V)
-\{f(x_j)-f(\ell_i)\}B_{d,i}(V).
\tag{3}
$$
这里 $f(\ell_i)=0$，但 $B_{d,i}$ 对一般成本未必零。故
$\mathfrak F_j=0$ 不能单独推出原必要量 $H_{d,j}=0$。

三者都是固定真实查询的线性泛函。这里没有把平台项视作可独立选取的常数。

## 2. 原未扣平台内部量可以直接实际联调

R395 的 $K_0,\ldots,K_{10}$ 在当前不交 rank-one 包上的整个输出都是紧支撑局部式。因此
$$
B_{d,i}(K_n)=0,\qquad
H_{d,j}(K_n)=\mathfrak F_j(K_n).
\tag{4}
$$
取原至多十一个同形对应点，(4)表明换成 H 后的响应矩阵仍是 R345 已付的同一个可逆矩阵。

所以 R396 的证明可从起点直接将额外查询替换为
$$
H_d=(H_{d,1},\ldots,H_{d,m}),\quad m\le11.
$$
其真实原型清 A 基准、整个复制基准、后置 A 截面成本和最后同一有限整数都保留。准确得到
$$
\boxed{
(P_{\mathscr L}E,\ A,\ H_d)(\mathcal S)
=\mathscr L\times\mathbb R^2\times\mathbb R^m,}
\tag{5}
$$
并有紧目标集上的实际 $C^1$ 截面。这里
$A=(\Lambda_{u_+},\Lambda_{u_-})$ 仍仅为 R390 的两条固定自然读出。

这不是宣称 R396 已经选出的某条路径会自动满足 H 目标；必须以 H 作为查询，重新解其同一个完整增强方程。旧 E 响应列上的 H 值与所有新增基准未知值均进入实际方程，而非只替换形式矩阵后删去它们。

(5)没有支付 whole E 或 $\Lambda_{\rm all}$。其原 $qE$ 基准仍是 R396(9) 的完整三项。特别若取 $H_d=0$，那么(3)给
$\mathfrak F_j=-f(x_j)B_{d,i}$，不能同时称二者已零。

### 2.1 这确是原 period 的不变量

R184/R225 的不除 $p=f'$ 身份为
$$
p(L_fk)''=\{A_f(pk''-f''k')\}'.
$$
从原平端 $\ell_i$ 积分到 $x_j$，两个边界都使右侧为零。因此任意允许光滑 k 均有
$$
\int_{\ell_i}^{x_j}p(L_fk)''=0.
\tag{6}
$$
不需要先假设其它平台或自然通量已经为零。

在真实 $T=\tau\mathfrak H$ 背景中，所有合法二阶 gauge 对 period 的改变为 $2\tau L_f(k_\theta)$，故(2)准确不变。特别，原 incoming $X=\Phi_{m_*}$ 与
$w_c=-XD_\theta$ 产生
$$
\mathsf V_d^c=\mathsf V_d-2\tau L_f(X\Delta),\qquad
\mathsf V_e^c=\mathsf V_e+2\tau L_f(X(f,g)),
$$
所以原 G 目标的两个内部量分别就是
$-H_{d,j}/(2\tau)$、$-H_{e,j}/(2\tau)$。真实入历史没有成为新的可选平台常数。

若按 R396 从起点嵌入固定非零 hook 基准，全部 H 基准也依原四副本规则一起扣除，(5)可实际置零这些原内部必要量。未付平台与端点条件仍可能阻止全局 inverse，不能只因(5)就授完整局部或全局解。

## 3. 当前十一维轨道对两个通道的准确范围

把所有真实复制展开为
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad
R_i=a_i^2-b_i^2,\quad T_i=a_ib_i.
$$
对选中包均有 $R_i\ne0$。R345 的完整局部式为
$$
K_n(f^2,\phi_\theta)
=-\frac13\sum_i a_i^2(a_i^2-c_i(\theta)^2)
P_n(x,u_i,u_i',u_i''),
\quad c_i=a_i\cos\theta+b_i\sin\theta .
$$
在同一个点取(1)、(2)，直接得到
$$
\boxed{H_{e,j}(K_n)=-\frac{T_i}{R_i}H_{d,j}(K_n).}
\tag{7}
$$
这没有先用 $\pi V=0$；对这些 $K_n$ 是完整原式。

因而定义真实余行
$$
\boxed{\mathcal C_j(V)=R_iH_{e,j}(V)+T_iH_{d,j}(V).}
\tag{8}
$$
整个 $\mathscr K=\operatorname{span}(K_0,\ldots,K_{10})$ 都被(8)杀掉。在 m 个所选对应点上，前 m 列的像准确是
$$
\{(h_j,-T_i h_j/R_i)_j:h\in\mathbb R^m\}.
\tag{9}
$$
所以相对于这一个已付响应模块，双通道的余商可用 $\mathcal C=(\mathcal C_j)$ 完整表示。恒等变换
$$
(H_d,H_e)\longleftrightarrow(H_d,\mathcal C)
$$
可逆。此处 m 只描述该模块的商坐标数，不断言这些行在整个 U 或全部响应上独立。

## 4. whole E 零时，余行只看真实 ordered suffix

本节明确另假设原
$$
\boxed{E(V)=0.}
\tag{10}
$$
它不是(5)的自动后果。下面不使用 $\Lambda_{\rm all}=0$。

沿 R394，以原 self 和 ordered 输出定义
$$
s_i(x)=\int_{\ell_i}^x u_i'S_i'',\qquad
\mathfrak a_i(x;n)=\int_{\ell_i}^x u_i'\mathscr U_i(\,\cdot\,;n)''.
$$
$\mathscr U_i$ 是原右方二阶三矩尾经完整第三 Range 与第四 period 的真实输出；它对右矩 n 线性，保全部 s-history 和原初值，不是局部 jet 模型。

由(10)，各原左二次尾准确成为仿射尾；不是置零。其它 outer 包在 $J_i$ 上的二阶导于是零。R394 原两式给
$$
H_{d,j}=a_i^3\left[
R_i s_i(x_j)+
\mathfrak a_i\!\left(x_j;\sum_{k>i}R_k\mu_k\right)\right],
$$
$$
H_{e,j}=-a_i^3\left[
T_i s_i(x_j)+
\mathfrak a_i\!\left(x_j;\sum_{k>i}T_k\mu_k\right)\right],
\tag{11}
$$
其中 $\mu_k=\mu(u_k)$ 是含原 $2u'v'$ 的全部三个真矩。

代回(8)，self 精确相消：
$$
\boxed{
\mathcal C_j(V)=a_i^3\,
\mathfrak a_i\!\left(
x_j;\ n_i\right),\qquad
n_i=\sum_{k>i}(T_iR_k-R_iT_k)\mu_k.}
\tag{12}
$$
右侧保真实方向与全部后续包的权，并不只保一个裸 cell 的均值。一般点上的 $n_i$ 不必为零；即使全部自然总通量为零，也只能消相应整包终值，不能据此删除内部(12)。

因此在(10)下、选中点且 $R_i\ne0$ 时，两条原内部门准确等价于
$$
H_{d,j}=0,\qquad \mathfrak a_i(x_j;n_i)=0.
\tag{13}
$$
第一条已有(5)的实际方向，第二条是本局部模块确切不能改变的 ordered 读出。没有把它宣布为整个响应空间的障碍。

## 5. 一类实际可用的首、末包使 suffix 准确为零

将原实际支持按从左到右分成连续块 $\mathcal B_\nu$。本节使用的“cell”是十二包装中的每个**完整八副本块**，包括其全部最细包，而不是编码中的单个裸格点组。需要并确实保留
$$
\boxed{
\sum_{i\in\mathcal B_\nu}R_i\mu_i=0,\qquad
\sum_{i\in\mathcal B_\nu}T_i\mu_i=0.}
\tag{14}
$$

来源链如下。

- R280 §6—8 的八/十二包装与五个最终块，各用完整三矩闭的 circle；其独立副本的 inner 三矩确为零。R324 §6、8、9 明确在有理芽构造中保留同一个实际副本库及这些三矩。
- R391 §1、4 中，一个基本包的全部副本同步改变形状，且 $\mathcal F_{\rm rat}$ 逐基本包保全部三个二次矩。于是(14)在最终有限 N、有限纠正和简单退化选择之后仍准确成立。
- 所有共同幅度、平移、正伸缩和整块 g 翻号都按实际权作用。对 $\widetilde u(x)=\rho u((x-d)/H)$，真矩为
$$
\widetilde\mu=\rho^2
\begin{pmatrix}
H^{-3}&0&0\\ dH^{-3}&H^{-2}&0\\
d^2H^{-3}&2dH^{-2}&H^{-1}
\end{pmatrix}\mu .
\tag{15}
$$
其第三行包含 $2\int(u')^2$ 的真实输运。故每个已零向量保持为零；g 翻号只使 T 权同号翻转，R 不变。最后五块的正四次幅权取正四次根后，同样不破二次闭合。

特别，选中 cell 之后的**所有**完整 cells、同最终块其余包装及更右的最终块，都满足(14)。因此若 i 是该 cell 的第一个最细包，
$$
\sum_{k>i}R_k\mu_k=-R_i\mu_i,\qquad
\sum_{k>i}T_k\mu_k=-T_i\mu_i;
$$
若 i 是其最后一个最细包，两向量都为零。两种情形均有
$$
\boxed{n_i=0,\qquad\mathcal C_j(V)=0\ \text{在(10)下}.}
\tag{16}
$$
这是完整三向量恒等；没有把 cross 中的同尾常数改成自由参数。

可以在同一最终 block 的十二个已有完整 cells 中，选同一个首微包的 $m\le11$ 个真实对应点。形状相同，完整共同幅度非零，g 的整块翻号保留在 $b_i$ 内；R345 的同形对应点矩阵继续适用。不能误称十一个点都来自只有八个成员的单一八包装。

因此，**若同一实际对象另已联合满足 whole E 零**，在这些点支付 $H_d$ 也支付 $H_e$。这一条件性加强不把当前(5)的响应 E 投影升级为 whole E。

还有一个必须与(5)分开的实际推论。R345 §8—9 已给 $(E,\mathfrak F)$ 的整个实际截面。对现在固定的这些首包对应点，取其 whole E 与全部 $\mathfrak F$ 为零；由(3)、(10)、(16)，同一实际新几何满足
$$
\boxed{E=0,\qquad H_{d,j}=H_{e,j}=0\quad(1\le j\le m).}
\tag{16a}
$$
该构造保同一 profiles、原低阶 hook 与全部真实基准，却没有同时指定 R390 的两条 A。相反，(5)指定两条 A，却只指定响应 E 分量。不能把这两个分别存在的实际路径拼成一个未经证明的联合零解。两条结论均不支付其它内部点与全部自然总通量。

## 6. 在现有实际截面下，剩余代价是什么

对上述首、末包，(16)表明线性读出 $\mathcal C_j$ 在 $\ker E$ 上为零。因此它经有限真实像 E(U) 因子化：
$$
\mathcal C_j=\ell_j\circ E.
\tag{17}
$$
这只是准确线性因子化，不为 $\ell_j$ 指定一个未经评价的数值，也不授新满秩。

依 R396 从起点选定的分裂 $E(U)=\mathscr L\oplus\mathscr C_*$，可写
$$
\mathcal C_j(V)=\ell_j(F(V))+\bar\ell_j(qE(V)).
\tag{18}
$$
若在(5)中取 $F=0$，这些配对门的唯一余值就是(18)的真实 qE 分量。它们没有被两个固定 A 或局部 K 列消掉。

同理，原平台读出 $B_{b,i}$ 在 whole E 零时为零，故也是 E 的真实线性读出。它解释了(3)与 raw H 的差距为何仍是未付 E 基准的一部分，而不是可以忽略的规范常数。

对一般内部微包，(12)并未消失；需要的是同一个成本上的具体映射
$$
V\longmapsto
\left(F(V),A(V),H_d(V),\mathcal C(V)\right),
\tag{19}
$$
其中已付局部模块只提供(9)的图像。若使用首、末包，(19)中新增余行退化为(18)的一组原商读出；一般包则保完整(12)。两种范围都不能只靠把更多函数塞进一个 F 记号就称已实际可控。

本稿完成了 raw 内部必要量的真实联调，以及双 period 同点余差的准确消 self 与 cell 边界归约。它未支付 remaining qE、全部自然总通量、未选中的内部点、仿射平台/端 germ、R394 的 k 值闭合和十三行同规范解；更没有给不同相位另选 gauge 后拼成全局解。
