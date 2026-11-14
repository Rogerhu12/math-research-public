# 实际 Laplace 行的分部积分与同一开曲线上的恰当微分检查

日期：2026-11-12。状态：本文的解析恒等式和 $p=7$ 的精确检查已证明。
它限定的是自然完整行与通常 de Rham 类的直接比较；没有排除
实际简单极点子空间上的另一个、仍需证明的 Coleman 或 Frobenius 比较。

## 1. 沿用真正的共同参考

采用[固定同源与归一解析行](2026-11-12-inert-fixed-isogeny-jets-and-normalized-rows.md)
的规范。令

$$
 E_0:y^2=x^3-x,\quad dz=\omega=\frac{dx}{2y},\quad
 \delta=\frac d{dz},\quad \alpha=4-i,\quad N=17,
$$

$$
 f_0(z)=\theta_T(\alpha z),\qquad
 \mathcal D=[\alpha]^{-1}T\setminus\{T\},\qquad
 U=E_0\setminus\mathcal D.
$$

写 $V=x^{-2}$，并记已经固定的

$$
 \begin{aligned}
 q(V)&=V+\frac35V^2-\frac15V^3+\frac15V^4,\\
 u_\alpha(V)&=1+(12-20i)V+(-10+28i)V^2
                 +(-20-12i)V^3+(1+4i)V^4,\\
 R_*&=\frac{q(V)}{u_\alpha(V)},\qquad A=f_0R_*.
 \end{aligned}                                                \tag{1}
$$

$R_*$ 在 $O$ 为四阶零点，仅在 $\mathcal D$ 的十六个点有简单极点。
固定惰性 $p\ge7$，令 $d=p+1$，$c$ 为 sigma 在正式参数中的首坏项，
$v_p(c)=-1$，$a=Nc$。

对在 $O$ 正式盘整的固定有理函数 $R$，置

$$
 F=f_0R=e^{az^d}G_F,\qquad
 J_F(u)=\sum_{h\ge0}[z^{dh}]G_F\,a^{-h}(u)_h,
 \quad (u)_h=u(u-1)\cdots(u-h+1).
                                                               \tag{2}
$$

前文的半径 $\rho=p^{-1/(2p)}$ 及相同的整有理函数界保证此函数
实际解析；它不要求 $F$ 在整个复曲线上全纯。
准确插值为

$$
                  J_F(k)=k!a^{-k}[z^{dk}]F.                   \tag{3}
$$

$J_{f_0}(0)=1$。定义归一行

$$
 K_R(u)=\frac{J_{f_0R}(u)}{J_{f_0}(u)},\qquad
 \ell_p(R)=K_R'(0).
                                                               \tag{4}
$$

它是关于 $R$ 的线性泛函，$K_R(0)=R(O)$，且

$$
                           \ell_p(1)=0.                      \tag{5}
$$

当 $R(O)=0$ 时，$\ell_p(R)=J_{f_0R}'(0)$。
这些定义保留全部指数卷积和完整解析尾项。

## 2. 自然分部积分算子含有实际参考连接

对一个满足上述解析界的 $G$，定义

$$
 \mathscr L_a(G)=
  \sum_{h\ge1}(-1)^{h-1}(h-1)!
                         [z^{dh}]G\,a^{-h}.
                                                               \tag{6}
$$

它就是 $J_{e^{az^d}G}'(0)$。相关各项的赋值至少以正的线性速率
增长，因此以下逐项移位、乘以 $h$ 及求和均合法。
令 $E=z\partial_z$。直接移位 $h\mapsto h-1$ 得

$$
 \boxed{\quad
 \mathscr L_a\left(\frac EdG+az^dG\right)=G(0).
 \quad}                                                       \tag{7}
$$

具体地，第一项是
$\sum_{h\ge1}(-1)^{h-1}h![z^{dh}]G/a^h$；
第二项是 $G(0)$ 减去同一个和。

等价地，回到 $F=e^{az^d}G$ 后有完整解析恒等式

$$
                     J_{zF'/d}(u)=uJ_F(u).                   \tag{8}
$$

也可先用 (3) 对非负整数 $k$ 逐系数证明，再由解析性证明 (8)。
对 $F=f_0R$，真正被 (8) 处理的算子是

$$
 \mathcal D_pR
   =\frac zd\left(\delta R+\frac{\delta f_0}{f_0}R\right),
 \qquad K_{\mathcal D_pR}(u)=uK_R(u),\qquad
 \ell_p(\mathcal D_pR)=R(O).                                 \tag{9}
$$

这里可把定义域扩到满足同一收敛界的正式解析函数，
但 $\mathcal D_p$ 一般不是 $K(E_0)$ 上的代数微分算子。
它包含正式椭圆对数 $z$，以及

$$
 \frac{\delta f_0}{f_0}
   =17\left(\zeta(z)+\frac{y(z)}{x(z)}\right)
         +\delta\log u_\alpha(x(z)^{-2}).                    \tag{10}
$$

因此仅把 $R\omega$ 放进通常的 de Rham 复形，并不能由 (7)
直接得到相应的分部积分。必须另证如何处理这个参考连接。

## 3. 同一个 $U$ 上的 exact form，其自然行却非零

以下给出一个不改变开曲线的具体检查。取固定有理函数

$$
                            H=-yR_*\in K(E_0).               \tag{11}
$$

因为 $R_*$ 在 $O$ 为四阶零点，而 $y$ 在 $O$ 为三阶极点，
$H$ 在 $O$ 正则，首项为 $z$。在 $T$ 和另外两个二挠点也正则；
它仅可能在 $\mathcal D$ 有简单极点。因此 $H\in\mathcal O(U)$，并且

$$
                    (\delta H)\omega=dH
$$

在 $H^1_{\rm dR}(U/K)$ 中为零。$\delta H$ 在同一个 $U$ 上正则，
它在边界 $\mathcal D$ 的极点至多为二阶。

另一方面，$[i]^*H=iH$，所以 $\delta H$ 是 $i$ 不变的，
$\delta H(O)=1$，且 $\delta H-1\in z^4K[[z^4]]$。
所有有关点在 $p=7$ 处可分良好，故它在正式参数中的系数为 $7$ 整。

下面全部系数计算在 $K=\mathbb Q(i)$ 中准确进行。由

$$
 x=z^{-2}+\frac15z^2+\frac1{75}z^6+O(z^{10}),\qquad
 y=-z^{-3}+\frac15z+\frac1{25}z^5+O(z^9),
$$

以及 (1)，得到

$$
 H=z-(12-20i)z^5+
             \left(-\frac{3628}{15}-516i\right)z^9+O(z^{13}).
                                                               \tag{12}
$$

又 $\alpha^4=161-240i$，所以

$$
                 f_0=1+\frac{161-240i}{12}z^4+O(z^8).
$$

于是

$$
 \boxed{\quad
 f_0(\delta H-1)=(-60+100i)z^4
   +\left(-\frac{4909}{5}-\frac{6307}{3}i\right)z^8+O(z^{12}).
 \quad}                                                       \tag{13}
$$

在未分歧二次域 $\mathbb Q_7(i)$ 中，(13) 的 $z^8$ 系数模 $7$ 为 $1$。

为保留完整解析尾，使用前文已证的首层式：若
$F=f_0R$、$R\in t^4\mathcal O[[t^4]]$，则

$$
                  \frac{J_F'(0)}p
                  \equiv\frac{[z^d]F}{Np c}\pmod p.         \tag{14}
$$

其原因是 $e^{-az^d}F$ 的 Gauss 范数至多为 $\rho^4$。
所以对所有 $h\ge2$，下降阶乘系数的赋值至少为

$$
          \left\lceil\frac{h(p-1)+4}{2p}\right\rceil\ge2;
$$

这些界同时趋于无穷，故 (14) 没有丢弃一个未控制的无限尾。

在 $p=7$，sigma 的明确递推给 $c=103/168$，从而
$7c\equiv4\pmod7$、$17\cdot7c\equiv5\pmod7$。
将 (13) 代入 (14)，再用 $\ell_7(1)=0$，得到

$$
 \boxed{\quad
  \frac{\ell_7(\delta H)}7
   =\frac{\ell_7(\delta H-1)}7
                  \equiv3\pmod7.
 \quad}                                                       \tag{15}
$$

因此这个完整自然行对同一开曲线上的恰当微分确实非零。

## 4. 这一检查排除什么、保留什么

式 (15) 排除下列直接比较：存在一个仅依赖通常 de Rham 类的
线性泛函 $L$，使对该自然定义域内的所有 $R\in\mathcal O(U)$ 有

$$
                         \ell_7(R)=L([R\omega]).             \tag{16}
$$

因为 (11) 的 $[\delta H\,\omega]$ 为零，而 (15) 非零。
这是同一个 $U$、同一个实际 $f_0$ 和同一个归一 Mahler 行的检查，
并未用另一个不保留参考的覆盖代替输入。

实际目标 $R_*$ 及十七维表示中的简单极点函数仍具有已经证明的
注入性：若 $R\omega=dG$ 只有简单极点，则 $G$ 不可能有极点，
故 $G$ 为常数、$R=0$。因此本篇不排除该有限子空间上的另一种
周期比较；任何线性泛函在有限子空间上本来都可以抽象延拓。
需要新增的是与真正 Frobenius、端点或参考连接兼容的比较式，
不能仅以有限维性或通常 de Rham 类代替这一步。
