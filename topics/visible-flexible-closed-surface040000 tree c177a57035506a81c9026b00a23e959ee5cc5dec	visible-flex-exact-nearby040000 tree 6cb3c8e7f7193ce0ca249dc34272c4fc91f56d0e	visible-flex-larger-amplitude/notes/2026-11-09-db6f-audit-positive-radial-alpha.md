# 固定 weighted 背景的精确径向归一参数为正

2026-11-09，`/root/independent_geometry`。本文的解析 TV 论证及拼合账本为新推导，待 root 或 tail_theory 独审。cell 0 区间积分器由 tail_theory 编写，已由本文作者全文独审及独立复跑。结论针对固定解析旋转背景，不是无限非线性尾或完整等距曲面的存在结论。

## 1. 固定的几何定义

主参数、cap、有限 valley controls、positive warp weights 与有限 pulse levels 都使用正式 coupled M8 checkpoint 的 binary64 数作为精确实数。有限 cells $0\le n<160$ 的 source 校准数 $\widehat\alpha_n$ 使用 `notes/2026-11-09-db6f-tail-finite-source-calibrations.json` 中冻结的 160 个 binary64 数，作为几何系数本身；不额外宣称它们是未给出误差条的精确校准根。此表 SHA256 为 `bcfaba00aec62290b5b29432836c9e76ef6cf0d582b06c046677b0f8688ca9f4`。

该有限表在原 32/64/128 及新 M8/M12 求解输入中固定；`calibrationSteps=512` 不作为后续 PDE/RK 加密参数改变。从 $n=160$ 起仍采用原先已审的无限 source 定义，未把这张有限表推广为无限表。

其余派生量按同一解析公式定义，例如

$$\delta_n=\delta_0 2^{-n},\quad \eta_n=\delta_0c_0 2^{-3n/2},\quad
T=6\delta_0+\frac{6\delta_0c_0}{1-2^{-3/2}},\quad
r_{old}=a_c e^{T/\sqrt{12}},$$

$$\epsilon_{source}=\frac{w_{cut}r_{old}^7}{(2\delta_0)^{11/4}}.$$

这里 $a_c$ 是 cuff 半径，避免与 source 指数或校准参数混淆。本文不把独立舍入的 `oldCut`、`epsilonScale` 与这些解析公式视作精确相等；认证对象是上述明确的解析定义。

已用 Fraction 核对全部冻结 $\widehat\alpha_n\in[1/2,2]$，且其 hex 字符串与数值字段逐项一致。实际 minimum 约为 $1.01545$，maximum 约为 $1.49512$。以下证明只用有理盒，不用这些小数近似。

## 2. 要证明的精确归一方程

设 $r_d$ 为原 source 的 cell 159 最深端半径。有限部分通过真实积分定义新的径向坐标；总宽度形如

$$A+\alpha B,$$

其中每个 profile 上

$$A_j=\int\left((1-\chi)j_0r'_o
 +\frac{\chi|w_x|}{6(1+w^2)^{3/2}}\right)dx,$$

$$B_j=\int\frac{\chi r'_o\omega}{1+w^2}\,dx.$$

$r'_o>0$，$\omega>0$ 是固定正权重，$0\le\chi\le1$。只有 cell 0 的最后 raw port 与 cell 159 的第一个 protected port 有 $\chi\ne1$。其余 $A_j$ 正是 $w/\sqrt{1+w^2}$ 总变差除以 6。

目标宽度为 $L=r_{cut}-r_d$。由于 $A,B$ 的 integrands 与未知全局径向参数 $\alpha$ 无关，只要 $B>0$ 且 $A<L$，就有唯一的精确解

$$\alpha=\frac{L-A}{B}>0.$$

此参数不是表中的有限 cell 校准数 $\widehat\alpha_n$。

## 3. cell 0 的独立区间积分

已全文审读 `scripts/db6f-tail-background-height-interval.py`，修正版 SHA256 为 `37adea90f144d3550ddfd098dcf8fa08eb30e8b0bab46d28df20efffaf7ab94e`。检查了原 source 半径、log slope、valley、variable cap、cut-preserving 恢复、正权重、最后端 $j_0$ 和 $\chi$ 的全部九段公式，与源实现一致。

指数区间先缩到 $|y|\le1/8$，用 18 阶 Taylor 及 $\frac87(1/8)^{19}/19!$ 余项，再逐次向外平方。`log2/ceil` 只提供初始缩放猜测；修正版增加精确二进缩放后的 guard，确保余项所用的 $1/8$ 范围真正成立。对数使用精确二进 frexp 分解及 $2\operatorname{atanh}z$ 的 32 项级数、显式几何余项。分段 cap 的所有交叠分支均取包围；未将 adaptive Gauss 结果当成证书。

在每个 source profile 的 $[0,1]$ 上取 4096 个有理区间，以区间函数范围乘其精确长度并向外求和。独立命令（本题目录）：

```sh
python scripts/db6f-tail-background-height-interval.py \
  notes/2026-11-09-db6f-prefix-flat-v17v18-coupled-m8-q10-fine_tail_0017.json.gz \
  notes/2026-11-09-db6f-tail-background-split.json \
  notes/2026-11-09-db6f-audit-tail-background-height-rerun.json \
  --cells 4096
```

全部数值字段与作者报告同值。尤其

$$A_0\le0.208230146301551<21/100,$$

$$B_0\ge0.0009760409686192003>0.$$

上式中的小数端点是向外区间的精确 binary64 数，最终比较由 Fraction 完成。cell 0 最后恢复段及最后 raw port 已包含在这份证书内。

## 4. 内有限尾每个 cell 至多有两段上升

对 $1\le n\le159$，cap level 是同一个常数 $c_{cap}\le1/49$，没有 `flatOuterThroughCell` 覆盖。把 valley control $\beta_n$ 吸收到中间平台后，五个 log 平台为

$$v_0=\log\delta_n,\quad v_1=\log R_n,\quad
v_2=2\log\delta_n-\log\widehat\alpha_n+\beta_n,\quad
v_3=0,\quad v_4=\log\delta_n+(11/4)\log2.$$

在每个 transition 上，未 capped log slope 具有形式

$$z(x)=C+(v_{k+1}-v_k)S(x)-\lambda x,\qquad
\lambda>0,\quad S'(x)=30x^2(1-x)^2.$$

若 jump $v_{k+1}-v_k\le0$，则 $z'<0$。若 jump 为正，由 $S'$ 先严格增后严格减，$z'>0$ 至多在一个连通区间中成立。flat 平台与 port 的 log slope 均严格递减。

由于 $R_n>1$ 且 $\delta_n2^{11/4}<1$，第一条 jump 为正，最后一条为负。中间两条 jump 的和为 $-\log R_n<0$，所以其中至多一条为正。故每个 cell 只可能有两段正向上升。

常值 smooth cap 对 raw log slope 的导数位于 $[0,1]$；它不能创造额外的正向变化。$f(w)=w/\sqrt{1+w^2}$ 也严格递增。若全 cell 的 $w\le M_n$，则其总正变差不超过 $2M_n$。记 $V_+,V_-$ 为 $f(w)$ 的正负变差，由

$$V_++V_-=2V_+-(f_{end}-f_{start}),\qquad0\le f\le M_n,$$

得到简单而有余量的界

$$\operatorname{TV}_{cell\ n}\frac{w}{\sqrt{1+w^2}}\le5M_n.\tag{4.1}$$

此式不需要把不同 cell 的端点误差当成零，也不依赖有限 valley control 的大小。

## 5. 从第十个 cell 起使用几何衰减

对 $1\le n\le9$ 取 $M_n=1/49$。冻结输入从 $n\ge10$ 的 valley control 全为零，$1<R_n\le64$，且 $\widehat\alpha_n\ge1/2$。于是所有平台上的 $e^{v_k}\le64$；log 插值也满足同一界。

归一化 source 公式给

$$w_{raw}(r)=\frac{1}{2^{15/4}\delta_0}
\left(\frac{r_{old}}{r}\right)^7
2^{-7n/4}e^{v(x)}.$$

有理参数盒给 $T<1/20$、$\sqrt{12}>3$，因此

$$\left(\frac{r_{old}}r\right)^7
\le e^{7T/\sqrt{12}}<6/5.$$

再用 $\delta_0\ge1/200$、$2^{11/4}>6$ 及 $e^v\le64$，得到

$$w_{raw}\le1280\,2^{-7n/4}=:W_n.$$

smooth cap 从不增大 raw slope，故同一 $W_n$ 适用于 capped 值。这一步仅用于已冻结的有限 cells $10\le n\le159$，不需要把有限校准表外推到无限。

由 $\sqrt2>7/5$ 和 $2^{-7/4}<1/3$，

$$W_{10}<25/3584,\qquad
\sum_{n=10}^{159}W_n<\sum_{n=10}^\infty W_n<75/7168.$$

这里最后的无穷级数只是显式数列的上界，不是无限非线性解的尾误差。结合 (4.1)，所有内 finite cells 的 curvature-width 部分满足

$$A_{inner,curv}\le\frac56\left(\frac9{49}+\frac{75}{7168}\right).\tag{5.1}$$

## 6. 保护端的旧径向项

cell 159 第一个 port 的 $j_0=1$，额外项至多其旧 source 的径向长度。保守地用整个旧 source 厚度包围即可：

$$A_{protect,old}\le r_{old}-a_c
<\frac{a_c}{59}\le\frac3{1180}.\tag{6.1}$$

因为 $T/\sqrt{12}<1/60$ 且 $e^x\le(1-x)^{-1}$，确有 $r_{old}<60a_c/59$。这覆盖保护端的所有内部点及端点；没有遗漏原 source 与有限 warp 的混合区域。

## 7. 严格比较并得到正参数

将 cell 0、(5.1)、(6.1) 相加，Fraction 账本给

$$A<\frac{21}{100}+\frac56\left(\frac9{49}+\frac{75}{7168}\right)
+\frac3{1180}<\frac38.$$

保留 cell 0 的实际向外区间端点时，上界约为 $0.372553052$；上式较圆整的有理上界约为 $0.374322906$。两种表示均由精确有理比较判定严格小于 $3/8$。

另一方面，$r_d<r_{old}<60a_c/59\le9/59<4/25$，而实际冻结 $r_{cut}>59/100$，故

$$L=r_{cut}-r_d>43/100>3/8>A.$$

再由 cell 0 已给 $B\ge B_0>0$，得到唯一精确的全局径向归一参数

$$\boxed{\alpha=(L-A)/B>0.}$$

所有权重均不超过 3，所以 $B<3(r_{old}-a_c)<9/1180$。结合 cell 0 的正下界，当前粗账本甚至给出严格包含区间，显示值为

$$7.2998<\alpha<255.841.$$

完整精确有理端点保存在 JSON 中。该粗区间只用于确认存在与正性，不把原数值 $\alpha$ 冒充精确解。

每个 profile 的新 radial speed 严格为正：$\chi>0$ 时正的 free term 起作用；$\chi=0$ 的端点则由正的旧径向项起作用。真实积分连续累加后，最深端固定、外端严格等于给定 $r_{cut}$。

## 8. 可执行账本及其作用域

```sh
python scripts/db6f-audit-tail-radial-alpha.py \
  --checkpoint notes/2026-11-09-db6f-prefix-flat-v17v18-coupled-m8-q10-fine_tail_0017.json.gz \
  --calibrations notes/2026-11-09-db6f-tail-finite-source-calibrations.json \
  --cell-zero notes/2026-11-09-db6f-audit-tail-background-height-rerun.json \
  --out notes/2026-11-09-db6f-audit-positive-radial-alpha.json
```

脚本核对全部参数盒、有限校准表、source hashes、cell 0 已审实现哈希、checkpoint 与 bookkeeping 绑定，并用 Fraction 进行最终比较。它不调用 source Gauss 积分器或原非线性求解器。

因此，背景高度界中“存在正的精确全局径向归一参数”这一条件现有可审的完整支付。结合已独审的 cell 0 $AH,BH$ 包，整尾高度的 $0.083159187775$ 上界可以在这同一个解析固定背景上使用。仍须将实际显式非线性尾的导数、端迹、共同 metric 与这个解析背景严格绑定，不能从背景正性直接宣布全图认证完成。
