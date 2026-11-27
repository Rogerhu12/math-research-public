# R1119. 原 full47 的带符号 CM 坐标：反向项链迹与有限 Jacobi 读取

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**状态：几何恒等式与精确读取方法已证明；新的 Jacobi 数值尚待公开执行。**
本文给原 $X_{\mathrm{ns}}^+(47)$ 上四个基本 CM 类的带符号坐标来源。
它直接消费 R89 已证明的加权 Heegner–Jacobi 模性及 RSST 公式，
不重算层41，也不从 CM 比例的平方选择符号。
全部新的有限线性代数都有明确的完成条件；本文不预报其秩或坐标值。

## 1. 原曲线、原同源和所求坐标

固定
$$
p=47,\qquad N=p^2=2209,\qquad q=4513,\qquad
X=X_{\mathrm{ns}}^+(p),\quad J=\operatorname{Jac}(X).
$$
$C_\infty$ 是原23个尖点之和。
对 $D\in\{-3,-4,-7,-8\}$，令 $y_D\in X(\mathbf Q)$ 为原最大 CM 序的规范项链点，
并置
$$
u_D=23[y_D]-C_\infty,\qquad
w_D=|\mathcal O_D^\times/\{\pm1\}|,\qquad
r_D=\begin{cases}N,&D\text{ 为奇数},\\0,&D\text{ 为偶数}.\end{cases}
\tag{1119.1}
$$
为避免混淆，$r_D$ 始终表示 Jacobi 的余数标号；
点比例另记为 $\rho_D$。

四个二次域在47处均惰性，且其最大序类数均为一。
原基本点及下面实际源的次数为：

| $D$ | $j(y_D)$ | $w_D$ | $r_D\bmod 2N$ | $\deg Y_{DN,r_D}$ |
|---:|---:|---:|---:|---:|
| $-3$ | $0$ | $3$ | $N$ | $16$ |
| $-4$ | $1728$ | $2$ | $0$ | $24$ |
| $-7$ | $-3375$ | $1$ | $N$ | $48$ |
| $-8$ | $8000$ | $1$ | $0$ | $48$ |

使用 [R71 §1](R71-necklace-isogeny-polarization-and-level41-spectrum.md)
对一般 $p$ 已构造的实际整项链同态
$$
\mathfrak q=\varphi r_C:J_0(N)\longrightarrow J,\qquad
\mathfrak q^\dagger=r_C^*\lambda,\qquad
\mathfrak q\mathfrak q^\dagger=\kappa.
\tag{1119.2}
$$
$\lambda$ 取一个项链的全部无序对跖对子，$r_C^*$ 恢复有序对子。
R71 的命题1证明 $\mathfrak q$ 恰保留真正的 $N$-new、Fricke $+$ 部分，
并在该部分与**完整原 $J$** 之间给有理同源。
本节使用这一一般命题，不把 R71 的层41数值谱搬到层47，
也不把它缩成某个未指定的 Heegner 商。

由 [R1093](R1093-certified-original-Gaussian-CM-generator-and-full-MW-lattice.md)、
[R1096](R1096-certified-original-CM-moving-units-and-odd-Hecke-height-basis.md)，
原整 Hecke 代数及 MW 格满足
$$
\mathcal T=\mathbf Z_q[H],\qquad H=T_3+T_5,\qquad
\operatorname{rank}_{\mathbf Z_q}\mathcal T=73,\qquad
M=\mathcal T u_{-4}.
\tag{1119.3}
$$
因而每个 $\rho_D$ 由
$$
u_D=\rho_Du_{-4}
\tag{1119.4}
$$
唯一确定，并属于 $\mathcal T$。这里首先是在实际有理 Hecke 代数上定义比例，
再由 (1119.3) 得到其 $q$ 整性；没有假定一个任意模符号基是原整 MW 基。

## 2. 包括偶判别式的原源点及粗模权重

沿用 [R89 §1](R89-signed-CM-coordinates-and-actual-T2-translation.md) 的定义：
对 $\Delta<0$、$r^2\equiv\Delta\pmod{4N}$，
$$
Y_{\Delta,r}=
\sum_{\Gamma_0(N)\backslash\mathcal Q^+_{N,\Delta,r}}
 \frac{[z_Q]}{e_Q},
\qquad
y_{\Delta,r}=[Y_{\Delta,r}-\deg(Y_{\Delta,r})\infty].
\tag{1119.5}
$$
$\mathcal Q^+_{N,\Delta,r}$ 中的形式 $[A,B,C]$ 满足
$A>0$、$N\mid A$、$B\equiv r\pmod{2N}$、$B^2-4AC=\Delta$，
而 $e_Q$ 是除去 $\{\pm1\}$ 后的实际稳定子阶。
次数零化中的尖点 $\infty$ 固定不变。

### 2.1. 本原性、导子和 $r_D$

对本文的 $\Delta=Dp^2$、$r=r_D$，写
$$
Q=[p^2a,p^2b,c],\qquad p^2b^2-4ac=D.
\tag{1119.6}
$$
模 $p$ 得 $p\nmid ac$。任何公因子的平方须整除 $Dp^2$，
所以奇公因子均不可能；当 $D=-4,-8$ 时还必须单独排除公因子2。

若2整除 (1119.6) 的三个系数，则 $a,c$ 都为偶数，
且 $b=2b_0$，从而
$$
D/4=p^2b_0^2-ac\equiv b_0^2\pmod4.
$$
对 $D=-4,-8$，左边分别为 $3,2\bmod4$，均非平方。
故这两个偶判别式的源也本原。
因此每个源点的 CM 序均为判别式 $Dp^2$、导子 $p$ 的序；
其单位只有 $\{\pm1\}$，所以
$$
e_Q=1\quad\text{对四个源的每一点成立。}
\tag{1119.7}
$$

若 $\tau$ 为源参数，$X_0(p^2)\simeq X_{\mathrm{sp}}(p)$ 的中间参数
$\tau_0=p\tau$ 满足形式 $[a,pb,c]$，判别式为 $D$。
因此中间曲线有最大 CM，并带有
$$
A=\langle\tau_0/p\rangle,\qquad B=\langle1/p\rangle,
\qquad \sqrt D=2a\tau_0+pb.
$$
由于 $p\nmid2a$，得到
$$
A=\sqrt D\,B.
\tag{1119.8}
$$
$\sqrt D$ 在射影非分裂 Cartan 中正是唯一对合，故 (1119.8) 是原对跖条件。

反过来，给定最大 CM 曲线及一个有序对跖对子，
取与两条线相容的格基；其中间形式 $[a,b_0,c]$ 满足 $p\mid b_0$。
写 $b_0=pb$ 即返回 (1119.6)。由于 $D$ 为奇数时 $b$ 为奇数，
$D$ 为偶数时 $b$ 为偶数，源的中间系数 $p^2b$ 恰给 (1119.1) 的
$r_D=N$ 或 $0$。不能用同余方程的一个任意平方根替换这个实际标号。

存在性的具体形式可取
$$
[N,N,(N-D)/4]\quad(D\text{ 奇}),\qquad
[N,0,-D/4]\quad(D\text{ 偶}).
\tag{1119.9}
$$

有序对由 $B\in\mathbf P^1(\mathbf F_p)$ 决定，共48个。
非标量 CM 单位在惰性 $p$ 处没有固定射影线，
所以单位商在有序对上自由作用。
因此不同有序粗模点共有 $48/w_D$ 个，且由 (1119.7) 每个源权为一。

### 2.2. 实际反向 incidence 的重数

复合对应 $\mathfrak q^\dagger$ 的泛纤维次数为48。
在四个特殊点上，保留对应闭包的真实拉回重数，得到
$$
\boxed{\ \mathfrak q^\dagger([y_D])=w_DY_{DN,r_D}
       \quad\text{作为非尖点循环。}\ }
\tag{1119.10}
$$
其中 Gaussian 情形需要区分两个阶段。

- $D=-3$：阶三单位不能固定无序两点集，
  因而 $\lambda$ 的 incidence 粗模映射有分歧3；
  恢复次序后得到16个点，各重数3。
- $D=-4$：射影单位 $i$ 本身就是对跖对合，固定每个
  **无序**对跖对子。因此这个阶段的对象仍有阶二稳定子，
  不能先在 $\lambda$ 阶段额外乘2。
  恢复有序对子后该稳定子消失，$r_C$ 的粗模映射在此分歧2。
  两种次序给同一个有序粗模点，最终是24个点，各重数2。
- $D=-7,-8$：没有额外射影单位，得到48个点，各重数1。

三个情形总次数均为48。特别 (1119.7) 的源权1与
(1119.10) 的目标稳定子重数 $w_D$ 是不同来源，
不能再给源的 Gaussian 或 cubic 项除以2或3。

反向对应保持尖点，故 $\mathfrak q^\dagger(C_\infty)$ 是次数 $23\cdot48$
的尖点循环。由 Manin–Drinfeld，次数零尖点差在有理 Jacobian 中为零。
于是
$$
\boxed{\ \mathfrak q^\dagger u_D
       =23w_D\,y_{DN,r_D}. \ }
\tag{1119.11}
$$
这是同一个 (1119.2) 的伴随，并非另选的跨曲线 trace。
它也说明这些次数零 Heegner 类已落入实际 new、Fricke $+$ 部分。
本节及下一节使用的是 $\mathbf Q$ 同源范畴中的等式；
没有假定 $\mathfrak q^\dagger$ 在4513处是整同源同构。

## 3. 真正的带符号比例及 $B_q$ 规范

直接消费 R89 引理1：加权且次数零化的
$y_{\Delta,r}$ 的 Hecke 特征分量与权二、指标 $N$ 的
holomorphic Jacobi 特征形式 $\phi_f$ 的系数
$c_f(\Delta,r)$ 成同一比例。
该命题使用允许全部判别式的 Borcherds 已刊模性及勘误、
粗模权 $1/e_Q$ 和 Manin–Drinfeld，
因此适用于本文与 $N$ 不互素的四个判别式 $DN$。
这里不另作一个只对基本判别式有效的替代论证。

R1093 给 $u_{-4}$ 在全部73个 Hecke 嵌入上非零；
结合 (1119.11) 和 $\mathfrak q^\dagger$ 的单射性，
$y_{-4N,0}$ 的每个对应分量也非零。
因此抽象 Jacobi 特征线的参考系数 $c_f(-4N,0)$ 均非零。
于是
$$
\boxed{\quad
\rho_{D,f}=\frac{w_D}{2}
 \frac{c_f(DN,r_D)}{c_f(-4N,0)} .
\quad}
\tag{1119.12}
$$
在实际半单 Hecke 代数中逐嵌入汇合，即为 (1119.4) 的唯一 $\rho_D$。

确切地，将 (1119.12) 乘以
$\mathfrak q^\dagger u_{-4}=46y_{-4N,0}$，
右边得到 $23w_Dy_{DN,r_D}=\mathfrak q^\dagger u_D$；
再用 $\mathfrak q^\dagger$ 单射即得 (1119.4)。
整个证明没有除以未知的极化单位：
原 $\kappa$ 和共同的23在同一反向来源中取消。
也没有选择平方根、复周期相位或某个实嵌入的正号。

令
$$
B_q=q+1-T_q,\qquad D_4=B_qu_{-4}.
$$
R1089 已证明 $B_q\in\mathcal T^\times$。
用于 R1103 原 QC 坐标的真正基本点坐标为
$$
\boxed{\quad c_{y_D}=\rho_DB_q^{-1},\qquad
             u_D=c_{y_D}D_4. \quad}
\tag{1119.13}
$$
而 $B_qu_D=\rho_DD_4$。
这两种比例不能混用；特别 $c_{y_{-4}}=B_q^{-1}$，
并非恒等元。本文的后继读取以 (1119.13) 为目标。

## 4. 原 RSST 整数路径和：有限且不丢正负向量

以下是新层47计算的完整方法；没有使用层41已有数值。

### 4.1. 有限辅助列表

首辅助判别式和标号固定为
$$
\Delta_0=-11,\qquad r_0=2027,\qquad
2027^2+11=465\cdot8836.
\tag{1119.14}
$$
若首辅助尚未覆盖全部参考分量，继续请求中固定的有限列表：
所有 $\ell\le199$、$\ell\equiv3\pmod4$、
$\left(\frac{-\ell}{47}\right)=1$ 的素数，
除去已用的11后按递增次序取 $\Delta_0=-\ell$。
对每一个辅助取 $r_0^2\equiv-\ell\pmod{4N}$ 的规范根，
并在回执中打印实际根和同余核验。
$\ell=47$ 不在该列表，$-\ell$ 均为负素基本判别式。

不能假定这一个有限辅助列表一定在所有特征线上非零。
完成条件是 §6 的真实共同参考秩73；否则只保留已经完成的辅助及其秩，
不输出缺失分量的坐标。

### 4.2. 原权二、star $+$ 功能

使用 R89 §4 所核的 RSST Theorem 4.15、Remark 4.19。
在实际 cuspidal modular symbols 上，
$$
j_{\Delta,r}^{(\Delta_0,r_0)}(\sigma)
=\sum_{Q\in\mathcal Q_N(\Delta\Delta_0,rr_0)}
  \chi_{N,\Delta_0}(Q)\,C_Q\cdot\sigma,
\quad
C_Q\cdot\{\alpha,\beta\}
=\frac{\operatorname{sgn}Q(\alpha)-\operatorname{sgn}Q(\beta)}2.
\tag{1119.15}
$$
对本文所有辅助与目标，$\Delta$ 及 $\Delta\Delta_0$ 均非平方；
程序仍逐项核查这个输入。
权二 holomorphic 情形的 $\varepsilon=-1$ 给
$\operatorname{diag}(-1,1)$ 特征 $(-1)^{2-1}\varepsilon=+1$，
所以采用真实 **star $+$** 空间。

取一条实际生成路径 $\{g0,g\infty\}$，
$g=\left(\begin{smallmatrix}\alpha&\beta\\\gamma&\delta\end{smallmatrix}\right)
\in\mathrm{SL}_2(\mathbf Z)$，置 $\mathcal D=\Delta\Delta_0>0$。
将形式变成 $\widetilde Q=[a,b,c]$ 后，
贡献只可能有 $ac<0$。
正 $a$ 部分的完整枚举为
$$
b^2<\mathcal D,\qquad
n=(\mathcal D-b^2)/4\in\mathbf Z_{>0},\qquad
a\mid n,\ a>0,\qquad c=-n/a.
\tag{1119.16}
$$
这是完整有限范围，不是一个经验性的系数窗口。
恢复原形式时
$$
\begin{aligned}
A&=\delta^2a-\delta\gamma b+\gamma^2c,\\
B&=-2\delta\beta a+(\delta\alpha+\beta\gamma)b-2\gamma\alpha c.
\end{aligned}
\tag{1119.17}
$$
保留 $N\mid A$ 与下面两个真实余数条件。

因为 $N$ 为平方且 $(\ell,N)=1$，
R89 中的广义 genus character 在这里仍是普通 $-\ell$ genus character；
可利用其完整 $\mathrm{SL}_2(\mathbf Z)$ 不变性在 $\widetilde Q$ 上计算：
$\ell\nmid a$ 时取 $(a/\ell)$，否则若 $\ell\nmid c$ 取 $(c/\ell)$，
若三系数均被 $\ell$ 整除则取零。
判别式关系保证最后一种分支的判断相容。

正 $a$ 的交数是 $-1$。
取负形式时，交数与 $\chi_{-\ell}$ 同时变号，
故每个 (1119.16) 对路径行的贡献正是
$$
-\chi_{-\ell}(\widetilde Q)
\left(
 \mathbf1_{B\equiv rr_0\ (2N)}
+\mathbf1_{B\equiv-rr_0\ (2N)}
\right).
\tag{1119.18}
$$
本文四个 $r=0,N$ 都满足 $r=-r\bmod2N$；
由于 $r_0$ 为奇数，这两个指标在命中时相同，
但它们来自不同向量 $Q,-Q$，**仍须各计一次**。
用集合去重会把所有四个目标功能错误地减半。
R89 的 Jacobi 生成级数中的共同正负向量因子也同样保留，
最后只在实际系数比例中取消。

## 5. 精确相对功能与真实 new、Fricke $+$ 投影

先在 $\mathbf Q$ 上重建层2209、权二、star $+$ 的实际 modular-symbol 空间。
原已认证维数是 ambient189、cuspidal165、new157；
逐实际 Fricke 作用取 $+$ 部分得到73维，
另84维为 new Fricke $-$。
本轮脚本核 ambient189、new157、new+73 的实际维数及完整 star/Fricke 算子关系；cuspidal165 消费 R1080 已认证的来源，不冒称本轮另算。不能按目标维数截断。

令 $E$ 是原基符号在全部实际生成路径上的取值矩阵，
$j_{\Delta,r}^{(a)}$ 是 (1119.18) 的整数行所对应的列。
先精确解
$$
Ew_{\Delta,r}^{(a)}=j_{\Delta,r}^{(a)}
\quad\text{over }\mathbf Q,
\tag{1119.19}
$$
并回代核全部路径关系，包括椭圆关系。
只有已满足这些关系的列才是实际相对上同调功能。

令 $P$ 为在该同一 ambient 坐标中得到的189行、73列
new、Fricke $+$ 基矩阵。
请求预先固定有限 Hecke separator 列表，包括
$T_3+T_5$ 以及 $T_2+cT_3+c^2T_5$ 类型；
范围与次序由请求固定，不在遇到结果后改变。
对一个候选 $S_{\mathrm{full}}$，记
$$
F_S(X)=\operatorname{charpoly}(S_{\mathrm{new}}),\qquad
S_{\mathrm{full}}P=PS_{\mathrm{new}}.
$$
只有在 $\mathbf F_q$ 上实核
$
\gcd\!\left(
 F_S,\operatorname{charpoly}(S_{\mathrm{full}})/F_S
\right)=1
\tag{1119.20}
$$
后，才取
$$
Q_S=\operatorname{im}F_S(S_{\mathrm{full}}).
$$
程序核 $\operatorname{rank}Q_S=116$、
$[P\ Q_S]$ 秩189，并令 $\pi$ 为其逆矩阵的前73行。
完整核验为
$$
\pi P=I,\qquad
\pi T_{n,\mathrm{full}}=T_{n,\mathrm{new}}\pi
\quad(n=2,3,5).
\tag{1119.21}
$$
原 Hecke 交换性使该分离的补空间对整个 Hecke 代数不变。
得到真正投影列
$$
v_{\Delta,r}^{(a)}=\pi w_{\Delta,r}^{(a)}.
\tag{1119.22}
$$
Separator 只用于付清补空间，**最终坐标生成元始终是 $H=T_3+T_5$**。

RSST 权二的边界修正只在 cuspidal 输入上消失。
(1119.22) 是实际 cuspidal new 同调投影的对偶；
所以这里确实只对边界为零的输入应用 (1119.15)。
没有先对任意相对路径宣称边界项为零，再以维数修补。

(1119.19)、$P$ 和所需 Hecke 矩阵先在 $\mathbf Q$ 上精确形成，
送入 $\mathbf F_q$ 前逐项核分母为 $q$ 单位；
投影 $\pi$ 的上述矩阵运算实际在 $\mathbf F_q$ 上完成。
这仍是原有理 Hecke 投影的准确约化：原 $P$ 不变，
所以两个首一特征因子在 $\mathbf Z_q[X]$ 中整除；
(1119.20) 使它们的 resultant 为单位。
Bezout 因而在 $\mathbf Z_q[S_{\rm full}]$ 中给出真正的 new+ 幂等投影。
其核为原互补特征部分，模 $q$ 核正是 $Q_S$，
而 $P$ 的单位 minor 及 $[P\ Q_S]$ 的满秩固定其像和坐标。
故 (1119.21)–(1119.22) 读取的是这个整延拓的约化；
没有假称程序先在 $\mathbf Q$ 上计算了 $\pi$。

同一辅助的四个功能始终使用同一尺度。
不分别重标参考列和目标列，也不在未知饱和的数域基中直接约化。

## 6. 多辅助共同参考，而非假定每一个辅助非零

用 $a$ 标记已经完成的辅助对，置
$$
v_a=v_{-4N,0}^{(a)},\qquad
K_a=[v_a,Hv_a,\ldots,H^{72}v_a].
$$
垂直堆叠所有 $K_a$ 得到 $\mathcal K$。
只有
$$
\operatorname{rank}_{\mathbf F_q}\mathcal K=73
\tag{1119.23}
$$
时才读取全部坐标；回执同时保留一个实际非零73阶 minor
以及所有辅助的秩增量。

R89 的一维 Jacobi 特征线及 Hecke 等变性说明，
对每个辅助和每个目标，真实系数比
$$
b_D=\frac{c(DN,r_D)}{c(-4N,0)}
$$
满足
$$
v_{DN,r_D}^{(a)}=b_D(H)v_a .
\tag{1119.24}
$$
一个辅助构造可以在某些块为零，甚至整列为零；
(1119.24) 对它仍然成立，但不能从该列单独作除法。
(1119.23) 恰保证没有一个剩余 Hecke 块在所有参考列中都缺失。
因此堆叠系统
$$
\mathcal K\,\mathbf b_D
=\operatorname{stack}_a(v_{DN,r_D}^{(a)})
\tag{1119.25}
$$
有唯一的73维升幂坐标解，且必须回代全部行。
同样必须得到 $b_{-4}=1$。

这些解的实际 $q$ 整性已经由
$b_D=(2/w_D)\rho_D$、(1119.3) 支付；
这里没有由一次有限域可解反推一个未经证明的全局有理关系。
精确有理关系来自 §§2–3，有限计算只读取其约化并认证所有分量都被读到。

若固定辅助列表用尽后秩仍小于73，
算法输出准确未完成状态及已完成辅助，
不以任意补列或任选非零特征向量构造缺失比例。

## 7. 与原 Hodge/Hecke 坐标的完整桥及 $B_q$

记 $P_H$ 为 $H=T_3+T_5$ 在实际73维 new+ 空间上的特征多项式。
它的模 $q$ 多项式须与 R1096/R1101 的原 Hodge $H$ 特征多项式完全相同；
后者的 SHA-256 为
$$
\texttt{990a3205813f9785f40b97a754092530d9797edaee616b2814f2382530d06b37}.
$$
这只是第一项核验。对 $n=2,3,5$，
从同一共同参考系统读取 $p_n(H)=T_n$，
先在 new+ 空间完整矩阵回代，再核原 Hodge row-action
$$
p_2(M_H)=M_2,\qquad
p_3(M_H)=M_3,\qquad
p_5(M_H)=M_5,\qquad
p_3+p_5=X\pmod{P_H}.
\tag{1119.26}
$$
因此输出的 $b_D,\rho_D,c_{y_D}$ 是原已认证的
$\mathbf F_q[X]/P_H$ 坐标，而非只凭两特征多项式相同选择一个嵌入排列。
源采用列作用、原 Hodge 采用行作用时，均以明确的多项式等式连接，
不得在中间暗换转置方向。

此外必须在同一个 $P$ 上读取真正的 $T_{4513}$：
先构造其精确矩阵，再由堆叠参考的
$T_{4513}v_a$ 求 $p_q(X)$，并核
$$
p_q(H)=T_{4513}
\quad\text{完整矩阵等式。}
\tag{1119.27}
$$
R1089 的旧 $T_{4513}$ 特征多项式 SHA-256
$$
\texttt{ca554eaecfa7f5ac349fdf9db69f32e584eb45c0787714e97e6ef3c44e1cba62}
$$
作为实际整数特征多项式的必要复核，
但它本身不能确定 $T_{4513}$ 在 $H$ 代数中的坐标。
同时核
$$
\det(1-T_{4513})=551\pmod q,
\tag{1119.28}
$$
与原 $\#J(\mathbf F_q)$ 证书一致。
于是
$$
\overline{B_q}=1-p_q(X)\in(\mathbf F_q[X]/P_H)^\times
$$
有唯一逆，最终读取
$$
\boxed{
\overline{\rho_D}=\frac{w_D}{2}\,\mathbf b_D(X),\qquad
\overline{c_{y_D}}=
 \frac{w_D}{2}\,\mathbf b_D(X)(1-p_q(X))^{-1}
 \pmod{P_H}.
}
\tag{1119.29}
$$
保留 $B_q$ 是为了与原 $D_4$、CM 首对数和 QC 第一层严格同源；
不能因为它是单位就删去其数值作用。

## 8. 公开执行的证书范围及尚未宣称的结论

新的消费者只需完成以上有限任务：

- 固定 Sage image、实际 GP 版本、源码及请求 hash，
  有限辅助列表、总预算与保留时间；
- 原全部路径、有限整数枚举、两个正负指标、
  精确 $Ew=j$ 回代及实际 new+ 投影；
- 所有分母单位，原 $P_H$、$M_2,M_3,M_5$ 桥，
  每一辅助的共同尺度和共同参考 rank73；
- 四个基本类的完整73维坐标与全部堆叠回代，
  实际 $T_q$ 坐标、旧特征多项式 hash、(1119.28) 及 $B_q$ 逆。

正文没有执行这些数学代码，也没有填入尚未得到的 CM 坐标值。
一次合格的公开回执将支付 (1119.29) 的指定数值，
无需重复 R1093 的 CM 高矩或在原四点上运行长整数倍对数链。
它仍不单独给第三类微分、QC 首jet秩或八个原残余盘的有理唯一性。

本篇的几何比例 (1119.12) 是特征零的实际带符号关系；
有限辅助不足只影响这次读取是否完成，不否定该几何关系。
所有候选/预算失败均应保留已完成输出，
不能把缺失块默认为零或由其它点的低矩替代。

## 9. 所消费的准确来源

- [R71 §1](R71-necklace-isogeny-polarization-and-level41-spectrum.md)：
  一般 $p$ 的同一 $\mathfrak q=\varphi r_C$、
  $\mathfrak q^\dagger=r_C^*\lambda$ 和完整 new、Fricke $+$ 范围。
- [R89 §§1、3、4](R89-signed-CM-coordinates-and-actual-T2-translation.md)：
  已刊 Borcherds/GKZ 的加权次数零源、实际惰性反向 incidence、
  RSST Theorem 4.15 / Remark 4.19、star $+$、整数路径及相对功能投影。
  本文新增的是 full47 四个惰性判别式（包括 $-4,-8$）的精确重数与同源读取；
  不复制层41的数值证书。
- [R1080](R1080-certified-full-level47-Jacobian-rank.md)、
  [R1089](R1089-certified-full-level47-auxiliary-Bq-and-component-groups.md)：
  原完整73维 new+ 来源、实际 $T_q$ 多项式和 $B_q$ 单位。
- [R1093](R1093-certified-original-Gaussian-CM-generator-and-full-MW-lattice.md)、
  [R1096](R1096-certified-original-CM-moving-units-and-odd-Hecke-height-basis.md)、
  [R1101](R1101-certified-original-level47-smallest-odd-Hecke-basis.md)：
  原 MW 生成元、同一 $H=T_3+T_5$、原整 Hodge 坐标及实际多项式桥。
- [R1103](R1103-original-CM-tangents-finite-field-third-kind-and-QC-first-jets.md)：
  $D_4=B_qu_{-4}$ 下的原 QC 坐标规范。
