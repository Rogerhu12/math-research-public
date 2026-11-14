# 两个完整 mean 根的有理差界

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted）
日期：2026-11-12

**状态：已证明，实全角条件工具；本记录没有新增数值结论。**
本工具用于比较原物理插值与 carrier 插值的完整 mean，保留 R64 的一般
实正分支，不要求 R33 的小 Wiener 球。它可收紧
$|c_B-c_A|\le |c_A|+|c_B|$，并与已付 $\int w\,dr=I_{00}+I_{01}$ 相乘；
不改变任一候选，不构造新的根，也不把相位采样作为全角证书。

## 1. 完整实根和记号

在一个固定真实径向点，$w>0$，置 $z=w^2$、$E=1+z$。
对实周期非均值场 $\overline K,P$，置 $T=P_\theta$，$K=c+\overline K$，
并定义

$$
Y=1+K,\qquad
A=1-zP^2,\qquad
D=E-zY^2-EzP^2=EA-zY^2,\qquad
L=Y+ET.
\tag{M.1}
$$

完整连接转角及其归一平均为

$$
 \Gamma(c,\overline K,P,T)
 =\frac{1+zYT/A}{\sqrt D},\qquad
 \mathcal M(c,\overline K,P,T)
 =\frac{\langle\Gamma\rangle-1}{z}.
 \tag{M.2}
$$

均值括号是整个真实角圆周上的归一平均，平方根为正实支。
这就是 R30/R64 使用的完整转角条件，既未投影非线性分母，也未删除 mean。
假设两组数据 $i=A,B$ 各有同一允许分支内的精确根 $c_i$，满足

$$
 \mathcal M(c_i,\overline K_i,P_i,T_i)=0,\qquad
 A_i\ge a_*>0,\quad D_i\ge d_*>0,\quad L_i\ge l_*>0
 \quad\hbox{对所有 }\theta .
 \tag{M.3}
$$

$\overline K_i$ 的角均值为零，$T_i$ 作为角导数也均值为零。
上述严格界必须覆盖真实整叶和完整根区间；仅保存某一近似 root 的值不够。
所有后续差记作 $\delta X=X_B-X_A$。

## 2. 不要求中间状态也是根的安全路径

取全部状态的共同线段

$$
 (c_t,\overline K_t,P_t,T_t)
 =(1-t)(c_A,\overline K_A,P_A,T_A)
  +t(c_B,\overline K_B,P_B,T_B),\qquad 0\le t\le1.
 \tag{M.4}
$$

此路径一般不满足 mean 方程，但它始终位于需要的实正域。准确展开给

$$
\begin{aligned}
 A_t&=(1-t)A_A+tA_B+zt(1-t)(\delta P)^2,\\
 D_t&=(1-t)D_A+tD_B+
 zt(1-t)\bigl((\delta K)^2+E(\delta P)^2\bigr),\\
 L_t&=(1-t)L_A+tL_B.
\end{aligned}
\tag{M.5}
$$

故全路径 $A_t\ge a_*$、$D_t\ge d_*$、$L_t\ge l_*$。
同时 $D_t=E-zY_t^2-EzP_t^2\le E$。
因此可以在这条路径对完整函数 (M.2) 使用微积分基本定理，不需要
先证明一个未经核销的中间根族。

## 3. 准确微分、零平均及差恒等式

令

$$
 B_K=\frac{L}{D^{3/2}},\qquad
 B_T=\frac{Y}{A\sqrt D},
$$

$$
 B_P=\frac{EP(1+zYT/A)}{D^{3/2}}
       +\frac{2zPYT}{A^2\sqrt D}.
 \tag{M.6}
$$

对归一 integrand $(\Gamma-1)/z$ 求导，关于 $K,P,T$ 的偏导分别为
$B_K,B_P,B_T$。特别地

$$
 \mathcal M_c=\langle B_K\rangle>0.
 \tag{M.7}
$$

**偏导核对。** 关于 $K$ 微分的两个项相加后，分子是
$T(D+zY^2)+AY=A(ET+Y)=AL$，从而恰为 $LD^{-3/2}$。
关于 $P$ 微分分别作用于 $A^{-1}$ 和 $D^{-1/2}$，给 (M.6) 的两个
完整项；关于 $T$ 微分直接给 $B_T$。没有未保留的 $z$ 因子或 $1/w$ 分母。

两端 mean 方程均为零，于是

$$
 \delta c\int_0^1\langle B_K(t)\rangle\,dt
 =-\int_0^1\left\langle
 B_K(t)\delta\overline K+B_P(t)\delta P+B_T(t)\delta T
 \right\rangle\,dt.
 \tag{M.8}
$$

由于 $\langle\delta\overline K\rangle=\langle\delta T\rangle=0$，右侧可
**准确地**替换为

$$
 -\int_0^1\left\langle
 (B_K(t)-1)\delta\overline K+B_P(t)\delta P+
 (B_T(t)-1)\delta T\right\rangle\,dt.
 \tag{M.9}
$$

这是固定的零平均相消，不是用不同 Fourier 模式的取样相消。它特别避免
把背景处两个恒为一的导数系数收费两次。$\delta T$ 是真实角导数差，
其范数仍须实际支付，不能免费从 $\delta P$ 的零阶范数推出。

## 4. 不用平方根求值的完整有理门

设同一整叶上已有非负上界

$$
 z\le z_*,\quad E_*=1+z_*,\quad
 |K_t|\le k,\quad |P_t|\le p,\quad |T_t|\le t_0.
 \tag{M.10}
$$

例如 $k$ 可取两端
$\|\overline K_i\|_\infty+|c_i|$ 上界的最大值；
$p,t_0$ 也取各自端点完整角范数的最大值。凸组合自动保留它们。
令

$$
 d_0=\min(1,d_*),\qquad
 u=z_*(2k+k^2+E_*p^2).
 \tag{M.11}
$$

则 $|D_t-1|\le u$。以下全为精确有理表达式：

$$
\begin{aligned}
 C_K&=\frac{k+E_*t_0}{d_0^2}+\frac{3u}{2d_0^3},\\
 C_T&=\frac{k+z_*p^2}{a_*d_0}+\frac{u}{2d_0^2},\\
 C_P&=\frac{E_*p(1+z_*(1+k)t_0/a_*)}{d_0^2}
       +\frac{2z_*p(1+k)t_0}{a_*^2d_0}.
\end{aligned}
\tag{M.12}
$$

它们满足 $|B_K-1|\le C_K$、$|B_T-1|\le C_T$、$|B_P|\le C_P$。
并且

$$
 \int_0^1\langle B_K(t)\rangle\,dt\ge \frac{l_*}{E_*^2}.
 \tag{M.13}
$$

**证明。** 写
$B_K-1=(K+ET)D^{-3/2}+(D^{-3/2}-1)$。
在 $D$ 与 $1$ 之间使用单变量均值定理，
$|D^{-3/2}-1|\le(3/2)u\,d_0^{-5/2}$。
因为 $0<d_0\le1$，用整数幂 $d_0^{-3}$ 包围它；
同理 $D^{-3/2}\le d_0^{-2}$。

又
$B_T-1=K/(A\sqrt D)+(A^{-1}-1)/\sqrt D+
(D^{-1/2}-1)$，
其中 $A^{-1}-1=zP^2/A$，
$|D^{-1/2}-1|\le u\,d_0^{-3/2}/2\le u/(2d_0^2)$。
这给 $C_T$。对 (M.6) 的 $B_P$ 各项取绝对值、使用 $|Y|\le1+k$，
再取同一安全整数幂，即得 $C_P$。
最后 $L\ge l_*$、$D\le E\le E_*$ 给
$B_K\ge l_*/E_*^{3/2}\ge l_*/E_*^2$，证明 (M.13)。证毕。

因此，若完整实角范数差满足

$$
 \|\delta\overline K\|_\infty\le e_K,\qquad
 \|\delta P\|_\infty\le e_P,\qquad
 \|\delta T\|_\infty\le e_T,
$$

则

$$
 \boxed{|c_B-c_A|
 \le \frac{E_*^2}{l_*}(C_K e_K+C_P e_P+C_T e_T).}
 \tag{M.14}
$$

可以将 (M.14) 与原有效界 $|c_A|+|c_B|$ 取较小者，因为两者控制的是
**同一个根差**。这没有更换候选，也没有对不同候选的残差逐点择优。

## 5. 接现有 carrier primary 的准确单位

PA/CF 的共同源叶已保存：

- 完整 mean 根的绝对上界，以及 real_S_lower、real_D_lower、real_L_lower；
  这里 real_S 就是 (M.1) 的 $A$；
- 同一真实 $r,w$，并以物理 $r$ 为独立变量；
- 全部实非均值 cosine 系数 H、Kbar、Kbar_r，没有省去任一原 20 个模式。

于是可只用标准库有理算术取两侧 real 下界的最小值为 $a_*,d_*,l_*$。
从这些实系数的完整绝对和得到 $e_K$；同一 $r,w$ 下

$$
 \delta P=\frac{\partial_\theta\delta H}{rw},\qquad
 \delta T=\frac{\partial_{\theta\theta}\delta H}{rw}
 \tag{M.15}
$$

给 $e_P,e_T$，所有频率 $m$ 和 $m^2$ 都实际计入。
两侧场幅度 $k,p,t_0$ 同样用完整系数与真实正下端计算。
这里用 Fourier 绝对和控制实 supremum，未将点态和交换成逐模径向 supremum。

在有限真实叶上，(M.14) 与
$\omega_I=I_{00,I}+I_{01,I}=\int_Iw\,dr$ 相乘，给完整 mean 高度差增量。
沿叶排序累积并只选一个左端常数，即得到整个替换区间的高度偏移界。
对原 source-x 候选，若没有同位置的完整非均值场差输入，应继续使用原
已付根绝对界或先恢复其实际场；本工具不从只有 $J$ 系数的文件倒推出
不存在的高度数据。

本引理只给实全角 mean 差。它不提供新的复杂角条带逆、外 Green/Schur、
空间水平展开误差、reach 或握持幅度。既有简单 mean ledger 的三条绝对界
仍有效；后续若应用本引理，需另存实际输入、全部有理门和新输出，
不能悄悄把未运行的收紧写回旧证据。

相关完整工具：
[R30](../results/R30-source-cut-to-cartesian-boundary-traces.md)、
[R64](../results/R64-general-outer-mean-and-compatible-defect.md)、
[carrier 几何接口](2026-11-12-tail-carrier-mean-and-geometric-interface.md)。
