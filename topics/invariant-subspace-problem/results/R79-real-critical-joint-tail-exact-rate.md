# R79：实系数临界联合尾的精确指数率

日期：2026-11-12（UTC）。经主会话逐段核验。

**状态：以下精确极限定理已证明。** 本条接续并冻结 [R77 联合尾归约稿](../notes/2026-11-12-critical-two-scale-joint-tail-0c-agent.md)。只处理实系数 $c$，不把复系数的相位问题省略。

## 1. 模型与结论

固定
$$
p>1,\qquad q=2p-1,\qquad c\in\mathbb R.
$$
令
$$
C_{s,m}=\sum_{j\ge m}(j+2)^{-s}E_j,\qquad
V_m=C_{p,m}^2+cC_{q,m},\qquad M=m+2.
$$
对 $u>0$ 定义负实时间联合尾范数
$$
F_m(u)=\|e^{uM^q V_m^*}1\|.
\tag{1.1}
$$
这正是 R77 的 $F_m(-uM^q)$。

仍记
$$
\ell_{\mathbb C}(z)=\frac12\log\left(1-\Re z+\frac{|z|^2}2\right),
$$
$$
h_{p,q}(z,w)
=\int_1^\infty
\ell_{\mathbb C}(zx^{-p}+wx^{-q})\,dx,
$$
$$
E_u(v)=-\frac{v^2}{4u}+h_{p,q}(-v,-uc),
\qquad
H_{p,c}(u)=\max_{v\in\mathbb R}E_u(v).
\tag{1.2}
$$
$p,q>1$ 保证积分收敛。线性增长界与 Gaussian 二次项保证最大值在有限位置取到。

**定理 1.1。** 对每个固定紧区间 $0<a\le u\le b<\infty$，
$$
\boxed{
\sup_{u\in[a,b]}
\left|
\frac1M\log F_m(u)-H_{p,c}(u)
\right|\longrightarrow0.}
\tag{1.3}
$$
所以 R77 的 Gaussian 变分上界在实 $c$ 时就是精确的联合尾指数率。

## 2. 实际乘积向量与逐位 Gram 恒等式

R77 的 Bochner-Gaussian 公式写为
$$
e^{uM^qV_m^*}1
=A_m(u)\int_{\mathbb R}
e^{-Mv^2/(4u)}\Psi_{m,u}(v)\,dv,
\qquad
A_m(u)=\sqrt{\frac{M}{4\pi u}},
\tag{2.1}
$$
其中
$$
\Psi_{m,u}(v)
=\exp[M^pvC_{p,m}^*+uM^qcC_{q,m}^*]1.
$$
它是逐位向量的张量积。令
$$
x_{j,m}=\frac{j+2}{M}\ge1,\qquad
a_{j,m,u}(v)=vx_{j,m}^{-p}+ucx_{j,m}^{-q}.
$$
在第 $j$ 位的归一化二元空间中，相应因子为
$$
w(a)=\frac1{\sqrt2}(1+a,1).
$$
因为 $a$ 为实数，
$$
P(a)=\|w(a)\|^2=1+a+\frac{a^2}2\ge\frac12,
$$
$$
G(a,b)=\langle w(a),w(b)\rangle
=1+\frac{a+b}2+\frac{ab}2.
\tag{2.2}
$$
最关键的精确恒等式是
$$
\boxed{P(a)P(b)-G(a,b)^2=\frac{(a-b)^2}{4}.}
\tag{2.3}
$$
因此对 $a\ne b$，
$$
\left|\frac{G(a,b)}{\sqrt{P(a)P(b)}}\right|<1.
\tag{2.4}
$$
全局内积未必为非负；本证明只在明确控制的近区使用正号。

所有无限乘积均按原参考向量意义收敛，因为对每个固定 $m,u,v$，
$\sum_{j\ge m}|a_{j,m,u}(v)|<\infty$。

Riemann 和给
$$
E_{m,u}(v):=-\frac{v^2}{4u}
+\frac1M\log\|\Psi_{m,u}(v)\|
\longrightarrow E_u(v)
\tag{2.5}
$$
在 $u,v$ 的紧集上一致成立。统一线性界还给
$$
E_{m,u}(v)\le-\frac{v^2}{4b}+C_1|v|+C_2
\tag{2.6}
$$
对 $u\in[a,b]$、全部 $M$ 一致成立。

## 3. 已有上界

由 (2.1) 的 Minkowski 不等式、(2.5) 的紧集一致收敛及 (2.6) 的 Gaussian 尾控制，Laplace 上界为
$$
\frac1M\log F_m(u)\le H_{p,c}(u)+o(1)
\tag{3.1}
$$
关于 $u\in[a,b]$ 一致。$A_m(u)$ 只贡献 $O(\log M)/M$。

以下证明反向不等式，同时处理 Bochner 积分的远区可能负号。

## 4. 最大点附近的内积符号统一为正

对每个 $u\in[a,b]$，选取任意最大点 $v_0=v_0(u)$：
$$
E_u(v_0)=H_{p,c}(u).
$$
由统一二次上界，全部可能的 $v_0$ 位于一个固定紧区间
$[-R_0,R_0]$。不要求选择 $v_0(u)$ 连续。

取单位测试向量
$$
h_{m,u}=
\frac{\Psi_{m,u}(v_0)}
{\|\Psi_{m,u}(v_0)\|}.
\tag{4.1}
$$
在 $v=v_0$ 时，每个局部 Gram 因子为
$G(a(v_0),a(v_0))=P(a(v_0))\ge1/2$。又
$$
\frac{\partial}{\partial v}
G(a_{j,m,u}(v),a_{j,m,u}(v_0))
=\frac{1+a_{j,m,u}(v_0)}2\,x_{j,m}^{-p}.
$$
右侧在全部 $j,m,u,v_0$ 上一致有界，因为 $x_{j,m}\ge1$、
$u\in[a,b]$、$v_0\in[-R_0,R_0]$。故存在固定 $\delta_0>0$，使
$$
|v-v_0|<\delta_0
\quad\Longrightarrow\quad
G(a(v),a(v_0))\ge1/4
$$
对每个尾位都成立。

因此在这个近区中，
$$
\boxed{\langle\Psi_{m,u}(v),h_{m,u}\rangle>0.}
\tag{4.2}
$$
这是逐位乘积的正号结论；不是从整体 Gram 非负性作的推断。

在近区定义投影后的对数率
$$
\begin{aligned}
K_{m,u}(v;v_0)
={}&-\frac{v^2}{4u}
+\frac1M\sum_{j\ge m}
\log G(a_{j,m,u}(v),a_{j,m,u}(v_0))\\
&-\frac1{2M}\sum_{j\ge m}
\log P(a_{j,m,u}(v_0)).
\end{aligned}
\tag{4.3}
$$
局部 Gram 因子有统一正下界，且尾部的差离一由可积幂函数控制，所以 (4.3) 的 Riemann 极限在相关紧集中一致，并且极限关于 $v,v_0,u$ 连续。在 $v=v_0$ 时，
$$
K_u(v_0;v_0)=E_u(v_0)=H_{p,c}(u).
$$
故对每个 $\varepsilon>0$，存在固定
$0<\delta_1<\delta_0$，使充分大 $m$ 下
$$
|v-v_0|\le\delta_1
\quad\Longrightarrow\quad
K_{m,u}(v;v_0)\ge H_{p,c}(u)-2\varepsilon
\tag{4.4}
$$
对全部 $u\in[a,b]$ 一致成立。

## 5. 远区的指数分离压过可能取消

先在一个固定大区间 $|v|\le R$ 内考虑
$|v-v_0|\ge\delta_0$。取约 $M$ 个满足
$$
1\le x_{j,m}\le2
$$
的尾位。其局部参数差满足
$$
|a_{j,m,u}(v)-a_{j,m,u}(v_0)|
=|v-v_0|x_{j,m}^{-p}
\ge\delta_0\,2^{-p}.
$$
所有 $P(a(v)),P(a(v_0))$ 在该紧集上有共同有限上界。由 (2.3)，存在固定 $\rho\in(0,1)$，使每个这些位都满足
$$
\left|
\frac{G(a(v),a(v_0))}
{\sqrt{P(a(v))P(a(v_0))}}
\right|\le\rho.
$$
其余位用 Cauchy–Schwarz 的上界一。于是
$$
\boxed{
\frac{|\langle\Psi_{m,u}(v),h_{m,u}\rangle|}
{\|\Psi_{m,u}(v)\|}
\le e^{-\kappa M}
}
\tag{5.1}
$$
在这个远区一致成立，其中 $\kappa>0$。

这给的是绝对值界，所以允许局部或整体内积为负。即使 $E_u$ 有别的同高最大点，只要它与 $v_0$ 距离至少 $\delta_0$，也受 (5.1) 的指数分离控制。

对无界区 $|v|>R$，用归一化内积绝对值不超过一，再用 (2.6) 的 Gaussian 衰减。由于连续函数 $H_{p,c}$ 在 $[a,b]$ 上有有限下界，可先取 $R$ 足够大，使这部分积分相对
$e^{MH_{p,c}(u)}$ 至少有一个固定正指数差。随后把 $\kappa$ 缩小到不超过该差的一半。结合紧集远区，得到
$$
\left|
A_m(u)\int_{|v-v_0|\ge\delta_0}
e^{-Mv^2/(4u)}
\langle\Psi_{m,u}(v),h_{m,u}\rangle\,dv
\right|
\le C A_m(u)e^{M[H_{p,c}(u)-\kappa/2]}
\tag{5.2}
$$
对大 $m$ 一致成立。所有可能的负号或取消都已包含在这个绝对值上界中。

## 6. 下界与统一极限

近区中的被积函数为正，所以可以在该区内仅保留
$|v-v_0|\le\delta_1$。由 (4.4)，这部分至少为
$$
2\delta_1A_m(u)e^{M[H_{p,c}(u)-2\varepsilon]}.
$$
取 $\varepsilon<\kappa/8$，该正项在指数上严格大于 (5.2) 的全部可能负贡献。因此对充分大 $m$，
$$
\begin{aligned}
F_m(u)
&\ge
\left|\left\langle e^{uM^qV_m^*}1,h_{m,u}\right\rangle\right|\\
&\ge
\delta_1A_m(u)e^{M[H_{p,c}(u)-2\varepsilon]}.
\end{aligned}
$$
取对数除以 $M$，得到关于 $u\in[a,b]$ 一致的下界
$$
\liminf_{m\to\infty}
\inf_{u\in[a,b]}
\left[\frac1M\log F_m(u)-H_{p,c}(u)\right]
\ge-2\varepsilon.
$$
$\varepsilon$ 可任意小；与 (3.1) 合并即证定理 1.1。

测试向量 $h_{m,u}$ 依赖 $m,u$ 只用于证明一个范数的下界，不用它代替实际核分离证明中的固定循环测试向量 $1$。

## 7. 对临界模型的含义与限制

一个可以立即严格排除的参数方向是 $c\ge0$。若 $c>0$，在变分式中取 $v=0$ 就有
$$
H_{p,c}(u)\ge h_{p,q}(0,-uc)>0\qquad(u>0),
$$
因为每个非零实负局部参数都使 $P_{\mathbb C}$ 大于一。若 $c=0$，取充分小的正 $v$，由
$h_{p,q}(-v,0)=v/[2(p-1)]+O(v^2)$，
也有 $-v^2/(4u)+h_{p,q}(-v,0)>0$。因此对 $c\ge0$，**任何正区间都不可能给出负实时间的负 BW 证书**。这里排除的是这一时间方向，而非排除算子单射性。

对实 $c$，R77 的负实时间联合尾方法所面对的轮廓确切就是
$H_{p,c}$。因此如果某一区间的
$$
g_{a,b}+\int_a^bH_{p,c}\,d\nu_{a,b}
$$
非负，不能仅通过改进同一个联合尾范数的指数上界，把该区间变成负 BW 证书；主指数已经精确。但这不说明别的区间、别的复时间方向或别的核分离机制失败，更不说明实际算子有非零核。

在均值抵消点 $c=-1/(p-1)$，R77 的三阶小时间展开现在也是实际联合尾的精确指数轮廓展开。不过全区间负 BW 仍需另行证明；局部收缩不足以自动完成它。

对复 $c$，局部 Gram 因子通常带有相位。即使每个因子靠近正实轴，$O(M)$ 个因子的相位仍可能累积，近区积分可出现真正的振荡取消。因此本条的正近区论证不能直接推广；目前只保留 R77 对复 $c$ 的上界。

