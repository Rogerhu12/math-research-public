# R125：完整响应至少 48 维与真实第四成本至少 49 维

日期：2026-11-14。**已证明。** 本稿只把三个已经完成的公开原式证书放到同一个真实线性空间中，使用秩—零化度定理；没有新的研究编译、profile 评价或数值优化。

结论是

$$
\boxed{
\dim\mathcal R_8\ge48,\qquad
\dim\mathcal U_4\ge49.
}
\tag{1}
$$

[R121](R121-central-baseline-correction-and-joint-fourth-query-control.md) 因而至少给出 **49 个可以在同一个合法光滑三矩圆上联合支付的独立实查询**。这仍不是完整函数成本、ruling 或有限等距族的完成结论。

## 1. 同一个完整真实响应空间

继续记

$$
R=\mathcal R_8
=\operatorname{span}_{\mathbb R}
\{\mathcal B_P(T):P\in E_8,\ T\in W_{36}\}.
$$

所有列都指同一 canonical 目标、同一右锚和完整 $-4,-2$ 两相位输出，不把 pure 模式和完整模式混为一谈。$R$ 是真实函数空间；word 代表仅用于已经被原式复核的关系，不承担独立性假设。

真实缩放使

$$
R=\bigoplus_wR_w.
\tag{2}
$$

本文只组合三个准确事实：

1. R116 给完整 $m=8$ pure 尾投影的像维数 $31$；
2. R98 给 $R_0$ 内一个真实 $14$ 维子空间；
3. R118 给 $\dim R_1=7$。

它们虽然使用不同的测试输入或输出投影，但都在同一空间 $R$ 上证明性质，故可以通过核与像结合；不是把不同测试矩阵的秩直接相加。

## 2. pure 尾确为真实函数空间上的线性映射

按 [R116](R116-full-m8-tail-response-rank-and-finite-query-control.md)，定义

$$
q_c(\xi)=(c-\xi)^8,\qquad r=c-\xi,\qquad
\Pi(V)(c,r)=V_{-4}[q_c](c-r).
\tag{3}
$$

右端以 $r^8$ 接零，查询点左侧可在不改变任何右因果查询的地方作光滑截断。完整 R8 响应至多需要六阶输入 jet；这个紧支撑尾是 $C^7$，并可由共同右 collar 的 $C^\infty$ 输入在 $C^6$ 中逼近。有限乘积和固定紧区间的右 Volterra 原函数对该收敛连续。

所以，如果两个原表达式代表同一个完整真实算子，它们在 (3) 上也相同。$\Pi$ 因而是定义在真实函数商 $R$ 上的线性映射，而不是仅定义在一个任意 formal 表达式空间的取值规则。

R116 全部 288 列的完整有理多项式及每条丢列关系已经准确保存。其分权投影秩为：

| 权 $w$ | $-8$ | $-7$ | $-6$ | $-5$ | $-4$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $\dim\Pi(R_w)$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 6 | 3 | 1 | 0 |

不同权的输出总次数是 $32+w$，所以像的和也是直和，准确有

$$
\boxed{
\operatorname{rank}\Pi=31,\qquad
\operatorname{rank}(\Pi|_{R_0})=3,\qquad
\operatorname{rank}(\Pi|_{R_1})=1.
}
\tag{4}
$$

特别，**权零的秩是 3，权一的秩是 1**。不能把这两个数错位，也不能把像维数当成完整 $R_w$ 的维数。

## 3. R98 的 14 维空间确实包含在当前 R0 中

[R98](R98-weight-zero-separation-of-all-positive-state-P1.md) 使用物理七维二阶空间

$$
E_{\rm phys}
=\operatorname{span}\{r_0,r_1,s_0,p_0,s_1,p_1-t_1/4,p_2\}
\subset E_8.
\tag{5}
$$

它的权零响应有 16 个原列，两条原式关系给准确上界 14。原有理 Volterra 评价又给控制 $14\times14$ 子式

$$
\det A_{14}\equiv1836229422\ne0
\pmod{2147483647}.
\tag{6}
$$

相应分母都通过该实际 evaluator 的非零检查。故这些 14 个完整两模式列在特征零、实系数意义下独立。记其张成为 $V_0$，则

$$
V_0\subseteq R_0,\qquad \dim V_0=14.
\tag{7}
$$

这一步的接口对齐不是仅看同名符号。R98 的 producer 是
[literature_total_P1_scaling_blocks.py](../scripts/literature_total_P1_scaling_blocks.py)，
SHA256：

40ff170136838907ecb4d2557c2ba3b4d06b5f3fcf63746697f3d5248e92d0fa。

这正是 R118 和当前完整 R8 consumer 调用的同一个 blocks.full_response。它接受任意二阶 $P$，输出同一个 R78 完整两模式式；(5) 的每个算子都是当前八维基的准确实线性组合。三阶原模板、共同右锚与外槽/内槽约定也都由相同来源绑定。没有将旧 pure 对角或不同幅度规范的响应移入当前空间。

由 (4)、(7)，

$$
\dim\ker(\Pi|_{V_0})
=14-\operatorname{rank}(\Pi|_{V_0})
\ge14-3=11.
\tag{8}
$$

不需要进一步计算 $\Pi(V_0)$ 是否恰为整个三维 $\Pi(R_0)$；上界 3 已经足够。

## 4. 权一另外给六个独立的不可见方向

[R118](R118-static-G-exact-separation-and-nonzero-fourth-cost-quotient.md) 使用完整八维 $E_8$ 的权一八列，先消费原式关系

$$
C_6=-C_1+C_3,
$$

再给七个保留原列的准确控制子式

$$
\det A_7\equiv1896063777\ne0
\pmod{2147483647}.
$$

所以完整真实权一空间恰为七维。结合 (4)，

$$
\boxed{\dim\ker(\Pi|_{R_1})=7-1=6.}
\tag{9}
$$

(8) 的核向量属于权零，(9) 的核向量属于权一。真实整权直和 (2) 说明它们的交只有零；不能因使用同一个 pure 投影就把这些核方向视为重复。

故

$$
\dim\ker\Pi\ge11+6=17.
\tag{10}
$$

现在才对同一个真实线性映射使用秩—零化度：

$$
\boxed{
\dim R=\operatorname{rank}\Pi+\dim\ker\Pi
\ge31+17=48.
}
\tag{11}
$$

这里没有从一个低秩投影推出更多算子关系；恰恰相反，两个完整独立性证书证明了该投影至少遗漏 17 个真实方向。

## 5. 成本、闭锥与查询的严格推论

R118 已证 $G\in\mathcal U_4\setminus R$。因此

$$
\dim\mathcal U_4\ge\dim R+1\ge49.
\tag{12}
$$

R120 的适用范围内还有

$$
R+\mathbb RG\subseteq\operatorname{lin}\mathcal C,
$$

所以 unrestricted universal 真成本闭凸锥的 lineality 至少 49 维。这里继续保闭锥与实际有限成本集合的区别；不把 lineality 本身当成实际成本逆元。

实际有限路径的联合支付来自另一个完整构造：R121 已给 $r+1$ 个独立查询的真实联合满射，其中 $r=\dim R$。用 (11) 可保守选择其中 49 个，令其他已选坐标目标固定，即得同一个合法 $C^\infty$ 三矩圆、共同物理区间上 49 个独立实查询的任意指定值。R121 的真实基准清除、乘积盒及整数重复次数仍全部保留；不是只凭维数得出可达性。

R122 更一般地给 $r+s$ 个查询，$s=\dim((R+\operatorname{span}\operatorname{Orb}G)/R)\ge1$；本稿未确定 $s$，没有提前给出第二个新的 G 轨道方向。

这 49 个查询可以是有限点/模式查询的固定实线性组合。本文没有列出一个新的数值 profile 或新的 49 行节点表，也没有称整个 $\mathcal U_4$ 已由这 49 个查询忠实覆盖。

## 6. 公开证据的完整定位

本稿读取的是已经发布的小文本回执，不读取大型二进制导出，也不重新执行旧评价。

| 证据 | 运行与文件 | SHA256 |
|---|---|---|
| 权零完整控制 14 维 | [run 43638896281 的权零原回执](../notes/actions-43638896281-1-total_P1_blocks/total-P1-blocks-weight-p0.json) | 1146e6789d2f842ecc255930e2394bec5073029b13dcff4cc6f1aa445d07a78d |
| 完整 pure 尾像 31，权零像 3、权一像 1 | [run 43646543691 主报告](../notes/actions-43646543691-1-full_m8_tail_response_projection/full-m8-tail-response.json) | 7237cadaac3c4581862d8aee86b94692f0e2436ab7fdb7e393c7b721125d61a7 |
| 权一完整控制 7 维与 G 非成员 | [run 43647225907 主报告](../notes/actions-43647225907-1-static_g_rational_dual/static-G-rational-dual.json) | 743594e95eedda896410cc20a30949675899e075bacc262fa5192388dbeba7f9 |

旧 R98 的其他更强横向结论没有用于这个下界；尤其没有把两个在同一个泛函上非零的新列自动称为两个独立方向。后续若有更多准确完整块秩，可在同一个投影映射下继续改善下界，但本稿不预先计入。

完整第四函数匹配、ruling、更高阶、嵌入、reach 和宏观位移仍未由 (1) 自动支付。
