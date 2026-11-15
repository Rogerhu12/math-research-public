# R742 — 固定十七处算子、同一有限门与原 primitive 负一行的完整极限

日期：2026-11-15。**状态：已证明。**

本篇继续 R737、R740 的同一个 $q_N^*$，没有重新适配测试。
先将 $n=N+r$、固定 $r\ge1$ 的完整过滤式，化为不再含 N 的有限门恒等式。
取 $r=1$ 时，所有真实门深度都在1至125之间。
随后对完整 Y 观察及两条 $Y_\kappa$ 返回观察作十七处投影：
两个返回向量由旧模289射线确定的固定局部算子给出，
相互之间保一个阶整除17的实际算子。

有限 p 门的 Mumford 平移可以选取兼容的周期代表，
从而在十七处逐项固定整个 ramified gluing 模块。
所需的全配对相位仍显式保留。
因此本篇可以对**同一个门**写三次分量的完整关系，
而不是先取一个裸 W 边际再重新加门。

两条原负一线在过滤后的关系中各自非零。
它们的完整四-unit项、W/V返回项及原 paired-T 外部仍在同一等式内；
这里没有将这些投影后的局部非零改认成原 $J_T'$ 非零。

## 1. 固定原参数，实际权的 u=0 极限

记
$$
K=\mathbf Q(\omega),\quad\delta=1+2\omega,\quad b=17,\quad
\lambda=-\bar\pi_0^{-1},\quad
\kappa=p\lambda^2=\pi_0/\bar\pi_0,\quad u=\kappa^N,
\qquad N\in4\mathbf Z_{>0}.
\tag{1}
$$
固定 R734 的一个合格 p。所有极限只令 N 增大；
$\lambda,\kappa$ 及它们在17处的类均固定。
特别 $\mathrm N(\kappa)=1$。

原轴为
$$
Y=A+c+2d,\quad W=A+3\delta c+4d,\quad
b_Y=(20+3\omega)/17,\quad Z=W-b_YY,
$$
$$
\alpha=17-3\omega,\quad V=36Y-\alpha W,\quad
E=(5+6\omega)A-29c-(58+87\omega)d .
\tag{2}
$$
原三个 A 伙伴仍逐个保留。
R737 的完整 cd 权写成
$$
\Phi_N=\sum_{a=0}^{30}E^a\phi_{a,N}.
\tag{3}
$$
每个 $\phi_{a,N}$ 只依赖正交于 Y、Z、E 的三个伙伴。
使用 R715 的完整两个 C 分支时，它们来自
$$
\begin{aligned}
P_N(H,E_\perp+uK_0,G_\perp+guK_0)
-\eta\lambda P_N(H,\kappa E_\perp+uK_0,
 G_{00}+\kappa(G_\perp-G_{00})+guK_0),\\
H=D_*-E/29,\qquad K_0=H-406D_*/143,\qquad g=3-2\omega .
\end{aligned}
\tag{4}
$$
每个齐次块保原 $b,\Omega$ 归一。
若改用原 $C^\perp$-unit 表示，则其指示不随 u 改动；
(4) 是该同一指示的完整返回，不能只留第一项。

R715 的50阶逆、R734 的5阶逆及其全部指定分母，在
$(\lambda,\kappa,0)$ 处均为单位。
故它们的实际系数在 $u=0$ 附近属于 $\mathcal O[[u]]$；
这里没有冻结 $\kappa$ 或 $\lambda$。
于是逐个固定单项式有
$$
\phi_{a,N}=\phi_{a,\infty}+u\,\widetilde\phi_{a,N},
\qquad
\|\widetilde\phi_{a,N}\|_\infty\le1,
\qquad
\Phi_\infty:=\sum_{a=0}^{30}E^a\phi_{a,\infty}.
\tag{5}
$$
(5) 直接来自单位分母的有理函数之差和 (4)，
不是对随 N 改动的测试使用一个未经证明的 N 递推。
全部系数在原共同周期归一后仍为 K 中的代数数。
$\Phi_\infty$ 是固定 p 下的真实有限正矩权，包含两个 C 分支。

整个 Y、W、quarter 与第一 Z 来源等式都可以取该一致极限。
例如
$$
Y_*(\Phi_\infty e_0)=\nu_S,\qquad
W_*(\Phi_\infty(e_0,e_1,e_2))=6\delta(\nu_T,\nu_T,-\nu_T),
\qquad Y_*(Z\Phi_\infty e_0)=0 .
\tag{6}
$$
它们不允许在任一附加斜门后继续把第一 Z 行删为零。

## 2. 不再含 N 的真实有限门关系

沿 R737，置
$$
\begin{array}{c|cc}
i&b_i&e_i\\ \hline
1&-(170+117\omega)/526&-(4+9\omega)/263\\
3&(170+291\omega)/526&(2-3\omega)/263
\end{array},
\quad
B_i=b_iZ+e_iE,\quad
\Delta_\ell=1_{B_1\in p^\ell}-1_{B_3\in p^\ell}.
\tag{7}
$$
原射线保证所需系数及
$b_1e_3-b_3e_1=-5/263$ 为单位。

定义固定权的 primitive 行
$$
p_a(r)=
 \int_{\{Y,Z,E\ {\rm unit}\}}
   \Delta_r\,\frac ZY\,E^a\phi_{a,\infty}\,de_0,
\quad
p_a^F(r)=\lambda^r p_a(r),
\quad
c_a=-\chi_A\lambda^3\kappa^{a+1}.
\tag{8}
$$
$\chi_A^2=1$ 仍是原 odd29 符号，不另猜其值。
记作用于 r 的实际偶移位为 $\mathsf T_2$，并保
$$
\begin{aligned}
\mathscr P&=\prod_{j=1}^{31}(\mathsf T_2-\lambda^4\kappa^{2j}),\\
\mathscr Q&=\prod_{a=0}^{30}(\mathsf T_2-\lambda^6\kappa^{2(a+1)}),\\
U_{31}&=\prod_{j=1}^{31}(1-\kappa^{2j}),\qquad
V_{31}=\prod_{j=1}^{31}(1-\lambda^2\kappa^{2j}) .
\end{aligned}
\tag{9}
$$
$\mathscr Q_{\ne a}$ 表示删掉第 a 个因子。

令 R734 的实际代数系数在 $u=0$ 为 $a_\infty,c_\infty$，并定义
$$
\mathfrak I_\infty
=\Omega\left\{\frac{c_\infty}{a_\infty}I_{2,p}
                         +\frac1{a_\infty}I_{4,p}\right\}.
\tag{10}
$$
R735、R733 已证明 (10) 非零，且两个显示系数均为代数单位。

则对每个固定整数 $r\ge1$，有完整恒等式
$$
\boxed{
\frac{d_p}{b_Y}\mathscr P
 \sum_{a=0}^{30}\mathscr Q_{\ne a}
   \{p_a^F(r+2)+c_a p_a^F(r+1)\}
=
\frac{d_p(-1)^r}{b_Y}
 \lambda^{2r+248}U_{31}V_{31}\mathfrak I_\infty,
\qquad d_p=p-1 .
}
\tag{11}
$$

**证明。**
在 R737(21) 中取 $n=N+r$，将整个式子除以
$u\lambda^{4N}$。此时
$\lambda^{n+3N}=\lambda^{4N}\lambda^r$，
所有过滤器系数均不依 N。
(5) 使每一条有限门积分一致趋向 (8)。
R737(20) 的余项除以 u 后趋零；
它原为 $p^{2N}\mathcal O$，而 $v_p(u)=N$。
主项则准确趋向 (11)。
不能省略 $\lambda^{-4N}$：单位序列 $\lambda^{4N}$ 未被假定有极限。证毕。

左边只使用 $r\le\ell\le r+124$ 的实际门。
故 $r=1$ 时全部指示的 p 层至多125，且不再随 N 增长。
其中的 $Y^{-1}$ 仍是完整单位负一函数，
没有将它截成一个有限 Taylor 多项式。

## 3. 完整17模块的两个稳定子

用 R740 的原17自对偶 Hermitian 格
$$
\Lambda_{17}=\mathcal O_{K,17}^6,\qquad
\varphi_{\rm sph}=\mathbf1_{\mathbf Z_{17}^6}.
$$
本节的 Heisenberg 与 Weil 算子均使用 R740 已固定的
自对偶测度、原加性角色与 canonical splitting。
设 y 是 Y 的物理行，$N(y)=34$，并写
$$
G_Y(g)=I+(g-1)\frac{\bar y^{\,t}y}{34},
\qquad
g\in\mathcal O_{K,17}^{\,1}.
\tag{12}
$$
对原18个 Teichmüller 元 $g_j=g_0^j$，$g_0\bmod17=2+4\delta$，
定义
$$
\mathcal V_Y=\operatorname{span}
 \{\mathsf H(h)\,\omega_{17}(G_Y(g_j))\varphi_{\rm sph}:
           h\in\Lambda_{17},\ 0\le j<18\}.
\tag{13}
$$
$\mathsf H$ 是 Weyl 归一的 Heisenberg lift，因17为奇数，
其 $1/2$ 中心因子没有二进歧义。

有两个完整稳定子结论：
$$
\boxed{
\mathsf H(\Lambda_Y)\text{ 逐点固定 }\mathcal V_Y,\qquad
\Lambda_Y=\{h\in\Lambda_{17}:yh\in17\mathcal O_{K,17}\},
}
\tag{14}
$$
$$
\boxed{
\omega_{17}(K(17^2))\text{ 逐点固定 }\mathcal V_Y,\qquad
K(17^2)=\{k\in U(\Lambda_{17}):k\equiv I\bmod17^2\}.
}
\tag{15}
$$

对 (14)，$G_Y(g_j)^{-1}h$ 仍整，因为
$(g_j^{-1}-1)\bar y^{\,t}(yh)/34$ 整。
整 Heisenberg 元固定原球向量，故由协变性得到结论。
不同整 h 的交叉中心相位在原自对偶格上为一。
y 有单位系数，所以
$\Lambda_{17}/\Lambda_Y\simeq\mathbf F_{289}$；
若使用任意全局平移代表，所需的17补偿最多只读这个有限标签，
并非一个新的无限来源族。

对 (15)，$G_Y(g_j)$ 及其逆的分母都至多含一个17。
若 $k=I+17^2X$，则
$$
G_Y(g_j)^{-1}kG_Y(g_j)
=I+17^2G_Y(g_j)^{-1}XG_Y(g_j)
$$
属于原整 unitary 群，因而在相同 splitting 下固定球向量。
此外 $kh-h\in17^2\Lambda_{17}\subset\Lambda_Y$；
Heisenberg 交换的中心相位仍为一。
这证明所有 (13) 的向量被逐项固定。
这里使用的是诚实的已定标 unitary Weil 表示，
不是只比较 projective 交织。

(14) 尤其给 $\mathsf H(17\Lambda_{17})=I$。
相同结论在任何17整 unitary 共轭的 Y 轴上成立。

## 4. 原模289射线给两个固定返回算子

原射线已经包含
$$
\pi_0\equiv273+87\omega\bmod289 .
$$
令
$$
\pi_*=273+87\omega,\qquad \kappa_*=\pi_*/\bar\pi_* .
\tag{16}
$$
这只定义一个固定的17处单位，不给 p 增加同余。
准确有
$$
\kappa\equiv\kappa_*\bmod289,\qquad
\kappa\equiv-1\bmod17,\qquad
\kappa^2\equiv1-17\delta\bmod289 .
\tag{17}
$$
后两式也是 R698 所用的旧17二层数据。
它们可由第一式在 $\mathbf Z[\omega]/289$ 中直接代入，
不涉及一个新的数值证书。

对 L=W 或 V，设
$$
P_{L,t}=I+(t-1)\frac{\bar L^{\,t}L}{N(L)} .
$$
$N(W)=72,N(V)=18936$ 都为17单位。
故
$P_{L,\kappa}P_{L,\kappa_*}^{-1}\in K(17^2)$。
由 (15)，在本篇全部相关17向量上可准确使用固定算子
$P_{L,\kappa_*}$，无需保一个随 p、N 改动的局部矩阵。

为避免 splitting 角色混淆，先对18元环面的任意角色 $\chi$ 写
$$
\mathcal P_\chi^Y
=\frac1{18}\sum_{j=0}^{17}\chi(g_0)^{-j}
                         \omega_{17}(G_Y(g_j)),
\qquad
v_\chi=\mathcal P_\chi^Y\varphi_{\rm sph}.
\tag{18}
$$
所有下式对每个 $\chi$ 成立。
在 R735 的具体 Schrödinger 转模中，两个算术投影的角色是
$$
\tau_2(g_0)=-\omega^2,\qquad \tau_4(g_0)=-\omega .
\tag{19}
$$
这是含原 quadratic splitting 的真实 Weil 角色。
若改用 Hecke splitting，须同时换算整个表示和角色；
不能只把 (19) 的负号删掉后保原矩阵。

置
$$
v_\chi^V=\omega_{17}(P_{V,\kappa_*})^{-1}v_\chi,\qquad
v_\chi^W=\omega_{17}(P_{W,\kappa_*})^{-1}v_\chi .
\tag{20}
$$
R740 的完整观察
$$
Y_\kappa^V=(\kappa V+\alpha W)/36,\qquad
Y_\kappa^W=(V+\alpha\kappa W)/36
$$
均仍为范数34。因此 (20) 正是这两个实际观察的 ramified 向量，
不是裸 W/V 的球向量。

进一步定义固定局部算子
$$
\mathcal C_{17}=\omega_{17}(P_{V,\kappa_*^2}) .
$$
原共同平面缩放 $P_{W,\kappa}P_{V,\kappa}$
与 (12) 交换且固定 $\varphi_{\rm sph}$，故
$$
\boxed{v_\chi^W=\mathcal C_{17}v_\chi^V.}
\tag{21}
$$
由 (17)，$\kappa_*^{34}\equiv1\bmod289$。
所以 (15) 给
$$
\boxed{\mathcal C_{17}^{17}v_\chi^V=v_\chi^V.}
\tag{22}
$$
同式作用于它生成的循环空间。
这只是“阶整除17”，不宣称其为标量或阶恰17。
$\mathcal C_{17}$ 始终只作用于17局部因子；
(21) 不是在 p 处另作一次 V 两深返回，因而不改原门。

## 5. 同一 p 门的 CRT 代表及完整 Mumford 相位

这里支付将 (18) 放进原有限门时的平移问题。
不能把普通复 theta 平移中的准周期因子删掉，
也不能使用 $\log\zeta_{p^m}=0$ 来替代 formal-group 平移。

在原复周期格 $\Lambda$ 上，设 $t_{p^m}$ 是一个 formal p 幂挠点，
$v_m\in\Lambda\otimes\mathbf Q$ 是其复 uniformization 的任一周期代表。
p 不等于17，所以 $v_m$ 在17处整。
可选 $\ell_m\in\Lambda$，逐坐标满足
$$
v_m+\ell_m\in17^2\Lambda_{17}.
\tag{23}
$$
这是 $\Lambda/17^2\Lambda$ 上的有限 CRT 选择。
它不改变 $t_{p^m}$，也不改变原 additive Fourier character。

令 $v_0$ 是所用 theta 模型中的原 prime-to-p 挠基点，
包括全部17 gluing 标签、原 W-quarter 标签和其他固定半特征。
取一个与 p 互素的整数 $N_0$，使所有这些标签满足 $N_0v_0\in\Lambda$，
并使 $17\mid N_0$。

有 quarter 基点时，不能同时要求
$\epsilon\equiv0\bmod2$ 与 $\epsilon\equiv1\bmod N_0$。
这里统一使用 Bannai–Kobayashi Proposition 2.19 的**第一式**。
取
$$
\epsilon\equiv1\bmod\mathfrak p^m,\qquad
\epsilon\equiv0\bmod\bar{\mathfrak p}^{\,m},\qquad
\epsilon\equiv2\bmod4N_0^2,
\quad v'_0=v_0/2,\quad
\Delta_0=(\epsilon-2)v_0/2\in2N_0\Lambda .
$$
按原 CM type 逐因子理解前两条件；它们与第三条件由 CRT 相容。
第三条件已包含该命题所需的2因子。
这不改任何旧射线；$\epsilon$ 只是有限平移公式中的一个可选整数。

由原 Mumford 周期公式，准确有
$$
\vartheta^M_{\epsilon v'_0}
=c_0\vartheta^M_{v_0},\qquad
c_0=\alpha_{\mathcal L}(\Delta_0)
          \langle v_0,\Delta_0/2\rangle_{\mathcal L}.
$$
于是同一 formal 平移严格为
$$
\boxed{
\widehat\vartheta^M_{v_0}(t\oplus t_{p^m})
=
c_0^{-1}
\left\langle\epsilon(v_m+\ell_m),\epsilon v'_0/2
 \right\rangle_{\mathcal L}
\widehat\vartheta^M_{\epsilon v'_0+\epsilon(v_m+\ell_m)}(t).
}
\tag{24}
$$
所有 $c_0$ 和全配对都保在原系数中。
这是 Proposition 1.14 的 Mumford 周期因子与
Proposition 2.19 第一式的直接合成，未对偶阶基点使用不相容的式(32)。

后一个命题允许任意周期代表；将它分别用于 $v_m$ 与 $v_m+\ell_m$，
左边是同一个 formal 平移，故右边的**乘积**严格相同。
这支付换代表的准周期及中心相位，未声称两个裸 theta 译相等。

由 (23)，$\epsilon(v_m+\ell_m)$ 的17分量在
$17^2\Lambda_{17}$ 内，而 $\Delta_0\in2N_0\Lambda$
也落在 (14) 的稳定子。
原标签至多有一层17分母，故 $c_0$ 及 (24) 配对的17因子都为一。
其它处的 root-of-unity 配对完整保留。
若选取更大的固定 theta cover，只需加强 $N_0$ 和 (23)
到该明确稳定子之内；不增加 p 门的深度，也不换 formal 挠点。

有限层指示使用它原来的 Fourier 恒等式，例如
$$
1_{L(\xi)\in p^\ell}
=\frac1{p^\ell}\sum_{a\bmod p^\ell}
          \zeta_{p^\ell}^{\,aL(\xi)}
\tag{25}
$$
及单位指示的差。
每个字符用 (24) 的兼容代表。
于是对 (18)、(20) 的17投影，原有限门和原有限词的
p-local 算子严格交换；全部实际 Fourier 系数和 (24) 的配对不变。

这比“任意全局 lift 都与17投影交换”更准确。
若坚持原任意代表 h，须保 (14) 的补偿
$\mathsf H_{17}(-h)$；其标签为 $Yh\bmod17$。
(23)–(24) 给一种完整付清相位的选择，使这项补偿在17处恒等。
本篇没有在不同投影向量之间擅自删去一个中心符号。

原有限正矩微分和全部伴随也与不同有限处的算子相容。
最后单位负幂、相对 logarithm 取真实有界极限。
这里只用有限17投影的连续性，没有假设17处 Galois 自同构
连续作用于 $\mathbf C_p$。

## 6. 完整同门的三个投影来源

记 $\mu_{\chi,0}$ 为原 $e_0$ 在 Y17模型中取 (18) 的完整来源。
对两条返回来源 $e_1$，分别记
$$
\mu_{\chi,1}^W=\mathcal P_\chi^{Y_\kappa^W}e_1,\qquad
\mu_{\chi,1}^V=\mathcal P_\chi^{Y_\kappa^V}e_1 .
\tag{26}
$$
其17因子是 (20)，且由 (21) 联系。
其它有限处、全部16个 W-quarter lift、无穷处向量及原系数一律保留。
(26) 未把 e1 与 e0 认作相同来源。

令
$$
\begin{aligned}
z_W&=(263\kappa W-\bar\alpha V)/612,&
y_W&=(V+\alpha\kappa W)/36,\\
z_V&=(263W-\bar\alpha\kappa V)/612,&
y_V&=(\kappa V+\alpha W)/36,
\end{aligned}
$$
$$
\Delta_\ell^L
=1_{b_1z_L+e_1E\in p^\ell}
 -1_{b_3z_L+e_3E\in p^\ell},\qquad L=W,V .
\tag{27}
$$
这些门没有取 $\kappa=0$。
定义
$$
\begin{aligned}
g_{\chi,a}(\ell)
 &=\int_{\{Y,Z,W,V,E\ {\rm unit}\}}
       \Delta_\ell\,\frac ZY E^a\phi_{a,\infty}\,d\mu_{\chi,0},\\
h_{\chi,a}^W(\ell)
 &=\int_{\{V,E\ {\rm unit}\}}
       \Delta_\ell^W\,\frac{z_W}{y_W}
                E^a\phi_{a,\infty}\,d\mu_{\chi,1}^W,\\
h_{\chi,a}^V(\ell)
 &=\int_{\{W,E\ {\rm unit}\}}
       \Delta_\ell^V\,\frac{z_V}{y_V}
                E^a\phi_{a,\infty}\,d\mu_{\chi,1}^V .
\end{aligned}
\tag{28}
$$
所有三个伙伴仍在这些积分内。
在对应的 V/W-unit 域，$y_L,z_L$ 准确为单位。

对原 primitive 行先在**完整来源**上投影，记为 $p_{\chi,a}$，
则 R737 的源级返回及 (24) 给
$$
\boxed{
p_{\chi,a}(\ell)
=g_{\chi,a}(\ell)+\lambda h_{\chi,a}^W(\ell)
                           +\gamma\lambda h_{\chi,a}^V(\ell),
\qquad\gamma=\chi_A\chi_E .
}
\tag{29}
$$
从原 Y 投影穿过物理 $P_{L,\kappa}$ 时，使用的是
$$
\mathcal P_\chi^{Y_\kappa^L}
 =\omega_{17}(P_{L,\kappa})^{-1}
       \mathcal P_\chi^Y\omega_{17}(P_{L,\kappa}),
\tag{30}
$$
所以 (26) 的轴正是必需的共轭轴。
若误把右边两个投影改成 W/V 球投影，就不会得到 (29)。

特别两个条件质量仍完整地出现在
$$
\frac{z_W}{y_W}=-b_Y+\frac{36\kappa W}{V+\alpha\kappa W},
\qquad
\frac{z_V}{y_V}=\frac{263}{17\alpha}
       -\frac{36\kappa V}{\alpha(\kappa V+\alpha W)} .
\tag{31}
$$
(31) 是整条有理观察，而非仅其首个 W 或 V 负一矩。
$\kappa$ 在固定 p 后不随 N 改变；
其所有高次项都仍在 (28) 中。

## 7. 两条原 Kummer 负一分量各自的有限恒等式

本节中的 $\chi=\tau_k$ 使用 R735 的完整有限向量及同一个转模，
$k=2,4$。那两条投影在原第一 Y 截面上分别固定 $D_{2,17}$、
$D_{4,17}$，并杀掉另一条。
不是由两个好素数的特征猜测这一事实：
它是 R735(12)–(25) 的完整17向量、绝对 splitting 与全来源识别。

令
$$
\mathfrak I_{2,\infty}
=\Omega\,\frac{c_\infty}{a_\infty}I_{2,p},\qquad
\mathfrak I_{4,\infty}
=\Omega\,\frac1{a_\infty}I_{4,p}.
\tag{32}
$$
它们各自非零，并有 R735/R733 的同一 $E_1$ 微分下的实际
代数系数乘一次点 logarithm 表达。

将 R737 的推导在完整有标签来源上先作上述投影，
再作门限制与积分。E/Z 共同深返回、原 Y 反射、
两个斜门的 Y 正交操作都与 Y 环面相容；
W/V 返回则严格使用 (30)。
有限门的交换由 §5 支付。
R734 的完整冻结来源等式因此分别只剩
$(c/a)D_{2,17}$ 与 $(1/a)D_{4,17}$。
重复 §2 的一致极限，得到
$$
\boxed{
\begin{aligned}
&\frac{d_p}{b_Y}\mathscr P
 \sum_{a=0}^{30}\mathscr Q_{\ne a}
 \{\lambda^{r+2}p_{\tau_k,a}(r+2)
                   +c_a\lambda^{r+1}p_{\tau_k,a}(r+1)\}\\
&\qquad=
 \frac{d_p(-1)^r}{b_Y}\lambda^{2r+248}
          U_{31}V_{31}\mathfrak I_{k,\infty}\ne0,
\qquad k=2,4 .
\end{aligned}}
\tag{33}
$$
左边的每个 $p_{\tau_k,a}$ 都必须按 (28)–(29) 保留三条真实支。
(33) 的系数已经固定；它没有再引入一个可自由选择的测试。

这里是从完整 theta/Schwartz 来源等式推导 (33)，
不是对一条已经积分成 $\mathbf C_p$ 数的等式任意施一个“投影”。
原 (11) 中其余局部分量的总和为零，只是
R734 已付整个冻结差恰为两线的结果；
它们在 (28) 的三个单独条带里并未被宣称为零。

## 8. 原完整外部、有限点公式与剩余范围

对原 paired-T 两个外部，先按 R713 的整数旋转
将第二支完全搬回同一个 Y 观察，再取本篇投影。
等价地，在原未搬回的两支上分别用各自共轭的 Y 轴投影。
不能只在其中一支改变投影或保旧 q1 而不换元。

完整域分割恒等式于是仍为
$$
\mathcal O_{\tau_k,\rm pair}^T
=-\mathcal I_{\tau_k,\rm pair}^T .
\tag{34}
$$
对 (34) 作同一两次过滤和 §2 的归一极限，
外部给的正是 (33) 的相反数。
所以本篇没有从各自非零推导原三个中央不可能同时为零。

另一方面，(11)、(33) 已将这一步的 N 依赖准确移除：
取 r=1，只有至多125层的原有限门，
固定系数的正矩权，以及完整 Y、$Y_\kappa^W$、
$Y_\kappa^V$ 的负一观察。
其17向量由 (18)、(20)–(22) 的固定算子给出，
p 门的所有 formal/complex 转换由 (24) 给出。
这是可以直接交给有限 p-Schwartz 点公式的具体输入；
无需展开并截去 (31) 的无限 $\kappa$ 级数。

若进一步使用 R739/R744 的相对点对数独立性，
仍须证明这些**完整同域**来源落在该定理许可的代数点 span。
原 W-quarter 的2处角色不在本篇消失；
尤其涉及 $E_{2312}$ 的返回时，
R744 所需的2处不分歧条件也须单独支付。
不能只凭17球性或同一个范数34就替代这些点公式假设。

本篇不生成新的可重算数据，不增加射线或重新求一个矩阵逆。
新增内容是 (11) 的真实有限门极限、(15)–(22) 的固定17算子，
(23)–(25) 的同门规范平移，以及完整两分量式(28)–(34)。

### 依赖与原文

- [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)、
  [R735](R735-two-type-five-schwartz-and-rank-one-negative-moments.md)。
- [R737](R737-common-depth-elimination-and-native-primitive-strips.md)、
  [R740](R740-original-w-v-spherical-seventeen-tensor-and-mixed-cuts.md)。
- [R715](R715-complete-first-z-source-and-fifty-neutral-returns.md)、
  [R692](R692-original-four-axis-three-state-and-arithmetic-unit-cuts.md)、
  [R698](R698-adjusted-cm-and-thirty-four-layer-arithmetic-words.md)。
- K. Bannai, S. Kobayashi,
  [Algebraic theta functions and the p-adic interpolation of Eisenstein–Kronecker numbers](https://arxiv.org/pdf/math/0610163),
  arXiv:math/0610163v4，Proposition 1.14 及 Proposition 2.19，pp.30–31；
  采用后者第一式，保式(31)的 ordinary 条件及命题后周期代表独立性的说明。
