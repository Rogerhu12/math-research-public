# R133：最终 moving 候选的完整物理 regular 端口与实际长段入球

**已证明；是指定近似中心的完整端口证书。** 本文在真正的
$R=25/8$ 上直接消费完整有限 moving 中心，证明其原物理角中的
$Z=(C-C_{\rm ref})_\perp$ 已进入真实 periodic-long 图的输入球。
所有物理频率、真实 regular 乘子的误差、nonlinear 余项和两个 mean
均计入。本文不把这些小的端口残差改称零，也不授予主体的完整 BVP 逆、
远端标签方程或闭曲面存在性。

## 1. 同一个实际中心及目标

完整候选索引为
`moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json`，SHA-256 为

```
ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413
```

索引给6145个径向节点及全部分片三次系数；所有数据 shard 的 SHA、
相同 dyadic 接口和完整形状由原 loader 检查。有限求解的成功状态只用于
识别输入，本证明没有使用它替代任何连续数学门。准确幅度、度量参数是

$$
 \alpha=\frac{6890507429876859}{9007199254740992},\qquad
 \nu=-\frac{2572625729470897}{72057594037927936}.
 \tag{F.1}
$$

原 $E_\nu=E e^{\nu h}$ 的 $h$ 支于 $(1/20,9/50)$，所以在 $R$ 处，
$a_R,\omega,C_{\rm ref}$ 是已证明的同一真实原目标数据。使用
[真实 $R$ 端口证明](R133-supplement-actual-regular-R25over8-vector-and-long-ports.md)
所绑定的整个原 affine 参数区间（半宽 $10^{-9}$）和全部 primitive 尾。
本报告把同一有限 moving 系数与各参数下的真实 $s_R=1/C_{\rm ref}$
相接，故结论对该完整区间成立；没有把一个参数点冒充参数区间。

记最后一片左端为 $r_-$、$h_R=25/8-r_-$。对每一列采用

$$
 x_R=((c_3h_R+c_2)h_R+c_1)h_R+c_0                      \tag{F.2}
$$

的**准确有理运算**，每个输入 double 按其准确 dyadic 值解释。
native 报告保存全部65个准确端值，不使用浮点 PPoly 端点评估代替它们。
写 $M=32$，由这些端值定义

$$
 u=\alpha\sum_{j=1}^{M}U_j\sin(4j\phi),\qquad
 v=s_R+\alpha\left(V_0+\sum_{j=1}^{M}V_j\cos(4j\phi)\right),
$$
$$
 m=s_R+\alpha V_0,\qquad
 \psi=\frac\alpha m\sum_{j=1}^{M}\frac{V_j}{4j}\sin(4j\phi),
 \qquad\theta=\phi+\psi.                               \tag{F.3}
$$

使用 $\langle f\rangle=(2/\pi)\int_0^{\pi/2}f$，准确有
$\theta_\phi=v/m$。下面的原生门给

$$
 -m>5.84461145233,\qquad
 \theta_\phi>0.9999999999985,
 \qquad -v>5.84461145232.                               \tag{F.4}
$$

因此它是整个实角圆上的度1微分同胚，$u$ 奇、$v$ 偶、$\theta$ 奇。
定义真实物理场 $B\circ\theta=u/v$、$C\circ\theta=1/v$。

## 2. 全物理矩和均值，保留准确消去

[完整 moving 边界矩公式](R133-supplement-moving-chart-complete-physical-boundary-moments.md)
的真实换元给，对 $k=4j>0$，

$$
 \widehat C_k=\frac1m\left\langle
     e^{-ik\phi}(e^{-ik\psi}-1)\right\rangle,\qquad
 \widehat B_k=\frac1m\left\langle
     u e^{-ik\phi}e^{-ik\psi}\right\rangle.             \tag{F.5}
$$

第一式减去的是积分准确为零的非恒定 Fourier 模。它既提高数值消去，
也保留下面全部物理尾中真实的 $\psi$ 小量，未删除任何非零物理行。
设正频曲率变量 $b_k=i\widehat B_k$，负频取
$b_k=i\operatorname{sgn}(k)\widehat B_k$。于是
实正弦/余弦边界行 $B_j^{\sin}+q_k C_j^{\cos}$ 与
$b_k+q_k\widehat C_k$ 相同，只差复 Fourier 的因子2；下面的范数始终
同时计入正负频率。

对 nominal $q_k^{\rm nom}$，直接对**完整相关被积函数**

$$
 \frac{e^{-ik\phi}}m
 \left[iu e^{-ik\psi}
           +q_k^{\rm nom}(e^{-ik\psi}-1)\right]          \tag{F.6}
$$

作区间积分；没有先分别给 $B,C$ 大包络后才相加。特别是第一项的
$e^{-ik\psi}$ 保留。

均值使用准确恒等式

$$
 \widehat B_0=0,\qquad
 \widehat C_0=1/m,\qquad
 \widehat C_0-C_{\rm ref}
       =-\frac{C_{\rm ref}\alpha V_0}{m}.               \tag{F.7}
$$

此处的 $B$ 均值为零来自整个反射类，$C$ 均值没有被指定为零：实际得到

$$
 |\widehat C_0-C_{\rm ref}|<6.055\,10^{-43}.             \tag{F.8}
$$

真正 nonlinear long 图的非零 mean 输出仍须另外相减，见第5节。

## 3. 连续 strip、所有 alias 和全部物理频率

取准确 $\sigma=1/8$。有限三角多项式在整个复条带有可直接有向求和的界

$$
 U_\sigma=\alpha\sum|U_j|e^{4j\sigma},\qquad
 V_\sigma=\alpha\sum_{j\ge1}|V_j|e^{4j\sigma},\qquad
 P_\sigma=\frac\alpha{\inf|m|}
       \sum_{j\ge1}\frac{|V_j|}{4j}e^{4j\sigma}.        \tag{F.9}
$$

实际完整64个非恒定有限系数给

$$
 U_\sigma<1.643190\,10^{-9},\quad
 V_\sigma<9.603792\,10^{-9},\quad
 P_\sigma<1.480385\,10^{-11}.                            \tag{F.10}
$$

$|v|>5.8446114427$ 也在整个复条带成立。
$d=\sigma-P_\sigma>0.124999999985$。所有这些是连续条带门，不是角样本。

由 $|e^z-1|\le |z|e^{|z|}$，把 (F.5) 的积分向下或向上平移，分别覆盖
全部正、负频，得

$$
 |\widehat C_k|\le\frac{|k|P_\sigma}{\inf|m|}e^{-|k|d},
 \qquad |\widehat B_k|\le\frac{U_\sigma}{\inf|m|}e^{-|k|d}.
 \tag{F.11}
$$

移线合法，因为原有限函数整解析、指数整解析、$m$ 为非零常数；四重周期
使两个竖边准确抵消。这里不需要构造复逆角，更没有把 $B,C$ 当成有限
物理 Fourier 多项式。

记输出权为 $e^{|k|\tau}$，$0\le\tau<d$，$x=e^{-4(d-\tau)}$。
对任何 $J\ge1$，全部物理尾准确被几何级数控制为

$$
 \sum_{|k|>4J}e^{|k|\tau}|\widehat C_k|
 \le\frac{8P_\sigma}{\inf|m|}
 \frac{x^{J+1}[(J+1)-Jx]}{(1-x)^2},
$$
$$
 \sum_{|k|>4J}e^{|k|\tau}|\widehat B_k|
 \le\frac{2U_\sigma}{\inf|m|}\frac{x^{J+1}}{1-x}.
 \tag{F.12}
$$

本次实际取 $\tau=0,J=128$；全 $j>128$ 的两尾分别小于
$6.540\,10^{-37}$、$1.391\,10^{-37}$。

对每个已解析的物理 $j\le128$，以320-bit Arb/Acb 对512个真实均分
$\phi_n=\pi n/(2N)$ 节点积分 (F.5)–(F.6)。该非线性被积函数通常含
无限多个 moving 模；不以 $N>2M$ 假称积分准确。对 strip 内有界的
四重周期解析函数 $f$，完整 Fourier 级数给

$$
 |Q_Nf-\langle f\rangle|
 \le\frac{2\sup_{|\Im\phi|\le\sigma}|f|}{e^{4N\sigma}-1}.
 \tag{F.13}
$$

证明是对所有非零 alias $\ell N$ 的指数 Fourier 界求和，未截断 alias。
从 (F.5) 可取

$$
 \epsilon_{C,k}=
 \frac{2|k|P_\sigma e^{|k|(\sigma+P_\sigma)}}
      {\inf|m|(e^{4N\sigma}-1)},\quad
 \epsilon_{B,k}=
 \frac{2U_\sigma e^{|k|(\sigma+P_\sigma)}}
      {\inf|m|(e^{4N\sigma}-1)}.                          \tag{F.14}
$$

(F.6) 的 alias 费为 $\epsilon_{B,k}+|q_k^{\rm nom}|\epsilon_{C,k}$。
实际128对物理模的完整 alias 费用分别小于
$5.374\,10^{-92}$、$1.180\,10^{-92}$、$6.553\,10^{-92}$。
全部有向舍入由 Arb 同时包围；full-parameter $m$ 的依赖也保留在同一次
区间计算中。区间包裹变宽只降低精度，不影响包含性。

## 4. 真 regular 行、全部漏出物理模与实际原生值

令 $A_0=\{f:\sum_{k\in4\mathbb Z}|\widehat f_k|<\infty\}$。
本段非均值范数删去的只有零模，后者已单独处理。
原有限 BVP 使用32个正物理行的同一个准确 dyadic proposal

$$
 q^{\rm nom}=\frac{562949953420957}{562949953421312}.
 \tag{F.15}
$$

真实帽乘子满足 $0<q_k<1$。原报告逐频保留
$q_k=-\lambda_k/(|k|\omega\sqrt{1+w_R^2})$，$\lambda_4=-4\omega$
准确，其他模的非零 regular 尾费仍为正；nominal 与实际的完整参数误差
被原有向报告中的 $\epsilon_{q,k}$ 包围。因此已解析模另付

$$
 2\sum_{j=1}^{128}\epsilon_{q,4j}|\widehat C_{4j}|,
 \tag{F.16}
$$

未解析模则付完整 $B$ 尾加完整 $C$ 尾。此处不将 proposal 当成实际
尾乘子。新
[两参数实际 regular 线](R119-supplement-two-parameter-full-tail-chart-reconstructed.md)
(U.1)、(U.17)、(U.21) 已重新实例化其第四 connector 和全模好参数，
并保持同一 $a_*,\omega,L$；其 $2^{41}e^{-2|k|L}$ 费用严格包含于本次
使用的 $2^{42}e^{-2|k|L}$ 包络。因此同一端口估计也适用于该新两参数
真实线，条件仍是先按该篇固定真实 $\Gamma,t$，而非任意删去远端方程。

一次完整实际运算正常 exit0、12.35秒，得到以下严格上界：

| 全原物理角对象 | 严格上界 |
|---|---:|
| $\|Z\|_{A_0}$，$Z=(C-C_{\rm ref})_\perp$ | $2.532986\,10^{-13}$ |
| $\|B\|_{A_0}$ | $2.5328041\,10^{-13}$ |
| $\|b+qZ\|_{A_0}$，真 regular 乘子 | $1.256750\,10^{-15}$ |
| 真 proposal 误差的总费 (F.16) | $2.317577\,10^{-30}$ |
| 所有 $j>32$ 的真 Robin 行，包括完整无限尾 | $6.662282\,10^{-21}$ |
| $|\widehat C_0-C_{\rm ref}|$ | $6.055\,10^{-43}$ |
| $\widehat B_0$ | 准确为 $0$ |

第33至128模是对非线性物理矩的实际包围，不是扩大的有限 BVP。
它们之后由 (F.12) 付完整无限尾。因此上述 Robin 结果没有遗漏原有限
求解器未保留的边界行。

## 5. 真 periodic-long 输入球和非线性边界残差

前表首先严格证明

$$\|Z\|_{A_0}<10^{-10},                                 \tag{F.17}$$

从而它是已证原真实长段图的**实际输入**。独立 $f_B$ 满足
$\|f_B\|_{\dot A^2}\le2^{-60}$；$\dot A^2$ 的非零模权准确是
$|k|^2$，mean 另保留。

本次源代码在运行前还固定更小的 $r_Z=10^{-12}$，只执行一次该门。
前表严格落在这个球内。按原全模 $C\to f_*$ 证明，取

$$
 r_B=2^{-60},\quad r_f=10(r_Z+r_B),\quad F=r_f+r_B,
 \qquad H=6F.
$$

原 $L_C^{-1}:A_0\to\dot A^2$ 的完整上界9、完整 nonlinear 费用给

$$
 \operatorname{image}\le9r_Z+2e^{-6L}r_B+9\,2^{12}F^2,
 \qquad\operatorname{Lip}\le36\,2^{12}F.                \tag{F.18}
$$

实际正余量为 $r_f-\operatorname{image}>1.0000049\,10^{-12}$，
$\operatorname{Lip}<1.474562\,10^{-6}$。
同时 $2F<2^{-25}$、$H<2^{-20}$，全部原 long-BVP 域门成立。
这是同一已证全频收缩的较小明确输入球，没有从有限边界 Jacobian 猜逆。

保留真 regular–finite-long 差和远端反射后，真实长段的非均值图
$b+qZ=d(Z,f_B)$ 和两个 mean 输出满足

$$
 \|d\|_{A_0}<1.638404\,10^{-18},\qquad
 |c_0(Z,f_B)|<2.048004\,10^{-19},\qquad B_0^{\rm long}=0.
 \tag{F.19}
$$

例如第一式完整使用
$(\epsilon_{\rm reg}+8e^{-8L})r_Z+2e^{-6L}r_B+2^{14}F^2$，
而不是只保留二次项。报告中的所有非四模指数费和反射费均以 Arb 的
非零正数保留，即使其指数极小也不替换为零。

因此该实际候选对真 periodic-long 图的完整边界残差满足

$$
 \boxed{\|b+qZ-d(Z,f_B)\|_{A_0}<1.258388\,10^{-15},}
$$
$$
 \boxed{|C_0-C_{\rm ref}-c_0(Z,f_B)|<2.048004\,10^{-19},
 \qquad B_0-B_0^{\rm long}=0.}                          \tag{F.20}
$$

上述非均值是**物理**范数。若主体采用除以 $\alpha$ 的规范化边界行，
应将其费用除以 (F.1) 的准确 $\alpha$，不能直接沿用未缩放数字。
若只消费原 $10^{-10}$ 球，报告也单独保留其较粗完整非均值残差
$<1.764075\,10^{-14}$ 和 mean 残差 $<2.048001\,10^{-15}$。

原独立 mean 高度常数仍独立；本证明没有用 $B_0=0$ 去固定它。
远端仍须联立

$$
 k_B(a)+C_L f_B(a)-S_Lf_*-E_D(f_B(a),f_*)=0.             \tag{F.21}
$$

(F.20) 是供真实主体后验消耗的非零残差，不是已完成 (F.21)，
也不是闭面已经存在的声明。

## 6. 完整可复现文件

- 程序：[fourfold_codazzi_moving_actual_R_boundary.py](../scripts/fourfold_codazzi_moving_actual_R_boundary.py)。
- 原生完整报告：[2026-11-13-R133-moving0765-actual-R-boundary-native.json.gz](../notes/2026-11-13-R133-moving0765-actual-R-boundary-native.json.gz)。

报告保存准确端值、全部128个有向物理矩、每模 alias/真 $q$ 误差、
所有无限尾、完整参数和候选/shard身份、原球和一次较小球的全部门。
运行命令为

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps:scripts \
python scripts/fourfold_codazzi_moving_actual_R_boundary.py \
  --candidate /dev/shm/visible-exact-ac0d699811ad/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json \
  --native notes/2026-11-13-R133-moving0765-actual-R-boundary-native.json.gz \
  --progress
```

重建时使用尚不存在的新输出路径，保持本次实际成功记录。
完成这个端口后仍继续最终中心的完整源逆、真实 regular 标签联立和
全族几何；这些任务不由本篇的小数值替代。
