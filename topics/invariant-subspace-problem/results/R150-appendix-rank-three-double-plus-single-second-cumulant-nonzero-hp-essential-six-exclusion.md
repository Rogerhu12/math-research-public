# R150 附录：二重加单点 H 的非零 Hp 本质六维截面排除

日期：2026-11-26（UTC）。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：已证明。** 原完整临界点若 rankH3 为 $2+1$ 物理支撑、rankV2 且 $Hp\ne0$，则 $\dim\operatorname{ess}(T_3)\le5$。最后显示的有理多项式 gcd 与两个有限有理商代数的单位身份已经由原精确 QQ 源实际成功验证；不使用模素数空集作为特征零证明。

## 1. 已付规范、全部非零边界与两个 V 行

[退化 Gram 全排除](R150-appendix-rank-three-double-plus-single-second-cumulant-degenerate-gram-essential-six-exclusion.md)与[非约化 V 全排除](R150-appendix-rank-three-double-plus-single-second-cumulant-nonreduced-third-cumulant-essential-six-exclusion.md)已经使本质六维反设只余非退化 H Gram、约化 V、$F\ne0,e\ne0$。沿用可逆尺度，取
$$
F=h=g=1,\quad H=z_0z_1+z_1z_0+\tfrac12w^2,\quad
K_R=\begin{pmatrix}0&0&1\\0&b_H&c_H\\1&c_H&0\end{pmatrix},
$$
$$
V=\tfrac12(u^3+v^3),\qquad e=uKv,\qquad p(u)=p(v)=e.
$$
六列 $(y,z_0,z_1,w,u,v)$ 是原整个六空间的基；所有物理值及局部 jet 均沿用原 K，未替换为自由一般矩阵。

[非零 Hp 的重节点配对完整归约](R150-appendix-rank-three-double-plus-single-second-cumulant-nonzero-hp-distinct-node-pairings.md)给出
$$
\chi=e^3,\quad r=p(w)=p(z_0)\ne0,\quad
b_H=(1-\chi)/6,\quad c_H=(2\chi+1)/12,
$$
$$
r^2=(\chi+2)/(4-\chi),\qquad
p(z_1)=r(5-2\chi)/12,
$$
$$
\chi\notin\{0,1,-2,4\},\qquad
C_0D_0(C_0-D_0)\ne0,
\tag{1.1}
$$
其中 $C_i=K(z_i,u),D_i=K(z_i,v)$。

作非零尺度定义两行
$$
(a_1,b_1,c_1)=\frac1{er}
  \bigl(K(z_0,u),K(z_1,u),K(w,u)\bigr),
$$
$$
(a_2,b_2,c_2)=\frac1{er}
  \bigl(K(z_0,v),K(z_1,v),K(w,v)\bigr).
$$
令
$$
d=\chi(\chi+2),\quad k=5-2\chi,\quad
n=-4\chi^2+14\chi-1,\quad \sigma=a_1+a_2.
$$
完整原值和一次系数已经给
$$
a_1^2+a_2^2=3/d,\quad a_1^3+a_2^3=k/d,
$$
$$
a_1b_1+a_2b_2=n/(12d),\quad
a_1^2b_1+a_2^2b_2=3/(4d).
\tag{1.2}
$$
因此
$$
\Phi:=d\sigma^3-9\sigma+2k=0,
$$
$$
J:=9-dk\sigma=-d^2a_1a_2(a_1-a_2)^2\ne0.
\tag{1.3}
$$
两个一次坐标唯一为
$$
b_i=\alpha a_i+\beta,\qquad
\alpha=\frac{n-3d\sigma}{4J},\quad
\beta=\frac{2(\chi-1)^2(4-\chi)}{3J}.
\tag{1.4}
$$
至此只除过 (1.1)、(1.3) 中已经非零的量。

## 2. 孤立物理值及完整 V mean 给第二个三次式

完整 V mean 方程分别为
$$
4a_ib_i+c_i^2=(4-\chi)/(\chi+2),\quad i=1,2.
\tag{2.1}
$$
完整 H 极线和最高恒等式在孤立物理值 w 处分别给
$$
c_1^2+c_2^2=\frac{C}{3d},\qquad
c_1^3+c_2^3=\frac{E}{d},
$$
其中
$$
C=-2\chi^2+10\chi+1,\qquad E=-\chi^2+3\chi+1.
\tag{2.2}
$$
为核查系数，未缩放的原 w 值是
$$
2e(C_w^2+D_w^2)=r^2+4c_H-4b_H,\qquad
2(C_w^3+D_w^3)=12c_Hr-r^3.
$$
除以 $(er)^2$、$(er)^3$ 才得到 (2.2)。

置 $\tau=c_1+c_2$。由 (2.2)，
$$
H_\tau:=d\tau^3-C\tau+2E=0.
\tag{2.3}
$$
没有要求 $c_i$、$\tau$ 或 $c_1-c_2$ 非零。

因 $a_1\ne a_2$，存在唯一的 $\gamma,\delta$ 使
$c_i=\gamma a_i+\delta$，并有 $\delta=(\tau-\gamma\sigma)/2$。定义
$$
\Delta=6/d-\sigma^2=(a_1-a_2)^2.
$$
把 (1.4) 代入 (2.1)，在二次关系
$a_i^2-\sigma a_i+( \sigma^2-3/d)/2=0$ 下比较两个系数，准确得到
$$
\gamma\tau=-4(\alpha\sigma+\beta),\qquad
\gamma^2\Delta+\tau^2=2C/(3d).
\tag{2.4}
$$
这些是系数身份，仍覆盖 $\gamma=0$、$\tau=0$ 的全部边界。

## 3. 两个原 N 值之差保留完整 Gaussian 与 V 项

完整 H 张量为
$$
N=yy^{\mathsf T}-2H
-2\bigl(y(Hp)^{\mathsf T}+(Hp)y^{\mathsf T}\bigr)
+4HKH+2e(u^2+v^2).
$$
在物理值 u、v 处，用完整 V mean 消去第一对项后，原 N 极线准确给
$$
(HKH)(K u_i,K u_i)-e\,H(p,K u_i)+e^3/2=0.
$$
这里 $u_1=u,u_2=v$。代入原 (1.1) 的 Gram 及上述行尺度，得到
$$
b_Ha_i^2+(c_Ha_i+b_i)c_i
-\bigl((1/2-c_H)a_i+b_i+c_i/2\bigr)
+\frac{e}{2r^2}=0.
\tag{3.1}
$$
最后一项在两行完全相同，不能在单行中删除；在两式相减时才消去。

代入 $b_i=\alpha a_i+\beta$、$c_i=\gamma a_i+\delta$，用两 a 值的二次关系，再除以已经非零的 $a_1-a_2$，得到
$$
A\gamma+B\tau+C_0=0,
$$
$$
A=(c_H+\alpha)\sigma/2+\beta-1/2,\quad
B=(c_H+\alpha)/2,\quad
C_0=b_H\sigma-(1/2-c_H+\alpha).
\tag{3.2}
$$

为给出整数输入，设
$$
n_a=n-3d\sigma,\qquad n_b=2(\chi-1)^2(4-\chi),
$$
$$
B_*=(2\chi+1)J+3n_a,
$$
$$
A_*=B_*\sigma+8n_b-12J,
$$
$$
C_*=4(1-\chi)J\sigma-2kJ-6n_a,
\qquad L_*=-3n_a\sigma-4n_b.
\tag{3.3}
$$
则 $A_*=24JA,B_*=24JB,C_*=24JC_0$，且
$3J\gamma\tau=L_*$。

将 $A_*\gamma+B_*\tau+C_*=0$ 乘以 $\tau$，再用第一条 (2.4)，得到
$$
\boxed{G_1=3JB_*\tau^2+3JC_*\tau+A_*L_*=0.}
\tag{3.4}
$$
将同一线性式平方，再用第二条 (2.4)，得到
$$
\boxed{
G_2=3(6-d\sigma^2)(B_*\tau+C_*)^2
+A_*^2(3d\tau^2-2C)=0.
}
\tag{3.5}
$$
没有除以 $A_*,B_*,C_*,L_*,\tau,\gamma$。因此这些系数的每种退化都保留。完整反设必满足四个显示的整数式
$$
\Phi=H_\tau=G_1=G_2=0.
\tag{3.6}
$$

## 4. 原精确 QQ 消元完整覆盖全部参数

新源按 (1.3)、(2.3)、(3.3)—(3.5) 重新构造整数输入，定义
$$
R_i(\chi,\sigma)=\operatorname{Res}_\tau(H_\tau,G_i),
\qquad
N_i(\chi)=\operatorname{Res}_\sigma(\Phi,R_i),\quad i=1,2.
\tag{4.1}
$$
有限的原共同根必使这些结果式为零，即使某个次要首项降次也如此；没有以结果式的非零首项作未经支付的除法。

原精确 QQ 源实际计算出 $N_1,N_2$ 的次数分别为 **93、126**，均非零；其真实有理 gcd 的次数为 **56**，全部根均包含于
$$
\chi(\chi-1)(\chi+2)(\chi-4)Q_2(\chi)Q_4(\chi)=0,
\tag{4.2}
$$
其中
$$
Q_2=4\chi^2-4\chi-27,\qquad
Q_4=8\chi^4-24\chi^3-30\chi^2+100\chi-27.
$$
源码通过实际 QQ gcd、逐次精确整除和余数为零检查验证 (4.2)，不使用有限域 gcd 猜测特征零公因子。

前四个根已经由 (1.1) 排除。重要的是：$Q_2,Q_4$ 的根不能因为它们来自 J 的范数就直接删除。同一个 $\chi$ 处仍可能有不同的、J 非零的 $\sigma$。下一节保留并处理所有这些好纤维。

## 5. 两个异常谱的全部好纤维

准确恒等式
$$
dk^2-27=(\chi-1)^2Q_2,\qquad 2dk^2-27=Q_4
$$
给出：

在整个 $\mathbb Q[\chi]/(Q_2)$ 上，
$$
27\Phi=d(3\sigma-k)^2(3\sigma+2k).
\tag{5.1}
$$
因 $d\ne0$，原 $\Phi=0$ 迫某个因子为零。$3\sigma-k=0$ 时
$J=9-dk^2/3=0$，已被 (1.3) 排除；所以全部合法纤维必须满足
$$
P_2:=3\sigma+2k=0.
$$

在整个 $\mathbb Q[\chi]/(Q_4)$ 上，
$$
27\Phi=d(3\sigma-2k)(9\sigma^2+6k\sigma-2k^2).
\tag{5.2}
$$
前一个因子为零时 $J=9-2dk^2/3=0$，同样已排除。因此全部合法纤维必须满足
$$
P_4:=9\sigma^2+6k\sigma-2k^2=0.
$$
(5.1)—(5.2) 为整商代数身份，包含全部复根、所有平方根符号及重复的 J 零因子。

对这些保留的好纤维继续使用原 $G_1$ 与 $H_\tau$，定义
$$
B_2(\chi)=\operatorname{Res}_\sigma(P_2,R_1),\qquad
B_4(\chi)=\operatorname{Res}_\sigma(P_4,R_1).
\tag{5.3}
$$
原精确 QQ 源实际构造并回乘的两个单位身份是
$$
B_2\text{ 在 }\mathbb Q[\chi]/(Q_2)\text{ 中为单位},\qquad
B_4\text{ 在 }\mathbb Q[\chi]/(Q_4)\text{ 中为单位}.
\tag{5.4}
$$
源码实际使用有理 xgcd 构造两个逆，并逐一准确回乘一；另验证 $d,k$ 与先前四个非零因子在对应商代数中的全部除法边界。两个原 QQ 单位身份已实际成功，(5.3) 的必要零式因此与单位身份矛盾，(4.2) 的两个异常谱全被排除。实际 $B_2,B_4$ 的次数分别为 **34、68**；源码并未用平方自由根近似或有限域单位替代这些特征零逆。

## 6. 完整结论与实际执行身份

§4 的整个 QQ gcd 门与 §5 的两个原 QQ 单位门已经实际成功；(3.6) 不存在任何未支付边界，整个非退化 $2+1$ H、非零 Hp、约化 rankV2 的本质六维反设为空。结合已登记的退化 H Gram、非约化 V 排除，便有
$$
\operatorname{rank}H=3,\ H\text{ 为 }2+1,\quad
\operatorname{rank}V=2,\quad Hp\ne0
\quad\Longrightarrow\quad
\dim\operatorname{ess}(T_3)\le5.
$$

本稿的[原精确 QQ 源](../notes/2026-11-26-h21-nonzero-hp-exact-347c.py)已经在[独立公开执行](https://github.com/Rogerhu12/math-research-public/actions/runs/45795365604/job/139824523000)完成：run **45795365604**，job **139824523000**，源提交 **96819c8f4b69f55f513137692d3e4587f104196d**；exit code **0**，源内耗时 **0.011088509 秒**，报告峰值 RSS **36048 KiB**。源 SHA-256 为 **df42d64c9a2288fb1a64976e68882a10e83d8449ea5490516a0d4786a464936d**。全部六个 QQ 逆均准确回乘一，其中两个为上述原障碍逆，另四个支付先前非零因子与 k 的异常谱边界。结果式次数以该真实源的 **93、126、34、68** 为准，未使用早期模点探针含额外清分母幂的次数。

零 Hp 的原物理九次候选层、本质四五维及 ISP 完成标准仍未由本结论关闭。

实际stdout SHA及pull/规则身份保[小回执](../notes/2026-11-26-h21-nonzero-hp-execution-347c.json)。
