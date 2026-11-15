# 八个完整第三对角核的三导局部性消费设计

日期：2026-11-15。状态：**新源码已写成；新增人工和研究尚未执行。** 全部新执行只使用本公开仓库 GitHub Actions。此设计不改冻结生产者，不重 R254 已完成的八个对角提升。

建议 driver：scripts/literature_third_kernel_eight_local_operators.py。
建议 lane：third_kernel_eight_local_operators。

## 1. 唯一新的数学问题

R254 已给出八个准确的完整三线性算子
$$
\chi_j=\tau_j-\gamma_j,\qquad
j\in(30,32,34,37,40,100,104,109),\qquad
\Delta\chi_j=0.
$$
其中完整 $\tau_j$ 有不同的外槽 a 与对称内槽 b,c；不能把 $\Delta\chi_j=0$ 当作完整 $\chi_j=0$。

R258 已对 $Z_{71}$ 的十个方向证明
$$
K_f^\tau(w)=\tau(w;f,f)=-\mathcal J^3\mathscr A_f^\tau w,
\quad
(\mathscr A_f^\tau)^*=\mathscr A_f^\tau,\quad
\mathscr A_f^\tau f=0,
$$
且 $\mathscr A_f^\tau$ 为局部至多四阶算子。新任务只问剩余八个 $\chi_j$ 的
$$
K_j(w)=\chi_j(w;f,f),\qquad A_j(w)=D_x^3K_j(w)
\tag{1}
$$
是否也有这个准确结构，并给出完整原式答案。

每个 j 只新生成 (1) 一次。对八个目标共同保原外槽、全部真实右积分、profile 色 f/w。没有第四响应生成，没有几何或固定 profile 评价，没有矩阵秩或 membership 消元。尤其不重旧 18 参考对角、31/40/70 关系、151/152/3974 原式、旧 P1 或 $\Delta\chi_j$。

一般对角零三线性算子并不自动具有三导局部性；形式 $D^{-3}$ 也不能代替带真实左多项式尾的右锚算子。因此 (1) 是尚未支付的新目标，结果不能预先写成“八个均局部自伴”。

## 2. 原输入与来源

### 2.1 唯一完整 W 原式

使用已发布目录

notes/actions-43645177423-1-local_fourth_quotient

的四项：

| 项目 | 字节与 SHA256 |
|---|---|
| local-fourth-quotient.json | 3982；19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a |
| receipt.json | 31846；c9206d68c786613e84e4f080d2a6899b46333979e88b16f0d5306a6c88e8c0ba |
| local-fourth-quotient-W-original-expressions.json.gz | 7377；45cbdc8f38a4b5561924badaf9cd68a93a7fa71c6264d95489034703af4ee44a |
| 上项解压原文 | 31750；615d848611aaf787bc3ae790b4b1f81fe91338301bcb57afdfd111758cf533bf |

run 43645177423；source 2f1b809c0b0abb7a26303d36940edc203815f872。
W-only schema 为 visible-flex-R109-local-fourth-quotient-static-v1-original-expressions，content_scope=W-only；完整根 W0,...,W35。

原主件 completion=output_limit 只表示原 194340 字节大摘要触及输出上限；该 W-only 原式导出在当时已完整成功。复用冻结 reader 的真实 publication/source/run/packed/raw/root 绑定，不改完成标准，也不借这个字段声称原局部第四商已完成。

### 2.2 v2 完整槽绑定

使用已发布目录

notes/actions-43633746055-1-full_phase_bridge_exact

的 full-phase-bridge-exact.json；157380 字节，
SHA256 7c2cb9fece518fb6fbb15b6b4e034565dfcc5a10cf0e103a7011cd56dc4ac960；
run 43633746055；source 26c3f2c0308d179a094d3967cfb7189db426081e。

沿用 reader.load_templates 对该旧 v2 身份、152 个原 hash、36 个真正保留原根的检查。保留原索引为
$$
0,\ldots,27,30,32,34,37,40,100,104,109.
$$
仅解码、绑定已发表数据；不调用 compile_colored_local、raw_decomposition 或 control_templates。

### 2.3 八个已证明提升的准确继承

R254 actual：run 43707570035，source 282173404f65d5cc7b1dee61c66c69c3ca17866c，job 132791905419。
其完整主报告原 stdout 为 29457 字节，
SHA256 79f3fd82a22a3e24122e14f22c07fab89ebb7572048a22f9f5a8321ad1c5d11e。
该报告按根规则 15 没有新增保存为可重算 payload。

新脚本直接把 R254 已证明的八组有理坐标和 full-$\chi$ 原 hash 作为冻结数学输入常数，逐组从同一 W 原根作原式组合后核 hash。这样完整继承同一个 $\chi$；无需读取或重新执行旧对角求解。

按 R87 字典序原 $C_0,\ldots,C_{27}$：
$$
\begin{aligned}
\gamma_{30}&=(3C_2+C_{20})/256,\\
\gamma_{32}&=(C_3-3C_4-C_8)/128-C_{21}/512,\\
\gamma_{34}&=-(C_3+5C_4+3C_8)/128-3C_{21}/512,\\
\gamma_{37}&=(C_5+C_9+2C_{10})/32,\\
\gamma_{40}&=-C_{11}/32,\\
\gamma_{100}&=-C_5/8-C_{10}/4-C_{24}/32,\\
\gamma_{104}&=3C_0/4+C_6/16+3C_{11}/8-3C_{14}/16,\\
\gamma_{109}&=-C_{12}/4.
\end{aligned}
\tag{2}
$$

完整 $\chi$ 原 hash 依次为：

| j | full $\chi_j$ SHA256 |
|---:|---|
| 30 | e934dba9b2ee51574cdf22bb0eb1efa4f151125d2a6973c934d0b3c6942cf72c |
| 32 | d5eecb73427456b3075a0e93526ea5ffaee15baf902d6e72122a184cff14ee43 |
| 34 | e9711cae8ea70e3d57672acb6577e016630659235732fbb89697671d8ffdc443 |
| 37 | 3e262852b4a465df76bc6a3c917fb58bd30f73102b60c3b77daebdc7850a7b8f |
| 40 | f9cbe1f2435f9aeee4acaed8e8862832c067ea2873ba355d023b0cbf8460c71a |
| 100 | cf0662a4a39fd1076db9ba1cdf18ec8842d6399fc3852c01e6fbfea94d262a9c |
| 104 | 22becb0a3bbe0dae7becd09f079f476fc923be3178653fc8acd0b09a2facd54d |
| 109 | 6f919eb3aca85cb37f930995c088c67fed52ea44b6e0a48c1e99d1bf4c852aa6 |

gamma 和 tau 的原 hash 也继承 R254，以免正确的 chi 字符串掩盖错误来源拼接。

## 3. 同右锚的完整新操作

原 Ring.I 始终是
$$
I(F)(x)=\int_{r_*}^xF(\xi)\,d\xi,
\qquad D I(F)=F.
$$
它等于 R258 正右积分 $\mathcal J$ 的负号。不能将原 I 当作正积分后仅在最终报告补符号。

对每个完整 $\chi$， simultaneous substitute
$$
a\mapsto w,\qquad b,c\mapsto f
$$
穿过所有原嵌套积分。随后对真实表达式连续作三次 D；不先将 primitive 当独立常数，不先删左尾，不只微分显式 x。

用已冻结 PriorityWords，色序 (f,w)，最大总 profile 次数 3，对完整 $A_j(w)$ 作第一次新规范表示。逐项核 degree 为 $f^2w$，所有 surviving letters 均满足 R178 的固定颜色余语法，故可使用 R179 的原函数单射。

每个完整 word 代表再按相同右积分语法还原为原 Ring 表达式；另一个独立 mapper 核原差
$$
D^3K_j-\operatorname{Eval}(\operatorname{Word}(D^3K_j))=0.
\tag{3}
$$
(3) 的完整原差 SHA、原项数、fresh word 结果保存在本次内存证明摘要中。它是新 $D^3K$ 的原差检查，不是重跑 $\Delta\chi=0$。

## 4. 怎样准确判断局部性

只在规范代表的全部 surviving word 为空时，才提取
$$
A_j(w)=\sum_{k=0}^{m_j}a_{j,k}(x,jf)\,w^{(k)}.
\tag{4}
$$
每项恰有两个 f jets 和一个外 w jet；$m_j$ 从完整结果读取，不预先裁到四阶。输出每个系数的完整有理单项式列表：
(x 次数，两个 f jet 阶数，有理系数)。

若仍有非空 word，完整保留并按两种语法记录：

1. w 出现在某个积分 letter 内；
2. w 只在外部，非局部尾只含 f。

两种情况不可混同。报告“非空规范 word 存在”及完整原代表，不把它误称为固定圆不可能，也不把形式编译成功变成局部性已证。R179 在本 universal 多项式 right-word 范围内保证：非空规范部分不能与任何空 word 多项式差消；它没有赋予固定 f 或固定圆同样的 faithful 性。

若 (4) 成立，重新组装 $A_j(w)$ 并使用独立 mapper 核
$$
D^3K_j-A_j(w)=0.
\tag{5}
$$
再直接按有限微分算子的定义生成形式伴随
$$
A_j^*(w)=\sum_{k=0}^{m_j}(-D)^k\{a_{j,k}w\}.
\tag{6}
$$
(6) 中全部系数链式求导。检查完整局部多项式 $A_j^*w-A_jw$，保存零或非零原差，不以 coefficient 标签对称替代。若不自伴，这是准确的新结构结果，不是自动的实现错误。

从 R254 已有 $\Delta\chi=0$ 可以纸面继承 $A_j(f)=D^3\chi_j(f;f,f)=0$；本次不重新运行这个旧对角目标。

## 5. 可下的结论和不能下的结论

所有原 profiles 在共同右 collar 为零，完整 $\chi$ 的原表达式也在那里恒零，故 $K_j,K_j',K_j''$ 的真实右迹全为零。不论局部性是否成立，总有完整同锚恢复
$$
K_j=-\mathcal J^3(D^3K_j).
\tag{7}
$$
所以若八个目标均局部、自伴、至多四阶，R254+R255+R258 给整个十八维 Z 的统一公式；这是真正的原函数结构，不是八个 raw hash 的同值猜测。

反之，非局部、高阶或非自伴结果均完整报告，仍可将准确 $D^3K_j$ 用于 R225 的 period 接口，但不能把尚未付的条件写成全 Z 定理。

无论结果如何，本次均不计算：

- 固定圆的响应 rank、满射或 annihilator；
- 第四完整 pure 核中不由 Z 产生的分支；
- 任意带符号实际成本实现；
- 同一 gauge 的第四 ruling；
- R225 的全部平台、内部退化与两端 germ 是否同时可付。

## 6. 新人工仅覆盖新实现

计划八类小人工，全部首次执行在公开 Actions：

1. 空 word 的准确外 w-jet 分组及重建；
2. 一个含内部 w 的真实右 word，不能误标局部；
3. 一个外 w 乘纯 f 尾的 word，与上一类区分；
4. 人工 $D^2(f^2D^2w)+D((f')^2Dw)$ 的完整形式自伴检查；
5. 人工 $f^2Dw$ 的非自伴差不能误报零；
6. 原负号约定下 $D^3I^3(A)=A$，不偷换左右 I 号；
7. 原 $wI(ff')=wf^2/2$ 的同锚 IBP，fresh 原差为零；
8. 人工六阶局部目标保真实阶数 6，不因预期四阶而截断。

这里只是 invented algebra/API checks，不调用真实 W 输入，不重旧人工或研究。

## 7. 输入、执行与资源

实际 CLI 计划只需两个原目录：

python scripts/literature_third_kernel_eight_local_operators.py
--w-directory notes/actions-43645177423-1-local_fourth_quotient
--third-directory notes/actions-43633746055-1-full_phase_bridge_exact
--output @OUT@/third-kernel-eight-local-operators.json
--max-seconds 120
--max-memory-mib 512
--max-nodes 300000
--max-atoms 40000
--max-terms 40000
--max-word-calls 150000
--max-cache-entries 150000
--max-rational-bits 8192
--max-monitored-rational-operations 1000000
--max-proof-bytes 8000000
--max-summary-bytes 95000
--max-mathematical-stdout-bytes 1000000

人工以 --toy-only 和自己的临时 --output 运行；科学与人工都要求 GITHUB_ACTIONS=true 且 GITHUB_REPOSITORY=Rogerhu12/math-research-public。不将人工报告或 temporary main 写到公开仓库。

只写 runner 临时 main；内存证明不落文件、artifact 或 Release。stdout 逐个打印 EIGHT_KERNEL_OPERATOR（准确完整系数或 surviving words），末尾 MATHEMATICAL_RESULT、COMPLETE_REPORT、TEMPORARY_MAIN 含 bytes/SHA；publisher 仅记录源码、参数、run、费用、SHA 元数据。完整新数学行的 stdout 另有累计 1000000 字节上限；临时 main 去掉已经完整打印的长 word/adjoint 行，只保其真实 SHA、项数、局部系数与结论。若达到预算，保已完成目标摘要并将其余明确为未完成，不假装完整，不自动扩大预算重跑。

rational 计数仅覆盖 MonitoredLimits.rational 的实际调用；不得冒充全部 DAG 算术总次数或全局最大位数。总体 elapsed/RSS 独立如实记录。

## 8. 源码复用边界

直接 imports 仅 ColoredRing、PriorityWords、原 reader 与 exact budget/API；通过 AST 递归读取并绑定其全部 frozen literature_ 源。这会在元数据中出现旧完整生产者源码，但调用链只有已有输入读取/解码/hash，绝不调用它们的研究入口或编译函数。

R254 driver 本身不用 import，八组 (2) 与原 SHA 是已发表的准确常数。新文件不改任何旧源。source_inventory 对全部十五个旧递归源逐字节核冻结的 bytes/SHA，并检查真实 AST import 闭包正好等于该集合；生产者研究入口没有调用。最终 source SHA、完整递归 source_bindings、准确 public CLI 与源一同交 root；本文没有宣称新增人工已通过。

当前独占待合并路径位于 /dev/shm/tail-eightK-pending-9974ea84/，以避免已满的 workspace。源码仅作文本生成、静态阅读和文件 SHA；没有 import 新源、没有执行新增人工，也没有在本地运行真实 (1)。

