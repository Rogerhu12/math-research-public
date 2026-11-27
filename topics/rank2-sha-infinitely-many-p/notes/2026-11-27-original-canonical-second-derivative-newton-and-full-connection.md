# 原 canonical 二阶导数的完整 Newton 端点与未删连接补偿

日期：2026-11-27 UTC。**状态：以下同一 Gaussian 的全精度恒等式、完整尾和实际端点阶数已证明；主目标未完成。**

本注保持原 $S_{34}$ 来源、同一个高度二 Gaussian 与全部有理系数，证明
$$
J_{D^2S}^{[-2]}(v)=(p+1)v((p+1)v-1)J_S(v).
$$
这里 $D^2S$ 是原函数的实际二阶导数，**不是**另一个已付有界的 degree34 theta 截面。其 Newton 级数的全部尾在本文由真实导数的三项卷积支付。

因 $S(0)=0$，完整归一负二函数 $K_{D^2S}=J_{D^2S}^{[-2]}/(pv)$ 的零点值恒为零；原 canonical 坏条件 $J'_S(0)=0$ 准确要求的是 $K'_{D^2S}(0)=0$。这与原 PB4 三条实际 type‑4 读者 $K_{j,p}(0)$ 是不同的条件。以下把另一 dyadic 分量与全部 $\zeta$ 项同式保留，不由非零 Soulé 端点删除它们。

## 1. 同一原来源和同一个 Gaussian

在原 $b=1$ 模型上固定
$$
E:y^2=x^3+1,\qquad Dx=2y,\quad Dy=3x^2,\quad
D=\frac d{dz},\quad \zeta=\frac{\sigma'}{\sigma},\quad D\zeta=-x.
$$
原 [R798(6)](../results/R798-original-halfperiod-two-types-and-e-depth-second-source.md) 的实际来源为
$$
\begin{split}
S&=\sigma^{34}R_S,\\
R_S&=x^2\left(X^4-\frac{53}7X^3-\frac{12}7X^2
                    -\frac{80}7X-\frac{128}7\right),\quad X=x^3,\\
S&=z^6+O(z^{12}).
\end{split}
\tag{1}
$$
式(1)也就是 R855(44) 的同一个 $A_{24}H_{10}$，未更换原有限向量。回 $b=17$ 时按原首 $z^6$ 的 homothety 与周期同时运输；本注不重新给该运输选相位。

取
$$
p=6s-1>211,\quad d=p+1,\quad
c_\sigma=[z^d]\log(\sigma/z),\quad C=34c_\sigma,\quad v_p(C)=-1.
\tag{2}
$$
保原算术桥及实际谱投影的固定坏集。系数环 $\mathcal O$ 可在删去固定判别式后取为包含全部原系数的不分歧完成；$v_p(p)=1$。本注纯 Newton 部分只需式(1)的固定分母及原高度二范围，使用 PB4/Soulé 身份时另保各篇的原有限删集。

置
$$
\widehat S=e^{-Cz^d}S,\qquad
s_h=[z^{dh}]\widehat S,\qquad a_h=C^{-h}s_h\quad(h\ge0);
\quad a_h=0\ (h<0).
\tag{3}
$$
$s_0=a_0=0$。与 R989 的 $S$ 行完全同一的中央 Newton 函数是
$$
J_S(v)=\sum_{h\ge0}a_h(v)_h,\qquad
(v)_h=v(v-1)\cdots(v-h+1).
\tag{4}
$$
指数先按形式卷积解释。其真实解析性使用
$\sigma^\circ=\sigma e^{-c_\sigma z^d}$，而非假设剥出的指数在整个后述圆盘单独收敛。

## 2. 原来源的整尾及真实二阶导数的不同尾

令 $R=p^{-1/(2p)}$。R301 的完整原界给
$$
W=z^2x,\quad \|W\|_R\le1,\qquad
\|\log(\sigma/z)-c_\sigma z^d\|_R<p^{-1/(p-1)}.
$$
式(1)精确给
$$
\widehat S
=z^6\left(W^{14}-\frac{53}7z^6W^{11}
-\frac{12}7z^{12}W^8-\frac{80}7z^{18}W^5
-\frac{128}7z^{24}W^2\right)
e^{34(\log(\sigma/z)-c_\sigma z^d)}.
$$
所以 $\|\widehat S\|_R\le R^6$，从而
$$
v_p(a_h)\ge
B_h:=\left\lceil\frac{h(p-1)+6}{2p}\right\rceil\quad(h\ge1).
\tag{5}
$$
尤其 $B_1=1,\ B_2=B_3=2,\ B_4=3$，且 $B_h\to\infty$。这给
$$
J_S\in pv\,\mathcal O\langle v\rangle
$$
及半径 $|v|_p<p^{(p-1)/(2p)}$ 上的解析性。这里的下降阶乘有整系数；其导数在闭单位盘的 Gauss 范数同样不超过一。

现在定义实际局部函数
$$
Q=D^2S,\qquad
\widehat Q=e^{-Cz^d}D^2S,\qquad
b_h=C^{-h}[z^{dh-2}]\widehat Q,\qquad
J_Q^{[-2]}(v)=\sum_{h\ge0}b_h(v)_h.
\tag{6}
$$
负次系数按零解释。由于 $Q=30z^4+O(z^{10})$，有 $b_0=0$。

完整求导给
$$
\widehat Q=\widehat S''
+2Cd\,z^{d-1}\widehat S'
+Cd(d-1)z^{d-2}\widehat S
+C^2d^2z^{2d-2}\widehat S .
\tag{7}
$$
逐项取式(6)的系数，不删 Gaussian 项：
$$
\boxed{
b_h=dh(dh-1)a_h+
d\bigl(d(2h-1)-1\bigr)a_{h-1}+d^2a_{h-2}.
}
\tag{8}
$$
式(8)为特征零全式，$h=0,1,2$ 同样成立；没有以临界低窗代替全部级数。

与原有界 type‑4 theta 截面不同，式(8)只直接给
$$
v_p(b_1)\ge2,\qquad v_p(b_2),v_p(b_3)\ge1,\qquad
v_p(b_h)\ge B_{h-2}\quad(h\ge3).
\tag{9}
$$
第一式用 $d-1=p$，不是一般 type‑4 的首系数界。
因此 $J_Q^{[-2]}$ 在与式(4)相同的开圆盘解析，并有
$$
J_Q^{[-2]}\in pv\,\mathcal O\langle v\rangle,\qquad
K_Q(v):=\frac{J_Q^{[-2]}(v)}{pv}\in\mathcal O\langle v\rangle.
\tag{10}
$$
这已经独立证明了原点可去，而非从尚未证明的端点等式定义函数。

例如截到 $h\le H$、$H\ge3$，式(9)给整个闭单位盘上的准确安全尾界
$$
\left\|
K_Q-\frac1p\sum_{h=1}^{H}b_h\frac{(v)_h}{v}
\right\|_{\rm Gauss}
\le p^{-(B_{H-1}-1)}.
\tag{11}
$$
右端趋于零；同一界适用于任一固定阶的 $v$ 导数。其原因是
$(v)_h/v\in\mathbf Z[v]$，求导不增加 Gauss 范数。
本注没有将 R806 负二截面的较强 $B_h$ 尾直接套到 $D^2S$。

## 3. 真实三项卷积的完整解析恒等式

在下降阶乘基中，
$$
v(v)_h=(v)_{h+1}+h(v)_h,\qquad
v^2(v)_h=(v)_{h+2}+(2h+1)(v)_{h+1}+h^2(v)_h.
\tag{12}
$$
所以多项式 $dv(dv-1)$ 乘式(4)后，$(v)_h$ 的系数恰为式(8)。
式(5)、(9)已付全部尾，因此这次有限带重排在原解析圆盘合法，得到
$$
\boxed{
J_{D^2S}^{[-2]}(v)=dv(dv-1)J_S(v).
}
\tag{13}
$$
这里没有使用 $p^v$、没有作未定义的权延拓，也没有把不同 Gaussian 的两个截面相等。

作为独立的整数权核验，有限 Gaussian 卷积给每个 $k\ge1$
$$
\begin{split}
J_S(k)&=k!C^{-k}[z^{dk}]S,\\
J_Q^{[-2]}(k)&=k!C^{-k}[z^{dk-2}]D^2S
             =dk(dk-1)J_S(k).
\end{split}
\tag{14}
$$
式(13)的证明已由三项重排完成；式(14)不承担任何额外的 period 或幂的解析延拓。

## 4. canonical 坏条件准确位于哪个端点

由式(10)、(13)，
$$
\boxed{
K_Q(v)=d(dv-1)\frac{J_S(v)}p.
}
\tag{15}
$$
$J_S(0)=0$ 是原来源的真实质量零。因此
$$
\boxed{
K_Q(0)=0,\qquad
K_Q'(0)=-\frac d p J_S'(0),\qquad
(J_Q^{[-2]})''(0)=-2dJ_S'(0).
}
\tag{16}
$$
特别，在原通常全 Selmer 桥所授权的坏假设 $J_S'(0)=0$ 下，
$$
K_Q\in v^2\mathcal O\langle v\rangle.
\tag{17}
$$
若 $J_S'(0)\ne0$，则 $K_Q$ 在原点恰一阶；更一般，$J_S\not\equiv0$ 时
$$
\operatorname{ord}_{v=0}K_Q=\operatorname{ord}_{v=0}J_S.
\tag{18}
$$
这里 $d(dv-1)$ 在原点的常数为 $-d$，是单位。没有声称它在整个闭单位盘处处可逆。

故原坏条件的下一工作目标是式(16)的**一阶**，不能把它改成
原三条 type‑4 $K_{j,p}(0)$ 的零。
同样不能仅由 $K_{j,p}(0)$ 为单位，就否定式(17)。

## 5. 原连接的全部六列及完整 $\zeta$ 补项

置
$$
\nabla=D-34\zeta,\qquad F=\nabla^2S=\sigma^{34}D^2R_S.
\tag{19}
$$
用
$D^2x^a=2a(2a+1)x^{a+1}+4a(a-1)x^{a-2}$
逐项作用于式(1)，准确得
$$
\boxed{
F=\frac{\sigma^{34}}7
\left(-1024-8960X-11488X^2-26584X^3-21722X^4+5684X^5\right).
}
\tag{20}
$$
所以 $F$ 属于原完整六维 $V_4=\sigma^{34}K[X]_{\le5}$，首项为
$812z^4$。这是固定全来源，未只保首项。

令 $P_4$ 为 R798(10) 的同一个完整 dyadic 幂等元，定义
$$
F_+=P_4F,\qquad F_-=(I-P_4)F,\qquad
\mathcal R_S=68\zeta\nabla S+(1156\zeta^2-34x)S.
\tag{21}
$$
$F_+$ 与 $F_-$ 都是实际全纯 degree34 截面；其所有六列由
式(20)和 R798(10)准确固定，无另选同首项来源。
原完整恒等式是
$$
\boxed{D^2S=F_++F_-+\mathcal R_S.}
\tag{22}
$$
它来自 $\zeta'=-x$，特别最后的 $34x$ 为**负号**。
在原点
$$
F=812z^4+\cdots,\qquad
\mathcal R_S=-782z^4+\cdots,\qquad
D^2S=30z^4+\cdots,
$$
三个首项相符。虽然 $\mathcal R_S$ 在原点全纯、型为4，它含真实
$\zeta$，不将它认作原有限六维 theta 截面。

对 $F_\pm$ 用相同 $C$ 的原负二构造定义 $J_\pm,K_\pm$。
它们属于原完整 type‑4 有界格；由旧 Newton 注相同的
$z^2e^{-Cz^d}F_\pm$ 整界，$K_\pm\in\mathcal O\langle v\rangle$。
对 $\mathcal R_S$ 则定义其实际系数级数，解析尾由式(22)、(9)及
$F_\pm$ 的已付尾相减取得。于是也有实际整函数
$K_{\mathcal R}\in\mathcal O\langle v\rangle$，并且
$$
\boxed{
K_+(v)+K_-(v)+K_{\mathcal R}(v)
=d(dv-1)\frac{J_S(v)}p.
}
\tag{23}
$$
这里没有让 $\zeta/G$ 补偿躲在一个未定义常数中：
$\mathcal R_S$ 是式(21)完整指定的原函数，其所有 Newton 系数都从同一 Gaussian 取出。

R806 的三条首 $z^4$ 归一线 $D_j$、$j=4,10,16$，完整张成
$\operatorname{im}P_4$。令 $e_j$ 为其实际 CM13 谱幂等元，明确取
$$
u_j=[z^4](e_jF_+),\qquad F_+=\sum_{j=4,10,16}u_jD_j .
$$
这些 $u_j$ 是固定原全谱确定的代数数，不是随 $p$ 拟合的系数。
因此式(23)的第一项准确是
$K_+=\sum_j u_jK_{j,p}$。其原有限分母及 Artin 基仍保持。
式(16)遂变成
$$
\boxed{
\begin{split}
\sum_j u_jK_{j,p}(0)+K_-(0)+K_{\mathcal R}(0)&=0,\\
\sum_j u_jK'_{j,p}(0)+K'_-(0)+K'_{\mathcal R}(0)
&=-d\,J'_S(0)/p .
\end{split}}
\tag{24}
$$
第一行不使用坏假设；坏假设控制的是第二行。
原 signed 绝对整周期或真实几何 cross 对三个 $K_j$ 的结论可用于
式(24)，但不能据它们删除另外两个实际完整来源。

## 6. 半周期三个译像及连接交换子

沿 R798 的同一绝对 lift，记三个非零二挠 Weyl 算子为 $U_e$，
$e^3=-1$。其和为 $\mathcal U$，并有
$$
\mathcal H=\frac{\mathcal U-I}{2},\quad
\mathcal H S=\omega^2S,\quad
P_4=\frac{I-\omega\mathcal H}{1-\omega^2}
    =\frac{\mathcal H-\omega^2}{\delta}.
$$
令 $\Pi_r$ 为实际 $\mu_6$ 型 $r$ 投影。原 CM lift 循环三个
$U_e$；因此对主型 $S$，每个 $e$ 精确满足
$$
\Pi_0U_eS=\frac13\mathcal U S=-\frac{\delta}{3}S.
\tag{25}
$$
原 $J_S$ 的各 $z^{dh}$ 读数只取型0，所以完整译像的同一
Newton 中央行确返回这个标量。它不授权对乘上其它函数的译像作同一替换。

$\nabla^2$ 把型0送型4，故
$$
\Pi_4\nabla^2U_eS=-\frac{\delta}{3}F,\qquad
\Pi_4U_eF=\frac{\delta}{3}(2P_4-I)F .
$$
从而
$$
\boxed{
\Pi_4[\nabla^2,U_e]S=-\frac{2\delta}{3}P_4F .
}
\tag{26}
$$
这里的实际交换子全式为
$$
\boxed{
[\nabla^2,U_e]S
=68j_eU_e\nabla S+(34Dj_e+1156j_e^2)U_eS,\qquad
j_e=\frac{y}{x-e}.
}
\tag{27}
$$
式(26)说明：若在完整译像之后作同一个连接，免费得到的三条行仍只有
原 $F$ 的同一个标量；新的 PB4 部分恰由式(27)的全费用产生。
不能将式(25)穿过 $j_e,Dj_e,j_e^2$，也不删其真实点移、Miller 或 cut。

## 7. 原物理首位：完整导数的 $h=2,3$ 不可省

式(5)给 $a_h\in p^2\mathcal O$ 对所有 $h\ge2$。
设
$$
\alpha_{S,p}:=\overline{a_1/p}
=\overline{\frac{[z^{p+1}]S}{pC}}\in k.
\tag{28}
$$
这里 $[z^d]\widehat S=[z^d]S$，因为 $S(0)=0$。
又 $J'_S(0)/p\equiv a_1/p\pmod p$，所以 $\alpha_{S,p}$ 正是
原 canonical 的第一必要行，含原 $pC$ 单位，未更换归一。

式(8)给全部模 $p^2$ 所需项
$$
b_1\equiv0,\qquad b_2\equiv2a_1,\qquad
b_3\equiv a_1,\qquad b_h\equiv0\ (h\ge4)\pmod{p^2}.
\tag{29}
$$
因此在整个 Tate 代数模 $p$，
$$
\boxed{
K_Q(v)\equiv
\alpha_{S,p}\{2(v-1)+(v-1)(v-2)\}
=\alpha_{S,p}v(v-1).
}
\tag{30}
$$
特别 $K_Q(0)=0$ 的首层抵消用到真实 $h=2,3$ 两项；
若把 $D^2S$ 冒认为原 type‑4 有界截面而只读其 $h=1$，会失去
式(30)的一阶条件。

真正的有界 $F_\pm$ 则满足旧负二读者的恒定首层
$$
K_\pm(v)\equiv K_\pm(0)\pmod p.
$$
于是式(23)进一步给
$$
\boxed{
K_{\mathcal R}(v)\equiv
-K_+(0)-K_-(0)+\alpha_{S,p}v(v-1)\pmod p.
}
\tag{31}
$$
即使其中某条原 $K_j(0)$ 是单位，它也先进入式(31)的常数补偿，
并不迫 $\alpha_{S,p}\ne0$。

作为原除 $p$ Hurwitz 规范的核对，R855(29)、(33)给
$$
\alpha_{S,p}
=-\frac{\mathfrak B_{34,p}(R_S)}{pC}
=\frac{\mathfrak B_{34,p}(R_S)}{34c_p}\quad\bmod p,
$$
其中 $pc_\sigma\equiv-c_p$。这没有将 Hurwitz 系数与普通
Taylor 系数混用。

## 8. 本注给出的真实后继条件

式(13)是同一原来源、同一 Gaussian、全部精度的恒等式。
它允许把实际 canonical 坏条件准确接到式(24)的一阶，且式(11)
给全部未知高尾的确定截断误差。没有从质量零推未付的中央零，也没有
将 ordinary 单位域读者搬到惰性处。

若要利用已付 type‑4 signed／几何非零，后继须消费式(24)的
$K'_-(0)+K'_{\mathcal R}(0)$，或证明其与相同 $K'_j(0)$ 的
真实关系；不能只重验三个 $K_j(0)$ 的非零或同一个 dyadic 秩。
同样，新 S3150 的有限 $K/Y$ 点域投影不会自动作用于式(24)的
无限 Newton 导数：两者若要连接，须先付同一有限测试与这条完整函数身份。

### 精确依赖

- [R798 原绝对 halfperiod、完整两型和矩阵](../results/R798-original-halfperiod-two-types-and-e-depth-second-source.md)，(3)–(11)。
- [R806 原三个十八阶 type‑4 来源](../results/R806-original-type-four-order-eighteen-and-negative-two-katz.md)。
- [R809 三个完整 CM13 连接分量](../results/R809-original-primitive-connection-three-cm13-components.md)。
- [R855 原 canonical 除 $p$ 行与同一完整来源](../results/R855-original-full-heat-connection-and-canonical-divided-jet.md)，(29)–(34)、(39)。
- [R989 十个实际来源的完整六位必要系统](../results/R989-original-ten-source-sixth-digit-and-unchanged-six-block-prefixes.md)，(12)–(21)；本文的 $S$ 即其中同一行。
- [原 type‑4 惰性负二 Newton 与全部尾](2026-11-27-original-type-four-inert-negative-two-newton-and-signed-line.md)，§§2–3。其 $B_h$ 界只用于本文真实有界的 $F_\pm$，不用来替代式(9)。
- [原绝对整周期 signed 比较](2026-11-27-original-type-four-inert-signed-cross-comparison.md)；其中原 Artin 基、Euler $1+1/p$、所有 norm 及固定有限坏集仍完整保留。
- [R321 原完整 Euler／移位 Newton 身份](../results/R321-jzero-fixed-six-torsion-primitives-and-complete-u-frame-transpose.md)，§8。本注的具体二阶三项卷积与端点阶数由式(7)–(16)直接证明。

本文无数学数值执行、无素数扫描、无新增工作流。

## 9. 完整 $\zeta$ 补项的指定热导数返回

本节只用 R855 的同一个双变量 sigma、微分及原齐次提升，进一步把式(21)中的非有界部分集中到一个准确的横向 jet。它不对 CM 点的 canonical 零值作参数微分。

在 R855 的参数环中写 $b=-g_3/4$，取
$$
\widetilde R_S=x^{14}-\frac{53}7 b x^{11}
-\frac{12}7 b^2x^8-\frac{80}7 b^3x^5-\frac{128}7 b^4x^2,
\qquad \widetilde S=\sigma^{34}\widetilde R_S.
$$
这是 R856(29) 已指定的原提升；沿整个参数环从 $z^6$ 起、首系数一。固定
$$
L_2=6g_3\partial_{g_2}+\frac{g_2^2}{3}\partial_{g_3},\qquad
\dot S=(L_2\widetilde S)|_{g_2=0,g_3=-4}.
\tag{32}
$$
$\dot S$ 是一个真实函数的指定参数导数，不是另选同一 CM 值的延拓。

R855(8)–(11)逐项给
$$
L_2\sigma=\frac12(\zeta^2-x)\sigma,\quad
L_2\widetilde R_S=2x^2R_{S,x}+\zeta DR_S
\quad\text{在原 CM 点}.
$$
这里 $L_2b=-g_2^2/12=0$ 在该点，全部 $b$ 系数导数已经计入。
将这些式子直接代入原 $\mathcal R_S$，得到
$$
\boxed{
\mathcal R_S=68\dot S+\sigma^{34}P_\zeta(X),\qquad
P_\zeta=
\frac{-108800X-35360X^2-408X^3+19822X^4-5474X^5}{7}.
}
\tag{33}
$$
特别 $P_\zeta$ 是完整固定多项式，并非一个未指定的边界误差。
可不展开地核它为
$$
P_\zeta(x^3)=1122xR_S-136x^2R_{S,x}.
$$
式(20)与(33)合并给
$$
\boxed{
D^2S=68\dot S+Q_S,\qquad
Q_S=\frac{\sigma^{34}}7
(-1024-117760X-46848X^2-26992X^3-1900X^4+210X^5).
}
\tag{34}
$$
$Q_S$ 是原完整六维 $V_4$ 中的固定截面，首项 $30z^4$。
它也正是 R855(13) 的
$-68\sigma^{34}\mathcal H_{34}\widetilde R_S|_{\rm CM}$，
因而保留了同一有限热连接的所有系数。

### 9.1 原 Gaussian 在这一横向 jet 没有新增项

在通用模型中，
$c_\sigma(g_2,g_3)=[z^d]\log(\sigma/z)$
是权 $d$ 的有理多项式。由于 $d=6s$，其中可能的单项
$g_2^a g_3^b$ 满足 $4a+6b=d$，故 $3\mid a$。
因此精确地
$$
\boxed{L_2(34c_\sigma)|_{\rm CM}=0.}
\tag{35}
$$
这是特征零等式，不是仅模 $p$ 删一个可能带 $p$ 分母的项。

等价地，可在双数环上取
$g_2=-24\epsilon,\ g_3=-4,\ \epsilon^2=0$。
原来源和原 Gaussian 的一阶资料准确为
$$
\widetilde S_\epsilon=S+\epsilon\dot S,\qquad
C_\epsilon=C .
$$
因 $dh-2\equiv4\bmod6$，$S$ 的对应系数全部为零，故同一
负二系数构造的一阶项就是
$$
J_{\widetilde S_\epsilon}^{[-2]}(v)
=\epsilon J_{\dot S}^{[-2]}(v).
\tag{36}
$$
此处解析性不用未经证明的整个模量盘：式(34)已把这个实际一阶函数
写成 $D^2S$ 与有界 $Q_S$ 的线性组合，所以其全部 Newton 尾由
式(9)–(11)和原 type‑4 尾直接支付。

原低阶规范还给
$$
\widetilde S=z^6+\frac{67}{120}g_2z^{10}+O(z^{12}),
\qquad \dot S=-\frac{67}{5}z^{10}+O(z^{16}).
$$
第一式只用 $x=z^{-2}+g_2z^2/20+\cdots$ 与
$\sigma=z\exp(-g_2z^4/240+\cdots)$ 的完整最低项；
第二式再使用 $L_2g_2=-24$ 及 CM 型。没有因首阶较高就将
$\dot S$ 当作一个原有界 type‑4 截面。

### 9.2 原坏条件现在集中到同一热 jet 的一阶

按上述实际系数定义 $K_{\dot S}$。式(34)给完整解析身份
$$
\boxed{
68K_{\dot S}(v)+K_{Q_S}(v)
=d(dv-1)J_S(v)/p.
}
\tag{37}
$$
因此
$$
68K_{\dot S}(0)+K_{Q_S}(0)=0,\qquad
68K'_{\dot S}(0)+K'_{Q_S}(0)=-dJ'_S(0)/p.
$$
$Q_S$ 的两个 dyadic 分量均须保留；它们可以用原完整矩阵直接分解。
式(30)还给
$$
K_{\dot S}(v)\equiv
-\frac{K_{Q_S}(0)}{68}+
\frac{\alpha_{S,p}}{68}v(v-1)\pmod p.
$$
这使待消费项成为一个指定的同源横向热 jet，而非任意扩展连接。
但是 $J'_S(0)=0$ 只在原 CM 纤维授权，不给
$L_2J'_S$、$K_{\dot S}(0)$ 或 $\dot S$ 的中央另加零。

若用 full toric 双核或 Gauss–Manin 来返回式(37)，必须识别
式(32)的实际提升，或同时支付它与另一水平有限来源之间的
$\mathcal H_{34}$ 差。式(35)已支付这一层的 Gaussian，
却没有支付任何尚未证明的横向 canonical 消失。

## 10. 原半周期投影的两端热运输及准确有限修正

本节把上一节的 $Q_S$ 同时认作原有限投影的实际一阶变化。所有参数变化均在判别式不为零的一个单连通邻域上进行；先固定完整 level2 标签、原半特征和 R798 的 canonical lift，再作导数。这里使用的是 whole degree34 theta bundle，不在变形前后硬认同 CM 型四子空间。

### 10.1 挠点、准周期与 lift 一起变化

在 R855 的通用曲线上，令 $\tau$ 为一个非零半周期的实际解析 lift，置
$$
e=x(\tau),\qquad a_\tau=\zeta(\tau),\qquad
(U_\tau F)(z)=
\epsilon_\tau e^{-m a_\tau(z+\tau/2)}F(z+\tau).
\tag{38}
$$
$\epsilon_\tau$ 是 R798 原 lift 的固定根单位；它由 CM 点的完整 multiplier 锚定，随后在所取邻域内保持同一分支。其导数为零。不能把这个常数换成另一半周期规范。特别在 $m=34$ 时，三个原 $U_\tau$ 的有限乘法关系继续给 R798 的同一个 $\mathcal H=(\sum U_\tau-I)/2$ 和两条 dyadic 特征。

因 $y(\tau)=0$，由 R855(9)及 $Dy(\tau)=3e^2-g_2/4\ne0$，准确有
$$
L_2\tau=-a_\tau.
$$
再对 $\zeta(\tau)$ 作全导数，得到
$$
\boxed{
L_2\tau=-a_\tau,\qquad
L_2a_\tau=g_2\tau/12,\qquad
L_2 e=2e^2-g_2/3 .
}
\tag{39}
$$
这里第二式的两项 $-\zeta(\tau)e$ 和
$D\zeta(\tau)L_2\tau$ 正好相消。三式都在完整族上成立，不是仅在 CM 点冻结挠点。

置
$$
H_m^\infty=\frac{D^2}{2m}+\frac{mg_2z^2}{24}.
$$
直接对(38)求导，并保留其平移参数和指数常数项，得
$$
\boxed{
[L_2,U_\tau]=[H_m^\infty,U_\tau]
=-a_\tau U_\tau D+
\left(\frac{m a_\tau^2}{2}
-\frac{mg_2\tau z}{12}
-\frac{mg_2\tau^2}{24}\right)U_\tau .
}
\tag{40}
$$
右端的 $U_\tau D$ 表示先作 $D$ 再作完整 $U_\tau$。
也可由 $DU_\tau=U_\tau(D-ma_\tau)$ 核其二阶部分；
势项的差为 $mg_2(z^2-(z+\tau)^2)/24$，正好给余下两项。
所以原 heat connection $L_2-H_m^\infty$ 与三个实际 lift 全部交换。

### 10.2 回原有限有理格的矩阵式

在 R855 的原有理基中写
$$
\mathcal H_m=L_2+B_m .
$$
其中 $L_2$ 只对基的系数作用，$B_m$ 是 R855(12)、(16) 给出的完整有限矩阵。用 $\sigma^m$ 共轭(40)，得到
$$
\mathcal H_m U_\tau^{\rm rat}=U_\tau^{\rm rat}\mathcal H_m.
$$
因而对同一 whole dyadic 幂等
$$
\mathsf P=\frac{\mathcal H-\omega^2}{\delta}
$$
有
$$
\boxed{
L_2\mathsf P+[B_m,\mathsf P]=0 .
}
\tag{41}
$$
(41) 包含半周期标签、全部 theta multiplier 及其相位；
不是把原 CM 点的一个常矩阵认成全族常矩阵。它在 $m=34$ 的 CM 型四部分正是既有 $P_4$，在 CM 型零的原 $R_S$ 上则有
$\mathsf P R_S=0$；最窄原出处是 [R798](../results/R798-original-halfperiod-two-types-and-e-depth-second-source.md)(2)、(6)、(7)，其中先付 whole $\mathcal H_YS=\omega^2S$，再定义该幂等，并非由 restricted type4 矩阵反推。

现在使用上一节的指定齐次提升。其有理基系数在 CM 点的
$L_2$ 导数为零，而
$$
Q_S=-68\sigma^{34}B_{34}R_S.
$$
将(41)作用于 $R_S$ 后，得到完整的有限修正
$$
\boxed{
(L_2\mathsf P)R_S
=\mathsf P B_{34}R_S
=-\frac1{68}P_4(Q_S/\sigma^{34}).
}
\tag{42}
$$
右边是式(34)的同一六列经 R798 的同一完整矩阵所得；
没有一个尚待任意选择的横向分量。

### 10.3 实际 heat-flat 来源与原齐次来源的区别

设 $R_S^{\rm flat}$ 解同一有限连接
$\mathcal H_{34}R_S^{\rm flat}=0$，且在 CM 点等于 $R_S$。
只取这一双数层，存在性和唯一性就是完整有限线性方程。
由(42)，准确有
$$
\boxed{
\begin{aligned}
L_2R_S^{\rm flat}|_{\rm CM}
   &=Q_S/(68\sigma^{34}),\\
L_2(\sigma^{34}R_S^{\rm flat})|_{\rm CM}
   &=\dot S+Q_S/68=D^2S/68,\\
L_2\bigl(\mathsf P\widetilde S\bigr)|_{\rm CM}
   &=-P_4Q_S/68,\\
L_2\bigl(\mathsf P S^{\rm flat}\bigr)|_{\rm CM}
   &=0 .
\end{aligned}
}
\tag{43}
$$
第三行的 $\mathsf P$ 按同一 sigma frame 作用于完整 theta 来源；因
$\mathsf P S=0$，求导该零值时 frame 本身的额外项不再贡献，
而有限矩阵导数仍正是(42)。第四行中，(42)与
$\mathsf P L_2R_S^{\rm flat}=P_4(Q_S/\sigma^{34})/68$
逐项相消。

等价地，在未剥 sigma 的函数表示中，
$0=(L_2\mathsf P)S+\mathsf P D^2S/68$；
这时 $\mathsf P$ 在 $D^2S$ 上必须按(38)的完整平移延拓理解。
$D^2S$ 不属于原有界 theta bundle，不能把这个延拓误认成只作用于六个有理基的常矩阵。

因此 actual finite Schwartz 的横向 Jacobi jet 可以完整返回：
它是 $\dot S+Q_S/68$，其 Newton 端点仍严格为式(37)除以68。
对原 CM 点的 $J'_S(0)=0$ 并未作模量微分；
(43)也未给 $\dot S$ 或 $P_4Q_S$ 增加算术中央零。
凡接 full toric 双核，须沿(40)–(43)保留这一同源有限修正，
并继续保留其 beta 槽的一阶费用。
