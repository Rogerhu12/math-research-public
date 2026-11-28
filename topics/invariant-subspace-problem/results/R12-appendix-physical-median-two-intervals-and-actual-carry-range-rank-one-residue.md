# 原 Walsh 中位双区间、完整进位的实际值域与一维余项

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。作者：stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：完整证明。** 本稿继续[统一中位间隙与迹类极化](R12-appendix-uniform-walsh-root-median-gap-and-trace-class-physical-polarization.md)，先把真实中位投影写成两个明确整数区间，再对完整原 $K$ 支付实际 $C$ 除法的来源。结论是自然域恰为一个明确闭超平面，并构造有界同源原像；没有把 $\overline{\operatorname{Ran}C}$ 当作 $\operatorname{Ran}C$。

始终固定同一原 Haar 尾 $C=A^{(m)}=D+K$、$a_j=\alpha_{m+j}$。所有 $u_j,v_j,\mu_j,\delta_j$ 及完整跨块、常数列沿用[原全 Walsh 块](R12-appendix-actual-walsh-block-trace-class-carry-and-closed-diagonal-roots.md)：
$$
u_j=q_{j,0},\quad v_j=q_{j,2^j-1},\quad
\mu_j=(a_j+\mu_{j+1})/2,\quad
\delta_j=(a_j-\mu_{j+1})/2=\mu_j-\mu_{j+1}.
\tag{1}
$$
特别 $u_0=v_0$；它与 $\Omega$ 仍为不同的正交向量。以下不省略这个首块。

## 1. 中位集合的两个准确整数区间

记前稿两个互补固定字为 $u_-,u_+=1-u_-$，
替换为 $0\mapsto0111,\ 1\mapsto1000$。本节的小写实数 $u_\pm$
与原向量 $u_j$ 区分。沿用
$$
q=h_8(u_-)-3/7,\quad
17/840\le q\le10511/430080,\quad
c=21/(20\,2^m),\quad t_\varepsilon=(2\varepsilon+1)/4.
$$
令 $N=2^L$，$L\ge20$，定义
$$
k^-_{L,\varepsilon}=\left\lceil Nu_--t_\varepsilon+cq\right\rceil,
\qquad
k^+_{L,\varepsilon}=\left\lceil Nu_+-t_\varepsilon-cq\right\rceil.
\tag{2}
$$
则前稿两物理分量的中位选择**恰为**
$$
\boxed{\quad
I_{L,\varepsilon}
=[k^-_{L,\varepsilon},N/2-1]\ \cup\
[k^+_{L,\varepsilon},N-1].
\quad}
\tag{3}
$$
区间均取整数。此处是有限行的准确身份，不是概率极限。

证明需要一个前稿未用到的比较。
两个固定字的相同数字连续段至多长 $4$：
块内部最长 $3$，跨两个块最多为 $3+1$ 或 $1+3$。
因而任意二进制移位尾都位于 $[1/32,31/32]$。
若 $u$ 与同半区的 $u_\sigma$ 首次在第 $n\ge2$ 位不同，
则
$$
|u-u_\sigma|\ge2^{-n-5},\qquad
|f_{16}(u)-f_{16}(u_\sigma)|\le16^{1-n}/15
\le(8/15)|u-u_\sigma|.
$$
所以 $h_{16}(u)-7/15$ 与 $u-u_\sigma$ 同号，且
$$
|h_{16}(u)-7/15|\ge(7/15)|u-u_\sigma|.
\tag{4}
$$
若 $|k-Nu_\sigma|\ge3$，前稿精确中心式 (4) 的主项至少为 $7/5$，
其余项绝对值小于 $3/4+9/20+4\,2^{-L}<7/5$；
原中心行和
$k-Nu_\sigma+t_\varepsilon-c(h_8(u_\sigma)-3/7)$ 同号。
若 $|k-Nu_\sigma|<3$，上述首次差位界迫公共前缀至少长 $L-7$；
前稿 (13)–(15) 的同一误差于是仍不超过 $140\,2^{-L}<1/1200$。
其 quarter 间隙至少 $1/600$，所以符号仍完全一致。
在两半区分别取 $\sigma=-,+$ 即得 (3)。

从 (2) 立刻得到
$$
F_L^{(0)}\le F_L^{(1)},\qquad
\operatorname{rank}(F_L^{(1)}-F_L^{(0)})\in\{0,2\}.
\tag{5}
$$
确切地，置 $x=Nu_-+cq$，两个端点的变化同时为一，
当且仅当 $\{x\}\in(1/4,3/4)$；端点相等情形已被前稿间隙排除。

## 2. 物理中位图的完整两条出流

在 $Q_LH\oplus Q_LH$ 上，取 $\mathcal B_{D_L}=\begin{pmatrix}0&D_L\\I&0\end{pmatrix}$，
及前稿的 $F_L=\operatorname{diag}(F_L^{(0)},F_L^{(1)})$。
由 (5)，恒等下左块没有漏出。
上右块中，(3) 的起点最多相差一个；原前向一步将每个起点送入相应上区间。
因此只有两条末端出流：
$$
\boxed{
(I-F_L)\mathcal B_{D_L}F_L
=\begin{pmatrix}
0&
a_{L-1}\,q_{L,N/2}\otimes q_{L,N/2-1}^*
-\mu_L\,u_L\otimes v_L^*\\
0&0
\end{pmatrix}.}
\tag{6}
$$
两项使用不同的原行、原列。正闭合已吸收头的第二项相应为 $+\mu_L$。
这没有把中间 $a_{L-1}$ 项并入更小的 $\mu_L$。

在全部高 Walsh 块上，完整原 $K$ 的跨块末列到首行仍全部保留：
对 $i\ne j$，
$$
K_{ij}=2^{-|i-j|/2}\delta_{\max(i,j)}\,u_i\otimes v_j^*.
\tag{7}
$$
所有高位 $u_i$ 都在 $F^{(0)}$ 外、$v_j$ 都在 $F^{(1)}$ 内，
故 (7) 整项进入漏角。低有限头及其交叉列若单独分组，是确切有限秩余项，
并没有从原方程删除。下面直接处理全部块和常数列，不再作这个分组。

## 3. 原末列空间、首行空间及完整矩阵

令
$$
X=\overline{\operatorname{span}}\{\Omega,v_0,v_1,\ldots\},\qquad
Y=\overline{\operatorname{span}}\{\Omega,u_0,u_1,\ldots\},\qquad
U=Y\ominus\mathbb C\Omega.
$$
两组所列向量分别为正交基。
令 $J_X(c,t)=c\Omega+\sum_jt_jv_j$、$J_Uy=\sum_jy_ju_j$，
以及 $r=2^{-1/2}$。

原全部块公式给
$$
C J_X(c,t)=d\Omega+J_Uy,
$$
$$
d=\mu_0c+\sum_jr^j\delta_jt_j,\qquad
y_j=-r^j\delta_jc+\sum_k M_{jk}t_k,
\tag{8}
$$
其中
$$
M_{jj}=-\mu_j,\qquad
M_{jk}=r^{|j-k|}\delta_{\max(j,k)}\quad(j\ne k).
\tag{9}
$$
$K=KP_X$ 且 $\operatorname{Ran}K\subset Y$。
此外，
$$
\boxed{\quad C^{-1}(Y)=X.\quad}
\tag{10}
$$
这里 $C^{-1}(Y)$ 指 $\{f\in H:Cf\in Y\}$，不是形式逆。
确实，每个非末列 $q_{L,k}$，$k<2^L-1$，
唯一输出内行 $a_{v_2(k+1)}q_{L,k+1}$。
没有其他列或 carry 输出到该内行。
若 $Cf\in Y$，这些坐标逐个为零；所有原权非零，故 $f$ 只能在 $X$ 中。
(8) 给反向包含。

## 4. 保原逆权的有界全行

置 $D_a=\operatorname{diag}(a_j)$，先在有限列定义
$$
B=D_a^{-1}M,\qquad b_j=-r^j\delta_j/a_j,\qquad
\mathcal A=[\,b,\ B\,]:\mathbb C\oplus\ell^2\longrightarrow\ell^2.
\tag{11}
$$
这些实际权除法延伸为有界算子，并有
$$
\boxed{\quad
\mathcal A\text{ 有界可逆},\quad
\|\mathcal A\|\le1,\quad\|\mathcal A^{-1}\|\le2.
\quad}
\tag{12}
$$

以下证明同时核全部交叉行与扰动常数。
令 $S$ 为 $\ell^2(\mathbb N_0)$ 的单边右移，
$T_r=rS(I-rS)^{-1}$，$g=(r^j)_{j\ge0}$。
比较的全行是
$$
B_0=-\tfrac12I+\tfrac12T_r
=r(S-rI)(I-rS)^{-1},\qquad
b_0=-g/2,\qquad
\mathcal A_0=[\,b_0,B_0\,].
\tag{13}
$$
由 $S^*S=I$ 直接乘回，
$(S-rI)(I-rS)^{-1}$ 是等距；
其像的正交补恰为 $\mathbb Cg$。
又 $\|b_0\|=r$，所以 $\mathcal A_0$ 是 $r$ 倍酉，
是从 $\mathbb C\oplus\ell^2$ 到 $\ell^2$ 的真正双射。

原相邻权满足
$$
-\log(a_{j+1}/a_j)
=1400\,16^{m+j}-630\,8^{m+j}+300\,2^{m+j}
\ge1070\,2^{m+j}.
$$
写 $s=e^{-1070}<1/1000$、$\rho_j=a_{j+1}/a_j$，则
$\rho_j\le s^{j+1}$、$\sum_j\rho_j\le s/(1-s)$。
令 $e_j=\mu_{j+1}/(2a_j)\le\rho_j/2$。
原下三角及对角准确给
$$
B-B_0=-\operatorname{diag}(e_j)(I+T_r)+V,
$$
其中唯一上三角余项为
$$
V_{j,j+k}=r^k\delta_{j+k}/a_j,\quad k\ge1,\qquad
|V_{j,j+k}|\le\tfrac12r^k\rho_js^{k-1}.
\tag{14}
$$
所以 $V$ 的全部矩阵元绝对和至多
$\frac{r}{2(1-rs)}\,\frac{s}{1-s}$。
又 $\|I+T_r\|\le(1-r)^{-1}<4$，
$b-b_0=(e_jr^j)_j$。
这些式给严格的矩形迹范数界
$$
\|\mathcal A-\mathcal A_0\|_1\le8s.
\tag{15}
$$
没有只检查对角或删去上三角。
因 $r-8s>1/2$、$r+8s<1$，
对 $\mathcal A_0^{-1}(\mathcal A-\mathcal A_0)$ 作有界 Neumann 反演即得 (12)。

由 (11) 的有界延伸，原输出关系对全部 $(c,t)$ 成立：
$$
y=D_a\mathcal A(c,t).
\tag{16}
$$
特别不是先假定 $D_a^{-1}y\in\ell^2$ 再忽略来源；这里对整源已实际支付它。

## 5. 精确值域与同源费用

原有 $\sum_j\delta_j=\mu_0$。由 (9)，逐个有限列可核
$$
\sum_i r^{-i}M_{ij}=-r^j\delta_j.
\tag{17}
$$
其中 $i<j$ 的有限和为
$\delta_j(r^{-j}-r^j)$，$i>j$ 的尾和为 $r^{-j}\mu_{j+1}$，
再加对角即为 (17)。
因此 (8) 的全部输出满足
$$
d=-\sum_jr^{-j}y_j.
\tag{18}
$$
该和绝对收敛：由 (16)，$y=D_az$、$z\in\ell^2$，
而 $(a_jr^{-j})_j\in\ell^2$。
(17) 先在基列核实后，以这一实际连续泛函延到全部源，未把形式无界列当作 Hilbert 向量。

反过来，任给 $y=D_az$、$z\in\ell^2$，
取同一实际源 $(c,t)=\mathcal A^{-1}z$。
(8)、(18) 返回准确目标。结合 (10)，得到
$$
\boxed{
\operatorname{Ran}C\cap Y=CX
=\left\{d\Omega+\sum_jy_ju_j:
\sum_j|y_j/a_j|^2<\infty,\quad
d=-\sum_jr^{-j}y_j\right\}.}
\tag{19}
$$
该源唯一，并有
$$
\left\|(y_j/a_j)_j\right\|
\le\|C^{-1}(d\Omega+J_Uy)\|
\le2\left\|(y_j/a_j)_j\right\|.
\tag{20}
$$
所以保留的是原 $a_j^{-1}$ 费用，不是去权后的闭包值域。

作为区别，取 $y^{(n)}=-r^ne_n$，
则 $d=1$，对应 $CX$ 中的向量趋于 $\Omega$，
而源费用至少为 $r^n/a_n\to\infty$。
$\Omega$ 本身不满足 (19)。故这个稠密逼近绝不能当作实际原像。

$B$ 的像闭且余维恰为一：由 (12)，
$B=\mathcal A|_{\{0\}\oplus\ell^2}$ 是闭超平面的有界同构像。
这也准确解释了补回原常数列的重要性。
若令 $\zeta$ 为唯一满足
$\mathcal A^*\zeta=(-1,0)$ 的向量，则
$$
\ker B^*=\mathbb C\zeta,\qquad
\langle b,\zeta\rangle=-1,\qquad
\operatorname{Ran}M
=D_a(\zeta^\perp).
\tag{21}
$$
(21) 使用同一个原全行；没有另换可逆替代矩阵。

## 6. 完整进位的实际除法恰有一个条件

定义坐标泛函
$$
\psi(f)=\mu_0c-\sum_j\mu_jr^{-j}t_j,
\qquad P_Xf=J_X(c,t).
\tag{22}
$$
它有界，且 $\psi(\Omega)=\mu_0>0$。
原 $D$ 在 $X$ 上准确为
$D J_X(c,t)=\mu_0c\Omega-\sum_j\mu_jt_ju_j$。
所以由 $K=C-D$、(16)，
$$
D_a^{-1}J_U^*Kf
=\mathcal A(c,t)+\operatorname{diag}(\mu_j/a_j)t,
\qquad
\|D_a^{-1}J_U^*K\|\le2.
\tag{23}
$$
这里涵盖常数列、每一末列和全部高低交叉块；其余列本来为零。

设
$$
L=J_X\mathcal A^{-1}D_a^{-1}J_U^*K.
\tag{24}
$$
(12)、(23) 给全 $H$ 上的实际有界算子 $\|L\|\le4$，
且 $L=P_XLP_X$。它不是只在形式有限列上定义。

由 (19)，$CLf$ 与 $Kf$ 的所有 $u_j$ 坐标相同；
两者的常数坐标之差用 (18)、(22) 准确算出为 $\psi(f)$。
故
$$
\boxed{\quad CL=K+\Omega\psi.\quad}
\tag{25}
$$
$\Omega\psi$ 表示 $f\mapsto\psi(f)\Omega$。
进而 (19)、(23) 给真正的充要条件：
$$
\boxed{\quad
Kf\in\operatorname{Ran}C\ \Longleftrightarrow\ \psi(f)=0,
\qquad C^{-1}Kf=Lf\quad(f\in\ker\psi).
\quad}
\tag{26}
$$
所以最大自然组合 $C^{-1}K$ 的定义域恰为闭余维一空间 $\ker\psi$，
在其上有界，范数至多 $4$。
这不是在整个 $H$ 上的除法，也不是仅关于 $\overline{\operatorname{Ran}C}$ 的陈述。

## 7. 一个满射右因子及其准确边界

令 $\mathcal V=I-L$。由 (25)，
$$
\boxed{\quad C\mathcal V=D-\Omega\psi.\quad}
\tag{27}
$$
这个右因子实际上满射，核恰为 $\mathbb C\Omega$。
在 $X^\perp$ 上它是恒等；在 $X$ 的同一坐标中，(23)–(24) 给
$$
\mathcal A\,J_X^{-1}\mathcal V J_X(c,t)
=-\operatorname{diag}(\mu_j/a_j)t.
\tag{28}
$$
因为 $1/2\le\mu_j/a_j<1$，
右侧可遍历全部 $\ell^2$，且为零当且仅当 $t=0$。
这证明满射与核，并给范数至多 $2$ 的实际右逆：
对 $z\in X$，取源
$$
J_X\left(0,-\operatorname{diag}(a_j/\mu_j)\mathcal A J_X^{-1}z\right);
$$
在 $X^\perp$ 上仍取恒等。

(27) 是完整原算子的**非交换右因子身份**。
没有证明 $\mathcal V$ 与 $C$ 或 $D$ 交换，
它也非单射。因此不能由 $D$ 的闭根直接开出 $C$ 的闭根，
不能以满射右因子代替相似或拟亲和交织。
同样，$\ker\psi$ 只是这次实际除法的自然域，
本稿没有把它宣称为 $C$ 不变空间。

新增来源是 (19)–(26) 的全部原末列与常数列的精确范围和统一费用，
以及 (27)–(28) 的真实满射右因子。
原场外二次分子、真正闭稳定根的两坐标和普通 ISP 继续按原完成标准研究。
