# R384：完整纯 δ 四次系数的自然像恰为二维，以及其正锥边界

日期：2026-11-15。**有限纸面推导；未执行新的符号、积分、秩或人工研究计算。**

本稿只计算原完整正规系数的一个自然线性像。来源是
[R370](R370-complete-quartic-velocity-cost-and-exact-C2-total-flux.md) 的完整 $-\Psi(u,n)$ 四次成本，
[R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md) 的自然读出，
及 [R382](R382-universal-cancellation-of-the-corrected-H-total-flux-and-independent-Q4.md) 的全状态 H 零值。
没有恢复旧 H 的非零或秩结论。

## 1. 两个固定 profile 泛函

对同一右锚下任意实紧光滑 $u$，记
$$
r=u'',\qquad
X(u)=\int x r^5,\qquad M(u)=\int r^5.
$$
定义自然读出映射
$$
\mathcal N(V)(u)=\Lambda_u(V).
$$
原 $\mathcal R\subset\ker\mathcal N$。R382 又严格给出
$$
\mathcal N(\mathcal H_i(S))=0
$$
对全部真实状态 $S$ 及 $i=1,2$ 成立。这里是整个 profile 泛函为零，并非只在一个测试 profile 上零。

固定 $h=1$，用
$$
\mathcal Q(d)=\mathcal Q_\delta(1,k,k+d)
$$
表示 R370 的完整纯 $\delta^4$ 系数。该系数属于原真实有限环境 $U$，且其自然像不依赖此处自由的 $k$：
$$
\boxed{\mathcal N(\mathcal Q(d))=\frac{X+dM}{80}.}
\tag{1}
$$
每个有限 $d$ 均可由足够大的有限 $k$ 实现正 $\omega=k+d$，也可满足预定的有限物理下界。这只是选择真实系数状态；未声称这些状态共用另一个既有固定度量。

## 2. 同一有限窗口中的独立性

取非零非负偶紧 bump $\eta$，选小的正间隔 $b$ 使三个支撑不交，令
$$
r_{x_0}(x)=\eta(x-x_0)
-\frac12\eta(x-x_0-b)
-\frac12\eta(x-x_0+b).
$$
准确有 $\int r_{x_0}=\int xr_{x_0}=0$，故 $u_{x_0}=J^2r_{x_0}$ 真正紧支撑。
由于支撑不交且 $\eta^5$ 为偶函数，
$$
M(u_{x_0})=\frac{15}{16}\int\eta^5>0,\qquad
X(u_{x_0})=x_0M(u_{x_0}).
\tag{2}
$$
可预先选择同一个有限窗口及公共 collar，使至少两个不同的 $x_0$ 都合法。

若 $aX+b_0M$ 在该窗口的全部紧 profile 上恒零，将两个不同的 $x_0$ 代入(2)，得到 $a=b_0=0$。
因此 $X,M$ 是两个真正独立的 profile 泛函。

记 $\mathscr Q_\delta=\operatorname{span}_{\mathbb R}\{\mathcal Q(d):d\in\mathbb R\}$。
(1)给上界二，而
$$
\mathcal N(\mathcal Q(d_1)-\mathcal Q(d_0))
=\frac{d_1-d_0}{80}M\quad(d_1\ne d_0)
$$
与(2)给下界二。所以
$$
\boxed{
\mathcal N(\mathscr Q_\delta)=\operatorname{span}\{X,M\},
\qquad
\dim\frac{\mathscr Q_\delta}{\mathscr Q_\delta\cap\ker\mathcal N}=2.}
\tag{3}
$$

这个等式并不计算 $U/\mathcal R$ 的全部维数。
它只给该完整系数族的自然像；$\ker\mathcal N$ 也没有被识别为 $\mathcal R$。
由于全部 H 自然像为零，(3)的两个方向也不能由 $\mathcal R$ 与全部实际 H 的线性包产生。

## 3. 正系数锥并不是整个二维平面

考虑完整纯 $\delta^4$ 系数的有限非负组合。由(1)，
$$
\mathcal N\!\left(\sum_{j=1}^n\lambda_j\mathcal Q(d_j)\right)
=aX+b_0M,\quad
a=\frac1{80}\sum_j\lambda_j,\quad
b_0=\frac1{80}\sum_j\lambda_jd_j,\quad \lambda_j\ge0.
$$
若有非零权，则 $a>0$。反之，给定任意 $a>0,b_0\in\mathbb R$，
只需一个真实有限中心 $d=b_0/a$ 和权 $\lambda=80a$。
故准确的系数正锥是
$$
\boxed{
\mathcal N\bigl(\operatorname{cone}\{\mathcal Q(d)\}\bigr)
=\{0\}\cup\{aX+b_0M:a>0,\ b_0\in\mathbb R\}.}
\tag{4}
$$
其闭包是 $a\ge0$ 的闭半平面。
其中 $a=0,b_0\ne0$ 的边界值不由任何有限非负组合实现；
以(4)逼近这类值须让中心 $b_0/a$ 无界，不能把此极限当成一条有限路径。

如果从起点把中心限制在闭区间 $[d_-,d_+]$，
相应有限正锥准确变为
$$
\{0\}\cup
\{aX+b_0M:a>0,\ d_-\le b_0/a\le d_+\}.
\tag{5}
$$
这是因为 $b_0/a$ 是中心的真实加权平均，且反向仍可用一个中心实现。

## 4. 与实际路径控制的边界

对固定的一个 $u$，(1)是标量
$(X(u)+dM(u))/80$。
当 $M(u)\ne0$，中心穿过 $-X(u)/M(u)$ 就会改变该标量的符号；
这与(4)中的 $X$ 系数一直为正完全相容。

但真实路径还必须满足水平关系、矩阵和第三历史闭合，并支付低导数项、所有桥与完整第四传递。
(3)不能自动给实际二维控制，(4)也不能当作包含这些额外成本后的实际路径集合。
快速脉冲若要利用上述标量两号，必须另外证明全部大加速度项消失、真实矩阵可补、桥成本有统一界，并在有限参数处解出目标。
那些步骤是独立的实际问题，不由系数线性代数代付。

本稿完成的是完整纯 $\delta^4$ 系数的**准确二维自然像及有限正锥**；
同一固定度量、完整 period、全时嵌入和 reach 均未由此得到。
