# 原 M12 正 K 全位置 BVP 与 signed coast 的实际双端回传

2026-11-26，Astra-visible-flex-6a65e705/g5_and_exact。

本次对原固定 $g$ 的整个 up 减速正曲率 ramp，实际解了一个两端口均自由的
Cartesian 位置有限 BVP。独立观察的相对 metric 峰从 $6.126\cdot10^{-10}$
降到 $3.801\cdot10^{-11}$。随后真实接入反向精确 coast，并把其另一端按完整两 jet
接回 R221 的首 ramp；首 ramp 峰升至 $5.166\cdot10^{-9}$。
因此本次局部 BVP 有真实改善，而接合后的整个候选**不采用为全域改善**。
没有把端口差留在待办而继续使用局部更小的数值作为全图指标。

## 1. 冻结对象与真正的自由端口位置空间

原参数和 $g$ 与 R220/R221 相同。设
$T_u=\delta/[v(1-\epsilon)]$、$R=T_u\epsilon$。
本次求解域是完整 $[T_u-R,T_u]$，其准确端点为

$$
s_l=\frac{348491827713809}{816652732429850},\qquad
s_r=\frac{1569467665433573303349898379264}{2206726164877301818986894580375}.
$$

原正曲率 profile 为
$f(s)=1+\delta-vR P((T_u-s)/R)$，$f'=vF$、$f''=-vF'/R$，
用已登记的同一分段多项式 $P,F$。背景是实际原 M12 位置图，经过准确 bridge 比例
的数值评价 $u_{\rm native}=\lambda s$ 与原辅助角的反函数；没有用旋转模型替换背景，
也没有使用 R114 的材料修复 $\Phi$。

固定中央材料 chart $u_0(\theta)=a_{\gamma_0}^{-1}\int_0^\theta|\gamma_0'|$，
记 $\rho_0=u_0'$、$b=f\rho_0$。未知量是

$$
W(s,\theta)=\sum_{i,a}c_{ia} B_i(s) P_a(\theta),\qquad Z=X_{\rm old}+W.
$$

$B_i$ 为五次 clamped B-spline；所有控制系数均自由，包含左右端的位置、一阶和二阶径向迹。
角基为完整选定 C3/反射空间：
$P_m=(\cos m\theta,\sin m\theta,0)$，$m=1+3j$、$-J\le j\le J$；
以及 $P_k=(0,0,\cos k\theta)$，$k=3j$、$0\le j\le J$。
这是可直接微分的实际周期 $C^2$ 位置图，没有独立拟合的标架。
没有加入修改 $f$ 的 rho 设计列。$W$ 内部为 $C^4$；背景已有节点保持原 $C^2$ 定义。

优化残差直接取

$$
e=|Z_s|^2-1,\quad z=Z_s\cdot Z_\theta/b,\quad
q=|Z_\theta|^2/b^2-1,\qquad r=(e,\sqrt2z,q).
$$

对任意位置方向 $V$，真正的解析 Jacobian 是

$$
J(V)=\left(2Z_s\cdot V_s,
\frac{\sqrt2}{b}(Z_s\cdot V_\theta+Z_\theta\cdot V_s),
\frac{2}{b^2}Z_\theta\cdot V_\theta\right).
$$

代码按 $\sqrt{w_s b/N}$ 乘行权，用 FFT 与 sparse B-spline 乘积计算 $J$ 和准确离散转置 $J^T$，
不存稠密 Jacobian。每个角频率使用
$H_k=\int[B'B'^T+(k^2+.01)BB^T]ds$ 的 Cholesky 逆平方根作变量预条件；
$.01$ 只在预条件中，不添加物理惩罚或改变目标的零集。
非线性更新后重新算实际 $E,F,G$，用真实能量下降及峰值约束选择步长。

## 2. 三次真实运行及独立观察

三次均实际 exit 0；它们不是已证的无限维收敛序列。
低角阶试跑验证了端口自由与解析伴随接口，但没有得到峰值改善。
随后角阶扩大支付主要缺陷频率；最后增大径向 Gauss 取样核查训练网格留下的误差。

| 运行 | 自由度 | 训练角点 / 每单元 Gauss | LSMR 次数 | 训练峰 | 独立观察峰 |
|---|---:|---:|---:|---:|---:|
| J12 / 36 元，2 Newton | 1558 | 192 / 4 | 350+350 | 6.184e-10 | 6.195e-10 |
| J32 / 47 元，1 Newton | 5096 | 384 / 4 | 1600 | 2.330e-12 | 4.908e-11 |
| J32 / 47 元，1 Newton | 5096 | 384 / 8 | 1800 | 4.435e-11 | 3.801e-11 |

独立观察总是每单元增加两个 Gauss 点、角点数加倍；最终为 Gauss 10 与 768 角点。
最终独立观察的原图峰为 `6.125882023866339e-10`，新图为 `3.800369056078325e-11`，
能量从 `4.3023289543970534e-20` 到 `5.157289602718875e-25`。
新图主曲率采样峰约 `1.840352925`，support 约 `0.817884897`。
第二行的 $2.33\cdot10^{-12}$ 是训练观察，不作为最终精度。
三次 LSMR 都到达显式迭代上限（stop=7），不是已验证的精确线性方程解。

最终运行的随机离散伴随恒等式相对差为 `2.9885013671569426e-14`。
左右端位置迹真实移动约 $1.7145\cdot10^{-11}$、$2.7946\cdot10^{-11}$，
一阶径向迹约 $2.4943\cdot10^{-10}$、$4.4001\cdot10^{-10}$，
二阶径向迹约 $3.1578\cdot10^{-7}$、$1.7984\cdot10^{-6}$。
因此程序确实释放了两个端口，并未隐藏冻结 Cauchy 数据。

## 3. 既有 R137 的 signed 消费域与完整形状传递

旧 [flat-outlet continuation](2026-11-09-db6f-flat-outlet-ruling-continuation-v1.md) §5
已经登记局部 $x<0$ 延拓。本次不重新申领该结论；新增的是保留旧正向源码身份的
`6a65-r137-signed-coast.py` 消费器、明确的可用域及实际完整两 jet 回传。

保持物理增 $s$ 方向的 $d$ 和 $v>0$，负 $x$ 时不额外取反它们。
写 $r_0=a/v$、$r=r_0+x$、$\Delta=x(2r_0+x)$。
同一连通根为

$$
A=\sqrt{r_0^2+(1+k^2)\Delta},\qquad
w=\frac\Delta{r_0+A},\qquad
D=a+w[v(1+k^2)-k_t].
$$

充分域条件为 $r>0,A>0,D>0$。恒等式
$A=r_0+(1+k^2)w$ 给
$r_0+w=(r_0k^2+A)/(1+k^2)>0$，故同一 atan2 分支无跳跃，
$U_t=D/(vA)>0$，且 $U(t+2\pi)=U(t)+2\pi$。
在该全角条件成立时，signed 图与正向图同样是同一 $g$ 的准确位置表达式。
原 consumer 的 $x\ge0$ 检查只是原实现域，不是更一般恒等式的限制。

在新的半径 $f=a+vx$ 处，新的形状量满足

$$
n_{\rm new}=\frac{a n(vA)^2}{Df^2},\qquad
k_{\rm new}=\frac{r_0k}{A},\qquad m_{\rm new}=n_{\rm new}k_{\rm new}.
$$

从原 $n,m$ 的零至三阶材料导数，直接对这些公式求两阶 $t$ 导数，再用
$t_U=1/U_t$、$t_{UU}=-U_{tt}/U_t^3$ 转到新材料角。
第三阶 $k$ 的求法可写为
$k_{ttt}=(m_{ttt}-3n_tk_{tt}-3n_{tt}k_t-n_{ttt}k)/n$。
所有三阶形状导数从同一有限 Fourier 曲线的六阶导数算出。
程序不对新的 $n,m$ 或 $X_{ss}$ 迹另作 Fourier 拟合。
由准确 coast 的角向 Gauss 恒等式

$$
d_U=vT+fmN,\quad T_U=-vd+fnN,\quad N_U=-f(md+nT)
$$

及其导数，形成回传端的完整 $d,T,N$ 两阶角迹，供 R221 的真实 Hermite 接合使用。
这些恒等式只用于按 R137 从一条曲线准确生成的 coast，不套到原近似图的独立标架上。
实际返回的 $X,X_s,X_U,X_{ss},X_{sU},X_{UU}$ 仍来自 signed 位置公式自身微分。

## 4. 实际两条接缝及对整段候选的否决

在最终 BVP 的左端，用 768 个固定中央 $\theta$ 点取实际位置，
按原 C3/反射约束生成新的 degree-191 Cartesian Fourier 曲线。
这明确是新有限曲线，不冒充原无限复合角函数的恒等展开；采样位置差为
`6.662263269364698e-15`。
其精确弧长归一到原 $f(s_l)$，并从 $s_l$ 反推原整段 $L=T_u(1-2\epsilon)$，
到达首 ramp 的 $R$，没有改变 affine profile。

在正 K ramp 的第一个完整多项式 piece，以及首 ramp 的最后一个完整 piece，
分别按整个角函数的零、一、二阶径向迹构造五次 Hermite 接合。
左端基函数为

$$
H_0^-=1-10z^3+15z^4-6z^5,\quad
H_1^-=h(z-6z^3+8z^4-3z^5),\quad
H_2^-=h^2(z^2/2-3z^3/2+3z^4/2-z^5/2),
$$

右端基函数沿用 R221。三条迹及它们的两阶角导数均来自同一实际定义；
原 M12 迹的角导数用完整辅助角反函数链式法则，包含 $\psi_s,\psi_{ss}$，
没有以独立位置采样差分替代。
所以两个接口的 C2 相等是函数恒等式；误差观察则重新微分修正后的整张实际图。

实际结果为：

| 子域 | 本次真实 seam 后的 metric 采样峰 |
|---|---:|
| 首 ramp | `5.16570100483951e-09` |
| signed coast 的两端和中点 | 小于 `5.78e-15` |
| 正 K ramp | `3.800369056078325e-11` |

首 ramp 原 M191 峰约 $4.31\cdot10^{-12}$，所以整段候选明显变坏。
回推到首 ramp 的 $X,X_s,X_{ss}$ 迹差分别约
$1.3383\cdot10^{-9}$、$1.5599\cdot10^{-8}$、$5.0381\cdot10^{-7}$；
必须支付这些真实接合差，不能只引用反向 coast 自身的精确 metric。
signed 公式实际返回的 $n$ 与上式 transport 之差小于 $7.55\cdot10^{-15}$，
$m/n$ 之差小于 $5.00\cdot10^{-16}$。

本次不接正 K ramp 的右端，也不声称整个闭图已经构造。
下一全局变量空间应联动内部接口，保留真正中央/平 cut 的完整边界迹；
此处已经实际排除了“先逐段降低，再把完整两 jet 接缝作为小数忽略”的实现。

## 5. 命令、源码与 receipt

源码 SHA256：

| 文件 | SHA256 |
|---|---|
| `6a65-m12-positive-ramp-position-bvp.py` | `b8857ea5eaccd1c744fddd94182cc733396360fadb96400576cb9fb818eeeca0` |
| `6a65-r137-signed-coast.py` | `3263cc2305589576c02c13fc361a38c8b73d2d2fd8fb47debe08eb6fcace97eb` |
| `6a65-m12-positive-ramp-signed-coast-seam.py` | `12cca45b493617a729caf7c73aca98fc51cb704f18abde7a3676db81f088c7ee` |

固定旧 M12 数据 SHA256 为 `359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0`，
原 frozen geometry 为 `253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2`，
准确 bridge 参数证书为 `1389cf1a339b0a0d749beb666b6def24a31e766eff0abf63289217728ceacdaa`。
依赖的 R221 glue SHA 为 `d4af218afcf686febb4db29685762b1ec56cb27df45e0e2fccb9e5b0236b2f7a`，
首 ramp 源码为 `532b6ffbf256f085229ab56febc02601f99a6678c047daf3630fdd29881f846a`，
已修正 old-packet adapter 为 `3eec8c14f5b43c8c660401d8dd3e7868d2e15ce24d0beabd7955f27389af7145`。
本次运行环境 NumPy 2.3.5、SciPy 1.17.0。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/visible-flexible-closed-surface/scripts/6a65-m12-positive-ramp-position-bvp.py \
  --data /tmp/visible-flex-6a65e705/exact-work/m12-prefix-data.npz.gz \
  --out /tmp/visible-flex-6a65e705/exact-work/m12-positive-K-free-bvp-o12-e36.json \
  --elements 36 --order 12 --angular 192 --gauss 4 --iterations 350 --newton 2

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/visible-flexible-closed-surface/scripts/6a65-m12-positive-ramp-position-bvp.py \
  --data /tmp/visible-flex-6a65e705/exact-work/m12-prefix-data.npz.gz \
  --out /tmp/visible-flex-6a65e705/exact-work/m12-positive-K-free-bvp-o32-e48.json \
  --elements 48 --order 32 --angular 384 --gauss 4 --iterations 1600 --newton 1

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/visible-flexible-closed-surface/scripts/6a65-m12-positive-ramp-position-bvp.py \
  --data /tmp/visible-flex-6a65e705/exact-work/m12-prefix-data.npz.gz \
  --out /tmp/visible-flex-6a65e705/exact-work/m12-positive-K-free-bvp-o32-e48-g8.json \
  --elements 48 --order 32 --angular 384 --gauss 8 --iterations 1800 --newton 1

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/visible-flexible-closed-surface/scripts/6a65-m12-positive-ramp-signed-coast-seam.py \
  --data /tmp/visible-flex-6a65e705/exact-work/m12-prefix-data.npz.gz \
  --bvp-report /tmp/visible-flex-6a65e705/exact-work/m12-positive-K-free-bvp-o32-e48-g8.json \
  --bvp-field /tmp/visible-flex-6a65e705/exact-work/m12-positive-K-free-bvp-o32-e48-g8.json.field.npz \
  --ramp-report /tmp/visible-flex-6a65e705/exact-work/m12-central-ramp-M191-h001.json \
  --ramp-field /tmp/visible-flex-6a65e705/exact-work/m12-central-ramp-M191-h001.json.field.npz \
  --out /tmp/visible-flex-6a65e705/exact-work/m12-positive-K-signed-seam-o32-g8-d191.json \
  --angular 768 --degree 191 --gauss 10
```

全部实际 exit 0。输出路径须新建，数组与扫描 JSON 留 scratch。

| 运行 | 秒 | 报告 SHA256 | 场/新 curve SHA256 |
|---|---:|---|---|
| J12 | 8.067034751 | `6b7f47d9f09d88766396ca966531a8dddfcf6bbadda914df068ddf9769647b97` | `195949501b54f08e67f46efc9d0d93ff5613cf339712a049de3b2205b9037899` |
| J32/G4 | 40.180087957 | `f089f197fd7427f36e7b25d942bfd5de5e157b7ccb7f8cb9ed589faff9aa1c24` | `51e4194951ed8dca496cc6777bde1dd3b58921329e065d515f562b4576dca62e` |
| J32/G8 | 111.140591624 | `3dca2d4482af6c4969b2e82d2961c39a70645a1fdf24ffe80fdc78e67d96e370` | `58901e2fcdf70c812fbe9c69b5db64184712dc43a1267e1be750d64683924cdc` |
| 双 seam | 23.001379869 | `c5f9e0e1c71573c078af7c64b4d753404b77d4d8f3b93fcac44ec8131e57e03f` | `9eaa39c1c11b3cb51a0e1853f4f525aac50251a08900d70fc28de9e3312d05d2` |

报告包含耗时，重跑 JSON hash 可以变化；场定义和绑定身份须核对。
同一新 signed curve 的首个整数区间尝试采用 2048 初块、最大二分深 6；实际 exit 1，未支付其设置的 $D>1/2$、曲率小于 6 的整域门槛。该失败仅表示本次包含盒不足，不是实际 focus 或不存在证明。本记录保留 `continuous_domain_for_new_signed_curve_certified=false`，不能移用 R221 的另一条 curve 证书；§3–4 的全角精确表达及接合结论仍带 §3 明列的连续域条件。
