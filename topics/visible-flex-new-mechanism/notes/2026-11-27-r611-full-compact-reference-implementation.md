# 实际圆参考的完整紧区间二 jets 与全 reach：新计算定义

2026-11-27，Astra-new-mechanism-1f4a61a4-20261127。
**v2准确区间系数修复后已完成认证，完整证明见[R611](../results/R611-actual-circular-reference-complete-reach-certificate.md)；不是非圆候选的reach结论。**

## 1. 沿用的准确对象

固定 R608 所定义的同一解析圆参考及其实际控制
$\mu=-.040019082162222074$、$\nu=-.048942275258064924$。
两个数是原公开 true-core run 已登记的 binary64 常数，不重新射击、
优化或比较尾口。完整 $a,z$ 由 `r582_continuous_mean_profile_20261126.py`
定义；端点和样条系数作为准确实常数，端点的数学差通过区间运算包住。
数值 CUT 不改变 $H$ 的从零开始的无限积分。

R608 已支付 $s\ge s_*:=L-2\ell/25$ 的无限尾：$z_s>0$、
$a>r_c$、$|\kappa_m|<1/3$ 及完整平圆盘的光滑接口。
新 scope 只补尚未支付的 $[c,s_*]$ 完整二 jets。
实际右端取 $s_*$ 区间上端再向上舍入一次，故与 R608 的准确尾范围有重叠。
不重做旧的 $[c,L-.08]$ 单独正图检查；新二 jet 单元同时支付所有几何条件。

## 2. 准确区间公式

记 $b$ 为背景阶跃，$\chi$ 为全宽自由阶跃，
$\beta=4\chi(1-\chi)$，$\psi$ 为原紧支撑控制。
用五次 B 样条的 de Boor 递推及其两次准确导数系数得到
$P_a,P_{a,s},P_{a,ss}$ 与 $P_z$ 的同类区间。每个实际跨结单元取所有相交 knot span 的区间并。
设

$$
\alpha=\beta P_a+\mu\psi,\quad Z=\beta P_z+\nu\psi,
\quad r_0=r_c+L-s,\quad a_b=(1-b)a_c+br_0.
$$

则完整半径二 jets 为

$$
a=e^\alpha a_b,\quad
a_s=e^\alpha(a_{b,s}+a_b\alpha_s),\quad
a_{ss}=e^\alpha[a_{b,ss}+2a_{b,s}\alpha_s+
 a_b(\alpha_{ss}+\alpha_s^2)],
$$

其中 $a_{b,s}=b_s(r_0-a_c)-b$，
$a_{b,ss}=b_{ss}(r_0-a_c)-2b_s$。
全部和、积、商、幂逐次向外舍入，不能先把 $r_c+L$ 或端点差舍入为新的准确常数。

对 $w=H_s=A\exp[-(2-\sin\delta^{-2})/\delta]$，
$\delta=(L-s)/\ell$，直接使用

$$
w_s=-\frac w\ell\left[
 \frac{2-\sin\delta^{-2}}{\delta^2}
 -\frac{2\cos\delta^{-2}}{\delta^4}\right].
$$

令 $T=h_0+H-(.02+s)$。同一高度的两导数准确为

$$
z_s=1-b+b_sT+bw+Z_s,\quad
z_{ss}=-2b_s+b_{ss}T+2b_sw+bw_s+Z_{ss}.
$$

$H$ 由继承的向外舍入 Riemann 积分包住，并包含
$[0,\mathrm{CUT}]$ 的解析余项；这项新几何计算所需的积分再生全部计费。
不实例化旧 `ContinuousMean` 的数值 QUADPACK 表，更不把其误差估计当成区间证明。

### 全平端点的二阶导数

在阶跃端点相邻的归一单元 $0\le x\le h\le1/8$ 上，令
$B=\exp[-1/h+1/(1-h)]$。
$x^{-j}e^{-1/x}$ 对 $j\le4$ 在此区间递增，故

$$
0\le\chi\le B,\quad
|\chi_s|\le\frac B d[h^{-2}+(1-h)^{-2}],
$$

$$
|\chi_{ss}|\le\frac B{d^2}
\left\{[h^{-2}+(1-h)^{-2}]^2+2h^{-3}+2(1-h)^{-3}\right\}.
$$

反射端用同一绝对界。更宽端点单元先二分。对紧支撑 bump 取
$B=\exp(4-1/h)$ 的同样正多项式上界；这是删去小于一的
$\exp[-1/(1-x)]$ 后的严格上界，不按浮点端值直接置零。
内部单元直接微分原 logistic/bump 公式。
自由包络的值始终由稳定的 $\chi(1-\chi)$ 区间计算，避免用
接近一的 $\chi$ 作减法而丢失振荡尾尺度。

## 3. 同时接受条件与全域推论

一个闭区间单元只在以下全部严格区间条件成立时接受：

$$
a_{\min}\ge r_c,\quad (z_s)_{\min}>0,\quad
\frac{|a_sz_{ss}-z_sa_{ss}|_{\max}}
 {\bigl(a_s^2+z_s^2\bigr)_{\min}^{3/2}}
\le\frac1{.06072}.
$$

平方根由90位 Decimal 正确舍入加保守保护量再向外转为 binary64。
三角与指数沿用原90位端点证明；余弦用带误差区间的 $\pi/2$ 平移，
不能把其浮点近似当准确相位。请求中声明的相位范围小于继承的1200上限。

不合格单元是未决，继续二分，不解释成实际失败。
若全部紧区间被接受，结合 R608 的准确开尾、中央柱和两完整平帽，
R599 的全正负子午切圆证明给出**整个圆参考**的 reach 至少 $.06072$。
这已含跨半面、跨帽和帽内源点，不只是局部曲率。
圆参考的直径还由
$D\le2\sqrt{a_{\max}^2+h_0^2}$ 包住；其中尾半径界 $.237$、
中央半径 $.38$ 及帽半径 $.22$ 都计入最大值。

即使上述 scope 成功，R604 传给非圆候选所需的连续扰动范数仍未支付；
固定度量精化、宏观幅度和整个准确非圆族也不由本计算推出。

## 4. 执行、输出与保存

新源 `scripts/r611_circular_reference_global_geometry_20261127.py`，
新请求 `computations/request-r611-circular-global-20261127.json`，
新 workflow `.github/workflows/visible-r611-circular-global-20261127.yml`。
沿用原真实双仓 pull、README blob 和本会话 QUEUE 检查的 stdin runner。
只有公开 Actions 执行本科学范围；本地只做源码阅读和 AST/JSON/hash。
无新 ODE、seed、优化或旧方向门。

完整叶区间流只算 SHA256，不保存可再生表。stdout 输出实际覆盖、
未决区间、计数、积分余项和成本；成功只声明圆参考，未决不伪造证书。
任务级别继续非圆有限解与完整历史路线，不以此必要几何子项收尾。

## 5. 首轮回执及准确系数修复

原 run `45881358480` / job `140121219177`（source `1edc7e36cb6ea0fe0669d78803bcca68d939d21c`）
在 34.78825178699998 科学秒后返回成功，4180 个考察单元中接受2125个叶单元，
曲率上界16.469037030693656、直径上界1.560001714985865。
原日志134668B，SHA256 `80cf0b92854adb3167e8a37c737f7e00b137662922c69b747666421ad95fb103`；
只保本地读取，不提交表或日志。原输出不登记为严格 R611。

逐式复核发现继承的 `ValidatedTailHeight.height()` 先以 binary64 计算
`-AMP * ELL`，再乘区间。该中间舍入不能冒充两个准确存储实常数的准确乘积。
v2 直接读取同一向外 Riemann 前缀的端点包围，使用
`-(Interval(AMP) * ELL) * Interval(low.lo, high.hi)`，并将输出的积分宽度也改为
同一准确区间系数；不再调用继承的 `height()`，查询越过覆盖范围直接未决。
这是修复现有证书的一处实际算术缺口，重算费用单列；原解析对象、R608尾、
几何接受条件和目标reach完全相同。只有修复后的完整覆盖可登记为严格结论。
