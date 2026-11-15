# R787：真实精度增量的完整核格与来源契约

日期：2026-11-15。状态：**完整纸面证明与条件式消费契约；本稿没有消费更深的原 current，没有新增格、LLL 或候选算术。**

本文接
[已成42维基到56维基的完整增广](R787-original-incremental-three-probe-reconstruction-method.md)
及[原双探针规范](R787-original-projective-two-probe-reconstruction-method.md)。
这里改变的是同一组原探针的实际已发布精度。
新增探针的另一操作在第7节单独处理。
原 $L$、整阶、归一自由列1186、原 $Z'$、截面次序及 $82^{10}$ 尺度保持。

## 1. 实际已有来源与尚未满足的输入

原完整430位来源为 run43708449812，source
ac5998f333ab49c4747874e2e44b7ca4ccfa3acf；
原 mathematical configuration SHA256 为
71ea66416a42e024de61cf5927bc493fbc8422dc1b5970d75c51bd788d88529d。
其规范模数是
$$
\ell=1000000753,\qquad M=\ell^{430}.
$$

已经实际保存的完整行基有：

| 原格 | 实际来源 | 完整行与完整基见证 |
|---|---|---|
| $H_2$，42行 | run43748801736；source e2ac3449ac480c6f00bce197c0bd5202f8b1fda4 | 原 LLL 阶段 SHA256 3b8fbe90d539bb01609391a3ce7843e2ca75896bb2de3322840b4aef2ce452ef；其 all_42_reduced_rows 保全部42行 |
| $H_3$，56行 | run43754407301；source 1827d794565f94455e4f251f20d1979b55fee783 | 原 raw56 阶段 SHA256 bfe1b7e82811779e1c1969f40cfc1e292c27d6685393860ed560268f51dd526a；其 all_56_reduced_rows 保全部56行 |
| $H_2$ 的整幺模见证 | 同一已完成56维来源 | previous-basis-and-third-probe 阶段 SHA256 e8b173eb8fa265013e9966ffba4bdd5f75f6b63e19236dd4384ff84f3454ca56，保原42基相对 canonical graph 基的整变换及行列式 $\pm1$ |
| $H_3$ 的整幺模见证 | 同一已完成56维来源 | 完整 LLL/witness 阶段 SHA256 6cafcdaa430b9c5d01b233330414c30c398ee5e52fc489644085f69f5e6b6c25，保新56基相对三探针 canonical graph 基的整变换及行列式 $\pm1$ |

实际旧探针分别是 $(C_0,C_1)$ 和 $(C_0,C_1,A_0)$。
完整基见证已经属于已完成来源；后继直接核其原文件身份并消费，
不重复旧42/56维 LLL，也不把仅若干候选分母当作完整基。

新的精度输入必须是**真正完成并已发布**的原归一 current。
设其位数为
$$
n'=430+d,\qquad d\ge1,\qquad q=\ell^d,\qquad M'=Mq.
\tag{1}
$$
本稿不给它虚构 run、artifact、文件 SHA 或 $d$。
来源、归一化和精度相容的实际检查列在第8节；
在这些输入到达以前，不激活本接口。

本文得到的是新同余条件的全部解格。
它在旧格中有有限指数；“完整”指没有丢失同余解，
不包含通常无挠商意义的整数饱和声明。

## 2. 原整阶、行约定与完整格

固定
$$
\mathcal O=\mathbf Z[B_{\rm fld},s],\qquad s^2=-3,
$$
其中 $B_{\rm fld}=\lambda b$ 满足同一个原首一7次多项式。
使用原14维整基
$$
\omega=(1,B_{\rm fld},\ldots,B_{\rm fld}^6,
s,sB_{\rm fld},\ldots,sB_{\rm fld}^6).
$$
记 $r=14$。所有行向量均为此基下的整数坐标。
原乘法矩阵按
$$
\operatorname{coeff}(u x)=\operatorname{coeff}(u)\,R_x
\tag{2}
$$
定义，故 $R_x$ 右乘整数行。

给定 $k$ 个原坐标探针 $x_1,\ldots,x_k\in\mathcal O/M\mathcal O$，
定义
$$
\Lambda_k(M;x)=
\left\{(D,N_1,\ldots,N_k)\in\mathcal O^{k+1}:
N_i\equiv D x_i\pmod{M\mathcal O}\quad(1\le i\le k)\right\}.
\tag{3}
$$
它是秩 $n=r(k+1)$ 的整数格。
令 $m=rk$。原 canonical graph 基为
$$
G_k(M;x)=
\begin{pmatrix}
I_r&R_{x_1}&\cdots&R_{x_k}\\
0&MI_r&&0\\
\vdots&&\ddots&\\
0&0&&MI_r
\end{pmatrix},
\tag{4}
$$
其中每个乘法矩阵可用同一原模类的任一整数代表。
于是
$$
[\mathbf Z^n:\Lambda_k(M;x)]=M^m.
\tag{5}
$$

令 $H\in M_n(\mathbf Z)$ 的各行是已认证的 (3) 的完整整数基，
不要求这些行仍为某种 canonical 或 Hermite 顺序。
本题可取上述实际 $H_2$ 或 $H_3$。

新的已发布 current 给同标签坐标
$x'_i\in\mathcal O/M'\mathcal O$，并须实际满足
$$
x'_i\bmod M=x_i.
\tag{6}
$$
这是本篇全部精度增量公式的相容前提。
不重新选择旧探针标签，不更换 $\lambda$ 或 $s$，不把失败残差当成新探针。

## 3. 下一精度的残差映射是满射

对 $v=(D,N_1,\ldots,N_k)\in\Lambda_k(M;x)$，定义
$$
\Psi(v)=
\left(\frac{N_i-Dx'_i}{M}\bmod q\mathcal O\right)_{i=1}^k
\in(\mathcal O/q\mathcal O)^k.
\tag{7}
$$
由 (3)、(6)，分子在原14个整坐标中均可被 $M$ 整除。

这里 $x'_i$ 可以取任何整数代表。
将它改成 $x'_i+M' y$，(7) 只改变 $-qDy$，
故 $\Psi$ 不依赖代表。它是整数模同态。

**命题1。** 有短正合列
$$
0\longrightarrow\Lambda_k(M';x')
\longrightarrow\Lambda_k(M;x)
\xrightarrow{\ \Psi\ }(\mathcal O/q\mathcal O)^k
\longrightarrow0.
\tag{8}
$$

**证明。**
(7) 为零恰表示每个 $N_i-Dx'_i$ 可被 $Mq=M'$ 整除，
因此其核恰为左侧的新精度格。

对任意目标 $k$ 组14维剩余类，取整数代表 $a_i\in\mathcal O$，
则
$$
v=(0,Ma_1,\ldots,Ma_k)
$$
属于旧格，且 $\Psi(v)=(a_1,\ldots,a_k)\bmod q$。
所以映射满射。证毕。

由于 $\mathcal O$ 是秩14的自由整数模，
$$
[\Lambda_k(M;x):\Lambda_k(M';x')]=q^{14k}
=\ell^{14kd}.
\tag{9}
$$
证明没有要求任一探针或 $D$ 是单位，
没有要求 $\mathcal O/\ell\mathcal O$ 是域，
也没有使用14个分支根或其高精度提升。

特别地，本题两种完整增量的秩与指数为：

| 已成完整基 | 新格秩 | 残差靶秩 | 在旧格中的指数 |
|---|---:|---:|---:|
| $H_2$ | 42 | 28 | $\ell^{28d}$ |
| $H_3$ | 56 | 42 | $\ell^{42d}$ |

这个指数是同余格的准确整数指数。
它不是未知代数分母的高度上界或 LLL 成功保证。

## 4. 在旧基坐标中构造实际 unit minor

把第 $j$ 个旧基行写成
$$
H_j=(D_j,N_{j,1},\ldots,N_{j,k}).
$$
以 (7) 的行坐标组成
$$
E\in M_{n,m}(\mathbf Z/q\mathbf Z),\qquad
E_{j,*}=\Psi(H_j).
\tag{10}
$$
任意旧格元素唯一写成 $aH$，$a\in\mathbf Z^n$，
其新精度残差恰为 $aE$。

因为 $H$ 是完整基，命题1说明 $E$ 所定义的行映射满射。
特别地 $E\bmod\ell$ 的行秩为 $m$。
因此可以按固定顺序实际选出 $m$ 个行下标 $P$，
使
$$
U=E[P,*]\in M_m(\mathbf Z/q\mathbf Z),\qquad
\det(U\bmod\ell)\ne0.
\tag{11}
$$
这里取的是全部 $m$ 个靶列，只选择源行。
可对 $E^{\mathsf T}\bmod\ell$ 做准确模消元取首个主元列集，
并保存原行次序、真实模 $\ell$ 行列式和完整 (10)。

由于 $\mathbf Z/q\mathbf Z$ 是局部环，(11) 保证 $U$ 可逆。
实际消费者必须保存并验证
$$
UU^{-1}=U^{-1}U=I_m\pmod q.
\tag{12}
$$
不以仅记录“预期满秩”代替实际 minor 或逆的验证。

若 $d>1$，可先求这个至多42阶矩阵的模 $\ell$ 逆，
再用
$$
V_{\rm new}=V(2I-UV)\pmod{\ell^{\min(2e,d)}}
\tag{13}
$$
把已成立模 $\ell^e$ 的逆倍增到所需精度。
恒等式
$U V_{\rm new}=I-(UV-I)^2$
证明每一步准确。
这是一个新的小残差矩阵逆，不是原归一 Dixon 的重算，
也不是14个1186阶 Schur 逆。

在已验证所有前提时，找不到 (11) 会与命题1矛盾。
这种情况应定位来源、坐标或实现错误；
不能被解释为原函数不存在或新格的理论秩变小。

## 5. 显式完整核基、行列式与来源等式

令 $F$ 为 $P$ 的补集，按原下标升序排列，则 $|F|=r=14$。
定义
$$
W=-E[F,*]\,U^{-1}\pmod q
\tag{14}
$$
并选其标准整数代表 $0,\ldots,q-1$。

令 $\Pi$ 的各行依次为
$$
e_{F_1},\ldots,e_{F_r},e_{P_1},\ldots,e_{P_m};
$$
因此 $\Pi E$ 的上块是 $E[F,*]$，下块是 $U$。
置
$$
V=
\begin{pmatrix}
I_r&W\\
0&qI_m
\end{pmatrix},\qquad
K=V\Pi,\qquad H'=KH.
\tag{15}
$$

**命题2。** $K$ 的行是整数同态
$a\mapsto aE\bmod q$
的完整核基；$H'$ 的行是 $\Lambda_k(M';x')$ 的完整整数基。

**证明。**
先按 $(F,P)$ 重排系数。
若 $(u,v)\in\mathbf Z^r\times\mathbf Z^m$ 在核中，则
$$
uE[F,*]+vU=0\pmod q.
$$
乘 (12) 得
$$
v\equiv uW\pmod q,
$$
所以存在唯一 $b\in\mathbf Z^m$ 使
$$
(u,v)=(u,b)V.
\tag{16}
$$
反之，每个右侧由 (14) 都在核中。
故 $V$ 给重排坐标中的完整核，而右乘 $\Pi$ 恢复原系数次序。
再由 $a\mapsto aH$ 是整数模同构，得到关于 $H'$ 的结论。证毕。

公式同时给
$$
|\det K|=q^m,\qquad
|\det H'|=q^m|\det H|=(Mq)^m=(M')^{14k}.
\tag{17}
$$
这与 (9) 一致。
$W$ 的其他整数提升只相差 $q$ 的整倍数，
对应向上块加下块的整数行组合，故完整格不变。

实际新证书保留：
完整旧 $H$ 的原 SHA、(10)–(12)、$F/P$ 顺序、$W$、$K$、$H'$，
准确验证
$$
KE=0\pmod q,\qquad H'=KH,
\qquad
N'_i\equiv D'x'_i\pmod{M'}
\tag{18}
$$
对所有新行成立。
完整性来自命题2及旧完整基见证。
不必重求旧 LLL、旧整幺模见证或巨大格行列式，
也不凭“有 $n$ 个合格向量”猜测它们生成全部新格。

后继若需要短候选，可对真正不同的 $H'$ 执行一次新的 LLL，
并保存全部新约化行与整幺模变换。
它消费旧基作为准确预条件输入；
没有重复运行旧精度下的 LLL。

## 6. 最小残差实现不需要原大方程

(10) 可直接以旧完整行和新 probe 的真实14坐标求得，
不需要任何原 $A$ 方块逆、Schur 逆、Fourier 行或 Laurent 尾。

对每个旧行和每个 probe，只计算原整阶乘积模 $M'$：
$$
r_{j,i}=(N_{j,i}-D_jx'_i)\bmod M',
\qquad 0\le(r_{j,i})_a<M'.
$$
逐坐标确认 $M\mid(r_{j,i})_a$ 后取
$$
E_{j,i}=r_{j,i}/M\in\{0,\ldots,q-1\}^{14}.
\tag{19}
$$
这是 (7) 的标准代表，保其正残差符号。
原 $B_{\rm fld},s$ 的首一商环乘法直接适用模 $M'$；
不调用分支评价，不求 $\ell$ 进根。

总共只需 $nk$ 个这样的14维乘积：
$k=2$ 时为84个，$k=3$ 时为168个。
这两个数是本公式的循环长度，不是声称已经执行的运行数据。
残差阶段按旧行原序原子保存，后续继续读取已完成行。
完成 $E$ 后的小 unit minor、逆、核基和新格各有独立完成阶段，
同一阶段不重复计算。

本步骤只构造新精度的完整探针格。
要验证一个后继函数候选，仍须消费原 R787/R781/R786 的准确来源闭包，
保原129阶、280个有理坐标、非零 $B$ 和自由模式。
格的完整性不能代替这个特征零成功出口。

## 7. 提高精度与增加探针的兼容性

精度增量保持维数 $14(k+1)$；
新增一条探针使维数再增加14。
两者的来源和新算术分别记录。

设 $y'\in\mathcal O/M'\mathcal O$ 是一个真正指定的新 probe，
$y=y'\bmod M$。
对任何精度 $L$ 和已有完整基 $H_k(L)$，
上一增广证明给
$$
\operatorname{Aug}_y(H_k(L))=
\begin{pmatrix}
H_k(L)&C\\
0&LI_{14}
\end{pmatrix},
\tag{20}
$$
其中第 $j$ 行的最后一块为 $D_jy\bmod L$ 的任一整数提升。
其行空间恰为 $\Lambda_{k+1}(L;x,y)$。

因此以下两条路径得到同一个完整目标格：

1. 在模 $M$ 增加 $y$，然后对全部 $k+1$ 条固定标签按 (7)–(18) 提高到 $M'$；
2. 先把原 $k$ 条标签提高到 $M'$，再按 (20) 增加 $y'$。

两条路径都得到 $\Lambda_{k+1}(M';x',y')$；
它们的具体基和 LLL 输出无需逐行相等。
行列式因子也相容：
$$
M^{14}\,q^{14(k+1)}
=q^{14k}(M')^{14}.
\tag{21}
$$

若旧56维基已经完成，第一条路径直接消费它，
不再重新生成或约化旧增广格。
本题旧第三 probe 已实际选定为原 $A_0$，
后继精度沿用这个原标签。

一般地，在更深 current 上重新运行“第一条非零且不同的 $A_i$”规则，
可能选择另一个下标：
旧模数下为零或重合的更早坐标可能在新精度下分开。
这种标签改变不能冒充同一旧格的精度增量。
必须保持旧标签，或者显式用 (20) 处理新标签和实际来源。

(8) 与 (20) 对重复或代数相关 probe 仍成立，
因为每个 probe 有自己的分子坐标块。
因而它们的指数与满射性不证明这些 probe 对未知分母提供独立的高度信息。
不从“不同下标”“新增14维”或“指数增长”推出恢复保证。

## 8. 未来 current 的最小真实来源契约

后继执行前须同时具备并核实以下来源；这里没有新 active 请求。

**旧完整格。**
读取实际旧42或56的全部行、对应原 probe 坐标、
原模数 $M$、旧 configuration 和已经完成的整幺模见证。
按不可变 manifest 核 file/bytes/SHA，原 stage 保原 tag。
若选择42基，其完整基见证可直接消费已成56来源里的旧基证书；
若选择56基，消费其 raw56 与完整 witness 两阶段。

**更深原 current。**
读取实际已结束或已发布且完整的阶段，
核其真实 run/source/artifact/manifest、core 和原 configuration。
固定的数学 core 仍须是原
93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04，
原 configuration 仍为第1节的71ea…；
新提交号可以不同，不能用提交号比较代替数学身份比较。
核 prime、digits、modulus、chart_sha256、
full_original_modular_relations_verified 及完整 A/C 形状。
新位数实际满足 $n'>430$、模数等于 $\ell^{n'}$；
原 chosen_free_column 的 $C$ 仍为1，其他自由列仍为0。

原 chart、整阶、$\lambda$、$s$、1234个基的顺序和尺度逐项一致。
来源可为原预算结束时保存的完整 current；
整个工作流不必已经恢复特征零函数。
但正在运行且尚未发布的目录、缺失阶段或推测的位数不属于输入。

**实际兼容关系。**
从新 current 读取同标签 probe，
与旧完整格里已经绑定的原 probe 逐14坐标核 (6)。
数学上构造增量格只需要这些指定坐标的兼容；
若额外核整个 A/C 降模，则明确记录实际核过的范围。
原中间 lift 可以已按合法断点政策退役；
不要求恢复全部中间 raw，
也不因此略过当前两端的直接兼容检查。
真正被读取的旧/new current 或其已认证选取阶段的原 SHA 都保留。

这套最小格消费者只需要原整阶描述、完整旧基和新 probe，
不必重新传输或生成全部 Fourier/Laurent 数据。
若要接原函数准确出口，
再消费其仍活跃的完整原来源闭包；
不得因为本节省了某组输入而把准确验证所需的旧数据重算。

新 tag 至少绑定
old_basis_source、new_current_source、old_digits、new_digits、
实际 $d$、同一 $\ell$、原 field/labels、(19) 的坐标约定、
unit-minor 选取顺序及完整核构造策略。
旧 stage 的 tag 不改写为新 tag。
预算或有限候选数量是运行控制，不能改变已成格的数学身份。

阶段意义严格区分：

- source compatibility 完成：只证明原输入与固定标签可衔接；
- incremental kernel/basis 完成：只证明完整新精度格已实际构造；
- 新 LLL 完成：只给有限候选；
- 原129阶准确出口完成：才可恢复原函数。

所有阶段另记 new_normalized_Dixon_digits_computed=0；
$new_digits$ 是实际 producer 已完成并提供的精度，
不是本消费者计算的新归一位数。

## 9. 精度改变时，旧拒绝的精确复用边界

增加精度后，即使同一个正号14维 $D$ 再次出现，
$$
\operatorname{center}_{M'}(Dx'_i)
$$
一般也不同于原
$\operatorname{center}_M(Dx_i)$。
因此旧精度下仅按 $D$ 保存的准确拒绝，
不能不加检查地用于新构造出的 $A',C'$。

有一个无需重建旧候选的充分判据，但它另需比 (6) 更强的实际来源检查：
必须核新原归一 current 的**全部1214个 $C$ 坐标、各14个整分量**降模 $M$ 后
与原430 current 的全部相应 $C$ 坐标一致，
或消费已准确认证、覆盖这全部坐标的等价来源证书。
仅核 $k$ 个 probe 的 (6) 不足以使用本节的旧拒绝复用。
在这项完整 $C$ 相容检查之后，
再设新精度实际构造出的非自由 $C'$ 的每个整坐标都在旧中心区间
$$
-\frac{M-1}{2}\ \le c\le\ \frac{M-1}{2}.
\tag{22}
$$
因为上述完整 $C$ 相容检查保每一项模 $M$ 的类不变，旧中心代表的唯一性强制这些坐标
与旧 $C'$ 逐项完全相同。
自由列始终准确为同一个未约化 $D$，其他自由列为0；
所以整个未除 content 的 $C'$ 相等。
(22) 只是复用来源的充分判据，不是新候选的接受高度界。

如果原
[固定C障碍](R787-original-fixed-C-next-digit-obstruction-and-shared-source-contract.md)
随后确有该 $D$ 的真实非零 $\Omega$，
则这个源绑定的严格排除适用于所有分子 $A$，
故可直接拒绝相同的新 $C'$。
这里必须消费实际完成的非零残差，
不能预设正在运行的 $\Omega$ 结果。

若只有旧 A/B 的准确非零关系，
还须先实际核新原归一 current 的**全部1234个 $A$ 坐标、各14个整分量**
降模 $M$ 后与原430的全部对应 $A$ 坐标相同，
或消费覆盖这全部坐标的准确相容证书；
随后对新 $A'$ 的全部整坐标也核旧中心区间，
再结合上述 $C'$ 相等、同一原 $Z'$ 和共同 content 规则，
才能复用同一个旧准确候选拒绝。
仅某一 probe 的中心代表相等不够。
若不满足这些充分条件，仍可通过其他真实准确等同性证书复用；
没有这种证书时，新精度构造出的候选应按新身份验证。

反向地，旧 $\Omega=0$ 只说明其当时的必要条件通过，
没有成功结论可供更深精度继承。
格精度增加、第三 probe 增加和固定 $C$ 的排除各自提供不同的实际信息，
其来源和证书始终分开。

## 10. 发布与结论边界

本文证明了旧完整基到新精度完整格的确定构造，
包括满射、实际 unit minor 的存在、准确核基与指数，
并证明它与新增 probe 的操作相容。

没有更深原 current 的真实来源就不执行；
没有实际新格就不报告新 determinant 或候选；
没有原129阶准确出口就不报告原函数、CM点、极理想、eta或高度。

全部新增算术只在公开仓库 Actions。
Git 仅保存源码、参数、纸面证明及简明 run/SHA 登记；
机器回执、完整格、current、残差、逆和候选载荷只在一日 active artifact/carrier 中续传。
