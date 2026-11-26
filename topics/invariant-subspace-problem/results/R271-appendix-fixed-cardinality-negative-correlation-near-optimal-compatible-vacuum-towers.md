# R271：固定基数负相关给精确相容真空塔的三次损失与三分之二幂窗口

日期：2026-11-27（Asia/Taipei）；2026-11-26（UTC）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：已证明的中间结论。** 本文继续使用已经登记的同一条件 Bernoulli 池精确塔，不把其公式重新计为新结果。新增的是对真实量
$J_r=\|(D_x^*)^r\Omega\|\,\|v_r\|$ 的直接估计：通过固定基数乘积权测度的负相关，整个相容塔近最优的充分范围由旧的 $L=o(\sqrt x)$ 扩至 $L=o(x^{2/3})$。在同一个实际 forcing 上，有限孔真核比较的平方损失相应降为 $O(L(L+\log x)^2/x^2)$。

没有证明一般实际来源到 $\ker C^{L+1}$ 的投影损失趋零，也没有把这些真模型核直接当作原全局 $T$ 的真核。$N=\overline{B\ker T}=\ker T$ 仍未闭合。

依赖的旧对象和完整身份：

- [同一条件池的精确相容真空塔](R271-appendix-compatible-bernoulli-vacuum-towers-and-same-test-exact-kernel-approximation.md)，其 §§1–2 的塔与 §§4–6 的同源 Gram／真核比较；
- [固定头的完整物理 Gram 带宽](R271-appendix-fixed-head-physical-gram-bandwidth-and-same-test-coherent-top-repair.md)，仅在最后固定头推论中使用其已经支付的完整截尾界。

## 1. 原空间与结论

在原连续 Boolean 尾上令
$$
D=D_x=\sum_{i\ge x}b_iE_i,\qquad b_i=(i+1)^{-2},\qquad
z_i=b_i^2,\qquad t=z_x,
$$
$$
S_x=\sum_{i\ge x}z_i,\qquad p_i=z_i/t,\qquad
\lambda=\sum_i p_i=S_x/t.
\tag{1.1}
$$
原相干列和其范数为
$$
\omega_r=(D^*)^r\Omega=r!\sum_{|I|=r}b_Ie_I,
\qquad \sigma_r^2=(r!)^2e_r(z).
\tag{1.2}
$$

取独立 Bernoulli 池 $\mathcal P$，位置 $i$ 的纳入概率为 $p_i$，并令
$N=|\mathcal P|$。因为 $\mathbb EN=\lambda<\infty$，$N$ 几乎处处有限。
给定整数 $L\ge1$，沿用旧稿同一个条件事件 $N\ge L$，以及
$$
v_r=\mathbb E\left[
\frac1{(N)_{\underline r}}
\sum_{\substack{I\subset\mathcal P\\|I|=r}}b_I^{-1}e_I
\ \middle|\ N\ge L\right],\qquad 0\le r\le L.
\tag{1.3}
$$
零阶是 $v_0=\Omega$。所有条件概率严格正。
旧稿的逐坐标计数准确给
$$
Dv_r=v_{r-1},\qquad D^rv_r=\Omega,\qquad
\langle v_r,\omega_r\rangle=1.
\tag{1.4}
$$
下面的范数证明也独立支付 (1.3) 的 Hilbert 收敛。

假设
$$
\lambda\ge16,\qquad L+\log\lambda\le\lambda/16.
\tag{1.5}
$$
置
$$
\kappa=\frac{128L(L+\log\lambda)^2}{\lambda^2},\qquad
\mathfrak A_{x,L}
=\frac{e^\kappa+2\lambda^{-3}}{1-e^{-\lambda/4}}.
\tag{1.6}
$$

**定理 1.1（整个原精确塔）。** 对全部 $0\le r\le L$，
$$
\boxed{1\le J_r:=\sigma_r\|v_r\|\le\mathfrak A_{x,L}.}
\tag{1.7}
$$
并且
$$
\boxed{
0\le1-\mathfrak A_{x,L}^{-2}
\le\frac{256L(L+\log\lambda)^2}{\lambda^2}
 +4\lambda^{-3}+4e^{-\lambda/4}.
}
\tag{1.8}
$$
由于 $\lambda\asymp x$，$L=o(x^{2/3})$ 时，(1.5) 最终成立且
$\mathfrak A_{x,L}\to1$。

这控制的是完整物理 $\sigma_r$，没有把 $\sigma_r^2$ 换成
$r!S_x^r$ 后忽略碰撞损失，也没有把分别最小的各层原像拼接为相容塔。

## 2. 固定基数乘积权测度：所需负相关的完整证明

给有限或可数正权 $a_i$，满足 $\sum_i a_i<\infty$，固定整数 $r\ge1$。
在 $r$ 元子集上定义
$$
\mu_r(I)=\frac{a_I}{e_r(a)},\qquad X_i(I)=\mathbf1_{\{i\in I\}}.
$$
只在 $e_r(a)>0$ 时使用。则
$$
\operatorname{Cov}_{\mu_r}(X_i,X_j)\le0\quad(i\ne j).
\tag{2.1}
$$

先证有限权。去掉 $i,j$ 后，记
$A=e_{r-2}$、$B=e_{r-1}$、$C=e_r$，越界指标按零计。
完整分母是
$$
Z=C+(a_i+a_j)B+a_ia_jA.
$$
直接展开给
$$
\mathbb EX_i\,\mathbb EX_j-\mathbb E(X_iX_j)
=\frac{a_ia_j(B^2-AC)}{Z^2}.
\tag{2.2}
$$
这里 $B^2\ge AC$ 可用以下短归纳完整证明。有限正权的基本对称和序列从
$(1)$ 开始，每加入一个权 $u\ge0$，序列由 $c_k$ 变为
$d_k=c_k+u c_{k-1}$。若 $c$ 无内部零且对数凹，则
$$
\begin{aligned}
d_k^2-d_{k-1}d_{k+1}
={}&(c_k^2-c_{k-1}c_{k+1})\\
&+u(c_kc_{k-1}-c_{k-2}c_{k+1})
+u^2(c_{k-1}^2-c_{k-2}c_k)\ge0.
\end{aligned}
$$
中间项非负来自相邻非零比值递减；零端点直接成立。归纳给所需对数凹性，
从而 (2.2) 证明 (2.1)。可数权用有限截断的基本对称和及概率极限得到。

设 $\alpha_i,\beta_i\ge0$ 都有界。令
$$
F_\alpha(I)=\exp\!\left(\sum_{i\in I}\alpha_i\right).
$$
则
$$
\boxed{
\mathbb E(F_\alpha F_\beta)
\le e^{r\|\alpha\|_\infty\|\beta\|_\infty}
\,\mathbb EF_\alpha\,\mathbb EF_\beta.
}
\tag{2.3}
$$
事实上，置
$\Psi(s,u)=\log e_r(a_i e^{s\alpha_i+u\beta_i})$。
其混合导数为相应倾斜后的固定基数测度中的协方差。
倾斜后仍是正权乘积测度，所以 (2.1) 继续成立；因此
$$
\partial_s\partial_u\Psi
\le\sum_i\alpha_i\beta_i\operatorname{Var}(X_i)
\le r\|\alpha\|_\infty\|\beta\|_\infty.
$$
在单位正方形积分即得 (2.3)。可数权由有界倾斜及有限截断得到；
每个子集恰有 $r$ 位，相关随机变量统一有界，无交换极限的缺口。

## 3. 同一池列的精确系数及其归一化

对 $|J|=r$，令 $N_{J^c}=|\mathcal P\setminus J|$，并记
$$
F_r(J)
=\mathbb E\frac{N_{J^c}!}{(N_{J^c}+r)!}
=\frac1{(r-1)!}\int_0^1
u^{r-1}\prod_{i\notin J}(1-p_i u)\,du.
\tag{3.1}
$$
保留旧条件事件的系数为
$$
F_{r,L}(J)
=\mathbb E\left[
\frac{\mathbf1_{\{N_{J^c}+r\ge L\}}}
{(N_{J^c}+r)_{\underline r}}\right],
\qquad0\le F_{r,L}(J)\le F_r(J).
\tag{3.2}
$$
写 $P_j=\Pr(N\ge j)$，独立性给原 (1.3) 的准确坐标
$$
(v_r)_J=\frac{b_J}{t^rP_L}F_{r,L}(J).
\tag{3.3}
$$

在本节取 $\mu_r(J)=z_J/e_r(z)$。一个关键归一化是
$$
\boxed{\mathbb E_{\mu_r}F_r
=\frac{t^r}{r!e_r(z)}P_r\ge\lambda^{-r}P_r.}
\tag{3.4}
$$
第一等式直接来自非条件池：每个大小至少 $r$ 的确定池，其逆权列经
$D^r$ 恰为 $\Omega$；大小不足 $r$ 时列为零。也可将 (3.1) 按
$r!z_J/t^r$ 求和，按每个确定池计数。第二步只用
$r!e_r(z)\le S_x^r$。

用 Chernoff 参数 $\log2$，对 $j\le L\le\lambda/4$ 有
$$
\Pr(N<j)\le2^{j-1}\mathbb E2^{-N}
\le\exp(j\log2-\lambda/2)\le e^{-\lambda/4}.
\tag{3.5}
$$
故 $P_j\ge1-e^{-\lambda/4}\ge1/2$。

## 4. Beta 积分低段：直接估归一化方差

取
$$
u_0=\frac{8(L+\log\lambda)}\lambda\le\frac12.
$$
将 (3.1) 分为 $F_r^{\rm lo}$（$0\le u\le u_0$）与
$F_r^{\rm hi}$。在低段置
$$
a_r(u)=\frac{u^{r-1}}{(r-1)!}\prod_i(1-p_i u),
\qquad h_u(i)=-\log(1-p_i u).
$$
则
$$
F_r^{\rm lo}(J)=\int_0^{u_0}a_r(u)
\exp\!\left(\sum_{i\in J}h_u(i)\right)du,
\qquad0\le h_u(i)\le2u_0.
$$
在 $[0,u_0]$ 上，乘积均严格正且收敛。对两点 $u,v$ 使用 (2.3)，再以
非负 Tonelli 交换二重积分，得到
$$
\boxed{
\mathbb E_{\mu_r}(F_r^{\rm lo})^2
\le e^{4r u_0^2}
\bigl(\mathbb E_{\mu_r}F_r^{\rm lo}\bigr)^2.
}
\tag{4.1}
$$
这一步控制的是系数的相对方差。旧逐坐标最大值估计会额外支付没有必要的
一阶偏移；(4.1) 保留真实归一化，故损失为 $O(L^3/\lambda^2)$。

## 5. Beta 积分高段：统一尾误差

因为 $p_i\le1$，对 $|J|=r$ 有
$\sum_{i\notin J}p_i\ge\lambda-r=:\beta\ge3\lambda/4$。
于是
$$
F_r^{\rm hi}(J)
\le\frac1{(r-1)!}\int_{u_0}^\infty
u^{r-1}e^{-\beta u}\,du
\le\beta^{-r}2^r e^{-\beta u_0/2}.
\tag{5.1}
$$
最后一步就是形状为 $r$、速率为 $1$ 的 Gamma 密度在参数 $1/2$ 的
指数 Markov 界，其指数矩为 $2^r$。

由 $r\le L\le\lambda/4$、(3.4)–(3.5)，
$$
\begin{aligned}
\frac{\sup_JF_r^{\rm hi}(J)}{\mathbb E_{\mu_r}F_r}
&\le P_r^{-1}\left(\frac\lambda{\lambda-r}\right)^r
2^r e^{-\beta u_0/2}\\
&\le2\exp\bigl[L/3+L\log2-3(L+\log\lambda)\bigr]\\
&\le2\lambda^{-3}.
\end{aligned}
\tag{5.2}
$$
这里用了
$-r\log(1-r/\lambda)\le r^2/(\lambda-r)\le L/3$。
所有估计对 $1\le r\le L$ 同时成立。

由 $L^2(\mu_r)$ 三角不等式、(4.1) 和 (5.2)，
$$
\frac{\|F_r\|_{L^2(\mu_r)}}{\mathbb E_{\mu_r}F_r}
\le e^{2r u_0^2}+2\lambda^{-3}
\le e^\kappa+2\lambda^{-3}.
\tag{5.3}
$$
最后由 (3.3)–(3.4)，
$$
\sigma_r\|v_r\|
\le\frac{r!e_r(z)}{t^rP_L}\|F_r\|_{L^2(\mu_r)}
=\frac{P_r}{P_L}
\frac{\|F_r\|_{L^2(\mu_r)}}{\mathbb E_{\mu_r}F_r}
\le\mathfrak A_{x,L}.
$$
这证明上界及 Hilbert 收敛。下界来自 (1.4) 的 Cauchy–Schwarz。
零阶直接成立。

又
$$
\log\mathfrak A_{x,L}
\le\kappa+2\lambda^{-3}+2e^{-\lambda/4},
$$
将 $1-e^{-2a}\le2a$ 用于 $a=\log\mathfrak A_{x,L}$ 得 (1.8)。

## 6. 返回同一实际 source 的真核比较

令 $C^h=0$ 与 $D_x$ 作用于不同张量因子，取 $L<h$，并保持原
$$
R_La=\sum_{r=0}^L(-C)^ra\otimes\frac{\omega_r}{\sigma_r^2},
\qquad
T_La=\sum_{r=0}^L(-C)^ra\otimes v_r,
\qquad W_L=\ker C^{L+1}.
$$
这里 $T_L$ 是塔映射，不是原全局边界算子 $T$。
由精确相容性，$T_LW_L\subset\ker(C+D_x)$。
由 (1.4)，同层正交差保持旧准确身份
$$
R_L^*T_L=H_L:=R_L^*R_L,
\qquad
\boxed{H_L\preceq T_L^*T_L\preceq\mathfrak A_{x,L}^2H_L.}
\tag{6.1}
$$

对同一个 forcing $F=i_0g_0$，令
$f_L=P_{R_L\mathfrak h}F$，$p_L=P_{R_LW_L}F$，
$k_L=P_{T_LW_L}F$，并令
$$
\delta_L^2=\|f_L-p_L\|^2.
$$
所有投影在原物理内积中，两个限制源 inverse 均先压缩到同一个真实
$W_L$ 再求逆。式 (6.1) 给
$\|k_L\|^2\ge\mathfrak A_{x,L}^{-2}\|p_L\|^2$。
因此，在原同一个 $V_Q,K_Q$ 和 $Q\ge R+L$ 的已付 forcing 身份下，
$$
\boxed{
\|(P_{V_Q}-P_{K_Q})F\|^2
\le(1-\mathfrak A_{x,L}^{-2})\|f_L\|^2
+\mathfrak A_{x,L}^{-2}\delta_L^2.
}
\tag{6.2}
$$
这是旧精确同源比较中把粗 $A_{x,L}$ 替换为实付的 $\mathfrak A_{x,L}$。
没有修改 source、核旗、母支持或完整 Gram，也没有用
$\|C^{L+1}g_0\|$ 代替真实距离 $\delta_L$。

对固定原头 $m$，在额外条件 $d-1\le L<h$ 下，旧完整物理相似／带宽证明已给
$$
\delta_L^2\le\chi_m^2\rho_m^{2\nu_{m,L}}\|g\|^2,
\quad \rho_m=(\chi_m-1)/(\chi_m+1),
\quad \nu_{m,L}=\left\lceil\frac{L-d+2}{d-1}\right\rceil.
$$
因此所有旧的 $m,R,Q$ 条件保留时，新的同源充分预算是
$$
\boxed{
\|u_g\|^2\le
\left[
\frac{256L(L+\log\lambda)^2}{\lambda^2}
+4\lambda^{-3}+4e^{-\lambda/4}
+\chi_m^2\rho_m^{2\nu_{m,L}}
\right]\|g\|^2.
}
\tag{6.3}
$$
$\chi_m=1$ 的相应尾项仍按旧稿删除。

当 $x\ge4$，积分比较给 $(x+1)/3\le\lambda\le x$。
所以 (6.3) 中的前三项还可用
$$
\frac{2304L(L+\log x)^2}{x^2}
+\frac{108}{x^3}+4e^{-(x+1)/12}
\tag{6.4}
$$
上界；例如 $L+\log x\le(x+1)/48$ 保证所需小参数条件。
沿旧固定头的 $L=O_m(\log x)$ 选参，并保持其
$\rho_m^{2\nu_{m,L}}\le(x+1)^{-6}$，得到改进
$$
\boxed{\|u_g\|=O_m\!\left(\frac{(\log x)^{3/2}}x\right)\|g\|.}
\tag{6.5}
$$

## 7. 接现有 Chebyshev 源界：更小的 moving-head 模型窗口

以上固定头 Neumann 写法不是当前最强的源界。
[缩放齐次头与完整源 Chebyshev 稿](R271-appendix-scaled-head-similarity-chebyshev-source-energy-and-moving-model-window.md)
已经在 $d-1\le L<h$、同一个物理源及同一个 $W_L$ 上证明
$$
\log\chi_m\le\frac{47}{4}d^4,\qquad
\vartheta_m=\frac{\sqrt{\chi_m}-1}{\sqrt{\chi_m}+1},\qquad
\nu=\left\lfloor\frac L{d-1}\right\rfloor,
$$
$$
\delta_L^2\le\min\{1,4\vartheta_m^{2\nu}\}\|f_L\|^2.
\tag{7.1}
$$
因此当前更强的同源结论是
$$
\boxed{
\|u_g\|^2\le
\left[1-\mathfrak A_{x,L}^{-2}
+\mathfrak A_{x,L}^{-2}\min\{1,4\vartheta_m^{2\nu}\}\right]\|g\|^2.
}
\tag{7.2}
$$
旧稿的显式真核候选 $k_{\rm pol}=T_La_{\rm pol}$ 也原样保留：它的原
$m$ 后总孔数至多 $L$，且
$$
\|f_L-k_{\rm pol}\|^2
\le\left[4\vartheta_m^{2\nu}
+(\mathfrak A_{x,L}^2-1)(1+2\vartheta_m^\nu)^2\right]\|g\|^2.
\tag{7.3}
$$
这一步是把新塔估计放入已付的真实候选，不重新证明或重新计数旧 Chebyshev 引理。

一个比该稿原 $x_m=\lceil e^{12d^4}\rceil$ 更小的明确模型窗口是
$$
x_m=\lceil e^{9d^4}\rceil,\qquad
R_m=x_m-m,\qquad
L_m=\lceil e^{(71/12)d^4}\rceil,\qquad
Q_m\ge R_m+L_m,\quad m\ge10.
\tag{7.4}
$$
原 $d-1\le L_m<d+R_m$ 保留。沿旧稿的准确整数估计，
$$
\vartheta_m^{2\nu}
\le\exp\left[-\frac2d e^{d^4/24}\right].
$$
而 $\log\lambda\le\log x_m\le L_m$，(1.5) 成立，
(6.4) 给
$$
1-\mathfrak A_{x_m,L_m}^{-2}
\le73728e^{-d^4/4}+108e^{-27d^4}+4e^{-x_m/12}.
$$
从而
$$
\boxed{
\sup_{\|g\|\le1}\|u_g\|^2
\le73728e^{-d^4/4}+108e^{-27d^4}+4e^{-x_m/12}
+4\exp\left[-\frac2d e^{d^4/24}\right]\longrightarrow0.
}
\tag{7.5}
$$
这仍是**原有限头模型**的 moving-head 结论。
虽然 $9d^4$ 比旧 $12d^4$ 小，但两者都超出已付全局母窗
$Q\le e^{O(d^3)}$；原全局 lift、同 $W$ 运输和两侧高头幂费用仍不能省略。

## 8. 尚未支付的实际终端

在移动头中，新塔误差只要求 $L=o(x^{2/3})$，但原
$\delta_L=\operatorname{dist}(f_L,R_L\ker C^{L+1})$ 仍要支付。
它是完整源在真实短核上的限制损失；一般源的末端可达
$h-1$，不能因为新塔在较长窗口近最优就删掉该损失。

下一实际接口是：对同一个 $w$ 的源，证明该完整限制损失受其真实尾层能量控制，
或给出足够的源相关 Schur 预算，再将同一 $K_Q$ 核经已付 carry／正则 lift
运输到原全局 $N$。本稿不把 $T_LW_L$、$\ker(C+D_x)$ 和 $\ker T$
混作一个空间，也未证明普通 Hilbert ISP。
