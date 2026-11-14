# R236 附录：稀疏偏离支撑、任意 ℓ² 共振背景与既有空谱范围

日期：2026-11-13。作者：Astra-ISP-0c017065 / central_review。
状态：主会话已完整核验；一般普通 Hilbert ISP 未完成。

完整证明见[支撑扩展稿](../notes/2026-11-13-sparse-deviation-support-and-arbitrary-l2-resonant-background-central-review.md)；
旧范围的逐式核对见[空谱锚范围稿](../notes/2026-11-13-existing-empty-spectrum-anchor-scope-for-near-resonance-central-review.md)。
本附录扩展[近共振实际预解准则](R236-appendix-next-order-quadratic-resonance-and-resolvent-criterion.md)的偏离支撑；完整主行始终保留。

## 1. 支撑版本

给定
$$
u=a_*+\sum_j a_j\chi_j,\qquad w=b_*+\sum_jb_j\chi_j,\qquad
a,b\in\ell^2(\mathbb C).
$$
取无限集合 $S\subseteq\{j:a_j\ne0\}$，其非零主幅度排序为
$\rho_n^S$。$S^c$ 上的主行任意，只需完整 $a\in\ell^2$。
固定实数 $\kappa>2$，令
$$
c_j=0\ (j\notin S),\qquad
|c_j|\le C_0|a_j|^\kappa\ (j\in S),
$$
并对充分高物理位 $j\in S$ 有
$|c_j|\ge c_0|a_j|^\kappa$，$c_0>0$。

记 $R_j=V(e^{-2b_j}N_j)$，以及
$$
Y_S=\sum_{j\in S}c_j(R_j-I),\qquad
B=\sum_{j\ge0}a_j^2(R_j-I)^2\in\mathcal G.
$$
$X_b$ 和 $B$ 使用完整主行，包括全部 $S^c$ 的慢位。

**定理。** 固定 $0<\varepsilon<c_0^2/64$。
若沿无穷 $N$，$\delta_N=\rho_N^S$ 满足
$$
L_N=1+\log^+\delta_N^{-1}=O(N^{3/2}),\qquad
\sup_{|z|=\varepsilon\delta_N^{2\kappa-2}}
\log^+\|z(z-Y_S)^{-1}\|=O(N^2),
\tag{1.1}
$$
则自然闭算子
$$
T=X_b^2+Y_S-B,\qquad \operatorname{Dom}T=\operatorname{Dom}X_b^2
$$
单射、稠密像，且
$$
\boxed{
\left[u^2+2\sum_{j\ge0}a_j^2(\chi_j-1)
+\sum_{j\in S}c_j(\chi_j-1)\right]e^w
\text{ 非零且循环}.
}
\tag{1.2}
$$
不要求 $S^c$ 上有偏离下界；其中无限多个非零主位可以完全共振。

## 2. 为何完整慢背景仍受控制

从 $S$ 内前 $N$ 个幅度删去前 $N/4$ 个排序秩和最低 $N/4$ 个物理位，
仍可取 $Q_N=\lfloor N/2\rfloor$ 位组成 $I_N\subset S$。全部选位有
$$
\min I_N\ge\lfloor N/4\rfloor,\qquad
\delta_N\le |a_j|\le2\|a\|_2/\sqrt N.
$$
固定小 $\theta>0$、$r=\lceil\sqrt{N/\theta}\rceil$ 时，
任意 $r$ 元 $F\subset I_N$ 满足
$\sum_F|a_j|=O_\theta(1)$，$\sum_F|a_j|^2=O_\theta(N^{-1/2})$。

若 $M=\ker T$，R176 对完整主行给
$M\subset\bigcap_n\operatorname{Dom}X_b^n$、$X_M$ 有界和
$X_M^2=(B-Y_S)|_M$。
原准则的共同核内逆
$$
\left(\prod_{j\in F}(8a_jX_M+4c_jI)\right)\mathfrak R_F=I_M
$$
仍仅支付一次联合预解成本
$K_0N^2+(2\kappa-1)rL_N+C_Mr+C$。

$S^c$ 的主尾虽不出现在形式符号差中，真实反射仍必须计入它。
R260 的最高位壳仅使用完整 $a\in\ell^2$、$a^2\in\ell^1$、$c\in\ell^1$，
故全部自然 jets 的误差仍为
$s!Ce^{-385\,16^{m_N-1}}$，不含 $\max F$。
准确
$$
\widehat B-B=\sum_{j\in F}
16a_j^2(e^{-2b_j}N_j)^3
(I-e^{-4b_j}N_j^2)^{-2}
$$
无 Boolean 一次项。核内先消逆，再施左反射，得到同一个非零弱平均。
固定局部低头的两侧 $A$ 幂支付四次导子成本；完整自然域配对排 $M$。
这证明 (1.2) 的整个向量，未把它换成子行向量。

## 3. 可直接验证的子行

(1.1) 在以下情况下已由前稿的实际预算付清，所有条件只针对 $\rho^S$：

- 某个 $\sigma_S\ge1$ 满足
  $0<\limsup n^{\sigma_S}\rho_n^S\le\sup n^{\sigma_S}\rho_n^S<\infty$；
- 某个 $0<\alpha\le1$ 有全局指数上界
  $\rho_n^S\le B e^{-\beta_-n^\alpha}$ 和无穷子序列下界
  $\rho_N^S\ge b e^{-\beta_+N^\alpha}$；
- 沿无穷 $N$ 有 $L_N=O(N)$ 且
  $\sum_{n>N}(\rho_n^S)^\kappa=o((\rho_N^S)^{2\kappa-2})$。

第三条包含非弱 $\ell^1$ 长平台。其 Laplace 双侧逆只使用辅助 $c$ 的排序与真实物理头，不要求 $S$ 具有正密度。

## 4. 不落既有空谱分支的慢幂例子

取
$$
a_j=(-1)^j(j+1)^{-\sigma},\qquad \frac12<\sigma<1,
\quad
S=\{\lceil k^{1/\sigma}\rceil-1:k\ge1\}.
$$
完整主行属于 $\ell^2\setminus\ell^1$，无弱 $\ell^1$ 上界。
但在 $j_k=\lceil k^{1/\sigma}\rceil-1$ 上，
$$
2^{-\sigma}/k\le |a_{j_k}|\le1/k.
$$
因此对任意 $\gamma\ne0$、任意单位相位 $\omega_k$，令
$c_{j_k}=\gamma|a_{j_k}|^\kappa\omega_k$、$c_{S^c}=0$，
(1.2) 对任意复 $\ell^2$ 指数权成立。
偏离排序是 $k^{-\kappa}$，不在 R270E 的超三次快类。

对每个相位 $\phi$，偶数与奇数子行的相位缺陷分别为
$(j+1)^{-\sigma}(1-\cos\phi)$ 和
$(j+1)^{-\sigma}(1+\cos\phi)$。
两条质量均发散、两个因子不同时为零，所以
$$
\sum_j(|a_j|-\operatorname{Re}(e^{-i\phi}a_j))=\infty
\quad\text{对全部 }\phi.
$$
R138 将该完整 first 归入全平面连续谱类；
此例没有重复旧空谱锚结论。

## 5. 支撑外的独立快偏离

允许再加 $S^c$ 上的 $d\in\ell^1$，条件是
$$
D_{\rm fast}=\sum_{j\notin S}d_j(R_j-I)\in\mathcal G.
$$
有限支撑或非零幅度排序满足
$-\log d_n^*/n^3\to\infty$ 足够。
令 $B'=B-D_{\rm fast}$，仍属 $\mathcal G$。
因为 $F\subset S$，形式符号差
$\widehat D_{\rm fast}-D_{\rm fast}=0$；
实际物理反射的余壳用 $d\in\ell^1$ 另付。
故 (1.2) 可再加
$[\sum_{j\notin S}d_j(\chi_j-1)]e^w$。
重叠快行会改变选位线性系数，不能未经重验忽略。

## 6. 必须保留的既有范围

若 $a\notin\ell^1$，但存在 $\phi$ 使相位缺陷可和，
[R134](R134-empty-spectrum-first-chaos-polynomial-cyclicity.md)、
[R138](R138-first-chaos-complete-spectrum-classification.md)
已经给 $X_u$ 空谱。
其逆 $R=X_u^{-1}$ 拟幂零，且
$\operatorname{Dom}X_u^p=\operatorname{Ran}R^p$。
对任意有界 $D_k\in A'$，
$$
\left(X_u^p+\sum_{k<p}D_kX_u^k\right)^{-1}
=R^p\left[I+\sum_{k<p}D_kR^{p-k}\right]^{-1}.
$$
任意有界交换扰动仍为空谱，故任意复权的倾斜也保持该结论。
这些真实逆保持每个未知闭 $A$ 不变子空间，并在完整自然域上给双射。

[R155](R155-empty-anchor-bounded-auxiliary-polynomials.md)
早已将它用于任意 $\ell^1$ 辅助及任意复 $\ell^2$ 权的首一主变量多项式。
因此同射线非 $\ell^1$ 主行的近共振，即使 $c\in\ell^1$ 完全任意、$a_*=0$，
也不是本次新闭合范围。
另若 $a\in\ell^1$ 且 $a_*+\sum a_j\ne0$，
$X_b^2+Y-B$ 的字符非零，原本就是范数代数单位。

真正继续的问题包括全平面连续谱主行的全支撑慢偏离。
上述交替慢幂在 $\sigma=1$ 时已由近共振统一准则关闭；
尚未闭的规则全支撑带为 $1/2<\sigma<1$。
R259 的原点解析 Bell 分支不能直接处理这里的分歧平方根，
也未提供未知二次核上的统一预解界。
