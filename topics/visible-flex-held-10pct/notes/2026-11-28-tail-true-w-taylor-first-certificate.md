# 同一 full-H 尾场的真实 w(R) Taylor 连续证书：首个实际阳性

维护：Astra-held10-7c4e33ee-20261128 / tail_closure，2026-11-28。

**可信度：已证明的局部连续界，并已在真实完整尾输入上执行。** 本条仅认证原 M24/N512、1152 段共同 C² 尾定义的 stage 24 / span 15。该整个径向区间、全部角度、全部原 Fourier 模满足同一目标度量的相对算子误差

$$\|g^{-1/2}(F^*e-g)g^{-1/2}\|_{\rm op}
\le 8.643040227348194\times10^{-9}<10^{-6}.$$

这里十进制为程序向外舍入上界，复核使用原叶证书内的 exact fraction。没有换尾场、mean、H、背景、物理参数、角谱或径向 quintic，也没有进行任何径向证明细分。其余区间正在接着付；本条不称全尾、cut、八轮 coupled physical-H、闭图、reach 或 README 完成。

## 1. 原未通过上界的具体来源

原 `resume_n4/certify_q060_shared_r_tail_batch.py` 对一个完整 stage 使用常数包围 $w_0\pm d_w$，在 stage 24 中

$$w_0\simeq .08104234189476943,\qquad d_w\simeq .008239397771013441.$$

stage 24 / span 15 的原算子上界为 $1.5592122745872465\times10^{-4}$。其中第一 Gram 分量的固定 $w_0$ 合并项约 $6.5322517\times10^{-5}$，另付 $w$ 变化项约 $6.5329975\times10^{-5}$；完整高阶二次乘积余界只有 $3.2163189\times10^{-9}$。这是一个可具体消除的包围损失，原上界超阈值并不证明实际度量误差超阈值。

本条保留原所有线性 Fourier 项、所有低频二次项的精确合并，以及所有其余二次乘积的完整余界。`quadratic_mode_cutoff=12` 只选择哪些二次乘积显式合并，不截断场或遗失高模乘积。

## 2. 同一真实背景的严格 Taylor 包围

背景仍是 R58 的真实积分定义，使用同一 normalization 证书与全部 160 个字面校准常数。不是把 JS 求积 profile 当成真实背景。对原径向 quintic 的某个真实字面区间 $[R_0,R_1]$，先调用原 `local_background_cover`，以严格单调的真实 primitive 上下界证明原 source pieces 覆盖该物理半径区间。传入包围器的两个浮点半径已分别向外舍入，内部仍对原有理半径计算 Gram 多项式。

在该 source cover 内选取真实锚点 $x_*$，记 $R_*=r(x_*)$。从原 oracle 的 outward intervals 取得字面有理近似 $\widehat R_*,\widehat w_*,\widehat d_*$ 及严格误差

$$|R_*-\widehat R_*|\le e_R,\quad
|w(R_*)-\widehat w_*|\le e_w,\quad
|w_R(R_*)-\widehat d_*|\le e_d.$$

每个原 source piece 都保持原边界，并在其内部划分八个证明盒。原 oracle 给出 $r_x>0$、$w_x,w_{xx}$ 和 `r_xx_one_sided_hull`；因此

$$w_{RR}=\frac{w_{xx}r_x-w_xr_{xx}}{r_x^3}\quad\text{a.e.},\qquad |w_{RR}|\le B_2.$$

这里必须保留原绝对值 cusp 两侧的 $r_{xx}$ hull。原 $w_R=w_x/r_x$ 连续、分片绝对连续，故这个几乎处处的界给出 Lipschitz 估计及积分 Taylor 余项，不要求真实背景全局 C³。跨原 source 接口时使用所有相邻 pieces 的并集，不从某一侧导数外推。

取

$$L=\max_{i=0,1}|R_i-\widehat R_*|+e_R,\qquad
W(R)=\widehat w_*+\widehat d_*(R-\widehat R_*),$$

则整个区间内

$$|w(R)-W(R)|\le
\varepsilon:=e_w+e_dL+|\widehat d_*|e_R+\tfrac12B_2L^2.$$

证明是对 $w(R)$ 在真实 $R_*$ 使用积分 Taylor 公式，再分别支付锚点、函数值和斜率的近似误差；$L$ 确实包围到真实锚点的距离。代码中的 anchor 位于所用 source cover 内。

## 3. 完整 Gram 计算及原门

按原核的同步竖向符号约定，尾场写作旋转背景加完整有限扰动 $V$；目标度量为

$$g=(1+w(R)^2)dR^2+R^2d\theta^2.$$

Gram 残差中只有两个线性项显含 $w$：$2w\,\partial_RV_z$ 和 $w\,\partial_\theta V_z$。新入口把原两个常数乘法改为与精确有理一次多项式 $W$ 的乘法；将对应频率合并后，以 Bernstein 系数包围整个径向区间。再以 $2\varepsilon\|\partial_RV_z\|$ 和 $\varepsilon\|\partial_\theta V_z\|$ 支付真实 $w-W$。其余项与原 Gram 核逐项相同。

设由此得到的三个非负分量界为 $A,B,C$，其中混合项与角向项已分别除以径向下界 $R_0$、$R_0^2$。因 $1+w^2\ge1$，原来的严格算子上界 $\max(A,C)+B$ 仍成立。门继续使用精确 $1/10^6$，没有放宽。

在真实输入上把新 $W$ 特化为原常数 $w_0$、余界特化为原 $d_w$ 后，`metric/components/merged/quadratic_remainder` 与原核的全部 exact fractions 逐项相等。该核对只验证这两处代数替换恢复原式，不代替上述 Taylor 证明。

## 4. 本次真实返回

实际执行入口 `scripts/resume_20261128/tail/tail_metric_true_w_taylor.py`，TTY `90195`，exit 0。参数为 `--stage 24 --spans 15 --max-depth 0 --quadratic-mode-cutoff 12`，完整命令及输入、输出 SHA 见同名小 JSON。原实际几何 bundle 为 `3b312be557d67cda05624e41d46266925fbe3836c48759c613ede6cf52c70b98`，原 full-H packet 为 `81f6eb0f5c253c13d6aaaa320adbf95bfc6c59dca7a45b888bacd7b6991b770c`。

| 本次实际连续量 | 向外上界 |
|---|---:|
| $e_R$ | $9.818352081798818\times10^{-14}$ |
| $e_w$ | $1.6816625127357517\times10^{-18}$ |
| $e_d$ | $4.715091262288298\times10^{-12}$ |
| $B_2$ | $145.64525039406522$ |
| $L$ | $5.7306371679484\times10^{-5}$ |
| $\varepsilon$ | $2.3915176555402023\times10^{-7}$ |
| $A$ | $7.148453212086667\times10^{-9}$ |
| $B$ | $1.4945870152615249\times10^{-9}$ |
| $C$ | $1.2587066775760945\times10^{-10}$ |
| $\max(A,C)+B$ | $8.643040227348194\times10^{-9}$ |

核心证明循环实测 5.779301260001375 秒；此数不包含输入总验证与常数特化核对，不能称完整进程墙钟。只有一个原 span，全部端点共同二阶 jet 与全谱身份仍由原 validator 核验；证明区间细分次数为零。

新脚本可对未通过的原 span 做精确仿射证明细分；它只重写证明坐标，保留原 quintic 函数及其对物理 $R$ 的导数。已通过的原证书、真实有限尾场和活跃全尾运行均不覆写。后继按实际原证书选择未付的 metric 区间，并分别保留原几何、曲率和 placement 结论的适用条件。

## 5. 已实际扩展到 stage 16 与 24 的完整覆盖

后继仅补 stage24 尚未付的0–14，并另对 stage16 的全部16个原span执行；旧stage24/span15未重算。现在这两段各自全部16个原span已准确覆盖，向外最大metric界分别为 `1.3930787705095377e-8`（stage16）和 `8.643040227348194e-9`（stage24）。root核44个实际引用SHA与全部32叶的exact Gram分量有理数、原span的 `[0,1]` 单覆及向外浮点包含，未重算Gram多项式。

原v1新入口没有内联旧certifier的全部 selected-stage 容器门。因此这两个具体结果另由[实际来源补核](2026-11-28-tail-manifest-count-and-selected-gates.json)重新执行原 spectrum/stage/status/physicalParameters/mapHash/mean 门，并与原同SHA证书及三份Taylor summary绑定。补核只查身份，没有重算metric。后续通用v2将独立内联这些门；旧v1源码和已出实际结果不覆写。这里的数学结论仅在已实际补齐门的这两个stage上成立，不泛化为任意外部输入已通过验证。

同一sidecar还按真实完整manifest更正总span为18,460：28段有原exporter已有的额外stationary节点。原场、每段节点、共享两jet、所有当前数值证书均不受这一摘要计数更正影响。
