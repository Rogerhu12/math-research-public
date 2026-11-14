# R133：真实 moving 系统的一阶角能量、分数阶与完整普通源

**已证明并实际完成。** 对[完整二维能量](R133-supplement-actual-moving-mean-full-energy.md)
的同一 $\alpha=3/4$、M256 accepted000 中心及其准确
$\nu=-2443457753738987/72057594037927936$，本篇支付整个 $[0,.238]$
上的一阶角正则。1528条真实径向闭盒、每盒4096个闭角单元、1013个真实
moving 接缝、全部允许 Fourier 变分和独立均值均保留。候选的256模支撑
没有用来截断变分或源。

记 $q=\sqrt{-K}$，并在各个真实 $r$ 上使用同一 Bessel 标度

$$
\|h\|_{s,r}^2=\sum_{m\in4\mathbb Z}(1+m^2)^s
\bigl(|(h_1)_m|^2+q(r)^2|(h_2)_m|^2\bigr),\quad0\le s\le1.
\tag{S.1}
$$

反射类中 $h_1$ 为奇函数、$h_2$ 为偶函数，后者的平均没有删除。全区间
及任意径向子区间的充分界为：

| 完整输入或源 | $H^0$ | $H^{1/6}$ | $H^{1/3}$ | $H^1$ |
|---|---:|---:|---:|---:|
| 正向任意允许初值 | 3.614669115 | 5.753713268 | 9.158574495 | 58.795833333 |
| 正向真实初始均值为0的子空间 | 2.333679075 | 2.746380083 | 3.232065470 | 6.199521694 |
| 正向完整 $L^1_rH^s$ 普通源 | 11.712299133 | 21.062791983 | 37.878233906 | 396.172980912 |
| 反向任意初值及完整普通源 | 47.305976121 | 65.729367615 | 91.327779729 | 340.389913451 |

小数均向上放宽；$H^{1/3}$ 列也可直接由两端列按
$C_{1/3}^3=C_0^2C_1$ 核算。初始均值为0只能在真实腰平面、转角整数1和
固定 $a(0)$ 已经支付时采用；沿径向的均值耦合始终存在。

实际仿射接缝另付正向 $H^1$ 小于 $2.181\cdot10^{-11}$、
$H^{1/3}$ 小于 $9.035\cdot10^{-13}$；反向相应小于
$3.395\cdot10^{-10}$ 和 $1.234\cdot10^{-11}$。

这是 moving 非线性方程自身在该近似中心的线性 Cauchy/source 合同。
中心的完整 PDE 残差仍须支付。若改用原物理 Jacobi，必须同时消费
[残差敏感变分桥](R133-supplement-residual-sensitive-moving-physical-Jacobi-bridge.md)，
不能仅凭本篇把近似中心当成真解。

## 1. 完整导数方程，不删除非局部列

沿用准确 moving 定理 M.9–M.12。写 $Q=(u,v)$、
$H=\operatorname{diag}(1,-K)$、$z=\langle h_2\rangle$、
$T_h=2u h_1+2Kv h_2$，则

$$
h_r=(dI+\gamma mJ)h_\phi+L_0h
-\beta I(T_h)Q_\phi+\gamma zJQ_\phi+f.
\tag{S.2}
$$

这里 $I=\partial_\phi^{-1}P_0$，其四重圆完整 $L^2$ 范数为 $1/4$；
$m=\langle v\rangle$，$J=\left(\begin{smallmatrix}0&K\\-1&0\end{smallmatrix}\right)$。
令 $w=h_\phi$。$K,\gamma,m,\beta$ 都只依 $r$，所以准确微分给

$$
\begin{aligned}
w_r={}&(dI+\gamma mJ)w_\phi+(L_0+d_\phi I)w
 +(L_0)_\phi h\\
&-\beta P_0(T_h)Q_\phi-\beta I(T_h)Q_{\phi\phi}
 +\gamma zJQ_{\phi\phi}+f_\phi.
\end{aligned}\tag{S.3}
$$

因此非局部项的导数不是被忽略，也不需要另假设高频截断。
$\langle w\rangle=0$ 是角微分的准确恒等式；它不意味着 $z=0$。

置

$$
E_0=\|H^{1/2}h\|_2,\quad E_1=\|H^{1/2}h_\phi\|_2,
\quad M=|z|,
$$
$$
R=\|H^{1/2}Q\|_\infty,\quad
L=\|H^{1/2}Q_\phi\|_\infty,\quad
L_2=\|H^{1/2}Q_{\phi\phi}\|_\infty.
\tag{S.4}
$$

对 (S.3) 的局部齐次部分，$HL_0$ 的非对角项在 Hermitian 能量中准确
相消。共同漂移经周期分部积分贡献 $-d_\phi/2$，而额外的
$d_\phi w$ 保留，故一阶能量两个实际对角是

$$
\begin{aligned}
G_{1,1}&=-\beta(1+3u^2+Kv^2)+d_\phi/2,\\
G_{1,2}&=\beta(1-u^2-3Kv^2)+K'/(2K)+d_\phi/2.
\end{aligned}\tag{S.5}
$$

其余项可以全部用较低阶能量和均值控制。令 $a=u,b=qv$，则
$a^2+b^2\le R^2$、$a_\phi^2+b_\phi^2\le L^2$。
$H^{1/2}(L_0)_\phi H^{-1/2}$ 的两个对角绝对值至多
$6|\beta|RL$，两个非对角绝对值至多 $2|\beta|RL$，故其算子范数
不超过 $8|\beta|RL$。再由 $P_0$ 是正交投影，

$$
\|P_0T_h\|_2\le2RE_0,\qquad
\|IT_h\|_2\le RE_0/2,
$$

而 $H^{1/2}JH^{-1/2}$ 是 $q$ 倍正交矩阵，得到完整三维正比较系统

$$
\frac d{dr}\begin{pmatrix}E_0\\M\\E_1\end{pmatrix}
\le
\begin{pmatrix}
g_0&\gamma qL&0\\
2|\beta m|R&c_0&0\\
|\beta|R(10L+L_2/2)&\gamma qL_2&g_1
\end{pmatrix}
\begin{pmatrix}E_0\\M\\E_1\end{pmatrix}
+\begin{pmatrix}F_0\\F_0/q\\F_1\end{pmatrix}.
\tag{S.6}
$$

这里 $g_0,c_0$ 是已付二维系统的准确对角，
$g_1=\max(G_{1,1},G_{1,2})$，
$F_j=\|H^{1/2}\partial_\phi^jf\|_2$。
反向取 $g_1^- =\max(-G_{1,1},-G_{1,2})$，原两行也用已付的反向
对角；所有非对角绝对值保留。因此 (S.6) 是真正完整的线性强源估计，
不是把普通源当作已含角原函数的特殊源。

## 2. 实际完整 $L_2$ 及径向传播

沿用完整零阶证书的真 $D=\langle1/v\rangle_\theta$、$R,L,m$ 和
全 primitive 尾。准确换角为 $\partial_\phi=Dv\partial_\theta$，从而

$$
u_{\phi\phi}=D^2v(v_\theta u_\theta+vu_{\theta\theta}),\qquad
v_{\phi\phi}=D^2v(v_\theta^2+vv_{\theta\theta}).
\tag{S.7}
$$

在同一个径向闭盒、同一个闭角单元内形成 (S.7)，再计算
$L_2^2=u_{\phi\phi}^2-Kv_{\phi\phi}^2$ 的上界。每个真实 Fourier
系数仍以准确 dyadic 三次 PPoly 和真实目标 $s=1/C_r$ 包络；有向直接
三角和分别支付到四阶的节点值，闭角余项含完整五阶 $A_0$ 费。
所有浮点四则误差沿用已经证明的显式逐频率误差，不对一个仅有零阶费用的
包络求形式导数。实际整个区间得到

$$L_2<386.321630062.\tag{S.8}$$

四个382行的实际计算完全覆盖1528条原共同分割。完整消费者按每一条
原节点、scalar germ、候选片、目标身份和真实参数核对，只把对应的新
三行矩阵连接到同一连续变分；没有在片界重新设均值或角导数。

逐盒 Arb 矩阵指数及径向有序乘法，正向所有子区间的充分矩阵为

$$
U_f\le\begin{pmatrix}
2.333679075&1.184573700&0\\
0.115288217&1.094830185&0\\
5.273567944&49.350148334&2.275410369
\end{pmatrix}.
\tag{S.9}
$$

反向相应为

$$
U_b\le\begin{pmatrix}
41.112611840&0.782257560&0\\
2.222866583&1.019840347&0\\
125.941389543&26.382968879&38.998656671
\end{pmatrix}.
\tag{S.10}
$$

这里仍用每盒对角与0取较大值的全非负矩阵积支付任意源插入点，
不是只求最远终点。保留有符号对角的终点矩阵另存原生报告。

## 3. $H^1$、分数阶与所有源插入点

给一个完整3乘3正上界 $U$。初始 $M\le E_0/q_i$ 后，
$(E_0,E_1)$ 的充分二维矩阵为

$$
T_i=\begin{pmatrix}
U_{00}+U_{01}/q_i&U_{02}\\
U_{20}+U_{21}/q_i&U_{22}
\end{pmatrix}.
\tag{S.11}
$$

以其 Frobenius 范数控制算子范数即可得到 $H^1$ 列，因为
$\|h\|_{1,r}^2=E_0^2+E_1^2$。普通源在任意位置使用全区间真实
$q_\min$，故相同计算完整控制 $L^1_rH^1_\phi$ 源积分。
对 $M_i=0$ 的真实边界子空间，只在 (S.11) 删除初始列系数
$U_{01}/q_i,U_{21}/q_i$；$U$ 的内部反馈保持原值。

对每一对真实输入、输出径向点，线性传播是同一个完整线性算子。
两个端点的加权 Fourier Hilbert 标度 (S.1) 是准确插值标度：对角权
$(1+m^2)^{s/2}$ 与固定 $r$ 的 $H^{1/2}$ 可同时对角化。因此
三线定理（先对有限 Fourier 和的稠密域，再由两端有界延拓）给

$$\|\mathcal U(r,t)\|_{H^s_t\to H^s_r}
\le C_0^{1-s}C_1^s,\quad0\le s\le1.\tag{S.12}$$

真实 $M_i=0$ 子空间在两个端点都由同一个 Fourier 投影给出，故同样
插值。对 ordinary source 先对每个插入点应用 (S.12)，再用 Minkowski
积分不等式，得到表中的完整 $L^1_rH^s$ 费用。零模在 (S.1) 中的权为1，
没有凭 $m\ne0$ 的估计把它删掉。

标准严格对称双曲 Cauchy 构造与已付有界非局部项给 $H^1$ 唯一解；
上述能量和稠密延拓给各 $0\le s\le1$ 的完整解算子。有限候选的角解析性
仅用来支付系数，未对解的 Fourier 支撑作有限限制。

## 4. 完整 moving 一阶接缝

记一处真实接口的物理跳界为 $\epsilon_u,\epsilon_v$，其完整角导数跳
$\epsilon_{u\theta},\epsilon_{v\theta}$ 从原 dyadic PPoly 左右迹准确求值，
逐模乘真正物理频率 $4j$ 再求和。已付零阶跳给 $\Delta_D$ 及两侧逆角差
$\Delta_\theta$。取两侧统一上界
$D_+,V,U_\theta,V_\theta,U_{\theta\theta},V_{\theta\theta}$，由
$Q_\phi=DvQ_\theta$ 的乘法差及逆角复合，得

$$
\begin{aligned}
J_{u\phi}\le{}&\Delta_DVU_\theta+D_+\epsilon_vU_\theta
+D_+V\epsilon_{u\theta}
+D_+(V_\theta U_\theta+VU_{\theta\theta})\Delta_\theta,\\
J_{v\phi}\le{}&\Delta_DVV_\theta+D_+\epsilon_vV_\theta
+D_+V\epsilon_{v\theta}
+D_+(V_\theta^2+VV_{\theta\theta})\Delta_\theta.
\end{aligned}\tag{S.13}
$$

实际三维跳向量为 $(J_0,J_M,\sqrt{J_{u\phi}^2+q^2J_{v\phi}^2})$。
角导数的平均准确为0，但 $J_M$ 仍采用完整零阶跳。在1013个接口逐项
支付后用同一个 $U_f,U_b$ 传播，得到开头的完整跳费。
分数阶跳还可由同一实际输出函数的 Fourier Hölder 不等式
$\|j\|_s\le\|j\|_0^{1-s}\|j\|_1^s$ 支付。

## 5. 实际文件与精简重建

执行源码为 `scripts/fourfold_codazzi_moving_sobolev_rows.py` 和
`scripts/fourfold_codazzi_moving_sobolev_complete.py`；完整原生证书是
`notes/2026-11-13-R133-moving-H1-alpha075-complete-native.json.gz`。
后者保存全部1528条原强系数行和1013个实际一阶跳，正常完成用时约34.78秒。

四个原强系数片为实际正常完成的382行片。遵根规则11，它们的大文件只在
本地保留，不重复入 Git。小记录
`notes/2026-11-13-R133-moving-H1-reconstruction-manifest.json` 保存所有原
header、source、kind、SHA、区间、完成状态及重算命令；
`scripts/fourfold_codazzi_moving_H1_reconstruction.py` 直接从完整证书抽取
未变数学行，可无损恢复四个原报告，已实际核对逐字节及 SHA 相同。
原文件没有删除或修改。

后续真正根图、完整正帽、真实 regular 方程和主体两端可逆性仍须联立。
本篇给它们可消费的完整强角 Cauchy/source 合同，不把一个初值传播界称为
已经解决的混合边值逆。
