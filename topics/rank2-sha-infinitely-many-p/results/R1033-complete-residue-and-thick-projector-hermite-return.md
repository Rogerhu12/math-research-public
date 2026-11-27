# R1033 — 原完整剩余核与厚幂等投影的直接 Hermite 返回

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

**已证明的范围：** 下述两个算法返回原 $R=k[t]$ 上的完整 Hermite
理想基；每个原坐标、幂零方向、完整局部长度和原常数嵌入都保留。
它们接入 R1008 的同一生产程序时，只替换原 primary decomposition
中的两个理想构造器。本文登记的是证明、源码与静态检查，
没有数学执行，也没有四交、Norm 或 shadow 的新 PASS。

唯一 v9 仍运行；本文的新文件及未激活请求不会触发或取消它。
必须等其真正终态并消费完整回执，再决定是否启动这个有实质改变的后继。

## 1. 原模块与准确问题

保持 R925/R931 的同一个已认证正规仿射环
$A=R^{306}$、完整乘法、原单位和有序整基。每个已给有效理想
$I\subset A$ 的完整上三角行 Hermite 基为 $H_I$。
它不是分式域的某个子空间，而是已经支付双向多项式模包含的整格。

一个原闭点分量给出准确剩余映射
$$
 \operatorname{ev}:R^n\longrightarrow k_\pi^d,\qquad
 v\longmapsto \overline v\,C,\quad
 k_\pi=R/(\pi),\quad n=306,
 \tag{1}
$$
其中 $C$ 的全部 $n$ 行均来自原剩余域的实际坐标，秩恰为 $d$。
$k_\pi^d$ 中的乘法和原常数嵌入仍由原构造器给出。
需要返回的是整个 $\ker(\operatorname{ev})$。

另一处给一个完整 $\pi$-primary 理想 $I$ 和已逐式提升的
$e\in A/I$，满足 $e^2=e$。需要返回的是
$$
 J=I+(1-e)A.
 \tag{2}
$$
其商是完整厚局部因子。不能只用其 reduced quotient、
猜测的重数，或一个截断的幂零邻域代替它。

## 2. 原剩余核的直接基

从 $C$ 的最后一行往前，贪心选取线性独立的行，
得到递增指标 $S=\{s_1,\ldots,s_d\}$。
矩阵 $C_S$ 可逆，完整等式
$$
 B=C\,C_S^{-1},\qquad BC_S=C
 \tag{3}
$$
给每行对这些原行的全部坐标。右端优先的选择保证：
若 $i\notin S$ 且 $s_j<i$，则 $B_{ij}=0$。
确实，在扫描到 $i$ 时，所有右边行的张成空间已经确定；
若 $C_i$ 不独立，它只能用右边已经选中的行表达。

用原固定 $k_\pi$ 模型把每个 $B_{ij}$ 唯一提升为次数
$<\deg\pi$ 的多项式 $\widetilde B_{ij}$。定义
$$
 H_i=
 \begin{cases}
  \pi e_i,&i\in S,\\
  e_i-\sum_j\widetilde B_{ij}e_{s_j},&i\notin S.
 \end{cases}
 \tag{4}
$$
这是上三角、对角首一的完整 Hermite 基：非主元列只有对角一，
主元列的其余项次数严格小于 $\deg\pi$。
每行实际代回(1)为零，且
$\det H=\pi^d$。

这里不只用一个秩或行列式推测等式。对任意 $v\in R^n$，
用(4)作完整多项式除法后，余式只支撑在 $S$，各系数次数
$<\deg\pi$。若 $\operatorname{ev}(v)=0$，余式的系数向量乘
$C_S$ 为零，故所有余式系数都为零。因此
$$
 \operatorname{row}_R H=\ker(\operatorname{ev}).
 \tag{5}
$$
这也给出任意核元素的真实整返回。

源码另外保留一组完整生成元：所有 $i\notin S$ 的(4)及
$\pi$ 乘全部原标准基。每个 $H_i$ 都是其中实际的一行；
反过来，每个生成元被 $H$ 完整除尽。
所以两个方向的多项式模包含均实际检查。
原闭点 registry 继续以整个 Hermite 矩阵而非仅哈希比较身份。

## 3. 在整个厚商中作后缀 Krylov 返回

写 $d_i=\deg(H_I)_{ii}$。全商 $A/I$ 的准确 $k$ 基是
$$
 t^a e_i,\qquad 0\le a<d_i.
 \tag{6}
$$
其维数 $L=\sum_i d_i=\deg\det H_I$；
(6)包含全部幂零部分，不只剩余域。
利用完整 Hermite 除法，展平和恢复(6)互为逆。
乘 $t$ 也先在原 $R^{306}$ 中进行，再模整个 $I$ 约化。

令 $M_e$ 是原完整乘 $e$ 的矩阵。
先计算所有 $306$ 个原坐标在
$$
 \mu_e:A/I\to A/I,\quad v\longmapsto ve
 \tag{7}
$$
下的实际像。现在从 $i=n-1$ 到 $0$，依次考虑
$\mu_e(t^a e_i)$，$a=0,1,\ldots$。把它们对已经保留的全部
像作精确 $k$ 线性消元。记录每个消元行对原 Krylov 向量的
完整表达，不丢掉任何商坐标。

在第一个相关处，得到
$$
 \mu_e(t^{m_i}e_i)
  =\sum_{j\ge i,\ 0\le a<m_j} c_{j,a}\,\mu_e(t^a e_j).
 \tag{8}
$$
其中 $j=i$ 项只含此前已加入的低幂。于是返回
$$
 H'_i=t^{m_i}e_i-
        \sum_{j\ge i,\ 0\le a<m_j}c_{j,a}t^a e_j.
 \tag{9}
$$
$m_i=0$ 完全允许，给一个单位主元。

终止和完整性由如下归纳保证。已处理的整个后缀像空间对乘 $t$
稳定；加入一个新坐标的各幂后，首个关系(8)使扩大后的空间仍然
对 $t$ 稳定。因而它张成该后缀的全部多项式像，且所保留向量
线性独立。每增加一个向量都增加全厚商中的维数，至多增加 $L$ 次。
处理全部原坐标后，得到的正是 $\operatorname{im}\mu_e$。

所以(9)的矩阵 $H'$ 是真正上三角 Hermite 矩阵：
同列 $j$ 的非对角次数 $<m_j$，对角首一；
其标准单项式全部独立并张成(7)的像。
特别
$$
 \deg\det H'=\sum_i m_i=\dim_k\operatorname{im}\mu_e.
 \tag{10}
$$
这没有使用半单性、无分歧性或任何预先指定的局部重数。

## 4. 对原整理想的两个实际返回

仅有(8)的向量空间解释还不作为程序接受条件。
源码还对原多项式矩阵执行下面的完整返回。

取原单位所给的完整恒等矩阵，令
$M_c=I_n-M_e$。已认证的原乘法线性性与原单位给
$M_c=M_{1-e}$。入口逐项核 $e^2-e\in I$。
首先把原全部生成元
$$
 \begin{pmatrix}H_I\\M_c\end{pmatrix}
 \tag{11}
$$
用整个 $H'$ 作多项式除法，要求每个坐标余式为零。
这准确证明 $I+(1-e)A\subset\operatorname{row}_R H'$。

反向则计算完整 $H'M_e$，用 $H_I$ 作真实整除，得到
$C_0\in M_n(R)$ 并逐坐标核
$$
 H'M_e=C_0H_I.
$$
最后完整检查
$$
 \boxed{\quad H'=C_0H_I+H'M_c.\quad}
 \tag{12}
$$
所以 $\operatorname{row}_R H'\subset I+(1-e)A$。
两者结合，返回的恰为原(2)；变换矩阵为
$(C_0\mid H')$，有完整哈希回执。
分式域解、局部化、清分母或只看泛型秩均没有出现。

算法在商维数大于源码的内存阈值4096时，直接调用已存在的
完整原行算法处理同一(11)，不删除任何行或降低数学范围。
该阈值只选择等价实现；实际 receipt 明示是否走这个回退。

## 5. 原生产程序的准确接线

新模块保留原
`original_ys_closed_point_tools.py`
完整 primary decomposition 的实际输入和后续所有检查；
只把原 maximal ideal 和 $I+(1-e)A$ 两个构造器分别换成§2和§3–4。
原源文件的 SHA256 固定为
`7428cadb6b2179aebd547c749ec11ae46305476947aa443f7266e64d03ccc7bb`。

以下对象和门全部保持：

- 原实际两图、有序306基、46971产品、常数域与其固定嵌入；
- 原完整 primary 理想、Frobenius、primitive idempotents 及全厚提升；
- 每个原剩余映射、整个最大理想、局部完整长度及真实交重数；
- 全幂等元正交且和为一，全部小长度/约化长度/完整长度返回；
- 同一七式、四个完整交、两图无穷边界、完整 Norm、18×9 shadow。

新外层生产器逐字钉住 R1008 的 v9 生产器，
并保其所有旧运行时验收。它只在本次离线进程中绑定新函数，
不修改旧文件、其它工作流或旧回执。
旧主程序返回全部成功后，新外层才允许自己的 COMPLETE 记录。

新的 host launcher 仍认证两个原 char0 PASS，使用原 Sage10.6
精确镜像、无网络数学容器、只读源码挂载、r29/q2453/batch64/minimal，
并记录全部52个实际源文件与两 README 的哈希。
旧49个源完整保留，另加本模块、外层生产器和新 launcher。
人工 API preflight 仍为 false，既不运行也不宣称该例 PASS。

源码：

- `scripts/original_projector_hermite.py`：19146 B，
  SHA256 `99e64fd3ae1c7b49882357b60ef39e6c3856fb66685275be344a2814a8bb084e`。
- `scripts/produce-original-projector-artinian-shadow.py`：6992 B，
  SHA256 `9229b6e47ce95eb9dd0833e37a761f33162e264b28c21a2d163c1c55d054d683`。
- `scripts/launch-original-projector-artinian-shadow.py`：10872 B，
  SHA256 `ca8b0f252494c2f2fad1a15235852e91050cbfe65fe60e33790e5aaf0e0b3490`。

上述源码只作文本、AST和哈希检查；没有在本地执行数学。
准备的 v10 请求为
`ci/original-projector-artinian-shadow-request.json`，
尚未接入触发路径，不能记为已经启动、通过或完成。

## 6. 当前实际回执与继续门

v9 的第七次只读 collector 为
run45952136806/job140350212654/source3bc9c96dfad511c56be4487c1340cfe68fc99a21。
它在06:29:11UTC得到原完整日志31514035 B，
SHA256 `eef3c1abad50318fb3e445e225e89071431b8c251eedb0f5f4e1ee397ae0ff59`。
末行06:25:55UTC位于原 cubic branching 负向、base-prime0、
actual maximal ideal1，Hermite138/306，剩余行列式次数1。
原 run/job/math step 仍为 in_progress，全部最终数学记录仍空。
这不是四交、全 Norm 或 shadow PASS。

后继必须首先消费同一 v9 的真实终态；
若需要启用本篇算法，再运行完整原对象并消费全验收，
不能把算法正确性或静态检查写成原 shadow 非零。
主目标的固定曲线、通常全群及无限多个不同素数条件仍未完成。
