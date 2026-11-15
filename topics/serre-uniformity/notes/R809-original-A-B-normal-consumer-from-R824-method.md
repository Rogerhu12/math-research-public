# R809：从真实 R824 五次关系求原 A/B normal 向量的最小消费契约

日期：2026-11-15。状态：执行契约；没有宣称新的准确 A/B 向量已经算出。

本契约接已经成功的 R809 固定 S5 块和实际完成的 R824 新五次关系。
六个已成 C0,…,C5 目标、原 S5 整数行、其真实模 minor 及固定模逆全部只读。
唯一的新准确目标是同一新关系的 A、B 两个原 L 截面，共 28 个 Q 右端。
原 R787 的保留自由列 1186 仍由原求解器继续，本消费者不重算它。

## 1. 关系与原基不改变

R824 的原准确关系读取器
scripts/R824_original_exact_relation_adapter.py
按实际 producer、完整 manifest、原配置和 17 个已成全关系检查段读出
$$
A=\sum_{i=0}^{1233}a_iF_i,\qquad
B=\sum_{i=0}^{1233}b_iF_i,\qquad A=yB,\qquad B\ne0.
$$
这里的 F_i 是原 R786 次序的 H^5 基，全部保留原 82^10 尺度。
真实性证明和 20×129>2566 的零点界见
R824-original-exact-relation-adapter-to-beta-consumers.md；
不能把 R824 的真实新来源改名为 R787 的完成关系。

最终整数 a_i、b_i 已经共同清分母并除共同整数 content。
求值和换基都不重新插入这两个已去掉的公因子。
如果它与原 R787 的某关系相差非恒定函数，这不妨碍比值仍是原 y；
本消费者始终完整绑定自己实际消费的这一对截面。

原 14 列按
$$
(B_{\mathrm{fld}}^0,\ldots,B_{\mathrm{fld}}^6,
 sB_{\mathrm{fld}}^0,\ldots,sB_{\mathrm{fld}}^6),
\quad B_{\mathrm{fld}}=\lambda b,\quad s=1+2\zeta
$$
排列。R809 normal 接口使用
$$
(b^0,\ldots,b^6,sb^0,\ldots,sb^6).
$$
因此第 k 列只乘原有的 $\lambda^{k\bmod7}$。
两块不混合，不引入 $\zeta$ 相位，不作另一个曲线模型或三同源实下降。

## 2. 已成固定块的原来源

原 R809 成功来源为：

- run 43712427063；
- source 91fbd81eb539c07f11e21116e71def91fdab5254；
- artifact 14168728276；
- core SHA256 dedb5d6149a3c3ae86ad09e51f30c1424951a09010bf48afd948d2628e1ec21d；
- full manifest SHA256 84908131c5a232d7accf5919a999c0bfbae4b2b632dcfc03c1e634494ef27b4e；
- S5 index SHA256 f6f6f0ee2bae106ef474d2cff32c743b1d8e0a886f80c26aaf8708c89ea1c119；
- 固定模逆 R809-S5-fixed-modular-inverse.json.gz，7693407 B，
  SHA256 d61b9eb35866dfca066aa5bb22042465d68b5aacf4372f75be0908e5fa9115ca。

其真实模 minor 的素数为 1000000007，行列式为 29693114。
只读该源已认证的行选择和逆，不再次求秩、求逆或重生成任何 S5 行。
完整原 normal 基的权为
$$
\epsilon=(0,1^{144},2^{127}),
$$
而 S5 次序是 a 在外、$j=0,\ldots,5-\epsilon_a$ 在内，共 1234 行。
第 (a,j) 个截面除以 $\tau^5$ 后是 $z^j\beta_a$。

新消费者必须读原成功证书、原 S5 index 的全部 1234 个 source 行、
accepted minor、其 actual rank stage、固定模逆和 source metadata。
每个旧文件保持原字节、原配置和原 SHA。新产物以明确的新 RESULT/source
登记这些外部来源；不能把旧 S5 行重新贴上新 core 的配置。

## 3. 原 V5 的真实实坐标输入

R787 已成
R787-real-power5-row-0000.json.gz 至
R787-real-power5-row-1233.json.gz
保存原 129×20 整数 t 坐标。此处只读前 69×20 项，不重新做原
$\xi^{10n}$ 相位、实子域转换或 q 级数乘积。

逐行核：

1. 原 R787 的实际 ended producer、原 core、配置和 manifest；
2. complete=true、index=i、all_original_phase_involutions_verified=true、
   averaging_used=false；
3. R786_row_sha256 与原 R786 basis_index 的第 i 行一致；
4. 原 R787、R809 与 R824 使用同一个实际原 R786 producer/index；
5. 每行完整保存 129 个 20 坐标行，截取只改变本次读取的前缀长度。

原 R787 在这里仅是已成 V5 实坐标 producer，不需要其最终关系证书。
可以从当前成功 carrier 运输这些已成旧成员，但必须逐原 manifest SHA
并同时核 parent-child 身份；不能因旧 artifact 过期而重新生成这些行。

## 4. 两个新全右端与尺度

令 $F$ 为上述原前缀构成的 1380×1234 整数矩阵，
$C$ 为原 R809 S5 的同一 1380×1234 整数矩阵。
两者都保留原 $82^{10}$ 尺度，因此无需再乘或除 82。

对于 $X=A,B$，先在原 B_fld/s 坐标中形成
$$
Y_X=F\,(x_{i,k})_{i,k}.
$$
每一列 $Y_{X,k}$ 取非负整数 content $c_{X,k}$：

- 若此列非零，primitive target 为 $Y_{X,k}/c_{X,k}$，
  其原有理尺度为 $c_{X,k}\lambda^{k\bmod7}$；
- 若此列为零，primitive target 全零，尺度为 0。

这一步的 content 只用于该个 Q 右端的求解效率，不是重新插入 R824
已共同移去的整数 content。两者必须使用不同字段名并分别保留来源。

按 k=0,…,6 和 k=7,…,13 分成两组，使用原 p=1000000007 固定逆。
每组只保存一个当前大 lift 和准确已除残差，小 name/SHA 历史另存。
每次重构使用原严格矩形界，并最终核全部 1380 个真实整数坐标：
$$
C N_{X,k}=d_{X,k}\,Y_{X,k}^{\mathrm{primitive}}.
$$
只有准确代回全部成立才输出完成坐标。模数据、部分重构或预算结束都不能
代替这一步，也不预填完成所需的 Dixon 位数。

## 5. 输出原 normal 向量

原 S5 坐标为
$$
q_{X,(a,j),k}
=\frac{N_{X,(a,j),k}}{d_{X,k}}\,
  c_{X,k}\lambda^{k\bmod7}.
$$
输出对应
$$
v_X=\sum_{a,j,k}q_{X,(a,j),k}z^j\beta_a e_k
=\frac{X}{\tau^5},
\qquad j\le5-\epsilon_a.
$$
其中 $e_k$ 是第 1 节的原 b/s 基。于是
$$
y=\frac{v_A}{v_B}
$$
作为原函数域中的恒等式成立。这里没有作 normal 环中的除法，也没有
计算 $M_A,M_B$、极理想、$\eta$ 或高度；只交付已经准确认证的两个向量。

每组输出保留 numerator、正 denominator、各列 original rational scale；
normal index 只引用这些组和原 S5 index，不重复大坐标表。
新 certificate 明确 actual_A_B_normal_vectors_computed=true，
old_C_targets_recomputed=false、old_S5_rows_or_fixed_inverse_recomputed=false。

## 6. 真实来源与后继适配

逻辑输入最小为四组：

| 组 | 必要内容 |
|---|---|
| R809 | 成功 metadata、证书、S5 index/1234 行、minor/rank/旧逆 |
| R786 | 同一原证书、basis_index 与 metadata；不再带旧 q 行 |
| R787 | 真实 ended producer metadata、原 chart 与 1234 已成实坐标行 |
| R824 | 真实完成的五次 exact relation、17 个全关系检查段、其 metadata 和必要 index |

R824 exact relation 未在一个已结束 artifact 中真实发布时，配置必须 pending。
已完成的独立关系可来自成功 scope 或明确源绑定的 ended checkpoint；
两种情形均按原 adapter 实际校验，不把运行中的文件当完成输入。

新 RESULT 与 source hash 独立于原 R809。新 normal stages 的数学配置
包含实际 R824 pair 及外部固定 S5 来源，不改变原 source bytes。
后继 R811/R825 应显式接受这个新 producer 类型，并通过外部原 S5
index 的 SHA 读取同一基映射；不能伪装原 R809 已计算 A/B。

运行恢复保持实际 pair、原 S5/index/逆和全部字段尺度不变。预算、wrapper
传输方式和新结束 run 不进入数学恒等。所有新的乘法、Dixon 和准确回代
仅在本公开仓库 Actions 执行；本地只读源码、schema 和 IO。
