# 同一实际投影缺陷支付双边发生器与全部暗对高矩

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro  
日期：2026-11-15

## 0. 仍是原来的固定测试和原投影

保持原连续远尾、原有限 cut 闭空间 $K_Q\subset V_Q$ 及同一个固定有限物理测试 $f$。远尾起点 $x$ 取到 $f$ 在全部 $i\ge x$ 位上为真空。写
$$
v=P_{V_Q}f,\qquad k=P_{K_Q}f,\qquad u_f=v-k,
$$
$$
e=f-v,\qquad
\zeta_f=\|e\|+\|k\|.
\tag{0.1}
$$
由于 $e\in V_Q^\perp$、$k\in K_Q\subset V_Q$，
$$
e\perp k,\qquad f-u_f=e+k,
$$
从而
$$
\boxed{
\zeta_f^2\le2\|f-u_f\|^2
=2\bigl(\|f\|^2-\|u_f\|^2\bigr).
}
\tag{0.2}
$$
最后等式使用原 $u_f=P_{V_Q\ominus K_Q}f$ 的正交投影身份。

本文把先前实际交换行、双边发生器和全部暗对高矩中的固定测试范数，替换为这个同一投影的真实缺陷。没有重选 $u_f$、重选窗口或新增正则化源。

## 1. 双边发生器的缺陷预算

令 $\mathcal L=\sum_{i\ge x}(I-V_i)$ 为已付原加权交换闭发生器，
$\mathcal A=\mathcal L-\mathcal L^*$。原远真空 $f$ 满足
$$
V_if=V_i^*f=f,\qquad
\mathcal Lf=\mathcal L^*f=\mathcal Af=0.
\tag{1.1}
$$
对 $E=V_Q$ 或 $K_Q$、$z=P_Ef$，已付真实压后谐和方程给
$$
\langle(I-V_i)z,z\rangle=0,
$$
以及
$$
\mathcal Lz=P_E\mathcal Az,\qquad
\mathcal L^*z=-(I-P_E)\mathcal Az.
\tag{1.2}
$$
这两列相互正交。

因 (1.1)，$e=f-v$ 也有
$$
\langle(I-V_i)e,e\rangle
=\langle(I-V_i)v,v\rangle=0.
$$
局部真实矩阵的实部估计因而同时给
$$
\mathfrak e_x(e)\le\frac{\|e\|^2}{x},
\qquad
\mathfrak e_x(k)\le\frac{\|k\|^2}{x},
\tag{1.3}
$$
其中 $\mathfrak e_x(z)=\sum_i\|P_i^-z\|^2$。

又 $\mathcal Av=-\mathcal Ae$。将已付单调漂移算子界
$$
\|\mathcal Az\|
\le8x^{-1/2}\mathfrak e_x(z)^{1/2}
+4x^{-1}\|z\|
$$
应用于 $e,k$，并使用 (1.2)，得到
$$
\|\mathcal Lv\|^2+\|\mathcal L^*v\|^2
=\|\mathcal Ae\|^2\le144x^{-2}\|e\|^2,
$$
$$
\|\mathcal Lk\|^2+\|\mathcal L^*k\|^2
\le144x^{-2}\|k\|^2.
$$
所以原同一个 $u_f=v-k$ 满足
$$
\boxed{
\mathfrak e_x(u_f)\le\frac{\zeta_f^2}{x},
\qquad
\left(\|\mathcal Lu_f\|^2+\|\mathcal L^*u_f\|^2\right)^{1/2}
\le\frac{12\zeta_f}{x}.
}
\tag{1.4}
$$
发生器在原有限孔直和上的有界实现与其闭直和自然域一致；这里没有将反向完整伴随误换成压缩伴随。

## 2. 实参数投影列的相对导数方程

任取有限组不交相邻远对，仍作保持各对几何平均的真实变形
$$
S(t)=\exp\left(\sum_i t_iH_i\right),
\qquad H_i=n_{i+1}-n_i,\qquad0\le t_i\le\theta_i.
$$
$f$ 在每个所选对上真空，故 $H_if=0$。对原闭空间 $E(t)=S(t)E(0)$，令 $P(t)=P_{E(t)}$。

正交投影的实微分公式
$$
\partial_iP=H_iP+PH_i-2PH_iP
$$
给出一个保同列的反射方程：无论取
$$
z(t)=P(t)f
\quad\text{还是}\quad
z(t)=(I-P(t))f,
$$
都准确有
$$
\boxed{
\partial_i z(t)=R_i(t)z(t),
\qquad R_i(t)=(I-2P(t))H_i,
\qquad \|R_i(t)\|\le1.
}
\tag{2.1}
$$
两种取法均使用 $H_if=0$；没有把 $P(t)$ 与 $H_i$ 交换。

原实参数归纳给
$\|\partial_TP(t)\|\le4^{|T|}|T|!$。因此 $|T|\ge1$ 时
$$
\|\partial_TR_i(t)\|\le2\cdot4^{|T|}|T|!.
$$
对 (2.1) 再微分，并在同一参数点使用较低阶相对导数界，得
$$
\boxed{
\|\partial_Sz(t)\|\le4^r r!\,\|z(t)\|,
\qquad |S|=r.
}
\tag{2.2}
$$
详细地，若相对常数记为 $a_r$，则
$$
a_r\le a_{r-1}
+2\sum_{j=1}^{r-1}
\binom{r-1}{j}4^j j!\,a_{r-1-j}.
$$
代入 $a_s=4^s s!$，右边至多
$(2r-1)4^{r-1}(r-1)!\le4^r r!$。这是在每个实参数点的齐次估计；$z(t)=0$ 时也由同一方程成立，不需除以其范数。

沿实参数盒逐坐标积分，(2.1) 的 Gronwall 界还给
$$
\boxed{
\|z(t)\|\le
\exp\left(\sum_{i\in S}\theta_i\right)\|z(\theta)\|.
}
\tag{2.3}
$$
因此混合微积分基本定理最终可以使用原实际权处的列范数，而非整个 $\|f\|$。

## 3. 未压旗的全部暗对矩

记
$$
e(t)=(I-P_{V_Q(t)})f,\qquad
k(t)=P_{K_Q(t)}f.
$$
二者各自适用 (2.1)--(2.3)，且
$$
u_f(t)=f-e(t)-k(t).
$$
所有物理暗投影、真 primitive 暗投影均杀掉 $f$。在任一 $t_i=0$ 面上，原物理 $U_i$ 约化两个原空间，故各暗分量仍严格消失。

沿用原稿的两种暗计数 $N_\sigma$，其中物理暗对 $\sigma=4$、真 primitive 暗对 $\sigma=5$。对 $r$ 元所选对集 $S$，混合微积分基本定理、(2.2)--(2.3)，以及真 primitive 局部投影的 $\|(A_i^-)'(t_i)\|\le1$，给
$$
\left\|\left(\prod_{i\in S}P_{i,\sigma}^{\rm dark}\right)u_f\right\|
\le
\sigma^r r!\,
\prod_{i\in S}(\theta_i e^{\theta_i})\,
\zeta_f.
\tag{3.1}
$$
原相似仅改有限对，其余所有位、所有 nuisance 与 cut 不变。

定义同一不交对族的有限量
$$
a_x=\sum_i\theta_i^2e^{2\theta_i}
\le\frac{e^{2/(x+1)}}{x}.
\tag{3.2}
$$
有限族同时对角化，再对无限族作非负 Tonelli，得到
$$
\boxed{
\left\langle\binom{N_\sigma}{r}u_f,u_f\right\rangle
\le r!(\sigma^2a_x)^r\zeta_f^2.
}
\tag{3.3}
$$
这保留原计数次序，不把它移过 MP。若对族为空，则 $a_x=0$ 且所有相关暗分量都为零。

## 4. 全部真正交 jet 旗的缺陷高矩

写
$$
F_j(t)=P_{\ker D(t)^j}-P_{\ker D(t)^{j-1}},
\qquad \mathcal F(t)z=(F_j(t)z)_j.
$$
[全旗导数带宽稿](R271-appendix-all-orthogonal-jet-flags-dark-factorial-moments-and-derivative-bandwidth.md)已证明
$$
\left\|z\mapsto((\partial_SF_j)z)_j\right\|
\le2\sqrt{2r+1}\,4^r r!.
\tag{4.1}
$$
它来自真实 $H_i$ 三带及每个导数词至少插入一个 $F_j$，不是逐 $j$ 求和。

将 (4.1) 与 (2.2) 做完整 Leibniz，对 $z=e$ 或 $k$ 得
$$
\|\partial_S[\mathcal F(t)z(t)]\|
\le2(r+1)\sqrt{2r+1}\,4^r r!\,\|z(t)\|.
\tag{4.2}
$$
这里 $D(t)f=0$，所以
$$
F_1(t)f=f,\qquad F_j(t)f=0\quad(j>1).
$$
其暗列整列为零。因而可以在暗面微积分基本定理中准确用
$-\mathcal F(t)e(t)-\mathcal F(t)k(t)$，而不是分别付两次 $\|f\|$。

结合 (2.3)，对 $r$ 元对集 $S$ 的整个暗分析列有
$$
\left(\sum_j
\left\|\left(\prod_{i\in S}P_{i,\sigma}^{\rm dark}\right)
F_ju_f\right\|^2\right)^{1/2}
\le
2(r+1)\sqrt{2r+1}\,\sigma^r r!
\prod_{i\in S}(\theta_i e^{\theta_i})\,\zeta_f.
$$
平方并作同一个非负 Tonelli，即得
$$
\boxed{
\sum_j
\left\langle\binom{N_\sigma}{r}F_ju_f,F_ju_f\right\rangle
\le
4(r+1)^2(2r+1)r!
(\sigma^2a_x)^r\zeta_f^2.
}
\tag{4.3}
$$
全部旗已共同求和；没有额外 $j,h,Q$ 因子。

对任意 $1\le r\le k$，也有准确全旗尾界
$$
\boxed{
\sum_j\|\mathbf1_{N_\sigma\ge k}F_ju_f\|^2
\le
4(r+1)^2(2r+1)
\frac{r!}{\binom kr}(\sigma^2a_x)^r\zeta_f^2.
}
\tag{4.4}
$$
先前明确的 floor 选择可将 $x$ 换成 $a_x^{-1}$ 使用；此处保 (4.4) 的全整数原式，不省略适用条件。任何附加输出孔带限制仍可取同一右边；不据此声称带自身范数替代已经付清。

## 5. 固定测试逼近原 $w$ 时的准确含义

对任意同一物理 $w$，由 $u_f=P_Uf$、$U=V_Q\ominus K_Q$，
$$
\|f-u_f\|
\le\|f-w\|+\|(I-P_U)w\|.
\tag{5.1}
$$
现在令 $w\in W$，并明确取[真正最小投影带权窗口](R271-appendix-true-minimal-projection-weighted-window.md) §1(1.4)、§4 的同一合法窗口
$$
m\ge10,\qquad d=2^m,\qquad
4d\le Q=Q(m)\le\exp\!\left(\frac{1601}{64}d^3\right).
\tag{5.2}
$$
该已付定理针对同一 $P_U=P_{V_{m,Q}}-P_{K_{m,Q}}$ 给
$$
\|P_Uw-P_{\mathrm{tail}(m)\le Q}w\|
\le2e^{-6d^4}\|w\|.
\tag{5.3}
$$
[强位并头同源稿](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md) §2(2.2) 保留的正是这个顶部，有限强位重分组没有更换 $P_U$。因而
$$
\begin{aligned}
\|(I-P_U)w\|
&\le\|P_{\mathrm{tail}(m)>Q}w\|+2e^{-6d^4}\|w\|\\
&\le\|(I-P_{\mathrm{tail}(m)=0})w\|+2e^{-6d^4}\|w\|
\longrightarrow0 .
\end{aligned}
\tag{5.4}
$$
最后的收敛在原共同物理 Hilbert 空间内成立：有限位支撑向量稠密，且在 $m$ 越过其支撑后尾真空投影准确固定它。两个投影均为收缩，故此强极限对 (5.2) 中任意 $Q(m)$ 一致；没有使用带增长因子的未知速率。小二次窗口 $R=d$、$h=2d$、$Q\asymp L_0h^2$ 在充分大 $m$ 时也满足 (5.2)。

由 (5.1)、(5.4)，对一次选定的固定有限物理 $f$，
$$
\boxed{\limsup_{m\to\infty}\zeta_f\le\sqrt2\,\|f-w\|.}
\tag{5.5}
$$
(1.4)、(3.3)、(4.3) 的系数因而也随固定测试对 $w$ 的逼近而变小。这使用的是同一个正交投影及其实际缺陷，没有任意选择另一条来源或新的 cut。

本文没有得到 $\zeta_f$ 的关于移动 $m,Q$ 的速率，也不将它乘增长的未知 MP/逆 Gram 费用。完整顺次返回仍须证明一个真实同源不等式，才能使用这里的缺陷因子；不能把 (5.5) 当作已付全返回或普通右费用。
