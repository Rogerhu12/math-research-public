# 真 T112 零高度锚、完整 J 和独立二阶核对

2026-11-14，exact_refinement，AI 辅助。

**实际结果：T112/N2048 的原非线性尾 worker 已完成完整零 H、完整 J 和完整
finite audit。它与已完成 prepare112 的全部数值配置和数学源相同，可以作为
下一次真实耦合的严格首零缓存。没有重复求解零 H；没有以 ready 的线性图
代替实际 J，也没有据此接受新前缀或闭曲面。**

## 1. 原公开 Actions 的实际回执

- Run [43588155190](https://github.com/Rogerhu12/math-research-public/actions/runs/43588155190)，
  job `132427013813`，artifact `14111343237`，数值 step 实际成功。
- [完成记录](public-actions-43588155190-1-tailzero112/zero-H-T112/result.json)、
  [完整 response 包](public-actions-43588155190-1-tailzero112/zero-H-T112/tail_0001.json.gz)、
  [独立零 J 核对](public-actions-43588155190-1-tailzero112/zero-H-T112-J-audit.json)。
- `modes=112, quadrature=2048, spacing=2`；保持原物理 `depth=8`、RK12、
  audit12、所有校准、`solveTolerance=2e-9` 和原完整审计。
- 总耗时 `1351.7417891979999 s`，实际 request 耗时
  `1330.3097704309998 s`。worker 正常退出 `0`，stderr 为空。

| 实际字段 | 值 |
| --- | ---: |
| 全 112 项 cut H | 全部精确为 0 |
| 非线性 shooting residual | `0` |
| 全 Jacobian | `338 × 112`，共 `37856` 个有限条目 |
| 完整 shooting 状态 | `577 × 224` |
| actual shooting depth | `576` |
| 原 physical depth | `8` |
| rawNode / rawStates | 9 个节点及完整对应状态 |
| fullD / normalizedFullDefect | `0 / 0` |
| minLeading / minD | `1 / 1` |
| actualMetric | `9.992007221626409e-16` |
| formalCurvature | `7.994254693518797` |
| maxPhysicalPV / holonomy | `0 / 0` |

切口实际读数为
`r=0.30000000000000004`、`w=0.08000000000000027`、
`w_r=-1.866666666666673`、`E=1.0064`、
`E_r=-0.2986666666666687`。非均值 height/slope/second 全为零；
`meanSlope=w`、`meanSecond=w_r`，两个均值修正均为零。

原 trace 的 tangent predictor 记录
`maxChartCondition=385639413119263240000`。这是实际有限切向传播的诊断，
原值完整保留；不能因为本次 H=0 的 residual 为零就据此声称非零 H 的条件性
或频率收敛已经解决。下一步仍按原 worker 对真实非零 H 求解。

## 2. 完整缓存结构和跨 job 身份

对下载的七件完整缓存包运行既有 `seeded_zero_tail_client.load_completed`
的结构校验，未启动 Node、未再算尾。全部检查通过：实际正常完成、精确零 H、
`jacobian=true` 与 `audit=true` 原 request、全 J/jet/mean、完整状态与 raw
状态副本、所有输入和 source/capacity 指纹彼此对应。

另与同 run 的实际 prepare112 包逐项比较，以下四项全部相同：

1. 除原 helper 明确允许迁移的输出 I/O 路径外，**全部数值配置相同**。
   实际输入 `T112-config.json` 和零锚 `config.json` 的文件 SHA 本身也相同。
2. ready 的切口、线性数据、物理参数、校准表、原始源 SHA 和 profile 指纹
   等完整语义相同；只有跨 job 的绝对路径、内存诊断等非数值信息不同。
3. response/intent 的全部实际数学源条目相同；没有读取私有库或换用另一实现。
4. Node 版本和三个 constructor capacity 变换的完整记录相同，实际容量为 112；
   原数学文件没有被覆盖修改。

因此下一真实耦合使用

`VISIBLE_FLEX_COMPLETED_ZERO_TAIL_DIR=notes/public-actions-43588155190-1-tailzero112/zero-H-T112`

所指向的这份完整包。目录必须含下表七件原文件。严格 client 在新 job 初始化
真实 worker 后还会再核当前 ready/source/config 身份；首个**精确零 H、非 audit**
请求才可复用。非零 H 或最终 audit 请求会清除导入缓存并调用原真实 worker。
T96 包不能通过这份配置/维数检查；数值小量也不会被阈值化成零。

## 3. 独立零背景 J 检查的真实数值

`exact_20261114_zero_tail_response_audit.py` 在同一个公开 Actions 中消费
已完成的 response；它没有进行另一次尾求解。检验使用零背景 Darboux 线性式

\[
J_{rr}=\frac{w_r}{w}
\left[\operatorname{diag}\left(\frac{(2j)^2}{r}\right)-J_r\right].
\]

| 检查项 | 实际误差 |
| --- | ---: |
| 二阶 J 与线性化 Darboux 关系，最大绝对误差 | `5.223322659730911e-6` |
| 同项最大相对条目 / 列误差 | `1.5240178845565773e-12` |
| slope J 的 Fourier 非对角误差 | `0` |
| second J 的 Fourier 非对角误差 | `0` |
| meanSlopeCorrection 的全部 J 行 | `0` |
| meanSecondCorrection 的全部 J 行 | `0` |
| height J 与单位矩阵之差 | `0` |
| 最大 slope J 绝对值 | `32802.403742635055` |
| 最大 second J 绝对值 | `3839524.316526198` |

原 second 行仍是原源码在实际 tangent graph 上的对称差分，步长 `1e-4`；
上述检查没有更改该方法、原容差或任何验收门。

尤其要保留另一项真实差异：实际 shooting slope J 与 ready 中预先计算的
线性 stable graph 之差，最大绝对值为 `828.7132857724173`，最大相对条目/
列值为 `0.035157884011777545`。这两个对象属于各自的原数值算法；ready
线性图可继续用于实现链的 FD 测试参考，**不得替换本次实际 full J**。

## 4. 使用范围

此结果支付的是新 T112/N2048 原尾在 H=0 的真实有限锚、全 J 和原 audit。
它没有接受 M112 的完整前缀，没有证明实际非零材料 H 的尾存在，没有支付
真实 cut 的无限材料谱，也没有改变同 g 频率/网格精化、完整 Cartesian
接缝、闭曲面全相位 reach、握持幅度等剩余条件。

下一步直接继续已准备的 M112/T112/N2048 完整耦合，读取首零缓存命中及随后
真正的非零尾请求记录。无需重复本次耗时的零锚计算。

## 完整七件缓存包指纹

| 文件 | SHA-256 |
| --- | --- |
| `result.json` | `10493cd7ff3eef8698d9d39a59f3a009d1b327a560fcaf8eb0388ab2a5282389` |
| `tail_0001.json.gz` | `6b4ff3e5bc11e23419242ee018b668c57f08b6dbdd791cd43d81883bf6f4960e` |
| `tail_ready.json.gz` | `ab21aac94e8c3e28bebc5bbcdf66c57b37b3c8c73a672e132087bbdb4b62ab0e` |
| `tail_intent.json` | `e36bbacfcf7d3708be34e6d8c350132184b4c46c76ce6be391a643a2d1bb127d` |
| `config.json` | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| `tail_runtime-config.json` | `a6c0425250b2db5e477928a29a4c550d97e733af254611f8daf367e3f9378f6c` |
| `tail_capacity.json` | `4f0f7aaab43f8ed90c478c2983026671f4c17ddcbe25d494746a4dafc96210dc` |

独立 J 核对 JSON 的 SHA-256 为
`6fb7b6461e38311c262e51fd0af92e92c9272c413d259275c5c11422652ec9d9`。
