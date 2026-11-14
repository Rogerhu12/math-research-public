# R236 附录：固定阶全域双导子与全部广义核的等向闭像约束

日期：2026-11-13（UTC）。作者：central_review / Astra-ISP-0c017065；AI 辅助：GPT-6 Astra Pro。root 全文核验204行并回读原双导子§6–7的统一实际误差。
状态：完整直接推论；范围是已付全域 Bell 双导子工具的有界行。
不声称原核为零，不将闭像改成实际像，也不外推到未知中央压缩。

## 1. 准确输入与结论

沿用
[R236 全域 Bell 双导子附录](R236-appendix-global-bell-difference-units-and-double-commutator-projections.md)
的全部假设、普通 Bell 累积量与有界实现
$$
T=\mathcal P(X;G)\in\mathcal A.
$$
明确地，非零主幅度的非增重排满足
$$
\rho_k\le B e^{-\beta_-k^\alpha},\qquad
\rho_N\ge c_0e^{-\beta_+N^\alpha}
\quad\text{沿无穷子序列 }N,
$$
其中 $\alpha>0$、$0<\beta_-\le\beta_+$，且 $B,c_0>0$ 固定。
全部相位与物理排列任意，指数权仍为原任意复 $\ell^2$ first。
$q$ 是固定非零多项式，$s=a_*+\sum a_j$；
可先除以最高系数归一为首一，这不改变以下任何幂核或闭像。
若 $q(s)\ne0$，$T$ 是单位，以下结论为空。
故设 $q(s)=0$。

所有自然幂域都是 $H$，并且
$$
T^*=CTC,\qquad
\mathcal B(x,y)=\langle x,Cy\rangle.
$$
记
$$
M_n=\ker T^n,\qquad n\ge1.
$$
这里使用有界算子 $T$ 的真实算子幂；没有把它等同于普通点态多项式 $q(u)^n$ 的轨道实现。

**定理。** 对全部固定整数 $n,m\ge1$，
$$
\boxed{\mathcal B(M_n,M_m)=0,}
\tag{1.1}
$$
等价地，
$$
\boxed{M_n\subseteq\overline{\operatorname{Ran}T^m}.}
\tag{1.2}
$$
这里的 $n,m$ 可分别任意固定，不须相等。

因而
$$
\mathcal R=\overline{\bigcup_{n\ge1}M_n}
$$
是全 $\mathcal B$ 等向的闭 $A$ 不变空间，且
$$
\boxed{
\mathcal R\subseteq
\bigcap_{m\ge1}\overline{\operatorname{Ran}T^m}.
}
\tag{1.3}
$$
若 $\mathcal R\ne0$，它是真正的无限维真子空间；
本稿没有证明其非零，也没有由此排除它。

## 2. 固定阶时不需要右伪逆

全域双导子附录 §7 已在原实际模型证明：
对每个固定整数 $r\ge1$，存在有界算子 $U_{N,r}$，使
$$
\left\|
\operatorname{ad}_T^{2r}(U_{N,r})-C_{I_N}^r
\right\|\longrightarrow0,
\qquad
C_{I_N}=\frac2{Q_N}\sum_{j\in I_N}E_j,
\tag{2.1}
$$
其中 $Q_N\to\infty$、$\min I_N\to\infty$。
其构造中的所有差分逆、物理 carry 和全域导子都已经支付。
本文只固定 $r$ 后让 $N\to\infty$；
不使用 $r\asymp Q_N$，也不加入右侧 Moore--Penrose 逆。

对任意固定有限柱向量 $x$，充分高的池位均独立于其物理支撑。
由于
$$
E_j\Omega_+=\frac12(\Omega_+-\Omega_-),
\qquad
\Omega_\pm=\frac{e_0\pm e_1}{\sqrt2},
$$
各个单高位波动正交，故
$$
\|(C_{I_N}-I)x\|=\frac{\|x\|}{\sqrt{Q_N}}.
\tag{2.2}
$$
所有 $\|C_{I_N}\|\le2$，所以有限柱稠密性给
$$
C_{I_N}\longrightarrow I\quad\text{强收敛}.
$$
$r$ 固定时用有限望远镜积式，
$$
C_{I_N}^r\longrightarrow I\quad\text{强收敛}.
$$
于是 (2.1) 给
$$
\boxed{
\operatorname{ad}_T^{2r}(U_{N,r})
\longrightarrow I\quad\text{强收敛}.
}
\tag{2.3}
$$
$U_{N,r}$ 自身的范数可增长；
这里只需要其导子输出的已证范数近似和强极限。

## 3. 全部广义核的完整配对

取固定
$$
f\in M_n,\qquad g\in M_m,
$$
再固定一个 $r$ 满足
$$
2r\ge n+m-1.
\tag{3.1}
$$
有界算子的完整导子展开为
$$
\operatorname{ad}_T^{2r}(U_{N,r})
=
\sum_{k=0}^{2r}(-1)^k\binom{2r}{k}
T^{2r-k}U_{N,r}T^k.
$$
利用原 $\mathcal B$ 对称性，逐项有
$$
\mathcal B(T^{2r-k}U_{N,r}T^kf,g)
=
\mathcal B(U_{N,r}T^kf,T^{2r-k}g).
\tag{3.2}
$$
若 $k\ge n$，右边的第一个幂向量为零。
若 $k<n$，则
$$
2r-k\ge2r-n+1\ge m,
$$
第二个幂向量为零。
所以每个 $N$ 都准确满足
$$
\mathcal B(\operatorname{ad}_T^{2r}(U_{N,r})f,g)=0.
$$
令 $N\to\infty$，用 (2.3) 得
$$
\mathcal B(f,g)=0.
$$
这证明 (1.1)。
没有要求 $C$ 保持任何 $M_n$，也没有把等向性传到局部矩阵作用后的向量。

## 4. 闭像与闭广义核空间

因为 $T$ 全域有界且 $T^*=CTC$，
$$
(T^m)^*=CT^mC.
$$
故
$$
\overline{\operatorname{Ran}T^m}
=(\ker(T^m)^*)^\perp
=(CM_m)^\perp.
$$
由 (1.1) 得 (1.2)。

各 $M_n$ 递增、闭且在 $A$ 下不变。
双线性配对连续，所以其并集的范数闭包 $\mathcal R$ 仍全等向。
每个固定闭像包含整个并集，故也包含 $\mathcal R$，给出 (1.3)。

若 $\mathcal R=H$，连续性会使 $\mathcal B(H,H)=0$，
与 $C$ 为反线性等距对合矛盾。
因此 $\mathcal R$ 必为真子空间。
若它非零且有限维，
原 $A$ 在该不变空间上仍单射且拟幂零，
这与有限维单射算子的谱性质矛盾。
故非零时必无限维。

## 5. 与旧有限闭像结论及端段的区别

旧
[R236 高位反射闭像附录](R236-appendix-all-finite-range-closures-by-high-bit-reflections.md)
针对规范非可和正平方根分支，
证明原核进入每个有限闭像，
并明确没有把所有广义核放进全部闭像。

本稿使用后来已经支付的全域双阶导子，
在其有界 Bell 伸缩指数范围内得到 (1.1)–(1.3)。
两稿的具体算子与域假设不同；
不能只凭本稿的短证明就回写一个无条件的无界版本。

本稿仍未得到：

- $M_n\subset\operatorname{Ran}T^m$；
- 原像范数的一致控制；
- $\mathcal R$ 上的限制 $T|_{\mathcal R}$ 有稠密值域；
- $\mathcal B(DM_n,M_m)=0$ 对任意固定局部 $D$；
- 未知中央压缩保留原高位双导子；
- 任意非零原核存在或被排除。

尤其 $r\asymp Q_N$ 的强投影方案仍有原右伪逆末段；
本稿固定 $r$，因此避开的是这一特定推论对伪逆的需求，
没有支付一般局部排核的末段连接。

四位全等向有限校准说明，
只有原核全等向仍不能把正交伪逆移入该核。
本稿给更强的全部广义核约束，
但它本身也不提供所缺的局部等向性。
