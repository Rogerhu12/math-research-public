# Actions v2：冻结数值源码，控制 checkout 独立拉取

日期：2026-11-28。状态：准备和有限入口核验完成；没有新Actions run、BVP或完整J。本记录接 `2026-11-28-design-actions-continuation-prepared.json`，旧准备来源与旧worker保持原字节。

root审查发现旧准备中一个真实来源隔离风险：数值子进程从控制checkout加载源码，而worker每次pull会改这份磁盘目录。即使已加载的Python对象不变，后续动态import和末尾文件SHA仍可能混合不同提交。因此最终执行入口改为独立v2，不dispatch旧v1。

## 隔离合同

worker在真正pull并检查双README后，取实际HEAD，建立独立detached sparse worktree，只检出本题及Git自动保留的根文件。随后固定该commit，逐个记录实际检出文件的SHA-256，并保留完整本地文件清单。公开小记录只含确切commit/tree、清单SHA、文件数和总字节；不上传清单、原场、矩阵或证书。

新增 `ci_frozen_chain_entry.py` 从这份冻结树执行原70源/物理输入setup，再调用既有 `ci_fresh_design.py`。因此setup、后续数值 `@REPO@`、cwd和GITHUB_WORKSPACE均使用同一固定源码；数值PYTHONPATH移除。`@WORK@`单独指向worker拥有的computation目录。控制checkout继续拉main、检查新规矩、读request并通过终端git发布，不能改冻结树的数值文件。后续同runner命令继续使用并重核这份冻结树；不会静默换成当前main源码。

规则变化仍由控制树立即发现并暂停自己拥有的数值进程组；root读差异并更新已读commit后续算同一真实场。冻结数值源码不冻结本次研究对新规矩的遵守。

## 最终入口与依赖

只启动 `.github/workflows/held10-design-mapped-v2-20261128.yml`，读取 `ci/mapped-design-v2-command.json`。dispatch必须提供root实际读过双README的完整 `read_rules_commit`；request中的null沿用该值。

需要随本次提交的执行依赖为 `ci_terminal_worker_v2.py`、`ci_frozen_chain_entry.py`、`ci_fresh_design.py`、`ci_q_material_recovery.py`，加上述v2 workflow/request和本记录。相邻JSON给出完整路径、文件字节、冻结SHA与准确提交清单。六个共享映射入口已经由root推到 `f1f16aff492595a56091b61a804a7f41d5ff54ad`，本次未修改。

数值路线与前一准备记录相同：完整q恢复和两档q/warp割线、原M24材料恢复、直接M32 bootstrap、完整两源M40/.064与M48/.128初猜，再按原全部门继续 .192/.256/.384/.512/.75/1。原λ≤.128前沿只是必要再生。单个runner的时间限制不代表课题结束；即使λ1有限前缀通过，真正非线性DN和本题其余完成要求仍须继续。

## 已做核验与尚未发生的事实

v2 worker/launcher的compile/help、v2 YAML/request、内嵌Python和shell bash-n均已通过；最终四个Python源按本记录SHA再次仅做语法编译。未执行本地git、未跑新BVP或组J、未dispatch，也没有宣称新runner的资源或数值返回已经获得。root审查后推送并实际dispatch；首run号、冻结commit、真实runner RAM/磁盘及逐项原门返回另记。
