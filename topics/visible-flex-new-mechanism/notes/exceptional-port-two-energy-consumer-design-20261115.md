# 例外偶端芽：两个完整 mixed 能量的最小公开消费者

日期：2026-11-15。此文件是新目标的输入、算法和公开运行接口；不是实际结果。

## 1. 唯一新目标和来源

程序：scripts/literature_exceptional_port_two_energy_gate.py。

最终源码 16867 B，SHA256
e1b9f37b8ce5af296a8120bd790f852b813c8aef5c3befee74ec195f643c0745。

数学来源为
[完整 mixed 领先门 R231](../results/R231-complete-mixed-leading-gate-for-the-exceptional-even-port.md)。
固定 b=0，只计算

$$
L_c=E_0(G_0(f,f),G_0(g,g)-G_0(f,f)),\qquad
L_s=E_0(G_0(f,f),G_0(f,g)).
$$

这里

$$
E_0(a,b)=\frac14\int_I(x^2a''b''+2a'b'),
$$

$$
G_0(a,b)=\frac{xab}{2}
-\frac{x^2(ab'+a'b)}4+\frac{x^3a'b'}4
+\frac{x^2}{8}\int_x^r(\eta^2a''b''+2a'b')\,d\eta.
$$

两个 G(ff)、G(gg) 各自保留真实共同左二次尾；只有其差和 G(fg) 是紧槽。本消费者不调用需要把两个 G 槽都当紧支撑的能量简式。先按完整原算子恢复 G，再按上面的原 E 求值。

实际目标端芽是

$$
h=h_e e^{\varepsilon\sigma^2},\qquad
k=k_e(1-2\varepsilon\sigma^2),\qquad
\omega=k_e/h,
$$

其中 h_e>0、ε>0、k_e≠0，且所选固定 I 满足
x>0、x+k_e/h_e>0。仅在这些 R231 物理条件内使用解析偶部结论。

新问题与 R193 的四个 c 系数不同。不重算 c0/c2/c4/c6、不调用旧
densities、actual 或 halfline_gate，不编译 forcing、几何轨道或 W 基，
也不恢复任何旧 head。

## 2. 冻结输入与唯一依赖

唯一研究来源文件：

scripts/literature_derivative_packet_full_width_gate.py

- 字节数：29108。
- SHA256：adc5b987861633efcf56c1df5a4de4a076055d64444f05c8302025e654de6795。
- schema：visible-flex-derivative-packet-four-coefficient-gate-v1。

新脚本在人工/实际分支之前核其完整字节身份与 schema。只复用
frozen_polynomials、有限有理多项式运算、正立方根区间运算和资源检查。
不要求任何旧机器数据目录，因此新 workflow 只需检出两个脚本。

冻结定义如下：

$$
\rho(t)=51480t^7(1-t)^7,\quad
S(t)=\int_0^t\rho,\quad
\eta(t)=65536t^8(1-t)^8.
$$

ρ、η在 [0,1] 外为零，S 在左右延为 0、1。单 packet 主体为

$$
f_0=S(x-8)-S(x-12),\qquad
g_0=S(x-10)-S(x-14).
$$

设 A=∫(ρ')²、B=∫(η'')²。左补矩在 1、3、5：
f 加入 √(7A/B)η(x−1) 和 3√(A/B)η(x−5)，
g 加入 4√(A/B)η(x−3)。
对应普通复平方系数是 (7,−16,9)A/B，而 real g² 是正 16A/B。
交叉矩由导数支撑分离为零，三个自矩由 R193 已证相等。
本次只为恢复这些原输入幅度重新算必要的 A、B；不重新研究旧 quartic 目标。

完整输入为八个平移 20j 的单 packet，幅度 α_j 取实立方根

$$
\alpha_j^3=(-1)^j\binom7j,\qquad j=0,\ldots,7.
$$

共同宽度伸缩 q_λ(x)=q_raw(x/λ)，λ>0，支撑 [λ,155λ]。
共同正归一化依原 R183 圆约定；两个 quartic 能量同时乘正四次幂，
故不影响严格非零结论。旧 DEFINITION 的完整 hash 仅用于来源追踪；
其中旧 constant_state 字段不作为此次端芽参数，主报告的输入定义已剔除它。

## 3. 全右尾恢复，而非只导数包积分

每个单 packet 保留 n=1,...,14 的全部单位区间，包括：
三个补矩 bump，三个间隙，四个主导数段以及所有常值平台。

局部 t∈[0,1]、x=left+t 上，pair_parts 返回 G 的原局部部分和密度
x²f''g''+2f'g'。从最右端向左依次保持累计量：

$$
J(t)=J_{\mathrm{right}}+\int_0^1 d-\int_0^t d.
$$

recover_original_fields 对 ff、gg、fg 三槽分别保存所有已累计的尾。
不在 piece 边界重设积分常数。常值平台上即使输入导数零，G 的局部值
和右尾仍可能非零，因而这些区间必须参与最后能量积分。

每个 packet 在完成恢复后准确检查：

1. ff 与 gg 的左总密度相同且严格正，fg 左总密度为零。
2. Gff、Ggg 左端 0/1/2 阶导数等于实际 x²C/8 尾，而非零。
3. Gfg 左端和三槽右端 0/1/2 阶导数均符合紧尾/右锚。
4. 全部单位区间接口处三槽的 0/1/2 阶导数相接。

然后逐区间用原 E 积分 Lc、Ls。一次 packet 保存两个新有理值的 hash
和完成检查，不保存大局部多项式。

跨 packet 的尾不是以导数支撑不交为由删除。R231(29) 给出：

$$
E_0(x^2,Z)=0
$$

对真正紧槽 Z 成立。每个 packet 已确认 Ggg−Gff、Gfg 紧尾，
右侧其他 packet 在本 packet 上只给 Gff 增加共同 x² 常倍；
这些跨包交叉才可逐项准确消失。单包内部的所有 history 始终保留。

## 4. 两个有限实代数数和全部宽度

每包振幅的第四幂为 binomial^(4/3)。把相同 binomial 的两包有理值相加，
最终两个值均写成

$$
c_0+c_7\sqrt[3]7+c_{21}\sqrt[3]{21}+c_{35}\sqrt[3]{35},
\qquad c_j\in\mathbb Q.
$$

源码报告完整 2×4 有理表和稀疏精确槽。只有槽向量准确零才立即报零；
非零槽向量不被当作实数非零证明。非零符号必须由正立方根的严格有理
包含区间证明，保留上下界、精度和表达式 hash。超预算仍不能分离则未决，
不得提升为正性/非零。

R231 原式伸缩证明给

$$
L_c(\lambda)=\lambda L_c(1),\qquad
L_s(\lambda)=\lambda L_s(1).
$$

所以只做本次两个 raw 系数，不再运行多项式半轴最小值门或扫描宽度。
若任一严格非零，则所有能嵌入所选 I 的正宽度都违反 R231 必要门。
这不是对任意其他 profile、其他端芽或全部几何的排除。
若两值准确零，仅此领先 mixed 层已付，完整局部恢复及下一层仍待处理。

固定支撑 C4 连续性和 R183/R193 的精确三矩补偿允许严格非零结论转为
C∞ 输入。原 piecewise C7 曲线不直接冒作 C∞。没有严格非零证书时，
程序不宣此转移结论。

## 5. 人工开发范围与当前状态

公开首次 job 必须先 py_compile，再 --toy-only，最后仅在人工成功时 actual。
环境当前不可用，作者没有执行 Python，不能称本地人工已通过。
13 项都是新接口的有限小多项式或代数数玩具；逐条纸核预期值如下：

1. 密度 2、右尾 3 恢复 J=5−2t，左尾 5。
2. 常输入 f=g=1、left=2、非零右尾 3，恢复 G 的系数 (5/2,2,3/8)。
3. 人工 f=t、g=1−t 的原局部 G 为 (t²−t³)/4。
4. 同例原积分密度为 −2。
5. 同例右尾 4 与原局部相加给 t²/2。
6. 对 v=t²(1−t)²，原 E((2+t)²,v)=0。
7. 原 E(2+t,2+t)=1/2，固定 1/4 规范。
8. 原 E(v,v)>0。
9. 两个人工相邻 piece 的累计尾跨界保持，不各自重锚。
10. 第三个左 bump 的 real g² 系数为正 16ratio，不误用复平方负号。
11. n=11 的 f=g=1 平台确实保留。
12. 正立方根 a³=7 满足 a⁴=7a，第四幂权正确。
13. −∛7 的负号由严格有理区间得到。

人工分支不调用 frozen_polynomials，不作实际 profile 积分，不读机器报告。

## 6. 明确 CLI、预算与失败回执

建议 lane 名 exceptional_port_two_energy_gate。

先运行：

~~~sh
python -m py_compile scripts/literature_exceptional_port_two_energy_gate.py
python scripts/literature_exceptional_port_two_energy_gate.py \
  --toy-only --output "$OUT/exceptional-port-two-energy-development.json"
~~~

唯一研究运行：

~~~sh
python scripts/literature_exceptional_port_two_energy_gate.py \
  --seconds 120 --memory-mib 512 --fraction-bits 16384 --max-root-bits 1024 \
  --output "$OUT/exceptional-port-two-energy.json"
~~~

actual 同时要求 GITHUB_ACTIONS=true 与
GITHUB_REPOSITORY=Rogerhu12/math-research-public。人工可在普通环境运行，
但此次尚未执行。最大 CLI 上限为 300 秒、1024 MiB、16384 位有理分子/分母、
2048 次根区间二分精度；默认预算如上。

时间/RSS在复用算术与逐 piece 位置轮询，不称 OS 硬限。
有理位长在每个多项式 trim、Alg 初始化及最终 packet 值处检查。
出现资源或环境退出时保 completion、stage、已经完整完成的 packet 检查，
以及能已完成的两个能量；不将部分算完的数据叫最终符号证书。

所有异常的正常处理路径给小 JSON，含源码身份、run/source、参数、阶段、
completion、理由、秒数和峰值 RSS。主报告限制小于 95000 B，
不构建 gzip/大型证书。没有来源身份时不进入新研究。

## 7. 公开输出与不重复边界

stdout 第一行是小摘要及完整临时 JSON 的 bytes/SHA256。
actual 完成两个能量后另外输出：

- MATHEMATICAL_TWO_ENERGY_COEFFICIENTS：完整两个 4 槽有理表；
- MATHEMATICAL_TWO_ENERGY_SIGN_PROOFS：准确零或严格有理区间符号证明。

依根 README 15，JSON 仅 job 内临时保留，不存仓库、不存 Release、不上传
机器 artifact。仓库只保存源码、参数、run 及输出 hash；人读结果论文可引用
完整新有理表和符号推导。

不会重跑：旧四系数、旧三矩研究结论、forcing、W/响应列、head/word、
旧 profile 查询、几何轨道、LP 或完整 ruling 数值积分。
本次是两个新的原 profile 能量的准确算术，所有实际积分只在上述公开 actual
分支执行。
