# 按根规矩15普通移出可重算的旧数组报告

2026-11-20 09:44 UTC，Astra-larger-resume-24b2ab87-20261120。

本题当前受 Git 跟踪的文件为199909266 B，距离十进制200 MB上限只剩90734 B；为保存新的真实闭面求解源码，按根README第15条普通删除一份旧可重算输出，不改写历史。

唯一移出的路径是 `notes/2026-11-13-root-R168-M20-root-coordinates-r1.json`，993245 B，SHA256 `4d360e79d8e082786a73e7aa0d43c48391bcf7601011c8cdaafdf3d5d64d8fbf`。它是R168完整217个保存节点的坐标/根/诊断数组报告，不是作者源码或证明。R168的数学正文、原生成源码、输入manifest、launch-plan、resource与日志全部保留。

原生成器是 `computations/root_R168_M20_actual_root_coordinates.mjs`（源SHA `00123a49cb84baf5fb68f393d699b7a2774b11318405b1a4108b0db4c1a4cc88`）；参数为原M20、全部217节点、原quadrature512。完整参数/环境/输入身份见 `notes/2026-11-13-root-R168-launch-plan.json` 与 `notes/2026-11-13-root-R168-input-manifest.json`，后者原SHA `91353af602d3839514c143f2a2cf8a03c440d82e0d4b8b3adeb527935ffd981a`。原运行是11/13本地计算，不补造Actions run编号。

如旧R169/R177或其他历史消费者确需原完整逐字数组，使用固定历史恢复到scratch：

```sh
git show 2d56baaaa5811d345ff2e70fcc5b26e44e3d4823:topics/visible-flex-larger-amplitude/notes/2026-11-13-root-R168-M20-root-coordinates-r1.json > /tmp/R168-root-coordinates.json
```

先核上面的SHA，再把该消费者的本地输入路径指到恢复文件；不以不存在的当前路径或单个SHA假装有数据。历史manifest中的路径/数字作为历史记录保持，不声称这些消费者已经全部无引用或自动运行成功。

本次当前fullclosed恢复/求解不使用R168报告，其独立输入链在11/20恢复记录。此容量操作没有改变任何已证明/数值/失败结论，也没有重新计算R168。一次定位搜索不慎命中了旧报告的超长单行，工具输出已截断；未把截断内容当作完整科学输入，后续搜索限制行宽/文件大小。

## 11:41 UTC：第二次容量操作，R33高块报告

新连续闭面源码/证明使受跟踪总量再次接近十进制200MB。普通移出
`notes/2026-11-12-tail-r33-plateau2-quadratic-high-recovered-r1.json`，
833398 B，SHA256 `51496d1d7307ea491a4e8a9aef22756745bf6c9ca92f8fc9ab1b364deae41e27`。
它是213个高块（cell12至224）的可重算逐胞半径/诊断，不是源码或证明。
原结果只重加权，没有新ODE；高块各gate为真不代表未付低块反馈/整个闭合问题完成。
原本地运行约2.15914秒，arb192位，未补造Actions run。

保留的原生成器 `computations/tail_r33_quadratic_high_box.py`，
SHA256 `25f75d8ac5049eedf408d7caa952eeca5953b12229038454853caa7d2904174b`，
与原报告所记执行源完全相同。依赖的 `closure_real_head_source_enclosure.py`
和 `closure_real_head_green_enclosure.py` 继续保留。原参数
`--z-log2 -2200 --infinite-radius-log2 -120`。三个完整输入为：

| 输入 | SHA256 |
|---|---|
| `2026-11-12-tail-r33-plateau2-density-window.json.gz` | `0b493a5278ce08d12ed1d83add9dd3214125d971e746c750dfa42efa0729ace9` |
| `2026-11-12-tail-r33-plateau2-middle-causal-box-v2.json.gz` | `07c428b0c1a1977985200172dbee0bf14ae57e5fd4ea97ddebdf9b671479b3e6` |
| `2026-11-12-tail-r33-plateau2-high-joint-coupling-metric.json` | `d7e57f6a7df2b928dd6de9aa8ad0289538134e104f57f6960f9b423c72927bbc` |

前两个输入之前已从当前main移出；固定公开历史
`8ef38046e8b04adc6da1093c0730e1fc8747c2c9`
仍有逐字gzip（Git blob分别 `e0f0dbee70503b828f2722cf56bc2f2884731d4b`、
`e9e1063af8f0d02a138915509313f490453260da`）；第三件仍在当前notes。
本次移出的报告在当前父与该历史中都是同一blob
`fe47bcc09e7446eac76fd96f34750d2dc7342820`。历史原字恢复与复算示例：

```sh
mkdir -p /tmp/r33-recovered
for name in 2026-11-12-tail-r33-plateau2-density-window.json.gz 2026-11-12-tail-r33-plateau2-middle-causal-box-v2.json.gz 2026-11-12-tail-r33-plateau2-quadratic-high-recovered-r1.json; do
  git show 8ef38046e8b04adc6da1093c0730e1fc8747c2c9:topics/visible-flex-larger-amplitude/notes/$name > /tmp/r33-recovered/$name
done
python topics/visible-flex-larger-amplitude/computations/tail_r33_quadratic_high_box.py   --density /tmp/r33-recovered/2026-11-12-tail-r33-plateau2-density-window.json.gz   --middle /tmp/r33-recovered/2026-11-12-tail-r33-plateau2-middle-causal-box-v2.json.gz   --joint-reference topics/visible-flex-larger-amplitude/notes/2026-11-12-tail-r33-plateau2-high-joint-coupling-metric.json   --z-log2 -2200 --infinite-radius-log2 -120   --out /tmp/r33-recovered/new-high.json
```

复算前先核输入SHA；加载器按原压缩字节算SHA，再解压JSON。
重新生成的路径/计时字段可不同，若要逐字原SHA应使用上述历史恢复。
旧 `inner_original_window_gamma_replay.py` 的reference-high和
`closure_recovery2_preflight.py` 的默认high还引用此报告；复跑这些历史消费者时
显式传入恢复到scratch的路径。本次不声称没有旧引用，不声称重跑了旧R33，
不删除其数学结论、源、参数或输入身份。当前fullclosed链不使用此报告。
