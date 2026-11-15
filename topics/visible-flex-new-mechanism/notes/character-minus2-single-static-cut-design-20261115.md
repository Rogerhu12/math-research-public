# R166 后继：只追加静态 $k=1/2$ 一行的准确必要系统消费者

日期：2026-11-15。**实现与新增人工接口已完成；真实续算尚未运行。** 实际研究只在 Rogerhu12/math-research-public 公开 Actions 中执行。

独占新源：scripts/literature_character_minus2_static_cut.py。原 scripts/literature_character_minus2_finite_necessary.py 保持冻结，不修改，不调用它的真实主入口。

## 1. 唯一新目标

R166 从已发表外部候选直接读出

$$
a(k)=-k^2+k^4+k^6,\qquad a(1/2)=-11/64.
$$

原有限系统的静态状态为 $k=-2,-1,0,1,2$，均未切掉该点。新任务只追加已经由真实长常段证明的一个必要半空间：

$$
a(1/2)\ge0.
\tag{1}
$$

不增加原参数网，不增加路径，不消费新的原函数或不同权。tail 的 R165 频率门在这个候选上是 $t^2+5t+2\ge0$，不能切它；本轮不加入该门。

然后在同一准确外部系统上重新寻找全部自由坐标的双符号 Farkas 证书，或保存一个新的准确外部点。旧点被排除不表示整个外锥为零；外锥非零也不表示真实正字符存在。

## 2. 输入与来源固定

唯一实际输入是公开 run 43665971895 的三件输出，源码 commit 为

~~~text
05bb659b59997906316ddd2873aedbf4840f62a5
~~~

目录：

~~~text
topics/visible-flex-new-mechanism/notes/actions-43665971895-1-character_minus2_finite_necessary
~~~

| 输入 | 字节 | SHA256 |
|---|---:|---|
| character-minus2-finite-necessary.json | 10143 | 1e8d751fca7fb6d8b2c33d1152e8651399824be22ffad5496c8bdb48de7fef6c |
| receipt.json | 40026 | 6fbdf4f3c98bfa14fe6344d988a5df9acad10b4c7e598711aa3f5b57c8515764 |
| character-minus2-finite-necessary-certificate.json.gz | 31976 | 5658e056313fff939356f91c97578a8dfc3e1158661b209c84ba7d2b86aa3634 |

完整证书 raw 为 143028 字节，SHA256：

~~~text
dd539b088c354d99c04af46d8d7c63822679f13ebc02b14a673c76767fd745f7
~~~

复用准确算术/LP 支持提出器的冻结源码为：

~~~text
literature_character_minus2_finite_necessary.py
45116 bytes
d4c3751cf58f1ef08c534e61a16d7a40cd368980c0cca0ef48a0bce505ce3545
~~~

新消费者把这些身份全部固定在 PREVIOUS 中。CLI 只给实际文件位置，不能用另一轮未声明的候选替换它们。校验包括：

- 主报告 schema、complete、公开仓库、run、source、原 driver；
- receipt 的 repo/lane/run/source，source_files 中原 driver 的真实字节身份；
- 主报告输出身份和证书 packed/raw 四项身份；
- 完整证书 schema、source_hashes、原 head 输入链、权 −2 与完整嵌入声明；
- 107 正规坐标的编号、旧 124 条等式/63 条不等式/23 自由坐标的已发表计数；
- 保存的 $x=B y$ 中每个自由原坐标确实仍是对应 $y_j$。

输入中已有完整 head 链。新任务不读 6.56 MB head 原导出，不 import head 或 profile helper，不重复其 78 条收缩。

## 3. 原数据的继承，不重新构造

新消费者原样读取旧证书的：

- normal 坐标语义与自由编号；
- 124 条等式的已存 RREF；
- 原 $x=B y$；
- 63 条约化必要半空间；
- 已存 F0 正规 $k$ 多项式的线性系数行；
- 原候选 $y^*$。

原 124 条等式不重新消元，原 63 条半空间不重新生成或归一化，原六条路径积分不重新计算。源码只是从其已存原行恢复 RowTable 的读取接口；旧每条 record 的顺序、coefficients 与元数据均保持。

设证书存有

$$
a(k)=\sum_{\ell} A_\ell(x)k^\ell.
$$

唯一新原坐标行是

$$
L(x)=\sum_\ell 2^{-\ell}A_\ell(x),
\tag{2}
$$

唯一新约化行是 $L(B y)$。新行可乘正的公分母/gcd 归一化，不能翻符号。消费者检查它在原已证有理候选上严格为负，并保存这个准确值；若不严格切该点、若行为零或已有相同约化行，则拒绝宣称这是本次有目标续算。

旧行的完整 canonical SHA 在读取前后保持。新证书还保存旧等式、RREF、坐标变换、原/约化不等式、六条路径积分的 canonical SHA；这些只是对已存数据的身份绑定，不是重新求解或评价它们。

## 4. 严格判定逻辑

设同一自由坐标数为 $d$，更新后的必要行是 $A_i y\ge0$。调用冻结的精确支持核验器：

1. 浮点 HiGHS 只提出表示 $\pm e_j$ 的非负支持；
2. 在有理数上求该支持的准确系数；
3. 对原约化行核准确等式及全部非负性；
4. 仅当每个 $j$ 的两个符号均完成，才输出 positive_character_excluded=true。

因此排除的是**非零真实权 −2 正字符**，不指任意符号泛函，不指其他权。原全生成坐标仍被覆盖，没有退化为只测试 $\lambda J=1$。

若任一步没有取得准确双证，程序可以保存逐有理不等式核验的非零外部点。该点只是这个必要系统的点；即便它通过本轮 (1)，也不授完整静态、完整路径或真实原函数依赖。

本任务不把浮点不可行状态当证明，不把一个浮点极小值近零设零，不把候选坐标称为真实正泛函。沿用原有精确支持核验并不重复旧数学目标：新的 LP 的锥已多出 (1)，求的是这一新系统的必要结论。

## 5. 输出

主 schema：

~~~text
visible-flex-character-minus2-single-static-cut-v1
~~~

输出：

~~~text
character-minus2-static-cut.json
character-minus2-static-cut-certificate.json.gz
~~~

新完整证书包含：

- 原主报告/receipt/完整证书的不可变身份；
- 旧坐标与 RREF 的来源/摘要；
- (2) 在原坐标与自由坐标中的完整 Fraction 行；
- 原候选的准确新行值；
- 仍与旧顺序一致的全部更新约化行；
- 每个完成的双符号非负有理组合；
- 若有，新的准确外部候选；
- all_true_positive_characters_embed_in_this_outer_system=true；
- 明确原证书是解释旧 normal 语义的必要组成。

不重复输出旧原函数 DAG 或 profile 原语。完整证书无法保存时，小回执不得继续声称数学排除成立。

## 6. 新人工与预算

新增接口共八项人工检查，全部只用两个虚构坐标和小有理矩阵：

1. 从已存虚构 F0 行只构造一个新静态行；
2. 旧 rows/metadata/整个输入字节语义不被修改；
3. 小例中一条新增行后全坐标双符号准确证书成立；
4. 将旧 rref、construct_system、path_integrals 入口全部替换为拒绝哨兵，续接仍成功，证明没有调用这些入口；
5. 另一人工例只切旧点但仍有非零外锥，不误报整锥为零；
6. 原自由坐标语义被改时拒绝；
7. 新行不切原目标点时拒绝；
8. publication 的旧完整 raw SHA 被改时拒绝。

这不是旧十三项开发或旧实际的重跑。开发中只纠正了一次拒绝哨兵的旧函数名称，最终八项通过；没有任何真实候选文件进入人工入口。

缺省预算保持 240 秒、轮询 RSS 1024 MiB、有理位长 16384 bits。小主报告 <95000 字节，新完整证书 gzip ≤4500000 字节，总新输出 ≤4.8 MB。预算不因前轮未排除而增大。

CLI：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_character_minus2_static_cut.py \
  --toy-only --output WORK/character-minus2-static-cut-development.json

python topics/visible-flex-new-mechanism/scripts/literature_character_minus2_static_cut.py \
  --source-report OLD/character-minus2-finite-necessary.json \
  --source-publication OLD/receipt.json \
  --source-certificate OLD/character-minus2-finite-necessary-certificate.json.gz \
  --output WORK/character-minus2-static-cut.json
~~~

OLD 必须是第 2 节原目录。实际入口强制 GITHUB_ACTIONS=true 且 GITHUB_REPOSITORY=Rogerhu12/math-research-public；本地只执行 --toy-only。

