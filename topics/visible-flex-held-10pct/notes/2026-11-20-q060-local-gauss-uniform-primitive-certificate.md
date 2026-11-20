# q060 尾局部 G16 规则的全域原函数误差

日期：2026-11-20  
维护：Astra-held10-1b6d88ec-20261120 / n4_continue  
可信度：**已证明：真实被积函数、字面 Gauss 节点权重、实数仿射节点下的积分规则误差。** 本条不将未验证的 IEEE/Math.exp 查询误差一并清零。

## 1. 本次实际付清的层

背景仍是 [R58](../results/R58-q060-valley-background-height-and-curvature.md) 的首 valley 4.625、固定 binary 校准常数与真实函数定义。没有启动或重跑尾 Newton。此前
[紧真积分证书](2026-11-20-q060-tail-tight-integral-certificate.md)
只支付全局归一化常数差；本条另外支付**所有局部查询位置的 Gauss 原函数误差**。

取实际 JS 生成的 G16 字面节点及权重，将被积函数按 R58 的真实函数解释，仿射节点、求和与缓存也先按实数解释。允许原工厂所能产生的任意后续二分和任意停止层；不使用 G8/G16 差或 quadratureTolerance 作为误差证明。

对从同一深端锚到任意源坐标 $x$ 的完整累积原函数，严格有：

| 被积项 | 全域绝对误差上界 |
|---|---:|
| $A$ | $3.309513\,10^{-10}$ |
| $B$ | $8.892550\,10^{-18}$ |
| $wA$ | $2.072665\,10^{-11}$ |
| $wB$ | $1.315287\,10^{-17}$ |

因此在固定字面归一化
$\alpha_J=161.16325458995925$ 下，

$$
|\widetilde r-r_{\alpha_J}|<3.309527\,10^{-10},\qquad
|\widetilde h-h_{\alpha_J}|<2.072877\,10^{-11}.       \tag{1}
$$

这里 $r_{\alpha_J}$、$h_{\alpha_J}$ 使用真实积分；带波浪号的量使用上述实数解释的字面 G16 规则。两者固定同一个深端锚，且采用**同一源单元坐标及材料角**。

若只比较半径值和未更改的手填一阶量
$r_x=A+\alpha_JB$，相关对角度量矩阵的相对误差小于

$$
1.323810611\,10^{-8}.                              \tag{2}
$$

再与已付的全局归一化分项复合，有

$$
1.373350983\,10^{-8}.                              \tag{3}
$$

(2)–(3) 是值/手填 jet 矩阵的分项预算，**不是**自适应分支程序逐点导数的误差证书，也不是整个非旋转尾图的度量验收。

实际最终执行 session **6258** 已返回 **exit 0**，35.3643 秒。显式覆盖前32个单元，另付全部未修改深端余项；35个 cap 阈值根盒、128个原 source critical split 均包含在证明中。

## 2. 被核查的源规则

当前
closing_recalibrated_tail.mjs 的局部规则为：

- 初始网格为16段，$i/16\le x\le(i+1)/16$；
- 每段先按 source 保存的 critical split 切开；
- 每次递归计算 G8 和 G16；满足数值判据或达到16层即返回 G16，否则对半递归；
- entry.point(x) 使用 cumA/cumB 的完整网格前缀，再加最后一个局部部分积分；
- physicalCell 的半径用这些数值原函数，而 drdx 直接取被积函数 $A+\alpha_JB$。

加权 wrapper 改的是 $B$ 及对应的累积量，不改变上述规则。实际源 SHA-256：

~~~
closing_weighted_tail.mjs
740e672edee58cff7a15f89d75e181577dd439c1c62777c57d0d0ab1af32141e

closing_recalibrated_tail.mjs
4a109f26b0e6c9741dfff678c0fe42da4935bfda9c605e55688e97848aef0dd6
~~~

由最后一条可知，不能将返回的 drdx 直接称为自适应分支半径程序的真实导数。正确的后续 $C^2$ 对象应使用同一真实原函数或另作明确的兼容表示；本条不跨过这一差别。

## 3. 字面 G16 的精确 Peano 常数

把源生成的节点 $g_i$ 和权重 $w_i$ 均视为精确 binary64 有理数，归一到 $[0,1]$：

$$
t_i=(1+g_i)/2,\quad \omega_i=w_i/2,\quad
Q(f)=\sum_{i=1}^{16}\omega_i f(t_i),\quad
L(f)=\int_0^1f-Q(f).
$$

节点在 $(0,1)$，权重严格为正。令

$$
\mu_j=\frac1{j+1}-\sum_i\omega_i t_i^j,\qquad
K_m(t)=\frac{(1-t)^m}{m!}
-\sum_{t_i\ge t}\omega_i\frac{(t_i-t)^{m-1}}{(m-1)!}. \tag{4}
$$

这些量全部在有理数中计算。没有把字面规则误认为恰好满足所有经典 Gauss 矩条件。实际

$$
\max_{0\le j\le8}|\mu_j|<2.200\,10^{-15},\qquad
\tau:=\min(t_1,1-t_{16})>.00529953250417503,
$$

其中节点按大小排序；$\sum\omega_i<1$。较宽但严格的常数如下：

| $m$ | $\|K_m\|_1$ 上界 | $\|K_m\|_\infty$ 上界 |
|---:|---:|---:|
| 2 | $1.944175\,10^{-4}$ | $7.495413\,10^{-4}$ |
| 3 | $2.667611\,10^{-6}$ | $7.009494\,10^{-6}$ |
| 4 | $3.634831\,10^{-8}$ | $1.139325\,10^{-7}$ |
| 5 | $5.154910\,10^{-10}$ | $1.638832\,10^{-9}$ |
| 6 | $7.405687\,10^{-12}$ | $2.517570\,10^{-11}$ |
| 7 | $1.082619\,10^{-13}$ | $3.926048\,10^{-13}$ |
| 8 | $1.605350\,10^{-15}$ | $6.173202\,10^{-15}$ |

证明计算按每两个相邻 Gauss 节点之间的精确多项式进行。转换成 Bernstein 系数后，统一符号的区间可精确积分绝对值；其余区间有理二分，剩余量用区间长度乘 Bernstein 绝对上界。无穷范数同样用 Bernstein 凸包和固定细分。原输出保留精确分数，上表只是再朝外取整的展示。

## 4. 分段解析 Peano 恒等式

设 $f$ 在有限个内部点分段解析，存在所需的一侧导数。约定跳跃为右值减左值。Taylor 带积分余项及截断幂展开给出

$$
L(f)=
\sum_{j=0}^{K-1}\frac{f^{(j)}(0)}{j!}\mu_j
+\int_0^1 f^{(K)}(t)K_K(t)\,dt
+\sum_b\sum_{j=0}^{K-1}[f^{(j)}]_bK_{j+1}(b).     \tag{5}
$$

本条使用 $K=8$。式 (5) 中一侧第8导数按各光滑段积分；所有低阶导数跳跃另行加入。因此没有假设 soft cap 全局具有32阶导数。

在长度为 $h$ 的物理 panel 上，若 $C_j$ 包围第 $j$ 导数的绝对值，则

$$
|L_h(f)|\le
\sum_{j=0}^{7}\frac{C_j}{j!}|\mu_j|h^{j+1}
+C_8\|K_8\|_1h^9
+\sum_b\sum_{j=0}^{7}|[f^{(j)}]_b|
 \|K_{j+1}\|_\infty h^{j+1}.                     \tag{6}
$$

对一个初始 panel 的任意自适应分割，
$\sum h_\ell^{j+1}\le H^{j+1}$。每个真实跳跃只落在一个叶子内部；边界重计只会加大上界。故用初始 panel 长度 $H$ 的 (6) 能统一控制任意后续细分和任何部分终点。程序是否因为 G8/G16 差小而停止，对这个上界没有影响。

## 5. soft cap 的跳跃为何已付

真实未截断 log slope 在每个原始九段单元中形如

$$
z_{\rm raw}(x)=a+bS_5(x)+cx,
$$

局部 cap level 为 $d+eS_5(x)$。其中固定校准根、参数等均沿用 R58 的实际 binary 常数，随后按真实函数解释。两条 cap 阈值满足一个至多五次的方程：

$$
z_{\rm raw}(x)-z_{\rm cap}(x)=\pm2.                \tag{7}
$$

源使用七次平滑权及其八次原函数。这给 cap 后的 log slope 全局 $C^4$，但第5导数可以跳跃。因此：

- 普通段 $A=|w'|/[8(1+w^2)^{3/2}]$ 和 $wA$，在排除 absolute-value critical cusp 后为 $C^3$，第一项可能非零跳跃是第4阶；
- $B$ 和 $wB$ 为 $C^4$，第一项可能非零跳跃是第5阶；
- 外 port 的特殊 $A$ 使用其完整混合公式，不误用普通段简式。

脚本用 (7) 的区间 Bernstein 系数完整排除无根区间；其余二分为小于 $10^{-15}$ 的根盒。在阈值盒中强制阈值的精确值关系，再对两侧公式作区间高阶自动微分，收取 (6) 的所有4至7阶或5至7阶跳跃。每个未完全分开的根盒保守按五个根计；并未凭浮点根个数宣称完整。

本次实际得到35个阈值根盒。第8导数范围来自原四阶核的同一 Taylor 代数扩展到9阶：若 $J_k=f^{(k)}/k!$，乘法、指数和正值实幂均按封闭的系数递推实现。普通 $A$ 的第8阶需要 log slope 的第9阶，代码确实保留了这一阶。

作为实现检查，另对9个覆盖 head/deep、cap/普通/外 port 的位置，将0至8阶系数与独立高精度标量微分比较，共324项全部被区间包含。连续证明使用 (5)–(7) 与全盒区间范围，该点检查不替代它们。

## 6. 近似 critical split 与绝对值 cusp

源保存的是数值 critical split，不能把它们直接认成真实极值。对每个原 split $p$，取

$$
[p-d,p+d]\cap[0,1],\qquad d=10^{-10}.
$$

在这些小带以外，程序通过区间细分证明真实 log slope 导数保持同一符号；全128个原 split 对应的检查均实际通过。精确的 cap 平台按零导数处理。因而所有会破坏普通 $A$ 高阶正则性的未决符号变化，都已限制在这些小带中。

在 source split 的一侧，可能错号的条带宽度至多 $d$。若一个 Gauss 节点落在条带中，该叶子长度至多 $d/\tau$；所有相关叶子的总长度至多 $d(1+1/\tau)$。由正权性，设 $U$ 包围该小带内有符号普通被积项的绝对值，则两侧完整误差可取

$$
4Ud\left[1+\Bigl(\sum_i\omega_i\Bigr)(1+1/\tau)\right]. \tag{8}
$$

这里直接区间计算 $U$，不额外假定根是简单根。若条带重叠，分别收取原条带，允许重计。本次所有同一 piece 内的 split 间隔实际上大于 .4802，远大于 $2d$。

式 (8) 使用了条带贴着**实际 source split 边缘**这一事实；没有将其错误搬到未分段 panel 内部。最终所有这些错位带的总成本小于

$$
1.059\,10^{-17}\quad(A),\qquad
8.806\,10^{-19}\quad(wA).                          \tag{9}
$$

n0/j7 的 cut-preserving 混合在左端有精确平坦导数。对该段使用同一个导数的 $x^2$ 因式形式：

$$
z'=(1-S_5)z_{\rm cap}'
+x^2\{x(10-15x+6x^2)z_{\rm raw}'
 +30(1-x)^2(z_{\rm raw}-z_{\rm cap})\}.
$$

又 $z_{\rm raw}-z_{\rm cap}\ge0$，故能保留端点的真实符号。初版展开式的区间依赖损失因此消除，物理 profile 没有改变。

## 7. 全部未修改深端

对 $n\ge N=32$，沿用 R58 已证的

$$
W_N=256\,2^{-7N/4},\qquad H_N=17+\frac75N,\qquad q=3/10.
$$

该范围内全部 valley/weight 改动已结束，$w\le W_N$ 且 cap 不再起作用。四个过渡的 log level 差分别不超过 $H_n$，
$\sup S_5'=15/8$。因此任意正权 G16 分割的普通 $A$ 累计值满足

$$
Q_A\le\frac{(\sum\omega_i)W_N}{8}
\left[\frac{(15/2)H_N+1}{1-q}
+\frac{(21/2)q}{(1-q)^2}\right].                  \tag{10}
$$

真实 $A$ 积分仍用 R58 的总变差界。两者相加已经能严格支付该深端误差，唯一的 cell159 内侧混合再以旧径向跨度补入。

$B$ 可更紧：每一小段旧径向导数的最大最小比不超过

$$
e^{\ell_N},\qquad \ell_N=\delta_0\,2^{-N}/\sqrt{12}.
$$

正权规则与真实部分积分的比位于

$$
\left[
\frac{(\sum\omega_i)e^{-\ell_N}}{1+W_N^2},\
(\sum\omega_i)e^{\ell_N}(1+W_N^2)
\right].                                       \tag{11}
$$

把 (11) 的偏离1乘完整旧径向跨度；cell159 内侧混合另作正值上界。高度项再乘 $W_N$ 即可。

最终未修改深端误差小于

$$
(A,B,wA,wB)_{\rm deep}
<
(4.566\,10^{-13},\ 4.906\,10^{-26},\
1.622\,10^{-27},\ 8.597\,10^{-28}).               \tag{12}
$$

这覆盖到 protectCell=160 的全部改造背景，并用 R58 的相同深端锚。没有把有限真正尾场误称为已经存在无限非线性极限。

## 8. (1)–(3) 的坐标和对象契约

本条在原 source 单元坐标 $x$ 与同一材料角 $\theta$ 中比较。真实旋转背景度量为

$$
g_\alpha=\operatorname{diag}
\big((1+w^2)(A+\alpha B)^2,\ r_\alpha^2\big).
$$

对 G16 值/手填 jet 矩阵，径向项仍使用同一个 $A+\alpha_JB$；本积分规则分项只改变半径值。因真实半径至少为固定 cuff 半径
$.04999999999999999$，若 (1) 的半径界为 $\varepsilon_r$，则

$$
\|g_{\alpha_J}^{-1/2}
 (\widetilde g_{\rm hand}-g_{\alpha_J})
 g_{\alpha_J}^{-1/2}\|
\le 2\frac{\varepsilon_r}{r_{\rm cuff}}
 +\left(\frac{\varepsilon_r}{r_{\rm cuff}}\right)^2,
$$

得到 (2)。再用已有归一化分项 $e_\alpha<4.954038\,10^{-10}$，复合上界为

$$
(1+e_{\rm quad})(1+e_\alpha)-1,
$$

即 (3)。

若改用各自物理半径作参数，须另外明确拉回和场的表示，不能省略这个坐标变化。特别是，数值原函数很接近真原函数，不自动证明它的逐点导数接近手填 drdx，也不自动证明字面分支图是 $C^2$。

本条尚未包含：

- JS 变量查询时的 IEEE 仿射节点形成、各层求和及缓存加法；
- source 有限常数代数组合与 R58 真常数表达之间的剩余差；
- 变量 Math.exp 等 elementary 求值误差；
- 非旋转场、共同均值、实际尾的 Cartesian 接缝和完整闭合表示。

这些项目在机器记录中仍明确为 unpaid。后续可直接使用真正区间背景作为目标 $g$，但不能把本条部分预算说成原完整浮点 query 已经逐项认证。

## 9. 源、实际执行与复现

新增源：

- [dump_q060_local_quadrature.mjs](../scripts/resume_n4/dump_q060_local_quadrature.mjs)
- [certify_q060_gauss_peano_constants.py](../scripts/resume_n4/certify_q060_gauss_peano_constants.py)
- [certify_q060_local_quadrature.py](../scripts/resume_n4/certify_q060_local_quadrature.py)

读取 R58 的 constants.json 和已发布紧真积分结果后，设 WORK 为工作目录，TOPIC 为课题目录，SOURCE 为恢复后的 visible-flexible-closed-surface 源目录：

~~~bash
node "$TOPIC/scripts/resume_n4/dump_q060_local_quadrature.mjs" \
  "$SOURCE" "$WORK/m3-work/bootstrap/q060-port.json" \
  "$WORK/n4-work/q060-tail-geometry/local-quadrature-cache-final.json" \
  "$WORK/n4-work/q060-tail-geometry/local-gauss-rules-final.json"

python "$TOPIC/scripts/resume_n4/certify_q060_gauss_peano_constants.py" \
  --rules "$WORK/n4-work/q060-tail-geometry/local-gauss-rules-final.json" \
  --out "$WORK/n4-work/q060-tail-geometry/local-gauss-peano-final.json"

OPENBLAS_NUM_THREADS=1 python "$TOPIC/scripts/resume_n4/certify_q060_local_quadrature.py" \
  --kernel "$TOPIC/scripts/resume_n4/certify_q060_background_integrals_tight.py" \
  --constants "$WORK/n4-work/q060-tail-geometry/constants.json" \
  --cache "$WORK/n4-work/q060-tail-geometry/local-quadrature-cache-final.json" \
  --peano "$WORK/n4-work/q060-tail-geometry/local-gauss-peano-final.json" \
  --normalization-certificate "$WORK/n4-work/q060-tail-geometry/tight-integrals-certificate.json" \
  --inspect-cells 32 \
  --out "$WORK/n4-work/q060-tail-geometry/local-quadrature-certificate-final.json"
~~~

最终主源 SHA-256：

~~~
3a16b0a616035609e115132a775b9cf38ccfc508be31bd8f272a7ffb1ba43a27
~~~

本次完整输出 SHA-256：

~~~
75b372105557899b6e4366748397c9de8872e238234ccbb63820244a51fbd955
~~~

[紧凑执行记录](2026-11-20-q060-local-gauss-execution.json)
保存实际命令、输入/依赖/输出散列和小标量。本次执行源位于 scratch，与提交源逐字一致；Peano helper 只改发布文件名，内容未变。可再生的规则数组、缓存、区间树与完整输出不入 Git 或 Release。

这是一项背景原函数分项的实际连续证书。后续继续支付其余求值分项和真实尾，不把它当作全题、全闭面或固定参数收敛的完成。
