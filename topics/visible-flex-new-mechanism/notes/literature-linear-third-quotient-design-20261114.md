# 完整 C1 对角第三一形式的商检验

日期：2026-11-14。状态：**准确算法及人工开发检查；真实目标尚未执行。**

独占脚本：`../scripts/literature_linear_third_bridge_quotient.py`。本稿不改已发表的 R71、R73、R76、R77 或既有实际输出。研究编译只由本公开仓库自己的 GitHub Actions 执行。

## 1. 要解决的具体兼容问题

实际 run `43630157008` 的 `local_third_exact` 在局部系数函数与 R71 响应组成的形式空间中，给出纯四阶目标的一条准确关系。其中线性速度部分用了三个系数：

$$
h^{-1}k_s: -4,\qquad k_s: -2,\qquad hk_s: -4.
$$

这不允许只给这三个积分赋值后忽略其余线性密度。真实一条桥会同时积累完整线性一形式，其余项可能含 $k,\omega,\log h$。新脚本逐项处理完整密度，确定它们是否可由已知控制空间支付。

本次严格限于对角第三函数

$$
\tau(q)=T(q;q,q).
$$

其中 $q$ 是普通复光滑函数，所有乘积为复双线性乘积；不取共轭。对角恒等式只确定全对称三线性化，**不确定保留外槽、内两槽角色的完整 $T(f;g,j)$**，因而不能独自支付全部相位通道。该完整彩色槽问题由后续独立接口处理。

## 2. 沿用的准确分解

调用冻结的 `literature_local_third_bridge_decompose.py`。它先完成真实几何导数与历史导数，再把历史值置零，从 R56 恢复公式产生 R73 的局部第三密度。不是先把历史函数设成常零再微分。

设

$$
\omega_s=\frac{k_s}{2h},\qquad h>0.
$$

已有准确分解为

$$
C_s=D_s(P_{\rm acc}+P_h)
 +\mathcal A(h,k,\omega)(k_sh_{ss}-h_sk_{ss})
 +\mathcal C(h,k,\omega;h_s,k_s)
 +k_sR(h,k,\omega),
\tag{1}
$$

其中 $\mathcal C$ 对 $(h_s,k_s)$ 三次齐次。$R$ 是几何 Laurent/log 多项式，系数为准确 profile 函数。脚本保留它的全部系数，不先代入某条状态路径或抽样 profile。

$P_h$ 采用 $h=1$ 的准确零锚。两端都是常 germ 且 $h=1$ 时，$P_{\rm acc}$ 和 $P_h$ 的端差均为零。对其他端点，势项端差必须继续保留；新脚本没有默认为零。

## 3. 两个明确的商空间

设 $\Phi_1,\ldots,\Phi_8$ 是 R73 的八矩二次算子。第一组列是 28 个**第三**对角交换子

$$
\tau_{ij}(q)=\Phi_i(q,\Phi_j(q,q))-
                 \Phi_j(q,\Phi_i(q,q)),\qquad i<j.
\tag{2}
$$

这是 R71 的实际可达第三控制，不是它们经 $H_A$ 映到纯四阶后的响应。$H_A$ 有核，不能把响应层的相等提升成第三层相等。

第二组空间在 (2) 上加入 (1) 中 $\mathcal A$ 的全部几何系数 profile，以及 $\mathcal C$ 四个速度单项的全部几何系数 profile。只删掉准确改写后的零项或完全相同项；不凭数值秩截断。它们的可达性来自 R76/R77 的独立几何证明，不能由本脚本的线性代数给出。

每组都检查相同的完整 $R$。因此报告可区分：原有交换子已经足够、需要三次速度控制、或本次不完备改写仍留下未处理项。

## 4. 精确三矩假说与更一般的三函数检验

从原 $R$ 中取几何单项 $h^{-1},1,h$ 的准确 profile 系数，分别记为 $L_-,L_0,L_+$；这三个单项都要求 $k,\omega,\log h$ 的幂为零。不存在的系数明确取零。

第一项检验是

$$
R(h,k,\omega)\equiv h^{-1}L_-+L_0+hL_+
\pmod{\mathcal W},
\tag{3}
$$

其中 $\mathcal W$ 分别为第 3 节的两个空间。由于 (3) 是整个几何 Laurent/log 多项式的恒等式，每个剩余几何系数都须被支付，不能只验证选中的三个系数。

若 (3) 没有被本次正规化验证，第二项检验允许

$$
R(h,k,\omega)\equiv
 f_-(h,k,\omega,\log h)L_-+
 f_0(h,k,\omega,\log h)L_0+
 f_+(h,k,\omega,\log h)L_+
\pmod{\mathcal W}.
\tag{4}
$$

输出三个实际系数函数及仍未消去的部分。**(4) 通过不意味着三个系数还是 $h^{-1},1,h$。** 当参考 profile 在商空间中相关时，输出的系数表示也不唯一。

所有有理消元都保留缺失主元之后仍可消去的行。一个不在当前列空间的早期行不能使其余目标行直接停止化简。

## 5. 若 (3) 通过，对应的一条真实状态路径

这只是路径的准确三矩身份，不预先宣称 (3) 已通过。令

$$
h_+=2+\sqrt3,\qquad h_-=2-\sqrt3,
\qquad h_+h_-=1,\quad h_++h_-=4.
$$

从 $(h,k,\omega)=(1,1,1)$ 出发，依次在 $k=1$ 升 $h$ 至 $h_+$，在 $h_+$ 将 $k$ 从 $1$ 降至 $0$，在 $k=0$ 改 $h$ 至 $h_-$，在 $h_-$ 将 $k$ 从 $0$ 降至 $-1$，最后在 $k=-1$ 恢复 $h=1$。每段用光滑常端 germ，始终 $h>0$。沿全路径使用唯一的实际积分 $\omega_s=k_s/(2h)$，有

$$
\int dk=-2,\qquad
\int h\,dk=-h_+-h_-=-4,\qquad
\int h^{-1}dk=-h_+^{-1}-h_-^{-1}=-4.
\tag{5}
$$

因此 $\Delta\omega=-2$，末端为 $(1,-1,-1)$，三个积分恰为实际形式关系所需的数。$\omega$ 在所有 $k$ 递减段单调递减，在 $h$ 改变段恒定，故取共同紧区间 $\xi>1$ 可保持 $\xi+\omega>0$。框架、二阶矩、其它第三项、完整四阶范围及最终闭曲面均需另付，不能由 (5) 冒称已完成。

## 6. 正关系的复核及负结果的边界

正规化沿用已执行的全深度 word/shuffle 层，符号约定是

$$
I(f)(\xi)=\int_r^\xi f(x)\,dx,\qquad J=-I.
$$

所有 profile 在同一开放右 collar 为零；没有把左尾重置为零。每一条通过的行关系都从原 profile 表达式和原模空间列重新构造残差，以新的 IBP/word 实例验证零。它不是从消元后的行再次自证。

失败仅表示当前改写代表未发现关系。脚本没有声称 word 正规化完备、代表秩等于真实函数维数，或某个非零代表就是函数非成员证明。预算超限单独输出 `resource_budget_exceeded`；不能混成数学失败。

详细关系矩阵独立输出，包含全部几何键和准确有理系数。可读表达式文件给三个参考 profile 及各类前几个剩余项，受 95 KB 上限时明确标成节录；完整生成程序和哈希保留。主报告不输出大数组或 profile 数值。

## 7. 已执行的人工开发检查

只在人工 profile 多项式上检查：已知三矩关系从原式验证、故意添加的无法支付系数保留、未匹配早期行之后继续消元、$\omega_s=k_s/(2h)$ 接触链式，以及 $h_\pm$ 的二次域三矩身份。全部通过。

报告：`literature-linear-third-quotient-development-check-20261114.json`。此运行没有调用真实 local compiler，没有求 profile/几何积分，也没有拟合路径。

公开 Actions 最小命令：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_linear_third_bridge_quotient.py \
  --out "$VISIBLE_OUT/linear-third-quotient.json"
```

默认预算为 240 秒、600000 个系数 DAG 节点、80000 个 profile atoms、100000 个表达式项、300000 次 IBP 调用及 2 GiB RSS 轮询阈值。输出主报告、`-relations.json`（必要时 gzip）和 `-expressions.json`。实际编译须在 `Rogerhu12/math-research-public` 的 GitHub Actions 中执行；`--toy-only` 不进入研究路径。

无论此次结果如何，本稿都没有支付完整非对称三线性响应、全部四阶相位、$P_0$、完整 ruling 条件、有限等距族、闭面嵌入及 reach。
