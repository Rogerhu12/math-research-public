# 非零初始径向加速度与平面核心的完整镜像两 jet

作者：visible-larger-astra-20261110 / alternative_mechanism，2026-11-10。

**状态：已证明。** 本文取消一个不必要的设计限制：平面核心的镜像 $C^2$ 接合不要求 $a''(0)=0$。这允许在强核心处立即进入负曲率段。本文不证明一个任意指定的 Cauchy 数据有全域解，也没有把 profile 的定义当作闭曲面存在。

## 1. 不依赖三阶导数的镜像定理

设 $F_+:[0,S]\times S^1\to\mathbb R^3$ 为 $C^2$ 浸入，满足

$$
F_+(0,\theta)=\gamma(\theta)\in\{z=0\},\qquad
\partial_sF_+(0,\theta)=e_z,
\tag{1}
$$

且 $|\partial_sF_+|^2=1$。令 $J(x,y,z)=(x,y,-z)$，定义

$$
F(s,\theta)=
\begin{cases}
F_+(s,\theta),&s\ge0,\\
J F_+(-s,\theta),&s\le0.
\end{cases}
\tag{2}
$$

则 $F$ 是整个 $[-S,S]\times S^1$ 上的 $C^2$ 浸入。

**证明。** 在 $s=0$，位置 $\gamma$ 水平，故 $J\gamma=\gamma$。由 (1)，

$$
- JF_{+,s}=-Je_z=e_z=F_{+,s},\qquad
JF_{+,\theta}=F_{+,\theta}.
$$

故两侧一 jet 相同。对 $|F_{+,s}|^2=1$ 作一次 $s$ 导数，得到
$F_{+,s}\cdot F_{+,ss}=0$；在入口 $F_{+,s}=e_z$，所以 $F_{+,ss}$ 水平。
这一步只使用 $C^2$ 正则性。对 (1) 中的恒等式 $F_{+,s}(0,\theta)=e_z$ 作角导数，得到 $F_{+,s\theta}=0$。
最后 $F_{+,\theta\theta}=\gamma''$ 也水平。于是入口的全部二阶匹配为

$$
JF_{+,ss}=F_{+,ss},\qquad
-JF_{+,s\theta}=0=F_{+,s\theta},\qquad
JF_{+,\theta\theta}=F_{+,\theta\theta}.
\tag{3}
$$

左右导数在闭半域上连续，且 (3) 与前面零、一阶匹配成立，所以通常的分片导数判据给出全局 $C^2$。入口导数 $e_z,\gamma'$ 线性无关，故接缝也保持浸入。证毕。

若上半部诱导 $ds^2+a(s)^2d\theta^2$，则要求平面核心与竖直入口速度相容会给 $a'(0)=0$；但证明从未要求 $a''(0)=0$。将 $a$ 偶延拓为 $a(|s|)$，只要 $a'(0)=0$，它在零点就是 $C^2$，第二导数的两侧迹同为 $a''(0)$。

上述是局部接合及浸入结论。全域单射、闭合、reach 和整个族的量化指标仍须另证。

## 2. Frenet 模型的入口二阶导数及曲率

进一步假设 $\gamma$ 为正向平面凸曲线，曲率半径为 $\rho>0$、周长 $2\pi a_0$。采用向外平面法向 $n_{\rm out}$。在径向旋转 metric 下，真实 Frenet 速度为

$$
F_s=\alpha N+\beta B,\qquad
\alpha=-\frac{a'}{a\kappa},\quad
\beta=\sqrt{1-\alpha^2},
\tag{4}
$$

其中入口 $N=-n_{\rm out},B=e_z,\kappa=1/\rho$。设该经典流可对其角二阶 jet 作一次径向微分（本题的光滑角向有限谱流满足此条件）。因为入口 $F_s=e_z$ 是角向常量，曲线的一、二阶角导数的径向变分都为零；故 Frenet 标架的径向一阶变分为零。又 $a'(0)=0$，所以

$$
\alpha_s(0)=-\frac{a''(0)\rho}{a_0},\qquad \beta_s(0)=0.
$$

直接微分 (4) 得

$$
\boxed{F_{ss}(0,\theta)=\frac{a''(0)\rho(\theta)}{a_0}\,n_{\rm out}(\theta).}
\tag{5}
$$

这确为水平向量，与第 1 节的纯 $C^2$ 结论相容。入口混合第二基本形式为零，两个主曲率的绝对值是

$$
\boxed{\frac1\rho,\qquad \frac{|a''(0)|\rho}{a_0}.}
\tag{6}
$$

按一致法向取符号时，两者乘积为 $-a''(0)/a_0$。因此正的初始径向加速度产生负高斯曲率，而不是接缝奇点。

对本题强核心

$$
h=1+A\cos2\varphi-\frac A{10\sqrt2}\cos4\varphi,
\quad A=.38,
$$

其 $a_0=1$，已有直接公式

$$
\rho_{\min}=1-\frac{3A}{\sqrt2},\qquad
\rho_{\max}=1+\left(3+\frac3{2\sqrt2}\right)A.
$$

取 $a''(0)=2$ 时，初始经线曲率最大约 $5.08610$，仍低于初始环向曲率最大约 $5.15734$。因此在这个参数上，加速度 2 不增加初始最大绝对主曲率；这只是一项入口曲率计算，不替代后续曲率控制。

## 3. 可直接计算的快速 outward 段

给定 $0<V<1$、$S>0$ 与整数 $p\ge1$，在 $0\le s\le S$ 定义

$$
\begin{aligned}
a(s)&=1+VS\left[u-\frac{1-(1-u)^{p+2}}{p+2}\right],\\
a'(s)&=V[1-(1-u)^{p+1}],\\
a''(s)&=\frac{V(p+1)}S(1-u)^p,
\qquad u=s/S.
\end{aligned}
\tag{7}
$$

在 $s\ge S$ 延拓为

$$
a(s)=a(S)+V(s-S).
\tag{8}
$$

逐项求导给出 (7) 的三条关系；在 $S$ 两侧位置、速度和加速度分别同为

$$
a(S)=1+VS\frac{p+1}{p+2},\qquad a'(S)=V,\qquad a''(S)=0.
$$

所以 (7)–(8) 定义真正 $C^2$ 的同一径向函数。入口 $a'(0)=0$，而
$a''(0)=V(p+1)/S>0$；可用第 1 节镜像。这个设计族允许在短初段中用较大的初始加速度，并逐渐减速加速过程，随后接明确可展段。

## 4. 一个完整一周期的 $C^2$ profile provider

为直接接现有 `PlanarSymmetryFlow` 与其原 bridge，给出更一般的一周期公式。选径向增量 $\Delta>0$、向外段长度 $T_u>0$、初始加速度 $k_0\ge0$，置

$$
A=k_0T_u,\qquad B=\frac{30\Delta}{T_u}-\frac52 A,
$$

并要求 $A+B\ge0$ 及下述速度绝对值小于 1。在 $u=s/T_u\in[0,1]$ 定义

$$
\begin{aligned}
a&=1+T_u\left[\frac A2u^2+\frac{B-2A}3u^3
 +\frac{A-2B}4u^4+\frac B5u^5\right],\\
a'&=u(1-u)^2(A+Bu),\\
a''&=\frac1{T_u}\left[A+2(B-2A)u+3(A-2B)u^2+4Bu^3\right].
\end{aligned}
\tag{9}
$$

其入口三值为 $(1,0,k_0)$，出口三值为 $(1+\Delta,0,0)$。
积分系数检验为 $A/12+B/30=\Delta/T_u$。

在返回段 $x=(s-T_u)/T_d\in[0,1]$，用

$$
\begin{aligned}
a&=1+\Delta-\Delta(10x^3-15x^4+6x^5),\\
a'&=-\frac{30\Delta}{T_d}x^2(1-x)^2,\\
a''&=-\frac{60\Delta}{T_d^2}x(1-x)(1-2x).
\end{aligned}
\tag{10}
$$

在两端分别为 $(1+\Delta,0,0)$ 与 $(1,0,0)$。因此 (9)–(10) 内部接合是 $C^2$，末端可直接接原 bridge 的 $(a,a',a'')=(1,0,0)$。

选择 $T_d=15\Delta/(8v_d)$ 时，返回速度的最大绝对值为 $v_d$。向外最大速度可由 (9) 的三次导数多项式全部实根准确确定（数值实现枚举其在 $(0,1)$ 的实根并检查），不能把配置名 `vu` 自动当成实际最大速度。

实现为 `computations/alternative-fast-profile.py` 的 `FastStartCycle`，通过 `install(PlanarSymmetryFlow)` 在内存中加入 `ramp_law='fast_start'` 的分支。它更新 `Tu/Td/prefix_end/end/breakpoints`，不修改原 bridge，不修改其他文件，不对最后时刻取模返回到加速度 $k_0$。当前明确只接受一个周期，以免第二周期入口 $k_0$ 与前一周期出口 0 产生加速度跳变。

该 provider 只定义新的物理度量；一旦选定参数，后续 refinement 必须保持这些参数不变。任意 profile 的非线性 Cauchy 域、末端反馈和闭合均没有由这些代数公式自动得到。
