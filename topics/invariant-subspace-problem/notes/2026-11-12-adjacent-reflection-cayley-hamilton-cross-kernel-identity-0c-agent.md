# 相邻两位反射的真实 Cayley--Hamilton 跨核恒等式

日期：2026-11-12。状态：完整接口；不另占结果号。它保留一个尾移位因子，不宣称排除慢平方核。

## 1. 范围与真实块分解

设实或复一阶行 $a=(a_i)\in\ell^2$ 的最低非零位为 $j$，并令 $k=j+1$。低于 $j$ 的恒等张量因子可略去；若 $j>0$，以下所有公式只多一个固定有限放大。

记

$$
a=a_j\ne0,\quad b=a_k,\quad B=N_k,\quad
\eta=\eta_j,\quad t=\eta B,
\quad N=N_j=\begin{pmatrix}0&t\\I&0\end{pmatrix}.
\tag{1.1}
$$

在第 $j$ 位的物理基中，$E_j=\left(\begin{smallmatrix}0&0\\I&0\end{smallmatrix}\right)$。令 $J_i=M_{\chi_i}$，以及 $U=J_jJ_k$。则

$$
UBU=-B,\qquad
N'=UNU=\begin{pmatrix}0&t\\-I&0\end{pmatrix},
\qquad N'-N=-2E_j.
\tag{1.2}
$$

最后一个等式是实际进位恒等式：$N=E_j+\eta E_j^*B$ 的进位项在同时反射两位时符号抵消。因而不能将两位差照抄成单比特的 $N$ 乘一个接近恒等的单位。

令

$$
X=\sum_i a_iV_i,
\quad B_2=\sum_i a_i^2(I-V_i^2),
\quad Y=\phi(B_2),\quad T=X-Y,
\tag{1.3}
$$

其中 $\phi$ 是零附近的标量全纯函数，并以通常全纯演算定义 $Y$。$T$ 的域是 $\operatorname{Dom}X$。记 $M=\ker T$。

将 $Y\in\overline{\operatorname{alg}}(N)$ 写成

$$
Y=U_0I+V_0N,
\qquad U_0,V_0\in\mathcal A_{\rm tail}
:=\overline{\operatorname{alg}}(B).
\tag{1.4}
$$

这是有界真实分解，不是形式除法。对多项式用 $N^2=tI$ 分成偶、奇项；在范数极限中，$U_0$ 是一个对角块，$V_0$ 是左下块，故两者在尾代数中范数收敛。上右块自动为 $tV_0$。

写

$$
s(t)=\frac{1+t}{1-t},\qquad r(t)=\frac2{1-t},
\quad V(N)=s(t)I-r(t)N,
$$

以及闭高尾一阶算子 $W=\sum_{i\ge k+1}a_iV_i$。于是

$$
T=HI+KN,
\quad H=W+a s(t)+bV(B)-U_0,
\quad K=-a r(t)-V_0\in\mathcal A_{\rm tail}.
\tag{1.5}
$$

在尾代数上记 $\gamma(F)=J_kFJ_k$，所以 $\gamma(B)=-B$。所有高于 $k$ 的真实 $N_i,V_i$ 被该反射固定，因而 $\gamma(W)=W$，且

$$
T'=UTU=H'I+K'N',\quad
H'=W+\gamma(H-W),\quad K'=\gamma(K).
\tag{1.6}
$$

特别地，$h=H'-H\in\mathcal A_{\rm tail}$ 有界。

## 2. 域与交换子

有限头拆分给出

$$
\operatorname{Dom}T
=\mathbb C^2\otimes\operatorname{Dom}W
=\operatorname{Dom}T'.
\tag{2.1}
$$

尾代数中的每个有界算子保持 $\operatorname{Dom}W$ 并与 $W$ 作真实域交换。物理头矩阵也保持该域。因此

$$
D:=T'-T=hI+K'N'-KN
\tag{2.2}
$$

是有界算子，保持 (2.1) 的域。下面每个涉及 $TD$ 的恒等式都在这个真实域上计算。

$T,T'$ 都是 $C$ 自伴闭算子；$U$ 与 $C$ 的共轭符号为正，因为它含两个单比特反射。因此有界差 $D$ 是 $C$ 对称的。

尾系数彼此交换，也与 $W,N,N'$ 交换。由

$$
NN'=-tJ_j,\quad N'N=tJ_j,
$$

得到精确有界交换子

$$
[T,D]=[T,T']=-2tKK'J_j.
\tag{2.3}
$$

没有把有限柱上的计算直接外推到未确定的最大域；(2.1) 及尾代数域保持已支付这个步骤。

## 3. 二次矩阵恒等式与一次真实除法

令 $R_0=K'N'-KN$。它的两条非对角块为 $t(K'-K)$ 和 $-(K'+K)$，所以

$$
R_0^2=t(K^2-K'^2)I.
$$

因此

$$
D^2-2hD+dI=0,
\qquad d=h^2-t(K^2-K'^2).
\tag{3.1}
$$

由于 $\gamma(h)=-h$，以及

$$
\gamma(K^2-K'^2)=-(K^2-K'^2),
$$

R124 的二余数组分解给出真正有界的

$$
h=Bh_1,\qquad K^2-K'^2=Bk_1,
\qquad h_1,k_1\in\overline{\operatorname{alg}}(B^2).
\tag{3.2}
$$

也可直接在 $B$ 自身的首位物理块中看出这一点：奇部分的左下块就是除以 $B$ 后的系数，故范数极限合法。

由此

$$
d=B^2D_0,\qquad
D_0=h_1^2-\eta k_1\in\overline{\operatorname{alg}}(B^2).
\tag{3.3}
$$

这里只对奇余数组做了一次已证有界除法。不能因 $K$ 的字符为零，就再写 $K=BK_1$ 为有界算子。

## 4. 跨核配对：可取消一次，仍保留一次

记 $\mathcal B(x,y)=\langle x,Cy\rangle$。对 $u\in M$、$w\in UM=\ker T'$，同域性和 $C$ 对称性给出

$$
\mathcal B(Du,w)=0.
\tag{4.1}
$$

又因 $D$ 保持真域，

$$
\mathcal B(D^2u,w)
=\mathcal B(Du,Dw)
=-\mathcal B(Du,Tw)
=-\mathcal B([T,D]u,w).
\tag{4.2}
$$

$h\in\mathcal A_{\rm tail}$ 保持 $M$ 且与 $D$ 交换，所以 $\mathcal B(hDu,w)=0$。将 (3.1) 代入 (4.2)，得到

$$
\mathcal B(B^2D_0u,w)
=-2\eta\,\mathcal B(BKK'J_ju,w).
\tag{4.3}
$$

$B$ 是实际归一化幂，且 $B$ 在 $M$ 上有稠密值域。由 $BU=-UB$，它在 $UM$ 上也有稠密值域。利用 $B$ 的 $C$ 对称性，将 (4.3) 两边同一个 $B$ 移到 $w$ 一端，再以真实稠密性延拓，得到

$$
\mathcal B(BD_0u,w)
=-2\eta\,\mathcal B(KK'J_ju,w).
\tag{4.4}
$$

写 $w=J_jJ_kv$，并使用 $J_j$ 的 $C$ 转置为 $-J_j$，有

$$
\boxed{\quad
\mathcal B(BD_0u,J_jJ_kv)
=2\eta\,\mathcal B(KK'u,J_kv),
\qquad u,v\in M.
\quad}
\tag{4.5}
$$

这是完整实际恒等式，不含形式误差。

若 $D_0$ 是尾代数单位，其逆保持 $M$，于是

$$
\mathcal B(Bu,J_jJ_kv)
=\mathcal B(Eu,J_kv),
\qquad E=2\eta KK'D_0^{-1}
\in\overline{\operatorname{alg}}(B^2).
\tag{4.6}
$$

例如，若已有单比特跨核范数界

$$
|\mathcal B(x,J_ky)|\le\varepsilon_k\|x\|\|y\|
\quad(x,y\in M),
$$

则 (4.6) 给出

$$
|\mathcal B(Bu,J_jJ_kv)|
\le\|E\|\varepsilon_k\|u\|\|v\|.
\tag{4.7}
$$

即使只用平凡界 $\varepsilon_k=1$，这个带 $B$ 的估计仍是有效的。它不是不带 $B$ 的两比特范数界。

## 5. 危险平方分支中的单位判据

现在令

$$
\phi(z)=\sqrt{a^2-z},\qquad\phi(0)=a,
$$

即 R208 的危险平方分支。形式系数在此只用于识别已经构造出的有界尾算子的字符。

由 $Y=aV(N)$ 在仅保留最低位时的恒等式，

$$
\chi(K)=0.
\tag{5.1}
$$

写 $H=W+H_b$。$H_b$ 的 $B$ 一次系数为

$$
[B]H_b=2b\left(\frac ba-1\right).
\tag{5.2}
$$

具体计算如下：$a s(t)$ 提供 $2a\eta$；$bV(B)$ 提供 $-2b$；$Y$ 的对角块一次系数为 $2a\eta-2b^2/a$。高于 $k$ 的 $N_i$ 都至少含 $B^2$，所以不影响这个一次系数。于是

$$
\chi(h_1)=-4b\left(\frac ba-1\right),
\qquad \chi(k_1)=0,
$$

以及

$$
\boxed{\quad\chi(D_0)=16b^2\left(\frac ba-1\right)^2.\quad}
\tag{5.3}
$$

因此，当 $b\ne0$ 且 $b\ne a$ 时，$D_0$ 是真正的尾代数单位，(4.6) 适用。没有要求 $a,b$ 为实数，也没有将一个一般零字符尾算子自动除以 $B$。

## 6. 仍缺少的步骤

从 (4.7) 和 $\overline{BM}=M$ 不能得到相同常数的不加权两比特估计。稠密性允许对精确零配对作延拓，却没有给 $B_M^{-1}$ 的范数。

同样，(4.6) 中的 $E$ 属于 $\overline{\operatorname{alg}}(B^2)$ 且字符为零，并不保证 $E/B$ 是有界算子。R167、R168 已显示，非负形式阶本身不足以保证实际商有界。

所以本稿严格地把两比特问题归到一个真实加权单比特关系；它没有解决第二次除法，也没有证明未知 $M$ 为零。后续若从实际核方程获得 $E=B\widetilde E$ 的有界实现，或相应限制上的可控因子，才可以继续取消剩下的 $B$。

## 7. 规则慢行中，剩余的全空间除法确实无界

本节加强第 6 节的边界：在一个可检验的慢尾条件下，(4.6) 的 $E/B$ 在全空间上确实不是有界算子。这个结论不外推到未知 $M$。

仍在危险平方分支，令

$$
Z=\sum_{i\ge k}a_i^2(I-V_i^2)
=4\sum_{i\ge k}a_i^2N_i(I+N_i)^{-2}.
\tag{7.1}
$$

由 $Y^2=a^2V(N)^2-Z$，以及 $Y+aV(N)$ 的字符为 $2a\ne0$，有真正的有界单位

$$
H_*=\bigl(Y+aV(N)\bigr)^{-1},\qquad
T=W_{\ge k}+ZH_*.
\tag{7.2}
$$

按 (1.4) 分解 $H_*=H_{*,0}+H_{*,1}N$。于是

$$
K=ZH_{*,1},\qquad \chi(H_{*,1})=1/a.
\tag{7.3}
$$

这里的字符可在 $Z=0$ 的首阶计算中读出：$H_*=(2a)^{-1}V(N)^{-1}$ 的 $N$ 一次系数为 $1/a$。所以 $H_{*,1}$ 是尾代数单位。

当 $b\ne0,a$ 时，(4.6) 可写成

$$
E=Z\gamma(Z)\,U_*,\qquad
U_*=2\eta H_{*,1}\gamma(H_{*,1})D_0^{-1},
\tag{7.4}
$$

其中 $U_*$ 是尾代数单位。因而存在有界 $Q$ 满足 $BQ=E$，当且仅当存在有界 $Q_0$ 满足 $BQ_0=Z\gamma(Z)$。这只是在等式右侧乘真实有界单位，没有形式除法。

**命题 7.1。** 若沿某个 $r\to\infty$ 的子列满足

$$
\frac{\eta_{r-1}}{|a_ra_{r+1}|^2}\longrightarrow0,
\tag{7.5}
$$

则不存在有界 $Q_0$ 使 $BQ_0=Z\gamma(Z)$。因此在 $b\ne0,a$ 时，也不存在有界 $Q$ 使 $BQ=E$。

**证明。** 记 $c_i=a_i^2$、$A_2=\sum_{i\ge k}|a_i|^2$。对 $i<r$，以真实有限头截断 $N_i^{[r]}$ 代替 $N_i$；对 $i\ge r$，以纯单比特 $E_i$ 代替。令

$$
Z^{[r]}=H_r\otimes I+4\sum_{i\ge r}c_iE_i,
\quad
H_r=4\sum_{k\le i<r}c_iN_i^{[r]}(I+N_i^{[r]})^{-2}.
\tag{7.6}
$$

已知实际逆界为 $\|(I+N_i)^{-1}\|\le3$，有限头与纯模型也满足此界。写 $F(N)=N(I+N)^{-2}=R_N-R_N^2$，逆差恒等式给出

$$
\|F(N)-F(M)\|\le63\|N-M\|.
$$

再用

$$
\|N_i-N_i^{[r]}\|=\alpha_r/\alpha_i\le\eta_{r-1} (i<r),
\qquad \|N_i-E_i\|\le\eta_i\le\eta_{r-1} (i\ge r),
$$

得到

$$
\|Z-Z^{[r]}\|\le252A_2\eta_{r-1},
\qquad \|Z\|,\|Z^{[r]}\|\le36A_2.
\tag{7.7}
$$

由于 $r>k$，$\gamma$ 固定 (7.6) 的纯尾，而将 $H_r$ 酉共轭为另一个严格下三角有限头矩阵。因此

$$
\|Z\gamma(Z)-Z^{[r]}\gamma(Z^{[r]})\|
\le18144A_2^2\eta_{r-1}.
\tag{7.8}
$$

取物理乘积单位向量 $x_r,y_r$：在 $k,\ldots,r+1$ 各位，$x_r$ 全为 $0$；$y_r$ 在 $k,\ldots,r-1$ 为 $0$，在 $r,r+1$ 为 $1$；更高位都取原乘积真空。低于 $k$ 的固定恒等张量因子任取相同单位向量。

严格下三角的头项及其乘积，在头 $0\to0$ 矩阵元上都为零。纯尾平方只有同时选取 $r,r+1$ 的项能从 $x_r$ 到 $y_r$，故

$$
\langle Z^{[r]}\gamma(Z^{[r]})x_r,y_r\rangle
=32c_rc_{r+1}.
\tag{7.9}
$$

另一方面，$B=N_k=A^{2^k}/d_k$ 的通常伴随，在 $y_r$ 上的唯一借位到达第 $r$ 位。前 $2^k-1$ 个低权的乘积与归一化分母相消，所以精确地

$$
\|B^*y_r\|=\alpha_r/\alpha_k.
\tag{7.10}
$$

若 $BQ_0=Z\gamma(Z)$ 且 $Q_0$ 有界，则 (7.8)--(7.10) 迫

$$
\|Q_0\|\ge\frac{\alpha_k}{\alpha_r}
\left(32|a_ra_{r+1}|^2-18144A_2^2\eta_{r-1}\right).
\tag{7.11}
$$

由 (7.5)，括号最终不小于 $16|a_ra_{r+1}|^2$。又因 $\eta_{r-1}=\alpha_r/\alpha_{r-1}$，右侧沿该子列趋于无穷，与有界性矛盾。证毕。

例如，规范慢行

$$
a_i=(-1)^i(i+1)^{-\sigma},\qquad \tfrac12<\sigma\le1,
$$

满足 (7.5)，且最低两项满足 $b\ne0,a$。因此该例中 (4.6) 的第二次全空间除法确实失败。

$B$ 单射，所以最大商 $B^{-1}E$ 是闭算子，且其域含稠密的 $\operatorname{Ran}B$。命题还说明 $\operatorname{Ran}E\not\subset\operatorname{Ran}B$：否则闭图定理会给出被排除的全域有界商。

本节没有排除 $B^{-1}E$ 在未知核空间上的特殊有界实现，也没有证明该核空间包含于商域。真正可用的下一步仍必须来自 $M$ 的额外结构。

依赖：R23 的归一化幂限制稠密性；R124 的二余数组有界除法；R125/R176 的闭一阶域及有界交换子域保持；R208 的危险平方核等价和单比特接口。
