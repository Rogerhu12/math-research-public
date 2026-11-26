# R598 宽十八块与 prepared guide 的首次公开收据

日期：2026-11-26。会话：Astra-new-mechanism-0105020f-20261126。
状态：**实际公开数值记录；mass 阶段尚未进入，不能解释成原方程失败。**

本次新母的代数节点、正权、192阶完整固定积分与正平方 Gram 均实际构造。
新 prepared guide 用尽400 nfev，改善但未闭全部八矩；
其原 frame/位置预算也已实付。随后新 source 的矩阵编码调用出现
明确 broadcast 错误，故没有 mass 初始状态、Jacobian、信赖域试探或接受轨迹。
这不是数值根、秩证书或 README 完成。

全文仅从本 run 自然终态后的原 stdout 和已推源码解析；
没有本地求积、ODE、符号或优化，没有再读活日志，没有重跑旧科学。

## 1. 公开身份、源码与原输出

- [run 45828239888](https://github.com/Rogerhu12/math-research-public/actions/runs/45828239888)，attempt 1。
- [job 139937889703](https://github.com/Rogerhu12/math-research-public/actions/runs/45828239888/job/139937889703)。
- source commit：
  `92d261c4e239c4aa5e6cd59033d12c3f4e0087b2`。
- source：`scripts/r598_wide_mother_prepared_mass_bvp_agent.py`，
  42,519 bytes，SHA256
  `513290476ce4795e75b7d3802b2d94f906c55465cbaca59970eaf93b919146c0`。
- request：`computations/request-r598-wide-prepared-mass-bvp-20261126.json`，
  11,597 bytes，实际已推 SHA256
  `fd6f148820e9189fad8b60d83960d3a0782c16b4cd273e996a076a8ecb558fd4`。
  它已将 private_rules_read_commit 改为发布前实际读过的提交；
  不使用未推草稿的旧 request hash。
- workflow：`.github/workflows/visible-r598-wide-prepared-mass-bvp-20261126.yml`，
  3,494 bytes，SHA256
  `3024b45d8ffadecf6e9b31e80c689516da97f0ab4d76dacf654dbbf61796b349`。
- implementation note：
  `notes/2026-11-26-r598-prepared-wide-mother-original-mass-bvp-implementation-agent.md`，
  12,312 bytes，SHA256
  `56191054e6b927841e6db95610e30905ff7ee81d3b6cbb61ebfadf4fb394fde3`。
- 证明：`results/R598-three-rotations-wide-eighteen-block-mother.md`，
  14,481 bytes，SHA256
  `1f1e81e1779be336a88b3df7880d53c30c9342c93efae403e0acec141051a1f1`。

run/job 自然 completed/success 后完整 stdout 只取一次。
解码原文 **141,550 bytes**，SHA256：

```text
85ff477ffd81e30b8b8d02968d8343f578740692c4e93bb0f8f18392126101d9
```

scratch 原文：
`/tmp/r598-wide-run45828239888-job139937889703-decoded.log`。
共有11个结构化记录；无 accepted-state/trial 记录。
按根规矩15不提交原日志、系数表或轨迹数组。

## 2. actual pull 与全部实付时间

public actual pull 于 13:21:06.485903 UTC 完成，before/after
均为 source commit。根 README blob
`282e86b03385d3b6245ce7100ae2e2af7b103c2d`、
本课题 README blob `d0432faff569c8e9af7ed4809847e12880976c11`
均匹配、diff 为空。

private actual pull 于 13:21:10.747275 UTC 完成，before/after 为
`6e81dbdd10cf560abc5c68f69a620da0745e39bc`；
private 根 README blob
`5ba164843b1f5802184178a82d786264404873a3` 匹配，
QUEUE 当前课题唯一且仍为本会话进行中。不公开私库正文。

科学子进程实际起止：

```text
2026-11-26 13:21:24.392865 UTC
2026-11-26 13:21:54.339434 UTC
```

墙钟 **29.946569 秒**；main 自报 **28.74959921836853 秒**。
这些是两个口径，不能互相代替或都计一次。

| 项目 | 本次真实成本 |
|---|---:|
| 原十九行必要定义重建 | 9.068577766418457 秒 |
| 其中旧 formal-definition 部分 | 7.146933317184448 秒，已包含在上一项 |
| R598 80位代数图与正权 | 0.3260655403137207 秒 |
| 新192阶 fixed coefficients | 0.5210483074188232 秒 |
| 新正权 QR 因子 | 0.28053879737854004 秒 |
| 新 prepared guide 优化 | 14.414389610290527 秒 |
| guide nfev / 实际 residual calls | 400 / 8,916 |
| 单调 $c$ 根求解 / 其标量被积式评价 | 8,917 / 98,288 |
| 新 guide 原 frame/几何读出 | 0.09821319580078125 秒 |
| frame DOP853 nfev | 1,010 |
| 全部 guide geometry calls | 8,919 |
| 完整 coefficient value evaluations | 1,027 |
| coefficient jet evaluations | 0 |
| mass RHS / Jac / trial / accepted states | 全部0 |

分项有包含关系，不机械相加。
实际 scientific interpreter 为 Python3.12.14；
numpy2.3.5、scipy1.17.0、mpmath1.3.0、sympy1.14.0。
wrapper 已在科学前移除凭据，15个源/证明/note/workflow hash 匹配。
只有一个公开 job，无 artifacts、缓存、Release 或 job git 写入。

## 3. 新母与新固定表的实付读出

实际18块、576微包、三旋转、半宽 $1/12000$、
实际幅 $(2w)^{1/4}\varepsilon^{7/4}/256$ 与窗口 $[4,6]$
均按 R598 生成。80位代数图打印的最小中心间距为

```text
0.01196833602302861736897578533385433509785813570737
```

相应十次矩最大数值误差为
$3.16265938297\cdot10^{-81}$。
这符合已付有理间距 $>319/30000$；实际几何的证明继续用 R598，
不以这个浮点数替代。

三组权均严格正；$\tau=-1$ 的右端权、$\tau=1$ 的左端权
实际为 $1/36$ 的数值表示。
源以新 $\tau=0$ 的六参考块、总四次质量6、每块权 $w$
评价全部18个真实块；没有把旧36块数值表当新表。

新表用339个 profile moments / 4,642个 geometry monomials，
order=192、gap_order=8，SHA256：

```text
e36fd88a6c347dd427b49a9511902a68903feb7c9200967b682c07e22d230b84
```

正 Gram 因子为36,096正行、18列，不截秩；
列单位范围
$[4.535412491547372\cdot10^{-7},\,38016256.29554514]$，
normalized-Gram 最大绝对 QR 缺陷
$9.146329527087715\cdot10^{-16}$。
本次未做候选专属求积加密，因尚无候选根；
这些数值不被称为严格原积分证书。

## 4. 新 prepared guide：参数与全部八矩

优化达到 max_nfev=400，status0，success=false。
找到 sampled feasible guide，实际11参数为

```json
[0.9814869366977396,-0.5245685552774372,1.584058067848438,
 -1.3124986482926952,-1.0349903056614995,
 1.0039495529332485,0.35561151877897246,-0.08606876424154568,
 0.03597506392470256,-0.26051011522776046,7.481421292452849]
```

即源码的 $(a_0,\ldots,a_4,b_1,\ldots,b_5,L)$；
单调积分选择的实际固定 $c=-0.36297895632208516$。
prepared 中心 $(p_0,p_2,r_0,s_1)$ 为

```json
[0.027303671786739814,0,0.007971806526575014,0.013651835893369907]
```

七个 weighted 原目标与三项盒罚的最终打印值为

```json
[-0.003223161667870999,0.005489079591850426,
 -0.0002655009105879576,-0.0011829390595825308,
 -0.006954827419432626,-0.01997990580453521,0.011294204631206598,
 0,0,0]
```

真正全部八个513节点末矩按
$(p_0,p_1,p_2,t_1,r_1,s_1,s_0,r_0)$ 的顺序为

```json
[-0.012056909997267745,0.041066059574522355,
 1.6650790220737161e-9,-0.00024827618072577865,
 -0.0011062723251786613,-0.013008004364442226,
 -0.037369565580437726,0.010562102573417154]
```

最大约 $0.041066059574522355$，未闭。
$p_2$ 保留实际 $1.6650790220737161\cdot10^{-9}$，
没有因其连续单调定义而在数值输出里手动置0。

原 sampled geometry 范围：

| 变量 | 最小 | 最大 |
|---|---:|---:|
| $h$ | .9455299288176235 | 2.897626249782836 |
| $k$ | -1.6710667262926244 | 1.6980930722536616 |
| $\eta$ | -.7761865075718921 | .35420169931382073 |
| $\gamma$ | -3.162449560481358 | 2.9498080949584806 |
| $\upsilon$ | -1.4454434884188625 | 1.4478191977329236 |

$\eta$ 的累计求积和这些采样值不授全域严格盒证书。
该 guide 是新真实运动学初猜，尚未满足 ruling，
也没有通过这次操作产生一个准确有限路径。

## 5. 已实际支付的空间范围与第一曲率变分

源沿上述同一 guide 的 $h,k$ 实际积分原 frame / $\alpha$ ODE，
再读两侧 $y=4,6$ 的 collar 边界。结果：

| 读出 | 实际值 |
|---|---:|
| 采样原边界直径下界 | 31.438695000042266 |
| 采样原 collar 主曲率绝对值最大 | 1.1580146370971414 |
| 相应局部 focal cap | .8635469431601959 |
| cap / 采样直径 | .027467645942652358 |
| 两个原 pose 读出 | $(-.4730572845640886,\ 15.502118764024493)$ |

这里的 $.02747<.03$ 是**这条实际 guide 的必要预算失利**：
假设后来的嵌入面保留这些原 collar 点，其 reach 至多受该局部曲率限制，
直径至少包含这些点。当前仍只是浮点采样；它不是严格连续不可能性证书，
更不是 reach 下界。不能从这一个 guide 推断 R598 母或任何后续
改变的实际路径都失败。

全部18块真实位置/幅的中心第一场与准确法曲率一阶变分采样为：

| profile | 第一场范数峰值 | $|n(Y_f)_{uu}|$ 峰值 |
|---|---:|---:|
| $f$ | .000010574925563726618 | 137169691.7488228 |
| $g$ | .00001057493429722344 | 137146093.68308365 |

变分用 R598 的准确式
$\,n(Y_f)_{uu}=-z^3\sqrt Q\,f'''/(2h^2)$。
它显示本新母的真实二 jet 成本仍大；不能只凭半宽扩大就宣称有宏观可见解。
同样不能把一阶变分乘任意大幅度而冒作非线性有限族的真实曲率。

## 6. 机械失败发生在哪里，哪些 history 已计算

原错误精确为

```text
ValueError: operands could not be broadcast together with shapes (5,513) (5,)
```

新 `make_seed` 调用旧 `FiniteCoordinates.encode(geometry)` 时，
`geometry` 是5乘513整阵；旧 encoder 是单列5向量接口，
其 `shifted / limits` 中 `limits` 的形状是(5,)。
这是新调用者的接口错误。明确修复是逐列调用同一个旧 encoder，
不改 arctan 物理图或任何原方程。

根据已推源码的执行顺序和实际1,027次 coefficient value 计数：

1. 同一新 guide 的513节点真实 $A(x)$ 已由原 $M$ 完整积分到末端。
   它是中间数组，未序列化；上述末八矩是前面的完整公开读出。
2. 两侧513点共1,026次 coefficient value 评价已完成，
   以及相应正能量配对；此后又做了1次 center coefficient 评价。
   初始化父类另有1次参考能量单位的值评价。
3. 真 guide 的 energy 最大值、中心 $\zeta_0$ 已在内存计算，
   但 `R598_TRUE_PREPARED_SEED` 尚未发出，因此**数值未知**；
   不从旧母、纸面尺度或未输出数组补造它们。
4. 错误发生在 state[:5] 编码。后面的双侧 $\rho$ 预积分循环、
   两个常数 gauge 的全 guide LS、完整 seed 输出与 guard 单位冻结
   **均尚未开始/完成到可报告状态**。具体地 $\rho$ 积分代码在出错语句之后，
   本次没有实际运行该循环，不能称“完整第三 history 已走完”。
5. 尚未调用任何 mass RHS 或31变量 Jac，没有配点初始 current，
   没有线性试探、接受状态、物理 Hermite 读出或细化。

因此这份收据保留全部已付成本，但不把“wrapper success”
写成求解成功，也不把这个 shape bug 当成路线、原公式或物理盒的障碍。
有限搜索 guard 根本未进入；本次故障不能归咎于其阈值。

## 7. 后继允许继承的内容

已付新代数图/192表的**定义与hash**、以上11个真实 guide 参数和
$c$ 可作为明确新 request 的小输入；原数组不入库。
若继续同一个 guide，须标清这只是补做尚未进入的 history/mass 阶段，
不得再从原初猜重复400nfev。
若采用额外真实中心 jet 条件 $h_{ss}(0)=H$，那是有数学理由的新
初猜问题，应从这11个已付参数出发、保留其来源，并另计真实优化成本。

下一实际源会逐列编码，并继续完整 positive square、同一固定
$\chi$、两侧原 ruling、全部19微分/29边界与原空间范围。
本收据未将新 jet、八矩、pose 或主几何门写成已完成。

