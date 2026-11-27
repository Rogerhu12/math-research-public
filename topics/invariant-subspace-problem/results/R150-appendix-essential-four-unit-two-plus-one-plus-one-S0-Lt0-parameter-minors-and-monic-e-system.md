# R150：S0 / Lt0 的原四生成参数子式、整个 H9 零支及全局首一返回

- 日期：2026-11-27（台北时间，UTC+8）。会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro，分证及根会话复核。
- 范围：已登记各边界之外的原 S0 / Lt0 图；这里的参数始终为原 $(e,k)$，所有奇部仍使用同一 $\eta$。
- 结论：支付一个完整的 $H_{9,7}=0$ 边界，并从真实值列 $(\lambda,f,v,1)^t$ 得到 11 个非零原参数子式。结合已证 $F_{41,33}$ 与原 $G_{132,109}$，精确得到含 12 个非饱和生成元的三变量必要系统；所有除 $F$ 外的生成元均可无新增参数分母地降至 $\deg_e\le40$。
- 此稿不宣称一般 Lt0 已排空。下述 QQ 单位门已完成输入构造，完整结果待实际返回。

## 1. 沿用的原式和真实值列

前置结果为：

- `results/R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-five-quadrics-parameter-curve.md`；
- `results/R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-quadratic-head64-zero-exclusion.md`；
- `results/R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-four-generator-two-parameter-original-system.md`。

五个原二次式的已付局部化理想，已逐项验证等于六条“二次单项式减仿射式”的理想。六条规则使商模由 $(1,\lambda,f,v)$ 生成；这里不假定四生成元自由，也不假定任意参数点上的规则合流。

新源完整再生该结论：六条规则各自回乘至五个原式，并验证反向包含；每个待返回原式以第二层规则组合回乘，且每个组合系数分母均由已付单位组成。原同一 $\eta=n/d$ 的消元恒等式也逐式回乘。由此得到 15 行四列的参数矩阵 $R(e,k)$，满足

$$
R(e,k)(\lambda,f,v,1)^t=0.
$$

这 15 行为 9 个原三次重叠返回和全部 6 个剩余原输入：`U_moment, Nvalue, NB_even, NB_odd, PB_even, PB_odd`。常数坐标恒为 1；任何后续秩约束均施于这个真实非零列。

## 2. 完整支付公共因子 H9 的零支

把原 `N1elim, Qa` 对三个原均值式返回后的 $(\lambda v,fv,v^2)$ 系数记为两行。取第 1、3 列的二阶子式，清除并逐项回乘已付分母、已付因子后，得到原始不可约因子 $H=H_{9,7}(e,k)$。源码同时核验整个标量乘积，不把归一化常数悄然丢弃。

该 $H$ 有 54 项，双次数为 $(9,7)$，规范序列 SHA256 为

`6fe1d2d2f22082738cada074f04da6afbf0f578a4a254948064103bf1a0092d1`。

首先在 QQ 上计算完整原结式 $\operatorname{Res}_k(H,F)$。它为 386 次，完整精确剥除的已付部分是

$$
e^{24}(e-1)^{10}(e+1)^{123}(e-\tfrac12)^{53}.
$$

余下 176 次覆盖再精确分为 $(e^2+1)C_{174}(e)$；所有商乘回原结式。$C_{174}$ 的 SHA256 为

`67946c6ac8de028f04d6951e5e786a38ba2b19276c507412dfbeb189cb944135`。

令 $S(e)=\operatorname{Res}_k(H,G_{132,109})$，作为完整 QQ Sylvester 结式定义，模 1031 实算。两个输入的原 $k$ 次数 7 和 109 在模域完整保留，所得 $\bar S$ 为 1263 次。$C_{174}$ 的全部系数可在 1031 处约化，且其首项为单位、次数仍为 174。实际计算并回乘

$$
A\overline{C}_{174}+B\overline S=1,
\qquad (\deg A,\deg B)=(1262,173).
$$

两系数序列 SHA256 为

`0f3a82477f48dc8510c6c628c6ab6b455b2d94a50a4ca6ba98c7e4e93ff49ea7`。

这里的提升只用于这个完整一元 QQ 覆盖：若原 $C_{174},S$ 有共同复根，其共同最小多项式的首一版本在 $\mathbb Z_{(1031)}[e]$ 内，且约化仍有正次数；它会整除上述两个约化式，与实际 Bézout 等式矛盾。没有从多变量模单位推断 QQ 单位。

最后在整个二次域 $K=\mathbb Q[e]/(e^2+1)$ 内直接返回原 $H,F$，得到

$$
\gcd_{K[k]}(H,F)=k.
$$

9 次逆元、8 次除法和 1 条 Bézout 等式全部乘回。原物理单位 $k=Q/e\ne0$ 排除此整域，两个复嵌入同时保留。综上整个 $H=0$ 支排尽；原 $k$ 首项为零的纤维没有被除去。因此 $H$ 可加入已付单位。

## 3. 不除以 Cramer 行列式的 11 个参数必要式

从 15 行中选第 $(2,6,8)$ 行（零基编号），即

`cubic_overlap_1_2, cubic_overlap_3_4, cubic_overlap_4_5`。

将这三行重新编号为 $R_0,R_1,R_2$。记它们的前三列为 $A$，常数列为 $b$，$\delta=\det A$，并置

$$
C_{\rm raw}=\binom{-\operatorname{adj}(A)b}{\delta}.
$$

源码实际回乘全部 12 条 Cramer 系数恒等式。四分量的完整公共因子仅含下列已付因子（忽略非零有理内容）：

$$
h\in\mathbf Q^\times k^2(4e-k-4)H_{16,13}^{2}H_{9,7}.
$$

以下 $h$ 取源码实际逐次乘回的规范因子；精确剥除后定义 $C=C_{\rm raw}/h$。四分量双次数为

$(70,60),(71,61),(71,62),(69,60)$，项数为 $(2572,2636,2708,2567)$。源码核验四条完整乘回，并核验余下多项式公因子为常数；这一公因子事实没有被用于判空，也不意味着四分量没有共同零点。

对每一原返回行 $r$，取 $Q_r=rC$。其原组合身份逐个系数验证为

$$
\delta r-\sum_{j=0}^2\sum_{i=0}^2
 r_j\operatorname{adj}(A)_{ji}R_i
 =hQ_r(0,0,0,1).
$$

将这个等式施于真实列 $(\lambda,f,v,1)^t$，直接得到 $hQ_r=0$，故 $Q_r=0$。全程没有除 $\delta$，所有 $\delta=0$ 纤维均保留。

15 行中有 11 个非零 $Q_r$。对各式只精确剥除已付单位，剥除乘积逐一回乘。`cubic_overlap_1_3` 与 `cubic_overlap_1_4` 的规范式确为重复；`cubic_overlap_2_4` 与它不同，单独保留。再加上已证 $F$ 和完整原 $G$，共得到 12 个不同非饱和生成元。

## 4. 全局首一 F41 与无新增边界的降次

直接读取原 $F=F_{41,33}$ 的完整系数，得到

$$
\operatorname{lc}_e(F)=4503599627370496=2^{52}.
$$

故 $F_m=F/2^{52}$ 在整个参数平面上关于 $e$ 为 41 次首一式。对其余每个必要式 $p$，做精确除法并实际验证

$$
p=qF_m+r,\qquad\deg_e r<41.
$$

再以非零有理内容把 $r$ 规范为本原整数式，内容恒等式同样回乘。因此保留 $F$ 时，降次前后的参数理想相同；没有新增首项零纤维，也没有新增参数分母。

最终生成元规模如下。双次数均按 $(e,k)$ 计。

| 原输入 | 最终双次数 | 项数 |
|---|---:|---:|
| $F_{41,33}$ | (41,33) | 846 |
| 完整原 $G_{132,109}$ 的余式 | (40,126) | 4658 |
| cubic_overlap_0_1 | (40,61) | 1993 |
| cubic_overlap_0_3 | (40,65) | 2157 |
| cubic_overlap_1_3 | (40,65) | 2157 |
| cubic_overlap_2_4 | (40,65) | 2157 |
| U_moment | (40,66) | 2198 |
| Nvalue | (40,86) | 3018 |
| NB_even | (40,71) | 2403 |
| NB_odd | (40,95) | 3387 |
| PB_even | (40,74) | 2526 |
| PB_odd | (40,99) | 3551 |

## 5. 一次新的三变量 QQ 证书门及实际构造回执

新完整自含源：

`notes/2026-11-27-unit211-S0-Lt0-four-basis-monic-e-parameter-minors-safe-slimgb-QQ-8542.py`

- 源 SHA256：`d8dbf16c15ede8f33205b848889ce15a41f00a5aa57519292a31023b2c461907`；56315 字节。
- 实际参数：`--build-only`；exit 0；墙钟 79.611829 秒；峰值 RSS 155168 KiB。
- 标准输出：39340 字节；SHA256 `2be542bda6694cf68425bd96605007e06cf915f734a8cdd998237041c951a1e8`。
- 完整生成 Singular 输入：2896594 字节；SHA256 `cbc47d3ceabd1e650531f396797549f97addecf8a46830219c3165775fae43d7`。
- 小回执：`notes/2026-11-27-unit211-S0-Lt0-four-basis-monic-e-parameter-minors-build-execution-8542.json`。

必要系统在 $\mathbb Q[\mathrm{invUnit},k,e]$ 上，含上表 12 式及 $\mathrm{invUnit}\,S-1$。$S$ 恰是以下已付参数单位的乘积：

$$
e,k,j,x,ek-1,D_3,e+1,e-1,4e-k-4,4e-k,2e-1,
U,77e-16,\Omega,H_{6,4},H_{16,13},H_{9,7},B_{4,4}.
$$

其中 $j=k+2-2e$，$x=k+4$，$U=ek+2e-2$， $\Omega=2e^2-ek+2$；其余原因子按前置证书。没有饱和任何未付的 $\delta$ 因子。未加那些依赖 $\lambda,f,v$ 的物理单位只会放大必要系统，不会丢失原解；本稿没有把这个参数必要系统宣称为整个原系统的等价模型。

完整执行时，Python 先在独立 Singular 进程运行 `liftstd(...,"std")` 小单位检查，45 秒、8 GiB，必须同时通过真实 returncode、精确 marker、无 `?` 诊断。通过后才写出并运行完整 `liftstd(I,cert,"slimgb")`，1200 秒、8 GiB。只有实际返回 $\mathrm{matrix}(I)\,\mathrm{cert}=[1]$ 且 marker/exit/诊断均通过，才可登记一般图排空；超时、内存界或无单位均只记录真实负结果。

早先未做首一余式的 `...four-basis-two-parameter-minors-safe-slimgb-QQ-8542.py`（SHA `fc124775143c30f883d039f0d2c6f0d5a0f0c8907b293066a0ae0af7fe082028`）也只做过输入构造，未运行完整 QQ 门。它被本源取代，不安排两次同结论门。

## 6. 结论边界

已完成的是整个 $H_{9,7}=0$ 排除、原四列子式的逐系数组合身份、完整 $\delta=0$ 覆盖，以及保理想的全局首一压缩。一般 Lt0 的新三变量单位门尚待实际返回；普通 ISP 和 R150 总目标均未在此完成。


## 实际完整 QQ 门返回（2026-11-27）

run `45915323942` 的独立 std 检查通过；完整 slimgb 实际1200秒超时，仅有 BEGIN 标记，无返回基或单位乘回。driver墙钟 `1250.098953` 秒、峰值RSS `6473964` KiB、源exit1。原输入冻结，不提高时限重跑。完整源/输入/实际pull规则身份与小回执见[运行回执](../notes/2026-11-27-unit211-S0-Lt0-monic-e-parameter-minors-actual-QQ-timeout-8542.json)。

S0/Lt0随后由[独立完整原QQ覆盖证明](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-complete-original-cubic-cover-exclusion.md)关闭；该证明不依赖本次QQ门。取消请求曾被自动审批拒绝，故本次运行保留至上述自然超时，并未被手动取消。
