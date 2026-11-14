# R327：原目标的单 sigma 二次差权与 p² 收缩重构

日期：2026-11-13。**状态：原秩二来源的八个同 sigma 输入、准确二次差权、全部输入 p 的两阶收缩、完整测度的范数收敛重构、所有输出 carry 与原中央零的准确等价均已证明。该来源没有秩零参考斜率。条件输出的零阶平均为零，但完整归一输出测度没有额外的 p 因子；下文用一个真实单位矩严格区分这两点。尚未由此证明目标中央导数非零。**

## 1. 原 CM7 加法公式给出同一个目标

固定 $E_b:y^2=x^3+b$、$b=17$，保持
$$
dz=\frac{dx}{2y},\qquad x=z^{-2}+\cdots,\quad
y=-z^{-3}+\cdots,\quad \sigma=z+\cdots,
$$
以及 $X=x^3$、$\Theta=x\sigma^2$。令
$$
\omega^2+\omega+1=0,\qquad \delta=1+2\omega,\qquad
\gamma_7=3+\omega=\frac{5+\delta}{2}.
$$
所以 $\delta^2=-3$，且
$$
2-\delta=-\omega\gamma_7,\qquad
2+\delta=-\omega^2\bar\gamma_7.
\tag{1}
$$
原 reduced sigma 满足 $\sigma(\zeta z)=\zeta\sigma(z)$ 对 $\zeta\in\mu_6$。
式 (1) 的两个单位乘积为一，故 R297 的真实 CM7 乘积准确是
$$
\sigma(\gamma_7z)\sigma(\bar\gamma_7z)
=\sigma((2+\delta)z)\sigma((2-\delta)z).
$$
用同一 sigma 的加法公式，右边等于
$$
\sigma(2z)^2\sigma(\delta z)^2
                 \{x(\delta z)-x(2z)\}.
\tag{2}
$$
这里的负号由 $x(v)-x(u)$ 固定，不能由总次数猜测。

R297 已识别的原秩二来源是
$$
S=\frac1{28}\sigma(z)^2\sigma(2z)^2\Theta(z)\Theta(2z)
                       \sigma(\gamma_7z)\sigma(\bar\gamma_7z).
\tag{3}
$$
又 R319 的真实三同源式给
$$
\sigma(\delta z)=\delta\sigma(z)\Theta(z),\qquad
\sigma(2\delta z)=\delta\sigma(2z)\Theta(2z).
\tag{4}
$$
因而设
$$
\boxed{Q=\sigma(z)\sigma(2z)^3\sigma(\delta z)^3\sigma(2\delta z),}
\tag{5}
$$
则 (2)–(4) 给出本篇的固定原恒等式
$$
\boxed{S=\frac{Q}{84}\{x(2z)-x(\delta z)\}.}
\tag{6}
$$
这八个因子的真实 theta 次数是 $1+3\cdot4+3\cdot3+12=34$，原点总阶为八。
它们全部来自同一个 sigma，零除子只在固定 $E[6]$。

也可完全在原曲线上核定 (6)。准确有
$$
\begin{aligned}
Q&=144\sigma^{34}x^4(X+b)^2(X-8b),\\
x(2z)&=\frac{x(X-8b)}{4(X+b)},\\
x(\delta z)&=-\frac{X+4b}{3x^2},\\
x(2z)-x(\delta z)
 &=\frac{7X^2-4bX+16b^2}{12x^2(X+b)}.
\end{aligned}
\tag{7}
$$
代入后正得
$$
S=\frac17\sigma^{34}x^2(X+b)(X-8b)
                         (7X^2-4bX+16b^2),
\tag{8}
$$
即 R297 的原多项式。$Q=144z^8+\cdots$，括号首项为
$7/(12z^2)$，所以 $S=z^6+\cdots$，没有未定标量。
第二个原系数同样保留：$[z^{12}]S=-988b/105$。
由 $\log(\sigma/z)=bz^6/210+\cdots$，
$[z^6]\log(Q/(144z^8))=-808b/105$，再用 (7) 即得。

## 2. 同一个 sigma 测度上的二次差权

由 $(\log\sigma)''=-x$，(6) 等价于
$$
\boxed{
S=-\frac{Q}{1008}
 \left\{3(\log\sigma(2z))''+4(\log\sigma(\delta z))''\right\}.}
\tag{9}
$$
两项在 $z$ 上分别给 $-12x(2z)$、$12x(\delta z)$，故符号与 (6) 相同。
虽然写成 log 导数，(9) 乘回 $Q$ 后全局全纯：所需每一对 sigma 都已在
$Q$ 中出现，没有未支付的除子。

现在固定普通素数 $p>7,p\equiv1\pmod3$，使用 R300、R316 的同一个
$E_{17}$ 形式周期 $\Omega_p$ 和原有界整测度
$$
\sigma(\Omega_p\log(1+T))
       =\int_{\mathbf Z_p}(1+T)^x\,d\nu_\sigma(x).
$$
把 $\delta$ 取为这个普通嵌入中的单位。置 $\mu=\nu_\sigma^{\otimes8}$，
八个变量按 $s,a_1,a_2,a_3,r_1,r_2,r_3,t$ 排列，并定义
$$
\begin{aligned}
y&=s+2(a_1+a_2+a_3)+\delta(r_1+r_2+r_3)+2\delta t,\\
w&=(a_1-a_2)^2-(r_1-r_2)^2.
\end{aligned}
\tag{10}
$$
**定理1（原完整测度）。**
$$
\boxed{\nu_S=-\frac1{168\Omega_p^2}\,y_*(w\mu).}
\tag{11}
$$

证明对两个相同 sigma 输入使用准确恒等式
$$
\int (u-v)^2e^{a(u+v)z/\Omega_p}
               \,d\nu_\sigma(u)d\nu_\sigma(v)
=2\Omega_p^2\{\sigma''(az)\sigma(az)-\sigma'(az)^2\}.
\tag{12}
$$
这里右侧的 prime 指 sigma 自变量的导数；没有额外遗漏 $a^2$。
分别取 $a=2,\delta$，再乘其余六个真实因子，(12) 的差为
$-2\Omega_p^2Q(x(2z)-x(\delta z))$。由 (6) 得 (11)。
有界测度的 Amice 变换单射，故这是整个测度的恒等式，包括非单位输出、
所有 tame 分支和原点；并非只核正整数矩。$\square$

这个核没有 $H_3,H_5$ 的斜率或逆参考。它也没有把加法 Mellin 拆成各因子的
乘法 Mellin：单位条件始终是原来的 $y\in\mathbf Z_p^\times$。

### 2.1 真正的对称平均及其边界

交换两个三元组 $(a_1,a_2,a_3)$ 和 $(r_1,r_2,r_3)$ 保持 $\mu$。记
$$
\widetilde y=s+\delta(a_1+a_2+a_3)+2(r_1+r_2+r_3)+2\delta t,
\qquad q_a=(a_1-a_2)^2.
$$
于是对任意连续测试函数 $\varphi$，
$$
\boxed{\nu_S(\varphi)
 =-\frac1{168\Omega_p^2}
   \int q_a\{\varphi(y)-\varphi(\widetilde y)\}\,d\mu.}
\tag{13}
$$
还可在每个三元组内平均，将 $(a_1-a_2)^2$ 换为
$$
\frac13\sum_{i<j}(a_i-a_j)^2
   =\sum_i a_i^2-\frac{(a_1+a_2+a_3)^2}{3},
\tag{14}
$$
另一组三个变量同理。这是实际 product measure 的对称平均。

式 (13) 没有说两个输出的单位域相同。以原 principal 中央变量 $d=p-1$ 记
$$J_S(u)=\int_{\mathbf Z_p^\times}\langle x\rangle^{du}\,d\nu_S(x).$$
令 $\mathcal B$ 为 $y,\widetilde y$ 都为单位的域，
$\mathcal B_y$ 为只有 $y$ 为单位的域，$\mathcal B_{\widetilde y}$ 为只有
$\widetilde y$ 为单位的域。则完整中央导数为
$$
\boxed{\begin{aligned}
J_S'(0)=-\frac d{168\Omega_p^2}\bigg[
 &\int_{\mathcal B}q_a\log_p(y/\widetilde y)\,d\mu\\
 &+\int_{\mathcal B_y}q_a\log_p\langle y\rangle\,d\mu\\
 &-\int_{\mathcal B_{\widetilde y}}
                         q_a\log_p\langle\widetilde y\rangle\,d\mu
\bigg].
\end{aligned}}
\tag{15}
$$
这保留了两项真正的边界贡献。单独的 norm-one 比值不能替代整个式子。

## 3. 全部输入 p 给真正的两阶收缩

沿同一已付普通规范，置
$$
\pi=\psi_{17}(\mathfrak p),\quad \pi\bar\pi=p,\quad
v_p(\pi)=1,\quad
\varepsilon=\psi_0(\mathfrak p)/\psi_{17}(\mathfrak p)\in\mu_6,
\quad \kappa=p/\bar\pi^2.
$$
R316 的原 sigma core 为
$$
\nu_\sigma|_{p\mathbf Z_p}
       =\frac{\varepsilon^3}{\bar\pi}[\kappa]_*\nu_\sigma.
\tag{16}
$$
令
$$
\mathcal D=\mathbf Z_p^8\setminus(p\mathbf Z_p)^8,\qquad
\Pi=-\frac1{168\Omega_p^2}
                 y_*(\mathbf1_{\mathcal D}w\mu).
\tag{17}
$$
$\Pi$ 保留所有输出，包括 $y\in p\mathbf Z_p$。
八个输入同时属于 $p\mathbf Z_p$ 时，有限角色为
$(\varepsilon^3)^8=1$；二次权额外贡献 $\kappa^2$。准确的全系数是
$$
\boxed{\left(\frac{\varepsilon^3}{\bar\pi}\right)^8\kappa^2
                      =\frac{p^2}{\bar\pi^{12}}=:a_p,\qquad v_p(a_p)=2.}
\tag{18}
$$
因此 (11) 给完整恒等式
$$
\boxed{\nu_S=\Pi+a_p[\kappa]_*\nu_S.}
\tag{19}
$$
这里的两个 $p$ 来自真实二次权，不来自一个任意正则化。

**定理2（范数收敛重构）。** 在原有界整测度的 Banach 范数中，
$$
\boxed{\nu_S=\sum_{r\ge0}a_p^r[\kappa^r]_*\Pi.}
\tag{20}
$$
截断到 $r=N$ 的尾正好是
$$a_p^{N+1}[\kappa^{N+1}]_*\nu_S,$$
其范数至多 $p^{-2(N+1)}$。因而 (19) 在有界测度中有唯一解。

证明 $[\kappa]_*$ 的范数至多一，$\|\nu_S\|,\|\Pi\|\le1$，
而 $|a_p|=p^{-2}$，故 (19) 的迭代在范数中收敛并给上述准确尾。
若两解相减，则 $\|\eta\|\le p^{-2}\|\eta\|$，只能 $\eta=0$。
因此这里没有未定 Dirac 项，也不只是在稠密整数权上重构。$\square$

对任何有界连续测试函数，上述尾界乘其范数即可；对一个局部解析参数族，
包括每个固定输出环带上的 Mellin 及其任意阶参数导数，同一结论逐导数成立。
原单位测试在 $r\ge1$ 的项上为零，故 $J_S$ 就是 $\Pi$ 的单位输出。
这并不允许删掉 $\Pi$ 本身的非单位输出：它们在 (19)、下一节的真实 carry
及参数化比较中仍然存在。

这是按全输入的共同 p 深度作的范数收敛；不要将它换成一个未经证明的
按所有归一输出环带作范数收敛的级数。

## 4. 全部输出 carry 与原中央零的准确传播

R300 给的是同一个原来源的完整 core：
$$
\nu_S|_{p\mathbf Z_p}=\bar\pi^{-1}[\kappa]_*\nu_S,\qquad T_pS=S.
\tag{21}
$$
对 $n\ge0$，定义 (17) 的实际归一输出测度
$$
\mathfrak C_n=-\frac1{168\Omega_p^2}(y/p^n)_*
             (\mathbf1_{\mathcal D,\ v_p(y)=n}w\mu).
\tag{22}
$$
$n=0$ 时 $\mathfrak C_0=\nu_S^\times$。对 $n\ge1$，
先用 (21) 取整个第 $n$ 输出环带，再用 (18) 减去全部输入非单位的
第 $n-1$ 环带，得到
$$
\boxed{\mathfrak C_n=
 \bar\pi^{-n}[\bar\pi^{-2n}]_*
        \left(1-\frac{p^2}{\bar\pi^{11}}\right)\nu_S^\times.}
\tag{23}
$$
括号是单位。它的指数 $11$ 是 $12-1$，不能误写成未加权八核的指数。

对任何 tame 指数 $j$，定义
$$M_j(u)=\int_{\mathbf Z_p^\times}
                  \tau(x)^j\langle x\rangle^{du}\,d\nu_S(x).$$
则 (23) 的完整 Mellin 为
$$
\boxed{\mathfrak C_{n,j}(u)=
 \left(1-\frac{p^2}{\bar\pi^{11}}\right)
 \bar\pi^{-n}\tau(\bar\pi)^{-2nj}
 \langle\bar\pi\rangle^{-2ndu}M_j(u).}
\tag{24}
$$
求导必须保留 $-2nd\log_p\bar\pi\,M_j(0)$。所以本篇没有从 principal
中央零推断其他 tame 分支的任意质量或导数为零。

在目标 principal 支上，$S(0)=0$ 与 (21) 给 $J_S(0)=0$。于是
$$
\boxed{
\mathfrak C_{n,0}(0)=0,\qquad
\mathfrak C_{n,0}'(0)
 =\left(1-\frac{p^2}{\bar\pi^{11}}\right)\bar\pi^{-n}J_S'(0)
 \quad(n\ge1).}
\tag{25}
$$
因此任意一层 (22) 的完整 principal 中央导数为零，都与原 $J_S'(0)=0$
严格等价；反方向也成立。这是由原完整测度推出的真实零传播。
没有将新增的 $V$、$A_6$ 或其他有限空间方向另行指定为零。

## 5. 输出 y ≡ 0 的条件平均：质量为零，但没有整条额外 p

式 (25) 证明归一每一非单位输出层的零阶条件平均准确为零。
另一方面，二次差权和 $y\equiv0$ 的条件并不使整个归一输出测度多一个 $p$。
可以对同一个实际测度作精确的非样本检验。

原 $S=z^6+\cdots$，所以完整第六矩为 $6!\Omega_p^6$。
由 (21)，单位第六矩准确是
$$
\int_{\mathbf Z_p^\times}x^6\,d\nu_S(x)
 =\left(1-\frac{\pi^6}{\bar\pi^7}\right)6!\Omega_p^6.
\tag{26}
$$
再用 (23)，得到对每个普通 $p>7$、每个 $n\ge1$：
$$
\boxed{
\int x^6\,d\mathfrak C_n(x)
 =\bar\pi^{-13n}
  \left(1-\frac{p^2}{\bar\pi^{11}}\right)
  \left(1-\frac{\pi^6}{\bar\pi^7}\right)6!\Omega_p^6
 \in\mathcal O^\times.}
\tag{27}
$$
两个 Euler 因子和 $\Omega_p$ 都是单位，且 $p\nmid6!$。
所以即使完成 (13)、(14) 的真实对称平均，(22) 的原测度仍不是 $p$ 倍整测度。
这是完整归一输出的结论；原输出坐标的六阶矩另带平凡的 $p^{6n}$，
不能将两种坐标混同。

式 (27) 只是检查所谓“额外 p”是否实际存在。它不是 $J_S'(0)$，
也不由它推断目标中央非零。相反，(25) 和 (27) 可以同时成立：
一条完整测度的质量及中央导数为零，并不迫它的第六矩为零。

## 6. 与 R321、R323 的同 U 观察真正相接

保持
$$
U=\Theta(z)\Theta(2z)^4,\qquad
A_6=U/X,\quad B_6=U/(X-8b),\quad C_6=U/(X-8b)^2.
$$
R323 的新实际 pure-plus 来源为
$$
V=\frac13\sigma(2z)\Theta(2z)^3\Theta(\delta z)
  =\frac1{3\delta}\sigma(2\delta z)\Theta(2z)^2\Theta(\delta z).
\tag{28}
$$
后式直接用了 (4)，所以新旧核共享真实 norm2、norm3 来源。
它的完整返回 $D_V=\nabla_UV$ 满足
$$
D_V=\frac23U-\frac{4b}{3}A_6+60bB_6+432b^2C_6,
$$
$$
S+\frac{H_3+U}{336b}
 =\frac{A_6}{168}-\frac{3B_6}{56}+\frac{D_V}{112b}.
\tag{29}
$$
这些是 R323 已付的真实全函数身份，不在这里重做其五输入分解。

在 R321 的同一普通中央规范
$$
\mathcal C_U(G)=J_G'(0)-J_G(0)\frac{J_U'(0)}{J_U(0)}
$$
中，原 $J_U(0)\ne0$，且 $J_S(0)=0$。所以
$$
\boxed{
\frac{\mathcal C_U(A_6)}{168}
-\frac{3\mathcal C_U(B_6)}{56}
+\frac{\mathcal C_U(D_V)}{112b}
-\frac{\mathcal C_U(H_3)}{336b}
=J_S'(0),}
\tag{30}
$$
而右端现在准确由 (15) 的同一个单 sigma 核给出。
因此所有参考质量、$U$ 斜率、$V$ 的 tame-one 一阶导数和连接卷积的
这个指定组合，都被放进了一个没有参考斜率的实际原观察。
这是完整来源恒等式消去，不是分别将各项设为零。

更具体地，R321 的 $D_1$ 及六真 CM 行仍给
$$
J_S'(0)=
-\frac3{112}\mathcal C_U(B_6)
+\Omega_p^{-1}\{Z_1'(0)-\ell_UZ_1(0)\}
-\{Q_1'(0)-\ell_UQ_1(0)\}.
\tag{31}
$$
式 (15) 正好替换 (31) 的整个右侧，而非只替换一个裸 dlog。
特别没有把 exact 部分的实际中央贡献删去。

旧 $C_X$ 的两种返回和 (28) 仍保 R321、R323 的全部 carry。
新优势是 (11) 直接输出原 $S$，故其输出 core 是标量一、其 principal
中央零由 (25) 控制；不需要给这些新增来源假定中央零。

## 7. 全尾与惯性处的适用范围

普通处 (11) 是八个有界整测度的有限加法卷积，所以各 tame Mellin 在原
$p$-进单位支上解析；式 (15) 可在相应开闭单位域上逐参数求导。
式 (20) 更给所有输入共同深度的统一两阶范数尾，不以“形式无限和”代替。

代数恒等式 (6)、(9) 对惯性处同样准确，但不能把普通测度 $\nu_\sigma$
搬到高度二。若 $p=6s-1>7,p\ne17$，使用 R301 的原
$$
c_p=[z^{p+1}]\log(\sigma/z),\quad \kappa_0=34c_p,\quad
\widehat S=e^{-\kappa_0z^{p+1}}S.
$$
由 (7) 的真实表达，$\widehat Q$ 在 R301 的
$R=p^{-1/(2p)}$ 圆盘范数至多 $R^8$；
$z^2(x(2z)-x(\delta z))$ 解析、范数至多一。
于是 (6) 给 $\|\widehat S\|_R\le R^6$，准确重现同一原来源的 Gauss 界。
它的全部 Newton 系数与中央功能仍是
$$
J_{S,p}(u)=\sum_{h\ge0}
 [z^{(p+1)h}]\widehat S\;\kappa_0^{-h}(u)_h,
\quad
v_p(\text{第 }h\text{ 项系数})
 \ge\left\lceil\frac{h(p-1)+6}{2p}\right\rceil.
\tag{32}
$$
这里没有删掉 (9) 中任何 sigma 比或 Gaussian；也没有从单 sigma
代数身份推定普通的 $p$-core 可在惯性处使用。

## 8. 证书与当前结论

脚本 check-jzero-single-sigma-quadratic-kernel.py 及同名 JSON
精确核定 CM7 两个方向与单位相位、原多项式、真实 degree、首两项、
二次权标量、交换两组三输入的原关系、全部输入的两阶系数，以及条件输出
第六矩的全部 Euler 因子。没有扫描目标素数。
测度单射、完整 contraction、参数全尾及中央零传播由本文正文证明。

本篇把原 $J_S'(0)$ 放进一个八个相同测度上的固定二次差权，
并使全部输入 p 的重构成为范数收敛的严格收缩。原参考斜率没有留在该表达式中。
但 (15) 的单位域边界和相加对数仍须真正控制，(25) 只是正确的等价零传播，
不是跨素数非零的证明。

依赖：

- [R297：真实原来源与 CM7 乘积](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)。
- [R300：原全 theta p-core 与单 Euler 测度](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)。
- [R301：惯性原半因子与 Gauss 全尾](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)。
- [R316：同 frame 的真实低 degree core](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)。
- [R319：真实 norm3 与混合缩放](R319-jzero-ramified-three-minimal-unit-and-mixed-scaled-return.md)。
- [R321：完整 U primitive 与两素类中央转置](R321-jzero-fixed-six-torsion-primitives-and-complete-u-frame-transpose.md)。
- [R323：新 pure-plus 五因子及其原中央返回](R323-new-pure-five-factor-source-and-complete-central-kernels.md)。
