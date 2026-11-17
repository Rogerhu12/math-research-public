# n4 实际尾：保留 N 的周期求积复用

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。
本笔是有限求积的等价实现及实际状态对照，不是新的 tail 解或幅值
纪录。只复用整数周期，不叠加反射复用，不改原局部或最终门槛。

## 为什么有限求积相同

令声明的等距角向节点数为 N，所有表示频率为 spacing·j，
d=gcd(N,spacing)，nq=N/d。将节点编号 n 改为 n+nq 后，每个
Fourier 相位增加 2π·j·spacing/d，是 2π 的整数倍。因此 Q、L、P、
Pt、U 及由它们组成的 root、moment、flux 投影 integrands 都逐
节点周期重复；对有限状态系数的导数也具有相同周期。

完整 N 点平均等于前 nq 个独立行的平均，权重为 1/nq。
mean 分量也保留。每次 root 的完整 rows 仍恢复为 N 行，后续
物理 jet 和 audit 继续看到声明的全部 N 行。这个等价是数学上的
有限求积等价；三角函数求值与加法路径发生变化，不主张 bit identity。

原 `N > 4*M*spacing` 门仍检查**原声明 N**，public `N` 不改，
不以 nq 冒充原节点数。D/S/A 条件、root 容差、RK 网格、实际
shooting 方程与最终 `2e-9` 门均保留。

## 实现与导入路径

`scripts/resume_n4_tail/install_periodic_quadrature.py` 在调用者明确
指定的独立 source 副本的 `scripts/periodic-quadrature/` 生成四个
owned 模块：general root、fast momentum、split flux、fast split
flux。canonical `repro/source-root` 只读；安装器在结束时再次比较
原四模块字节。

安装器只在 owned stage core、stage split 和 worker 的 warm-remesh
engine 入口上重定向 imports。core 的稀疏全局线性系统与原接受
逻辑没有替换成旧 Riccati 代码。四个生成源码的审阅副本在
`scripts/resume_n4_tail/periodic_modules/`；它们通过
`VISIBLE_FLEX_SOURCE_ROOT` 读取未改动的 raw/cusp 辅助模块。

复现安装：

```sh
python scripts/resume_n4_tail/install_periodic_quadrature.py \
  --source-topic FRESH_SPARSE_SOURCE_COPY \
  --manifest INSTALL_MANIFEST_JSON
```

完整安装前后 SHA-256 在 `periodic_install_manifest.json`。本会话
已安装的独立 source 位于 `transfer_work/periodic-source`。

## 已接受 M16/N512 真尾的局部对照

输入来自 n4 eta=.1/q=.01 运行的实际 .2H accepted 尾记录
`n4-coupled-eta010-q010-v1/seed-tail_0001.json.gz`，输入原 residual
1.00419e-9 量级；其精确值与 SHA-256 保留在机器记录。
选择 stage 0、40、46、120，各比较 x=0 与沿**原** cusp-aware
RK 路径得到的 x=.5 状态，共 8 个真实状态。两引擎使用同一状态
和同一物理 profile。

| 量 | 8 点最大差或检查结果 |
|---|---:|
| root L 相对 L∞ 差 | 2.508809244955944e-18 |
| root L 绝对 L∞ 差 | 1.0057428355040522e-20 |
| RHS 相对 L∞ 差 | 3.5629613486399885e-16 |
| RHS 绝对 L∞ 差 | 6.938893903907228e-18 |
| Jacobian 相对 L∞ 差 | 4.49254689224948e-18 |
| Jacobian 绝对 L∞ 差 | 1.673470251262188e-10 |
| 周期 root 代入原 N 点矩方程的相对 residual | 1.429628973961541e-16 |
| public N / 独立行 / 完整 rows | 512 / 128 / 512 |
| rows 周期复制差 | 0 |

表中相对差以被比较整个向量或矩阵的 L∞ 尺度归一，不能被误读为
每个近零分量都具有相同相对精度。原始逐点尺度、min A/min D 与
root residual 均保留在记录里。将 N 设为被禁止的边界
`4*M*spacing` 时，两引擎都以同一个原错误拒绝。

8 个单次局部调用的观测总时间为原实现约 92.87 ms、新实现约
93.41 ms，包含启动/JIT 影响。本笔不作整体实测提速声明；实际
worker 的完整负载重启另外记录。

入口为 `compare_periodic_actual_stages.mjs SOURCE_TOPIC
ACCEPTED_RECORD_GZ OUT_JSON`，scalar 结果在
`periodic_m16_stage_comparison.json`。没有提交真实场、网格或
checkpoint。后续仍必须让实际 worker 按原门槛完成真正求解，
局部等价对照不能替代该终态。
