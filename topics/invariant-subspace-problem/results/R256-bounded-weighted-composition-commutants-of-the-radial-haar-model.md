# R256：径向 Haar 模型中有界加权复合交换子的完整分类

日期：2026-11-12（UTC）。作者：kernel。
状态：完整证明，中间结论。本文只分类明确的加权复合算子，不分类整个交换子代数，也不据此排除未知危险核。

## 1. 模型与结论

设 $H=L^2(\mathbb Z_2,\mu)$，$\mu$ 为 Haar 概率测度。记 $y_j\in\{0,1\}$ 为第 $j$ 个二进位，$\tau y=y+1$。取正递减权
$$
\alpha_j>0,\qquad \frac{\alpha_{j+1}}{\alpha_j}=\eta_j\longrightarrow0,
$$
并定义
$$
w(y)=\alpha_{v_2(y)}\quad(y\ne0),\qquad w(0)=0,
\qquad
(Af)(y)=w(y)f(y-1).
\tag{1.1}
$$
原课题的具体超快权满足这些条件。以下证明实际上只需这里较弱的比率条件。

设 $\phi:\mathbb Z_2\to\mathbb Z_2$ 可测且 nonsingular，即 Haar 零测集的原像仍零测。设可测 $b$ 使
$$
(Vf)(y)=b(y)f(\phi(y))
\tag{1.2}
$$
在 $H$ 上给出有界算子。起初不假定 $b\in L^\infty$，也不假定 $\phi$ 可逆或保 Haar 测度。

**定理。** 若 $V\ne0$ 且 $AV=VA$，则存在唯一 $n\in\mathbb N_0$ 和 $c\in\mathbb C\setminus\{0\}$，使
$$
\boxed{
\phi(y)=y-n\quad\text{a.e.},\qquad
b(y)=c\prod_{k=0}^{n-1}w(y-k)\quad\text{a.e.},
\qquad V=cA^n.
}
\tag{1.3}
$$
空乘积取1。反向显然成立：每个 $cA^n$ 都具有这个形式并与 $A$ 交换。

这里的 $n$ 是普通非负整数，不是任意 $2$-adic 整数。特别不存在非零有界的反向加权平移交换子，也不存在非整数 $2$-adic 平移上的非零有界加权复合交换子。

## 2. 先从交换关系识别底映射

因为 $1\in H$，(1.2) 给 $V1=b\in H$。将 $AV=VA$ 作用于1，
$$
w(y)b(y-1)=b(y)w(\phi(y))
\quad\text{a.e.}
\tag{2.1}
$$
$w>0$ a.e.，而 $\phi$ nonsingular 保证 $w\circ\phi>0$ a.e.。
所以 $b(y-1)=0$ 当且仅当 $b(y)=0$，模零集成立。

加一作用在 Haar $\mathbb Z_2$ 上遍历。为说明所用事实，若 $E$ 模零集不变，则加一循环置换每个有限商 $\mathbb Z/2^m\mathbb Z$ 的全部剩余类，故
$$
\mu(E\cap\{y\bmod2^m=r\})=\mu(E)/2^m.
$$
由有限柱代数及单调类，$E$ 与所有可测集独立，特别与自身独立，因而 $\mu(E)\in\{0,1\}$。
应用于 $b$ 的零集，$V\ne0$ 排除 $b=0$ a.e.，得到
$$
b(y)\ne0\quad\text{a.e.}
\tag{2.2}
$$

对每个 dyadic Haar 字符 $\chi$ 使用交换关系：
$$
w(y)b(y-1)\chi(\phi(y-1))
=
b(y)w(\phi(y))\chi(\phi(y)-1).
$$
由 (2.1)、(2.2) 取消同一个非零系数。所有此类字符构成一个可数、分离点的族，所以可在同一个余零集上得到
$$
\phi(y-1)=\phi(y)-1.
\tag{2.3}
$$
于是 $\psi(y)=\phi(y)-y$ 是可测的加一不变 $\mathbb Z_2$ 值函数。每个有限剩余类坐标 $\psi\bmod2^m$ 由遍历性为常数；这些常数相容，确定一个 $t\in\mathbb Z_2$。因此
$$
\boxed{\phi(y)=y+t\quad\text{a.e.}}
\tag{2.4}
$$

记 $(U_tf)(y)=f(y+t)$。它是 Haar 酉算子。现在 $V=M_bU_t$，故 $M_b=VU_{-t}$ 有界，从而
$$
b\in L^\infty,\qquad \|b\|_\infty=\|V\|.
\tag{2.5}
$$
这个有界性是在识别底映射后推出的，没有先假定一般复合底映射保测度。

## 3. 实际归一化幂提供高位约束

R12 的径向 dyadic 幂计算仅需要 §1 的权假设。对
$$
N_j=\frac{A^{2^j}}{\|A^{2^j}\|},
$$
令 $E_j$ 为第 $j$ 位的实际矩阵单位 $e_{10}$，其他位恒等，则
$$
\boxed{\|N_j-E_j\|=\eta_j\longrightarrow0.}
\tag{3.1}
$$
具体公式为
$$
(E_jf)(y)=\mathbf1_{\{y_j=1\}}f(y-2^j).
\tag{3.2}
$$
输出位为1时减去 $2^j$ 不影响其他位，因此 (3.2) 正是逐位提升。

$V$ 与 $A$ 交换，故与每个 $N_j$ 交换。于是
$$
\boxed{
\|[V,E_j]\|
=\|[V,E_j-N_j]\|
\le2\eta_j\|V\|.
}
\tag{3.3}
$$
这也可直接视为 R20 §3 的整个交换子高位估计。

将 (3.2) 与 $V=M_bU_t$ 逐项代入，得到
$$
([V,E_j]f)(y)
=
\left[
b(y)\mathbf1_{\{(y+t)_j=1\}}
-\mathbf1_{\{y_j=1\}}b(y-2^j)
\right]f(y+t-2^j).
\tag{3.4}
$$
后面只在 $f=1$ 上使用这个实际等式。

## 4. 非整数平移被两位 Haar 柱排除

一个 $2$-adic 整数属于普通 $\mathbb Z$，当且仅当它的二进位最终全0或最终全1。若 $t\notin\mathbb Z$，则有无穷多个 $j\ge1$ 满足
$$
t_j\ne t_{j-1}.
\tag{4.1}
$$
对这样的 $j$，定义两个高位组成的柱集
$$
C_j=\{y:y_j=0,\ y_{j-1}=1-t_j\}.
\tag{4.2}
$$
$\mu(C_j)=1/4$，并且
$$
y_j=0,\qquad (y+t)_j=1
\quad(y\in C_j).
\tag{4.3}
$$

为核对第二个等式，令 $r=y\bmod2^{j+1}$，$s=t\bmod2^{j+1}$。
若 $t_j=0,t_{j-1}=1$，则
$$
2^{j-1}\le s<2^j,\qquad 2^{j-1}\le r<2^j,
$$
所以 $2^j\le r+s<2^{j+1}$。
若 $t_j=1,t_{j-1}=0$，则
$$
2^j\le s<3\cdot2^{j-1},\qquad 0\le r<2^{j-1},
$$
仍有 $2^j\le r+s<2^{j+1}$。
因此 (4.3) 保留了所有低位进位，而不是忽略它们。

由 (3.4)，$[V,E_j]1=b$ 在 $C_j$ 上成立。结合 (3.3)，
$$
\|b\mathbf1_{C_j}\|_2\le2\eta_j\|V\|.
\tag{4.4}
$$

另一方面，对于任何固定 $h\in L^1(\mu)$，两个位都趋向无穷的柱集 (4.2) 满足
$$
\int h\mathbf1_{C_j}\,d\mu\longrightarrow\frac14\int h\,d\mu.
\tag{4.5}
$$
确实，对固定有限低位柱函数是准确独立性；$L^1$ 柱逼近及
$\|\mathbf1_{C_j}\|_\infty\le1$ 给一般结论。这里可能出现的两种柱模式都具有概率 $1/4$，所以即使模式随 $j$ 改变，论证也一致。

取 $h=|b|^2\in L^1$，则沿 (4.1) 的无穷子列，
$$
\|b\mathbf1_{C_j}\|_2\longrightarrow\frac12\|b\|_2>0.
\tag{4.6}
$$
这与 (4.4)、$\eta_j\to0$ 矛盾。因此
$$
\boxed{t\in\mathbb Z.}
\tag{4.7}
$$

这一排除同时使用了真实进位范数误差和同一个 Haar 正常函数 $|b|^2$。
它不是把抽象边界态的高位统计移到未知子空间上。

## 5. 普通整数平移的权重唯一性与方向

将 (2.4) 代入 (2.1)，交换系数方程成为
$$
w(y)b(y-1)=b(y)w(y+t).
\tag{5.1}
$$

### 5.1 $t=-n$，$n\ge0$

令
$$
p_n(y)=\prod_{k=0}^{n-1}w(y-k),\qquad p_0=1.
$$
它几乎处处正且有限，并满足
$$
w(y)p_n(y-1)=p_n(y)w(y-n).
$$
因此 (5.1) 使可测函数 $b/p_n$ 加一不变。遍历性给它为常数 $c$，于是
$b=cp_n$、$V=cA^n$。这里允许比值起初无界：遍历性对任意有限可测复值不变函数仍成立，
可用其实部、虚部的有理阈值集证明。

### 5.2 $t=m$，$m\ge1$

令
$$
q_m(y)=\left(\prod_{k=1}^m w(y+k)\right)^{-1}.
$$
它几乎处处正且有限，满足 (5.1) 的相同方程。故 $b/q_m$ 不变，得到 $b=cq_m$。

但 $q_m$ 本质无界。因为 $w\le\alpha_0$，
$$
q_m(y)\ge\frac{\alpha_0^{-(m-1)}}{w(y+1)}.
$$
$\alpha_r\to0$，而每个集合 $\{v_2(y+1)=r\}$ 都有正 Haar 测度，所以右侧本质无界。
由 $b\in L^\infty$ 只能有 $c=0$，这与 $V\ne0$ 矛盾。

故只有 §5.1 的方向可能，定理得证。平移参数及 $c$ 的唯一性也由上述识别立即得到。

## 6. 与既有结果及新来源的范围关系

本文已对照 R16、R20、R32 以及现有结论索引。
R16 处理无限乘积向量的循环性；R32 处理 $\mathcal A$ 的圆作用与形式系数。
R20 的高位禁向估计是本证明的输入，但这些文件没有给出一般可测底映射 (1.2) 的完整分类。
本稿的新一步是将该估计与无限二进位转折处的两个高位 Haar 柱结合，再由交换关系识别全部底映射和整数方向。

OpenAI 公开预印本 *Backward intertwiners and a transitive commutant* 的
[固定版本](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026)
在 $L^2(X;\ell^2(\mathbb Z))$ 上构造分解的前移 $S$ 及一个同时移动底空间、降低纤维坐标的有界交换子。
其 [intertwiner.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/build/sections/intertwiner.tex)
先解每纤维双向递推，再用同一纤维中的 $\sup_j\widetilde b_j(x)$ 归一化。
这一步合法，因为 $S$ 本身不移动底点 $x$；共同归一化因子在交换方程中抵消。

原模型的 $A$ 自身就移动 Haar 底点。任意点态重新归一化须满足 (5.1)，不能在不同底点分别自由缩放。
本定理精确说明，该来源的反向加权复合机制没有以 (1.2) 的形式落在原 $A$ 的交换子中。

结论不排除一般 $R\in\{A\}'$，不排除积分算子、非复合算子或其他未知机制。
也没有证明规范危险平方核为零，或解决普通不变子空间问题。
