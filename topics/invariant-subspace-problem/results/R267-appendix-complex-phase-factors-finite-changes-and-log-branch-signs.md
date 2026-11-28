# R267 附录：复相位实际因子、有限修改不变性与对数支的精确符号

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：实际复因子扩展及精确同源恒等式已证明。** 本稿使后续复抵消尝试具有明确来源，并区分真实无限因子变化与只改有限前缀或对数支。没有支付任何新的奇项上界或单列强紧性。

## 1. 同一原收缩构造允许复相位

固定原 Haar 尾 $C$，记 $c=\|C\|$。使用[相容有理根稿](R267-appendix-coherent-bounded-rational-roots-of-one-flat-common-denominator.md)的 $M_n,d_n,\epsilon_n$ 与实际多项式收缩 $F_n=F_{m_n,q_n}$。它们满足前 $n+1$ 个 Walsh 测试上的正、伴随误差之和不超过 $\epsilon_n/2$。

给任意实数 $\theta_n$ 和 $0<\zeta_n\le\epsilon_n/8$，改取
$$
Z_n=(1-\zeta_n)F_n+\zeta_n e^{i\theta_n}C/c=C U_n(C).
\tag{1}
$$
三角不等式直接给 $\|Z_n\|\le1$。并且
$$
\|Z_n-F_n\|\le2\zeta_n,
$$
所以同一测试仍满足
$$
\|(Z_n-I)h_\ell\|+\|(Z_n^*-I)h_\ell\|
\le\epsilon_n\qquad(\ell\le n).
\tag{2}
$$
$U_n(0)=\zeta_n e^{i\theta_n}/c\ne0$，因而是原范数多项式代数内的可逆解析单位。固定任一零点附近解析对数芽 $\mathcal L_n$，并始终令
$$
U_n(C)^s=\exp(s\mathcal L_n(C)).
\tag{3}
$$
同一个 $n$ 的指数按这个固定选择相加。

以下原证明只使用收缩、(2)、合法整数指数及 (3)，完全继续成立：

- 全部合法整数尾 $T_{r,N}$ 的强*收敛、收缩界和 Walsh 尾预算；
- 切口相容的 $P_r$ 及 $P_rP_s=P_{r+s}$；
- 每个实际 $C^{-a}P_r$ 的有界来源、共同幂理想及同一个原多项式强单位；
- 全部原有限放大闭不变旗子商上的单射和稠值；
- $Y_N^2=CD_N$、$D_N\to I$ 强*，以及固定 $t$ 的实际 $Q_N(t)$。

特别，[全切口平方稿](R267-appendix-all-cut-square-contractions-and-unconditional-strong-square-limit.md)的
$$
L_{NM}
=\left(\prod_{\nu=N}^{M-1}Z_\nu^{d_\nu/M_N}\right)
T_{1/M_N-1/M_M,M}
=R_{NM}^2
\tag{4}
$$
仍是收缩。由同一个实际单射 $D_M$ 消去仍合法，故
$$
Q_N(t)^2\longrightarrow C^{-1}P_{2t}\quad\text{强*}
\tag{5}
$$
和全部平方能量结论不变。[单真空列根接口](R267-appendix-single-actual-denominator-column-compactness-and-stable-root.md)只用原 $J$ 对称性、(5) 和实际 $P_t$ 稠值，因此也适用。

不保留的性质是函数正锥保持：一般复相位下，不声称 $Z_n,T_{r,N},D_N,L_{NM}$ 或 $P_1$ 为正锥保持算子。旧分离单列证明的高二项式同号性也不能照搬到这些复因子。

## 2. 任意有限实际修改的完整关系

考虑两组合法构造，采用同一个 $M_n,d_n$；假设它们从某个 $K$ 起的实际因子和固定对数芽完全相同。$n<K$ 时允许改变块、混合大小、相位及对数支。记两组为无撇和有撇，定义原解析芽
$$
H_s(C)=
\exp\left(
s\sum_{\nu<K}d_\nu
\bigl(\mathcal L_\nu'(C)-\mathcal L_\nu(C)\bigr)
\right)
\qquad(s\in\mathbb R).
\tag{6}
$$
每个 $H_s$ 都是原范数多项式代数内的有界可逆元，
$H_sH_u=H_{s+u}$。

对任一固定正有理数 $r$，取合法切口 $L\ge K$。两组尾积完全相同；有限解析前缀的逐项比值正是 (6)，因而
$$
\boxed{P_r'=H_rP_r.}
\tag{7}
$$
没有把整个平坦乘积取对数；(6) 仅含有限个已定义的解析单位。

对所有 $N\ge K$，记 $\delta_N=1/(2M_N)$，原定义逐项给
$$
V_N'=H_{\delta_N}V_N,\qquad D_N'=D_N.
$$
于是
$$
\boxed{
Y_N'=Y_N,\qquad
Q_N'(t)=H_tQ_N(t).
}
\tag{8}
$$
首式使用 $P_{\delta_N}'=H_{\delta_N}P_{\delta_N}$；第二式使用
$H_{t-\delta_N}H_{\delta_N}=H_t$。$H_t$ 固定且与全部实际来源交换。

因此同一个指定真空列有
$$
\frac{\|Q_N(t)\Omega\|}{\|H_t^{-1}\|}
\le\|Q_N'(t)\Omega\|
\le\|H_t\|\,\|Q_N(t)\Omega\|.
\tag{9}
$$
两列存在强收敛子列当且仅当彼此存在；有界性、相对强紧性、范数趋于无穷亦各自等价。这里直接使用
$Q_N'(t)\Omega=H_t(Q_N(t)\Omega)$，没有把输入换成另一个未知费用向量。

有限修改甚至不改变相应单列极限产生的闭根。若沿某子列
$q_N\to q$，则 $p'=H_tp$、$q'=H_tq$。
由单列稿，旧闭根 $S$ 是两列多项式图的闭包，并在实际域上与 $C$ 交换。
$H_t$ 与 $H_t^{-1}$ 都是原范数多项式极限；闭性遂给二者保持
$\operatorname{Dom}S$ 并与 $S$ 交换。因此
$$
\operatorname{diag}(H_t,H_t)\Gamma S=\Gamma S,
$$
而新两列图的闭包正是左边。所以同一子列产生的实际闭根相同。

## 3. 只换对数支时的全部无限自由度

现在保持每个实际 $Z_n,U_n$ 不变，只令
$$
\mathcal L_n'=\mathcal L_n+2\pi i k_n,\qquad k_n\in\mathbb Z.
\tag{10}
$$
允许无限多个 $k_n$ 非零。写
$$
K_L=\sum_{\nu<L}k_\nu d_\nu.
$$
对正有理数 $r$，选 $rM_L\in\mathbb N$，定义
$$
\chi(r)=e^{2\pi i rK_L}.
\tag{11}
$$
若增大合法切口，每个新增 $r d_\nu$ 为整数，因此 (11) 不变。共同切口又给
$$
\chi(r+s)=\chi(r)\chi(s),\qquad |\chi(r)|=1,
\qquad \chi(a)=1\quad(a\in\mathbb Z_{>0}).
$$
有限前缀直接返回
$$
P_r'=\chi(r)P_r.
\tag{12}
$$

令
$$
\sigma_N=\chi(\delta_N)e^{-2\pi i\delta_N K_N}.
\tag{13}
$$
因为 $2\delta_N=1/M_N$ 在第 $N$ 切口已经合法，
$$
\sigma_N^2
=\chi(1/M_N)e^{-2\pi iK_N/M_N}=1.
$$
故 $\sigma_N\in\{1,-1\}$，且
$$
\boxed{
D_N'=D_N,\qquad
Y_N'=\sigma_NY_N,\qquad
Q_N'(t)=\chi(t)\sigma_NQ_N(t).
}
\tag{14}
$$
因此任意无限对数支修改都不改变这两个实际来源的范数。
它也不改变单列强收敛子列的存在性：在已有强子列内再取一个
$\sigma_N$ 恒定的无限子列即可；反方向相同。
若该子列产生旧闭根 $S$，新两列至多产生 $S$ 或 $-S$。

(14) 不能用于改变实际 $Z_n$ 的复相位；它仅处理同一个
$U_n(C)$ 的对数芽整数分支差。

## 4. 真实尚待支付的复来源

复相位改变了不同二项式阶的相对相位，所以旧正系数单列下界不再直接适用；但这种自由度也尚未给单列上界。

(8) 说明，只改有限个真实因子不能改变这条紧性端点；
(14) 说明，单独换任意多对数支也不够。
若要沿本族解决根来源，必须有真正无限且协调的实际因子选择，并付
$Q_N(t)\Omega$ 的强紧性或其他完整原域输入。
本文没有构造这样的选择，不把复相位自由度本身当作根存在。
