# R150 附录：单位 2+1+1 的最高基点值零支全部为空

日期：2026-11-26（UTC）。作者：Astra-ISP-347c-20261126；AI-assisted GPT-6 Astra Pro。

**状态：本条完整范围已证明。** 在原本质四维外均值、rankH4、单位 $2+1+1$ 加一个孤立零点的长度五分支中，完整临界点必须有最高基点值 $P_0\ne0$。本条证明以前未覆盖的一般非零配对，并引用已登记的零配对、零基点 mean、相等和相反配对结论，不重算这些已闭分支。最高值非零支、其他原除子型和普通 Hilbert ISP 仍继续。

## 1. 同一原物理除子、全部值和一阶 jet

沿用[原单位 2+1+1 模型](R150-appendix-essential-four-unit-two-plus-one-plus-one-one-zero-base-pairing-exclusion.md)，保同一长度五物理除子 $2A+B+C+Z$，以及它在原六维非退化型中的全部独立列。活跃 Frobenius 代数为
$$
\mathcal B=\mathbb C[\epsilon]/(\epsilon^2)\oplus\mathbb C\oplus\mathbb C,
\quad\tau(x)=a x_0+x_1+b x_B+c x_C,\quad a=1-b-c.
$$
由已闭[零配对](R150-appendix-essential-four-unit-two-plus-one-plus-one-one-zero-base-pairing-exclusion.md)、[零基点 mean](R150-appendix-essential-four-unit-two-plus-one-plus-one-zero-base-mean-exclusion.md)、[整个相等配对](R150-appendix-essential-four-unit-two-plus-one-plus-one-equal-base-pairings-complete-exclusion.md)、[整个相反配对](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-base-pairings-exclusion.md)，可且只需处理共同齐次规范
$$
K_B=\begin{pmatrix}0&0&1&q\\0&A_1&r&s\\1&r&0&t\\q&s&t&0\end{pmatrix},
\qquad bcq(q-1)(q+1)u\ne0,\qquad u=b+cq.
\tag{1.1}
$$
原孤立零点列记作 $U=(u_0,u_1,u_B,u_C)$，$m=\tau(U)$。完整 Gram 为
$$
\widehat K=\begin{pmatrix}K_B&U\\U^T&0\end{pmatrix},\qquad
\operatorname{rank}\widehat K\ge4.
\tag{1.2}
$$
这是原五维子空间在六维非退化型中的根空间维数至多一的后果。

记 $1=(1,0,1,1)$，$k_i$ 为原 $K_B$ 的行，并定义
$$
(D_Kx)_i=\tau(k_i x),\quad d=D_K1,\quad f=\tau(d)/2,
$$
$$
P(x)=\tfrac12\tau((x-\tau(x)1)^3),
$$
$$
N(x)=\tfrac12\tau((d-f1)x^2)-\tau(x)\tau(dx)+f\tau(x)^2
+\tfrac14\tau(xD_Kx).
\tag{1.3}
$$
原 active mean 是
$$
E=e-2D_Kd-2d^2+4fd=0,
\quad e=(\tau k_0^2,2\tau k_0k_1,\tau k_B^2,\tau k_C^2).
\tag{1.4}
$$
所有 $P_i,N_i$ 都是 (1.3) 在同一原行上的值或双点一阶 jet。原最高式、第二梯度以及零点自身的 mean 给
$$
(P_0,P_1,P_B,P_C)=(-u_0^3,-3u_0^2u_1,-u_B^3,-u_C^3),
$$
$$
(N_0,N_1,N_B,N_C)=(-mu_0^2,-2mu_0u_1,-mu_B^2,-mu_C^2),
\qquad \tau(U^2)=2m^2.
\tag{1.5}
$$
因此反设 $P_0=0$ 时，必须同时有
$$
u_0=P_1=N_0=N_1=0.
\tag{1.6}
$$
本稿不从有限必要方程反推原物理临界点存在。

## 2. 无遗漏的权重图和线性 mean 图

令 $\ell=b+c$，保可逆换元
$$
b=\frac{q\ell-u}{q-1},\qquad c=\frac{u-\ell}{q-1},
\quad x=d_B,\quad y=d_C,\quad X=\frac{bx+cqy}{u},\quad \zeta=x-y.
$$
原 $E_0=0$ 恰给
$$
x=X+\frac{cq\zeta}{u},\quad y=X-\frac{b\zeta}{u},\quad
f=\frac X2+\frac u2-\frac{b+cq^2}{4u},
$$
$$
r=x-(1-\ell)-ct,\quad s=y-q(1-\ell)-bt,\quad
A_1=2f-2bx-2cy+2bct.
\tag{2.1}
$$
此时定义
$$
J=2u^2-3(q+1)u+q^2+q+1,\qquad D=3u-q-1,
$$
有准确恒等式
$$
P_0=\frac{uJ+q\ell D}{2}.
\tag{2.2}
$$

若 $D=0$，则 $u=(q+1)/3$，(2.2) 成为
$$
P_0=\frac{(q+1)(q-2)(2q-1)}{54}.
$$
由于 $q+1\ne0$，只有 $(q,u)=(2,1)$ 或 $(1/2,1/2)$。这两张图在 §6 独立处理。

若 $D\ne0$，则
$$
\ell=-\frac{uJ}{qD},\qquad
b=-\frac{u(q-2u)(q-u)}{(q-1)D},\qquad
c=\frac{u(u-1)(2u-1)}{q(q-1)D}.
\tag{2.3}
$$
所以 $u-1,2u-1,q-u,q-2u$ 都非零。置
$$
H=q+1-2u.
$$
原 $P_1=N_0=0$ 对 $(X,\zeta)$ 是两个一次式，其系数行列式准确为
$$
-\frac{3u^2(q-2u)^3(q-u)(u-1)(2u-1)^3H}
{8q(q-1)D^4}.
\tag{2.4}
$$
因此 $H=0$ 是唯一尚需另付的线性图；由 (2.3)，它恰为 $\ell=1,b=c=1/2$，见 §7。

下文先令 $DH\ne0$。以 (2.1)、(2.3) 下原 $P_1,N_0$ 的 Cramer 唯一解定义 $X_*,\zeta_*$。分母只含上述已非零因子，配套源码准确重建并检验该解，而不是读取已消元数组。代回原 $N_1$ 后，仅除已非零因子，精确留下
$$
\boxed{tJL=0,}
\tag{2.5}
$$
$$
L=A_0+B_0t,\quad
A_0=(q-1)^2(q-2u)(2u-1),\quad
B_0=-u(2q^2-4qu+q-4u+2).
\tag{2.6}
$$
剩余三条 mean 的原分子记为 $M_1,M_B,M_C$；它们由 (1.4) 与该唯一代换完全定义，关于 $t$ 均至多二次。

## 3. $t=0$ 的抽象族由完整物理秩排除

在 $t=0$，从三条原 mean 分子中只除已非零因子，三者均为非零常数乘 $u-q-1$。因此
$$
u=q+1,\quad\ell=\frac12,\quad
b=-\frac{q+2}{2(q-1)},\quad c=\frac{2q+1}{2(q-1)}.
$$
原 Cramer 解为
$$
X_*=\frac{2q^2+3q+2}{4(q+1)},\qquad \zeta_*=-\frac{q-1}{2}.
$$
由 (2.1) 得 $A_1=r=s=t=0$。直接代回同一原式，四个 $P_i,N_i$ 全为零。于是 (1.5) 迫 $u_0=u_B=u_C=0$，而 $m=u_1$、$\tau(U^2)=0$ 又迫 $u_1=0$。

此时 $K_B$ 秩二、$U=0$，所以 $\widehat K$ 秩二，违反 (1.2)。本节没有把这个非空抽象 mean 族误称为代数空集。

## 4. $J=0$ 的全部 QQ 结式纤维

对每个 $M_i$ 先取模 $J$ 的 $u$ 余式，再只反复除与
$$
q(q-1)(q+1)u(u-1)(2u-1)(q-u)(q-2u)DH
\tag{4.1}
$$
的 gcd，得到 $J_1,J_B,J_C$。这保留所有当前图的原解。计算完整有理数结式
$$
R_B=\operatorname{Res}_u(\operatorname{Res}_t(J_1,J_B),J),\qquad
R_C=\operatorname{Res}_u(\operatorname{Res}_t(J_1,J_C),J).
$$
其 $q$ 次数为 $41,42$，最大公因子除非零有理常数外恰为
$$
\boxed{q^6(q-2)^8(q-1)^8(2q-1)^8(q^2+q+1)^3.}
\tag{4.2}
$$
所有结式均使用完整原多项式，未假设首项在特化后非零。

在 $q=2$，$J=(u-1)(2u-7)$；$u=1$ 已由 $c\ne0$ 排除，故只余 $u=7/2$。把它返回三个原 $M_i$，在 $\mathbb Q[t]$ 的 gcd 为非零常数。$q=1/2$ 同样只余 $u=7/4$，三个原分子也无共同根。

在 $q^2+q+1=0$，$J=u[2u-3(q+1)]$；$u\ne0$ 给 $u=3(q+1)/2$。代回三个原 mean，连同 $q^2+q+1$ 在 $\mathbb Q[t,q]$ 中的准确约化 Gröbner 基为 $\{1\}$。所以整个 $J=0$ 支为空。

## 5. $L=0$：先付一次系数，再返回全部末纤维

不能直接除 $B_0$。若 $B_0=0$，因 $u(q+1)\ne0$ 必有
$$
u=\frac{2q^2+q+2}{4(q+1)}.
$$
此时
$$
A_0=\frac{q(q-2)(q-1)^2(2q-1)}{4(q+1)^2}.
$$
要使 $L=0$，只能 $q=2$ 或 $1/2$，分别给已禁止的 $u=1$ 或 $1/2$。故本图 $B_0\ne0$，现在才令 $t=-A_0/B_0$。

将它代入三原 mean 分子，取约分后的分子，只除 (4.1) 与 $B_0$ 的因子，得 $L_1,L_B,L_C$。每个 $(u,q)$ 次数为 $(6,5)$。两个完整结式
$$
\operatorname{Res}_u(L_1,L_B),\qquad\operatorname{Res}_u(L_1,L_C)
$$
的 $q$ 次数均为 $31$，gcd 除非零有理常数外恰为
$$
\boxed{q^5(q-2)^6(2q-1)^6(25q^2-14q+25).}
\tag{5.1}
$$
在 $q=2$，三个 $L_i$ 的 $u$ gcd 为常数乘 $(u-1)^2$；在 $q=1/2$，为常数乘 $(u-1/2)^2$。两者均违反当前非零权。

在 $25q^2-14q+25=0$，三个 $L_i$ 连同该二次式在 $\mathbb Q[u,q]$ 中的准确约化基为
$$
\left\{u-\frac{q+1}{2},\quad q^2-\frac{14}{25}q+1\right\}.
\tag{5.2}
$$
第一式就是 $H=0$，违反本图假设；其原奇异图在 §7 独立排除。至此 $DH\ne0$ 全闭。

## 6. 奇异权重图 $D=0$

先取 $q=2,u=1$；此时 $b=2\ell-1,c=1-\ell$，所以 $\ell\ne1/2,1$。使用 (2.1) 的原坐标，$P_1,N_0$ 对 $(X,\zeta)$ 的行列式为
$$
-\frac38(\ell-1)(2\ell-1)^3\ne0.
$$
唯一解为
$$
X=\frac{16\ell^2t-4\ell^2-16\ell t+8\ell-3}{4\ell-2},\qquad
\zeta=\frac{8\ell t-2\ell-2t+1}{4\ell-2}.
$$
原 $N_1$ 准确为
$$
-2\ell t(\ell-1)(6\ell t-2\ell-t+1).
\tag{6.1}
$$
若 $\ell=0$，三个剩余 mean 分子可取
$$
2t-1,\quad-18t^2-8t+1,\quad t(t-1),
$$
其 gcd 为一。若 $t=0$，gcd 为常数乘 $2\ell-1$，也已排除。

最后令 $(6\ell-1)t-2\ell+1=0$。在 $6\ell-1=0$ 时余项为 $2/3$，故没有解；否则 $t=(2\ell-1)/(6\ell-1)$。三原 mean 分子约分后可取
$$
(2\ell-1)(128\ell^3-164\ell^2+12\ell-1),
$$
$$
64\ell^3-212\ell^2+148\ell-25,\qquad-32\ell^2(2\ell-1),
$$
其 gcd 为一。整个 $(q,u)=(2,1)$ 图为空。

交换 $B,C$，再将完整 $K_B,U$ 同乘 $1/q$，将规范参数变为 $q'=1/q,u'=u/q$。所有原 mean、最高式、第二梯度和物理秩均按共同齐次次数保持。因此该变换将 $(2,1)$ 与 $(1/2,1/2)$ 两图互换，后一张也全部排除；未单独改变某一条物理配对。

## 7. 半权图的原物理等向矛盾

这里 $b=c=1/2,a=0$。直接在原参数 $(A_1,r,s,t,q)$ 中同时使用 $E_0=P_1=N_0=0$，唯一要求是
$$
A_1=0,\qquad s=q(1-r).
$$
其余三条 mean 全等于
$$
-q(2r^2-2r+1).
$$
故 $2r^2-2r+1=0$，也就是 $r=(1+\iota)/2$、$\iota^2=-1$；两个根均保留。代回同一原 $P,N$，有
$$
P_0=P_1=N_0=N_1=0,\qquad
\boxed{P_B=2N_B,\quad P_C=2N_C.}
\tag{7.1}
$$
这些身份不限制 $t$，也不除以任何零点配对分量。

若 $m=0$，由 (1.5)、(7.1) 得 $u_B=u_C=0$，所以 $m=u_1$ 又迫 $u_1=0$。若 $m\ne0$，相同式子给
$$
u_i^2(u_i-2m)=0\quad(i=B,C),\qquad
\frac{u_B^2+u_C^2}{2}=2m^2.
$$
因此 $u_B,u_C$ 恰有一个为 $2m$、另一个为零。于是
$$
m=u_1+\frac{u_B+u_C}{2}=u_1+m,
$$
仍得 $u_1=0$。

现在 $A_1=u_0=u_1=0$，原双点值、双点一阶 jet 与孤立零点 $Z$ 三列的所有相互配对均为零。这给同一原曲线上的三维全等向支撑 $2A+Z$，与已完整证明的[原长度三等向 jet 分类](R150-appendix-classification-of-isotropic-length-three-curve-jets.md) §§3、5 矛盾。该分类包括所有有限点和无穷远，单位归一及可逆局部 jet 不改变全等向性。半权图全部排除。

## 8. 执行身份与准确推进范围

[自含原式 QQ 源](../notes/2026-11-26-unit211-general-zero-highest-347c.py)从同一 Frobenius 乘法、原 $K_B$ 和原 $E,P,N$ 重建全部消去；线性图后使用原生有理多变量算术，所有结式和数组只在内存中。它检查两张线性图的全部分母、原 $N_1$ 因子、完整 $41/42$ 与 $31/31$ 次结式、每个末纤维，以及半权图的原 $P_i=2N_i$ 身份。实际执行用时 **16.849538 秒**、峰值 RSS **74488 KiB**、**exit 0**。具体源码 SHA、执行身份和环境见[小执行回执](../notes/2026-11-26-unit211-general-zero-highest-execution-347c.json)。

上述常规图、$D=0$ 和 $H=0$ 穷尽 (1.1) 下 $P_0=0$。结合所引已闭边界，单位 $2+1+1$ 的整个最高基点值零分支为空。下一未闭范围准确为 $q\ne0,\pm1$、$b+cq\ne0$、$P_0\ne0$，其中 $m=0$ 和 $m\ne0$ 继续分别处理；没有把这一个闭合提升为整个课题完成。
