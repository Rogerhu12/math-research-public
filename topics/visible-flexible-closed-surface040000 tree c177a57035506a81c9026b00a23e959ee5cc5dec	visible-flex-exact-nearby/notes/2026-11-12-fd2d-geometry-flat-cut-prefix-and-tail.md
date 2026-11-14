# 精确平尾与实际有限平切口前缀输入

2026-11-12，constructive_geometry。本记录闭存本轮物理输入与两个已完整证明的几何/坐标结果。它不是已经求成的强幅非圆闭核。

## 当前可直接消费的实体

`2026-11-12-fd2d-flat-cut-prefix-v1-coast-compatible-candidate.json`
的 SHA-256 为
`a92b552f70bcc26c97f16261fbc78fac10c1daad6d72eafc8063dcb093cdd147`。
它与最初 `...flat-cut-prefix-v1-candidate.json` 的物理度量逐项相同，只恢复旧 coast 接口需要的 `cut_second_jet_brake` 标签，并添加 `cut.tail_height_span=0`。这个零仅指 $A=0$ 的旋转平尾背景；非零 $A$ 的切口高度是 R128 的完整角函数，不能用这个标量字段代替。

当前 scalar reader、coast 参数和完整初始化的用途分别为：

- `fd2d_frozen_ellipse_candidate.py::Candidate` 读取冻结段函数；
- `fd2d_gc_design_profile_positive.py::CoastDesignProfile` 使用 R131 的正径向坐标并返回完整 $T$ JVP；
- `fd2d_flat_cut_prefix_candidate.py::FlatCutCandidate(bundle).reference(s,u)` 给不除 $b,n$ 的旋转初始位置、标架和两 jet。

原生场顺序为
`[l,m,n,X[3],e1[3],e2[3],N[3]]`，总计 15 分量。旧 14 场正 $n$ reader 不能仅凭标签恢复 $l=(m^2+K)/n$。

## 真实前缀与平切口

中央周长半径仍由原准确椭圆定义给出，$a_0\simeq1.0040828380214688$。前缀保留原反馈 Hermite 段；中央直柱长度改为 $.5$。收缩阶段使用连续相位导数的三段 `phase_bridge`，控制径向速度到 $-.4$，相位曲率设计值 $6.8$；早回转采用 $3.4$。浅直行段参考长度为 $T_0=.02$，再下转到相位 $-1.45$，最后直行段的实际长度为 $.02062650307234244$。

最终长度 $.04$ 的相位 Hermite 段准确以

\[
\phi(0)=-1.45,\quad\phi(1)=-\pi/2,
\quad \phi_s(0)=\phi_s(1)=0
\]

定义；输入额外写明 `exact_endpoint_phase='-pi/2'`，小数只是数值 reader 的求值形式。由三次端值插值，在终点有

\[
\phi+\pi/2=O((s_c-s)^2),\quad
\phi_s=O(s_c-s),\quad
b=\cos\phi=O((s_c-s)^2).
\]

因此 $a_s=\sin\phi\to-1$，$a_{ss}=\cos\phi\,\phi_s\to0$，旋转背景的两个主曲率 $-\phi_s,b/a$ 都趋零；其完整 Cartesian 两 jet 与 $A=0$ 的平尾连续匹配。没有在最后一点调用除 $b$ 的线性方程。

实际生成报告给：前缀弧长 $1.344258724456249$，旋转背景 cut 高度 $1.202982473751077$，径向 cut 两 jet 准确返回 $(.8,-1,0)$。采样最大旋转经向曲率约 $6.8$。32 个角点的 $X,X_s,X_u,X_{ss},X_{su},X_{uu}$ 与平圆 cut 完整表达式之差均为零。这里的采样几何不冒充待求非圆图的曲率或 reach。

最初生成执行的完整报告已落盘；本次恢复未保留最初工具的 exit 回执，因此不补造该退出状态。其后独立兼容 reader 检查实际 session 97448 / chunk 46d2ef 返回 exit 0；实际初始化了 `CoastDesignProfile`，核对原/兼容物理标量逐位一致，且 $T=.018,.02,.022$ 的 cut 两 jet 和两段正长度成立。随后 R131 的真实检查亦已 exit 0，见正式结果的执行身份。

## 已支付的尾和仍需求解的中段

R128 的尾是准确平坦共同度量 $dr^2+r^2du^2$ 上的广义柱弯，$.32$ cuff 外还有至 $.34$ 的完整固定平领。R130 完整证明在 $A\le1.2$ 时，包含该尾的完整柱面 reach 至少 $736/4725>.136$，并给尾内部/平盘—尾/上下尾点对法球、球包、相位零板宽和低高度 held 条件。尾 alone 的相位像集彼此全等；最终欧氏非全等量仍来自活动核心与固定非轴对称帽。

旧三类稿件的可用结论必须区分：

1. `db6f-horizontal-core-finite-flat-collar-v1` 从真实水平核心给有限平坦领，但出口仍是小正斜率和正第二形式；不能当成当前 $a_s=-1$、含零角弧的欧氏平尾。
2. `db6f-positive-k-centered-cap-flat-outlet-v1` 构造真实正曲率有心帽和近单位正斜率出口；反向接入要改变斜率符号并匹配完整位置/标架/两 jet，旧稿没有替这个全函数边值问题给解。
3. `db6f-flat-outlet-ruling-continuation-v1` 证明正秩一第二形式沿有限正常纯平坦母线延拓仍非零，并给锥角 holonomy 约束。这只限制该纯平坦延拓路线，未排含真实非平度量段的新桥。

当前输入确实从中央 $a_s=0$ 经非平段到达 $a_s=-1$，所以没有重复以上直接贴接错误。但这个 scalar 物理候选本身不证明大非圆中央数据能同时达到 R128 的全部 cut 两 jet。原生 $(l,m,n)$ 边值问题、全域真实度量精度、前缀内部与前缀—尾跨片法球、实际 held 和固定帽条件仍须由实际解支付。

## 固定 $g$ 与计算坐标

调整 $T$ 改变的是物理前缀设计。R131 在同一个固定 $T$ 下替换计算坐标，允许整个 $0<T<T_{\max}$，其中 $T_{\max}\simeq.22510364412376974$。新 reader 没有改变任何段的物理函数；它只解除旧五次参数映射的额外可逆性门。

最终非圆解若选择了新的 $T$，应冻结其完整 candidate 后再做同一个 $g$ 的精度序列；若从旧计算坐标续算已有场，须按真实物理 $s$ 重采样。相关准确逆式和 JVP 已在 R131 完整给出。
