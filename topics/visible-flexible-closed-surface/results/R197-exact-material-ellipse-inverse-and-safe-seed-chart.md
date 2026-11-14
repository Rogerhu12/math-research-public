# R197：保存椭圆的准确材料角反解与全域安全 seed 角图

**状态：已证明，当前真实保存轴已有完整 quarter 严格消费。** 本文沿 [R187](R187-closed-unit-angular-tangents-and-direct-position-metric.md) 的完整单位切向量，补其准确中央椭圆材料角和 seed 函数。它保持已经选择的实际轴长身份，不将有限 55 步轴搜索暗换成精确 gap 方程。真实计算不是新曲面 BVP。

## 1. 准确轴、准确周长与原反解

令 $A,B>0$ 是保存 binary64 轴长作为准确 dyadic 实数，

$$
\ell(\theta)=\sqrt{A^2\sin^2\theta+B^2\cos^2\theta},
\qquad Q=\frac{\pi}{2},
$$

$$
a_E=\frac{2}{\pi}\int_0^{Q}\ell(v)\,dv.
$$

准确目标中央半径 $a_0$ 仅在最终中央位置缩放时使用。当前定义的曲线为

$$
\gamma(u)=\frac1{a_E}(A\cos\theta(u),B\sin\theta(u)),
\qquad X_{\rm central}(u)=a_0\gamma(u).
\tag{1}
$$

材料角反解由

$$
\int_0^{\theta(u)}\ell(v)\,dv=a_Eu,\qquad 0\le u\le Q
\tag{2}
$$

唯一给出。因为 $\ell\ge b_-:=\min(A,B)>0$，积分严格增加；式(2)存在唯一解，满足

$$
\theta(0)=0,\qquad\theta(Q)=Q,\qquad
\theta_u=\frac{a_E}{\ell(\theta)}>0.
\tag{3}
$$

本题实际 $a_E$ 由已闭正项有理级数消费得到；其准确对象是同一保存轴的真实周长。有限程序的 Gauss8 累计和 Newton 终止条件不是式(2)的严格误差证明。本文给同一个准确反解的独立可计算区间入口，未改轴或归一化。

## 2. 归一 quarter 上的完整多项式微分系统

令 $t=u/Q$、$\nu=Qa_E$、$D=A^2-B^2$，并设

$$
s_\theta=\sin\theta,\qquad c_\theta=\cos\theta,\qquad
v=\ell(\theta)^{-1}.
$$

准确系统是

$$
\theta_t=\nu v,\qquad
(s_\theta)_t=\nu c_\theta v,\qquad
(c_\theta)_t=-\nu s_\theta v,
$$

$$
v_t=-\nu D\,s_\theta c_\theta v^4.
\tag{4}
$$

证明只需对 $\ell^2=B^2+D\sin^2\theta$ 微分：
$v_\theta=-D\sin\theta\cos\theta\,v^3$，再乘 $\theta_t=\nu v$。
所有右端均为有限多项式，没有材料角反解中的除零支。

每次新的径向场或角参数查询无需重建这个图。$A,B,a_E$ 固定以后，式(4)与曲面径向参数无关。

## 3. 逐格严格 Taylor 累计

设一个归一角单元为 $[t_j,t_{j+1}]$，其左端准确 $\theta(t_j)$ 已由区间 $I_j$ 包围。由式(3)的全局正速度界，

$$
0<\theta_t\le\frac{\nu}{b_-}.
$$

因此整个单元的真实 $\theta$ 位于

$$
J_j=
\left[\inf I_j,\ \sup I_j+
\left(\frac{\nu}{b_-}\right)^+(t_{j+1}-t_j)\right]
\cap[0,Q^+].
\tag{5}
$$

该先验包来自真实全局速度与准确 quarter 单调性，不依赖待验证数值解。这里 $(\cdot)^+$ 表示严格上界。

对式(4)作普通带 factorial 的 Taylor 系数运算。若

$$
\theta=\sum_k\theta_kh^k,\quad
s_\theta=\sum_ks_kh^k,\quad
c_\theta=\sum_kc_kh^k,\quad
v=\sum_kv_kh^k,
$$

则

$$
(k+1)\theta_{k+1}=\nu v_k,
$$

$$
(k+1)s_{k+1}=\nu(c_\theta v)_k,\qquad
(k+1)c_{k+1}=-\nu(s_\theta v)_k,
$$

$$
(k+1)v_{k+1}=-\nu D(s_\theta c_\theta v^4)_k.
\tag{6}
$$

右边是准确有限卷积，所需系数阶数不超过 $k$。区间初值由真实
$\sin I_j,\cos I_j,(B^2+D\sin^2 I_j)^{-1/2}$ 给出；
速度平方还可以与准确范围 $[b_-^2,b_+^2]$ 相交。

在左端 $I_j$ 上计算至 $N-1$ 阶；再把初始 $\theta$ 换为整个先验包 $J_j$，计算式(6)的第 $N$ 阶系数区间。后者包含该单元任一点的真实 $N$ 阶导数除以 $N!$。由实变量 Taylor 定理，对 $0\le h\le t_{j+1}-t_j$，

$$
\theta(t_j+h)\in
\sum_{k=0}^{N-1}[\theta_k]h^k+
[\theta_N]_{\rm whole}h^N.
\tag{7}
$$

$s_\theta,c_\theta,v$ 同理。因此式(7)给下一端点的严格区间并归纳覆盖整个 quarter。全部区间运算和平方根向外包围，有限浮点级差没有作为余项使用。

最后端点可以与准确恒等式 $\theta(1)=Q$ 相交，因为式(2)与准确 $a_E$ 的定义已证明这一点。它不是用期望边界替代一个未满足的数值 ODE 条件。如果两个包围不相交，消费者应拒绝其计算；不能选择忽略失败。

任意查询点由所在单元的同一式(7)消费。任意子盒 $[l,r]$ 可利用准确单调性，将两个端点包围合为
$[\theta(l)^-,\theta(r)^+]$。这不是在离散节点之间假设线性插值。

## 4. 完整材料角 jet

归一 $t$ 的 Taylor 系数转为物理材料 $u$ 的系数时，准确乘 $Q^{-k}$。输出约定是

$$
\text{第 }k\text{ 项}=\frac1{k!}\partial_u^k f.
$$

这一区分在下游 R188 primitive 中必须保留，不能把归一角系数当物理角导数。

令

$$
\mathbf v(u)=(-A\sin\theta\,v,\ B\cos\theta\,v),\qquad
J(x,y)=(-y,x),
$$

$$
b(u)=a_EABv^3,\qquad
b_u=-3a_E^2AB(A^2-B^2)\sin\theta\cos\theta\,v^6.
\tag{8}
$$

直接微分式(1)–(3)得到

$$
\gamma_u=\mathbf v,\quad |\mathbf v|=1,\quad
\mathbf v_u=bJ\mathbf v,\quad
\mathbf v_{uu}=b_uJ\mathbf v-b^2\mathbf v.
\tag{9}
$$

这些是整条准确材料曲线的真实 jet，并非有限 DFT 导数。

精确椭圆对称性给

$$
\theta(-u)=-\theta(u),\quad
\theta(\pi-u)=\pi-\theta(u),\quad
\theta(u+\pi)=\theta(u)+\pi.
\tag{10}
$$

例如对速度的对称性作变量替换，式(2)两边相同；再用唯一性即得。故 quarter 图及其相应反射导数准确延拓整圈，不需要再独立积分其他三个 quarter。

## 5. seed 的全域安全角图

令 $\mathbf e(u)=(-\sin u,\cos u)$。在 $0\le u\le Q$，
$\theta(u)\in[0,Q]$，所以 $\mathbf e,\mathbf v$ 都在同一闭象限。于是

$$
c_\delta:=\mathbf e\cdot\mathbf v\ge0,\qquad
s_\delta:=e_xv_y-e_yv_x,
\quad c_\delta^2+s_\delta^2=1.
\tag{11}
$$

有唯一连续 $\delta\in[-\pi/2,\pi/2]$ 满足
$\mathbf v=R_\delta\mathbf e$，但严格消费者不必调用 atan2。
定义

$$
H(u)=\frac{s_\delta}{\sqrt{(1+c_\delta)/2}}.
\tag{12}
$$

分母至少 $1/\sqrt2$，且式(12)准确等于 $2\sin(\delta/2)$，符号完整保留。由 $\delta_u=b-1$、$\delta_{uu}=b_u$，

$$
H_u=\sqrt{\frac{1+c_\delta}{2}}\,(b-1),
$$

$$
H_{uu}=-\frac H4(b-1)^2+
\sqrt{\frac{1+c_\delta}{2}}\,b_u.
\tag{13}
$$

式(10)给 $H$ 的正确奇对称与 $\pi$ 周期性。quarter 两端 $\delta=H=H_{uu}=0$，$H_u$ 不必为零；消费者不错误删除该导数。

取 R187 的准确径向权 $q(s),r(s)$，它们满足

$$
0\le q\le1,\qquad r^2=q(1-q).
$$

原完整 seed 为

$$
T_*=\bigl((1-q)\mathbf e+q\mathbf v,\ rH\bigr).
\tag{14}
$$

由 $H^2=2(1-c_\delta)$，

$$
|T_*|^2=1,\qquad
R^2:=|T_{*,h}|^2
=1-2q(1-q)(1-c_\delta)
\ge\frac{1+c_\delta}{2}\ge\frac12.
\tag{15}
$$

因此原 seed 的水平角图全域有固定正下界，与曲率正负、有限求解残差、半径设计变量无关。这个结论来自完整函数，不是检查若干角点所得。

这里的 $R$ 是 seed 水平范数，不是新增半径样条的步长或曲面 reach。

## 6. 完整角修改的无反三角表达

令 $P(s,u),W(s,u)$ 是 R187/R190 的两个完整角修正，包括所有实际有限系数，仍按原定义的奇对称与 $\pi$ 周期条件。定义

$$
\begin{aligned}
T_h&=R_P T_{*,h}
\left(\cos W-\frac{T_{*,z}}R\sin W\right),\\
T_z&=T_{*,z}\cos W+R\sin W.
\end{aligned}
\tag{16}
$$

这是原程序
$(\Theta_*,\Phi_*)\mapsto(\Theta_*+P,\Phi_*+W)$ 的同一个完整实函数。证明是写
$T_{*,h}=R(-\sin\Theta_*,\cos\Theta_*)$、
$T_{*,z}=\sin\Phi_*$、$R=\cos\Phi_*>0$，
再使用角加法公式。

式(16)只除 $R\ge1/\sqrt2$，所以没有 atan2/asin 分支，也不除修改后的 $\cos(\Phi_*+W)$。后者允许为零；不能把它的正性新增成曲面存在或求解的门。实际 immersion 仍由 R193/R194 的 Gram 条件支付。

式(16)保持准确 $|T|=1$。若 $P,W$ 的径向系数为 C²，它与 $q,r$ 一样给出 C² 的实际 $T$；高阶角导数可由完整函数微分，不要求径向 C³。R188 所需 $T,T_s,T_{ss}$ 及全部参数/mixed 列可在这一同函数表达上通过真实链式微分构造，不准先将非线性结果截断回有限 Fourier 模。

这条等价性是实函数恒等式；改用式(16)重新排列有限浮点运算时，其舍入误差或主离散目标的读数仍须如实另记，不能宣称两个程序逐位相同。

## 7. 与 R188、R193、R194 的明确接口

实际源
scripts/fd2d_R197_saved_ellipse_material_chart.cjs，
10092 B，SHA256 3ccca82923ac0ed4cebcd66cc912944e41565d8e27567e0bd08f684a029ff79f，
提供 createR197SavedEllipseChart(spec,arithmetic)。

其输入必须是同轴的已证 R187 saved-axis perimeter certificate。当前实际使用冻结 R188 arithmetic 源 SHA256
5c04a135eed859a6d6d583877e53681cdc1dddc6102c913152adfc1913a9f97e。
它使用准确有理数和向外 dyadic 区间，π 包来自已证明 Machin 余项；平方根亦由整数平方根向外夹取。

主要方法：

- thetaPoint / thetaBox：归一 quarter 查询，返回准确材料角反解包围；
- materialJetBox：$\theta,\sin\theta,\cos\theta,\ell^{-1}$ 的完整物理材料角 Taylor 系数；
- geometricSeedBox：$\gamma,\mathbf v,\mathbf v_u,\mathbf v_{uu},H,H_u,H_{uu}$ 和 safe-chart 下界；
- portablePackets：本次真实全部 cell 的 Taylor 系数与 whole-cell 余项。

后续 R188 full-channel producer 应消费这里的准确函数与完整导数，结合实际径向 $q,r,P,W$ 和全部参数列。当前源尚未生成某个完整曲面状态的所有 nonlinear $T_s,T_{ss}$ primitive 盒，因此不能把这些后续输入填写为已付。

R193 的中央 ellipse 误差入口可由这些准确盒与同物理点/盒的参考函数比较取得。有限 Newton point 的误差若只在一个点包围，不能扩充为全角程序误差。R194 则在完整实际位置 jet/Gram/form 包就绪后消费。

## 8. 当前真实完成状态

本次输入确实是当前已保存的小幅 seed：

$$
A\text{ bits}=0x3ff0767c5c4cf6bc,\qquad
B\text{ bits}=0x3fef535f1f0053de.
$$

其准确 $a_E$ 来自
notes/2026-11-12-fd2d-metric-R187-saved-ellipse-normalization-01-report.json，
SHA256 8c2f37b42187712e5cb20cc24e7b862d5b71b8b4c20224738837ab84b23717c6。
没有重新运行轴搜索。

真实 functions cell g2:46 已完整返回，643.853 秒；32 个完整 quarter 单元、16 阶、160 位向外区间。每个单元都按式(5)–(7)完成。最大节点 $\theta$ 包宽为准确有理数

$$
\frac{245057301338398166056725}
 {1461501637330902918203684832716283019655932542976}
<1.677\cdot10^{-25}.
$$

七个选定点、物理角两 jet 和归一角区间 $[7/30,1/4]$ 的完整 geometric seed 盒也实际返回。例子 $u=\pi/4$ 的 $\theta$ 显示约 .7978402686697263，$H$ 显示约 .03731388834277425；严格有理端点在报告，不以显示小数代替。

报告
notes/2026-11-12-fd2d-metric-R197-saved-ellipse-material-chart-01-report.json，
85146 B，SHA256 bd9c9af847fbd0821d3011a00444d4f1d7f96027ef2179e4a5a8d91d378f22af。
它只删除了重复拷贝的 definition 并用同文件引用替代；实际数值字段不变。首次保存后仅缩进从两空格变一空格，使文本明显小于 100 KB。

原重复 report 为 120596 B/SHA256
05718d4f2ac8456919acfe58ed3ad8c70560087d47babe29b3fcb7c0e5ff87ac。
完整 portable 32-cell packets 为 879135 B/SHA256
39aad4ebdbc35fe843eef7df35bbd3f9a29450f1fb2bd6d1d547a98a1771f65f，
当前保留在实际 V8 store；执行环境失联期间没有将大包编码或拆件经小文本 API 上传。它们可由已保存完整源和准确输入重新生成，恢复终端后优先核原实体/保存已有 store。

本次没有 OS 子进程，所以不补填 OS exit。它准确支付这条当前中央 saved-axis 曲线的材料角图与上述 seed 盒；尚不构成当前主曲面的全域等距、曲率、reach 或闭帽完成证书。
