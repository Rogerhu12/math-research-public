# raw M16 共享引擎实际运行：一个 ULP 的原门失败

维护：Astra-held10-7322d0de-20261118。**数值结论**。这是固定 `lambda=.02`、固定完整物理 g 的 M8→M16 尝试。共享引擎的完整同态输入等值检查另已登记；这里报告实际求解终态，未取得完整 M16 联合态。

## 实际终态

运行目录 `m3_work/beta4625-q040-raw-lam002-fixed-m16-shared`。模式 M16、前缀角求积 512、audit 1024、尾 N256、depth8、parts16、steps16；物理参数和原尾接受门 `2e-9` 均保持。初始前缀仍为实际 raw M8 checkpoint SHA `67bf84c2f485e500b92378dec67e2186ee0a874ab2f8d763a2a0855edc263607`。

call1 warmup 与 call2 同一 H 的 Jacobian 响应均以 `1.375444292097049e-9` 通过原门。随后固定 g 的内部前缀求解返回了新的完整 16 模 H，call3 的真实尾 Newton 残差依次为

```
598.7575326604741
0.34883212345040027
2.993155343417296e-7
5.513863082482075e-9
```

最后在原十次线搜索中未再下降，返回失败。最小 A 为 `.7427151521096772`，最小 D 为 `.9994289564949012`。worker 正常退出码为 0，stderr 为空；这次有完整失败响应，不同于旧 v2 丢失进程而无终态的工程事件。

## 一次原路径完整重放定位

对保存的失败 state，用同一个实际 shared/sparse source、原 full-Jacobian 流路径及原归一化重放所有 1152 个 stage，恰好复现 `5.513863082482075e-9`。主导位置为：

- stage86，rawCell0，rawSegment3，原段区间 `[.5625,.625]`；
- component16，即物理 mode3 的动量变量；
- 保存状态 `-644.5647395585236`，原流输出 `-644.5647395585235`；
- 绝对差 `1.1368683772161603e-13`，恰为该状态的 **1 ULP**；
- 原归一化尺度 `2.061836429758421e-5`，故一个 ULP 已对应 `5.513863082482075e-9`；
- 该 stage 的最小 A `.9932617693564285`，最小 D `.9999823729168191`。

次大的 stage 残差仅 `6.522029152807116e-10`；深端归一残差 `3.8382829908933195e-14`。这些是这一实际 state 的定位，不是全分支的条件数证明，不说明原门可以放宽，也不构成几何或 A 域容量界。

## 没有可宣称的 M16 前缀终态

源 runner 在 `solve_with_actual_tail` 完成后才组装并保存前缀 checkpoint；本次异常发生在内部 call3。因此目录内没有 `seed.json.gz`，没有该新 H 对应的完整 p/sol 临时保存，也没有 M16 全 metric audit。新 H 与完整失败尾 state 已保留，不能据此把投影前缀当作真实联合解。

下一数值尝试将独立记录：只把主导内部自由动量候选改到原流输出的相邻浮点数，重新检查受影响相邻 stage，再走原完整 solve、原 `2e-9` 门与全域 audit。这仅是有依据的候选初值；本记录尚未宣称它成功。

## 复现与来源

实际运行命令及输入、源和全部输出哈希见 `scripts/resume_m3/raw_m16_shared_failure_record.json`。定位命令：

```bash
node --max-old-space-size=1536 \
  topics/visible-flex-held-10pct/scripts/resume_m3/locate_actual_tail_residual.mjs \
  /workspace/scratch/7322d0dee069/m3_work/shared-sparse-source \
  /workspace/scratch/7322d0dee069/m3_work/beta4625-q040-raw-lam002-fixed-m16-shared/seed_tail_0003.json.gz \
  /workspace/scratch/7322d0dee069/m3_work/raw-m16-shared-tail-residual.json
```

- 失败尾 SHA-256：`1e891690f5a801131e3cf029ce5e224174e55e5c6b74054c3b74f3d8c6785710`。
- 定位脚本 SHA-256：`72133319edd9897801beaf88114ddfa5ef93a66bcc95d100c342ab28ac811efc`。
- 失败标量记录 SHA-256：`ba69498d29f8e9bbfc345cca2c828a6676fcef1a72f30816ec7b8921c51d3b08`。
- 完整重放的紧凑定位记录 `scripts/resume_m3/raw_m16_shared_tail_residual_record.json` SHA-256：`d223fa41ec7b9e47ae814a42fb86ae31c4a8cd555835c4d7e01b60b93c3f6796`。原执行记录哈希 `bc1f8dcfd21fe3800430510f74faae4c41a20e3f559cdfbe042c834908d87a4c`；发布只保主导项、次大 stage 标量及最小 A 位置，不存可再生排名表。

可重算 state 不入 Git；记录保留原失败及来源，后续改进不能覆盖此终态。
