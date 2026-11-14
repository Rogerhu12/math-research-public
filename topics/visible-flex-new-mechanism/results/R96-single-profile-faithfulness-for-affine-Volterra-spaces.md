# 将有限 universal Volterra 空间的分离搬到同一光滑三矩圆

日期：2026-11-14。完整纸面结果 R96。依赖 [R86](R86-left-moment-completion-preserves-right-Volterra-obstructions.md) 的左侧三矩补全及 [R91](R91-affine-character-dichotomy-for-positive-universal-P1.md) 的有限仿射算子空间；不执行新的 profile 评价或完整编译。

本稿补一个 R91 当时明确保留的界限。一般多 profile 评价不能直接当成固定 profile 的证书；但这里的有限 Laurent 仿射作用、统一次数和真正右因果结构，允许另作完整构造。结论仍有明确前提，且不会把一个正规形余项当作真实非成员。

## 1. 算子空间假设

设 $V$ 是一个有限维实向量空间，其元素是作用于一对实光滑紧支撑 profile $(f,g)$ 的有限个实输出函数。复模式的实部、虚部可分别看作输出分量。假设：

1. 每个算子都是输入 jet、坐标多项式、乘积和真实共同右 Volterra 原函数的有限多项式表达式。每个原函数节点的被积式有严格正的 profile 次数。没有左端总矩或某个固定外部点的额外评价节点。
2. 所有算子对 $(f,g)$ 统一齐次，次数为同一个正整数 $r$；当前 P1 应用为 $r=4$。
3. 正仿射 pullback

$$({\sf P}_{H,d}F)(f,g)(x)
=F(C_{H,d}f,C_{H,d}g)(Hx+d),\qquad
C_{H,d}f(x)=f((x-d)/H),\quad H>0,$$

保持 $V$，且在一个固定基中的作用矩阵是 $H$ 的有限 Laurent 多项式、$d$ 的有限多项式。

把所有右锚取在全部输入支撑右方。由于每个原函数节点有正 profile 次数，单个 packet 之外的右侧空区对积分贡献准确为零，所以改用更右的共同锚不改变表达式。这逐层归纳到全部嵌套原函数。

由同一个结构还得到**右因果性**：在查询点 $x$ 的输出只依赖输入在 $[x,\infty)$ 上的 jet。左方支撑改变不会影响该查询。微分、乘积和正次数右原函数均保持这个性质。

R90/R91 的

$$V=\mathcal R_*+\operatorname{span}\{b_{H,d}:H>0,d\in\mathbb R\}$$

满足这些假设：R56 的有限分子闭合没有引入左评价节点，全部 P1 项为四次齐次，R91 已证明有限 Laurent 仿射不变性。此处用的是完整原式，不是由有限采样猜测的算子空间。

## 2. 一组多输入评价先形成准确满秩矩阵

令 $m=\dim V>0$，取真实算子基 $F_1,\ldots,F_m$。

普通输入/输出评价分离 $V$：若一个元素在所有光滑紧支撑 profile、所有查询点与所有输出分量上都为零，它按真实函数定义就是零。因此存在 $m$ 个评价

$$e_j(F)=\operatorname{component}_j F(f_j,g_j)(x_j),\qquad 1\le j\le m,$$

使矩阵

$$M=(e_j(F_k))_{j,k=1}^m$$

可逆。这一步允许不同的 $(f_j,g_j)$，尚未把它们视为同一个 profile。

选一个紧区间 $I_j$，其内部同时含 $x_j$ 和 $f_j,g_j$ 的支撑。独立地给第 $j$ 行作正仿射变换 $a_j=(H_j,d_j)$，得到

$$\widetilde f_j=C_{H_j,d_j}f_j,\quad
\widetilde g_j=C_{H_j,d_j}g_j,\quad
\widetilde x_j=H_jx_j+d_j.$$

变换后的行恰为 $e_j({\sf P}_{H_j,d_j}F_k)$。其行列式是所有 $(H_j,d_j)$ 的有限 Laurent 多项式，且在全部 $(H_j,d_j)=(1,0)$ 时等于 $\det M\ne0$。

现在预先指定任意非空有界开区间 $J$。要求这些变换后的紧区间 $H_jI_j+d_j$ 全部位于 $J$ 内，且按 $j=1,\ldots,m$ 从左至右严格互不交。这些严格不等式给参数空间中的一个非空开集：将每个 $H_j$ 取充分小，再把各中心放进 $J$ 内的不同小区间即可。

一个非零 Laurent 多项式不可能在该非空开集恒零；乘以各 $H_j$ 的足够正幂即是普通多项式的同一事实。因此可以同时满足

$$H_1I_1+d_1<\cdots<H_mI_m+d_m\subset J$$

及

$$\boxed{\det\widetilde M\ne0,\qquad
\widetilde M_{jk}=F_k(\widetilde f_j,\widetilde g_j)(\widetilde x_j)
\text{ 的指定实分量}.}\tag{1}$$

这里没有分别变换几何后将不同右锚混在一起；(1) 是同一个 universal 算子空间的 pullback，单 packet 右侧为空使其与最终共同右锚准确相同。

## 3. 用右因果性合成一个 profile

给 packet 取实幅 $z_1,\ldots,z_m$，定义

$$f_z=\sum_{j=1}^m z_j\widetilde f_j,\qquad
g_z=\sum_{j=1}^m z_j\widetilde g_j.$$

在第 $j$ 个查询点 $\widetilde x_j$，所有编号小于 $j$ 的 packet 都位于其左方，故由右因果性不产生任何贡献。于是评价矩阵

$$E(z)_{jk}=\operatorname{component}_jF_k(f_z,g_z)(\widetilde x_j)$$

的第 $j$ 行仅依赖 $z_j,\ldots,z_m$，且为总次数 $r$ 的齐次多项式。

该行中 $z_j^r$ 的系数恰为第 $j$ 个 packet 单独输入时的行 $\widetilde M_{j\cdot}$：出现 $z_j^r$ 已用完所有 $r$ 个输入次数，所以没有其他 packet 的因子。

按 $z_1,z_2,\ldots,z_m$ 的词典序逐次取最高次数。在 $\det E(z)$ 中，变量 $z_1$ 只出现在第一行，其最高次数至多为 $r$；取 $z_1^r$ 后该行成为与剩余幅无关的隔离行。随后对第二行重复，再依次进行。由此

$$\boxed{[z_1^r\cdots z_m^r]\det E(z)
=\det\widetilde M\ne0,}\tag{2}$$

且这是上述词典序的首个可能全次数项。不存在由另一行补回更低 $z_j$ 次数的途径，因为右方行不依赖 $z_j$。

故 $\det E(z)$ 是一个非零实多项式。它不能在正正交体 $z_j>0$ 上恒零，所以可取有限的严格正实幅使其非零。合成得到一个光滑紧支撑 profile 对 $(f_*,g_*)$，支撑在 $J$ 内，满足

$$\boxed{E_*:V\longrightarrow\mathbb R^m,\qquad
F\longmapsto\big(\operatorname{component}_jF(f_*,g_*)(\widetilde x_j)\big)_j
\text{ 是单射}.}\tag{3}$$

这是一个真实同 profile 评价，不是多个测试结果被重新命名成一个 profile。幅度可能很大，packet 可能很窄；本命题不给统一导数盒或定量长度上界。

## 4. 准确补三矩、归一且保留全部分离行

将 (3) 的复 profile 记为 $q_*=f_*+ig_*$。在 $J$ 左方、所有支撑与查询点之前留三个互不交的紧子区间，仍放在某个指定更大开区间 $I$ 内。按 R86，取三个同形偶实 bump，其中心 $c_1,c_2,c_3$ 不同，二次矩列为

$$\left(a_0,a_0c_j,a_2+a_0c_j^2\right),\qquad a_0>0.$$

三列矩阵的行列式为 $a_0^3$ 乘非零 Vandermonde。用普通复平方系数解线性系统，并逐个取复平方根作为 bump 幅，得到左补丁使

$$\int q''^2=0,\qquad
\int xq''^2=0,\qquad
\int x^2q''^2+2\int q'^2=0.\tag{4}$$

所有补丁都严格位于每个查询点左方。因此由右因果性，矩阵 (3) 完全不变。$q$ 非零，因为原矩阵可逆。

写 $q=f+ig$，(4) 的第一式给

$$\int f''^2=\int g''^2>0,\qquad \int f''g''=0.$$

后两式同样给 R39 所需的另外两组等长/正交矩。故这是真正非退化的三矩圆平面，而不是一条实方向的复倍数。最后用一个共同正实常数将 $\int f''^2$ 归一为 1。在本课题的 $r=4$ 应用中，全部算子为四次齐次，所以每行都乘同一个非零四次因子，可逆性仍保留；一般统一次数 $r$ 时相应因子为同一个 $r$ 次幂。

由此，对任意具有足够小左补丁空间的开区间 $I$，可构造一个 $C^\infty$ 紧支撑、非退化且归一的合法三矩 profile 圆，使整个有限空间 $V$ 的同 profile 评价单射。若从一开始取 $J$ 为 $I$ 内较右的紧子区间，就自动留下该左侧空间。

## 5. R91 负分支的同 profile 推论

仍假设尚待确认的真实非成员

$$b\notin\mathcal R_*.$$

R91 给出真实实线性泛函 $\Lambda$，湮灭 $\mathcal R_*$，且

$$\Lambda(b_{H,d})=H^n>0.$$

取第 4 节的同 profile 单射 $E_*:V\to\mathbb R^m$。因维数相同，它可逆；将 $\Lambda\circ E_*^{-1}$ 写成行向量 $\lambda_*$。于是对所有 $F\in V$

$$\lambda_* E_*(F)=\Lambda(F).$$

尤其这是**同一个固定合法光滑三矩圆**上的真实查询泛函，满足

$$\lambda_*E_*(\mathcal R_*)=0,\qquad
\lambda_*E_*(b_{H,d})=H^n>0.\tag{5}$$

因此，对这个 profile 圆，任何有限个 reciprocal 状态、任意正 bulk 长度和任意允许的独立真实第三控制都不能支付完整 P1。这里控制系数即使在看到该 profile 后才选择，仍会被 (5) 湮灭。

这比 R91 单独给出的 universal 负结论多用了第 2–4 节的准确拼接论证。它仍不意味着所有 profile 圆都失败，也不排除别的机制或固定 $N$ 的 $P_0+NP_1$ 相消。共同物理区间仍须适用于实际候选；负结论只对该区间上确实定义的候选使用原式。

## 6. 无统一导数盒时的相对开稠密性

在一个固定有界开区间 $I$ 内，令 $\mathcal Q(I)$ 为所有光滑紧支撑、满足 (4) 且 $\int f''^2=1$ 的复 profile。允许各 profile 有自己的左零 collar；不要求整个类保持同一固定宽 collar。

固定上面构造的 $q_*$、查询点及输出分量。取足够大的有限 $K$，使 $V$ 的所有原式在固定区间上关于 $C^K$ 输入连续。因为表达式有限，原函数节点只作有限区间积分，这样的 $K$ 存在。

矩阵行列式非零显然给一个相对 $C^K$ 开集。为证稠密，取任意 $q_0\in\mathcal Q(I)$。在同一组查询上

$$\Delta(t)=\det E(q_0+tq_*)$$

是实参数 $t$ 的多项式，最高系数为 $t^{4m}\det E(q_*)\ne0$。故除有限个 $t$ 外均非零，并可取任意小的非零 $t$。

虽然 $q_0+tq_*$ 未必满足三矩，但因 $q_0,q_*$ 各自满足 (4)，其三个矩缺陷为 $O(t)$。在两者支撑以及全部查询左方取三个固定 bump；该位置在 $I$ 内存在，因为这些集合均紧含于 $I$。R86 的线性系统给平方幅 $O(t)$，实际复幅为 $O(\sqrt{|t|})$。因此对固定这些 bump，修正量在 $C^K$ 中趋零，且全部查询值保持不变。共同归一因子趋于 1，所以归一后的圆仍趋于 $q_0$，行列式仍非零。

于是整个 $V$ 的同 profile 满秩评价在 $\mathcal Q(I)$ 中相对开稠密。若 R91 处于负分支，(5) 对这个开稠密集合中的每个圆分别成立。没有给导数上界、振幅盒、固定左 collar 宽度或几何 reach 约束下的稠密性声明。

## 7. 当前状态

本稿的有限构造定理不依赖实际计算。后续 [R98](R98-weight-zero-separation-of-all-positive-state-P1.md) 已通过权零原式14/15非零子式支付实际 $b\notin\mathcal R_*$，且最高未付权为零，因此第5–6节推论在本题实际模型上成立；仍不外推所有特殊圆或固定有限N的完整第四消项。

本文未执行新的实际 profile/几何评价，没有给具体 packet 参数或新查询矩阵数值；有限构造存在性由非零多项式与右因果性证明。P0、完整第四 ruling、全部更高阶及主课题的闭面嵌入、厚度和宏观位移仍未完成。
