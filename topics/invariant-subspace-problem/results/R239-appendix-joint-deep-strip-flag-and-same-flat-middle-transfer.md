# R239 附录：深 jets 与单高块条带的联合源旗、同源 Schur 及中段运输

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：联合源旗的两费用比较、真正 $M$ 投影、联合图上的左 Schur 小偏离以及同一原平坦源/裸费运输均已证明。物理中段与源坐标的交叉范围逐项列明，不把它们互换。普通 ISP 与边界 $N=M$ 仍为 OPEN。

依赖：
[深源同一平坦源 Schur](R271-appendix-deep-source-jet-schur-elimination-with-original-flat-cost.md)、
[物理输出切分](R271-appendix-output-cut-schur-localization-and-larger-middle-band.md)、
[单高块 primitive 三角带的真正源图支付](R239-appendix-paid-single-high-block-source-graph-strip.md)。
本稿组合的是已经付清的原右链列；没有假定新的多高位交织。

## 1. 相同原窗口中的两组便宜右链

固定
$$
m\ge8,\quad d=2^m,\quad4d\le q\le e^{d^3/4},
\quad p=d/2,\quad K=2^r,\quad4\le K\le d/4.
$$
沿用前稿
$$
\Gamma:\mathscr R_q\overset{\sim}{\longrightarrow}\mathscr U_q,
\quad B_U=\Gamma^{-1},\quad
\mathscr U_q=\bigoplus_{t=0}^{d-2}H_{\ge t+1}\otimes K_{q-t},
$$
$$
\mu(r)^2=\langle\mathcal G\Gamma r,\Gamma r\rangle,
\quad \mathcal G\succeq I,\quad
M=B+LGL,\quad \chi^2=\alpha^2+\lambda_{\rm flat}^2.
\tag{1.1}
$$
物理首源头 $P$ 约化 $B,G$，共同逆度量如前稿；它的坐标像为
$$
\Delta=\bigoplus_{t=0}^{d-2}\mathbb Ce_{t+1}\otimes K_{q-t}.
$$

第一组是单高块条带
$$
\mathscr A=\bigoplus_{0\le i<K}\ \bigoplus_{i\le t\le p+i-2}
\mathbb Ce_{p+i}\otimes K_{q-t}.
$$
前稿在每个 $a\in\mathscr A$ 上给出同一原完整右旗中的链 $R_Aa$，其源 $s_A(a)=F_{\rm flag}R_Aa$ 满足
$$
\Gamma s_A(a)=a-Na,\qquad Na\in\Delta,\qquad
\|R_A\|\le\delta_A\le e^{-4d^4}.
\tag{1.2}
$$
$Na=b_{m-1}a_{\rm anc}(z_a)$。更精确地，$Na$ 仅支持在 $\Delta$ 的 $0\le t<K$ 部分。

第二组由 R271 深源稿给出。置
$$
h=5d/8,\qquad
\mathscr D=\bigoplus_{h\le t\le d-2}
H_{\ge t+1}\otimes K_{q-t}.
$$
该稿的原顺次右链列 $R_D=-C_{\rm dp}$ 满足
$$
F_{\rm flag}R_Dd_0=B_Ud_0,\qquad
\|R_D\|\le\varepsilon_d=e^{-d^4/20}.
\tag{1.3}
$$
这里 $d_0\in\mathscr D$，且 $R_D$ 使用原完整联合旗。它没有被认作裸最小链。

## 2. 去掉重复坐标后的联合图

为避免重复计算，定义
$$
\mathscr A_{\rm sh}
=\mathscr A\cap\{t<h\},\qquad
\mathscr D_\perp=\mathscr D\ominus(\mathscr D\cap\Delta),
$$
$$
\boxed{\mathscr Y=\mathscr A_{\rm sh}\oplus\mathscr D_\perp.}
\tag{2.1}
$$
这是真正物理坐标正交和，且 $\mathscr Y\perp\Delta$。$\mathscr A$ 的深部分已包含在 $\mathscr D$ 中，故无损于要支付的联合坐标。

对于 $y=(a,d_0)\in\mathscr Y$，定义
$$
R_Yy=R_Aa+R_Dd_0,\qquad s_Y(y)=F_{\rm flag}R_Yy,
\qquad Ny=Na.
$$
有
$$
\boxed{\Gamma s_Y(y)=y-Ny,\qquad Ny\in\Delta.}
\tag{2.2}
$$
两个右链的像不被假定正交；真正使用的是 Cauchy：
$$
\|R_Yy\|
\le\delta_A\|a\|+\varepsilon_d\|d_0\|
\le\delta\,\|y\|,
$$
$$
\boxed{
\delta=(\delta_A^2+\varepsilon_d^2)^{1/2}
\le\sqrt2\,e^{-d^4/20}<1.
}
\tag{2.3}
$$
特别 $\delta^2\le e^{-8d^4}+e^{-d^4/10}$。因为 $Ny\perp y$，
$$
\|\Gamma s_Y(y)\|^2=\|y\|^2+\|Ny\|^2.
\tag{2.4}
$$

## 3. 一次支付的真实联合源旗

定义
$$
\boxed{
\mathscr X_{\rm joint}
=\Gamma^{-1}(\Delta\oplus\mathscr Y)
=\Gamma^{-1}(\Delta+\mathscr A+\mathscr D).
}
\tag{3.1}
$$
右侧第二式只是相同闭坐标空间的另一种写法；和式中已有重叠被 (2.1) 除去。

任取 $r\in\mathscr X_{\rm joint}$，唯一
$$
y=P_{\mathscr Y}\Gamma r,\qquad r-s_Y(y)\in P\mathscr R_q.
$$
于是 $Qr=Qs_Y(y)$，$\|y\|\le\mu(r)$。$Q$ 约化完整右度量，所以
$$
\boxed{\lambda(Qr)\le\lambda(s_Y(y))
\le\delta\|y\|\le\delta\mu(r).}
\tag{3.2}
$$
按物理源头分裂同一个完整 $Lr$，得到
$$
\mu(r)^2
\le\alpha_0(r)\lambda_{{\rm flat},0}(r)
+\delta\mu(r)\lambda_{{\rm flat},1}(r).
$$
与前稿相同的准确三变量最小化给
$$
\boxed{
\mu(r)^2\le c_\delta\chi(r)^2,\qquad
c_\delta=(2-\delta^2)^{-1}<1,
\quad r\in\mathscr X_{\rm joint}.
}
\tag{3.3}
$$
常数中的两项都已保留；没有把两组非正交右链作错误的正交相加。

因此可以在同一个 $M$ 度量中一次投到 $\mathscr X_{\rm joint}$。设
$$
r_X=P_{\mathscr X_{\rm joint}}^Mr,\qquad \widehat r=r-r_X.
$$
则
$$
\chi(r)^2=\chi(r_X)^2+\chi(\widehat r)^2,\qquad
\mu(r_X)\le\sqrt{c_\delta}\chi(r).
\tag{3.4}
$$
如果原 $E_q^\dagger r_m\to w$ 且 $\chi(r_m)\to0$，则
$E_q^\dagger\widehat r_m\to w$、$\chi(\widehat r_m)\to0$。

准确的余条件是
$$
\boxed{
P_{\Delta\oplus\mathscr Y}\Gamma^{-*}M\widehat r=0.
}
\tag{3.5}
$$
它不是 $P_{\Delta\oplus\mathscr Y}\Gamma\widehat r=0$。本节支付整个联合图中的修正，不声称原残余在这些坐标上无支撑。

## 4. 另一种合法缩减：沿联合便宜图作完整左 Schur

本节提供与 §3 不同、但仍保同一原源的缩减。它不同时要求 §3 的 $M$ 正交条件保持。

记 $\mathscr W=\mathscr U_q\ominus\mathscr Y$。因为 $N:\mathscr Y\to\Delta\subset\mathscr W$，定义三角坐标同构
$$
\mathcal T:\mathscr Y\oplus\mathscr W\to\mathscr U_q,
\qquad
\mathcal T(y,b)=y+b-Ny.
\tag{4.1}
$$
它的逆准确为
$$
y=P_{\mathscr Y}a,\qquad
b=P_{\mathscr W}a+Ny\quad(a\in\mathscr U_q).
\tag{4.2}
$$
因此保持 $b$ 固定并不等于保持原物理 $\mathscr W$ 坐标固定；(4.2) 的低锚必须保留。

在这些坐标中写完整左 Gram
$$
\widetilde{\mathcal G}
=\mathcal T^*\mathcal G\mathcal T
=\begin{pmatrix}H&K\\K^*&J\end{pmatrix}.
\tag{4.3}
$$
这里的 $J$ 只是本节矩阵块，不是原 $J_q$。由 (2.4) 及 $\mathcal G\succeq I$，
$$
\boxed{H=s_Y^*Ls_Y\succeq I.}
\tag{4.4}
$$
取原同一个 $r$，令 $\Gamma r=\mathcal T(y,b)$，并定义
$$
y_0=-H^{-1}Kb,\qquad z=y-y_0,\qquad
\widehat{\mathcal G}=J-K^*H^{-1}K.
\tag{4.5}
$$
$y_0$ 是固定图补坐标 $b$ 后真正的最小联合图补全，通常非零。

因为 $s_Y=F_{\rm flag}R_Y$，同一个原
$c^\flat=F_{\rm flag}^*Lr$ 给
$$
\boxed{Hz=R_Y^*c^\flat.}
\tag{4.6}
$$
于是
$$
\boxed{
\mu(r)^2
=\langle\widehat{\mathcal G}b,b\rangle+\langle Hz,z\rangle,
\quad
0\le\langle Hz,z\rangle\le\delta^2\|c^\flat\|^2,
\quad
\|z\|\le\delta\|c^\flat\|.
}
\tag{4.7}
$$
这里仅用 $H^{-1/2}$ 的收缩；没有要求整个图变换 $\mathcal T$ 收缩，也没有宣称 $\widehat{\mathcal G}\succeq I$。

## 5. 原 cflat、裸最小者与合法源分裂

定义两个真正源
$$
r_{\rm cut}=B_U\mathcal T(y_0,b),\qquad
\delta r=s_Y(z),\qquad r=r_{\rm cut}+\delta r.
\tag{5.1}
$$
由完整左 Schur 正交，
$$
\langle E_q^\dagger r_{\rm cut},E_q^\dagger\delta r\rangle=0,
$$
$$
\boxed{
\mu(\delta r)\le\delta\lambda_{\rm flat}(r),\qquad
\lambda(\delta r),\alpha(\delta r)
\le\delta^2\lambda_{\rm flat}(r).
}
\tag{5.2}
$$
第二行因为 $R_Yz$ 是同一原完整旗中的可行右链，其范数不超过 $\delta\|z\|$。

可以把剩余对偶方程完全写成原同一个 $c^\flat$。在 $\mathscr W$ 上选取真正完整右最小链映射
$$
R_W=F_{\rm flag}^\dagger B_U|_{\mathscr W},
$$
它在固定参数下有界，不对其范数作温和假设。定义
$$
\widehat R=R_W-R_YH^{-1}K.
\tag{5.3}
$$
完整源等式给 $F_{\rm flag}\widehat Rb=r_{\rm cut}$。从 (4.3) 的两个块式消元得到
$$
\boxed{\widehat{\mathcal G}b=\widehat R^*c^\flat(r).}
\tag{5.4}
$$
所有回馈都保留在 (5.3) 中；右侧没有换成 $r_{\rm cut}$ 自己未经控制的平坦向量。

令 $a_b(r)$ 为真正裸最小链，$\widehat a_b=a_b(r_{\rm cut})$。该最小逆线性，故 (5.2) 给
$$
\boxed{
\|a_b(r)-\widehat a_b\|
\le\delta^2\lambda_{\rm flat}(r).
}
\tag{5.5}
$$
特别 $\alpha(r_{\rm cut})\le\alpha(r)+\delta^2\lambda_{\rm flat}(r)$。
没有声称 $\lambda_{\rm flat}(r_{\rm cut})$ 被原 $\lambda_{\rm flat}(r)$ 控制；同源对偶信息准确是 (5.4)。

## 6. 物理中段重建可合法运输，但不产生源支撑结论

使用 R271 物理输出切分，令
$$
r_*=3d/8,\qquad
\mathscr P_{\rm mid}
=\mathbb C^d\otimes
\bigoplus_{q-d+2\le n\le q-r_*}K_n.
$$
对任意真正左最小者 $v=E_q^\dagger r$，写其 primitive 中段为 $b_{\rm mid}(r)$、远低部分为 $u(r)$、非 primitive 部分为 $\nu(r)$。该文证明同一个算子 $\mathcal T_{\rm out}$ 满足
$$
\|u(r)-\mathcal T_{\rm out}b_{\rm mid}(r)\|
\le\varepsilon_d\|\nu(r)\|.
\tag{6.1}
$$
$\mathscr P_{\rm mid}$ 包含全部自由头，不能换成强制源坐标。

将 (6.1) 应用于 (5.1) 的合法差源 $\delta r$，并用 (5.2)，得到
$$
\boxed{
\|\mathcal T_{\rm out}
[b_{\rm mid}(r)-b_{\rm mid}(r_{\rm cut})]\|
\le(1+\varepsilon_d)\delta\lambda_{\rm flat}(r).
}
\tag{6.2}
$$
原因是 $u,\nu,b_{\rm mid}$ 都来自同一个线性最小逆，且各正交部分范数不超过 $\mu(\delta r)$。这一步没有乘可能巨大的 $\|\mathcal T_{\rm out}\|$。

此外
$$
\|E_q^\dagger r-E_q^\dagger r_{\rm cut}\|
\le\delta\lambda_{\rm flat}(r).
\tag{6.3}
$$
因此对实际 $v_m\to w$、原 $\lambda_{\rm flat}(r_m)\to0$ 的序列，
$r_{\rm cut}$ 的最小左前驱仍趋向同一 $w$，原中段重建也由 (6.2) 保持。剩余裸费与对偶应读作 (5.4)–(5.5)，不另造平坦源收缩。

## 7. 与中间带相交后的准确坐标清单

本节只作坐标集合核对，不能取代 (3.5) 或 (4.5) 的真实图条件。

取最大 $K=d/4$。在强制坐标中记头为 $j$、深度为 $t$，所以
$$
0\le t\le d-2,\qquad t+1\le j\le d-1.
$$
联合旗已支付所有 $j=t+1$ 的最小头对角，以及：

- 所有 $t\ge5d/8$ 的强制坐标；
- $d/2\le j<3d/4$ 上满足 $j-d/2\le t\le j-2$ 的单高块条带。

物理中段对应 $t\ge3d/8$。因为 $j-d/2<d/4<3d/8$，在该中段内，单高块条带的上角限制自动满足。因此，在把全部已支付**源方向**除去的集合账本中，中段内尚未直接支付的强制坐标恰为
$$
\boxed{
3d/8\le t<5d/8,\qquad
t+2\le j\le d-1,\qquad
j<d/2\ \text{或}\ j\ge3d/4.
}
\tag{7.1}
$$
第一部分是 $t+2\le j<d/2$ 的小楔；第二部分是 $j\ge3d/4$ 的高四分之一。

但完整物理中段还含全部自由头 $j\le t$。而真正 $M$ 图残余满足 (3.5)，左 Schur 残余满足 (4.5)–(5.4)，两者都允许已支付坐标上的非零回馈。因此 (7.1) 不是说原或修正后的源只支持这些格子，更不是把自由中段消去。

可选渐近版也准确兼容。对固定
$$
1/4<\rho<1-(128/770)^{1/3},\qquad
(128/770)^{1/3}<\theta<1,
$$
充分大 $m$ 时，分别使用物理输出顶带 $\lfloor\rho d\rfloor$ 与深源阈值 $\lceil\theta d\rceil$，(2.3) 换成各已付指数误差的平方和，全部证明不变。集合账本将 (7.1) 的深度范围换为
$\lfloor\rho d\rfloor\le t<\lceil\theta d\rceil$。
这仍保留所有自由头和全部 Schur 回馈。

本稿新增了可一次 $M$ 支付的联合旗，以及联合图上同一原平坦源、裸费和物理中段重建的合法运输。尚未支付的高四分之一、多高位主耦合和中段自由头反馈继续保留为研究对象。
