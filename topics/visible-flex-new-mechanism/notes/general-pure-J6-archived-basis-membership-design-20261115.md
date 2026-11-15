# J6 一般 pure：只消费九个已存真基的单目标设计

日期：2026-11-15。状态：**新源、设计与小人工已准备；真实目标未在本地运行。**
真实研究执行只允许 Rogerhu12/math-research-public 自己的 GitHub Actions。

## 1. 为什么只取这一条

唯一目标是 R141 candidate 6：

$$
J_6=[h^{-2}k^0\omega^0]\bar A_{kk}\in U_{-2}.
$$

它是 R136 已保存的完整正规加速度系数，只有真 profile 仿射权 $-2$。
它的状态键为 $[-2,0,0,0]$，不是只取某条 forcing 的局部片段。
R130 已支付对应真实成本 span 身份；R134 证明这五族正规加速度系数
从完整 $v_4$ 决定，无须新编 $N_2$ 收缩。

R141 的权负二正字符条件中 $\lambda J_6=c_0\ge0$。
这个系数还决定是否可能进入 R158 的 $c_0>0$ 秩一边界。
所以先查一个与当前真实正性问题直接相关的原目标，比无目标扫描
20 个状态轨道或其全部系数更具体。

本次只问

$$
(J_6)_{-4}\in\pi R_{-2}\ ?
$$

R151 已证明右端真实维数恰为9，并保存了九个真基的完整原式及 word
代表。本次不改变这个比较空间，也不重新验证其旧31条依赖。

## 2. 冻结新源与已运行的小人工

新脚本：

~~~text
scripts/literature_general_pure_J6_membership.py
23040 B
SHA256 48afb00617c5c5251bde7ab2f7782740ff43bf4318cfd78193137c3343c0f745
~~~

它直接复用已实际成功的 R157 读取/求解接口：

~~~text
literature_general_pure_D0_membership.py
25604 B
SHA256 c296f72becff4366297e3b9f00db97425b1aa5b15c10ba7625932966ae7c8f1f
~~~

具体复用其 source_identity、load_nine_basis、bind_word_row 和 solve_once。
这些接口保持原文件不变。本脚本独立增加 J6 的精确来源选择和输出范围；
没有把旧 D0 目标换名后重新执行，也不读取旧 D0 的研究原根。

本地只执行过语法检查和新的六项人工接口：

~~~text
general-pure-J6-membership-artificial-development.json
48944 B
SHA256 539bd78b7132a2b78172a948277aec3e32f1a520510f72eb9ce2af8d55d03bde
~~~

人工 all_passed，0.011404082993976772 秒，RSS17.375 MiB。
它们检查唯一状态/原hash选择、公开 Actions 环境谓词、仅选定原根解码、
读已存代表后新有理目标及 fresh 原差、未决余项边界、原表达式 roundtrip。
所有数学值都是小人工；没有读取研究报告或研究原根，没有评价任何
profile/几何、重编 forcing 或运行本次真实目标。

公开 job 仍应先运行同一 toy-only，再运行 actual。不能把这份本地人工
当成本次 J6 研究结果。

## 3. 原目标的完整来源

原 producer：

~~~text
literature_acceleration_layer_mixed.py
47656 B
SHA256 271dd150fe95d280fdf3cad0f5bbb5b5fde6f81631a96e7fdbfeb628711ebf7c
~~~

实际身份：

~~~text
run: 43654534244
source: 1177f251dc3d9455adf88b585e4c0e4bd6f7e69b
lane: acceleration_layer_mixed
directory: notes/actions-43654534244-1-acceleration_layer_mixed
~~~

| 输入 | bytes | SHA256 |
|---|---:|---|
| acceleration-layer-mixed.json | 57753 | baccbf48f39a7fb3296ca4e8a933d18f246a8db317423846e66d9c46374b2745 |
| receipt.json | 35241 | 3c147ca2edaa03d4c27fa0694adca26764c0f98c8fde363387359d8fddccc494 |
| acceleration-layer-mixed-original-expressions.json.gz | 318634 | b3227509c891a2e86e9bcc7823e3d6b3abb0a9ff80975b2e1162a0911739146e |
| 上一文件解压原文 | 1909429 | 7c1e0bda999d2c8958d7e5fdf6d9460f30eb6003eb1c69172ba1ca948dfeac38 |

完整导出有314个两模式 family 记录、10个 selected weight 记录，共648根。
本次只 subset_decode 一根：

~~~text
family_0191_-4
9f28420162242f5899bcbf4bb2398b793935ebad021b8f57bbd1fe129f4a0ab1
~~~

它必须同时与 family A_kk/state_key[-2,0,0,0] 和 selected id6 的
selected_0006_-4 一致。两记录的完整 mixed 元数据也必须一致：

~~~text
family_0191_-2 = selected_0006_-2
19e1c92b975c9e59df6e2e09432a5cb9c824412fface2b85b47161a7aa10e18f
~~~

mixed 只读来源 hash，不解码、归约或评价。没有以“只做 pure”为理由
允许改掉原目标完整两模式身份。

输入读取使用原 layer.read_bound_json/read_bound_export/check_publication，
检查主报告 complete、run/source/repository、完整 source_hashes、
receipt 的主报告/原导出字节和 hash、原导出 schema/scope、全部声明根数、
唯一目标状态、原权与 selected alias。再由 subset_decode 重算所取
pure 原根的原 SHA。其余647根不构造为研究表达式对象。

## 4. 已发表九基与完整旧证据

复用 R151：

~~~text
run: 43657785023
source: c606688a842bd811106ff2844e1161a4f34c159e
lane: general_pure_J_membership
directory: notes/actions-43657785023-1-general_pure_J_membership
producer: literature_general_pure_J_membership.py
producer bytes: 37092
producer SHA256: 1a84590f8b6f0c35a1df5f251a8ffa0e9f4da65ea2cc3bd777e752482ef05bcc
~~~

| 输入 | bytes | SHA256 |
|---|---:|---|
| general-pure-J-membership.json | 45019 | 98442251ed15b708a70e3fcbbdb2ae6cf76c8c1873aa21345354a5a320a9cfac |
| receipt.json | 35841 | 31d6380160437b0098d33d35e4b722c79cd780d351f614a4e48901100a9d0fa4 |
| general-pure-J-membership-certificate.json.gz | 84283 | af46437f676716a20051bf3bad5a96235398dcf8a45c179d1395bc1f9d84712e |
| 上一文件解压原文 | 456216 | 9859368ec20e0923cc168199a7ecb82eff0beac5fa191f1b6388e67cfd1aa550 |

九个 R151 消费位置：

$$
0,1,2,3,8,9,10,12,19.
$$

对应完整响应的 R116 全局列号：

$$
0,48,88,112,41,73,81,193,170.
$$

load_nine_basis 原样检查这两套标签、原根 hash、word 代表 hash、
complete 状态、九维 cover、31条已证明原式依赖及其证据列表 hash。
它只是读取并绑定旧证明，没有重新归约那31个差式。

原九个 pure 根用 subset_decode 读取；其代表通过
decode_word_rows/bind_word_row 还原，不对旧原根再次运行 normalizer。
全模式原40列的真实独立性和九维纯像下界沿用 R131/R151 原结果，
不将本次九个代表的秩误作新的函数独立性证明。

## 5. 唯一新增数学工作

actual 的顺序固定：

1. 读取并核对唯一 J6 pure 原根；
2. 读取九个已存原根与准确代表；
3. 由实际原 DAG 扫描必要最大 jet，确认无 mixed color、总次数4及真权−2；
4. 只对新 J6 pure 作同右锚 sound 归约，在九个存储代表上求一组准确
   $\mathbb Q$ 系数；
5. 从原 J6 与原九根形成完整新原差，用独立 fresh normalizer 归约；
6. 完整保存候选有理系数、原差、所有代表和零/未决证据。

旧模坐标或模整数 lifts 完全不进入有理求解。
原根已经含完整相位归一化；不再外乘 $1/16$、$1/128$ 等因子。
右端积分锚、左尾、全部导数和真实原根身份保持不变。

明确为零的工作量：

- 新 response/forcing/W/N2/v4 构造；
- 旧40原列归约、旧31 pure 依赖重算；
- 任一研究 profile 或幂尾评价；
- 任一 mixed 原根解码、归约或评价；
- 任一 balanced 比较块生成或其旧独立性复验。

## 6. 结论分支

若 fresh 原差准确归零，则报告唯一结论

$$
(J_6)_{-4}=\sum_{i=1}^9a_i(C_i)_{-4}
\quad\text{对所有共同右 collar 光滑 profiles}.
$$

令 $K_6$ 为同一实有理系数的**完整**响应组合，可以准确取
$H_6=J_6-K_6$ 为 pure-zero 向量。然后 R159 才允许将一个后继完整
成员问题转为该 $H_6$ 的 balanced mixed 原式问题。
这一步没有宣称 $J_6$ 完整属于响应、属于现有43维空间，或可取任意
正负真实成本。

如果候选原差仍有 sound NF 余项，则只报告未决，完整保存余项。
不完备 NF 非零不是函数非成员；本次没有原有理分离分支，
也不自动扩成新的采样、其他状态或完整 mixed 扫描。

预算超限或接口失败保留准确 status/error。早期完整原根和九代表
证书已经先写出；它们不冒充数学目标完成。

## 7. 输出、边界和可复用性

主报告为 general-pure-J6-membership.json，严格小于100KB。
如有必要，完整大正文另存 gzip，紧凑主报告保留来源、状态、结果和完整
文件元数据。

原证书为 general-pure-J6-membership-certificate.json.gz：
完成时包含唯一新目标、九个已存 pure 原根和唯一新原差，共11个原根，
以及九个准确 word 代表、新目标代表、fresh 原差代表、
有理全局列系数和完整来源。它可供后继只消费结果，不重算本次目标。

默认有限预算：180秒、1024MiB轮询内存、500000系数节点、
100000 profile atoms、120000项、每normalizer 500000 IBP calls、
有理位宽8192。主报告90000B、原证书1.5MB、完整正文2MB，
总和不超过既有发布预留上限。脚本是单进程、单目标，不生成额外 lane。

## 8. 公开 Actions 接线

建议 lane 名：general_pure_J6_membership。

新增数据 sparse 仅需以下两个已发布目录：

~~~text
topics/visible-flex-new-mechanism/notes/actions-43654534244-1-acceleration_layer_mixed
topics/visible-flex-new-mechanism/notes/actions-43657785023-1-general_pure_J_membership
~~~

所有源码依赖均已在该课题 scripts 中发布；本次只新增一个脚本。
原 producer 和 R157 solver 一律冻结不改。

公开同 job 先执行小人工：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_general_pure_J6_membership.py \
  --toy-only \
  --output /tmp/general-pure-J6-membership-development.json
~~~

再执行唯一 actual：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_general_pure_J6_membership.py \
  --family-directory topics/visible-flex-new-mechanism/notes/actions-43654534244-1-acceleration_layer_mixed \
  --basis-directory topics/visible-flex-new-mechanism/notes/actions-43657785023-1-general_pure_J_membership \
  --max-seconds 180 \
  --memory-mib 1024 \
  --output /tmp/general-pure-J6-membership.json
~~~

只由公开仓库现有终端 Git 发布器发布本次 main、development、certificate
及可能的完整报告 gzip；不通过集成工具分片或编码搬运大导出。
根代理负责 request、workflow、实际 dispatch、公开 receipt 与结果登记。
本设计没有将上述 actual 命令在本地执行。
