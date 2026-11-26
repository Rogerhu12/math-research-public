# R582：区分物理可行性与辅助上界的 97q 真实续接

日期：2026-11-27。会话：Astra-new-mechanism-1f4a61a4-20261127。
状态：新源码与实际输入已准备；本地只作源码、AST、JSON 和 SHA256 处理，没有 import 科学源码、数值求解或旧门重跑。结果须由本次公开 Actions 的真实运行给出。

## 1. 为什么改变原 callback

[已读取的原终态](2026-11-27-r582-current-rows-first-original-terminal.md)来自 run `45856511629` / job `140036193500`、source `389151351f3334fb90bb29bbb506b307891f9417`。
前次实际49个后端点的全行违约都超过 $10^{-8}$，没有任何 optimizer callback fine；保留q和真实metric仍未改变。
后端原日志没有分开物理几何违约与两组metric epigraph违约，因此没有给“全因epigraph欠量”的结论。本次在真实新续算里分组读取同一全行向量，直接据实际物理违约决定操作。

改动有两项，服务于同一次继续求解：

1. 原未完成求解的最后raw q作为明确未合格warm trial；真正保留态仍是通过完整fine的旧q。后端BFGS工作数组没有输出，不声称恢复了它们；新后端从末trial重建内部状态，避免从旧保留q重演49步。
2. 对每个新raw q，先区分物理行与两组metric上界行。物理行合格时精确抬升辅助epigraph；物理行不合格时向真正保留q做有限二分回溯，再抬升该新q的epigraph。所有候选仍通过全部原行、盒和完整fine后才可能接受。

## 2. 两种输入身份均来自同一公开 FINAL

真实保留q binary64 SHA256：
`eb37b419ccb59cfca020b21290953ebf36353984dc409ede51832991e9e19635`。
其完整fine资格为 $\eta=.0004334870087785436$、工作几何违约 $1.2869696627837435\cdot10^{-12}$。

未合格warm q binary64 SHA256：
`f8394b8406fd1725df626a2653f18f14507e71c37f2fbeca44b8192457859dcb`。
原epigraph为 $3.446624594355867\cdot10^{-5}$，全行违约 $2.2103241421139958\cdot10^{-6}$；原fine没有读取，不能继承保留q的资格。

实际约束网 $189\times1536$，完整fine $10942\times3072$，原trust 2不变。
所有10942圈、3072细角及父未采用的189×3072约束角proposal保留；新角升级仍必须有真实候选的角漏峰见证。径向容量769、约束角容量1536未改变。

新配置284156 B，SHA256
`4311d0a03166ee5b75d51a4e918c073fece1d1c11a9e033b8d1b6bd0c6efea1d`。
其254768 B嵌套父输入逐字保留，SHA256仍为
`bfb95ba6682cc0cf5c97b257af2836db9eae515f1490dd5314219e381d10762b`。
其余新字段只取上述公开FINAL的实际q、末raw trial、网身份、scan、计数与成本，不含任何私有正文。输入随request通过终端git传送，不经集成上传大JSON；raw/完整FINAL不提交。

## 3. 辅助变量修复的准确含义

原metric阶段有8个物理组以及最后两个metric组。除 $\overline E$ 的189行外，每个组通过原四点角轨道取最小，保留全部原不等式。两组metric共

$$
N_m=2n_r(n_\theta/4+1)
$$

行，位于原 `Rows.fun` 的末尾。新程序只按这一已固定顺序拆分，不删除任何行。
对原 $(q,e)$，记末 $N_m$ 行的最小值为 $m$。令

$$
e^*=e+\max(0,-m)+\operatorname{pad},\qquad
\operatorname{pad}=16\epsilon_{\rm mach}\max(1,|e|,\max(0,-m)).
$$

按原 `NonlinearRows.groups` 的公式，两组metric行关于e的系数恒为1，其余物理行与e无关。因此在精确算术中抬升e不改变任何物理行，并清掉metric上界欠量。实现不把浮点行向量直接平移后当合格，而是调用原 `Rows.fun(q,e*)` 重新构造原全部行，并检查同一个 $10^{-8}$ 容差和完整原盒；同q时能命中的几何cache只按原cache复用。

此处抬升的是辅助上界，不是修改表面，也没有降低metric要求。只有该粗网真实上界仍小于当前保留态的完整fine误差，才为候选付下一次fine扫描；接受时再次使用完整fine实际 $\eta$，不使用 $e^*$。

## 4. 物理回溯、完整fine及原后端

若raw q的物理行不合格，对同一实际保留态 $q_b$ 依次尝试

$$q_j=q_b+2^{-j}(q_{\rm raw}-q_b),\qquad j=0,\ldots,16.$$

回溯中的每个q都调用原完整行算子；原参数盒和本次固定信赖盒均须满足。两端在同一盒中时线段也在盒中，但实现仍读真实盒违约。q通过物理行后，按上节取得原全部行合格的 $(q_j,e_j^*)$，再支付全部10942及后续保留点上的fine。

完整fine的曲率余量、球、条带、正高、det、$\overline E$、镜像必要条件和实际metric严格改进规则全部沿用。原几何容差 $10^{-8}$、曲率工作余量 $.001$ 均未放松；没有用较小观察网替代原fine。
真实漏峰仍按原公式产生pending与必要ExchangeGrid，完整资格和后端内部状态分别保留。

raw SLSQP向量不被callback改写；单独评估的回溯q不会偷偷替换它。未发生必要网交换或阶段完成时原SLSQP继续迭代，已接受的完整fine q仅更新独立best/retained记录。原自然OptimizeResult若返回也独立记录，不能把回溯点称作它。记录分别给raw q identity、回溯比例、抬升量、评估q identity、原行违约、fine状态和真实接受情况。

首次warm trial在新求解中也经过同一过程；这个必要评估不是重做旧fine，因为源从未对该q作过完整fine。原当前网/实际保留q的10942×3072完整fine可以按严格字面身份复用；任意p/q/网变化均须新资格。

## 5. 运行文件、成本与尚未完成的门

- `scripts/r582_physical_epigraph_continuation_20261127.py`。
- `computations/request-r582-physical-epigraph-20261127.json`。
- `.github/workflows/visible-r582-physical-epigraph-20261127.yml`，单lane `physical-epigraph97`。

沿用固定Python/NumPy/SciPy版本、25个来源绑定、实际双库pull和README/QUEUE核对。只做本地AST和真实JSON身份核对，不执行帮助命令触发科学import。科学上限2400秒、预留30秒，job上限50分钟；原记录说明clock可能在后端单次工作后返回，真实耗时原样计入，不截断为名义值。

同口内部场没有保存，因此本次必要dense/material/核心与高度重建仍全部是新费用。新计数区分物理回溯行读取、抬升后完整行读取、真正fine、metric无改进而省去fine、后端Jacobian、自然返回及warm入口。原2422.614817932秒、778.9737511349998秒Jacobian及全部嵌套来源成本完整保留；计时口径不混加。

当前97维物理模型、参数AD、全部空间jets、固定p阶段目标和向目标p=.8的顺序没有改变。既有97q方向核、七点诊断和旧49步不重播。此次也没有取得固定g精化、连续reference/nonround reach、宏观幅度或精确存在的资格；只有本次真实接受才能改变当前数值状态，主课题继续。
