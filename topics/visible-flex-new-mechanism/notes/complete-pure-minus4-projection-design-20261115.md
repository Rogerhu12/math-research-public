# 完整权 −4 pure 像：最后候选权的原根消费设计

日期：2026-11-15。数学装配与实现责任：tail_cost；root 负责全文阅读、合并、公开 Actions 和结果登记。**本文是新实际目标的设计；四项本地新增人工已通过，尚未运行真实输入。** 不把设计、旧权结论或人工检查写成新的研究结果。

新脚本：scripts/literature_complete_pure_minus4_projection.py。

建议 lane：complete_pure_minus4_projection。

## 1. 唯一完整目标

沿用 $U=\mathcal U_4$、$R=\mathcal R_8$，$\pi$ 为同一右锚的 universal pure 投影。新目标是

$$
\boxed{\pi(U_{-4})=\pi(R_{-4})\ ?}
\tag{1}
$$

下标 $-4$ 是真正的 profile 仿射缩放权。导出中 mode 为 $-4$ 则表示 canonical 复相位的 pure 系数；这两个标签来源不同，程序分别核对。原 pure mode 与 $\pi$ 的共同非零标量不影响本次秩、成员性和函数核。

[R201](../results/R201-weight-zero-pure-image-and-failure-of-positive-character-readout.md)、[R204](../results/R204-complete-weight-minus2-pure-image-equals-nine-dimensional-response.md) 和 [R207](../results/R207-complete-weight-minus6-pure-image-equals-three-dimensional-response.md) 已支付完整 pure 权 $0,-2,-6$；[R203](../results/R203-general-pure-lowest-two-weights-vanish.md) 已从一般 profile 的真实递推消去最低两权。结合 [R202](../results/R202-pure-cost-cone-and-three-remaining-negative-character-weights.md)，只剩权 $-4$ 可能承载非零 pure 正字符。因此 (1) 是当前主线所需的最后完整候选权，非重复权表扫描。

若 (1) 成立，pure 正字符的最后可能性被响应 lineality 排除，随后可将 R202 与 [R206](../results/R206-full-pure-cone-equivalent-to-actual-finite-pure-controllability.md) 的完整闭锥/真实有限 pure 支付定理连接。若 (1) 不成立，输出完整 pure 商维数、原商基及准确有理对偶；非零商本身不证明存在正字符。这两种结果均不自动支付 mixed 成本或 ruling，也不宣告原课题完成。

本次不对旧幂尾、旧响应评价、旧 forcing、旧 $W$ 或已完成的权 $-6$ 再作研究计算。所有真实新投影、收缩、正规化及精确矩阵仅在本公开仓库 Actions 运行。

## 2. 为什么完整十四族足够

[R129](../results/R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R130](../results/R130-true-fourth-span-from-horizontal-normal-coefficients.md) 与 [R163](../results/R163-complete-normal-coefficient-cocycle-and-single-weight-character-head.md) 给出真实函数空间恒等

$$
U=R+\operatorname{span}\{\text{全部正规状态系数值}\}.
\tag{2}
$$

十四族准确为

$$
F_0,\quad Q_{2,0},Q_{2,1},Q_{2,2},\quad
\bar A_{hh},\bar A_{hk},\bar A_{kk},H_1,H_2,\quad
Q_{4,0},Q_{4,1},Q_{4,2},Q_{4,3},Q_{4,4}.
\tag{3}
$$

本消费者完整装配 (3) 的权 $-4$ pure 系数。有限 Laurent/log 表达式的所有状态系数张成与真实状态值张成的对应由 (2) 支付，不把形式系数独立当作实际控制。

始终保持

$$
D_s\omega=\frac{k_s}{2h},\qquad
X=\partial_h,\qquad Y=\partial_k+\frac{1}{2h}\partial_\omega.
\tag{4}
$$

使用已发表 StateField 的完整水平微分。$\log h$ 的导数、面积项、非完全对称的速度平方乘加速度项和最终四次速度项均保留。

## 3. 负权势选择：范围、参考常数与 logarithm

完整几何键按

$$
(h,k,\omega,h_s,k_s,h_{ss},k_{ss},\log h,h_{sss},k_{sss})
\tag{5}
$$

排序。对指数键 $a$ 定义

$$
\kappa(a)=a_0-a_2+a_3+a_5+a_8.
\tag{6}
$$

这个几何指数只通过以下真协变与 profile 权联系，不能直接把 metadata 当研究结论。

### 3.1 原 $v_2,v_4$ 与 $N^{[2]}$

[R190](../results/R190-complete-weight-plus2-quotient-vanishes-and-remaining-even-weights.md) 从真实 history 导数未删的原式得到

$$
v_j(S_H,\mathrm{jets}_H)=P_Hv_j(S,\mathrm{jets}),\qquad j=2,4,
\tag{7}
$$

以及

$$
[N^{[2]}(S_H;Hu,w)]=P_H[N^{[2]}(S;u,w)]\quad\bmod W,
\qquad S_H=(Hh,k,\omega/H).
\tag{8}
$$

比较有限指数多项式 $H^\kappa(\log H)^r$，计算 $\Pi_{-4}v_j$ 只需几何指数 $\kappa=-4$ 的原根再作真正 profile 投影。对第三权 $\sigma$，(8) 允许 $N^{[2]}$ 模 $W$ 只保留 $\kappa=\sigma$ 的零 log 原系数；其它指数及 log 商系数为零。

### 3.2 $N^{[0]}$ 必须先减同一参考值

静态势只有常势差协变

$$
[N^{[0]}(S_H)]-P_H[N^{[0]}(S)]=C_H,\qquad
N^{[0]}(S_*)=0,\quad S_*=(1,1,1).
\tag{9}
$$

将其在 $S$ 与 $S_*$ 相减。对负 $\sigma\ne0$，

$$
f_\sigma(S_H)-f_\sigma(S_{*,H})=H^\sigma f_\sigma(S),
\qquad f_\sigma=[\Pi_\sigma N^{[0]}].
\tag{10}
$$

逐非恒几何 Laurent 单项比较 $H^\kappa(\log H)^r$：先由最高 log 次数下降，再比较不同 $\kappa$，得

$$
\boxed{
f_\sigma(S)=
\sum_{\substack{\kappa(a)=\sigma\\a_7=0}}
\bigl(M_a(S)-M_a(S_*)\bigr)[\Pi_\sigma N_a^{[0]}].
}
\tag{11}
$$

本次仅用 $\sigma=-1,-2,-3,-4,-5$；$N^{[0]}$ 实际只用前四个。裸 $\log h$、$\kappa=0$ 的常势例外不在此范围，不把 (11) 扩成未经证明的零权公式。

本次四个被省掉的 log 项准确为

$$
k^2\omega\log h,\quad k^2\omega^2\log h,\quad
k^2\omega^3\log h,\quad k^2\omega^4\log h.
\tag{12}
$$

其根标签为 N0_48、N0_50、N0_52、N0_54。它们是非恒几何项，所选投影模 $W$ 为零；程序不声称这些原 DAG 字面为零。所有选中零 log 单项在 $S_*$ 的值均为 $1$，每个 $N^{[0]}$ 条目都同时加入原状态项与系数 $-1$ 的常状态项，收缩时使用同一缓存，不删除参考减项。

势代表改变只加 $W$ 值项，$\mathcal B_E$ 的差落入 $R$；因此十四族的这些代表加上完整 $R_{-4}$ 后，仍准确给出 (2) 的权 $-4$ pure 像。

## 4. 五份已有公开输入及严格绑定

输入均核原 run/source、生产者、main、receipt、packed/raw 字节与 SHA、原根 SHA 和覆盖语义。这里只读取旧数据；新输出仍受根 README §15 的 metadata-only 规则。

### 4.1 未降模势及原局部生成元

目录：notes/actions-43651096112-1-local_fourth_derivative_factors。

- run：43651096112；source：2259b57065cfad67682f4c4319885fd5334c4f76。
- producer：literature_local_fourth_derivative_factors.py，SHA 02785c34bfe35993094cb30cc8508a9695f78116bd4423b3ab5ae4b438295abf。
- 文件：local-fourth-derivative-factors-original-expressions.json.gz。
- packed：2132064 bytes，9daddeaf6ad8e7aa647df4f8084ec803625c589bfc51f595ff0d9c680ce0dd4a。
- raw：11864540 bytes，58e450c47123fc682f665fffb2bb66829d9d37f502b7163e2875089b72f93fd3。

覆盖 79 个 $N^{[0]}$、93 个 $N^{[2]}$ 原记录；局部生成元总数 3802，两个 mode 各有 $v_2$ 665、$v_4$ 1236。只解码所需 pure/typed 根的原 atom 闭包，不重编这个 producer。

### 4.2 已存输入投影缓存

目录：notes/actions-43665345551-1-character_head_minus2。

- run：43665345551；source：0aae9a6a85583a9f87415e586d8db2c9c7fea6a7。
- main：15967 bytes，55320985df05f928caf007016777ecb2413f16c969dca4741b0c2e936f00b940。
- receipt：39451 bytes，88bdcf2dadbba25d816e886705b70e7844f698f07917b696698e86ea2770f675。
- 文件：character-head-minus2-original-expressions.json.gz。
- packed：1247411 bytes，2c1242e13d253ba352c7ff1b025a91cf564ab2a7cfd93c6bcedc19baa5fac45c。
- raw：6560138 bytes，7a93a53aa7fafa1cff76608aceaeac294911ca4f828746913c1b125ae2fd33af。

原完整计划的 1139 个请求、1057 个准确空投影、78 个非零缓存由冻结 check_cached_head 与原来源绑定验证。本次只使用 §5 所列的 44 个已完成请求；不重旧权 $-2$ 研究目标。

### 4.3 完整静态原密度

目录：notes/actions-43645177423-1-local_fourth_quotient。

- run：43645177423；source：2f1b809c0b0abb7a26303d36940edc203815f872。
- 文件：local-fourth-quotient-original-expressions.json.gz。
- packed：657195 bytes，ea8ba97319ef3fa43ff8cacc7f98b106b13280aef4641b969f5f820194aebace。
- raw：3518194 bytes，d74e87790a00a246e01438c54575c3190389e3adbdefed0cec233b6ec9a664d1。

全部 197 个 pure 静态原根作**新的权 $-4$ 投影**，这 197 项属于本次新工作，不能漏记。旧静态势曾模 $W$ 归约，代表差只改 $R$ 项；完整像范围不变。原小 main 的 output-limit fallback 走既有严格 receipt 例外，不补造缺失字段。

### 4.4 已存五族完整正规原根

目录：notes/actions-43654534244-1-acceleration_layer_mixed。

- run：43654534244；source：1177f251dc3d9455adf88b585e4c0e4bd6f7e69b。
- 文件：acceleration-layer-mixed-original-expressions.json.gz。
- packed：318634 bytes，b3227509c891a2e86e9bcc7823e3d6b3abb0a9ff80975b2e1162a0911739146e。
- raw：1909429 bytes，7c1e0bda999d2c8958d7e5fdf6d9460f30eb6003eb1c69172ba1ca948dfeac38。

[R134](../results/R134-acceleration-layer-from-complete-local-v4.md) 给出 $N^{[2]}m_2$ 只影响四次速度项。本次直接消费旧五族中 profile_weights 恰为 [-4] 的 **29** 条记录：

| 族 | 原记录数 |
|---|---:|
| $\bar A_{hh}$ | 9 |
| $\bar A_{hk}$ | 6 |
| $\bar A_{kk}$ | 4 |
| $H_1$ | 6 |
| $H_2$ | 4 |

逐根核旧 mode $-4$ 原 SHA，不重 A/H 正规化，不把其它 profile 权纳入。

### 4.5 已存完整 $R_{-4}$ 响应基

目录：notes/actions-43654534244-1-g_translation_successor。

- run：43654534244；source：1177f251dc3d9455adf88b585e4c0e4bd6f7e69b。
- producer：literature_G_translation_successor.py，39670 bytes，a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406。
- main：G-fifth-translation.json，24966 bytes，faf6c2a0019ce614bb8d6f28b049f0a38a6c2f6e2e00930a1beab17e6c86f93e。
- receipt：34625 bytes，e8f37f37ba85f822e6eacc17167fb6941017dc05ec7670b8fafa7b450dc4d24d。
- 文件：G-fifth-translation-original-expressions.json.gz。
- packed：76352 bytes，b266eebf27d001ef90fcc94f8b49b9f9984ed5d3f7a047d9b5cef5ddffd2423b。
- raw：427950 bytes，6e19e56d879eed7f7d741957526679521f65f06b92c42b4cb29f39fb2c2276e4。

[R139](../results/R139-fifth-G-translation-separation-and-188-query-control.md) 的完整两 mode 原块为 50 列，真维数 40；十条已证原依赖 SHA 为 866e724012d102537c7ff1da010c5deb5d94d1ab19cffb601552248043f8f0ab。保留的原下标按下列顺序：

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,
    21,22,23,24,26,27,28,29,30,32,34,35,36,37,41,42,43,44,45,49

只解码这 40 个已存 pure 原根；不重建响应，不重十条原依赖、旧 minor、旧 G 第五平移目标或旧 profile 评价。**40 是完整两 mode 响应维数，不是假定的 pure 秩。** 本次共同 pure 矩阵自己准确确定其 pure 秩。这也不是先前权 $-2$ 的另一组 40 列。

## 5. 已存、必要恢复和真正新工作的边界

### 5.1 114 个势投影请求

零 log 选择清单为：

| 原势 | 第三权 | 原记录数 |
|---|---:|---:|
| $N^{[0]}$ | −4 | 13 |
| $N^{[0]}$ | −3 | 14 |
| $N^{[0]}$ | −2 | 12 |
| $N^{[0]}$ | −1 | 10 |
| $N^{[2]}$ | −5 | 24 |
| $N^{[2]}$ | −4 | 19 |
| $N^{[2]}$ | −3 | 12 |
| $N^{[2]}$ | −2 | 7 |
| $N^{[2]}$ | −1 | 3 |

共 49 个静态、65 个导数势请求，合计 114。四个 log 项另由 (11) 处理。

其中旧缓存覆盖 $N^{[0]}$ 权 $-1,-2$ 和 $N^{[2]}$ 权 $-1,-2,-3$：合计 **44** 个原请求，**35** 个非空 typed 缓存直接消费，**9** 个已证空投影直接使用。

九个旧空请求：

    N0_39@-1, N0_40@-2, N0_58@-1, N0_59@-2, N0_63@-1,
    N0_64@-2, N0_67@-1, N0_68@-2, N0_70@-1

只有在上述已完成 1139 请求的明确子集内，非零缓存中不存在某根才代表旧准确空投影；未请求或预算失败的项不能据此当零。新代码以 archived_request 显式限定两个导数层的不同权集合，再核同一原根 SHA、状态键和 derivative_weight。

余下 **70** 个输入为 $N^{[0]}$ 权 $-4,-3$ 的 27 个，以及 $N^{[2]}$ 权 $-5,-4$ 的 43 个。这些纯对角投影曾作为 R207 的临时中间输入存在；根 §15 禁止保存可重算 payload，故没有可读的已存输出。本次必须从同一旧原根恢复这些依赖。它们不是新发现，也不是重跑权 $-6$ 目标：只恢复必要对角输入，完全不调用 R207 的收缩、十四族、矩阵或旧研究入口。

typed 第三式的三个槽同时代入 $q$；不假定外槽对称。已存 typed 投影不再投影一次，新的必要恢复先取 pure 对角再作所需真权投影。每个输出保存原根/已存投影/纯对角 SHA 对应。

### 5.2 新局部原投影

本次新的原 $v_2$ pure 权 $-4$ 投影为 **62** 个。$v_4$ 在该权的原记录共有 97 个，其中三个已存 A 族贡献 19 个，不重编；新 $\beta,C,Q$ 原投影为 **78** 个。29 个已存 A/H 正规根直接使用。另有 §4.3 的 **197** 个新静态投影。

这些计数只表示完整输入/装配范围，不是真函数维数。所有新输出继续保完整 profile jets；[R208](../results/R208-every-universal-pure-response-has-a-second-jet-representative.md) 的二阶 jet 代表定理不用作删项规则。

### 5.3 新 pure 收缩上界 164

使用八个原二次算子的准确权及原 $m_0,m_2$ 支撑。本次可能的 $N^{[2]}$ 收缩为：

| 第三权 | 二次参数 | 上界 |
|---:|---|---:|
| −5 | $p_2$ | 24 |
| −4 | $p_1,t_1$ | 38 |
| −3 | $p_0,s_1$ | 24 |
| −2 | $r_1,s_0$ | 14 |
| −1 | $r_0$ | 3 |

共 103。$N^{[0]}m_2$ 的相应上界为：

| 第三权 | 二次参数 | 上界 |
|---:|---|---:|
| −4 | $t_1$ | 13 |
| −3 | $s_1$ | 14 |
| −2 | $r_1,s_0$ | 24 |
| −1 | $r_0$ | 10 |

共 61，合计 **164**。这是去零和原 SHA 合并前上界；实际计划按 (quadratic_index, pure_input_sha256) 去重，不把相同原对角响应重算。引用同一响应的状态项、参考减项和不同局部层全部共享缓存。

这些收缩输出权均为 $-4$，与 R207 的权 $-6$ 输出不同；旧输入恢复与真正新响应两类数量在摘要中分别报告。

## 6. pure 响应及十四族完整装配

设 $\tau(a,b,c)$ 为外槽与内槽类型保留的原第三式，$\tau_\Delta(q)=\tau(q,q,q)$；$E$ 为原二次对称算子。由完整相位式直接对角化，

$$
(\mathcal B_E\tau)_{-4}
=\frac18\left(D\tau_\Delta(q)[E(q,q)]-2E(q,\tau_\Delta(q))\right).
\tag{13}
$$

导数 $D\tau_\Delta$ 同时包含三个槽，不把 $\tau$ 当作完全对称三线性式。冻结的 diagonal_response 已由先前新人工对完整相位原式验证，本次只复用函数，不重跑其旧目标。

准确局部原式为

$$
L_2=v_2-\mathcal B_{m_0}N^{[2]}-\mathcal B_{m_2}N^{[0]},
\qquad
L_4=v_4-\mathcal B_{m_2}N^{[2]}.
\tag{14}
$$

八矩坐标保持 $(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)$。不以诱导 $m_2$ 项替代完整 $v_2,v_4$。

取同一静态原 $L_0$ 的本权 pure 投影，使用 R130 的同八参考态和同逆矩阵：

$$
\Gamma(E)=\sum_{i=1}^8a_i(E)L_0(S_i^*),\qquad
F_0=L_0-\Gamma m_0,\qquad
Q_2=\operatorname{IBP}(L_2)-\Gamma m_2.
\tag{15}
$$

原逆矩阵字符串先转为 Fraction。八个 $F_0(S_i^*)$ 均作准确原表达式零检查，$\Gamma m_2$ 完整进入三个二次速度系数。

四次速度项使用冻结的准确算式

$$
\widehat Q_4=Q_4^{raw}-\frac13D_{\rm hor}C
+\frac13D_{\rm hor}^2\beta-\mathcal B_{m_2}N^{[2]}.
\tag{16}
$$

与旧五族 A/H 合并后必须恰为 (3) 全十四族。缺失收缩 token 明确失败，不能默认为零。

## 7. 一次完整新 pure 矩阵和原式关系证明

先按原 terms 做字面比例合并：每个非零原根除以首个非零有理系数，相同 terms/SHA 合并；每条 family/state 保准确比例与别名。此时不作任何函数独立性判断。

随后按顺序处理 40 个旧 pure 响应和所有不同的新 normalized original columns。每列只通过一次同锚固定颜色 PriorityWords 转换。按 [R178](../results/R178-fixed-color-priority-IBP-and-terminating-shared-word-map.md)，转换是 sound 原式身份；每个 surviving letter 检查余字语法。[R179](../results/R179-universal-independence-of-fixed-color-remainder-words.md) 的真实单射性使完整共同字典的秩恰为函数秩。

每条依赖都保：

1. 当前原列的非零系数及先前真独立原列的准确有理组合；
2. 对完整原列已转换 word 向量重新相加得到准确零；
3. 独立形成原 DAG 差的 SHA 与项数；
4. 所有被使用列的原 SHA、转换后 SHA 和余字语法身份。

因此证明是逐列原转换身份的有理和，不能只凭消元余式标签。无需对同一个原差再次运行另一个 NF；程序明确标记 fresh_original_difference_normalization_repeated=false。

### 7.1 全成员分支

输出两真秩、商维数零、全部原独立响应列、所有新列的准确有理坐标及完整 family/state 别名。所证明的是 (1)，不只是某些新方向通过。

### 7.2 非成员分支

首个新方向出现后仍完成全部十四族和矩阵，不提前结束。输出全商基与所有坐标；另在原 pivot 小方阵上求准确有理对偶，其 word 行支撑至多

$$
\dim\pi(R_{-4})+1.
\tag{17}
$$

在全部 40 个旧原响应上逐一验值为零、在指定新原列上为 $1$。这是纯函数商证据；不声称它对其它权、真实成本锥或指定 profile 有任何额外性质，也不把非零商当作正字符。

## 8. 源复用、人工检查和输出边界

本文件导入冻结的 literature_complete_pure_minus6_projection.py，仅使用通用绑定/子集解码/pure 对角响应/整数消元函数，以及其明确列出的原 helper。该文件为 51380 bytes，SHA c57776cfc75ed437bf3b7f8cbcae45072b295892ecee6c93c6297519eee22c2e。新 source_identity 先核此身份，再递归保原所有依赖绑定，新增本 driver；未修改旧模块全局常量，不调用其 actual 或 toy_only。

本次源：43687 bytes，SHA be5d2ffa861968dddd9db085cfef0ecc06d9c96a6f1ca719905e8544458bc946。

本地人工报告：8057 bytes，SHA cdba44606748956d481e4e56b5fcb4e3384dfaf67fce8823fe7a28b76bb19864；0.004691271999035962 秒，21.234375 MiB。当前同一 source 的四项新人工全部通过：

1. 权 $-3$ 时 $N^{[0]}$ 与 $N^{[2]}$ 的旧缓存请求范围准确不同；
2. 可变完整响应块大小的全矩阵正确给商方向、准确坐标与对偶；
3. 新目标全成员分支无伪商方向；
4. 新权 $-4$ 下 $N^{[0]}m_2$ 同时保原状态与固定参考减项。

没有读取研究输入，没有重旧 $-6$ 九人工，也没有新 profile 采样。公开 Actions 先在最终 source 真正执行这四项，再运行实际目标。

### 8.1 子集原根解码

整体旧 packed/raw 身份先核，再只注册所选根的传递 atom 闭包；每个 primitive 必须引用更早 atom，颜色/jet 阶合法、Fraction 已约分、选中原根 SHA 全相同。typed 势允许 $a,b,c$，pure 根仅许 $q$；不注册未选 mixed 分支。最终新响应和正规列必须四次 pure 齐次、真权 $-4$。

### 8.2 可读结果与根 §15

脚本直接 stdout：

- MATHEMATICAL_RESULT：完整结论、两秩、商维数、独立原列及非成员对偶；
- 每条 MATHEMATICAL_COLUMN：原 SHA、完整有理坐标、所有 family/state/比例别名；
- OLD_RESPONSE_PURE_COORDINATES：40 原响应的准确 pure 坐标；
- CERTIFICATE_METADATA：内存完整证明字节/SHA；
- EXECUTION_STATUS、REPORT_METADATA：真实阶段、数量、预算、source/summary SHA。

临时主摘要压缩前保留上述完整数学行的直接引用，即使主件超过 95KB 需要缩小，全部坐标仍直接写公开日志。不会把数学结论只留在无法取得的 runner 临时文件里。

完整可重算证明仅在内存构造，**不写新数据 gzip，不上传 repo/Release/artifact，不保存可重算 cursor**。临时 output 只供根已修改的 metadata-only publisher 取大小/SHA；正式发表结果由数学正文、源、参数、run/source 和 SHA 组成。

## 9. 预算与非完成边界

| 项目 | 上限 |
|---|---:|
| wall time | 240 秒 |
| RSS | 1024 MiB |
| rational bit length | 8192 |
| 单表达式 / 新 word 字典项数 | 150000 |
| IBP primitive 调用 | 600000 |
| 共用 cache entries | 300000 |
| exact nodes / atoms | 500000 / 150000 |
| 内存完整证明 | 8000000 bytes |
| 临时主摘要 | 95000 bytes |

资源或接口中断只报告真实 phase、已完成数量和失败原因，不声称完整像、不把缺根或缺收缩当零。若预算确实不足，后继依实际停止阶段设计必要调整；本设计没有安排重复任何已成旧目标或保存被规则禁止的 payload。

## 10. CLI 与五个 sparse 目录

开发：

    python topics/visible-flex-new-mechanism/scripts/literature_complete_pure_minus4_projection.py \
      --toy-only --output @OUT@/complete-pure-minus4-development.json

实际：

    python topics/visible-flex-new-mechanism/scripts/literature_complete_pure_minus4_projection.py \
      --factor-directory topics/visible-flex-new-mechanism/notes/actions-43651096112-1-local_fourth_derivative_factors \
      --static-directory topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient \
      --acceleration-directory topics/visible-flex-new-mechanism/notes/actions-43654534244-1-acceleration_layer_mixed \
      --cache-directory topics/visible-flex-new-mechanism/notes/actions-43665345551-1-character_head_minus2 \
      --R4-directory topics/visible-flex-new-mechanism/notes/actions-43654534244-1-g_translation_successor \
      --max-seconds 240 --memory-mib 1024 --integer-bits 8192 \
      --max-terms 150000 --max-IBP-calls 600000 --max-cache-entries 300000 \
      --max-summary-bytes 95000 --max-certificate-bytes 8000000 \
      --output @OUT@/complete-pure-minus4-result.json

这是 28 个实际参数。实际入口要求 GITHUB_ACTIONS=true 且 GITHUB_REPOSITORY 恰为 Rogerhu12/math-research-public。五旧目录和全部脚本由 root 统一接入 sparse/workflow；本地只使用不载真实输入的人工入口。
