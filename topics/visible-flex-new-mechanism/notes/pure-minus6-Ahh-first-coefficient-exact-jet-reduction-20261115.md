# 一个完整加速度系数的 pure 权 −6 原式：三阶 profile 导数准确消去

日期：2026-11-15。**已证明的单根原式身份。** 本稿只读已发表的原 DAG 及其身份元数据，再作下列五次纸面分部积分；没有重新编译 forcing、评价 profile、运行正规化或进行成员消元。

## 1. 原根与规范

对象是 [R134](../results/R134-acceleration-layer-from-complete-local-v4.md) 的完整正规加速度系数 $\bar A_{hh}$ 中，状态单项 $h^{-8}k^0\omega^0(\log h)^0$ 的 pure 模式原系数。它已经由 [R136](../results/R136-acceleration-coefficient-beyond-response-and-G-orbit.md) 的五族原式消费者导出：

- 公开 run：`43654534244`；source：`1177f251dc3d9455adf88b585e4c0e4bd6f7e69b`。
- 生产脚本：`literature_acceleration_layer_mixed.py`，47656 B，SHA256 `271dd150fe95d280fdf3cad0f5bbb5b5fde6f81631a96e7fdbfeb628711ebf7c`。
- 原式 schema：`visible-flex-complete-acceleration-layer-mixed-v1-original-expressions`；scope：`five-complete-two-mode-normal-acceleration-families`。
- `family_records[0]`：`family=A_hh`，`state_key=[-8,0,0,0]`，`profile_weights=[-6]`。
- pure 原根：`family_0000_-4`；SHA256 `be363cd7f5ff36e22a59f97051e1373854f228705774385397369178a2bebada`；准确九项。

此处 $-4$ 是相位模式，$-6$ 是 profile 仿射真权，二者不能混用。R134 已证明这类加速度系数不受 $\mathcal B_{m_2}(N_2)$ 的速度四次项改变，因此这里确是完整正规加速度系数的一个原根，不是删掉 $N_2$ 后猜出的近似。

固定同一个右锚 $r_*$，令输入 q 在右 collar 恒为零，并记

$$
I(F)(x)=\int_{r_*}^{x}F(t)\,dt,
\qquad p=q',\qquad r=q'',\qquad r'=q'''.
$$

本稿的 r 是 $q''$，右端另写 $r_*$。原 DAG 的 `int_right` 正是有符号原函数 I，故 $I'=\mathrm{id}$；它不是正尾积分 $J=\int_x^{r_*}$。再置

$$
A=I(r^2),\qquad B=I(r^3),\qquad C=I(r^4).
$$

所有积分保留真实左尾，绝不在 packet 或 s 段间重锚。

## 2. 九项原式和五个完整右锚身份

设上述原系数为 $F_{hh,-6}(q)$。按原根九项直接读出

$$
\begin{aligned}
8192F_{hh,-6}={}&4p^2r^2-8pI(prr')+8pI(xr^2r')-A^2
-2xr^2A\\
&-8xI(pr^2r')+4xI(xr^3r')+4xI(rAr')-x^2r^4.
\end{aligned}                                                   \tag{1}
$$

这里原函数中的 x 是其积分变量；外面的 x 是查询坐标。全部三阶 profile 导数都明确保留在 (1)。

由于 q 及其各阶导数在右 collar 为零，且 A 在同一 collar 为零，下列五个候选原函数的右端值全部为零。因此普通乘积求导准确给

$$
\begin{aligned}
I(prr')&=\frac12pr^2-\frac12B,\\
I(xr^2r')&=\frac13xr^3-\frac13B,\\
I(pr^2r')&=\frac13pr^3-\frac13C,\\
I(xr^3r')&=\frac14xr^4-\frac14C,\\
I(rAr')&=\frac12r^2A-\frac12C.
\end{aligned}                                                   \tag{2}
$$

例如最后一行使用 $A'=r^2$，而
$(r^2A/2)'=rr'A+r^4/2$。第一、三行另使用 $p'=r$。这五式没有遗漏独立积分常数；共同右 collar 已准确确定它们。

将 (2) 代入 (1)，$p^2r^2$、$xpr^3$、$xr^2A$、$x^2r^4$ 的系数逐对相消，剩下

$$
8192F_{hh,-6}=\frac43pB-A^2-\frac13xC.
$$

所以得到完整函数身份

$$
\boxed{
F_{hh,-6}(q)
=\frac{4q'I((q'')^3)-3I((q'')^2)^2-xI((q'')^4)}{24576}.
}                                                               \tag{3}
$$

若改写为正尾 $J=-I$，同一式是

$$
F_{hh,-6}(q)
=\frac{xJ((q'')^4)-4q'J((q'')^3)-3J((q'')^2)^2}{24576}.
\tag{4}
$$

式 (3)、(4) 只含 q 的二阶 jets 与同锚原函数。它们是任意光滑右 collar 零输入的原式身份，不依赖 pure 幂尾、固定 profile、常状态几何或模响应取商。

## 3. 这个原系数确非零，但尚未判断响应成员

由同锚 shuffle 身份

$$
A^2=2I(r^2 I(r^2)),
$$

式 (3) 的三类词是

$$
q'I((q'')^3),\qquad I((q'')^2I((q'')^2)),\qquad xI((q'')^4).
$$

它们的外局部因子、词长或词字母不同；每个字母 $(q'')^j$ 的最高 jet 重数至少为二，已属 [R178](../results/R178-fixed-color-priority-IBP-and-terminating-shared-word-map.md) 的余语法。由 [R179](../results/R179-universal-independence-of-fixed-color-remainder-words.md) 的真实单色特例，这些余词没有非平凡 universal 函数关系。尤其双词的系数 $-6/24576$ 非零，故

$$
F_{hh,-6}\not\equiv0.
$$

这里的非零是对所有合法测试输入而言的 universal 算子非零，不表示每一个指定 q 上处处非零。

本稿**不**断言该根在 $\pi R_{-6}$ 之外，也不将其当作新的有符号可达成本。它是否属于真实 pure 响应像，由独立的权 −6 完整消费者处理；本稿不重复该消元。

## 4. 范围

已付的是一个完整加速度原系数中全部 $q'''$ 的准确消去，以及所得二阶-jet 算子的非零性。这个系数本身已保真实几何正规化来源。

没有由此推广到其他加速度系数、完整动态 $v_2/v_4$、局部势 $N_0/N_2$、整个 pure 成本，或证明所有 pure 高 jet 都可模 $R$ 消去。特别，别处若出现重复最高 jet 的原函数，例如 $I((q''')^2F)$，不能仅凭“再作分部积分”便把它删除；其真实系数抵消或响应成员仍需要原式证明。
