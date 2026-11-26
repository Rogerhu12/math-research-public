# R150 附录：秩二第三累积量的全部内均值临界点

日期：2026-11-26（UTC）。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：已证明。** 本稿关闭非约化二重 jet 的整个内均值层；结合此前两点层，任一原完整临界点若 $\operatorname{rank}V=2$ 且 $y\in\operatorname{Ran}V$，则整个普通第三矩 $T_3$ 为零。二阶累积量的支撑由最高方程推出，未作任何预设。

## 1. 原张量与完整分类

采用原整数 $K$、物理曲线 $u(a,b)=(a^5,a^4b,\ldots,b^5)^{\mathsf T}$、Hankel 二阶和三阶累积量及完整 $\mathcal Q_3$。精确原定义和全部梯度见[两点系数一致定理](R150-appendix-rank-two-third-cumulant-aligned-mean-pencil-is-zero-third-tensor.md) §§1–3。

由[低秩 Hankel 张量的有限 jet 表示](R150-appendix-length-three-common-jets-and-inside-mean-critical-dichotomy.md) §6，原第三张量展平秩为二时，其唯一最小物理除子恰为两个不同点，或一个二重点。这里第三张量一阶展平的重复列按 $j+k$ 合并后正是原二元十五次泛函的五阶 catalecticant，故所引引理准确适用；不涉及无限矩延拓。

**定理。** 假设原完整临界点满足
$$
\operatorname{rank}V=2,\qquad y\in\operatorname{Ran}V.
$$
则它恰为以下两种类型之一。

**两个不同点：**
$$
\begin{aligned}
y&=a u+b v,\\
H&=\tfrac12a^2u^2+\tfrac12b^2v^2,\\
V&=\tfrac12a^3u^3+\tfrac12b^3v^3,
\end{aligned}
\qquad u=u(s),\ v=u(t),\ s\ne t,\ ab\ne0.
\tag{1.1}
$$
此型已由[两点第三累积量内均值完整分类](R150-appendix-rank-two-reduced-third-cumulant-inside-mean-complete-classification.md)证明。

**一个二重点：**
$$
\boxed{
\begin{aligned}
y&=a u,\\
H&=\frac{a^3+4c}{6a}uu^{\mathsf T}
  +\frac d a(uw^{\mathsf T}+wu^{\mathsf T}),\\
V&=c u^{\otimes3}
 +d(u\otimes u\otimes w+u\otimes w\otimes u+w\otimes u\otimes u),
\end{aligned}
}
\tag{1.2}
$$
其中
$$
a d\ne0,\quad c\in\mathbb C,\qquad
s\in\{0,2,-6,\infty\}.
\tag{1.3}
$$
有限点使用 $u=u(s)$、$w=u'(s)$；在无穷远使用局部曲线
$(z^5,z^4,z^3,z^2,z,1)$ 的值和导数，即 $u=e_5,w=e_4$。
改变局部参数或代表只重标量这些系数。

所有 (1.1)、(1.2) 的完整第三矩 $T_3=y^3-6yH+4V$ 均零。以下只证明尚未付的二重点排除。

## 2. 二重点的原最高整除及唯一可能的系数关系

设非约化第三张量准确为
$$
V=c u^3+d\,\operatorname{Sym}_{\Sigma}(u^2w),\qquad d\ne0,
$$
并写内均值
$$
y=a u+bw.
\tag{2.1}
$$
这里 $\operatorname{Sym}_{\Sigma}$ 是三个不同位置之和；作为对偶变量三次多项式，$V=cX^3+3dX^2Y$。

记原物理极线
$$
A(x)=u^{\mathsf T}Ku(x),\qquad
B(x)=w^{\mathsf T}Ku(x),\qquad P=aA+bB.
$$
$A,B$ 线性无关。全部原最高式是
$$
P^3-6PG_H+4cA^3+12dA^2B=0.
\tag{2.2}
$$
若 $y=0$，该式迫 $A^2(cA+3dB)=0$，与 $d\ne0$ 及线性无关矛盾。因此 $P\ne0$。

先假设 $b\ne0$。写
$$
A=gG,\qquad B=gH,\qquad \gcd(G,H)=1,\quad
\overline P=aG+bH.
$$
从 (2.2) 得
$$
\overline P\mid g^2G^2(cG+3dH).
$$
因为 $\gcd(\overline P,G)=1$，而模 $\overline P$ 有
$b(cG+3dH)\equiv(cb-3da)G$，准确得到
$$
\boxed{cb=3da\quad\text{或}\quad \overline P\mid g^2.}
\tag{2.3}
$$
下一节完整排除第二项，保全部重接触点和无穷远。

## 3. 同点极线与导数的公共因子不可能吸收均值

### 3.1 自接触和所有额外公共点

有限图中
$$
A(z)=-(z-s)^2q_s(z),\qquad B(z)=\partial_s A(z),
$$
其中 $q_s$ 是前稿的原三次式。原完整接触表为
$$
\begin{array}{c|cc}
s&\operatorname{ord}_sA&\operatorname{ord}_sB\\ \hline
s\notin\{0,2,-6,\infty\}&2&1\\
s=2,-6&3&2\\
s=0,\infty&4&3
\end{array}
\tag{3.1}
$$
见[原曲线 jet 接触表](R150-appendix-length-three-common-jets-and-inside-mean-critical-dichotomy.md) §1。因为 $b\ne0$，$P=aA+bB$ 的自接触阶数总是较小的 $\operatorname{ord}_sB$；故除掉 $g$ 的全部自因子以后，
$$
\overline P(s)\ne0.
\tag{3.2}
$$

有限 $s$ 时，无穷远不是额外公共点，因为
$A(\infty)=-(s+1)$ 而 $B(\infty)=-1$。任一不同有限公共点 $t\ne s$ 必满足
$$
q_s(t)=0,\qquad \partial_s q_s(t)=0.
\tag{3.3}
$$
利用核的对称性，这恰说明 $q_t(z)$ 在 $z=s$ 有重根。

在自接触特殊点 $s=0,2,-6,\infty$，这样的额外点不可能出现。确实，这些点的 $w^{\mathsf T}Kw=0$；(3.3) 若成立，会使
$\operatorname{span}\{u,w,u(t)\}$ 成为原全等向长度三的 $2+1$ jet 支撑，已由[完整等向 jet 分类](R150-appendix-classification-of-isotropic-length-three-curve-jets.md) §§3、5 排除。因此这些点的公共因子只有自因子。

### 3.2 八次双根图的原多项式逆

对普通自接触点，前稿的[原八次双根门](R150-appendix-rank-two-reduced-third-cumulant-inside-mean-complete-classification.md) §5 已证明：任何 (3.3) 的不同点对都满足
$$
D(t)=0,\qquad s=\alpha(t),
$$
$$
D(t)=5t^8+50t^7+153t^6-936t^5-2888t^4
+15936t^3-3392t^2-25472t+9600,
$$
$$
\alpha(t)=
\frac{9a_3a_0-a_2a_1}{2(a_2^2-3a_3a_1)},
\qquad q_t(z)=a_3z^3+a_2z^2+a_1z+a_0.
\tag{3.4}
$$
该文已支付显示分母、$s\ne t$、普通自接触以及 $q_s'(t)\ne0$ 的全部 QQ 逆，所以每个额外公共点在 $A$ 中只有一重。这些事实不在本稿重新作为新结论登记。

这里需要的新事实是：同一个 $s$ 不可能对应两个不同的 $t$。在
$E_D=\mathbb Q[t]/(D)$ 中构造八阶矩阵
$$
M_{ij}=[t^i](\alpha(t)^j\bmod D),\qquad 0\le i,j\le7.
\tag{3.5}
$$
准确 QQ 运算得到 $\det M\ne0$，并回乘核其逆的全部64个条目。
令 $(r_0,\ldots,r_7)^{\mathsf T}=M^{-1}e_1$，则同一计算逐系数证明
$$
\boxed{t=\sum_{j=0}^7r_j\alpha(t)^j\quad\text{于 }E_D.}
\tag{3.6}
$$
若两个复根 $t_1,t_2$ 有相同 $\alpha$ 值，对 (3.6) 代入便给 $t_1=t_2$。此处不需不可约性或数值选根。

因此普通点的公共因子只能是
$$
g=\Delta_s\quad\text{或}\quad g=\Delta_s\Delta_t\ (t\ne s),
\tag{3.7}
$$
额外点在 $g$ 中也仅一重。特殊点则分别为
$\Delta_s^2$ 或 $\Delta_s^3$；所有齐次形式差非零常数。

### 3.3 全部吸收情形为空

若 $g$ 只支持 $s$，(3.2) 立即使 $\overline P\mid g^2$ 不可能。

若 $g=\Delta_s\Delta_t$，$\overline P$ 的齐次次数是三，而 (3.2) 排除了 $s$。唯一可用的根只有 $t$，但 $g^2$ 在 $t$ 只有重数二，仍不可能。

无穷远自接触已在 (3.1) 和特殊点结论中覆盖；也可直接核
$$
A_\infty=-a^4(a+b),\qquad
B_\infty=5a^3(a^2+ab+b^2),\qquad
\gcd(A_\infty,B_\infty)=a^3.
$$
至此 (2.3) 的吸收项全排，所以在 $b\ne0$ 下必有 $cb=3da$。

## 4. 系数一致后最高式唯一决定全部原二阶矩

按原权 $(1,2,3)$ 缩放将 $b$ 置一，并将 $a/b,d/b^3$ 重新记为 $a,d$。此时
$$
y=a u+w,\qquad c=3da,\qquad d\ne0.
\tag{4.1}
$$
原最高式准确成为
$$
P\{P^2-6G_H+12dA^2\}=0.
$$
在多项式整环中取消非零 $P$，得
$$
G_H=P^2/6+2dA^2.
\tag{4.2}
$$
因为原 $J_2$ 可逆，定义唯一 Hankel 矩阵
$$
\mathsf C_s=J_2^{-1}[B^2],
\tag{4.3}
$$
就有唯一完整原二阶矩
$$
\boxed{
H=(a^2/6+2d)uu^{\mathsf T}
 +(a/6)(uw^{\mathsf T}+wu^{\mathsf T})
 +\mathsf C_s/6.
}
\tag{4.4}
$$
$\mathsf C_s$ 一般不支持 $\operatorname{span}\{u,w\}$；(4.4) 没有免费附加共同支撑。

## 5. 完整原 mean 梯度排除所有真正切向均值

记 $p=Ky,F=y^{\mathsf T}Ky/2,h=Hp,b_0=p^{\mathsf T}Hp,\tau_2=\operatorname{tr}((KH)^2)$，并置
$$
P_0=p^{\mathsf T}u,\quad P_1=p^{\mathsf T}w,\quad
G_{00}=u^{\mathsf T}KHK u,\quad G_{01}=u^{\mathsf T}KHK w.
$$
原全部三阶贡献给
$$
\begin{aligned}
\Gamma={}&(F^2-2b_0+2\tau_2)y-4FHp+8HKHp\\
&+4c(P_0^2-2G_{00})u\\
&+4d\{(2P_0P_1-4G_{01})u+(P_0^2-2G_{00})w\},
\end{aligned}
\tag{5.1}
$$
$$
\begin{aligned}
N={}&Fyy^{\mathsf T}-2FH-2(yh^{\mathsf T}+hy^{\mathsf T})+4HKH\\
&+4(cP_0+dP_1)uu^{\mathsf T}
 +4dP_0(uw^{\mathsf T}+wu^{\mathsf T}).
\end{aligned}
\tag{5.2}
$$
仍有 $\nabla_y\mathcal Q_3=3K\Gamma$ 和
$\partial_{H_m}\mathcal Q_3=-6[z^m]u(z)^{\mathsf T}KNKu(z)$。

在 (4.4) 上，源从原矩精确核 $P_0=G_{00}=G_{01}=0$。虽然 (5.1) 的三阶项最后为零，(5.2) 中 $4dP_1uu^{\mathsf T}$ 一般不为零，始终保留。验证器用原 $J_3$ 计算完整
$$
\mathcal Q_3=G_6+4[P^3-6PG_H]^{\mathsf T}V+8V^{\mathsf T}J_3V,
$$
并核 $s,a,d$ 三参数的全部原链式法则，包含十六个 $V$ 偏导。

### 5.1 有限点的完整64阶门

对原六个 mean 梯度准确展开后，有
$$
\Gamma_i=A_i(s)+aB_i(s),\qquad 0\le i\le5,
\tag{5.3}
$$
全部独立于 $d$。源逐项核 $a$ 次数至多一、$d$ 次数零，没有丢弃项。

若 $\Gamma=0$，两个原二阶子式
$$
R_1=A_0B_1-A_1B_0,\qquad
R_2=A_0B_2-A_2B_0
$$
必须同时为零。准确 QQ 计算给
$$
\deg R_1=\deg R_2=32,\qquad \gcd(R_1,R_2)=1.
$$
每个系数分母为1009单位，两首项分别约化为964和458。整个64阶 Sylvester 行列式实际为
$$
\boxed{\det\operatorname{Sylv}(R_1,R_2)\equiv618\pmod{1009}.}
\tag{5.4}
$$
因此完整有理数行列式非零，原两式在 $\mathbb C$ 无共同根。所有有限 $s$、所有有限 $a$ 和所有 $d\ne0$ 均被排除，包含自接触特殊点及任何低阶降次。

### 5.2 无穷远

直接取原 $u=e_5,w=e_4$，从 (4.3)–(5.2) 重建所有张量。前两个原 mean 方程是
$$
\Gamma_0=
\frac{621081558405921875+36721276678565625a}
 {5948992536757826857744},
$$
$$
\Gamma_1=
\frac{-1109582063944109375-64060260227878125a}
 {5948992536757826857744}.
\tag{5.5}
$$
二者的常数/一次系数矩阵行列式约化为45，分母为1009单位；故原有理数行列式非零，不能同时为零。这支付了整个无穷远切向层。

所有 $b\ne0$ 内均值情形均已排除。

## 6. 剩余物理值均值直接给完整第三矩为零

只能 $b=0$，故 $y=a u$；由 §2，$a\ne0$。原最高式取消非零 $aA$ 后唯一给
$$
G_H=\frac{a^3+4c}{6a}A^2+\frac{2d}{a}AB.
$$
原 $J_2$ 可逆，直接得到 (1.2) 的 $H$。代回完整张量
$T_3=y^3-6yH+4V$，纯 $u^3$ 及混合 $u^2w$ 系数分别全部消掉，所以
$$
T_3=0.
$$

[非零均值、零第三矩的完整临界分类](R150-appendix-nonzero-mean-zero-third-moment-critical-classification.md) §§4–5 已证明：此类切向二阶系数为 $d/a$，其完整二阶梯度要求
$$
(d/a)^2\,w^{\mathsf T}Kw=0.
$$
因为 $ad\ne0$，有限点须
$$
w^{\mathsf T}Kw=-2s^2(s-2)(s+6)=0,
$$
并加无穷远原 $e_4^{\mathsf T}Ke_4=0$，恰得 (1.3)。该旧定理也已证明这些点的全部低阶及最高梯度同时为零。因此 (1.2)–(1.3) 是完整必要且充分的清单。

与此前两个不同点的完整分类合并，定理涵盖所有原 rankV2 内均值临界点。

## 7. 实际精确执行及剩余范围

[自含验证器](../notes/2026-11-26-r150-tangent-rank-two-v-inside-mean-verify.py)从原整数 $K$ 卷积 $J_2,J_3$，核原两个行列式，构造 (3.5) 的准确逆和 (3.6) 的原多项式身份；随后直接重建完整二jet张量、六 mean、十一二阶、十六最高及三参数原链式法则。最后完整核64阶门618和无穷远两方程门45。

实际源码 SHA256：
0e94b0f786c48bade2af4b3c809c47be6092e66095838e5589bb3a19c8003640。

2026-11-26以 Python 3.12.14、python-flint 0.9.0 实际执行，exit 0，源内时间0.10892299099941738秒。完整结果见[实际执行回执](../notes/2026-11-26-r150-tangent-rank-two-v-inside-mean-execution.json)。八阶基矩阵、逆矩阵、恢复多项式和全部梯度均有紧凑哈希；可重算长数组不入库。

本稿没有从 rankV2 免费推出 $y\in\operatorname{Ran}V$。新的明确剩余是
$$
\boxed{\operatorname{rank}V=2,\qquad y\notin\operatorname{Ran}V,}
$$
以及更高秩层。此处 $H$ 仍须由完整原方程处理，不能预设其支撑。原全局 Bell 自然幂、实际算子费用桥和普通 Hilbert ISP仍未关闭。

