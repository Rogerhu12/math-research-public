# 完整权重 0 字符头部的最小原式消费设计

日期：2026-11-15。状态：源码和十项新人工入口已准备；没有把尚未运行的人工或实际计算写成通过。研究实现由本课题当前代理负责，结论须以公开 Actions 的真实运行和准确源身份为准。

新脚本：scripts/literature_character_head_zero.py。

源码 42361 字节，SHA256 为 337966b4fb9a417ed62d650cac87ffc4c41bedc9938e11c1520fe1136b53dee4；未挂 Git blob 为 bf002e805a0c6c4c2636b6f24df23308fa42911b。

依据：[R190](../results/R190-complete-weight-plus2-quotient-vanishes-and-remaining-even-weights.md)、[R192](../results/R192-weight-zero-character-multiplier-and-first-order-action.md)、R130/R163 的完整 span 与平移分母，以及 R178/R179、R159 的共同真函数表示。

## 1. 完整目标和范围

本次唯一新目标是完整

$$
H_0=U_0/(R_0+NU_1).
$$

它必须包括十四族全部系数、真正原函数核、同一八矩 cocycle 的平移分母，再给精确有理自由参数。不是孤立一列非成员门，也不是某个有限必要系统的外空间。

成功输出：

1. 权重 0 的完整十四族呈示及全部原模式哈希。
2. 原响应十六列加全部十四族状态系数的共同忠实函数矩阵。
3. 该矩阵的完整核，每条原关系的完整两模式差 SHA、项数和逐列转换身份的准确和。
4. $U_0$、$U_0/R_0$、$H_0$、$(R_0+NU_1)/R_0$ 的真维数。
5. $H_0^*$ 的有理自由参数，每个 normal 坐标及八矩 $c_j,d_j$ 在自由参数中的线性形式。
6. R192 的 $d_{p_1}$ 障碍形式，但不预先用它限制整个 $H_0$。

不判正性，不宣布其他偶权完成，不付实际 signed control，不宣布固定 profile 的 period 或 ruling 完成。旧 −2 头部与正性已经结案，本次不重做。

## 2. 五个只读原输入

以下目录均位于本课题 notes 下。

| 来源 | 目录 | 只消费的内容 |
|---|---|---|
| 完整静态密度及 $W$ | actions-43645177423-1-local_fourth_quotient | 两模式各 197 个静态原根；十六个响应所需的 $W_j$ |
| 3974 完整因子 | actions-43651096112-1-local_fourth_derivative_factors | 原几何记录、八矩标量系数、新权重 0 的 $v_2,v_4$ 投影 |
| 完整五族原根 | actions-43654534244-1-acceleration_layer_mixed | 唯一含权重 0 的 $A_{hh}$ 状态根 |
| 已完成 −2 头部 cache | actions-43665345551-1-character_head_minus2 | 只读已保存的第三输入投影，不重算 −2 目标 |
| 已证明完整 $R_0$ | actions-43649525432-1-g_first_translation | 标签、十六个原列哈希、旧真秩及四条原依赖证明 |

每个输入均同时绑定原 main、receipt、run、source commit、producer 源码、packed/raw 字节数与 SHA、完整 scope。已有 gzip 只在公开 Actions 从仓库读取；不通过集成接口读取、编码或分片。

三个新增直接 helper 绑定：

| 文件 | 字节 | SHA256 |
|---|---:|---|
| literature_character_head_minus2.py | 58856 | fcc41b4d5a640a1ac411e7f6f29622db81c39cb2be37aed7811136418a045f11 |
| literature_character_head_literal_relations.py | 58885 | 80ab553a2dbb35fd4547beaf1b7ad094e831a2cb7f02e4968b867c4654cd9995 |
| literature_color_priority_words.py | 21642 | ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9 |

其余完整旧语义依赖通过冻结 head.source_identity() 继续逐源绑定。不会改旧模块全局 WEIGHT，不调用旧 actual，不重新编 W 或 forcing。

## 3. 只恢复缺失的十六个旧响应原根

R126 原实际：

- run：43649525432；
- source：5852d7d4400859e53dde789b4d63f200d0e0acce；
- 原 driver：literature_G_first_translation.py，26885 字节，SHA256 331fea2c1aef154c4d5866e4708f067c555f9fb61f02a11ee32a7f44d25f01f5；
- main：G-first-translation.json，23923 字节，SHA256 9926a1f7026064c95c297b34da60ed5f1b345bc37753a23e75295cf44792fe82；
- receipt：33085 字节，SHA256 06e5d82a7e7db8922d42347920609c83a3ad0114050cdbbdafc72084c3e25bec；
- G-first-translation-complete-report.json.gz：17734 字节，SHA256 511431508d58a1b6fe3fb783efe6d9c0b9be9005c86c08796d992ad19441a30b；
- raw：74559 字节，SHA256 4f88bc5fa5af321c57953c1eb7316efbd53d7f4d2da21d2b9c933bcaf617ab45。

旧报告没有 portable 响应 DAG，故只按原标签恢复下列已证明保留列：

$$
(0,1,2,3,4,5,7,8,9,10,11,12,13,15,17,19).
$$

原模板字段是 third_index，外方向字段是 quadratic_index。每个 $W_j$ 先核 third_original_sha256；新恢复的完整两模式原根必须逐项等于 original_mode_sha256。总计 16 个响应列、32 个模式原根。

完整 $R_0$ 真维数 16 继承 R126：四条 fresh 原依赖给 20 列的上界；旧真实有理评价的 16 阶非零子式给下界。脚本只核旧证明 metadata、四条依赖整体 SHA 和原枢轴行列式 775740714，不重这四条依赖、旧评价或旧 NF。

本次共同函数矩阵的前十六列必须仍独立。这是新的完整函数矩阵装配条件，不能把旧字面独立误作真独立。

## 4. 不重算任何旧 $N$ 投影

已完成 cache 的 run/source 是 43665345551 / 0aae9a6a85583a9f87415e586d8db2c9c7fea6a7。

主件 15967 字节，SHA256 55320985df05f928caf007016777ecb2413f16c969dca4741b0c2e936f00b940；receipt 39451 字节，SHA256 88bdcf2dadbba25d816e886705b70e7844f698f07917b696698e86ea2770f675。

character-head-minus2-original-expressions.json.gz 为 1247411 字节，SHA256 2c1242e13d253ba352c7ff1b025a91cf564ab2a7cfd93c6bcedc19baa5fac45c；raw 6560138 字节，SHA256 7a93a53aa7fafa1cff76608aceaeac294911ca4f828746913c1b125ae2fd33af。

完整 plan 有 1139 个声明请求、1057 个精确零投影请求和 78 个不同非零输入响应缓存，全部 78 项已完成。每条缓存保存 projected_input_root，及其原 $N$ 根、原几何键、原 SHA、第三权和全部用途。

本次只按 (raw N root, third weight) 取已经保存的第三原输入。多个旧外方向保存同一投影时，其原 SHA、几何键、导数权和投影 SHA 必须一致。

只有在该完整请求 plan、完整 cache、原 source、同一个未降模 $W$ 的 factor export 全部绑定后，非零 plan 中缺失的目标投影才可引用旧“精确空投影”结论。partial、缺失 cache 或失败输出不能证明零。导出元数据逐绑定字段匹配，允许 persisted 等无害额外字段。

## 5. R190/R192 的完整支撑与至多十六个新收缩

十个几何坐标固定为

$$
(h,k,\omega,h_s,k_s,h_{ss},k_{ss},\log h,h_{sss},k_{sss}),
$$

几何缩放指数

$$
\kappa=a_h-a_\omega+a_{h_s}+a_{h_{ss}}+a_{h_{sss}}.
$$

R190/R192 的原式证明允许在模 $W$ 下：

- $N_{2,\sigma}$ 只保 $\kappa=\sigma$ 的原状态系数；
- $N_{0,0}$ 只保 $\kappa=0$；
- $N_{0,1}=(hk-1)\tau_1$，必须保参考常数；
- $v_2,v_4$ 严格协变，权重 0 只取几何指数 0 的原记录。

因此所需新响应为：

| 第三势 | 第三权 | 原状态系数数 | 新外方向 |
|---|---:|---:|---|
| $N_2$ | 0 | 1：$h^{-2}h_s^2$ | $p_1,t_1$ |
| $N_2$ | −1 | 3 | $p_2$ |
| $N_0$ | 0 | 10 | $t_1$ |
| $N_0$ | 1 | 1：$hk$ 并保 $-1$ | $s_1$ |

共至多 $2+3+10+1=16$。以外方向和第三输入 SHA 去重；旧已证空投影或相同原根只会减少实际数。$hk$ 与 $-1$ 共用同一原输入和响应，不额外计一次，也不是倒行取负。

每条新响应均为完整两模式响应，检查结果真权为 0。原八矩的所有标量项都乘回：

$$
L_2=v_2-B_{m_0}N_2-B_{m_2}N_0,\qquad
L_4=v_4-B_{m_2}N_2.
$$

$m_2$ 的 $p_0,p_1,p_2$ 原坐标必须确为零。新 $N$ 代表与旧代表的差在完整 $W$，故替换只改变 $R_0$；不冒原 DAG 逐点相等，也不遗漏完整导数密度。

## 6. 全十四族和同一 $\Gamma$

完整 factor metadata 必须仍有 $N_0$ 79 条、$N_2$ 93 条；每模式 $v_2$ 665 条、$v_4$ 1236 条。几何指数 0 的支撑恰为每模式 10 条 $v_2$、4 条 $v_4$。

已保存五族完整原记录中，唯一含权重 0 的是 $\overline A_{hh}$ 的状态键 $(-2,0,0,0)$。只消费此原根，其余五族权重 0 的空支撑直接来自完整已发记录。四次速度部分仍由完整所选 $\beta,C,Q$ 原根与全部 $B_{m_2}N_2$ 组装。

水平导数必须为

$$
X=\partial_h,\qquad
Y=\partial_k+\frac1{2h}\partial_\omega.
$$

冻结的标量积分分部 helper 保系数链式导数，十四族完整次序是

$$
F_0,\ Q2_0,Q2_1,Q2_2,\
A_{hh},A_{hk},A_{kk},H_1,H_2,\
Q4_0,\ldots,Q4_4.
$$

用同一原八矩逆与参考状态定义

$$
\Gamma m=\sum_i L_0(S_i^*)a_i(m).
$$

$F_0$ 减 $\Gamma m_0$，全部 $Q_2$ 减同一 $\Gamma m_2$。八个规范静态参考值必须原式全零；不能分别拟合低层，也不能将最高层支撑结论当完整密度结论。

## 7. 新完整函数核

列次序为十六个 $R_0$ 原响应，随后为完整十四族每个非零状态系数的两模式原向量。新 normal 数由实际决定，不预设为维数。

每列同时保：

- 模式 −4 的完整 pure $q^4$ 根；
- 模式 −2 的 balanced $q^2\bar q^2$ 根。

R159 的联合忠实性必须两根一起用。没有假设全部 pure 都在 $R$，没有删除 pure，亦没有假设输入相位作用保持成本锥。

两根送入同一个 R178 固定颜色优先级映射。每个 word letter 都须属于 R179 的余类型，共同右锚保持，primitive 不是独立变量。R178 逐列转换身份加 R179 真实单射、R159 联合忠实性，使此共同有理矩阵的秩和核等于完整原函数秩和核。

逐列消分母，以整数向量和原列组合同步精确消元。每条依赖再从已存转换向量重新求和，核两根共同为零；另记完整两模式原 DAG 差的项数和 SHA。字面 DAG 非零也不能丢掉其来源身份。新统一映射的同列来源加准确组合本身就是完整原关系证明，不要求重跑某个旧 NF。

全部列结束后才宣完整核。当前 rank 或部分关系不能提升为整个 $U_0$ 或 $H_0$。这是新的权重 0 完整函数矩阵；不重 −2 的四十/七十七列或旧 NF 目标。

## 8. 完整平移分母与真头部

R163 给低层的同一 cocycle：

$$
D F_0=\partial_\omega F_0-
\sum_i(\partial_\omega F_0)(S_i^*)a_i(m_0),
$$

$$
D Q_2=\partial_\omega Q_2-
\sum_i(\partial_\omega F_0)(S_i^*)a_i(m_2).
$$

最高九族用状态 $\omega$ 微分。不能把低层写成单纯 $\partial_\omega$。

令完整函数核投到 normal 坐标给 $K$，全部平移呈示给 $D$，求

$$
K\nu=0,\qquad D\nu=0.
$$

精确有理消元保原行和归一化轨迹，自由形式回代后逐条代入全部原行核零。由 R130/R163 双向得到 $H_0^*$，不是有限必要外空间。

维数必须同时满足：

$$
\dim U_0=\operatorname{rank}(\text{共同函数矩阵}),\quad
\dim R_0=16,
$$

$$
\dim(U_0/R_0)=\dim U_0-16,\qquad
\dim((R_0+NU_1)/R_0)=\dim U_0-16-\dim H_0.
$$

完整原核关系数必须等于列数减真秩。

静态参考 $\omega$ 导数及 $(h\partial_h-\omega\partial_\omega)$ 导数须通过同一原矩阵逆转到

$$
(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)
$$

的 $c_j,d_j$。八个参考点 $h=1$，故冻结 helper 的参考导数取法准确。参考序号不能直接当矩阵单位坐标。

本次输出 $d_{p_1}$，但不加它为 head 方程。R192 的正字符判据随后才使用它和需选择的乘子参数 $\alpha$；$\alpha$ 不自动成为 head 坐标。

## 9. 预算、失败与最新根规则

实际入口仅接受本公开仓库的 GitHub Actions。默认：

| 资源 | 上限 |
|---|---:|
| 时间 | 240 秒 |
| RSS 轮询 | 1024 MiB |
| 整数/有理 bit | 8192 |
| 表达式及共同字典条目 | 150000 |
| 新 primitive 调用 | 500000 |
| 共享缓存条目 | 500000 |
| 内存 certificate | 16000000 字节 |
| stdout 主摘要 | 95000 字节，参数严格小于 100000 |

RSS 是轮询阈值，不称操作系统硬限制。新整数列初始化、消元及自由形式回代均核 bit cap。

执行最新根 README 第 15 条：不把新可重算数据、证书、cache 或 Actions 输出提交仓库或 Release；不分片。完整 certificate 只在内存形成，记 bytes/SHA 后不持久保存。仅交脚本、全部参数、run/source 与 SHA。可选 --output 只供临时 runner 文件，不能接旧数据 publisher、upload-artifact 或 Release。

主摘要在公开 Actions stdout 给完整 head 形式与证明门状态。超 cap 就给完整摘要原 SHA/bytes 并明确资源退出，不把删减后的输出冒完整呈示。

本版不持久保存跨 run 新 checkpoint。任何中断保准确阶段和已完成新项数，不把 partial 当 head。具体未完成阶段可据实际预算继续解决，但不为续算违反新规则，也不重复旧已成研究目标。

## 10. 十项新增人工

全部为代码准备，尚未运行：

1. R192 原 metadata 的 15 项选择。
2. 有理头部参数化保一个 toy 自由坐标。
3. 新 $D$ 行可杀掉整个 toy 商。
4. 两根联合投影保 pure 和 balanced。
5. 错误 canonical pure scope 被拒绝。
6. $N_{0,1}$ 的 $hk-1$ 参考减项保准确符号。
7. 缺失新响应不能当“模 $R$ 可删”。
8. 完整 cache 逐字段绑定允许无害额外 metadata。
9. partial cache 不能证明缺失投影为空。
10. 冲突的旧投影 aliases 被拒绝。

只生成小型合成对象，不读研究输入，不运行旧人工套件或研究评价。公开 Actions 先 py_compile 新源，再只运行这十项，随后同 lane 进入实际。

## 11. 准确 CLI 与 sparse

人工命令：

```bash
python -m py_compile topics/visible-flex-new-mechanism/scripts/literature_character_head_zero.py
python topics/visible-flex-new-mechanism/scripts/literature_character_head_zero.py --toy-only
```

实际命令：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_character_head_zero.py \
  --static-directory topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient \
  --factors-directory topics/visible-flex-new-mechanism/notes/actions-43651096112-1-local_fourth_derivative_factors \
  --acceleration-directory topics/visible-flex-new-mechanism/notes/actions-43654534244-1-acceleration_layer_mixed \
  --cache-directory topics/visible-flex-new-mechanism/notes/actions-43665345551-1-character_head_minus2 \
  --R0-directory topics/visible-flex-new-mechanism/notes/actions-43649525432-1-g_first_translation \
  --max-seconds 240 \
  --memory-mib 1024 \
  --integer-bits 8192 \
  --max-terms 150000 \
  --max-IBP-calls 500000 \
  --max-cache-entries 500000 \
  --max-summary-bytes 95000 \
  --max-certificate-bytes 16000000
```

需要 scripts 完整依赖目录及 §2 五个旧目录，无其他新增数据目录。建议 lane 为 character_head_zero，采用不保存可重算新输出的 runner 流程。

成功摘要 schema：visible-flex-complete-character-head-zero-v1。

关键字段：

- completion="complete"；
- phase="complete_true_weight_zero_character_head"；
- new_function_kernel_complete=true；
- normal_presentation：完整十四族、normal 数、D 行数和同一规范化；
- new_common_word_matrix：真秩、完整基列、关系数和转换/关系 SHA；
- complete_true_weight_zero_head：全部 normal 记录、真自由坐标、normal/c/d 有理形式、全部维数；
- reproducible_certificate：内存 bytes/SHA，persisted=false；
- positive_character_decided=false，period_or_ruling_paid=false。

末尾单行给准确主摘要 bytes/SHA。成功后立即用真 $H_0$ 接 R192/R194 的协变乘子与全路径正性，不停在原呈示或矩阵报告。
