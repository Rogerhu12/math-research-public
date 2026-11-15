# R165：预设 h 路径后的完整 k 二次型与 log-linear 频率门

日期：2026-11-15。**已证明。** 原支撑只读取已经发表的完整 head 元数据；证明不执行新的 profile 评价、响应编译、路径积分或候选优化。

以下定理以完整真权 −2 最高层的明确支撑为输入，保留所有加速度、面积及速度四次项。它给出一条专门用于当前字符候选的检验：先预设任意正函数 h(s)，完整最高 action 对 k(s) 成为一个常数加齐次二次泛函；在有限但任意长的 log-linear h 段上，共轭后得到一个准确的一元二次多项式门。

这里“预设 h”指预先选定整个正路径 h(s)，允许 h 非常数。若 h 真为常数，下式退化为已经知道的 $d\int h^{-2}(k'')^2$；本稿的新增内容来自非常数 h 的全耦合。

依据 [R137](../results/R137-real-fast-pulse-positivity-and-acceleration-PSD.md)、[R140](../results/R140-full-action-multiplier-equivalence-for-real-cost-positivity.md)、[R141](../results/R141-affine-character-acceleration-covariance-and-J-positivity.md)、[R148](../results/R148-sharp-one-dimensional-highest-action-positivity.md)、[R163](../results/R163-complete-normal-coefficient-cocycle-and-single-weight-character-head.md)、[R164](../results/R164-covariant-eight-matrix-multiplier-for-positive-affine-characters.md) 和 [首次完整 head actual](../notes/character-head-minus2-first-complete-actual-20261115.md)。

## 0. 本次只读的完整 Q4 元数据

来源为公开 run [43665345551](https://github.com/Rogerhu12/math-research-public/actions/runs/43665345551)，源提交 `0aae9a6a85583a9f87415e586d8db2c9c7fea6a7`，lane `character_head_minus2`。完整原导出是

```text
notes/actions-43665345551-1-character_head_minus2/
character-head-minus2-original-expressions.json.gz
```

压缩 1,247,411 字节，SHA256 `2c1242e13d253ba352c7ff1b025a91cf564ab2a7cfd93c6bcedc19baa5fac45c`；解压 6,560,138 字节，SHA256 `7a93a53aa7fafa1cff76608aceaeac294911ca4f828746913c1b125ae2fd33af`。schema 为 `visible-flex-complete-character-head-minus2-v1-original-expressions`，完整十四族 gate 为真。

设 $V_i$ 表示该导出 `normal_family_records` 中 index=i 的完整两模式系数。七条 Q4 记录准确是：

| index | 族 | 状态单项 |
|---:|---|---|
| 100 | $Q4_2$ | $h^{-4}$ |
| 101 | $Q4_3$ | $h^{-5}k$ |
| 102 | $Q4_3$ | $h^{-4}\omega$ |
| 103 | $Q4_4$ | $h^{-6}$ |
| 104 | $Q4_4$ | $h^{-6}k^2$ |
| 105 | $Q4_4$ | $h^{-5}k\omega$ |
| 106 | $Q4_4$ | $h^{-4}\omega^2$ |

$Q4_i$ 乘 $h_s^i k_s^{4-i}$。两族 $Q4_0,Q4_1$ 在完整原导出中均为原式零；这些七项没有其他状态键或 log 项。原根名是 `normal_00100_mode_-4/-2` 至 `normal_00106_mode_-4/-2`，每条均保存两个原 hash；本稿只读它们的状态键和已发完整性标记，不重新评价原根。

R163 的平移协变使一个真实字符在这些族的取值与 $\omega$ 无关，故 $\lambda(V_{102})=\lambda(V_{105})=\lambda(V_{106})=0$。这不是原 $V_i$ 自身为零。A/H 的十条已发支撑在本导出对应 index 90–99，按 R141 依次是 $J_0,\ldots,J_9$。下节的十个标量据此准确对应

$$
(a,b,c,d,e,f,g,j,\ell,m)
=\lambda(V_{90},V_{91},V_{94},V_{96},V_{97},V_{99},V_{100},V_{101},V_{103},V_{104}).
$$

其中 $a=\lambda(J)$、$d=\lambda(J_6)$；$\ell$ 对应完整轴向 D0 的原根。这样每个后继候选都可由已存精确坐标直接读取这十个数，不新增研究计算。

## 1. 真实字符与十个最高层标量

设 $\lambda:U\to\mathbb R$ 是定义在真实完整成本空间上的实仿射字符，满足

$$
\lambda(R)=0,\qquad \lambda\mathsf P_{H,d_0}=H^{-2}\lambda
\quad(H>0,d_0\in\mathbb R).
\tag{1}
$$

用 $d_0$ 表示群平移参数，以免与下面的最高层系数 d 混同。暂不假定字符正；正性只用于把后面的准确恒等式变成必要不等式。

R141 的 A/H 原支撑、完整 head 的 Q4 原支撑，以及 R163 的最高十族协变，给出十个实数

$$
a,b,c,d,e,f,g,j,\ell,m
$$

使完整已取 $\lambda$ 的最高正规密度为

$$
\begin{aligned}
L_4^\lambda={}&h^{-4}(a+bk^2)h_{ss}^2
+c h^{-3}k h_{ss}k_{ss}+d h^{-2}k_{ss}^2\\
&+(e h^{-4}k h_s+f h^{-3}k_s)
 (h_s k_{ss}-k_s h_{ss})\\
&+g h^{-4}h_s^2k_s^2+j h^{-5}k h_s^3k_s
+h^{-6}(\ell+mk^2)h_s^4.
\end{aligned}
\tag{2}
$$

这些系数是同一个 $\lambda$ 对完整原算子的评价，不是可以独立指定的成本控制。式 (2) 使用已经含 $-\mathcal B_{m_2}N^{[2]}$ 与完整边界势微分的正规速度四次式。既不以 raw $Q_4^v$ 代替它，也不删除 e、f 面积项。

令

$$
r=\log h,\qquad v=r',\qquad z=r''+(r')^2=v'+v^2,
\qquad \rho=e^{-2r}=h^{-2}.
\tag{3}
$$

真实水平变量依旧满足

$$
\omega(s)=\omega_*+\frac12\int_{s_*}^s \frac{k'(t)}{h(t)}\,dt.
\tag{4}
$$

不是固定 $\omega$。因为 (1) 的平移不变性已经使所有已取 $\lambda$ 的最高正规系数与 $\omega$ 无关，(4) 保证这些标量路径确能用于原问题，而不会在 (2) 中产生漏项。

把 $h_s=hv,h_{ss}=hz$ 代入，得到

$$
\begin{aligned}
L_4^\lambda=\rho\{&a z^2+\ell v^4+d(k'')^2
+(c z+e v^2)kk''+f v k'k''\\
&+(g v^2-f z)(k')^2+(jv^3-e v z)kk'
+(b z^2+m v^4)k^2\}.
\end{aligned}
\tag{5}
$$

这是对全部 k、k′、k″ 的准确至多二次式。特别没有把面积项按定号假设估计掉。

## 2. 对任意预设 h 的准确四阶二次型

取有限区间 $[s_-,s_+]$。设 $h>0$ 光滑且在两个端部开邻域各为常数，k 也在两个端部开邻域各为常数；左右常数允许不同。定义

$$
I_0[h]=\int_{s_-}^{s_+}\rho(a z^2+\ell v^4)\,ds,
\tag{6}
$$

$$
P_h=\rho[(g-e-c)v^2-(c+\tfrac32 f)v'],
\tag{7}
$$

$$
Q_h=\rho(b z^2+m v^4)
+\frac12[\rho(cz+e v^2)]''
-\frac12[\rho(jv^3-e v z)]'.
\tag{8}
$$

则完整 action 满足

$$
\boxed{\int L_4^\lambda\,ds=I_0[h]+\mathscr Q_h[k],\qquad
\mathscr Q_h[k]=\int[\rho d(k'')^2+P_h(k')^2+Q_h k^2]\,ds.}
\tag{9}
$$

**证明。** 在 (5) 置

$$
A=cz+e v^2,\quad B=fv,\quad
C=g v^2-fz,\quad D=jv^3-e v z,\quad E=bz^2+mv^4.
$$

三项准确分部积分分别是

$$
\int\rho A kk''
=-\int\rho A(k')^2+\frac12\int(\rho A)''k^2,
$$

$$
\int\rho Bk'k''=-\frac12\int(\rho B)'(k')^2,
\qquad
\int\rho Dkk'=-\frac12\int(\rho D)'k^2.
$$

全部边界项确实为零：k′ 在端部为零，且 h 常值 germ 给 $v,z,A,B,D$ 及所需导数为零；故即使 k 的左右常值非零，也没有残留 $k^2$ 端点势。于是

$$
P_h=\rho(C-A)-\tfrac12(\rho B)',\qquad
Q_h=\rho E+\tfrac12(\rho A)''-\tfrac12(\rho D)'.
$$

利用 $\rho'=-2v\rho,z=v'+v^2$，第一式化成 (7)，第二式即 (8)。证毕。

式 (8) 可以含 h 的高阶导数，但它们只是已经固定的 h 路径的二次型系数；没有新增原 action 的未知几何 jet，也不要求重建任何 profile 原根。对紧支撑测试 k，对应形式对称算子可写为

$$
\mathscr L_h k=(\rho d k'')''-(P_h k')'+Q_h k.
\tag{10}
$$

本稿不用未选定边界实现的谱声明，后面的结论直接由 (9) 的积分式证明。

## 3. 二次型负方向如何排除正字符

对每一固定 h，$\mathscr Q_h$ 是齐次二次泛函，因此

$$
\int L_4^\lambda[h,Kk]\,ds=I_0[h]+K^2\mathscr Q_h[k]
\quad(K\in\mathbb R).
\tag{11}
$$

由此，最高 action 对全部真实平端路径非负，当且仅当

$$
I_0[h]\ge0\quad\hbox{且}\quad\mathscr Q_h[k]\ge0
\tag{12}
$$

对全部正平端 h、全部平端 k 同时成立。必要性先取 k=0，再在任一负二次方向上令 |K| 足够大；充分性直接来自 (9)。 由 R148 已证明的准确一维判据，第一项对全部正平端 h 非负等价于 $a\ge0$ 且 $\ell+25a/9\ge0$；这只是复用该已付判据，新的全耦合义务是所有 $\mathscr Q_h[k]\ge0$。它是本权已发表支撑带来的准确二次化，不需要先固定一条完整状态曲线再改变时速。

若某个确定的有限平端形状满足 $\mathscr Q_h[k]<0$，先固定这两个形状，再选一个有限 K，使

$$
K^2>\frac{\max(I_0[h],0)+1}{-\mathscr Q_h[k]}.
\tag{13}
$$

此时完整最高 action 严格负。按 (4) 选定真实 $\omega$ 后，h、Kk、$\omega$ 的像仍是一个有限紧集，所有端口都是合法常值 germs。可在这一步之后为这个有限路径与补偿族统一选择允许的共同 profile 带；不需要给尚未选择的无穷长段或无穷振幅预先固定一个包络。

最后作真实正时长缩放 $s=\delta t$，先前已经固定的三个 action 层按

$$
\delta I_0^{\rm full}+\delta^{-1}I_2^{\rm full}
+\delta^{-3}I_4^{\rm full}
\tag{14}
$$

变化，其中 $I_4^{\rm full}<0$。R137 的真实矩阵/frame 补偿与倒行去第三成本，使负的 $\delta^{-3}$ 项压过完整低阶及桥成本；R140 的同一乘子也不能改变最高层。故一个真正正字符不可能具有这样的负二次方向。

顺序是：**有限形状先固定，k 的有限振幅其次，时长缩放最后。** 不将渐近负值直接当作一条已闭合的原路径，也不假定高次 history 在单纯拼接时消失。若坐标只是有限必要系统的外候选，(13)–(14) 排除的是它成为真实正字符的可能性；未证明该外候选本身已定义 U 上的泛函。

## 4. 有限 log-linear 段上的常系数化

在 k 的紧支撑所处的一个开区间内，规定

$$
r(s)=r_*+\tau s,\qquad \tau\ne0.
\tag{15}
$$

因此 $v=\tau,z=\tau^2$。h 在这一区间外可以光滑变成两个常值 germs；这不会影响支撑于内部的二次型测试。由 (7)–(8)，在线性段上

$$
P_h=\rho(g-e-c)\tau^2,
$$

$$
Q_h=\rho(b+m+2c+e+j)\tau^4.
\tag{16}
$$

取任意实 $y\in C_c^\infty$，令

$$
k=e^r y.
\tag{17}
$$

有 $k'=e^r(y'+\tau y)$、$k''=e^r(y''+2\tau y'+\tau^2y)$。把这些代入 (9)，共同 $\rho=e^{-2r}$ 与 $e^{2r}$ 准确消去。再用 y 的紧支撑消去所有边界项，得到

$$
\boxed{\mathscr Q_h[e^r y]
=\int\left[d(y'')^2+\beta\tau^2(y')^2+\gamma\tau^4y^2\right]\,ds,}
\tag{18}
$$

其中

$$
\boxed{\beta=2d+g-e-c,\qquad
\gamma=d+g+b+m+c+j.}
\tag{19}
$$

完整 f 面积项在这个特定 log-linear 子类中成为准确总导数，故它从 (18) 中消失；它在一般 h 的式 (7) 仍然保留。e 面积项进入 $\beta$，c 混合加速度项进入 $\beta,\gamma$，速度四次 g、j、m 也全部保留。$a,\ell$ 属于常数部分 $I_0[h]$，不能从完整 action 删除，但由先选定形状后的振幅步骤 (13) 精确支付。

## 5. 一元频率多项式的准确必要门

定义

$$
\boxed{\mathcal P(t)=d t^2+\beta t+\gamma.}
\tag{20}
$$

**定理。** 式 (18) 对任意有限 log-linear 区间、任意紧支撑 y 非负，当且仅当

$$
\boxed{\mathcal P(t)\ge0\quad\hbox{对全部 }t\ge0.}
\tag{21}
$$

其等价标量条件为

$$
\boxed{d\ge0,\qquad \gamma\ge0,\qquad
\beta+2\sqrt{d\gamma}\ge0.}
\tag{22}
$$

**充分性。** 二次多项式在半轴非负当且仅当 (22)；退化的 $d=0$ 或 $\gamma=0$ 也包括在内。由紧支撑积分分部，

$$
\begin{aligned}
&\int[d(y'')^2+\beta\tau^2(y')^2+\gamma\tau^4y^2]\,ds\\
&=\int(\sqrt d\,y''+\sqrt\gamma\,\tau^2y)^2\,ds
+(\beta+2\sqrt{d\gamma})\tau^2\int(y')^2\,ds\ge0.
\end{aligned}
\tag{23}
$$

**必要性与实际有限截断。** 若存在 $t_0>0$ 使 $\mathcal P(t_0)<0$，取固定非零实 $\chi\in C_c^\infty((-1,1))$，并令

$$
\xi=|\tau|\sqrt{t_0},\qquad
y_L(s)=\chi(s/L)\cos(\xi s).
\tag{24}
$$

支撑位于 $(-L,L)$。把导数展开，所有微分到 cutoff 的项都比主项低一阶 L；而 $\cos^2$、$\sin^2$ 的平均项给

$$
\lim_{L\to\infty}\frac1L\int
[d(y_L'')^2+\beta\tau^2(y_L')^2+\gamma\tau^4y_L^2]\,ds
=\frac{\tau^4}{2}\mathcal P(t_0)\int_{-1}^1\chi(x)^2\,dx<0.
\tag{25}
$$

该极限可直接由分部积分估计振荡项得到，不需要假定一个无限长真实路径。严格负的极限保证存在某个**有限** $L_*$，其二次型已经为负。若 $\mathcal P(0)=\gamma<0$，改用 $y_L(s)=\chi(s/L)$；除以 L 后极限为 $\gamma\tau^4\int\chi^2<0$，结论相同。

选定这个有限 $L_*$ 后，在 $[-2L_*,2L_*]$ 上令 $r=r_*+\tau s$，在更外侧用固定光滑截断接到常值 germs，取 h=e^r。该 h 处处严格正，虽然其最大/最小值可能相差很大，但整条有限路径仍位于 $h>0$ 的紧子集。令 $k=e^r y_{L_*}$，它在接缝前已恒零。于是取得一条真实有限平端的负二次方向，再依 (13) 选有限振幅，依 (14) 缩短时长。所有界面和端势已经支付。

因此 (21) 是真实权 −2 正字符的必要条件。它只是这个特别路径族的完整判据；即使 (21) 成立，仍不能保证一般预设 h 的二次型、静态/二次层或完整真实成本非负。

## 6. 对有限必要系统的最小使用方法

本门只需要已发最高层十个标量中的七个 $b,c,d,e,g,j,m$。它们均线性依赖于同一字符坐标；无需重新构造原响应、求新的 profile 值或重跑十四族。

最小新增行是选定一个有理 $t\ge0$ 后的准确线性必要式

$$
d t^2+(2d+g-e-c)t+(d+g+b+m+c+j)\ge0.
\tag{26}
$$

如果现有准确有理外候选已经使 (20) 在半轴某处为负，可以定向选择一条严格违反的有理 t 行；多项式连续性保证当存在严格负值时有这样的有理 t。该行的有效性由 (24)–(25) 的真实有限截断证明保证，不要求为加入这一行先在本地计算一个长指数路径积分。

若想一次保留整个半轴门，(22) 是一个小二阶锥条件。但本稿不新增求解依赖、不自动改动已冻结 consumer；当前流程可以只使用上述有根据的有理线性行。若候选不违反 (21)，应回到具体 $P_h,Q_h$ 或其他完整成本关系，而不是宣称它已正。

## 7. d=0 边界的一条附加准确推论

若一个真正正字符满足 $d=\lambda(J_6)=0$，R141 的逐状态加速度 PSD 先给 $c=0$。这不预设现有 J6 的头部类为零；它是条件命题。

在 d=0 时，(9) 的二次型没有 $k''$ 平方项。对固定 h，若某点 $P_h<0$，在其小邻域取紧支撑高频 k，则负的 $P_h(k')^2$ 主项压过有界的 $Q_hk^2$，与所有二次方向非负矛盾。因此必须 $P_h\ge0$ 逐点。

现在允许预设 h 的任意内部 jet。在某点取 $v=0$ 而让 $v'$ 分别为正负，式 (7) 在 c=0 下成为

$$
P_h=-\tfrac32\rho f v'.
$$

所以 $f=0$。再取 $v\ne0,v'=0$，得到 $g-e\ge0$。故

$$
\boxed{d=0\quad\Longrightarrow\quad c=0,\ f=0,\ g\ge e
\quad\hbox{对真正正字符成立}.}
\tag{27}
$$

这些内部 jets 可由一条正的光滑平端 h 实现；高频 k 的支撑在内部，真实 $\omega$ 仍由 (4) 积分给出。式 (27) 是本二次化在退化面的定向后果，不授 d=0 本身，也不把 $g=e$ 当作已证明。

## 8. 结论范围

新结论是当前完整真权 −2 支撑导致的准确 k 二次化、有限 log-linear 平段的一元频率门，以及 d=0 时的条件推论。原 $L_4$ 的所有 H、完整 Q4、同一真实水平约束和边界势均已保留。

本稿不宣称任何现有候选已经违反 (21)，不把外坐标候选当作 U 上已定义泛函，不宣布完整正字符不存在，也不授 J/D0/J6 的 signed control 或 period/ruling 完成。数值或有理候选的具体系数只应从已经发表的实际回执读取；下一消费只需要将那些准确数代入本门。
