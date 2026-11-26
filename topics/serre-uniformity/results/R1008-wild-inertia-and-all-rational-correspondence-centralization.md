# R1008：原六次覆盖全部有理对应的三阶甲板中央化

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；global_route / root。

**状态：已证明。** 本篇把 R1007 的甲板相容假设推广到原曲线的每个
$\mathbb Q$-有理 Jacobian 自同态，覆盖非 CM 和旧形式成分。
同一结论适用于 R587 实际偶分支的全部 $X_d$。
因此在 R1007 的同一整高度、自伴性与特征条件下，
另找一个不与甲板交换的有理自对应不能绕开赋值一障碍。
这没有排除底曲线高度项，也没有给出 Serre 一致性的参数上界。

## 1. 原对象及定理

固定素数 $p>37$。使用光滑射影正规化，置
$$
X_d=\operatorname{Norm}
 \bigl(X_{\rm ns}^+(p)\times_j\mathbb P^1_b\bigr),
\qquad j=6912\,d b^3(1-d b^3),
\qquad J_d=\operatorname{Jac}(X_d).
\tag{1008.1}
$$
在 $K=\mathbb Q(\zeta_3)$ 上记三阶甲板变换为
$\delta_d:b\mapsto\zeta_3b$，其 Jacobian 推前仍记 $\delta_d$。
原第一曲线是 $X_1$；原第二曲线的 $d$ 满足 R587 的实际条件，
特别是 $d\in\mathbb Q_3^{\times3}$。两者的 $b=0$ 基点由甲板固定。

**定理。** 若 $d\in\mathbb Q^\times$ 且 $d\in\mathbb Q_3^{\times3}$，
则对每个 $Z\in\operatorname{End}_{\mathbb Q}(J_d)$，
$$
\boxed{Z\delta_d=\delta_d Z
 \quad\text{于 }\operatorname{End}_{\overline{\mathbb Q}}(J_d).}
\tag{1008.2}
$$
同样适用于 $\operatorname{End}_{\mathbb Q}^0(J_d)$。
这里是整个 Jacobian 的断言，不只针对 R575 的 CM 商。
证明由一个实际野惯性算子给出。

## 2. canonical 模曲线的全 $H^1$ 在三处无野分歧

先取
$$
X_4:\quad j=2^{10}3^3u^3(1-4u^3).
\tag{1008.3}
$$
Brau–Jones 的 level $6$ 模曲线具有这个准确的 $j$ 映射；
其模子群是
$$
H_6=\{(\vartheta(g),g):g\in\operatorname{GL}_2(\mathbb F_3)\}
 \subset\operatorname{GL}_2(\mathbb F_2)\times
       \operatorname{GL}_2(\mathbb F_3),
\quad \ker\vartheta=Q_8.
\tag{1008.4}
$$
与 level $p$ 的真实非分裂正规化子取 CRT 乘积，
得到 (1008.3) 的 canonical fiber product 模曲线。
这里的 $X_4$ 不能与原 $X_1$ 的有理模型混同；
二者的三次扭曲正是后面所需的差别。

令 $U\subset\operatorname{GL}_2(\mathbb A_f)$ 是相应紧开子群。
虽然 level $6$ 条件将二、三处分量关联起来，$U$ 仍包含
仅三处分量非恒等的子群
$$
K_3(1)=1+3M_2(\mathbb Z_3).
\tag{1008.5}
$$
因为其模三约化为单位，(1008.4) 的模二分量亦可取单位。
其他素数分量取单位即可。

取 Tate 素数 $5$。紧模曲线的整个
$H^1_{\mathrm{\acute et}}(X_{4,\overline{\mathbb Q}},
\overline{\mathbb Q}_5)$ 由所有出现的权二尖点自守表示分解；
每项的重数空间是相应 $\pi_f^U$。
采用对偶或 Tate 扭曲的另一规范不影响三处的野惯性。
这个全 $H^1$ 分解包括旧形式、非 CM 形式及所有重数，
不是先投影到某个 CM 因子后的结论。

若 $\pi_f^U\ne0$，由 (1008.5) 必有
$\pi_3^{K_3(1)}\ne0$。
Miyauchi–Yamauchi Theorems 1.1–1.2 在
$F=\mathbb Q_3,n=2,m=1$ 给出以下全部情形：

- 若 $\pi_3=\operatorname{Ind}(\chi_1,\chi_2)$ 为主系列，
  两个字符的导子指数各不超过一。
- 若 $\pi_3=\chi\otimes\operatorname{St}$ 为特殊表示，
  $c(\pi_3)\le2$，故 $\chi$ 的导子指数不超过一。
- 若 $\pi_3$ 超尖点，则 $c(\pi_3)\le2$。

现在逐项说明这确实杀掉野惯性，而不是只给一个总导子界。
主系列的两个 Weil 字符在 $1+3\mathbb Z_3$ 上平凡，
所以野惯性作用平凡。特殊表示中，$\chi$ 也驯分歧；
其非零单值算子经五进驯惯性参数作用，
而 pro-$3$ 的野惯性到 $\mathbb Z_5$ 的连续加法同态为零。
所以该情形的真实五进表示在野惯性上仍为单位。

超尖点情形的二维 Weil 表示 $r$ 不可约且单值算子为零。
其惯性不变量必须为零：不变量空间由 Weil 群保持；
若非零则不可约性迫整个表示惯性平凡，
但在代数闭系数域上，无分歧 Weil 群的不可约表示只能一维。
因此
$$
c(r)=2+\operatorname{Swan}(r)\le2,
$$
从而 $\operatorname{Swan}(r)=0$，野惯性也平凡。

Carayol 的局部—整体相容性将上述 Weil–Deligne 参数
与每个实际五进 Galois 成分对应。
Frobenius 半单化不改变其惯性限制；
特殊表示的单值部分已在上段单独处理。
因此没有从局部半单化错误推出实际表示无野分歧的问题。
从全 $H^1$ 分解得到
$$
\boxed{\rho_4(P_3)=1
 \quad\text{于 }V_5(J_4),}
\tag{1008.6}
$$
其中 $P_3$ 是三处绝对 Galois 群的野惯性。
所用已发表输入的准确定位列于文末。

## 3. 原三次扭曲将甲板变换变为野惯性算子

取 $\alpha^3=4$。令 $t=\alpha-1$，则
$$
t^3+3t^2+3t-3=0.
\tag{1008.7}
$$
这是在三处的 Eisenstein 多项式，
所以 $\mathbb Q_3(\alpha)/\mathbb Q_3$ 全分歧三次。
$\mathbb Q_3(\zeta_3)/\mathbb Q_3$ 全分歧二次且驯分歧。
二者次数互素；合成域
$$
L_3=\mathbb Q_3(\zeta_3,\alpha)
$$
是全分歧次数六的分裂域，其 Galois 群为 $S_3$。
野惯性在此有限商中的像为三阶正规子群。
故可选 $\sigma\in P_3$ 满足
$$
\sigma(\zeta_3)=\zeta_3,\qquad
\sigma(\alpha)=\zeta_3\alpha.
\tag{1008.8}
$$

先看 $d=1$。真实几何同构为
$$
\iota_1:X_1\longrightarrow X_4,\qquad u=a/\alpha,
\qquad \sigma(\iota_1)=\delta_4^{-1}\iota_1.
\tag{1008.9}
$$
它与甲板作用相容。
协变 Tate 模上的运输公式为
$$
\sigma(\iota_{1,*})
=\rho_4(\sigma)\iota_{1,*}\rho_1(\sigma)^{-1}
=\delta_4^{-1}\iota_{1,*}.
$$
用 (1008.6) 得
$$
\boxed{\iota_{1,*}\rho_1(\sigma)\iota_{1,*}^{-1}=\delta_4.}
\tag{1008.10}
$$
这一步明确保持 R575 的正扭曲方向，
没有将 $\kappa_4$ 偷换为反向角色。

现在设 $d\in\mathbb Q_3^{\times3}$。
选 $s^3=d$，并在所用三进嵌入下取 $s\in\mathbb Q_3$。
定义
$$
\iota_d:X_d\longrightarrow X_4,\qquad
u=(s/\alpha)b.
\tag{1008.11}
$$
同一 $\sigma$ 固定 $s$，所以仍有
$\sigma(\iota_d)=\delta_4^{-1}\iota_d$，
进而
$$
\iota_{d,*}\rho_d(\sigma)\iota_{d,*}^{-1}=\delta_4.
\tag{1008.12}
$$
一般 Kummer 记号下这里是
$\kappa_4\kappa_d^{-1}$；实际偶分支的 $\kappa_d$ 在整个
$G_{\mathbb Q_3}$ 上平凡。
因此 (1008.12) 同时覆盖原 $X_1$ 与全部实际偶分支 $X_d$。

若 $Z$ 在 $\mathbb Q$ 上定义，它在 $V_5(J_d)$ 上与
$\rho_d(\sigma)$ 交换。
将其经 $\iota_{d,*}$ 运输，由 (1008.12) 得与 $\delta_4$ 交换。
再运输回来，并用特征零 Abel 簇同态到 Tate 模作用的忠实性，
得到真正的同态恒等式 (1008.2)。
这里仅需忠实性，不需要把任意 Galois 模同态实现为代数同态。
有理自同态清分母后应用同一论证即可。

注意 $d=4$ 不满足 $d\in\mathbb Q_3^{\times3}$；
canonical $J_4$ 本身只用作证明中的驯分歧模型，
不能反套本定理得到其全部有理自同态中央化甲板。

## 4. 全部有理对应的 Picard 与高度后果

在实际 $X_d$ 上写
$$
\phi_d:X_d\longrightarrow Y,\qquad v=db^3,\qquad
N_d=\phi_d^*\phi_{d,*}=1+\delta_d+\delta_d^2.
$$
令 $q_d:J_d\to A_d$ 为任一满足 $q_dN_d=0$ 的实际新 Prym 商。
取原甲板固定基点 $c_{0,d}$。
对称、有理、迹零的整数对应 $Z$ 的修改对角类为
$$
D_Z(y)=[\operatorname{Fix}Z-2Z(y)].
$$
R1007 §2 的代表无关论证使用
$\Delta^*\mathcal C-\mathcal C|_{X\times c_0}
-\mathcal C|_{c_0\times X}$，
杀掉两个因子的拉回线丛，故只依赖 Jacobian 同态。
因此本篇定理对任意这样的有理对应都给
$$
N_dD_Z(c_{0,d})=3D_Z(c_{0,d}),\qquad
\boxed{3q_dD_Z(c_{0,d})=0.}
\tag{1008.13}
$$
这是整群中的三挠结论；有理化或在 $\ell\ge5$ 处再除去三挠后才为零。
不能把底曲线类本身删掉。实际上
$$
D_Z(c_{0,d})
=\phi_d^*\bigl(\phi_{d,*}D_Z(c_{0,d})/3\bigr)
\quad\text{于 }\operatorname{Pic}^0(X_d)\otimes\mathbb Q.
\tag{1008.14}
$$

保留 R1007 §3 的同一真实整格
$M_d=(J_d(\mathbb Q)/\mathrm{tors})\otimes\mathbb Z_\ell$、
同一高度 $b(M_d,M_d)\subset\ell\mathbb Z_\ell$，
并假设 $N_d,Z$ 对该高度自伴。
若
$$
N_dG=0,\qquad ZG=\lambda G,\qquad\lambda\in\ell\mathbb Z_\ell,
$$
则对每个 $y\in X_d(\mathbb Q)$，
$$
\begin{aligned}
b(G,D_Z(y))
&=b(G,D_Z(c_{0,d}))-2b(G,Z[y-c_{0,d}])\\
&=-2\lambda\,b(G,[y-c_{0,d}])
 \in\ell^2\mathbb Z_\ell.
\end{aligned}
\tag{1008.15}
$$
第一项为零由 (1008.13) 和 $N_d$ 自伴直接得出。
这对**全部有理自对应**成立；
不再需要先限制到纯 CM 或某个 tame Hecke 子代数。
有理对应仍必须带着原清分母因子的 $\ell$ 赋值应用本式。

因此 R1007 §6 曾保留的“在原 $X_1$ 上找新的非甲板相容有理对应”
这一入口现已关闭，并延伸到实际偶分支第二曲线。
其余入口保持开放：$N_dG=3G$ 的底曲线块、
原 $\eta_h$ 修正与全高度项、另一个确有来源的曲线或完整高度关系。
本篇没有证明任何这些项消失，也没有给 $a,b,d$ 的一致上界。

## 5. 证明来源与适用边界

- [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md)：
  原模型与 canonical 模型的准确三次扭曲方向。
- [R587](R587-actual-even-conductor-and-root-number.md)：
  实际偶分支 $d\in\mathbb Q_3^{\times3}$；这里消费已成结论。
- [R593](R593-actual-quotient-height-and-uniform-bad-place-support.md)、
  [R1007](R1007-deck-compatible-CM-correspondence-height-valuation-obstruction.md)：
  原 quotient、固定点、Picard 修正及同一整高度条件。
- Julio Brau、Nathan Jones，
  *Elliptic curves with 2-torsion contained in the 3-torsion field*，
  [作者 PDF](https://homepages.math.uic.edu/~ncjones/2tin3t.pdf)，
  (7)–(10) 与 Theorem 1.4：准确 $H_6$ 图子群和 $j$ 映射。
- Michitaka Miyauchi、Takuya Yamauchi，
  *A remark on conductor, depth and principal congruence subgroups*，
  Journal of Algebra 592 (2022), 424–434，
  [作者公开版本](https://arxiv.org/pdf/2107.08130)，
  Theorems 1.1–1.2（公开版印刷第2–3页）；
  此处只取 $n=2,m=1,F=\mathbb Q_3$。
- Henri Carayol，
  *Sur les représentations $\ell$-adiques associées aux formes modulaires de Hilbert*，
  Annales scientifiques de l'École Normale Supérieure, série 4,
  19(3) (1986), 409–468，
  [原文](https://numdam.org/item/10.24033/asens.1512.pdf)，
  Théorème (A)，第410–411页：有限处局部—整体相容性。
  此处基域 $\mathbb Q$ 次数为奇数，偶数次基域的额外条件不涉及本应用。
- Henri Carayol，*Formes modulaires et représentations $\ell$-adiques*，
  Astérisque 147–148 (1987), 33–47，
  [原文](https://www.numdam.org/article/AST_1987__147-148__33_0.pdf)，
  §3.4.3，第41–42页：整个模曲线塔 $H^1$ 的自守/Galois 分解。

本结论为理论证明，无新增数值扫描或旧计算重跑。
主目标仍为 OPEN；全惯性、非整 $j$、变化二次域等 O0 分支
并未因本篇局部中央化论证而被排除。
