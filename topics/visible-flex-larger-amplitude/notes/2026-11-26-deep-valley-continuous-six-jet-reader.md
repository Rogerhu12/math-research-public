# R690 新固定标量的完整连续六 jet 与分批 first 消费者

**状态：解析包围接口已证明，完整源码已实现；本入口尚无科学返回。** 本文只扩展 R674 的标量输入与诚实身份接口，不重复 R650/R672 的形状算子证明，不新增一个已通过的 R666。源为 `scripts/resume_20261126/deep_valley_interval.py`，SHA-256：

`5ec4ebc2975bb35e3374911cca34de53d8b5638038d7b63451af8042fb31f1d6`。

已做源码 AST/compile 和接口静态阅读，未在本地运行科学计算。后续真实返回须另记 run、完整命令、实际 bundle 与输出 SHA。

## 1. 新 canonical 与旧纯公式的边界

输入必须是 `deep-valley-fixed-scalar-fullclosed-lift-v1`，实际 factory 为 4ae012…、实际 R690 标量为 e091f6…、原完整物理/J/J* 源为 R671 的 2e0219…。读取器核对新模型的完整 scalar definition、当前 bundle/node/observation SHA、实际 mesh/$M$、固定 $g_n$ 声明、同一 $\lambda=1$ 和精确 $\eta$ 端点。普通旧 R674 reader 仍拒绝此新模型。

已有径向 Bernstein、全有限角模和完整 analytic lift 公式只依赖实际 $q$、精确符号节点、$S,R,H$。本源在 runner scratch 写明确 schema 的 `explicit-new-scalar-radial-view.json`：

- $S$ 为同一个原准确值，$R$ 为新 R690 的完整包围；
- `scalar` 中原曲率律参数仅用于未改的前缀；
- 旧 `true_a_stage_boxes` 留空；需要的前缀 anchor 从原准确 oracle 重新得到；
- 新尾全部由本源的 new profile 方法提供，不用原 out-ramp 多项式；
- view 具有自身 schema、source、实际新 node/model SHA，不冒称原 scalar/canonical 证书。

节点生产者可为首 prepare 的 factory，也可为真正的精化器。`--node-producer-source` 显式给该源，核它的实际字节 SHA 等于新 node report 自报值并记录；默认用首 prepare 的 4ae factory。生产者不被导入或执行。几何数学身份仍由读取器独立核验的新完整 canonical、scalar 和实际节点决定。

## 2. 新连续标量包围的完整证明

记 $d$ 为 R690 的原准确 out-width，$t=S-s$，$x=t/d$。新尾满足

$$
a_n(s)=R_n+\int_0^t\cos\beta(v)\,dv,\qquad
I_n(s)=\int_0^t\sin\beta(v)\,dv.
$$

同一分割包括原 scalar 分段、原 $\chi$、两个 $\eta$ 端点和新增的 $S-d/4$、$S-d/8$、$S-d\epsilon$。各端点均为精确 $\alpha S+\beta$；每个原 cell 与这些点相交，再按所选 dyadic 参数分片。没有以浮点中点决定拼接的哪一侧。

### 2.1 未改部分

在 $s\le S-d/4$，$a_n=a_{\rm old}$，而

$$
I_n(s)=I_{\rm old}(s)+
\bigl(Z_n(S)-Z_{\rm old}(S)\bigr).
$$

因此 R674 的同一完整 Taylor 微分公式和原曲率律余项仍适用。唯一常数项使用新 oracle 的 $I_n$ anchor。它不是沿用原场的 $H-I_{\rm old}$，也没有把自由 $H$ 相关量当作可免费消去的公共项。

非参考 active 区内的固定目标 $a_n$ 由未改的准确 quintic/前缀包围给出。该区处于新修改尾之前。

### 2.2 有限新尾

在不跨 cutoff 的 $x\ge\epsilon$ 有限分片，R690 的整数 jet 给出阶乘归一化的 $\beta$ 关于 $x$ 的系数。换成物理 $s$ 的第 $j$ 个系数，乘

$$
(-1/d)^j.
$$

用完整 sin/cos jet 递推求出 $-\cos\beta$ 和 $-\sin\beta$ 的系数，以新准确 $a_n,I_n$ anchor 积分，得到一对共同次数 $n$ 的 Taylor 多项式。其一、二阶多项式直接由这同一 power polynomial 微分，再转成局部 Bernstein 控制点；不是对 interval anchor 做差分。

设完整分片上的 $\beta$ 物理导数界为 $D_j\ge|\partial_s^j\beta|$。整数 jet 的第 $j$ 个区间须乘 $j!/d^j$ 才成为 $D_j$。定义

$$
B_0=1,\qquad
B_j=\sum_{k=1}^j {j-1\choose k-1}D_kB_{j-k}.
$$

由 $\partial_s e^{i\beta}=i\beta'e^{i\beta}$ 的逐阶 Leibniz 公式及 $|e^{i\beta}|=1$，有

$$
|\partial_s^j e^{i\beta}|\le B_j.
$$

所以 $a_n$ 与 $I_n$ 的第 $n+1$ 阶导数均不超过 $B_n$。若该分片到共同 anchor 的准确距离至多 $r$，那么阶 $j=0,1,2$ 的余项同时不超过

$$
e_j=\frac{B_n r^{n+1-j}}{(n+1-j)!}.
$$

所有 $D_j,B_j$ 与余项先由 Fraction/整数区间向外求得，再向外转换为 IEEE 区间。拼接处仅需 $C^2$；高阶 Taylor 在各已分开的闭侧分片上使用相应单侧解析公式及有界余项，不假设跨 cutoff 的高阶光滑性。

### 2.3 整个无限尾

在 $0\le x\le\epsilon\le1/8$，R690 给出包含全部无限振荡的

$$
|\beta|\le b_0,\qquad |\partial_t\beta|\le b_1.
$$

直接取低次数准确主部

$$
a_{\rm poly}=R_n+t,\qquad I_{\rm poly}=0.
$$

由 $|\sin y|\le|y|$、$0\le1-\cos y\le y^2/2$，逐阶误差为

| 阶数 | $a_n-a_{\rm poly}$ 的界 | $I_n-I_{\rm poly}$ 的界 |
|---|---|---|
| $0$ | $t_{\max}b_0^2/2$ | $t_{\max}b_0$ |
| $1$ | $b_0^2/2$ | $b_0$ |
| $2$ | $b_0b_1$ | $b_1$ |

第二行使用 $a_s=-\cos\beta$、$I_s=-\sin\beta$；第三行使用 $a_{ss}=-(\partial_t\beta)\sin\beta$、$I_{ss}=(\partial_t\beta)\cos\beta$。实现为 $a_n$ 与 $I_n$ 分别传递这两组余项；水平 $f$ 只支付 $a_n$ 的误差，竖直 $k,z$ 只支付 $I_n$ 的误差。兼容诊断字段中的逐阶最大值不参与这两个实际物理误差预算。准确 $R_n$ 的盒已经包含在主部的 Bernstein 控制点内，不漏其不确定性。

这覆盖从 $\epsilon$ 一直到精确 cap 的整个闭区间，不在某个最小正 $t$ 停下，不将剩余振荡取零。$t=0$ 的三 jet 给出准确平盘的 $C^2$ 接口。

对整个替换区 $0\le x\le1/4$，同样的低阶包围也成立，只需改用 R690 已证的完整界

$
b_0=A\,29/4096,\qquad b_1=35211/65536.
$

这给出一个处理有限尾的有效后备包围。有限区间中 $x^{-4}$ 的振荡可能使高阶 interval Bell 界很宽；若同阶 Taylor 余项未同时优于上述两组低阶余项，源码返回整个有效的 $R_n+t,0$ 包围，并分别支付 $a,I$ 的误差。它不改精确 profile、不删振荡、不重新拟合输入。使用同一主部及各阶真实导数误差的 Bernstein 包围仍合法。高阶 Taylor 真正更紧时保留原 Taylor 包围。

对 first 所需的水平分量，这避免把竖直的 $b_0$ 误差误灌成水平误差：$a_s$ 的准确余项为 $b_0^2/2$。这是实际字段包围的解析改善，不是请求额外精度试验或新验证门。

### 2.4 完整物理六 jet 和固定目标

独立的新 `profile_controls` 按原完整代数调用上述新多项式，按原完整 Leibniz 公式构造

$$
f=\eta a_n,\quad h=\eta,\quad k=-\eta I_n,\quad z=hH+k.
$$

阶 $j\le2$ 的乘积误差支付

$$
\sum_{\ell=0}^j {j\choose\ell}
\|\eta^{(\ell)}\|_\infty e^a_{j-\ell}
\quad\hbox{或}\quad
\sum_{\ell=0}^j {j\choose\ell}
\|\eta^{(\ell)}\|_\infty e^I_{j-\ell},
$$

分别用于 $f$ 和 $k,z$；固定目标 $a$ 使用同一个 $e^a_0$。$z$ 先将 $H-I_n$ 组合后包围。全部 $F,F_s,F_\phi,F_{ss},F_{s\phi},F_{\phi\phi}$ 由原完整 radial/Laurent 公式读取；保留所有原有限 Fourier mode，保留 nonlinear analytic lift 的完整 Taylor/Laurent 尾。低模保留数仅控制包围效率，高模仍按完整尾支付，未从数学场删除。

`a_poly0/a_error0` 来自同一个新 $a_n$。metric mode 比较固定的 $ds^2+a_n^2d\theta^2$，没有移动均值投影。当前直接 interval Gram 入口可能宽；其返回只是实际全域上界，不伪称已具备 R657 的全部 numerator cancellation 精度。

## 3. 可实际运行的分批 first

在真实新 solver 返回后，令 `NEW_PREP` 为 prepare 输出，`NEW_SOLVE` 为该真实求解场目录；使用它自己的 profile carrier：

~~~sh
python "$TOPIC/scripts/resume_20261126/deep_valley_interval.py" \
  --repo "$REPO" \
  --bundle "$NEW_SOLVE/final.npz" \
  --observations "$NEW_PREP/observations.npz" \
  --node-report "$NEW_PREP/nodes.json" \
  --scalar-input "$ORIGINAL_SCALAR" \
  --reference-carrier "$NEW_SOLVE/exact-tail-lift-profiles.npz" \
  --mode first --cells all \
  --levels 256:1:24,512:2:32,1024:4:48 \
  --target-support .14 --target-diameter 4.198 \
  --scalar-tail-cutoff 1/8 --scalar-integral-tolerance 1e-18 \
  --scalar-admission-seconds 300 --admission-seconds 600 \
  --maximum-new-cells 1024 --scalar-degree 5 --radial-block 4 \
  --scratch "$WORK/deep-continuous-first" \
  --journal "$WORK/deep-continuous-first/journal.json" \
  --out "$WORK/deep-continuous-first/batch-0001.json"
~~~

其中 body 目标 $4.198$ 是 marked $D\le4.2$ 预算减去准确 $0.002$ 的数值细化请求；任何报告都仍以实际向外返回的 $D$ 为准。first 从当前新 bundle 重新计算全部 $D,L,E,W^2,\rho$ 和 support。不能仅因为 finite solver 幅度筛通过就预填这些值。

续批使用相同 runner journal 和新 out 路径；可显式 `--cells 0-127,160-191` 选胞，不重复已覆盖且已达当前目标的胞。journal 严核 source、当前 model/profile/bundle/node/observations、mode、所列角/径向 level plan、Taylor 次数、纯尾切点与实际 run/attempt。积分工作精度、panels 和 admission 预算不在 journal identity 中；这些工作参数不改变准确 profile，先前完整有效的同场包围可继续复用。每个 whole cell 自然完成后才决定是否继续接收下一个，立即保存该完整结果。预算退出不抛弃完成的胞，也不假装剩余胞已覆盖。

报告 schema 为 `R690-deep-fixed-scalar-continuous-interval-v1`。公开紧凑 summary 用胞号区间字符串与同列来源、$D,L,E,W^2,\rho,\sigma,K$；原 records 和 journal 仅在同 runner scratch。只有全部原胞都存在时 `complete_scope=true`。

对真实精化节点，另给 `--node-producer-source "$ACTUAL_REFINER_SOURCE"`。其余输入全部换为同一实际精化场的文件，精确 scalar/profile 仍固定不变。

## 4. 同场曲率与尚未完成的责任

curvature mode 必须消费这个新 reader 的同一 bundle、同一新 node/observations 的**完整** first 报告，既用于合法的实际 $E,W^2$ 下界，也用于实际直径：

$$
K_{\rm goal}=\frac{100}{3(D_{\rm actual}+1/500)}.
$$

源码从已返 $D_{\rm actual}$ 准确计算并向下取可用浮点目标；可显式要求更紧目标，不能用期望 $D=4.10$ 或旧场 $D$ 放宽。平盘曲率为零；R661 marker 的曲率、support 与非平面/欧氏形状见证仍另需同场消费者支付。完整 $K$ 返回也不自动写 reach 通过。

本入口不声称已有连续 metric 达标、固定-$g_n$ 精化收敛、marker/E3、README 完成或新非轴对称精确解存在。它提供这些真实后继计算所需的完整新输入消费者；当前未接近目标的场只按所需职责运行 first，避免重复昂贵的失败 upper。
