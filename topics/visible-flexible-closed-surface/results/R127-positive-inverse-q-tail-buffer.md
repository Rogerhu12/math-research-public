# R127：正系数 inverse-Q 有限尾与准确 C² 端口

2026-11-12，metric_closure。

本结果给出可直接计算的有限物理尾构造：用正 Bernstein 多项式规定 m2
线性高度，再准确恢复正背景斜率，避免在低斜率谷的端点计算 0/0。
背景曲率、真实线性第二基本形式与图坐标系数分别保留。
完整证明和实际输入见[构造全文](../notes/2026-11-12-fd2d-metric-inverse-q-buffer-design.md)。

## 1. 构造定理

令 r=a+ℓt，a,ℓ>0，0≤t≤1，b=a+ℓ。给严格正多项式 k，记端值 k0,k1。
若

\[
\int_0^1t(1-t)k(t)dt=\frac{a^2k_0+b^2k_1}{12\ell^2},
\]

定义

\[
Q=-\frac{a^2k_0}{12\ell^2}+\int_0^t v(1-v)k(v)dv,
\quad H=r^4Q,
\quad J=H_r-4H/r.
\]

多项式 F=r²Qtt+8ℓrQt+12ℓ²Q 在两端为零，故准确存在多项式 P 满足
F=t(1−t)P。对任意 w0>0 取

\[
w_{raw}(t)=w_0\exp\left[-\int_0^t\frac{P(v)}{r(v)^2k(v)}dv\right].
\]

则 wraw>0 且光滑；H 与它准确满足物理 m2 方程

\[
H_{rr}=-(w_r/w)(H_r-4H/r).
\]

给定任意 μ>0，令 Z=r⁴wJ/(√12 μ)、Q=H/r⁴，即为 canonical 系统
Qr=√12 μZ/(r⁸w)、Zr=−√12 r⁶wQ/μ 的解。
向内单位 cut 高度比例恰为

\[
\gamma=|H(a)/H(b)|=(a/b)^6 k_0/k_1.
\]

**证明。** Qt=t(1−t)k，故 J=r⁴t(1−t)k/ℓ。
加权矩条件给 Q(1)=b²k1/(12ℓ²)，直接求值便有 F(0)=F(1)=0。
Hrr=r²F/ℓ²，与 (log wraw)r=−P/(ℓr²k) 相乘立即得方程。
再求 Qr、Zr 即得 canonical 两式。H 两端分别为 −a⁶k0/(12ℓ²)
和 b⁶k1/(12ℓ²)，给所述增益。全部分母在闭区间上严格正，故正则性包含端点。

## 2. 准确端口和可计算参数化

若指定 s_i=(w_r/w)(r_i)，只需规定

\[
k'_0=k_0[1-\ell(10/a+s_0)/2],\quad
k'_1=-k_1[1+\ell(10/b+s_1)/2].
\]

从 F 的端导数及 F=t(1−t)P 得
P(0)=10aℓk0+2a²(k′0−k0)、
P(1)=10bℓk1+2b²(k1+k′1)，故准确恢复这两个 logarithmic 端导。
匹配 w,w_r 给背景高度原函数的 C² 接合；不增加 w_rr/C³ 条件。

正 Bernstein 系数的准确加权矩为
ωi=(i+1)(d−i+1)/[(d+1)(d+2)(d+3)]。
四个端系数由 k0,k1,k′0,k′1 确定，剩余正系数按剩余加权矩作一次正比例归一，
即同时保证 k>0 和矩等式。详细充分条件及无需幂基相除的 P 系数算法已在
[全文 §§4–5](../notes/2026-11-12-fd2d-metric-inverse-q-buffer-design.md) 证明。

对于任意目标外端 w1>0，还可用

\[
w=w_{raw}\exp(cS_5),\quad
c=\log(w_1/w_{raw}(1)),\quad S_5=10t^3-15t^4+6t^5
\]

准确校准端值。S5′、S5″ 在两端均为零，所以 logarithmic 端导保持，C²
接合不变。原 H 此时有准确方程缺陷 (c/ℓ)S5′J；若 c≠0，新 g 的真实
线性和非线性尾须重新计算，不能自动沿用 H。

## 3. 物理预算与实际样本

全文从完整 height-jet 公式导出

\[
\delta l=-H_{rr}/\sqrt{1+w^2},\quad
\delta n=-\sqrt{1+w^2}J/r,\quad
\delta m=2H/r^2-2H_r/r,
\]

并与 Γ=J/w−4Hw/r 分别控制。它还证明固定端值的最优二阶必要预算

\[
\|H_{rr}\|_\infty\ge
\frac{2S+\sqrt{4S^2+\ell^2(v_1-v_0)^2}}{\ell^2},
\quad S=|H_1-H_0-(v_0+v_1)\ell/2|.
\]

一个已实际计算的 raw0 候选由闭存 JSON、MJS reader 和 check 给出：
外端 r=.65,w=.1，4097点有限检查的背景曲率最大值6.952313、
单位真实线性 II 行和329.263629、Γ972.027685；准确定义采用上述正矩归一
和 S5 端值校准。完整文件身份见
[闭存清单](../notes/2026-11-12-fd2d-metric-inverse-q-closed-group-01.json)。

这些有限检查不是全连续证书。该样本 γ=.0959543，大于原 raw0 的 .0470740，
深 source 的实际单位 cut 归一化因而改变。几何分支正在对同一新 g 消费整个
有限尾；本结果没有声称强幅度非线性尾、完整闭核或 reach 已完成。
