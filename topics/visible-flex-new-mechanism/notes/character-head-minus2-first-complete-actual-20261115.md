# 真权 −2 的十四族与字符头部：首次完整原式呈示

日期：2026-11-15。状态：**公开 GitHub Actions 已完成全部必要原式生成；字符头部的真实维数、正性及完整 period 尚未判定。**

本次只取 profile 的真仿射权 $-2$。依据 [R163](../results/R163-complete-normal-coefficient-cocycle-and-single-weight-character-head.md)，它保存完整十四族的 **107 条两模式原系数记录**、平移分母的 **66 条有理组合记录**、同一八矩规范化及其两组参考导数。107 和 66 都是呈示记录数，不能读成函数空间或字符空间的维数。

全部 78 个必要不同收缩已完成，其中两条直接复用已经发表的轴向原收缩，新增 76 条。完整导出已经发表，后继直接消费；不再重跑本次原式生成，也不启动缓存续算。下一步是完整字符的必要条件与可核线性关系，不把原式归档本身当成本课题完成。

## 1. 公开来源及实际完成范围

实际运行：[43665345551](https://github.com/Rogerhu12/math-research-public/actions/runs/43665345551)，lane `character_head_minus2`，源提交 `0aae9a6a85583a9f87415e586d8db2c9c7fea6a7`。研究 driver 为 [literature_character_head_minus2.py](../scripts/literature_character_head_minus2.py)，58,856 字节，SHA256：

```text
fcc41b4d5a640a1ac411e7f6f29622db81c39cb2be37aed7811136418a045f11
```

主报告 [character-head-minus2.json](actions-43665345551-1-character_head_minus2/character-head-minus2.json) 的 `completion=complete`、`head_generation_complete=true`。完整导出的 `all_fourteen_families_complete=true`、`completed_contractions=planned_contractions=78`。研究耗时 **33.326963494 秒**，峰值 RSS **330.09375 MiB**；预算为 240 秒和 1024 MiB。

同 job 先运行的 [development](actions-43665345551-1-character_head_minus2/character-head-minus2-development.json) 中，13 项小人工检查全部通过，耗时 0.008379884 秒，RSS 29.6640625 MiB。人工检查只覆盖新增接口和代数装配，未读取研究目标；其通过不能替代本节独立的实际完成回执。

本次没有重新编译旧 forcing、36 个 W 模板、旧响应基，没有重新评价旧枢轴或新采样 profile/几何路径，没有新建相邻权 $-1$ 的目标，也没有进行函数空间秩或正性求解。全过程保留同一右锚和完整相位模式 $-4,-2$。

## 2. 唯一新计算范围与已发原式的复用

所有输入同时核对小主报告、publication receipt、原导出的压缩/解压字节数与 SHA256、生产者源提交、run、driver 以及每条原根的摘要。输入不是先前 normal-form 的标签；它们都是可重新读取的完整原式。

| 已发输入 | 本次实际使用的范围 | 原 Actions run |
|---|---|---:|
| 完整静态密度 | 两模式各 197 条 $L_0$ 原系数，取真权 −2；旧主报告虽因摘要大小记为 `output_limit`，完整静态导出已成功 | 43645177423 |
| 完整导数因子 | 未降模 W 的 $N^{[0]}$ 共 79 条、$N^{[2]}$ 共 93 条；完整 $v_2$ 及 $v_4$ 中尚需装配的第三导数、速度二次乘加速度、速度四次块 | 43651096112 |
| 五个最高加速度族 | 已经完成的三个 $\bar A$、两个 H 的真权 −2 原根 | 43654534244 |
| 真权 −2 响应空间 | [R131](../results/R131-third-G-translation-separation-and-111-query-control.md) 已证明独立的 40 个完整两模式原响应；只读取，不重算 | 43653293263 |
| 两个轴向收缩 | $\mathcal B_{r_1}(N^{[2]}_{h^{-2}u^2})$、$\mathcal B_{t_1}(N^{[2]}_{h^{-4}u^2})$ 的已发完整原式 | 43657526246 |

这里“真权”始终指 profile 仿射缩放权，不能与几何导数权 $0,2,4$ 混同。矩阵方向顺序为

$$
(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1),
$$

其真权为 $(-1,0,1,-3,-2,-2,-1,0)$。为得到输出权 $-2$，各方向只需要第三势的真权

$$
(-1,-2,-3,1,0,0,-1,-2).
$$

$N^{[2]}$ 需要八方向；$N^{[0]}$ 只需 $r_0,r_1,s_0,s_1,t_1$，因为原矩阵 $m_2$ 的三个 p 坐标为零。相同投影原根与方向的缓存由 $L_2$、$L_4$ 共用。

筛选前共有 $93\cdot8+79\cdot5=1139$ 个类型化请求。准确投影后，1057 个请求是空原式；余下 82 次使用按“方向与投影原根 SHA”合并为 78 个不同非零输入。两条已发轴向收缩与未降模势的输入原 hash 精确一致，直接充入缓存，故只新增 **76** 个完整两模式响应。没有按未知函数依赖、比例猜测或 normal-form 相同来删减请求。

原输入身份摘要为

```text
dad5e1e350887589d61d7ad8040405f60533e61d8f691cee9bd0cd4d2dcafa57
```

完整必要收缩计划摘要为

```text
5de54deede711d7bab3ce1640fede6ae6e448fc27cddf17048a3acac2c465b67
```

输入原势与响应的关系未作任意赋值；缓存中缺失的必要收缩会使装配失败，而不会被当作零。本次全部计划条目均完成。

## 3. 正规化保留了哪些原成本

使用 [R129](../results/R129-horizontal-geometry-IBP-for-complete-fourth-costs.md) 的真实水平微分

$$
X=\partial_h,\qquad Y=\partial_k+\frac1{2h}\partial_\omega,
\qquad [X,Y]= -\frac1{2h^2}\partial_\omega,
$$

并逐项保留 Laurent 及 $\log h$ 的链式导数。写 $u=h_s,w=k_s$，$D_0=uX+wY$，其作用时将 u、w 当作此步的形式速度变量；第三导数项、加速度项的消除使用完整 R129 正规化。

设原 $v_2=p\,h_{ss}+q\,k_{ss}+q_{20}u^2+q_{11}uw+q_{02}w^2$。本次低阶正规系数准确来自

$$
\begin{aligned}
\widehat Q_2={}&(q_{20}-Xp)u^2
+(q_{11}-Yp-Xq)uw+(q_{02}-Yq)w^2\\
&-\mathcal B_{m_0}N^{[2]}-\mathcal B_{m_2}N^{[0]}-\Gamma(m_2).
\end{aligned}
$$

最高速度四次部分准确来自

$$
\widehat Q_4=Q_4^v-\frac13D_0(uC_h+wC_k)
+\frac13D_0^2(uB_h+wB_k)-\mathcal B_{m_2}N^{[2]}.
$$

这里 $B_h,B_k$ 是原第三导数项的速度线性系数，$C_h,C_k$ 是原加速度项的速度二次系数；$uB_h+wB_k$ 是二次速度式，$uC_h+wC_k$ 是三次速度式。顺序微分 $D_0^2$ 未将 X、Y 误设为可交换。五个 $\bar A/H$ 族直接消费既有完整原式，不重复其生成。

静态和二次层使用同一组八参考状态

$$
S_i^*=(1,k,d+k),\qquad d\in(0,1,-1,2),\quad k\in(0,1),
$$

同一矩阵坐标 $a_i$，以及同一

$$
\Gamma(M)=\sum_i a_i(M)L_0(S_i^*),\qquad
F_0=L_0-\Gamma(m_0).
$$

八个 $F_0(S_i^*)$ 均以完整原表达式核得零。旧静态密度使用的势代表曾降模 W，而导数因子保存未降模势；二者的代表差只贡献点态 R 响应，合法性由 R109/R163 支付。本次既没有将未降模 $N^{[0]}$ 说成已降模代表，也没有在二次层漏掉同一个 $\Gamma(m_2)$。

完整十四族依 [R130](../results/R130-true-fourth-span-from-horizontal-normal-coefficients.md) 和 R163 生成实际 $U/R$；端势在规定平端路径上消失。由此可用本次呈示研究真实成本商，而非把任意几何 monomial 系数当作独立可达成本。本文不另外宣称这些记录已有独立性或符号控制。

## 4. 十四族的实际记录数及两条原式零结论

每条记录包含一个状态键 $(h,k,\omega,\log h)$ 的幂指数，以及同一完整 profile 算子的两个 canonical 原模式。至少一个模式的原表达式非空时保留一条记录；同一记录的两个模式不能各自算成独立方向。

| 族 | 速度约定 | 非空原系数记录数 | 平移组合记录数 |
|---|---|---:|---:|
| $F_0$ | 静态 | 20 | 19 |
| $Q2_0$ | $w^2$ | 12 | 6 |
| $Q2_1$ | $uw$ | 26 | 14 |
| $Q2_2$ | $u^2$ | 32 | 20 |
| $\bar A_{hh}$ | $h_{ss}^2$ | 4 | 2 |
| $\bar A_{hk}$ | $h_{ss}k_{ss}$ | 2 | 1 |
| $\bar A_{kk}$ | $k_{ss}^2$ | 1 | 0 |
| $H_1$ | $u(uk_{ss}-wh_{ss})$ | 2 | 1 |
| $H_2$ | $w(uk_{ss}-wh_{ss})$ | 1 | 0 |
| $Q4_0$ | $w^4$ | 0 | 0 |
| $Q4_1$ | $uw^3$ | 0 | 0 |
| $Q4_2$ | $u^2w^2$ | 1 | 0 |
| $Q4_3$ | $u^3w$ | 2 | 1 |
| $Q4_4$ | $u^4$ | 4 | 2 |
| **合计** | 完整十四族 | **107** | **66** |

因此，在本次真权 $-2$、同右锚、完整两模式正规化下，确实有

$$
\boxed{\Pi_{-2}Q4_0=0,\qquad \Pi_{-2}Q4_1=0.}
$$

这是全部必要收缩和完整正规化都已加入后的原表达式零，既不是未完成条目的空值，也不是仅某个 profile、幂尾或混合投影上的零。其范围只限这个真权与这两个正规系数，不能外推其他权的全 $\widehat Q_4$、完整第四成本或 period 为零。后继字符测试可直接保留该原式零事实，不必重新评价。

## 5. 完整字符头部如何由这些记录给出

令 $V_0,\ldots,V_{106}$ 为 `normal_family_records` 中按 index 保存的真实两模式原算子。令

$$
T_{-2}=\operatorname{span}_{\mathbb R}\{V_j:0\le j<107\}.
$$

每条 `head_translation_presentation` 保存一个明确有理向量 $b_{\ell j}$，给出

$$
D_\ell=\sum_{j=0}^{106}b_{\ell j}V_j,\qquad
D_{-2}=\operatorname{span}_{\mathbb R}\{D_\ell:0\le\ell<66\}.
$$

这些不是凭空新增的独立变量，而是同一原系数表的线性组合。低阶两层使用

$$
\partial_\omega F_0-c_{-2}(m_0),\qquad
\partial_\omega\widehat Q_2-c_{-2}(m_2),
\qquad
c_{-2}(M)=\sum_i a_i(M)\partial_\omega\Pi_{-2}F_0(S_i^*).
$$

最高十族使用相应的 $\partial_\omega$。尤其没有把低层平移像简写成单独的 $\partial_\omega$。

据 R163 的已证明等式，本次完整呈示满足

$$
\boxed{
U_{-2}=R_{-2}+T_{-2},\qquad
R_{-2}+\mathsf N U_{-1}=R_{-2}+D_{-2}.
}
$$

从而真实权 $-2$ 字符头部为

$$
\boxed{
H_{-2}=\frac{U_{-2}}{R_{-2}+\mathsf N U_{-1}}
\simeq \frac{R_{-2}+T_{-2}}{R_{-2}+D_{-2}}.
}
$$

这里的 $R_{-2}$ 为 R131 已发真维数 40 的完整响应空间，本次同时保存其 40 个独立原代表。没有重新编译或评价这个旧基。关系的真正秩、$T_{-2}$ 与 $R_{-2}$ 的交，以及 66 条组合之间的依赖均尚未求出；尤其不能把 $107-66$ 当作头部维数。

## 6. 后继字符必要系统的准确接口

主报告 schema：`visible-flex-complete-character-head-minus2-v1`。原导出 schema：`visible-flex-complete-character-head-minus2-v1-original-expressions`。完整 scope：

```text
complete-fourteen-weight-minus2-families-and-translation-presentation
```

下一 consumer 必须核定该 scope 和 `all_fourteen_families_complete=true`，并完整绑定本次 run/source/driver 与字节摘要。原导出共 **544 个根、2332 个 profile atoms**，含以下必需对象：

- `normal_family_records`：107 个真实 U 原系数，附家族、状态键、真权、两模式根名和各自原 hash。
- `head_translation_presentation`：66 个分母生成向量，只引用上述 index。
- `archived_R_basis_records`：40 个旧响应的完整原根和原列标签。
- `static_translation_reference_coefficients`、`static_scaling_reference_coefficients`：分别为八参考态的 $\partial_\omega F_0$ 和 $(h\partial_h-\omega\partial_\omega)F_0$ 的有理组合；log 导数在置 $h=1$ 之前已保留。
- `reference_matrix.inverse` 和 `eight_reference_coordinate_polynomials`：将上述参考态序号转换成 R73 的八矩方向坐标，并保留 $m_0,m_2$ 两层的准确 $a_i$。
- `cache_records`：全部 78 个完成收缩的投影输入原根、方向和完整两模式输出；每条标明新增或已发表轴缓存来源。

两组参考导数列表的索引是参考态 i，**不是**八矩方向 j。依 [R164](../results/R164-covariant-eight-matrix-multiplier-for-positive-affine-characters.md)，应先乘参考矩阵逆的 `inverse[i][j]`，才得到同一 $c_j,d_j$ 并确定唯一规范化乘子。保存的 `static_reference_i_mode_*` 则是原 $L_0(S_i^*)$，不是 $F_0$；它们仅用于装配 $\Gamma$，不能在只定义于 U 的字符坐标中额外设为独立变量。

完整 necessary-system consumer 可以对所有真实字符建立一个更大的有理坐标外部候选空间，只加入已证明的原零、原比例、平移和协变关系。若其有限必要系统有完整精确不可行证书，便可排除这个真权的非零正字符；若仍可行，只得到尚需实际函数关系及全部路径正性检查的候选。R159 的一般原恒等仍须保留 pure 与 balanced 两根；不能因若干已知新方向的 pure 可消就假定整个十四族都在同一个 pure 响应像内。

R164 的同一乘子、三个时长层和全路径条件均继续有效。八参考态导致的额外乘子消元是既有规范化的纸面推论，可直接用于后继必要系统，不要求重算本次导出。当前 J6 是否落入 $R_{-2}+\mathsf N U_{-1}$ 也仍是一个具体的头部简化目标；本次没有回答它。

## 7. 文件及可核摘要

全部文件位于 [actions-43665345551-1-character_head_minus2](actions-43665345551-1-character_head_minus2/)。[receipt.json](actions-43665345551-1-character_head_minus2/receipt.json) 将源、输出摘要及实际 pull/README 检查绑定在同一次公开发布。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `character-head-minus2.json` | 15,967 | `55320985df05f928caf007016777ecb2413f16c969dca4741b0c2e936f00b940` |
| `receipt.json` | 39,451 | `88bdcf2dadbba25d816e886705b70e7844f698f07917b696698e86ea2770f675` |
| `character-head-minus2-development.json` | 8,283 | `ba42063dbbafab7c76d0599057c927ee4c7b82c815014c0746c9539caed3cc35` |
| `character-head-minus2-complete-report.json.gz` | 4,919 | `38ad7dde1f69c50d34c5ca784e1c43111c509bd0a01478d6615b7195c0492e46` |
| `character-head-minus2-original-expressions.json.gz` | 1,247,411 | `2c1242e13d253ba352c7ff1b025a91cf564ab2a7cfd93c6bcedc19baa5fac45c` |

完整主报告解压后 15,681 字节，SHA256 `c69aa9915011ba8271bbcf74a99dc53772b745af58c5223147b7b46c9bef07ca`。完整原式导出解压后 6,560,138 字节，SHA256 `7a93a53aa7fafa1cff76608aceaeac294911ca4f828746913c1b125ae2fd33af`。

主报告明确保留 `function_space_rank_computed=false`、`positive_character_decided=false`、`period_or_ruling_paid=false` 和 `task_complete=false`。本次成功支付的是完整真权 −2 原呈示所缺的数据门；后继继续在这份数据上作实际字符必要条件与原式关系判断。
