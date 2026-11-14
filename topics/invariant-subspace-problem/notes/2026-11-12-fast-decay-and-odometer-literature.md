# 快幂衰减、径向 odometer 与经典定理适用性核查

日期：2026-11-12（北京时间）。分工：`universal_model`。本笔记针对 [R8](../results/R8-two-generator-quasinilpotent-model.md) 的 $T_\lambda=S+\lambda V$ 及 [R9](../results/R9-radial-odometer-and-nilpotent-approximants.md) 的标量 $A$，不是完整 ISP 的解答。

## 1. 当前结论与核查边界

目前核对到的快衰减、正算子和 weighted-composition 定理，没有直接给出这个 $A$ 的普通不变子空间。这个表述仅报告本次核查结果，不宣称已经穷尽文献，也不把尚未核对的技术假设当成不适用。

已经能严格排除的具体路线有：

- Atzmon 1980 Theorem 5 的一侧多项式预解式界：$A$ 的预解式范数径向对称，而任何固定多项式界都会迫使 $A$ 幂零。
- 直接寻找与 $A$ 交换的非零紧算子：已由 [R12](../results/R12-normalized-powers-and-compact-commutant.md) 排除。
- Foiaş–Jung–Ko–Pearcy 2004 Corollary 3.4 中从非零紧算子出发的有界交织链：§5 给出更强的排除证明。
- 用 $A$ 支配非零紧算子来应用正算子定理：§6 的局部性证明表明不存在这样的紧算子。
- 对目标向量 $1$、误差 $1/\sqrt2$，直接断言所有 backward-minimal-vector images 范数收敛：§7 的精确 dyadic 计算否定该断言。

这些是对特定证明机制的限制。没有从它们推出 $A$ 没有普通或超不变子空间。

## 2. Gaussian 幂界实际给出的预解式增长

设某有界算子 $T$ 满足

$$
\|T^n\|\le e^{-cn^2+Cn}\quad(n\ge0),\qquad c>0.
\tag{2.1}
$$

则 $T$ 拟幂零，并且对 $z\ne0$，范数收敛的 Neumann 级数给出

$$
\begin{aligned}
\|(zI-T)^{-1}\|
&\le\frac1{|z|}\sum_{n\ge0}
 \exp\bigl(-cn^2+(C+\log|z|^{-1})n\bigr)\\
&\le\frac{K_c}{|z|}
 \exp\left(\frac{(C+\log|z|^{-1})_+^2}{4c}\right).
\end{aligned}
\tag{2.2}
$$

最后一步由配方和移位 Gaussian 级数的一致有界性得到。等价地，整算子函数 $(I-\zeta T)^{-1}$ 的增长满足 $\log M(r)=O((\log r)^2)$，从而阶为零。

**这只是增长上界。** Atzmon [1, §5, Theorem 5] 除要求上半平面的指数界外，还要求另一半平面的多项式界

$$
\|(zI-T)^{-1}\|\le K|\operatorname{Im}z|^{-N}
\qquad(\operatorname{Im}z<0).
\tag{2.3}
$$

(2.2) 不提供 (2.3)。同篇 Proposition 4 是两类算子不变子空间问题之间的等价归约，不能引用为所有有限指数型预解式算子已有不变子空间。

作为范围校准，Müller–Zajac [2, Theorem 1] 构造了幂范数按任意预定速度衰减的非零拟幂零算子，并控制其交换子的自反性。其存在性构造不是一个对所有快衰减算子的普通不变子空间定理。这里也不从那篇例子推断任何“快衰减不足以保证 ISP”的反例结论。

## 3. $A$ 的旋转对称使一侧多项式界不可能

沿用 R9：

$$
(Af)(y)=w(y)f(y-1),\qquad
w(y)=a_{v_2(y)}>0\quad\text{a.e.},\qquad
a_r=e^{-10-B_r}.
\tag{3.1}
$$

对每个有限阶连续特征标 $\chi:\mathbb Z_2\to\mathbb T$，乘法算子 $U_\chi=M_\chi$ 是酉算子，且

$$
U_\chi A U_\chi^*=\chi(1)A.
\tag{3.2}
$$

这是因为 $\chi(y)\overline{\chi(y-1)}=\chi(1)$。数 $\chi(1)$ 包括所有阶为 $2$ 的幂的单位根，它们在单位圆中稠密。因而先对这些旋转用酉等价，再对固定 $z\ne0$ 用预解式的范数连续性，得到

$$
\boxed{\|(\rho e^{i\theta}I-A)^{-1}\|
\text{只依赖 }\rho>0.}
\tag{3.3}
$$

如果沿任意一条射线，在足够小的 $\rho$ 上存在

$$
\|(\rho e^{i\theta_0}I-A)^{-1}\|\le K\rho^{-N},
\tag{3.4}
$$

则 (3.3) 使该界在整个小圆上成立。Cauchy 系数公式给

$$
A^j=\frac1{2\pi i}\int_{|z|=\rho}z^j(zI-A)^{-1}\,dz,
\qquad
\|A^j\|\le K\rho^{j+1-N}.
\tag{3.5}
$$

固定整数 $j>N-1$ 并令 $\rho\downarrow0$，得到 $A^j=0$。但 $A$ 单射且作用在非零空间上，故不可能幂零。因此 (3.4) 不成立，尤其 (2.3) 对 $A$ 不成立。

这里排除的是算子预解式范数的一侧多项式控制；没有把这个结论推广成所有局部向量预解式方法均失效。

## 4. AF/UHF 归属与表示不能混用

R9 §3 已证明

$$
A_m=J_m\otimes I,\qquad J_m^{2^m}=0,
\qquad\|A-A_m\|=a_m\to0.
\tag{4.1}
$$

这把 $A$ 放进低位有限矩阵代数的范数闭包，也给出有限秩拟对角化。它没有提供一个收敛到非平凡投影的共同不变空间序列；R9 §5 及 [R10](../results/R10-ergodic-support-projection-obstruction.md) 已精确说明自然支集投影的退化。

这里 $L^2(\mathbb Z_2,\mu)$ 对应每一位参考向量 $(1,1)/\sqrt2$ 的纯乘积表示。若改用每一位参考向量 $(1,0)$ 的不完全张量积，则同一形式的有限进位矩阵会表现为带有明显尾子空间的单边加权移位：以有限个 $1$ 的二进位串编号 $e_n$，其作用是 $e_n\mapsto a_{v_2(n+1)}e_{n+1}$。该移位的值域闭包余维为 $1$，而当前 $A$ 的值域稠密，所以两者甚至不可能酉等价。有限因子标准 $L^2$ 表示的右乘交换子及内部投影结论，同样不能直接搬到当前表示。

R12 给出了一个当前表示内可直接检验的区别：若

$$
F_k=\frac{A^{2^k}}{\|A^{2^k}\|},
$$

则 $F_k\to I/2$ 于 WOT，且对 $f\ne0$ 有 $\|(F_k-I/2)f\|\to\|f\|/2$；这立即排除非零紧交换子。

## 5. 更一般的紧交织链也不能使用

Foiaş–Jung–Ko–Pearcy [3, Corollary 3.4] 给出的一个充分条件是：从非零紧算子 $J_0$ 出发，存在一致有界的非零算子序列 $(J_n)_{n\ge0}$，即 $\sup_{n\ge0}\|J_n\|<\infty$，满足

$$
J_{n-1}A=AJ_n\quad(n\ge1)
\tag{5.1}
$$

或反向关系。原文第 352 页明确要求 “bounded sequence”；第 353 页证明开头将整个序列统一缩放为压缩算子，也确认其含义是范数一致有界，而不是仅指每个 $J_n$ 单独为有界算子。这比紧交换子条件更宽。对当前 $A$，该条件仍然不可能成立。

**命题 5.1。** 不存在非零紧算子 $K$ 以及满足 $\sup_{n\ge1}\|L_n\|<\infty$ 的一致有界算子序列 $(L_n)_{n\ge1}$，使

$$
KA^n=A^nL_n\quad(n\ge1).
\tag{5.2}
$$

反向关系 $A^nK=L_nA^n$ 也不可能成立。

**证明。** 用 R12 的 $E_k$：它只在第 $k$ 位作用矩阵单位 $e_{10}$，且

$$
\|F_k-E_k\|=\eta_k:=a_{k+1}/a_k\to0.
$$

置 $Q_k=M_{\mathbf1_{\{b_k=0\}}}$。有 $Q_kE_k=0$，故 $\|Q_kF_k\|\le\eta_k$。将 (5.2) 取 $n=2^k$ 并归一化，得到

$$
\|Q_kKF_k\|=\|Q_kF_kL_{2^k}\|
\le\eta_k\sup_n\|L_n\|\to0.
\tag{5.3}
$$

固定 $f$，紧性及 $F_kf\rightharpoonup f/2$ 给 $KF_kf\to Kf/2$ 于范数。因此

$$
\left|\|Q_kKF_kf\|-\tfrac12\|Q_kKf\|\right|\to0.
$$

而 $Q_k\to I/2$ 于 WOT，故 $\|Q_kKf\|\to\|Kf\|/\sqrt2$。与 (5.3) 合并得到 $Kf=0$。$f$ 任意，矛盾。

对反向关系取伴随，使用 $F_k^*$、$E_k^*$ 以及第 $k$ 位为 $1$ 的投影，完全相同的论证给出结论。证毕。

迭代 (5.1) 得到 $J_0A^n=A^nJ_n$，所以命题确实排除了 [3] 的这一充分条件，而不只是紧交换子特例。

## 6. 正算子定理中的紧支配条件不成立

Abramovich–Aliprantis–Burkinshaw [4] 的相关结论要求正拟幂零算子支配一个非零紧算子。这里的支配指

$$
|Kf|\le A|f|\qquad(f\in H).
\tag{6.1}
$$

**命题 6.1。** 满足 (6.1) 的紧算子只能为零；将 $A$ 换成任何 $A^j$，$j\ge1$，结论仍然成立。

**证明。** 写 $A=M_wU$，其中 $(Uf)(y)=f(y-1)$ 是保测平移酉算子。令 $L=KU^{-1}$，则

$$
|Lg|\le w|g|.
\tag{6.2}
$$

若 $g$ 支持在可测集 $E$ 上，(6.2) 表明 $Lg$ 同样支持在 $E$ 上。将任意 $g$ 分为 $\mathbf1_Eg+\mathbf1_{E^c}g$，得到 $L$ 与每个 $M_{\mathbf1_E}$ 交换。设 $b=L1$；对简单函数有 $Lg=bg$，由稠密性和有界性推广至所有 $g\in H$。并且 $|b|\le w$，所以 $L=M_b$。

Haar 测度无原子。若 $b\ne0$，则存在 $\delta>0$ 和正测度集 $E$ 使 $|b|\ge\delta$ 于 $E$。把 $E$ 分成可数个正测度互不相交集合，在其上取归一化指示函数，就得到正交单位向量列，其 $M_b$ 像仍互相正交且范数至少 $\delta$。故 $M_b$ 不紧。由于 $K=M_bU$，紧性迫使 $b=0$。

$A^j$ 仍是有界非负权乘以保测平移，同一证明适用。证毕。

Anisca–Troitsky [5] 的另一个明确结论针对 $C_0(\Omega)$ 上的 interval-preserving 算子；本题的 Hilbert 范数不是那个范数。其在一般 Banach lattice 上的结果带有额外的紧化/子列条件，不能仅凭正性、拟幂零、单射、稠密值域就引用。

## 7. Minimal vectors 的精确 dyadic 非收敛

### 7.1 定义与可直接验证的公式

取 $f_0=1\in H$，$\varepsilon=1/\sqrt2$。令 $y_n$ 是满足

$$
\|A^ny_n-1\|\le\varepsilon
$$

的最小范数向量。因为 $A^n$ 值域稠密，该可行集非空；它闭且凸，Hilbert 投影定理保证唯一最小范数向量。

写 $A^nA^{*n}=M_{\Phi_n}$。这里 $\Phi_n>0$ 几乎处处。存在唯一 $\mu_n>0$ 使

$$
\int\frac{d\mu(y)}{(1+\mu_n\Phi_n(y))^2}=\frac12.
\tag{7.1}
$$

连续严格递减的左端从 $1$ 下降至 $0$，所以该参数确实存在。令

$$
r_n=(I+\mu_nA^nA^{*n})^{-1}1,
\qquad y_n=\mu_nA^{*n}r_n.
\tag{7.2}
$$

则 $1-A^ny_n=r_n$，且 $\|r_n\|=\varepsilon$。这个 $y_n$ 的最小性可以自证：若 $z$ 可行，则

$$
\|r_n-A^n(z-y_n)\|^2\le\|r_n\|^2,
$$

从而 $\operatorname{Re}\langle A^n(z-y_n),r_n\rangle\ge0$，于是

$$
\operatorname{Re}\langle z-y_n,y_n\rangle\ge0,
\qquad \|z\|^2\ge\|y_n\|^2+\|z-y_n\|^2.
$$

这也说明 (7.2) 与文献 [6, §2] 的 backward-minimal-vector 公式一致。

### 7.2 Dyadic 参数的标量方程

对 $n=2^k$，在 $y=r+2^kz$ 的 R9 分解中，

$$
\Phi_{2^k}(y)=C_k^2a_{k+v_2(z)}^2.
\tag{7.3}
$$

记

$$
u_k=\mu_{2^k}C_k^2a_k^2,
\qquad d_{k,s}=a_{k+s}/a_k.
$$

因为 $\mu\{v_2(z)=s\}=2^{-s-1}$，(7.1) 精确化为

$$
\boxed{\sum_{s=0}^{\infty}
 \frac{2^{-s-1}}{(1+u_kd_{k,s}^2)^2}=\frac12.}
\tag{7.4}
$$

其中 $d_{k,0}=1$、$0<d_{k,s}\le d_{k,1}=\eta_k\to0$（$s\ge1$）。

先证明

$$
u_k\longrightarrow\infty.
\tag{7.5}
$$

否则有子列 $u_k\le M$。对 $s\ge1$，求和部分沿该子列趋于 $\sum_{s\ge1}2^{-s-1}=1/2$，而 $s=0$ 项至少为 $1/(2(1+M)^2)>0$，与 (7.4) 矛盾。

再证明

$$
u_k\eta_k^2\longrightarrow0.
\tag{7.6}
$$

否则有 $\delta>0$ 及子列使 $u_k\eta_k^2\ge\delta$。由 (7.5)，$s=0$ 项趋于零；$s=1$ 项不超过 $1/(4(1+\delta)^2)$，剩余项之和不超过 $1/4$。这使 (7.4) 左端的上极限严格小于 $1/2$，再次矛盾。

### 7.3 Images 逼近独立高位指示函数

第 $k$ 位 $b_k(y)$ 就是 $z$ 的奇偶位。当 $b_k(y)=1$ 时，$v_2(z)=0$，由 (7.5)，$r_{2^k}(y)=1/(1+u_k)\to0$。当 $b_k(y)=0$ 时，$v_2(z)\ge1$，而 (7.6) 给出一致界

$$
\frac1{1+u_k\eta_k^2}\le r_{2^k}(y)\le1.
$$

因此

$$
\|r_{2^k}-\mathbf1_{\{b_k=0\}}\|_2\to0,
\qquad
\boxed{\|A^{2^k}y_{2^k}-\mathbf1_{\{b_k=1\}}\|_2\to0.}
\tag{7.7}
$$

不同二进位在 Haar 测度下独立，所以对 $k\ne\ell$，

$$
\|\mathbf1_{\{b_k=1\}}-\mathbf1_{\{b_\ell=1\}}\|_2
=\frac1{\sqrt2}.
\tag{7.8}
$$

故 $(A^{2^k}y_{2^k})_k$ 没有范数收敛子列，而弱极限为 $1/2$。特别地，整个序列 $(A^ny_n)_n$ 不范数收敛。

**未排除的部分。** [6, Theorem A] 允许选择其他指数子列，并同时要求相邻最小向量范数之比趋于零；还可以选择其他目标向量和误差。因此 (7.7) 仅否定上述固定目标与误差的全序列收敛，以及其 dyadic 子列的强紧性，不是对全部 minimal-vector 方法的否定。

### 7.4 不能省略 normal-type 条件

[6, Definition 2.1, Theorems 2.2、3.2] 对乘法算子 $A^nA^{*n}$ 另有比值排序和正则性要求；“所有这些算子都可交换”不是充分条件。[6, §4.4] 专门指出遍历 Bishop-type 情形不满足那里采用的严格比较关系。

对当前 odometer 可以不依赖一般遍历论就看到障碍。取 $h=w^2$，其最大值 $a_0^2$ 在奇数集达到。任意点沿整数平移无限多次落在奇数集，所以对任意 $t,r$，只要避开可数个分母为零的例外点，

$$
\limsup_{n\to\infty}\frac{h(t-n)}{h(r-n)}\ge1.
\tag{7.9}
$$

因此该文用 $\limsup<1$ 定义的严格比较关系在这里为空。不能从 Gaussian 幂衰减与 $A^nA^{*n}$ 为乘法算子直接调用其收敛定理。

## 8. 尚须核对的 centered 子类

本算子是 centered：每个 $A^nA^{*n}$ 和 $A^{*n}A^n$ 都是乘法算子，故这整个族两两交换。$|A|$ 的非零特征值为 $a_r$，每个具有无限重数。

Jung–Ko–Pearcy [7] 的出版社摘要明确只处理一个有附加结构的拟幂零子类，并引用 Paulsen–Pearcy–Petrović 1995 的 weakly-centered 结构定理。本次已核对出版社题名、页码和摘要；并由 `defect_route` 代理交叉检查作者所在机构库。Ewha 的[原始库记录](https://dspace.ewha.ac.kr/handle/2015.oak/248118)明确没有附属全文文件，出版社下载需要机构授权。最后一轮公开作者稿检索也未取得含完整额外假设的原文。因此此项的准确状态是：**适用性未核实**。不能写成“此定理覆盖 $A$”，也不能写成“已排除它覆盖 $A$”。这是后续接手时仍需补齐的文献条件。

## 9. 已核对的一手资料

1. A. Atzmon, *Operators which are annihilated by analytic functions and invariant subspaces*, **Acta Mathematica 144** (1980), 27–63，特别是 §5 Theorem 5、Corollary 8、Proposition 4。DOI：[10.1007/BF02392120](https://doi.org/10.1007/BF02392120)。[公开原文](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6271-11511_2006_Article_BF02392120.pdf)。正文只做文本核查，没有上传 PDF。
2. V. Müller and M. Zajac, *A quasi-nilpotent operator with reflexive commutant, II*, **Studia Mathematica 132** (1999), 173–177，Theorem 1。DOI：[10.4064/sm-132-2-173-177](https://doi.org/10.4064/sm-132-2-173-177)。[作者公开原文](https://users.math.cas.cz/~muller/zajac.pdf)。文中 “hyperreflexive operator” 指其交换子自反，不能与另一种定量距离定义混淆。
3. C. Foiaş, I. B. Jung, E. Ko and C. Pearcy, *On quasinilpotent operators, II*, **Journal of the Australian Mathematical Society 77** (2004), 349–356，Corollary 3.4。DOI：[10.1017/S1446788700014488](https://doi.org/10.1017/S1446788700014488)。[出版社原文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/18D61A8506E1642D98358B9E2384C451/S1446788700014488a.pdf/on-quasinilpotent-operators-ii.pdf)。
4. Y. A. Abramovich, C. D. Aliprantis and O. Burkinshaw, *Invariant subspace theorems for positive operators*, **Journal of Functional Analysis 124** (1994), 95–111。DOI：[10.1006/jfan.1994.1099](https://doi.org/10.1006/jfan.1994.1099)。本次核对的是出版社摘要中精确列出的紧支配结论，未据此虚构定理编号。
5. R. Anisca and V. G. Troitsky, *Minimal vectors of positive operators*, **Indiana University Mathematics Journal 54** (2005), 861–872。[期刊原始摘要](https://iumj.org/article/767/)。本次只使用其中明确列出的空间及附加条件，未声称已经核对其全部证明。
6. I. Chalendar, A. Flattot and J. R. Partington, *The method of minimal vectors applied to weighted composition operators*, in **The Extended Field of Operator Theory**, Operator Theory: Advances and Applications **171** (2006), 89–105。DOI：[10.1007/978-3-7643-7980-3_5](https://doi.org/10.1007/978-3-7643-7980-3_5)。核对了作者上传的完整预印本文本，特别是 §§2、4.4 及 Theorem A：[作者公开全文页](https://www.researchgate.net/publication/227192023_The_Method_of_Minimal_Vectors_Applied_to_Weighted_Composition_Operators)。预印本页首写 2005；此处出版年依 Springer 正式引文写 2006。
7. I. B. Jung, E. Ko and C. Pearcy, *Hyperinvariant subspaces for a class of quasinilpotent operators*, **Studia Mathematica 245** (2019), 289–296。DOI：[10.4064/sm171209-18-1](https://doi.org/10.4064/sm171209-18-1)。[出版社摘要](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/245/3/111414/hyperinvariant-subspaces-for-a-class-of-quasinilpotent-operators)。全文额外假设待核对。

本文件及 R12 都不对新颖性作判断。下一步若要从这些性质得到普通不变子空间，需要新的闭子空间构造，或一个已经完整核对、且其每个假设都能在当前表示中验证的定理。
