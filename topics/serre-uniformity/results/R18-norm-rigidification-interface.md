# R18. 用沿有理除子的范数替代基点刚性化

日期：2026-11-12。会话：serre-uniformity-astra-cont；global_geometry。

**状态：已证明的代数计算接口。** 本结果把 R14 的规范平移接到实际的线丛族与纤维计算：用“对角纤维的 $d$ 次张量幂除以沿 $D$ 的范数”代替“对角纤维除以一个有理基点纤维”。整个表达式不要求选取有理基点、不要求选取 $d$ 次根，也不因代表线丛乘一个基底线丛而改变。

这处理 Hashimoto–Lido–Lombardo–Mascot–Parent, *Equationless quadratic Chabauty for non-split Cartan modular curves*, arXiv:2608.10919v1 (2026), Remark 3.8 和 Lemma 4.2.14 中的刚性化接口。这里只使用经典 Poincaré 双线性和有限平坦范数，独立给出证明；没有把该预印本的所有算法结论作为输入。没有声称已完成任意层的 QC 或统一点集排除。

## 1. 设置与规范纤维公式

先令 $S=\operatorname{Spec}k$，$k$ 是特征零域。也允许 $S$ 为离散赋值环的谱，且下述曲线在 $S$ 上光滑射影、几何纤维连通。令
$$\pi:\mathcal X\longrightarrow S,\qquad
\mathcal J=\operatorname{Pic}^0_{\mathcal X/S}.$$
令 $D\subset\mathcal X$ 是**有限 étale 的有效除子**，在 $S$ 上次数为 $d>0$。这已经覆盖本课题在好素数处使用的约化尖点除子。域情形中，有重数或负系数的除子也可用逐闭点张量幂的同一公式处理；证明在 §3 末给出。

令 $U$ 为 $S$ 概形，$x:U\to\mathcal X$ 为态射，$\mathcal T$ 为 $\mathcal X\times_S U$ 上沿 $U$ 相对次数零的实际线丛。记它的 Picard 类态射为
$$v:U\longrightarrow\mathcal J.$$
令 $a:\mathcal J^\vee\to\mathcal J$ 为 Abel–Jacobi 拉回所给的基点独立自对偶同构，符号与 R12、R14 一致；$\mathcal P$ 为 $\mathcal J\times_S\mathcal J^\vee$ 上的刚性化 Poincaré 线丛。

记 $\gamma_x:U\to\mathcal X\times_S U$ 为 $x$ 的图，$\pi_D:D\times_S U\to U$ 为有限 étale 投影。定义 $U$ 上的线丛
$$
\mathcal E_D(\mathcal T)
 =\bigl(\gamma_x^*\mathcal T\bigr)^{\otimes d}
   \otimes
 \operatorname{Nm}_{\pi_D}
    (\mathcal T|_{D\times_S U})^{-1}.
\tag{1.1}
$$
有限平坦范数可具体定义为
$$\operatorname{Nm}_{\pi_D}(L)
 =\det((\pi_D)_*L)\otimes
  \det((\pi_D)_*\mathcal O_{D\times_SU})^{-1};\tag{1.2}$$
因此在环上的计算是有限自由模的行列式运算。

**定理 1。** 存在与任意基变换、线丛同构和张量积相容的规范同构
$$
\boxed{\quad
\mathcal E_D(\mathcal T)
 \simeq
 (u_D\circ x,\ a^{-1}\circ v)^*\mathcal P,
 \qquad u_D(z)=[d z-D].
\quad}
\tag{1.3}
$$
特别地，若 $U$ 是 $\mathcal X$ 的开集且 $x$ 为包含，则 $\gamma_x$ 是对角线在 $U$ 上的限制，(1.3) 就是所需的无基点计算公式。

这里不把 $\mathcal E_D(\mathcal T)$ 先随意识别为 $\mathcal O_U$。它是实际的 Poincaré 拉回线丛；若 R14 的条件使它平凡，还需要选择一个处处非零截面。这个全局标量歧义与原有基点公式的标量歧义同类，并非 $d$ 次根歧义。

## 2. 基底因子与同构的全部标量恰好抵消

任取 $U$ 上的线丛 $A$，并把 $\mathcal T$ 换为
$$\mathcal T'=\mathcal T\otimes\pi_U^*A.$$
对角拉回多出 $A$，故 (1.1) 第一因子多出 $A^{\otimes d}$。而范数的投影公式给出
$$\operatorname{Nm}_{\pi_D}(\pi_D^*A)\simeq A^{\otimes d}.$$
两因子规范抵消，所以
$$\mathcal E_D(\mathcal T')\simeq\mathcal E_D(\mathcal T).\tag{2.1}$$

若一个线丛同构被乘以基底上的单位 $\alpha\in\mathcal O_U^\times$，则它在第一因子上的作用为 $\alpha^d$，在范数因子上的作用也是 $\alpha^d$，所以在 $\mathcal E_D$ 上作用恒等。这是**同构层面的**抵消，而不只是在 Picard 群中得到同一个类。

因此，在只知道相对 Picard 类的情形，可以在一个忠实平坦覆盖上选择实际代表线丛；重叠处相差的基底线丛和同构标量在 (1.1) 中消失，给出规范下降。存在代表线丛的 Brauer 障碍不会转化为本表达式的标量选择障碍。

## 3. 规范同构的证明：局部选基点再消去它

光滑满射 $\mathcal X\to S$ 在 étale 局部有截面。再作有限 étale 基变换，可以同时选择截面 $b:S\to\mathcal X$，并把 $D$ 分解为 $d$ 个截面 $P_1,\ldots,P_d$ 的不交和。下述构造对基变换相容，最后检查它不依赖这些选择，从而下降。

设 $i_b(z)=[z-b]$，$y=a^{-1}v:U\to\mathcal J^\vee$。将 $\mathcal T$ 沿 $b$ 规范化：
$$
\mathcal T_b=\mathcal T\otimes
 \pi_U^*\bigl((b\times\mathrm{id}_U)^*\mathcal T\bigr)^{-1}.
\tag{3.1}
$$
它沿 $b\times U$ 有自然平凡化。由 Poincaré 线丛的刚性化泛性质，存在唯一保持该平凡化的同构
$$\mathcal T_b\simeq(i_b\times y)^*\mathcal P.\tag{3.2}$$
由 §2，$\mathcal E_D(\mathcal T_b)$ 规范等于 $\mathcal E_D(\mathcal T)$。在 $D$ 已分裂的覆盖上，范数是各纤维的张量积。将 (3.2) 代入 (1.1)，并用 Poincaré 在第一变量的双线性，得到
$$
\begin{aligned}
\mathcal E_D(\mathcal T)
 &\simeq \mathcal P_{(i_bx,y)}^{\otimes d}
       \otimes\bigotimes_{j=1}^d
          \mathcal P_{(i_bP_j,y)}^{-1}\\
 &\simeq\mathcal P_{(d i_bx-\sum_j i_bP_j,\,y)}\\
 &=\mathcal P_{([d x-D],\,y)}.
\end{aligned}
\tag{3.3}
$$
这就是 (1.3)。最后一个等号是
$$d[x-b]-\sum_j[P_j-b]=[d x-D].$$

若换成基点 $b'$，(3.1) 只是再次乘以一个基底线丛；§2 的同构层面抵消说明 (3.3) 不改变。更直接地，$i_{b'}=i_b-t$，其中 $t=[b'-b]$；第一因子带入 $-d t$，$d$ 个范数因子共带入同一个 $-d t$，两者在双线性同构下相消。截面 $P_j$ 的重新编号也不改变张量积。Poincaré 的双线性满足结合与交换的相容性，因而重叠覆盖上的同构一致，能够下降到 $S$。定理 1 得证。

域情形的一般除子 $D=\sum_P n_P P$，可将 (1.1) 中范数改为
$$\bigotimes_P\operatorname{Nm}_{k(P)/k}
  \bigl(\mathcal T|_{P\times U}\bigr)^{\otimes n_P}.$$
在分裂域上仍是按重数的纤维张量积，其总指数为 $d=\sum_Pn_P[k(P):k]$，所以 §2 和 (3.3) 完全相同。这里不要求 $D$ 有效。

这个规范同构也可写成经典 Deligne 配对公式
$$\mathcal E_D(\mathcal T)
 =\langle\mathcal O(d\gamma_x-D\times U),\mathcal T\rangle_{\mathcal X\times U/U}.$$
但上面的证明没有把配对—Poincaré 识别作为未经解释的黑箱。若采用正极化 $\lambda$ 的另一种符号约定，通常会出现一个逆线丛；本结果用 $a=i_b^*$ 固定符号，(3.3) 明确消除了这个歧义。

## 4. 从实际对应显式构造所需的次数零族

回到特征零域 $k$。设 $\mathcal B$ 是 $X\times X$ 上的实际线丛，且其限制 $\mathcal B_y$ 在第一个 $X$ 上有固定次数 $n$。令它诱导的 Jacobian 同态为
$$F:J\to J,$$
其约定由
$$[\mathcal B_y\otimes\mathcal B_z^{-1}]=F([y-z])\tag{4.1}$$
确定。令 $f=a^{-1}F:J\to J^\vee$，并假设 R14 所需的次数零条件成立。Hecke 对应的实际 Cartier 线丛可在此作为 $\mathcal B$。

取 R14 的实际范数线丛 $\mathcal M_D$，它表示 $\eta_D$。沿第二变量的 $D$ 定义第一个 $X$ 上的线丛
$$\mathcal W_D=
 \operatorname{Nm}_{X\times D/X}(\mathcal B|_{X\times D}).\tag{4.2}$$
对有重数或负系数的域上除子，仍用逐闭点范数张量幂。它的次数是 $dn$。在 $X\times X$ 上定义
$$
\boxed{\quad
\mathcal T_D=\mathcal B^{\otimes d}
  \otimes\mathrm{pr}_1^*\mathcal W_D^{-1}
  \otimes\mathrm{pr}_1^*\mathcal M_D^{-1}.
\quad}\tag{4.3}
$$
每个第一变量纤维的次数为 $dn-dn-0=0$。

**定理 2。** $\mathcal T_D$ 的 Picard 类态射是
$$v_D(y)=F(u_D(y))-\eta_D=a(h_Du_D(y)),\tag{4.4}$$
其中 $h_D=f-a^{-1}\eta_D$ 是 R14 的规范仿射修正。于是
$$\mathcal E_D(\mathcal T_D)
 \simeq(u_D,h_Du_D)^*\mathcal P\simeq\mathcal O_X.\tag{4.5}$$

**证明。** 在分裂域上写 $D=\sum_Pn_PP$。由 (4.1)，
$$
\begin{aligned}
[\mathcal B_y^{\otimes d}\otimes\mathcal W_D^{-1}]
 &=\sum_Pn_P[\mathcal B_y\otimes\mathcal B_P^{-1}]\\
 &=F\left(\sum_Pn_P[y-P]\right)
 =F([d y-D]).
\end{aligned}
$$
减去 $[\mathcal M_D]=\eta_D$ 即得到 (4.4)，它是基域上的等式。再应用定理 1 及 R14 得到 (4.5)。证毕。

因此，从实际对应得到目标 Poincaré 纤维的步骤均是张量幂、范数、拉回和既有线丛的逆；不需要先知道某个有理曲线点，也不需要通过开 $d$ 次根来猜测刚性化。

在好约化 DVR 上，只要 $D$ 延拓为有限 étale 除子，且实际对应线丛 $\mathcal B$ 和 $\mathcal M_D$ 已在光滑模型上给定，同一构造逐项定义于 DVR。其 Picard 类等式在泛纤维成立，因相对 Jacobian 分离而在整个基底成立。由 R14 定理 2，(4.5) 的平凡化可取为积分且处处非零。

## 5. 纤维值与有限精度运算

定理 1 识别的纤维，在域值点 $y$ 处是
$$
(\mathcal T_D)_{(y,y)}^{\otimes d}
 \otimes\operatorname{Nm}_D((\mathcal T_D)|_{D\times\{y\}})^{-1}.
\tag{5.1}
$$
这正是用实际次数零除子 $d y-D$ 评价 $\mathcal T_D|_{X\times\{y\}}$ 的线。选择 (4.5) 的一个处处非零截面，便得到 R14 的 torsor 提升在该纤维中的实际非零元素。

若在所用开集上选择 $\mathcal T_D$ 的有理截面 $\tau$，且它在对角与 $D\times U$ 的泛点上均不恒零或恒无穷，则
$$
(\gamma^*\tau)^{\otimes d}\otimes
 \operatorname{Nm}_{D\times U/U}(\tau|_{D\times U})^{-1}
\tag{5.2}
$$
是 $\mathcal E_D(\mathcal T_D)$ 的有理截面。它若有除子，须计算并除去一个给出该主除子的有理函数，才得到所需的处处非零截面；不能把任意 (5.2) 直接当作提升。交点处使用线丛的局部生成元和转移函数，原式 (1.1) 仍然有定义；单纯把一个零或无穷的数作除法当然无效。

对于 $R/\ell^mR$ 上有限 étale 的 $D$，范数可以在有限自由代数中以行列式实现。若一个局部生成元的变化由单位 $z$ 给出，则范数变化为乘法算子 $m_z$ 的行列式；因此在有限精度下不必分裂 $D$，也不必求其各个几何点。$z$ 是单位时 $\det m_z$ 也是单位。

本式解决的是表示与刚性化的兼容性。计算任意层的高维全局截面空间、找到主除子函数、控制有限精度误差和计算 Mordell–Weil 闭包仍有各自的代价；这里没有把它们隐藏在“规范”一词中。

## 6. 本课题中可直接使用的范围

在 $X_{\rm ns}^+(p)$ 上取约化尖点和 $D$，次数 $d=(p-1)/2$。Deligne–Rapoport 的标准模模型中，尖点除子在 $\mathbb Z[1/p]$ 上有限 étale；这一性质见 A. Sutherland, *Counting points on modular curves* (AGCT 2019) 的模曲线定义页：[讲义](https://math.mit.edu/~drew/AGCT2019.pdf)。因此在所考虑的辅助好素数 $\ell\ne p$ 处，$D$ 可在光滑模模型上作为有限 étale 除子使用。这使用模模型的尖点性质，不能仅由尖点的定义域不分歧就推断任意模型中尖点互不相交。若只使用 $\ell\ge5$，也避开粗模空间在小特征下需要额外讨论的表现。

R14 与 R18 合起来，给出无已知有理 CM 基点层上如下完整的代数链条：

1. 用 $u_D$ 代替基点 Abel–Jacobi 映射；
2. 用 R14 的范数类 $\eta_D$ 作规范平移；
3. 用 (4.3) 构造实际次数零线丛族；
4. 用 (1.1) 和 (1.3) 计算 Poincaré 拉回，所有基底标量自动抵消；
5. 在好约化模型上选取积分平凡化。

仍未解决的是：坏约化素数处的分量修正、有效的生成元与主除子函数、随层增长的计算/精度控制，以及每个残数圆盘与每个局部高度分支的非 CM 共同根排除。特别是 (1.3) 不是 QC 集合只含 CM 点的判据。

## 7. 文献核对

- S. Hashimoto, G. M. Lido, D. Lombardo, N. Mascot, P. Parent, *Equationless quadratic Chabauty for non-split Cartan modular curves*, [arXiv:2608.10919v1](https://arxiv.org/abs/2608.10919), 2026。PDF 原编号是 **Remark 3.8**、**Lemma 4.2.14**；其有基点公式为 (4.2.1)–(4.2.2)。本结果的 (1.1) 在 $D=b$、$d=1$ 时恰恢复“对角纤维除以基点纤维”。
- P. Deligne, *Le déterminant de la cohomologie*, in *Current Trends in Arithmetical Algebraic Geometry*, Contemporary Mathematics 67 (1987), 93–177；[IAS 书目与原文](https://publications.ias.edu/node/404)。Deligne 配对是同一范数表达式的一般框架；本证明已直接从刚性化 Poincaré 的泛性质推导所需识别。
- J. S. Milne, *Jacobian Varieties* (1986), §6；[作者修订版](https://jmilne.org/math/xnotes/JVs.pdf)。用于符号已固定的自对偶同构。
