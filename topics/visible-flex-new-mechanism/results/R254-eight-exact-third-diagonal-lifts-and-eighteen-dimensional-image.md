# R254：八个完整第三对角提升及真实十八维对角空间

日期：2026-11-15。**公开 Actions 实际已完成，八个新原差全部准确为零。** 本文直接消费 run **43707570035**、source **282173404f65d5cc7b1dee61c66c69c3ca17866c**、job **132791905419** 的完整 stdout 和原回执；没有在本地重算任何 profile、旧原式、旧正规化或科学矩阵。

本次给出八个额外完整第三模板的准确交换子提升。减去提升后得到八个明确的、完整三槽非零而对角为零的算子。必要输入恢复的十八个规范参考均取得独立枢轴；结合 R179 的真实函数独立性和 R208 的既有上界，可进一步确定
$$
\dim\Delta W=\dim\Delta W_{71}=18,\qquad
\dim Z_{71}=10,\qquad \dim Z=18.
$$
这不确定完整第四响应秩，也不解决固定圆的完整 period/ruling 联调。

作者责任：本文区分公开实际记录、由已发表定理推得的数学结论及仍未支付的范围；所有新科学运算均在本仓库公开 Actions 进行。

来源：[R71](R71-third-holonomy-commutators-and-complete-fourth-P1.md)、[R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md)、[R87](R87-exact-complete-P1-separation-and-smooth-moment-circles.md)、[R178](R178-fixed-color-priority-IBP-and-terminating-shared-word-map.md)、[R179](R179-universal-independence-of-fixed-color-remainder-words.md)、[R208](R208-every-universal-pure-response-has-a-second-jet-representative.md)、[R247](R247-complete-response-Jacobi-presentation-and-pure-kernel-decomposition.md)。

## 1. 原三槽、索引与同一右锚

沿 R247，$E=E_8$ 的坐标顺序为
$$
(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1).
$$
对称二次算子为 $\Phi_A$，完整第三交换子为
$$
C(A,B)(a;b,c)
=\Phi_A(a,\Phi_B(b,c))-\Phi_B(a,\Phi_A(b,c)).
\tag{1}
$$
外槽 $a$ 与对称内槽 $b,c$ 全部保留。把所有 $i<j$ 按上述 E 坐标顺序作字典序枚举，所得原索引 $0,\ldots,27$ 的算子记为 $C_i$。例如
$$
C_2=C(p_0,r_0),\quad C_{20}=C(r_0,s_1),\quad
C_{24}=C(r_1,t_1).
$$

所有 primitive 均按原方向
$$
I(F)(x)=\int_{r_*}^{x}F(\xi)\,d\xi
\tag{2}
$$
解释；输入在共同右 collar 恒零，保留完整左尾。本文没有更换左右锚，也没有把 primitive 数值作为独立常数赋值。

原 152 个完整模板中，已发表 v2 原差保留的 36 个索引为
$$
0,\ldots,27,\quad30,32,34,37,40,100,104,109.
\tag{3}
$$
前 28 列张成 $W_{71}$；后八个原模板记为 $\tau_j$。R87 已用完整原函数有理子式证明这 36 列独立，因此
$$
\dim W_{71}=28,\qquad \dim W=36,\qquad
W=W_{71}\oplus\operatorname{span}\{\tau_j\}.
\tag{4}
$$
(4) 是既有事实，本次没有重跑该独立性或全部 152 列。

八个额外模板的来源仍是：

| 原索引 $j$ | v2 保留位置 | 完整来源 | 状态 monomial |
|---:|---:|---|---|
| 30 | 28 | R77 area | $h^{-5}k$ |
| 32 | 29 | R77 area | $h^{-4}$ |
| 34 | 30 | R77 area | $h^{-4}k^2$ |
| 37 | 31 | R77 area | $h^{-3}k$ |
| 40 | 32 | R77 area | $h^{-2}$ |
| 100 | 33 | R79 h-shape | $h^{-2}k$ |
| 104 | 34 | R79 h-shape | $h^{-1}k^2$ |
| 109 | 35 | R79 h-shape | $k$ |

令
$$
\Delta\tau(q)=\tau(q;q,q),\qquad
Z=\ker(\Delta|_W),\qquad Z_{71}=Z\cap W_{71}.
\tag{5}
$$
本次任务是对这八个 $\tau_j$ 给出具体 $\gamma_j\in W_{71}$，并从完整原式准确核验 $\Delta(\tau_j-\gamma_j)=0$。

## 2. 八个准确提升

公开实际得到以下八个有理公式：
$$
\begin{aligned}
\gamma_{30}&=\frac{3C_2+C_{20}}{256},\\
\gamma_{32}&=\frac{C_3-3C_4-C_8}{128}-\frac{C_{21}}{512},\\
\gamma_{34}&=-\frac{C_3+5C_4+3C_8}{128}-\frac{3C_{21}}{512},\\
\gamma_{37}&=\frac{C_5+C_9+2C_{10}}{32},\\
\gamma_{40}&=-\frac{C_{11}}{32},\\
\gamma_{100}&=-\frac{C_5}{8}-\frac{C_{10}}4-\frac{C_{24}}{32},\\
\gamma_{104}&=\frac{3C_0}4+\frac{C_6}{16}
+\frac{3C_{11}}8-\frac{3C_{14}}{16},\\
\gamma_{109}&=-\frac{C_{12}}4.
\end{aligned}
\tag{6}
$$
未写出的原 28 坐标均为零。取
$$
\boxed{\chi_j=\tau_j-\gamma_j.}
\tag{7}
$$
八个新核验均从 (7) 的完整三槽原 DAG 开始，再同时把三个槽代为同一 $q$。独立的 fresh word 转换给
$$
\boxed{\Delta\chi_j=0
\quad(j=30,32,34,37,40,100,104,109).}
\tag{8}
$$
这些是所有允许光滑 profiles 上的普适同右锚函数身份，不只是在某个幂尾、某个圆或有限采样上为零。

完整 $\chi_j$ 没有被置零。由 (4)，它们在 $W/W_{71}$ 中分别与八个 $\tau_j$ 同类，故八个 $\chi_j$ 的完整商类独立，尤其每个完整 $\chi_j$ 都非零。该非零性来自 R87 的真实独立性，**不是**从原 DAG 的项数非零推得。

本次输出的原差大小及最后核验为：

| 原索引 | 完整 $\chi_j$ 原项数 | $\Delta\chi_j$ 原项数 | fresh 规范余项数 |
|---:|---:|---:|---:|
| 30 | 25 | 15 | 0 |
| 32 | 46 | 24 | 0 |
| 34 | 49 | 26 | 0 |
| 37 | 76 | 44 | 0 |
| 40 | 75 | 42 | 0 |
| 100 | 88 | 49 | 0 |
| 104 | 125 | 68 | 0 |
| 109 | 81 | 45 | 0 |

八个 fresh 零代表的 SHA256 都为
**4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945**。
完整原根、提升和原差的 SHA 分别列在附录 A；零代表哈希不是单独的数学证明，证明是原式绑定、完整代入和 sound 转换三者共同给出。

## 3. 本次实际核验的准确范围

旧 closed-C1 实际只用作十八个参考的选择来源。本次必要恢复集合为
$$
\mathcal I=
(0,1,2,3,4,5,6,7,8,9,10,11,12,14,18,20,21,24).
\tag{9}
$$
它们都是原前 28 个交换子。读入已发表 W-only 原表达式后，新的驱动：

1. 解码 36 个完整原根，只为核绑定逐根 SHA；没有重编第三或第四 forcing。
2. 只对 (9) 的 18 个必要参考及本次八个新目标取三槽对角；其余 10 个根没有对角化。
3. 对固定参考作准确有理消元，求八个目标在参考空间中的坐标。目标残余没有被加作新参考，也没有假定参考秩为 18。
4. 用所求坐标在原 colored DAG 中构造完整 $\gamma_j,\chi_j$，然后再取 $\Delta\chi_j$，以另一套新 mapper 从原差开始验证 (8)。
5. 对全部存活 letter 检查 R179 的固定颜色余类型；两套 mapper 的 cycle fallback 都为零。

步骤 4 因而不是把求解器已经消成零的行再打印一次。完整外槽、内部原函数和所有左尾均在新原差里保留。每个新公式既有可读有理坐标，又有原式层的独立核零。

旧 bound_W.original_152_hashes_matched 是已发表生产者的来源绑定，本次继承它；本次重新匹配的是已保存的 36 个根与 v2 保留根的真实 SHA。没有把这两件事写成“本次重算全部 152 原差”。同样没有重跑旧 151 对角空间、旧 116 个依赖、P1、旧 pure/完整第四响应，或全部 3974 局部原因子。

## 4. 十八个枢轴的真实函数后果

### 4.1 这次观测的十八个枢轴

主报告明确记录：

- word_span_pivot_count_for_solving = 18；
- independent_input_positions_used_by_solver = [0,...,17]；
- rank_eighteen_not_assumed = true；
- all_surviving_letters_checked_against_R179 = true。

这里的 18 是为八个新目标恢复必要参考时已出现的准确枢轴数，不是另派一次旧 151 列求秩。所有十八个最终代表只有颜色 $q$，最高局部 jet 阶为 2、最大 word 长度为 1；各代表 SHA 见附录 B。

### 4.2 为什么这不是只有形式代表的秩

R179 的准确文件是
[R179-universal-independence-of-fixed-color-remainder-words.md](R179-universal-independence-of-fixed-color-remainder-words.md)，
15431 B，SHA256
**f995fb7dc54eed828dcb0bee46b0469adead408724a48c58c68045d45add07c6**。

其第 1 节主定理及第 6 节式 (19) 证明：在同右 collar、任意小自由开区间内的光滑输入和整个查询区间上，固定颜色余 letter 的规范 word 解释是单射。单色集合 $\{q\}$ 正是该定理允许的情形。它不把 primitive 当独立数值，而是用真实紧支撑 packets 和局部 jet 变化分离规范系数。

设 (9) 的十八个原函数有一个常系数线性关系。sound 转换使其规范代表的同一线性组合评价为零；R179 单射迫该规范组合本身为零。实际十八枢轴又迫全部系数为零。因此这十八个原函数真实独立。

R208 第 2 节已由旧全部 151 列的 sound 覆盖给出
$$
\Delta W=\Delta W_{71},\qquad \dim\Delta W\le18.
\tag{10}
$$
本次十八个真实独立参考给反向下界，故
$$
\boxed{\dim\Delta W_{71}=\dim\Delta W=18.}
\tag{11}
$$
(11) 是对原完整函数空间的结论。没有假定某一个固定圆、三矩受限输入子集或固定输出点仍忠实。

### 4.3 对角核和模类型

由 (4)、(11) 及秩零度公式，
$$
\boxed{\dim Z_{71}=28-18=10,\qquad
\dim Z=36-18=18.}
\tag{12}
$$
结合 (7)、(8) 和完整商类独立，得到具体分解
$$
\boxed{
W=W_{71}\oplus\operatorname{span}\{\chi_j\},\qquad
Z=Z_{71}\oplus\operatorname{span}\{\chi_j\}.
}
\tag{13}
$$
这里第二个新增加项恰为 8 维；$\gamma_j$ 的选择在 (9) 所张参考空间内固定。若允许另加 $Z_{71}$ 元素，可得到其他提升，不改变 (13)。

还有一个无需新原式计算的表示论后果。R247 第 6、7 节已给
$$
W_{71}\simeq2V_6\oplus V_4\oplus3V_2,
$$
以及真实七维 hook 串 $\mathcal H_7\simeq V_6\subset Z_{71}$。三槽对角映射与该三个导子交换，所以 $Z_{71}$ 是子模。有限维 $\mathfrak{sl}_2$ 模完全可约，(12) 使除去这个 $V_6$ 后只余三维；$W_{71}$ 内没有平凡模，也没有维数二的类型。于是
$$
\boxed{Z_{71}\simeq V_6\oplus V_2.}
\tag{14}
$$
(14) 只确定类型；本次没有求出余下 $V_2$ 的具体三条完整原式。也没有据此断言八个 $\chi_j$ 张成的补空间对非仿射导子 $\delta$ 封闭。

## 5. 对完整 pure 零响应的可用结论

沿 R247，完整响应为
$$
\mathcal B_A(\tau)(F,\phi)
=2\tau(\Phi_A D;D)-4\tau(\phi;\phi,\Phi_A D)
+4\Phi_A(\phi,\tau(\phi;D)),\qquad D=F-\phi^2.
\tag{15}
$$
R80/R247 给其 pure 投影
$$
\pi\mathcal B_A(\tau)(q)=
\frac18\left\{
D(\Delta\tau)(q)[\Phi_A(q,q)]
-2\Phi_A(q,\Delta\tau(q))
\right\}.
\tag{16}
$$
因此 (8) 使 64 个明确完整响应定义
$\mathcal B_{e_i}(\chi_j)$ 全部 pure 零。这里 **64 是定义的数量**；本次实际新评价的第四响应数量是 **0**，没有证明这 64 个响应独立。

令 $\mathcal R_{71}=\mathcal B(E,W_{71})$，
$\mathcal R_{\mathrm p0}=\mathcal R\cap\ker\pi$，其中 $\mathrm p0$ 是全权 pure 核。R247 的穷尽分解现有具体提升可直接代入：
$$
\boxed{
\mathcal R_{\mathrm p0}
=(\mathcal R_{71}\cap\ker\pi)
+\operatorname{span}\{\mathcal B_{e_i}(\chi_j)\}.
}
\tag{17}
$$
不能删去第一项：第三对角核产生的第四响应不必覆盖全部第四 pure 核。两个响应像也未证明直和。

完整响应的既有范围
$$
228\le\dim\mathcal R\le232,\qquad
164\le\dim\mathcal R_{71}\le168
$$
仍按 R247 保留。本次不把任何上界改成等号，也不推出固定圆上 gauge 商满射、有符号实际成本、完整 period 或第四 ruling 已解。

## 6. 实际来源和输入绑定

### 6.1 新运行

- 仓库：Rogerhu12/math-research-public。
- lane：third_diagonal_eight_lifts。
- run：**43707570035**；job：**132791905419**。
- 科学源码提交：**282173404f65d5cc7b1dee61c66c69c3ca17866c**。
- 驱动：[literature_third_diagonal_eight_lifts.py](../scripts/literature_third_diagonal_eight_lifts.py)，26756 B，SHA256 **075b106b1fb15fbcf1b2460b501ac7309d2fdfdf249e75fdde6078deabaca1a0**。
- 设计：[third-diagonal-eight-lifts-design-20261115.md](../notes/third-diagonal-eight-lifts-design-20261115.md)。
- [公开 Actions 运行](https://github.com/Rogerhu12/math-research-public/actions/runs/43707570035)。
- [metadata-only 原回执](../notes/actions-43707570035-1-third_diagonal_eight_lifts/receipt.json)：51353 B，SHA256 **3098324f65673eacc6dc2dbbe0acc60b611824eb74f2657033d4642588ef201e**。

主报告和开发报告都完成；本文逐字节提取 stdout 的完整 COMPLETE_REPORT，分别重新计算其 UTF-8 加末尾换行的 SHA，与原回执一致。该读取只核已发表结果身份，没有新科学运算。

| 原输出 | 字节数 | SHA256 |
|---|---:|---|
| third-diagonal-eight-lifts.json | 29457 | 79f3fd82a22a3e24122e14f22c07fab89ebb7572048a22f9f5a8321ad1c5d11e |
| third-diagonal-eight-lifts-development.json | 4501 | 71f95df87275bbe96d4905943abb3d419eed8c8f46ada172690419699ab67f4d |
| 内存完整 proof | 22126 | e73f4957b68daf8f73570e70680df22c4c761de565e49b2717bb4a1bf2ba3280 |

依根 README 第 15 条，以上可重算报告、proof 没有作为数据负载写入仓库、Release 或 artifact；保留脚本、参数、run 与 SHA。proof 可由原 W 根、(6) 的准确坐标与本次脚本重建。

### 6.2 旧 W-only 原表达式

输入目录为
[actions-43645177423-1-local_fourth_quotient](../notes/actions-43645177423-1-local_fourth_quotient/receipt.json)，
run **43645177423**，source **2f1b809c0b0abb7a26303d36940edc203815f872**。

| 输入 | 字节数 | SHA256 |
|---|---:|---|
| local-fourth-quotient.json | 3982 | 19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a |
| receipt.json | 31846 | c9206d68c786613e84e4f080d2a6899b46333979e88b16f0d5306a6c88e8c0ba |
| local-fourth-quotient-W-original-expressions.json.gz | 7377 | 45cbdc8f38a4b5561924badaf9cd68a93a7fa71c6264d95489034703af4ee44a |
| 上项未压缩原文 | 31750 | 615d848611aaf787bc3ae790b4b1f81fe91338301bcb57afdfd111758cf533bf |

导出 schema 为 visible-flex-R109-local-fourth-quotient-static-v1-original-expressions，scope 是 W-only，含 36 个原根、170 个 profile atoms。旧主件的 output_limit 来自当时过长的总摘要；原 W-only 导出已完整且有真实公开终端回执绑定，不能把它误读成 W 导出失败。本次没有消费旧局部第四密度根。

### 6.3 v2 原索引与旧十八参考选择

v2 身份来自
[full-phase-bridge-exact.json](../notes/actions-43633746055-1-full_phase_bridge_exact/full-phase-bridge-exact.json)：
157380 B，SHA256
**7c2cb9fece518fb6fbb15b6b4e034565dfcc5a10cf0e103a7011cd56dc4ac960**，
run **43633746055**，
source **26c3f2c0308d179a094d3967cfb7189db426081e**。

参考选择来自
[closed-C1-endpoint.json](../notes/actions-43632772378-1-closed_c1_endpoint/closed-C1-endpoint.json)：
13911 B，SHA256
**622cd662e60eed74e58f59bb52981aed6a209eeaf4664bc7304a5e3826b6da86**，
run **43632772378**，
source **31a276f6f4b2361d10bea9a46fea307a951bb639**。
该旧报告只提供 (9) 的已发布选择及 R208 继承的上界，本次没有重做其 151 列。

## 7. 实际费用、人工开发和完整参数

### 7.1 新科学费用

| 指标 | 公开实际值 |
|---|---:|
| 总 elapsed_seconds | 0.27904966100000195 |
| Linux 峰值 RSS，MiB | 30.00390625 |
| MonitoredLimits.rational 调用数 | 6117 |
| 这些被监测调用的最大有理位数 | 10 |
| 必要恢复后 profile atoms | 258 |
| 固定参考与八目标 mapper primitive 调用 | 83 |
| 上述固定颜色 IBP 次数 | 55 |
| 上述缓存条目峰值 | 473 |
| fresh 八原差 mapper primitive 调用 | 67 |
| fresh 固定颜色 IBP 次数 | 46 |
| fresh 缓存条目峰值 | 400 |
| 两套 cycle fallback | 0 / 0 |

6117 和 10 只描述 MonitoredLimits.rational 的监测范围；不冒作全部原 DAG 算术操作总数或所有中间有理数的最大位数。总 elapsed/RSS 按原报告给出。

### 7.2 本次新人工

公开实际之前的八项新人工全部通过，elapsed 为 0.1393879250000012 秒，RSS 为 30.01953125 MiB。其范围分别是固定参考准确有理组合、依赖参考不制造假 pivot、完整 colored hook 非零而 fresh 对角零、原嵌套 primitive 双层保留、非零目标不被加作参考、原正向 I 方向、非规范 letter 拒绝、旧选择被改时拒绝。

开发报告明确 real_input_files_opened=false，没有重跑旧 151、152、P1 或响应目标。这里不把人工通过等同于 (8)；(8) 由随后的真实八目标单独支付。

### 7.3 可重建命令

在上述 source 的本仓库公开 Actions 环境，使用：

~~~text
python topics/visible-flex-new-mechanism/scripts/literature_third_diagonal_eight_lifts.py
  --w-directory topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient
  --third-directory topics/visible-flex-new-mechanism/notes/actions-43633746055-1-full_phase_bridge_exact
  --reference-directory topics/visible-flex-new-mechanism/notes/actions-43632772378-1-closed_c1_endpoint
  --max-seconds 120
  --max-memory-mib 512
  --max-nodes 300000
  --max-atoms 40000
  --max-terms 40000
  --max-word-calls 150000
  --max-cache-entries 150000
  --max-rational-bits 8192
  --max-monitored-rational-operations 1000000
  --max-proof-bytes 8000000
  --max-summary-bytes 95000
  --output @OUT@/third-diagonal-eight-lifts.json
~~~

此处换行表示参数列表，@OUT@ 为 runner 临时目录。公开开发入口另加 --toy-only，时间预算为 30 秒，输出名改为 third-diagonal-eight-lifts-development.json。所有运行均受原公开仓库环境门限制。

## 附录 A：八个新目标、提升与 fresh 原差的完整身份

以下都是已发布主报告的原 SHA256，不由本文另作原式运算。完整 $\gamma_j$、$\chi_j$ 的定义由 (6)、(7) 给出；$\Delta\chi_j$ SHA 指 fresh 转换前的真实原 DAG，不能与最后空 word 的 SHA 混同。

### 原索引 30

| 对象 | SHA256 |
|---|---|
| 完整原模板 $\tau_j$ | be8a31110800e396af0d8b2c7d240584f03cd30bcf4e1d1d8f222f2cafc8c199 |
| 原目标 $\Delta\tau_j$ | bb63796ced683896e75c76b8a08dd4a2d3e3c83dd73251a66c98a214b2f0fa95 |
| 完整提升 $\gamma_j$ | ff6b5eb5de2c4134a1d1d8f9abaa886e0d822c0a0bb51bc0a2988002c2b4d999 |
| 完整 $\chi_j$ | e934dba9b2ee51574cdf22bb0eb1efa4f151125d2a6973c934d0b3c6942cf72c |
| fresh 原差 $\Delta\chi_j$ | 626ace54b6a81a52b654e120ef2dd35bfd3980c1be7b65afe34f27a9f0ea9742 |

### 原索引 32

| 对象 | SHA256 |
|---|---|
| 完整原模板 $\tau_j$ | c8f4568fbddee3985dfd3245aff22592bb065d22dbdc958fc61433ba20279f79 |
| 原目标 $\Delta\tau_j$ | ef6d17bbdb3e463f44e4a3552e05fb2f0985b183afa2f8efe4702f60242c7916 |
| 完整提升 $\gamma_j$ | 85d617b19b2eb0f7e5c75e5d2144c8003e9283aa58dd1c90f63d83fdde86a613 |
| 完整 $\chi_j$ | d5eecb73427456b3075a0e93526ea5ffaee15baf902d6e72122a184cff14ee43 |
| fresh 原差 $\Delta\chi_j$ | 70e565248e2f67fe59748b811857899894642ce12a80f06635cfe5516863129b |

### 原索引 34

| 对象 | SHA256 |
|---|---|
| 完整原模板 $\tau_j$ | 4e76c7b917c4a00138308388d72c40def5837044d287c28242f91d635bf5f312 |
| 原目标 $\Delta\tau_j$ | 221cde625a9d04a25072b68c64a44d01549b23905786347682063d95114f1797 |
| 完整提升 $\gamma_j$ | 571d5f3ac02bf3feab995cbe1d4bba51719f84abcfd86bf1457052fee41cf849 |
| 完整 $\chi_j$ | e9711cae8ea70e3d57672acb6577e016630659235732fbb89697671d8ffdc443 |
| fresh 原差 $\Delta\chi_j$ | cc5f734b4228db4a0968d720a79c7095f23cb90184776850e9fc8d1ed72305d1 |

### 原索引 37

| 对象 | SHA256 |
|---|---|
| 完整原模板 $\tau_j$ | 94b42fb4261209e6e6e72c078b6e873dfe08dd477672afdcb0156f95051ead28 |
| 原目标 $\Delta\tau_j$ | dac93b92091f02dc96b1fc57818c98525eb4f97b2c0406a9216bbe61f831b944 |
| 完整提升 $\gamma_j$ | 10a08ed427128e7f5bed6d02d81bd5c221904de457225eea5fbd7a12558be8c8 |
| 完整 $\chi_j$ | 3e262852b4a465df76bc6a3c917fb58bd30f73102b60c3b77daebdc7850a7b8f |
| fresh 原差 $\Delta\chi_j$ | 413d54eea37feb7f1d67e685dbea0971b40afd30df24570415e4caf21e0f965a |

### 原索引 40

| 对象 | SHA256 |
|---|---|
| 完整原模板 $\tau_j$ | b5155855451e65acb83b0efd8ec51e6467fe343fa80fbeab6c04e1e523c0f368 |
| 原目标 $\Delta\tau_j$ | 1b2c7696d1e349a58ca1f72fa5fe62a83098586bc09e2bdb66a149a1440469c2 |
| 完整提升 $\gamma_j$ | c81e2b2aa662db6d8b01d8a5ef276c7f724dccd79807f3074f614f1d3eed4751 |
| 完整 $\chi_j$ | f9cbe1f2435f9aeee4acaed8e8862832c067ea2873ba355d023b0cbf8460c71a |
| fresh 原差 $\Delta\chi_j$ | 20fded28be67cae2057904f4d0d8f865b329b30547a7a2386c227c5c0846a33a |

### 原索引 100

| 对象 | SHA256 |
|---|---|
| 完整原模板 $\tau_j$ | 8aa68ac3defca7d0d88ec9b5c67dc7b30bedc569129d6fbd8705314fbe331e2d |
| 原目标 $\Delta\tau_j$ | fc69e0b642fde19629346bec5c2046a33285b03ca93cf25b103d8c9b26c9b77f |
| 完整提升 $\gamma_j$ | 6b32db600f6da3f71a2906e831e8a0435e14b9346dbf58f9a7960433368bde80 |
| 完整 $\chi_j$ | cf0662a4a39fd1076db9ba1cdf18ec8842d6399fc3852c01e6fbfea94d262a9c |
| fresh 原差 $\Delta\chi_j$ | e3270998f65bc5a5f00048eb7221949a2c697a82fd348b9dd4ef7180f3d4d792 |

### 原索引 104

| 对象 | SHA256 |
|---|---|
| 完整原模板 $\tau_j$ | 578763eecd81ff4e4bf2f3775b253c4315c6c3d58cfb2e3346524b79d8203f0d |
| 原目标 $\Delta\tau_j$ | 9c32d9cf1f51e70ebe7333bbb69f9bf7cb692a2dac979e2c678299a2d59f909a |
| 完整提升 $\gamma_j$ | 1d343bd34fc54d582c213164ff4eaec5587ea4ac7d120723189c884ff9d70f10 |
| 完整 $\chi_j$ | 22becb0a3bbe0dae7becd09f079f476fc923be3178653fc8acd0b09a2facd54d |
| fresh 原差 $\Delta\chi_j$ | 2adf8282534ce2b410cf76e379b4c50e556da235e78aab24c50bd2cd745eaa61 |

### 原索引 109

| 对象 | SHA256 |
|---|---|
| 完整原模板 $\tau_j$ | 63ec5cb74cb487c52a3e81f1f0b010352f7df57edabb1f08f42dea9093eb52ee |
| 原目标 $\Delta\tau_j$ | 61f46fe32b42aa7ebe3b40463f40c090049d3a7f599fb01e68727638d5fd3348 |
| 完整提升 $\gamma_j$ | a371b3118f0bfa7d0272e17dc9438915361ed42fd8c71ac7e2ac91f2825cad23 |
| 完整 $\chi_j$ | 6f919eb3aca85cb37f930995c088c67fed52ea44b6e0a48c1e99d1bf4c852aa6 |
| fresh 原差 $\Delta\chi_j$ | 146510f512f8c5fcbc42de4ce0524571cee44bfce3a36e957ad33383534266bc |

## 附录 B：十八个必要参考的原根与规范代表

表中的十八个位置正是主报告已观测的独立参考，不包含八个新目标。列出原 SHA 可避免把既有索引选择误认为新规范数据本身。每个规范代表都通过 R179 语法检查，颜色为 q、最高局部 jet 为 2、最大 word 长度为 1。

| 原索引 | 二次 pair | 完整原根 SHA256 | 对角原根 SHA256 |
|---|---|---|---|
| 0 | p0, p1 | abaf05b445a67ba5244461402066c36052e095095587927878a94f1e3982b7a2 | d57bcd00f544a9ff16987128a1b2f54f0faaa52a1fe8cff4b59af3c80dc29749 |
| 1 | p0, p2 | 74989d9bb1c98d42670b014315707d42bf4cd936c4b1f9251e67badda4462b13 | bf707582d52ef79edf067d143718317c0250be07660cd70f141fdbad2299c9ba |
| 2 | p0, r0 | e87d826c616a462b5e74843e10e58cb788702a1b59886bb122a87c5e3fcfb01e | 486ea200b8a45780d011cf78aad8eb6240c73c248f833ea689a33f6ee0e12a00 |
| 3 | p0, r1 | 6d0f9700615494896810e2c410b2984adf1ff9fadf0750860ec98fc982661ff6 | 8a95c8332fb736790413eb68dbff94a858e729235d8089275fd2a5efc4515424 |
| 4 | p0, s0 | 6045ad12f6fb5b180bc3fa65680e2b34a2679bd6ed6d0b5ea23cf672dba65159 | 1408ed5226fc554213b55fb56c3b63284636228ecdc3ca548f8d0524034a5c36 |
| 5 | p0, s1 | 7194e5d2ef91f17d9551148ed17f4ea05a9eba8e9d3b8ac3a075a5a012939811 | 8a079cfdf1831544cdc447500d4344c49a2665a21da895b7b89a70067d4fdf08 |
| 6 | p0, t1 | d5addb93c2cf80a60e444b2a884d18d9577158d3ef8042282993e4d56468dc39 | ea404854196acf12fa8c673a2ef1ec341b4e5578f06aa9e3180f9ebf888d6051 |
| 7 | p1, p2 | 586788dc0fcf4aec7cc329277836c89e82ddb46a5739d71dfcd154cdece83a56 | 6b048c57f9c1c4f2be4774d430c2ccbbc673ccda0f84102d1096fcd3e4f9d93f |
| 8 | p1, r0 | 589f7965592b0564e1319b28e6ba03a07de34306e980feb32c499a13d7192c2c | 902b6f7ea33e4acc8f9a8d74abd200a00e7372bf982d116a64eaf0c2487e8bb6 |
| 9 | p1, r1 | 785155ee982710fb95a14a62691adf567347c58901f77c3f7e7dc36641b3fb4e | 8ad82eb1abe0b0323fb45fd82b026ae0e293a98245b413651c519f5c4766c40b |
| 10 | p1, s0 | 406692985982a1e6610a631fbc26af111d9fd8c22bf58ef73d18b00fbb5598ff | 729378fec9a28f507732852791bbea3b8a7f963f4a2c3adcfd9ce9c33dbb10d8 |
| 11 | p1, s1 | c38ea99fe6227f06594b2a5831d976a860247ff8ac25595af4b457f8c7d62d07 | 42383d9ead8dfc2da947fa6ca2c20d17a22f8dbb9b38b0096463431d47fb7ab5 |
| 12 | p1, t1 | a36765c31af4d4583535ced0ac473d79f8c2a48081a45db7bede1002f7a15d76 | efb5d01d186a27062df1d4eb40d8863eaba952da62b043b6a4a88eccf409146d |
| 14 | p2, r1 | 99ceb97f81ba22f03776f27d4b2fc28b671022ebbfb0e32b39756b9985bd19da | 0b2e75272dd6f426b920b4ba5ef849f722615778adb4dec61b24a07301a53a83 |
| 18 | r0, r1 | 8bc8b3b9ebbaebcd5189090624c3c7a682c3fef85a611ddb6fbac4bd3ad96027 | f7b9b038d95ee4f7f6eb74d0cda0f3081dba0849ca1b9c8b9b7aa3f5d6660a9b |
| 20 | r0, s1 | 3eb1dfe8b814371fafca378393820e955c769696dc95b41603bec1bc76da0cab | 0060b7163dc1cca95eda5bcc9ab2f7a5eec95ac57250d0c0c02e00f930398a79 |
| 21 | r0, t1 | 8ce172ccbd14be41ed330362ec87966788102d59f2889aad12efe932f4d0a05f | 9ff3655c37e5c7ca6f55f9986e7948be95228588e296ae67e93502df8367b745 |
| 24 | r1, t1 | aaf991686caea0fb9f38c97530864d38193b2bd5edb4ec0d1ae6d8114920410d | c083c7b65edd51994a914a5d31a65018dcfb345bb2fe9286be18054fe138144f |

| 原索引 | 规范项数 | 规范代表 SHA256 |
|---|---|---|
| 0 | 17 | 9e4026805b2c495713a6a79ba8ff0b6cceb16fbbf6999586e9554e49ac04e935 |
| 1 | 7 | 3027c6542f36b6ab342eeab2f98d0534333ca666e275c35c2fe624aebef72c21 |
| 2 | 1 | 018ea1a28a7a29176fc18f8110d80f63be4b9b19a1963a05e6ce87c8f157d7cf |
| 3 | 6 | 5eced3caa0e1f845b2297aef5f605914c4d4dfbf9feb08bb0695abe8585808b2 |
| 4 | 6 | 37ef71abcaea088f31c1f1452a7d33839e8e2359b3524b46d328ba24d190cd98 |
| 5 | 12 | 2d165990caca41dce9a42ecbdc6f5da8bc898ef86bcabef8ab5cb2a67f215a57 |
| 6 | 12 | f2f0827ce4a2e9c842dee1bdce3be096102fa07c2e85aae17264c3afbe973064 |
| 7 | 9 | ce69939c28648e22090bf6ccf52f00d25467c6d7e1a8595c00cde8c875858690 |
| 8 | 7 | cec4f09f89d7213c94c607cbe8ff760507267964a8af901ec0767bfc1b4cd72f |
| 9 | 7 | 9d838b6eb59675a4f7611d38cc825f2a72a584b5888e130cc2c86f043a925473 |
| 10 | 4 | 558b51bc7187b1fa71acb6cb29a4d30a991121ec21f44594b46763e668ff4551 |
| 11 | 15 | cf1c83a368f7f01b31f799c183a57222b1e30fe70c0a7118e9afe5f16b9e4ee6 |
| 12 | 10 | ce13d23b0ea1d4bff66fe772ec4d1e1d31dbfc17533c67a13b01ddeab105012e |
| 14 | 10 | de8b9fec5d898c62930133b5f521a7777821e0375b27729fe795c2061fa9323d |
| 18 | 1 | 228b9cc9f78f8d22f2e6a730c035878de8917c67fa49f6f156e8013243ebf9a7 |
| 20 | 3 | 0f423c573ad61ddeb57baf86c700cbc193079aba2abd3d35cc91e86fe0c5e64d |
| 21 | 5 | a1f5aa0f3cd57524bf3c29781f02a1bfd3a2274343eed319d5bd73131deca30c |
| 24 | 8 | 1d9423aabf053d2681e2bf8fe4205cfbfc225d2a5565c09d9805b85cfb974680 |

## 附录 C：新驱动递归源码身份

下表是主报告实际记录的 16 个递归源码身份，均已与本次公开 receipt 同路径的字节数和 SHA 匹配。它是来源闭包，不表示每个旧模块的科学入口都被调用；本次只执行前述八目标及必要输入恢复。

| scripts/ 下文件 | 字节数 | SHA256 |
|---|---|---|
| literature_c7_transverse_tail_probe.py | 11020 | 98c879d83799e275e145310f5c9fdd9b85a87503d15f1690925d2f648ebc305b |
| literature_closed_c1_endpoint.py | 21532 | b0c9c5a74cdc50935f97fbe1641b705155dbec82e42750393da2a34f38357bd1 |
| literature_color_priority_words.py | 21642 | ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9 |
| literature_colored_profile_algebra.py | 15738 | c0d87a214f27a03fb29cd07cc5e9740249580da7f854ed4ff02d6eaf69b1f66f |
| literature_full_m8_tail_response_projection.py | 32096 | e66bf0d2f41570526d5e6b05aedc28118a18a492a299e097d341cc71e804e345 |
| literature_full_phase_bridge_exact.py | 35368 | d7513321bea70248851e9b71b02c97b7e869531097f290de40257c94507fed0e |
| literature_full_phase_rational_dual.py | 19492 | bcfb26b85918a8648ad98bbde7643c4cf6d01d34b35c53bc06c3dbaff31de84f |
| literature_linear_third_bridge_quotient.py | 24699 | 0627875fe06950c9e7c360baaf0429451697a460e2cf10aa6b3434c501363bd2 |
| literature_local_fourth_quotient.py | 38857 | 9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0 |
| literature_local_third_bridge_decompose.py | 30635 | 08ada4219df23e50dff2c784c2457dab3c732cd82cacc1477389fdc53fbb6ee0 |
| literature_pure_bulk_exact_membership.py | 33718 | f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70 |
| literature_pure_bulk_word_normal_form.py | 32310 | d39482c9e33e7358f1afa51b073daf5f65e84b4858f9a18f446206e8f9d9ea65 |
| literature_range_profile_algebra.py | 33169 | a7f1771a33a8e73934f9549b3407a9e351fed59a9eec163c5b11c965c7f1dc52 |
| literature_rational_volterra_polynomial.py | 19803 | 6bf16dd5c6cc8157fd53b20b58b504a5c3ea56ade9db9b62a30d385e5e69fd22 |
| literature_third_diagonal_eight_lifts.py | 26756 | 075b106b1fb15fbcf1b2460b501ac7309d2fdfdf249e75fdde6078deabaca1a0 |
| literature_total_P1_scaling_blocks.py | 37293 | 40ff170136838907ecb4d2557c2ba3b4d06b5f3fcf63746697f3d5248e92d0fa |

本次已完成的具体结果是 (6)–(8)、(11)–(14) 及由这些结果具体化的 (17)。固定圆上的完整 gauge 商、这 64 个响应的真实依赖、剩余 $V_2$ 的显式基及完整 joint 实现均保持未付，不从原始项数或有限表示维数代替它们。
