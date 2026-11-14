# R150 附录：正 first 半群的精确加权占据指数增益

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf。根代理提出临界常数与剥头测试；本文补全无限张量、移动权、真实 carry 和全部自然域；根代理与 normal_resume_1cf 已核全部证明。

状态：完整证明。这里的权是系数加权占据算子，不是通常 Walsh 次数。临界增益准确为 $2t$；在不可和情形，任意更大的增益均失败。结论不包含正常见证的聚合配对预算。

## 1. 定理与精确自然域

取非负实系数
$$
a=(a_j)_{j\ge0}\in\ell^2,\qquad a_j\ge0,
$$
令 $X=X_a$ 为原 Haar 表示中的实际闭 first，
$$
S(t)=e^{-tX}\qquad(t\ge0).
$$
$X$ 最大增生，$S$ 是收缩 $C_0$ 半群。定义非负自伴算子
$$
\mathcal N_a\chi_F=\left(\sum_{j\in F}a_j\right)\chi_F
$$
及
$$
W_\sigma=e^{\sigma\mathcal N_a},\qquad
H_{a,\sigma}=\operatorname{Dom}W_\sigma,\qquad
\|f\|_{a,\sigma}=\|W_\sigma f\|,\quad \sigma\ge0.
$$
$W_{-\sigma}=e^{-\sigma\mathcal N_a}$ 是全空间收缩，准确将 $H$ 一一映到 $H_{a,\sigma}$。

**定理。** 对每个固定 $t>0$、$\delta\ge0$：

1. 有临界端点的完整像包含
   $$
   \boxed{
   S(t)H_{a,\delta}\subseteq H_{a,\delta+2t},\qquad
   W_{\delta+2t}S(t)W_{-\delta}\in B(H).
   }
   \tag{1.1}
   $$
2. 对任意 $\rho\ge0$，自然算子
   $$
   T_{\rho,\delta}(t)=W_\rho S(t)W_{-\delta},
   \quad
   \operatorname{Dom}T_{\rho,\delta}(t)
   =\{h:S(t)W_{-\delta}h\in H_{a,\rho}\}
   \tag{1.2}
   $$
   闭且稠密定义。若 $a\notin\ell^1$，则
   $$
   \boxed{
   \operatorname{Dom}T_{\rho,\delta}(t)=H
   \ \Longleftrightarrow\
   T_{\rho,\delta}(t)\text{ 有全域有界延拓}
   \ \Longleftrightarrow\
   \rho\le\delta+2t.
   }
   \tag{1.3}
   $$
   对 $\rho>\delta+2t$，下面给出实际自然域中的测试向量，使算子范数比趋于无穷。
3. 若 $a\in\ell^1$（包括零行），则 $\mathcal N_a$ 有界，所以 (1.2) 对全部 $\rho,\delta\ge0$ 全域有界；不在此情形声称有限临界阈值。

特别，$\delta=0$ 给
$$
\boxed{e^{2t\mathcal N_a}S(t)\in B(H),}
\tag{1.4}
$$
而在 $a\notin\ell^1$ 时，任何 $\rho>2t$ 均不能替换 (1.4) 中的 $2t$。

以下证明给一个明确有限的上界。置
$$
g=\|a\|_2,\quad M=\|a\|_\infty,\quad
\eta_*=\sup_j\eta_j<1/4,
$$
$$
b_\delta(r)=\sum_j a_j\sinh((\delta+2r)a_j),
\tag{1.5}
$$
以及
$$
K_a(\sigma)
=18\left(\sum_j a_j\eta_j\right)
\sum_{L\ge1}e^{\sigma g\sqrt{L+1}}\eta_*^{L-1}.
\tag{1.6}
$$
这些量在每个紧参数区间有限且有界。可取
$$
\boxed{
\|W_{\delta+2t}S(t)W_{-\delta}\|
\le
\exp\!\left[
\int_0^t\bigl(b_\delta(r)+K_a(\delta+2r)\bigr)\,dr
\right].
}
\tag{1.7}
$$
常数不声称最优；增益阈值 $2t$ 则由后半篇证明锐性。

## 2. 实际 first 的纯部分与局部 carry

沿用 [正时间半群完整行分类](R150-appendix-positive-time-semigroup-first-domain-classification.md) §2 的实际分解
$$
X=X^0+E_a,\qquad
E_a=\sum_j a_j(V_j-S_j^0),\qquad
\operatorname{Dom}X^0=\operatorname{Dom}X.
\tag{2.1}
$$
在每位 Walsh 基 $(1,\chi_j)$ 上，
$$
S_j^0=\begin{pmatrix}0&-1\\1&2\end{pmatrix},\qquad
n_j=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
$$
$X^0$ 是纯和的实际最大增生闭实现，
$$
S^0(t)=e^{-tX^0}.
$$
有限 Walsh 柱为 $X^0$ 的图核心；有限纯张量半群在紧时间区间强一致收敛到 $S^0$。该生成元识别与强极限已由所引稿 §3.2 逐项证明。

本稿还使用 [R181 §§2--3](R181-bounded-coefficient-bell-polynomial-spectrum-trichotomy.md) 的真实局部级数
$$
V_j-S_j^0=\sum_{L\ge1}B_{j,j+L},\qquad
\operatorname{supp}B_{j,j+L}\subseteq[j,j+L],
$$
$$
\|B_{j,j+L}\|\le18\eta_j\eta_*^{L-1}.
\tag{2.2}
$$
它们是有限位矩阵，外面张量恒等；不删除原进位。通常范数下还有
$$
\|V_j-S_j^0\|\le8\eta_j,\qquad
\|E_a\|\le8\|\eta\|_2g.
\tag{2.3}
$$
$E_a$ 属于 UHF 范数闭包；不将其自动放入 $\mathcal A$。

## 3. 真实 carry 的完整加权共轭

对作用于有限位集 $J$ 的算子 $B$，把 $\mathcal N_a$ 分成 $J$ 内外两部分。在 $J$ 的有限维空间上，权的最大、最小比给
$$
\|W_\sigma B W_{-\sigma}\|
\le e^{\sigma\sum_{j\in J}a_j}\|B\|.
\tag{3.1}
$$
这里先在有限柱上共轭；右侧有界后延为全空间算子。对 (2.2) 的支撑，
$$
\sum_{k=j}^{j+L}a_k\le g\sqrt{L+1}.
$$
所以级数
$$
E_a(\sigma)
=\sum_{j\ge0}\sum_{L\ge1}
a_j\,W_\sigma B_{j,j+L}W_{-\sigma}
\tag{3.2}
$$
在算子范数中绝对收敛，并且
$$
\boxed{\|E_a(\sigma)\|\le K_a(\sigma).}
\tag{3.3}
$$
$\sum a_j\eta_j\le g\|\eta\|_2$；
对每个固定上界 $\sigma_0$，
$e^{\sigma_0g\sqrt{L+1}}\eta_*^{L-1}$ 可和。
因此 (3.2) 在 $0\le\sigma\le\sigma_0$ 上一致范数收敛。
每个有限局部共轭项对 $\sigma$ 算子范数连续，故 $E_a(\sigma)$ 也范数连续。

从每个局部项的准确恒等式取范数极限，得到全空间有界恒等式
$$
\boxed{E_aW_{-\sigma}=W_{-\sigma}E_a(\sigma).}
\tag{3.4}
$$
因为 $\operatorname{Ran}W_{-\sigma}=H_{a,\sigma}$，
(3.4) 同时证明 $E_a$ 保持该真实加权域，且其共轭恰为 (3.2)。
没有在未验证的输入上直接施加无界 $W_\sigma$。

## 4. 纯半群的移动权：端点中的线性项准确消去

固定 $\delta\ge0$ 与 $T<\infty$。先取有限头
$$
\mathcal N_{a,n}=\sum_{j<n}a_jn_j,\qquad
X_n^0=\sum_{j<n}a_jS_j^0.
$$
对 $0\le s\le t\le T$ 定义全域有界算子
$$
U^0_{\delta,n}(t,s)=
e^{(\delta+2t)\mathcal N_{a,n}}\,
e^{-(t-s)X_n^0}\,
e^{-(\delta+2s)\mathcal N_{a,n}}.
\tag{4.1}
$$
所有因子仍为实际有限位纯矩阵；没有改变其外面的 Haar 真空。

### 4.1 一位时间生成元

单个位的移动权方程为
$$
\frac d{dt}U^0_j(t,s)=G_j(t)U^0_j(t,s),
$$
$$
G_j(t)=
-a_j\begin{pmatrix}
0&-e^{-(\delta+2t)a_j}\\
e^{(\delta+2t)a_j}&0
\end{pmatrix}.
\tag{4.2}
$$
确实，原 $-a_jS_j^0$ 的占据对角项 $-2a_jn_j$
被移动权导数 $2a_jn_j$ 准确抵消。
$G_j(t)$ 的实部有特征值
$\pm a_j\sinh((\delta+2t)a_j)$。
于是对有限头的范数平方求导，得到
$$
\boxed{
\|U^0_{\delta,n}(t,s)\|
\le
\exp\!\left(\int_s^t\sum_{j<n}
a_j\sinh((\delta+2r)a_j)\,dr\right).
}
\tag{4.3}
$$
因为
$$
a_j\sinh((\delta+2r)a_j)
\le(\delta+2T)\cosh((\delta+2T)M)a_j^2,
$$
右侧统一有界。极限上界可记为
$$
C_\delta(t,s)=
\exp\!\left(\int_s^t b_\delta(r)\,dr\right).
\tag{4.4}
$$
它满足 $C_\delta(t,r)C_\delta(r,s)=C_\delta(t,s)$。

### 4.2 无限张量的强极限

强极限也要单独支付。对单个位真空 $\Omega_j=1$，令 $h=t-s$。右侧初始权固定真空，故
$$
U_j^0(t,s)\Omega_j=
e^{-ha_j}\left[(1+ha_j)\Omega_j
-ha_je^{(\delta+2t)a_j}\chi_j\right].
\tag{4.5}
$$
其真空内积为
$$
r_j=e^{-ha_j}(1+ha_j)\in[0,1],\qquad
1-r_j\le h^2a_j^2/2.
\tag{4.6}
$$
对一个尾区间 $J=[n,N)$，用 (4.3) 及 tensor 范数乘法，
$$
\left\|\bigotimes_{j\in J}U_j^0(t,s)\Omega_j\right\|^2
\le\exp(C_{\delta,T,a}\sum_{j\in J}a_j^2).
$$
结合 (4.6) 和 $1-\prod r_j\le\sum(1-r_j)$，
$$
\left\|
\bigotimes_{j\in J}U_j^0(t,s)\Omega_j-\Omega_J
\right\|^2
\le
e^{C_{\delta,T,a}\sum_Ja_j^2}-1+T^2\sum_Ja_j^2
\le C'_{\delta,T,a}\sum_Ja_j^2.
\tag{4.7}
$$
最后一步用 $\sum_Ja_j^2\le g^2$，常数与 $n,N,s,t$ 无关。

对任何固定有限柱输入，将其低头与 $[n,N)$ 的真空尾分开，
(4.3)、(4.7) 给 $U^0_{\delta,n}(t,s)$ 的强 Cauchy 性，且在
$0\le s\le t\le T$ 上一致。
有限柱稠密及 (4.3) 遂给全空间强极限
$$
U^0_\delta(t,s)=\operatorname*{SOT-lim}_{n\to\infty}
U^0_{\delta,n}(t,s),\qquad
\|U^0_\delta(t,s)\|\le C_\delta(t,s).
\tag{4.8}
$$
它对 $(t,s)$ 强连续，且有限头的演化律在统一有界强极限中保留。

### 4.3 无界权的准确识别

从有限头准确等式
$$
e^{-(\delta+2t)\mathcal N_{a,n}}U^0_{\delta,n}(t,s)
=e^{-(t-s)X_n^0}
e^{-(\delta+2s)\mathcal N_{a,n}}
$$
取强极限。所有这里取极限的权都是有界逆权，
它们逐 Walsh 系数收敛且范数至多1。
纯半群的强极限由 §2 已付。
因此
$$
\boxed{
W_{-(\delta+2t)}U^0_\delta(t,s)
=S^0(t-s)W_{-(\delta+2s)}.
}
\tag{4.9}
$$
右侧的像于是确在 $H_{a,\delta+2t}$，
且其左乘 $W_{\delta+2t}$ 正是 $U^0_\delta(t,s)$。
这个步骤没有从有限无界权的形式极限直接认定完整域。

## 5. 加回真实 carry 的移动权演化

在 $0\le s\le t\le T$ 上，考虑强 Volterra 方程
$$
U_\delta(t,s)=U^0_\delta(t,s)
-\int_s^t U^0_\delta(t,r)
E_a(\delta+2r)U_\delta(r,s)\,dr.
\tag{5.1}
$$
§§3--4 已给强连续、统一有界的纯演化和范数连续有界扰动。
逐次代入 (5.1) 的 Picard 级数，每个向量积分都是 Bochner 积分；
第 $k$ 项有固定常数的 $k$ 次幂乘 $(t-s)^k/k!$ 的界。
故该级数定义唯一的强连续有界解。

利用 (4.4) 的乘法性质，对向量范数的积分不等式作 Gronwall，
得到
$$
\boxed{
\|U_\delta(t,s)\|
\le\exp\!\left[
\int_s^t\bigl(b_\delta(r)+K_a(\delta+2r)\bigr)\,dr
\right].
}
\tag{5.2}
$$

现在把 (5.1) 左乘有界 $W_{-(\delta+2t)}$。
由 (4.9) 与 (3.4)，
$$
W_{-(\delta+2t)}U^0_\delta(t,r)
E_a(\delta+2r)
=
S^0(t-r)E_aW_{-(\delta+2r)}.
$$
所以
$$
F(t,s):=W_{-(\delta+2t)}U_\delta(t,s)
$$
满足准确的无权 Duhamel 方程
$$
F(t,s)=
S^0(t-s)W_{-(\delta+2s)}
-\int_s^t S^0(t-r)E_aF(r,s)\,dr.
\tag{5.3}
$$
而 $X=X^0+E_a$ 是在同一完整域上的有界扰动，
实际半群 $S(t-s)W_{-(\delta+2s)}$ 满足同一个方程。
由强 Volterra 方程的唯一性，
$$
\boxed{
S(t-s)W_{-(\delta+2s)}
=W_{-(\delta+2t)}U_\delta(t,s).
}
\tag{5.4}
$$
取 $s=0$，$W_{-(\delta+2t)}$ 的准确像是
$H_{a,\delta+2t}$，故 (5.4) 付清 (1.1)，并由 (5.2) 得 (1.7)。

若 $0\le\rho\le\delta+2t$，再左乘有界逆权
$W_{-(\delta+2t-\rho)}$，得到
$$
W_\rho S(t)W_{-\delta}
=W_{-(\delta+2t-\rho)}U_\delta(t,0)\in B(H).
\tag{5.5}
$$

## 6. 全部参数的自然闭图与稠密域

$S(t)W_{-\delta}$ 有界，$W_\rho$ 闭，所以 (1.2) 的自然乘积闭。

若 $\rho>\delta+2t$，置 $\kappa=\rho-\delta-2t>0$。
对 $h\in H_{a,\kappa}$，
$$
W_{-\delta}h\in H_{a,\delta+\kappa}.
$$
将 (1.1) 用于起始权 $\delta+\kappa$，即得
$S(t)W_{-\delta}h\in H_{a,\rho}$。
因此
$$
\boxed{
H_{a,\max(0,\rho-\delta-2t)}
\subseteq\operatorname{Dom}T_{\rho,\delta}(t).
}
\tag{6.1}
$$
这些空间都包含全部有限 Walsh 柱且稠密，故自然域稠密。

自然域若为全 $H$，闭图定理给有界。
若一个闭的稠密自然图有全域有界延拓，以自然域向量逼近任意输入再用闭性，
也迫自然域本来就全域。
所以只须在越过临界时证明自然域上的范数比无界。

## 7. 不可和行的实际剥头与正对角测试

以下假设 $a\notin\ell^1$，固定 $t>0$。记
$$
H_m=\sum_{j<m}a_jV_j,\qquad
A_m=\sum_{j<m}a_j,\qquad
g_m=\|a_{\ge m}\|_2,\qquad
\varepsilon_m=\sup_{j\ge m}a_j.
$$
$H_m$ 是实际有界头和，保留其对无限尾的 carry。
由于 $a_j\to0$，有
$$
A_m=o(m),\qquad \varepsilon_m\to0,\qquad g_m\to0.
\tag{7.1}
$$

每个不可和正尾都有有限集 $F_m\subseteq[m,\infty)$，使
$$
m\le s_m:=\sum_{j\in F_m}a_j\le m+\varepsilon_m.
\tag{7.2}
$$
例如沿物理次序累加到首次越过 $m$。零系数位不影响构造。

令 $S_{\ge m}(t)$、$S^0_{\ge m}(t)$ 分别是实际尾与纯尾半群。
实际正 first 的半群加法及有界交换给
$$
\boxed{S(t)e^{tH_m}=S_{\ge m}(t).}
\tag{7.3}
$$
这里 $e^{tH_m}$ 是原有界算子的真正指数。
(7.3) 可先用有限实际系数指数相乘，再取已知一致有界负半群强极限；
也可由有界交换扰动识别。

### 7.1 纯尾对角系数的下界

充分大的 $m$ 满足 $t\varepsilon_m\le1/2$。
在每位上，
$$
e^{-xS_j^0}=e^{-x}
\begin{pmatrix}1+x&x\\-x&1-x\end{pmatrix}.
$$
所以纯尾的准确 Walsh 对角系数为
$$
\langle S^0_{\ge m}(t)\chi_{F_m},\chi_{F_m}\rangle
=
\prod_{j\in F_m}e^{-ta_j}(1-ta_j)
\prod_{\substack{j\ge m\\j\notin F_m}}
e^{-ta_j}(1+ta_j).
\tag{7.4}
$$
第二个无限乘积收敛且为正，因为其对数绝对值由常数乘
$t^2\sum_{j\ge m}a_j^2$ 控制。
该式也可直接从纯张量强极限取得。

对 $0\le x\le1/2$，
$$
\log(1-x)\ge-x-x^2,\qquad
\log(1+x)\ge x-x^2/2.
$$
代入 (7.4)，得到
$$
\boxed{
\langle S^0_{\ge m}(t)\chi_{F_m},\chi_{F_m}\rangle
\ge e^{-2ts_m-t^2g_m^2}.
}
\tag{7.5}
$$

### 7.2 真实 carry 不改变该指数下型

实际与纯尾的有界扰动差为
$$
E_{a,\ge m}=\sum_{j\ge m}a_j(V_j-S_j^0).
$$
两尾半群均收缩，所以 Duhamel 给
$$
\|S_{\ge m}(t)-S^0_{\ge m}(t)\|
\le t\|E_{a,\ge m}\|
\le8t g_m\|\eta_{\ge m}\|_2.
\tag{7.6}
$$
本题原进位满足 $\eta_j\le e^{-77016^j}$，因此
$$
\|S_{\ge m}(t)-S^0_{\ge m}(t)\|
\le16t g_m e^{-77016^m}.
\tag{7.7}
$$
由 (7.2)，这个误差比 (7.5) 的下界小任意固定比例。
故充分大的 $m$ 有
$$
\boxed{
\left|\langle S_{\ge m}(t)\chi_{F_m},\chi_{F_m}\rangle\right|
\ge\tfrac12 e^{-2ts_m-t^2g_m^2}.
}
\tag{7.8}
$$
$F_m$ 的最大物理位可以很大；(7.7) 只按真实尾起点 $m$ 估计，因此没有遗漏该选择的成本。

## 8. 任意起始权的锐性，含全部测试域

固定 $\delta\ge0$。由 §3，每个有限实际头 $H_m$ 保持 $H_{a,\delta}$，
其准确加权共轭记为 $H_{m,\delta}$。
纯头的单个位矩阵给
$$
\|W_\delta S_j^0 W_{-\delta}\|
\le3+e^{\delta M}=:C_\delta.
$$
头 carry 的共轭是 (3.2) 对 $j<m$ 的子和，故
$$
\boxed{\|H_{m,\delta}\|
\le C_\delta A_m+K_a(\delta).}
\tag{8.1}
$$
从有界恒等 $H_mW_{-\delta}=W_{-\delta}H_{m,\delta}$
取指数级数可得
$$
e^{tH_m}W_{-\delta}=W_{-\delta}e^{tH_{m,\delta}}.
\tag{8.2}
$$
所以所有以下输入都在准确加权域内。

定义
$$
f_m=e^{tH_m}W_{-\delta}\chi_{F_m},\qquad
h_m=W_\delta f_m.
\tag{8.3}
$$
由 (8.1)--(8.2)，
$$
\boxed{
\|h_m\|\le\exp\{t[C_\delta A_m+K_a(\delta)]\}.
}
\tag{8.4}
$$
同一论证对任意更大的固定权也成立；
$\chi_{F_m}$ 属于全部这些权域，
故 $f_m$ 属于每个 $H_{a,\sigma}$。
结合 (1.1)，$S(t)f_m$ 也属于每个有限权域。
因此 $h_m$ 确实属于每个
$\operatorname{Dom}T_{\rho,\delta}(t)$，
下面不是在假定全域后才写一个未定义的测试。

由 (7.3) 与 $W_{-\delta}\chi_{F_m}=e^{-\delta s_m}\chi_{F_m}$，
$$
S(t)f_m=e^{-\delta s_m}S_{\ge m}(t)\chi_{F_m}.
$$
因为 $W_\rho\chi_{F_m}=e^{\rho s_m}\chi_{F_m}$，
(7.8) 给
$$
\begin{aligned}
\|T_{\rho,\delta}(t)h_m\|
&=\|W_\rho S(t)f_m\|\\
&\ge e^{(\rho-\delta)s_m}
\left|\langle S_{\ge m}(t)\chi_{F_m},\chi_{F_m}\rangle\right|\\
&\ge\tfrac12 e^{(\rho-\delta-2t)s_m-t^2g_m^2}.
\end{aligned}
\tag{8.5}
$$
若 $\rho>\delta+2t$，由 (7.1)--(7.2) 与 (8.4)，
$$
\boxed{
\frac{\|T_{\rho,\delta}(t)h_m\|}{\|h_m\|}
\ge
\tfrac12\exp\!\left[
(\rho-\delta-2t)s_m-t^2g_m^2
-tC_\delta A_m-tK_a(\delta)
\right]\longrightarrow\infty.
}
\tag{8.6}
$$
这证明临界之外自然乘积无界。
由 §6 的闭图与稠密域事实，它不可能全域，也不可能有全域有界延拓。
定理全部得证。

## 9. 范围扣除与准确用途

先前正时间完整行分类给
$$
Y_cS_a(t)\in B(H)
\quad\Longleftrightarrow\quad
c\in\ell^1+\ell^2(a^{-1}),
$$
其中零 $a_j$ 位由 $\ell^1$ 部分承担。
本稿不重证该分类；新增的是系数占据算子
$\mathcal N_a$ 的全部指数权域、临界 $2t$ 和其锐性。

当 $a\notin\ell^1$ 时，这与
$S_a(t)H\not\subseteq\operatorname{Dom}X_a$ 完全相容：
$\mathcal N_a$ 是非负占据权，$X_a$ 还含实际的产生、消灭及 carry。
二者的域不能互换。

又因 $a_j\to0$，这里的 $H_{a,\sigma}$ 不是通常
$\operatorname{Dom}e^{\sigma\mathcal N}$。
不能用 (1.1) 免费获得 R255 所需的统一 Walsh 次数指数矩，
也不能由此保证 R244/R267 对任意正常见证的指定配对域或聚合矩。
R253/R263 的慢符号值域障碍仍保持原范围。

证明全程在原 Haar 空间中进行。
$W_\sigma$ 是用于估计的实际占据权，不假定它保持未知 $A$ 不变空间；
本稿不把任何结论自动下传到这些限制或旗子商。
普通 Hilbert 不变子空间问题的完成标准仍未达到。
