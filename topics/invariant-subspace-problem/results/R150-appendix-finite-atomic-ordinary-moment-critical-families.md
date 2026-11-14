# R150 附录：多物理方向的有限普通矩临界族

日期：2026-11-13（UTC）。作者：normal_rebuild / Astra-ISP-1cf8c51d。

状态：**已证明。** 这是完整 ordinary 多项式的有限代数结论，不是实际联合谱、非循环或新的全局 Jacobian 归属结论。

## 1. 一般多因子有限矩截面

令 $v(z)=(1,z,\ldots,z^{q-1})$，$F(Y)=\tfrac12Y^{\mathsf T}KY$ 为齐次二次式，且 $F(v(z))\equiv0$。固定 $h\ge2$ 及整数 $0\le k<h$，任取复参数 $\alpha_1,\ldots,\alpha_k,z_1,\ldots,z_k$。在足够大的有限次数 $D\ge2h$ 内，规定
$$
y_j=\sum_{\nu=1}^k\alpha_\nu z_\nu^j,
\qquad
W_{d,m}=\frac{(d-1)!}{2^{d-1}}
\sum_{\nu=1}^k\alpha_\nu^d z_\nu^m
\quad(2\le d\le D).
\tag{1.1}
$$
全部合并物理键 $(d,m)$ 各只保留一个坐标。

**定理。** 式 (1.1) 是完整 $\mathcal Q_{F^h}$ 的零临界点。并且，对每个齐次多项式 $P$，若 $k<\deg P\le D$，则
$$
\boxed{\mathcal Q_P(y,W)=0.}
\tag{1.2}
$$
任意固定 $P$ 都可先取 $D\ge\max(2h,\deg P)$ 再应用此式。特别，任意 first $a=r\cdot Y$ 的匹配完整 Bell 多项式 $\mathcal Q_{a^h}$ 都在这个族上为零。

证明。记 $t=(t_0,\ldots,t_{q-1})$。完整普通矩的生成函数为
$$
\begin{aligned}
M(t)
&=\exp\left[y\cdot t+
\sum_{d=2}^D\frac{(-2)^{d-1}}{d!}
\sum_mW_{d,m}\sum_{i_1+\cdots+i_d=m}
t_{i_1}\cdots t_{i_d}\right]\\
&=\exp\left[\sum_{\nu=1}^k\sum_{d=1}^D
\frac{(-1)^{d-1}}d
\big(\alpha_\nu v(z_\nu)\cdot t\big)^d\right]\\
&=\prod_{\nu=1}^k\big(1+\alpha_\nu v(z_\nu)\cdot t\big)
\pmod{\deg t>D}.
\end{aligned}
\tag{1.3}
$$
因此这个完整矩泛函准确等于
$$
\boxed{
\Lambda(P)=\mathcal Q_P(y,W)
=\left[\prod_{\nu=1}^k
\big(I+\alpha_\nu v(z_\nu)\cdot\nabla\big)P\right]_{Y=0}.
}
\tag{1.4}
$$
右侧只取 $P$ 的零至 $k$ 次齐次项，故 (1.2) 成立。式 (1.3) 是截断多项式恒等式，不要求真实测度、正性或级数收敛。

再核全部临界条件。由 $F(v(z))=0$，
$$
(v(z)\cdot\nabla)^dF^h
=\frac{h!}{(h-d)!}F^{h-d}
\big(v(z)^{\mathsf T}KY\big)^d
\quad(0\le d\le h),
\tag{1.5}
$$
且 $d>h$ 时为零。对 $d\le h$，(1.5) 为次数 $2h-d\ge h>k$ 的齐次多项式，故被 (1.4) 送为零。比较 $z$ 的系数，再使用
$$
\partial_{W_{d,m}}\mathcal Q_{F^h}
=\frac{(-2)^{d-1}}{d!}\mathcal Q_{\mathcal D_{d,m}F^h}
\quad(d\ge2)
$$
以及一次坐标的相应公式，得到完整显示梯度全零。一次方向 $v(z)$ 张成全部一次坐标。$F^h$ 自身次数 $2h>k$，所以临界值也为零。所有未出现的高阶显示变量的偏导本来就为零。证毕。

同一个证明还处理外多项式 $Q(F)$：只要其每个非零正次系数的支撑次数都大于 $k$，(1.1) 就是完整 $\mathcal Q_{Q(F)}$ 的临界点，临界值为 $Q(0)$。

这扩展了[旧单方向完整矩截面](../notes/2026-11-13-complete-ordinary-moment-sections-and-bell-denominator-degree-obstruction-1cf.md)；不同 $z_\nu$ 同时存在，不能把它们合并成同一条物理直线。

## 2. 六模式立方的四参数临界族

现在取原六模式 $F_0$，令 $h=3,k=2$。记两因子参数为 $a,b,s,t$。第一、二、三层完整矩为
$$
y_j=a s^j+b t^j,
\qquad
H_m=\frac12(a^2s^m+b^2t^m),
\qquad
V_n=\frac12(a^3s^n+b^3t^n).
\tag{2.1}
$$
这里 $0\le j\le5$、$0\le m\le10$、$0\le n\le15$。全部较高显示层按 (1.1) 填充；它们对目标的完整梯度无贡献。

式 (2.1) 的全部完整第三矩均为零。它不是要求第三阶累积量 $V$ 为零，而是准确的张量恒等式
$$
\mathcal Q_{(r\cdot Y)^3}(y,H,V)=0
\quad\text{对所有 }r\in\mathbb C^6.
\tag{2.2}
$$
由上一节，完整 $\mathcal Q_{F_0^3}$ 的值及全部偏导也为零。

当 $ab(s-t)\ne0$ 时，仅看 $y_0,y_1,y_2,y_3$，其对 $(a,b,s,t)$ 的 Jacobian 是四列
$$
v_{\le3}(s),\quad v_{\le3}(t),\quad
a v_{\le3}'(s),\quad b v_{\le3}'(t),
$$
行列式为 $\pm ab(s-t)^4\ne0$。所以该像族的维数恰为四；不能把完整立方临界集只看成三参数的单方向族。

## 3. 原曲线族是两方向碰撞层

在 $s=t=z$ 时，(2.1) 变成
$$
y_j=\gamma z^j,
\qquad H_m=h_0 z^m,
\qquad V_n=\frac{6\gamma h_0-\gamma^3}{4}z^n,
\tag{3.1}
$$
其中 $\gamma=a+b$、$h_0=(a^2+b^2)/2$。任取复数 $\gamma,h_0$，都可取 $a,b$ 为
$$
X^2-\gamma X+\frac{\gamma^2-2h_0}{2}=0
$$
的两个根。因此旧的整个单方向立方临界族都包含在这个碰撞层中。

特别，在基点
$$
p_0:\quad y_0=\cdots=y_5=1,\qquad H_0=\cdots=H_{10}=0,
\tag{3.2}
$$
可取 $a=(1+i)/2,b=(1-i)/2,s=t=1$；相应 $V_n=-1/4$。这是真正完整临界点。

## 4. 基点附近的准确有理图

以下给出后续局部消元可直接使用的同一四参数族。置
$$
\gamma=y_0,\qquad m=y_1,\qquad h_0=H_0,\qquad k=H_1,
$$
并要求
$$
(\gamma^2-2h_0)(4h_0-\gamma^2)\ne0.
\tag{4.1}
$$
此条件在 (3.2) 成立。由 $a+b=\gamma$、$ab=(\gamma^2-2h_0)/2$ 及两条一次矩方程，得到位置的准确对称数
$$
S=s+t=\frac{2(\gamma m-2k)}{\gamma^2-2h_0},
$$
$$
P=st=
\frac{4\gamma km-8k^2-(\gamma^2-2h_0)m^2}
{(\gamma^2-2h_0)(4h_0-\gamma^2)}.
\tag{4.2}
$$
然后用同一递推 $u_{j+2}=S u_{j+1}-P u_j$ 定义全部 $y,H,V$，初值分别为
$$
(y_0,y_1)=(\gamma,m),\qquad
(H_0,H_1)=(h_0,k),
$$
$$
(V_0,V_1)=
\left(\frac{\gamma(6h_0-\gamma^2)}4,
\gamma k-\frac{(\gamma^2-2h_0)m}{4}\right).
\tag{4.3}
$$
这些有理式由 (2.1) 直接得到，反向先取振幅二次式的两根 $a,b$，再由 $as+bt=m$ 与 $a^2s+b^2t=2k$ 恢复 (2.1)，所以它们给出同一个完整临界族；(4.1) 保证所有分母为单位。

其第一个剩余一次坐标为
$$
\boxed{
y_2=\Phi(\gamma,m,h_0,k)=
\frac{8\gamma k^2-16h_0km+\gamma(6h_0-\gamma^2)m^2}
{(\gamma^2-2h_0)(4h_0-\gamma^2)}.
}
\tag{4.4}
$$
特别固定 $\gamma=m=1,h_0=0$，令 $u=y_2-1$，则
$$
S=2-4k,\quad P=1-4k+8k^2,
\qquad \boxed{u+8k^2=0.}
\tag{4.5}
$$
这是基点附近一条实际完整临界分支的准确方程，不是只到某个次数成立的 Taylor 近似。

经[完整第三矩 Schur 换元](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)，(2.1) 上 $Z=0$。因此 (4.2)–(4.4) 的 $(y,H)$ 图上，$R_3$ 和其全部十七个偏导均为零，而且每个匹配 $B_r$ 均为零。这一完整有理图可以用于局部理想计算；它不穷尽全局临界集。

## 5. 范围

这里构造了更多完整临界点，并同时证明它们不能反驳匹配 Bell 分母。没有由“在这些点上消失”推出全局根理想或自然幂归属。两指定全等向三平面的其他截面见[平面矩定理](R150-appendix-isotropic-three-plane-moment-critical-sections-and-matched-bell-values.md)；任意完整临界点的分类、全局立方证书及原普通 ISP 仍开放。
