# 原完整两轮呈示的 24 条新均值像：实际来源检查点

作者：OpenAI ChatGPT /root 与 normal_annihilator（GPT-6 Astra Pro）；2026-11-16。

## 1. 本次实际完成的范围

[至多两轮稳定的完整210列呈示](../results/R150-appendix-original-parameter-stable-closure-stops-at-two-and-complete210-presentation.md)在原已付106列之外还需四条保留路径作用于26个低种子。本次实际完成其中全部24条均值像：
$$
N_pN_qY_j,\qquad
(p,q)\in\{(1,4),(2,3),(2,4),(3,4)\},\quad 0\le j<6.
$$
每条向量均保留全部十个坐标，参数权为9；每条来源均保留全部原十八坐标，其中 Bell 坐标严格为零。系数仅为原合法剩余点 $\mathbf F_{127}$、$d=100$，没有特征零提升。

另外80条交换子二次像由独立的 final 阶段继续；本检查点只确认24条均值像，完整210条的实际生产结论须另有完成回执。本次未建立新的加权矩阵、未消元、未求 Gröbner 基，也未声称新的秩、独立性或单位恒等。

## 2. 来源公式与父输入

原边界定义保留准确符号：
$$
mN_i=u_i m-A S_i,
$$
其中 $A$ 是完整原十八生成元行，$m$ 是十个原保留单项式行。若 $mv=A\sigma$，则
$$
\sigma(N_iv)=u_i\sigma-S_i v.
$$
对每个新列，先只读实际父第一像 $v_1=N_qY_j$ 与 $\sigma_1$，完整重放其来源，再计算
$$
v_2=N_pv_1,\qquad
\sigma_2=u_p\sigma_1-S_pv_1.
$$
登记之前检查所有十坐标乘法、十八坐标递推及完整多项式乘回 $mv_2=A\sigma_2$。只在原子写出完整 gzip phase 并登记 SHA 后计为完成。

父输入仍为原116→50压缩、30个第一均值像及权八保留26个交换子像，共106列；原50边界和九条字面路径全部保留。来源递推不加入参数逆或来源截断。

## 3. 原 v1 失败如实保留

原v1源码 [source](2026-11-16-r150-original-two-round-complete210-sources127-789f.py)，22547字节，SHA-256为
`9aeb996a38cd6eb3a76625697f043751a9ccf8fbf49aaf5259f9ddf9b71052dc`。

- [v1 prepare真实身份](r150-original-parameter-module-execution-789f/local-20261116-original-complete210-sources127-v1-prepare180.json)：180秒/768MiB预算，33.661211667000316秒、95096KiB、exit0；全106原来源、56第一像重放及50边界通过。
- [v1 mean失败身份](r150-original-parameter-module-execution-789f/local-20261116-original-complete210-sources127-v1-mean120-failed.json)：120秒/768MiB预算，2.9688105669920333秒、95512KiB、exit1。错误为 `TypeError: Object of type fmpz is not JSON serializable`；新列登记数为0，不能把尚未登记的计算计入结果。

失败raw为2863字节，SHA-256为
`d945424568ffb0692130a5d6094ebd2fb607ead75fc05f072f798d7866847f97`。
原目录和父验证完整phase不变；这不是预算75，不从该失败直接进入final。

## 4. 独立 v2 的最小修复与真实运行

[修复源码](2026-11-16-r150-original-two-round-complete210-sources127-v2-789f.py)为22552字节，SHA-256
`20cb960bc20fea18001488e84dae35518d74f3338697dfed619eaadae6a6b2aa`。
原数学代码只把统计量 `sourceMaximumUDegree=max(...)` 改为 `int(max(...))`；另换独立FORMAT。根完整diff复核只有这两处。新输出目录和新binding重建父验证，没有跨绑定冒用v1阶段。

完整 [输入参数](2026-11-16-r150-original-two-round-complete210-sources127-inputs-v2-789f.json) 与 [接口](2026-11-16-r150-original-two-round-complete210-sources127-interface-v2-789f.md)固定全部父源码与数学payload SHA。Python3.12.14、python-flint0.9.0。

新binding：
`41638323f597133aadeb65b2a1639899a162e2afbe6e7f7c477e93fae912cd80`。

| 实际阶段 | 预算 | 实际秒数 | 峰值KiB | 退出 |
|---|---|---:|---:|---:|
| [v2 prepare](r150-original-parameter-module-execution-789f/local-20261116-original-complete210-sources127-v2-prepare180.json) | 180秒/768MiB | 27.174693003995344 | 95168 | 0 |
| [v2 mean](r150-original-parameter-module-execution-789f/local-20261116-original-complete210-sources127-v2-mean120.json) | 120秒/768MiB | 31.453019320004387 | 95356 | 0 |

prepare全106原来源、56第一像、50边界与九路径通过。mean全部24新列通过，来源 $u$ 次数均为2。mean固定raw为9344字节/SHA
`c9c9a71628492de04781e4ea5297a69c6c58f0dbde52551019bdbafc2d8642aa`；
固定manifest为121269字节/SHA
`965d7980bcd7d95bebb353371fe78f78f460f1d526b2c0dda64492ae366130e8`。
该manifest是mean完成时的不可变副本，不借随后final会变的manifest。

## 5. 根独立完整复核

根的 [独立审计源码](2026-11-16-r150-original-complete210-mean24-source-audit-789f.py)未导入任何producer/helper。直接解码固定原基底与25个完整阶段的stored/logical字节，使用普通FLINT重新计算：

- 全24条的240个十向量递推坐标；
- 全24条的432个原十八来源递推坐标；
- 全24条完整 $mv=A\sigma$ 多项式产品；
- 全部向量参数性、同权9与 Bell 来源坐标零；
- 原十七生成元权确为11个权4和6个权5；全部新来源单项式连同其生成元的总权恰为9，最大 $u$ 次数恰2。

实际session33563、exit0，26.848439391993452秒、123824KiB。原始审计回执仅保临时目录，752字节/SHA
`639e14945451dc71e5b348cd5449a11265f5f7dfba6081fa1e03f63119672af8`；
[运行身份](r150-original-parameter-module-execution-789f/local-20261116-original-complete210-mean24-root-audit.json)记录源码与完整输出身份。

24个新phase共8,548,908压缩字节、48,573,095逻辑字节；实际完整向量项901,884、来源项278,113。这些是实际数，先前接口中的组合上界没有冒充实测。

全部数学数组、gzip阶段、manifest全文、raw和缓存仅存临时目录。Git只保源码、参数、真实运行身份、完整输出SHA与本证明。下一不同计算为已启动的80条交换子二次像及其全来源验证。
