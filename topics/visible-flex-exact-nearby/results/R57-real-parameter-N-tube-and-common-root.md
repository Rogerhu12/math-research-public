# R57：真实参数的负 N 管、共同简单根与准确控制点包含

2026-11-12，constructive-route。

**状态：已证明的中间结论，含有向区间有限证书。** 本文将 R55 的
单个显式对称无限 R33 图扩展为一个实际控制点参数族。证明整个实参数
区间、整个实核心、全部角度上的 $N<0$，并证明该参数族拥有一个共同的
简单转折根 collar。另以准确 dyadic 比较，将一个新的 rounded Newton
predictor 的显式对称无限图包含进已认证的控制点盒。

这里的参数族改变输出径向目标 $g_0$。本文不把有限 Schur 方向当作精确
等距 PDE 切向，不把旧浮点近似镜像射线当作本文准确对称图的返回映射，
也不声称已完成复角返回、完整 PDE 逆、闭帽或精确等距弯曲族。

## 1. 两个相关但不同的准确对象

### 1.1 仿射实参数族

取 R55 的冻结输入

`data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz`，

SHA256 为
`0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b`。

记其中 raw phase spline 控制点为 $c_0$，三个 mean 参数为 $\alpha_0$。
取冻结方向

`data/phase_ring_continuation/type_fixed_step02_d5_actual_parameter_direction.npz`，

SHA256 为
`8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab`。

记其两组准确 binary64 系数为 $v,w$。定义
$$
c(\delta)=c_0+\delta v,\qquad
\alpha(\delta)=\alpha_0+\delta w,
\qquad |\delta|\le d,
\tag{57.1}
$$
其中 $d$ 是 binary64 数 `.01` 按准确实数解释的值。因此该区间包含
准确有理区间 $|\delta|\le1/100$。所有加法和乘法在定义中均指实数运算。

其余 knots、base radius、radius shift、mean radius、height slope 固定
为 R55 冻结输入。先对 raw phase 作同一固定 base weight：$\beta$ 乘
base radius 的三次方，$\gamma$ 乘其二次方；实际周长半径和 height
slope 按保存的 mean 线性组合生成。之后将 $a,\beta$ 显式偶平均，
$\gamma$ 显式奇平均，高度定义为偶 slope 从 $0$ 开始的准确积分。
最后按 R33 取无限角 primitive，得到 $F_\delta$。

这一定义保留了真实 phase 变分、真实 circumference 半径及高度变分。
它不是只改变径向作用量的替代模型。固定的 radius shift 不随参数改变。
背景参数 $p=0.4413514918092046$ 仅用于说明中心输入的数值来源；本文
的准确参数原点是上述冻结控制点，不能用未支付的浮点结合律把它等同于
另一 checkpoint 加全局参数的表达式。

### 1.2 更大的独立控制点盒

对每个控制点分量定义有向 binary64 包络
$$
\mathcal C_i=\operatorname{out}\bigl((c_0)_i+[-d,d]v_i\bigr),
\qquad
\mathcal A_j=\operatorname{out}\bigl((\alpha_0)_j+[-d,d]w_j\bigr).
\tag{57.2}
$$
令 $\mathcal B=\prod_i\mathcal C_i\times\prod_j\mathcal A_j$。这里各坐标
可以独立选择，因此 $\mathcal B$ 通常严格大于 (57.1) 的一维集合。
在 $\mathcal B$ 中仍按 1.1 的固定权重、显式对称化和无限 primitive
定义曲面。下面的负 $N$ 结论对整个 $\mathcal B$ 成立；共同简单根的
较窄证书则只对 (57.1) 成立。两者不能互相偷换。

## 2. 负 N 的统一参数结论

对所有 $(c,\alpha)\in\mathcal B$，所有实角度及
$$
|x|\le b,\qquad b=\operatorname{binary64}(.24),
\tag{57.3}
$$
显式对称无限 R33 图满足
$$
\boxed{\quad
\Phi>0.37213,\qquad -N_{\rm raw}>0.42503,
\qquad N<-0.30865.
\quad}
\tag{57.4}
$$
特别地，准确有理核心 $|x|\le2399/10000$ 被覆盖。$N_{\rm raw}$、$N$
及 $\Phi$ 使用 R55 的方向和定义：
$$
N_{\rm raw}=(F_\theta\times F_x)\cdot F_{\theta\theta},
\qquad N=N_{\rm raw}/|F_\theta\times F_x|.
$$

**证明。** 先在 (57.2) 的独立控制点区间上应用 spline 导数的准确线性
递推，并将每次基本运算向外舍入。这样得到的每一阶 derivative control
interval 同时包含 $\mathcal B$ 中所有 spline 的该阶导数控制点。
这种方法会忘记同一个 $\delta$ 的相关性，但只会扩大包络。

所有径向闭单元使用 R55 已覆盖的 partition。每个单元的左右端点先
确定所选 span，在闭 span 内的 binary64 中心计算同一个多项式的
de Boor/Taylor 包络。中心允许为端点，第五系数始终来自所选 span。
故对极窄的相邻 binary knots 单元也没有删去端点或缝隙。

将这些 interval jets 代入 R55 的完整全角标量判据。每单元使用
$4096$ 个四分之一周期角节点及实际角 Lipschitz gap 包住
$1+\beta_\theta$ 和 $\gamma_\theta$；用 $256$ 个四分之一周期的直接
区间 DFT 和解析尾、混叠界包住同一无限 primitive 的 $F_x$。
基本运算、Machin 公式的 $\pi$、Taylor 三角函数及有理 exp 包络沿用
R55 的有向运算实现。因而这一步不是有限角节点上的符号检查。

R55 的准确恒等式为
$$
N_{\rm raw}=-a^2\left[
 (1+\beta_\theta)\cos\gamma\,\langle F_x,e_\gamma\rangle
 -\gamma_\theta\langle F_x,e_\phi\rangle\right].
\tag{57.5}
$$
该判据的所有正乘子条件在每个单元和整个控制点盒上成立。全部
$592$ 个闭单元通过，未使用额外 subdivision，也没有失败单元。
逐单元有向结果给出
$$
\min\underline\Phi=0.37213043506474364,
$$
$$
\min\underline{(-N_{\rm raw})}=0.4250393264037103,
\qquad
\max\overline N=-0.30865948539175136.
\tag{57.6}
$$
这些是已向外舍入的 binary64 端点，并严格蕴含 (57.4) 的有理界。
闭单元按准确 binary64 实数排序，相邻端点逐值相等；首端点为 $0$、
末端点为 $b$。因此正侧核心完整覆盖。显式径向对称给出负侧，四重
角对称将四分之一周期的证明延拓至全角。

最后，$N_{\rm raw}\ne0$ 蕴含 $F_\theta\times F_x\ne0$，所以浸入性
同时成立，而不是预先假定面积分母非零。证毕。

有限证书为
`data/phase_ring_continuation/type_fixed_step02_d5_parameter_N_interval.json`，
SHA256：
`b52537b755e7b5475dc945a5781c0d57a93e71ccdf39ec90891c236fcae2438a`。
它保存所有闭单元、标量界和源文件哈希。生成源为
`scripts/fourfold_phase_parameter_N_interval.py`。

## 3. 同一仿射参数族的共同简单根

以下仅针对 (57.1)。定义真实输出径向目标
$$
g_0(\delta)=E(x,\delta)\,dx^2+a(x,\delta)^2\,d\theta^2,
\qquad E=\langle|F_x|^2\rangle_\theta,
$$
以及
$$
C=a'E'-2a''E,\qquad K_0=\frac{C}{2aE^2}.
\tag{57.7}
$$
对每个 $|\delta|\le d$，在以下区间有一个正根
$$
t(\delta)\in
\bigl(\operatorname{binary64}(.238394),
      \operatorname{binary64}(.238400)\bigr).
\tag{57.8}
$$
该根在下述共同准确有理 collar 内唯一：
$$
I=\left[\frac{238397}{10^6}-\frac1{4096},
         \frac{238397}{10^6}+\frac1{4096}\right]
\tag{57.9}
$$
并在整个 $I\times[-d,d]$ 上有
$$
a>1.0969,\qquad E>1.5072,\qquad
53<\partial_xK_0<68.
\tag{57.10}
$$
于是
$$
53<\frac{K_0(x,\delta)}{x-t(\delta)}<68
\tag{57.11}
$$
对 $x\in I\setminus\{t(\delta)\}$ 成立，且商在根处按连续极限定义。
显式径向对称给出相应负根 $-t(\delta)$。这里没有声称整个正半面
仅有一个根。

**证明。** 为避免把独立控制点区间先差分造成过大高阶误差，先分别
对中心 spline $S_0$ 和准确方向 spline $V$ 计算有向导数包络，再用
$$
S^{(j)}(x,\delta)=S_0^{(j)}(x)+\delta V^{(j)}(x).
\tag{57.12}
$$
这是 spline 对控制点线性的恒等式。将所得 raw phase jets 代入
同一固定权重和显式对称化，再对真实无限 primitive 的角均值计算
$E,E',E''$。无限角尾与实际区间 DFT 的误差全部保留。

有向计算在 (57.8) 两端分别给出
$$
C_{\rm left}\subset
[-0.0014545315600597022,-0.0003342569881028545],
$$
$$
C_{\rm right}\subset
[0.0003473492547891865,0.0014668841041785565].
\tag{57.13}
$$
准确 collar (57.9) 被向外包进保存的 binary 区间
`[.238152859375,.23864114062500003]`。整个区间的有向结果为
$$
a\subset[1.096972306542676,1.0972484630701707],
$$
$$
E\subset[1.5072101270606768,1.5105398622831714],
\qquad
K_0'\subset[53.1011920872526,67.12730394546958].
\tag{57.14}
$$
因此 (57.13) 给出异号端点，连续性给出根；(57.14) 给出整个 collar
内严格单调，故根唯一且简单。中值定理给出 (57.11)。

在这个 collar 内，各输入 spline 都来自固定多项式 span。角向相位
有限，trigonometric 组合及无限 primitive 对实参数均解析，且在紧集
上可逐阶一致求导。$a,E$ 的分母正界排除了奇点。因此局部隐函数定理
适用，唯一性将这些局部根函数接成整个参数区间上的实解析 $t(\delta)$。
此结论没有给出 $t'$、$t''$ 的数值界。证毕。

证书为
`data/phase_ring_continuation/type_fixed_step02_d5_parameter_root_interval.json`，
SHA256：
`b5900c391667b2a1be90912f2abaf58eaea66dfc51c082a8db39ea582b4b94a8`；
源为 `scripts/fourfold_phase_parameter_root_interval.py`。该源导出的
`make_affine_target` 保留了 (57.12) 的真实参数含义。

## 4. Rounded predictor 的准确包含

另一个已保存的有限 predictor 是

`data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton128_probe.npz`，

SHA256：
`566c95612ee91f9fb04282873530dbb97a1450f4c01c8b1814b003bd0e06aee5`。

它来自浮点标签 $p=.4396774815837377$，不声称其控制点逐值等于 (57.1)
的某个准确实参数点。重新物化的完整输入为
`type_fixed_step02_d5_actual_Newton128_interval_inputs.npz`，SHA256：
`d115181ecc0391943e416b0cdb4aaf3b8213eeb96426133815a02548db7599fc`。

对该输入，所有固定背景数组与 R55 原点逐值相同；$19296$ 个 raw phase
控制点及三个 mean 参数分别满足 (57.2) 的闭区间包含。比较对象都是
有限 binary64 数所表示的准确 dyadic 实数，比较操作自身不需要加入
舍入误差。区间盒端点由与第 2 节相同的向外运算重新产生，并保存其
逐数组 SHA256。

因此该 predictor **先显式对称化再取无限 primitive** 所得图属于
$\mathcal B$，严格继承 (57.4)。这只使用盒包含，不使用“附近应当安全”
的经验判断。它也不继承第 3 节仿射子族的根证书，除非另行证明它恰在
该子族中或对自身重新认证根。

上述有限比较的完整记录为
`type_fixed_step02_d5_actual_Newton128_N_membership.json`，SHA256：
`3a29e4fc67dba83797c18b7496d9aa295c9619c76aa915d7ac6ec96cf3977792`；
源为 `scripts/fourfold_phase_N_tube_membership.py`。

## 5. 重做入口与剩余接口

在课题目录执行：

```sh
OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_parameter_N_interval.py \
  --checkpoint data/phase_ring_continuation/type_fixed_step02_d5_jet_corrected_probe.npz \
  --inputs data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz \
  --directions data/phase_ring_continuation/type_fixed_step02_schur_directions.npz \
  --parameter-map notes/2026-11-12-phase24-corrected-step02-parameter-map48.json \
  --frozen-direction data/phase_ring_continuation/type_fixed_step02_d5_actual_parameter_direction.npz \
  --origin-certificate data/phase_ring_continuation/type_fixed_step02_d5_jet_core_N_interval.json \
  --parameter-radius .01 --out /tmp/D5-parameter-N-replay.json

OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_parameter_root_interval.py \
  --inputs data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz \
  --frozen-direction data/phase_ring_continuation/type_fixed_step02_d5_actual_parameter_direction.npz \
  --out /tmp/D5-parameter-root-replay.json

OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_N_tube_membership.py \
  --checkpoint data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton128_probe.npz \
  --candidate-inputs data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton128_interval_inputs.npz \
  --origin-inputs data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz \
  --frozen-direction data/phase_ring_continuation/type_fixed_step02_d5_actual_parameter_direction.npz \
  --tube-certificate data/phase_ring_continuation/type_fixed_step02_d5_parameter_N_interval.json \
  --out /tmp/D5-rounded-predictor-N-membership.json
```

本结果支付的是同一真实参数族的实核心图表及共同根邻域。返回映射的
复域、ODE 误差、实际参数共轭的 Wiener 残差和二阶 Taylor 常数仍须在
各自明确的同一对象上继续支付。曲面的精确等距方程、完整 PDE 传递、
闭曲面粘接及可见幅度和 reach 完成标准均未由本文解决。
