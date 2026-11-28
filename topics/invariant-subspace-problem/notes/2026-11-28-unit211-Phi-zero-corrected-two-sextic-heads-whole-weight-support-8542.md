# 正确 Phi 两条原六次的完整 QQ 首项共同权支持：新输入

日期：2026-11-28（Asia/Taipei）。这是尚未运行的新目标，不能预记头互素、全图首一性或排空。

## 1. 已成原来源

[正确整个原 I6 的十五列三坐标呈示](../results/R150-appendix-unit211-Phi-zero-corrected-whole-original-I6-fifteen-by-three-and-two-sextics.md) 的唯一实际 run 46130918529 返回两条原必要六次：
$$
C_{\rm NP},\ C_{\rm ov}\in I_6,\qquad
\deg_\lambda C_{\rm NP}=\deg_\lambda C_{\rm ov}=6.
$$
它们是在正确 $\Phi=0$、物理 $D\ne0$ 图，沿完整 $A=0,B=0$ 原排除支付三均值头后得到。原纯权系数环仅倒
$$
Q(1-Q)(u-1)KLM_nAB.
$$
不倒旧斜率、任一新六次首项或原 $D$ 范数。

原两个多项式的 SHA256 分别为：

    fcf79be98410a2eea2ebdb588b441b8f4aceb20acb4704a96ee34fc0012d01d5
    2407107501f1790a288ecabd75f14f92c7602859bfc033727b76312675f91014

两个真正首项
$$
h_{\rm NP}=[\lambda^6]C_{\rm NP},\qquad
h_{\rm ov}=[\lambda^6]C_{\rm ov}
$$
的 SHA256 分别为：

    63c05c345cbc7055d652d46c173684bd7fdb159db3741232ef94d6cb58992bf6
    9794fac2ee8bf7de08d80b9f3102480f1d06c9cfb4ff8be3981817dcfbd682fb

已知双次数、总次数、项数分别为 $(37,21),41,471$ 与 $(24,15),27,230$。这些只识别已有输入，不把非零首项冒称物理单位。

## 2. 必要定义前缀与不重放范围

唯一数学源读取下列两个既有文件：

    2026-11-28-unit211-Phi-zero-corrected-whole-original-I6-fifteen-by-three-8542.py
    2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py

第一文件 SHA256：

    84e0efcc19a0274d571484b187b7b155c81ebf255e40a39c38ac13a03f911cf0

第二文件 SHA256：

    5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7

新源只取第一文件在 seeds 定义以前的 $12067$ 字节，SHA256：

    e2e9bab84bca700400c8e26d5787208c9aceafe27c64aa7ecf828b0552025a1f

第一文件内部只需第二文件原 $4007$ 字节的正确四式定义。新 AST 明确保留创建四条原系数行的定义循环，省去其它旧顶层动作、overlap、矩阵缺陷、NSPS 末审核循环与 say/assert，也省去仅服务这些旧门的 AA/BB 等定义；函数内部必要原系数运算检查不改。旧源字节保持不变。

完整 N4/P2 三系数仅作为已成六次的必要参数定义再生；不重跑十五列稳定呈示或旧两 cofactor 的三坐标证书。新源按已刊三个实际乘子的公内容公式，只计算其已知标量坐标，核上述四个参数 SHA。所有省去的顶层行号明确打印。

这种参数定义再生不是新成果，不重新登记旧原式、动作或 cofactor。

## 3. 真正新增的因式与共同支持

分别仅剥原已付纯权因子，并完整乘回
$$
h_i=U_iH_i,\qquad U_i\text{ 在当前图已付为单位}.
$$
对 $H_i$ 首次进行完整 QQ 因式分解，返回全部因子乘积；每个未付因子的整个零集保持。

然后新算
$$
g=\gcd_{\mathbb Q[u,Q]}(H_{\rm NP},H_{\rm ov}),\qquad
H_{\rm NP}=gA_1,\quad H_{\rm ov}=gA_2
$$
并精确返回两个商和全部乘积。$g$ 也作完整 QQ 因式分类。所有内容及因子都只按其实际结果登记。

这里不从二元 gcd 为 $1$ 推原理想为单位：

- 若某个 $H_i$ 实为非零常数，只有这时该真实六次在整个当前已付权环上首一化，给尚未反演几何 $D$ 的必要原 I6 代数统一十八生成元。
- 若两个 $H_i$ 非常数而 $g=1$，仅说明两个头共同零的权支持有限，其不同复权点和未局部化平面交的长度均至多 $\deg H_{\rm NP}\deg H_{\rm ov}$。
- 若 $g$ 非常数，完整曲线 $g=0$ 全部保留；其外共同头零点至多 $\deg A_1\deg A_2$。两余商互素来自完整 gcd，不据此排除曲线或原点。
- 在两个原头的并开集，已刊十八生成结论继续有效。不得把有限权支持自动变成这些特殊权处的有限 lambda 纤维。

本门没有对原 C6 的固定 lambda 结果式、全部原值理想或特殊头零纤维作新空性测试。原 $D\ne0$ 开集不被冒称同一权环上的有限模。

## 4. 首次执行身份与边界

新源：

    2026-11-28-unit211-Phi-zero-corrected-two-sextic-heads-whole-weight-support-8542.py

SHA256：

    fbe5c3060172c415d15f7c582bedd055a8acce8bd760fccd5a4c2d3b3161caae

120 秒、1 GiB，总截止包含两个嵌套必要前缀；外驱动135秒。每个首项因式完成后立即给小 checkpoint；无大系数、载荷、编码片或缓存输出。

未执行之前，当前结论仍只是已刊两头并开集的十八生成元与所有共同头零纤维保留，不预报全 Phi 有限或空。
