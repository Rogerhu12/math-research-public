# R1070 — 原惰性中央解的等范数 CM 转移与实际 wild 正则迹

日期：2026-11-28（UTC）。**状态：以下同电荷正则迹、完整整逆及准确返回已证明；原中央零到全部边界零的蕴含与主目标仍未证明。**

固定 R663 的惰性好素数 $p>211$，$q=p^2,\ d=p+1,\ e=p-1,\ m=34,72$。下文的 $Y,j,a,k,\mathcal B$ 均指 R663(10),(18),(21) 的同一组原数据，
$$
Y'+maY=k\mathcal B,\qquad Y(0)=j_m,\qquad
L(v)=\sigma(z(v))T_g(u(v))/v,\quad W=v^d,\quad a=d\log L/dW.
$$
$L$ 仅作特征零形式级数使用。$Q=W^e-p,\ r_E=p^{-1/e}$。R663(22),(25)–(27) 给 $r_E<r_+<r_2=r_E^{1/q}$，使 $a$ 在闭 $r_+$ 盘解析、$\partial_W+ma$ 在此闭 Tate 代数上有有界逆，$k$ 的极恰为 $Q$ 的根，均为简单极且留数 $d\xi$。$\mathcal B$ 在开单位盘整解析。

## 1. 等范数给同一完整连接

保持 $\delta=\omega-\omega^2,\ A=1+p(p+1)\omega,\ B=\bar A,\ \eta=A/B$。$A,B\equiv1\bmod 2$，在 $p$ 为单位，$N(A)=N(B)$，且 $\eta=1+p\delta\bmod p^2$。对 $h=\eta^l,\ l\ge0$ 取原形式 CM 作用并置
$$
\Phi_h(W)=[h](v)^d,\qquad U_h(W)=L([h]v)/L(v).
$$
这里的 $\sigma$ 始终属于 R663 的原 $E_{17}:y^2=x^3+17$，不换成 $E_1$。R1062(G34)的证明直接在此原整模型适用：原 CM 除点函数 $r_\alpha=\sigma(\alpha z)/\sigma(z)^{N\alpha}$ 以 $\sigma\sim z$ 刚性化；$\alpha\equiv1\bmod2$ 消半特征，等范数消相同 Gaussian。prime-to-$p$ 非零核点不落原形式盘，故正规化后是整个形式盘的整单位。分别取 $\alpha=A^l,B^l$ 再作原整 $[B^{-l}]$ 代换，便直接给下述同模型比值，无模型运输费。

因此 R1062(G34)–(G35)的同一论证对 $F=\sigma(z(v))/v$ 给 $F([h]v)/F(v)$ 与逆都在 $1+v\mathcal O[[v]]$，因为 $N(h)=1$。也可直接在 $A^l,B^l$ 两个有相同范数的原 Miller 恒等式中相除，再以 $[B^{-l}]$ 作整可逆代换。$T_g^{\pm1}$ 整，故 $U_h^{\pm1}$ 同样整。R663(3),(18) 给 $\mu_d$ 在 $v$ 中的线性作用以及 $L$ 的不变性，故 $U_h\in1+W\mathcal O[[W]]$、$\Phi_h\in h^dW+W^2\mathcal O[[W]]$。$\Phi_{h^{-1}}$ 是整组合逆。这些整级数及逆保持每个闭 $r<1$ 盘并在其上 Tate。这里不要求 $L$ 本身在首边界收敛。

在严格内盘 $p^{-1}<r<r_E$ 定义
$$
T_hY=U_h^m(Y\circ\Phi_h),\qquad
F_h=U_h^m\Phi'_h (k\mathcal B)\circ\Phi_h .
$$
由 $d\log U_h=(a\circ\Phi_h)d\Phi_h-a\,dW$ 和链式法则，
$$
(\partial_W+ma)T_hY=F_h,\qquad (T_hY)(0)=j_m .
$$
这是同电荷 $m$ 和同一初值的真实转移。$T_\eta^l=T_{\eta^l}$，但一般 $T_\eta^p\ne1$。以下所有平均都是写出的有限和，仅在首层留数空间上使用有限群投影。

## 2. 首层乘子及其绝对相位

令 $T_v$ 为 R703 的复参数 $\Omega v/p$ 的非零挠点，使用同一代数嵌入输回 $p$ 进，记 $\xi=W(T_v)$。$\Phi_\eta(\xi)=\xi$。取 $x\in\mathbb Z[\omega]$ 使 $Bx=v\bmod p$，令 $T'=T_x$，故 $[A]T'=[B]T'=T_v$。R1062(G34) 对两个真实整 CM 整数的等范数消去给
$$
U_\eta(\xi)=\frac{\psi_A(T')}{\psi_B(T')}.
$$
确实原 Miller 比在 $v(T')$ 处有附因子 $v([B]T')/v([A]T')=1$，且两个 $T_g$ 值相等；所用除点函数在非零 $p$ 挠点均有限非零。R694(7)消去 Klein Gaussian，故上式在指定复嵌入等于 $\mathfrak k(\Omega Ax/p)/\mathfrak k(\Omega Bx/p)$。置 $\ell=(A-B)x/p=(p+1)\delta x\in2\mathcal O_K$。R703(1)–(2) 的半特征 $\chi(\ell)=1$，从而有准确的
$$
U_\eta(\xi)=e_p([\ell,Bx]/2)=e_p(-N(v)),\qquad
U_\eta(\xi)^m=\chi_{m,N(v)}(\eta)^{-1}.
$$
末一步用 $\ell=\delta v\bmod p,\ [\delta v,v]=-2N(v)$ 及 R705(6)–(7)。因此 $e=p-1$ 个 $\mu_d$ 轨道恰有 $e$ 个不同非平凡 $p$ 次单位根乘子，标签与 R716(30) 的原 wild 标签含符号一致。每个剩余范数恰一个轨道。

## 3. 原 $j_m$ 的完整正则迹与全部同源非平凡补项

在原系数域添入 $\mu_p$ 作有限分解；平凡角色平均回原域。对 $t\in\mathbf F_p$ 置
$$
Y^{(t)}=\frac1p\sum_{l=0}^{p-1}e_p(mtl)T_{\eta^l}Y,\qquad
F^{(t)}=\frac1p\sum_{l=0}^{p-1}e_p(mtl)F_{\eta^l}.
$$
在原严格内盘有 $(\partial_W+ma)Y^{(t)}=F^{(t)}$，且 $Y^{(0)}(0)=j_m,\ Y^{(t)}(0)=0$（$t\ne0$）。每个 $\Phi_{\eta^l}$ 是闭 $r_+$ 盘可逆解析映射，逐点固定全部 $Q$ 根且导数非零。因此 $F_{\eta^l}dW$ 在该盘至多有这些简单极，留数为原 $d\xi\mathcal B(\xi)$ 乘 $U_{\eta^l}(\xi)^m$。用实际 cocycle 在该固定点得 $U_{\eta^l}(\xi)^m=e_p(-mlN(v))$。从而
$$
\operatorname{Res}_{\xi}\bigl(F^{(t)}dW\bigr)
 = \mathbf1_{N(v)=t}\,d\xi\mathcal B(\xi).
$$
特别 $F^{(0)}$ 在整个同一闭 $r_+$ 盘 Tate。具体而言 $QF^{(0)}$ 在盘上解析，因 $\Phi_{\eta^l}$ 保持简单零除子，且所有 $Q$ 根上的值均为零，故可逐个除去 $W-\xi$；商在同一闭盘 Tate。由 R663(27) 外盘上的完整有界逆和严格内盘唯一性，
$$
Y^{(0)}=(\partial_W+ma)^{-1}_{r_+}F^{(0)},\qquad
j_m=\left[(\partial_W+ma)^{-1}_{r_+}F^{(0)}\right]_{W=0}.
$$
这个正规解在 $j_m=0$ 时确为外盘零初值解。$1/p$ 在系数域上使用，未宣称整算子。对 $t\ne0$，写 $\xi_t$ 为唯一目标轨道，$D_t=d\xi_t\mathcal B(\xi_t)$。完整正则补项为
$$
F_{\mathrm{reg}}^{(t)}=F^{(t)}-\frac{D_t}{W-\xi_t}.
$$
在原内盘逆与外盘正则逆下，准确有
$$
0=\big[(\partial_W+ma)^{-1}_{r_+}F_{\mathrm{reg}}^{(t)}\big]_0+
D_t\big[(\partial_W+ma)^{-1}_{r}((W-\xi_t)^{-1})\big]_0 .
$$
两项均保留。$t=0$ 的平均没有把原 $Y$ 自身延过边界，亦未推出任一 $D_t=0$。$Y=\sum_tY^{(t)}$ 在严格内盘恒等。

## 4. 全指定深度的 forcing

同一公式给所有有限深度的完整微分形式，而无须外推 R663 逆的半径。对 primitive $T_v=\Omega v/p^i$ 置 $A_i=A^{p^{i-1}}, B_i=B^{p^{i-1}}, h_i=A_i/B_i$。二项式给 $h_i=1+p^i\delta\bmod p^{i+1}$，所以 $\eta$ 在该 $W$ 点的轨道长度为 $p^{i-1}$：$\eta^l\bmod p^i$ 为 $\mu_d$ 时，模 $p$ 的平凡性先迫该 $\mu_d$ 元为1，再用 $v_p(\eta^l-1)=1+v_p(l)$。取 $B_i x=v\bmod p^i,\ \ell_i=(A_i-B_i)x/p^i\in2\mathcal O_K$。相同的等范数除点函数及准周期律给
$$
U_{h_i}(W_T)=e_{p^i}\bigl([\ell_i,B_ix]/2\bigr),\qquad
[\ell_i,B_i x]/2=-N(v)\bmod p .
$$
因此该乘子有确切阶 $p^i$，其 $m$ 次幂也如此。$k=1+dWH'/H$ 所有非零挠点极均简单；这是 R663§2 的对数零点分类及整坐标导数单位。给定 $n\ge1$，对同一个完整 $F_{\eta^l}dW$ 作 $0\le l<p^{2n-1}$ 平均。层 $i\le n$ 每个原点的和按 $l\bmod p^{i-1}$ 分组，组内 $\Phi$ 的目标固定，留数的 Jacobian 已由 $d\Phi$ 支付，余下正是上述 primitive $p^i$ 次根的幂和。每组长度 $p^{2n-i}$ 被 $p^i$ 整除，故全部这些挠点极消去。所得 forcing 在下一层前每个闭盘 Tate，平均有明确 $p^{-(2n-1)}$ 费用。此处 $2n-i\ge i$ 正因 $i\le n$，不需对其它层预设消失。外盘解可逆性只在已付的首层 $r_+$ 使用。

## 5. 原 $X$ 返回

在严格内盘 $X=z(v)^d=WH(W)^d,\ L(v)=E_{\rm c}(X)H(W)$，故
$$
H(W)^mE_{\rm c}(X)^m T_{\eta^l}Y
 = E_{\rm c}(\eta^{dl}X)^m\mathcal R_m(\eta^{dl}X).
$$
若 $j_m=0$，R639(5) 给右边恰为零初值 Euler 原函数的 $d\Pi_0\mathscr U_m$ 在此缩放点的值。平凡平均在 $X^k$ 上的系数乘
$$
b_k=\frac1p\sum_{l=0}^{p-1}\eta^{dlk}
 = \frac{\eta^{dpk}-1}{p(\eta^{dk}-1)},\quad k>0,\qquad b_0=1.
$$
每个 $b_k$ 都是单位，因为 $\eta^{dk}\equiv1\bmod p$ 且 $v_p(s^p-1)=1+v_p(s-1)$ 对应于 $s=\eta^{dk}$。因此此对角算子与逆在任一给定 $X$ 盘的系数 Gauss 范数上等距。已得的外盘函数是 $Y^{(0)}(W)$，而不是上述 $X$ 级数本身；$H^{-m},E_{\rm c}^{-m}$ 和 $X=WH^d$ 的多支下降仍须支付，不能由 $b_k$ 为单位直接推原 $Q\mid\mathcal B$。

## 6. 同一个极限解同时读出原初值和全部首层余数

记 $T^0=T_\eta$ 为对函数的上述有权拉回，本节用 $T^1$ 表示对微分形式的同一有权拉回（含 $\Phi'_\eta$，上标表示形式次数）。对 $i=0,1$ 及 $M\ge0$ 写
$$
S_M^i=p^{-M}\sum_{l=0}^{p^M-1}(T^i)^l.
$$
在每个固定 $r<1$ 上，$(T^i)^{p^M}$ 在闭盘 Tate 代数的算子范数中趋于恒等。事实上 $h_M=\eta^{p^M}\to1$。$\Phi_{h_M}$ 及 $U_{h_M}$ 的系数分别逐项趋于 $W$ 与 $1$。这由形式对数下 $[h_M]$ 线性缩放、固定系数只用有限次运算，以及原形式比 $L([h_M]v)/L(v)$ 得到；各 $M$ 的完整整性已付。因此对每个严格 $r<1$，统一整尾使上述函数按 Gauss 范数趋于各自极限，$\Phi'_{h_M}\to1$ 亦然。对闭盘 Tate 函数 $f$，幂差分解和连续性给
$$
\|f\circ\Phi_{h_M}-f\|_r
 \le r^{-1}\|\Phi_{h_M}-W\|_r\|f\|_r .
$$
结合 $U_{h_M}^m$（对1-形式再乘 $\Phi'_{h_M}$），得到所称算子范数收敛。

给定闭 $r<1$，先由前节的层数选 $M_0$，使 $S_{M_0}^1(k\mathcal B\,dW)$ 在该闭盘 Tate。随后可进一步增大 $M_0$，因为有限加权拉回保持该盘 Tate。令 $D=(T^1)^{p^{M_0}}-I$，令 $\|D\|<p^{-1/(p-1)}$。则在该同一代数上，
$$
\lim_{s\to\infty}\frac1{p^s}\sum_{l=0}^{p^s-1}(I+D)^l
 = \sum_{j\ge0}\frac{(-1)^jD^j}{j+1}.
$$
确实左侧 $D^j$ 的系数是 $\binom{p^s}{j+1}/p^s=\binom{p^s-1}{j}/(j+1)$，逐项趋于右侧，并受 $|1/(j+1)|_p$ 一致控制；乘 $\|D\|^j$ 后尾一致趋零。因有限和按整块精确分解，上式施于 $S_{M_0}^1(k\mathcal B\,dW)$ 给
$$
F_\infty\,dW=\lim_{M\to\infty}S_M^1(k\mathcal B\,dW)
$$
在每个闭 $r<1$ 解析，结果在限制下相容。所以得到一条开单位盘解析的同源 forcing。没有称 Volkenborn 平均为整测度，也没有统一抹掉各盘起始的 $p^{-M_0}$ 费用。

对闭 $r_+$ 上的函数作同一证明；可先从已真正延拓的 $S_1^0Y$ 开始，故不用假设原 $Y$ 延过边界。于是有同一个实际极限
$$
Y_\infty=\lim_{M\to\infty} S_M^0Y \in K\langle W/r_+\rangle,\qquad
(\partial_W+ma)Y_\infty=F_\infty,\qquad Y_\infty(0)=j_m .
$$
微分在固定闭 $r_+$ 盘上有界，故可取极限。最后的初值由所有有限和的准确初值给出。

该函数还满足一条无需未知 forcing 的准确差分式
$$
\boxed{(T^0-I)Y_\infty=d\log_p(\eta)\, W\mathcal B(W).}
$$
证明先在严格内盘。有限几何和给 $(T^0-I)S_M^0Y=p^{-M}((T^0)^{p^M}-I)Y$。计算该右侧的逐系数极限只需在特征零形式级数中微分。若 $h=\exp(s)$，则 $X(\Phi_h)=h^dX(W)$ 与 $X=WH^d$ 给
$$
\left.\partial_s\Phi_h\right|_0 = \frac{d W}{k(W)}.
$$
$U_h=L(\Phi_h)/L(W)$ 的形式 log 导数随之给
$$
\left.\partial_s T_hY\right|_0
 =\frac{d W}{k(W)}(\partial_W+ma)Y=dW\mathcal B(W).
$$
在形式级数中置 $s=p^M\log_p\eta$ 即得系数极限；左侧已在严格内盘以至 $r_+$ 盘有真实 Tate 极限，右侧本身开盘解析。因此逐系数等式延到整个同一 $r_+$ 盘。这里 $dW$ 在右侧函数中是整数 $d$ 乘变量 $W$，不是一个微分。

在首层实际固定点 $\xi=W(T_v)$ 评价得
$$
\boxed{
(e_p(-mN(v))-1)Y_\infty(\xi)
 = d\log_p(\eta)\,\xi\,\mathcal B(\xi).
}
$$
乘子非零且估值 $1/(p-1)$，$\log_p\eta$ 的估值为1，$v_p(\xi)=1/(p-1)$。从而每个原轨道准确有 $v_p(Y_\infty(\xi))=1+v_p(\mathcal B(\xi))$，包括无穷赋值的情形。特别，同一个外盘规范函数的原点读数是 $j_m$，全部首层点逐点等价于原全部余数的消失。由 $Y_\infty(0)=0$ 传到这些点仍是实际待证的算术步骤；这里没有从一个零推所有零。

## 7. 真正有限 $p$ 项迹的全部局部 jet

首层有限迹记作 $Y_{\rm tr}=S_1^0Y$。当 $M\ge1$，$S_M^0Y$ 是将 $(T^0)^p$ 的 $p^{M-1}$ 项平均用于 $Y_{\rm tr}$。在每个实际 $\xi$ 上，$\Phi_{\eta^p}(\xi)=\xi,\ U_{\eta^p}(\xi)=1$，因此每个 $M\ge1$ 都有
$$
S_M^0Y(\xi)=Y_{\rm tr}(\xi)=Y_\infty(\xi).
$$
特别上节的所有首层公式已经在这同一个有限 $p$ 项、原点值 $j_m$ 的真正外盘函数上成立。

以下给该函数的全部 jet。取 $\xi=W(T_v)$ 上的任一原 $v$ 坐标分支，以 $t=z(v)$ 作局部坐标，$t(\xi)=0$。$z'(v)$ 为单位且 $dW/dv\ne0$，故此坐标在某个小盘双解析；选取范数足够小的圆盘，使 $\eta t$ 保持该盘。$\Phi_\eta$ 对应 $t\mapsto\eta t$。在该盘取唯一局部单位 $G(t)$ 满足 $G(0)=1$，$d\log G=m a\,dW$；积分后指数在足够小盘收敛。置
$$
\epsilon=e_p(-mN(v)),\qquad
g(t)=G(t)\,W(t)\mathcal B(W(t)),\quad f_\infty=G Y_\infty,\quad f_{\rm tr}=G Y_{\rm tr}.
$$
两边 log 导数和初值给真正的 $U_\eta^m=\epsilon G(\eta t)/G(t)$。因此上节差分式在每个 $h\ge0$ 给
$$
(\epsilon\eta^h-1)[t^h]f_\infty=d\log_p(\eta)[t^h]g.
$$
因 $\eta^h\in1+p\mathcal O,\ v_p(\epsilon-1)=1/(p-1)$，所有分母都非零且估值恰 $1/(p-1)$。同一规范化下 $(T^0)^p$ 作用 $t^h\mapsto\eta^{ph}t^h$。对上述准确的有限分块逐系数取极限（固定任一 Taylor 系数是有界泛函），从真正 $Y_{\rm tr}$ 到 $Y_\infty$ 的系数乘子在 $h=0$ 为1，在 $h>0$ 为
$$
\lim_{M\to\infty}\frac{1}{p^{M-1}}\sum_{l=0}^{p^{M-1}-1}\eta^{phl}
=\frac{ph\log_p\eta}{\eta^{ph}-1}.
$$
从而有限 $p$ 项外盘迹的完整返回为
$$
\boxed{
[t^h]f_{\rm tr}=
\begin{cases}
\dfrac{d\log_p\eta}{\epsilon-1}[t^0]g,&h=0,\\[2mm]
\dfrac{d(\eta^{ph}-1)}{ph(\epsilon\eta^h-1)}[t^h]g,&h>0.
\end{cases}}
$$
全部乘子非零，且估值恒 $1-1/(p-1)$。这里 $\eta$ 非根单位可由其非零 $p$ 进对数看出。

上述规范和 $g$ 的任意有限阶 Taylor 系数均为代数。确实有
$$
a\,dW=\tfrac12 d\mathscr L(bu^6)+d\log(u/v)+d\log T_g(u),
$$
其中 $\mathscr L=\log(x\sigma^2)$；这是原点正式微分身份，继而在开单位盘成立。R681(18)–(29) 给 $\mathscr L$ 的全部正阶、$T_g$、$u,v$ 及 $\mathcal B$ 的原点外首挠点 jet 的代数性。$z'(u)=C(u)$ 确定 $t$ 在此处的全部正阶代数导数及有限组合逆；$t=0$ 与 $G(0)=1$ 固定常数。局部一阶方程逐系数确定 $G$ 的全部代数 jet。故 $f_{\rm tr}(0)$ 是 $\log_p\eta$ 乘一个明确代数数，而所有 $h>0$ 的 $[t^h]f_{\rm tr}$ 已经是明确代数数。未将原 $j_m$ 认作这种边界点值。

因所有局部乘子均非零、$W(\xi)\ne0$、$G$ 是局部单位，对每个 $\ell\ge1$ 有
$$
\boxed{Q^\ell\mid Y_{\rm tr}\text{ 于 }K\langle W/r_+\rangle
\quad\Longleftrightarrow\quad Q^\ell\mid\mathcal B\text{ 于 }\mathcal O[[W]].}
$$
同式对 $Y_\infty$ 成立。左侧用诸简单根上的消失阶，右侧用 R663(15)–(16) 的整余数刻画。这在原点值仍等于 $j_m$ 的真正外盘有限迹上读出了全部高次边界剩余，不要求原 $Y$ 自身延过边界。

最后，外盘构造的 $1/p$ 费用不表示在首边界范数必损精度。对 $p^{-1}<r<r_E$，$D=T^0-I$ 满足 $\|D\|_r\le\max\{p^{-1},r\}$，因为 $U_\eta-1\in W\mathcal O[[W]]$，$\Phi_\eta-W\in pW\mathcal O+W^2\mathcal O[[W]]$。上节二项式展开中 $|1/(j+1)|_p r_E^j\le1$，这是 $j\ge p^{v_p(j+1)}-1\ge(p-1)v_p(j+1)$。所以所有 $S_M^0$ 在这些内盘的算子范数至多1。由 R663 的有界逆和 R710(7)的内盘界，$\|Y\|_r\le p^{-1}$，令 $r\uparrow r_E$ 得
$$
\|Y_{\rm tr}\|_{r_E}\le p^{-1},\qquad \|Y_\infty\|_{r_E}\le p^{-1}.
$$
这里没有在更外的 $r_+$ 盘无条件删除平均分母。

## 8. 原差分算子在整个开单位盘的整逆

差分式能把同一个 $Y_\infty$ 本身从首层外盘延到整个开单位盘，而无须更大盘上的 $\partial_W+ma$ 有界逆。置
$$
h_m(W)=\frac{U_\eta(W)^m-1}{W},\qquad
\mathcal M f=\frac{T^0f-f}{W}
=h_m f+U_\eta^m\frac{f(\Phi_\eta)-f}{W}.
$$
由 $L'/L=a,\ \Phi'_\eta(0)=\eta^d$，有 $h_m(0)=mc(\eta^d-1)$。$v_p(c)=-1,\ \eta=1+p\delta\bmod p^2$ 且 $md\delta$ 为单位，所以 $h_m\in\mathcal O[[W]]^\times$。

此外有更强的完整整位移
$$
\Phi_\eta(W)-W\in pW\mathcal O[[W]]+W^{e+1}\mathcal O[[W]] .
$$
确实将 $[\eta]v$ 写成 $v\oplus[\eta-1]v$。因 $\eta-1\in p\mathcal O$ 且原 LT 坐标的 $[-p]v=-pv+v^q$，$[\eta-1]v\bmod p$ 从 $v^q$ 起。整形式加法 $F(v,y)-v$ 被 $y$ 整除，故 $[\eta]v/v=1\bmod(p,v^{q-1})$。取 $d$ 次幂、乘 $W$，再用完整 $\mu_d$ 不变性及 $q-1=de$ 即得。这个加强使变量位移的费用严格低于 $U_\eta^m-1$ 的非零一次项。

对每个 $p^{-1}<r<1$ 的闭盘，
$$
\|\Phi_\eta-W\|_r/r\le\max\{p^{-1},r^e\},\qquad
\left\|h_m^{-1}U_\eta^m\frac{f(\Phi_\eta)-f}{W}\right\|_r
\le\max\{p^{-1}/r,r^{e-1}\}\|f\|_r.
$$
分子常数为零，除 $W$ 的 Gauss 费用为 $1/r$；$\|h_m^{\pm1}\|_r=\|U_\eta^{\pm m}\|_r=1$。右侧严格小于 $\|f\|_r$。因此 $\mathcal M$ 在每个此类盘上是 Gauss 等距同构，完整逆为严格收缩的 Neumann 级数。不同盘上的逆由唯一性相容。对所有 $r\uparrow1$ 用相同范数界可知 $\mathcal M$ 限制为 $\mathcal O[[W]]$ 的整线性自同构；并不称它为环同态。

由首层外盘的差分式及这个唯一逆，
$$
\boxed{\;
Z_m=\mathcal M^{-1}\mathcal B_m\in\mathcal O[[W]],\qquad
Y_\infty=d\log_p(\eta)\,Z_m\in p\mathcal O[[W]],\qquad
d\log_p(\eta) Z_m(0)=j_m .
\;}
$$
故原极限解本身在整个开盘解析，且对所有 $p^{-1}<r<1$ 有 $\|Z_m\|_r=\|\mathcal B_m\|_r$。首层得到的原微分式 $(\partial_W+ma)Y_\infty=F_\infty$ 因两边均已在整个开盘解析也随之在开盘成立。有限 $p$ 项的 $Y_{\rm tr}$ 没有因这个极限解延拓而自动获得整开盘的断言。

这里 $a$ 的整开盘解析范围来自 R663§5(19)，独立于形式指数 $L$ 的收敛。具体地 $d v^{d-1}a=\Xi(u)C(u)du/dv+\partial_v\log T_g-1/v$。R639(14)–(15) 的 $\Xi=u^{-1}\sum J_nb^n u^{6n}$ 满足 $v_p(J_n)\ge-\lceil v_p(6n-1)/2\rceil$，故只有已由 $-1/v$ 抵消的原点极，其他部分在整个开盘解析。$T_g$、坐标及整逆均已给；商的 $\mu_d$ 型使余下只含 $v^{d-1}W^k$。

对第 $i$ 层 primitive 点 $T_v$，置 $W_i=W(T_v),\ H_i=p^{i-1},\ \epsilon_i=U_{\eta^{H_i}}(W_i)^m$，这是前面准确给出的 primitive $p^i$ 次根。对 $(T^0-I)Z_m=W\mathcal B_m$ 作 $H_i$ 项几何和，在同一实际 $W_i$ 上评价，全开盘身份给
$$
\boxed{\;
(\epsilon_i-1)Z_m(W_i)=
\sum_{l=0}^{H_i-1}U_{\eta^l}(W_i)^m
\Phi_{\eta^l}(W_i)\mathcal B_m(\Phi_{\eta^l}(W_i)).
\;}
$$
所有局部比值、orbit Jacobian 的函数/形式区别及完整原 $\mathcal B_m$ 均保留。若 $j_m=0$，$Z_m\in W\mathcal O[[W]]$。因此上式右侧除 $W_i$ 后的估值至少为 $v_p(\epsilon_i-1)=1/(p^{i-1}(p-1))$。不假设中央为零时，由 $Z_m$ 的整性仍有对应下界 $1/(p^{i-1}(p-1))-1/(p^{2i-2}(p-1))$。首层是单点；高层保全部 $p^{i-1}$ 项。

## 9. 原常数前两位与已付中央行的核对

写 $s=\eta^d,\ D=s-1,\ z_j=[W^j]Z_m,\ b_j=[W^j]\mathcal B_m,\ a_1=[W]a$，$h_0=mcD$。LT 坐标使全部 $\mu_{q-1}$ 线性作用，而 $[\eta]$ 与它们交换，所以 $[\eta]v/v$ 是 $v^{q-1}$ 的级数，$\Phi_\eta=sW+O(W^{e+1})$。比较 $\log U_\eta^m=m(\log L(\Phi_\eta)-\log L(W))$ 的前两项，得
$$
h_1=[W^2]U_\eta^m=h_0^2/2+(m a_1/2)(s^2-1).
$$
原整逆方程的头两行逐项为
$$
b_0=h_0z_0+D z_1,\qquad
b_1=h_1z_0+s h_0z_1+(s^2-1)z_2 .
$$
其中 $b_0=[z^d]A_m,\ b_1=g^{\rm c}_{m,2}$ 由 R663(12)、R710(20) 给出，不能任取。$D\in p\mathcal O$ 且 $h_0$ 为单位，所以
$$
z_0\equiv\frac{b_0}{h_0}
  -\frac{D b_1}{h_0^2}+\frac{D h_1 b_0}{h_0^3}\pmod{p^2}.
$$
乘 $d\log_p\eta=\log(1+D)$ 后，$h_1$ 中的 $h_0^2/2$ 项正抵一次相对 log 修正。R710(6) 给 $v_p(a_1)\ge-1$。故真实 $j_m$ 的前两位为
$$
j_m\equiv\frac{b_0}{mc}
  -\frac{b_1}{m^2c^2}+\frac{a_1 b_0}{m^2c^3}\pmod{p^3}.
$$
若 $j_m=0$，则先有 $b_0\in p\mathcal O$，再还原出 $(pmc)b_0/p\equiv b_1\bmod p$。这恰与 R710(27) 在保留 $b_{m,e}$ 两边后相消的实际第二位相同。$h_0$ 是坐标单位，不给固定非零中央输入。

## 10. 真实 $p$ 项 CM 迹在整开盘的精确像

在函数上简记 $T=T^0$、$P(T)=\sum_{l=0}^{p-1}T^l$，无 $1/p$。对每个整函数 $f$，全部首层 $\xi$ 上的 $P(T)f$ 都为零，因为 $\Phi_\eta(\xi)=\xi$ 而 $U_\eta(\xi)^m$ 是非平凡 $p$ 次根。所以 $Q\mid P(T)f$，并有更准确的
$$
\boxed{\quad Q^{-1}P(T):\mathcal O[[W]]\longrightarrow
\mathcal O[[W]]\quad\hbox{为整线性自同构}.\quad}
$$
在每个 $r_E<r<1$ 闭盘的 Tate 代数先证明。上面的逐点消失付 $Q$ 的全盘可除性。令 $\mathsf D=T-I$，$V$ 为乘函数 $Wh_m$ 的算子。前节给 $\|\mathsf D-V\|_r\le\max(p^{-1},r^e)<r$，$\|\mathsf D\|_r=\|V\|_r=r$。由二项式
$$
P(T)=\sum_{j=0}^e\binom{p}{j+1}\mathsf D^j
$$
仅顶项 $\mathsf D^e$ 系数为单位，其余项的算子范数至多 $p^{-1}<r^e$。非交换差幂的伸缩恒等式给 $\|\mathsf D^e-V^e\|_r<r^e$。同时 $Qh_m^e-W^e h_m^e=-p h_m^e$ 的范数 $p^{-1}<r^e$。由于 $\|Q\|_r=r^e$，Gauss 范数的乘法性给 $\|Q^{-1}P(T)-h_m^e\|_r<1$。乘 $h_m^e$ 是等距可逆，故所称算子也等距可逆；半径从下趋一恢复整环和其整逆。

因此在同一原电荷上，$Q\mid\mathcal B_m$ 等价于 $Q\mid Z_m$，也等价于存在整开盘函数 $f$ 使 $Z_m=P(T)f$。此时 $f$ 唯一且
$$
(T^p-I)f=W\mathcal B_m,\qquad
j_m/(d\log_p\eta)=p f(0).
$$
反向，若整 $f$ 满足这条差分方程，则 $(T-I)(P(T)f-Z_m)=0$，由全盘 $\mathcal M$ 的单射性即得 $P(T)f=Z_m$。这精确支付原算子从 $\eta$ 到 $\eta^p$ 的整迹像。单个 $j_m=0$ 条件只给 $Z_m(0)=0$，尚未给整迹原像或全部 $Q$ 根读数零。

## 11. 原同电荷连接的整测度与所有奇数指数的野角色

保上一节的同一 $E_{17}:y^2=x^3+17$、指定 $p$ 进嵌入、严格 $v$、$W=v^d$ 和 $T f=U_\eta^m f(\Phi_\eta)$。上一节所需整 Miller 单位可直接在本模型证明：R639(6) 分别在等范数的 $A^l,B^l$ 上用本曲线的原 $\sigma,z$ 及两个真实除点函数，相除并在整坐标代 $[B^{-l}]$，即得原 $F=\sigma(z(v))/v$ 的整比，且单位刚性化为1。乘本模型的 $T_g$ 整比后恰为 $U_{\eta^l}$。R1062(G34)–(G35)的逐系数证明在这里沿同一模型应用，未以 $E_1$ 的 physical 标记替换本模型。

令 $\mathsf D=T-I,\ g(W)=U_\eta^m-1=W h_m(W)$。$h_m(0)=mc(\eta^d-1)$ 为单位，故 $g$ 是原开盘的整可逆坐标，$g,g^{-1}$ 保持每个闭 $r<1$ 盘。以独立变量 $X$ 定义线性算子
$$
\mathfrak C:\quad \sum_{n\ge0}c_nX^n
 \longmapsto \sum_{n\ge0}c_n\,\mathsf D^n 1.
$$
在这里 $X$ 是测度的 Amice 变量，与前文 $z^d$ 使用不同。对 $p^{-1}<r<1$，置 $\epsilon_r=\max(p^{-1},r^e)<r$。上一节给 $\|\mathsf D-M_g\|_r\le\epsilon_r,\ \|\mathsf D\|_r=\|M_g\|_r=r$，其中 $M_g$ 是乘 $g$。伸缩恒等式于是给
$$
\|\mathsf D^n1-g^n\|_r\le(\epsilon_r/r)r^n,\quad n\ge1 .
$$
对整个闭盘 Tate 代数，上述和收敛且 $\mathfrak C$ 与 $f\mapsto f(g(W))$ 的算子距离至多 $\epsilon_r/r<1$。后者是等距同构，Neumann 逆给 $\mathfrak C$ 亦为等距同构。各盘相容并沿 $r\uparrow1$ 得
$$
\mathfrak C:\mathcal O[[X]]\overset{\sim}{\longrightarrow}\mathcal O[[W]],
\qquad \mathfrak C(Xf)=\mathsf D\,\mathfrak C(f),\qquad
(\mathfrak C f)(0)=f(0).
$$
这是线性同构，不能当作任意两函数乘法的同态。

对指定的原整输入设
$$
\boxed{\mathscr L_{m,\eta}(X)=\mathfrak C^{-1} Z_m,\qquad
\mathscr L_{m,\eta}(0)=\frac{j_m}{d\log_p\eta},\qquad
\mathfrak C(X\mathscr L_{m,\eta})=W\mathcal B_m.}
$$
这个整幂级数是 $\mathbb Z_p$ 上实际有界测度的 Amice 变换，即其第 $n$ 个系数准确规定 $\binom{x}{n}$ 的积分。连续函数的 Mahler 展开给唯一有界延拓。所用的一般对应可见 R. Sharifi, *Iwasawa Theory*, [§5.2, Proposition 5.2.9、Corollaries 5.2.12–13、Theorem 5.2.14](https://math.ucla.edu/~sharifi/notes/iwasawa-ch05.html)；本文用的是原有限未分歧系数环，实际系数和每个有限角色值由上式指定。以 $l\mapsto\eta^l$ 标记原范数一群的 pro-$p$ 部分（$\eta=1+p\delta\bmod p^2$ 故为拓扑生成元），其在每个连续有限角色 $\eta\mapsto\lambda$ 的值是 $\mathscr L_{m,\eta}(\lambda-1)$。Tame 部分在此取平凡角色；须另保 R716 真 Hecke twist 的平方。

## 12. 所有 primitive 层的循环向量与非零归一

固定 $i\ge1$。所有确切 $p^i$ 阶形式群点按 $\mu_d$ 商后有
$$
D_i=(q-1)q^{i-1}/d=e p^{2i-2}=\varphi(p^{2i-1})
$$
个不同 $W$ 值，且其赋值均为 $1/D_i$。首层由 $v^{q-1}=p$ 给出；以后 $[-p](v)=-pv+v^q$ 的唯一大项为 $v^q$，故每次除以 $q$。这些点的乘积多项式 $Q_i(W)=\prod_\xi(W-\xi)$ 在 $\mathcal O[W]$，因为原形式群和 $\mu_d$ 轨道为 Galois 所保。常数项估值为1，其余非首系数估值均正且在未分歧基域为整数，故 $Q_i$ 为 Eisenstein 多项式。$Q_1=Q$。

在一个 $\eta$ 轨道上写 $H=p^{i-1},\ \xi_l=\Phi_{\eta^l}(\xi_0),\ u_l=U_{\eta^l}(\xi_0)^m$。已证轨道长度为 $H$，且 $u_H=\epsilon_i$ 是上文按原 Klein 公式指定的 primitive $p^i$ 次根。对每个 $\lambda^H=\epsilon_i$ 定义
$$
\ell_\lambda(f)=\sum_{l=0}^{H-1} u_l\lambda^{-l} f(\xi_l).
$$
原 cocycle 给 $\ell_\lambda(Tf)=\lambda \ell_\lambda(f)$，包括末端 $u_H=\lambda^H$。在包含所有该层点和所需根单位的有限基扩，任取 $r>|\xi_0|$ 且 $r<1$。评价映射从该闭盘 Tate 代数满射到全部 $D_i$ 个点的函数：这些点互异，有限 Lagrange 多项式给任意向量。$\mathfrak C$ 在同一基扩仍满射，故 $\{\mathsf D^n1:n\ge0\}$ 的像线性生成这个有限维空间，有限维子空间已经闭。$\ell_\lambda$ 本身非零，因它在轨道某单点函数上的系数非零；若 $\ell_\lambda(1)=0$，本征关系会使其杀掉全部 $\mathsf D^n1$，矛盾。两个不同轨道也不能给同一个 $\lambda$，否则两个有不交支撑的独立本征泛函的非零线性组合会杀掉 $1$，同样矛盾。因每个 $\lambda$ 阶恰为 $p^{2i-1}$ 且总计为 $D_i$，遂恰好一重穷尽所有该阶根单位。

对每个真正 $\lambda$ 可在原闭盘 Tate 代数逐项评价，得到完整全层式
$$
\boxed{\;
(\lambda-1)\mathscr L_{m,\eta}(\lambda-1)
=\frac{\ell_\lambda(W\mathcal B_m)}{\ell_\lambda(1)} .
\;}
$$
原分母非零由上述循环性付清，未假设其为单位。因非零整 Weierstrass 级数在开单位盘只有有限个零，所有这些无界奇数指数层的取值确定整测度至多一份。此唯一性需共同基域离散赋值及整性，并不把其它命名的 period 或测度自动识别为它。

## 13. 整有限商、精确赋值与 $\mu,\lambda$ 不变量

令 $\Pi_i(X)=\Phi_{p^{2i-1}}(1+X)$，它是 cyclotomic Eisenstein 多项式。上一节的完整本征泛函构成全部 $D_i$ 点函数空间的对偶基，且 $\ell_\lambda(\mathfrak C f)=f(\lambda-1)\ell_\lambda(1)$。所以
$$
\mathfrak C^{-1}(Q_i\mathcal O[[W]])=\Pi_i\mathcal O[[X]] .
$$
两侧积分除法可用各自 monic distinguished 多项式的 Weierstrass 余数。此同构只比较整线性模。

置 $\rho_i=p^{-1/D_i}$。由于 $|g(\xi)|=\rho_i$，上面的严格算子界在 $r=\rho_i$ 给 $v_p((\mathsf D^n1)(\xi))=n/D_i$。将 $f$ 模 $\Pi_i$ 的余数写为 $\sum_{n<D_i}a_nX^n$，系数在原未分歧域，各项非零赋值有不同的小数部分。因此
$$
v_p(f(\lambda-1))
 =\min_{n<D_i}\bigl(v_p(a_n)+n/D_i\bigr)
 =v_p((\mathfrak C f)(\xi)).
$$
同样，$\mathcal M$ 保 $Q_i$ 的零理想，因为 $\Phi_\eta$ 置换该层点且 $\xi\ne0$。在该商以内以次数 $<D_i$ 的余数 $P$ 计算；分数不同给 $\|P\|_{\rho_i}=|P(\xi)|$。$\mathcal M P-h_mP$ 的共同 Gauss 范数严格小于 $\|P\|_{\rho_i}$，$|h_m(\xi)|=1$。于是 $v_p((\mathcal M P)(\xi))=v_p(P(\xi))$，包括零余数。对原源特别给
$$
\boxed{v_p(\mathscr L_{m,\eta}(\lambda-1))
=v_p(Z_m(\xi))=v_p(\mathcal B_m(\xi)).}
$$
这里没有混同一般不同的两个全分歧域的乘法。

整环等距同构先给三者的 $p$-content 相同。又 $\bar\Phi_\eta=W+O(W^{e+1})$，故对每个 $n\ge0$，
$$
\overline{\mathsf D(W^n)}
 =\bar h_m(0)W^{n+1}+O(W^{n+2}).
$$
这里变量位移对 $n>0$ 从 $W^{n+e}$ 才起，$n=0$ 时无位移。由归纳 $\overline{\mathsf D^n1}=\bar h_m(0)^nW^n+O(W^{n+1})$，所以 $\mathfrak C\bmod p$ 保持最低次数。相同位移界给 $\overline{\mathcal M(W^n)}=\bar h_m(0)W^n+O(W^{n+1})$，亦保最低次数。对非零原源，若 $\mu$ 表示系数共同 $p$ 指数，$\lambda$ 表示除 $p^\mu$ 后的首单位次数，则
$$
\boxed{\;
\mu(\mathscr L_{m,\eta})=\mu(\mathcal B_m),\qquad
\lambda(\mathscr L_{m,\eta})=
\operatorname{ord}_{W=0}\bigl(\overline{p^{-\mu}\mathcal B_m}\bigr).
\;}
$$
这些是原 $\mathcal B_m$ 的不变量，不能据此把 $\mu=0$ 或 Rubin 函数的 $\lambda_p$ 直接转给它。

## 14. 首层返回原 $E_{17}$ Hall 及 $E_1$ 上的同一 Katz 质量

对首层 $T=T_v,\ r=N(v)\bmod p,\ \epsilon=e_p(-mr),\ x=\epsilon-1$，上式为 $x\mathscr L_{m,\eta}(x)=\xi\mathcal B_m(\xi)$。保持 R696(16)–(17) 的 $w_T$、$G_T=T_g(u_T)$、$\mathcal T_{m,T}$ 和 $v_T$，实际全迹给
$$
\boxed{\;
x\mathscr L_{m,\eta}(x)
=\frac{K_{m,T}}{d}\mathcal T_{m,T},\qquad
K_{m,T}=(v_T w_T/G_T)^m\in\mathcal O_{\overline K}^{\times}.
\;}
$$
此处整单位称谓仅指所选 $p$ 位，系数为已选定代数数。确实 $v_p(v_T)=1/(q-1),\ v_p(w_T)=-1/(q-1),\ v_p(G_T)=0$。全部原 Hall 项、轨道质量 $d$ 及根的相位已在式中。

特别在 $m=34$，R703(20) 及 R1067《第一 wild Rubin 偶重数》式(25),(26),(35),(37) 对同一 $N(v)=r$ 给
$$
\boxed{\;
\boldsymbol\mu_H(1)=H_r(0)
=\frac{\vartheta^6}{\sqrt d}\mathscr S_{p,34}(r)
=\vartheta^6\sqrt d\
 \rho_v^{34}e_p(\tau_{34}(v))\,K_{34,T}^{-1}\,
 x\mathscr L_{34,\eta}(x).
\;}
$$
模型运输保 $\vartheta=17^{1/6}$、原 Miller lift、$\chi_r$ 和单 Hall 的 $d^{-1/2}$。若 lifts 已吸收 $\chi_r$，不再乘一次。R716(36) 的固定实周期和全部非 $p$ Schwartz 向量也原样给
$$
\frac{L(\psi\widetilde\eta_{p,r},1)}{\Omega_{\mathbf R}}
=\frac{48940416}{p}\,
 \left|d K_{34,T}^{-1} x\mathscr L_{34,\eta}(x)\right|^2 .
$$
右边的绝对值在 R716 的同一复嵌入评价刚得到的代数数。真实 Hecke twist 在 $p$ 地为 $\chi_r^2$，而 $x$ 读的是 $\chi_r^{-1}(\eta)$ 的减一；不相认两个 Iwasawa 参数。保持 R303 整基和原 $\gamma$ 时，R1063(I21)对 $t_\nu=\widetilde\eta_{p,r}(\gamma)-1$ 准确给
$$
v_p\mathcal A_p(t_\nu)=2v_p(x\mathscr L_{34,\eta}(x)).
$$
连同 $(X\mathscr L)'(0)=j_{34}/(d\log_p\eta)$，已把原中央与单 Hall 的同一固定质量放进上述新有界测度的不同取值。首层比较本身不能把较高导子的有限样本当作 Rubin 整基的整个 family，也未将 $\mathscr L$ 的 Iwasawa 不变量认作 $\mathcal A_p$ 的不变量。

## 15. 两模型的同电荷规范与真实参考整单位

本节起谱变量一律为 $X$。原第一来源 $S_{17}$、$m=34$ 在 $E_{17}$，参考 $\Theta_2=\sigma_1^2x_1$ 在 $E_1$。对各自模型的严格 LT 坐标分别记 $v_b,L_b,T_{g,b},\mathfrak C_{b,m}$。选 R1067 既定的模型同构，$\vartheta=17^{1/6}$，$z_1=\vartheta z_{17}$。在当前未分歧二次局部域中 $\vartheta$ 为单位：$\mathbf F_p^\times$ 均为 $\mathbf F_{p^2}^\times$ 的六次幂，因为 $6\mid p+1$，再用 Hensel；六个可能根也全在该域。原指定嵌入给其中既定一根。以 $\iota(v)$ 表示模型同构后的实际 $v_1$ 坐标，线性项为 $\vartheta v$，但不以线性截断替换它。由 $\sigma_{17}(z)=\vartheta^{-1}\sigma_1(\vartheta z)$，对完整 $\mu_d$ 中央化再比较 $T_g$，得到
$$
T_{g,17}(v)=T_{g,1}(\iota(v)),\qquad
\frac{L_1(\iota(v))}{L_{17}(v)}=\frac{\vartheta v}{\iota(v)} .
$$
这里 $T_g(v)$ 简记其原 $u(v)$ 代入。$\iota$ 与各 CM 标量交换；这是几何同构，仍在两套严格坐标中分别作代换。

取 R1062§13 的准确范数 $N(a)=17$ 的原局部 CM 单位，置
$$
\Psi(W)=([a]\iota(v))^d,\qquad
D_a(W)=\frac{L_1([a]\iota(v))}{L_{17}(v)^{17}} .
$$
$D_a,D_a^{-1}\in1+W\mathcal O[[W]]$：先在 $E_1$ 用 R1062(G35) 的范数 $17$ 形式 Miller 比，乘完整的 $T_{g,1}$ 比，再用上式的 $(\vartheta v/\iota)^{17}$，最后按 $\mu_d$ 不变下降。$\Psi$ 有整逆。等电荷关系 $2N(a)=34$ 给
$$
 T_{17,34}(D_a^2 f\circ\Psi)
=D_a^2 (T_{1,2}f)\circ\Psi .
$$
这是同一局部几何标记下的函数恒等。逐项作用于 $\mathsf D^n1$，再取真实闭盘极限，得
$$
\mathfrak C_{17,34}^{-1}(D_a^2 f\circ\Psi)
= V_a(X)\mathfrak C_{1,2}^{-1}f(X),\qquad
V_a(X)=\mathfrak C_{17,34}^{-1}(D_a^2)\in1+X\mathcal O[[X]] .
$$
右侧的乘法在谱变量中。证明中使用 $\mathfrak C^{-1}\mathsf D=X\mathfrak C^{-1}$，未使用 $\mathfrak C$ 具有乘法性。

记 $f_{b,m}(v)=L_b(v)^{-m}A_{b,m}(z(v))=v^m T_{g,b}^{-m}\phi_{b,m}$，$\bar f_{b,m}=\frac1d\sum_{\zeta\in\mu_d}f_{b,m}(\zeta v)$，横线在此专指有限角平均。原 $A_{17,34}=S_{17}, A_{1,2}=\Theta_2$。R663(9)–(11)给 $\bar f_{17,34}=W\mathcal B_{34}$。而 $f_{1,2}=v_1^2T_{g,1}^{-2}x_1\in1+v_1\mathcal O[[v_1]]$，故 $\bar f_{1,2}\in1+W_1\mathcal O[[W_1]]$。令
$$
\mathscr E_2=\mathfrak C_{1,2}^{-1}\bar f_{1,2}\in1+X\mathcal O[[X]],\qquad
\mathscr J(X)=\frac{X\mathscr L_{34,\eta}(X)}{V_a(X)\mathscr E_2(X)}.
$$
因此 $\mathscr J'(0)=j_{34}/(d\log_p\eta)$，分母是全部层上的实际整单位。

## 16. 所有 $p^{2i}$ 导子的 absolute Klein 采样

以下只用 $b=17,m=34$ 和 $b=1,m=2$。两模型各取 R716/R1067 自己的 $\Omega_{{\rm CM},b}$、$\mathfrak k_b$ 和固定 $\phi_{b,m}$。取一个 primitive 整数标签 $v_0\bmod p^i$，$T=P(\Omega_{{\rm CM},b}v_0/p^i)$。以下记 $v_T$ 为严格 LT 坐标，避免与整数标签混用。令
$$
k_b(v_0)=\mathfrak k_b(\Omega_{{\rm CM},b}v_0/p^i),\qquad
\mathcal A_{b,m}(v_0/p^i)= k_b(v_0)^m\phi_{b,m}(T).
$$
$k_b(v_0)$ 为代数数且 $v_p(k_b(v_0))=v_p(v_T)$。为直接支付，取奇整数 $n=1+2p^i$，则 $[n]T=T$，原 $\psi_n(T)=k_b(v_0)^{1-n^2}$ 乘 R703(2) 的根单位（准周期公式在 $p^i$ 分母逐字成立）。非零 $\psi_n(T)$ 代数，故 $k_b(v_0)$ 代数；同一个整 Miller 式给 $v_p(\psi_n(T))=(1-n^2)v_p(v_T)$，因为 $n$ 在 $p$ 为单位，非零核点均不落入形式盘。所称估值随即得到。

对任意 $h\in\mathcal O_{K_p}^{\,1}$，选 $\widehat h\in\mathbb Z[\omega]$ 满足 $\widehat h=h\bmod p^{2i},\ \widehat h=1\bmod2$。对 $hT$ 以上标记 $k_b(\widehat h v_0)$，保完整代表。准确有
$$
U_{h,b}(W_T)=
\frac{v_T}{T_{g,b}(T)k_b(v_0)}
\frac{T_{g,b}(hT)k_b(\widehat h v_0)}{v_{hT}} .
$$
先以 $h=A/B,\ A,B\in\mathcal O_K,\ N(A)=N(B),\ A=B=1\bmod2$、$p$ 处为单位证明。取 $Bx=v_0\bmod 2p^{2i}$。等范数给 $\psi_A(T_x)/\psi_B(T_x)=k_b(Ax)/k_b(Bx)$，两边坐标及完整 $T_g$ 附因子即为上式。标签差 $2p^{2i}\mathcal O_K$ 不改 Klein 值，因为相应准周期的半特征及指数均为1。一般 $h$ 由此等范数有理元逼近：局部 Hilbert 90 在此可直接用 $c/\bar c=h$，$h\ne-1$ 时取 $c=1+h$ 并除去共同有理 $p$ 次幂，$h=-1$ 可取 $c=\delta$；再用 CRT 取 $c_n=1\bmod2$、$c_n\to c$ 且 $p$-单位。$h_n=c_n/\bar c_n$ 充分近时稳定同一个模 $2p^{2i}$ 代表类。左侧由原形式比逐系数连续及整尾在固定 $v_T$ 一致收敛，故上式对 $h$ 成立。这里只使用 $T_g$ 整单位值，不需要预设高层 $T_g$ 是代数数。

设 $H=p^{i-1}$、$\lambda$ 是所在 $\eta$ 轨道允许的本征值。对 $h=\zeta\eta^l,\ \zeta\in\mu_d,\ 0\le l<H$ 定义真正完整原和
$$
\mathscr S_{b,m,i,\lambda}(v_0)=
\sum_{\zeta,l}\lambda^{-l}\,
 \mathcal A_{b,m}(\widehat{\zeta\eta^l}v_0/p^i).
$$
若将 $l$ 增加 $H$，准周期给前面已证的 $\epsilon_i=\lambda^H$，与外权准确抵消；代表模 $2p^{2i}$ 的进一步变化已在上一段支付。由于 $U_{\zeta,b}=1$，有限 $\mu_d$ 平均与上式直接给
$$
\ell_{\lambda,b,m}(\bar f_{b,m})
 =\frac{1}{d}
\left(\frac{v_T}{T_{g,b}(T)k_b(v_0)}\right)^m
\mathscr S_{b,m,i,\lambda}(v_0).
$$
括号为实际 $p$ 单位；系数域中选定的所有根及准周期相位均保。此式本身不把括号称为在 $i$ 上固定的代数 period。

由模型同构和 $[a]$ 把目标 $T$ 送到参考 $T'$，其标签可取 $v'_0=a v_0\bmod p^i$，因为原两周期满足 $\Omega_{{\rm CM},1}=\vartheta\Omega_{{\rm CM},17}$。$\Psi$ 映同一轨道到对应轨道；完整 $D_a^2$ cocycle 给
$$
\ell_{\lambda,17,34}(D_a^2 f\circ\Psi)=D_a(W_T)^2\ell_{\lambda,1,2}(f).
$$
特别 $\lambda$ 在两条真实向量上完全相同，含全部 $p^{2i}$ 相位而不只模 $p$ 的范数关系。取 $f=\bar f_{1,2}$ 并比较相应谱特化，$\ell_{\lambda,17,34}(1)$ 精确消去。由于 $V_a\mathscr E_2$ 是整单位且该分母非零，
$$
\mathscr S_{1,2,i,\lambda}(v_0')\ne0,\qquad
v_p\mathscr J(\lambda-1)=
v_p\mathscr S_{17,34,i,\lambda}(v_0)
-v_p\mathscr S_{1,2,i,\lambda}(v_0').
$$
这里两条完整和先在同一固定标记下取比，所有剩余坐标及 $D_a$ 的确切单位性已经逐个支付。

## 17. 原全局 theta 周期及所有高导子的 Rubin 估值

给 $\mu_d$ 平凡、$\eta\mapsto\lambda^{-1}$ 的范数一局部角色记作 $\theta_\lambda$。它准确有导子 $p^{2i}$：$\eta$ 生成 $1+p\mathcal O$ 的范数一部分，而 $\lambda$ 阶为 $p^{2i-1}$。其余地点取同 R716§5 的紧代表延拓（类数一、全局 $\mu_6$ 上平凡）。真正的全局 Hecke twist 为 $\nu(z)=\theta_\lambda(z/\bar z)$，限制于局部范数一元时为 $\theta_\lambda^2$，同样有阶 $p^{2i-1}$。非 $p$ 的坏非分裂处整个角色仍平凡；好分裂处容许原未分歧因子。

为使用 Yang 的平方公式须核对原有限向量。各模型沿 R716(21)–(28)、R1067 第一 wild 偶重数式(12)–(14)的同一极化，取 $e_v^{(m)}=\rho_p(-h_m(v/p^i))\boldsymbol 1_{\mathbb Z_p}$。这里 $h_m$ 专指这些已付的 Heisenberg 位移矩阵；其行列式为带符号的 $m$，当前 $p$ 为单位。Lagrangian 平移与调制的正交关系给 $p^{2i}$ 个不同标签的向量正交且范数1，因为内积非零恰要求两位移差的两个坐标都在 $\mathbb Z_p$。真实 Weil 协变和不变球给 $\omega(g)e_v=e_{gv}$。更换整数代表 $v\mapsto v+p^i s$ 给 $e_{p^i}(m[s,v]/2)$ 的准周期，正是以上 Klein 幅度的相位。用 $\widehat h$ 表示 $h$ 的向量时模 $p^{2i}$ 精度足够。于是
$$
\varphi_{b,m,i,\lambda}=
(dH)^{-1/2}\sum_{\zeta,l}\lambda^{-l}
      e^{(m)}_{\widehat{\zeta\eta^l}v_0}
$$
恰有范数1；$dH$ 项为不同 $v\bmod p^i$。在 $p$ 的整个紧范数一群上本征字符为 $\bar\theta_\lambda$。其在生成元 $\eta$ 的本征值为 $\lambda$，在 $\mu_d$ 为1，末端相位由 $\epsilon_i=\lambda^H$ 支付。连续性覆盖整个群。非零单位向量给原 Hermitian 类的局部 dichotomy。

分母从 $p$ 改为 $p^i$ 不改 R716§3.1 非 $p$ 处的整性：在 $3$、$17$、其余奇处 $p^{-i}$ 为单位，在 $2$ 处仍为奇单位并保持平移/调制的原同奇偶条件。故所有非 $p$ 原 Schwarz 向量、绝对 splitting 及有理 Heisenberg 换元保持。无穷处仍为两条原零阶 Hermite；因此实际 theta-null 是对应 $C_{b,m}\mathscr S_{b,m,i,\lambda}/\sqrt{dH}$。Yang, *Theta liftings and Hecke L-functions* (1997), Cor. 2.4 及 Thms. 1.11, 2.6, 2.15 规定在非分裂分歧处取范数1的指定本征向量，不要求它只在第一个导子出现。紧商单位群 $\mu_6$、体积及全部原模型的 $C_{b,m}$ 保 R716/R1067 原归一。新增 $p$ 处在 $c(0)$ 中的因子为 $(1+p^{-1})^{-1}$，只依分歧非分裂集合；Yang (2.19) 左边为 $c(0)L$，解出 $L$ 时乘的是 $1+p^{-1}$。故实际单位范数 theta-null 平方的因子为 $(1+p^{-1})/(dH)=p^{-i}$。于是
$$
\frac{L(\psi_{17}\nu,1)}{\Omega_{\mathbf R,17}}
=48940416\,p^{-i}|\mathscr S_{17,34,i,\lambda}|^2,\qquad
\frac{L(\psi_1\nu,1)}{\Omega_{\mathbf R,1}}
=\tfrac16 p^{-i}|\mathscr S_{1,2,i,\lambda}|^2 .
$$
这些是指定复嵌入下的实际绝对平方。为取原 $p$ 进估值，复共轭把 $v_0$ 送到 $-\omega\bar v_0$、$h$ 送到 $\bar h=h^{-1}$、$\lambda$ 送到 $\lambda^{-1}$，两处改变同时作用，仍是同一组 $\lambda^{-l}$ 加权的和，种子改为 $-\omega\bar v_0$。新种子具有相同模 $p^i$ 范数，故属于原轨道：其商模 $p^i$ 是范数一元，能 Hensel 提升到真正范数一群（把范数的近一单位平方根除去即可）。换轨道起点只给 $\lambda$ 幂和原 Klein 准周期根。后者在全体 $h$ 下为同一根：若种子差 $p^i s$，则相位中的 $[hs,hv_0]=N(h)[s,v_0]=[s,v_0]\bmod p^i$，相同半特征也由 $m$ 偶支付。因此非零时每个和与其复共轭只差根单位，在固定 $p$ 位的绝对平方估值为两倍该和估值。

最后比较 R303 的原整系数 $\mathcal A_p(T)$，原生成元保 $\gamma$，$t_\nu=\nu(\gamma)-1$。两曲线的整 Rubin 基、$F_\vartheta$ 及固定 CM 周期比较全沿 R303 和 R1067§4；$\Omega_{\mathbf R}/\Omega_{\rm CM}=1-\omega$ 两边皆为固定单位。Burungale–He–Kobayashi–Ota, *Hecke L-values, definite Shimura sets and Mod $\ell$ non-vanishing*, Thms. 4.14–4.15 对所有本层奇数指数 $2i-1$ 的有限角色分别给两模型的非零 signed 局部因子 $\delta_\nu$；对于实际整基生成元，其估值只依 $p,2i-1$，故取比后准确抵消。同一结论也可直接沿 R303 的整同构运输局部整基，两个基的差为整 Iwasawa 单位。两条原模型根号皆正，故这些奇数指数角色属于同一允许符号。参考的整 Rubin 函数是单位，且上面已从具体向量证明参考 theta-null 非零。两条固定实常数 $48940416,1/6$ 均为当前位单位；共同 $p^{-i}$ 必须先保留再取比。因而每一层都得到
$$
\boxed{
v_p\mathcal A_p(t_\nu)=2v_p\mathscr J(\lambda-1)
=2v_p\bigl((\lambda-1)\mathscr L_{34,\eta}(\lambda-1)\bigr).}
$$
若目标和为零则两端同为无穷。即便 $\gamma$ 与所选 $\eta$ 的局部 Artin 标记不同，$t_\nu$ 与 $\lambda-1$ 仍同为确切阶 $p^{2i-1}$ 的单位根减一；这里比较的是固定实际角色的两个特化，并未把变量认同。

对非零 $A\in\mathcal O[[X]]$，确切阶 $p^k$ 的 $\alpha$ 在充分大 $k$ 满足 $v_p(A(\alpha-1))=\mu(A)+\lambda(A)/\varphi(p^k)$。这是取共同 $p^\mu$ 后首单位项严格主导的 Weierstrass 估值。原 $\mathcal A_p$ 非零且 $\mu(\mathcal A_p)=0$（同 R303 及已用的 BHKO 定理）。上式遂先迫 $\mathscr L_{34,\eta}\ne0$。固定 $p$ 令 $i$ 增大，先取极限，再乘回 $D_i$，得到真实不变量关系
$$
\boxed{\quad
\mu(\mathcal B_{34})=0,\qquad
\lambda_p=2\bigl(1+\operatorname{ord}_{W=0}\overline{\mathcal B}_{34}\bigr).
\quad}
$$
没有由这些估值等式宣称两条命名幂级数只差整单位。R1067 的中央/第一 wild 精确重数于是直接约束同一个几何模 $p$ 阶数，而证明无穷不同 $p$ 的所需上界或原 $j_{34}$ 非零仍须独立算术输入。

原始文献：[Yang 作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)，[BHKO 作者全文](https://arxiv.org/pdf/2408.13932)，特别 BHKO §4.4.1、Thms. 4.14–4.15。原固定模型与标准基见 R290、R302、R303、R696(17)、R703、R705、R716 及 R1067 第一 wild 偶重数 §§2–5、10。

具体原文位置：Yang 作者稿 p.13 Thm.1.11、(1.16)后之 $c(s)$，p.17 Cor.2.4 (2.9)，p.19 Thm.2.6 (2.19)，p.24 (2.29)后和Thm.2.15；BHKO §4.4.1（论文pp.29–30）Thms.4.14–4.15及Thm.1.5（当前两固定Q-curve、好惰性 $p\nmid6h_K$）给本文所用 $\mu=0$。

## 18. 原中央 Newton 商的全整权延拓

续前节，保 $b=17,N=34$ 与 $b=1,N=2$，$a$ 的局部范数准确为 $17$，模型坐标 $z_1=\vartheta z_{17}$。对整数 $k\ge0$、$d\mid k$ 置
$$
\Lambda_{b,N,0,k}(F)=[z^k]L_b(v_b(z))^N F(v_b(z)^d).
$$
此泛函只需原点有限 jet，因而在任一严格原点闭盘上有界。令 $(T F)(W)=U_\eta(W)^N F(\Phi_\eta(W))$，原正式乘法式立刻给 $\Lambda(TF)=\eta^k\Lambda(F)$。取 $F=W^{k/d}$ 可见 $\Lambda(F)=1$，所以 $\Lambda$ 非零。由 $\mathfrak C_{b,N}$ 的满性及 $\mathfrak C(X^n)= (T-I)^n1$，必有 $\Lambda(1)\ne0$；并对全整 $F$ 有
$$
\Lambda(F)=\Lambda(1)\,(\mathfrak C_{b,N}^{-1}F)(\eta^k-1).
$$
该结论同样涵盖 $k=0$。原 $L_b$ 为 $\mu_d$ 不变，且 $z([\zeta]v)=\zeta z(v)$。对 $\bar f_{b,N}$ 取此泛函时，全部项恰成为 $N$ 次原 sigma 来源旋转的 $k$ 次系数，角权 $\zeta^k=1$。因此 $\Lambda_{17,34,0,k}(\bar f_{17,34})=s_{17,k}$，$\Lambda_{1,2,0,k}(\bar f_{1,2})=\beta_k$，后者是 R303(2) 的 $[z^k]\Theta_2$。两模型的真实交织式则给
$$
\Lambda_{17,34,0,k}(D_a^2 F\circ\Psi)=(a\vartheta)^k\Lambda_{1,2,0,k}(F).
$$
由于 $V_a\mathscr E_2$ 谱上整单位，同时得 $\beta_k\ne0$。在比值中消去目标线同一 $\Lambda(1)$，有确切数值
$$
\mathscr J(\eta^k-1)=(a\vartheta)^{-k}s_{17,k}/\beta_k.
$$
R303(3),(23) 给 $s_{17,k}=\vartheta^{k-6}\alpha_k$，以及当 $k=du$ 时 $\alpha_{du}/\beta_{du}=17^u J_p(u)/J_{0,p}(u)$；两个阶乘在相同位置消去。$17/a^d\in1+p\mathcal O$ 来自 $a\bar a=17$、剩余域 Frobenius 为共轭。因此先对 $u\in\mathbf Z_{\ge0}$、继于整个原闭盘有准确身份
$$
\boxed{\mathscr J(\eta^{du}-1)=\frac1{17}\left(\frac{17}{a^d}\right)^u\frac{J_p(u)}{J_{0,p}(u)}.}
$$
两端均按原 $p$ 进指数在 $|u|\le1$ 解析，参考 $J_{0,p}\in1+p\mathbf Z_p\langle u\rangle$。因而这是真实全整谱系数给原指定中央 germ 的延拓，含全部模型与指数因子。微分后 $j_{34}=J_p'(0)/17$，零阶 $\operatorname{ord}_{X=0}\mathscr J=e_{\rm cent}$。

## 19. 同一个谱在各挠点的物理 Hermite 导数

取一实际 primitive $Q$，阶 $n=p^i$，严格参数 $v_Q$ 及 $W_Q=v_Q^d$。局部不变时间记为 $t$，$Q+t$ 指群法平移，$v(Q+t)$ 在充分小盘按 $t$ 解析且导数非零。选择适当小的盘，取唯一 $G_{b,N,Q}(t)$ 使 $G(0)=1$、$d\log G=Na_b(W)dW$。以下取局部有限 jet，所以不需要 $L_b$ 的 sigma 级数越原首挠半径收敛。准确定义
$$
\Lambda_{b,N,Q,k}(F)=[t^k]G_{b,N,Q}(t)F(W(Q+t)).
$$
由全开盘 $d\log U_h=h^*(a\,dW)-a\,dW$ 与常数项，得
$$
\Lambda_{Q,k}(T^l F)=u_l(Q)\eta^{lk}\Lambda_{\eta^lQ,k}(F),\quad u_l(Q)=U_{\eta^l}(W_Q)^N.
$$
因此在同一前节轨道 ($H=p^{i-1}$、$\lambda^H=\epsilon_i$) 上，$\Lambda_{\lambda,k}:=\sum_{l<H}u_l\lambda^{-l}\Lambda_{\eta^lQ,k}$ 在 $T$ 下的本征值为 $\lambda\eta^k$。对不同 $W_{\eta^lQ}$ 作有限 Hermite 插值，可在选择的一点指定阶 $k$ 导数而令其他点的 $k$ 阶以下 jet 全零。$W(Q+t)'(0)\ne0$ 保此主系数非零；适当乘标量使多项式整。因此 $\Lambda_{\lambda,k}\ne0$，同一循环性再次给
$$
\Lambda_{\lambda,k}(1)\ne0,\qquad \Lambda_{\lambda,k}(F)=\Lambda_{\lambda,k}(1)(\mathfrak C_{b,N}^{-1}F)(\lambda\eta^k-1).
$$
这里使用普通 Taylor 系数 $[t^k]$；把两边换成 $D_t^k$ 须同时乘 $k!$。

须实际对准原 Miller 物理微分。设该模型原 $n$ 除法函数 $r_n=\sigma(nz)/\sigma(z)^{n^2}$，$\Xi_b$ 为 R1063(H6) 的同模型 zeta Laurent 函数（$b=17$ 时保 $b^j$）。原正式等式 $D\log r_n=n\Xi_b([n]P)-n^2\Xi_b(P)$ 在开形式盘乘去两端有限的极后延拓。$n\Xi_b([n](Q+t))=1/t+O(t)$，故常数项给
$$
\Xi_b(Q)=-\frac{D^2r_n(Q)}{2n^2Dr_n(Q)}=\zeta(q_Q)-\eta_{q_Q},\quad q_Q\in n^{-1}\Lambda_b.
$$
末等式由原复除法函数在 $q_Q+t$ 展开，保 $nq_Q$ 的准周期；任意 $n=p^i$ 都相同。因 $D\Xi_b=-x_b$，全部高阶局部 jet 也恰是 $\zeta(q_Q+t)-\eta_{q_Q}$ 的原代数 Taylor jet。令 $k_b(Q)=\mathfrak k_b(q_Q)$，$\mathscr F_{b,N,Q}(t)=\exp[-N\eta_{q_Q}(t+q_Q/2)]A_{b,N}(q_Q+t)$，它是 R1067(15) 的实际标签。把 $Na\,dW=N(\Xi_b\,dt+d\log(T_{g,b}/v))$ 积分并以 $G(0)=1$ 固定常数，得正规化等式
$$
G_{b,N,Q}(t)f_{b,N}(v(Q+t))=\left(\frac{v_Q}{T_{g,b}(Q)k_b(Q)}\right)^N\mathscr F_{b,N,Q}(t).
$$
即便 $\phi_{b,N}(Q)=0$ 也可用左边的有理因子直接相乘，不需将它除去。对 $h=\zeta\eta^l$，局部时间需乘 $\zeta$ 或 $\eta^l$；以上本征权已保 $\eta^{lk}$。角平均余下 $\zeta^k$，在 $d\mid k$ 时恰为1。结合上一节全精度 $U_h$ 的绝对中心返回，有
$$
\Lambda_{b,N,\lambda,k}(\bar f_{b,N})=
\frac{K_{b,N,Q}}d\sum_{\zeta,l}\lambda^{-l}[t^k]\mathscr F_{b,N,\widehat{\zeta\eta^l}Q}(t),\qquad
K_{b,N,Q}=\left(\frac{v_Q}{T_{g,b}(Q)k_b(Q)}\right)^N.
$$
帽号含所选固定 $2p^{2i}$ CRT 代表，仍按前节的准周期相位理解。$Q'=[a]\iota Q$ 的同电荷交织在局部时间乘准确的 $a\vartheta$，从而
$$
\Lambda_{17,34,\lambda,k}(D_a^2F\circ\Psi)=D_a(W_Q)^2(a\vartheta)^k\Lambda_{1,2,\lambda,k}(F).
$$
这给所有 $i\ge1$、$k\ge0,d\mid k$ 的原两条完整 Hermite 和：参考和非零，目标和可零；取比时除了显示的 $D_a^2,(a\vartheta)^k$ 与两个明确的 $K_{b,N,Q}$，其余共同泛函常数都相消。

特别在原首层 $H=1$，沿 R716/R1067 既定的 $\chi_r(v)$ 选种子。若用非原初始种子，其精确 Hall 权须再乘固定的 $\chi_r(v)$；该常数不依 $k$。记 $B_r$ 为上述 $K_{17,34,Q}/(D_a(W_Q)^2K_{1,2,Q'})$ 乘相应参考与目标种子字符比。则对全部合法整数 $d\mid k$，原 R1067(15) 的同一批和准确满足
$$
\mathscr J(\lambda\eta^k-1)=B_r(a\vartheta)^{-k}\,\frac{\mathscr D_{34,r,k}}{\mathscr D_{2,17r,k}}.
$$
可将 R1067(25) 的合法步长 $M$ 同乘一个正整数，使 $(A_{34,*}/(a\vartheta A_{2,*}))^M$ 在指数收敛盘中；这是同一 germ 的有限指标重参数。两边分别沿 $k=Ml$，其实际 $A_{N,*}^{Ml}$ 因子给准确等式
$$
\boxed{\mathscr J(\lambda\eta^{Mt}-1)=B_r\left(\frac{A_{34,*}}{a\vartheta A_{2,*}}\right)^{Mt}
\frac{\mathcal H_{34,r}(t)}{\mathcal H_{2,17r}(t)}.}
$$
先在全部非负整数 $l$ 用已付的(26)，再以 $l=p^j\to0$ 在参考单位邻域解析延拓。$B_r$ 是准确固定单位，包括原 wild 相位。由此 $\operatorname{ord}_{X=\lambda-1}\mathscr J=\operatorname{ord}_{t=0}\mathcal H_{34,r}$，整个原中央与首层 Hall 权函数现在是同一整权函数的两个真实局部展式。

## 20. 实际高度给 Rubin 不变量的间隙

设 $p$ 足够大到 R707 的固定高度界适用，$D=p-1$。对第一 wild $x=\lambda-1$，原始 $v_p(x\mathscr L(x))=v_p(\mathcal T_{34,T})$，其参考固定整单位。若该迹非零，则 R707 增补给
$$
 v_p(x\mathscr L(x))\le\tfrac34+\frac{\tfrac14\log(1+\log p)+O(1)}{\log p}<1.
$$
因为 $\mu(x\mathscr L)=0$，$n=\lambda(x\mathscr L)=\lambda_p/2$。若 $n\ge D$，其前 $D$ 个系数全部含 $p$，从 $D$ 次起各项估值也至少1，矛盾。故 $n<D$，在 $x$ 处首单位项严格主导所有项，得到精确及上界
$$
\lambda_p=2(p-1)v_p(\mathcal T_{34,T})\le \tfrac32(p-1)+O\left(\frac{p\log\log p}{\log p}\right).
$$
若该迹为零，R1067(8) 已给 $\lambda_p\ge 2e_{\rm cent}+2(p-1)\ge2p$。反之若 $\lambda_p\ge2(p-1)$，前述严格单元主导已排除非零迹。因此充分大的允许 $p$，该迹是否为零等价于原 $\lambda_p\ge2(p-1)$，该阈值的上方实际从 $2p$ 开始；原中央坏且迹零时从 $2p+2$ 开始。以上间隙应用的是同一原迹的实际高度，保留两支并未选择其中一支。

## 来源

- [R663](R663-original-lubin-tate-residues-and-closed-boundary-equivalence.md)：本文所指原来源、坐标、连接或角色规范。
- [R639](R639-complete-original-central-gauge-and-full-formal-disc-stokes.md)：本文所指原来源、坐标、连接或角色规范。
- [R1062](R1062-original-translated-miller-jets-and-critical-weight-germs.md)：本文所指原来源、坐标、连接或角色规范。
- [R694](R694-original-cm-kummer-descent-and-full-norm-one-trace.md)：本文所指原来源、坐标、连接或角色规范。
- [R703](R703-original-hall-phase-and-finite-fourier-return.md)：本文所指原来源、坐标、连接或角色规范。
- [R705](R705-original-wild-character-and-absolute-weil-projection.md)：本文所指原来源、坐标、连接或角色规范。
- [R710](R710-original-all-order-central-kernel-and-exact-boundary-remainder.md)：本文所指原来源、坐标、连接或角色规范。
- [R681](R681-original-torsion-gauge-and-finite-algebraic-residues.md)：本文所指原来源、坐标、连接或角色规范。
- [R716](R716-original-wild-global-theta-period-and-exact-central-l-value.md)：本文所指原来源、坐标、连接或角色规范。
- [R696](R696-original-absolute-roots-p2-field-and-linear-height-trace.md)：本节原全Hall、Katz质量及首wild Rubin准确归一。
- [R1063](R1063-original-tame-zero-hall-and-five-layer-miller-return.md)：本节原全Hall、Katz质量及首wild Rubin准确归一。
- [R1067](R1067-original-first-wild-rubin-even-multiplicity.md)：本节原全Hall、Katz质量及首wild Rubin准确归一。
