# R254 第九附录：同一平顶的纯尾幂右逆与 p>1/3 实际正则核饱和

日期：2026-11-13（UTC）。作者：boundary；Astra-ISP-1cf8c51d 复核。状态：已证明的实际中间结论。

本稿继续 [R254 第七附录](../results/R254-appendix-restricted-pure-kernel-right-inverse-and-subexponential-stable-range.md) 和 [R254 第八附录](../results/R254-appendix-quartic-head-budget-and-four-ninths-stable-range.md)。新步骤在前半桥：对纯删除算子的多次右逆固定同一个平顶与对角相似，只支付一次相似成本。随后重新支付低方程交集、准确顶部修复和实际 $X_7\to X_3$ 桥。一般核内稠密性仍不在结论中。

## 1. 一个平顶支付整个纯尾幂

仍令
$$
D_a=\sum_{j\ge m}a_jE_j,\qquad a_j=(j+2)^{-2},
$$
作用于高尾有限子集的 Hilbert 空间。$\mathcal H_\ell$ 表示完整的 $\ell$ 孔层；位置不要求有界。任意外部有限头只作为张量恒等因子。

给定整数 $q\ge0$，置
$$
M_*=m+q+2,\qquad J=4M_*,
\qquad \beta=(m+J+1)^{-2},
$$
$$
b_j=\min(a_j,\beta),\qquad
D_b=\sum_{j\ge m}b_jE_j,\qquad C_b=D_b^*.
\tag{1.1}
$$
前 $J$ 个系数恰为 $\beta$，以后不变。因为删除和创建只在同一位不交换，
$$
D_bC_b-C_bD_b
=\sum_{j\ge m}b_j^2(I-2P_j).
$$
在每个 $\mathcal H_\ell$、$0\le\ell\le q$ 上，
$$
D_bC_b\ge (J-2q)\beta^2 I
\ge \frac{2}{625}M_*^{-3}I.
\tag{1.2}
$$
这里用了 $J-2q\ge2M_*$ 和 $m+J+1\le5M_*$。因此
$$
U_\ell=C_b(D_bC_b|_{\mathcal H_\ell})^{-1}
:\mathcal H_\ell\longrightarrow\mathcal H_{\ell+1}
$$
是真实右逆，
$$
D_bU_\ell=I,\qquad
\|U_\ell\|\le\frac{25}{\sqrt2}M_*^{3/2}<18M_*^{3/2}.
\tag{1.3}
$$
范数界由
$U_\ell^*U_\ell=(D_bC_b|_{\mathcal H_\ell})^{-1}$
直接得到。没有要求这些右逆保有限位置。

令 $\rho_j=a_j/b_j\ge1$，以
$$
S e_F=\left(\prod_{j\in F}\rho_j\right)e_F
$$
定义正对角算子。只有前 $J$ 个 $\rho_j$ 不等于 $1$，所以固定 $m,q$ 后 $S$ 和 $S^{-1}$ 都是实际有界算子。逐个有限子集准确计算给
$$
D_a=S^{-1}D_bS,\qquad \|S^{-1}|_{\mathcal H_\ell}\|\le1.
\tag{1.4}
$$
对 $0\le t\le q$，$\|S_t\|$ 的最大值来自最前面的 $t$ 个位置：
$$
\|S_t\|
=\prod_{i=0}^{t-1}
\left(\frac{m+J+1}{m+i+2}\right)^2.
$$
当 $t>0$，积分估计给
$$
\prod_{i=0}^{t-1}(m+i+2)
\ge[(m+t+1)/e]^t.
$$
又有 $tM_*\le(q+1)(m+t+1)$，故
$$
\begin{aligned}
\log\|S_t\|
&\le2t\left(\log(5e)+\log\frac{q+1}{t}\right)\\
&\le 2q\log(5e)+2(q+1)/e\\
&\le8(q+1).
\end{aligned}
\tag{1.5}
$$
$t=0$ 也满足该界。

现在取 $1\le s\le\ell\le q$。把同一个 $D_b$ 的右逆连续复合 $s$ 次：
$$
R_{b,s,\ell}
=U_{\ell-1}\cdots U_{\ell-s}.
$$
逐步使用 $D_bU_j=I$ 得
$D_b^sR_{b,s,\ell}=I$。定义
$$
R_{a,s,\ell}
=S_\ell^{-1}R_{b,s,\ell}S_{\ell-s}.
\tag{1.6}
$$
由 (1.4)，这是真实 $D_a^s$ 的右逆，且
$$
\boxed{
\|R_{a,s,\ell}\|
\le e^{8(q+1)}
[18(m+q+2)^{3/2}]^s.
}
\tag{1.7}
$$
中间的全部相似因子准确消掉；没有把单次右逆的指数成本重复支付 $s$ 次。

设 $\Pi_s$ 为 $\ker D_a^s$ 的正交投影。由于 $D_a^s$ 严格降低 $s$ 次孔，$\Pi_s$ 保每个完整孔层。对各层用最小距离不超过实际右逆输出，再作正交直和，得到
$$
\boxed{
\|P_{\le q}(I-\Pi_s)f\|
\le e^{8(q+1)}
[18(m+q+2)^{3/2}]^s\|D_a^s f\|.
}
\tag{1.8}
$$
$\ell<s$ 的层本来就在核内。这里没有交换 $\Pi_s$ 与任何混合平方符号。

## 2. 原实际平方核在 q=25d^4 的纯核逼近

沿用去掉原第 $0$ 位后的记号，$d=2^m$，
$$
P_m=D^2+Q_m,\qquad D=D_a,
$$
$P_m$ 是真实前 $m$ 尾位加纯高尾的混合平方符号。两型仍分别为
$$
P_m=(A_m+D)^2-\eta C_m\quad(N),
$$
$$
P_m=(A_m+D)^2-\eta C_m(I+A_m+D)^2\quad(Y).
$$
实际无限符号记作 $P$，实际平方核为 $K=\ker P$。已证
$$
\|P-P_m\|\le36\eta_m,\qquad
\|P_m\|<1,\qquad \|Q_m\|<1/2,\qquad Q_m^d=0.
$$
准确进位率是
$$
-\log\eta_m=1400d^4-630d^3+300d.
\tag{2.1}
$$
实际伴随多项式
$$
\mathcal A_m=\sum_{k=0}^{d-1}(-Q_m)^kD^{2(d-1-k)}
$$
满足
$$
\mathcal A_mP_m=D^{2d}.
\tag{2.2}
$$
[R254 第三附录](../results/R254-appendix-high-order-pure-tail-kernel-constraint-without-similarity.md) 已证明，对 $u\in K$，
$$
\|D^{2d}u\|\le36d\,2^{1-d}\eta_m\|u\|.
\tag{2.3}
$$

令
$$
q=25d^4,\qquad \Pi=\Pi_{2d},\qquad m\ge4.
$$
由 (1.8) 和 (2.3)，
$$
\|P_{\le q}(I-\Pi)u\|
\le\epsilon_{m,q}\|u\|,
$$
$$
\epsilon_{m,q}
=36d\,2^{1-d}\eta_m
 e^{8(q+1)}
 [18(m+q+2)^{3/2}]^{2d}.
\tag{2.4}
$$
这个新公式不含旧的 $14dq$ 指数。

具体地，$m+q+2\le26d^4$，并且对 $d\ge16$，
$$
-\log\eta_m\ge1360d^4.
$$
除 $8q=200d^4$ 外，(2.4) 的其余正对数不超过
$$
\log(36d)+8+2d\log18+3d\log(26d^4)\le d^4.
$$
末一不等式在 $d=16$ 已有充分余量，此后 $(1+\log d)/d^3$ 递减。因此
$$
\boxed{
\epsilon_{m,25d^4}\le e^{-1100d^4},\qquad m\ge4.
}
\tag{2.5}
$$

## 3. 新尺度下低方程仍可在同一纯核内支付

这里必须重新处理低方程，不能直接把纯核距离当作混合核距离。

设 $x=\Pi u$，并令
$$
r=P_{\le q-2}P_mx.
$$
$P_m$ 与 $D^{2d}$ 交换，孔截断也保 $\ker D^{2d}$，所以
$$
r\in\ker D^{2d}\cap\mathcal H_{\le q-2}.
\tag{3.1}
$$
$P_m$ 对高尾孔数只降低 $0,1,2$。因此 (2.5) 给
$$
\|r\|
\le(36\eta_m+\epsilon_{m,q})\|u\|
\le e^{-1099d^4}\|u\|.
\tag{3.2}
$$

采用第七、八附录的同一个实际受限右逆
$$
\mathcal G_m=H\sum_{k<d}(-Q_mH)^k,\qquad P_m\mathcal G_m=I.
$$
它与第 1 节为纯幂投影另造的 $R_{a,s,\ell}$ 是不同用途的算子。前者的核阶、输出次数和真实头四次衰减全部沿用已证公式。

当输入属于 $\ker D^{2d}\cap\mathcal H_{\le q}$ 时，置
$$
L_*=512\sqrt{q+2d+1}(m+q+2d+2)^{3/2}.
$$
旧受限预算为
$$
\mathcal B_{m,q}=d(4d)^{2d}L_*^{6d^2-d}.
$$
在本稿 $q=25d^4$ 下，
$$
\log L_*<13+8\log d,
$$
因而
$$
\boxed{
\log\mathcal B_{m,q}\le100d^2(1+\log d)\le2d^4,\quad m\ge4.
}
\tag{3.3}
$$
这支付明确的 carry 误差。

更小的真实头四次预算则为
$$
\log\mathfrak B_{m,q}
=\log d+\max\{2mL,U+3L^{4/3}\},
$$
$$
U=2\log(4d)+6d\log L_*,
\qquad L=U+\log32.
$$
同样有 $L\le128d(1+\log d)$，故
$$
\boxed{
\log\mathfrak B_{m,25d^4}
\le4096d^{4/3}(1+\log d)^{4/3}.
}
\tag{3.4}
$$
可以始终取 $\mathcal B,\mathfrak B$ 的较小值。第八附录逐词证明中的实际 carry、Cayley 逆和 $HD^{t_k}H\cdots D^{t_1}H$ 原次序未作任何改变；只有最大输出次数 $q$ 增大。

取 $z=\mathcal G_mr$。由 (3.2)--(3.3)，
$$
\|z\|\le e^{-1097d^4}\|u\|.
$$
(2.2) 给
$$
D^{2d}z=\mathcal A_mr=-\mathcal A_mP_{>q-2}P_mx.
$$
$\mathcal A_m$ 的尾孔降低量至多 $2d-2$，所以右侧只在次数至少 $q-2d+1$ 上有支撑；而
$D^{2d}P_{\le q}z$ 只在次数至多 $q-2d$ 上有支撑。正交分层遂给
$$
P_{\le q}z\in\ker D^{2d}.
$$
又因 $P_mP_{>q}z$ 的最低输出次数为 $q-1$，
$$
y=x-P_{\le q}z
\in\mathcal V_{m,q}
:=\ker D^{2d}\cap\ker(P_{\le q-2}P_m).
$$
这正是第五附录的兼容性论证；不假设 $\Pi$ 与 $P_m$ 交换。

$\mathcal V_{m,q}$ 按 $\mathcal H_{\le q}\oplus\mathcal H_{>q}$ 作正交直和。令 $\mathsf V_{m,q}$ 为它的正交投影，取
$$
v_m=P_{\le q}\mathsf V_{m,q}u.
$$
从刚构造的低部竞争向量及最小距离性质，
$$
\boxed{
\begin{gathered}
v_m\in\ker D^{2d}\cap\mathcal H_{\le q},\quad
P_{\le q-2}P_mv_m=0,\quad \|v_m\|\le\|u\|,\\
\|P_{\le q}u-v_m\|\le e^{-1000d^4}\|u\|,\qquad
v_m\longrightarrow u.
\end{gathered}
}
\tag{3.5}
$$
最后一个极限为真实 Hilbert 强收敛；高尾孔截断余项由总孔尾控制。

## 4. 顶部准确修复和实际稳定像提升

令
$$
r_m=P_mv_m,\qquad
c_m=\mathcal G_mr_m,\qquad
k_m=v_m-c_m.
$$
准确地，
$$
r_m\in\ker D^{2d}\cap(\mathcal H_{q-1}\oplus\mathcal H_q),
$$
$$
c_m\in\ker D^{2d}\cap\mathcal H_{[q+1,q+2d]},
\qquad
k_m\in\ker P_m\cap\mathcal H_{\le q+2d}.
\tag{4.1}
$$
证明与第六附录一致：$\mathcal G_m$ 最低增加两次孔；而
$D^{2d}c_m=\mathcal A_mr_m=D^{2d}v_m=0$。
由 (3.5)，
$$
\|r_m\|\le\tau_{q-2}(u)+e^{-1000d^4}\|u\|,
$$
$$
\|c_m\|\le
\min(\mathcal B_{m,q},\mathfrak B_{m,q})\|r_m\|.
\tag{4.2}
$$

令 $J_m$ 为前述实际多项式图，$\|J_m\|\le5/4$，而
$\|J-J_m\|\le27\eta_m$。使用
[R239 的实际 $X_7\to X_3$ 正则提升](../results/R239-appendix-mixed-low-hole-kernel-regular-lift-to-stable-range.md)
的原公式，得到
$$
n_m=\Lambda_{m,Q}k_m\in N,\qquad Q=q+2d,
$$
$$
\|n_m-J_mk_m\|\le\delta_{m,Q}\|k_m\|,
$$
$$
\delta_{m,Q}
=130C_G\sqrt{(2m+5)(Q+m+2)}
 e^{7(Q+2m+3)}\eta_m,
\quad C_G=\frac43e^{4\cdot2^{22}}.
\tag{4.3}
$$
不能套用该文仅针对 $Q\le50d^3$ 的数值推论；本稿直接重算。

因为 $Q\le26d^4$、$\log(130C_G)\le257d^4$，且平方根项及 $7(2m+3)$ 的总对数小于 $d^4$，(2.1) 给
$$
\boxed{
\delta_{m,q+2d}\le e^{-900d^4},\qquad m\ge4.
}
\tag{4.4}
$$
结合 (3.3)、$\|r_m\|\le\|u\|$，有
$$
\|k_m\|\le2e^{2d^4}\|u\|.
$$
所以
$$
\boxed{
\|n_m-(J_mv_m-J_mc_m)\|
\le e^{-897d^4}\|u\|.
}
\tag{4.5}
$$
原实际正则输出域和真进位误差均已支付，不把混合模型核直接认作原实际核。

## 5. 所有 p>1/3 的原实际正则核属于 N

**定理。** 对两个原实际慢边界核 $M=\ker T$，任意 $p>1/3$、$c>0$ 都有
$$
\boxed{
M\cap\operatorname{Dom}e^{c(1+\mathcal N)^p}\subseteq N.
}
\tag{5.1}
$$

证明：写 $w=Ju\in M$。从第一位分量提取及高尾孔数不超过总孔数，
$$
\tau_Q(u)\le C_we^{-c(1+Q)^p}.
$$
在 $q=25d^4$ 下，
$$
d^{4/3}(1+\log d)^{4/3}=o(d^{4p}).
$$
(3.4)、(4.2) 因而给 $\|c_m\|\to0$。
(3.5) 给 $v_m\to u$，实际图 $J_m\to J$，再由 (4.5)，
$n_m\to Ju=w$ 强收敛。因每个 $n_m\in N$ 且 $N$ 闭，得 $w\in N$。证毕。

这是实际核向量的直接证明，不要求缺陷正交投影保任何次数权，也不依赖 Haar 表示中的值域或域密度。

## 6. 真缺陷的改进必要尾率

仍以 $\tau_Q(w)=\|\mathbf1_{\{\mathcal N>Q\}}w\|$ 表示全部物理孔次数尾。

设 $0\ne w=Ju\in M\ominus N$。由 $n_m\in N$、(3.5)、(4.5)，
$$
\langle J_mc_m,w\rangle\longrightarrow\|w\|^2.
$$
$J_m$ 的图项至多降低一次高尾孔，而 $c_m$ 最低次数为 $q+1$；因此 $J_mc_m$ 的总孔数至少为 $q$。于是对充分大的 $m$，
$$
\|c_m\|\tau_{q-1}(w)\ge\frac25\|w\|^2.
$$
结合 (4.2) 及 $\|u\|\le\|w\|$，并用旧预算吸收
$e^{-1000d^4}$，得到
$$
\min(\mathcal B_{m,q},\mathfrak B_{m,q})
 \tau_{q-2}(w)^2\ge\frac15\|w\|^2.
$$
(3.4) 与 $q=25d^4$ 遂给
$$
\log\frac{\|w\|}{\tau_{25d^4-2}(w)}
\le2048d^{4/3}(1+\log d)^{4/3}
+\tfrac12\log5.
$$
相邻 $q$ 网格比现在为 $16$。按尾范数单调性推广至全部次数，得到
$$
\boxed{
-\log\frac{\tau_Q(w)}{\|w\|}
=O\!\left(Q^{1/3}(\log(Q+2))^{4/3}\right).
}
\tag{6.1}
$$
它是非零缺陷的必要慢尾条件。没有推出相反方向的尾部上界。

## 7. 仍未闭合的接口

第 1 节右逆用于纯幂的全层投影；第七、八附录的受限右逆只用于已经证明属于 $\ker D^{2d}$ 的残量。两处域不能混同。

本稿没有断言临界 $p=1/3$ 对任意 $c>0$ 成立，也没有证明这些正则核在 $M$ 内稠密。一般 Hilbert 向量的尾仍可能慢于 (6.1) 允许的全部速率，因此特殊修复可能没有有界子列。$N=M$、无权缺陷能量和普通 ISP 仍然未完成。
