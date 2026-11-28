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

## 20. 固定Fermat曲线的真实混积微分与非挠首端点

沿(AB1)并允许 $C=0$ 表示原源。对 $C\ne0$ 置 $N_C=130$，$N_0=1$。给原 $X(3)$ 分量选 Hesse 坐标 $\lambda$，令原 $f_3$ 唯一零尖点 $c_0=\infty$，与它同为三级幺幂 deck 不动点的原 CM 点为0，其余三尖点为 $\mu_3$。剩余三重旋转以下精确定标。该坐标的遗忘映射是
$$ j(\lambda)=27\,\frac{\lambda^3(\lambda^3+8)^3}{(\lambda^3-1)^3}.\tag{AC1}$$
例如 Hesse 三次 $x^3+y^3+z^3-3\lambda xyz=0$ 的九个恒定 flex 给全三级标记，四个退化点即上述四尖点；换 Weierstrass 方程系数可取 $-27\lambda(\lambda^3+8),54(\lambda^6-20\lambda^3-8)$，代标准 $j$ 即(AC1)。利用 deck 把选定的尖点转到无穷，固定该尖点的幺幂的另一个不动点对应0。该 Hesse 公式亦见 [Hesse pencil 的显式 Weierstrass 模型](https://doi.org/10.1016/j.jaca.2026.100043)；亦见 Artebani–Dolgachev [§2，(6)–(8)](https://sites.lsa.umich.edu/idolga-new/wp-content/uploads/sites/1467/2024/08/hesse09.pdf)。

原 $j(E_v)=1728\cdot4v^3/(4v^3+27)$ 与 $w=v/6+\cdots$ 给 $(d\lambda/dw)(0)^3=-4$，故可唯一选择 $\mu_3$ 旋转使此导数为原 $x(Q_3)$。这时(Z3)的 $f_3(0)^2=432x(Q_3)$。权二的 Kodaira–Spencer 像在 $X(3)$ 上为对数微分；$f_3^2$ 的零部为 $2[c_0]$，故对应通常亚纯微分的除子为 $[c_0]-\sum_{a\in\mu_3}[a]$，即 $d\lambda/(1-\lambda^3)$ 的除子。在一个水平基中 $\mathrm{KS}(\kappa^2)$ 为 $h^2\,dw$ 乘该基同一固定 cup 常数。在中央用刚定的导数与(Z3)标定比例；在 $C$ 商上拉回时 cup 要乘 $N_C$，而归一 $\kappa_C$ 拉回等于源微分。由此逐支准确得到
$$ \mathcal F_C(w)^2dw=432N_C\,\frac{d\lambda_C}{1-\lambda_C^3},
 \qquad \lambda_C=\lambda(E_v/C,q_C\alpha_3).\tag{AC2}$$
换言之 $\langle\omega_C,\nabla\omega_C\rangle$ 拉回为源值除 $N_C$，而 $\mathcal F_C^2dw=P^2G_C^2dw$，故右侧确为乘 $N_C$。单支平方原函数等于 $-144N_C\sum_{a\in\mu_3}a\log(\lambda_C-a)$，按同一基点取差。

写 $r_C=\mathcal F_{\delta C}(-w)/\mathcal F_C(w)$。由真正母三级同源的微分，
$$ \frac{\mathcal D_C(w)}{\mathcal D_{\delta C}(-w)}
 =\delta^{12}\frac{\Delta(E_v/C,\kappa_C)}
 {\Delta((E_v/C)/D_\delta,\kappa_{C,\delta})}
 =(1-\lambda_C^3)^2.\tag{AC3}$$
最后一步作用在单个普适三级曲线上：左边此模函数在 $c_0$ 有六阶极，在其余三尖点各有二阶零，且在原 $E_1$ 中取1，所以与右边完全相等。交换(AB1)的两侧标签给 $r_C^{24}=(1-\lambda_C^3)^8$。因此整个胚芽中 $e_C=(1-\lambda_C^3)/r_C^3$ 是由中央值确定的常数、属于 $\mu_8$；令 $\beta_C=e_C^3$，这是 $\mu_8$ 中使 $\beta_C^3=e_C$ 的唯一选择。置 $\mu_C=\beta_C r_C$，则
$$ \lambda_C^3+\mu_C^3=1,\qquad
 \mathcal F_C(w)\mathcal F_{\delta C}(-w)\,dw
 =432N_C\beta_C^{-1}\frac{d\lambda_C}{\mu_C^2}. \tag{AC4}$$
在首个闭盘内 $\mu_C$ 也可直接按 $\mu_C^3=1-\lambda_C^3$ 及其中央值整 étale 延拓；所有商皆非尖点且好约化，右侧在整个剩余盘是单位。故(AC4)在 $w=\infty$ 的首圈端点也以 $v$ 的正则微分解释。

Fermat 曲线 $\mathcal E:X^3+Y^3=1$ 以 $[1:-1:0]$ 为原点。先取 $x=12/(X+Y),\,y=36(X-Y)/(X+Y)$ 得 $y^2=x^3-432$；再取 $x'=x/\delta^2,\ y'=y/\delta^3$，因 $\delta^6=-27$ 得 $E_{16}:y'^2=x'^3+16$，是 $K$ 上的同构。它将 $\omega_{16}=dx'/(2y')$ 拉回为 $\delta\,dX/(6Y^2)$。因此(AC4)右侧为 $2592N_C(\delta\beta_C)^{-1}\omega_{16}$ 的拉回。$E_{16}$ 与 $y^2+y=x^3$ 由 $x'=4x,\ y'=8y+4$ 同构；其 CM Hecke 角色为(Z1)的 $\psi_0$。也可直接查 $E_{16}[3]\subset E_{16}(K)$（三挠的 $x=0$ 或 $x^3=-64$），故每个好主理想的 Frobenius 生成元模3为1，而该生成元唯一。特别 $n>0,\ n\equiv1\bmod6$ 时 $\psi_0((n))=n$。

### 原216标签与实际首圈端点的非挠

记 $P_C=(\lambda_C(0),\mu_C(0))\in\mathcal E(\overline K)$。对 $\gcd(n,130)=1,\ n\equiv1\bmod6$，主理想 $(n)$ 的 Artin 作用固定该点。事实上在 $E_1$ 的3挠上 $\psi_1((n))=n$ 为1，而在所有130射影线上为标量；所以固定 $\lambda_C(0)$。在原环类单位 $u_{\delta C}/u_C=r_C(0)$ 中亦固定。其作用在 $\mu_8$ 上为 $n^2\equiv1\bmod8$，故固定 $\beta_C$。若 $P_C$ 为 $m$ 挠，进一步选 $(n,m)=1$，$E_{16}$ 的 CM 角色给 $(n-1)P_C=0$。用 CRT 使任何 $\ell\ge5$ 的指定 $\ell\mid m$ 上 $n\bmod\ell$ 非0非1；使 $v_2(n-1)=1$ 或 $v_3(n-1)=1$；均可保持其余互素条件。故 $m\mid6$。但 $K(E_{16}[6])/K$ 在5与13不分歧，而 (AC1) 的 $j(E_1/C)\in K(P_C)$ 生成130环类域；原 $\mathrm{Pic}(\mathcal O_{130})$ 的局部5、13环面像具有非平凡惯性（最大序类数1，对角 $\mu_3$ 在2环面上已自由，故5和13因子仍分别嵌入）。于是对所有 $N_C=130$ 均得到 $P_C$ 非挠。

对(W8)任一端点 $v_D$ 令 $P_{C,D}=(\lambda_C(v_D),\mu_C(v_D))$。它与 $P_C$ 同约化。前者的 $j$ 来自 $E_1/(D\oplus M^{-1}C)$ 的乘子环 $\mathcal O_{130p}$，后者为 $\mathcal O_{130}$，故两点不同。若差为 $m$ 挠，对额外素于 $130pm$ 的上述主理想 $(n)$，两点的 $\lambda$ 坐标均由其固定：原 $q_D$ 及130核在有理标量下不动，Fr 重标是固定的标签矩阵，3挠不动。因 $\mu_3\subset K$，三个相同 Artin 作用至少固定两点的 $\mu$ 坐标（可在整个阿贝尔 torsion compositum 及所需代数闭包取 lift；$\lambda$ 固定且 $\mu^3=1-\lambda^3$ 已足）。故 $m\mid n^3-1$。对各 $\ell\ge5$ 取非零模 $\ell$ 的 $n$ 使 $n^3\ne1$，总可兼顾其余互素条件。$m$ 于是素于 $p$，而同约化两点之差不可能是非零 prime-to-$p$ 挠点。由此
$$\boxed{
 \int_{0}^{v_D}\mathcal F_C(w)\mathcal F_{\delta C}(-w)\,dw
 =\frac{2592N_C}{\delta\beta_C}\,
   \log_{E_{16}}\!\left(P_{C,D}-P_C\right)\ne0.} \tag{AC5}$$
等式中把 Fermat 点经上式送 $E_{16}$，以 $\omega_{16}$ 的正式对数取值。两点落在同一剩余盘，故普通原函数差等于该正式对数。这里所有非挠断言均逐个实际 $C,D$；固定 $\chi_b$ 的代数线性组合和(W8)的完整权一二重积分尚需另证。

## 21. 两个原角色首圈分部积分中的真实有限椭圆端项非零

设 $d=p+1,h=130p$，$p\equiv5\bmod6$。沿(AB1),(AC1)–(AC5)。记
$$ K_C=\frac{2592\cdot130}{\delta\beta_C},\quad
 h_C(w)=\frac{1}{w\mathcal F_{\delta C}(-w)},\quad
 j_C(v)=\log_{E_{16}}(P_C(v)-P_C(0)). \tag{AD1}$$
此 $j_C$ 是固定 Fermat 模型的正规椭圆对数，不是此前原 Rubin 的 $j_m$。首圈所在稍大闭盘内各点都在同一好约化剩余盘，故这是真解析原函数。由(AC4)，
$\mathcal F_C\,d\log w=K_Ch_C\,dj_C$。$h_C$ 只在 $v=0$ 有一阶极：用母三级同源的 $a_\delta=q_\delta^*\omega(v')/\omega(v)$ 写成
$6\delta/[vQ(v)a_\delta(v)G_{\delta C}(v')]$。其中 $Q$ 无零，两个同源素于 $p$，$G_{\delta C}$ 是原分量非尖点的单位。故 $h_Cj_C$ 处处正则，在零的值是 $\mathcal F_C(0)/K_C$。

### 端点的全部微分与实际射影标签

令 $M$ 是(K2)实际特殊 Frobenius 的 prime-to-$p$ 标记矩阵。将原标签 $(C,D)$ 送 $I=(M^{-1}C,D)$，这是 $E_1[h]$ 中原130开循环加上一个 $p$ 线。设
$$ F_I=f_3(E_1/I,q_I\alpha_3 M_3^{-1},\kappa_I),\qquad q_I^*\kappa_I=\omega_E.$$
原 $\alpha_3$ 的参数自始取定；$h\equiv-1\bmod3$，加 $M_3^{-1}$ 后确在原 Weil 分量，故值均非零。令 $a_D=q_D^*\omega(v_D)/\omega_E$。逐同源复合给 $F_I=a_D G_C(v_D)$。

母 $\delta$ 同源在 $v_D$ 处的标记满足
$q_{\delta,v_D}\circ q_D=q_{\delta D}\circ[-\delta]$，采用右边的归一商同构来识别。两边核相同，右边的特殊纤维为 $\mathrm{Fr}[-\delta]=[\delta]\mathrm{Fr}$，正好是左边的特殊标记；prime-to-$p$ 三级标记在该目标约化已固定，有限 étale 性给同一延拓。130线上 $\delta,-\delta$ 的射影像相同，且 $M^{-1}\delta C=\delta M^{-1}C$。微分因而有
$a_\delta(v_D)a_D=-\delta a_{\delta D}$。在(K2)的记号 $q_D^* e'_1=B e_0$（$B$ 是对所有核线相同的非零 crystalline 常数），从(W8)首圈 $P=0$ 得 $a_D=B\,v_D Q(v_D)/6$。所以
$$ h_C(v_D)=-B/F_{\delta I},\qquad
 r_C(v_D)=-F_{\delta I}/F_I,\qquad
 P_{C,D}=(\lambda_I,-\beta_C F_{\delta I}/F_I).
 \tag{AD2}$$
$\lambda_I$ 用上述实际三级标记评价。全 $\mu_3$ 原物理轨道并未删除。确实 $\mathcal F_{uC}(u^2w)=\mathcal F_C(w)$，(AC2)和三级 deck 给 $\lambda_{uC}(u^2w)=u^2\lambda_C(w)$，而 $\beta,\mu$ 不变。Fermat 自同构 $(X,Y)\mapsto(u^2X,Y)$ 在差点上为 $[u^2]$（其原点平移为3挠，微分为 $u^2$）。在首圈源核的相应置换是 $D\mapsto\bar uD$，这是 $\mathrm{Fr}\,a=\bar a\,\mathrm{Fr}$ 的反转。因 $h_{uC}(u^2w)=u^{-2}h_C(w)$，(AD1)端点的 $K_Ch_Cj_C$ 恰在这些三元轨道恒等。删去 $h_C$ 的裸椭圆对数全轨道和反而为零。

因此在 $I_2$ 处选固定一条线，等价于在原 $C_2=M_2I_2$ 处取固定线。其余自由标签构成
$$ H_h=T_5\times T_{13}\times T_p,\qquad
 |H_h|=6\cdot12\cdot(p+1),$$
其中前两项与(Z2)相同，$T_p=\mathbf F_{p^2}^\times/\mathbf F_p^\times$。后续回到原完整216时取三份这些代表。要求 CM Artin 元在模24上为1，可由 CRT 仍遍取此群的全部平移：选 $\alpha\in\mathcal O_K$ 模24为1，模 $5,13,p$ 取任意给定单位剩余，理想 $(\alpha)$ 的 $\psi_1$ 矫正因子为1（$\mathfrak f_1=2\delta$）。所以 $\alpha_3,\mu_8$ 均不动。在原中心 $r_C(0)=u_{\delta C}/u_C$、$\lambda_C(0)$ 真按 $C$ 平移，故 $\beta_C$ 在选定2线的全部代表上同一。由(AD2)实际 $P_I:=P_{C,D}$ 也按 $I$ 作纯平移，先固定 $M_3$ 再运输 $q_I\alpha_3 M_3^{-1}$。旧点 $P_C$ 在同一类 Artin 作用下仍在旧点集合中；$T_p$ 的单独平移可选模 $24\cdot5\cdot13$ 为1，固定所有旧点。

### 归一真实三级值的倒数在唯一环类呈指数主项

取原复格 $\varpi_1\mathcal O_K$。商格为 $(\varpi_1/h)L_I$，$L_I=h\mathcal O_K+\mathbf Z v_I$，$v_I\bmod h$ 处处单位，余线类型固定。选最短非零 $\alpha\in L_I$ 并补成缩减格基 $\alpha,\gamma$。$\tau=\gamma/\alpha$ 属标准基本域，且 $\operatorname{Im}\tau=\sqrt3 h/(2N\alpha)$，$N\alpha\le h$ 由 $\operatorname{Im}\tau\ge\sqrt3/2$。$\alpha\bmod3$ 非零，因为 $h$ 与3互素，若 $\alpha/3\in\mathcal O_K$ 则也在 $L_I$，与最短矛盾。在此基的 Tate 尖点处，原三级标记的乘法线为 $M_3\langle\alpha\bmod3\rangle$：在 $L_I/3$ 上标签 $a$ 对应 $h M_3^{-1}a$，短基标出乘法方向。$M_3$ 保持根基线 $\mathbf F_3\delta$，所以该尖点为 $c_0$ 当且仅当 $\delta\mid\alpha$。

在有限多三级标记的基本域上，(Z3)以后的除子计算给一致复估计。在 $c_0$ 的首 Fourier 项是非零常数乘 $e^{2\pi i\tau/3}$，其余尖点的首项为非零常数；在基本域紧部没有零。因此在 $c_0$ 型
$$ |1/F_I|\asymp \frac{|\alpha|}{h}
 \exp\!\left(\frac{\pi\sqrt3 h}{3N\alpha}\right),$$
在其余型 $|1/F_I|\ll |\alpha|/h$。各常数与 $p,I$ 无关：标记变化及 $M_3$ 只在有限群中，$|\varpi_1|$ 已纳入常数，微分的尺度为 $|\varpi_1\alpha|/h$。

$c_0$ 型最小可能 $N\alpha=3$，恰由 $\alpha=u\delta,\ u\in\mu_6$ 给出。因 $\delta$ 为模 $h$ 单位，只属于唯一射影标签，六个全局单位在 $H_h$ 恰为同一类（固定二线得到唯一代表）。该格确以 $\delta$ 某单位倍为最短：若有范数1单位亦落其中，其与 $\delta$ 的基行列式须为 $h$ 的整数倍，但其绝对值至多2且非0。其他 $c_0$ 型均 $N\alpha\ge4$。故唯一项下界为 $c h^{-1}\exp(\pi\sqrt3 h/9)$，全体余项上界为 $O(h^{1/2}\exp(\pi\sqrt3 h/12))$，已包含 $|H_h|=O(h)$ 项。对充分大 $p$，该项严格压倒所有余项绝对值之和。平移 $I\mapsto\delta I$ 或对各项乘任意根单位不改变此优势。特别对于任一原 $b$，有限向量
$$ b_I=\chi_b(C)^{-1}\beta_C^{-1}/F_{\delta I}\quad(I=(M^{-1}C,D))
 \tag{AD3}$$
在 $\mathbf C[H_h]$ 的所有角色上的 Fourier 系数均非零。这是代数非零，故每个 $p$ 进嵌入也保留。

### 对真实有限端项的非零与它在原二阶中的位置

在 $E_{16}(\overline K)\otimes_{\mathbf Z}\mathbf Q$ 的 $K$ 向量空间中除去全部旧 $P_C$ 的 $K$ 跨度。$P_I$ 模此跨度并非全零。事实上固定同一 $C$、令 $D_1\ne D_2$，对应两 $j$ 环类不同（固定二线已去掉单位重复），两点同约化。按(AC5)的主理想三次论证，若其差为挠点，阶只含2和3，故同约化将迫两点相等，矛盾。单独 $T_p$ 平移固定所有旧点并移动这些 $P_I$，所以至少一个新像非零。由前述真实 Artin 移动，正则表示 $K[H_h]$ 到这些新像跨度的映射具有平移不变的核（先在实际点上作用，再扩标量，不对指数系数作 Galois 共轭）。

固定非阿基米德代数嵌入，Fuchs–Pham 的椭圆对数线性独立定理说明 $K$ 上无关的 $E_{16}$ 代数点模挠之对数，在 $\overline{\mathbf Q}$ 上仍线性无关。可把全有限点集取同一整数倍进入足够小的正式盘，$K=\operatorname{End}^0(E_{16})$。因此若 $\sum_I b_I\log_{E_{16}}(P_I-P_{C(I)})=0$，则在上述新像的 $\overline{\mathbf Q}$ 扩标量中系数向量 (AD3) 属于关系核。其每个 Fourier 分量非零，故其所有纯平移张成整个正则表示，将迫全部新像零，矛盾。乘回(AD2)的非零公共 $B$、$K_C$ 的共同有理部分及三元轨道数，得到对两个原角色均有
$$ \boxed{\,L_b^{\rm end}:=
 \sum_{C\in\mathcal C,D}\chi_b(C)^{-1}K_C h_C(v_D)j_C(v_D)\ne0
 \quad(p\text{ 充分大且惰性}).\,}\tag{AD4}$$
定理原文 Fuchs–Pham, *Some applications of the p-adic analytic subgroup theorem*, [Theorem 2.1](https://web.math.pmf.unizg.hr/glasnik/51.2/51(2)-04.pdf)。

末将端项放回原(W8)。令 $A_b(s)$ 为 (AD4) 的同一全和，但端点改为 $v=\pi X(Y)$ 的全部 $Y^d=-s/\kappa$；令 $B_b(s)$ 为这些端点下从0出发的 $\int\sum_C\chi_b(C)^{-1} K_C j_C\,dh_C$ 的全和。两个函数均过收敛，因为后一个微分在0的留数是 $-\sum\chi_b^{-1}G_C(0)=0$，其余点正则；前一和在0的值也由同一原零质量消去。逐项分部积分准确为 $I_{f_b}(s)=A_b(s)-B_b(s)$。特别
$$ A_b(0)=B_b(0)=0,\qquad A_b(1)=B_b(1)=L_b^{\rm end}\ne0 .\tag{AD5}$$
若 $\Theta=ds/s+d\,ds/(1-s)$，实际二阶标量仍为
$$65 f_1(0)(d\log\rho)^2[T^2]\mathcal A_b
 =-\int_0^1(A_b(s)-sL_b^{\rm end})\Theta
  +\int_0^1(B_b(s)-sL_b^{\rm end})\Theta .\tag{AD6}$$
(AD5)使两个被积函数分别正则。有限代数点的原端项已被直接证明非零，同时也证明包含移动权 $dh_C$ 的整项在首端确实不能删除；(AD6)中两次正则积分的差尚未因此决定。

## 22. 母三同源的绝对三级相位与完整二阶积分的真实反演

在原全九级分量把 $\alpha_9(a)=[a]Q_9$ 固定得和 $\alpha_3$ 相容。对母 $\delta$ 同源，目标的实际三级标记可标为
$$ a\longmapsto q_\delta\alpha_9(\bar\delta a)\qquad(a\in\mathcal O_K/3). \tag{AE1}$$
改变 $a$ 一个 $3b$ 时所差点在 $D_\delta$。在原中央 $[\delta][\bar\delta]=[3]$ 给出原 $\alpha_3$，故该有限 étale 三级标记在整个连通分量是同构。目标的根基线是对偶三级核，因为在中央对应 $E_1[\delta]$。因此在 $X_0(3)$ 上此三级商正给 Atkin–Lehner 反演。坐标 $1-\lambda^3$ 的零、极是其两个尖点，在上述固定 CM 点取1，所以该反演把 $1-\lambda^3$ 送其倒数。

由(AC3)和原母同源微分，$r_C$ 可在 $E_C=E_v/C$ 本身写成
$$ r_C=\delta^{-1}\,
 \frac{ f_3(E_C/D_\delta,q_\delta\alpha_{9,C}(\bar\delta\,\cdot),\kappa_{C,\delta})}
 {f_3(E_C,\alpha_{3,C},\kappa_C)} .\tag{AE2}$$
这是给定的全九级分量上的模函数。对 $N_C=130$，取 $\alpha_{9,C}=q_C\alpha_9\circ[4]$，因为 $130\cdot4^2\equiv1\bmod9$，此标记与源在同一 Weil 分量。$4\equiv1\bmod3$ 使目标分母的三级标记不变，而 $q_\delta\alpha_{9,C}(3\bar\delta a)=0$ 使分子的实际三级标记也不变。对 $N_C=1$ 用原 $\alpha_9$。在这个连通 $X(9)$ 分量，(AC3)给 $e=(1-\lambda^3)/r^3\in\mu_8$，所以 $e$ 为常数，代原 $E_1$ 时 $\lambda=0,r=1$。因此确有
$$ \beta_C=1,\qquad\mu_C=r_C=\mathcal F_{\delta C}(-w)/\mathcal F_C(w)
 \qquad( N_C=1,130 ).\tag{AE3}$$
在(AC4),(AD1)的 $K_C$ 因而正是 $2592N_C/\delta$。

因 $(1-\lambda_{\delta C}(-w)^3)=(1-\lambda_C^3)^{-1}$，且 $r_{\delta C}(-w)=r_C^{-1}$，所以 $\lambda_{\delta C}(-w)=-\zeta\lambda_C/\mu_C$，$\zeta\in\mu_3$。Fermat 微分在 $(X,Y)\mapsto(-\zeta X/Y,1/Y)$ 下乘 $-\zeta$，而在(AC4)两源交换、$w\mapsto-w$ 后原微分仅乘 $-1$；因此 $\zeta=1$。得到真正的同一反演
$$ P_{\delta C}(-w)=(-\lambda_C/\mu_C,1/\mu_C),\quad
 j_{\delta C}(-w)=-j_C(w),\quad
 h_{\delta C}(-w)=-\mu_C(w)h_C(w). \tag{AE4}$$
椭圆曲线的原点平移在差点中相消。首圈母三级同源给 $Y\mapsto -Y$：其在 $w$ 上为负，在 $Y=0$ 的解支由(W1),(W2)唯一，然后沿原稍大闭盘延拓。故每个径向全和都保持这个变换；不能在单个奇层核上擅设符号。

令 $\varepsilon_b=\chi_b(\delta)$，两条原曲线各为 $-1,+1$。在(AD5)两项中保留原 $\chi_b(C)^{-1}$，用(AE4)把相互成对的 $C,\delta C$ 合并，正好可以将 $h_C$ 换为
$$ H_{C,\varepsilon_b}=\tfrac12(1+\varepsilon_b\mu_C)\,h_C,\qquad
 dH_{C,\varepsilon_b}
 =\tfrac12\left((1+\varepsilon_b\mu_C)\,dh_C+
                    \varepsilon_b h_C\,d\mu_C\right). \tag{AE5}$$
第一项为径向全和 $\sum_C\chi_b^{-1}K_C H_{C,\varepsilon_b}j_C$，第二项为 $\sum\int\sum_C\chi_b^{-1}K_C j_C\,dH_{C,\varepsilon_b}$。代回(AD6)仍完全相等，特别两项在首端点各自的非零值不改变。后式最后的 $d\mu_C$ 来自真实移动的三级商。

这一反演也给固定商坐标
$$ X_0=\lambda_C/(1-\mu_C),\quad Z=(1+\mu_C)/(1-\mu_C),\quad
  3Z^2=4X_0^3-1,\qquad (X_0,Z)\longmapsto(X_0,-Z). \tag{AE6}$$
由 $d\mu=-\lambda^2 d\lambda/\mu^2$ 微分 $X_0$ 得 $dX_0/d\lambda=-Z/\mu^2$，故
$$ d\lambda_C/\mu_C^2=-dX_0/Z. \tag{AE7}$$
置 $b_C=w\mathcal F_C$, $\mathcal G=b_C(1-\mu_C)$；$\mathcal G$ 在整 $(C,w)$ 反演下不变。于是
$$ H_{C,+}=\frac{3Z}{2(X_0^3-1)\mathcal G},\qquad
 H_{C,-}=\frac{3}{2(X_0^3-1)\mathcal G}.\tag{AE8}$$
直接代入 $b_C=(Z+1)\mathcal G/2$ 和 $Z^2-1=4(X_0^3-1)/3$ 即可。由此正号积分 $H_{C,+}dj_C$ 的椭圆平方根 $Z$ 消去，负号留下一个 $1/Z$。两者都保留同一移动的 Hesse 水平周期 $\mathcal G$，(AD6)所需两整积分的比较仍待支付。

## 23. 实际首圈的负一权及固定椭圆有理函数的四位 Gauss 和

沿本R1073原先规定的充分大好惰性素数及全部固定有限排除集，保留(P9),(Q1),(R1),(W8),(K1)及(AD2)的全部标记。这里 $d=p+1,q=p^2$，$B_0(v)=vQ(v)/6$，$w=B_0/P$，$B$ 单独表示原晶体反对角常数 $q_D^*e'_1=B e_0$，$\rho_t=t/\bar t$，$\rho=\rho_\eta$。由(Q1)的真实水平作用在原首闭盘先得
$$ B_0(v)(\mathcal T_t f)(v)=\rho_t^{-1}(B_0f)(\Phi_t(v)).\tag{AF1}$$
等式只须在 $w$ 有限处以 $w(\Phi_t v)=\rho_t w(v)$、$P(v)\mathcal T_t f(v)=(Pf)(\Phi_t v)$ 验证，再在整盘延拓；$\Phi_t$ 整且固定0，保此盘。$P(v_D)=0$ 的全部 $d$ 个首圈点已由(W8)实辨。其标记下 $\Phi_t(v_D)=v_{\bar tD}$：准典提升的态射由源的 $[\bar t]$ 经 $q_D$ 下降，特殊纤维 $\mathrm{Fr}\,[\bar t]=[t]\mathrm{Fr}$，按(P7)的刚性它正是所标 $U_t$。这里只用 $p$ 可除群的同构。特别 $\eta$ 固定每个 $D$，Teich 商 $\Delta=\mu_{q-1}/\mu_{p-1}$ 正则置换全部首线。

置 $F^{\rm corr}_{k,D}=f_k(E_1/D,q_D\alpha M^{-1},\kappa_D)$，$q_D^*\kappa_D=\omega_E$；$M$ 是原特殊 Frobenius 在 $c_k$ 水平上的实际矩阵。于是 $F^{\rm corr}_{k,D}=a_D f_k(v_D)=B(B_0f_k)(v_D)$。取任意基线 $D_*$，在(P9)应用(AF1)，给真确的固定负一权
$$ \mathscr S_{k,p}=\sum_{t\in\Delta}\rho_t^{-1} F^{\rm corr}_{k,\bar tD_*},
 \qquad \boxed{\mathscr S_{b,p}=65\,\mathcal A_b(\rho^{-1}-1)\mathscr S_{1,p}.} \tag{AF2}$$
换 $D_*$ 只同时改变三个和的同一单位相位。确实 $B_0P_\Delta f$ 在 $v_D$ 取得 $(dB)^{-1}$ 倍该和，每个 $\mathcal T_\eta-I$ 在这一点对 $B_0 f$ 作标量 $\rho^{-1}-1$；严格盘上的有界收敛允许整 $\mathcal A_b$ 逐项作用。

参考和准确满足 $v_p(\mathscr S_{1,p})=1/d$。因 $\Phi_t'(0)=\rho_t$、$\Phi_t$ 整、$v_p(v_D)=1/d$，有 $v_{\bar tD}/v_D\equiv\rho_t\bmod\mathfrak m$；(R5)给 $B_0(v_D)/v_D\equiv1/6$，而 $f_1(v_D)\equiv f_1(0)\ne0\bmod\mathfrak m$。所以 $\mathscr S_{1,p}/(B v_{D_*})\equiv d f_1(0)/6$。又 $v_p(a_D)=1/d$ 是(P6)的首层，故 $B=a_D/B_0(v_D)$ 是单位。这付掉全部样本、参考和相位可能的分母。

### 原物理曲线上一个固定真有理函数

任取非零 $Q_*\in D_*$。为各 $k=1,65,8125$ 写 $c_1=6,c_b=390$，$Q_{c_k}$ 如(A)。因为模 $c_k$ 的 $M^{-1}$ 是反线性的可逆映射，存在唯一 $m_{k,p}\in(\mathcal O_K/c_k)^\times$ 使 $M^{-1}a=m_{k,p}\bar a$。置
$$\begin{aligned}
 \widetilde G_k(X)&=\sum_{a\in(\mathcal O_K/c_k)^\times}\epsilon_k(\bar a)^{-1}
          F_7(X+[a]Q_{c_k}),\\
 \lambda_{k,p}&=\epsilon_k(\bar m_{k,p}).
\end{aligned}\tag{AF3}$$
这三个 $\widetilde G_k$ 都固定且保留原 $2,3,5$ 及两个 $13$；$\lambda_{k,p}$ 是明确由原 Frobenius 重标产生的根单位。由(P2)及上述换标逐项有 $F^{\rm corr}_{k,D}=\lambda_{k,p}\sum_{R\in D}\widetilde G_k(R)$。当 $h=\bar t$ 时 $\rho_t^{-1}=\rho_h$；零点在全和的系数是非平凡角色之和，故为零。每条线的 $p-1$ 个非零点均应计入，各点权相同。于是
$$ \boxed{\mathscr S_{k,p}=\lambda_{k,p}
   \sum_{h\in\mathbf F_{p^2}^\times}[h]_{\rm T}^{\,1-p}
                       \widetilde G_k([h]Q_*) .}\tag{AF4}$$
$[h]_{\rm T}$ 为其 Teich 提升，点上的 $[h]$ 是原 CM 模 $p$ 作用。$\widetilde G_k$ 在原点形式盘整，由(A)的固定水平极与好约化论证；其 $\mu_6$ 变换是 $\widetilde G_k([u]X)=u^{-2}\widetilde G_k(X)$，因为 $\epsilon_k(u)=u^{-1}$。特别三个源在物理原点本身均零，秩零参考的首圈非零由(AF2)付出。

取 R663/R1065 在**物理** $E_1$ 上的严格整坐标 $Z$，$[-p](Z)=-pZ+Z^q$、$[u](Z)=uZ$ 对 $u\in\mu_{q-1}$，令 $z_*=Z(Q_*)$，$z_*^{q-1}=p$。写 $g_{k,n}=[Z^n]\widetilde G_k$，均整。完整有限 Fourier 正交性将(AF4)变成
$$\begin{aligned}
 \mathscr S_{k,p}&=\lambda_{k,p}(q-1)z_*^{p-1}\mathscr R_{k,p},\\
 \mathscr R_{k,p}&=\sum_{j\ge0}p^j\,g_{k,p-1+j(q-1)}. 
\end{aligned}\tag{AF5}$$
严格坐标及其 Taylor 数可以依赖 $p$，原有理函数本身不变。这里选择的是 $p-1\bmod(q-1)$ 的唯一完整模类，未将任意 Gauss 伙伴置零。由 $v_p(z_*^{p-1})=1/d$ 及参考估值得 $\mathscr R_{1,p}\in W^\times$。故对每条真实目标
$$ \mathcal A_b(\rho^{-1}-1)
 =\frac{\lambda_{b,p}}{65\lambda_{1,p}}\frac{\mathscr R_{b,p}}{\mathscr R_{1,p}}.\tag{AF6}$$
已证原 $\mathcal A_b$ 至少含 $T^2$；若 $[T^2]\mathcal A_b=0$ 则实际 Rubin 平方使它含 $T^4$。由于 $v_p(\rho^{-1}-1)=1$，必有
$$ \boxed{\ \sum_{j=0}^{3}p^j\,g_{b,p-1+j(p^2-1)}=0\bmod p^4.\ }\tag{AF7}$$
无条件同一个和模 $p^2$ 已为零，任一条在模 $p^4$ 违背(AF7)就给该 $p$ 的真实通常全 Sha 有限证书。两个目标的共同坏会使二条固定有理函数各满足(AF7)。旧 R1065/1066 为 degree34、102 的负二测试；此处是固定曲线对的原 $T=-1+\rho^{-1}$ 值、原参考的准确单位和非平凡首层驯角色。迄今尚未证明(AF7)在无穷 $p$ 上违背。

## 24. 同一原首圈的全负权、两条真正驯行及准确参考

沿(AF1)–(AF7)，并沿(W1)取 $\pi^{p+1}=p$、$v_p(\pi)=1/(p+1)$。对 $D\subset E_1[p]$ 让 $D(v)$ 是特征零形式邻域中的唯一有限 étale 延拓。把源水平始终预合实际 $M^{-1}$。置
$$ F_{k,D}(v)=f_k(E_v/D(v),q_D\alpha M^{-1},\kappa_D(v)),\qquad
 q_D^*\kappa_D(v)=\omega(v),\qquad
 L_{k,D,n}=[w^n]P(v)F_{k,D}(v).\tag{AG1}$$
这个物理系数含整个商曲线与移动的除点。记 $A,B$ 为(K2)的同一反对角晶体常数。相比水平基，目标线参数 $w'=A/(Bw)$，且 $P(v)F_{k,D}(v)=B(B_0f_k)(v'_D)$，$B_0=vQ/6$。令
$$ z=\pi/(6w')=c_p w,\quad c_p=\pi B/(6A),\qquad
 b_{k,D,n}=[z^n](B_0 f_k)(v'_D(z)). \tag{AG2}$$
则 $L_{k,D,n}=B c_p^n b_{k,D,n}$。$v'_D(z)=\pi X(Y_D(z))$ 用(K2)在原首端 $D$ 的实际根支。由(AF1)并用 $z(\Phi_t v')=\rho_t^{-1}z(v')$，
$$ b_{\,\mathcal T_t f_k,D,n}=\rho_t^{-(n+1)} b_{k,\bar tD,n}.$$
这对全部 $t$ 成立：在各端点附近的解析映射由其标记、点 $v'_D$ 的像及此局部参数唯一决定。因此
$$ \mathscr L_{k,n}=\sum_{t\in\Delta}\rho_t^{-(n+1)}L_{k,\bar tD_*,n},\qquad
 \mathscr L_{b,n}=65\,\mathcal A_b(\rho^{-n-1}-1)\mathscr L_{1,n}.\tag{AG3}$$
$D_*$ 是同一个实际原核。对群环幂级数取系数可先在足够小的 $z$ 盘逐项作，在那里由(P9)的严格盘收敛及 Cauchy 控制可交换；或者先取有限局部 jet 连续作用。(AG3)仍能在参考为零时作乘法使用。

下面对全部 $n=p^a-1$ 付准确参考，包括 $a=0$。由(W1),(R5)，在 $W[\pi]$ 加首圈根的整数环中有
$$ (B_0 f_1)(\pi X(Y))/\pi\equiv Y f_1(0)/6\bmod\mathfrak m.$$
代每支 $1+\kappa Y_D(z)^d=zY_D(z)$ 的整形式幂级数仍逐项成立，因为在零处的隐方程导数是单位。置 $Y_*=Y_D(0)$，$Y_D(z)=Y_* y$。由 $1-y^d=zY_* y$，Lagrange 式给
$$ [z^n]Y_D(z)=Y_*^{n+1}\frac{(-1)^n}{n+1}
                           \binom{(n+1)/d}{n}.\tag{AG4}$$
当 $n=0$ 右侧为 $Y_*$。当 $n=p^a-1>0$，二项式中首项 $p^a/d$ 赋值 $a$，除数 $n$ 为单位，剩下 $\prod_{r=1}^{n-1}(p^a/d-r)/r$ 全为单位；再除 $n+1=p^a$ 准确抵消。又 $Y_{\bar tD_*}(0)\equiv\rho_tY_{D_*}(0)\bmod\mathfrak m$ 由(AF2)及 $X(Y)\equiv Y$。故(AG3)的真实整驯和首项是 $d$ 倍同一单位。$B$ 为单位；$v_p(A)=1$ 因原次数 $p$ 同源在 de Rham cup 上乘 $p$，两个所用水平基取同一原 cup，故 $-AB=p$。于是
$$ \boxed{\,v_p(\mathscr L_{1,p^a-1})=\frac{p^a}{p+1}-(p^a-1).\,}\tag{AG5}$$

取 $T_a=\rho^{-p^a}-1$，准确定标 $v_p(T_a)=a+1$。用原整 Rubin 比及质量、一次项皆零，得到每一层
$$ \boxed{\ \frac{\mathscr L_{b,p^a-1}}
                   {65\,\mathscr L_{1,p^a-1}T_a^2}
              \equiv[T^2]\mathcal A_b\pmod {p^{a+1}}.\ }\tag{AG6}$$
如原中央卷积含 $T^4$，(AG5)右侧加 $4(a+1)$ 即相应 $\mathscr L_b$ 的下界。全部层使用同一 $p+1$ 个首圈原核；在(AG3)只实际出现 $\rho_t^{-1}$ 和 $\rho_t$ 两条驯行，因为 $p\equiv-1\bmod d$。这个负权数列与原中央正权 $d p^a$ 在同一 $\mathcal A_b$ 两侧取值，(AG6)没有将低阶负一采样单独当作极限。

### 第一个移动除点导数的代数归一

仍用(AF3)的 $\widetilde G_k$ 和显式 $\lambda_{k,p}$。在原 $E_v$ 上把该有限平移和按原 tame 挠点的特征零延拓写为 $\widetilde G_{k,v}(t)$，$t=x^{-1/2}$ 选择 $y=-t^{-3}(1+vt^4+t^6)^{1/2}$ 的原正式支。于是 $\omega_v=\ell_{v,t}(t)dt=(1+vt^4+t^6)^{-1/2}dt$，$\ell_v(0)=0$ 是椭圆正式对数。对 $R(v)\in E_v[p]$，在 $v=0$ 附近有 $\ell_v(t(R(v)))=0$，因为它是 $p$ 挠。该等式可逐点在略小的 $v$ 邻域对 $v$ 求导：$|t(R)|<1$，上述积分与其一阶参数导数在任意固定严格小 $t$ 盘一致收敛。令 $H(t)=6\partial_v\ell_v(t)|_{v=0}$，$D=\omega^{-1}d$ 为固定 $E_1$ 的不变导数。$v'(w)(0)=6$、$P'(0)=0$ 给真正首阶物理来源
$$ L_{k,D,1}=\lambda_{k,p}\sum_{R\in D}\left(
       6\,\left.\partial_v\widetilde G_{k,v}(t_R)\right|_{v=0,t_R\ {\rm fixed}}
                   - H(t_R) D\widetilde G_k(R)\right). \tag{AG7}$$
第一项也包含全部 tame 平移点的变化。它是固定带水平代数族在 $t$ 为局部坐标时的代数导数。对 $R=O$ 用整延拓，最终完整非平凡席位会去掉这项。

在 $E_1:y^2=x^3+1$ 上设 $\eta=x\omega$。直接微分 $x^2/y$ 得
$$ dH=6\,\partial_v\omega_v|_0=\eta-d(x^2/y),\qquad
 H=-\zeta_E-x^2/y .\tag{AG8}$$
这里 $\zeta_E$ 是正式盘上满足 $d\zeta_E=-\eta$、主部 $1/t$、为奇的亚纯原函数；逐项积分给整个开盘收敛，除 $O$ 外正则。令 $\psi_p$ 为原 $p$ 除多项式，以任意固定非零倍数归一。在正式盘的亚纯函数域，
$$ D\log\psi_p=p\zeta_E\circ[p]-p^2\zeta_E.$$
确可先在原点以经典 $\sigma(pz)/\sigma(z)^{p^2}$ 的形式 Laurent 式验证，所有系数在 $K$；换 $\zeta_E$ 一次线性项也相消。再以亚纯延拓到整个开盘。对非零 $R\in E_1[p]$，在 $R+X$ 的参数 $z=\log_E X$ 取常项；$\psi_p$ 在 $R$ 为单零，$p\zeta_E([p](R+X))=1/z+O(z)$。故
$$ \zeta_E(R)=-\frac{D^2\psi_p(R)}{2p^2D\psi_p(R)},\qquad
 H(t_R)=\frac{D^2\psi_p(R)}{2p^2D\psi_p(R)}-\frac{x(R)^2}{y(R)}.\tag{AG9}$$
$y(R)$ 对奇数 $p$ 的非零 $p$ 挠不为零。此值同时为复准周期校正下 $\zeta_E(R)=\mathcal E_1^*(R)$ 的代数值：在复格中相同 Laurent 比较的 $p\zeta(pR+pX)$ 常数为 $p\eta_{pR}$，故正抵去 $\eta_{pR}/p$。由(AG7)–(AG9)每个 $n=1$ 的真实移动项都能用原 E1 上的代数点与除多项式读出。对该 $n$，(AG4)的系数 $-1/d$ 为单位，故仍有 $v_p(\mathscr L_{1,1})=2/(p+1)-1$，相应的第二个固定评值是 $\mathcal A_b(\rho^{-2}-1)$。中央二阶在无穷素数的非零仍需从这些真正同源值推出。

## 25. 两条完整 Gauss 行、全部移动扭点的代数导数与原中央两位

沿(AF)、(AG)全部原标记及固定有限坏素集。令 $r=\rho^{-1}$、$T_j=r^j-1$。若 $1\le j\le i<p$，(AG4)的首项模 $p$ 为 $(-1)^{j-1}$，因此
$v_p(\mathscr L_{1,j-1})=j/(p+1)-(j-1)$。对整幂级数
$\mathcal A_b(T)/T^2$ 用 $\prod_{j=1}^i(T-T_j)$ 作 Weierstrass 除法，再在零处取值，得
$$ [T^2]\mathcal A_b\equiv
 \sum_{j=1}^i\left(\prod_{h\ne j}\frac{-T_h}{T_j-T_h}\right)
 \frac{\mathscr L_{b,j-1}}{65\mathscr L_{1,j-1}T_j^2}
 \pmod {p^i}.\tag{AH1}$$
余项被 $\prod T_j$ 整除；每个 $T_j$ 和每个差 $T_j-T_h$ 赋值为一，故各 cardinal 权为单位。这里所有样本由同一原首圈给出。

### 固定极及真实全扭点导数

写 $U=B-[a]Q_{c_k}$，$B\in E[7]$、$a\in(\mathcal O_K/c_k)^\times$，并置
$$ m_U=\epsilon_k(\bar a)^{-1}
 \begin{cases}48/7,&B=O,\\-1/7,&B\ne O.\end{cases}$$
这些极互异；其素于七部分准确为原 $6$ 或 $390$ 水平，故 $x_U,y_U$ 非零。相反极的留数互为相反数，$\widetilde G_{k,v}$ 为偶函数。因此在整个带标记族中有
$$ \widetilde G_{k,v}
 =\widetilde G_{k,v}(O)+
       \sum_{U/\{\pm1\}}\frac{2m_Uy_U(v)}{x-x_U(v)}.$$
中心 $\widetilde G_k(O)=0$。在中心的 $\mu_3$ 轨道，
$x_{uU}=u x_U,\ y_{uU}=y_U,\ m_{uU}=u^{-1}m_U$，所以
$$ \widetilde G_k=
 6t^4\sum_{U/\mu_6}\frac{m_Uy_Ux_U}{1-x_U^3t^6},\qquad t=x^{-1/2}.
 \tag{AH2}$$
各 $x_U^3$ 在这些轨道之间互异。

对任一原标记非零扭点 $T(v)$、阶 $m>2$，记
$e=\mathcal E_1^*(T)=\zeta(z_T)-\eta_\Lambda(z_T)$。在 $T+X$ 处对
$m\zeta(m(T+X))-m^2\zeta(T+X)=D\log\psi_m$ 取常项，得到
$$ e=-\frac{D^2\psi_m(T)}{2m^2D\psi_m(T)}.$$
$\psi_m$ 始终为完整除函数，偶 $m$ 时保留 $y$ 因子；此式是实际代数截面。令 $D_v=4v^3+27$。原族 $y^2=x^3+vx+1$ 上全部标记点满足
$$\begin{aligned}
 D_v\partial_vx&=9ye+9x^2+2v^2x+6v,\\
 D_v\partial_vy&=\tfrac92(3x^2+v)e+(\tfrac{27}2x+3v^2)y,\\
 D_v\partial_ve&=(v^2-\tfrac92x)e-\tfrac92y .
\end{aligned}\tag{AH3}$$

给出完整微分证明。以 $\omega=dx/(2y),\eta=x\omega$，取
$$ a=-v^2/D_v,\quad b=9/(2D_v),\quad c=3v/(2D_v),$$
$$ F=-\frac{9x^2/2+v^2x+3v}{D_vy},\qquad
 J=\frac{-v^2x^2+3vx/2+9/2}{D_vy}.$$
直接代曲线方程即有
$\partial_v\omega=a\omega+b\eta+dF$、
$\partial_v\eta=c\omega-a\eta+dJ$，这里先固定 $x$ 求参数导数。
$\omega,\eta$ 的原函数为 $z,-\zeta$。沿固定 Betti 分量的扭点，
$z_T,\eta_\Lambda(z_T)$ 的导数分别为
$az_T-b\eta_\Lambda(z_T)$、$-cz_T-a\eta_\Lambda(z_T)$。
固定 $x$ 时，
$\partial_vz=az-b\zeta+F$、
$\partial_v\zeta=-cz-a\zeta-J$；奇 Laurent 式确定积分常数为零。
所以
$$ \partial_vx_T=2y(be-F),\qquad
 \partial_ve=-ae-J-x(be-F).$$
又 $xF-J=-9y/(2D_v)$，求 $y$ 导数便得(AH3)。这些为代数截面等式，故所有特征零嵌入相容。中心对 $w$ 的真导数记点号，由 $v'(0)=6$ 得
$$ \dot x=2x^2+2ye,\qquad
 \dot y=3xy+3x^2e,\qquad
 \dot e=-y-xe.\tag{AH4}$$
它同时用于全部 tame 极 $U$ 和实际 wild 点 $R$。

### 原两行及保留的整精度

置 $\xi(h)=[h]_{\rm T}^{1-p},\ R_h=[h]Q_*,\
\Delta_0=p^2-1,\ z_*=Z(Q_*)$。定义
$$\begin{aligned}
 J_k(R)&=\sum_{U/\{\pm1\}}2m_U
 \left(\frac{\dot y_U}{x_R-x_U}
       -\frac{y_U(\dot x_R-\dot x_U)}{(x_R-x_U)^2}\right),\\
 N_{k,0}&=\frac{\sum_{h\in\mathbf F_q^\times}\xi(h)\widetilde G_k(R_h)}
                  {\Delta_0z_*^{p-1}},\\
 N_{k,1}&=\frac{p\sum_{h\in\mathbf F_q^\times}\xi(h)^2J_k(R_h)}
                  {\Delta_0z_*^{2(p-1)}} .
\end{aligned}\tag{AH5}$$
通用部分分式的导数另有 $\partial_w\widetilde G_{k,v}(O)$，但它在整个非平凡 $\xi^2$ 和中抵消；每个核的零点贡献也抵消。四位标量全整，参考 $N_{1,0},N_{1,1}$ 均为单位，由(AF2)、(AG5)及 $n=1$ 的 $-1/d$ 首项付出。

对(AH1)取 $i=2$，直接化简得到
$$ \boxed{
 A_{b,2}\equiv\frac{\lambda_{b,p}}{65\lambda_{1,p}}\,
 \frac{(1+r)^3N_{b,0}N_{1,1}-N_{b,1}N_{1,0}}
 {r(1+r)^2(r-1)^2N_{1,0}N_{1,1}}
 \pmod {p^2}.}\tag{AH6}$$
分母净损两位；分子赋值小于四便给真实原二阶非零。

具体尾界亦保原源。设
$$ J_k^{\rm form}(t)=
 6\,\partial_v\widetilde G_{k,v}(t)|_0-H(t)D\widetilde G_k(t).$$
首项是原带 tame 水平族在 $(v,t)$ 盘上的整函数，$D\widetilde G_k$ 整。又
$$ H(t)=-3\sum_{m\ge0}\binom{-3/2}{m}\frac{t^{6m+5}}{6m+5}.$$
整换 $t=t(Z)$ 后，$[Z^N]H$ 赋值至少 $-\lfloor\log_pN\rfloor$。
对 $N<5p^2$ 还有至少 $-1$：指数 $6m+5$ 的首个 $p^2$ 倍数是 $5p^2$。$J_k^{\rm form}$ 满足同样下界。令
$m_j=2(p-1)+j(p^2-1)$，真正完整 Fourier 和遂给
$$ N_{k,1}\equiv
 \sum_{j=0}^3p^{j+1}[Z^{m_j}]J_k^{\rm form}\pmod {p^4}.
 \tag{AH7}$$
$j=4$ 用 $m_4<5p^2$；$j\ge5$ 用
$\lfloor\log_pm_j\rfloor\le j-3$，其起点 $m_5<p^3$，以后左端指数线性增长而右侧允许幂每步乘 $p$。故尾赋值全至少四。第一行仍按(AF5)取四个整系数；两列的原参考、混合项与除去的两位均已保留。

### 七乘法在完整真实和中的准确合并

对 $n=p^s-1$ 或 $n=1$，$n+1$ 的驯角色非平凡。令
$P_{h,a}(v)=R_h(v)+[a]Q_{c_k}(v)$；$h$ 只标实际 $p$ 挠点的有限 étale 延拓，不在非 CM 的 $E_v$ 上假设 $[h]$ 为自同态。整数 $[7]$ 则在全族真实存在。因
$$ F_7(T)=7e(T)-e([7]T),$$
且 $(h,a)\mapsto(7h,7a)$ 双射、$\xi(7)=\epsilon_k(7)=1$，得到
$$ \mathscr L_{k,n}=6\lambda_{k,p}
 \sum_{h,a}\xi(h)^{n+1}\epsilon_k(\bar a)^{-1}
      [w^n]\bigl(P(v)e(P_{h,a}(v))\bigr).\tag{AH8}$$
$n=0,1$ 的两行分别为 $6\sum e$ 和 $-6\sum(y+xe)$，保留全部原权、点与相位。每个 $e$ 是通用向量扩张的唯一扭提升；其加法由 zeta 加法给
$$ e(P+Q)=e(P)+e(Q)+\frac{y(P)-y(Q)}{x(P)-x(Q)}.$$
(AH3)可直接作用于这些真正复合点，结合原(R3)的 $P,w$ 得全部高阶。以上仍未证明(AH6)的原分子在无穷多个 $p$ 上非零。

## 26. 同一有理二次扭曲的原负权、固定数域及普通分母

**已证明。** 沿(AF)–(AH)全部原标记。记
$A=\operatorname{area}(\Lambda_1)/\pi,\ \Lambda_1=\varpi_1\mathcal O_K$；
这里面积分母的 $\pi$ 指圆周率。取 $Q_*=Q_p=\varpi_1/p$。
对 $j=n+1$ 且 $d\nmid j$，定义完整primitive Hecke角色
$$
 \Psi_{k,n}((\alpha))=\alpha^{2n+1}\epsilon_k(\bar\alpha)
                 [\alpha\bmod p]_{\rm T}^{(p-1)j}. \tag{AI1}
$$
在全局单位上有限两因子乘积为 $u^{1-2j}$，恰与无穷部抵消。
原 $c_1=6,c_b=390$ 各自的坏支撑全保留，$p$ 处非平凡。

由(AH8)原Betti扭标记及 $\eta=x\omega$ 周期为 $-\bar\lambda/A$，
除 $P(v)$ 后的格和点为
$\Lambda-w\bar\Lambda/A,\ T-w\bar T/A$。
在Hecke正则化的绝对收敛域对归一格每项取 $w$ 系数，在 $w=0$
导数系数为 $(1+s)_n/n!$ 乘
$A^{-n}\overline{T+\lambda}^n/
((T+\lambda)^{n+1}|T+\lambda|^{2s})$。
取 $s=0$ 解析延拓，该系数为一；角次数 $2n+1$ 非零，无平凡极。
这也给Kronecker Laurent–Taylor对角式的本次取系数。
CRT $r=pa+c_kh$ 的 $\epsilon_k(p)=-1,\ \xi(c_k)=1$，
(AH8)的 $7-1$ 和六个理想生成元全部保留，故
$$
 \mathscr L_{k,n}=-36c_kp\,\lambda_{k,p}A^{-n}
        \frac{\bar\varpi_1^n}{\varpi_1^{n+1}}L(n+1,\Psi_{k,n}). \tag{AI2}
$$
理想求和初得共轭角色，取共轭理想即显示的 $\Psi_{k,n}$。
同(AG3)给
$$
 \mathcal A_b(\rho^{-j}-1)=\frac{\lambda_{b,p}}{\lambda_{1,p}}
                 \frac{L(j,\Psi_{b,j-1})}{L(j,\Psi_{1,j-1})} \tag{AI3}
$$
于每个已证非零的参考；$c_b/c_1=65$ 已相消。
$j=1$ 是实际非平凡驯 $p+1$ 阶首圈，
$j=p^a$ 的全部层仅用互逆两条驯角色。

置 $g=(p+1)/2,\ j_m=(2m+1)g$。
(AI1)的 $p$ 角色恰为
$\chi_{p^*}(\mathfrak a)=(N\mathfrak a/p)$，
$p^*=(-1)^{(p-1)/2}p$。因为 $3\mid j_m$、
$\epsilon_k(\bar\alpha)=\epsilon_k(\alpha)^{-1}$，
$$
 \Psi_{k,j_m-1}=(\psi_k\chi_{p^*})^{2j_m-1}. \tag{AI4}
$$
$m=0$ 是 $L((p+1)/2,\psi_k^p\chi_{p^*})$。
对固定 $0\le m<i,\ p>2i+3$，
(AG4)中的 $j_m/d=m+1/2$ 前两 $p$ 进位为 $g+m,g-1$，
$j_m-1$ 的两位为 $g+m-1,m$。
Lucas给二项为单位，$j_m$ 亦为单位，
所以实际参考估值为 $j_m/d-(j_m-1)$。
$p$ 进上标的Lucas式可先用正整近似上标再取极限。

对 $\sigma\in G_K$ 令 $s$ 为其在 $E_1[c_kp]$ 的兼容CM标量。
经(AH8)两个指数换元 $(a,h)\mapsto(sa,sh)$，得到
$$
 \frac{\sigma(\mathscr L_{k,n}/\lambda_{k,p})}
      {\mathscr L_{k,n}/\lambda_{k,p}}
       =\epsilon_k(\bar s)(Ns/p),
$$
为零时读作乘法等式。
由(J),(Q3)的原Hecke descent，
$\epsilon_1(s)=1$ 且
$\epsilon_b(s)/\epsilon_1(s)=\theta_b/(\sigma\theta_b)$，
所以这次反 $\epsilon$ 的真正因子是 $\sigma\theta_k/\theta_k$。
Weil配对给 $Ns$ 为 $\sigma$ 的模 $p$ 圆分作用，
故 $(Ns/p)=\sigma(\sqrt{p^*})/\sqrt{p^*}$。
取正实 $\tau_p$：$p^*>0$ 时取 $\sqrt p$，
$p^*<0$ 时取 $\sqrt{3p}$；
后者等于某符号的 $\delta\sqrt{p^*}$，
$\delta=\sqrt{-3}\in K$。两者给同一 $G_K$ 特征。
置 $\kappa_n=(1-\omega)(-\omega)^n$。
由 $\varpi_1=\Omega_{\mathbb R,1}/(1-\omega)$，
$\bar\varpi_1^n/\varpi_1^{n+1}=\kappa_n/\Omega_{\mathbb R,1}$。
理想共轭给显示的中心 $L$ 值为实，因而
$$
\begin{aligned}
 D_{k,p,m}&=\frac{\mathscr L_{k,j_m-1}}
  {\lambda_{k,p}\theta_k\tau_p\kappa_{j_m-1}}\in\mathbb Q,\\
 R_{b,p,m}&=\theta_b^{-1}
  \frac{L(j_m,(\psi_b\chi_{p^*})^{2j_m-1})}
       {L(j_m,(\psi_1\chi_{p^*})^{2j_m-1})}
   =\frac{D_{b,p,m}}{65D_{1,p,m}}\in\mathbb Q .
\end{aligned} \tag{AI5}
$$
$\lambda_k$ 由 $M^{-1}$ 实际标记决定。

令 $u=-g\log_p\rho$，
$F(x)=\mathcal A_b(\exp(ux)-1)/x^2$，
$F(0)=u^2[T^2]\mathcal A_b$。若 $a_k=[T^k]\mathcal A_b$，则
$$
 [x^s]F=\frac{u^{s+2}}{(s+2)!}
       \sum_{k=2}^{s+2}k!\left\{\!{s+2\atop k}\!\right\}a_k .
$$
$p>2i+3$ 时，全部 $s\ge i$ 的估值至少 $i+2$：
$s+2<p$ 时直接可见；其余用
$v_p(N!)\le(N-1)/(p-1)$。
对固定节点 $x_m=2m+1$ 取普通Lagrange权
$b_m=\prod_{0\le h<i,\ h\ne m}(-x_h)/(x_m-x_h)$，
它们都是 $p$ 单位。由(AI3),(AI5)，同一个真实中央有普通有理近似
$$
 \sum_{m=0}^{i-1}\frac{b_mR_{b,p,m}}{(2m+1)^2}
 \equiv\frac{\lambda_{1,p}}{\theta_b\lambda_{b,p}}
     (g\log_p\rho)^2[T^2]\mathcal A_b\pmod{p^{i+2}} . \tag{AI6}
$$
固定 $i$ 时全部 $p$ 驯角色、权、导子如(AI4)。

### 逐项分母与实际高度

在一个固定数域取良约化模型。对
$T=[h]Q_p+[a]Q_c$，其在每个有限处的prime-to-该处部分非零，
故 $x_T,y_T$ 乘固定数后全整。
又 $e(T)=e(R)+e(A)+(y_R-y_A)/(x_R-x_A)$，
$A=[a]Q_c,\ R=[h]Q_p$。
在 $\ell\ne p$ 的好模型上，$R$ 为非零prime-to-$\ell$ étale挠点，
$\psi_p$ 的零简单；原全除函数
$-D^2\psi_p/(2p^2D\psi_p)$ 给 $e(R)$ 的整性。
等价地，(AH8)的通用向量扩张上 $p$ 可逆，
$R$ 的唯一 $p$ 挠提升在整模型内。
$R$ 约化阶为 $p$，$A$ 的阶除 $c$，故不会相等或互为负；
加法分母不增加这些好素位的代价。

在 $p$ 处，(AG8)及 $v_p(t_R)=1/(p^2-1)$ 给
$v_p(e(R))>-1$：各阶 $H$ 用其显式积分，
首个 $p^a$ 分母的最小次数至少 $p^a$；
$a\ge2$ 时该次数为 $5p^a$（$a$ 偶）或 $p^a$（$a$ 奇）。
$x_R^2/y_R$ 估值为 $-1/(p^2-1)$，加法剩余项至多此极。
因此有固定 $C$ 使 $Cp\,e(T)$ 全整。

令 $\partial=\partial_w=(2/9)D_vP^2\partial_v$，
添 $U$ 为 $\eta$ 沿 $e_0$ 的系数。
由(R2),(AH3)，$\partial$ 在
$\mathbb Z[1/6][v,P,U,x,y,e]$ 上为一个固定多项式导子，
例如
$\partial P=P^2(U-2v^2P/9)$，
$\partial U=P^2(vP/3+2v^2U/9)$。
$\partial^n(Pe)$ 总度数为 $O(n)$；
$n\ge1$ 时 $e$ 次数至多 $n$，因为首步至多一，
其后每步至多加一。
中央 $[w^n]Pe=\partial^n(Pe)|_0/n!$，
故扩大一次固定 $C$，
$C^{n+1}p^n n!\mathscr L_{k,n}$ 均为代数整数。
对固定有限的两目标和参考取同一个 $C$。
结合(AI5)及准确参考估值，$n=j_m-1$、
$v_p(n!)=m$，可以使
$$
 I_{k,p,m}=C^{n+1}p^{n-m}\frac{n!}{p^m}D_{k,p,m}\in\mathbb Z,
 \qquad p\nmid I_{1,p,m},\qquad
 R_{b,p,m}=\frac{I_{b,p,m}}{65I_{1,p,m}} . \tag{AI7}
$$
$p$ 外只额外除固定 $\lambda,\theta,\kappa_n$ 及 $\tau_p$；
后者除 $p$ 外最多在 $3$ 处有固定代价。
$p$ 处由(AG3),(AG4)得 $v_p(D_1)=m-n$，目标至少此值，
所以显示的整数确实 $p$ 整，参考是单位。

在任一固定小复 $w$ 盘，归一格形状共紧；
非零 $cp$ 挠标记距格至少固定 $1/(cp)$ 的倍数。
$\mathcal E_1^*(T)$ 的唯一极为格点简单极，故一致 $O(p)$。
所有 $h,a$ 共 $O(p^2)$ 项，Cauchy给
$|\mathscr L_{k,n}|\le C^{n+1}p^3$。
所以
$\log^+|I_{k,p,m}|=O((n+1)\log(np)+\log p)$，
(AI6)全 $i$ 项的普通共分母对数有
$O(i^2p\log(ip^2))$ 界。
此界超过要比较的 $(i+2)\log p$；
本节未由有理性、实性或这个高度界推出无穷 $p$ 的中央非零。
