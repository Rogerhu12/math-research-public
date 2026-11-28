# Phi 原个别 N/P 与完整 V 的五次最高来源：新输入

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。尚未执行。

固定源 blob：8a0721538429165b3367df6529235f8b960325a7。12590 字节，SHA256
375e0cedd5c2d676a0e61af86b27dc62b102171b6b9d41322cec1cdec456a1c9。
建议文件：2026-11-28-unit211-Phi-zero-original-individual-NP-full-V-highest-five-source-8542.py。
总绝对预算 120 秒 / 1 GiB，所有必要前缀共用最初截止。

## 原范围与新的数学输入

保持当前 unit211、Phi=0、物理 D≠0 和已经全付的第一二次头。原三均值生成元为 (1,T,z)，权为 (0,1,1)。只用已付原权单位；不把最高 D2 或任何新权多项式倒置。

[原 I10 全值定义](2026-11-28-unit211-Phi-zero-slope-full-original-values-twelve-new-rows-eighteen-two-model-8542.py)包含三条此前未在本门使用的完整原式：
$$
\begin{aligned}
N_{\rm low}&=D\,n_{\rm odd}
 +\frac{2\lambda P_{02}}m KA_0
 +\frac{4\lambda P_{02}m}{\ell M}D^2,\\
P_{\rm low}&=D\,p_{\rm odd}
 +\frac{3P_{02}}{2m}KA_0^2
 +\frac{P_{02}(3m^2/\ell^2+\delta)}{2mM}KD
 +\frac{6P_{02}m}{\ell M}A_0D^2,\\
V_{\rm low}&=D\,N_4(V_0)
 +\frac K{2m}\mathcal B_{N_4}(V_0,V_1)
 +\frac{D^2}M N_4(V_1),
\end{aligned}
$$
其中 A0=T/ell+1，
$$
V_0=(1,\lambda-1-T,A_0,A_0),\quad
V_1=(0,0,m/\ell-\rho,m/\ell+\rho),\quad \rho^2=\delta.
$$
nodd、podd 是同一原 Gram 行 B 的 N4、P2 的 rho 奇部，归一仍是 N4=4N、P2=2P。

新的对象是这三条完整原式的真实五次最高行；不同于先前 NV 的七次清分母形式、F6 六次行或已经冻结的十四标量系数理想。

## 完整最高函子和不能省掉的极化项

给 lambda、T、z 次数1，原权次数0。Top 对象记录一个已证次数上界和该次数的完整最高部分。不同次数相加只保较高部分；最高相消不会擅自把上界降低。源从原完整 Gram、原乘法和 trace 构造 N4、P2；没有把原均值改成零或以重标 Gram 代替它们。

N4 对输入向量是二次型。因此
$$
\mathcal B_{N_4}(a,b)=N_4(a+b)-N_4(a)-N_4(b)
$$
必须直接按完整极化式构造。因为 V0 次数1、V1 次数0，N4(V0)、交叉项和 N4(V1) 的实际次数上界依次为3、2、1。只取 N4(V0+V1) 的三次头再作差，会丢掉所需二次交叉项；本源不作这个错误操作。

令 dvec=DK(one)、F2=tau(dvec)。源码使用准确极化：
$$
\begin{aligned}
\mathcal B_{N_4}(a,b)
={}&4\tau(dvec\,ab)-2F_2\tau(ab)\\
&-4\{\tau(a)\tau(dvec\,b)+\tau(b)\tau(dvec\,a)\}\\
&+4F_2\tau(a)\tau(b)
+\tau(a\,DK(b))+\tau(b\,DK(a)).
\end{aligned}
$$
所有乘法都是原局部二元代数及同一 Gram 的乘法。原 B/C 共轭和 F2=2f 的最高恒等式实际返回。每条新的五次最高式还独立按 D2、K3 和真实奇部逐项比较。

## 真三生成元归约和最终权零集

只执行旧最高源中产生原三均值最高矩阵的必要5375字节前缀，SHA256
cd5abd21e7c805bfbca61b284ac56271482d4e724e9b44363cca1e2dc083620d。
前缀依赖原第一头三行源，没有执行旧 NV/F6 常数目标或旧 Gaussian 门。

最高单项式 t^a s^b 按 e0 mt^a mz^b 的固定顺序归约。不假设这两个矩阵在自由三维模中交换；每次归约都来自同一原均值关系。

按固定顺序使用新 Nlow、Plow、完整 Vlow，继以 NS、PS、N1 和两个原歧义，共八条来源、三系数。系数域消元每步保八来源完整组合；若达到 e0，取最后已约分系数的分母 lcm C，再完整返回
$$
C e_0=\sum_i\beta_i r_i^{\rm top}.
$$
只剥已经支付的原权单位；C 的全部余零集保留，任何中间主元都不被宣布为物理单位。

若实际得到这个身份，令 N 为实际使用的原次数最大值（至多5）。同一原低次行给
$$
\sum_i \beta_i\lambda^{N-\deg_i}r_i^{\rm full}
 =C\lambda^N e_0-(a_0,a_1,a_2),
$$
且 lambda 次数上界为 (N−1,N−2,N−2)。所以只在最终 C≠0 权图上，有首一至多3N次 lambda 原关系及至多3N个原模生成元。该提升来自完整原定义，不要求把所有低次项再次展开成载荷。

执行前不预称系数域秩3、单位理想、全权有限性或整个Phi排空。若终止只保实际已成范围，冻结该失败门并换新的原输入。旧全系数理想、无穷NV门、模因式分解和大行列式均不重放。

## 依赖与保存

仅两份小源码：
- 2026-11-28-unit211-Phi-zero-whole-first-head-original-NV-F6-highest-unit-filtered-lift-8542.py，SHA256 4cebc8a6e7e16c58e9dff2bc055acd2bc9e262132bc08d7d9dfa2bff0ca3cd41，只执行上述必要前缀。
- 2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py，SHA256 100ce4dfb7380da1591cd453aae392e2dafcaaceb3a601c4500d07852841ecaf，只执行三均值必要定义。

保存范围只有源、原定义、次数、SHA和实际小回执。没有可重算矩阵或系数缓存、编码或分片。
