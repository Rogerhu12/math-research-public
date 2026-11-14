# 尾间隙的实际预解预算与非弱 ℓ¹ 长平台近共振族

日期：2026-11-13（UTC）。作者：central_review / Astra-ISP-0c017065。
状态：完整证明的新具体族，接续[任意复 ℓ² 主行的近共振预解准则与实数偏离阶](2026-11-13-general-ell2-near-resonance-resolvent-criterion-central-review.md)。本稿只建立新的充分条件，不声称关闭一般慢辅助或普通 ISP。

## 1. 主结论

取原模型中的
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
w=b_*+\sum_{j\ge0}b_j\chi_j,\qquad a,b\in\ell^2(\mathbb C),
$$
其中 $a$ 有无限非零支撑，非零幅度的非增重排为 $\rho_n$。
固定实数 $\kappa>2$，要求
$$
|c_j|\le C_0|a_j|^\kappa\quad(j\ge0),
\tag{1.1}
$$
并对充分大的物理位 $j$、$a_j\ne0$ 要求
$$
|c_j|\ge c_0|a_j|^\kappa,\qquad c_0>0.
\tag{1.2}
$$
特别 $a_j=0$ 时 $c_j=0$。这里只比较绝对值，实数 $\kappa$ 不涉及复数幂的分支。

**定理 1（尾间隙准则）。** 若沿无穷整数子序列 $N$，
$$
L_N:=1+\log^+(\rho_N^{-1})=O(N),
\tag{1.3}
$$
$$
\boxed{
\sum_{n>N}\rho_n^\kappa
=o\!\left(\rho_N^{\,2\kappa-2}\right),
}
\tag{1.4}
$$
则
$$
\boxed{
\left[u^2+\sum_j(2a_j^2+c_j)(\chi_j-1)\right]e^w
\text{ 非零且对原实际 }A\text{ 循环}.
}
\tag{1.5}
$$
主行不要求属于 $\ell^1$ 或弱 $\ell^1$；允许任意相位和物理排列。
偏离系数 $c_j$ 也无需与 $a_j$ 同相。
定理通过实际算子预解式的范数估计证明，不将幅度排序变为物理位重排。

下文先给一个对任意有限物理集合统一的指数预算，再构造真正的全方向 Laplace 预解式，最后给出满足 (1.3)–(1.4) 而不属于既有三类主行的明确例子。

## 2. 实际保序上界与任意有限头的统一预算

令
$$
t_j=e^{-2b_j},\qquad R_j=V(t_jN_j),\qquad
Y=\sum_jc_j(R_j-I).
\tag{2.1}
$$
由于 $\kappa>2$ 和 $a\in\ell^2$，有 $c\in\ell^1$；
全部 (2.1) 的级数在原物理位上绝对算子范数收敛。
设
$$
L=\max(1,\sup_j|t_j|),\qquad
W(z)=\frac{2Lz}{1-Lz},\qquad
M_c=\sum_j|c_j|W(N_j).
\tag{2.2}
$$
$W(N_j)$ 由真正有理演算定义。
也可用绝对收敛的非负系数级数
$2\sum_{k\ge1}L^kN_j^k$ 定义；其相等性来自实际准幂零预解式。
高位的 $N_j^2=\eta_jN_{j+1}$ 与有限低位逐个处理给
$$
C_W:=\sup_j\|W(N_j)\|<\infty.
\tag{2.3}
$$

原逐点函数锥下，全部 $N_j$ 保持非负函数。
因而
$$
|(R_j-I)f|\le W(N_j)|f|,\qquad
|Y^nf|\le M_c^n|f|.
\tag{2.4}
$$
对任意复数 $\lambda$，真实指数范数收敛给
$$
|e^{\lambda Y}f|\le e^{|\lambda|M_c}|f|,
\qquad
\|e^{\lambda Y}\|\le\|e^{|\lambda|M_c}\|.
\tag{2.5}
$$
这使用保序算子及函数绝对值，并不假设 $N_j$ 或 $Y$ 为 Hilbert 意义的自伴正算子。

**引理 2.1（有限任意物理头）。** 对任意有限物理位集 $H$，令
$$
M_H=\sum_{j\in H}|c_j|W(N_j).
$$
存在只依赖固定行 $c$ 与指数权 $b$ 的常数 $K,C,C_1>0$，使
$$
\boxed{
\|e^{sM_H}\|
\le K\exp\!\left[C(\log(2+s))^{4/3}\right]
\prod_{j\in H}(1+C_1s|c_j|)
\quad(s\ge0).
}
\tag{2.6}
$$
常数与 $H$ 的大小及最大物理位均无关。

**证明。** 因
$$
W(N_j)^2
=4L^2N_j^2(I-LN_j)^{-2}
$$
且真实逆一致有界，有
$$
\|W(N_j)^2\|\le C_2\eta_j,\qquad
\|W(N_j)\|\le C_W.
$$
偶奇幂展开于是给
$$
\|e^{sqW(N_j)}\|
\le(1+C_Wsq)\exp(C_3sq\sqrt{\eta_j})
\quad(s,q\ge0).
\tag{2.7}
$$
有限低位只扩大固定常数，未将其忽略。

令 $h=h(s)\ge1$ 是满足
$$
385\,16^h\ge2\log(2+s)
\tag{2.8}
$$
的最小整数。这里 $\eta_j$ 是实际进位系数
$
\eta_j=\frac{d_{j+1}}{d_j^2}
=\exp\!\left[-1400\,16^j+630\,8^j-300\,2^j\right]
\le e^{-385\,16^j},
$
其中 $d_j=W_{2^j}$；最后一项只是统一粗上界，并非实际系数的等式。
因此
$$
s\sum_{j\ge h}|c_j|\sqrt{\eta_j}
\le\|c\|_1.
\tag{2.9}
$$
对 $H\cap[h,\infty)$ 使用 (2.7)，这些交换因子的 carry 总成本由 (2.9) 统一控制。

剩余是一个真正物理低头，而不是按幅度截出的未知巨大头。
由实际有限除法
$$
N_j=A\,\frac{A^{2^j-1}}{W_{2^j}},
$$
以及已核实的有限头范数界，准确有
$$
M_{H\cap[0,h)}
=A U_{H,h},\qquad
\|U_{H,h}\|\le C_4\|c\|_1e^{125\,16^{h-1}}.
\tag{2.10}
$$
这里包含的 $(I-LN_j)^{-1}$ 都是真实一致有界逆。
所有指数 $2^j-1$ 非负，所以 (2.10) 是有限有界算子和，不是对一般尾作形式除 $A$。

[R109](../results/R109-invariant-restriction-exact-quartic-type.md) 的实际幂界允许固定 $d>0,K_A$ 使
$$
\|A^n\|\le K_Ae^{-dn^4}.
$$
于是对任意固定有界交换 $U$，
$$
\begin{aligned}
\|e^{sAU}\|
&\le K_A\sum_{n\ge0}
 \frac{(s\|U\|)^n}{n!}e^{-dn^4}\\
&\le K'_A\exp\!\left[
 C_A(\log(2+s\|U\|))^{4/3}
\right].
\end{aligned}
\tag{2.11}
$$
最后一步由
$n\log^+(s\|U\|)-(d/2)n^4
\le C_A(\log(2+s\|U\|))^{4/3}$
与剩余可和四次尾得到。

由 (2.8) 的最小性，当 $h\ge2$，
$385\,16^{h-1}<2\log(2+s)$；
$h=1$ 时对应界由固定常数吸收。
因此
$$
\log(2+s\|U_{H,h}\|)
\le C_5\log(2+s).
\tag{2.12}
$$
结合 (2.7)–(2.12)，先得到 (2.6) 中只含
$H\cap[h,\infty)$ 的乘积。
把其扩为全部 $H$ 只增加大于等于1的标量因子，故得到 (2.6)。
全证明只移动标量和及交换算子因子，没有对原物理算子作排列。证毕。

## 3. 半径上真实预解式的头尾预算

下面的引理独立于主行的具体比较关系。

**引理 3.1（有限头加小范数尾）。**
设 $H$ 为含 $N$ 个物理位的有限集，$0<r\le1$，且
$$
\left\|\sum_{j\notin H}|c_j|W(N_j)\right\|\le r/4.
\tag{3.1}
$$
记 $\ell_r=1+\log(r^{-1})$。
则对每个 $|z|=r$，实际 $z-Y$ 可逆，并且
$$
\boxed{
\log^+\|z(z-Y)^{-1}\|
\le C\left[
1+N\log(N+1)+N\ell_r+\ell_r^{4/3}
\right].
}
\tag{3.2}
$$
常数对 $H,N,r$ 统一。

**证明。** 写 $M_c=M_H+M_{H^c}$。两项交换，由 (2.5)、(2.6)、(3.1)，对 $t\ge0$，
$$
\begin{aligned}
\|e^{tY/z}\|
&\le\|e^{(t/r)M_c}\|\\
&\le
e^{t/4}K
\exp\!\left[C(\log(2+t/r))^{4/3}\right]
(1+C_6t/r)^N.
\end{aligned}
\tag{3.3}
$$
最后一步只用 $|c_j|\le\|c\|_\infty$，即把有限头的标量乘积界为 $N$ 次多项式。

因为 $r\le1$，
$$
\log(2+t/r)\le C+\ell_r+\log(1+t),
$$
$$
(1+C_6t/r)^N
\le e^{C_7N+N\ell_r}(1+t)^N.
\tag{3.4}
$$
对固定常数 $C_8$，存在 $C_9$ 使
$$
C_8(\log(1+t))^{4/3}\le t/4+C_9
\quad(t\ge0).
\tag{3.5}
$$
因此下面的积分在真实算子范数中绝对收敛：
$$
Z_z:=\int_0^\infty e^{-t}e^{tY/z}\,dt.
\tag{3.6}
$$
而且
$$
\begin{aligned}
\|Z_z\|
&\le K_1e^{C_7N+N\ell_r+C_{10}\ell_r^{4/3}}
\int_0^\infty e^{-t/2}(1+t)^N\,dt\\
&\le K_1e^{C_7N+N\ell_r+C_{10}\ell_r^{4/3}}
\,2^{N+1}e^{1/2}N!.
\end{aligned}
\tag{3.7}
$$
这里最后一个积分由替换 $v=(1+t)/2$ 直接界得。

(3.3) 还给 $e^{-t}e^{tY/z}\to0$ 于范数。
对实际指数求导并在 (3.6) 中积分，得到
$$
(I-Y/z)Z_z=Z_z(I-Y/z)=I.
\tag{3.8}
$$
所以
$$
\boxed{Z_z=z(z-Y)^{-1}.}
\tag{3.9}
$$
这是真正的双侧逆，适用于圆周的全部复方向；
没有用只在某个半平面成立的未经验证的 Laplace 公式，也没有预先假设一个形式 Neumann 级数具有所需预算。
对 (3.7) 取对数及 $N!\le(N+1)^N$，得 (3.2)。证毕。

## 4. 尾间隙推出统一近共振准则

现在取 $H_N$ 为原物理位中幅度最大的 $N$ 个非零 $a_j$ 所在的集合。
并列幅度固定任意规则选择。
这里只选集合，$H_N$ 的最大物理位可以任意大。

固定 $0<\varepsilon<c_0^2/64$，置
$$
\delta_N=\rho_N,\qquad
r_N=\varepsilon\delta_N^{\,2\kappa-2}.
\tag{4.1}
$$
由 (1.1)、(2.3)，
$$
\begin{aligned}
\|M_{H_N^c}\|
&\le C_W\sum_{j\notin H_N}|c_j|\\
&\le C_WC_0\sum_{n>N}\rho_n^\kappa
=o(r_N).
\end{aligned}
\tag{4.2}
$$
故沿给定子序列，充分大 $N$ 满足 (3.1)。
又 $\rho_N\to0$，所以 $r_N\le1$，
且
$$
\ell_{r_N}\le C_{\kappa,\varepsilon}L_N.
$$
引理 3.1 遂给完整的实际预算
$$
\boxed{
\sup_{|z|=r_N}\log^+\|z(z-Y)^{-1}\|
\le C\left[
1+N\log(N+1)+NL_N+L_N^{4/3}
\right].
}
\tag{4.3}
$$
由 (1.3)，右侧为 $O(N^2)$。

《任意复 ℓ² 主行的近共振预解准则》只要求
$L_N=O(N^{3/2})$ 及 (4.3) 左侧 $O(N^2)$，
两者现已满足。
其闭算子为
$$
T=X_b^2+Y-B,\qquad
B=\sum_ja_j^2(R_j-I)^2\in\mathcal G,\qquad
\operatorname{Dom}T=\operatorname{Dom}X_b^2.
$$
该准则在同一实际核内建立 $X_M^2=(B-Y)|_M$，
共同半径 $r_N$ 上只支付一次联合预解成本，
再以高位平均、完整自然域配对和固定局部头的四次预算排核。
本稿没有改变这些域或逆的作用空间；
(4.3) 只是补齐所需的实际辅助输入。
因此 $\ker T=0$、$\overline{\operatorname{Ran}T}=H$，
且原真实作用恒等式给 (1.5)。定理 1 得证。

条件 (1.4) 可弱化为沿所选子序列
$\sum_{n>N}\rho_n^\kappa
\le[\varepsilon/(4C_WC_0)]\rho_N^{2\kappa-2}$。
使用小 $o$ 的陈述省去了未知固定模型常数的显式阈值。

## 5. 不属于弱 ℓ¹ 的明确长平台族

固定任意实数 $\kappa>2$，选
$$
\frac12<\sigma<1,
$$
并取整数
$$
p>\frac{\sigma(2\kappa-2)}{\kappa\sigma-1}.
\tag{5.1}
$$
分母为正，且该比值大于2，所以这样的整数 $p\ge3$ 存在。

令
$$
N_k=2^{p^k}\quad(k\ge1),\qquad N_0=0,
$$
并按排序秩定义
$$
\boxed{
\rho_n=N_k^{-\sigma}
\quad(N_{k-1}<n\le N_k).
}
\tag{5.2}
$$
这是严格下跳、块内恒定的非增正行。
允许把这些幅度放到任意互异物理位，并逐项乘任意单位相位；其余物理位的系数取零。

首先，
$$
\sum_n\rho_n^2
\le\sum_kN_k^{1-2\sigma}<\infty.
\tag{5.3}
$$
另一方面，每块的 $\ell^1$ 质量
$$
(N_k-N_{k-1})N_k^{-\sigma}
\sim N_k^{1-\sigma}\longrightarrow\infty.
\tag{5.4}
$$
故此行不属于 $\ell^1$。
而在块末端，
$$
N_k\rho_{N_k}=N_k^{1-\sigma}\longrightarrow\infty,
\tag{5.5}
$$
所以 $\sup_n n\rho_n=\infty$，也不属于弱 $\ell^1$。

对 $N=N_k$，有
$$
L_{N_k}=1+\sigma\log N_k=O(\log N_k).
\tag{5.6}
$$
由于 $N_{k+1}=N_k^p$、$\kappa\sigma>1$，尾的连续块质量按超几何速度下降。
充分大 $k$ 时，
$$
\begin{aligned}
\sum_{n>N_k}\rho_n^\kappa
&\le\sum_{\ell>k}N_\ell^{1-\kappa\sigma}\\
&\le2N_{k+1}^{1-\kappa\sigma}\\
&=2N_k^{-p(\kappa\sigma-1)}.
\end{aligned}
\tag{5.7}
$$
与所需半径的比值因此满足
$$
\frac{\sum_{n>N_k}\rho_n^\kappa}
{\rho_{N_k}^{\,2\kappa-2}}
\le
2N_k^{\,\sigma(2\kappa-2)-p(\kappa\sigma-1)}
\longrightarrow0,
\tag{5.8}
$$
末步正是 (5.1)。
(5.6)、(5.8) 验证定理 1 的全部新增假设。

因此，对每个 (5.2) 的任意物理排列和相位主行 $a$，
每个 $b\in\ell^2$，以及每个满足 (1.1)–(1.2) 的复杂偏离行 $c$，
(1.5) 都非零且循环。

一个完全具体的参数选择是
$$
\kappa=3,\qquad \sigma=3/4,\qquad p=3.
$$
此时 $N_k=2^{3^k}$，主行在第 $k$ 块取幅度 $N_k^{-3/4}$，
尾比值在 (5.8) 中至多为 $2N_k^{-3/4}$。
可以取 $c_j=\gamma a_j^3$，其中固定 $\gamma\ne0$；
也可取 $c_j=\gamma|a_j|^3\omega_j$、$|\omega_j|=1$，
允许与主行相位完全独立。

## 6. 准确的新范围与已有快类

此例不是排序幂行 $\rho_n\le Cn^{-\sigma'}$、$\sigma'\ge1$：
(5.5) 已排除其端点。
它也不满足任何固定 $\alpha,\beta>0$ 的全局排序指数上界
$\rho_n\le Ce^{-\beta n^\alpha}$，
因为在 $n=N_k$，其值仍为 $N_k^{-\sigma}$。
所以它不属于统一准则此前明确计算的弱 $\ell^1$、
更快可和幂行和 $0<\alpha\le1$ 指数三类。

对 $|c_j|=|\gamma||a_j|^\kappa$ 的具体选择，
辅助行在 $N_k$ 处的排序值满足
$$
-\log c_{N_k}^*=O(\log N_k),
\qquad
\frac{-\log c_{N_k}^*}{N_k^3}\longrightarrow0.
$$
因此这里的辅助本身也不满足超三次排序快条件。
R270 第五附录已处理的任意慢主行加超三次快辅助，并不能直接覆盖本例。

这一范围判断使用 R270E 已正式陈述的结论，不参与本稿的正向证明。
其快辅助归属 $\mathcal G$ 的准确来源也已另行核实：
[R151 §6.1](../results/R151-quartic-analytic-approximation-gauge-stability.md)
明文使用非零归一化系数的幅度重排；
[R154 引理 2.1](../results/R154-supercubic-modes-all-polynomials-exponential-weights.md)
给 $\sum_j\beta_jN_jU_j\in\mathcal G$，
要求 $U_j$ 逐项真解析且统一有界，并明确允许任意物理排列。
它由 R115 §2 的实际占据界、先删有限最大幅度、再用物理头吞并这些坐标来证明尾型趋无穷。
这里不把 R175 的标准闭理想结论反向当成 $\mathcal G$ 的定义。

新的正向结论严格来自 (1.3)–(1.4)；
本稿没有证明任意 $\ell^2$ 行都具有这样的尾间隙。
无间隙的慢排序行、一般独立慢辅助及完整普通 Hilbert ISP 仍开放。
