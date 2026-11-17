# R40：q≈.04 时原 flat ramp 的严格首负 K 特征窗

2026-11-18，Astra-held10-7322d0de-20261118 / m3_true_coupling。

本条补足一个具体局部设计门：**在原实际 flat ramp 参数不变时，半径
$R=1+8q$、法向角半宽 $a_0=.21$ 的精确圆弧，其 R5 已知保护窗在首个负 K 加速段结束前已经耗尽。**
此前 R32 用于 $q\approx.085$ 的峰值下界不能直接移给 $q\approx.04$；在后者参数处，
同样的粗界略小于 $.21$，只说明该估计不足。本条保留原完整 ramp，通过精确分段积分下包围得到正余量。

这是条件性的局部特征窗检查，不是圆弧 BVP 的存在性结论，也不证明圆弧在保护窗外实际消失。
当前 raw $\lambda=.02$ 入口本身仍不是精确圆弧；本条用于后续明确选择的 $\lambda=1$ 设计。

## 1. 参数与结论

固定与当前 outward prefix 相同的设计

$$
 v=\frac9{20},\qquad \varepsilon=\frac25,\qquad
 \eta=\frac1{20},\qquad
 T_u=\frac{\delta}{v(1-\varepsilon)}.
$$

对整个参数范围

$$
 q\in\left[\frac{39}{1000},\frac{41}{1000}\right],\qquad
 \delta\ge\frac3{50},\qquad R=1+8q,                       \tag{1}
$$

初始加速段 $0\le s\le L:=\varepsilon T_u$ 的 R5 损耗满足

$$
 \boxed{\quad \frac{\chi(L)}R
   >.2108827779904414>.21=a_0.\quad}                      \tag{2}
$$

同时

$$
 Rv\le\frac{747}{1250}=.5976<1.                         \tag{3}
$$

因此所用平方根在该段及随后 coast 上有统一正余量。圆弧的材料半宽是 $Ra_0$，
故 (2) 正是 $\chi(L)>Ra_0$，不是把材料弧长和法向角混为一谈。
这里的 $\delta\ge.060$ 没有暗含上界；本条只讨论该局部 ramp，其他全局设计门仍须对实际选定的 $\delta$ 另行验证。

结论仅用 $R$ 与上述局部 profile，**不依赖主圆化过渡宽度或控制转接宽度**。
这种独立性要求新设计在保护弧上仍精确满足 $\rho=R=1+8q$，且完整控制在该弧上为零。
加宽过渡区不能据此继承 R32 的其他几何、矩、reach 或握持常数。

## 2. 原 ramp 的精确表达式

设 $t=s/(\varepsilon T_u)\in[0,1]$。记 $F$ 为速度 ramp，$P'=F$、$P(0)=0$，
$d=F'$。在 $0\le z\le1/2$，令 $x=z/\eta$，定义

$$
 f(z)=\begin{cases}
 \dfrac{\eta}{1-\eta}(x^3-x^4/2),&z\le\eta,\\
 \dfrac{z-\eta/2}{1-\eta},&z\ge\eta,
 \end{cases}
$$

$$
 p(z)=\begin{cases}
 \dfrac{\eta^2}{1-\eta}(x^4/4-x^5/10),&z\le\eta,\\
 \dfrac{z^2/2-\eta z/2+3\eta^2/20}{1-\eta},&z\ge\eta,
 \end{cases}
$$

$$
 d_0(z)=\begin{cases}
 \dfrac{3x^2-2x^3}{1-\eta},&z\le\eta,\\
 \dfrac1{1-\eta},&z\ge\eta.
 \end{cases}
$$

当 $t\le1/2$，取 $(F,P,d)=(f(t),p(t),d_0(t))$；当 $t\ge1/2$，取

$$
 F(t)=1-f(1-t),\qquad
 P(t)=\frac12-(1-t)+p(1-t),\qquad d(t)=d_0(1-t).           \tag{4}
$$

两段在所有接点匹配。这正是原源 `950f-prefix-flat-accel-screen.py` 的 `turn_ramp` 定义，
其中 `.15` 对应精确系数 $3/20$。直接微分给 $P'=F$、$F'=d$；
$F$、$P$ 非减，$F(0)=P(0)=d(0)=0$、$F(1)=1$、$P(1)=1/2$、$d(1)=0$。
$d$ 在 $[0,\eta]$ 上非减、在 $[\eta,1-\eta]$ 上常数、在 $[1-\eta,1]$ 上非增。
这也验证 R5 所需初始 $a''$ 的非减性，且此 ramp 给出 $a\in C^3$。

为避免与圆弧半宽 $a_0$ 混淆，把度量的纬线尺度记为 $A(s)$。令
$B=\delta\varepsilon/(1-\varepsilon)$，则

$$
 A(s)=1+BP(t),\qquad A'(s)=vF(t),\qquad
 A''(s)=\frac{v}{\varepsilon T_u}d(t).                   \tag{5}
$$

R5 中曲率 $k=1/R$，所以将 (5) 代入其定义，并使用
$v\varepsilon T_u=B$，得到完整精确积分

$$
 \frac{\chi(L)}R
  =J(B,y):=\int_0^1
   \sqrt{\frac{B d(t)}{(1+BP(t))(1-y^2F(t)^2)}}\,dt,
 \qquad y=Rv.                                           \tag{6}
$$

该式保留了 ramp 端部加速度分布；没有把 $A$ 和 $A''$ 同时换成全段峰值。

## 3. 参数单调性

在适用范围内 $P,d,F\ge0$、$0\le yF<1$。对每个固定 $t$，

$$
 \frac{\partial}{\partial B}\frac{B}{1+BP(t)}
   =\frac1{(1+BP(t))^2}>0.
$$

且 $1/(1-y^2F(t)^2)$ 随 $y\ge0$ 非减。因此 $J$ 随 $\delta$ 和 $q$ 非减，
整个 (1) 的下界只需在

$$
 q_-=39/1000,\quad \delta_-=3/50,\quad
 B_-=1/25,\quad y_-=(1+8q_-)v=369/625                   \tag{7}
$$

处支付。上端 $q_+=41/1000$ 则直接给出 (3)。此处是逐点解析单调性，不是参数采样所得的猜测。

## 4. 有限精确下包围

取 $N=2000$、$t_j=j/N$。对第 $j$ 个小区间置

$$
 m_j=\min\{d(t_j),d(t_{j+1})\},\qquad
 r_j=\frac{B_-m_j}
 {(1+B_-P(t_{j+1}))(1-y_-^2F(t_j)^2)}.                  \tag{8}
$$

由 $d$ 的上述单峰结构，$m_j$ 是整个小区间上的下界；由 $F,P$ 非减，
(8) 分母的两个因子分别是 (6) 中对应因子的上界，且均为正。
故每点被积函数至少为 $\sqrt{r_j}$。

所有 $r_j$ 都是非负有理数。令 $S=10^{60}$，并完全使用整数算术计算

$$
 k_j=\operatorname{isqrt}
       \left(\left\lfloor S^2\operatorname{num}(r_j)/
                    \operatorname{den}(r_j)\right\rfloor\right).
$$

则 $k_j/S\le\sqrt{r_j}$，从而

$$
 J(B_-,y_-)\ \ge\ \frac1{NS}\sum_{j=0}^{N-1}k_j
  >.2108827779904414>.21.                               \tag{9}
$$

最后两个比较都由精确有理数交叉相乘完成；显示的小数不是判断依据。
脚本不用浮点平方根、浮点数值积分或三角函数。

## 5. 实际参数绑定与可重放性

配套源为 [certify_m3_smallq_ramp_window.py](../scripts/resume_m3/certify_m3_smallq_ramp_window.py)。
`--profile-checkpoint` 可读取已有实际 checkpoint 的 `frozen_profile`，核对 outward、flat、
$v=.45$、ramp $.4$、eta $.05$，并以实际 binary64 数值的精确有理表示检查 $q,\delta$ 落在 (1)。
它还对把这三个 binary64 参数本身视作精确参数的同一解析分段 ramp 独立重算下包围；
本次仍通过 (9)，而 $Rv<.597601$。该附加检查不把 NumPy 每次多项式浮点评价当作严格曲面证书。

本次绑定的是已经登记的 raw $\lambda=.02/M8$ 实际联立参数：
$q=.04$、$\delta=.06105141410261685$。
所核的是其已有完整 ramp 的参数身份；没有将该非圆核冒充为新的 $\lambda=1$ 解。
未来 M16 或其他实际终态只要保持该 profile 并满足 (1)，可直接调用同一命题，无须重做同一窗口结论。

命令、源文件 SHA-256、输入及输出 SHA-256 见
[smallq_ramp_window_execution.json](../scripts/resume_m3/smallq_ramp_window_execution.json)。
输出只在 scratch 保存，仓库保留定理、可再生源和执行标量。

本条使计划中的 $q\approx.04$ 精确圆弧入口通过这个局部门。完整新核的正性、真实尾联立、
原接受阈值、全角 metric、同一固定度量上的细化、闭图接缝及最终几何比例仍各按原标准检查。
