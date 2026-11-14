# R106 / R110：同一九场矩形接真实严格区首相位

2026-11-13，constructive-route。

新增源 scripts/fourfold_subprincipal_from_energy_rectangle.py。
本篇证明新的误差重加权和场代数；当前没有九场 producer 的完成数值输出，
所以新 consumer 尚未运行，也没有新的 strict 全角数值报告。
它不修改任何 R110 producer、旧场报告、几何参数或旧 R106 字段。

## 同一输入

读取 fourfold_phase_core_energy_fields.py 的完整九场矩形：

$$
(a,b,c,\tau,\sigma,\alpha,v,\gamma,\kappa),\quad
\alpha=1/a,\quad v=b/a,\quad\gamma=bv-c=\mu^2/a,\quad\kappa=-K_0 .
$$

最后的 $\kappa$ 只是负目标曲率，不是 $\mu$。
完整零阶为 $d=\tau+\partial_\theta\sigma$。
原 producer 已付准确选定 dyadic 系数 $P_{i,k}$ 到真系数的每项误差
$\epsilon_{i,k}$、真实复时间盘 $|u|\le R$ 和归一角带
$|\Im(4\theta)|\le S$ 上的真实模界 $M$。
文件中同时保存整个 positive_coefficient_error_radii；
不能只拿已经求和的实角 A0 错称复角误差。

实物理半段为 $r=c+hu$。每个场的 $+k$ 系数是 $P_{i,k}$（偶场）
或 $iP_{i,k}$（b、sigma、v 三个奇场），$-k$ 系数按真实实性取共轭。
物理导数始终乘 $4ik$。源构造的正负频和 Nyquist 约定原样保留。

## 完整复角误差

请求物理带 $0<s<S/4$，置 $s_*=S-4s>0$。在 $|u|\le1$ 上，
对 $\theta$ 导数 $j=0,1,2$，完整误差由下列互不遗漏的三部分支付。

1. 保留矩形的误差为
   $$
   E_{{\rm finite},j}
   =\sum_{i<m}\left[\mathbf1_{j=0}\epsilon_{i,0}
     +2\sum_{k=1}^K(4k)^j e^{4ks}\epsilon_{i,k}\right].
   $$
   对物理 $r$ 导数再逐项乘 $i/h$。

2. 全部高角频（包括其全部时间系数）为
   $$
   E_{{\rm angle},j}=2M\sum_{k>K}(4k)^j e^{-ks_*}.
   $$
   在实 $u\in[-1,1]$，其物理 $r$ 导数费至多
   $E_{{\rm angle},j}/[h(R-1)]$，这是逐 Fourier 系数的完整径向 Cauchy 界。

3. 保留角频中遗漏的时间系数为
   $$
   E_{{\rm time},j}
   =M\frac{R^{-m}}{1-R^{-1}}
      \left[\mathbf1_{j=0}+2\sum_{k=1}^K(4k)^j e^{-ks_*}\right].
   $$
   对物理 $r$ 导数，将前面的时间系数换为
   $$
   \frac{M}{h}R^{-m}
   \left[\frac{m}{1-R^{-1}}+
                 \frac{R^{-1}}{(1-R^{-1})^2}\right].
   $$

真几何系数在同一个已付外盘/角带全纯，所以
$|f_{i,k}|\le MR^{-i}e^{-|k|S}$。这证明第三式。
第二式先对真正 $f_k(u)$ 使用整个时间盘模界，不先把其时间系数绝对和
多付或漏付；其角频范围与第三式互补。第一式使用已付的逐项真系数误差，
包含原时间 DFT、角 alias、节点球和准确系数选择全部费用。
因此这里不重新调用无限原函数，也没有把实角误差直接延拓到复带。

精确角常数 $\kappa$ 的高角频及对应误差保持为零。其余场不删除任何小系数。
几何级数的零、一、二阶矩由现有 geometric_tail 完整支付。

## 真实边界圆、内部支与相位字段

在上边界 $\theta_j+is$，源以全部有限频率准确 DFT 求
$f,f_\theta,f_r,f_{r\theta}$，然后加入上述各自误差。
角间隙半宽为 $\Delta=\pi/(4N)$。整闭角 cell 使用
$$
f(\theta_j+\delta+is)
=f(\theta_j+is)+\delta f_\theta(\theta_j+is)+\mathcal E,\quad
|\mathcal E|\le\Delta^2M_{\theta\theta}/2
$$
以及导数的一阶包络；所有半径系数先用整个所选闭径向区间作 Horner。
因此不是仅检查角节点。上下边界由实际实性和 Schwarz 共轭对应。

程序单独要求整个上边界的 $\operatorname{Re}\alpha$、
$\operatorname{Re}\gamma$、$\operatorname{Re}(-K_0)$ 正。
实部调和最小值原理补齐内部及下边界；不能从实轴 $\gamma>0$
免费得到该复带支。定义
$$
\mu=\sqrt{\gamma}/\sqrt{\alpha},\quad
a=\alpha^{-1},\quad b=v/\alpha,\quad c=v^2/\alpha-\gamma,
$$
$$
L_r=\tfrac12(\gamma_r/\gamma-\alpha_r/\alpha),\qquad
L_\theta=\tfrac12(\gamma_\theta/\gamma-\alpha_\theta/\alpha).
$$
两个平方根各在右半平面取与实轴相容的解析支，避免将一个松矩形商
$\gamma/\alpha$ 误判为跨负实轴。于是以下全部是真实原算子的场：
$$
D_{\rm full}=
\frac{\tau+\partial_\theta\sigma-
 (aL_r^2+2bL_rL_\theta+cL_\theta^2)/4}{\mu},
\quad
V_r=\frac{aL_r+bL_\theta}{\mu},\quad
V_\theta=\frac{bL_r+cL_\theta}{\mu}. 
$$
这里使用完整 $d$，所以 R106 的独立角散度 $S$ 可以准确取零。
对 $\varepsilon=\pm1$、$w_\varepsilon=v-\varepsilon\alpha\mu$，
完整代数恒等式是
$$
V_\theta-w_\varepsilon V_r
=\varepsilon(L_r+w_\varepsilon L_\theta).
$$
源在全部边界角 cell 另验其区间残差含零。已经全纯的实际场再由最大模原理
从两个完整边界取得整个带的模界，而不是把边界节点最大值当作域上界。

## 与已付真射线的接法

默认物理带为 $1/800$，严格包含 R106T 的实际像
$8221101/8000000000<1/900$。输入必须绑定同一 origin/direction 与对象，
并覆盖整个 $\delta_5\pm10^{-9}$。请求区间还限制在 R80 已付的中央 bulk
范围内；若要进入根 collar，程序拒绝把这一 strict consumer 延用过去。

在标签带 $1/1024$，每个闭径向片已付的 $D_{\rm full}$ 模积分乘
$J_*/2$ 得该片真实主相位积分界。这里只支付主积分；
R106 的端点仍以同一真实 $J(V_r+\varepsilon L_\theta)$ 接线。
相邻真实片的内部端点准确相消，全局累积器只加入真正外端。
根有限部、最终 KAM 标签再参数和 R104 的整个强余项仍另付。

## 实际重放入口与状态

~~~sh
python scripts/fourfold_subprincipal_from_energy_rectangle.py \
  --field-report ACTUAL_COMPLETED_NINE_FIELD_REPORT.json \
  --physical-strip 1/800 --angles 4096 \
  --out /tmp/R106-strict-phase-from-energy.json.gz
~~~

ACTUAL_COMPLETED_NINE_FIELD_REPORT.json 是必须真正完成且含原数组 SHA 的输入，
不是占位伪报告。程序会核查 producer 与依赖源码、全部数组、参数、
真射线证书和 R80 证书的身份。径向递归只分割同一准确有限矩形，并重新收费；
没有跨标量 knot 换 germ。完整通过前 complete 保持 false，原失败记录保留。

截至本篇保存，native 不可用，同伴九场源尚无新完成报告；故没有执行上述命令。
恢复后这项 consumer 的首个实际输出将同时支付新复支门和实际 D/V 模数，
并可直接复用到 R106 完整严格区积分。
