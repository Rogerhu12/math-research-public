# R18：可计算 F224 的精确全频尾与理想 Robin 误差包络

2026-11-12，exact_closure，GPT-6 Astra Pro，AI-assisted。

**新结论。** 不改变 R15/R17 的有理 profile、共同度量或完整方程，仅改进局部存在证明的辅助 cutoff 与角宽分配，局部全频胞元 map 可从 n192 开始。随后在 R15 的 Green 方程里缩小球，得到 **F224 处的真实 low46-height-to-full-trace 图**，其归一低高度球可取

$$\boxed{|z|_1<2^{-1947}.}$$

这个图限制到 N4096 后，由同一完整方程和 R17 的唯一性直接与 R17 精确族重合；不需要浮点走过下溢区。这个结论仍不认证浅头数值数据属于该图，也未完成大幅闭曲面。

**端口编号。** 本文严格沿用 R15 的 $X_{n-1}=\mathcal A_nX_n+\cdots$：$U_n$ 位于 source cell n 的**内端**。数值程序的 physical node k 位于 cell k−1 的内端。因此数学 F224 对应 **physical node225 / linearFar225**；程序 far224 是数学端口223，二者不可混称。下面的尺度换算和诊断明确包含这个 +1。

## 1. 保持的对象与这次改变的辅助量

保持 R15/R17 的固定深源、实际半径归一、完整 mean 分支，以及

$$
h=(\log2)/4,\quad b=11/2,\quad
\sigma=3/8,\quad C_G<2^{27},\quad C_E=2^{61}.
$$

取新的局部辅助量

$$
\widetilde\gamma=h/2,\qquad
\widetilde M_n=
2\left\lceil\frac{6144}{2\widetilde\gamma}(1+|\log\delta_n|)\right\rceil.
\tag{1.1}
$$

最终胞元 map 是实际全角 Cauchy map；改变证明 cutoff 不改变它。取完整流唯一性所用的共同小物理球，之后所有 map 均属于同一分支。

由 $\log2<7/10$、$|\log d_0|<6$、$h>1/6$，对 n≥192 有

$$
1+\widetilde M_n
\le73728\{(7/10)n+7\}+3
\le\overline M_n:=51611(n+10).
\tag{1.2}
$$

所有整数/有理比较由附属 closure_scaled_radius_ledger.py 核算。下文不使用原来的充分限制 $M\le\delta^{-1/16}$。

## 2. 直接支付低模实际传播

R17 §3 对六个短段的真实生成元积分给

$$
\sum_{\rm short}\int\|B_m\|_1
\le24(1+m)^4\sqrt\delta.
$$

在 n192 上，

$$
24\overline M_{192}^4\,2^{-199/2}<1/2<\log2.
\tag{2.1}
$$

这等价于一个整数比较，未用浮点谱采样。此后左侧的相邻比值至多
$(203/202)^4/\sqrt2<1$。故对每个 n≥192 和全部 $m\le\widetilde M_n$，六段总增益及任意部分逆的总增益仍至多2。

三个真实平台和 raw/canonical 端口因子完全沿用 R17 (3.1)，所以原明确常数继续成立：

$$K_M\le2^{16}(1+\widetilde M_n)^{12}.$$

R17 的材料常数 $C_{\rm mat}=2^{52}$、辅助复输入球
$R_0=2^{-240}\mu_0\delta^2(1+\widetilde M)^{-60}$、bootstrap 比例 $2^{-154}$、完整 mean 和统一物理球的全部推导，只在这一处用到了旧 cutoff 限制。因此这些估计在新的 cutoff 上逐项不变。

## 3. 更充分使用一次固定角宽

有限 Galerkin 近解仍在 $\tau+h$ 上构造。

1. 花 $h/8$ 转换强时空范数，得到近解在 $\tau+7h/8$ 上的
   $Y_{\rm app}\le2^{32}\delta^{-1}(1+\widetilde M)^{15}I$。
2. 把完整残差降到 $\sigma_0=\tau+3h/8$；这次可用整个 $h/2$ 的差，故高频因子为 $e^{-(h/2)\widetilde M}=e^{-\widetilde\gamma\widetilde M}$。
3. 真全频强迫流只花至多 $h/8$；最后仍余 $\tau+h/4$，足够输出 raw 值和完整两 jet。

第三项必须重新检查，不能从旧的 $h/4$ 门直接引用。对 n192，

$$
\beta(\delta)
\le3\delta+4\delta^{3/2}
+\sqrt{5\delta^{3/2}\{10+6(n+6)\}},
$$

其上界在 n≥192 递减。在 n192 上平方根的常数小于128，因而

$$256\beta(\delta_{192})<2^{-133}<1/48<h/8.$$

所以整个真实九段只支出这一次固定角宽；没有在 Picard 迭代中重新缩 strip。

完整残差仍是
$e=B^{-1}(I-\Pi_{\widetilde M})(B\kappa_y^M-\rho_{\rm dens}\mathscr G)$。
R17 的强范数、完整 leading inverse 与 mean 推导因此仍给

$$
S\le2^{44}e^{-\widetilde\gamma\widetilde M}
(1+\widetilde M)^{15}\delta^{-7/2}I.
\tag{3.1}
$$

真输入与投影输入的物理初值差，从 $\tau+h$ 到 $\sigma_0$ 有 $5h/8$；保留 $h/8$ 支付三阶角导数，剩下 $h/2$ 支付指数尾。

$$
\sup_{m\ge0}(1+m)^3e^{-(h/8)m}
\le(1+24/h)^3<145^3<2^{22}.
$$

连同物理换算和 complete mean 的 Lipschitz 因子，$I_0\le2^{32}e^{-\widetilde\gamma\widetilde M}I$。
因此仍有

$$
I_0+9S\le2^{48}e^{-\widetilde\gamma\widetilde M}
(1+\widetilde M)^{15}\delta^{-7/2}I.
\tag{3.2}
$$

## 4. 校正球、输出球和同一局部常数

由 $\widetilde\gamma\widetilde M\ge6144(1+|\log\delta|)$ 和 R17 已逐项支付的 $K_R<2^{6764}$，

$$
\|V\|_{\mathcal W^1}^{\#}
\le2^{6812}(1+\widetilde M)^{15}\delta^{3250.5}I.
\tag{4.1}
$$

n192 有 $\overline M_{192}<2^{24}$、$\delta<2^{-199}$，所以右侧 $I$ 系数的二进制对数小于

$$6812+15\cdot24-3250.5\cdot199=-639677.5.$$

此后该上界单调改善。代入辅助输入球后，它远小于 $10^{-6}w_{\min}/4$，实际支付每个子段的强迫允许球。

这次连源 F §5.3 的更强要求——**校正输出**落在粗原点 raw 输入球——也直接支付。raw 转换至多4，所以在最大输入上

$$
4\|V\|\le2^{6574}\mu_0(1+\widetilde M)^{-45}\delta^{3252.5}.
$$

R17 的 $c_\rho>2^{-6822}$ 给

$$
\frac{4\|V\|}{c_\rho\mu_0\delta^{2891}}
<2^{13396}\delta^{361.5}
<2^{-58542.5}<1.
\tag{4.2}
$$

这里比较的是校正输出，不只是初值加残差。这个附加要求比实际 forced Volterra 所需更强，已经支付。

校正两 jet 仍至多 $2^{14}\delta^{-5/2}\|V\|$，所以其 $I$ 系数至多
$2^{6826}(1+\widetilde M)^{15}\delta^{3248}$，在 n192 起远小于1。
端口 map 增益、共同复球全纯性及 Cauchy 余项推导因此逐项沿用 R17 §6：

$$
\boxed{c_*=2^{-256},\qquad C_*=2^{320},\qquad n\ge192.}
\tag{4.3}
$$

条件仍包括 $64\epsilon\delta_n^{7/4}\le1$；当前严格 $2^{14}<\epsilon<2^{15}$ 使它在 n192 起成立。局部真实 map 的半径、二次余项和两 jet 公式使用 $\widetilde M_n$ 代替 R15/R17 的旧辅助 $M_n$。

## 5. F224 的缩球 Green 解

在任意 F≥192 仍取

$$
\zeta_n=\epsilon\delta_n^{11/2},\quad
\tau_n=\tau_F+(n-F)h,\quad \tau_F>0.
$$

真实线性 Green 和中心/不稳定规范保持 R15 的定义；其线性误差门为
$\eta_F<2^{85-F/2}$。
改写两个局部预算：

$$
\widetilde A_F=\sup_{n\ge F}(1+\widetilde M_n)^{60}\delta_n^{3/4},
$$

$$
\widetilde B_F=\sup_{n>F}(1+\widetilde M_n)^{72}\delta_n^{3/8},\qquad
\mathcal K_F=C_G\,2^{-11/2}C_*\delta_F^{3/8}\widetilde B_F.
$$

必须处理第二个上确界，不能未经证明取它在 F 的值。对 n192…315，
$\overline M_n\le\overline M_{315}=16773575<2^{24}$。
对 n≥315，$(n+10)^{72}2^{-3n/8}$ 递减，因为
$72/(n+10)<1/4<(3/8)\log2$。因此对 F=192、224，

$$
\widetilde B_F\le2^{72\cdot24}\delta_F^{3/8}.
\tag{5.1}
$$

对应的60次幂函数已经从 n192 递减，故
$\widetilde A_F\le2^{60\cdot24}\delta_F^{3/4}$。

在 F224 得

$$
\widetilde A_{224}<2^{1266.75},\qquad
\mathcal K_{224}<2^{1896.25},\qquad
\eta_{224}<2^{-27}.
\tag{5.2}
$$

现在在半径

$$\boxed{\mathfrak r=2^{-1900}}$$

的 $\mathcal X$ 球解同一个真实方程

$$
X=H(\mathbf b)+\mathcal G_0\{\mathcal E X+\mathscr R^\sharp(X)\}.
$$

局部胞元允许球的相对用量满足

$$c_*^{-1}\widetilde A_{224}\mathfrak r<2^{-377.25}<1/4.$$

当 $|\mathbf b|_1\le\mathfrak r/2$ 时，映射把该球映入自身；其 Lipschitz 常数至多

$$
\eta_{224}+2\mathcal K_{224}\mathfrak r
<2^{-27}+2^{-2.75}<1/4.
\tag{5.3}
$$

所以这是完整全频、完整 mean 的真实解，且 $\|X(\mathbf b)\|\le2|\mathbf b|_1$。两 jet 和平端点、单值发展、深部嵌入由同一局部界与 R15 §7 继续成立。

作为核对：F192 也可取状态球 $2^{-1924}$，其线性门仍小于 $2^{-11}$；这里只没有给 F192 使用同样数值的低高度反函数界。旧 R17 cutoff 的 F512 状态球 $2^{-2188}$ 是另一项充分选择，已经被当前较浅构造超越。

## 6. 真实低46高度图的数值半径

F224 的线性高度 chart 仍由 R15 §8 支付：

$$\|D'(0)^{-1}\|_1\le A:=2000000<2^{21}.$$

在缩球内，同一固定点差量估计给

$$
\|D(\mathbf b)-D'(0)\mathbf b\|\le8\mathcal K_{224}|\mathbf b|_1^2,
$$

$$
\|R(\mathbf b)-R(\mathbf c)\|
\le8\mathcal K_{224}(|\mathbf b|_1+|\mathbf c|_1)|\mathbf b-\mathbf c|_1.
$$

取

$$r_b=2^{-1924},\qquad r_z=2^{-1947}.$$

有 $r_b<\mathfrak r/4$、$16A\mathcal K_{224}r_b<1/4$，
且 $Ar_z\le r_b/4$、$8A\mathcal K_{224}r_b^2\le r_b/8$。
于是高度反函数方程在 $|\mathbf b|\le r_b$ 上把球映入自身且收缩。这支付了开头的完整 low46-height-to-full-trace 图。

给定的是前46个**归一高度**；输出包括全部斜率、全部第47模起的高度/斜率以及完整 mean 梯度。不得把未表示高模高度另行设0。

## 7. 为什么它就是 R17 的精确族，而非另一个远边界

限制当前解到 N4096，并取 R17 的绝对角宽为
$\tau_N=\tau_F+(4096-F)h$。两套归一状态 $X_n$ 在 n≥4096 逐项相同。
当前 $\|X\|\le2^{-1900}$，而 R17 在该段的单位球局部/收缩条件全部成立。

把当前解的中心无穷端极限和45个不稳定投影在 N 处的值用作 R17 标签。
这些标签小于 R17 的 $1/4$ 球：例如对 j≤46，$\nu_j<2^{23}$；由 R15 的真实理想矩阵和特征值间隙，可以将全部有限谱投影范数之和粗放到 $2^{60}$，故标签范数小于 $2^{60-1900}$。
R17 的同规范固定点唯一性遂给两段一致。mean 高度只需沿用同一次平移规范。

这一论证在精确实数/解析空间中进行，**没有在 double 下把 $\delta_{4096}$ 置0**。N4096 不再是数值深桥必须抵达的端口；F224 已是一个精确可用的入口。

## 8. 数值数据应如何接入，哪些尚未接入

设数值程序的物理 raw 高度为 $Q_{\rm phys}=C_{\rm phys}/r^4$。
在 $r=r_c\rho,z=r_c\widetilde z$ 的归一下，

$$
Q_{\rm norm}=r_c^3 Q_{\rm phys},\qquad
\xi_{\rm norm}=r_c^3\xi_{\rm phys},\qquad
\epsilon=\epsilon_{\rm phys}/r_c^7.
$$

因此 F224 的低高度输入是

$$
z_j=(-1)^{jF}e^{2j\tau_F}
\frac{r_c^{10}Q_{{\rm phys},2j}(F)}
{\epsilon_{\rm phys}\delta_F^{11/2}}.
\tag{8.1}
$$

实际数据必须连同斜率匹配该图；(8.1) 小于允许半径只支付定义域，不会自动消除斜率缺陷。幅度的对数诊断也必须注明是否只是线性外推。

当前 q003 新 g 的有限非线性求解在 depth8 成功。它的精确 F224 端口、未表示高模、以及从 finite Robin 到上述真实图的斜率/mean 差量尚待实际尺度化传播与误差控制。已有有限线性 log gain（含上述端口 +1）给出的约394bit余量只用于选择下一步的预算；不是已经证明的匹配。

后续应把实际 rawStates[8] 送入同一固定新 g 的有限头，求 F224 的低高度及完整 trace 残差，再用本图补全深端。源 head 的非线性、warp、calibration 存数及数值误差全部保留，不再把阶段性数值图当成完整闭合。

## 9. 可执行的理想 Robin 边界及严格误差包络

现在对每个自由模预条件为 $(Q_j,\xi_j/\nu_j)$，其中
$\nu_j=j^2(4j^2-1)/3$。这是一次线性估计的范数选择；不改物理状态、非线性 map 或 Galerkin 方程。

### 9.1 预条件后的真实线性漂移

对 R15 的三个平台，理想 shear 的范数现在是

$$s_1=65,\quad s_2=1+\alpha\nu_j\le3\nu_j,\quad s_3=2.$$

相应非零 shear 元素为 $(64,\alpha\nu_j,1)$，误差中剩余元素为
$(\nu_j/64,1/\alpha,\nu_j)$。由同一个真实三角函数公式，三项分别仍满足
$e_i/s_i\le(5/2)\nu_j\delta$。
六个短段的积分范数仍至多
$L\le(130/3)\nu_j\sqrt\delta$。
因而 R15 的不交换次序的乘积差估计现在给

$$
\|S_j(T_{2j,n}-T_{2j,\infty})S_j^{-1}\|_1
\le339300\nu_j^2\sqrt{\delta_n},
\quad S_j=\operatorname{diag}(1,\nu_j^{-1}).
\tag{9.1}
$$

这里乘积 $\prod s_i\le390\nu_j$，比原 raw 范数少一个 $\nu_j$，没有用一个粗糙的 $\|S_j\|\|S_j^{-1}\|$ 再丢回去。
归一矩阵再乘 $2^{-11/2-j/2}$。利用

$$
\nu_j^2<(16/9)j^8,\qquad
\sup_{x>0}x^8 2^{-x/2}
=\{16/(e\log2)\}^8<9^8,
$$

全部46模可以统一取

$$
C_{E,\rm bal}<2^{40},\qquad
\|\mathcal E_n\|_{\rm bal}\le2^{40}\sqrt{\delta_n}.
\tag{9.2}
$$

附属脚本用整数平方验证最后一个常数比较。

### 9.2 小的平衡 Green 常数

预条件理想 raw 矩阵的范数小于 $76\nu_j$，大、小特征值之间的间隙大于 $63\nu_j$，因此不稳定投影范数小于2、稳定投影小于3。第一模中心/稳定投影也满足同样上界。
对 j2…46，精确整数比较给

$$
\nu_j2^{-(j-1)/2}>1+1/256.
$$

小特征值模小于1/4。把共同标量核从 $\ell^\infty_n\ell^1_j$ 的求和中提出，分别估计中心未来、稳定未来和不稳定过去三类核，可取

$$
\|\mathcal G_{0,\rm bal}\mathcal E\|
\le(6+4+512)C_{E,\rm bal}\sqrt{\delta_F}
<2^{50}\sqrt{\delta_F}.
\tag{9.3}
$$

这里没有把46个独立核的最大值错误替代其和：中心、稳定和不稳定各使用一个统一的正标量卷积核，然后对模态求和。
F224 上 $\delta_F<2^{-231}$，故 $\eta_{\rm bal}<2^{-65}$。

令 $s_j$ 是 R15 理想 raw 不稳定/中心向量 $(1,s_j)$ 的斜率（$s_1=0$）。有 $|s_j|/\nu_j<d<3/20$，所以平衡归一后的第一分量大于1/2。理想高度逆至多2，实际线性高度逆至多4。Neumann 扰动和高度坐标转换于是给真实线性图

$$
\sum_{j=1}^{46}
\frac{|X^{\rm lin}_{\xi,j}-s_j z_j|}{\nu_j}
\le2^{-60}|z|_1.
\tag{9.4}
$$

其第47模以后的线性 trace 严格为0，因为实际线性方程不耦合角频。

### 9.3 完整非线性余项和实际可用小球

回到已证明的 raw 范数，不借用未证明的“平衡非线性常数”。§6 给
$|\mathbf b|\le2A|z|$、$\|X(\mathbf b)\|\le2|\mathbf b|$。
将 nonlinear 图与**相同低高度**的实际线性图比较，参数修正至多
$32A^3\mathcal K_{224}|z|^2$，故完整 raw trace 差可放宽到

$$
\|\Gamma_{224}(z)-\Gamma^{\rm lin}_{224}(z)\|_{\rm raw}
\le128A^3\mathcal K_{224}|z|_1^2
<2^{1967}|z|_1^2.
\tag{9.5}
$$

这一界包含全部高模。平衡范数不大于 raw 范数，因此如果

$$\boxed{|z|_1\le2^{-2048},}$$

则完整精确图满足可直接使用的误差条件

$$
\boxed{
\sum_{j\le46}\frac{|X_{\xi,j}-s_jz_j|}{\nu_j}
<2^{-59}|z|_1,\qquad
\sum_{j>46}(|X_{Q,j}|+|X_{\xi,j}|)
\le2^{1967}|z|_1^2\le2^{-81}|z|_1.
}
\tag{9.6}
$$

所以在这个明确小球内，可用理想 Robin 作为**带严格误差包络的数值端口**。它仍不是精确等号；实际匹配需要吸收 (9.6) 而不是直接删除它。理想斜率的浮点求值误差也应另加进实现的区间。

### 9.4 完整 mean 的端口和高度规范

为给 mean 同样明确的接口，取 $\tau_F\ge h$。real 角上的非mean物理梯度满足

$$
Y_\perp\le2^{30}(1+3/\tau_F)^3
\epsilon\delta_F^{11/2}|z|_1.
$$

端口 $p_*=1$、$w_F\ge\epsilon\delta_F^{11/4}/128$，
完整 mean 根 $|\kappa_0|\le40Y_\perp^2/w_F$ 因而给

$$
\boxed{|\kappa_0(F)|\le2^{99}\epsilon\delta_F^{33/4}|z|_1^2.}
\tag{9.7}
$$

这里是物理 slope 修正，归一前后相同。没有把它设为0。

固定 cuff 上的 mean 高度为0，沿实际尾统一积分。完整胞元物理梯度界与同一个 mean 根给每胞元增量至多
$2^{86}\epsilon(1+\widetilde M_n)^{30}\delta_n^{25/4}\|X\|^2$。
从 F224 起该数列相邻比值小于1/64，且 $\|X\|\le4A|z|<2^{23}|z|$。放宽后得到物理高度规范

$$
\boxed{
|\overline v_{\rm phys}(r_F)-\overline v_{\rm phys}(r_c)|
\le r_c\,2^{853}\epsilon\delta_F^{25/4}|z|_1^2.
}
\tag{9.8}
$$

两 jet 仍由 §4 的完整胞元引理给出。式 (9.7)–(9.8) 是 mean 的真实重建界，只允许这一次 cuff 平移规范，不是另设两个 mean 边界条件。
