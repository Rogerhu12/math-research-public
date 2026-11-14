# R385：原强普通窗的零共振与整个 theta 的二阶提升

日期：2026-11-14。**状态：已证明。** 本文在 R356 已付的普通系数窗口内完成 R363 的第一整商。唯一可能的 $z^p$ 共振由原 sigma 规范准确消去；不留下自由参数。由此将 R377 的 whole-theta 代表加强为普通系数模 $p^2$，而不只是在三块除幂目标中比较。原 R382 的高轴 $B_1$ 在这个指定模型中模 $p$ 为零。整个第三精度矩阵和原中央第三聚合只需同一个确定低轴 $A_0$ 与原坐标修正，仍保全部固定残数、Gaussian、公共因子和十三行。

## 1. 同一个原窗口与有限算子

仍取
$$
p=6s-1>83,\quad b=17,\quad
E_b:y^2=x^3+b,\quad D=D_z,\quad
Dx=2y,\quad Dy=3x^2,
$$
并用 R356 的 $\mathcal O,k,\widetilde Z,Z,\kappa_\sigma,\zeta_\sigma$。
在原点 $x=z^{-2}+\cdots,y=-z^{-3}+\cdots$，$w=z^6$。
以下普通系数比较均指有限 Laurent 窗口；不给未付的无限级数整性。

为避免径向 Gaussian 常数的同名混淆，置
$$
a_E=x^2/y,\qquad a_\kappa=p\kappa,\qquad
\lambda_{\rm lin}=(1-3p)^{-1},
$$
$$
D\widetilde Z=1-3p\widetilde Z a_E,\qquad
DZ=1,\quad D^p=0,\qquad
Z=z+O(z^{5p})\pmod p.
\tag{1}
$$
对特征零和特征 $p$ 的同一个有限和分别记
$$
\widetilde I(f)=\sum_{i=0}^{p-2}
 \frac{(-1)^i\widetilde Z^{i+1}D^if}{(i+1)!},
\qquad
I_Z(f)=\sum_{i=0}^{p-2}
 \frac{(-1)^iZ^{i+1}D^if}{(i+1)!}.
\tag{2}
$$
所有阶乘是单位。原 $c_p=\binom{3s-1}{2s-1}b^s$ 为单位。

R356 的普通比较准确为
$$
\zeta_\sigma-\widetilde G_\sigma
 \in p\mathcal O((z))+z^{5p-2}\mathcal O[[z]],
\quad \widetilde G_\sigma=\widetilde I(-x),
\quad [z^p]\zeta_\sigma=0.
\tag{3}
$$
两边在此窗口整；最后一个等式在特征零中准确成立。
因此 R363 的实际商
$$
z_1=(z-\widetilde Z)/p,\qquad
j_1=(\zeta_\sigma-\widetilde G_\sigma)/p
$$
在所用窗口整，$z_1$ 从一次项起，$j_1$ 仅允许一阶极。
下文使用它们的约化，必要时写横线。

沿 R363 定义
$$
e=3Za_E,\qquad
\Pi_Z(f)=\sum_{i=0}^{p-1}\frac{(-Z)^iD^if}{i!},
$$
$$
\tau_p=\overline{\frac{D^{p-1}(-x)/(p-1)!-u_\sigma}{p}},
\quad u_\sigma=-[z^{p-1}]x,
$$
$$
j_0=\bar j_1-c_pZ^{p-1}\bar z_1,\qquad
\mathfrak F_p=Z^{p-1}\tau_p+e\Pi_Z(-x).
\tag{4}
$$
这些都是原指定整商；准确有
$$
D\bar z_1=e,\qquad Dj_0=\mathfrak F_p.
\tag{5}
$$
$\mathfrak F_p$ 全局有理，$j_0$ 此时只指实际局部整商。
令
$$
G_1=I_Z(\mathfrak F_p),\qquad Z_1=I_Z(e).
\tag{6}
$$

## 2. 强窗使第二 forcing 的原点 Cartier 常数消失

**命题1。** 在原点
$$
D^{p-1}\mathfrak F_p=O(z^{6p}),
\qquad
j_0-G_1=\beta Z^p+O(z^{5p-2})
\tag{7}
$$
对某个确定的 $\beta\in k$ 成立。

**证明。** R363 已付 $\mathfrak F_p$ 至多二阶极，主部 $-z^{-2}$。
$D^{p-1}$ 杀掉该主部；其结果是 $p$ 次幂，在原点正规。
它的常数为
$(p-1)![z^{p-1}]\mathfrak F_p$。
但 (3) 保证 $j_0$ 在含 $z^p$ 的普通窗口整；
(5) 给
$[z^{p-1}]\mathfrak F_p=p[z^p]j_0=0$ 于 $k$。
所以该常数确为零。

$\mathfrak F_p$ 的 $\mu_6$ 型是负二，而 $p-1\equiv4\bmod6$，
故 $D^{p-1}\mathfrak F_p$ 型零。
一个在原点正规的型零 $p$ 次幂，常数去掉后首次可能项为 $z^{6p}$；
这证明第一式。

有限求导身份给
$$
DG_1=\mathfrak F_p+Z^{p-1}D^{p-1}\mathfrak F_p.
$$
附加项从 $z^{7p-1}$ 起，超出 (3) 的窗口。
$j_0,G_1$ 具有同一个 $1/z$ 主部和负一型。
所以它们的差在所用窗口只含导数为零的同型项：
指数为 $mp$，且 $m\equiv1\bmod6$。
唯一可能项为 $z^p$；下一项 $z^{7p}$ 超出窗口。
由 (1) 可用 $Z^p$ 代替它，得到 (7)。$\square$

这里消去的是该有理 $p$ 次幂在原点的常数，并未把整个
$D^{p-1}\mathfrak F_p$ 置为零；R363 的全局非零 Cartier 链仍成立。

## 3. 原 sigma 规范准确给 beta 等于零

**命题2。**
$$
\boxed{\beta=0.}
\tag{8}
$$

**证明。** 先在特征零中，把 (2) 的形式变量 $\widetilde Z$ 换为 $z$：
$$
I_z(f)=\sum_{i=0}^{p-2}
 \frac{(-1)^iz^{i+1}D^if}{(i+1)!},
\qquad
H_{f,z}=\sum_{i=0}^{p-2}\frac{(-z)^iD^if}{i!}.
$$
原有限普通窗口内 $\widetilde Z=z-pz_1$，所有分母都是单位，
所以逐项有限 Taylor 展开准确给
$$
\widetilde G_\sigma
\equiv I_z(-x)-p z_1 H_{-x,z}\pmod{p^2}.
\tag{9}
$$
这里只读取 $z^p$ 系数；所需的 $x,\widetilde Z,z_1$ 系数都在
(3) 已付的普通窗口内。高于该窗口的项不可能经 (9) 的有限导数
降到所读系数，因为每次导数同时伴相应的 $z$ 次幂。

对任意 Laurent $f$，$I_z(f)$ 的 $z^p$ 系数为
$$
[z^{p-1}]f\,
 \sum_{i=0}^{p-2}\frac{(-1)^i}{i+1}\binom{p-1}{i}=0.
\tag{10}
$$
此为特征零准确等式：
完整到 $i=p-1$ 的有限和是 $1/p$，被删的末项也是 $1/p$。
没有将一个非整 $1/p$ 单项约化；(10) 的实际部分和全由单位分母组成。

模 $p$ 后，R363 给
$$
H_{-x,z}=\Pi_Z(-x)+c_pZ^{p-1}
\tag{11}
$$
至所需窗口。$\Pi_Z(-x)$ 是 $p$ 次幂，在原点至多二阶极，
所以实际正规；其型为负二，首次可能项从 $z^{2p}$ 起。
又
$$
[z]\bar z_1=\overline{(1-\lambda_{\rm lin})/p}=-3.
$$
结合 (9)、(10) 与 $[z^p]\zeta_\sigma=0$，得到
$$
[z^p]\bar j_1=[z^p](\bar z_1H_{-x,z})=-3c_p,
$$
$$
[z^p]j_0=-3c_p-c_p(-3)=0.
\tag{12}
$$
同理在 (6) 中，由 $Z=z+O(z^{5p})$ 且
$\mathfrak F_p$ 至多二阶极，
其 $z^p$ 系数可直接用 $I_z(\mathfrak F_p)$ 计算；
同一个 (10) 给 $[z^p]G_1=0$。
于是 (7) 的 $\beta$ 正是零。$\square$

Gaussian 整重标 $\kappa=\kappa_\sigma+\Delta$ 不改变本结论：
R363 的准确式
$$
j_{1,\kappa}-j_{1,\sigma}
=-\delta_\kappa(z^p-\widetilde Z^p)/p
\in p\mathcal O[[z]]
$$
于同一窗口成立。因此 (8) 支持同一原 Gaussian 的全部合法重分解，
没有另选有利的 theta。

## 4. 第一整商的全部普通系数

R377 的坐标第一商已证明
$$
\bar z_1=Z_1+O(z^{5p}).
$$
配合 (4)、(7)、(8)，现在得到
$$
\boxed{\bar j_{1,\kappa}
=G_1+c_pZ^{p-1}Z_1+O(z^{5p-2}).}
\tag{13}
$$
定义指定的实际有理函数
$$
G_1^\sharp=G_1+c_pZ^{p-1}Z_1,\qquad
r_1^\sharp=(x/y)G_1^\sharp\in k(t).
\tag{14}
$$
(13) 保留原先落入普通高轴、在 R363 中仅凭
$w^s=p\epsilon$ 支付的那一项。

此修正保持 R363/R377 的全部真实局部条件：

- 在每个非原点测试点 $Z=0,\ x,y$ 为单位，$e=0$，
  所以 $Z_1=I_Z(e)$ 至少有二阶零；新增项至少有 $p+1$ 阶零。
  因而 $r_1^\sharp$ 仍具有原准确双零
  $-3x(P)^4Z^2/(2y(P)^2)+O(Z^3)$。
- 在原点，新增项从 $z^p$ 起，乘 $x/y$ 后从 $w^s$ 起；
  故 $r_1^\sharp(O)=-1$。
- 在 $x=0$，$Z$ 一阶零，$e=3Zx^2/y$ 至少三阶零，
  故 $Z_1$ 至少四阶零；新增项不破坏原 $r_1$ 至少三阶零。
- 在每个非零二挠点，$Z$ 的极阶为 $p$，
  $e$ 的极阶至多 $p+1$，所以 (2) 给
  $\operatorname{pole}Z_1\le p^2+p-1$。
  新增 $Z^{p-1}Z_1$ 的极阶至多 $2p^2-1$，
  与原 $G_1$ 的已付上界相同。
  乘 $x/y$ 后至多 $2p^2$；不产生其他极。

因此
$$
N_1^\sharp=(1-t)^{p^2}r_1^\sharp\in k[t],\quad
\deg N_1^\sharp\le p^2-1,\quad
B_p(-t)^2\mid N_1^\sharp.
\tag{15}
$$
沿 R363 的真实整测试多项式 $\mathscr B_p$，
提升商 $N_1^\sharp/B_p(-t)^2$，保持上述次数，
并准确指定常数为 $-\eta_{\rm lin}$，其中
$\eta_{\rm lin}=(c_{\rm lin}+1)/p\equiv1\bmod p$。
置
$$
\widetilde r_1^\sharp
=\frac{\mathscr B_p(-t)^2\widetilde Q_1^\sharp(t)}
       {(1-t)^{p^2}},\qquad
G_\kappa^{(2),\sharp}
=\widetilde G_\kappa+p(y/x)\widetilde r_1^\sharp .
\tag{16}
$$
整系数提升总能按 (15) 完成；指定常数与原约化 $-1$ 相容。

(13) 现在给强普通比较
$$
\boxed{
G_\kappa^{(2),\sharp}\equiv\zeta_\kappa
       \pmod{p^2,z^{5p-2}}.
}
\tag{17}
$$
这个比较的精度是普通 Laurent 系数。
(16) 在原点极部准确为 $1/z$，在 $x=0$ 至少二阶零，
在所有真正 lifted 测试点值为零且导数为 $-x$。
它属于原共同整环 $\mathcal O[x,y,1/y]/(y^2-x^3-b)$，
全局只有原固定二挠极；R363 的整原像配对仍原样成立。

## 5. 整个原 theta 的普通模 p² 提升

保持 R377 的同一个 $\widetilde H_\kappa=\widetilde I(\widetilde G_\kappa)$
和全部原点常数。定义
$$
\widetilde\chi=(1+\widetilde Z a_E)^p/\widetilde Z,
$$
$$
F_1^\sharp=\frac1p
 \left(G_\kappa^{(2),\sharp}
       -D\widetilde Z/\widetilde Z
       -D\widetilde H_\kappa+\widetilde\chi\right).
\tag{18}
$$
与 R377 相同的准确消分母式
$$
\widetilde\chi-D\widetilde Z/\widetilde Z
=4pa_E+\sum_{j=2}^{p-1}\binom pj
       \widetilde Z^{j-1}a_E^j+\widetilde Z^{p-1}a_E^p
$$
证明分子在原共同平坦整环内，且模 $p$ 为零。
所以 (18) 全局可除以 $p$，不只是在原点取整商。

其约化在 $O$ 正规且型负一，在 $x=0$ 至少二阶零，
在每个原非原点测试点值为 $4a_E(P)$。
二挠极阶仍至多 $2p^2-1$，因为 (16) 没有增加原极界。
令
$$
H_1^\sharp=I_Z(\overline{F_1^\sharp}).
$$
沿 R377 的同一真实 $B_p$ 因子、次数和零常数约束取整提升
$\widetilde H_1^\sharp$。于是
$$
H_1^\sharp(O)=0,\qquad
H_1^\sharp(P)=0,\qquad DH_1^\sharp(P)=4a_E(P),
$$
$$
\operatorname{pole}_{E[2]\setminus O}H_1^\sharp\le3p^2-3.
\tag{19}
$$
没有增加移动测试点。

仍用 R377 的准确常数
$$
C_H=-c_{\rm lin}\sum_{j=1}^{p-1}\lambda_{\rm lin}^j/j,\qquad
c_*=\lambda_{\rm lin}^{34}E_{p-1}(34C_H)\in1+p^2\mathcal O,
$$
定义
$$
\Theta_\kappa^\sharp
=c_*^{-1}(\widetilde Z^2x)^{17}
 E_{p-1}\!\left(34(\widetilde H_\kappa
                           +p\widetilde H_1^\sharp)\right),
\qquad
g^\sharp=\Theta_\kappa^\sharp(1+8t).
\tag{20}
$$
它们的原点值准确为一。

**定理1。**
$$
\boxed{
g^\sharp\equiv g_\kappa
 \pmod{p^2,w^{5s-1}}
}
\tag{21}
$$
是普通系数的比较。

**证明。** 令
$$
\ell_\kappa=\log(\sigma/z)-\kappa w^s/34,\qquad
\mathfrak L=\log(z/\widetilde Z)
                   +\ell_\kappa-\widetilde H_\kappa.
$$
R377 已付
$\mathfrak L(0)=-\log\lambda_{\rm lin}-C_H\in p^2\mathcal O$。
现在由强普通式 (17)，在整个导数窗
$z^{6j-1}$、$j<5s-1$ 上都有
$$
D\mathfrak L=pF_1^\sharp-\widetilde\chi+O(p^2).
\tag{22}
$$

必须保留 $\widetilde\chi$ 的全局含义，只在这个短窗支付它：
$1+\widetilde Za_E$ 的常数是 $1-\lambda_{\rm lin}\in p\mathcal O$，
正次从 $w$ 起。其 $p$ 次幂在 $w^j$ 的系数被
$p^{p-j}$ 整除；乘 $1/\widetilde Z=z^{-1}$ 乘整单位后，
所读系数仍至少有此下界。当前 $j<5s-1$，
所以 $p-j\ge s+1>2$。因此 (22) 中的这一项在整个所用窗为零模 $p^2$。

有限原函数的导数误差为
$$
DH_1^\sharp-\overline{F_1^\sharp}
=Z^{p-1}D^{p-1}\overline{F_1^\sharp}.
$$
右侧从 $z^{6p-1}$ 起：后一个 $p$ 次幂在原点正规，
型为一，首次可能幂为 $z^{5p}$。
这个误差也超出所用窗口。因此
$D(\mathfrak L-p\widetilde H_1^\sharp)=0\bmod p^2$
到全部 $j<5s-1$。积分分母 $6j$ 都是单位，
因为 $5s-2<p$；加上已付常数，得
$$
\mathfrak L\equiv p\widetilde H_1^\sharp
            \pmod{p^2,w^{5s-1}}.
\tag{23}
$$

最后核有限指数尾。其自变量的常数属于 $p\mathcal O$，
正次从 $w$ 起。遗漏的第 $r\ge p$ 项读 $w^j$ 的赋值至少
$r-j-v_p(r!)$。该函数在 $r\ge p$ 时至少为 $p-1-j$：
可用 $v_p(r!)\le(r-1)/(p-1)$，或逐段基 $p$ 阶乘公式证明。
当前 $j\le5s-2$，此下界至少 $s\ge14$。
故有限 $E_{p-1}$ 与完整局部指数在此窗相同模 $p^2$。
R377 已付的 $c_*$ 归一仍适用。
(23) 乘回准确 $(\widetilde Z^2x)^{17}(1+8t)$，
得到 (21)。$\square$

此处没有把全局 $\widetilde\chi$ 或它的固定二挠残数删去。
它们已进入 (18)，只在明确的原点短窗使用了赋值下界。

## 6. 原第三精度矩阵只余确定低轴

在这个指定模型中，定义原低窗
$$
\mathcal L_{<s}(t)=
 \left[\log(1+8t)+
 \sum_{j=1}^{s-1}\frac{17}{3j}
              \frac{(1/3)_j}{(5/6)_j}t^j\right]_{<s},
$$
$$
\boxed{
A_0^\sharp(t)=\frac1{p^2}
  [\,\mathcal L_{<s}(t)-\log g^\sharp(t)\,]_{<s}
  \in t\mathcal O[t]_{<s}.
}
\tag{24}
$$
这是已知的有限有理系数公式；(21) 支付它的整性。
$t(w)=-bw+\cdots$ 为原整单位换元。
令
$$
g^{\sharp,[3]}=g^\sharp(1+p^2A_0^\sharp).
\tag{25}
$$

**定理2。** R382 的高轴修正对当前模型满足
$$
\boxed{B_1^\sharp\equiv0\pmod p,}
\tag{26}
$$
且
$$
\boxed{
g^{\sharp,[3]}\equiv g_\kappa\pmod{p^3\Gamma_T},
\qquad T\le3s.
}
\tag{27}
$$

**证明。** (21) 使普通低、中、高三个所需块全部相同模 $p^2$。
(24) 进一步把低块 $r<s$ 消至 $p^3$。
对中块 $s\le r<2s$，原三块要求普通系数模 $p^2$；
高块 $2s\le r<3s$ 只要求模 $p$。
(25) 不破坏这两块，故得 (27)。

若仍按 R382 的完整原高窗对数定义
$$
B_1^\sharp=\frac1{pt^s}
 [\,\mathcal L^\kappa_{<2s}
       -\log(g^\sharp(1+p^2A_0^\sharp))\,]_{[s,2s)},
$$
其分子由 (21) 全被 $p^2$ 整除，所以 (26) 成立。
这里没有把旧模型的 $B_1$ 免费置零；变更模型的准确代价
正是 (13) 的 $c_pZ^{p-1}Z_1$，已完整进入 (18)–(20)。$\square$

坐标仍须使用 R382 的确定第三位：
$$
\widetilde Z_2=\widetilde Z+p\widetilde I(3\widetilde Z a_E),\quad
W(t)=(-t/b)h(t)^6,
$$
$$
C_0(t)=\frac1{6p^2}
 [\,W(t)/\widetilde Z_2(t)^6-1\,]_{<s},\qquad
\widetilde Z_3=\widetilde Z_2(1+p^2C_0),
\quad
\epsilon^{[3]}=\widetilde Z_3^{p+1}/p.
\tag{28}
$$
它与本文的提升选择无关；R382 已证明
$\epsilon^{[3]}\equiv\epsilon\bmod p^3\Gamma_T$。
因此每条完整原 charge $N=n+40$ 列取
$$
\mathcal S_{n,j}^{\sharp,[3]}
=\left(\frac{g^{\sharp,[3]}}{1+8t}\right)^N
 F_{n,j}(t)e_2(Na_\kappa\epsilon^{[3]}),
\tag{29}
$$
就得到逐项准确的
$$
\boxed{M^{\sharp,[3]}\equiv M^{\rm orig}\pmod{p^3}.}
\tag{30}
$$
原 $F_{n,j}$、$P_{134}$、$U_0/G_0$、$Z^{-78}$ 和十三行全部在式内。
相同来源、目标、首次提升像和真正 $C_2$ 因而保持不变。
可直接使用 R382 的完整第三精度 Serre 对偶，或在同一 $K_2$ 输入上
使用 R380 已付的一次对偶；所有原测试点与固定二、三挠边界仍须求总和。

## 7. 同一个低轴读取原中央第三聚合

令原角因子为
$$
a_{\rm ang}(t)=t(t-1)(16t^2+4t+7),
$$
并按 R382 记
$$
\widehat S=g_\kappa\,a_{\rm ang}(t)/(7b),\quad
c_j=[w^{js}]\widehat S,\qquad
\widehat S^\sharp=g^\sharp\,a_{\rm ang}(t)/(7b),\quad
c_j^\sharp=[w^{js}]\widehat S^\sharp .
$$
角因子从 $w$ 起，故从 (25)–(27) 在准确端点得到
$$
\boxed{\begin{aligned}
&a_\kappa^2c_1-pa_\kappa c_2+2p^2c_3\\
&\equiv
 a_\kappa^2c_1^\sharp-pa_\kappa c_2^\sharp+2p^2c_3^\sharp
 +p^2a_\kappa^2[w^s](A_0^\sharp\widehat S^\sharp)
 \pmod{p^3}.
\end{aligned}}
\tag{31}
$$
证明是逐项提取：(25) 对 $c_1$ 的贡献须保到 $p^2$，
对 $c_2$ 的 $p^2$ 贡献再乘 $p$ 后消失模 $p^3$，
对 $c_3$ 同理。原 $c_3$ 只读径向系数至 $w^{3s-1}$，
未添加新的第 $3s$ 行。

R382 的完整 Gauss 尾仍给
$$
J'_S\equiv
  \frac p{a_\kappa}c_1
 -\frac{p^2}{a_\kappa^2}c_2
 +\frac{2p^3}{a_\kappa^3}c_3\pmod{p^4}.
\tag{32}
$$
所以原完整中央失败必满足 (31) 的右端为零模 $p^3$。
本篇使该指定聚合与原 $d_2$ 使用同一个确定 $A_0^\sharp$；
不再留下另一个模 $p$ 高轴函数。
但 (31) 仍是一条中央聚合，(30) 仍是整个真实矩阵身份：
两者本身不推出任意 $C_2$ 对偶、任意测试残数分别为零。
跨 $p$ 的完整中央非零和固定 rank 二曲线的主目标仍未完成。

## 依赖与同步

- [R356](R356-original-gaussian-zeta-primitive-and-all-test-pole-normalization.md)：原普通窗口、准确 sigma 共振及特征零线性常数。
- [R363](R363-original-first-frobenius-quotient-and-second-rational-connection.md)：实际第一商、全局 Cartier 链、原测试双零与固定极界。
- [R377](R377-whole-original-theta-first-lift-and-integral-serre-model.md)：原 whole-theta、坐标第一商、全部整 frame 和 Serre 规范。
- [R380](R380-original-low-axis-correction-and-full-second-bockstein-model.md)、[R382](R382-original-third-central-aggregate-and-full-third-precision-model.md)：同一 $K_2/C_2$、原低轴、完整第三精度及全中央尾。

全篇为参数证明，没有扫描目标素数，也没有把大极度代表称为新的低成本来源。
执行环境仍不可用期间，仅按根规则传送此小文本；API 同步不冒称实际 git pull。
