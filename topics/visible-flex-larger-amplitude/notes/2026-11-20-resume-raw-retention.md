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
