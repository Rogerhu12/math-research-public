# R58. 首 valley 为 4.625 的 q060 尾背景连续高度与曲率界

维护：Astra-held10-1b6d88ec-20261120 / n4_continue。2026-11-20 UTC。

## 结论与对象

**已证明并实际执行区间计算：** 对当前 q060 物理参数、首 valley=4.625 的旋转尾背景，以固定 512-step 算法产生的有限 binary64 校准常数为参数，随后按真实积分定义径向重分配，完整背景满足

$$
0\le w\le\frac{41}{100},\qquad
\frac{2877037660749259}{144115188075855872}
 \le h(.3)\le
\frac{7446320975220351}{288230376151711744}
 <\frac{259}{10000}<.029,
\tag{1}
$$

$$\boxed{\quad |\kappa_{\rm mer}|,\ |\kappa_{\rm ang}|\le8.\quad}\tag{2}$$

它在正半径 cuff 上以 $C^2$ 接到平盘。若该背景上侧的 cut 高度 $z_b$ 在 $[.1,1.28]$，则本尾背景加平盘及其上下反射满足

$$
|X|<1.34,\qquad X\cdot n>.087,\qquad D\le2.68.
\tag{3}
$$

$D$ 在 (3) 中是这个反射组件的直径；只有其他组件也位于同一中心的该球内时，才据此得到整个曲面的直径界。没有通过改变中心或局部缩放来增加比例。

**范围：** 这是新的 4.625 背景结论，不是 R21 的 3.125 数据复用。它不认证当前非旋转 Fourier 尾场、真实 DN 收敛、前缀接缝、全 $t$ 嵌入/reach 或握持比例。真实积分定义的背景与 JS 有限求积 profile 的求值误差在本条仍未支付；不能把本条当作后者与前者相差小于 $10^{-6}$ 的证明。

深端只使用 R21 已明确列出的**同源旋转背景**校准根括号；没有继承任何无限非线性延拓或指定 Dirichlet 端口的满射结论。

## 1. 此次固定的物理背景

实际输入为重新生成的 q060-port，其 parameters 来自
[q060_cosine_reference_binding.json](../scripts/resume_closed/q060_cosine_reference_binding.json)；
相应尾 config 由 [portable_bootstrap.py](../scripts/resume_m3/portable_bootstrap.py) 生成。
关键参数为

$$
r_{\rm cut}=.3,\quad w_{\rm cut}=.08,\quad
{\rm width}=.25,\quad K_{\rm allocation}=8,\quad
{\rm orientation}=1,\quad{\rm protectCell}=160,
$$

$$
\delta_0=.006,\quad R=64,\quad a_{\rm exponent}=11/4,\quad
\eta{\rm Power}=3/2,\quad\eta_0/\delta_0=.05.
$$

有限 valley 前六项为

$$[4.625,\ 2.8125,\ 4.0625,\ 5,\ 5.25,\ 4.0625],$$

其余为零。首单元 pulse caps 为 [.4,.02]、valley cap 为 .1，warp weights 为 [1,.5,3,.05,1]；其余单元 cap 为 .02、weights 为 1。保留 cut-preserving 规则，prefixR=2、prefixEnd=15、prefixReturnStart=8，没有 flatOuter 或 rejoinR20 修改。

与 R21 相同，基础有限校准系数取原算法 512 steps 返回的**字面 binary64 数**；本次 dump 的有限系数最小/最大浮点显示分别为 1.0154504636256139、1.4951194808096238。全部真实有理输入落在向外取整的区间

$$[1.0154,\ 1.4952]\subset[1/2,2].$$

这些系数在本条是已固定输入，不声称它们正好是精确传输零点。改变 calibrationSteps 会改变这一有限参数对象，除非另给精确根误差和同一根分支证明。

固定这些有限常数之后，窗口、cap、径向重分配和高度用真实函数/积分解释。记 cuff 半径为 $a_0$；它是 rCut-width 的已声明 binary 值，满足

$$a_0>.04.$$

真实无限深源继续使用相同 $\delta_n,\eta_n,R=64$ 和 R21 所引用的深根括号。这个条件只涉及没有改过的深源段，不涉及新的首 valley 或非旋转场。

## 2. 真实径向重分配与此次区间积分

在源单元坐标 $x$ 中记旧半径为 $r_o$、$E=1+w^2$。沿用实际构造的表达式

$$
A=(1-\chi)j_0(r_o)_x+
 \chi\frac{|w_x|}{8E^{3/2}},\qquad
B=\chi\frac{(r_o)_x}{E}\,W,
$$

$$
r_x=A+\lambda B,\qquad
\lambda=\frac{r_{\rm cut}-r_{160}-\int A}{\int B},
\qquad h(r)=\int_{a_0}^{r}w(v)\,dv.
\tag{4}
$$

这里 $\lambda$ 是总宽度归一化，区别于单元校准根和核心圆化参数。$W$ 是上述正 warp 权。普通段 $\chi=1$；两处端口混合按原完整公式保留。

此次实际执行
[certify_background_integrals_v2.py](../scripts/finite_closure/m3_m8_collar_disk/certify_background_integrals_v2.py)，
对**新输入**前 16 个原始九段单元，每段使用 128 个 dyadic 区间、60 位 mpmath.iv，包围整个区间的 $A,B,wA,wB$ 值域。没有用两次浮点 quadrature 的差猜测误差。

其余单元使用 R21 已证明的同源估计

$$
W_n\le256\,2^{-7n/4},\qquad H_n\le17+\frac75n,
$$

$$
{\rm TV}_{n\ge N}(w)\le
W_N\left[
 \frac{4H_N+1}{1-3/10}
 +\frac{(28/5)(3/10)}{(1-3/10)^2}
\right].
\tag{5}
$$

因为 $n\ge16$ 的 $R=64$、valley 为零、weights 为 1，首单元的 4.625 修改不进入 (5)。常 cap 不增加斜率上界或总变差。剩余旧径向跨度以对应 $a_0\operatorname{expm1}(Y_N/\sqrt{12})$ 包围；由此同时包围 $\int A,\int B,\int wA,\int wB$ 的余项，保护端旧径向项也包含在内。

所有最终端点向外舍入并作为精确有理数保存。下表十进制再次朝外取整；复核使用输出中的 exact fraction 字段：

| 量 | 下界 | 上界 |
|---|---:|---:|
| $\int A$ | .1367197758708651 | .1711840826960824 |
| $\int B$ | .0006006176461188288 | .0006009098224778464 |
| $\int wA$ | .01719740358526352 | .02184325587608766 |
| $\int wB$ | .00002108901318996714 | .00002116239711806606 |
| $\lambda$ | 131.1609735033469 | 188.6062203818817 |
| 完整 $h(r_{\rm cut})$ | .01996345908548454 | .02583461561074652 |
| cell0 内半径 $r_1$ | .1227297670552738 | .1480347219788586 |

特别地，真实 $\lambda>100$ 且 $r_1>.1227297670552738$。高度的 exact upper 是 (1) 中的有理数。

此前同次输入的 64 panels 包围给出高度上界 .029150884605912666，尚不能支付 .029 窗口；这只是区间包围过宽。改为 128 panels 后满足窗口，物理参数、冻结校准常数和真实积分定义均未变。工厂浮点 heightSpan=.022772089996296273 仅作为先行诊断，不替代上面的真实积分界。

## 3. 全域斜率与两主曲率

旋转图的两条主曲率绝对值为

$$
|\kappa_{\rm mer}|=\frac{|w_x|}{r_x E^{3/2}},
\qquad
|\kappa_{\rm ang}|=\frac{w}{r\sqrt E}.
\tag{6}
$$

### 3.1 普通有限段

普通段 $\chi=1$。由 (4) 与 $\lambda B>0$，

$$r_x\ge\frac{|w_x|}{8E^{3/2}},\qquad r_x>0,$$

包括 $w_x=0$ 的点。因此 $|\kappa_{\rm mer}|\le8$。

对 $1\le n\le159$，没有首单元大 cap；实际 slope cap 小于 $1/49$。因为 $r>a_0>1/25$，

$$|\kappa_{\rm ang}|<\frac{25}{49}<8.$$

### 3.2 cell0 的大 cap 与 cut-preserving 段

除最后两段外，局部 cap 均不超过实际 .4，所以 $w\le.41$；首 valley 的 4.625 不越过这些 cap 界。

倒数第二段令 $t=S_5(x)$。该段没有 valley 修改。此次新 elementary gates 对同一 source 参数独立验证了

$$
\log w_{\rm raw}\le\frac75-3t,\qquad
\log w_{\rm capped}<-\frac{19}{5}.
$$

cut-preserving 混合给

$$
\log w\le-\frac{19}{5}+\frac{26}{5}t-3t^2
 \le-\frac{116}{75}<-\frac32.
$$

又 $\exp(3/2)>4$，故该段 $w<1/4$。最后 port 的原 slope 另有 $w<.1$。于是整个 cell0 的确有 $w\le.41$。

结合这次重新计算的 $r_1$，

$$
|\kappa_{\rm ang}|\le\frac{.41}{r_1}
 <3.340673<8.
\tag{7}
$$

这里不能用 R21 的旧 $r_1$ 数字代替新输入。

最后 port 是唯一外端 $\chi\ne1$ 的混合段。在此
$\chi=1-t$、$j_0>1+4t$、$E<1.01$、$W=1$，所以

$$
\frac{r_x}{(r_o)_x}
\ge t+4t^2+\frac{10000}{101}(1-t)\ge5.
\tag{8}
$$

最后一个不等式可直接减去 5，分解为
$(1-t)(10000/101-5-4t)\ge0$。原 port 有
$w_{r_o}=-7w/r_o$，而 $w<.1$、$r_o>.04$。由 (8)，

$$
|\kappa_{\rm mer}|
 <\frac{7(.1)}{(.04)5}=3.5<8.
$$

因此没有把这个混合段误当成 $\chi=1$ 的普通段。

### 3.3 保护端、无限深源与 C² cuff

对没有修改的无限深源，仅引用 R21 所列公开适用性审核中的

$$\alpha_n\in[1/2,2],\qquad n\ge80,$$

且使用其实际参数前提
$\delta_0\in[1/200,1/160]$、$\eta_0/\delta_0\in[1/25,1/16]$、$R=64$。当前参数逐项满足；这里没有从首部新 valley 推出新的无限非线性结论。

由 $|S_5'|\le15/8$、$\sqrt{12}<7/2$，深源满足

$$
|w_{r_o}|\le
 \frac{(7/2)(15/8)W_nH_n}{a_0\eta_n}
 +\frac{7W_n}{a_0}.
\tag{9}
$$

在 $n=160$，用
$\eta_{160}\ge2^{-240}/5000$、$a_0>1/25$，
(9) 的精确有理上界小于 .046030。新 gate 实际得到
.0460295268567279 的浮点显示；比较使用 exact rational。

第一项以后按 $2^{-1/4}H_{n+1}/H_n$ 缩小，第二项更快。由于
$2^{-1/4}<17/20$ 且
$(17/20)(1212/1205)<1$，它们都趋零，$w\to0$。

cell159 第一 port 是保护混合段。该段的原斜率远低于 cap 的不激活阈值；新 gate 用
$W_{159}<256\,2^{-278}<1/400$ 和 $\exp(2)<8$ 验证这一点。其原 $|w_{r_o}|$ 极小且小于 8。在 $\chi\in[0,1]$ 的混合中，旧径向速度和曲率分配项都满足 $r_x\ge |w_x|/(8E^{3/2})$，另有非负 $\lambda B$，因此也有 (2)。

各有限 join 的 $w,w_r$ 连续。$|w_x|$ 可能使辅助参数的径向速度出现 cusp，但 $r_x>0$ 且 $w_r=w_x/r_x$ 连续，所以真实半径图的 $h$ 仍为 $C^2$。深端 $w,w_r\to0$，故在 $a_0$ 处把 $h$ 延拓为零，再在 $0\le r\le a_0$ 接平盘，得到真正 $C^2$ 的旋转组件；极点采用普通 Cartesian 平盘坐标。

综上，完整背景满足 (1)、(2)。

## 4. 高度安放、support 与直径预算

上侧旋转背景取

$$
X(r,\theta)=\bigl(r e^{i\theta},\,Z-h(r)\bigr),\qquad
Z=z_b+h(r_{\rm cut}).
$$

对上向单位法向

$$n=(w e^{i\theta},1)/\sqrt{1+w^2},$$

有

$$
X\cdot n
 =\frac{r w+Z-h(r)}{\sqrt{1+w^2}}
 \ge\frac{z_b}{\sqrt{1+.41^2}}.
\tag{10}
$$

平盘的 support 是 $Z$，更大。若 $z_b\ge.1$，(10) 严格大于 .087。因为 $r\le.3$、$z_b\le1.28$ 和 (1)，

$$
|X|^2\le(.3)^2+
 \left(1.28+\frac{7446320975220351}{288230376151711744}\right)^2
 <(1.34)^2.
\tag{11}
$$

新 gate 用精确 Fraction 比较 (10)、(11)，不是把四舍五入的显示值当严格阈值。下侧按同一原点反射，support 和范数不变，得到 (3)。

当前新桥已支付的**条件实际 cut 高度窗**
$z_c\in[.6001,1.0213]$ 本身落在此更宽的背景放置窗内。若真实非旋转尾的完整 mean primitive 还贡献 $\mu$，应使用 $z_b=z_c+\mu$，不能重置 mean。比如沿用已有条件 $|\mu|\le.01$ 时，$z_b\in[.5901,1.0313]\subset[.1,1.28]$。$\mu$ 的实际界必须来自那个实际尾场；本条不为未求出的场假定该条件已成立。

非旋转扰动的位移、归一一阶/二阶 jet 对 (2)、(10)、(11) 的损耗，按原条件尾预算另外支付。背景 K=8 留出了与新全域 K=12.3 目标的差，但不能直接把 4.3 作为未经归一化的场二阶导数许可。

## 5. 复现、真实执行与数据边界

实际本地运行名为 q060-tail-geometry-20261120。输入和输出的精确 SHA、命令、区间摘要及执行状态记录在
[2026-11-20-q060-tail-background-execution.json](../notes/2026-11-20-q060-tail-background-execution.json)。
新的解析 gate 为
[certify_q060_tail_background_gates.py](../scripts/resume_n4/certify_q060_tail_background_gates.py)；
旧 3.125 gate 未修改，也没有把旧脚本的通过记录当作新参数的通过记录。

可搬迁的完整调用顺序如下。TOPIC 指本题目录；SOURCE 指按既有 portable_bootstrap 恢复的 source_topic；PORT 是该次生成的 q060-port.json；WORK 是库外临时目录。

~~~bash
node "$TOPIC/scripts/finite_closure/m3_m8_collar_disk/dump_background_constants.mjs" \
  "$SOURCE" "$PORT" "$WORK/constants.json"

python "$TOPIC/scripts/finite_closure/m3_m8_collar_disk/certify_background_integrals_v2.py" \
  --input "$WORK/constants.json" --out "$WORK/integrals128.json" \
  --cells 16 --panels 128

python "$TOPIC/scripts/resume_n4/certify_q060_tail_background_gates.py" \
  --constants "$WORK/constants.json" --integrals "$WORK/integrals128.json" \
  --out "$WORK/analytic-gates.json"
~~~

这三步实际 exit 0。128 panels 的区间积分约 8.35 秒；新解析 gate 全部断言通过。无 BVP、无 nonlinear shooting、无场数组被运行或移动。

全部校准数组、完整区间输出均由命令再生并只保留在 scratch，不提交可再生数据；仓库只保留脚本、固定输入来源、命令、输出 SHA 和本条必要结论摘要。

## 来源与继承范围

- [R21](R21-finite-c2-tail-collar-and-disk.md)：同型径向重分配、背景深源括号与 collar 结构；本条只复用通用公式/同源深段，有限积分和首部几何数据均重新支付。
- [R21 来源范围](../scripts/finite_closure/m3_m8_collar_disk/R114-closure-scope.md)：公开审核中背景校准根区间的精确适用边界；不继承无限非线性结论。
- [固定背景原完整论证](../scripts/finite_closure/m3_m8_collar_disk/M3-finite-C2-collar-and-disk.md)，仅其结构公式与未改深源段。
- [本会话固定背景身份核查](../notes/2026-11-20-n4-frozen-tail-metric-identity.md)：真实 worker 的 H 请求不重校准背景，以及有限校准设置与目标精确定义的区别。

