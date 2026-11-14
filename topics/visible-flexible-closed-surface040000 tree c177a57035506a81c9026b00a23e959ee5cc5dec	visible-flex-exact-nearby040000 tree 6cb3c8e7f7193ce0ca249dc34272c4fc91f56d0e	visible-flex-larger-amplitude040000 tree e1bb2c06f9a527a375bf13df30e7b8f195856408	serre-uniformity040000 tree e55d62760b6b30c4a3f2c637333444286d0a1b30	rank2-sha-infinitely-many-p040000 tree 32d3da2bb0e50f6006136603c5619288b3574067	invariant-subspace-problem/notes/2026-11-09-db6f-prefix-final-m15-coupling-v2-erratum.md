# 最终 M15 准备器 v2：cut jets 数值门修正

2026-11-09，`/root/coupled_prefix`。状态：**纯元数据修补和真实 quarter 字段 fixture 已实际完成；v2 仍待独审，最终 s=1 成功分支尚未执行。** 不运行求解器，不改变物理问题或数值方程。

## 1. v1 的具体漏洞与历史范围

已冻结 v1 `scripts/db6f-prefix-prepare-final-m15-coupling.py` 的 SHA256 为 `22e43581c929145483b704673eb767cabfc1961eb41400595f1a289caf59855e`。`tail_theory` 指出其中 `finite_tree` 把 `None`、字符串和布尔值也当作合法叶值，所以一个含 `null` 的数值 jet 可能通过“非有限数”检查；同时没有强制 `height/slope/second` 的长度。JavaScript JSON 序列化非有限数可产生 `null`，因此这属于需要修补的实际验收门漏洞。

本次保留 v1 原字节及旧 gate/restart 报告、旧计划、root 的历史初审，不覆盖或撤回真实已完成的 restart-only 核查。此前只实际执行过 v1 的“当前 continuation 未闭合”拒绝路径，**没有**依据 v1 放行最终目标或启动最终 prefix。旧初审不能作为修正版最终正分支的替代。

## 2. 最小 v2 差分

新文件 `scripts/db6f-prefix-prepare-final-m15-coupling-v2.py`，SHA256 `8b235dfd97d558fc16e446b65bff2412642b041b9bbe6efb193fc88147426b81`。

相对 v1 只替换原递归谓词及其唯一调用点：

- 键集合必须**恰为**原 `cutJets` 的 14 个标量键和 `height/slope/second` 三个向量键；
- 标量均为有限 `int/float`，明确排除 bool；
- 三个向量必须是 JSON list，各长度等于正整数 $M$，每个元素同样有限且不是 bool；
- 缺键、额外键、`null`、字符串、bool、非有限数或错误数组长度均拒绝。

字段集合取自原真实已闭 $s=.25$ 响应，并与原 `cutJets` 返回结构吻合。所有其他已审门、源绑定、原 argv、配置来源、默认边界 warm 校正和未来启动方式都没有改变。最终绑定仍记录执行的准备器本身 SHA，因此 v2 与历史 v1 可区分。

原计划中的准备器命令现应使用 **v2**：

```bash
python scripts/db6f-prefix-prepare-final-m15-coupling-v2.py --check-current-gate
```

只有真实 continuation02 完成 $s=1$/Jacobian/source audit，并有 root 实测自然退出和四件最终文件身份记录之后，才能用 v2 的 `--observed-execution` 生成 ready launch。其他命令旗标沿用旧计划；本稿不声称该条件已经成立。

## 3. 真实 quarter fixture 与拒绝例

独立的小验证入口为 `scripts/db6f-prefix-final-m15-cut-jets-fixture.py`。它只读已闭响应
`2026-11-09-db6f-prefix-amplitude-recovery-s025-iter004-01_tail_0001.json.gz`，SHA256 `07db124d2da380171b99e6d577255b43d4f5496fbd6d982d5dea1a6df873c2e5`。
该数据是原有限 $M=15,s=.25$ 的真实成功 warm，`audit=None`；**没有把它改写或冒称为 s=1 结果**。

验证实际 exit 0：原真实 jets 通过；对它的内存深复制注入 86 个错误案例，全部被 v2 拒绝。案例覆盖每个标量的 null/string/true/false、三个数组首项的同类错误、三个数组过短/过长/整体 null、无穷与 NaN、缺键/额外键及整体 null。特意复现了 v1 对 `backgroundSlope=null` 的错误接受，证明验证触达本次修正的真实差异。

这些错误副本只存在于内存；没有写出任何伪造 solver response、s=1 packet 或伪 continuation 成功记录。原 quarter 文件 SHA 在前后核对不变；fixture 没有调用完整准备门或数值 solver。

输出 `2026-11-09-db6f-prefix-final-m15-cut-jets-fixture.json`，SHA256 `ebaa95d264e4a46bf22862d0fd520db14d4d9f16298cf5c03d894d303388e140`。只保存字段名、案例标签、接受/拒绝结果和输入/源码身份，不保存错误数据数组。

重放时使用一个新输出名：

```bash
python scripts/db6f-prefix-final-m15-cut-jets-fixture.py \
  --output notes/2026-11-09-db6f-prefix-final-m15-cut-jets-fixture-NEW.json
```

本修补只让准备器准确拒绝坏元数据，不产生新的数学解，不解释或改变任何现有 solver 残差，也不代付最终 s=1 审计、prefix 联解或 README G5。
