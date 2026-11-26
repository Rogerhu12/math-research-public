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

新增 `rank2-sha-triangular-preimage-api.yml` 独立入口，在固定 Sage 10.6 镜像和原规定公开 Actions 内执行两个小型完整模算法检查；明确使用 F29²、a²=2。它不重建原曲面，不启动第二份正规化，也不改变单 F 请求。完整矩形来源、重复不可约二次因子、零余来源和全附加块均与官方小型完整核 API 交叉。源码与定理已登记，公开运行结果待收，不预填 PASS。

| 来源 | SHA-256 |
|---|---|
| `original_triangular_preimage_tools.py` | `bb8afb949563f6ab4e7d14774e89e859dedd0c28e7b4734ed166a318a789c195` |
| `check-original-triangular-preimage-api.py` | `34a09ac84aeab9b1c044ed4c6e769b4fdb2ee1d9653cd5c4365d176b1c87ec42` |
| `original-triangular-preimage-api-request.json` | `ed80b3b87bda93897da4224c7961ae150200e89b3d85762e93b8a6de11d04430` |
| `rank2-sha-triangular-preimage-api.yml` | `dfb146f9b825fc3a7fcd351819e360eb6a8f6093bc6c127080d59f1743988ed4` |
