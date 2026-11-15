# D0 一般 pure 后继：只消费 R151 的九个已发表真基

日期：2026-11-15。**新源码及六项小人工已完成；本研究目标未在本地或公开 Actions 运行。** 本稿只准备一次公开消费任务，不自行激活计算。

## 1. 唯一问题和先前结论

R153 已用同一固定有理 profile 对、新 mixed 查询和43阶非零子式证明

$$
\mathcal D_0\notin
\mathcal R_8+\operatorname{span}\operatorname{Orb}(G)+\mathbb RJ.
$$

这不决定 D0 的一般 pure 分量。R153 的 pure 模残差为零只是同一测试对与一个素数的结果，不能成为本次的有理系数或原式身份。

本次唯一目标为

$$
D=(\mathcal D_0)_{-4}
\stackrel{?}{\in}\pi(\mathcal R_{8,-2}),\qquad \pi V=V_{-4}.
\tag{1}
$$

相位 $-4$ 与仿射权 $-2$ 分开记录。D0 是已发布的完整轴系数，包含全部 $N_2$、真实三阶势和速度四次项；此 consumer 不重新计算这些部分。

R151 已准确证明一般 pure 像恰九维，并保存九个原基及其准确 word 代表。它的40个旧原根和31条新 pure 依赖不再归约或重新评价。本次只把九个存储代表还原，再对 (1) 作一次新的有理求解和原差证明。

## 2. 固定的九个真实基

设 R116 全局列为 $C_{8j+a}=\mathcal B_{P_a}(W_j)$，$P_a$ 依次为 p0,p1,p2,r0,r1,s0,s1,t1。全部索引从零开始。

| 本次新索引 | R151 消费原位置 | R131 块内原列 | R116 全局列 |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 48 |
| 2 | 2 | 2 | 88 |
| 3 | 3 | 3 | 112 |
| 4 | 8 | 8 | 41 |
| 5 | 9 | 9 | 73 |
| 6 | 10 | 10 | 81 |
| 7 | 12 | 12 | 193 |
| 8 | 19 | 19 | 170 |

在这九条中原位置恰等于块内号；程序仍分字段保留，不以此省略全局号和原根身份。

公开证书顶层保存40条 pure_column_representatives，每条包含 original_position、original_root、original_sha256、word_summary、word_rows。新程序只取上表九条：

1. 核完整来源字节和原 producer 身份；
2. 核 R151 的31条原差证明列表 SHA，但不重新运行这些证明；
3. 用已发 subset decoder 解码九个原根；
4. 调用已发 decode_word_rows 原样恢复九个代表，核其摘要与原根 hash 对应；
5. 使用同一个新 word owner，不调用这些旧原根的 normalizer.expression。

九维真实上界来自 R151 已发布的完整31条原差，真实下界来自同稿对 R131 原有理40阶控制子式的九个 pure 行的论证。新九列代表的线性解码/消元只检查输入一致，不替代这个真实维数证明。

## 3. 唯一新增数学计算

对 D 的原表达式作一次 sound 归约，得到 $v_D$；九个旧代表直接载入为 $v_0,\ldots,v_8$。在 $\mathbb Q$ 上消元提出

$$
v_D=\sum_{j=0}^{8}a_jv_j+\rho.
\tag{2}
$$

不使用 R153 的模整数 lifts，也不作模数采样。

无论 $\rho$ 是否为零，都从原 D 与原九列重新形成

$$
\Delta=D-\sum_{j=0}^{8}a_j(C_{g_j})_{-4},
\tag{3}
$$

然后用独立的新 normalizer 检查这一个完整原差。右 Volterra 锚仍是共同的零右 collar；左右端没有重新重置。所有 primitive 保持正 profile 次数，已有 sound IBP 的真实右端边界条件不变。

只准两个数学结论：

- **原差准确归零：** 输出完整有理系数、R116 全局列对应、原根/原差 SHA、原差零证书，证明一般光滑 profile 上的 pure 成员。
- **原差 sound 余项非零：** 输出未决。正规形不完备，不能声称非成员，也不启动新的 profile、子式或目标。

即使代表求解余项非零，(3) 若独立证明为零，仍是合法阳性；反之，仅某个代表标签相等不能替代原差检查。

本次没有原有理 profile 评价分支。已有完整 mixed 非成员结论不因 pure 阳性而撤销；pure 阴性代表也不能增加完整商维数或给成本符号。

## 4. 精确输入来源

### 4.1 D0 原根

公开目录：notes/actions-43657526246-1-h_axis_sharp。

- Run：43657526246。
- Source：0d5df1843fd829e7c09b17afdead930ec4395f34。
- 原 producer：literature_h_axis_sharp_coefficient.py，31222 B，SHA256 7f4ee057a16a620e089102ea9c84fccafd922306e8febf8b73391b478e4a4a0b。
- 主报告：h-axis-sharp.json，17542 B，SHA256 e0007757b7d113a34b5c2ec594a607d380855f5652042f67fe3f32c1c81397f0。
- receipt：36161 B，SHA256 1d635cdbe80251339d1157cee579c6838cad8975310a80959ef92b171f2458ea。
- 原式导出：h-axis-sharp-original-expressions.json.gz，14497 B，SHA256 ecd9edf2d461f6d4f6b9355e17e210ad435b20c53bc16baeda412258b8b3fabd。
- 原文：80444 B，SHA256 2d0433a628b22f223a0f8700cebad02e70305699ff39a65e075de81dad5ceed0。

固定 pure 根 SHA256：

~~~text
1236f94a788454870d655dda499714eacccfee730cba582e22fb2c0b4d892f7f
~~~

消费器复用已发 D0 输入 helper；两个模式只读 hash 绑定，但仅 pure 根进入新的代数。mixed 根不归约、不评价、不形成新差。

### 4.2 R151 的原基与存储代表

公开目录：notes/actions-43657785023-1-general_pure_J_membership。

- Run：43657785023。
- Source：c606688a842bd811106ff2844e1161a4f34c159e。
- Producer：literature_general_pure_J_membership.py，37092 B，SHA256 1a84590f8b6f0c35a1df5f251a8ffa0e9f4da65ea2cc3bd777e752482ef05bcc。
- 主报告：general-pure-J-membership.json，45019 B，SHA256 98442251ed15b708a70e3fcbbdb2ae6cf76c8c1873aa21345354a5a320a9cfac。
- receipt：35841 B，SHA256 31d6380160437b0098d33d35e4b722c79cd780d351f614a4e48901100a9d0fa4。
- 完整证书：general-pure-J-membership-certificate.json.gz，84283 B，SHA256 af46437f676716a20051bf3bad5a96235398dcf8a45c179d1395bc1f9d84712e。
- 原文：456216 B，SHA256 9859368ec20e0923cc168199a7ecb82eff0beac5fa191f1b6388e67cfd1aa550。
- 31条原差列表 SHA256：bdd01870f261b98a4f63c38789ccbe81b96084e71c25ef0831c3893718536a69。

完整文件中的73个原根不全部解码。本次只选择九个命名 original_pure_column_XX 的基列；J 原根、旧31差和旧 J 原差都不重新归约。

输入 SHA、schema、scope、run/source、publisher source_files/outputs、原 source_hashes、完整 pure 上界、九位置及全局号同时绑定。旧原证明文件只读，不修改。

## 5. 新源码、人工开发和实际命令

新独占源码：

~~~text
literature_general_pure_D0_membership.py
25604 B
c296f72becff4366297e3b9f00db97425b1aa5b15c10ba7625932966ae7c8f1f
~~~

仅新增六项人工检查：

- 存储基位置及重复/缺失索引拒绝；
- word 代表解码过程中旧原根归约计数为零；
- 原根名、原 SHA、word 摘要错配拒绝；
- 一个新小有理目标的准确系数与 fresh 原差归零；
- 一个不在小玩具代表 span 中的余项只标未决；
- 新原式证书往返保持原根身份。

这些检查不读任何实际报告或研究原根，不评价研究 profile/几何，不运行旧40基或31依赖。

人工结果：D0-pure-development.json，25296 B，SHA256
484712a3454b8b4dfd85a0467b9852a6157037d25fe5900ab8227066bb2496af。
六项通过；耗时0.006704259秒，RSS14.875 MiB。

计划唯一公开 CLI：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_general_pure_D0_membership.py --toy-only --output /tmp/D0-pure-output/general-pure-D0-development.json
python topics/visible-flex-new-mechanism/scripts/literature_general_pure_D0_membership.py --output /tmp/D0-pure-output/general-pure-D0-membership.json
~~~

默认路径已精确绑定上述两个公开目录；可仅为物理文件位置改 D0 的三路径和 basis-directory，所有字节与身份仍须相同。真实路径要求 GITHUB_ACTIONS=true 且 GITHUB_REPOSITORY=Rogerhu12/math-research-public，人工路径不读取实际输入。

## 6. 预算、输出和失败保留

默认180秒、软轮询RSS1024 MiB，原节点500000、atoms100000、项120000、每个归约器IBP调用500000，有理消元分子/分母位长8192。内存是主动检查阈值，不称操作系统硬限额。有理位长门准确限定在消元层。

上次 R151 整个40基/31差/一个目标实际只用4.134秒和94.235 MiB；本次复用九代表且不重复旧依赖。预算保持足以加载已发原件，不盲增旧研究范围。

输出：

- general-pure-D0-membership.json：小主报告，至多90000 B；目标身份、九个原列、有理系数、原差结果、真实边界和资源。
- general-pure-D0-membership-certificate.json.gz：至多1.5 MB；D0 pure、九原基、一个新原差的11个原根；九个已存代表及新目标/余项、准确系数和 fresh 核验。
- 主报告必要时另存完整报告 gzip，至多2 MB；总上限3.59 MB。

在真实输入完成后即先保存10个目标/基原根；若后续资源退出，来源和已完成阶段仍有回执。异常写入 source-bound 主报告，资源退出不冒数学非成员。非零 sound 余项正常完成为未决，不自动增预算、切换 profile 或执行第二目标。

## 7. 对后继数学的精确作用

若 (1) 阳性，记得到的完整响应组合为 $K_D\in R_{-2}$。则

$$
H_D=\mathcal D_0-K_D,\qquad \pi H_D=0.
$$

结合 R153，$[H_D]$ 仍独立于 R 加 G 轨道和 J，因此这是新的 pure 恒零完整商代表；它不证明该 mixed 类可调正负。

若未决，R153 的完整43维子空间和 $\dim U\ge239$ 原结论不变。本次仍不能决定 $\pi U=\pi R$，也不把全部成本、ruling、有限族或嵌入目标标为完成。
