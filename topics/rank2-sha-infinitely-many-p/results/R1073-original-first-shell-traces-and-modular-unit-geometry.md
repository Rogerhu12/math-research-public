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
