# R152：固定 h 的最高第四 action 与 Sturm–Liouville 二次型的准确等价

日期：2026-11-15。**已证明。** 本稿只有纸面推导，没有新原式评价、profile 积分或研究计算。

依据 [R137](R137-real-fast-pulse-positivity-and-acceleration-PSD.md)、[R140](R140-full-action-multiplier-equivalence-for-real-cost-positivity.md)、[R141](R141-affine-character-acceleration-covariance-and-J-positivity.md) 与 [R148](R148-sharp-one-dimensional-highest-action-positivity.md)。与 R148 固定 k、变化 h 的门互补，这里固定 h、允许 k 任意转向，并给出这一真实一维路径类上的必要充分判据。

结论仅针对完整最高导数 action 的这个子类；不把它当作全部水平路径、低阶耦合或真实第四成本半群的正性判据。

## 1. 真实路径与完整系数

令 $\lambda$ 为 R141 的实仿射字符，满足

$$
\lambda(\mathcal R_8)=0,\qquad
\lambda\circ\mathsf P_{H,d}=H^\sigma\lambda,
\qquad H>0,\ d\in\mathbb R.
\tag{1}
$$

$\sigma\in\mathbb Z$。协变本身不要求 $\lambda$ 正；只有把本稿的门施加到真实成本闭锥的正泛函时，才使用 R137 的非负最高 action 结论。

完整正规第四层为

$$
L_4^\lambda
=A_{hh}^\lambda a^2+A_{hk}^\lambda ab+A_{kk}^\lambda b^2
+(H_1^\lambda u+H_2^\lambda w)(ub-wa)
+\widehat Q_4^\lambda(S;u,w),
\tag{2}
$$

其中

$$
S=(h,k,\omega),\qquad
u=h_s,\ w=k_s,\ a=h_{ss},\ b=k_{ss}.
$$

这里必须保留完整

$$
\widehat Q_4=Q_4^v-D_0P_{3v}-\mathcal B_{m_2}(N_2).
\tag{3}
$$

不能用未正规化的速度四次项或 pure 投影代替 (3)。

固定 $h=H>0$，令 $k=k(s)$ 任意光滑变化，并准确设置

$$
\omega(s)=\omega_*+\frac{k(s)-k_*}{2H}.
\tag{4}
$$

于是 $\omega_s=k_s/(2h)$ 是真实水平约束，而不是把 $\omega$ 错误固定。R141 的平移不变性使所有已取 $\lambda$ 的正规最高层系数独立于 $\omega$。其缩放协变和 R148 式 (2) 给

$$
A_{kk}^\lambda(H,k,\omega)=H^\sigma c(k),
\qquad
[w^4]\widehat Q_4^\lambda((H,k,\omega);0,w)
=H^\sigma e(k),
\tag{5}
$$

其中 $c,e$ 为实光滑函数。因为 $u=a=0$，混合加速度项、其余加速度项和面积项都严格消失，故

$$
\boxed{
L_4^\lambda\big|_{h=H}
=H^\sigma\left[c(k)(k'')^2+e(k)(k')^4\right].
}
\tag{6}
$$

$H^\sigma>0$，不改变符号。下文给 (6) 的准确判据，同时处理端点、转向点和无穷多个单调弧。

## 2. 一维等价定理

令 $J\subseteq\mathbb R$ 为开区间，$c,e\in C(J;\mathbb R)$。对任意有限 $L>0$、在两端开邻域分别为常数的 $k\in C^\infty([0,L];J)$，定义

$$
\mathscr A[k]
=\int_0^L\left[c(k(s))(k''(s))^2
+e(k(s))(k'(s))^4\right]ds.
\tag{7}
$$

左右常值可以不同。定义实二次型

$$
\mathscr Q[\psi]
=\int_J\left[\frac49c(x)(\psi'(x))^2+e(x)\psi(x)^2\right]dx,
\qquad \psi\in C_c^\infty(J;\mathbb R).
\tag{8}
$$

**定理。** 下列条件等价：

1. 对所有上述真实有限时间平端 k，$\mathscr A[k]\ge0$；
2. 对所有 $\psi\in C_c^\infty(J;\mathbb R)$，$\mathscr Q[\psi]\ge0$。

同一个判据允许任意有限或无限多个转向点。必要性中只需使用单调的平端路径；充分性覆盖所有路径。

(8) 是形式 Sturm–Liouville 算子

$$
\mathscr L\psi=-\frac49(c\psi')'+e\psi
\tag{9}
$$

的非负二次型条件。定理不要求预先选择算子的自伴边界实现，也不依赖谱论结果；下面直接证明。

## 3. 一个单调弧上的准确换元

设 $(s_-,s_+)$ 是集合 $\{s:k'(s)\ne0\}$ 的一个连通分支。$k'$ 在该弧上符号固定；设 k 的像为 $(\alpha,\beta)$，按从小到大排列。

在状态变量 $x=k(s)$ 中，定义

$$
v(x)=|k'(s(x))|>0,\qquad
\psi(x)=v(x)^{3/2}.
\tag{10}
$$

正向和反向弧均有

$$
v_x=\frac{k''}{v},\qquad
\psi_x=\frac32\frac{k''}{\sqrt v},
\qquad |dx|=v\,ds.
\tag{11}
$$

因此准确得到

$$
\int_{s_-}^{s_+}(k'')^2ds
=\frac49\int_\alpha^\beta(\psi_x)^2dx,
\qquad
\int_{s_-}^{s_+}(k')^4ds
=\int_\alpha^\beta\psi^2dx,
\tag{12}
$$

并且

$$
\boxed{
\int_{s_-}^{s_+}\left[c(k)(k'')^2+e(k)(k')^4\right]ds
=\int_\alpha^\beta
\left[\frac49c(x)\psi_x^2+e(x)\psi^2\right]dx.
}
\tag{13}
$$

没有假设 k 单调递增；下降弧的两个方向符号在 (11) 中正确抵消。

在弧的两端，由 $k'$ 连续及分支的极大性，$v\to0$。两端若落在全路径端部，也由平端条件给出同一结论。式 (12) 说明 $\psi,\psi_x\in L^2(\alpha,\beta)$，其一维 Sobolev 迹为零。因此

$$
\psi\in H_0^1(\alpha,\beta).
\tag{14}
$$

在内部 $\psi$ 光滑；不要求它在状态端点具有普通光滑零延拓。

## 4. 零速度集合与可数单调弧：充分性

设 (8) 对全部光滑紧支撑测试函数非负。固定任一真实平端 k。

其状态像是 J 内的紧集，所以 c,e 在像的一个紧邻域内有统一界。任意单调弧的 $[\alpha,\beta]$ 也在这个紧邻域中。二次型 (8) 在每个 $H_0^1(\alpha,\beta)$ 上连续；通过零延拓和标准光滑稠密逼近，非负性从 $C_c^\infty(J)$ 延续到 (14)。故每个弧的 (13) 均非负。

还需说明没有漏掉零速度集合

$$Z=\{s:k'(s)=0\}.$$

对 $g=k'\in C^1$，若某个 $s\in Z$ 满足 $g'(s)=k''(s)\ne0$，则该零点由局部严格单调性成为 Z 的孤立点。这样的点至多可数。因此

$$
k''=0\quad\text{在 Z 上几乎处处}.
\tag{15}
$$

$k'=0$ 在 Z 上处处成立，所以 (7) 的整个被积式在 Z 上几乎处处为零。这也覆盖带正测度的零速度集合、任意常值平台和累积转向点。

开集 $[0,L]\setminus Z$ 是至多可数个互不交单调弧的并。由于

$$
\int_0^L\left(
|c(k)|(k'')^2+|e(k)|(k')^4
\right)ds<\infty,
\tag{16}
$$

各弧的积分绝对可加，不能发生依赖排列的抵消。由 (15)、(16)，

$$
\mathscr A[k]
=\sum_{\text{单调弧}}\mathscr Q[\psi_{\mathrm{arc}}]\ge0.
\tag{17}
$$

这是可数弧的实际等式，而不是先把路径假设成只有有限个转向再忽略极限。

## 5. 从一个负测试函数构造有限时间的真实平端路径

现在反证必要性。假设存在实 $\psi\in C_c^\infty(J)$ 使 $\mathscr Q[\psi]<0$。

先取 $|\psi|\in H^1$。弱导数在几乎处处满足 $|(|\psi|)'|=|\psi'|$，故

$$
\mathscr Q[|\psi|]=\mathscr Q[\psi]<0.
$$

选择一个紧区间 $[a,b]\subset J$，使其内部包含 $\operatorname{supp}\psi$。用非负光滑核作足够小的卷积，可得到非负

$$
f\in C_c^\infty((a,b)),\qquad \mathscr Q[f]<0.
\tag{18}
$$

这里用的只是 $H^1$ 收敛和 c,e 在 $[a,b]$ 上有界；没有假定 c 已非负。

直接把 $f^{2/3}$ 作为 k 的速度可能使行程时间无穷。下面用一条固定实际平端路径产生端帽，准确支付这个问题。

### 5.1 固定的有限时间平端模型

取

$$
\rho(t)=
\begin{cases}
\exp\!\left(-\dfrac1{t(1-t)}\right),&0<t<1,\\
0,&t=0,1,
\end{cases}
$$

并定义

$$
\kappa(t)=a+(b-a)
\frac{\int_0^t\rho(\tau)d\tau}{\int_0^1\rho(\tau)d\tau},
\qquad 0\le t\le1.
\tag{19}
$$

$\kappa$ 光滑，内部严格递增，所有正阶导数在两端为零。把它分别延拓为常数 a,b，便得到真实开平端路径。

在状态区间内令

$$
\psi_*(x)=
\left[\kappa'\!\left(\kappa^{-1}(x)\right)\right]^{3/2},
\qquad a<x<b.
\tag{20}
$$

它在内部光滑且严格正。由第 3 节的准确换元，

$$
\psi_*\in H_0^1(a,b),\qquad
\int_a^b\psi_*^{-2/3}\,dx=1.
\tag{21}
$$

(21) 特别给出一个在状态端点趋零、却仍能用有限时间行进的端帽。其状态变量表达式不需要在 a,b 普通光滑。

### 5.2 正端帽加入及真实反函数

令

$$
\psi_\varepsilon=f+\varepsilon\psi_*,\qquad \varepsilon>0.
\tag{22}
$$

它在 $(a,b)$ 内严格正，且在两个固定端邻域准确等于 $\varepsilon\psi_*$。又有

$$
\psi_\varepsilon\longrightarrow f
\quad\text{于 }H_0^1(a,b),
$$

所以对充分小、仍严格正的有限 $\varepsilon$，

$$
\mathscr Q[\psi_\varepsilon]<0.
\tag{23}
$$

定义真实时间坐标

$$
s_\varepsilon(x)=\int_a^x\psi_\varepsilon(y)^{-2/3}dy,
\qquad
T_\varepsilon=s_\varepsilon(b).
\tag{24}
$$

由 $\psi_\varepsilon\ge\varepsilon\psi_*$ 与 (21)，

$$
0<T_\varepsilon\le\varepsilon^{-2/3}<\infty.
\tag{25}
$$

令 $k_\varepsilon$ 为 (24) 的反函数。内部满足

$$
k_\varepsilon'=\psi_\varepsilon(k_\varepsilon)^{2/3}>0.
\tag{26}
$$

它在端点具有真正的光滑平坦接入：因为 f 在 a 的固定邻域为零，

$$
s_\varepsilon(x)=\varepsilon^{-2/3}\kappa^{-1}(x),
\qquad
k_\varepsilon(s)=\kappa(\varepsilon^{2/3}s)
\tag{27}
$$

在左端邻域准确成立。同理，在右端邻域，

$$
k_\varepsilon(s)=
\kappa\!\left(1-\varepsilon^{2/3}(T_\varepsilon-s)\right).
\tag{28}
$$

(19)、(27)、(28) 使其两端所有正阶 s 导数为零。左右再接任意正长度的常值段，即为定理要求的 $C^\infty$ 开平端路径，且不会增加 action。

按 (13)，

$$
\mathscr A[k_\varepsilon]
=\mathscr Q[\psi_\varepsilon]<0.
\tag{29}
$$

这与路径非负性矛盾，完成必要性。没有把 $\varepsilon\to0$ 的无限时间极限当作实际路径；负成本已由某个有限 $\varepsilon$、有限 $T_\varepsilon$ 的光滑路径实现。

## 6. 两个直接后果

首先，二次型非负必迫 $c(x)\ge0$。若 $c(x_0)<0$，在其负邻域取

$$
\psi_\delta(x)=f((x-x_0)/\delta)
$$

且 f 非常值光滑紧支撑，则导数项为负的 $O(\delta^{-1})$，势项仅为 $O(\delta)$，小 $\delta$ 时违反 (8)。这也独立恢复 R137 的这个一维 PSD 门。

其次，若 $c\equiv0$，(8) 恰等价于 $e\ge0$ 逐点。若 $c$ 非零，不能把势 e 的逐点非负当作必要条件。例如

$$
c(x)=1,\qquad e(x)=x^2-\frac23
$$

给出准确平方

$$
\mathscr Q[\psi]
=\int_{\mathbb R}
\left(\frac23\psi'(x)+x\psi(x)\right)^2dx
\ge0,
\tag{30}
$$

虽然 e 在零的邻域为负。式 (30) 由紧支撑分部积分直接得到，说明加速度项与速度四次项必须作为完整 action 耦合处理。

在 R141 权 $\sigma=-2$ 的已发加速度支撑中，$c(k)=\lambda(J_6)=c_0$ 是常数。因此该权的固定 h 门为

$$
\boxed{
\int_{\mathbb R}
\left[\frac49c_0(\psi')^2+e(k)\psi^2\right]dk\ge0
\quad\text{对全部 }\psi\in C_c^\infty(\mathbb R).
}
\tag{31}
$$

本稿没有计算完整 e(k)，也没有从已有 J 或 pure 证据推断其符号。任何以后消费 e 的原式任务仍须保留 (3)。

## 7. 适用范围与真实几何

对每一条构造，h 恒为 H，k 的像在一个固定紧状态区间内，$\omega$ 由 (4) 准确确定。因此真实水平约束全程成立；frame 和中心位移继续按原 ODE 积分，不在此强行重置。

若只允许某一共同物理 profile 区间，应先使这条有限状态路径的整个 $\xi+\omega$ 范围远离零；可以对已选择的有限构造再选共同物理区间，或把本定理限制到本来满足该条件的状态区间 J。这里不保证任何事先指定的任意小物理区间都容纳全部辅助端口控制。真实 frame、矩阵、第三成本等补偿的作用范围仍按 R137/R140 保留。

对于真实成本正字符，R137 已使每条开平端路径的最高 action 非负，因此 (8) 是必要条件；对固定 h 的最高层路径类，定理证明它同时充分。

它没有支付一般 h,k 联动、面积项、低阶层、同一八矩乘子、完整第四 ruling、实际半群逆元或有限等距族。允许的时间长度无统一上界；(25) 只保证每个用来反证的实际路径时间有限。

