# 恒周长椭圆延续：公开 Actions 的下一实际设计搜索

**状态：已实现驱动，未在本地运行非线性延续。** 这次参数选择依据 `core-tail-inward-actions-audit-20261114.md` 的真实 B/C 失败数据：大内部度量误差、过低平盘高度和高曲率。完成标准未达到。

## 1. 每一阶段改变什么

固定目标物理椭圆半轴 $(1,.3)$ 对应的周长半径
$$a_0=2\operatorname E(.91)/\pi=.6980392675284104\ldots.$$
设计路径为
$$q(t)=\exp\{t\log(1/.3)\},\qquad
A(t)=\frac{a_0\pi}{2\operatorname E(1-q(t)^{-2})},\quad B(t)=A(t)/q(t).$$
它从半径 $a_0$ 的圆到半轴 $(1,.3)$ 的椭圆，始终保持准确周长 $2\pi a_0$。圆参考、连接长度、径向基底、圆尾半径和角模式范围在一个 lane 内保持相同。每次仅改变入口的准确椭圆 jets，再由前一实际候选的自由系数开始求解。

现有 `core_to_tail_bvp.py --warm` 已支持保存 JSON 的系数。相同基底时直接恢复同一函数，基底变化时执行已有的明确投影。驱动 `scripts/ellipse_core_continuation.py` 调用这个接口，不另造隐含的圆化或按截面重置中心。

每个阶段仍允许设计径向度量，因此整个路径是**设计延续**，不是本课题要求的固定共同度量加密序列。即使设计走到 $t=1$，仍要冻结那一个度量，完成误差收敛、闭合、全像集位移与 reach 检查。

## 2. 参考选择与高度约束

两个 lane 使用 `unit` 圆参考与 `beta_wiggle=.8`。它们有小幅的外扩和一个内部环向法曲率零点，区别于把半径推到约 $1.5$ 的旧负角回折。这里不声称一个零点自动解除一般刚性。

| 开发级参考检查 | L10 | L11 |
|---|---:|---:|
| 核心柱高 $h_0$ | .23 | .25 |
| 连接长度 | 1.0 | 1.1 |
| 最大圆参考半径 | .78769182 | .82710357 |
| 最终参考高度 | .56758141 | .67115202 |
| 最大参考高度 | .71419264 | .79802000 |
| 参考最大主曲率样本 | 9.69269 | 8.78856 |
| 参考到原点最大距离样本 | 1.01894 | 1.10057 |
| 目标椭圆至参考尾的最大对应弦长样本 | .79521142 | .83412770 |
| 非线性求解前准确圆控制的度量误差 | $9.34\times10^{-14}$ | $2.77\times10^{-13}$ |

尾切口半径为 $.28$，平区域外半径 $.26$，内切口 $.23$。尾高度下界分别设为 $.299$、$.319$，按 R4 的实际椭圆柱和平盘法球几何给出；上界为 $1.05$。这是一个主动限定的搜索子族，不能当成所有可能轴偏移方案的必要条件。

所有表项都属于初始圆参考或端口几何。它们不证明真实非轴 field 的相同界，也没有把半带直径当成整个闭曲面的 $D$。两份 `ellipse-L10-plan-summary.json`、`ellipse-L11-plan-summary.json` 由 `--plan-only` 生成，含源文件哈希和准确命令；没有调用最小二乘。

## 3. 驱动行为

默认使用 9 个径向自由基、12 个角模、96 个角点及每径向区间 6 个 Gauss 点。先求 $t=0$ 圆控制，随后尝试 $\Delta t=.125$；细网格度量误差不超过 $10^{-4}$ 且端口 jets 与正则性检查通过时才接受并更新 warm 候选。失败时从上一个已接受候选重新尝试半步，最小步为 $1/128$，最多 40 次设计尝试。成功后可恢复较大步长。

该 $10^{-4}$ 是**设计阶段接受门**，高于本题最终 $10^{-6}$ 门；汇总里始终写明 `task_complete=false`。若某分支只能维持极小非圆幅度，驱动会如实保存停滞位置和全部失败记录，不把它们当目标解。

每次尝试后原子更新 summary JSON。可用 `--warm-json` 从同周长且满足当前设计接受门的已保存椭圆阶段继续；这个入口会检查 profile 类型、周长和轴比范围。它不把其他度量或其他尺度的文件静默当作同一个问题。

## 4. 两条 Actions 命令

将输出目录换成该 lane 的 artifact 目录。

```bash
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/ellipse_core_continuation.py \
  --length 1.0 --h0 .23 --beta-wiggle .8 --radial-free 9 --modes 12 \
  --accept-metric 1e-4 --initial-step .125 --min-step .0078125 --max-attempts 40 \
  --max-nfev 250 --out-dir "$RUN_DIR" --prefix ellipse-L10

OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/ellipse_core_continuation.py \
  --length 1.1 --h0 .25 --beta-wiggle .8 --radial-free 9 --modes 12 \
  --accept-metric 1e-4 --initial-step .125 --min-step .0078125 --max-attempts 40 \
  --max-nfev 250 --out-dir "$RUN_DIR" --prefix ellipse-L11
```

`--plan-only` 只作约几秒的圆控制、参考几何与命令生成；此次仅运行了该模式。后续对实际结果按完整 $E/F/G$、真实尾中心、主曲率和全像集包络重新审计，不能由本表代替。
