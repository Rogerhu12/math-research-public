# 实际连续角弧残差与共享网格参考

2026-11-12。这里保存两个真实无限图的**一个连续复角弧、一个实时间小区间**
的有向残差验证，以及 δ₃ 全初值有限 Fourier 参考的准确构造和有限域预算。
没有完整圆周或两腿误差证书；局部 R60 的零初差是假设另取匹配初值，
不是从全程历史获得的零误差。

## 1. 共享网格与准确参考

`scripts/fourfold_shared_dense_reference.py` 读取完整共享时间网格的两场
$Y,L$，输出 degree 7 Bernstein 时间多项式和有限角 Fourier 系数。
每个存储的 binary64 系数被当作准确 dyadic 数，定义一条新的、完全明确的
参考函数；浮点 DOP853 的插值精度不被当作证明。负 Fourier 模取共轭，
偶数网格的 Nyquist 项以半权分到正负模，零模虚部归零。

在每个时间接口，下一块的首 Bernstein 系数准确替换为前块末系数，
$Y,L$ 内腿跳跃严格为零；外时间端点用准确 $\pm\pi/2$，内部端点保留准确
dyadic 时间。回腿若使用 `--previous-reference`，准确复制 $U$ 端点，
$L$ 可按新腿归一化重置。R61 的跳跃公式仍须包含这种参考 $q$ 的变化。

δ₃ 输入和输出身份：

- 对象 `type_fixed_step02_d5_exact_affine_step3_object.json`，SHA
  `e6ff2d46ed2d321c1b287e6c9d8e44ead7b9a70523350d145d703b4edd6def0f`。
- 实际 516 共享网格两腿报告，SHA
  `3ba4ca28b138a63ca9fe3ce6202e393ab33cc7d5b15063a7580902458085278b`。
- 正腿参考 manifest `data/phase_ring_continuation/r61_step3_shared_forward/manifest.json`，
  SHA `0b5c7b410fd2ec2638f583396f51fcb1ddc1c311c39f978f3dfb3e1d6f7dd5a7`。
  共 550 段、角 Fourier degree 258；31,285,861B 可重算探索分片暂不入库。
  若选为最终证书的实际输入，则必要系数分片须另保存。

用冻结的 `fourfold_fourier_reference_bounds.py` 对**全角有限函数**验证：

| 初值归一化宽 $S_x$ | $|\Im Y|$ 上界 | $|q|$ 下界 | $|q|$ 上界 |
| --- | ---: | ---: | ---: |
| $1/512$ | .00200489328 | .02871481063 | 19.419118 |
| $1/256$ | .00401786744 | .02839997033 | 19.634397 |
| $1/128$ | .00810217693 | .02713419 | 20.550317 |

宽 $1/512$ 的初始 $\|H-4Y_0\|$ 上界为 $6.980311\times10^{-15}$，
$q_0=1$。这些有限域结论不估计实际 ODE 误差。
完整有向结果为 `2026-11-12-R61-step3-shared-forward-bounds.json.gz`。

重做入口（在本课题目录）：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/fourfold_shared_dense_reference.py --trace-dir data/phase_ring_continuation/exact_affine_step3_shared_knot_dense516 --leg forward --rays 516 --out-dir data/phase_ring_continuation/r61_step3_shared_forward
```

上游共享网格生成的准确源、命令、全部大中间量 SHA 见
`2026-11-12-shared516-step4-preconjugacy-frozen-manifest.json` 及其说明。

## 2. 双变量系数环与真实无限 primitive

`fourfold_time_angle_jets.py` 用矩形截断环
$\mathbb C[u,v]/(u^m,v^n)$，其中 $u$ 是归一化时间，$v$ 是连续初值角弧。
Kronecker 乘法步长为 $2m-1$，故被截断的高时间次数不会错误进位成角次数。
倒数、指数、对数及平方根用以原生时间 series 为系数的角递推；所有运算
由 Arb 有向包住。准确有理幂级数和进位陷阱自检通过。

`fourfold_phase_time_angle_residual.py` 先将准确 Bernstein 参考转成中心时间
幂系数，再在 $x=z_0+h_xv$ 上对**有限 Fourier 参考本身**求双 jet。
物理角为 $Y=x/4+U$。非线性真实几何沿同一准确 scalar germ 求值。
只在 $v=0$ 计算一次带无限尾费用的 $X=F_r$ 时间 jet；其余角系数由
旋转 frame 的准确等式

\[
 X_\theta=a_rT+aT_r-JX,\qquad J(X_1,X_2,X_3)=(-X_2,X_1,0)
\]

乘 $Y_v$ 后逐项递推得到。每步只用已知更低的 $X$ 角系数，不需要
假设角截断后的函数等于真实无限 primitive。

真实场及其物理角导数给 $e_0=Y_\tau-f$、$e_1=L_\tau-f_\theta$。
时间和角的相关性在相减前始终保留。另检查第一角系数的准确链式恒等式
$\partial_v f=f_\theta Y_v$；两个报告的全部保留时间系数均通过。

## 3. 全外双圆盘、余项及局部管

在外双圆盘 $|u|\le R_t,|v|\le R_x$ 上，用完整有限 Fourier 参考求
$Y$ 的角偏移包络，再交给真实场的外域门。这里**不**用截断角 jet
冒充整个外圆盘像。原生场模型支付无限 primitive、非零分母及 $-K$
平方根分支，产生实际 $M_f,M_{f_\theta},B_2$。

双 Cauchy 的省略行/列总误差至多

\[
 M\frac{R_t^{-m}+R_x^{-n}}{(1-R_t^{-1})(1-R_x^{-1})}.
\]

交叉角被多计是安全的。参考的时间导数虽然时间次数有限，角 Taylor
仍有无限尾，另付
$M_{Y_\tau\text{ 或 }L_\tau}\,R_x^{-n}/(1-R_x^{-1})$。
对有限保留残差系数取模和，加上这两笔费用，得到每个连续弧/时间窗的
sup 界。$q=e^L$ 的模上下界也含完整参考角尾。
随后局部 R60 以**另取匹配左初值**计算 $A,B,C$ 并检查管内包含；
不能丢掉真正全程传来的初差。

## 4. 两个已完成实际弧

共同设置 $z_0=1/2+i/512$、$h_x=1/4096$、$R_t=8$、$R_x=4$，
时间保留 degree 16、角 degree 23、160 bits、Q512，
各参考段的归一化时间窗均为 $[31/64,33/64]$。

| 准确对象与参考段 | $\sup|e_0|$ 严格上界 | $\sup|e_1|$ 严格上界 | 两笔 $e_0$ 尾合计 |
| --- | ---: | ---: | ---: |
| δ₂，881段参考的653段 | $4.593373\,10^{-7}$ | $.000572901235$ | $6.281787\,10^{-15}$ |
| δ₃，共享550段参考的419段 | $7.420387\,10^{-10}$ | $1.622920\,10^{-7}$ | $5.914534\,10^{-15}$ |

报告是 `2026-11-12-R61-step2-time-angle-arc-pilot.json` 和
`2026-11-12-R61-step3-time-angle-arc-pilot.json`，内含源、依赖、对象、根、
参考 shard 的完整 SHA。它们各自的局部匹配初值 R60 管门通过，运行约
11.4秒和12.9秒。完整独立审查见 `2026-11-12-time-angle-arc-independent-audit.md`。

δ₃弧重做：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/fourfold_phase_time_angle_residual.py --manifest data/phase_ring_continuation/r61_step3_shared_forward/manifest.json --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_root_tight.json --segment 419 --out notes/2026-11-12-R61-step3-time-angle-arc-pilot.json
```

冻结源还用旧 binary64 root interval，因此约 $10^{-13}$ 的系数半径仍存在；
新的共享 native refined-root 入口已另通过实际参考重放，可以在后续新验证器中
采用而不改写上述冻结证书身份。全圆/全时间/回腿、连续参数源及最终 KAM
仍欠；当前主要计算问题是外域粗区间引起过多时间细分和逐微弧遍历费用。
