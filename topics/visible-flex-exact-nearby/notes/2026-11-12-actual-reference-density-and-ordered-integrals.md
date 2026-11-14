# 实际第 419 段：完整参考坐标密度与有序积分

2026-11-12，visible-exact-astra-f6a2。固定准确 δ₅、前腿第 419 段、
原有物理时间与负特征分支。本文记录实际连续证书，不将其转授给未算的其余段。

## 1. 完整准确输入与真正复合

前腿 raw、U/L 与 Q 已分别逐文件重建，并与冻结的旧文件 bytes/SHA 全部一致。
本段必要的完整 Bernstein 控制点、初值修正、原始 manifest、δ₅ 对象和根证书
另抽成 259998 字节小包：

`data/phase_ring_continuation/step5_forward419_exact_reference_package.npz.gz`，SHA256
`bf9e219a46415dc330a089d56be73eccb7329fe0e99b8fcdc1aa43f2fe9b8c04`。

抽取后逐数组 bitwise 核对，并把原始路径隐藏后独立重新装载；这不是只保存
几个节点。实际参考仍准确是原 $Y_4+Q a$，保留完整 8 个时间系数和 644 个
正标签频率。原 $Q$ 是选定的有限函数，不在此冒称真实 Jacobian。

写

$$
\tau=c+h_\tau u,\qquad
Y(u,x)=x/4+\sum_{i=0}^7u^iW_i(x),\qquad q=Y_x,
$$

其中 $x$ 的周期为 $2\pi$。$h_\tau$ 为原段**有符号**半长。完整物理场
$f=d\theta/d\tau$ 的本段准确有限近似记作 $P$，它的物理频率为 $4k$。
参考坐标密度和有限场密度分别是

$$
g=\frac{h_\tau f(u,Y)-Y_u}{q},\qquad
g_P=\frac{h_\tau P(u,Y)-Y_u}{q}.
\tag{1}
$$

$P(u,\theta)$ 是已经保存、准确重读的有限双重多项式，因此在两个变量上整。
只有 $g_P$ 的分母 $q$ 需要在它使用的外域上排除零点。原始物理场的定义域
不因此扩大。

## 2. 参考的完整复时间／复标签域

`fourfold_packaged_reference_bidisk.py` 先用完整 Laurent 乘积物化 $U+Qa$。
每个时间系数在标签边界的闭角格内，用全部频率和显式 Taylor 余项支付
$W_i,W_i'$。对同一角格保留 $q$ 的中心下界及其本格时间变化，得到

$$
\operatorname{Re}q(u,x)\ge
\inf_{\text{同格}}\operatorname{Re}(1/4+W'_0)
 -\sum_{i=1}^7R^i\sup_{\text{同格}}|W'_i|.
\tag{2}
$$

下边界由 $Y(u,x-is)=\overline{Y(\bar u,x+is)}$ 与整个时间圆盘的共轭
不变性支付；两边界进入整个带内部用调和最大／最小值原理。
不能在非实 $u$ 上错误地固定 $u$ 后直接共轭上下边界。

实际通过的部分域如下；每行是独立证明的域。

| $|u|\le R$ | 初值标签带 $S$ | $\operatorname{Re}q$ 下界 | $|\operatorname{Im}Y|$ 上界 |
|---:|---:|---:|---:|
| 1 | $1/128$ | 0.04604824937 | 0.00596578320 |
| 3 | $1/64$ | 0.04566124078 | 0.01312077512 |
| 6 | $1/64$ | 0.04512518908 | 0.01790542405 |
| 3 | $3/100$ | 0.04551194856 | 0.02125310383 |

较宽两行的物理像超过真实场已有的一些物理角带，只用于有限 $P$。
独立逐式审阅见 `2026-11-12-packaged-reference-bidisk-independent-audit.md`。

若 $S_Y$ 是本行的真实像域界，则有限 $P$ 的准确全系数给

$$
M_P(R,S_Y)=\sum_{i,k}|p_{ik}|R^ie^{4|k|S_Y},\qquad
M_{g_P}\le\frac{|h_\tau|M_P+\sup|Y_u|}{\inf\operatorname{Re}q}.
\tag{3}
$$

三组使用的 $M_{g_P}$ 安全上界约为 $42444.54$、$0.122953$、$21170.63$，
依次对应 $(3,.03)$、$(3,1/64)$、$(6,1/64)$。它们是完整有限模数，
没有用真实场模数冒充外域有限多项式的模数。

## 3. 有限密度的完整重建

实际运行 `fourfold_actual_reference_density.py`：

- 8192 个实标签节点，保留标签频率 $|k|\le3500$；
- 时间圆周半径 $\rho=5/4$，64 个时间节点，由 Schwarz 对称独立计算 33 个；
- 保留 48 个时间系数，320-bit 有向算术；
- 完整有限 $P(u,Y)$ 用局部角 Taylor 算法计算，目标尾误差 $10^{-42}$。

所有原 $P$ 频率都参加局部 Taylor 表。即使角 anchor 数少于频率数，先乘
原频率导数后准确折叠，所得是完整有限函数的节点值；没有物理角投影。
负标签频率共轭的是每个时间系数，不能在复时间上共轭已经求值的正频率。

时间 DFT 给

$$
b_i(x)=a_i(x)+\sum_{\ell\ge1}a_{i+\ell N_t}(x)\rho^{\ell N_t},
\qquad g_P(u,x)=\sum_{i\ge0}a_i(x)u^i.
\tag{4}
$$

由于采样圆在共轭下不变，$b_i$ 在实 $x$ 上准确为实数。因此先以有向实部
球支付所有节点误差，再选择实 dyadic 中点。其标签 DFT 继续支付算术球和
准确系数选择误差，零模定义为实数、负模定义为正模的准确共轭。
保存的有限密度 $\widehat g$ 因而在实 $(u,x)$ 上严格为实。

对 $K<N/2$，实节点 Fourier 折叠再保留 $|k|\le K$ 的算子在任意
$A_s$ norm 下为收缩：被折叠的原模式 $k+\ell N$ 满足
$|k|\le|k+\ell N|$，其权不会增加。因此时间 alias 按其独立解析域
支付一次，不再当成标签节点的独立白噪声。标签尾、标签 alias、时间 alias
和整个时间尾均有各自完整几何级数。每个独立外域分别给完整的有效上界，
可逐项选其中较小者，但不把不同外域拼成更大的未证 Cartesian 积。

在 $|u|\le1,|\operatorname{Im}x|\le1/128$ 上，实际完整预算为：

| 项目 | 安全上界 |
|---|---:|
| 节点与准确系数选择误差 | $1.494\times10^{-29}$ |
| 标签 Fourier alias | $1.904\times10^{-43}$ |
| 全部未保留标签频率 | $1.068\times10^{-27}$ |
| 折叠的全部时间 alias | $1.636\times10^{-37}$ |
| 全部未保留时间系数 | $2.897\times10^{-31}$ |
| $\|g_P-\widehat g\|_{A_{1/128}}$ | $1.083\times10^{-27}$ |

准确有限系数共有 12 个 gzip 分片、15469279 字节，单件均小于 5 MB。
manifest `step5_forward419_reference_density/manifest.json` SHA256
`93e840dec6bf290a212480ab46c3e01671be6b7aceb41f4e39b4976fbe0595ac`。
全部系数已经准确重读相等。

## 4. 真实场误差只在实时内域加入

实时工作标签带的完整参考像满足 $|\operatorname{Im}Y|<.005965784<.006$。
实际 δ₅ 同一段、同一根、同一 germ 的独立宽角／大时间预算给

$$
\sup_{|u|\le1,\,|\operatorname{Im}\theta|\le.006}|f-P|
 <2.326\,10^{-24}.
$$

这里 $u$ 可取实值以支付实际场的转授。由 (1)–(2)，

$$
\sup|g-g_P|\le\frac{|h_\tau|\,\varepsilon_{f-P}}
                              {\inf|q|}
 <1.557\,10^{-25}.
\tag{5}
$$

这个误差没有进入时间或标签 DFT 的节点球。总结果是

$$
\boxed{\sup_{-1\le u\le1,\,|\operatorname{Im}x|\le1/128}
        |g-\widehat g|<1.567\,10^{-25}.}
\tag{6}
$$

(6) 是一致复带误差，不在同一个边界带上额外冒称真实 $g-\widehat g$ 的
Wiener 误差。R72 使用的正是该一致范数，已经足够。

本段实际时间区间完整位于选定的一个共同 germ，没有未付跨 knot cap。
其他段须另付真正 moving crossing 的三重零费用及同参考复像条件。

## 5. R72 的实际输入和完整有限积分

设 $\widehat g=\sum_{i=0}^{47}c_i(x)u^i$。以
$M(u)=\sum_i\|c_i\|_{A_S}|u|^i+\varepsilon$ 同时控制 $g,\widehat g$。
准确积分 $\int_{-1}^1|u|^i,du=2/(i+1)$ 得

$$
A<4.809918032\,10^{-11},\qquad
E<3.133701748\,10^{-25},\qquad S=1/128.
\tag{7}
$$

完整第一积分只有偶时间阶：

$$
C_1=\sum_{i\ {\rm even}}\frac{2c_i}{i+1},\qquad
\|C_1\|_{A_S}<1.282944775\,10^{-12}.
\tag{8}
$$

第二个有序积分为

$$
G(u)=\sum_i\frac{c_i}{i+1}
                     [u^{i+1}-(-1)^{i+1}],\qquad
C_2=\int_{-1}^1\widehat g_x(u)G(u),du.
\tag{9}
$$

`fourfold_reference_density_integrals.py` 用 16384 个标签点准确容纳全部
$2K=7000$ 频率；每点用完整时间多项式相乘，并准确按偶次幂积分。
没有丢掉二次产生的高标签频率。首次大矩阵实现 exit137，已保存原源与
仅完成六个 off-grid 比较的报告，没有填入未完成的积分结果。
分块版本以准确 fixed-point 节点和逐行有向误差球转存，重新装载为包络；
这些误差完整进入后续乘积和 DFT。最终积分选 dyadic 系数的误差也独立支付。
分块版本已实际完成，28.870 CPU 秒、184.143 wall 秒；准确 dyadic 积分包
949015 字节，SHA256
`3fdb9ef31bb90f3e5a39e5c86ae01f5d4654c02bc417babd7a7eb3f7e154b6bd`。
完整二次项满足

$$
\|C_2\|_{A_{1/128}}<1.908\,10^{-23}.
$$

准确有限积分至保存 dyadic 的误差分别小于 $2.621\,10^{-107}$ 和
$1.503\,10^{-56}$。后一个界包含全部临时 fixed-point 转存、时间乘积和 DFT
算术球，没有把临时整数表当成原函数的准确节点值。

取内标签带 $\sigma=1/256$，由 (7) 可直接验证 $A\le(S-\sigma)/2$。
R72 给本段以 $X(-1,x)=x$ 开始的真实参考坐标流：

$$
\boxed{\sup_{|\operatorname{Im}x|\le1/256}
 |X(1,x)-x-C_1(x)-C_2(x)|<3.171\,10^{-25}.}
\tag{9a}
$$

其中三阶以上有序项的费用小于 $3.647\,10^{-27}$；剩余主要来自真实场
转授误差。实际完成报告
`notes/2026-11-12-actual-forward419-two-chronological-integrals.json` SHA256
`32b3e3561349742edd0fbac0ca721bbf12bb89fa0feec0b40b341f7d0d39c19e`。

六个 off-grid 检查使用实时间 $-2/5,1/3$、标签七等分点和上下 $1/128$
边界。直接完整物理 Laurent 求和与 $\widehat g$ 的完整求值差均小于第 3 节
连续误差；它们没有复用原时间圆或原8192标签网格。

跨多个实际时间段时，按 R72 必须同时累积

$$
C_1^{\rm new}=C_1+G_{\rm end},\qquad
C_2^{\rm new}=C_2+(G_{\rm end})_xC_1^{\rm old}+J.
\tag{10}
$$

不能在每段重置标签初值，也不能遗漏交叉项。完整两腿的 $A,E$、全部有限
校正及参数源仍待逐段支付；本段成果不表示完整返回或主课题已经完成。

## 6. 实际重放入口

在课题目录运行：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_actual_reference_density.py \
  --polynomial-dir data/phase_ring_continuation/step5_forward419_reference_density_replay \
  --out notes/2026-11-12-actual-forward419-complete-reference-density-replay.json
```

原实际密度报告 SHA256：
`69a25068ab98d5df10ef491725d0e3cd0b262d07e47f84eafec9fe28d73c9296`。
其运行使用 40.8079 CPU 秒、278.507 wall 秒。独立审阅另存
`2026-11-12-actual-reference-density-independent-audit.md`。

以上所有误差均属于同一个准确 δ₅ 对象；未向其他参数、完整 KAM、
全反馈逆、非线性同度量族或可见性/reach 自动转授。
