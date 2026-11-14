# Request 20 之后的三行域保护独立入口

依据[真实 request 20](2026-11-14-actual-request20-protected-query-and-next-domain-rows.md)，
仅扩展优化器的临时切空间；不改已冻结的完整方程、Rphi、native
接口、度量公式、原接受门或原 699 节点。

## 输入和 CLI

`geometry_20261114_multiline_tangent_warm.py` 固定三条实际观测查询：
`(interval, physical-angle-index)=(473,0),(480,0),(473,11)`，
均用原左 RMS fraction `0.17267316464601146`。角 index 指原
N2048 物理角网；`--angles 4096` 仍指原材料边界的角积分规则。
index 11 已在 request 20 的 alpha=`2^-7` 原报告直接出现。

首运行从 request 20 的完整实际新 warm 续接，SHA256 为
`0036063ff99e7b3624e494b29430b9a3a8ec3eaae15f277447efcc71b8cc5e71`。
四个原输入的字节身份仍逐一硬锁：原 accepted M96、原 prepared
699 节点、真正完成的 T112 零 H 全 J、同一 T112 config。
`check_resume` 核整个原场/标量公式、实际 p、常值约束、完整 producer
账；可消费已冻结单行 schema 或本新 schema 的实际后续 warm，
每次都必须显式给出所读压缩文件 SHA。

以下变量分别代表这些实际文件及一个新的空输出目录：

```bash
python computations/geometry_20261114_multiline_tangent_warm.py \
  --accepted "$A96" --prepared "$P699" \
  --tail-anchor "$ZERO112" --tail-config "$CFG112" \
  --resume "$W20" \
  --expected-resume-sha 0036063ff99e7b3624e494b29430b9a3a8ec3eaae15f277447efcc71b8cc5e71 \
  --out "$OUT" --iterations 1 --lsmr-iterations 200 \
  --damping 270 --damping-attempts 5 --line-search-steps 17 \
  --budget-seconds 1200 --jac-workers 2 --angles 4096
```

这是一个有原始试步次数上限的模型；不以增加模型数或放宽域门
掩盖新的阻断。若产生新 warm，完整新 FD 使用独立薄入口：

```bash
python computations/geometry_20261114_multiline_tangent_response.py \
  --accepted "$A96" --prepared "$OUT/warm-001.json.gz" \
  --tail-anchor "$ZERO112" --tail-config "$CFG112" \
  --out "$FDOUT" --angles 4096
```

FD 内部执行原已冻结 descended-warm response 全部方向、三步长、
Richardson 和 `5e-5` 门，仅识别新 producer schema 并补全来源。
报告真实绑定新 warm SHA，不能给旧报告换 SHA。

## 原行、保留秩和多乘子

每条查询都调用冻结的 `HermiteDomainRow`，重算完整 nodal RHS、
Hermite 链和实际 scalar 直导，并各做原 complex / 实差分检查。
三条完整缩放 covector 为矩阵 B 的三行。先逐行归一化，再调用
原 `TangentProjector` 的 SVD，明确使用相对 `1e-12` 保留阈值。
保留秩无需冒称必为 3；这是临时优化子空间的数值政策，不能删除
任何原物理、Rphi 或域条件。所有原行的实际作用和泄漏均记录，
不能只验 SVD 保留基。

仍实际求解 `[A P C^-1; lambda P C^-1]`，LSMR `damp=0`，恢复
`z=P(solution/C)`；C 是原未投影列范数加正阻尼的对角预条件，
不是投影后精确列范数。实际 merit 只含完整原残差，权重在该模型
及其所有 trial 内固定，阻尼不混入真实 merit。

令 Q 为保留的正交行基，N 为原 B 的逐行归一化矩阵，实际
`g=A.T@(WrR+Az)+lambda^2*z`。只在最多三行的小矩阵上求

`(N@Q.T).T @ nu = -Q@g`，

再令原行乘子 `mu_i=nu_i/||B_i||`。记录小系统秩/奇异值、全部
mu、`g+B.T@mu` 与 `P@g` 的实际重构误差。若归一化 SVD 丢弃
数值小方向，实际误差仍保留，不能把打印的 mu 叫精确 KKT 证明。
未预条件 projected KKT norm 和实际预条件 normal residual 分开
报告，延续 request 20 已发现的尺度区别。

## 输出和接线边界

- `domain-rows.json`：三个实际完整梯度检查、原全域、归一化 Gram、
  全部奇异值、保留秩和原行身份。
- `model-000-operator-check.json`：原完整 J/JT、原 augmented 作用
  和独立真实 collocation complex 检查。
- `model-000.json`：LSMR、投影后真实方向、所有原行 Bz、归一化
  泄漏、Pz-z、多乘子/KKT、真实 slope、所有 trial 和原两组 RMS。
- `direction-XX.json.gz`：完整实际使用方向，供只读复核，不是再生的
  代理方向。
- `warm-001.json.gz` 和 `driver-status.json`：只有原全域通过且真实
  merit 下降才保存新 warm，并始终保持 `success=false`。

没有本地数值运行。只有 AST 静态核；上述真正梯度、SVD、LSMR、
域与 FD 必须由公开仓库自己的 Actions 实算。预算仍为 1200 秒，
预计为数分钟的一个模型，实际时间由产物记录。

新 warm 和 FD 仍兼容原 `physical_test_full_dn` 的字节 / source
绑定：完整 field/scalar schema、states/rhs、实际 p 和全部 core
保留；响应仍具有原 physical-test schema、当前 prepared SHA、
完整 consumed-source 账和原 FD 门。新优化 schema 不冒作接受场。
本入口不调用 native，也不把新 H 近零化；后来若接完整求解器，
必须真解该新 H，保持原所有 inner/outer/final audit 条件。
