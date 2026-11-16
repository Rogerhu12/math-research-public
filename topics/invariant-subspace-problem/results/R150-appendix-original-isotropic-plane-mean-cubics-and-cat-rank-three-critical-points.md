# 原等向平面的均值兼容三次曲线与真正 Cat 秩三临界点

作者：Astra-ISP-789f / normal_annihilator。AI-assisted: GPT-6 Astra Pro。  
日期：2026-11-16 UTC。

状态：**已证明；两个完整参数模型与两个特征零数域点均实际验证。** 在两个已付原等向平面 $W_\pm$ 上，保留全部原物理 Hankel 条件后，均值的完整临界兼容性在一个明确非空开集上由两个三次因子的乘积控制。其中一个是原 Cat 降秩三次式，另一个是不同的三次式。

后一个因子确实承载 **Cat 均值秩三、第三普通矩本质维数三** 的原完整临界点。本稿给出两个确切三次数域中的点，并核全部 $33$ 个原梯度。由此，不能以“全原临界均值必 Cat 秩至多二”为消去目标；所有 Cat 三阶 minor 的幂也不可能都属于原完整梯度理想。

这些点属于已经分类的 $W_\pm$ 支，三个原匹配 Bell 值仍全部为零。它们不构成匹配 Bell 结论的反例。真正未闭合部分仍是 Bell 非零、从而第三矩本质维数至少四的原临界支。

## 1. 原平面、原支撑与原最高梯度

保留 [全部本质三维的完整分类](R150-appendix-all-essential-cubic-dimensions-at-most-three-have-zero-matched-bell-values.md) 的两个平面。令

$$
P_+(z)=z^3-5z^2+\frac{32}{5}z-\frac85,
\qquad
P_-(z)=z^3+27z^2+\frac{864}{5}z+\frac{864}{5}.
$$

写 $P_\sigma(z)=z^3+p_2z^2+p_1z+p_0$，定义 $E_\sigma\in\operatorname{Mat}_{6\times3}(\mathbb Q)$：

- 前三行为三阶单位矩阵；
- 对 $i=3,4,5$，逐列用递推
  $E_i=-p_2E_{i-1}-p_1E_{i-2}-p_0E_{i-3}$。

这固定了同一原有理基，不是任取投影坐标。原二次式为

$$
Q_\sigma(U)=U^{\mathsf T}C_\sigma U,
$$

$$
C_+=
\begin{pmatrix}
279&121&608\\121&-521&-608\\608&-608&-1024
\end{pmatrix},
\qquad
C_-=
\begin{pmatrix}
-1769&1369&5024\\1369&-969&-5024\\5024&-5024&-1024
\end{pmatrix}.
$$

此次程序独立精确核

$$
E_\sigma^{\mathsf T}KE_\sigma=0,\qquad
E_\sigma^{\mathsf T}Kv(z)=P_\sigma(z)\psi_\sigma(z),\qquad
Q_\sigma(\psi_\sigma(z))=0
\tag{1.1}
$$

的全部原系数。两个 $C_\sigma$ 均非退化。

令均值参数为 $a=(a_0,a_1,a_2)^{\mathsf T}$，$y=E_\sigma a$。只在本节明确的共同支撑范围内取

$$
H\in\mathcal H_2\cap\operatorname{Sym}^2W_\sigma,\qquad
V\in\mathcal H_3\cap\operatorname{Sym}^3W_\sigma.
\tag{1.2}
$$

完整第三普通矩写为

$$
T_3(r)=\widetilde T_3(E_\sigma^{\mathsf T}r),\qquad
\widetilde T_3(U)=(a\cdot U)^3-6(a\cdot U)H_W(U)+4V_W(U).
$$

[原完整矩判据](R150-appendix-isotropic-three-plane-moment-critical-sections-and-matched-bell-values.md) 在这一准确共同支撑范围给

$$
\nabla\mathcal Q_3=0
\quad\Longleftrightarrow\quad
\widetilde T_3=Q_\sigma\,\ell
\quad\text{对某个一次式 }\ell.
\tag{1.3}
$$

本稿保留并重核其物理支撑前提，没有仅凭 $y\in W_\sigma$ 就断言其他矩也支撑于该平面。

## 2. 全物理交空间与十个原系数

在 $\operatorname{Sym}^2\mathbb Q^3$ 的六个普通对称坐标上，施加全部原 Hankel 等式

$$
(ESH E^{\mathsf T})_{ij}=(ESH E^{\mathsf T})_{kl}
\quad\text{当 }i+j=k+l.
$$

这里 $SH$ 表示一般三阶对称矩阵。对上三角 21 个位置按十一条 anti-diagonal 合并，得到完整 $10\times6$ 约束，两个符号都实际秩三。因此 (1.2) 中的二阶物理交空间维数恰为三。

同理，对三阶对称张量的十个坐标，保留原 56 个无序三指标位置按十六个总和分组的全部等式，得到完整 $40\times10$ 约束。两个符号都实际秩七，三阶物理交空间也恰为三。

所有核均由完整 RREF 的原 free-I 规范得到，并核完整原约束乘回。回到原张量后，全部 36 个二阶位置与全部 216 个三阶位置的 Hankel 等式保留。因此可取确定的有理基

$$
H_W=\sum_{\nu=1}^3h_\nu H_\nu(U),\qquad
V_W=\sum_{\nu=1}^3v_\nu V_\nu(U).
\tag{2.1}
$$

在全部十个普通三次单项式上，(1.3) 准确等价于

$$
A_H(a)h+C_0(v,\ell)^{\mathsf T}=-c(a),
\tag{2.2}
$$

其中：

$$
A_H(a)=\operatorname{coeff}_3\big(-6(a\cdot U)H_\nu(U)\big)_{\nu=1}^3,
$$

$$
C_0=\operatorname{coeff}_3
\big(4V_1,4V_2,4V_3,-Q_\sigma U_0,-Q_\sigma U_1,-Q_\sigma U_2\big),
$$

$$
c(a)=\operatorname{coeff}_3((a\cdot U)^3).
$$

这是原 $10\times9$ 参数线性系统，不是只取某几个必要系数。

$C_0$ 的实际秩是六。令 $L$ 是 $C_0^{\mathsf T}$ 的完整 $10\times4$ 左核基，原 free-I 规范固定。全部原乘积 $L^{\mathsf T}C_0=0$ 通过，而且核维数完整。因此 (2.2) 相容当且仅当

$$
A(a)h=-b(a),\qquad
A(a)=L^{\mathsf T}A_H(a)\in\operatorname{Mat}_{4\times3}(\mathbb Q[a]),
\quad b(a)=L^{\mathsf T}c(a).
\tag{2.3}
$$

没有在这个消去过程中漏掉 $V$ 或 $\ell$ 的自由方向。

## 3. 真均值兼容因子

令 $C_\sigma^{\rm Cat}(a)$ 是
$\operatorname{Cat}(E_\sigma a)$ 全部四个三阶 minor 的 primitive 整数公因子，取 $a_0^3$ 系数为正。实际所有非零 minor 都是该三次式的非零有理常数倍；它在两个符号下的 $a_0^3$ 系数分别为 $64$、$746496$。因此

$$
\operatorname{rank}\operatorname{Cat}(E_\sigma a)=3
\quad\Longleftrightarrow\quad C_\sigma^{\rm Cat}(a)\ne0.
\tag{3.1}
$$

程序从 (2.3) 的全部原条目精确计算增广行列式，完整系数乘回给：

$$
\boxed{
\det[A(a),b(a)]
=\kappa_\sigma C_\sigma^{\rm Cat}(a)R_\sigma(a),
}
\tag{3.2}
$$

其中

$$
\kappa_+=\frac3{7343653900},\qquad
\kappa_-=\frac1{10669430952158400}.
$$

第二个 primitive 三次式分别为

$$
\begin{aligned}
R_+(a)={}&22475476032a_0^3-79578650944a_0^2a_1
+8624859280a_0^2a_2\\
&-59981484864a_0a_1^2+159198806880a_0a_1a_2
-51639754895a_0a_2^2\\
&+214593704512a_1^3-343274602800a_1^2a_2
+157629721905a_1a_2^2-21488509950a_2^3,
\end{aligned}
$$

$$
\begin{aligned}
R_-(a)={}&165348799195327488a_0^3
+440095375734672384a_0^2a_1
+40085972603282880a_0^2a_2\\
&+388563179761188864a_0a_1^2
+69855169362287040a_0a_1a_2
+3026156669239635a_0a_2^2\\
&+113719115184570368a_1^3
+30195679886568960a_1^2a_2
+2556975337923835a_1a_2^2
+67253624923350a_2^3.
\end{aligned}
$$

$R_\sigma$ 与 $C_\sigma^{\rm Cat}$ 不成常数比例。完整 factor 乘积与原增广行列式逐系数相等；没有只比较次数。

在开集 $\operatorname{rank}A(a)=3$ 上，(3.2) 为相容性的充分必要条件：一个 $4\times3$ 满列秩矩阵的增广秩仍为三，当且仅当这个四阶 determinant 为零。相容时 $h$ 唯一；$C_0$ 满列秩又使 $(v,\ell)$ 唯一。

因此在

$$
\operatorname{rank}A(a)=3,\qquad C_\sigma^{\rm Cat}(a)\ne0
\tag{3.3}
$$

的原参数范围内，完整临界条件准确化为

$$
\boxed{R_\sigma(a)=0.}
\tag{3.4}
$$

这是一条真实原参数支结论，而非新增孤立数值样本。低秩集 $\operatorname{rank}A<3$ 尚不能仅凭 (3.2) 作充分性判断；本稿没有删除这个边界。

## 4. 两个特征零数域中的完整原正点

取 $a=(1,0,\xi)$。分别令 $\xi$ 满足以下 primitive 整数多项式：

$$
f_+(\xi)=
21488509950\xi^3+51639754895\xi^2
-8624859280\xi-22475476032,
\tag{4.1}
$$

$$
f_-(\xi)=
22417874974450\xi^3+1008718889746545\xi^2
+13361990867760960\xi+55116266398442496.
\tag{4.2}
$$

它们分别是 $R_+(1,0,\xi)$、$R_-(1,0,\xi)$ 的非零常数倍。实际独立不可约性证书是：

- $f_+$ 的模 $103$ 次数仍为三，全部 103 个域元素都不是根；
- $f_-$ 的模 $139$ 次数仍为三，全部 139 个域元素都不是根。

次数三无一次因子即不可约。因此两个 $f_\sigma$ 在 $\mathbb Q$ 上都不可约，给确切特征零数域

$$
K_\sigma=\mathbb Q[\xi]/(f_\sigma).
$$

这两个小素数只证明数域模多项式不可约；它们没有用于把有限域临界点提升成有理临界点。

在 $K_\sigma$ 中，程序直接求解 (2.2) 的全部十行九列。两个符号都实际秩九，全部十个方程逐项乘回。所有求逆都用精确多项式扩展 Euclid，并在原数域中乘回为一。

由唯一解定义 $h,v,\ell$，再用 (2.1) 和原 $E_\sigma$ 构成

$$
y_\sigma=E_\sigma(1,0,\xi)^{\mathsf T},\quad H_\sigma,\quad V_\sigma.
\tag{4.3}
$$

(2.2)、(4.1)–(4.3)、原 free-I 基和唯一线性解给完整确定的代数点；完整坐标由冻结生成器重建。此次实际另将它们运回原坐标，并独立核以下全部身份：

$$
\operatorname{rank}\operatorname{Cat}(y_\sigma)=3,
\qquad
\operatorname{rank}\operatorname{ess}(T_{3,\sigma})=3,
\tag{4.4}
$$

以及全部原 33 个梯度，而不只依赖支撑定理的推论。

具体而言，先在原六坐标中计算 $p=Ky$、$F=y^{\mathsf T}Ky/2$、原 $N,\Gamma$ 与原最高梯度；程序核

$$
-6\,\operatorname{antiDiag}(KNK)=0,\qquad
3K\Gamma=0,\qquad
4\ell_{\rm orig}+16J_3V=0.
\tag{4.5}
$$

这里 $\ell_{\rm orig}$ 是原 Schur 模型的 $p^3-6(KHK)p$ 系数向量，与 (1.3) 的三变量一次式 $\ell$ 区分。式 (4.5) 是 $11+6+16=33$ 条原方程，在三次数域中共 99 个有理坐标，两个符号均全部为零。

全部 36 个原 $H$ 位置和 216 个原 $V$ 位置也逐项核同一 Hankel anti-diagonal。第三普通矩的本质秩由其三个一阶偏导在完整六个二次单项式上的真实秩三验证。没有只把 $\ell\ne0$ 当作省略全部秩核验的理由。

由 (4.4) 与原 $10\times9$ 秩九，(3.3) 的开集在每个 $R_\sigma=0$ 支上确实非空。

## 5. 对均值消去理想与真正主缺口的意义

记原完整梯度理想为

$$
J=(\nabla\mathcal Q_3)\subset\mathbb Q[y,H,V].
$$

(4.3)–(4.5) 给 $J$ 的特征零点，同时至少一个原 Cat 三阶 minor 非零。因此：

$$
\boxed{
I_3(\operatorname{Cat}(y))\not\subseteq\sqrt J.
}
\tag{5.1}
$$

同样，全部 Cat 三阶 minor 不会都落入均值消去理想
$J\cap\mathbb Q[y]$ 的根式。若其中一个非零 minor 的某次幂属于 $J$，代入相应数域点便得到一个非零域元素等于零，矛盾。

这与 [原 Cat 秩三空纤维及非零均值消去多项式](R150-appendix-original-cat-rank-three-full-macaulay-rank4368-and-mean-elimination.md) 不冲突。后者给一个非空均值开集无临界点；本稿在它的真实异常零集中支付了两条已知安全支上的正点。

这些正点的完整第三矩为 $Q_\sigma\ell$。原三个匹配方向均满足 $Q_\sigma(E_\sigma^{\mathsf T}r_j)=0$，所以它们的三个 Bell 值全部零，完全属于已付的本质维数三分类。

因此后继不能把“所有 Cat 秩三纤维为空”作为目标。真正有待排除的是某个匹配 Bell 非零的原临界点。该问题应保完整原梯度，并对每个匹配方向使用

$$
J+(1-\eta B_{r_j})
$$

或等价的原 Bell 非零饱和接口，先剥离已付 Bell 零支。仅饱和三个 Bell 的乘积会只覆盖三者同时非零的开集，不能替代“至少一个非零”的完整量词。由旧完整分类，该真正未闭合部分才必有 $\dim\operatorname{ess}(T_3)\ge4$。

## 6. 两次真实计算与可重现身份

两步均为授权后的本地 executor 实际执行，没有 GitHub Actions run ID。使用 Python 3.12.14、SymPy 1.14.0、python-flint 0.9.0。

| 项目 | 参数兼容性 | 两个原数域正点 |
|---|---:|---:|
| 数学用时 | 1.148088401 秒 | 0.408871297 秒 |
| 完成状态 | exit 0 | exit 0 |
| 完整原物理 $H$ 约束 | $10\times6$，秩三 | 全 36 位置 |
| 完整原物理 $V$ 约束 | $40\times10$，秩七 | 全 216 位置 |
| 原三次系数 | 全十个，未删 | 全十个乘回 |
| 原完整梯度 | 由完整支持判据 | 每个符号 33 条、99 有理坐标 |
| Cat / 本质秩 | 全参数模型 | 每个符号均 $3/3$ |

两份冻结源：

- [完整参数兼容性](../notes/2026-11-16-r150-original-isotropic-plane-mean-compatibility-789f.py)：Git blob 044e5ffbc078a0e404324af4a1bd457550f2fa80，10935 B，SHA256 a0fdc5849f43d481701926acef3141b4bee498e7a8cae20b39cd37b21c4ad323。
- [原数域点与全部梯度验证](../notes/2026-11-16-r150-original-isotropic-plane-cat3-critical-points-789f.py)：Git blob 2e2bfec7c82b436eb47784749f04e060b8aca84d，14719 B，SHA256 cb9cd6d933eb64dbab823a8e0d685329b32bbeddc7bf5b90436444a2319c1596。

[冻结参数](../notes/2026-11-16-r150-original-isotropic-plane-compatibility-and-cat3-points-inputs-789f.json) 保全部 CLI、依赖版本及两步输入绑定。[执行 manifest](../notes/r150-nonrankone-execution-789f/20261116-local-isotropic-plane-cat3-critical-points.json) 只含源码、参数、执行身份与输出 SHA。

完整参数临时模型为 26409 B，SHA256：

~~~text
17ecc103fd28b5e617353eda80c417494d2de03ca49836d6c64eb3c2e64f9f66
~~~

其实际回执为 9081 B，SHA256：

~~~text
2bc10ce59803dc4f6a5170b3c1ab5bd4c6ce5ac792b78bf2444743315bfa253b
~~~

参数 binding：

~~~text
ed7174cd2a10d5eee4ddfa45f4d764385c6899f87c209b8d96696e82a9124956
~~~

两个完整原数域点的临时模型为 23525 B，SHA256：

~~~text
969f61a81956a9712eeb9df01da5989939115e4ad5f6c1423689da52393a900c
~~~

实际正点回执为 2925 B，SHA256：

~~~text
e25979602982923666385c370e7dc8f64eee300931434e065b1b5e7e798aebd9
~~~

正点 binding：

~~~text
0715aebdcb12a2feed9acdd36fe54ec70d98b0be7191833275d5fab2011c6d37
~~~

按仓库规则15，完整计算模型和数域点数组均只保在临时目录。两个点由数域多项式、原平面基、完整物理交空间与唯一线性解确定；源码可忠实重建并逐全部原梯度核验，不依赖没有来源含义的数值近似。
