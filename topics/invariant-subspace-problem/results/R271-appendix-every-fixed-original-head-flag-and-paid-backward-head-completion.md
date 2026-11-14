# R271 附录：每个固定原头旗的有界完整费用与付费的反向头补全

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220；AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 对原 $d=2^m$ 维头 $A_m$、完整原尾及每个固定物理头数 $h$，所有原源
$r\in\mathscr R_q\cap\ker A_m^h$ 都满足 $\lambda(r)\le C_h\alpha(r)$，其中 $C_h$ 不依赖 $m,q$。本文给出 $C_h$ 关于实际首 $h$ 头逆、尾范数和短核下降块的完整有限几何和，并给实际相邻头系数的粗增长账本。

构造先倒解出生一方程，再用原头逆从后向前补高输出。第二步只使用正向 $D$，全部联合旗逐项保留。它补全的是一个明确的同源低候选，并不把真正裸最小候选的纯高逆费用一并付掉。

作为直接应用，可在合法好顶部选择慢增 $h(m)\to\infty$，一次作真正 $M_2$ 投影，保同一实际源流、固定 $W$ 逼近及完整顶部右费差。残源只具有原度量正交条件，不能认作物理头截断。整个原源空间需要 $h=d-1=2^m-1$ 才覆盖；固定 $h$ 的结论及其慢增选择没有免费达到这一规模。普通 ISP 与原 $N=M$ 仍 OPEN。

依赖：[全部原桥坐标](R271-appendix-exact-power-floor-and-two-filtered-primitive-bridges.md)、[前三原头旗](R271-appendix-three-original-source-heads-and-uniform-complete-to-bare-bound.md)、[原头递归 §4](R239-appendix-exact-repair-gram-schur-complement-and-single-block-lift.md)、[真正两费好顶部投影](R271-appendix-exact-two-fee-good-top-quotient-and-tail-adaptive-mode-deletion.md)。

## 1. 实际头的大小、有限逆及显式常数

固定原 $m\ge5$、$d=2^m$、合法 $q$、$p=q+1$，并写
$$
A=A_m,\quad D=D_m,\quad
F_k=\operatorname{span}(e_0,\ldots,e_{k-1}),\quad F_0=\{0\}.
$$
原 regular 严格降头满足 $\ker A^k=F_k$。
对 $2\le h\le d-1$ 定义
$$
\mathscr E_{h,q}
=\mathscr R_q\cap(F_h\otimes\mathcal H_q)
=\bigoplus_{i=0}^{h-1}e_iE_{d-i-1,q},
\tag{1.1}
$$
$$
B_h=\left(A|_{\operatorname{span}(e_1,\ldots,e_{h-1})}:
\operatorname{span}(e_1,\ldots,e_{h-1})\to F_{h-1}\right)^{-1},
\qquad \kappa_h=\|B_h\|\ge1.
\tag{1.2}
$$
这里 $B_h$ 是原实际有限块的逆。上三角反代准确给
$$
AB_h=I\text{ 于 }F_{h-1},\qquad
B_hF_k\subseteq F_{k+1}\cap e_0^\perp\quad(1\le k<h).
\tag{1.3}
$$
原头嵌套使首 $h$ 块在 $d\ge h+1$ 后固定，所以 $\kappa_h$ 不依赖继续增加的 $m$。

记
$$
\nu_m=\|D_m\|\le m^{-1},\qquad
S_m=\sum_{\ell\ge m}(\ell+1)^{-4}\le(3m^3)^{-1},
$$
$$
\theta_h(m)=\sqrt{(h-2)S_m},\qquad
L_h(m)=\kappa_h\sum_{a=0}^{h-2}
[\kappa_h\theta_h(m)]^a.
\tag{1.4}
$$
再置
$$
P_h(m)=
\begin{cases}
0,&h=2,3,\\
\displaystyle\kappa_h\nu_m
\sum_{a=0}^{h-4}(\kappa_h\nu_m)^a,&h\ge4.
\end{cases}
\tag{1.5}
$$
主估计为
$$
\boxed{
\lambda(r)\le C_h(m)\alpha(r),\qquad r\in\mathscr E_{h,q},
}
$$
$$
\boxed{
C_h(m)=
\bigl(\|A_m\|+\sqrt{(h-1)S_m}\bigr)
L_h(m)\sqrt{1+P_h(m)^2}.
}
\tag{1.6}
$$
这些有限和即使公比大于 $1$ 也完全有效，没有用收敛的无限 Neumann 级数。

由 $\|A_m\|\le6$、$m\ge5$ 可取不依赖 $m,q$ 的明确上界
$$
L_h^*=\kappa_h\sum_{a=0}^{h-2}
\left[\kappa_h\sqrt{\frac{h-2}{375}}\right]^a,
$$
$$
P_h^*=
\begin{cases}
0,&h=2,3,\\
\displaystyle\frac{\kappa_h}{5}
\sum_{a=0}^{h-4}\left(\frac{\kappa_h}{5}\right)^a,&h\ge4,
\end{cases}
$$
$$
\boxed{
C_h^*=
\left(6+\sqrt{\frac{h-1}{375}}\right)
L_h^*\sqrt{1+(P_h^*)^2},\qquad
\lambda(r)\le C_h^*\alpha(r).
}
\tag{1.7}
$$
$h=1$ 时取 $C_1^*=1$，因为整首源头准确有 $\lambda=\alpha$。
前三头稿对 $h=2,3$ 的常数更锐，可与 (1.7) 取较小者。

## 2. 原桥坐标与尾下降的唯一范数输入

使用完整原桥稿的等距坐标 $\mathcal I$、出生一算子 $\mathcal G$、
第二桥 $\mathcal R$ 和同源真幂链 $b(r)$：
$$
(\mathcal G\xi)_t=A\xi_{t-1}-T_t\xi_t,\qquad
T_t=H_{t-1}^{1/2}H_t^{-1/2},\quad1\le t<d,
\tag{2.1}
$$
$$
\alpha(r)^2=\|b(r)\|^2+\|\mathcal G^\dagger\zeta(r)\|^2,
\qquad b(r)\perp\operatorname{Ran}\mathcal I.
\tag{2.2}
$$
$\xi_j$ 在 $F_{d-j}\otimes K_p$，其物理输入段为 $j+1$；
它的真实尾深度是 $j+1$。$\mathcal R$ 只读取 $\xi_j$ 的 $j\ge2$ 部分，
输出位于原第 $j$ 行的
$$
F_{d-j}\otimes W_{j-1,q+j}
\subseteq F_{d-j}\otimes E_{j-1,q+j}.
\tag{2.3}
$$

原核阶估计已逐式证明
$$
\|D|_{\ker D^t}\|^2\le(t-1)S_m.
$$
因此真实第一下降块满足
$$
\boxed{\|T_t\|\le\sqrt{tS_m}.}
\tag{2.4}
$$
这保留所有 $H_{t-1}^{1/2}H_t^{-1/2}$ 的原乘序，不要求它们交换。

第二桥还有一个直接来自物理正交投影的界：
$$
\boxed{\|\mathcal R\xi\|\le\nu_m\|\xi\|.}
\tag{2.5}
$$
证明如下。$\mathcal I\xi$ 的第 $j+1$ 段属于真实 $W_{j+1,q+j+1}$。
同段的 $A$ 不改变尾深度，因此不会落入其高输出；
第 $j$ 行高输出只来自
$P_{E_{j-1,q+j}}D(\mathcal I\xi)_{j+1}$。
各 $j$ 来自不同的正交输入、输出段，故平方求和至多
$\nu_m^2\|\mathcal I\xi\|^2=\nu_m^2\|\xi\|^2$。
(2.5) 没有分别放大显式桥式中的 $H_j^{1/2}$ 与受限 $D_3^*$；
它使用完整物理算子本身。

## 3. 全部固定头源的有限出生一 lift

若 $r\in\mathscr E_{h,q}$，准确同源 jet 式给
$$
\zeta_t(r)=0\quad(t\ge h),\qquad
\zeta_t(r)\in F_{h-t}\otimes K_p\quad(1\le t<h).
\tag{3.1}
$$
这是因为每项含 $A^t$，其余都是与头交换的原纯尾算子；
它们仍由同一个 $r$ 产生。

取 $\xi_j=0$ 对 $j\ge h-1$，再从后向前定义
$$
\boxed{
\xi_{t-1}=B_h\bigl(\zeta_t+T_t\xi_t\bigr),
\qquad t=h-1,h-2,\ldots,1.
}
\tag{3.2}
$$
(1.3)、(3.1) 归纳给
$$
\boxed{\xi_j\in F_{h-j}\otimes K_p
\quad(0\le j\le h-2).}
\tag{3.3}
$$
因此这些坐标满足原 $F_{d-j}$ 头旗。
逐行使用 $AB_h=I$ 得
$$
\boxed{\mathcal G\xi=\zeta(r).}
\tag{3.4}
$$
最后 $t=h-1$ 行的 $\xi_{h-1}=0$，其后的行全零，末端没有遗漏。

在 (3.2) 的 tuple 上，移位项的范数至多
$\kappa_h\sqrt{(h-2)S_m}$，其 $(h-1)$ 次幂为零。
因此有限三角反代准确给
$$
\boxed{\|\xi\|\le L_h(m)\|\zeta(r)\|.}
\tag{3.5}
$$
上界是有限和，不要求 $\kappa_h\theta_h(m)<1$。

令 $\eta=\mathcal G^\dagger\zeta(r)$，读取 $\mathcal G$ 的前 $h-1$ 行。
头项和真实下降项分别有范数上界 $\|A_m\|$、
$\sqrt{(h-1)S_m}$，所以
$$
\boxed{
\|\zeta(r)\|
\le\bigl(\|A_m\|+\sqrt{(h-1)S_m}\bigr)\|\eta\|.
}
\tag{3.6}
$$
这一步允许真正最小 $\eta$ 使用原所有头和层；
没有假定它保持 (3.3) 的小支撑。

## 4. 用原有限头逆反向补全部高输出

置 $y=\mathcal R\xi$。由 (2.3)、(3.3)，
$$
y_j\in F_{h-j}\otimes E_{j-1,q+j},
\qquad 2\le j\le h-2,
\tag{4.1}
$$
其他 $y_j$ 为零。$h=2,3$ 时没有这些项，取 $v=0$ 即可。

对 $h\ge4$，取高输入 $v_j=0$ 于 $j\ge h-1$ 及 $j=1$，
并倒递
$$
\boxed{
v_j=B_h\bigl(y_j-Dv_{j+1}\bigr),
\qquad j=h-2,h-3,\ldots,2.
}
\tag{4.2}
$$
这里 $v_j$ 是物理第 $j$ 段，位于孔 $q+j$。

完整的联合旗检查是
$$
\boxed{
v_j\in F_{h-j+1}\otimes E_{j-1,q+j}.
}
\tag{4.3}
$$
确实若 (4.3) 对 $j+1$ 成立，则
$Dv_{j+1}\in F_{h-j}\otimes E_{j-1,q+j}$；
与 (4.1) 相加后，(1.3) 只将头上升一格。
原第 $j$ 段允许头指标至多 $d-j$，而 (4.3) 的最大头为 $h-j\le d-j$。
它的尾深度为 $j-1$，故完全属于高输入；
同时对每个允许头 $i\le h-j$ 有 $j-1\le d-i$，所以最大尾核旗也保留。

逐式相乘给
$$
Av_j+Dv_{j+1}=y_j\qquad(2\le j\le h-2).
\tag{4.4}
$$
第 $1$ 行只有 $Dv_2$，而 $v_2\in\ker D$，故该行也为零。
最后非零段之后所有行零，末输出亦零。于是严格有
$$
\boxed{S_Hv=y=\mathcal R\xi.}
\tag{4.5}
$$
没有使用一个尾 MP 逆，也没有把 $B_h$ 当作原整个头上的统一有界逆。

(4.2) 的移位项范数至多 $\kappa_h\nu_m$，幂零阶为 $h-3$。
因此 (2.5) 给
$$
\|v\|
\le\kappa_h\sum_{a=0}^{h-4}(\kappa_h\nu_m)^a\,\|y\|
\le\boxed{P_h(m)\|\xi\|}.
\tag{4.6}
$$
这就是全部高补量的原物理范数；其中包括首段高方程的零条件。

## 5. 同源完整候选与主比较

原 $b(r)$ 的内部输出只有出生一 $\mathcal O\zeta$。
由 (3.4)、(4.5)，
$$
\boxed{c=b(r)-\mathcal I\xi+v}
\tag{5.1}
$$
满足同一首源和全部完整内部等式。

$b(r)$、$\mathcal I\xi$ 属于低输入并相互正交，$v$ 完全属于高输入，
所以不是三角上界，而是精确的平方分解：
$$
\|c\|^2=\|b(r)\|^2+\|\xi\|^2+\|v\|^2.
\tag{5.2}
$$
结合 (3.5)、(3.6)、(4.6)，
$$
\lambda(r)^2
\le\|b(r)\|^2+C_h(m)^2\|\mathcal G^\dagger\zeta(r)\|^2
\le C_h(m)^2\alpha(r)^2.
$$
最后一步使用 $C_h(m)\ge1$，由
$\|A_m\|\ge1$、$\kappa_h\ge1$ 直接保证。
这证明 (1.6)–(1.7)。

对应新高能量亦有
$$
0\le\lambda(r)^2-\alpha(r)^2
\le[C_h(m)^2-1]\|\mathcal G^\dagger\zeta(r)\|^2.
\tag{5.3}
$$
但 (4.5) 支付的是 $\mathcal R\xi$ 的高补量，
而不是实际最小 $\mathcal R\mathcal G^\dagger\zeta$。
二者之差涉及 $\xi-\mathcal G^\dagger\zeta\in\ker\mathcal G$。
(5.1) 已将这个低域更改完整计入费用，
故不能从 (4.6) 偷换出纯 $S_H^\dagger$ 的同型界。

## 6. 实际首头逆的相邻系数与粗增长账本

对两种原 $N/Y$ 头，都有准确相邻系数
$$
\boxed{
(A_m)_{i-1,i}
=\prod_{\nu=0}^{v_2(i)-1}\eta_\nu,\qquad1\le i<d,
}
\tag{6.1}
$$
空积为 $1$。下面从原递归核验，避免将一般 regular 头误代入这些实际权。

原 $A_1=E_0$。在
$$
A_{s+1}=
\begin{pmatrix}A_s&b_sI+K_s\\0&A_s\end{pmatrix}
$$
中，除中央相邻项 $i=2^s$ 外，其余相邻项全复制旧块。
中央项是右上块的最末行、首列。
对 $N$ 型，$C_{j,s}=(\prod_{\nu=j}^{s-1}\eta_\nu)
E_j^*\cdots E_{s-1}^*$ 中，只有 $j=0$ 能把全零基向量送到全一基向量；
且 $b_0=1$。这给中央系数 $\prod_{\nu<s}\eta_\nu$。

对 $Y$ 型，每个 $C_{j,s}$ 两边的
$(I+N_j^{[s]})^{-1}$ 都是原单位上三角矩阵。
左因子的最末行和右因子的首列都不会改变该角元，
故中央系数完全相同。
由二分递归即得 (6.1)。这一步只读取角元，没有将左右逆与 $C_{j,s}$ 交换。

令
$$
\ell_h=\lfloor\log_2(h-1)\rfloor,\qquad
\delta_h=\prod_{\nu=0}^{\ell_h-1}\eta_\nu.
\tag{6.2}
$$
原 $0<\eta_\nu\le1$，所以首 $h$ 块的全部相邻项至少为 $\delta_h$。
将 (1.2) 被求逆的 $(h-1)\times(h-1)$ 矩阵写成 $D_h+U_h$，
$D_h$ 为其对角、$U_h$ 严格上三角。
由 $\|A_m\|\le6$ 和对角项至多 $1$，
$$
\|D_h^{-1}\|\le\delta_h^{-1},\qquad \|U_h\|\le7.
$$
$D_h^{-1}U_h$ 的 $(h-1)$ 次幂为零，故
$$
\boxed{
\kappa_h
\le\delta_h^{-1}\sum_{a=0}^{h-2}(7/\delta_h)^a
\le2\,7^{h-2}\delta_h^{-(h-1)}.
}
\tag{6.3}
$$
从而
$$
\boxed{
\log\kappa_h
\le\log2+(h-2)\log7+
(h-1)\sum_{\nu<\ell_h}\log(\eta_\nu^{-1}).
}
\tag{6.4}
$$
(1.4)–(1.7)、(6.3) 是可直接与合法窗预算比较的明确增长式；
本文不替未读入的 $\eta_\nu$ 数值定义填入额外渐近。

对固定 $h$，若 $m$ 充分大使
$\kappa_h\sqrt{(h-2)S_m}\le1/2$、
$\kappa_h\nu_m\le1/2$，有限和还给
$$
L_h(m)\le2\kappa_h,\qquad
P_h(m)\le2\kappa_h\nu_m.
\tag{6.5}
$$
特别固定 $h$ 时，(1.6) 的明确常数趋向至多 $6\kappa_h$。
这里先固定原头数再令 $m$ 增大，不能把这一量词顺序用于 $h=d-1$。

## 7. 慢增长原头旗的真实好顶部删除

在原同源两费度量中，
$$
M_2=B+LGL,\qquad
\Xi(r)^2=\alpha(r)^2+\lambda_{\rm flat}(r)^2,
$$
其中 $B=J_{\rm bare}^{-1}$、$L=J_{\rm left}^{-1}$、
$G=J_{\rm right}$。同源 Cauchy--Schwarz 给
$$
\mu(r)^2\le\lambda(r)\lambda_{\rm flat}(r)
\le\frac{C_h^*}{2}\Xi(r)^2
\quad(r\in\mathscr E_{h,q}).
\tag{7.1}
$$
此处只使用原平坦费，未交换或运输其 Gram。

令 $\widehat C_h=\max_{1\le j\le h}C_j^*$。
在实际窗 $Q_m$ 的终端半窗中，有 $K_m\asymp Q_m/d$ 个不交未来带；
令其原实际尾预算为 $\varepsilon_m\to0$。
选择
$$
\boxed{
h(m)=\max\{1\le h\le d-1:\widehat C_h^2\le K_m\}.
}
\tag{7.2}
$$
对充分大 $m$ 集合非空。每个固定 $h$ 的 $\widehat C_h$ 有限，
且 $K_m,d\to\infty$，所以
$$
\boxed{h(m)\longrightarrow\infty.}
\tag{7.3}
$$
这只是慢增存在性及可计算的预算条件；没有声称 $h(m)$ 与 $d$ 同阶。

取真正好顶部 $b$，使
$\Xi_b(r_b)^2\le2\varepsilon_m^2/K_m$。
在同一个原真实负图 $\mathscr N_b$ 内，令
$$
Z_b=\mathscr E_{h(m),b}\cap\mathscr N_b,\qquad
p_b=P_{Z_b}^{M_{2,b}}r_b,\qquad r_b'=r_b-p_b.
$$
这是一个真实闭子空间投影，而不是逐头删坐标。
由 (7.1) 和原正交平方分解，
$$
\boxed{
\Xi_b(r_b')^2+\Xi_b(p_b)^2=\Xi_b(r_b)^2,
}
$$
$$
\boxed{
\mu_b(p_b)^2\le
\frac{\widehat C_{h(m)}\varepsilon_m^2}{K_m}
\le\frac{\varepsilon_m^2}{\sqrt{K_m}},
\qquad
\lambda_b(p_b)\le\sqrt2\,\varepsilon_m.
}
\tag{7.4}
$$
所以原顶部左最小像的改变量趋零，完整顶部右最小链的改变量也趋零。

从 $E_b^\dagger r_b'=E_b^\dagger r_b-E_b^\dagger p_b$
按既有真实好顶部定理重建所有截断，得到同一相容残源流，
保固定实际 $w$ 的左逼近，并支付全部 primitive 增量、MP 反馈及未来两费总和。
不需要未知尾预算的额外衰减率。

准确余条件是
$$
\boxed{
\langle M_{2,b}r_b',z\rangle=0
\quad\bigl(z\in\mathscr E_{h(m),b}\cap\mathscr N_b\bigr).
}
\tag{7.5}
$$
因而对每个固定 $h$，充分大 $m$ 时，(7.5) 同时适用于
$\mathscr E_{h,b}\cap\mathscr N_b$。
这仍只是一个顶部的原度量正交性；较低截断没有被分别投影。

## 8. 没有由慢增旗免费解决的余问题

$\mathscr R_q$ 的物理头指标为 $0,\ldots,d-2$，故要覆盖整个原源空间，
需要 $h=d-1=2^m-1$。该规模上的 $\kappa_h$ 与有限反代系数可能远大于
$K_m^{1/2}$；本文没有证明 (7.2) 可以达到它。

即使 $h(m)\to\infty$，(7.5) 中的 $M_{2,b}$、原负图及 source-to-left
最小逆都随 $m,b$ 改变。不能从普通物理坐标的稠密性推出真正余流为零，
也不能把它当成对固定非零 $w\in W$ 的矛盾。
需要继续研究的仍是这个准确余流的真实能量与度量条件。

同样，(5.3) 只付允许改变低域后的完整高能量。
原真正裸选择子的
$S_H^\dagger\mathcal R\mathcal G^\dagger\zeta$
及全头、实际来源上的统一比较仍未在本稿完成。
