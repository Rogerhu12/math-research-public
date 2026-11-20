# 当前 M24 真桥的切口高度与保存尾 mean 的标量接续

维护：Astra-held10-1b6d88ec-20261120 / geometry_advance。2026-11-20 UTC。

## 结论

**已证明并实际执行精确标量组合：** 对 [R60](../results/R60-actual-m24-c2-bridge-and-continuous-metric.md) 的当前 $\lambda=.002$、M24、真共享 C² 桥，保留同一原字面节点 mean1168 与其真实径向 primitive，切口的标量高度 $Z_c$ 满足

$$
.49816463756368945\le Z_c<1.2699551265208522.
$$

对当前保存的 warm `.25 H` 尾，**保留原非旋转 mean**，并明确将真实背景 cut 高度定义为

$$z_b=Z_c+\mu_c,$$

其中 $\mu_c$ 是该尾保存的 cut 非旋转 mean（精确 binary64 `3.681650775547157e-7`），则

$$
.498165005728767\le z_b<1.2699554946859297,
\qquad \boxed{\ .49<z_b<1.27\ }.
$$

因此，按这个明确的常数高度安放，当前 [R58](../results/R58-q060-valley-background-height-and-curvature.md) 背景、已付深圆领和平盘、以及 stage 0 连续 R 图所需的 $z_b\in[.1,1.28]$ 条件全部满足。

本条只接续**高度常数/零模**。warm `.25 H` 的非零模式并不是当前桥的 full H 端口，不能据此声称其 Cartesian 值、一阶、二阶接缝已完成。没有把尾部的 512 点规则认成前缀的 1168 点规则，没有重置原 mean，也没有改变已有桥图的位置。

## 1. 所有桥端量确实属于同一图

所用 run.json 与 physical.npz 分别为

`c44b6fd2fbb13cc9ce0451cc6ab1d3c06521de0622de27190bde94c4c550462a`，

`f2e22fe19bb0b6fdeff79c4fa99363d9be6cbb1ef382fd882679a2b717a3030d`。

以下已执行证书的 run/physical SHA、公共 Hermite 定义和 mean 节点数都逐项一致：

- [前缀绝对高度](2026-11-20-m24-prefix-absolute-height-certificate.md)：公共右二阶 Hermite $Y,e$、端点归一 profile、完整真 R53 lift、mean1168。
- [显式 C² 桥 §3–5](2026-11-20-m24-r59-explicit-c2-bridge-certificate.md)：同一 $Y,e$ 的共享 Hermite、桥相位末段解析延拓、真实半径原函数、mean1168 的真实径向 primitive。
- R60：上述实际 C² 桥的全域位置与连续度量结论。

桥起止点按原 binary64 数精确解释，长度为

$$L_s=\frac{4191465360069805}{4503599627370496}.$$

入口高度已有

$$z_0\in[.44631325197234495,.47839691621379593].$$

现有全桥连续 mean 证书不是只给 $|M-\cos\phi|<.01$，还直接给出了严格值域

$$
M(s)\in[.055712706838148364,.9986787565095109].
$$

特别是 $M>0$。这些是已付真实有限 1168 点均值的连续径向界，不是原 GL6 高度查询值。端点共享 C² 修补已包含在该证书内；没有用旧未修补多项式的峰值替换它。

## 2. 不重新积分得到的切口高度界

按同一真 primitive 定义

$$Z_c=z_0+\int_{s_b}^{s_e}M(s)\,ds.$$

因此

$$Z_c\ge z_{0,-}+L_sM_-\ge .49816463756368945.$$

上界不使用较松的 $z_{0,+}+L_sM_+$，而用 R60 全桥 $|F|<1.245$。在切口

$$F_z(s_e,\psi)=Z_c+G_z(s_e,\psi).$$

同一 C² 非均值证书已给全桥全角

$$|G|\le G_0=\frac{6238781630213}{250000000000000}=.024955126520852.$$

故对任何角度都有

$$Z_c=F_z-G_z<1.245+G_0
=\frac{317488781630213}{250000000000000}.
$$

这些等式没有依赖浮点高度采样，也没有再次计算均值积分。上下界的最终比较仅作 Fraction 运算。

## 3. 保存尾的原 mean 如何接入

保存尾使用与 stage 0、深圆领相同的 checkpoint：

`302662026a7e213647d8bfb2813f970174c8c919bb6f4d406e073ef9f3c110de`。

stage 0 的实际导出数据明确把背景 mean 与非旋转 mean 分开。其 cut 高度系数的 $m=0$ 项逐字等于

$$\mu_c=\operatorname{binary64}(3.681650775547157\cdot10^{-7}).$$

它没有被设成零，亦没有因替换成真背景 primitive 而重复加入背景 mean。

当前桥的 late cutoff 是 $1-10u^3+15u^4-6u^5$。在 $u=1$ 的值、一阶和二阶导数精确为零，所以切口材料角等于 $\psi$，其角图混合的一、二阶也消失。桥竖向非均值项只有 $3,6,\ldots,72$ 的非零 cosine 频率；切口常数高度槽是 $Z_c$。

在上侧，将尾的原高度扰动整体反射，写成

$$
F_{{\rm tail},z}(R,\theta)
=z_b+h(R_c)-h(R)-\mu(R)-\widetilde H(R,\theta),
$$

其中 $\widetilde H$ 无零模。切口处 $h(R_c)-h(R_c)=0$，因此其常数项是 $z_b-\mu_c$。取

$$z_b=Z_c+\mu_c$$

恰将两个已指定组件的**常数高度槽**对齐。这是背景放置常数的明确数学定义，未用区间中点代替 $Z_c$，未更改尾原 mean 函数。与 $Z_c$ 的界相加就得到开头的 $z_b$ 区间，严格落入 R58 所需窗口。

相同 $z_b$ 用于整条真背景与内部圆领/平盘，没有给不同组件分别选择有利平移。内侧 $h$ 的真实定义和当前首 valley=4.625 参数均未变。尚未接好的非零模式、径向一阶/二阶以及 full H 条件，仍不能由常数高度对齐推出。

## 4. 执行与保持的边界

独立标量源为
[certify_m24_cut_height_contract.py](../scripts/resume_m3/certify_m24_cut_height_contract.py)。它只读取已完成证书的有限摘要及 stage 0 保存数据，验证共同 SHA/mean1168/共享图合同，再作有理标量运算和 cutoff 端点等式；没有积分、求解器调用或均值 provider 再评价。实际 exit 0，约 0.0118 秒。执行绑定见
[2026-11-20-m24-cut-height-contract-execution.json](2026-11-20-m24-cut-height-contract-execution.json)。

~~~bash
python "$TOPIC/scripts/resume_m3/certify_m24_cut_height_contract.py" \
  --prefix-height "$N4WORK/prefix-z0-normalized-certificate.json" \
  --bridge-mean "$WORK/newg-m24-r59-c2-mean-certificate.json" \
  --bridge-nonmean "$WORK/newg-m24-r59-c2-nonmean-certificate.json" \
  --bridge-geometry "$WORK/newg-m24-r59-c2-geometry-combination.json" \
  --stage-data "$WORK/stage0000-literal-r-data.json" \
  --stage-packet "$WORK/stage0000-saved-native-input.json" \
  --out "$WORK/m24-cut-height-contract-certificate.json"
~~~

后续末端目标 $g$ 的微小统一修补只改目标度量，不改 R60 的实际图和 mean；因此不会改动本条 $Z_c$。中央入口紧支撑修补在桥之前已经恒为零，也不会改变本条。相反，新的 $\lambda$、新的完整联立场或新的 mean 规则不能未经证明直接继承这里的高度界。
