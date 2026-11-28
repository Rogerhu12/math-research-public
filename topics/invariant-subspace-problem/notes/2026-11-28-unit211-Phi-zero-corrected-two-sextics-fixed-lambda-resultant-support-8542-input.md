# 新输入：正确两条原六次的固定 lambda 结果式与非零纯权支持

日期：2026-11-28（Asia/Taipei）。尚未执行；只准备新目标，不预记非零、有限性或排空。

## 1. 整个正确原图的已成来源

沿[正确整个原 $I_6$ 的十五列三坐标呈示](../results/R150-appendix-unit211-Phi-zero-corrected-whole-original-I6-fifteen-by-three-and-two-sextics.md)，当前 $\Phi=0,D_{\rm phys}\ne0$ 图已有
$$
C_{\rm NP},C_{\rm ov}\in I_6,\qquad
\deg_\lambda C_{\rm NP}=\deg_\lambda C_{\rm ov}=6.
\tag{1}
$$
其系数只在原已付纯权环中使用分母
$$
Q(1-Q)(u-1)KLM_nAB.
$$
$u$ 还由整个原零基点 mean 排除支付。原三均值头由完整正确 $A=0,B=0$ 排除支付，不借错误旧紧凑式。

(1) 的参数 SHA256 为

    fcf79be98410a2eea2ebdb588b441b8f4aceb20acb4704a96ee34fc0012d01d5
    2407107501f1790a288ecabd75f14f92c7602859bfc033727b76312675f91014

其 $(u,Q,\lambda)$ 双单次数和总次数分别为
$$
(42,22,6),\ 47;\qquad (30,15,6),\ 33.
$$
两头的已成完整 QQ 支持为 $uH_{31}$ 与 $H_{14}$，互素，当前物理 $u\ne0$ 后共同零权点至多 $434$。这只限制共同头零的权支持；其完整 $\lambda$ 和几何纤维从未排除。

## 2. 必要定义边界与依赖

新源仅读取下面两个已刊小源码：

    2026-11-28-unit211-Phi-zero-corrected-whole-original-I6-fifteen-by-three-8542.py
    2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py

完整 SHA256 分别为

    84e0efcc19a0274d571484b187b7b155c81ebf255e40a39c38ac13a03f911cf0
    5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7

新源在 AST 执行之前，外层显式读取并核对上述两个完整源码的 SHA；第二文件的完整性检查不依赖被省略的旧顶层 assert。

第一文件只取 seeds 定义前 $12067$ 字节，SHA256：

    e2e9bab84bca700400c8e26d5787208c9aceafe27c64aa7ecf828b0552025a1f

AST 选择与已成两头新输入一致：只保创建原四式系数的定义循环，省去旧动作、overlap、矩阵缺陷、NSPS 末审核、十五列和 cofactor 全坐标证明门及只为这些检查服务的赋值。第二文件内部只取其已定 $4007$ 字节的正确原式定义。

新源从已成三个实际乘子的公内容定义，再生 (1) 的标量系数，核准确两 C6 和两头 SHA。没有执行旧头因式、gcd、有限点界、六式空性或任意旧投影门。

## 3. 真正新固定多项式矩阵

先分别用非零有理常数将 (1) 整数化并除整数公内容，得到
$$
\widehat C_i=c_i C_i\in\mathbb Z[u,Q,\lambda],
\qquad c_i\in\mathbb Q^\times.
\tag{2}
$$
全部原系数尺度精确乘回。这里只改变非零常数，所有原根和首项零纤维不变。

取固定 $12\times12$ 矩阵 $\mathcal S(u,Q)$：前六行为
$\lambda^r\widehat C_{\rm NP}$，后六行为
$\lambda^r\widehat C_{\rm ov}$，$0\le r<6$，列为
$1,\lambda,\ldots,\lambda^{11}$。定义
$$
F(u,Q)=\det\mathcal S(u,Q)\in\mathbb Z[u,Q].
\tag{3}
$$
本源只用该精确矩阵定义，不展开大的 QQ 行列式。

在每个原点，两个真正原六次为零，因此
$$
\mathcal S(1,\lambda,\ldots,\lambda^{11})^{\mathsf T}=0.
$$
更准确地，$e_0^{\mathsf T}\operatorname{adj}(\mathcal S)\mathcal S
=F e_0^{\mathsf T}$，乘以同一个单项式列，给
$$
F\in(\widehat C_{\rm NP},\widehat C_{\rm ov})\subset I_6.
\tag{4}
$$
这是全已付系数环上的原多项式身份，不需要原三生成元自由，也不倒任何 $\lambda$ 首项。尤其两头同时为零的至多 $434$ 个权点和所有降次纤维也被 (4) 完整覆盖。

## 4. 严格次数上界

$\lambda^j$ 系数的纯权总次分别至多 $47-j$、$33-j$。对固定矩阵的第 $r$ 行，赋权 $47+r$ 或 $33+r$；第 $j$ 列赋权 $-j$，编号均从 $0$ 起。每个非零条目的实际 QQ 总次数都逐项核在对应行列权和内。于是
$$
\deg_{u,Q}F
\le\sum{\rm rowweights}+\sum{\rm colweights}
=6\cdot47+6\cdot33-36=444.
\tag{5}
$$
这只是严格上界，不是 QQ 精确次数或模观测次数，也不靠预期的最高项无取消。

## 5. 固定素数、事前点表与唯一新非零测试

事前固定 $p=1009$ 和依序候选表
$$
(2,2),(3,2),(4,2),(5,2),(6,2),(2,3),(3,3),(4,3).
\tag{6}
$$
选择第一个满足以下条件的点：

- 原已付权乘积和 $u$ 在模 $1009$ 下非零；
- (2) 的两个真正固定 $\lambda^6$ 首项在该点都非零。

选择只看输入、原单位和固定顶头；不先作 gcd、原理想或行列式测试。若没有合格点，记录未返，不换素数或扩大候选表。

在唯一选中的点，首次计算两个完整模 $\lambda$ 多项式的真 Bézout，并返回所有系数；同时计算同一个固定 $12$ 阶矩阵的行变换，实际返回全部 $144$ 个乘积坐标与行列式。之后无论测试结果如何，都不换点。

若此行列式非零，则 (2) 为整数模型，故 (3) 在 QQ 上确实非零。只有此时可以登记
$$
F\ne0,\qquad F=0\ \text{是整个当前原图的纯权必要条件}.
\tag{7}
$$
若该点行列式为零或共同 $\lambda$ 因子非恒定，只记该点的真实返回；不推 $F$ 在 QQ 上恒零，也不推任何原权点排空。程序保留完整 $\lambda$ 多项式，不因已付物理 $\lambda$ 而擅自剥除模因子。

(7) 若完成，给新纯权代数支持；不是由单点满秩宣整个原图空。共同头零权纤维仍保留，没有新增它们的原值计算。

## 6. 首次身份与限额

源：

    2026-11-28-unit211-Phi-zero-corrected-two-sextics-fixed-lambda-resultant-support-8542.py

SHA256：

    39631a64da054107209d296765b755e2fe25a685f5734cb5607165dd39100b7b

总时限 $120$ 秒、内存 $1$ GiB、外层 $135$ 秒。两个必要定义前缀也受最初绝对截止限制；不重置或延长已用时间。

只输出已有输入 SHA、新整数尺度计数、固定度数上界、点表资格及小型模 Bézout/行列式回执。没有大型 QQ 行列式、系数文件或编码载荷。整个 $\Phi=0$ 与普通 ISP 均不能在本次实际返回之前预记完成。
