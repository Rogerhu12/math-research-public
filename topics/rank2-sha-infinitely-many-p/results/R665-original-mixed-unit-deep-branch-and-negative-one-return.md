# R665 — 原两混合单位行的 L 深支、完整二阶系数与已知负一矩

日期：2026-11-15。**状态：已证明。**

本篇继续 R662 的同两个真实混合单位观察 $\Theta_\pm$。
限制原 L 输入深以后，完整角型迫原六次测试只留下其 L 二阶项；
整条深支差因而分成一个实际四输入系数与同一 S5 pair 的负矩级数。
这个四输入系数也已由原冻结右逆付成单位尺度。
调用 R655 的原 $\sigma^5$ 负一非零，得到该真实深支的准确非零值层。

全文保留原 L 浅补域和原 T 外部项，三者在同一式中联立。
不由深支非零推整个中央非零，也不另换测试或来源。

## 1. 原完整 pair 与两个混合单位观察

保持 R653/R659/R662 的原 $b=17$、$\lambda,\kappa,\Omega$、
同一个 R594 测试、$N\in4\mathbf Z_{\ge1}$ 和全部固定坏集。
不增加新的 ray 条件。原 whole odd5 核已由 R655 准确定为
$\beta=-\lambda$，且同一未缩放来源满足
$$
I_{\Sigma,-1}:=\int_{Q\ {\rm unit}}Q^{-1}\,d\nu_{\Sigma_5}(Q)\ne0,
\qquad\Sigma_5=\sigma^5 .
\tag{1}
$$
这是原 E80/BDP 桥付出的非零，不是用正五矩代负一。

记
$$
\mu_0=\nu_4\otimes\nu_{\rm pair},\qquad
\nu_4=-\mathcal P_{6,C}\nu_\sigma^{\otimes4}/84,
$$
$$
\nu_{\rm pair}\ \longleftrightarrow\
\sigma(q+2l)\sigma(2q-l).
$$
原整个 pair 是
$$
\begin{aligned}
\nu_{\rm pair}={}&
\nu_{F_{12}}\otimes\nu_{D_5}
-\nu_{D_5}\otimes\nu_{F_{12}}+3\nu_{Z_5}\otimes\nu_{Z_5}\\
&+6b(\nu_{X_5}\otimes\nu_{\Sigma_5}
                    +\nu_{\Sigma_5}\otimes\nu_{X_5}),
\end{aligned}
\tag{2}
$$
其中 Q/L 次序固定，
$D_5=-xy\sigma^5,\ Z_5=x^2\sigma^5,\ X_5=x\sigma^5$、
$F_{12}=\sigma(z)\sigma(2z)$，各原规范不变。

R662 的两个实际行是
$$
\Theta_\epsilon^{[1]}=
\int_{\mathcal G_{0,N}}p_{0,N}\,
 1_{\{b_LL+\epsilon b_YQ\ {\rm unit}\}}
 \log\langle b_LL+\epsilon b_YQ\rangle\,d\mu_0,
\qquad\epsilon=\pm1,
\tag{3}
$$
$$
b_L=(2+12\omega)/5,\quad b_Y=(20+3\omega)/17,\quad h=b_L/b_Y .
$$
$b_L,b_Y,h$ 在当前 ray 上为单位：
其范数的额外因子仅 $31,349$，分别不满足原 $p\equiv7\bmod64$。
$\mathcal G_{0,N},p_{0,N}$ 就是 R653 的冻结门和完整权。

对每个 $n\ge N$，记 $\Theta_{\epsilon,n}^{[1]}$ 为 (3)
额外限制 $L\in p^n$ 的同一积分，置
$$
\Delta_{N,n}=\Theta_{+,n}^{[1]}-\Theta_{-,n}^{[1]}.
\tag{4}
$$

## 2. 原 L 深域的准确门、单位 cut 和角型

令
$$
D_4=\xi_1+\omega^2\xi_2-2\omega\xi_3,\quad
a=-(5+6\omega)/29,\quad g=3-2\omega,\quad \ell_0=-3\omega/5,
$$
$$
D_*=D_4-aA,\qquad E_*=D_*+14C,\qquad
G_*=13H_1+g(D_*+C).
\tag{5}
$$
原冻结三行准确为
$$
D_0=D_*+\ell_0L,\qquad E_0=E_*+\ell_0L,\qquad
G_0=G_*+g\ell_0L .
\tag{6}
$$
whole L 核给
$\mu_0|_{L\in p^n}=\beta^n(P_{L,\kappa^n})_*\mu_0$，
保持 Q 和四个原第一输入。

写 $t=\kappa^n$。因为 $n\ge N$，
(6) 的完整门准确成为
$$
\mathcal G_*=\{C\ {\rm unit},D_*\in p^N\}.
\tag{7}
$$
又因 $n\ge1$，
$b_LtL\pm b_YQ$ 单位准确等价于 Q 单位。
这些都是逐点域恒等，不以某条边际替换完整来源。

令
$$
X_*=(D_*/\kappa^N,E_*,G_*),\qquad
\mathcal V_N=\kappa^{-N}\partial_D+\partial_E+g\partial_G .
$$
整个 degree 六权在返回后的真实展开是
$$
\frac{\widehat P_p(X_*+\ell_0tL(\kappa^{-N},1,g))}{b\Omega^6}
=\sum_{j=0}^6 t^jL^j p_{j,N},
$$
$$
p_{j,N}=\frac{\ell_0^j}{j!\,b\Omega^6}
             (\mathcal V_N^j\widehat P_p)(X_*).
\tag{8}
$$
这些系数只依原四输入，特别独立于 Q、L。
其可能的 $\kappa^{-jN}$ 全部显示，不能当成单位系数省去。

两个 principal log 的常数准确相消：
$$
\log\langle b_YQ+b_LtL\rangle-
\log\langle-b_YQ+b_LtL\rangle
=2\sum_{\substack{k\ge1\\k\ {\rm odd}}}
       \frac{h^kt^kL^kQ^{-k}}k .
\tag{9}
$$
级数在 Q 单位上统一收敛，保整个 L 输入。

Q 的负 $k$ 矩只保角型 $-k\bmod6$。
(2) 的 pair 总角型为二，所以其 L 型为 $k+2\bmod6$。
L 的总正矩 $j+k$ 因而迫
$$
j\equiv2\pmod6.
$$
在 (8) 的全部七个次数 $0\le j\le6$ 中，**只有 $j=2$**。
这是整条级数的精确消去，不只检查首几项。

定义真正的四输入系数
$$
\boxed{J_N=\int_{\mathcal G_*}p_{2,N}\,d\nu_4.}
\tag{10}
$$
对 $F=\Sigma_5,X_5,Z_5$ 记
$$
I_{F,-k}=\int_{Q\ {\rm unit}}Q^{-k}\,d\nu_F,\qquad
M_{F,k+2}=\int L^{k+2}\,d\nu_F .
$$
前者保 Q 单位，后者是完整总矩，不能添 Euler 因子。
令
$$
\begin{aligned}
\mathscr H_p(t)={}&
6b\sum_{k\equiv1\ (6)}
 \frac{h^kt^k}{k}I_{\Sigma_5,-k}M_{X_5,k+2}\\
&+6b\sum_{k\equiv3\ (6)}
 \frac{h^kt^k}{k}I_{X_5,-k}M_{\Sigma_5,k+2}\\
&+3\sum_{k\equiv5\ (6)}
 \frac{h^kt^k}{k}I_{Z_5,-k}M_{Z_5,k+2},
\qquad k\ge1 .
\end{aligned}
\tag{11}
$$
于是得到同一原域的完整因子式
$$
\boxed{\Delta_{N,n}=2\beta^n\kappa^{2n}J_N\,
                         \mathscr H_p(\kappa^n).}
\tag{12}
$$
(11) 的其余负矩仍原样保留；没有给它们猜值。

## 3. 四输入系数的完整 whole 核与半特征

这里必须保两个实际细节：
$$
\boxed{\langle D_*,C\rangle=-1,\qquad
N(D_*)=143/29.}
\tag{13}
$$
因此 D 核会移动 C；也不能只用单个分支的 degree4147。
置
$$
C^\perp=C+\frac{29}{143}D_*,
\qquad N(C^\perp)=114/143,\qquad C^\perp\perp D_* .
\tag{14}
$$
一个完整四输入整正交框架为
$$
(87D_*,429C^\perp,A,R),\qquad
R=(-4-5\omega,\ 3,\ 1-\omega,\ 5+4\omega).
\tag{15}
$$
其度数、行列式为
$$
\boxed{(37323,146718,29,54),\qquad
\det(15)=3359070+1343628\omega.}
$$
$$
37323=3^2\cdot11\cdot13\cdot29,\qquad
146718=2\cdot3^3\cdot11\cdot13\cdot19.
\tag{16}
$$
附证书给完整六个 C 旋转后的所有行。
它们全部整，模二非零系数个数恒为 $(3,4,3,4)$。
所以整个 $\nu_4$ 严格在
$$
\mathcal S_{37323}^{\rm odd}\boxtimes\mathcal S_{146718}
 \boxtimes\mathcal S_{29}^{\rm odd}\boxtimes\mathcal S_{54}.
\tag{17}
$$
仅 $29D_*$ 在 $\zeta=-1$ 等 C 分支含 $1/\delta$；
(15) 的真实三倍覆盖不能省掉。
正交 Gaussian 和各轴完整半特征同时支付 (17)，没有 flat twist。

沿原 R488 代表直接取比值，完整中心同余为
$$
\boxed{
g_\pi\equiv1\pmod{74646},\qquad
g_\pi\equiv146719=1+146718\pmod{293436}.}
\tag{18}
$$
这些模数的全部条件已在旧 ray，不需要新细分。
第一项使 whole odd37323 核为标量 $\chi_D$；
第二项的完整 even Heisenberg 交织为恒等，使 whole146718
核为标量 $\eta$。下面支付绝对平方，未猜两个符号。

取 $\gamma_{79}=10+3\omega$。真实两 sigma 正交联合的两系数
$\delta,2\gamma_{79}$ 范数为 $3,316$，两轴总范数 $319$，
每轴一个 odd 系数。whole odd319 在当前 ray 为 scalar；
与两个原 sigma 同时深比较，得到该 scalar 的平方一。
再按 $3\gamma_{13}=12+3\omega$ 拉回，范数为 $117$，
且 $319\cdot117=37323$，故 $\chi_D^2=1$。

类似地，$\delta,\gamma_{19}=5+2\omega$ 的范数为 $3,19$。
其原两 sigma 联合在标准 even $\mathcal S_{22}\boxtimes\mathcal S_{22}$；
$g_\pi\equiv23=1+22\bmod44$ 给 scalar，其平方由同一原联合为一。
按
$$
3\delta\gamma_{13}\gamma_{19}=-12+75\omega,\qquad
N(-12+75\omega)=6669
$$
拉回，$22\cdot6669=146718$，得到 $\eta^2=1$。
所有拉回是普通单位，并严格与 p 深限制交换。

因此整个原 $\nu_4$ 有准确双核心
$$
\boxed{
\nu_4|_{D_*\in p^k}=(\chi_D\lambda)^k(P_{D_*,\kappa^k})_*\nu_4,\quad
\nu_4|_{C^\perp\in p^j}=(\eta\lambda)^j(P_{C^\perp,\kappa^j})_*\nu_4,
\quad \chi_D,\eta\in\{\pm1\}.}
\tag{19}
$$
这来自完整张量格，不是假设 D 核与 C 平均交换。
原 $N\in4\mathbf Z$ 使 $\chi_D^N=1$；未知 $\eta$ 保两种情况。

## 4. 原单位补域保留后的准确 Laurent 系数

在 $D_*$ 深域上，原 C 单位准确等价于 $C^\perp$ 单位。
记
$$
E_\perp=14C^\perp,\qquad
G_\perp=G_*-\frac{-789+526\omega}{143}D_*,
$$
$$
G_{00}=G_\perp-
       \left(-\frac{263}{38}+\frac{263}{57}\omega\right)C^\perp .
$$
完整回代是
$$
E_*=E_\perp-\frac{263}{143}D_*,
\qquad
G_*=G_\perp+\frac{-789+526\omega}{143}D_*,
\qquad
G_{00}=\left(\frac{13}{6}-\frac{13}{18}\omega\right)R .
\tag{20}
$$
用 (19) 先付真 D 深返回，再把 $C^\perp$ 单位拆为全域减深域，
得到 (10) 的准确有限四次矩公式。为同时保所有高层项，置
$t=\kappa^N$、$\mathcal D_t=\partial_D+t\partial_E+tg\partial_G$，
并以 $\mathfrak M_4(P)=\Omega^{-4}\int P\,d\nu_4$ 表示完整四次矩。
则
$$
\begin{aligned}
\frac{2b\Omega^2}{\ell_0^2}\lambda^{-N}\kappa^{2N}J_N
=\mathfrak M_4\bigl[&
(\mathcal D_t^2\widehat P_p)
  (D_*,E_\perp-\tfrac{263}{143}tD_*,
       G_\perp+\tfrac{-789+526\omega}{143}tD_*)\\
-\eta\lambda\,&(\mathcal D_t^2\widehat P_p)
  (D_*,\kappa E_\perp-\tfrac{263}{143}tD_*,
       G_{00}+\kappa(G_\perp-G_{00})
                 +\tfrac{-789+526\omega}{143}tD_*)\bigr].
\end{aligned}
\tag{21}
$$
微分是在显示的代入之前作；(21) 保全部实际 $\lambda,\kappa,t$
和原整右逆。第二行就是完整 C 单位补项，未删去。

R659(21)–(22) 已从同一 R594 原右逆得到
$$
\bar P_L=L^{-1}P_{-1}+P_0
-\frac{P_{-1}^{[0]}+LP_0^{[0]}}{1+L},
\qquad P^{[0]}=P(D,0,G).
\tag{22}
$$
此处 L 仅为形式变量，不是物理轴。
将 (21) 模 $p$，准确得到
$$
\boxed{
\frac{2b\Omega^2}{\ell_0^2}\lambda^{-N}\kappa^{2N}J_N
\equiv \frac{\mathscr P_\eta(\lambda)}
                  {\lambda(1+\lambda)}\pmod p ,
}
\tag{23}
$$
其中两个 $\mathscr P_{\pm1}\in K[L]$ 都为 degree 至多二的固定多项式。
明确地，令
$$
\begin{aligned}
a_-&=\mathfrak M_4((\partial_D^2P_{-1})(D_*,E_\perp,G_\perp)),\\
a_0&=\mathfrak M_4((\partial_D^2P_0)(D_*,E_\perp,G_\perp)),\\
a_-^0&=\mathfrak M_4((\partial_D^2P_{-1})(D_*,0,G_\perp)),\\
a_0^0&=\mathfrak M_4((\partial_D^2P_0)(D_*,0,G_\perp)),\\
b_-&=\mathfrak M_4((\partial_D^2P_{-1})(D_*,0,G_{00})),\\
b_0&=\mathfrak M_4((\partial_D^2P_0)(D_*,0,G_{00})).
\end{aligned}
$$
则
$$
\boxed{\mathscr P_\eta(L)=
a_-+(a_-+a_0-a_-^0-\eta b_-)L+(a_0-a_0^0-\eta b_0)L^2.}
\tag{24}
$$
六个固定矩和两条完整多项式都在附 JSON，未知符号没有被删掉。

原 $\nu_4$ 的整个最低四次生成函数是
$$
\frac1{42}(z_Zz_Q^2-z_Z^3)z_r,\qquad
z_Z=(z_1-z_3-2z_x)/6,\quad z_Q=(z_1+z_3)/2,\quad z_r=z_2 .
\tag{25}
$$
这是 R594 原六次函数去掉两个独立 sigma 线性因子后的准确式。
把 (20) 代入 (25)，逐单项式乘原阶乘，直接计算得到
$$
\boxed{
a_-=\frac{-885702640402936000276875600056127980453128800659519178770044
          -1265630629890465110326582590111290283671110894972293491439245\omega}
         {138234164900256144816527927695749460122797567082628229782080}\ne0.}
\tag{26}
$$
所以无论实际 $\eta=+1$ 还是 $-1$，完整 (24) 都不恒等为零。
其固定系数分母的一个公倍数是
$$
D_{665}=14929289809227663640185016191140941693262137244923848816464640.
\tag{27}
$$
正文没有从有限素数采样推非零；这是同一原右逆的特征零准确配对。

排除 (27)、原 $D_{594}$ 和全部固定坏集后，
对固定非零乘积 $\mathscr P_+(L)\mathscr P_-(L)$ 使用
[固定 CM 单位密度引理](../notes/2026-11-14-fixed-cm-polynomial-unit-density.md)。
在当前 ray 再删一个 $O(\sqrt X\log X)$ 的坏集，
两个实际多项式同时为单位；这与 R659 的相对密度一子族相交仍相对密度一。
由 (23)，得到同一个实际系数的准确结论
$$
\boxed{v_p(J_N)=-2N
\quad\text{对所有 }N\in4\mathbf Z_{\ge1}\text{ 同时成立}.}
\tag{28}
$$
多项式 (24) 与 N 无关；所有 N 的变化仅为已经显示的
$\lambda^N,\kappa^{-2N}$ 及模 $p$ 消失的 $\kappa^N$。
这里未把 p 依赖的 $I_{\Sigma,-1}$ 套入固定多项式引理。

## 5. 同一真实 L 深支的准确非消失

原 $X_5(z)=z^3+O(z^9)$，所以完整总矩
$M_{X_5,3}=6\Omega^3$。
(11) 的第一个系数因而准确为
$$
[t]\mathscr H_p(t)=36b\Omega^3h\,I_{\Sigma,-1}\ne0 .
\tag{29}
$$
其余原负矩保留在 (11)，但无需猜它们的值来比较尾项：
各单位负矩和各总正矩都整，故第 k 项的系数赋值至少
$-v_p(k)$。对每个 $n\ge1$、奇 $k\ge3$，
$kn-v_p(k)\ge3n$，于是
$$
\boxed{\mathscr H_p(\kappa^n)
=36b\Omega^3h\,I_{\Sigma,-1}\kappa^n+p^{3n}\mathcal O .}
\tag{30}
$$
没有宣称整个形式级数有整系数；分母 k 已完整计入。

结合 (12)、(28)：
$$
\boxed{
\Delta_{N,n}
=72b\Omega^3h\,J_N\beta^n\kappa^{3n}I_{\Sigma,-1}
       +J_Np^{5n}\mathcal O .
}
\tag{31}
$$
R655 已给 $I_{\Sigma,-1}\ne0$，其赋值有限。
因此在 (28) 的同一无限子族上，凡
$$
n\ge N,\qquad 2n>v_p(I_{\Sigma,-1}),
$$
都严格有
$$
\boxed{v_p(\Delta_{N,n})=3n-2N+v_p(I_{\Sigma,-1}).}
\tag{32}
$$
这是 (3) 的两个实际混合单位观察在同一 L 深域上的差，
不是把裸负一矩直接当成一个中央。

## 6. 全部 L 浅补域和原 T 外部的同一式

在原六输入上定义完整浅补域
$$
\begin{aligned}
\mathcal R_{N,n}=\int_{\mathcal G_{0,N},\,L\notin p^n}p_{0,N}
\{&
1_{\{b_LL+b_YQ\ {\rm unit}\}}\log\langle b_LL+b_YQ\rangle\\
-&1_{\{b_LL-b_YQ\ {\rm unit}\}}\log\langle b_LL-b_YQ\rangle\}\,d\mu_0 .
\end{aligned}
\tag{33}
$$
注意此处保两个原混合单位 cut，没有额外加 Q 单位或 L 单位。
准确的全域分解为
$$
\boxed{\Theta_+^{[1]}-\Theta_-^{[1]}
       =\Delta_{N,n}+\mathcal R_{N,n}.}
\tag{34}
$$

R662(23)–(26) 的原 T 外部是
$\{Y\in p^{r+m},A\notin p^{2r}\}$，带原完整 W 词及同一个 $q_N$。
若原 $J'_T=0$，令其两个正确归一的真实极限为
$\mathcal E_\epsilon$（$m=0,1$ 分别对应 $\epsilon=+1,-1$），则
$$
\mathcal E_\epsilon=-\Theta_\epsilon^{[1]}.
$$
所以本篇已知负一矩进入原完整算术关系的准确形式是
$$
\boxed{
\mathcal E_+-\mathcal E_-+\mathcal R_{N,n}
=-\Delta_{N,n}.
}
\tag{35}
$$
(32) 给右侧的准确非零赋值，因而也给左侧**完整补偿和**的赋值。
它没有迫 $\mathcal E_\epsilon$ 或 $\mathcal R_{N,n}$ 单独为零。
原 $J'_S=0$ 下的 R662 外部 log 质量三角项仍另按原式保留，
不能与 (35) 混为同一个测试。

相邻层也有一个无需新增来源的实际关系：
$$
\boxed{\mathcal R_{N,n+1}-\mathcal R_{N,n}
       =\Delta_{N,n}-\Delta_{N,n+1}.}
\tag{36}
$$
右侧就是同一原 L 环带的差，由 (31) 为
$$
72b\Omega^3hJ_N\beta^n\kappa^{3n}
 (1-\beta\kappa^3)I_{\Sigma,-1}+J_Np^{5n}\mathcal O .
\tag{37}
$$
因 $1-\beta\kappa^3$ 是单位，(32) 的条件下，
(36) 的准确赋值仍为 $3n-2N+v_p(I_{\Sigma,-1})$。
这记录浅补域随 n 的真实非零变化，而不是把它固定成零。

剩余问题是在 (35) 的同一个浅域和两个原 T 外部词之间支付附加关系。
(34)–(37) 已保持全部这些量，故本篇不以局部非零宣称主目标完成。

## 精确文件

- [check-r665-mixed-unit-negative-one-and-second-coefficient.js](../scripts/check-r665-mixed-unit-negative-one-and-second-coefficient.js)
- [check-r665-mixed-unit-negative-one-and-second-coefficient.json](../scripts/check-r665-mixed-unit-negative-one-and-second-coefficient.json)

脚本直接使用 R659 保存的原 R594 $P_{-1},P_0$，
不重求右逆、不更改测试。它精确给完整四输入框架、六分支半特征、
原中心同余、两绝对平方锚、全部四次矩和两个 $\eta$ 多项式。
原角型选择、全域因子、统一尾界与全补域身份由正文完整支付。
