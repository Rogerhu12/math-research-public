# 实际113首跑：历史输入读取在首快照前失败

2026-11-15，ChatGPT /root（GPT-6 Astra Pro，AI-assisted）。**这是实际工程失败，不是 binary128 数值试验结果；课题与113科学比较均未完成。**

## 原运行与身份

公开仓库 [run43687907457](https://github.com/Rogerhu12/math-research-public/actions/runs/43687907457)，计算 job132732158878，源码提交 `7308ea262f596e4caf1cf49ab7c16cdca6a7f504`，06:59:42 UTC 创建，最终 failure / exit2。执行入口与全部参数见[113完整接口](2026-11-15-complete-binary128-native-primal-experiment-interface.md)：同actual91原输入、原32次迭代/十档/tol2e−9，完整129248残差的两个binary128 root配置、7200s独立child预算均未修改。

实际 setup 回读的 C++ / bridge / probe SHA 分别是 `1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d`、`3655c81a5771deaa26a0d22b8fc4bbbead0302cd06983ddd4f5d12eded44ebe8`、`ba3564ca6ef5329326861a66a948292280e2ab9e311eb8912c11d4e24d7d8409`。编译已成功；实际 executable SHA 为 `91efd6f2984be486609928cc1c0112bbe5fa268ae8e7ebe3f37dc57c040b0196`。

读取的完整原 job log 为65777B、SHA256 `a5e0a15ade430c551f6df14e2846824a52ebdd8167f620e92021912726284c37`。原 `native113_final` 事件报告 summary SHA `942b3c55b2096951c8cffcac31365a808a2493fee4e57157494a48b1ffa1cf47`，original result SHA `bd6789bd11d47c8005334d2129cc524912706f51df96bff7fe5c93b4069a9e9d`；原response receipt/scalars均null。可重算完整输出及日志不提交Git/Release。

## 实际停止位置

原驱动仍执行 `git show HEAD:topics/visible-flex-larger-amplitude/notes/2026-11-13-strong-m28-recovered-full-audit-r1-ready.json`，该文件已随104普通数据清理从main移除；Git实际返回128和path不存在。原结果记录 `CalledProcessError(128, ...)`、elapsed `0.28494221799999764` 秒；外层入口elapsed `6.110566640999991` 秒。

原loop结束事件的snapshots、directions、residual全部null。尚未建立freshJ/R273方向，更未进入binary128的base或十档评价。`native_accepted=false`、`success=false`只是本次入口未成功，不能解释成128方向被拒、根精度失败或新的数值底线。

同job规则监控已实际pull，在07:00:38 UTC读main `c25d932903645cb82084158eaa737c0a8cd8ec51` 并推规则记录 `f1401d6ef2607fdac059809616f930678f3d1171`；两README保持当前已读blob。

清理阶段删除了113科学临时树和公开原源码临时树；只读actual91父临时树删除报 `PermissionError(13)`。这是另一个准确记录的清理问题，不是此次入口停止原因，也不是native验收条件。

## 直接修复边界

下一版本只把旧驱动的历史输入读取接到公开仓库准确历史对象/原真实artifact，并逐项检查同类输入；源参数与原SHA合同继续保留，数据只在Actions临时恢复，不重新写入main。对该request自己拥有的只读临时父树修正属主写权限后清理。不得用新造数据替换，也不改三层科学门或把本次空结果当锚。修复发布后重跑113以取得原本尚未发生的比较；110和115继续独立推进。
