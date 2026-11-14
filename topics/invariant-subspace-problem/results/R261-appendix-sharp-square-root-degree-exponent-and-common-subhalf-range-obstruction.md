# R261 附录：平方根次数指数的实际锐性与共同低于半阶的像障碍

日期：2026-11-13（UTC）。作者：normal_states / Astra-ISP-1cf。

状态：已证明的中间结论；root已全文核验真实尾积、低头三角行、carry及闭图量词。本文给 R261 的次数指数 $1/2$ 一个实际锐性例子：对同一个非零规范正预解式无穷积，每个正平方根次数域都在其像内，但所有严格低于半阶的拉伸指数域的共同交仍不包含于其像中。这不是慢理想的正常湮灭见证，也不排除 R244 的见证专属配对。

## 1. 固定同一个非零无穷积

在原 Haar 空间中取
$$
b_j=\frac1{\sqrt{j+2}\log(j+2)}\qquad(j\ge0).
\tag{1.1}
$$
这里及下文的 $\log$ 均为自然对数。积分比较给
$$
\sum_{j\ge0}b_j^2
=\sum_{n\ge2}\frac1{n(\log n)^2}<\infty.
$$
令第 $j$ 个非负系数行只在位置 $j$ 非零：
$$
b^{(j)}=b_je_j,\qquad
P_n=\prod_{j=0}^{n-1}(I+b_jV_j)^{-1}.
\tag{1.2}
$$
累计行正是 (1.1)。R230 的实际无穷积分类遂给非零收缩强极限
$$
P=\operatorname*{SOT-lim}_{n\to\infty}P_n\in A',
$$
且 $P$ 单射并有既有收缩强主理想单位。

沿用已经发布的实际逆测试，记
$$
G_n=\prod_{j=0}^{n-1}(I+b_jV_j).
$$
对每个正指数次数空间 $H_\sigma=\operatorname{Dom}e^{\sigma\mathcal N}$，
$G_n$ 在严格分离的指数尺度之间按算子范数收敛到相容的 $G$，并有
$$
PGx=x,\qquad x\in H_\sigma,\quad\sigma>0.
\tag{1.3}
$$
所以这些输入上的 $G$ 是真正的 $P^{-1}$。

令 $\Pi_{\le q}$ 为全部 Walsh 次数至多 $q$ 的正交投影。

**第一结论。** 存在常数 $c>0$，使所有充分大的 $m$ 都有
$$
\boxed{
\|G|_{\operatorname{Ran}\Pi_{\le m}}\|
\ge\exp\!\left(c\frac{\sqrt m}{\log m}\right).
}
\tag{1.4}
$$
因此不能将 R261 的整个算子类中的平方根次数指数统一降为任何固定 $\beta<1/2$；对于本稿这同一个 $P$，即便常数允许依赖 $P$，也不存在
$$
\|G|_{\operatorname{Ran}\Pi_{\le m}}\|
\le C\exp(t(m+1)^\beta)
$$
对所有 $m$ 成立，其中 $C,t<\infty$、$\beta<1/2$。

更强的同一向量量词将在第 5 节证明。

## 2. 在物理全零头上，尾逆积是准确 Haar 乘积

令
$$
x_m=e_0^{\otimes m}\otimes\Omega_{\ge m}.
\tag{2.1}
$$
它是原 Haar 单位向量，并只依赖前 $m$ 位，所以
$x_m\in\operatorname{Ran}\Pi_{\le m}$。

固定 $m$。由于实际 $V_j$ 只作用于位 $j,j+1,\ldots$，$j\ge m$ 的因子保持 (2.1) 的低头。更重要的是实际恒等式
$$
V_F\Omega_{\ge m}=\chi_F
\qquad(F\subseteq\{m,m+1,\ldots\}\text{ 有限})
$$
给
$$
\prod_{j=m}^{n-1}(I+b_jV_j)\Omega_{\ge m}
=\prod_{j=m}^{n-1}(1+b_j\chi_j)
=:h_{m,n}.
\tag{2.2}
$$
本式是真实 carry 模型中的准确等式，没有在此把 $V_j$ 替换为纯算子。

Walsh 正交性给
$$
\|h_{m,n}\|^2=\prod_{j=m}^{n-1}(1+b_j^2).
$$
若 $n>k\ge m$，则
$$
\|h_{m,n}-h_{m,k}\|^2
=
\prod_{j=m}^{k-1}(1+b_j^2)
\left[\prod_{j=k}^{n-1}(1+b_j^2)-1\right].
\tag{2.3}
$$
因此 $b\in\ell^2$ 保证 $h_{m,n}$ 在原尾 $H$ 中收敛到 $h_m$，且
$$
\boxed{
1\le\|h_m\|^2=\prod_{j\ge m}(1+b_j^2)
\le e^{\|b_{\ge m}\|_2^2}.
}
\tag{2.4}
$$
特别该尾积不是零向量。

记固定有限个低位实际因子的乘积
$$
L_m=\prod_{j=0}^{m-1}(I+b_jV_j)\in\mathcal A.
$$
对 $n\ge m$，实际因子交换，(2.2) 给
$$
G_nx_m=L_m(e_0^{\otimes m}\otimes h_{m,n}).
$$
固定 $m$ 后 $L_m$ 有界；结合 (2.3) 和已有 $G_nx_m\to Gx_m$，得到
$$
\boxed{
Gx_m=L_m(e_0^{\otimes m}\otimes h_m).
}
\tag{2.5}
$$
这里只在每个固定 $m$ 先令 $n\to\infty$，没有将增长的低头范数带入一个未经控制的同时极限。

## 3. 真实低头的物理 00 行与全部 carry 误差

对 $j<m$，令 $N_j^{[m]}$ 为 R171 的实际有限头截断，定义
$$
V_j^{[m]}=(I-N_j^{[m]})(I+N_j^{[m]})^{-1}.
$$
真实递推和 Cayley 逆差给
$$
\|N_j-N_j^{[m]}\|
=\prod_{\ell=j}^{m-1}\eta_\ell,
$$
$$
\|V_j-V_j^{[m]}\|
\le18\prod_{\ell=j}^{m-1}\eta_\ell
\le18\varepsilon_m,\qquad
\varepsilon_m=e^{-77016^{m-1}}.
\tag{3.1}
$$
其中实际、截断的 $\|(I+N)^{-1}\|\le3$；$18$ 来自两倍 Cayley 逆差。并有
$$
\|V_j\|,\|V_j^{[m]}\|\le6.
$$

置
$$
\widetilde L_m=\prod_{j<m}(I+b_jV_j^{[m]})\otimes I_{\ge m},
\qquad
s_m=\sum_{j<m}b_j.
$$
对这两个有限乘积作望远镜，不需要实际和截断的混合因子交换，得到
$$
\begin{aligned}
\|L_m-\widetilde L_m\|
&\le18\varepsilon_m
\sum_{j<m}b_j\prod_{\substack{i<m\\i\ne j}}(1+6b_i)\\
&\le18\varepsilon_m s_m e^{6s_m}
=:r_m.
\end{aligned}
\tag{3.2}
$$
由 $s_m\le\|b\|_2\sqrt m$，
$$
r_m\longrightarrow0.
\tag{3.3}
$$
所以本稿虽允许低头逆积增长，全部实际 carry 仍有单独的双指数预算。

令 $B_m$ 为低 $m$ 位的真实有限加权前移。每个
$N_j^{[m]}=B_m^{2^j}/d_j$
在物理基中严格前移并且幂零。因此
$V_j^{[m]}$ 是 $B_m$ 的常数项为 $1$ 的有限多项式。
于是 $\widetilde L_m$ 的有限头矩阵为
$$
\Delta_m I+\text{严格前移矩阵},\qquad
\Delta_m=\prod_{j<m}(1+b_j).
$$
取物理全零头行，准确有
$$
\boxed{
(\langle e_0^{\otimes m}|\otimes I)
\widetilde L_m(e_0^{\otimes m}\otimes y)
=\Delta_m y\qquad(y\in H_{\ge m}).
}
\tag{3.4}
$$
这只是明确的有限三角矩阵行，不是把整个有限柱压缩当作代数同态。

由 (2.5)、(3.2)、(3.4)，
$$
\|Gx_m\|
\ge(\Delta_m-r_m)\|h_m\|.
$$
$\Delta_m\ge1$，$r_m\to0$，且 $\|h_m\|\ge1$，所以对充分大的 $m$，
$$
\boxed{
\|Gx_m\|\ge\frac12\prod_{j<m}(1+b_j).
}
\tag{3.5}
$$

## 4. 固定显式行给接近半阶的增长下界

对每个 $x\ge0$，
$$
\log(1+x)\ge x-\frac{x^2}{2}.
$$
故 (3.5) 给
$$
\log\|Gx_m\|
\ge s_m-\frac12\|b\|_2^2-\log2.
\tag{4.1}
$$
对于 (1.1) 的具体行，取后一半位置，
$$
s_m\ge
\sum_{\lceil m/2\rceil\le j<m}
\frac1{\sqrt{j+2}\log(j+2)}
\ge
\frac{m/2-1}{\sqrt{m+1}\log(m+1)}.
$$
因此存在 $c>0$，使充分大的 $m$ 有
$$
s_m-\frac12\|b\|_2^2-\log2
\ge c\frac{\sqrt m}{\log m}.
$$
结合 $\|x_m\|=1$ 和 $x_m\in\operatorname{Ran}\Pi_{\le m}$，便得到 (1.4)。

另一方面，R261 对每个固定 $\ell^2$ 总行已经证明上界
$$
\log\|G|_{\operatorname{Ran}\Pi_{\le m}}\|=o(\sqrt m).
$$
所以本稿的下界与零型完全相容；它只说明不能将指数的幂 $1/2$ 换成任意严格更小的固定幂，不声称 $\sqrt m/\log m$ 是该例的精确增长。

## 5. 同一个全部严格低于半阶的 Fréchet 域仍不在像内

定义
$$
\mathcal G_{<1/2}
=
\bigcap_{\substack{0<\beta<1/2\\t>0}}
\operatorname{Dom}e^{t(I+\mathcal N)^\beta}.
\tag{5.1}
$$
可以等价取可数共尾权
$$
\beta_n=\frac{n}{2(n+1)},\qquad t_n=n,\qquad n\ge1.
$$
其交以这些加权范数成为 Fréchet 空间：每个权是闭的 Walsh 对角算子，逐个使用闭性即可证明完备，且该空间连续嵌入 $H$。

**第二结论。**
$$
\boxed{
\mathcal G_{<1/2}\not\subseteq\operatorname{Ran}P.
}
\tag{5.2}
$$

证明如下。令
$$
a_m=\|Gx_m\|,\qquad y_m=x_m/a_m.
$$
每个 $x_m$ 是有限柱向量，所以 $y_m\in\mathcal G_{<1/2}$；
由 (1.3)，它也在 $\operatorname{Ran}P$ 中，并且
$$
\|P^{-1}y_m\|=1.
\tag{5.3}
$$
对于任意固定 $0<\beta<1/2$、$t>0$，
$$
\|y_m\|_{\beta,t}
\le
\exp\!\left(t(m+1)^\beta-c\frac{\sqrt m}{\log m}\right)
\longrightarrow0.
\tag{5.4}
$$
这里是同一个序列对全部固定权收敛，不按 $\beta,t$ 重选向量。

若反设 $\mathcal G_{<1/2}\subseteq\operatorname{Ran}P$，由于 $P$ 有界单射，
$$
P^{-1}:\mathcal G_{<1/2}\to H
$$
处处定义且图闭。Fréchet 到 Banach 的闭图定理迫它连续；
(5.4) 与 (5.3) 矛盾，证明 (5.2)。

因此存在同一个向量
$$
v\in\mathcal G_{<1/2}\setminus\operatorname{Ran}P.
\tag{5.5}
$$
它同时具有全部固定 $t>0$、$\beta<1/2$ 的拉伸次数矩。
特别，每个单独的这些加权空间也不包含于 $\operatorname{Ran}P$。

与之同时，R261 仍给这个完全相同的 $P$：
$$
\operatorname{Dom}e^{\epsilon\sqrt{I+\mathcal N}}
\subseteq\operatorname{Ran}P
\qquad\text{对每个 }\epsilon>0.
$$
所以 (5.5) 的向量不具有任何一个正平方根次数矩。
这里的 $v$ 由闭图矛盾得到存在性，未给闭式表达。

## 6. 与正常见证问题的边界

本例精确显示：R261 的零型允许每个任意小的正平方根次数权，但不能只凭总行平方可和就覆盖整个严格低于半阶的共同光滑域。整个构造保留真实尾积、真实低头 carry 及实际有界无穷积。

本文没有构造慢主理想的正常湮灭泛函。由 (5.5) 得到的向量只是一个值域见证；既不自动循环，也不自动满足任何湮灭矩方程。R244 仍只要求为一个具有额外湮灭方程的有限元组找到指定配对域，本稿不把上述普遍像障碍当作该专属问题的反例。
