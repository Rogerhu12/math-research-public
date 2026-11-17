# R39 有限主部进入全域 metric 算术的精确接口

**状态：有限表示的代数接口已实现并执行；没有新增全域 metric 或闭面结论。** R39 已支付真积分核与有限主部之间的全径向微分误差，但此前缺少将那个完整主部直接送入 R31 卷积程序的实现。本条补这一项，复用已登记的 R37 有限主部系数与原共享数据，不重算原真积分证书、不求 BVP、不重铺已知 metric 不合格的 M8/M16 图。

## 1. 被编译的唯一对象

令 $C$ 为原有限 Cartesian 共享二 jet 五次图，$f$ 为同一网格上的一次参考 lift 系数；$C_j=\partial_s^jC(0,\psi)$。$h_0,h_1,h_2$ 是原中心宽度上的三条 Hermite 权重，$V_{\rm in}$ 是原参考初始 Fourier 投影。输入另包括 R37 已认证的字面有限 $G_N,T_N$，以及 R39 的有限圆函数 $E_N$。接口输出的对象正是

$$
\begin{aligned}
P={}&C+f(G_N-E_N-q_gV_{\rm in})\\
 &+h_0(E_N+q_gV_{\rm in}-C_0)
  +h_1(e_z-C_1)+h_2(bT_N-C_2),\\
 b(\psi)={}&-E''(0)\sin(3\psi)/3.
\end{aligned}
\tag{1}
$$

$q_g$ 必须取检查点的 `gauge_amplitude`。实际核幅度 `actual_primary_amplitude` 已包含在 $G_N,T_N$ 的来源中；固定 $g$ 精化时两者可以不同，不允许用实际核幅度替换 (1) 的 $q_g$。

这是用于误差证明的辅助有限主部，不是修改原实际图。真图与 $P$ 的差仍按 R36/R37/R39 支付。新候选必须有自己的完整角余项证书；R41 的 17 点接口误差不能作为此处所需的全角 C¹ 证书。

## 2. 全部系数的精确构造

新增 [integral_principal_polynomials.py](../scripts/resume_closed/integral_principal_polynomials.py) 把输入 binary64 系数逐一转为精确 `Fraction`，每个径向 span 按需构造 (1) 的系数，最后才用向外 binary64 包围交给原区间算术。

原源的柱坐标投影约定是

$$
V_{xy}=e^{i\psi}\left[c_0+\sum_j r_j\cos3j\psi
+i\sum_jt_j\sin3j\psi\right],\quad
V_z=\sum_jz_j\cos3j\psi.
$$

所以 $1+3j$、$1-3j$ 两个平面频率的系数分别为 $(r_j+t_j)/2$、$(r_j-t_j)/2$，频率 1 为 $c_0$。全部系数保留，包括高度分量。

圆主部按

$$
E_N=e^{i\psi}\sum_{r=0}^{N}\frac1{r!}
\left[\frac{e_r}{6}(e^{-3i\psi}-e^{3i\psi})\right]^r
\tag{2}
$$

直接进行有理二项式展开，没有 FFT。R37 的 $G_N$ 系数精确为实数，$T_N$ 系数精确为纯虚数。若 $T_N$ 的频率 $k$ 系数为 $it_k$，则 $bT_N$ 在 $k+3$ 和 $k-3$ 的贡献分别为

$$
-E''(0)t_k/6,\qquad E''(0)t_k/6.
\tag{3}
$$

因此输出平面系数仍为实数，且频率均为 $1\pmod3$；高度保持 $\cos3j\psi$。精确三重协变与反射性来自这些字面条件，不依赖近零的 DFT 残差。

每段局部变量是 $t=(s-s_0)/(s_1-s_0)$。原共享二 jet 按精确有理五次 Hermite 公式转换，端点差在转成浮点以前完成。中心权重在同一变量中由
$h_j(s)=w^jH_j(s/w)$ 精确重展开；$w$ 必须已经是共同网格节点，超过 $w$ 后所有中心权重恒为零。每项的径向次数均不超过 5。

于是 (1) 在所有共享节点是 C²，中心宽度处也 C²。$f(0),f'(0),f''(0)=(1,0,0)$ 的字面输入检查给

$$
P(0,\psi)=G_N(\psi),\qquad P_s(0,\psi)=e_z,
\qquad P_{ss}(0,\psi)=b(\psi)T_N(\psi).
\tag{4}
$$

中心参考角与实际中心角的极小差仍留在 R39 的真图余项内，不在编译过程中把两个角静默设为相同。

## 3. 与 R31 程序的连接和边界

`IntegralPrincipalCompiler.span_box(i)` 返回该段完整 $(6,C)$ 系数的外包围与精确段长；`phase_box(i)` 返回相同网格上的角图五次系数。`metric_numerators(i, auxiliary_radius_box)` 直接调用原 `interval_prefix_metric.prefix_numerators`，保留全部有限乘积：

$$
\varrho=1-e\cos3\psi,\quad \theta_s=-e_s\sin3\psi/3,
\quad Y=\varrho P_s-\theta_sP_\psi,
$$
$$
A=|Y|^2-\varrho^2,\qquad B=Y\cdot P_\psi,
\qquad C=|P_\psi|^2-a_5^2\varrho^2.
\tag{5}
$$

调用者仍须给出真实候选的辅助半径 $a_5$，支付它与同一物理 $a(\sigma)$ 的差、固定 atlas 变换，以及该候选自己的真积分余项。编译器不会因能产生 (5) 就宣称已通过 metric 门。

当前版本明确拒绝已带 cut lift 的包：它需要那条实际 lift 的有限系数另作为输入，才可加入 (1)。这里不假定未来接缝误差为零，也不把低幅 R31 的数值界移到当前 raw 图。

在登记的 R37/M8 数据上，编译器生成 344 个平面系数、9 个高度系数；最大平面绝对频率 515，高度频率 24，径向次数 5。原完整卷积程序为 (5) 保留到频率 1038、径向次数 20。这些只是有限代数的规模，不是关于真实谱尾或 metric 大小的结论。

## 4. 新接口的实际核验

执行源为 [audit_integral_principal_polynomials.py](../scripts/resume_closed/audit_integral_principal_polynomials.py)。输入是已有的 raw M8 共享包和 R37 已认证的字面 $G_N,T_N$；检查点、共享包、角证书、有限系数文件的 SHA 逐项绑定，未改任何源图。

选择 11 个结构相关 span：中心入口、中心宽度两侧、参考 lift 两端、最短原段及其邻段、最后一段。其有理角点为 $e^{i\psi}=(3+4i)/5$，局部径向点为 $t=2/5$。独立求值直接使用原柱坐标公式、有限指数 (2) 的链式导数与原 Hermite 权重；另一边使用编译后的 Laurent 系数。对
$P,P_s,P_{ss},P_\psi,P_{\psi\psi},P_{s\psi}$ 的 198 个坐标比较，差全部是**精确有理数 0**。这不是浮点接近零。

另在中心宽度处逐系数比较左右零、一、二阶径向 jets，共 1059 个恒等式全部严格相等。最短被纳入的原段长度为
$30747203/1125899906842624$，避免只检查普通长度段而漏掉端点相减问题。

最后只在首段一个有理点核对 (5) 的消费接口，辅助半径明确取形式常量 $a_5=1$。直接有理 Gram 值分别落在原区间卷积给出的 $A,B,C$ 包围内；该常量半径只用于接口核验，**不是该点或整个图的物理 metric 计算**。没有执行全域 metric 区间盒。

正式 session `19587`，exit 0，约 15.50 秒。命令、输入／源／输出 SHA 与紧凑标量见
[integral_principal_polynomial_execution.json](../scripts/resume_closed/integral_principal_polynomial_execution.json)。不提交逐 span 系数或大数组。

这补齐了“已认证角主部 → 完整径向有限主部 → 原 metric 卷积”的接口。新的合格实际终态到来后仍须生成它自己的共享包和全角证书，再进行全域验证；当前 M8/M16 的已知坏 metric 不因本接口成立而改善。
