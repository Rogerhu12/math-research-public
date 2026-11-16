# R150 共同原目标系数模 B：完整 D 结构的同作业执行接口

作者：ChatGPT（AI），GPT-6 Astra Pro / literature_audit  
日期：2026-11-16  
状态：源代码已冻结，尚未执行本轮数学；下文不预填共同模的低指数或最少生成元数。

## 1. 对象与本轮范围

令 $p=31$，$D=\mathbb Z_{(31)}$，$R=D[s]=D[x]$，$x=s-2$。沿用完整原 $4367\times6188$ 多项式矩阵 $A$、泛像饱和模 $N$、$L=\operatorname{im}A$、$C=N/L$ 及其完整系数扭子 $T=C[p^\infty]$。九个原 ordinary 平方目标为 $t_j$，$j=2,\ldots,10$，并置

$$
h_*=s^3F_+^2F_-^2E_8,\qquad b_j=[h_*t_j],\qquad
B=\sum_{j=2}^{10}R b_j.
$$

已付完整同基四参数计算 run43830684123 / job133175032397 给出

$$
\operatorname{Ann}_R B=\operatorname{Ann}_R b_j=(p^5,p^2x,x^2).
$$

准确证明路径是 [完整原九目标积分 annihilator](../results/R150-appendix-original-nine-targets-complete-integral-annihilator-and-parameter-denominator-law.md)。该事实只给每个循环子模 $Rb_j$ 的 $D$ 类型 $(5,2)$；它没有给共同 $B$ 的类型或长度。本次计算独立求共同 $B$。

因为 $x^2B=0$，以下十八个真实原元素作为 $D$ 模生成 $B$：

$$
b_2,\ldots,b_{10},\quad xb_2,\ldots,xb_{10}.
$$

完整已付 $T$ 的 $D$ 指数为

$$
1,1,2,2,2,2,2,3,3,4,4,4,4,5,5,6.
$$

其 $s=1$ 系数分量有指数 $(1,2)$，$s=2$ 分量有指数

$$
1,2,2,2,2,3,3,4,4,4,4,5,5,6,
$$

后者长 $47$。在前一分量上 $x$ 为单位，所以 $x^2B=0$ 已经严格给出 $B$ 全部位于后一分量。

## 2. 四个高循环直和项的精确引理

本轮将真正计算 $p^2B$ 在完整根二系数模中的坐标，而非只读一个模 $p$ 矩阵。已付且本轮重新验证的类型是

$$
p^2B\simeq_D D/(p)\oplus D/(p^2)^2\oplus D/(p^3).
$$

因此 $B$ 中指数至少 $3$ 的因子恰为 $(3,4,4,5)$；其余因子至多为 $2$。

选择四个原 $b_i$，使其 $p^2b_i$ 生成 $p^2B/p^3B$。本轮进一步实际验证它们生成完整 $p^2B$，包括全部 $p,p^2,p^3$ 关系。记 $H=\sum_iDb_i$。

抽象分解 $B=B_{\mathrm{hi}}\oplus B_{\mathrm{lo}}$，其中前者有四个高指数，后者被 $p^2$ 杀掉。由 $p^2H=p^2B$，以及

$$
\ker(p^2:B_{\mathrm{hi}}\longrightarrow p^2B)
=B_{\mathrm{hi}}[p^2]\subset pB_{\mathrm{hi}},
$$

得到 $H\to B_{\mathrm{hi}}$ 满射。另一方面，$H$ 至多四生成，又是 $B$ 的子模，其四个有序不变因子逐项不超过 $B$ 的四个最大指数 $(3,4,4,5)$。故 $\ell_D(H)\le16$；满射给出反向不等式。因此该投影是同构，$H$ 是一个真实 $D$ 直和项，类型恰 $(3,4,4,5)$。

这不把选定的四个原 $b_i$ 当成旧十六基的某四个坐标轴。适应基与后续所有系数均从本轮的真实高关系产生。

## 3. 最小原来源重建

本轮只重建已经付过的来源依赖闭包：

| 层 | 原索引，零基 | 本轮列数 |
|---|---|---:|
| $L_3$ | $0,\ldots,7$ | 8 |
| $L_4$ | $6,\ldots,12$ | 7 |
| $L_5$ | $10,11,12$ | 3 |
| $L_6$ | $12$ | 1 |

不重做完整 $197\to204\to208\to210$ 来源。原 F2 的全部 204 行和 F3 的全部 208 行仍用于检查该选列闭包，没有删去配方外的非零依赖。

模数提升为真正的

$$
p^9=26439622160671,
$$

Taylor 原参数仍为 $x=s-2$，新精度链为

$$
35\longrightarrow30\longrightarrow25\longrightarrow20\longrightarrow15.
$$

所有 $4433$ 个原整数方程系数都从已钉 exact primitive 文件重新约化，十八个原常数比例仍为 $31$ 单位。这里没有把旧模 $p^7$ 乘积补零成模 $p^9$。

新 G/V 的全部 35 项由原 graph 真生成。程序同时重新构造其全部已付 25 项前缀，核旧完整数学字节 SHA：G 的 ef9976aca179c382c4bf265b362e56280ea725aea16e164e8d29d5759bd92202；V 的 ed02ca487853bff3a9f117b2e3c749c0cf5c9897bb4bb9d4dd53184ee0597d5a。V 中仅在第 25 项之后才出现的 entry 在比较旧前缀时按原格式删除并重记该行 entry 数；新 35 项自身不删除。

新 p9 来源头为 SJ91，乘积 checkpoint 为 SX91，完整目标乘回的 checkpoint 为 TX91。高精度来源只能来自本轮真实新父包。子程序把父 binding 的明确 64 字节重绑定到本轮 binding，逐文件核全部 SHA 并保存不变数学 payload 的 SHA；其余字节不改。

## 4. 真根二基，不把有限域投影冒充整数投影

设已付十六原除源为 $g_i=A\kappa_i/p^{e_i}$。程序只在约模 $p$ 后用实际 $P_2U_{16}$ 选择十四列，分层核秩 $1,5,14$ 和指数分布，总长 $47$。

整数来源 $\kappa_i$ 没有被偷偷投影。它们在真正根二完成分量中的像被用于全部 carry。由这十四个像的模 $p$ 独立性、各自的真实阶上界 $p^{e_i}$、以及该完整分量的已付长度 $47$，Nakayama 与长度相等给出真正的 $D$ 不变量因子基。

每次读数均保留：原 $6188$ 来源、$4367$ 输出、$104$ 局部自由条件、完整 $315$ 坐标、$505$ 原全局自由观察及同一参数作用检查。CRT8 的根一槽显式为零，输出明确标记为根二投影；没有从这件事断言一个未验证的全局原多项式来源。

因为原 $B$ 已严格位于根二分量，该分量的忠实性最终将结果送回原 $B$。不丢弃可能的低阶进位，也不把旧 $J_{16}\bmod p$ 当成高 $p$ 动作。

## 5. 高关系只需三个真实数字

先沿原完整 U7 校正及真实 q0，重算

$$
p^2b_j-AS_{1,j}=p^3r_{1,j}.
$$

该步骤采用 $20\to15$ 的真实稳定精度，并逐原 $315$ 坐标核已付首 carry SHA 4a2086fdfc64ffeb9171c3198cabb46ae04c2e013788711de44eb0f71ddab1e6。

为了使用最高阶 $e_i=6$ 的原来源，而不引入负的 $p$ 次幂，将整个等式乘 $p^3$：

$$
p^5b_j-A(p^3S_{1,j})=p^6r_{1,j}.
$$

若 $r_1\bmod p=\sum_i g_i c_{1,i}$，就加上来源 $\sum p^{6-e_i}\kappa_i c_{1,i}$，原输出除以 $p^6$ 后全 field 商为零，再求完整 q1。随后有

$$
p^5b_j-AS_{2,j}=p^7r_{2,j}.
$$

第二次同样加 $\sum p^{7-e_i}\kappa_i c_{2,i}$ 和完整 $p^7q_2$，得到 $p^8r_3$。精度链为 $15\to10\to5$。模 $p^9$ 足以支付所有三个数字。

于是 $p^2b=p^3r_1$ 的完整坐标只需读取：

- $e_i=4$ 行的 $c_{1,i}\pmod p$；
- $e_i=5$ 行的 $c_{1,i}+pc_{2,i}\pmod{p^2}$；
- $e_i=6$ 行的 $c_{1,i}+pc_{2,i}+p^2c_{3,i}\pmod{p^3}$。

其余行被 $p^3$ 消去。这是真正七行混合模数 $(p,p,p,p,p^2,p^2,p^3)$ 的坐标。

小 Smith 操作在统一 $(D/p^3)^7$ 中进行，保存两个可逆变换并核全部原乘积。四个主对角赋值必须为 $(0,1,1,2)$。完整九列对这四列的真实关系都实际验证，不能只凭四个模 $p$ 主列宣称完成。

## 6. 十五个低目标与额外的真 p h3

用上一节选定并保留的整数系数，定义五个真实余类

$$
r_j=b_j-\sum_{i\in I}a_{ij}b_i,\qquad j\notin I.
$$

它们被 $p^2$ 杀掉。再加九个真实 $xb_j$，得到十四个低目标，生成一个子模 $S$，且 $B=H+S$。

适应高基按阶 $(5,4,4,3)$ 排为 $(h_5,h_4,h'_4,h_3)$。完整 $H[p^2]$ 有四个生成元

$$
p^3h_5,\quad p^2h_4,\quad p^2h'_4,\quad ph_3.
$$

前三列从真实 $p^2H$ 坐标得到，最后一列必须独立计算；不能从 $p^2h_3$ 任意除 $p$。所以本轮低目标数是十五：五个 $r_j$、九个 $xb_j$ 和一个实际 $ph_3$。

适应基与全部 $a_{ij}$ 均使用本轮确定的同一整数 lift。改变 lift 可能改变低层，因此程序不会用另一个仅模 $p$ 相同的系数来代换这些目标。

## 7. 六数字原来源 carry

对十五个已经证明阶至多 $p^2$ 的目标 $w$，维护完整原身份

$$
p^2w-AS_k=p^{k+2}r_k.
$$

起点 $S_0=0,r_0=w$。因为 $p^2w=0$ 在模中成立，$r_k$ 的阶至多 $p^{k+2}$。所以在真实十四基中的首数字 $c_{k,i}$ 必须满足

$$
e_i>k+2\quad\Longrightarrow\quad c_{k,i}=0.
$$

程序每一层实际核此支持门，然后才使用非负来源权

$$
\sum_i p^{k+2-e_i}\kappa_i c_{k,i}.
$$

把它与完整的 $p^{k+2}q_k$ 加回来源后，原全部输出严格除以 $p^{k+3}$，给出下一 carry。五次完整求解的稳定精度为

$$
30\longrightarrow25\longrightarrow20\longrightarrow15
\longrightarrow10\longrightarrow5.
$$

得到六个真实数字 $c_0,\ldots,c_5$ 后，$p^6T=0$ 支付最后余项。因而

$$
[w]=\sum_i g_i\left(\sum_{k=0}^5p^kc_{k,i}\right)
$$

是完整的原根二模坐标。该结论依靠真阶界、逐层原乘回及忠实完成，不依靠有限域作用矩阵猜测进位。

新来源的精度足够：$e=3$ 首次可能在低第 1 层使用，要求 25 项，而父提供 30；$e=4$ 第 2 层要求 20，父提供 25；$e=5$ 第 3 层要求 15，父提供 20；$e=6$ 第 4 层要求 10，父提供 15。高链第一次使用 $e=6$ 时要求 15，父也恰提供 15。

## 8. 完整低商、共同 D 类型与最少生成元

在真实十四基中算

$$
K=H[p^2]+S\subset T[p^2].
$$

因为 $S$ 被 $p^2$ 杀掉，

$$
B/H\simeq K/H[p^2].
$$

程序必须实际验证 $H[p^2]$ 恰有类型 $(2,2,2,2)$。设

$$
\ell=\ell_D(K)-8,\qquad
n_2=\ell_D(pK+H[p^2])-8,\qquad n_1=\ell-2n_2.
$$

则 $n_1,n_2$ 正是低商中指数 $1,2$ 的完整重数，且

$$
B\simeq_D (D/p)^{n_1}\oplus(D/p^2)^{n_2}
\oplus D/p^3\oplus(D/p^4)^2\oplus D/p^5.
$$

本接口不预填 $n_1,n_2$。小群计算将各第 $i$ 行乘 $p^{6-e_i}$，把真实混合模数坐标单射到 $(D/p^6)^{14}$，然后做完整可逆 Smith 操作，逐原矩阵乘回。

此外 $xB\subset B[p^2]$，其高直和分量落在 $H[p^2]\subset pH$。因此

$$
d_D(B)=4+n_1+n_2,
$$

而 $d_R(B)$ 由 $B/(pB+xB)$ 精确决定。程序既按低商长度计算，也按下节完整表示的模 $p$ 秩独立核对。该最少生成元数不是任一单循环子模的生成数。

## 9. 一个完整 18×22 D 表示和真实 x 作用

按四个 $H[p^2]$ 及十四个 $S$ 的顺序，计算 $K$ 的十八生成元矩阵。在统一模数 $p^6$ 下写其完整 Smith 身份为 $U K V=\operatorname{diag}(p^{v_i},0)$。

模 $p^6$ 的核列取为

$$
V\operatorname{diag}(p^{6-v_i},1\text{ on zero positions}).
$$

它们的每个整数 lift 都给出真实关系，因为坐标模已被 $p^6$ 杀掉。将前四个系数分别乘 $p^{e_H-2}$，送到 $H$ 的四个适应生成元，再加四条 $p^{e_H}h_H=0$，得到十八生成元、二十二条真实关系的整数矩阵 $P$。

这里不能仅凭“模 $p^6$ Smith”就把 $P$ 宣称为完整 $D$ 呈示。程序另核 $P$ 在模 $p^6$ 下有全部十八个主元，赋值 $w_i<6$，且 $\sum_iw_i$ 等于上一节独立算得的 $\ell_D(B)$。把两边的模 $p^6$ 变换任意提升为 $D$ 矩阵；其行列式约模 $p$ 非零，所以都是 $D$ 单位。变换后前十八列为

$$
\operatorname{diag}(p^{w_i})+p^6E
=\operatorname{diag}(p^{w_i})
 \bigl(I+\operatorname{diag}(p^{6-w_i})E\bigr).
$$

右侧括号是 $D$ 单位。因此这十八列已生成指数为 $\sum_iw_i$ 的满格。其余四列是 $p^6$ 的倍数，落在该满格中，故

$$
\ell_D\operatorname{coker}P=\sum_iw_i.
$$

全部二十二列的原关系乘回又给出满射 $\operatorname{coker}P\to B$；长度相等迫使它是同构。这是从有限精度证书得到真实 $D$ 呈示的提升与等长论证，不需要另假列入 $p^6I_{18}$。逆向来源组织也完整：任何 $h+s=0$ 中，$p^2s=0$ 迫使 $h\in H[p^2]$，正是上述关系拉回的范围。

参数动作按原元素直接运输：

$$
xh_i=\sum_{k\in I}v_{ki}xb_k,\qquad
xr_j=xb_j-\sum_{i\in I}a_{ij}xb_i,\qquad x(xb_j)=0.
$$

程序核全部关系在 $x$ 下仍为关系、$x^2=0$、原十八个 $b_j,xb_j$ 张满表示，并核每个原二生成子模类型仍为已付 $(5,2)$。它同时独立计算 $d_D(B)$ 和

$$
d_R(B)=\dim_{\mathbb F_{31}}B/(pB+xB).
$$

这一步提供完整有限表示，不把仅维数相符当作来源身份。

## 10. 运行、恢复、费用与边界

采用与已成功 run43830684123 相同的三类恢复：原十四文件、六个小矩阵文件、四个真实原除源家族加 exact primitive/jet map。全部原 archive/run/member SHA、双解压 SHA 和原标签仍硬核。无需 currentK4，无需 H25 历史来源，无需恢复旧整条 3.7GB 链。

同一新 job 中按顺序执行：

1. 恢复原十四文件；
2. 恢复六个小文件；
3. 恢复四个真实家族、原整数模型与 jet map；
4. 实际 p9 / 35 项的 $8\to7\to3\to1$ 重建；
5. 同一新父基中的完整共同 $B$ 消费者。

两个数学入口每次预算 1800 秒、4096 MiB；仅退出码 75 的预算 checkpoint 可在同 binding、同 job tmp 中自动续接。独立执行尝试的预算都不超过既定边界。预估总数学墙时约 10–25 分钟，只作资源估计，不是数学完成预告。整体 workflow 上限 180 分钟，遇来源、精度、全行乘回或秩门失败立即保真实失败，不把失败记录成负数学结论。

程序直接验证并生成的对象是系数模结构和原关系。对其中已经证明为原像的目标关系，已有完整原降度定理继续给来源费用不超过 8515：这里目标都是九个 $h_*t_j$ 的常数或至多二次 $x$ 组合，目标支至多 $64+2$，其余两支仍由 8515 控制。此界是同原有限来源存在界，不声称本轮输出了一套全局来源系数或高度界。

所有大数组、来源、坐标、Smith 变换和完整数学 JSON 只留同 job 临时目录。仓库仅放源、参数、run 身份与 SHA；实际数学回执进入完成 job 日志。未执行 AST、编译或新数学；必须在实际 job 中完成语法、编译及所有门之后才能宣布结果。

## 11. 冻结文件、精确 CLI 与回执路径

完整小文本源清单、旧输入和全部 SHA 位于 [执行输入 manifest](./2026-11-16-r150-original-joint-b-complete-structure-input-manifest-789f.json)，blob `9e046d6dca0ab1f14fcf7585ed1507d3805afd50`，SHA256 `9f6de3309d76307f5ae66d262cff33848b6a94c188475e8d2dd2d1c3439a55be`。

会话参数位于 [五步 request](./2026-11-16-r150-joint-b-complete-structure-session-789f-request.json)，blob `06a018a49019e0726c05d69c8327340aeea172b0`，SHA256 `77da1143c147d36efbb06a925f25edcc4afeb4f659a35c31d1f407e56c8524d1`。根代理已将 `rulesReadAtCommit` 更新为实际已读提交 `02320c3a035d03c31c4e1fada1d19d9661bf7179`，并同步本清单与请求的精确身份；该规则身份不进入数学绑定。恢复、脚本与参数 SHA 门保持不变。

| 文件 | Blob | SHA256 |
|---|---|---|
| `topics/invariant-subspace-problem/notes/2026-11-16-r150-joint-b-complete-structure-session-789f.py` | `0735b784a417c15af97ef539bd1726199f6a2a8f` | `52774420377ce97b7aad1fa58abbfd4d5d3501cb620ec043799fefe1cc0ca4d4` |
| `.github/workflows/invariant-subspace-r150-joint-b-complete-structure-session.yml` | `e09ccf7ec156471c960a1b32f4b0a90133df7e2a` | `404a7d1301b3559d5ad441dca4eb11edb9a9a6223b96b65c210300c71052554b` |

以下占位符由同一会话脚本替换为其真实临时路径；原数组不复制到仓库。

### 4. rebuild-selected-true16-original-p9-through35

```text
python {scripts}/2026-11-16-r150-joint-b-true16-source-rebuild-p9-789f.py \
  --notes-root {scripts} \
  --original-input-dir {work}/global197-original-inputs \
  --small-input-dir {work}/root2-fourth-small-inputs \
  --true-source-dir {work}/root2-fourth-true-source-inputs \
  --exact-gzip {work}/original127-inputs/original-primitive-integer-equations.json.gz \
  --jet-map-dir {work}/root2-fourth-jet-map \
  --recipe {work}/joint-b-selected-true16/prepared210/complete210-fourth-source-recipes.json.gz \
  --out {work}/joint-b-selected-true16 \
  --seconds 1800 \
  --memory-mib 4096 \
  --through final
```

原临时回执：`{work}/joint-b-selected-true16/selected-true16-source-rebuild-receipt.json`。外层时限 1860 秒，退出 75 才按同一源、参数、binding 和临时目录续接，至多 3 次。

### 5. complete-original-joint-b-structure-p9

```text
python {scripts}/2026-11-16-r150-original-joint-b-complete-structure-p9-789f.py \
  --notes-root {scripts} \
  --original-input-dir {work}/global197-original-inputs \
  --small-input-dir {work}/root2-fourth-small-inputs \
  --true-source-dir {work}/root2-fourth-true-source-inputs \
  --exact-gzip {work}/original127-inputs/original-primitive-integer-equations.json.gz \
  --jet-map-dir {work}/root2-fourth-jet-map \
  --recipe {work}/joint-b-selected-true16/prepared210/complete210-fourth-source-recipes.json.gz \
  --parent-out {work}/joint-b-selected-true16 \
  --out {work}/complete-original-joint-b \
  --seconds 1800 \
  --memory-mib 4096 \
  --through final
```

原临时回执：`{work}/complete-original-joint-b/original-joint-b-complete-d-module-receipt.json`。外层时限 1860 秒，退出 75 才按同一源、参数、binding 和临时目录续接，至多 3 次。

完整数学呈示仅存 `{work}/complete-original-joint-b/complete-original-joint-b-presentation.json`，其原全文件 SHA 写进最终临时回执和 job 日志。仓库身份目录为 `notes/r150-joint-b-complete-structure-execution-789f/`，只保存源、参数、run 与原输出 SHA。新低重数、共同长度和最少生成元数均须等本轮实际成功后填写。
