# own fixed QR：完整 CSR 预映射、实际来源分支与原数值门

**可信度：必要执行修复及真实导入/编译/CLI 检查已完成；没有新的 fixed BVP、native 返回或曲面证书。** 此时尚无真正的 QR anchor / own fixed 阳性场，已有准备记录保留其当时源码 SHA，不回写为本版本。

## 1. 改动针对的真实问题

严格 R87 设计线的同 $\lambda=.032/M24$ 计算在完整五个 Newton 步后收到原因未证实的 $-9$，后继以同一完整状态、同方程和全部原门，经完整 CSR 在 QR 前映射及因子映射真实通过。因此不能假定未来更大的 fixed / full-DN 计算继续使用匿名 CSR 会自动足够。

旧 qr_fixed_support_actual_resources.py 原样保留，仍是 RHS64/Jac32 和 factor-only mmap。新独立 [qr_fixed_support_actual_prefactor_resources.py](../scripts/resume_20261128/analytic/qr_fixed_support_actual_prefactor_resources.py) 通过显式 --resource-mode prefactor 选择：RHS/Jacobian 都分成八节点批次，所有节点、状态、支持参数、原 $q$ 参数列及完整边界仍计算；矩阵在 QR 之前完整映射，全部因子在原 QR 构造后完整映射。没有删行、删列、改变方程或只解局部系统。

step 默认仍可走原 factor-only 分支；首次 fixed launcher 默认显式传 prefactor。真实 argv、来源文件、resource_mode、资源方法和退出清理均匹配所选分支，不把新执行贴成旧 64/32/factor-only 记录。

## 2. 完整预算与两次接触矩阵后的释放

[新预算](../scripts/resume_20261128/analytic/fixed_support_prefactor_memory_budget.py)直接使用已运行的 complete_prefactor_memory_budget.py。原 Jacobian 分块/完整 CSR 组装峰、QR 构造峰以及完整矩阵与因子在热 solve 中同时驻留的峰均保留。另对 fixed Flow 加 $512$ MiB 独立余量，另保 $512$ MiB 外部 RAM 余量与实际 backing 之外的 $512$ MiB 磁盘余量。这是执行估计，不是已证明的内存上界或中断原因。

只用当时实测匿名 RSS 抵扣；完整 CSR 已映射，因此也不能像旧 factor-only 分支那样将 CSR 字节记作匿名 RSS。映射逻辑字节不会再次加到 MemAvailable。

原完整 QR 求解和原全矩阵残差观察保留。这个观察在 solve 已清页以后再次读取 CSR，故新分支在该观察结束后**再次实际释放 CSR 与因子两组存储**；两组均须真实报告 MADV_DONTNEED 成功，才回到原非线性工作。所有构造和热 solve 峰仍支付，未宣称清页消除了全部峰。

原 owner 继续真正等待 child 终态并回收所有自有成员；之后按显式模式调用原 factor-only 或既有 complete-storage 清理器。清理器只删除该真实 child 的带 owner/hash 的临时映射目录，原场、检查点和证明证据不在删除范围。

## 3. 原数学和两种真实 anchor 身份

fixed 模型 KIND、原支持族、fixed=True 构造器、完整未知空间、真实 $\delta$、gauge、profile、warp、chart、全 mean、GL6、全尾背景及所有 physical-H 门保持。数值接受仍是原 RMS、BC、physical BC、完整 metric、native4/chord3、全部八次 outer 与真实 final physical-H；storage 不构成数学收敛或逆界证明。

来源现在明确区分：

| 真实 inner schema | 实际 reader | 实际 source kind |
|---|---|---|
| original-lambda-one-native4-chord3-outer8-prefix-qr-v1 | qr_actual_coupled_prefix.py | actual_lambda_one_qr_chord_final_physical_height |
| original-lambda-one-native4-chord3-outer8-prefix-mapped-qr-v1 | mapped_qr_actual_coupled_prefix.py | actual_lambda_one_mapped_qr_chord_final_physical_height |

每条都调用其实际完整 reader，核自身 summary/command/source/所有完整物理门。fixed_problem.anchor_source_kind 与其真实 provenance 一致，后继始终继承同一字面完整 fixed problem；不会修改 anchor 原记录。

own fixed 的 complete-tail producer 和 C² 比较器只更新实际 reader/model/acceptance 版本绑定。新 mapped anchor 后先做 own fixed1 → own fixed2 的同问题比较；旧 anonymous anchor 的 continuous provider 不接受新 mapped anchor 冒名输入。该限制不影响两份真正 own fixed 场的完整比较，也不把任何准备记录当成数学阳性。

## 4. 实际检查及边界

十个新/更新 Python 源已实际编译。实际导入新资源、预算、模型与已有完整 BeforeQRMappedBlockQR；三个真实 CLI help 全部 exit 0，step 和首次 launcher 均展示两个显式资源选项。没有构造矩阵、调用 BVP/native 或传假 accepted 对象。

逐字源码比较另实际返回 0：

- 六个核心模型/完整高度函数原字节相同。
- 从 obj.initial(par) 起的完整实际 DN 科学后缀，在仅恢复被选资源变量名后逐字相同；包含全 native、八次 outer、原接受门、保存场与最终物理 H。
- 接受器的原数值/来源场验证主段逐字相同；变化限于显式来源身份与资源合同分支。
- 全尾比较器的十四个原函数/类和生产器的六个原函数逐字相同；未改全谱、共同半径分割、公共两jet或任何区间计算。

完整原→新 SHA、真实工具终态、函数段 SHA 与实际 import/help 回执见[同名 JSON](2026-11-28-qr-fixed-complete-prefactor-resource-and-provider.json)。这只为真正新输入准备可执行路径；仍须从真 $\lambda=1$、全非线性 DN、同一完整 $g$ 精化到各项连续证书实际完成。
