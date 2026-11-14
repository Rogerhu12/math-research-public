# R119 续篇：实际负型段的度量参数与严格非零旋转导数

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 在实际 R72 无限尾的每个下降过渡内部加入一个
明确的实参数，可以同时保持所有胞元端点二阶 jet、全部正型区间、
平坦极限和闭参考面的嵌入。每个完整负型分量含一个这样的参数；
在零非径向标签处，其真实两射线往返圆周映射是旋转，旋转角对该
参数有严格同号的显式导数。所得可调角窗的平方为
$\delta_j^{3/2}/j$ 的量级。

本结论给出可供后续联合选取的**度量族**。它没有把原固定度量的
Newton 步偷偷换成另一个度量，也没有证明非径向背景上的完整混合
return 可逆。特别，本文不把零标签的旋转导数直接当作非径向
圆周映射旋转数的导数。

## 1. 实际胞元、两种下降段及其所在的负型分量

使用 quantitative-newton-twist-flex 的 R72 §2 的实际数据；其被
R69 §5 安装的物理缩放不变。对 $j>128$，
$$
 \delta_j=\frac2{25}2^{-j},\qquad
 \eta_j=\frac{\delta_j^{3/2}}{4\sqrt2},\qquad
 w=\frac{\epsilon\delta_j^6p_*}{r^7},\quad 1\le r\le2,
 \quad r_y=\frac r{\sqrt{12}}.
 \tag{M.1}
$$
五个平台依次为
$1,64/\delta_j,\delta_j/(65/64),1/\delta_j,64$。
令 $t=\log r+\mathrm{const}$，则 $dt=dy/\sqrt{12}$。
每个 log-quintic 过渡上使用
$$
 S(x)=10x^3-15x^4+6x^5,\qquad 0\le x\le1.
$$
两种下降段的准确 log 落差为
$$
 \Delta_{j,1}=\log65+2|\log\delta_j|,
 \qquad
 \Delta_{j,2}=|\log\delta_j|-\log64.
 \tag{M.2}
$$
在任一这样的段内，
$$
 dt=\frac{\eta_j}{\sqrt{12}}dx,\qquad
 \log p_*=\log p_{\rm in}-\Delta S(x),\qquad
 A:=w_t/w=-7-\Lambda S'(x),\quad
 \Lambda=\frac{\sqrt{12}\Delta}{\eta_j}.
 \tag{M.3}
$$
对全部 $j\ge129$，
$$
 1<\frac j2<\Delta_{j,k}<3j.                 \tag{M.4}
$$
例如 $2/3<\log2<3/4$、$2<\log(25/2)<3$ 和 $\log65<5$
直接给出两端界；它们在 $j=129$ 后严格改善。

两次上升段各有一个 $A>0$ 的开区间。下降段上始终 $A<-7$，
所以两个下降段属于不同的负型分量。每个内部负型分量恰含一个
下降段；第二类分量跨过相邻胞元接缝。最外侧分量若在 cut128
结束，就以该固定截面作为外端。以下两射线往返取各分量的固定
左右端点，内部端点允许是 $A=0$ 的真实转向点。

## 2. 明确的内部参数及全部接缝 jet

定义 $C^2$ bump
$$
 B(z)=
 \begin{cases}64z^3(1-z)^3,&0\le z\le1,\\0,&\text{otherwise},\end{cases}
 \qquad
 \psi(x)=B\bigl(8(x-1/4)\bigr).
 \tag{M.5}
$$
其支集为 $[1/4,3/8]$，且支集两端的零、一、二阶 jet 均为0。
直接微分给出
$$
 0\le\psi\le1,\quad |\psi_x|\le96,\quad
 |\psi_{xx}|\le6144,\qquad
 \int\psi\,dt=\frac{2\eta_j}{35\sqrt{12}}.
 \tag{M.6}
$$
最后一式使用 $\int_0^1 B(z)dz=16/35$。

取所有实参数
$$
 \Gamma=(\gamma_{j,k})_{j\ge129,\ k=1,2},\qquad
 |\gamma_{j,k}|\le r_\gamma:=2^{-16}.
$$
在对应的实际下降段使用 (M.5)，记作 $\psi_{j,k}(t)$；这些支集
两两不交。准确定义
$$
 w_\Gamma=w\exp\!\left(\sum_{j,k}\gamma_{j,k}\psi_{j,k}\right),
 \qquad
 A_\Gamma=A+\sum_{j,k}\gamma_{j,k}(\psi_{j,k})_t.
 \tag{M.7}
$$
每一点至多有一项非零。所有胞元端点和原过渡端点附近均未改变，
故 $w,w_t,w_{tt}$ 的完整接缝 jet 准确不变。所有正型区间及其
邻域也准确不变，而不仅是零点位置接近。

在支集上，
$$
 \frac{135}{128}\le S'\le\frac{3375}{2048}<\frac{15}{8},
 \qquad 3<\frac{225}{64}\le S''\le\frac{45}{8}<6.
 \tag{M.8}
$$
因此
$$
 \frac{|\gamma\psi_t|}{-A}
 \le\frac{96|\gamma|}{\Delta}<\frac1{32},\qquad
 \frac{|\gamma\psi_{tt}|}{-A_t}
 \le\frac{2048|\gamma|}{\Delta}<\frac1{32}.
 \tag{M.9}
$$
这里 $-A_t=12\Delta S''/\eta_j^2$。所以 $A_\Gamma<0$，
$A_{\Gamma,t}<0$ 在支集内严格成立；支集外型别完全未变。
没有产生额外转向点。

同时，下降段的实际 log profile 仍严格单调，并具有原来的端值。
全部 $p_*,p_*^{-1}$ 的逐段范围保持原值。这一点比粗乘一个
$e^{r_\gamma}$ 更强；后者只在几何差分估计中使用。

## 3. 零标签的真实两射线往返与非零导数

在轴对称参考背景，即非径向标签为0时，准确一阶 principal 是
$$
 \begin{pmatrix}0&1\\-A_\Gamma(t)&0\end{pmatrix}\partial_\theta.
$$
其两个实特征值为 $\pm\sqrt{-A_\Gamma}$。按
$Y_t=\lambda Y_\theta$ 的 ray 约定 $\dot\theta=-\lambda$，
先用正支从左端走到右端，再用负支从右端走回左端，得到实际 lift
$$
 R_{j,k,\gamma}(\theta)=\theta+\Theta_{j,k}(\gamma),\qquad
 \Theta_{j,k}(\gamma)=-2\int_{I_{j,k}}\sqrt{-A_\Gamma(t)}\,dt.
 \tag{M.10}
$$
所有积分有限，端点的平方根零点可积。支集与端点分离，所以关于
$\gamma$ 的任意微分都在严格负型的紧子段内进行，不涉及微分移动
转向点。每个 $\Theta_{j,k}$ 只依赖自己这个参数；其余参数的偏导
准确为0。

积分分部给出
$$
 \begin{split}
 \Theta'_{j,k}(\gamma)
 &=\int\frac{\psi_t}{\sqrt{-A_\Gamma}}\,dt\\
 &=-\frac12\int
       \frac{\psi(A_t+\gamma\psi_{tt})}{(-A_\Gamma)^{3/2}}\,dt>0.
 \end{split}                                                     \tag{M.11}
$$
支集端点的 $\psi=0$ 消除了边界项。该严格正号来自真实下降段的
$A_t<0$，不是由一条抽象参数横截假设提供。

在 $\gamma=0$ 时，$\Lambda>7$，故支集上
$\Lambda<-A<3\Lambda$，以及
$36\Delta/\eta_j^2<-A_t<72\Delta/\eta_j^2$。
连同 (M.6)，
$$
 \frac{36}{35\sqrt{12}\,3^{3/2}(\sqrt{12})^{3/2}}
       \sqrt{\frac{\eta_j}{\Delta}}
 <\Theta'_{j,k}(0)
 <\frac{72}{35(\sqrt{12})^{5/2}}
       \sqrt{\frac{\eta_j}{\Delta}}.
$$
左侧系数大于 $3/560>1/256$，右侧小于 $8/35<1/4$。
(M.9) 将被积函数改变的乘法因子夹在 $1/2$ 与2之间，因此得到
整个实际参数盒上的统一严格界
$$
 \boxed{\quad
 \frac1{512}\sqrt{\frac{\eta_j}{\Delta_{j,k}}}
 <\Theta'_{j,k}(\gamma)
 <\frac12\sqrt{\frac{\eta_j}{\Delta_{j,k}}}.
 \quad}                                                         \tag{M.12}
$$
这是完整负型分量两支射线的往返角，不是一个截面的瞬时速度。
但它仍只是零标签背景的射线往返；实际 PDE 的正型传播、转向
connection 和幅度传播不由 (M.10) 自动决定。

## 4. 可逐层独立选择的真实相位窗

定义
$$
 \kappa_{j,k}=2^{-25}\sqrt{\eta_j/\Delta_{j,k}}.
 \tag{M.13}
$$
由 (M.12)，闭角窗
$$
 |\vartheta_{j,k}-\Theta_{j,k}(0)|\le\kappa_{j,k}
$$
严格位于 $\Theta_{j,k}([-2^{-16},2^{-16}])$ 的内部。实一维
中值定理给出唯一的连续、事实上 $C^1$ 参数选择，并且
$$
 \left|\frac{d\gamma_{j,k}}{d\vartheta_{j,k}}\right|
 <512\sqrt{\Delta_{j,k}/\eta_j}.
 \tag{M.14}
$$
任意同时选取这些角窗中的目标角，都产生一个参数序列 $\Gamma$。
此处不需要先把无穷多个参数裁成有限项。

准确平方尺度及其两边界为
$$
 \kappa_{j,k}^2=2^{-50}\frac{\eta_j}{\Delta_{j,k}},\qquad
 \frac{2^{-55}}j\delta_j^{3/2}
 <\kappa_{j,k}^2<\frac{2^{-51}}j\delta_j^{3/2}.
 \tag{M.15}
$$
使用 (M.4) 和 $1<\sqrt2<2$ 即得。这里 $\Theta$ 是实角 lift；
若使用 $2\pi$ 圆的归一旋转数，则再除以 $2\pi$；若使用实际
$\pi/2$ 商圆，则再乘 $2/\pi$。后续小除数常数必须采用同一约定。

## 5. 无限参数下的真实 $C^2$ profile 和几何范围

记 $L_j=1+|\log\delta_j|$。由 (M.1)、(M.3)、(M.6) 直接得到
$$
 |w|\le64\epsilon\delta_j^5,\quad
 |w_r|\le2^{15}\epsilon L_j\delta_j^{7/2},\quad
 |w_{rr}|\le2^{25}\epsilon L_j^2\delta_j^2,
$$
$$
 |\psi_r|\le2^{12}\delta_j^{-3/2},\qquad
 |\psi_{rr}|\le2^{23}\delta_j^{-3}.
 \tag{M.16}
$$
例如 $|S'|\le15/8$、$|S''|\le6$、$\Delta<3|\log\delta_j|$
给 $|\partial_r\log p_*|<2^8L_j\delta_j^{-3/2}$ 和
$|\partial_r^2\log p_*|<2^{13}L_j\delta_j^{-3}$；再微分
$w=\epsilon\delta_j^6p_*r^{-7}$ 即得前一行。

对两个盒中参数序列，乘积微分和
$|e^z-e^{\tilde z}|\le2|z-\tilde z|$ 给出
$$
 \max_{0\le q\le2}
 \frac{|\partial_r^q(w_\Gamma-w_{\widetilde\Gamma})|}
      {\delta_j^{5-3q/2}}
 \le2^{34}\epsilon L_j^2
       \max_{k=1,2}|\gamma_{j,k}-\widetilde\gamma_{j,k}|.
 \tag{M.17}
$$
这里二阶微分的四类项依次由
$2^{26},2^{29},2^{30},2^{31}$ 倍的右侧基本量控制，其和小于
$2^{34}$。所有指数 $5-3q/2$ 均为正。

因此 $w_\Gamma,w_{\Gamma,r},w_{\Gamma,rr}$ 在平坦极限处一致趋于0。
固定外端后，整个参数乘积盒连续映入 $C^2$ profile 空间：先控制
有限多个胞元，再用 (M.17) 一致控制其余尾部。这既证明任意无限
参数序列都定义真实 profile，也证明坐标逐点收敛足以产生 $C^2$
收敛。特别没有把无限个参数改变当作形式级数。

保留 R69 的物理缩放 $a=\rho r$ 及 $\epsilon=\epsilon_{\rm tail}$。
因 $|\psi_t|<1920\delta_j^{-3/2}$，新的物理两主曲率所需界满足
$$
 \max\{w_\Gamma/a,|(w_\Gamma)_a|\}
 \le e^{r_\gamma}(1+8r_\gamma)\,B_{69},
 \quad B_{69}=\frac{9375}{131072}.
 \tag{M.18}
$$
具体地，新增项至多
$2^{17}r_\gamma(\epsilon/\rho)\delta_j^{7/2}$；R69 (69.24)
旧界含 $2^{14}(\epsilon/\rho)L_{128}\delta_{128}^{7/2}$，故其比值
小于 $8r_\gamma$。由
$e^{r_\gamma}\le(1-r_\gamma)^{-1}$，
$$
 e^{r_\gamma}(1+8r_\gamma)B_{69}
 <\frac43\frac{9375}{131072}<\frac18.
 \tag{M.19}
$$
所以全部无限尾仍满足原物理曲率预算，而不只是在 cut128 检查
$A=-7$。

## 6. 最终目标度量、mean 高度和普通参数源

在物理尾上准确定义
$$
 g_\Gamma=(1+w_\Gamma^2)\,da^2+a^2\,d\theta^2.
 \tag{M.20}
$$
其他区域沿用原参考目标，尾接缝的完整二阶 jet 已由 §2 保持。
固定 cut128 的高度后，参考高度由
$Z_{\Gamma,a}=-w_\Gamma$ 积分确定。平盘高度是该积分的输出；
不能再独立重置它。直接有
$$
 |Z_\Gamma-Z_0|
 \le2r_\gamma\int w\,da<r_\gamma a_T^2/8,
 \tag{M.21}
$$
其中最后使用 R69 (69.27)。若要上下反射，则在两帽上用同一个
$\Gamma$ 的对应反射，保留原闭面的反射规范。

由于 $w_\Gamma>0$ 且外端高度为正，新增尾的高度仍为正，径向
支持函数 $(Z_\Gamma+aw_\Gamma)/\sqrt{1+w_\Gamma^2}$ 也为正。
其他区域未改。R69 §6 的径向投影覆盖论证因而仍给出闭 $C^2$
参考嵌入。这是近似背景的几何结论，不是完整非径向精确解族。

参数的实际 metric-source 和参考高度列为
$$
 \partial_{\gamma_{j,k}}g_{aa}=2w_\Gamma^2\psi_{j,k},\qquad
 \partial_{\gamma_{j,k}}g_{a\theta}
 =\partial_{\gamma_{j,k}}g_{\theta\theta}=0,
$$
$$
 \partial_{\gamma_{j,k}}Z_\Gamma(a)
 =-\int_{a_e}^{a}w_\Gamma(s)\psi_{j,k}(s)\,ds.
 \tag{M.22}
$$
这些是改变目标度量产生的普通源列，不能当作固定 $g_0$ 下的
齐次 Jacobi 标签方向。最终若联合选定 $\Gamma_\infty$，所求
相位族必须全部对**同一个** $g_{\Gamma_\infty}$ 精确等距。

非径向标签上的 holonomy、径向 mean 及两个高度端值仍须用完整
方程。本文没有为新的 $\Gamma$ 免费宣称一个已存在的全标签图。
它提供该统一图需要的实际 profile 门；完整图的统一构造和依赖
估计应另行给出。

## 7. 正型接口准确保留了什么，以及还没有保留什么

每个正型分量及其两个转向邻域内，$w_\Gamma=w$、
$A_\Gamma=A$ 准确成立。所以
[实际正型两端 DN](R119-supplement-actual-positive-band-two-end-dn-and-ordinary-source.md)
的零标签原始高度参考 form、完整两端 $S_m$、mean 电阻和普通
source 的原始径向系数均准确未变。两端真实角图、密度及非径向
背景则必须随新标签解重算，不能称其 actual updated DN 也不变。

同样，cut128 的背景 jet 不变不意味着实际第四标签的两迹方向
不变。R11 的真实无限尾方向依赖所有胞元，故原 R69/R74 的
critical-fourth 选择不能直接移植。最终联合构造须重新选定
connector 停止位置、物理缩放及双 bump 条件，或证明相应的完整
共同选择定理。长径向段的极大放大使这项遗漏不能由一个小的
绝对 profile 误差代替。

本结果确切支付的是：实际允许的无限维目标度量族、所有端 jets、
其连续几何极限，以及每个完整负型分量在零标签处可调的真实
两射线旋转角和显式逆费用。非径向 return 的参数导数、其 KAM
共轭、正型两端强 Airy 费用及最终单一目标的全局匹配仍须继续。

## 8. 可复核的准确预算

`scripts/fourfold_negative_band_metric_parameters_20261113.py` 使用准确
有理数和符号多项式核对 bump jet、面积、区间导数界、旋转导数
常数、相位窗、$C^2$ 预算和物理曲率余量。输出为
`notes/2026-11-13-R119-negative-band-metric-parameter-budget.json`。
程序不把有限采样当作无限层证明；无限层、全部参数及几何收敛的
论证在上文。
