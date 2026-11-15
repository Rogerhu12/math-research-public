# D0 完整轴系数的公开实际回执：R150 研究记录

日期：2026-11-15。**实际符号计算记录；成员关系仍未决。** 本次不是资源退出或实现失败，但也没有得到新的原式成员/非成员定理。因此本稿放在 notes；R150 不用来宣布新的正性或可控性结论。

## 1. 实际结果

公开 Actions [43657526246](https://github.com/Rogerhu12/math-research-public/actions/runs/43657526246)，源提交

~~~text
0d5df1843fd829e7c09b17afdead930ec4395f34
~~~

lane 为 h_axis_sharp。实际完成状态为 complete，耗时 **13.469353102 秒**，峰值 RSS **222.5390625 MiB**。独立的 14 项人工开发检查也已在同一 job 中全部通过，耗时 0.007257736 秒；这些人工检查不读取研究输入，也不评价研究 profile。

本次准确形成 [R148](../results/R148-sharp-one-dimensional-highest-action-positivity.md) 要求的同一个两模式完整轴系数

$$
\mathcal D_0
=[h^{-6}\log(h)^0]\left(
Q-\frac13\partial_h(C-\partial_h\beta)
-\mathcal B_{m_2}(N_2)
\right),
\tag{1}
$$

随后取真 profile 权 $-2$。同时保存

$$
\mathcal K_0=\mathcal D_0+\frac{25}{9}J.
\tag{2}
$$

(1) 使用完整未归约 $N_2$；没有借 pure 投影或假设 $N_2\in W$ 删除它。

实际报告确认：

- 轴上原 $A-\beta$ 两模式准确等于 R136 已发表 J；
- 对 $\log h$ 的链式微分在提取常系数之前完成；
- 唯一新增的响应收缩为 $\mathcal B_{r_1}(N_{-2})/8$ 与 $-\mathcal B_{t_1}(N_{-4})/8$，其总和是应从 (1) 扣除的矩阵收缩；
- $\mathcal D_0$ 的两个未分权模式都只含真权 $-2$；
- 原外槽、内槽与共同右锚完整保留。

这里

$$
m_2/u^2=\frac{r_1}{8h^4}-\frac{t_1}{8h^2},
$$

从完整原因子的两条有理记录直接核对；使用的 $N_{-2}$、$N_{-4}$ 分别是未删项的 N2_77、N2_38 原根。

## 2. 已做和未做的成员检验

比较空间由已完成的原式证书给定：

$$
\mathcal S_{-2}
=\mathcal R_{8,-2}
+\mathbb R N^3G+\mathbb R J,
\qquad \dim\mathcal S_{-2}=40+1+1=42.
\tag{3}
$$

本次消费这 42 个已存原列，不重新编译 forcing、不重新构造旧响应、不重跑其依赖或模素数分离。原列标签与 R136 的 J 分离输入逐项绑定，同一个实有理系数向量必须同时适用于两个模式。

声义正确的 word 正规化得到比较列秩 42，但对 $\mathcal D_0$ 留下 **205 项**余式，SHA256 为

~~~text
4127686655c5274d71e550de13dbc14e628ed37b37ac18a4b7543281a61865a5
~~~

实际结论字段为

~~~text
outcome = undecided_sound_remainder
rational_nonmembership_certified = false
weight_minus_two_positive_character_forced_to_kill_J = false
actual_signed_J_control_proved = false
~~~

正规化只保证它执行的恒等式正确，并没有证明其正规形完备。所以 205 项不是原函数非零证书，也不证明 $\mathcal D_0\notin\mathcal S_{-2}$。本次没有进行新的有理 profile 评价或非成员子式搜索。

特别，目前没有得到

$$
\mathcal D_0=R+c_GN^3G+c_JJ
$$

的原式身份，因而不能借 R148 的 $c_J+25/9$ 符号迫任何正字符杀 J；反过来也不能据此宣布存在新的独立成本方向。

## 3. 完整新原根已保存，可直接供后继消费

本次把 D0、K0 及两条未归约 N2 收缩保存为可携原 DAG。共有 **12 根、383 个 profile 原子**，无需再次构造这两个新响应。

| 原目标 | 模式 $-4$ 的原式 SHA256 | 模式 $-2$ 的原式 SHA256 |
|---|---|---|
| D0 | 1236f94a788454870d655dda499714eacccfee730cba582e22fb2c0b4d892f7f | ce6e1dd221080cd0a4961f2cf81b9a1be1f8a276d587b0cd34e0dd884fd83c5f |
| K0 | 4ab920951e1c7c5cd4279dfba3a6929bfb697ff73167bb7791309c4eddf120b9 | 7367fa52fe88a689a54945fef0c2e74060a9f14a3c24ed7226005aa7e56256df |

公开目录：

~~~text
notes/actions-43657526246-1-h_axis_sharp/
~~~

| 文件 | 字节 | SHA256 |
|---|---:|---|
| h-axis-sharp.json | 17542 | e0007757b7d113a34b5c2ec594a607d380855f5652042f67fe3f32c1c81397f0 |
| receipt.json | 36161 | 1d635cdbe80251339d1157cee579c6838cad8975310a80959ef92b171f2458ea |
| h-axis-sharp-original-expressions.json.gz | 14497 | ecd9edf2d461f6d4f6b9355e17e210ad435b20c53bc16baeda412258b8b3fabd |
| h-axis-sharp-complete-report.json.gz | 20660 | d68d7ab257edcee3460af57757f5c3fdfcdea75dd52995783422d8335898fff1 |
| h-axis-sharp-development.json | 6607 | 065d6f3c3882577555d025ce1dfda25c72bebc48de890f63cb0cd181d7a966c1 |

原表达式解压 80444 字节，SHA256

~~~text
2d0433a628b22f223a0f8700cebad02e70305699ff39a65e075de81dad5ceed0
~~~

完整报告解压 63259 字节，SHA256

~~~text
450c0fbb127df93cb8b64c83746f37eff4fd7f75ec7027fd33f22d6adbd39d9d
~~~

本次读取并核对了小型主报告、receipt 和开发报告的原字节；上述压缩输出的长度与双 SHA 来自公开 publisher receipt，与主报告元数据相符，没有通过 API 搬运二进制。

冻结 driver 为 literature_h_axis_sharp_coefficient.py，31222 字节，SHA256

~~~text
7f4ee057a16a620e089102ea9c84fccafd922306e8febf8b73391b478e4a4a0b
~~~

receipt 登记 171 个来源文件。实际消费的三个旧输入分别是完整原因子 run43651096112、G³ 已成原块 run43653293263、J 已成分离 run43654534244；其原导出、主报告、来源与标签绑定均由本次 consumer 核过。预算为 180 秒、软轮询 1024 MiB，实际远低于上限。

## 4. 下一步的最小对象

下一步若要判定非成员，应直接消费本次 D0 原根及 R136 已发原子式，而不重作 (1) 或再次扩大 word 正规化预算。

R136 的小主报告明确保存的是原 42×42 增广子式，即 40 个响应、$N^3G$ 与 J 的完整秩证据；旧完整报告是否另含全部 96 个查询行仍须按其实际内容确认。不能把 42 行误作 96 行。

若只保存了该 42 行，则它已经可作为固定满秩 pivot。只评价 D0 新列后，可以在模素数域解出候选坐标，再从已存原根形成一个候选线性组合，在额外查询上检验真正原式余值。这不需要重跑旧 42 列的全部评价。模坐标始终只是有理 pivot 解的约化，不能当作有理恒等式的系数。

这一后继目标仍只处理 D0，不自动扫描其他状态系数。无论后继得到什么，本次 actual 本身都不增加 $\dim U_4$ 下界，也不支付正性、实际 lineality、完整 ruling 或有限等距族。

