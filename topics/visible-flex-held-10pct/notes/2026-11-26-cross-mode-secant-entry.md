# 跨 M 原 R53 割线初猜：独立入口与执行范围

日期：2026-11-26。会话：Astra-held10-06bbeb39-20261126。

新增独立文件
`scripts/resume_20261126/material_design_cross_mode_secant_predictor.py`。
它不修改现有 predictor、controller、CI 或原求解器。输入是两份真正接受的
原 portable/R53 线性-DN 设计场；左 M 严格小于右 M，且
\(0<\lambda_L<\lambda_R<\lambda_*\le1\)。
输出只有库外的 `initial.npz` 与 `predictor.json`，明确均未接受。

## 来源、坐标和完整 lift

入口分别调用原 `material_design_secant_predictor.accepted_original`，
保其全部真实 solver/RMS/BC/metric、raw/physical、源码和输入 SHA 检查。
共同 profile 基值、尾物理参数/cut、角图、gauge、warp、源码、门和 R53 设置
仍须相同；R53 设置只允许 λ 不同。M、angular、pscale 长度、端口分辨率和
各自真实 mean 另行明确记录，不能把左源改写成一份 M40 接受记录。

用原 `actual_m3_metric_model.load_model` 重建左源；再用该同一已安装
R53 factory/exact-lift 的类、左 cfg/λ/δ、右实际 M/角分辨率/port 构造左升阶模型。
右 port 的全部物理 parameters/cut 必须与左相同。首参数仍是原加性 δ，
高项仍是 normal-angle support 坐标，**不是 v5 phase 参数**。

复用原 `prepare_lifted_mode_restart.embed/lift_weights`，定义

\[
p_{L,0}^{\uparrow}=p_{L,0},\qquad
p_{L,j}^{\uparrow}=p_{L,j}\,\mathrm{scale}_{L,j}/
 \mathrm{scale}_{R,j},
\]

新增高 support 项为零。实际旧/新完整 support 向量及尺度仅记录 SHA/shape，
公共项的浮点 roundtrip 差记录 \(\ell^1,\ell^\infty\) 和逐位相等标量，
不新设“必须 1ulp 内逐位相同”的停止门。

若 \(\Delta I=I_{\rm new,L}-\operatorname{embed}I_{\rm old,L}\)，则

\[
Y_L^\uparrow(t)=\operatorname{embed}Y_L(t)
 +a_L(s_L(t))\chi_L(s_L(t))\,\Delta I.
\]

系数是1。程序核 left old/new 的 literal chart_join/reference_prefix/breaks
以及查询网格上的 \(s,ds\) 相同；始终用左自己的 δ 和 \(s_L(t)\)，不使用右
物理坐标替左查询。沿原 transfer 的径向样点、角规则及 \(10^{-7}\) 门，
对左已保存 physical quintic 做相同的完整参考位置/两jet有限检查。
所报 raw 参考六jet与原脚本一样省略共同 mean-height 项。保左源 literal mean
及 primitive 起点只是同参考重建条件；这里没有实算新的 mean integral，
没有认证完整 Cartesian 误差，也不产生新的 accepted interpolant。

## 共同网格上的预测

分别使用两端保存的原 computational-t cubic。左 cubic 的值再加上述完整 lift，
不对新左节点拟合 cubic；右端原 cubic 直接评价。公共网格取两端 t 并集；
若超过真实右端原 max_nodes，则沿既有策略退到右端原网格，不降低右端 M、
角分辨率、目标或求解预算。

\[
\beta=\frac{\lambda_*-\lambda_R}{\lambda_R-\lambda_L},\qquad
Y_*=Y_R+\beta(Y_R-Y_L^\uparrow),\qquad
p_*=p_R+\beta(p_R-p_L^\uparrow).
\]

mean1552 与 mean1936 各保真实来源，lift 的参考检查仍对应左原 mean。
上述只是完整**求解状态**的 design 初猜，不是同 g 精化，也没有插入独立
可调平均高度。目标 mean 必须由新目标场按原规则重新构造和审计。
原 raw cubic 与 physical quintic 没有被混称逐字同一函数。

原 `portable_prefix_continue.py` 已能从 x/y/p/pscale 消费该输出。所有后续
initial-domain、实际 BVP/RMS、BC、完整 metric 门仍须真跑。割线不自动保持
目标非线性 inlet 或几何域，也不保证可解。低 M 误差会进入差商；未建立
forward-error 界，不能拿已通过的 RMS 当作状态误差来担保预测。

## 调用合同

`predict(repo, left_path, right_path, target, outdir)` 供只读接口核对；
实际使用应每次以独立 CLI 进程调用，因为原 geometry loader 安装全局类：

~~~bash
python material_design_cross_mode_secant_predictor.py \
  --repo REPOSITORY \
  --left-run ACTUAL_LOWER_M_RUN \
  --right-run ACTUAL_HIGHER_M_RUN \
  --target-lambda TARGET \
  --outdir NEW_OUTSIDE_REPOSITORY_DIRECTORY
~~~

当前准备针对同一 material VM 的 secant attempt-000
(.032/M32/866节点) 与 attempt-002 (.064/M40/889节点)，不能替换成另一
design VM 的 .032 场，也不能用中间 metric-only attempt-001 当接受锚。
本次没有读取或生成这两实际场的新预测；下一实际目标由真实续入状态决定。

## 本次实际本地检查与 SHA

compile 和 `--help` 均真实退出0。附独立小核
`check_cross_mode_secant_algebra.py` 只用合成 M2→M4、多项式与非平凡径向图，
没有调用 BVP/DN，也没有伪造接受记录：

- 独立显式三块嵌入与新 evaluator 的差为0；
- 完整参考 lift 抵消误差 \(6.938893903907228\times10^{-17}\)；
- 故意使用另一 δ 的右径向图会产生约0.130127的状态差，实际被坐标门拒绝。

实际标量记录在
`notes/2026-11-26-cross-mode-secant-source-checks.json`。
独立窄源码审查未发现此次模型/参数/来源接口阻断；这不代替真实输入执行。

| 文件 | SHA-256 |
|---|---|
| 新 material_design_cross_mode_secant_predictor.py | 79ebe59d041a4c9f600345890875237f2b222f8301b8c736c586ab0884ecaae9 |
| 新 check_cross_mode_secant_algebra.py | ab2f69f5701130b9147efea79b2d5859e1c36c958f4e8a700dfab63dcdcdb060 |
| 新 source-checks.json | 117fa69463d9eca5672f8354cd10def8c43efedc1beb419eeb6dad5d16dc900d |
| 原 material_design_secant_predictor.py | 60877969b981712f6d8c00219ae9eeb02f1e432b41cda4c96159a5b5a50d63bf |
| 原 prepare_lifted_mode_restart.py | c1f7741ee1882bd8413a04f280df759da4165792291f5419b243b7deed2882fe |
| 原 actual_m3_metric_model.py | 0b1dd3e35be3cc51f27a5f1a3fe5437904fa8363ef8bfcdf2d40547c0a860ba8 |
