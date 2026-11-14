# R133 参数诊断：噪声差商与实际度量族的解析变分

2026-11-13，visible-exact-astra-ac0d / newton_source。

**已经跑完的结论范围。** 原实际仿射参数 $\delta$ 对同一旋转
参考的第四模返回，在直接变分积分中只有约
$1.13809\cdot10^{-5}$ 的导数。此前以 $10^{-7}$ 量级步长独立
积分的差商没有稳定下来，不能用它们判断横截或根。
这两类原输出一并保留。本记录仍为浮点诊断，不证明严格导数、
区间根、分岔或任何固定度量的非线性 flex。

## 1. 这是另一个明确的度量族，不修改固定目标证书

每个参数都使用原保存的准确仿射族
$S(\delta)=S_0+\delta V$，包括原固定 base 权、显式偶/奇对称和
实际 natural graft；定义
$$
g_\delta=E_\delta(r)dr^2+a_\delta(r)^2d\theta^2,
\qquad E_\delta=\langle|F_{{\rm original},\delta,r}|^2\rangle.
$$
原中心为
$$
\delta_0=-7789843107295549/4611686018427387904.
$$
已有固定 $g_0=g_{\delta_0}$ 的证书没有改动。这里的点和导数
是实际**改变目标度量**的方向，不能称作保持 $g_0$ 的 Jacobi 位移。

对每个 $\delta$，从闭腰线性初值 $b_4(0)=0,c_4(0)=1$ 积分到
$r_*=.239$，并从真正 regular 外切口 $R=25/8$ 回传旋转帽的
$q_4=-b_4/c_4$。所测返回为
$$
\mathcal F(\delta)=b_4(r_*;\delta)
                  +q_4(r_*;\delta)c_4(r_*;\delta).
\tag{P.1}
$$
第四模的真实 R74 入口值恰为 $q_4(R)=(1+w_*^2)^{-1/2}$，
其指数反射 fee 准确为0。五个小步长点都位于原 R74 已证明的
参数盒；非第四模没有在本次参数诊断中求解。

## 2. 五点独立积分：差商实际未稳定

每个点另写一个准确 binary64 参数对象，原 origin/direction
及所有其他定义不变。DOP853 使用 `rtol=2e-11`、`atol=2e-13`，
帽区步长上限 `.005`，腰区 `.00025`。五个运行均结束，但不能
将 solver 的局部误差指标当作差商的误差界。

| 参数偏移的请求值 | 实际浮点返回 $\mathcal F$ |
|---:|---:|
| $-2\cdot10^{-7}$ | −.0000193560666567061 |
| $-10^{-7}$ | −.0000193850193686007 |
| $0$ | −.0000193592898730666 |
| $+10^{-7}$ | −.0000193400679937561 |
| $+2\cdot10^{-7}$ | −.0000193577138611900 |

实际参数差用保存的 dyadic 值读取，所得中心差商为
$$
h=10^{-7}:\quad .224756874223,
\qquad 2h:\quad -.004118011210.
$$
符号和量级都不稳定。由它们得到的 Newton 外推参数只是报告里的
原始诊断列，**没有被采纳为候选根**。也没有把五个中心点扩成一个
连续参数结论。

## 3. 在实际有限原函数实现中先微分，再积分变分方程

新 provider 不对最终两个很接近的 ODE 返回相减。它先对相同
仿射几何的标量 jet 和角原函数作准确链式微分。记参数微分为点，
径向微分为撇。对于 R133 的稳定变量
$$
L=a'/a,\quad L'=a''/a-L^2,\quad
H=Z'/a^2,\quad H'=Z''/a^2-2LH,
$$
逐项采用
$$
\begin{split}
\dot L&=(\dot a'-L\dot a)/a,\\
\dot L'&=\dot a''/a-a''\dot a/a^2-2L\dot L,\\
\dot H&=\dot Z'/a^2-2H\dot a/a,\\
\dot H'&=\dot Z''/a^2-2Z''\dot a/a^3-2\dot LH-2L\dot H.
\end{split}                                                     \tag{P.2}
$$
单位切向量的参数导为 $T_\beta\dot\beta+T_\gamma\dot\gamma$，
对其完整前两个径向 jet 同样微分，再应用相同的线性 Fourier
原函数算子。当前实现仍使用512点有限 primitive；没有省略
这项未认证的无限尾范围。

对 $u=LP+P_r$、$u_r=L'P+LP_r+P_{rr}$，其参数导全部保留。
$e,e_r$ 是 R133 的均值双线性式，其导数由完整乘积法则给出。
例如
$$
\dot e=2\dot L\langle u_x\rangle
       +2L\langle\dot u_x\rangle+2\langle u\cdot\dot u\rangle.
$$
然后对
$$
\overline E=L^2+a^2H^2+e,\quad
\mathscr R=H^2+e/a^2,
$$
$$
N=H^2(L^2-L')+LHH'+(Le_r-2L'e)/(2a^2),\quad
K=N/\overline E^2
$$
作完整微分，并使用
$$
\dot\gamma=\dot{\overline E}/(2\sqrt{\overline E}),\quad
\frac{\dot C_0}{C_0}
=\frac12\left(\frac{\dot{\mathscr R}}{\mathscr R}
              -\frac{\dot{\overline E}}{\overline E}\right),
$$
$$
\dot\ell=
\frac{\dot K\overline E+K\dot{\overline E}}{\mathscr R}
-\ell\frac{\dot{\mathscr R}}{\mathscr R}.
\tag{P.3}
$$

### 3.1 实际 graft 也被微分

`[3,25/8]` 仍使用同一个固定 $C^4$ cutoff 乘以入口有限 Taylor
jet 的准确 natural-graft 公式。入口 $\log a$ 的参数导是
$\dot a/a$，$H$ 的导数是 (P.2)。归一相位的参数导分别为
$$
\partial_\delta(\beta/a^3)=\dot\beta/a^3-3\beta\dot a/a^4,
\quad
\partial_\delta(\gamma/a^2)=\dot\gamma/a^2-2\gamma\dot a/a^3.
$$
这些入口 jet 进入同一个 graft 多项式，而后将 $a^3$、$a^2$
及其参数导一并恢复。这里的相位 $\gamma$ 与上式标量
$\sqrt E/a$ 采用代码中的不同变量，未混作一个量。

独立核对点覆盖 $0,.05,.239,.8,1.5,2.99,3,3.0625,3.125$。
中心值与此前使用 Arb 构造实际 graft 的浮点 provider 比较，
body 差通常约 $10^{-16}$；最大的 graft 标量差约
$7.18\cdot10^{-11}$。参数导再与同点 $h=10^{-5}$ 中心系数
差商核对，最大观测差约 $1.39\cdot10^{-10}$。
这些是实现核对，不是有向舍入上界；该较大步长仅用于局部系数
公式核对，没有在 R74 盒外假定新的 regular 线定理。

## 4. 独立变分 ODE 和实际结果

帽区的 $q=q_4$ 满足
$$
q'=4\gamma(q^2-\ell)+\beta(\ell-1)q.
$$
将 $\dot q$ 作为独立状态，准确方程为
$$
\begin{split}
\dot q'={}&[8\gamma q+\beta(\ell-1)]\dot q
 +4\dot\gamma(q^2-\ell)-4\gamma\dot\ell\\
 &+\dot\beta(\ell-1)q+\beta\dot\ell q.
\end{split}                                                     \tag{P.4}
$$
入口导数完整包含
$\dot q(R)=-w_*\dot w_*/(1+w_*^2)^{3/2}$。
腰区同时解 $y'=M_\delta y$ 和
$\dot y'=M_\delta\dot y+\dot M_\delta y$，其中
$\dot y(0)=0$ 对应固定归一化 $b(0)=0,c(0)=1$。
因此最终读取
$$
\dot{\mathcal F}=\dot b+\dot q\,c+q\dot c.
\tag{P.5}
$$
实际运行622.69秒，得到
$$
\mathcal F(\delta_0)\simeq-1.9360431695814\cdot10^{-5},
\qquad
\dot{\mathcal F}(\delta_0)\simeq1.1380867735991\cdot10^{-5}.
$$
形式线性外推的参数位移为
$-\mathcal F/\dot{\mathcal F}\simeq1.70113845$。
这远超本次原参数盒，不是可采用的近邻根，也不据此在远处
外推原数学对象的证书。实际观察只说明原仿射方向在该旋转返回
上非常弱；此前较大的独立差商不可信。

## 5. 冻结、复跑与剩余门

精确文件、五个参数对象和全部输入 SHA 见
`2026-11-13-R133-m4-parameter-variation-manifest.json`。
复跑 producer 分别为
`fourfold_codazzi_m4_parameter_return_probe.py` 和
`fourfold_codazzi_m4_variational_return_probe.py`；后者使用新
`fourfold_codazzi_rotational_target_parameter.py`。

对另一个紧支撑的明确度量控制作灵敏度计算，是后续另定义的
目标族。它不能倒填本次固定 $g_0$ 的证书。真正根、非线性帽、
完整补空间、mean/regular 匹配以及最终共同度量的选择仍须付清。
