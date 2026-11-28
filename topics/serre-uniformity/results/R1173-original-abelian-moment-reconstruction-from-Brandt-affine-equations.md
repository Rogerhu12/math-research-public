# R1173：原两个 abelian 矩由超奇异仿射 Hecke 方程唯一恢复

日期：2026-11-28。  
会话：Astra-serre-24b8836b-20261126。  
状态：下述原 Norm、仿射右端与单位理想给出无 Bernoulli 门的有限重建定理。没有执行数学程序，没有把中央相关项或一般 $p$ 的排点结论认作已完成。

## 1. 结论与原规范

固定 $p>37$，沿 [R1171 §§2–5](R1171-original-affine-supersingular-Frobenius-reduction.md) 的同一有限域 $k$、$W=W(k)$、超奇异代表 $E_i$、自同构可延伸的参考提升 $\mathcal E_i$、原 Hodge frame 与 mod-$p^2$ quotient 标记。记原未平滑 moment 的 abelian Frobenius 坐标为
$$
\mathsf A_{4,i}=X_i,\qquad
\mathsf A_{8,i}=Y_i,\qquad
\mathbf A_d=(\mathsf A_{d,i})_i.
\tag{1173.1}
$$
这里是 R1147 的原 $\mathsf M_4,\mathsf M_8$，不是已经乘上 $k_d(2)=4-2^{-d}$ 的 raw $\theta_2$ 矩。primitive/all-vector 的整尺度沿 R1147 保留；模 $p$ 时其 $1-p^d$ 因子约化为一，不另乘一个 moment $d!$。

令
$$
\mathscr L=\{\ell>3\text{ 为素数}:\ell\ne p,\ \ell^6\not\equiv1\bmod p\}
\setminus\Sigma,
\tag{1173.2}
$$
其中 $\Sigma$ 是任意固定有限集，包含原固定辅助素数 $c$。该族与 R1171 §13 的三中央槽来源共用。

**定理。** 对 $d=4,8$，原参考向量 $\mathbf A_d$ 满足
$$
\boxed{\qquad
W_{\ell,d}\mathbf A_d=\mathbf D_{\ell,d},\qquad
W_{\ell,d}=(\ell+\ell^{-d})-T_\ell^{(d)}
\quad(\ell\in\mathscr L).
\qquad}
\tag{1173.3}
$$
每个 $\mathbf D_{\ell,d}$ 由 §4 的显示式给出，只使用参考曲线的实际 coefficient crystal、已知原 connection、实际 cyclic quotient 模 $p^2$ 的位置及同源 pullback。它不含任何未知 $\mathsf A_{d,i}$ 或中央 $F_0$。

这些实际算子在相同受限 Hecke order 中生成单位理想。因此存在有限个 $\ell_a\in\mathscr L$ 和几何 Hecke operators $C_{a,d}$，使
$$
\boxed{\qquad
\sum_aC_{a,d}W_{\ell_a,d}=1,\qquad
\mathbf A_d=\sum_a\overline C_{a,d}\mathbf D_{\ell_a,d}.
\qquad}
\tag{1173.4}
$$
这是原 abelian 参考输入的有限几何重建，不要求 $B_{p-3}$、$B_{p-5}$ 为单位，也不假设某个原 local/global 类非零。本文证明该公式及有限过程终止，未为某个数值 $p$ 实际运行它。

## 2. 已刊局部输入：小偶权 $p$-new 形式不含惯性端点对

使用 Breuil–Mézard，*Multiplicités modulaires et représentations de* $\mathrm{GL}_2(\mathbb Z_p)$ *et de* $\operatorname{Gal}(\overline{\mathbb Q}_p/\mathbb Q_p)$ *en* $\ell=p$，Duke Math. J. **115** (2002), 205–310。

其 [作者原文](https://www.imo.universite-paris-saclay.fr/~christophe.breuil/PUBLICATIONS/multiplicite.pdf) 的 Theorem 1.2、Theorem 4.2.4.7 和 Corollary 4.3.3.1 给出本篇需要的如下直接推论：
$$
\boxed{\quad
\begin{gathered}
2<k<p,\quad k\ \text{偶},\quad
f\text{ 为级别 }Np\text{ 的 }p\text{-new 本征尖点形式},\\
(p,N)=1,\quad\text{nebentypus 在 }p\text{ 平凡}
\quad\Longrightarrow\quad
(\bar\rho_f|_{I_p})^{\rm ss}\not\simeq
1\oplus\omega^{k-1}.
\end{gathered}
\quad}
\tag{1173.5}
$$

说明这一推论所需的全部范围。分类中若惯性是 niveau-one 的两个角色，其指数只可能为
$$
\{k/2,k/2-1\},\qquad
\{k/2-j,\ k/2+j-1\},
\quad -k/2+2\le j\le-1.
\tag{1173.6}
$$
它们均在 $[1,k-2]$。其余分支为 niveau-two 角色：写其指数为 $a+pb$，原表中的 $0\le a,b<p$ 且 $a\ne b$。因 $a+pb\equiv a-b\bmod(p+1)$，它不为 $p+1$ 的倍数，故不可能成为 $\omega=\omega_2^{p+1}$ 的幂。于是所有分支都排除 (1173.5) 的两个端点。此为从原分类逐项得到的结论，没有只用较弱的闭区间惯性权界。

Theorem 4.2.4.7 明取任意稳定格；不要求残表示不可约，也不要求系数域未分歧。作者 $\overline{\mathbb Q}_p,\overline{\mathbb Z}_p$ 的记号在文本抽取时上横线可能缺失；其 §1 首段及 §4.3.1 明确定义代数系数，故不能将其误读为只允许 $\mathbb Q_p$ 值本征形式。半稳定基域仍是 $\mathbb Q_p$。§4.3.3 明确用 $p$-new、character 在 $p$ 平凡得到半稳定非 crystalline；没有把 level-prime-to-$p$ 的 crystalline 分支混入。

其 §4.3.1 用 arithmetic Frobenius，给 $\operatorname{tr}\rho_f(\mathrm{Frob}_\ell)=a_\ell$、$\det\rho_f(\mathrm{Frob}_\ell)=\ell^{k-1}\chi(\ell)$。这与本篇的 $\omega$ 及 R1170 相同，不需要反转两个惯性指数。

## 3. 原 abelian 算子的受限 Hecke 单位理想

### 3.1 同一个有限整 Brandt 格与标准 Hecke 归一

沿 [R1170 §§2–4](R1170-original-supersingular-Brandt-common-kernel.md)，取
$$
\mathcal B_d=
\bigoplus_i\bigl(\operatorname{Sym}^d
                  H^1_{\rm crys}(E_i/W)\bigr)^{\operatorname{Aut}(E_i)},
\qquad d=4,8.
$$
原 coefficient convention 是
$$
T_\ell^{(d)}=\sum_{|C|=\ell}
                   \operatorname{Sym}^d(\psi_C^{-1}),
\qquad
\psi_C^{-1}=\ell^{-1}\phi_C^*,
\qquad
B_\ell=\ell^dT_\ell^{(d)}.
\tag{1173.7}
$$
实际晶体格、self-duality、同源方向及 characteristic-zero Jacquet–Langlands 谱均由 R1170 付清：标准 $B_\ell$ 的谱来自权 $k=d+2$、级别 $p$、trivial nebentypus 的 $p$-new 尖点形式。因 $d>0$，这里不含 quaternionic 常数 Eisenstein 部。

因此
$$
W_{\ell,d}
=\ell^{-d}\{\ell^{d+1}+1-B_\ell\}.
\tag{1173.8}
$$
右端的假想 Galois 系统是 $1\oplus\omega^{d+1}$，其 determinant 与权 $d+2$ 形式的 $\omega^{d+1}$ 一致。不能将它误写成 R1170 中某一中央槽的两个越界指数；本篇确需 §2 的更强端点排除。

### 3.2 真残余分支与受限 prime set

令
$$
\mathbb T_{d,\mathscr L}
=W[B_\ell:\ell\in\mathscr L]
\subset\operatorname{End}_W(\mathcal B_d).
$$
这是有限、无挠的交换 $W$-order。若 $(W_{\ell,d}:\ell\in\mathscr L)$ 是真理想，取其上的极大理想，并沿 R1170 §4 的 characteristic-zero 分支得到一个实际新形式 $f$、一个系数素理想 $\mathfrak p$，满足
$$
a_\ell(f)\equiv1+\ell^{d+1}\pmod{\mathfrak p}
\qquad(\ell\in\mathscr L).
\tag{1173.9}
$$
这里使用具体有限 order 在 characteristic-zero 谱乘积中的嵌入及 lying-over；没有假设任意模 $p$ 系统自动提升。限制到子 order 不损害这个事实。

取包含 $\bar\rho_f$ 和 $\omega$ 的共同有限 Galois quotient。Chebotarev 先将 (1173.9) 给到所有 $\omega(g)^6\ne1$ 的 $g$，有限 $\Sigma$ 不影响此步。再用 R1171 §13.3 的二维 trace 补全：若 $\omega(g)\in\mu_6$，取 $\omega(h)=a$ primitive，因 $p-1>12$，$h,gh,gh^2$ 都属已知范围。两表示具有相同 determinant，故
$$
t(gh^2)-t(h)t(gh)+\det(h)t(g)=0
$$
唯一补回 $t(g)$。由此
$$
\bar\rho_f^{\,\rm ss}\simeq1\oplus\omega^{d+1}.
\tag{1173.10}
$$
权 $k=d+2$ 为 $6$ 或 $10$，满足 $2<k<p$；级别正是 $p$、character 平凡。故 (1173.10) 与 (1173.5) 矛盾。

所以
$$
\boxed{\quad
(W_{\ell,d}:\ell\in\mathscr L)=\mathbb T_{d,\mathscr L},
\qquad
\bigcap_{\ell\in\mathscr L}\ker W_{\ell,d}=0
\quad\text{于 }\mathcal B_d/p,\qquad d=4,8 .
\quad}
\tag{1173.11}
$$
模 $p$ Hecke action 无须半单。单位理想本身给出有限证书 (1173.4)，比只排共同本征向量更强。

## 4. 原 Norm 与实际商曲线给不含未知 abelian 值的右端

### 4.1 从指定 Norm 点读取实际等式

[R1159 §§5.1–5.3](R1159-original-correlation-to-Hecke-cochain-comparison.md) 的原 product/Weil restriction 有给定的 quotient Norm 点。其交换商 kernel 的两个方程正是
$$
\sum_Cv_{C,d}=(\ell+\ell^{-d})v_{0,d},
\qquad d=4,8.
$$
同一原 filtered realization 的态射保持唯一 Hodge 点，故对原 Frobenius 读取
$$
\boxed{\quad
\sum_{|C|=\ell}\operatorname{Sym}^d(\psi_C^{-1})
             \mathsf A_d(\mathcal E_i/\mathcal C)
=(\ell+\ell^{-d})\mathsf A_{d,i}.
\quad}
\tag{1173.12}
$$
这里没有未知 central source，也没有 R1160 的算术 $B_n$。原同根 $\eta_d$ 并非被设成零；它已是给定 Norm trivialization 的 cocycle 表达，R1159 的群图正支付其到 Hodge 点的同一性。

所有 $\ell\in\mathscr L$ 均在 R1171 §10 已证明的整来源范围内。式 (1173.12) 没有反除 $\ell+1$、$k_d(\ell)$ 或一个含 $p$ 的分裂域次数。

### 4.2 独立于全部 $F_0$ 的 abelian 增量

R1171 (1171.10) 在该参考 chart 给
$$
R(\Delta_j(\xi))
=\bar C_j^{\rm c}
 \exp\bigl(\sigma(\xi L_j)\bigr)
 \exp\bigl(-\sigma(\xi L_j^{\rm c})\bigr)
 (\bar C_j^{\rm c})^{-1}.
\tag{1173.13}
$$
$\bar C_j^{\rm c}$ 是原纯 coefficient divided Frobenius；$L_j,L_j^{\rm c}$ 是已知 connection 的降一阶部分。两个 exponentials 有限，所有分母为单位；$\sigma(\xi L)=\xi^p\sigma(L)$ 仍保留。

定义
$$
\delta_{4,j}(\xi)=\Delta X_j(\xi),\qquad
\delta_{8,j}(\xi)=\Delta Y_j(\xi).
\tag{1173.14}
$$
这两个量既不含 $Z_{\rho,j}$，也不含 $X_j,Y_j,T_j$。原群右乘在 abelianization 上就是加法，所以对实际 quotient 的位置
$\xi_{i,C}=u_{i,C}/p\bmod p$，
$$
\mathsf A_d(\mathcal E_i/\mathcal C)
=\mathsf A_{d,j(C)}+\delta_{d,j(C)}(\xi_{i,C}).
\tag{1173.15}
$$
这里的增量方向是“参考提升到实际 quotient”，与 R1171 相同，不能反号。

代入 (1173.12) 即得 (1173.3)，且
$$
\boxed{\quad
D_{\ell,d,i}
=\sum_{|C|=\ell}
   \operatorname{Sym}^d(\psi_C^{-1})
       \delta_{d,j(C)}(\xi_{i,C}).
\quad}
\tag{1173.16}
$$
右端是正号。每个 quotient 的实际 differential scaling、$\eta$ shear 及可能的 Frobenius 重排均沿相同 correspondence 运输；未把各商曲线替成参考曲线后忘记第一 $p$ 位。

### 4.3 为什么这些是有限几何输入

(1173.16) 需要的输入正是：

- 有限多个 $E_i$、所选好约化参考提升及原适配 frame；
- 它们的实际 coefficient crystalline Frobenius 与 R1149 的 $E_6/E_{10}$ 连接；
- 有限个 $\ell$ 下的 cyclic quotient、mod-$p^2$ chart 位置及 $\ell^{-1}\phi_C^*$。

这些均可由实际曲线及其 coefficient cohomology 的有限计算读取。$\bar C_i^{\rm c}$ 不是原 unipotent torsor 的未知 Frobenius 矩阵；在 (1173.13) 中 full $F_i$ 已严格消去。不能把“已知 connection”替换为“可以任意重选一个同 connection 的格”，这里始终是 R1150、R1165–R1166 的原整比较。

自同构变换同时作用于 $\xi$、$\Delta$ 和 $\psi_C^{-1}$，由原自然性得到 $\mathbf D_{\ell,d}\in\mathcal B_d/p$，与 quotient 标记选择无关。这不是额外假定参考点之外的绝对 $F_0$ 约化不变。

## 5. 真实有限重建与对三中央槽的用途

把 (1173.16) 代入单位理想证书，(1173.4) 给原 $\mathbf A_4,\mathbf A_8$。如需一个完全有限的操作描述，可枚举 (1173.2) 中的素数，计算原有限格上的 Hecke matrices、已知 $\mathbf D_{\ell,d}$ 及它们生成的 operator 理想；(1173.11) 保证某一有限阶段包含恒等算子，届时同一证书给原向量。等价地，可叠加有限多组 (1173.3) 至共同 kernel 为零，再解该相容线性系统。相容性由原 moment 的实际存在给出，不是对任意右端的满射断言。

这里证明的是过程终止，不给所需素数统一大小界，也不宣称只用 $2,5$ 足够。本篇未运行该过程。与逐点原高 Hurwitz 公式相比，新增内容是把所有未知 abelian 参考值同时换成一个右端独立可读的有限几何系统。

原第三个 abelian 槽 $T_i$ 是从基域拉回的 $\gamma_5$，与超奇异参考点无关；在 [R1152 (1152.51)](R1152-original-global-Heisenberg-weight-eight-Frobenius-readout.md) 的同一 Tate frame 中，其值为
$$
T_i=s=\frac{24}{5}B_{p-5}\pmod p.
\tag{1173.17}
$$
允许此数为零；底域扩到 $W(k)$ 时沿同一原 Tate frame 和半线性 Frobenius base change，不给每个 $i$ 另选一个缩放。

此处须单独说明 $p$ 的范围。R1152 的完整 global Heisenberg 讨论以 $p>C_{\rm cyc}$ 为前提；本式只消费其 (1152.47)–(1152.50) 的 weight-five **abelian** 比较。原未平均的兼容加权 Kummer product 在同一 Tate generator 下直接给 depth-one 类
$-\gamma_{5,\infty}/[4!(1-p^4)]$。这个具体扩张的身份不要求 $\gamma_5$ 生成整个 global $H^1$，不要求其非零，也不使用 $\Theta$ 的中央唯一性。相同标准路径的安全 weight-five 有限 Frobenius 读数为
$b_p=-B_{p-5}/5$（R1152 (1152.37)–(1152.38)）；其所用整尾与分母在 $p>37$ 已满足。因而原 $\gamma_5$ 的坐标为 $-24b_p$，即 (1173.17)。这里是对这个 abelian 身份逐项核清后使用 $p>37$，没有删除 R1152 其它全局结论的 $C_{\rm cyc}$ 门。

因此 R1171 三槽仿射平移所需的 $(X_i,Y_i,T_i)$ 不再必须逐个以未知 unipotent period 输入：前两者由 (1173.4)，第三者由 (1173.17)。一旦这些有限几何数据读取完成，所有三中央槽的商位置修正都是具体已知量，包括最低 BCH 中的 $-\lambda_\infty\Delta X\,T_i/2$。

尚未由本篇自动给出的，是足够多辅助素数上的实际中央 $Z_{{\rm corr},\ell,\rho}$。尤其最低槽仍需 R1172 corrected 来源的独立局部读取；不能因其连续算术 primitive 存在便把它当作一个已读数。三中央向量非零性、global subtraction 的排点力及整个 $p$-盘提升均不由本篇的 abelian 单位理想推出。

## 6. 精确来源与核验范围

1. Breuil–Mézard 的 [作者 PDF](https://www.imo.universite-paris-saclay.fr/~christophe.breuil/PUBLICATIONS/multiplicite.pdf)：Theorem 1.2 在 PDF 第 4–5 页；任意稳定格的 Theorem 4.2.4.7 在第 49–50 页；§4.3.1 的 arithmetic Frobenius 约定在第 50 页，Corollary 4.3.3.1 在第 51–52 页。均已亲读上述段落。出版信息见 [作者正式目录](https://www.imo.universite-paris-saclay.fr/~christophe.breuil/publications.html)。使用的是已刊 2002 年结果，不是一个关于一般高权约化的条件性 zigzag 命题。
2. R1170：原完整有限格、$B_\ell=\ell^dT_\ell$、实际 JL 谱及 finite-order residual 分支。本篇不重新假设 eigenform lift。
3. R1159 §5、R1171 §§3–5、10–13：指定 Norm 点、同源与 Hodge 相容、原有限半线性 Taylor、restricted-prime 全源及 trace 补全。
4. R1152 §13：原 $\gamma_5$ 的绝对 Tate 规范；本文没有由一个可能为零的值倒除以校准任何整线。

本文的新增证明是端点排除在原 abelian Brandt 算子上的使用，以及 (1173.12)–(1173.16) 将该单位理想接到原实际 moment 的非齐次方程。全部为纸面证明与来源核对；无数学程序执行。

root另逐页核了作者PDF第49–52页的稳定格、全分类及arithmetic Frobenius约定，并核作者出版目录；原Norm/仿射正号及weight-five独立范围由root与global_route分别纸核。
