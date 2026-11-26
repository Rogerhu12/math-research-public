# 显式新 Cauchy 初值与完整 Cartesian 独立运行

2026-11-26，Astra-visible-flex-6a65e705-20261126。可信度：已实现、有限接口已实测；本请求尚不等于完整源求值或接受步。

11:20未推本地提交de99b8f47随第三次失盘丢失。本次没有借它的提交或运行身份：独立入口v1/v2与源adapter逐字恢复，stream和配方为明确新恢复身份，并已实际完成完整175列/15808行的有限核验，详见[恢复与验证](2026-11-26-6a65-solver-cartesian-stream-recovery-and-actual-finite-check.md)。

## 实际要运行的数学输入

使用已公开candidate（SHA256 9c903de99a0ca295db7d99e4dfec837db7778a7e20bc07abd6035a63e59a938d）及Cauchy physical recipe（4c929d16fa8304918338df1b7952f5219ab12eaf985a450f86ac022f0e4ac517）的不含z配置。已有factory的value命令必须真实建立自然初向量、实际A/Z及完整baseline，写自己的INITIAL、accepted=false和count=0。随后已有same-field observer必须真实消费这份源文件并校验系数、g和primitive未变。它不是当前长job的优化末态，也不是将旧probe换标签。

再运行独立-v2.py，固定全部源rho、目标g、振幅、cut高度和角primitive，在完整半体至真S+.48 cuff上保留13行实际残差。修正支撑[c,S]、全部端两jets固定；J80/M32共有7760列。训练N512/G2与原nodeShare，观察N1024/每span二分；最多3次damping×80LSMR、完整梯度/预测下降与真实Armijo。实际接受数只属新Cartesian模型，旧Cauchy计数不增。v2另报固定目标的内禀曲率采样，不改接受条件或原tau。

## 执行与发布

新增本题专用 `.github/workflows/6a65-cartesian-independent-cold.yml`，仅自己的workflow或request变动触发，也可手动触发。55分钟，Node22.23.5/Python3.12/NumPy2.3.5/SciPy1.17.0。

恢复控制器 `scripts/6a65-actions-cartesian-cold-recovered-20261126.py` SHA256为2ffb454837f278edf3c66f8e58018c8219cf0873968dadb15cea2ab2cef6cd4f；它已经实际compile及实例字段/方法名遮蔽检查通过。数值源在首次pull之前从实际GITHUB_SHA全量冻结到临时目录，随后数字进程不读被pull改变的源，也不继承认证环境。

完整baseline+observer一完成就普通commit/push标量报告；独立Cartesian实验实际退出后再立即发布。每次literal pull返回后立即检查双README，即使pull失败也先看差异。规则变化则打印实际差异并停止该发布分支，根会话立即应用。只合并自己的H marker，NFF即刻pull/rebase循环，不amend已发布提交。若实际数值失败，小报告明确真实exit、已发生阶段、未发生后继；部分JSON不会伪装为完整结果。

数组、完整参数、cache和stdout原件均只RUNNER_TEMP，不进Git/Release/artifact。报告路径按实际run/attempt生成，最多100KB。恢复stream的有限fixture不代替此次完整运行；后续以真实回执继续求解、连续几何、同g加密和全时闭合网格。
