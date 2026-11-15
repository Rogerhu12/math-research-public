# 九条原式关系之后，指定全层正外点的公开准确核对

**状态：指定点的公开消费已完整通过。它满足原 86 条必要半空间、九条新增真等式，并准确得到 R177 的完整十四族、同一乘子和全层正证。真实原函数泛函是否良定义仍未证明。**

本记录落实 [R177](../results/R177-explicit-all-layer-positive-point-after-nine-original-relations.md) 的有限接口核对，不重新证明其平方恒等式，也不运行新的 LP 或路径测试。此前 R176 保存的不同外点已有负路径；本次直接评价 R177 给出的新完整有理点，没有在两点之间拟合或搜索。

## 1. 运行、输入与输出身份

实际 run 为 `43672582314`，source 为
`14f33da3731f543bdafeee98f5f83ec5390f0b5e`，lane 为
`character_minus2_raw_positive_candidate`。

| 输出 | 字节数 | SHA256 |
|---|---:|---|
| [主报告](../notes/actions-43672582314-1-character_minus2_raw_positive_candidate/character-minus2-raw-positive-candidate.json) | 7063 | `25b16d6cd538bb7affbc2d532ef1f1a688546f1f4777b355a632af8a0e421067` |
| [完整证书](../notes/actions-43672582314-1-character_minus2_raw_positive_candidate/character-minus2-raw-positive-candidate-certificate.json.gz) | 12864 | `b7b7cf0fc4bf476c918f9302462e3dc2071b5bff799bdf6131e8b6d7c22e2778` |
| 完整证书原文 | 60197 | `e37ce83e392bdc743614451126cbb64c7444788fd6ae253ead154d3d1a8f7d26` |
| [新人工回执](../notes/actions-43672582314-1-character_minus2_raw_positive_candidate/character-minus2-raw-positive-candidate-development.json) | 3085 | `e04f98caa6547ae31880febd4eace171f48d37e72a29acd532090e0d49ef6b8d` |
| [发布回执](../notes/actions-43672582314-1-character_minus2_raw_positive_candidate/receipt.json) | 41821 | `61712e89f0f14b1ad6f4dab3a5423b3c3a925d30e8ad628d62fe42af3421d655` |

冻结消费者 `literature_character_minus2_raw_positive_candidate.py` 为
29045 字节 / SHA256
`415e1b67f5c52ac60bf4b0fc152e1cf1c21f05b327536920517c46cc1a397d09`。
实际耗时 `0.009609177999998053` 秒，峰值 RSS `25.20703125 MiB`，
`completion=complete`。此前同 job 的八项新人工接口检查全部通过；
人工没有评价该研究点或重跑旧人工套件。

输入只有两套已经发表的完整数据：run `43671759155` 的 raw9 主报告、发布回执、86 行证书，以及 run `43665971895` 的原完整 107 坐标/十四族证书。源码核 packed/raw 字节身份、生产者来源、旧 B 与十四族/乘子形式 SHA，以及同一旧行前缀。没有读取或重新生成原 profile 表达式。

## 2. 原 23 坐标、全部 107 值与 86 行

本次固定评价

$$
\begin{aligned}
y_*={}&(1/4,0,-1,1,0,1/4,0,-1,1,1,0,1,-1/4,\\
&\qquad1,1/4,-1/4,1/16,1/12,-1/8,0,-1/12,1,1/4).
\end{aligned}
\tag{1}
$$

它仍使用原 free normal 下标

$$
(2,3,14,23,26,28,38,43,58,63,67,69,73,
90,91,94,96,97,99,100,101,103,104).
$$

实际由原 B 评价并保存全部 107 个生成坐标；同一组生成值再给十四族和乘子，未为任何层另选参数。

86 个必要行值全部非负，负行列表为空。准确零行恰为原编号

$$
64,65,\ldots,85.
\tag{2}
$$

其中原 64–67 行来自此前奇偶等式，68–85 为九条新等式的正负两行。其余 64 条行在此点严格正。九个原 relation 索引

$$
0,4,35,55,62,64,65,66,67
$$

在 (1) 上的准确值全部为零。原表、次序、provenance 和已发表的两 mode 原零证书保持不变；本次只评价它们的线性赋值，没有重做原式消元。

这不是求解器返回的浮点可行性结论。本次没有调用 LP，所有行值、坐标和系数比较都用准确有理数完成并存入完整证书。

## 3. 全十四族与同一八矩乘子全部匹配

实际准确得到以下完整多项式。原存储中的静态六次项、二次层错误奇偶位置和 $Q_{4,2}$ 常数项也被遍历并确认为零；没有按预期丢掉额外项。

| 族 | 准确值 |
|---|---|
| 静态 $a_{\rm static}(k)$ | $(1+k^2)^2/4$ |
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

所有十四项的完整系数比较均为 true。按原八矩顺序
$(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)$，同样从原形式得到

$$
\mu=(0,1/2,2,0,0,0,0,2),\quad c=0,\quad
d=(0,1,6,0,0,0,0,4).
\tag{3}
$$

最高层五条原关系残差全部为零，R175 的矩阵准确为

$$
M=\begin{pmatrix}1/16&0\\0&11/48\end{pmatrix},
\qquad\det M=11/768.
\tag{4}
$$

纯 h 两项为 $a=1$、$\ell+25a/9=34/9$。因此本次同一完整点确实满足 R177 纸面证明的全部系数前提。

## 4. 此实际核对支持的全路径标量结论

令 $r=\log h$、$v=r'$、$\psi=hD_s(k/h^2)$。R177 的已证身份在刚核对的同一点上给出

$$
L_0=\frac14h^{-2}(1+k^2)^2,
$$

$$
L_2=h^{-2}\left\{(k')^2+(1+k^2)v^2+
\frac{k^2}{4}(k'-2kv)^2\right\},
$$

以及保全部边界项后的平端积分

$$
\int L_4=
\int\left\{h^{-2}\left[\left(v'-\frac23v^2\right)^2+
\frac{34}{9}v^4\right]+\frac1{16}(\psi')^2+
\frac{11}{48}v^2\psi^2\right\}ds.
$$

所以对每条正时长、正 h 的真实平端路径，同一标量 action 满足

$$
\boxed{\mathcal A[h,k]\ge\frac14\int h^{-2}\,ds>0.}
\tag{5}
$$

这里真实角变量仍按 $\omega'=k'/(2h)$ 恢复，所有 H 面积项都已包含在 R175/R177 的完整恒等式中。当前实际只核同一存储系数，不重新积分这些路径，也未做新的 Gram 搜索。

因此继续添加由这个完整标量 action 导出的路径必要门不会排除 (1)。真正剩下的问题是它能否对全部真实原函数关系保持一致。

## 5. 已付 70 条关系与未付的完整函数核

[R174](../results/R174-nine-original-character-relations-and-rejection-of-the-positive-outer-point.md) 的完整生成记录表明，旧 B、此前奇偶关系和新增九行覆盖已经获得的全部 70 条字面原式关系。结合本次九式为零，(1) 尊重这些已发表关系；无需再重算其原两 mode 表达式。

本次主报告保留了早期命名字段
`checkpoint.original_function_relations_beyond_the_published_nine_unpaid=true`。
该名称不够精确，本记录明确限定其解读：**尚未证明已发表原关系穷尽全部真实函数核**；不能把它理解为已经支付的 70 条中还有其余 61 条未付。旧结果保持原字节，不因这个标签重跑或覆盖实际。

报告同时准确保留
`complete_functional_relations_paid=false` 与
`true_positive_character_constructed=false`。
字面 rank、非零 word 余式或有限必要表都没有被当作真实函数核的完整性证明。

本次得到的是一个通过已付关系与完整标量正性门的明确有理外点。它没有证明真实正字符存在，没有排除全部权 −2 正字符，更没有支付完整几何、四阶周期、ruling、收敛或主课题。后继应消费同一完整候选进行有根据的原函数关系检查，不重复本次点代入或已经完成的全路径正证。
