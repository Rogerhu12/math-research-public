# R296：任意出生的定长子集残差、两带升层与真实桥创新

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit。

**状态：本稿的概率表示、两带回归恒等式及创新能量等价已证明；一般出生的统一加强 S1 常数尚未证明。** 单高度的完整 Schur 原理已有 R239、R275 等结果。本稿不把它重新计作一般正性结论；新增接口是把所有高度的最高次残差放进同一族定长子集空间，直接从乘积权证明两带升层，并把真实三次桥创新写成相邻最优回归系数的差。这样需要控制的是一个共同的物理映射，而不是三个单高度夹逼。

## 1. 物理空间与定长子集空间

取 \(M\) 个任意正权 \(b_i\)，置
\[
z_i=b_i^2,\qquad d=\sum_i b_iE_i,
\qquad C=\sum_i b_i^3E_i.
\]
\(\mathcal H_r\) 的物理占据基 \(e_J\) 正交归一。记
\[
K_r=\ker d\cap\mathcal H_r,
\qquad
\mathcal J_{j,r}=(d^j/j!)^\dagger|_{K_r},
\qquad \Gamma_{j,r}=\mathcal J_{j,r}^*\mathcal J_{j,r}.
\]
每个最小逆都在完整物理层中取，之后才限制 primitive 输入。

对 \(0\le k\le M\)，在全部 \(k\) 元子集上使用未归一内积
\[
\langle F,G\rangle_k=\sum_{|I|=k}z_I\overline{F(I)}G(I),
\qquad z_I=\prod_{i\in I}z_i.
\tag{1.1}
\]
相应概率为 \(\mu_k(I)=z_I/e_k(z)\)。因此 \(\|F\|_k^2=e_k(z)\mathbb E_{\mu_k}|F|^2\)，后面的公式始终保留这个归一因子。

映射
\[
\mathcal V_kF=\sum_{|I|=k}b_IF(I)e_I
\tag{1.2}
\]
是从 (1.1) 到物理 \(\mathcal H_k\) 的等距同构。

记 \(\mathscr P_{\le r}^{(k)}\) 为多线性多项式在 \(k\) 元子集上的限制，次数至多 \(r\)。只要 \(k\ge r\)，这个空间已经由所有 \(r\) 次单项式张成，因为对 \(|J|\le r\)，
\[
1_{J\subset I}
=\binom{k-|J|}{r-|J|}^{-1}
\sum_{\substack{A\supset J\\|A|=r}}1_{A\subset I}.
\tag{1.3}
\]

对物理 \(f\in\mathcal H_s\) 定义其最高次特征
\[
\Phi_{s,f}(I)=\sum_{\substack{J\subset I\\|J|=s}}\frac{f_J}{b_J}.
\tag{1.4}
\]
若 \(k=s+n\)，直接逐集合计算给
\[
\mathcal V_k\Phi_{s,f}=\frac{(d^*)^n}{n!}f.
\tag{1.5}
\]

## 2. 完整最高次残差及源度量

固定 \(s\ge1\)，记 \(h=M-2s\)。首先取 \(0\le n\le h\) 和 \(k=s+n\)。对 \(f\in K_s\)，定义唯一的最优残差函数
\[
\mathcal R_{k,s}f
=(I-\Pi_{\le s-1}^{(k)})\Phi_{s,f},
\tag{2.1}
\]
其中投影按 (1.1) 的真实乘积权内积计算。这里必须减去**全部**低于 \(s\) 次的特征；仅减均值只适用于 \(s=1\)。

置
\[
G_n=\Gamma_{n,s},\qquad C_n=G_n^{-1},\qquad G_0=C_0=I_{K_s}.
\]
则实际残差映射是
\[
\boxed{
\mathcal T_{n,s}:=\mathcal V_{s+n}\mathcal R_{s+n,s}
=\mathcal J_{n,s}C_n,
\qquad \mathcal T_{n,s}^*\mathcal T_{n,s}=C_n.
}
\tag{2.2}
\]

证明保留完整 Schur 顺序。令 \(A_n=d^n/n!\)、\(F_n=A_nA_n^*\)，都在所列完整物理层上。若 \(u\in\mathcal H_{s-1}\)，则
\[
\Phi_{s,d^*u}=(n+1)\Phi_{s-1,u}
\quad\text{在 }(s+n)\text{ 元子集上}.
\tag{2.3}
\]
因此 (2.1) 的极小问题准确等于
\[
\inf_{u\in\mathcal H_{s-1}}
\left\|A_n^*(f+d^*u)\right\|^2.
\tag{2.4}
\]
最优向量 \(q_n=f+d^*u_n\) 满足 \(F_nq_n\in K_s\)。完整块逆给 \(F_nq_n=C_nf\)，所以
\(A_n^*q_n=A_n^*F_n^{-1}C_nf=\mathcal J_{n,s}C_nf\)。这就证明 (2.2)，而不是把 \(F_n\) 的压缩当成 \(C_n\)。

全部低阶系数也有明确的完整逆表达：
\[
u_n=-\frac1{(n+1)^2}
\left(F_{n+1}^{(s-1)}\right)^{-1}dF_n^{(s)}f,
\tag{2.5}
\]
因为 \(dF_n^{(s)}d^*=(n+1)^2F_{n+1}^{(s-1)}\)。一般 \(u_n\) 不在 \(K_{s-1}\)，不可把该完整逆替换成 primitive 压缩逆。

### 2.1 全矩阵条件协方差

令 \(X_r(I)=(1_{J\subset I})_{|J|=r}\)，并记
\(M_{ab}^{(k)}=\mathbb E_{\mu_k}[X_aX_b^*]\)。令 \(D_{b,s}\) 为 \(\mathcal H_s\) 上的对角矩阵 \(\operatorname{diag}(b_J)\)。在 \(\operatorname{Ran}d^*\) 上零延拓的实际精度满足
\[
\boxed{
\widetilde C_n
=e_k(z)D_{b,s}^{-1}
\left(M_{ss}^{(k)}
-M_{s,s-1}^{(k)}(M_{s-1,s-1}^{(k)})^{-1}M_{s-1,s}^{(k)}\right)
D_{b,s}^{-1}.
}
\tag{2.6}
\]
其在 \(K_s\) 上的限制是 \(C_n\)，核恰为 \(\operatorname{Ran}d^*\)。合法区间内低阶特征矩阵满列秩，故这里的逆存在。出生一时 \(X_0=1\)，(2.6) 才退化为 R239、R271 的普通占据协方差。

### 2.2 硬顶的真实零残差

还定义 \(\mathcal R_{M-s+1,s}=0\)、\(C_{h+1}=0\)。这不是制造一个不存在的上出生 MP Gram：当 \(k=M-s+1\) 时，补集大小是 \(s-1\)，所以每个该切片上的函数都能由次数至多 \(s-1\) 的多项式表示，故 (2.1) 的残差本来就为零。下出生 \(s-1\) 在这一层仍是合法最高阶。

## 3. 乘积权自身给出的两带性质

在相邻切片间定义
\[
(\mathsf U_{k-1}F)(I)=\sum_{i\in I}F(I\setminus\{i\}),\qquad |I|=k.
\tag{3.1}
\]
它的加权伴随是
\[
(\mathsf D_kG)(J)=\sum_{i\notin J}z_iG(J\cup\{i\}),\qquad |J|=k-1.
\tag{3.2}
\]
物理等距关系准确为
\[
\mathcal V_k\mathsf U_{k-1}=d^*\mathcal V_{k-1},
\qquad \mathcal V_{k-1}\mathsf D_k=d\mathcal V_k.
\tag{3.3}
\]

如果 \(g\) 是多线性多项式，记 \(W(x)=\sum_i z_ix_i\)、\(S=\sum_i z_i\)。在切片上
\[
\mathsf D_kg=(S-W)g+\sum_i z_i(1-x_i)\partial_i g.
\tag{3.4}
\]
因此 \(\mathsf D_k\) 最多把次数提高一；次数提高的最高项仅来自 \(-Wg\)。另一方面，\(\mathsf U_{k-1}\) 在齐次 \(r\) 次特征上的作用是乘以 \(k-r\)。

现在令 \(k=s+n\)、\(1\le n\le h+1\)，并在需要处使用上节真实硬顶约定。\(\mathsf U_{k-1}\mathcal R_{k-1,s}f\) 的最高次项等于 \(n\Phi_{s,f}\)。减去 \(n\mathcal R_{k,s}f\) 后只剩低于 \(s\) 次的函数。此外，对任意次数至多 \(s-2\) 的 \(g\)，
\[
\langle\mathsf U_{k-1}\mathcal R_{k-1,s}f,g\rangle_k
=\langle\mathcal R_{k-1,s}f,\mathsf D_kg\rangle_{k-1}=0,
\]
因为右侧第二个函数次数至多 \(s-1\)。所以余项只能属于**低一出生的最高次残差空间**，不含更低出生。这是由真实乘积权给出的两带结构，而不是任意抽象 Hodge 模型的推测。

## 4. 两带系数恰为真实三次桥

设
\[
L=K_{s-1},\qquad L_j=\Gamma_{j,s-1},
\qquad B=C|_{K_s}:K_s\longrightarrow L.
\]
\(B\) 的值在 \(L\)，因为 \([d,C]=0\)。其伴随始终按两个真实 primitive 源内积计算。

对 \(g\in L\)，\(\mathsf D_k\mathcal R_{k,s-1}g\) 的最高 \(s\) 次项是 \(-\Phi_{s,C^*g}\)。这是因为 (3.4) 只在 \(-W\Phi_{s-1,g}\) 中产生最高次数，而在物理系数上，\(W\) 的最高次乘法正好是 \(\sum_i b_i^3E_i^*=C^*\)。

又 \(C^*g-B^*g\in\operatorname{Ran}d^*\)，其特征在 \((k-1)\) 元切片上按 (2.3) 降到低于 \(s\) 次。因此真实交叉内积是
\[
(\mathcal V_k\mathcal R_{k,s-1})^*
\mathcal V_k\mathsf U_{k-1}\mathcal R_{k-1,s}
=-BC_{n-1}.
\tag{4.1}
\]
新切片的低一出生残差 Gram 是 \(L_{n+1}^{-1}\)。于是其准确回归系数为 \(-L_{n+1}BC_{n-1}\)，得到
\[
\boxed{
\mathsf U_{k-1}\mathcal R_{k-1,s}
=n\mathcal R_{k,s}
-\mathcal R_{k,s-1}L_{n+1}BC_{n-1}.
}
\tag{4.2}
\]
整个式子在同一 \(k\) 元切片上，右侧两个残差空间正交。它与既有真实两带 MP 公式一致，但本节从完整回归空间、乘积权伴随及最高系数独立证明了它。

等价的物理形式是
\[
d^*\mathcal J_{n-1,s}C_{n-1}
=n\mathcal J_{n,s}C_n-\mathcal J_{n+1,s-1}BC_{n-1}.
\tag{4.3}
\]

## 5. 相邻回归系数之差就是创新

固定 \(1\le n\le h\)，置 \(k=s+n\)，并定义两个从同一 \(K_s\) 到同一 \(L\) 的真实系数
\[
\Theta_{n-1}=L_{n+1}BC_{n-1},\qquad
\Theta_n=L_{n+2}BC_n.
\tag{5.1}
\]
这里没有把两个切片的向量直接相减；相减的是两个已经放在同一物理低出生源中的回归系数。

记
\[
\delta_{n+1}^*=\frac{\Theta_n-\Theta_{n-1}}{n+1},
\qquad
\delta_{n+1}=\frac{C_nB^*L_{n+2}-C_{n-1}B^*L_{n+1}}{n+1}.
\tag{5.2}
\]
这正是加强相邻序中的真实桥创新。特别 \(n=1\) 时，
\(\delta_2=(C_1B^*L_3-B^*L_2)/2=\Delta\)。

在新切片 \(k+1\) 上定义一个共同映射
\[
\boxed{
\mathsf Z_n
=\frac{1}{n+1}
\left(\mathsf U_k\mathcal R_{k,s}
+\mathcal R_{k+1,s-1}\Theta_{n-1}\right).
}
\tag{5.3}
\]
它用上一步的真实最优回归系数，在新切片的低出生残差空间中重建并校正当前升层。由 (4.2)，
\[
\boxed{
\mathsf Z_n
=\mathcal R_{k+1,s}-\mathcal R_{k+1,s-1}\delta_{n+1}^*.
}
\tag{5.4}
\]
两项严格正交。因此它的实际联合能量是
\[
\boxed{
\|\mathsf Z_nf\|_{k+1}^2
=\langle(C_{n+1}+\delta_{n+1}L_{n+2}^{-1}\delta_{n+1}^*)f,f\rangle.
}
\tag{5.5}
\]
这一步保留了创新与上出生项的共同来源；不能把两个邻接高度的独立协方差夹逼当成对 (5.5) 的证明。

相应旧切片上的源能量为
\[
\left\|\mathcal R_{k-1,s}G_{n-1}C_nf\right\|_{k-1}^2
=\langle C_nG_{n-1}C_nf,f\rangle.
\tag{5.6}
\]
所以对于任何 \(\kappa>0\)，加强相邻不等式
\[
\kappa C_nG_{n-1}C_n-C_{n+1}
-\delta_{n+1}L_{n+2}^{-1}\delta_{n+1}^*\succeq0
\tag{5.7}
\]
**准确等价于**共同残差运输估计
\[
\boxed{
\|\mathsf Z_nf\|_{k+1}^2
\le\kappa\left\|\mathcal R_{k-1,s}G_{n-1}C_nf\right\|_{k-1}^2
\quad(f\in K_s).
}
\tag{5.8}
\]
\(n=h\) 时 (5.4) 的上出生项真实为零，其他项仍合法；没有给硬顶之外制造 \(G_{h+1}\)。

### 5.1 首边及小精度方向

当 \(n=1\) 时，\(\mathcal R_{s,s}\) 经 \(\mathcal V_s\) 就是源恒等映射，因此 (5.8) 成为
\[
\|\mathsf Z_1f\|_{s+2}^2\le\kappa\|C_1f\|^2.
\tag{5.9}
\]
等价地，一个从原物理源 \(K_s\) 出发的具体映射必须满足
\[
\boxed{
\left\|\frac12\left(
d^*\mathcal J_{1,s}
+\mathcal J_{3,s-1}L_3^{-1}L_2BC_1^{-1}
\right)\right\|\le\sqrt\kappa.
}
\tag{5.10}
\]
第二项与第一项在同一个 \(\mathcal H_{s+2}\) 中相加后再取范数。它补偿的是前一步回归，而不是任意上界。特别 \(C_1\) 很小的方向必须在这个共同映射中处理；对 \(d^*\mathcal J_{1,s}\) 单独估范数会丢失需要的抵消。

## 6. 深一出生项不会被回归表示消掉

对 \(s\ge2\) 记 \(B_-=C|_{K_{s-1}}\)、\(Y=B_-B\)。连续两次使用 (4.2)，从最低切片 \(s\) 升到 \(s+2\)，得到
\[
\begin{aligned}
\mathsf U_{s+1}\mathsf U_s\mathcal R_{s,s}
={}&2\mathcal R_{s+2,s}
-\mathcal R_{s+2,s-1}(L_3BC_1+3L_2B)\\
&+\mathcal R_{s+2,s-2}\Gamma_{4,s-2}Y.
\end{aligned}
\tag{6.1}
\]
三个残差空间正交。经物理等距映射并除以二，恰好得到既有 R288 三塔式
\[
\frac{(d^*)^2}{2}|_{K_s}
=\mathcal J_{2,s}C_2
-\frac12\mathcal J_{3,s-1}(BC_1+3L_3^{-1}L_2B)
+\frac12\mathcal J_{4,s-2}Y.
\tag{6.2}
\]
因而 \(Y^*\Gamma_{4,s-2}Y/4\) 是真正深一出生能量。新概率坐标没有删去它，也没有把全部低阶回归误压成单一均值。\(s=1\) 时这一项才为零。

## 7. 一个准确排除的实根捷径

不能仅因模型来自乘积权，就把所有 primitive 输入的完整 creation 范数生成式当作实根多项式。取真实四位权
\[
b=(1,2,3,4),\qquad f=(2,-1,4,-3)\in K_1,
\]
其中 \(b^*f=2-2+12-12=0\)。逐集合上升得到
\[
\sum_{j=0}^{3}\left\|\frac{(d^*)^j}{j!}f\right\|^2t^j
=30+308t+1290t^2+2500t^3
=(5t+1)(500t^2+158t+30).
\tag{7.1}
\]
二次因子判别式为 \(-35036\)，所以有非实根。这仅排除该实根推导路线；它不是 (5.7) 的反例，且本稿没有借此否定一般正性。

## 8. 已付与未付

本稿付清了任意正权、任意合法出生与高度的真实概率源、全部低阶残差空间、两带升层系数、桥创新及其共同范数目标，并保留顶硬端和 \(C^2\) 深塔。特别 (4.2)、(5.3)–(5.10) 给出了可以直接尝试定长子集耦合或回归能量比较的同源接口。

尚需证明的是 (5.8) 或至少首边 (5.9) 的一个与权、位数和出生无关的有限 \(\kappa\)。出生一的标量／协方差估计不能未经证明地推广到最高 \(s\) 次残差；逐位无权泄漏下界目前也没有独立支付这里的小 \(C_1\) 方向。原 graph 首物理头返回费用更未由本稿自动获得。

基础完整 incidence 与反向对偶见 [R239 任意出生倒数权对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)；实际三塔和完整 \(F_3\) Schur 次序见 [R288 一般出生三塔附录](R288-appendix-general-birth-three-tower-s1-schur-cancellation.md)。本稿全部推导在有限乘积权空间内完成，没有使用尚未公认的外部定理。

## 9. 有限精确复核

[原精确脚本](../notes/2026-11-14-all-birth-residual-regression-and-actual-bridge-789f-next.py) 用两个固定有理模型 \((1,2,3,4,5)\)、\((1,2,3,4,5,6)\) 的完整出生二层，核验概率残差与完整物理逆相等、全部低次 nuisance 正交性、连续两带系数、共同创新 Gram 和深塔 \(C^2\) 项。前一个模型覆盖真实硬顶，后一个覆盖通常第二高度。所有运算为精确有理数；这些是恒等式与归一校验，不是一般正性的有限扫描证据。当前完整运行通过，耗时约一秒。
