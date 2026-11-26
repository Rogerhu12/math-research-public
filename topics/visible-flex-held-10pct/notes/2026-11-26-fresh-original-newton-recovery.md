# 独立恢复真实锚后的一次原 Newton 方向诊断

会话 `Astra-held10-06bbeb39-20261126`，2026-11-26。

现有 warm runner 的同一父链继续自然运行，原单方向诊断仍排在其后。该 worker 不支持在活动父链内另启请求，且有既定作业期限。为获得可用于继续求解的真实方向数据，新建独立 probe 通道；不以排队状态代替执行。

入口为 `scripts/resume_20261126/seam_recover_original_newton_probe.py`，SHA256 `5ab5b0a2b485e9de8ff4c4dbb25601867eae6bdc3cb99ac8c4734ed139e1624c`。其 port、q=.006→.06、λ0完整lift、λ=.002 M8/M16/M24块与实际成功的 `lowq_prefix_recovery_design.py`（`a69f5c6c…`）逐字相同，6801 bytes/SHA `c6eb048d90ffa2863234455b68c324a43869ff7a5a10b88a6d2c7141dcc4dd9a`。chart及物理域绑定也保留。只有原metric单失败的完整M8/M16可作升模初猜；最终M24必须通过原solver/RMS/BC/完整metric门。

M24返回后，入口只准备明确未求解、未接受的旧接口模型规格，用原 `warm_handoff_equivalence_probe.py --skip-jacobian-probe` 重算全部零控制raw方程、核心和两jet身份，再走原v2、v3同图转换。没有复用旧95cf锚的identity文件，也不为取得记录而重跑v1暖BVP。随后调用已冻结 `d9b3a7ad…` 单方向诊断：λ=.004、原全局LU、21个原缩步值、原域/merit、同LU有限方向差；不更新一次Newton场。

启动命令：

```text
python -u REPO/topics/visible-flex-held-10pct/scripts/resume_20261126/seam_recover_original_newton_probe.py --repo REPO --work WORK --outdir WORK/fresh-one-direction
```

新输入在本runner从真实求解产生，chart和全部field重新绑定，不断言与旧warm锚逐位同一。数组仅留runner；输出只登记命令、SHA和小标量。原wrapper仅新增 `probe` 通道选择；其他通道行为不变。新workflow保原350分钟/同数值依赖和规则检查，无暖12次继续或δ继续。

本地已实际compile/help成功，并核新prepare规格与原loader字段兼容；尚未有本次实际方向结果。实际run号及返回另追加。

## 实际启动

[run45806625263](https://github.com/Rogerhu12/math-research-public/actions/runs/45806625263) 已于11:00:51 UTC启动，源提交 `d8097620e49e74f070b657c44958505eddacb9f4`；工作目录 `/home/runner/work/_temp/held10-probe`。没有把启动记为方向结果。
