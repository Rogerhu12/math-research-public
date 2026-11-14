# R144 附注：平方共振核等于一个有界代数限制

日期：2026-11-12。作者：l2_moments；核化简由根代理提出并共同逐域核验。
状态：完整独立附注，供 R144 附录使用。不修改已审主稿。

本文准确刻画 R144 尚未排除的唯一平方值，不宣称该核已经为零。

## 1. 记号及安全因子

设
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad (a_j)\in\ell^2,\qquad
j_0=\min\{j:a_j\ne0\},\quad a=a_{j_0}\ne0,
\quad h=2^{j_0},\quad d=W_h.
$$
令 $X=X_u$ 为 R125 的第一阶闭乘子，并置
$$
B_2=\sum_j a_j^2(I-V_j^2)\in\mathcal A_h,
\qquad \mathcal A_h=\overline{\mathbb C[I,A^h]}^{\|\cdot\|}.
\tag{1.1}
$$
此级数算子范数绝对收敛，$\chi(B_2)=0$。在唯一字符为 $a$ 的分支取
$$
Y=(a^2I-B_2)^{1/2}\in\mathcal A_h,
\qquad \chi(Y)=a.
\tag{1.2}
$$
这是围绕 $\sigma(B_2)=\{0\}$ 的真正全纯演算。特别地，$Y$ 有界可逆，保持所有 $X$ 的自然幂域，并与 $X$ 域交换。

R142 的首系数计算给
$$
c_h(B_2)=\frac{4a^2}{d},\qquad c_h(Y)=-\frac{2a}{d}.
\tag{1.3}
$$
对 dyadic $\zeta$ 且 $\zeta^h\ne1$，R139 的实际余数除法给
$$
\gamma_\zeta(X+Y)-(X+Y)=A^h U_\zeta,
\qquad
\chi(U_\zeta)=-\frac{4a}{d}(\zeta^h-1)\ne0.
\tag{1.4}
$$
因而 $U_\zeta\in\mathcal A_h$ 是有界单位。R125 的闭加性 cocycle 排核准则（也即 R142 使用的闭有界扰动接口）遂给
$$
\boxed{\ker(X+Y-\lambda I)=0\quad(\lambda\in\mathbb C).}
\tag{1.5}
$$
这里安全因子的有界 gauge 差已真实提取 $A^h$；没有把一般零字符代数元任意除以 $A^h$。

## 2. 固定正则化核恰等于危险因子核

取 R128/R140 的任意固定共同第一阶正则化 $R=R(t)$。记
$$
P(X)=X^2+B_2-a^2I=X^2-Y^2,
\qquad \operatorname{Dom}P(X)=\operatorname{Dom}X^2,
$$
$$
S=P(X)R^2\in\{A\}',\qquad M=\ker S.
\tag{2.1}
$$
R144 已证明 $R^nH\subseteq\operatorname{Dom}X^n$，且对任意闭 $A$ 不变空间，固定 $R^n$ 的像稠密。尤其 $R^2M$ 在 $M$ 稠密。

若 $x\in R^2M$，则 $x\in\operatorname{Dom}X^2$ 且 $P(X)x=0$。由于 $Y$ 保持 $\operatorname{Dom}X$，自然域上的因式分解合法：
$$
P(X)x=(X+Y)(X-Y)x.
$$
由 (1.5)，得到 $(X-Y)x=0$。对任意 $x\in M$，用 $R^2M$ 中的向量 $x_n\to x$，则
$$
Xx_n=Yx_n\longrightarrow Yx.
$$
$X$ 闭，故 $x\in\operatorname{Dom}X$ 且 $Xx=Yx$。因此
$$
M\subseteq\ker(X-Y).
\tag{2.2}
$$

反之，若 $Xx=Yx$，则 $Yx\in\operatorname{Dom}X$，所以 $x\in\operatorname{Dom}X^2$ 且
$$
X^2x=XYx=YXx=Y^2x.
$$
全部有界交换子保持 $\ker(X-Y)$，特别 $R^2x$ 仍在此核内，于是 $Sx=P(X)R^2x=0$。结合 (2.2)，
$$
\boxed{
\ker\bigl((X^2+B_2-a^2I)R^2\bigr)
=\ker(X-Y)=M.
}
\tag{2.3}
$$
进一步逐阶归纳给
$$
\boxed{M\subseteq\bigcap_{n\ge1}\operatorname{Dom}X^n,
\qquad X^n|_M=Y^n|_M.}
\tag{2.4}
$$
特别 $X_M$ 是一个定义在整个 $M$ 上的有界算子，等于 $Y|_M$。这不是从一般一阶闭乘子的限制自动有界，而是由特定二次核和安全因子的单射性推出。

## 3. 与 R131 真正二阶闭乘子的核一致

令 $T=X_{u^2-a^2}$ 为 R131 的二阶闭乘子。有限柱为其图核心，$T^*=CTC$，且 $\overline{\operatorname{Ran}T}=\operatorname{cyc}_A(u^2-a^2)$。

R134 的真实二阶 Bell 恒等式与一阶幂域证明在每个有限柱 $z$ 上给
$$
Tz=P(X)z.
$$
对 $x\in\operatorname{Dom}X^2$，利用有限柱 $z$ 和 $B$ 对称性，
$$
B(x,Tz)=B(X^2x+(B_2-a^2I)x,z).
$$
有限柱是 $T$ 的图核心且 $T$ 为 $C$ 自伴，通常伴随定义域判据遂给
$$
\operatorname{Dom}X^2\subseteq\operatorname{Dom}T,
\qquad T|_{\operatorname{Dom}X^2}=P(X).
\tag{3.1}
$$
它还说明 $T=\overline{P(X)}$，但无需声称两个原定义域相等。

由 (2.4) 和 (3.1)，$M\subseteq\ker T$。反之，若 $x\in\ker T$，R131 的全部有界交换子域交换给
$$
R(s)^2x\in\ker T\cap\operatorname{Dom}X^2,
\qquad P(X)R(s)^2x=0.
$$
由安全因子单射性，这些向量均属于 $\ker(X-Y)=M$。当 $s\downarrow0$ 时 $R(s)^2x\to x$；$M$ 闭，故 $x\in M$。于是
$$
\boxed{
\ker X_{u^2-a^2}
=\ker(X-Y)
=\ker\bigl((X^2+B_2-a^2I)R(t)^2\bigr)
\quad(t>0).
}
\tag{3.2}
$$
由 $C$ 自伴性，剩余循环性问题等价于上述共同核为零。

## 4. 删去首位后的精确形式

写
$$
v=u-a\chi_{j_0},\qquad W=X_v,
\qquad Z=\sum_{j>j_0}a_j^2(I-V_j^2)\in\mathcal A_{2h}.
\tag{4.1}
$$
$v$ 保留常数项 $a_*$。由
$$
B_2=a^2(I-V_{j_0}^2)+Z,
\qquad Y^2-a^2V_{j_0}^2=-Z,
$$
且 $\chi(Y+aV_{j_0})=2a\ne0$，得到真实有界单位
$$
H=(Y+aV_{j_0})^{-1}\in\mathcal A_h,
\qquad Y-aV_{j_0}=-ZH.
$$
因而在相同第一阶闭域上，
$$
\boxed{X-Y=W+ZH.}
\tag{4.2}
$$
所以任何可能的非零核还必须满足
$$
W|_M=-ZH|_M.
\tag{4.3}
$$
右边有界，而 $Z$ 只含首位之后的平方系数。
若全部尾系数为零，(4.2) 退化为 $a_*I$；其核非零恰好发生在 $a_*=0$，此时原符号 $u^2-a^2$ 本来就是零向量。

## 5. 尾平方误差能受控，但解析头配对仍是缺口

记
$$
B_{2,m}=\sum_{j<m}a_j^2(I-V_j^2),\qquad
Y_m=(a^2I-B_{2,m})^{1/2},\qquad \chi(Y_m)=a,
\qquad t_m=\left(\sum_{j\ge m}|a_j|^2\right)^{1/2}.
$$
$Y_m$ 是真正解析芽在 $A$ 上的值。由于 $\|V_j\|\le6$，
$$
\|B_2-B_{2,m}\|\le37t_m^2.
$$
全纯演算连续性给 $Y_m\to Y$；从
$$
Y-Y_m=-(B_2-B_{2,m})(Y+Y_m)^{-1}
$$
可知存在只依赖固定 $a,B_2$ 的常数 $C_Y<\infty$，使所有充分大的 $m$ 满足
$$
\boxed{\|Y-Y_m\|\le C_Yt_m^2.}
\tag{5.1}
$$

固定一个非零候选核向量 $g\in M$，以 R104 选 $n_0$ 使 $\beta=B(A^{n_0}1,g)\ne0$。令
$$
\Phi_{g,m}f=\bigl(B(A^{n_0}(2N_j-I)f,g)\bigr)_{j\ge m}.
$$
R104 在纯高尾第一阶空间上的左界为 $|\beta|/2$，对充分大的 $m$ 统一成立。另一方面，对任意有界交换子 $D$，不能直接在全 $H$ 使用有限次数合成；但可将 $D$ 真实地移过每个测试，从常向量的合成得到
$$
\left\|\Phi_{g,m}(D1)\right\|_{\ell^2}
\le C_0 W_{n_0}\|g\|\,\|D\|,
\tag{5.2}
$$
其中 $C_0$ 与 $m,D$ 无关。确实
$$
\left\|\sum_j c_j(2N_j-I)D1\right\|
\le\|D\|\left\|\sum_j c_j(2N_j-I)1\right\|
\le C_0\|D\|\|c\|_2.
$$

把 $u-Y1$ 写为
$$
u-Y1=h_m+\sum_{j\ge m}a_j\chi_j-(Y-Y_m)1,
\qquad h_m=a_*+\sum_{j<m}a_j\chi_j-Y_m1.
$$
$h_m=F_m(A)1$，$F_m$ 是真正解析芽。由于 $g\in\ker(X-Y)$，所有实际矩为零，故 (5.1)—(5.2) 和 R104 给
$$
\frac{|\beta|}{2}t_m
\le\|\Phi_{g,m}h_m\|_{\ell^2}
+C_0W_{n_0}\|g\|C_Yt_m^2.
\tag{5.3}
$$
当 $m$ 足够大时，平方项可以吸收，得到
$$
\boxed{t_m\le\frac4{|\beta|}\|\Phi_{g,m}h_m\|_{\ell^2}.}
\tag{5.4}
$$
这一步没有除以某个最小非零 $a_j$；固定常数只依赖所选 $g,n_0,a,B_2$。

但 (5.4) 目前不是矛盾。即使 $h_m=1$ 是固定解析头，在纯模型中，相应数组也包含未知 $g$ 的一阶尾系数；这些系数可以以任意 $\ell^2$ 速度衰减。R104 对任意 $g$ 只给尾趋零，没有给超快实际进位速度。因此不能因 $F_m$ 是解析芽，就将 $\|\Phi_{g,m}h_m\|$ 换成 $O(\eta_m)$，也不能仅由平方误差的可吸收性宣称共振核为零。

本文留下的准确任务是排除 (2.4)/(4.3) 这种特定的有界代数限制，或为其中的解析头配对建立额外估计。一般第一阶全空间稠密值域、有限 chaos 双端分离及 R104 的尾左界，均不能单独替代这个步骤。
