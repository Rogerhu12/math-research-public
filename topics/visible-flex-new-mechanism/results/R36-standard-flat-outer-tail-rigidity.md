# R36：二重 C 根的标准指数平尾、真实光滑芽及相位唯一性

日期：2026-11-14。root 全文审读，repo_sources 独立核对复 Laplace 积分、快速 Green 核、标准前三阶 jet 与适用范围。把先前指数主阶诊断加强为实际存在与唯一性。没有运行新的研究数值计算。

**范围。** 本稿覆盖在一个二重端根上满足前三阶标准指数 jet 的外尾。准确假设是 $q$ 在端点内侧不为零，且对某个实数 $\lambda>0$，

$$t^{2j}\frac{q^{(j)}(t)}{q(t)}\longrightarrow\lambda^j,
\qquad j=1,2,3.\tag{1}$$

不预设第四阶渐近，不预设幂次前因子或复幅值极限。本文证明：这种尾必有唯一的实 $C^\infty$ 前因子，只剩一个公共复幅相。没有证明任意全平 $C^\infty$ 外尾都自动满足 (1)。

## 1. 弱方程和指数率的必要性

采用内向坐标 $t\ge0$，实际八系数满足

$$L[q]=Aq+2Bq'-2Cq'',\quad B=C'-W,\quad
A=2W'-\frac43C'',$$

并设

$$C(t)=ct^2+dt^3+O(t^4),\qquad
W(t)=w_0+w_1t+O(t^2),\qquad c\ne0.\tag{2}$$

系数实解析。使用 R34 的全区间弱式

$$ (Lp)'+ap=0,\qquad
p=q''',\quad a=A'q+(A+2B')q'-2Wq''.\tag{3}$$

由 (1) 的第一条，$\operatorname{Re}(q'/q)\ge\lambda/(2t^2)$ 在足够小的区间成立。固定一个内点后向端点积分，得 $q(t)$ 的模比任意幂次衰减得更快；再由其余两条，$q',q'',q'''$ 的值也比任意幂次衰减得更快。因此下述 $Lp$ 的端点值确为零。

先记

$$\ell=-2\lambda(w_0+c\lambda).$$

(1)–(2) 给

$$L/q=\ell t^{-2}+o(t^{-2}),\qquad
p/q=\lambda^3t^{-6}+o(t^{-6}),$$

$$a/q=-2w_0\lambda^2t^{-4}+o(t^{-4}).$$

需要的端点积分比准确为

$$\int_0^t\frac{q(s)^2}{s^{10}}\,ds
=\frac{q(t)^2}{2\lambda t^8}\{1+o(1)\}.\tag{4}$$

它对复 $q$ 也成立。证明是令 $y=1/s-1/t$：对每个固定 $y\ge0$，

$$\frac{q(t/(1+ty))}{q(t)}\longrightarrow e^{-\lambda y},$$

因为该比值为 $q'/q$ 沿正实区间的指数积分。同时其模至多为 $e^{-\lambda y/2}$。换元后 (4) 左侧除以 $q(t)^2/t^8$，成为

$$\int_0^\infty
\left\{\frac{q(t/(1+ty))}{q(t)}\right\}^2(1+ty)^8\,dy.$$

固定小 $\delta$ 后以 $e^{-\lambda y}(1+\delta y)^8$ 支配，支配收敛给极限 $1/(2\lambda)$。乘上一个趋于常数的系数时同样适用。

将弱式 (3) 从零积分，$Lp=-\int_0^t ap\,ds$。由 (4) 比较 $q(t)^2/t^8$ 的系数，得到

$$\ell\lambda^3=w_0\lambda^4,$$

$$\boxed{\quad \lambda=-\frac{3w_0}{2c}>0,\qquad
\ell=-\frac{2c\lambda^2}{3}\ne0.\quad}\tag{5}$$

这也排除了待定 $\ell=0$ 的可能；推导没有先除以 $L$ 或假设 $q^{(4)}$。由 (5)，$L$ 在整个删去端点的近邻不为零，弱式自动恢复经典四阶 ODE。

## 2. 正确幂次、快速主算子与三个严格负特征值

定义实数

$$\mu=\frac{14}{3}-\frac{d\lambda}{c}-\frac{3w_1}{2c},\qquad
f(t)=t^\mu e^{-\lambda/t},\quad t>0.\tag{6}$$

直接将 $f'/f=\lambda/t^2+\mu/t$ 代入 $Q[f]$，给出前两个系数：

$$\begin{aligned}
t^{10}\frac{Q[f]}{f^2}
={}&-2\lambda^5(2c\lambda+3w_0)\\
&-\frac{2\lambda^5}{3}
 (6c\mu-28c+6d\lambda+9w_1)t+O(t^2).
\end{aligned}\tag{7}$$

这里第二行已采用第一行的指数关系；(5)–(6) 使这两个系数都为零。

令 $\mathscr D=t^2\partial_t$，置 $q=fv$。普通导数可换成 $\mathscr D$ 的多项式，例如

$$q''=t^{-4}(\mathscr D^2-2t\mathscr D)q,\qquad
\mathscr D(fv)=f(\mathscr D+\lambda+\mu t)v.$$

因此把 $Q[fv]$ 除以 $f^2t^{-10}$，所得式对 $t$ 和 $v,\mathscr Dv,\mathscr D^2v,\mathscr D^3v,\mathscr D^4v$ 解析，并且对最高快速导数一次。当 $t=0$、$v=\alpha\ne0$、其余三个导数为零时，最高系数为 $\ell\alpha\ne0$，可正规化为

$$\mathscr D^4v=F(t,v,\mathscr Dv,\mathscr D^2v,\mathscr D^3v).$$

$F$ 一次齐次，故可除去公共幅相。设

$$y_1=\frac{\mathscr Dv}{v},\quad
y_2=\frac{\mathscr D^2v}{v},\quad
y_3=\frac{\mathscr D^3v}{v}.$$

得到

$$\mathscr Dy=Jy+N(t,y),\qquad
J=\begin{pmatrix}
0&1&0\\
0&0&1\\
-6\lambda^3&-11\lambda^2&-6\lambda
\end{pmatrix},$$

$$\operatorname{spec}J=\{-\lambda,-2\lambda,-3\lambda\}.\tag{8}$$

其主多项式可独立从指数交叉项检查：在 $f$ 上用扰动 $h=e^{-M/t}$ 线性化，$t^{10}DQ_f[h]/(fh)$ 的常数项为

$$-\frac{2c\lambda^2}{3}
M(M-\lambda)(M+\lambda)(M+2\lambda).$$

相对变量的快速指数为 $M-\lambda$，去掉公共幅值的零根后，正好得到 (8) 的三个负数。

由 (7) 消去常数和一次残差，非线性满足

$$N(t,0)=O(t^2),\qquad
N(t,y)=O(t^2+t|y|+|y|^2),\qquad
D_yN=O(t+|y|).\tag{9}$$

这一步保留了正确的 $\mu$；只消去指数率不足以得到后面的有限幅值极限。

## 3. 有界 Green 核给真实 C∞ 前因子

系统 (8) 的有界端点解满足

$$\boxed{\quad
y(t)=\int_0^t
e^{J(1/s-1/t)}N(s,y(s))\,\frac{ds}{s^2}.
\quad}\tag{10}$$

由于 $J$ 的特征值严格为负，

$$K_0=\int_0^\infty\|e^{Jr}\|\,dr<\infty.$$

换元 $r=1/s-1/t$ 可见，(10) 的 Green 核在无权上确界范数中的界为 $K_0$；在权范数
$\|y\|_2=\sup |y(t)|/t^2$ 中也不超过 $K_0$，因为 $s/t\le1$。

由 (9)，在足够短的区间上，(10) 在一个固定的 $O(t^2)$ 球中自映射且为收缩，因而得到真实的连续解 $y=O(t^2)$。它在 $t>0$ 为光滑解。

为说明零点处也是真正的 $C^\infty$，可以逐阶构造实多项式 $P_N(t)$，使系统残差为 $O(t^{N+1})$。因为 $J$ 可逆，每阶新系数都由一个固定的可逆线性方程决定；$\mathscr D(t^n)=nt^{n+1}$，所以不出现正整数共振。首两项为零。

对 $y-P_N$ 使用同一个 Green 算子和权 $t^{N+1}$，得到

$$y-P_N=O(t^{N+1})$$

对任意 $N$ 成立。识别为原来的解使用无权小球的唯一性。再从正规一阶式逐次求导，每次至多损失两个 $t$ 幂；对任意固定导数阶先取足够大的 $N$，便得所有导数的端点极限与相应多项式一致。因此 $y$ 有 $C^\infty$ 延拓，且 $y_1/t^2$ 也为 $C^\infty$。本证明不要求其 Taylor 级数收敛。

定义

$$v_1(t)=\exp\left(\int_0^t\frac{y_1(s)}{s^2}\,ds\right),\qquad
v_1(0)=1.\tag{11}$$

它为真实实 $C^\infty$ 函数。三维系统的前两条方程是
$\mathscr Dy_1=y_2-y_1^2$、$\mathscr Dy_2=y_3-y_1y_2$，故恢复后这三个 $y_j$ 确为 $v_1$ 的相应导数比。于是

$$q_1(t)=t^\mu e^{-\lambda/t}v_1(t)$$

准确满足 $Q=0$。它与零作 $C^\infty$ 拼接，任意复常数倍 $\alpha q_1$ 也是真解。

## 4. 所有满足标准前三阶指数 jet 的弱尾都只有一个相位

回到 §1 的任意候选 $q$。令 $v=q/f$；(1) 及 $\mathscr Df/f=\lambda+\mu t$ 给

$$\frac{\mathscr D^jv}{v}\longrightarrow0,\qquad j=1,2,3.$$

这不需要预先知道 $v$ 的模有界，或假设 $v$ 有非零极限。只使用前三阶导数比即可得到 $y\to0$。

由 (5)，删去端点后 $L\ne0$，所以该 $y$ 满足经典系统 (8)。变分常数公式的下端项
$e^{J(1/s-1/t)}y(s)$ 随 $s\downarrow0$ 趋零，故它必满足 (10)。

在无权小球 $\|y\|_\infty\le\varepsilon$ 内，(9) 和 $K_0<\infty$ 给 Lipschitz 常数
$K K_0(\delta+2\varepsilon)$。先取小球再缩区间，可使其小于一。因而所有趋零的连续解都与 §3 的真实 $C^\infty$ 解相同。

现在这个唯一的 $y_1/t^2$ 可积，积分 $v'/v=y_1/t^2$ 强制

$$v=\alpha v_1,\qquad \alpha\in\mathbb C\setminus\{0\}.$$

因此任意候选必为

$$\boxed{\quad q(t)=\alpha t^\mu e^{-\lambda/t}v_1(t).\quad}\tag{12}$$

尤其，幂次 $\mu$、有限非零幅值极限及前因子的实性都是结论，而非假设。标准指数率下的更快全平修正也不能增加新的复相位参数。

## 5. 同号 C 的正性链与两个二重外根

设 $a<b$，左端满足上述二重根和标准指数条件，$q\in C^3([a,b])$ 满足完整弱式，并且
$C$ 在 $(a,b)$ 不为零。通过整体符号和公共复幅值归一，可使 $C>0$，左端 $c>0$，且 (12) 的 $\alpha=1$。

于是近左端

$$q',q'',q'''>0,\qquad
L=-\frac{2c\lambda^2}{3t^2}q\{1+o(1)\}<0.$$

弱式仍给准确恒等式

$$Z=L^2q''',\qquad Z'=-2LC(q''')^2.$$

在初始实正分支上 $Z>0$ 且严格增加。与 R19 相同，任何有限的首次 $L=0$ 或 $q'''=0$ 都与 $Z$ 的严格正下界矛盾；$q',q''$ 一直增加。正常 ODE 唯一性又保持实相位。全局 $C^3$ 保证这些量在任意内点有限，因此符号链持续到右端。

结果是 $q'(x)>0$ 遍及 $(a,b)$，所以 $q(b)\ne0$。因此这种标准平尾不可能在同号 $C$ 区间内返回零；不需要尾矩满秩或三矩条件。

特别地，若非零的至多四次多项式 $C$ 在两个不同外端各有一个二重根，则它只能为

$$C(x)=c_*(x-a)^2(x-b)^2,\qquad c_*\ne0.$$

其内部始终同号。故在这类双端几何中，只要任意一侧满足本文的标准指数 jet，就不可能完成一个非零的两端零 profile。

## 6. 尚未处理的端尾

本稿真正证明了实际 $C^\infty$ 标准指数芽的存在及同类全部 $C^3$ 弱尾的相位唯一性；它不只是有限指数展开或形式线性模式计算。

仍未证明的是：任意全平弱尾都必具有 (1) 的标准指数 jet；更高重数端根、非标准快速振荡尾以及其他局部场和有限弯曲机制，也不由本稿一概排除。双端结论明确依赖相应的根结构或内部同号条件。

本课题的闭嵌入有限连续族、握持位移及 reach 要求仍未完成。

