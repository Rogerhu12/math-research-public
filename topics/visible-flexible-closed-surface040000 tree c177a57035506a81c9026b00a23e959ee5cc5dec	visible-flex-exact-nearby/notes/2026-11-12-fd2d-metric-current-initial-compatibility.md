# 当前准确中央曲线的全角初始相容常数

## 对象和用途

本条支付 R119、R124、R125 中当前保存字段的初始误差项。它使用 R173 明确的准确中央曲率族和准确目标，而不把旧浮点曲线求积的输出直接当作准确初值。

实际输入是 [grouped27 的已接受场](2026-11-12-fd2d-raw-bump-grouped27-trial-back00-a01-accepted.npz)，SHA256 为 2b65810c5c09985d54544e6ca697ee609f066a17ecbce4b83e89adad0b52ae6f。该场保存 131 个径向节点、31 个中央参数、16 个尾参数、7 个物理径向参数。完整定义取自 [R173 native definition](2026-11-12-fd2d-metric-current-complete-arb-02-native-definition.json)，准确物理目标取自 R171 原 packet。本文没有改变任一保存数组。

独立消费者是 [fd2d_gc_current_initial_compatibility.py](../scripts/fd2d_gc_current_initial_compatibility.py)。其 source SHA256 为 4798015e22dc7d335cd7eb6b96c1d0f57b3bfc5a2a2d1ab2c3e9e7c5c205cca6。完整区间结果在 [actual report](2026-11-12-fd2d-metric-current-initial-compatibility-01-report.json)。

## 1. 准确中央曲线

设 $\xi$ 是固定 balanced seed 的法向角，$\rho(\xi)>0$ 是已经明确定义并严格包围的 seed 曲率半径，

$$
 u=U_*(\xi),\qquad U_*'(\xi)=\frac{\rho(\xi)}{a_0}.
$$

所有中央参数 $c_j$ 按保存的 binary64 字节解释为准确有理数。定义

$$
 \mu_j=\frac1{2\pi a_0}\int_0^{2\pi}
                 \rho(\xi)\cos(2j\xi)\,d\xi,
 \qquad
 \kappa_C(\xi)=\kappa_{\rm base}(\xi)
                 +\sum_{j=1}^{31}c_j(\cos(2j\xi)-\mu_j).
\tag{1}
$$

这里实际 base 是 balanced seed，即 $\kappa_{\rm base}=1/\rho$。源码也显式区分圆 base $1/a_0$，绝不依靠参数总长度猜测 base。所用 $\mu_j$ 是 [512 模严格矩包](2026-11-12-fd2d-balanced-weighted-means-512-02.json.gz) 的前 31 项；它们由准确积分定义，区间只是准确数的包围，不把中点重新定义为真实均值。

令切向角满足 $\vartheta_u=a_0\kappa_C$，取与声明 seed 相同的初始定向，令

$$
 T=(\cos\vartheta,\sin\vartheta),\qquad \gamma_u=a_0T.
\tag{2}
$$

因为 $\rho$ 和所有 $2j$ 模都是 $\pi$ 周期，(1) 的每个修正满足半周带权积分零；准确 seed 和圆 base 在半周的总转角均为 $\pi$。因此 $T(\xi+\pi)=-T(\xi)$，而 $\gamma_\xi=\rho T$ 为半周反周期。两半周的位置增量相消，准确曲线闭合。取半周中心积分确定平移，就得到原中央族的准确可计算位置定义。其速度严格为 $|\gamma_u|=a_0$。这一步不需要数值求积恰好闭合，也不在此声称曲线嵌入或完整曲面已存在。

## 2. 保存字段与准确曲率的全角差

原点处 seed 权为 1，tail、coast 和 terminal 窗均为 0，atlas 为 $U_*$，准确径向目标为中央柱 $a(0)=a_0,\ a_s(0)=0$。这些条件由完整定义逐项核对。

写保存 raw 的初始余弦系数为 $b_0,b_j$，初始 $m$ 的正弦系数为 $d_j$。实际字段在该点满足

$$
 n_F=\kappa_{\rm base}+b_0+\sum_jb_j\cos(2j\xi),
 \qquad
 m_F=\sum_jd_j\sin(2j\xi).
$$

所以

$$
 \Delta n:=n_F-\kappa_C
   =b_0+\sum_jc_j\mu_j+\sum_j(b_j-c_j)\cos(2j\xi).
\tag{3}
$$

式 (3) 的常数用严格 $\mu_j$ 包围，其余系数差用准确有理运算；三角函数绝对值不超过 1。于是对整圆成立

$$
 \|\Delta n\|_\infty
 \le \left|b_0+\sum_jc_j\mu_j\right|_{\rm upper}
          +\sum_j|b_j-c_j|,
 \qquad
 \|m_F\|_\infty\le\sum_j|d_j|.
\tag{4}
$$

这是全角不等式，不是从有限角网格推断连续上界。实际输入中 $b_j=c_j$、所有 $d_j=0$、初始 raw $l=0$ 均逐项以有理数严格相等；唯一非零误差来自保存的浮点常数项与准确带权均值之间的差。

## 3. R119 的 $D_0$ 和 $C_0$

取准确初始标架 $F_0=(e_1,T,N)$，其中 $e_1$ 为固定横向单位向量，按右手定向选择 $N$。令 $B_F$ 是保存字段和准确目标的材料角标架矩阵，$B_C$ 是准确曲线矩阵。由于 $a_s(0)=0$，

$$
 D_0=F_{0,u}-F_0B_F=F_0(B_C-B_F).
$$

叉乘矩阵的算子范数等于其轴向量长度，且 $F_0$ 正交，因此

$$
 \|D_0\|_{\rm op}
 =a_0\sqrt{(\Delta n)^2+m_F^2}.
\tag{5}
$$

另一方面 $\gamma_u=a_0T$ 是定义恒等式，故

$$
 C_0:=\gamma_u-a_0e_2=0,\qquad C_{0,u}=0.
\tag{6}
$$

(5) 结合 (4) 直接给出后验所需的 $d_0$，(6) 给出 $k_0=0$。没有求解新的 frame/body ODE。

若后续角变分预算需要 $D_{0,u}$，不能因 (3) 只剩常数就把整个矩阵导数设为零：$F_0$ 本身随角旋转。由乘积法则和 $\|F_{0,u}\|_{\rm op}\le a_0\|\kappa_C\|_\infty$，

$$
 \|D_{0,u}\|_{\rm op}
 \le a_0\|\kappa_C\|_\infty d_0
      +a_0\|((\Delta n)_u,(m_F)_u)\|_2.
\tag{7}
$$

其中 $d/du=(U_*')^{-1}d/d\xi$，而 $\inf U_*'>0$ 已在完整 atlas 绑定中支付；对有限三角多项式按各 $2j$ 系数绝对和给出最后一项。源码保留 (7) 的第一项。

## 4. 已发生的实际计算

原进程 session 21449，首块 1617a1、末块 21912f，真实 exit 0；计算耗时 1.5715151870026602 秒，峰 RSS 92596 KiB。环境中断后原 source/report 的 SHA 均重新核对相同，没有重复计算或将恢复写入过程算成另一次数学运行。

report 给出准确常数差区间

$$
 b_0+\sum_jc_j\mu_j
 \in[-8.375284475056731\cdot10^{-17},
       -7.456473715969723\cdot10^{-17}],
$$

并给出如下向外舍入的全角预算：

$$
 d_0\le8.409479404952111\cdot10^{-17},
 \quad k_0=0,
 \quad \|D_{0,u}\|_{\rm op}
       \le8.975006069222694\cdot10^{-16},
 \quad C_{0,u}=0.
$$

机器可消费的准确 dyadic 端点在 report 中；显示的小数仅便于阅读。所有本次界都绑定 2b 输入和 R173 的完整 accurate-domain binding，不能直接转用到后来改变的中央参数。

## 5. 重做命令与范围

在本课题目录运行；输出 stem 必须改用未存在的新名称：

~~~sh
PYTHONPATH=/workspace/scratch/fd2d-recovered-deps/python-flint-0.9.0 \
python scripts/fd2d_gc_current_initial_compatibility.py \
  --native-definition notes/2026-11-12-fd2d-metric-current-complete-arb-02-native-definition.json \
  --profile-packet notes/2026-11-12-fd2d-metric-r136-arb-profile-01-packet.json.gz \
  --out-prefix notes/2026-11-12-fd2d-metric-current-initial-compatibility-replay
~~~

这支付了完整后验的准确中央初值项。全径向/全角 forcing 余项、实际重建的 seam、完整 metric 和几何界仍由对应后续消费者支付；本条没有把未完成场宣称为完整闭曲面。
