# 新输入：正确 Phi 两个原权矩阵的 QQ 已付因子最小赋值提取

日期：2026-11-28。会话：Astra-ISP-8542378f-20261127。

**尚未执行。** 这是两个已定义原 Sylvester 矩阵上的新整除输入：逐条目在 QQ 多项式环中支付旧权因子的真实幂，再比较商矩阵。旧未归一矩阵的双轴行列式、gcd、最高矩阵门均不重跑；不删除任何模 gcd 因子。最后范围只由唯一首次真实返回决定。

## 1. 已付原支持和当前未付内容

既有
$$
F=\det S_{12}\in I_6,\qquad
G=\det S_{14}\in I_6+(Vlow)
$$
分别来自真正原 $\lambda$ 的两个六次式和真正原 $t$ 的六次式、完整 Vlow 八次式。两个固定矩阵的伴随身份保所有最高系数为零的纤维。

上一条唯一实际 run46156015273 / job141012730204 已付
$$
\deg F\le444,\quad (\deg_uF,\deg_QF)=(402,222),
$$
$$
\deg G\le730,\quad 642\le\deg_uG\le643,\quad \deg_QG=371.
\tag{1}
$$
在预定 $p=1009,Q=2$ 与 $p=1009,u=2$ 上，完整模 gcd 的次数分别为 41 和 68；没有支付 QQ 无公共曲线。特征零共同 gcd 仅有双次上界 $(41,68)$。

准确来源：
[完整 Vlow 第二支持及公共曲线界](../results/R150-appendix-unit211-Phi-zero-corrected-complete-Vlow-second-weight-support-and-common-curve-bidegrees.md)。

本次不利用模 gcd 的任何猜测因式。新的目标是在完整原矩阵条目中证明
$$
F=U_F F_*,\qquad G=U_G G_*,
\tag{2}
$$
其中 $U_F,U_G$ 必须是已付纯权因子的明确正幂乘积。只有 (2) 真正返回后才研究新的商支持 $F_*,G_*$。

## 2. 事前固定的原权因子

记
$$
s=u-1,\quad \delta=1-Q,\quad K_w=Q+4s,
$$
$$
L=Q-2s(u-2),\quad \ell=L/Q,\quad m=u-\ell,\quad
M_n=2uL-L^2-u^2Q.
$$
本次严格按以下顺序处理：

1. $Q$；
2. $u$；
3. $u-1$；
4. $\delta$；
5. $K_w$；
6. $L$；
7. $M_n$；
8. $2L-Q$；
9. $Q+2u-4$。

它们全部是当前正确 Phi、distinct singleton、物理 $D\ne0$ 图的已付权单位。特别地，
$$
2\ell-1=(2L-Q)/Q,\qquad
m=(u-1)(Q+2u-4)/Q.
\tag{3}
$$
两个 (3) 在源码按原变量完整返回。$u$ 来自独立原零 base-mean 排除，$2\ell-1$ 来自正确整 ell-half 排除；$m$ 的旧完整原等权来源见
[静态追溯记录](2026-11-28-unit211-Phi-corrected-equal-weight-m-unit-static-provenance-8542.md)。
其余为原恢复图权单位。本门只在当前已付 $m$ 的物理 Phi 权图上使用最后一个因子；它是该图的进一步纯权局部化，不改写十三生成论文所用的未几何局部化系数环。

不引入 $\theta,\alpha$、任何新斜率或新最高系数，也不需要重新调用 A/B 零支定理。每个因子先乘非零有理常数化成 primitive 整系数多项式 $h$，该常数等式逐项返回；这只改变有理单位，不丢权零面。方法不要求 $h$ 不可约，只使用其真实整除幂。

## 3. 完整条目整除阶与最小完美匹配

对当前矩阵 $S$ 及一个固定 $h$，每个非零条目实际计算
$$
v_{ij}=\max\{r\ge0:h^r\mid S_{ij}\text{ in }\mathbb Q[u,Q]\}.
$$
每次成功短除和最后一次非零余式均完整乘回。零条目标为禁止匹配边，不能当成零次非零条目。

随后在整数成本 $v_{ij}$ 上求最小权完美匹配，同时返回整数对偶
$$
a_i+b_j\le v_{ij}
$$
对每条非零边成立，并返回
$$
K=\sum_i a_i+\sum_j b_j
=\sum_i v_{i,\pi(i)}\ge0.
\tag{4}
$$
这和此前用于 QQ 次数上界的最大次数匹配是不同的数学目标；本次不重跑旧上界匹配或最高矩阵。

若 $K=0$，原矩阵原样保留，只记本方法未提取该因子。若 $K>0$，定义
$$
M_{ij}=h^{-a_i-b_j}S_{ij}.
\tag{5}
$$
$a_i+b_j\ge0$ 时，源码真实精确除法并乘回；负指数时只乘旧已付多项式的正幂。每个新条目仍在 $\mathbb Q[u,Q]$ 中。所有条目的整系数也逐项核对；原 $S$ 整、$h$ primitive，Gauss 整性保证合法整除后的商仍整。

在 $\mathbb Q(u,Q)$ 中由行、列尺度直接得到
$$
\det S=h^K\det M.
\tag{6}
$$
两边又都是 QQ 多项式，所以 (6) 是全多项式身份，包括 $h=0$。(5) 的全部条目返回就是这一固定行列式身份的完整来源，不需要展开两个巨大的行列式。

顺次对 §2 全部因子做 (4)–(6)，给
$$
U_F=\prod_hh^{K_{F,h}},\qquad
U_G=\prod_hh^{K_{G,h}}
$$
及 (2)。程序只保存这个明确的因式定义，不展开高次 $U_F,U_G$。在原已付权局部化上它们为单位，所以
$$
F_*\in I_6,\qquad G_*\in I_6+(Vlow).
\tag{7}
$$
所有未付首项的整零纤维保留。

$K$ 只是一项实际证明的整除下界，可能小于真正行列式的阶数。即使 $K=0$ 时模 $h$ 的矩阵奇异，也不从函数域主元或“看起来还有重数”推更高整除；余因子全部保留。本源没有 DVR 高阶消去尾段。

## 4. 商支持的 QQ 次数，不重复旧最高门

两个原支持已知非零，所以 (2) 自动使商支持非零。对任一坐标，多项式乘积的次数相加，故
$$
\deg_uF_*=402-\deg_uU_F,\qquad
\deg_QF_*=222-\deg_QU_F,
\tag{8}
$$
$$
642-\deg_uU_G\le\deg_uG_*\le643-\deg_uU_G,
\qquad
\deg_QG_*=371-\deg_QU_G,
\tag{9}
$$
负的保守下界按零截断。总次数上界同样是
$$
B_F=444-\deg U_F,\qquad B_G=730-\deg U_G.
\tag{10}
$$
因子幂的总次数和坐标次数由各个真实原因子直接相加。没有展开 QQ 行列式，也没有重新计算 (1) 的任何最高矩阵。

只有两个矩阵各自至少有一个实际正幂提取，本源才进入新商矩阵的双轴比较。若任一矩阵的全部 $K$ 都为零，则记录两者已成的全部 QQ 精除与次数界后立即结束，不计算该未改变矩阵的旧行列式，也不增加新尝试。

## 5. 只对新商矩阵做固定双轴返回

唯一素数仍是 $1009$，唯一两个切片仍按事前顺序
$$
Q=2\ (u\text{ variable}),\qquad u=2\ (Q\text{ variable}).
$$
不根据因子、次数、秩、gcd 或目标改点、加点或换素数。

源码从新商矩阵的整条目直接形成完整 $\mathbb F_{1009}[x]$ 固定行列式。Bareiss 每次除法乘回，之后两个新多项式的完整扩展 Euclid 乘回 gcd。没有从旧模 gcd 中删除任何因子；即使结果在模环里等于某个旧 gcd 的商，也只有 §3 的 QQ 来源允许它成为本次输入。

新的 $F_*$ 实际模次数若达到 (8) 的 QQ 真次数，便保留该坐标的全局次数。$G_*$ 的 $Q$ 方向同理可用 (9)；$u$ 方向仍有未付一阶差，不强求某个预想次数。

在每个方向，只有实际模 gcd 为一且至少一个新商支持保全局次数，才支付该方向上没有正坐标次数的 QQ 公共因子。原因与上条相同：在固定局部 Gauss 整环内，保度多项式可首一化；它的首一公共因子整性保证约化仍保次数并整除两个模式。

两个方向都支付后，才宣布两个新支持无 QQ 公共曲线，并给权点 Bezout 上界 $B_FB_G$。第一方向不能代替第二方向对纯 $Q$ 内容的控制。即使给有限权点，也不宣布物理图为空或给未经恢复的完整规范点数。

若仍有非恒定 gcd，在保度条件满足时可以记录对应 QQ 公共因子的次数上界；否则只保全部未付内容。无论哪一种，所有未付纯权零纤维都保留。

## 6. 唯一参数再生边界及依赖

本源只从上条冻结源
[2026-11-28-unit211-Phi-zero-corrected-Vlow-second-weight-support-two-axis-comparison-8542.py](2026-11-28-unit211-Phi-zero-corrected-Vlow-second-weight-support-two-axis-comparison-8542.py)
读取必要参数。完整 SHA256：

060d321f863b93ef8d1825ca3dc86d41f12573101257b1ace3c3a6ac8e24e2f7。

截取位置严格在 def sylvester_models(pair) 之前，共 10491 字节，SHA256：

7313f0bda9d11c57e91e51019b7fe2fdc4c2d3442638df54d1355539a71bf678。

AST 移除旧顶层资源/时钟设置和日志，保留完整四依赖 SHA 检查、唯一参数 SHA 及精确算术定义；原四参数只再生系数身份。它不构造旧固定矩阵的总次数审核段，也不进入旧最大匹配、最高矩阵、未归一固定轴行列式或旧 gcd 门。

另只导入五个算术函数定义：axis_degree、modular_polynomial、poly_profile、polynomial_det、xgcd_return。最后两个仅用于本次新商矩阵；没有调用旧主循环。必要权量 L、Mn、gg 从其嵌套真 t-Gram 定义环境中读取，不混淆外层参数命名。

共五份源码依赖，全部仅在 runner 临时目录读取：

| 依赖 basename | 全源 SHA256 |
|---|---|
| 2026-11-28-unit211-Phi-zero-corrected-Vlow-second-weight-support-two-axis-comparison-8542.py | 060d321f863b93ef8d1825ca3dc86d41f12573101257b1ace3c3a6ac8e24e2f7 |
| 2026-11-28-unit211-Phi-zero-corrected-t-complete-Vlow-two-original-cofactors-8542.py | 0800a0f6ba0cad4cc4ddc7a592525c198bcc213bfa36df568ec0e9301b8f4335 |
| 2026-11-28-unit211-Phi-zero-corrected-two-sextics-fixed-lambda-resultant-support-8542.py | 39631a64da054107209d296765b755e2fe25a685f5734cb5607165dd39100b7b |
| 2026-11-28-unit211-Phi-zero-corrected-whole-original-I6-fifteen-by-three-8542.py | 84e0efcc19a0274d571484b187b7b155c81ebf255e40a39c38ac13a03f911cf0 |
| 2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py | 5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7 |

第二层旧 fixed12 前缀的资源上限同为 1 GiB，所有嵌套 alarm/setitimer 始终受本源最初绝对截止钳制；非正计时调用也不会关闭外层计时。源码不访问网络，不读取或保存旧大系数载荷。

## 7. 冻结身份、预算和返回边界

新源：
[2026-11-28-unit211-Phi-zero-corrected-QQ-paid-entry-minimum-assignment-two-supports-8542.py](2026-11-28-unit211-Phi-zero-corrected-QQ-paid-entry-minimum-assignment-two-supports-8542.py)。

冻结 blob：b0ef31bafd35a2e6f9e82efdf25f99d19824c7b8。

SHA256：72ab1c093136233e35f72a15697dc84dc65ae637fc16c031da0535c61d98a64a。

UTF-8：17095 字节。首次预算严格 **120 秒 / 1 GiB，外层 135 秒**。

输出仅保每个因子的次数/profile、准确整数对偶与 K、全部条目乘回状态、商矩阵 profile、新固定轴结果和小计数。没有 QQ 二元行列式展开、系数载荷或缓存。

源码尚未执行；旧 2179 草稿只作执行前边界修正，没有运行、不是实际失败。本文不预言任何 K、残余 gcd 或有限性。若资源触界，只保最后完整的原条目整除身份及其准确结论，不加时、加内存、换顺序、换点或重跑同一目标。
