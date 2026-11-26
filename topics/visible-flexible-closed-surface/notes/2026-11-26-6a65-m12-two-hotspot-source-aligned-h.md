# 原 M12 同 $g$ 的第二热点加密入口与传递观察集合

日期：2026-11-26；会话：Astra-visible-flex-6a65。本文登记实际完成的热点定位、准确源节点恢复、空间准备、观察集合包含检查和冻结运行入口。本文为执行前入口记录；实际完整结果已登记于 [R245](../results/R245-actual-h487-refinement-and-continuous-geometry.md)。第 8 节为旧历史发布实现，已按根 README 第 15 条停用；后续仅保存实际结论与重生身份，不保存完整可重算输出。

## 1. 以实际全域峰值选择第二单元

[实际 run 45821092388 回执](https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-entire-half-ci-45821092388-1.json) 对应源提交 cd31d2b00bcf8470c3856c8ac22e88e89b83ab8d，保存场 SHA-256 为 6d328d4cfbc5e6fdafd44705e7c8f35dfe00833b3675f53e8ae3ca2fc6cf00af。原 297 个微窗点的峰由上一实际场的 $1.933428950273708\cdot10^{-8}$ 降至 $3.9674219465268834\cdot10^{-10}$；全域独立观察及旧观察超集的峰为 $4.216833660031229\cdot10^{-9}$，位于 $q=2.1217812728079277$。

独立观察径向索引为 1413，每元 8 个 Gauss 点，因此它属于零起算第 176 元。该单元在第一次加密位置之前，原 362 元和当前 428 元的编号相同。数值区间为

$$
2.120213395105453452<q<2.1222689105337496417,
$$

对应原半径约 $0.5122239271385713<r<0.5140824465372431$。峰点约 $r=0.5126653381288877$，位于原源分片 17456。上述十进制用于数值定位，不冒充准确有理端点的认证包围。

本次保留第 190 元的全部 66 个源节点，在第 176 元另加入原节点 17432 至 17490，共 59 个。没有继续假设已经改善的旧微窗仍控制全域峰，也没有排除角向或求解误差。

## 2. 固定对象和嵌套空间

单元数为 $362+66+59=487$。径向五次 B 样条全部内节点仍为单重，故修正仍为 $C^4$。中央与真平 cuff 的完整二阶零端迹规则不变。每个自由径向系数有 98 个原实角向通道，总未知量为

$$
(487-1)\,98=47628.
$$

保留旧节点使旧函数可经 Boehm 插入准确表示于新空间。新冷入口仍从零修正重新求解；未声称拥有随旧 runner 结束而消失的实际暖启动系数。固定的 $g$、原准确积分尾、准确 common-cut 图、确定中央归一修正、完整中央至真 cuff 范围不变；原半径 $0.6$ 仍是内部自由接口。

角阶 32、角网格 384、训练 Gauss 6、独立角网格 768、独立 Gauss 8、LSMR 上限 800、一次完整非线性更新、完整 Cartesian Gram 残差和原 H1 预条件均保持。这里没有改用邻题 mild $g$ 或新几何设计。

## 3. 所有祖先观察集合都保留

设 $O_0,O_1,O_2$ 为 362、428、487 元的完整 G8 径向点集。第一次加密的额外点集为 $E_1=O_0\setminus O_1$。第二次定义

$$
E_2=(E_1\cup O_1)\setminus O_2.
$$

从而 $O_0\cup O_1\subset O_2\cup E_2$。实际程序直接核对 binary64 Gauss 点集合，并为额外点保存祖先网格 SHA 和原径向索引。本次得到 $|O_0|=2896$、$|O_1|=3424$、$|O_2|=3896$、$|E_2|=16$。前一代所有准确尾查询半径也取并集保留，最终共 4631 个。

新并集报告只合并 metric 峰、曲率峰与支撑下界，不把并集误作同一个求积能量。原观察的遗漏点在完整同场物理 jets 上重新求值，不沿用旧场值。

## 4. 两个微窗各自锁定准确点身份

新完整尾流的积分、24 个历史 blob 的校验、连续原源 $C_X$、准确端点和原 dyadic 端导身份均沿用 R230。改变仅是诊断窗口选择和标签。实际观察窗口为 $[0.432,0.436]$ 与 $[0.5122,0.5141]$。恢复节点时使用包络 $[0.432,0.5141]$ 只为取得两个元素的源节点，不把间隙冒称已观察。

每个与窗口相交的原分片取端点及四分点；共享端点只保留一次，窗口掩码取并集。准备检查实际得到：

| 窗口 | 原分片 | 分片数 | 半径点数 |
|---|---|---:|---:|
| $[0.432,0.436]$ | 17102–17175 | 74 | 297 |
| $[0.5122,0.5141]$ | 17429–17490 | 62 | 249 |

旧 297 个准确有理半径字符串及原分片索引与 R230 已恢复缓存逐项完全相同。两组逐点身份 SHA 分别为 70cf21e82e96949622b36d831feafe77bd1364d94342430334523972d2bb9f34 和 abcbc018655c23b9696bdbe3030eb4cd9bdf4298dc5ee3d66a67f5e6a6ae8ef5。新场观察器必须再次核对这类哈希，并通过 R223 逆图转换到共同材料坐标后才使用同一 $W$ 的物理六 jets。两窗合计 546 点；它们仍是有限观察。

## 5. 实际准备与验证回执

局部节点恢复读取 3 个已知历史 blob，共 10,624,295 字节，13.3043548 秒、exit 0；配方 SHA 为 01431641aef199086494da699dc3c86bd9133bf5551f84edb7fe0557877801e5。完整准确径向归一化仍由后续 24 块主流核对。

传递准备 14.8969037 秒、exit 0；网格报告 SHA 为 11464789bf6058f649ee587c02654e9bc1672e82581f402173459939dae0fde9，查询配方 SHA 为 2ad64e01e99855502e5fc03887fb8d8ac09ccf43bcd51c9a1093f9a9c5e5dcda。网格报告含本地祖先来源元数据，故其文件 SHA 不冒称为 Actions 网格报告 SHA；前一代查询配方确与实际 h428 回执的 2cdbcd42135ef6f4d8588a4c85ed82e9c0e07a0cb073c9ef04d06b9cb5ff64bd 一致。

使用扩大的源节点包络重新实际准备第一个热点后，旧 428 元网格逐项和查询 SHA 均保持完全相同。[集合及精确点检查](https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-two-hotspot-prepare-check.json) 实际 0.147938 秒、exit 0；新冷入口 plan-only 实际 exit 0，未运行新求解。八个 Python 文件均可编译；工作流 YAML、9 段 bash 语法、6 段 Python AST 实际通过。身份见 [冻结源码回执](https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-two-hotspot-frozen-source-receipt.json)。

## 6. 完整同场流水线

新入口为 scripts/6a65-m12-entire-half-two-hotspot-cold-run.py。它依次执行原整域准备、准确节点后缀恢复、第 190 元插入、第 176 元及祖先查询并集、全尾准确查询与连续源界、全 prefix 源界、完整同 $g$ 求解、R226 实际六 jets 界、全时几何传递、两准确微窗观察、全部祖先独立观察并集。工作流继续运行同一保存场的三相位完整 STL 与 R236 连续局部 Bernstein/角向预算；每个消费器锁定实际场 SHA。

直接数值命令如下，临时目录须已恢复并验证原 prefix blob：

~~~bash
python topics/visible-flexible-closed-surface/scripts/6a65-m12-entire-half-two-hotspot-cold-run.py \
  --data "$M12_COLD_DIR/m12-prefix-data.npz.gz" \
  --directory "$M12_COLD_DIR/entire-half" \
  --local-element 190 --second-local-element 176 \
  --source-knot-window .432 .5141 \
  --diagnostic-window .432 .436 --diagnostic-window .5122 .5141 \
  --prefix-elements 80 --tail-elements 64 --tail-depth 12 \
  --order 32 --angular 384 --gauss 6 --iterations 800 --newton 1 --block 24
~~~

## 7. 长作业规则检查与源码冻结

本档工作流给 90 分钟预算。数值开始前将触发提交的整个 topic 和两份 README 复制到 RUNNER_TEMP 的冻结目录，核对触发 HEAD、干净文件及 README SHA。数值程序只读这份冻结来源；发布工作树可继续普通拉取。监督器在开始时和每隔 2700 秒实际执行 pull --rebase，返回后立即读两份 README 的差异；未变则只更新本作业 HANDOFF marker，普通 commit/push。非快进后重复该过程，保留其他人的正文与 marker。

发现 README 变化时，监督器保存实际差异，终止当前数值进程组并以 42 退出；后续 scalar publisher 也检查同一状态，不能跳过。主会话据此应用新规则再继续。已执行的 [纯本地 Git 集成检查](https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-live-rules-supervisor-check.json) 实际制造并通过一次非快进重试、保留并发 HANDOFF 内容，随后制造真实 README 变化并确认没有再发布 marker、没有把变更提交标成已读；检查耗时 0.481403 秒、exit 0。该检查只操作临时本地仓库，没有外部 ref 写入。

所有 raw 仍只留 RUNNER_TEMP；不上传 artifact、Release 或 raw Git。恢复凭据仅留恢复子进程；纯数值消费器剥离该变量。发布普通小 scalar 回执的窄 push 路径不被报告自身触发。本文只证明此运行入口的对象和观察包含性，未支付第 5 条所需的完整精确解或无缺陷收敛。

## 8. 历史分件实现（已停用）

旧 h428 实际主回执已有 70,453 字节。为完整保留 R236 与双微窗、祖先来源、长作业规则记录，新 publisher 固定写三个相互绑定的小 JSON：主身份/数值观察、全部连续及 STL 报告、全部 localized metric 报告。主文件包含每个外件的路径、字节数、SHA-256 以及同一场/网格/源提交身份；外件也保存这些身份。三件在同一个普通提交中发布，不删报告内容。

[格式预算回执](https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-two-hotspot-scalar-format-budget.json) 只使用旧真实 h428 报告和独立实际执行的人工场 R236 报告做序列化格式检查，未冒认二者属于同一数学场。给主文件和连续报告各另加 8192 字节元数据余量后，实际执行工作流中的分件代码，得到 35,190、53,383、14,385 字节；各件均小于 100,000 字节。反序列化后全部输入 scalar 项逐项恢复，并重新验证外件 SHA 与字节数。临时格式样本未发到仓库；公开的只有这份明确标识格式用途的小检查回执。
