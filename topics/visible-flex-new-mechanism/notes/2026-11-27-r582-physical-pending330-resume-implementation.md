# 97q：准确3bc1与原pending330的正常完整物理续算

2026-11-27，会话 `Astra-new-mechanism-1f4a61a4-20261127`。
这是原自然终态的必要后继输入与薄wrapper；只有本地文本/AST/JSON/hash和原日志解析，
没有本地优化、ODE、FFT、科学探针或旧诊断回放。

## 1. 接哪一个真实点

原normal311 run
[45909167191](https://github.com/Rogerhu12/math-research-public/actions/runs/45909167191)，
job `140213091600`，source `181de62c735dfa087cd62e842c191c7d226f4e0a`，
实际runtime pull `08e0b93016a795fd312f83db96ff07f444810bbd`。
其新材料实际为0d，完整支付入口16167以及后来新网；末真保留q是
`3bc11a9c80696ad3ec54066a9bf0d5cee4436081dee79b9e22b61757fe507aa1`，
eta `3.722676721935829e-5`。完整原证据和8次接受见
[normal311原终态收据](2026-11-27-r582-normal311-original-terminal.md)。

| 原输入 | 已付事实 |
|---|---|
| 实际材料mesh SHA | `0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991` |
| 真保留q资格fine | 16189×3072，物理违反0、工作违反 `2.3094850684635126e-12` |
| 原当前required fine | 与这份资格同一16189数组 |
| 原当前coarse | 327，1536角 |
| 原pending径向 | `.230712890625`, `.249609375`, `.25532226562500004` |
| 原拟定下一coarse | 准确330，1536角 |
| 当前/拟定trust | 2 / 2 |
| p / epsilon | `.181` / `.0010000000000000009` |

当前327的SHA为
`6c55a5e61e09146bd8972348a3176db35ee585985b46667128b041ef0e05b440`；
拟定330的SHA为
`d67124b1f5d7e01959036ff617ba269dd1189373cc89c663cc87c3af88f3a0da`；
源永久fine SHA为
`d6a0d6e71af4341f2ce4c64723c124835071ca1f7148fda7278c3dd053f17ccb`。
新输入保留每个原binary64坐标，按原driver采用源明确提出的三个pending点。
不能把拟定330说成源run已经优化过的实际网。

末raw候选 `135e3bccf8ee50fc816c3acad03a9928b67cfcc0323ea20035a4591dff064e72`
没有完整fine，原完整当前行违反 `1.428317347522942e-6`。
它只按原算法保留为未合格warm候选，不能顶替真best。
原最后完整scan就是从另一个raw候选half-step得到的3bc1，其e为
`3.7226767222911544e-5`；所有身份仍分开。

## 2. 为什么这个入口必须完整付新fine

原driver的 `reused_initial` 条件比较p、q、fine数组和角数、完整scan标记；
它**没有一个独立比较材料mesh SHA的通用分支**。此范围不宣称存在该分支。

这里有更直接的原输入依据：准确330的相邻中点中，下列六个坐标不在原16189 fine：

| 原330相邻中点新增值 |
|---|
| `.2278564453125` |
| `.2325439453125` |
| `.248876953125` |
| `.2513671875` |
| `.25422363281250004` |
| `.25642089843750004` |

这是对原JSON坐标的必要输入核对，没有求新科学场。
原driver仍取永久fine、实际material observation点、新coarse与全部相邻中点的并集。
因此首次新fine必异于源16189，至少保留其16189点并增加这六点。
实际重建材料若另有新观测点也继续加入；最终真实节点数/identity以新run原START为准，
不提前伪造一个“已经合格16195”的记录。

这保证同一个新构造field对象上完整支付首次新fine资格，即便实际重建材料与原mesh不同，
也不借旧3bc1的fine通过结果。新mesh、必要ODE、Hermite端点、稳定cells和全部准备费照实输出。
现有字段虽然名为 `material_mesh_binary64_sha256`，原构造器实际计算的是
`SHA256(material_knots.tobytes() + values.tobytes())`，其中values包含每个节点的
完整六分量 `A, A_s, A_ss, C, C_s, C_ss`。因此它已绑定节点和全部端点数据，
在同一已绑定源码下标识共同端点定义的数学Hermite场，无须另造一个重复哈希接口。
原base的入口reuse判据仍没有比较这个字段；本scope的安全复用边界由六个新中点明确给出。
本段后续全部coarse、fine、AD及原物理门使用这同一个实际对象。

若原入口完整观察不满足工作物理门，原driver进入geometry restoration；
若合格，则继续metric phase。原phase门、目标、所有boxes、trust、独立epigraph抬升、
物理回溯、当前完整行、全fine、8个物理组和raw/best分轨都不改。

## 3. 这里只换必要输入，不改科学实现

新wrapper先核已发normal311 source和request，再让原父load_input恢复固定材料seed、
冻结reference q、完整参数和历史成本。然后只以唯一原FINAL里的3bc1、327/330、16189、
三点pending、原未合格raw和实际剩余费用替换后继状态。
原物理driver、field、StableField、tail columns、NonlinearRows和FineObserver全部保持源字节。

原normal311四个backend分别已有2 / 6 / 2 / 4份J，三次实际交换；原native有机会进行
内部MODEM1更新。它与B03022次首J后交换的形态不同。
本范围继续这个已经实际下降的原98维后端，不把独立82维native曲率helper改常量接上。
原未输出H/workspace不恢复、不猜；这不消除其已经支付的历史成本。

`initial_radial_nodes=298`等旧字面参数照原request保留；续算的真实网来自原FINAL明确的
330数组，而不是用该旧基数重新生成一个网。所有原1536角、3072 fine角和永久坐标都保留。

## 4. 本段原费用全部继承

本scope继承原normal311新科学 `2427.43645062` 秒，及其完整prior ledger。
完成outer计数中的10J/130方向块/53 value，与第四backend未折入outer的
4J/52块/44 value分列保留：实际总共14完整J、182块、97 value。
不只引用completed outer计数而丢掉当前backend。

原17份完整fine / 2159 blocks / 275020径向点、13次callback scan、42次物理行回溯观察、
8次真接受、960944 dense RHS / 1023386 weight / 2510 core RHS / 206短尾RHS /
235893高度RHS、全部稳定Hermite准备与旧primitive成本原样存在。
新field的必要重建、各新网baseline、实际full J、value line search、回溯、全fine和失败尝试
继续计入本次新clock；旧方向检查、七点诊断和24/48/96拟合不回放。

单lane、单并发job，maximum_seconds=2400、final_reserve_seconds=30。
每个实际原子操作耗时和真正elapsed照实记，未闭工作不伪记为已完成J或完整scan。
原数学/优化接受阈值不变。原stalled/capacity/clock终态都只作可继承状态，
不是达到课题完成标准。

3bc1的mean q[64:80]和q[96]已不同于具有完整连续reach证书的59a4；
本scope不消费59a4的连续范数或mean参考reach作为新q资格，也不作固定g或精确族声明。
这些独立历史几何费用和结论仍在原收据与课题总账中保留。

## 5. 原字节与新冻结文件

原stdout 7220660 B，SHA-256
`9726268200ac107dbd7c7c411e13b33cba913522bb1663b7930f66c0a4985d0a`。
唯一原FINAL 506334 B，SHA-256
`23bef2fbc32807204c2ee2c3bebbb646ccd740642c95de117289809504b282d7`。
新必要输入保留其原字节，不复制整份原stdout入库。

| 新文件或stdin | 字节 | SHA-256 |
|---|---:|---|
| `scripts/r582_physical_pending330_resume_20261127.py` | 12325 | `fffe47880d413b52f9fabd4bd963e4ec9ea51af925444dd8eb42436894e5124d` |
| `computations/request-r582-physical-pending330-resume-20261127.json` | 529785 | `7f518dcf0d11e0071615049087d9472ad46340e0f18c5629802191b38e327da4` |
| `.github/workflows/visible-r582-physical-pending330-resume-20261127.yml` | 6087 | `3df3570f06259acfac8426ccb3e6f7bb4fc8081627175fb1fc63829ef95f4eaf` |
| 完整stdin | 510950 | `8f8d55778bce0d655b970ca004dbadcef9f8eaa3f9383a5ea56b30de7e174b94` |

39条文件绑定和原FINAL逐字、正确matrix lane `actual-3bc1-0d-pending330`，
已作本地文本/AST/JSON/hash核对；没有执行科学入口。
规则metadata为root00:01 UTC实际拉取并读过的public
`7ad798390451dda805da35f99eb1c232d4a935a3`、private
`724f5769d39c1f05826ed6c36792a5bb66da6aa0`，README差异均空。
新request的push触发原串行97q并发组，不额外dispatch。
