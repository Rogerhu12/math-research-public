# R50. 固定槽圆弧控制空间在完整 C4 相容空间中的稠密性

维护会话：Astra-held10-7322d0de-20261118。

**状态：已证明。** 本条证明定义函数空间的 $C^4$ 稠密性。[R44](R44-circle-trace-controls-complete-two-missing-directions.md) 已区分完整零迹空间与有限 raw 空间，[R47](R47-fixed-slot-nested-circle-homotopy.md) 已证明固定槽有限空间的独立性和嵌套；本条补上其端点空间之并的闭包。没有执行新核心、积分、BVP、尾或 metric，也不证明实际正性域、Jacobian 逆界或非线性解的存在。

## 1. 空间、窗口与结论

令

$$
\ell=\frac{2\pi}{3},\qquad L=\frac\pi3,\qquad \phi_0=L,
\qquad 0<a<L.
$$

在每个周期以 $d=\phi-\phi_0\in[-L,L]$ 为局部坐标；$I$ 表示闭弧 $|d|\le a$ 及其三重重复。所有函数为实值。在 $2\pi$ 圆周上取

$$
\mathcal C=\{f\in C^4:f(\phi+\ell)=f(\phi),\ f(2\phi_0-\phi)=f(\phi)\},
\qquad
\|f\|_{C^4}=\max_{0\le k\le4}\sup_\phi|f^{(k)}(\phi)|.
$$

记 $x(\phi)=\cos3\phi$，$e=(1,x)^\mathsf T$，归一化积分为

$$
\langle g\rangle=\frac1{2\pi}\int_0^{2\pi}g(\phi)\,d\phi.
$$

对三重周期函数，这也等于一个长度为 $\ell$ 的周期上的平均。定义闭子空间

$$
\mathcal X=\{f\in\mathcal C:\langle f\rangle=\langle fx\rangle=0\},
\qquad
\mathcal X_0=\{f\in\mathcal X:f|_I=0\},
$$

$$
\mathcal X_{\rm circ}=\{f\in\mathcal X:(f+f'')|_I\text{ 为常数}\}.
$$

固定 $W\in\mathcal C$，要求

$$
W|_I=0,\qquad W(\phi)>0\quad(\phi\notin I).
\tag{1}
$$

不要求 $W$ 超过 $C^4$，也不要求其在弧边有指定的有限阶渐近式。式 (1) 的“整个弧外严格正”比 R35、R47 只为 Gram 可逆而使用的“某个弧外开区间严格正”更强；当前 R44 九次 smoothstep 的 $W=1-\chi$ 满足 (1)：其过渡多项式的导数为 $630s^4(1-s)^4>0$（$0<s<1$）。若窗口还在别处为零，本条不能据此申领对上述完整 $\mathcal X_0$ 的稠密性。

以真积分定义固定矩阵及 raw 列：

$$
G=\langle W e e^\mathsf T\rangle,\qquad
\binom{a_j}{b_j}=G^{-1}\left\langle W\cos(3j\phi)e\right\rangle,
$$

$$
B_j=W\bigl(\cos(3j\phi)-a_j-b_jx\bigr),\qquad j\ge2.
\tag{2}
$$

**定理。** 在上述同一 $C^4$ 拓扑下：

$$
\boxed{\overline{\bigcup_{N\ge2}\operatorname{span}\{B_2,\ldots,B_N\}}^{\,C^4}
=\mathcal X_0.}
\tag{3}
$$

固定 R44 的两条迹列，并按 R47 记 $T=S_A-S_B$、$U=S_B$。令

$$
\mathcal E_M=\operatorname{span}\{B_2,\ldots,B_{M-2},T,U\},\qquad M\ge8.
$$

则

$$
\boxed{\overline{\bigcup_{M\ge8}\mathcal E_M}^{\,C^4}
=\mathcal X_{\rm circ}.}
\tag{4}
$$

而且对每个 $f\in\mathcal X_{\rm circ}$，可取逐层近似 $f_M\in\mathcal E_M$ 使 $f_M\to f$ 于 $C^4$，并对每个 $M$ 精确保留两个迹值

$$
t(f)=f(\phi_0)+f''(\phi_0),\qquad u(f)=f(\phi_0).
\tag{5}
$$

两低矩也在每个有限层精确为零。这里的 $T$ 是迹函数，周期已另记为 $\ell$。

## 2. 固定低矩校正是连续算子

式 (1) 使 $G$ 正定：对非零 $z\in\mathbb R^2$，

$$
z^\mathsf TGz=\langle W(z_0+z_1x)^2\rangle>0.
$$

弧外含开区间，$x$ 在其中不恒定；非零一次多项式不可能在该区间恒零。因此 $G^{-1}$ 存在，且不依赖截断阶数。

记 $m(g)=\langle ge\rangle$，定义矩校正

$$
\mathcal Qg=g-W e^\mathsf T G^{-1}m(g).
\tag{6}
$$

这是 $\mathcal C\to\mathcal C$ 的连续线性算子：矩泛函由 $C^0$ 范数控制，而 $W$、$Wx$ 都是固定 $C^4$ 函数。直接积分给

$$
m(\mathcal Qg)=0,\qquad
\mathcal Qg=g\quad(g\in\mathcal X),
\qquad \mathcal QW=\mathcal Q(Wx)=0.
\tag{7}
$$

在闭弧 $I$ 上，校正项恒零。故 $g|_I=0$ 时也有 $(\mathcal Qg)|_I=0$。式 (2) 正是 $B_j=\mathcal Q(W\cos(3j\phi))$；若 $P$ 为阶数不超过 $N$ 的偶三重余弦多项式，则

$$
\mathcal Q(WP)\in\operatorname{span}\{B_2,\ldots,B_N\}.
\tag{8}
$$

这里的消去只用两条真积分矩方程，不使用随 $N$ 改变的高矩逆。

## 3. 完整 C4 零迹函数可先切掉弧边薄带

取任意 $r\in\mathcal X_0$。因 $r$ 在闭弧内恒零且全局为 $C^4$，每个弧端的 $0,1,2,3,4$ 阶导数都为零。

选固定光滑函数 $\eta$，在 $s\le1$ 时为零、$s\ge2$ 时为一。对足够小的 $\varepsilon>0$，在基本周期内置

$$
\psi_\varepsilon(\phi)=\eta\!\left(\frac{|d|-a}{\varepsilon}\right),\qquad
r_\varepsilon=\psi_\varepsilon r,
$$

并作偶、三重周期延拓。由于它在 $d=0$ 附近恒零、在周期接缝附近恒一，绝对值及周期代表不会破坏光滑性。取 $2\varepsilon<L-a$ 即可。

令 $\omega(\varepsilon)$ 为两个弧端外侧宽度 $2\varepsilon$ 邻域中 $|r^{(4)}|$ 的最大值。连续性及端点零四阶 jet 给 $\omega(\varepsilon)\to0$。从弧端向外的距离记为 $s\in[0,2\varepsilon]$，由反复积分，逐个 $0\le j\le4$ 有

$$
|r^{(j)}|\le\frac{(2\varepsilon)^{4-j}}{(4-j)!}\,\omega(\varepsilon).
\tag{9}
$$

对 $j=4$，这就是 $\omega$ 的定义。又有 $|\psi_\varepsilon^{(k)}|\le C_k\varepsilon^{-k}$。Leibniz 公式于是给

$$
\|(r-r_\varepsilon)^{(k)}\|_\infty
\le C\varepsilon^{4-k}\omega(\varepsilon),\qquad 0\le k\le4.
\tag{10}
$$

差只支撑在这些薄带中；在其他地方为零。因此

$$
\|r-r_\varepsilon\|_{C^4}\longrightarrow0.
\tag{11}
$$

这是端点平坦 $C^4$ jet 给出的 $o(1)$ 结论，不假定第五阶导数或任何统一 Hölder 模量。

## 4. 切除后才除以 W，再用 Fejér 逼近

$r_\varepsilon$ 在比 $I$ 稍大的闭邻域上恒零。因而

$$
f_\varepsilon=r_\varepsilon/W
$$

可在该零邻域内以零延拓，得到 $f_\varepsilon\in\mathcal C$。对每个固定 $\varepsilon$，需要相除的集合与 $I$ 保持正距离；式 (1) 和紧致性使 $W$ 在该集合有严格正下界，倒数为 $C^4$。这一步没有要求原来的 $r/W$ 可连续延拓或具有有界 $C^4$ 范数。

为使逼近论证自足，取 Fejér 核

$$
K_N(\theta)=\frac1{N+1}\left|\sum_{k=0}^N e^{ik\theta}\right|^2.
$$

它非负，归一化积分为一，且对任意固定 $\delta>0$，其在 $\delta\le|\theta|\le\pi$ 上的积分趋零；后一点由几何级数式及 $|\sin(\theta/2)|\ge\sin(\delta/2)$ 直接得到。于是对任意连续周期函数，卷积在一致范数下趋于该函数：在 $|\theta|<\delta$ 用一致连续性，在其余部分用上述尾质量界。

定义

$$
P_{\varepsilon,N}(\phi)
=\frac1{2\pi}\int_{-\pi}^{\pi}K_N(\theta)
 f_\varepsilon(\phi-\theta/3)\,d\theta.
$$

它是频率不超过 $3N$ 的三重三角多项式。反射对称与 $2\phi_0=\ell$ 使其为 $\sum_{j=0}^N c_j\cos(3j\phi)$。对 $0\le k\le4$，对 $\phi$ 求导可与卷积交换；将同一一致收敛论证分别用于 $f_\varepsilon^{(k)}$，便有

$$
\|P_{\varepsilon,N}-f_\varepsilon\|_{C^4}\longrightarrow0
\quad(N\to\infty,\ \varepsilon\text{ 固定}).
\tag{12}
$$

乘以固定 $W$、再施加连续算子 $\mathcal Q$，由 (8) 得

$$
\mathcal Q(WP_{\varepsilon,N})\in\operatorname{span}\{B_2,\ldots,B_N\},
\qquad
\mathcal Q(WP_{\varepsilon,N})\longrightarrow\mathcal Q(r_\varepsilon)
\quad\text{于 }C^4.
$$

而 (11)、$\mathcal Qr=r$ 又给 $\mathcal Q(r_\varepsilon)\to r$。先取小 $\varepsilon$，再取足够大的有限 $N$，即可任意接近 $r$。反向包含关系来自各 $B_j\in\mathcal X_0$ 及该空间在 $C^4$ 下闭，故 (3) 得证。

## 5. 补回两个圆弧迹，且每层保留相同迹

这里使用 R44 已付的两维迹补全。为明确所需性质，取偶、三重周期的 $C^4$ 窗 $\chi$，在 $I$ 上为一，在基本周期接缝邻域为零；当前 R44 可取它原来的 $\chi=1-W$。对一般满足 (1) 的 $W$，也可另外选择这样的 $\chi$，不要求一般 $W$ 在接缝附近为一。

局部 $\chi\cos d$ 因在接缝邻域恒零而定义全局 $C^4$ 函数。令

$$
S_A=\mathcal Q\chi,\qquad S_B=\mathcal Q(\chi\cos d),
\qquad T=S_A-S_B,\quad U=S_B.
$$

它们两低矩为零，且在 $I$ 上

$$
T=1-\cos d,\qquad U=\cos d.
$$

这正给 $t(T)=1,u(T)=0$ 与 $t(U)=0,u(U)=1$。对当前 R44 的窗口，这些式子就是原真积分定义，没有换列或改变物理空间。

若 $f\in\mathcal X_{\rm circ}$，则弧上 $f''+f=t$，反射给 $f'(\phi_0)=0$，从中心初值直接得

$$
f(\phi_0+d)=t+(u-t)\cos d,\qquad
r=f-tT-uU\in\mathcal X_0.
\tag{13}
$$

由 (3) 选 $r_N\in\operatorname{span}\{B_2,\ldots,B_N\}$ 趋于 $r$，再置

$$
g_N=r_N+tT+uU\in\mathcal E_{N+2}.
$$

这给出完整 $C^4$ 收敛，同时每层的 $t,u$ 与两低矩都精确保留。R47 的固定槽端点空间恰为 $\mathcal E_M$；利用其嵌套性，可将此逼近序列扩充到每个整数 $M\ge8$：在相邻选中截断阶之间保留上一有限和，未用列补零。于是仍有 $f_M\to f$。反向包含由 $\mathcal X_{\rm circ}$ 的闭性得到，证明 (4) 与 (5)。

## 6. 结论的边界

这是对固定真定义窗口、完整 $C^4$ 目标函数的稠密性；并未把任何单个有限空间等同整个 $\mathcal X_0$，也没有证明 $W$ 乘法的像在该拓扑下闭。切除后商函数的范数和所需 Fourier 阶数可以随 $\varepsilon\downarrow0$ 增大，所以没有统一逼近率、统一系数界或数值条件数结论。

两矩校正和所有迹恒等式使用真积分定义。生产实现中的浮点矩、系数和函数求值误差仍须实际计入；本条不把它们当作精确零矩。控制空间稠密亦不推出 BVP 的解可由这些有限解逼近，不给实际核心的正性域、Jacobian 可逆性、全图 metric 或 reach，也不支付课题 README 的固定度量和参数加密标准。R48 的有限状态/reference 转换及实际均值重建仍是独立问题。

**既有结论核对。** 2026-11-18 通过只读 GitHub GET 核对 [R35](R35-raw-circle-homotopy-has-a-singular-supported-endpoint.md)、[R44](R44-circle-trace-controls-complete-two-missing-directions.md)、[R47](R47-fixed-slot-nested-circle-homotopy.md)，分别对应 Git blob b376fd10fc3cd3617372d39efee8e6f0c4d1a60c、fee150947685b845f76d7b4a7598054314857da2、2d1867b418360122f6fcd3e9608219f54212d058。这些文件已给端点奇异性、完整迹分解和有限嵌套，未给本条的 $C^4$ 闭包等式。本条在执行环境不可用期间完成解析推导和原定义核对，没有重跑任何已登记计算。
