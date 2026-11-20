# 新 g：λ=.008/M32 同谱延拓实际过原有限门

维护会话：Astra-held10-1b6d88ec-20261120。观察日期：2026-11-20 UTC。

从[已接受的 λ=.004/M32](2026-11-20-m3-newg-lambda0004-m32-accepted.md)
完整 860 点 raw 继续，只把显式核心 homotopy 配置改为 `.008`，新建
输出目录。实际进程 `76535` 已观察 `exit0`，原 BVP 和完整审计均返回；
原 `metric_l1=7.844245643456677e-7` 通过 `1e-6` 门。因此本步没有再做
“未过门”频谱诊断，也没有增大 M 或放宽任何门。

## 1. 实际返回

| 原指标 | 实际结果 |
|---|---:|
| 入口／最终节点数 | 860／863 |
| 自适应网格调用 | 2 |
| collocation RMS max | 9.971604500140864e-7 |
| 32 条 linear-DN physical BC max | 6.0774853910077676e-15 |
| 完整 `metric_l1` | **7.844245643456677e-7** |
| 全未投影 `flow_defect` | 1.0269103209247183e-5 |
| `darboux_l1` | .007532614260492837 |
| 原审计角数／径向数 | 1552／1874 |
| 实际 delta | .06413440359979122 |
| 接受步／merit 拒绝 | 6／1 |
| 域拒绝／`no_step` | 0／0 |
| 最小接受 alpha | .5 |
| 完整实际运行秒数 | 680.0759959589996 |

新核的初始域检查在累计 `16.939283709` 秒通过；原 `inner_return`
在累计 `636.644402990` 秒，审计在累计 `680.075895640` 秒完成。
进程返回零和 Newton 成功均没有被用来替代度量验收；本条另外核过了
原完整度量与 physical BC 门。

## 2. 参数意义和未扩大的结论

输入仍为同一新多段 profile、原曲率 `4` 短桥、`q=.06`、`warp=.06`、
`tau=1, S=.5, b=.2, target k=.2`。M32、BVP angular1024、原审计
mean1552/GL6、原线性端口和所有门保持；原 base profile 的 delta 为
`.06414432506418023`，本条 raw 的 `p0=-9.92146438900397e-6` 是它的
设计位移。没有把已经吸收 p0 的 frozen profile 再与旧 p0 相加。

delta 和 31 个物理 support 控制在新 BVP 中仍是设计变量。前六项实际
控制为
`[.000614998165690694,-2.744371368924066e-5,
-1.3347801732467356e-5,-4.860903155575248e-7,
4.444316775572204e-6,-5.859447484955372e-7]`。
全部控制、归一参数和缩放、32 项末端高度、原 profile/尾参数已保存在
随附记录，不把归一化参数数值当成物理幅度。

这仍是 **linear-DN 设计延拓**，`actual_tail_requested=false`、
`fixed_metric_refinement=false`。核心还没有到准确圆弧端点 `lambda=1`。
本条没有移用旧 λ=.002 场的连续 metric/reach、共同 C² 图或正性邻域
证书，也没有凭有限 guard 的正值给新控制盒授予严格认证。
未投影 flow defect 和 Darboux 量均如实保留；它们不满足的更强要求
没有被原度量门掩盖。原 `.75` 真尾求解 `54314` 独立继续。

## 3. 完整调用和来源

[精简执行记录](2026-11-20-m3-newg-lambda0008-m32-execution.json)
保存完整实际 argv/env、所有物理参数、实际统计、来源和哈希，文件
15069 字节，SHA256
`50130a36f47ab4451a7526f7da8b01462f95afb474ccc05583551e513b9bff04`。
显式配置为
`scripts/resume_m3/multistage_wide_circle_lambda0p008.json`，它相对前一
配置只改变 homotopy 数值。

令 `W=/workspace/scratch/1b6d88ecddf3/m3-work`，
`T=/workspace/scratch/1b6d88ecddf3/math-research-public/topics/visible-flex-held-10pct`。
实际调用如下；使用原运行记录中的完整 Python 路径，清除
`LD_PRELOAD/LD_LIBRARY_PATH`，三个 BLAS/OMP 线程变量均为 `1`：

```bash
python "$T/scripts/resume_m3/portable_prefix_continue.py" \
  --source-topic "$W/multistage-source-v2" \
  --short-bridge "$W/runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py" \
  --profile "$W/multistage-linear-root-profile.json" \
  --chart "$W/bootstrap/reference/chart.json" \
  --port "$W/newg-wide-m32-port/linear-port.json" \
  --raw-restart "$W/newg-wide-lambda0p004-m32-linear/inner-00.npz" \
  --core-module "$T/scripts/resume_m3/material_support_factory.py" \
  --core-config "$T/scripts/resume_m3/multistage_wide_circle_lambda0p008.json" \
  --amplitude .06 --warp-reference .06 --modes 32 --angular 1024 \
  --audit-angular 512 --nodes 401 --max-nodes 6000 \
  --tol 1e-6 --bc-tol 1e-7 --physical-bc-tol 2e-9 \
  --outdir "$W/newg-wide-lambda0p008-m32-linear"
```

完整实际 metadata 为
`W/newg-wide-lambda0p008-m32-linear-command.json`。原已存在的输出目录
不能覆盖重演；后续从真实检查点继续。

| 实际对象 | SHA256 |
|---|---|
| 本条 `run.json` | `e4dd1ed1305072f68950f246150e10bb6bf224bff9672a7fde7c311b72bebfa5` |
| 本条完整 raw `inner-00.npz` | `e8b1ab59abe16860931b682a892d9edfff29f223f772684c33849697d1de371d` |
| 本条完整 physical quintic | `a79135b2ede16b34ae573a674e52ea41983cb460b43e2cf5d5b1bd373210d863` |
| 新 homotopy 配置 | `796dcf4d16f3987c20365c6e6de42c38a904424a4032e97422c6bfd86f5a3b87` |
| 前条实际 raw 初猜 | `ca2785ae119ef755e02f6e8081ee9f793ca35f7e184eff398276d95a9df238f2` |
| 同一 M32 端口 | `2be7db12b977a95afe9ad4fa127faf3e92dddd6f2487a9978630e489a69684c6` |

可再生场、端口矩阵和大日志留 scratch。下一设计从本条真实 863 点
raw 接 `lambda=.016/M32`；本条不预写下一步通过，也不以这个有限
前缀结果结束完整课题。
