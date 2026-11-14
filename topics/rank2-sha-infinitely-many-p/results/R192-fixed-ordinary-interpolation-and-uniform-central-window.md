# R192. 固定普通位的真实插值与统一两行中央窗口

日期：2026-11-12。**状态：已证明。** 对 R117/R162 的同一原
theta 平面，任意正整数 $r$ 的第 $64,128$ 条中央行始终线性独立。
证明使用固定普通素数 $q=257$、同一参考测度、准确单 Euler 因子
及一个有限整数证书；不以任何未知中央导数为输入。
它还给目标惰性 $p=4r-1$ 的真实 first-pivot 两层行列式的
$O(p)$ 赋值上界。这个上界不是单位结论，也不是已获得的
原消失前缀预算。

## 1. 全部固定对象和结论

采用共同曲线 $E_0:y^2=x^3-x$、$\omega=dx/(2y)$ 及 R57 的
$$
 u'=v,\qquad v'=-2u^3,\qquad L'=u^2,\qquad
 \vartheta'=L\vartheta,\qquad
 (u,v,L,\vartheta)(0)=(0,1,0,1).
 \tag{1}
$$
于是 $\sigma=u\vartheta$，$\vartheta^2=x_E\sigma^2$，
$\vartheta(0)=1$。参考始终是这个 $\vartheta(z)$，
没有改成 $\vartheta(2z)$ 或别的截面。

原两条秩二行是
$$
 A(z)=A_{17,\mathrm{common}}(2z)/16,\qquad
 B(z)=B_{34,\mathrm{common}}(z).
$$
置 $w=z^4$、$s=u^4$。R162 的精确式为
$$
 A=\vartheta^{68}P(s),\qquad B=\vartheta^{68}Q(s),
 \tag{2}
$$
其中
$$
\begin{aligned}
 H_1(s)&=1+4s+70s^2+4s^3+s^4,\\
 H_2(s)&=1+20s-26s^2+20s^3+s^4,\\
 Q_8(s)&=1+364s^2-1088s^3+1190s^4
                     -1088s^5+364s^6+s^8,\\
 P(s)&=\frac{s}{5}(1-s)^2(1+s)(1-2s+5s^2)(5-2s+s^2)H_1H_2,\\
 Q(s)&=\frac{s}{5}(1-s)(1+s)^2(1-2s+5s^2)(5-2s+s^2)Q_8.
\end{aligned}
 \tag{3}
$$
特别，$A(w)=w+\cdots$、$B(w)-A(w)=-22w^2+\cdots$。
对 $F=A,B,\vartheta$ 记原 Hurwitz 系数
$$
 H_F(m)=m![z^m]F(z).
 \tag{4}
$$
(1) 的整数 Hurwitz 递推及 (2) 的齐次写法给
$5H_A(m),5H_B(m)\in\mathbb Z$、$H_\vartheta(m)\in\mathbb Z$。
没有把 $m!$ 吸收到原多项式源格中。

**定理。** 对每个正整数 $r$，
$$
 \boxed{\quad
 \det\begin{pmatrix}
 [w^{64r}]A &[w^{64r}]B\\
 [w^{128r}]A &[w^{128r}]B
 \end{pmatrix}\ne0.
 \quad}
 \tag{5}
$$
更精确地，置
$$
 \mathscr D_r=
 H_A(256r)H_B(512r)-H_B(256r)H_A(512r).
$$
则有固定辅助位的准确赋值
$$
 \boxed{\qquad v_{257}(\mathscr D_r)=3+3v_{257}(r).\qquad}
 \tag{6}
$$
因此 (5) 是同一个有理行列式的非零结论，适用于所有目标 $r$；
没有把辅助位 $257$ 当作目标惰性素数。

## 2. 在 257 处支付相同 Euler、周期与原截面规范

固定 $q=257$。直接有
$$
 q\equiv1\pmod8,\qquad 17^{64}\equiv1\pmod q,\qquad
 34^{128}\equiv1\pmod q.
 \tag{7}
$$
故 $17$ 在 $\mathbb Z_q^\times$ 中有四次根，$34$ 有平方根。
相应的两个曲线缩放把 $E_{17}:y^2=x^3-17x$、
$E_{34}:y^2=x^3-1156x$ 都在 $\mathbb Z_q$ 上 CM 同构到
$E_0$；缩放与 $[i]$ 交换。三条约化曲线的迹都是 $2$。
选择 $i\equiv16\pmod q$，可取
$$
 \pi=1+16i,\qquad \bar\pi=1-16i,\qquad
 v_q(\pi)=1,\quad\bar\pi\equiv2\pmod q.
 \tag{8}
$$
这里 $\pi\bar\pi=q$。同一个 CM 嵌入及上述实际 CM 同构，
使三条曲线的 Frobenius 端都为这一个 $\pi$，
不是仅凭相同迹擅自交换两个根。

在 $\mathcal O=\widehat{\mathbb Z_q^{\mathrm{ur}}}$ 中选择共同
普通周期 $\Omega\in\mathcal O^\times$。R38/R155 给同一个
正式坐标下的有界整 Amice 测度 $\nu_A,\nu_B,\nu_\vartheta$，
满足
$$
 \int_{\mathbb Z_q}x^m\,d\nu_F
       =\Omega^m H_F(m),\qquad F=A,B,\vartheta.
 \tag{9}
$$
这保留了 $A(2z)/16$ 的 $[2]_*/16$ 推前；它是 $q$ 进单位缩放，
并与以下乘法 Euler 分布交换。

令 $J_F(T)$ 为单位部分的 principal Mellin 变换。原两条曲线的
已证中心质量给
$$
 J_A(0)=J_B(0)=0,\qquad
 J_\vartheta(0)\in\mathcal O^\times.
 \tag{10}
$$
参考的后一结论是 R60 §1 的实际秩零参考计算：
$L(E_0,1)/\Omega_{\mathrm{real},0}=1/4$，中央平方的剩余
Euler 因子为 $(1-\bar\pi^{-1})^2$，由 (8) 是单位。

对每个正整数 $m\equiv0\pmod{256}$，三者都有**相同**的准确式
$$
 \boxed{\quad
 J_F((1+q)^m-1)
  =E(m)\Omega^m H_F(m),\qquad
 E(m)=1-\frac{\pi^m}{\bar\pi^{m+1}}.
 \quad}
 \tag{11}
$$
特别 $E(m)\in\mathbb Z_q^\times$。这里没有把仅仅趋零的
Euler 误差当作零。

为说明 $B$ 的单因子符号及有限角色，R118 §4 的全分支平方
公式和同节的正权插值，在 $m\equiv0\pmod{q-1}$ 时同时带有
同一个 $68^m$ 因子；它在比较中消去。所得平方恒等式是
$$
 \left(\int x^m\,d\mu_B\right)^2
 =\left((1-\bar\pi^{-1}(\pi/\bar\pi)^m)
             \int x^m\,d\nu_B^{(0)}\right)^2,
 \tag{12}
$$
其中 $(0)$ 是平凡 tame 平均，$\mu_B$ 是其单位限制。
将 $\delta=\nu_B^{(0)}-\bar\pi^{-1}[\pi/\bar\pi]_*\nu_B^{(0)}$
代入既有 principal annulus 证明：乘法卷积测度去掉原点后
嵌入 $\mathbb C_q[[T]][[X]]$ 整域，核仅为原点原子。
全部正权矩及 (10) 的零质量给 $\mu_B*\mu_B=\delta*\delta$。
在单位环带，$\delta$ 与 $\mu_B$ 本来相等；其非零性也可由
下文 $H_B(256)\ne0$ 及 (12) 直接核定。所以整域中的符号只能
为正，余下原点原子再由总质量为零消去。于是得到
$$
 \nu_B^{(0)}|_{q\mathbb Z_q}
   =\bar\pi^{-1}[\pi/\bar\pi]_*\nu_B^{(0)}.
$$
这正给 $B$ 的 (11)。$A$ 使用已证的同一单 Euler 关系及
$[2]_*/16$；参考 $\vartheta$ 可能保留原点原子，但正权矩
杀掉该原子，所以仍给 (11)。这也说明原有限层相位和
三者不同的 theta 次数没有留下额外的依权标量。

## 3. 同一固定 Tate 变量和全部系数的界

对 $t\in\mathbb Z_q$，定义
$$
 \mathcal M_F(t)
  =J_F((1+q)^{256t}-1)
  =\int_{\mathbb Z_q^\times}\langle x\rangle^{256t}\,d\nu_F(x).
 \tag{13}
$$
写 $\mathcal M_F(t)=\sum_{k\ge0}c_{F,k}t^k$。
由 $v_q(\log\langle x\rangle)\ge1$ 和测度整性，
$$
 v_q(c_{F,k})\ge k-v_q(k!)
 =\frac{255k+s_q(k)}{256}\qquad(k\ge1).
 \tag{14}
$$
这里 $s_q(k)$ 是 $q$ 进数字和。故这些是实际 Tate 函数，
不是仅在整数点给出的插值符号。

置 $\kappa=255/256$。由整赋值和 (14)，每个正次数系数的
赋值至少为 $\lceil\kappa k\rceil$。这里不宣称这些级数在
边界半径 $q^\kappa$ 的闭盘上收敛：例如 $k=q^n$ 时，
(14) 中的数字和只有一，所给加权项界不趋零。

由 (10)，可以形式地写
$\mathcal M_\vartheta=c_0(1+h)$，其中
$c_0\in\mathcal O^\times$、$h\in t\mathcal O[[t]]$，
且 $v_q([t^k]h)\ge\lceil\kappa k\rceil$。形式逆
$(1+h)^{-1}=\sum_{n\ge0}(-h)^n$ 的每个 $t^k$ 系数只涉及
$n\le k$ 的有限求和；其中每个乘积满足
$\sum_i\lceil\kappa k_i\rceil\ge\lceil\kappa k\rceil$。
因此逆级数也满足同一正次数系数界。与分子的级数相乘，得到
$$
 R_A(t)=\frac{\mathcal M_A(t)}{\mathcal M_\vartheta(t)},\qquad
 R_B(t)=\frac{\mathcal M_B(t)}{\mathcal M_\vartheta(t)}
 \tag{15}
$$
都满足 $R_F(0)=0$，且
$$
 v_q([t^k]R_F)\ge\lceil\kappa k\rceil.
 \tag{16}
$$
普通参考的单位性还给，对所有正整数 $t$，
$H_\vartheta(256t)\in\mathbb Z_q^\times$。由 (11)，准确有
$$
 \boxed{\quad R_F(t)=\frac{H_F(256t)}{H_\vartheta(256t)}
                \quad(t=1,2,\ldots).\quad}
 \tag{17}
$$
周期、Euler、阶乘规范在同一个 $m=256t$ 上同时消去。

这些比值在正整数处属于 $\mathbb Q$，所以 (15) 的所有系数
实际上属于 $\mathbb Q_q$：先令 $t=q^n\to0$ 得常数项属于
$\mathbb Q_q$，再依次减去已知低项、除以 $q^{nk}$ 后取极限，
得到每个第 $k$ 项。$\mathbb Q_q$ 在 $\mathbb C_q$ 中完备且闭。
结合 (16)，这给 $R_A,R_B\in\mathbb Z_q\langle t\rangle$。

进一步定义整 Tate 函数
$$
 F_A(t)=\frac{R_A(t)}{qt},\qquad F_B(t)=\frac{R_B(t)}{qt}.
 \tag{18}
$$
在 $t=0$ 使用其可去值，不需要假设任何未知导数是单位。
(16) 给
$$
 v_q([t^k]F_F)\ge\lceil\kappa(k+1)\rceil-1.
$$
特别，可以准确写成
$$
 F_A=a_0+q a_1t+q^2U(t),\qquad
 F_B=b_0+q b_1t+q^2V(t),
 \tag{19}
$$
其中 $a_0,a_1,b_0,b_1\in\mathbb Z_q$，
$U,V\in t^2\mathbb Z_q\langle t\rangle$。
对所有 $k\ge2$ 的整性成本已经由 (14)–(16) 支付，
不只检查了有限 Taylor 截断。

## 4. 一个固定的精确有理证书

随附脚本从 (1) 的整数 Hurwitz ODE 算到 $z^{512}$，
并独立用 (2) 的有理 $s$ 级数、椭圆对数反演核对所有系数。
第二种输入是
$$
 \begin{aligned}
 w&=s\left(\sum_{n\ge0}
       \frac{\binom{2n}{n}}{4^n(4n+1)}s^n\right)^4,\\
 68\log\vartheta
   &=\sum_{n\ge1}\frac{17}{n}
       \prod_{j=0}^{n-1}\frac{4j+1}{4j+3}s^n.
 \end{aligned}
 \tag{20}
$$
两种算法逐项相同；不输入 $p$ 进 $L$ 值或中央零性。
得到以下完整有限证书。表中单位是除去所列赋值后模 $257$ 的值。

| $m$ | $v_qH_A(m)$；单位 | $v_qH_B(m)$；单位 | $v_qH_\vartheta(m)$；单位 |
|---|---:|---:|---:|
| $256$ | $1;\ 179$ | $1;\ 188$ | $0;\ 1$ |
| $512$ | $1;\ 202$ | $1;\ 238$ | $0;\ 2$ |

在这两行的原 Hurwitz minor 上，准确有
$$
 v_q\mathscr D_1=3,\qquad
 \mathscr D_1/q^3\equiv224\pmod q.
 \tag{21}
$$
脚本还核对
$\mathscr D_1/q^3\equiv13356000\pmod{q^3}$。
用 (17)–(18) 而不是未知导数，(21) 给
$$
 \frac1q\det\begin{pmatrix}F_A(1)&F_B(1)\\F_A(2)&F_B(2)\end{pmatrix}
 \equiv\frac{224}{2\cdot1\cdot2}=56\pmod q.
 \tag{22}
$$
故 (19) 中的实际系数满足
$$
                    a_0b_1-b_0a_1\equiv56\pmod q.
 \tag{23}
$$
这不是由数值精度猜测非零：全部输入是有限的整数／有理数
递推，赋值及余数为精确计算。

## 5. 整个单位盘上的差商，而不只两个校准点

若 $U(t)\in\mathbb Z_q\langle t\rangle$，其差商
$(U(t_2)-U(t_1))/(t_2-t_1)$ 属于
$\mathbb Z_q\langle t_1,t_2\rangle$。这是逐项展开
$(t_2^n-t_1^n)/(t_2-t_1)$ 的整数多项式，并利用原 Tate
系数趋零得到；没有 $1/n$ 或阶乘分母。

对 (19) 使用此事实，(23) 给
$$
 \boxed{\quad
 \frac{
 F_A(t_1)F_B(t_2)-F_B(t_1)F_A(t_2)}
 {q(t_2-t_1)}
 \in56+q\mathbb Z_q
 \quad(t_1,t_2\in\mathbb Z_q,\ t_1\ne t_2).
 \quad}
 \tag{24}
$$
等价地，该除式是一个两变量整 Tate 函数，其模 $q$ 恒为
$56$。所以所有两个不同的参数值都给独立行，而不是仅在
$t=1,2$ 给独立行。

现在取任意正整数 $r$、$t_1=r,t_2=2r$。由 (17)–(18)，
$$
 \mathscr D_r
 =2q^2r^2H_\vartheta(256r)H_\vartheta(512r)
       \{F_A(r)F_B(2r)-F_B(r)F_A(2r)\}.
$$
两个参考 Hurwitz 系数都是单位，(24) 于是准确给 (6)。
再除以 $(256r)!(512r)!$ 得 (5)。证明没有排除 $q\mid r$；
此时 (24) 正确支付额外的 $v_q(r)$。

## 6. 对目标惰性位的有限层数和统一算术上界

令目标 $p=4r-1\ge7$、$p\ne11$，仍使用 R185/R189 的原整轴及实际
$\omega_s$。由 (5)，原中央前缀的第一、第二次秩跳 $a<b$
满足
$$
                       a\le64,\qquad b\le128.
 \tag{25}
$$
R190 §5.1 的 first-pivot 论证准确给
$$
 \det(q_a,q_b)
 =\omega_a\omega_b
 \det\begin{pmatrix}
 [w^{ra}]A &[w^{ra}]B\\
 [w^{rb}]A &[w^{rb}]B
 \end{pmatrix}\ne0.
 \tag{26}
$$
没有为任意非 first-pivot 两行免费删掉换元系数。

还可保留一个统一的整数高度账本。R190 §2 的同一正 theta
增长界给固定常数 $C,c>0$，使
$|A(z)|,|B(z)|\le Ce^{c|z|^2}$。Cauchy 估计及 Stirling 界
遂给
$$
 \log\max(1,|5H_F(m)|)
       \le\frac m2\log m+O(m),\qquad F=A,B,
 \tag{27}
$$
其中常数与 $m,p$ 无关。对 (26) 的非零原 minor，
乘 $(m_a)!(m_b)!$、$25$ 后是非零整数，
$m_a=(p+1)a$、$m_b=(p+1)b$。非零整数的 $p$ 赋值
不超过其绝对值对数除以 $\log p$，故
$$
 v_p\det(R_a,R_b)
 \le (96+o(1))p\qquad(p\to\infty).
 \tag{28}
$$
这里 $a+b\le192$；被除去的两个阶乘只会降低赋值，
不能增加右侧。即使 $a,b$ 随 $p$ 变化，有限的行号范围
也使 (27) 的常数保持一致。

当 $p>128$ 时，$v_p(\omega_a)=a-1$、
$v_p(\omega_b)=b-1$；有限个较小 $p$ 另外吸收进常数。
所以
$$
 \boxed{\quad
  \exists\,a\le64,\ b\le128:\quad
  0\ne\det(q_a,q_b),\qquad
  v_p\det(q_a,q_b)\le(96+o(1))p.
 \quad}
 \tag{29}
$$
特别存在一个固定常数 $C_*$ 使该赋值对所有这些目标素数
至多 $C_*p$。这给 R189 两层 Smith 的真实有限输入与
多项式成本，完全避免把定性 Weyl 均值当成统一收敛速度。

## 7. 边界、证书和依赖

(5)、(6)、(25)、(29) 都是原两条函数的结论，不是假设
$J_A'(0)=J_B'(0)=0$ 后另选两条函数。它们也不证明目标
$p$ 处的原两导数之一非零；在双零假设下，
R190 的必要条件 $v_p\det(R_a,R_b)\ge2+v_p(ab)$
仍可能成立。R189 中把这些行送入全部原前缀的 Schur 补、
读取精度和其他源格成本仍须保留。

可复跑证书：
[check-fixed-257-central-window.py](../scripts/check-fixed-257-central-window.py)。
它同时核曲线的三份 Frobenius 迹、两种原有理级数构造、
全部 $z^{512}$ 以下系数、(21) 和 (22)。

本篇使用的规范来源均为本课题已经证明的实际等式：

- [R117 的实际两行与卷积证明](../notes/2026-11-12-two-rank-two-theta-linear-convolution.md)，给共同 $E_0$ 尺度及 $[2]_*/16$。
- [R162](R162-actual-theta-plane-nonlinear-flow-and-lagrange-jets.md)，给 (2)–(3)、(20)。
- [R57 的整数 Hurwitz 递推](../scripts/check-theta-hurwitz-integers.py)，给 (1) 的无分母算法。
- [准确 principal 单 Euler 分布证明](../notes/2026-11-12-theta-principal-tame-euler-distribution.md) §2–4，给平方到单因子的符号和原点原子处理。
- [R118 的实际 E34 插值](../notes/2026-11-12-e34-rank-two-and-central-slope-criterion.md) §4，给 $B$ 的原有限角色及平方公式。
- [R60 参考比较](../notes/2026-11-12-ordinary-reference-normalized-rational-newton.md) §1–2，给同一个 $\vartheta$ 的中心单位和正权矩。
- [R155](R155-two-theta-rows-common-amice-lattice.md)，给共同有界整 Amice 格。
- [R190](R190-central-projection-of-square-theta-sections.md) §2、§5.1，给固定增长界与 first-pivot 精确等式。

本篇的有限校准不使用未知 $J_A'(0)$ 或 $J_B'(0)$；
全部统一层数由同一个固定 $257$ 进解析差商推出。
