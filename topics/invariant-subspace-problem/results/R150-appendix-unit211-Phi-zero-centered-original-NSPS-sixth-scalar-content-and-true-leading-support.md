# Phi 斜率补图：完整 NS/PS 原六次标量、平凡 λ 内容及真实四十二次首项支持

> **2026-11-28 更正：本页经旧紧凑 R2 / Rbar 导出的原必要性、有限性、点数与排除声明已撤回。** 二重点一次坐标的平方被误写为 d1²，真实值为 2d0d1；完整更正和依赖边界见[原定义更正](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md). 已实跑的旧定义矩阵等式、次数与失败记录保留，不能再据此推原 Gram 条件或支付新模型单位。下文保留为原记录。


日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

本次唯一实际输入完整返回一个原 $I_6$ 标量 $C_6(u,Q,\lambda)$：其 $\lambda$ 次数恰为六，$\lambda$ 内容为 1；真实最高系数除去原已付单位后留下总次数 42 的完整权支持。全部原来源已经乘回。整斜率零图、整新首项零图与其它原点仍保留。

**后续范围提升：** 同一个六次标量的全部三原乘子已证明仅含旧权分母，现[覆盖整个当前 Phi 图](R150-appendix-unit211-Phi-zero-whole-original-NSPS-sixth-scalar-and-regular-three-source-extension.md)，包括斜率零集。本页保留其首次构造与真实首项；该提升不表示斜率零集或首项零集已排空。

## 1. 原范围与真正新增目标

沿已经完成的
[精确 I10 十八行两列呈示](R150-appendix-unit211-Phi-zero-complete-original-values-exact-eighteen-by-two-presentation.md)
及
[原 N1 斜率补图六行两列定理](R150-appendix-unit211-Phi-zero-original-N1-slope-exact-six-by-two-presentation-and-three-eighth-degree-scalars.md)，保当前原 $\Phi=0,D\ne0$ 图，并仅在明确的斜率 $\Delta_N\ne0$ 上使用两生成元坐标。整个 $\Delta_N=0$ 权面继续保留。

本次没有计算旧三个 $\lambda^8$ 标量，也不重新生成十八行的其余原值。只取已成完整 $N_S,P_S$ 的必要原定义，新增一个真实两列 cofactor、它的实际共同乘子取消、完整 $\lambda$ 内容及真实最高系数。无大投影、范数、Gaussian 或旧因式门。

## 2. 不增加单位的中心变化

原 N1 的线性余式为
$$
n=p_0+p_1T+p_2z,\qquad
p_0=e\lambda^2+f\lambda+g,\quad
p_1=a\lambda+b,\quad p_2=c\lambda+d,
$$
其中 $a,b,c,d,e,f,g$ 都是原权量，
$$
\Delta_N=ad-bc,\qquad \mathcal Z=aT+cz.
$$
置
$$
\mathcal X=\mathcal Z+e\lambda+f.
$$
这只是 $A[\lambda]$ 上的平移，不要求 $\lambda\ne0$。模 $n$ 的完整反解是
$$
T=\frac{(c\lambda+d)\mathcal X-de\lambda+cg-df}{\Delta_N},
$$
$$
z=\frac{-(a\lambda+b)\mathcal X+be\lambda+bf-ag}{\Delta_N}.
\tag{1}
$$
实际返回 $\mathcal Z=\mathcal X-e\lambda-f$、$n=0$ 的全部四个系数。特别是 (1) 每个系数对 $\lambda$ 次数至多一。

原首一关系 $\mathcal Z^2=\beta_1\mathcal Z+\beta_0$ 变为
$$
\mathcal X^2=(\beta_1+2h)\mathcal X+
(\beta_0-\beta_1h-h^2),\qquad h=e\lambda+f.
$$
两个新系数对 $\lambda$ 次数均至多二：原三个均值规则的列次数为 $(2,1,1)$，代入 (1) 后即得此上界。源码同时直接检查这两个真正系数。

已成完整 $N_S,P_S$ 的原 $(1,T,z)$ 行次数为 $(3,2,2)$。于是代入 (1)，它们的两个真实系数全部对 $\lambda$ 次数至多三。没有对高次幂反复代入；只在最后一次作坐标变化。

若原三系数行为 $r=(r_0,r_1,r_2)$，新的二系数行为 $(s_0,s_1)$，则
$$
r_0=s_0+s_1h+\kappa p_0,\quad
r_1=as_1+\kappa p_1,\quad
r_2=cs_1+\kappa p_2,\qquad
\kappa=(-cr_1+ar_2)/\Delta_N.
\tag{2}
$$
本次对 $N_S,P_S$ 都返回 (2)，因此仍是同一原理想中的实际来源。

## 3. 真正共乘子取消与完整标量来源

写新二行为 $N=(N_0,N_1)$、$P=(P_0,P_1)$。先以权量公分母 $L$ 清除 $N_1,P_1$ 的分母，构造真正多项式乘子
$$
\mu=LP_1,\qquad \nu=-LN_1.
$$
令 $g_c=\gcd(\mu,\nu)$，对两者逐项精确除法并乘回，得到
$\widehat\mu=\mu/g_c$、$\widehat\nu=\nu/g_c$。
随后直接核
$$
\widehat\mu N+\widehat\nu P=(C,0).
\tag{3}
$$
因此取消的是两个真实乘子的共同因子，且取消后的完整身份 (3) 在其零集上仍成立；没有将一个原方程任意除掉未知因子。

$C$ 的 $\lambda$ 次数至多六。清除它的真实权分母并仅剥已付权因子后，源码还把 (3) 接回 (2)，逐个返回全部三个原系数，得到
$$
\mu_*N_S+\nu_*P_S=C_*+\kappa_*n
 \pmod{(q_R,q_W,q_O)}.
\tag{4}
$$
从而 $C_*$ 是新的原 $I_6$ 标量，而不是只在某个泛型点上的必要值。

接着逐个真实 $\lambda$ 系数作 QQ 权多项式 gcd，精确返回
$$
C_*=\operatorname{cont}_{\lambda}(C_*)\,P_*.
$$
整个未知内容都保留。只有真实已付权因子可以删除。最高系数单独返回、剥已付权因子后保存其完整未付支持；它不自动是单位。本次实际 cofactor 非零，准确返回见下节；未知最高系数的零集没有据此删除。

## 4. 唯一实际结果与首一补图

记精确规范标量为 $C_6$。本次实际返回如下：

| 对象 | $(\deg_u,\deg_Q,\deg_\lambda)$ | 总次数 | 项数 |
|---|---:|---:|---:|
| $C_6$ | $(53,27,6)$ | 58 | 5716 |
| $[\lambda^6]C_6$ | $(48,26,0)$ | 52 | 742 |
| 剥原已付单位后的头 $H_{42}$ | $(39,22,0)$ | 42 | 540 |

精确 $C_6$ 定义 SHA256：
`f4ce16cd647975b8a431dabd5006289b475402096c92a2fb1c12897c4afd033c`。

真实最高系数 SHA256：
`f047ea501bc24863c7104b6ca60cdf58836819e6c959fec42edea1d2ffd358d6`。

整个未付 $H_{42}$ 定义 SHA256：
`1988b732b97dfdded9386c97d261774e6cc4d7e8db659f211faa54961c67a8e7`。

本次两个实际初始乘子的 gcd 是 1，没有非平凡公因子取消。$\lambda$ 系数的完整 QQ 权 gcd 也恰为 1；因此没有非平凡纯权内容需要分支，但不能据此排除多个系数在个别权点同时为零。

最高系数只剥 $u$ 一次、$u-1$ 两次、$Q$ 一次及 $\ell$ 的清分母分子三次，全部乘积返回。所有这些因子均为当前原图已经支付的单位。没有把 $H_{42}$ 称作单位或不可约因子，也没有删除它的任何零点。

在 $\Delta_NH_{42}\ne0$ 上，$C_6$ 可规范为真正首一 $\lambda^6$ 原关系。结合已经返回的首一 $\mathcal X^2$，每个固定原权对 $(u,Q)$ 的必要代数由
$$
\lambda^j,\quad \lambda^j\mathcal X,\qquad 0\le j<6
$$
生成，故长度至多 12，原 $(\lambda,T,z)$ 的不同点数也至多 12。这是指定首项补图上的有限性，不是全部权对有限，也不是整个 Phi 排空。

本次末两乘子恰好都返回为 QQ$[u,Q,\lambda]$ 多项式。但当前证明只使用已明确倒置 $\Delta_N$ 的原来源；它没有仅由这两个乘子是多项式就擅自把中间 $n$ 系数的分母删掉。整 $\Delta_N=0$ 的扩展需要另外付出真正全权来源。

## 5. 唯一执行与可再生定义

[实际小回执](../notes/2026-11-28-unit211-Phi-zero-centered-original-NSPS-cofactor-content-and-leading-support-8542-execution.json)记录本次返回的准确对象和范围。

- run `46091530208`，job `140813324185`；
- 冻结源提交 `d32b9f0a053a399d7cb24aeb03797ba74d474139`；
- 实际 pull：`2026-11-28T01:08:11.005732+00:00`，从上述提交到
  `67da4dbfe318d18b1bf92b4d37f803e456885fa5`，两份 README 无变化；
- 3.242041814 秒，51128 KiB，内层 exit 0；
- stdout 9455 字节，SHA256
  `7ab4d8220e924c6303c865d99f5b8577dbbe8fbd33c0f9d2799e692637bdc36b`。

2.155017017 秒时中心与首一二次的全部系数返回；
2.442265318 秒时 NS/PS 的完整两行及三原系数返回；
2.627129363 秒时真实共乘子 cofactor 返回；
3.205279590 秒时完整内容、首项和三原系数最终身份返回。原完整 Gram 必要前缀含 1536 个来源节点；没有执行其余 I10 四值或旧三个 $\lambda^8$ 标量。

实际源文件：
`2026-11-28-unit211-Phi-zero-centered-original-NSPS-cofactor-content-and-leading-support-8542.py`。

源 SHA256：
`baaac1d2cb05437b6c771856aea8991692cad5ff62276e6bce12584d15da8ca6`，
7915 字节。唯一直接依赖是 I10 源：

- `2026-11-28-unit211-Phi-zero-slope-full-original-values-twelve-new-rows-eighteen-two-model-8542.py`，
  SHA256 `527cddc0905e6ab51530b08172fc44c7652926e928de6769603e3a5d037c4c59`。
  可由 `ISP_PHI_I10_SOURCE` 指定。只读到第一次完整 Gram 记录之前的 7782 字节，
  前缀 SHA256 `e65ccba5fe91105a3d2c05d433a19d17b59761f6bc8d1cfffedda7e525f818aa`。
  不进入十二行的保存或其后四个新值条件。

其两件递归依赖保持原规范：

- `2026-11-28-unit211-Phi-zero-original-N1-slope-exact-six-by-two-mean-presentation-8542.py`，
  SHA256 `c4af169436165777186a811ccbea1b242b64e0bd84ac14bde43289254c4a2332`，
  由 `ISP_PHI_SLOPE_SOURCE` 指定，只用原 5809 字节坐标前缀；
- `2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py`，
  SHA256 `100ce4dfb7380da1591cd453aae392e2dafcaaceb3a601c4500d07852841ecaf`，
  由 `ISP_PHI_FIRST_HEAD_RULE_SOURCE` 指定，只用原 7097 字节规则前缀。

所有嵌套 alarm/setitimer 始终受最初的同一个 120 秒绝对截止约束。输出只含定义、次数、项数、SHA、完整乘回标记及真实执行身份，不存可重算系数、编码载荷或分片。
