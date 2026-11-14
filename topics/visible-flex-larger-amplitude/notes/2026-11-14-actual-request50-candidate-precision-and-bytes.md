# Actual request 50：两种完整单步候选的精度身份与原件字节

可信度：数值证据与原件字节核验。2026-11-14，/root/geometry 与 /root，GPT-6 Astra Pro，AI辅助。

## 结论及范围

公开 Actions [run 43632067148](https://github.com/Rogerhu12/math-research-public/actions/runs/43632067148) 已在同一组 request 47 保存的四个局部矩阵上形成两份完整 $226\times224$ 单步矩阵。直接在原坐标使用 longdouble 的候选，实际完整诱导无穷范数误差小于本次 R271 逐级频率平衡候选。因此下一份完整系统使用直接 longdouble 路径；本次没有证据把 R271 路径选为较优者。

这里的比较对象是四个保存的 binary64 局部矩阵所定义的精确有理 RK4 映射。它没有认证局部矩阵等于连续方程的精确导数，也没有接受新的 native 解或让旧方向继续试步。完整误差分析由独立的 `exact_20261114_saved_stage_full_rational_reference.py` 给出。本条补齐候选本身的工作精度、完整数组和可复核字节身份。

## 实际回执

本次固定 checkout 是 `d843fb1dcc8cb4b80e54956d98f8076a9c1398c5`。完整 artifact 为 `14127474149`，ZIP 为 50,175,610 字节，SHA256 为 `955be8bc5fa3b74b5018aa3f6a4be162e3415a6f035d0f18f567d0c7e3f5d06e`。根会话已唯一下载并核对该 ZIP；本条没有再次下载或运行科学计算。

候选源为 [geometry_20261114_saved_stage_rk_covariance.py](../computations/geometry_20261114_saved_stage_rk_covariance.py)，SHA256 `01ec3476ce8d2331b49122ce3d001908eb427d52ea52d367a978cd6de9dde548`。它只消费 request 47 的保存数组；输入捕获 result SHA256 为 `da9715ef1685c04210d5c3d8bbfb40629fd4bf810455b497e5e25630ac0aa403`。

| 原件 | 字节数 | SHA256 |
| --- | ---: | --- |
| `saved-stage-covariance/result.json` | 72,160 | `ddb903372b10dd8ebad1e1729eb3dfb67a7f0937f0740fbbfdc7b9cb2a12e8c4` |
| `saved-stage-covariance/array-manifest.json` | 49,663 | `e41e2a0f597647fc08db0477d8fd727ddb76ed7f00c25ae191ccfd99e788da22` |
| `saved-stage-covariance/input-binding.json` | 67,216 | `1f8a09d4a12f1a1a686b1ed56661e51bfcada8ecae441d4be122e3b43fcfd578` |
| 直接 longdouble 恢复后的完整原坐标矩阵 | 404,992 | `29edc4a6fb630f26a645e1f7a9be17e5ea80cbfbb607844d742e6df61eba7232` |
| R271 longdouble 恢复后的完整原坐标矩阵 | 404,992 | `71d9c953a990623e844cb9e6e4ebbfe1c18d3befb5b6a38d1f0c9133f84662bc` |

两份最终矩阵均为 C 次序的 little-endian binary64，保存全部 224 个输入列、224 个 shape 输出行和两行 mean。末端 port 只作用于 Pi 行；mean 不反馈进入下一局部 shape 乘法，也不作 port 缩放。每份单独的 shape 与 mean 文件已按完整矩阵的原字节切片核实，未重新计算或转换数值。

## 实际工作精度及填充

实际 runner 为 x86_64，Python 3.12.14、NumPy 2.3.5。该 runner 的 `longdouble` 虽以 `<f16`、每元素 16 字节存储，其实际格式是 **x87 binary80**：64 位有效数、63 位显式 fraction、最大指数 16384，只有前 10 字节参与数值；后 6 字节是存储填充。它不是 IEEE binary128。

生产者在序列化副本上把每个元素的 6 个填充字节置零，不改变参与计算的数值。所有工作矩阵都保留此明确 encoding。纯字节审计实核了 43 个工作精度数组的 **7,930,284 个填充字节全部为零**，没有把任意未定义填充当作科学位身份。

全部 manifest 包含 49 个数组：6 个 binary64 数组与 43 个 x87 工作数组，共 **22,767,392 字节、1,524,210 个元素**。每个原文件的完整 SHA256、dtype、shape、C 次序、元素数量、指数与符号零计数均与 descriptor 相符；所有元素的保存格式均为有限值。result 中 52 处数组引用，包括重复别名，均与 manifest 的完整 descriptor 一致。

审计记录为 [actual-request50-candidate-byte-audit.json](2026-11-14-actual-request50-candidate-byte-audit.json)，24,895 字节，SHA256 `d9e247d6e57c0f05a5ae33e10c85444fff2043da2dea641bfd17d8cc0c22add8`。本地工作仅解析 JSON、核原字节/SHA、检查整数位字段和切片，没有导入数值数组、重做 cast、矩阵运算、RK、范数或求解。

生产者实际记录两种候选的**合计**耗时 `1.0034859379999972` 秒，峰值 RSS `90216` KiB。它没有分别计时 direct 与 R271，不能从这条记录拆出各自耗时。独立完整有理参考的实际耗时为 `29.961380359000003` 秒。

## 已有科学读出如何使用

以下只是转录独立完整参考的实际报告，没有本地重算：

| 矩阵 | 完整诱导无穷范数误差（近似显示） | 与正确 RN 矩阵不同的 binary64 字数 |
| --- | ---: | ---: |
| 原 request 41 / request 47 observed | $1.5556918699475\times10^{-2}$ | 49,522 |
| 直接原坐标 longdouble 后转 binary64 | $7.1681214304747\times10^{-6}$ | 15,343 |
| R271 逐级平衡 longdouble 后恢复原坐标 | $9.1952611614905\times10^{-6}$ | 9,154 |
| 精确有理矩阵逐元素正确 RN | $3.3611566944625\times10^{-6}$ | 0 |

R271 候选与正确 RN 不同的字数更少，却有较大的完整诱导无穷范数误差；这两个统计不能互相替代。此处既没有新增误差通过阈值，也没有将一块的改善推广为全系统结论。request 47 已显示，把更精确单块直接换入原坏方向会破坏相消，见 [原new519精确账](2026-11-14-actual47-stage43-exact-action-and-new519-attribution.md) 和 [R272](../results/R272-native-RK-reference-and-propagation-error-split.md)。

后续完整构造保持原 868 个步骤的 profile、x/h、完整 226 状态路径、末端 port 及两行 mean，形成新的原坐标 binary64 单步块；后 504 个原块及全体 base、residual、cut、far、原 sigma、577 节点限制保持原身份。新块构成新的有限矩阵，必须一致重解，再以原非线性方程、原 guard、原 sigma 和原严格残差下降规则检验。当前记录没有完成这个后续求解。
