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

## 12:42 UTC：第三次容量操作，R33强M20逐胞高联合盒

为继续保存新的完整求解与连续几何源码，普通移出
`notes/2026-11-12-tail-r33-strong-m20-high-joint-box.json`，657776 B，
SHA256 `708479849d3fa7c4786503bc72844285f5988eef76a9590063a8d13612ff1e29`。
这是213胞高块的可再生数组报告，不是作者源码、原始问题输入或数学证明。
原R33正文、[强M20完整结果说明](2026-11-12-tail-r33-strong-m20-high-response.md)和
[完整重建manifest](2026-11-12-tail-r33-strong-m20-high-response-manifest.json)全部保留。
后者SHA `1e002b64f899ef2bf64163f512be94e185d0f8fbf005da82504f51fa5d7bfd60`，
包含density/local/wide/causal/joint/column的全部源码、完整命令、输入SHA、算术payload SHA及真实运行状态。

本次已逐字核实当前两个执行源仍与原报告相同：
`computations/tail_r33_high_joint_box.py` SHA `0883e4fd68fa2941588236ab6b8e921fb0b0b1b8193aa7fce6f5aeec208386be`；
`computations/tail_r33_refined_high_joint_box.py` SHA `a60eb9ed85b9490cfb54ee1e945457f56972635e945c94d1b1de04048192af34`。
原三个完整直接输入为：

| 输入 | 原SHA256 | 再生责任 |
|---|---|---|
| `strong-m20-density-window.json.gz`（文件名前缀均为`2026-11-12-tail-r33-`） | `3dc23cefdaafb0210548d868d85e5f81f231d9069dcec6670b7684dcbd1eb5a3` | manifest的density完整命令与五个原输入 |
| `strong-m20-middle-causal-box.json.gz` | `77ecd5fc17cb9d0c1290da2f0eb65a64c81262968f14b3596c0dd9d855bb547b` | 原即未提交派生数组；manifest的causal完整命令 |
| `strong-m20-middle-wide-low-density.json.gz` | `d90cfb688f4f1430fc9e7277ddc6ba234ac9a62762e661ab117396e6f4789663` | 原即未提交派生数组；manifest的wide完整命令 |

原arb精度192，z_log2从同一middle载入为−2224，infinite-radius-log2=−96，domain-weight-floor=true。
从本题目录并在scratch复建上述依赖后，原完整joint命令为：

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python computations/tail_r33_refined_high_joint_box.py \
 --density notes/2026-11-12-tail-r33-strong-m20-density-window.json.gz \
 --middle notes/2026-11-12-tail-r33-strong-m20-middle-causal-box.json.gz \
 --wide-hybrid notes/2026-11-12-tail-r33-strong-m20-middle-wide-low-density.json.gz \
 --infinite-radius-log2 -96 --domain-weight-floor \
 --out /tmp/R33-strong-m20-new-joint.json
~~~

源是完整实际执行的adapter加完整base，不以单个SHA代替源码。上游原未提交大数组必须按manifest重建，不能冒称当前仓库已有原文件。
重新计算路径/计时/输入压缩字节字段可不同，纯算术payload比较约定见原manifest；若需要逐字原输出，固定历史恢复最直接：

~~~sh
git show 60592e4f58d80a20e6a575b7d900ec807a9e7374:topics/visible-flex-larger-amplitude/notes/2026-11-12-tail-r33-strong-m20-high-joint-box.json > /tmp/R33-strong-m20-original-joint.json
~~~

该历史blob为`180780ac9ac93ab18ac4411eb5a7c7a71a7a7d0a`；恢复后核上述SHA，
旧`tail_r33_low_to_high_column.py --joint`等消费者显式指向该scratch文件。旧R33/结果说明里的链接和manifest路径是原历史记录，不声称移出后仍能直接打开当前raw路径。
原完整算术报告五个gate均true、failure=null，实际记录3.108668秒；原最终poll退出码未保留，
本次仍不补造exit0，不重跑已结束旧结论、不创建Actions、不改变已证明/失败范围。当前fullclosed链不使用此文件。

## 13:49 UTC：第四次容量操作，R33 plateau2 高联合盒

为公开 Actions 续算完整源码与后继证明腾出空间，普通移出
`notes/2026-11-12-tail-r33-plateau2-high-joint-coupling-metric.json`，657791 B，
SHA256 `d7e57f6a7df2b928dd6de9aa8ad0289538134e104f57f6960f9b423c72927bbc`。
这是213胞可重算高块数组报告，不是源码、原始问题输入或证明。原 R33 §14.3、生成器与全部条件范围保留。
本次只核对字节、源码与来源，没有重跑科学计算。

完整实际执行源为 `computations/tail_r33_high_joint_box.py`
（SHA256 `0883e4fd68fa2941588236ab6b8e921fb0b0b1b8193aa7fce6f5aeec208386be`）
及 `computations/tail_r33_refined_high_joint_box.py`
（SHA256 `a60eb9ed85b9490cfb54ee1e945457f56972635e945c94d1b1de04048192af34`），
两件仍在当前树且逐字匹配原执行源。arb192，`z_log2=-2231` 从同一 middle 继承，
`--infinite-radius-log2 -110 --domain-weight-floor`。完整三个输入为：

| 输入（均在原notes） | SHA256 | 固定历史Git blob |
|---|---|---|
| `2026-11-12-tail-r33-plateau2-density-window.json.gz` | `0b493a5278ce08d12ed1d83add9dd3214125d971e746c750dfa42efa0729ace9` | `e0f0dbee70503b828f2722cf56bc2f2884731d4b` |
| `2026-11-12-tail-r33-plateau2-middle-causal-box-v2.json.gz` | `07c428b0c1a1977985200172dbee0bf14ae57e5fd4ea97ddebdf9b671479b3e6` | `e9e1063af8f0d02a138915509313f490453260da` |
| `2026-11-12-tail-r33-plateau2-middle-wide-low-density.json.gz` | `4c79356c3791dd491fbf5c4222a0051ab0046923718f1f26ba1be09eef1fd089` | `9ee6a92c89d2cf637fdcad5bc9ef6815bf1ac7d8` |

三个输入均已逐字核实可从固定公开历史 `8ef38046e8b04adc6da1093c0730e1fc8747c2c9` 恢复；
本次报告可从 `0e2acb2e1500fdb8f645551af802db43189453f9` 恢复，blob
`d2b2b2dde5c59f3440ca7b4ecee788074d15b994`。精确旧输出恢复及完整复算命令如下；
复算应在公开 Actions 的 scratch 中执行，示例 `r33scratch` 指向该临时目录。

~~~sh
mkdir -p "$r33scratch"
for name in 2026-11-12-tail-r33-plateau2-density-window.json.gz 2026-11-12-tail-r33-plateau2-middle-causal-box-v2.json.gz 2026-11-12-tail-r33-plateau2-middle-wide-low-density.json.gz; do
  git show 8ef38046e8b04adc6da1093c0730e1fc8747c2c9:topics/visible-flex-larger-amplitude/notes/$name > "$r33scratch/$name"
done
git show 0e2acb2e1500fdb8f645551af802db43189453f9:topics/visible-flex-larger-amplitude/notes/2026-11-12-tail-r33-plateau2-high-joint-coupling-metric.json > "$r33scratch/original-joint.json"
python topics/visible-flex-larger-amplitude/computations/tail_r33_refined_high_joint_box.py \
 --density "$r33scratch/2026-11-12-tail-r33-plateau2-density-window.json.gz" \
 --middle "$r33scratch/2026-11-12-tail-r33-plateau2-middle-causal-box-v2.json.gz" \
 --wide-hybrid "$r33scratch/2026-11-12-tail-r33-plateau2-middle-wide-low-density.json.gz" \
 --infinite-radius-log2 -110 --domain-weight-floor \
 --out "$r33scratch/new-joint.json"
~~~

恢复后核上述输入SHA。重新计算的路径、计时等字段可能不同，逐字旧输出应使用固定历史恢复。
原 R33 §14.3 记录本组工具全部正式 exit0；本报告真实耗时 `1.6880759199993918s`、峰值RSS `117812 KiB`，
五个gate均true、failure=null。`low46_held_fixed=true`，`low_feedback_paid=false`，`whole_head_closed=false`：
该结果一直只付条件高块响应，不是全闭合解。

11:41段中“第三件仍在当前notes”是当时状态；自本次普通移出后，旧
`tail_r33_quadratic_high_box.py --joint-reference` 与 `tail_r33_low_to_high_column.py --joint` 等消费者
须显式传入上述恢复到scratch的原报告路径。没有把历史引用伪称成当前可直接打开的raw，
没有改写原结论、历史或输入身份。当前 fullclosed 链不依赖此旧文件。

## 2026-11-20 第五次容量操作：R33 原始联合高盒

本次仅普通移出可重算数组报告 notes/2026-11-12-tail-r33-plateau2-high-joint-box.json，469230 B，SHA256 ba0ea67bdbf503742998f062daa24c047d58fa1260883dddb17d514938f3b614，Git blob8125c86a9f21bd75735515804811545d15ff8e1b。逐字旧文件可从固定公开提交1e7143497538a45d7613059f80aaa1ce0c77af48恢复，scratch副本保留；不改历史、不重算旧结论。当前closed链不依赖此旧报告。

原实际主源computations/tail_r33_high_joint_box.py，6729B，SHA0883e4fd68fa2941588236ab6b8e921fb0b0b1b8193aa7fce6f5aeec208386be仍在当前树。两件import依赖closure_real_head_source_enclosure.py（20321B，SHA97ff78a171b284cd8d5acc8dc233bcfe1f0b7c428ce2fbbd5b7104bd0ecb8c47）、closure_real_head_green_enclosure.py（11896B，SHA4b2e74d07f678e11631c51cf01831a4c1e588e8d207c144e2f1dace8413022e0）也保留。三件已与固定8ef38046e8b04adc6da1093c0730e1fc8747c2c9逐字核对一致。完整两个输入与第四节同名density-window和middle-causal-box-v2；其准确SHA分别0b493a5278ce08d12ed1d83add9dd3214125d971e746c750dfa42efa0729ace9、07c428b0c1a1977985200172dbee0bf14ae57e5fd4ea97ddebdf9b671479b3e6，固定8ef38046e8b04adc6da1093c0730e1fc8747c2c9可逐字恢复，blob也已在第四节给出。

完整参数：arb精度192bit；--infinite-radius-log2 -90；z_log2=-2231由同middle输入继承；没有--domain-weight-floor适配。公开Actions scratch复算完整命令：

~~~sh
mkdir -p "$r33scratch"
for name in 2026-11-12-tail-r33-plateau2-density-window.json.gz 2026-11-12-tail-r33-plateau2-middle-causal-box-v2.json.gz; do
  git show 8ef38046e8b04adc6da1093c0730e1fc8747c2c9:topics/visible-flex-larger-amplitude/notes/$name > "$r33scratch/$name"
done
git show 1e7143497538a45d7613059f80aaa1ce0c77af48:topics/visible-flex-larger-amplitude/notes/2026-11-12-tail-r33-plateau2-high-joint-box.json > "$r33scratch/original-high-joint-box.json"
python topics/visible-flex-larger-amplitude/computations/tail_r33_high_joint_box.py \
 --density "$r33scratch/2026-11-12-tail-r33-plateau2-density-window.json.gz" \
 --middle "$r33scratch/2026-11-12-tail-r33-plateau2-middle-causal-box-v2.json.gz" \
 --infinite-radius-log2 -90 --out "$r33scratch/recomputed-high-joint-box.json"
~~~

恢复先核上述输入SHA；计时与路径可能不同，所以逐字历史输出用git show恢复。旧报告实际2.5392517930004033秒、峰RSS73304KiB，五个gate true且failure null；low46_held_fixed=true、low_feedback_paid=false、whole_head_closed=false，始终仅是固定低46场的条件高块响应。R33既有证明不改。R33 §13的旧raw链接应依本节恢复，不再称当前树可打开；未来消费者若用该旧报告须显式传入scratch恢复路径，完整源码和参数不缺。

## 2026-11-20 第六次容量操作：R33 常strip低源后的旧联合盒

普通移出 notes/2026-11-12-tail-r33-plateau2-high-joint-wide-low.json，657103B，SHA256 7306027ee5e4e1b29cf9881c4962fef1cf6b8894fa4f979973f5d7a78265587f；Git blob0998ee9426c0054011649519b337eb2340ee4eb0。逐字文件已核可从固定公开提交870b797170b94046c25ab4209722265aa8637174恢复，scratch副本保留。当前closed链不依赖它。仅核字节、源和元数据；没有重跑科学结论。

该raw实际adapter SHA为b27785f57335d8e9f288f30132afc25cba51995ad87152e3242b5a5311d8e212，并非当前带domain-weight-floor的a60eb9…版本。此次从当前adapter移除后来新增的floor参数/三行weight替换/输出标签，精确还原2647B原source并核得相同SHA；完整字节另存 computations/tail_r33_refined_high_joint_box_before_floor.py，原文件不改。该恢复只处理源文本，没有执行科学代码。它按同目录载入完整base tail_r33_high_joint_box.py（6729B，SHA0883e4fd68fa2941588236ab6b8e921fb0b0b1b8193aa7fce6f5aeec208386be）；另两import源closure_real_head_source_enclosure.py/closure_real_head_green_enclosure.py的完整字节及SHA已在第五节登记且仍保。不能用只带SHA的说明替代这些完整源。

三个实际输入与第四节完全相同：density-window SHA0b493a5278ce08d12ed1d83add9dd3214125d971e746c750dfa42efa0729ace9；middle-causal-box-v2 SHA07c428b0c1a1977985200172dbee0bf14ae57e5fd4ea97ddebdf9b671479b3e6；middle-wide-low-density SHA4c79356c3791dd491fbf5c4222a0051ab0046923718f1f26ba1be09eef1fd089。本次再次逐字核固定8ef38046e8b04adc6da1093c0730e1fc8747c2c9中的三件输入，其blob与第四节表一致。arb192；infinite-radius-log2=-110直接由raw准确mantissa1/binary_exponent−110确认；z_log2=-2231从同middle继承；这个旧adapter没有domain-weight-floor。

完整恢复与公开Actions scratch复算命令：

~~~sh
mkdir -p "$r33scratch"
for name in 2026-11-12-tail-r33-plateau2-density-window.json.gz 2026-11-12-tail-r33-plateau2-middle-causal-box-v2.json.gz 2026-11-12-tail-r33-plateau2-middle-wide-low-density.json.gz; do
  git show 8ef38046e8b04adc6da1093c0730e1fc8747c2c9:topics/visible-flex-larger-amplitude/notes/$name > "$r33scratch/$name"
done
git show 870b797170b94046c25ab4209722265aa8637174:topics/visible-flex-larger-amplitude/notes/2026-11-12-tail-r33-plateau2-high-joint-wide-low.json > "$r33scratch/original-wide-low-joint.json"
python topics/visible-flex-larger-amplitude/computations/tail_r33_refined_high_joint_box_before_floor.py \
 --density "$r33scratch/2026-11-12-tail-r33-plateau2-density-window.json.gz" \
 --middle "$r33scratch/2026-11-12-tail-r33-plateau2-middle-causal-box-v2.json.gz" \
 --wide-hybrid "$r33scratch/2026-11-12-tail-r33-plateau2-middle-wide-low-density.json.gz" \
 --infinite-radius-log2 -110 --out "$r33scratch/recomputed-wide-low-joint.json"
~~~

恢复核原SHA；复算计时/路径字段可不同，逐字原报告以固定git show恢复。实际旧报告五个gate全true、failure=null，elapsed1.3349231330003022秒、峰RSS117968KiB；phase2-manifest只明记all_jobs_in_this_manifest_exited=true，本条不补造该进程原poll退出码。low46_held_fixed=true、low_feedback_paid=false、whole_head_closed=false，仍只付固定低46的条件高响应，不冒后来的新coupling范数或完整闭解。旧phase2-manifest中的raw路径是历史记录；此后消费者须显式指向上述scratch恢复文件，不能误称当前树仍有raw。

## 第七次容量操作：R33 plateau2 低到高完整列账本

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / geometry_path。

**已普通移出下述可重算旧 raw，原字节保留 scratch，完整公开历史仍可准确恢复。** 已读前六次操作与 R33 §13–14 的上下游。
当前 R33 名下超过300KB的报告只剩 plateau2 与 strong-M20 两份低到高列账本，已没有另一份达到该尺寸的 wide 联合盒。
本次普通移出同一 plateau2 wide/coupling 链的
`notes/2026-11-12-tail-r33-plateau2-low-to-high-coupling-column.json`：

- 568918 B；SHA256 `9bc4a1f2f026958e5f92ef411dd38ee184fcf5a255fb1929774d780b001b3fdb`；
- 固定已核恢复提交 `717d87e6745a54226c6c98cc781dbce10bc7575b`；
- Git blob `69f629bae4c9c1ccce151a594ae275bc13467415`。

它是原胞12至224共213行的可重算导数列账本，不是源码、问题原始定义或证明。
R33 §14.2–14.3、原 phase2 manifest 和完整小源保留。
本次只读取必要元数据、核源码/输入/原输出字节及静态引用，再普通移出该派生 raw；没有科学重跑、没有启动新 Actions、没有历史重写。

### 完整实际源码

主源当前仍逐字匹配原报告的 `source_sha256`。两个直接 import 及一个传递 import 也全部存在，且已与固定公开历史
`8ef38046e8b04adc6da1093c0730e1fc8747c2c9` 逐字核对一致；不需要另造恢复版源码。
四个文件均在 `computations/`：

| 文件 | 字节 | SHA256 | 该历史 Git blob |
|---|---:|---|---|
| `tail_r33_low_to_high_column.py` | 6317 | `77ba11616af520796b5ccd9cab542e64633227cf7086b83360fd2f3fe303f6e3` | `5347816069e2d13352c4fde783ebade0793283bf` |
| `closure_real_head_source_enclosure.py` | 20321 | `97ff78a171b284cd8d5acc8dc233bcfe1f0b7c428ce2fbbd5b7104bd0ecb8c47` | `7fe97d00cdc7271590c8e21bf2f5991c953dcd31` |
| `closure_real_head_green_enclosure.py` | 11896 | `4b2e74d07f678e11631c51cf01831a4c1e588e8d207c144e2f1dace8413022e0` | `d2ecd12c72080f93c435bc43a4de50fcc41043ba` |
| `closure_projective_interval_column.py` | 3594 | `45997a1d5be6326a1ebbe85ac4240ea7d9dde1c2fb6acdf832460dade89e4f97` | `bd0e759f32cc41958d3d0de4279e5c46fbbc56c1` |

最后一件是 green 模块的加载依赖，即使本生成器只消费 green 的 `load_json/ball`，仍需保留完整文件。
除标准库外，这条完整 import 链使用 python-flint。原源准确设置 `ctx.prec=192`；原报告没有另外保存 Python/python-flint 版本，本次不补造版本。

### 五个准确直接输入

文件均在原 `notes/`。表中 joint 使用其另列提交，其余四件均从
`8ef38046e8b04adc6da1093c0730e1fc8747c2c9` 恢复：

| 文件 | SHA256 | 固定 Git blob |
|---|---|---|
| `2026-11-12-tail-r33-plateau2-density-window.json.gz` | `0b493a5278ce08d12ed1d83add9dd3214125d971e746c750dfa42efa0729ace9` | `e0f0dbee70503b828f2722cf56bc2f2884731d4b` |
| `2026-11-12-tail-r33-plateau2-middle-causal-box-v2.json.gz` | `07c428b0c1a1977985200172dbee0bf14ae57e5fd4ea97ddebdf9b671479b3e6` | `e9e1063af8f0d02a138915509313f490453260da` |
| `2026-11-12-tail-r33-plateau2-high-joint-coupling-metric.json` | `d7e57f6a7df2b928dd6de9aa8ad0289538134e104f57f6960f9b423c72927bbc` | `d2b2b2dde5c59f3440ca7b4ecee788074d15b994` |
| `2026-11-12-closure-plateau2-box.json` | `5474b056b5012e290e5efd3bebb2b6f4681b42150a53d03f03b61c55b8c59ceb` | `cb262f7a9df223c4128736aed61d403509a72c65` |
| `2026-11-12-closure-plateau2-nonlinear-low-far-lift.json` | `ba839f5b7c0eb8587ab2ff6bc9985399eceb0eb02d7aa649e83dc47fde2b4da2` | `1acb53bd231e0c4bd022952ee6cc04bc68dae37f` |

joint 的固定恢复提交为 `0e2acb2e1500fdb8f645551af802db43189453f9`；其完整再生源与三个直接输入已在第四次容量操作登记。
必须使用这里的 **coupling-metric** joint，不能把第六次的旧 wide-low joint 当作相同距离权输入。
本次五件均通过固定 commit 的完整原字节 SHA 核对。density、middle、joint 已不在当前 main；low-box、low-far 仍在且逐字匹配上述 SHA。

### 全部实际参数与恢复命令

主源没有额外数值 CLI 开关：五个输入路径与输出路径均为必需参数，Arb精度192bit和原胞12–224是源中的准确常数。
`z_log2=-2231` 从相同 joint 继承；其 `infinite_radius` 的准确端点都是 mantissa1、binary exponent−110。
这些不是本列生成器可以任意重设的隐藏默认值。

以下命令只供未来确需该历史材料时在公开 Actions 的 scratch 执行；本次没有执行科学命令：

~~~sh
mkdir -p "$r33scratch/source" "$r33scratch/inputs"
for name in tail_r33_low_to_high_column.py closure_real_head_source_enclosure.py closure_real_head_green_enclosure.py closure_projective_interval_column.py; do
  git show 8ef38046e8b04adc6da1093c0730e1fc8747c2c9:topics/visible-flex-larger-amplitude/computations/$name > "$r33scratch/source/$name"
done
for name in 2026-11-12-tail-r33-plateau2-density-window.json.gz 2026-11-12-tail-r33-plateau2-middle-causal-box-v2.json.gz 2026-11-12-closure-plateau2-box.json 2026-11-12-closure-plateau2-nonlinear-low-far-lift.json; do
  git show 8ef38046e8b04adc6da1093c0730e1fc8747c2c9:topics/visible-flex-larger-amplitude/notes/$name > "$r33scratch/inputs/$name"
done
git show 0e2acb2e1500fdb8f645551af802db43189453f9:topics/visible-flex-larger-amplitude/notes/2026-11-12-tail-r33-plateau2-high-joint-coupling-metric.json > "$r33scratch/inputs/2026-11-12-tail-r33-plateau2-high-joint-coupling-metric.json"
git show 717d87e6745a54226c6c98cc781dbce10bc7575b:topics/visible-flex-larger-amplitude/notes/2026-11-12-tail-r33-plateau2-low-to-high-coupling-column.json > "$r33scratch/original-low-to-high-column.json"
python "$r33scratch/source/tail_r33_low_to_high_column.py" \
 --density "$r33scratch/inputs/2026-11-12-tail-r33-plateau2-density-window.json.gz" \
 --middle "$r33scratch/inputs/2026-11-12-tail-r33-plateau2-middle-causal-box-v2.json.gz" \
 --joint "$r33scratch/inputs/2026-11-12-tail-r33-plateau2-high-joint-coupling-metric.json" \
 --low-box "$r33scratch/inputs/2026-11-12-closure-plateau2-box.json" \
 --low-far "$r33scratch/inputs/2026-11-12-closure-plateau2-nonlinear-low-far-lift.json" \
 --out "$r33scratch/recomputed-low-to-high-column.json"
~~~

恢复后先核上表源码/输入 SHA。gzip 输入按原压缩字节计算身份，再解压 JSON；不要重新压缩后冒同一输入 SHA。
复算的输入路径、计时和RSS等字段可能不同；要取得逐字原输出，使用固定 `git show` 恢复，不把一次新运行的输出 SHA 预定为历史 SHA。

### 原结论与消费者影响

原报告 `complex_mean_domain_paid=true`、`low_to_high_paid=true`，但
`high_to_low_paid=false`、`full_head_closed=false`。原记录耗时
`0.8076283440004772s`、峰RSS `75000 KiB`，最坏中频胞120。
R33 §14.3 明确记载本组工具均正式退出0，phase2 manifest 记
`all_jobs_in_this_manifest_exited=true`；没有新的运行记录，也没有本公开仓库的旧 run 编号可补写。

本次完整文件名的定向检索得到两个明确历史引用：R33 §14.3 的数据链接与
`notes/2026-11-12-tail-r33-phase2-manifest.json` 的原文件条目。它们应作为历史记录保留，不重写科学结论。
移出后，确需该完整导数列的旧消费者须先按本段恢复到 scratch 并显式传入实际路径；不再称原 raw 链接在当前树仍可打开。
当前 `resume_20261120` 与本轮完整 closed 求解/几何入口无该旧报告的路径引用，其明确输入链也不以该报告为输入。
本操作不将小源、原问题材料或数学证明一起删除，不改写已有提交；root 已执行上述普通移出；释放568918 B后继续当前公开求解与完整几何任务。

## 第八次容量操作：R33 strong M20 低到高完整列账本

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / fullclosed_solver。root已普通移出该可重算旧raw，完整原字节保在scratch；以下记录实际恢复入口及全部再生责任。

本次只普通移出可重算派生报告 `notes/2026-11-12-tail-r33-strong-m20-low-to-high-column.json`，568756 B，SHA256 `f9aef3bff332ad24babf007e8c5e6fd5d58a64a169e8099a8af95b557ffc42bc`。完整原输出的固定公开提交为 `46c0db11b34296b7c05223842f7d34594fb66ab9`，Git blob `92c0edb20a05059cfb639c374e72a5751326e488`；本次已核当前完整原字节摘要及该历史 blob 身份。它是胞12–224共213行的导数列账本，不是原始问题、源码或证明。R33 §17、[原强 M20 说明](2026-11-12-tail-r33-strong-m20-high-response.md)及[完整重建 manifest](2026-11-12-tail-r33-strong-m20-high-response-manifest.json)全部保留，不改原结论。

### 完整源与五个直接输入

主源 `computations/tail_r33_low_to_high_column.py` 6317 B，SHA256 `77ba11616af520796b5ccd9cab542e64633227cf7086b83360fd2f3fe303f6e3`，仍在当前树并与原执行源逐字相同。完整仓库 import 链为 `closure_real_head_source_enclosure.py`、`closure_real_head_green_enclosure.py`、`closure_projective_interval_column.py`；连同主源的完整 SHA/固定历史 blob 已在第七次容量操作登记，四件均继续保留。外部算术依赖为 python-flint；不补造原报告未记录的 Python/python-flint 版本。

本次另逐字核 manifest 的全部11件生成源码，当前均与原 manifest SHA 相同；因此 density/local/wide/causal/joint/column 的完整生成链仍有真实源文件，不能用只有 SHA 的清单代替源码。最短 middle 重建使用的三个额外源为：

| 源文件，均在 `computations/` | 字节 | SHA256 |
|---|---:|---|
| `tail_r33_middle_wide_low_density.py` | 3769 | `b0d80bbd21d51d5f2de04bc66293f28470ec6d6a236c7bfdfea5e0fa396af336` |
| `tail_r33_middle_hybrid_density.py` | 9430 | `465b2a6a6cb5e28fd2f35ddbf489e0f3594348b66ba844468526523136c1b8fc` |
| `tail_r33_middle_causal_box.py` | 11768 | `9b9c5b5fd0c76a853dc07aa6c4f5ceaea54594e445e961320c7debf3bd867346` |

五个原直接输入的完整身份如下，文件名前缀/路径不省略：

| 输入，均在原 `notes/` | 原 SHA256 | 原字恢复方式 |
|---|---|---|
| `2026-11-12-tail-r33-strong-m20-density-window.json.gz` | `3dc23cefdaafb0210548d868d85e5f81f231d9069dcec6670b7684dcbd1eb5a3` | 240299 B；固定 `8ef38046e8b04adc6da1093c0730e1fc8747c2c9`；blob `05cdc755c012a328b8531b6a4433125b3854b0b1` |
| `2026-11-12-tail-r33-strong-m20-middle-causal-box.json.gz` | `77ecd5fc17cb9d0c1290da2f0eb65a64c81262968f14b3596c0dd9d855bb547b` | 原1978834 B，原即未提交；必须按下述 manifest 链重建，不声称有 Git 原字 blob |
| `2026-11-12-tail-r33-strong-m20-high-joint-box.json` | `708479849d3fa7c4786503bc72844285f5988eef76a9590063a8d13612ff1e29` | 657776 B；固定 `60592e4f58d80a20e6a575b7d900ec807a9e7374`；blob `180780ac9ac93ab18ac4411eb5a7c7a71a7a7d0a` |
| `2026-11-12-closure-newg-strong-m20-real-box.json` | `81f8f89aa5ca4ce18d4ea55c33e5fc0d63a8f1776090725af0ab032bc2e703c7` | 当前590044 B逐字匹配；固定 `8ef38046e8b04adc6da1093c0730e1fc8747c2c9`；blob `6a9b14728d0b3d7538c41c5fcfdc4a982c9356be` |
| `2026-11-12-closure-newg-strong-m20-real-low-far-lift.json` | `41bc0b2407ea83415be43363e212bac2024b1c5d0c9d80fa6684a6d6abe9c2e3` | 当前305825 B逐字匹配；同一 `8ef38046e8b04adc6da1093c0730e1fc8747c2c9`；blob `3ed049d03e242200162e7b9fb2d16054dd8e0c24` |

density 的定向 `git log` 明确记录原加入提交 `8ef38046e8b04adc6da1093c0730e1fc8747c2c9`，后由 `2be1ad966256bc04307f67d86ebabcc21e27d686` 普通移出。本次已实际核上述 density 原压缩字节 SHA；不再猜测 joint 的 `60592…` 提交也含 density。density、middle、joint 当前均不在 main，不能把历史路径说成当前仍可打开。

### 原未提交 middle 的完整恢复路径

完整 manifest 的 `rebuild_order` 是 density→local→wide→causal→joint→column，已包含每段完整命令、源/输入 SHA 和算术 payload SHA。为取得本列的五个输入，最短路径是先恢复已有历史 density、local 及下列固定材料，只新生成原未提交的 wide 和 causal；joint 使用上表的准确原文件，无需重跑已完成联合盒。

以下五件上游原字节本次也已从固定 `8ef38046e8b04adc6da1093c0730e1fc8747c2c9` 核对，与 manifest 全部相同：

| 原文件名，均在 `notes/` | SHA256 | Git blob |
|---|---|---|
| `2026-11-12-closure-positive-highband-38.json.gz` | `cf293799252e8beb9ef15ff27dba1ebbe698186cee3258b6f9df34ab8dff5600` | `1bb3cb191977a335488553c70b6e502ed32490eb` |
| `2026-11-12-closure-middle-high-subhead24.json.gz` | `33acb8d33185b539fef61bbcf91b9d46422625e50fef5101039b858a4e603948` | `2181fca42b2f0447358e0ccbee433c54498975c4` |
| `2026-11-12-tail-r33-strong-m20-middle-local-homogeneous.json.gz` | `799031c1cd3442c46fac1a0a958fbfa11cf9767dadf2388586509418bb63b2d3` | `05483c8d97481ade4ff2be3f275a6134e2a38b3f` |
| `2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json` | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` | `4fa8a8a7ae5d482cd0eaf35790db85201bbac4a3` |
| `2026-11-12-closure-middle-high-subhead16to23.json.gz` | `ae75b84ff4e9a55e5ba538a3651c71d0e3dcd19344aac35249ca553d3438b03b` | `65421d003e4f178cb92833bb9defb3cfcadeafb7` |

wide 原压缩 SHA 为 `d90cfb688f4f1430fc9e7277ddc6ba234ac9a62762e661ab117396e6f4789663`，原算术 payload SHA 为 `33a5437fb63561cfd39db55d22567b49ba484486e57eeb74df5eafffd1ad8838`；causal 的原算术 payload SHA 为 `59212b299a86aa4f98a7bd191083b36f0b6938d137192e9d75035401860889c5`。两件原均明确未提交，不能捏造历史 blob。新运行计时/RSS/输入摘要及压缩字节可能不同，须按 manifest 给出的完整 payload 规则比较算术内容；本次没有运行或宣称新文件已通过这些比较。

### 全部参数及公开 Actions scratch 命令

主列源只有五个输入路径和 `--out`，没有额外数值 CLI 开关；Arb 精度为源中固定192bit，胞12–224共213行。`z_log2=-2224` 与无限半径 $2^{-96}$ 由准确 strong-M20 joint 继承，不可换成第七次 plateau2 的 −2231/−110。原联合盒用 `--domain-weight-floor`，但本列没有这个 CLI 参数。

以下仅为未来确需旧材料时的完整恢复/复算命令，本次未执行科学步骤。`r33scratch` 是 Actions 的独立 scratch 目录。源码先逐字核上述 SHA 与 manifest，再使用当前保留的完整小源；输入原字按固定历史恢复：

~~~sh
r33src="$REPO/topics/visible-flex-larger-amplitude/computations"
r33in="$r33scratch/inputs"
mkdir -p "$r33in"
for name in 2026-11-12-tail-r33-strong-m20-density-window.json.gz 2026-11-12-tail-r33-strong-m20-middle-local-homogeneous.json.gz 2026-11-12-closure-positive-highband-38.json.gz 2026-11-12-closure-middle-high-subhead24.json.gz 2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json 2026-11-12-closure-middle-high-subhead16to23.json.gz 2026-11-12-closure-newg-strong-m20-real-box.json 2026-11-12-closure-newg-strong-m20-real-low-far-lift.json; do
  git show 8ef38046e8b04adc6da1093c0730e1fc8747c2c9:topics/visible-flex-larger-amplitude/notes/$name > "$r33in/$name"
done
git show 60592e4f58d80a20e6a575b7d900ec807a9e7374:topics/visible-flex-larger-amplitude/notes/2026-11-12-tail-r33-strong-m20-high-joint-box.json > "$r33in/2026-11-12-tail-r33-strong-m20-high-joint-box.json"
git show 46c0db11b34296b7c05223842f7d34594fb66ab9:topics/visible-flex-larger-amplitude/notes/2026-11-12-tail-r33-strong-m20-low-to-high-column.json > "$r33scratch/original-strong-m20-low-to-high-column.json"
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python "$r33src/tail_r33_middle_wide_low_density.py" \
 --density "$r33in/2026-11-12-tail-r33-strong-m20-density-window.json.gz" \
 --positive "$r33in/2026-11-12-closure-positive-highband-38.json.gz" \
 --subhead "$r33in/2026-11-12-closure-middle-high-subhead24.json.gz" \
 --local "$r33in/2026-11-12-tail-r33-strong-m20-middle-local-homogeneous.json.gz" \
 --ready "$r33in/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json" \
 --extra-positive "$r33in/2026-11-12-closure-middle-high-subhead16to23.json.gz" \
 --out "$r33in/2026-11-12-tail-r33-strong-m20-middle-wide-low-density.json.gz"
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python "$r33src/tail_r33_middle_causal_box.py" \
 --density "$r33in/2026-11-12-tail-r33-strong-m20-density-window.json.gz" \
 --positive "$r33in/2026-11-12-closure-positive-highband-38.json.gz" \
 --subhead "$r33in/2026-11-12-closure-middle-high-subhead24.json.gz" \
 --local "$r33in/2026-11-12-tail-r33-strong-m20-middle-local-homogeneous.json.gz" \
 --hybrid "$r33in/2026-11-12-tail-r33-strong-m20-middle-wide-low-density.json.gz" \
 --ready "$r33in/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json" \
 --extra-positive "$r33in/2026-11-12-closure-middle-high-subhead16to23.json.gz" \
 --z-log2 -2224 \
 --out "$r33in/2026-11-12-tail-r33-strong-m20-middle-causal-box.json.gz"
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python "$r33src/tail_r33_low_to_high_column.py" \
 --density "$r33in/2026-11-12-tail-r33-strong-m20-density-window.json.gz" \
 --middle "$r33in/2026-11-12-tail-r33-strong-m20-middle-causal-box.json.gz" \
 --joint "$r33in/2026-11-12-tail-r33-strong-m20-high-joint-box.json" \
 --low-box "$r33in/2026-11-12-closure-newg-strong-m20-real-box.json" \
 --low-far "$r33in/2026-11-12-closure-newg-strong-m20-real-low-far-lift.json" \
 --out "$r33scratch/recomputed-strong-m20-low-to-high-column.json"
~~~

需要逐字原列时只用上述固定 `git show`，无需生成 middle。不得把新复算输出预定为旧完整 SHA；本列原算术 payload SHA 为 `d0a21e1d4a7a6ca06b32eaf582768ddc57afa325b0559bd8dc66579aac6016d8`，其排除字段/序列化规则在完整 manifest 中保留。

### 原状态与现有引用

原列 `low_to_high_paid=true`、`high_to_low_paid=false`、`full_head_closed=false`；最坏中频胞100。原实际 session26802 正式退出0，耗时 `0.7507356370006164s`，峰RSS `74788 KiB`。joint2606 的退出码原未保存，完整 JSON 已有五门通过；本次不将它补写为 exit0。

完整文件名定向检索仅得到三件历史引用文件：R33 §17、原强 M20 说明、完整强 M20 manifest。它们按原状态保留，不把数据链接改写成新的科学结论。移出后确需原列的消费者须先恢复 scratch 并显式传真实路径；当前 `scripts/resume_20261120` 与 `.github` 中没有该文件的路径引用，当前完整闭面求解/几何链不以它为输入。

本次只是必要元数据/源码/输入身份和静态引用核查，没有重算旧结论、没有科学导入执行、没有删除源码或证明，也没有历史重写。单件普通移出释放568756 B；新增说明和后继小源占用另计。

## 2026-11-26 06:38 UTC：第九次容量操作，R39实际线性参考逐胞数组

本轮完整新g/固定g/连续证书源码使本题跟踪总量达到199348151 B。普通移出旧可重算输出 `notes/2026-11-12-closure-newg-strong-m20-real-reference.json`（648675 B，SHA256 `d87a6862836c31f9cb72ed9b8ad74c0ee618797e45a83785c8206a83455233cb`），不改历史。该报告有213个完整cell rows及46个endpoint rows；其线性参考的全部已有结论保R39正文，不是非线性闭合、数值轨道认证或本轮新计算。

新增紧凑[保留记录](../computations/resume-20261126-legacy-R39-reference-retention.json)逐字保原检查、参数、全部输入/源码SHA及小标量界，仅删逐胞/逐模数组。生成器 `computations/closure_rebase_actual_reference.py`、两依赖、原resource完整argv、原ready/response与46列组身份均保留；原记录为11/12本地运行、exit0、wall 2.2512502670288086秒，不补造Actions run。当前相同源码是否仍在由紧凑记录列出真实SHA，不能假定源码路径即原字节。

旧消费者需要完整原数组时，先从固定历史恢复到scratch并核SHA：

```sh
git show 0a5c529f01b4eba31856ba7f551b3cbbe06f9634:topics/visible-flex-larger-amplitude/notes/2026-11-12-closure-newg-strong-m20-real-reference.json > /tmp/R39-real-reference.json
```

其后明确将旧消费者输入指向此文件；历史manifest路径照保，不声称所有旧消费者已无引用。原完整生成命令仍在 `notes/2026-11-12-closure-newg-strong-m20-real-reference-resource.json`；今后若重算，按现规矩只在公开Actions执行并把raw留runner。当前实际输入再生已完成28阶段，本轮后继使用该run自身field/carrier和永久点；此移出没有改变其实际数据或数学目标。

## 2026-11-26 07:59 UTC：第十次容量操作，R39实际low46逐胞固定点盒

本轮在题目约199.58 MB时普通移出旧可重算输出 `notes/2026-11-12-closure-newg-strong-m20-real-box.json`（590044 B，SHA256 `81f8f89aa5ca4ce18d4ea55c33e5fc0d63a8f1776090725af0ab032bc2e703c7`），仅去213个完整胞row。全部已有标量门、误差范围、完整modes/公式/参数、源和三个输入SHA、原resource argv与真实exit0保 [紧凑记录](../computations/resume-20261126-legacy-R39-box-retention.json)。本轮只是复制既有元数据，没有重跑旧数学。R39正文和历史消费者原样保留，不改写其辅助低46/线性远边界范围为完整非线性闭合。

原逐字报告可从普通历史恢复：

```sh
git show db01d7c63c549c333319cbd51c9660c9c05782f3:topics/visible-flex-larger-amplitude/notes/2026-11-12-closure-newg-strong-m20-real-box.json > /tmp/R39-real-box.json
```

原三个输入的固定恢复提交与SHA逐字验证已完成：Green取8ef38046、reference取0a5c529f，ready仍在当前树；紧凑记录保完整40位提交号。今后确需重新计算，在Actions独立scratch复制原相对`notes/`路径、原完整生成器`closure_anisotropic_low46_box.py`及两依赖，再用原argv和明确precision192。Green检查器以原相对路径为身份键，不能随意换绝对路径后假称源失效。旧resource真实wall2.2743313312530518秒、exit0、峰RSS44652KiB；无旧Actions编号或已记录runtime版本，不虚构。

当前run已经真实再生28阶段，v2幅度/新深谷入口用自身原场和scalar数据，此旧辅助盒不是其输入。其他旧消费者需要该原数组时必须先恢复到scratch并显式接入；未删除任何源码/证明或改写历史。

## 2026-11-26 08:18 UTC：第十一次容量操作，旧plateau2辅助low46逐胞盒

本题已接近199.68 MB，普通移出原可重算`notes/2026-11-12-closure-plateau2-box.json`，589775 B、SHA256 `5474b056b5012e290e5efd3bebb2b6f4681b42150a53d03f03b61c55b8c59ceb`。只去213个生成row；所有旧scalar门、完整46 modes、公式/参数、源/输入SHA、完整原resource argv保 [紧凑记录](../computations/resume-20261126-legacy-plateau2-box-retention.json)。旧参考和所有源仍保留，未动证明/旧消费者/任何历史提交。

原数组逐字恢复：

```sh
git show a026c36124a8134e3cf2b8aefbf1833589530487:topics/visible-flex-larger-amplitude/notes/2026-11-12-closure-plateau2-box.json > /tmp/plateau2-real-box.json
```

Green输入已从固定8ef38046历史逐字核验，参考和ready为当前保留字节；全部40位恢复提交与摘要保紧凑记录。原实际resource为本地wall2.118471622467041秒、exit0、峰RSS44764KiB，无旧Actions号或已记录runtime版本；不虚构。主源cde09c4a及两完整依赖、原precision192/完整三个输入/原相对路径身份要求保留，若需要再生只能Actions执行并留raw于runner。本次仅metadata复制/字节核验，没有重算旧结果。当前新固定gn、幅度SOC及旧g face的实际输入不依赖此辅助盒。

## 2026-11-26 08:39 UTC：第十二次容量操作，旧plateau2参考逐胞数组

当前题约199.45 MB，普通移出旧可重算 `notes/2026-11-12-closure-plateau2-reference.json`（566084 B / `0e8fcd3ee16f27262389a91647b129b3c2f520c0b36d33a20bad580fa9fa8fb5`），仅去213个cell_rows。全部其余标量/区间字段、原完整resource命令、默认precision192/relative-radius1/500/far-strip38/far-log2-ball−2200、三源和八个输入逐字SHA及恢复提交保[紧凑记录](../computations/resume-20261126-legacy-plateau2-reference-retention.json)。八输入均从固定8ef38046历史再次逐字核验；三源当前字节均匹配。只读复制元数据及SHA，无科学重算。

```sh
git show 83de126ff488566899e7aa0dc4bdbdbf6a942fb6:topics/visible-flex-larger-amplitude/notes/2026-11-12-closure-plateau2-reference.json > /tmp/plateau2-reference.json
```

原本地resource真实wall2.5225894451141357秒、exit0、峰RSS85272KiB；旧Python/python-flint版本没有记录，不虚构。未来若消费者需要原数组，先恢复原相对路径至Actions隔离scratch，按已保完整源/argv生成；raw只留runner，不改旧证明或历史。当前新deep/幅度/旧g face输入均不依赖这份旧辅助参考。

同时把当前run已实际返回的stage50–60共11项summary字段映射完整移至[第二份映射存档](../computations/resume-20261126-returned-summary-fields-02.json)；活跃queue的全部id、源、argv、父、输出、清理和scope逐值保留，仅这些已返项summary改空。恢复规则/原queue SHA/固定提交及每项真实stage均保，未删除任何执行步骤或科学参数。

## 2026-11-26 09:41:03 UTC：第十三次容量操作，旧 outward M160 完整系数轨道

普通移出可重算旧输出 `notes/alternative-outward-coast-m160-end09.json`（942804 B，SHA256 `0b44c331e2309209ebc7c82948b7e4db7dbd5a2b71887d42c923c7366afe7705`，blob `5a97e189282c305c286dc62d2393018faf67b8e5`），完整原字节留scratch/固定历史。保留[紧凑记录](../computations/resume-20261126-legacy-outward-m160-retention.json)的全部原非数组字段、首末row、原provenance条目及完整重生argv；原provenance summary不改，尤其保留这次M160高模污染的失败精化结论，不将其隐藏或改作不存在证明。没有科学重算。

记录原source c35f3e47与当前cf163a5c不同。本次从当前完整源码纯文字逆掉后来加入的XYZ诊断转换，所得7581B完整源SHA准确匹配 `c35f3e47bbadc01b30a528096273eae47b367d961c08917c744fb9c094188fd8`；已保存为 `computations/resume-20261126-legacy-alternative-outward-probe.py`，只AST/compile、没有导入科学执行。原report对该旧误名诊断作了键重命名；紧凑记录完整保留该后处理，不把当前已修正诊断源假称原执行源。两源均保留。

原输入是源码内完整解析core与profile，无外部数组。A=.38/M160/N2560/v=.5/S1/amax1.35/rtol1e−9/steps60/maxstep.0003/end_s.9/coast_at.8/coast_length.1全部保；依赖NumPy/SciPy与单线程BLAS设置源内完整。原elapsed69.29625940322876秒/status success/calls42120如实保留；没有记录旧OS exit或Python/NumPy/SciPy版本，不补造旧Actions号。以后如确需科学再生，仅在本公开Actions按完整argv执行，raw只留runner。精确原字节直接恢复：

```sh
git show e95fea50651bcfe32aad52826caa8a692c2ff741:topics/visible-flex-larger-amplitude/notes/alternative-outward-coast-m160-end09.json > /tmp/outward-m160-original.json
```

完整文件名定向搜索只找到原 `alternative-provenance-summary.json`，该历史引用照保；旧消费者要完整轨道时先恢复scratch。当前两代resume求解/几何及请求不使用该路径。只移出61套完整系数状态/482末系数和逐行数组；原标量结论、完整小源、参数和历史均保留，不改已有提交。
