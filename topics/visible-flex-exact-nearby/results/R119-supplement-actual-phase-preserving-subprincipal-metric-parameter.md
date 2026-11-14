# R119 续篇：实际保持主相位的第二度量参数及首低阶相位横截

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 在实际强尾的每个完整负分量中，增加一个不接触根的
明确径向 bump。两个实际参数对“全两射线主相位”和“严格内部首低阶
相位”的归一 Jacobian 有统一非zero下界，所有层同时成立：

$$
 \det D_{(\gamma_1,\gamma_2)}
       (\sqrt B\,\Theta,\mathfrak b/\sqrt B)>2^{-11}.
                                                               \tag{P.1}
$$

从原零标签 KAM 径向参数出发，可以**准确保持**整个负段的 $\Theta$，
同时把这个真实首相位系数改动任意 $|s|\le1$，参数改动小于 $2^{-87}$。
两侧根的完整 germ、原正段 raw DN 和所有端二 jet 均准确不变。

这是对一个明确的新最终度量候选族的真实横截结果。它没有把旧
$\Gamma^0$ 的标签、外好集、第四停止点或非线性逆自动改成新族的结论。
本篇证明的首系数是完整严格区 Cauchy 传播的系数变化；完整 mixed
return 的根有限部、Maslov 号、两端反射和全部余项仍须接到同一个单位。
不把主相位或这个首系数单独称为已取得全网络逆。

## 1. 两个实际支集及新族的身份

采用[强尾 KAM](R119-supplement-stronger-tail-joint-actual-return-KAM.md)
的全部 $\delta_j,\eta_j,K_j,c_j$ 和真实下降 log-quintic。
每个完整负分量包含一个下降段，写其固定局部坐标为
$x\in[0,1]$，$dt=\eta\,dx/\sqrt{12}$，原 log 落差为 $\Delta$。
令 $S(x)=10x^3-15x^4+6x^5$，则

$$
 B=\sqrt{12}\Delta/\eta,\qquad
 f(x)=S'(x)=30x^2(1-x)^2,
 \qquad Q=-A=7+Bf(x)
                                                               \tag{P.2}
$$

在未加参数的下降段成立。原参数的 bump 是

$$
 \psi_1(x)=64z_1^3(1-z_1)^3,
 \quad z_1=8(x-1/4),\quad 1/4\le x\le3/8.
$$

本篇新增

$$
 \psi_2(x)=64z_2^3(1-z_2)^3,
 \quad z_2=32(x-3/16),\quad3/16\le x\le7/32,
                                                               \tag{P.3}
$$

支集外均为0。两个支集相离，端点的0、1、2阶 jet 准确为0。
实际新 profile 为

$$
 \log p_{\gamma_1,\gamma_2}
   =\log p_{\rm base}+\gamma_1\psi_1+\gamma_2\psi_2,
 \qquad
 Q= B u,
 \quad u=f+7/B-(\gamma_1/\Delta)\psi_1'
                        -(\gamma_2/\Delta)\psi_2'.
                                                               \tag{P.4}
$$

其中 $\gamma_1$ 是原参数的同一个坐标，不另加一个重复的旧 bump。
新实际几何域取
$|\gamma_1|\le2^{-18}$、$|\gamma_2|\le2^{-30}$。
数值横截证明还在更大的 $|\gamma_1|\le2^{-16}$ 上同时成立。

两个支集都在严格负区；根位于另一未变的上升 quintic germ。
$p,w$ 及其端二 jet 在两个 bump 端点完全相同，所有其它位置的 $w$
也完全相同。因此真实负区两个根、正区 $A,w$、原 raw 密度及 raw DN
准确保持。这里说的是 raw 竖直高度/flux 单位；平均参考高度的积分变化
另在第7节保留，不因此宣称 grounded 框架也未经转换就相同。

## 2. 真正全层参数盒

前篇的第一类落差是 $\Delta_1=\log(K_j\alpha)+2|\log\delta_j|$；
第二类为 $\Delta_2=|\log\delta_j|-\log c_j$，其指标 $j\ge130$。
用 $\log2>2/3$、$\log(25/2)>2$、$\log64<9/2$ 得

$$
 \Delta_2>2+(2/3)130-9/2>80,
 \qquad\Delta_1>80.
                                                               \tag{P.5}
$$

又 $\delta_j<2^{-129}$、$\eta=\delta_j^{3/2}/(4\sqrt2)$，所以

$$
                         B>2^{190}.                         \tag{P.6}
$$

后面的全层计算使用更宽的独立盒

$$
 0\le e_B:=1/B\le2^{-190},\quad0\le d:=1/\Delta\le1/80,
 \quad |d\gamma_1|\le2^{-16}/80,
 \quad |d\gamma_2|\le2^{-30}/80.
                                                               \tag{P.7}
$$

没有只检查若干层后外推。支集上的 $u,u_x$ 在整个盒中严格为正，由
第5节的完整区间覆盖证明。因此两支集都未产生新型别零点。

## 3. 完整严格区首相位与准确变分

在同一个径向 raw 方程
$ (\mu h_t)_t+m^2\mu Qh=0$、$\mu=w/a$ 中，
准确有 $(\log\mu)_t=-1-Q$。先令 $y=\sqrt\mu h$，再令
$ds=\sqrt Q\,dt$、$u_w=Q^{1/4}y$，就得到已证的

$$
 (u_w)_{ss}+(m^2+V_w)u_w=0,
$$

$$
 V_w=\frac{Q_t}{2Q}-\frac{(1+Q)^2}{4Q}
              +\frac{5Q_t^2}{16Q^3}-\frac{Q_{tt}}{4Q^2}.
                                                               \tag{P.8}
$$

取固定严格切口 $x=1/8,7/16$，包含两个完整支集，且两端所有系数
与参数无关。完整两行 wave 传播的首相位系数为

$$
 \mathfrak b(\gamma_1,\gamma_2)
   =\frac12\int_{J}V_w\sqrt Q\,dt.
                                                               \tag{P.9}
$$

它包括原密度 potential，不只保几何光学 $m^2$。
这个有限积分没有转向发散，也没有任何被删掉的端项。

为说明 (P.9) 确实是实际传播系数，使用完整两态
$(\sqrt M u_w,(u_w)_s/\sqrt M)$，$M=|m|$，再分成两个复 wave 分量。
去掉 $e^{\pm iMs}$ 后，两个对角项准确为
$\pm iV_w/(2M)$，交叉项是同样系数乘 $e^{\pm2iMs}$。
$V_w$ 在这个严格区间是分片光滑的 BV 函数；真实 $C^2$ bump 接缝只
给有限跳变，必须保留在 $\operatorname{Var}V_w$ 中。对交叉项作一次
Stieltjes 分部积分，模小于
$(2\|V_w\|_\infty+\operatorname{Var}V_w)/(4M^2)$。
完整 Volterra 中含至少两次扰动的项由
$M^{-2}\|V_w\|_1^2e^{\|V_w\|_1}$ 控制。把对角的一次项重新写成指数，
只再增加同阶项。因此两支实际 phase 是
$\pm(M\int_J\sqrt Q\,dt+\mathfrak b/M)$，完整两行误差为
$C_J/M^2$，其中以上显示的实际 BV/L1 量给有限 $C_J$。
这一步不丢 slope，也没有把它升级成已付根网络的统一余项常数。

区间之外的完整真实根、严格片和正段因素不随两个参数改变。
所以其准确因式分解中，参数所新增的首相位变化就是 (P.9) 的变化。
若后来把整个返回的首系数写成根有限部加严格积分，这同一个变化仍必须
被保留；本篇没有把未知的固定根偏移常数设为0。

令 $\Theta=-2\int_{I}\sqrt Q\,dt$ 是整个真实负分量的两射线主相位。
只有两个 bump 支集参与变分。由端 jet 完全相同，分部积分准确给

$$
 \delta\mathfrak b
 =\delta\int_J\left[-\frac{(1+Q)^2}{8\sqrt Q}
                     -\frac{Q_t^2}{32Q^{5/2}}\right]dt.
                                                               \tag{P.10}
$$

被保留后相消的边界原函数是
$\sqrt Q/2-Q_t/(8Q^{3/2})$。
定义完整 Euler 密度

$$
 \mathcal E(Q)=-\frac3{16}\sqrt Q-\frac1{8\sqrt Q}
 +\frac1{16Q^{3/2}}+\frac{Q_{tt}}{16Q^{5/2}}
                         -\frac{5Q_t^2}{64Q^{7/2}}.
                                                               \tag{P.11}
$$

则 $\partial_{\gamma_s}\mathfrak b
=-\int\mathcal E(Q)(\psi_s)_t\,dt$。
这写法只使用 $Q_{tt}$ 的真实分片值，不引入一个未支付的第四径向导数。

## 4. 全两参数 Jacobian 的准确无量纲公式

在第 $s$ 个支集，只有 $\gamma_s$ 非zero。令

$$
 T_s=\sqrt B\,\partial_{\gamma_s}\Theta,
 \qquad B_s=B^{-1/2}\partial_{\gamma_s}\mathfrak b.
$$

把 (P.4) 代入全部变分，得到

$$
 T_s=\frac12\int\psi_s u_xu^{-3/2}dx,
                                                               \tag{P.12}
$$

$$
 \begin{aligned}
 B_s={}&\int\psi_su_x\left[-\frac3{32\sqrt u}
       +\frac{e_B}{16u^{3/2}}-\frac{3e_B^2}{32u^{5/2}}\right]dx\\
 &+d^2\int\psi_s'\left[-\frac{u_{xx}}{16u^{5/2}}
                         +\frac{5u_x^2}{64u^{7/2}}\right]dx.
 \end{aligned}                                               \tag{P.13}
$$

关键比例 $[(\sqrt{12}/\eta)^2/B^2]=\Delta^{-2}=d^2$ 准确抵消。
故归一 Jacobian 是

$$
 \mathcal M=\begin{pmatrix}T_1&T_2\\B_1&B_2\end{pmatrix},
 \qquad
 \det D(\Theta,\mathfrak b)=\det\mathcal M.
                                                               \tag{P.14}
$$

不是只在量纲上猜测两个参数独立。

## 5. 实际执行的完整区间积分

脚本把每个实际支集分为2048个闭子区间。在各区间上同时包住整个
(P.7) 参数盒，直接用以下准确多项式计算全部 integrand：

$$
 \psi=64z^3(1-z)^3,\quad
 \psi_x=192\ell^{-1}z^2(1-z)^2(1-2z),
$$

$$
 \psi_{xx}=384\ell^{-2}z(1-z)(1-5z+5z^2),\qquad
 \psi_{xxx}=384\ell^{-3}(1-12z+30z^2-20z^3),
                                                               \tag{P.15}
$$

其中 $\ell=1/8$ 或 $1/32$。$u,u_x,u_{xx}$ 的所有参数项同时保留。
矩形区间积分是整闭片上的模乘长度，不是节点采样或未付余项的求积式。
所有片的 $u>0,u_x>0$ 门都实际通过。

完整输出落在下列更宽有理盒内：

$$
 .085<T_1<.087,\quad .058<T_2<.061,
$$

$$
 -.023<B_1<-.021,\qquad -.010<B_2<-.008.
                                                               \tag{P.16}
$$

保留原有向积分区间相乘，真实得到

$$
 \boxed{\quad\det\mathcal M>2^{-11},\qquad
       \|\mathcal M^{-1}\|_{1\to1}<512,\qquad
       0<T_2/T_1<1,\quad(\det\mathcal M)/T_1>2^{-8}.
 \quad}                                                       \tag{P.17}
$$

这里 determinant 的门消费原有向区间，而不是只用展示的小数中点。
所有层都包含在同一个 $B,\Delta$ 盒，因而没有未处理的无限层。

## 6. 准确保持整个主相位的实际第二反项

取任何原实际径向 KAM 参数 $|\gamma_1^0|<2^{-19}$，起点
$(\gamma_1^0,0)$。由 $T_1>0$，存在唯一的局部曲线

$$
 \Theta(\gamma_1(s),s)=\Theta(\gamma_1^0,0),
 \qquad \gamma_1'(s)=-T_2/T_1.
                                                               \tag{P.18}
$$

因为其导数模小于1，曲线可以延至整个 $|s|\le2^{-31}$，仍严格留在
$|\gamma_1|<2^{-18}$ 的真实新几何盒内。在此曲线上

$$
 \frac d{ds}\mathfrak b(\gamma_1(s),s)
       =\sqrt B\,\frac{\det\mathcal M}{T_1}>2^{-8}\sqrt B.
                                                               \tag{P.19}
$$

两端 first-phase 的实际可达跨度各大于
$2^{-39}\sqrt B>2^{56}$。因此对每个 $|\zeta|\le1$，存在唯一实际参数
点，使 $\Theta$ 完全保持而
$\mathfrak b-\mathfrak b(\gamma_1^0,0)=\zeta$，且

$$
 |\gamma_2|\le2^8|\zeta|/\sqrt B<2^{-87},\qquad
 |\gamma_1-\gamma_1^0|<2^{-87}.
                                                               \tag{P.20}
$$

这是完整非线性参数曲线上的结果，不只是原点 Jacobian 非zero。
选择的 $ζ$ 与解参数的连续性来自同一严格单调逆。
目前这里只调径向参考；非径向全标签背景的真实 wave 首系数、全平均行和
所有参数导数仍须识别，不能将 (P.20) 自动用于它们。

## 7. 端点、背景 mean、物理 jet 与未转授的权限

两个 bump 均有准确零端二 jet，所以新的 $p,w$ 在所有原径向接缝匹配。
第二 bump 的 $k$ 阶导数至多为同形第一 bump 的 $4^k$ 倍。对 $k\le3$，

$$
 2^{-18}+4^k2^{-30}<2^{-16}.
                                                               \tag{P.21}
$$

因此新域中这些参数 jet 的绝对预算位于旧真实 scalar profile 证明所用的
预算内；根 quartet 和正型 raw 系数则完全未改。旧背景平端的实际正幂及
各接缝端 jet 可沿同一物理公式使用，不需把更陡新 profile 当作旧 profile。
这句话仅涉及这些已列出的背景 jet 门，不自动转授完整非线性标签图及源逆。

参考高度仍准确为

$$
 Z(a)=Z_e-\int_{a_e}^a w(s)ds,
 \qquad
 \delta Z=\delta Z_e+w_e\delta a_e-\int_{a_e}^a\delta w(s)ds.
                                                               \tag{P.22}
$$

当前局部参数的 $a_e$ 固定；以后第四停止点或尺度变化时，显示的移动端项
必须恢复。两支集内部改变了 $w$，故 (P.22) 的积分一般非zero，不能因
端 jets 相同而删掉 mean 高度变化。最终仍只有一个独立平移常数。

新参数将产生一个新的最终公共度量候选。真正完成后，phase 族必须共用
同一个已选参数点。旧 $t_0$ 好集、全允许线、第四返回、两 bump 和
完整标签/source realization 均需在这个新候选上按相应门重新实例化。
本篇没有改变第41--42束已固定 $\Gamma^0$ 的身份。

接下来的具体工作是：把 (P.9) 的变化与真实双根/正 DN return 的完整首
系数合并，利用第二反项支付完整相位算术，再对第42束 (S.21) 的完整
内部 Green 核付清同权费用。所有普通、weak、mean 和 bare 端荷继续保留。

## 8. 证据

`scripts/fourfold_phase_preserving_subprincipal_parameter_20261113.py` 同时
检查完整相位积分分部公式、实际 Euler 密度、4096个闭片的全参数 integrand、
两参数 determinant、准确曲线范围和全部新数字门。
报告为 `notes/2026-11-13-R119-phase-preserving-subprincipal-parameter-budget.json`。
实际数值用于 (P.17) 的严格区间门，不以 WKB 近似值判断某个真实谱分母。
