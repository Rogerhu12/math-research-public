# R133 独立浮点诊断：同一目标的旋转参考、真正帽线性图与腰返回

2026-11-13，visible-exact-astra-ac0d / newton_source。

本记录冻结三项已经实际跑完的**浮点诊断**。它们均保留原固定
$g_0=E(r)dr^2+a(r)^2d\theta^2$，其中
$E=\langle|F_{{\rm original},r}|^2\rangle$；没有把后续曲面的角均值
重新定义为目标。本记录不给全参数、连续径向、无限角尾的证书，
也不给 nonlinear cap DN 或全闭曲面。

## 1. 对象、frame 和计算域

输入是原精确仿射对象
`type_fixed_step02_d5_exact_affine_step5_object.json`，SHA-256 为
`91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`。
参数严格为
$$
\delta=-7789843107295549/4611686018427387904.
$$
origin 与 direction 的 SHA 分别为
`0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b`、
`8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab`。
所有 primitive 浮点评估使用512个四重周期网点。

旋转参考准确公式是
$$
z'_{\rm rot}=\sqrt{E-a'^2},\quad B_0=0,\quad
C_0=-\sqrt{E-a'^2}/(a\sqrt E),\quad A_0=K/C_0,
$$
方向为 $X=F_r/\sqrt E$、$Y=F_\theta/a$、$n=Y\times X$。
数值 provider 用半径消去后的 $\overline E=E/a^2$、
$\mathscr R=(E-a'^2)/a^4$ 计算 $K$ 和 $C_0$，不在深帽从两个大数
相减。body 仅在 $0\le r\le3$ 使用；$[3,25/8]$ 使用原实际 natural
graft，绝不外插 body spline。

## 2. 实际 Cauchy 端点相对该旋转参考

下表来自冻结的1024角点有限 Cauchy 候选，不是精确分支的区间端迹。

| 半径 | $K$ | $C_0$ | $\sup|B|$ | $\sup|C-C_0|/|C_0|$ | $\sup|A-A_0+\ell(C-C_0)|$ |
|---|---:|---:|---:|---:|---:|
| .235 | −.2934224926 | −.8959690775 | .8757313759 | 2.35704882 | .7784392539 |
| .239 | .03308223613 | −.8951117369 | 1.0172342444 | 2.17930098 | .8191275744 |

这里 $\ell=K/C_0^2$，最后一列直接消费准确代数恒等式
$$
A-A_0+\ell(C-C_0)
=\frac{B^2}{C}+\frac{K(C-C_0)^2}{CC_0^2}.
$$
因此不能把该非圆腰分支未经预算当作旋转参考的小线性扰动。
深帽 $r=3$ 的稳定计算为 $K\simeq.029342446292$，直接浮点差分式
给 $.029342651367$，显示半径消去对实际计算确有必要。
这些点值不代替连续正性证书。

## 3. 真 regular 线回传的物理 Fourier 图

取物理频率 $m=4j$，$\delta B=b_m\sin(m\theta)$、
$\delta C=c_m\cos(m\theta)$。同一目标的真实旋转 Jacobi 系统为
$$
b_m'=-2\beta b_m+\gamma m\ell c_m,
\qquad c_m'=\gamma m b_m-\beta(\ell+1)c_m,
\quad \gamma=\sqrt E/a,\quad\beta=a'/a.
$$
真实 R74 regular 尾在 $r=25/8$ 给
$$
\frac{b_m}{c_m}=\frac{\lambda_m}{m\omega\sqrt{1+w^2}},
\qquad \lambda_4=-4\omega.
$$
本浮点运行对所有列用稳定中心 $q_m=-b_m/c_m=1/\sqrt{1+w^2}$。
第四模的这个入口值准确；其它模还有本运行**未传播**的真实费用
$\le2^{42}\exp[-2m\underline\omega(2^{24}-25/8)]$。
独立 native producer 才负责把该费用和完整原函数尾一起付清。

本次从实际 graft 端回传到 $.239$，使用 DOP853、
`rtol=2e-10`、`atol=2e-12`、径向步长上限 `.005`。
它实际调用目标15227次，运行145.15秒，列出物理频率4到64的16模。

| $m$ | $q_m(.239)$ | 原 Cauchy $b_m+q_mc_m$ |
|---:|---:|---:|
| 4 | 1.056180708410158 | −.0395690166153 |
| 8 | .876310174878219 | .0152574287656 |
| 12 | .785225582116488 | .0229645291429 |
| 16 | .723073237079604 | .0110285586808 |

16模的这个**线性参考图**余量 $\ell^1$ 为 `.5409171252951115`。
候选的未列高模 DFT $\ell^1$ 分别为
`B: .6086925620452387`、`C: 1.238054770360009`，没有删除。
候选 mean $C-C_0=.00224154019564$ 也单列保留。
body/graft 在 $r=3$ 的浮点接缝差分别约为
$\gamma:-2.49\cdot10^{-14}$、$\beta:2.40\cdot10^{-14}$、
$K:6.31\cdot10^{-14}$、$C_0:-7.22\cdot10^{-16}$；这只是实现一致性
诊断，不是接缝舍入界。

## 4. 真闭腰线性初值到正帽的返回缺口

第二次独立 ODE 积分从 $r=0$ 出发，对每个列取
$b_m(0)=0,c_m(0)=1$。这保留线性闭腰的 $B=0$ 与固定 mean；
非零 $C$ 模只是独立归一化列。使用 DOP853、`rtol=2e-11`、
`atol=2e-13`、步长上限 `.00025`，运行186.60秒。

| $m$ | $b_m(.239)$ | $c_m(.239)$ | $b_m+q_mc_m$ |
|---:|---:|---:|---:|
| 4 | −.636506606120303 | .602631005891805 | −.0000193634075701 |
| 8 | −.780348908893688 | −.294457496595795 | −1.03838500922975 |
| 12 | −.298601811116150 | −1.08021190562410 | −1.14681183351900 |
| 16 | .477042044315831 | −1.22257579795819 | −.406969795488978 |

第四模的有符号夹角正弦约为 $-1.51882\cdot10^{-5}$；其余首四
物理模中的三个明显不近临界。这个实测现象支持将物理 $m=4$ 单独
作为后续分岔诊断核心，而不能仅因保存了四个低序号就把它们都当核。
本次误差没有有向封装，故没有证明缺口非零、导数非零、存在根或
任何非线性分岔。另沿 $g_\delta$ 改变目标必须声明为另一个度量家族，
不能回写或偷换本记录的固定 $g_0$。

regular mean 高度是独立的轴向刚体平移端口；曲率 mean 的形式 ODE
不提供 forced mean contact 的逆。完整 nonlinear 帽、真实 mean 根、
labels、两 bump 和全部源项仍须与非圆腰分支联立。

## 5. 可复跑入口与冻结清单

三次命令依次为：

```bash
python scripts/fourfold_phase_codazzi_rotational_reference_probe.py \
  --out notes/2026-11-13-Codazzi-rotational-reference-floating.json \
  --spectrum notes/2026-11-13-Codazzi-rotational-reference-spectra.npz.gz
python scripts/fourfold_codazzi_rotational_cap_jacobi_probe.py \
  --out notes/2026-11-13-Codazzi-rotational-cap-Jacobi-floating.json
python scripts/fourfold_codazzi_rotational_waist_return_probe.py \
  --out notes/2026-11-13-Codazzi-rotational-waist-regular-return-floating.json
```

本环境在各命令前加
`PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps`、
`OPENBLAS_NUM_THREADS=1`、`OMP_NUM_THREADS=1`。
准确文件与全部 repo 内 Python 依赖、输入 SHA 见同目录
`2026-11-13-R133-rotational-diagnostics-manifest.json`。
三套原报告和 producer 已冻结；后续连续 native 或更高阶非线性工作
另写文件，不改写这些结果的数学范围。
