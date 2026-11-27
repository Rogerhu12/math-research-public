# 实际 18 六项几何约束与下一完整初场：端层总长取 S/2，profile 保 1/32

2026-11-27 UTC。本文记录一个已经由实际几何读数支持的下一次完整输入选择，不登记新的定理，不改变既有运行源，不把参数方向写成数值改善保证。选择为：

- 固定同一 Fejér/R690 度量与冻结参考。
- 将 `--seed-boundary-total-length` 从 `1/4` 改为 `1/2`。
- `--seed-profile-delta` 保持 `1/32`。
- 当前完整 driver `10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f`、reader `8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49`、launcher `f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506` 全字不变。
- 新独立科学输出命名空间为 `{work}/fixed-fejer-meridian-batched-bhalf-first`。原全部 157 个 science argv 词、7 个 pure argv 词、全部变量、32 阶段、原观察域、预算和历史责任保留；科学参数只改变这一条 seed 宽度，路径另作独立归属。

## 1. 实际来源与完整六项读数

本次亲读 fresh main 的确切提交为
`42e52a68c95f18ccf945ddf598e313116b835ab1`，完整小索引为
[实际 18 索引](2026-11-27-public-actions-46062343475-1.md)，
24,357 B，SHA-256
`18437f61a5ff6f756edb29481e2050f8ee616c9068935ae9f3baed0b577f4d82`。
索引生成时间 22:09:33 UTC，实际观察时间 22:09:31 UTC。它是仍运行的子进程的有界完整标量观察，不是自然返回的科学步骤或证书。

运行 `46062343475/1` 的当前完整科学来源为：

| 对象 | 实际身份 |
|---|---|
| 科学工作树提交 | `e3d2ebacae1ddce7990d72d778c96e851810ffe8` |
| driver | `10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f` |
| launcher | `f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506` |
| 原标量 observer | `321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5` |
| 固定数学 recipe | `957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9` |
| 当前 normal model | `9ec211ddc5c14e0d4f0e47045ed84abc3ec4bc97fcf0e893959d6ba0cf8609bd` |
| 初始及尚未接受方向的当前点 | `7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47` |
| 实际小数学进度文件 | 7,270 B，`5fe23dc1a517d6ec5b8edad2173a0d58943c5e9a8374ae27b47df32c22bfd5e3` |

该点初始统计为 $\Phi=4954.71485872585$、相对 Gram 屏幕最大值 $0.6374168330977955$；初始几何已完整返回。同点六项 signed physical g 为：

| 约束家族 | 实际 signed g |
|---|---:|
| reach | +2.0480426708394406 |
| body diameter | −0.04304843011978521 |
| distance plus | +0.11871374548166669 |
| distance minus | −3.0936337267043594 |
| cap diameter | −0.06715131487906445 |
| height floor | −1.0411715967426867 |

因此当前完整有限屏幕的主正项是 reach，第二正项是 distance plus。负号只表示该次完整有限屏幕中的约束满足，不能升级成连续、全相位或误差已付证书。

21:56:50.421541 UTC 已返回试点
`7d0d7e61c365986749b28def3e7759425f39ec7cb644737b13567b58592fd913`
的统计，$\Phi=4954.694898882503$、Gram $0.6374164670510036$；至上述观察，试点几何与接受判定仍为 null，accepted directions 为 0。22:09:25 的根链进度属于这个试点，不属于初始点。上述两点绝不混合。

原完整 geometry scan 会保存 `worst={cell,u,phi,branch,...}` 与逐点主曲率记录，但当前已读索引没有公开这些位置。故本文没有把最大曲率定位到端层、中央段、某一角或某个具体径向格点。

## 2. 屏幕公式实际约束了什么

完整几何源
[so3_fixed_fejer_batched_missing_angle_geometry.py](../scripts/resume_20261126/so3_fixed_fejer_batched_missing_angle_geometry.py)
SHA-256 `5730b1792d58c1c695592aaea8a229d76b68f8bd1fefe8ded6016afba9566135`
使用完整第一、第二基本形式的广义主曲率根，当前 $K$ 不是可以仅靠重新解一个 $2\times2$ 矩阵便缩小的粗三角上界。

其 reach 屏幕为
$$
g_{\rm reach}=0.03\,D_{\rm point}K_{\rm sampled}-0.992,
\qquad
D_{\rm point}=\max(2,2|H|,2\max|F|).
$$
本次正项意味着屏幕乘积为 $3.0400426708394406$，而要求是至多 $0.992$。这没有支付连续曲率、全部闭面或实际 reach。

distance plus 的原公式为
$$
g_+(F)=1-\frac{|F-Xe_y|^2}{0.9^2},
\qquad X=1+\sum_{m=1}^{160}c_m.
$$
因此其最大正项对应有限已读图像离这个见证点的最小距离
$$
0.9\sqrt{1-0.11871374548166669}.
$$
没有一个已证定理说增大端层宽度必把这个最近距离向外推。新初场的这一项必须真实重读，不能继承旧位置或旧负项。

## 3. 当前实际混合端点是 d，不能混为 v=r d

本次完整读取
[fixed_fejer_supported_meridian_reference.py](../scripts/resume_20261126/fixed_fejer_supported_meridian_reference.py)
39,771 B，SHA-256
`ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a`。
它的 `_means` 将完整均值求解器给出的 `d,d_phi,d_phiphi` 传入 `evaluate`。实际边层为
$$
Y=(1-\chi)T_0+\chi d,\qquad T_b=Y/|Y|,
$$
其代码确为 `Y = (1.-chi)*T[boundary]+chi*d`。没有在这个混合公式中使用 `v=r*d`。准确 $d=N(v)$，故 [R721](../results/R721-supported-seed-width-and-profile-sensitivity.md) 的单位端点公式适用于其明确的准确单位、非零分母和同一准确根等假设；工作浮点向量不能因为变量名为 d 就被当成误差为零的单位向量。

为避免将该公式误用于另一种混合，完整一般表达是：若 $T_0$ 单位、径向上固定的端点为 $Z$，则 cutoff 转向项的范数为
$$
\frac{|\chi_s|\,|T_0\times Z|}
 {|(1-\chi)T_0+\chi Z|^2}.
$$
若 $Z=r d$、$|d|=1$、$T_0\cdot d=\cos\theta$，则此量是
$$
\frac{|\chi_s|\,r\sin\theta}
 {(1-\chi)^2+\chi^2r^2+2\chi(1-\chi)r\cos\theta}.
$$
除非 $r=1$ 或另有完整共同分母界，不得把它替成单位端点的 $15\tan(\theta_{\max}/2)/b$ 界。

本文对当前源的参数动机沿用 R721 的已证单位端点结论：每端物理长 $\Delta=b/4$，所以
$$
\max|\chi_s|=\frac{15}{2b},\qquad
|(T_b)_s|\le \frac{U_s}{\nu}
+\frac{15}{b}\tan(\theta_{\max}/2).
$$
将 b 加倍，只在冻结共同 $U_s,\nu,\theta_{\max}$ 时把最后一项减半。真实新 seed 的方向、参考采样区域、分母和均值同时改变；本文没有把这些量冻结为旧实际值。

## 4. 为什么选 b/S=1/2，而不同时再改 profile

原支持端点不动：
$$
U/S=[1/32,15/32]\cup[17/32,31/32],\qquad |U|=7S/8.
$$

| 长度或参数 | 当前 18 | 新独立初场 |
|---|---|---|
| 四端层总长 b | $S/4$ | $S/2$ |
| 每端层长 | $S/16$ | $S/8$ |
| 中央总长 $L_c$ | $5S/8$ | $3S/8$ |
| 每个中央段长 $\ell$ | $5S/16$ | $3S/16$ |
| profile $\delta$ | $1/32$ | $1/32$ |
| 每中央 ramp 物理长 $\ell\delta$ | $5S/512$ | $3S/512$ |

新增中央区间分别为 $[5S/32,11S/32]$ 与 $[21S/32,27S/32]$，均严格正长。原 `SeedParameters.definitions` 要求 $0<b/S<7/8$ 与 $0<\delta<1/8$，本选择满足同一源定义；这只是源级合法域，不是均值根存在证明。

旧 16 与 17/18 的 reach 屏幕乘积大约相差四倍，而端层总宽也扩大四倍，是提出 width 方向的启发。它同时混有 profile 改变、不同模型/点、真实均值及图像直径变化，所以不是对 $K\propto1/b$ 的识别或证明，更不能用这个比值预测新的 g。

新值取 $1/2$ 是一个明确的完整候选：在上述冻结尺度中给端层 cutoff 两倍宽度，而中央仍保 $3S/8$ 总长；没有向退化端点 $b/S=7/8$ 靠拢。它不被称为最优值、最大允许可行值或已证明优于 $3/8$、$5/8$。

保持 profile 为 $1/32$，是不再同时改变 R721 已证明存在竞争效应的另一个旋钮。R721 已证同准确 r 与中央长度下，增大 $\delta$ 会提高中央 $\max|F_{ss}|$，但降低 $\max|\alpha_{ss}|$；两者都不能直接排序真正曲率。这里没有利用这一结论删除任何 profile piece 或降低求积预算。

## 5. 中央段和均值变化是明确代价

若暂时固定准确 $r=|v|$、方向、架与 $\delta$，则 profile 幅度 $\lambda$ 不变，中央主项
$$
U_c=\frac{\lambda}{(1/4-\delta)\ell}
$$
会因 $\ell:5S/16\to3S/16$ 增大为原来的 $5/3$。所以本建议绝不等同于“所有径向曲率都下降”。

真实的 $r,d$ 由每一个 b 的完整方程
$$
(L-b)v+B(b,Nv,\phi)-K(\phi)=0
$$
重新确定。固定支持保证 K 不变，但 B 的物理区域、归一化方向及全部两角 jets 均会变。R721 的完整关系
$$
Jv_b=v-B_b,\qquad
\partial_b\log U_c=\frac1{L-b}
+\frac{r_b}{\lambda A_\delta'(\lambda)}
$$
没有给未知 $r_b$ 固定符号。本建议不沿用另一 b 的准确根或工作 mean batch。

新 b 还使原 R709 的粗充分条件更紧。它们未满足不等于数学无根；R722 后验分支仍须本次真实候选、完整准确残差、全角积分与严格有理不等式。当前源不会把旧 R709 false 改成 true，也不以额外前置试验作为新科学入口条件。

Gram 的混合/角向项、完整法向投影、距离见证、帽、接缝、全相位、历史地址和所有费用继续本次真实重付。即便边层纯 cutoff 成分下降，$F_\phi,F_{\phi\phi}$ 与面积分母变化仍可能使最大主曲率上升。

## 6. 固定 g 与发生变化的对象

冻结 Fejér 七项 RN-even dyadic 配方、完整 R690 scalar、冻结材料图、参考 M160/J923/N2048、原 scalar 参数投影和整域 g 都不变。新 run 从原确定性 maker/reference 完整构造自己真实文件，不把 18 的 whole file SHA 当成已发生的新返回。

改变的是 supported seed 的边层和中央分割、由此重新解出的均值/角 jets、seed identity、normal model 及其初始物理场。新实际 model/point/report/packet/费用身份尚未知；它们不能从同固定 recipe 的事实中推出来。当前所有自由变量仍保留，既没有把参考 seed 换成 17 或 18 的试点，也没有迁移旧工作值或旧证书。

保留当前137完整来源角色、原120父来源、原五已支持 peer CLI 和全部已知/未知历史责任。不把尚未自然返回的试点当作完整父场，不把未消费的新 peer history 声称为空。

## 7. 完整后续费用与输出归属

后续准备仅派生参数文件：原 normal/geometry/closed 的完整运行体与 SHA 不变，消费新 namespace 中真实自然返回的 report 与同点完整 immutable packet；全部原参数、selector、输出和历史来源保留。正常科学、准确费用、闭面、R716 和 mesh 各自只使用同一新场自己的输入，现有 18 的完整记录继续留作来源与独立实验事实。

本文只做完整源码、已公开小索引和符号公式核读。没有本地科学计算、求根、CAS、AST、fixture、额外预算探测或任何 refs/queue 写入。新均值可行性、初始几何改善、接受步、连续证书和性能均未宣称。
