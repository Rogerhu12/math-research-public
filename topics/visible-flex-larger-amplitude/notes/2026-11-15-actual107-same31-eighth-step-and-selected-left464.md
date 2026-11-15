# actual107：同31点获得1/8步，最近1/4仍由已建模 LEFT464 拒绝

/root GPT-6 Astra Pro（AI-assisted），2026-11-15。

## 实际接受与完成范围

[run43683739473](https://github.com/Rogerhu12/math-research-public/actions/runs/43683739473)，source `6df3e818bf5acb8e144c1839fb57647c8b3587f4`，job132719696865，实际 wrapper/model/FD 子进程 exit0。原status明确 `accepted_warm_steps=1`、`optimization_progress=true`，但 `success=false`、`new_coupled_finite_acceptance=false`。接受的是原 warm 优化步，未完成全BVP、当前H上的native/fullDN或闭面。

从真实98 warm/status重建同31点完整模型，全部B/H8453、C4059、outside与原预算保持。fresh固定权重目标 `43.363003729098274` 降至 `43.33594286031892`；原实降 `0.02706086877935121`、预测降 `0.026913362440847455`、比值 `1.0054807844552296`，接受步长1/8。旧98的末merit使用另一轮权重，不能与本轮freshW直接相减。

## 完整四档实际试探

| α | 原固定权重目标 | 节点/中点域 | 原RMS | 实际结论 |
|---:|---:|---|---|---|
| 1 | 未形成有限merit | 节点0坏，中点3坏（471/483/487） | 未执行 | 拒绝 |
| 1/2 | 43.35121770838128 | 全合法 | LEFT464/472/483坏，RIGHT0坏 | 拒绝 |
| 1/4 | 43.33703438037944 | 全合法 | 仅LEFT464坏，RIGHT0坏 | 最近被拒档 |
| 1/8 | 43.33594286031892 | 全合法 | LEFT/RIGHT各698点均0坏 | 接受 |

最近1/4的原merit实降 `0.025969348718831498`、比值 `0.4901184851120571`；其唯一RMS坏点已是31点中的query0。位置 `s=1.1553475805065636`，最小 beta² `-0.2683514415128212`，角索引54、φ `0.16566992509164924`，2048角中4个负值、0非有限。它不是缺少一个新query，也不是merit没下降。

半步的LEFT464/472/483 beta²分别 `-1.6567326303518066`、`-0.07884121569005864`、`-0.008966141266157024`；464/472已选，483未选但不是最近失败档，不据远档立即扩大点集。原完整节点、中点及左右RMS继续保留。

接受后31点全部2048角的原最小beta²均正，31个负角计数及非有限计数全0；LEFT/RIGHT各698 RMS点全合法。实际物理collocation最大值 `0.007107481419519517`，仍在interval461/row155819；完整BC最大 `6.857449986338445e-9`，左边界与constant collocation为0。它们仍没有达到原完整BVP目标。

## 原完整 QP 与新warm上的 FD

原候选选择仍为R270-condensed-complete-H。全63488线性行重读可行，最小slack `1.053046538856961e-12`；完整原stationarity L2 `0.003038625816318205`。原下界浮点读数 `43.24758714671914`、跨点gap `3.000998560764856e-9`，都不是validated enclosure或完整QP最优证明，更不是非线性域保证。512 working rows和200 dual sweeps原上限保持。

本次新warm上实际重新执行原边界FD，fourth-order最大相对误差 `8.81884772255149e-10`，second-order `9.88344249574147e-6`，原阈值 `5e-5`，implementation check通过。没有复制旧FD，也没有把原复用锚J解释为当前非零H的完整nonlinear DN；`nonlinear_DN_evaluated=false`、`nonlinear_native_at_current_H_solved=false`、`full_BVP_solved=false`、`full_Cartesian_closed_surface=false`。

独立model与status嵌套模型的7个对应科学字段实际全等，纯读出，不另设科学门。整文档的顶层provenance无需与嵌套模型逐字相同。

## 可重建身份与留存

原summary35131B（含末LF）SHA `42dd12dfab65e25c8e8c7153fb514852bd5832be14f66c5e6fa8ac393f24c491`；原job log72899B SHA `91df357ede0d30f18e3a27e38019e1636938f464c2bce969800665f916d3d663`。

| 原临时输出 | bytes | SHA-256 |
|---|---:|---|
| thirty-one-condensed-warm/model-000.json | 771487 | `ee0298f8dd1806181e535c52c601883fd28618347ec5287ba098729f2268ee51` |
| thirty-one-condensed-warm/driver-status.json | 3591869 | `714347e07a160f56575fc76855fc890b53715923c2920a63a0d268f143a8850b` |
| thirty-one-condensed-warm/condensed-QP-summary.json | 121665 | `7b1e5507369020066b6cecdfbbfaa0e3eabbbf76c285e098b5e1d7183025a252` |
| physical-response/response-check.json | 2825059 | `78dc6fe7cad8cc94877a6c686672a5b9451e27ffa3695b3e89aea946ba090b3d` |
| thirty-one-condensed-warm/warm-001.json.gz | 4938114 | `6d2e5b1c936f874a678a94cdfe44dfc25c45ad18c8b4c01274fbc76e7cf801c1` |

源wrapper `2b4e9f2132263d166d7d4ee298725f55e547427cb1c25c335edf366b4aa784ba`，request `f508c1e5e5396b5f9a9a927703557e89cd24542d16ddd4a74774aa780121c545`。父98原artifact14147700690，809042943B/SHA `9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a`，只解压真正warm/status两件；原四输入由918fdb11历史按身份临时恢复。科学步骤前实际pull/read6df3e818并推规则记录d5719655，双README未变。

原完整raw已在本runner消费后清理，不上传Git、artifact或Release。root只读取实际摘要/日志与hash，没有重算数学。不能由以上hash恢复新warm场或伪造继承。

## 继续同31点的真实批次

继续110：最近阻碍是已经建模的LEFT464非线性RMS，先保持同31。新job须从真实98 artifact开始一条新重算轨迹；只有每批实际产生接受warm、其原paired status及该新warm上的原FD完成，才将原字节送下一批。原107只可作读取对照，不冒从已删除107 raw续接。每批仍保原独立W、所有域/RMS/FD/预算及完整B/H/C/outside，不预设收敛或跳过失败。
