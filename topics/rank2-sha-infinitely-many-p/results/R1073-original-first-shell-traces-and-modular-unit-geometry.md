# R1073 — 原首层迹与模单位几何

承接[同编号§§1–16](R1073-original-fixed-quadratic-curve-pair-and-central-certificates.md)。两条固定曲线、完整390角色、原水平变形与canonical二阶保持不变。

## 17. 原权一Hecke全迹与首层外端的全部正次数

用(W1)–(W8)。此恒等式适用于每个原 $g=f_k$ 以及由三级截面经固定130同源拉回的每个 $g=G_C$。对任意具相应水平结构 $(E',\alpha',\omega')$ 的变形，依 $q_D^*\omega_D=\omega'$ 取所有 $p+1$ 个 $p$ 商。有
$$ \sum_{D\subset E'[p],\,|D|=p}g(E'/D,q_D\alpha',\omega_D)=0. \tag{K1}$$
对 $f_k$ 用(P2)的七除点同源迹，各核点总和是整个 $E'[p]$ 加上零点的 $p$ 个额外拷贝。$[p]$ 的归一目标微分为 $\omega'/p$，故全 $E'[p]$ 和为 $p\sum_a\epsilon_k(a)^{-1}F_7([p]\alpha'(a))=p\epsilon_k(p)g$。原三条 $\epsilon_k(p)=-1$。对 $G_C$，把固定130商与$p$商交换，完整标记及微分由归一唯一性相容；三级 $\epsilon_0(p)=-1$。

记 $\Phi_g(Y)=P(\pi X(Y))g(\pi X(Y))$。在 $z$ 近零，$1+\kappa Y^d-zY=0$ 在 $d$ 个端点各有一解析根 $Y_i(z)$。有整个局部恒等式
$$ \sum_{i=1}^d \Phi_g(Y_i(z))=0. \tag{K2}$$
具体让源沿带全水平的小盘邻域变动，特征零下各 $p$ 线在原点附近解析延拓。源水平预先重标为 $\alpha M^{-1}$，其中 $M$ 是原 $\mathrm{Fr}$ 在 prime-to-$p$ 水平上的矩阵，故全部目标 $q_D\alpha M^{-1}$ 在特殊纤维皆为原 $\bar\alpha$，每个目标都采用(W2)的原 $g$。由(W8)末段的统一 $\mathrm{Fr}$ 标记，这些同源在水平等晶体上都由同一特殊 $\mathrm{Fr}^*$ 作用。记它在两条水平线的反对角系数为 $A,B$，即 $q_D^*e'_0=Ae_1,\ q_D^*e'_1=Be_0$。这些等式在各中央目标点由等晶体比较给出，沿分支由连接延拓。源参数 $w$ 与目标 $w'$ 满足 $w'=A/(Bw)$，且 $q_D^*\omega(v')=[Bw'P(v')/P(v)]\omega(v)$。对 $w\ne0$，从(K1)除去公共非零因子 $Bw'/P(v)$。取 $z=\pi/(6w')$，由(W2)各目标就是 $1+\kappa Y^d-zY=0$ 的各支，在 $z=0$ 由首层全部 $d$ 个不同端点识别。在非零 $z$ 先得全和再解析延拓即(K2)。此处保留了各分支的 $P(v')$。

在径向变量 $t=-\kappa Y^d$，$\Phi_g=(1-t)G_g/(1+pt)$。对 $(Y,z)\mapsto(\zeta Y,\zeta^{-1}z)$，$\zeta^d=1$ 作完整平均，将 $G_g$ 换为(W7)的 $F_g(t)$。设 $x=-z^d/\kappa$，$t_1,\ldots,t_d$ 是 $(1-t)^d=xt$ 的根；$z\ne0$ 时 $t$ 唯一确定 $Y=(1-t)/z$。于是
$$ \sum_{(1-t_i)^d=xt_i}\frac{1-t_i}{1+pt_i}F_g(t_i)=0 \qquad(x\sim0). \tag{K3}$$
在 $t=1$ 取 $\xi=(1-t)t^{-1/d}$、$t(0)=1$。$x=\xi^d$，且 $d\log\xi=-(1+pt)dt/[d\,t(1-t)]$。令 $J_g$ 为 $F_g(t)dt/t$ 在 $t=1$ 的任一局部原函数；则(K3)给 $\sum_{\zeta^d=1}J_g(t(\zeta\xi))=dJ_g(1)$。全部正次数外端条件为
$$ [\xi^{dj}]J_g(t(\xi))=0,\qquad
 [y^{dj-1}](1-y)^{j-1}F_g(1-y)=0\quad (j\ge1). \tag{K4}$$
第二式用 $y=1-t,\ y=\xi(1-y)^{1/d}$ 的 Lagrange 式。对 $g=f_b$ 可取 $J_g=I_g$，其 $J_g(1)=0$；并且(W8)的二次原函数在 $t=1$ 的全部正 $\xi^{dj}$ 系数同样为零，因为其导数是常数乘 $I_g\,d\log\xi$。其零次项仍为(W8)所求标量。每个 $G_C$ 的外端约束来自自身原权一 Hecke 迹，没有给单支的一、二阶积分常数赋值。

## 18. 原三级的相反Weil分量与奇层逐商真零

在(Z1)原分量记 $\iota:\alpha_3\mapsto\alpha_3\circ[\omega]$。$f_3$ 为特征 $\omega^{-1}$ 的非零截面，因为 $f_3(\alpha_3\circ[\omega])=\epsilon_0(\omega)f_3(\alpha_3)$ 且(Z3)非零。另取 $e(E,\alpha_3,\kappa)=E_1^*(\alpha_3(\delta))$，采用同一 $\kappa$。$\omega\delta\equiv\delta\bmod3$ 故 $\iota e=e$。它亦非零：每个非零三挠 $P$ 有 $E_1^*(P)=-\wp''(P)/(6\wp'(P))$。若此值为零，则该三挠 flex 在短 Weierstrass 三次模型上的切线水平，所以 $x^3+Ax+B-y(P)^2=(x-x(P))^3$，迫 $x(P)=A=0$。在一般 $j\ne0$ 曲线上不发生。原分量 $X(3)\simeq\mathbf P^1$ 的 $\omega$ 次数一，故 $H^0(\omega)$ 仅有两维；以上两特征已经占尽。

预合 $c:a\mapsto\bar a$ 把另一 Weil 配对分量的 $f_3$ 拉回原分量，因 $c$ 的模3行列式为 $-1$。被拉回的(Z1)经 $a\mapsto\bar a$ 重编后，其理想方向角色为 $\epsilon_0\circ c$，在 $\omega$ 上的特征为 $\omega$。这个特征在 $H^0(\omega)$ 缺失，故
$$ f_3|_{X(3)^{\rm opp}}=0.\tag{AA1} $$
(Z2)作为不依分量的七同源生成元迹仍成立，130模3为1，所以每个 $G_C$ 以及两条 $f_b$ 都在相反分量全零。原 $p\equiv-1\bmod3$ 的奇数 $s$ 对实际 $q_D:E_1\to E_1/D$ 有 $e_3(q_DP,q_DQ)=e_3(P,Q)^{p^s}=e_3(P,Q)^{-1}$。因此用未经重标的原水平、原归一微分逐个确有
$$ F_{b,D}=0\qquad(|D|=p^s,\ s\text{ 奇},\ b=65,8125). \tag{AA2} $$
$F_{1,D}$ 的三处角色不同，(AA2)没有赋给参考。K2的预标 $\alpha M^{-1}$ 在另一分量，目标 $q_D\alpha M^{-1}$ 回到原非零分量，故 K2 仍是全部非零分量截面值间的加性迹等式。

## 19. 整个三级同源胚芽及原首层完整单位范数

沿(Z1)–(Z5),(K1)–(K4)。记 $v=v(w)$，$\mathcal F_C(w)=P(v)G_C(v)$，$\mathcal D_C(w)=P(v)^{12}\Delta(E_v/C,\kappa_C)$，并以 $C=0$ 表示未取130商的源。每个商微分由 $q_C^*\kappa_C=\omega(v)$ 固定。置 $d_C=\mathcal D_C/\mathcal D_0,\ u_C=\mathcal F_C/\mathcal F_0$；在中心与(Z5)一致。

取三级标记的核 $D_\delta=\alpha_3(\mathbf F_3\delta)$。其商在中央经 $[\delta]$ 标回 $E_1$，并以此中央标记在特征零形式邻域延拓原 prime-to-3 的130水平。$q_\delta\alpha_{130}=\alpha'_{130}[\delta]$，因为已在中心相等且水平为有限 étale。新的三级标记用原中央 $\alpha_3$ 在目标形变唯一延拓，此处并不求 $\delta$ 模3的逆。水平 cohomology 上 $q_\delta^*e'_0=\delta e_0,\ q_\delta^*e'_1=\bar\delta e_1$，由中心 CM 和连接自然性。于是 $w'=(\delta/\bar\delta)w=-w$，$q_\delta^*\omega(v')=[\delta P(v')/P(v)]\omega(v)$。先取 $C$ 再取三级核与先取三级核再取 $\delta C$ 相同；对原归一微分所生因子仍为 $\delta P(v')/P(v)$。故(Z4)在整个胚芽准确给
$$ \mathcal F_C(w)^{24}=2^{48}3^{12}\delta^{36}
              \frac{\mathcal D_{\delta C}(-w)^3}{\mathcal D_C(w)},\qquad
 u_C(w)^{24}=\frac{d_{\delta C}(-w)^3}{d_C(w)} .\tag{AB1}$$
$\delta^2=-3$ 在130标记上为射影标量，故 $S:(C,w)\mapsto(\delta C,-w)$ 满足 $S^2=1$，$(3S-I)^{-1}=(3S+I)/8$。可逐项应用于归一单位的局部对数或对数微分，得到完整各阶身份。

任意椭圆曲线及微分的全部 $p$ 商有准确范数
$$\prod_{|D|=p}\Delta(E/D,\kappa_D)=p^{12}\Delta(E,\kappa)^{p+1}.\tag{AB2}$$
在复格 $\mathbf Z+\mathbf Z\tau$，各超格分别为 $p^{-1}(\mathbf Z+\mathbf Z p\tau)$ 及 $\mathbf Z+\mathbf Z((\tau+j)/p)$、$0\le j<p$。前一项的微分尺度给 $p^{12}\Delta(p\tau)$；其余乘积按 $\Delta=q\prod(1-q^m)^{24}$，区分 $p\mid m$ 与否，得 $\Delta(\tau)^{p+1}/\Delta(p\tau)$，首 $q^{1/p}$ 的 $p$ 次相位乘积为1。任意微分的两边同权，故也在代数族成立。令 $M$ 为 $E_1$ 特殊 Frobenius 在原 prime-to-$p$ 水平的实际可逆矩阵。在(K2)全部 $p$ 支目标处写 $w'_i$ 及其真正形变点 $v_i$；相同 $w'_i=A/(Bw)$ 可有不同逆像，以下函数按各自 $v_i$ 评值。源预标为 $\alpha M^{-1}$，目标标记均在原分量。将130与$p$商方形交换，目标的 $C$ 在源恰为 $M^{-1}C$。取(AB2)在该130商和原源上的比，共同 $p^{12}$ 及各临时微分准确相消，得
$$ \prod_i d_C(v_i(w))=d_{M^{-1}C}(w)^d,\qquad d=p+1.\tag{AB3}$$
其中 $w=0$ 取完整首圈。对分子也可完全不比较三级标记的逆：由(Z4)直接相除，任一原分量上 $u_C^{24}$ 是 $\Delta(E/C/D_\delta)/\Delta(E/D_\delta)$ 的三次方除以 $\Delta(E/C)/\Delta(E)$，四个微分全自源归一。$M$ 保持三级根基线 $\mathbf F_3\delta$，因为 $M$ 为可逆半线性，乘单位及共轭都保存该线。于是在全部 $p$ 商上分别对四个实际鉴别式用(AB2)，共同的 $p^{12}$ 全消，源的130线改为 $M^{-1}C$，而三级核仍为 $D_\delta$。最后才在原分量源上用(Z4)把该比认回 $u_{M^{-1}C}^{24}$。等价地，$(C,w)\mapsto(\delta C,-w)$ 交换整套$p$线且 $M^{-1}\delta C=\delta M^{-1}C$，因为 $\bar\delta=-\delta$。准确得到
$$ \boxed{\prod_i u_C(v_i(w))^{24}=u_{M^{-1}C}(w)^{24d}.} \tag{AB4}$$
等式始终在预标后目标的原 Weil 分量使用 $f_3$；跨分量使用的是鉴别式的(AB2)。中心取 $p$ 进对数即 $\sum_i\log_p u_C(v_i)=d\log_p u_{M^{-1}C}(0)$，所以(U6)的全部独立72个对数也由同一第一层的真单位迹恢复。
