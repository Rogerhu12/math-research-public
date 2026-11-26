# R1007：原甲板相容 CM 对应对赋值一高度判据的障碍

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；global_route / root。

**状态：已证明的精确范围排除。**
下文证明一个实际 Picard 恒等式及整高度整除结论。
它说明，在所列同一整格与自伴条件下，原非平凡三阶甲板 CM 块
不能用原纯 CM 对应满足“对应特征模 $\ell$ 为零、而指定交叉高度
赋值恰一”的组合条件。它不是对二次 Chabauty 一般方法的否定，
也没有把 Serre 主目标或真正高度问题标为完成。

## 1. 原曲线、基点及甲板算子

固定 R593 的真实曲线
$$
X=X_1=Z_p,\qquad Y=W_p,\qquad \phi:X\longrightarrow Y,\quad v=a^3,
$$
以及 $\mu_3$ 固定的有理基点 $c_0$（$a=0$）。
令
$$
J=J_X,\quad \iota(x)=[x-c_0],\quad
q:J\longrightarrow A,\quad j(x)=q\iota(x).
\tag{1007.1}
$$
这里 $A$ 是 R593(593R.2) 的实际正 CM 型商，不是被撤回的反向扭曲。
在 $K=\mathbb Q(\zeta_3)$ 上，$\delta:a\mapsto\zeta_3a$ 是甲板生成元。
原已证明的关系为
$$
q\phi^*=0.
\tag{1007.2}
$$
置
$$
N=\phi^*\phi_*\in\operatorname{End}_{\mathbb Q}(J).
$$
pull–push 恒等式给
$$
N=1+\delta_*+\delta_*^2,\qquad N^2=3N,\qquad qN=0.
\tag{1007.3}
$$
$N$ 对 Jacobian 主极化 Rosati 自伴。因此对 R593 的实际伴随
$q^\dagger$ 也有
$$
Nq^\dagger=(qN)^\dagger=0.
\tag{1007.4}
$$

保留原甲板不变极化 $\lambda_A$、实际
$\kappa=qq^\dagger\in F$ 和
$$
F^0=\{h\in F:\operatorname{Tr}_{F/\mathbb Q}(\kappa h)=0\}.
\tag{1007.5}
$$
对 $h\in F^0$，原纯 CM 对应同态为
$$
Z_h=q^\dagger hq.
\tag{1007.6}
$$
需要整数对应时按原规范清除分母。其迹零条件是 (1007.5)，
不能删去 $\kappa$ 后改用 $\operatorname{Tr}(h)=0$。
$q,q^\dagger$ 都甲板相容，$h$ 与 CM 甲板元交换，所以 $Z_h$ 与 $\delta$ 交换。

## 2. 修改对角的实际 Picard 类

对称整数对应 $Z$ 若无对角分量且在全纯微分上的迹为零，
定义
$$
D_Z(y)=[\operatorname{Fix}Z-2Z(y)]\in J(\mathbb Q).
\tag{1007.7}
$$
迹零和 Lefschetz 次数公式保证它次数为零。

为避免把同态相容误当某个循环代表字面相容，直接在 Picard 群中说明。
对 $X\times X$ 上的对应线丛 $\mathcal C$，定义
$$
D_{\mathcal C}(y)=
\Delta^*\mathcal C-
\mathcal C|_{X\times\{y\}}-
\mathcal C|_{\{y\}\times X}.
\tag{1007.8}
$$
式中使用加法记线丛张量积。它杀掉从任何一个因子拉回的线丛。
用基点 $c_0$ 将两条轴上的限制刚性化后，剩余线丛由
$J\to J^\vee$ 的同态经 Poincaré 线丛唯一给出。
所以 (1007.8) 只依赖对应的 Jacobian 同态。
对实际对称循环，它与 (1007.7) 是同一 Picard 类。

假设 $Z\delta=\delta Z$ 作为 Jacobian 同态。
$\delta^\dagger=\delta^{-1}$，故
$(\delta\times\delta)^*\mathcal C$ 与 $\mathcal C$ 的同态相同；
两者之差只来自两因子的拉回。
由于 $\delta c_0=c_0$，由 (1007.8) 得
$$
\delta^*D_Z(c_0)=D_Z(c_0),\qquad
ND_Z(c_0)=3D_Z(c_0).
\tag{1007.9}
$$
结合 $qN=0$，
$$
\boxed{3qD_Z(c_0)=0.}
\tag{1007.10}
$$
对整数对应，这是整 Picard 类投影后的三挠结论，
没有声称 $qD_Z(c_0)$ 在 $A(\mathbb Q)$ 中必字面为零。
在 $A(\mathbb Q)\otimes\mathbb Q$ 或
$A(\mathbb Q)\otimes\mathbb Z_\ell$、$\ell\ge5$ 中它为零。
有理对应先清分母再用此式；除回的有理零结论成立，
但不能忽略清分母整数的 $\ell$ 赋值。

对原 $Z_h$，这也与 R593 的直接线丛身份一致：
若 $\mathcal L_h$ 是原对称刚性化线丛，则
$$
D_{\mathcal C_h}(c_0)=2j^*\mathcal L_h
 =2\phi^*\eta_h
 \quad\text{于 }\operatorname{Pic}^0(X)\otimes\mathbb Q.
\tag{1007.11}
$$
这里 $\eta_h$ 仍可能非挠；消失的只是其 $A$ 投影。
不能删掉 R593 完整高度公式中的 Picard 修正。

对任意 $y\in X(\mathbb Q)$，固定点除子相消给准确恒等式
$$
\boxed{D_Z(y)=D_Z(c_0)-2Z[y-c_0].}
\tag{1007.12}
$$
若 $qZ=Z_Aq$，则在上述 $\ell$ 进群中
$$
qD_Z(y)=-2Z_Aj(y).
\tag{1007.13}
$$
对于 (1007.6)，$Z_A=\kappa h$，并保留同一清分母因子。
它不是自由替换为 $h$。更换基点时必须同时保留 (1007.12)。

## 3. 同一真实整高度的整除命题

取 $\ell\ge5$，并令
$$
M=(J(\mathbb Q)/\operatorname{tors})\otimes\mathbb Z_\ell
$$
为真实整 Mordell–Weil 格。设
$b:M\times M\to\mathbb Q_\ell$ 是同一个双线性高度，满足：

1. $b(M,M)\subset\ell\mathbb Z_\ell$；
2. $N$ 与 $Z$ 均对 $b$ 自伴。

取 $G\in M$ 满足
$$
NG=0,\qquad ZG=\lambda G,\qquad\lambda\in\ell\mathbb Z_\ell.
\tag{1007.14}
$$
此时不需要假设 $G$ 原始，也不需要假设其对数深度。

由 (1007.9) 及 $N$ 自伴，
$$
3b(G,D_Z(c_0))
=b(G,ND_Z(c_0))
=b(NG,D_Z(c_0))=0.
$$
故 (1007.12) 和 $Z$ 自伴给
$$
\begin{aligned}
b(G,D_Z(y))
 &=-2b(G,Z[y-c_0])\\
 &=-2\lambda\,b(G,[y-c_0])
 \in\ell^2\mathbb Z_\ell
 \qquad(y\in X(\mathbb Q)).
\end{aligned}
\tag{1007.15}
$$
因此
$$
\boxed{v_\ell b(G,D_Z(y))\ne1}
\tag{1007.16}
$$
（零值的赋值取 $+\infty$）。
这是实际高度的整除恒等式，不只是缺少某个待核接口。

特别，另一 CM 点 $c_1$ 与 $c_0$ 的差可以非挠，
但一致改基点仍给 $-2\lambda$ 乘同一交叉高度，
不能因此绕开 (1007.16)。

## 4. 与新赋值判据的关系，以及不能省略的假设

Manvir Jaswal 的 2026 预印本
*The rational points of the non-split Cartan modular curve of level 121*，
Theorem 1.2(c)、Proposition 2.9、Proposition 3.2，
提出使用模 $\ell$ 的对应特征为零、指定交叉高度赋值为一的组合。
其中秩一块的特征取值于 $\mathbb F_\ell$，所以特征为零确是
其整标量 $\lambda\in\ell\mathbb Z_\ell$。
该方法还要求好素数、整性、饱和性和局部项控制。
本篇只识别这个组合条件的障碍，不引用其有理点主定理作已认可输入。

(1007.15) 的全部几何与代数证明已经在前面给出，
因此不依赖该新预印本的证明是否最终成立。

应用时仍必须针对**同一高度、同一实际格**核实第3节两项假设。
$\ell\nmid\#J(\mathbb F_\ell)$、$\ell$ 不整除坏处分量群指数，
以及合适的整 de Rham splitting，可用于建立高度整性；
不能因潜在好约化或有理张成就省略它们。
Hecke 稳定 splitting 的自伴性也必须真实运输到所用原对象。

若使用甲板相容的 Poincaré 高度，则 $N$ 自伴：
在 $K$ 上 $\delta$ 是等距算子，其伴随是 $\delta^{-1}$，
故 $1+\delta+\delta^2$ 自伴，再按 base change/trace 下降。
R593 §7 对原高度数据确有这种甲板平均。
但这不自动证明整个 $J$ 在任意辅助好素数上的整高度格。
本结果不更换原角色 $\chi$、splitting、$C_h$ 或有限高度目标集合。

另外，第3节的整性本身给一个简单的原始性检查。
若 $D\in M$、$G=\ell^rH$ 且 $H\in M$，则
$$
v_\ell b(G,D)\ge r+1.
\tag{1007.17}
$$
所以赋值恰一会强迫 $G\notin\ell M$。
$\log G\in\ell^2\operatorname{Lie}$ 与此不矛盾：
那是对数像不饱和，并不是 $G$ 在整 Mordell–Weil 格中可除。
原 $F\beta$ 的有理生成不能代替该整格论证。

### 4.1 整 splitting 的变化也不能恢复赋值一

进一步假设同一好约化模型上
$\log M\subset\ell\operatorname{Lie}$，两个 splitting 都是
同一整 $H^1_{\rm dR}$ 格中的拉格朗日直和补，且对数与高度归一相同。
两补的差是整线性映射；相应归一第三类微分之差为全纯微分，
其系数是该映射作用于 $\log Q$。
再对 $P$ 积分，得到
$
b'(P,Q)-b(P,Q)=B(\log P,\log Q),
\tag{1007.19}
$
其中 $B$ 是整双线性型。于是对 $P,Q\in M$，差在
$\ell^2\mathbb Z_\ell$ 中；若 $\log G\in\ell^2\operatorname{Lie}$，
取 $P=G$ 时差甚至在 $\ell^3\mathbb Z_\ell$ 中。
因此在这些额外整性条件下，换另一个整 splitting 也不能将
(1007.15) 改成赋值一。坏约化或分歧下降时，差矩阵的整性
必须另证，本段不自动适用。

## 5. 分歧基变换不能直接保留好素积分界

若想把一个要求 $\ell$ 不整除模水平的好约化判据直接用于原 $\ell=p$，
原水平含 $p$ 已不满足其前提。
潜在好约化本身不能修补这个差别。

一个基本的积分例子足以说明为何必须重算界。
在分歧指数为 $e$ 的扩域中取参数 $\pi$，
$v_\ell(\pi)=1/e$。积分微分 $t^{\ell-1}dt$ 在原点盘内给
$$
\int_0^\pi t^{\ell-1}dt=\frac{\pi^\ell}{\ell},
\qquad
v_\ell\left(\frac{\pi^\ell}{\ell}\right)=\frac{\ell}{e}-1.
\tag{1007.18}
$$
当 $e\ge\ell$ 时，连原来的正赋值结论也不能照搬。
此例只排除未作修改的基变换论证；Galois trace 或其它下降
可能改善具体对象的整性，须用真实格与实际点另外证明。

## 6. 排除范围与真正保留的入口

(1007.16) 排除的精确组合是：原非平凡 $\mu_3$ 块、
与甲板交换的对应（特别是原纯 $Z_h$）、同一整高度及自伴性、
$\lambda\in\ell\mathbb Z_\ell$，同时要求指定高度赋值为一。
它对所有有理基点同时成立。

后继 [R1008](R1008-wild-inertia-and-all-rational-correspondence-centralization.md)
已由真实三处野惯性证明：原 $X_1$ 和实际偶分支 $X_d$ 的全部
$\mathbb Q$-有理自对应都与 $\mu_3$ 交换。因此本节原先保留的
“新非甲板相容有理对应”入口现已关闭；(1007.16) 对这些曲线的
全部有理自对应适用，仍保第3节的整性、自伴和特征条件。

以下入口没有被排除：

- 甲板不变底曲线块 $NG=3G$；
- 原完整高度函数的其他二次项、线性项及局部项关系；
- 同时重算全部局部项与目标集合后的其他高度方法。

尤其 $\eta_h$ 及 R593 的底曲线交叉高度项不能被删除。
原高度与 O0 的全局覆盖仍开放。

## 来源

- [R593](R593-actual-quotient-height-and-uniform-bad-place-support.md)，§§1–7：真实曲线、固定基点、$q\phi^*=0$、加权迹、Picard 下降及同一高度数据。
- R596 §4 的修改对角及因子二；(1007.8)–(1007.15) 在本篇重新给出所需完整论证。
- Manvir Jaswal，*The rational points of the non-split Cartan modular curve of level 121*，2026，预印本，[作者页面](https://manvirjaswal.github.io/papers/xns-121/)，[PDF](https://manvirjaswal.github.io/papers/xns-121/jaswal-xns-121.pdf)，Theorem 1.2(c)（印刷第4页）、Proposition 2.9（第9页）、Proposition 3.2（第11页）。只用于准确定位所讨论的方法假设。
