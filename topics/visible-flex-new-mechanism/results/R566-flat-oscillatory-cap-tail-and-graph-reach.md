# R566：固定全平振荡圆盘尾与完整图像片的reach下界

状态：**可直接核算的正面输入。已证明 C-infinity 全平、无限次简单曲率变号和凸底域图像 patch 的 reach 下界；未证明非径向同度量分支或完整闭面。**

本条仅覆盖已证明的局部输入及条件估计，不授予 O4 成功、固定度量返回、全表面 reach 或课题完成。

## 1. 为什么换这个输入

Boyang Hu, *Smooth isometric bending of a closed sphere*, 2026，[原文](https://hexagonmath.org/2611.00534v1)，Proposition 3.2 考察径向图度量
\[
g_w=(1+w(r)^2)\,dr^2+r^2\,d\theta^2
\]
在径向高度处的线性角模
\[
(wf')'-j^2\frac{w'}r f=0.
\]
在文中所列正斜率、单调 flat 端假设下，趋零的模和通量只能给零解。换成任意 C-infinity 阶跃，只避开“解析尾”的字面条件，没有自动支付该论文真正采用的无限振荡和谱条件。

下面给一个**固定有限公式**，无需随网格加密增加层数，即包含无限次曲率变号。此公式没有取得 Hu 论文的全频非共振、零模调谐和非线性解；无限变号只是新增的必要结构输入，不是充分定理。

## 2. 精确函数、定义域和端口

固定
\[
r_c=\frac{11}{50},\qquad \ell=\frac15,\qquad A=\frac1{10},
\qquad \delta=\frac{r-r_c}{\ell}.
\]
在 \(r_c<r\le3/10\)，即 \(0<\delta\le2/5\)，令
\[
w(r)=A\exp\left[-\frac{2-\sin(\delta^{-2})}{\delta}\right]. \tag{1}
\]
在 \(0\le r\le r_c\) 令 \(w(r)=0\)。取任意常数 \(z_c\)，定义
\[
h(r)=z_c-\int_{r_c}^{r}w(t)\,dt,\qquad
X(r,\theta)=(r\cos\theta,r\sin\theta,h(r)). \tag{2}
\]
\(r\le r_c\) 时按零延拓积分，故整个开圆盘 \(r<r_c\) 精确水平。极点用 Cartesian 图 \(x\mapsto(x,h(|x|))\) 定义，因中心邻域常数而光滑。

该片的第一形式精确为 \(g_w\)。高度负号只是朝向选择，不改变此度量和 Gaussian 曲率。外边 \(r=3/10\) 的 jets 由 (1)–(2) 唯一定义；与中段的过渡仍须另付相容和曲率预算，不把任意 cutoff 的代价记作零。

## 3. 全平证明

记
\[
L(\delta)=\log(w/A)=-\frac{2-\sin(\delta^{-2})}{\delta}.
\]
因 \(1\le2-\sin(\delta^{-2})\le3\)，
\[
0<w\le A e^{-1/\delta}. \tag{3}
\]
每个固定阶 \(k\) 的导数 \(d^k w/d\delta^k\) 都是 \(w\) 乘有限个负幂 \(\delta\) 和有界三角函数组成的有限和。因此存在仅依赖 \(k\) 的 \(C_k,M_k\)，使
\[
\left|\frac{d^k w}{d\delta^k}\right|
 \le C_k\delta^{-M_k}e^{-1/\delta}\longrightarrow0.
\]
换到 \(r\) 只多固定因子 \(\ell^{-k}\)。故在 \(r=r_c\) 的零延拓是 C-infinity，所有阶导数为零，\(h-z_c\) 亦全平。指数下溢是机器算术现象，不改变 \(r>r_c\) 时函数数学上严格非零。

方便实现的前三个对数导数为
\[
L_\delta=\frac{2-\sin(\delta^{-2})}{\delta^2}
          -\frac{2\cos(\delta^{-2})}{\delta^4}, \tag{4}
\]
\[
L_{\delta\delta}
=-\frac{2(2-\sin(\delta^{-2}))}{\delta^3}
 +\frac{10\cos(\delta^{-2})}{\delta^5}
 -\frac{4\sin(\delta^{-2})}{\delta^7}, \tag{5}
\]
\[
L_{\delta\delta\delta}
=\frac{6(2-\sin(\delta^{-2}))}{\delta^4}
 -\frac{54\cos(\delta^{-2})}{\delta^6}
 +\frac{48\sin(\delta^{-2})}{\delta^8}
 +\frac{8\cos(\delta^{-2})}{\delta^{10}}. \tag{6}
\]
于是
\[
w_\delta=wL_\delta,\quad
w_{\delta\delta}=w(L_{\delta\delta}+L_\delta^2),\quad
w_{\delta\delta\delta}
=w(L_{\delta\delta\delta}+3L_\delta L_{\delta\delta}+L_\delta^3).
\]
**(4) 的余弦项是负号。** 下文上界使用绝对值，不依赖未检查的导数符号约定。

## 4. 无限次简单曲率变号

令 \(u=\delta^{-2}\ge25/4\)，并设
\[
F(u)=2u\cos u+\sin u-2.
\]
(4) 化为
\[
L_\delta=-uF(u).
\]
对每个充分大的整数 \(m\)，在 \(u=2m\pi\) 有
\(F=4m\pi-2>0\)，而在相邻的
\(u=2m\pi-\pi/2\) 和 \(u=2m\pi+\pi/2\) 分别有 \(F=-3,-1\)。
故每个这样的半周期至少有两个零，零点趋向 \(u=\infty\)，相应 \(r\) 趋向 \(r_c\)。

所有这个定义域中的零都是简单零。事实上，在零点
\[
0<\cos u=\frac{2-\sin u}{2u}\le\frac3{2u},\qquad
F'(u)=3\cos u-2u\sin u.
\]
若 \(\sin u<0\)，则 \(F'>0\)。若 \(\sin u>0\)，则
\[
F'(u)\le\frac9{2u}-2u\sqrt{1-\frac9{4u^2}}<0
\quad (u\ge25/4).
\]
零点不可能有 \(\sin u=0\)，因为那会要求 \(u=1\) 或无解。
因此 \(w_r'\) 的零简单且反复变号。径向图的 Gaussian 曲率是
\[
K(r)=\frac{h'h''}{r(1+h'^2)^2}
    =\frac{w\,w_r'}{r(1+w^2)^2}. \tag{7}
\]
由于 \(w>0\)，它具有相同的无限次简单变号，并且在 \(r_c\) 全平。

这一结论是精确函数结论；有限网格只能看到有限个零，不能把“网格未分辨的尾”误读为没有这些零。

## 5. 显式二阶和高度预算

由 (3)–(4)，
\[
|w_r'|
 \le \frac A\ell e^{-1/\delta}
             (3\delta^{-2}+2\delta^{-4}).
\]
令 \(x=1/\delta\ge5/2\)。\(x^2e^{-x}\) 在此区间最大于 \(x=5/2\)，
\(x^4e^{-x}\) 最大于 \(x=4\)。故
\[
|w_r'|\le K_0:=
 \frac{75}{8}e^{-5/2}+256e^{-4}
 <5.459. \tag{8}
\]
另外
\[
|w|\le\frac1{10}e^{-5/2}<0.008209,\qquad
\frac{|w|}{r}\le\frac5{11}e^{-5/2}<0.037312, \tag{9}
\]
以及
\[
|h-z_c|\le (r-r_c)\,A e^{-1/\delta}
 \le\frac1{125}e^{-5/2}<0.000657. \tag{10}
\]
径向 Cartesian Hessian 的两个特征值为 \(-w_r'\) 和 \(-w/r\)，所以在整个闭圆盘
\[
D=\{x\in\mathbb R^2:|x|\le3/10\}
\]
有
\[
\|D^2h\|_{\rm op}\le K_0.
\]

(8) 采用分项取最大值，故保守但完全显式。没有使用峰值采样替代连续上界。

## 6. 凸底域图像的 reach：直接证明及准确适用范围

令
\[
S=\{(x,h(x)):x\in D\},
\]
此处 \(D\) 是上面的**整个凸闭圆盘**，包括开平帽和振荡尾。

先对两个图像点 \(p=(x,h(x))\)、\(q=(y,h(y))\)，Taylor 积分余项给
\[
|h(y)-h(x)-\nabla h(x)\cdot(y-x)|
 \le \frac{K_0}{2}|y-x|^2.
\]
以图像单位法向 \(n(p)=(-\nabla h(x),1)/\sqrt{1+|\nabla h(x)|^2}\)，得到
\[
|(q-p)\cdot n(p)|
 \le \frac{K_0}{2}|q-p|^2. \tag{11}
\]
所以这整个 patch 内所有法弦都满足半径 \(1/K_0\) 的条件。

这里还能直接证明 **作为带边界闭集的 \(S\) 本身**
\[
\operatorname{reach}(S)\ge\frac1{K_0}>0.1832. \tag{12}
\]
证明无需忽略边界法锥。取距离 \(S\) 为 \(d<1/K_0\) 的任意环境点 \(z\)，存在最近点 \(p=(x,h(x))\)，写 \(v=z-p=(v_x,v_z)\)。在凸域 \(D\) 上的一阶最小条件是
\[
(v_x+v_z\nabla h(x))\cdot(y-x)\le0\qquad(y\in D).
\]
因此对任意 \(q=(y,h(y))\in S\)，
\[
v\cdot(q-p)
 \le |v_z|\frac{K_0}{2}|y-x|^2
 \le d\frac{K_0}{2}|q-p|^2.
\]
若另一个不同点 \(q\) 也是最近点，则
\[
0=|z-q|^2-|z-p|^2
 \ge (1-dK_0)|q-p|^2>0,
\]
矛盾。故 \(d<1/K_0\) 时最近点唯一，证明 (12)。

**范围限制：** (11)–(12) 仅涵盖这个凸底域图像 patch。它不涵盖完整闭面中 cap/body、tail/body、正负两半等跨块点对。把这个 patch 接到一个闭面后，完整闭面的 reach 可以更小；必须重新支付所有跨块法弦和嵌入门。

一个有用的条件余量是：若最终实际曲面在同一凸底域上仍为图像 \(h+v\)，且已连续验证
\[
\|D^2v\|_{\rm op}\le10,
\]
则同一证明给
\[
\operatorname{reach}(\operatorname{graph}(h+v))
 \ge\frac1{K_0+10}>0.06468>0.061. \tag{13}
\]
这里的 \(v\) 是**实际外在图像高度**，不是任意材料参数下的系数；必须先证明图像表示及底域凸性。未付全闭面跨块门时，(13) 不能写成全闭面 reach。若在材料坐标里改变水平分量，不能直接把它们忽略而套 (13)。

## 7. 怎样送入逆设计求解器

在靠近开圆领的过渡尾，选单调半径 \(r=r(s)\)，令
\[
z_{\rm bg}(s)=h(r(s)),\qquad
z_{{\rm bg},s}=-r_s\,w(r(s)).
\]
在准确圆形背景上，这是 (1)–(2) 的同一几何；不依赖有限层数、网格或截断公差。外边的中段拼接必须使用上述真实 jets。

可让自由修正使用更快全平权
\[
b(\delta)=
\begin{cases}
e^{-c/\delta^2},&\delta>0,\\
0,&\delta\le0,
\end{cases}
\qquad c>0\ \text{固定}. \tag{14}
\]
对任意固定非负整数 \(m,k\)，
\[
\frac{d^k}{d\delta^k}\!\left(\frac{b}{w^m}\right)\longrightarrow0.
\]
因为其每项是负幂和有界三角函数乘
\[
A^{-m}\exp[-c/\delta^2+m(2-\sin(\delta^{-2}))/\delta]
 \le A^{-m}\exp[-c/\delta^2+3m/\delta],
\]
后者压过所有固定次幂。该性质可在相对端部权中保留背景的全平尺度。

自由的非径向修正必须在每个 \(r>r_c\) 仍允许存在；只有 \(r\le r_c\) 强制准确平圆盘。若把整个 \(r_c<r<3/10\) 也冻结为径向背景，再在 \(r=3/10\) 才打开自由量，就把真正的分支问题移到了另一个有限圆周，并未利用无限振荡尾。

(14) 的渐近小不代表其有限位置导数没有代价。任何 \(c\)、系数幅度和中段 cutoff 都要计入实际连续曲率预算。把 \(b\) 选得太快也可能排除真正的 flat 核：本笔记没有证明存在该权空间中的线性解，应保留更一般全平权作为搜索方向。

## 8. 已付与未付

已付：
- 单个固定、有限可复现公式定义无限层振荡，不用随网格更改输入。
- 准确开圆盘端口、所有阶端相容。
- 无限次简单 Gaussian 曲率变号。
- 连续二阶上界、凸底域 graph patch 的 reach 下界及有条件扰动余量。
- 可实现的显式前三阶导数、可与自由逆设计对接的端部权说明。

未付：
- 非零且全平的线性角模或其全频非共振；
- 精确非径向 Darboux/等距分支；
- 与非圆核心的完整连接；
- 闭面嵌入、跨块 reach 和宏观 hold 幅度；
- 固定度量候选的误差小于 1e-6 及真正固定 g 精化。

本输入使“只用单调 flat 尾”的限制变成可实际改写的模型，但不能把避开一个障碍当成完成几何。应继续求解新候选，失败则换尾或换结构，而不是用本笔记收尾。

