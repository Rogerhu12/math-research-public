# R763　真 U 上必需的周向轴斜与保持全部实射线的一次旋度下降

## 1　原 R750 给定开集强迫的周向轴斜

用 [R750](R750-two-rigid-core-disks-and-all-prescribed-annulus-chords.md) 和 [R760](R760-true-meridian-shortening-and-the-two-edge-three-curl-field.md) 的同一固定材料、两个给定开带及真实径向弧长 $\ell$。在两个 U 的各自中段，用原环弧长 $\sigma$。令 $I$ 是其中任一段长度 $d=.60$ 的恒曲率圆弧。存在这样的实区间。U 的原角是 $-\pi S(v)$ 或其平移，$|S(v)-v|<.002$，因而 $L_U\ge .4/(2/\pi+.002\pi)>.62$。原光滑阶跃在 $[.0015,.9985]$ 上有恒导 $1/.998$。故这些圆弧的原周曲率 $k=-\pi/(.998 L_U)$，$|k|<5.1$。

从真实强迫袖末 $\ell_*=.050069$ 到内末竖直开带的给定锚 $\ell_i$，实际径长 $L<.726$。若 $u(\ell)$ 是原长 S 和原圆角的内偏，$-.044<u<.112$，更精确地 $|k|<\pi/(.998\cdot .62)<5.078$。此真材料矩形的度量和边标满足
$$
 g=d\ell^2+h(\ell)^2 d\sigma^2,\qquad h=1+ku,\quad .43<h<1.23,\quad |h'|<5.1 .
$$
在 $\ell_*$，U 刚运，真周单位切线是原 $T_0(\sigma)$。在 $\ell_i$，刚盘把它转到 $Q_\lambda T_0(\sigma)$，实际 $YZ$ 转角 $q=.5074\lambda$。这也固定两处的真实邻域和两 jet。

设 $F$ 是满足两端数据的 $C^2$ 真等距图。如果整个矩形保持 $x_\sigma=0$，则 $F_\ell=A(\ell)e_x+b N$，$F_\sigma=hT$，其中 $T,N$ 是 $YZ$ 内的有向单位正交对。$b^2=1-A^2$ 对周标为常数，故由连续性，带符号的 $b$ 在每一段 $I$ 上也为常数，包括 $b=0$ 时。比较两种混合导的 $N$ 分量得到 $h\,T_\ell\cdot N=b_\sigma=0$。于是同一实标签的 $YZ$ 切线沿径向恒定。对每个 $\lambda>0$ 这与两个实际开带转角 $q$ 冲突。该结论适用于任意原子午角、任意已闭射线积分及任意内部材料标架。

若还付清两主曲率绝对值 $\le K=10.4$，可给真斜率定量。令 $\varepsilon=\sup |F_\sigma\cdot e_x|/h$。只须处理 $0<\varepsilon\le10^{-4}$。写
$$
 F_\sigma/h=w e_x+cV,\quad c=\sqrt{1-w^2},\qquad
 F_\ell=Ae_x+aV+bN,\quad a=-Aw/c,\quad b^2=1-A^2/c^2 ,
$$
$V=(\cos\phi,\sin\phi)$ 为 $YZ$ 内的单位向量，$N=iV$。对两个真周标，$f(\ell)=x(\ell,\sigma_1)-x(\ell,\sigma_2)$ 满足 $|f|\le1.23d\varepsilon$。两端的 $f=f'=0$ 来自外给定真平袖和内给定真竖片。两径线都是源单位速测地线，故 $|f''|\le2K$。延零后仍有相同的一阶 Lipschitz 界。用步长 $t$ 的中心差得 $|f'|\le\|f\|_\infty/t+Kt$，于是
$$
 \operatorname{osc}_I A\le2\sqrt{K\,1.23d\varepsilon},\qquad
 \operatorname{osc}_I b\le B(\varepsilon)
 =2\sqrt{\frac{4\sqrt{K\,1.23d\varepsilon}+2\varepsilon^2}{1-\varepsilon^2}} .
$$
第二式先比较任意两点的 $b^2$，用 $|A|\le1$ 和 $1\le c^{-2}\le(1-\varepsilon^2)^{-1}$。若 $b$ 异号，两点之间有 $b=0$，所以带符号振幅至多是同一平方振幅开方的两倍。

比较 $F_{\ell\sigma}=F_{\sigma\ell}$ 的 $N$ 分量，
$$
 hc\phi_\ell=b_\sigma+a\phi_\sigma .
$$
$T=F_\sigma/h$ 沿径向内在平行，故 $|T_\ell|\le K$。沿周向的内在分量为 $-h'F_\ell$，法分量至多 $hK$，故 $|T_\sigma|\le\sqrt{h'^2+h^2K^2}<14$。有 $|\phi_\ell|\le K/c,|\phi_\sigma|\le14/c$。在材料矩形上连续提升 $\phi$；两边角差 $q+2\pi n$ 的 $n$ 对 $I$ 恒定，绝对值至少为 $q$。因 $h$ 在 $I$ 上不变，先积周标再积径向得
$$
 q\le .726\left[\frac{B(\varepsilon)}{.43d}
  +\frac{14\varepsilon}{.43(1-\varepsilon^2)}
  +\frac{10.4(1-\sqrt{1-\varepsilon^2})}{\sqrt{1-\varepsilon^2}}\right]
 <19\varepsilon^{1/4}.
$$
最后一步用 $d=.60,\varepsilon\le10^{-4}$。故对两个真实 U 各自的上述材料矩形，都必须有
$$
 \boxed{\displaystyle \sup\frac{|x_\sigma|}{h}>4.9\cdot10^{-7}\lambda^4 \quad (\lambda>0).}
$$
若 $\varepsilon>10^{-4}$ 显然也成立。此处的数值门使用 $10.4$ 曲率上界。原题的 reach 需求为 $.03D$，对 $C^2$ 嵌入它给主曲率上界 $1/(.03D)$。采用 R750 候选证书中半径 $1/10.4$ 的全法球即可使用上式；只知某个别的实际 $D$ 和 $.03D$ 时，可在前面未取数值的估计中用该曲率上界。起首的零斜排除不需曲率常数。整个环带、跨片法球、所有相位的同一 $D$ 仍用原题门。

## 2　保持径向刚好不变的真同度量标架

在 R760 的材料子午带，$U_0=X_{0,\ell}$，$|U_0|=1$。任取其完整原三轴场 $R(q_{\rm old})$。令 $A(U_0,a)$ 表示绕真实源轴 $U_0$ 的正向空间旋转，取
$$
 \widetilde R=R(q_{\rm old})A(U_0,a).
$$
$a$ 支撑在真子午内部以及 U 恒曲率开区间内，两端、角界和中心都有完整不动开带。设 $L=RU_0$, $T=RX_{0,\sigma}/h$, $M=L\times T$。新场为
$$
 \widetilde\beta_\ell=L,\qquad
 \widetilde\beta_\sigma=h(\cos a\,T+\sin a\,M).
$$
两者点积为零、长度分别为 $1,h$。取 $a=0$ 包含原 R760 整个空间。对任意 $q_{\rm old}$ 和 $a$，原径一形式及其各导完全不变。因而两开带原姿及完整两 jet、所有三分量实射线积分、对旧 $q$ 的所有位置列也不变；对 $a$ 的位置列严格为零。尤其 [R760](R760-true-meridian-shortening-and-the-two-edge-three-curl-field.md) 已闭的小相位所有标签三真矩原样继承。大相位实际已有的横向残量也照原数保留。

从两端按原 R750 规则径向积分并补固定权得到的实体 $P$ 只用原边、$\beta_r$ 及其导。因此对固定 $q_{\rm old}$，所有 $a$ 给相同的 $P$ 和五导，相同的实际度量误差、曲率、法球与直径。新的对象是完整旋度、实际周向一形式、其导、以及对原和新系数的真实旋度 Jacobian。后续拟合须能改变旧 $q$ 才会改变实体。若两端都锚定且三分量射线已闭，令 $W=\partial_\sigma(P_{\rm out}+\int\beta_\ell d\ell)$。任一保持同一 $L$ 的同度量标架都有点态缺口
$$
 |\widetilde\beta_\sigma-W|^2\ge (W\cdot L)^2+
    (|W-(W\cdot L)L|-h)^2=:d_W^2 .
$$
正交投影非零时，取沿该投影的单位向量使之相等。外边处两项准确匹配，径向积分旋度得到 $\widetilde\beta_\sigma-W$；因此到该点的 $\sup|\partial_\ell\widetilde\beta_\sigma-\partial_\sigma L|\ge d_W/(\ell-\ell_{\rm out})$。即使当前射线未闭，上式对单独从外端锚定的径积分仍成立，并须另外支付真实内端差。$d_W=0$ 是实体周切向长度/正交的条件；若全场该条件、正则性与真实三端位移均成立，取 $T=W/h$ 可组成可积同度量标架。全局嵌入、reach 和宏观仍另行支付。

## 3　完整三分量能量的有限严格下降

保留 R760 零控制实场的 $\Theta,\psi$，$T=(0,T_\psi)$，$L=(\cos\Theta,-\sin\Theta N_\psi)$，$M=(\sin\Theta,\cos\Theta N_\psi)$。记
$$
 K(a)=\partial_\ell[h(\cos a\ T+\sin a\ M)]-\partial_\sigma L .
$$
$\sigma$ 是原周弧长，使用真实三个空间分量的 $\mathcal E(a)=\int |K(a)|^2d\ell d\sigma$。由 $K'(0)[y/h]=(yM)_\ell$，对支撑在两个实开边之间的平滑函数有
$$
 D\mathcal E(0)[y/h]=-2\int y\,(\partial_\ell K(0))\cdot M\, d\ell d\sigma .
$$
画出全部三个分量时，置 $T_a=\cos a\ T+\sin a\ M$，$M_a=-\sin a\ T+\cos a\ M$，$S=(k+\psi_\sigma)\sin\Theta$, $B=\Theta_\sigma$。按 $T_a,M_a,L$ 的有向分解，
$$
 K(a)=(h'-S\cos a+B\sin a)T_a+
 [h(a_\ell+\cos\Theta\,\psi_\ell)+S\sin a+B\cos a]M_a+
 h(\Theta_\ell\sin a-\psi_\ell\sin\Theta\cos a)L .
$$
这包括原 $a=0$ 时全部周标变化。对非零旧 $q$ 应从其完整 $SO(3)$ 场实际求导。

在每个 U 的恒曲率段，R760 小相位三矩支的**原圆角内部**满足 $\Theta=\theta_0,\ \psi=q\eta$，$\eta=10t^3-15t^4+6t^5$，$t=(\ell-.602)/(\ell_{\rm flat}-.602)$。于是
$$
 (\partial_\ell K(0))\cdot M=q\cos\theta_0(h\eta')'.
$$
取 $.12<t<.22$。真实圆角宽 $.1739<\ell_{\rm flat}-.602<.174$，原 $\theta_0<.35$，$h'\ge-5.1\sin(.35)>-1.76$，$h>1-5.1(.174)(.22)\sin(.35)>.932$。$\eta''\ge60(.12)(.78)(.56)/.174^2>103$，$0\le\eta'<30(.22)^2/.1739<8.36$。故显示的真投影大于 $60q$。

全相位轴缩支在 U 上的 $\Theta$ 只依赖 $\ell,\ \psi=q\eta$，$t=(\ell-.065)/.537$。在 $.02<t<.06$ 有
$$
 (\partial_\ell K(0))\cdot M=q\cos\Theta
      [h\eta''+k(2\sin\theta_0-\sin\Theta)\eta']>2q .
$$
事实上 $.0257<\ell-.050<.0473$，原 S 上 $|\theta_0|<.057$，R760 实首转与原角凸混合给 $|\Theta|<.475$，且 $u\le0,h\ge1$。又 $\eta''>60(.02)(.94)(.88)/.537^2>3.43$，$\eta'<.202$。将这些量和 $|k|<5.1$ 代入即得。

在上述各支真实径区间取非负 $a=\tau q\chi(\sigma)B(t)$，其中 $\chi$ 是任一 U 内部非零紧支非负 $C^2$ 函数，$B$ 是该真开径段的非零紧支非负 $C^2$ 函数。代 $y=hq\chi B$ 得 $D\mathcal E(0)[q\chi B]<0$，故所有充分小的正有限 $\tau$ 都给完整三分量平方积分的严格下降。径、周支持之外的旋度逐点原样。支内 $h\sin a\sin\Theta$ 是新周向轴分量；圆角 $\theta_0>0$，全长支的指定 S 首腿处 $\Theta<0$。两个真实 U 都可付此变化。$\lambda=0$ 取 $a=0$。带分支选择的此候选不补 R760 两个姿之间尚未证明的整体场同伦。

对一般已付场，还可在每条真材料线最小化完整线性化平方积分 $\int|K(0)+(yM)'|^2$。相应紧支试函数空间上的正定双线性型是 $\int (y' z'+|M'|^2yz)$，右端为 $-\int K(0)\cdot(zM)'$。给定两开带零迹后正定；精确非线性候选仍须按原物理 $K(a)$ 回溯。积分下降不能代替两个原生离散全场的绝对峰、所有位置行、全列拟合与真实实体资格。本文没有运行数值，没有给非零相位的等距闭壳。
