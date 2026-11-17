# 同一 HoldProfile 的 1.03 完整边值准备：全部原评价点通过

这是一个新的有限边值目标，尚非求解成功或新几何父。长区间 1.04 的原评价点准备在 1800 节点预算内失败后，本条仍从真实 d644 前缀与真实 a425 变化型界面出发，只把显式二 jet 参考的末端定为 1.03。未读取任何失败场。所有数据留在仓库外；以下结论为 binary64 实算及指定采样，非区间证明。

## 问题与来源

同一固定 HoldProfile，M160/N2048，完整 482 个 Frenet ODE，325 个左端条件与 157 个冻结右端条件。左端保持原 d644 前三 core 系数及全部原 core 关系。真实界面为 `1.0283496328972757`，其后仅 `0.0016503671027243705` 使用真实保存的 0/1/2 jet 的二次外推。全前缀二 jet 桥与 Fourier 下投影定义沿用原准备源码；初猜不称精化或接受父。

末端对这个新的完整参考重新计算移动标架 Jacobian，并取恰好 157 维的完整实 Schur 块；冻结 `L` 与非零目标 `L y_ref`，不删任何 ODE/模态，不随 Newton 换行。这是有限边界，尚非非线性真尾 DN。

固定输入 SHA256：

| 输入 | SHA256 |
|---|---|
| 原前缀 `parallel-continue0995-m112.json.gz` | `d6441e642b0bb0903915d42e0d4dd9fd564a2e0378e32070110fe6cc7922403f` |
| 真界面 `parallel-negative-hold-type-interface.json.gz` | `a425e38ed4caeebf4d1f96629721c2ba1f54d72eef863ac278e7fb64f0327ba8` |
| HoldProfile 源 | `ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1` |
| 原完整 prepare 源 | `fe6bbefb8cc0411ab6018376b6fde6c957acbe4f57bb24c4a10ce7acecdc9104` |
| 新精确替换生成器 | `b796d6ce10f547eee361714dba4d210925e16bfff92c5e1b33bcec2320f117b5` |
| 实际生成的 prepare 源 | `30a899fd199092197f5cd7dd7c2c1f0f09652e13e267016554a14907d6b55c92` |

生成器逐字断言每处替换唯一；除新末端、超过末端的旧断点与原评价点覆盖外，保持冻结完整准备算法。

## 实际准备门

602 节点无需二分。指定共同 quintic 在每胞四分点/8192 角点通过；另以**实际完整 RHS 作为端导数**构造原 SciPy collocation cubic，检查每胞中点及两个原 RMS 点 `x_mid ± h sqrt(3/7)/2`，全部通过。所有原评价点合计的 Q/W/H 最小值为 `0.027562119423855 / 0.000219164087951 / 0.000212414227938`；不能把这些采样下界冒作全连续界。

完整初猜 ODE 系数缺陷最大 `3.39398823749e-4`，相对分量最大 `2.75691913447e-4`，相对向量 RMS 最大 `2.49994374043e-5`。完整 collocation 缺陷系数最大 `2.66520324761e-8`，除胞长后最大 `3.22983079729e-4`。边界最大残差 `4.16334e-17`，左矩阵秩 325，严格分离 325/157 行。

末端实部截口为 `[2.14366562142, 2.87148124923]`，间隙 `0.727815627814`，L 条件数 `1.00184766693`；目标最大值 `0.100833437525`。但不变子空间相对 sep 估计仅 `1.84843791195e-10`，斜谱投影范数 `6294.28287758`。瞬时行条件好不等于全边值稳定。代表胞估计一次完整 QR 51.07 秒、磁盘 4.47 GB；准备阶段未装配完整 QR，也未做 Newton。

## 最小复现

在恢复上述 SHA 匹配原数据后，使用仓库源码与任意仓库外输出目录运行；`$T` 为本课题绝对目录、`$S` 为 scratch 目录：

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH="$T/scripts" \
python "$T/scripts/parallel_20261117_hold_short_bvp_generate.py" \
  --base-source "$T/scripts/parallel_20261117_hold_bvp_prepare.py" \
  --generated-source "$S/parallel-hold-short-bvp-prepared-source.py" \
  --topic "$T" --parent "$S/parallel-continue0995-m112.json.gz" \
  --interface "$S/parallel-negative-hold-type-interface.json.gz" \
  --hold-source "$T/scripts/parallel_20261117_negative_hold_profile_ivp.py" \
  --warm "$S/parallel-hold-m160-short-bvp-warm.json.gz" \
  --arrays "$S/parallel-hold-m160-short-bvp-arrays.npz" \
  --out "$S/parallel-hold-m160-short-bvp-prepare.json"
```

实际输出 warm SHA `1662ee34a820776570c7535ee5735812d7e7a27822901849c211a89992629057`，完整冻结矩阵 NPZ SHA `2d3c4133959e662b87289fb26fd1aa2c73d2a1ddd278e8f0e1d23fbc1b9d6f7e`，准备 report SHA `88766cbbd645253bbcf5df490ed307fc2060698b2f8e1fbebb1fd43ad4433ef1`。报告含计时与生成器文件 SHA，跨路径/环境复现应比较科学数据及源身份，不要求含计时报告逐字相等。

该有限准备门已过，因此另启动一次原 `tol=1e-8, bc_tol=1e-11, max_nodes=1800` 完整 BVP；其求解结论单独登记。本条不把准备通过、局部谱间隙或初始 QR 估价当作边值求解、实际全域 Gram、嵌入、闭合、reach 或全 t 族通过。

## 已启动的原预算完整求解

[求解生成器](../scripts/parallel_20261117_hold_short_bvp_run_generate.py) 2433B，SHA `d46cd5fb136ae92f3d93138ea7a95099915e41254cc2ff359b438005f799d53a`，仅从原完整f93d源码替换新warm/矩阵身份、描述和初始诊断数；全部求解控制流与门保持。实际生成求解源SHA `af0e5ab2d198c1a475b51a35b57f4a6ced171595b96a8e4d905377adfb404c9c`，仅留scratch。

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH="$T/scripts" python "$T/scripts/parallel_20261117_hold_short_bvp_run_generate.py" --base-source "$T/scripts/parallel_20261117_hold_full_bvp_once.py" --generated-source "$S/parallel-hold-short-bvp-run-source.py" --topic "$T" --warm "$S/parallel-hold-m160-short-bvp-warm.json.gz" --arrays "$S/parallel-hold-m160-short-bvp-arrays.npz" --hold-source "$T/scripts/parallel_20261117_negative_hold_profile_ivp.py" --out "$S/parallel-hold-m160-short-bvp-once.json.gz"
```

发布时第一全段QR实际76.79秒、约化条件3.98478e6；首线性修正max3.45024e−4、完整线性残差1.765e−16。第0步以α=1/1024被接受后正在重算fresh J；这不是最终BVP成功，实际终态另刊。当前生成器及源冻结，未重复派发。
