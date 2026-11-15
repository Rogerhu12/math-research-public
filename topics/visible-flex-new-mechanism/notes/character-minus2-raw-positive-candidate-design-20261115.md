# 九条真关系之后的一个指定有理点：86 行与完整标量 action 的准确消费

状态：新源码及八项小人工接口已完成；**没有在本地评价指定真实点、读取研究输入进行求解或运行任何旧测试。** 实际只允许本公开仓库 Actions。当前不再追加 $p=-1$ 的 LP，也不运行新的优化、RREF 或路径积分。

新源码：`scripts/literature_character_minus2_raw_positive_candidate.py`。
建议 lane：`character_minus2_raw_positive_candidate`。

## 1. 为什么这次改成指定点核对

run `43671759155` 已将 R174 九条准确原关系加入旧外部系统，总行数 68→86。R176 对该运行保存的外点给出完整 $k=K/h$ 有限负路径；其最高层矩阵非半正定。无需沿着这个点再做逐条必要行 LP 迭代。

R177 给出了一个明确的更强外点。它已经有静态、二次层和完整最高层的纸面平方证明，仍须准确核对它是否确实对应保存的同一个 $\nu=By$、全部 86 行和 R164 的同一乘子。这个核对才是本消费者的唯一新研究目标。

通过全部检查仍只证明这个**外部标量 action** 满足所列条件。原函数空间上的全部线性关系尚未支付，不能宣布真实正字符存在、闭锥已分离或主课题完成。

## 2. 完整指定点

R174 的 12 个参数取

$$
(\alpha,\beta)=(1/4,1/4),
\qquad(B_0,B_2,C_1,D_0,D_2)=(1,1/4,0,1,1),
$$

$$
(a,b,f,g,\ell)=(1,1/4,-1/8,0,1).
$$

原 23 维坐标固定为

$$
\begin{aligned}
y={}&(1/4,0,-1,1,0,1/4,0,-1,1,1,0,1,-1/4,\\
&\quad1,1/4,-1/4,1/16,1/12,-1/8,0,-1/12,1,1/4).
\end{aligned}
$$

没有以该点为初值求解或调整坐标的分支，也没有失败后另找一点的循环。全部坐标仍在旧完整盒 $|y_i|\le1$ 内，并且非零。

实际必须从旧 B 算出完整 107 个生成坐标，再从保存的十四族形式算系数；不能只把纸面预期多项式抄入输出。预期对照表为：

| 族 | 应准确得到的完整多项式 |
|---|---|
| $F_0$ | $1/4+k^2/2+k^4/4$ |
| $Q_{2,0}$ | $1+k^2/4$ |
| $Q_{2,1}$ | $-k^3$ |
| $Q_{2,2}$ | $1+k^2+k^4$ |
| $\bar A_{hh}$ | $1+k^2/4$ |
| $\bar A_{hk}$ | $-k/4$ |
| $\bar A_{kk}$ | $1/16$ |
| $H_1$ | $k/12$ |
| $H_2$ | $-1/8$ |
| $Q_{4,0}$ | $0$ |
| $Q_{4,1}$ | $0$ |
| $Q_{4,2}$ | $0$ |
| $Q_{4,3}$ | $-k/12$ |
| $Q_{4,4}$ | $1+k^2/4$ |

遍历所有已存 degree，包括零系数、旧错误奇偶位置及静态六次项；任何多余非零项都会使完整比较失败，不按预期截断。

八矩顺序仍为 $(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)$，应准确得到

$$
\mu=(0,1/2,2,0,0,0,0,2),\quad
c=0,\quad d=(0,1,6,0,0,0,0,4).
$$

这些同样从原 multiplier/cocycle 形式评价；不另给一组可调乘子。

## 3. 这次实际要核的正证适用性

纸面身份为

$$
F_0=(1+k^2)^2/4\ge1/4,
$$

$$
L_2=h^{-2}\left\{(k')^2+(1+k^2)(r')^2+
\frac{k^2}{4}(k'-2kr')^2\right\},\qquad r=\log h.
$$

R175 的同一完整最高层矩阵应为

$$
M=\begin{pmatrix}1/16&0\\0&11/48\end{pmatrix},
\qquad \det M=11/768.
$$

其五条最高原关系必须逐项为零；纯 h 两项是 $a=1$ 与
$\ell+25a/9=34/9$。令 $\psi=hD_s(k/h^2)$，平端后

$$
\int L_4=
\int\left\{e^{-2r}\left[\left(r''-\frac23(r')^2\right)^2+
\frac{34}{9}(r')^4\right]+\frac1{16}(\psi')^2+
\frac{11}{48}(r'\psi)^2\right\}ds.
$$

这给全部真实平端路径上的标量 action 下界

$$
\mathcal A\ge\frac14\int h^{-2}\,ds>0
$$

（正长度路径）。源码消费已证恒等式，仅准确核它们对应的全部输入系数。它不会重新做积分、Gram 优化或平方分解搜索。若某一系数、行或同一乘子不符，报告保完整失败值，不能继续宣称此正证适用。

## 4. 四件准确输入及原接口绑定

前三件来自
`notes/actions-43671759155-1-character_minus2_literal_relation_cuts/`：

| 输入 | 字节 | SHA256 |
|---|---:|---|
| `character-minus2-literal-relation-cuts.json` | 6961 | `f7c371df8ee3d9faac42a9fd66c392e7397c4065ee773a69072b6ac4807c0881` |
| `receipt.json` | 40896 | `2d4108f8ead23669957edb24f9f621e60647f266e9fae162cecdd01f60010722` |
| `character-minus2-literal-relation-cuts-certificate.json.gz` | 12478 | `cf9a5df3eb3914c3bd5dd53b8b79839b42d87c100af744ea70f6327d5d6eb544` |
| 上项原文 | 59431 | `afa554873c635a265275605f7518f774334c08d925c66a028b2a67da5534c1d5` |

第四件是既有完整系数原件：
`notes/actions-43665971895-1-character_minus2_finite_necessary/character-minus2-finite-necessary-certificate.json.gz`，
31976 字节 / SHA256
`5658e056313fff939356f91c97578a8dfc3e1158661b209c84ba7d2b86aa3634`；
原文 143028 字节 /
`dd539b088c354d99c04af46d8d7c63822679f13ebc02b14a673c76767fd745f7`。

冻结原 raw9 producer 为 31639 字节 /
`1861db94d22ffb1a7c4e96319fb9fe18fed9121a0d1edfeb20f83e22290aa4f0`。
新消费者核 source/run/repository/lane、发布输出的 packed/raw bytes 与 SHA，
再核完整 23/107 接口、旧 B、全十四族、乘子形式和旧 68 行前缀哈希。
raw9 中已经保存九条原关系的完整两 mode 真零记录；本次仅消费它们，
计算其在新点上的值，不重做任何原表达式消元或零证书。

原最早 63 行也与第四输入中的原列表逐字比较。完整 86 行列表保持原顺序、不改 provenance、不重新规范化或生成必要行。

## 5. 实现接口与明确不发生的旧工作

复用冻结 `literature_character_minus2_literal_relation_cuts.py` 的依赖身份，
以及原输入 helper 的字节校验、已存线性形式读取、准确点代入和行值记录。
不调用 `consume` 的旧七输入链，也不重新运行 raw9 LP。
新 source 的实际入口只执行：

1. 读取四个准确输入并核同一接口；
2. 评价一个指定的完整 23 维点；
3. 保存其 107 值、86 行值、九个等式值、十四族及 $\mu,c,d$；
4. 核完整预期系数与 R175 矩阵；
5. 输出准确通过或具体失败，并保留“真实泛函良定义性未付”。

没有新增半空间，没有 LP/Farkas 求解，没有原查询、profile 根或矩阵秩评价。
也不继承已被 R174 排除的旧 R173 点的任何科学结论。

## 6. 输出和预算

默认预算 60 秒、RSS 软轮询 256 MiB、Fraction 位长 16384。参考前一个只做小 LP 的同依赖实际峰值约 91.5 MiB，本消费者没有 LP；这个预算保留充足解码空间，不人为制造无关资源失败。

小主报告名为 `character-minus2-raw-positive-candidate.json`，上限 95000 字节。
完整证书为同 stem 的 `-certificate.json.gz`，上限 4500000 字节，
总输出上限 4.8 MB；预期约为数十 KB。
schema 为 `visible-flex-character-minus2-raw-positive-candidate-v1`。

主字段包括 `prescribed_outer_point_verified`、`inequality_verification`、
`nine_equality_values`、`fourteen_scalar_families`、
`unique_multiplier_and_cocycles` 和 `scalar_action_certificate`。
完整证书保 86 个行值、107 值、23 点、全部旧行、九关系记录及旧 forms/B 的 SHA。
无论检查是否通过，`true_positive_character_constructed=false`。
实现错误、资源或输出退出有独立小回执，不冒成功。

## 7. CLI 与稀疏检出目录

建议新 lane 同时检出以下两个输入目录，避免上一次 raw9 首运行的漏检出问题：

- `topics/visible-flex-new-mechanism/notes/actions-43671759155-1-character_minus2_literal_relation_cuts`
- `topics/visible-flex-new-mechanism/notes/actions-43665971895-1-character_minus2_finite_necessary`

新人工与实际命令：

~~~bash
python -m py_compile topics/visible-flex-new-mechanism/scripts/literature_character_minus2_raw_positive_candidate.py
python topics/visible-flex-new-mechanism/scripts/literature_character_minus2_raw_positive_candidate.py --toy-only --output character-minus2-raw-positive-candidate-development.json
python topics/visible-flex-new-mechanism/scripts/literature_character_minus2_raw_positive_candidate.py \
  --source-report topics/visible-flex-new-mechanism/notes/actions-43671759155-1-character_minus2_literal_relation_cuts/character-minus2-literal-relation-cuts.json \
  --source-publication topics/visible-flex-new-mechanism/notes/actions-43671759155-1-character_minus2_literal_relation_cuts/receipt.json \
  --source-certificate topics/visible-flex-new-mechanism/notes/actions-43671759155-1-character_minus2_literal_relation_cuts/character-minus2-literal-relation-cuts-certificate.json.gz \
  --original-system-certificate topics/visible-flex-new-mechanism/notes/actions-43665971895-1-character_minus2_finite_necessary/character-minus2-finite-necessary-certificate.json.gz \
  --max-seconds 60 --memory-mib 256 --rational-bits 16384 \
  --output character-minus2-raw-positive-candidate.json
~~~

真实入口检查 `GITHUB_ACTIONS=true` 且
`GITHUB_REPOSITORY=Rogerhu12/math-research-public`。上述实际命令未在本机执行。

## 8. 这次新增人工的具体范围

八项人工使用两自由坐标、三生成坐标的自造表，检查同一点的坐标/十四族/乘子，
原表不变、负行与非零等式保留、全 degree 比较、重复零 degree 拒绝、
R175 矩阵与五关系同时必要、静态奇次非零项不能截断。
`rref`、`construct_system`、`path_integrals`、`certify_zero` 在人工中临时替换为报错函数，
确认新接口不调用这些旧研究入口；结束后恢复。

人工没有消费研究输入，没有评价本设计中的真实指定点，也没有重跑任何旧人工套件。
公开首次执行仍先跑该新源的这八项人工，然后才核唯一指定点。
