# 同一母提升的正向 gauge 联合预算与真实低零源核反馈

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：完整证明。本文在原 c26 母提升的每一步修复中直接插入同一个有限多项式 \(p_m\)，支付 \(p_m(B)(\Lambda-I)\) 的范数。由此得到原 \(w\in W\) 对真实低零源核的正向 gauge 反馈界。未支付整个 joined 源恢复、反向最小投影反馈或高孔自配对。

## 1. 原同一来源与目标

取原 \(N/Y\) 模型，\(m\ge10,d=2^m\)，并沿用
\[
M=\ker T,\qquad N=\overline{BM},\qquad W=M\ominus N.
\]
置
\[
\rho_m=e^{-25d^3/2},\qquad
p_m(z)=\sum_{k<d}p_{m,k}z^k,\qquad
p_{m,0}=d_0,\qquad |p_{m,k}|\le2d_0\rho_m^{-k},
\]
其中 \(p_m\) 是 \((F_m(z)/z)^{-1}\) 的 \(<d\) Taylor 截断。
真正有限头 gauge 为
\[
G_{1,m}=p_m(B_m)\otimes I.
\]
[全局 carry 锚](2026-11-15-global-weighted-shift-to-true-head-gauge-carry-and-w-anchor-789f-next.md)
已经证明
\[
\|p_m(B)-G_{1,m}\|\le\eta_m:=e^{-80d^4}.
\tag{1.1}
\]

令
\[
K_{m,Q}=\ker L_m\cap\mathcal H_{\le Q}^{(m)},
\qquad 1\le Q\le e^{26d^3}.
\]
使用 [c26 原证明 §§4–6](2026-11-14-joint-positive-carry-budget-and-twenty-six-window-actual-sources-789f-next.md)
中同一个线性母提升
\[
\Lambda_{m,Q}:K_{m,Q}\longrightarrow N.
\]
本稿证明
\[
\boxed{
\|p_m(B)(\Lambda_{m,Q}-I)k\|
\le8e^{-2d^4}\|k\|
\quad(k\in K_{m,Q}).
}
\tag{1.2}
\]
特别，置
\[
\theta_m=8e^{-2d^4}+\eta_m,
\]
则
\[
\boxed{
\|p_m(B)\Lambda_{m,Q}k-G_{1,m}k\|
\le\theta_m\|k\|.
}
\tag{1.3}
\]
这里没有先估 \(\|\Lambda-I\|\)，再乘 \(\|p_m(B)\|\) 或
\(\|G_{1,m}\|\)。

## 2. c26 一步修复的原域与交换关系

在第 \(p-m\) 步，令
\[
p\ge m,\quad z=2^p,\quad Q_p=Q+z-d,
\]
\[
k_p\in\ker L_p\cap\mathcal H_{\le Q_p}^{(p)},
\qquad
A_{p+1}=
\begin{pmatrix}A_p&b_pI+C_p\\0&A_p\end{pmatrix},
\qquad
K_p=L_{p+1}-L_p=
\begin{pmatrix}0&C_p\\0&0\end{pmatrix}.
\]
原一步修复准确为
\[
c_p=\sum_{j<z}(-A_{p+1})^jR'_{j+1}K_pk_p,
\qquad
k_{p+1}=k_p-c_p.
\tag{2.1}
\]
这里 \(R'_t\) 是原有限孔输入上、只作用于新尾 \(D_{p+1}\) 的相容右逆，
其参数可取
\[
R_0\le512(Q+5z)^2\le\mathcal R_p,
\qquad
\mathcal R_p=\exp\!\left(\frac{417}{8}z^3\right).
\]
原证明已给
\[
L_{p+1}c_p=K_pk_p,\qquad
\|c_p\|\le e^{-2z^4}\|k_p\|,
\qquad \|k_p\|\le2\|k_m\|.
\tag{2.2}
\]
孔数至多增加 \(z\)，后续仍在同一个原序列的域内。

记
\[
P_p=p_m(B_p),\qquad P_{p+1}=p_m(B_{p+1}),
\]
在更高尾位按恒等延拓。这里下标 \(p\) 只改变代入的原有限后移；
标量多项式始终是初始 \(m\) 的同一个 \(p_m\)。

由于 \(A_{p+1}=F_{p+1}(B_{p+1})\)，
\(P_{p+1}\) 与 \(A_{p+1}\) 交换；它也与全部纯尾 \(R'_t\)
及 \(D_{p+1}\) 交换。
\(K_pk_p\) 落在新位 \(0\) 的物理头块，在该块
\(P_{p+1}\) 恰为 \(P_p\)，而 \(A_{p+1}\) 恰为 \(A_p\)。
因此
\[
P_{p+1}c_p
=\sum_{j<z}(-A_{p+1})^jR'_{j+1}P_{p+1}K_pk_p.
\tag{2.3}
\]
原有限孔域和所有新位支撑均保持，没有把 \(R'_t\) 延成全空间有界右逆。

又因为 \(K_pE_p=0\)，原真实核关系给
\[
D_{p+1}^{\ell}P_{p+1}K_pk_p
=P_{p+1}K_p(-A_p)^\ell k_p.
\tag{2.4}
\]
这是同一个输入的全部真实导数，不能换成另一个 \(P_pk_p\) 的环境范数估计。

## 3. 将 \(p_m\) 插入原联合正系数跨块

定义非负系数多项式
\[
h_m(s)=\sum_{k<d}|p_{m,k}|s^k
\]
和 c26 的同一个正系数函数
\[
g_p(s)=\sum_{i<p}b_i\frac{s^{2^i}}{d_i-s^{2^i}}.
\]
在真实 \(B_{p+1}\) 上，
\[
g_p(B_{p+1})=
\begin{pmatrix}\mathsf A_p&\mathsf C_p\\0&\mathsf A_p\end{pmatrix},
\qquad |A_p|\le\mathsf A_p,\quad |C_p|\le\mathsf C_p
\]
均按原物理矩阵条目理解。
所有这些矩阵的支配条目非负。

对 \(j,\ell<z\)，原指定的一个跨块项被完整非负跨块和支配：
\[
\boxed{
|A_p^jP_pC_pA_p^\ell|
\le
[\,h_m(B_{p+1})g_p(B_{p+1})^{j+\ell+1}\,]_{01}.
}
\tag{3.1}
\]
例如将 \(h_m\) 的对角块放在指定的 \(C_p\) 左侧，就得到左边的支配项；
完整右边还包含其他非负的跨块位置。
这里不是将两个互不交换的物理块随意交换，而是使用同一
\(B_{p+1}\) 标量函数的完整乘积。

把 (2.3)–(2.4) 放入原相容右逆估计，再用
\(1/(j+1)!\le1/j!\)，得到
\[
\begin{aligned}
\|P_{p+1}c_p\|
&\le
R_0\sum_{j,\ell<z}
\frac{R_0^{j+\ell}}{(j+1)!\ell!}
 \|A_p^jP_pC_pA_p^\ell\|\,\|k_p\|\\
&\le
\sum_{u,v=0}^{z-1}
\left[
\mathcal R_p h_m(B_{p+1})g_p(B_{p+1})
e^{2\mathcal R_p g_p(B_{p+1})}
\right]_{u,z+v}\,\|k_p\|.
\end{aligned}
\tag{3.2}
\]
全部 \(h_m\) 系数放在原同一跨块内；没有另乘独立的头幂和。

取原正圆点
\[
\zeta_p=\frac{d_0}{4\mathcal R_p}.
\]
因为 \(p\ge m\)，
\[
\frac{\zeta_p}{\rho_m}
=\frac{d_0}{4}
\exp\!\left(-\frac{417}{8}z^3+\frac{25}{2}d^3\right)<\frac12.
\]
所以
\[
h_m(\zeta_p)
\le\frac{2d_0}{1-\zeta_p/\rho_m}\le4d_0<1.
\tag{3.3}
\]
原 c26 已逐式证明
\[
\mathcal R_pg_p(\zeta_p)
e^{2\mathcal R_pg_p(\zeta_p)}\le e/2.
\]
乘 (3.3) 后仍不超过同一个 \(e/2\)。
因此 c26 §3 中原
\[
\frac{d_pW_v}{W_u}\zeta_p^{-(z+v-u)}
\]
的全部权、最高次数 \(2z-1\)、真实最坏位置 \(u=0,v=z-1\)
以及 \(z^2\) 条目计数一字不变。其原 \(-2z^4\) 指数预算给
\[
\boxed{\|p_m(B_{p+1})c_p\|
\le e^{-2z^4}\|k_p\|.}
\tag{3.4}
\]
这是真正同源带 gauge 的修复费用。

## 4. 返回全局同一个 \(p_m(B)\)，并求和

全局 carry 锚的逐幂证明对任意更大头同样适用。
因为 \(\deg p_m<d\le2^{p+1}\)，
\[
\|p_m(B)-p_m(B_{p+1})\otimes I\|
\le2dd_0\,\alpha_{p+1}\rho_m^{-(d-1)}
\le\eta_m<1.
\tag{4.1}
\]
这里用原 \(\alpha_j\) 递减，不改变初始的 \(\rho_m\) 或 \(p_m\)。

由 (2.2)、(3.4)、(4.1)，
\[
\|p_m(B)c_p\|
\le(1+\eta_m)e^{-2z^4}\|k_p\|
\le4e^{-2z^4}\|k_m\|.
\]
而同一个母提升满足
\[
\Lambda_{m,Q}k-k=-\sum_{p\ge m}c_p.
\]
右边在原物理 Hilbert 空间范数收敛；上式还证明其
\(p_m(B)\) 像的级数绝对收敛。于是
\[
\|p_m(B)(\Lambda_{m,Q}-I)k\|
\le4\sum_{p\ge m}e^{-2\cdot16^p}\|k\|
\le8e^{-2d^4}\|k\|,
\]
即 (1.2)。再加 (1.1) 即得 (1.3)。
只使用了原母提升，没有另选一个更方便的同源修复。

## 5. 对真实 \(W\) 的低零源核反馈

原 \(\Lambda_{m,Q}k\in N\)，且 \(N\) 对 \(B\) 不变，所以
\(p_m(B)\Lambda_{m,Q}k\in N\)。
若 \(w\in W\)，(1.3) 给
\[
|\langle w,G_{1,m}k\rangle|
\le\theta_m\|w\|\,\|k\|.
\]
对 \(K_{m,Q}\) 中所有单位向量取上确界，
\[
\boxed{
\|P_{K_{m,Q}}G_{1,m}^*w\|
\le\theta_m\|w\|,\qquad
\theta_m=8e^{-2d^4}+e^{-80d^4}\le e^{-d^4}.
}
\tag{5.1}
\]
等价地，
\[
\|P_WG_{1,m}P_{K_{m,Q}}\|\le\theta_m.
\]
这是原整个低零源核的一个真实方向，不仅一个指定 primitive 列。

本稿没有给反方向
\(\|P_{K_{m,Q}}G_{1,m}w\|\)，也不将
\(G_{1,m}\) 与正交投影互换。
特别，对真正 \(v_Q=P_{V_Q}w\)，构造性修复的带权小量
不能删除 \(P_{V_Q}G_{1,m}(I-P_{V_Q})\) 的反馈；
从 \(v_Q\) 再取左最小者时也须保相应非自伴交叉项。
原高孔自配对、普通右费和完整 joined 源恢复仍未支付，
因此本稿不声称 \(N=M\) 或普通 ISP 已完成。
