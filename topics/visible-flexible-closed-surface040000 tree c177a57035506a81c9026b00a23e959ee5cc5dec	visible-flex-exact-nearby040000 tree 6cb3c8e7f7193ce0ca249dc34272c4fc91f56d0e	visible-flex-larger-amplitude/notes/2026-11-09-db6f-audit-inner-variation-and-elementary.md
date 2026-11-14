# 内有限尾 A 的临界值精算及初等区间组件独审

2026-11-09，`/root/independent_geometry`。内 A 算法是本文作者新实现，待未参与者独审；tight exp/log 组件由 tail_theory 编写，本文作者已独立全文审查通过。下文始终使用已冻结有限几何系数和精确解析 source 归一化，不使用 source Gauss 值作为真积分。

## 1. 认证对象和输出

`scripts/db6f-audit-inner-warp-variation.py` 对固定有限 source 的 cells $1\le n\le159$ 认证

$$A_{inner}=\sum_{n=1}^{159}\int\left((1-\chi)r'_o
  +\frac{\chi|w_x|}{6(1+w^2)^{3/2}}\right)dx.$$

这里唯一的 $\chi\ne1$ 区域是 cell 159 的第一个 protected port，其 $j_0=1$。cell 0 不包含在本输出中，故可与 tail_theory 的 cell 0 独立精算直接相加。

正式 checkpoint SHA256 为 `d23b03e4ce5cd7aaf4ac9d1134f8a23ee274be3a1d0a0192a7b294f1195e43f0`，冻结 160 个有限 source 校准数的表 SHA256 为 `bcfaba00aec62290b5b29432836c9e76ef6cf0d582b06c046677b0f8688ca9f4`。代码核对全部参数盒、校准表的值与 hex、深有限控制为零、有限 pulse level 范围及保护端约定。

当前脚本 SHA256 为 `aaa0c5da752d955a786c9ef8b563c218f5ad5988cdc35886435a5768744808ab`。运行（本题目录）：

```sh
python scripts/db6f-audit-inner-warp-variation.py \
  --checkpoint notes/2026-11-09-db6f-prefix-flat-v17v18-coupled-m8-q10-fine_tail_0017.json.gz \
  --calibrations notes/2026-11-09-db6f-tail-finite-source-calibrations.json \
  --out notes/2026-11-09-db6f-audit-inner-warp-variation.json \
  --tail-start 40
```

包含全部剩余项的结果为

$$A_{inner}\in[0.0706548168707253,\ 0.07065481687073313].$$

区间宽约 $7.83\times10^{-15}$。这些端点是经过向外舍入的 binary64 数，而非四舍五入显示后用于比较的十进制。source bookkeeping 的旧 Gauss 值略在此区间之外，差约数个 $10^{-15}$；该数只作数值诊断，未被强迫纳入或冒充同一真积分。

## 2. 无求积的临界点公式

在一个 source transition 上，吸收 valley control 后，raw log slope 为

$$z(x)=C+\Delta S(x)-\lambda x,\quad
S'(x)=30x^2(1-x)^2,\quad\lambda>0.$$

若 $\Delta\le0$ 或 $\Delta(15/8)\le\lambda$，则全段单调。否则有且仅有两个临界点。置

$$u=\sqrt{\lambda/(30\Delta)},\qquad
x_- =\frac{2u}{1+\sqrt{1-4u}},\qquad x_+=1-x_-.$$

这是二次方程的稳定等价公式，避免近零根的减法相消。所有常量与根都用向外区间包围；程序要求两根与端点及 $1/2$ 严格分离。若符号或重根判定不能由区间确定，程序直接失败，不猜测根数。

常值 smooth cap 是 raw log slope 的单调函数，因此在两个相邻 raw 临界点之间，$f(w)=w/\sqrt{1+w^2}$ 仍单调。故该 profile 的积分精确为

$$\frac16\sum_i |f(w(x_{i+1}))-f(w(x_i))|,$$

其中节点为两个端点及存在的两个临界点。不存在数值积分离散误差，只剩这些有限函数值的区间宽度。若两端都已严格处于完全 capped 分支，它们是同一个精确 binary cap 常数，差严格为零；代码按此恒等式处理，避免把同一个常数拆成两个独立误差。

对于实际 cells 1–39，共 351 个 profiles 中 78 个有两个内部临界点，其余没有。代码不按采样结果数极值，而由上述解析判定得到。

## 3. source 公式和剩余部分

程序用

$$\delta_n=\delta_0 2^{-n},\quad \eta_n=\delta_0c_0 2^{-3n/2},$$

$$after_n=3\delta_n+\frac{6\eta_n2^{-3/2}}{1-2^{-3/2}}$$

计算每段的解析 source log 半径；$\sqrt2$ 与 $\sqrt{12}$ 都用已审的向外平方根包围。归一化 raw log slope 化简为

$$\log w_{cut}+\frac7{\sqrt{12}}(T-d(x))
-\frac{11}{4}\log2-\frac{7n}{4}\log2-\log\delta_0+v(x).$$

这与固定解析 source 的 $\epsilon\delta_n^{11/4}e^{v(x)}/(\delta_n r_o^7)$ 严格相同；没有把 source `Math.log` 的舍入值当作解析对数。

对剩下的 cells $40\le n\le159$，前一正性证明已给

$$\operatorname{TV}f(w)\le5W_n,\qquad W_n=1280\,2^{-7n/4}.$$

用 $2^{-7/4}<1/3$，该 curvature-width 余项严格小于

$$\frac56\sum_{n=40}^{159}W_n<\frac{1600}{2^{70}}.$$

保护端额外旧径向项则有

$$\int(1-\chi)r'_o dx\le\frac{4}{75}\eta_{159}
<\frac1{48000\,2^{238}},$$

因为整个旧 source 半径小于 $4/25$、$\sqrt{12}>3$、$\delta_0c_0\le1/2560$。这两项都是显式正有理数，加入总上界；总下界只使用已精算的 cells 1–39。因而没有遗漏 cell 159 的混合区域。

## 4. tight exp/log 组件的独立审查

`scripts/db6f_tail_interval_elementary.py` 的本次 SHA256 为 `88400506e7b660c328e03cb6547fe9056d2cde00963ebb16890d054169805145`。全文独立审查 **PASS**。

对每个精确 binary 输入 $x$，指数例程把它先转为 Fraction，以精确比较保证 $|x/2^k|\le1/8$。18 阶有理 Taylor 和 $\frac87(1/8)^{19}/19!$ 余项包围该指数值。每次平方前后，都把有理上下端点分别向下、向上取整到 $2^{-200}$ 网格；正区间平方保持包围。最后 `qbounds` 比较精确有理数与 binary64，取得真正向外端点。`libm log2` 只用于猜初始缩放次数，不能决定余项是否合法。

对数例程通过精确二进 frexp 分解得到 $m\in[1,2]$，令 $z=(m-1)/(m+1)$，使用

$$\log m=2\sum_{j=0}^{47}\frac{z^{2j+1}}{2j+1}+R,\qquad
|R|\le\frac{2|z|^{97}}{97(1-z^2)}.$$

负的二进指数乘 $\log2$ 时正确交换上下端点。整个级数与余项在 Fraction 上计算，不受浮点求和误差影响；输出 interval wrapper 利用 exp/log 的单调性处理输入区间。

该模块复用的基础 I 算术后端 SHA256 为 `e1870297b172a372bbf889f9714249d4997171db7f53dbb3ec6195a5de2c642d`，此前已独审。不同 import 实例可能生成不同 I 类，因此本实现统一使用 tight 模块提供的 I，避免混用对象。

## 5. 与完整任务的关系

这份区间可以缩紧精确径向 $\alpha=(L-A)/B$，但它本身不认证 $B$、真实背景与保存数值 geometry 的误差、任何非线性尾或完整曲面。后续相同物理 $g$ 的不同 M/RK 求解可共用同一背景区间；换了有限 source 常数或控制值就必须重新绑定并计算。
