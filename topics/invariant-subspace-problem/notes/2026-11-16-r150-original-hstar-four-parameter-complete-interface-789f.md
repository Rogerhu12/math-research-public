# 原九目标：完整四参数湮灭理想的同基执行接口

**作者：** ChatGPT（AI），GPT-6 Astra Pro / literature_audit  
**日期：** 2026-11-16  
**状态：** 源码与输入已固定，尚未执行这条新链。已发表的四参数定理不含最后两列的计算值。

## 1. 精确范围

设 $D=\mathbb Z_{(31)}$、$p=31$、$x=s-2$，$b_j=[h_*t_j]$，$j=2,\ldots,10$。令 $B=\sum_jD[s]b_j$。已证

$$
K=(p^5,p^2x,px^2,x^4)
\ \subset\ I=\operatorname{Ann}_{D[x]}B\
\subset\ J=(p^4,px,x^2).
$$

$J/K$ 的四个有序基为 $p^4,px,x^2,x^3$，$p$ 的作用为零，$x$ 的作用为

$$
(\alpha,\beta,\gamma,\delta)\longmapsto(0,0,0,\gamma).
$$

本次真正计算同一个已识别的七维 socle 基中的四列

$$
W_j=p^4b_j,\qquad V_j=pxb_j,\qquad
Z_j=x^2b_j,\qquad Q_j=x^3b_j.
$$

将九个 $7\times4$ 块叠为 $63\times4$，其完整核就是 $I/K$；每个块的核给出单个 $b_j$ 的完整湮灭理想。不存在未纳入的更高参数系数：$x^4$ 已在 $K$ 中。

理论来源为：

- results/R150-appendix-original-hstar-fourth-parameter-annihilator-and-complete-four-scalar-test.md；
- results/R150-appendix-original-nine-targets-one31-scaled-annihilator-and-hstar-tail.md；
- results/R150-appendix-complete-coefficient31-exponent-six-and-exact-original-p2h0-sources.md。

这只是 R150 原模块的后继计算，普通 Hilbert 不变子空间问题仍未解决。

## 2. 不依赖失效本地缓存

新 job 独立恢复原历史输入，并只重建真正需要的来源列：

| 层 | 在原完整层中的零基列号 | 新列数 | 计算 / 稳定 Taylor 精度 |
|---|---|---:|---:|
| L3 | 0 至 7 | 8 | 25 / 20 |
| L4 | 6 至 12 | 7 | 20 / 15 |
| L5 | 10、11、12 | 3 | 15 / 10 |
| L6 | 12 | 1 | 10 / 5 |

F2 的三个完整原列和 F3 的一个完整原列都逐原索引检查：所列来源之外的全部系数必须为零。新程序不删除“看起来为零”的来源，也不从两条旧探针推完整结论。原完整 210 列的 E=6 定理仅作已证输入，本次不重新运行完整 210 链。

原 G/V 单位及全部 DAG 都沿原固定规范构造；固定单位行列、自由坐标零与原 q1 多项式求值均不改。新完整 G、V 文件只将头中的 binding 临时替换为旧全宽 binding 后，必须分别得到旧全文件 SHA-256：

- G：ef9976aca179c382c4bf265b362e56280ea725aea16e164e8d29d5759bd92202；
- V：ed02ca487853bff3a9f117b2e3c749c0cf5c9897bb4bb9d4dd53184ee0597d5a。

保留完整原 6188 来源与 4367 输出、p7 整数产品、104 个局部自由条件、505 个全局自由观测和全部 315 个商坐标。30 个原阶段全部完成后才生成新的 selected-true16-parent.json。

## 3. 高 p 同基门

U16 和参数作用的模 31 矩阵相同，本身不够识别高 p 的 socle 坐标。因此本次在同一个新父 pack 内重新计算所有四列：

1. 原 $h_*$ 首次真实 carry 重新给出 C1；$W$ 为 C1 第16行乘以唯一第6阶 socle 轴。
2. 原 $h_0=xh_*$ 七 socle 消费者重新给出 $V$。
3. 原 H25=$x^2h_*$ 的历史全局来源给出 $Z$。
4. 同一历史来源在 Taylor 变量中乘 $x=[0,1]$，给出 $Q$。

所有消费者逐文件核同一个父 pack、同一个父 binding、完整来源文件字节与原标签。父 source-family header 会显式重写为 child binding；数学 payload 逐原行选列，不能只接受一个旧魔数便假定兼容。

新的首 carry 必须重现九个原 $h_*$ 恰需五个 31 因子的已付结果；新的 $h_0$ 控制必须重现九个原目标恰需两个 31 因子、socle 像秩1且前四行零。若失败，计算以失败退出，不将另一套坐标混入最后的核。

## 4. H25 最小历史恢复

独立恢复程序只读取历史提交

8c6304e273e64b0544d3dd58bc0e48a672a87c36。

所需全局 H25 来源由两条既存历史 gzip 分片恢复，共 4,774,246 个压缩字节。解压原来源为 4,989,406 字节，SHA-256：

593643d82b259995194b0d89c9f46c8f042cd8d0c66bdfff0a00227689810cdd。

这是读取旧历史，不新建分片或新存数据。Actions 只将原字节读取到临时目录。另恢复五个小文本：

- original-product.json；
- original.recipe；
- continuation-receipt.json；
- original-integer-h25-mod29791.txt；
- root-preservation-manifest.json。

恢复程序逐 archive member/git blob 的固定路径、字节数和 SHA 核验。原 815 字节乘回记录完整保留 17 方程、6188 来源、4367 输出、九目标、模 $31^3$ 与零失败条件。新 native 独立复乘 $h_*=s^3F_+^2F_-^2E_8$、再乘 $(s-2)^2$ 或 $(s-2)^3$，逐系数核原模型；普通平方的非对角系数为2，不能换成对称张量的另一规范。

本次无需 currentK4，也无需旧完整 3.7GB 来源链。

## 5. 两个真实尾 carry

对于 $w=x^2h_*t_j$ 或 $x^3h_*t_j$，初始来源给出

$$
w-AY=p^3r_3.
$$

使用同父真除源基和完整 315 商，依次写成

$$
r_3=G_{13}a+Aq_3+pr_4,\qquad
r_4=G_{15}d+Aq_4+pr_5.
$$

整数程序计算的是原 target 减原 A 乘积。乘 p 后，两个正号来源补偿依次产生 $p^5r_4$ 和 $p^6r_5$；从而

$$
[w]=p^3G_{13}a+p^4G_{15}d+p^5G_{16}f.
$$

七个 socle 坐标正是四个 e4 的 a、两个 e5 的 d、一个 e6 的 f。本式读的是 w 本身，不是 pw。

15→10→5 的稳定精度由原固定 G 的最多5阶精度损失控制。每次有限 G 解的全部计算系数仍逐原 G 核验；稳定尾和完整 104/505/315 门共同给出已证完成模中的真实类。程序不把 CRT 插值或有限 jet 直接宣布为全参数多项式恒等式。对这七个坐标的全局解释，使用已经证明的系数扭子分解、root1 部分消失和完成忠实性。

## 6. 最终完整核及规范形式

最终消费者核验：

- 同一真实父来源基、同一原九目标字典；
- 每个 $7\times4$ 块与全部 $63\times4$ 行；
- 前两列秩2；
- 核到后两坐标的投影单射；
- 核在 $(\alpha,\beta,\gamma,\delta)\mapsto(0,0,0,\gamma)$ 下稳定；
- 所有核向量乘回原小矩阵精确为零。

若核维数为0，输出 $I=K$。若维数为1，则输出唯一规范关系

$$
x^3+a p^4+bpx,\qquad a,b\in\mathbb F_{31},
$$

并将理想写为 $(p^5,p^2x,px^2,x^3+ap^4+bpx)$。

若维数为2，则输出

$$
I=(p^5,p^2x,x^2+ap^4+bpx).
$$

因此 D[x]/I 的 D 循环指数依次为 $(5,2,1,1)$、$(5,2,1)$、$(5,2)$。对每个单目标，这也给出其实际循环模的长度9、8或7；共同理想的商环长度不能冒称整个九生成元 B 的长度。

原九目标模的完整湮灭理想为首一化 $h_*$ 乘本次 I；每单目标亦同。所有原来源存在证书仍适用已付统一费用8515，不把恢复的有限 jet 当作已显式写出这些全局来源。

## 7. 一次 job 的完整队列

工作流：

.github/workflows/invariant-subspace-r150-hstar-four-parameter-session.yml

请求：

notes/2026-11-16-r150-hstar-four-parameter-session-789f-request.json

十个步骤按次序执行：

| 步骤 | 工作 | 上限 |
|---|---|---|
| 1 | 恢复原14个历史输入 | 600秒、2GiB |
| 2 | 恢复六个已付小系统 | 600秒 |
| 3 | 恢复四族真来源、原 primitive 和 jet map | 600秒 |
| 4 | 恢复 H25 五小文本和两历史分片 | 180秒 |
| 5 | 一次 8→7→3→1 真来源重建 | 1800秒、4GiB |
| 6 | 同基原 $h_*$ 首 carry | 1800秒、4GiB |
| 7 | 同基原 $h_0$ 七 socle 控制 | 1800秒、4GiB |
| 8 | 同基 $x^2h_*t_j$ | 1800秒、4GiB |
| 9 | 同基 $x^3h_*t_j$ | 1800秒、4GiB |
| 10 | 完整共同与逐九四参数核 | 60秒、512MiB |

数学步骤只在预算退出码75时以同 binding 自动续接，每步最多三个 attempt；其余失败保留实际身份，不作成功依赖。整个 job 上限180分钟。按旧九列实际运行，预计总时长约15–25分钟；这不是新链的实测承诺。所有步骤在同一个 job 中共享 tmp，不在步骤之间重建父来源。

所有 Python 源在 Actions 读入后先实际编译语法，再运行；native 的编译与完整乘回门照原代码。当前共享 executor 不可用，本文不声称本地 AST、编译或新数学运行已经完成。

## 8. 文件与发布边界

完整 path→blob→bytes→SHA 表、20项原 helper/restorer 依赖、全部 CLI 与小文件清单见：

notes/2026-11-16-r150-original-hstar-four-parameter-complete-manifest-789f.json。

新源码合计十二件，另加本接口与上述输入清单。旧 helper 的字节不改。根维护 request.rulesReadAtCommit，实际 job 每次 pull 后核两 README；非快进按原规则 pull/rebase 再 push。

所有原数组、来源 cochain、C1、O、Z、Q、63×4 以及完整核只留 job 临时文件和完成日志。Git 只提交源、参数、run 身份与输出 SHA，不上传 Release 或新数据工件。身份记录目录为 notes/r150-hstar-four-parameter-execution-789f/。没有任何未知核维数、a、b 或最终理想预填到输入。
