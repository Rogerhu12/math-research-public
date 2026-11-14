# R33. 对称对应的显式范数平凡化与实际 Hecke 分量数据

日期：2026-11-12。会话：serre-uniformity-astra-cont；global_geometry。

**状态：已证明。** 对实际对称对应，R14、R18 的泛纤维平凡化可由线丛和范数直接消去，剩余只是一维常数线的基选择。对 $X_{\rm ns}^+(p)$ 的小次数 Hecke 对应，本文证明实际水平闭包的多度数确为超奇异 Brandt 矩阵，并证明沿全部尖点的范数没有垂直缺陷。最终积分障碍还包含**实际对角拉回的多度数**，不能只取 Brandt 对角元。最后给出一个真实 Hecke 格的秩结论：至少 $g-n$ 个独立 trace-zero 对应的全光滑开集垂直障碍为零，其中 $g$ 为曲线亏格、$n$ 为超奇异分量数。

单个 $T_\ell$ 一般不满足 R14 的次数零条件。以下用于 R14 的对应都是满足该条件的**实际整数线性组合**；允许负系数，解释为实际线丛的对偶张量幂。本文不把所有 $T_\ell$ 自动称为 trace-zero，也不把积分障碍消失称为最终 QC 共同零点排除。

## 1. 对称线丛族的泛纤维消去

先设 $X/k$ 为特征零域上的光滑射影几何连通曲线，$D$ 为次数 $d>0$ 的有效除子。设 $\mathcal B$ 为 $X\times X$ 上的实际线丛，给定相容于交换两因子的对称同构
$$\tau^*\mathcal B\simeq\mathcal B.$$
实际对称 Cartier 对应 $Z=\tau Z$ 的 $\mathcal O(Z)$ 具有这种同构。设它沿两个变量的次数均为 $n\in\mathbb Z$。记
$$K_{\mathcal B}=\Delta^*\mathcal B,\qquad
W_D=\operatorname{Nm}_{X\times D/X}(\mathcal B|_{X\times D}).\tag{1.1}$$
于是 $\deg W_D=dn$。假设
$$\deg K_{\mathcal B}=2n.\tag{1.2}$$
令 $F:J\to J$ 为 $\mathcal B$ 诱导的同态，$f=a^{-1}F$，符号同 R14、R18。

**定理 1。**

1. R14 的特殊次数零类满足
   $$\eta_D=[K_{\mathcal B}^{\otimes d}\otimes W_D^{-2}].\tag{1.3}$$
2. 可用以下实际族代表 R18 的规范类态射：
   $$\mathcal T_D'
   =\mathcal B^{\otimes d}\otimes
   \operatorname{pr}_1^*(W_D\otimes K_{\mathcal B}^{-d}).\tag{1.4}$$
3. 设 $C_D$ 为一维 $k$ 向量空间
   $$C_D=\operatorname{Nm}_{D/k}
   \bigl((W_D\otimes K_{\mathcal B}^{-d})|_D\bigr).\tag{1.5}$$
   则有规范线丛同构
   $$\boxed{\quad\mathcal E_D(\mathcal T_D')
   \simeq C_D^{-1}\otimes_k\mathcal O_X.\quad}\tag{1.6}$$
   任取 $C_D^{-1}$ 的一个非零向量，即得到实际的处处非零平凡化截面。

**证明。** 在一个闭点 $P$ 的定义域上，以 $P$ 刚性化 $\mathcal B$，得到
$$\mathcal B_P^{\rm norm}
=\mathcal B\otimes\operatorname{pr}_1^*(\mathcal B|_{X\times P})^{-1}
\otimes\operatorname{pr}_2^*(\mathcal B|_{P\times X})^{-1}
\otimes\mathcal B_{(P,P)}.$$
最后一因子是常数线；它使两个轴上的刚性化相容。此线丛就是 $(i_P,fi_P)^*\mathcal P$ 的双变量版本。拉回对角线，利用对称性，得到 Picard 类
$$\kappa_P=[K_{\mathcal B}]-2[\mathcal B|_{X\times P}].$$
对 $D$ 的闭点取带重数的范数并相乘，正好得到 (1.3)。作为实际线丛，同构还可以带一个常数线因子；它不改变 Picard 类，在 $\mathcal E_D$ 中又由 R18 的基底因子消去规范抵消。因此可选 (1.3) 右侧的实际线丛代表 $\eta_D$。

将此代表代入 R18 的
$$\mathcal B^d\otimes\operatorname{pr}_1^*W_D^{-1}
\otimes\operatorname{pr}_1^*\mathcal M_D^{-1}$$
即得 (1.4)。其第一变量次数为 $dn+dn-d(2n)=0$。对角拉回时，两个 $K_{\mathcal B}$ 因子完全抵消：
$$\Delta^*\mathcal T_D'=W_D.$$
沿第一个变量的 $D$ 取范数时，对称性把 $\operatorname{Nm}_{D\times X/X}(\mathcal B)$ 规范识别为 $W_D$，故
$$\operatorname{Nm}_{D\times X/X}(\mathcal T_D')
=W_D^{\otimes d}\otimes(C_D\otimes_k\mathcal O_X).$$
在评价—范数表达式中再次消去 $W_D^d$，得到 (1.6)。证毕。

此处没有要求 $D$ 有有理点，也没有开 $d$ 次根。定理 1 的消去本身甚至不需要 $D$ 为 Hecke 特征除子；Hecke 的尖点性质只用于下一节把 $W_D$ 写成明确除子。得到 (1.6) 仍要求实际线丛、其范数及相应同构能够被表示和计算，但不再需要另找一个未知高维全局主函数。

## 2. 真正的整数 Hecke 组合与次数零条件

取 $X=X_{\rm ns}^+(p)/\mathbb Q$、$p\ge17$，$D$ 为全部尖点之和，$d=(p-1)/2$。令 $Z_\ell$ 为 $\ell\ne p$ 的通常 Hecke 对应，$\Delta$ 为恒等对应。考虑
$$Z=a_0\Delta+\sum_{\ell\in S}a_\ell Z_\ell,
\qquad a_0,a_\ell\in\mathbb Z,\tag{2.1}$$
以及实际线丛 $\mathcal B=\mathcal O(Z)$。负系数按对偶张量幂解释。双次数是
$$n=a_0+\sum_{\ell\in S}a_\ell(\ell+1).\tag{2.2}$$
对偶同源反转 $Z_\ell$；复合的标量 $[\ell]$ 不改变非分裂 Cartan 正规化子结构，故 $Z_\ell$ 与其转置相同，$\mathcal B$ 对称。

全部尖点在 $\mathbb Q$ 上是一个 Galois 轨道，见 R4 命题 G1。Hecke 对应保持尖点，其在除子上的作用定义于 $\mathbb Q$，所以 $T_\ell(D)$ 的每个几何尖点系数相同。总次数为 $(\ell+1)d$，故
$$T_\ell(D)=(\ell+1)D,\qquad Z(D)=nD.\tag{2.3}$$
有限态射的除子范数给出保持规范有理截面的实际同构
$$W_D\simeq\mathcal O_X(nD).\tag{2.4}$$

令 $F=a_0+\sum a_\ell T_\ell$ 作用于 $H^0(X,\Omega^1)$。在特征零，交对应与对角线的 Lefschetz 公式给出
$$\deg K_{\mathcal B}=Z\cdot\Delta
=2n-2\operatorname{Tr}(F|H^0(X,\Omega^1)).\tag{2.5}$$
这里 $H^0$ 与 $H^2$ 的迹各为 $n$，$H^1$ 分解为互为共轭的两个微分部分；这些定义于 $\mathbb Q$ 的 Hecke 作用在两部分的迹相同。该等式对实际整数虚对应线性成立，包括对角线自交。

因此 R14 的次数零条件在这里精确等价于
$$\operatorname{Tr}(F|H^0(X,\Omega^1))=0
\quad\Longleftrightarrow\quad\deg K_{\mathcal B}=2n.\tag{2.6}$$
例如 $gT_\ell-\operatorname{Tr}(T_\ell)\mathrm{id}$ 给一个满足条件的整数组合；是否非零须另看该 Hecke 算子。以下涉及 R14 的断言都假设 (2.6)。

结合定理 1，实际族可写为
$$\boxed{\quad
\mathcal T_D'
=\mathcal B^{\otimes d}\otimes
\operatorname{pr}_1^*(\mathcal O(nD)\otimes K_{\mathcal B}^{-d}).
\quad}\tag{2.7}$$

## 3. 最小正则模型共同奇点的重数

记号同 R28、R30，基底为 $R=\mathbb Z_p^{\rm ur}$。最小正则模型 $\mathcal X$ 的特纤维所有分量在共同点 $P$ 相交，$U=\mathcal X^{\rm sm}$。令
$$\rho=\operatorname{ord}_{\mathfrak m_P}(p),$$
即特纤维在正则曲面点 $P$ 处的重数。

**定理 2。**
$$\boxed{\quad\rho=\frac{p-\left(\frac{-3}{p}\right)}6
=\begin{cases}(p-1)/6&p\equiv1\pmod3,\\(p+1)/6&p\equiv2\pmod3.\end{cases}\quad}\tag{3.1}$$

**证明。** 沿 R28 §6 的交矩阵，从 Edixhoven–Parent 的正规交叉模型实际收缩。先收缩全部非例外的 $D_i$，它们自交 $-1$；这使相应 $E_i$ 自交变为 $-1$，再收缩全部 $E_i$。中央 $A$ 的自交遂变为 $-1$，故接着收缩 $A$。

若 $p\equiv1\pmod3$，普通 $j=0$ 链 $A-B-C$ 的 $B$ 此时自交变为 $-1$，收缩后 $C$ 自交变为 $-1$。最后收缩的是重数 $(p-1)/6$ 的 $C$。若 $p\equiv2\pmod3$，超奇异 $j=0$ 链的 $D_0$ 此时自交 $-1$，收缩后 $E_0$ 自交变为 $-1$；最后收缩的是重数 $(p+1)/6$ 的 $E_0$。超奇异 $j=1728$ 的保留分量不改变这条顺序。这些自交计算均由单次收缩的公式 $M'_{ij}=M_{ij}+M_{iE}M_{jE}$ 得到。

最后一次 $(-1)$ 曲线收缩的逆是对光滑曲面点 $P$ 的一次吹起。纤维方程在 $P$ 的消失重数恰等于该次吹起的例外曲线在总拉回纤维中的系数。因此分别等于上述最后分量的重数，得到 (3.1)。证毕。

**推论 3（低次数闭点避开共同奇点）。** 若 $L/K$ 有限，$x\in X(L)$ 的整数延拓特化到 $P$，则 $e(L/K)\ge\rho$，从而 $[L:K]\ge\rho$。

**证明。** 局部映射 $\mathcal O_{\mathcal X,P}\to\mathcal O_L$ 把 $\mathfrak m_P$ 送入 $\mathfrak m_L$。因 $p\in\mathfrak m_P^\rho$，有 $v_L(p)\ge\rho$。证毕。

这一点值推论本身不证明某个二维对应闭包处处有限。下一节只在参数特纤维的**泛点 DVR** 上使用它，那里会另行证明有限平坦性。

## 4. 小 Hecke 对应的实际闭包、范数和 Brandt 矩阵

对一个素数 $\ell\ne p$，令 $\overline Z_\ell$ 为 $Z_\ell$ 在正则空间 $\mathcal X\times_RU$ 中的纯水平闭包，$\mathscr B_\ell=\mathcal O(\overline Z_\ell)$。固定 $U_j$ 的泛点 $\eta_j$，记
$$A_j=\mathcal O_{U,\eta_j}.$$
它是 DVR，一致化参数仍为 $p$，剩余域为 $k(U_j)$。

**引理 4（在这个 DVR 上确实有限平坦）。** $\overline Z_\ell$ 到 $U$ 的投影在 $\operatorname{Spec}A_j$ 上是有限平坦次数 $\ell+1$ 的有效 Cartier 除子族。

**证明。** 其到 $\operatorname{Spec}A_j$ 的映射真，泛纤维次数 $\ell+1$。如果闭纤维含有整个目标曲线分量 $C_i\times\eta_j$，那么在原三维空间中取闭包会使 $\overline Z_\ell$ 包含整垂直素除子 $C_i\times U_j$。两者维数均为 $2$，这将是 $\overline Z_\ell$ 的一个垂直不可约分量，与纯水平闭包的定义矛盾。因此所有纤维有限，真且拟有限即有限。无垂直分量又保证坐标有限模无 $p$-挠性，故在 DVR 上平坦；秩由泛纤维确定为 $\ell+1$。证毕。

这不声称原投影在整个二维参数空间 $U$ 上有限，也不从 $U(R)$ 的点值信息推断闭包的全部纤维。

假设
$$\ell+1<\rho.\tag{4.1}$$
把引理 4 的泛纤维分解为有限域扩张后，各分支的总次数至多 $\ell+1$。正规化和真性给出到 $\mathcal X$ 的整数延拓。若某分支在特纤维映到 $P$，推论 3 的同一个局部环论证在 $A_j$ 上给出其分歧度至少 $\rho$，矛盾。因此
$$\overline Z_\ell\cap(P\times\eta_j)=\varnothing.\tag{4.2}$$

**定理 5（范数无垂直缺陷）。** 当 (4.1) 成立时，泛纤维上的尖点范数同构唯一延拓为
$$\operatorname{Nm}_{D_{\mathcal X}\times_RU/U}
   (\mathscr B_\ell|_{D_{\mathcal X}\times_RU})
\simeq\mathcal O_U((\ell+1)D_{\mathcal X}).\tag{4.3}$$
此式保持规范有理截面，沿每个 $U_j$ 的垂直缺陷均为零。

**证明。** R30 证明 $D_{\mathcal X}$ 的特殊支集就是 $P$。由 (4.2)，在 $\operatorname{Spec}A_j$ 上，$\mathscr B_\ell$ 的规范截面限制到 $D_{\mathcal X}$ 后是单位：闭纤维支集不遇该对应，而泛纤维的相关范数除子是 Hecke 作用于尖点的除子。有限平坦范数把单位送到单位，故规范范数的 $U_j$ 赋值为零。另一方面 $D_{\mathcal X}\cap U$ 在特纤维没有支集，所以 (4.3) 右侧的规范有理截面在 $A_j$ 上也为单位。

在泛纤维，同构由 (2.3) 给出；可能的差异只是一项垂直除子，而上述计算使所有垂直系数为零。$U$ 正则，故该有理同构处处延拓为单位同构。这里使用的是 codimension-one 除子检查，没有假设整个 Hecke 闭包有限平坦。证毕。

**定理 6（实际多度数确为 Brandt 数）。** 对 (4.1) 下的 $\ell$，选取对应于 $C_i$ 的超奇异椭圆曲线 $E_i/k$。则 $\mathscr B_\ell$ 的第一变量多度数为
$$\boxed{\quad
H_{ij}(\ell)
=\#\{G\subset E_j:\ |G|=\ell,\ E_j/G\simeq E_i\}.
\quad}\tag{4.4}$$
右侧按子群计数，不再除以目标或源的自同构数。特别地
$$\sum_iH_{ij}(\ell)=\ell+1,\qquad
e_iH_{ij}(\ell)=e_jH_{ji}(\ell).\tag{4.5}$$

**证明。** 在 $A_j$ 的分式域上，泛 Hecke 纤维参数化椭圆曲线的 $\ell+1$ 个循环 $\ell$ 子群。必要时作有限扩域取得椭圆曲线和全部子群。源的 $j$ 在此 DVR 整，并特化为 $j_j$：$U_j$ 位于未被收缩的 Drinfeld 分量内部，遗忘 $j$-映射在那里正则，特值是该超奇异不变量。

因此源具有潜在好约化，进一步有限扩域后成为好约化，其约化同构于 $E_j$。因 $\ell\ne p$，$\ell$ 挠点有限 étale，几何 $\ell$ 子群的专门化是双射。对应的同源延拓到好约化模型，商的约化就是 $E_j/G$。定理 5 之前的低次数论证已经保证每个目标分支避开 $P$；于是其所在分量必须是目标约化 $j$ 值标记的 $C_i$。

引理 4 保证有限平坦总次数不变。即使分支在闭纤维合并，Cartier 相交数也按其专门化长度计数，恰为对应几何子群的数目。因此实际线丛的多度数等于 (4.4)，而不是仅有集合层面的对应。

列和是 $E_j$ 的全部循环 $\ell$ 子群数。若 $N_{ij}$ 是次数 $\ell$ 的实际同源 $E_j\to E_i$ 数，则
$$N_{ij}=2e_iH_{ij}(\ell).$$
对偶同源给 $N_{ij}=N_{ji}$，得到 (4.5)。证毕。

因此本文是在具体小次数范围内证明实际 Hecke 闭包的多度数等于 Brandt 数据；没有对未经检查的任意坏约化对应直接作这种识别。

## 5. 任意真实整数组合的剩余修正公式

对 (2.1) 取实际延拓
$$\mathscr B=\mathcal O\left(a_0\overline\Delta+
\sum_{\ell\in S}a_\ell\overline Z_\ell\right)
\quad\text{在 }\mathcal X\times_RU\text{ 上}.$$
记 $H_{ij}$ 为它的第一变量多度数。令 $K_{\mathscr B}$ 为 $\gamma^*\mathscr B$ 从 $U$ 到 $\mathcal X$ 的唯一线丛延拓，存在唯一性由 R28 的删去 codimension-two 点论证给出；记
$$\nu_i=\deg(K_{\mathscr B}|_{C_i}).\tag{5.1}$$
令 $W_{\mathcal X}=\mathcal O_{\mathcal X}(nD_{\mathcal X})$。定义沿尖点范数的垂直缺陷 $\tau_j$，符号由
$$
\operatorname{Nm}_{D_{\mathcal X}\times U/U}(\mathscr B)
\simeq W_{\mathcal X}|_U\otimes
\mathcal O_U\left(\sum_j\tau_jU_j\right)
\tag{5.2}
$$
固定；此同构保留泛纤维的 (2.4)。这里的 $\tau_j$ 总能定义，因为泛纤维同构已给定。对角线没有该缺陷；若每个 $\ell\in S$ 都满足 (4.1)，则定理 5 给 $\tau_j=0$，而定理 6 给
$$H=a_0I+\sum_{\ell\in S}a_\ell H(\ell).\tag{5.3}$$

取 (2.7) 的实际延拓
$$\mathscr T
=\mathscr B^d\otimes\operatorname{pr}_1^*
  (W_{\mathcal X}\otimes K_{\mathscr B}^{-d}).\tag{5.4}$$
其多度数是
$$\boxed{\quad\delta_i^{(j)}
=dH_{ij}+n r_i-d\nu_i,\qquad r_i=6/e_i.\quad}\tag{5.5}$$
因 (2.6)，各列之和为零。

**定理 7（实际积分障碍）。** 采用定理 1 的泛纤维平凡化，并用以下一维 $R$-模的一个基固定常数：
$$\operatorname{Nm}_{D_{\mathcal X}/R}
   (W_{\mathcal X}\otimes K_{\mathscr B}^{-d}),$$
其在原 $\mathcal E_D(\mathscr T)$ 上的垂直系数是 $-d\tau_j$。R30 乘二并修正后，最终系数精确为
$$\boxed{\quad
k_j=6n+d\bigl[e_j(H_{jj}-\nu_j)-2\tau_j\bigr].
\quad}\tag{5.6}$$
全 $U$ 上存在积分平凡化当且仅当方括号内的量与 $j$ 无关。若 (4.1) 对所有使用的 Hecke 素数成立，则该条件简化为
$$\boxed{\quad e_j(H_{jj}-\nu_j)\ \text{不依赖于 }j.\quad}\tag{5.7}$$

**证明。** (5.5) 直接来自 (5.4) 的三个因子。其对角拉回是 $W_{\mathcal X}|_U$。沿第一变量 $D$ 的范数是 (5.2) 的 $d$ 次幂，再乘上述常数 $R$-线。因此同定理 1 的消去给出
$$\mathcal E_D(\mathscr T)
\simeq\mathcal O_U\left(-d\sum_j\tau_jU_j\right)
\otimes(\text{常数 }R\text{-线})^{-1}.$$
选常数线的 $R$-基后，规范泛纤维截面的赋值确是 $-d\tau_j$。R30 的式 (6.4) 随即给
$$k_j=-2d\tau_j+e_j\delta_j^{(j)}.$$
代入 (5.5) 及 $e_jr_j=6$ 得 (5.6)。R28 的全 $U$ 判据给最后两项。证毕。

这条公式明确区分三种数据：$H$ 来自真实对应的第一变量纤维，$\nu$ 来自真实对角拉回，$\tau$ 来自真实尖点范数。低次数论证确定 $H$、消去 $\tau$，但**没有消去 $\nu$**。

对单个 $Z_\ell$，若 $Q_\ell$ 为其泛纤维固定点除子，$\lambda_{\ell,j}$ 为对角拉回规范有理截面的垂直赋值，则
$$K_{\mathscr B_\ell}\simeq
\mathcal O_{\mathcal X}\left(\overline Q_\ell+\sum_j\lambda_{\ell,j}C_j\right),
\qquad
\nu_i(\ell)=\overline Q_\ell\cdot C_i+
\sum_j\lambda_{\ell,j}M_{ij}.\tag{5.8}$$
若对角拉回在某特纤维分量上恒消失，$\lambda_{\ell,j}$ 就可能非零。对恒等对应，$K_{\overline\Delta}=\omega_{\mathcal X/R}^{-1}$，因而
$$\nu_i(\mathrm{id})=2-2p_a(C_i)+C_i^2\tag{5.9}$$
由伴随公式得到。式 (5.8)–(5.9) 是实际算术交数，不能用 $H_{ii}$ 代替。它们也说明只看 Brandt 矩阵对角项不足以判断哪条 trace-zero 对应的局部修正恒定。

## 6. 至少 $g-n$ 个真实 Hecke 方向的垂直障碍消失

本节不需要限制 Hecke 素数大小；它使用完整的实际对应及 R30 的乘二构造，因而允许 (5.2) 中的 $\tau$ 非零。

令 $\mathbb T\subset\operatorname{End}(J)$ 为有理定义的非分歧 Hecke 算子生成的整数 Hecke 格，取其无挠加法群；$g=\dim J$。Chen–Edixhoven–de Smit 的 Hecke 相容同源把 $J$ 识别到 $J_0^+(p^2)$ 的新部分；新形式的重数一分解给出
$$\dim_{\mathbb Q}(\mathbb T\otimes\mathbb Q)=g.$$
这是通常的交换半单 Hecke 代数，各新形式的系数域次数之和为 $g$。令
$$\mathbb T_0=\{F\in\mathbb T:
\operatorname{Tr}(F|H^0(X,\Omega^1))=0\}.$$
它的秩为 $g-1$，因为恒等算子的迹为 $g\ne0$。

对 $F\in\mathbb T_0$，记 R14 的规范仿射修正为 $h_F=f_F+c_F$，定义实际线丛
$$\mathscr L_F=(u_D,2h_Fu_D)^*\mathcal P^{\rm ext}
\quad\text{在 }U\text{ 上}.\tag{6.1}$$
R30 保证第二坐标落在对偶 Néron 恒等分量。R14 保证其泛纤维平凡。

**定理 8。** 存在秩至少 $g-n$ 的子格
$$\mathbb T_{\rm int}\subset\mathbb T_0$$
使每个 $F\in\mathbb T_{\rm int}$ 的 $\mathscr L_F$ 在整个 $U$ 上平凡。对任何实际对称对应代表，这恰等价于 (5.6) 的 $k_j$ 为常向量。

**证明。** 泛纤维平凡线丛在 $U$ 上的类群是
$$\ker\bigl(\operatorname{Pic}(U)\to\operatorname{Pic}(X_K)\bigr)
\simeq\mathbb Z^n/\mathbb Z\mathbf1.\tag{6.2}$$
满射来自垂直除子；核恰为常向量，因为若一个垂直除子主，其函数在完整泛纤维上处处非零，故属于 $K^\times$，沿全部约化分量具有相同赋值。此群秩为 $n-1$。

R14 的 $F\mapsto\eta_{D,F}$ 对加法相容：它由固定 Abel–Jacobi 拉回的 Poincaré 线丛、逐闭点范数及张量积定义。因此 $F\mapsto h_F$ 亦对加法相容。Poincaré 在第二变量的双线性给出
$$\mathscr L_{F+G}\simeq\mathscr L_F\otimes\mathscr L_G.$$
所以 (6.1) 定义一个真正的群同态
$$\mathbb T_0\longrightarrow\mathbb Z^n/\mathbb Z\mathbf1.$$
其核的秩至少是 $(g-1)-(n-1)=g-n$，而在该核中线丛类为零，正是存在整 $U$ 平凡化。R28 及定理 7 证明与 $k_j$ 常值的等价性。证毕。

本节在有理 Hecke 格上作整数线性代数，不是先在 $\mathbb Q_\ell$ 向量空间中得到核再未经证明地声称核含有同样多的有理点。它也没有给出这些子格生成元的统一系数界；有效寻找它们仍需 (5.5)–(5.8) 的实际数据。

定理 8 只消去几何积分提升的垂直障碍。若要把它表述为某个具体 QC 高度函数的坏素数贡献恒定，还须固定该高度与此 Poincaré torsor 规范化之间的识别；不能省略高度定义、归一化或其他局部项。辅助好素数处的二阶系数、Mordell–Weil 闭包及全部共同根排除更不由此推出。

## 7. 文献和已证明范围

- R14、R18、R28、R30 给出本文使用的无基点规范平移、实际族、积分范数和分量公式。本结果的对称范数消去、DVR 上的小次数有限平坦论证、Brandt 识别及格的秩估计均已在上文展开证明。
- B. Edixhoven and P. Parent, **Regular models of modular curves in prime level over $\mathbb Z_p^{\rm ur}$**, *Documenta Mathematica* **29** (2024), 1017–1058, DOI [10.4171/DM/974](https://doi.org/10.4171/DM/974)；[期刊全文](https://content.ems.press/assets/public/full-texts/serials/dm/29/5/14298148/online/10.4171-dm-974.pdf)。Theorem 3.4、Corollary 3.2 的正规交叉模型与收缩是 §3 的输入；实际收缩顺序和最后重数已自行计算。
- B. de Smit and B. Edixhoven, **Sur un résultat d'Imin Chen**, *Mathematical Research Letters* **7** (2000), 147–153；[作者全文](https://pub.math.leidenuniv.nl/~smitbde/papers/2000-de_Smit_Edixhoven.pdf)，Theorems 1–2：非分裂正规化子 Jacobian 与相应新部分的同源来自对有限群作用的函子性构造，因此与非分歧 Hecke 作用相容。§6 仅使用这一已发表同源和经典新形式重数一分解，不把点集间的映射当作该同源的后果。
- J. S. Balakrishnan, N. Dogra, J. S. Müller, J. Tuitman and J. Vonk, **Quadratic Chabauty for modular curves: algorithms and examples**, *Compositio Mathematica* **159** (2023), 1111–1152；[期刊全文](https://www.cambridge.org/core/journals/compositio-mathematica/article/quadratic-chabauty-for-modular-curves-algorithms-and-examples/C317E63BB0128EB3F2163621CA63E66E)。§5.5 对 $X_{\rm ns}^+(17)$ 明确选择真实 Hecke 组合以使坏素数高度消失；这说明这样的选择有实际先例，但其具体高度结论不是本文 (6.2) 自动等同的定义。本文未把该特定层的计算推广为所有层的 QC 点集排除。
