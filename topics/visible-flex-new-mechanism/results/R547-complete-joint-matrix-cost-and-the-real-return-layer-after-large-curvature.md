# R547：同一固定规范的联合矩成本与大曲率入端后的真实返回层

日期：2026-11-16。**完整原式纸面证明；没有执行数值、符号、profile、秩或新的科学任务。**

本文继续 R540/R546 的同一个三十三行母、同一个第二规范 $w=0$ 和同一个固定第三规范 $\chi$。R546 的二次矩脉冲已经支付一个固定矩读出的准确有限控制，但它没有清掉 $t_1$。下面证明一个比“快段时间太短”更强的完整成本门：从该实际入端继续，只要留在 $k\ge0$、$d_c<0$ 且离 $d_c=0$ 有固定距离的同一大曲率区域，那么无论后继多长、多慢、怎样使用完整历史反馈，都不能在保留净负 $p_1^{\omega_c}$ 的同时补回原 $t_1$。

若希望补清，这个控制族必须发生真正的返回动作：或者 $k$ 改变符号，或者 $d_c$ 从约 $-2$ 回到宽度 $O(L^9)$ 的零层。后一动作需要一个有固定非零下界的反向真实 $\delta$ 积分，不能只将已有正向 null 弧放慢。

另一个精确联合恒等把中心化的 $t_1$ 与 $p_1^{\omega_c}$ 耦合。它给出一个整个 history 系统都必须遵守的 slab 障碍，并把常高度后继的必要 $p_1^{\omega_c}$ 代价完整求到尖锐下界。这里的“尖锐”只针对明确写出的几何放松，不宣称原 ruling 能取到等号。

本稿没有构造新的慢 $t_1$ 入口，也没有把另一母库或另一 Gram 规范拼进来。结论是一个具体长时控制区域的完整阻断，以及下一真实返回必须支付的定量费用。

主要来源：

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：原八矩的逐点完整公式；
- [R533](R533-complete-velocity-quadratic-form-and-all-history-regular-ruling-coordinates.md)：同母完整速度二次式和真实八矩演化；
- [R536](R536-real-negative-total-matrix-density-from-a-complete-fast-height-loop.md)：固定规范的净负 $p_1^{\omega_c}$ 前缀；
- [R540](R540-same-positive-null-branch-and-real-large-curvature-with-negative-total-matrix-density.md)：同一实际高曲率入端；
- [R542](R542-complete-second-matrix-sign-and-duration-gates-for-the-fast-ruling-family.md)：原 $t_1$ 和中心化 $t_1$ 的真实负累计；
- [R546](R546-real-quadratic-matrix-pulses-and-an-exact-same-gauge-zero-coordinate.md)：完整二次矩脉冲及其真实静态费用。

## 1. 三个累计读出与两个必须分清的 $t_1$

固定 R540 的 $\omega_c>0$，记
$$
\eta=\omega-\omega_c,\qquad d_c=h\eta-k,\qquad
a=\frac{h_s}{h},\qquad
\delta=\frac{k_s}{2}-\eta h_s.
\tag{1}
$$
原水平关系和(1)给
$$
k_s=2(\delta+\eta h_s),\qquad
\eta_s=\frac{k_s}{2h},\qquad
(d_c)_s=-\delta.
\tag{2}
$$

以下小写表示原密度，大写表示从原零 history 起的真实累计：
$$
\begin{aligned}
\pi&=p_1-2\omega_c p_2=-kd_c,&
\Pi&=m_{p_1}-2\omega_c m_{p_2},\\
\tau&=t_1,& \Theta&=m_{t_1},\\
\tau_c&=t_1+\frac{\omega_c}{2}p_2,&
\Theta_c&=m_{t_1}+\frac{\omega_c}{2}m_{p_2}.
\end{aligned}
\tag{3}
$$
因此 $\Pi_s=\pi$、$\Theta_s=\tau$、$(\Theta_c)_s=\tau_c$。$\Theta$ 是原坐标；$\Theta_c$ 是一个固定的原矩线性组合。本文从不把二者互换。全 $M=0$ 必须使它们都为零。

由 R73(6)(9)(10)，准确有
$$
\boxed{
\begin{aligned}
8\tau&=k^2+2kd_c+2h\omega_c k-1-a^2,\\
8\tau_c&=k^2+2kd_c-1-a^2,\\
\pi&=-kd_c .
\end{aligned}}
\tag{4}
$$
这不是低速度展开。特别 $-a^2$ 始终是完整原费用，$\delta$ 没有被指定成外部自由状态。

## 2. R540/R546 入端可以保留的真实数量

原全部前缀、R536 的负保持段、R540 的高曲率弧，以及所选 R546 有限矩脉冲，都先真正走完。以下 $s=0$ 仅是后继区间的计时起点，不把任何累计量重新置零。

在原有限选择中，可同时保
$$
\boxed{
\begin{gathered}
k_0>2,\qquad -\frac94<d_{c,0}<-\frac74,\\
\Pi_0=-\varepsilon_P<0,\qquad
\Theta_0=-D<0,\qquad
\Theta_{c,0}=-D_c<0,\\
0<\varepsilon_P\le C_P L^7,\qquad
D,D_c\ge \frac{L^{-2}}{32}.
\end{gathered}}
\tag{5}
$$
$C_P$ 是各个先固定有限回路和保持长度的常数；它不是新输入。

说明(5)的来源也有助于防止隐藏原型成本。R536 的非恒区间以 $s-t_0=Lr$ 表示，$k,d_c=O(L^3)$，所以其完整 $\Pi$ 值为 $L^7$ 乘一个严格负的有限系数。常态前缀的 $\pi$ 为零。R540 及 R546 的新增三个 $p$ 坐标没有速度平方项，可把全部新增 $\Pi$ 费用限制在原严格负余量的一小部分，并保其绝对值仍为 $O(L^7)$。

R542 已使原 $\Theta,\Theta_c$ 不大于 $-t_0/16$，其中 $t_0=L^{-2}$。R546 的完整二次矩满足
$$
t_1(N)=-\frac{h_s^2}{8h^2}\le0,\qquad p_2(N)=0.
$$
因此其可能为正的 $\Theta,\Theta_c$ 增量只来自实际静态密度乘真实长度。对那个已经固定的有限目标，R546 可把平台和 ramp 的实际长度再取足够小，使这一正增量小于 $t_0/32$。其完整矩目标仍由原有限端时间 IFT 准确支付，并不因这个长度要求失去解。

R540 的参考末值是 $d_c=-2$；其真实 shadow 误差及 R546 的追加 scalar 误差可共同取小于 $1/4$。这给(5)的 $d_c$ 区间。所有这些都是同一有限母、同一固定 $\chi$、同一个原起点上的原允许参数选择；没有增加 profile 行，没有再选 Gram，也没有把 $m,T$ 重置。

下文实际上先证明对任意精确入值
$\varepsilon_P,D,D_c>0$ 的结论，再代入(5)。故其逻辑不依赖只知大 $O$ 而不知真实值。

## 3. 任意时长的负 $d_c$ 区域成本

保 R540/R533 已固定的合法 scalar 紧盒 $\mathcal B$，记
$$
h_+=\max_{\mathcal B}h,\qquad
K=\max_{\mathcal B}|k|,\qquad
\mathfrak K=K+2h_+\omega_c>0.
\tag{6}
$$
研究从(5)实际入端继续的任意有限光滑路径，完整满足原 ruling、原水平关系和全部历史方程。暂设在整个后继 $0\le s\le\ell$ 上
$$
k(s)\ge0,\qquad d_c(s)\le-d_*<0,\qquad S(s)\in\mathcal B.
\tag{7}
$$
其余条件不作简化：$\ell$ 可以任意大，$h_s,k_s$ 可以变化，$m,T$ 可以很大。

令
$$
\Delta\Pi=\int_0^\ell\pi\,ds,\qquad
\mathscr E_h=\int_0^\ell a^2\,ds.
\tag{8}
$$
由(7)，$\pi=k(-d_c)\ge d_*k\ge0$。原式(4)遂逐点给
$$
\begin{aligned}
8\tau
&\le k^2+2h\omega_c k-1-a^2\\
&\le \mathfrak K k-1-a^2\\
&\le \frac{\mathfrak K}{d_*}\pi-1-a^2.
\end{aligned}
\tag{9}
$$
第一步只舍去了非正的 $2kd_c$；没有舍掉高度速度平方。于是完整累计满足
$$
\boxed{
8\Theta_{\rm final}
\le -8D+\frac{\mathfrak K}{d_*}\Delta\Pi
-\ell-\mathscr E_h.
}
\tag{10}
$$
同样，对中心化矩有更小的静态常数：
$$
\boxed{
8\Theta_{c,{\rm final}}
\le -8D_c+\frac{K}{d_*}\Delta\Pi
-\ell-\mathscr E_h.
}
\tag{11}
$$

如果仍要求原累计 $\Pi_{\rm final}<0$，则
$$
0\le\Delta\Pi<\varepsilon_P.
$$
所以(10)直接推出
$$
\boxed{
8\Theta_{\rm final}
<-8D+\frac{\mathfrak K\varepsilon_P}{d_*}
-\ell-\mathscr E_h.
}
\tag{12}
$$
特别，只要
$$
d_*\ge\frac{\mathfrak K\varepsilon_P}{8D},
\tag{13}
$$
后继就不可能把原 $\Theta$ 补到非负。这是任意时长的门，不是只排一个快极限。延长停留会继续加入(12)中的 $-\ell$；若高度不恒定，还要加入真实的 $-\mathscr E_h$。

反之，若同一个后继真的达到
$\Theta_{\rm final}\ge0$、$\Pi_{\rm final}<0$，则在(7)范围内必须有
$$
\boxed{
d_*<
\frac{\mathfrak K\varepsilon_P}
{8D+\ell+\mathscr E_h}.
}
\tag{14}
$$
原总矩、原前缀亏损、后继正 $p_1^{\omega_c}$ 代价和高度能量都出现在同一个不等式中。

## 4. 从当前实际入端补 $t_1$ 必须发生真实返回

(12)可以不预先指定一个后继区域，而直接化成所有同盒后继的必要二择。

假定一条真实后继达到
$$
\Theta_{\rm final}\ge0,\qquad \Pi_{\rm final}<0.
\tag{15}
$$
定义由真实入值确定的正数
$$
d_{\rm gate}=\frac{\mathfrak K\varepsilon_P}{8D}.
\tag{16}
$$
则这条路径上必有以下两种事件中的至少一种：

1. $k$ 从正入值走到负值，因连续性先真实经过 $k=0$；
2. $d_c$ 从约 $-2$ 走到 $d_c>-d_{\rm gate}$。

否则全程有 $k\ge0$ 和 $d_c\le-d_{\rm gate}$，可在(12)取
$d_*=d_{\rm gate}$，得到 $\Theta_{\rm final}<0$，与(15)矛盾。
这一步不要求 $\Pi$ 在中途也为负，只要求最后为负；若中途曾使用更大正费用，最后仍必须全部偿还。

代(5)，
$$
\boxed{
d_{\rm gate}\le 4\mathfrak K C_P L^9.
}
\tag{17}
$$
因此在当前尺度下，补清原 $t_1$ 的路径不能只留在已有的“大正曲率、负 $d_c$”区域。它必须改变曲率号，或真正回到 $d_c=0$ 的 $O(L^9)$ 层；后者可以继续进入 $d_c>0$，但不能只把一条停在 $d_c\approx-2$ 的弧走慢。

这一返回有非零的原控制费用。取 $L$ 小到 $d_{\rm gate}<1/4$。
在第二种事件的首次到达时刻 $s_*$，由(2)(5)，
$$
\int_0^{s_*}\delta\,ds=d_{c,0}-d_c(s_*)
<-\frac74+\frac14=-\frac32.
\tag{18}
$$
所以某处必须有真实 $\delta<0$，且其有向积分不能是一个趋零的调整。
若选择第一种事件，在首次 $k=0$ 时亦有
$$
\int_0^{s_*}(\delta+\eta h_s)\,ds=-\frac{k_0}{2}<-1.
\tag{19}
$$
两式均是原水平系统的准确积分，不是给任意 formal null 方向预授实现。

## 5. 一个完整联合恒等：大 $k$ 不是正确的单一慢变量

另定义一个几何变量
$$
\zeta=2h\eta-k=k+2d_c.
\tag{20}
$$
$\zeta$ 不是 profile 自然约束 $\mathbf q$，也不是新增自由矩。
由(2)，
$$
\boxed{
\zeta_s=2\eta h_s=(k+\zeta)\frac{h_s}{h}.
}
\tag{21}
$$
因此常高度段使 $\zeta$ 准确不变，无论累计 history 多大。

将(4)重写为
$$
\pi=\frac{k(k-\zeta)}2,\qquad
8\tau_c=\zeta k-1-a^2,
$$
遂得完整恒等
$$
\boxed{
8\tau_c-2\pi
=\zeta^2-1-(k-\zeta)^2-a^2.
}
\tag{22}
$$
没有对 $h_s,k_s$ 作展开，没有对 $m,T$ 作假设，也没有用某个相位的 ruling 代替原全相位方程。

从真实入端积分：
$$
\boxed{
\begin{aligned}
8\Theta_{c,{\rm final}}-2\Pi_{\rm final}
={}&-8D_c+2\varepsilon_P\\
&+\int_0^\ell
\{\zeta^2-1-(k-\zeta)^2-a^2\}\,ds.
\end{aligned}}
\tag{23}
$$
(5)保证 $8D_c-2\varepsilon_P>0$。因此，如果后继始终满足
$|\zeta|\le1$，则(23)右边严格为负。它不可能同时满足
$$
\Theta_{c,{\rm final}}\ge0,\qquad\Pi_{\rm final}\le0.
\tag{24}
$$

这是一个完整联合 slab 障碍。它适用于任意速度和完整历史；不是只针对常高度或快脉冲。全 $M=0$ 必须满足(24)，所以也被该 slab 排除。
不过不能把 $\Theta_c$ 换成原 $\Theta$：如果尚未清 $p_2$，原
$t_1$ 的单行恢复与中心化行恢复是两个不同问题。

更精确地，若 $\Theta_{c,{\rm final}}\ge0$、$\Pi_{\rm final}<0$，
(23)给
$$
\boxed{
\begin{aligned}
\int_0^\ell(\zeta^2-1)_+\,ds
>{}&8D_c-2\varepsilon_P\\
&+\int_0^\ell(1-\zeta^2)_+\,ds
+\int_0^\ell(k-\zeta)^2\,ds+\mathscr E_h.
\end{aligned}}
\tag{25}
$$
所以单纯跨过 $|\zeta|=1$ 还不够：还必须支付原前缀的全部时间亏损、错误号区域、$k-\zeta=-2d_c$ 的平方以及高度能量。

若在实际盒内 $|\zeta|\le Z_{\mathcal B}$，且 $Z_{\mathcal B}>1$，则真正在 $|\zeta|>1$ 区的时间满足
$$
\boxed{
|\{s:|\zeta(s)|>1\}|
>\frac{8D_c-2\varepsilon_P}{Z_{\mathcal B}^2-1}.
}
\tag{26}
$$
若 $Z_{\mathcal B}\le1$，(24)根本不可能。
这给原时间参数下的成本，不能用重新参数化将它消掉。

## 6. 常高度后继的尖锐几何放松

现在只考虑一个从实际入端接出的常高度后继：
$$
h(s)\equiv h_0,\qquad \zeta(s)\equiv\zeta_0.
\tag{27}
$$
仍不假设它可由原 ruling 免费实现。实际入端若没有 $\gamma=0$
的相容 germ，还须先支付真实接入段。这里求的是任何这样的后继都必须满足的最小矩费用。

设后继长度为 $\ell>0$，记
$$
I=\int_0^\ell k\,ds,\qquad J=\int_0^\ell k^2\,ds.
$$
由(22)前的两个原密度式，
$$
\Delta\Theta_c=\frac{\zeta_0 I-\ell}{8},\qquad
\Delta\Pi=\frac{J-\zeta_0 I}{2}.
\tag{28}
$$
若要补回 $D_c$，必须
$$
\zeta_0 I\ge\ell+8D_c.
\tag{29}
$$

当 $\zeta_0=0$，$\tau_c=-1/8$，无恢复可能。以下取
$0<q=\zeta_0^2\le1$，置 $\mathcal D=8D_c>0$。
真实 Cauchy 不等式 $I^2\le\ell J$ 给
$$
\Delta\Pi\ge
\frac12\left\{\frac{(\zeta_0 I)^2}{q\ell}
-\zeta_0 I\right\}.
$$
该括号作为 $v=\zeta_0 I$ 的函数，在 $v\ge\ell+\mathcal D$ 上严格增，
因为 $q\le1$。故
$$
\boxed{
\Delta\Pi\ge
\frac{(1-q)\ell+(2-q)\mathcal D+\mathcal D^2/\ell}{2q}.
}
\tag{30}
$$
对于 $0<q<1$，再用两正项的算术几何均值，
$$
\boxed{
\Delta\Pi\ge
\frac{\mathcal D(1+\sqrt{1-q})^2}{2q}.
}
\tag{31}
$$
对于 $q=1$，有限 $\ell$ 仍准确有
$$
\boxed{
\Delta\Pi\ge\frac{\mathcal D}{2}
+\frac{\mathcal D^2}{2\ell}
>\frac{\mathcal D}{2}.
}
\tag{32}
$$
所以所有 $0<|\zeta_0|\le1$ 的常高度恢复，单是其正
$p_1^{\omega_c}$ 费用就至少为 $4D_c$；而当前可用负预算只有
$O(L^7)$，$D_c$ 至少为 $L^{-2}/32$。它们不可能同时完成(24)。

(31)在纯几何放松中是尖锐的：先不施加 ruling、入端 germ 或其它矩，取
$\ell=\mathcal D/\sqrt{1-q}$，并令 $k$ 为满足(29)等号的常数，便在所有使用的不等式中取等。这个说明只识别放松问题的准确下界；它没有构造一条原 $F=0$ 路径，更没有忽略从实际入态接到该常数的成本。

对于 $|\zeta_0|>1$，(30)的首项系数改变符号，本文不把(31)延拓过去。该区域仍可能具有几何上的正恢复预算；完整同 $\chi$ 的实际慢分支和其长时存在性必须另外证明。

## 7. 原 ruling 仍是返回层的真实接入门

前面每个不等式都由原八矩密度证明，所以它们对所有真正
$F=0$ 路径成立；反向不能据此宣布某个所需速度可实现。

特别，要在固定当前 $S,m$ 取 $\gamma=0$，完整原二次式必须满足
$$
\boxed{
H_{22}\delta^2+\mathsf l_\delta\delta+\mathsf c_\nu=0.
}
\tag{33}
$$
若 $H_{22}\ne0$，须核真实判别式
$\mathsf l_\delta^2-4H_{22}\mathsf c_\nu$；还须所选根属于与实际入 germ 相接的分支。$H$ 严格不定本身不推出(33)有实根。

同样，若实际控制从 $\delta\ge0$ 转入(18)要求的负 $\delta$
区，首次 $\delta=0$ 点必须满足
$$
\boxed{
H_{11}\gamma^2+\mathsf l_\gamma\gamma+\mathsf c_\nu=0.
}
\tag{34}
$$
当 $H_{11}=0$ 时应按实际线性或常数方程处理，不能除以它。
R546 所用的两个完整图仍是
$$
X=a_{\rm in}\ne0,\qquad
Y=\frac{\Delta(S,m)}{2\kappa_Na_{\rm in}},
$$
或
$$
Y=b_{\rm in}\ne0,\qquad
X=\frac{\Delta(S,m)}{2\kappa_Nb_{\rm in}}.
$$
它们只消掉一个速度未知量。其 $z_c,\Delta$ 保完整 $m$ 平方和固定
$\chi$，没有把(18)、(33)或(34)自动支付。也不能将另一母库中从起点重新选择的 Gram 向量拿来替代当前 $\nu$。

所有后继状态仍按
$$
m_s=M_{\rm raw}(S,\gamma,k_s),\qquad
T_s=-M_{\rm raw}\circ\Phi_m+C(S,j^2S)
\tag{35}
$$
真实积分；固定初端势、共同右锚、frame、位置和第四成本都保留。
本文没有对(35)作新的界或重置，也未授予一个从实际入态尚未到达的 slow branch。

## 8. 已闭范围与下一具体问题

本稿完整排除了一个自然但不合法的捷径：R540 已经达到 $k>2$，
不意味着可以在原负 $d_c$ 大曲率区任意慢停留并补回 $t_1$。
在保留净负 $p_1^{\omega_c}$ 的真实预算下，(12)对任意时长都成立；
其要求的返回层宽为(17)，而真实反向控制必须付出(18)或(19)。

联合恒等(22)还说明，完整矩返回不能只按 $k$ 的幅度判断。
即使离开(7)，若仍锁在 $|\zeta|\le1$ 的 slab，中心化 $t_1$ 与
$p_1^{\omega_c}$ 也不可能共同清零。常高度属于这一障碍中最直接的子类，其最小正 $p_1^{\omega_c}$ 费用由(30)–(32)给出。

真正仍欠的是同一个固定母和 $\chi$ 上的实际返回：从已实现的
$(S_0,m_0,T_0)$ 出发，如何经过完整(33)(34)的相容分支，进入能同时支付两种累计费用的区域，并保持足够长的原时间。本文不以新的条件列表代替这一存在性；它证明的是当前具体控制区域确实被排除，后继必须改变实际轨道。全八矩、第三返回、末 scalar/germ、pose 及最终同一规范仍未闭合。
