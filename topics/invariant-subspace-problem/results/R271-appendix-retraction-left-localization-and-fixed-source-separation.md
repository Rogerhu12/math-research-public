# R271 附录：回缩源的左前驱局域化与固定实际来源的严格分离

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_2220。

状态：**已证明。** [原尾强位-boson回缩](R271-appendix-original-tail-strong-bit-boson-retraction-and-same-source-high-schur-bound.md)支付了同源三个真正最小费用。本稿进一步说明：当其失真趋于一且暗前缀至少一孔时，整个嵌入模型源类的左最小前驱与每个固定物理向量渐近正交，因而不能在左费用中逼近一个固定非零边界缺陷。对原全部 primitive 源有更强的准确式：左最小前驱就只在源孔层，完全不需要回缩近等距假设。

这些是原物理 Hilbert 空间中的来源限制。它们不否定模型的全源二次型测试，也不由此排除一般实际来源、证明 $N=M$ 或解决普通 ISP。

## 1. 同源可行前驱与真正最小前驱

保留回缩稿的全部参数
\[
m\ge5,\quad d=2^m,\quad n=q-s,\quad
J=m+k+2n,\quad
\epsilon=\frac{4(s+d)^2}{J+1}<1,
\]
\[
R=e^{2/(m+k+1)},\qquad
\kappa=(1-\epsilon)^{-1/2}.
\]
记 $\mathsf B$ 为该稿的右截面，$\mathsf T$ 为回缩。它们保持原头 $A_m$、边界方程和所有使用的核旗，且
\[
\mathsf T\mathsf B=I,\qquad
\|\mathsf T\|\le R,\qquad\|\mathsf B\|\le\kappa.
\tag{1.1}
\]
模型左孔层为 $0,\ldots,s$；$\mathsf B$ 将模型第 $j$ 层送到原第 $n+j$ 层。因此其左侧直和 $\mathsf B_-$ 的像准确支持在原尾孔 $[n,q]$。

给定任意模型源 $\widehat r$，始终使用同一个原源
\[
r=\mathsf B_s\widehat r.
\]
令
\[
\widehat v=\widehat E_s^\dagger\widehat r,\qquad
v=E_q^\dagger r,\qquad v_0=\mathsf B_-\widehat v.
\tag{1.2}
\]
$v_0$ 是原源 $r$ 的一个真实可行左前驱；$v$ 是该源的真正最小前驱。原左零源核是闭子空间，所以
\[
v_0-v\in\ker E_q,\qquad v\perp\ker E_q.
\]
因而有完整 Pythagoras
\[
\boxed{\|v_0-v\|^2=\|v_0\|^2-\|v\|^2.}
\tag{1.3}
\]
这一步不要求非酉截面与任何正交投影交换。

回缩稿给 $\|\widehat v\|\le R\|v\|$。与 $\|\mathsf B_-\|\le\kappa$ 合并，(1.3) 给
\[
\boxed{\|v-v_0\|^2\le
(\kappa^2R^2-1)\|v\|^2.}
\tag{1.4}
\]
置
\[
\omega^2=\kappa^2R^2-1
=\frac{e^{4/(m+k+1)}}{1-4(s+d)^2/(J+1)}-1.
\tag{1.5}
\]
这是由两个真正最小费直接支付的相对误差，没有混入未付的 $\lambda_{\rm flat}$。

## 2. 对整个模型源类一致的物理低孔界

若 $n\ge1$，令
\[
Q_{m,n}=P_{\ge n}^{(m)}
\]
为原物理尾孔投影。由 $v_0=Q_{m,n}v_0$ 与 (1.4)，
\[
\boxed{\|(I-Q_{m,n})E_q^\dagger\mathsf B_s\widehat r\|
\le\omega\,\|E_q^\dagger\mathsf B_s\widehat r\|.}
\tag{2.1}
\]
它对所有模型源同时成立，与源系数大小、头自由度及其选择方式无关。

定义原物理左像
\[
\mathcal U_{m,k,s,q}
=\overline{\{E_q^\dagger\mathsf B_s\widehat r:
                    \widehat r\in\mathsf R_s\}}.
\tag{2.2}
\]
每组固定有限参数下模型源本身有限维；写闭包也使以下论证无需额外使用有限维性。(2.1) 由连续性对 $\mathcal U_{m,k,s,q}$ 全部向量成立。

对任意固定物理向量 $w$ 和单位 $v\in\mathcal U_{m,k,s,q}$，
\[
\begin{aligned}
|\langle w,v\rangle|
&\le\|(I-Q_{m,n})w\|\,\|(I-Q_{m,n})v\|
+\|Q_{m,n}w\|\,\|Q_{m,n}v\|\\
&\le\omega\|w\|+\|Q_{m,n}w\|.
\end{aligned}
\]
因此
\[
\boxed{\|P_{\mathcal U_{m,k,s,q}}w\|
\le\min\{\|w\|,\ \omega\|w\|+\|Q_{m,n}w\|\}.}
\tag{2.3}
\]
由正交投影的距离公式，得到量化分离
\[
\boxed{\operatorname{dist}(w,\mathcal U_{m,k,s,q})^2
\ge\left[\|w\|^2-
(\omega\|w\|+\|Q_{m,n}w\|)^2\right]_+.}
\tag{2.4}
\]

## 3. 暗前缀不必趋于无穷：正一孔就足以分离固定向量

考虑任意一族原合法参数，满足
\[
m\longrightarrow\infty,\qquad
n_m=q_m-s_m\ge1,\qquad
\epsilon_m\longrightarrow0.
\tag{3.1}
\]
因为 $k_m\ge0$，$R_m\to1$；故 (1.5) 给 $\omega_m\to0$。

对每个固定 $w\in L^2(\mathbb Z_2)$，有
\[
\boxed{Q_{m,n_m}w\longrightarrow0.}
\tag{3.2}
\]
证明：原有限位柱函数在物理 Hilbert 空间稠密。若柱函数只依赖前 $M$ 位，则对 $m\ge M$ 它的第 $m$ 位之后完全为尾真空。因 $n_m\ge1$，$Q_{m,n_m}$ 消去该柱函数。全部 $Q_{m,n_m}$ 都是范数一投影，稠密逼近即给 (3.2)。

这里无需 $n_m\to\infty$。即使 $n_m$ 恒为一，也已由移动的尾起点 $m\to\infty$ 得到 (3.2)。

于是 (2.3)–(2.4) 给
\[
\boxed{P_{\mathcal U_m}\longrightarrow0\ \text{强算子拓扑},\qquad
\operatorname{dist}(w,\mathcal U_m)\longrightarrow\|w\|.}
\tag{3.3}
\]
等价地，$\mathcal U_m$ 中任意范数一致有界的向量族都弱趋于零；它不能强趋于一个固定非零 $w$。

## 4. 对真实边界来源和已经支付的规范化的含义

设 $r_m$ 是同一个原合法孔层 $q_m$ 上的实际源，且
\[
u_m=E_{q_m}^\dagger r_m\longrightarrow w\ne0
\]
为强收敛。模型参数满足 (3.1)。最小逆线性，所以
\[
\inf_{\widehat r_m}
\mu_{m,q_m}(r_m-\mathsf B_{s_m}\widehat r_m)
=\operatorname{dist}(u_m,\mathcal U_m).
\]
距离到闭子空间是 1-Lipschitz；由 (3.3)，
\[
\boxed{\inf_{\widehat r_m}
\mu_{m,q_m}(r_m-\mathsf B_{s_m}\widehat r_m)
\longrightarrow\|w\|.}
\tag{4.1}
\]
这里允许每个模型源任意选择，也允许其普通源范数很大；结论仍由整个左像的统一角度给出。

因此这些嵌入模型源不仅没有被证明来自固定 $W$，而且在显示的小失真区间内，已经被证明不能在左费中逼近任何固定非零实际来源。若先作一个已支付的修正 $a_m$，满足
\[
\mu_{m,q_m}(a_m)\to0,
\]
则 $E_{q_m}^\dagger(r_m-a_m)\to w$，(4.1) 原样成立。特别，[负源图与联合旗](R271-appendix-negative-source-flow-joint-paid-flag-and-actual-window-reduction.md)中保同一 $w$ 的小左费规范化不会消除本分离。

本节不需要假设模型源已经满足某个两费用图，也没有从模型的全源费用比较倒推出实际 $W$ 来源。

## 5. 原全部 primitive 源的左最小前驱准确集中于顶部

还有一个不需要 (1.1)–(1.5) 的更强特例。令
\[
A_0=A_m|_{e_0^\perp}:e_0^\perp\longrightarrow\operatorname{Ran}A_m.
\]
它是原有限头同构。若原源的每个尾头分量都 primitive，
\[
r\in\operatorname{Ran}A_m\otimes K_q,\qquad
K_q=\ker D_m\cap\mathcal H_q,
\]
则
\[
\boxed{E_q^\dagger r=(A_0^{-1}\otimes I)r
\quad\text{放在唯一孔层 }q.}
\tag{5.1}
\]
证明：记右边为 $u$。由于 $Du=0$，单层向量 $u$ 满足所有低输出方程，顶源为 $Au=r$，所以可行。任一其他可行左向量 $v$ 的顶部满足
\[
v_q=u+e_0h,
\]
因为 $\ker A_m=\mathbb C e_0$。$u$ 与 $e_0h$ 的头位置正交，其他孔层又与顶部正交。因此
\[
\|v\|^2=\|u\|^2+\|h\|^2+\sum_{\ell<q}\|v_\ell\|^2
\ge\|u\|^2,
\]
等号恰在 $v=u$ 成立，证明 (5.1)。

这也与[准确源流像稿](R271-appendix-exact-left-source-flow-range-and-minimal-upward-extension.md)的
$\ker T_q=\bigoplus_{i=0}^{d-2}e_iK_q$ 一致：primitive 源的真正最小前驱没有任何更低的物理层。

特别，[两强位原头二次型稿](R271-appendix-two-strong-bit-boson-head-quadratics-and-original-source-transfer.md)的明确原源
\[
r(u)=A_m u\otimes f_q,\qquad
u\perp\ker A_m,\quad f_q\in K_q,\quad\|f_q\|=1
\]
满足准确等式
\[
\boxed{E_q^\dagger r(u)=u\otimes f_q,\qquad
\mu(r(u))^2=\|u\|^2.}
\tag{5.2}
\]
该稿的双向费用夹界仍正确，(5.2) 只把其中左费进一步算成准确值；完整右费与裸费的两头二次型并未因此被计算出来或比较完成。

## 6. Primitive 来源的严格分离没有失真条件

设 $m\to\infty$ 且 $q_m\ge1$。对原全部 primitive 源的左像，(5.1) 给
\[
\mathcal U_m^{\rm prim}
\subseteq P_{\ge1}^{(m)}H.
\]
对任何固定 $w$，柱函数证明仍给
\[
\|P_{\mathcal U_m^{\rm prim}}w\|
\le\|P_{\ge1}^{(m)}w\|\to0.
\tag{6.1}
\]
所以
\[
\boxed{\operatorname{dist}(w,\mathcal U_m^{\rm prim})
\longrightarrow\|w\|.}
\tag{6.2}
\]
它不要求 $\epsilon_m\to0$、不限制强位数，也不要求 $q_m-s_m\to\infty$。合法窗口 $q_m\ge4d_m$ 当然满足正孔假设。

因此任何仅在一个原 primitive 尾向量上张量任意原头系数的测试源，都不能给保固定非零左极限的实际缺陷族。它仍可有效测试全源算子序或暴露环境费用增长；不能把这些测试与固定来源混同。

对一般回缩族，$n_m=0$ 或失真不趋于一时，§§2–4 的渐近分离不自动成立；对非 primitive、非该模型像的一般实际源，本稿也没有给分离或费用上界。原两图余源比较、完整高返回、无权 $N=M$ 与普通复 Hilbert ISP 继续开放。
