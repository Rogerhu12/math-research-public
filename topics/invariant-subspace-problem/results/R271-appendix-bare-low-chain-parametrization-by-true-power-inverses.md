# R271 附录：原裸低链的首段参数化与真幂 MP 度量

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_continue。

状态：**已证明。** 本文在[首段先消元](R239-appendix-boundary-first-elimination-small-sources-and-exact-return-energy.md)的原完整旗中，准确参数化整个裸低链核。参数只有第一段；各后段使用真正的删除幂 Moore--Penrose 逆，而不是顺次单步逆。由此给出原裸源 Gram 的首段公式，并把高出生返回写成真幂逆的相容缺陷。尚未控制高返回逆费用，亦未得到三 Gram 上界。

## 1. 原完整旗和真幂逆

固定原 $m\ge5$、$d=2^m$、$4d\le q\le e^{d^3/4}$，写 $A=A_m,D=D_m$，
$$
E_{h,p}=\ker(D^h|_{\mathcal H_p}),\qquad E_{0,p}=\{0\}.
$$
完整右输入及内部输出为
$$
\mathscr C_{q,t}=\bigoplus_{i=0}^{d-t}e_iE_{d-i,q+t}
\quad(1\le t\le d),
$$
$$
\mathscr Y_{q,t}=\bigoplus_{i=0}^{d-t-1}e_iE_{d-i-1,q+t}
\quad(1\le t<d).
$$
内部算子是 $(Sc)_t=Ac_t+Dc_{t+1}$；最右端 $Ac_d=0$ 已由显示的头旗自动满足。首源是 $Fc=Dc_1$，其完整范围为
$$
\mathscr R_q=\bigoplus_{i=0}^{d-2}e_iE_{d-i-1,q}.
$$

沿原相对出生数 $a=t-h+1$，低输入和高输出的逐段形式准确为
$$
\boxed{
\mathscr X_{L,q,t}
=\bigoplus_{i=0}^{d-t}e_i
\left(E_{d-i,q+t}\ominus E_{t-1,q+t}\right),
}
\tag{1.1}
$$
$$
\boxed{
\mathscr Y_{H,q,t}
=\bigoplus_{i=0}^{d-t-1}e_i
E_{\min\{d-i-1,t-1\},q+t}.
}
\tag{1.2}
$$
(1.1) 中 $d-i\ge t$，所以被减去的核确实包含在大核中。原低链核为
$$
Z_q=\ker S_L
=\{a\in\mathscr X_{L,q}:Sa\in\mathscr Y_{H,q}\}.
\tag{1.3}
$$
特别第1段低输入就是整个首段联合旗
$$
\mathscr X_q:=\mathscr C_{q,1}
=\bigoplus_{i=0}^{d-1}e_iE_{d-i,q+1}.
\tag{1.4}
$$

原尾所有固定有限孔层的删除幂均满射且有有界右逆；例如[有限—连续尾归约 §3](R271-appendix-universal-adjacent-height-constants-finite-models-and-continuous-tail.md)给了完整证明。故对 $0\le j\le d-1$ 可定义
$$
U_j=(D^j|_{\mathcal H_{q+1+j}})^\dagger:
\mathcal H_{q+1}\longrightarrow\mathcal H_{q+1+j},\qquad U_0=I.
\tag{1.5}
$$
它满足
$$
D^jU_j=I,\qquad
\operatorname{Ran}U_j\perp\ker D^j.
\tag{1.6}
$$
这里的逆先在整个孔层取，再使用显示的原源或联合旗；没有先压缩 Gram 再取逆。$U_j$ 只作用于尾，因此与全部原头矩阵交换。

## 2. 整个低链恰由第一段唯一确定

**定理。** 定义
$$
\boxed{
(\mathcal T_qx)_t=(-1)^{t-1}U_{t-1}A^{t-1}x,
\qquad 1\le t\le d,\quad x\in\mathscr X_q.
}
\tag{2.1}
$$
则 $\mathcal T_q:\mathscr X_q\to Z_q$ 是有界双射，其逆就是取第一段。它保留原全部逐头旗和物理范数，并且
$$
F\mathcal T_qx=Dx.
\tag{2.2}
$$

先证唯一性。取 $a\in Z_q$，置 $x=a_1$。由 (1.2)，内部残量
$$
e_t=Aa_t+Da_{t+1}
$$
满足 $D^{t-1}e_t=0$。因此
$$
D^ta_{t+1}=-A D^{t-1}a_t.
$$
从 $a_1=x$ 归纳，准确得到
$$
D^{t-1}a_t=(-A)^{t-1}x.
\tag{2.3}
$$
又 (1.1) 给 $a_t\perp\ker D^{t-1}$。由真正幂逆的唯一最小性质，(2.3) 迫出 (2.1)。没有把 $Da_{t+1}$ 错写成在整个空间都等于 $-Aa_t$；其高出生差已经保留。

再证任意 $x\in\mathscr X_q$ 都给合法低链。$A^{t-1}$ 只把头指标 $\ell$ 降到 $i\le\ell-t+1$，所以 (2.1) 的头指标至多为 $d-t$。对给定输出头 $i$，来自头 $\ell\ge i+t-1$ 的输入 $x_\ell$ 被 $D^{d-\ell}$ 杀去。提升 $t-1$ 次后，由
$$
D^{t-1}U_{t-1}=I
$$
可知该项被 $D^{d-\ell+t-1}$ 杀去，而
$d-\ell+t-1\le d-i$。所以输出确在 $E_{d-i,q+t}$。再用 (1.6)，它也与 $E_{t-1,q+t}$ 正交。因此各段都属于 (1.1)。

内部残量仍在原 $\mathscr Y_{q,t}$：$A$ 降低头指标，$D$ 降低一个尾核阶。由 (2.3)，
$$
D^{t-1}(A(\mathcal T_qx)_t+D(\mathcal T_qx)_{t+1})=0.
$$
它因而还属于 (1.2)，正是 $S_L\mathcal T_qx=0$。第一段为 $x$，所以映射单射且取首段为逆；上一段的唯一性给满射。所有和与使用的孔层数都有限，各 $U_j$ 有界，故映射有界。证毕。

## 3. 原裸费用与源 Gram 的首段公式

在 $\mathscr X_q$ 的原内积中定义
$$
\boxed{
M_q=\mathcal T_q^*\mathcal T_q
=\left. P_{\mathscr X_q}
\left[\sum_{j=0}^{d-1}(A^j)^*(U_j^*U_j)A^j\right]
\right|_{\mathscr X_q}\succeq I.
}
\tag{3.1}
$$
投影表示真正限制后的伴随；不要求大括号保持 $\mathscr X_q$。记
$$
D_X=D|_{\mathscr X_q}:\mathscr X_q\to\mathscr R_q.
$$
该映射满射：任意 $r\in\mathscr R_q$ 的单步最小原像 $D^\dagger r$ 逐头属于 (1.4)。因此
$$
\boxed{
\alpha_q(r)^2
=\min_{\substack{x\in\mathscr X_q\\D_Xx=r}}
\langle M_qx,x\rangle.
}
\tag{3.2}
$$
这是原 $Z_q$ 中的裸最小链，与更宽或更窄的链空间无关。若
$$
K_q=D_XM_q^{-1}D_X^*,
$$
则 $K_q$ 在整个 $\mathscr R_q$ 上严格正、有有界逆，且
$$
\boxed{
J_{{\rm bare},q}=K_q,
\qquad x_r=M_q^{-1}D_X^*K_q^{-1}r,
\qquad a_q(r)=\mathcal T_qx_r.
}
\tag{3.3}
$$
例如严格正性可由 $M_q\preceq\|M_q\|I$ 以及 $D_X$ 的有界右逆直接得到。这只是固定 $m,q$ 的合法性，不宣称 $\|M_q\|$ 温和。

若希望只消去首段的自由 primitive 部分，令
$$
\mathscr K_q^{(1)}=\ker D_X
=\mathbb C^d\otimes K_{q+1},\qquad
x_0=D_X^\dagger r,
$$
则所有首段可行点是 $x_0+\mathscr K_q^{(1)}$。将 $M_q$ 在
$\mathscr K_q^{(1)}\oplus(\mathscr K_q^{(1)})^\perp$ 上作真正 Schur 补，便给 (3.2) 的另一表达。首段 primitive 自由坐标一般不为零，不能因为 $x_0$ 是普通最小原像就把它们删掉。

## 4. 高出生返回准确是真幂逆的相容缺陷

对 $1\le t<d$，令
$$
\boxed{K_t=DU_t-U_{t-1}:\mathcal H_{q+1}\to\mathcal H_{q+t}.}
\tag{4.1}
$$
由 (1.6)，
$$
D^{t-1}K_t=0,\qquad
P_{(\ker D^{t-1})^\perp}DU_t=U_{t-1},
\qquad K_1=0.
\tag{4.2}
$$
对每个输入 $g$，(4.2) 是同一个原空间中的正交分解，所以
$$
\boxed{
\|DU_tg\|^2=\|U_{t-1}g\|^2+\|K_tg\|^2.
}
\tag{4.3}
$$
不假定 $DU_t=U_{t-1}$。

将 (2.1) 代入完整内部输出，得到
$$
\boxed{
(S\mathcal T_qx)_t=(-1)^t A^tK_tx,
\qquad 1\le t<d.
}
\tag{4.4}
$$
它已经属于 $\mathscr Y_{H,q,t}$。因此原返回算子
$B_q=P_{\mathscr Y_H}S|_{Z_q}$ 在首段坐标中恰为
$$
\boxed{B_q\mathcal T_qx=\bigl((-1)^t A^tK_tx\bigr)_{t=1}^{d-1}.}
\tag{4.5}
$$
没有删掉任何高出生源，也未把它换成旧有效源或非同源的环境向量。

(4.3) 还给逐段能量等式
$$
\|(S\mathcal T_qx)_t\|^2
=\|D(\mathcal T_qx)_{t+1}\|^2
-\|A(\mathcal T_qx)_t\|^2.
\tag{4.6}
$$
求和便得原返回算子的直接范数预算
$$
\|B_q\mathcal T_qx\|^2
\le\|D_m\|^2\sum_{t=2}^d\|(\mathcal T_qx)_t\|^2
\le\|D_m\|^2\langle M_qx,x\rangle.
\tag{4.7}
$$
(4.7) 不控制回到高链时要使用的逆 Gram；故不能把小返回源范数直接认作小完整修复费用。

## 5. 对同一个源的全部真幂最小逆下界

对任意 $a\in Z_q$、$Fa=r$，(2.3) 再施加一次 $D$，给
$$
D^ta_t=(-A)^{t-1}r.
$$
由每段最小范数性质及段间物理正交性，原裸费用满足
$$
\boxed{
\alpha_q(r)^2\ge
\sum_{t=1}^{d-1}
\left\|(D^t|_{\mathcal H_{q+t}})^\dagger A^{t-1}r\right\|^2.
}
\tag{5.1}
$$
第 $d$ 项的源是 $A^{d-1}r=0$，故省去。该式可直接用于完整原源，不先假定 $r$ primitive。

它不提供顺次单步 MP 链的相同比较。顺次 MP 与真幂 MP 的范数比即使在三正权、primitive 真空、两步情形也可发散；见[三权范围澄清笔记](../notes/2026-11-13-three-weight-sequential-versus-power-mp-obstruction-1cf.md)。本文 (2.1)、(3.1)、(4.1) 的所有逆均是真幂逆，且首段仍做完整原旗内的约束最小化。

真正剩余的问题是：结合 (3.2) 的首段最小者与原左完整源度量，控制 (4.5) 经原高链逆 Gram 后的费用。本文只建立准确接口；不从真幂 Gram 的相邻估计自动推断顺次链比较，亦不声称已达到原 $C_m=O(e^{d^3/4}/d)$ 的求和门槛。
