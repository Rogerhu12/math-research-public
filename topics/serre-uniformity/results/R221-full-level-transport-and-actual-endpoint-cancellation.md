# R221：全部 Hecke 核的真实 level 运输、端点 primitive 与 D0 消项

状态：**已证明并已完整实算**。2026-11-13。

本结果在 R209 的两源常数核 DAG／四阶变形上恢复真实 level-41
标号，将 R216 的 scalar primitive 接到全部 54 个指定 Hecke 指数，
并逐项核实与全局主函数的 D0 线性因子相消。它给出完整的积分接口，
不宣称尚未装配的 51 个全局高度、QC 共同根或 Serre 一致性主目标已经完成。

## 1. 结论和实际规模

记 R145 原 family0 的 54 个基点为 \(X_i\)，物理参数为
\(t=B-32\)，\(Y_i\) 的参数为已保存的 \(t_i\in47R_2\)。始终使用
\(D_0(mB)=\sum_i(Y_i-X_i)\)，不重新选择 family，不把 R197 的 projective
参数代入这个物理参数。

两源分别是 \(A=1,B=32\) 和 \(A=-1,B=0\)。对每源的全部 3326 个 DAG
节点（3282 个指定目标及 44 个必要辅助节点），已从真实椭圆曲线点算出
\(\phi(P),\phi(Q)\) 的参考基矩阵、同构尺度和所有所需 necklace 标号。
原始 \(\phi Q\) 始终保留；矩阵行列式为总次数 \(n\bmod41\)，没有乘
\(n^{-1}\) 把它改成行列式 1。

对 54 指数的 3282 个目标，原 family0 给出 177228 个积分端点行：

| 类型 | 实际行数 | 已取得的量 |
|---|---:|---|
| 普通标号 | 176678 | 完整 tiny primitive 差 |
| 真 CM3 标号 | 12 | 完整正则 primitive 差 |
| 真 CM4 标号 | 538 | 正则部分、整线性因子和相消后的全部单位对数 |

全部 54 个合并余项都由实际运算落在 \(\mathbf Q_{47}\)，而非只在
\(R_2\)。七个没有 CM4 对数碰撞的指数得到完整 tiny 值：

| 指数 | tiny 值模 \(47^4=4879681\) |
|---:|---:|
| 1 | 890368 |
| 2 | 463561 |
| 3 | 924161 |
| 4（\(C_4\)） | 845060 |
| 7 | 1994633 |
| 15 | 4770829 |
| 17 | 1333484 |

前三值是独立检查，不参与求解。其余指数的输出明确区分完整 tiny 值与
须和全局范数配对的合并余项。

## 2. 从核多项式到实际 41 挠点

计算使用已发布的 \(\mathbf F_{47^{80}}\) 模型及其中的
\(\mathbf F_{47^2}\) 嵌入。对原五参考曲线和精确模型
\(E_{-4}:A=1,B=0\)、\(E_{-3}:A=0,B=1\)，分别真实构造
\[
 \{aP+bQ:0\le a,b<41\}.
\]
逐点验证曲线方程、\([41]P=[41]Q=0\) 及 1681 个点互异。
坐标表的有序 SHA 保存在证书中。因此每次基变换是实际点坐标相等，
不是由 \(j\) 或 Frobenius 迹猜测一个矩阵。

设奇素数核的首一多项式为 \(h(x)=\prod_a(x-a)\)，
\(s_1=\sum a\)，\(f=x^3+Ax+B\)，并令
\[
 S_1=h'/h,\quad S_2=S_1^2-h''/h,\quad
 S_3=S_1^3-\tfrac32S_1h''/h+\tfrac12h'''/h.
\]
归一化 Vélu 映射为
\[
 \phi_x=\ell x-2s_1-2f'S_1+4fS_2,\qquad
 \phi_y=y\bigl(\ell-12xS_1+6f'S_2-8fS_3\bigr).
\tag{1}
\]
证明只需对一对核点 \(\pm T\) 使用加法公式：其对 \(x\) 的贡献是
\(2f'(a)/(x-a)+4f(a)/(x-a)^2\)，求和后即得第一式；对 \(x\) 微分得
第二式。所以 \(\phi^*(dx/y)=dx/y\)。程序中的 \(h''/2,h'''/6\) 是除阶乘
导数，代入后系数恰为 (1)。

二次核 \((r,0)\) 则用
\[
 \phi_x=x+\frac{3r^2+A}{x-r},\qquad
 \phi_y=y\left(1-\frac{3r^2+A}{(x-r)^2}\right).
\tag{2}
\]
核次数与 41 互素，所用分母在非零 41 挠点处均非零。每条边均检查父点和
像点的曲线方程。由父节点恢复原始点，再按 (1)/(2) 运输；没有在复合途中
遗失前一条边的 level 结构。

给定目标同构 \((x,y)=(c^2x_*,c^3y_*)\)，在完整点表中找到两列，得到
\(g\in\mathrm{GL}_2(\mathbf F_{41})\)。Weil 配对给
\(\det g=\deg\phi\pmod{41}\)，程序对每节点实际验证该等式。Necklace
按同一 \(g\) 运输。有限 étale 的 41-level 结构在 47-adic 盘内唯一延拓，
故这些真实剩余标号足够确定整个变形盘；这里不声称重新计算了全部 41 挠点
的四阶坐标。

整数域乘法的加速只预先计算 \(x^k\bmod F\) 的 159×80 约化矩阵。
卷积后立即模 47，再矩阵乘法；中间整数分别受
\(80\cdot46^2\)、\(159\cdot46^2\) 控制，远小于 \(2^{63}\)。无浮点计算。
它与原逐项多项式约化作了独立比较。

## 3. 参考模型和端点的精确参数

输出的外层 `reference_key` 使用原五参考，保持 R216 接口。
每个 \(j\equiv0,1728\pmod{47}\) 节点还同时提供 `coarse` 子对象，
其中尺度、矩阵和标号都是精确 CM 模型的实际结果，不限于真椭圆标号：

| 参考 | 固定模型 | `stack_parameter` | 真椭圆标号的参数 |
|---|---|---|---|
| CM4 | \(A=1,B=t\) | \(t\) | \(u=t^2=B^2/A^3\) |
| CM3 | \(A=t,B=1\) | \(t\) | \(u=t^3=A^3/B^2\) |

对普通标号继续用 stack 参数；只有真正 E2/E3 标号改用 \(u\)。
这允许后续全局范数计算统一选择精确 CM 参考而不混淆普通点与椭圆点。

设 R209 给出的实际目标四阶模型为 \(A(t),B(t)\)，常数同构尺度为 \(c_0\)。
当参考的 \(A_*\) 为单位时，端点的固定参考参数由
\[
 B_{\mathrm{ref}}(t)
 =\frac{B(t)}{c_0^6}\left(\frac{A(t)}{A(0)}\right)^{-3/2}
\tag{3}
\]
减去该参考的常数 \(B_*\) 得到。若参考 \(B_*\) 是单位且
\(j\equiv0\)，则相应公式为
\[
 A_{\mathrm{ref}}(t)
 =\frac{A(t)}{c_0^4}\left(\frac{B(t)}{B(0)}\right)^{-2/3}.
\tag{4}
\]
括号中的单位均属于 \(1+47R_2\)，二项式展开至三次即模 \(47^4\) 精确。
因此无需每个端点重新选根，也无尺度分支歧义。尺度分支的改变已经同时反映
在真实 level 矩阵中。

普通 primitive 用 R216 的次数 1、2、3 系数求
\(F(t_{\mathrm{ref}}(t_i))-F(t_{\mathrm{ref}}(0))\)。系数模 \(47^3\) 足够，
因为各参数在 \(47R_2\)。真 CM3 的 \(u\in47^3R_2\)，只需其常数微分系数
乘 \(u_Y-u_X\)。不再额外乘 \(1/n\)：实际同源端点及其换参已经给出
\(\int\phi^*\eta\)。

## 4. 真 CM4 的四阶整因子和单位余项

R216 已证明，在每个真 CM4 盘
\[
 \eta=\left(\frac1u+c_0+c_1u+\cdots\right)du.
\]
对撞到该盘的 Hecke 分支，\(B(0)\in47R_2\)、\(A(0)\) 为单位，而且
\(B'(0)\) 为单位。后一点也由 R209 的
\(b_{\mathrm{target}}=b_{\mathrm{source}}/n\) 以及
\(B'=-6aB-\frac43 A^2b\) 在 \(B\equiv0\) 处立即得到；程序直接验证
所有 538 行所涉分支的这个单位条件。

令 \(B(t)=b_0+b_1t+\cdots+b_4t^4+O(t^5)\)。两次单位 Newton 步求出
唯一 \(\alpha\in47R_2\) 至模 \(47^4\)，并整除为
\[
 B(t)=(t-\alpha)v(t),\qquad
 \begin{aligned}
 v_0&=b_1+b_2\alpha+b_3\alpha^2+b_4\alpha^3,\\
 v_1&=b_2+b_3\alpha+b_4\alpha^2,\\
 v_2&=b_3+b_4\alpha,\qquad v_3=b_4.
 \end{aligned}
\tag{5}
\]
所有 \(v_0\) 为单位。每行都验证
\((t_i-\alpha)v(t_i)=B(t_i)\pmod{47^4}\)。被省略的 \(b_5t^5\) 对
\(v(t_i)\) 的贡献至少为 \(47^4\)，所以四阶已足够；三阶一般不足。

因此该行的积分为
\[
 2\log\frac{t_i-\alpha}{-\alpha}
 +2\log\frac{v(t_i)}{v(0)}
 -3\log\frac{A(t_i)}{A(0)}
 +c_0(u_Y-u_X)\pmod{47^4}.
\tag{6}
\]
后面三项已经实际算完：两个对数的比值都在 \(1+47R_2\)，使用
\(\log(1+z)=z-z^2/2+z^3/3\)。从未在模 \(47^4\) 下直接倒置
\(B(0)\)、\(B(t_i)\) 或 \(u\)，也没有把第一项误设为零。

公式 (6) 对目标的常数或变动同构尺度不变：\(u=B^2/A^3\) 不变，
由 \(B\) 的尺度产生的单位对数正好由 \(-3\log A\) 项补偿。

## 5. 与同一个 f_B 的 D0 因子逐项相消

仍取 R197 的同一个主函数
\[
 \operatorname{div}(f_B)=mB-D_0(mB),\qquad
 m=21113421681728164076758160383370947105909472013138012462421148345826995695660466565589785072.
\]
在第 \(i\) 个原 j9 物理盘内，其由 D0 引起的线性因子是
\[
 \frac{t}{t-t_i}.
\tag{7}
\]
所以在静态 CM Hecke 点 \(t=\alpha\) 上，(7) 的值为
\(\alpha/(\alpha-t_i)\)，正好抵消 (6) 的
\((t_i-\alpha)/(-\alpha)\)。这里的单位部分必须与同一局部物理参数下的
Miller／末端函数一起保留；不能只丢弃一个低赋值因子。

这个配对已对全部 54 指数独立实际核实。具体地，在 CM4 源的真实静态
Hecke 像中，搜出所有落在 j9 参考且标号属于原 54 个 \(X_i\) 的行；
以 **(原 necklace 标号，物理参数 \(\alpha\))** 作计数器。每一指数的计数器
都严格等于 source-j9 端点的 CM4 极点计数器乘 2。总数分别为
\[
 1076=2\cdot538.
\]
完整对应列表保存在 `D0_matches`，包括双方节点、行号、参数和重数。
因而重数 2 不来自对总次数的猜测。其几何原因是粗 CM4 参数
\(u=B^2/A^3\) 的二次零；自伴 Hecke 对应给出两边同一个精确因子除子。
数值匹配定位了这些因子至本次所需精度，精确相消来自该除子恒等式。
若不同精确分支在模 \(47^4\) 下相遇，单位余项仍只依赖所保存的这个精度。

故送入后续全局总装的量是：普通积分、CM3 正则积分，以及每个 CM4 行的
\[
 2\log(v_Y/v_0)-3\log(A_Y/A_0)+c_0(u_Y-u_0),
\tag{8}
\]
再加上已消去 (7) 的同一 \(f_B\) 单位范数。R221 并未声称这个单位范数已计算。
Miller 初始、负点、当前理想、最终末端 \(g\) 及 frame 因子均仍由完整范数
步骤负责，不可因本节的线性因子匹配而省略。

## 6. 静态真正 CM4 邻域的额外精度清单

上一节只消去 D0 因子；它不消去真正 \(mB\) 支持引起的
\(m\log(j-1728)\)。完整 CM4 静态目标中：

* 38 个水平节点、760 行恰为真正 \(Z_{-4}\)；
* 200 个不同节点各有一行邻近真 CM4，全部满足 \(v_{47}(B)=1\)；
* 没有赋值 2 或 3 的额外近点；真 CM3 标号另有 4 行。

对每个指数，程序检查水平节点数等于
\[
 \rho_{\mathrm{cyc}}(n)
 =\frac14\#\{(a,b)\in\mathbf Z^2:a^2+b^2=n,\ \gcd(a,b)=1\}.
\]
这正是 Gaussian CM 自同源的循环核数；四个单位给同一核。
对 \(n=4\) 得 0，与本课题的 \(C_4\) 六个循环核一致。由 R199 的完整对应和
这个逐项计数，模 \(47^4\) 为零的 760 行全是真 \(Z_{-4}\)，没有被隐藏的
更高赋值近点。

200 个近点的 \(u\) 赋值为 2。要取得 \(\log u\bmod47^4\)，须知道
\(B/47\bmod47^4\)，所以这些路径的 \(B\) 要补到模 \(47^5\)；\(A\) 的原
四位足够。清单 `near_CM4_node_inventory` 给出全部 200 个 node key、指数、
完整祖先路径和实际行号。它允许只提升必要路径，而不重算全部素核。
不能仅凭现有 \(u\bmod47^4\) 相等就合并这些静态对数；合并须在所需位数
核实，或另有精确 CM 对应身份。

## 7. 可复现程序、输入绑定与边界

程序都只读已有证书，没有新的大 Miller 链或大挠点域重算：

* `p41_dag_level_transport47.py`：真实两源 level 运输；每 100 节点落盘。
* `p41_dag_endpoint_integrals47.py`：物理端点、全部 primitive、整因子和单位余项。
* `p41_dag_cancellation47.py`：1076 行逐项消项及 200 路径补位清单。
* `p41_dag_equivalence47.py`：把 source 运输期间的两个 DAG 生成版本精确绑定。

source 运输先使用较早 DAG 序列化；随后逐字段比较了两版本的 `curve`、
`order`、`modulus`、`indices`、全部 `nodes` 和 `targets`，包括每个核系数、
模型、线 ID、父路径，3326 节点全部相同。等价证书绑定两文件 SHA 和 level
输出 SHA。端点计算读取规范的较新 DAG／四阶文件，并检查此等价证书。
这仅解决来源元数据不同，不替换任何已执行的数学计算。

在课题目录下可重新生成（`CHECKPOINT_DIR` 使用自己的持久检查点目录）：

```bash
OPENBLAS_NUM_THREADS=1 python scripts/p41_dag_level_transport47.py \
  --script-dir scripts \
  --dag scripts/data/p41_source_j9_descending_kernel_dag47.json.gz \
  --output "$CHECKPOINT_DIR/p41_source_j9_descending_level47.json.gz"

OPENBLAS_NUM_THREADS=1 python scripts/p41_dag_level_transport47.py \
  --script-dir scripts \
  --dag scripts/data/p41_CM4_descending_kernel_dag47.json.gz \
  --output "$CHECKPOINT_DIR/p41_CM4_descending_level47.json.gz"

python scripts/p41_dag_endpoint_integrals47.py \
  --dag scripts/data/p41_source_j9_descending_kernel_dag47.json.gz \
  --quartic scripts/data/p41_source_j9_descending_gauss_manin_quartic47.json.gz \
  --level "$CHECKPOINT_DIR/p41_source_j9_descending_level47.json.gz" \
  --primitives scripts/data/p41_scalar_primitive_atlas47_complete.json.gz \
  --source-frame scripts/data/p41_hecke3_formal_height47_compact.json.gz \
  --output "$CHECKPOINT_DIR/p41_source_j9_all_endpoint_integrals47.json.gz"

python scripts/p41_dag_cancellation47.py \
  --cm-dag scripts/data/p41_CM4_descending_kernel_dag47.json.gz \
  --cm-level "$CHECKPOINT_DIR/p41_CM4_descending_level47.json.gz" \
  --source-dag scripts/data/p41_source_j9_descending_kernel_dag47.json.gz \
  --endpoints "$CHECKPOINT_DIR/p41_source_j9_all_endpoint_integrals47.json.gz" \
  --primitives scripts/data/p41_scalar_primitive_atlas47_complete.json.gz \
  --output "$CHECKPOINT_DIR/p41_all_D0_cancellation_and_CM4_poles47.json.gz"
```

若直接使用本次已保存的 source level 输出，应给 endpoint 程序另加
`--equivalence scripts/data/p41_source_j9_dag_equivalence47.json`。重新在规范
DAG 上生成 level 后不需要该参数；来源哈希可能不同，但数学节点、积分和
配对数据应一致。

主要输出 SHA-256：

| 文件 | SHA-256 |
|---|---|
| source level | `9e89d6f7907eb7d27d765337bae3ab5d8f802bce441565bad3da6ecc96619e67` |
| CM4 level | `e28dcd6844a504568061f92539405aa8e3ca1ff6867ca54a797c3edc6dba54dc` |
| 全部 endpoint | `f6e76ad3577d805e3907543fbae41fcdd0c9af56e0ce4d4b7a32edb076e4888d` |
| D0 消项／CM4 补位 | `607c5761d27bd9840b0ef8f034c7bfcf7771c178f5f786c779fe0b5a2bc13bc3` |
| DAG 等价绑定 | `a7b97028e8c5106e8f0ba115292422b8794e15ef95df6634128b2bfed7b3d96b` |

R221 完成全部实际 level、端点和 D0 消项输入。尚须同一 \(f_B\) 的剩余
静态单位范数、上述 200 路径的额外位数、51 个全局高度、全局系数及完整 QC
盘共同根，才能完成本有限素数分支；主 uniformity 目标仍另有开放障碍。
