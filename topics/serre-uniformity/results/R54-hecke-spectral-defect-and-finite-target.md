# R54. Hecke 谱缺陷向量：积分核的共同根与坏纤维有限靶集

日期：2026-11-12。会话：serre-uniformity-astra-resume2；qc_global。

**状态：已证明。** 本文把 R45–R47 的全部真实高度方程放回一个明确的 Hecke 谱向量。结论不仅是一个维数估计：R45 的积分核共同根恰对应谱向量落入坏纤维数据的线性包；而有理点必须落入这个线性包中的一个**有限靶集**。取积分核时丢掉的正是这部分离散数据，可以用至多 $n-1$ 个补充方向恢复。

设 $T_A=e_A\mathbb T_{\mathbb Q}\simeq\prod_fK_f$，其单位为 $1_A=e_A$，维数为 $a$；令
$$W=\ker(\operatorname{Tr}_{T_A/\mathbb Q}:T_A\to\mathbb Q),
\qquad\dim W=a-1.$$
对 R45 的整数格 $\Lambda_A\subset W$，记实际垂直障碍为
$$\Phi_A:\Lambda_A\longrightarrow\mathbb Z^n/\mathbb Z\mathbf1,
\qquad\mathcal K_A=\ker\Phi_A.$$
固定一个参考坏分量 $i_0$。本文构造由完整垂直系数决定的 $\beta_i\in W$，满足 $\beta_{i_0}=0$，并构造实际解析谱缺陷
$$\Delta_\ell:X(\mathbb Q_\ell)\longrightarrow W\otimes\mathbb Q_\ell.$$
其准确结论是
$$\boxed{\quad
\Psi_G(x)=0\text{ 对全部 }G\in2\mathcal K_A
\iff
\Delta_\ell(x)\in C_\ell,
\quad C_\ell=\operatorname{span}_{\mathbb Q_\ell}\{\beta_i\}.
\quad}\tag{0.1}$$
这里
$$\dim C_\ell=\operatorname{rank}\Phi_A\le n-1.$$
而对有理点有更强的必要条件
$$\boxed{\quad
\Delta_\ell(x)=-\log_\ell(p)\,\beta_i
\quad\text{对某个 }i\text{，即 }x\text{ 在坏 }p\text{ 处实际到达的分量。}
\quad}\tag{0.2}$$

因此全部有理点属于有限个向量等式的联合，而不仅满足 (0.1)。本文不证明这个有限靶集的逆像只有 CM 点；(0.2) 仍是必要条件，不是有理性的充分条件。

## 1. 从整个 trace-zero 商方向开始

本题只需在 $X(\mathbb Q)\ne\varnothing$ 的分支继续研究；无有理点的分支已经满足当前层的排除目标。在非空分支中，R45 §4 给出秩 $a-1$ 的实际整数格 $\Lambda_A\subset W$，已统一清除同源与 Chow–Heegner 挠投影所需的有限分母。对每个 $F\in\Lambda_A$，对应及规范平移都消去互补商 $B$。

注意这里用的是整个 $\Lambda_A$，尚未取 $\Phi_A$ 的核。对
$$G=2F$$
只乘二一次。其实际积分线丛是
$$\mathscr L_F=(u_D,2h_{D,F}u_D)^*\mathcal P^{\rm ext}
\quad\text{于坏模型的光滑开集 }U,$$
泛纤维即 R47 的 $L_{D,G}$。选 $\Lambda_A$ 的一个整数基，为基元选实际有理截面，再按 Poincaré 双扩张群律作张量积，得到对 $F$ 可加的截面族 $s_G$。在展开几何分量的有限非分歧扩张上写
$$\operatorname{div}_U(s_G)=\sum_{i=1}^n k_i(F)U_i,
\qquad k_i(F)\in\mathbb Z.$$
每个 $k_i$ 对 $F$ 为整数线性函数，且
$$\Phi_A(F)=[(k_i(F))_i].$$
这里 $k_i(F)$ 是**完整实际截面的垂直阶**。它包含一般 Hecke 对应在 R33 中的尖点范数缺陷；不把该缺陷设为零，也不把小次数 $T_2$ 的支集结论移到 $e_A$ 投影后。

取参考几何分量 $i_0$，定义
$$b_i(F)=k_i(F)-k_{i_0}(F),\qquad b_{i_0}=0.
\tag{1.1}$$
这些差与最初有理截面的标量选择无关。它们都是定义于 $\mathbb Q$ 的 $W$ 上线性泛函；从整数格延拓到 $W$ 无歧义。

## 2. 全局有理截面的一致归一化

在每个好素数 $q\ne p$，R47 的光滑模型论证给
$$\operatorname{div}_{\mathcal X_q}(s_G)=m_q(F)\mathcal X_{q,s},
\qquad m_q(F)\in\mathbb Z.$$
几乎所有 $m_q(F)$ 为零，且对 $F$ 可加。于是用有限有理数
$$c_F=p^{-k_{i_0}(F)}\prod_{q\ne p}q^{-m_q(F)}$$
归一化
$$\widetilde s_G=c_Fs_G.
\tag{2.1}$$
这给一个全局有理、与加法相容的截面族。在好素数处全部垂直阶为零；在坏 $p$ 处的阶恰为 $b_i(F)$。所有乘数都是有理数，故没有逐局部选择不相容常数的问题。

固定辅助素数 $\ell\ne p$ 和 R47 的同一圆分字符、同一 Hecke 相容 Poincaré splitting。对 $q\ne p,\ell$，
$$\lambda_q(\widetilde s_G(x))=0.$$
所有 $x\in X(\mathbb Q_p)$ 都落在 $U$，见 R43。因此若 $x$ 落在分量 $i$，则直接由积分双扩张 splitting 得
$$\lambda_p(\widetilde s_G(x))
=b_i(F)\chi_p(p)
=-b_i(F)\log_\ell(p).
\tag{2.2}$$
式 (2.2) 没有额外的 $1/2$：$\mathscr L_F$ 已经是 $G=2F$ 的线丛。若改用 R43 中未乘二的 $H_{D,F,p}$，才会出现该文的 $1/2$。

当 $F\in\mathcal K_A$ 时，全部 $b_i(F)=0$，(2.1) 恰给 R47 的所有非辅助局部项恒零归一化。因此下面的全空间方程限制到积分核后，就是 R47 已固定的真实方程。

定义
$$\begin{aligned}
\mathcal Q_F(x)
={}&\sum_f\operatorname{Tr}_{K_f\otimes\mathbb Q_\ell/\mathbb Q_\ell}
\bigl(c_fz_f(x)(2F_fz_f(x)-\xi_{2F,f})\bigr)\\
&-\lambda_\ell(\widetilde s_{2F}(x)),
\qquad x\in X(\mathbb Q_\ell).
\end{aligned}\tag{2.3}$$
全部 $z_f$、$c_f$ 和 $\xi$ 与 R47 相同；只把原来限于核中的截面归一化延伸到了全部 $\Lambda_A$。

### 引理 1：完整方向的共同有限分支

$F\mapsto\mathcal Q_F$ 为 $\mathbb Q$ 线性，延拓后为 $W\otimes\mathbb Q_\ell$ 到局部解析函数的 $\mathbb Q_\ell$ 线性映射。若 $x\in X(\mathbb Q)$ 在坏 $p$ 处落于分量 $i$，则
$$\mathcal Q_F(x)=-\log_\ell(p)b_i(F)
\quad\text{对全部 }F\in W.
\tag{2.4}$$

**证明。** 规范平移与对应可加；全局高度为双线性；归一化截面按张量群律相容，故辅助局部高度也对方向可加。先从整数格延拓到有理空间，再到 $\mathbb Q_\ell$，得到线性性。

对有理点，R47 的同一全局 Poincaré 高度恒等式给“全局项减辅助局部项”等于所有非辅助项之和。由 (2.1)–(2.2)，只有坏 $p$ 一项保留，恰为右边。一个有理点使用的是同一个分量 $i$，不能对每条方程单独选一个分量。证毕。

## 3. 迹配对与有理坏纤维谱向量

有限可分代数 $T_A$ 的迹配对
$$\langle u,v\rangle=\operatorname{Tr}_{T_A/\mathbb Q}(uv)$$
非退化，而且 $W^\perp=\mathbb Q1_A$。因为 $\operatorname{Tr}(1_A)=a\ne0$，有正交直和
$$T_A=\mathbb Q1_A\oplus W.$$
因此迹配对限制到 $W$ 仍非退化。定义投影
$$\pi_0(t)=t-\frac{\operatorname{Tr}(t)}a1_A.
\tag{3.1}$$
所有式子都在特征零中使用；$\ell\mid a$ 时仍合法，不添加整数单位假设。

对每个分量 $i$，存在唯一 $\beta_i\in W$ 使
$$b_i(F)=\operatorname{Tr}(F\beta_i)
\quad(F\in W).
\tag{3.2}$$
这给 $\beta_{i_0}=0$。它们由实际坏纤维数据确定。具体地，取有理基 $F_1,\ldots,F_{a-1}$，形成可逆 Gram 矩阵
$$M_{rs}=\operatorname{Tr}(F_rF_s).$$
把 $\beta_i$ 在此基中的坐标写作列向量，则其值恰为
$$M^{-1}\bigl(k_i(F_r)-k_{i_0}(F_r)\bigr)_r.
\tag{3.3}$$
这是明确的有限有理线性代数公式，不要求先得到某个低分母基。

令
$$C=\operatorname{span}_{\mathbb Q}\{\beta_i:1\le i\le n\}\subset W.$$
参考坐标给出单射
$$\mathbb Q^n/\mathbb Q\mathbf1\longrightarrow\mathbb Q^{n-1},
\quad[k]\longmapsto(k_i-k_{i_0})_{i\ne i_0}.$$
所以 $b_i$ 的张成空间就是 $\Phi_A\otimes\mathbb Q$ 的对偶像。由非退化迹配对，
$$\boxed{\quad C=(\mathcal K_A\otimes\mathbb Q)^\perp,\qquad
\dim C=\operatorname{rank}\Phi_A\le n-1.\quad}
\tag{3.4}$$
这里正交取在 $W$ 内。如果使用 $T_A$ 代替 $W$，则正交空间多出标量直线 $\mathbb Q1_A$，维数至多 $n$；把 trace-zero 商遗漏会产生一个多余维度。

## 4. 实际解析谱缺陷的完整公式

由引理 1 及迹配对，存在唯一的解析映射
$$\Delta_\ell:X(\mathbb Q_\ell)\longrightarrow W_\ell:=W\otimes\mathbb Q_\ell$$
满足
$$\mathcal Q_F(x)=\operatorname{Tr}(F\Delta_\ell(x))
\quad(F\in W_\ell).
\tag{4.1}$$
这不是只给一个未知“抽象类”；下面写出其真实全局项与局部项。

记
$$R=T_A\otimes\mathbb Q_\ell=\prod_f(K_f\otimes\mathbb Q_\ell),\qquad
z(x)=(z_f(x))_f,\qquad c=(c_f)_f.$$
由 R47 的秩一 Mordell–Weil 坐标和规范平移的加法性，
$$\Xi:W\longrightarrow T_A,\qquad F\longmapsto(\xi_{2F,f})_f$$
是有理线性映射。把它延拓为
$$\Xi_0=\Xi\circ\pi_0:T_A\longrightarrow T_A.$$
记 $\Xi_0^*$ 为对迹配对的伴随。由于 $\Xi_0(1_A)=0$，有
$$\operatorname{Tr}(\Xi_0^*(t))
=\operatorname{Tr}(t\Xi_0(1_A))=0,$$
所以 $\Xi_0^*$ 的像在 $W$ 内。

定义**完整辅助局部高度谱向量** $\mathbf H_\ell(x)\in W_\ell$，使
$$\lambda_\ell(\widetilde s_{2F}(x))
=\operatorname{Tr}(F\mathbf H_\ell(x)).
\tag{4.2}$$
它由 (3.3) 相同的 Gram 逆矩阵应用到真实局部高度值求得，含有全部迭代积分。

### 定理 2：谱公式

有恒等式
$$\boxed{\quad
\Delta_\ell(x)=2\pi_0(cz(x)^2)
-\Xi_0^*(cz(x))
-\mathbf H_\ell(x).
\quad}\tag{4.3}$$

**证明。** 对 $F\in W_\ell$，全局项为
$$2\operatorname{Tr}(Fcz^2)-\operatorname{Tr}(cz\Xi(F)).$$
第一项可将 $cz^2$ 替换为 $\pi_0(cz^2)$，因为 $\operatorname{Tr}(F)=0$。第二项由伴随定义等于 $\operatorname{Tr}(F\Xi_0^*(cz))$。减去 (4.2)，再用迹配对非退化性即得 (4.3)。证毕。

式中的 $2$ 来自明确的 $G=2F$，而不是重新乘二；$\Xi$ 本身已经按 $2F$ 定义。$d=(p-1)/2$ 也已经包含在 $z(x)$ 的实际 $u_D$ 坐标中，不在外面重复乘 $d^2$。

## 5. 核条件、有限靶集，以及被取核丢掉的约束

记
$$I_p=\{i:\text{存在 }x_p\in X(\mathbb Q_p)\text{ 在 }U_i\text{ 的光滑处特化}\}.$$
若 $I_p=\varnothing$，则 $X(\mathbb Q_p)=\varnothing$，从而有理点为空。一般有 $|I_p|\le n$；这里不把全部几何分量自动当成 $\mathbb Q_p$ 可达分量。

置
$$\kappa_\ell=-\log_\ell(p),\qquad
\mathcal B_p=\{\beta_i:i\in I_p\}\subset C.$$
对不同素数 $p\ne\ell$，$\log_\ell(p)\ne0$。确实，$p$ 是 $\ell$ 进单位，而标准 $\ell$ 进对数在单位群上的核是有限的根单位群；正有理素数不可能为根单位。因此也可以改用
$$\delta_\ell=\Delta_\ell/\kappa_\ell,$$
使靶集本身为有理向量，不携带对数因子。这个除法不声称整数可逆性；R48 已说明特征零共同根无需这一附加条件。

### 定理 3：准确的共同根接口

有
$$\begin{aligned}
Z_{\rm ker}&:=\{x:\Psi_G(x)=0\text{ 对全部 }G\in2\mathcal K_A\}
=\Delta_\ell^{-1}(C_\ell),\\
Z_{\rm all}&:=\Delta_\ell^{-1}(\kappa_\ell\mathcal B_p)
=\delta_\ell^{-1}(\mathcal B_p),\\
X(\mathbb Q)&\subseteq Z_{\rm all}\subseteq Z_{\rm ker}.
\end{aligned}\tag{5.1}$$
这些等式和包含都是关于同一实际局部高度、同一全局归一化的陈述。

**证明。** 对核中方向，(2.3) 是 R47 的 $\Psi_{2F}$。由 (4.1)，全部核方向在 $x$ 消失恰意味着 $\Delta_\ell(x)$ 与 $\mathcal K_A\otimes\mathbb Q_\ell$ 正交。由 (3.4) 得第一式。引理 1 的所有方向等式及 (3.2) 给
$$\operatorname{Tr}(F\Delta_\ell(x))
=\kappa_\ell\operatorname{Tr}(F\beta_i)
\quad(F\in W_\ell)$$
对每个有理点成立。非退化性给向量等式 $\Delta_\ell(x)=\kappa_\ell\beta_i$，证明有理点包含。有限靶集包含在线性空间 $C_\ell$ 中，给最后包含。证毕。

**恢复离散约束的精确规模。** 令 $r=\operatorname{rank}\Phi_A$，取
$$W=(\mathcal K_A\otimes\mathbb Q)\oplus W_1,\qquad\dim W_1=r.$$
先解核方向，已知 $\Delta_\ell(x)\in C_\ell$。再取 $W_1$ 的任意有理基 $F'_1,\ldots,F'_r$；其评价
$$\bigl(\mathcal Q_{F'_s}(x)/\kappa_\ell\bigr)_{s=1}^r$$
必须属于已确定的联合有限集
$$\left\{\bigl(b_i(F'_s)\bigr)_{s=1}^r:i\in I_p\right\}.
\tag{5.2}$$
因为迹配对把 $C$ 与 $W_1^\vee$ 同构，(5.2) 与完整向量条件等价。只需 $r\le n-1$ 个补充方向；但是必须保留联合靶集，不能将每条方程的值集合独立作笛卡尔积。

## 6. 归一化不变性与方程强度的准确范围

### 6.1 换参考分量只平移同一个有限靶问题

把参考分量由 $i_0$ 换成 $j$，则
$$\beta_i'=\beta_i-\beta_j.$$
新截面为旧截面乘 $p^{-b_j(F)}$，因而辅助局部高度变化为 $-b_j(F)\log_\ell(p)$。所以
$$\Delta_\ell'=\Delta_\ell-\kappa_\ell\beta_j.
\tag{6.1}$$
左右两边的有限靶集随同一个平移变化，$Z_{\rm all}$ 不变。又 $\operatorname{span}\{\beta_i-\beta_j\}=C$，故 $Z_{\rm ker}$ 也不变。

改变 Mordell–Weil 基或有理 Hecke 基只是重新表达 (4.1)，不改变其内在泛函。R49 命题 2A 的证明适用于整个 $W$：它只用对应和平移消去 $B$、以及 R47 的对数满秩，不使用 $\Phi_A(F)=0$。因此改变 Hecke 相容 Hodge splitting 也不改变这里的 $\Delta_\ell$。

### 6.2 全方向仍为真正独立的解析条件

R49 对实际线丛的证明同样适用于全部 $W$：辅助局部曲率和 NS 类的独立性不受非辅助高度的常数分支影响。因此对 $W$ 的一组有理基，$a-1$ 个真实函数 $\mathcal Q_F$ 与全部全纯积分仍在每个非空圆盘上代数独立。减去任何一个固定有限靶值也保持这种独立性。

这保证 (5.2) 不是把恒等式重写成新条件；它确实恢复了积分核中省掉的方向。但不能因此断言 $Z_{\rm all}\subsetneq Z_{\rm ker}$ 对每个水平都严格，更不能断言有限靶逆像等于有理点或 CM 点。

### 6.3 仍需解决的算术问题

目前已知的坏纤维数据决定 $\beta_i$，实际全局与辅助高度决定 $\Delta_\ell$。下一项明确的目标是证明：对非 CM 候选，有没有可能满足
$$\Delta_\ell(x)\in\kappa_\ell\mathcal B_p$$
并同时满足其他素数与全局 Galois 条件。

本文没有计算一般层的全部 $c_f$、$\Xi$ 或辅助迭代积分，也没有从维数推出其值避开有限靶集。它将原来“核的共同根位于低维空间”的必要条件加强为“全部容许方向位于已确定的有限靶集”的必要条件，并精确指出恢复这一离散信息所需的方向数。这个加强不额外假设统一整数指数、单位导数或高度非退化。

## 7. 来源与依赖

- [R45](R45-heegner-quotient-integral-directions.md) §4 给整个 $\Lambda_A$、实际 $\Phi_A$、互补商上的 Chow–Heegner 消失及完整垂直系数接口。
- [R47](R47-heegner-logarithms-global-height.md) §§3–5 给实际对数坐标、Hecke 平衡高度的迹表示、归一化截面与同一 splitting 的符号。本结果将其归一化从核延伸到全部方向，保留一个共同坏分量分支。
- [R43](R43-neron-height-from-integral-correction.md) §1 的积分 Poincaré splitting 和 §3 的局部点落在 $U$，确保 (2.2) 是真实局部高度。
- [R48](R48-analytic-saturation-and-root-certificates.md) 说明上述有理基、迹投影和对数标量除法不需要统一整数指数作为共同根问题的逻辑前提。
- [R49](R49-independent-qc-functions-and-saturated-degree.md) 的实际 NS 匹配与 Besser–Müller–Srinivasan Theorem 7.9 给 §6.2；其命题 2A 给相容 Hodge splitting 不变性。BMS 原文：[最终版](https://arxiv.org/abs/2112.03873v4)，[作者全文](https://padmask.github.io/QuadraticChabauty.pdf)，Theorem 7.9、Lemma 7.12，作者版本 pp.51–53。

本结果的迹伴随公式、正交空间识别、参考分量平移和有限靶集恢复均已在正文证明，不调用新的未证明文献输入。
