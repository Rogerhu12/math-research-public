# R150 附录：非割线均值、本质三维的完整原临界分类

日期：2026-11-14（UTC）。作者：normal_resume_2220 / Astra-ISP-1cf8c51d。

状态：**已证明。** 在原六模立方的完整临界方程中，若均值的 \(4\times3\) Hankel catalecticant 秩为三、普通第三矩的本质维数为三，则全部临界点均属于两个已知全等向物理三点平面 \(W_+\)、\(W_-\)。外均值整类为空；内均值的准确完整条件是原投影二次式 \(Q_\pm\) 整除完整第三矩。原三个匹配 first Bell 值在这个整个截面上为零。

本稿汇集已经逐条证明并发布的整支结果，给出完整的必要与充分陈述。它不把这个有限临界截面的完成扩张为全部均值秩、全部本质维数或原 Jacobian 的全局自然幂证书。

## 1. 原数据与分类定理

保留原 \(K\)、物理曲线 \(v(z)=(1,z,\ldots,z^5)\)、原完整 \(\mathcal Q_3(y,H,V)\)，以及
\[
T_3(r)=(y^{\mathsf T}r)^3-6(y^{\mathsf T}r)H(r,r)+4V(r,r,r).
\]
记 \(\mathcal H_2,\mathcal H_3\) 为原合并键定义的 Hankel 对称二阶、三阶张量空间。均值假设为
\[
\operatorname{rank}(y_{j+k})_{0\le j\le3,\ 0\le k\le2}=3.
\tag{1.1}
\]
令 \(W=\operatorname{ess}(T_3)\)，并假设 \(\dim W=3\)。

两个平面 \(W_\sigma\) 是下列三次式的三根对应物理向量的张成：
\[
P_+(z)=z^3-5z^2+\frac{32}{5}z-\frac85,
\]
\[
P_-(z)=z^3+27z^2+\frac{864}{5}z+\frac{864}{5}.
\tag{1.2}
\]
两三次式都无重根。取唯一的基矩阵 \(E_\sigma:\mathbb C^3\to W_\sigma\)，使其前三行是三阶单位矩阵；其余行由 (1.2) 的线性递推确定。这正是[两个平面的完整矩判据](R150-appendix-isotropic-three-plane-moment-critical-sections-and-matched-bell-values.md)中的有理基。

在该基下定义
\[
Q_\sigma(u)=u^{\mathsf T}C_\sigma u,
\]
\[
C_+=\begin{pmatrix}
279&121&608\\121&-521&-608\\608&-608&-1024
\end{pmatrix},
\quad
C_-=\begin{pmatrix}
-1769&1369&5024\\1369&-969&-5024\\5024&-5024&-1024
\end{pmatrix}.
\tag{1.3}
\]
它们均非退化，且原投影曲线的齐次核理想正好是 \((Q_\sigma)\)。

**定理。** 在 (1.1)、\(\dim\operatorname{ess}(T_3)=3\) 的原允许显示点中，
\[
\nabla\mathcal Q_3=0
\]
当且仅当存在 \(\sigma\in\{+,-\}\)，使
\[
y\in W_\sigma,\qquad
H\in\mathcal H_2\cap\operatorname{Sym}^2W_\sigma,\qquad
V\in\mathcal H_3\cap\operatorname{Sym}^3W_\sigma,
\tag{1.4}
\]
且唯一满足
\[
T_3(r)=\widetilde T_3(E_\sigma^{\mathsf T}r)
\]
的三变量形式有
\[
\boxed{\widetilde T_3=Q_\sigma\,\ell}
\tag{1.5}
\]
对某个一次齐次式 \(\ell\) 成立。当前本质维数三假设保证 \(T_3\ne0\)，所以这里 \(\ell\ne0\)。定理仍保留原 Cat 条件 (1.1)，不把它从支撑平面归属中自动推断。

## 2. 必要性：内均值已分类，外均值全部排除

先分 \(y\in W\) 与 \(y\notin W\)。

内均值的整个原截面已由[内均值完整支撑分类](R150-appendix-inside-mean-complete-critical-support-classification.md)证明：必 \(W=W_+\) 或 \(W=W_-\)，且前三累积量均支撑于该平面。它包含全部 \(H,V\) 降秩、双 jet、两不同点、内部奇点、坐标轴奇点及无穷图。再由[两平面完整矩判据](R150-appendix-isotropic-three-plane-moment-critical-sections-and-matched-bell-values.md)，完整临界性给 (1.5)。

对外均值，[原 conormal 与四 jet 支撑归约](R150-appendix-essential-cubic-conormal-and-four-jet-support-reduction.md)先给唯一的准确长度四物理 Artin 支撑及同一原 \(\lambda\) 的矩关系。不能把这个支撑任意替换为四个泛点。

[全部外均值降秩排除](R150-appendix-no-secant-cuspidal-companion-and-outer-mean-rank-drop-exclusion.md)排除了 \(\operatorname{rank}H<4\)。剩下满 \(H\) 后，长度四除子的五种重数类型已经全部支付：

| 支撑重数 | 原整类结论及证明 |
|---|---|
| \(4\) | [四重 jet 排除](R150-appendix-quadruple-jet-supports-have-no-full-rank-outer-mean-critical-point.md) |
| \(3+1\) | [三重 jet 加单点排除](R150-appendix-three-plus-one-full-rank-outer-mean-critical-exclusion.md) |
| \(2+2\) | [两个二重 jet 排除](R150-appendix-two-plus-two-full-rank-outer-mean-critical-exclusion.md) |
| \(2+1+1\) | [conic 与单点半权支](R150-appendix-two-one-one-conic-and-single-half-weight-critical-exclusion.md)、[双点块半权节点支](R150-appendix-two-one-one-double-half-node-critical-exclusion.md)、[双点块半权非节点支](R150-appendix-two-one-one-double-half-nonnode-critical-exclusion.md)共同排尽 |
| \(1+1+1+1\) | [四不同外均值完整截面为空](R150-appendix-reduced-four-point-outer-mean-critical-section-is-empty.md)，连同其已列出的有基点、单点半权、零配对、相等配对、零 \(Z\)、零 \(h\) 独立整支排除 |

这五项穷尽所有长度四复除子的重数分割。每一项都保留原最高与低阶完整梯度及必要的局部乘法秩条件，而不是只排掉必要降秩矩阵的几个样本。因此整个外均值截面为空。

原临界点只能处于内均值类，必要性证明完成。

## 3. 充分性保留完整允许矩

反过来，设原允许数据满足 (1.4)、(1.5) 及定理的两个秩条件。由 \(E_\sigma^{\mathsf T}KE_\sigma=0\)，原二次式 \(F_0=\tfrac12Y^{\mathsf T}KY\) 在 \(W_\sigma\) 上恒零。

以原前三累积量构造次数六的截断形式矩泛函；其生成函数为
\[
\exp\!\left(y\cdot t-H(t,t)+\frac23V(t,t,t)\right)\pmod{\deg t>6}.
\tag{3.1}
\]
因 \(y,H,V\) 全支撑于 \(W_\sigma\)，(3.1) 经 \(E_\sigma^{\mathsf T}t\) 因子化，所以整个有限矩泛函支撑于该平面。这一步使用全部三个累积量；没有仅凭 \(y\in W_\sigma\) 推断完整矩支撑。高于三阶的累积量在 (3.1) 取零，是原允许显示点。

[完整矩判据](R150-appendix-isotropic-three-plane-moment-critical-sections-and-matched-bell-values.md)已逐项核验：对平面支撑的有限 ordinary 泛函，原 \(F_0^3\) 的全部完整导数为零，当且仅当 \(Q_\sigma\mid\widetilde T_3\)。其中一、二阶导数含正次 \(F_0\)，在平面上消失；三阶导数准确给完整 \(T_3\) 在原物理投影二次曲线上的值；更高显示导数恒零。于是 (1.5) 给完整临界性，充分性成立。

这个论证保留原 Hankel 合并键，也不要求形式矩来自正测度。

## 4. 原三组选定 first Bell 值在整个截面上为零

原平方证明选出的三个方向 \(r_j=(A_j,B_j,0,0,0,1)\) 同时满足
\[
Q_+(E_+^{\mathsf T}r_j)=Q_-(E_-^{\mathsf T}r_j)=0.
\tag{4.1}
\]
其准确构造已在[两平面完整矩判据第五节](R150-appendix-isotropic-three-plane-moment-critical-sections-and-matched-bell-values.md)给出：令 \(d_j\) 遍历
\[
3725d^3-43931504d^2+6080833024d+52565262336=0
\]
的三个已隔离实根，取
\[
A_j=-\frac{521d_j^2-46784d_j+271360}{160(5d_j-704)},\qquad B_j=A_j+d_j.
\]
各分母非零，且 (4.1) 是已证明的精确代数身份。

在本稿的每一个原完整临界点上，定理给
\[
\mathcal Q_{(r_j\cdot Y)^3}
=\widetilde T_3(E_\sigma^{\mathsf T}r_j)
=Q_\sigma(E_\sigma^{\mathsf T}r_j)\ell(E_\sigma^{\mathsf T}r_j)=0.
\tag{4.2}
\]
回到原 first \(a_j=iA_jU_1+B_jU_2+U_6\) 只乘非零标量 \(i^3\)，所以三个原匹配 Bell 值仍为零。完整第三矩 Schur 换元在临界点的相应附加变量为零，因此同一结论适用于其已定义的匹配 \(S_r=B_r\)。

## 5. 此定理支付的边界与继续任务

已经完成的是原完整临界簇中 **Cat 均值秩三、普通第三矩本质维数三** 的全部支撑与矩判据；不是只在一个稠密开图或固定权重样本上成立。该类的外均值完全不存在，内均值恰是 (1.4)—(1.5)。

仍未由本稿支付的事项包括：

- 均值 catalecticant 秩至多二的完整临界分类；
- 普通第三矩本质维数四、五、六；
- 由整个全局 Jacobian 理想得到原匹配 Bell 的某个自然幂归属；
- 把相应实际 Bell 算子逆与同一自然域闭合连接到目标算子。

尤其，(4.2) 是本稿整个已分类截面上的消失结论，不能单凭它断言全局自然幂，不能据此宣布普通复 Hilbert 不变子空间问题完成。本轮继续 open.md 的 Cat 秩二、本质第三矩维数三、\(\operatorname{ess}V\le3\) 分支，并与满 \(\operatorname{ess}V=4\) 分支分工。
