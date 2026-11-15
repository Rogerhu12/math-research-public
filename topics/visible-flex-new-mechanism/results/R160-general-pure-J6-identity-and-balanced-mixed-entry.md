# R160：J6 的一般 pure 恒等与完整 balanced mixed 入口

日期：2026-11-15。**已证明。** 唯一新研究目标在公开仓库 Actions 完成：
R136/R141 的 $J_6=[h^{-2}]\bar A_{kk}$ 的一般 pure 分量，
对 R151 已保存九个真基的准确有理成员门。

准确结论是

$$
\boxed{(J_6)_{-4}=(K_6)_{-4}
\quad\text{对全部共同右 collar 光滑复 profile 成立},}
\tag{1}
$$

其中完整响应 $K_6$ 是第2节的六项有理组合。
新目标只62个原项；提出关系后，完整307项原差经独立 sound 归约准确为零。
本次没有研究 profile 评价、mixed 原根解码、旧40列归约或旧31条依赖重算。

(1) 允许取 $H_6=J_6-K_6$ 为真正的 pure-zero 完整成本向量。
它尚不说明 $J_6$ 完整属于响应空间，也不增加任何维数、
lineality 或实际有符号控制下界。R159 给出的下一准确门是
$H_6$ 的一个 balanced mixed 原差；本稿没有提前运行或宣称该门结果。

## 1. 唯一完整原目标

记

$$
U=\mathcal U_4,\qquad R=\mathcal R_8,\qquad \pi V=V_{-4}.
$$

这里 $-4$ 是弯曲相位模式；本次目标的 profile 仿射权是 $-2$。
两个编号不混同。

[R136](R136-acceleration-coefficient-beyond-response-and-G-orbit.md)
已完整导出 R129 正规加速度的五族两模式原根。
[R141](R141-affine-character-acceleration-covariance-and-J-positivity.md)
candidate 6 的准确身份为

$$
J_6=[h^{-2}k^0\omega^0(\log h)^0]\,\bar A_{kk}.
\tag{2}
$$

该记录只有真权 $-2$，没有未列出的其他 profile 权。
R130 已支付正规系数属于真实 $U$ 的 span 身份。
R134 给出这五族由完整 $v_4$ 决定的分层，本次无需重编 $N_2$ 或其响应。

原始记录 family=A_kk、state_key=[−2,0,0,0]，
family_0191_-4 与 selected_0006_-4 是同一个 pure 原算子；
其 SHA256 为

~~~text
9f28420162242f5899bcbf4bb2398b793935ebad021b8f57bbd1fe129f4a0ab1
~~~

对应完整 mixed 原根 family_0191_-2 与 selected_0006_-2 的 SHA256 为

~~~text
19e1c92b975c9e59df6e2e09432a5cb9c824412fface2b85b47161a7aa10e18f
~~~

本次对第二个 hash 只作完整目标来源绑定，没有解码或计算 mixed 根。
不能因为只查 pure 就把它换成另一条几何系数。

## 2. 同一组完整响应的准确有理组合

沿用 R151 的全局编号

$$
C_{8j+a}=\mathcal B_{P_a}(W_j),\qquad
(P_0,\ldots,P_7)=(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1).
$$

$C_i$ 是完整两模式真实响应，不是独立任意指定的 pure 列。
R151 的九个已存 pure 基中，本次非零系数恰为：

| R151 消费原位置 | R116 全局列 | 二次/第三模板 | 准确系数 |
|---:|---:|---|---:|
| 0 | 0 | $p_0/W_0$ | $-1/64$ |
| 2 | 88 | $p_0/W_{11}$ | $-1/64$ |
| 8 | 41 | $p_1/W_5$ | $-1/128$ |
| 9 | 73 | $p_1/W_9$ | $-1/32$ |
| 10 | 81 | $p_1/W_{10}$ | $-5/128$ |
| 12 | 193 | $p_1/W_{24}$ | $1/256$ |

其余已存三列 $C_{48},C_{112},C_{170}$ 的系数恰为零。
定义完整响应

$$
\boxed{
K_6=-\frac1{64}C_0-\frac1{64}C_{88}
-\frac1{128}C_{41}-\frac1{32}C_{73}
-\frac5{128}C_{81}+\frac1{256}C_{193}.
}
\tag{3}
$$

所有系数在 $\mathbb Q$ 上求得，没有使用模坐标的整数 lifts。
原根已经含完整相位系数，(3) 不再额外乘 $1/16$ 或其他归一化因子。
整式在同一个 profile、右锚和实际响应定义下成立。

## 3. 准确原式证明，而非代表相等猜测

R151 已公开保存：

- 九个真基的完整 pure 原根；
- 每个根的准确 word 代表及对应原 hash；
- 31条 fresh 原式依赖证明和真实九维 span 的上下界。

本次直接读取其中九根与九代表。没有对旧40个原列重新运行归约，
也没有重做旧31个差式或其独立性验证。

唯一新目标的原式有62项，sound 归约得到16项代表，
该代表 SHA256 为

~~~text
9b673df17058db26733569e1a1599a533485a72b0035ab8a5c3a3ca099aed341
~~~

在九个存储代表上求得 (3) 后，从**原 J6 与原六个非零列**重新形成

$$
\Delta_6=(J_6)_{-4}-(K_6)_{-4}.
\tag{4}
$$

这个完整新原差有307项，SHA256 为

~~~text
53958fd1febb5dd07595e9a807c3576923dfc8c00408fe463941d3560458cfab
~~~

一个独立 fresh normalizer 把 (4) 准确归约为零项，
零代表 SHA256 为

~~~text
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
~~~

新目标和新原差的 right-IBP、word 两层均没有 cycle fallback。
输入原 DAG 实际扫描最高 jet 为4，颜色只有 $q$，总次数4，
真 profile 仿射权为 $-2$。

每一步只使用已证明 sound 的同右锚分部积分、word shuffle 和准确
有理运算。所有 primitive 都有正 profile 次数，共同零右 collar
使其右边界项准确消失；左尾从未删除或途中重锚。
因此原差的零证明给全部共同右 collar 光滑复 profiles 的真实函数身份 (1)。

这不依赖 normalizer 完备。若原差非零，只能保留未决；
本次实际得到的是可直接用于原函数的正身份。

## 4. 完整 pure-zero 代表与仿射轨道

令

$$
\boxed{H_6=J_6-K_6.}
\tag{5}
$$

由 $J_6\in U_{-2}$、$K_6\in R_{-2}\subset U_{-2}$ 及 (1)，

$$
H_6\in U_{-2}\cap\ker\pi,\qquad
[H_6]=[J_6]\quad\text{于 }U/R.
\tag{6}
$$

当前没有确定这个商类是否为零，也没有证明它独立于已知
$R+\operatorname{span}\{N^3G,J,\mathcal D_0\}$。
所以 (6) 不给新的真实维数下界。

R89/R105 的真实正仿射作用保持 $R$，且不混合相位模式。因此对全部
$H>0,d\in\mathbb R$，将 (1) 整体输运即得

$$
\boxed{
\pi(\mathsf P_{H,d}J_6)
=\pi(\mathsf P_{H,d}K_6)\in\pi R.
}
\tag{7}
$$

故 $J_6$ 的整个正仿射轨道的 pure 部分均已在响应像中。
这不宣称轨道商维数、轨道 lineality 或任意真实 signed control。
也没有开始一条新的逐次平移计算链。

R141 的权负二正字符满足 $c_0=\lambda J_6\ge0$。
若 $\lambda R=0$，可准确改写为

$$
c_0=\lambda H_6.
$$

这是同一完整算子类的改写，不是符号的新证明，也不使 $c_0$ 自动为零。

## 5. R159 给出的最小完整 mixed 门

[R159](R159-balanced-mixed-faithfulness-after-pure-cancellation.md)
已证明：在 universal pure-zero canonical 空间中，
mixed $-2$ 的双次数 $(q^2,\bar q^2)$ 投影 $\Xi$ 是忠实的。
因此对本次已付的 (5)，

$$
\boxed{\Xi H_6=0\quad\Longleftrightarrow\quad H_6=0.}
\tag{8}
$$

最小的新完整身份检查因此只需从已发 J6 mixed 原根及 (3) 的同六个
完整响应 mixed 原根形成

$$
\Xi\left((J_6)_{-2}-(K_6)_{-2}\right)
\tag{9}
$$

这一条原差。若其 sound 归约为零，(1)、(8) 即给完整 $J_6=K_6$；
无须先生成或重算31个响应 pure 核基。

如果 (9) 留有不完备 NF 余项，仍不能宣布非成员。完整成员问题须再比较
$R^0_{-2}=R_{-2}\cap\ker\pi$ 的31维 balanced 像，
或明确扩大的34维已有 pure 核比较空间，按所问目标区分。
不能将两个空间混称为响应空间。

本稿没有执行 (9)，没有用 pure 身份替代它，也没有提前给它的符号或
成员结论。后继继续只消费已有原根，不重跑本次 pure 或旧31/40数据。

## 6. 唯一公开实际与小人工

[公开 run43660884663](https://github.com/Rogerhu12/math-research-public/actions/runs/43660884663)，
source：

~~~text
b41c6f13ffbe56543d3593acb0b9023d8320e93c
~~~

lane 为 general_pure_J6_membership，attempt 1。
实际 complete；耗时 **0.190484952秒**，峰值 RSS **57.9921875 MiB**。
新脚本为

~~~text
scripts/literature_general_pure_J6_membership.py
23040 B
SHA256 48afb00617c5c5251bde7ab2f7782740ff43bf4318cfd78193137c3343c0f745
~~~

它复用冻结 R157 solver（25604 B，c296f72b…），
只对本次 J6 实例执行新目标和原差。
全部来源链、两份原 manifest、publication receipt、
压缩/解压原导出 hash 与所取原根 hash 均准确绑定。

同 job 六项新增小人工 all_passed，用时0.004361622秒，
RSS27.6953125 MiB。人工只核小接口，不读取研究原根；
真实目标的结论来自上述 actual。

| 工作 | 本次数量 |
|---|---:|
| 新一般 pure 目标 | 1 |
| 新目标有理求解后的 fresh 原差 | 1 |
| 已存真基原根与代表消费 | 9 |
| 新 response/forcing/W/N2/v4 编译 | 0 |
| 旧基重新归约、旧31条依赖重算 | 0 |
| mixed 或 balanced 研究原根解码 | 0 |
| profile、幂尾或几何评价 | 0 |

## 7. 完整可复用证书

公开目录：

~~~text
topics/visible-flex-new-mechanism/notes/actions-43660884663-1-general_pure_J6_membership
~~~

| 文件 | bytes | SHA256 |
|---|---:|---|
| general-pure-J6-membership.json | 64382 | d52e8cea9d0e7db1ca1b5348336ca18e0d7e38ab1e98d8c5ade79b84c9825660 |
| receipt.json | 37243 | 825cfe157853f75513ece5ae728e9a4db15c718b3195d72ead36afe9d2905ae2 |
| general-pure-J6-membership-development.json | 49023 | 28c4fa01d747d99c9328fc8e2a2d4373e5513daa719a1c76e9ba3fbf13a63ef2 |
| general-pure-J6-membership-certificate.json.gz | 15080 | 03e4e377632a7bfea3225d8ef27339bf26567f5aaa818ec7d23f9ce1a74568bd |
| 上一证书解压原文 | 101758 | bd9eabce279313b74dc51adfc1b55c4bac72369544fb7a1ec33c296cfdc246d6 |

完整证书保留唯一 J6 pure 目标、九个已存 pure 原根和新原差，
共11个原根；另保原九个 word 代表、完整有理系数、新目标代表、
fresh 原差代表及全部来源。

主报告字段 one_J6_proposal.coefficients_in_original_global_columns
给出 (3) 的六项准确字符串分数；
result.general_pure_J6_member_proved 为 true。
原差根名是 one_J6_proposed_original_difference。
后继可以严格消费这份成功身份，不需重新运行本目标。

原目标仍只来自 R136 run43654534244 的完整五族导出；
九基和旧依赖仍只来自 R151 run43657785023。
本次没有新建几何、改变 profile 圆或宣布主课题完成。

## 8. 结论范围

已付一般 pure 的六项准确原式身份、完整 pure-zero 代表及其正仿射轨道
pure 像，并给出 R159 的唯一新 balanced 原差入口。

未付 J6 的完整响应成员关系、相对于已有完整43维空间的类、
真实成本符号或任意有符号实现。完整第四 period、ruling、
更高阶、有限等距族与本课题几何完成标准均不由本稿自动得到。
