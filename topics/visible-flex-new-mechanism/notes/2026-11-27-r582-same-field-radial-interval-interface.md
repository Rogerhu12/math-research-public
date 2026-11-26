# R582 当前 97q 的同一连续材料场与径向区间接口

2026-11-27，Astra-new-mechanism-1f4a61a4-20261127。新源码接口和原式纸核；没有在本地执行科学，没有新全域数值证书，也没有重跑旧 ODE 或细网。对应源码为 [r582_same_field_radial_intervals_20261127.py](../scripts/r582_same_field_radial_intervals_20261127.py)。

## 1. 精确区分当前场与生成它的 ODE

当前 `r582_physical_epigraph_continuation_20261127.py` 的 `ResonantField` 继承 `StableField`，没有另换空间材料函数。实际链条是：

1. `PaidDenseTail` 用已付 mouth/inner 输入做新的 dense outward transfer；`core_forward` 和 `tail_backward` 生成中段端点。`.78` 到 `.80` 的两 jet blend 也只参与端点生成。
2. `material_knots` 和每个端点共同的 `(A,A_s,A_ss,C,C_s,C_ss)` 六个 binary64 数定义**同一条分片 quintic Hermite C² 样条**。
3. 任意点材料查询调用 `residual_hermite`。它的所有导数来自上述同一个多项式，不再调用 dense ODE 的值并另配 formal ODE 导数。
4. 用同一个冻结圆参考半径 `a_ref` 作商，得到

   \[
   U=\frac{3A}{2a_{\rm ref}}-(1-\chi_{\rm bg})\frac3{4r_{\rm ref}},
   \qquad V=-\frac{2C}{a_{\rm ref}},\qquad r_{\rm ref}=.38.
   \]

   `RadiusOnlyField` 的半径公式使用原 `SOURCE_Q[64:72]`、原 compact bump 和原固定 `mu`，不是当前有限 q 的半径；避免高度积分没有改商函数。

5. 加原 64 个角 B-spline 坐标和 16 个局部 tail 坐标。若 `beta=4 chi(1-chi)`，`P^u_m,P^v_m` 是原八系数五次 B-spline，`epsilon=p-.18`，则完整径向系数为

   \[
   u_m=\beta P^u_m+\epsilon U
       \left({\bf1}_{m=2}+\sum_{j=0}^3d^u_{jm}\chi_j\right),
   \quad
   v_m=\beta P^v_m+\epsilon V
       \left({\bf1}_{m=2}+\sum_{j=0}^3d^v_{jm}\chi_j\right),
   \]

   其中 `m=2,4,6,8`，只有 `m=2,4` 有 `d` 列；四个开启区间仍为 `(.78,.82),(.82,.84),(.84,.86),(.86,.88)`。于是

   \[
   u(s,\theta)=(1-\chi_{\rm bg}(s))u_{\rm core}(\theta)
      +\sum_m u_m(s)\sin(m\theta),\qquad
   v(s,\theta)=\sum_m v_m(s)\sin(m\theta).
   \]

该分组是原式恒等变形，保留每个原坐标。先将 `1+sum(d_j chi_j)` 合并再取区间，可以保留实际三个约 `-1/3` 的 mode-2 tail 系数造成的抵消；分别取绝对值再相加会无谓丢掉该抵消。此处没有把抵消大小或当前 q 的连续范数宣称为已经认证。

## 2. 同一 quintic 的严格、可实施包络

对原材料单元 `[s_i,s_{i+1}]`，令 `h=s_{i+1}-s_i`，两端 jets 为 `(v_0,d_0,e_0)`、`(v_1,d_1,e_1)`。把原 binary64 数解释为它们**精确的二进制有理值**。这不是对 ODE 真解的区间假设，而是原有限材料样条的系数定义。

原 quintic 在归一变量 `t=(s-s_i)/h` 的六个 Bernstein 控制点准确为

\[
\begin{split}
b_0&=v_0,\quad b_1=v_0+hd_0/5,\quad
b_2=v_0+2hd_0/5+h^2e_0/20,\\
b_3&=v_1-2hd_1/5+h^2e_1/20,\quad
b_4=v_1-hd_1/5,\quad b_5=v_1.
\end{split}
\]

这是原 endpoint Hermite 多项式：六个端点条件直接代入 Bernstein 端点导数式即可核对，而次数不超过五的这六条件唯一决定多项式。真实 s 导数的 Bernstein 控制点依次为

\[
b^{(1)}_j=5(b_{j+1}-b_j)/h,\qquad
b^{(2)}_j=4(b^{(1)}_{j+1}-b^{(1)}_j)/h.
\]

新接口用 `Fraction` 完整构造这些有理数；如需单元子区间，用精确 de Casteljau 限制。各阶多项式的值落在相应控制点的凸包中。**直到最后**才将有理端点转为 binary64，并以精确有理比较决定是否需要 `nextafter` 向外移动。因而没有“先给巨大独立值项一个浮点误差，再除以 h²”的新误差。

`ExactEndpointHermite(field, expected_mesh_sha256, backend)` 直接读取本次 Actions 内已构造的 `field.material_knots` 与 `field.material_endpoint_jets`，按原数组顺序重新核对 `knots || endpoint_jets` 的 binary64 SHA256，并与实际 `field.material_mesh_sha256` 同时核对。它不调用 `field.evaluate`、dense 输出或 ODE。端点不是旧日志中只有一个 SHA 时可以凭空恢复的数据；若进程里已无端点，必要的新场构造须另计新费用，仍要求 hash 认同一场。

`SameFieldRadialDesign` 再核实际 97q 的 binary64 SHA，使用 R611 v2 的有向区间基础运算、原 spline 递归和 flat-step 两 jets。商、各 gate 乘积、原 beta 列均使用同一函数的乘积/商法则。`coefficients(a,b)` 返回所有原 mode 的连续值、一阶和二阶径向包络；`angular_box(a,b,core_u,core_utheta,core_uthetatheta)` 给整个角圈的 u/v、s、ss、theta、s-theta，若传入 core 第二角导则也给 theta-theta。

最后一个接口要求 core 三个角界来自**同一个 rounded ellipse、同一个归一弧长角**，不能使用有限 `brentq` 样本或另拟合正弦。给 root 的 R604 `Jet` 可以直接取 `value,s,ss,theta` 四项。R504 的完整连续 primitive 范数与真实空间 jets、R514 的同一控制场两 jet 规则可以直接复用，无须重证或把有限 FFT 原函数当作连续原函数。

### 2.1 同一 rounded core 的显式全角输入

源码同时提供 `rounded_core_angular_boxes(p,q,offset)`，从原精确半轴和 offset 直接给出所需角界；没有另求数值反弧长。以下用 `d` 表示 offset，避免与参考半径混淆。

以外法向角 `phi` 参数化原 ellipse，令

\[
h(\phi)=\sqrt{p^2\cos^2\phi+q^2\sin^2\phi},\quad
\rho(\phi)=d+\frac{p^2q^2}{h(\phi)^3},\quad
a_0=d+\frac1{2\pi}\int_0^{2\pi}h(\phi)\,d\phi.
\]

`rho=h+h''+d` 给出最后一个周长公式。平方根的弦下界及 Jensen 上界给

\[
d+\frac{p+q}{2}\le a_0\le d+\sqrt{\frac{p^2+q^2}{2}},\qquad
d+\frac{q^2}{p}\le\rho\le d+\frac{p^2}{q}.
\]

原归一角满足 `theta(phi)=a0^{-1} integral_0^phi rho`，所以

\[
u_{\rm core}=\phi-\theta,\quad
(u_{\rm core})_\theta=\frac{a_0}{\rho}-1,\quad
(u_{\rm core})_{\theta\theta}=-\frac{a_0^2\rho_\phi}{\rho^3},\qquad
|\rho_\phi|\le\frac{3p^2(p^2-q^2)}{2q^3}.
\]

最后一个界直接来自 `h_phi=-(p²-q²)sin(phi)cos(phi)/h`、`h>=q`，因而涵盖全部角。

为避免以整个 rho 范围估计 `u_core` 太松，取 `x=(p²-q²)/q²>=0`。对 `y>=0`，Taylor 积分余项给

\[
(1+y)^{-3/2}=1-\frac32y+R(y),\qquad 0\le R(y)\le\frac{15}{8}y^2.
\]

于是同一 rho 可写为

\[
\rho=d+q+\frac{qx}{4}-\frac{3qx}{4}\cos(2\phi)+E(\phi),\qquad
-\frac32qx^2\le E\le\frac{15}{8}q(1+x)x^2.
\]

各长 `pi/2` 的角区间中，E 的平均相同。这由 E 仅依赖 `cos²(phi)` 的周期和反射对称直接给出。对任意区间长度 `ell` 和 `E in [a,b]`，减去同区间平均后的原函数满足

\[
\left|\int_0^t(E-\overline E)\right|
\le (b-a)\frac{t(\ell-t)}{\ell}\le(b-a)\frac{\ell}{4}.
\]

将 cos 项准确积分，并用每个象限的零端点重置该估计，得到整个角圈上的显式界

\[
|u_{\rm core}|
\le \frac{\frac38qx+\frac\pi8
   \left(\frac32qx^2+\frac{15}{8}q(1+x)x^2\right)}
 {d+(p+q)/2}.
\]

源码用准确有理上界 `pi/8<11/28`，而 x 和 `p²-q²` 先从原 binary64 参数的精确有理值形成。所有商和平方根均在原有向区间接口内求值。该界是原 rounded ellipse 的连续恒等/不等式，不需要 `brentq` 样本误差，也没有假设 `u_core` 本身恰好只有 mode 2。

## 3. 开 core、零 suffix 和真帽分别是什么

在 `[0,C]`，原端点场准确为 `A=1/2,C=0` 及零一二导，参考半径为同一 `r_ref=.38`；商与 core 补偿准确相消，`U=V=0`。原 beta 和四个 tail gates 也恒零。因此完整角场正是原 rounded-core `u_core`、`v=0`，没有微小非圆 seed 留在核心上。中间柱和上下 core 以原 z 直线拼接。

这里的准确相消指源文件声明的**实数公式**。例如 `3/(4*r_ref)` 进入区间后才除，不把 ordinary Python 预先舍入的一个商悄悄宣布为新精确常数。将逐点浮点程序本身视为 C² 实函数没有意义；需要的数学对象是源文件已声明的实数场。若要把某条 ordinary 数组上通过的门移交给该实数场，还必须包住普通求值误差。本接口直接给实数场重新作严格观察，未继承有限门为严格结论。

数值 seed 确有零 suffix，但其实际起点不能只用打印的 `alpha160` 代替：`u >= alpha` 的判定、u-to-s 舍入和各 jet underflow 都进入最终端点数组。新接口从该**实际数组**向左找所有六 jet 都为零的公共端点后缀。两端六 jets 为零的 Hermite 单元恒零，得到准确的材料零后缀；还需取它与实际背景终点的较大值，才能宣称 `U,V` 都恒零。

这不把**完整**非圆输入改成固定圆环：原 beta-B-spline 列在每个 `C<s<L` 仍可活动；固定解析高度尾 `w,H` 也保留至真实帽边。原 `cap_collar_width=0`，没有新建正宽度冻结环带。只有在 `s=L`，beta 及其全部 jets 平坦消失，材料 seed 已在其零 suffix，背景已为尾；实际接缝的 jets 为

\[
u=v=u_s=v_s=u_{ss}=v_{ss}=0,\quad
a=r_c,\ a_s=-1,\ a_{ss}=0,\quad
z=H_q,\ z_s=z_{ss}=0.
\]

因而原开圆盘 `r<r_c=.22`、`z=H_q` 的拼接保持。C² 材料场中段只要求共享两 jets；无需假称所有 material knots 上 C∞。下半面按原镜像，中心柱和两盘均须作为闭面的实际部分计入 R604 全域范数。

`L-.08` 是实际背景终点表达式，tail gate 的 `.82` 则是原文字面常数；它们不得按显示小数或 `1e-13` 材料建网容差合并。`initial_partition()` 取原材料 knots 与全部命名接口的逐值并集。这个证明细分不改变原材料插值网。

## 4. 哪些误差已被绕开，哪些仍必须支付

| 要证明的对象 | 当前可直接使用的输入 | 仍须支付的部分 |
|---|---|---|
| 此次实际端点定义的有限 C² 材料场 | 完整端点数组、mesh SHA、实际 q；精确 Bernstein 包络 | 新的全径向区间覆盖与 core 全角界；不能把接口源码本身算作数值通过 |
| 同一有限完整位置映射 | 原精确连续 T、零均值 primitive、原精确 a/z 公式 | 精确高度积分及全角/全径向的组合范数；复用 R611 的同一解析高度证书时仍核系数与定义 |
| 把旧 finite FFT/ordinary 门转为该连续映射的严格门 | 旧门只作有限观察 | FFT 离散化、ordinary 浮点、椭圆反弧长及高度求积误差，或直接重新对精确函数作严格包络 |
| 将材料 quintic 识别为无限 flat ODE 核 | 只有生成来源关系，尚无相等或 C² 距离证书 | finite DtN 与 inner 尾、数值 ODE、端点 jets、插值、blend defect、underflow 与人为数值零 suffix 的统一 C² 误差 |
| 固定 g 的精确有限等距族或 README 完成标准 | 本接口没有给出 | 原完整 metric 方程、固定 g 连续族、宏观幅度和全部几何完成门 |

因此有限场自身的严格几何不需要先偿还“它等于无限核”这一不必要等同；但要引用无限核的定理、线性核身份或固定 g 的精确求解，不能把这些未付误差写成零。后续同一 Actions driver 应在完整径向覆盖完成后，将各 `angular_box` 和当前/参考 a/z 区间交给 root 的 `r604_rotating_frame_continuous_norms_20261127.py`，包括中心柱与帽，才形成全闭面 C⁰/C¹/C² 结论。

本次本地验证仅为 Python AST 和五条源码 hash 绑定；没有执行该模块或任何 interval/ODE/优化科学。
