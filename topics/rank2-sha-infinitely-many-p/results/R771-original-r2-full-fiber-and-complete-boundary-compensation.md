# R771 — 原 r2 全有限纤维、末零角联合主部与完整边界补偿

日期：2026-11-15。**状态：本文的实际来源分裂、完整边界迹和同一修正的返回已证明；指定近支的全两输出像、真正第二余类及主课题仍开放。**

本篇接 R768 的实际 $r=2$ 增补。
在原有限纤维中，前篇只把最高一层的平方主部指定下来；
本篇支付整个两层的实际像。
当余因子零角阶为零时，再把它与末零角上的实际主部联合，
给出原 $\mathcal W_D$ 中明确的 $4+a_4$ 个列和完整剩余源核。
这些列都保原高尾，不是目标中的自由补列。

随后直接计算这些真实列的全部纤维迹。
除一个明确的顶 charge 情形外，三个 normal 输出的完整迹全部为零；
顶情形也只剩一条显示的有理函数行。
这准确定位了先前末零角单位的补偿，
没有将单个边界留数当成原左余核非零。
最后将所有列放回整个原 $M$ 的同一个修正方程。

## 1. 原实际窗口与两个零角阶

保 R750、R755、R765、R766 以及 R768 实际 $r=2$ 增补的全部前提：
$$
P^{\rm fact}=qt^2F^3,\quad q=d^{-C_D}Q,\quad d=1+8t,
$$
$$
r=2,\quad \ell=1,\quad k=0,\quad s=2h+2,\quad
N_0=s-13,\quad T=N_0-2,
$$
$$
p=6s-1>101,\quad f_D<p,\quad
b=\deg_YF,\quad \deg_YF(0,Y)=3,\quad D\ge3b.
\tag{1}
$$
仍使用原几何整曲线 $C=(F=0)$、光滑点 $P=(0,1)$、
原同一个整提升、$\mathcal E=Y\partial_Y$、
$\mathcal N=\mathcal O_C(C)$、全部十九角与
$$
M=c_*U_0w^{13}J.
$$
强接触和原 $e(P),q(P)$ 单位条件不变。
令
$$
B=\frac{b_s(0)q_0(0)e(0)^3u(0)^2}{a}\in k^\times
\tag{2}
$$
为前篇的原 forcing 常数。

原零角赋值为
$$
v_0(H)=\min_{t^iY^n\text{ 出现}}(4i-n).
$$
因为 $\deg F(0,Y)=3$、$q(P)\ne0$，
以及 $v_0(qt^2F^3)\ge-2$，准确有
$$
\boxed{-v_0(F)=3,\qquad m_q=-v_0(q)\in\{0,1\}.}
\tag{3}
$$
确实，若 $m_F=-v_0(F)$，则 $m_F\ge3$，
$v_0(q)\le0$，且 $3m_F+m_q\le10$。
因此 $m_F=3$，$m_q\le1$。

$m_q=0$ 时 $q(0,Y)$ 是一个非零常数；
$m_q=1$ 时它至多为一次多项式，不能把它在其它有限点认成单位。
特别，在 $D=3b$ 的原范围，
$\deg_YQ\le D-3b=0$，故必有 $m_q=0$。
这只是实际参数门，不宣称已有一个满足强接触的具体 $F$。

以下第2节对两种 $m_q$ 都成立。
第3节的末零角主部块明确要求 $m_q=0$。

## 2. 整个有限两层是原四个列的真实像

写
$$
F_0(Y)=F(0,Y)=c_0(Y-1)V_0(Y),\qquad
\deg V_0=2,\quad V_0(1)\ne0.
$$
令 $Z_0$ 是有限 $t=0$ 纤维中除 $P$ 外的全部部分。
它长度为二，可以非约化，也可以位于原 $C$ 的奇点。

在 $A=k[t]/t^2$ 上，原有限 Weierstrass 分解给
$$
F=U_F W,\qquad W=(Y-\psi)V,\qquad \deg W=3,\quad\deg V=2.
\tag{4}
$$
$U_F$ 在这个有限部分为单位，$\psi=1+\gamma_1t$，
$\gamma_1=154/15$。
$V(\psi)$ 为单位，所以准确有
$$
A[Y]/W\simeq A\times A[Y]/V.
\tag{5}
$$
这在 $V_0$ 有重根时仍成立；未将两个非 $P$ 方向当成两个独立简单根。

原 $n=0,1,2$、系数次数小于二的六列，
因 $q_0=q_1=1$、$q_2=(t-1)/d$ 为 $A$ 中单位，
向 $A[Y]/W$ 是同构。
限制在同一个低二阶值核后，准确满射到
$A[Y]/V$，后者维数为四。

使用前篇两个完整列
$$
L_2=Y-1+\gamma_1tY^2q_2,
$$
$$
Q_2=1-2Y-(1+9t)Y^2q_2
=(Y-1)^2-\frac{9t^2Y^2}{d}.
\tag{6}
$$
它们沿 $P$ 支消到 $t^2$。
在 $t=0$ 上，$Y-1$ 与 $(Y-1)^2$ 是 $k[Y]/V_0$ 的一组基；
因此 $L_2,Q_2$ 是 $A[Y]/V$ 的一组 $A$-基。

于是四个真实列
$$
\boxed{L_2,\ Q_2,\ tL_2,\ tQ_2}
\tag{7}
$$
给整个有限两层的单位矩阵。
乘 $t$ 后的系数次数仍不超过二，完全在原 $n=0,1,2$ 帽内。
这里的所有 $q_2$ 高尾均保留。

在原残余除子
$$
E|_C=2P+E'
$$
中总有 $2Z_0\le E'$；
$q$ 在其它有限点有零时，只是使 $E'$ 更厚。
按同一个 $q_0t^2$ 线束框，存在真实商
$$
\pi_{\rm fin}:\mathcal V_{E'}\longrightarrow
\mathcal P_{E'}/\mathcal P_{E'-2Z_0}.
\tag{8}
$$
它读取 $R|_C\bmod t^2$ 的非 $P$ 有限部分，
由 (7) 满射，秩准确为四。
若 $m_q=0$，$q(0,Y)$ 为常数单位，
所以有限 $t=0$ 部分的 $E'$ 准确就是 $2Z_0$。

这只指定一个实际投影。
原完整首次修正仍仅固定其中最高层
$$
R(0,Y)=-3B(Y-1)^2.
\tag{9}
$$
下一层由同一个 $R$ 决定，不能把 (7) 的满射当成它已被算术指定。

## 3. 末零角的完整原框与明确列

在第四零角图取
$$
U=tY^4,\qquad X=Y^{-1},
\qquad t=UX^4.
$$
由 (3) 及原来源帽，
$$
\widehat F(U,X)=X^3F(UX^4,X^{-1}),\qquad
\widehat R(U,X)=X^2R(UX^4,X^{-1})
\tag{10}
$$
在该图的有限 $U$ 部分正规。
原 $d=1+8UX^4$ 在 $X=0$ 为单位。

置
$$
A_F(U)=\widehat F(U,0)
=c_0+\sum_{j=1}^{a_4}\alpha_jU^j,\qquad
a_4=\deg A_F\le\left\lfloor\frac{b-3}{4}\right\rfloor.
\tag{11}
$$
$a_4$ 是实际次数，不能无条件换成右侧上界。
$A_F(0)=c_0\ne0$。

令 $Z_4$ 是末例外分量 $X=0$ 与 $C$ 在有限 $U$ 部分的全部交。
它由 $A_F=0$ 给出，长度准确为 $a_4$，没有 $U=0$ 部分；
$U=\infty$ 和前三条零角分量此时尚未删除。

写
$$
q(UX^4,X^{-1})=X^{-m_q}\widehat q(U,X).
$$
在原 $\mathcal B_D$ 框中，$P^{\rm fact}$ 为
$$
X^2qt^2F^3
=X^{1-m_q}U^2\widehat q\,\widehat F^3.
\tag{12}
$$
所以 $E$ 在末零角分量上的准确系数是 $1-m_q$。
当 $m_q=0$ 时有 $Z_4\le E'$，
并且 (10) 给真实最高主部投影
$$
\pi_4:\mathcal V_{E'}\longrightarrow
\mathcal P_{E'}/\mathcal P_{E'-Z_4}
\simeq k[U]/A_F.
\tag{13}
$$
右侧框读取
$$
B_R(U)=\widehat R(U,0).
$$
即使 $\widehat q(U,0)$ 与 $A_F$ 有共同根，
(13) 仍用 (12) 的线束框，而不是将 $\widehat q$ 当函数单位。
$m_q=1$ 时 (12) 不提供这份 $Z_4$ 主部，不能沿用 (13)。

对完整原列，$B_R$ 的准确自由帽为
$$
\deg B_R\le M_4=\left\lfloor\frac{D-2}{4}\right\rfloor.
$$
它只读 $n=4j+2$ 的最低 $t^j$ 系数。
令
$$
n_j=4j+2,\qquad
\kappa_j=7^j(-1)^{\lfloor(4j+3)/3\rfloor}\in k^\times.
$$
原 canonical 列给
$$
Z_j^{\rm seed}=\kappa_j^{-1}Y^{n_j}q_{n_j},
\qquad B_{Z_j^{\rm seed}}=U^j.
\tag{14}
$$
对 $1\le j\le a_4$，$n_j\le b-1<D$，
且原系数次数为零，故全部原帽已经支付。

$j\ge2$ 时，(14) 被 $t^2$ 整除，不需要低值校正。
$j=1$ 时取完整真实列
$$
Z_1=\frac17Y^6q_6+tY^2q_2,
\qquad q_6=th_7(t-1)^2d^{-3}.
\tag{15}
$$
它沿 $P$ 支消到 $t^2$，并且
$$
Z_1=t(Y^6-Y^2)\pmod{t^2},\qquad B_{Z_1}=U.
$$

还要同时杀掉整个有限 $2Z_0$，不能只杀其最高层。
将
$$
Y^2(Y^3+Y^2+Y+1)
$$
模 monic $V_0$ 的余式写为 $\alpha+\beta(Y-1)$，定义
$$
\boxed{\overline Z_1=Z_1-t(\alpha L_2+\beta Q_2).}
\tag{16}
$$
因为
$$
Y^6-Y^2-(Y-1)\{\alpha+\beta(Y-1)\}
$$
被 $(Y-1)V_0$ 整除，(16) 在整个有限 $2Z_0$ 上为零。
其低 $P$ 值仍消到二阶，末零角初式仍为 $U$。
对 $j\ge2$ 置 $\overline Z_j=Z_j^{\rm seed}$。
于是
$$
\boxed{
\pi_{\rm fin}(\overline Z_j)=0,\qquad
\pi_4(\overline Z_j)=U^j\bmod A_F.
}
\tag{17}
$$
所有校正只用了原 $tL_2,tQ_2$，没有新增来源或丢掉高尾。

$U,U^2,\ldots,U^{a_4}$ 是 $k[U]/A_F$ 的一组基：
$U$ 为单位，且从 $1,U,\ldots,U^{a_4-1}$ 换基的行列式是
一个符号乘 $c_0/\alpha_{a_4}$。
因此 (17) 是真正的单位块，而非仅一条非零边界行。
任取整系数提升后，其有限矩阵仍有单位子式；
这不声称原物理评价像因此饱和。

## 4. 联合实际像、整个剩余源核与参数门

以下保 $m_q=0$。
定义
$$
Z_{\rm one}
=-\sum_{j=1}^{a_4}\frac{\alpha_j}{c_0}\overline Z_j.
\tag{18}
$$
$a_4=0$ 时置 $Z_{\rm one}=0$，并省去末零角块。
它有
$$
\pi_{\rm fin}(Z_{\rm one})=0,\qquad
B_{Z_{\rm one}}=1-A_F/c_0,\qquad
\pi_4(Z_{\rm one})=1.
$$
再置
$$
Q_{\rm clr}=Q_2-Z_{\rm one}.
\tag{19}
$$
$Q_{\rm clr}$ 的完整有限两层与 $Q_2$ 相同，但末零角投影为零。

**定理 1。** 同一个实际来源给满射
$$
\boxed{
\Pi=(\pi_{\rm fin},\pi_4):
\mathcal V_{E'}\longrightarrow
\bigl(\mathcal P_{E'}/\mathcal P_{E'-2Z_0}\bigr)
\oplus k[U]/A_F,
}
\tag{20}
$$
秩准确为 $4+a_4$，有明确真实列
$$
L_2,\ Q_{\rm clr},\ tL_2,\ tQ_2,\
\overline Z_1,\ldots,\overline Z_{a_4}.
\tag{21}
$$
每一列保其整个原高尾。两个支撑不交，所以 (20) 是原主部的真实商。

整个源端核也可直接读取。令
$$
\mathcal W_D^{(2)}
=\{R\in\overline{\mathcal W}_D:\operatorname{ord}_P R|_C\ge2\}.
$$
则 $\Pi(R)=0$ 当且仅当
$$
\boxed{
R(0,Y)=0,\quad R=tS,\quad
F_0(Y)\mid S(0,Y),\quad A_F(U)\mid B_R(U).
}
\tag{22}
$$
这里 $R$ 始终属于原 $\mathcal W_D^{(2)}$；
(22) 不把 $S$ 或其高尾换成自由多项式来源。

证明如下。有限投影为零，加上原 $P$ 的低二阶门，
使整个有限 $W$ 商中的 $R$ 模 $t^2$ 为零。
原 $R(0,Y)$ 次数至多二，故被三次 $F_0$ 整除时只能为零。
写 $R=tS$ 后，准确只剩 $F_0\mid S(0,Y)$；
原 $t^1$ 层还给 $\deg_Y S(0,Y)\le6$。
末零角条件正是最后一个整除。
因 $B_R(0)=0$ 且 $A_F(0)\ne0$，它也可写为
$$
B_R=A_F\,U\,H(U),\qquad
\deg H\le M_4-a_4-1.
$$
这只是准确边界条件，不能据此把整个 $R$ 免费写成 $tF$ 倍数。

(20) 立刻给
$$
\boxed{\dim\mathcal V_{E'}\ge4+a_4.}
\tag{23}
$$
结合 R750 的真实 $\dim\mathcal V_{E'}=e'-\delta_C$，
得到实际必要门
$$
\boxed{
\mathcal B_D\cdot C-3\kappa-\delta_C\ge6+a_4.
}
\tag{24}
$$
$m_q=1$ 时本篇只支付有限块给出的右侧 $6$，
不免费加上 $a_4$。
(24) 是实际来源条件，未预付高接触 $F$ 的存在，也不是指定 forcing 非零。

## 5. 整个原 M 中的同一个 R

原首次修正满足 $R(0,Y)=-3B(Y-1)^2$。
由 (20)–(22)，它准确具有下式，而非各输出分别选解：
$$
\boxed{
R=-3B Q_{\rm clr}
+\lambda_1tL_2+\lambda_2tQ_2
+\sum_{j=1}^{a_4}\nu_j\overline Z_j
+R_{\rm rem},
\qquad R_{\rm rem}\in\ker(\Pi:\mathcal W_D^{(2)}\to\operatorname{target}).
}
\tag{25}
$$
两个 $\lambda_i$ 是原先未指定的下一有限层；
$\nu_j$ 和 $R_{\rm rem}$ 仍联立全部其它原边界。
(25) 的 kernel 是 (22)，不是环境主部的任意核。

令原完整
$$
\bar\beta=M(P^{\rm fact})/p\bmod p.
$$
全首次提升的剩余条件准确为
$$
\boxed{
\bar M R_{\rm rem}
+\lambda_1\bar M(tL_2)+\lambda_2\bar M(tQ_2)
+\sum_j\nu_j\bar M(\overline Z_j)
=3B\bar M(Q_{\rm clr})-\bar\beta .
}
\tag{26}
$$
这是整个原目标中的同一个方程。
也可以将 (25) 直接代入前篇的全长两输出 (21)，
但必须使用每条 (21) 的完整 $q_n$、$t/w$ 和 regular 高尾。

(20) 的单位发生在有限主部投影，**没有**把 (26) 中的物理列认成单位。
进入 $p^3$ 时仍保原整 $P^{\rm fact}+pR$、
完整 $U_0$、两个十三行 carry 和同一个下一修正。
整低右逆的 $p$ 倍变化照 R750 进入下一位，未重新选择高尾。

## 6. 全部纤维留数的准确有理迹

写原 primitive 多项式
$$
F(t,Y)=f_b(t)Y^b+\cdots+f_0(t).
$$
因 $b<p$，$k(C)/k(t)$ 可分；
在正规化上 $t$ 的映射次数为 $b$。
对任一原 $R$，令 $R_{\rm red}$ 是在 $k(t)[Y]$ 中模 $F$ 的次数 $<b$ 余式。

**定理 2。**
$$
\boxed{
\operatorname{Tr}_{k(C)/k(t)}\!\left(\frac{R}{F_Y}\right)
=
\frac{[Y^{b-1}]R_{\rm red}}{f_b(t)}.
}
\tag{27}
$$
所以同一个原微分满足
$$
\boxed{
\operatorname{Tr}\!\left(\frac{R\,dt}{tF_Y}\right)
=
\frac{[Y^{b-1}]R_{\rm red}}{t f_b(t)}\,dt.
}
\tag{28}
$$

证明：在分裂域对 $F$ 的互异根作 Lagrange 插值，
比较次数 $b-1$ 的系数，得 (27)；
$F$ 倍数的取值为零，所以先取余式合法。
(28) 随即成立。
对每个底点 $\alpha\in\mathbb P^1$，微分迹的局部留数公式给
$$
\operatorname{Res}_\alpha\operatorname{Tr}\omega
=
\sum_{Q\mid\alpha}
\operatorname{Tr}_{k(Q)/k(\alpha)}\operatorname{Res}_Q\omega.
\tag{29}
$$
可在 tame 参数 $t-\alpha=c z^e+\cdots$ 中直接核对；
$b<p$ 保这些分歧均 tame。
原 $C$ 奇点处取正规化各支和，即原 Rosenlicht 留数。
因此 (29) 保留了完整纤维，包含前三条零角、$U=\infty$ 和所有原固定角。

这是一个实际可用递推。令
$$
T_n(t)=\operatorname{Tr}(Y^n/F_Y).
$$
则
$$
T_n=0\ (0\le n\le b-2),\qquad T_{b-1}=1/f_b,
$$
$$
\boxed{
f_bT_n+\sum_{i=0}^{b-1}f_iT_{n-b+i}=0
\quad(n\ge b).
}
\tag{30}
$$
故对完整 canonical 来源 $R=\sum_nY^nq_np_n(t)$，
$$
\operatorname{Tr}(R/F_Y)=\sum_nq_np_nT_n.
\tag{31}
$$
同一式也读取 $\mathcal ER$、$\mathcal E^2R$，
只须分别乘 $n,n^2$。
(30)–(31) 不添加观察列，只计算原给定来源的完整边界。

(28) 的有限底极点仅可能位于
$$
t=0,\quad d=0,\quad f_b(t)=0,
$$
另保底无穷远。
个别分支的 ramification 极在迹中准确取消；
$f_b$ 的其它零点则不能删掉。
整个支持由原实际 $F$ 给定，没有将其换成固定有界极帽。

## 7. 联合边界块的完整三输出迹至多一维

假设 $b\ge4$。
(21) 中的低列仅含 charge $0,1,2$，而
$\overline Z_j$ 只有 charge $4j+2$ 和这些低校正。
所有 charge 都不超过 $b-1$。

因此 (30) 给一个准确范围，而非仅渐近估计：

- 若不存在 $j\le a_4$ 满足 $4j+2=b-1$，
  (21) 的全部列在
  $\operatorname{Tr}(R/F_Y)$、
  $\operatorname{Tr}(\mathcal ER/F_Y)$、
  $\operatorname{Tr}(\mathcal E^2R/F_Y)$ 下都为零。
- 唯一可能的非零情形是
  $b=4a_4+3$，且 $\alpha_{a_4}\ne0$ 为实际顶项。
  此时只有 $\overline Z_{a_4}$ 提供新迹，
  准确为
  $$
  \boxed{
  \left(
  \operatorname{Tr}\frac{\overline Z_{a_4}}{F_Y},
  \operatorname{Tr}\frac{\mathcal E\overline Z_{a_4}}{F_Y},
  \operatorname{Tr}\frac{\mathcal E^2\overline Z_{a_4}}{F_Y}
  \right)
  =
  \frac{q_{b-1}}{\kappa_{a_4}f_b}
  \bigl(1,b-1,(b-1)^2\bigr).
  }
  \tag{32}
  $$
  $Q_{\rm clr}$ 的非零迹只是这同一条的实际标量倍。

所以这个完整实际边界块的三输出迹秩至多一；
并未因三个 normal 观察而变成三个独立全局方向。
尤其原 $Q_2$ 的完整三个迹全为零，
但其有限主部仍有 $(\mathcal E^2-\mathcal E)Q_2(P)=2$。
任何只经过这些完整纤维迹的泛函，都不能代替这条指定近支的 normal 行。

## 8. 末零角的单位到底由哪里补偿

在 (10) 的原图，沿 $C$ 直接计算得
$$
F_Y=X^{-2}(4U\widehat F_U-X\widehat F_X),\qquad
dt=X^3(4U\widehat F_U-X\widehat F_X)\frac{dX}{\widehat F_U}.
$$
因此
$$
\boxed{
\frac{R\,dt}{tF_Y}
=\frac{\widehat R}{U\widehat F_U}\frac{dX}{X}.
}
\tag{33}
$$
沿用前篇的常数局部代表
$$
\omega_{\rm ord}=2c_0qt\,dt/F_Y.
$$
对 $u_R=R/(q_0t^2)$，其乘积在 (33) 上乘 $2c_0$。

于是末零角有限部分的完整留数和准确为
$$
\boxed{
\ell_4(B_R)
=2c_0\,\operatorname{Res}_{A_F=0}
\frac{B_R(U)\,dU}{U A_F(U)}.
}
\tag{34}
$$
对简单根 $\alpha$，其项为
$2c_0B_R(\alpha)/(\alpha A_F'(\alpha))$。
重根时用同一个有限完全交的 Grothendieck 留数；
它等于 monic 余式的最高系数泛函。
这一等式可在通用系数环的可分开集由 (33) 核实，
再因有限自由代数的两个迹泛函均正规而延拓；
不丢掉非约化交点或原奇点的分支和。

对 (18)，$B_{Z_{\rm one}}\equiv1\bmod A_F$，
所以当 $a_4\ge1$ 时
$$
\boxed{\ell_4(Z_{\rm one})=-2.}
\tag{35}
$$
这来自 $U=0$ 留数 $1/c_0$ 和无穷远留数零；
不是使用有限样本或假设根全在 $k$ 中。
(18) 的整个有限 $2Z_0$ 主部为零，$P$ 处也无留数。

(35) 的补偿现在完全由 (27)–(32) 决定：

1. **非顶情形。** 若 (32) 不发生，
   $Z_{\rm one}$ 的完整迹恒为零。
   因而同一 $t=0$ 纤维中其余原零角支的留数和准确为 $+2$。
   这些正是尚未包含于有限 $Z_4$ 的早层或 $U=\infty$ 支，不能删除。

2. **顶情形。** 若 $b=4a_4+3$，
   有 $f_b(t)=\alpha_{a_4}t^{a_4}+O(t^{a_4+1})$，
   且
   $$
   \boxed{
   \operatorname{Tr}\left(
   \frac{2c_0 Z_{\rm one}\,dt}{tF_Y}\right)
   =
   -\frac{2\alpha_{a_4}}{\kappa_{a_4}}
   \frac{q_{b-1}}{t f_b}\,dt.
   }
   \tag{36}
   $$
   其 $t=0$ 留数准确为 $-2$。
   此时有限纤维度三，加 $Z_4$ 上 $t=UX^4$ 的度 $4a_4$，
   已等于整个映射度 $b$，
   所以没有遗漏的其它 $t=0$ 支。
   其余底纤维的留数和准确为 $+2$，
   全由 (36) 在 $d=0$、$f_b=0$ 与无穷远的原有理补项给出。

同样，$Q_2$ 的有限 $Z_0$ 留数为 $+2$；
当 $a_4\ge1$ 时其 $Z_4$ 留数为 $-2$。
对 $b\ge4$，它的完整迹恒为零，故这两个局部单位没有留下一个
可直接充当原全局左行的余数。

(34)–(36) 支付的是实际补偿位置。
它们不证明任意候选全球 $\omega$ 必须等于这个局部代表，
也不证明 R768 的全球延拓方程有解或无解。
其它 $E'$ 数据、允许改动和原指定近支仍必须按 (26) 联立。

## 9. 保留的真正目标

本篇给出了一个全参数、同原帽的明确进展：
原有限两层四方向、末零角联合块、全部剩余源核，
以及该块所有边界的准确补偿。
它避免将未知下一有限层当成已固定，
也避免将单个零角单位或三个完整迹当成原非零左证书。

下一步仍是 (26) 的真实像，
或等价的 R768 指定近支全两输出与全球对偶延拓。
完整 $\xi$、同一个 $R$、原 $p^3$、$P_{134}/U_0$
和两条十三行 carry 均未删去。
原固定曲线的无穷素数结论仍未完成。

依赖：
[R768](R768-finite-fiber-normal-residue-and-original-global-pole-divisor.md)；
[实际 r2 增补](../notes/2026-11-15-r768-actual-r2-cubic-fiber-and-full-two-output-source.md)；
[R750](R750-whole-source-residual-divisor-and-specified-forcing-residue-rows.md)；
[R755](R755-whole-original-cube-carry-filter-and-specified-value-class-invariance.md)；
[R765](R765-original-zero-angle-and-unavoidable-nonfactor-first-correction.md)；
[R766](R766-actual-principal-part-normal-functional-and-specified-small-obstruction.md)。
