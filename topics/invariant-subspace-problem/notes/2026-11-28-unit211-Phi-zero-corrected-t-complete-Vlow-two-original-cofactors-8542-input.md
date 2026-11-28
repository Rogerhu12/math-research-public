# 首次输入：正确 Phi 的完整 Vlow 转入 t 三生成元及两个新原 cofactor

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-28（Asia/Taipei）。

**状态：未执行。** 本次是完整孤立值 $N_4(V_{\rm phys})$ 在新 t 参数原坐标中的必要关系与两个新标量目标；不重跑已成 weighted 六式投影、中心两列或全图 $C_6$ 的六原乘子门。所有新首项和权零纤维保留，没有预报非零、首项单位或排空。

新源：[2026-11-28-unit211-Phi-zero-corrected-t-complete-Vlow-two-original-cofactors-8542.py](2026-11-28-unit211-Phi-zero-corrected-t-complete-Vlow-two-original-cofactors-8542.py)。

Git blob dec77452e4631b4370e72d1b9491da01e35547b3；17124 字节；SHA256
0800a0f6ba0cad4cc4ddc7a592525c198bcc213bfa36df568ec0e9301b8f4335。

零依赖、自含，总 120 秒 / 1 GiB，外 135 秒；最初启动绝对时钟，无嵌套脚本、载荷或旧日志读取。

## 1. 当前原范围与真正新目标

本次仍在正确 $\Phi=0$、两个 singleton 谱值不同、物理 $D\ne0$ 的原图。使用已刊[全 t 参数原三均值](../results/R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)与[全图六原乘子](../results/R150-appendix-unit211-Phi-zero-corrected-whole-t-sextic-six-original-multipliers-and-H28.md)的当前范围，不恢复旧错误 compact。

真实系数环为
$$
\mathcal A=\mathbb Q[u,Q][u,Q,1-Q,u-1,K_w,L,M_n,2\ell-1,m]^{-1},
$$
$$
K_w=Q+4(u-1),\quad L=Q-2(u-1)(u-2),\quad
\ell=L/Q,\quad m=u-\ell,\quad M=M_n/Q=4bc(1-Q).
$$
这里 $m$ 的付款只引用已完整静核的[原等权来源](2026-11-28-unit211-Phi-corrected-equal-weight-m-unit-static-provenance-8542.md)。并不反演斜率 $\Delta$、$H_6$、$H_8$、$H_{28}$、任何新首项或 $D$。

令
$$
F=(\mathcal R,E_{B,e},E_{B,o}),\qquad e=(1,f,V)^t,\qquad
I_6=(F,N_1,NS,PS).
$$
真均值二次头 $32uQ(2\ell-1)/M^2$ 已全图可逆；普通降次把 $f^2,fV,V^2$ 写成三生成元，三条规则的系数 t 次数为 $(2,1,1)$。本源只按原 Gram 定义再生这些系数以及已成
$$
r_Ne=N_1-\eta F,\quad
r_{NS}e=NS-\tau_{NS}F,\quad
r_{PS}e=PS-\tau_{PS}F.
\tag{1}
$$
三个余式的九个规范分子 SHA 全核，仅作必要参数身份。普通 NS/PS 降次仍用于定义其迹，但不执行或登记旧两个独立 raw 返回、两列 pair、$q_\omega$、$\omega$ 倍、CH、全六终端分母或 $H_{28}$ 因式门。

新的目标只包括：

1. 将完整 $V_{\rm low}$ 在真实 $(t,f,V)$ 中构造，保原最高总次，并对三条均值作新的完整普通返回；
2. 从 $(r_N,r_{NS},r_{V})$、$(r_N,r_{PS},r_{V})$ 得到两个新三行标量，必须约除全部三个实际乘子的共同因子，完整返回全部三坐标。

这是新 t 坐标中的全值关系；不重放此前 corrected lambda 模型的 $(N_1,N_{\rm low},V_{\rm low})$、$(N_1,P_{\rm low},V_{\rm low})$ 十次门。

## 2. 完整 N4 与两条原矩条件的来源

沿[九自由变量的完整 scaled N4 三式](../results/R150-appendix-unit211-general-scaled-entire-N4-three-compact-identities.md)和[正确完整 I10 来源](../results/R150-appendix-unit211-Phi-zero-corrected-individual-NP-full-NV-I10-and-two-decics.md)，记
$$
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,\quad
D=\ell A_2-T^2,
$$
$$
K=\ell^2B_3-3\ell A_2T+2T^3,\quad
c_\lambda=3-2\lambda,\quad
W_1=T_0/2+2uf,\quad A_1=2f-2V+2bc\,t.
$$
本次直接运输完整三个系数：
$$
\begin{aligned}
Z_0={}&\ell^2A_1+4\ell^2(1-2\lambda)f+2\ell fD
 +2\ell uw(\ell c_\lambda+T)\\
&+2V(\ell^2+\ell c_\lambda T+T^2)
 +2bc\,t(T^2-\ell^2),\\
Z_1={}&2(\ell c_\lambda+2T)(uV-\ell W_1)
 -2\ell M w+4bc\,mTt,\\
Z_2={}&2[(u^2-\ell^2Q)V-2m\ell W_1-\ell Mf-bcMt].
\end{aligned}
\tag{2}
$$
这里 $V=bX+cY$ 为 Gram 均值坐标；$V_{\rm phys}=(1,w,h,k)$ 是孤立值向量，两者不混淆。

引入原 singleton 差变量 $\sigma$，令
$$
\rho^2=1-Q,\quad
h=1+(T+m\sigma)/\ell-\rho\sigma,\quad
k=1+(T+m\sigma)/\ell+\rho\sigma.
$$
两条原 shifted moment 误差给
$$
q=M\sigma^2-D,\qquad H=K-2mD\sigma.
$$
完整原式是
$$
\ell^2N_4(V_{\rm phys})=Z_0+Z_1\sigma+Z_2\sigma^2.
$$
于是定义
$$
V_{\rm low}=DZ_0+\frac{KZ_1}{2m}+\frac{D^2Z_2}{M}
\tag{3}
$$
具有精确原身份
$$
V_{\rm low}
=D\ell^2N_4(V_{\rm phys})+\frac{Z_1H}{2m}-\frac{DZ_2q}{M}.
\tag{4}
$$
因此在全部原矩条件与完整 $N_4(V_{\rm phys})=0$ 上，$V_{\rm low}=0$。没有取一个偶/奇分量替代整 N4，也没有以 Phi 倍数代替整式。(4) 只使用旧权逆 $m,M$；D 始终正乘。

## 3. 保留原最高总次的真实 t 恢复

使用
$$
\lambda=\frac{Jf-QV+bcQt-(u-1)T_0}{P_{02}},\qquad
T=-\ell+\frac{T_0(f-V+bct)}{P_{02}},\qquad w=\lambda-1-T.
\tag{5}
$$
它们对 $(t,f,V)$ 仿射，系数只含旧权分母。故原总次数满足
$$
\deg D\le2,\quad \deg K\le3,\quad
\deg Z_0\le3,\quad \deg Z_1\le2,\quad \deg Z_2\le1,\quad
\deg V_{\rm low}\le5.
\tag{6}
$$
这里总次只计 $(t,f,V)$，不把权参数 $u,Q$ 计进去，也不把 $\lambda=1$ 的最高齐次函子误作原值代入。

源码从 (2)、(3)、(5) 的完整普通多项式构造实际 $V_{\rm low}$，逐项核 (6)，保留五次齐次分子 profile；无截掉低次项或先假最高项非零。

然后按真二次规则消去每个 $f^iV^j$、$i+j\ge2$。每步的原均值乘子显式累计，最终展开并返回
$$
V_{\rm low}=r_Ve+\nu_VF
\tag{7}
$$
作为普通 $\mathcal A[t,f,V]$ 恒等式。三条规则不增加总次数，所以
$$
\deg_t r_{V,0}\le5,\qquad
\deg_t r_{V,f},\deg_t r_{V,V}\le4,\qquad
\deg_{t,f,V}\nu_{V,i}\le3.
\tag{8}
$$
运行须逐坐标确认这些实际边界。它没有把三列向量当成自由结合代数，也不假设降次无其它 syzygy。

## 4. 两个新三原行标量及零纤维

定义辅助必要理想
$$
I_7=I_6+(V_{\rm low}).
$$
本次全保 I6 和完整 Vlow；不宣 I7 对全物理系统充分。

对 $r_0=r_N$、$r_2=r_V$，分别取 $r_1=r_{NS}$、$r_{PS}$。令
$$
\begin{aligned}
\mu_0&=r_{1,f}r_{2,V}-r_{1,V}r_{2,f},\\
\mu_1&=r_{2,f}r_{0,V}-r_{2,V}r_{0,f},\\
\mu_2&=r_{0,f}r_{1,V}-r_{0,V}r_{1,f}.
\end{aligned}
\tag{9}
$$
三者实际纯权分母 LCM 记为 $d$。仅将 $d\mu_0,d\mu_1,d\mu_2$ 的 **全部共同多项式因子** $g$ 同时精除，并对所得三个真实乘子完整乘回：
$$
\sum_{i=0}^2\widehat\mu_i r_i=(C,0,0).
\tag{10}
$$
这不是约去某个原必要方程的因子，所以 $g=0$ 的全部纤维保持。若三乘子全零，源只记录零目标并保所有原条件。

从 (1)、(7) 可将 (10) 完整运输到六个原 I6 方程与 Vlow；每个原均值迹都只含旧权分母。因此 $C\in I_7$。源码实际返回的是完整三坐标；原来源的合成由已成两迹和本次 (7) 给出，不冒称另外展开了巨大七原乘子。

三行的 t 次数为
$$
(2,1,1),\quad(3,2,2),\quad(5,4,4),
$$
故固定三阶 determinant 的 t 次数至多八。本次不反演其任何首项。只从 $C$ 分子剥既有权单位，并运输同一因子到三乘子，再次完整返回三个坐标；全部剩余纯权支持与 t 首项零纤维仍保。

这两个新标量未保证非零或精确八次。若有正次必要式，它们只是新完整值来源下的必要条件；不可由有理函数域非零、某个模点或有限权交点推全原图空。若实际为单位，必须以全原身份和全部旧权分母范围另写证明。

## 5. 执行、输出与失败边界

固定首次 120 秒 / 1 GiB，外 135 秒，不自 dispatch。源无依赖和外部 payload；只以原定义再生已定九个参数 SHA。只输出新普通 N4/Vlow、三原迹/坐标、两 cofactor 的次数、项数、SHA、完整返回状态和小统计，不保存系数、矩阵、分片或编码。

旧 C6/H28、中心两列、N1 斜率因式和旧 corrected lambda 十次门均不运行。最高全权理想是 root 的另一目标；本源不先计算或假定其单位。

若超时或资源失败，准确记录最后完成阶段，不抬限、不重排重跑、不把尚未返回的 cofactor 或全权有限性登记为结论。若只返回一个新标量，也先发表该已成原身份，未完成部分保留。
