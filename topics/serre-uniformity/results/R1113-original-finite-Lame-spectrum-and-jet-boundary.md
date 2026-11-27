# R1113：原 theta 核的完整有限 Lamé 谱及指定 jet 的边界运输

日期：2026-11-27。纯证明；无数学程序或新窗口。本文消费 [R1061](R1061-actual-genus-two-etale-cover-and-original-three-torsion-Petri-point.md) 与 [R1095](R1095-original-theta-kernel-dual-Psi-normalization.md) 已固定的原模型、相对 Cartier、$J$、$A$、$\mathscr F$；不重新归一化核。

## 1. 原空间与结论

令 $p=6k-1\ge41$，$m=(p-1)/2=3k-1$，$N=k-1$。在代数闭包上工作，原曲线和微分为
$$
E:\quad V^2=U^3+v^2,\qquad v^2=-108,\qquad
\omega=\frac{dU}{2V},\qquad D=d/\omega .
$$
$Q=(0,v)$。保原
$$
D\Psi=\delta\in\mathbf F_p^\times,\qquad
D\mathcal R=\Psi,\qquad
\Psi^2=U^p+2\delta\mathcal R,\qquad
\Psi=VU\,S(U^3),\quad \deg S=N,\quad \operatorname{lc}S=-1.
$$
$\mathcal H=L((p+1)O)$，$V_0=L((p-1)O)$；保原 $\mathscr F=J^\sharp A$，其在 $V_0$ 上为 $\Phi$。在原 $u=U^{-1/2}\sim-U/V$ 标架中，$\ell_p$ 读 $u^{-p}$，$\ell_{\rm top}$ 读 $u^{-(p+1)}$。定义
$$
W=\ker(\ell_p:\mathcal H\longrightarrow k),\qquad
\mathscr L=D^2-2U .
\tag{1113.1}
$$
这是一个实际 $p$ 维空间：
$$
W=
\operatorname{span}\{1,U,\ldots,U^{m+1}\}
\oplus
\operatorname{span}\{V,VU,\ldots,VU^{m-2}\}.
\tag{1113.2}
$$

**结论。** $\mathscr L$ 保持 $W$，在 $W$ 上半单。设
$$
\mathcal Z=\{P\in E:\Psi(P)=0\}
$$
为全部有限零点，则 $\#\mathcal Z=p$，且原 $J_P(R)=J(P,R)$ 是 $W$ 的完整本征基：
$$
\mathscr L J_P=U(P)^p J_P .
\tag{1113.3}
$$
其特征多项式与首一最小多项式分别为
$$
\begin{aligned}
\chi_{\mathscr L}(X)&=X^2(X^3+v^2)S(X^3)^2,\\
\mu_{\mathscr L}(X)&=-X(X^3+v^2)S(X^3).
\end{aligned}
\tag{1113.4}
$$
最小多项式无重根。零本征空间恰为
$$
\ker\mathscr L=\operatorname{span}\{J_Q,J_{-Q}\}
=\operatorname{span}\{(V-v)^{2k},(V+v)^{2k}\}.
\tag{1113.5}
$$
这不是原指定 $e$ 的非零结论；其准确运输见 §6。

## 2. 双变量方程与实际极界

R1061 的原对数导数和 $J(T,R)=(U(T)^p-U(R))K(T,R)$ 给
$$
D_R\log J(T,R)=\Psi(T)+
\frac{V(R)-V(T)^p}{U(R)-U(T)^p}.
\tag{1113.6}
$$
置后项为 $\mu$。$D_RU=2V$、$D_RV=3U^2$ 直接给
$$
D_R\mu+\mu^2=2U(R)+U(T)^p .
$$
因而
$$
\left(D_R^2-2\Psi(T)D_R-2U(R)\right)J(T,R)
=-2\delta\mathcal R(T)J(T,R).
\tag{1113.7}
$$
$J$ 的原对称性给交换 $T,R$ 的另一行。这些都是实际有理核恒等式；在表面极点处按有理延拓，不删除零乘极。

不能据此把 $\mathscr L$ 说成保持整个 $\mathcal H$：确有
$\mathscr L\Psi=-2U\Psi$，极阶为 $p+2$。正确空间是 (1113.2)。逐基计算为
$$
\begin{aligned}
\mathscr L(U^j)
 &=2(2j-1)(j+1)U^{j+1}
   +4j(j-1)v^2U^{j-2},\\
\mathscr L(VU^j)
 &=2(2j+5)(j+1)VU^{j+1}
   +4j(j-1)v^2VU^{j-2}.
\end{aligned}
\tag{1113.8}
$$
系数为零的负幂项按零处理。偶基最高 $j=m+1$ 有 $2j-1=p$；奇基最高 $j=m-2$ 有 $2j+5=p$。因此两个越界项都真实为零，证明 $\mathscr L W\subset W$。

## 3. 全部零点、本征基与重数

$\Psi$ 在 $O$ 的极阶恰为 $p$，且 $D\Psi=\delta$、$\omega$ 处处非零，所以它的全部有限零点均为单零，恰有 $p$ 个。写 $Z=\sum_{P\in\mathcal Z}P$，则
$\operatorname{div}\Psi=Z-pO$。评价映射
$$
\operatorname{ev}_Z:\mathcal H\longrightarrow k^{\mathcal Z}
$$
的核为 $L((p+1)O-Z)$。该线丛同构于 $O(O)$，维数为一，且核含 $\Psi$，故核恰为 $k\Psi$。于是全部 $p$ 个评价泛函线性无关。

R1095 已付原 $J^\sharp:\mathcal H^*\to\mathcal H$ 可逆，且
$\ell_p(J_P)=\Psi(P)$。所以这 $p$ 个评价泛函的像 $J_P$ 全在 $W$，并构成 $W$ 的基。在 $\Psi(P)=0$ 处，原 Pell 式给
$-2\delta\mathcal R(P)=U(P)^p$；代入 (1113.7) 即得 (1113.3)。

零点分为：$Q,-Q$；$V=0$ 的三点；以及 $S(U^3)=0$ 的 $6N$ 点。这里
$$
S(0)=\frac{\delta}{2v^2},\qquad
S(-v^2)=-\frac{\delta}{3v^2},
$$
均非零。若 $S(\xi)=0$，则
$$
\delta=6\xi(\xi+v^2)S'(\xi),
$$
故 $S$ 无重根，也不碰前述两组。所有系数属于 $\mathbf F_p$，所以 $U(P)^p$ 与 $U(P)$ 有同一零点多重集：$0$ 重二，$X^3+v^2$ 的三个根各重一，$S(X^3)$ 的 $3N$ 个根各重二。这给 (1113.4)，并给其无重根的最小多项式。半单性来自已经构造的完整本征基，不来自“最小多项式应当无重根”的假定。

## 4. 本征基的精确原配对

保 R1095 的
$$
A(f,g)=[u^{-p-1}]\,fg\,\frac{\omega}{du}.
$$
其在 $\mathcal H$ 上的根基恰为 $k\Psi$。由于 $\ell_p(\Psi)=1$，$W$ 是该根基的补空间，$A|_W$ 非退化。

原 Fay 核给
$$
A(J_P,J_R)=
-\frac{V(P)-V(R)}{U(P)-U(R)}\bigl(\Psi(P)+\Psi(R)\bigr).
\tag{1113.9}
$$
在 $\mathcal Z\times\mathcal Z$ 上，准确结果为
$$
A(J_P,J_R)=-\delta\,\mathbf 1_{R=-P}.
\tag{1113.10}
$$
若 $R\ne-P$，弦斜率无极（同点使用切线），右边为零。若 $R\to-P$，取原 invariant 局部参数 $t$，则弦斜率为 $t^{-1}+O(1)$，而
$\Psi(P)+\Psi(R)=\delta t+O(t^2)$，故极限为 $-\delta$。当 $P=-P$ 为非零二挠点时，$U(R)-U(P)$ 始于 $3U(P)^2t^2$，$V(R)$ 始于 $3U(P)^2t$，同样得到斜率 $t^{-1}+O(1)$ 和 $-\delta$。这一步保留了所有零乘极和二挠对角项。

此外，对所有有限极界足以定义所需系数的有理函数，
$$
A(Df,g)=-A(f,Dg),\qquad
A(\mathscr Lf,g)=A(f,\mathscr Lg).
\tag{1113.11}
$$
第一式是 $[u^{-p-1}](fg)'=0$：对应未微分系数为 $u^{-p}$，因子为 $-p=0$。第二式随之成立。故 $\mathscr L$ 的上述半单谱与原 $A$ 完全相容。

## 5. 原 projector，及它不能代替的读数

对 $g\in W$，$A(g,J_P)=(\mathscr Fg)(P)$。原零谱投影因此是
$$
\Pi_0g=-\frac1\delta\left(
(\mathscr Fg)(-Q)J_Q+(\mathscr Fg)(Q)J_{-Q}\right).
\tag{1113.12}
$$
尤其 $\operatorname{im}\mathscr L=\ker\Pi_0$。

取原 $f=U^m$。R1061 已付
$\mathscr Ff=UH_p(U^3)$，所以 $\Pi_0f=0$ 自动成立。这既不证明
$H_p(0)\ne0$，也不证明 $H_p'(0)\ne0$。原 $e$ 读取 $J_P$ 对 $P$ 的一阶导数；它不是 (1113.12) 中的零谱系数。

## 6. 指定一阶与四阶 jet 的完整边界

令
$$
J_r(R)=\left.D_P^rJ(P,R)\right|_{P=-Q}.
$$
对 $1\le r<p$，(1113.7) 对第一变量逐次微分给
$$
\mathscr L J_r=2r\delta\,D_RJ_{r-1}
-r(r-1)\delta^2J_{r-2}.
\tag{1113.13}
$$
其中 $r=1$ 的末项为零。这里必须使用邻域中的完整式
$\mathscr LJ=2\Psi(P)D_RJ+(U(P)^p-\Psi(P)^2)J$：
$D_P(U(P)^p)=0$、$D_P\Psi=\delta$，但
$D_P^2(\Psi^2)=2\delta^2$，等价于 $D_P^2\mathcal R=\delta$。
不能把只在中心成立的 $-2\delta\mathcal R(P)=U(P)^p$ 用来微分。
原最高两系数同时给
$$
\ell_{\rm top}J_0=1,\quad
\ell_{\rm top}J_r=0\ (r\ge1),\qquad
\ell_pJ_1=\delta,\quad
\ell_pJ_r=0\ (r\ne1).
\tag{1113.14}
$$
因此 $J_1$ 的 $\delta\Psi$ 边界必须保留；$J_r\in V_0$ 对 $r\ge2$。

原读数准确为
$$
A(f,J_1)=e,\qquad
A(f,J_4)=16ve+4\delta^2K_4.
\tag{1113.15}
$$
这是 R1061 的原 Picard 一阶、四阶公式，而非辅助超几何参数导数。

还可把一阶障碍变成同一个 Lamé 算子的有界原像问题。令 $g$ 为满足
$$
\mathscr Lg=f,\qquad
g\in\operatorname{span}\{U^{3i+1}:0\le i\le k-1\}
\tag{1113.16}
$$
的唯一多项式。存在唯一性直接由 (1113.8) 的三角系数：从次数
$m-1$ 到 $1$，所有对角 $2(2j-1)(j+1)$ 都非零；源目标同为 $k$ 维。特别 $g$ 为偶函数，$\deg_Ug=m-1$，且 $Dg\in V_0$。由 (1113.11)、(1113.13)，
$$
e=-2\delta\,(\mathscr F(Dg))(-Q).
\tag{1113.17}
$$
$\mathscr F$ 保 $[-1]$ 奇偶，所以另一个点的读数为其负。因此
$$
e=0\quad\Longleftrightarrow\quad Dg\in\operatorname{im}\mathscr L.
\tag{1113.18}
$$
若 $e=0$，存在唯一奇函数
$h\in W$、其 $U$ 指数皆为 $2\bmod3$，满足 $\mathscr Lh=Dg$；其最高项至多
$VU^{m-3}$。两次同一实际分部积分又给
$$
\begin{aligned}
A(f,J_4)
={}&48\delta^2A(Dh,J_2)
+48\delta^3A(h,J_1)
-12\delta^2A(g,J_2).
\end{aligned}
\tag{1113.19}
$$
准确地，先用 $r=4$ 得
$A(f,J_4)=-8\delta A(Dg,J_3)-12\delta^2A(g,J_2)$，
再用 $\mathscr Lh=Dg$ 与 $r=3$ 即得 (1113.19)。
所以在 $e=0$ 下，
$$
K_4=12A(Dh,J_2)+12\delta A(h,J_1)-3A(g,J_2).
\tag{1113.20}
$$
三个项都属于原源；没有证明后两项相消，必须全部保留。这里也没有以
$\mathscr L$ 半单性代替该指定组合非零。

## 7. 第一障碍与原半 Dixon 的精确比例

写 $g=\sum_{j=0}^{N}g_jU^{3j+1}$。由 (1113.8)，
$$
g_N=\frac14,\qquad
\frac{g_{j+1}}{g_j}
=-\frac{(j+\frac16)(j+\frac23)}
 {v^2(j+1)(j+\frac43)},\qquad
g_0=\frac14(-v^2)^N
 \frac{N!(\frac43)_N}{(\frac16)_N(\frac23)_N}.
\tag{1113.21}
$$
这些分子分母在本范围均为单位。

在奇函数、CM 类 $0$ 的块
$\operatorname{span}\{VU^{3j}:0\le j\le N\}$ 上，
$\mathscr L$ 的像有余维一。取其余核泛函 $\ell(V)=1$，则
$$
\frac{\ell(VU^{3j+3})}{\ell(VU^{3j})}
=-v^2\frac{(j+\frac13)(j+\frac23)}
 {(j+1)(j+\frac32)}.
\tag{1113.22}
$$
在 $-Q$，原 $\Phi(V)(-Q)=v/3$；而
$\Phi(\mathscr Lh)(-Q)=0$ 由实际核方程成立。因此在整个该块上准确有
$\Phi(w)(-Q)=(v/3)\ell(w)$，不是未定单位比例。

令
$$
\mathcal D_N(z)=\sum_{j=0}^{N}
\frac{(\frac23)_j^2(\frac16)_j}
 {(j!)^2(\frac32)_j}z^j .
$$
$Dg$ 的第 $j$ 项对 $\ell$ 的贡献为
$t_j=2(3j+1)g_j\ell(VU^{3j})$。结合 (1113.21)–(1113.22)，
$t_0=2g_0$，且
$$
\frac{t_{j+1}}{t_j}
=\frac{(j+\frac16)(j+\frac23)^2}
 {(j+1)^2(j+\frac32)}.
$$
由 (1113.17) 得
$$
e=-\frac{4\delta v g_0}{3}\mathcal D_N(1),\qquad
\eta_k=\frac{16v^2g_0}{3\delta}\mathcal D_N(1).
\tag{1113.23}
$$
第二式消费 R1076 的原 $e=-\delta^2\eta_k/(4v)$。这把上述 Lamé 余核
和 R1061/R1109 的第一短系数放在同一精确标度上；没有将完整 $2k$ 项
反对称和、加权一阶矩或 Gross–Koblitz 参数变分替换成原 $\nu_k$。

**继续入口。** 本文封闭原有限 Lamé 空间、本征重数和全部 jet 边界；
尚需证明 (1113.17) 与 (1113.20) 的两个指定读数不能同时为零，或从同一原核
给出可替代它们的真实本原标签。


## 8. 同一个有限空间的完整 Lax 联合谱与三平移因子

定义原三阶算子
$$
\mathscr B=D^3-3UD-3V.
\tag{1113.24}
$$
它确实保持 $W$，并在该空间满足
$$
[\mathscr B,\mathscr L]=0,\qquad
\mathscr B^2=\mathscr L^3+v^2,\qquad
\mathscr B J_P=V(P)^pJ_P\quad(P\in\mathcal Z).
\tag{1113.25}
$$
所以 $(\mathscr L,\mathscr B)$ 的每条联合本征线都是一维。
这仍不把指定的 $e,K_4$ 变成一条已知非零的谱系数。

先完整检查空间边界。逐基微分给
$$
\begin{aligned}
\mathscr B(U^j)
={}&(2j-1)(2j+1)(2j+3)VU^j
 +8j(j-1)(j-2)v^2VU^{j-3},\\
\mathscr B(VU^j)
={}&8(j+1)(j+2)(j+3)U^{j+3}\\
&+(2j+1)(8j^2+8j+21)v^2U^j
 +8j(j-1)(j-2)v^4U^{j-3}.
\end{aligned}
\tag{1113.26}
$$
负幂项按其零系数解释。偶行的三个可能越界指标
$j=m-1,m,m+1$，分别由因子 $2j+3,2j+1,2j-1=p$ 消失；
奇行最高 $j=m-2$ 只到 $U^{m+1}$。故没有遗漏 $u^{-p}$ 或更高极边界。

对任意 $P$，令 $c=\Psi(P)$、$a=U(P)^p$、$b=V(P)^p$。
(1113.6) 给 $(D_R-c)J_P=\mu J_P$，
$\mu'+\mu^2=2U_R+a$。再微分一次，准确得到
$$
\left((D_R-c)^3-3U_R(D_R-c)-3V_R\right)J_P=bJ_P.
\tag{1113.27}
$$
事实上左边除以 $J_P$ 是
$V_R+(a-U_R)\mu=b$。在 $P\in\mathcal Z$ 时 $c=0$，
即得 (1113.25) 的本征值及其正号。
因为 §3 的全部 $J_P$ 是基，而 $b^2=a^3+v^2$，
前两个算子恒等式也在整个 $W$ 成立。
原分部积分还给
$$
A(\mathscr B f,g)=-A(f,\mathscr B g).
\tag{1113.28}
$$
这里使用 $DU=2V$，故 $(UD)^*=-UD-2V$；常数项 $-3V$
正是使三阶算子反自伴的项。

原 $Q$ 三平移也有一个完全付清的微分因子式。置
$$
h_0=\frac{V+v}{U},\qquad
h_1=-\frac{2v}{U},\qquad
h_2=\frac{v-V}{U}.
$$
原加法律给 $h_i=h_0\circ\tau_{-iQ}$，且 $h_0+h_1+h_2=0$。
直接有
$$
(D-h_1)(D-h_0)=D^2+h_2D-U,
$$
所以
$$
\boxed{\quad
(D-h_2)(D-h_1)(D-h_0)=\mathscr B+v.
\quad}
\tag{1113.29}
$$
把 $v$ 换成 $-v$ 得反向的 $\mathscr B-v$。
可直接核最后一步：$Dh_2-h_2^2=-2U$，
$-DU+h_2U=v-3V$。这是同一个原三挠点及同一个微分，
没有重选 theta 相位。单个一阶因子有真实极点；
本文只说完整乘积保持 $W$，不把每个因子当作 $W$ 的自同态。

对原 $f=U^m$，
$$
(UD+V)f=0,\qquad
\mathscr Bf=D^3f=-15v^2VU^{m-3}.
\tag{1113.30}
$$
因为 $D^2f=3v^2U^{m-2}$。这给原输入在联合谱中的实际联系，
而非任意换成一个本征向量。

(1113.27) 还给所有原中心 jet 的另一条完整关系：
$$
(\mathscr B-v)J_r
=3r\delta\,U J_{r-1}
 +3r(r-1)\delta^2D J_{r-2}
 -2r(r-1)(r-2)\delta^3J_{r-3},
\quad 1\le r<p.
\tag{1113.31}
$$
负指标项为零。证明时先微分 (1113.27)，得到
$3r\delta(D^2-U)J_{r-1}
 -3r(r-1)\delta^2DJ_{r-2}
 +r(r-1)(r-2)\delta^3J_{r-3}$，
再用已经修正的 (1113.13)。在 $P=-Q$，
$V(P)^p=v$；所有 Frobenius 坐标的正阶导数为零。
因此 (1113.31) 同时保留二次和三次的完整 carry。

## 9. 原输入自身的一维零谱源块及其全部实际 Cartier 列

另记
$$
\mathscr C=UD+V,\qquad d=2k-2,\qquad
W_C=U^2\,k[V]_{\le d}\subset V_0.
\tag{1113.32}
$$
$\mathscr C$ 不保持整个 $W$，例如
$\mathscr C(U^{m+1})=2VU^{m+1}$ 已越界。
但它严格保持这里的原 CM 类块，并有
$$
\mathscr C(U^2P(V))
=U^2\left(3(V^2-v^2)P'(V)+5VP(V)\right).
$$
其完整本征基及本征值为
$$
\begin{aligned}
f_j&=U^2(V-v)^j(V+v)^{d-j},\qquad 0\le j\le d,\\
\mathscr Cf_j&=6v(j-k+1)f_j.
\end{aligned}
\tag{1113.33}
$$
证明只需 $5+3d=p=0$。各本征值互异，且全部因子
$6v$ 与 $j-j'$ 在当前范围为单位。因此
$$
\ker(\mathscr C|_{W_C})=k f_{k-1}=kU^m.
\tag{1113.34}
$$
这个有限空间保留原输入，未用其它 theta vacuum 替换它。

也可直接检查整个有理函数域上的关系 $\mathscr C^p=-\mathscr C$。
取 $w=(V-v)/(V+v)$，则
$D\log w=6v/U$，所以
$\vartheta=(U/(6v))D$ 在 $k(w)$ 上是 $w\,d/dw$。
$k(E)/k(w)$ 可分，故 $\vartheta^p=\vartheta$。
由 $v^p=-v$ 得 $(UD)^p=-UD$。
而 $D\log U^m=-V/U$ 给
$\mathscr C=U^m(UD)U^{-m}$，结论随之成立。
这不取消前述空间极界；有限半单性已经由 (1113.33) 单独证明。

这里的每一列都有原 Miller/Cartier 来源。
记 $n=2k-1$，$\ell=n-j$，于是 $1\le\ell\le n$。
在 R1061 固定的 $Q$ 标架
$g_Q=U/(V-v)^{2k}$ 中，准确有
$$
f_jg_Q=
F_\ell:=\left(\frac{V+v}{V-v}\right)^\ell.
\tag{1113.35}
$$
因为两个指数之和由 $U^3=(V-v)(V+v)$ 完全相消。
原中间列 $j=k-1$ 恰为 $\ell=k$，即原 $F_Q$。

对所有这些 $\ell$，取任意零常数的多项式 primitive
$$
I_\ell'(V)=(V-v)^{n-\ell}(V+v)^{n+\ell}.
$$
其次数 $4k-1<p$，所有积分分母为单位。由于
$p-2=3n$ 及 $dV=3U^2\omega$，
$$
d\!\left(\frac{I_\ell(V)}{3U^p}\right)=F_\ell\omega.
\tag{1113.36}
$$
因此这些完整输入的 Cartier 值均为零。
令原次级读数
$$
e_\ell\omega'
=C_{\rm rel}(F_\ell\Psi\,\omega).
$$
使用 $D\Psi=\delta$ 作同一实际分部积分，
再把
$$
\frac{I_\ell}{3U^p}\omega
=\left(\frac1{9U^2}\right)^p
 I_\ell(V)(V^2-v^2)^n\,dV
$$
交给相对 Cartier，得到精确有限式
$$
\boxed{\quad
e_\ell=-\frac{\delta}{3}\,
 [V^{p-1}]\,I_\ell(V)(V^2-v^2)^n.
\quad}
\tag{1113.37}
$$
总次数至多 $8k-3<2p-1$，所以仅读 $p-1$，没有第二个
Cartier 指标。改变 $I_\ell$ 的积分常数也不影响此系数，
因为 $2n<p-1$。相对 Cartier 固定底域常数，
此处没有把 $v,\delta$ 另取 $p$ 次根。

由 R1061 的原导数核，$e_\ell$ 正是
$D_R(\Phi f_j)(-Q)$：原 CM 角色使
$(\Phi f_j)(-Q)=0$，故第三类修正项在该中心的值为零。
特别 $e_k=e$，(1113.37) 对中间列就是此前的原 $K_2$ 读数。
这一完整特征列族可供检验真正相邻列或三平移关系，
但它没有证明中间的 $e_k$ 为单位，也没有把其它列的非零代替原
$e,K_4$。要排除原两个读数同时为零，仍须保 (1113.20)
的全部三项或证明与此实际列族的精确比较。
