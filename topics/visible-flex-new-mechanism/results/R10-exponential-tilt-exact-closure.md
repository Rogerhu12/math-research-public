# R10：指数倾斜准确闭合的对称带状基底

日期：2026-11-14。本文给出一族准确满足中心线闭合和渐近周期条件的基底参数化，供完整周期系数设计使用。中心线是闭合正则浸入；其嵌入性、带的 reach、九系数零条件、非零连续 profile 及闭曲面均不由本文保证。

## 1. 曲线与速度的定义

令整数 $m\ge2$，$x=m\theta$，取 $b>1/2$。定义

\[
r(\theta)=\exp\!\left(\rho_0+\rho_1\cos x+\rho_2\cos2x+\rho_3\cos3x\right)>0,
\]

\[
\varphi(\theta)=\theta+\frac b m\sin2x,
\qquad B(\theta)=\frac{(r\cos\varphi,r\sin\varphi,1)}{\sqrt{1+r^2}}.
\tag{1}
\]

假设 $B_\theta\ne0$；下面给出本模型的准确可检查判据。记 $d\sigma=|B_\theta|d\theta$，

\[
N=B_\sigma,\qquad T=-B\times N,
\qquad B_\sigma=N,\quad N_\sigma=-B-\kappa T.
\]

取任意有限偶周期函数

\[
\ell(x)=\sum_{j\in I}c_j\cos jx,\qquad 2\notin I,
\]

并定义一个尚待确定的实倾斜常数 $d$：

\[
w_d(x)=\exp(2\ell(x)+2d\cos2x),\qquad
v(\theta)=\frac{(1+r^{-2})w_d(x)}{C},\quad C>0.
\tag{2}
\]

归一化 $C$ 可以准确取为

\[
C=\frac{\int_0^{2\pi}(1+r^{-2})w_d|B_\theta|d\theta}
{\int_0^{2\pi}|B_\theta|d\theta}.
\]

这样 $\oint v\,d\sigma=\oint d\sigma$。它只固定总体尺度，并不额外承担闭合条件。

## 2. 唯一的闭合倾斜

中心线定义为

\[
\alpha_\theta=-v B\times B_\theta.
\tag{3}
\]

直接计算其竖直分量：

\[
(-B\times B_\theta)_z=-\frac{r^2}{1+r^2}\varphi_\theta,
\quad\varphi_\theta=1+2b\cos2x.
\]

代入 (2)，径向函数准确消去，因此轴向闭合等价于

\[
\int_0^{2\pi}w_d(x)(1+2b\cos2x)\,dx=0.
\tag{4}
\]

令 $Z(d)=\int w_d(x)dx$，并对概率密度 $w_d/Z(d)$ 记期望 $E_d$。方程 (4) 等价于

\[
E_d[\cos2x]=-\frac1{2b}.
\tag{5}
\]

对 $d$ 求导，

\[
\frac{d}{dd}E_d[\cos2x]=2\operatorname{Var}_d(\cos2x)>0.
\]

密度处处为正，而 $\cos2x$ 非常数，所以严格不等式成立。又因 $\ell$ 连续有界，指数权重在 $d\to\pm\infty$ 时集中到 $\cos2x$ 的极大/极小处；具体地，任意离开极值 $\varepsilon$ 的闭集，其权重与一个更接近极值的小开区间相比以指数速率消失。因此期望分别趋于 $1$ 和 $-1$。

因为 $b>1/2$，右侧严格位于 $(-1,0)$，连续性和严格单调性证明：**存在唯一有限实数 $d$ 使 (4) 成立。** 这是一条准确数学定义，而不是软罚项最小化。

## 3. 其余闭合与渐近周期

由于 $r,v$ 在 $\theta\mapsto\theta+2\pi/m$ 下不变，$B$ 和 $\alpha_\theta$ 的水平分量随之旋转 $2\pi/m$。对完整周期求和，水平闭合向量是一个被该非平凡平面转动固定的向量，故为零。结合 (4)，$\oint\alpha_\theta d\theta=0$，因此 (3) 定义一条闭曲线。

对反射 $S=\operatorname{diag}(1,-1,1)$，有 $B(-\theta)=SB(\theta)$。球面弧长速度、球面有符号曲率 $\kappa$ 和 $v$ 都是偶函数，$\kappa_\theta$ 是奇函数，故

\[
\oint\frac{\kappa_\sigma}{\sqrt v}\,d\sigma
=\int_0^{2\pi}\frac{\kappa_\theta}{\sqrt v}\,d\theta=0.
\]

于是存在唯一对 θ 取零均值的周期函数 $\omega$ 满足 $\omega_\sigma=\kappa_\sigma/(2\sqrt v)$。R7/R8 所需的原始中心线闭合与这一渐近周期条件都得到满足。九个完整二阶周期系数仍需另外求解。

若 $B_\theta\ne0$，由 $v>0$ 可知 $\alpha_\theta\ne0$。这只证明正则浸入。自交、非局部法球与足够厚度需要实际几何审计，不能从闭合本身推出。

## 4. 球面指示曲线的全角正则判据

由 (1)，

\[
|B_\theta|^2=\frac{r_\theta^2+r^2(1+r^2)\varphi_\theta^2}{(1+r^2)^2}.
\]

因此退化只可能发生在 $r_\theta=\varphi_\theta=0$。当 $\varphi_\theta=0$ 时，

\[
\cos^2x=c^2=\frac{1-1/(2b)}2\in(0,1/2),
\]

并且

\[
(\log r)_\theta=-m\sin x\,[\rho_1+4\rho_2\cos x+3\rho_3(4\cos^2x-1)].
\]

此处 $\sin x\ne0$。记 $A=\rho_1+3\rho_3(1-1/b)$，则两个可能括号是 $A\pm4\rho_2c$。因此

\[
\boxed{B_\theta\ne0\text{ 对全部角成立}
\quad\Longleftrightarrow\quad A^2-16\rho_2^2c^2\ne0.}
\tag{6}
\]

对于脚本中以 binary64 保存的有限参数，把这些数解释成准确有理数，(6) 可用 `Fraction` 无舍入地核验。它证明不退化，不给定量曲率或 reach 下界；接近零的判别式仍可能产生不可用尖峰。

## 5. 数值复现的固定数据要求

实现为 `scripts/literature_closed_codesign.py`。设计时每次用参考角积分求唯一倾斜的数值近似；设计结束后，把倾斜常数、所有几何/速度系数和归一化一起冻结，再做 768/1536/3072 点复核。后两级不得重新解倾斜或重算归一化来隐藏闭合残差。

所存倾斜是准确积分定义的数值近似，不是精确积分值的证明。输出同时保留真实中心线闭合向量、渐近周期、六项公式和两个新恒等式的残差；Fourier primitive 所减去的均值仍明确显示。

开发检查仅验证 32 点人工输入的代数公式，没有运行研究优化：轴向闭合标量约 $1.11\times10^{-16}$，竖直叉积恒等式和解析球面速度误差均约 $4.44\times10^{-16}$。这些不代表任何完整周期系数已经为零。实际设计只能在本公开仓库 GitHub Actions 执行。
