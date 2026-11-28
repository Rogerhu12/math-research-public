# R87. 单级缓升速、k=1/2 准确圆弧与较长握持扫窗

维护：本次 `/root/design_continuation`；日期：2026-11-28。

**本条已证明新的条件几何输入与标量预算，未构造完成的闭族。** 改用一段较缓的上升加速，同时取准确圆弧曲率 $k=1/2$、材料半宽 $S=27/40$、过渡宽 $b=3/10$、相位端点 $\alpha_1=4/5$。该输入的首准确圆片在曲率小于12.3、支撑大于.087时已经耗尽保证保护窗；整个首升降周期另有全角 $|X|<1.34$ 的连续尺寸证书。若同一新物理输入最终支付完整闭面条件 $D_0\le2.68,\ X\cdot n\ge.087,\ |\kappa_i|\le12.3$，则 R54/R67 的短柱、固定标记及共同两 jet 接合给本条新的 H/held/reach 严格比例。

这里明确改变原 R55 的 profile。原两级升速在同一 r 盒的 $k=.5,S=.675$ 已有新的经典支 reach 排除，见[旧 profile 筛选](../notes/2026-11-28-design-higher-k-old-profile-screen.md)。本条既不重跑 R57，也不把可调 $\delta$ 当作取消其前提。所有非圆前缀 BVP、真正非线性 DN、尾、完整 C² 图和固定最终 g 的精化尚未在此新输入上执行。

## 1. 核心与有理参数

取三重、反射对称、严格凸、单位材料速度、周长 $2\pi$ 的 R53 核心，记
$$
T=2\pi/3,\qquad L=\pi/3,\qquad
k=\frac12,\quad S=\frac{27}{40},\quad b=\frac3{10}.
\tag{1}
$$
这些是材料角宽，不是法向角宽。$S+b=39/40<\pi/3$，可用
$\pi>333/106$ 精确确认。

设原支持 Fourier 参数满足
$$
A=\sum_{j\ge1}(9j^2-1)|a_j|\le\frac23.
\tag{2}
$$
于是原曲率半径 $\rho_0\in[1/3,5/3]$，原曲率
$\kappa_0\in[3/5,3]$。目标 $k=1/2<3/5$，所以 R53 的补偿 $\beta\ge0$。
其平滑窗口积分为
$$
J=2S+b=\frac{33}{20},\qquad
\frac{J}{T-J}<\frac{583}{157}.
$$
因此同一 R53 定义的全部 $0\le\lambda\le1$ 都满足
$$
\boxed{\frac12\le\kappa_\lambda<
3+\frac52\frac{583}{157}
=\frac{3857}{314}
<\frac{123}{10}.}
\tag{3}
$$
最后的严格余量为 $123/10-3857/314=13/785$。在 $\lambda=1$、curvature_blend=1 时，$|u-L|\le S$ 上准确为
$$
\Gamma(L+x)=O+2e^{i(L+x/2)}.
\tag{4}
$$
其存在、闭合与参数 jet 使用 [R53](R53-material-flattening-homotopy-and-positive-domain.md) 的已证明构造，不重新证明该构造。有限 Gauss 计算与 binary64 参数文件并不自动成为 (3)–(4) 的精确实现；具体实际场仍须按其完整来源和误差证书验收。Newton 参数若离开 (2)，本条核心上界也不再自动适用。

## 2. 新的完整参考 profile

仍用原 flat ramp 的同一个 $F$，$\eta=1/20$。其左、中央、右三段可写为
$$
F(t)=
\begin{cases}
\dfrac{t^3}{\eta^2(1-\eta)}
-\dfrac{t^4}{2\eta^3(1-\eta)},&0\le t\le\eta,\\[1ex]
\dfrac{t-\eta/2}{1-\eta},&\eta\le t\le1-\eta,\\
1-F(1-t),&1-\eta\le t\le1.
\end{cases}
$$
有 $F(0)=0,F(1)=1$、$F'\ge0$、$F'\le1/(1-\eta)$，且两端
$F'=F''=0$。每个 ramp 令 $v=v_0+(v_1-v_0)F(s/L_i)$。

参考 excursion $\delta_{\rm ref}=3/50$，明确六段为：

| 段 | 起速度 | 末速度 | 参考长度 |
|---|---:|---:|---:|
| 单级升速 | 0 | 9/20 | 10/57 |
| 上 coast | 9/20 | 9/20 | 1/855 |
| 上减速 | 9/20 | 0 | 4/45 |
| 下加速 | 0 | −1/2 | 2/25 |
| 下 coast | −1/2 | −1/2 | 1/25 |
| 下减速 | −1/2 | 0 | 2/25 |

第一段参考峰加速度和半径增量是
$$
B=\frac{9/20}{(10/57)(19/20)}=\frac{27}{10},\qquad
A_0=\frac{(9/20)(10/57)}2=\frac3{76}.
\tag{5}
$$
上 coast、上减速分别增半径 $1/1900$、$1/50$，故
$$
\frac3{76}+\frac1{1900}+\frac1{50}=\frac3{50}.
$$
下三段总增量是 $-3/50$。上、下与总参考长度分别为
$$
T_{u,\rm ref}=\frac{227}{855},\qquad
T_{d,\rm ref}=\frac15,\qquad T_{\rm ref}=\frac{398}{855}.
\tag{6}
$$
整个周期回到 $a=1,v=0,a''=a'''=0$。各段 $a,a',a'',a'''$ 匹配；没有折痕或被忽略的接点。

保持原 additive-$\delta$ chart 的缩放方式：
$$
r=\frac{\delta}{3/50},\qquad
a_r(s)=1+r\bigl(a_{\rm ref}(s/r)-1\bigr),\qquad
\boxed{\frac{21}{20}\le r\le\frac{11}{10}.}
\tag{7}
$$
全部段长乘 r，速度不变，加速度除以 r。该盒即
$.063\le\delta\le.066$。本条不改变 ShortBridge 的 curvature=4、
peak_fraction=.2；桥本身的全角实际几何仍另付。

## 3. 首准确圆片的曲率与保证窗

关于“强制准确圆片”的解释沿用 [R5](R5-degenerate-inlet-local-arc-uniqueness.md) 与 [R55](R55-flat-ramp-reach-obstruction-and-soft-start.md)、[R57](R57-soft-start-intermediate-curvature-obstruction.md) 的精确旋转度量、完整圆弧 Cauchy 数据及 C³ 经典唯一性前提。这里不声称该唯一性已对任意 C² 解成立。

在第一升速段，始终 $0\le v\le9/20<k=1/2$，所以准确圆片根余量
$$
k^2-v^2\ge\frac{19}{400}>0.
$$
R55 的真实圆片主曲率公式给
$$
K_m=\frac{|a''|}{\sqrt{k^2-v^2}},\qquad
K_c=\frac{\sqrt{k^2-v^2}}a.
$$
由 $a''\le B/r$、$a\ge1$，整个首段仍受保护的每片均有
$$
\boxed{K_m^2\le
\frac{(27/10)^2}{(21/20)^2(19/400)}
=\frac{129600}{931}<\left(\frac{123}{10}\right)^2,\qquad
K_c\le\frac12.}
\tag{8}
$$
平方余量是 $1125099/93100>0$。不把 (8) 施加于后续下行速度 −.5 的片或未知补弧。

现在支付材料特征损耗。首段 $a\le1+rA_0$，换元 $dv=a''ds$ 得
$$
\chi_{\rm up}
=\int\sqrt{\frac{a''}{a(k^2-v^2)}}\,ds
\ge
\arcsin(9/10)
\sqrt{\frac{r}{B(1+rA_0)}}.
\tag{9}
$$
这与用于排除的损耗上界是不同方向；这里需要下界以耗尽保证窗。
$r/(1+rA_0)$ 随 r 严格增加，故只须取 $r=21/20$。
arcsin 的前六个正项给
$$
\arcsin(9/10)>
\frac{2180010198706569}{1971200000000000}.
$$
代入后得
$$
\chi_{\rm up}^2>
\frac{10032938318092048295325634587051}
     {21967683584000000000000000000000}
>\left(\frac{27}{40}\right)^2,
\tag{10}
$$
最后严格正差为
$$
\frac{23912485132048295325634587051}
     {21967683584000000000000000000000}.
$$
因此保证保护窗在第一升速末端之前已经耗尽，彼时全过程曲率仍满足 (8)。
这移除了原两级 profile 在第二段仍被保护的高曲率机制；**它不证明所有实际圆片在此消失，不证明后续正 K 退化边界唯一延拓，也不证明全角 BVP 可解。**

## 4. 新首圆片的独立支撑下界

这一节重新付新参数的支撑，未搬用 R55 的旧 $>.32$ 数字。

严格凸三重核心内部含原点。若其最小支撑为 $h_{\min}$，三个旋转的支撑半平面形成外接等边三角形；凸周长单调给
$2\pi\le6\sqrt3\,h_{\min}$。所以
$$
h_\Gamma\ge\frac{\pi}{3\sqrt3}>\frac35,
$$
最后可用 $\pi>333/106,\sqrt3<26/15$ 作有理比较。

准确圆片以核心高度0为原点，满足
$$
X=O+\frac ak e+Ze_z,\qquad
n=\sqrt{1-v^2/k^2}\,e-\frac vk e_z,\qquad 0\le Z\le s.
$$
因此首段
$$
X\cdot n=
\sqrt{1-v^2/k^2}\left(h_\Gamma+\frac{a-1}k\right)-\frac vk Z
>
\frac35\frac{\sqrt{19}}{10}
-\frac9{10}\frac{11}{10}\frac{10}{57}.
$$
只用 $\sqrt{19}>87/20$ 已足以得到
$$
\boxed{X\cdot n>\frac{1659}{19000}>
\frac{87}{1000},\qquad
\frac{1659}{19000}-\frac{87}{1000}=\frac3{9500}>0.}
\tag{11}
$$
这是仍受保护首圆片的未插柱支撑。插柱平移的扣减在第7节统一支付；未知全角补弧、桥和尾没有因此获得支撑证书。

## 5. 新完整首周期的连续尺寸证书

本节只用实际图的三重对称、完整角长和经向单位速度，不要求 R5 的 C³ 唯一性。R55 的轨道弦长引理给
$$
|X_{xy}(s,u)|\le K_3a_r(s),\qquad
K_3=\frac{2\pi}{3\sqrt3},\qquad |z(s,u)|\le s.
$$
于是全角
$$
|X|^2\le K_3^2a_r(s)^2+s^2
<\frac{1936}{1323}a_r(s)^2+s^2.
\tag{12}
$$
首周期 $a_{\rm ref}\ge1$，右侧对 r 非减，只须核 $r=11/10$。

配套脚本使用同一 flat primitive $P'=F$。左、中央及右片分别为
$$
P_{\rm left}(t)=
\frac{t^4}{4\eta^2(1-\eta)}
-\frac{t^5}{10\eta^3(1-\eta)},\qquad
P_{\rm mid}(t)=
\frac{3\eta^2/20-\eta t/2+t^2/2}{1-\eta},
$$
以及 $P_{\rm right}(t)=t-1/2+P_{\rm left}(1-t)$。
每个径向段 $a_{\rm ref}=1+A_{\rm start}+L[v_0t+(v_1-v_0)P(t)]$。
平方包络次数至多10。上升部分 a 与 s 同增，只核末点；下 coast 一盒；
两个下行 ramp 的三个多项式片各作8等分，共50个新标量盒。

本次已用 BigInt 实际生成并检验全部 Bernstein 系数，均为正：
$$
\boxed{
\left(\frac{67}{50}\right)^2
-\frac{1936}{1323}a_r(s)^2-s^2
\ge
\frac{255651723153109}{7164045000000000}>0.}
\tag{13}
$$
因此新盒上完整首周期、全部材料角满足
$$
\boxed{|X|<67/50=1.34.}
\tag{14}
$$
加入下反射仍给该组件直径小于2.68。后续 bridge、tail、圆领和帽未被 (14) 包括，不能据此宣布完整 $D_0\le2.68$。

若整个该组件已有全角全段 relative operator metric 误差≤$10^{-6}$，(12) 右侧可乘 $1+10^{-6}$。采用更保守的平方余量
$$
\frac{255638859393907}{7164045000000000}>0
$$
仍给同一 (14)。这里只说明尺寸包络的稳健版本；有限 BVP RMS 或若干采样不能代替这个全域 metric 前提。

## 6. 新 H、完整扫窗与 held 比例

令 $0<\ell\le1/100$ 为全柱长，仍要求实际完整相位族已按 R54 接出中央柱
$$
G_\alpha(u,z)=(R_\alpha\Gamma(u-\alpha),z),
\qquad 0\le\alpha\le\alpha_1=\frac45.
$$
取
$$
I=[L+13/100,L+67/100],\qquad
\overline H=I\times[-\ell/2,\ell/2].
\tag{15}
$$
I 的材料宽为 $27/50$，全扫窗为
$$
\bigcup_{\alpha\in[0,4/5]}(I-\alpha)
=[L-67/100,L+67/100]
\Subset(L-27/40,L+27/40).
\tag{16}
$$
两侧严格余量均为 $1/200$。$\ell>0$ 保证 H 有二维内点；不是以一条曲线充当握持区。

沿用 R54 的全空间刚体握持校正，此处
$Q_\alpha=R_{\alpha/2}$、
$b_\alpha=R_\alpha O-Q_\alpha O$，所得 $F_\alpha$ 在 H 上逐点固定。
校正保持完整度量、嵌入性、reach 和全欧氏群取商的距离。

H 的水平弦给
$$
\operatorname{diam}F_0(H)
\ge4\sin(27/200)
>
4\left[\frac{27}{200}-\frac16\left(\frac{27}{200}\right)^3\right]
=\frac{2153439}{4000000}.
\tag{17}
$$
开 H 使用内部点趋近边界，直径上确界相同。

R54 的三重整像支持函数引理和 $|O|>2-K_3$ 给
$$
\delta_{\rm hold}\ge
(\,2\sqrt3-2\pi/3\,)\sin(1/5)
>
\frac{535357}{1968750}.
\tag{18}
$$
此处用了 $\sqrt3>433/250,\pi<22/7,\sin x>x-x^3/6$。
它是同一完整紧像的 Hausdorff 下界，不是材料点位移。

对同一个完整初态
$$
D\le\frac{67251}{25000}=2.69004
$$
有精确正余量
$$
\frac{2153439}{4000000}-\frac D5
\ge\frac{1407}{4000000}>0,\qquad
\frac{535357}{1968750}-\frac D{10}
\ge\frac{46043}{15750000}>0.
$$
因而条件比值为
$$
\boxed{
\frac{\operatorname{diam}F_0(H)}D>
\frac{717813}{3586720}>\frac15,\qquad
\frac{\delta_{\rm hold}}D>
\frac{2141428}{21184065}>\frac1{10}.}
\tag{19}
$$

## 7. 完整闭面的条件 reach 与非全等接口

仍需实际未插柱、未标记的**完整**新图，包括 bridge、真实 nonlinear DN 尾、圆领与平盘，满足
$$
D_0\le67/25,\qquad X\cdot n\ge87/1000,\qquad
|\kappa_i|\le123/10,
\tag{20}
$$
并共用完整 Cartesian 二 jet。第一周期的 (14) 和首片的 (8)、(11) 只支付 (20) 的相应部分。

按 [R67](R67-universal-threefold-marker-and-euclidean-noncongruence.md) 选
$\ell\in\{1/200,1/100\}$，插柱直径成本≤.01，半面平移支撑损失≤.005。
R67 固定三重全谐波帽的直径成本≤1/25000、支撑>.0997、曲率≤.0252。
本核心有准确曲率1/2的开弧，而周长 $2\pi$ 的圆曲率为1，故核心非圆；
R67 的“某个有限 $3j$ 阶矩非零”结论直接适用，不要求某个指定 $m_3\ne0$。

完整共同 C² 接缝、圆盘高度等 R67 前提真实支付后，可选上述两个柱长之一避过活动矩抵消，从而在非空相位区间 $(0,4/5)$ 得 $\delta_E>0$。不宣称端点 $4/5$ 一定是其非全等见证。
帽与柱长选定后连同所有物理输入一次性冻结；后续相位族使用同一 g。

由 R54/R67 与既有正支撑球面全局引理，
$$
D\le67251/25000,\qquad
X\cdot n\ge41/500=.082,\qquad
\inf_\alpha\operatorname{reach}F_\alpha(M)\ge10/123.
$$
支撑到焦距余量为 $43/61500>0$。更具体地，
$$
\boxed{\frac{\inf_\alpha\operatorname{reach}F_\alpha(M)}D
\ge\frac{250000}{8271873}>\frac3{100},}
\tag{21}
$$
且 $10/123-(3/100)(67251/25000)=184381/307500000>0$。
这些结论都以同一完整图的 (20) 及共同两 jet 为前提，尚未由本次 scalar 运行支付。

## 8. 参数化接口与不能移用的旧门

已按实际源码核查：

- `multistage_flat_profile._reference` 接受显式有理段表，逐段检查正长度、速度连续、端点速度、上下精确面积。新六段无需修改 provider。原 tag 的 `profile_budget_box` 仍仅是旧 $1\le r\le1.05$ 标签，本条不使用它作证。
- `portable_prefix_continue.py` 的 `--profile`、`--core-config` 和原 `material_support_factory` 已参数化；没有固定 $k=.2,S=.5$ 的门。保全部 state/support/δ 参数、R48 lift、原 complete RMS/BC/metric 门。
- 原 `accepted_original` 要求实际正 λ 原 R53 返回、全部 source/input/raw/physical hash、完整 mean 和真实有限门；不要求 $k=.2$。同一 λ 割线的 `same_design_contract` 则正确要求共同 profile、chart、端口和除 λ 外全部 core settings 相同。不能把旧 profile 的锚与本新 profile 的锚混成 λ 割线。
- 原 bootstrap 与 lifted-secant controller 继承 seed 的全部 core settings，只改 homotopy；取得同一新 profile 的真实接受锚后，可继续原目标 λ 序列。
- 已读原7a `continue_original_actual_dn_chord` 的入口只允许真实 λ=1、curvature_blend=1、$M\le64$，没有硬编码目标曲率或半宽；其全部物理端口和 source 绑定仍须通过。固定最终 g 的新入口也须明确绑定该新场，不能把设计 δ 后续漂移称为同 g 精化。
- 已读 `chord_actual_closed_map` 的 phase 是实际函数参数，其柱半长≤.005与本条兼容。有限三相位查询不是全时证明。旧 M24/mean1168 固定字段、旧小参数族或仅已认证旧场的几何结果，均不因此自动适用于新场。
- 旧 `calibrate_multistage_profile.py`、`check_multistage_profile.py` 硬编码原 profile 文件与旧校准调用，保留不改。另存新 `calibrate_single_gentle_profile.py`，显式读新 profile/chart/完整 port，调用同一原 BackwardLine，仅在 [.063,.066] 定位浮点线性输入根；这份 Python 新入口未执行或编译，不算校准已完成。

核心配置给 $\lambda=0$ 和 .002 两份；$\lambda=0$ 时原 R53 factory 精确返回原 support provider。起始 profile 的 $\delta=.0645$ 只是盒内未校准初值。原 q012 已接受场可作为明确标注的**新物理输入未接受初猜**；不能继承它的已接受身份、尾响应或完整几何。新的 λ 续入须先取得本 profile 的真实正 λ 接受锚。若线性根不在本盒，或后续 δ 出盒，要换输入或重新支付预算，不能修改 (7) 的标签放行。

## 9. 实际执行、配置与剩余任务

配套文件：

- `scripts/resume_20261128/design/certify_single_gentle_ramp_k050.mjs`
- `scripts/resume_20261128/design/single_gentle_k050_profile_initial.json`
- `scripts/resume_20261128/design/material_single_gentle_k050_lambda0.json`
- `scripts/resume_20261128/design/material_single_gentle_k050_lambda002.json`
- `scripts/resume_20261128/design/single_gentle_k050_design.json`
- `scripts/resume_20261128/design/calibrate_single_gentle_profile.py`
- `notes/2026-11-28-design-single-gentle-k050-scalar-observed.json`

本次在 `functions.exec` 的 JavaScript V8 中实际执行了第一份源的完整
`certificate()`。全部50个新 Bernstein 盒、arcsin 六项、核心域/曲率、
保护窗、支撑及 H/held/reach 比例用 BigInt 有理运算；没有浮点阈值判定。
Node 文件的 CLI 没有执行。终端不可用期间没有 Python、BVP、Jacobian、
真尾或新数组运行；prepared Python 入口也没有冒称已通过编译。

复算标量命令：

```bash
node topics/visible-flex-held-10pct/scripts/resume_20261128/design/certify_single_gentle_ramp_k050.mjs
```

实际数学参数定义是上文有理数；原数值构造器将配置中的普通数值存为
binary64。严格余量使微小数值变化有希望被实际区间证书覆盖，但本次未声称
有限 quadrature/舍入字段与精确定义完全相同，最终要明确认证实际选定的同一 g。

下一实质工作是对这份新 profile 取得真实原线性校准或有效完整初猜，
运行保全部门的非圆 λ 续入；不是先重跑已排除的原两级 k=.5 族。
若 λ=1 真接受，随后完成同一场的 full-H nonlinear DN/尾、连续 Cartesian
metric/曲率/支撑/直径、共同 C² 接缝、非全等标记以及冻结最终全部物理参数的
离散与时间精化。R87 只是对这条不同输入路线已付的严格几何预算，不是本题完成声明。
