# 实际 warm .25 尾深端的有限 C² 圆领与平盘

维护：Astra-held10-1b6d88ec-20261120 / geometry_advance。2026-11-20 UTC。

## 结论与范围

**已证明，并实际执行精确有理计算：** 从当前 M24、depth 8、warm `.25 H` 已接受尾解的最后一段 stage 1151，取深端保存的 Cartesian Fourier 物理半径两阶数据，以这些字面数据定义一个新的有限共享 Hermite 圆领。它在外端精确匹配这份两阶数据，在内端以共同零两阶数据接回 [R58](../results/R58-q060-valley-background-height-and-curvature.md) 的当前首 valley=4.625 真实背景，再沿同一背景接到已有 C² 平盘。

在背景 cut 高度 $z_b\in[1/10,32/25]$ 的明确放置窗内，这个圆领加内部背景和平盘是 C² 嵌入的盘组件；对同一真实背景度量

$$g=(1+w(R)^2)\,dR^2+R^2\,d\theta^2$$

满足

$$
\boxed{\quad
\|g^{-1/2}(F^*\langle\cdot,\cdot\rangle-g)g^{-1/2}\|_{\rm op}
 <3.772\,10^{-30},\quad
|\kappa_i|<8.001,\quad |F|<1.34,\quad F\cdot n>.09.
\quad}
$$

外端与内端合计 **918 条标量两阶端点等式**用 Fraction 精确验证。有限圆领完全消掉非旋转扰动；没有诉诸无限非线性尾的渐近延拓。

本条的对象是**由实际保存参数显式定义的新 C² 图**。原 planar `rr` 是有限差分输出，本条只把它作为新 Hermite 图的字面端点参数，不把它称为原 shooting 场位置的精确二阶导数。这里未证明 full H 真尾存在、前缀与尾的 Cartesian 接缝、全闭面、同度量加密收敛或全时族。$z_b$ 的窗口是明列的组件放置条件，未通过重置 mean 把它冒充成已付的前缀接缝。

## 1. 实际输入与共同物理坐标

实际 checkpoint 为
`newg-wide-lambda0p002-m24-actual/tail_0001.json.gz`，SHA-256：

`302662026a7e213647d8bfb2813f970174c8c919bb6f4d406e073ef9f3c110de`。

该次已接受的 warm `.25 H` residual 为 $1.8946163107633334\,10^{-10}$，在原 $2\,10^{-9}$ 门内。原 native record 为
`newg-native-m24/runs/actual-lambda0p002/0009-jac-record.json`，SHA-256：

`a15afe15bdea350f03ea282c475deece4179f59c72f227b0bac9b5ec00980e7a`。

[extract_q060_stage_from_native_record.py](../scripts/resume_n4/extract_q060_stage_from_native_record.py)
读取原 native record；实际核对全部 1152 个 native 输入的前 48 个分量与 checkpoint 的相应内端 state **逐字相等**，并核原 token、来源哈希与 complete 状态。所选 stage 1151 为 raw cell 7、segment 0、$x\in[0,1/16]$，其内端非旋转 mean 与背景 mean 槽分别为零。没有重新求解边值问题。

[export_q060_saved_stage_r_jets.mjs](../scripts/resume_n4/export_q060_saved_stage_r_jets.mjs)
仅以原 source 的实际 Cartesian 发展重放所选已有 IVP，保留其 $\Omega$/Darboux 和 mean 语义。以下定义均保留该导出的合同：

1. node 0 的 `radiusJS` 是新物理 $R$ 图的**精确 binary-real 外端结点**，并非真实背景半径区间的中点。
2. 水平扰动写成 $V_x+iV_y=\sum_m a_m(R)e^{im\theta}$；本次有 128 个水平 Fourier 项。
3. 高度扰动写成 $\sum_{m=0,3,\ldots,72}c_m(R)\cos(m\theta)$，共 25 项。原非均值高度采用实际 $r_{\rm JS}^4u$，不默换成 $R_{\rm true}^4u$。
4. 这些高度项只含**非旋转 mean**；背景高度另由 R58 的真实 primitive 加入。不能把 `meanBackground` 再加进扰动槽。
5. 上侧图对所有高度系数及其两阶导数统一取负号。背景取
   $\Xi(R,\theta)=(R\cos\theta,R\sin\theta,z_b+h(R_c)-h(R))$。

本条的唯一外端共享数据就是该 node 0 的 459 个有理标量。后继全尾图应在此边界使用同一份数据；不能以另一次浮点评价“很接近”替代共同两阶等式。

## 2. 一个明确的有限圆领

取

$$
R_0=\frac{1821664769296115}{36028797018963968},\qquad
a_0=\frac{900719925474099}{18014398509481984},
$$

$$
R_i=\frac{R_0+a_0}{2}
=\frac{3623104620244313}{72057594037927936},\qquad
L=R_0-R_i=\frac{20224918347917}{72057594037927936}.
$$

这里 $a_0$ 是同一个当前背景的 cuff 半径，且 $1/25<a_0<R_i<R_0<3/10$。对每个 Fourier 系数，其外端物理 $R$ 两阶数据记为 $(v_0,v_1,v_2)$。设 $u=(R-R_i)/L$，定义

$$
H_0=10u^3-15u^4+6u^5,\qquad
H_1=-4u^3+7u^4-3u^5,\qquad
H_2=\tfrac12u^3-u^4+\tfrac12u^5,
$$

$$p(R)=H_0(u)v_0+LH_1(u)v_1+L^2H_2(u)v_2.$$

于是 $p^{(j)}(R_0)=v_j$、$p^{(j)}(R_i)=0$，$j=0,1,2$。源对全部 153 个系数逐项用有理 Horner 求值验证这 918 条等式。取这些 $p$ 组成 $V$，在 $R_i\le R\le R_0$ 令 $F=\Xi+V$；$R\le R_i$ 令 $V=0$。圆领内外均为明确共享两阶的 C² 图。R58 已证明同一真实背景在 $a_0$ 处 C² 接到平盘；本次不重新积分背景或重新证明深源一般定理。

## 3. 全圆领、全角的有理 Fourier–Bernstein 界

对每个 $p^{(i)}$，源在 $u\in[0,1]$ 上转换成精确 Bernstein 系数，取系数绝对值的最大值。各 Fourier 项乘以 $|m|^j$ 后求和，给出

$$\sup_{[R_i,R_0]\times S^1}|\partial_R^i\partial_\theta^jV|\le B_{ij}.$$

水平复 Fourier 项与竖直 cosine 项都通过向量三角不等式计入。下表为向外显示值；比较与所有端点等式使用精确有理数：

| $i\backslash j$ | 0 | 1 | 2 |
|---|---:|---:|---:|
| 0 | $1.0584683291083784\,10^{-34}$ | $3.1754047454388777\,10^{-34}$ | $9.526214259116107\,10^{-34}$ |
| 1 | $1.885562152807175\,10^{-30}$ | $5.656686027523822\,10^{-30}$ | $1.6970058123186592\,10^{-29}$ |
| 2 | $3.4678964874537255\,10^{-26}$ | $1.0403688847544198\,10^{-25}$ | $3.1211066628331617\,10^{-25}$ |

这些是连续范围界，不是角采样峰值，也不是原 finite audit 的数值输出。

令 $r_*=1/25$，则目标正交方向一阶误差由

$$
\eta_1=\sqrt{B_{10}^2+(B_{01}/r_*)^2}
\le1.885578863922015\,10^{-30}
$$

包围，因为 $\sqrt{1+w^2}\ge1$。故真实相对 operator 度量误差至多 $2\eta_1+\eta_1^2$，得到结论中的严格界。根号上界由整数 `isqrt` 和精确整数比较得到，不依赖浮点平方根方向。

同样，目标归一的 ambient 二阶误差由

$$
\eta_2=\sqrt{B_{20}^2+2(B_{11}/r_*)^2+(B_{02}/r_*^2)^2}
\le3.4679541559035833\,10^{-26}
$$

包围。R58 给背景 $|\kappa_i|\le8$、$0\le w\le41/100$。其目标归一 ambient Hessian 的三个方向分别满足

$$
|\Xi_{RR}|/(1+w^2)\le8\sqrt{1+(41/100)^2},\quad
|\Xi_{R\theta}|/(R\sqrt{1+w^2})\le25,\quad
|\Xi_{\theta\theta}|/R^2\le25.
$$

因此该矩阵的 Frobenius 范数小于 45。新旧同向单位法线之差至多 $\sqrt2\eta_1$：参考正交切标架 $A_0$ 与误差 $E$ 满足 $A_0^Tn=-E^Tn$，故夹角的正弦至多 $\eta_1$；沿 $\Xi+tV$ 的浸入同伦保留正向，得到此界。于是

$$
|\kappa_i(F)|\le
\frac{8+45\sqrt2\eta_1+\eta_2}{(1-\eta_1)^2}<8.001.
$$

## 4. 大小、support 与这个盘组件的嵌入性

本次复用的 R58 高度严格上界是

$$h(R_c)\le h_*:=\frac{7446320975220351}{288230376151711744}.$$

因此对明确的 $z_b\in[1/10,32/25]$，

$$
R_*:=\sqrt{(3/10)^2+(32/25+h_*)^2},\qquad
|F|\le R_*+B_{00}\le1.339852246826965<1.34.
$$

背景上向法线为 $(w e_R,1)/\sqrt{1+w^2}$；由 $Rw\ge0$、$h(R_c)-h(R)\ge0$ 和 $\sqrt{1+w^2}<11/10$，其 support 大于 $1/11$。新图于是有

$$F\cdot n\ge\frac1{11}-R_*\sqrt2\eta_1-B_{00}>.09.$$

同一个 $\eta_1$ 还界定水平扰动关于 Euclidean 平面坐标的一阶 operator 范数，因为该界在径向没有除以 $\sqrt{1+w^2}$。将 $V$ 在内部延拓为零后，平面投影为 $p\mapsto p+V_{xy}(p)$，扰动在整个凸盘上的 Lipschitz 常数小于 $\eta_1<1$。所以投影单射，从而这个 C² 盘组件嵌入。平盘中心附近扰动恒零，没有极坐标奇点。

这里没有由局部曲率直接推出整个闭曲面的 reach；其他组件、相互位置、完整接缝以及全时运动仍须另付。

## 5. 实际执行与复现

源为 [certify_warm025_deep_collar.py](../scripts/resume_m3/certify_warm025_deep_collar.py)，SHA-256：

`ce79a1fd84b55d13285f2ca6c2a2988b333d0e60820ec8c4ba49b53fbad30099`。

它逐项绑定实际物理参数、首 valley=4.625、protectCell=160、当前 factory SHA 和真实背景定义 SHA，没有搬用旧 3.125 尾数据。完整执行绑定见
[2026-11-20-warm025-deep-collar-execution.json](2026-11-20-warm025-deep-collar-execution.json)。三步均实际 exit 0，最后的精确圆领证书约 0.1334 秒。输出摘要：

| 项目 | 连续严格界或实际检查 |
|---|---:|
| exact endpoint equalities | 918 |
| relative operator metric | $<3.772\,10^{-30}$ |
| principal curvature | $<8.001$ |
| radius | $<1.34$ |
| support | $>.09$ |
| planar perturbation Lipschitz | $<1.886\,10^{-30}$ |
| nonlinear solves / background integral recomputations | 0 / 0 |

以下命令中 `TOPIC` 为本题目录，`WORK` 为复现的库外临时目录；`M3WORK` 保留当前公开来源恢复出的 native record 和 checkpoint 路径：

~~~bash
python "$TOPIC/scripts/resume_n4/extract_q060_stage_from_native_record.py" \
  --checkpoint "$M3WORK/newg-wide-lambda0p002-m24-actual/tail_0001.json.gz" \
  --native-record "$M3WORK/newg-native-m24/runs/actual-lambda0p002/0009-jac-record.json" \
  --stage 1151 --out "$WORK/stage1151-saved-native-input.json"

node "$TOPIC/scripts/resume_n4/export_q060_saved_stage_r_jets.mjs" \
  --input "$WORK/stage1151-saved-native-input.json" \
  --out "$WORK/stage1151-literal-r-data.json"

python "$TOPIC/scripts/resume_m3/certify_warm025_deep_collar.py" \
  --stage-data "$WORK/stage1151-literal-r-data.json" \
  --stage-packet "$WORK/stage1151-saved-native-input.json" \
  --tail-constants "$N4WORK/q060-tail-geometry/constants.json" \
  --out "$WORK/warm025-deep-collar-certificate.json"
~~~

完整 stage 数组、重放输出与有理证书仅在 scratch 保留；仓库只收源、必要标量、命令和哈希。原 checkpoint 与 native record 的生成来源继续沿用该次已有记录，不为了本局部组件重新求 full H 或其他尾解。
