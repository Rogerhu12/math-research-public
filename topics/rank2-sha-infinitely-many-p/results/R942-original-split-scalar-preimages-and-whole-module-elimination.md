# R942 — 原分裂标量的全厚原像及不累计变换矩阵的完整行模消元

日期：2026-11-26；会话 Astra-rank2-Sha-7d29daa5-20261126。

**状态：下列完整行模、逐重因子原像和整像算法的等价性已证明。尚无这次公开运行、性能回执、完整 F 除子或 shadow PASS。**

本篇接 R925§24、R927§10、§12 的同一原 $Y$、两个正规化图表和原全144 mixed核，
只改变整多项式线性代数的实现。原常数域 $k=\mathbf F_{29^2}$、原 $\omega$、
306有序基、原函数、所有厚度、全源与两图返回均保持。

## 1. 全行模的逐操作证书

令 $R=k[t]$，$M\in R^{m\times n}$ 满列秩，$m\ge n$。
以下消元在整个行向量上执行；不以分式域核清分母替代 $R$ 模。

对当前第 $j$ 列，从尚未用作主元的行中选择非零元 $a$。
若另一行在该列的元为 $b$，且 $b=qa$，则作初等行运算
$r_b\leftarrow r_b-q r_a$。
若不能整除，取多项式 Bézout 恒等式

$$
sa+tb=g,\qquad a=gu,\quad b=gv,
$$

其中 $g$ 首一。将两整行同时替换为

$$
\begin{pmatrix}r_a'\\r_b'\end{pmatrix}
=\begin{pmatrix}s&t\\-v&u\end{pmatrix}
\begin{pmatrix}r_a\\r_b\end{pmatrix}.
\tag{1}
$$

该 $2\times2$ 变换的行列式严格等于 $su+tv=1$，新列元为 $(g,0)$。
因此它在 $R$ 上可逆，精确保留整个行模，且不需要保存历次变换矩阵的乘积。
交换行、非零域常数缩放和加另一行的多项式倍同样是可逆的。
逐列清除下方全部元素，将主元化为首一，再对上方元素作带余除法。
每个先前主元列在后续主元行中为零，故后续操作不会损坏先前列。
有限的列数和每列有限个 Bézout 步保证终止。

末端得到 $n\times n$ 的上三角行 Hermite 矩阵 $H$；额外的 $m-n$ 行为**恒零行**。
只能删除这些恒零行，不能根据分式域线性相关丢弃未归零的整行。
由逐步可逆性，$\operatorname{row}_R(H)=\operatorname{row}_R(M)$。
实现还把输入的每一行对 $H$ 作完整多项式带余除法，核余式全零；
这给另一方向的全源返回。

实际证书保存完整输入/输出哈希、每步操作类型和所有多项式参数的有序哈希、
每次 Bézout 行列式为1、每次缩放为域单位、删除的行全零和全源返回。
这些对象全部由已提交源码重算；不储存庞大的累计 $U$。
**这一步只适用于完整行模基；它没有生成任何核的原坐标投影。**

## 2. 同一个原分式的全部源整像

设 $D\in R^{n\times n}$ 非奇异，$W\in R^{r\times n}$ 给全部待除的源行。
要求解整个多项式矩阵 $V$，使

$$
VD=W. \tag{2}
$$

对拼接矩阵 $[D^{\mathsf t}\mid W^{\mathsf t}]$ 执行第1节操作，
**只以左侧的 $n$ 列选择主元，但所有操作完整施加到两边**。
于是虽不存储累计矩阵 $U$，仍逐步严格保持

$$
H=UD^{\mathsf t},\qquad Z=UW^{\mathsf t}.
$$

因 $U$ 在 $R$ 上可逆，(2) 当且仅当
$HV^{\mathsf t}=Z$。
按 $H$ 的上三角形从末行向前回代；每个源坐标均须被实际主元准确整除。
任一非零余式立即拒绝，不清分母、不缩放源、不丢行。
所得矩阵还必须全坐标满足原式 $VD=W$。
由于 $D$ 非奇异，分式域解唯一；故通过的多项式解恰为全部源的实际整像。

应用到 R925§24，取

$$
D=M_b,\qquad W=H_I M_a,
$$

其中 $M_a,M_b$ 为原完整乘法矩阵，$H_I$ 为原完整源理想基。
则 $V$ 的整个行模准确是 $(a/b)I$。
第1节的全行模消元给其完整 Hermite 基；保全部306源行及原分母回乘。
这里没有丢弃原 R925§24 的整像条件，只是不显式构造常常很大的 $U$。

## 3. 一个线性标量的完整原像

设 $I\subset R^n$ 为满秩子模，$H$ 是其整行基，
$\pi=t-\alpha$，$\alpha\in k$。
记

$$
K=\ker\bigl(k^{1\times n}\xrightarrow{\ u\mapsto uH(\alpha)\ }
k^{1\times n}\bigr),
$$

并取 $K$ 的**完整域上线性基**，按原 $k\hookrightarrow R$ 嵌入提升为矩阵
$\widetilde K$。因为 $\widetilde K H$ 的全部坐标在 $\alpha$ 消失，
它们逐个被 $\pi$ 整除。则有完整模等式

$$
\boxed{I:\pi
=\operatorname{row}_R\begin{bmatrix}H\\\widetilde K H/\pi\end{bmatrix}.}
\tag{3}
$$

证明：右侧每一行乘 $\pi$ 后都在 $I$，故包含于左侧。
反之，若 $\pi x=uH$，按多项式除法写
$u=u(\alpha)+\pi u_1$。
约化原等式得 $u(\alpha)H(\alpha)=0$，故
$u(\alpha)$ 是完整 $K$ 基的 $k$ 线性组合。
除回 $\pi$ 即得
$x=u_1H+u(\alpha)H/\pi$，属于右侧。
两个方向均使用完整 $R$ 行模，没有分式域饱和或维数推测。

更精确地，映射

$$
K\longrightarrow (I:\pi)/I,
\qquad v\longmapsto vH/\pi\pmod I
$$

是 $k$ 线性同构。满射由上证。
若 $vH/\pi=wH$，则由 $H$ 非奇异有 $v=\pi w$；
因为 $v$ 是常数向量，只能 $v=0$。
所以每一层完整长度恰减少 $\dim_kK$，并且首一行列式满足

$$
\det H_I=\pi^{\dim_kK}\det H_{I:\pi}.
\tag{4}
$$

实现以域上核的全秩和全零乘积认证其完整性，保所有提升行，
核 $\pi D=\widetilde K H$ 的全坐标，再以第1节的可逆消元规范化全部生成元。
(4)是这个已证完整构造的返回条件，不是允许丢掉来源的验收捷径。

## 4. 重因子保全部厚度，适用于原两条标量

若 $q=c\prod_i\pi_i^{e_i}$ 在**原** $k$ 上完全分裂，$c\in k^\times$，则

$$
I:q=\bigl(\cdots((I:\pi_1):\pi_1)\cdots:\pi_2\cdots\bigr), \tag{5}
$$

每个因子准确重复 $e_i$ 次。这直接来自
$(I:a):b=I:(ab)$。
实现完整回乘实际因式分解到 $q$；每个重复层均重新读取当前**整模**，
不先约化其支集，不将重数模化。
只在全部因子是原域上的线性因子时使用此实现；否则明确拒绝，
不暗中扩域或改变原根。

R927§10 的两个原标量分别为

$$
q(\xi)=-\theta_{17}^3\xi^3(\xi^2-9)^3(\xi^2-1),
$$
$$
q_0(s)=-\theta_{17}^3s(1-9s^2)^3(1-s^2)=s^{12}q(1/s).
$$

在 $k=\mathbf F_{29^2}$ 中全部分裂，有限图为
$0$ 重3、$\pm3$ 各重3、$\pm1$ 各重1；
另一图为 $0$ 重1、$\pm1/3$ 各重3、$\pm1$ 各重1。
这是实际全多项式因子，与原 cusp 的306维纤维厚度是两种数据；
(3)–(5)作用于全部306维整模，因而并未把 cusp 纤维改成单点或约化点。

## 5. 接原 F 全零极门

原 $I_A=(a/b)I_B$、$I_A+I_B=A$、$I_C=I_A+qA$ 保持 R927§10 的真实意义。
由 R927§12，完整零理想为 $I_+=I_A:q$，完整极理想为
$I_-=(qb/a)I_+$。
现在用第3–4节得到 $I_+$，用第2节的**全部源整像**得到 $I_-$。
仍必须核完整多项式/Hermite 等式

$$
I_+I_C=I_A,\qquad I_-I_C=qI_B,\qquad I_++I_-=A.
$$

两图各自执行原 $q$、$q_0$ 和同一 $a/b$ 的框转换，
两个符号仍计算完整 infinity boundary，最后才核全次数1296。
原144行全核、全部剩余分母的理想成员关系、1080/4752/3456长度、
实际函数双图交叉相乘、$\theta_{17}$ 相位和所有原常数嵌入均不改变。
没有删减旧几何/算术门。

## 6. 源码与运行范围

新增 helper：`scripts/original_polynomial_row_reduction.py`。
它只在公开 Actions 的固定 Sage 进程中允许运行数学；本地仅作源码/AST检查。
新算法的早期小例核验同时验证完整行模、附加块的所有源、重复因子和单位模；
这些只检测实现/API，不代替第1–5节的证明，也不代替原曲面的任何接受门。

旧五个 run 的实际失败结局见
[接续注](../notes/2026-11-26-geometry-7d29.md)。
新实现没有宣称其失败原因已经确定，也没有宣称必定更快或低于固定内存。
本篇目前只付完整等价算法及接口，原完整 F 除子、四 $E$、shadow、ordinary 与无穷 $p$
仍须分别完成；来源编号和数学对象均保持原样。


## 7. 单个原 F 公开入口已接入

同一个 `rank2-sha-original-low-f-divisors.yml` 入口现选择
`linear_algebra=r942-unimodular-split`，request schema 更新为 v2；
原 F/P 两份完整特征零回执、原 q2453、batch64、原 Sage 镜像及数学断网均未变。
没有启动其余四条旧入口，也没有更改它们的数学源码。

这一次链保原完整144 mixed核、全B理想、所有余行及双图来源。
`OriginalOperationHermiteEngine` 只替换理想行模基算法；
`OriginalFullSourceImageTools` 对每张图先读整个 IA=(a/b)IB，后读整个 I-=(qb/a)I+；
`OriginalSplitScalarColonTools` 对原 q/q0 逐重因子读取完整 I+。
两个完整乘积返回 I+ IC=IA、I- IC=qIB 及全零极互素均实检，
原所有长度和完整 infinity boundary 门保持。

host 与 producer 的同序33源清单已逐一检查存在、AST及交叉一致性；
source manifest 同时记录旧整像/标量 helper 和本次具体实现。
早期 R942 小例在原 maps 常数域中运行，先于昂贵正规化；
它验证API和全源语义，不能代替原曲面门。
host 现在记录真实 Sage/docker 子进程 returncode；旧F的终点仍不能因此追认具体失败原因。

本节只有静态接入，尚无这次运行的数学或性能 PASS。实际 run/job/source 和回执另登记。

| 本次源文件 | SHA-256 |
|---|---|
| `original_polynomial_row_reduction.py` | `465dfb359be5777a1ea2812438d06fcabe5f3d1ec1108e413e32314481a6f7b4` |
| `original_low_f_complete_divisors.py` | `9e539eb0ed99a558924ae4608c006e045843e625e5233740a8140b91489ddabe` |
| `produce-original-low-f-divisors.py` | `80539892d89b2e24734644f9fcaba4c66dfe5b042f6c5decc964373714c8c705` |
| `launch-original-low-f-divisors.py` | `77e810cb5744bbe6975a31b55002ca4dd8f359afe9914d81b30f4b102a490248` |
| `original-low-f-divisors-request.json` | `799480af924f7e055b957b04d9fe5f68ef8570ba5d4af5b4bb6684eab25df4c6` |
| `rank2-sha-original-low-f-divisors.yml` | `1149109e1e25409273a003b9139cecdc7a4da81879131ba6c6411a5ba0e42518` |

## 8. 不假设分裂的一般完整三角原像

下列完整原像定理针对旧 Artinian/Tate 的实际多项式核障碍；本节不更改正在运行的单 F 来源 b35d61dd。它只替换完整整模原像计算，尚无原306对象或性能回执。

### 8.1. 原目标格与全部来源

设 R=k[t]，H 为 n×n 的完整上三角行 Hermite 基，
每个 h_j=H_jj 首一且非零，M 为 r×n 多项式矩阵，r≥1。
所求为全部来源系数的模

\[
 \mathcal L(H,M)=\{v\in R^r:vM\in\operatorname{row}_R H\}.
 \tag{1}
\]

它总是满秩 r：det(H)R^r 包含于它。
在本课题的实际应用，k、R、H 和乘法矩阵 M 均来自同一原正规化；
n=r=306。但证明不依赖 306，也不假 M 可逆。

令 rem_H 为对整个上 HNF 从左到右的准确多项式除法。
每次只减某条完整 H 行的多项式倍数。
故 rem_H(V) 与 V 在整个目标商中同类，并且第 j 坐标次数小于 deg h_j。
余式的唯一性来自 H 上三角及其非零对角，不是一个维数猜测。

### 8.2. 逐列保持的完整来源基

初始 P_0=I_r、W_0=rem_H(M)。
在第 j 步前，保持 r×r 的完整来源基 P_j 以及 r×n 的完整余式 W_j，
满足

\[
 W_j\equiv P_jM\pmod{\operatorname{row}H},\qquad
 (W_j)_{a,i}=0\quad(i<j).
 \tag{2}
\]

P_j 的行模准确等于已经满足前 j 个 Hermite 同余的所有原来源；
不是其中任一同秩子模。
令 w 为 W_j 的第 j 列，h=h_j。
在原来源系数 c∈R^r 中，下一条件恰为

\[
 cw\in hR
 \quad\Longleftrightarrow\quad
 \exists z\in R:\ cw-zh=0.
 \tag{3}
\]

把整个 W_j 下面添一条原目标行 −H_j，把整个 P_j 下面添一条零行。
两块始终同步做相同的完整行运算。
第 j 列原来是 (w,−h)^t；它不是零列，因为 h 非零。

使用换行、加倍行、非零常数倍，以及 R942 已逐式检查的 Bézout 二行操作。
存在完整可逆 U∈GL_(r+1)(R)，把这一列化为

\[
 U\binom w{-h}=(g,0,\ldots,0)^t,\qquad
 g=\gcd(h,w_1,\ldots,w_r)\ \text{首一}.
 \tag{4}
\]

只对这一列选 pivot，所有残余坐标和全部原来源坐标都接受相同操作。
算法不累计整个 U，但每一个实际操作的可逆性、系数和全块返回均保留。

#### 全部核关系与单射投影

U 的后 r 行准确生成列 (w,−h)^t 的整个 R 核。
确实，任意关系 a 都唯一写成 bU；
由 a(w,−h)^t=b_0g=0 及 R 无零因子，必有 b_0=0。
因此不能漏掉任何饱和关系，也没有分式域清分母步骤。

此核投影到前 r 个来源坐标是单射。
若来源坐标为零，关系只有 −zh=0，故 z=0。
其像由 (3) 正好是下一条件的全部来源系数。
于是后 r 行的完整附加来源块给出下一完整基 P_(j+1)；
对应的残余块再由整个 H 准确取余，得到 W_(j+1)。
已清掉的前 j+1 列仍全为零。

这里丢掉的是唯一非零 pivot 行，保留的是全部 r 条核行。
任何来源行即使原残余为零，也必须留在附加块中。
若 w 全零，则整个原来源已经满足本列，直接保 P_j、W_j 不变；
尤其 h=1 的规范余式列自动全零，不另造大矩阵。

由归纳，n 步后 W_n=0，而且

\[
 \boxed{\operatorname{row}P_n=\mathcal L(H,M).}
 \tag{5}
\]

最后仅用 R942 的完整可逆行模算法把 P_n 规范成上 HNF。
该规范化保全部来源，再把每一行乘回原 M、以原 H 全除，复核 (1)。

### 8.3. 每层准确指数是附加核验

同余映射 R^r→R/(h)、c↦cw 的像为 (g)/(h)，所以每层来源指数为 h/g：

\[
 \det(P_{j+1})/\det(P_j)\doteq h/g,\qquad
 \operatorname{length}_k(P_j/P_{j+1})=\deg(h/g).
 \tag{6}
\]

等号中的格为相应行模，点等号只差 R 的常数单位。
所有 h、g 首一，因此最终规范基的首一行列式严格等于

\[
 \prod_{j=0}^{n-1}h_j/g_j.
 \tag{7}
\]

源码把 (7) 与完整最终基的实际行列式相比较。
完整性先由全部一列核及其单射投影证明；(7) 不是用来猜完整性的条件。
全返回则检每条最终来源行的 M 像都属于原完整 H，
不是只检最后长度或约化支撑。

本算法不对 h_j 或 detH 因式分解，不选择新常数域、根或嵌入，
不删除重复因子，也不把目标商换成半单商。
一般不可分剩余和重复厚度都留在原多项式同余中。

### 8.4. 回到原完整有效理想商

原 I⊆C 为同一 Dedekind 正规化上的非零整理想。
保持 R931 的全部生成元约束，候选从 J_0=A 开始。
对 C 的第 j 条原基 c_j，若 J_j 的完整基为 B_j，
其下一完整来源系数正是

\[
 U_j=\mathcal L(H_I,B_jM_{c_j}),\qquad
 J_{j+1}=\operatorname{row}(U_jB_j).
 \tag{8}
\]

(5) 使 (8) 严格等于 J_j∩(I:c_j)，故每个候选包含真正 I:C。
没有把不同 c_j 的秩相加，也没有改成某个方便的整分子。

原 required=detI/detC、全部候选包含方向、
候选范数被 required 整除、以及最终完整乘积

\[
 J\,C=I
 \tag{9}
\]

逐字保留。达到原 required 后才可依已证包含方向终止生成元扫描。
源码重新求整个产品 HNF，要求与原 I 完全相等，并保所有长度。
在 split_support 中，这替代的只是 Fitting 稳定后的真实补厚理想商；
Fitting 平方、原 bad/good 互素、完整 CRT 产品和幂零厚度均不删除。

这没有修改其它 fraction_graph、CRT 求系数或全 π 层范数算法。
那些下一具体操作仍必须各自实际完成，不能借本定理填 PASS。

### 8.5. 独立实现及公开运行门

实现为 scripts/original_triangular_preimage_tools.py：

- complete_triangular_preimage 保一般 r×n 的全部来源，附加完整源块；
- OriginalTriangularArtinianNormTools 只替换实际有效商中的整个来源原像；
- triangular_preimage_preflight 在原 k 内用小例，与 Sage 完整多项式核的
  全投影 HNF 交叉，并验证重复不可约二次因子及零残余来源。

小例仅验证安装 API 与实现语义；不能代替原306对象上的全回执。
每个原消费者仍须绑定全部源码、原固定请求、完整原 F/P PASS、
实际正规化、原 k/omega、两张图、所有厚长度及原边界。
当前尚未接入或启动新的第二份正规化运算，也没有性能 PASS。

每个非零目标列只暂存 r+1 条完整残余行和完整来源行，
矩形大小为 (r+1)×(n+r)；
这不保证运行时间，也不把未执行算法登记为已算出原数学对象。

### 8.6. 小型公开 API 请求

新增 `rank2-sha-triangular-preimage-api.yml` 独立入口，在固定 Sage 10.6 镜像和原规定公开 Actions 内执行两个小型完整模算法检查；明确使用 F29²、a²=2。它不重建原曲面，不启动第二份正规化，也不改变单 F 请求。完整矩形来源、重复不可约二次因子、零余来源和全附加块均与官方小型完整核 API 交叉。源码与定理已登记；公开小例实际结果见§8.7，原306对象仍待。

| 来源 | SHA-256 |
|---|---|
| `original_triangular_preimage_tools.py` | `bb8afb949563f6ab4e7d14774e89e859dedd0c28e7b4734ed166a318a789c195` |
| `check-original-triangular-preimage-api.py` | `34a09ac84aeab9b1c044ed4c6e769b4fdb2ee1d9653cd5c4365d176b1c87ec42` |
| `original-triangular-preimage-api-request.json` | `ed80b3b87bda93897da4224c7961ae150200e89b3d85762e93b8a6de11d04430` |
| `rank2-sha-triangular-preimage-api.yml` | `dfb146f9b825fc3a7fcd351819e360eb6a8f6093bc6c127080d59f1743988ed4` |

### 8.7. 小型完整 API 的实际成功

公开 [run45767886956](https://github.com/Rogerhu12/math-research-public/actions/runs/45767886956)、job139733127722、source `15609ef3fedaf7001cd58a6fe16cac7713104c16` 于2026-11-26 06:24:35 UTC通过两个完整算法检查。固定Sage10.6/指定F29²(a²=2)、12个源码AST、原全行模和全部附加源、重复分裂标量、r=3/n=2原像与官方全kernel投影HNF、重复不可约二次因子及零余来源均过。结果状态为 `both_complete_module_algorithm_API_gates_passed`。实现语义的数学/AST阶段约0.282081秒；这个微型例子不提供原306来源的性能保证或任何原除子、范数、shadow回执。

- result SHA-256：`d6560cee2781baf5bedcb3cbb12ec13cbe4bbe5b0db2ec0d15369dbd4c801a61`。
- manifest SHA-256：`707b68d42645e2e1b0ac69b58ea99b39e58cffba4b7b99a6943cf03f0d5a2092`。
- 工具返回完整job日志UTF-8保BOM，31061 bytes，SHA-256：`6a8c12901607e5a888a914e639c6fa04a0f50f4e3b0c6811dbf66d79901ddf46`。

仅结果陈述和hash登记；完整输出不入库。当前单F来源b35d61dd继续，不因小例成功追认其末端。

## 9. 六原P的完整R3算子复用

下列读取严格保持旧原六P的全部来源，只登记独立helper；当前单F继续，四个P触发路径不改。

### 9.1. 已在同一个原对象中存在的算子

build_original_section_ring_embedding 对每个原退化 j 与原 M2 基 f_a 定义

\[
 u_{j,a}=\pi_j^*f_a/J,\qquad
 M_{j,a}=m_{u_{j,a}}
 \tag{1}
\]

为同一原306基上的完整多项式乘法矩阵。
basis_multiplier 正是通过同一个 operations.multiplication_matrix 构造它，
并把实际矩阵保存在 embedding["actual_multiplier_cache"][(j,a)]。

原六 endpoint 的 selected section_coordinates 已使用这些算子做完整 Horner 读取。
旧 low-P _section_reader 另为每条完整 recipe 调 direct multiply，
没有读取这个已存在的原算子缓存。
本次只改后一段，前面的六个 selected 原截面、vnew、全部 j^3 与 Frobenius 返回均不变。

缓存来源是这个真实 embedding 构造出的矩阵对象。
全 operator 的依据是原完整乘法表和该构造，不是一个 caller 提供的 hash，
也不是单独由 unit*M=u 推知所有行正确。
新代码另检全 unit 行返回作为一致性核验。
缺少的 (j,a) 只通过同一个 certified chart 构造一次；
新增矩阵只在本次完整 reader 中保留，不写入或改写原 embedding 的缓存。

### 9.2. 全部528原行的精确读取

对于原 R3 basis 的每条 recipe r=(a_1,a_2,a_3)，定义

\[
 v_j(())=1,\qquad
 v_j((a))=u_{j,a},\qquad
 v_j((a,r'))=v_j(r')M_{j,a}.
 \tag{2}
\]

这里每次使用全部306来源与全部306输出列。
原 A 是已经认证的交换结合环，因此 (2) 逐步等于同一个实际乘积

\[
 \pi_j^*(f_{a_1}f_{a_2}f_{a_3})/J^3.
 \tag{3}
\]

因子排序只采用原 embedding 的 Horner 约定。
原528条 recipe 的输出顺序完全不变；重复 recipe 也按原位置各自返回，
不会由于内部复用同一向量而少掉原矩阵行。

代码只缓存本批 recipe 所需的全部 suffix。
按 degree=2,3 和原首因子 a 分组，以至多32个完整来源行为一批，
执行整个矩阵乘法 V*M_(j,a)。
这与逐行 (2) 严格相同；没有挑选坐标、随机比较或按某个长度推测乘积。

每个 degree=d 的全部输出满足原过滤界

\[
 \deg(v_i)+w_i\le4d.
 \tag{4}
\]

因此最终 degree=3 的完整坐标槽准确为全部

\[
 (i,e),\quad 0\le e<13-w_i,\qquad
 \sum_i(13-w_i)=3114.
 \tag{5}
\]

所有528行均写入原 k 上的528×3114矩阵，再用原 _unflatten
从每一行的全部槽重建整个306坐标向量并逐行相等返回。
(4) 只证明所有坐标槽的范围已经完整；
实际值由 (1)–(3) 的全矩阵乘法给出，不能由次数门替代。

### 9.3. 原除子门完全继承

新 OriginalLowPOperatorRecipeDivisors 继承原 reader，
只覆盖 _section_reader，保持相同 (flat, slots, receipt) 接口。
所以完整原配对核、两个投影、三原 embedding 的全部常数与 Artin 顺序，
以及之后的以下操作原样执行：

- 每个来源152条配对 N,D，原 numerator 仍为 (2/vnew)*A+B；
- 原两图表、selected pair 及实际传入函数的全交乘；
- 每次使用完整 A 乘法行生成真正非约化理想；
- 同一个非空来源子集对两图同时推进，所有余下 N,D 逐条返回；
- 真有限长度、完整 infinity-primary 理想、零极双2256及六端点全计数。

类的 source receipt 另外绑定新 helper。
原 helper、所有原认证输入、source 追踪、k/omega、Artin(2,0,1)
和全高展开都不变。

待接入 producer 还选择已公开小例通过的 R942 完整可逆行 HNF engine。
这只给实际理想行模选择新的精确实现，不更改它们的生成元或接受门。
尚未运行的原306除子不能由小矩阵 API PASS 追认。

### 9.4. 源码接入状态

新 helper 为 scripts/original_low_p_operator_recipes.py。
已经准备好完整 producer/launcher/request/workflow 对应文本：

- request schema v2 只增加具体 reader 和行模算法名；
- 两份原 F/P PASS 的 run/job/source/result hash 逐字保持；
- q_precision=2453、normalization batch_size=64、原 kernel_method=minimal 保持；
- host/producer 同序34源；缺一源或原请求不一致都拒绝；
- 数学仍只在原固定 Sage10.6 镜像、network none、source read-only 中执行；
- launcher 记录真实 Sage/docker 子进程 returncode。

原 workflow 的这些已有触发路径现在不推送，
因此不会在当前单 F 仍运行时开第二份重型正规化。
当前可单独登记新 helper 与本等价证明；待真正接入后，实际 run/source/hash 另登记。
没有删除完整门，也没有声称能从某个测试时长推定原六除子必能在时限内完成。

### 9.5. 已备接入源码的准确定位

独立helper `original_low_p_operator_recipes.py` 的SHA-256为 `72146ce1b3bc53a30c6bd689db77daa066f11890c474ee471eaa276246978e61`。以下完整小文本已在本仓库建立不可变Git blob，尚未挂到main的对应触发路径；真正接入时必须与最新原入口逐差合并，不覆盖并行修改。

| 原入口 | 目前原blob | 已备新blob |
|---|---|---|
| produce-original-low-p-divisors.py | 7bb9251bd530ec381177c6c709bb632d326a73d7 | 424187aa2cfb5b8c50daad7889916b04536e50d0 |
| launch-original-low-p-divisors.py | 047edc5b9d63b4acf577f31d34c7f925eb911bf3 | 87339541b7bbff11438e448f5976292be1c64a4c |
| original-low-p-divisors-request.json | e6af13264b4cc1e7da8e0e9f2e6b15300b76ff60 | f05f0fa7b6bf6a83d3969617de4ccf3cee4069a6 |
| rank2-sha-original-low-p-divisors.yml | eeedd02b8fe3fe823f27da1ab9ba6bc2ebe4bb62 | 3b89076c157248f96c04458d82df30e8d58cccce |

这些是待接入的源码，不是已执行回执。原两份F/P认证、q2453/batch64/minimal及34源完整绑定均保；没有以“已备”冒原六除子完成。

### 9.6. 同一原 F 的全部 324 条 R2 recipe：准确的二次对应

R942 §9 的原 M2 operator 复用同样作用于原 F 混合 R5/R2 核的
**全部**二次分母来源。这里是不同于端点 R3 的准确输入：
退化指标 j=2，原 M2 拉回矩阵为 120×306，完整原有序 R2 recipe
为324条，每条有两个原索引；原分母核是完整 144×324 矩阵，完整
权坐标数为1890，允许的幂为 0≤d≤8−w_i。

令 b_i 为同一 embedding 的第 i 个 M2 拉回，M_i 为原完整306维
代数中的乘法矩阵。按行向量约定，对任意原坐标行 v，

    v M_i = coords(v b_i).

每条原 recipe (i,j) 的像因此准确等于 coords(b_j) M_i。
原代数交换，允许将这一条 recipe 的两个因子排序以复用 Horner 的
同一 head；**原324条输出行的顺序及重复次数保持原样**，没有只取
不同单项式的子矩阵。M_i 来自同一 embedding 的 actual_multiplier_cache；
已有 operator 直接用同一对象，缺项只在同一认证 chart 构造一次。
完整 operator 的正确性来自原全乘法构造；unit*M_i=b_i 仅作一致性
返回，绝不把一个 unit 行测试当成全部306乘法行的证明。

每次至多32条完整306来源行右乘同一个完整306×306 M_i，保留每个
输出坐标。由原 section 乘法，输出在 L(8P∞)，所以
deg(v_l)+w_l≤8。展为全部1890个权坐标后，对每条原有序 recipe
都从全部坐标重建并返回其完整向量。这给出与旧逐条 engine.multiply
完全相同的 324×1890 flat。最后计算原 **144×324** 分母核乘 flat，
得到全部144条原分母行，不换核基、不缩秩、不选代表。

新薄子类 OriginalLowFOperatorRecipeDivisors 只覆盖
_full_denominator_reader。原 selected 分式的两图全交乘、完整混合核、
原144行的逐行读入、同一行子集的两图 A-ideal 生成、其余全部来源
的归属返回、完整像/colon/乘积返回和两图完整边界全部继承，
原各个 projective degree 门也不修改。没有以 recipe 复用宣告除子
已经返回，更没有引入新的原数值输入或替代常数域。

本次失败 run 45764459557 的324行完整返回实际用到5095.377089612秒。
该记录说明重跑时存在值得修复的重复前置成本；新 operator 读法的
实际耗时必须由后续公开运行测量，不由代数等式估计冒充。

## 10. 完整 paired graph 与仿射单位提升：同一三角原像的两个推论

R931 原厚模路径在有效理想商之后，还有两个真实费用：完整分式图调用第二个 $2n\times n$ 多项式核，分式值与单位逆再调用带全部变换矩阵的多项式单位解。只更换 §8 的有效商尚不能消除这些后继调用。本节直接使用已经证明的完整三角原像和 §3 的附加块整左除法，保留全部原来源和目标坐标。

### 10.1 全分式图的两投影一起返回

设 $R=k[t]$，$M_D,M_N\in\operatorname{Mat}_n(R)$，且 $M_D$ 非奇异。它们在实际路径中是同一原归一化基上的分母、分子乘法矩阵。完整图为
$$
\mathcal G=\{(x,y)\in R^n\oplus R^n:xM_D=yM_N\}.
\tag{10.1}
$$
先用完整行模算法求
$H_D=\operatorname{HNF}_{R}(M_D)$，再按 §8 求完整原像
$$
Y=\operatorname{basis}_R\{y:yM_N\in\operatorname{row}_R(H_D)\}.
\tag{10.2}
$$
$Y$ 保全部 $n$ 个来源方向。逐行使用 §3 的附加块整左除法，求
$$
XM_D=YM_N.
\tag{10.3}
$$
每个条目必须在 $R$ 中，且 (10.3) 回乘全部行、全部列。

**命题 10.1。** $(X\mid Y)$ 是 (10.1) 的完整 $R$-基，不只是其分式域张成空间。

**证明。** 任意 $(x,y)\in\mathcal G$ 的 $y$ 属于 (10.2)，故唯一写为 $y=bY$，$b\in R^n$。由 (10.3)，
$(x-bX)M_D=0$；$M_D$ 非奇异给 $x=bX$。反向包含由 (10.3) 逐项成立。因此全部图和两投影都准确返回。证明允许 $M_N=0$，未要求分子可逆。$\square$

原分式的真极理想就是 (10.2) 的整个分母投影：它记录所有使 $y(N/D)$ 整的原 $y$。在实际整曲线的乘法中，这个模块本来就是理想。不能用某个被选分母 $D$ 的零除子替代它，也不能只保留少数 paired rows。新 helper 返回原来相同的 $X,Y,M_N,M_D$ 与完整极理想接口。

### 10.2 仿射约束必须保留最后一个来源坐标

设 $H$ 是完整非奇异上 HNF，$M\in\operatorname{Mat}_{r,n}(R)$，$b\in R^n$。所需方程为
$$
uM-b=vH,\qquad u\in R^r,\ v\in R^n.
\tag{10.4}
$$
构造整个增广来源
$$
\widetilde M=\binom M{-b},
\qquad
\mathcal P=\{(u,\lambda)\in R^{r+1}:
uM-\lambda b\in\operatorname{row}_R(H)\}.
\tag{10.5}
$$
按 §8 取得完整基 $P$；特别不能丢掉 $\lambda$ 列，也不能在分式域中先把它归一为一。$\mathcal P$ 有满秩 $r+1$：$R^n/\operatorname{row}(H)$ 为扭模，某个非零多项式杀掉整个目标，故其倍乘的全部标准源属于 $\mathcal P$。

令
$$
g=\operatorname{monic\,gcd}(P_{0,r},\ldots,P_{r,r}).
\tag{10.6}
$$
最后源坐标在完整模块中的像准确为理想 $(g)$。故 (10.4) 有整解，当且仅当 $g=1$。若成立，用多项式 Bézout 组合给
$$
\beta P=(u,1).
\tag{10.7}
$$
算法保留整个 $\beta$、整个 $(u,1)$，并回乘 (10.7) 的全部源坐标。最后用完整 HNF 坐标除法返回 $v$，回乘
$$
uM-b=vH
\tag{10.8}
$$
的每个目标坐标。若 $g$ 非单位，准确拒绝该仿射解；不能除以 $g$ 或局部化后接受。

这证明了存在性、必要性和完整返回。多项式 gcd 过程中可以归一基域非零常数；没有逆掉非单位的目标乘子或有理函数分母。

### 10.3 原厚分式值与单位逆保留哪些门

在同一原归一化代数 $A$ 中，令 $I$ 是完整有效理想，$H=I.\mathrm{basis}$，原单位向量为 $1_A$。

对于原分式 $N/D$，先用 §10.1 保整个 paired graph，然后用 §10.2 解
$$
uY\equiv1_A\pmod I.
\tag{10.9}
$$
返回的全局向量为
$$
D'=uY,\quad N'=uX,\quad N'D=D'N,\quad D'-1_A\in I.
\tag{10.10}
$$
原分式在完整厚商 $A/I$ 上的值因此是 $N'\bmod I$。即使原 $N,D$ 在该支上同时为零，(10.10) 仍是先在全局成立的真实分式恒等式，随后才利用 $D'\equiv1$；没有仅凭模 $I$ 的 $hD=N$ 断言可恢复 $0/0$。

值也不依赖选择：若另一组 $(N'',D'')$ 满足同样条件，由乘以原非零因子 $D$ 的单射性得
$N'D''=N''D'$；模 $I$ 后两个分母均为一，故 $N'\equiv N''$。算法另外保留旧接口的全局 cross-product、完整极理想加 $I$ 为单位、以及最终原算子在整个 $I$ 上的返回。

单位逆是 (10.4) 的特例：
$$
uM_h\equiv1_A\pmod I.
\tag{10.11}
$$
返回整个 $u$ 的约化并回乘原完整 $M_h$。目标始终是同一个全厚理想；没有取根基、删重复层或换剩余域。空除子的值与范数约定沿用 R931。

此外，原几何前置调用的 zero_pole_ideals 也必须使用同一完整图，
其零、极理想分别是全部 $X,Y$ 行模的规范化；不能在前置阶段又回到旧的 $2n\times n$ 核。
若完整源理想 $J$ 的基为 $B_J$，原 integral_fraction_multiple 则直接用
已证附加块整除法返回
$
VM_D=B_JM_N.
\tag{10.12}
$
它对每个原基行同时求解并完整回乘；只要一条来源不整就拒绝。
所得像是整个 $J(N/D)$，没有丢掉非整来源或清分母。
新 engine 继承已证完整行 HNF，仅替换这两个调用。

厚值实现类继承 §8 的完整有效商，并只替换 R931 的
fraction_graph、recover_fraction、inverse_unit。R931 的每个 $\pi$-进厚层、原 $k_\pi/k$ 嵌入、完整诱导算子和相对范数仍由原 norm_unit 执行。本节没有实现新 CRT，也没有改原曲面或影子目标。

### 10.4 独立小 API 与尚未接入的生产路径

新独立源为
[original_triangular_artinian_values.py](../scripts/original_triangular_artinian_values.py)；
小入口为
[check-original-triangular-values-api.py](../scripts/check-original-triangular-values-api.py)，固定原先同一 Sage 10.6 镜像和显式算法 fixture $k=\mathbf F_{29^2}$、生成元平方为二。

小入口逐项要求：

- 对非分裂重复因子的 $2\times2$ 完整图，与 Sage 原完整 $4\times2$ 多项式核的两投影作同一个整 HNF 换基比较；
- 对零分子返回全部分母自由源；
- 对 $(\pi t)/\pi$ 返回完整图 $(tI,I)$，保原同时为零情形；
- 对 $3$ 个来源、$2$ 个目标的仿射方程返回全部原坐标；
- 在 $\pi^2(t-1)$ 的全厚模上恢复该共同零分式；
- 对确实无整解的 $\pi u\equiv1\pmod{\pi^2}$ 拒绝，不局部化。

这只检查新接口与小例的执行语义，不是原 $306$ 维曲面、除子、范数或 shadow 的 PASS。新 helper 与小入口不改变正在运行的单 $F$ 任务，也尚未挂进第二个重型正规化入口。实际小 API 回执见 §10.5。


### 10.5 公开小 API 的实际回执（2026-11-26）

公开 run **45776902177**、job **139762630727**，source
`d402e5f22e3ae9abfa515b002c76202f7f299ee4`，于
2026-11-26 07:39:51 UTC 给出成功 RESULT。完整日志含 UTF-8 BOM 共
**42124 bytes**，SHA-256
`ef64f1c6e292110a06f4dc8ef7d7d4265a1553fd211e0ae31c751623314bab36`。
root 已亲读完整图、全部增广原像、非单位拒绝和末 RESULT 的实际回执，并按原始字节核 hash。

同次 run 检查全部 **13** 个来源 AST；实际 helper SHA-256 为
`9327760e26f1666dcd04a22b964b3b15a67b3e7d66e4f66bee84dd350b73db5d`，
完整 manifest SHA-256 为
`225ba33829bffe191c46c92f7dce616badfb935b2eb8be6c98d352e395d006d5`。
末 RESULT 原紧凑 JSON（无尾换行）1606 bytes，SHA-256
`0cbb7c5ea101d4a533f24aed5c73ba49827317137e8ed00fd02d3e052c432815`；
记录耗时 **0.3342467539999916 s**。

§10.4 的全部六项都实际通过：官方全核的两投影相等、零分子的完整图、
共零分式的全局图返回、完整矩形仿射来源、混合非分裂厚模、
以及非单位增广障碍的准确拒绝。没有保存可重算结果文件。
这仍是明确标记的算法 fixture；RESULT 明确没有重算原 maps、
原正规化或原几何，不是 $306$ 维实际除子、厚 Norm、四交或 shadow PASS。


### 10.6 同原生产接入的四个已备源码

在 §10.5 实际通过后，已完整审读下面四个不可变 Git blobs。
当前只登记可审查的源码位置；它们尚未挂到 main 的生产入口，
也未启动第二次 $306$ 正规化：

| 目标路径（本课题 scripts/ci，workflow 除外） | Git blob |
| --- | --- |
| scripts/produce-original-triangular-artinian-shadow.py | `9f49258629538a527765a2edc1f6f9215be080cf` |
| scripts/launch-original-triangular-artinian-shadow.py | `52de62e7f4e6a6c230a3bbcec5388581c0a91ff2` |
| ci/original-triangular-artinian-shadow-request.json | `4e44d037d77d3ad733d36364b7e51e52a1de85da` |
| .github/workflows/rank2-sha-original-triangular-artinian-shadow.yml | `5713d440f42e1bd2f638944ce2dc9d3d4ddd1d5b` |

生产 wrapper 的原始 8003 bytes SHA-256 为
`123abc7793884286b43a2ef5b47074288c5fe0ffac1d628ab75a85ae1a4bd084`。
它先固定核对旧 producer、fraction bridge 与 shadow consumer 的三个完整源码 SHA；
只在本次离线进程中将原 producer/bridge 的完整 ideal engine、
原 producer/consumer 的完整 Norm tools 共四个类绑定，替换为 §10 的子类。
所有旧类身份都须先相等、替换后再相等；结束时还核对原两个实际 $306$ engine、
完整交集上下文和真正 Norm 实例。

之后直接调用原 producer.main，保持原 q2453、batch64、两份特征零 PASS 的
job/run/source/result hash；完整 maps、两张正规化图、混合厚预检、
四个原交集、九个原配对及原 shadow 接受门都不重写。
原 Norm 的全部 $\pi$ 厚层仍由原消费者执行。
它不将“所有厚支持已计入”改称“全部闭点已分解”，
也不宣称 ordinary 或无穷素数结论。

新 workflow 仅监听自身四个新路径，ubuntu-latest、最长360分钟，
host总管上限21000秒；数学容器保持无网络、源码只读，token只给原公开PASS reader。
没有保存正规化或重算数据，没有改共享 bridge 或触发旧重型 workflow。
是否实际完成仍须以未来这条完整生产 run 的回执为准；
随后单 $F$ run45764459557 已失败，准确终点见§11.1；后续v3接入见§11.10。


## 11. 完整多项式行模的有界次数 Hermite 算法

日期：2026-11-26。承接 R942 的全行模、全部附加块和三角原像接口。
本条解决运行时的共同次数障碍，不声称原除子或完整 shadow 已经返回。

### 11.1 实际失败与修复范围

单 F 入口的源为 b35d61ddf92880b44f22fbd2e4284c200c79a8f6，
run 45764459557、job 139721906263。完整日志为 542235 bytes，
SHA256 为
fc8b74d469c4909aafde44cace03eb3519b7da672f0c5c11281db2ef88c1d079。
324 条原 R2 recipe 在 5095.377089612 秒完整返回。随后原 central yF
mixed denominator 的 chart=False、row=1 的 306×306 行模进入 HNF；
594.543392581 秒只完成 16 列，累计 4863 次行加与 17 次 Bézout。
宿主于 5867.785860947 秒明确收到 Sage 返回码 137，
完整流水线未 PASS。日志未记录操作系统杀进程的原因，不能据此确定 OOM。

R942 原算法每步是整 unimodular 变换，模保持证明本身并未失效；
但它没有控制 Bézout 变换的中间次数。只先做一次 unshifted
weak-Popov 再回到同一无界消元，不给出全程次数保证。本条完全去除
该列式 Bézout 阶段，以有界次数的完整 Popov 规约代替。全部原行、
原常数域、原变量、原列序、重复厚度和两图接口均保持。

### 11.2 固定记号与完整行操作

令 R=k[t]，M∈R^{m×n} 满列秩，m≥n。L 为 M 的全部行生成的子模。
记 D=max deg M_ij，δ=dim_k(R^n/L)=deg det H，其中 H 是唯一的
monic 上三角行 HNF。对于非零多项式向量 v 与非负整数 shift s，
定义

    deg_s(v)=max_j(deg(v_j)+s_j),
    LP_s(v)=达到最大值的最右列。

零行的 leader 为 (-1,-1)。只使用下列完整行操作：

- 交换两条完整行；
- r_i←r_i+q(t)r_j，i≠j；
- 以 k× 的元素乘整行。

这些操作的行变换行列式均是 k×，故每步 L 精确不变。若 m=n
且给出任意完整附加块 B，所有操作同时作用于 [M|B]，没有附加列
参与主块的 pivot 选择，也没有删除附加列或按分式比例改换来源。

实现逐条哈希操作、源行号与系数；完成后对每条原 M 行作完整 HNF
除法，验证其余式为零。一个方向由全部 unimodular 操作给出，反方向
由全部原行返回给出。没有把只验证维数或行列式替代模的双包含。

### 11.3 有限的 shifted Popov 阶段

同一 LP=j 的两行中，设主列次数较小的一行为 r_a。以整多项式商
q=(r_b,j div r_a,j) 执行 r_b←r_b−qr_a。被改行的 leader 按字典序
严格下降。这里不需要扩展 gcd。

若该阶段初始主块次数最大值为 E，max(s)=a、min(s)=0，则任何
被改行的 shifted degree 不增，故全阶段主块次数≤E+a。
取 leader 势 n(deg_s(v)+1)+LP_s(v)+1，零行势为0；
每次 weak-Popov 行加使总势至少降1。该势非负，因此终止。
实现逐步核 leader 严格下降、主块次数界，并核行加总数不超过初始势。

满列秩给出恰 n 条非零行及互异的全部 n 个 leading positions。
归一化各 pivot 的首系数后，对每条行，反复选取“可由另一行 pivot
整除其最高次数”的最大 shifted monomial，作整多项式商消去。
选中项严格小于该行自身 leader；从 reducer 引入的项又严格小于
选中项。因此自己的 leader 不变，最大可规约项严格下降，这一阶段
也终止且仍满足 E+a 的主块界。

完成后每个 pivot 列中其它行的次数严格小于 pivot 次数。这是完整
shifted Popov，而不是仅互异 LP 的 weak-Popov。将非零行按 LP
排序，把仅主块恒零的行置底。因为满列秩，所有列都是 pivot 列，
故任何完成的 Popov 主块条目的次数≤相应列 pivot 次数。

设这些 pivot 次数为 d_0,…,d_{n−1}。shifted leading matrix
在按 LP 排序后为三角且对角非零，故

    deg det P = Σ_i deg_s(P_i) − Σ_j s_j = Σ_i d_i.

矩形输入只在最初阶段有 m−n 条主块恒零行，非零的 n 行就是完整
L 的基。因此 δ=Σ_i d_i 是完整模指数；此等式不依赖计算或猜测
一个原有行列式。每个完成的 Popov 主块次数≤δ。

### 11.4 只移动一列的 Hermite 提取

先对 M 全体 m 行作 s=0 的完整 Popov，故这一阶段次数从不超过 D。
其 n 条非零行给出上述 δ；把零行留在底部，后续不再需要操作它们。

归纳地，设当前前 c 列已经提取，上方行保留，余下方阵 P_c 是
unshifted Popov，指数为 δ_c。其条目次数≤δ_c。令 g 是当前首列
所有条目的 monic gcd，e=deg g。只给这一列 shift a，其余列 shift 0。
对全部余行执行上一节的完整 shifted Popov。

若首列其它行仍有非零条目，增大 a 并继续；不丢原行，不仅投影
该列的 gcd。可从当前尾块最大次数加1起步，按倍增增长，截在

    a_safe = δ_c − e + 1.

这给出实际停机界。证明如下：g 整除这一列的每个条目，并在所有
unimodular 变换后继续如此。若完成 Popov 后某个非首 pivot 行
仍在首列非零，则该条目次数≥e，shifted degree≥e+a_safe=δ_c+1。
但其自身 pivot 在另一列，shift 为0，pivot 次数≤δ_c，矛盾。
因此在 a_safe 时首列必须清空，唯一 monic pivot 正是 g。

提取该首 pivot 行后，余行的旧首列全为0，旧其余列的 shift 都为0，
所以留下的尾块自动是 unshifted Popov。列约简条件也完整继承。
其行列式次数恰为 δ_c−e，归纳继续，不需要重新假设尾块的性质。

每次移位阶段的入口为完成的 Popov，故 E≤δ_c；又
a≤δ_c−e+1≤δ_c+1，得到全阶段

    deg 左块条目 ≤ 2δ_c+1 ≤ 2δ+1.

这里不使用 ((n−1)a,…,a,0) 的一次大移位，其总 shift 范围可达
nδ。本算法只移动当前一列、清完就取出，完整主块的统一次数界为

    C = max(D, 2δ+1).

某阶段的实际 a 可以远小于 a_safe。实现逐步核本阶段 E+a 界；
每个阶段输出 E、a、δ_c、实际次数和完整操作计数，没有从理论界
倒推“运行已经成功”。

### 11.5 从完整上三角基到唯一 HNF

前节得到 monic 上三角基 T，其对角次数 d_i 之和为 δ，条目次数≤δ。
自下而上处理每条行 i，按 j=i+1,…,n−1 的顺序，用已经完整 HNF
化的下行 j 对第 j 列取整多项式商。令

    E_i = max_{k≥i}(deg T_ik − d_k).

它在整个行规约中不增：第 j 行的第 k>j 列次数<d_k，
商次数≤E_i，因此引入项在第 k 列的次数≤E_i+d_k−1。
所以主块中间次数≤E_i+max d_k≤2δ。逐步核该不变量，最后再核
H.is_hermite()、全部原行的完整除法与全部对角乘积。

这一步用的是已经完成的下行，不能用一般上三角但尚未约简的行
来假装同一界成立。

### 11.6 附加块的区别与完整整返回

主块次数界不能无条件套到附加块。对 m=n，记全过程主块为 C_i=U_i M，
附加块为 Z_i=U_i B。每个 U_i 由实际的全行 elementary 操作给出，
因此是 R 上的 unimodular 矩阵。由

    U_i = C_i adj(M) / det(M)

只为证明次数而在 k(t) 写此式，实际算法没有按它计算任何分式。
deg adj(M)≤(n−1)D，deg det(M)=δ，故

    deg Z_i ≤ C+(n−1)D−δ+deg B.

实现记录主块与附加块各自的实际最大次数，并分别核各自界。
本式不声称恢复一个完整 U 的矩阵比传递 B 更便宜；实际只传递要求的
整个 B，全 U 不存储。

应用于 R942 的完整左除法时，[M^t|W^t] 在相同全部操作下变成
[H|Z]，然后用完整多项式回代求 V。任何原坐标有非整余数就失败；
最终回乘 V M=W 检查全部来源行。应用于整 paired graph 或三角原像
时，原来完整来源投影及全回乘门继续保留，不能由本条的主块程度界
代替它们。

矩形 m>n 只支持不带附加块的完整行模 HNF；不会丢弃可能非零的
kernel tracking 块。需要 kernel 的旧接口仍用已经证明的完整三角
原像或完整 paired graph，而不是拿本条删除的主块零行猜其投影。

### 11.7 可执行接口与公开小检查

新增独立 helper original_degree_bounded_row_reduction.py，函数为
complete_degree_bounded_row_hermite。它与 R942 complete_row_hermite
的输入输出签名相同，其最初加入时未改生产入口；实际检查成功后的单F接入见§11.10。

公开小检查应在同一个固定 Sage 10.6 镜像、明确的 F_(29²) 算法
fixture 内执行以下全模门：小矩形输入与 Sage 官方 HNF 对照；
方阵附加 identity 得到的完整 U 回乘原矩阵；非方形完整附加 RHS
精确左除法；实际 R942 repeated-scalar、triangular-preimage、paired
graph、affine augmentation 的既有 API；最后一个明确构造、全306
坐标的有重复因子来源矩阵返回其已知完整 HNF。

最后一项仅测算法的306维全坐标与次数行为，不生成原 Y，不是原306
规范化、原除子或 shadow PASS。源代码、参数、版本、实际 run 与
输出哈希登记；不提交运行结果数据表或完整日志。只有实际返回后
才将它接到单个生产入口。


### 11.8 当前独立公开 API 请求

此节全文与实现已由root审读，并独立复核单列shift、完整Popov、δ=0大输入、附加来源的不同次数界和旧接口；δ为完整商的k维数，非未计剩余域次数的R组合长度。新helper原始16513B SHA-256为 `963a0624b2df11e4ba11b573c9a0a1c27c5f2b07c1698acb55954771b798ce9f`。新10分钟workflow只检查明定算法fixtures和完整旧API，不改原生产入口。首次请求时等待实际回执；实际成功已登记§11.9，仍不将全306 fixture当原几何。

### 11.9 公开有界次数 API 的实际成功

run **45781623462**、job **139778213646**，source
`30092c04402ead647dd7467916a20fc3b83b5c50`，
于2026-11-26 08:16:37 UTC返回成功，实际执行 **24.416324761秒**。
root亲读完整日志中的逐阶段、全部旧接口和最终RESULT，并重算原始字节hash。
全部 **14** 个来源AST通过，manifest SHA-256为
`43450f54b53e1098fba3d64d7d4a9aa3929fe49538b35df06d6f5e08f2d9cf45`。
原紧凑RESULT无尾换行 **3330 bytes**，SHA-256
`d890aced1936efda66903b068a957e2743d8f9759c9c3dfdbdf94b9e5efe27a0`。
完整UTF-8 BOM日志 **254833 bytes**，SHA-256
`43be4a09c4e4ae03caa6de77c9ac2cd73e5c1eeff42f5b22ca56f30049f585c0`。
依根规则15，只保来源、参数、run和hash，不提交可重算输出或日志。

小矩形完整行模与官方HNF一致；方阵的完整变换U回乘原矩阵并保持
det(U)为基域单位；非方形附加RHS保全来源整返回；δ=0且输入次数19
的例子实际检查了全局界必须保留D。自适应例
`[[t^7,1],[t^6+1,t^7]]`先使用shift=8，未清完后实际升至15，
并完整返回HNF和附加identity，没有仅测试一次就直接成功的分支。

明定的全306坐标算法fixture实际δ=918、证明界1837，左块实际最大次数5；
其已知完整HNF与全部附加块均准确返回。原repeated-scalar、三角全原像、
完整paired graph、零分子、共同零分式、矩形仿射增广和非单位拒绝接口
也全部通过。该306维例子没有生成原Y、原maps或原正规化，
因此不冒充原除子、四交、完整厚Norm或shadow的PASS。

### 11.10 只接单个原 F 的 v3 生产入口

在§11.9全部实际通过后，原F入口接入有界次数HNF和§9.6全324条
R2 recipe的完整算子复用。旧 complete_row_hermite 现在准确绑定到
complete_degree_bounded_row_hermite；原逐列Bézout函数体已删除，
原整像、全scalar原像和两图ideal engine的调用接口保持。
生产开始前直接断言两个函数对象同一，并实际运行旧完整模preflight。
F reader只将完整分母recipe读法换为薄子类，原两图、144核、1890坐标、
全部剩余来源返回、product/colon和dF=1296的门继续执行。

原请求仍为p=29、q_precision=2453、batch64、minimal，
两份原特征零PASS的job/run/source/hash逐字保持。
schema明确升为v3，linear_algebra标识为
`r942-bounded-popov-split-m2`。host与数学producer的同序来源均为35项，
新bounded和R2 helper都列入manifest与实际reader依赖；
root审读时修正了host旧33项断言为35，未放松来源集合核验。
R2 helper原始9579B SHA-256为
`f15d37d389a7a8d237d1e5743dbb3d9f598c92874cd0748ff0d3cf7c37a77025`。

本次更改的四个既有入口路径及新R2 helper，经当前全部57个rank2
workflow真实源的push paths逐项审计，仅命中既有
rank2-sha-original-low-f-divisors.yml。root另亲读该workflow；
ubuntu-latest、360分钟、宿主21000秒、固定Sage10.6镜像、
数学容器无网络/只读源码及token仅给公开PASS reader均保持。
没有启动第二个原306正规化或Artinian重型任务。
本节记录接入与等价性，实际原除子是否返回另以本次run终点登记。

## 12. 七条原椭圆方程的三代表运输及完整整返回

本节只改变同一已认证原 map builder 中七条方程的重复展开次数。
原根的全局身份、全部原尺度、六个端点的 W 身份和全部常数反射
身份继续逐个以原306坐标的完整交乘验证。下游的完整除子、原
Artinian 商、非约化厚度、全局 norm 和原 shadow 门没有变化。

### 12.1. 原完整环上 W 的整性域与全部过滤来源

沿用 R925 与原函数桥证明，令

    Y=X_0(3468), ξ=y_s, P∞=div∞(ξ),
    A=Γ(Y−Supp(P∞),O_Y)=⊕_{i=1}^{306} k[ξ] b_i,
    W_n=L(nP∞)=⟨ξ^j b_i : j+d_i≤n⟩_k.

这里 k 是原 local context 的 F_(r²)，r=29或41；所有 basis、权 d_i、
原 F_r 乘法结构常数、原常数扩张和另一完整图表保持。W 是 R883
附录C、R924(41) 已识别的同一源自同构，而不是在曲线上新猜的变换：

    W(ξ)=(ξ+3)/(ξ−1), W²=1,
    π2∘W=π2, π1∘W=π4, π4∘W=π1.

设 h=ξ−1，P1=div0(h)。由于 W(h)=4/h，完整除子（包括每个分歧
和 cusp 的真实重数）满足

    div(h)=P1−P∞,  W*P∞=P1,  W*P1=P∞.

因此对每个 n≥0 及整个 W_n 定义

    T_n(a)=h^n W(a).

若 a∈L(nP∞)，则 W(a)∈L(nP1)，乘 h^n 后回到 L(nP∞)，且

    T_n²(a)=h^n W(h)^n a=4^n a.

4∈k×，所以 T_n 是 **整个** W_n 的 k 线性自同构，逆为
4^(−n)T_n。没有仅在若干底函数的值或某个短展开上宣称源满秩。
特别，对任意 a∈A，选其真实过滤界 n，则 W(a)=h^(−n)T_n(a)，
所以 W 是 A[h^(−1)] 的自同构。W 通常不是 A 本身的自同构；
本节不会在 A 或一个固定非约化商上错误假设 h 可逆。

实现仍按原生成元计算实际 W：ξ按上式替换，原常数固定，已经通过
R926完整全局身份的 RF、vF、Ri、Yi，分别按上述 πj 函子性运输。
原 builder 的 formulas(swapped=True) 因而是实际 W 的计算；
七椭圆方程从未被用来定义或证明 W，故以下没有循环论证。

本引理给全部过滤来源的整返回证明，不声称已经构造任意原
306/666维基的 W 矩阵；具体原函数仍通过已认证截面拉回表达式计算。

### 12.2. 常数反射确为完整代数的半线性自同构

令 σ 只将 k 系数 c 变为 c^r，固定 ξ 及全部 b_i。R925§15.4
和实际全乘法表的每一块给全部 C_ij;l,e∈F_r，而不是仅抽查若干
乘积。因此 σ 对整个 A 满足 σ(ab)=σ(a)σ(b)、σ²=1，
并保每个 W_n。原另一图 c_i=ξ^(−d_i)b_i 也被固定，
所以两图全来源都保持；该 σ 不是函数幂 f↦f^r。

保原 Artin 次序及 R883(D2)–(D5) 的尺度与相位：
σ(θ17)=−θ17，σ(ω)=ω^(−1)，σ(v)=v，v=ξ²−1。对原有序
A_0,A_1,A_2，j=0,2，实际完整交乘门为

    σ(x_0,j)=x_0,j,              σ(y_0,j)=y_0,j,
    σ(x_1,j)=ω^(−1) x_2,j,      σ(y_1,j)=y_2,j,
    σ(x_2,j)=ω^(−1) x_1,j,      σ(y_2,j)=y_1,j.

还保 σ(f0)=f0、σ(yF)=−yF 的原门。所有 x_i,j 是目标横坐标
除以原 x_s 的函数；不遗忘这个原 scale。

### 12.3. 三个直接代表与四个完整运输

首先在原完整306代数中直接验证：

    E_F=yF²−v f0³−1=0,
    E_0,0=y_0,0²−v x_0,0³−1=0,
    E_1,0=y_1,0²−v x_1,0³−1=0.

每个等式仍由原完整分式交乘读出，不以较少系数、点值或 dimension
替代。由 σ(E_1,0)=0、上节实际反射身份及 (ω^(−1))³=1，得
E_2,0=0。

令 c=2/h。原恒等式 W(v)=c³v，连同全部原 W 交乘门给

    c W(x_i,0)=x_i,2,   W(y_i,0)=y_i,2  (i=0,1,2).

故

    E_i,2 = W(y_i,0)²−v(cW(x_i,0))³−1
          = W(E_i,0)=0.

逆端点的三条 W 身份、F 的 W 身份和 T/T0/T2 的原等式也保留，
并非仅检查用于此推论的最少几条。以上准确覆盖七个原标签：
直接 F、A0q0、A1q0；反射给 A2q0；W 给 A0q2、A1q2、A2q2。
没有合并原函数对象，也没有给未算的标签赋零。

为了把代数推论作为可核的一般证书，可在独立整系数多项式环验证
以下两条形式恒等式，然后将变量代入同一原函数域。它们不涉及
近似值：

    (Y²−vX³−1)−(B²−VA³−1)
      =(Y−B)(Y+B)
        −v(X−cA)(X²+cXA+c²A²)+(V−vc³)A³,

    (B²−vA³−1)−(Y²−vX³−1)
      =(B−Y)(B+Y)
        −v(A−λX)(A²+λAX+λ²X²)−v(λ³−1)X³.

第一式中 A=W(x_i,0)、B=W(y_i,0)、V=W(v)、X=x_i,2、Y=y_i,2。
第二式中 A=σ(x_1,0)、B=σ(y_1,0)、X=x_2,0、Y=y_2,0、
λ=ω^(−1)。右侧每个 factor 是既有全坐标交乘门或确切原常数门。

### 12.4. 非零因子及任意非约化商的正确下降

A 是同一光滑不可约原曲线的整环，完整306基使 A⊂k(Y) 单射。
每个实际分式 (N,D) 都保全部坐标，且构造器已经验证 D≠0。
因此 D 是 A 中非零因子，所有实际分母及 h 的乘积仍为非零因子。
允许的共同标量约分逐条核原612坐标整返回；不按 norm 的 gcd 约分。

对任一被运输的方程，写 x=Nx/Dx、y=Ny/Dy。前节在 k(Y) 证明
其等于0，所以其完整清分母子

    Z=Ny² Dx³ − v Nx³ Dy² − Dy² Dx³ ∈ A

在 A 中准确等于0：这是 A 到其分式域的单射，未在商环取消任何元素。
因为306基在 k[ξ] 上自由，Z=0 是全部306原坐标同时为零，
不是只在 generic point 上通过的不同来源函数。

随后对任意完整有限理想 I⊂A，Z 在 A/I 中仍为0，包含任意
π-primary 厚度和所有 nilpotent 层。这不要求 W(I)=I 或 σ(I)=I，
因为先在原 A 得到全局恒等式，再降至实际 I；从未强行在同一个
厚商中定义 W 或 σ。

若需要在 A/I 中读取 x、y，必须先满足现有完整 regularity/unit
门。选中的显示分母可能在 I 上消失；这时用 R942§10 的完整
paired graph 和 affine augmentation 找到全局同函数 N'/D'、
D'≡1 mod I。随后以真正单位分母的表示在 A/I 中读取。全局
椭圆方程经上述严格整返回自然给整个非约化商上的原方程。
下游 _WholeQuotient.curve_gate 仍直接核完整商上的方程。

在另图 s=1/ξ，用同一真实 pole bound 的完整306坐标反转式
N∞,D∞ 同时乘 ξ^(−M)，再逐坐标反转返回。此图的 v 也必须写成
自己的完整分式 Nv/Dv，不能假设 v 在 ξ=∞ 整。相应整清分母子为

    Ny² Dx³ Dv − Nv Nx³ Dy² − Dy² Dx³ Dv.

全部显示分母在该图原整环中仍是非零因子；因为该图仍是同一个
k(Y) 的子环，此完整清分母子准确为0。ξ=∞ 的所有厚层继续由原
完整 boundary ideal 和原 regularity/unit 门读取，不由有限图点值补猜。

### 12.5. 接口边界

未来独立 builder 可以把旧七次直接展开改成上述三次；除这一段的
执行顺序、形式证书与详细 provenance 外，应逐字保留原 root/
compact/source、原常数、原七函数定义、全 W 与全反射门。应明确
登记哪些代表直接展开、哪些通过完整身份运输，不能称每条都重新
计算过同一昂贵立方。

旧 producer、bridge 与下游 consumers 可以用新独立入口的明确
函数绑定来调用它，避免修改 shared bridge 而同时触发多个重型
workflow。本节证明不表示当前原 maps/除子/shadow 入口已经切换，
也不表示新的实际性能或最终原 shadow 已经返回。

### 12.6 独立源码与公开小 API 接口

root已完整审读本节证明、独立builder及小API；并亲读原完整乘法
context与fast adapter的生成位置，核对新增全表字段确实来自同一原对象。
独立helper original_ys_equation_transport.py 原始17236B SHA-256为
`5f16e13e0ea46086384eb261e750855a206e503c85e81575e5d771e7a0950036`。
旧完整bridge SHA固定为
`788949117cba32c3ce347257ab71681bfe4a6940f935e017efef852c6ea4d9b8`。

小API只检查两条ZZ形式恒等式、原W的有理标量身份，以及新旧builder
全部root/source前缀、公式、双向W loop、所有反射loop和返回context的
逐AST同一性。独立workflow为10分钟固定Sage10.6，只监听四个新路径；
没有调用原正规化或接入Artinian生产，也不影响正在运行的单F。
本次仅发出公开检查请求，实际成功与否另记；不以小API冒原maps PASS。

### 12.7 独立运输 API 的实际回执

run **45784345594**、job **139787226926**、source
`2a343a67de47f90e2061152d0fc25a0cae1206dd`，
于2026-11-26 08:35:34 UTC实际全部成功，耗时
**0.07261244299999703秒**。root亲读来源manifest、全部AST保持门、
两条ZZ恒等式、原W有理标量式及最终RESULT，并核原始字节hash。

同次 **7** 个明列来源AST通过；manifest SHA-256为
`5ce9d9fa7869bd855246f91875931ccf3f054ff9c3b4c5a44b9dee0131afcccf`。
紧凑RESULT无尾换行1678 bytes，SHA-256为
`2291ee58c9b018148384572ebd5b0a9eaa7dbc5fa2fb53c26c3e08ea13ea483e`；
完整日志20398 bytes，SHA-256为
`a69d8580152eae31fcb1eaee526dc1ed2d3d57743b7e4e80c80b3c7705189e4a`。

原root/source前缀、函数定义、完整双向W与全部反射loop及最终context
的逐AST比较全部通过；相同原断言仅去除被证明运输覆盖的y2直接立方项。
这检查形式证书和源码保持，不生成原maps/正规化/除子或shadow，
也没有将独立builder挂入第二个重型生产。实际单F v3继续使用自己的
完整原来源及前述有界次数修复。


## 13. 原 W 在完整306基上的次数4整矩阵：同一 R3 来源的有限恢复

本节给 §12.1 的全过滤自同构一个可直接实现的完整矩阵构造。
它只使用同一原中央 π2 的完整 R3，不对306曲面另作正规化，
不新增常数域，不把点值或短展开当作全局证书。本节尚未执行
原306矩阵的实际构造；所有实际回执须另行登记。

### 13.1. 原函数域、两图及准确加权次数

仍令 B=X0(867)、Y=X0(3468)、ξ=y_s。以下具体的次数4、五系数构造
以已经有完整权4回执的原 r=29、k=F_(29²) 为执行目标。
函数域、纤维满秩和中央身份的证明对 r=41 也成立；在该素数尚未
认证权4以前，须用 R925 的无条件最高权5，改为次数5及六个系数，
不得把 r29 的 h3 回执跨素数使用。
R883 H.1 及 R882 给

    k(Y)=k(B)(ξ),  [k(Y):k(B)]=6,
    T=φ(ξ)=ξ²(ξ²−9)²/(ξ²−1)².

因此 Y 是同一 B×_(P1_T)P1_ξ 的光滑射影正规化。
这是从原几何次数6和原函数的双向返回识别的函数域，未选新的分支。

沿用原两个完整图表与权：

    A∞=⊕ k[ξ]b_i,  A0=⊕ k[s]c_i,  s=ξ^(−1),
    c_i=ξ^(−d_i)b_i,  0≤d_i≤4（原 r29 已认证版本）,
    W_n=L(nP∞)=⟨ξ^j b_i:j+d_i≤n⟩_k.

设 h=ξ−1，Wξ=(ξ+3)/h。§12.1 已在所有完整除子上证明
T_n(a)=h^nW(a) 保整个 W_n，并有 T_n²=4^n。
故对每条原基 b_i，存在唯一的多项式矩阵 C 满足

    h^(d_i)W(b_i)=Σ_j C_ij(ξ)b_j,
    deg C_ij≤d_i−d_j.                                      (13.1)

当 d_i<d_j 时，C_ij 必须为0。每个条目次数至多4；
此上界来自原完整过滤，包含全部 cusp 重数。
没有从若干展开系数反推一个未证明的次数帽。

另一图的对应矩阵也已经由同一个 C 决定：

    D_ij(s)=s^(d_i−d_j) C_ij(1/s)∈k[s],
    W(s)=(1−s)/(1+3s),
    W(c_i)=(1+3s)^(−d_i) Σ_j D_ij(s)c_j.                   (13.2)

所以 C 的完整构造会同时给两个图的全部原基运输；W 并不因此成为
A∞ 或 A0 各自的整环自同构。分母 h 或 1+3s 的零处仍须保另一图。

### 13.2. 原完整528源在 ξ=2 纤维上必满306秩

R924§1 的原线束为 L=Ω_B¹(C_B)，deg L=204，g(B)=85，
完整 R3=H⁰(B,L³) 的维数528。原完整乘积 recipes 已经按同一
Sturm/整格及原窗口核准，故这里使用该全部528行与其原顺序。

令 a=φ(2)=100/9。直接求导给

    φ'(ξ)=2ξ(ξ²−9)(ξ²+3)²/(ξ²−1)³,
    φ'(2)=−980/27≠0                                   (r=29,41). (13.3)

P1_ξ→P1_T 在 ξ=2 的一个邻域 étale。其对光滑 B 的 base change
仍 étale，因而正规；原正规化 Y 在该邻域是同构。于是这里有的是
整个纤维概形的同构

    Y×_(P1_ξ){2} ≅ B×_(P1_T){a},                         (13.4)

并非仅是几何点集的对应。任何残余域和非约化层都随之保留。

R883 的原 deg(T)=306。因此 D_a=div_0,B(T−a) 长度306，且

    deg L³(−D_a)=612−306=306>2g(B)−2=168.

Riemann–Roch 给 H¹(B,L³(−D_a))=0，所以全部 R3 向
H⁰(D_a,L³|D_a) 满射，目标维数306。

原 embedding 把每条真实 a_i∈R3 读成

    p_i=π2*(a_i)/J³=Σ_j P_ij(ξ)b_j,                      (13.5)

其中 J 是原同一截面框，div(J)=4P∞，故在 ξ=2 纤维为单位。
其原对数微分因子 2³ 已包含在 π2* 内；没有在此重新定尺度。
(13.4) 和乘上该真实单位说明矩阵 P_all(2)（528×306）秩恰为306。
这不是预设全R3在泛点张满，而是完整纤维限制满射的结论。

实际构造时必须从 P_all(2) 的原528行选择306条线性独立行。
例如对转置取枢轴列。保留行号和全部原行的 hash；不得用含 ξ
系数的行组合替代，因为下一节的中央 W 本征身份逐条作用于
原 π2 来源，而不是作用于人为的 k[ξ] 组合。

### 13.3. 中央原来源的完整 W 身份及可逆的常数矩阵

原 builder 已完整证明

    SY=π2*S/J=(ξ²+3)²,
    W(SY)=16 h^(−4) SY,
    π2∘W=π2.                                              (13.6)

π2*(a_i)/π2*(S³) 是原 B 函数的拉回，所以 W 固定它。
由 p_i=[π2*(a_i)/π2*(S³)] SY³ 得到准确的函数域身份

    W(p_i)=4^6 h^(−12)p_i.                                (13.7)

原完整权12表示给 deg P_ij≤12−d_j。定义全体多项式

    Q_all,ij(ξ)=h^(12−d_j)P_all,ij((ξ+3)/h)
              =Σ_e p_ij,e (ξ+3)^e h^(12−d_j−e).          (13.8)

不存在负指数，也不需分式约分。将 (13.1) 代入 (13.7)，得到
全部528行的完整多项式矩阵身份

    Q_all C=4^6 P_all.                                    (13.9)

取上节选中的306原行，记其方阵为 P、Q。因为 W(5)=2、h(5)=4，

    Q(5)=P(2) diag_j(4^(12−d_j))                          (13.10)

可逆。这是原常数域中的一次完整306阶可逆性判据。
不需要在 k(ξ) 上求逆高次多项式矩阵。

### 13.4. 五个 Taylor 系数的准确恢复和全部原来源回乘

写 τ=ξ−5。实际由 P、Q 取准确多项式 Taylor 系数：

    Q(5+τ)=Σ_l Q_l τ^l,  P(5+τ)=Σ_l P_l τ^l.

先求一次 Q_0 的原常数域逆并完整回乘。令 λ=4^6，递推

    C_0=Q_0^(−1) λP_0,
    C_l=Q_0^(−1)(λP_l−Σ_(j=1)^l Q_j C_(l−j)),  1≤l≤4.   (13.11)

得到 C(ξ)=Σ_(l=0)^4 C_l(ξ−5)^l。准确性来自两个已证明事实：
真实 C 确实存在且每条目次数≤4；Q_0 可逆使它的0至4阶系数
由 (13.9) 唯一决定。因此这五个系数已经唯一确定真实全局矩阵。

实际接受仍必须执行以下全门：

1. 核全部306²条目的加权次数界 deg C_ij≤d_i−d_j；
2. 核全部原528行的多项式回乘 Q_all C=λP_all，含所有系数，
   不仅所选306行、不仅 ξ=5 或 τ^0…τ^4；
3. 核下一节全部306行的整逆身份；
4. 保原528 recipes、全部真实 π2 拉回、完整乘法来源和所选原行号。

可以将多项式矩阵拆成其全部系数矩阵作有限域矩阵乘法，再完整
卷积相加；所有超过右侧真实次数的系数也必须为0。
这只是完全相同的多项式乘法，不是点值插值证书。
π2、原基和 W 均定义于原 F_r，故理论上 C 的系数也在原 F_r。
若实现采用该原素域的快矩阵，须先逐个核全部 P_all 系数在原
F_r、再用同一个已认证嵌入返回 k；不得另选一个同构的二次域。

### 13.5. 完整整逆、两图返回与厚商边界

定义

    Cstar_ij(ξ)=h^(d_i−d_j)C_ij((ξ+3)/h).                 (13.12)

当条目非零时 (13.1) 保证右侧为多项式，仍用完整系数公式构造。
由 W²=1，

    Cstar C=diag_i(4^(d_i)),                              (13.13)
    C^(−1)=diag_i(4^(−d_i)) Cstar.                       (13.14)

因此 C 是整个自由 k[ξ] 模的幺模矩阵，而非只有泛点秩306。
实际构造应核 (13.13)，并核 (13.14) 的左右两个完整乘积。
(13.2) 的 D 则由每条目完整反转读出，也要核反转回 C，所有
d_i<d_j 位置仍严格为0。

对任意原全源 a=Σ a_i(ξ)b_i，

    W(a)=Σ_i a_i((ξ+3)/h) h^(−d_i) C_i.

给定它的真实全局权帽 n，先在原整环计算 h^nW(a) 并核全部
306坐标，分母只记录为真实 h^n。这样可以把一整组原理想生成元
运输到 A∞[1/h]；所有原源行与重复厚度均保留。

但是把该局部化理想收缩回整个 A∞ 时，h=0 的原支撑不会自动
返回。必须从另一原图运输完整 h-primary 部分，再同远离 h 的
部分粘合。仅作 h 饱和或只比较 determinant 次数不足以给
原完整除子。因此本节给完整基运输的构造，不提前宣称六个原
P 极除子、任意厚理想或四交除子已通过；这些仍保各自全门。

### 13.6. 实现成本、素数界限与事实范围

本构造的新增来源是同一原中央完整528个R3 recipe 像，允许
依 R942§9 的方式精确复用同 embedding 的完整 M2 乘法算子，
但输出须保528原行序、全部3114权坐标及完整回填。
之后只需常数域306方阵的一次逆、五个系数的递推以及全部
多项式回乘；不启动第二次正规化，不借不相关的306维代数。

若之后在 r41 用最高权5版本，(13.1) 改成最高次数5，(13.11)
递推至 l=5；其余完整528行回乘、整逆和两图全门相同。若有该
素数自己的真实权4回执，才可改回五个系数。

当前只登记这个完整数学构造与待执行门。没有原306 W 矩阵的
实际 RESULT、运行时间或 PASS；也没有据此替代当前唯一 F 作业。


### 13.7. 全部三组120原M2与相对另一端的完整来源运输

这一步进一步核定源自同构在三个实际退化映射上的身份，而不
使用七条椭圆方程来定义 W。这里 π2*S 是原全局对数微分截面，
SY=π2*S/J 是 (13.6) 的有理函数，二者不得混同。
由 π2∘W=π2，在 W*(π2*L)=π2*L 的自然识别下，

    W*J=(π2*S)/W(SY)
        =J·SY/W(SY)=h^4 J/16.

故对任意原 a∈H⁰(B,L^m)，若 p_j(a)=πj*(a)/J^m，则

    T_(4m)(p_1(a))=4^(2m) p_4(a),
    T_(4m)(p_2(a))=4^(2m) p_2(a),
    T_(4m)(p_4(a))=4^(2m) p_1(a).                        (13.15)

πj* 是原真正的微分拉回，原 q 退化中的 j^m 因子已经包含在
(13.15) 内；不能在实现中把这三个因子另行抹去。

同一次 embedding 已实际给三个 120×306 的完整原 M2 拉回，
所以新 C 构造后应以全部多项式系数直接回乘核

    T4(pull_1)=16 pull_4,
    T4(pull_2)=16 pull_2,
    T4(pull_4)=16 pull_1,                                (13.16)

包含三个完整120行块及每条原306坐标。原 central R3 满秩保证
C 就是真实 W；(13.16) 再以实际原另一端数据核其整个低权来源。

因此未来读取完整528个原R3的 π4 像时，可在保留全部原
recipes、原行序与完整加权坐标的前提下，从其已实际构造的
π1 像逐行使用 4^(−6)T12 返回。来源的完整性由原R3和
(13.15) 保证，不由有限个点的值代替，也不需要重新创建一组
π4 的120个完整乘法算子。任何具体接入仍须记录哪些原行由
完整运输得到，保原两图、全部152成对行及各自极理想全门。

### 13.7a. 独立源码与小 API 请求

原完整helper `original_full_w_basis_transport.py` 为23625 bytes，SHA-256
`fcb13dc02e2c2b7d4479222fe07104b0c62eee77c9e8ba753ba43734b23309db`。
root已逐式审核上述证明、全部原528源的后缀读取、所有完整卷积回乘、
两图加权逆及三组120原M2回乘；原全部依赖导入闭合为4份明列源码。
独立小API使用固定Sage10.6、只读来源、禁网容器及10分钟上限，
检查非恒定权4矩阵、额外未选源行损坏的真拒绝、权5六系数、同一
二次域准确返回/非素域系数拒绝与权0边界。仅监听四个新增路径，
不改现有单F入口或接入第二原306计算。实际结果待公开Actions返回；
构造fixture成功也不能登记为原W、原除子或shadow PASS。
