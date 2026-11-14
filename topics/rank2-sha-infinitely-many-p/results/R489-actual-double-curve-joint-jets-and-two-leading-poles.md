# R489 — 同一实际修正的双 jet 真像与两个最高极系数

日期：2026-11-14。**状态：已证明。** 本篇将 R472 的单独法向导数像推进为 R459 所需的**同一个修正的分支值与法向导数**。原连续 $2b$ 条 charge 给 $F^2$ 厚化上的完整限制，从而得到两个显式长度界；在界内，单位 $-2$ 与单位 $5$ 两条必要条件可同时由原仿射修正格实现。

界外也保真像：先给完整厚化空间的准确余核对偶，再用其余原列的实际消元选出整个 $\mathcal W_D$ 的真左行。对任一合法行，两条指定首项的配对恰为一个单位乘以两个最高极系数的明确组合。这个组合在真实高 $b$ 候选上的非零仍未证明。

以下始终区分这两条分支条件、整个相对 $J$ 首次提升、原 $M$ 的两条十三行 carry，以及 $d_2^J\to G_2$。联合分支满射不解决后三项。

## 1. 原来源与两个不同长度

沿用 R472 的实际单部分。设 $p=6s-1>83$、$f_D=\lfloor9D/2\rfloor+4<p$，写
$$
\mathcal W_D=\bigoplus_{n=0}^D Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
\qquad Y=\mathscr R,\qquad\mathcal E=Y\partial_Y,
$$
$$
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},\quad
A_n=\lfloor(n+1)/4\rfloor,\quad B_n=\lfloor(n+1)/3\rfloor,\quad
C_n=\lfloor n/2\rfloor,
$$
$$
h_7=7+4t+16t^2,\quad d=1+8t,\quad
e_m=3\lceil3m/4\rceil+2\lceil m/2\rceil+\lceil2m/3\rceil-2,
$$
$$
f_n=\deg q_n+e_{n+1}=\lfloor9n/2\rfloor+4,\qquad
M_n=f_n+C_n=5n+4-(n\bmod2).
\tag{1}
$$
以下向量空间都在原剩余域 $k$ 上；证明可先作代数闭包，所得矩阵秩及满射按原域下降。

设 $F(t,Y)=\sum_{i=0}^b f_i(t)Y^i\in k[t,Y]$ 不可约，
$F(0,1)=0$、$F_Y(0,1)\ne0$、$1\le2b\le D$。其正规分支为 $Y=\psi(t)$，并置
$$
u=u(F)=\max_i(\deg_t f_i-4i)\ge0.
\tag{2}
$$
待计算的映射准确为
$$
\boxed{\mathcal T_{V,N}:\overline{\mathcal W}_D\longrightarrow
k[[t]]/(t^V)\oplus k[[t]]/(t^N),\quad
R\longmapsto\bigl(R(t,\psi),(\mathcal ER)(t,\psi)\bigr).}
\tag{3}
$$
这里 $V\ge N$ 为长度。$t=-w+\cdots$ 保完整 jet 长度和像；乘共同角单位 $d^{C_D}$ 也只运输像，不扩来源。

## 2. 连续 2b 条原 charge 与全部低行

令
$$
n_0=D-2b+1,\quad A=A_D,\quad B=B_D,\quad
K=M_{n_0}-3A-B,\qquad
\mathcal H=(th_7)^A(t-1)^Bd^{-C_{n_0}}.
\tag{4}
$$
对 $n=n_0+i$、$0\le i\le2b-1$，
$\mathcal H/q_n$ 是实际多项式，次数为
$3(A-A_n)+(B-B_n)+C_n-C_{n_0}$。原列余下允许次数准确为
$$
e_{n+1}-\deg(\mathcal H/q_n)
=f_n-3A-B+C_{n_0}\ge K+4i.
$$
所以有同一预算的真实包含
$$
\boxed{\mathcal H Y^{n_0}\mathcal S_{2b-1,K}
\subset\overline{\mathcal W}_D,\qquad
\mathcal S_{m,K}=
\left\{\sum_{i=0}^{m}Y^iP_i(t):\deg P_i\le K+4i\right\}.}
\tag{5}
$$
负次数界表示零系数。这里没有在原来源上除 $\mathcal H$。

最初 $A$ 行必须在两个输出中同时填齐。对每个 $0\le r<A$，取两个原列
$$
Y^nq_n(t)t^{\,r-A_n},\qquad n=r+1,\ r+2.
\tag{6}
$$
有 $0\le r-A_n\le e_{n+1}$，且 $n\le D$。它们在 (3) 的首项阶为 $r$，两个首系数向量为 $(c_n,nc_n)$、$c_n\ne0$。行列式为 $c_{r+1}c_{r+2}$，是单位。依 $r$ 递增，得到最初 $A$ 对行上的块三角单位矩阵；产生的高尾全部保留。

在分支上写
$$
\eta(t)=\mathcal H(t)\psi(t)^{n_0}
=t^A\eta_0(t),\qquad\eta_0(0)\ne0.
\tag{7}
$$
对 (5) 中的 $R=\mathcal H Y^{n_0}Q$，其余输出长度为
$V'=V-A$、$N'=N-A$，规范化后恰是
$$
Q(t,\psi)=\eta^{-1}R(t,\psi),\qquad
(\mathcal EQ)(t,\psi)
=\eta^{-1}(\mathcal ER)(t,\psi)-n_0\eta^{-1}R(t,\psi).
\tag{8}
$$
因为 $V'\ge N'$，第二式没有丢失所需系数。这里只除已知的输出 $t^A$ 因子，不将其逆加入原格。

## 3. F² 厚化上的完整限制

用 R472 的 Hirzebruch 曲面 $\mathbb F_4$，负截面及纤维记为 $S_0,F_0$：
$$
S_0^2=-4,\quad S_0F_0=1,\quad
K_{\mathbb F_4}=-2S_0-6F_0.
$$
令 $C$ 为 $F=0$ 的整曲线闭包，**不作规范化**。则
$$
C\sim bS_0+(u+4b)F_0,\qquad
p_a(C)=(b-1)(2b-1+u).
\tag{9}
$$
$P=(0,1)$ 光滑，其他点可奇异。$C$ 及非约化 Cartier 曲线 $2C$ 都是 Gorenstein；以下保其真实对偶化层和算术亏格。

置
$$
\mathscr L=\mathcal O_{\mathbb F_4}
((2b-1)S_0+(K+8b-4)F_0).
$$
限制到 $2C$ 的核是
$$
\mathscr L(-2C)
=\mathcal O_{\mathbb F_4}(-S_0+(K-2u-4)F_0).
$$
它在每个纤维为 $\mathcal O_{\mathbf P^1}(-1)$，直接像及一阶高直接像均零，故所有上同调均零。因此
$$
\boxed{H^0(2C,\mathscr L|_{2C})=\mathcal S_{2b-1,K}.}
\tag{10}
$$
这支付了整个厚化限制及其余法丛部分，并非只比较两个维数。

记 $L=\mathscr L|_C$。准确序列为
$$
0\longrightarrow L(-C)\longrightarrow
\mathscr L|_{2C}\longrightarrow L\longrightarrow0.
\tag{11}
$$
伴随公式和交数给
$$
\boxed{\begin{aligned}
\deg(\omega_C L^{-1})&=-bK-u-4b^2-2b,\\
\deg(\omega_C L(-C)^{-1})&=(2b-1)u-bK-2b.
\end{aligned}}
\tag{12}
$$
例如 $\deg\omega_C=4b^2-6b+(2b-2)u$、$C^2=4b^2+2bu$，逐项相减即得两式。所用负度无截面及 Gorenstein 曲线对偶正是 R472 §3 中已经保全奇点的同一工具。

## 4. 同一个原仿射修正的联合满射界

定义
$$
\boxed{\begin{aligned}
\mathsf V_D(F)&=A+bK+u+4b^2+2b-1,\\
\mathsf N_D(F)&=A+bK-(2b-1)u+2b-1.
\end{aligned}}
\tag{13}
$$

**定理 1。** 若
$$
A<N\le V,\qquad V\le\mathsf V_D(F),\qquad N\le\mathsf N_D(F),
\tag{14}
$$
则原同源映射 (3) 满射。因而每个实际仿射修正空间
$R_{\rm base}+\overline{\mathcal W}_D$ 也同时充满两个目标。

**证明。** 先用 (6) 填齐两个输出的最初 $A$ 行，再减去所取原列的**全部**输出。余对在两分量均被 $t^A$ 整除；按 (7)–(8) 化为长度 $V',N'$。

由 (12)、(14)，有
$\deg(\omega_C L^{-1}(V'P))<0$，
故 $H^1(C,L(-V'P))=0$，所需值 jet 可由 $L$ 的全局截面实现。
另一界给
$\deg(\omega_C L(-C)^{-1}(N'P))<0$，
所以 $H^1(C,L(-C)(-N'P))=0$，并特别有 $H^1(C,L(-C))=0$。
已选的值截面遂可在 (11) 中提升；剩下的法向差由核 $L(-C)$ 修正。
局部核修正为 $FQ$，满足
$(\mathcal E(FQ))|_C=(\mathcal EF)|_C\,Q|_C$，
而 $(\mathcal EF)(P)=F_Y(0,1)$ 是单位。因此任意长度 $N'$ 的剩余法向 jet 都可实现，且不改变分支值。
最后 (10) 回到 (5) 内的同一个实际修正。$\square$

若两长度均不超过 $A$，(6) 单独满射。若 $N\le A<V$，先填低对再用 R472 的单输出值版本即可；(14) 则是下面两条长 jet 的范围。

R459 的 $r>2k$ 可读窗中，应取
$$
V=2h+k+1,\qquad N=h+k+1.
\tag{15}
$$
当 (14) 成立时，单位 $-2$ 值与单位 $5$ 导数，连同其前面全部零系数，可以由原仿射格**同时**实现。这只排除了基于这两条必要条件的单独不相容论证，尚未求解其余 $J$ 行。

## 5. 界外准确的几何余核，而非任意 Laurent 行

以下保 $K\ge-1$、$V',N'\ge1$。由
$\pi_*\mathscr L=\bigoplus_{i=0}^{2b-1}\mathcal O_{\mathbf P^1}(K+4i)$
及 (10)，有 $H^1(2C,\mathscr L|_{2C})=0$。
在 $P$ 的正规坐标 $(t,n)$ 中令 $n=F(t,Y)$，所以 $2C$ 上 $n^2=0$。取理想层
$$
\mathscr I_P=(t^{V'},\,nt^{N'}),
\tag{16}
$$
在 $P$ 外为整个结构层。其余长为 $V'+N'$，准确表示 (8) 的两个 jet，因为
$$
Q=q_0(t)+nq_1(t)\pmod{n^2},\qquad
q_1=(\mathcal EQ)|_C/(\mathcal EF)|_C.
\tag{17}
$$

令
$$
\boxed{\mathscr D_{V',N'}=
H^0\!\left(2C,\operatorname{Hom}
(\mathscr I_P,\omega_{2C}\otimes\mathscr L^{-1})\right).}
\tag{18}
$$
评价长正合列及 Gorenstein Serre 对偶把 (18) **准确识别**为 (10) 对 (16) 评价的余核对偶。这里不再商掉一个正则对偶截面：
$H^0(\omega_{2C}\mathscr L^{-1})
=H^1(2C,\mathscr L|_{2C})^*=0$。

在原仿射多项式平凡化下，将行写成
$$
\Phi=(A_\Phi(t)+nB_\Phi(t))\frac{dt\wedge dn}{n^2}.
\tag{19}
$$
其允许主部恰为
$$
\operatorname{ord}_tA_\Phi\ge-N',\qquad
\operatorname{ord}_tB_\Phi\ge-V'.
\tag{20}
$$
因为乘 $t^{V'}$ 及 $nt^{N'}$ 都必须正则。反之这两个界即充分。$t^{V'}$ 为非零除子，所以每个局部 Hom 都由总商环中这样的乘法给出，没有另漏一个扭 Hom。

准确剩余作用为
$$
\boxed{\lambda_\Phi(q_0,q_1)=
\operatorname{Res}_{t=0}(A_\Phi q_1+B_\Phi q_0)\,dt.}
\tag{21}
$$
两个主部不是独立全局行。式 (18) 的层有准确序列
$$
0\longrightarrow\omega_C L^{-1}(V'P)
\longrightarrow\operatorname{Hom}(\mathscr I_P,\omega_{2C}\mathscr L^{-1})
\longrightarrow\omega_C L(-C)^{-1}(N'P)
\longrightarrow0.
\tag{22}
$$
全局正则及右端截面的真实提升条件都包含在 (18) 中。由 (12) 得到的两个负度界使两端截面全零，正好给定理 1 的充分范围；界外某一度数非负本身并不证明行存在。

### 从完整厚化块回到全部原列

选 (6) 的块三角低行右逆 $\mathscr L_{\rm low}$。对任意原目标对 $v$，定义
$$
\widehat v=v-\mathcal T_{V,N}
\mathscr L_{\rm low}(v_{\text{最初 }A\text{ 对行}}).
\tag{23}
$$
减去的是原列的整个输出，高尾不删。再按 (7)–(8)、(17) 规范化 $\widehat v$，便可用 (21) 评价。

整个 (3) 的真左行空间准确为
$$
\boxed{\mathscr D^{\rm actual}_{V,N}
=\{\Phi\in\mathscr D_{V',N'}:
\lambda_\Phi(\widehat{\mathcal T_{V,N}(R)})=0
\text{ 对每一原基列 }R\in\mathcal W_D\}.}
\tag{24}
$$
帽号后始终含上述完整规范化。只须检查 (5) 及所选低列之外的原列；前两部分已自动消掉。
反过来，每条原左行杀低列，故经 (23) 因子化；它又杀 (5)，故由 (18) 的唯一行给出。这证明 (24) 是等号。

所有测试都用原 $q_n$、原次数帽和同一代数分支。未通过 (24) 的几何行不能当原真实障碍。

## 6. 单位 5 与单位 −2 的一个准确最高极组合

取真正的单 $Y$ 来源候选
$$
\bar P=t^rF^3Q,\quad
h=\operatorname{ord}_wF(t(w),\bar g(w)),\quad k=2h+r-s,
$$
$$
k<\min(s-h,\ell,h),\qquad r>2k.
\tag{25}
$$
这里允许 $Q$ 保原 $d$ 分母；它在 $(0,1)$ 为单位。R459 的局部证明直接适用于 $Y=\mathscr R$、$\mathcal E=Y\partial_Y$，并不需要将一个混 $\Theta$ 因子免费换成单 $Y$ 因子。

保 R459 的实际首项
$$
u_0=[w^h]F(t(w),\bar g(w)),\quad e_0=(\mathcal EF)(0,1),\quad
C_0=\left.(t(w)/w)^rQ(t(w),\bar g(w))\right|_{w=0}.
$$
Gaussian 常数 $a=p\kappa$ 为单位。两个必要目标准确为
$$
v(w)=-\frac{2C_0u_0^4}{ae_0}w^{2h+k}\pmod{w^{2h+k+1}},
\qquad
z(w)=\frac{5C_0u_0^3}{a}w^{h+k}\pmod{w^{h+k+1}}.
\tag{26}
$$
若使用共同清分母单位，必须同时运输两条目标，以下像及系数比不变。

取 (15) 的长度并保 $N>A$，置
$\iota=[t]w(t)=-1$、$\eta_*=[t^A]\eta(t)\in k^\times$。
两条目标的前 $A$ 对行都零，故 (23) 不改变它们。按 (8)、(17) 后，
$$
q_0=\alpha_Vt^{V'-1}\pmod{t^{V'}},\qquad
q_1=\alpha_Nt^{N'-1}\pmod{t^{N'}},
$$
$$
\alpha_V=-\frac{2C_0u_0^4\iota^{2h+k}}{ae_0\eta_*},
\qquad
\alpha_N=\frac{5C_0u_0^3\iota^{h+k}}{ae_0\eta_*}.
\tag{27}
$$
(8) 的 $-n_0q_0$ 项高于第二可读长度，因为 $V'-N'=h>0$；所有单位高项也不改变显示的首系数。

写
$A_\Phi=a_{-N'}t^{-N'}+\cdots$、
$B_\Phi=b_{-V'}t^{-V'}+\cdots$。
则 (21) 准确给
$$
\boxed{\lambda_\Phi(v,z)
=\alpha_N\left(a_{-N'}-\frac25u_0\iota^h b_{-V'}\right).}
\tag{28}
$$
$\alpha_N$ 为单位。这就是同一个修正的两条必要首项之间的实际配对。

对真实仿射修正空间 $R_{\rm base}+\overline{\mathcal W}_D$，两 jet 可同时实现，当且仅当每条 $\Phi\in\mathscr D^{\rm actual}_{V,N}$ 满足
$$
\boxed{\alpha_N\left(a_{-N'}-\frac25u_0\iota^h b_{-V'}\right)
=\lambda_\Phi(\mathcal T_{V,N}(R_{\rm base})).}
\tag{29}
$$
右端保 (23)、(8)、(17) 的整套规范化，不能把仿射基修正默设为零；对齐次像问题右端才是零。
全局正则 (18)、其他原列 (24) 和真实仿射基准都须保留。自由指定两个最高极系数不是非零证明。

## 7. 准确覆盖范围与临界高 b 的剩余部分

当 $D=3b$ 时，写 $A=\lfloor(3b+1)/4\rfloor$、
$\epsilon=(b+1)\bmod2$，有
$$
n_0=b+1,\qquad K=4b+9-\epsilon-3A.
\tag{30}
$$
因此
$$
\begin{aligned}
\mathsf N_D(F)&=A+b(4b+9-\epsilon-3A)-(2b-1)u+2b-1,\\
\mathsf V_D(F)-\mathsf N_D(F)&=2bu+4b^2.
\end{aligned}
\tag{31}
$$
若 $u/b\to\zeta$，两界的二次主项分别为
$(7/4-2\zeta)b^2$ 和 $(23/4)b^2$。
所以小 $u$ 且满足准确长度 (14) 时有真正的全参数联合像范围，仍在原 $D$ 预算，可包含 $D$ 为 $\sqrt p$ 量级的窗口。

但 R472 对真实立方只强制 $u\le b+O(1)$，端点处法向界的主项是 $-b^2/4$。**本充分界不覆盖整个高 b 或整个维数临界范围。** 其余范围应使用 (24)、(29)，不能把几何空间大小或有限计算称为统一满射。

固定证书取 $p=101,D=6,b=2,F=Y^2-1-t$：
$$
A=1,\quad n_0=3,\quad K=13,\quad
\mathsf V_D=47,\quad\mathsf N_D=27.
$$
(5) 的 $80$ 个真实高块列及 (6) 的两个低列，在 $47+27$ 个联合行上秩为 $74$。
这是原来源块的代数分支证书，**不声称该样本分支有原 theta 的所需高接触**。全参数结论由定理证明，不依靠样本外推。

## 8. 原 carry 与完整中央仍保原义

(26) 属于 R459 相对 $J$ 层 $p^2$ 提升的必要条件。原 $M$ 层还含 R479 的同一修正所输出的
$w^{s-13}B_0,w^{s-13}B_1$。不能将它们当自由选择，亦不能由联合分支满射将其删除。

在下一层继续保
$$
M=c_*U_0m_{13}J,\qquad
K_2^{\rm red}(M)=\ker(\pi\beta_J),\qquad
G_2=C_2(J)/\overline H
$$
及 R481 的同一修正完整公式。全 $P_{134}/U_0$、十三自由行、两条十三行 carry 和第三精度均未改变。

本篇不给任何新增来源列赋中央零。三条原完整中央失败仍按 R468 约束实际 regularized theta 轴，不能用来任意调整 $F$ 或其对偶行。要将 (29) 变成排除，须在该实际轴及仿射基准上证明一条通过 (24) 的行使两边不相等；这项非零尚未获得。

固定小证书见 [check-r489-actual-joint-branch-image.py](../scripts/check-r489-actual-joint-branch-image.py)。

