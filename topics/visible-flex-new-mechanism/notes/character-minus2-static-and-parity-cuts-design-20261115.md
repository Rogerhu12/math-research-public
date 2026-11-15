# 权 −2：同一旧有限系统的一条静态行与完整 Q2 反射奇偶续接

日期：2026-11-15。**新源和八项专用人工已完成；真实续算尚未执行。** 数学前提 R168 的完整真实反射证明已发表在 results；本次公开实际直接使用它的修正二次奇偶等式。本文不从先前外部候选的符号推断真实奇偶。

新源：scripts/literature_character_minus2_static_and_parity_cuts.py。
它复用冻结的 scripts/literature_character_minus2_static_cut.py 读取与准确行接口，后者复用 scripts/literature_character_minus2_finite_necessary.py 的准确 Farkas 支持核验器。没有先运行 static-cut 中间实际；本次直接从原 run 43665971895 接入全部已证明的新条件。

## 1. 为什么联合这两个有目标增量

R166 已证原候选的 $a(k)=-k^2+k^4+k^6$ 在 $k=1/2$ 严格为负。因此保留唯一新增静态必要半空间

$$
a(1/2)\ge0.
\tag{1}
$$

R168 跟踪真实反射、同一 $\Gamma$ 缺陷和唯一协变乘子，给出完整 corrected 二阶系数的奇偶：

$$
b_0(-k)=b_0(k),\qquad
b_1(-k)=-b_1(k),\qquad
b_2(-k)=b_2(k).
\tag{2}
$$

这是关于真实字符的原式必要等式，不是由当前候选拟合的经验规则。程序完整遍历证书中的 Q2_0、Q2_1、Q2_2 每一个已存 degree。凡 degree 的奇偶不符合 (2)，其字符线性行必须为零。

不只选出当前候选的四个非零违例，不硬编码 normal 序号，也不先删除某些变量。正确奇偶的系数保留为原来未知值。

R165 的新频率门在原候选上没有被违反，本次不加入它，不扩大静态取值网或六条路径表。

## 2. 不变输入与两层冻结 helper

输入仍是：

~~~text
topics/visible-flex-new-mechanism/notes/actions-43665971895-1-character_minus2_finite_necessary
~~~

| 输入 | 字节 | SHA256 |
|---|---:|---|
| character-minus2-finite-necessary.json | 10143 | 1e8d751fca7fb6d8b2c33d1152e8651399824be22ffad5496c8bdb48de7fef6c |
| receipt.json | 40026 | 6fbdf4f3c98bfa14fe6344d988a5df9acad10b4c7e598711aa3f5b57c8515764 |
| character-minus2-finite-necessary-certificate.json.gz | 31976 | 5658e056313fff939356f91c97578a8dfc3e1158661b209c84ba7d2b86aa3634 |

证书 raw 为 143028 字节，SHA256 dd539b088c354d99c04af46d8d7c63822679f13ebc02b14a673c76767fd745f7。
原 source 为 05bb659b59997906316ddd2873aedbf4840f62a5。

冻结 helper：

| 源文件 | 字节 | SHA256 |
|---|---:|---|
| literature_character_minus2_static_cut.py | 26313 | d5a65482df040627b1a9a13fb8fce3e813f90e8ec196714cb9cf1bd78e97da5d |
| literature_character_minus2_finite_necessary.py | 45116 | d4c3751cf58f1ef08c534e61a16d7a40cd368980c0cca0ef48a0bce505ce3545 |

新源运行时核对两层 helper 原字节身份，复用前者完整主报告、receipt、raw/gzip 来源校验。它不 import 原 head/profile/forcing helper，不读 head 大原式。

旧 107 个生成坐标、124 条等式、准确 RREF、23 个自由坐标、63 条旧约化半空间、同一乘子与六条路径积分全部继承。新实际不会重算这些目标。

## 3. 追加等式不重做 RREF

设已存变换为 $x=B y$。(1) 由已存静态正规线性行在 $k=1/2$ 求值，沿已存 B 代入。

对任一违反奇偶的系数行 $E(x)$，新源只追加

$$
E(B y)\ge0,\qquad -E(B y)\ge0.
\tag{3}
$$

因此自由坐标的编号、含义与旧 RREF 不变。(3) 准确表达等式，不需要重新消元或声称新的真实函数秩。

所有三族 degree 都有扫描记录，包括正常与异常次数。每个异常条目保存：

- family、degree、要求的模 2 次数；
- 完整原 normal 线性行；
- 已存 B 下的准确自由坐标等式；
- 两个符号各自对应的约化半空间索引；
- 新行、已有行或经旧等式已经为零的状态。

对重复半空间，仅记录已有索引，不修改旧行的 additional_reason_count 或其他元数据。经旧等式已经为零的行也完整记录，不制造虚假的非零行。每个实际新增非零行仅作正的公分母/gcd 归一化，不翻转符号。

所以证书保留了“遍历全部系数”与“去同后实际新增半空间数量”的区别；不会拿后者冒原式独立秩。

## 4. 准确决策与范围

沿用已核的准确双证逻辑：浮点 LP 只提支持；每份有效证书必须在原 Fraction 行上重新核非负乘子与准确目标等式。必须对全部自由坐标的两个符号完成，才可排除全部非零权 −2 正字符。

若仍保存非零外部点，它只是加入 (1)(2) 后的必要系统中的准确可行点。未表达的原函数依赖和全部路径不等式仍可能排它。既不把浮点不可行当证明，也不把外部可行当真实正性。

本轮不会宣称其他权正字符消失、全部闭锥已求出，或完整第四周期/ruling 已支付。

## 5. 八项新人工

人工仅用四个虚构 normal 坐标、三个自由变量和几条简单行，没有读取任何真实 head、原候选或旧证书。

1. 三族所有错误次数均被扫描，专门加入超出当前实际表的高次例；
2. 正确奇偶系数不会被删除或错误置零；
3. 每个非零错误系数有两个准确相反的半空间；
4. 经既有等式为零者仍被记录但不新增假行；
5. 去同不改变任何旧 row record 或原输入；
6. 小人工例的成对条件确约束到所需全部坐标；
7. 重复 degree 元数据被拒绝；
8. 旧 rref、construct_system、path_integrals 设为拒绝哨兵时新奇偶接口仍成功。

这些是新奇偶接口的八项人工，不重跑旧十三项或 static-cut 的八项人工，不做实际研究求解。

## 6. 输出、预算与 CLI

主 schema：

~~~text
visible-flex-character-minus2-static-and-quadratic-parity-cuts-v1
~~~

输出：

~~~text
character-minus2-static-parity.json
character-minus2-static-parity-certificate.json.gz
~~~

完整新证书保存旧输入与未变数据的 canonical 身份、唯一静态新行、完整三族 degree 扫描和所有奇偶等式、更新约化半空间、准确双证或准确新外部点。解释旧 normal 坐标仍需已绑定的原完整证书；不重复复制原 DAG。

预算保持 240 秒、轮询 RSS 1024 MiB、有理数位长 16384 bits；main <95000 字节，新 certificate gzip ≤4500000 字节，总输出 ≤4.8 MB。若完整证书不能保存，主报告不得保留数学排除声明。

建议 lane：character_minus2_static_parity。

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_character_minus2_static_and_parity_cuts.py \
  --toy-only --output WORK/character-minus2-static-parity-development.json

python topics/visible-flex-new-mechanism/scripts/literature_character_minus2_static_and_parity_cuts.py \
  --source-report OLD/character-minus2-finite-necessary.json \
  --source-publication OLD/receipt.json \
  --source-certificate OLD/character-minus2-finite-necessary-certificate.json.gz \
  --output WORK/character-minus2-static-parity.json
~~~

OLD 是第 2 节原目录，不是一个尚未运行的 static-cut 目录。公开实际入口检查 GITHUB_ACTIONS 与本指定公开仓库；本地只执行新增 --toy-only。

