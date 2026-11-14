# R333：六个原 sigma 输入与两种二次核的完整负矩返回

日期：2026-11-13。**状态：原目标的六 sigma 核、恰一个输入为单位的完整负权展开、同目标的两种真实二次核及其原单位域差均已证明。两种二次核的差有一个对全部普通 p>7 都为单位的固定首系数，准确乘原负五次矩；完整高尾只读同一原负矩族，没有剩余参考斜率。本篇没有把一个输入子域的中央导数单独设为零，也没有预支负五次矩的非零。**

## 1. 再合并一次后的真正六 sigma 来源

沿 R297、R316、R327，固定 $E_{17}$ 的原 reduced sigma、普通周期
$\Omega_p$ 和 $\delta^2=-3$，$\gamma=(5+\delta)/2=3+\omega$。
R297 的原目标为
$$
S=\frac1{28}\sigma(z)^2\sigma(2z)^2
       \Theta(z)\Theta(2z)\sigma(\gamma z)\sigma(\bar\gamma z).
$$
将两个实际 $\Theta$ 都用
$\sigma(\delta w)=\delta\sigma(w)\Theta(w)$ 合并，准确得到
$$
\boxed{S=-\frac1{84}
 \sigma(z)\sigma(2z)\sigma(\delta z)\sigma(2\delta z)
                      \sigma(\gamma z)\sigma(\bar\gamma z).}
\tag{1}
$$
尺度向量记为
$$
\boldsymbol a=(1,2,\delta,2\delta,\gamma,\bar\gamma),
\qquad \prod_{i=1}^6a_i=-84.
\tag{2}
$$
它的真实次数为 $1+4+3+12+7+7=34$，首项准确为 $z^6$。
没有另选一个具有相同阶的候选。

对普通 $p>7,p\equiv1\pmod3$，所有 $a_i$ 都是原嵌入中的单位。
令 $\nu=\nu_{\sigma,17}$ 为 R316 的同一个原测度。则 (1) 是完整式
$$
\boxed{\nu_S=-\frac1{84}
 \left(\sum_{i=1}^6a_ix_i\right)_*\nu^{\otimes6}.}
\tag{3}
$$
它没有 $\Theta$ 输入，也没有输入质量一边界；六个输入的质量均为零。
对原 principal 支，置 $d=p-1$，则
$$
J_S(u)=-\frac1{84}\int
 \mathbf1_{\sum a_ix_i\in\mathbf Z_p^\times}
       \left\langle\sum a_ix_i\right\rangle^{du}\,d\nu^{\otimes6}.
\tag{4}
$$
所有单位条件仍施加于真实相加输出。

本文用
$$
\lambda=\frac{\varepsilon^3}{\bar\pi},\qquad
\kappa=\frac p{\bar\pi^2},\qquad
t_p=\lambda\kappa=\frac{\varepsilon^3p}{\bar\pi^3},
\tag{5}
$$
其中 $\pi=\psi_{17}(\mathfrak p)$、$\pi\bar\pi=p$，
$\varepsilon=\psi_0(\mathfrak p)/\psi_{17}(\mathfrak p)$。
R316 的原完整等式是 $\nu|_p=\lambda[\kappa]_*\nu$。
六输入同时在 $p$ 内的系数是 $\lambda^6=\bar\pi^{-6}$。
结合 R300 的整个目标 core，(3) 的原 primitive-input 第 $n$ 输出
carry 为
$$
\bar\pi^{-n}[\bar\pi^{-2n}]_*
                   (1-\bar\pi^{-5})\nu_S^\times\qquad(n\ge1).
\tag{6}
$$
本篇不再重复 R327、R330 已付的 carry 证明；下面的新内容是指定输入域
对原负矩的完整返回。

## 2. 恰一个输入为单位：六核的整个五深展开

定义原正矩和负矩函数
$$
\mu_r=\int_{\mathbf Z_p}x^r\,d\nu(x),\qquad
I_{-R}(u)=\int_{\mathbf Z_p^\times}
                      x^{-R}\langle x\rangle^{du}\,d\nu(x).
\tag{7}
$$
$\mu_r=0$ 除非 $r\equiv1\pmod6$，且 $\mu_1=\Omega_p$。
所有 (7) 的负权函数都属于原 $\mathcal O\langle u\rangle$。
固定记
$$I_{-5-6K}=I_{-5-6K}(0)\qquad(K\ge0).$$
它们是 R332 的同一 $E_{17}$、同一周期和同一测度的负矩；
不将其直接换成基曲线的无尺度数值。

对每个 $j$，取实际域
$$
\mathcal E_j=\{x_j\in\mathbf Z_p^\times,\quad x_i\in p\mathbf Z_p
                                      \text{ 对所有 }i\ne j\}.
\tag{8}
$$
在这个域上输出必为单位，因为 $a_j$ 为单位。
记 (4) 在 $\mathcal E_j$ 上的整条函数为 $D_{6,j}(u)$。
利用 (5)，在单位 $a_jx_j$ 周围展开，准确有
$$
\boxed{\begin{aligned}
D_{6,j}(u)=-\frac{\lambda^5\langle a_j\rangle^{du}}{84}
\sum_{\substack{r_i\ge1,\ r_i\equiv1\ (6)\\i\ne j}}
 &(du)_R\,a_j^{-R}I_{-R}(u)\\
 &\times\prod_{i\ne j}
       \frac{(\kappa a_i)^{r_i}\mu_{r_i}}{r_i!},
\qquad R=\sum_{i\ne j}r_i.
\end{aligned}}
\tag{9}
$$
这里每个输入属于整个 $p\mathbf Z_p$，而不只是第一个环带；
(9) 已用真实 core 包含其全部更深部分。

写 $r_i=1+6k_i$、$K=\sum k_i$，则 $R=5+6K$。
每一项的 $(du)_R$ 在 $u=0$ 为零，所以 $D_{6,j}(0)=0$。
求导没有留下 $I_{-R}'(0)$、$\log_p a_j$ 或任何参考斜率，准确为
$$
\boxed{
D_{6,j}'(0)
=-\frac{d\lambda^5}{84}
 \sum_{\boldsymbol r}(R-1)!\,a_j^{-R}I_{-R}
       \prod_{i\ne j}\frac{(\kappa a_i)^{r_i}\mu_{r_i}}{r_i!}.}
\tag{10}
$$
符号来自 $R$ 恒为奇数，故 $(du)_R'(0)=d(R-1)!$。

所有 tame 分支也仍在原接口中。若测试函数为
$\mathbf1_{\mathrm{unit}}\tau(x)^\ell\langle x\rangle^{du}$，
只须在 (9) 外面乘 $\tau(a_j)^\ell$，并将 $I_{-R}(u)$ 换成
$$
I_{\ell,-R}(u)=\int_{\mathbf Z_p^\times}
        \tau(x)^\ell x^{-R}\langle x\rangle^{du}\,d\nu(x).
$$
这是因为在实际单位盘内 Teichmüller 角色不变。下文二次核 (17)
同样乘 $\tau(c_{L,j})^\ell$ 并用 $I_{\ell,e_j-R}$。
本文的目标与固定负族取 $\ell=0$；没有将其他分支的值替成 principal 值。

### 2.1 全部尾与恰一单位域的固定首系数

普通素数在本范围内至少为十三。因为 $\mu_r$、负矩函数均整，
而
$$
\sum_i v_p(r_i!)\le\frac{6K}{p-1},
$$
$K=1$ 的全部阶乘为单位；$K\ge2$ 时右端的整数部分至多 $K-1$。
所以 (9) 的 $K\ge1$ 部分属于 $p^{11}\mathcal O\langle u\rangle$，
且随 $K$ 增长的估计至少为 $5+6K-(K-1)$。
这证明整个级数、任意中央导数及以下余项的收敛。

令 $D_6=\sum_jD_{6,j}$，即整个“恰一个输入为单位”域。
由 (2)，全部 $r_i=1$ 的实际首项给
$$
\boxed{
D_6'(0)=d\,t_p^5\Omega_p^5 C_6I_{-5}
                              \pmod{p^{11}\mathcal O},}
\tag{11}
$$
$$
\boxed{
C_6=24\sum_{j=1}^6a_j^{-6}
 =\frac{99166301}{36\cdot7^6}
 =\frac{13\cdot19\cdot97\cdot4139}{36\cdot7^6}.}
\tag{12}
$$
此处准确用了
$$
\sum_{a\in\{1,2,\delta,2\delta\}}a^{-6}=\frac{845}{864},
\qquad \gamma^{-6}+\bar\gamma^{-6}=-\frac{286}{7^6}.
$$
因此不能遗漏 $p=13,19,97$ 对 (11) 首系数的影响；
所有 $p$ 的完整式仍是 (9)、(10)。

## 3. 同一目标的两种真实八 sigma 二次表示

保持共同四因子
$$
Q_{\mathrm{com}}=\sigma(z)\sigma(2z)\sigma(\delta z)\sigma(2\delta z).
$$
R327 使用 CM7 方向的单位旋转，将其余两因子写成
$\sigma((2+\delta)z)\sigma((2-\delta)z)$，其相位乘积为一。
直接使用 $\gamma,\bar\gamma$ 本身则有
$\gamma+\bar\gamma=5$、$\gamma-\bar\gamma=\delta$。
因此对以下两个实际参数对，
$$
(u_A,v_A)=(2,\delta),\qquad
(u_B,v_B)=(5/2,\delta/2),
\tag{13}
$$
都准确有
$$
\boxed{
S=\frac{Q_{\mathrm{com}}\sigma(u_Lz)^2\sigma(v_Lz)^2}{84}
              \{x(u_Lz)-x(v_Lz)\},\qquad L=A,B.}
\tag{14}
$$
这两式分别是同一个 sigma 加法公式的两组真实输入，不是相近总次数的猜测。
两组均满足 $u_L^2-v_L^2=7$，首项同为 $z^6$。

第二组的单独因子在固定二覆盖上取值。把自变量统一换为 $2z$ 后，
所有尺度变成整数 CM 尺度，且整个来源准确是 $S(2z)$；
原完整单位 Mellin 乘 $\langle2\rangle^{du}$。
本文直接在 (13) 的原普通测度上保留单位 $1/2$，所以不遗漏这个尺度。
整条来源及下面每个恰一单位域的质量均为零，故求其 principal 中央导数时，
相应 $\log_p2$ 质量项准确为零。其他 tame 分支不作这一步无条件删除。

在固定八变量上，用共同尺度向量
$$
\boldsymbol c_L=(1,2,\delta,2\delta,u_L,u_L,v_L,v_L)
$$
及同一二次权
$$W=(x_5-x_6)^2-(x_7-x_8)^2.$$
则 R327 的完整 variance 恒等式给两份真正原测度
$$
\boxed{\nu_S=-\frac1{168\Omega_p^2}
                 \left(\sum_i c_{L,i}x_i\right)_*
                            (W\nu^{\otimes8}),\qquad L=A,B.}
\tag{15}
$$
特别两个相加输出的单位域不是先验相同的集合。

## 4. 两种二次核在恰一单位域的完整负族

把 $W$ 展开成有限单项式
$$W=\sum_{\boldsymbol e}h_{\boldsymbol e}x_1^{e_1}\cdots x_8^{e_8},
\qquad |\boldsymbol e|=2.$$
对某个 $j$，仍取 $x_j$ 为单位、其余七输入在 $p\mathbf Z_p$，
记 (15) 上该域的函数为 $D_{L,j}(u)$。
对每个 $i\ne j$ 令 $r_i\ge e_i$ 且 $r_i\ge1,r_i\equiv1\pmod6$，并置
$$
R=\sum_{i\ne j}(r_i-e_i),\qquad
\sum_{i\ne j}r_i=7+6K.
$$
因为 $|\boldsymbol e|=2$，
$$
R=5+6K+e_j,\qquad e_j-R=-5-6K.
\tag{16}
$$
由真实输入 core 和单位盘上的二项式展开，得到完整式
$$
\boxed{\begin{aligned}
D_{L,j}(u)
={}&-\frac{\lambda^7\langle c_{L,j}\rangle^{du}}{168\Omega_p^2}
\sum_{\boldsymbol e}h_{\boldsymbol e}
\sum_{\boldsymbol r}
 (du)_R c_{L,j}^{-R}I_{e_j-R}(u)\\
&\hspace{12mm}\times
 \prod_{i\ne j}
 \frac{\kappa^{r_i}c_{L,i}^{\,r_i-e_i}\mu_{r_i}}
      {(r_i-e_i)!}.
\end{aligned}}
\tag{17}
$$
若某个深输入单项式指数超过 $r_i$，该项不出现。
公式保留了权中深输入的 $\kappa^{e_i}$；它们与展开的
$\kappa^{r_i-e_i}$ 一起正好给 $\kappa^{r_i}$。

所有 $R\ge5$，所以 $D_{L,j}(0)=0$。在 (17) 求导，只需将
$(du)_R$ 换成 $d(-1)^{R-1}(R-1)!$，并把 $I_{e_j-R}(u)$
换成原值 $I_{-5-6K}$。**因此整条中央式只含固定原负矩族的值，
没有负矩导数或任何参考斜率。**

分母满足
$$
\sum_{i\ne j}v_p((r_i-e_i)!)
\le\sum_{i\ne j}v_p(r_i!)
\le\frac{6K}{p-1}.
$$
与 §2.1 相同，$K\ge1$ 的完整尾属于
$p^{13}\mathcal O\langle u\rangle$，并允许逐项求导。
这付清了高权负族的整个尾，而非只留下第一个负矩。

### 4.1 八种真实单位选择的准确首系数

令 $D_L=\sum_{j=1}^8D_{L,j}$。
取全部七个 $r_i=1$，权中的深变量平方项不贡献首层。
其余平方或交叉项必须连同当前真实单位位置一起相加。
完整结果为
$$
\boxed{
D_L'(0)=d\,t_p^7\Omega_p^5 C_LI_{-5}
                           \pmod{p^{13}\mathcal O},}
\tag{18}
$$
$$
\boxed{C_A=\frac{1333}{36},\qquad
C_B=\frac{229812977}{112500}.}
\tag{19}
$$
一个不依赖逐位置列举的核验如下。设 $x=u_L^2,y=v_L^2$，
$D_0=845/864$ 为共同四尺度的逆六次幂之和，则
$$
C_L=\frac1{14}
\left\{1920\left(\frac y{x^3}-\frac x{y^3}\right)
 +96\left(\frac1{x^2}-\frac1{y^2}\right)
 +48(x-y)D_0\right\}.
\tag{20}
$$
代入 $(x,y)=(4,-3)$ 或 $(25/4,-3/4)$ 得 (19)。
生产证书还独立按 (17) 的八个真实单位位置逐一求值，核对 (20)。

特别，两份系数之差为
$$
\boxed{\eta=C_B-C_A=\frac{6267982}{3125}
              =\frac{2\cdot7^3\cdot9137}{5^5}.}
\tag{21}
$$
$9137$ 是素数（试除至 $95$ 即证明），且 $9137\equiv2\pmod3$。
所以 $\eta$ 对所有当前普通 $p>7$ 都为单位。
这避免了单独 $C_A$ 在普通素数 $31,43$ 处出现的首系数损失。

## 5. 两个真实多单位域之差与完整目标

对六核或任一二次核，将输出为单位的域分成“恰一个输入为单位”和
“至少两个输入为单位”。全部输入在 $p$ 内时输出不为单位，故这是穷尽分割。
分别记其后者的完整函数为 $N_6(u),N_A(u),N_B(u)$。准确有
$$
\boxed{J_S(u)=D_6(u)+N_6(u)
             =D_A(u)+N_A(u)=D_B(u)+N_B(u).}
\tag{22}
$$
每个 $N_L$ 仍带其自身的实际条件
$\sum_i c_{L,i}x_i\in\mathbf Z_p^\times$；没有把它们换成共同的抽象单位域。
由 (22)，得到真正完整的差域身份
$$
\boxed{N_A'(0)-N_B'(0)=D_B'(0)-D_A'(0).}
\tag{23}
$$
右端完全由 (17) 的同一个原负矩族给出，没有 $J_S'$ 或参考斜率的剩余项。
其首层为
$$
\boxed{
N_A'(0)-N_B'(0)
=d\,t_p^7\Omega_p^5\eta I_{-5}
                              \pmod{p^{13}\mathcal O}.}
\tag{24}
$$
同样六核与二次核的差是
$$
N_6'(0)-N_L'(0)=D_L'(0)-D_6'(0),
\tag{25}
$$
右端由 (10)、(17) 完整支付。式 (24) 是实际输入域的非齐次负矩关系，
不是把共用的 $\nu_S$ 相同误解为按单位输入个数分层后仍相同。

例如若 $v_p(I_{-5})<6$，则 (21)、(24) 给出这个指定差域的准确赋值
$$v_p(N_A'(0)-N_B'(0))=7+v_p(I_{-5}).$$
本文没有假定这一条件成立。即使它成立，也不意味着原 $J_S'(0)$ 非零：
原中央零只准确强迫
$$N_L'(0)=-D_L'(0),$$
并不分别强迫这两项为零。式 (22) 始终保留这份原目标约束。

## 6. 原负族的算术接口和一个已付单位输入

R332 已把这里的 $I_{-5}$ 接到同一原 Soulé 单位类的实际局部对数，
并保留 full 与 primitive 的二处 Euler 常数。其固定非零未被预支。
(10)、(17)、(23) 可直接使用那份算术规范，不引入新的 period 或未知斜率。

另一方面，整个负族不可能都在模 $p$ 下消失。
令 $h=(p-1)/6$，则在单位上 Fermat 给
$$
I_{1-6h}(\sigma)\equiv
\int_{\mathbf Z_p^\times}x\,d\nu(x)
=\Omega_p\left(1-\varepsilon^3\frac{\pi}{\bar\pi^2}\right)
\not\equiv0\pmod p.
\tag{26}
$$
这里 $1-6h=-5-6(h-1)$，确实属于同一原负族。
这是一个真实测度单位输入；但其权随 $p$ 变化。
它不自动说明固定 $I_{-5}$ 非零，也不把 (17) 的不同系数逐一分离。

后续若由真正四 sigma 加法或原域运输得到对 (22) 多单位部分的独立控制，
则 (23)、(26) 给出可用于比较的完整算术右端。
仅在同一单位域中交换相同 sigma 输入，仍只是齐次对称；
跨越不同输出单位域的边界必须继续保留。

## 7. 证书与依赖

脚本 check-jzero-six-sigma-and-two-quadratic-negative-family.py 及同名 JSON
核定全部六尺度相位、两实际二次参数对、首项、原六单位首系数、
两种二次核每一个真实单位位置、独立闭式 (20)、差系数及固定整数的素性。
全负族与尾由正文 (9)、(17) 证明，证书没有扫描目标素数。

- [R297：实际来源及 CM7 因式](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)。
- [R316：原 sigma 全 core](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)。
- [R327：单 sigma 二次核与原目标的完整传播](R327-original-single-sigma-quadratic-kernel-and-contracting-reconstruction.md)。
- [R330：原七八核与全部六重差分](R330-original-target-seven-eight-carry-and-sixfold-central-difference.md)。
- [R332：固定负矩的实际 Soulé 类及原局部规范](R332-fixed-negative-original-moments-actual-soule-classes-and-reflected-root-signs.md)。

