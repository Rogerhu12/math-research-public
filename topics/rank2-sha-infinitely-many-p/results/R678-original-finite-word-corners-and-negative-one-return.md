# R678 — 两参数原词的八个环带角域、零质量差商与负一返回

日期：2026-11-15。**状态：已证明。**

本篇把 R665/R674 的已知负一首项放回**有限层的原坐标**。
使用同一个固定 N 的测试 $q_N^\dagger$，取八个互不相交的
原 $A,Q,L$ 环带角域。它们同时属于原第一 Y 环带和对顶 Y 的更深环带。
在这些真实角域上，一个整的三阶差商严格杀掉完整质量，
其 S/T 相对中央行在所有充分深的有限层准确非零。

没有先令 A/Q 词趋向极限，再把冻结门认成有限域。
全原 S/T 总行与全部角域外部在同一个等式中保留。
对顶算术测试的不同多项式、不同观察和 $x^2/y$ 项也明确列出；
本文不把它们免费认成当前测试。

## 1. 同一原测试、坐标和完整核心

保持 R674 的相对密度一普通子族、原全部 ray 及固定坏集。
固定 $N\in4\mathbf Z_{\ge1}$，全文只使用其同一个
$q_N^\dagger$，不使它依下面的 r、m、n 变化。
记其整六次多项式为 $\widehat P^\dagger=\widehat P^\dagger_{N,p}$。

沿用
$$
Q=c+2d,\qquad L=2c-d,\qquad
Y_0=A+Q,\quad Y_1=A+L,\quad Y_2=A-Q,\quad Y_3=A-L,
$$
$$
W_0=A+b_QQ+b_LL,\qquad
W_1=A-b_LQ+b_QL,
$$
$$
b_Q=\frac{11+6\omega}{5},\quad
b_L=\frac{2+12\omega}{5},\quad
b_Y=\frac{20+3\omega}{17},\quad h=\frac{b_L}{b_Y},
$$
$$
a=-\frac{5+6\omega}{29},\qquad
b_F=\frac{5+6\omega}{5},\qquad
\ell_0=-\frac{3\omega}{5},\qquad g=3-2\omega .
\tag{1}
$$
这些显示分母和 $h$ 在原子族均为单位。
$\delta=1+2\omega$，$\beta=-\lambda$；
后一个绝对符号由 R655 支付。

保持全部原四个第一输入及 Q/L pair：
$$
\mu_0=\nu_4\otimes\nu_{\rm pair},\qquad
\mathcal A_{\nu_{\rm pair}}(q,l)
=\sigma(q+2l)\sigma(2q-l).
$$
原 A 两层核心、Q/L whole odd5 核严格给
$$
\boxed{
\mu_0|_{\{A\in p^{2r},\,Q\in p^k,\,L\in p^n\}}
=\lambda^{2r}\beta^{k+n}
(P_{A,\kappa^{2r}}P_{Q,\kappa^k}P_{L,\kappa^n})_*\mu_0 .
}
\tag{2}
$$
这是 R662/R665 的完整来源身份，所有伙伴均保留。
不是把 A 深域认成四个 sigma 输入各自深。

原 carry 的完整实际门和权为
$$
q_N^\dagger=
\frac{1_{\{C\ {\rm unit},\,F-C\in p^N\}}}{b\Omega^6}
 \widehat P^\dagger((F-C)/\kappa^N,F+13C,G),
$$
$$
F=C+D_*+aA+b_FQ+\ell_0L,\qquad
G=13H_1+gF .
\tag{3}
$$
$C,D_*,H_1$ 均与 A、Q、L 正交。
R674 的整个 $\pi_4$ 中性以及原九条约束保持；
特别没有只使用它的模 p 多项式。

## 2. 八个实际原角域与精确 pullback

固定整数 $M\ge2$，取 r 为偶整数，满足
$$
r>\max(N,M+3).
$$
对 $m=0,1$、$j=0,1,2,3$ 置
$$
k_m=r+m,\qquad n_j=r+M+j,\qquad
x=\kappa^r,\quad z_m=\kappa^m,\quad y_j=\kappa^{n_j}.
$$
定义原物理角域
$$
\boxed{
\mathcal D_{r,m,j}
=\{A\in p^{2r},\
Q\in p^{k_m}\mathbf Z_p^\times,\
L\in p^{n_j}\mathbf Z_p^\times\}.
}
\tag{4}
$$
八个域互不相交。由于
$$
k_m<n_j<2r,
$$
逐点准确有
$$
\boxed{
v_p(Y_0)=v_p(Y_2)=v_p(c)=v_p(d)=k_m,\qquad
v_p(Y_1)=v_p(Y_3)=n_j .
}
\tag{5}
$$
原 R664 的共同伴随
$\mathcal E=5A-29(Q+L)$ 也恰在第 $k_m$ 环带。

所以 (4) 是原 $Y_1$ 深、$Y_0$ 浅的真实外部角域，
并在原 $CD_{k_m}$ 中。这里 $k_m$ 随 r 变；
不能据此直接调用 R671 对固定 CD 层的递推。

对 (2) 的真实返回，原输入变为
$$
A_{\rm phys}=x^2A,\qquad Q_{\rm phys}=xz_mQ,\qquad
L_{\rm phys}=y_jL,
\tag{6}
$$
而返回后 Q、L 均取单位。其余伙伴原样保留。
令
$$
\mathcal G_*=\{C\ {\rm unit},D_*\in p^N\},
\quad
X_*=(D_*/\kappa^N,D_*+14C,13H_1+g(D_*+C)),
$$
$$
v_N=(\kappa^{-N},1,g).
$$
因 $k_m,n_j,2r\ge N$，原门的准确返回为 $\mathcal G_*$，且
$$
\boxed{
q_N^\dagger\circ B_{r,m,j}
=1_{\mathcal G_*}\,
 \frac{\widehat P^\dagger(X_*+s_m(x,y_j)v_N)}{b\Omega^6},
\quad
s_m(x,y)=a x^2A+b_Fxz_mQ+\ell_0yL .
}
\tag{7}
$$
这里
$B_{r,m,j}=P_{A,\kappa^{2r}}P_{Q,\kappa^{k_m}}P_{L,\kappa^{n_j}}$。
(7) 是有限层完整等式，未冻结多项式中的任何一项。

## 3. 同域的原 S/T 观察与对顶观察

原第一轴完整核心使用物理缩放 $(-\kappa)^{k_m}$。
记 $\epsilon_m=(-1)^m$。返回后原 S 观察准确为
$$
\boxed{
S_m(x)=\frac{Y_0}{(-\kappa)^{k_m}}\circ B_{r,m,j}
=\epsilon_m(Q+xz_m^{-1}A).
}
\tag{8}
$$
它不是 $A/\kappa^{2r}+Q/\kappa^{k_m}$。

原 T 观察是 $W_0P_{Y_0,(-\kappa)^{k_m}}^{-1}$，
其完整返回为
$$
\boxed{
T_m(x,y)=
b_YS_m(x)+(b_Q-b_Y)xz_mQ
 +(1-b_Y)x^2A+b_LyL .
}
\tag{9}
$$
因 $r>m$，在 (4) 上两个原单位 cut 准确成立：
返回后它们都等价于 Q 单位。
因此同一角域上的实际相对 log 是
$$
\boxed{
\log\left\langle\frac{T_m(x,y)}{b_YS_m(x)}\right\rangle
=
\log\left(
1+\epsilon_m
 \frac{(b_Q-b_Y)xz_mQ+(1-b_Y)x^2A+b_LyL}
      {b_Y(Q+xz_m^{-1}A)}
\right).
}
\tag{10}
$$
整个分母保留；右端是 p 进收敛的真实 log。

同一物理角域也属于原对顶 $Y_1$ 环带。
令 $q_{1,N}^\dagger=q_N^\dagger\circ J^{-1}$，
其中 $J(c,d)=(d,-c)$，保持前四输入。
它的准确返回仍有同一门，但多项式移位不同：
$$
\boxed{
s_{1,m}(x,y)=a x^2A-\ell_0xz_mQ+b_FyL .
}
\tag{11}
$$
令 $\epsilon_{n}=(-1)^n$。原对顶 S/T 观察准确为
$$
\boxed{
S_{1}(x,y)=\epsilon_n(L+x^2y^{-1}A),
}
$$
$$
\boxed{
T_{1}(x,y)=b_YS_1(x,y)-b_Lxz_mQ
 +(1-b_Y)x^2A+(b_Q-b_Y)yL .
}
\tag{12}
$$
在 (4) 上它们的单位 cut 都准确为 L 单位，
因为 $2r>n_j$。

所以两个原算术框架确实共享 (4) 的物理域。
但 (7)、(11) 是不同权，(8)–(9)、(12) 是不同观察。
特别 $x^2/y_j=\kappa^{r-M-j}$ 必须保留；
不能把有限层 (12) 换成它的极限。
在共同门上的完整权差就是
$$
\frac1{b\Omega^6}\sum_{a'=1}^{6}
 \frac{(\partial_{v_N}^{a'}\widehat P^\dagger)(X_*)}{a'!}
 \{s_{1,m}(x,y)^{a'}-s_m(x,y)^{a'}\}.
\tag{13}
$$
它仍依同一原四输入，没有引入自由辅助来源。

## 4. 四个整权与完整质量的准确消去

置
$$
D_\kappa=(1-\kappa)(1-\kappa^2)(1-\kappa^3),
$$
$$
\boxed{
(\alpha_0,\alpha_1,\alpha_2,\alpha_3)
=\frac{(\kappa^3,-\kappa-\kappa^2-\kappa^3,
                  1+\kappa+\kappa^2,-1)}{D_\kappa}.
}
\tag{14}
$$
它们都整，赋值分别为 $(3,1,0,0)$。
完整恒等式为
$$
\sum_{j=0}^3\alpha_j\kappa^{aj}=0\quad(a=0,1,2),
\qquad
\sum_{j=0}^3\alpha_j\kappa^{3j}=\kappa^3 .
\tag{15}
$$
对任意解析函数 f，
$$
\sum_{j=0}^3\alpha_j f(y_0\kappa^j)
=\kappa^3y_0^3
 [y_0,y_0\kappa,y_0\kappa^2,y_0\kappa^3]f,
\tag{16}
$$
右边是通常三阶差商，读的是三次系数而非未除阶乘的导数。

现在在返回域 $\mathcal G_*\times Q^\times\times L^\times$，
对每个固定 m 考虑 (7) 的完整质量。
pair 同时 $\mu_6$ 旋转的角型为二，两个单位限制均保持该旋转。
六次原权中的 $Q^aL^b$ 因而只可能在
$$
a+b\equiv2\pmod6,\qquad a+b\le6
$$
时有非零积分，故只有 $a+b=2$。
于是这个完整质量作为 y 的多项式次数至多二，
包括所有 $a x^2A$ 和 $b_Fxz_mQ$ 项。
由 (15)，
$$
\boxed{\text{每个 m 的四角域归一质量和严格为零。}}
\tag{17}
$$
这不只消首阶质量，也不以原 S/T 的总质量零代替局部计算。

## 5. 同一个有界八角域 Mellin 行

令 $d_p=p-1$，对 Z=S,T 定义真实角域 Mellin 行
$$
\mathcal K^S_{r,m,j}(w)=
\int_{\mathcal D_{r,m,j}}q_N^\dagger
 \left\langle Y_0/(-\kappa)^{k_m}\right\rangle^{d_pw}\,d\mu_0,
$$
$$
\mathcal K^T_{r,m,j}(w)=
\int_{\mathcal D_{r,m,j}}q_N^\dagger
 \left\langle W_0P_{Y_0,(-\kappa)^{k_m}}^{-1}\right\rangle^{d_pw}
 \,d\mu_0 .
\tag{18}
$$
两个观察在 (4) 上确已为单位。
按 (2)，每行返回的完整标量为
$\lambda^{2r}\beta^{k_m+n_j}$。

定义
$$
\boxed{
\mathcal B^Z_{r,M}(w)=
\sum_{j=0}^3\alpha_j\lambda^{-2r}
 \left\{\beta^{-r-n_j}\mathcal K^Z_{r,0,j}(w)
       -\beta^{-r-1-n_j}\mathcal K^Z_{r,1,j}(w)\right\}.
}
\tag{19}
$$
所有显示系数整且有界；这就是八个互不相交原角域上的实际测试。
(17) 给
$$
\boxed{\mathcal B^S_{r,M}(0)=\mathcal B^T_{r,M}(0)=0.}
\tag{20}
$$
特别常数 $\log\langle b_Y\rangle$ 的贡献在这一完整行中严格为零。

令
$$
\mathfrak B_{r,M}=
\frac1{d_p}\left.
 \frac{d}{dw}\{\mathcal B^T_{r,M}(w)
       -\langle b_Y\rangle^{d_pw}\mathcal B^S_{r,M}(w)\}
 \right|_{w=0}.
\tag{21}
$$
它准确就是 (10) 的同一个有界八角域相对 log 行；
没有另改观察或删除某个尺度质量。

## 6. 有限层的负一系数与统一误差

令 $F_m(x,y)$ 表示在
$\mathcal G_*\times Q^\times\times L^\times$ 上，
(7) 的完整权乘 (10) 的积分。
只在这里把 x、y 当作解析变元，以读取 (21) 的有限层值。
它们最后始终代回 $x=\kappa^r,y=y_j$。

在 x=0，两个 m 的权相同，观察差准确为
$$
2\sum_{\substack{k\ge1\\k\ {\rm odd}}}
 \frac{h^k y^kL^kQ^{-k}}{k}.
$$
R665 的完整角型消去仍适用于 L 单位：
六次原权只留下其 L 二阶项。
因此
$$
[y^3](F_0(0,y)-F_1(0,y))
=72b\Omega^3h\,J_N^\dagger
          (1-\beta\kappa^3)I_{\Sigma_5,-1}.
\tag{22}
$$
这里
$$
I_{\Sigma_5,-1}=\int_{Q\ {\rm unit}}Q^{-1}\,d\nu_{\Sigma_5}\ne0
$$
正是 R655 的原负一矩。
新增因子只来自真实 L 单位正三矩
$$
\int_{L\ {\rm unit}}L^3\,d\nu_{X_5}
=6\Omega^3(1-\beta\kappa^3).
$$
没有给已是单位积分的负一矩再添 Euler 因子。

R674 准确付过
$$
\boxed{
J_N^\dagger=\frac{\ell_0^2}{2b\Omega^2}
                    \lambda^N\kappa^{-2N}.
}
\tag{23}
$$
所以 (22) 的赋值为 $-2N+v_p(I_{\Sigma_5,-1})$。

下面给有限 r 的误差，不交换两个深度极限。
对 m=0,1，原完整整右逆及 (7)、(10) 严格给
$$
F_m(\kappa^N X,\kappa^N Y)\in\mathcal O[[X,Y]] .
\tag{24}
$$
证明是：权的第一坐标移位变成
$a\kappa^N X^2A+b_F\kappa^mXQ+\ell_0YL$，其余坐标也整。
log 中含逆 Q 的分母可按
$Q+\kappa^{N-m}XA$ 展开；$N\ge4$，
所有 log 幂分母 k 均由其至少 $p^{(N-m)k}$ 的分子支付。
两个单位输入上的有界测度积分逐系数保持整性。

对整二元级数应用 (16)：
三阶差商的常数是 y 三次系数，
其余项由 X 或四个 Y 节点之一整除。
这里 $v_p(X)=r-N$，四个 Y 的赋值至少 $r+M-N$。
再付回 $\kappa^{-3N}$，得到
$$
\boxed{
\begin{aligned}
&[y_0,y_0\kappa,y_0\kappa^2,y_0\kappa^3]
 (F_0(\kappa^r,\cdot)-F_1(\kappa^r,\cdot))\\
&\quad=
72b\Omega^3hJ_N^\dagger(1-\beta\kappa^3)I_{\Sigma_5,-1}
+p^{r-4N}\mathcal O,
\qquad y_0=\kappa^{r+M}.
\end{aligned}}
\tag{25}
$$
这使用三阶差商的完整齐次多项式表达，
没有按节点分母分别作会丢失消去的估计。

结合 (16)、(21)，得到真正有限层的主式
$$
\boxed{
\mathfrak B_{r,M}
=\kappa^{3(r+M)+3}
 \left\{
36\ell_0^2\Omega h\lambda^N\kappa^{-2N}
 (1-\beta\kappa^3)I_{\Sigma_5,-1}
+p^{r-4N}\mathcal O
 \right\}.
}
\tag{26}
$$
故只要再取
$$
r>2N+v_p(I_{\Sigma_5,-1}),
$$
便有
$$
\boxed{
v_p(\mathfrak B_{r,M})
=3(r+M)+3-2N+v_p(I_{\Sigma_5,-1}).
}
\tag{27}
$$
这是八个有限原角域的准确非零行。
r 可依 p 选取；没有把 p 依赖的负矩套入固定多项式密度引理，
也不增加 ray 条件。

## 7. 原 S/T 全总行和全部外部的同一个等式

对每个 m，保持原算术全行
$$
\mathcal F^S_{r,m}(w)=
\int_{Y_0\in p^{k_m}\mathbf Z_p^\times}q_N^\dagger
 \langle Y_0/(-\kappa)^{k_m}\rangle^{d_pw}\,d\mu_0,
$$
$$
\mathcal F^T_{r,m}(w)=
\int_{Y_0\in p^{k_m}}q_N^\dagger
 1_{\{W_0P_{Y_0,(-\kappa)^{k_m}}^{-1}\ {\rm unit}\}}
 \langle W_0P_{Y_0,(-\kappa)^{k_m}}^{-1}\rangle^{d_pw}\,d\mu_0 .
$$
原 whole Y 核和同一 $\pi_4$ 中性给
$$
\boxed{(\mathcal F^S_{r,m},\mathcal F^T_{r,m})
=\lambda^{k_m}\beta^N(J_S,6\delta J_T).}
\tag{28}
$$
本篇明确用 $(-\kappa)^{k_m}$ 归一。
与 R662 的 $\kappa^r p^m$ 归一比较，须对全行及其全部外部
同时乘 $\langle\lambda^2\rangle^{-m d_pw}$；
没有只在某个局部项去掉这一尺度。

对 Z=S,T，在 (19) 中以
$\mathcal F^Z_{r,m}-\mathcal K^Z_{r,m,j}$
替换每个角域行，定义完整加权外部 $\mathcal E^Z_{r,M}$。
每个补项保原自己的单位 cut、同一个 q 和观察。
它准确分成 A 不深 $2r$ 的部分与 A 深而 L 不在所指定环带的部分。
后者包括全部更浅、更深 L 输入；
T 的 Q 非单位可能部分和 S/T 不同的 W 失败支均未删去。

置
$$
A_\kappa(z)=\sum_{j=0}^3\alpha_jz^j
=-\frac{(z-1)(z-\kappa)(z-\kappa^2)}{D_\kappa},
$$
$$
\boxed{
c_{r,M}=2\lambda^{-2r}\beta^{N-r-M}A_\kappa(\beta^{-1}).
}
\tag{29}
$$
因为 $1+\lambda$ 已由 R410 付成单位，
$A_\kappa(\beta^{-1})$ 和 $c_{r,M}$ 都是单位。
注意 m=1 的外部核心是 $\beta^{r+1}$；
其负号正是使两原总行相加为 (29) 的原因。

逐项使用 (28)，得到完整 Mellin 身份
$$
\boxed{
\mathcal B^S_{r,M}+\mathcal E^S_{r,M}=c_{r,M}J_S,\qquad
\mathcal B^T_{r,M}+\mathcal E^T_{r,M}=6\delta c_{r,M}J_T .
}
\tag{30}
$$
这两个行使用同一组角域和同一个固定 q，
各自完整外部仍按其原 cut 定义。

原 $J_S(0)=J_T(0)=0$ 与 (20) 还给
$\mathcal E^S_{r,M}(0)=\mathcal E^T_{r,M}(0)=0$。
这里只是两个**完整加权和**的质量为零，
不把单个原外部质量赋零。

若原两个中央导数同时为零，(30) 准确给
$$
\boxed{
\frac1{d_p}\left.
 \frac{d}{dw}\{\mathcal E^T_{r,M}(w)
 -\langle b_Y\rangle^{d_pw}\mathcal E^S_{r,M}(w)\}
 \right|_{w=0}
=-\mathfrak B_{r,M}\ne0 .
}
\tag{31}
$$
其准确赋值就是 (27)。
这是一条原 S/T **同角域、零质量**的强制外部差，
没有把局部非零当作整个中央非零。

## 8. 与原对顶外部的准确接点及剩余条件

由 (5)，八个角域已真实落在
$Y_1$ 环带 $n_j$、$Y_0$ 浅及 $CD_{k_m}$ 的交域。
因此它们与 R668/R671 的原对顶外部有真实物理交集。

但把 (31) 进一步接回该外部的原算术行，还必须同时处理：

- 同一门中的完整六次权差 (13)；
- 原观察 (8)–(9) 与 (12) 的差，尤其 $x^2/y_j$ 项；
- (30) 中角域外的全部 A、L 和单位失败部分；
- $k_m=r+m$ 随 r 变化，不能套固定 CD 层的递推。

这些是同一有限原来源上的明确转置，未产生新的未知算术来源。
已知的负一非零现在位于真正原对顶交域中的有限有界测试，
而非只位于 r 趋向无穷后的冻结门。
本篇未证明 (31) 的完整外部差为零，主目标仍未完成。

## 精确文件

- [check-r678-finite-word-corners-and-third-difference.js](../scripts/check-r678-finite-word-corners-and-third-difference.js)
- [check-r678-finite-word-corners-and-third-difference.json](../scripts/check-r678-finite-word-corners-and-third-difference.json)

脚本以 $\mathbf Q(\omega)$ 精确核两套全部六坐标观察、原 F/G 门、
两套移位、四个整插值权和完整总行系数，共 61 条身份。
同时保原质量角型的全部可能 $(Q,L)$ 次数，
没有用有限点采样代解析误差或原算术证明。

主要依赖：
[R655](R655-original-sigma-five-schwartz-and-rank-one-negative-moment.md)；
[R662](R662-original-annulus-exterior-and-exact-w-compensation.md)；
[R665](R665-original-mixed-unit-deep-branch-and-negative-one-return.md)；
[R674](R674-original-double-s-arithmetic-adaptation-and-negative-one.md)。
