# 物理径向 bump 场的明确原生定义及实际 body 入口

状态：**原生有限场与 C² 位置图的定义；浮点评估入口。**
本件没有求解新 BVP，没有对当前失败或未收敛场重复运行完整 body。
任何实际全段 body 结果必须另有真实运行报告；此处不预付连续等距、reach 或闭缝。

新增文件：

- `scripts/fd2d_gc_bump_native_field.py`：`RawBumpNativeField`；
- `scripts/fd2d-metric-bump-body-screen.py`：未来真实候选的固定材料角 body 入口；
- `scripts/fd2d-metric-bump-native-check.py`：已有输入的字段/导数小检查。

原 `fd2d_gc_raw_native_field.py`、当前 provider 和原 body 几何消费者均保持不变。

## 1. 准确参数与网格身份

参数向量是
$$
[c_1,\ldots,c_K,\ b_0,\ldots,b_K,\ \delta_1,\ldots,\delta_J].
$$
这里最后一个参数是物理径向扰动量 $\delta_J$，不是 coast 参数 $T$。
`fixed_base_T` 仅标识已给定 base candidate 的固定 coast；新 reader 核对该
标识和 candidate SHA，而实际目标直接读取保存的 base profile 加上 bumps：
$$
a_\delta(s)=a_{\rm base}(s)+\sum_{j=1}^J\delta_j\psi_j(s),\qquad
g_\delta=ds^2+a_\delta(s)^2du^2.
$$
$\psi_j=1024q_j^5(1-q_j)^5$ 位于实际保存的 support 上，外部为零。
径向坐标恒为 **$x=s$、$J=S_x=1$**；不应用 coast 时钟，也不要求 $|a_s|\le1$。
$a_\delta>0$ 的全域证书仍由实际外设计/连续消费者提供，reader 只拒绝请求点的非正半径。

必须明确保存或由调用者报告绑定以下字段：candidate SHA、`profile_supports`、
`fixed_base_T`、`profile_kind=physical_bumps`、`tail_kind=positive_bernstein`、
`base_kind` 和固定角图册的 `blend`。若 archive 与调用者同时给值，两者须相同。
所有 $\delta_j$ 从实际 archive 原样保留。定义 JSON 记录完整参数块、来源、
准确中央 moments/means 包、profile 源、两端保护区和字段 SHA。

**保存的 NPZ mesh 就是 P1 场的实际定义。** Reader 不调用 factory 的 mesh builder，
不补点、不删点，也不静默消去近重复节点。原 tiny-cell 场和以后明确 P1 重采后的
clean-mesh 场是不同的有限表示，分别绑定其 SHA。新 reader 可消费任意严格递增
且覆盖同一实际径向域的保存 mesh。

## 2. 全 lifting、独立三场与真实导数

在每个实际保存的径向格，所有 Fourier 修正系数作准确 P1 插值。
三场仍为独立的 $n,m,l$；完整中央/尾 lifting 与旧 reader 相同，绝不把完整尾函数
换成有限角模投影。固定角图册为
$$
u=U(s,\xi)=(1-\beta(s))U_*(\xi)+\beta(s)\xi,
$$
其 $\beta$ 和基准 $U_*$ 均独立于 $\delta$。
继承的 `evaluate_native` 给出 $(n,m,l)$ 的实际 $s$、$\xi$、
$\xi\xi$、$s\xi$ 导数，径向导数使用所选相邻格的真实 P1 斜率。
`physical(s,u)` 反解同一个单调 $U$，并用
$$
f_u=\frac{f_\xi}{U_\xi},\qquad
f_{uu}=\frac{f_{\xi\xi}-f_uU_{\xi\xi}}{U_\xi^2},\qquad
f_s\big|_u=f_s\big|_\xi-\frac{U_s}{U_\xi}f_\xi.
$$
任何格边界的字段值和全部角导共享；只允许径向一侧导数跳变。
这与 R133 中已给的 P1 原生定义相同，不能通过更改 mesh 隐藏残差。

## 3. 实际 C² 位置图及固定材料角 24 态

使用 R119/R124 的真实定义
$$
F_s=FA,\qquad X_s=Fe_1,
\qquad A=[\alpha]_\times,\quad \alpha=(m,-l,0).
$$
令 $r=\operatorname{vee}(F^TF_u)$、$b=F^TX_u$、
$v=r_u$、$q=b_u$，则
$$
\begin{aligned}
r_s&=r\times\alpha+\alpha_u,&
b_s&=-\alpha\times b+r\times e_1,\\
v_s&=v\times\alpha+r\times\alpha_u+\alpha_{uu},&
q_s&=-\alpha\times q-\alpha_u\times b+v\times e_1.
\end{aligned}
$$
实际位置二 jet 是
$$
X_s=Fe_1,\quad X_u=Fb,\quad X_{ss}=Fl e_3,\quad
X_{su}=F(r\times e_1),\quad X_{uu}=F(r\times b+q).
$$
此处 $n$ 不被当成实际 $X_{uu}$ 的捷径。即使有限 Gauss/Codazzi 未为零，
这些方程仍定义一个可计算的实际图，并能独立显示其真实 Gram 误差。

共享 P1 值使 $l,m$ 及所需角导跨径向格连续；角图册光滑且单调。
线性 frame/角变分 ODE 的连续系数给上述 $F,r,b,v,q$ 的连续解。
从所列公式直接得到 $X$ 的全部连续二导，故图是 C²；无需把 II 强迫成全局 C¹，
也不需要 C³ 曲面。浸入、嵌入、等距误差、reach 和尾缝是另外的真实几何条件。

## 4. body CLI 和输出语义

```bash
python3 scripts/fd2d-metric-bump-body-screen.py \
  --field notes/<actual-field>.npz \
  --report notes/<true-producer-report>.json \
  --out-prefix notes/<fresh-body-stem> --angles 32
```

`--angles` 支持 8/16（入口小检查）及 32/64。输入 field SHA 必须出现在实际 producer
报告中；candidate 和实际固定图册也由该报告/archive 绑定。
使用保存的 P1 mesh 分割真实 body ODE；每次 stage 都计算完整物理 profile 与完整
角图册/lifting。光滑 profile、图册或 lifting 的内部位置不必成为额外 ODE 分格，
因此不会把 clean producer 明确去掉的近重复 blend 点作为人工 tiny-cell 再插回。
这只是浮点适应积分的分格选择，场和物理度量从未改变。

实际 Gram、法向和曲率完全复用已运行过独立精确尾检查的原 body consumer：
曲率相对真实诱导 Gram 求，不把形式矩阵的两个特征值冒称实际曲率。
cut 用同材料角的一次 proper position-only 刚体 SVD 对齐；同一 $Q,t$ 应用于
全部六个 Cartesian jets 和法向，明确报告 tilt 与水平平移，不强制它们为零。
输出每格端点 checkpoint、全部实际采样、cut 二 jet、输入定义、report 和失败原因。
仅因程序退出 0 不表示强目标通过。

本件不运行当前未收敛场的完整 body；该入口留待有用实际候选。

## 5. 本次实际小检查与真实退出

输入为已保存的 `...raw-bump-jvp01-warm.npz`，候选 SHA 为 `7c3f31de...88bfd1`。
另存明确测试 fixture，把其 7 个外参数设为
$\delta_j=.0003\cos(.7+1.3j)$，保持原 mesh、修正和其余参数；这不是 accepted 状态。

第二次实际检查 **82243 / 595cb4，退出 0，16.728 秒**：

- 原生全部节点场与实际 `RawBumpDAE` 相差至多 $2.043\cdot10^{-14}$；
- 完整一阶角 jets 相差至多 $3.287\cdot10^{-13}$；
- 固定物理材料角的径向链式导数，三个场的 scaled $L^2$ 差均小于
  $8.403\cdot10^{-10}$，全部定义参数保留且实际 $J=1$；
- 格两侧共享值、角一/二导完全相同，definition 往返求值逐位相同；
- 全 cut II 与自身完整尾相差至多 $4.441\cdot10^{-16}$，这不是 Cartesian 缝已闭；
- 已实际调用固定材料角 24 态 RHS 和初端实际位置二 jets，全部有限；没有积分 body。

第一次 **84705 / 7bdae5，退出 1**，在最终 JSON 序列化时遇到 NumPy boolean
不能由标准 JSON 编码的问题。测试 fixture 和 definition 已写，但没有完整数值报告，
故不引用其未保存检查值；原 checker 源副本和失败回执保留。修正只把 `checks` 值
转换成原生 Python bool 后，以新 stem 重新真实执行。

body CLI 另实际完成 `--help` 导入检查（38015 / 2183ab，退出 0），未运行积分。
完整 report、fixture、definition、来源 SHA 和退出回执列在本组 manifest。

后续若 producer 更换 seed lifting 的衰减区间，须有明确新定义与对应 reader，不能
把本件旧权重 `1-S5(s/min(.55,.4end))` 的结果直接转借新表示。

