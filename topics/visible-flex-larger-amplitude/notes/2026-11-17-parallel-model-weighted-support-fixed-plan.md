# 固定 β=1/4 的实际 G 全连续支持量：唯一有限计划

## 1. 对象与已有证据

只读 `parallel-pulse-a5-complete-base.json.gz`，SHA `26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72` 所定义的共同五次场。实际像为 R638/R648 的

\[
G=c+\lambda(F-c),\qquad c=Z_0e_z,\quad
\lambda=a/\operatorname{mean}_{4096}|F_\phi|.
\]

新的审计量是以中心 0、取向 \(N=G_\phi\times G_s\) 的
\[
\sigma_{1/4}=(G_xN_x+G_yN_y+\tfrac14G_zN_z)/|N|.
\]

这是一项新的支持量检查；它不重算 R648 的全域 Gram、归一化或当前在跑的 G 曲率。819 份已付证书的完整索引为 `parallel-pulse-gram-fixed-recovery/result.json`，SHA `df41433b71147ac11d3f0193be31323d7e23a879cb2b05231d3a3e166b0d88fb`。

## 2. 固定范围与调用账

819 个精确径向片按 `0:all` 至 `816:all`、`817:before`、`817:after` 排列。最后分界是精确有理数 \(1-5/2^{60}\)，不把最后极小 after 片删掉。

先且仅先调用以下五片，每片一次：`0:all, 390:all, 498:all, 817:before, 817:after`。如果五片全部证明严格正支持，则完整复用五个结果，仅调用其余 814 片，每片一次；任一失败不自动调整网格、不重跑，也不以另一个候选替换。

每个精确片固定角网 Q8192、4 个闭径向子片、β=1/4。分片先从原胞宽形成共同五次的 Bernstein 控制及真正 s 导数，再用精确有理参数作 de Casteljau 限制；小 after 片不另除极小宽。每片的 \(|\lambda-1|,|\lambda_s|\) 直接消费对应 R648 报告。

最终全域成功要求完整 819/819 覆盖、零异常/失格，以及每个连续盒的 \(|N|>0\) 与 \(\sigma_{1/4}>0\)。实际全域下界以所有已证片的最小值报告；没有另加未经声明的 σ 数值门。

## 3. 科学入口与覆盖理由

几何分工冻结的 reader 为 `parallel-geometry-weighted-support-interval.py`，19,497 B，SHA `f1158760756728ed1cbbdb419ed88a8d47bea2f5fba070bf4c1d7de43d3cfe6b`。`Reader(...)` 只验证完整输入/819 已付报告；首次 `certify(cell,part)` 才构造 Q8192 区间变换。

它以实际公式
\[
G_s=c_s+\lambda(F_s-c_s)+\lambda_s(F-c),\qquad G_\phi=\lambda F_\phi
\]
覆盖同一像的一阶 jet。R643 分量角 Taylor 覆盖用于这三个向量；旋转正交架中的各输入分量频率不超过 640。对角矩阵 \(A_{1/4}\) 与绕 z 轴旋转可交换，因此在该架中计算 \((A_{1/4}G)\cdot(G_\phi\times G_s)\) 与法向长度即是物理量。不把最后的三重积当成带宽 640 的函数；乘积只在已经覆盖输入向量的区间盒内计算。支持量与法向长度逐角盒相除，避免把全域小分子与全域大法向长度错配。

R638 的正角重参数化不改变像的单位法向。\(A_{1/4}\) 同时与相位旋转及水平镜像可交换，所以此上半开放前缀的正支持下界自动适用于同一相位族及已付 C² 镜像半；没有新增 t 扫描。完整封口尚未给出，不能据开放带结果直接调用 R650 的闭曲面 reach 结论。

## 4. 冻结封装与元数据准备

封装 `parallel-model-weighted-support-fixed-batch.py`，11,145 B，SHA `97a707839c3ef45fb47ae9a9d844e0f8f293cb65b4cdd481f84bc48079740f0f`，仅作调用/身份/终态账。计划 raw `parallel-model-weighted-support-fixed-plan.json`，408,556 B，SHA `a2acf3719692e360f8e5a4d0dce1777882494a05286700ae82c5ff7a5561899b`。元数据准备已实际退出 0，未构造 Transform、未读取新几何点。

完整计划绑定每片 exact endpoints、原 R648 路径/SHA 和 λ 两个界。执行时完整核对五代表报告的候选/源码/参数/分片/λ 身份及正性，逐值复用 records；仅其余片调用 reader。每次原子落盘报告、进度及 journal；源码/计划/已消费证据改变则 fatal。异常报告不冒充几何否定证书。原始 JSON 留 scratch，不入仓库。

准备命令（本次已执行，不重复覆盖计划）：

```sh
W=/workspace/scratch/16f63c8bce6b
T="$W/math-research-public/topics/visible-flex-larger-amplitude"
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python "$W/parallel-model-weighted-support-fixed-batch.py" \
  --reader "$W/parallel-geometry-weighted-support-interval.py" \
  --input "$W/parallel-pulse-a5-complete-base.json.gz" \
  --interval-source "$T/scripts/parallel_20261117_arclength_interval_positive.py" \
  --gram-index "$W/parallel-pulse-gram-fixed-recovery/result.json" \
  --component-source "$T/notes/2026-11-17-parallel-root-pulse-curvature-component-box.py" \
  --plan "$W/parallel-model-weighted-support-fixed-plan.json"
```

五代表由几何分工唯一生成 `parallel-geometry-weighted-support-representatives.json`。其全正终态后，对同一命令补：

```sh
  --representatives "$W/parallel-geometry-weighted-support-representatives.json" \
  --outdir "$W/parallel-pulse-weighted-support-fixed-20261117" --execute
```

实际启动日志定向 `parallel-pulse-weighted-support-fixed-20261117.log`，使用可继续读取的 exec session，避免已知会消失的 detached 包装。此计划没有声称已执行剩余 814 片；真实启动和终态另记。

## 实际执行登记（root续记）

19:39:09 UTC真实session34099按本计划开始，五代表48d5完整复用，只补814。环境中断前已有249/819完整报告、0失败；未把中断记为成功或几何失败。原reader/参数/λ来源完全不变，后续最小恢复187c3990b414ebe40a8f8f232720cf943de7e9e3d117f02f922b7930457b6d61/manifest447150d49573f80b9db282f68fc585c21b4ecd224e33c02467c897e3e13cc814复用全部249，仅补570，真实session18950已启动。model唯一完整终态读者。所有完整报告仓外，终态另刊，不以本条计划预付全域结论。
