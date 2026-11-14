# R28 冻结候选的只读残差分布审计器

2026-11-14。独立脚本：`../scripts/frame_collar_residual_audit.py`。它不优化、不改变参数或参考度量；实际研究候选只在公开仓库 Actions 评价。本地执行仅限内置温和人工输入的开发检查。

## 1. 从原报告重建同一个对象

输入是 `frame_collar_bvp.py` 的完整最终报告或 checkpoint。审计器依次核对：

- 原报告记录的 `frame_collar_bvp.py`、`ellipse_frame_port.py`、`cosine_connector_radial_seed.py` 三个 SHA256 与当前运行实现逐一相同；不以新实现悄悄重算旧定义。
- 准确核心、侧号和端口身份的 JSON SHA256，以及 CLI 参数和这些准确身份的一致性。
- 每个场系数的有理数字符串准确等于其 binary64 值，同时与原报告浮点系数数组逐位相同。任意不可准确回转的有理数会被拒绝，不能舍入成一个新模型。
- 径向 seed 完整准确身份、S5/S11 段配置、原 metric 数学定义及其 hash。若原报告来自度量设计，这里只冻结回放其实际系数，不再设计。重建后的 metric 完整数学字典必须与原件相同。

输出另记录原文件 SHA256、原 Actions commit/run ID，以及包含场定义、准确系数、度量身份和三个实现 SHA256 的冻结状态 hash。数值评价可能有舍入误差；这套身份核验不把浮点评价称作准确几何证书。

当前 adapter 针对准确椭圆柱端口。它不从一般余弦曲线的坐标采样重新拟合一个椭圆，也不把未受支持的旧 metric basis 自动换成新 basis。

## 2. 报告哪些分布

使用 R28 原重构函数，在每个径向行记录：

- 全材料角上的 \(|R|\)、\(R\cdot T\)、\(R\cdot V\)、\(R\cdot(T\times V)\) 的极值及其材料角；另记三个分量的角平均与 \(|R|\) 的角 RMS。
- 真正诱导的相对度量算子误差、\(E-1,F/a,G/a^2-1\)、最小面积、主曲率绝对值、椭圆投影半径平方及 \(\min(\sigma X_z)-w\) 的极值位置。
- 每行真实三坐标范围、中心高度、目标 \(a,a',K\)，以及残差三个标架分量的有限角 Fourier 系数模长。

所有极值都给出物理径向位置 \(t\)、材料角 \(\theta\) 及网格指标。全域最大项还附该点坐标和三个标架残差分量。角平均没有单独的角位置，故对应 `theta`、`angular_index` 明确为 null。

分区采用准确 seed 的五个区间：开放核心、第一 S5、负 K 的第二 S5、末 S11（或输入明定的旧 S5）、开放平领。为了完整覆盖接缝，两相邻分区可以共同含边界行；没有由不同分区名称重复计算一个新几何点。表中的 `R_T_mean_extreme` 用于辨认先前尾部平均阶数失配是否仍表现为显著误差。

曲率来自实际位置一、二 jet 与实际面积，未用目标单位框架替代诱导几何。不能评价曲率的点会计入 `undefined_curvature_sample_count`，有限极值不会掩盖这些未定义点。shape-operator 判别式仅在取平方根时作非负舍入截断，截断前的最小值另外记录。

Fourier 模长的定义为 `abs(FFT(R_component)[k])/N`，没有把非零频率乘二。它只是解释残差的角尺度，不是高模尾和或谱收敛证书。完整二维数组没有写入输出；每行极值、前若干模长和五区摘要足以定位首轮问题，原准确系数仍可复算全部场。

## 3. 同网格回放与可选分段加点

默认读取原报告的最细已保存审计网格；若原报告只有 checkpoint，则读取其 collocation 网格。只有径向点、角数与中心积分阶数全部相同时，输出才附 `published_summary_comparison`，把重算最大值与原报告逐项对照。

`--include-breakpoints` 会加入三个过渡的端点与局部 Cauchy 修正截止点。它保留同一场与同一度量，但改变中心积分的细分方式，因此不冒称与原报告进行了逐项同网格回放。`--radial-nodes`、`--angular-nodes` 可另设有限审计精度。

所有报告坚持 `sampled_only: true`、`continuous_metric_certificate: false`、`embedding_proved: false`、`whole_surface_reach_proved: false`。这些分布用于判断误差在入口、负曲率段、尾部还是包络约束附近，不承担完成标准的连续认证。

## 4. 已执行的人工开发检查

内置人工输入仅为 \(A=0.9,B=0.72,w=0.02,L=1.1,r_c=0.22\)，两个侧号均检查。正侧另含一个非零 metric 自由系数，以验证设计报告冻结为 fixed 时的同一性；没有进行优化。

实际开发 JSON：`frame-collar-residual-audit-check-20261114.json`。核验包括：

- 原模型与冻结回放的 \(X,X_t,X_{tt},R\) 逐位一致；
- 新全域极值与原 solver 审计摘要一致，每个径向行都被分区覆盖；
- 错误实现 hash、被改动的浮点系数、不属于 binary64 的假准确系数、被修改的 metric 定义、被修改的核心身份均被拒绝。

上述检查通过仅说明审计器的身份和定位接口受检，没有在本地评价本课题的强椭圆候选。

## 5. 公开 Actions 调用

先运行人工检查，再读取已归档的实际候选。以下两个研究命令都是只读重评价，可以按需要选择其一；没有第二次优化：

```bash
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/frame_collar_residual_audit.py \
  --check-only --out "$RUN_DIR/frame-audit-development-check.json"

# 原报告的 121 x 768 最细网格，保留同网格摘要对照。
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/frame_collar_residual_audit.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43602519926-1-ellipse_frame/frame-ellipse-positive-fixed.json \
  --out "$RUN_DIR/frame-ellipse-fixed-distribution.json"

# 同一参数，加入径向接缝与入口截止点，以定位窄区误差。
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/frame_collar_residual_audit.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43602519926-1-ellipse_frame/frame-ellipse-positive-fixed.json \
  --include-breakpoints --out "$RUN_DIR/frame-ellipse-fixed-breakpoints.json"
```

原输入 commit 和当前 audit commit 可以不同；三个定义几何的实现文件必须仍逐一同 hash。未来若更新了 solver 的 metric basis 或基场，不能用这次审计的身份通过声明替代新的明确迁移检查。
