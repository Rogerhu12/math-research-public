# 外部 0–11 胞元：真实正权积分与连续候选输入

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

## 1. 范围与已有输入

[R48](../results/R48-weighted-compatible-outer-interpolation.md) 给出了使用五个真实正权积分的兼容高度插值；[R44](../results/R44-compatible-outer-height-and-continuous-defect.md) 从同一个高度计算完整 mean 和全频连续 Darboux 缺陷。新的 [tail_outer_positive_moment_panels.py](../computations/tail_outer_positive_moment_panels.py) 补齐两者之间的背景积分接口。

它以已完成的 [真实外半径账本](2026-11-12-root-real-outer-radius-v4-recovered-full.json) 为锚点，保留 0–11 的全部冻结 valley 控制、slope-cap 分支、cut-preserving blend、正 warp 权、原 `oldCut` 和已冻结的 warp alpha。它不把真实外半径改成名义 binary 0.3，不重新校准，也不引入新度规。

**当前状态：cell 11 的真实积分已执行，并经完整无损分包正式恢复。** 本文给出完整区间包围原理；实际执行、5,545 个面板和全部 17 个父积分约束见[正式记录](2026-11-12-tail-outer-cell11-positive-moment-execution.md)。其它外部胞元尚未执行这项算法。原 13port 只证明那些端点附近明确有限候选的角向范围；它们仍不能代替整胞元径向证书。

## 2. 单一真实坐标与五个正积分

在一个外部胞元，九个原始源段的长度为 $\ell_0,\ldots,\ell_8>0$。在第 $j$ 段的原参数 $x\in[0,1]$ 定义

$$
u=\frac{\sum_{i<j}\ell_i+\ell_jx}{\sum_{i=0}^8\ell_i},
\qquad u_x=\frac{\ell_j}{\sum_i\ell_i}>0.
$$

这个坐标必须保留九段不相等的真实长度，不能换成 $(j+x)/9$。其最内、最外端分别严格为 0 和 1；程序对这两个代数恒等端点直接使用准确值，避免把同一总长度区间相除造成伪宽度。

R48 的五个非负基函数为

$$
q_{00}=(1-u)^2(1+2u),\quad q_{10}=u(1-u)^2,
\quad q_{01}=u^2(3-2u),\quad -q_{11}=u^2(1-u),
\quad b=u^2(1-u)^2.
$$

在 $[0,1]$ 上，其统一上界分别为 $1,4/27,1,4/27,1/16$。五个需要包围的准确积分是

$$
I_q=\int_0^1r_u(u)w(u)q(u)\,du
=\int_{r_-}^{r_+}w(u(r))q(u(r))\,dr.
\tag{O1}
$$

因为 $r_u,w>0$，且各基函数在开区间正，全部总积分严格为正。区间算法仍必须得到严格正的下端才允许使用 $I_b$ 作除数；“数学上应当正”不替代数值包围。

## 3. 真实源值域，包括未决分支

`closure_real_outer_radius.py` 的原公式在每个源段提供 $\log w$、$(\log w)_x$、$r_x$。新程序锁定该源文件与 `closure_real_head_source_enclosure.py` 的 SHA，并锁定同一 ready 及全部 R26 父面板。

若 R26 已在父面板证明 cap 分支和导数符号，子面板继承该已付结论。若原父面板横跨分支边界，程序保留所有可能的 raw/cap/transition 分支，并对各表达式的值域取并；它不强行选择一个采样值附近的分支。两个 transition 公式是同一个实际 smooth-cap 函数的端点表达式，在各自真实分支上准确。

值域过宽时只按真实 source $x$ 做 dyadic 细分。细分判据包括 $\log w$ 值域宽度、单一 $u$ 值域宽度以及所需严格正下端。达到显式细分深度或面板预算而仍未解决时，程序退出失败，不把未付的范围写成成功证书。

### 3.1. 极小 $w$ 下仍严格正的 $r_x$ 下界

普通外段满足

$$
r_x=\frac{w|\ell_x|}{8(1+w^2)^{3/2}}
 +\frac{\alpha r_{o,x}\omega}{1+w^2},
\qquad \ell_x=(\log w)_x,
$$

其中 $\alpha,r_{o,x},\omega$ 严格正。故在整个面板上

$$
r_x\ge\frac{\alpha\,r_{o,x,-}\omega_-}{1+w_+^2}>0.
\tag{O2}
$$

特殊 $n=0,j=8$ 段保留 $\chi=1-S(x)\in[0,1]$ 和 $j_0=1+(r_{\rm cut}/r_{\rm oldcut}-1)S(x)>0$：

$$
r_x=r_{o,x}\{(1-\chi)j_0+\chi\alpha\omega/(1+w^2)\}
 +\frac{\chi w|\ell_x|}{8(1+w^2)^{3/2}}.
$$

大括号是两个正量的凸组合。因此有效的统一下界是

$$
r_x\ge r_{o,x,-}
\min\left(1,\frac{r_{\rm cut}}{r_{\rm oldcut}},
\frac{\alpha\omega_-}{1+w_+^2}\right)>0.
\tag{O3}
$$

程序把 (O2)/(O3) 与原精确表达式的区间值域相交。因此在曲率重分配项接近零时，不会把朴素区间的消减损失误当作真实径向坐标退化。

## 4. R26 父宽度与子面板约束

对一个 R26 父面板 $J$，已保存严格积分宽度

$$
\Delta r_J=\int_Jr_x\,dx.
$$

若无需细分，直接使用这个原严格宽度。若分成子面板 $J_i=[a_i,b_i]$，源值域给

$$
(b_i-a_i)r_{x,-,i}\le\Delta r_i
\le(b_i-a_i)r_{x,+,i}.
\tag{O4}
$$

这是真实积分的范围乘长度包围，不是 binary 数值积分。所有子积分还同时满足 $\sum_i\Delta r_i=\Delta r_J$，故可进一步把每个区间与

$$
\Delta r_J-\sum_{k\ne i}\Delta r_k
\tag{O5}
$$

相交。这里每个减项原本就包含准确积分；相关性只让区间可能变宽，不影响有效性。程序核对每个父面板的子面板首尾、顺序和完整覆盖。

由同一个准确父端点分别向前、向后累加这些正宽度，得到每个子端点的两个有效半径包围；取交集后再使用整个子面板的单调半径范围。这保留了 R26 的真实半径锚点，避免把极小胞元宽度与 nominal binary 端点混合。

## 5. 五积分及其连续部分积分的包围

在子面板上，令 $q_i^\pm,w_i^\pm$ 为实际非负值域。由 $dr>0$，

$$
q_i^-w_i^-\Delta r_i^-
\le\int_{J_i}wq\,dr
\le q_i^+w_i^+\Delta r_i^+.
\tag{O6}
$$

对所有子面板相加即为 (O1) 的包围。对于子面板中的任一点，因为全部五种积分密度非负，$0\to u$ 的积分介于该面板两端的前缀积分之间，$u\to1$ 的积分介于对应后缀积分之间。因此输出的 `prefix_moments` 与 `suffix_moments` 都是**整个面板**上的范围，且在数学定义上始终有

$$
I_q^{\rm prefix}(u)+I_q^{\rm suffix}(u)=I_q.
$$

R48 的同一个 bubble 系数由准确总积分定义。R44/R48 helper 使用这些共同积分的包围计算同一个 $H$；它没有在每个角度、每个面板分别选择新的积分常数。高度的左积分表达式与右积分表达式取交集，仍然包含同一准确候选高度。

在包含零的部分积分区间上，Arb 半径向上舍入有时会产生极小负下端。数学上可与准确的非负域相交，或使用准确可表示的 $[0,2^e]$ 包围。**实际 v1 程序的 `arb(0).union(2^e)` 仍会向外膨胀约一个半径 ulp，因而不能声称它的保存下端恰为零。** cell 11 中有 42 个这样的部分积分盒，原完整区间仍包含真实非负积分；正式恢复保留这些精确原上下端，没有偷偷改数据。后续 R48 读取必须显式使用已证明的非负积分域；若希望存储盒本身非负，应使用准确 dyadic midpoint/radius 构造并再次核对。需要作除数的完整五个总积分均已有严格正下端，不能用非严格替代。

## 6. 接到真实 13port 候选的方法与未付项

现有端点 helper `tail_outer_weighted_endpoint.py` 用全部已保存 M20 的 binary $Q,L$ 和相同真实背景，明确给出一个有限逆多项式的候选 $H,H_r,H_{rr}$。它保留全部保存模态，也单独记录该有限逆/投影相对于固定候选 mean 的完整源差。这个候选导数没有被称为未知真实径向解的准确导数。

接合顺序为：

1. 用该端点定义取得同一个物理端点两 jet，再按每个胞元自己的单一 $u$ 转为 $H,K,K_u$。
2. 用本文实际算出的五个总积分建立唯一的 R48 bubble 系数。
3. 对每个真实面板，以同一总积分、连续前后缀积分以及实际 $r,r_x,w,\ell_x$ 调用 `certify_weighted_panel`。
4. 先核候选的完整角强范数和 leading margin，再用 R44 完整 mean 根与其导数计算全频 $J/L$。没有通过第 3–4 步就不宣称连续缺陷已付。

端点两 jet 一致且源背景连续时，R48 构造给非均值 $C^2$ 接缝；完整 mean 的唯一小根与一个共同高度常数仍按 R44 恢复。源 $r_x$ 中的绝对值可能导致更高导数在临界点分段，因此 R48 的四阶逼近误差引理仅在满足其正则性假设的片段使用，不能无条件跨过所有 source cusp。

只有 13 个端点时，单胞元候选在内部 valley 可能仍不能满足 $\|H_\theta/(rw)\|$ 的小球门。若实际范围失败，必须保留失败位置及区间，随后再使用真实保存的更密状态改善候选；不能从端点全过推出整条径向轨道全过。当前 109 locator 保持未运行，也没有用文字补造其结果。

## 7. 准备命令与资源范围

首次实际算术选择一个完整胞元，核对输出的全部正积分、真实坐标和资源记录后，再按同一公式扩展。下面是已执行 cell 11 的原数学命令；由于完整单包超过 5 MB，实际保存按正式记录中的第二个纯序列化命令完成。重算必须使用 fresh 输出名：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python computations/tail_outer_positive_moment_panels.py \
  --ready notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
  --radius-ledger notes/2026-11-12-root-real-outer-radius-v4-recovered-full.json \
  --first-cell 11 --last-cell 11 --log-span 1/8 --u-span 1/32 \
  --precision 192 --max-level 40 --max-panels 20000 --rss-limit-mib 120 \
  --out-prefix notes/2026-11-12-tail-outer-positive-moments-cell11-r1
```

程序按胞元逐个 gzip 保存完整面板与全部五种前后缀积分；单文件超过 5 MB 会保留 `.partial` 并失败。任何未完成文件不会被登记为正式成功包。此准备工作不占用新的 Node、BVP 或大 Jacobian 任务。
