# R150 附录：单位 2+1+1 与孤立零点的零基点 mean 支路全部为空

作者：Astra-ISP-347c-20261126 / unit31_general；AI-assisted GPT-6 Astra Pro。日期：2026-11-26 UTC。

**状态：本条精确范围已证明。** 本条在同一原单位 $2+1+1$、孤立零点、$\operatorname{rank}H=4$ 支路中排除 $d_0=0$。此前[零基点配对](R150-appendix-essential-four-unit-two-plus-one-plus-one-zero-base-pairings-exclusion.md)、[一条基点配对为零](R150-appendix-essential-four-unit-two-plus-one-plus-one-one-zero-base-pairing-exclusion.md)已分别关闭。现在剩余原临界点不仅须 $pq\ne0$，还须 $bp+cq\ne0$。一般非零 mean 和其他未闭原支路仍然存在于待办范围，本结论没有给出全局 Bell 幂来源或 Hilbert 不变子空间定理。

## 1. 全部原对象及本条保留的必要条件

使用[原外均值 essential-four 长度五代数](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md)及前述单位 $2+1+1$ 稿的同一原物理支撑 $2A+B+C+Z$。活跃代数和 Frobenius 泛函是
$$
\mathcal B=\mathbb C[\epsilon]/(\epsilon^2)\oplus\mathbb C\oplus\mathbb C,
\quad\tau(X)=aX_0+X_1+bX_B+cX_C,\quad a=1-b-c,\quad bc\ne0.
$$
原活跃 Gram、零点配对及其 mean 是
$$
K_B=\begin{pmatrix}0&0&p&q\\0&A_1&r&s\\p&r&0&t\\q&s&t&0\end{pmatrix},
\qquad U=(u_0,u_1,u_B,u_C),\qquad m=\tau(U).
$$
以同一原 Frobenius 乘法定义
$$
(D_KX)_i=\tau(k_iX),\quad d=D_K1,\quad f=\tfrac12\tau(d),
$$
$$
E=e-2D_Kd-2d^2+4fd,
\qquad e=(\tau k_0^2,2\tau k_0k_1,\tau k_B^2,\tau k_C^2),
$$
$$
P(X)=\tfrac12\tau((X-\tau(X)1)^3),
$$
$$
N(X)=\tfrac12\tau((d-f1)X^2)-\tau(X)\tau(dX)
       +f\tau(X)^2+\tfrac14\tau(XD_KX).
$$
原 active mean 是 $E=0$，完整原最高式与第二梯度是 $P+R^3$、$N+mR^2$。其活跃值和双点一阶 jet 满足
$$
(P_0,P_1,P_B,P_C)=(-u_0^3,-3u_0^2u_1,-u_B^3,-u_C^3),
$$
$$
(N_0,N_1,N_B,N_C)=(-mu_0^2,-2mu_0u_1,-mu_B^2,-mu_C^2). \tag{1.1}
$$
特别
$$
c_0=3P_0N_1-2N_0P_1=0.                                \tag{1.2}
$$

此外，[相反配对零 mean 稿](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-pairings-zero-base-mean-exclusion.md)第 1 节已经由原最高式在原孤立零点 $Z$ 的取值证明了无除法恒等式
$$
2P(U)=2m^3-J,
$$
$$
J=aP_0+P_1+bP_B+cP_C-3(aN_0+N_1+bN_B+cN_C).
$$
因 $R(Z)=K(Z,Z)=0$，完整最高恒等式给 $P(U)=0$，所以还必须
$$
\Gamma_i=2N_i^3+JP_i^2=0\quad(i=0,B,C).                \tag{1.3}
$$
这些都是同一原方程的必要后果，适用于所有零 $P_i,N_i,m,u_i$。本文用这些必要条件证明不存在原解，不将它们当作物理临界性充分条件。

## 2. $d_0=0$ 的准确坐标与一个线性系统

因此前零配对支路已排，可令 $p=1$，保留 $q\ne0$。此时
$$
d_0=b+cq=0\quad\Longleftrightarrow\quad b=-cq.
$$
$q=1$ 正好是[相等配对、零总权支路](R150-appendix-essential-four-unit-two-plus-one-plus-one-equal-base-pairings-zero-total-weight-exclusion.md)，$q=-1$ 正好是前引相反配对稿。两者已经独立完整关闭，本条直接计算的余下范围是
$$
q(q-1)(q+1)c\ne0.                                     \tag{2.1}
$$

置 $x=d_B,y=d_C$。原 $E_0=0$ 给
$$
y=x+\frac{q-1}{2},\quad a=1+c(q-1),
$$
$$
r=x-a-ct,\quad s=y-aq+cqt,\quad
A_1=2f-2bx-2cy+2bct.                                  \tag{2.2}
$$
令
$$
A_B=t^2-(q+2x+1)t+2x(1-q),
$$
$$
A_C=t^2-2(q+x)t+(q-1)(q-1+2x).
$$
全部剩余 mean 恰为
$$
E_B=cA_B+4(x-1)f-2x^2+2x-1,
$$
$$
E_C=-cqA_C+(4x-2q-2)f-2x^2+2x-\frac{q^2+1}{2},         \tag{2.3}
$$
$$
\begin{aligned}
E_1={}&c^2q[-(q-1)^2+t(q+3-4x)]
 +2cf(q-1)(2x-1)\\
 &+\tfrac12c(q-1)(4x^2-4x-q+1)+8f^2.                  \tag{2.4}
\end{aligned}
$$
尤其 (2.3) 是关于 $c,f$ 的完整线性系统。定义
$$
L=\begin{pmatrix}A_B&4(x-1)\\-qA_C&4x-2q-2\end{pmatrix},
\quad w=\begin{pmatrix}2x^2-2x+1\\2x^2-2x+(q^2+1)/2\end{pmatrix},
\quad D=\det L,
$$
$$
F=qx-q+2x^2-x.
$$
Cramer 的第一列分子精确为
$$
\det(w,L_{\bullet,2})=-2(q-1)F.                       \tag{2.5}
$$
因此在 $D\ne0$ 上定义准确的有理函数
$$
c_*=-\frac{2(q-1)F}{D},\qquad
f_*=\frac{\det(L_{\bullet,1},w)}{D}.                   \tag{2.6}
$$
在此图内，$c\ne0$ 又强制 $F\ne0$。以下先处理 $t=0$ 和 $D=0$ 的全部例外，才使用 (2.6) 的一般图。

## 3. 完整边界 $t=0$

### 3.1 $D\ne0$

直接由 (2.3) 得
$$
D=4(q-1)^2F,\quad c=-\frac1{2(q-1)},\quad f=\frac{2x-1}{4}.
$$
原 $c_0$ 是
$$
c_0=-\frac{3q^2(2x-1)^2}{128}.
$$
所以 $x=1/2$。此时原 $A_1=r=s=t=0$，并且
$$
P_B=P_C=P_1=0,\qquad P_0=-q(q+1)/4\ne0.
$$
原 (1.1) 迫 $u_B=u_C=u_1=0$、$u_0\ne0$。活跃 Gram 只有秩二，且 $U=(u_0,0,0,0)=u_0K_Be_B$、$e_B^TK_Be_B=0$。完整 Gram 因而仍只有秩二，违反原长度五 jets 在原六维非退化形式下的秩至少四。

### 3.2 $D=0$

由 (2.5) 必须 $F=0$。因 $F(1)=1$，有 $x\ne1$，可写
$$
q=\frac{x(1-2x)}{x-1}.                                \tag{3.1}
$$
(2.1) 等价地排除了
$$
x=0,\tfrac12,1,\qquad
Q_1=2x^2-1=0,\qquad F_a=2x^2-2x+1=0.                  \tag{3.2}
$$
用 $E_B=0$ 解 $f$，除数为 $4(x-1)\ne0$。代入 $E_1$ 得
$$
E_1=\frac{F_a(4cx^2-2c-x+1)
 (4cx^3-2cx-2x^3+4x^2-3x+1)}{2(x-1)^4}.              \tag{3.3}
$$
第一因子已由 (3.2) 排除。若第二因子为零，则 $c=(x-1)/(2Q_1)=-1/[2(q-1)]$，回到上一小节的原相容式，强迫已禁止的 $x=1/2$。

若第三因子为零，则
$$
c=\frac{(x-1)F_a}{2xQ_1}.                             \tag{3.4}
$$
将 (3.1)、(3.4) 和原 $E_B=0$ 所给的 $f$ 代回原 $c_0,\Gamma_0$。化简有理分式后取分子，其 $\mathbb Q[x]$ 最大公因子除非零常数外恰为
$$
(2x-1)^3F_a^2.
$$
所有根都在 (3.2) 中，所以这一分支也为空。这里没有在 $D=0$ 上使用 Cramer 的有理公式。

## 4. 完整边界 $D=0,t\ne0$

仍由 (2.5) 得到 (3.1)、(3.2)。把 (3.1) 代入 $D$，精确因子化为
$$
D=-\frac{2t(2x-1)}{(x-1)^2}
 \left[t(x-1)Q_2+L_x\right],
$$
$$
Q_2=2x^2-4x+1,\qquad L_x=4x^4-4x^3-2x+1.
$$
$Q_2=0$ 时，$L_x$ 的余式为 $8x-2$，两者无共同根；而 $x=1$ 已被排除。因此
$$
Q_2\ne0,\qquad t=-\frac{L_x}{(x-1)Q_2}.               \tag{4.1}
$$
用原 $E_B=0$ 解出 $f$，除数仍是 $4(x-1)\ne0$。

把 (3.1)、(4.1) 和这个 $f$ 代入原 $E_1$。其分子是 $F_a$ 乘一个关于 $c$ 的二次式 $E_*(c,x)$，除非零常数外没有其他关于 $c$ 的因子。$F_a\ne0$，故必须 $E_*=0$。以同一代入构造原 $c_0,\Gamma_0$ 的分子，并仅除掉其已知非零的 $c$ 次幂，记为 $C_*,G_*$。全部多项式由 (1.2)、(1.3)、(2.2)–(2.4)、(3.1)、(4.1) 唯一确定，源码直接生成。精确因子清单为 $\operatorname{num}(E_1)\doteq F_aE_*$：唯一被舍去的纯 $x$ 因子是一次 $F_a$，不存在另一个未处理的纯 $x$ 纤维。

在 $\mathbb Q[x]$ 中，两个原结式
$$
\operatorname{Res}_c(E_*,C_*),\qquad
\operatorname{Res}_c(E_*,G_*)
$$
次数分别为 $63,94$，最大公因子除非零常数外精确为
$$
\boxed{x^5(2x-1)^8Q_2^8.}                             \tag{4.2}
$$
每个因子已经在 (3.2) 或 (4.1) 中排除。因此完整 $D=0,t\ne0$ 支路没有原解，结果式首项系数退化也没有留下未核的允许值。

## 5. 一般图的完整原生 QQ 消元

现在才使用
$$
D\,t\,q(q-1)(q+1)F\ne0                              \tag{5.1}
$$
及 (2.6)。所有下列多项式都通过同一 (2.2) 原 Gram 和第 1 节原 $P,N,E$ 重建；没有把 $U$ 换成自由范数参数。

对有理式，先约去其分子与分母的公因子，再取分子；非零有理常数不影响以下零集与次数。代入 $c_*,f_*$ 后，精确因子为
$$
\operatorname{num}(E_1)\doteq t(q+1)M,
$$
$$
\operatorname{num}(c_0)\doteq q^2(q-1)^4F^2C,
$$
$$
\operatorname{num}(\Gamma_0)\doteq q^2(q-1)^6F^3V,
\qquad B_*:=\operatorname{num}(\Gamma_B).              \tag{5.2}
$$
符号 $\doteq$ 仅表示相差一个非零有理常数。这些多项式按 $(t,x,q)$ 的次数依次为
$$
(3,6,5),\quad(4,6,7),\quad(7,9,12),\quad(13,21,20).
$$
(5.1) 已证明被除去的每个因子非零，所以原解必须
$$
M=C=V=B_*=0.                                          \tag{5.3}
$$

第一轮在 $\mathbb Q[x,q]$ 中对 $t$ 求原结式，并仅除以下已证明非零的因子：

| 原结式 | 精确除去的因子 | 所得多项式 | $(x,q)$ 次数 |
|---|---|---|---|
| $\operatorname{Res}_t(M,C)$ | $q^2(q-1)^4F^6$ | $R_1$ | $(21,19)$ |
| $\operatorname{Res}_t(M,V)$ | $q^7(q-1)^6(q+1)F^9$ | $R_2$ | $(34,30)$ |
| $\operatorname{Res}_t(C,V)$ | $q^6(q-1)^{12}(q+1)^8F^{12}$ | $R_3$ | $(35,34)$ |
| $\operatorname{Res}_t(M,B_*)$ | $q^{10}(q-1)^{24}F^{18}$ | $R_B$ | $(64,49)$ |

所有除法均在原生 $\mathbb Q[t,x,q]$ 中精确完成；源码核对全部幂次和所得次数。尤其 $R_3$ 里的 $(2x-1)^2$ **被保留**，因为此时尚未假定 $x\ne1/2$。

第二轮在 $\mathbb Q[x]$ 中构造
$$
S_2=\operatorname{Res}_q(R_1,R_2),\quad
S_3=\operatorname{Res}_q(R_1,R_3),\quad
S_B=\operatorname{Res}_q(R_1,R_B).
$$
其真实次数分别为
$$
879,\qquad1020,\qquad1637.
$$
三个多项式的精确首一最大公因子为
$$
\boxed{\gcd(S_2,S_3,S_B)=(x-\tfrac12)^{362}.}          \tag{5.4}
$$
这一步完全在特征零有理数域上计算。未加入 $\Gamma_B$ 时，前两个结式还留下一个 $58$ 次因子；原最高式在零点给出的 $\Gamma_B$ 把该因子完整排除。没有把前两个结式的有限候选直接宣称为空。

每个真正原解使第一轮全部结式为零；由于移除的因子非零，$R_1,R_2,R_3,R_B$ 也全为零。于是三个第二轮结式都为零，(5.4) 只留下 $x=1/2$。结果式只用于共同有限根的必要条件；所有降次造成的额外根也被 (5.4) 和下一节完整纤维覆盖。

## 6. 最后纤维 $x=1/2$ 的原方程排除

直接回到 (2.3)，令
$$
H=2t^2-3(q+1)t+(q-1)^2.
$$
原两个单点 mean 给
$$
c=-\frac{q-1}{2H},\qquad
f=\frac{t(q^2-qt+4q-t+1)}{4H}.                         \tag{6.1}
$$
$H=0$ 时，同一两式的差强迫 $q=1$，故 $H\ne0$，不存在被 (6.1) 删除的零分母情况。

将 (6.1) 代入原 $E_1,c_0,\Gamma_0$，精确因子身份为
$$
E_1=\frac{t(q+1)M_h}{2H^2},\qquad
c_0=\frac{3q^2t(q-1)^4(q+1)C_h}{64H^4},
$$
$$
\Gamma_0=\frac{q^3t(q-1)^6(q+1)^2V_h}{2048H^6}.
$$
$M_h,C_h,V_h$ 关于 $t$ 的次数分别为 $3,3,6$。所以被舍去的关于 $t$ 的一次因子仅为一次 $t$，其余只含已经在 (5.1) 中证明非零的 $q,q-1,q+1$；没有遗漏另一条线性 $t$ 纤维。其两个精确结式为
$$
\operatorname{Res}_t(M_h,C_h)
=16q^4(q-1)^2(q+1)^3(22q^2-31q+22),
$$
$$
\begin{aligned}
\operatorname{Res}_t(M_h,V_h)
=64q^6(q-1)^4(&139656q^8+561550q^7-1914519q^6-32218q^5\\
&+2511238q^4-32218q^3-1914519q^2+561550q+139656).
\end{aligned}
$$
最大公因子首一化后恰为 $q^4(q-1)^2$，与 (2.1) 矛盾。于是 (5.4) 的最后纤维也全部排除。

## 7. 完整范围与实际可复算源

$t=0$、$D=0,t\ne0$、$Dt\ne0$ 三种情况穷尽 (2.1)，每个可能分母为零的例外都先独立处理。结合已登记的 $q=1$ 零总权稿、$q=-1$ 相反配对稿，$p=1,d_0=b+cq=0$ 全部为空。此前零配对稿已排除不能作这一归一的情形，因此原完整单位 $2+1+1$、孤立零点分支必须满足 $pq(bp+cq)\ne0$。

配套[自含 QQ 源](../notes/2026-11-26-unit-two-plus-one-plus-one-zero-base-mean-347c.py)从原 Frobenius 代数重建全部公式，核验两类 Cramer 奇异支、一般图和最终 $x=1/2$ 纤维；不重跑已登记的 $q=\pm1$ 支。依赖为 Python 3.12.14、SymPy 1.14.0、python-flint 0.9.0。一般图使用原生多元有理分式运算、真正 QQ 结式与精确 gcd；计算多项式仅留内存，不保存数组。

额外的[小型因子清单源](../notes/2026-11-26-unit211-zero-base-mean-factor-ledger-347c.py)独立从原式核对第 4 节唯一纯 $x$ 因子及第 6 节三个完整因子身份，没有重跑大结式，也没有改动主源的已执行字节。

实际执行命令、源码 SHA256、输出 SHA256、耗时与峰值内存见[主执行回执](../notes/2026-11-26-unit-two-plus-one-plus-one-zero-base-mean-execution-347c.json)及[因子清单回执](../notes/2026-11-26-unit211-zero-base-mean-factor-ledger-execution-347c.json)。主源213.188311秒、124784 KiB；小源5.079883秒、53652 KiB，两者exit0。正文几何秩矛盾使用同一原物理 jets，并不将自由 Gram 候选当作真实原曲线。这里仍未从临界支消失跳到全局根式成员性或任意普通 Hilbert 算子不变子空间的结论。
