# R1000 — 同 degree238 的五条无条件零、实际五轴校准与全位余式

日期：2026-11-26 UTC。**已证明：R996 新两基点格内有五条同 degree238、同 charge119 的完整原来源，其惰性中央导数无条件为零，前五 jet 矩阵准确为三角单位阵。它们的完整中央 family 因而在每个当前好惰性位给一个全精度整解析坐标，不需要先假设任何 rank≥2 canonical 中央失败。**

本文把 R996 的两条新真零及全部原 canonical/old 来源放入这个实际校准，给同一六位 Schur 读者和明确非零的 old 剩余。还完整回代新 $31/195$ Hilbert 主项：它改善实际格维数，但本身不改变全位严格门 $a+2b<3$。所有比较仍在同一来源整数像格、实际 Taylor 旗标和原有序目标中。

## 1. 同一个 degree238 中的五条实际零来源

沿 R996 固定

$$
\delta^2=-3,\quad\gamma=(5+\delta)/2,\quad
X=x^3,\quad\Theta=x\sigma^2,\quad t=-X^{-1},\quad w=z^6,
$$

$$
A=A_\gamma=X^2+(20-24\delta)X-8-24\delta,
\qquad Q=\gamma X-2+2\delta.
\tag{1}
$$

此处 $Q=\gamma R_\gamma$，不是 R996 的 $t(t-1)$。对 $1\le r\le5$ 定义完整 degree34 下层来源

$$
g_r=\sigma^{34}x^{17-3r}=\Theta^{17}(-t)^r
=w^r+O(w^{r+1}).
\tag{2}
$$

$17-3r=14,11,8,5,2$，所以每条均 whole、principal、质量零。置

$$
c_r=\gamma^{6r}-\bar\gamma^{6r},\qquad
\boxed{H_r=\frac{D_\gamma g_r-D_{\bar\gamma}g_r}{c_r}.}
\tag{3}
$$

$c_r\ne0$，因为 $\gamma/\bar\gamma$ 不是根单位。完整原 norm7 恒等式给

$$
\boxed{H_r=\sigma^{238}x^{17-3r}P_r(X),\qquad
P_r=\frac{A^{17-3r}Q^{6r}-\bar A^{17-3r}\bar Q^{6r}}{c_r}.}
\tag{4}
$$

全部五条的 degree 都是238，charge 都是119。$\deg P_r=34$、首系数一，所以准确有

$$
\boxed{H_r=w^r+O(w^{r+1}).}
\tag{5}
$$

共轭交换分子两项及 $c_r$ 的符号，故所有系数有理。固定清分母可准确指定如下：令

$$
U_0=0,\quad U_1=1,\quad
U_{j+2}=-286U_{j+1}-117649U_j.
\tag{6}
$$

因为 $\gamma^6+\bar\gamma^6=-286$、$\gamma^6\bar\gamma^6=7^6=117649$，有
$c_r=360\delta U_r$。$A,Q\in\mathcal O_K[X]$ 且反共轭系数除以 $\delta$ 为整数，所以

$$
P_r\in(360U_r)^{-1}\mathbf Z[X].
\tag{7}
$$

以下另删固定 $360\prod_{r=1}^5U_r$ 的素因子，并保全部原坏集。该有限集合先于 $p$ 固定，不把某个随 $p$ 选的 minor 当作单位。

### 1.1 五源全部在 R996 的同一完整格内

其完整角式为

$$
H_r=\Theta^{119}h_r(t),\qquad
h_r(t)=(-t)^{34+r}P_r(-1/t).
\tag{8}
$$

因此 $\deg h_r\le34+r\le39$、$\operatorname{ord}_0h_r=r$。在 $X=-1$，R996 的准确值
$A=\bar A=-27$、$Q=-3\delta\omega^2$、$\bar Q=3\delta\omega$
使 $Q^{6r}=\bar Q^{6r}$，故 $h_r(1)=0$。所以五条完整来源都属于

$$
\boxed{B^{(8)}_{119}=\Theta^{119}t(t-1)R[t]_{\le37},}
\tag{9}
$$

其中 $\lfloor64\cdot119/195\rfloor=39$。没有省略最高列或临时扩大角帽。它们可按 R996 的同一 $c_8$ 整返回，不改变规范化或 Hilbert 主项。

### 1.2 无条件完整惰性二重零

固定好 $p=6s-1>211$，$d=p+1$、$c=[w^s]\log(\sigma/z)$。同一 raw pull 插值给

$$
\boxed{J_{H_r,p}(v)=
\frac{(\gamma^d/7)^v-(\bar\gamma^d/7)^v}{c_r}
J_{34,g_r,p}(v).}
\tag{10}
$$

两个底数都在 $1+p\mathcal O$；$g_r(0)=0$。因此

$$
\boxed{J_{H_r,p}\in v^2\mathcal O\langle v\rangle
\quad(1\le r\le5).}
\tag{11}
$$

R602 的 Hurwitz 证明适用(2)、(4)，故(10)是真限制 Tate 身份，未把整数插值形式地当作解析延拓。本节只使用惰性范围；没有为下层整个 $\mathcal S_{34}$ 另猜 ordinary core。

## 2. 五条真零给全精度的实际整解析坐标

保持 R989 的同一实际高轴坐标 $x=A-A^*$、

$$
\eta_x=\sum_{j=1}^5x_jt^{s-j},\quad
\kappa=34c,\quad a=p\kappa\in\mathcal O^\times,
\quad q_H=119/17=7.
\tag{12}
$$

所有五条都用相同 family $H_{r,x}=H_r e^{7\eta_x}$，没有按行改 Gaussian。定义完整、未截断的

$$
\mathcal F_r(x)=\frac ap J'_{H_{r,x},p}(0),\qquad
\mathcal F=(\mathcal F_1,\ldots,\mathcal F_5)^t.
\tag{13}
$$

具体地，若 $P_r=\sum_{j=0}^{34}p_{r,j}X^{34-j}$，则完整 regularized inner 是

$$
B_{H_r,x}=w^{-1}H_r e^{-7\kappa w^s}e^{7\eta_x}
=f^{-119}\sum_{j=0}^{34}p_{r,j}
 w^{r+j-1}W^{119-3r-3j}e^{7\eta_x}.
\tag{13a}
$$

所有 $w$ 幂非负，最小 $W$ 幂为 $17-3r\ge2$。所以 R989 的完整整 Hurwitz 界逐个变量系数适用，实际为

$$
v_p\left(\frac ap(h-1)!(7\kappa)^{-h}
[w^{hs-1}]B_{H_r,x}\right)
\ge\left\lceil\frac{h(5p-7)+6}{6(p-1)}\right\rceil-1
  +v_p((h-1)!).
\tag{13b}
$$

每个 $h$ 的系数是有限 $x$ 多项式，而(13b)对全部系数成立且随 $h$ 趋于无穷。因此完整和(13)属于
$\mathcal O\langle x_1,\ldots,x_5\rangle^5$，不是仅在每个数值 $x$ 上收敛的形式 family。所有 $h\ge2$ 的 Newton 导数项在乘 $a/p$ 后仍含 $p$；$h=1$ 中 $\eta_x^2$ 的首阶大于目标 $s-1$，因 $s>35$。因此模 $p$ 它是仿射函数。

令

$$
B_H=([w^5]H_r,[w^4]H_r,[w^3]H_r,[w^2]H_r,[w]H_r)_{r=1}^5.
\tag{14}
$$

由(5)，反序列后的这个矩阵是三角矩阵，反序符号
$(-1)^{5\cdot4/2}=1$，故

$$
\boxed{\det B_H=1.}
\tag{15}
$$

原 $t\to w$ 的同一个三角矩阵 $T$ 对角为 $\pm1$。所以模 $p$ Jacobian 为 $B_HT$，是单位。由(11)，$\mathcal F(0)=0$ 准确成立，故可写

$$
\boxed{\mathcal F(x)=Vx+pG(x),\qquad
V\in\mathrm{GL}_5(\mathcal O),\quad
G\in\mathcal O\langle x_1,\ldots,x_5\rangle^5,\quad G(0)=0.}
\tag{16}
$$

这里 $V$ 可取(14)乘同一个实际 $T$ 的整提升；没有按目标选择不同的坐标。

**准确结论。** $\mathcal F:\mathcal O^5\to\mathcal O^5$ 是整解析双射，且

$$
\boxed{\min_i v_p(\mathcal F_i(x)-\mathcal F_i(y))
=\min_i v_p(x_i-y_i).}
\tag{17}
$$

证明用整 Tate 函数的一致1-Lipschitz性：$p(G(x)-G(y))$ 比 $x-y$ 多一位，而 $V$ 为单位矩阵。给定目标 $z$，方程
$x=V^{-1}(z-pG(x))$ 是严格压缩，唯一解即得双射；逐级 Hensel给同一结论。于是对每个 $N\ge1$，

$$
\boxed{\mathcal F(x)\equiv0\pmod{p^N}
\quad\Longleftrightarrow\quad x\equiv0\pmod{p^N}.}
\tag{18}
$$

这是五条无条件真来源固定的实际点，不先假设五条 canonical 坏中央。若在原绝对 $A$ 坐标中计算，其唯一零点就是 $A^*$。

## 3. 两条新 norm7 行及所有原目标的准确 Schur 剩余

令 $F$ 是任一已付质量零完整来源，保持它自己的 charge $q_F$ 和完整 Gaussian。置

$$
b_F=([w^5]F,\ldots,[w]F),\quad
c_F=b_FB_H^{-1},\quad
\mathcal R_F(x)=\frac apJ'_{F_x,p}(0)-c_F\mathcal F(x).
\tag{19}
$$

全部 $c_F$ 由固定来源的前五 jet 唯一指定，$T$ 被同一右逆消去，故 $c_F$ 不随 $p$ 任意改选。式(19)模 $p$ 的全部高轴一次项恰消失，因而

$$
\mathcal R_F(x)-\mathcal R_F(y)
\in p\sum_{i=1}^5(x_i-y_i)\mathcal O
\tag{20}
$$

右边是各坐标差生成的标量理想。特别，若 $x_5$ 是五条无条件行的任何模 $p^5$ 零点的整提升，则(18)给 $x_5\equiv0\pmod{p^5}$，并且

$$
\boxed{\mathcal R_F(x_5)
\equiv\frac apJ'_{F,p}(0)\pmod{p^6}.}
\tag{21}
$$

各项可全部用 R989 的完整六项读者取代；原五条校准行同样读到第六位。三角单位阵(15)使这一 Schur 消去不产生未知第六提升或新除 $p$。

对 R996 的 $\mathcal X_{42},\mathcal X_{70}$，右边无条件为零，得到两条完整的同点六位恒等式。对原十条 canonical，只有在各自中央坏的假设下才将右边赋零。原 R992 的 $\mathcal X_{130}$ 同样无条件为零。所有行使用同一个 $x_5$；没有将不同 Hensel 点的余式拼接。

### 3.1 第一位的固定 whole 余式

令 $\mathcal E=\vartheta\partial_\vartheta/17$。同一来源中的

$$
\Delta_F=F-\sum_{r=1}^5c_{F,r}H_r\in w^6K[[w]],
$$

$$
\boxed{Q_F=\mathcal E^{-1}\Delta_F
=\frac F{q_F}-\frac{1}{7}\sum_{r=1}^5c_{F,r}H_r}
\tag{22}
$$

均为准确全函数，不是 jet 代替整源。逆只在这些固定非零权上取，当前 $p$ 下为单位。模 $p$ 的(19)准确是

$$
\boxed{\mathcal R_F(x)\equiv[w^s]Q_F\pmod p,}
\tag{23}
$$

并与 $x$ 无关：$\mathcal EQ_F=\Delta_F$ 从 $w^6$ 起，乘从 $w^{s-5}$ 起的高轴扰动后首次影响为 $w^{s+1}$。不同 charge 的全部因子已在(22)显示；不能把它改成 $\Delta_F/q_F$。

若需要把 $\Delta_F$ 的高起阶与中央线性同时读取，准确使用 R982 的公共读者：固定 $N_0$，对每个实际 theta degree $N_i$ 乘
$(N_i/N_0)^{(p-1)v}J_i((p-1)v)$。在稠密整数处这是同一个全函数系数读取，所有质量零使零处导数等于 $(p-1)\sum_i a_iJ_i'(0)$。本篇没有把这份跨 charge 读者认作单一 Gaussian 的第六 Cartier 输入。

### 3.2 明确非零的原 old 目标

R978 的准确原有理来源为

$$
R_{\rm old}=F_{10}+\frac{11}{2}\Phi_*
=\frac\delta{10080}\Delta_{125},\qquad
\Delta_{125}=D_{\pi_{13}}\Psi_{125}-D_{\bar\pi_{13}}\Psi_{125},
\quad\pi_{13}=(7+\delta)/2.
\tag{24}
$$

它在 $B^{(6)}_{65}\subset B^{(8)}_{65}$ 中，首项 $(13/2)w$。R978 已证明对每个当前惰性 $p$，

$$
\boxed{\mathcal R_{R_{\rm old}}(0)
=\frac{a\delta(p+1)}{10080p}
\log_p(\pi_{13}/\bar\pi_{13})\ne0.}
\tag{25}
$$

式(21)把同一个非零值准确接入六位余式。它不声称该值模 $p^6$ 一定非零；也没有从(19)给 $F_{10}$ 或任何原 mixed 项赋零。

## 4. 这个非零对照的有限精度上界与真正输入窗

这一节给全 $p$ 的确定深度，不用有限素数扫描。置
$\alpha=\pi_{13}/\bar\pi_{13}$。惰性位上 $\alpha^{p+1}\in1+p\mathcal O$，且 $p+1$ 是单位，所以

$$
v_p\log_p\alpha
=v_p(\pi_{13}^{p+1}-\bar\pi_{13}^{p+1}).
\tag{26}
$$

差是 $\delta B_p$，$B_p\in\mathbf Z\setminus\{0\}$；非零由 $\alpha$ 不是根单位。复绝对值直接给

$$
|B_p|\le\frac2{\sqrt3}\,13^{(p+1)/2}.
$$

因此定义整数

$$
\boxed{L_p=\left\lfloor
\frac{(p+1)\log13}{2\log p}
 +\frac{\log(2/\sqrt3)}{\log p}\right\rfloor,}
\tag{27}
$$

便有 $1\le v_p\log_p\alpha\le L_p$。特别(25)的赋值不超过 $L_p-1$，故其模 $p^{L_p}$ 必非零。对 $p>211$，还可统一用
$L_p\le\lfloor(p+1)/4\rfloor$：比较
$(p/169)^{(p+1)/4}>2/\sqrt3$ 即得，最左端随 $p$ 增长，在211时用 Bernoulli不等式已严格成立。

这份深度可以在 R614 的**另一个更长但已付的完整整窗**中读取。置 $h_0=(p-1)/2$。保持原五轴扰动，$1\le h\le h_0$ 的 inner 目标 $hs-1$ 均小于
$L_0=s(p-1)=(p^2-1)/6$。到这一次数，指数扰动的幂 $j$ 满足

$$
j\le\frac{hs-1}{s-5}
<\frac{p^2-1}{2(p-29)}<p
\qquad(p>211).
\tag{27a}
$$

故所用 $j!$ 都是单位；由 R614 的原 $W,f$ 整窗及非负幂，完整 inner 系数确实整。其第 $h$ 个归一导数项至少含 $p^{h-1}$。对全部 $h\ge h_0+1=(p+1)/2$，则使用 R989 的强 Hurwitz 界，而不再把指数阶乘一律当作单位：

$$
v_p\left(\frac ap(h-1)!(q\kappa)^{-h}C_h\right)
\ge
\left\lceil\frac{h(5p-7)+6}{6(p-1)}\right\rceil-1
>\frac{p+1}{4}\ge L_p.
\tag{28}
$$

最后一个严格界在首端点 $h=(p+1)/2$ 已成立：用 $\lceil u\rceil\ge u$ 后，只须 $2p^2-14p+20>0$；随后随 $h$ 单调增加。
所以 $L_p<h_0$，且 $L_p+1\le h\le h_0$ 的项由整性至少含 $p^{L_p}$，所有 $h>h_0$ 的项由(28)处理。保留 $1\le h\le L_p$ 已准确读取(25)模 $p^{L_p}$。最高实际输入为 $w^{sL_p-1}$，仍严格在 R614 完整窗内。

这里没有扩大原 $\Gamma_L^{(6)}$：当 $L_p>6$ 时这是另一份明确较长的 coefficient 读取，不能冒作原六块的第七或更后物理行。重生这些更长系数时，原递推遇到的每个真实除 $p$ 都必须重新按其整窗支付；没有把 R941 到 $w^p$ 的“两次除 $p$”免费沿用到(28)。

## 5. 新 Hilbert 主项在完整全位不等式中的准确位置

用 R996 的八源环，或再加入本篇五条及原四新 canonical、$\mathcal X_{130}$ 后的环，全部夹在同一
$A^{(8)}\subset A\subset B^{(8)}$ 内。固定局部化只增加各来源的已显示分母；仍有同一导子 $c_8$。对实际权上界 $N=M+69615$，取全部合法源单项式的整数像格 $\Lambda_M$，实范数为完整呈示的 Euclidean 商范数，有限处为同一个整数像格的 gauge。于是

$$
\boxed{n_M=\operatorname{rank}\Lambda_M
=\frac{31}{195}M^2+O(M+1).}
\tag{29}
$$

饱和旗标仍是
$K_{M,k}=\Lambda_M\cap\ker(r_0,\ldots,r_{k-1})$、$r_k=[w^k]$。
R957 的同一逐跳跃乘积公式继续给

$$
0\le\sum_{i=1}^{n_M}\sum_v
\log\|r_{k_i}|_{K_{M,k_i}}\|_v.
\tag{30}
$$

所有来源的角次数都小于权的三分之一，实际原点阶正，故新全纯 Cauchy、ordinary 整测度和惯性闭内盘的完整估计分别仍为

$$
\log\|r_k\|_\infty
\le-3k\log k+3k\log(M+1)+O(k+M+1),
$$

$$
\log\|r_k\|_p\le0\quad(p\text{ ordinary}),\qquad
\sum_{p\equiv5(6)}\log\|r_k\|_p
\le3k\log k+O(k+M+1).
\tag{31}
$$

普通估计只需原有界 Amice 整性，不要求本篇五条的 ordinary 中央为零。全部加法卷积仍先完成再切总和单位域。新固定分母、69615导子和 $5r_8$ 跨界只进入已付的低阶项。

若真正中央失败进一步给同格、全 $M,k$ 的

$$
\sum_{p\equiv5(6)}\log\|r_k\|_p
\le a k\log(M+1)+b k\log k+O(k+M+1),
\tag{32}
$$

则仍须 $a+2b<3$。准确地，$S_M=\sum_i k_i\ge n_M(n_M-1)/2$，且

$$
\sum_i k_i\log k_i
\ge S_M\log(S_M/n_M)
\ge S_M\left(2\log(M+1)+\log\frac{31}{390}+o(1)\right).
\tag{33}
$$

新常数31代替旧30，只在(33)增加 $S_M\log(31/30)+o(S_M)$；它没有改变 $2\log M$ 的系数。当 $b<3$ 时，完整主项仍是
$(a+2b-3)S_M\log(M+1)$。当前无条件(31)为 $(a,b)=(0,3)$，所以(29)本身不足产生严格矛盾。

这不是忽略新真实输入：新增的五条无条件同 charge 行已给(17)–(23)的实际校准和两条新真余式；原明确非零方向则是(25)，并有(27)–(28)的确定检出深度。后继要在这些**同一**已指定读者中将 canonical 坏条件真正连到(25)，或对(32)支付全 $M,k$ 的损益。不能把校准矩阵的单位 Jacobian 当作 $\Gamma_L^{(6)}$ 的深核。

## 6. 原六块与全部有序前缀保持的范围

若 $x_6$ 满足五条实际校准式模 $p^6$，(18)无条件给 $x_6\equiv0\pmod{p^6}$。因此对 R996 新整数格的整个评价

$$
P\longmapsto P\left(t(w),h_{x_6}(w)
\exp(a\epsilon/17)\right)
$$

在原
$\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^6,w^\ell\epsilon^5,p^6)$
上与实际点逐行相同。所有低权、完整来源列、每个有序前缀均保持；经过 $c_8$ 时仍使用原长目标及 $r_8=r_c+16$，不删 $5r_8$ 费用。

这里的确定点不再需要旧五 canonical 坏条件。原十条 canonical 若同时坏，只额外使其同点剩余(21)为零；新 norm7 来源、归一化参数的幂、所有 mixed cut 与全部 Cartier $P_2/Z$ 缺陷没有被删掉。本文不从任何单独来源的中央零传播乘积零，也未证明无穷素数主目标。

## 依赖

- R996：两个 norm7 原相位、新两基点规范化、全整数格与导子。
- R989：同一五高轴、整 Hurwitz 系数界、六位完整 Schur 和 ordered 前缀。
- R614：完整 $w<s(p-1)$ 整窗；本篇(28)明确区别于原六块。
- R978：有理 old 来源(24)及完整非零对数。
- R957/R960/R982：真实整数像格、全部位、跨 charge 公共读者与原严格门。

本篇全部新固定来源、单位行列式、解析校准及对数深度由显示公式手证，没有新增数学运行或生成数据文件。
