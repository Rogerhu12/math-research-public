# R271 附录：单链目标的全部交织与交换子代数的实际有界表示

日期：2026-11-27（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127 / stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

继续[原同源迹类构造](R271-appendix-actual-directional-intertwiner-exclusion-and-trace-class-rosenblum-solutions.md)和[真闭单链限制](R271-appendix-proper-single-chain-restriction-and-common-trace-class-intertwiner-range.md)。固定原两型之一 $T=T_N,T_Y$，原 $B,S=B^*$，以及同一个规范右逆 $G$。置
$$
u_n=G^ne_0,\qquad U=\overline{\operatorname{span}}\{u_n:n\ge0\},\qquad T_U=T|_U.
$$
已付
$$
Tu_n=u_{n-1}\ (n\ge1),\quad Tu_0=0,\quad
\langle u_n,e_0\rangle=\mathbf1_{\{n=0\}},
\quad \|u_n\|\le e^{A_\lambda n^3},
$$
$$
\ker T_U^{r}=\operatorname{span}\{u_0,\ldots,u_{r-1}\},\qquad
U\cap\ker T=\mathbb Ce_0,\qquad \{0\}\ne U\ne H.
\tag{0.1}
$$
所有 $L_y=\sum_{n\ge0}u_n\otimes S^ny$ 是实际迹类 $H\to U$，满足
$$
T_UL_y=L_yB,\qquad L_y^*e_0=y,\qquad
\|L_y\|_1\le C_{\rm tr}\|y\|,\qquad
C_{\rm tr}:=\sum_{n\ge0}\|u_n\|\|B^n\|<\infty.
\tag{0.2}
$$
特别 $L_{e_0}$ 单射且像在 $U$ 稠密。内积对第一变量线性，$(u\otimes v)x=\langle x,v\rangle u$。

## 1. 目标 U 上的全部有界交织已经穷尽

**定理 1。**
$$
\boxed{\{Z\in B(H,U):T_UZ=ZB\}=\{L_y:y\in H\},\qquad y=Z^*e_0.}
\tag{1.1}
$$
因此每个此方向的有界交织自动为迹类，且
$$
\|Z^*e_0\|\le\|Z\|\le\|Z\|_1\le C_{\rm tr}\|Z^*e_0\|.
\tag{1.2}
$$

**证明。** 令 $\beta_0=1$、$\beta_k=\prod_{\nu=1}^k\alpha_{v_2(\nu)}$。
$B^{k+1}e_k=0$，故
$$
Ze_k\in\ker T_U^{k+1}=\operatorname{span}\{u_0,\ldots,u_k\}.
$$
在该有限链中，$P_0T_U^n$ 准确读出 $u_n$ 系数，其中 $P_0=e_0\otimes e_0$。由交织式，该系数为
$$
\langle ZB^ne_k,e_0\rangle
=\frac{\beta_k}{\beta_{k-n}}\langle e_{k-n},y\rangle
=\frac{\beta_k}{\beta_{k-n}}\overline{y_{k-n}}
\quad(0\le n\le k).
$$
所以 $Ze_k=L_y e_k$。有限整数支撑稠密且两算子有界，得到 $Z=L_y$。(1.2) 由 (0.2) 成立。证毕。

这里仅对目标 $U$ 作完整分类。没有把它升级成任意 $H\to H$ 的交织分类；全 $T$ 另有无限维核。

## 2. 交换子代数的同一有界、单射表示

记
$$
\mathcal C_U=\{D\in B(U):DT_U=T_UD\}.
$$
对 $D\in\mathcal C_U$ 置
$$
c_n(D)=\langle Du_n,e_0\rangle.
$$
由 (0.1)
$$
|c_n(D)|\le\|D\|e^{A_\lambda n^3}.
\tag{2.1}
$$
所以原四次幂衰减保证
$$
\boxed{
\rho(D):=\sum_{n=0}^\infty c_n(D)B^n
}
\tag{2.2}
$$
在算子范数中绝对收敛，而且
$$
\|\rho(D)\|\le C_{\rm tr}\|D\|.
\tag{2.3}
$$
它位于 $B$ 的范数闭多项式代数中，特别与 $B$ 交换。式 (2.1) 控制的是普通 $B^n$ 系数，未混用 dyadic 归一化系数。

对每个同一来源 $y\in H$，实际有
$$
\boxed{D L_y=L_y\rho(D).}
\tag{2.4}
$$
确切地，$DL_y$ 仍是目标 $U$ 的交织。其真空行由实际收敛级数给
$$
(DL_y)^*e_0
=L_y^*D^*e_0
=\sum_{n\ge0}\langle D^*e_0,u_n\rangle S^ny
=\rho(D)^*y.
$$
另一方面，凡 $C$ 与 $B$ 交换，(0.2) 的同一收敛级数给
$$
L_yC=L_{C^*y}.
\tag{2.5}
$$
定理 1 的唯一性遂给 (2.4)。

此外
$$
\boxed{\rho:\mathcal C_U\longrightarrow\{B\}'
\text{ 是有界、单射、保单位的代数同态},\qquad
\rho(T_U)=B.}
\tag{2.6}
$$
线性与保单位直接由系数可见。由 (2.4)，
$$
D_1D_2L_{e_0}=L_{e_0}\rho(D_1)\rho(D_2).
$$
再用 $L_{e_0}$ 单射，得到乘法性。若 $\rho(D)=0$，则 $DL_{e_0}=0$；其像稠密给 $D=0$。最后
$\langle T_Uu_n,e_0\rangle=\mathbf1_{\{n=1\}}$，故 $\rho(T_U)=B$。

一个直接的有界演算后果是
$$
\boxed{\|p(B)\|\le C_{\rm tr}\|p(T_U)\|}
\tag{2.7}
$$
对所有复多项式 $p$ 成立。没有证明 $\rho$ 满射、反向范数界或逆封闭。

## 3. 非零交换子的真实稠密像

若 $D\ne0$，(2.6) 保证 $\rho(D)\ne0$。令 $k$ 是 (2.2) 的第一个非零系数，则
$$
\rho(D)=B^k V,\qquad
V=\sum_{n\ge0}c_{n+k}(D)B^n.
\tag{3.1}
$$
同一三次/四次估计保证 $V$ 在范数中绝对收敛。其常项 $c_k(D)\ne0$。

为支付 $V$ 的真实可逆性，$V-c_kI$ 是零常项 $B$ 多项式的范数极限。那些多项式均拟幂零，并与极限交换；交换算子的谱半径次可加性给
$$
r(V-c_kI)\le\|V-c_kI-p_N(B)\|\longrightarrow0.
$$
故 $V$ 可逆。又 $B^k$ 像稠密，因 $S^k$ 单射。因此 $\rho(D)$ 像稠密。由
$DL_{e_0}=L_{e_0}\rho(D)$ 及 $L_{e_0}$ 像稠密，得到
$$
\boxed{\overline{\operatorname{Ran}D}=U\quad(0\ne D\in\mathcal C_U).}
\tag{3.2}
$$
特别 $\mathcal C_U$ 无非平凡幂等元：非零有界幂等元的像既闭又稠密，只能为 $U$。这不排除 $T_U$ 的已知不变旗，也不是无不变子空间断言。

## 4. 同一个真实最大图来源的准确接口

固定 $y,f\in H$ 满足原式
$$
T^*y=Sf.
\tag{4.1}
$$
原 $S$ 与 $T^*$ 交换。利用 (2.5)，并保同一 $y,f$，得到
$$
\boxed{L_yT=L_{T^*y}=L_{Sf}=L_fB=T_UL_f.}
\tag{4.2}
$$
又 $\ker L_y$ 是 $B$ 不变子空间，而原 $T$ 属于 $B$ 的范数闭多项式代数，所以它也被 $T$ 保持。由 (4.2) 和 (0.1)，
$$
\boxed{L_f(\ker L_y)\subset\mathbb Ce_0.}
\tag{4.3}
$$
于是
$$
L_f(\ker L_y)=0
\iff
f\in\overline{\operatorname{span}}\{S^ny:n\ge0\}.
\tag{4.4}
$$
这里使用前稿 $\ker L_y=(\overline{\operatorname{span}}\{S^ny\})^\perp$，并由 $P_0L_f=e_0\otimes f$ 读出 (4.3) 的准确真空残量。共同闭包像 $U$ 本身不消去这一残量。

事实上，若 $y\ne0$，不存在有界 $D:U\to U$ 满足
$$
L_f=DL_y.
\tag{4.5}
$$
若它存在，$\operatorname{Ran}L_y$ 在 $U$ 稠密，且两 $L$ 都交织，故
$$
(DT_U-T_UD)L_y=DL_yB-T_UL_f=0,
$$
即 $D\in\mathcal C_U$。由 (2.4)–(2.5) 和真空行唯一性，
$f=\rho(D)^*y$。代入 (4.1) 得
$$
(T^*-S\rho(D)^*)y=0.
\tag{4.6}
$$

原正权前移 $S$ 的每个非零交换子均单射。给出所需的简单证明：若 $A$ 与 $S$ 交换，则
$Ae_n=\beta_n^{-1}S^nAe_0$。若 $A\ne0$，$Ae_0$ 有最小非零坐标 $j$；任何非零 $x$ 有最小非零坐标 $k$，于是 $Ax$ 的第 $j+k$ 坐标是
$$
\frac{\beta_{j+k}}{\beta_j\beta_k}(Ae_0)_j x_k\ne0.
$$
这是有限坐标计算，对一般 $x$ 由有界性成立。因此 (4.6) 迫
$T^*=S\rho(D)^*$。这却使 $T^*e_0\in\operatorname{Ran}S$，与[原形式除法闭关系](R271-appendix-actual-formal-division-closed-relation-and-two-range-cores.md) §4 已证
$$
\mathcal D(G_0^*)=\{v:T^*v\in\operatorname{Ran}S\}\subset e_0^\perp
$$
矛盾。故 (4.5) 不成立。

最后若该同源对还满足真正第二 Green 式
$$
By+Tf=0,
$$
它目前准确给出
$$
P_0(L_yS+L_fT^*)=e_0\otimes(By+Tf)=0.
\tag{4.7}
$$
不能由 (4.7) 宣称整个算子为零。若 $Q=L_yS+L_fT^*$，直接计算的全交换子为
$$
T_UQ-QB=L_y[B,S]+L_f[B,T^*].
\tag{4.8}
$$
这里完整保留两项原交换子。

本稿没有证明 (4.4) 对真实 Green 来源自动成立，没有把同来源的两有界迹类算子变成有界商，也没有证明 $U$ 对 $B$ 不变。真正 $W$ 的原费用、两道范围核心和 $N=M$ 继续保留。新增的是目标 $U$ 的全部交织分类、有界忠实表示 $\rho$、同一个来源的准确真空残量，以及其不能由有界后因子免费消除的事实。
