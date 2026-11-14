# 临界平方加正实尾：明确系数区间的真实单射稠密定理

日期：2026-11-12（UTC）。子任务：critical_kernel。**状态：以下参数区间已严格证明。** 本条处理 R77 的实际临界模型在正实时间上的一个完整区间，不修改已冻结的 R77 或 R71。

## 1. 定理及范围

取
$$
1<p\le\frac{17}{10},\qquad q=2p-1\in(1,12/5],
$$
并令
$$
S=L_p^2+cL_q,\qquad c>0
$$
为 R77 中的实际算子。设
$$
B_q=
\begin{cases}
20,&1<q\le2,\\
30,&2<q\le12/5,
\end{cases}
$$
$$
A(B)=2\arctan(B-1)+\frac\pi2
=\int_0^B\frac{dz}{1-z+z^2/2}.
\tag{1.1}
$$

**定理 1.1。** 若
$$
\boxed{c>\frac{A(B_q)}q,}
\tag{1.2}
$$
则 $S$ 单射且值域稠密。因此它把每个 $A$ 循环向量送成非零循环向量。

一个稍保守、形式更简单的充分条件是
$$
\boxed{c\ge\frac{3\pi}{2q},}
\tag{1.3}
$$
因为对每个有限 $B$ 都有 $A(B)<3\pi/2$。

这里的主指数上限来自已严格认证的纯 $q$ 尾负 BW 区间，而非实际截断误差或 Gevrey 估计。没有把结论扩到未认证的 $q>12/5$。

## 2. 有限 $m$ 上的精确 Gaussian 比较

记
$$
C_{p,m}=\sum_{j\ge m}\theta_{p,j}E_j,\quad
C_{q,m}=\sum_{j\ge m}\theta_{q,j}E_j,\quad
\theta_{s,j}=(j+2)^{-s},
$$
$$
V_m=C_{p,m}^2+cC_{q,m},\qquad
P(z)=1-z+z^2/2\quad(z\in\mathbb R).
$$
取正实时间 $t>0$。Gaussian Fourier 恒等式在实际有界算子上给
$$
e^{-tV_m^*}1=
\frac1{\sqrt{4\pi t}}
\int_{\mathbb R}e^{-s^2/(4t)}
e^{isC_{p,m}^*-tcC_{q,m}^*}1\,ds.
\tag{2.1}
$$
这是绝对可积的 Bochner 积分，证明与 R77 相同。

纯 $q$ 尾向量的范数为
$$
F_{q,m}(tc)=\|e^{-tcC_{q,m}^*}1\|
=\prod_{j\ge m}P(tc\theta_{q,j})^{1/2}.
$$
在积分内，逐位精确恒等式为
$$
\begin{aligned}
&\left\|(I+(is\theta_{p,j}-tc\theta_{q,j})E_j^*)1_j\right\|^2\\
&\qquad
=P(tc\theta_{q,j})+\frac{s^2\theta_{p,j}^2}{2}.
\end{aligned}
\tag{2.2}
$$
关键在于 $tc\theta_{q,j}$ 为实数，故没有关于 $s$ 的线性交叉项。

由 $\log(1+x)\le x$，
$$
\frac{\|e^{isC_{p,m}^*-tcC_{q,m}^*}1\|}
{F_{q,m}(tc)}
\le
\exp\left[
\frac{s^2}{4}
\sum_{j\ge m}
\frac{\theta_{p,j}^2}{P(tc\theta_{q,j})}
\right].
\tag{2.3}
$$
因此，只要
$$
\Gamma_m(t):=
t\sum_{j\ge m}
\frac{\theta_{p,j}^2}{P(tc\theta_{q,j})}<1,
\tag{2.4}
$$
对 Gaussian 直接积分得到有限 $m$ 的真实不等式
$$
\boxed{
\|e^{-tV_m^*}1\|
\le\frac{F_{q,m}(tc)}
{\sqrt{1-\Gamma_m(t)}}.}
\tag{2.5}
$$
没有将 $e^{-tC_{p,m}^{*2}}$ 的全空间范数单独提出；(2.5) 保留了两个尾在同一个乘积参考向量上的联合作用。

## 3. 临界指数恰好使条件可以显式积分

置 $M=m+2$，使用纯 $q$ 尾的变量
$$
v=\frac{tc}{M^q},\qquad t=\frac{vM^q}{c}.
$$
因为 $2p=q+1$，
$$
\Gamma_m(v)=
\frac{v}{cM}\sum_{j\ge m}
\frac{((j+2)/M)^{-(q+1)}}
{P(v((j+2)/M)^{-q})}.
\tag{3.1}
$$
其 Riemann 极限为
$$
\begin{aligned}
\Gamma(v)
&=\frac vc\int_1^\infty
\frac{x^{-(q+1)}}{P(vx^{-q})}\,dx\\
&=\frac1{qc}\int_0^v\frac{dz}{P(z)}
=\frac{A(v)}{qc}.
\end{aligned}
\tag{3.2}
$$
这个精确代换就是临界关系 $q=2p-1$ 的作用。

收敛关于每个固定 $v\in[a,b]$ 一致。可以直接给误差：记
$$
f_v(x)=x^{-(q+1)}/P(vx^{-q}).
$$
由于 $P\ge1/2$，在 $0<v\le B$ 上
$$
\int_1^\infty|f_v'(x)|\,dx
\le
2+\frac{4Bq(1+B)}{2q+1}
=:C_{q,B}.
$$
逐小区间的和积分比较遂给
$$
\boxed{
|\Gamma_m(v)-\Gamma(v)|
\le \frac{B C_{q,B}}{cM}
\qquad(0<v\le B).}
\tag{3.3}
$$

若 (1.2) 成立，设
$$
\Delta=1-\frac{A(B_q)}{qc}>0.
$$
在 R61 已认证的 $q$ 区间上，对充分大 $m$，(3.3) 保证
$$
\Gamma_m(v)\le1-\Delta/2.
\tag{3.4}
$$
所以 (2.5) 中的额外因子至多为固定常数 $\sqrt{2/\Delta}$，不贡献任何 $M$ 阶指数。

## 4. 搬回实际算子并完成核分离

R61 的纯 $q$ 尾公式给
$$
\log F_{q,m}(vM^q)=Mh_q(v)+O(1)
$$
在相应认证区间上一致成立。因此由 (2.5)、(3.4)，
$$
\log\|e^{-(vM^q/c)V_m^*}1\|
\le Mh_q(v)+O(1).
\tag{4.1}
$$

R77 已对实际 $S=L_p^2+cL_q$ 证明：

- 混合截断模型及实际 $S$ 有一致的权 $q-1$ 幂界；
- 头部理想幂零阶为 $2^k+m-k$，而非 $2m$；
- 取 $k=\lfloor\beta\log_2M\rfloor$、$1/4<\beta<1$ 时，在当前时间尺度上的真实误差为
  $$\exp[-c_0M^{4\beta}+O(M+\log M)].$$

故对任意实际核向量 $f$，R77 的头多项式次数为 $M+o(M)$、常数项为 $\langle f,1\rangle$，而 (4.1) 给它的边界。使用纯 $q$ 尾已经严格认证的
$$
g+\int h_q\,d\nu<0
$$
就迫使 $\langle f,1\rangle=0$。核在 $A$ 下不变，$1$ 对 $A^*$ 循环，所以核为零。$S\in\mathcal A$ 的复对称性给稠密值域。定理 1.1 得证。

## 5. 方向与尚未覆盖的参数

R79 已证明实 $c\ge0$ 时负实时间的精确联合尾轮廓处处为正；那个时间方向不可能给负 BW。本条改用正实时间，利用 Fourier-Gaussian 表示中真正正交的实、虚局部扰动，得到不同的、有效的联合作用界。

条件 (1.2) 以下的中间正实系数尚未由本条闭合；R75 的有限小型判据另覆盖零附近的一部分参数，二者不能未经比较就声称接上。复 $c$ 会在 (2.2) 中出现线性 $s$ 项，本条没有忽略它，也没有声称同一阈值对复系数成立。

对 $c<0$，R77–R79 的负实时间变分轮廓仍是另一条实际路线，不能用本条的纯 $q$ 尾负号直接替换。

这些均为明确算子类的结果，不是一般 Hilbert ISP 的完成证明。

