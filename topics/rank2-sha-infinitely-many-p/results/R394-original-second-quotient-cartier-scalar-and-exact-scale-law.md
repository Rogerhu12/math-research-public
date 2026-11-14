# R394：原第二整商的 Cartier 标量、单系数公式与准确尺度律

日期：2026-11-14。**状态：已证明。** R388 的实际 $Q_3\,dz$ 经两次 Cartier 后有一个明确的一维系数。本文把它化为一个真实二挠点的单个整 Laurent 系数，支付其中的第一层抵消，并证明其对允许的 Gaussian 和整提升变更不变。另一方面，它在相容的 Weierstrass 同构下有一个非零的 logarithmic 尺度项；整个原低窗矩阵、$A_0$ 及中央条件却经准确运输保持。因此这个单独标量不能代替完整基准加修正的规范不变量。

## 1. 同一个原整商

取
$$
p=6s-1>83,\quad b=17,\quad E_b:y^2=x^3+b,\quad
D=D_z,\quad Dx=2y,\quad Dy=3x^2,\quad a_E=x^2/y .
$$
所有 Cartier 计算可在 $k=\mathbf F_{p^2}$ 上进行。
整提升在相应不分歧整环 $\mathcal O$ 中，仍用
$$
\mathcal A=\mathcal O[x,y,1/y]/(y^2-x^3-b),\qquad
t=-b/x^3.
$$
保留 R363/R388 的全部实际数据：
$$
\widetilde Z=\mathscr R_p(x)/y^p,\quad
\mathscr R_p'(x)=\tfrac12(x^3+b)^{(p-1)/2},\quad
D\widetilde Z=1-3p\widetilde Za_E,\quad DZ=1,\quad D^p=0,
$$
$$
e=3Za_E,\quad Z_1=I_Z(e),\quad
C_e=D^{p-1}e=B_e^p,\quad
C_F=D^{p-1}\mathfrak F_p=B_F^p.
\tag{1}
$$
有限 primitive 是
$$
I_Z(f)=\sum_{i=0}^{p-2}\frac{(-1)^iZ^{i+1}D^if}{(i+1)!}.
$$
写
$$
c_p=\binom{3s-1}{2s-1}b^s,\qquad
\lambda_p=\frac12b^{5s-2}\frac{(3s-1)!}{(4/3)_{3s-1}}
\quad\text{于 }\mathbf F_p^\times .
\tag{2}
$$
R363 已证明
$$
\mathcal C(e\,dz)=\lambda_p(da_E-x\,dz),\qquad
\mathcal C^2(\mathfrak F_p\,dz)=-c_p\mathcal C(e\,dz).
\tag{3}
$$

为明确本文计算的对象，R388 的定义是
$$
\begin{aligned}
T_2={}&\widetilde Z^{p-1}
 +(p-1)p\widetilde Z^{p-2}\widetilde Z_1
 +\binom{p-1}{2}p^2\widetilde Z^{p-3}\widetilde Z_1^2,\\
\widetilde\Xi_2={}&
 \widetilde Z^{p-1}\widetilde B_F^{\,p}
 +\widetilde c_p\widetilde Z^{2p-2}\widetilde B_e^{\,p},\\
Q_2={}&(-x-u_\kappa T_2-DG_2+p\widetilde\Xi_2)/p^2,\\
Q_3={}&Q_2-u_\kappa(p-1)\widetilde Z^{p-1}C_0(t).
\end{aligned}
\tag{4}
$$
这里 $Q_2,Q_3\in\mathcal A$ 的全局整除已付；
$C_0$ 是同一真实第三坐标，而不是任意常数。
另一个原整商仍记为 $K_2$。在约化后，$Q_3$ 和 $K_2$ 在原点正规，
只在非零二挠点有极，其界分别为
$$
3p^2-p-2,\qquad 3p^2-2.
\tag{5}
$$
函数的 $\mu_6$ 型分别是负二、负一。
本文没有更换这些全局代表为具有同一原点截断的任意函数。

## 2. 实际第二 Cartier 像

**定理1。** 存在唯一 $c_Q,c_K\in k$，使
$$
\boxed{\mathcal C^2(\bar Q_3\,dz)
=c_Q(da_E-x\,dz)=3bc_Q\,x\,dz/y^2,}
\tag{6}
$$
$$
\boxed{\mathcal C^2(\bar K_2\,dz)
=c_Kx^2\,dz/y^3=-\frac{c_K}{6}d(y^{-2}).}
\tag{7}
$$
从而
$$
\mathcal C^3(\bar Q_3\,dz)=-c_Q^{1/p}c_p\,dz,\quad
\mathcal C^4(\bar Q_3\,dz)=0,\quad
\mathcal C^3(\bar K_2\,dz)=0.
\tag{8}
$$

**证明。** 在二挠点取参数 $v=y$。函数 $Q_3$ 为偶型，
所以 $Q_3\,dz$ 的 Laurent 指数为偶数。
由 (5)，两次 Cartier 后至多三阶极；奇偶性再将其压至双极。
在原点仍正规，且 $p^2\equiv1\bmod6$，所以两次 Cartier 保持微分的负一型。
将这种微分乘 $y^2/dz$，得到 $L(6O)$ 中负二型的函数，
该空间恰由 $x$ 张成。这给 (6)。

同理 $K_2$ 为奇函数，两次 Cartier 后至多三阶极。
乘 $y^3/dz$ 后落在 $L(9O)$ 的二型部分，恰由 $x^2$ 张成。
直接求导给 $d(y^{-2})=-6x^2dz/y^3$，得到 (7)。
再用 $\mathcal C(x\,dz)=c_pdz$、$\mathcal C(dz)=0$ 和 exact 微分的
Cartier 为零，得到 (8)。$\square$

这个一维归属本身不判定 $c_Q$ 是否为零。

## 3. 一个真实 Laurent 系数，以及不能省去的整除

固定非零二挠点 $T$，写 $x_T^3=-b$、$v=y$，
并在其不分歧整提升中计算。因为
$$
dz=\frac{dv}{3x^2},
$$
定义整 Laurent 系数泛函
$$
\ell_T(f)=
[v^{-p^2-1}]\frac{f}{3x^2}.
\tag{9}
$$
由 (6) 的首主部是 $-c_Qx_T^2v^{-2}dv$，
有准确公式
$$
\boxed{c_Q=-x_T^{-2}\ell_T(\bar Q_3)^{1/p^2}.}
\tag{10}
$$
在 $k=\mathbf F_{p^2}$ 上最后的幂根是恒等。
由奇偶性及 (5)，这是此处唯一可能产生第二 Cartier 双极的原指数；
没有遗漏其邻接的高极项。

在 $T$，特征零的坐标方程准确变成
$$
\frac{d\widetilde Z}{dv}+\frac p v\widetilde Z
=\frac1{3x^2}.
$$
右边正规且为偶函数，因此
$$
\boxed{\widetilde Z=A_Tv^{-p}+Z_+(v)}
\tag{11}
$$
中只有一个负 Laurent 项。有限 beta 和给
$$
A_T=\mathscr R_p(x_T)
=\frac{x_Tb^{3s-1}}2\frac{(3s-1)!}{(4/3)_{3s-1}}.
\tag{12}
$$
R371 的真实二挠主部又给
$$
c_p\bar A_T=-x_T^{2p}.
\tag{13}
$$
结合 (2)、(12)，得到一个简化：
$$
\lambda_p=\bar A_Tb^{2s-1}/x_T,\qquad
\boxed{c_p\lambda_p=b^{p-1}=1.}
\tag{14}
$$
最后一步使用本来的有理 $p$ 单位 $b$，未使用任何中央行。

先取原 sigma Gaussian，故 $u_\sigma=-[z^{p-1}]x$。
置
$$
\widetilde A=\widetilde Z^{p-2}\widetilde Z_1,\qquad
\widetilde B=\widetilde Z^{p-3}\widetilde Z_1^2,
$$
$$
h_T=\ell_T\{\widetilde\Xi_2-u_\sigma(p-1)\widetilde A\}.
\tag{15}
$$

**定理2。** $h_T\in p\mathcal O$，并且
$$
\boxed{
c_Q=-x_T^{-2}\,
 \overline{\,h_T/p+\widetilde c_p\ell_T(\widetilde B)\,}.
}
\tag{16}
$$
右边只需原已指定有限有理函数的一个整 Laurent 系数。
(15) 的括号不被擅自宣称为整个函数上的 $p$ 倍数。

**证明。** 先支付其第一层抵消。于特征 $p$ 记
$$
X=Z^{p-1}C_F,\qquad Y=c_pZ^{2p-2}C_e.
$$
因为 $\mathcal C(\mathfrak F_pdz)=-B_Fdz$，(3) 给
$$
\mathcal C^2(Xdz)=c_p\mathcal C(e\,dz),\qquad
\mathcal C(Ydz)=0.
\tag{17}
$$
后式也由 $Ydz=-c_p\,d(Z^{2p-1}C_e)$ 直接得到。
同时
$$
d(Z^{p-1}Z_1)=
(-Z^{p-2}Z_1+Z^{p-1}e+Z^{2p-2}C_e)\,dz.
$$
利用 $e=3Za_E$ 和
$\mathcal C(a_Edz)=a_Edz$，可得
$$
\mathcal C(Z^{p-2}Z_1dz)=e\,dz.
\tag{18}
$$
由于 $\overline{u_\sigma(p-1)}=c_p$，(17)、(18)
使 (15) 括号的第二 Cartier 像为零，故其指定系数模 $p$ 为零。

再把 (4) 逐项代入 (9)。$-x$、$T_2$ 的第一项及 $C_0$ 校正
都没有足以到达 $v^{-p^2-1}dv$ 的极。
$\widetilde G_\sigma=\widetilde I(-x)$ 的极阶至多 $p^2-p-1$：
最高一项含 $D^{p-2}x$，这是正规奇函数，在二挠点有零。
又 $G_2=\widetilde G_\sigma+pL$，所以
$[v^{-p^2}]G_2\in p\mathcal O$。
因此 $-dG_2/p^2$ 在 (9) 的贡献模 $p$ 为零。
剩下的两项准确为
$$
h_T/p-u_\sigma\binom{p-1}{2}\ell_T(\widetilde B).
$$
因 $\bar u_\sigma=-c_p$、$\binom{p-1}{2}\equiv1\bmod p$，
得到 (16)。$\square$

(16) 保留了真正的下一位 $h_T/p$；第一层抵消不能代替它。

## 4. 原允许提升与 Gaussian 的相容性

改变 $\widetilde H_1$ 为 $\widetilde H_1+pC$，
只使 $K_2$ 变为 $K_2-DC$，不改变 $Q_3$。
改变 $G_2$ 为 $G_2+p^2H$，使 $Q_3dz$ 只增加 $-dH$。
二者都不改变 (6)。

$\widetilde B_F,\widetilde B_e$ 的提升增加一个 $p$ 倍数时，
其 $p$ 次幂只改变 $p^2$ 倍数，故 $\bar Q_3$ 不变。
$\widetilde c_p$ 增加 $p\eta$ 时，$\bar Q_3dz$ 增加
$\eta Z^{2p-2}C_e dz$，仍为 exact。
这些断言只涉及实际允许的同一整模型，未自由改变来源。

Gaussian 变更也有完整 exact 公式。
设 $\delta$ 为其整参数差；按 R385 同步取
$$
u_{\rm new}=u_\sigma+p\delta,\qquad
G_{2,\rm new}=G_{2,\sigma}-\delta\widetilde Z^p.
$$
在 (4) 中保留完整二项式后，约化差为
$$
\Delta\bar Q_3
=\bar\delta\{Z^{p-2}Z_1-Z^{p-1}e\}.
$$
所以
$$
\boxed{
\Delta\bar Q_3\,dz
=-\bar\delta\,d\{Z^{p-1}Z_1+Z^{2p-1}C_e\}.
}
\tag{19}
$$
$C_0$ 项的差含 $p$，已经在此约化中支付。
因此 (6) 对原合法 Gaussian 重分解不变。
这仍不允许省略整个矩阵的 $e_2(Na_\kappa\epsilon)$。

## 5. 真正的 Weierstrass 尺度律

这一节比较相容的两个 Weierstrass 模型。
令 $b,b'$ 为有理 $p$ 单位，$b'=\alpha^6b$，
取 $\alpha$ 于不分歧二次整环中；约化在 $\mathbf F_{p^2}$。
准确同构为
$$
x'=\alpha^2x,\quad y'=\alpha^3y,\quad
z'=\alpha^{-1}z,\quad D'=\alpha D,\quad t'=t.
\tag{20}
$$
所有提升相容运输，特别取
$$
\widetilde Z'=\alpha^{-1}\widetilde Z,\quad
\widetilde Z_1'=\alpha^{-1}\widetilde Z_1,\quad
u_\sigma'=\alpha^{p+1}u_\sigma,\quad G_2'=\alpha G_2,
$$
$$
\widetilde c_p'=\alpha^{p+1}\widetilde c_p,\quad
\widetilde B_F'=\alpha^{p+1}\widetilde B_F,\quad
\widetilde B_e'=\alpha^{1-p}\widetilde B_e,\quad C_0'=C_0.
\tag{21}
$$
这些确为所需 Frobenius 根的提升：
$\mathfrak F_p'=\bar\alpha^2\mathfrak F_p$，
$C_F'=\bar\alpha^{p+1}C_F$，
$C_e'=\bar\alpha^{p-1}C_e$；
用 $\bar\alpha^{p^2-1}=1$ 即核定 (21) 的 $p$ 次幂。

设
$$
\Lambda=\alpha^{p^2-1}\in1+p\mathcal O,\qquad
\eta=\overline{(\Lambda-1)/p}.
\tag{22}
$$
本节 $b,b'$ 有理，故 $\Lambda=(b'/b)^{(p^2-1)/6}$ 有理，
$\eta\in\mathbf F_p$。
将 (21) 代入 (4)，除 $\widetilde\Xi_2$ 外的各项都准确乘 $\alpha^2$，
而两项 Frobenius lift 分别多出 $\Lambda,\Lambda^{-1}$：
$$
\widetilde\Xi_2'
=\alpha^2\{
 \Lambda\,\widetilde Z^{p-1}\widetilde B_F^{\,p}
 +\Lambda^{-1}\widetilde c_p
       \widetilde Z^{2p-2}\widetilde B_e^{\,p}\}.
$$
因此
$$
\boxed{\bar Q_3'=\bar\alpha^2\{\bar Q_3+\eta(X-Y)\}.}
\tag{23}
$$

**定理3。** 对相容的原整模型，准确有
$$
\boxed{c_Q(b')=c_Q(b)+
 \overline{\frac{\alpha^{p^2-1}-1}{p}}.}
\tag{24}
$$

**证明。** $\mathcal C^2$ 在 $\mathbf F_{p^2}$ 上线性，
而 $dz'=\alpha^{-1}dz$、
$da_E'-x'dz'=\alpha(da_E-xdz)$。
将 (17)、(14) 代入 (23) 即得 (24)。$\square$

两个具体推论是
$$
\boxed{c_Q(17)=c_Q(1)+\tfrac16q_p(17),\quad
q_p(17)=(17^{p-1}-1)/p\bmod p,}
\tag{25}
$$
以及
$$
\boxed{\alpha=1+p\tau\quad\Longrightarrow\quad
c_Q((1+p\tau)^6b)=c_Q(b)-\bar\tau.}
\tag{26}
$$
(25) 不判定 $c_Q(1)$ 或 Fermat 商非零。
(26) 比较的是同一曲线的两个有理同构模型。

## 6. 完整原矩阵的运输及低窗不变

(24) 没有产生新的中央输入。
准确说明这一点需要同时保留源、目标、Gaussian 和基准。

在 (20) 下，
$$
\sigma_{b'}(z/\alpha)=\alpha^{-1}\sigma_b(z),\qquad
\Theta_{b'}(z/\alpha)=\Theta_b(z),\qquad
S_{b'}(z/\alpha)=\alpha^{-6}S_b(z).
$$
因此原 weighted 三生成元
$$
A=7bS(z),\qquad B=7bS(\delta z),\qquad C=7bS(2z)
$$
作为 $t$ 的截面准确不变；其 canonical 来源及导子也相容不变。
公共 $G_0$ 不被删除。由于 $w'= \alpha^{-6}w$，
其 $w^{13}U_0$ 分解同步给 $U_0'=\alpha^{78}U_0$，
仍是同一个实际目标运输，十三行全部保留。

取 $\kappa'=\alpha^{p+1}\kappa$。
则
$$
a_{\kappa'}=\alpha^{p+1}a_\kappa,\qquad
\epsilon'=\alpha^{-(p+1)}\epsilon,\qquad
a_{\kappa'}\epsilon'=a_\kappa\epsilon.
\tag{27}
$$
全部 $e_2(Na_\kappa\epsilon)$ 因子准确相同。
$\widetilde H$、相容的 $\widetilde H_1$ 及原点规范常数不变，
且 $(\widetilde Z'^2x')^{17}=(\widetilde Z^2x)^{17}$；
故 $g^\sharp(t)$、真实 $g_\kappa(t)$ 和 $A_0^\sharp(t)$ 均相同。
这里的相同指 (20)、(27) 的实际坐标运输，不是把行或列免费改成新来源。

同时 $\bar K_2'=\bar\alpha\bar K_2$，故 forcing 的变化为
$$
\mathcal R'-\mathcal R=\frac{34\eta}{6x}(X-Y).
\tag{28}
$$
R388 的真实保阶式给
$$
X=O(z^{7p-1}),\qquad Y=O(z^{6p-2}).
$$
除以 $x$ 后分别从 $w^{7s-1}$、$w^p$ 起。因此
$$
\boxed{\mathcal R'=\mathcal R\pmod{t^p}.}
\tag{29}
$$
整个 R390 的 $p-1$ 维 Pascal 向量和实际低轴不变，
尽管全局 (6) 的标量改变了。

完整 Mellin 也相容：原正整数插值逐项给
$J_{\kappa'}^{\,b'}=\alpha^{-6}J_\kappa^{\,b}$，
再由同一个完整 Newton 收敛展开得到全权等式。
因此完整中央零及原第二 Bockstein 条件保持。
这不是只从有限 $\Gamma$ 推断全中央。

## 7. 精确可用范围

本文给出可计算的原标量 (16)、全部 Gaussian/整提升相容性，
以及它在真实同构下的必要补偿 (24)。
它是全局高 Frobenius 尾对 Hodge 尺度的协变量；
(26)、(29) 说明不能把它单独当作原 $C_2$ 或完整中央的非零证书。

后续可以在固定原规范中继续使用 (16)；
一旦与中央或第二障碍比较，仍须保 R390/R392 的完整
“基准项加 forcing 转置”以及同一个 $P_2,\lambda_2$。
本文没有增加任何已知中央零的来源，也没有改变固定曲线和无穷素数的完成标准。

## 依赖与同步

- [R363](R363-original-first-frobenius-quotient-and-second-rational-connection.md)：真实第一整商、$\lambda_p$ 及完整 Cartier 链。
- [R371](R371-original-frame-defect-cartier-logarithm-and-weighted-exact-term.md)：二挠主部及 $c_p\mathscr R_p(x_T)=-x_T^{2p}$。
- [R385](R385-original-zero-resonance-and-strong-whole-theta-second-lift.md)：相容第一提升、零共振及完整 theta 强窗。
- [R388](R388-original-second-quotient-global-forcing-and-first-resonance.md)：原 $Q_3,K_2$、平坦整除、保阶提升和固定极界。
- [R390](R390-original-second-obstruction-adjoint-and-fixed-two-torsion-boundary.md)：实际整左核、Pascal 运输和完整转置。
- [R392](R392-original-third-precision-without-extra-poles-and-gauge-covariance.md)：完整第三精度与基准加修正的规范协变。

全篇为参数证明，不作目标素数扫描。
执行环境不可用期间按根规则使用小文本 GitHub API；API 同步不冒称 git pull。
