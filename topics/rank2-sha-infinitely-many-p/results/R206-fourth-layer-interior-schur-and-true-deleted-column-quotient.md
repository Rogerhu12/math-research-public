# R206 — 内部第四层 Schur 行、真实删列商与第一带 Hermite–Padé 矩阵

状态：证明完成；内部跨角向边界、整次数降阶与完整第一带参数变换已交叉核查，根端已核全文。本文只给实际局部格恒等式和明确的后续检测矩阵，不声称已取得严格的全素数预算。

本文沿用 [R199](R199-exact-first-band-exponential-and-complete-divided-image.md) 的原源与第一带、[R200](R200-first-saturation-graph-log-schur-kernel.md) 的有限 graph–log 核、[R203](R203-finite-central-companion-and-rational-row-lattices.md) 的中央整正规式，以及 [R205](R205-all-first-band-prefixes-and-truncated-image-interlacing.md) 的全部 $q$ 第三层两行边界。

## 1. 原对象、精度与本篇结论的范围

取
$$
 p=4r-1\ge19,\qquad R=r(p-1),\qquad O=\mathbf Z_p,\qquad
 a=17\tau_p\in O^\times,\qquad b=a/p.
$$
固定原源
$$
 E_D=O[A,C]_{\le D},\qquad C=B-A,\qquad
 A(w)=w+\cdots,\quad C(w)=v_0w^2+\cdots,\quad v_0=-22.
 \tag{1}
$$
特别 $p\ne11,17$。所有次数都是原 $A,C$ 总次数。

真实整轴 $f,c\in O[[y]]$ 满足
$$
 f=y+\cdots,\quad c=v_0y^2+\cdots,\qquad
 A(w)=e^{bw^r}f(w),\quad C(w)=e^{bw^r}c(w)
       \pmod{w^{R+1}}.
 \tag{2}
$$
令 $\mathcal E=A\partial_A+C\partial_C$。对原 $P\in E_D$ 定义
$$
 g_h(P;y)=(\mathcal E^hP)(f(y),c(y)).
$$
在
$$
 k=rq+s,\quad 0\le s<r,\quad q\le p-2
$$
的完整连续前缀中，真实归一行是
$$
 J_{rh+l}(P)
 =p^h[w^{rh+l}]P(A(w),C(w))
 =\sum_{i=0}^h p^{h-i}\frac{a^i}{i!}
       [y^{\,l+r(h-i)}]g_i(P;y),
 \quad 0\le l<r.
 \tag{3}
$$
所有 $n<k$ 行一起使用。设
$$
 K_N(J,k)=\{P\in E_D:J_{<k}P\in p^N O^k\},
 \qquad \Lambda_N(J,k)=p^{-N}K_N(J,k).
 \tag{4}
$$
不把一个源分解的各 summand 独立放进前缀核。

中央条件在所需前三项上给出
$$
 v_j=(f_{rj},c_{rj})=p j\,t_j+a\,t_{j-1},\qquad
 t_0=0,\quad t_j\in O^2.
 \tag{5}
$$
比较轴 $f^\circ,c^\circ$ 删去至少前三个中央项；删去更多项不改变本文模 $p^4$ 计算。只删前两个中央项时，下述内部第四层结论也相同，见 §2。比较行记 $J^\circ$。

R205 对每个 $q$ 都保证：若 $P\in K_3(J,k)$，则
$$
 (J_n-J_n^\circ)(P)\in p^3O\qquad(n+2<k).
 \tag{6}
$$
小 $q$ 时没有在此宣称同一个 $k$ 的 $\Lambda_3$ 完全相等。最后两行仍须单独保留。

## 2. 第四层展开：保留下一 $p$ 位与原二阶扰动

对 $t=(t_A,t_C)$ 写 $D_t=t_A\partial_A+t_C\partial_C$。定义
$$
 \begin{split}
 T^1_{h,l}(P)
 &=\frac{a^{h-1}}{(h-1)!}[y^l]\,
 D_{t_1}\{\mathcal E^{h-1}+(h-1)\mathcal E^{h-2}\}P(f,c),\\
 T^2_{h,l}(P)
 &=\frac{a^{h-2}}{(h-2)!}[y^l]\,
 D_{t_2}\{2\mathcal E^{h-2}+(h-2)\mathcal E^{h-3}\}P(f,c).
 \end{split}
 \tag{7}
$$
第一式 $h=1$ 省去第二项；第二式 $h=2$ 省去第二项。$h<1$ 的 $T^1$ 和 $h<2$ 的 $T^2$ 均为零。

由 (5)，第 $j$ 个向量 $t_j$ 的轴扰动准确为
$$
 t_j\{p j\,y^{rj}+a\,y^{r(j+1)}\}.
$$
在 (3) 中线性化并按归一幂计数得到
$$
 J_{rh+l}-J^\circ_{rh+l}
 =p^2T^1_{h,l}
 +p^3\{T^1_{h-1,l+r}+T^2_{h,l}\}\pmod{p^4}.
 \tag{8}
$$
二次及更高 Hasse Taylor 项从 $p^4$ 起；这不要求把源次数除以阶乘。第一式的低角项在实际轴或比较轴上相同，移位项的两种轴值模 $p$ 相同，因此 (7) 可以统一使用实际轴。

若只删 $v_1y^r+v_2y^{2r}$，则 (8) 的 $T^2$ 改成
$$
 \frac{2a^{h-2}}{(h-2)!}[y^l]D_{t_2}\mathcal E^{h-2}P(f,c).
$$
它在下面的内部范围同样为零。

对 $P\in K_3(J,k)$，不能先把 (8) 第一项除以 $p^3$ 后直接令 $P$ 模 $p$。起初要保留
$$
 p^{-1}T^1_{h,l}(P)+T^1_{h-1,l+r}(P)+T^2_{h,l}(P).
 \tag{9}
$$
下一节用已观测的真实前缀，合法消去第一项中的下一 $p$ 位。

## 3. 全部内部行的准确公式

定义去掉第一角带的移位
$$
 \mathsf Sg=\frac{g-g_{<r}}{y^r}.
$$
在实际轴上有
$$
 D_{t_1}=K(y)\mathcal E+L(y)\frac d{dy},
 \tag{10}
$$
其中
$$
 K=\frac{t_{1,A}c'-t_{1,C}f'}{fc'-cf'},\qquad
 L=\frac{ft_{1,C}-ct_{1,A}}{fc'-cf'},\qquad
 \operatorname{ord}K\ge-2,\quad\operatorname{ord}L\ge-1.
 \tag{11}
$$
这是应用于原多项式后再取轴值的等式；$\mathsf Sg_h$ 不是一个已经免费观测到的新列。

**定理 3.1（全内部第四层行）。**
若 $P\in K_3(J,k)$，$n=rh+l$、$h\ge1$、$0\le l<r$ 且 $n+2<k$，则
$$
 \begin{split}
 \frac{(J_n-J^\circ_n)(P)}{p^3}
 \equiv\frac{a^{h-2}}{(h-1)!}[y^l]\Bigl[
 &-K\{\mathsf Sg_{h-1}+(h-1)\mathsf Sg_{h-2}\}\\
 &+r(h-1)\frac Ly
       \{\mathsf Sg_{h-2}+(h-2)\mathsf Sg_{h-3}\}
 \Bigr]\pmod p.
 \end{split}
 \tag{12}
$$
负下标的项依其零前因子省去。特别 $h=1$ 时右边为
$-a^{-1}[y^l]K\mathsf Sg_0$。
$n<r$ 的差为零。

**证明。**
真实第零块首先给 $P$ 的常数和 $A$ 系数属于 $p^3O$。因此对每个 $h$，$g_h$ 的角 $0,1$ 系数属于 $p^3O$。

对 $j<r$，只要第 $h$ 块的第 $j$ 行已经观测，由 (3) 模 $p^2$ 得
$$
 \frac{[y^j]g_h}{p}
 \equiv-\frac h a [y^{j+r}]g_{h-1}\pmod p.
 \tag{13}
$$
这里分子先由真实行证明可除 $p$。

在 $j=r+e,\ e=0,1$ 的两个角向边界，要读下一块真实行。由于其首项 $g_{h+1,e}\in p^3O$，该行给出
$$
 p\frac{a^h}{h!}g_{h,r+e}
 +p^2\frac{a^{h-1}}{(h-1)!}g_{h-1,2r+e}
 \equiv0\pmod{p^3}.
$$
故 (13) 对 $j=r,r+1$ 仍成立；$h=0$ 时右边为零。由 $n+2<k$，应用 $K,L$ 所需至多第 $l+2\le r+1$ 个角系数确都已经付清。这里没有把一个尚未观测的高角系数假作原行。

先把 (13) 代入 $p^{-1}T^1$。再把 $T^1_{h-1,l+r}$ 中
$g_j$ 写成 $y^r\mathsf Sg_j$ 模 $p$。导数满足
$$
 y^{-r}(y^r\mathsf Sg)'=(\mathsf Sg)'+r\,y^{-1}\mathsf Sg.
$$
两个普通导数项消去；$K\mathsf Sg_{h-1}$ 的系数是
$-h+(h-1)=-1$，另一个 $K$ 项系数是
$-(h-1)^2+(h-1)(h-2)=-(h-1)$。留下恰好 (12) 的正号 $rL/y$ 项。

还须核 $T^2$ 消失。R205 的真实前缀论证给
$$
 \bar g_j\in y^{r+2}\mathbf F_p[[y]]\ (j\le q-2),\qquad
 \bar g_{q-1}\in y^{r+\min(s,2)}\mathbf F_p[[y]].
$$
在完整块 $h<q$，$T^2$ 所读最高下标是 $h-1\le q-2$，配合 (11) 后角 $l<r$ 全为零。在部分块 $h=q$，内部条件给 $l\le s-3<r-2$，同样消失。这也说明 (12) 的 Laurent 表达在所取系数上正则。证毕。

(12) 只依赖 $P\bmod p$。准确地说，它定义在
$$
 K_3(J,k)/pK_2(J,k)
 \simeq \operatorname{im}(K_3(J,k)\longrightarrow E_D/pE_D)
 \tag{14}
$$
上的线性行。此商是可提升到真实第三层的剩余源；不是任意 mod $p$ 前缀核。要由该行推出第四层源核旋转，还须加上实际下一层 $J$-像的零条件；仅知道此行在 (14) 上非零不等于已取得范数增益。

## 4. 第一内部行与真正的 $C$ 系数

记 $P_C,P_{A^2},P_{AC}$ 为原单项式系数。若 $k>r+2$，早期真实行给
$$
 P_A\in p^3O,\qquad P_{A^2}+v_0P_C\in p^3O.
$$
第 $r+2$ 行准确为
$$
 a[y^2]g_1+p[y^{r+2}]g_0\in p^3O.
$$
其中 $[y^2]g_1\equiv-v_0P_C\pmod{p^3}$，故
$$
 P_C\in pO,\qquad
 [y^{r+2}]g_0\equiv a v_0(P_C/p)\pmod{p^2}.
 \tag{15}
$$
又 $K_{-2}=-t_{1,C}/v_0$，因此 (12) 的第一内部行为
$$
 \frac{(J_r-J_r^\circ)(P)}{p^3}
 \equiv t_{1,C}(P_C/p)\pmod p.
 \tag{16}
$$
若 $k>r+3$，同一原前缀还给 $P_{AC}\in pO$，而下一行是
$$
 \frac{(J_{r+1}-J_{r+1}^\circ)(P)}{p^3}
 \equiv-2v_0t_{1,A}(P_C/p)+t_{1,C}(P_{AC}/p)\pmod p.
 \tag{17}
$$
这也可直接从 $p^2D_{t_1}P$ 的角 $0,1$ 系数读出。

所以当 $t_{1,C}$ 是单位时，第一内部行对全部真实 $K_3$ 消失，准确等价于
$$
 P_C\in p^2O\quad\text{对全部 }P\in K_3(J,k).
 \tag{18}
$$
若 $t_{1,C}\equiv0\pmod p$，(16) 自动为零，不能反推 (18)；若同时 $t_{1,A}$ 是单位，则 (17) 检测相同的 $P_C/p$。若 $t_1\in pO^2$，本篇全部内部第四层行为零，但这不取消最后两行或更高层其他方向。

## 5. 删去原 $C$ 列的循环商：完整而可计算的门

本节对任意整矩阵成立，允许完整行中有有理冗余。令 $J_0$ 为 $J$ 删去原 $C$ 列，$I=J(E_D)$、$I_0=J(E_D\cap\{P_C=0\})$。设非零 Smith 指数为 $s_i(J)$，并置
$$
 \mathcal L_N(J)=\sum_i (N-s_i(J))_+
 =\operatorname{length}_O((I+p^NO^k)/p^NO^k).
$$
则
$$
 \{P_C:P\in K_N(J,k)\}=p^{a_N}O,\qquad
 a_N=\mathcal L_N(J)-\mathcal L_N(J_0).
 \tag{19}
$$
证明是把 $C$ 系数映入真实循环商
$$
 (I+p^NO^k)/(I_0+p^NO^k).
$$
其生成元是原 $C$ 列，核正是左边的系数理想，长度即 (19)。

若 $r_t(J)=\#\{i:s_i(J)\le t\}$，亦有
$$
 a_N=\sum_{t=0}^{N-1}\{r_t(J)-r_t(J_0)\}.
 \tag{20}
$$
在 $J_0$ 的整 Smith 目标基中，把原 $C$ 列写成 $v=(v_i)$，相应指数记 $u_i$，未占的有理目标方向记 $u_i=\infty$，则更具体地
$$
 a_N=\max_i\bigl(\min(u_i,N)-v_p(v_i)\bigr)_+.
 \tag{21}
$$
于是 $0\le a_N\le N$、$a_{N+1}-a_N\in\{0,1\}$。

在本文实际情形，(15) 已付 $a_3\ge1$。当 $t_{1,C}$ 是单位时，第四层第 $r$ 行全部消失的准确门为
$$
 a_3\ge2.
 \tag{22}
$$
本文没有证明 (22)。这需要第二或第三个真实像层在删列比较中再贡献一次；只比较两个 mod $p$ rank 不够。

这里用全部完整行的 Smith 没有违反 R198 的 jump 警告：计算的是固定有限像商，不是把有冗余行的 minor gcd 当成真实消失旗标的累计值理想。

## 6. 大 $p$ 时真实 Hasse 方向的整次数降阶

现在加
$$
 r>2D,\qquad D\ge1.
 \tag{23}
$$
所以所有至 $2D$ 的实际行均在第零块。令 $t\in O^2$ 为原方向的 primitive 向量；若从 $t_1=p^\kappa t$ 提取此方向，后续应用 $D_{t_1}$ 必须保留 $p^\kappa$。

**定理 6.1（整源同构与真实 Schur）。**
存在显式整线性同构
$$
 E_D\ \simeq\ E_{D-1}\oplus O^{D+1},
 \qquad
 P\longmapsto\bigl(D_tP,\text{所选 }D+1\text{ 个实际低行}\bigr).
 \tag{24}
$$
所选行都不超过 $2D$。因此对每个 $k>2D$，同一固定整源变换及目标消元给
$$
 J_{<k}\ \sim_O\ I_{D+1}\oplus S_{k,D-1}.
 \tag{25}
$$
这准确保持所有 Smith、各有限精度像长度及此后真实前缀的值理想。

**构造与证明。**
若 $t_C\in O^\times$，取
$$
 X=C/t_C,\qquad Y=A-(t_A/t_C)C.
$$
则 $D_t=\partial_X$、$Y(w)=w+\cdots$，在
$O[Y]_{\le D}$ 上选行 $0,\ldots,D$，其矩阵整三角单位。

否则 $t_A$ 是单位，取
$$
 X=A/t_A,\qquad Y=C-(t_C/t_A)A.
$$
此时 $\bar Y(w)=v_0w^2+\cdots$，选行 $0,2,\ldots,2D$，其约化矩阵三角且对角 $v_0^j$，仍为单位矩阵。两组 $X,Y$ 都是原源的 $GL_2(O)$ 坐标。

对 $Q\in E_{D-1}$，逐 $X$ 积分并取 $X=0$ 常数为零，得整截面 $\mathcal I Q$。分母只有 $1,\ldots,D<p$。由所选低行的单位矩阵，存在唯一 $H_Q(Y)\in O[Y]_{\le D}$ 使
$$
 \mathcal R_D Q=\mathcal I Q-H_Q(Y)
$$
杀掉这 $D+1$ 个真实低行，且 $D_t\mathcal R_DQ=Q$。这给 (24) 的显式逆及整直和
$$
 E_D=\mathcal R_D(E_{D-1})\oplus O[Y]_{\le D}.
$$
在目标用已经位于每个 $k>2D$ 前缀中的这些单位 pivots 消元，即得 (25)，其中
$$
 S_{k,D-1}=J_{<k}\mathcal R_D
$$
在删去所选单位行后的剩余行上读取。

这个构造对 $k$ 一致；$k$ 增长只添同一 Schur 矩阵的新行。对 exact prefix 核，$D_t$ 是源范数等距的饱和注入。对 $K_N$，若已知真实低行在 $p^N$，则
$$
 P\in p^NE_D\quad\Longleftrightarrow\quad D_tP\in p^NE_{D-1}.
$$
最关键的限制是：$S_{k,D-1}$ 不是原来的 $J_{D-1}$。第二次降阶仍须证明新的单位块，不能免费重复 (25)。

第四层的原方向确只读降一次次数的 Hasse 源：由
$$
 D_t\mathcal E^j=(\mathcal E+1)^jD_t
$$
可把 (7) 第一行在 $h\ge2$ 时写成
$$
 T^1_{h,l}(P)=\frac{a^{h-1}}{(h-1)!}[y^l]
 (\mathcal E+1)^{h-2}(\mathcal E+h)D_{t_1}P(f,c).
 \tag{26}
$$
(24)–(25) 付清这个源运输；它们没有把任意 latent 轴系数宣布为已经观测的真实行。

## 7. 第一带改用 $z=A(w)$ 保持完整整像

这个更具体的变化使 §6 的 $\partial_C$ 方向完全成为固定图的 Hermite–Padé 矩阵。

设
$$
 z=A(w),\qquad \Phi(z)=C(A^{-1}(z))\in\mathbf Q[[z]].
$$
这里 $\Phi$ 是同一原有理 germ，与 $p$ 无关；它不同于 R196/R200 的整轴图 $\phi=c\circ f^{-1}$。定义
$$
 \widehat J_n(P)=p^{\lfloor n/r\rfloor}[z^n]P(z,\Phi(z)).
$$
输出换参矩阵为
$$
 J_n=\sum_{j=0}^n H_{nj}\widehat J_j,\qquad
 H_{nj}=p^{\lfloor n/r\rfloor-\lfloor j/r\rfloor}
             [w^n]A(w)^j.
 \tag{27}
$$
在整个所用第一带内 $H$ 是整单位下三角矩阵。事实上，由 (2)，指数项只用
$h\le\lfloor(n-j)/r\rfloor<p$，故
$$
 v_p([w^n]A(w)^j)\ge-\lfloor(n-j)/r\rfloor.
$$
而
$$
 \lfloor n/r\rfloor-\lfloor j/r\rfloor
 \ge\lfloor(n-j)/r\rfloor.
$$
于是 (27) 每个条目整，对角为一。其每一个完整前缀都是 $GL(O)$，因此不但 exact prefix 的首剩余系数等距，所有有限像、归一 Smith 和各有界源原像也准确相同。

这一步只在已经付清的第一带使用；没有把任意非整参数变化当作整目标变换。

## 8. 完全明确的真实 Hermite–Padé 余矩阵

在 (23) 下取 §6 的方向 $t=(0,1)$。在 $z=A(w)$ 输出中，原列
$1,A,\ldots,A^D$ 的低行 $0,\ldots,D$ 就是单位矩阵。对
$$
 i,j\ge0,\qquad i+j\le D-1
$$
取余源基
$$
 \mathcal R_{ij}(A,C)=
 \frac{A^iC^{j+1}-[A^i\Phi(A)^{j+1}]_{\le D}}{j+1}.
 \tag{28}
$$
系数整，因为至 $D<r$ 的图系数整，且 $j+1\le D<p$。它满足
$\partial_C\mathcal R_{ij}=A^iC^j$，并准确杀掉全部低 $0,\ldots,D$ 行。

因此 (25) 的剩余矩阵现在是显式的
$$
 \boxed{\displaystyle
 S_{n,(i,j)}
 =\frac{p^{\lfloor n/r\rfloor}}{j+1}
      [z^{\,n-i}]\Phi(z)^{j+1},
 \quad D<n<k,\quad i+j\le D-1.}
 \tag{29}
$$
它保持原次数，包含完整连续行；没有只选稀疏 h-block，也没有增加自由的角参数源。

原 $C$ 系数在 (28) 中恰是 $(i,j)=(0,0)$ 的坐标，原纯 $A$ 源没有 $C$ 系数。故若 $S_0$ 为 (29) 删去该常数余列，则
$$
 a_N(J,C)=\mathcal L_N(S)-\mathcal L_N(S_0).
 \tag{30}
$$
这把 (22) 变成同一个固定图函数的完全明确有限 Hermite–Padé 商，不再需要付额外 latent 坐标读取。

该常数余列代表的实际原源是
$$
 C-[\Phi(A)]_{\le D},
$$
其余列是图幂的相应高尾。第一带所有原 $C$ 列的 $p^N$ 归属问题，因而可由 (29)–(30) 直接核算。


## 9. 完整 Hasse 向量的全精度整变换

本节保持同一个原 $P\in E_D$，只把其有限个真实 Hasse 偏导同时记录；不把这些偏导当成互相独立的新源。

比较曲线另以自身的 $A^\circ$ 为输出参数，记全图为
$\Phi^\circ$。在共同的形式变量 $z$ 中令
$\delta=\Phi-\Phi^\circ$。第一带有准确的加权界
$$
 p^{\lfloor n/r\rfloor}[z^n]\delta\in p^2O,\qquad
 \operatorname{ord}_z\delta\ge r.
 \tag{31}
$$

这里要付清输出逆函数，不能仅从原 $A,C$ 两个差的界直接断言 (31)。取 $\pi^r=p$。由 (2) 及指数项的阶乘都是单位，
$$
 A(\pi z)/\pi,\ C(\pi z)/\pi^2,\
 A^\circ(\pi z)/\pi,\ C^\circ(\pi z)/\pi^2
$$
在所需截断内均整，且第一个和第三个级数首项为 $z$。由 $v_1=pt_1$ 及后续中央轴系数整，
$$
 (A-A^\circ)(\pi z)/\pi\in\pi^{2r-1}O_\pi[[z]],\qquad
 (C-C^\circ)(\pi z)/\pi^2\in\pi^{2r-2}O_\pi[[z]].
$$
首项为 $z$ 的整形式级数取逆，在每一有限截断都保持同余精度。因此两个归一逆函数之差在 $\pi^{2r-1}$ 中。再作整复合，得
$$
 \delta(\pi z)/\pi^2\in\pi^{2r-2}O_\pi[[z]].
$$
原系数的 $p$-赋值为整数，故这恰推出 (31)。

记
$$
 F_j=(\partial_C^{[j]}P)(z,\Phi(z)),\qquad
 F_j^\circ=(\partial_C^{[j]}P)(z,\Phi^\circ(z)),
 \quad 0\le j\le D.
$$
Hasse Taylor 公式准确给
$$
 F_j=\sum_{t=0}^{D-j}\binom{j+t}{j}\delta^t F_{j+t}^\circ .
 \tag{32}
$$
对每个分量使用同一行归一 $p^{\lfloor n/r\rfloor}$。乘 $\delta^t$ 的目标矩阵条目为
$$
 p^{\lfloor n/r\rfloor-\lfloor m/r\rfloor}
      [z^{n-m}]\delta^t\in p^{2t}O,
 \tag{33}
$$
且只有 $n-m\ge rt$ 才可能非零。于是完整有限 Hasse 向量的目标变换是整单位上三角，其第 $t$ 个 Hasse 偏对角在 $p^{2t}$ 中，输出只读取过去的行。对任意同一完整前缀，这准确保持联合像的全部 Smith 与所有有限精度源原像。

回原 $w$ 输出时，分别复合 §7 的两个整单位目标变换，结论仍是完整 Hasse 向量的整等价；不额外宣称其原 $w$ 对角块同余于单位矩阵模 $p^2$。

标量第零分量的像并不由这个向量上三角变换保持，因为 (32) 的第零行确实混入较高 Hasse 分量。该标量投影仍是实际 Schur 问题。这是全精度联合接口，不是严格的标量预算。

## 10. 同一实际大素数样本的完整校准

根端已经执行纯 JavaScript BigInt 有理证书
[check-deleted-c-finite-image.js](../scripts/check-deleted-c-finite-image.js)，完整输出保存在
[check-deleted-c-finite-image.json](../scripts/check-deleted-c-finite-image.json)。
它逐项重建 R162 的原 $P,Q,W$ 源，并先精确复现既有
$D=4,p=19$ 的全部 15 个 raw 饱和值
$$
 0^7,\ (-1)^7,\ -2.
$$
随后只对同一个 $D=4,p=43,r=11,N=3$ 样本取两个相邻完整前缀。所用有限阶 $s\leftrightarrow w$ 变换整且首项单位，因此这些 finite-image 正是本文的真实归一像。

| 前缀长度 $k$ | $J$ 的非零 Smith 指数 | 删原 $C$ 列 | $\mathcal L_3(J)$ | $\mathcal L_3(J_0)$ | $a_3$ |
| --- | --- | --- | ---: | ---: | ---: |
| 14 | $0^{12},1^2$ | $0^{11},1^3$ | 40 | 39 | 1 |
| 15 | $0^{13},1^2$ | $0^{12},1^2$ | 43 | 40 | 3 |

在 $k=14$ 时，实际 primitive 原整多项式见证为
$$
 \begin{split}
 P={}&43C+946A^2-28836AC+1057C^2-19191A^3\\
 &-6801A^2C-24896AC^2+32115C^3+23103A^4\\
 &-18044A^3C+852A^2C^2+1169AC^3+969C^4.
 \end{split}
 \tag{34}
$$
证书直接验证全部 14 个归一前缀值模 $43^3=79507$ 为零，而
$P_C=43$；例如 $C^2$ 系数模 $43$ 是单位，故 $P$ primitive。它与 (15) 合起来准确认证 $a_3=1$。

这里 $r=11>2D=8$，所以这个实际样本排除“仅凭大素数次数条件就有 $a_3\ge2$”的说法。加一条真实连续行后 $a_3$ 变成 3，也说明必须用完整前缀。没有证明或假设 $p=43$ 满足双完整中央零；因此它不是对“双中央零加上其他已付条件”的反例，也不是已满足本文条件性第四层比较的样本。


## 11. 已付款与仍未付款的区别

本篇已证明：

1. 第四层差在全部真实内部行 $n+2<k$ 上的完整公式 (12)，包括跨角 $r,r+1$ 的补读；没有丢掉下一 $p$ 位。
2. 第一内部行所需的 $P_C/p$ 是真实删列循环商 (19)，当方向非零时给准确检测门，而不是一个自由轴变量。
3. 大 $p$ 原源的整 Hasse–Schur 分解 (24)–(25)，以及第一带真实整输出变换 (27)。
4. 同一原 $E_D$ 的显式 Hermite–Padé 矩阵 (29)，全部 finite-image 与后续 prefix 范数没有单位损失。
5. 完整真实 Hasse 向量的全精度整目标变换 (32)，以及同一实际样本的删列商与 primitive 见证 (34)。

尚未证明的是：双完整中央零会使 (30) 在所需范围满足 $a_3\ge2$，或者使全部 Schur 像产生达到严格门的统一收益。即使某个内部方向变化已显出，仍须保留实际下一像层；不能由源核方向不同推出 Smith、值理想或全局斜率改善。R204 已给过相反的实际校准。

下一步的具体对象是 (29) 的全部连续前缀和删常数余列的有限像差，并将完整中央条件加入其真实 Schur 补。只扩大首带方向定位、把新 $S$ 再当成原 $J_{D-1}$、或者把几条轴关系独立作用于每个源 summand，都不支付这个问题。
