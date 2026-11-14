# R63：水平角切向的准确 C² 等距条带分类

日期：2026-11-14。repo_sources 独立纸面推导，root 全文复核。未评价任何研究候选，也未进行数值求解。

本稿给新直接度量模型的一条必要结构限制。结论只适用于角切向在**整个连通条带**恒为水平的准确解；不适用于仅在入口水平、角切向很小但非零，或度量仅近似准确的数值场。

## 1. 假设与结论

设 $J\subset\mathbb R$ 为连通开区间，

$$X:J\times(\mathbb R/2\pi\mathbb Z)\longrightarrow\mathbb R^3$$

为 $C^2$ 浸入，并准确满足

$$|X_s|^2=1,\qquad X_s\cdot X_\theta=0,\qquad
|X_\theta|^2=a(s)^2,\qquad a>0.\tag{1}$$

仅需先假设 $a\in C^1$。令 $T=X_\theta/a$。另假设

$$T\cdot e_z\equiv0\quad\hbox{在整个 }J\times S^1.\tag{2}$$

则恰有下列两类可能：

1. **非圆直柱。** 存在一个固定闭合平面正则曲线 $\gamma_0(\theta)$、常数 $a_0>0$ 及固定 $\sigma\in\{-1,1\}$，且该曲线的角转速非恒定，使
   $$X(s,\theta)=(\gamma_0(\theta),\sigma s+z_0),\qquad
   |\gamma_0'|=a_0.$$
2. **固定轴的圆截面。** 存在固定平面中心 $C$、非零整数 $m$ 及单位向量场 $N(\theta)$，使
   $$X(s,\theta)=\left(C-\frac{a(s)}mN(\theta),z(s)\right),\qquad
   \frac{a'(s)^2}{m^2}+z'(s)^2=1,\tag{3}$$
   其中每个截面是半径 $a/|m|$ 的 $m$ 重参数化圆。若每个截面本身为嵌入圆，则 $|m|=1$。

圆直柱归入第二类；第一类已明确要求角转速非恒定。本结论不要求原条带已全局嵌入。

## 2. 零径向速度与换号的处理

由 (2) 及每个角圆的连通性，存在 $C^2$ 函数 $z=z(s)$，使

$$X(s,\theta)=(\gamma(s,\theta),z(s)).$$

以下把 $T=\gamma_\theta/a$ 看作平面单位向量，令 $N=\mathcal JT$，其中 $\mathcal J$ 是固定的平面逆时针直角旋转。

由正交条件，存在一个全局 $C^1$ 标量 $\nu(s,\theta)$，使

$$\gamma_s=\nu(s,\theta)N,\qquad
\nu(s,\theta)^2=1-z'(s)^2.\tag{4}$$

固定任意 $s$。若 (4) 右侧严格为正，连续函数 $\theta\mapsto\nu(s,\theta)$ 的值只能落在两个互不相交的点中；角圆连通，因此其符号和数值都与 $\theta$ 无关。若右侧为零，则全角 $\nu=0$。所以在全部 $s$ 上都可准确写成

$$\nu(s,\theta)=\nu(s,0)=:\nu(s),\qquad \nu\in C^1(J).\tag{5}$$

此处没有除以 $\nu$。它可以在任意 $s$ 为零，圆分支也允许它经过零后换号；这些情形均保留在后续等式中。这里的 $\nu$ 是平面截面的法向速度，不是数值 frame 表示中控制 $T_z$ 的角场变量。

## 3. 混合二阶导数直接给出分类

定义连续的有向平面曲率 $\kappa$，使

$$T_\theta=a\kappa N,\qquad N_\theta=-a\kappa T.$$

由 $X\in C^2$ 可交换混合导数。将 $\gamma_\theta=aT$、$\gamma_s=\nu(s)N$ 求导，得到

$$a'T+aT_s=\gamma_{\theta s}=\gamma_{s\theta}
=-a\nu\kappa T.$$

由于 $T_s\perp T$，分别取切向和法向分量便有

$$\boxed{T_s=0,\qquad a'=-a\nu\kappa.}\tag{6}$$

故 $T$ 与 $N$ 只依赖角变量，

$$k_0(\theta):=T_\theta\cdot N=a(s)\kappa(s,\theta)$$

也与 $s$ 无关，且 (6) 成为

$$a'(s)=-\nu(s)k_0(\theta)\quad\hbox{对全部 }s,\theta.\tag{7}$$

若 $k_0$ 非恒定，取两个 $k_0$ 值不同的角点相减，(7) 迫 $\nu(s)=0$ 对每个 $s$ 成立。于是 $a'=0$、$\gamma_s=0$，并由 (4) 得 $z'^2=1$。连续性及 $J$ 连通进一步迫 $z'=\sigma$ 为同一个固定符号。这就得到第一类，不能通过在某个半径“停住”再进入圆分支。

若 $k_0$ 为常数，方程 $T_\theta=k_0\mathcal JT$ 与 $2\pi$ 周期性迫 $k_0=m\in\mathbb Z$。$m=0$ 会使 $\gamma_\theta=aT$ 为非零常向量，从而 $\gamma$ 无法闭合，故 $m\ne0$。积分角方向得

$$\gamma(s,\theta)=C(s)-\frac{a(s)}mN(\theta).$$

再代 $a'=-m\nu$、$\gamma_s=\nu N$，立即得到 $C'(s)=0$。最后由 (4) 得 (3)。在此分支 $a,z$ 实际具有从 $X\in C^2$ 继承的二阶正则性；证明未使用三阶或更高 Taylor 展开。

## 4. 对本题模型的适用范围

准确椭圆平柱入口的角转速非恒定。如果同一连通连接带到圆尾始终满足 $T_z=0$，上述分类即排除这种连接。因此真正的非圆入口至圆领的准确等距连接，必须在某些地方具有非零空间角切向 $T_z$。

独立中心速度 $b=z_c'$ 改善的是所有角共享的高度自由度；它本身不能代替截面向空间弯曲的角场。当前 167 维模型仍保留 72 个相应角场列，因此不被本命题排除。

本命题没有提供 $T_z$ 必须多大的正下界，也没有提供有限离散场的度量残差下界。后续若读取 $T_z$ 或截面非平面程度，仅能把它作为有这条准确背景的数值诊断；不得用采样接近零代替恒等式 (2)。更一般的非水平截面、非解析 $C^2$ 实现、完整闭面嵌入和 reach 均未在这里处理。

与直接度量的关系见 [R57](R57-direct-reconstructed-metric-and-auxiliary-frame-space.md)，逐圈松弛筛见 [R59](R59-scalar-center-speed-elimination-and-metric-lower-bounds.md)及 [R61](R61-joint-radius-slope-center-projection-and-local-reconstruction.md)。
