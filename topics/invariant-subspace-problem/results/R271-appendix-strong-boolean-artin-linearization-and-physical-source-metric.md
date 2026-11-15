# 强 Boolean 块的精确 Artin 线性化、真实源度量与固定 forcing 的反向费用

日期：2026-11-15。作者：literature_audit / 789f。

**状态：已证明的有限代数交织与物理范围。** 本文把 $\psi_m(A_m+E)$ 中的全部强位混合项放入一个明确可逆的有限代数替换；没有把它直接等同于 $B_m+d_0E$。替换有真实双向物理表示，并能运输完整左、右及裸商的来源。然而其物理度量不能删去：原 $N$ 模型中，一个固定一阶真空 forcing 的反向列已经有四次指数下界。因此后续仍必须保完整 Schur，不能由代数可逆性或正向固定该 forcing 推出所需的统一预算。

## 1. 原加权代数与全高度截断

取原头 $d=2^m$、$A_m=F_m(B_m)$，其中 $F_m$ 是原 $N$ 或 $Y$ 有限函数，
$$
F_m(0)=0,\qquad F_m'(0)=d_0^{-1},\qquad d_0=e^{-20}.
$$
记其形式逆为 $\psi_m$。在本节，所有复合均发生在有限 Artin 代数
$$
\mathcal A=\mathbb C[x,y_1,\ldots,y_R]/(x^d,y_1^2,\ldots,y_R^2)
$$
中。令
$$
E=\sum_{i=1}^R a_i y_i,\qquad a_i>0,\qquad h=d+R.
$$
极大理想的 $h$ 次幂为零。因此 $\psi_m$ 以及 $Y$ 型有理函数的代入均使用其完整 Taylor 系数直到 $h-1$；这里不能只保旧头的 $d-1$ 阶。

定义单位元
$$
v(E)=\frac{\psi_m(E)}{d_0E},\qquad v(0)=1,
$$
以及
$$
x'=\psi_m(F_m(x)+E)-\psi_m(E),\qquad
y_i'=y_i v(E).
\tag{1.1}
$$
$x'$ 可被 $x$ 整除，而且 $x'/x$ 的常数项为一；故 $(x')^d=0$。
各 $(y_i')^2=0$。所以 (1.1) 给出 $\mathcal A$ 的代数自同态 $\alpha$。

在极大理想模其平方上，$\alpha$ 是恒等。这已经由有限维逐次回代保证可逆。更明确地，若
$$
E'=\sum_i a_i y_i'=\psi_m(E)/d_0,
$$
则逆替换为
$$
\boxed{
E=F_m(d_0E'),\qquad
y_i=y_i'\frac{F_m(d_0E')}{E'},\qquad
x=\psi_m\!\left(F_m(x'+d_0E')-F_m(d_0E')\right).
}
\tag{1.2}
$$
两个商在零点均按其单位 Taylor 延拓理解；第二个 $x$ 表达式可被 $x'$ 整除。把 (1.2) 代回 (1.1)，使用 $F_m\circ\psi_m=\psi_m\circ F_m=\mathrm{id}$ 的有限形式恒等，即得到双向恒等。

特别
$$
\boxed{\alpha(x+d_0E)=\psi_m(F_m(x)+E).}
\tag{1.3}
$$
这是精确消去强位混合的方式；代价随后全部进入物理相似的 Gram。

## 2. 真实 $W_n$ 度量下的双向实现

用原物理头基记
$$
B_me_n=\frac{W_n}{W_{n-1}}e_{n-1},\qquad W_0=1.
$$
令 $\Omega$ 是头与强位的共同真空。creation 正则表示是
$$
\mathcal J(x^n y_I)
=(B_m^*)^n\prod_{i\in I}E_i^*\Omega
=W_n e_n\otimes e_I.
\tag{2.1}
$$
因而 $\mathcal A$ 的单项式范数为 $W_n$，而不是一。所有 $W_n$ 都保留在这一个物理表示中。

置
$$
\mathcal S=\mathcal J\alpha\mathcal J^{-1},
\qquad V=\mathcal S^{-*},
$$
并在完整物理头加全部强位上记
$$
C=A_m+E_{\mathrm{phys}},\qquad
L=B_m/d_0+E_{\mathrm{phys}},
\qquad E_{\mathrm{phys}}=\sum_i a_iE_i.
$$
所有原函数系数均为实数，故由 (1.3) 及伴随得到
$$
\boxed{
VLV^{-1}=\frac{\psi_m(C)}{d_0}.
}
\tag{2.2}
$$
再令
$$
\Phi(z)=F_m(d_0z)=zJ(z),\qquad J(0)=1.
$$
$J(L)$ 是可逆单位多项式，并与 $L$ 交换。因此
$$
\boxed{C=V L J(L)V^{-1}.}
\tag{2.3}
$$
这同时给全部真实幂旗
$$
\ker C^k=V\ker L^k,\qquad
\operatorname{Ran}C^k=V\operatorname{Ran}L^k.
\tag{2.4}
$$
没有假设 $V$ 为酉或具有与 $m,R$ 无关的条件数。

还可保留逐位旗：$\alpha(x)=x$ 乘一个单位，
$\alpha(y_i)=y_i$ 乘一个单位，
$\alpha(E)=E$ 乘一个单位。所以相应 $B_m$、各 $E_i$ 及 $E_{\mathrm{phys}}$ 的幂核旗也由该交织准确保持。这里的“保持”是线性子空间意义，不是保持其原正交补或最小逆。

## 3. 固定强真空 forcing 的正反方向不同

对任何头向量 $f$，设 $f_\Omega=f\otimes\Omega_{\mathrm{strong}}$。
因为每个 $\alpha(y_i)$ 可被 $y_i$ 整除，而在 $E=0$ 时
$\alpha(x)=\psi_m(F_m(x))=x$，creation 代数替换的真空输出行准确为恒等。故
$$
\mathcal S^*f_\Omega=f_\Omega,\qquad
(\mathcal S^{-1})^*f_\Omega=f_\Omega,
$$
也即
$$
\boxed{Vf_\Omega=V^{-1}f_\Omega=f_\Omega.}
\tag{3.1}
$$
但一般
$$
V^*f_\Omega=\mathcal S^{-1}f_\Omega\ne f_\Omega.
\tag{3.2}
$$
后者正是完整核 Schur 使用的 forcing，不能用 (3.1) 替换它。

具体地，令 $K=\ker L$，$\iota:K\hookrightarrow\mathcal H_{\mathrm{phys}}$ 是物理包含，记
$$
G=\iota^*V^*V\iota>0,\qquad
c_f=\iota^*V^*f_\Omega.
$$
则完整正交核投影为
$$
\boxed{
P_{\ker C}f_\Omega=V\iota G^{-1}c_f,\qquad
\|P_{\ker C}f_\Omega\|^2=\langle G^{-1}c_f,c_f\rangle.
}
\tag{3.3}
$$
这个源与这个 Gram 必须一起保留。虽然 $c_f$ 的未压缩列可能很大，
(3.3) 的能量仍至多 $\|f_\Omega\|^2$；反过来，后一个平凡上界没有支付 Green 列。

若 $Q_C=P_{\ker C^*}$，完整伴随最小逆的准确因式为
$$
\boxed{
(C^*)^\dagger f_\Omega
=(I-Q_C)V^{-*}(L^*)^\dagger
J(L)^{-*}V^*(I-P_{\ker C})f_\Omega.
}
\tag{3.4}
$$
确实 $V^*(I-P_{\ker C})f_\Omega\perp K$，且 $J(L)^{-1}K=K$，
所以 $(L^*)^\dagger$ 的实际输入属于 $\operatorname{Ran}L^*$。
逐因子代回 (2.3) 给正确方程；最外面的 $I-Q_C$ 保证最小性。
这里没有把任何 Moore–Penrose 逆穿过非酉相似。

## 4. 左、右及裸商的完整来源运输

另有一个与上述强头交换的实际远尾删除 $D$。为了说明源的变化，先写出完全代数的有限链运输；其费用仍使用以下列出的真实行度量。

若线性头 $L$ 的完整右链为 $c_1,\ldots,c_h$，满足
$$
Dc_1=r_0,\qquad Lc_j+Dc_{j+1}=0,\qquad Lc_h=0,
$$
则
$$
b_j=VJ(L)^{j-1}c_j
\tag{4.1}
$$
满足原头 $C$ 的全部右链方程，其来源准确为
$$
Db_1=Vr_0.
$$
最后一行和全部自然头幂旗由 (2.4) 保留。头算子 $VJ(L)^{j-1}$ 与远尾 $D$ 交换，所以各段的远尾高旗
$\ker D^{j-1}$ 也被双向映射。因而完整右域、零源域及裸商都得到双向来源映射；不能据此把它们的物理正交投影也视为不变。

类似地，线性头左链 $c_0,\ldots,c_p$ 若满足低行
$Lc_j+Dc_{j+1}=0$、顶部来源 $r_0=Lc_p$，则
$$
v_j=VJ(L)^{j-p-1}c_j
\tag{4.2}
$$
是原头的合法左链，且 $Cv_p=Vr_0$。负次幂因 $J(L)$ 可逆而合法。

这些公式使用所有强位及所有完整链段，不引入 $D^\dagger$。
但是每一行的真实度量都变为
$$
J(L)^{*a}V^*VJ(L)^a
$$
（$a$ 是该行实际指数）。完整最小化与全部零源 Schur 必须在这些度量中进行。
没有估计它们之前，(4.1)–(4.2) 不给原两费与线性两费的统一比较。

## 5. 原 N 模型的固定一阶反向列已含四次指数

本节只用原 $N$ 模型，
$$
F_m(z)=\sum_{i<m}b_i z^{2^i}/d_i,
\qquad b_i=(i+1)^{-2}.
$$
取固定物理 forcing
$$
f_1=e_1\otimes\Omega_{\mathrm{strong}}.
$$
从逆替换 (1.2) 中取关于 $x$ 的一次项，严格得到
$$
\alpha^{-1}(x)
=x\,d_0F_m'(d_0E)+O(x^2).
$$
因此，保实际 $W_1=d_0$ 后，
$$
\boxed{
P_{\mathrm{head}=1}\mathcal S^{-1}f_1
=e_1\otimes d_0F_m'(d_0E_{\mathrm{phys}}^*)\Omega_{\mathrm{strong}}.
}
\tag{5.1}
$$
这里逆芽的高阶系数已经在一次头系数中准确消掉，但剩下的原 $F_m'$ 系数仍须付费。

令 $q=2^{m-1}=d/2$。最高原头位在 (5.1) 的强位次数 $q-1$ 中给
$$
\frac{q b_{m-1}d_0^q}{d_{m-1}}
(E_{\mathrm{phys}}^*)^{q-1}\Omega_{\mathrm{strong}}.
\tag{5.2}
$$
其他原位的强位次数不同，所以不能与 (5.2) 抵消。
若实际强块含 $q-1$ 个原连续尾位，其权均至少
$(m+q)^{-2}$，则选取这些位的一个实际物理单项式即得
$$
\|(E_{\mathrm{phys}}^*)^{q-1}\Omega_{\mathrm{strong}}\|
\ge\frac{(q-1)!}{(m+q)^{2q-2}}.
$$
原从 $m$ 附近开始的强前缀在 $R\ge q-1$ 时满足这个条件，端点编号平移一位也可直接放大分母而不改量级。故
$$
\boxed{
\|V^*f_1\|=\|\mathcal S^{-1}f_1\|
\ge
\frac{q b_{m-1}d_0^q}{d_{m-1}}\,
\frac{(q-1)!}{(m+q)^{2q-2}}.
}
\tag{5.3}
$$
代入真实权
$$
-\log d_{m-1}
=\frac{25}{4}d^4-\frac{105}{8}d^3+
\left(75m-\frac{125}{2}\right)d
$$
及 $(q-1)!\ge((q-1)/e)^{q-1}$，得到
$$
\log\|V^*f_1\|
\ge
\frac{25}{4}d^4-\frac{105}{8}d^3-O(d\log d).
\tag{5.4}
$$
特别，对任意固定 $K$，这个实际反向 forcing 列不能被
$\rho_m^{-K}$ 控制，其中 $\rho_m$ 是领先指数
$(25/2)d^3$ 的任一上述原安全芽半径。

(5.3) 是未压缩的 $V^*f_1$ 下界，不是 (3.3) 的 Schur 能量下界，
更不是原 Green 或普通右费用的反例。
本稿没有估计 $\iota^*V^*f_1$ 后再经 $G^{-1}$ 的共同抵消。
它准确排除的是：因为代数替换可逆、或因为 $V$ 正向固定了
$f_1$，就直接把反向 forcing 当作一个只有 $\rho_m^{-O(1)}$ 费用的列。

## 6. 与原目标的接口

与
[强尾源的精确收缩和圆盘演算](R271-appendix-first-row-observability-loss-exact-source-contraction-and-disk-calculus.md)
以及完整 Riordan 右域运输配合时，可以先把头函数改为 $\psi_m(C)/d_0$，
再用本文的实际 $V$ 将其形式上写成真正分级的 $B_m/d_0+E_{\mathrm{phys}}$。
全部强位混合现在准确记录在 $V^*V$、反向 forcing 和行权中，不再留作错误的直接等号。

真正未付的是这些对象在同一个原源、固定测试或完整 Green Schur 中的费用。
只估未压缩 $V$ 或 $V^*$ 已受到 §5 的实际列障碍；
只保形式分级而删除这个度量则改变了问题。原 $N=M$ 仍未完成。
