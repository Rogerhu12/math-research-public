# root 复核：固定目标的末端误差后验门

2026-11-09，Astra-visible-flex-db6f0b0e。**PASS，明确为已有完整连续证书的条件式组合。未来正常候选分支尚未实际运行。**

root 全文读 `db6f-audit-terminal-error-gate.py`（SHA256
`1be7add52ec2c06653a2a64baa8653e675559a55551cf22603d14a80f9cfb234`）及
`audit-terminal-error-gate-method.md`；另读 coupled 的正常入口定向独审。
没有新 root、flow、solver、几何导出或区间后端运行。

## 1. 数学合成

同一实际图的前缀对源目标有完整界 $\epsilon$，精确目标变化界为 $\eta$。
使用已审变更度量不等式，$U_p=\epsilon(1+\eta)+\eta$。源码从 source 字段
取 $\epsilon$，对 angular 已转移字段只作相等检查，不再把它当 source。
angular 的 source 最大值是若干已向外包围 binary64 上界的最大值，故仍是
其中一个精确 binary Fraction；与兼容浮点字段的精确相等门有效。

尾部两个完整界若都属于同一 manifest、同一目标，可取其最小值；它们均
须覆盖全尾及 collar。最终误差上界是前缀、尾及零误差固定帽的最大值。
源代码精确重算这些算术，并与 closed-budget、whole 逐一连接。曲率独立
来自同一个新图的 prefix/tail 证书，不能由 metric-only 输出代付。

旧 M12 实际误差不小于已审点界
$L=370012576184137/18889465931478580854784$。
root 独立用 Fraction 复算 $B=1/500000000$、$F=195883/20000$ 后得
$$
L-FB=\frac{61863470598928509}{23058430092136939520000000000000}>0.
$$
因此新图若有 $0\le\mathcal E_{new}\le U\le B$，则
$\mathcal E_{12}\ge L>FU\ge F\mathcal E_{new}$。
该乘法证明也覆盖新误差为零；无需假设其严格正或对它作除法。

## 2. 对象与目标身份

实际 prefix、metric、moment 绑定同一个最终 common-cut 图；base/target/
bridge 的文件联系独立核对。prefix profile、chart、warp gauge 和已审源
保持旧目标，而候选未知量 $q$ 和各离散系数可变化。

bridge 的旧支持网格可不同于最终实际尾网格，但必须按其 SHA 显式给出，
并核实际 checkpoint 与全部非数值参数；原 exact cut/唯一根/目标定义不变。
任何旧支持图的 metric 或曲率都不会转用。六个固定背景定义和原校准/alpha
文件各自 pin 原身份；参数比较区分键缺失、null 和布尔/数字类型。

实际 tail、其完整曲率包和可选完整 metric-only 包全部绑定最终 manifest；
后者保留前者的同图曲率，不混入 M12 曲率。完整覆盖标记、数量、范围和
文件 hash 都有核查；这些核查仍依赖已审证书的逐行覆盖证明及实际重跑，
不是重新验证所有叶盒的独立数值内核。

## 3. 可宣称与不可宣称的结果

真实 M12 负向模式单独核冻结对象及标量拒绝，不因旧schema放宽未来正常
入口。它证明旧 M12 实际误差确已超过末端目标，不能凭继续收紧旧图的
估计达到该门。root 没有额外重跑该负向程序；实际执行状态以执行者的闭件记录为准。

正常入口的未来成功仅支付一个完整末端误差上界及一次严格实际下降。
它不自动证明固定几何收敛序列、全部 README 条件、最终端到端独立复跑
或无限精确解存在；程序保留这些总完成标记为 false。后续必须使用真实
最终候选，实际执行正常入口，再由原完整研究流程支付其余门槛。
