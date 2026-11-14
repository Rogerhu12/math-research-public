# 首段单调 Bernstein 速度族：保持入口曲率的缩短候选

日期：2026-11-12。分类：下述代数与不等式已证明；末尾数表只是该代数的 JavaScript float64 计算，不是 BVP、实际新解、完整直径或 reach 证书。
本方向不替换正在恢复的实际 q096 目标。它可作为下一次已接受态全 Jacobian 响应中的额外物理列。

## 1. 旧 pulse 的一个明确代价

当前 computations/strong_initial_speed_pulse.py 使用
$
v(u)=V u^2(3-2u)+a u(1-u)^2+64b u^3(1-u)^3,
\qquad a=k_0S,\quad u=s/S.
$
它保持首段半径增量、端点速度和加速度，并通过
$
\delta=\left(\frac V2+\frac{16b}{35}\right)S+\frac{k_0S^2}{12}
$
决定长度。源已读于 main cb6b2058；本注不改该源或任一 MJS。

直接微分并取 $u=4/5$ 得
$
\frac{v_u(4/5)}{1-4/5}
 =\frac{24V-7a}{5}-\frac{9216}{625}b.
$
故只要
$
 b>\frac{125}{384}V
$
且 $a>0$，该点的 $r''=v_u/S<0$。
因此其附近的 warped metric Gaussian curvature
$K=-r''/r$ 为正。对 $V=0.3198$，阈值约 .1041；
此前考虑的 $b=.2,.35,.5,.6$ 背景预算都会付出这种正曲率袋。
这并不证明不能求解，也不否定小 pulse 的真实局部收益；
只是说明“更短”同时改变了首段的曲率符号，可能影响高模传输，须实算而不能省略。

## 2. 一个保留非正 Gaussian 曲率的多项式族

设 $d\ge3$ 为整数，$V\in(0,1)$、$k_0,\delta>0$。
记 $B_j^d(u)=\binom dj u^j(1-u)^{d-j}$。
取 degree-$d$ Bernstein 速度控制点
$
(c_0,c_1,c_2,\ldots,c_d)
  =\left(0,\frac{k_0S}{d},V,\ldots,V\right),
\qquad
v_d(u;S)=\sum_{j=0}^d c_j B_j^d(u).
$
这是一条明确多项式，不是拟合或渐近取代。

由 Bernstein 端点与导数公式，
$
v_d(0)=0,\quad v_d(1)=V,\quad
\partial_s v_d(0)=k_0,\quad
\partial_s v_d(1)=0.
$
如果
$
 k_0S\le dV,
$
全部相邻控制点差非负，因而 $0\le v_d\le V<1$、$r''\ge0$。
对 $r(0)=a_0>0$，整段 $r\ge a_0$，故 $K=-r''/r\le0$。

Bernstein 基的积分都为 $1/(d+1)$，因此半径增量为
$
\delta=S\int_0^1v_d(u;S)\,du
 =A_dVS+B_dk_0S^2,\qquad
 A_d=\frac{d-1}{d+1},\quad B_d=\frac1{d(d+1)}.
$
唯一正长度可用无相消公式计算：
$
 S_d=\frac{2\delta}
 {A_dV+\sqrt{A_d^2V^2+4B_dk_0\delta}}.
$
固定 $\delta,V,k_0$ 后仍保持全部原首段端点半径、速度、加速度。

当 $d=3$ 时，Bernstein 展开恰是
$
v_3=V u^2(3-2u)+k_0S u(1-u)^2
$
及原长度方程 $\delta=VS/2+k_0S^2/12$。
实现时 default $d=3$ 或下述 $\lambda=0$ 应直接委托旧 provider，保留旧浮点算术。

### 半径的稳定表达

积分后 $r(u)$ 是 degree-$d+1$ 的 Bernstein 多项式。
其控制点满足
$
R_0=a_0,\qquad R_{j+1}-R_j=\frac{S c_j}{d+1}.
$
因此 $R_1=a_0$，
$R_2=a_0+k_0S^2/[d(d+1)]$，其后逐个增加 $SV/(d+1)$，
最后 $R_{d+1}=a_0+\delta$。
可以用 de Casteljau 或 Bernstein 递推评价，
无需将高阶多项式展开到有严重相消的单项式系数。

## 3. 长度单调性与极限

令 $f_d(S)=A_dVS+B_dk_0S^2$。直接相减：
$
f_{d+1}(S)-f_d(S)
 =\frac{2VS}{(d+1)(d+2)}
  \left(1-\frac{k_0S}{dV}\right).
$
若在 $S_d$ 上满足上面的单调速度条件，
则 $f_{d+1}(S_d)\ge\delta$。
由于 $f_{d+1}$ 在正轴严格递增，$S_{d+1}\le S_d$。
并且 $k_0S_{d+1}\le k_0S_d\le dV<(d+1)V$，所以条件向后保持。
从旧三次段的 $k_0S_3\le3V$ 出发，所有整数阶均合法且长度不增。

又 $v_d\le V$ 给 $S_d\ge\delta/V$，
而 $A_d\to1,B_d\to0$ 与长度方程给
$
 S_d\downarrow\frac{\delta}{V}.
$
这只是背景首段的长度极限；不代表整个曲面幅度或直径也按此收敛。

## 4. 连续物理控制，而不是换离散阶数

固定一个 $D\ge4$，引入
$
v_\lambda=(1-\lambda)v_3(\,\cdot\,;S_\lambda)
                  +\lambda v_D(\,\cdot\,;S_\lambda),\qquad 0\le\lambda\le1.
$
这里两项使用同一个真实长度 $S_\lambda$，并取
$
A_\lambda=(1-\lambda)/2+\lambda A_D,\qquad
B_\lambda=(1-\lambda)/12+\lambda B_D,\qquad
\delta=A_\lambda VS_\lambda+B_\lambda k_0S_\lambda^2.
$
全部端点 jets 仍相同。
在旧 $k_0S_3\le3V$ 条件下，
$
f_D(S_3)-f_3(S_3)
 =\frac{S_3(D-3)}{2(D+1)}
   \left(V-\frac{k_0S_3(D+4)}{6D}\right)\ge0,
$
因为 $(D+4)/(2D)\le1$ 对 $D\ge4$ 成立。
故 $S_\lambda\le S_3$，两项速度均单调；
凸组合也满足 $0\le v_\lambda\le V$、$r''_\lambda\ge0$。

这是可以进入真实物理 profile 的一个连续外控制。
$\lambda=0$ 原样返回旧 provider；非零 $\lambda$ 是新 $g$，不能称固定 $g$ 加密。
中心差分若需要负 $\lambda$，须在实现时另外核共同 Bernstein 导数控制点/速度域；
不能把上述仅 $[0,1]$ 的证明自动外推到负数。

## 5. 显式加速度峰与高度预算

写 $a=k_0S_d$、
$C=d((d-1)V-a)$，直接化简导数：
$
v'_d(u)=(1-u)^{d-2}(a+Cu).
$
若 $C\le(d-2)a$，最大值在 $u=0$，为 $a$。
否则唯一内部最大点为
$
u_*=\frac{C-(d-2)a}{(d-1)C}.
$
故首段的 $\max r''=\max v'_d/S_d$ 可直接精确评价，
不需要粗略的 $dV/S$ 系数界。

在旋转背景上，
$
|\kappa_{\rm meridian}|
 =\frac{r''}{\sqrt{1-v^2}}
 \le\frac{\max r''}{\sqrt{1-V^2}},
\qquad
|\kappa_{\rm parallel}|\le\frac1{a_0}.
$
真实非圆核心的曲面第二基本形式不由此界自动控制，仍要付完整场几何检查。

首段背景高度为
$
H_d=S_d\int_0^1\sqrt{1-v_d(u)^2}\,du,
\qquad
S_d\sqrt{1-V^2}\le H_d\le S_d.
$
例如若 $S_d<S_3\sqrt{1-V^2}$，这些粗界已经证明
$H_d<H_3$，不需依赖数值积分。
后续段可保留其原 $r,v,r''$ 起始数据；
但实际 BVP 为维持核心约束而发生的 $\delta/L_B/v_p$ 联调，
可能抵消背景高度收益，必须由真实全场响应判断。

## 6. 当前 q096 暖设计背景的标量数表

输入是已保存的 q096 **未解暖设计**：
$\delta=.16208113625386517,V=.3198,k_0=.45$。
以下只把上面的闭式公式在函数工具的 JavaScript float64 中执行；
没有加载 PDE/RHS、没有 Node 物理求解、没有构造新曲面。
小数舍入不是区间认证。

| degree | S | H 的粗界 | max r'' | 背景 meridian κ 的上界 |
|---|---:|---:|---:|---:|
| 3 | 0.8458494981 | 0.8014297719–0.8458494981 | 0.5097398854 | 0.5379925245 |
| 4 | 0.7743828810 | 0.7337162191–0.7743828810 | 0.6973849158 | 0.7360378934 |
| 6 | 0.6873861623 | 0.6512881269–0.6873861623 | 1.1218485532 | 1.1840276828 |
| 10 | 0.6135612247 | 0.5813401006–0.6135612247 | 2.0195669652 | 2.1315026767 |
| 16 | 0.5724748761 | 0.5424113987–0.5724748761 | 3.3950765108 | 3.5832506646 |
| 22 | 0.5541536116 | 0.5250522741–0.5541536116 | 4.7799635643 | 5.0448959144 |
| 28 | 0.5438121189 | 0.5152538641–0.5438121189 | 6.1682113638 | 6.5100881817 |

即 degree22 的背景首段长度约 .5542，旧三次段约 .84585；
其背景加速度峰约4.78，meridian曲率粗界约5.05。
这些数只说明存在值得实际求列的方向，不是大幅/闭面/reach结论。

## 7. 下一实际接口

先完成当前 q096 原实际 BVP；
在其真正接受后冻结 fixed-view，
把 $\lambda$ 列与 pulse $b$ 列一同加入一次真实 fixed-J 响应。
两者均需完整场、所有核心模、core-held $\delta/L_B/v_p$ 补偿、
完整线性后向误差与半步导数对照。
再以重算的全场 RMS、物理曲率和 D 预算选小真实非线性步。
本注没有执行这些步骤，也不替代固定 $g$ 的 M28/径向误差收敛工作。
