# 二阶 gauge 定义域：纯模型的严格反例与真实有限头修复

日期：2026-11-12（UTC）。独占稿：critical_kernel。
状态：以下反例与修复均已证明。它们区分“已经 C 自伴”与“gauge 保持同一定义域”，不构造实际 A 的非零核。

## 1. 纯二阶 C 自伴并不保证 gauge 同域

在物理第0、1位组成的四维头空间上，以 e_0,e_1,e_2,e_3 表示低两位整数坐标。令

$$
M=E_0+E_1.
$$

取只作用于 j≥2 的一个无界纯第一阶闭乘子 L，例如系数
a_j≥0、a∈ℓ²\ℓ¹。纯第一阶 Dirac 证明给 L 的 C 自伴性；其无界性由有限纯第一阶乘子范数至少 ∑_{2≤j<n}a_j 得到。因此存在 h∈H_tail 不属于 DomL。

在有限头张量有限 chaos 上定义 M⊗L，并取闭包 T。
有限头奇异值分解直接给

$$
\operatorname{Dom}T
=(\ker M\otimes H_{\rm tail})
\oplus
((\ker M)^\perp\otimes\operatorname{Dom}L).
\tag{1.1}
$$

原因是 M 在 (kerM)⊥ 上有严格正的最小奇异值，故该部分的图范数等价于 L 的图范数；在 kerM 上图范数只是 H 范数。这个 T 也是纯二阶 Dirac 定理得到的 C 自伴闭乘子。

有

$$
v=e_1-e_2\in\ker M.
$$

但四阶 gauge U_i 在物理头上为 diag(1,i,−1,−i)，所以

$$
U_i v=i e_1+e_2,\qquad
M(U_i v)=(i+1)e_3\ne0.
$$

因此

$$
v\otimes h\in\operatorname{Dom}T,\qquad
U_i(v\otimes h)\notin\operatorname{Dom}T.
\tag{1.2}
$$

对应的纯符号为

$$
f=(b_0^{\rm phys}+b_1^{\rm phys})
\sum_{j\ge2}a_j\chi_j
=
\left(1-\frac{\chi_0+\chi_1}{2}\right)
\sum_{j\ge2}a_j\chi_j,
$$

确实只有一阶和二阶 Walsh 项。这不是高次数或不稠密定义域造成的例外。

故不能从纯二阶 Dirac 本质自伴性、有限 chaos 图核心或
U_ζ𝓓=𝓓 单独推出 U_ζDomT=DomT。

## 2. 同一个分离符号在真实模型中有额外结构

令

$$
Y_j=N_j(I+N_j)^{-1},\qquad F(A)=Y_0+Y_1,
$$

并令 X_g 是真实闭第一阶乘子，g=∑_{j≥2}a_jχ_j。
当一个向量不依赖第 j 位时，实际公式精确给

$$
Y_ju=b_j^{\rm phys}u.
$$

例如将 u 写成 (v,v)，有 N_j(v,v)=(η_jN_{j+1}v,v)，且
(I+N_j)(0,v)=(η_jN_{j+1}v,v)。因此上面的二阶向量在真实模型中为

$$
f=F(A)g.
\tag{2.1}
$$

F 是一个真正有理解析芽的作用，首阶为1：

$$
F(z)=z\,u(z),\qquad u(0)=1/d_0\ne0.
$$

所以 F(A) 单射稠密。R125 给 g 循环，故有界交换子 F(A) 的稠密像立即推出 f 循环。纯模型 (1.2) 不能转移成实际核。

更细地，可恢复实际闭二阶乘子的 gauge 同域。记其有限 chaos 初始算子为 S_f、闭包为 X_f。有限部分与闭第一阶域控制给

$$
S_f x=F(A)X_gx\qquad(x\in\mathcal D).
\tag{2.2}
$$

对固定 ζ，真实第一阶同域式为

$$
\gamma_\zeta(X_g)=X_g+D_\zeta(A),
$$

D_ζ 是有限真正解析芽。而

$$
F(\zeta A)=R_\zeta(A)F(A),\qquad
R_\zeta(z)=\zeta\,u(\zeta z)u(z)^{-1}
$$

是实际解析单位。故在𝓓上

$$
\gamma_\zeta(S_f)
=R_\zeta(A)S_f+F(\zeta A)D_\zeta(A).
\tag{2.3}
$$

右侧第一因子 R_ζ(A) 有有界逆，第二项有界。于是
R_ζ(A)X_f+F(ζA)D_ζ(A) 是闭算子，定义域恰为 DomX_f，且𝓓仍是图核心。
左侧的图核心也为 U_ζ𝓓=𝓓。取闭包得到

$$
\boxed{
\gamma_\zeta(X_f)
=R_\zeta(A)X_f+F(\zeta A)D_\zeta(A),\qquad
U_\zeta\operatorname{Dom}X_f=\operatorname{Dom}X_f.
}
\tag{2.4}
$$

没有假设 F(A) 本身可逆，也没有声称自然乘积 F(A)X_g 在
DomX_g 上已经闭；使用的是 canonical 二阶闭包及两侧图核心。

## 3. 一般有限解析头的同一修复

设 F 为任意非零真正解析芽，F(z)=z^r u(z)、u(0)≠0。
若某个已确定闭算子 X 以𝓓为图核心，且在𝓓上有
X=F(A)X_g，其中 X_g 是 R125 的闭第一阶乘子，则完全同样得到

$$
\gamma_\zeta(X)
=
\left[\zeta^r u(\zeta A)u(A)^{-1}\right]X
+F(\zeta A)D_\zeta(A).
$$

只要 U_ζ𝓓=𝓓，右侧为有界可逆左因子乘 X 再加有界项，故该等式取闭包后为同域等式。

这是一条可用于分离有限头的修复机制。一般二阶无限矩阵的 gauge 差包含多个独立第一阶行，未被本节化成同一个有界可逆左因子。不能把特殊的有限解析头比例推广成任意二阶的域协变。

依赖：R125 第一阶闭乘子；R130 实际次数权；R131 二阶 C 自伴与图核心；R16/R88 有限头真实乘子公式。
