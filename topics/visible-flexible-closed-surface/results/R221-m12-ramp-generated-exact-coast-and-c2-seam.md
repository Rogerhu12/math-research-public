# R221 — 原 M12 首 ramp 出口生成的整段精确 coast 与真实 C2 接合

2026-11-26，Astra-visible-flex-6a65e705/g5_and_exact。

本结果把[三档原 M12 首 ramp 有限位置图](../notes/2026-11-26-6a65-m12-central-ramp-three-refinements.md)
的出口作为新的 R137 输入，而非继续使用 R220 的旧图中间截面。
对 M191 输入，整条材料圆周及原完整 affine plateau 有整数区间连续域证明。
首 ramp 与这张精确 coast 之间的全部 Cartesian 两 jet 由一个明确函数恒等式接合。
首 ramp 的 metric 三档数据仍是有限观察；这里没有全闭图、全域 metric 连续证书或 README 第 5 条完成声明。

## 1. 固定度量与新曲线身份

仍用原 `2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json` 的准确 binary64 有理参数。
记 $v=v_u$、$\epsilon=.4$、$\eta=.05$、
$T_u=\delta/[v(1-\epsilon)]$、$R=T_u\epsilon$。
首 ramp 为 $0\le\sigma\le R$，原 affine plateau 为

$$
R\le\sigma\le R+L=T_u(1-\epsilon),\qquad
L=T_u(1-2\epsilon),\qquad f(R+x)=a+vx,
$$

其中 $a=1+vR/2$。这里的 $\sigma,x$ 已是原物理长度坐标，未再作 bridge 尺度替换。
准确值是

$$
a=\frac{159535628153085399228442219580887}{155768905756044823091307366842368},\quad
L=\frac{313893533086714590971614133091}{2206726164877301818986894580375},\quad
v=\frac{6124895493223875}{36028797018963968}.
$$

从 M191 保存场的出口位置 Fourier 系数取 $|k|\le191$，定义有限 Cartesian 曲线
$\gamma(\theta)=\sum_{|k|\le191}c_ke^{ik\theta}$。
每个 $c_k$ 是保存的 binary64 数对应的准确有理数，$c_{-k}=\overline{c_k}$。
不用新的 DFT 近似定义此曲线。定义

$$
a_\gamma=\frac1{2\pi}\int_0^{2\pi}|\gamma'(\theta)|\,d\theta,
\qquad
t(\theta)=a_\gamma^{-1}\int_0^\theta |\gamma'(q)|\,dq,
\qquad
\widehat\gamma(t)=c_0+\frac a{a_\gamma}(\gamma(\theta(t))-c_0).
$$

积分及反函数在数学定义中均准确。数值消费用固定的 256-panel、16 点 Gauss 求积，
不把其数值周长重新定义为 $g$；下节另给严格积分包含区间。
由 $|\gamma'|>0$，$t$ 是满足 $t(\theta+2\pi)=t(\theta)+2\pi$ 的光滑全局升映射。
因此 $|\widehat\gamma_t|=a$，完整材料圆周按原 $g$ 的同一半径归一。

令 $T=\widehat\gamma_t/a$，$b=|T_t|$，$(T,N_F,B_F)$ 为原曲线 Frenet 标架，
$c=(1-v^2/b^2)^{1/2}$。选 R137 已登记的正 $n$ 分支

$$
d=-\frac vbN_F+cB_F,\qquad N=d\times T=cN_F+\frac vbB_F,
\qquad n=\frac{bc}{a}>0,
$$

并由同一曲线导数定义 $m=d_t\cdot N/a$、$k=m/n$。
这完全决定入口位置与两个方向，不添加独立高度、标架或第二形式数据。

## 2. 整个平台的连续域与全周期回程

沿用 [R137](R137-flat-coast-ruling-two-jets-and-actual-inlet-consumer.md) 的准确公式；其详细原推导见
[flat-outlet ruling continuation](../notes/2026-11-09-db6f-flat-outlet-ruling-continuation-v1.md)。
设 $r_0=a/v$、$\Delta=x(2r_0+x)$，

$$
w=\frac{\Delta}{r_0+\sqrt{r_0^2+(1+k^2)\Delta}},\quad
A=r_0+(1+k^2)w,\quad
B=v(1+k^2)-k_t,\quad D=a+wB.
$$

有 $0\le w\le x\le L$。材料图及位置为

$$
U=t-\frac1v\operatorname{atan2}(kw,r_0+w),\quad
U_t=\frac D{vA},\qquad
Y(x,U)=\widehat\gamma(t)+w(d-kT).
$$

所有入口量 $2\pi$ 周期，且 $r_0+w>0$，故反正切无支路跳跃，
$U(t+2\pi)=U(t)+2\pi$。下列严格 $U_t>0$ 证明整个圆周的全局单值反解，
并非只在有限节点作 Newton 逆映射。
R137 恒等式于是给整个闭材料角域上的
$Y^*e=dx^2+(a+vx)^2dU^2$。

整数证书使用 R220 的 96-bit dyadic 向外舍入；有理数、平方根边界、Machin 公式的 $\pi$
与三角 Taylor 余项全部由整数运算形成包含区间。
本次新增的是适合新 Fourier 曲线的局部 Taylor 盒与自适应覆盖，不修改 R220 原证书身份。
对于第 $j$ 个中心 $\theta_j$、半宽 $h$ 和 $0\le r\le4$，逐坐标采用

$$
\gamma^{(r)}(I_j)\subset
\gamma^{(r)}(\theta_j)
 +[-h,h]\gamma^{(r+1)}(\theta_j)
 +[-1,1]\frac{h^2}{2}
 \sum_{k\ge1}k^{r+2}(|a_k|+|b_k|).
$$

中心导数也按有理 Fourier 系数及严格三角区间求值。
初始 2048 等角块中，不能证明 $D>1/2$ 或 $\Lambda<6$ 的块再二分，
最终 6838 叶、4790 次二分、最大深度 4 完整覆盖 $[0,2\pi]$。
二分只改善同一函数的包含盒，没有删除不利角段或改变输入曲线。

严格弧长余项独立处理。若 $J=|\gamma'|$，则
$|J''|\le|\gamma''|^2/\min J+|\gamma'''|$。
由初始整块盒得 $\min J>0.2046676$、$|J''|<46.879387$。
2048-panel 复合中点公式的平均积分误差不超过
$\|J''\|_\infty(\pi/2048)^2/6<1.838530\cdot10^{-5}$，故

$$
1.02416309<a_\gamma<1.02419987.
$$

这是用于连续几何的严格但较宽包含区间，不声称已经把 seam 浮点观察的求积误差验证至 $10^{-12}$。

每个叶块对 $\gamma,\gamma',\ldots,\gamma^{(4)}$ 用 R220 的曲率、挠率及导数公式，
再对完整 $w\in[0,L]$ 作包含运算。下列十进制界从准确整数区间保守向外取整，不把 binary64 display 的末位四舍五入当作证明端点。所得统一严格界为

| 量 | 连续域下界 | 连续域上界 |
|---|---:|---:|
| $b=|T_t|$ | 0.604472 | 2.821467 |
| 入口 $n$ | 0.566379 | 2.749846 |
| $|k|$ | 0 | 0.489080 |
| $D$ | 0.500627 | 2.557959 |
| $U_t$ | 0.477172 | 2.497564 |
| 非零主曲率 $\Lambda$ | 0.566379 | 5.628725 |
| 外向 support $-Y\cdot N$ | 0.783969 | 1.170167 |

其中 $\Lambda=a n(1+k^2)/D$。法向沿母线不变，且 $(d-kT)\cdot N=0$，
因此 support 的入口包含区间自动覆盖整条母线。
这支付整个平台的非退化、曲率与 support；单凭该局部 annulus 仍不支付未来全闭图的远点对 reach。

按 [R218](R218-flat-coast-green-operator-and-two-port-range.md)，
母线弧长小于 $0.158345029$，故法向 Green 估计可取

$$
C_0<0.022134600,\qquad C_{\text{ruling},1}<0.279574284,
\qquad C_{\text{ruling},2}<1.765601900.
$$

这些仍只控制沿母线方向。两端源矩、横向导数、切向 holonomy 和全局边界条件保留 R218 原限定。

## 3. 与原有限 ramp 的真正 C2 函数接合

记三档首 ramp 的有限 Cartesian 图为 $X(\sigma,\theta)$。
保持其共同中央材料 chart
$u_0(\theta)=a_{\gamma_0}^{-1}\int_0^\theta|\gamma_0'|$，
并将新精确 coast 写成 $Y(x,u_0(\theta))$。
在 $\sigma=R$ 定义三个**整个角函数**

$$
\Delta_j(\theta)=\partial_x^jY(0,u_0(\theta))-
\partial_\sigma^jX(R,\theta),\qquad j=0,1,2.
$$

不对 $\Delta_j$ 作角向重新插值。
R137 入口为 $Y=\widehat\gamma$、$Y_x=d$、$Y_{xx}=\ell N$，其中 $\ell=m^2/n$。
数值观察中所需完整角导数也来自同一曲线：

$$
N_{tt}=-a(m_t d+m d_t+n_tT+nT_t),\quad
\ell_t=2mm_t/n-m^2n_t/n^2,
$$

$$
\ell_{tt}=2(m_t^2+mm_{tt})/n-4mm_tn_t/n^2-m^2n_{tt}/n^2+2m^2n_t^2/n^3,
$$

$$
(\ell N)_t=\ell_tN+\ell N_t,\qquad
(\ell N)_{tt}=\ell_{tt}N+2\ell_tN_t+\ell N_{tt}.
$$

然后准确使用 $\partial_\theta=u_0'\partial_t$、
$\partial_{\theta\theta}=(u_0')^2\partial_{tt}+u_0''\partial_t$。

令 $h=R\eta$，$z=(\sigma-(R-h))/h$。
仅在最后完整多项式 ramp piece $[R-h,R]$ 加上

$$
\widetilde X=X+H_0(z)\Delta_0+H_1(z)\Delta_1+H_2(z)\Delta_2,
$$

$$
H_0=10z^3-15z^4+6z^5,\quad
H_1=h(-4z^3+7z^4-3z^5),\quad
H_2=h^2(z^3/2-z^4+z^5/2).
$$

这些基函数在左端的零至二阶物理径向导数全为零；右端的相应三条迹组成单位矩阵。
所以 $\widetilde X$ 与原 ramp 在左端真实 $C^2$，
与 $Y$ 在右端共享整个角函数的零至二阶径向迹，因而所有混合 Cartesian 两 jet 也相同。
中央反射及之前所有共享 Hermite 节点保持原定义。
这项接合是准确函数恒等式，不依赖表中小差值的数值大小。

对修正后的**实际位置函数**逐单元微分，重新计算全部 $E,F,G$ 和主曲率；
三档有限观察峰值为

| shape 级别 | ramp 单元 | 观察角点 / 每单元 Gauss | 接合后 metric 采样峰值 |
|---:|---:|---:|---:|
| M95 | 145 | 768 / 6 | 3.4686862105823146e-10 |
| M191 | 287 | 1536 / 8 | 4.314835056092037e-12 |
| M383 | 571 | 3072 / 8 | 3.6668767176161476e-12 |

M95 修正使峰值有所增大；后两档峰值不变，均出现在修正支持外。
三档曲率采样峰值仍约 $5.11272468$。
M191 的三条原始径向迹差的最大范数依次为
$9.02969\cdot10^{-15}$、$9.07911\cdot10^{-12}$、$9.88843\cdot10^{-10}$；
代码还使用它们的完整一、二阶角导数，没有把这些径向数值单独当作 C2 范数。

## 4. 复现、身份与剩余接口

本结果源码、实跑命令、原输入 hash、输出 receipt hash 和整数行流 hash 见
[R221 实际运行记录](../notes/2026-11-26-6a65-r221-c2-coast-runs.md)。
两份脚本为
[`6a65-m12-ramp-exact-coast-c2-glue.py`](../scripts/6a65-m12-ramp-exact-coast-c2-glue.py)
与 [`6a65-m12-ramp-coast-continuous-domain.py`](../scripts/6a65-m12-ramp-coast-continuous-domain.py)。

新的精确 coast 在整个平台成立，但其右端与后续原正曲率段的两 jet 尚未匹配。
后续位置 BVP 必须允许这一整条入口曲线变化；每次变化应重新消费准确 coast 并重新观察左侧接合，
不能把初始 Cauchy 数据锁死后用局部正曲率推进替代两端边值问题。
首 ramp 仍缺连续 metric 误差与无穷细化论证，平台后也尚有正曲率 ramp、down、bridge、尾端和闭合几何。
