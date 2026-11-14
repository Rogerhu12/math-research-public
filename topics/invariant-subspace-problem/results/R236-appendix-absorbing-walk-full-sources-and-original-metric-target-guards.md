# R236 附录：吸收路径的完整源因式分解与指定目标费用

- 日期：2026-11-13。
- 作者线：normal-complex。
- 状态：纯模型完整源定理、目标守卫和指定解析提升下界已证明；实际正常理想接口仍未闭合。
- 范围：§§1–8 的精确分解属于纯产生位加有界头，指数比较仅为条件预算。§§9–10 回到实际尾交换子，证明任意复路径权及全部路径后实际尾权的归一目标一致弱零；准确范围是完整首列具有首达上闭支持，原普通 ISP 仍未完成。
- 已有结论扣除：纯尾核图、吸收链和纯线性排核范围已在 [R113](R113-pure-tail-dominance-and-carry-obstructions.md) 中证明。本稿不重计这些结论；这里补的是两个完整变换、全部叶源、指定输出及其费用。
- 实际桥参照：[完整有限头原像与 carry 费用](R236-appendix-exact-head-vacuum-column-and-carry-cost.md) §4.8，以及 [联合高幂行与修正目标](R236-appendix-joint-gauge-row-powers-and-carry-corrected-targets.md)。只有满足那里全部源和目标条件时，才可迁入原问题。

## 1. 模型与精确二乘二恒等式

固定整数 $n<M$，令 $h=M-n$。在

$$
\mathcal H
 =\mathcal K\otimes
  \bigotimes_{j=n}^{M-1}\mathbb C^2
  \otimes\mathcal K_{\rm far}
$$

上取纯产生算子

$$
E_j=
\begin{pmatrix}0&0\\I&0\end{pmatrix}_j.
$$

设 $a_j\ne0$，且

$$
C_j=H+\sum_{i\ge j}a_iE_i,\qquad
B_j=C_{j+1}.
\tag{1.1}
$$

这里 $H$ 是有界算子，作用在 $\mathcal K$ 上。远端的和可以有限，也可以按 $\sum|a_i|<\infty$ 在算子范数中收敛。$B_j$ 不作用于第 $j$ 位，所以与该位的矩阵单位交换。特别地，$B_j$ 始终保留全部尚未剥去的位；本稿从不把 $M$ 后的尾删掉。

对每个整数 $k\ge1$，

$$
C_j^k
 =
\begin{pmatrix}
 B_j^k&0\\
 k a_j B_j^{k-1}&B_j^k
\end{pmatrix}.
\tag{1.2}
$$

记

$$
L_{j,k}=R_{j,k}
 =
\begin{pmatrix}
 I&-B_j/(k a_j)\\0&I
\end{pmatrix},
\qquad
J_j=
\begin{pmatrix}0&I\\I&0\end{pmatrix}.
$$

直接相乘得到

$$
L_{j,k} C_j^k R_{j,k}J_j
 =
\begin{pmatrix}
 -B_j^{k+1}/(k a_j)&0\\
 0&k a_j B_j^{k-1}
\end{pmatrix}.
\tag{1.3}
$$

这个公式没有使用 $B_j$ 的逆、预解或闭值域。$L_{j,k}$、$R_{j,k}$ 的逆只把右上角的负号换成正号。

令

$$
\epsilon_j=\frac{\|B_j\|}{|a_j|}.
$$

则

$$
\|L_{j,k}^{\pm1}\|,\ \|R_{j,k}^{\pm1}\|
 \le 1+\epsilon_j/k\le1+\epsilon_j.
\tag{1.4}
$$

$k=0$ 时约定 $C_j^0=I$，并立即停止该支；此后不再使用 (1.3)。

## 2. 全树因式分解只按层收费

从状态 $(n,q)$ 开始，其中 $q\ge1$。每次 (1.3) 产生两支：

$$
(j,k)\longrightarrow
\begin{cases}
(j+1,k+1),&\text{系数 }-1/(k a_j),\\
(j+1,k-1),&\text{系数 }k a_j.
\end{cases}
\tag{2.1}
$$

一支首次到达 $k=0$ 就停止；未吸收的支只剥到 $j=M$。因此这是有限树，叶空间仍含全部未用位和外部因子。

沿路径乘起 (2.1) 的标量，记为 $\omega_\pi$。存在有界可逆算子 $\mathcal L,\mathcal R$ 和一个坐标置换酉 $P$，使

$$
C_n^q=\mathcal L\,\mathcal D\,\mathcal R.
\tag{2.2}
$$

其中 $\mathcal D$ 按叶空间对角分块：

- 吸收叶的块是 $\omega_\pi I$；
- 到 $M$ 尚处于高度 $k\ge1$ 的叶块是 $\omega_\pi C_M^k$。

特别是，吸收之后留下的是整个未剥空间上的恒等算子。无需令 $M$ 等于实际有限头截断位置 $p$。

令

$$
\kappa_{n,M}=\prod_{j=n}^{M-1}(1+\epsilon_j).
$$

全部变换满足

$$
\|\mathcal L^{\pm1}\|,
\ \|\mathcal R^{\pm1}\|
 \le\kappa_{n,M},
\tag{2.3}
$$

以及

$$
\|\mathcal L-I\|,
\ \|\mathcal R-P\|,
\ \|\mathcal R^{-1}-P^{-1}\|
 \le\kappa_{n,M}-1.
\tag{2.4}
$$

### 2.1 递归和范数的证明

在某一非停止节点，若两个子树的因式分解已经写成
$\mathcal L_\pm\mathcal D_\pm\mathcal R_\pm$，则由 (1.3) 取

$$
\mathcal L_{j,k}
 =L_{j,k}^{-1}
   \operatorname{diag}(\mathcal L_+,\mathcal L_-),
$$

$$
\mathcal R_{j,k}
 =\operatorname{diag}(\mathcal R_+,\mathcal R_-)
   J_j R_{j,k}^{-1}.
\tag{2.5}
$$

两个标量进入 $\mathcal D_\pm$。停止节点的三个因子均取恒等算子。对应的坐标置换为

$$
P_{j,k}
 =\operatorname{diag}(P_+,P_-)J_j.
\tag{2.6}
$$

直接和的范数是两支范数的最大值。因此每经过一个物理位，只乘一次 $1+\epsilon_j$，不是按叶数相乘。

例如设子树的统一上界为 $\kappa'$，则

$$
\|\mathcal R_{j,k}-P_{j,k}\|
 \le(\kappa'-1)(1+\epsilon_j)+\epsilon_j
 =(1+\epsilon_j)\kappa'-1.
$$

其余三项和逆变换同样由 (2.5) 逐层证明。这给出 (2.3)–(2.4)。

$P$ 只重排有限池的计算基坐标，且不作用于头和远端。因此它固定有限池的平坦真空

$$
\Omega_{\rm pool}
 =\bigotimes_{j=n}^{M-1}(e_0+e_1)/\sqrt2.
\tag{2.7}
$$

## 3. 任意吸收叶集合的完整源

令 $G$ 是吸收叶的任意集合，$Q_G$ 为其叶空间正交投影。只在这些叶上定义部分逆

$$
\mathcal D_G^{-1}
 =\bigoplus_{\pi\in G}\omega_\pi^{-1}I,
\qquad
\mathcal D_G^{-*}
 =\bigoplus_{\pi\in G}\overline{\omega_\pi}^{-1}I,
$$

其余叶上取零。这两个记号都指这里定义的部分逆，不是对带零块的整个算子求逆；没有对任何未吸收块求逆。

定义完整源算子及其准确输出

$$
\mathcal U_G
 =(\mathcal L^*)^{-1}
   \mathcal D_G^{-*}Q_G P,
\qquad
Y_G=\mathcal R^*Q_G P.
\tag{3.1}
$$

由 (2.2) 得到整个空间上的恒等式

$$
(C_n^q)^*\mathcal U_G=Y_G.
\tag{3.2}
$$

故对每个 $f\in\mathcal H$，$\mathcal U_Gf$ 都是输出 $Y_Gf$ 的真实源。此处不是只解一列或只给压缩方程。

令

$$
Q'_G=P^*Q_GP.
$$

这是原坐标中的一个正交投影，且

$$
\|\mathcal U_G\|
 \le\kappa_{n,M}
      \max_{\pi\in G}|\omega_\pi|^{-1},
\tag{3.3}
$$

$$
\|Y_G\|\le\kappa_{n,M},
\qquad
\|Y_G-Q'_G\|\le\kappa_{n,M}-1.
\tag{3.4}
$$

这些估计不涉及外部因子的维数。

## 4. 标量源费是路径面积

现在额外假设 $a_j=e^{-\ell_j}>0$，其中 $\ell_j\ge0$ 递增。设一条吸收路径依次具有高度
$k_n=q,k_{n+1},\dots,k_{n+\tau}=0$，首次到零前各高度均正。上、下步分别记为 $U,D$。

由 (2.1)，

$$
|\omega_\pi|
 =
\frac{\prod_D k_j a_j}{\prod_U k_j a_j}.
\tag{4.1}
$$

高度因子有精确恒等式

$$
\frac{\prod_D k_j}{\prod_U k_j}
 =
q!\prod_U\frac{k_j+1}{k_j}
 \ge q!.
\tag{4.2}
$$

证明是对 $k!$ 沿路径望远镜：下步的因子为 $k$，上步的逆因子为 $1/(k+1)$，其总积为 $q!$。

系数的对数也准确望远镜：

$$
\sum_D\ell_j-\sum_U\ell_j
 =
q\ell_n+
 \sum_{j=n+1}^{n+\tau-1}
 k_j(\ell_j-\ell_{j-1}).
\tag{4.3}
$$

所以

$$
\log|\omega_\pi|^{-1}
 \le
q\ell_n+
 \sum_{j=n+1}^{n+\tau-1}
 k_j(\ell_j-\ell_{j-1})
 -\log(q!).
\tag{4.4}
$$

若该支在 $t_0$ 步内吸收且此前 $k_j<2q$，则

$$
\log|\omega_\pi|^{-1}
 \le
q\ell_n+2q(\ell_{n+t_0}-\ell_n)-\log(q!).
\tag{4.5}
$$

这不是把全部权的条件数相乘；费用由该支经过的高度和系数增量决定。

## 5. 一个有统一正质量的早吸收集合

取 $h\ge256$ 及

$$
1\le q\le\frac{\sqrt h}{16},
\qquad
t_0=\lfloor h/8\rfloor.
\tag{5.1}
$$

令 $G$ 为以下吸收叶：从 $q$ 出发的简单对称随机游走，在 $t_0$ 步内先到 $0$ 而不是先到 $2q$。

对区间 $\{0,\dots,2q\}$ 的首次退出时间 $\tau$，直接解一阶差分式得到

$$
\Pr_q(k_\tau=0)=1/2,\qquad
\mathbb E_q\tau=q^2.
\tag{5.2}
$$

第二个等式也由 $u(k)=k(2q-k)$ 满足
$u(k)=1+[u(k-1)+u(k+1)]/2$ 及端点零值证明。

由于 $t_0\ge h/16$、$q^2\le h/256$，Markov 不等式给出

$$
\theta_{q,h}:=\Pr(G)
 \ge\frac12-\frac{q^2}{t_0}
 \ge\frac7{16}.
\tag{5.3}
$$

同时 $\theta_{q,h}\le1/2$。每条 $G$ 中的支满足 (4.5)，故

$$
\|\mathcal U_G\|
 \le
\frac{\kappa_{n,M}}{q!}
 \exp\!\left[
 q\ell_n+2q(\ell_{n+t_0}-\ell_n)
 \right].
\tag{5.4}
$$

在平坦池真空中，$Q'_G$ 的期望恰为 $\theta_{q,h}$。

### 5.1 纯模型中的有界弱目标

考虑一列这样的模型，池起点 $n\to\infty$，并假设

$$
\sum_{j=n}^{M-1}\epsilon_j\longrightarrow0.
\tag{5.5}
$$

则 $\kappa_{n,M}\to1$。对任意固定有限柱向量 $f,g$，当池在其支撑之外时，

$$
\langle Q'_Gf,g\rangle
 =\theta_{q,h}\langle f,g\rangle.
$$

由 (3.4)、(5.3) 和有限柱稠密性，

$$
\frac{Y_G}{\theta_{q,h}}
 \longrightarrow I
 \quad\text{WOT},
\qquad
\sup\left\|Y_G/\theta_{q,h}\right\|<\infty.
\tag{5.6}
$$

无需先选 $\theta_{q,h}$ 收敛的子列。这里的 WOT 是纯模型原内积中的算子弱收敛；它本身不声称 $Y_G$ 属于解析交换代数。

### 5.2 伸缩指数系数的纯尾条件

若

$$
a_j=\exp[-\beta(j+1)^\alpha],
\qquad \beta>0,\quad\alpha>1,
$$

且 $H=0$，则

$$
\epsilon_j
 \le \frac{\sum_{i>j}a_i}{a_j}
 \le C\exp[-c j^{\alpha-1}].
\tag{5.7}
$$

例如对足够大的 $j$，凸性给每个后继比
$a_{i+1}/a_i\le\exp[-c j^{\alpha-1}]$，先求几何尾再求 $j$ 尾即可。因此 (5.5) 对任意 $M>n$ 成立。

若模型中有变化的头 $H_n$，则额外足够条件为

$$
(M-n)\|H_n\|\,a_{M-1}^{-1}\longrightarrow0.
\tag{5.8}
$$

此时 $B_j$ 的头部分和纯尾部分分开估计即可。对于 $\alpha\le1$，(5.7) 所用的尾支配不成立；不能单凭下一节的指数参数范围补上它。

## 6. 两尺度预算只是条件比较

本节把一种可能的实际应用所需指数条件单独列清，避免令剥位终点 $M$ 与更远的实际截断 $p$ 相同。

假设某个尚待构造的实际接口同时满足：

1. 只剥 $n,\dots,M-1$，吸收后保留 $M$ 以后的全部因子；
2. $q\asymp\sqrt M$，walk 源费的对数至多 $O(M^{\alpha+1/2})$；
3. 周期低头度量只付一次 $F_n=O(16^n)$；
4. 低头压缩半径满足 $-\log\rho_n\asymp8^n$，故小头条件需要 $8^n\gg M^\alpha$；
5. 有限头提升付 $K_p=e^{O(p)}$，真实剩余尾的 $q$ 次预算为 $\exp[-c q p^\alpha]$；
6. 实际 carry 和完整有界目标也另外得到证明。

令

$$
M\asymp p^\gamma,\qquad
16^n\asymp p^t,\qquad
q\asymp p^{\gamma/2}.
$$

对任意 $\alpha>1/2$，可以先选

$$
\max\{0,2(1-\alpha)\}
 <\gamma<
\min\left\{
1,\frac1{\alpha+1/2},\frac3{4\alpha}
\right\},
\tag{6.1}
$$

再选

$$
\max\left\{
1,\gamma(\alpha+1/2),\frac43\alpha\gamma
\right\}
 <t<\alpha+\gamma/2.
\tag{6.2}
$$

区间确实非空：若 $1/2<\alpha<1$，左端 $2(1-\alpha)$ 小于 (6.1) 的三个右端；其余 $\alpha$ 更直接。由 (6.1)，(6.2) 中后两个下界均小于 $1$，而 $\alpha+\gamma/2>1$。

于是

$$
p,\quad M^{\alpha+1/2},\quad16^n
 =o(qp^\alpha),
\qquad
M^\alpha=o(8^n).
\tag{6.3}
$$

可用 $n=\lfloor(t/4)\log_2p\rfloor$ 得到 $16^n\asymp p^t$；不需要声称任意整数 $p$ 都有精确比值收敛。

(6.3) 只核指数之间有空间。它不证明上列第 6 项，不证明一般 $\alpha>1/2$ 的纯尾变换条件，也不证明本稿的输出已经是可用的实际右因子。

## 7. 周期度量返回原内积的目标费用

设 $D=D_n>0$ 是已证明的周期物理度量，作用在低 $n$ 位，而池在 $n$ 之后。写

$$
C^\flat=D^{-1}CD.
$$

若前文的源是在平坦度量中构造，即

$$
((C^\flat)^q)^*\mathcal U^\flat=Y^\flat,
$$

那么回原内积的准确式是

$$
(C^q)^*(D^{-1}\mathcal U^\flat D)
 =D^{-1}Y^\flat D.
\tag{7.1}
$$

源的确只付一次条件数：

$$
\|D^{-1}\mathcal U^\flat D\|
 \le \operatorname{cond}(D)\|\mathcal U^\flat\|.
\tag{7.2}
$$

然而 $Q'_G$ 虽与 $D$ 交换，目标误差只能先得到

$$
\|D^{-1}Y^\flat D-Q'_G\|
 \le
\operatorname{cond}(D)\,
 \|Y^\flat-Q'_G\|.
\tag{7.3}
$$

在本仓库的周期度量中，

$$
\operatorname{cond}(D_n)=e^{F_n},
\quad
F_n\asymp16^n,
\quad
-\log\rho_n\asymp8^n.
$$

假如 (3.4) 中的小头误差仅由
$\|H_n^\flat\|/a_M=O(\rho_n^r/a_M)$ 控制，则该粗界在乘上 $e^{F_n}$ 后并不趋零。因为固定 $r$ 时 $r|\log\rho_n|=O(8^n)$，无法吸收 $F_n\asymp16^n$。

这说明现有估计尚未支付原内积中统一有界的目标；它不是说真实误差必然达到该粗上界。需要额外的高阶抵消、不同目标或新的双行结构，才能越过 (7.3)。

正密度的非酉变换也不能规避此项：已经核验的正合同是 $D^{-1}\rho D^{-1}$，其对应左行是 $D S D$，一般不是相似后的 $D^{-1}SD$。不能同时免费保留正性和原湮灭理想。

## 8. 早吸收坐标目标的解析提升本身指数增长

本节即使在没有低头和 carry 的纯模型中也成立。它是对当前指定目标的精确检查，不是对所有可能目标的下界。

本节把池的位重新编号为 $1,\dots,h$。在有限池上，令反线性等距 $C$ 为计算基逐位互补后复共轭；它固定 $\Omega_{\rm pool}$。有限纯产生代数有唯一的提升 $X_w$，满足

$$
X_w\Omega_{\rm pool}=w.
$$

$P$ 的递归 (2.6) 表明：在原物理比特中，下降对应 $0$、上升对应 $1$，直到吸收。因此对 $Q'_G$，其转置真空提升为

$$
\mathcal X_G=X_{C Q'_G\Omega_{\rm pool}}
 =
\sum_{\pi\in G}
 \left(\prod_{i\in D(\pi)}E_i\right)
 \left(\prod_{i\in U(\pi)}(I-E_i)\right).
\tag{8.1}
$$

这里只使用停止之前的位。证明是在布尔立方体上先写互不相交的首次吸收柱事件，再取唯一的多线性展开；将其变量代入 $E_i$ 后，每个计算基坐标的累加值正好给 $C Q'_G\Omega_{\rm pool}$。

假设 $q\ge2$ 且 $t_0\ge q$。取

$$
u=\left\lfloor\frac{t_0-q}{2}\right\rfloor,
\qquad N=q+2u\le t_0.
$$

考虑 (8.1) 中全前 $N$ 位的单项式 $E_1\cdots E_N$ 的系数：

- 早于 $N$ 停止的项只用少于 $N$ 个变量，不能贡献此单项式；
- 晚于 $N$ 停止的项必含停止时的下降变量 $E_j$，其中 $j>N$，也不能贡献恰好为前 $N$ 位的单项式；
- 恰在 $N$ 停止的每条路径都有 $u$ 个上升步，所以该最高次系数均为同一个符号 $(-1)^u$。

故准确系数是

$$
(-1)^u A(q,N),
\tag{8.2}
$$

其中 $A(q,N)$ 为从 $q$ 出发、此前不触 $0,2q$、第 $N$ 步首次到 $0$ 的路径数。

从高度 $q$ 先做 $u$ 个任意选择的 $UD$ 或 $DU$ 两步环，再做 $q$ 个下降步，即得到 $2^u$ 条这样的路径。因 $q\ge2$，两步环始终处于 $1,\dots,2q-1$。因此

$$
A(q,N)\ge2^u.
$$

把 $\mathcal X_G$ 作用于全零计算基向量后，不同产生单项式给正交向量。所以

$$
\boxed{
\|\mathcal X_G\|
 \ge 2^{\lfloor(t_0-q)/2\rfloor}.
}
\tag{8.3}
$$

当 $q\asymp\sqrt h$、$t_0=\lfloor h/8\rfloor$ 时，右边在 $h$ 的尺度指数增长。将 $Q'_G$ 除以 $\theta_{q,h}\in[7/16,1/2]$ 只改变一个有界常数，不能消去该增长。

例如 $q=2$、$t_0=4$ 时，提升已经是

$$
E_1E_2+E_2E_3E_4+E_1E_3E_4
 -2E_1E_2E_3E_4,
$$

其全零列范数为 $\sqrt7$。

这与 (5.6) 没有矛盾：$Y_G$ 是整个算子空间中的有界弱目标，而 (8.3) 是要求该坐标目标经过解析真空提升后的费用。实际正常湮灭泛函只能测试真实交换代数中的右因子；不能用前者的 WOT 结论代替后者的统一有界性。

## 9. 任意复路径权及公共池后算子权的实际锚上界

日期：2026-11-13 UTC。状态：已证明的辅助结论。
本节加强 §8 的指定未加权 raw 目标障碍，但不限制所有可能的吸收源目标。

### 9.1 首达路径与实际解析位因子

固定 $q\ge1$，从高度 $q$ 开始，每步记为 $D$ 或 $U$，
分别令高度减一或加一。
令 $\mathcal P$ 为任意有限组**首次**到达零的路径，
每条路径长度 $N(\pi)$ 不超过共同池宽 $M$。
允许另加上边界或停止时间选择；只要所保留的路径仍是首达零路径即可。
非空时当然有 $M\ge q$。

所有路径从同一物理位 $n$ 开始依次使用
$n,\ldots,n+N(\pi)-1$。
首达条件保证这些有限字形成前缀互不包含的集合。
因此相应物理柱两两不交，且有 Kraft 界
$$
\sum_{\pi\in\mathcal P}2^{-N(\pi)}\le1.
\tag{9.1}
$$
若 $N=q+2u$，该长度的路径恰有 $u$ 个上步。

实际位因子定义为
$$
D_j=\frac{I-V_j}{2}=N_j(I+N_j)^{-1},
\qquad
U_j=\frac{I+V_j}{2}=(I+N_j)^{-1}.
\tag{9.2}
$$
纯比较因子为
$$
D_j^0=E_j,\qquad U_j^0=I-E_j.
$$
由实际 Walsh 首列
$V_j(\Omega_j\otimes h)=\chi_j\otimes h$，
对任意其余位向量 $h$ 有
$$
D_j(\Omega_j\otimes h)=2^{-1/2}e_1\otimes h,
\qquad
U_j(\Omega_j\otimes h)=2^{-1/2}e_0\otimes h.
\tag{9.3}
$$
纯因子满足同一等式。
这一步使用真正的 Cayley 因子，而不是把 $N_j$ 免费当成 $E_j$。

设 $\mathcal C_{n+M}=\{\widehat N_{n+M}\}'$ 为共同池之后的
完整实际尾交换子。
每条路径可取任意
$$
W_\pi\in\mathcal C_{n+M},
$$
并在整个池上按恒等提升。
由真实头尾矩阵包含，所有这些提升都属于原 $\mathcal A'$。
写
$$
R_\pi=\prod_{\pi_j=D}D_j\prod_{\pi_j=U}U_j,
\qquad
R_\pi^0=\prod_{\pi_j=D}E_j
\prod_{\pi_j=U}(I-E_j),
$$
$$
G=\sum_{\pi\in\mathcal P}R_\pi W_\pi\in\mathcal A',
\qquad
G^0=\sum_{\pi\in\mathcal P}R_\pi^0W_\pi.
\tag{9.4}
$$
$G^0$ 只作纯比较算子，不被称为实际 $\mathcal A'$ 元素。
标量任意复路径权是 $W_\pi=w_\pi I$ 的特例。

### 9.2 准确首列控制全部算子系数

令 $e_M$ 把池后尾向量 $h$ 送到
$\Omega_+^{\otimes M}\otimes h$。
由 (9.3)，
$$
R_\pi e_M=R_\pi^0e_M
=2^{-N(\pi)/2}|\pi\rangle\otimes
\Omega_+^{\otimes(M-N(\pi))}\otimes I,
$$
其中 $|\pi\rangle$ 的下步位取 $e_1$、上步位取 $e_0$。
不同首达路径的这些池向量相互正交。
所以
$$
Ge_M=G^0e_M,
$$
以及准确的算子列恒等式
$$
\boxed{
e_M^*G^*Ge_M
=\sum_\pi2^{-N(\pi)}W_\pi^*W_\pi
\le\|G\|^2I.
}
\tag{9.5}
$$
特别，任一非零的算子系数组都给非零 $G$。
相应真空配对也准确相同：
$$
\omega(G)=\omega(G^0).
\tag{9.6}
$$

### 9.3 全前缀系数保留任意复取消

对纯比较算子，在整个共同池取全零物理输入
$e_0^{\otimes M}\otimes h$。
对每个长度 $N$，读输出
$$
e_1^{\otimes N}\otimes e_0^{\otimes(M-N)}\otimes\mathscr H_{n+M}.
$$
其算子系数记为 $C_N$。

早于 $N$ 停止的项总次数小于 $N$，不能贡献该输出。
晚于 $N$ 停止的项，其最后一步一定是在 $N$ 之后的下步，
故强制至少一个池外前缀位为 $e_1$，也不能贡献。
恰在 $N=q+2u$ 停止时，取得全前 $N$ 位单项式
必须从每个上步因子 $I-E_j$ 中选取 $-E_j$。
因此准确有
$$
\boxed{
C_{q+2u}=(-1)^u
\sum_{\substack{\pi\in\mathcal P\\N(\pi)=q+2u}}W_\pi.
}
\tag{9.7}
$$
所有路径系数的相位取消都保留在这个算子和中。

不同前缀输出彼此正交，故同一个单位输入列给
$$
\boxed{
\sum_{u\ge0}C_{q+2u}^*C_{q+2u}\le\|G^0\|^2I.
}
\tag{9.8}
$$
不存在的长度按零处理。

每个纯位因子的真空均值均为 $1/2$，
所以 (9.7) 给
$$
\omega(G^0)
=\sum_{u\ge0}(-1)^u2^{-q-2u}
\omega_{\rm tail}(C_{q+2u}).
$$
对算子列 (9.8) 作 Cauchy–Schwarz，得到
$$
\boxed{
|\omega(G^0)|
\le
\left(\sum_{u\ge0}4^{-q-2u}\right)^{1/2}\|G^0\|
=
\frac4{\sqrt{15}}\,2^{-q}\|G^0\|.
}
\tag{9.9}
$$
这里不要求路径权为正、不要求同一长度的权相同，
也不要求尾算子权为标量。

### 9.4 相对实际 carry 由完整系数列支付

记
$$
\bar\eta_n=e^{-770\cdot16^n}.
$$
实际 $\|N_j-E_j\|\le\bar\eta_n$ 对所有 $j\ge n$ 成立。
由 $\|V_j\|<3$，$\|(I+N_j)^{-1}\|\le2$；
而 $\|(I+E_j)^{-1}\|=\|I-E_j\|<2$。
预解恒等式给
$$
\|U_j-U_j^0\|,\ \|D_j-D_j^0\|\le4\bar\eta_n.
\tag{9.10}
$$
实际与纯的所有单个位因子范数都至多二。

对一条长度 $N$ 的路径逐因子望远镜，
$$
\|R_\pi-R_\pi^0\|
\le4N2^{N-1}\bar\eta_n
\le2M2^N\bar\eta_n.
\tag{9.11}
$$
把 (9.4) 的差准确写成算子行与列的乘积：
$$
G-G^0
=
\big[\,2^{N(\pi)/2}(R_\pi-R_\pi^0)\,\big]_\pi
\operatorname{col}_\pi(2^{-N(\pi)/2}W_\pi).
$$
由 (9.5)，第二列范数不超过 $\|G\|$。
第一行范数的平方不超过
$$
\begin{aligned}
\sum_\pi2^{N(\pi)}
\|R_\pi-R_\pi^0\|^2
&\le4M^2\bar\eta_n^2\sum_\pi8^{N(\pi)}\\
&\le4M^2\bar\eta_n^2\,16^M
\sum_\pi2^{-N(\pi)}
\le4M^2\,16^M\bar\eta_n^2.
\end{aligned}
$$
因此
$$
\boxed{
\|G-G^0\|\le\epsilon_{n,M}\|G\|,
\qquad
\epsilon_{n,M}=2M4^M\bar\eta_n.
}
\tag{9.12}
$$
这是相对于完整实际输出范数的界，
没有把任意尾算子权的范数和视为免费。

结合 (9.6)、(9.9)、(9.12)，对每个非零 $G$ 得
$$
\boxed{
\frac{|\omega(G)|}{\|G\|}
\le
\frac4{\sqrt{15}}\,
2^{-q}(1+\epsilon_{n,M}).
}
\tag{9.13}
$$

### 9.5 统一弱零及准确剩余范围

若
$$
n\longrightarrow\infty,\qquad
q_n\longrightarrow\infty,\qquad
q_n\le M_n,\qquad M_n=o(16^n),
\tag{9.14}
$$
则 $\epsilon_{n,M_n}\to0$。
全部满足本节定义的非零 $G_n/\|G_n\|$
都是真实第 $n$ 位之后的尾算子，范数一，
且由 (9.13) 其真空配对一致趋零。
有限柱配对准确因式及稠密性给
$$
\frac{G_n}{\|G_n\|}\longrightarrow0
\quad\text{于 WOT，且对全部路径/算子权选择一致。}
\tag{9.15}
$$
同样对每个固定正常泛函 $\phi$，
$$
\sup_G\frac{|\phi(G)|}{\|G\|}\longrightarrow0.
$$
用有限秩迹类逼近和统一范数界即可由 (9.15) 得到这一句，
不要求 $\phi$ 正。

这排除了仅靠给 raw 吸收路径改变复权、作复平均，
或附加共同池之后的完整尾算子权来恢复正常锚。
原 §6 的两尺度候选具有 $M=o(16^n)$，所以此 carry 预算足够。

本节的最高前缀系数法尚未覆盖的自由度是：某条路径的权可作用在它吸收后尚未剥去、
但仍位于共同池内部的坐标上。
那时早停项可以产生更长前缀的单项式，(9.7) 的早停排除不再成立，
故不能把本节上界外推到这种权，也不能外推到任意完整
operator-valued 列目标或全部实际尾理想。

## 10. 完整 good 首列的多尺度界：允许全部路径后实际尾权

日期：2026-11-13 UTC。状态：已证明的辅助加强。
本节用另一种多尺度分解覆盖 §9 最后留下的池内后停权，
不再依靠早停项不能产生长前缀的假设。

### 10.1 good 物理集合与全首列假设

固定 $M\ge q\ge1$，池为 $n,\ldots,n+M-1$。
以 $F\subset\{1,\ldots,M\}$ 表示物理位中取 $e_1$ 的位置，
定义
$$
\mathcal G_{q,M}
=
\left\{
F:\max_{1\le r\le M}
\bigl(2|F\cap\{1,\ldots,r\}|-r\bigr)\ge q
\right\}.
\tag{10.1}
$$
这是向上闭的集合：若 $F\in\mathcal G_{q,M}$ 且 $F\subset F'$，
则 $F'\in\mathcal G_{q,M}$。
记 $P_{\mathcal G}$ 为这些物理基向量张成空间的正交投影。

取实际第 $n$ 位之后的尾交换子
$$
G\in\mathcal C_n=\{\widehat N_n\}'.
$$
本节的假设是整个算子列满足
$$
\boxed{
\operatorname{Ran}(Ge_M)
\subset
\operatorname{Ran}P_{\mathcal G}\otimes\mathscr H_{n+M}.
}
\tag{10.2}
$$
$e_Mh=\Omega_+^{\otimes M}\otimes h$，且 $h$ 任意。
由[实际尾真空的分离性](R236-appendix-faithful-vacuum-support-and-nonuniform-column-repair.md)命题1，(10.2) 等价于单个 $G\Omega$ 的精确物理支持条件；尾块系数均被真空分离。该等价仅用于精确零式，不给近支持的统一解析修复。

### 10.2 实际首列与纯比较算子的相对范数

使用算子系数 Walsh 首列提升：
$$
G=\sum_{F\subset\{1,\ldots,M\}}
V_F(I\otimes u_F),
\qquad u_F\in\mathcal C_{n+M},
$$
$$
\sum_Fu_F^*u_F=e_M^*G^*Ge_M\le\|G\|^2I.
\tag{10.3}
$$
这里 $V_F$ 的实际指标在相应池内。
这是已证明的完整交换子版本，
见 R236《算子系数 Walsh 首列提升、联合最大子式与精确一次尾交》§7。

令 $V_j^0=I-2E_j$，并定义纯比较算子
$$
G^0=\sum_F V_F^0(I\otimes u_F).
\tag{10.4}
$$
它的尾系数不被当成纯模型自身的交换子；
只需它们作用在共同池之后。
实际和纯的 Walsh 首列完全相同，所以
$$
G^0e_M=Ge_M,\qquad \omega(G^0)=\omega(G).
\tag{10.5}
$$

从实际单个位公式
$V_j=\left(\begin{smallmatrix}0&-I\\ I&2(I+t_j)(I-t_j)^{-1}\end{smallmatrix}\right)$
得
$$
\|V_j-V_j^0\|
\le\frac{4\eta_j}{1-\eta_j}\le5\bar\eta_n,
\qquad \|V_j\|,\|V_j^0\|<3.
$$
逐因子差及算子行估计给
$$
\begin{aligned}
\left\|[V_F-V_F^0]_F\right\|^2
&\le\frac{25}{9}\bar\eta_n^2
\sum_F |F|^2 9^{|F|}\\
&\le\frac{25}{9}M^2 10^M\bar\eta_n^2.
\end{aligned}
$$
再与 (10.3) 的完整系数列相乘，得到
$$
\boxed{
\|G-G^0\|\le \varepsilon_{n,M}\|G\|,
\qquad
\varepsilon_{n,M}=2M10^{M/2}\bar\eta_n.
}
\tag{10.6}
$$
因此不论系数有多少，始终有
$\|G^0\|\le(1+\varepsilon_{n,M})\|G\|$。

### 10.3 从完整真空列支持到纯单项式支持

设 $e_{\varnothing}=e_0^{\otimes M}$。
池上的可逆纯产生多项式
$$
T_M=2^{-M/2}\prod_{j=1}^M(I+E_j)
$$
满足 $T_Me_{\varnothing}=\Omega_+^{\otimes M}$，
且
$$
T_M^{-1}=2^{M/2}\prod_{j=1}^M(I-E_j).
$$
$T_M$、$T_M^{-1}$ 都保持向上闭物理空间
$\operatorname{Ran}P_{\mathcal G}$。
它们与 $G^0$ 交换，因为 $G^0$ 是以池后算子为系数的纯产生多项式。

由 (10.2)、(10.5)，
$$
G^0(e_{\varnothing}\otimes h)
=
T_M^{-1}G^0(\Omega_+^{\otimes M}\otimes h)
\in\operatorname{Ran}P_{\mathcal G}\otimes\mathscr H_{n+M}.
$$
将纯多项式完整展开为
$$
G^0=\sum_{F\subset\{1,\ldots,M\}}E_F W_F.
$$
因为 $E_Fe_{\varnothing}=e_F$，上述包含对每个 $h$ 成立，
准确迫使
$$
\boxed{W_F=0\quad(F\notin\mathcal G_{q,M}).}
\tag{10.7}
$$
这里 $T_M^{\pm1}$ 仅用于代数支持推论，
没有以它们的巨大范数支付任何源或目标预算。

### 10.4 前缀次数投影的多尺度覆盖

本小节完全在有限池的纯产生算子系数空间中进行。
令
$$
N_j=2^j q,\qquad
0\le j\le J:=\lfloor\log_2(M/q)\rfloor,
$$
$$
m_j=\min(2N_j,M),\qquad
h_j=\lceil N_j/2\rceil.
$$
定义 $\mathcal P_j$ 为保留前 $m_j$ 位产生次数至少 $h_j$ 的系数投影。

这些投影可由前 $m_j$ 位的有限相位酉作 Fourier 积分得到。
每个精确次数投影收缩，
所以在当前产生多项式空间上
$$
\|\mathcal P_j\|,\ \|I-\mathcal P_j\|\le3N_j.
\tag{10.8}
$$
补投影只保留 $0,\ldots,h_j-1$ 次；
这不是对整个 $B(\mathscr H)$ 声称同样的正次数截断公式。
各前缀相位作用相互交换，故所有 $\mathcal P_j$ 相互交换。

对任意 $F\in\mathcal G_{q,M}$，令 $r$ 为首次达到 (10.1) 阈值的前缀长度。
有 $q\le r\le M$，并且
$$
|F\cap\{1,\ldots,r\}|\ge(r+q)/2.
$$
取唯一 $j$ 使 $N_j\le r<2N_j$。
则 $r\le m_j$，且前 $m_j$ 位至少包含 $h_j$ 个选中位置，
所以该单项式被 $\mathcal P_j$ 保留。
由 (10.7)，
$$
\prod_{j=0}^J(I-\mathcal P_j)G^0=0.
$$
按尺度从小到大作准确分解
$$
G^0=\sum_{j=0}^JQ_j,\qquad
Q_j=\mathcal P_j\prod_{i<j}(I-\mathcal P_i)G^0.
\tag{10.9}
$$
(10.8) 给
$$
\|Q_j\|
\le(3q)^{j+1}2^{j(j+1)/2}\|G^0\|.
\tag{10.10}
$$

### 10.5 每个尺度的数目窗与统一纯上界

$Q_j$ 的每个单项式在前 $m_j$ 位都至少产生 $h_j$ 次。
取这 $m_j$ 位数目算子的中心窗
$$
P_j^{\rm win}
=1_{\{|\mathsf N_{m_j}-m_j/2|<h_j/2\}}.
$$
产生次数可以不同，但都至少为 $h_j$，
所以仍有 $P_j^{\rm win}Q_jP_j^{\rm win}=0$。
参考向量在这些位上的数目分布是
$\operatorname{Bin}(m_j,1/2)$。
由 $\cosh(u/2)^{m_j}\le e^{m_ju^2/8}$ 的指数 Markov 界，
窗外向量范数至多 $\sqrt2 e^{-h_j^2/(4m_j)}$。
把配对拆成至少一个向量在窗外的两项，得到
$$
|\omega(Q_j)|
\le2\sqrt2\,\|Q_j\|e^{-h_j^2/(4m_j)}
\le2\sqrt2\,\|Q_j\|e^{-N_j/32}.
\tag{10.11}
$$

对全部 $j\ge0$，
$$
\frac{j+1}{2^j}\le1,\qquad
\frac{j(j+1)}{2^j}\le\frac32.
$$
当 $q\ge512$ 时，
$$
\log(3q)+\frac34\log2\le\frac q{64}.
$$
因此 (10.10) 的对数成本不超过 $q2^j/64$。
结合 (10.9)–(10.11)，延长有限尺度和为无限和，得到
$$
\begin{aligned}
|\omega(G^0)|
&\le2\sqrt2\,\|G^0\|
\sum_{j\ge0}e^{-q2^j/64}\\
&\le4\sqrt2\,e^{-q/64}\|G^0\|.
\end{aligned}
$$
最后一步用 $2^j\ge j+1$ 及 $q\ge512$。
故完整纯结论为
$$
\boxed{
|\omega(G^0)|
\le4\sqrt2\,e^{-q/64}\|G^0\|
\quad(M\ge q\ge512).
}
\tag{10.12}
$$
这个界不含 $M$，也不要求 $q$ 与 $\sqrt M$ 比例固定。

### 10.6 回到实际目标与正常配对

由 (10.5)、(10.6)、(10.12)，任意满足 (10.2) 的非零实际 $G$ 都有
$$
\boxed{
\frac{|\omega(G)|}{\|G\|}
\le4\sqrt2\,e^{-q/64}
(1+\varepsilon_{n,M}).
}
\tag{10.13}
$$
因此在
$$
n\to\infty,\qquad q_n\to\infty,\qquad
q_n\le M_n,\qquad M_n=o(16^n)
\tag{10.14}
$$
下，全部该类实际 $G_n/\|G_n\|$ 一致 WOT 趋零，
并对每个固定正常泛函一致趋零。
证明与 (9.15) 相同：实际算子只作用在第 $n$ 位之后，
先用有限柱准确因式，再用统一范数界延拓。

### 10.7 所有路径后实际尾权均满足全首列假设

现在允许一条长度 $N(\pi)$ 的首达路径使用
$$
W_\pi\in\mathcal C_{n+N(\pi)},
$$
它可以作用在尚未剥去、但仍属于共同池的任何坐标上。
定义
$$
G=\sum_\pi R_\pi W_\pi
$$
仍为实际尾交换子。

对任意池后 $h$，$W_\pi$ 先作用在第 $n+N(\pi)$ 位之后，
不改变路径前缀的真空。
然后 (9.3) 对任意剩余向量成立，
故 $R_\pi W_\pi e_Mh$ 在路径前缀上准确取 $|\pi\rangle$，
后面的向量可以任意。
该前缀已经首达阈值 $q$，所以无论后面物理位为何，
输出都属于 (10.1) 的 good 集。
逐项相加给 (10.2)，于是 (10.13) 适用。

这说明 §9 中不能再用原最高前缀系数法处理的池内后停权，
仍被本节的多尺度方法覆盖。
它关闭的是这套“完整首列仍支持在吸收 good 区域”的解析目标桥。

一般 operator-valued 列目标可以没有 (10.2) 的支持限制；
本节没有排除这种目标，也没有对任意完整联合尾理想给出上界。
单个 $G\Omega$ 的精确支持已足以应用 (10.13)。若只有近支持，或池宽超出 (10.6) 可付的尺度，则须另付费用：[真实单位的反例](R236-appendix-faithful-vacuum-support-and-nonuniform-column-repair.md)给完整坏列趋零而精确解析修复范数指数增长，不能直接把近支持代入 (10.13)。

## 11. 当前可复用的接口与尚缺条件

本稿已经给出：

1. 有任意剩余尾的精确有限树因式分解；
2. 仅按层收费的两个可逆变换及全部吸收叶的完整源；
3. 源的路径面积费用和统一正质量的早吸收事件；
4. 纯模型中的有界 WOT 目标；
5. 两尺度的条件性指数相容；
6. 返回原内积的明确目标费用，以及当前 raw 路径目标的解析提升指数下界；
7. 任意复路径权和公共池后算子权的实际真空比上界 $4\,2^{-q}/\sqrt{15}$（含完整相对 carry）；
8. 全部 good 首列的多尺度上界 $4\sqrt2e^{-q/64}$，覆盖路径停止后仍在池内的任意实际尾权，且纯上界不依赖池宽。

仍未给出：

- 对实际 $T$ 或同一正常见证的 $S,Z$ 双行，满足全部费用的完整树源；
- 返回原内积后统一有界且有非零正常锚的实际目标；
- 不满足 (10.2) 的完整 good 首列支持限制、且仍支付实际全部源费和非零正常锚的目标；
- 任何新的临界实际排核、正常湮灭消去或普通 ISP 完成结论。

后续须改变完整首列的支持结构，或另付超出 (10.6) 的池宽费用；仅改变首达路径权或附加路径后的任意实际尾权不能恢复正常锚。完整联合尾理想和不受该支持限制的算子值列仍开。
