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
