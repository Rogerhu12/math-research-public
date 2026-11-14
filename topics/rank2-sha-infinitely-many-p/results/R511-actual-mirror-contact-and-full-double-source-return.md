# R511 — 同预算完整二倍来源、真实镜轴接触与 ξ 的进一步返回

日期：2026-11-14。**状态：已证明。** 原立方来源不仅允许 R505 的 $F^2H_1$ 修正，还允许完整 $FH_2$，其中 $H_2\in H^0(X,\mathcal O_X(2C))$。在同一个原三块目标中，这个更大的来源准确通过一个指定普通接触矩阵因子化；其轴是原 $g^2/\widetilde\psi$，长度 $S=s-r$，并非可任取的新 theta 来源。

这一镜轴矩阵的实际 $F^2$ Bockstein 代表为 $8e^2t^hu\xi$，经真实目标单射乘 $3/4$ 后，恰是 R502 的整个 $\xi$ 向量。本文给出全 $2C$ 的对偶、与 R505 一倍接触余核之间的准确精确序列、以及新的同预算吸收判据。只要该实际镜轴类为零，即可用一个原 $FH_2$ 修正吸收全部 $\xi$。没有由维数推满射，也没有将普通 $C$ 上的消失当作镜轴条件。

## 1. 同一实际范围与两个截断长度

保 R505/R507 的全部原对象：
$$
p=6s-1>83,\qquad f_D<p,\qquad
d^{C_D}\bar P=t^rF^3Q\in d^{C_D}\overline{\mathcal W}_D,
$$
$$
F(0,1)=0,\qquad F_Y(0,1)Q(0,1)\ne0,
\qquad
1\le\ell\le r<h<s,\qquad
k=2h+r-s,\quad 0\le k<\ell.
\tag{1}
$$
$X,C,P=(0,1)$ 仍为 R495 的固定十九次吹起面、同一严格变换及未动的光滑点。记
$$
\kappa=C^2,\qquad\chi=-K_XC\ge2\deg_YF,
\qquad
S=s-r=2h-k,\qquad q=S-h=h-k.
\tag{2}
$$
原整及约化目标为
$$
\Gamma_\ell=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^3,w^\ell\epsilon^2),
\qquad
\bar\Gamma_\ell=k[w,\epsilon]/(w^s,\epsilon^3,w^\ell\epsilon^2).
$$
所有 $t/w$、原 $a=p\kappa_{\rm Gauss}\in\mathcal O^\times$、$P_{134}/U_0$ 均不改。

按 R491 取真实整提升 $\widetilde F,\widetilde Q$，使
$$
P^{\rm fact}=d^{-C_D}t^r\widetilde F^3\widetilde Q\in\mathcal W_D.
$$
$\widetilde\psi$ 是该同一因子的整正规分支，$\psi$ 为其约化。写 R502 的实际
$$
\eta=\log(g/\widetilde\psi)=t^hu+p\xi\pmod{p^2},
\qquad \eta_0=t^hu\pmod p,
$$
$$
e=(\mathcal EF)|_C,\quad
f_2=(\mathcal E^2F)|_C,\quad
q_C=(d^{-C_D}Q)|_C,\qquad \mathcal E=Y\partial_Y.
\tag{3}
$$
$e,q_C,u$ 在 $P$ 都是单位。本篇不需要先把 $\xi(0)$ 归零；若采用 R507 的合法归一，所有公式仍相同。

## 2. 完整二倍整来源与指定镜轴矩阵

令 $\mathcal H_m$ 是同一整角曲面上 $\mathcal O(m\widetilde C)$ 的显示截面格，$m=1,2,3$。R491/R498 的逐系数 Hensel 角整除及次数帽给有限自由格，且
$$
\overline{\mathcal H}_m=H^0(X,\mathcal O_X(mC)).
\tag{4}
$$
每条吹起链的全部中间重数均保留。乘法给
$\widetilde F\mathcal H_2\subset\mathcal H_3$，而 R495 已付
$d^{-C_D}t^r\widetilde Q\mathcal H_3\subset\mathcal W_D$。因此
$$
\boxed{
\iota_2:\mathcal H_2\longrightarrow\mathcal W_D,\qquad
H\longmapsto d^{-C_D}t^r\widetilde Q\,\widetilde F H
}
\tag{5}
$$
是同预算的实际来源包含，不增加 $D$ 或任一原次数帽。它是 $p$ 饱和的来源包含：约化多项式域中的非零因子 $t^rQF$ 使乘法单射，且 (4) 的约化核为 $p\mathcal H_2$。这里不声称评价像饱和。

现在定义实际整单位轴
$$
g_{\rm mir}(t)=\frac{g(t)^2}{\widetilde\psi(t)}
=\widetilde\psi(t)\exp(2\eta(t))
$$
及有限自由矩阵
$$
\boxed{
E^{\rm mir}_S:\mathcal H_2\longrightarrow\mathcal O[t]/t^S,\qquad
H\longmapsto H(t,g_{\rm mir}(t))\pmod{t^S}.
}
\tag{6}
$$
$S<s$，故只读取原已付的普通整窗口。镜轴由同一个实际 $g$ 和同一个因子提升决定；它不是新算术对象，也不被赋中央零。

模 $p$ 后，$2h\ge S$ 给
$$
\bar g_{\rm mir}=\psi(1+2\eta_0)\pmod{t^S}.
\tag{7}
$$
不能把 (7) 的 $\eta_0$ 改成任意给定接触阶的多项式。

## 3. 在完整原目标中的严格因子化

先取原高像 $t^r\bar\Gamma_\ell$。因 $r\ge\ell$，它在除去这个已知像因子后准确对应
$$
\mathcal A=k[[t]][\epsilon]/(t^S,\epsilon^2).
\tag{8}
$$
这只是在原目标中取已知像；原第三块并未从整个问题删去。

在 (8) 上，原完整正规坐标的约化满足
$$
\zeta=\eta_0+a\epsilon,\qquad
\eta_0^2=0,\qquad
\boxed{\zeta^2=2\eta_0\zeta,\quad\zeta^3=0.}
\tag{9}
$$
它与 raw $\bar\Gamma_\ell$ 中可能非零的 $\zeta^3$ 不同。准确说，是乘 $t^r$ 后
$t^r(\zeta^2-2\eta_0\zeta)=t^r\zeta^3=0$；分别由 $r+2h\ge s$ 和 $r\ge\ell$ 支付。

在实际正规展开中，$F/\zeta$ 为整单位。令
$$
U_{\rm phys}
=\left.\frac{d^{-C_D}Q\,F}{\zeta}\right|_{Y=Y_{\rm phys}}\pmod p.
$$
这是完整单位；包括 $Q$ 和 $F/\zeta$ 的全部可见正规项。定义
$$
\boxed{
T_2:k[t]/t^S\longrightarrow\bar\Gamma_\ell,\qquad
f\longmapsto t^rU_{\rm phys}\,\zeta f.
}
\tag{10}
$$

**定理 1。** $T_2$ 是原完整目标中的单射，而且
$$
\boxed{\bar J\,\bar\iota_2=T_2\,\bar E^{\rm mir}_S.}
\tag{11}
$$

**证明。** 在 (8) 中，乘 $\zeta=\eta_0+a\epsilon$ 从 $k[t]/t^S$ 到 $\mathcal A$ 是单射，因为其 $\epsilon$ 系数为单位 $a$ 乘输入。再乘完整单位及取像嵌回原目标仍单射，证明第一部分。

将任意实际 $H$ 在 $\zeta$ 中展开为 $H_0+\zeta H_1+\zeta^2H_2+\cdots$。由 (9)，
$$
\zeta H(\zeta)
=\zeta(H_0+2\eta_0H_1)
=\zeta H(2\eta_0)
\quad\text{于 }\mathcal A.
$$
$H(2\eta_0)$ 正是 (7) 的实际镜轴评价。乘回原 $t^rU_{\rm phys}$ 即为 (11)，包含原所有三块。$\square$

因此有确定的余核映射
$$
\boxed{
\bar T_2:\operatorname{coker}\bar E^{\rm mir}_S
\longrightarrow\operatorname{coker}\bar J.
}
\tag{12}
$$
(10) 的单射不意味着 (12) 单射；其他原来源列仍可能吸收它的像。(11) 只在模 $p$ 声称交换。以下的除 $p$ 公式由真实展开另证，不以未付的整交换图作 Bockstein 自然性。

## 4. 镜轴的真实 F² Bockstein及完整 ξ 向量

因为 $F(\bar g_{\rm mir})$ 有阶 $h$，$F^2\in\ker\bar E^{\rm mir}_S$。定义实际代表及类
$$
\mu_{\rm mir}
=\overline{E^{\rm mir}_S(\widetilde F^2)/p},
\qquad
\beta_{\rm mir}(F^2)
=[\mu_{\rm mir}]\in\operatorname{coker}\bar E^{\rm mir}_S.
\tag{13}
$$

**定理 2。** 在同一个 $k[t]/t^S$ 中，
$$
\boxed{\mu_{\rm mir}=8e^2\eta_0\xi.}
\tag{14}
$$
R502 的整个实际 $\xi$ 向量满足
$$
\boxed{
\beta_\xi
=6a\epsilon\,t^{r+h}q_Ce^3u\xi
=\frac34\,T_2(\mu_{\rm mir}),
\qquad
[\beta_\xi]=\frac34\,\bar T_2\bigl(\beta_{\rm mir}(F^2)\bigr).
}
\tag{15}
$$

**证明。** 在镜轴上 $Y=\widetilde\psi e^{2\eta}$，所以
$$
\widetilde F(Y)=2e\eta+2f_2\eta^2+\cdots.
$$
其平方的首项是 $4e^2\eta^2$。模 $(p^2,t^S)$，所有普通 $\eta_0^2$ 项因 $2h\ge S$ 消失，唯一除 $p$ 后可见的项为
$8e^2\eta_0\xi$。三次及更高项即使含一个 $p$，仍含 $\eta_0^2$，因此在此普通截断消失。这证明 (14)。

(14) 至少有 $t^h$ 因子。于是 (10) 中的普通分量再乘 $\eta_0$ 后为零，$U_{\rm phys}$ 中额外的 $\zeta$ 项也因 (9) 为零；只剩
$$
T_2(\mu_{\rm mir})
=8a\epsilon\,t^r q_Ce^3\eta_0\xi.
$$
乘 $3/4$ 就是 (15)。这比较的是全部向量，不仅是一个首系数。$\square$

还须保因子提升变化。若 $\widetilde F$ 改为同一格中的
$\widetilde F+pH$，镜轴本身也随正规分支改变，不能将 (6) 冒称完全未变。准确的一阶根变化给
$\xi_{\rm new}=\xi+H|_C/e$，所以
$$
\mu_{{\rm mir,new}}-\mu_{\rm mir}
=8e\eta_0H|_C
=\bar E^{\rm mir}_S(4FH).
\tag{16}
$$
其中 $FH\in\overline{\mathcal H}_2$ 是实际来源。约化矩阵不变，(13) 的特殊类因此不变。这个系数四同时保留了因子平方和依赖于因子的镜轴两份变化；只改源向量而固定镜轴会漏掉一半。

## 5. 全 2C 镜 jet 的准确几何对偶

R495 的 $H^1(X,\mathcal O_X(mC))=0$ 给
$$
H^0(X,\mathcal O_X(2C))
\twoheadrightarrow H^0(2C,\mathcal O_{2C}(2C)),
$$
核为 $kF^2$，且
$H^1(2C,\mathcal O_{2C}(2C))=0$。
(7) 在 $2C$ 的完成局部环 $k[[t]][\zeta]/\zeta^2$ 中定义准确理想
$$
\boxed{\mathscr I_{\rm mir}=(t^S,\zeta-2\eta_0).}
\tag{17}
$$
因 $\eta_0^2\in(t^S)$，其商准确为 $k[t]/t^S$，长度 $S$；在 $P$ 外理想为整个结构层。

因此显示镜轴矩阵的全部余核对偶准确为
$$
\boxed{
\mathscr D_{\rm mir}
=
H^0\!\left(2C,\operatorname{Hom}
(\mathscr I_{\rm mir},K_X|_{2C})\right)
=(\operatorname{coker}\bar E^{\rm mir}_S)^*.
}
\tag{18}
$$
这里使用的是 $2C$ 的完整 Gorenstein 对偶；没有用普通 $C$ 上的某个 $H^1$ 取代 (17)。

在与 $\mathcal O_{2C}(2C)$ 互为对偶的同一局部框中写
$$
\Psi=(A_1+B_1\zeta)\frac{dt\wedge d\zeta}{\zeta^2}.
$$
(17) 的正则条件准确为
$$
\boxed{
A_1,B_1\in t^{-S}k[[t]],\qquad
A_1-2\eta_0B_1\in k[[t]].
}
\tag{19}
$$
另一条件 $\eta_0A_1$ 正则由 (19) 自动成立，因为
$\eta_0^2B_1$ 正则。特别 $\operatorname{pole}A_1\le q$。
在镜轴目标 $f\in k[t]/t^S$ 上，这条行的读法是
$$
\boxed{\lambda_\Psi(f)=\operatorname{Res}_P B_1 f\,dt.}
\tag{20}
$$
因为对 $H_0+\zeta H_1$ 的留数为
$\operatorname{Res}(A_1H_1+B_1H_0)dt$，而 (19) 使其等于
$\operatorname{Res}B_1(H_0+2\eta_0H_1)dt$。

这些系数必须满足 (18) 的全部全局正则条件，不能独立任取。作为层，还具有准确短正合列
$$
\boxed{
0\to (K_X-C)|_C(hP)
\to\operatorname{Hom}(\mathscr I_{\rm mir},K_X|_{2C})
\to K_X|_C(qP)\to0.
}
\tag{21}
$$
末箭头为限制；其局部满射由给定 $A_1$ 后取
$B_1=A_1/(2\eta_0)$ 核定。其核 $A_1=0$ 恰要求 $B_1$ 的极阶不超过 $h$，得到首项。可在完成局部环检查后由忠实平坦性下降。全局截面不必保持末端满射，其连接同态不能省略。

## 6. 原真行的精确镜轴限制

取 R498 的一条原真行
$$
\Phi=(A+B\zeta+C_2\zeta^2)\frac{dt\wedge d\zeta}{\zeta^3},
\qquad A-2\eta_0B\text{ 正则},
$$
保所有原低行高尾及其余原列测试。经 (12) 的对偶，它在 (18) 中对应
$$
\boxed{
A_1=eA,\qquad
B_1=eB+\tfrac12 f_2A.
}
\tag{22}
$$

**证明。** 在同一个 $3C$ 展开中
$F=e\zeta+\tfrac12 f_2\zeta^2$。将 $FH$ 代入原三层留数，得到
$$
\operatorname{Res}\bigl(
eA\,H_1+(eB+\tfrac12f_2A)H_0
\bigr)dt.
$$
这正是 (22)。全部 $FH$ 已由 (5) 支付，所以它杀整个镜轴来源像；相应全局行来自 (18)。并且
$$
A_1-2\eta_0B_1
=e(A-2\eta_0B)-\eta_0 f_2A
$$
正则，因为 $\operatorname{pole}A\le q\le h$。$\square$

因此
$$
\frac34\,\lambda_\Psi(\mu_{\rm mir})
=6\operatorname{Res}e^2\eta_0B_1\xi\,dt
=3\operatorname{Res}Ae^3\xi\,dt,
\tag{23}
$$
与 R505/R507 原真行的读法完全一致。$f_2A$ 部分在这一次 $\xi$ 配对中因 $\eta_0A$ 正则消失；这不允许删除 R502 独立的活 $V_1$ carry。

(22) 只是原真行到镜轴对偶的映射。反向，一个任意 $\Psi\in\mathscr D_{\rm mir}$ 未必能提升为满足全部原列测试的三层真行；(12) 的余核核正反映了这个区别。

## 7. 与一倍接触的精确序列及额外可用修正

令 $N_C=\mathcal O_C(C)$。源端有由 R495 支付的正合列
$$
0\to H^0(X,\mathcal O_X(C))
\xrightarrow{\ F\ }H^0(X,\mathcal O_X(2C))
\to H^0(C,N_C^2)\to0.
\tag{24}
$$
目标端有
$$
0\to k[t]/t^q
\xrightarrow{\ T_1\ }k[t]/t^S
\to k[t]/t^h\to0,
\qquad
T_1(f)=2e\eta_0 f.
\tag{25}
$$
实际评价使 (24)、(25) 构成交换图：左箭头为 R505 的 $\bar E_q$，中间为 $\bar E^{\rm mir}_S$，右箭头为
$$
E_{h,C}^{(2)}:H^0(C,N_C^2)\longrightarrow N_C^2|_{hP}.
$$
因为 $F(\bar g_{\rm mir})=2e\eta_0\bmod t^S$，且镜轴与 $\psi$ 模 $t^h$ 相同，交换性逐项成立。

蛇引理给出完整准确段
$$
\begin{aligned}
0\to\ker\bar E_q
&\to\ker\bar E^{\rm mir}_S
\to H^0(C,N_C^2(-hP))
\xrightarrow{\ \partial_\eta\ }\operatorname{coker}\bar E_q\\
&\xrightarrow{\ \bar T_1\ }\operatorname{coker}\bar E^{\rm mir}_S
\to\operatorname{coker}E_{h,C}^{(2)}\to0 .
\end{aligned}
\tag{26}
$$
$\partial_\eta$ 是实际可计算的图同态：对 $v\in H^0(C,N_C^2(-hP))$，取 (24) 的一个真正提升 $H\in H^0(X,\mathcal O_X(2C))$，则
$$
\boxed{
\partial_\eta(v)=
\left[\frac{\bar E^{\rm mir}_S(H)}{2e\eta_0}\right]
\in\operatorname{coker}\bar E_q.
}
\tag{27}
$$
除法只在已知的 $t^h$ 像中进行，余长为 $q$；改变提升仅加
$\bar E_q$ 的实际像。没有免费补独立 normal 系数。

三个实际返回相容：
$$
\boxed{
T_2T_1=T\ \text{（R505 的同一目标嵌入）},\qquad
\mu_{\rm mir}=4T_1(\mu_F).
}
\tag{28}
$$
从而
$$
\boxed{
\beta_{\rm mir}(F^2)=0
\quad\Longleftrightarrow\quad
\beta_{\rm cont}(F)\in\operatorname{im}\partial_\eta.
}
\tag{29}
$$
这是超过仅允许 $F^2H_1$ 的准确修正判据：现在允许 (27) 的完整二倍来源。它并不声称已经证明每个实际候选的右侧成立。

一个可付的辅助范围是
$$
h<\kappa+\chi.
\tag{30}
$$
此时
$$
H^1(C,N_C^2(-hP))
=H^0(C,K_X|_C(-C)(hP))^*=0
$$
因为其对偶次数为 $h-\kappa-\chi<0。因此 (26) 最后一项为零，$\bar T_1$ 在余核上满射，并有
$$
\dim H^0(C,N_C^2(-hP))
=\frac{3\kappa+\chi}{2}-h.
\tag{31}
$$
这没有证明 $\partial_\eta$ 满射，也没有证明镜轴矩阵满射。尤其不能只看 $S$ 与 $\kappa+\chi$ 的维数比较，就把 (29) 置为真；(27) 依赖原实际镜轴。

例如，(21) 的两层次数分别为 $h-\kappa-\chi$ 与 $q-\chi$。两个都负时，整个镜轴矩阵确实满射；但对 $\xi$ 的自动吸收，R505 已有的较直接条件 $q<\chi$ 本身就足够。本篇不把这个重合范围重新包装为严格扩大了的统一界。新增的是 (26)–(29) 对更大真来源的准确可用条件。

## 8. 同预算吸收及完整 p² 缺陷边界

若 (13) 的类为零，取一个实际 $H\in\mathcal H_2$，满足
$$
\bar E^{\rm mir}_S(\bar H)=\mu_{\rm mir}.
$$
则
$$
\boxed{
R_\xi=-\frac34\,d^{-C_D}t^r\widetilde Q\,\widetilde F H
\in\mathcal W_D,\qquad
\bar J\bar R_\xi=-\beta_\xi.
}
\tag{32}
$$
$\mu_{\rm mir}$ 从 $t^h$ 起，故 (10) 的第一块在 (32) 中为零，第二块从 $r+h$ 起，第三块为零。因而首次提升中已选的低行修正不变；第三精度仍须保同一个真实 $R_\xi$ 的全部输出。

原完整 Bockstein 没有只剩 (13)。保 R502 的
$$
b_s=(t/w(t))^s,\qquad V_0=q_Ce^3,\qquad
V_1=\left.d^{-C_D}\bigl((\mathcal EQ)e^3+
\tfrac32Qe^2\mathcal E^2F\bigr)\right|_C .
$$
准确有
$$
\boxed{
[\beta_J(P^{\rm fact})]
=
\left[
\epsilon V_0b_st^{h+k}u^3+
3a\epsilon^2V_0b_st^ku^2+
\epsilon V_1b_st^{2h+k}u^4
\right]
+\frac34\,\bar T_2\bigl(\beta_{\rm mir}(F^2)\bigr).
}
\tag{33}
$$
这是整个原相对余核中的等式；$r>2k$ 时的活 $V_1$、全部低行高尾和 (1) 的原两次 carry 均在。非零镜轴类也不推出 (33) 非零，因为 (12) 可有核，且仍可与显示 carry 相消。

原 $M$ 继续通过
$$
M=c_*U_0m_{13}J,\qquad
K_2^{\rm red}(M)=\ker(\pi\beta_J),\qquad
G_2=C_2(J)/\overline H
$$
比较。R479 的两条十三行输出及 R481 的同一首次修正到第三精度仍须一起使用，不能从 (32) 单独读取全 $M$ 的结论。

## 9. 与 R507 完整共振的准确相接处

镜轴的整对数满足原身份
$$
\mathcal P\log g_{\rm mir}
=2\mathcal R-\mathcal P\log\widetilde\psi
-2a s\,\mathsf B w^s,
\qquad \mathsf B=\mathsf h^{-2}.
\tag{34}
$$
若仅作计算性的完整 Gaussian 运输，
$g_{\rm mir}e^{2a\epsilon}=Y_{\rm phys}^2/\widetilde\psi$，
则两份原 Gaussian 缺项准确相消。这是一条从原 $Y_{\rm phys}$ 推出的恒等式，未给镜轴新增算术身份或中央条件。

但 (6) 是长度 $S<s$ 的**普通**接触矩阵；在这个目标上，$\mathcal P$ 只有常量核，其他对角单位
$n(6n-1)$ 尚未到达 $n=s$。不能把 R507 完整 $\Gamma$ 上唯一的 $p$ Smith 因子直接搬到这个普通目标。也不能把 (11) 的约化交换图升级为模 $p^2$ 交换；其真实进位已经明确留在 (33)。

对原真行，(22)、(23) 与 R507 的实际 forcing 转置直接相容：镜轴的 $\xi$ 配对仍只读有效极帽 $q=h-k$，不会因镜轴总长度变为 $S$ 就自动读取首共振。接续所需的是同一真行上 (33) 其余 carry 与 (34) 的实际来源关系，或直接支付 (27) 对原特定接触类的像条件。

本文没有新增环境来源、目标素数扫描或维数满射假设；全局跨 $p$ 非零仍未获得。
