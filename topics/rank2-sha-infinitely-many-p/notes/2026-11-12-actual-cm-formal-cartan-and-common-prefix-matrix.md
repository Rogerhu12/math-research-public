# 真实 CM 的整形式 Cartan 作用与同一混合前缀矩阵

日期：2026-11-12。**状态：本文形式作用、整坐标、稀疏图形及共同
行矩阵均已证明。** 原有限次数多项式源的高次尾仍准确保留，
没有把形式线性化当作整个 $E_D$ 上的免费整基变换。

固定 R167–R170 的实际平面

$$
a(w)=\vartheta(z)^4,\qquad b(w)=\sigma(z)^4,\qquad w=z^4,
\qquad (a(0),b(0))=(1,0).
$$

本篇只处理惰性 $p\equiv3\pmod4$、$p\ge7$。记

$$
\mathcal O=\mathbb Z_p[i],\quad
r=(p+1)/4,\quad R=(p^2-1)/4=r(p-1).
$$

## 1. 每个固定阶 jet 的明确参数多项式

在原点用环境坐标 $X=a-1$、$Y=b$。
定义固定有理级数

$$
\mathcal L(s)=\frac{z}{u}
=\sum_{n\ge0}\frac{\binom{2n}{n}}{4^n(4n+1)}s^n,\qquad
q(s)=s\mathcal L(s)^4.
\tag{1.1}
$$

于是 $q(s)=w$，并且它是 $s(w)=b(w)/a(w)$ 的正式反函数。
再置

$$
A_0(s)=a(q(s))=\exp(W(s)/17)\in1+s\mathbb Q[[s]].
$$

对两个独立形式参数 $\lambda,d$，令 $s=Y/(1+X)$，定义

$$
\begin{aligned}
\mathscr F_{\lambda,d,1}(X,Y)
&=(1+X)^d A_0(s)^{-d}a(\lambda q(s))-1,\\
\mathscr F_{\lambda,d,2}(X,Y)
&=(1+X)^d A_0(s)^{-d}b(\lambda q(s)).
\end{aligned}
\tag{1.2}
$$

二项式及指数在这里按形式级数展开。对每个固定 $(i,j)$，
$[X^iY^j]\mathscr F_{\lambda,d}$ 是
$\mathbb Q[\lambda,d]$ 中的多项式：
$(1+X)^d$ 的有限系数是 $d$ 的二项式多项式，
$A_0^{-d}=\exp(-d\log A_0)$ 的有限系数亦为 $d$ 的多项式，
而 $a(\lambda q)$、$b(\lambda q)$ 的有限系数是 $\lambda$ 的
多项式。这给出了所需连续性的具体公式，而不是依赖次数不断变化
的 $F_\beta$ 的抽象极限。

对 $\beta\in\mathbb Z[i]\setminus\{0\}$，R170 的精确乘法关系给

$$
\mathscr F_{\beta^4,N\beta}(X,Y)
=\bigl(F_{\beta,1}(1+X,Y)-1,\,
       F_{\beta,2}(1+X,Y)\bigr).
\tag{1.3}
$$

因此 (1.2) 在这些参数值是已经证明的实际整多项式映射的完成。

还可直接从 (1.2) 核查半群式。其变换后的 $s$ 为
$s(\lambda q(s))$，故变换后的 $q$ 为 $\lambda q(s)$；
两次变换的 $A_0$ 因子准确消去，得到

$$
\mathscr F_{\lambda_1,d_1}\circ\mathscr F_{\lambda_2,d_2}
=\mathscr F_{\lambda_1\lambda_2,d_1d_2}.
\tag{1.4}
$$

这项恒等式发生在同一个环境形式邻域中，保留了正次数 theta
参考与全部 sigma 因子。

## 2. 从 Gaussian 整数延拓到真实整 p 进作用

对 $\alpha\in\mathcal O$，令 $\bar\alpha$ 为未分歧二次扩张的非平凡
自同构，置

$$
\mathscr F_\alpha
=\mathscr F_{\alpha^4,\alpha\bar\alpha}.
\tag{2.1}
$$

选 $\beta_n\in\mathbb Z[i]$ 趋于 $\alpha$。
R170 给 $\mathscr F_{\beta_n}\in\mathcal O[[X,Y]]^2$；
(1.2) 的固定阶系数多项式使其逐系数趋于 (2.1)。
$\mathcal O$ 闭，因此

$$
\mathscr F_\alpha\in\mathcal O[[X,Y]]^2.
\tag{2.2}
$$

这一步使用了 R170 在所有奇素数处的整性，未假定
$\alpha$ 的复取值，也没有把不可收敛的 sigma 级数代入一个扭点。
若 $\alpha$ 是单位，则 (1.4) 给其整逆
$\mathscr F_{\alpha^{-1}}$。

在实际曲线上，正式恒等式仍为

$$
\mathscr F_\alpha(a(w)-1,b(w))
  =(a(\alpha^4w)-1,b(\alpha^4w)).
\tag{2.3}
$$

可由 (1.2) 直接相消，也可对每个固定 $w$ 阶数从 Gaussian
整数的恒等式取系数极限；不涉及改变无穷求和次序。

令 $\mu=\mu_{p^2-1}\subset\mathcal O^\times$。对
$\alpha\in\mu$ 有 $\bar\alpha=\alpha^p$，从而
$N\alpha=\alpha^{p+1}$。$\mu_4$ 的作用为恒等，故得到阶数
$R=(p^2-1)/4$、素于 $p$ 的真实有限群作用。
它的线性特征在

$$
\Xi=X-Y/3,\qquad Y
$$

上分别是 $\alpha^{p+1}$ 与 $\alpha^4$。

## 3. 整 Cartan 坐标及共轭下降

取两条准确的角色平均

$$
\begin{aligned}
U(X,Y)
&=\frac1{p^2-1}\sum_{\alpha\in\mu}
 \alpha^{-(p+1)}\,\Xi(\mathscr F_\alpha(X,Y)),\\
V(X,Y)
&=\frac1{p^2-1}\sum_{\alpha\in\mu}
 \alpha^{-4}\,\mathscr F_{\alpha,2}(X,Y).
\end{aligned}
\tag{3.1}
$$

分母是单位；由 (2.2) 得 $U,V\in\mathcal O[[X,Y]]$。
线性项准确为

$$
U=X-Y/3+O((X,Y)^2),\qquad V=Y+O((X,Y)^2).
\tag{3.2}
$$

因此 $(X,Y)\mapsto(U,V)$ 是整形式坐标变换，整逆同样存在。
重排有限和给

$$
U\circ\mathscr F_\alpha=\alpha^{p+1}U,\qquad
V\circ\mathscr F_\alpha=\alpha^4V
\quad(\alpha\in\mu).
\tag{3.3}
$$

事实上这两个坐标属于 $\mathbb Z_p[[X,Y]]$。因为 (1.2) 的系数
有理，故
$\overline{\mathscr F_\alpha}=\mathscr F_{\bar\alpha}$；
对 (3.1) 共轭后以 $\alpha\mapsto\bar\alpha$ 重排求和，两个式子
均保持不变。这也说明没有额外把一个二次系数域的源格免费当成
原 $\mathbb Z_p$ 格。

## 4. 沿原曲线的完整稀疏性

以下 $U(w),V(w)$ 表示 (3.1) 沿同一个实际 $\gamma(w)$ 的取值。
由 (2.3) 及有限角色正交，

$$
\begin{aligned}
U(w)
&=\sum_{\substack{k\ge1\\ k\equiv r\;(\mathrm{mod}\ R)}}
 [w^k]\bigl(a(w)-1-b(w)/3\bigr)\,w^k,\\
V(w)
&=\sum_{\substack{k\ge1\\ k\equiv1\;(\mathrm{mod}\ R)}}
 [w^k]b(w)\,w^k.
\end{aligned}
\tag{4.1}
$$

所以

$$
U(w)=u_0w^r+u_1w^{r+R}+\cdots,\qquad
V(w)=w+v_1w^{R+1}+\cdots.
\tag{4.2}
$$

这里的首项准确满足

$$
v_p(u_0)=-1,\qquad
pu_0\equiv C_p/(17r)\pmod p.
\tag{4.3}
$$

为核准 (4.3)，(1.1) 中次数 $\le r-1$ 的分母 $4n+1$ 均不被
$p$ 除，故 $q(s)$ 及其反函数到次数 $r$ 整。
R167 给 $A_0(s)$ 在次数 $<r$ 整，而第 $r$ 项首极为
$C_p/(17rp)$。因此 $a(w)$ 的第 $r$ 项有同一首极，
而 $b(w)=s(w)A_0(s(w))$ 的次数 $\le r$ 系数均整。
从 $u_0=[w^r](a-1-b/3)$ 即得 (4.3)。
不能仅凭 (3.2) 的环境二次误差而略去这项低阶整性核对。

可再以 $v=V(w)$ 作输出参数。其逆具有
$w=v(1+O(v^R))$ 的形式，由 (4.2) 得

$$
\boxed{\quad U=v^r g(v^R),\qquad g(0)=u_0,\quad v_p(g(0))=-1.\quad}
\tag{4.4}
$$

这是一条由实际端同态作用得到的完整稀疏图形。
输出换参首项为一，故保持所有准确前缀消失条件及其首个非零
系数；不要求 $V(w)$ 的全部高阶系数整。
在第二个共振之前，(4.4) 特别给

$$
U=u_0v^r\pmod{v^{pr}},
\qquad pr=r+R.
\tag{4.5}
$$

R171 的旧图形 $a=f(b)$ 在 $2r,3r,\ldots$ 的真实分母传播与此不
矛盾：它们被 (3.1) 的整环境形式坐标重新组合。此组合的高次
源尾仍须保留，见下一节。

## 5. 同一个实际有限次数源的共同矩阵

原源固定为

$$
E_D=\mathbb Z_p[X,Y]_{\le D}.
$$

沿曲线以 $v=V(w)$ 为输出时，记
$\gamma_v(v)=(a(w(v))-1,b(w(v)))$。
用 (3.1) 的同一个整形式逆，将 $P\in E_D$ 写成

$$
\widetilde P(U,V)=P(X(U,V),Y(U,V))
=\sum_{\ell,j\ge0}L_{\ell,j}(P)U^\ell V^j.
\tag{5.1}
$$

每个 $L_{\ell,j}$ 都是这个同一源上的整线性泛函，算子范数至多
一。没有为不同列选择不同坐标变换，也没有增加自由的源参数。
对 $k<pr$，代入 (4.5) 得准确的一行

$$
[v^k]P(\gamma_v)
=\sum_{\ell=0}^{\lfloor k/r\rfloor}
u_0^\ell L_{\ell,k-r\ell}(P).
\tag{5.2}
$$

令 $k=rh+j$、$0\le j<r$，并令
$\pi_0=u_0^{-1}\in p\mathbb Z_p^\times$。等价地定义整行

$$
\Lambda_{h,j}(P)
=\sum_{q=0}^{h}\pi_0^q
L_{h-q,j+rq}(P).
\tag{5.3}
$$

则

$$
\boxed{\quad
[v^{rh+j}]P(\gamma_v)=u_0^h\Lambda_{h,j}(P)
\quad(rh+j<pr).
\quad}
\tag{5.4}
$$

所有低行都由同一个 (5.1) 得到。因而限制到全部先前准确零行的
饱和核后，真实 jet 范数恰为 $p^h$ 乘该整行在该核上的像理想
范数，而不是直接等于 $p^h$。
模 $p$ 时
$\Lambda_{h,j}\equiv L_{h,j}$，但高精度的 $q\ge1$ 项不能删去。

一个内在的解释是对 $\widetilde P$ 用单首一式

$$
V^r-\pi_0U
$$

作形式 Weierstrass 除法。其余式为
$\sum_{j<r}V^jR_j(U)$，而
$[U^h]R_j=\Lambda_{h,j}(P)$。
这一除法在 $\mathbb Z_p[[U]][[V]]$ 中合法：
非首系数 $-\pi_0U$ 在系数环的极大理想中；
对固定 $U^h$，(5.3) 只含有限的 $q\le h$，与实际取值相容。

## 6. 明确的高次源尾成本

因为 (3.2) 的 Jacobian 是单位，取全部
$L_{\ell,j}$、$\ell+j\le D$，确实在 $E_D$ 上给整可逆矩阵。
但 (5.3) 还会用到

$$
\ell+j+rq>D
$$

的高次 Taylor 泛函；它们一般不是零。
所以前一个有限矩阵可逆，不能推出整条 (5.3) 在相同次数源上
只需低次项。

可把遗漏项的成本准确记下。在 (5.2) 中截掉
$\widetilde P$ 的总次数 $>D$ 部分时，第 $k$ 行的遗漏仅来自

$$
\ell+(k-r\ell)=k-(r-1)\ell>D.
$$

由于对应 $L_{\ell,k-r\ell}$ 整，其输出估值至少
$-\ell$。因此当 $D<k<pr$，遗漏行的范数至多

$$
p^{\,\min\left(
\lfloor k/r\rfloor,\,
\left\lfloor\frac{k-D-1}{r-1}\right\rfloor
\right)}.
\tag{6.1}
$$

当 $k\le D$ 时没有遗漏。
这只是由真实共同坐标得到的尾界，不声称总次数 $\le D$ 的部分
单独满足先前的全部零行；实际前缀可能需要两部分相消。

完整 (5.2) 给出的不依赖 $D$ 上界是
$p^{\lfloor k/r\rfloor}$，与 R170/R173 的同一区间结果一致。
要得到次数敏感的严格预算，必须进一步控制
$\Lambda_{h,j}$ 在 (5.3) 的全部先前零行核上的像理想，
并将高次尾 (6.1) 与原来的两条实际中央失败条件联立。
本篇既没有把那些两条条件外推到所有乘积列，也没有将整形式
Cartan 线性化直接当成 $\mathrm{GL}(E_D)$。

## 依赖

- [R166 完整 theta 除法](2026-11-12-actual-theta-division-frobenius-and-full-ghosts.md)、
  [R167 固定闭合平面](2026-11-12-closed-theta-sigma-plane-and-integral-dynamics.md)：
  实际 $a,b$、参数与原输入。
- [R170 全 CM 映射](2026-11-12-full-cm-theta-plane-and-sparse-resonance.md)：
  Gaussian 整数处的全整性及准确半特征、Norm 和切向规范；
  本文的形式极限只在这些已付对象上进行。
- [R171 真逆级数的非线性传播](2026-11-12-theta-graph-nonlinear-propagation-and-common-blocks.md)：
  与 (4.4) 的不同坐标表示相容；不以其单列分母代替共同前缀范数。
