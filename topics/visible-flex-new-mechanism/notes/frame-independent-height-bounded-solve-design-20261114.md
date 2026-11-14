# 独立中心速度：一次有界直接度量求解的公开 Actions 设计

日期：2026-11-14。状态：**新 driver 与完整人工流程已核验，真实求解尚待部署**。

脚本 `scripts/frame_independent_height_solve.py` 使用已经冻结的 `frame_independent_height.py`。旧 frame/enriched/自然帽初态 runner 均不改写。这个新流程只允许一次有界非线性求解；其后的 g 冻结及各类加密均不再优化。

## 1. 为何选原 c0

修复后的完整公开 run `43616949465` 只评价两组已存参数，没有应用线性步长。来源输出为：

`notes/actions-43616949465-1-natural_body_initial/frame-natural-body-initial-audit.json.gz`。

其 121×768 固定状态直接实际度量诊断为：

| 起点 | 最大 operator 误差 | 直接 metric+shape 成本 | strip 最大归一值 |
|---|---:|---:|---:|
| 原 enriched c0 | `1.7279955895` | `0.07980369469` | `0.96124813` |
| 已公开饱和 c1 | `1.9096199884` | `0.08506546221` | `1.03064425` |

两者在该采样中最小面积都为 `.22`，`side*z−w` 最小为 0。因此此次选 c0 的 u/v、高度控制全 0、主体 metric 控制全 0；暂不新增有符号高度罚项，但始终报告真正坐标最小值和 signed-height。c0 的最大主曲率样本约 `60.13`，仍远未支付整体 reach；选择它不等于得到可行几何。

原 239 列未约束线性预测涉及约 `6.6e4` 的最大步长及接近零的奇异值，不能作为可应用进展。本流程不使用该步长，也不使用逐圈中心速度最小根来初始化。

## 2. 固定数学模型与 167 维状态

参数分为：

- u：原 81 列；
- v：原 72 列；
- 独立连续 b：9 列；
- 主体 a：5 列。

准确自然帽、原 c0 锚、全平热尺度 `tau0=1/128`、补丁宽 `1/10` 和平台 cutoff 都保持已经声明的定义。主体 a 控制只支持 `[t_c,t_f−1/10]`，不改变尾补丁的源半径。b 的一维控制支持 `[t_c,t_f]`，所有圈共用同一个 z 积分。

完整 canonical 状态保存准确 u/v/b 系数、完整 metric 的准确 family 与系数、核心/端口/帽、固定 b0 来源和源实现 SHA。浮点系数同时保存为 `Fraction.from_float` 的准确有理数和 binary64 数组。

默认参数界是：

\[
|u_j|,|v_j|\le8,\qquad |\gamma_j|\le1,
\qquad |c_j^{\rm metric}|\le1/2.
\]

它们是这一次工程搜索的明确边界，不是数学可行性界。原始系数如果不在严格内部，直接拒绝，不静默 clipping。

## 3. 初态先保存，再过评价门

默认主要评价为 GH64，b0 全角均值采用固定 384 角，与查询 θ 集合分离。主求解网格保持准确身份的 61 个非均匀径向层和 192 角，径向中心求积阶为 4。

完整自然初态报告已经显示 GH32/64 的高阶标量差很大，不能沿用旧的 scalar-s 门并宣称通过。新目标只使用实际位置及其一阶度量，因此工程门直接比较同一数学状态的：

\[
X,\quad X_t,\quad X_\theta,\quad E-1,
\quad\sqrt2 F/a.
\]

先分别进行：

1. GH64→128，固定 b0 的角均值规则和查询网格；
2. b0 均值 384→768，固定 GH64 和查询网格。

两次比较均须断言完整 canonical 身份与全部系数相同。每次上述五类量的最大绝对差必须不超过 `1e-4`，并且初始同网格直接 metric+shape 成本不超过 1，才进入求解。

X 的二jet、b0 的两阶导数和其他数值差仍原样保存；它们没有因为一阶门通过就获得连续曲率误差证书。门限只是防止评价误差主导这次优化的工程阈值。任一门失败时记录具体原因与初态，求解次数为 0，仍继续固定状态诊断。

## 4. 唯一的有界求解

目标为

\[
\frac1{2N}\sum\big((E-1)^2+2(F/a)^2\big)
\]

加来源中已经声明的 ball/strip 三项软约束：

\[
|X|^2/1.01^2-1,\qquad y/.38-1,
\qquad -y/.38-1,
\]

其平滑正部仍用共同权重 `2/sqrt(N)`。没有 R 项，也没有旧 height/ellipse 或新的 signed-height 罚项。所有实际几何诊断仍保留。

仅调用一次带准确 Jacobian 的 bounded `scipy.optimize.least_squares(method='trf')`，默认最多 250 次函数评价、600 秒求解 wall budget。只在已完成的参数评价边界检查时间；这个计算预算不是课题结束条件。

每 10 个新状态评价或 60 秒原子保存当前最好准确状态、同评价规则成本、历史和边界占用。报告包括各参数块距离界的最小距离及贴界数。没有将未约束线性预测步直接交给求解器。

优化期间 GH、b0 均值规则、查询网格、径向求积阶和目标权重保持固定。同一次下降只比较这些完全相同的评价条件。max-nfev 或 wall-budget 终止保留当前最好状态，并继续后面的冻结与审计；求解器的 success 标记也不代表题目完成。

## 5. 先冻结完整 g，再做三类独立精化

选中状态先用原主体度量 basis/准确系数冻结 g。代码断言冻结前后完整 canonical 物理状态相同，并在主网格逐项比较

`X, Xs, Xt, Xss, Xst, Xtt`。

随后只做固定状态评价：

- 121×384、121×768；后者只改变查询角数，固定 b0 角规则和 GH，记录所有公共点位置二jet差；
- 单独含 `t=0,t_c,t_f,L` 的全局高度锚 chart，核准确核心和一个共同帽高下的全部位置二jet；
- GH64→128，固定最终 g、全部系数、b0 均值和其他网格；
- b0 均值 384→768，固定 GH 与其他网格；
- 径向中心求积 8→12，固定前述两类角规则。

每项完成都会原子保存，避免只有最后一步才有回执。初态门失败也保留这些诊断，不能把失败误写成未运行的成功。

主曲率、面积、E/F/operator 误差、球/条带、真实三坐标范围及 `side*z−w` 都用实际重构的位置二jet计算，不借辅助 V 代替 Xs。径向分布使用新 driver 自己的明确 `data` API，不复用旧 R-distribution 的参数签名。

非有限曲率样本明确计数；忽略它们后得到的有限最大值不被说成全域有效。所有极值、精化差和端口数值比较均标为采样，完整嵌入与整体 reach 始终未获证明。

## 6. 人工流程覆盖

`notes/frame-independent-height-solve-check-20261114.json` 使用一个人工小椭圆，并直接调用与实际 main 相同的 `run_problem`。它覆盖：

- 人工放宽工程阈值，只为进入一个最多 2 nfev 的小型有界求解；
- 强制门拒绝分支，确认非线性调用次数为 0；
- 人工零 wall budget 异常分支，确认状态保存且后续审计完整完成；
- 同 g 冻结、所有最终分布/端口/角/GH/Nb/径向求积调用；
- 完整报告的 JSON 往返及 canonical 状态 hash。

人工门阈值放宽只存在于 `--check-only` 内，输出明确声明，不能当成真实初态已经过门。人工 2 nfev 的求解器正常以 max-evaluation 结束，不冒称已经收敛。全部位置二jet的冻结回放误差为 0。

这次覆盖实际 orchestrator 与最终 distribution 调用，是针对上一 initial-only runner 漏测 main 接口错误的具体修正；不是增加同实现的空泛测试数量。

## 7. 待部署命令

实际 main 强制检查本公开仓库 Actions 环境；输入必须在公开 topic notes，且只能重放原 enriched c0 来源。

```bash
python topics/visible-flex-new-mechanism/scripts/frame_independent_height_solve.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json \
  --out "$RUNNER_TEMP/frame-independent-height-bounded.json" \
  --height-free 9 --metric-free 5 \
  --heat-order 64 --height-angular-nodes 384 \
  --radial-nodes 61 --angular-nodes 192 --quadrature-order 4 \
  --uv-bound 8 --height-bound 1 --body-bound .5 \
  --max-nfev 250 --max-seconds 600 \
  --checkpoint-every 10 --checkpoint-seconds 60 \
  --evaluation-tolerance 1e-4 --initial-cost-max 1 \
  --audit-radial-nodes 121 --audit-angular-nodes 384 \
  --audit-quadrature-order 8 --refined-quadrature-order 12
```

这是新参数化的一次有界设计，不是旧固定 g 结果的简单迭代延长。若 g 被改变，只能在最终冻结以后讨论同 g 精化。整个流程没有给合格闭面、连续同 g 极限、宏观位移或 reach 的成功结论。
