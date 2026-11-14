# R150 附录：斜率一的实际中心比、有限谱比例部分与原等权 Bell

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf。

状态：完整证明；根代理与 kernel_resume_1cf 已全文独立核查。本文处理超线性 Newton 结论没有自动覆盖的斜率1。只在已经支付的真实全柱预算下给中心谱结论，不把两个正 first 的等权扇区当作可任意缩小的高次扇形。

## 1. 两个原 first 的中心比

取原模型的复 first
$$
u=u_*+\sum_j\zeta_j\chi_j,\qquad
v=v_*+\sum_j\nu_j\chi_j,\qquad
\zeta,\nu\in\ell^2(\mathbb C),
$$
令
$$
Z=X_u,\qquad Y=X_v.
$$
假设 $Z$ 空谱，$L=Z^{-1}\in\mathfrak C=A'$ 为其真实有界逆。

取递增穷尽的有限位集 $F_n$，记
$$
d_n=|F_n|,\qquad
\sigma_n=u_*+\sum_{j\in F_n}\zeta_j,\qquad
\tau_n=v_*+\sum_{j\in F_n}\nu_j,
$$
$$
g_n=\|\zeta_{F_n^c}\|_2+\|\nu_{F_n^c}\|_2.
$$
假设
$$
\boxed{
|\sigma_n|\to\infty,\qquad
\frac{\sum_{j\in F_n}(|\zeta_j|+|\nu_j|)}{|\sigma_n|}
\le C,\qquad
\frac{\sqrt{d_n}\,g_n}{|\sigma_n|}\to0.
}
\tag{1.1}
$$
于是实际中心比
$$
\beta_n=\tau_n/\sigma_n
\tag{1.2}
$$
有界。允许只沿同一递增子列满足 (1.1)，再重新编号。

定义自然闭算子
$$
S=YL,\qquad \operatorname{Dom}S=\{h:Lh\in\operatorname{Dom}Y\}.
\tag{1.3}
$$

**定理 1。** 设在任意固定有限放大中，非零闭空间 $\mathcal M$ 被全部对角 $\mathfrak C$ 保持，且
$$
\mathcal M\subseteq\operatorname{Dom}S,\qquad
S\mathcal M\subseteq\mathcal M,\qquad
J=S|_\mathcal M\in B(\mathcal M).
$$
则：

1. (1.2) 的每个聚点 $\beta$ 都属于 $\sigma(J)$。
2. 如果 $\sigma(J)$ 有限，那么存在一个复数 $\beta$，使
   $$
   \boxed{\beta_n\to\beta,\qquad \sigma(J)=\{\beta\}.}
   \tag{1.4}
   $$

这里允许 $\beta=0$。没有声称这个谱值必定产生非零部分，也没有排除其拟幂零误差。

## 2. 聚点外的单位部分由真实全柱排除

记 $\Pi$ 为到 $\mathcal M$ 的正交投影，以下按相应有限对角放大理解。

[全柱多项式稿 §4](R150-appendix-polynomial-column-tests-and-invertible-normalized-parts.md)
已支付一般非最大增生空谱 $Z$ 的受限域：R186 的同一深正则器使
$Z^jR(t)^N$ 成为全域有界 $\mathfrak C$ 元素，故其像在真实部分的自然域中并稠密逼近 $\mathcal M$。全部预解保持又给 $Z_\mathcal M$ 的真实逆 $L_\mathcal M$。

对 $x\in\operatorname{Dom}Z_\mathcal M$，
$$
Yx=S Z_\mathcal Mx=JZ_\mathcal Mx.
\tag{2.1}
$$
用同一深正则核心以及原空间通常伴随配对，得到
$$
\boxed{\Pi Y^*f=J^*\Pi Z^*f}
\tag{2.2}
$$
于 $Z^*,Y^*$ 的全部有限共同自然词域。该证明不需要 $\mathcal M$ 被 $C$ 或原通常伴随保持。

固定 (1.2) 的一个聚点 $\beta$，沿相应子列有 $\beta_n\to\beta$。反设
$\beta\notin\sigma(J)$，则 $J-\beta I$ 是有界单位。由 (2.2)，
$$
\Pi(Y^*-\overline\beta Z^*)
=(J^*-\overline\beta I)\Pi Z^*.
\tag{2.3}
$$

考虑仅在已付共同深域上定义的多项式
$$
\mathscr P_n(z)
=I-\frac{Z^*}{\overline{\sigma_n}}
+z\,\frac{Y^*-\overline\beta Z^*}{\overline{\sigma_n}}.
\tag{2.4}
$$
写真实有限头/尾分解
$$
\frac{Z^*}{\overline{\sigma_n}}=I+A_n+T_n,\qquad
\frac{Y^*}{\overline{\sigma_n}}
=\overline{\beta_n}I+B_n+U_n.
$$
则
$$
\boxed{
\mathscr P_n(z)
=z(\overline{\beta_n}-\overline\beta)I
-(A_n+T_n)
+z[B_n+U_n-\overline\beta(A_n+T_n)].
}
\tag{2.5}
$$
常数项趋零；其余单项式都是一次。对每个固定 $|z|\le R$，系数一致有界。

R251 的真实混合头四次进位与同一补集尺度的尾词预算，正是全柱多项式稿 §§2—3 的输入。取整数 $p_n$，使
$$
p_n/d_n\to\infty,\qquad g_n\sqrt{p_n}/|\sigma_n|\to0.
$$
将 (2.5) 的 $p_n$ 次展开按常数数、头总次数、尾总次数分组，其中至少一项不小于 $p_n/3$。同一三组估计给
$$
\boxed{
\sup_{|z|\le R}
\|\mathscr P_n(z)^{p_n}Q_{F_n}\|^{1/p_n}\to0.
}
\tag{2.6}
$$
这里使用的是原 $Z,Y$ 全部真实整数词。没有把 $Y-\beta Z$ 另行声明为某个未知最大域的自然和。

令
$$
A_n'=Z^*/\overline{\sigma_n},\qquad
B_n'=(Y^*-\overline\beta Z^*)/\overline{\sigma_n},
\qquad D_n'=I-A_n'.
$$
(2.3) 给
$$
\Pi=\Pi D_n'+(J^*-\overline\beta I)^{-1}\Pi B_n'.
$$
逐次代入并对
$(D_n'+zB_n')^{p_n}Q_{F_n}$
用有限 Cauchy 系数公式。选固定
$$
R>\|(J-\beta I)^{-1}\|,
$$
得到
$$
\boxed{
\|\Pi Q_{F_n}\|
\le
\frac{1}{1-\|(J-\beta I)^{-1}\|/R}
\sup_{|z|=R}\|\mathscr P_n(z)^{p_n}Q_{F_n}\|
\to0.
}
\tag{2.7}
$$
而 $Q_{F_n}\to I$ 强，故 $\Pi=0$，矛盾。这证明每个聚点 $\beta$ 都在 $\sigma(J)$ 中。

## 3. 有限谱时所有分图必须取同一个中心

再设 $\sigma(J)$ 有限。对其中任意 $\kappa$，取 $J$ 的非零 Riesz 子空间
$\mathcal M_\kappa$。它闭，仍在自然 $S$ 域中，并且
$$
S\mathcal M_\kappa\subseteq\mathcal M_\kappa,\qquad
\sigma(S|_{\mathcal M_\kappa})=\{\kappa\}.
$$
因为所有对角 $\mathfrak C$ 与 $J$ 交换，Riesz 投影也与它们交换，所以
$\mathcal M_\kappa$ 仍满足定理1的全部真实不变条件。

对同一个任意聚点 $\beta$，将 §2 重新应用于每个
$\mathcal M_\kappa$，得到
$$
\beta\in\sigma(S|_{\mathcal M_\kappa})=\{\kappa\}.
$$
因此每个 $\kappa$ 都等于同一个 $\beta$，整个 $\sigma(J)$ 只有此点。
再用 §2 处理其余聚点，所有聚点也都等于它。

(1.2) 有界，故唯一聚点意味着序列收敛，得到 (1.4)。
这不是先选择某一个分图的谱点，然后忽略其他分图；每一个非零 Riesz 分图都使用同一组实际 $F_n,\sigma_n,\tau_n$。

## 4. 等权原 Bell 的准确排核判据

令标量 $F(x,y)$ 关于 $y$ 首一、次数为 $M\ge1$，并满足
$$
\deg_{\rm tot}F\le M.
\tag{4.1}
$$
记其最高齐次符号
$$
H(s)=F_M(1,s).
$$
$H$ 是首一、次数 $M$ 的标量多项式。

对固定 $\lambda\in\mathbb C,r\ge1,w$，保持原完整
$[F(x,y)-\lambda]^r$ 的全部 Bell 系数。因为本稿直接使用原 $Z=X_u,Y=X_v$，指数倾斜只带来有界 $\mathcal A$ 平移；这些平移和正阶 Bell 微分都严格降低普通总次数。

令 $D=rM$，所得实际核心 $P(Z,Y)$ 准确满足
$$
\widehat P(t,s)=t^DP(t^{-1},t^{-1}s)
=H(s)^rI+tE(t,s),
\qquad \deg_sE<D.
\tag{4.2}
$$
最高符号是原 $H(s)^r$，没有丢掉一个 weighted 的最高算子系数。

若原规范 Bell 核非零，同一 R186 单射正则器的充分深幂把其中非零向量送入自然
$S=YL$ 的首一多项式核：
$$
\widehat P[L](S)h=L^DP(Z,Y)h=0.
$$
全部归一幂非负，输入有限词深度可取 $N\ge2D+2$，并按原有限族需要增加固定深度。

原[有限阶非零簇稿 §§4—5](R150-appendix-finite-order-resolvent-narrow-sectors-and-all-nonzero-leading-clusters.md)的自然相伴图构造在此不需要有限阶，给非零闭 $\Gamma$ 和有界部分
$J=S|_\Gamma$，满足
$$
H(J)^r=-L_\Gamma E[L_\Gamma](J).
$$
右侧拟幂零，所以
$$
\sigma(J)\subseteq H^{-1}(0).
\tag{4.3}
$$
这是有限谱。定理1遂迫
$$
\boxed{
\beta_n\to\beta,\qquad H(\beta)=0.
}
\tag{4.4}
$$

因此得到以下完整循环判据：

- 若实际中心比 $\beta_n$ 不收敛，则每个满足 (4.1) 的首一 $F$，对全部
  $\lambda,r,w$ 都使 $[F(u,v)-\lambda]^re^w$ 循环。
- 若 $\beta_n\to\beta$，则只要 $H(\beta)\ne0$，同样得到全部
  $\lambda,r,w$ 的循环性。

证明最后一步仍在原完整空间：规范 Bell 的 $C$ 自伴性给零核等价于像稠密，原指数向量的循环图核心把像稠密传成所述原点态向量循环。

若 $H(\beta)=0$，本稿保留该线性最高分支；没有从有限谱只能为单点就宣称其核存在或消失。

## 5. 全部原 weighted 与可和误差直接进入有限头

下面给一个不需要改写原最高符号的具体应用。取
$$
a\ge0,\quad a\in\ell^2\setminus\ell^1,\qquad
c\in\ell^2(\mathbb C),\quad |c_j|\le C_0a_j,
$$
以及原函数
$$
u=u_*+\sum_j(a_j+d_j^0+e_j^0)\chi_j,\qquad
v=v_*+\sum_j(c_j+\gamma a_j+d_j^1+e_j^1)\chi_j,
\tag{5.1}
$$
其中 $d^\nu_j=0$ 于 $a_j=0$、
$\sum_{a_j>0}|d^\nu_j|^2/a_j=K_\nu^2<\infty$，
$e^\nu\in\ell^1(\mathbb C)$；常数任意复。

### 5.1 原 $Z=X_u$ 的空谱无需忽略可和项

已付锚
$$
Z_0=X_{a+d^0}+\omega,\qquad L_0=Z_0^{-1}
$$
空谱，$L_0$ 有界拟幂零。原算子为
$$
Z=Z_0+H_0,\qquad
H_0=u_*I+X_{e^0}-\omega I\in\mathcal A.
$$
这是完整有界扰动域等式。对所有复 $\lambda$，
$$
\boxed{
(Z-\lambda)^{-1}
=L_0[I+(H_0-\lambda I)L_0]^{-1}\in\mathfrak C.
}
\tag{5.2}
$$
括号为单位，因为 $(H_0-\lambda I)L_0$ 是实际交换拟幂零算子。
所以原 $Z$ 空谱；无需把原常数或可和项移出后再替换目标向量。

### 5.2 一个同时支付全部原尾的有限位集

令 $r_1\ge r_2\ge\cdots>0$ 为正 $a$ 的非零下降重排，$\iota(j)$ 为对应物理位。记
$$
S_n=\sum_{j\le n}r_j,\qquad G_n^2=\sum_{j>n}r_j^2.
$$
假设沿一个递增子列
$$
\boxed{nG_n^2/S_n^2\to0.}
\tag{5.3}
$$

取 $F_n$ 为下列四个集合的并：

1. 最大 $n$ 个 $a$ 系数的实际位；
2. 最大 $n$ 个 $|e^0|$ 系数的实际位；
3. 最大 $n$ 个 $|e^1|$ 系数的实际位；
4. 前 $n$ 个物理位。

每一误差行只取至多 $n$ 个非零位；有限支撑在 $n$ 超过支撑数后取其全部。并列按固定物理顺序打破。因此 $F_n$ 递增、穷尽，且 $d_n\le4n$。

除第一组外，至多新增 $3n$ 个位。它们的 $a$ 质量不超过
$$
\sqrt{3n}\,G_n=o(S_n).
$$
故
$$
s_n^a:=\sum_{F_n}a_j=S_n+o(S_n).
\tag{5.4}
$$
受控行在新增位的总绝对值也为 $o(S_n)$。

weighted 头由 Cauchy–Schwarz 控制：
$$
\sum_{F_n}|d^\nu_j|\le K_\nu\sqrt{s_n^a}.
\tag{5.5}
$$
可和头的总绝对值有固定界。因此原两个实际中心满足
$$
\sigma_n=u_*+\sum_{F_n}(a+d^0+e^0)
=S_n+o(S_n),
$$
$$
\tau_n=v_*+\sum_{F_n}(c+\gamma a+d^1+e^1)
=\gamma S_n+\sum_{j\le n}c_{\iota(j)}+o(S_n).
\tag{5.6}
$$
同时原两条完整行的头绝对值和除以 $|\sigma_n|$ 一致有界。

对 weighted 尾，因为 $a_j\le r_{n+1}$ 于 $F_n^c$，
$$
\|d^\nu_{F_n^c}\|_2^2\le r_{n+1}K_\nu^2,\qquad
\frac{n\|d^\nu_{F_n^c}\|_2^2}{S_n^2}
\le\frac{K_\nu^2}{S_n}\to0.
\tag{5.7}
$$
这里用了 $nr_{n+1}\le S_n$。

若 $e\in\ell^1$，记其幅度下降重排为 $s_j$。则
$ns_{n+1}\to0$，并且
$$
n\sum_{j>n}s_j^2
\le ns_{n+1}\sum_{j>n}s_j\to0.
\tag{5.8}
$$
$F_n$ 包含各误差最大 $n$ 位，故 (5.8) 同时支付两个原可和尾。原 $a,c$ 尾由 (5.3) 及 $|c|\le C_0a$ 控制。

结合 $d_n\le4n$ 与 (5.6)，得到 (1.1) 对全部原 $\zeta,\nu$ 成立，没有遗漏可和误差在远物理位上的大尾。

## 6. 用原系数直接计算的等权判据

定义沿 (5.3) 同一子列的排序加权平均
$$
b_n=\frac{\sum_{j\le n}c_{\iota(j)}}{S_n}.
\tag{6.1}
$$
它有界于 $C_0$。由 (5.6)，
$$
\boxed{\beta_n=\tau_n/\sigma_n=\gamma+b_n+o(1).}
\tag{6.2}
$$

因此，对原完整 (5.1)：

- 若 $b_n$ 在这条全柱好子列上不收敛，则每个首一
  $\deg_yF=M,\ \deg_{\rm tot}F\le M$ 的全部
  $[F(u,v)-\lambda]^re^w$ 都循环。
- 若 $b_n\to b$，则最高符号只需满足
  $$\boxed{F_M(1,\gamma+b)\ne0}$$
  即有同样的全 $\lambda,r,w$ 结论。

若两个全柱好子列具有不同平均极限，可将它们递增交织成同一好子列，得到第一项。

本文始终直接采用原 $Z=X_u,Y=X_v$。等权情形下可能出现的
$y_{\rm old}=Y+RZ+K$ 最高算子系数没有被丢掉；这里根本不进行该换元，而是用 §5 的真实有限头支付全部原项，使 §4 的标量最高符号准确成立。

## 7. 例子与留下的准确线性分支

取
$$
a_j=\frac1{j+1},\qquad
c_j=\frac{1+2(-1)^j}{j+1},
$$
先令其余误差与常数为零。正主行满足 (5.3)，且
$$
S_n\sim\log n,\qquad
b_n=1+\frac{2\sum_{j<n}(-1)^j/(j+1)}{S_n}\to1.
$$
所以每个普通总次数不超过 $y$ 首一次数的 $F$，只要
$F_M(1,1)\ne0$，其全部常数移位、点态幂和复指数权均循环。

例如
$$
\boxed{[v^2-u-\lambda]^r e^w\text{ 对全部 }\lambda,r,w\text{ 循环}.}
$$
辅助 first 的正、负系数都具有不可和质量；本结论没有假定它空谱，也没有假定它对正主锚相对有界。

若希望中心比本身不收敛，可取 $a_j=1/(j+1)$，
在逐渐支配此前全部调和质量的有限块上交替令 $c_j=a_j$ 与 $c_j=-a_j$。
例如令 $c_0=0$，取 $N_0=2,N_{\ell+1}=N_\ell^{\ell+2}$，在
$N_\ell\le j+1<N_{\ell+1}$ 上令 $c_j=(-1)^\ell a_j$。
块末以前全部旧质量除以当前质量为 $O(\log N_\ell/\log N_{\ell+1})=O(1/(\ell+2))$，所以块末的加权平均分别趋于 $+1,-1$，而正主行的全柱条件仍成立。
于是 §6 第一项排除全部等权首一 Bell 核。

本稿与已有单 first 中心谱和部分简单根条件相交时按旧来源扣除。新增接口是实际比例 $YL$ 的有限谱部分必须共享原中心比极限，以及这对完整混合等权 Bell 的应用。

若唯一中心比极限恰为最高符号的根，持久线性分支仍未被排除。没有全柱预算的一般等权边、一般低次零簇、原真正常见证聚合上界及普通复 Hilbert ISP 继续保持开放。
