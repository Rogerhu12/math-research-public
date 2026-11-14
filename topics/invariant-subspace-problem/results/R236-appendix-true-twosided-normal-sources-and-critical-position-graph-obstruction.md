# R236 附录：同一正常见证的真实双侧右源与临界位置图域禁阻

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

**状态：完整必要来源约束。** 在同一个原正常见证上，固定双侧原右因子产生的非正迹类源仍有集合尾下界。非零真实迹锚不能被这样的双侧因子同时送入临界位置图域。本文没有证明所需平滑因子存在，也没有排除一般正常湮灭者。

输入是[任意有限高位集合的实际 selector 与正源能量](R236-appendix-uniform-high-bit-set-energy-for-normal-positive-annihilators.md)，其中原头、非连续集合外背景及真实高尾均已付清。

## 1. 原模型与准确右测试范围

令
$$X=\sum_i a_iX_i,\qquad
X_i\in\{\mathsf N_i,\mathsf N_i(I+\mathsf N_i)^{-1}\},$$
$$|a_i|\le A(i+1)^{-2},\qquad
|a_i|\ge a_-(i+1)^{-2}\quad\text{对充分大的 }i.$$
设原 $\rho\ge0$ 为迹类。若有整个实际交换子代数上的方程
$$\operatorname{Tr}(\rho XG)=0\qquad(G\in\mathcal A'),\tag{1.1}$$
则对任意固定 $H,K\in\mathcal A'$，令
$$\sigma=H\rho K,\qquad s=\operatorname{Tr}\sigma
=\operatorname{Tr}(\rho KH).$$
由迹循环及原右因子与 $X$ 交换，
$$\operatorname{Tr}(\sigma XG)
=\operatorname{Tr}\{\rho X(KGH)\}=0
\qquad(G\in\mathcal A').\tag{1.2}$$
$H,K$ 不必彼此交换，$\sigma$ 一般不正。

如果已知的只有原闭幺代数 $\mathcal A$ 上的 $X\mathcal A$ 湮灭，则 (1.2) 只能无条件用于 $H,K\in\mathcal A$，或另已证明全部乘积 $KGH$ 属原测试类的情况。不能把较弱假设偷偷扩大到 $\mathcal A'$。有限矩阵放大在相同真实测试范围内同理。

## 2. 非正迹类源的有限集合下界

本节容许任意迹类 $\sigma$，假定
$$\operatorname{Tr}(\sigma XG)=0\quad(G\in\mathcal A),\qquad
s=\operatorname{Tr}\sigma\ne0,\qquad \mathfrak m=\|\sigma\|_1.$$
对非空有限集合 $I$，令
$$p=\min I,\qquad R_I=\prod_{i\in I}(I-Q_i^-).$$
存在只依赖原行常数及固定比值 $|s|/\mathfrak m$ 的 $p_0$，使 $p\ge p_0$ 时
$$\boxed{\|\sigma-R_I\sigma R_I\|_1
\ge\frac{|s|}{3584A}\left(\sum_{i\in I}|a_i|^2\right)^{1/2}.}\tag{2.1}$$
$p_0$ 不依赖 $I$ 的跨度、最大位、源的秩或有限放大维数；不声称对移动且迹锚退化的源一致。

**证明。** 使用所引稿中同一个实际 selector。取最大平方质量的四相位扇区 $F\subset I$，置
$$B^2=\sum_{i\in F}|a_i|^2\ge\frac14\sum_{i\in I}|a_i|^2.$$
实际均值零的 $G\in\mathcal A$ 满足 $\|G\|\le2$。令 $T=XG$，则
$$\|T\|\le12A,\qquad
R_ITR_I=\kappa_0R_I+E_I,$$
$$|\kappa_0|\ge B/64,\qquad
\|E_I\|\le e_p
=36A\eta_{p-1}
+\left(\frac{8A}{p}+\frac{144A^2p}{a_-}\right)\eta_p.\tag{2.2}$$
这是完整原算子的压缩身份，$R_I$ 从未被当作合法右因子。

此外，所引稿的单 Walsh 系数表示
$\kappa_0=\frac12\sum_{i\in F}a_ig_i$、$\sum_i|g_i|^2\le1$ 给
$|\kappa_0|\le B$；而 $B\le2A$。由
$$B\ge a_-/[2(p+1)^2]$$
和原超指数误差，$e_p/B\to0$ 一致于全部有限 $I$。

记 $\epsilon=\|\sigma-R_I\sigma R_I\|_1$。由 $\operatorname{Tr}(\sigma T)=0$，
$$|\operatorname{Tr}(R_I\sigma R_IT)|\le12A\epsilon.$$
又
$$|\operatorname{Tr}(R_I\sigma R_I)-s|\le\epsilon,\qquad
\|R_I\sigma R_I\|_1\le\mathfrak m.$$
结合 (2.2)，
$$(|\kappa_0|+12A)\epsilon
\ge|\kappa_0||s|-\mathfrak m e_p.$$
取高 $p$ 使 $e_p\le |s|B/(128\mathfrak m)$，右侧至少为 $|s|B/128$，左系数至多 $14A$。故
$$\epsilon\ge |s|B/(1792A)
\ge |s|\|a_I\|_2/(3584A).$$
没有对非正 $\sigma$ 使用 gentle compression。证毕。

## 3. 临界位置图域的真实双侧禁阻

令原位置算子
$$M\chi_F=(1+\max F)\chi_F,\qquad M\Omega=0,$$
并令 $\Pi_P$ 为所有 $\ge P$ Walsh 位均为 plus 的柱投影。

取原正分解
$$\rho=\sum_\ell |f_\ell\rangle\langle f_\ell|,
\qquad\sum_\ell\|f_\ell\|^2<\infty.$$
保持 §1 允许的固定原 $H,K$，置
$$u_\ell=Hf_\ell,\qquad v_\ell=K^*f_\ell,\qquad
\sigma=\sum_\ell |u_\ell\rangle\langle v_\ell|.$$
若两端属于真实闭算子的图域，且
$$\boxed{\sum_\ell\left\{
\|M^{3/2}u_\ell\|\|v_\ell\|
+\|u_\ell\|\|M^{3/2}v_\ell\|
\right\}<\infty,}\tag{3.1}$$
则必有
$$\boxed{\operatorname{Tr}(\rho KH)=0.}\tag{3.2}$$
有限秩时只需每个 $Hf_\ell,K^*f_\ell\in\operatorname{Dom}M^{3/2}$。

**证明。** 取 $I=[P,2P)$。因 $I-R_I\preceq I-\Pi_P$，逐项秩一分解给
$$\begin{aligned}
\|\sigma-R_I\sigma R_I\|_1\le\sum_\ell\{&
\|(I-R_I)u_\ell\|\|v_\ell\|\\
&+\|u_\ell\|\|(I-R_I)v_\ell\|\}.
\end{aligned}$$
对 $u\in\operatorname{Dom}M^{3/2}$，
$$P^{3/2}\|(I-\Pi_P)u\|\longrightarrow0,\qquad
P^{3/2}\|(I-\Pi_P)u\|\le\|M^{3/2}u\|.$$
由 (3.1) 作支配收敛，上述迹范数严格为 $o(P^{-3/2})$。

若 $s\ne0$，(2.1) 和
$$\|a_{[P,2P)}\|_2\ge a_-/(4P^{3/2})$$
给出相反的固定正倍数下界，矛盾。因此 (3.2) 成立。

另一个足够的精确条件是两个实际图乘积
$$M^{3/2}\sigma\in\mathcal S_1,\qquad
\sigma M^{3/2}\in\mathcal S_1.\tag{3.3}$$
这里必须由原闭算子定义并有迹类延拓，不能只是形式乘积。对第一项，
$$P^{3/2}\|(I-\Pi_P)\sigma\|_1
\le\|(I-\Pi_P)M^{3/2}\sigma\|_1\longrightarrow0,$$
右乘同理；由此直接得到同样矛盾。(3.1) 蕴含 (3.3)，无需宣称任意迹类图条件一定存在同一分解满足 (3.1)。

## 4. 范围与未付来源

(2.1) 保留同一个非正原源及其真实迹锚，(3.1) 保留 $Hf_\ell,K^*f_\ell$ 两侧图域和总费用。没有证明存在能将非零锚送进这些图域的合法 $H,K$，也没有对移动 $H_P,K_P$ 给出免费一致性。

取 $H=K=I$ 时，(3.1) 包含原正源的有限三阶位置矩，恢复已证的临界矩发散。若已有一般 $p>1$ 的实际 selector，并有 $|a_i|\asymp(i+1)^{-p}$，同一论证把临界图指数换成 $p-\tfrac12$；这仅是对应图域结论，不新增一般源排除。

完整 ISP、一般正常见证及其真正非对角源仍开放。
