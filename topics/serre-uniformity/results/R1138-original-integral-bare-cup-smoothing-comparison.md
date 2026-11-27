# R1138：原裸杯积与完整平滑符号的整模 p 比较

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纸面。** 本文从原 elliptic theta 函数的除子和真实 cyclic-subgroup norm 出发，在实际模 $p$ 单位类中比较 R1136 的完整平滑符号与原 $F_\chi,F_\psi$ 裸杯积。全部相关项保留并逐项计算；不把含 $1/p$ 的有理 Siegel 公式约模 $p$。结果对每个辅助素数 $n>3$、$n\ne p$ 成立，不要求 $\kappa_\chi(n)$ 或 $\kappa_\psi(n)$ 非零。

## 1. 实际系数、原权与声明

保持 [R1136](R1136-original-forced-compact-Manin-sources.md) (F1)–(F7) 的原曲线、Weil convention 与实际权。即
$$
p>37,\quad K=\mathbb Q(\zeta_p),\quad
X=X_{\rm ns}^+(p),\quad m=(p-1)/2,
$$
$$
\chi=\omega^{p-1-2j},\quad
\psi=\omega^{p-1-2k},\quad
1\le j,k\le\lfloor p/4\rfloor-1,\quad
\theta=\chi\psi=\omega^a,\quad a=p-1-2(j+k).
\tag{1138.1}
$$
所有函数指数先取原 augmentation-zero 整数提升，再约模 $p$。
用 $\mathcal L_\chi$ 表示对所有 $v\ne0$ 的原加权和：
$$
\mathcal L_\chi f=\sum_{v\ne0}a(v)[f(P_v)],\qquad
a(v)=m^{-1}N(v)^{2j}\pmod p.
\tag{1138.2}
$$
另一槽为 $\mathcal L_\psi$。因此共同的 base factor 在每槽严格消去。
下文 $\mathcal L$ 的值在 $K_1/p$，花括号在 $K_2/p$；
对原 theta 的 $\mathbb Z[1/30]$ 系数先映入 $\mathbb Z_{(p)}$。
相同公式也可用 prime-to-$p$ 倍数的实际函数代表解释。

取任意素数 $n>3$、$n\ne p$。令 $\pi$ 为添加 cyclic order-$n$ subgroup 的 degree $n+1$ cover，$q$ 为 physical quotient
$$
(E,(P_v),C)\longmapsto(E/C,(q_C(P_v))).
$$
$q$ 运输全部标记和 Weil root；它不是固定 Weil root 后的 correspondence。
按闭点及实际 residue field 求 corestriction，写
$$
\widetilde T_n=\pi_*q^*,\qquad
S_n=\sum_{v,w\ne0}a(v)b(w)B_n(P_v,P_w).
\tag{1138.3}
$$
这里 $B_n$ 是 R1136 (F7) 的完整符号，独立与依赖点对均包括。
本文证明
$$
\boxed{
S_n=\frac4{m^2}
 \bigl(n^4-n^2\widetilde T_n+n\theta(n^2)\bigr)
 \{F_\chi,F_\psi\}.
}
\tag{1138.4}
$$
它先在原 full-level field 成立，再由 R1136 的 $p+1$ transfer 下降到 $K(X)$。
没有除以 $n+1$、level $p$ 或任一 torsion splitting degree。

## 2. 一个可反除的辅助 c，只用于支付整比较

对实际角色置
$$
\kappa_\chi(c)=c^2-\chi(c^2),\qquad
\kappa_\psi(c)=c^2-\psi(c^2).
$$
其零集分别是 $\mathbb F_p^\times$ 中的 proper subgroup：
例如第一槽等价于 $c^{4j+2}=1$，而 $0<4j+2<p-1$。
两个 proper subgroup 的并不能覆盖整个群。取避开二者的非零剩余类，
再用 Dirichlet 定理选素数 $c>3$、$c\ne n,p$。
这里只需存在性；未声称 $c<p$，也不要求辅助分裂域次数为 $p$ 单位。

在任一带原标记的 elliptic curve 上，令
$$
M_{c,\chi}=\mathcal L_\chi\theta_c,\qquad
G_\chi=\kappa_\chi(c)^{-1}M_{c,\chi}.
$$
由原 all-vector division identity（R1136 (F27)，源为 R1070），
$$
M_{c,\chi}=\frac{2\kappa_\chi(c)}m[F_\chi],\qquad
\boxed{G_\chi=\frac2m[F_\chi].}
\tag{1138.5}
$$
$\theta_c$ 与 $\psi_c^{-1}$ 的 fiber divisor 相同，
其比是共同 base factor，已由 augmentation 消去。
所以 $G_\chi$ 不依赖所选 $c$。另一槽同理。

以下除子比较在 generic elliptic fiber 上完成。
两个具有相同 divisor 的 $p$-local theta 类只差 base 的 $K_1$ 类；
这个差在 (1138.2) 中精确消失，不需要选一个 $p$ 次根或丢掉相位。

## 3. 三个真实除子比较

令 $C\subset E[n]$ 为一个实际 cyclic subgroup，使用 SV §6.3 的
$$
\operatorname{div}\theta_n=n^2[O]-[E[n]],\qquad
\operatorname{div}\theta'_{n,C}=n[C]-[E[n]],\qquad
\operatorname{div}\theta_c=c^2[O]-[E[c]].
\tag{1138.6}
$$
$\theta'_{n,C}$ 的 elliptic curve 是 $E$ 添加 $C$ 后的 base change，
不是 $E/C$。所有 $P_v$、$cP_v$、$nP_v$ 都避开相应支撑。

第一项比较为
$$
\frac{\theta_n(T)^{c^2}}{\theta_n(cT)}
 =\lambda\,
 \frac{\theta_c(T)^{n^2}}{\theta_c(nT)}.
\tag{1138.7}
$$
两侧 divisor 均为
$c^2n^2[O]-c^2[E[n]]-n^2[E[c]]+[E[nc]]$。
重指标 $v\mapsto cv$ 或 $nv$ 分别乘
$\chi(c^2)$ 或 $\chi(n^2)$；共同 $\lambda$ 消去。
置 $x=\chi(n^2)$、$y=\psi(n^2)$，即得
$$
\boxed{\mathcal L_\chi\theta_n=(n^2-x)G_\chi.}
\tag{1138.8}
$$

第二项比较为
$$
\frac{\theta'_{n,C}(T)^{c^2}}{\theta'_{n,C}(cT)}
 =\lambda_C\,
 \frac{\bigl(\prod_{t\in C}\theta_c(T+t)\bigr)^n}
      {\theta_c(nT)}.
\tag{1138.9}
$$
因 $(c,n)=1$，$[c]^{-1}C=C+E[c]$。两侧 divisor 都为
$$
nc^2[C]-c^2[E[n]]-n[C+E[c]]+[E[nc]].
$$
乘积按有限群 scheme 的 norm 定义，不要求先把 $C$ 的点分裂。

第三项为
$$
\prod_{t\in C}\theta_c(T+t)=\lambda'_C q_C^*\theta_{c,E/C}(T).
\tag{1138.10}
$$
其共同 divisor 是
$c^2[C]-[C+E[c]]$，因为
$q_C^{-1}((E/C)[c])=C+E[c]$。
这里 target 的 $G_\chi$ 仍以运输的全部 $q_C(P_v)$ 和相同权定义。

对 (1138.9) 加权，再用 (1138.10) 及 (1138.5)，左侧是
$\kappa_\chi(c)\mathcal L_\chi\theta'_{n,C}$；
右侧是 $\kappa_\chi(c)(nq_C^*G_\chi-x\pi_C^*G_\chi)$。
只除已经选成单位的 $\kappa_\chi(c)$，得到准确的第二槽输入：
$$
\boxed{
\mathcal L_\chi\theta'_{n,C}
  =nq_C^*G_\chi-x\pi_C^*G_\chi,\qquad
\mathcal L_\psi\theta'_{n,C}
  =nq_C^*G_\psi-y\pi_C^*G_\psi.
}
\tag{1138.11}
$$
所有 base factor 均在形成每个 $K_1/p$ 类时消失；
没有把 cup 中未消去的常数符号事后忽略。

## 4. 单槽 physical Hecke 迹

对全部 cyclic subgroups 求 norm。每个非零 $n$-torsion 点属于唯一一个 $C$，
而 $O$ 被计 $n+1$ 次，故
$$
\sum_C[C]=[E[n]]+n[O],\qquad
\operatorname{div}\operatorname{Nm}_\pi\theta'_n
 =n^2[O]-[E[n]].
\tag{1138.12}
$$
因此 $\operatorname{Nm}_\pi\theta'_n$ 与 $\theta_n$ 只差 base factor
（trace-fixed 规范事实上给出严格相等，但这里无需用其唯一性）。
加权后结合 (1138.8)、(1138.11)，得到
$$
n\widetilde T_nG_\chi-x(n+1)G_\chi
 =(n^2-x)G_\chi.
$$
$n$ 是模 $p$ 单位，故
$$
\boxed{
\widetilde T_nG_\chi=(n+x)G_\chi,\qquad
\widetilde T_nG_\psi=(n+y)G_\psi.
}
\tag{1138.13}
$$
此计算在 $K_1/p$ 内成立。只用 degree $n+1$ 的真实 trace，
即使 $p\mid n+1$ 也成立；没有反除这个 degree。

## 5. 全部四项 correlation 的准确合并

令 $U=\{G_\chi,G_\psi\}$。
按 (1138.11) 展开 R1136 (F29) 的整个 cyclic norm，得到
$$
\begin{aligned}
\pi_*\{\mathcal L_\chi\theta'_n,\mathcal L_\psi\theta'_n\}
={}&n^2\widetilde T_nU\\
 &-ny\,\pi_*\{q^*G_\chi,\pi^*G_\psi\}
  -nx\,\pi_*\{\pi^*G_\chi,q^*G_\psi\}\\
 &+xy(n+1)U.
\end{aligned}
\tag{1138.14}
$$
projection formula 与 (1138.13) 分别给
$$
\pi_*\{q^*G_\chi,\pi^*G_\psi\}=(n+x)U,\qquad
\pi_*\{\pi^*G_\chi,q^*G_\psi\}=(n+y)U.
\tag{1138.15}
$$
所以两个 crossed 项被计算了，未被设为零。
第一项裸 product 是 $(n^2-x)(n^2-y)U$。从它减去 (1138.14) 后，
纯 scalar 系数严格为
$$
(n^2-x)(n^2-y)+ny(n+x)+nx(n+y)-xy(n+1)=n^4+nxy.
$$
于是
$$
S_n=(n^4-n^2\widetilde T_n+nxy)U.
\tag{1138.16}
$$
再用 $xy=\theta(n^2)$ 及
$U=4\{F_\chi,F_\psi\}/m^2$，即为 (1138.4)。

这也解释为何只保第一项 $(n^2-x)(n^2-y)U$ 会给错误算子：
两个 crossed norms 正好补齐全部线性与混合 scalar 项。

## 6. 原 X 上的 ordinary Hecke 与真实紧致来源

R1136 (F30) 已固定 physical convention：
$\widetilde T_n=\sigma_nT_n$，其中 $T_n$ 固定 $K$。
原杯积在角色 $\theta=\omega^a$ 中，所以
$$
\boxed{
S_n=\frac4{m^2}
 (n^4-n^{a+2}T_n+n^{2a+1})\{F_\chi,F_\psi\}
 =\frac4{m^2}n^{a+2}
 (n^{2-a}+n^{a-1}-T_n)\{F_\chi,F_\psi\}.
}
\tag{1138.17}
$$
原 full-level 到 $X_K$ 的 $H$-quotient degree $p+1$ 是 $p$ 单位，
restriction–corestriction 保证已经 $H$-不变的等式下降。
没有在 degree 含 $p$ 的 full-level 到 $\Gamma_1(p)$ 映射上反除。

由 R1136 (F21)、(F26)，(1138.17) 的左侧恰是
$$
2(p-1)e_\theta\mathfrak z_{n,X}(c^{(2)}_{\chi,\psi})
 +2\sum_La(v_L)b(v_L)\pi_L^*
       \mathfrak z_{n,1}(C^{(1)}_{\chi,\psi}).
\tag{1138.18}
$$
该式按 R1136 的 transfer 解释于原曲线上。
独立和依赖点对完整存在，rank-one diamond 是 $\theta^2$，
包含 $\theta$ quadratic、$\theta^2=1$ 的例外。
没有将后半项从公式中删除。

若进一步满足 R1136 (F33) 的低混合 Bernoulli 门，
这些 smoothing operators 在原紧致 Hecke 代数中生成单位理想。
(1138.17) 现已支付其与原裸杯积的准确模 $p$ 接口。
但仍须区分 source 上的单位理想与 target 中的公共核：
一个非零紧致循环的像可以非零，
仅有本等式不证明 $\{F_\chi,F_\psi\}=0$。
不把未分歧 $K_2[p]$ 的消失改写成 $K_2/p$ 的消失。
真正四阶覆盖还需低 cochains、全部跨轨道项与 cusp inertia moments。

## 7. 来源与验证

- Romyar Sharifi、Akshay Venkatesh，*Eisenstein cocycles in motivic cohomology*，
  Compositio Mathematica 160 (2024), 2407–2479；
  [作者全文](https://www.math.ucla.edu/~sharifi/publ/eisensymbol.pdf)，
  本文编号依该 87 页作者版 §6.3，尤其 (6.5)–(6.6)、(6.10)–(6.11)。
  所需输入是两个 divisor、degree $n+1$ 的 base change norm、
  以及 $\mathbb Z[1/30]$ theta 类；有理 unsmoothed 公式未作为输入。
- R1070、R1136：原 augmentation-zero 权、all-vector product、
  $F_\chi$ 的 Galois 方向及完整两种秩的紧致来源。
- (1138.7)–(1138.17) 由 root 与 global_route 独立纸面推得；
  root 已亲读上述 primary source，核定 $\theta'_n$ 的 base-change curve
  与 elliptic quotient $E/C$ 确实不同。
  没有数学程序执行，没有添加有限素数扫描。
