# 实际 small01 场的连续 R125 primitive 消费者

本记录证明 `fd2d-metric-gc-primitive-continuous.py` 和
`fd2d_gc_interval_models.py` 的区间消费规则。物理对象是已保存的原生 C¹ 三次场，加 `exact-profile-02.packet.json.gz` 所定义的准确物理目标／逐段 C² clock；旧浮点 body 读数不进入此证明。消费者不求 BVP、物理 frame ODE 或 tail。

## 1. 准确定义与分子恒等式

原生场 \(\eta(x,\xi),\zeta(x,\xi)\) 的每个 Fourier 系数由同一组保存 binary64 节点、值、真 first-x jets 作共享三次 Hermite 插值。角基是 \(\cos(2j\xi),\sin(2j\xi)\)，无 \(\sqrt2\) 系数。

令 \(s=S(x)\)，\(J=S_x>0\)，\(U=\xi+b(x)V(\xi)\)，其中 \(b=1-\beta\)、\(V=U_*(\xi)-\xi\)。记

\[
q=U_\xi=1+b d,\quad d=U_*'-1,\quad U_x=b_xV,
\quad v^2=1-a_s^2>0.
\]

全部 a、a_s、a_ss 均指**物理 s 导数**；eta_x、zeta_x 是固定 ξ 的计算 x 导数。物理字段准确为

\[
n=(v/a)e^\eta,\quad m=(v/a)\zeta,
\quad l=\frac{v^2\zeta^2-a a_{ss}}{a v e^\eta}.
\]

这使 Gauss 方程 \(nl-m^2=-a_{ss}/a\) 准确成立；不是把有限指数 Fourier 截断当作实际 n。关于角变量，准确 n 仍有完整指数。

沿用已闭 `log_codazzi_numerators` 的代数恒等式，定义

\[
\begin{aligned}
P_n={}&a q v^2\eta_x-a v^2U_x\eta_\xi-Jv^2e^{-\eta}\zeta_\xi\\
&-Ja_s q\{v^2e^{-2\eta}\zeta^2-a a_{ss}(e^{-2\eta}-1)\},\\
P_m={}&a qv^2\zeta_x-a v^2U_x\zeta_\xi\\
&-Je^{-\eta}\{2v^2\zeta\zeta_\xi-(v^2\zeta^2-a a_{ss})\eta_\xi\}\\
&+Ja_s q(v^2-a a_{ss})\zeta.
\end{aligned}
\]

则 \(\mathcal R_n=e^\eta P_n/(Ja^2qv)\)、
\(\mathcal R_m=P_m/(Ja^2qv)\)。R125 的准确反对称连接残差
\(\widehat H=JH\) 对应三维向量

\[
\widehat h=\frac{1}{q}\left(-\frac{e^\eta P_n}{av},\frac{P_m}{av},0\right)
=\frac{N}{q}.
\tag{1}
\]

所有 P_n、P_m 项先在有限 Fourier／径向系数层合并相减，再取范数，保留背景和配点间的真实相消。

## 2. 多项式模型及误差算术

每个解析径向支段映射到 \(z\in[-1,1]\)。一个模型是

\[
f(z,\xi)=p(z,\xi)+r(z,\xi),\qquad |r|\le e,
\]

其中 p 是有限径向幂／Fourier 多项式，全部系数由区间包围。每个真实系数指输入准确数据和下面代数公式所产生的值；区间本身不作为多值的物理场定义。

模型乘法用

\[
|fg-pq|\le \|p\|_1 e_g+\|q\|_1e_f+e_fe_g
\]

传播已有误差，\(\|p\|_1\) 取全部系数绝对和，因 \(|z|\le1\) 和每个复指数模为 1 而有效。径向次数超过 16 的系数移入误差时，支付其完整绝对和。辅助多项式外侧 Fourier 系数也允许对称缩短，**每个移出的系数仍完整计入误差**；每次缩短的选择阈值只是代码中的准确 binary64 `1e-22`，实际支付的是已经外包的系数和。实际原生字段没有被删除模态或改成新的字段。

原生 Hermite 系数及其 affine restriction 先用 `Fraction` 准确计算，然后向 binary64 区间外包。目标的 sin/cos／半径系数和显式余项由 `exact-profile-02` 提供。将这些多项式复合准确 clock 并限制到小段时，所有模型截断和已有余项继续支付；独立包围 a、a_s、a_ss，不把某个近似多项式的导数冒充准确目标的导数。

对原生指数使用 8 阶 Taylor 多项式。当 \(|\eta|\le r<1\) 时，余项严格不超过

\[
\frac{r^9}{9!(1-r)}.
\]

负 eta 与 `-2 eta` 使用各自完整的 r，`exp(-2 eta)-1` 从无常数项的式子构造。实际指数没有被重定义。对于正的纯径向 a 与 v²，在一个正的准确 binary64 中心 c 展开其倒数或逆平方根，令 \(w=f/c-1\)。当模型已证 \(|w|\le r<0.8\) 时，采用 24 阶几何／二项式级数；因为逆平方根的系数绝对值 \(\binom{2k}{k}/4^k\le1\)，两者尾项均可用
\(r^{25}/(1-r)\) 包围，再乘相应的 c 归一化。未证该范围时只细分计算盒，不改物理参数或字段。

## 3. 准确角 chart 和共用角分母

已闭 512 模准确均值区间及 `balanced-chart-fourier-tail-01` 包围准确 U_* 与前四导的完整余项。消费者用前 160 个区间的**准确有理中点**构造辅助有限函数

\[
d_M=2\sum_{j=1}^{160}\mu_j^{mid}\cos2j\xi,
\qquad V_M=\sum_{j=1}^{160}(\mu_j^{mid}/j)\sin2j\xi.
\]

被省略的第 161 至 512 项支付准确有理系数绝对和，再加原包的全部“中点代表误差＋无限尾”预算。故 \(|d-d_M|\le\epsilon_d\)、\(|V-V_M|\le\epsilon_V\) 是完整连续界，并非新的有限 chart 定义。

在**整个原生单元** \([x_0,x_1]\) 固定
\(b_0=b((x_0+x_1)/2)\)，该值是准确有理数。令

\[
q_0(\xi)=1+b_0d_M(\xi),\quad \delta b=b-b_0,
\quad C_j(\xi)=\frac{(-d_M)^j}{q_0^{j+1}}.
\]

q_0 的正性由覆盖全角的区间弧证明。相同 q_0、C_j 用于该原生单元内的所有解析分片。

由 (1) 的系数合并得到 N 的模型 \(N=P_N+R_N\)。在每个解析小段上构造

\[
P=\sum_{j=0}^{5} P_j(z,\xi)C_j(\xi),
\]

其中 \(P_j\) 是 \(P_N(\delta b)^j\) 的有限模型多项式部分，相关乘积截断误差单独保留。P 是辅助的有限径向多项式、光滑角有理函数；它不是实际的 H 或 n/m。

设 \(q_a=q_0+\delta b\,d_M\)。有限几何恒等式准确给出

\[
\frac1{q_a}-\sum_{j=0}^{5}\frac{(-\delta b d_M)^j}{q_0^{j+1}}
=\frac{(-\delta b d_M)^6}{q_0^6q_a}.
\]

该有限等式不需要假装分母恒定，也不依赖一个未支付的无穷级数。若 δb 模型也带有误差，将其乘 \(|d_M|\) 计入 \(\epsilon_q\)；并将 \(|b|\epsilon_d\) 计入。因此每一向量分量的完整余项可取

\[
\begin{aligned}
|\widehat h-P|\le{}&e_N/q_{\min}
 +|P_N|\epsilon_q/(q_{\min}q_{a,\min})\\
&+\frac{|P_N|}{q_{a,\min}}
  \left|\frac{\delta b d_M}{q_0}\right|^6
 +\sum_{j=0}^{5}e_j|C_j|.
\end{aligned}
\tag{2}
\]

消费者逐弧、逐径向盒支付 (2)，并实际核 q 与 q_a 为正。

## 4. 原生单元共用均值、连续 primitive

各解析小段可使用不同的局部 z 多项式，但 C_j 在整个原生单元相同。因此各 \(P_j\) 的完整单元积分能在 Fourier 系数层相加，再除原生单元宽得到准确均值。采用

\[
\overline P=(x_1-x_0)^{-1}\int_{x_0}^{x_1}P\,dx,
\qquad Q(x,\xi)=\int_{x_0}^x(P-\overline P)\,dx.
\tag{3}
\]

单项式积分准确使用 \(\int_{-1}^1z^{2k}dz=2/(2k+1)\)。每段 Q 包含前面所有小段的积分和、当前小段 primitive，并减去从**原生单元左端**累计距离乘共用均值。于是 Q 在内部接缝连续，在原生单元两端准确为零；不因 phase 分支而重置 Q。

准确内部 phase 根仅被夹在极小有理区间。其上采用 P=0，直接用安全物理 jet 包围真实 H；该段余项可较大，但只按其真实约 `4e-35` 宽度积分。不把根夹区间丢掉，也不将其中点冒充准确根。

**R125 的绝对连续版本。** (3) 所得 Q 对 x 连续、分片 C¹、整体绝对连续，关于 ξ 光滑。P 允许在有限个内部界面跳变，但 Q 不跳变。R125 的恒等式对几乎每个 x 成立；将每片恒等式积分后，接口的 FQ 项因 Q 连续准确抵消，所以同一个变常数公式及全部积分后验继续成立。无需增加实际物理图的正则性门，也不要求 Q 跨内部界面 C¹。

在固定材料 u 的特征线上，\(\partial_x|_u=\partial_x-w\partial_\xi\)、\(w=U_x/q\)。故残差是

\[
E=\overline P+(\widehat H-P)+wQ_\xi+[Q,\widehat A].
\tag{4}
\]

Q_ξ 对辅助函数精确求导；角 Fourier 频率是 **2j**。另外

\[
C_j'=-\frac{j(-d_M)^{j-1}d_M'}{q_0^{j+1}}
 -\frac{(j+1)(-d_M)^j b_0d_M'}{q_0^{j+2}},
\]

首项在 j=0 时省去。分母不通过除 d_M 求导，因此 d_M=0 的角也无奇性。

## 5. 连续角范围与外包算术

z 幂系数直接转为 `[0,1]` Bernstein 系数。所用准确矩阵第 (r,j) 项是

\[
\sum_{k\le\min(r,j)}
\binom jk(-1)^{j-k}2^k\binom rk/\binom Dk,
\]

即 \((2t-1)^j\) 的 D 次 Bernstein 系数。矩阵先用有理数求和，再外包。取每个 Fourier 系数的 Bernstein 凸包，之后使用全覆盖角弧的 sin/cos 区间；没有用角抽样最大值取代连续上界。

1024 弧覆盖 \(2\xi\in[0,2\pi]\)。所有对象具有 π 的 ξ 周期，并且准确 U_* 满足 \(U_*(\xi+\pi)=U_*(\xi)+\pi\)，故覆盖全部物理材料角。即使某辅助频率超过弧数，程序也取 `[-1,1]`，不会发生离散混叠或删掉该频率。

区间乘积复用已闭 binary64 外向运算及 gamma 误差证明。径向逐行直接 convolution 避免人工 padding；每行有限点积支付 \(\gamma_{2m+2}\)，m 为较短角系数长度，单位舍入参数保守取 \(2^{-52}\)，径向行累加逐次外向舍入。正常范围适配把非零且非常小的输入区间扩大到 \([-2^{-400},2^{-400}]\)，不改变浮点模式。下溢预算同时放大到至少 \(2^{-400}\)，故只能扩大包围。

平方和的准确值非负。外向加法在准确下端为零时可能产生一个负的最小 subnormal，程序以数学恒等式将其下端截回 0 后再开方。这不是删去真实负值。首次 diagnostic-01 因缺这一截取实际退出 1；失败源和失败 JSON 已另名闭存。随后 diagnostic-02 使用这一修正自然退出 0。

## 6. 后验递推

Gauss 残差为零，所以 Q 对应向量 \((Q_x,Q_y,0)\)，且
\(\widehat\alpha=(Jm,-Jl,0)\)。因此 \(|Qe_1|=|Q_y|\)，commutator 仅有 z 分量
\(Q_x\widehat\alpha_y-Q_y\widehat\alpha_x\)。消费者将 (4) 的 xy 分量与此 z 分量一起取欧氏范数，保留其正交结构。

若某解析小段宽 h 上 \(\|E\|\le B\)、\(|Qe_1|\le P\)、\(J\le J_+\)，则从原生单元左端开始追踪 \(W=D-FQ\) 的界 d 及 \(C=X_u-ae_2\) 的界 k，更新

\[
d_{new}=d+hB,\qquad
k_{new}=k+J_+(hd+h^2B/2+hP).
\]

内部小段 Q 不必为零，W 连续，所以此更新可逐小段使用；到原生单元末 Q 准确为零，d 就重新是 D 的界。每段内部的 D 另加 Q 范数。非负界单调增加，用段末 k 和该段连续 a 下界即可覆盖段内全部点：

\[
\|g^{-1/2}(X^*e-g)g^{-1/2}\|
\le2k/a+(k/a)^2.
\]

全域从已闭 native-inlet 包的真实 \(d_0\le1.638645511272696e-16,k_0=0\) 开始。新的 clock 在起点 J=1 且准确 a0、初始曲线和固定 seed chart 均相同，所以该初始缺陷预算可直接用于本准确对象。

## 7. 实际已完成诊断与后续全域记录

恢复后 diagnostic-02（session **9547**）自然退出 0，用时 **31.027516 秒**。它完整包围原生 cell 189，含三个内部小段：两条正常解析支式及约 `3.911157e-35` 宽的根夹区间。两正常支段 \(|\widehat H-P|\) 分别不超过 `9.058e-20,2.730e-19`；根夹段使用保守 `0.032779` 上界并乘准确极小长度。共用单元均值范数上界约 `1.589308e-6`，含全部漂移及 commutator 后，该单元按零位置缺陷、已知微小 d0 的局部推进得到 d 约 `9.018e-9`、k 约 `9.162e-11`。这不是整个前缀的度量界。

`fd2d-metric-gc-primitive-continuous-resume.py` 对复用报告逐一验证 source、backend、field、profile、chart、inlet 及所有有限近似设置。复用的单元两端以准确有理数比较，旧单元后验删除，新的全域传播从真实初值按原顺序重算。完整 237 格运行实际复用 cell 189，其余格计算一次；每个完成格立即写成完整 gzip member，便于真实中断后恢复。

全域实算结果另由 `primitive-continuous-full-01` 报告给出。闭曲面、非线性尾接合、达到强振幅及 G5 加密证据均不由一个前缀 metric 后验自动得到。
