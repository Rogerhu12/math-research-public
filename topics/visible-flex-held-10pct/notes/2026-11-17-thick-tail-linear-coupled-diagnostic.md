# 新题 10% 预算下的固定深度厚尾与共同前缀线性重匹配

## 数值结论与范围

这是一条**线性/采样诊断**，不是非线性存在定理、非线性幅度上界、精确解或闭曲面。保持同一实际深度 160 与 cut 两 jet，改变最前方谷/峰及 warp；没有通过增加层数压低原缺陷。将新尾自己的 DN 值重新代入短前缀求线性共振，避免沿用不匹配的旧端口。

选定 `thick_tail_selected.json` 是实际优化轨迹中的一个明确快照，后续两个独立入口复现该快照得到：

| 量 | 数值 |
|---|---:|
| cut 半径、斜率 | 0.3、0.08 |
| 物理深度 | 160 |
| 尾背景高度 | 0.016920637996259386 |
| 尾首模 DN D2 | 11.902268074721695 |
| 首模线性 T 正支路采样阈值 | 0.0003673798099657655 |
| 背景经线主曲率采样最大值 | 9.998898511031271 |
| 背景周向主曲率采样最大值 | 2.151225344033983 |
| cut 半径、斜率、二阶 jet 误差 | 5.6e-17、2.7e-16、6.0e-15 |
| 重新匹配前缀 delta | 0.17180596162702658 |
| 重新匹配 H1/q | 0.013508801169035745 |
| 前缀背景高度 | 1.2858909311820415 |
| 阈值除以新的 H1/q | 0.027195589406398005 |

这里最后一行只把线性高度诊断换算成线性 core 支撑振幅标度。它没有排除其他非线性支路，也没有断言 q > 0.0272 不存在。厚尾探索给出的正面信息是可以固定 cut 两 jet 大幅改变层的物理高度；本快照及同类有限扫描仍没有把正根线性容量提升到 q=0.16–0.20 所需量级，因此停止在同一有限参数 LP 上细扫。

## 不可变来源与可复现命令

源码均以 `46fe93d4bb708fdfb7935e91b8141ea77586f0d2` 为准；已有 prefix manifest 另从 `8ef38046e8b04adc6da1093c0730e1fc8747c2c9` 取两个历史 checkpoint。源码、历史数据逐文件 SHA-256 写在 manifest。`tail_recovery_manifest.json` 只增加 25 个必要源码/小配置文件，约 148 KB；恢复脚本必须指向用户选择的仓库外 scratch。以下路径由执行者替换：

```bash
python recover_prefix.py --repo REPO --dest SCRATCH --manifest prefix_recovery_manifest.json --endpoints
python recover_prefix.py --repo REPO --dest SCRATCH --manifest tail_recovery_manifest.json --endpoints
node thick_tail_reproduce.mjs SCRATCH/bundle/topics/visible-flexible-closed-surface thick_tail_selected.json SCRATCH/tail-summary.json 64 32
python coupled_tail_linear.py --bundle SCRATCH --diagnostic SCRATCH/tail-summary.json --out SCRATCH/coupled-summary.json
```

最后命令采用 vu=.55、vd=.60、flat ramp=.4、eta=.05、单次环路、末端 `turn_plateau_v1` bridge 的 curvature=4 与 peak_fraction=.5。完整参数在脚本和输出；这是新的 metric 设计筛选，不能称作旧 q18 同 g 加密。

该快照在本地 2026-11-17 运行，Node/NumPy/SciPy 环境不影响以下明确限制：曲率与线性正性仅按每小段 64 步采样，线性尾以 far=32 传递，真实构造深度 160；没有全体 t 的嵌入/reach、非线性尾对接、固定 g 加密或精确圆弧声明。

## 输入、脚本与输出哈希

- `thick_tail_selected.json`: `cc2392b7587004954f3d618b1a6bf21897ad47b3fbcd25e0df3cd72010d7abc4`
- `thick_tail_reproduce.mjs`: `d9b8bea1e0686a9721bcb01b552bfcc230cb57c699a9f4ccd15f62498018e5de`
- `coupled_tail_linear.py`: `6543e33508370849aa5efebeb466db0aa837d0e5652519328645e1efcf028db1`
- `tail_recovery_manifest.json`: `fe44a48ea7773726faa5d2840c8c568ff0596f3e248946783d65f4b9823bd445`
- `thick_tail_reproduced_summary.json`: `6f8b3235f2925f6d5730451a95bad4fd4b91bead3b834e55881c318a96c4c7c7`
- `thick_tail_coupled_summary.json`: `fbccb045af0d4744ce54d5f90aa6906e4deac52920e6cf3348bcb0a8d3a73214`

输出 JSON 可再生，不入库。提交本说明、输入参数、两个短入口与新增依赖 manifest 即可复现。

配置将valleyControls的零后缀按 `valleyControlsPadTo=160` 无损压缩，入口在构造前补零并删除该辅助字段。实际物理参数、完整展开的config和计算未改；不会把160个可省略零作为独立数值数据保存。
