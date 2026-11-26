# R150 附录：二重加单点 H 的退化 Gram 本质六维截面全部为空

日期：2026-11-26（UTC）。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：已证明。** 原完整临界点若 rankH3 的唯一物理支撑为 $2+1$ 型、rankV2，且原 K 在 $\operatorname{Ran}H$ 上退化，则 $\dim\operatorname{ess}(T_3)\le5$。两种 V 支撑、零 Hp、非零 Hp、全部特殊自接触及无穷远均包含。没有新增计算门。

## 1. 原规范、完整梯度与全部退化类型

仍用原非退化六维 K、$p=Ky$、$F=yKy/2$、$T_3=y^3-6yH+4V$。反设本质维数六，则原 $y,H,V$ 的支撑之和为整个六空间。rankV2 的内均值层已经分类为 $T_3=0$；本支亦可直接使用[外于 V 的均值支撑等式](R150-appendix-rank-two-third-cumulant-outside-range-mean-essential-support-equality.md)。所以以下六列组成原空间的一组基。

把 H 的二重点值、一阶 Taylor 列记为 $z_0,z_1$，孤立物理值记为 w。吸收二重点的值权到一阶列，并将孤立非零权吸收为平方，可完整规范
$$
H=h(z_0z_1+z_1z_0)+\frac12w^2,\qquad h\ne0.
\tag{1.1}
$$
具体地，原 $\alpha u_0^2+\beta(u_0u_1+u_1u_0)+\gamma v^2$ 中 $\beta\gamma\ne0$；取 $h=\beta$、$z_0=u_0$、$z_1=u_1+\alpha u_0/(2\beta)$、$w=\sqrt{2\gamma}\,v$ 即得 (1.1)。一阶列改变是合法的局部非零平凡化，覆盖有限与无穷远。

令
$$
b=K(z_1,z_1),\qquad g=K(z_0,w),\qquad c=K(z_1,w).
$$
物理恒等式给
$$
K_R=
\begin{pmatrix}
0&0&g\\
0&b&c\\
g&c&0
\end{pmatrix},
\qquad
\det K_R=-bg^2.
\tag{1.2}
$$
因此退化 Gram 准确分成 $g=0$ 或 $b=0$，无其他类型。若 $g=b=c=0$，R 是全等向的原 $2+1$ 长度三 jet 空间，已经由[完整物理全等向分类](R150-appendix-classification-of-isotropic-length-three-curve-jets.md)排除，包括全部射影边界。

记 $A=HK|_R$。在 (1.1) 的基中
$$
A=
\begin{pmatrix}
0&hb&hc\\
0&0&hg\\
g/2&c/2&0
\end{pmatrix},
\quad
\tau_2=2hgc,\quad
\tau_3=\frac32h^2bg^2.
\tag{1.3}
$$
令 $\mathfrak b=p^{\mathsf T}Hp$。完整 mean 的 Gaussian 部分由六列独立而分别为零：
$$
(2HK-FI)Hp=0,\qquad F^2-2\mathfrak b+2\tau_2=0.
\tag{1.4}
$$
完整最高梯度与加权 Euler 另给
$$
F^3+6F\tau_2-8\tau_3=8V^{\mathsf T}J_3V.
\tag{1.5}
$$
这里的完整 Gaussian 多项式原为
$F^3-6F\mathfrak b+6F\tau_2+12p^{\mathsf T}HKHp-8\tau_3$；
由 (1.4) 消项后才得到 (1.5)，没有遗漏 V 贡献。

所有后续 H 式均使用原
$$
N=Fyy^{\mathsf T}-2FH
-2\bigl(y(Hp)^{\mathsf T}+(Hp)y^{\mathsf T}\bigr)
+4HKH+4V_p,
\qquad k_x^{\mathsf T}Nk_x=0,
\tag{1.6}
$$
其中 $k_x=Kx$，x 遍历实际物理曲线。绝不将最后的极线零式增强为 $N=0$。最高式仍为
$$
p(x)^3-6p(x)H(k_x,k_x)+4V(k_x,k_x,k_x)=0.
\tag{1.7}
$$

V 约化时取 $V=(u^3+v^3)/2$，$e=uKv$，则 (1.5) 右边为 $4e^3$。最高式与两个 V mean 系数给 $p(u)^3=p(v)^3=e^3$；若 $e\ne0$，可作保 V 的单位根尺度使
$$
p(u)=p(v)=e,\qquad H(Ku,Ku)=H(Kv,Kv)=e^2/2.
\tag{1.8}
$$
若 $e=0$，则两个均值皆零且 $V_p=0$。

V 非约化时完整写为
$$
V=\alpha u^3+\beta\operatorname{Sym}_{\Sigma}(u^2v),
\qquad \beta\ne0,
$$
其中 v 为同一物理源的一阶 jet，允许加 u 倍数。完整原系数给
$$
p(u)=0,\quad H(Ku,Ku)=H(Ku,Kv)=0,\quad
V_p=\beta\,p(v)u^2,\quad V^{\mathsf T}J_3V=0.
\tag{1.9}
$$
物理上 $uKu=uKv=0$。在六维反设中，u 不能与任一 H 物理值重合，否则六列不独立。

## 2. 一个已完全显式的特殊源事实

$b=0$ 的二重点源准确是 $0,2,-6,\infty$；局部参数及非零平凡化不改变这张表。以下直接列出同一原核的极线：
$$
k_0(t)=t^4(5-t),
$$
$$
k_2(t)=-(t-2)^3(3t^2-17t+6),
$$
$$
k_{-6}(t)=(t+6)^3(5t^2+65t+66),
$$
$$
k_\infty(a,b)=-a^4(a+b).
\tag{2.1}
$$
两个二次剩余式的判别式分别为 $217$、$2905$；在本源的值分别为 $-16$、$-144$。前三个有限多项式均为完整五次式，所以无额外无穷远根。由此有准确结论：

**上述每个特殊物理值的极线，在所有不同物理点处只能有简单零点。** 因而它不可能同时正交于某个不同点的值和一阶 jet。后文只使用这一显示事实，不把一般极线的二重异点接触排除在外。

## 3. $g=0$ 的全部 V 类型排除

此时 A 幂零，$\tau_2=\tau_3=0$。若 $F\ne0$，(1.4) 先迫 $Hp=0$，再迫 $F^2=0$，矛盾。因此
$$
F=0,\qquad \mathfrak b=0,\qquad AHp=0.
$$
写 $p_0=p(z_0),p_1=p(z_1),p_w=p(w)$。直接代入 (1.3)：
$$
AHp=h\left(hbp_0+\frac c2p_w\right)z_0
+\frac{hc}{2}p_0w.
$$
若 $c\ne0$，得到 $p_0=p_w=0$；若 $c=0$，则 §1 已排除的全等向情形之外必有 $b\ne0$，先得 $p_0=0$，再由 $\mathfrak b=p_w^2/2=0$ 得 $p_w=0$。所以始终
$$
Hp=hp_1z_0.
\tag{3.1}
$$

约化 V 由 (1.5) 得 $e=0$，故 $V_p=0$。对非约化 V，假设 $t=p(v)\ne0$，并记
$$
C_0=K(z_0,u),\ C_1=K(z_1,u),\ C_w=K(w,u),
$$
以 D 表示 v 的对应配对。完整 N 在 $z_0$ 的值给 $C_0=0$；(1.9) 的首式再给 $C_w=0$。若 $C_1=0$，u 正交于全部六列基，违反 K 非退化，所以 $C_1\ne0$。(1.9) 的混合式于是迫 $D_0=0$。但现在 $z_0$ 正交于 H 三列、y、u、v，也是原六维 K 的非零根向量，矛盾。故非约化情形亦有 $t=0,V_p=0$。

完整 (1.6) 现在准确因式化为
$$
N=z_0\otimes W+W\otimes z_0,\qquad
W=-2hp_1y+2h^2bz_0+2hcw.
\tag{3.2}
$$
原 H 极线条件是 $k_{z_0}k_W=0$。K 可逆且 $z_0\ne0$，多项式整环性迫 $W=0$。六列独立于是迫 $p_1=b=c=0$，而 $b=c=0$ 与 §1 的物理全等向排除矛盾。故 $g=0$ 整块为空。

## 4. $b=0,\ g\ne0,\ c=0$ 的幂零型排除

A 仍幂零，所以仍有 $F=\mathfrak b=0,AHp=0$。直接代入给
$$
p_1=p_w=0,\qquad Hp=hp_0z_1.
$$
约化 V 仍由 (1.5) 得 $e=0,V_p=0$。

对非约化 V，假设 $t=p(v)\ne0$。完整 N 在物理值 w 处先给 $C_w=0$，而 (1.9) 给 $C_0C_1=0$。二者不能同时为零，否则 u 正交于整个六列基。

若 $C_1=0,C_0\ne0$，混合式给 $D_1=0$；于是 $z_1$ 正交于 H 三列、y、u、v，是原 K 的非零根向量，矛盾。

若 $C_0=0,C_1\ne0$，混合式给 $D_0=0$。这意味着特殊 H 物理值 $z_0$ 的极线同时在不同物理点 u 的值和一阶 jet 为零，违反 §2 的全部异点根简单性。故此处也有 $V_p=0$。

完整 H 张量现在是
$$
N=z_1\otimes W+W\otimes z_1,\qquad
W=-2hp_0y+2hgw.
$$
原极线乘积为零迫 $W=0$，与 $hg\ne0$ 及 y、w 独立矛盾。此幂零型全部排除。

## 5. $b=0,\ gc\ne0$ 的零 F 型排除

置 $\kappa=hgc\ne0$。此时 A 的特征多项式为
$$
\lambda(\lambda^2-\kappa),\qquad
\tau_2=2\kappa,\quad\tau_3=0.
\tag{5.1}
$$
先设 $F=0$。由 (1.4) 直接得
$$
p_w=0,\quad gp_1+cp_0=0,\quad
2hp_0p_1=2\kappa.
$$
定义
$$
L=cz_0+gz_1,\qquad r=cz_0-gz_1.
$$
于是
$$
Hp=\lambda r,\qquad \lambda^2=-h^2,
$$
$$
p_0=-\lambda g/h,\qquad p_1=\lambda c/h.
\tag{5.2}
$$
特别 $\lambda\ne0$。四空间 $E=\operatorname{span}(L,w,r,y)$ 非退化：唯一非零的基配对为
$$
K(L,w)=2gc,\qquad K(r,y)=-2\lambda gc/h.
\tag{5.3}
$$
四列各自平方为零，其他交叉项为零。故其正交补 M 是非退化二维空间。

约化 V 由 (1.5) 得 $e=0$、$p(u)=p(v)=0$、$V_p=0$。非约化 V 若 $t=p(v)\ne0$，完整 N 在 $z_0$ 处给 $C_0=0$，(1.9) 给 $C_w=0$。原六维非退化迫 $C_1\ne0$，混合式再迫 $D_0=0$，又违反 §2 的特殊极线异点简单性。所以所有 V 类型均满足
$$
p(u)=p(v)=0,\qquad V_p=0.
\tag{5.4}
$$

此时
$$
N=-2\lambda(y\otimes r+r\otimes y)
+2h(L\otimes w+w\otimes L).
\tag{5.5}
$$
对任意 $p(x)=0$ 的 x，原 N 极线值因此给 $K(L,x)K(w,x)=0$。

若 V 约化，此式分别应用到 u、v；而最高式在物理点 w 处给
$$
K(w,u)^3+K(w,v)^3=0.
$$
所以这两个 w 配对要么均为零，要么均非零；后一情形迫两个 L 配对均为零。两种情形都给
$$
K(L,u)K(w,v)+K(w,u)K(L,v)=0.
\tag{5.6}
$$
若 V 非约化，(5.6) 则直接来自同一原 N 恒等式在其物理源的一阶 Taylor 系数，因 (5.4) 消去了两个 y 配对。

由 (5.3)，当 $p(x)=p(z)=0$ 时，E 上投影的配对为
$$
K(x_E,z_E)=
\frac{K(L,x)K(w,z)+K(w,x)K(L,z)}{2gc}.
$$
所以 $K(u_E,u_E)=K(u_E,v_E)=0$。物理上 $uKu=uKv=0$，故
$$
K(u_M,u_M)=K(u_M,v_M)=0.
$$
但六列基迫 $u_M,v_M$ 在 M 中独立。非退化二维对称空间中，一个非零等向向量的正交补恰为其自身直线，不可能包含第二个独立向量。矛盾。此论证对非约化 v 不需要假定 $vKv=0$。

## 6. $b=0,\ gcF\ne0$ 时非约化 V 不可能

若 $Hp=0$，(1.4) 给 $F^2=-4\kappa$，因此 (1.5) 左边为
$$
F^3+12F\kappa=-2F^3\ne0.
$$
若 $Hp\ne0$，(5.1) 与 (1.4) 给 $F^2=4\kappa$，而同一左边为 $4F^3\ne0$。非约化 V 的 (1.5) 右边却为零，所以两种情况皆被排除。

从此 V 必约化，且 e 非零，可使用完整规范 (1.8)。只余下一节的两个 Hp 分支。

## 7. 零 Hp 由原一阶系数直接排除

现在 $Hp=0$，所以 $p_0=p_1=p_w=0$，并有
$$
F^2=-4\kappa,\qquad e^3=-F^3/2.
$$
最高式在二重点值处的常数、一次系数分别给
$$
C_0^3+D_0^3=0,\qquad
C_0^2C_1+D_0^2D_1=0.
\tag{7.1}
$$
完整 N 在相同实际物理 jet 的常数、一次系数分别给
$$
2e(C_0^2+D_0^2)=Fg^2,\qquad
2e(C_0C_1+D_0D_1)=Fgc.
\tag{7.2}
$$
这里 $H(Kz_0,Kz_0)=g^2/2$、$H(Kz_0,Kz_1)=gc/2$，而两个 $HKH$ 配对均为零，故 (7.2) 保留全部原项。

$Fg^2\ne0$ 与 (7.1) 迫 $C_0D_0\ne0$。写 $D_0=-\zeta C_0$，$\zeta^3=1$。一次最高式给 $D_1=-\zeta C_1$；比较 (7.2) 两式得到
$$
C_1=(c/g)C_0,\qquad D_1=(c/g)D_0.
$$
因此原非零 H Gram 核向量 $r=cz_0-gz_1$ 同时正交于 u、v。它也正交于 H 三列及 y，故正交于全部六列基，违反原 K 非退化。零 Hp 型为空。

## 8. 非零 Hp 的原常数与一次矩迫使 V 值等于 H 孤立值

现在 $Hp\ne0$。由前节的谱式和完整 Gaussian 系数，
$$
F^2=4hgc,\qquad p_w^2=F^2,\qquad
p_0=gp_w/F,\quad p_1=cp_w/F,\qquad e^3=F^3.
$$
必要时作原加权尺度 $y\mapsto-y,H\mapsto H,V\mapsto-V$，可设
$$
p_0=g,\qquad p_1=c,\qquad p_w=F.
\tag{8.1}
$$
该尺度保持临界性；同时取 u、v 的负代表保持 (1.8)，所以没有丢掉符号支。令 $\omega=e/F$，$\omega^3=1$。

原最高及 N 在 $z_0$ 的常数项为
$$
C_0^3+D_0^3=g^3,\qquad
C_0^2+D_0^2=Fg^2/e.
$$
它们的一次项为
$$
C_0^2C_1+D_0^2D_1=g^2c,\qquad
C_0C_1+D_0D_1=Fgc/e.
$$
定义
$$
C_0=\omega gR,\quad D_0=\omega gS,\quad
C_1=\omega cR_1,\quad D_1=\omega cS_1.
$$
准确得到
$$
R^2+S^2=R^3+S^3=1,
$$
$$
RR_1+SS_1=R^2R_1+S^2S_1=1.
\tag{8.2}
$$
$R=S$ 不可能：前两式将迫 $R=1$ 又迫 $2=1$。若 $RS\ne0$，后两式的系数行列式 $RS(S-R)$ 非零，而 $(R,S)$ 已是其一个解，故 $R_1=R,S_1=S$。于是 r 又正交于全部六列基，矛盾。

所以 $RS=0$。交换 u、v 后可设 $S=0,R=1$；(8.2) 再给 $R_1=1$，即
$$
C_0=\omega g,\quad C_1=\omega c,\quad D_0=0.
\tag{8.3}
$$
完整 V mean 式 (1.8) 给
$$
2hC_0C_1+C_w^2/2=e^2/2.
$$
由 $4hgc=F^2$，前一项已经是 $e^2/2$，故 $C_w=0$。最高式与 N 在孤立物理点 w 的值则给
$$
D_w^3=F^3,\qquad D_w^2=F^3/e.
$$
因为 $F\ne0$、$\omega^3=1$，这两式准确迫
$$
D_w=\omega F.
\tag{8.4}
$$

最后将完整 N 极线式评价在物理值 u。此时
$$
H(Ku,Ku)=e^2/2,\qquad
H(p,Ku)=\omega F^2/2,\qquad
(HKH)(Ku,Ku)=0.
$$
全部项代回 (1.6) 得
$$
-2e\omega F^2+2e^3=0,
$$
即 $\omega^2(\omega-1)F^3=0$。所以 $\omega=1$。

由 (8.1)、(8.3)—(8.4)，非零向量 $u-w$ 对 H 三列的配对为零；它对 y 的配对为 $e-p_w=F-F=0$，对 u 的配对为 $uKu-uKw=0$，对 v 的配对为 $e-D_w=F-F=0$。因此 $u-w$ 正交于全部六列基，原 K 非退化迫 $u=w$，与六列独立矛盾。非零 Hp 型也为空。

## 9. 完整范围与准确剩余

(1.2) 的所有退化 Gram 分支已逐一排除：$g=0$；$b=0,g\ne0,c=0$；$b=0,gc\ne0$ 的全部 F、Hp、V 类型。因此
$$
\boxed{
\operatorname{rank}H=3,\quad H\text{ 为 }2+1\text{ 物理支撑},
\quad K|_{\operatorname{Ran}H}\text{ 退化},\quad
\operatorname{rank}V=2
\ \Longrightarrow\ 
\dim\operatorname{ess}(T_3)\le5.
}
$$
所有使用 Gram 根向量的矛盾都明确检验了它与原六列基的全部配对；没有把 H 子空间退化误作原整个 K 退化。所有除法均已先证明其分母非零，特殊物理源及无穷远由 §2 完整覆盖。

因此 $2+1$ 型 H 的本质六维反设只余 $bg\ne0$ 的非退化 Gram。本文不关闭这个剩余型、本质四五维、更高秩层或 ISP 的完成标准。


后续[非约化V的完整排除](R150-appendix-rank-three-double-plus-single-second-cumulant-nonreduced-third-cumulant-essential-six-exclusion.md)已将所有二重jet V一并关闭，并独立排除非退化H中的全部F0及约化V的e0；本型ess6只余bgF e均非零的约化V。
