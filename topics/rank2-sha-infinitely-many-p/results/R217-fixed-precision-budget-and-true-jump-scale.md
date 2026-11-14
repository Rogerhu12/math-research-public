# R217 — 原真实 jump 的固定精度收益上限与双尾预算主阶

日期：2026-11-12。**状态：下面的真实 jump 总量、固定精度累计上限、低 torsion 总成本及目标边界预算均已证明。它们定位了当前斜率路线必须控制的主项；没有证明原中央非零，也不否定其他固定精度非零方法。**

本文把 R215 的全深原行权与 R214、R216 的实际双分量目标放在同一份原源预算中。结论是：若仅累计固定模 $p^N$ 可见的 Smith 长度，并只使用有正分母成本或实际中央比较发生变化的素数，则其总修正最多为 $O(ND^4)$。原 R159 严格门需要改变 $D^4\log D$ 主项。因此固定第三、第四层本身不足以完成这条预算路线；必须接到随 $D$ 增长的精度或整个原像。

## 1. 固定原源与全部真实跳跃

始终取同一个原二维源
$$
 E_D=\mathbf Z[A,C]_{\le D},\qquad C=B-A,\qquad
 m_D=\binom{D+2}{2}.
 \tag{1}
$$
不加入自由的 $w$ 源列，不按齐次次数分别取前缀核。
原系数行为
$$
 \ell_k(P)=[w^k]P(A(w),C(w)).
$$
依次保留真正增加有理秩的阶数
$$
                  0=k_1<k_2<\cdots<k_{m_D}.                 \tag{2}
$$
原代数独立性保证恰有 $m_D$ 个跳跃，且 $k_i\ge i-1$。

R191 的实际第一带消失阶定理，配合在 $p=(8+o(1))D$ 处选择一个惰性素数，给同一原有理源的统一上界
$$
                         K_D:=k_{m_D}\le(1+o(1))D^2.         \tag{3}
$$
这里只用该素数证明有理 jet 矩阵的秩；(2)–(3) 随后是固定原函数本身的事实，不为每个素数另选一组 jump。

置
$$
                             S_D=\sum_i k_i.
$$
由 (2)–(3)，
$$
 \frac{m_D(m_D-1)}2\le S_D\le m_DK_D,\qquad
                              S_D=\Theta(D^4).              \tag{4}
$$
进一步，
$$
                \sum_i k_i\log k_i
                   =2(\log D)S_D+O(D^4).                   \tag{5}
$$
为核查小阶项，令 $0\log0=0$。在 $0\le t\le CD^2$ 上，
$t|\log(t/D^2)|=O(D^2)$；对 $m_D=O(D^2)$ 项相加便得到 (5)。
因此不能把固定一个 Taylor 行的收益再重复乘成全部源维数后，仍称它为一层真实收益。

## 2. 累计范数必须使用 jump 矩阵

对惰性 $p=4r-1\ge7$，使用 R215 已证明整的原全部行权
$$
 e_{p,j}=
 \begin{cases}
 0,&h=0,\\
 h+\lfloor(h-1)/(p-1)\rfloor,&h\ge1,
 \end{cases}
 \qquad h=\lfloor j/r\rfloor.
 \tag{6}
$$
取原整单项式基，以固定的 (2) 为行构造方阵
$$
 J_p^{\rm jump}
          =\bigl(p^{e_{p,k_i}}\ell_{k_i}\bigr)_{1\le i\le m_D}.
 \tag{7}
$$
其整 Smith 指数记为 $s_{p,1},\ldots,s_{p,m_D}$。
R198 的准确旗标恒等式给
$$
 \sum_i\log\|\varphi_D^{k_i}\|_p
  =\left(\sum_i e_{p,k_i}-\sum_i s_{p,i}\right)\log p.
 \tag{8}
$$
原饱和核和原源系数范数均保留。

对 $N\ge1$，定义实际可见截断长度
$$
 B_{p,N}
   =\sum_i\min(N,s_{p,i})
   =Nm_D-\mathcal L_N(J_p^{\rm jump}),
 \quad
 \mathcal L_N(J)=\sum_i(N-s_i)_+.
 \tag{9}
$$
准确有
$$
                         0\le B_{p,N}\le Nm_D.               \tag{10}
$$
它已经累计了同一原源的全部 $m_D$ 个真实跳跃，不能再乘一次 $m_D$，也不能把源核扩大的长度混进来。

完整连续矩阵中晚出现的冗余行可能缩小最大 minor 理想；因此不能直接拿那个矩阵的 Smith 总和替代 (8)。当要用 R214/R216 的连续有限像计算 (8) 时，最终仍须保留实际 jump 行及其旗标。

## 3. 素数支持与固定精度的准确上限

令
$$
                  \mathcal P_D=\{p\equiv3\pmod4:
                           7\le p\le4K_D-1,\ p\ne11\}.       \tag{11}
$$
排除的固定有限集只影响下文的次阶项。

这里有两个不同而合法的使用方式：

1. 对原正分母包络进行改进。若 $p>4K_D-1$，则所有 $e_{p,k_i}=0$；在一个上界中，可以丢掉这些位的非正实际范数贡献。
2. 比较原矩阵与已经实际构造的删中央项矩阵。在 $r>K_D$ 时，原轴差的形式阶至少 $r$，两份保留至 $K_D$ 的原矩阵准确相同。因此这种中央比较在 (11) 之外没有变化。对尚未构造合法整比较矩阵的小素数，并不据此假设它存在。

**固定精度命题。** 若所记收益仅为 (11) 中固定精度 $N$ 可见的长度 (9)，则
$$
 \boxed{\quad
 \sum_{p\in\mathcal P_D}B_{p,N}\log p
                    \le Nm_D\,\vartheta(4K_D)
                    =O(ND^4).
 \quad}                                                       \tag{12}
$$
这里 $\vartheta(x)=\sum_{p\le x}\log p=O(x)$，二项式估计已足够。
同样，对同一原源、同一固定 jump 行上两份实际整矩阵的有限像长度差，只要比较支持在 (11)，其绝对加权和也至多 $O(ND^4)$：每份长度都在 $[0,Nm_D]$ 中，因此每个差至多 $Nm_D$。

对 R209 的已付第一带中央比较，$\Delta\in p^2\operatorname{Mat}(O)$。在其合法范围中，可将每个素数的粗差界改进成 $(N-2)_+m_D$；若在所比较的同一 jump 目标上另有完整共同 Schur 结构，仍可使用其更小的实际余源维数。不能从含冗余行的连续矩阵无证搬入那个维数。两者不改变固定 $N$ 时 (12) 的主阶。

**不能扩大支持结论。** $e_{p,k_i}=0$ 不意味着 Smith 指数为零：原整数 minors 仍可能被任意大的素数整除。式 (12) 不控制这些大素数处的一切负范数收益，也不排除通过那部分原全局算术获得新非零。它只适用于上面明确列出的正分母改进或实际中央比较。

同样，(12) 只控制已经记账的截断长度，不能把未知的
$\sum_i(s_{p,i}-N)_+$ 称为零。若一份固定精度结构另外证明了整个未观测尾的整性或强制大赋值，那是新的完整像定理，须把该证明一起使用。

## 4. 为什么固定层没有改变 R159 的主项

R159 在原二维平面上的复侧估计为
$$
 \sum_i\log\|\varphi_D^{k_i}\|_\infty
 \le-2\sum_i k_i\log k_i+2(\log D)S_D+O(D^4).
$$
用 (5)，即
$$
 \sum_i\log\|\varphi_D^{k_i}\|_\infty
                  \le-2(\log D)S_D+O(D^4).                  \tag{13}
$$
原普通位的全部真实 jet 成本非正，固定坏位的累计为 $O(D^4)$。
所以严格预算门讨论的量确实是
$$
                             S_D\log D=\Theta(D^4\log D).
 \tag{14}
$$

原无条件权包络也能准确对照。由 (6)，在 $p\le4j-1$ 时一致有
$$
 e_{p,j}=\frac{4pj}{p^2-1}+O(1),
$$
且更大的 $p$ 上它为零。使用 R173 已采用的模四素数和估计，
$$
             \sum_{p\equiv3\ (4)}e_{p,j}\log p
                              =2j\log j+O(j).
 \tag{15}
$$
故全部 jump 的该包络累计为
$$
 \sum_i\sum_p e_{p,k_i}\log p
             =4(\log D)S_D+O(D^4).                          \tag{16}
$$
若只从 (16) 扣除固定 $N$ 的 (12)，仍不改变它的 $\log D$ 系数。
即使另有完整像结果已经消去了 (16) 的一部分主项，固定层的新增比较仍只有 $O(D^4)$，不能独自提供一个固定比例的 $D^4\log D$ 改善。

在 R159 的逐行记号中，严格门为 $a_I+2b_I<2$。
小素数 $p\le8D-1$ 的现有包络满足
$$
 \sum_{\substack{p\le8D-1\\p\equiv3\ (4)}}
       e_{p,k}\log p
                       \le2k\log D+O(k+D).
 \tag{17}
$$
这部分本身已达到 $a_I=2,b_I=0$ 的边界；不能把小素数段删去，再将大素数段的有限层计算冒称严格门。

从 (12)、(14) 得到的必要规模判断是：若完全依靠这种有限像长度来改变固定比例的主项，则所用精度至少要达到
$$
                             N(D)\not=o(\log D).              \tag{18}
$$
这只是必要量级，绝不是充分条件。仍需实际收益方向、同一个源与真实 jump 比较；$N\asymp\log D$ 自身不会保证任何非零。

## 5. 小素数低 torsion 可以支付，但不能免费置零

R216 对任意 $D$ 的原双分量目标保留了低行
$0,\ldots,2D$。在原整分解
$K_D\oplus A^2E_{D-2}$ 上，准确矩阵为
$$
                         \begin{pmatrix}D_{\rm low}&F\\0&G\end{pmatrix},
 \qquad
 D_{\rm low}=\operatorname{diag}(p^{e_{p,0}},\ldots,p^{e_{p,2D}})
 \tag{19}
$$
（单位对角因子可先除去）。模 $p^N$ 商掉原 $K_D$ 像后，低行留下
$$
                  \bigoplus_{j=0}^{2D}
                      \mathbf Z_p/p^{\min(N,e_{p,j})}.
$$
记其准确环境长度
$$
                 \tau_{p,N}(D)=\sum_{j=0}^{2D}\min(N,e_{p,j}).
 \tag{20}
$$
低列与高尾的联合像仍须在这个目标中计算，不能只取 $G$。

由 (15) 对 $0\le j\le2D$ 求和，
$$
 \sum_p\left(\sum_{j=0}^{2D}e_{p,j}\right)\log p
                         =4D^2\log D+O(D^2).                \tag{21}
$$
另一方面，(20) 在 $p>8D-1$ 时准确为零，故
$$
 \sum_p\tau_{p,N}(D)\log p
                =O\!\left(D^2\min(N,\log D)\right).
 \tag{22}
$$
因此低 torsion 自身不是 $D^4\log D$ 主项的障碍。

若只把各可能次数 $d=D,D-2,\ldots$ 的这些环境长度相加，其总量至多
$$
                  O\!\left(D^3\min(N,\log D)\right).         \tag{23}
$$
但 (23) 只是所有低 torsion 的可支付总上界，**不是已经得到的小素数迭代 Schur 定理**。在小素数处，R214 的消低源截面可能非整；下一次乘 $M(C)^2$ 时，低块 $F$ 向高尾的卷积仍在。必须在同一个 torsion 目标中保留这些耦合，才能把形式递归变成真实有限像递归。

若已经观测全部原源的有理秩，则有一个无需非整消元的准确 determinant 事实。低 $2D+1$ 行都是实际 jump；对 (19) 的每个非零满列 minor，原 $K_D$ 列迫使选取全部低行。因而
$$
 \sum s_i(J^{\rm jump})
      =\sum_{j=0}^{2D}e_{p,j}
                       +\sum s_i(G^{\rm tail\ jump}).
 \tag{24}
$$
这里 $G$ 仍只取对应的真实剩余 jump 行。式 (24) 不表示有限精度低 torsion 消失，也没有计算未知的高尾 determinant；它只准确保留原源范数下的累计值。

## 6. 两条目标边界的损失与新增高尾列

在 R214 的单位截面范围 $p>8D-1$ 中，其实际递推为
$$
 \mathcal L_N(S_{D-2,k-2})-c_{D,k}-2N
 \le\mathcal L_N(H_{D,k})
 \le\mathcal L_N(S_{D-2,k-2}),
$$
再加入原 $2D-3$ 条高尾列 $G_{D,k}$。这里的两个 $G$ 记号按 R214 的原文含义使用：$H$ 是旧余块传递，新增块为实际核列的高尾，不能混同为自由源方向。

单就目标移位 $m\mapsto m+2$ 而言，R215 的全深权给准确对角损失和
$$
 \begin{aligned}
 c^{\,e}_{D,k}
 &=\sum_{m=2D-3}^{k-3}(e_{p,m+2}-e_{p,m})\\
 &=e_{p,k-2}+e_{p,k-1}
                -e_{p,2D-3}-e_{p,2D-2}.
 \end{aligned}                                               \tag{25}
$$
在 R214 的大素数范围，低端两项为零，且所有实际 jump 本来就在第一带内：由 (3)，$K_D\ll D^2$，而 $p>8D-1$ 给
$R_p=(p^2-1)/4>(16+o(1))D^2$。因此该范围的 (25) 退化为原来的第一带计数，全深换元并没有凭此扩大单位源截面的适用素数集合。

在有正分母成本的支持 $p\le4k-1$ 上，
$$
                  \sum_p c^{\,e}_{D,k}\log p
                                    =O(k\log k).             \tag{26}
$$
这是由 (15) 或其上界直接得到。投影丢掉两条目标行的 $2N$ 预算，在这个明确有限的素数支持上是 $O(Nk)$。
即便形式上最多走 $D/2$ 次，取 $k=O(D^2)$，这两类总量也只有
$$
                        O(D^3\log D+ND^3).                   \tag{27}
$$
(27) 没有把未证明的小素数源截面视为整；它只表明这些已经明确的目标边界成本不处在所需主阶。

真正尚未控制的是新增实际高尾列与旧像的重叠。它们单步能增加的长度是
$$
 \operatorname{length}
 \frac{\operatorname{im}H+\operatorname{im}G_{D,k}+p^N O^t}
      {\operatorname{im}H+p^N O^t},
 \quad 0\le\text{该长度}\le N(2D-3).
 \tag{28}
$$
不能把上界的符号解释成已经取得的收益。全源次数减少过程中，这些列总数为 $O(D^2)$；在 $p\le O(D^2)$ 的支持上，其固定精度加权总预算正是
$O(ND^4)$。这与 (12) 一致，没有多算一份来源相同的有限像长度。

## 7. 后续需要支付的具体对象

现有坐标运输、低 torsion 以及两条目标边界都已明确，且其可支付总量低于关键主阶。R215 的有限积分额外成本也没有自动变成原 Smith 收益；行权与全局微分标量的区别仍保留。

继续这条严格斜率路线，需要以下两类输入之一：

- 在同一原源和同一真实 jump 旗标上，控制随 $D$ 至少达到对数量级的精度，并证明原双高尾的相对像确有正确方向和足够累计长度。
- 给整个原像或完整 determinant 的直接定理，使未观测的所有 Smith 尾同时受到约束。

固定 $a_3$ 门或其他有限层仍可能是发现这种结构的入口；本文只说明其固定层长度不能单独充当所需主项。另一方面，某个固定精度非零证书若能直接对无穷素数成立，依然可以通过原有限性判据结束课题，完全不必走本篇的全素数范数路线。

依赖：[R159](R159-degree-sensitive-direct-slope-boundary.md)、
[R173](R173-full-depth-cm-carry-envelope-and-true-jets.md)、
[R191](R191-first-band-source-divisibility-and-global-multiplicity.md)、
[R198](R198-joint-image-saturation-and-complete-prefix-smith.md)、
[R209](R209-coherent-source-reduction-and-mixed-euler-schur-image.md)、
[R214](R214-quadratic-pair-tail-recursion-and-deleted-c-image.md)、
[R215](R215-full-depth-faber-transport-and-first-cross-band-carry.md)、
[R216](R216-all-degree-nonunit-low-kernel-and-true-finite-quotient.md)。
