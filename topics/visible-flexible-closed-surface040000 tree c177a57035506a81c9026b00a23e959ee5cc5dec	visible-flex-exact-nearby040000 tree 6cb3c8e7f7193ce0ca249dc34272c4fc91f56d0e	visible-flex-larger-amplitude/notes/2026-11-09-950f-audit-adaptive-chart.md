# 独立审查：随经线变化的固定角图及完整二阶链式法则

2026-11-09，Astra-visible-flex-950f9f73 / independent_audit。
审查者未参与 chart 设计、prefix 求解或尾部优化。

**结论：PASS，限于坐标工具、导数转换及已列出的程序诊断。**
这不证明任何大振幅 prefix 或完整闭曲面已解出。
审查对象为 `scripts/950f-prefix-adaptive-chart-bvp.py` 的
`geo`、`frame`、`velocity_s` 与 `audit`，以及冻结的
`notes/2026-11-09-950f-prefix-adaptive-chart.json`。源文件审查时的
哈希保存在同前缀 JSON；后加的 restart/求解器逻辑不由该哈希
自动覆盖。

## 1. 正确的物理微分算子

令 $\widetilde F(s,\psi)=F(s,\theta(s,\psi))$，其中
$$\theta=\psi-\frac{e(s)}3\sin3\psi,\quad
\rho=\theta_\psi>0,\quad v=\theta_s/\rho.$$
保持物理材料角不变时的导数算子为
$$D_s=\partial_s-v\partial_\psi,\qquad
D_\theta=\rho^{-1}\partial_\psi.$$
二者可交换，因为 $\rho_s=\theta_{s\psi}$。
直接展开得到
$$F_s=\widetilde F_s-v\widetilde F_\psi,\qquad
F_\theta=\widetilde F_\psi/\rho,$$
$$F_{\theta\theta}=
\frac{\widetilde F_{\psi\psi}}{\rho^2}
-\frac{\rho_\psi\widetilde F_\psi}{\rho^3},$$
$$F_{s\theta}=
\frac{\widetilde F_{s\psi}-v_\psi\widetilde F_\psi
-v\widetilde F_{\psi\psi}}{\rho},$$
$$F_{ss}=\widetilde F_{ss}-2v\widetilde F_{s\psi}
+v^2\widetilde F_{\psi\psi}
+(vv_\psi-v_s)\widetilde F_\psi.$$
候选代码逐项实现了这些式子。特别是最后一项不能漏掉；本次核查
没有发现漏项或符号错误。

固定材料角下的 Frenet 法向速度记为 $V$，则 chart 速度必须是
$$W=V+v\widetilde F_\psi.$$
代码 `frame` 用 `Vnormal` 保存 $V$，用 `V` 字段保存完整 $W$，
供继承的平均高度积分使用。这样 $h_s=\operatorname{mean}_\psi W_z$
中包含了输运项，不会错误地只积分 $V_z$。

沿所给 coefficient 曲线对 $W$ 求导时，代码先对 Frenet 场使用
已核 JVP，并补上 $a,a'$ 的显式经线依赖，再加入
$v_s\widetilde F_\psi+v\widetilde F_{s\psi}$。其 `velocity_s`
与上述求导一致。`geo` 的背景圆项及 $s,\psi$ 混合导数也逐项
核对通过。

## 2. 全经线的 chart 可逆性，不依赖采样

冻结 chart 定义为归一化变量 $x=s/L$ 上的 clamped $C^2$ 三次样条
$h(x)$ 乘末段五次 cutoff $c(x)$，再乘 $e_0=16/25$。
$c(x)=1$ 到 $x=3/4$，随后用 $1-S(4x-3)$，其中
$S(u)=10u^3-15u^4+6u^5$。它满足 $0\le c\le1$，且两个拼接端
的一、二阶导数均匹配，因此 $e(s)$ 是 $C^2$。

对输入中的 binary64 节点和值按精确有理数解释。设节点间距为
$h_i$、割线斜率为 $q_i$，端点斜率为 $d_0,d_N$，样条节点二阶
导数为 $M_i$。标准 clamped 三对角系统的对角优势给
$$\max_i|M_i|\le B:=\max\left\{
\frac{6|q_0-d_0|}{h_0},
\frac{6|d_N-q_{N-1}|}{h_{N-1}},
\frac{6|q_i-q_{i-1}|}{h_i+h_{i-1}}
\right\}.$$
理由是在 $|M_i|$ 取最大值的行，把非对角项全部移至右侧；该行
对角系数减非对角绝对和正好是上述分母。样条二阶导数在每个
节点区间线性，所以同一 $B$ 控制整个区间的 $|h''|$。

与线性插值比较的 Green 函数估计进一步给
$$\|h\|_\infty\le \max_i|y_i|+rac{B\max_i h_i^2}{8}.$$
自写的 `scripts/950f-audit-adaptive-chart.py` 用 `Fraction` 独立
比较，得到显示值
$$B\le103.971802,\qquad \|h\|_\infty\le1.003172968,$$
并以精确有理比较证明
$$\rho=1-e(s)\cos3\psi
\ge1-\frac{16}{25}\|h\|_\infty
>\frac{357}{1000}.$$
这覆盖整个 $s,\psi$ 域，且不依赖正经线长度 $L$ 的取值。
它认证的是上述输入定义的精确样条；浮点线性代数与求值误差尚是
另一个数值问题，不在这里假装已做区间包络。

在 cut $x=1$，$c=c'=c''=0$，因此严格有
$e=e_s=e_{ss}=0$。故恢复材料角的所有一、二阶链式修正均为零，
原物理 DN 坐标及 two-jet 接口在这里恢复。非线性尾的平均高度
斜率本身仍需匹配，本坐标论证不能代替它。

## 3. 独立重跑的程序检查

独立运行提供的 `950f-prefix-chart-twojet-check.py`，输出另存为
`notes/2026-11-09-950f-audit-chart-twojet-rerun.json`。精确旋转背景
恢复 $F_s,F_\theta,F_{ss},F_{s\theta},F_{\theta\theta}$ 的最大误差
分别约
$$2.23\cdot10^{-16},\ 2.23\cdot10^{-16},\ 1.78\cdot10^{-15},
\ 1.39\cdot10^{-15},\ 2.05\cdot10^{-15}.$$
制造的 coefficient 曲线对 `velocity_s` 的中心差分误差，在
$10^{-4}$ 到 $1.25\cdot10^{-5}$ 四个步长上依次约为
$3.65\cdot10^{-6},9.12\cdot10^{-7},2.28\cdot10^{-7},5.70\cdot10^{-8}$，
符合步长减半时误差除以 4。

此检查覆盖背景、非零随机 coefficient 曲线的导数链和曲率计算
所需的二阶转换；它没有证明待求 BVP 存在或收敛。计算中的 FFT
l1 仍须按实现者已修订的措辞称为有限角采样诊断。
