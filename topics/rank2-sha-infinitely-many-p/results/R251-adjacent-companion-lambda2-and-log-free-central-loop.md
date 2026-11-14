# R251 — 新相邻权伴随、原 E34 的实际投影与无对数中央回路

日期：2026-11-13。**状态：以下半周期运输、完整相邻权空间、真实 CM5 矩阵、R245 伴随的非零 $\lambda^2$ 分量、无对数全纯差及完整中央恒等式已证明。尚未把这些新行的零条件化为 R246 两个已知对数的代数相依。**

本篇接续 [R245](R245-third-rank2-full-mellin-and-cm17-log-bridge.md)、
[R246](R246-third-dyadic-bidirectional-cm17-and-complete-central-bridge.md) 和
[R248](R248-ray17-conjugate-trace-and-original-yang-projections.md)。
新输入直接使用 R245 的同一个 $C_*$，没有另选一个形式相似的伴随。

令 $B=A_{34}$、$H=A_{136}$，保留三曲线的首项一归一。
本篇构造固定线性算子 $\mathscr B$ 和一个固定、全局全纯、没有对数的伴随
$C_\circ$，使
$$
\boxed{
\mathscr B(C_\circ)=
\frac{128i\kappa_4}{5}\eta_\circ\,B(2z),\qquad
\eta_\circ=
\frac{822757710852163565}{43479138997811252736}\ne0.
}
\tag{1}
$$
同时 $C_\circ$ 的协变二阶导数位于原 $H,S_{2312}$ 和 CM17 反对称参考的
三维实际空间。因此 (1) 是两个已付原图之间的真实接口。
末节将两个方向的全部交换差、质量和移权写入同一个完整 Mellin 式。

## 1. 固定记号和真实相邻权空间

仍在 $E_0:y^2=x^3-x$、$dz=dx/(2y)$ 上，置
$$
U=x^2,\quad S_8=-y\vartheta\sigma^3,\quad
F=S_8^{17},\quad W=-y\vartheta\sigma^{67},\quad
D(U)=U^8(U-1)^8.
$$
于是 $F=WD$，原新截面为 $H=WP_H(U)$。
这里的 $W$ 是 theta 截面；末节的连接量另记 $W_F=zF_2'/F_2$。

同一个 degree-$68$、twist-$T_0$ 线丛中，两个准确空间是
$$
\mathcal V_+=\{WP(U):\deg P\le16\},\qquad
\boxed{\mathcal V_-=\{(W/x)P(U):\deg P\le16\}.}
\tag{2}
$$
它们的全局 $i$ 特征分别为 $+1,-1$。
第二个空间的每个截面在原点至少二阶，其 $z^2$ 系数恰是 $[U^{16}]P$。

说明 (2) 的完备性。任一偶截面除以 $W$ 后属于 $\overline{\mathbb Q}(x)$。
在 $T_+,T_-$，该商至多允许一阶局部极点；而 $x\mp1$ 的局部零阶为二，
所以偶有理商不能有这种极点。在 $T_0$，$W$ 有二阶零，因此至多允许
$1/x$ 的极点。在无穷远点的次数界为六十八；$i$ 特征为 $-1$ 时，
结果准确是 $P(x^2)/x$，$\deg P\le16$。
这些十七个截面线性独立，所以给出整个相邻权空间。

原有理伴随正位于此空间：
$$
C_R=F\frac{xR(U)}{U^8(U-1)^7}
    =\frac W x\,U(U-1)R(U),\qquad\deg R\le14.
\tag{3}
$$
它不是新变量中的任意代表。

## 2. 真实半周期同时控制有理部分和对数

取 $T_0=(1+i)\Omega_0/2$，在每个实际次数使用与乘积相容的同一规范
Mumford 平移，统一记为 $\mathcal J_0$。下式第一行作用于 degree-$4$
来源，其余截面式作用于 degree-$68$。加法公式给
$$
x(z-T_0)=-1/x(z),\qquad y(z-T_0)=y(z)/x(z)^2,
$$
$$
r(z)=\frac{x(z)-1}{x(z)+1},\qquad r(z-T_0)=-r(z)^{-1}.
\tag{4}
$$
包括完整 Gaussian 常数的准确截面等式是
$$
\boxed{\begin{aligned}
\mathcal J_0 S_8&=-iS_8/x,\
\mathcal J_0(WP(U))&=-i\frac W x\,U^{16}P(1/U),\
\mathcal J_0((W/x)P(U))&=iW\,U^{16}P(1/U).
\end{aligned}}
\tag{5}
$$
第一式可由原十六格直接校准：在 degree-$16$ 的基础尺度，
$T_0/2$ 的 lift 是 $-Z_0^{-4}X_0^4$，把 R239 的 $v$ 送到 $iw$，其中
$$
w=(0,t_0,0,-1,0,1,0,-t_0,0,-t_0,0,1,0,-1,0,t_0).
\tag{6}
$$
确切地，把 R246 四项算子改为
$$
\mathcal R_w=\frac{-i}{1+\zeta}
 (ZX-\zeta Z^{-1}X-\zeta ZX^{-1}+Z^{-1}X^{-1})
$$
就有 $\mathcal R_wv_0=w$。
在基础 degree-$16$ 尺度，其 Gaussian 截面是
$-\rho S_8(2z)/x(2z)$：R246 同一单项四挠 theta 的二阶系数为
$-i\,2^{-3/8}/4$，四项相加准确给 $-4\rho z^2$，
而 $S_8(2z)/x(2z)=4z^2+\cdots$。
亦可用 $\sigma(T_0)^4=-e^\pi$ 及 theta 自动因子直接得到 (5) 第一式。
另外两式由 $F=S_8^{17}=WD$ 和 (4) 得到，因而全部相位确定。
在本篇的 twist 空间上 $\mathcal J_0^2=1$。

标准 $p$ 进对数满足 $\log_p(-1)=0$，故 $L=\log r$ 准确变为 $-L$。
因此
$$
\mathcal J_0(FL)=iF x^{-17}L.
\tag{7}
$$
本次平移没有引入新的不明对数常数。

需要注意新的连接在原点有极：
$$
\mathcal J_0F=-iF x^{-17},\qquad
\operatorname{ord}_O(Fx^{-17})=34.
\tag{8}
$$
例如对 $\mathcal J_0C_*\in z^4\overline{\mathbb Q}[[z^4]]$，
先除输出的 $z^2$ 再作中央 Mellin 时，两个 Euler 因子是
$E-31,E-30$，其常数乘积为 $930$；不能当成原点正则连接的
$E+3,E+4$。
这一事实也由 R245 算子 $\mathscr L$ 的常数系数 $930$ 核对。

## 3. 同一原 CM5 迹及准确反序共轭

令 $\pi=2+i,\bar\pi=2-i$，沿用 R248 的
$$
q_\pi(U)=U-(1-2i),\quad k_\pi(U)=\pi U-i,
$$
以及 $c_\pi(U)$，由
$S_8(\pi z)=-y\vartheta\sigma^{19}c_\pi(U)$ 准确定义；共轭方向亦然。

在 (2) 两个空间上使用同一个真实几何算子
$\mathscr M=[\pi]_*[\bar\pi]^*$，分别记其矩阵为
$\mathscr M_+,\mathscr M_-$。
在五次纤维
$$
Uq_\pi(U)^4-tk_\pi(U)^4=0,
\qquad v=\frac{Uq_{\bar\pi}(U)^4}{k_{\bar\pi}(U)^4},
$$
上，相邻权的完整公式是
$$
\boxed{
(\mathscr M_-P)(t)=D(t)\operatorname{Tr}\left[
 \left(\frac{c_{\bar\pi}(U)}{c_\pi(U)}\right)^{17}
 \frac{q_\pi(U)^2k_{\bar\pi}(U)^2}
      {k_\pi(U)^2q_{\bar\pi}(U)^2}
 \frac{P(v)}{D(v)}\right].
}
\tag{9}
$$
新增的中间因子就是 $x(\pi z)/x(\bar\pi z)$；漏掉它会回到错误的正权矩阵。
迹包括所有分支及重数。

令 $\mathfrak R(P)=U^{16}P(1/U)$。准确计算给
$$
\boxed{\mathscr M_-=\mathfrak R\mathscr M_+\mathfrak R.}
\tag{10}
$$
这也完整核定 (5) 与 CM5 迹的相位相容，而非仅猜测它们交换。
证明可直接在 (9) 代入 (4)，或者用已证次数界，在十七个准确有理纤维
求出两个完整矩阵。证书另核一个未用于确定的纤维。

置 $\mathscr N_-=\mathscr M_-/\pi$。则
$$
\mathscr N_-^{16}=1,\qquad
\det(X-\mathscr N_-)=(X-1)(X^{16}-1).
\tag{11}
$$
在这十七维全纯空间上，准确的 $\lambda^2$ 投影是
$$
\boxed{\mathcal E_2^-=\frac1{16}\sum_{j=0}^{15}(-1)^j\mathscr N_-^j.}
\tag{12}
$$
正权空间的对应投影记为 $\mathcal E_2^+$。
式 (12) 是整个实际 torus 投影，已经杀掉其他十五个特征值；
不能只对前四个幂作平均后保留额外角色。

## 4. 三个真实相邻权来源及双向 dyadic 常数

设 R248 的实际中心一多项式为 $P_2,P_3$，分别对应
$S_{2312},S_{39304}$。准确定义
$$
\begin{aligned}
P_1^-&=-55\mathfrak R(P_H),\\
P_2^-&=\mathfrak R(P_2)/25,\\
P_3^-&=\mathfrak R(P_3)/13,
\qquad H_k^-=(W/x)P_k^-.
\end{aligned}
\tag{13}
$$
三者的 $z^2$ 系数均为一，且
$\mathscr M_-H_k^-=\pi i^kH_k^-$。
这些是相同三条曲线的真实 $m\equiv2\pmod4$ 行。
它们不是原 $m\equiv0$ 中央行；下节会用准确运输回到原 E34。

两个相邻 CM17 截面为
$$
S_8(\alpha_\pm z)/x(\alpha_\pm z)
=\frac W x P_\pm^-(U),\qquad
P_\pm^-=-\mathfrak R(P_\pm^+).
$$
在 R248 的 division 记号中也准确有
$P_\pm^-=D_{\alpha_\pm}K_{\alpha_\pm}^2$；其 $z^2$ 系数是
$\alpha_\pm^2$，不可归一后忘掉。

现在全体作 $[2]$ 拉回。令 $\mathcal J$ 为 degree-$272$ 的
$T_0/2$ 平移，并用 R246 的 $\mathcal U,\mathcal V$ 定义
$$
\boxed{\mathcal U_w=-i\mathcal J\mathcal U,
       \qquad\mathcal V_w=i\mathcal V\mathcal J.}
\tag{14}
$$
它们在旧 $v_0$ 与真实 $w$ 块之间互逆。
在原十六格，$I_2w=-w,Gw=iw$，由 (6) 逐项可核；
所以所有 dyadic 特征与原实际权一致。

由 R246 五块表与 (5)，得到

| 旧来源 | $\mathcal U_w$ 的像 |
|---|---|
| $\vartheta(4\alpha_+z)$ | $S_8(2\alpha_+z)/x(2\alpha_+z)$ |
| $\vartheta(4\alpha_-z)$ | $-S_8(2\alpha_-z)/x(2\alpha_-z)$ |
| $A_{17}(4z)$ | $-2iH_1^-(2z)/5$ |
| $S_{289}(2z)$ | $25iH_2^-(2z)/2$ |
| $S_{4913}(2z)$ | $-13iH_3^-(2z)/2$ |

定义 $Q_{+,w}=Q_{+,0}\mathcal V_w$，其中 $Q_{+,0}$ 仍是 R231/R246
的原八项算子。特别有
$$
\boxed{Q_{+,w}H_2^-(2z)=\frac{128i\kappa_4}{5}B(2z).}
\tag{15}
$$
另两行准确为
$Q_{+,w}H_1^-(2z)=-i\kappa_4S_{68}(2z)/2$ 和
$Q_{+,w}H_3^-(2z)=-2i\kappa_4S_{19652}(2z)/13$。
全部系数在 $p>19$ 都是单位；后续伴随分量系数只再排除固定有限集。

## 5. R245 原伴随的非零 $\lambda^2$ 分量

R245 的原伴随为
$$
C_*=C_{R_*}-\frac{\gamma_*}{8}FL,
\qquad \gamma_*=
\frac{402182437912192}{106525601325},
\qquad\nabla_8^2C_*=H-aK_I,
$$
$$
\nabla_8=\partial_z-F'/F,\qquad
a=-\frac{14548243}{4370281080}.
$$
使用 (3) 的原多项式 $U(U-1)R_*$，而非任意同余代表，(9)–(12) 给
$$
\boxed{
\mathcal E_2^-C_{R_*}=\eta_*H_2^-,\qquad
\eta_*=-\frac{2365009727546525379547}{30963292372771799040}\ne0.
}
\tag{16}
$$
其余三个 quartic 系数和两个 CM 系数都保存在证书。
十二个额外角色的总项也非零；(16) 用的是实际投影，未删掉它们再声称
$C_{R_*}$ 本来就在五维块。

对对数对象，按 (12) 的**固定有限算子公式**定义
$$
\mathcal L_2=\mathcal E_2^-(FL).
$$
它可以通过真实有限平坦迹作用于局部对数 germ。
这里不把 (11) 在全纯十七维空间的关系无证延长到含对数的无限空间，
也不声称 (12) 在后者仍为幂等。
线性性足以给
$$
\boxed{\mathcal E_2^-C_*=\eta_*H_2^--\frac{\gamma_*}{8}\mathcal L_2.}
\tag{17}
$$

## 6. 与实际第二伴随消去同一个对数

下面的第二伴随与 R250 使用的对象一致，其定义也可独立从 R245 的
固定矩阵给出。令
$$
a_2=\frac{8235327}{3310819},\qquad
\gamma_2=-\frac{471121690512128}{645609705}.
$$
取唯一次数至多十四的 $R_2$，满足
$$
P_2-a_2P_I=\mathscr LR_2+\frac{\gamma_2}{2}D+\gamma_2D/(U-1),
\tag{18}
$$
其中 R245 的实际算子为
$$
\mathscr L=16U^2(U-1)^2\partial_U^2
-12U(U-1)(37U-19)\partial_U+(3306U^2-3396U+930).
$$
R245 已证的十七列行列式非零；本篇证书在同一矩阵中准确解出 (18)，
并保留 $R_2$ 的全部十五项系数。
置
$$
C_2=C_{R_2}-\frac{\gamma_2}{8}FL.
$$
则
$$
\nabla_8^2C_2=S_{2312}-a_2K_I,
\qquad C_2=\tfrac12z^2+O(z^6).
\tag{19}
$$
同一实际投影给
$$
\mathcal E_2^-C_{R_2}=\eta_2H_2^-,\qquad
\eta_2=\frac{461734403779915958623}{31276052901789696}.
\tag{20}
$$

现在取固定有理数
$$
\tau=\frac{\gamma_2}{\gamma_*}
=-\frac{607305304175790}{3142050296189}.
$$
定义
$$
\boxed{C_\circ=C_2-\tau C_*=C_{R_2-\tau R_*}.}
\tag{21}
$$
两项对数完全消去。$C_\circ$ 是全局全纯原 theta 截面，在原点首项
$z^2/2$，在 $T_0$ 至少四阶、在 $T_\pm$ 至少三阶；这些实际零阶保证
其协变二阶导数全局正则。
完整恒等式为
$$
\boxed{
\nabla_8^2C_\circ
=S_{2312}-\tau H-(a_2-\tau a)K_I.
}
\tag{22}
$$
与此同时，(16)、(20) 给
$$
\mathcal E_2^-C_\circ=\eta_\circ H_2^-,\qquad
\eta_\circ=\eta_2-\tau\eta_*
=\frac{822757710852163565}{43479138997811252736}\ne0.
\tag{23}
$$
系数虽比两项小得多，却准确非零。
本篇完整精确证书同时核对 (18)、(22)、(23)，没有从小数取消认定它。

## 7. 三个完整中央函数之间的真实关系

对任一上述伴随定义固定算子
$$
\mathscr B(C)=Q_{+,w}\bigl((\mathcal E_2^-C)(2z)\bigr),
\qquad \mathscr L_B=\mathscr B(FL).
\tag{24}
$$
置 $k_B=128i\kappa_4/5$。
由 (15)、(17)、(20) 直接得到整条 germ 的准确等式
$$
\begin{aligned}
\mathscr B(C_*)&=k_B\eta_*B(2z)-\frac{\gamma_*}{8}\mathscr L_B,\\
\mathscr B(C_2)&=k_B\eta_2B(2z)-\frac{\gamma_2}{8}\mathscr L_B,\\
\mathscr B(C_\circ)&=k_B\eta_\circ B(2z).
\end{aligned}
\tag{25}
$$
第三式就是 (1)。

固定目标惰性 $p$，在 degree-$272$ 的同一个 gauge $c=272c_0$ 上，记
$$
\mathfrak b_*(u)=\mathcal J_c(\mathscr B(C_*);u),\quad
\mathfrak b_2(u)=\mathcal J_c(\mathscr B(C_2);u),\quad
\ell_B(u)=\mathcal J_c(\mathscr L_B;u),\qquad q_2=2^{p-1}.
$$
则完整解析式为
$$
\boxed{\begin{aligned}
\mathfrak b_*+\frac{\gamma_*}{8}\ell_B&=k_B\eta_*q_2^uJ_{34}(u),\\
\mathfrak b_2+\frac{\gamma_2}{8}\ell_B&=k_B\eta_2q_2^uJ_{34}(u),\\
\mathfrak b_2-\tau\mathfrak b_*&=k_B\eta_\circ q_2^uJ_{34}(u).
\end{aligned}}
\tag{26}
$$
所有对数常数、质量及完整尾都保留在 $\ell_B$ 中。
因为 $J_{34}(0)=0$，实际 $J_{34}'(0)=0$ 因而给出新的准确相依
$$
\boxed{\mathfrak b_2'(0)=\tau\mathfrak b_*'(0),\qquad
\frac{\mathfrak b_*'(0)}{\gamma_*}
=\frac{\mathfrak b_2'(0)}{\gamma_2}
=-\frac18\ell_B'(0).}
\tag{27}
$$
反过来，(26) 第三行和 $\eta_\circ\ne0$ 说明第一条导数相依也推出
$J_{34}'(0)=0$。所以它精确地保留了原 E34 的完整条件。

## 8. 无对数伴随的第二个真实输出及其全部转置

定义另一个固定算子
$$
\mathscr D(C)=Q_{+,v}\bigl((\mathcal E_2^+\nabla_8^2C)(2z)\bigr),
$$
其中 $Q_{+,v}$ 是 R246 的原正权 dyadic 算子。
由 (19)、(22) 及原三种不同十七角色，准确有
$$
\mathscr D(C_*)=0,\qquad
\mathscr D(C_2)=\mathscr D(C_\circ)=-640i\kappa_4B(2z).
\tag{28}
$$
结合 (1)，得到同一固定全纯伴随的真实二阶差分关系
$$
\boxed{
\mathscr D(C_\circ)=-\frac{25}{\eta_\circ}\mathscr B(C_\circ).
}
\tag{29}
$$
本式两边没有对数。常数非零且独立于目标素数。

完整 Mellin 转置不能只保留 (29) 的裸二阶部分，具体如下。
把 $\mathcal O=Q_{+,v}\mathcal E_2^+$ 写成实际有限 correspondence 的分支和
$\sum_\nu b_\nu\mathcal T_\nu$。
其中每个分支覆盖 $z\mapsto r_\nu z+s_\nu$；来自 $j$ 次 CM5 的
$r_\nu=\bar\pi^j/\pi^j$，且
$$
\mathscr N^j=\pi^{-j}[\pi^j]_*[\bar\pi^j]^*,\qquad 0\le j\le15.
$$
两端固定 dyadic lifts 和全部线丛 frame 也包含在 $\mathcal T_\nu$ 中。
这些是有限、固定、prime-to-$p$ 的实际 correspondence，未选择随 $p$ 变化的代表。

记 $C^{[2]}(z)=C(2z)$、$F_2=F(2z)$、$\nabla_2=\partial-F_2'/F_2$，并定义
$$
a_\nu=\partial_z\log\frac{\mathcal T_\nu F_2}{F_2}.
$$
链式法则给
$$
\nabla_2\mathcal T_\nu
=r_\nu\mathcal T_\nu\nabla_2+a_\nu\mathcal T_\nu,
$$
$$
\mathcal T_\nu\nabla_2^2C^{[2]}
=r_\nu^{-2}\left\{
\nabla_2^2\mathcal T_\nu C^{[2]}
-2a_\nu\nabla_2\mathcal T_\nu C^{[2]}
+(a_\nu^2-a_\nu')\mathcal T_\nu C^{[2]}\right\}.
\tag{30}
$$
因此置
$$
\widetilde C=\sum_\nu b_\nu r_\nu^{-2}\mathcal T_\nu C^{[2]},
$$
$$
\mathscr E_C=\sum_\nu b_\nu r_\nu^{-2}
\left\{-2a_\nu\nabla_2\mathcal T_\nu C^{[2]}
+(a_\nu^2-a_\nu')\mathcal T_\nu C^{[2]}\right\},
$$
便有
$$
\boxed{\mathscr D(C)=\frac14(\nabla_2^2\widetilde C+\mathscr E_C).}
\tag{31}
$$
外面的 $1/4$ 来自两个真实 $[2]$ 导数，不能省略。
各 $j$ 的 trace 及 dyadic 算子与全局 $i$ 交换，所以
$\widetilde C$ 有特征 $-1$，$g=z^{-2}\widetilde C$ 在原点正则。

令 $d=p+1$，$W_F=zF_2'/F_2$、$W_0=W_F-dcz^d$、$E=z\partial_z$，并记
$$
f=\mathcal J_c(g),\qquad
g_1=\mathcal J_c(W_0g),\qquad
h=\mathcal J_c((W_0^2+EW_0-W_0)g).
$$
于是 (31) 的全体 $u$ 形式是
$$
\boxed{\begin{aligned}
4\mathcal J_c(\mathscr D(C);u)={}&(du+1)(du+2)f(u)
 +du(d-3-2du)f(u-1)+d^2u(u-1)f(u-2)\\
&-2(du+1)g_1(u)+2dug_1(u-1)+h(u)
 +\mathcal J_c(\mathscr E_C;u).
\end{aligned}}
\tag{32}
$$
求导时还须保留 $3df(0)$；完整公式即 R246 (25) 的右侧，换成这里的
实际 $f,g_1,h,\mathscr E_C$。
在 (29) 中使用 $C=C_\circ$ 后，两侧只是全纯固定 theta 来源；
使用 $C_*,C_2$ 时，(30) 始终保留实际对数分支。
固定 prime-to-$p$ 平移后的线性对数首项按 R246 的 $p^{1/2}$ Gauss 成本支付；
全部连接差、固定阶导数和半径损失亦按 (30) 保留，故 (26)、(32) 的完整尾收敛。

## 9. 与原两条非零对数残差的准确关系

R246 的 $\Phi_*',\widehat\Psi_p'$ 在原 E17、E136 双零时分别等于
非零的 norm-one-$17$ 与 norm-$17$ 对数，并在代数系数上线性无关。
本篇给出原 E34 完整零条件的实际相依 (27)，而非另一个有限素数测试。
这两组泛函仍然不同：$\mathfrak b_*$ 使用 $Q_{+,w}\mathcal E_2^-$，
$\Phi_*$ 使用 $\nabla_8^2$，而 R246 的转置使用 $\mathcal V\nabla_8^2$。
它们之间所有交换差已明确列在 (30)–(32)，不能从有限矩阵可逆性删除。
因此 (27) 尚未成为 R246 两个独立对数之间的代数相依；这正是下一项
应在原固定系统中计算的条件。

## 精确证书与来源

- [脚本](../scripts/check-third-adjacent-companion-lambda2.py) 与
  [完整输出](../scripts/check-third-adjacent-companion-lambda2.json)
  给出 (9) 的十七列矩阵、(10) 的完整等式、三个实际相邻权多项式、
  $R_2,R_2-\tau R_*$ 的全部系数、两个 CM 分量及十二角色余项。
  在 $\mathbb Q(i)$ 及 $\mathbb Q$ 中的三十六项检验全部通过；
  没有数值识别、目标素数扫描或未付的逐权比例。
- 原实际算子和有限向量：R239、R246；全纯正权 CM5 矩阵：R248。
- 原协变算子、二挠除子对数及完整 Mellin：R245；第二伴随同 R250。
- 曲线身份始终用原 Yang theta 图，文献规范与 R246/R248 相同。
