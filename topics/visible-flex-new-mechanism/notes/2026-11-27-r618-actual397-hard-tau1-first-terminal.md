# R618：实际397硬 τ=1 首次固定 E 范围的真实均值根失败

日期：2026-11-27；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

## 1. 唯一原运行与终态身份

原 run [45914497186](https://github.com/Rogerhu12/math-research-public/actions/runs/45914497186)，
job [140230360702](https://github.com/Rogerhu12/math-research-public/actions/runs/45914497186/job/140230360702)，
source `414b7662f8cddf8a06fb9aa5595cadd69e05ca3c`。
job 于 2026-11-27 **00:03:38 UTC** 开始，**00:04:53 UTC** 自然结束，
Actions conclusion 为 success；科学状态必须取下面的原 FINAL，不能把该 conclusion 当成求根成功。

自然完成后只获取一次完整原 job log，本地只解析原日志、JSON及hash。
原 log 为 `384718 B`，SHA-256
`3672c10cb8c31e121270c68b27b4669a231f47fa78d63b81bc62c43c2e3037cb`。
唯一 `FIXED_E397_FINAL` JSON 为 `35131 B`，SHA-256
`2b27561b60402679332b45ae8235a02e7aea98a985de8a77c49a0d952bee2856`，
与原 `FIXED_E397_FINAL_IDENTITY` 完全相符。原完整数组及日志留在原 Actions，
不提交第二份大日志或原 response 数组。

本次 request 为 `230526 B`，SHA-256
`24276495f1152df7ee9a8a0d7e3695234f35e22ae4739bf42743532bbbcd3722`；
实际 stdin 为 `185644 B`，SHA-256
`d1d430078dd67777cc6ff972b6a6ec4cfc4262bdd0eb92d48e207df4a9f1e9ea`。
最后发布只更新实际已读双仓规则的 metadata，没有改变科学输入。

## 2. 实际失败发生在首输入的第103个均值根

原状态为
`declared_fixed_E_model_or_numerical_failure_actual_checkpoint`，
本轮实际 science 计时 **41.515274441秒**。
原异常类型 `ArithmeticError`；消息指出：

- 半径 `r=.22277851819887512`；
- 同分支 `lambda` 坐标；
- `same-branch scalar root exhausted its declared iterations`；
- trial 坐标盒循环最终记录的 `last_halfwidth=1.52587890625e-6`。

该最后宽度字段是在失败后的减半操作之后写出的，不能据此声称最后实际尝试盒
就是该半宽。原记录没有保存每一轮内部括号、迭代点或残差，不补造这些数据。

此前确实完成102个 trial 均值根和103个冻结参考目标。新τ1场的完整工作评价
尚未返回，因此没有完整目标值、没有新 Jacobian、没有 QR/SVD、没有接受步，
fine、双直接位置和完整锚定几何也都尚未执行。
`summary=null`、`readout=null`、`partial_readout=null`，
`pending_trial_not_accepted=null`；这些缺失不替换成τ0旧资格或旧fine结果。

最后真实 checkpoint 明确为
`actual_new_hard_tau1_input_before_its_first_physical_evaluation`。
完整1473维 response 仍是前1472项为0、最后 `tau=1`；其JSON为 `5893 B`，SHA-256
`9235b41ebcd2322c2005b542a0548f25db28ee8d2bb0b9cb9b7bcb24b1ebfb4d`。
范数和最大绝对值均为1，接受步数0，下一 damping 仍为 `1e-8`。

**这证明本次数值求根未完成，不证明硬τ1物理分支不存在，也不证明该分支已可解。**
本次没有静默降低τ、修改固定E或缩小原振幅。

## 3. 同一固定目标与真实源的边界

目标仍是实际397完整原参考场的同一个连续turning根，目标SHA
`86da8c603f3d7ed9eb928481f0afe492f10bb209c94bf0ccaf8070c1aa1cd6c5`。
原完整源SHA为
`79e6d6ce708687decd47fb8eb7a9668f8ca2ebf2351b2f3109fd571c6d692f9c`，
原1130q的SHA为
`d76a590766b2323698053321ad84608f17f110c1711c105470d2b876b4920875`。
`H=.5188903877153482`、`amp=1e-5` 均未改变。
本次真实 response model 身份为
`b6e15653663e0bf2e591340888aacfe284ae995c7a89eed182a0482cc4726816`。
另一普通397续算后来的q/H不能回写这个目标。

完整原1129非均值列、全J48独立post与所有2J至96从属项、a1真尾、
全部原工作950点/细网1728点、canonical512高度及固定mean512定义仍在模型中。
因为原评价在第103个均值根中止，没有完成所有这些点的物理读出；
保留定义和实际完成覆盖必须区分。

本次实际生产并打印了真实源合同以及条件帽尾界；合同的
`whole_reference_E` 假设 `.99≤E≤1.01` **只用于整个真实帽端至数值口区间**，
不是整个body、core或全闭面的E范围。
该合同仍只在实际重建的浮点归一值周围取相邻浮点区间；原七类来源误差均未解决，
严格消费器仍会拒绝，不能把条件真尾区间后果称作准确源的误差证书。

## 4. 本轮全部失败成本仍保留

下面是原 FINAL 中实际计数器；同一工作可能被不同模块重复记数，
这些行不是互不相交的总成本分解。

| 原累计计数器 | 本轮值 |
|---|---:|
| science秒 | 41.515274441 |
| 冻结参考根评价/完成径向点/角点 | 125 /103 /52736 |
| trial mean根评价/完成径向点/角点 | 1762 /102 /52224 |
| output径向角点 | 26112 |
| 完整固定E评价尝试/完整height评价尝试 | 1 /2 |
| 完整height径向角点 | 729600 |
| core根评价/目标尝试/完成目标 | 21 /1 /1 |
| core根角点/完整Laurent参数列 | 512 /24 |
| 参考坐标盒尝试/新冻结目标 | 103 /103 |
| trial坐标盒尝试/拒绝/完成均值 | 119 /17 /102 |
| 坐标盒端点评价 | 444 |
| 新core lift积分/integrand查询 | 106 /14868 |
| 真尾径向点/三jet值/float指数下溢观察 | 745 /11400 /231 |
| 真尾完整响应预算列/新Gaussian列界 | 117 /96 |
| 原germ比值界/完整原包络界/原参考系数 | 22 /1 /264 |
| 帽口均值或参数积分界/全尾分支盒 | 2 /1 |
| 真尾anchor生产者/纳入新尾系数/原germ响应系数 | 1 /96 /10 |
| 完整J/QR/SVD/line trial/接受步/直接位置 | 0 /0 /0 /0 /0 /0 |

原 dense 重建是本次真实启动所需，完整费用如下；没有把已付内口再算一遍。

| 原模块计数器 | 本轮值 |
|---|---:|
| seed RHS | 1981646 |
| connector/core basis RHS | 49357 /49214 |
| height RHS/height求积integrand | 8144 /17178 |
| forced connector/core/source | 6077 /5848 /15147 |
| j10…16已付口dense outer RHS/模式数 | 720370 /4 |
| j18…22已付口dense outer/inward RHS/模式数 | 539964 /51 /3 |
| factored查询/新dense径向查询 | 1338 /1335 |
| base basis点/forced basis点/gain空间jet点 | 18391 /950 /70522 |
| compact径向点/三jet值 | 950 /79800 |
| canonical高度cache/冻结tanh评价 | 2 /2 |
| canonical减均值函数/点 | 1 /486400 |
| 冻结tanh点 | 729600 |
| 原core completion评价 | 1 |
| 本次新inner Riccati/DtN RHS | 0 |

j18、20、22各17个inward RHS，outer RHS分别180007、180145、179812；
三者都是真实完成的已付口dense重建，没有隐藏未完成积分器费用。
旧来源实际337→397的4520.668522229001秒、全部60接受/205trial和更早费用
仍随完整源JSON及原FINAL继承；未计为本次新工作，也未删除。

## 5. 这次原终态支持的下一步

当前明确阻塞是同一固定E均值根的数值迭代，而非已经计算出的全S响应方向。
现有 `_root` 只在Newton候选离开开括号时二分；候选仍在括号内时没有
强制括号按固定比例收缩的保证。原终态没有内部轨迹，因此这里只能指出
实现上的进度保证缺口，不能把某一种浮点停滞轨迹冒充已观测事实。

后继应在不改变该E、τ1、振幅、完整行/列和原口定义的前提下，
加入有明确括号收缩保证的同分支求根，再继续真实求解；新算法及全部额外成本
必须另绑公开scope。原已发表源冻结，不改写原失败收据，也不把重复旧门作为入口。

连续均值/参考E/原M与ODE/primitive及角闭合/径向覆盖/曲率/reach仍未付。
本次没有得到固定E优化成功、宏观运动或README完成结论。
