# q060 首 valley 4.625 背景的紧真积分与归一化误差

维护：Astra-held10-1b6d88ec-20261120 / n4_continue。2026-11-20 UTC。

## 新结论

本条沿用 [R58](../results/R58-q060-valley-background-height-and-curvature.md) 的同一个真实积分背景，保留全部物理参数及有限 binary 校准常数。改变的是严格积分算法：普通段用原函数总变差，正权项用带区间四阶余项的 Simpson；没有再跑尾 Newton。

最终源实际单核执行 exit 0，用时 30.8809 秒。所得真量满足下表；十进制再次朝外取整，复核用输出中的 exact fraction：

| 量 | 下界 | 上界 |
|---|---:|---:|
| $\int A$ | .1531783215514056 | .1531783215515935 |
| $\int B$ | .0006007677040647719 | .0006007677041961640 |
| $\int wA$ | .01936751142963024 | .01936751142963256 |
| $\int wB$ | .00002112502978936221 | .00002112502995542107 |
| 真宽度归一化 $\lambda$ | 161.1632545693437 | 161.1632546049038 |
| 完整真高度 $h(.3)$ | .02277208998335820 | .02277209001087430 |
| 变形后 cell0 内半径 $r_1$ | .1355213410572165 | .1355213410676365 |

当前工厂的字面归一化值为 $\lambda_J=161.16325458995925$。故

$$|\lambda-\lambda_J|<2.062\,10^{-8}.$$

工厂字面 heightSpan=.022772089996296273 与上述真实高度之差严格小于

$$1.458\,10^{-11}.$$

若保持真实 $A,B,w$ 及同一深端锚，只把 $\lambda$ 换成 $\lambda_J$，在同一源单元坐标中造成的全域相对度量差小于

$$4.955\,10^{-10}.\tag{1}$$

这是**只替换全局归一化常数**的分项预算，不包含 JS 每次 profile 查询的局部积分误差或 elementary-function 舍入，也不是整个非旋转尾图的度量证书。

## 1. 与 R58 相同的对象

输入为 R58 实际 dump 的 constants.json，SHA256 为

1a1bcd1679f9f3b507c19bed8f3a1310fda81ac16452ad164edef3e95d82dfc9。

其上游 q060-port SHA256 为

aa482f3bbd9506b90e307df72a7890f02f933338a4b3dec230f90b10765b09a5。

首六 valley 为 [4.625,2.8125,4.0625,5,5.25,4.0625]，rCut=.3、width=.25、wCut=.08、曲率分配 8、orientation=1、protectCell=160。有限校准根、prefix R 常数等按 R58 的实际字面输入固定；窗口、cap、$\delta_n,\eta_n$、三角/指数函数及积分随后按真实函数解释。

这仍不把有限校准根称为精确传输零点；也不把 JS 完整浮点 profile 等同于其真函数定义。这里只收紧 R58 已定义对象的积分界，R58 的全域背景曲率、cuff 和球包络证明继续适用。

## 2. 普通段的总变差恒等式

沿用 R58 的

$$
A=(1-\chi)j_0(r_o)_x+
\chi\frac{|w_x|}{8(1+w^2)^{3/2}},
\qquad
B=\chi\frac{(r_o)_x}{1+w^2}W.
$$

普通段 $\chi=1$。令

$$F(w)=\frac{w}{\sqrt{1+w^2}},\qquad
G(w)=-\frac1{\sqrt{1+w^2}}.$$

因为 $w>0$，

$$
\int A\,dx=\frac18\,\mathrm{TV}\,F(w),\qquad
\int wA\,dx=\frac18\,\mathrm{TV}\,G(w).
\tag{2}
$$

在用区间导数证明 $w$ 单调的子段上，(2) 直接变成两个端点值之差，端点用 60 位外向区间运算。若一个子段的导数区间含零，则二分；未判明的小盒使用

$$
0\le\int A\le |J|
 \sup_J\frac{|w_x|}{8(1+w^2)^{3/2}},
\qquad
0\le\int wA\le (\sup_Jw)\,\text{上一上界}.
\tag{3}
$$

只有已证小于误差预算的盒才按 (3) 收取。没有依赖原工厂 128 点 sign scan 声称已找到全部极值。

为防止端点依赖损失，$S_5'=30x^2(1-x)^2$ 以因式形式包围，第二至第四导数亦使用解析表达式；cap 一阶值用已知非负平滑权的凸组合包围。原先展开式在平端点过宽的问题由这个真实表达式改进解决，物理参数未变。

## 3. $B,wB$ 和外 port 的验证 Simpson

在每个原始九段单元内，基础 log slope 是多项式、soft cap 为分段多项式，且 cap 在切换点为 $C^4$。外侧 cut-preserving 混合也是显式多项式组合。$B,wB$ 以及最后外 port 的 $A,wA$ 因而在各积分段上为 $C^4$；没有跨原单元接头套用这一条件。

程序用区间 Taylor 系数 $j_k=f^{(k)}/k!$，$0\le k\le4$，进行加法、乘法、正幂/负幂与指数的封闭运算。soft-cap 分支交叉时取各分支导数范围之并包围，包含切换点。

对长度 $h$ 的单个面板，

$$
S=\frac h6\left(f(a)+4f\left(\frac{a+b}2\right)+f(b)\right),
$$

$$
\left|\int_a^b f-S\right|
 \le\frac{h^5}{2880}\sup|f^{(4)}|
 =\frac{h^5}{120}\sup|j_4|.
\tag{4}
$$

(4) 与完整值域积分界取交，再按实际区间宽度二分。中间上界乘法也使用 outward interval，非只在输出时加一个 nextafter。最后所有端点再朝外舍入到 binary64，并同时保存其精确有理数。

外 port 的原 log slope 导数严格为负，故绝对值可用已证符号展开；它没有被误当成 $\chi=1$ 的 (2)。

这些四阶条件仅用于已知的旋转背景函数。它们不是非旋转场、PPoly 或 mean 的全局四阶正则性假设。

## 4. 深端余项为何能明显收紧

前 $N=32$ 个单元直接计算。对未修改的 $n\ge N$，沿用 R58 同源证明的

$$
W_N=256\,2^{-7N/4},\qquad H_N=17+\frac75N,
$$

$$
T_N=W_N\left[
\frac{4H_N+1}{1-3/10}
+\frac{(28/5)(3/10)}{(1-3/10)^2}
\right].
$$

设 $\rho_n$ 为**旧源**边界半径，

$$
\rho_n=a_0\exp\left[
\frac{6\delta_0\,2^{-n}
 +6\eta_0\,2^{-3n/2}/(1-2^{-3/2})}{\sqrt{12}}
\right].
$$

$n=N,\ldots,158$ 的 $\chi=1$、weights=1；唯一深侧混合在 cell159 内。因此

$$
0\le A_{\rm rest}
\le \frac{T_N}{8}+\rho_{159}-\rho_{160},
\tag{5}
$$

$$
\frac{\rho_N-\rho_{159}}{1+W_N^2}
 \le B_{\rm rest}\le\rho_N-\rho_{160}.
\tag{6}
$$

(6) 使用 $w\le W_N$ 的正权积分下界，没有把整个小径向跨度都算成不确定性。剩余高度项分别不超过
$W_N A_{\rm rest}$、$W_N B_{\rm rest}^{\rm upper}$。实际得到

$$
A_{\rm rest}<1.590\,10^{-13},\quad
\operatorname{width}(B_{\rm rest})<1.528\,10^{-42},
$$

$$
(wA)_{\rm rest}<5.649\,10^{-28},\quad
(wB)_{\rm rest}<4.299\,10^{-28}.
$$

真正 $n\ge160$ 的旧深端高度另用 R58 的同源几何级数界加入。没有使用任何新的无限非线性延拓假设。

## 5. 从积分到归一化、高度和 (1)

计算

$$
\lambda=
\frac{r_{\rm cut}-\rho_{160}-\int A}{\int B},
\qquad
h=\int wA+\lambda\int wB+h_{\rm deep}.
$$

各项用上述区间直接组合即得结论表。$r_1$ 用 cell1 及更深单元的同一积分和计算，没有把旧 R21 的 3.125 数值混入。

为证明 (1)，只考虑共享真实 $A,B,w$ 的两个背景：

$$
r_x=A+\lambda B,\qquad \widetilde r_x=A+\lambda_JB,
\qquad
r(x_{\rm deep})=\widetilde r(x_{\rm deep})=\rho_{160}.
$$

令 $\Delta=|\lambda-\lambda_J|$。因 $A\ge0,B>0$，

$$
\frac{|\widetilde r_x-r_x|}{r_x}
 \le e_x:=\frac{\Delta}{\lambda_{\min}},
$$

$$
\frac{|\widetilde r-r|}{r}
 \le e_r:=\frac{\Delta\,(\int B)_{\max}}{\rho_{160}}.
$$

在共同源坐标 $(x,\theta)$ 中，度量为
$\operatorname{diag}((1+w^2)r_x^2,r^2)$。所以相对算子误差不超过

$$
\max(2e_x+e_x^2,\ 2e_r+e_r^2)
<4.954037113551543\,10^{-10},
$$

故 (1) 成立。如果改用各自物理半径作坐标，还须明确对应拉回；本文不省略该坐标契约。特别地，这个分项结果没有把实际 JS 局部积分、旧半径 elementary 值和完整 field 的其他误差清零。

## 6. 执行和源检查

可执行源：

[certify_q060_background_integrals_tight.py](../scripts/resume_n4/certify_q060_background_integrals_tight.py)。

先按 R58 原命令重新生成同一 constants.json，再执行：

~~~bash
OPENBLAS_NUM_THREADS=1 python \
  topics/visible-flex-held-10pct/scripts/resume_n4/certify_q060_background_integrals_tight.py \
  --input "$WORK/n4-work/q060-tail-geometry/constants.json" \
  --out "$WORK/n4-work/q060-tail-geometry/tight-integrals-certificate.json" \
  --cells 32 --tol 1e-12 --variation-tol 1e-18
~~~

最终源实际 exit 0，30.8809 秒；源 SHA256 为
b7a8dc501dc3dbbe4ccb14d6b4ea2b4b85849d14b9551a94f5c23798d7985806。

作为实现检查，另对 head/deep、cap/混合分支的 135 个 0 至 4 阶 Taylor 系数与独立高精度标量微分作比较，全部包含。该点检查不代替 (2)–(6) 的连续证明。

小执行记录
[2026-11-20-q060-tail-tight-integral-execution.json](2026-11-20-q060-tail-tight-integral-execution.json)
记录实际调用、输入/源/输出 hashes 和关键标量。节点、积分树、完整可再生输出均不入 Git。没有把本条写成全闭合、reach、固定全部参数收敛或 10% 验收。

