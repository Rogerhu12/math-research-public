# R182：共同规范 word 的新原函数恒等式排除 R177 全层正外点

日期：2026-11-15。**已证明；使用公开 Actions 上的新精确有理运算、完整原差和逐列转换证书。**

新的共同 word 比较给出一条此前字面比较没有得到的完整原函数恒等式。它在 R177 已公开核过的全层严格正外点上取值 **384**。因此，该点不能定义一个杀真实响应空间的原函数泛函；其标量 action 的正性证明仍然成立，但不能据此构造真实正字符。

在 R174 的十二参数必要形状中，新条件准确成为

$$
\boxed{D_0=-\alpha-\beta.}                                      \tag{1}
$$

这里 $D_0$ 是二阶标量系数 $b_2(k)$ 的常数项，**不是** R150/R153/R157 中的完整轴算子 $D_0$。式 (1) 把当前已知线性必要外空间从十二维降至十一维；十一不是完整真实字符商的维数。

本次按预定接口在首条切点的完整原身份支付后保存状态，已经处理 77 个字面基列中的前 62 个。余下 15 列继续从该状态处理。R177 的排除不需要等待剩余列，也不表示整个课题或全部真实核已经完成。

## 1. 原对象、同右锚和 77 列的来源

沿用 [R174](R174-nine-original-character-relations-and-rejection-of-the-positive-outer-point.md) 的原列编号：

$$
(C_0,\ldots,C_{146})
=(R_0,\ldots,R_{39},V_0,\ldots,V_{106}),                         \tag{2}
$$

其中 $R_j$ 是已经证明真实独立的四阶响应原列，$V_i$ 是 [R163](R163-complete-normal-coefficient-cocycle-and-single-weight-character-head.md) 完整真权 $-2$ head 的 107 个 normal 原记录。每列都有已发布 canonical 模 $-4,-2$ 的原表达式。

R174 的 70 条逐项核零身份已给出一个由 77 列张成全部 147 列的字面呈示。本次只消费该 77 列，不重新生成其余 70 条关系。前 40 列仍是原 R40，顺序未变。

所有表达式保持同一物理右锚和同一右 collar：

$$
I(F)(\xi)=\int_r^\xi F,\qquad
q,\bar q\text{ 及有关 jets 在共同右 collar 上为零}.             \tag{3}
$$

这里没有把 primitive 值独立赋值，没有更换左右锚，也没有代入幂尾或采样 profile。

使用的两个忠实分量是

$$
\pi V=V_{-4},\qquad
\Xi V=[q^2\bar q^2]V_{-2}.                                    \tag{4}
$$

[R159](R159-balanced-mixed-faithfulness-after-pure-cancellation.md) 的含义是：若某完整 canonical 组合先满足 $\pi V=0$，则 $\Xi V=0$ 当且仅当该完整组合为零。因此，**同一个组合的两个分量都原式为零，就证明完整 canonical 函数为零**，无需把其余 mixed 颜色分量逐一当成独立输入。

## 2. 首条切点关系：完整 147 列身份

新证书的 relation_index 为 **9**。其依赖列是字面基下标 61，即原列 $C_{98}=V_{58}$。定义

$$
\mathcal A=\sum_{j=0}^{39}r_jR_j,                               \tag{5}
$$

其中全部非零系数如下，未列出的 $r_j$ 都为零：

| $j$ | $r_j$ | $j$ | $r_j$ | $j$ | $r_j$ |
|---:|---:|---:|---:|---:|---:|
| 0 | $-192$ | 1 | $96$ | 2 | $-192$ |
| 3 | $-192$ | 4 | $-144$ | 8 | $384$ |
| 9 | $-192$ | 11 | $-144$ | 12 | $-140$ |
| 13 | $-48$ | 16 | $96$ | 17 | $144$ |
| 19 | $-48$ | 20 | $-144$ | 21 | $-48$ |
| 24 | $24$ | 25 | $-2$ | 26 | $146$ |
| 27 | $-20$ | 28 | $-48$ | 29 | $96$ |
| 31 | $-144$ | 33 | $48$ | 36 | $25$ |
| 37 | $12$ | — | — | — | — |

新的完整原函数恒等式是

$$
\boxed{
\mathcal A+
256\bigl(2V_0-V_1+2V_2-V_4+V_7+V_8+V_{58}\bigr)=0.
}                                                               \tag{6}
$$

这给出了 147 个系数的完整描述：前 40 项为式 (5) 的 $r_j$；normal 部分仅

$$
(i,\text{系数})=
(0,512),(1,-256),(2,512),(4,-256),(7,256),(8,256),(58,256)          \tag{7}
$$

非零。证书同时保存 dense77、dense147 与稀疏原列系数，避免新基编号和原 normal 编号混用。

这些 normal 根的来源是：

| normal 下标 | family | state_key $(h,k,\omega,\log h)$ 的指数 |
|---:|---|---|
| 0 | F0 | $(-2,0,0,0)$ |
| 1 | F0 | $(-2,2,0,0)$ |
| 2 | F0 | $(-2,4,0,0)$ |
| 4 | F0 | $(-1,1,0,0)$ |
| 7 | F0 | $(-1,3,1,0)$ |
| 8 | F0 | $(-1,5,1,0)$ |
| 58 | Q2_2 | $(-4,0,0,0)$ |

表中的 F0 是完整八矩规范化原族；不能把只在 $\omega=0$ 上看到的几项替代完整身份 (6)。响应项 $\mathcal A$ 也不能在原函数层面直接删去。

## 3. 为什么这是一条完整原身份

### 3.1 每列转换与共同字典

[R178](R178-fixed-color-priority-IBP-and-terminating-shared-word-map.md) 给固定颜色次序 $q<\bar q$ 的局部 IBP 规则、严格下降 measure，以及同右锚的 all-depth shuffle。新映射从各列的完整已存原根出发，保留每一项转换，未使用 cycle fallback。

R40 的 40 个 pure 代表直接读取 [R151](R151-general-pure-J-identity-nine-dimensional-range-and-kernel.md) 已付的原式转换，不重做旧 pure40、31 条依赖或原 profile 评价；这次新增其 balanced 分量和尚未有代表的 normal 分量。每个新旧代表都检查了每个 word letter 满足 R178 的固定颜色余项语法。

实现保守地区分新规则映射 $\Phi$ 与在原 77 字面基上逐列延拓的共同映射 $\Psi$。证明 (6) 只需要每列已经绑定的转换满足

$$
\operatorname{Eval}\Psi(C_j)=(\pi C_j,\Xi C_j),                  \tag{8}
$$

不需要假设旧两段式 pure 归约与新 $\Phi$ 的执行路径相同。

[R179](R179-universal-independence-of-fixed-color-remainder-words.md) 另外证明该固定余 letter 字典的普适函数单射性；因此，对于已验证同锚、同原式和规范语法的代表，新旧表示事实上唯一。这里没有为这项纸面唯一性重新运行旧 pure 目标。

### 3.2 独立原差与两根零和

消元找到 relation 9 后，消费者另从全部原存储列重新相加，保存式 (6) 的完整 $-4$ 与完整 $-2$ 原多项式差，随后独立读回 32 个非零支持列的 64 份分量转换并求和。

| 项目 | pure 模 $-4$ | 完整 mixed 模 $-2$ |
|---|---:|---:|
| 重新相加的原 term rows | 6194 | 27694 |
| 相加后原字面差的项数 | 486 | 2152 |
| 忠实分量的独立规范 word 和 | 0 | 0 |

“原字面差还有项”与“原函数恒零”并不冲突：本次支付的正是超出 R174 字面抵消的积分/分部积分关系。两根和使用逐列原身份独立重合，未凭消元 row-id 或单个非零 normal form 下结论。

完整 pure 原差 SHA256 是

**8a7cb436d4a6c247eba86d8811f1b45b6f3a3e1385dcd47a80a4c9e07fc0ecc5**；

完整 mixed 原差 SHA256 是

**09cb10fcc9d834f8ec856818702e6cf8f6cec4adc6f1a7c1c73b3fdc6c0ba471**；

mixed 的忠实 balanced 原分量 SHA256 是

**86cb0a7994c0d3f6c7ed73a3ae1cf59384f82737b04498e4445667dd69104f91**。

两份独立 word 和都是空表，其共同 SHA256 是

**4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945**。

由 (8) 得 pure 原函数差为零，再由 balanced 原函数差为零和 R159 的忠实性，得到完整身份 (6)。这一步只使用 sound 转换及忠实两根，不依赖“尚未发现更多关系”。

## 4. 完整旧 free 等式及十二参数含义

对任何杀响应空间的真实泛函 $\lambda$，令 $\nu_i=\lambda V_i$。由 $\lambda\mathcal A=0$，式 (6) 给

$$
2\nu_0-\nu_1+2\nu_2-\nu_4+\nu_7+\nu_8+\nu_{58}=0.               \tag{9}
$$

在原来的 107×23 坐标映射 $\nu=By$ 中，证书保存的未缩放行是

$$
q_9(y)=768y_0+256y_1+256y_2+256y_8-768y_{12}=0.                 \tag{10}
$$

旧 $B$ 没有重算；107 坐标与 23 坐标的两个点值也分别核对相同。

证书对 R168、R174 和此前新行约去已知部分后，准确余行为

$$
-128y_2+256y_8=0.                                             \tag{11}
$$

它非零，所以这是一条真正新增的必要等式。R174 的已知关系给

$$
y_1=0,\qquad y_2=-2y_0+2y_{12},\qquad
\alpha=-y_{12},\quad\beta=y_0,\quad D_0=y_8.                    \tag{12}
$$

代入 (10)，得到

$$
q_9(y)=256(\alpha+\beta+D_0),                                  \tag{13}
$$

即 (1)。因此在 R174 的完整 corrected action 中，

$$
\begin{aligned}
a(k)&=(1+k^2)(\alpha+\beta k^2),\\
b_2(k)&=-\alpha-\beta+D_2k^2+4B_2k^4. 
\end{aligned}                                                 \tag{14}
$$

这只更新同一 action 的必要形状，全部 $b_0,b_1$、最高四阶层和同一八矩乘子仍须保留。尤其不能由 $D_0$ 可能为负就单独判整个含 0/2/4 层 action 为负。

R174 的十二个独立外坐标中，$D_0$ 原来可自由取值；(1) 现在准确消去它。因此加入这一条后的线性必要外空间恰为十一维。尚未付清的其他真实函数关系可能继续缩小它。

## 5. R177 指定点被准确排除

[R177](R177-explicit-all-layer-positive-point-after-nine-original-relations.md) 的公开指定点已经通过旧 86 条必要行、R174 九式、完整十四族解释和同一八矩乘子核对。其 relevant 参数为

$$
\alpha=\beta=\frac14,\qquad D_0=1.                             \tag{15}
$$

由 (13)

$$
\boxed{q_9(y_{\mathrm{R177}})
=256\left(\frac14+\frac14+1\right)=384\ne0.}                    \tag{16}
$$

所以不存在一个杀 R 的真实线性原函数泛函同时实现 R177 的 107 个已保存值。这已否定将 R177 的严格正标量 action 提升为真实字符的那一步。

本结论没有否认 R177 的标量恒等式、正性或其已过的有限必要行；它证明这些数值尚未尊重完整原函数空间中的全部关系。也没有据此排除其他真实正字符、构造零 period 或宣称固定合法 circle 上的闭合完成。

## 6. 首切实际的完整范围

公开实际为 run **43675575597**，source

**f423160a0ebb0a4239c4bc0b63fece9b3682c86c**，

lane **character_head_word_relations**。

| 项目 | 准确结果 |
|---|---:|
| 已处理字面基列 | 62 / 77 |
| 已完成两根转换的列 | 62 |
| 该前缀的共同代表矩阵 rank | 52 |
| 已付完整原函数关系 | 10 |
| 模旧 $B$、R168、R174 后的新增等式 | 1 |
| 切 R177 的关系 | relation 9，值 384 |
| 直接复用的旧 pure 代表 | 40 |
| 新映射的原分量 | 84 |
| 新处理原 term steps | 33422 |
| 新整数消元 steps | 1487 |
| 独立原列和 / 转换和的列次数 | 各 225 |
| 最大精确系数位数 | 45 |
| cycle fallback | 0 |
| 实际时间 | 17.918837628 秒 |
| peak RSS | 165.29296875 MiB |

十条关系的依赖字面基下标依次为

$$
47,48,50,53,55,56,57,59,60,61.                                 \tag{17}
$$

前九条对继承条件不新增独立等式且在指定点取零；第十条是 (6)。每条均保存完整原差、两根独立零和及三角原列系数。52 是这里明确的 62 列前缀矩阵 rank，不能把它当成全部 head 或字符商的最终维数。

head 的原共享 atom 表完整保留 2332 项；本次只解码 77 个选定完整原根实际可达的 2171 项。161 个不可达生产模板 atom 不参与该 canonical 消费。全部可达颜色严格为 $q,\bar q$，祖先闭包完整，任何可达的其他颜色仍会导致接口失败。

没有重做旧 pure40、31 条 pure 依赖、70 条字面依赖、旧 RREF/LP、旧 86 条必要行、旧 profile 评价或原 forcing/响应编译。

## 7. 原件、源码和保留的失败记录

全部本次原件在

[actions-43675575597-1-character_head_word_relations](../notes/actions-43675575597-1-character_head_word_relations/)。

| 原件 | 字节数 | SHA256 |
|---|---:|---|
| [主报告](../notes/actions-43675575597-1-character_head_word_relations/character-head-word-relations.json) | 12020 | d23d6bee725840a1867a2619494c5d4aea06f4bb5d87e860d825e546969b0a86 |
| [publication receipt](../notes/actions-43675575597-1-character_head_word_relations/receipt.json) | 42910 | 5d3a0cf2c9cd3c27ff64d37adece8994d8f92e42289f5cdeceb23136495dcedc |
| [完整新关系证书 gzip](../notes/actions-43675575597-1-character_head_word_relations/character-head-word-relations-certificate.json.gz) | 295591 | 0a3ee52c6feeeb79229179d022aa614e28e5876bb870ede8a9df237db9815148 |
| 关系证书 raw | 1952812 | 4869604911822f5b0e3872c306b03f5eece4d55cd6a9b8762077d5de779a7fbd |
| [完整续算状态 gzip](../notes/actions-43675575597-1-character_head_word_relations/character-head-word-relations-state.json.gz) | 551408 | 48c260b731c32f9b3e414194d0c5d1b7777305a61b335150c173c9fa4eefb409 |
| 续算状态 raw | 3156394 | 8d6bb1af8832cb732cbc41f36f45d66457cd8a3bd2933aae74bc0ede134826ff |
| [本次新增两项 atom 接口人工](../notes/actions-43675575597-1-character_head_word_relations/character-head-word-relations-atom-selection-development.json) | 2830 | df38c8cfb7924107920d2f7f35a8405c417dff3a4dac5caf685cd4add8a5884c |

两项新增人工在同一公开 run 上全部通过，时间 0.000685013 秒；它们只检查不可达生产 atom 与可达祖先的选择边界，没有重跑此前九项和两项人工。

driver 是 [literature_character_head_word_relations.py](../scripts/literature_character_head_word_relations.py)，79108 字节，SHA256

**1ec5fab96ec173c3e1583b40a124c5c98b3249cec9a87be39db3b3066e31b300**；

固定颜色模块是 [literature_color_priority_words.py](../scripts/literature_color_priority_words.py)，21642 字节，SHA256

**ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9**。

此前两次接口失败继续保存在原公开目录，并由
[首次 manifest 身份说明](../notes/character-head-word-first-actual-manifest-failure-20261115.md)
和
[第二次共享 atom 说明](../notes/character-head-word-second-actual-shared-atom-failure-20261115.md)
准确记录。两次都在绑定输入阶段退出，没有完成研究列或产生可冒作研究前缀的状态；本次是这些接口修正后的首个真实共同 word 比较结果。

## 8. 已保存状态与继续范围

已保存状态的 cursor 为 62，当前没有未完成 map/eliminate/proof 子阶段；其 exact_progress_sha256 是

**41ba785c127e1456f2912e52611ace5850588d52cf77337b81680a09e9dcf6fb**。

状态保存全部已成列、pivot、转换、完整关系与 mapper 缓存。后续使用同一冻结源、同六份输入以及本报告/receipt 的确切 hash，从该 cursor 加上 finish-all-77 继续剩余 15 列，保留已有关系，不重算已成前缀。

当前已经确定的是完整原身份 (6)、必要等式 (1) 和 R177 的排除。完整 77 列的规范核、其他可能的新字符等式以及更新后必要系统的性质，留给这一次真实续算及其后继处理；不会把首切成功当作整个课题的完成。
