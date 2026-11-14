# 独立扩域预计算与真实参数前 20 段保全

对象仍为准确 affine `delta5=-7789843107295549/4611686018427387904`，
同一 `step5_retargeted_reference/descriptor.json`（`097354fe...`）。
中心源与 `delta5 +/- 1e-9` 整盒源保持区分；本记录没有完成全 550 段返回。

## 1. 中断的原始范围

uniform 第 17、20 段的首次密度子进程均记录 `returncode=-9`，没有 Python
数学门异常。`step5_parameter_density_interruptions/` 保存各首次 partial JSON、
准确命令/退出记录；20 还保存原始 log 文件。两次退出的具体原因未得到系统证据，
不得称为 OOM、数学失败或“已定位的内存问题”。

同一 frozen v5、相同真实参数盒，在已完成的 Q512 扩域证明缓存上重启后，两段均通过。
20 的完成 center/uniform 报告 SHA256 分别为
`8b6c3472268072d2bd2728cf839031d803e86c7c63a8fe8fb429ffbd1b14a9eb`、
`2ab00ecc5bda85935d8a3e1dd65ee26d77e3fd13dbabe0157b248a6e0f0444e3`。
这仅是两次实际完成的结果，不据此推断先前进程退出原因。

## 2. 只改进程生命周期的 controller

新增 `fourfold_parameter_precompute_expanded_domain.py` 与
`fourfold_parameter_density_cover_efficient_v3.py`。前者准确复制 frozen v5 的
cache key/lock，逐实际 germ 选择已完整证明的更大真域，然后在独立子进程执行
原 `fourfold_parameter_expanded_time_domain.py`。该子进程结束后，cover 才执行
原 frozen v5 密度进程；实际 sampler、cap、DFT 噪声门和 target 不变。

v5 消费者仍逐件执行原 `checked_parameter_proof`：对象、root、descriptor、
真实 germ、准确时间、参数范围和依赖 SHA 均不因预计算而略过。不存在匹配的更大域时，
继续使用原 R3。真实 R6 证明未通过时保留该报告而回退 R3；子进程异常退出则停止当前
controller 并记录，不能将其伪装为解析预算通过。

实际运行已覆盖两个分支：

- 第 20 段重用已有完整缓存；报告
  `notes/2026-11-12-precompute-parameter20-cache-reuse.json`，SHA256
  `dc3a596c3780df8698c4aaf8975d21296e9962f65d724719ff487c4e053bdf53`。
- 第 22 段首次在独立子进程生成 Q512 中心及整个 `+/-1e-9` R6 证明；
  proof CPU 8.065 秒，墙钟 62.069 秒。实际 proof 为
  `step5_expanded_parameter_time_domain_full/forward_0022_f10003e1943744548c8b.json.gz`，
  SHA256 `8f114f897ffad3f1d3a3fe95b03745dbfa61bcfe1b1421ae39a941a6a4073d1d`。
  controller 报告 SHA256 为
  `3cfb2df0d888414528ec83e53a5af330d5516e81ffb4ef38db93bddd3008b651`。

最短重做入口（在课题根目录）：

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -u scripts/fourfold_parameter_precompute_expanded_domain.py --domain data/phase_ring_continuation/step5_sharp_time_domain_full/forward_0022_r.json.gz --out notes/2026-11-12-precompute-parameter22-isolated.json
```

已有缓存的该命令将明确报告 `reused=true`。欲重做 actual proof，使用该报告保存的
`children[].command`，将 `--out` 指到新文件，保留旧证书；不以覆盖旧报告冒充重算。

## 3. 固定前 20 段的完整有符号累计

`step5_parameter_density_prefix_checks/{center,uniform}_efficient_prefix0020/index.json`
是各 live index 在准确完成 20 段时的逐字快照，不是手工截断后沿用多余累计。
分别再次运行 frozen center/hybrid accumulator，得到完整 `C0/C1/C2` 与
`D0/D1/D2` 系数球，保留所有段间 `g1*g1`、`g0*g2` 和每叶 center `2J11`。

center chronological 报告 SHA256：
`b761788bb63983f9a7f8ea8820b2a76be4d5c14bce58870dbaf841172f2ea863`。
hybrid chronological 报告 SHA256：
`efa7f31365923809279726bc1a4cba23ed86a74b09e10a111ac5838a00e86c8e`。

两者有限首积分零频 `C1[0]` 的共同数值约 `2.19726007442804e-4`。
center/hybrid 的 `D2[0]` 分别约 `-8.13548467243609e-8` 与
`-8.13548467243562e-8`，实际报告保留完整有向球，以上十进制只作说明。
它们是前缀的有符号坐标积分，**不是完整 twist，更不是已验收的 KAM 常数**。

hybrid 全盒 `A/B/E0/E1` 已按真实 MVT 加入 `eta*C`、`eta*B` 费用；
不使用缺失的 uniform `g1`，也不把该缺失记为零。
连续推进使用新 cover v3，保存 live 文件与本固定包分离。
