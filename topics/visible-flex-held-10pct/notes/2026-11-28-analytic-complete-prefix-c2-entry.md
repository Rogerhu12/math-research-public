# R97 的完整真实来源前缀／切口 $C^2$ 消费入口

日期：2026-11-28。范围：新入口准备，**没有实际 fixed pair 数值返回**。

源为
[`qr_fixed_complete_prefix_c2.py`](../scripts/resume_20261128/analytic/qr_fixed_complete_prefix_c2.py)，
SHA256 `70069b8367d80063f3ef085d2e3a41e68c0cca7a6c85408bd3ab95cb18a03a86`。
它消费 [R97](../results/R97-complete-prefix-c2-in-common-physical-material-angle.md)
已证明的全部传递公式；纯界源保持
`f45298d263a09cca3b015b8f61fdfed2033167180867d667574cdd018cae560c` 不变。

## 真正允许的输入

右侧必须是真正已接受的 own QR fixed-g actual-DN 返回。左侧可以是同一完整固定
问题的另一 own 返回，或旧匿名 QR 分支的真正原锚及其 coupling summary。
当前新 mapped QR 主线使用 **own fixed1 → own fixed2**。新 mapped anchor-left
在没有其独立连续 provider 时明确拒绝，不能把它交给旧匿名 anchor 的
`CoupledContext` 冒名通过。

真实 pair gate 原样复用已发布
`tail/qr_fixed_complete_tail_c2.py`，SHA256
`1808a976bf4082fbe9b339fb24fdd7b87f3d29d36be05d15bcfdb7c7f24cc00e`，
其依赖版本为 `93d2b61d5cd8f413342f026e713c397ff3e5d10f`。
该 gate 会读取原锚，执行 `bootstrap/first_fixed_problem` 的原有限核心初始化，
以精确核对完整 frozen problem。这一既有身份核不是新 BVP、Jacobian、native tail、
mean 积分或完整真核心区间表重算，成本没有被隐去。

每场另给自己的完整 angular tables 和真实 cut report，逐一绑定：

- 当前 source run/raw/physical、最终 physical-H、完整 packet、runtime/baseline/port/native manifest；
- 同一个完整 $g$、同一 finite mean 节点数与 GL6、同一实际入口图/gauge；
- 全部 `rep.jets`、`lift_jets`、`chart_jets` 和各自原径向网格；
- 已完成真核心角区间表的全部 closed-box 三 jet；
- 完整切口模式并集、mean 零模及全部 outward coefficient intervals。

表的 true-oracle support 有理数列须等于实际返回的完整系数列。入口不读取浮点
`compensation_beta` 来替代真积分，也不从 sampled jets 构造连续界。

原 cut attempt 即使报告 metric unresolved，只要其完整 coefficient data 已真实构造
且全部来源身份成立，也可用于这个有限对比较。入口不将该状态改写成 metric
通过；它只证明自己的 $C^2$ 差上界，不额外制造一个接受门。

## 完整计算内容

共同径向分区是两边所有字面 Fraction 节点的精确并集，另加入同一 center/cut
repair 的连接点。每格将原两套共享二 jet quintic 限制到相同参数区间后相减，再
取 Bernstein 上界；全部 Fourier 模式和 mean 都保留。

核心部分使用 R97 的同材料逆角差、共同真实 $\beta$ 下的 $(1+\lambda)$ 相位界、
固定三重中心的 $44/35$ 位置传递。中心修补和完整 cut lift 逐项加入。
各场有限 $e(s)$ 的差及其一、二阶导数独立计算，完整逆角图两 jet 把同 $\psi$
差转成同物理 $(s,\theta)$ 差。所需角向下一阶界从各场自己的真 angular 表取出。

每格写入 `complete-common-spans.jsonl` 并 `fsync`，summary 保存累计六项界、
最坏格、角图差和完整来源。只有所有原共同区间精确单覆、末端到达真实物理端点、
全部当前输入和源码 SHA 再核一致后，才写
`complete_true_integral_prefix_cut_same_theta_finite_pair_certified`。

最终保留位置、一阶、二阶六项有理上界及梯度／Hessian Frobenius 上界的平方，
不把显示小数或浮点开方作为证书端点。两反射前缀具有相同范数界；完整尾、柱、帽、
规定 held-frame 变换和有限 Gauss mesh 查询另有明确范围，不能凭这个状态宣布全图
或无穷维 $C^2$ 收敛。

调用合同如下；变量须指向真正返回，不能构造替代输入：

```bash
python topics/visible-flex-held-10pct/scripts/resume_20261128/analytic/qr_fixed_complete_prefix_c2.py \
  --left-source-run "$PAIR_LEFT_RUN" \
  --right-source-run "$PAIR_RIGHT_RUN" \
  --left-tables "$PAIR_LEFT_TABLES" \
  --right-tables "$PAIR_RIGHT_TABLES" \
  --left-cut "$PAIR_LEFT_CUT" \
  --right-cut "$PAIR_RIGHT_CUT" \
  --outdir "$PAIR_NEW_OUTPUT"
```

旧匿名 QR anchor-left 还需 `--left-coupling-summary`；own/own 不提供该参数。
所有数组和逐格 journal 位于仓库外的新目录。

## 本次真实准备回执

最终源与 R97 pure helper 实际语法编译通过；当前 pair gate 的 11 条 reviewed-source
SHA 全部真实相等；最终源 `--help` 真 exit 0。该调用耗时
`0.7098319470005663` 秒、峰 `23040 KiB`。没有载入真实 fixed pair，没有运行
数值比较、BVP、native 或 J。

小回执在
`held10-analytic-work/complete-prefix-c2-final-preparation-20261128-a/preparation.json`；
对应仓内 JSON 保存完整事实。R97 早期符号检查记录中那个尚未冻结 CLI 的旧 SHA
仍保留原样，本条不回写它，也不把它宣称为这个最终来源的实际阳性。
