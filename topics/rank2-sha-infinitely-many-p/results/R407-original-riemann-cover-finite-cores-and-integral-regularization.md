# R407 — 原 Riemann 二覆盖的有限阶整 core、十六列正则化与真实消极点

日期：2026-11-14。**状态：以下固定无穷普通素数类、两条完整二覆盖 theta 算子的二阶/八阶身份、principal 分支的单位分母，以及每个原 mixed 来源的整双轴正则化和原全深输入因子整除均已证明。这里不把 mixed 单项降到未支付的 degree34/72 空间，也不由整正则化直接推出原中央非零。**

## 1. 同一原来源及一个明确的固定无穷类

沿用 R404 的 $E_{17}$、同一普通周期、两条原 rank-two 来源 $S,T$，
以及两个实际 mixed 十二 sigma 来源 $B_2,B_3$：
$$
S(z)T(w)=B_2(z,w)+B_3(z,w).
\tag{1}
$$
R404 已完整支付双 $[2]$ 的半特征。故
$$
F_j(z,w):=B_j(2z,2w)\in
 \mathcal S_{136}\otimes\mathcal S_{288},\qquad
\mathcal S_N=\sigma^N L(NO).
\tag{2}
$$
本篇保留这个真实二覆盖；不假设单个 $B_j$ 已经下降到
$\mathcal S_{34}\otimes\mathcal S_{72}$。

设 $\pi_0=\psi_0(\mathfrak p)$ 是 $E_1:y^2=x^3+1$ 的
$2\delta$-primary 生成元。把 R399 的模数只加倍，取
$$
\boxed{
\pi_0\equiv a_*:=261631+198018\omega
 \pmod{558144\mathcal O_K},\qquad
558144=64\cdot27\cdot17\cdot19.
}
\tag{3}
$$
它准确给
$$
\pi_0\equiv-1+2\omega\ (64),\quad
\pi_0\equiv1\ (27),\quad
\pi_0\equiv\delta\ (17),\quad
\pi_0\equiv1\ (19).
\tag{4}
$$
$Na_*=55854261127$ 与模数互素，且原 primary 条件已经相容。
固定 ray class 的 degree-one 素理想定理因此给正密度的普通有理
素数；以下只删去 $p\le19$。这是一套固定同余条件，不随 $p$ 新选角色。

R389/R399 的实际局部角色给
$$
\boxed{\pi:=\psi_{17}(\mathfrak p)=\psi_{24}(\mathfrak p)=-\pi_0.}
\tag{5}
$$
令
$$
\lambda=\bar\pi^{-1},\qquad
\kappa=p/\bar\pi^2,\qquad
\beta=\bar\pi^{-2}=\lambda^2,\qquad d=p-1 .
\tag{6}
$$
两条真正的原目标都有完整 core
$\nu_G|_p=\lambda[\kappa]_*\nu_G$，$G=S,T$。
此处 $\lambda$ 是 R399 的 $-\lambda_0$，不是改掉该篇的负号。

## 2. 原整 theta 格上的算子与全部中心

以下复述 R300 的逐支计算在任意偶 $N$ 的部分，明确它适用于
$136,288$。对原奇范数 CM 整数 $a$，置
$$
r_a(z)=\frac{\sigma(az)}{\sigma(z)^{Na}},\qquad
\mathscr M_a(\sigma^Nf)=
\sigma^N\operatorname{Tr}_{[a]}
 \left[\left(\frac{r_{\bar a}}{r_a}\right)^N f\circ[\bar a]\right].
\tag{7}
$$
原 division 函数的首项常数仍为 $a$。完整极点计算给
$\mathscr M_a\mathcal S_N\subset\mathcal S_N$。
实际普通算子是
$$
\boxed{K_N=T_{p,N}=\frac{\bar\pi}{p}\mathscr M_\pi,}
\tag{8}
$$
其原 Amice 表达为完整根单位平均；等价的测度定义是
$$
\nu_F|_{p\mathbf Z_p}=\lambda[\kappa]_*\nu_{K_NF}.
\tag{9}
$$
(8) 中的 $1/p$ 不能在单支上删除；(9) 已支付整个平均。

写 $N=2m$。原整基为
$$
\{\sigma^Nx^i:0\le i\le m\}
\ \cup\
\{\sigma^Nyx^j:0\le j\le m-2\}.
\tag{10}
$$
它的首阶准确覆盖 $0,\ldots,N$ 中除 $N-1$ 外的全部阶，
首系数均为 $\pm1$。原整 sigma、光滑形式参数中的
$x,y$ Laurent 展开使每列是有界整测度。
限制到 $p\mathbf Z_p$、支撑除以 $p$、单位缩放及乘 $\bar\pi$
均保持整测度；再按 (10) 的互异首阶消元，得到
$$
\boxed{K_N\mathcal S_N(\mathcal O)\subset\mathcal S_N(\mathcal O).}
\tag{11}
$$
此证明不要求整个 $N$ 维块是一条 Hecke 单线。

对 $v\in N^{-1}\Lambda$ 使用原对称 lift
$$
(\mathsf T_vF)(z)=e^{-N\eta_v(z+v/2)}F(z+v).
$$
R300 的逐支换元保留整个中心并给
$$
K_N\mathsf T_v=\mathsf T_{gv}K_N,\qquad
g=\pi/\bar\pi=\pi_0/\bar\pi_0
 \pmod{2N\mathcal O_K}.
\tag{12}
$$
此外
$$
\mathsf T_{v+2\ell}=\mathsf T_v,\qquad
\boxed{\mathsf T_{(1+N)v}=\mathsf T_v.}
\tag{13}
$$
第二式来自 $\ell=Nv\in\Lambda$ 和
$\eta_\ell=N\eta_v$；其完整指数常数为一。
这里不能只把参数模 $N$ 丢弃。

两个标准平移生成元的交换子是 primitive 的 $N$ 次根单位。
一个生成元的任一特征向量，由另一生成元循环出 $N$ 个不同
特征值；这给整个 $\mathcal S_N$ 的不可约性及标量交换子结论。
下面只在这个已经支付的完整空间中使用 Schur 引理。

## 3. 原 ratio 的准确二阶和八阶

由 $\pi_0\equiv-1+2\omega\pmod{64}$，其范数为七模六十四，
$$
g\equiv27+8\omega,\quad
g^2\equiv25+48\omega,\quad
g^4\equiv49+32\omega,\quad
g^8\equiv33\pmod{64}.
\tag{14}
$$
每个式子直接使用 $\omega^2=-1-\omega$；
例如 $(27+8\omega)^2=665+368\omega$。
另有 $g\equiv1\pmod9$、$g\equiv-1\pmod{17}$，所以
$$
\boxed{
g\equiv203+136\omega\pmod{272},\qquad
g^2\equiv137=1+136\pmod{272},
}
\tag{15}
$$
$$
\boxed{
g\equiv91+72\omega\pmod{576},\qquad
g^8\equiv289=1+288\pmod{576}.
}
\tag{16}
$$
因此 (12)、(13) 使 $K_{136}^2$、$K_{288}^8$
分别与整个原 Heisenberg 群交换，故各为标量。

绝对标量由两条已证非零来源固定：
$$
K_{136}S(2z)=S(2z),\qquad
K_{288}T(2z)=T(2z).
\tag{17}
$$
这是 (5)、原完整 core 及单位 $[2]$ 推前的直接结果。
$S(2z),T(2z)$ 都从 $64z^6$ 起，非零与待证的中央导数无关。
于是
$$
\boxed{K_{136}^2=I,\qquad K_{288}^8=I.}
\tag{18}
$$
这是整个原二覆盖块的身份，不只在 type0 或给定一条线上成立。

还可看出这两个是本固定 ray 上的**固定有限算子**。
对两个不同素数，它们分别交织同一个 (15)、(16) 的有限
theta 群自同构。由不可约性，两次算子只差标量；
(17) 又使该标量为一。它们在固定 theta 系数域上完全相同，
无需随 $p$ 构造大稠密矩阵。

## 4. principal 分支两个分母是真单位

由 (4)，
$$
\boxed{p=N\pi_0\equiv7\pmod{64}.}
\tag{19}
$$
令 $a_p=\pi_0+\bar\pi_0$ 是 $E_1/\mathbf F_p$ 的实际迹。
它是偶整数：$E_1$ 的有理二挠点 $(-1,0)$ 在这里保持非零，
所以 $\#E_1(\mathbf F_p)$ 为偶数。
在原普通嵌入中 $\pi_0\equiv0\pmod{\mathfrak p}$，故
$$
\bar\lambda=-a_p^{-1}\in\mathbf F_p^\times .
\tag{20}
$$
上横线在 (20) 表示模 $p$ 约化，不是 CM 共轭。

若 $\bar\lambda^8=1$，由
$\gcd(8,p-1)=2$ 得 $a_p^2=1$ 于 $\mathbf F_p$。
在这个域中分解 $(a_p-1)(a_p+1)=0$，所以
$a_p\equiv1$ 或 $-1\pmod p$。
Hasse 界与 $p>7$ 给
$|a_p|\le2\sqrt p<p-1$，于是只能 $a_p=1$ 或 $-1$，
与偶性矛盾。因此
$$
\boxed{1-\lambda^2\in\mathcal O^\times,\qquad
       1-\lambda^8\in\mathcal O^\times.}
\tag{21}
$$
这个证明使用了真实曲线的迹，不从有限 Weyl 相位猜单位。
(21) 只用于 principal 分支；任意 tame 扭转后的中心分母
未被一并宣称为单位。

## 5. 两个输出的完整有限 core 与十六列

取任意一个实际
$F\in\mathcal S_{136}(\mathcal O)\otimes\mathcal S_{288}(\mathcal O)$，
特别可以取 (2) 的每个单独 mixed 来源。
其完整二变量 Amice 测度为 $\nu_F$。
令 $K_1=K_{136}\otimes I$、$K_2=I\otimes K_{288}$。
原乘积线丛及 (10) 给有限张量展开，因而 (9) 逐列给出
保持另一输出的完整等式
$$
\nu_F|_{Y\in p}=\lambda[\kappa,1]_*\nu_{K_1F},\qquad
\nu_F|_{V\in p}=\lambda[1,\kappa]_*\nu_{K_2F}.
\tag{22}
$$
两个真实算子交换，且限制域与另一轴算子交换。
所以全部交叠准确满足
$$
\boxed{
\nu_F|_{Y\in p^n,V\in p^m}
=\lambda^{n+m}[\kappa^n,\kappa^m]_*
                    \nu_{K_1^nK_2^mF}\quad(n,m\ge0).
}
\tag{23}
$$
这保留另一输出的全部连续测试，没有用两个边际替代全联合；
这里未声称原十二个隐藏输入坐标也分别被这些输出算子保持。

定义原 unit-cell 行
$$
\mathcal J_F^{\ell_1,\ell_2}(u,v)=
\int_{\substack{Y\ {\rm unit}\\V\ {\rm unit}}}
 \omega_p(Y)^{\ell_1}\omega_p(V)^{\ell_2}
 \langle Y\rangle^{du}\langle V\rangle^{dv}\,d\nu_F.
\tag{24}
$$
以下只需十六条实际来源
$$
F_{a,b}=K_1^aK_2^bF,\qquad 0\le a<2,\ 0\le b<8.
\tag{25}
$$
每一条由 (7)、(8) 的原 trace 定义，且 (11) 保整。
不把这些来源认成额外曲线，也不预赋各自的中央零。

先取 $|q_1|,|q_2|<1$，按真实输出赋值为每个环带乘
$q_1^nq_2^m$，使用原单位部分 $Y/p^n,V/p^m$。
在任一输出为零处定义值零，即得到全空间连续测试函数和
真正收敛的积分 $\mathcal R_F(q_1,q_2;u,v)$。
置
$$
A_1=q_1\lambda\,\omega_p(\beta)^{\ell_1}\langle\beta\rangle^{du},
\qquad
A_2=q_2\lambda\,\omega_p(\beta)^{\ell_2}\langle\beta\rangle^{dv}.
$$
由 (18)、(23) 对两条环带几何级数准确求和，
$$
\boxed{
\mathcal R_F=
\frac{\displaystyle
 \sum_{a=0}^{1}\sum_{b=0}^{7}
 A_1^aA_2^b\,\mathcal J_{F_{a,b}}^{\ell_1,\ell_2}(u,v)}
 {(1-A_1^2)(1-A_2^8)}.
}
\tag{26}
$$
这是原完整两输出的十六列返回，所有 unit 碰撞补域都在
(24) 中；没有新添“只取输入为单位”的条件。

在任意 tame 分支，(26) 的中心分母在特征零都非零。
例如 $\lambda\omega_p(\beta)^\ell$ 的复绝对值为 $p^{-1/2}$，
其任意正整数次幂不等于一。因此它给中心附近唯一解析芽。

principal 分支的结论更强。置 $q_1=q_2=1$，
(21) 及 $\langle\beta\rangle^{du}\equiv1\pmod p$ 于
$\mathcal O\langle u\rangle$ 给
$$
\boxed{\operatorname{Reg}\mathcal R_F(u,v)
 :=\mathcal R_F(1,1;u,v)\in\mathcal O\langle u,v\rangle.}
\tag{27}
$$
第一轴、第二轴的延拓次序相容，因为它们在 (26) 中是两个
真实可交换算子的逆，而其分母都是单位。
这不只是给非零分母后任意选择有限部。

## 6. 回到每个原 mixed 来源及完整 Riemann 身份

对 $F_j=B_j(2z,2w)$，测度正是 $[2,2]_*\eta_j$。
单位 $2$ 不改任何输出赋值，故 (26)、(27) 返回原 $\eta_j$
时必须且只须乘
$$
\boxed{
\omega_p(2)^{-\ell_1-\ell_2}
 \langle2\rangle^{-d(u+v)}.
}
\tag{28}
$$
对单个 mixed 来源不擅自删去这个因子的导数质量项。
(28) 证明两个 $B_j$ **各自**都有整 principal 双输出正则化，
不再仅靠 R404 中它们的和。

另一方面，(1) 在整个固定二覆盖空间中成立。
所有原 trace、(24) 及 resolvent 都是线性操作。
原 $S(2z)\otimes T(2w)$ 又在 $K_1,K_2$ 下各自特征一，
所以两列的几何分子准确简化为
$$
\boxed{
\operatorname{Reg}\mathcal R_{B_2}
+\operatorname{Reg}\mathcal R_{B_3}
=\frac{J_S(u)J_T(v)}
 {(1-\lambda\langle\beta\rangle^{du})
  (1-\lambda\langle\beta\rangle^{dv})}.
}
\tag{29}
$$
(28) 与原 $[2]$ 两个 Mellin 因子在此精确相消。
(29) 与 R404 的全和正则化相同，而本篇还支付两个单项。

因 $J_S(0)=J_T(0)=0$，两曲线实际失败仍迫使 (29) 属于
$u^2v^2\mathcal O\langle u,v\rangle$。
这不是单项各自二重零；保留完整 mixed 差项仍是必要的。

## 7. 同一原全深输入因子的整消除

现在保 R404 的同一个十二 sigma 输入及原域
$\mathcal D$：“十二个输入不全在 $p\mathbf Z_p$”。
在本 ray 上 $\varepsilon=-1$，
原 sigma 的 core 为 $-\lambda$，故十二输入全深的系数正是
$$a=(-\lambda)^{12}=\lambda^{12}.$$
每个 $B_j$ 都是该十二输入的真实线性推前，不需要先相加。
因此在真正收敛的 $|q_1|,|q_2|<1$ 域，逐项有
$$
\boxed{
\mathcal R_{\mathcal D,j}
=\left(1-q_1q_2\lambda^{12}
 \omega_p(\beta)^{\ell_1+\ell_2}
 \langle\beta\rangle^{d(u+v)}\right)\mathcal R_{B_j}.
}
\tag{30}
$$
这个因子来自实际全深输入，不是由输出 degree 猜测的 Euler 因子。
$[2]$ 不改原输入深度或输出赋值，(28) 与 (30) 完全相容。

取 principal 分支并按 (27) 正则化，得到整 Tate 环中的准确整除：
$$
\boxed{
\operatorname{Reg}\mathcal R_{\mathcal D,j}
\in
\left(1-\lambda^{12}\langle\beta\rangle^{d(u+v)}\right)
                         \mathcal O\langle u,v\rangle,
}
\tag{31}
$$
而其整商恰为 (26)、(28) 给出的同一个
$\operatorname{Reg}\mathcal R_{B_j}$。
**即使 $1-\lambda^{12}$ 不是 $p$ 单位，(31) 仍成立。**
所以先消原全深输入因子、先延拓第一输出、先延拓第二输出，
都得到同一个已付整函数；该因子的任何盘内零都已由真实分子消掉。

(31) 是原 mixed 来源之正则化函数的整除；
它没有声称一个全局椭圆单位格的 principalization，
也不将另一个未经支付的线性超平面自动加入正则化。
这里已完成的是实际 $\mathcal D,Y,V$ 三种操作之间的相容性。

## 8. 范围及后续真正的中央约束

本篇把 R404 的两个单独 mixed 来源保在正确的二覆盖上，
并给固定无穷 ray 上的两阶/八阶原算子和十六条固定来源。
真实曲线的偶迹进一步支付 principal 分支的单位分母，
故其完整两输出正则化保整且次序相容。
同一原全深输入因子在整 Tate 环中准确消除，而不是被当成单位。

尚未证明原 $J_S'(0)$、$J_T'(0)$ 至少一个对无穷 $p$ 非零。
也没有将 (29) 的全和零传播给 (25) 的各个来源。
可以继续比较 R405 四角联合与这里的真实 $(Y,V)$ 输入域；
任何额外 hyperplane 或隐藏输入限制仍须逐个由同一原联合支付。

直接依赖：
[R300](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)、
[R316](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)、
[R396](R396-original-nontrivial-quartic-ray-three-cores-and-complete-scale-boundary.md)、
[R398](R398-e24-actual-polynomial-six-sigma-source-and-original-central-comparison.md)、
[R399](R399-original-two-ranktwo-cross-source-and-overlapping-core-domains.md)、
[R400](R400-full-square-interpolation-determines-core-and-e24-cmseven-phase.md)、
[R404](R404-two-original-ranktwo-riemann-joint-and-complete-two-axis-central-transport.md)。

全文使用原 division trace、含中心 theta 群和真实非零锚；
没有构造或提交大型稠密矩阵，也没有以素数扫描证明无穷结论。
当前终端不可用；按根规矩八以小文本 GitHub Contents API 提交，
不是本地 git pull。2026-11-14 03:14:29 UTC 读取 main
a69df5cf97d39cb05be225139523ba333a64ea27；
根 README blob 为 f787a306d90892d8dec765dc59747d60ba39f055，
本课题 README blob 为 f8dd8071ac0c2b31f344a40c15ac2a42796bf9af。
两者与已读版本相同；读号交根代理记入 HANDOFF。
