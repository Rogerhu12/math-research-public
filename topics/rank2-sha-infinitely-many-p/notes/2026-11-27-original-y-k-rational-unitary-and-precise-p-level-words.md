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


## 10. 一个只有新增五处分母的真实角及其完整 Bell 差

本节延续(23)，不将其中的其它有限输入当作原向量。
直接取
$$
 a=\frac25,\qquad b_n=\frac{\kappa^n}{5},\qquad
 g_n^\epsilon=\frac15
 \begin{pmatrix}2&21\epsilon\kappa^n\\
              -\epsilon\kappa^{-n}&2\end{pmatrix},
 \quad\epsilon\in\{+1,-1\}.
 \tag{26}
$$
其行列式为一，且(4)逐项成立。这也是 Cayley 参数 $c=1/7$；
虽不再是第1节的整数参数，(26)本身已直接证明全部有理等距条件。
新增分母只有5；原框架的2、3、7仍须保留。

### 10.1 原输出坐标的逆 Gram

(19)中的 Hermitian 系数在这里必须按输出的对偶坐标解释。
相对于原 sigma 的共同 Hermitian 类 $\alpha_\sigma=2$，
两条双系数为
$$
 \alpha_Y^{\rm rel}=1/126,\qquad \alpha_K^{\rm rel}=1/6.
$$
若记 $c_\sigma=2x_0^3$，则(19)–(21)准确使用
$c_Y=c_\sigma/126,\ c_K=c_\sigma/6$。
原行 Gram $(126,6)$ 与此逆 Gram 不混同；
$gDg^*=D$ 等价于 $g^*D^{-1}g=D^{-1}$。
因而(19)–(21)不需换公式，但不能把其中未展开的
$\alpha_L$ 误填为126或6。

先在5处取 $\kappa^n\equiv1\bmod25$。
由第二行再代第一行，整个格是
$$
 L_5^\epsilon=
 \{y\in5^{-1}\mathbf Z_5,\quad
       k-\epsilon y/2\in5\mathbf Z_5\}.
 \tag{27}
$$
两个格的自对偶 Haar 体积都是一。
这不是只取单位上的条件。

以 $u=5y,v=5k\bmod25$ 写其有限向量，则
$$
 \phi_5^\epsilon(u,v)={\bf1}_{\,2v=\epsilon u}.
 \tag{28}
$$
两轴的小球基均为 $\mathbf1_{u/5+5\mathbf Z_5}$，
每列范数平方为 $1/5$。所以(28)的25个非零系数均准确为一，
其张量范数平方也是一。

这里相位的符号有实质作用：
$$
 \frac1{126}+\frac{(1/2)^2}{6}=\frac{25}{504}.
$$
故图 $v=u/2$ 在完整模25逆 Gram 配对中是反辛图。
原共同 $\alpha_\sigma=2$ 仍在场。
Y轴改坐标 $u=5y$ 后的 Hermitian 代表是 $2/(126\cdot25)$；
因 $126\equiv1\bmod125$，其完整模25模型恰为
R1047(11)的 $2/25$ 模型。
K轴再改坐标 $w=2v$，其模型是该模型的对偶。
这同时固定原 $\omega$ 作用和 splitting；不是从反演奇偶猜相位。

沿 R1047(10)–(14)，令
$\mathcal T=(\mathcal O_K/25)^1$，生成元
$g_5=-\omega(1+5\delta)$，$\theta_r(g_5)=\zeta_{30}^r$。
保其实际矩阵
$$
 W(a+b\delta)_{uv}
 =\frac15\zeta_{25}^{\,3\{a(u^2+v^2)-2uv\}/b}
 \quad(5\nmid b)
$$
及同一表示对其它群元的定义。
全谱是一个平凡旧字和所有 $5\nmid r$ 的24个单重字。
令 $f_r=\Pi_re_{a_r}$、$n_r=\sum_u f_r(u)^2$，
取 R1047(14) 的同一最小非零列规范。
这些 $f_r$ 是实向量。完整 Bell 分解因此是
$$
 \boxed{
 \phi_5^+-\phi_5^-
 =2\!\!\sum_{\substack{0\le r<30\\r\ {\rm odd},\ 5\nmid r}}
       \frac{f_r(u)f_r(2v)}{n_r}.
 }
 \tag{29}
$$
这十二个标签是
$1,3,7,9,11,13,17,19,21,23,27,29$，
每项都非零；两轴取相反角色。
(29)在任一轴单独反演时为负，而两轴同时反演时为正。
它不是 R1047 的四条 even 型五线。
每条留下的角色在 $1+5\mathcal O_K$ 上均非平凡，
故不能把它们称为 $\mathbf Q$ 上 $j=0$ 椭圆曲线的六次角色。

(27)–(29)的全部标量由原 Haar、原模25 Gauss 核和同一个旧球固定。
没有任选一条平方根，也没有把5处的 wild 字换成 tame 字。

### 10.2 n 的固定有限状态与旧坏处

原 ray 已有 $\kappa\equiv1\bmod25$。
其它坏处不能因(26)的分母只有5就被抹去。
可以不改变原普通素数集合，而只让深度 n 取一个固定子序列。

例如令
$$
 M_{\rm bad}=2^{12}3^8 7^4 5^2,\qquad
 h_{\rm bad}=\#(\mathcal O_K/M_{\rm bad})^\times.
 \tag{30}
$$
取 $h_{\rm bad}\mid n$，则 $\kappa^n\equiv1\bmod M_{\rm bad}$。
这里 $\kappa$ 在这些处是单位，故这一断言只用有限单位群，
不改变原模64的条件。
两个相对矩阵 $g_n^\epsilon(g_0^\epsilon)^{-1}$ 及其反序
在5处整；例如正号支为
$$
 \frac1{25}\begin{pmatrix}
 4+21\kappa^n&42(\kappa^n-1)\\
 2(1-\kappa^{-n})&4+21\kappa^{-n}
 \end{pmatrix}.
$$
在2、3、7处它们与一的差分别含(30)的相应高次幂。
共轭回(1)时逆框架至多损失 $2^1,3^2,7^1$；
换回原标准极化后仍远深于原 Schwartz 的开稳定子。
具体地，原二处支撑在 $\frac14\mathbf Z_2^6$、周期为
$2\mathbf Z_2^6$，原三处为 $(3^{-1}\mathbf Z_3)^6$，
七处为标准球。对标准上剪切、下剪切和对角生成元逐项使用
这些支撑/周期，分别在 $2^5,3^2,7$ 的主同余群已固定原向量；
(30)连同上述框架损失足以覆盖它们。
在二处还保 $\det\equiv1\bmod8$，不遗漏 metaplectic 符号。

所以对这一 n 子序列，(23)中两个其它有限向量分别等于
$n=0$ 的两个实际向量。这没有说两向量彼此相同，
也没有说 $g_0^\epsilon$ 在2、3、7处固定原来源。

## 11. 其它有限费用的完整六 sigma 返回

反变规范须在此锁定。
本文(6)是 $\phi_0(gx)$；用全局有理 Weil 协变移到无限处，
其参数是 $g^{-t}$，不是 g。
因此 $\phi_n^+$ 的固定坏处返回对应下文 $F_-$，
$\phi_n^-$ 对应 $F_+$。

定义完整整行
$$
 U_\epsilon=2Y+21\epsilon K,\qquad
 V_\epsilon=-\epsilon Y+2K.
 \tag{31}
$$
例如
$$
\begin{aligned}
 U_+&=(-7,\,8+23\omega,\,-15-23\omega,\,27\delta,\,4\delta,\,4\delta),\\
 V_+&=(-9,\,-4+\omega,\,-5-\omega,\,-\delta,\,-2\delta,\,-2\delta).
\end{aligned}
$$
直接 Gram 为 $(3150,150)$，二行正交，且与 H/J/A/N 全正交。
两行模二各有四个非零系数，所以两完整半特征都是 standard even。

使用原同一个 sigma、原 $b=17$、原周期、原 $-1/84$，置
$$
 \mathcal G_\epsilon(z,w,\mathbf t)
 =-\frac1{84}\prod_{j=1}^6
 \sigma\left(
 U_{\epsilon,j}z+V_{\epsilon,j}w+
 H_jt_H+J_jt_J+A_jt_A+N_jt_N\right),
 \tag{32}
$$
$$
 \mathcal F_\epsilon(z,w,\mathbf t)
 =\mathcal G_\epsilon(z/5,w/5,\mathbf t),\qquad
 F_\epsilon(z)=\mathcal F_\epsilon(z,0,\mathbf0).
 \tag{33}
$$
(32)是两份实际固定来源，不是一个仅给维数的模型。
它包含旧2、3、7处和新增5处的全部相位。
(29)是它们在5处的有符号 Bell 差；
其它旧有限向量是原(32)本身的向量，未被替成球。

全局有理 lift 的乘积相位为一，且(26)的行列式为一；
无限 Gaussian 的二次型由(4)严格保持。
故原 theta 协变给出的正是(32)–(33)，没有未定非零标量。
也可在原六 sigma 的第一非零 Taylor 项逐项核定：
其系数是 $-\prod_j U_{\epsilon,j}/(84\cdot5^6)$，
与同一反变有理替换完全相同。
只读这个首项不是用来识别一个未付的 Hecke 线，而是核定
已经给出整个乘积的绝对规范。

原 ray 的
$\kappa\equiv3\bmod4$、$\kappa\equiv1\bmod9\cdot25\cdot7$
分别给两度的完整中心
$3151\bmod6300$、$151\bmod300$。
其非零绝对锚是
$$
 \Theta(15\gamma_7z),\qquad\Theta(5\delta z).
 \tag{34}
$$
原 $\Theta$ whole core 是 $\beta=-\lambda=\bar\pi_0^{-1}$；
prime-to-p CM pull 与全深限制严格交换。
因此(32)沿 U、V 两轴的整个核都是 $\beta$，
保其余四输出，不先取一个边际。
除以5只是 p 单位坐标变换，故(33)也有同一两个 whole 核。

## 12. 自然球经原 division/Miller 图的全部正负深度

以下锁定(21)到物理读者所缺的具体图。
固定(32)或(33)的其它有限输入；在当前好 split p，
将某轴的原自然球 $B_0$ 改为 $B_r$，再用(19)回标准极化。
记所得完整 theta/测度来源为 $\mathcal B_r$。
这个记号不把自然球先定义成物理深限制。

当 $r\ge0$，
$$
 B_r(x)=B_0(x)\frac1{p^r}
       \sum_{a\bmod p^r}\psi_p(ax/p^r).
 \tag{35}
$$
这条直线可以在(19)中直接核定，不能只命名为“对偶”。
写 $M_sf(y)=\psi_p(sy)f(y)$、$X_tf(y)=f(y+t)$，
并在本轴令 $c=c_L$。完成平方及换元逐项给
$$
 \begin{aligned}
 \mathcal U M_s\mathcal U^{-1}F(x)
 &=\psi_p(-sx-s^2/(2c))F(x+s/c),\\
 \mathcal U X_t\mathcal U^{-1}F(x)
 &=\psi_p(-ctx/2+ct^2/8)F(x-t/2).
 \end{aligned}
 \tag{35a}
$$
按 $T_{h,k}F(x)=\psi_p(k(x+h/2))F(x+h)$，
两条完整 Weyl 直线分别为
$(h,k)=(s/c,-s)$ 和 $(-t/2,-ct/2)$。
自然 dilation $f(y)\mapsto f(\kappa y)$ 的共轭
在调制线上给 $\kappa$，在位置线上给 $\kappa^{-1}$。
与 R300(16)的真实 CM 交织相对照，第一条正是原正式
$E[\pi_0^r]$ connected 线，第二条是 étale
$E[\bar\pi_0^r]$ 线。特别负线绝不是无相位的位置平移。
这锁定原 theta 的对偶 connected 直线及其全部 Weyl lift。
逆 Gram 及 theta degree 只在 a 上给单位换元；
$p\nmid3150\cdot150$，所以没有删支。
此处使用原正式同构送入的 connected 核，不能将未规范的
Schrödinger 位置平移与调制互换。
原相位和刚性化由 R300(8)–(12) 的 division 函数图逐支给出；
在同一 Amice 坐标中(35)正是
$$
 \frac1{p^r}\sum_{\zeta^{p^r}=1}
 \mathcal A\bigl(\zeta(1+T)-1\bigr).
 \tag{36}
$$
根单位的正式对数不被逐项代成零。
因此正 r 的整个返回是物理深限制。
再用(34)的 whole 核，得到
$$
 \boxed{\nu_{\mathcal B_r}=\beta^r[\kappa^r]_*\nu_{\mathcal B_0}
       \quad(r\ge0).}
 \tag{37}
$$

负深度必须另付 Haar 费用。
自然位置的完整平移平均给 $p^{-r}B_{-r}$，$r\ge0$；
原对偶图是 $E[\bar\pi_0^r]$ 的 étale 全迹。
共轭的同一个 whole 锚给其准确系数
$$
 \pi_0^{-r}=\beta^{-r}p^{-r}.
$$
乘回自然球前的 $p^r$ 后，才得到
$$
 \boxed{\nu_{\mathcal B_{-r}}
       =\beta^{-r}[\kappa^{-r}]_*\nu_{\mathcal B_0}
       \quad(r\ge0).}
 \tag{38}
$$
(38)的测度支撑在 $p^{-r}\mathbf Z_p$，
不被称为 $\mathbf Z_p$ 上的整测度。
(35)–(38)同时保 connected/étale 两个完整纤维、
原 $1/p^r$、CM 尺度和 division/Miller 因子。
这正是不能仅从 Yang Corollary2.10 的局部特征略过的步骤。
自然/标准间所有二次相位仍是(19)–(21)。

两个正交轴的图严格交换，故对整数 r,s 的联合返回为
$\beta^{r+s}[\operatorname{diag}(\kappa^r,\kappa^s)]_*\nu$，
保 H/J/A/N 全部坐标。
正负支撑及其扩域分别如(37)–(38)所示。

## 13. 原 Y-unit 的完整返回：两项 K 缩放差

记 $\mu_\epsilon$ 为(33)的完整六输出测度；
$\mu_\epsilon^\times$ 仅在其第一个真实物理坐标 Y 取单位。
这里 Y 是已经在反变图中明确锁定的输出坐标，
不是将原六输入之一更名为 Y。

令
$$
 D_{K,t}=\operatorname{diag}(1,t,1,1,1,1),\qquad
 d_n=(p-1)p^{n-1}.
$$
将(17)经(35)–(38)整式返回。
$r\ge1$ 的 Y 环带和第一项 $B_n\otimes B_0$ 在 Y-unit 上全零；
$r=0$ 的 $B_0-B_1$ 准确成为同一个 $\mu_\epsilon^\times$。
K 的两个负深度球不能丢弃。故对(30)的 n 子序列，
$$
 \boxed{
 \nu_{E_0\Phi_n^\epsilon}\big|_{Y\ {\rm unit}}
 =\frac{\beta^{-n}}{d_n}
   \left\{(D_{K,\kappa^{-n}})_*
             -\beta(D_{K,\kappa^{1-n}})_*\right\}
             \mu_{-\epsilon}^{\times}.
 }
 \tag{39}
$$
这是真测度身份，先作用于完整六输出，不是只比某个首矩。
原 H/J/N 投影可在两边共同施加，因为所有显示操作都固定这些轴。
任意仍读 K 的 mixed cut 必须保持(39)的两个实际转置。

只在忘掉 K 后，(39)才简化为
$$
 \boxed{
 (\operatorname{pr}_{Y,H,J,A,N})_*
   \nu_{E_0\Phi_n^\epsilon}\big|_{Y\ {\rm unit}}
 =c_n(\operatorname{pr}_{Y,H,J,A,N})_*\mu_{-\epsilon}^{\times},
 \qquad
 c_n=\frac{(1-\beta)\beta^{-n}}{(p-1)p^{n-1}}.
 }
 \tag{40}
$$
例如同一个原单位 Mellin 给
$$
 J_{E_0\Phi_n^+}(v)-J_{E_0\Phi_n^-}(v)
 =c_n\{J_{F_-}(v)-J_{F_+}(v)\}.
 \tag{41}
$$
所以(23)的固定坏处差已返回到(32)两个完整固定六 sigma，
不再留下自由的未指定局部向量。
$n$ 的全部分母和尺度显示在(39)–(41)中。
特别这里仍有 $p^{1-n}$，不能将它说成原整 carry。

两个 $F_\epsilon$ 的全质量为零；
由其 whole core，单位质量也为零。
若使用不除5的第一来源 $\mathcal G_\epsilon(z,0,\mathbf0)$，
其 Mellin 差只多 $\langle1/5\rangle^{dv}$；
中央首导数因质量为零而不另付 $\log5$。
这个规范只消一项已明确的质量费用，不将任何新来源赋中央零。

还可直接读真实 K/Y，而非猜它被平均杀去：
$$
 \boxed{
 \int_{Y\ {\rm unit}}\frac KY\,d\nu_{E_0\Phi_n^\epsilon}
 =\frac{\beta^{-n}\kappa^{-n}(1-\beta\kappa)}{d_n}
       \int_{Y\ {\rm unit}}\frac KY\,d\mu_{-\epsilon}.
 }
 \tag{42}
$$
右边是两个固定新来源自己的完整读数，不是原(25)。
原(25)仍属于移动投影(24)。
(39)同时说明：含 K 的原 carry/cut 不可只用(40)的标量。
因此本节没有把原 $j_Y(0)=0$ 微分成一个新零，也没有把
(29)的十二个 wild 字或(32)的新六 sigma 当作已知 rank-two
canonical 族。下一步可直接对这两个已完整返回的固定输入及
(39)的两项 mixed 测试作比较；无须再次重建 p 局部球/环带。


## 14. 原完整 5-old 迹的负号支：保 K/A 的准确反演

本节只使用原固定角(26)及原有限来源，未执行新数学程序。
5-old 指五处两个轴各自的旧球投影；它不是 p 处的
$E_0$，也不是把整个新来源赋成一个旧 canonical 行。
以下在完整 H/J/N 投影后保留 K 与 A 的全部类型。

### 14.1 固定半特征和真正的 625 项投影

写 $D=\operatorname{diag}(126,6)$，并令
$$
 Q_\epsilon=
 \begin{pmatrix}2&21\epsilon\\-\epsilon&2\end{pmatrix},
 \qquad Q_\epsilon DQ_\epsilon^{\,t}=25D,\qquad \det Q_\epsilon=25.
 \tag{43}
$$
R1040(84)–(85) 的整个来源为
$$
 \mathscr P_3\mathcal B
 =B_3(h)\Theta(j)\Theta_{14}(n)\mathcal C(z,k,a),
 \qquad
 \mathscr P_3=\Pi_{H,0}\Pi_{J,0}\Pi_{N,0}.
$$
原 $(Y,K)$ 两度均为 even，故其标准半特征为平凡：
在共同实周期归一及同一 Gaussian gauge 中可用完整基
$$
 \vartheta_{\mathbf c,D}(\mathbf z)
 =\sum_{\mathbf m\in\mathbf c+D\mathbf Z^2}
   \exp\!\left(\pi i\tau\,\mathbf m^tD^{-1}\mathbf m
                    +2\pi i\,\mathbf m^t\mathbf z\right),
 \quad
 \mathbf c\in\mathbf Z/126\times\mathbf Z/6 .
 \tag{44}
$$
其中 $\tau=(1-\omega)^{-1}$ 是同一个原周期比；改变到原 sigma
frame 只乘各轴共同的二次 Gaussian。
(43) 保持该二次型，因此此变框架不会添一个角依赖的指数或 phase。
A 的 odd degree9 半特征完全未动。

先在 degree $(3150,150)=25D$ 上形成
$\mathcal C(Q_\epsilon^t\mathbf z,a)$。
在两个轴的全部 $E[5]$ 上，使用原 Weyl lift 定义
$$
 \mathcal E_5F
 =\frac1{5^4}\sum_{u,v\in E[5]}
       \mathsf T_{3150,u}\mathsf T_{150,v}F .
 \tag{45}
$$
因为各度除以25后仍为 even，这个群的完整中心及整数周期
在(45)中平凡；其像准确是 $[5]^*H^0(\mathcal L_D)$。
定义唯一的旧返回 $\mathcal O_\epsilon$ 为
$$
 [5]^*(\mathcal O_\epsilon f)
       =\mathcal E_5\{f(Q_\epsilon^t\mathbf z)\}.
 \tag{46}
$$
这就是对(33)的五处旧球投影并返回原参数，不是另选一个同维模型。

### 14.2 25 列与 5 个交点锁定绝对系数

由(43)，$Q_\epsilon^tD^{-1}Q_\epsilon=25D^{-1}$。
所以 $f=\vartheta_{\mathbf c,D}$ 的拉回在
degree $25D$ 的完整 theta 基中恰为25个不同列之和，每列系数一。
另一方面
$[5]^*\vartheta_{\mathbf b,D}$ 也是25列之和，索引为
$$
 5\mathbf b+5D\mathbf t\pmod{25D},\qquad
 \mathbf t\in(\mathbf Z/5)^2 .
$$
第一组与后一组相交，必须
$\mathbf b\equiv Q_\epsilon\mathbf c/5\pmod D$；
除以5在两个原有限群中均唯一合法。
对这个唯一 $\mathbf b$，条件
$Q_\epsilon\mathbf m\in5\mathbf Z^2$ 在模5只有一个独立条件：
$Q_\epsilon\bmod5$ 秩一。因此两组恰交5列。

同一级的(44)各列正交且范数相同。
故正交投影的系数是 $5/25=1/5$，不是由非零平方值猜一个标量：
$$
 \boxed{\quad
 \mathcal O_\epsilon\vartheta_{\mathbf c,D}
   =\frac15\vartheta_{P_\epsilon\mathbf c,D},
 \qquad
 P_\epsilon\mathbf c=Q_\epsilon\mathbf c/5\pmod D .
 \quad}
 \tag{47}
$$
(45)的 $5^{-4}$、625个完整纤维及(47)的 $1/5$ 全部保留。
相交列中的系数均是一，故(47)也锁定绝对号。
这与(28)中两个归一旧球对 Bell 图的内积 $1/5$ 一致，
但本证明还支付了无限 theta 及其原 half-characteristic。

### 14.3 原三处 gluing 与二、七处符号

以下不用预先施加 $\Pi_{Y,0}$ 或 $\Pi_{K,0}$。

首先直接由原行，
$$
 \frac{Y+K}{\delta}
     =2(-\delta,-\omega,-\omega^2,2,1,1),\qquad
 N((Y+K)/\delta)=44.
$$
quotient 的 norm 偶，原六 sigma 准周期和 Weyl 指数因而准确给
$$
 \mathsf T_{Y,u}\mathsf T_{K,u}\mathcal C=\mathcal C
       \qquad(u\in\ker\delta).
 \tag{48}
$$
在原 $\Lambda=\mathbf Z+\tau\mathbf Z$ 中，
$\delta/3=2\tau-1$，可取真实实方向 $u=1/3$。
标准 even gauge 下该 Weyl 算子就是(44)的实平移，
所以若 $u_9,v_3$ 是 Y/K 的三处索引，(48)准确限制
$$
 v_3\equiv-u_9\pmod3 .
 \tag{49}
$$
这里不是把两个已经主型化的三处向量相乘；
K 的所有实际类型仍在(49)中。

二处使用 R1040(114) 之前的整个来源关系。
原 $Y-K\in2\mathcal O_K^6$、quotient norm33 odd，
故对全部三个非零 $t\in E[2]$，
$$
 \mathsf T_{Y,t}\mathsf T_{K,t}\mathcal C=-\mathcal C .
 \tag{50}
$$
在(44)的完整 CRT 基，实半周期是两侧同一个
$\operatorname{diag}(1,-1)$，虚半周期是两侧同一个交换矩阵；
$126/2=63$ 和 $6/2=3$ 都是 odd，第三个 Weyl 相位也一致。
因此(50)的整个二处共同空间准确是
$$
 e_0\otimes e_1-e_1\otimes e_0 .
 \tag{51}
$$
特别交换两侧的绝对号是 $-1$。这不由抽象 dyadic 号推断，
而是由三个真实平移及其相位锁定。

七处必须先用原投影前的 Bell 配对，再收缩 N。
R1040(112)–(113)已经付
$Y+4N\in\gamma_7\mathcal O_K^6$、
$Y+3N\in\bar\gamma_7\mathcal O_K^6$，
以及两个 quotient 的 even 半特征。
$\Theta_{14}$ 的七处向量收缩这个完整配对线后，
无论 K/A 采用哪个类型，Y 的七处都为同一个
R1038(44) 的实偶向量 $f_7$。故索引 $a_7\mapsto-a_7$ 对此向量
准确为 $+1$。
这里仍没有把单个 N 平移穿过 $\Pi_{N,0}$。
原 Weil $W_7(-1)$ 本身是负反射，有限特征
$\tau_7(-1)=-1$；二者合起来正说明实际向量的索引反射为正，
不遗漏该七处负号。

### 14.4 负号支是整个 K 反演

把 $P_-$ 在完整 CRT 索引中写开：
$$
 \begin{array}{c|c}
 2 & (u_2,v_2)\longmapsto(v_2,u_2)\\
 3 & (u_9,v_3)\longmapsto(4u_9+3v_3,\ v_3-u_9)\\
 7 & a_7\longmapsto-a_7 .
 \end{array}
 \tag{52}
$$
所有除以5都使用(47)的同一个有限群逆元。
在(49)上，第二行准确是
$(u_9,v_3)\mapsto(u_9,-v_3)$。
二处交换由(51)给 $-1$，七处由前段给 $+1$。
而 K 的整个反演在其二处索引上为恒等、在三处索引上正是
$v_3\mapsto-v_3$。于是(47)逐列给完整函数身份
$$
 \boxed{\quad
 \mathcal O_-\mathcal C(z,k,a)
       =-\frac15\,\mathcal C(z,-k,a).
 \quad}
 \tag{53}
$$
(53)保整个 A 变量，以及 K 的全部 principal 和非 principal
类型；没有在混合 $Y/K$ 前先删除 type1 的 $U_K$ 等来源。

把 H/J/N 的三个已付整因子放回，等价地
$$
 \boxed{\quad
 \mathcal E^{\rm old}_5
       \mathscr P_3\mu_-
     =-\frac15(R_K)_*\mathscr P_3((Y,K,H,J,A,N)_*\rho),
 \qquad R_K(Y,K,H,J,A,N)=(Y,-K,H,J,A,N).
 \quad}
 \tag{54}
$$
左边 $\mu_-$ 沿(33)的同一 $1/5$ 参数和原反变规范；
$\mathcal E^{\rm old}_5$ 精确指(45)–(46)。
这是两个整来源的完整测度身份，故对所有连续 mixed 测试都成立，
但测试中的 K 必须真的反演。

只在最后忘掉 K/A 等伴随后，R1040(4)与(54)给
$$
 \boxed{\quad
 (\operatorname{pr}_Y)_*\mathcal E^{\rm old}_5
           \mathscr P_3\mu_-
       =-\frac{39\delta}{5}\,\nu_{\Phi_{126,17}} .
 \quad}
 \tag{55}
$$
因此该支的系数和非零性都已经付清。
这不是由新 $F_-$ 的质量零反推它只能有旧 rank-two 分量。

### 14.5 同一个 Y-unit 读者及已付点对数

五处投影与 p 处的完整 $E_0$ 平均交换。
保(26)、(30)的 n 子序列及原反变号：
$\Phi_n^+$ 对应 $\mu_-$。
令 $\nu=\mathscr P_3((Y,K,H,J,A,N)_*\rho)$，并在其原 Y 轴取单位。
将(54)代入原(39)，严格得到
$$
 \boxed{
 \mathcal E^{\rm old}_5
    \nu_{E_0\Phi_n^+}\big|_{Y\ {\rm unit}}
 =-\frac{\beta^{-n}}{5d_n}
    \{(D_{K,-\kappa^{-n}})_*
       -\beta(D_{K,-\kappa^{1-n}})_*\}\nu^\times .
 }
 \tag{56}
$$
两次 K 缩放、反演、全部 p 分母和 H/J/N/A 测试均在式中。
忘 K 后才是
$$
 J_{\mathcal E^{\rm old}_5 E_0\Phi_n^+}(v)
       =-\frac{39\delta}{5}c_n J_{126,17}(v).
 \tag{57}
$$
在原 E3969 的坏中央条件下，(57)的首导数确为零。

另一方面，同一个完整测度身份给实际 K/Y
$$
 \boxed{
 \begin{aligned}
 \int_{Y\ {\rm unit}}\frac K Y\,
       d\nu_{\mathcal E^{\rm old}_5 E_0\Phi_n^+}
 &=\frac{\beta^{-n}\kappa^{-n}(1-\beta\kappa)}
          {5d_n}\,
       \frac{10\delta}{7}\Omega I_{D,p}\\
 &\ne0 .
 \end{aligned}}
 \tag{58}
$$
最后的非零是 R1046 已付的 E21609 同一个 Rubin 点对数；
$1-\beta\kappa\equiv1\bmod p$。
(58)并不与(57)冲突：二者测试函数不同。
它支付了新投影实际保留下来的非零点载体，不从
$j_Y(0)=0$ 微分出额外零，也不把 K-dependent cut 换成(57)。

### 14.6 原全和仍需保留的两个补项

对每个实际来源，准确分解始终为
$$
 \nu_{\Phi_n^+}
 =\nu_{\mathcal E^{\rm old}_5 E_0\Phi_n^+}
  +\nu_{(1-\mathcal E^{\rm old}_5)E_0\Phi_n^+}
  +\nu_{(1-E_0)\Phi_n^+}.
 \tag{59}
$$
对同一个 Y-unit 或其它完整 mixed 测试逐项使用(59)才合法。
五处单支 new 部分包含24个 wild 配对字；
只有在其它有限向量相同时，其局部有符号差才缩为(29)的十二个
odd 配对字。原两支的2、3、7向量未被证明相同，
所以不能用局部奇偶直接删掉(59)第二项。
这些字也不是 R1047 的四个 even type5 点载体；
其全部联合 Hermite 权和全坏处仍须返回。

第三项的 p 字是(18)中的 Y/K 相反字符。
原 $E^6$ 的对角 p 惯性会同时作用于两轴，两个字符可能相消；
所以不能仅因 R1046 的原点域在 p 未分歧，就通过惯性把它删掉。
(53)–(58)新增的是已完整支付的旧投影及真实读者，
尚未把(59)的两个补项变成已知中央零。


## 15. 正号支的完整 G 系数、四次有理迹及两个原补项

本节接(53)，计算另一支最后的真实 Y 边际。
仍先保完整 Y/K 旧投影，再取 K 质量；新来源的原质量零
不能用于删掉其旧投影。

### 15.1 原 K 的两个不同 δ 返回

原 $Y-H\in\delta\mathcal O_K^6$，quotient norm43 odd。
与 R1040(49)、(54) 的原 H 偶线相结合，
Y 的完整 $\delta$-old 投影为零。
在(43)–(47)的旧返回中，新 Y 的 $\ker\delta$ 平移回原
$(u,0)$，所以两个分支的 Y 都仍然 $\delta$-new。

新 K 的同一个平移则回到
$$
 Q_\epsilon^t(0,u/5)=( -\epsilon u/5,\,2u/5)
          \equiv(\epsilon u,u)\pmod{\Lambda^2}.
 \tag{60}
$$
这些平行整数周期的原 even Weyl 相位为一。
由(48)，正号支的 K 因而是整个 $\delta$-old；
负号支的 K 是 $\delta$-new。此区分发生在所有 K 类型都保留时。

正号支的 K 空间准确为
$$
 [\delta]^*\mathcal S_2
 =\langle\Theta(\delta k),\sigma(\delta k)^2\rangle,\qquad
 \Theta(\delta k)=\sigma(k)^6(X(k)+4b).
 \tag{61}
$$
整个空间在 $k\mapsto-k$ 下均为偶。
其 principal 质量一线为第一项；
先在 $b=1$ 的原二挠规范中用加法式
$$
 \mathsf T_e^6\{\sigma^6(X+4)\}
  =\sigma^6(X+4-6ex^2)/\sqrt3,\qquad e^3=-1.
$$
三项和为 $+\sqrt3\,\sigma^6(X+4)$；再按本篇同一 CM
homothety 把 sigma、二挠 lift 和 period 一起运到 $b=17$，
这个本征号仍是 $+\sqrt3$。
(50)于是迫最后 Y 主型的 dyadic 号为 $-\sqrt3$。
七处仍为(52)的实偶 $f_7$。三处还须保原完整向量，
不能只以 $\delta$-new 命名：正号置换为
$(u,v)\mapsto(4u+6v,u+v)$，在 $v\equiv-u\pmod3$ 上
准确是 $(7u,0)$。
若按 R1038 的三个偶代表 $(1,2,4)$ 写
$f_\Phi=(A,B,C)$，其返回为 $(C,A,B)$；
直接代原 $\zeta_9$ 坐标，得到这个非零向量与
$$
 f_G=(3+\delta(\zeta^4-\zeta^5),\
          -\delta(\zeta^2-\zeta^7),\
           \delta(\zeta^4-\zeta^5))
$$
成比例。故真正固定的是原 $\omega^2M$ 的一维线；
该比例不另猜，由下文全质量确定。
R1040 §§14.2–14.4 的全有限唯一性因此给
$$
 (\operatorname{pr}_Y)_*\mathcal E^{\rm old}_5\mathscr P_3\mu_+
           =c_+(b)\,\nu_{G_{126,b}} .
 \tag{62}
$$
这里 $G_{126,b}(0)=-\delta/28$，是原 E15876 质量一线
的这个已固定倍数；没有凭两三个好位本征值命名。
系数尚由下文的实际完整迹决定。

### 15.2 625 个纤维准确降为 25 个原 Weyl 值

在(45)的正号支取
$$
 w=2u-v,\qquad
 Q_+^t(u,v)=(w,25u-2w).
$$
每个 $w\in E[5]$ 有25个原 $(u,v)$。
与 $(w,-2w)$ 相比，第二分量只多原周期 $25u\in5\Lambda$。
其完整 Weyl 相位为
$\exp(\pm\pi i\,300E(u,w))=1$，
因为 $E(u,w)\in25^{-1}\mathbf Z$。
因此对总质量，原625项不是丢掉24个分支，而是逐纤维相等：
$$
 m_0(\mathcal O_+\mathcal C)
 =\frac1{25}\sum_{w\in E[5]}
    \{\mathsf T_{150,w}\,\mathcal C(z,-2z,0)\}(0).
 \tag{63}
$$
H/J/N 投影在其原点不改质量，所以(63)仍是原六 sigma 的值。

原行的完整因子是
$$
 \frac{Y-2K}{\delta}
 =(-3\delta,-2-3\omega,-1-3\omega,1,2,2),
 \qquad N((Y-2K)/\delta)=50.
$$
用 $2+3\omega=-\omega^2\gamma_7$、
$1+3\omega=\omega\bar\gamma_7$，两个 norm7 因子的单位与三个
负号的总乘积准确为正。令
$$
 \begin{aligned}
 Q_2(X)&=7X^2-4bX+16b^2,\\
 P_3(X)&=X^3-96bX^2+48b^2X+64b^3,\\
 h_{50}(z)&=\sigma(z)^{50}x(z)
              (X+b)(X+4b)Q_2(X)P_3(X).
 \end{aligned}
$$
原 division 恒等式
$$
 \sigma(\gamma_7z)\sigma(\bar\gamma_7z)=\sigma^{14}Q_2,\quad
 \sigma(3\delta z)=3\delta x(X+4b)P_3\,\sigma^{27},\quad
 \sigma(2z)^2=4(X+b)\sigma^8
$$
遂逐项给
$$
 \boxed{\mathcal C(z,-2z,0)=-\frac{\delta}{7}\,h_{50}(\delta z).}
 \tag{64}
$$
原 $-1/84$ 已在(64)中使用，不能再乘或再除一次。
$[\delta]^*$ 与完整五迹交织；$\delta$ 在 $E[5]$ 上为置换，
且原 Gaussian/Weyl 指数被其 norm3 精确保持。

### 15.3 同一个 Theta lift 把迹化为四次有理数

写原五分多项式
$$
 q_b(X)=5X^4+380bX^3-240b^2X^2-1600b^3X-256b^4.
 \tag{65}
$$
它来自 $\psi_5=\psi_4\psi_2^3-\psi_3^3$，不是拟合的系数。
对非零 $T\in E[5]$，原 $[5]^*\Theta$ 的 Weyl 值为1，故
$$
 \{\mathsf T_{50,T}h_{50}\}(0)
 =\frac{x(T)(X(T)+b)(X(T)+4b)Q_2(X(T))P_3(X(T))}
        {\phi_5(T)} .
$$
这里 $\Theta(5z)=\sigma^{50}\phi_5$；
$\phi_5$ 是原乘五 x-map 的分子。
在 T 的同一个参数中 $x(5(T+z))=(25z^2)^{-1}+O(z^4)$，
所以完整 pole 比较准确给
$$
 \phi_5(T)=\frac{(D\psi_5(T))^2}{25},\qquad
 D\psi_5=6x^2y\,q_b'(X).
 \tag{66}
$$
$T=O$ 的 $h_{50}$ 值为零。
其余24点分成四个各6点的原 $\mu_6$ 轨道。
(66)使每轨道的六项完全相同，并消掉显示的 $X+b$。
因此(63)–(64)准确成为
$$
 \boxed{
 m_0(\mathcal O_+\mathcal C)
 =-\frac{\delta}{42}\,T_b,\quad
 T_b=\operatorname{Tr}_{\mathbf Q[X]/(q_b)}
 \frac{(X+4b)Q_2(X)P_3(X)}{Xq_b'(X)^2}.}
 \tag{67}
$$
$x,y$、全部24个点、原 $25^{-1}$ 和 $-1/84$ 的费用
现在都已进入这个固定四次迹。
$X=bZ$ 直接给 $T_b=b^{-1}T_1$。

以下八个整数系数的恒等式是完整纸面证书。
令 $q=q_1$、
$f=(X+4)(7X^2-4X+16)(X^3-96X^2+48X+64)$，则
$$
 \begin{aligned}
 60f={}&Xq'\,(832-96X-204X^2-5X^3)\\
       &+q\,(-960+80X+520X^2+20X^3).
 \end{aligned}
 \tag{68}
$$
逐次相乘即可核(68)全部系数。
非零五挠在特征零为 étale，四个 $\mu_6$ 轨道的 X 值不同，
故 $q$ 无重根；又 $q(0)=-256\ne0$，
所以 $Xq'$ 在完整四次代数中可逆。
Lagrange 留数公式
$\sum_{q(r)=0}g(r)/q'(r)=\frac15[X^3]g$
给
$$
 \boxed{T_1=-\frac1{60},\qquad
        T_b=-\frac1{60b},\qquad
        m_0(\mathcal O_+\mathcal C)=\frac{\delta}{2520b}.}
 \tag{69}
$$
所以(62)的系数和非零性现在完全确定：
$$
 \boxed{c_+(b)=-\frac1{90b}.}
 \tag{70}
$$
本篇实际 $b=17$，故 $c_+=-1/1530$、
$m_0/\delta=1/42840$。
不需要新 degree3150 谱，也没有假设一个数值近零测试。

### 15.4 唯一公开四次回执与执行范围

本次只执行原(65)–(68)的有理四次代数，
保完整 Bezout 回乘、四乘四乘法矩阵的 trace、Lagrange 公式，
以及 b=1、17 的齐次返回；没有重跑756列或旧任何谱。

实际来源提交为
4e827843，run 46036879390、job 140634410835。
脚本
$\texttt{scripts/check-original-positive-five-old-quartic-trace.py}$
SHA256 为
0a315b319001a1f0b5ff3dfcedbd0e619059bd494529f8478312caafd3f82f75。
完整 stdout 1176B、SHA256
63ded7037646bb2ffd8e40c3ea5845159f61c85e8b36ac8b97b28bb1f8eaeea0；
完整 job log 9336B、SHA256
5ad23ec4bbeb38f5527b1c24c4059eba597633032fc00f46cae1a4d9da0b98a1。
回执返回的 $T_1,T_{17},m_0/\delta,c_+$ 全与(69)–(70)一致。
本节数学结论同时由(68)的完整手证支付。

### 15.5 原同一 Y-unit 的质量、中央和 K/Y

合并原反变号、(40)、(55)、(70)，得到
$$
 \boxed{
 \begin{aligned}
 J_{\mathcal E^{\rm old}_5E_0\Phi_n^+}(v)
       &=-\frac{39\delta}{5}c_nJ_{126,17}(v),\\
 J_{\mathcal E^{\rm old}_5E_0\Phi_n^-}(v)
       &=-\frac{c_n}{90b}J_G(v).
 \end{aligned}}
 \tag{71}
$$
同一个原单位 cut、所有 ordinary Euler 和 n 的 p 分母均保留。
在 E3969 坏中央时，第一行首导数为零，第二行是
$-c_nj_G/(90b)$；本篇没有把 $j_G$ 赋零。

(61)还付一个全源结论：正号固定来源的旧部分在 K 为偶。
因此对于任意保其余输出的实际 Y-unit 测试，
$$
 \boxed{
 \int_{Y\ {\rm unit}}\frac K Y\,
          d\nu_{\mathcal E^{\rm old}_5E_0\Phi_n^-}=0 .}
 \tag{72}
$$
这与(58)的另一支真正不同。
(72)由整个 K 偶性得出，没有使用某条 canonical 坏假设。

原 $J_G(0)=-\delta(1+\lambda)/28$ 为单位。
所以两支旧项之差的实际质量是
$$
 m_\times\!\left(
   \mathcal E^{\rm old}_5E_0(\Phi_n^+-\Phi_n^-)\right)
       =\frac{c_n}{90b}J_G(0)\ne0 .
 \tag{73}
$$
另一方面，原小角的 Y-unit 域仍是同一个原 Y-unit 域，
两条完整有理角的单位质量均为零。
因此同(59)的全部新项必须准确补偿(73)：
$$
 \boxed{
 \begin{aligned}
 m_\times\!\left(
 (1-\mathcal E^{\rm old}_5)E_0(\Phi_n^+-\Phi_n^-)
 +(1-E_0)(\Phi_n^+-\Phi_n^-)\right)
       =-\frac{c_n}{90b}J_G(0).
 \end{aligned}}
 \tag{74}
$$
(74)证明这两个实际补项的全和不可删，也不能因 n 深便赋更深误差。
它不指定二者分别的值。
中央和 K/Y 仍须在同一全和上使用(59)，不能从(71)的旧零
跳过这两个已经具有非零质量的补项。



## 16. 完整球面 Hecke 的两个实际读者及整边际零的有限字

本节继续使用同一原六 sigma、同一普通射线、
$\beta=-\lambda=\bar\pi_0^{-1}$、$\kappa=p\beta^2$，并取 $p>1296$。
记
$$
\nu=\mathscr P_3((Y,K,H,J,A,N)_*\rho),\qquad
\nu^\times=\nu|_{Y\in\mathbf Z_p^\times},\qquad
\mathcal L(\nu)=\int_{Y\in\mathbf Z_p^\times}\frac KY\,d\nu .
\tag{75}
$$
所有 H/J/N 投影和其余 A 输出均保留。
本节不重做 S3150 的450维谱或有限点投影。
新增的是同一原好处球上整个球面双陪集的完整返回，
及一个真正的有限算子，明确区分原中央边际与其非零角读者。

### 16.1 同一个原好处球的完整格计数

在本篇§2的 split unitary Schrödinger 模型，原自然 Y/K 向量为
$\phi_0=B_0\otimes B_0$。
令 $\mathcal K=\operatorname{SL}_2(\mathbf Z_p)$，
$a=\operatorname{diag}(\kappa,\kappa^{-1})$，
并令 $\mathcal H_p$ 是
$\mathcal K a\mathcal K/\mathcal K$
所有右陪集作用的**未平均和**。
其它地点的原有限向量、无限 Gaussian 和另四个输出不改。
determinant 为一，所以按§2的已固定 splitting，
每项是实际变量变换，没有另一个绝对值或根单位系数。
使用正变或反变约定只置换下述全部格。

由于 $\kappa/p$ 是单位，$\mathcal K a\mathcal K$ 与
$\mathcal K\operatorname{diag}(p,p^{-1})\mathcal K$ 相同。
其格是满足
$$
 p\mathbf Z_p^2\subset L\subset p^{-1}\mathbf Z_p^2,\qquad
 L/p\mathbf Z_p^2\simeq\mathbf Z/p^2\mathbf Z
\tag{76}
$$
的全部 covolume 一格。
乘 p 后，(76)对应
$(\mathbf Z/p^2\mathbf Z)^2$ 的全部自由秩一直属项。
其数为
$(p^4-p^2)/(p^2-p)=p(p+1)$。

对 $x\in\mathbf Q_p^2$ 令
$v(x)=\min(v_p(x_1),v_p(x_2))$。
若 $v(x)\ge1$，全部 $p(p+1)$ 个格都含 x；
若 $v(x)=0$，$px\bmod p^2$ 是非零 p-挠向量，
只有模 p 缩到其所指定直线的 p 个自由直线含它；
若 $v(x)=-1$，$px\bmod p^2$ 本原，只有它自己生成的一个自由直线含它；
若 $v(x)<-1$，没有格含它。
$x=0$ 属第一种。
因此得到整个 Schwartz 函数身份
$$
\boxed{\mathcal H_p\phi_0
 =p^2 B_1\otimes B_1
 +(p-1)B_0\otimes B_0
 +B_{-1}\otimes B_{-1}.}
\tag{77}
$$
四个区域上的值分别是 $p(p+1),p,1,0$，支付全部陪集。
这里没有混入经典 $T_{p^2}$ 的额外中心陪集。
若另选除以 $p(p+1)$ 的平均，必须将(77)及以下每项同时除去该数。

### 16.2 原全六输出上的正负球返回

原 Y、K 的 theta degree 是126、6，
半特征均为 standard even。
R1040(95)–(96)给 Y 的完整 core 是 $\beta$：
原射线 $\kappa\equiv127\bmod252$，
原非零锚是 $\Theta(3\gamma_7z)$。
K 的同一证明使用
$\kappa\equiv7\bmod12$ 及非零锚 $\Theta(\delta z)$。
两个锚都保持完整半特征并与原 division 图交换；
Heisenberg scalar 作用在整个相应 theta 空间上，
因而其余五个输出的任意系数都保留，而非只对单个边际成立。
特别
$$
\nu|_{Y\in p\mathbf Z_p}
   =\beta(D_{Y,\kappa})_*\nu .
\tag{78}
$$

本篇(35)–(38)已经用同一个 division/Miller 图分别支付
connected 正深度与 étale 负深度。
将它们应用于(77)两个正交轴，得到
$$
\boxed{
 \nu_{\mathcal H_p}
 =p^2\beta^2(D_{Y,\kappa}D_{K,\kappa})_*\nu
 +(p-1)\nu
 +\beta^{-2}(D_{Y,\kappa^{-1}}D_{K,\kappa^{-1}})_*\nu .
}
\tag{79}
$$
负球返回的 $\beta^{-2}$ 含两次原 Haar 费用；
其支撑允许落在 $p^{-1}\mathbf Z_p$，没有将它改称整测度。
H/J/N/A 输出和原 $-1/84$ 均在(79)两边不变。

现在才施加同一个物理 Y-unit。
(79)第一项因 Y 深而为零。
第三项要求原 Y 的赋值恰一；
由(78)在这一个完整环带上取限制，
$$
\nu|_{Y\in p\mathbf Z_p^\times}
 =\beta(D_{Y,\kappa})_*\nu^\times .
$$
故 Y 的两次缩放消去，而 K 的负缩放仍须保留：
$$
\boxed{
 \nu_{\mathcal H_p}^\times
  =(p-1)\nu^\times
    +\beta^{-1}(D_{K,\kappa^{-1}})_*\nu^\times .
}
\tag{80}
$$
这是真正的全输出测度等式。没有先忘 K，也没有把相反的
p 角色仅凭对角惯性删掉。

### 16.3 中央读者和有限点读者的不同本征值

忘 K 后，(80)给
$$
\boxed{
 (\operatorname{pr}_{Y,H,J,A,N})_*
       \nu_{\mathcal H_p}^\times
 =(p-1+\beta^{-1})
    (\operatorname{pr}_{Y,H,J,A,N})_*\nu^\times .
}
\tag{81}
$$
所以同一个 Y-Mellin 函数准确满足
$$
 J_{\mathcal H_p}(v)
 =(p-1+\beta^{-1})J_\nu(v),\qquad
 J_\nu(v)=39\delta J_{\Phi_{126},p}(v).
\tag{82}
$$
原 E3969 中央坏条件确实使(82)的原首导数为零。
这里没有将这个零微分到另一个方向。

另一方面，$K/Y$ 在(80)第二项多读到 $\kappa^{-1}$：
$$
\boxed{
 \mathcal L(\nu_{\mathcal H_p})
 =(p-1+\beta^{-1}\kappa^{-1})\mathcal L(\nu),
 \qquad
 \mathcal L(\nu)=\frac{10\delta}{7}\Omega I_{D,p}\ne0 .
}
\tag{83}
$$
最后一个等号和非零是 R1046(26)、(28)已经支付的同一个
$E_D:y^2=x^3+21609$ 固定非挠点，
包括完整 primitive Katz 来源、原微分和周期；
本节没有再造一个新点或重新执行其解析一阶证书。

更具体地，在同一个有限 Schwartz 空间定义
$$
 \mathcal Z_p=\mathcal H_p-(p-1+\beta^{-1})\,1 .
\tag{84}
$$
它只有 $p(p+1)+1$ 个显示有限项，系数 $\beta^{-1}$ 是原 CM
代数数。由(80)，
$$
\boxed{
 \nu_{\mathcal Z_p}^\times
   =\beta^{-1}\{(D_{K,\kappa^{-1}})_*-1\}\nu^\times,\qquad
 (\operatorname{pr}_{Y,H,J,A,N})_*
       \nu_{\mathcal Z_p}^\times=0 .
}
\tag{85}
$$
因此对任何仍保全部其它输出、但不读 K 的连续测试，
其整个积分都为零；所有原 Y-Mellin 系数也都为零。
这不需要中央坏假设。
然而同一个原有限角读者准确为
$$
\boxed{
 \mathcal L(\nu_{\mathcal Z_p})
 =\beta^{-1}(\kappa^{-1}-1)\,
       \frac{10\delta}{7}\Omega I_{D,p}\ne0 .
}
\tag{86}
$$
因为 $v_p(\kappa)=1$，$\kappa^{-1}-1\ne0$；
所有其它因子已在同一原规范中非零。

(85)–(86)是一个实际来源上的反例，说明
“整个 Y-unit 边际已知”本身不能定义其 $K/Y$ 读者，
即使先加入整个球面 Hecke 和也不行。
它不反证某个仍未取得的、同时使用其它真实来源的强迫定理，
也不假定原中央坏条件实际存在。
它精确关闭的是：从(82)的坏中央零或更强的整边际零，
仅凭这一个完整球面 Hecke 身份推出(83)或(86)为零。
S3150 全点载体的非零与原 canonical 坏条件之间，
仍须另给同一有序来源上真正读 K 的关系；
原(59)的5-new和p-new费用不能用(81)代替。
