# P1 全函数检验：全深度 word/shuffle 与带右锚的局部 IBP

日期：2026-11-14。状态：准确代数改写规则已证明，独立小型人工接口检查已执行；研究目标的新正规化尚待公开 Actions。没有取值任何研究 profile、几何积分或曲面，也没有支付完整第四 range。

## 1. 实际旧结果提示的具体缺项

公开 run `43628716304` 的原 producer 在 $2.1211$ 秒内完整结束。目标从 $473$ 个原始项改写成 $59$ 项，$28$ 个响应的显示代表秩为 $18$，消元留下 $76$ 项。没有预算失败，但这不是全函数非成员定理。

旧 `RightIBP` 有局部唯一最高 jet 的分部积分、单层 shuffle 和同一原语的幂规则。它没有把任意深度的原语乘积都展开。例如令

$$I(f)(x)=\int_r^x f(t)\,dt,$$

则准确恒等式为

$$\begin{aligned}
I(f)I(gI(h))={}&I(fI(gI(h)))\\
&+I(gI(fI(h)))+I(gI(hI(f))).
\end{aligned}\tag{1}$$

取人工符号输入 $f=q,g=xq,h=q^2$，旧层在 (1) 的两边之差留下 $3$ 项；新层归为零。这是明确的旧层遗漏实例，不是对实际 $76$ 项余式已经消失的声称。旧报告只保余式哈希；新脚本另外保存有共同原语定义的可读目标和余式，以供后续纸面分析。

## 2. 同一右锚的 word 表示

令局部 monomial 为

$$m(x)=x^p\prod_\ell q^{(j_\ell)}(x).$$

一个 word $w=(m_1,\ldots,m_k)$ 表示

$$I_w=I(m_1I_{(m_2,\ldots,m_k)}),\qquad I_{\varnothing}=1.\tag{2}$$

一般表达式保存为有限和

$$\sum_{L,w}c_{L,w}L(x)I_w(x),\qquad c_{L,w}\in\mathbb Q.\tag{3}$$

$q$ 是同一紧物理区间 $I\Subset(1,\infty)$ 上任意普通复值光滑函数，并在共同右 collar 中恒为零。所有乘法都是普通复乘法；没有 Hermitian 共轭，也没有把左尾重置为零。物理公式中正的右尾 $J$ 始终是 $-I$。

这里 profile weight 是局部因子与所有 letter 中 $q^{(j)}$ 的总次数，不把 $x$ 次数计入。三阶括号的 weight 为 $3$，第四响应和目标为 $4$。去掉纯 $x$ 前 letter 后，每个 word letter 的 weight 至少为 $1$，因此本次 word 长度最多为 $4$。这限制了 shuffle 深度，但不自动限制项数或最高 jet 阶；脚本仍有显式展开预算。

## 3. 两条实际使用的准确恒等式

### 3.1 任意深度 shuffle

对两个 word $v,w$，

$$I_v I_w=\sum_{u\in v\shuffle w}I_u.\tag{4}$$

重复 letter 必须按 interleaving 的重数计数。例如 $I(q)^4=24I_{(q,q,q,q)}$，不能把相同 word 去重后当成系数 $1$。

证明可以按总长度归纳。对两边求导，左边按乘积法则分别从 $v$ 和 $w$ 去掉首 letter，右边按 shuffle 首 letter 的来源分成这两组。归纳假设给相同导数；两边在共同右端都为零，因而相等。该证明不要求 $x>r$，所以适用于这里 $x<r$ 的带符号右原函数。

实现使用完整递归 shuffle，不要求两个 word 的内部原语是一层。

### 3.2 局部导数与任意 word 的 IBP

设 $F$ 是局部多项式函数。只要右边界乘积 $F(r)I_w(r)=0$，就有

$$I(F'I_w)=FI_w-I(FI_w').\tag{5}$$

当 $w\ne\varnothing$，$I_w(r)=0$，所以允许 $F$ 是纯 $x$ 多项式，且无需令 $F(r)=0$。当 $w=\varnothing$，脚本只在 $F$ 有正 profile weight 时使用 (5)，由右 collar 得到 $F(r)=0$。

若一个局部 monomial 中最高 jet 只出现一次，把该 jet 降一阶得到候选 $F$，准确展开 $F'$，然后使用 (5) 把余项和对 word 的导数一同保留。对非空 word，

$$I_w'=m_1 I_{\mathrm{tail}(w)},$$

所以导数项是已知的较短 word，不能丢掉。

特别地，纯 $x$ 的前 letter 可按

$$I(x^pI_w)=\frac{x^{p+1}I_w}{p+1}
-\frac{I(x^{p+1}I_w')}{p+1},\qquad w\ne\varnothing,\ p\ne-1\tag{6}$$

消去。当前多项式模型不需要 $p=-1$；若调用遇到对数或无 word 的纯多项式原函数，会明确拒绝，绝不默默丢掉涉及 $r$ 的积分常数。

改写循环的保守 fallback 是保留原本准确的 word，不能把未处理项判成零。小型人工检查中未触发 fallback；研究输出会另报实际次数。

## 4. 如何复用旧 producer，哪些判断才成立

新文件为

`scripts/literature_pure_bulk_word_normal_form.py`。

它直接导入原 `literature_pure_bulk_exact_membership.py`，绑定其 SHA256

`f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70`。

底层 R56 compiler 继续由原脚本绑定 Git blob `01c7424af3a96f2c2a0f0cb0c782b2037ff3ec74`。旧源码与旧实际输出完全保留。研究路径依次是：

1. 原函数生成同一个 $\mathcal P[q]/16$ 目标；仍先完成真实 $s$ 微分，再置入历史值为零，不能反过来丢掉历史 RHS。
2. 对每个原始 $\Phi_i,\Phi_j$，形成准确三阶对角括号 $\tau_{ij}$。先用旧层、再用 word 层改写，转回同一个实际 profile 代数。
3. 形成同一个响应

   $$H_A(\tau)=\frac{D\tau(q)[A(q,q)]-2A(q,\tau(q))}{8}.\tag{7}$$

   因 $A(q,q)$ 在右 collar 为零，沿此方向的 Fréchet 微分保留所用的右锚恒等式。原始括号同时保留给后面的独立正证书。
4. 对 word 代表作准确有理消元。这次会消去所有可用 pivot，即使更早某一行不在 pivot 集内；旧助手在第一个不可消 pivot 停下。这只使剩余表达式更便于阅读，不改变“是否属于代表张成空间”的答案。
5. 对得到的每条 column null relation，从**原始未改写三阶括号**重新形成响应和组合，再由新的改写实例核为零。若目标关系存在，同样从原始目标与原始括号重验一次。

所有改写都是函数恒等式，因此成功核过的 column relation 是真实普适函数关系；若核出 $28-d$ 条独立关系，$d$ 就是实际响应函数空间维数的一个上界。但是没有证明 word 代表的所有剩余行作为函数线性独立，所以不能称此上界为真实维数，不能把不匹配余项当成真正 obstruction。

目标匹配若成功，支付的也只是这里的标准互反对纯 $P_1$ 局部漂移。真实基准桥的第三局部项、其他相位模式、$P_0$、ruling 与有限等距族都仍是不同问题。

## 5. 输出能看见什么

主报告保存目标、$28$ 列、span 余式、消元系数、已重验的列关系及资源计数。另输出同 stem 的 `-expressions.json`，其中有：

- $q_j=d^jq/dx^j$ 的可读 monomial；
- 共用的 $W_i=I(m_iW_j)$ 定义，依赖有序；
- 完整目标和完全消元后的余式；
- 准确关系 `remainder = -target - sum(coeff*response)`。

该可读文件限 $95$ KB。若整个表达式超过此限，报告会显式标 `all_expression_rows_included=false` 并保留总项数、完整表达式哈希与可复现脚本；不会把截取的几项伪装成完整余式。原始大结构不读入对话。

默认资源界为 $240$ 秒、$500000$ 系数 DAG 节点、$60000$ profile atoms、$80000$ 项、$250000$ primitive calls 和 $2$ GiB RSS 轮询界；这不是 OS 硬限制。准确有理消元另设 $8192$ bit 上限。预算触发会写部分状态并退出 $2$，不得解释为不匹配。

## 6. 已执行的人工检查与公开命令

只在本地执行了 `--toy-only`。$13$ 个检查全部通过，包括完整三/six shuffle、重复 word 的 $24$ 重数、导数击中任意嵌套 word 的 IBP、纯多项式右端常数保护、转回旧代数的真实导数、$r_0/r_1$ 括号的准确 $I((q'')^3)/3$ 符号，以及有不可消行时继续消后续 pivot 的小型有理消元。没有编译真实研究目标。

人工输出是 `notes/literature-word-normal-form-development-check-20261114.json`。它记录旧层在 (1) 的人工例子余 $3$ 项，新层为零。

公开 Actions 的实际入口：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_pure_bulk_word_normal_form.py \
  --out "$VISIBLE_OUT/p1-bulk-word-normal-form.json"
```

若只运行人工路径，加入 `--toy-only`。研究入口同时检查 `GITHUB_ACTIONS=true` 和 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。无需为相同来源再安排机械的重复核验门；下一实际结果应直接用于读取余式结构、发现准确关系或明确下一缺失的代数恒等式。

## 7. 公开开发实际通过

run43629844644/source6eceaa90的higher_range_development成功执行本脚本13项toy，全部true，旧层遗漏的人工3项差在新层为零。该run整体失败来自另一个height loader，与本lane无关。现在请求p1_word_exact实际原target/28响应与可读表达式输出；预算和阴性范围不变。
