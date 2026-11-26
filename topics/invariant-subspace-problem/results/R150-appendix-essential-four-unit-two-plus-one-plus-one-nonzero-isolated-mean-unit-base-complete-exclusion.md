# R150 附录：单位211非零均值的整个单位基点均值图为空

日期：2026-11-26 UTC。作者：Astra-ISP-347c-20261126；AI-assisted GPT-6 Astra Pro。

**状态：完整证明。** 在原单位2+1+1与孤立零单点层中，共同规范p+q=2后，u=bp+cq=1的整个非零孤立点均值分支为空。全部已登记的低配对、P0零、半比例、jet除数及半权边界均合并；本稿支付最后高曲线和l2原纤维。一般u≠1的非零均值层继续，普通Hilbert ISP未完成。

## 1. 原范围及已经完整支付的边界

沿用[原半比例与jet除数证明](R150-appendix-essential-four-unit-two-plus-one-plus-one-nonzero-isolated-mean-unit-base-mean-half-ratio-exclusion.md)及[缩放有限覆盖](R150-appendix-essential-four-unit-two-plus-one-plus-one-nonzero-mean-unit-base-scaled-finite-cover.md)的同一Frobenius代数、完整Gram与原E/N/P。

写
$$
p=1-\kappa,\quad q=1+\kappa,\quad Q=1-\kappa^2,\quad
\ell=b+c,\quad u=bp+cq=1,
$$
$$
D=\ell^2Q-2\ell+1,\qquad P_0=Q(\ell-1)/2,\qquad
\lambda=m/U_0.
$$
全部零配对、相等/相反配对、P0零已分别关闭；零m整支也已关闭。
前述两稿再排尽l0、lambda=1/2、原jet的g系数零面和整个l=1/2。
其余原点可准确取
$$
v=2\lambda-1,\qquad z=(2f-1)/v
$$
并保持
$$
\mathcal U=v(v+1)Q(Q-1)\ell(\ell-1)
(\ell^2Q-2\ell+1)(z+Q\ell-1)\ne0,\qquad 2\ell-1\ne0.
\tag{1.1}
$$

解掉原jet的g后，保留原三mean的二次式A0,A1,A2，
以及原加权最高/N条件A4,A5；后两式对v至多三次。
这些五式的完整原定义、g图与所有被删单位均见前稿第1、2节。
三mean的系数行列式为B(z,l,Q)，次数(6,8,6)。

前稿已付所有恒零系数纤维，证明整个mean投影的纤维有限，
因此每个原完整点都满足明确的必要曲线
$$
\mathcal C_{18}(\ell,Q)=0,\qquad
(\deg_\ell,\deg_Q)\mathcal C_{18}=(18,10).
\tag{1.2}
$$
这个覆盖已包含特殊与孤立的最高/N交点；本稿不把平面gcd直接当作全零集。

## 2. 两个原混合行列式与真正一元结式

对四个关于v至多三次的多项式，取其对应(v³,v²,v,1)的四行系数行列式。
定义
$$
D_S=\operatorname{Strip}\det\operatorname{coef}_{v^3,v^2,v,1}
(vA_0,A_0,A_1,A_4),
$$
$$
D_N=\operatorname{Strip}\det\operatorname{coef}_{v^3,v^2,v,1}
(vA_1,A_1,A_2,A_5).
\tag{2.1}
$$
Strip始终只反复删除(1.1)及2l−1中的已付因子。
每个原点给非零核向量(v³,v²,v,1)，所以两个行列式必零；
没有除以任何v系数或假定一般秩。

实际原QQ构造给(z,l,Q)次数
$$
\deg D_S=(10,17,12),\qquad \deg D_N=(10,19,13).
$$
接着取
$$
J_S=\operatorname{Strip}\operatorname{Res}_z(B,D_S),\qquad
J_N=\operatorname{Strip}\operatorname{Res}_z(B,D_N),
$$
其(l,Q)次数分别为(60,37)、(82,45)。
每个原点仍须满足两式。
最后作真正QQ一元l结果式
$$
T_S(\ell)=\operatorname{Res}_Q(\mathcal C_{18},J_S),\qquad
T_N(\ell)=\operatorname{Res}_Q(\mathcal C_{18},J_N).
\tag{2.2}
$$

实际次数为1085、1389。完整QQ gcd准确为
$$
\boxed{\gcd(T_S,T_N)\doteq
\ell^{350}(\ell-1)^{84}(2\ell-1)^6(\ell-2)^2.}
\tag{2.3}
$$
这里只差非零有理常数。
已有(1.1)和整半权排除，所以任何原点只能有l=2。
所有结式在原多项式环中计算，领先项降次没有被除掉；有限原共同根必使结式零。

## 3. l2上唯一剩余九次必要因子

把l=2代回(1.2)，只删除已付Q(Q−1)(4Q−3)因子，
得到至非零有理常数唯一的九次多项式
$$
\begin{aligned}
M_9(Q)={}&262144Q^9-136445952Q^8+413595392Q^7\\
&-485798592Q^6+270885520Q^5-70094916Q^4\\
&+7538804Q^3-883844Q^2+156660Q-12753.
\end{aligned}
\tag{3.1}
$$
因此最后原点必须同时满足l=2、M9(Q)=0及五条原式。
此处没有选择九次式的某一个根，也没有用近似根代替原系数。

令
$$
\mathcal A=\mathbb Q[Q]/(M_9).
\tag{3.2}
$$
它是整个九维有理系数代数。下面的证明不需要预设M9不可约：
每一个实际要逆的系数均在整个商代数上单独求真逆，
所以同一次身份覆盖M9的所有复根。
源码还准确核对M9与其导数互素，但这个平方自由事实不代替任何单位检查。

## 4. 整个九维代数中的原z单位

在l2原图，v(v+1)Q(Q−1)(4Q−3)(z+2Q−1)非零。
记B2为原B的l2专门化，并将A_i同样专门化。
构造以下原必要z多项式，仍只删除上述已付单位：
$$
B_2,\qquad
R_{01}=\operatorname{Res}_v(A_0,A_1),\quad
R_{02}=\operatorname{Res}_v(A_0,A_2),\quad
R_{04}=\operatorname{Res}_v(A_0,A_4).
\tag{4.1}
$$
将它们的Q系数按M9取余，视为A[z]中的多项式。

源码在整个A中执行完整Euclid算法。每次需逆系数c时，
实际在QQ[Q]上计算
$$
u(Q)c(Q)+v(Q)M_9(Q)=g,\qquad g\in\mathbb Q^\times,
$$
并验证c·(u/g)=1 mod M9。
每步z多项式除法也实际乘回验证旧被除式=商·除式+余式。
因此没有把含零因子的有限代数当作域，也没有默除未付的领先项。

实际连续共同z次数为：

| 新加入的原多项式 | 原(z,Q)次数 | 加入后的共同z次数 | 累计QQ真逆数 |
|---|---:|---:|---:|
| B2 | (6,6) | 6 | 1 |
| R01 | (8,10) | 1 | 8 |
| R02 | (8,8) | 1 | 10 |
| R04 | (12,12) | 0 | 13 |

最后首一共同因子准确为1。
Euclid的全部单位与回乘身份因此给出
$$
\boxed{1\in(B_2,R_{01},R_{02},R_{04})\subset\mathcal A[z].}
\tag{4.2}
$$
对M9的任意复根Q0，代入映射A→C保持该身份。
故不存在满足(4.1)的有限z，更不存在原(v,z,Q)点。
原最后A5甚至不必再次使用；这不是删条件放宽后误认充分，
而是一个已经矛盾的原必要子系统。

## 5. 整个u1图合并

(2.3)迫最后原点到l2，(3.1)保其全部Q纤维，
(4.2)又在整个九维商代数中排空这些纤维。
与前稿已完整支付的低配对、P0零、l0、lambda半比例、
原jet除数及l半权合并，u1非零孤立点mean整图为空。

一般u≠1没有因此被规范到u1；这里的共同缩放已用于p+q=2，
不能再独立更换u。后续继续原U值图的一般非零mean及其L/S退化面。

## 6. 实际执行与可复算输入

[混合行列式源](../notes/2026-11-26-unit211-scaled-high-curve-mixed-projections-347c.py)
固定于提交3d671b1c98f929848e2c437698cece6f8d2e033e，
源码SHA256 3e946d84c93c28310d7be2a332295fcbd13c8cd44f6b9478be8f47aa8a3c00a0。
run45799548882/job139838880139实际24.917169209秒，
驱动25.054241903秒、RSS116052KiB、exit0，得到(2.3)。

[末投影短源](../notes/2026-11-26-unit211-scaled-l2-projection-347c.py)
在run45803350694/job139852028943实际5.498579259秒、
94096KiB、exit0，完整输出(3.1)的准确因子；当时只报告结构，
并未预先宣称纤维空。

[整九维代数源](../notes/2026-11-26-unit211-scaled-l2-nine-algebra-347c.py)
固定于提交816ddd187cbedbcd7af373ebc0ec9db50f3b3145，
Git blob c56ec251ddb70c33f28e425d5b0ef2e081c99119，
SHA256 1cfd5100af446074d2d98868eacba312afa5f50d1596fc2fe7aa72465ffdd861。
run45804559912/job139856248459实际5.703188372秒，
驱动5.837008895秒、RSS94636KiB、exit0，
13次QQ求逆和全部除法回乘均成功。
其stdout SHA256为f149695fb9c761210b9e4af893fcebfe9e24b0d8dbb4adf08228f6d26a3c7434。

[真实小回执](../notes/2026-11-26-unit211-unit-base-completed-execution-347c.json)
分别保留三个输入、执行、源码与规则读取身份。
原缩放覆盖的末JSON报告exit1仍据实保留；其数学断言和本次三个成功运行分开登记。
另一路较慢的多变量GB不参与本证明，无需等它或重跑它来认证(4.2)。
大多项式及QQ商环数组均由原源重建，不提交可再生表。
