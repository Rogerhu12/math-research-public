# R836 — 原三长窗的完整核呈示、受限 Euler 值方程与同一修正

日期：2026-11-15。**状态：下列完整核呈示、原第四短行长度和指定三块目标的仿射解条件已证明。主目标仍未完成。**

[R834](R834-original-three-long-euler-blocks-and-complete-ramification-ideal.md)
已证明原三个长 Euler 窗与整个 $F\mathcal H_2+e\mathcal H_2$ 的交核为零。
本篇继续剩下的实际值：它们须满足同一曲线上的一个受限 Euler 方程，
随后还须通过同一个 $\mathcal H_1$ 的真实镜轴像。
后一步的解若存在则唯一。最后短行也读取这个解，不能另选修正。

本篇所有格都是原十九角截面格，并须已经整返回同一 $\mathcal W_D$。
它给实际核和指定目标的完整呈示，没有把呈示中的未知成员性认作非零结论。
尤其不由全 Euler 像的余核至多二维，推断高前缀的受限 Euler 像满射。

## 1. 原来源和三个长行

保留 R834 的原曲面、曲线与记号
$$
C=(F=0),\quad P=(0,1),\quad
\mathcal H_j=H^0(X,\mathcal O_X(jC)),\quad
N=\mathcal O_C(C),\quad
\kappa=C^2,\quad\chi=-K_XC.
\tag{1}
$$
$C$ 几何整，$P$ 光滑，$\mathcal E=Y\partial_Y$，
$e=\mathcal EF$ 且 $e(P)\ne0$。
十九角已付 $\mathcal E\mathcal H_j\subset\mathcal H_j$；
它始终是相对 Euler，公共总 charge 四十另在物理运输中处理。

沿 $C$ 的原支 $Y=\psi(t)$，原低轴满足
$$
g=\psi e^\eta,\qquad \operatorname{ord}\eta=h.
$$
只使用模 $t^T$ 的有限 Taylor 身份。要求
$$
\boxed{h<T\le2h,\qquad T>2\kappa,\qquad 3b<p,}
\quad b=\deg_YF.
\tag{2}
$$
因此 $h>\kappa$。原返回为
$$
q_{\rm src}t^r\mathcal H_3\subset\overline{\mathcal W_D},
\qquad q_{\rm src}(P)\ne0,
\tag{3}
$$
全部 $d^{-C_D}Q$、十九角帽和固定公共载体都包含在 (3)。
在原四块物理矩阵中，
$$
\boxed{T=T_M=s-r-13,\qquad p=6s-1,\quad1\le\ell<s-13.}
\tag{4}
$$
相对 $J_4$ 如单独使用则取 $T_J=s-r$，不与 (4) 互换。

在 (3) 的真实单位下三角运输后，三个满块的核就是
$$
K_{3,T}=
\{G\in\mathcal H_3:
G(t,g),\mathcal EG(t,g),\mathcal E^2G(t,g)
\in t^T k[[t]]\}.
\tag{5}
$$
R834 已给
$$
K_{3,T}\cap(F\mathcal H_2+e\mathcal H_2)=0.
\tag{6}
$$

## 2. 三次截面上的真实 Euler 值映射

令 $Z=V(F,e)$ 为原完全交，长度 $\kappa$，并令
$$
V_T=H^0(C,N^3(-TP)),\qquad
\mathscr Z_3=H^0(Z,N^3|_Z).
\tag{7}
$$
所有有限概形，包括固定角、奇点和非约化部分，都保留。

原截面序列和 R495 的消失给
$\mathcal H_3\twoheadrightarrow H^0(C,N^3)$。
定义
$$
D_3:H^0(C,N^3)\longrightarrow\mathscr Z_3,\qquad
D_3(V)=(\mathcal EG)|_Z,
\tag{8}
$$
其中 $G\in\mathcal H_3$ 是 $V$ 的任一真实全局提升。
若换成 $G+FH$，$H\in\mathcal H_2$，则
$$
\mathcal E(G+FH)-\mathcal EG=eH+F\mathcal EH,
$$
在 $Z$ 为零，故 (8) 良定义。它并非任意给定的局部法向值。

记 $H_-$ 为原严格负水平截面，
$$
z_-=C.H_-=u-\mu_{d,1}-\mu_{\infty,1},\qquad Z_-=C\cap H_-.
$$
R833 的完整 charge 零计算在此给
$$
\boxed{
\operatorname{im}D_3
=\ker\bigl(\mathscr Z_3\to H^0(Z_-,N^3|_{Z_-})\bigr),
}
\tag{9}
$$
$$
\boxed{
\operatorname{coker}D_3
\simeq\mathcal H_3^0/(F_0\mathcal H_2^0),\qquad
\dim\operatorname{coker}D_3=z_-,
}
\tag{10}
$$
其中 $F_0=F(t,0)\ne0$。
对原完整 $r=2$ profile，R827/R833 已付 $z_-\le2$。

为支付 (9)–(10)，在同一原角基中
$$
\mathcal H_j^0
=d^{j\mu_{d,1}}k[t]_{\le jz_-}.
\tag{11}
$$
这里次数在提出所示 $d$ 因子之后读取；无限远的零点也在截面除子中。
因 $3b<p$，$\mathcal E$ 在所有正 charge $1,\ldots,3b$ 上是单位，
所以 $\mathcal E\mathcal H_3=\mathcal H_3^{>0}$。
原 Koszul 序列给
$$
\mathscr Z_3
=\mathcal H_3/(F\mathcal H_2+e\mathcal H_2).
$$
将正 charge 商掉，$e$ 的零 charge 为零，唯一剩余关系为
$F_0\mathcal H_2^0$，得到 (10)。
严格 $H_-\simeq\mathbf P^1$ 上的限制序列把该商准确识别为
$Z_-$ 上的值商，证明 (9)。
维数是 $(3z_-+1)-(2z_-+1)=z_-$，
不是只计算互异有限根。

再令
$$
\iota_T:V_T\longrightarrow\mathscr Z_3
$$
为原限制。它单射，因为其核为
$H^0(C,N^2(-TP))$，次数 $2\kappa-T<0$。

定义第一个真实受限方程
$$
\boxed{
A_T:V_T\longrightarrow\mathscr Z_3/\iota_T(V_T),
\qquad A_T(V)=[D_3(V)],
\quad W_T=\ker A_T.
}
\tag{12}
$$
对每个 $V\in W_T$，存在唯一 $V_1\in V_T$ 使
$$
\boxed{D_3(V)=\iota_T(V_1).}
\tag{13}
$$
由 (9)，这个 $V_1$ 必在 $Z_-$ 上消失。
这是一条真实受限值条件；(9) 的全像结论没有证明 (12) 恒零或单射。

## 3. 同一全局来源实现两值，全部自由恰为 $F^2\mathcal H_1$

**引理 1。** 对 $V\in W_T$ 及 (13) 的唯一 $V_1$，
存在 $G_V\in\mathcal H_3$ 满足
$$
G_V|_C=V,\qquad(\mathcal EG_V)|_C=V_1.
\tag{14}
$$
所有实现 (14) 的原来源组成一个 $F^2\mathcal H_1$ 挠集。

**证明。** 先取任一全局提升 $G_0$。
由 (13)，$(\mathcal EG_0)|_C-V_1$ 在 $Z$ 上为零，
因而能准确除以截面 $e|_C$：
$$
\frac{(\mathcal EG_0)|_C-V_1}{e|_C}\in H^0(C,N^2).
$$
R495 的同源限制 $\mathcal H_2\twoheadrightarrow H^0(C,N^2)$ 满射；
取其提升 $H$，置 $G_V=G_0-FH$ 即得 (14)。

若两种提升之差为 $FK$，则保持第二值要求
$eK|_C=0$。$e$ 在整曲线 $C$ 上非零，故 $K|_C=0$，
从而 $K=FL$、$L\in\mathcal H_1$。
反向显然。证毕。

此处只把一个已经落入实际像的全局截面提升；
没有任选 $Z$ 值后略过 (12)，也没有另选环境曲线。

## 4. 第三长行的准确 $3\eta$ 镜轴，而非自由 normal

置
$$
e_0=e|_C,\qquad f_2=(\mathcal E^2F)|_C.
$$
在整个长度 $T$ 中，
$$
c_F(t):=(\mathcal E^2(F^2))(t,g)
=2e_0^2\bigl(1+3(f_2/e_0)\eta\bigr)
\pmod{t^T}.
\tag{15}
$$
它是实际单位。定义同一个原 $\mathcal H_1$ 的评价
$$
\mathcal E_{3\eta,T}:\mathcal H_1\longrightarrow k[[t]]/t^T,
\qquad
L\longmapsto L(t,\psi e^{3\eta}).
\tag{16}
$$

**引理 2。**
$$
\boxed{
(\mathcal E^2(F^2L))(t,g)
=c_F(t)\,\mathcal E_{3\eta,T}(L)\pmod{t^T}.
}
\tag{17}
$$
并且 (16) 单射。

**证明。** 原乘积法则逐项给
$$
\mathcal E^2(F^2L)
=\mathcal E^2(F^2)L+4F(\mathcal EF)\mathcal EL
 +F^2\mathcal E^2L.
$$
末项在 $g$ 上含 $\eta^2$，模 $t^T$ 为零。
以 $F=e_0\zeta+f_2\zeta^2/2+\cdots$ 展开前两项，得到
$$
2e_0^2
\{L|_C+3\eta(\mathcal EL)|_C
+3(f_2/e_0)\eta L|_C\},
$$
即 (17)；没有遗漏 Euler 作用在 $e_0$ 上的项。

若 (16) 为零，则
$L|_C+3\eta(\mathcal EL)|_C=0\bmod t^T$，
故 $L|_C$ 消到 $h>\kappa=\deg N$，所以 $L=cF$。
再读 $F(t,\psi e^{3\eta})=3e_0\eta\bmod t^T$，
由 $h<T$ 和 $p>3$ 得 $c=0$。证毕。

由引理 1，以下余类与提升选择无关：
$$
\boxed{
\Theta_T:W_T\longrightarrow
\frac{k[[t]]/t^T}{c_F\mathcal E_{3\eta,T}(\mathcal H_1)},
\qquad
\Theta_T(V)=[(\mathcal E^2G_V)(t,g)].
}
\tag{18}
$$
它是线性映射，像分母使用 (16) 的整个真实列，
不是任意长 $T$ 的多项式。

**定理 1（完整三长核）。**
$$
\boxed{
K_{3,T}\xrightarrow[\ G\mapsto G|_C\ ]{\ \sim\ }\ker\Theta_T
\subset W_T.
}
\tag{19}
$$
而且每个 $V\in\ker\Theta_T$ 对应唯一的原 $G\in\mathcal H_3$。

**证明。** 若 $G\in K_{3,T}$，有限逆 Taylor 展开给
$$
G|_C=G(t,g)-\eta(\mathcal EG)(t,g)\in t^T,
$$
$$
(\mathcal EG)|_C=(\mathcal EG)(t,g)
-\eta(\mathcal E^2G)(t,g)\in t^T.
$$
因此它们属于 $V_T$，并满足 (13)，再由第三长行为零得到 (18) 为零。

反之，取 $V\in\ker\Theta_T$。由引理 2，存在唯一 $L\in\mathcal H_1$
使 $G=G_V-F^2L$ 的第三长行为零。
其两个全局限制仍是 $V,V_1$。写
$W_j=(\mathcal E^jG)|_C$。
有限 Taylor 给
$$
G(t,g)=V+\eta V_1=0\pmod{t^T},
$$
$$
(\mathcal EG)(t,g)=V_1+\eta W_2,\qquad
(\mathcal E^2G)(t,g)=W_2+\eta W_3=0.
$$
后式乘 $\eta$ 得 $\eta W_2=0$，故第二长行也为零。
这证明存在；唯一性也由引理 2，或 R834 的 $F\mathcal H_2$ 交核为零。
证毕。

## 5. 原第四短行与全部十三行边界

由 R821 的完整 $\Gamma^{(4)}$，
三个物理长块长度为 (4)，第四块在乘 $w^{13}$ 后的长度为 $\ell$。
再保真实 $t^r$，其准确剩余长度是
$$
\boxed{\ell_{\rm eff}=\max(\ell-r,0).}
\tag{20}
$$
由于 $\ell<s-13$，始终 $\ell_{\rm eff}<T$。

原总 charge 四十、完整 $q_{\rm src}$ 和 $U_0$ 给四行有限下三角单位变换。
当前三行已消到 $T$ 时，第四行中所有低 Euler 行贡献在
$<\ell_{\rm eff}$ 消失，剩下单位倍的
$(\mathcal E^3G)(t,g)$。
因此定义
$$
\sigma_{\ell_{\rm eff}}:\ker\Theta_T
 \longrightarrow k[[t]]/t^{\ell_{\rm eff}},
\qquad
V\longmapsto(\mathcal E^3G_V^{\,*})(t,g),
\tag{21}
$$
其中 $G_V^{\,*}$ 是定理 1 的唯一三长核来源。
则原完整四块首核在 (3) 这个子格上准确为
$$
\boxed{
\ker\bar M^{\rm orig}|_{q_{\rm src}t^r\mathcal H_3}
\simeq\ker\sigma_{\ell_{\rm eff}}\subset\ker\Theta_T.
}
\tag{22}
$$
若原 $\ell\le r$，(21) 的目标为零，(22) 就是整个 $\ker\Theta_T$；
这是实际公共 $t^r$ 后的短行为空，不是删去原目标。

式 (20)–(22) 只在约化后读取。
原三个十三行跨界仍分别乘 $p$；
原 $p^4$ 矩阵末端的四次 $p^3$ 项亦保持。
它们不影响本篇首核同构，却必须在下一次 lifting 中用同一个
$G_V^{\,*}$ 继续读取。

## 6. 同一个指定三块目标的仿射判据

本呈示也直接处理一个给定的实际目标，不只处理零核。

首先保完整原目标的低行。
在约化的 $\Gamma^{(4)}$ 中，(3) 的所有像都属于
$w^{13+r}\bar\Gamma^{(4)}$。
原公共单位及 $q_{\rm src}(t,g e^{a_p\epsilon})$ 都是真单位，
故任一指定目标若不在这个实际理想中，已经不属于本子格的像。
不能先除去 $w^{13+r}$ 而忘掉这项检验。

若该检验通过，才在已读行上去掉公共前缀，
并使用原完整单位下三角逆，得到三个确定目标
$f_0,f_1,f_2\in k[[t]]/t^T$ 和最后短目标
$f_3\in k[[t]]/t^{\ell_{\rm eff}}$。
这一步包括原 $a_p^i/i!$、charge 四十、$q_{\rm src}$ 和 $U_0$ 全尾。

定义真实仿射截面纤维
$$
\mathscr V_0(f)=
\{V\in H^0(C,N^3):[V]_{<T}=f_0-\eta f_1\},
$$
$$
\mathscr V_1(f)=
\{V_1\in H^0(C,N^3):[V_1]_{<T}=f_1-\eta f_2\}.
\tag{23}
$$
这些纤维可能为空；每个非空纤维的差空间恰为 $V_T$。

**定理 2（指定目标的同来源完整判据）。**
所给目标属于原 (3) 子格的像，当且仅当存在同一对
$V\in\mathscr V_0(f)$、$V_1\in\mathscr V_1(f)$，满足
$$
D_3(V)=V_1|_Z,
\tag{24}
$$
并且以下两步成立：

1. 由引理 1 的同源论证，取 $G_0\in\mathcal H_3$ 实现
   $G_0|_C=V,\ (\mathcal EG_0)|_C=V_1$。须有
   $$
   f_2-(\mathcal E^2G_0)(t,g)
   \in c_F\mathcal E_{3\eta,T}(\mathcal H_1).
   \tag{25}
   $$
2. 令 $L$ 是 (25) 的唯一原 $\mathcal H_1$ 解，
   $G=G_0+F^2L$。同一个 $G$ 必须满足
   $$
   [(\mathcal E^3G)(t,g)]_{<\ell_{\rm eff}}=f_3.
   \tag{26}
   $$

对固定 $V$，(24) 中的 $V_1$ 至多一个，因为两个可能值之差属于
$V_T$，其 $Z$ 限制单射。
(25) 也与 $G_0$ 的选择无关，并且不能将其中的 $L$ 自由赋值。

**证明。** 必要性由两次有限逆 Taylor 得 (23)，由实际 $D_3$ 得 (24)，
再由 (17) 得 (25)–(26)。
反之，第三块已由 (25) 解到 $f_2$。
以 $W_j=(\mathcal E^jG)|_C$ 记同一来源的系数，有
$$
G(t,g)=W_0+\eta W_1=f_0,
$$
因为 $W_0=f_0-\eta f_1$、$W_1=f_1-\eta f_2$ 模 $t^T$。
又由 $W_2+\eta W_3=f_2$ 得 $\eta W_2=\eta f_2$，
所以 $(\mathcal EG)(t,g)=W_1+\eta W_2=f_1$。
最后 (26) 给同一个第四短块，逆原单位运输即恢复完整指定目标。
证毕。

因此这不是用分别可解的值与 normal 代替共同修正：
(24)、(25)、(26) 始终使用同一个 $G$。
若指定目标来自原 Bockstein，仍须先用全部真实 native 项算出这些
$f_i$，本定理没有预先给它们零值。

## 7. 已构造的旧镜轴家族与剩余范围

R731/R738/R741 的全部原镜轴来源
$$
P_B=q_{\rm src}t^rFB,\qquad B\in K_{\rm mir}\subset\mathcal H_2
$$
都落入 (6) 的实际子格。
所以在本篇确有三个长窗及 (2)–(4) 的范围，
它们除零以外全部不属于原四块首核。
这包含旧 $F^3$，也包含已经产生的非 cube $FB$ 家族；
不能把它们原样当成第四中央的候选。

另一方面，(22) 仍允许具有非零 $C$ 限制的来源。
(9) 的完整全像及 $z_-\le2$ 没有消除 (12)、(18) 的受限成员性；
有限余核小也不保证 (23) 的全局截面纤维非空。
这些正是原高前缀和同一 normal 的实际剩余方程。

本篇只呈示已付的 $q_{\rm src}t^r\mathcal H_3$。
整个 $\mathcal W_D$ 的其它列、真正四次幂格及任意较大来源不得据此删除。
原旧两长一短的 $\alpha_\eta$、指定 ramification trace 与十九边界，
以及完整同一 $R$ 的下一位 carry，仍按原目标继续。
