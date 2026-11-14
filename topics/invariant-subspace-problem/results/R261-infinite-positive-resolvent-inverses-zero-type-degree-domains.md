# R261：无穷正预解式逆的平方根次数零型与任意小拉伸域

日期：2026-11-13（UTC）。作者：normal_states / Astra-ISP-1cf。

状态：已证明的中间结论；root已全文核验有限头/尾分词、全部实际域及逐次数原像。本文承接已经发布的 R230 无穷逆测试，不重做其收敛、配对反例或有限混合扩展。新增的是逆成本的零型改进，以及每个任意小平方根次数权空间的实际像包含。它没有构造假想正常湮灭见证的专属配对正则器，也没有估出 R253 的 $q_m$ 下界。

## 1. 已有输入与新增结论

沿用
[R230 无穷正预解式的收敛逆测试](R230-appendix-positive-infinite-resolvent-inverse-tests-and-pairing-obstruction.md)
的原 Haar 模型及记号：
$$
H_\sigma=\operatorname{Dom}e^{\sigma\mathcal N},
\qquad \|x\|_\sigma=\|e^{\sigma\mathcal N}x\|,
\qquad 0\le\sigma\le1.
$$
$\mathcal N\chi_F=|F|\chi_F$ 是 Walsh 次数算子，$H_0=H$。

给定非负行 $b^{(\nu)}\in\ell^2_+$，令
$$
X_\nu=\sum_jb_j^{(\nu)}V_j,\qquad
P_n=\prod_{\nu=1}^n(I+X_\nu)^{-1},\qquad
b=\sum_{\nu\ge1}b^{(\nu)}\in\ell^2_+.
\tag{1.1}
$$
所有一阶算子使用既有真实闭实现。R230 已证明：

- $P_n$ 强收敛到非零收缩 $P\in A'$，且 $P$ 单射；
- 反向自然词 $F_n=(I+X_n)\cdots(I+X_1)$ 在每对严格分离的指数次数空间之间按算子范数收敛；
- 其相容极限 $G=F_\infty$ 满足
  $PGx=x$ 对所有 $x\in H_\sigma$、$\sigma>0$ 成立。

故在这些输入上 $G$ 就是原 $P$ 的真正逆 $P^{-1}$。

令 $\Pi_{\le q}$ 为整个 Walsh 次数至多 $q$ 的正交投影；它通常是无限秩。定义
$$
\mathcal G_\epsilon
=\operatorname{Dom}\exp\!\bigl(\epsilon\sqrt{I+\mathcal N}\bigr),
\qquad \epsilon>0.
\tag{1.2}
$$

**主定理。** 对每个固定的非负总行 $b\in\ell^2$，有：

1. 对每个 $\epsilon>0$，存在有限常数 $C_{\epsilon,b}$，使所有
   $0\le\tau<\sigma\le1$ 都满足
   $$
   \boxed{
   \|G:H_\sigma\to H_\tau\|
   \le C_{\epsilon,b}
   \exp\!\left(\frac{\epsilon}{\sigma-\tau}\right).
   }
   \tag{1.3}
   $$
   换言之，逆在指数权损失趋零时的增长具有零型：
   $$
   \boxed{
   \lim_{\delta\downarrow0}
   \delta\log^+
   \sup_{\substack{0\le\tau<\sigma\le1\\\sigma-\tau=\delta}}
   \|G:H_\sigma\to H_\tau\|=0.
   }
   \tag{1.4}
   $$

2. 在整个有限次数空间上，
   $$
   \boxed{
   \log\|G|_{\operatorname{Ran}\Pi_{\le q}}\|
   =o(\sqrt q)\qquad(q\to\infty).
   }
   \tag{1.5}
   $$
   等价地，对每个 $\epsilon>0$，存在 $D_{\epsilon,b}<\infty$，使
   $$
   \boxed{
   \|Gx\|\le D_{\epsilon,b}
   e^{\epsilon\sqrt{q+1}}\|x\|,
   \qquad x\in\operatorname{Ran}\Pi_{\le q}.
   }
   \tag{1.6}
   $$

3. 对每个 $\epsilon>0$，
   $$
   \boxed{
   \mathcal G_\epsilon\subseteq\operatorname{Ran}P,
   \qquad
   P^{-1}:\mathcal G_\epsilon\to H
   \text{ 为有界线性映射。}
   }
   \tag{1.7}
   $$

这里每个 $C_{\epsilon,b}$、$D_{\epsilon,b}$ 可以依赖 $\epsilon$ 和 $b$。不声称它们在 $\epsilon\downarrow0$ 时一致，更不由 (1.7) 推出全部多项式次数光滑向量都属于 $\operatorname{Ran}P$。

## 2. 保留实际 carry 的正项比较与有限头分解

本节准确列出所用 R230 比较算子，说明新的有限头预算。

在一位 Walsh 基中令
$$
W_j=|V_j^0|_{\mathrm{ent}}
=\begin{pmatrix}0&1\\1&2\end{pmatrix},
\qquad
\kappa=\|W_j\|=1+\sqrt2.
$$
$\mathrm{ent}$ 表示逐个矩阵项取绝对值，并非算子绝对值。

R171 的真实局部级数为
$$
V_j-V_j^0=\sum_{L\ge1}B_{j,L},\qquad
\operatorname{supp}B_{j,L}\subseteq[j,j+L],
$$
$$
\|B_{j,L}\|\le18\eta_j\eta_*^{L-1},
\qquad
\eta_*=\sup_j\eta_j\le e^{-770}.
$$
令 $B_{j,L}^+=|B_{j,L}|_{\mathrm{ent}}$。R230 已完整支付有限维绝对矩阵成本
$$
\|B_{j,L}^+\|\le2^{(L+1)/2}\|B_{j,L}\|,
$$
从而对 $0\le s\le1$，
$$
\left\|\sum_jc_j\sum_{L\ge1}B_{j,L}^+
\right\|_{B(H_s)}
\le C_{\rm car}\|c\|_2
\quad(c\in\ell^2_+),
\tag{2.1}
$$
其中
$$
C_{\rm car}
=\frac{36e^2\|\eta\|_2}{1-\sqrt2e\eta_*}<\infty.
$$
这些级数在每个所用加权空间上绝对收敛。

辅助正项尺度映射为
$$
\mathcal M_c=\sum_jc_jW_j+
\sum_jc_j\sum_{L\ge1}B_{j,L}^+.
$$
它对非负行 $c$ 线性，并满足
$$
\boxed{
\|\mathcal M_c:H_s\to H_{s-\delta}\|
\le C_+\|c\|_2\delta^{-1/2},
\quad 0<\delta\le s\le1,
\quad C_+=16+C_{\rm car}.
}
\tag{2.2}
$$
所有矩阵比较均在固定 Walsh 系数非负锥中进行。没有把 $\mathcal M_c$ 当作原一阶乘子，也不要求它在全 $H$ 生成有界半群。

固定一个位置截断 $J\ge0$，分解
$$
b=b^{<J}+b^{\ge J},\qquad
L_J=\mathcal M_{b^{<J}},\qquad
T_J=\mathcal M_{b^{\ge J}},\qquad
g_J=\|b^{\ge J}\|_2.
\tag{2.3}
$$
$g_J\to0$。

有限头部分在每一个 $H_s$ 上有统一于 $s\in[0,1]$ 的有界实现。事实上，一位加权相似的条件数不超过 $e$，所以
$$
\|W_j\|_{B(H_s)}\le e\kappa.
$$
连同 (2.1)，得到
$$
\boxed{
\|L_J\|_{B(H_s)}\le B_J:=
e\kappa\sum_{j<J}b_j+C_{\rm car}\|b^{<J}\|_2
\quad(0\le s\le1).
}
\tag{2.4}
$$
$B_J$ 只在固定 $J$ 时使用，可以随 $J$ 增长。其 carry 部分仍包含所有实际更高位，并已由 (2.1) 支付；这里的“有限头”指有限个行系数，不是把真实 carry 再截断。

尾部分保留小的平方和系数：
$$
\boxed{
\|T_J:H_s\to H_{s-\delta}\|
\le C_+g_J\delta^{-1/2}.
}
\tag{2.5}
$$

## 3. 按尾因子数分组，不要求正项矩阵交换

R230 已证明实际 first 自然词在正指数输入上可交换，且其有界系数截断在严格分离的尺度间按范数收敛。先对实际词对称化、再取逐项绝对值，给
$$
|F_nx|
\le\sum_{k\ge0}\frac1{k!}\mathcal M_b^k|x|.
\tag{3.1}
$$
右边只用相容尺度映射的有限自然词和其范数收敛级数。

新增步骤是对
$$
\mathcal M_b=L_J+T_J
$$
的每个幂按尾因子数展开。$L_J$ 和 $T_J$ 未被假定交换。

固定总权损失 $\delta=\sigma-\tau>0$。考虑一个含 $h$ 个 $L_J$、$\ell$ 个 $T_J$ 的任意有序词。当 $\ell\ge1$ 时，将全部损失均分给这 $\ell$ 次尾作用；每个头作用保留当前权，不消耗损失。由 (2.4)–(2.5)，这个词从 $H_\sigma$ 到 $H_\tau$ 的范数至多为
$$
B_J^h
\left(C_+g_J\sqrt{\ell/\delta}\right)^\ell.
\tag{3.2}
$$
所有中间权都在 $[\tau,\sigma]$ 中。若最后一个尾作用后尚有头作用，它们仍由 (2.4) 在 $H_\tau$ 上控制。$\ell=0$ 时直接用 $B_J^h$ 和收缩嵌入 $H_\sigma\hookrightarrow H_\tau$。

长度 $h+\ell$ 的这类词共有 $\binom{h+\ell}{\ell}$ 个。因此
$$
\begin{aligned}
\left\|\sum_{k\ge0}\frac{\mathcal M_b^k}{k!}:
H_\sigma\to H_\tau\right\|
&\le
\sum_{h,\ell\ge0}
\frac{B_J^h}{h!}
\frac{(C_+g_J\sqrt{\ell/\delta})^\ell}{\ell!}\\
&=e^{B_J}
\sum_{\ell\ge0}
\frac{(C_+g_J/\sqrt\delta)^\ell\ell^{\ell/2}}{\ell!}.
\end{aligned}
\tag{3.3}
$$
零次项按 $1$ 解释。这是绝对范数收敛的主控，没有将两个非交换指数相乘。

由 $\ell!\ge(\ell/e)^\ell$ 及 Cauchy–Schwarz，
$$
\sum_{\ell\ge0}\frac{a^\ell\ell^{\ell/2}}{\ell!}
\le
\sum_{\ell\ge0}\frac{(\sqrt e\,a)^\ell}{\sqrt{\ell!}}
\le\sqrt2e^{ea^2}.
$$
所以 (3.1)–(3.3) 给全部有限逆词的统一界；再取已证的算子范数极限 $F_n\to G$，得到
$$
\boxed{
\|G:H_\sigma\to H_\tau\|
\le\sqrt2\exp\!\left(
B_J+\frac{eC_+^2g_J^2}{\sigma-\tau}
\right)
\qquad(J\ge0).
}
\tag{3.4}
$$
$J=0$ 恢复 R230 的原界；$J\to\infty$ 后才使用 $g_J\to0$，给本稿的新零型。

## 4. 权损失零型与完整有限次数零型

给定 $\epsilon>0$，先固定 $J$，使
$$
eC_+^2g_J^2\le\epsilon.
$$
再在 (3.4) 中允许任意 $\sigma,\tau$。取
$C_{\epsilon,b}=\sqrt2e^{B_J}$，即得 (1.3)。

更准确地，对固定 $J$，
$$
\limsup_{\delta\downarrow0}
\delta\log^+
\sup_{\sigma-\tau=\delta}
\|G:H_\sigma\to H_\tau\|
\le eC_+^2g_J^2.
$$
随后令 $J\to\infty$ 即得 (1.4)。这个先后次序没有把 $B_J$ 当作一致有界常数。

若 $x\in\operatorname{Ran}\Pi_{\le q}$，则
$$
\|x\|_\sigma\le e^{\sigma q}\|x\|.
$$
在 (3.4) 取 $\tau=0$，得到
$$
\|Gx\|
\le\sqrt2
\exp\!\left(B_J+\sigma q+
\frac{eC_+^2g_J^2}{\sigma}\right)\|x\|.
\tag{4.1}
$$
固定 $J$。若 $g_J>0$，对充分大的 $q$ 取
$$
\sigma=\frac{\sqrt e\,C_+g_J}{\sqrt q}\le1.
$$
便有
$$
\limsup_{q\to\infty}
\frac{\log\|G|_{\operatorname{Ran}\Pi_{\le q}}\|}{\sqrt q}
\le2\sqrt e\,C_+g_J.
\tag{4.2}
$$
若 $g_J=0$，对每个固定 $q$ 在 (4.1) 令 $\sigma\downarrow0$，直接得到统一的有界上界。

最后 $J\to\infty$ 给 (1.5) 的上界。由于 $P$ 是收缩且 $PGx=x$，
$$
\|Gx\|\ge\|x\|
$$
对所有正指数输入成立；所以这些有限次数限制的范数至少为 $1$，对数非负，(1.5) 确是零极限。吸收有限多个低次数即得 (1.6)。

这里控制的是整个 $\operatorname{Ran}\Pi_{\le q}$，不只是某一列基向量，也与最高物理位置无关。

## 5. 任意小平方根次数权的真正原像

记 $\Pi_q$ 为次数恰为 $q$ 的正交投影。固定 $\epsilon>0$，由 (1.6) 取常数 $D_{\epsilon/2,b}$，使
$$
\|G\Pi_qf\|
\le D_{\epsilon/2,b}
e^{(\epsilon/2)\sqrt{q+1}}\|\Pi_qf\|.
\tag{5.1}
$$
每个 $\Pi_qf$ 都属于所有 $H_\sigma$，因此这里使用的 $G$ 是已经证明的实际逆，不是仅形式延拓。

若 $f\in\mathcal G_\epsilon$，则 Cauchy–Schwarz 给
$$
\begin{aligned}
\sum_{q\ge0}\|G\Pi_qf\|
&\le D_{\epsilon/2,b}
\left(\sum_{q\ge0}e^{-\epsilon\sqrt{q+1}}\right)^{1/2}
\left(\sum_{q\ge0}
e^{2\epsilon\sqrt{q+1}}\|\Pi_qf\|^2\right)^{1/2}\\
&=:K_{\epsilon,b}\|f\|_{\mathcal G_\epsilon}<\infty.
\end{aligned}
\tag{5.2}
$$
所以
$$
h=\sum_{q\ge0}G\Pi_qf
$$
在 $H$ 中绝对收敛。$P$ 有界，且逐层 $PG\Pi_qf=\Pi_qf$，故
$$
Ph=\sum_{q\ge0}\Pi_qf=f.
$$
这证明 $f\in\operatorname{Ran}P$。$P$ 的单射性保证 $h=P^{-1}f$ 唯一，而 (5.2) 正好给 (1.7) 的有界逆图范数。

整个论证只在有限次数层先使用已知逆，再由绝对收敛和 $P$ 的有界性构造一般 $\mathcal G_\epsilon$ 原像。没有把原指数尺度上的恒等式无证推广到更大的域。

## 6. 与有限混合附加因子的相容性

R230 逆测试附录 §9 已允许在 $P$ 外乘固定有限个有界复杂 first 预解式及非负 first 半群，并构造具有真实中间域的逆测试。

这些有限附加因子的逆成本也具有本文的权损失零型：

- 一个复杂 first 预解式的逆是 $\lambda+X_c$；R207 给成本
  $|\lambda|+C\|c\|_2\delta^{-1/2}$，其对数为 $o(1/\delta)$。
- 一个非负 first 半群的实际逆测试为 $e^{X_c}$。其真实指数尺度和逆关系已由 R240 半群附录证明。逐项正比较由同一个 $\mathcal M_c$ 控制，故本稿 (3.3)–(3.4) 的有限头与尾预算原样适用，也有 $o(1/\delta)$ 的对数成本。

有限个这些逆测试与 $G$ 复合时，把总权损失分成固定有限份；每个中间权保持严格为正，直到最后允许到达 $H$。各个 $o(1/\delta)$ 对数成本的有限和仍为 $o(1/\delta)$。已有有限混合逆关系不变。

因此对这样的有界混合乘积 $R$，其相容逆测试同样在有限次数层具有 $e^{o(\sqrt q)}$ 成本。第 5 节逐次数构造随即给
$$
\mathcal G_\epsilon\subseteq\operatorname{Ran}R
\qquad(\epsilon>0).
$$
本节没有假定一般复杂 first 生成有界半群，也不涉及复杂行的未经分类无穷乘积。

## 7. 范围与尚未完成的接口

本稿把 R230 的固定 $e^{O(\sqrt q)}$ 逆成本加强为 $e^{o(\sqrt q)}$，并从一个足够大的平方根次数权扩到每个任意小的正平方根次数权。没有重新登记已发表的 R240 配对反例。

这一像包含不等于全空间可逆，也不等于全部多项式次数光滑域都在像中；常数可以随 $\epsilon\downarrow0$ 任意变大。进一步降低次数权需要新的统一估计。

它同样不构造 $Q_mG=P$ 的有界尾因式，也不证明某个假想正正常慢理想湮灭见证满足 R244 的指定配对域。已知普遍配对反例和正则器的收缩强单位仍然相容。主问题的完成标准保持原样。

