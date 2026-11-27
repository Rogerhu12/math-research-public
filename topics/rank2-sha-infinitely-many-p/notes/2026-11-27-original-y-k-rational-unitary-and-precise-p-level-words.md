# 原共同 Y/K 的有理等距变换、准确 p 级字及 norm11 端点

日期：2026-11-27。状态：本文的有理等距矩阵、原 split p Schwartz 稳定子与至少一个准确导子 p^n 的角色，以及固定 norm11 角端点的完整 sigma 身份均为手证。没有新增数学执行。本文只排除把所显示的单个变换向量未经投影当成固定有限未分歧 canonical 族的步骤；不排除某个另行证明的有限求和消去全部新字。

## 1. 原六维整框架与实际有理对应

使用 [R1040](../results/R1040-new-e3969-whole-companion-frame-and-sixth-degree-carry.md) §10 的原六行：
$$
\begin{aligned}
Y&=(7,4+\omega,3-\omega,3\delta,2\delta,2\delta),\\
H&=(1,-1,-1,0,0,0),\\
K&=(-1,\omega,\omega^2,\delta,0,0),\\
J&=(0,0,0,0,1,-1),\\
A&=(1,-\omega^2,-\omega,0,-\delta,-\delta),\\
N&=(0,-2,2,2,-1,-1).
\end{aligned}
\tag{1}
$$
其 Hermitian Gram 为 $\operatorname{diag}(126,3,6,2,9,14)$，行列式的范数为 $756^2$。因此在任何 $p>1296$ 的原普通分裂处，这六行及逆矩阵都保持原整格；特别 $(Y,K)$ 与其余四轴给真正的整直和坐标，而非只在 $K$ 上的一组抽象基。

原普通射线仍记
$$
\kappa=\pi_0/\bar\pi_0,\qquad
\kappa\bar\kappa=1,\qquad v_{\mathfrak p}(\kappa)=1.
$$
固定非零有理整数 $c$，置
$$
D_c=1+21c^2,\quad
a=\frac{1-21c^2}{D_c},\qquad
b_n=\frac{2c}{D_c}\kappa^n,\qquad n\ge1.
\tag{2}
$$
本节排除 $2cD_c(1-21c^2)$ 的素因子。因此 $a$、$2c/D_c$ 在当前 p 都是单位，且
$$
v_{\mathfrak p}(b_n)=n,\qquad
v_{\mathfrak p}(\bar b_n)=-n.
$$
完全明确的选择是 $c=1$，此时 $a=-10/11$、$b_n=\kappa^n/11$；当前 $p>1296$ 已支付这些单位条件。

在原 $(Y,K)$ 行坐标上取
$$
g_n=
\begin{pmatrix}
a&21b_n\\-\bar b_n&a
\end{pmatrix},
\tag{3}
$$
在其余四行上取恒等。直接计算
$$
a^2+21b_n\bar b_n=1,\qquad
g_n\begin{pmatrix}126&0\\0&6\end{pmatrix}
\bar g_n^{\,t}=
\begin{pmatrix}126&0\\0&6\end{pmatrix},
\qquad \det g_n=1.
\tag{4}
$$
因此这是 $K$ 上真实的 Hermitian 等距对应。它将原观察送到
$$
Y_n=aY+21b_nK,\qquad
a^{-1}Y_n=Y+t_nK,\quad
t_n=\frac{42c}{1-21c^2}\kappa^n\longrightarrow0
\quad(\mathfrak p\text{ 进}).
\tag{5}
$$

矩阵 (3) 一般有固定的 $D_c$ 分母，不能称为处处整的自同构或只含 p 次数的整同源。将固定分母、(1) 的固定逆分母及相应 $\pi_0^n,\bar\pi_0^n$ 分母一起清掉，得到原 $E^6$ 上真正的有限同源对应。其远离 p 的成本仅含一份固定有限集合。

若要在指定原坏处保持原 Schwartz，而不只保持一个固定有限轨道，可先取 c 被所需固定模数充分整除，再将原 ray 细化到对应 $\kappa$ 的单位类；(2) 在这些处趋于恒等，故确可保持其实际开稳定子。新固定分母的来源必须另列。本文的 p 处结论不以这项细化为假设。

## 2. 原 split p Schwartz 的完整稳定子

在好分裂 p，原六 sigma 的有限 Schwartz 是六个原球的张量。由 (1) 的整可逆性，它在所写六坐标中仍为
$\mathbf1_{\mathbf Z_p^6}$。在 split unitary Schrödinger 模型，(3) 的 determinant 为一，故原 Weil 作用就是变量变换，不产生额外绝对值或未付 unit splitting。采用反变规范，记变换向量
$$
\phi_n(x)=\mathbf1_{\mathbf Z_p^6}(g_nx).
\tag{6}
$$
换成正变规范只把 $g_n$ 改成逆，以下准确稳定子不变。

令 $u\in\mathbf Z_p^\times$，原 Y 的紧环面在该块上为
$t_u=\operatorname{diag}(u,1)$，在其余四轴上为一。原好处分量在这些 units 上未分歧，所以不存在一个可改变支撑的附加相位。完整共轭是
$$
g_nt_ug_n^{-1}=
\begin{pmatrix}
a^2u+21b_n\bar b_n&
21ab_n(1-u)\\
a\bar b_n(1-u)&
21b_n\bar b_nu+a^2
\end{pmatrix},
\qquad \det(g_nt_ug_n^{-1})=u .
\tag{7}
$$
两对角项永远整，右上项永远整；左下项的估值准确为
$$
-n+v_p(1-u).
$$
因 determinant 是单位，一个这样的矩阵保持整格当且仅当其全部条目整。这支付了正反两个包含，而非只给一个充分条件。因此
$$
\boxed{\operatorname{Stab}_{\mathbf Z_p^\times}(\phi_n)
=1+p^n\mathbf Z_p.}
\tag{8}
$$

这一步使用的是同一个原好处球和真实 (3)，不是从复范数不变推断的局部不变性。

## 3. 至少一个准确导子 p^n 的新字

由 (8)，$\phi_n$ 的紧环面轨道通过有限群
$$
\mathbf Z_p^\times/(1+p^n\mathbf Z_p)
$$
作用。对其全部角色采用实际有限投影
$$
e_\vartheta\phi_n=
\frac1{\#G_n}\sum_{u\in G_n}
 \vartheta(u)^{-1}t_u\phi_n .
\tag{9}
$$
在特征零中，这些幂等完整分解原向量。

对 $n\ge2$，如果所有导子恰为 $p^n$ 的 (9) 都为零，则每个留下的角色在 $1+p^{n-1}\mathbf Z_p$ 上平凡，于是该群固定 $\phi_n$，与 (8) 矛盾。对 $n=1$，若全部非平凡 tame 投影为零，则整个 $\mathbf Z_p^\times$ 固定 $\phi_1$，同样矛盾。故
$$
\boxed{\text{每个 }n\ge1\text{ 都有至少一条非零 }
e_\vartheta\phi_n\text{ 的导子准确为 }p^n.}
\tag{10}
$$

原固定有限曲线族在充分大的好 p 处，其指定 CM canonical 分量是 p 处未分歧的。原 p-old 向量仍在该未分歧角色的局部表示中；不能把 (10) 中另一个实际紧环面角色改称原未分歧字。因而 (5) 的整个角来源不能仅凭 Hermitian 等距、坏处不变或固定复范数就继承这个固定族的中央零。

(10) 的非零严格发生在所显示的原 Schwartz 向量及紧环面投影层面；尚未断言这些分量经后续 theta 求和、伴随平均或完整中央积分后非零。若这些后继操作消去全部新字，必须给出它们在同一原测试上的实际身份。

可以对 (6) 取未分歧投影，也可以求某个有限 Hecke 组合。但必须重新写其真实测试：被删去的 (9) 与原 unit cut、Mellin 导数和 (5) 的角差同时在场。本文没有证明它们的中央值非零，也没有证明任意有限求和都保留新字；所缺的确切步骤是一个使全部这些新字消失且保留所需角导数的实际恒等式。

## 4. 一个完全固定的角端点及其 CM 质量边界

原 (1) 还给无需 p 变化的准确身份
$$
Y+K=2\delta(-\delta,-\omega,-\omega^2,2,1,1).
\tag{11}
$$
括号内行的范数为11。令 $u=2\delta z$，使用原
$\sigma(\delta u)=\delta x(u)\sigma(u)^3$、
$\sigma(2u)=-2y(u)\sigma(u)^4$ 及
$\sigma(\zeta u)=\zeta\sigma(u)$，逐项相乘得到
$$
\boxed{
\prod_{j=1}^6\sigma((Y+K)_jz)
=2\delta\,x(u)y(u)\sigma(u)^{11}.}
\tag{12}
$$
这包括原全部半特征和绝对符号；若返回原 $\rho=-\nu_\sigma^{\otimes6}/84$，还须保这个 $-1/84$。

标准 odd degree11 的 principal 空间准确为
$$
\operatorname{span}_K\{xy\sigma^{11},\,x^4y\sigma^{11}\}.
\tag{13}
$$
前者从 $-z^6$ 起，后者质量为−1。因此质量核一维，但不能据此把它叫作一个 CM Hecke 本征来源。

以下直接在原 theta 线性化中检验这一点。取
$\gamma=3+\omega$，原完整算子为
$$
\mathcal N_\gamma=\gamma^{-1}[\gamma]_*[\bar\gamma]^*.
$$
其质量是在同一全七点纤维上对 $[\bar\gamma]^*(xy\sigma^{11})$ 作准确 theta trace。O 项为零。其余六个点是一个 $\mu_6$ 轨道。

这里六项相等并非忽略相位：原 geometric CM 作用 $\mathcal C_\zeta$ 与 canonical Weyl lift 满足
$$
\mathcal C_\zeta\mathcal T_U\mathcal C_\zeta^{-1}
=\mathcal T_{\zeta U},
$$
输入 $[\bar\gamma]^*(xy\sigma^{11})$ 的完整 principal 角色是一，原点质量泛函的角色也是一。故同一 trace 中的六项连同其 Gaussian、半周期和 CM 标量确实相等。每项非零：$\bar\gamma$ 在 $\ker\gamma$ 上可逆，其非零像是七挠点，不在二挠、$\ker\delta$ 或 O；原 sigma、x、y 在该点均非零，Weyl 指数也是非零数。于是
$$
\boxed{
m_0(\mathcal N_\gamma(xy\sigma^{11}))\ne0,\qquad
m_0(xy\sigma^{11})=0.}
\tag{14}
$$
所以 (12) 的 norm11 内层本身不是任一 $\mathcal N_\gamma$ 本征线。该固定角端点确为一个真实小来源，却没有因此增加一条已授权的 rank-two canonical 零。

## 依赖与继续使用的范围

- R1040 §10：原六维整框架及全部 theta 规范。
- R290、R316：原全局加性角色、好处分裂球、奇 sigma 和 Weil 规范。
- R816 §8：原 full-fiber pull/trace 及完整 theta carrier；本文沿用同一算子定义，不重算其 degree66 矩阵。
- R1042、R1044：原三 canonical 观察、共同 carry 和尚需保留的完整补域。

本笔记的输出是 (8)–(10) 这一准确投影成本及 (12)–(14) 这个固定来源边界。后继应检验真正的有限 Hecke/角求和是否在保留原中央测试时消掉新字，而非把 (5) 的无限角族逐个赋零。

## 6. 未分歧平均的整个球／环带公式

本节沿用 (1)–(8)，但将平均本身完整算出。所有有限平均先在特征零的原 Schwartz 空间进行；不能把下面的 $p$ 分母当作有界整测度的单位。

记
$$
q_n=\bar b_n/a,\qquad v_p(q_n)=-n,\qquad
B_r(x)={\bf1}_{p^r\mathbf Z_p}(x),\qquad
A_r=B_r-B_{r+1}.
\tag{15}
$$
从 $g_nx\in\mathbf Z_p^2$ 的第二行先解出
$k-q_ny\in\mathbf Z_p$。将它代回第一行，系数是
$(a^2+21b_n\bar b_n)/a=a^{-1}$，所以准确有
$$
\boxed{\phi_n(y,k)=B_0(y)\,
 {\bf1}_{\,k-q_ny\in\mathbf Z_p}.}
\tag{16}
$$
这是整个二维格，不仅是某个单位扇区。其余四个原坐标仍取原标准球。

取 $G_n=\mathbf Z_p^\times/(1+p^n\mathbf Z_p)$，用 (9) 的同一反变作用，即
$$
E_0\phi_n(y,k)=\frac1{|G_n|}\sum_{u\in G_n}\phi_n(uy,k).
$$
代表的选择不影响此有限和。若 $v_p(y)\ge n$，条件恰为 $k\in\mathbf Z_p$，每个 u 都满足。若 $v_p(y)=r<n$，条件恰为
$$
v_p(k)=r-n,\qquad u\equiv k/(q_ny)\pmod{p^{n-r}}.
$$
在 $G_n$ 中该陪集有 $p^r$ 个元素。若 $y\notin\mathbf Z_p$，没有贡献。由此得到没有遗漏的全式
$$
\boxed{
E_0\phi_n
=B_n\otimes B_0+
 \sum_{r=0}^{n-1}
 \frac{A_r\otimes A_{r-n}}{(p-1)p^{\,n-r-1}}.}
\tag{17}
$$
第一项也包括 $y=0$。各支在 $(y,k)$ 上不相交，所以其系数不能通过同支上的形式相消消去。特别 $r=0$ 支的系数估值准确为 $1-n$；整个原有限平均并非随 n 一致整。

同一计数还支付全部非平凡角色，而不仅是 $E_0$。若 $\vartheta$ 的准确导子为 $p^a$，$1\le a\le n$，置 $q_n^\circ=p^nq_n\in\mathbf Z_p^\times$，则在允许环带上
$$
\boxed{
E_\vartheta\phi_n(y,k)=
\sum_{r=0}^{n-a}
\frac{
 \vartheta(q_n^\circ)\,
 \vartheta(y/p^r)\,
 \vartheta(k/p^{r-n})^{-1}}
 {(p-1)p^{\,n-r-1}}\,
 A_r(y)A_{r-n}(k).}
\tag{18}
$$
证明仍是上述一个陪集上的角色求和：只有当 $\vartheta$ 在
$1+p^{n-r}\mathbf Z_p$ 上平凡时不消失，值为
$\vartheta(k/(q_ny))^{-1}$。这里每个角色只作用于显示的单位；没有将负赋值参数直接送进一个只定义在单位群上的角色。

(18) 显示实际新字是 **Y 与 K 的一对相反单位角色**，而非只在 Y 上任选一个新 twist。两轴及整个 unit 条件必须同时返回。

## 7. 回到原标准极化：完整二次相位不能省去

(17) 位于原好分裂处的自然极化。它不是此前
$\nu|_{L\in p^r}=\beta^r[P_{L,\kappa^r}]_*\nu$
的另一个写法。后者已经包含正式群、division 函数和 theta frame；必须先付二者间的实际交织。

Yang《Theta liftings and Hecke L-functions》§2.2 的 (2.25)–(2.28)、Corollary 2.14 给这一步的绝对公式。设原选定分裂嵌入下 $\delta=(x_0,-x_0)$，某一轴的 Hermitian 系数为 $\alpha_L$，并记
$$
c_L=x_0^3\alpha_L\in\mathbf Z_p^\times.
$$
原加性角色 $\psi_p$ 的导子为 $\mathbf Z_p$，自对偶 Haar 使
$\operatorname{vol}(\mathbf Z_p)=1$。从自然极化到原标准极化的交织为
$$
\boxed{
\mathcal U_L f(x)=
\psi_p(c_Lx^2/2)
 \int_{\mathbf Q_p}
 \psi_p(c_Lxy+c_Ly^2/4)f(y)\,dy.}
\tag{19}
$$
这是代数的有限 Gauss 计算；在紧开函数上积分只使用有限和及有理体积。
这里没有把一个 $p$-adic logarithm 放进复 Haar 积分。

在当前两轴，$\alpha_Y,\alpha_K$ 都是 p 单位；原其余四轴不变。式 (19) 的 $|c_L|^{1/2}$ 因子准确为1。它对所有整数 r 给
$$
\boxed{
\mathcal U_L B_r(x)=
\begin{cases}
p^{-r}\psi_p(c_Lx^2/2)\,B_{-r}(x),&r\ge0,\\
\psi_p(-c_Lx^2/2)\,B_r(x),&r\le0.
\end{cases}}
\tag{20}
$$
两式在 $r=0$ 相同，都等于 $B_0$。

对于 $r\ge0$，$y^2/4$ 在积分球上整，剩余 Fourier 积分直接给第一式。对 $r=-s<0$，完成平方
$y^2/4+xy=(y+2x)^2/4-x^2$。
若 $x\notin p^{-s}\mathbf Z_p$，分割为适当小球后每个非平凡线性字符和为零；否则平移仍保持原球，剩余二次 Gauss 积分
$$
\int_{p^{-s}\mathbf Z_p}\psi_p(c_Ly^2/4)\,dy=1.
$$
最后的1来自模 $p^{2s}$ 的单位二次 Gauss 和，其偶指数规范为 $p^s$，与 Haar 的 $p^{-s}$ 相消。没有留下可任选的二次根或 Weil 符号。

将 (20) 逐项代入 (17)，原标准极化中的整个向量是
$$
\boxed{
\begin{aligned}
(\mathcal U_Y\otimes\mathcal U_K)E_0\phi_n(y,k)
={}&\psi_p(c_Yy^2/2-c_Kk^2/2)\\
{}\cdot\Bigg\{&
p^{-n}B_{-n}(y)B_0(k)\\
&+\sum_{r=0}^{n-1}
 \frac{
 (p^{-r}B_{-r}(y)-p^{-r-1}B_{-r-1}(y))
 (B_{r-n}(k)-B_{r-n+1}(k))}
 {(p-1)p^{\,n-r-1}}\Bigg\}.
\end{aligned}}
\tag{21}
$$
在 $B_0(k)$ 上写入的负二次相位为1，所以第一项也完全正确。
(21) 包含全部球、环带、二次相位及所有 p 分母。
它的支撑在 $p^{-n}\mathbf Z_p^2$，而其局部常值尺度可取
$p^n\mathbf Z_p^2$。因此它是一个完全指定的有限
$(\mathbf Z/p^{2n})^2$ 向量，可以直接送入原完整 theta 构造；不需要猜一个 p-old 本征标量。

来源：
[Yang 原文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)，
§2.2，(2.25)–(2.28)、Corollary 2.14。
Corollary 2.14 只把 $B_0$ 锁回同一个 $B_0$；并没有把任意
$B_r$ 认作物理深限制。式 (20)–(21) 已把所需差异明确算出。

## 8. 实际 theta 与 Y 单位读者：哪一部分确实被消掉

这里把“投影后为零”限定到可直接核验的原向量，不以 (10) 的局部非零代替中央非零。

### 8.1 固定其它有限输入的准确有符号身份

在自然极化中置
$$
\phi_n^\pm(y,k)=
B_0(y){\bf1}_{\,k\mp q_ny\in\mathbf Z_p}.
$$
两者的整个平均由 (17) 可见完全相同，因此
$$
\boxed{E_0(\phi_n^+-\phi_n^-)=0.}
\tag{22}
$$
对任何固定的其余有限 Schwartz、原无限 Gaussian/Hermite 向量及原完整 theta 求和，(22) 都给整个 theta 来源零。它也给该来源上真正的
$$
{\bf1}_{Y\ {\rm unit}}\log\langle Y\rangle
\quad\text{以及任何已定义的完整 companion/cut 测试}
$$
读数为零。原因是整个输入向量先已为零，并非先在一个环带上删掉 log。

特别，(22) 的局部有符号部分不可能在删掉新字后继续携带一个未变的一阶角读数。这是一个真正投影结论；不需要猜测各新字的中央值。

### 8.2 原有理角的其它有限处必须同时保持

对 (3) 及 $b_n\mapsto-b_n$ 的两个实际有理变换，使用全局有理 Weil lift 将无限处变换转到所有有限处。这个 lift 的全局相位由原有理 splitting 唯一固定，不能逐处另选符号。

将 p 以外所有实际改变后的有限输入，连同原 H/J/N 投影，记为
$\Phi_{S,n}^{+}$、$\Phi_{S,n}^{-}$。S 只含原坏处、固定框架分母及
$2cD_c(1-21c^2)$ 的素因子；在其它有限处两者都是原球。
于是 p 处固定未分歧平均对整个有符号来源准确返回
$$
\boxed{
E_0\Phi_{n}^{+}-E_0\Phi_{n}^{-}
=(E_0\phi_n)\otimes
  (\Phi_{S,n}^{+}-\Phi_{S,n}^{-}).}
\tag{23}
$$
若这些其它处已经证明两向量相同，右边整个为零；否则必须保留显示的固定坏处差。特别，选择 c 使原旧坏处的开稳定子不变，并不自动处理
$D_c$ 的新分母素数。

对原完整 theta 映射及同一个 Y-unit Mellin 读者应用 (23)，就是实际投影后的精确式。其 p 处输入由 (21) 完全指定。右边不能在没有实际有限型比较时改称原 $J_{126}$ 的某个标量倍数：它还含固定坏处差和两轴的二次相位。

反过来，对某一新相位作进一步平均，也必须使用它在 (23) 的真实向量上所产生的结果；不能仅因一个原曲线在该处未分歧就把这个差指定为零。

### 8.3 保留原 K/Y 导数的是移动投影

还须区分两种确实不同的操作。记
$A_nf(x)=f(g_nx)$，所以 $\phi_n=A_n\phi_0$，
$\phi_0=B_0\otimes B_0$。在自然极化中
$E_0\phi_0=\phi_0$。因此真实随坐标移动的投影是
$$
\boxed{
E_n^{\rm mov}=A_nE_0A_n^{-1},\qquad
E_n^{\rm mov}\phi_n=\phi_n,\qquad
(E_n^{\rm mov}-E_0)\phi_n=(1-E_0)\phi_n.}
\tag{24}
$$
在标准极化中把所有算子共同共轭以
$\mathcal U_Y\otimes\mathcal U_K$，这些式子仍逐项成立。
这里没有把局部 torus 作用认作物理变量的任意单位倍乘。

原全局有理 theta 协变将“先在原球上作 $E_0$，再改变观察”送到
(24) 的移动投影，而不是送到固定 $E_0$。
前一种操作固定原完整来源，因此也固定它全部正式 Taylor 系数。
特别它固定 R1040(122) 的真实 K 一次条件矩及 R1046 已付的负一读者：
$$
\boxed{
\int_{Y\ {\rm unit}}\frac K Y\,\mathscr P_3\,d\rho
=\frac{10\delta}{7}\Omega I_{D,p}\ne0.}
\tag{25}
$$
所以不能把 (22) 的零输入说成“同一个 (25) 已为零”。
一旦从移动投影改成固定投影，新增的全部费用就是 (24) 的最后一项，再连同 (23) 的固定坏处差返回。其有限字符已经在 (18) 完整列出。

对原角函数，仍准确有
$$
\mathfrak j(t)=\mathfrak j(0)+
t\,d\frac{10\delta}{7}\Omega I_{D,p}+O(t^2),
\qquad t\in p\mathcal O.
$$
本附录不从 $\mathfrak j(0)=0$ 微分出额外零。
它支付的是：固定未分歧平均确实删掉 (22) 的有符号 p 局部分量；
保持实际原角导数的投影却是 (24)，其与固定投影的差不可丢弃。

## 9. 后继可直接消费的有限输入与尚未付清的行

(17)–(21) 是完整有限向量及原极化返回；没有新增数学执行。
(22)–(25) 明确说明实际 Y-unit 读者允许的零，和不得转移的非零一阶读者。

若后继要证明平均确只回原 canonical 行，必须对 (23) 的固定其它有限向量完成实际分解，并把 (21) 通过同一个 division/Miller 图送回原 Amice 测度。若要保留角导数，则必须同时消费 (24) 的真实新字项；仅给平均后的 p-old 行为零不够。

所有这些有限平均的原分母均保留，尤其
$(p-1)p^{n-r-1}$ 随 n 产生的 p 损。本文没有将它们改成此前整 bounded 的 whole carry，也没有声称 (10) 中某一新字的中央值非零。
