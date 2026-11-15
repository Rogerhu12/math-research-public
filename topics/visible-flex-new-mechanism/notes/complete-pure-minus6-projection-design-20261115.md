# 完整权 −6 pure 投影：原根消费与缺失收缩的最小设计

日期：2026-11-15。执行与本文责任：tail_cost；代码与公开运行由 root 阅读、合并、调度。**本稿是新目标的数学装配和实现设计，尚无真实研究运行结论。** 本地仅运行本消费者的新人工接口检查；旧根的读取、SHA 核对及已存几何键清单不作新的研究评价。实际投影、收缩和有理消元仅在 Rogerhu12/math-research-public 的公开 Actions 执行。

新脚本：scripts/literature_complete_pure_minus6_projection.py。

建议 lane：complete_pure_minus6_projection。

## 1. 唯一目标及其对主线的作用

记 $U=\mathcal U_4$、$R=\mathcal R_8$，$\pi$ 为 canonical 第四成本的完整 universal pure 投影；同一右锚、全部 profile jets 和原函数常数均保留。程序只读取复相位 $-4$ 的原根，其与 $\pi$ 的共同常数因子不会影响像、成员性或维数。

唯一完整目标是判断

$$
\boxed{\pi(U_{-6})=\pi(R_{-6})\ ?}
\tag{1}
$$

输入与新工作都覆盖整个这个权块，不能用一个幂尾、一个新方向或不完备正规形替代 (1)。[R203](../results/R203-general-pure-lowest-two-weights-vanish.md) 已从真实一般 profile 递推消去 pure 最低两权；[R201](../results/R201-weight-zero-pure-image-and-failure-of-positive-character-readout.md) 与 [R204](../results/R204-complete-weight-minus2-pure-image-equals-nine-dimensional-response.md) 已支付完整 pure 权 $0,-2$。本次不重做这些目标。

若 (1) 成立，所有杀 $R$ 的 pure 权 $-6$ 泛函为零，故 R202 的这一 pure 正字符可能性消失。若不成立，输出真正的 pure 商基、商维数和一个准确有理 word 对偶；这只证明新商方向，不证明存在正字符。两种结论都不自动支付另一权 $-4$、mixed 成本、指定 circle 的全部 period 或 ruling。

[R206](../results/R206-full-pure-cone-equivalent-to-actual-finite-pure-controllability.md) 已把“整个 pure 闭锥满”与“实际有限 pure 成本半群满”严格连接。因此 (1) 是当前主线所需的完整新问题，非为了补齐权表而运行的分类。

## 2. 完整十四族的生成定理

[R129](../results/R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R130](../results/R130-true-fourth-span-from-horizontal-normal-coefficients.md) 和 [R163](../results/R163-complete-normal-coefficient-cocycle-and-single-weight-character-head.md) 给

$$
U=R+\operatorname{span}\{\text{全部正规状态系数值}\}.
\tag{2}
$$

其十四族为

$$
F_0,\quad Q_{2,0},Q_{2,1},Q_{2,2},\quad
\bar A_{hh},\bar A_{hk},\bar A_{kk},H_1,H_2,\quad
Q_{4,0},Q_{4,1},Q_{4,2},Q_{4,3},Q_{4,4}.
\tag{3}
$$

程序装配全部 (3) 的权 $-6$ pure 原系数，而非只取五个加速度族。使用有限 Laurent/log 状态表达式；原有限系数张成与真实开状态值张成的对应来自 (2)，不假定任意形式系数可以独立控制。

几何变量仍为 $h>0,k,\omega$，真实水平约束和微分为

$$
D_s\omega=\frac{k_s}{2h},\qquad
X=\partial_h,\qquad
Y=\partial_k+\frac1{2h}\partial_\omega.
\tag{4}
$$

正规化调用已发表的 StateField.X/Y、normalize_v2、normalize_v4_quartic，因而保留所有系数链式导数、$\log h$ 导数、面积项及第四速度项。

## 3. 负权势选择引理：为何只需这些缺失输入

### 3.1 几何缩放指数

完整旧原键顺序为

$$
(h,k,\omega,h_s,k_s,h_{ss},k_{ss},\log h,h_{sss},k_{sss}).
\tag{5}
$$

对指数键 $a$ 定义

$$
\kappa(a)=a_0-a_2+a_3+a_5+a_8.
\tag{6}
$$

正缩放 $S_H=(Hh,k,\omega/H)$ 使零 log 单项乘 $H^\kappa$，而 $\log h$ 变为 $\log h+\log H$。$\kappa$ 与 profile 真权的联系必须通过实际协变证明，不能把这个元数据标签直接当算子权。

### 3.2 完整原 $v_2,v_4$

[R190](../results/R190-complete-weight-plus2-quotient-vanishes-and-remaining-even-weights.md) §2 从保留真实 history 导数的原 RHS 得到严格协变

$$
v_j(S_H,\mathrm{jets}_H)=P_Hv_j(S,\mathrm{jets}),\qquad j=2,4.
\tag{7}
$$

不同 $H^\kappa(\log H)^r$ 的有限指数多项式独立性，逐状态单项比较，保证计算 $\Pi_{-6}v_j$ 时只需 $\kappa=-6$ 的原几何系数再作真 profile 投影。遗漏的其它指数不是被预算删除，而由 (7) 证明在本权没有贡献。原式里若存在 log 根，也继续由完整微分处理，不能以数值权标签省掉其导数。

### 3.3 $N^{[2]}$ 模 $W$ 的严格协变

R190 §3 已证明

$$
[N^{[2]}(S_H;Hu,w)]=P_H[N^{[2]}(S;u,w)]
\quad\text{模 }W.
\tag{8}
$$

因此给定第三真权 $\sigma$，$N^{[2]}$ 在模 $W$ 中可取所有 $\kappa=\sigma$、零 log 单项的 $\Pi_\sigma$ 原系数。其它指数及非零 log 次数的真实商系数为零。这是对所有真实 profile 的商身份，不是某个 word 余式或幂尾结论。

### 3.4 $N^{[0]}$ 的常势差与参考减项

静态势只有

$$
[N^{[0]}(S_H)]-P_H[N^{[0]}(S)]=C_H,
\qquad N^{[0]}(S_*)=0,\quad S_*=(1,1,1).
\tag{9}
$$

必须保留 $C_H$。设 $f_\sigma(S)=[\Pi_\sigma N^{[0]}(S)]$。将 (9) 在 $S$ 与 $S_*$ 相减，准确得到

$$
f_\sigma(S_H)-f_\sigma(S_{*,H})=H^\sigma f_\sigma(S).
\tag{10}
$$

对固定负 $\sigma\ne0$，把有限原几何表达式代入 (10)，比较 $H^\kappa(\log H)^r$。任何非恒几何单项的最高 log 系数先为零，逐 log 次数下降；然后比较 $\kappa\ne\sigma$。由不同状态 Laurent 单项的独立性，得到本次可用代表

$$
\boxed{
f_\sigma(S)=
\sum_{\substack{\kappa(a)=\sigma\\a_7=0}}
\bigl(M_a(S)-M_a(S_*)\bigr)
[\Pi_\sigma N_a^{[0]}].
}
\tag{11}
$$

这里本次用到的 $\sigma$ 是 $-3,-4,-5,-6$；潜在 $N^{[2]}$ 请求还包含 $-7$，其旧几何清单为空。没有使用 $\sigma=0$。裸 $\log h$、$\kappa=0$ 的常势例外不进入本次选择，不能将 (11) 不加说明地延伸到零权。

本次三个被 (11) 删除的 log 键准确为

$$
k^2\omega^3\log h,\qquad
k^2\omega^4\log h,\qquad
k^2\omega^5\log h.
\tag{12}
$$

它们均是非恒几何单项。因此对应投影根仅被证明模 $W$ 为零，程序不把这些原根标成字面零。所有选中的零 log 单项在 $S_*$ 都为 $1$，程序对每个 $N^{[0]}$ 项同时保留原状态项和系数 $-1$ 的常状态项。参考减项使用同一个新响应缓存，不能删除。

改变势代表只加 $W$ 值项，任何 $\mathcal B_E$ 收缩差属于 $R$。因此下述十四族代表与原族只差 $R$ 值系数；由 (2)，其加上完整 $R_{-6}$ 后仍给准确的 $U_{-6}$ pure 像。

## 4. 五份已经公开的原数据

所有输入同时绑定原 run/source、生产者 SHA、主报告、receipt 及压缩和解压字节/SHA。下列既有导出不产生新的保存例外；本次只是读取此前已公开的数据。

### 4.1 完整未降模势与原 $v_2,v_4$

目录 notes/actions-43651096112-1-local_fourth_derivative_factors。

- run：43651096112；
- source：2259b57065cfad67682f4c4319885fd5334c4f76；
- producer：literature_local_fourth_derivative_factors.py；
- producer SHA：02785c34bfe35993094cb30cc8508a9695f78116bd4423b3ab5ae4b438295abf；
- 原导出：local-fourth-derivative-factors-original-expressions.json.gz；
- gzip：2132064 bytes，9daddeaf6ad8e7aa647df4f8084ec803625c589bfc51f595ff0d9c680ce0dd4a；
- raw：11864540 bytes，58e450c47123fc682f665fffb2bb66829d9d37f502b7163e2875089b72f93fd3。

仅读其 79 个 $N^{[0]}$、93 个 $N^{[2]}$ 元数据和所需原系数；3802 个局部生成元的旧覆盖计数也检查。没有重编 producer，没有恢复旧 mixed DAG。

### 4.2 已完成的权 −2 输入投影缓存

目录 notes/actions-43665345551-1-character_head_minus2。

- run：43665345551；
- source：0aae9a6a85583a9f87415e586d8db2c9c7fea6a7；
- 原导出：character-head-minus2-original-expressions.json.gz；
- gzip：1247411 bytes，2c1242e13d253ba352c7ff1b025a91cf564ab2a7cfd93c6bcedc19baa5fac45c；
- raw：6560138 bytes，7a93a53aa7fafa1cff76608aceaeac294911ca4f828746913c1b125ae2fd33af。

旧完整计划有 1139 个请求、1057 个准确空投影、78 个非零缓存。程序沿用已经冻结的 check_cached_head 和 old_projection_index；本次只消费其中 12 个第三权 $-3$ 的已存 typed 输入根，不重新计算这 12 个投影，也不将旧权 $-2$ 响应冒充新权 $-6$ 响应。

### 4.3 已存静态密度

目录 notes/actions-43645177423-1-local_fourth_quotient。

- run：43645177423；
- source：2f1b809c0b0abb7a26303d36940edc203815f872；
- 原导出：local-fourth-quotient-original-expressions.json.gz；
- gzip：657195 bytes，ea8ba97319ef3fa43ff8cacc7f98b106b13280aef4641b969f5f820194aebace；
- raw：3518194 bytes，d74e87790a00a246e01438c54575c3190389e3adbdefed0cec233b6ec9a664d1。

读取全部 197 个 pure 静态原系数，作新的权 $-6$ 投影。旧静态势代表曾模 $W$ 归约；它与未降模代表的差属 $R$，故用于本次完整商生成正确。其小主报告是已知 output-limit fallback；绑定复用 head.bind_input 的严格 receipt 例外，而不是伪造 completion/run 字段。

### 4.4 已存五个完整正规加速度族

目录 notes/actions-43654534244-1-acceleration_layer_mixed。

- run：43654534244；
- source：1177f251dc3d9455adf88b585e4c0e4bd6f7e69b；
- 原导出：acceleration-layer-mixed-original-expressions.json.gz；
- gzip：318634 bytes，b3227509c891a2e86e9bcc7823e3d6b3abb0a9ff80975b2e1162a0911739146e；
- raw：1909429 bytes，7c1e0bda999d2c8958d7e5fdf6d9460f30eb6003eb1c69172ba1ca948dfeac38。

[R134](../results/R134-acceleration-layer-from-complete-local-v4.md) 已付 $N^{[2]}$ 收缩只进入四次速度项，所以 $\bar A,H$ 可直接复用。完整 314 记录中，权清单恰为 $[-6]$ 的 58 记录为

| 族 | 完整原记录数 |
|---|---:|
| $\bar A_{hh}$ | 16 |
| $\bar A_{hk}$ | 12 |
| $\bar A_{kk}$ | 9 |
| $H_1$ | 12 |
| $H_2$ | 9 |

只读这些记录的已存 $-4$ 根，逐根比对原 SHA；不再次编译或正规化这些族。

### 4.5 已存完整 $R_{-6}$ 原响应

目录 notes/actions-43655713308-1-g_translation_successor。

- run：43655713308；
- source：d21c87a4d9341369a3dee35598ed88fb666cb99d；
- producer：literature_G_translation_successor.py，39670 bytes；
- producer SHA：a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406；
- 主报告：G-seventh-translation.json，26745 bytes，f5e514164cede76ba91786833d455b4638a45a3ee82cd2b7cadbcd76ee18ff15；
- receipt：35234 bytes，d1a5b9d8aa03553dfcf45731cbbbbb7861fbcbb496e90fb960e723e1597c3389；
- 原导出：G-seventh-translation-original-expressions.json.gz；
- gzip：15427 bytes，936a19bd60b49b236343cdea9466f8a2bbbfbf108b3163ffe6b25e99eb66a664；
- raw：80081 bytes，cffc0109bccd0a2aeb4e6e23e400c2de94e0bde68c57b41f08df724cd37a9dcb。

[R144](../results/R144-seventh-G-translation-and-230-query-control.md) 已证明全部 $E_8\times W_{36}$ 的此权响应由以下原索引 16 列张成且完整两模式真独立：

$$
(0,1,2,3,4,5,6,7,8,9,11,12,13,15,16,17).
\tag{13}
$$

四条旧原依赖的已发 SHA 为 e91fc2506262b7b9e5b0ddb19864a123e4a037acc3a8bf0f5bae6ea6d28d4b2e。它们与旧 minor 不重跑。原导出 metadata 位于主报告 checkpoint.portable_new_block_expression_export，而非顶层；新 reader 明确处理此真实位置。

程序只恢复 (13) 的已存 pure 根，**零条旧响应重建**。完整两模式维数 16 不授 pure 维数 16；后者由本次新的 pure 共同矩阵决定。不消费同一导出中的 $G^{(7)}$ 目标。

## 5. 新运算范围的准确上界

### 5.1 势系数

由 §3 和既有键清单，所需非 log 势记录为：

| 第三权 | $N^{[0]}$ 新投影 | $N^{[2]}$ 新投影 | $N^{[2]}$ 旧投影复用 |
|---:|---:|---:|---:|
| $-6$ | 2 | 27 | 0 |
| $-5$ | 11 | 24 | 0 |
| $-4$ | 13 | 19 | 0 |
| $-3$ | 14 | 0 | 12 |
| 合计 | 40 | 70 | 12 |

因此仅 110 个新的 potential pure 对角投影；12 个输入投影直接读旧原根。三个 log 根只按已证商身份删除，程序不伪称已算原式零。

新 $v_2$ 投影有 103 个 pure 原根。原 $v_4$ 此权有 197 根，其中 37 个二次加速度根已包含于旧 $\bar A,H$ 数据；新增只 49 个 $\beta$、64 个 $C$、47 个原四次速度根，共 160 根。

### 5.2 仅用第三势的 pure 对角

设原第三模板 $T(a;b,c)$ 对内二槽对称，$\tau(q)=T(q;q,q)$。R78 完整相位公式的 pure 分量准确为

$$
\boxed{
\mathcal B_E(T)_{-4}
=\frac18\left(D\tau(q)[E(q,q)]-2E(q,\tau(q))\right).
}
\tag{14}
$$

原因是

$$
D\tau[E(q,q)]
=T(E(q,q);q,q)+2T(q;q,E(q,q)).
\tag{15}
$$

外槽不被擅自对称化。(14) 先将原根同时代入 $a=b=c=q$，再用 exact Ring.variation；该 Fréchet 导数穿过所有真实右原函数，保其同右端常数。真权投影与此对角代入交换。

这样既不调用 full_response 的 mixed 分量，也不重复三次 typed 槽替换。每个新对角先剔除字面零，再以“参数索引、对角原 SHA”合并完全相同的新请求；不同 geometry uses 和参考减项完整保留。

参数权顺序仍为

$$
(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1):
(-1,0,1,-3,-2,-2,-1,0).
\tag{16}
$$

在零/同根合并以前，$N^{[2]}$ 最多产生 $54+48+38+12=152$ 条 pure 收缩，$N^{[0]}$ 最多 $2+11+26+14=53$ 条。因此总数

$$
\boxed{\text{新 pure 收缩}\le205.}
\tag{17}
$$

该数是完整范围的上界，不是预先宣称实际非零条数。参考减项复用同一缓存，不增加新响应。任何装配时需要但缓存缺失的 token 都报接口错误；不得把未完成请求当零。

## 6. 完整装配：同一 $\Gamma$、三个势收缩都保留

原密度分层为

$$
L_2=v_2-\mathcal B_{m_0}N^{[2]}-\mathcal B_{m_2}N^{[0]},
\qquad
L_4=v_4-\mathcal B_{m_2}N^{[2]}.
\tag{18}
$$

程序消费原八矩阵 $m_0,m_2$ 的完整系数，保坐标顺序 $(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)$，不以旧“诱导 $m_2$”替代真实 $v_2,v_4$。

对同一个旧静态 $L_0$ 的本权 pure 投影，令

$$
\Gamma(E)=\sum_{i=1}^8a_i(E)L_0(S_i^*).
\tag{19}
$$

使用 R130 的同八参考态、同逆矩阵，准确执行

$$
F_0=L_0-\Gamma m_0,\qquad
Q_2=\operatorname{IBP}(L_2)-\Gamma m_2.
\tag{20}
$$

参考逆矩阵旧 metadata 是有理数字符串；新入口明确转为 Fraction 后参与矩阵乘法，避免字符串接口混用。所有八个 $F_0(S_i^*)$ 作准确原表达式零检查；$\Gamma m_2$ 完整进入三个二次速度系数，不被省掉。

完整 $Q_4$ 使用冻结的

$$
\widehat Q_4=Q_4^{raw}-\frac13D_{\mathrm{hor}}C
+\frac13D_{\mathrm{hor}}^2\beta-\mathcal B_{m_2}N^{[2]}.
\tag{21}
$$

因此所有 $H$、非完全对称的速度平方乘加速度项和最终四次速度系数均被覆盖。五个旧 $\bar A,H$ 直接并入，最终必须得到 (3) 全十四族。

## 7. 共用纯词表示、完整函数核和可读的精确输出

[R178](../results/R178-fixed-color-priority-IBP-and-terminating-shared-word-map.md) 的固定颜色优先级转换给每个新原根一个同锚 sound 身份；[R179](../results/R179-universal-independence-of-fixed-color-remainder-words.md) 证明所用 remainder-letter 字典真实单射。

本次不混用旧的不同正规形。16 个旧 pure 原响应和全部新 normal pure 原系数在同一个新 PriorityWords 映射中只转换一次，所有 surviving letters 必须通过已证余字语法检查。

先做**字面原式比例合并**：某非零原根除以其首非零有理系数，完全相同的原 terms/SHA 合并为一个 normalized original column。每个 family/state 都保存准确比例与别名。这不使用函数独立性假设。

随后依次处理 16 个旧响应、所有不同的 normalized original columns：

1. 精确整数消元只用于新共同 pure 矩阵；
2. 每条依赖保当前列非零系数和所有先前真独立原列的准确有理组合；
3. 用原列完整已转换 word 向量重新相加检查为零；
4. 同时独立形成原 DAG 差，记录其 SHA/项数；
5. 证书是逐列 R178 转换身份的有理和，不将“消元余数为零”单独当原式证明。

由 R179 单射，所得全部函数关系和秩是真实 pure 函数的关系和秩。没有“NF 非零但可能未决”的分支：若预算和所有语法检查完整通过，共同字典的秩就是函数秩；若预算/接口中断，则只记录 partial，不声称完整像。

### 7.1 成员结果

若所有 normal 列均落入旧 pure 响应像，输出：

- $\dim\pi R_{-6}$ 和 $\dim\pi U_{-6}$；
- 每个 normalized original column 对原独立响应列的完整有理坐标；
- 所有十四族原 state 别名及比例；
- 所有逐列转换、原差和 fresh word 和的准确 SHA；
- (1) 成立及该权 pure 正字符被响应 lineality 排除。

### 7.2 非成员结果

若有新方向，继续完成全部十四族，不在第一列停下。输出整个 pure 商维数、全部原独立列与所有坐标。另取首个独立 normal 列，直接在原列 pivot 小方阵上求一个有理对偶，支撑至多

$$
\dim\pi R_{-6}+1
\tag{22}
$$

个共同 word 行，并逐条验证其在 16 原响应上为零、在指定新原根上为 $1$。这为可单独阅读的具体新商证据；不把该对偶自动当正泛函、实际 signed control 或固定 profile 读出。

### 7.3 stdout 不依赖 payload 恢复

临时主摘要上限 95000 bytes。脚本自身直接输出：

- MATHEMATICAL_RESULT：完整判定、两秩、商维数、原独立列、明确非成员对偶（若有）；
- 每条 MATHEMATICAL_COLUMN：新列原 SHA、完整有理坐标、全部 family/state 别名和比例；
- OLD_RESPONSE_PURE_COORDINATES：16 原响应在实际 pure 基中的准确坐标；
- CERTIFICATE_METADATA：内存完整证明字节和 SHA；
- EXECUTION_STATUS、REPORT_METADATA：真实预算、phase、源 SHA 和摘要 SHA。

即使临时小主件需要缩短诊断表，完整数学坐标也继续逐行直接输出到公开 job 日志。不会把决定性结果只放在无法取得的临时文件里。机器证明本体只在内存构造，不写新 gzip、repo 数据、Release 或 artifact。

## 8. 最小原 DAG 解码与资源边界

新 subset_decode 只收集所选根的传递 atom 闭包。每个使用的 primitive 必须引用更早 atom，每个 jet 的颜色/阶必须合法，每个有理系数必须已约分，根 SHA 必须与旧原导出完全一致。它不注册未使用的 mixed atoms，不重置任何原函数常数。

旧输入整体 packed/raw SHA 仍先验证。因此“只解码必要闭包”不是只信一段未经绑定的裁剪数据。typed 势闭包只许 $a,b,c$；pure 输入闭包只许 $q$。共同 factor 导入可含这四个颜色，但不含 $\bar q$。最终所有新响应和 normal 列均检查 pure 四次齐次与真权 $-6$。

推荐预算：

| 项目 | 上限 |
|---|---:|
| wall time | 240 秒 |
| RSS | 1024 MiB |
| exact rational bit length | 8192 |
| 单表达式 / 新 word 字典项数 | 150000 |
| 新 IBP primitive 调用 | 600000 |
| 共用 cache entry | 300000 |
| exact nodes | 500000 |
| atom | 150000 |
| 内存完整证明 | 8000000 bytes |
| 临时主摘要 | 95000 bytes |

预算退出准确记录实际 phase 和已完成数量，不声称 (1)，也不以缺根/缺收缩为零。依根 §15 不保存可重算 cursor；若真实研究预算不足，必须先据真实停止阶段调整最小实现或预算，不能把残缺结果包装成完整证明。当前没有安排复跑任何已完成旧目标。

## 9. 新人工开发范围与版本记录

首个内部版本完成八项新人工；修正参考逆矩阵字符串入口并增加完整新矩阵流水线人工后，可审版本为：

- source：50986 bytes；
- SHA：70fc9936f014eba3484318674572d8b2c6607b0dbf57effffda7f7727c7e99ef；
- 本地新人工九项全部通过；
- development：8328 bytes，a95a4285779b37f26b7805749055439c3ddc814c11d19ddef11b30f8053efb3f；
- elapsed：0.006501459996798076 秒；
- peak RSS：21.73046875 MiB；
- 没有载入真实研究输入。

九项为：

1. 选中嵌套右原函数原 SHA 不变，同时不解码未选 mixed 分支；
2. 被使用的 forward/cyclic primitive 拒绝；
3. 外槽不对称、内槽对称的人工第三式，(14) 与完整三槽 pure 相位式准确一致；
4. 同时 pure 对角代入与真权投影交换；
5. $N^{[0]}$ 参考常数减项在 $m_2$ 收缩中完整存活；
6. 缺失新 cache token 明确拒绝；
7. 精确三列人工区分真实依赖和新商方向；
8. 新对偶在原 pivot 方阵上准确回乘；
9. 完整“16 响应 + 3 新列”人工流水线给正确纯秩、全部坐标和新商 witness。

最终微小输出修订仅保留压缩前全部数学行的直接引用，并在完整证明序列化后再检查总预算。最终源码 51380 bytes，SHA c57776cfc75ed437bf3b7f8cbcae45072b295892ecee6c93c6297519eee22c2e；已作语法解析。上述九项本地回执对应前一可审 source，不虚称对最终 source 重新运行。公开 Actions 将在最终 source 上真正执行同九项新人工，然后才执行本次真实目标；不再运行旧 40/31/70 依赖、旧 profile 评价或已完成的其它 consumer。

## 10. 完整 CLI 与五个 sparse 输入目录

开发：

    python topics/visible-flex-new-mechanism/scripts/literature_complete_pure_minus6_projection.py \
      --toy-only --output @OUT@/complete-pure-minus6-development.json

实际：

    python topics/visible-flex-new-mechanism/scripts/literature_complete_pure_minus6_projection.py \
      --factor-directory topics/visible-flex-new-mechanism/notes/actions-43651096112-1-local_fourth_derivative_factors \
      --static-directory topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient \
      --acceleration-directory topics/visible-flex-new-mechanism/notes/actions-43654534244-1-acceleration_layer_mixed \
      --cache-directory topics/visible-flex-new-mechanism/notes/actions-43665345551-1-character_head_minus2 \
      --R6-directory topics/visible-flex-new-mechanism/notes/actions-43655713308-1-g_translation_successor \
      --max-seconds 240 --memory-mib 1024 --integer-bits 8192 \
      --max-terms 150000 --max-IBP-calls 600000 --max-cache-entries 300000 \
      --max-summary-bytes 95000 --max-certificate-bytes 8000000 \
      --output @OUT@/complete-pure-minus6-result.json

五个目录已明确列在参数中，没有隐含的未发表输入。源身份递归固定 old head、旧 cache reader、R178 word mapper 及原语义 helpers。实际入口要求 GITHUB_ACTIONS=true 且 GITHUB_REPOSITORY 恰为本公开仓库；本地人工入口不加载这五份研究数据。
