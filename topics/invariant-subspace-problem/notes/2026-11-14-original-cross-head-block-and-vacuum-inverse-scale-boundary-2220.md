# 原跨头块的主项不是 carry：与首层真尾逆的准确尺度

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_2220；AI-assisted，GPT-6 Astra Pro。

状态：**已证明的技术检查，不另计主要结果。** 本文计算原 $A_m$ 从高物理头进入前 $2^n$ 头的完整块。该块包含中间高位的真实一次下降，主范数为一段原平方权和的平方根，不能将整个块记成指数小的 carry。再与原尾真空到一孔的真正 MP 逆组合，可得到一个明确的非零极限。这里没有声称这一任意输入方向属于实际 $W$、固定测试伴随源流，或真正高返回选择子。

依赖：[R249 真实有限头及完整 carry 预算](../results/R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md) §6；[实际低头观察与高头反馈](../results/R239-appendix-actual-low-head-feedback-and-uniform-left-kernel-graph.md)。后者的反馈算子包含额外链基，本文不把它与下述原物理跨头块混同。

## 1. 在同一个原头中作二级位分解

对两个原边界模型 $T_N,T_Y$，记其真正有限头为 $A_m$，维数 $d=2^m$，原系数为
$$
a_j=(j+1)^{-2}.
$$
固定 $2\le n<m$，置 $H=2^n$，使用真正物理位分解
$$
\mathcal F_m=\mathcal F_n\otimes\mathcal H_{[n,m)}.
$$
后一个空间是第 $n,\ldots,m-1$ 位的有限二态张量积。它的真空记为 $\Omega_{\rm mid}$，$E_j$ 表示该位的原一次删除。
在原整数基中，前 $H$ 个头恰是
$\mathcal F_n\otimes\mathbb C\Omega_{\rm mid}$。

记到这个前缀的物理正交投影为 $P$。原有限头与二级理想分解满足
$$
\boxed{
\left\|A_m-
\left(A_n\otimes I+I\otimes D_{n,m}\right)\right\|
\le26\eta_{n-1},\qquad
D_{n,m}=\sum_{j=n}^{m-1}a_jE_j.
}
\tag{1.1}
$$
这是 R249 §6 的原全空间误差在不变前缀 $\mathcal F_m$ 上的压缩：所有位 $j\ge m$ 的真实项和理想删除在这个前缀都为零。因此它适用于原 $N$ 与完整 Cayley $Y$，没有只保留平方零项来替换 $Y$。

这里
$$
-\log\eta_{n-1}
=1400\,16^{n-1}-630\,8^{n-1}+300\,2^{n-1}
\tag{1.2}
$$
保持真实指数。

## 2. 完整低／高物理头块

定义真正跨头块
$$
B_{n,m}=P A_m(I-P):(I-P)\mathcal F_m\longrightarrow P\mathcal F_m.
\tag{2.1}
$$
理想块中，$A_n\otimes I$ 不改变中间位，故其此块为零。$D_{n,m}$ 只有在输入恰有一个中间位时才能进入中间真空。
若
$$
\omega_{n,m}=\sum_{j=n}^{m-1}a_j|j\rangle_{\rm mid},
\qquad
\beta_{n,m}^2=\sum_{j=n}^{m-1}(j+1)^{-4},
$$
则
$$
P\left(A_n\otimes I+I\otimes D_{n,m}\right)(I-P)
=I_{\mathcal F_n}\otimes
|\Omega_{\rm mid}\rangle\langle\omega_{n,m}|.
\tag{2.2}
$$
这是一个完整的原低头恒等张量一次位行。其范数准确等于 $\beta_{n,m}$；归一化中间输入
$\omega_{n,m}/\beta_{n,m}$ 给达到该范数的单位向量。

将 (1.1) 压缩到同一块，得到双边界
$$
\boxed{
\bigl|\|B_{n,m}\|-\beta_{n,m}\bigr|
\le26\eta_{n-1}.
}
\tag{2.3}
$$
特别，主项是实际高位下降，只有其与 (2.2) 的差是指数小的 carry。
不能把 $\|B_{n,m}\|$ 本身上界为 $O(\eta_{n-1})$。

## 3. 与同一原尾首层 MP 逆组合

保留原 $m$ 后方的完整无限尾
$$
D_m=\sum_{j\ge m}a_jE_j,\qquad
S_m=\sum_{j\ge m}(j+1)^{-4}.
$$
其真空到一孔的真正最小右逆为
$$
R_{m,0}\Omega_{\rm far}
=\frac1{S_m}\sum_{j\ge m}a_j|j\rangle_{\rm far},\qquad
\|R_{m,0}\|=S_m^{-1/2}.
\tag{3.1}
$$
这直接由一孔层中的原行 $(a_j)_{j\ge m}$ 得到，不是顺次幂逆或双 Fock 替身。

在高头张量远尾真空上，先用真正跨头块，再用这一首层逆。得到原物理算子
$$
\mathcal C_{n,m}
=B_{n,m}\otimes R_{m,0}
:(I-P)\mathcal F_m\otimes\mathbb C\Omega_{\rm far}
\longrightarrow P\mathcal F_m\otimes\mathcal H_1^{(m)}.
\tag{3.2}
$$
张量范数准确相乘，故
$$
\boxed{
\|\mathcal C_{n,m}\|=\frac{\|B_{n,m}\|}{\sqrt{S_m}},\qquad
\left|\|\mathcal C_{n,m}\|-
\sqrt{\frac{\sum_{j=n}^{m-1}(j+1)^{-4}}{S_m}}\right|
\le\frac{26\eta_{n-1}}{\sqrt{S_m}}.
}
\tag{3.3}
$$
源和目标均为原实际空间；这一计算仍不把它们自动归入某个实际窄源类。

## 4. 已付 $d^{3/4}$ 头宽对应的非零极限

对 $k\to\infty$，对递减函数 $x^{-4}$ 作积分夹逼得
$$
S_k=\sum_{j\ge k}(j+1)^{-4}
=\frac1{3k^3}\bigl(1+o(1)\bigr).
\tag{4.1}
$$
因此若 $n/m\to\vartheta\in(0,1)$，
$$
\frac{\beta_{n,m}^2}{S_m}
=\frac{S_n-S_m}{S_m}
\longrightarrow\vartheta^{-3}-1.
\tag{4.2}
$$
同时 (1.2) 给 $\eta_{n-1}/\sqrt{S_m}\to0$。
由 (3.3)，
$$
\boxed{
\|\mathcal C_{n,m}\|
\longrightarrow\sqrt{\vartheta^{-3}-1}.
}
\tag{4.3}
$$
取已经支付原源头旗所用的
$$
n=\lfloor3m/4-2\rfloor,\qquad H=2^n,
$$
便有
$$
\boxed{
\beta_{n,m}\sim\frac{\sqrt{37}}{9m^{3/2}},\qquad
\|\mathcal C_{n,m}\|\longrightarrow\sqrt{\frac{37}{27}}>0.
}
\tag{4.4}
$$
所以“跨头行趋零，再接一次原首层尾逆仍趋零”在这个原尺度上并不成立。一次尾逆准确抵消了其 $m^{-3/2}$ 主衰减。

## 5. 对当前真实测试路线的准确用途

固定测试伴随流的正耗散已经支付物理 $\|t_b(f)\|$ 与一整段 $v/e$ 能量，但其孔层是原巨大窗口 $b\asymp Q$。本文的 $R_{m,0}$ 只是一孔到真空的最小逆；它没有给那个巨大孔层的受限正逆一个统一界。

(4.4) 只排除一个不合法的费用简化：不能删掉实际高位一次下降主项，也不能仅凭它的原物理范数趋零，断言接尾逆后的整个反馈趋零。它不证明实际测试的端点费用坏增长，不证明纯高 $S_H^\dagger$ 反例，也不否定任何已付的同源完整右链或真实 $M_2$ 删除。

后续若控制原固定测试的跨头双链，必须使用同一个测试的伴随来源、弱误差或真实两费度量；一般高头输入的上述算子范数不能代替这些来源条件。
