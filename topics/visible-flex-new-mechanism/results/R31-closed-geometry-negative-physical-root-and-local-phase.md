# R31：真实闭合带几何的负物理根比值与非退化局部相位

日期：2026-11-14。独立完整存在证明。

**已支付的范围。** 构造 $C^\infty$、正则、周期的球面曲线 $B(s)$ 和闭合正则中心曲线 $\alpha(s)$，取 $h=1$，使本题实际周期积分的 $C$ 在物理半线上有简单实根，且

$$-\frac94<\frac{W}{C'}<-\frac54,$$

同时 $L$ 在二次多项式上的矩阵可逆。因此通用局部相位定理的 $\mathcal K\ne0$ 条件和三个 $B_j$ 的满秩条件都能由真实闭合几何实现。

**尚未支付。** 本稿只构造闭合正则曲线及周期浸入带，不证明中心曲线或带嵌入，不给 reach 下界，不给完整两端 profile 或有限等距族。两个简单四阶外尾的完整 $C^4$ 类仍受恒相位排除；本稿不使那个已排除的类重新成立。

## 1. 几何约定和要实现的严格开条件

沿用本题的有向单位框架

$$T_s=kN,\qquad N_s=-kT-B,\qquad B_s=N,$$

并取

$$h=1,\quad \alpha_s=T,\quad\omega=k/2,
\quad X(s,u)=\alpha(s)+uN(s).\tag{1}$$

这里 $s$ 同时是球面曲线 $B$ 和中心曲线 $\alpha$ 的弧长。周期的 $k$ 自动使 $\omega$ 周期；完整空间闭合另外要求 $\int T\,ds=0$，将在 §6 精确实现。

这种从闭球面法向曲线积分构造空间曲线的框架，与 Bates–Melko《On curves of constant torsion I》[原文 pp.1–4，式 (1.1) 与 §1.1](https://arxiv.org/pdf/1206.7086) 的 Darboux 表示一致，符号按本题固定为 (1)。下面给出的群闭合和周期算子计算是本稿自己的证明，不以文献中的例子替代当前条件。

物理变量满足

$$u=\frac1{\xi+k/2}.$$

我们将始终保持 $k\ge0$ 并选择 $\xi$ 接近 $31/3>0$，所以存在一个共同的紧物理 strip；分母的正下界不依赖采样。

## 2. h=1 的完整矩公式

对一条周期球面曲线，用其弧长平均记号 $\langle\cdot\rangle$，记

$$m_j=\langle k^j\rangle,\qquad
D=\langle k_s^2\rangle,\qquad E=\langle k k_s^2\rangle.$$

本节将所有周期系数除以总弧长；这个共同正因子不改变根、比值或是否满秩。令 $y=\xi$，则

$$e=y-k/2,\qquad
\mathscr K=k y^2-y-k^3/4-k/2-k_{ss}/2.$$

实际低导数积分给

$$C(y)=\frac18\left\langle\mathscr K(e^2+1)\right\rangle,
\qquad W(y)=\frac14\langle\mathscr K e\rangle.\tag{2}$$

按 $y$ 升幂展开，并对 $k_{ss}$ 项周期分部积分，得

$$\begin{aligned}
C(y)={}&-\frac{m_5}{128}-\frac{3m_3}{64}-\frac{m_1}{16}+\frac E{32}\\
&+\left(\frac{m_4}{32}+\frac{m_2}{32}-\frac18-\frac D{16}\right)y
 +\frac{3m_1}{16}y^2-\frac{m_2+1}{8}y^3+\frac{m_1}{8}y^4,\\
W(y)={}&\frac{m_4}{32}+\frac{m_2}{16}-\frac D{16}
-\frac{m_3}{16}y-\left(\frac{m_2}{8}+\frac14\right)y^2
+\frac{m_1}{4}y^3.
\end{aligned}\tag{3}$$

例如 $\langle k k_{ss}\rangle=-D$、
$\langle k^2k_{ss}\rangle=-2E$，所有端项都因周期性为零。

作用于 $\{1,y,y^2\}$ 的实际矩阵 $M=L|_{\mathcal P_2}$ 为

$$M=\begin{pmatrix}
-m_3/8-m_1/2&-m_2/16-1/4&m_5/32+3m_3/16+m_1/4-E/8\\
m_2/2&m_1/4&-m_4/8-m_2/4+D/4\\
-m_1/2&-1/4&m_1/4+m_3/8
\end{pmatrix}.\tag{4}$$

这也直接验证了实际 $D_{\rm period}=0$ 的迹零条件。本文用 $D=\langle k_s^2\rangle$ 表示一个非负曲率能量，**不是** 已恒等为零的 $D_{\rm period}$。

把均值写成 $a=m_1$，并用中央矩

$$v=\langle(k-a)^2\rangle,\quad t=\langle(k-a)^3\rangle,
\quad z=\langle(k-a)^4\rangle,\quad w=\langle(k-a)^5\rangle,
\quad J=\langle(k-a)k_s^2\rangle,$$

展开 (4) 的三阶行列式，得到精确恒等式

$$\det M=\frac1{256}\{
-2Dt+4Jv+3at^2-3azv+3av^3+tz+tv^2-vw\}.\tag{5}$$

所以 $h$ 恒常本身并不强制 $\det M=0$。后文会给出实际球面曲线使其严格非零。

## 3. 一个有严格余量的负比值极限

先考虑 $k\to a$ 一致、但 $\langle k_s^2\rangle\to D>0$ 的极限。此时 $m_j\to a^j$、$E\to aD$。记 $e=y-a/2$，则 (3) 化为

$$C_\infty(y)=\frac{K(e)(e^2+1)-De/2}{8},\qquad
W_\infty(y)=\frac{K(e)e-D/4}{4},$$
$$K(e)=(ae-1)(e+a).\tag{6}$$

取精确有理数

$$a=20,\qquad e_*=\frac13,\qquad
D=\frac{20740}{27},\qquad y_* = e_*+a/2=\frac{31}{3}.\tag{7}$$

直接代入给

$$C_\infty(y_*)=0,\quad
C_\infty'(y_*)=\frac{679}{36}>0,\quad
W_\infty(y_*)=-\frac{1037}{27},$$

$$\frac{W_\infty(y_*)}{C_\infty'(y_*)}
=-\frac{4148}{2037}\in\left(-\frac94,-\frac54\right).\tag{8}$$

根为简单根，比例处于严格开区间，$y_*>10$。因此足够小的系数扰动仍有邻近简单正根，并保持该比例范围。

这个极限的矩阵 $M$ 确实退化；不能直接把它当作已满足通用相位定理的 $\mathcal K\ne0$。下一节用一个具体非对称高频微扰支付该条件。

## 4. 实际闭球面高频曲线和非零行列式

令 $\beta_0\in(0,\pi/2)$ 满足 $\cot\beta_0=a=20$，并记

$$S=\sin\beta_0=\frac1{\sqrt{401}},\qquad
A=S\sqrt D,\qquad \varepsilon_n=\frac A n.$$

对每个充分大的正整数 $n$，定义明确的闭球面曲线

$$\begin{aligned}
\beta_n(\theta)&=\beta_0+\frac{AS^2}{n^3}
 \left(\cos(n\theta)+\frac18\cos(2n\theta)\right),\\
B_n(\theta)&=(\sin\beta_n\cos\theta,
 \sin\beta_n\sin\theta,\cos\beta_n),\qquad0\le\theta\le2\pi.
\end{aligned}\tag{9}$$

它是 $C^\infty$、周期、正则的曲线，并可按弧长参数化。其速度与有向球面曲率的精确公式为

$$\frac{ds}{d\theta}=\sqrt{\beta_\theta^2+\sin^2\beta},$$

$$k=\frac{\cos\beta(\sin^2\beta+2\beta_\theta^2)
-\sin\beta\,\beta_{\theta\theta}}
 {(\beta_\theta^2+\sin^2\beta)^{3/2}}.\tag{10}$$

在 (9) 中，$\beta-\beta_0=O(n^{-3})$、$\beta_\theta=O(n^{-2})$、$\beta_{\theta\theta}=O(n^{-1})$。由 (10) 的普通 Taylor 展开，且这些余项可对 $\theta$ 求一次导数，得到一致估计

$$k_n=a+\varepsilon_n f(n\theta)+O(n^{-3}),\qquad
(k_n)_s=\frac A S f'(n\theta)+O(n^{-2}),\tag{11}$$

其中

$$f(\vartheta)=\cos\vartheta+\tfrac12\cos2\vartheta,$$

而 $ds=S\{1+O(n^{-3})\}\,d\theta$。特别地，充分大 $n$ 时 $k_n>0$，并且总弧长趋于 $2\pi S$。

四个普通三角平均准确为

$$\langle f^2\rangle_{\vartheta}=\frac58,\qquad
\langle f^3\rangle_{\vartheta}=\frac38,\qquad
\langle(f')^2\rangle_{\vartheta}=1,\qquad
\langle f(f')^2\rangle_{\vartheta}=\frac38.\tag{12}$$

因此这些实际闭球面曲线的弧长中央矩满足

$$D_n\to D,\quad
v_n=\frac58\varepsilon_n^2+o(\varepsilon_n^2),\quad
t_n=\frac38\varepsilon_n^3+o(\varepsilon_n^3),$$

$$J_n=\frac{3D}{8}\varepsilon_n+o(\varepsilon_n),\quad
z_n=O(\varepsilon_n^4),\quad w_n=O(\varepsilon_n^5).\tag{13}$$

注意 (13) 中的中央矩是围绕实际均值 $m_1(k_n)$；(11) 给均值与 $a$ 的误差为 $O(n^{-3})=o(\varepsilon_n)$，足以支持所写的全部首项。

将 (13) 代入精确恒等式 (5)：

$$\det M_n=\frac{3D}{4096}\varepsilon_n^3
+o(\varepsilon_n^3)>0\tag{14}$$

对充分大的有限 $n$ 成立。同时 (3) 的所有系数趋于 (6)，所以 §3 的简单正根和严格负比值也已经在每个充分大的有限 $n$ 上成立。

这些 $B_n$ 已经是真实闭球面曲线，但 $\alpha_s=T_n$ 的空间位移一般不为零；现在单独支付这个闭合条件。

## 5. 有限、平滑、非负曲率的任意框架连接

**框架连接引理。** 给定 $F_0,F_1\in SO(3)$，以及两端任意已给定的非负光滑曲率函数芽，可以找到有限长度的 $C^\infty$ 非负控制 $k(s)$，使

$$F_s=F\Omega(k),\qquad
\Omega(k)=\begin{pmatrix}0&-k&0\\k&0&1\\0&-1&0\end{pmatrix},\tag{15}$$

从 $F_0$ 准确到达 $F_1$，并在两端与给定函数芽一致。函数芽的邻域只需足够小。

**证明。** 先要求端点附近 $k=0$。常值 $k=0$ 是绕体坐标 $-e_1$ 的旋转；常值 $k=1$ 是绕 $(-e_1+e_3)/\sqrt2$ 的旋转，角速度 $\sqrt2$。后者转角为 $\pi$ 的矩阵记为 $S_0$，它把 $e_1$ 送到 $-e_3$。因此用 $S_0$ 共轭 $k=0$ 的旋转，可得到绕第三坐标轴的任意旋转。每个逆旋转都能以正时长实现，因为两个常值流均周期。

绕第一、第三坐标轴的 Euler 旋转分解因而给任意目标矩阵的有限分段常值控制，且只用 $k=0,1$。可将各平台时间加上完整周期，使全部时间严格为正；首尾取 $k=0$ 平台。

为保证平滑以后仍准确到达目标，在这个词之前加一个端点为恒等的控制词：先作一个中间角为 $\pi/2$ 的三参数第一轴–第三轴–第一轴 Euler 词，再接上其固定逆词。该词的三个角参数在基点处给满秩的 $SO(3)$ 端点映射，因为三个相应的无穷小旋转轴线性无关。第三轴旋转仍用前述 $S_0$ 共轭实现。

现在把每次 $0/1$ 跳变替换成固定形状、长度为 $\delta$、两端全平的光滑过渡，始终保持 $0\le k\le1$。每个过渡的框架增量在 $\delta\to0$ 时趋于恒等，且依赖于 $\delta$ 和平台角参数的端点映射为 $C^1$：把过渡时间缩放到 $[0,1]$ 后，其 ODE 只是 $F_t=\delta F\Omega(k(t))$。上述满秩条件因此在小 $\delta$ 下保持。有限维隐函数定理调整那三个平台角，得到准确目标矩阵。平台时间仍严格为正，首尾 $k=0$ 开区间保留。

最后，对一般端点函数芽，先在各端用非负平滑截断接到 $k=0$。这些固定端帽产生两个确定的框架增量；把中间目标改成由这两个增量共轭后的矩阵，再应用上一段即可。端帽可以直接使用给定函数芽的一小段，故匹配的是全部 jet，不只是曲率值。证毕。

本引理只构造单位框架与球面路径；没有声称连接产生嵌入的空间曲线。

## 6. Klein 四元群的精确空间闭合

固定一个已经通过 §4 的有限 $n$，把 $B_n$ 的起始框架记为 $F_*=(T_*,N_*,B_*)$。取由三个相互垂直轴的半周旋转组成的 Klein 群

$$G=\{I,g_1,g_2,g_3=g_1g_2\}\subset SO(3),\qquad
\sum_{g\in G}g=0.\tag{16}$$

利用 §5，选两条固定的平滑球面框架路径，从 $F_*$ 分别到 $g_1F_*$、$g_2F_*$；它们的起终曲率函数芽都与 $B_n$ 起点的周期函数芽相同，并且处处 $k\ge0$。把每条路径前面加上 $N$ 圈完整的 $B_n$，得到两条路径 $P_1^{(N)},P_2^{(N)}$。

考虑有向 Cayley 图：每个 $g\in G$ 各有一条 $g\to gg_1$ 和一条 $g\to gg_2$ 的边。以下生成元词是一个遍历全部八条有向边的闭 Euler 游走：

$$g_1,g_2,g_1,g_2,g_2,g_1,g_2,g_1.\tag{17}$$

当游走位于顶点 $g$、取第 $j$ 类边时，放入完整旋转后的路径 $gP_j^{(N)}$。端点框架准确相接，且全部曲率 jet 一致，所以得到一条 $C^\infty$、单位速度、正则、周期的球面曲线。控制非负也逐段保持。

记未旋转路径的空间位移为

$$V_j^{(N)}=\int_{P_j^{(N)}}T\,ds.$$

每一类边恰好各在四个群顶点出现一次，故完整中心曲线的位移严格等于

$$\int T\,ds
=\sum_{g\in G}gV_1^{(N)}+\sum_{g\in G}gV_2^{(N)}=0.\tag{18}$$

这是真正的向量等式，没有用采样闭合残差或求解容差。由于框架和所有端点 jet 也周期，$\alpha(s)=\int_0^sT\,ds$ 为 $C^\infty$ 闭合正则曲线。

每个完整周期包含 $8N$ 圈 $B_n$，以及各四份固定连接路径。所有实际周期系数是沿 $s$ 的局部积分，且在适当旋转下不变；这里 $\omega=k/2$ 也是同一个全局周期函数。因此把全周期系数除以 $8N$ 后，随着 $N\to\infty$ 收敛到 $B_n$ 的系数（一个共同正弧长因子无关紧要）。

在固定 $n$ 后，§4 的非零行列式已经有严格余量。故可以再取足够大的有限 $N$，同时保持简单正根、严格负比值和 $\det M\ne0$。不能先令 $n,N$ 无约束共同趋于无穷来忽略微小行列式；这里按“先固定通过 (14) 的 $n$，再取 $N$”的次序选择。

## 7. 满秩和通用局部相位条件确实全部到位

令 $\mathcal B$ 为 R15 的尾积分系数矩阵：列依次对应 $B_0,B_1,B_2$，行依次对应常数、一次、二次项，即

$$\mathcal B=\begin{pmatrix}
r_0&s_0&t_0\\
r_1&s_1&t_1\\
-p_0/4&-p_1/4&-p_2/4
\end{pmatrix}.$$

一般的实际八系数表达式给

$$M=\begin{pmatrix}
p_0&2r_1&-4r_0\\
p_1&2s_1&-4s_0\\
p_2&2t_1&-4t_0
\end{pmatrix}
=\mathcal B^{\!T}
\begin{pmatrix}0&0&-4\\0&2&0\\-4&0&0\end{pmatrix},$$

$$\det M=-32\det\mathcal B.\tag{19}$$

在一个 $C(\xi_*)=0$ 的根处，把二次多项式的输入和输出都改为该点的零至二阶 jet。这个矩阵与 $M$ 共轭。先以 $q(\xi_*)=1$ 解 $L=L'=0$，再计算二阶残差，恰是通用局部定理的 $\mathcal K$。展开这个三行消元给

$$\det M=-4A_2(\xi_*)W(\xi_*)\,\mathcal K.\tag{20}$$

在当前负比值区间，$W\ne0$ 且
$A_2=C'-W=C'(1-W/C')\ne0$。因此 §6 的非零行列式同时给

$$\mathcal K\ne0,\qquad\det\mathcal B\ne0.$$

又因为整个闭合构造保持 $k\ge0$，且根仍可选在 $\xi_*>10$，所以在其一个固定紧邻域中

$$\xi+k(s)/2>0\quad\hbox{对所有 }s$$

严格成立。$u=1/(\xi+k/2)$ 定义一个真实物理带；其参数浸入没有退化，因为

$$|X_s|^2=(1-ku)^2+u^2>0,\qquad
X_s\cdot X_u=0,\qquad |X_u|=1.$$

通用局部 D=0 定理现可直接应用于这些真实几何系数，给内部单侧 $C^4$ 复相位分支。满秩 (19) 还允许选择三个局部积分常数，使 $O,O',O''$ 在一个锚点为零，再由 $Q=O'''=0$ 得该局部区间上的 $O=0$。这些常数仍不是完整右尾，不能据此省略总矩或两端条件。

## 8. 这条正向结论的实际意义

本稿排除了一个可能误导后续搜索的普遍障碍猜想：**精确空间闭合并不强制所有物理简单根的 $W/C'$ 非负，也不强制负比值根的局部非退化量为零。** 结论来自真实有限的光滑闭合几何，而不只是任意形式八系数或极限对象。

存在证明的高频和长重复段没有提供有效的厚度或振幅估计；它也没有建立全局嵌入。后续若使用这条路线，必须寻找更短、更厚的具体几何，并采用未被 C4 双外尾排除覆盖的完整 profile 机制，再继续有限等距路径。与此独立，已完成的实际 root-ratio Actions 可以提供较短的数值候选，但它需要自己的严格积分和嵌入核验，不能借本存在证明冒充对那个固定数值候选的认证。

## 9. 精确代数证书

[纯 Fraction 证书脚本](../scripts/literature_constant_h_moment_certificate.py) 与
[实际执行 JSON](literature-constant-h-moment-certificate-20261114.json)
检查 (5) 的七变量有理多项式恒等式、$\det M=-32\det\mathcal B$、四个三角平均、严格有理比值区间、极限本身 $\mathcal K=0$ 的保留，以及 Klein 群八条边和旋转和的精确恒等式。

脚本 SHA-256 为
`58b997fc49d1ffcd496866ccec49ef1f4976048a20fc074d74eea809d6f09563`。
执行命令为：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_constant_h_moment_certificate.py \
  --out topics/visible-flex-new-mechanism/notes/literature-constant-h-moment-certificate-20261114.json
```

这次本地执行只含精确代数，没有采样实际几何、选择有限 $n,N$、运行优化器或研究 ODE。它不代替 §4 的余项估计、§5 的平滑隐函数论证或任何嵌入/reach 证明。

## 9. 复核与准确代数证据

root完整独立核对各节，包括实际矩公式、非对称高频首项、正时长控制词的平滑隐函数论证、Klein精确空间闭合、先固定n再放大N以及根处Schur消元。repo_sources独立纸核§§2–4的完整行列式与一致渐近，没有只检查一个数值样例。root另实际打开Bates–Melko原始PDF核对其Darboux公式和框架约定。

[准确Fraction核验脚本](../scripts/literature_constant_h_moment_certificate.py) 与 [人工代数检查记录](../notes/literature-constant-h-moment-certificate-20261114.json) 只检查多项式恒等、四个三角平均、严格有理比例及Klein八边；实际平滑连接和有限n/N存在由正文证明，脚本不替代它们。相同核验另交本公开仓库Actions运行，实际输出将单独审计。
