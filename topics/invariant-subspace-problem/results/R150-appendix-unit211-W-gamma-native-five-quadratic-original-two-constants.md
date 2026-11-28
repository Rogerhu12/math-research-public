# R150：整个 W / $\gamma\ne0$ 的原 native NS/PS 二次拉回、精确五行与两条六次斜率约束

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / r150_open_geometry。日期：2026-11-28（Asia/Taipei）。

**状态：完整证明；首次实际执行成功。** 全部五个二次与原 $I_6$ 精确等价；两条新必要参数多项式对 $s$ 的次数均为六。它们非零且非单位，未排空当前 W；所有个别二次头和实际乘子共同因子的零纤维都保留。

## 1. 为什么是新的低次原输入

整个当前 W 已付 $t(f-u)\alpha\ne0$，令 $s=t/(f-u)$、$\gamma=\alpha/(f-u)$。已成 gamma 原图给 $x,y,t$ 都是同一个 $f$ 的一次式。此前真正返回的九二次系统是将两个原三次各乘三个二次头后消立方；其三条参数必要式的 $s$ 次数为 $5,10,10$。

本次不用这六条二次化，也不重新形成它们的三个标量。改用旧 native 坐标中已有的原均值六规则：将原 NS、PS 各自先约化为
$$
(1,x,y,t,y^2,yt)
$$
的线性组合，再作新 gamma 拉回。这些式子总几何次数已经不超过二，因而拉回后直接是 $f$ 二次。它们并不乘任何单个 $f$ 二次头。目标是精确五个二次、五行三列，并首次形成两条新固定原 cofactor；不先假定新 $s$ 次数一定下降。

本输入只需要两份已冻结源的必要定义前缀：gamma 同点 Gram 10176 字节、native 六均值规则 14656 字节。不执行旧十八乘法列、commutator、95 秒权行列式、旧 $f^3$ 头 Bézout、旧 $q_f$ 或冻结十行二列。

## 2. 原余式的精确来源

记原 native 六式
$$
F=(E_1,E_B^{even},E_B^{odd},N_1,NS,PS).
$$
六条 native 首一规则全部只由前四式组合产生，其 NS、PS 两来源坐标恒为零。按已刊原重写算法，对 $j=4,5$ 用初始来源列 $e_j$ 约化原 $F_j$，得到
$$
R_j=\sum_{\nu=0}^{5}r_{j\nu}b_\nu
   =F_j+\sum_{i=0}^{3}h_{ji}F_i,\qquad
b=(1,x,y,t,y^2,yt).
\tag{1}
$$
全部 $r_{j\nu}$ 只含权变量；$h_{ji}$ 总几何次数至多一。源完整核验原 (1)，确认 $F_j$ 的系数恰为一且另一个原三次的系数为零，并确认 $R_j$ 总几何次数至多二。

实际六规则首项只用当前 W 已付单位。来源尤其包括 [整等权排除](R150-appendix-unit211-equal-weights-complete-original-exclusion.md) 给 $k+2$、[整个 J19](R150-appendix-unit211-W-J19-entire-original-weight-curve-exclusion.md)、[整个 C9](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-C9-complete-original-exclusion.md)，以及既有原 W 基本权单位。新源逐项支付实际 $\delta_2,\delta_3$ 的分子/分母和全部规则来源分母，不用旧“开图”标签代替原支付。没有新几何分母。

## 3. 同一点的 gamma 拉回

沿用已成 gamma 原图，写 $\eta=f-u$、$\delta=1-Q$、$m=u-\ell$、
$$
\widehat U=u-\ell Q,\quad M=\ell(2u-\ell Q)-u^2,\quad
\gamma=4\delta-\widehat U s,
$$
$$
\beta=4\delta-2um s-\frac M4s^2,\quad
c_*=-s(Mu+mT_0/2)+\frac{Mu}4s^2.
$$
则
$$
V=\frac{\beta f+c_*}{\gamma},\quad
t=(f-u)s,\quad W_1=(T_0+4uf)/2,
$$
$$
x=\frac{\widehat U V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M}.
\tag{2}
$$
这些都是同一 $f$ 的一次式，分母只含原已付权和 $\gamma$。$E_0,N_0,P_0,P_1$ 的原恢复保持不变，且原 $E_1=EW$；同时
$$
EW=\ell E_B^{even}+mE_B^{odd}.
\tag{3}
$$
源不会把两个不同 fmpq_mpoly context 直接互相强转。对 native 的每个权多项式按其前两项指数显式嵌入 gamma 的 $(e,k,s,f)$ context，再按 (2) 替换 $x,y,t$。全部原权、$f,\lambda,T$ 和 Gram 十六条目的两个 $\rho$ 分量均实际同点核回。

(1) 拉回之后，记 $Q_0=EW,Q_1=E_B^{odd},Q_2=N_1$。用 (3) 得
$$
\widetilde R_j=F_j+
 (h_{j0}+h_{j1}/\ell)Q_0+
 (h_{j2}-m h_{j1}/\ell)Q_1+h_{j3}Q_2.
\tag{4}
$$
这里各 $h$ 均取同一拉回值。源码直接将 (4) 两边在完整 $f$ 有理多项式环中相减核零；不是只比较最高头。$\ell$ 已付。每条 $\widetilde R_j$ 都对 $f$ 至多二次。

因此在整个当前 gamma 环中，
$$
(Q_0,Q_1,Q_2,NS,PS)
=(Q_0,Q_1,Q_2,\widetilde R_4,\widetilde R_5).
\tag{5}
$$
两方向都由 (4) 中原三次系数一直接给出；不需要任何 $f$ 头非零假设。前面已刊三头 Bézout 仍可用于首一有限环境，但本源不再生成它，也不使用它来扩大 (5) 的范围。

## 4. 两个新固定常数目标

只清每行的已付分母、只剥已付参数内容，得到五个原二次 $P_0,\ldots,P_4$。将各行放在 $(1,f,f^2)$ 三列。只取新组
$$
(0,1,3),\qquad(0,1,4).
$$
第一组是两个原均值加 native NS 二次，第二组换成 native PS 二次。它们与先前九二次中的 Loww/NS 正乘子二次化不同。

对每组三行的末两列取实际 cofactor $\mu$，精确除去所有三个实际乘子的共同多项式因子后，完整返回
$$
\sum_i\mu_i'P_i=C,\qquad
\sum_i\mu_i'[1,f,f^2]\text{ 的系数}=(C,0,0).
$$
这只取消实际组合乘子的共同内容，绝不把原方程除以未付因子。随后仅剥 $C$ 的当前已付参数因子；所有其它内容、头零与主元零仍保留。若新行或 cofactor 为零，准确输出零，不作错误单位判定。

非零非单位的 $C$ 只给必要方程；没有多元 gcd 判空，也没有将五行的两个必要标量冒充完整消元理想。首次运行完成了全部上述原身份与两个实际目标，准确结果见第 6 节。

## 5. 冻结参数

新源 basename：2026-11-28-unit211-W-gamma-native-five-quadratic-original-two-constants-8542.py。

源字节数 10726，SHA256：508690f4d98bf6e4993316999bab0d6d3b9a19ca81bcd7e81939f663b9c3e1fe。

直接依赖一：2026-11-28-unit211-W-gamma-open-direct-native-f-cube-monic-two-8542.py，完整 SHA256 bd68e5e5e66f31e9c3e2ad0b66468c021fc7d852d44462d3a937966200ab961c；只执行 Necessary old definitions only 注释前的 10176 字节，前缀 SHA256 8545759f4c40266068fc932bd2ef10710fe67cd767cf743900fe3d215bfb6bcf。

直接依赖二：2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py，完整 SHA256 10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1；只执行 matrices/errors 定义前的 14656 字节，前缀 SHA256 88b8e2f49f925e51c0b940f929efb502ced9ed358228a605fea3755d9cdefff8。

固定新预算 180 秒/4 GiB。所有嵌套 alarm/setitimer 均钳在顶层绝对截止，硬内存界没有降低后冒称恢复。只输出源码身份、参数定义、次数/SHA和小回执，不保存可重算系数或矩阵。


## 6. 完整实际返回

Actions run 46116343901 / job 140890939469，source commit 7bf3f16bc523bca10b395570a1bb632916b8966c，实际源 blob 93cbfafe052a5961e5b5e297081aeb5acff57178。

- 内层源 exit 0；驱动 16.373311528 秒；峰值 RSS 106000 KiB。
- 原权、$f,\lambda,T$ 与全部 Gram 分量的跨 context 同点识别于 4.217599676 秒返回。
- native NS、PS 的完整原均值来源分别于 7.483045443、10.708841396 秒返回。
- 五个实际二次全部具有 $(\deg_f,\deg_s)=(2,4)$，精确五行三列于 14.329351688 秒完成。
- 两个固定原标量于 15.320892007、16.319845360 秒完成；最后数学 checkpoint 为 16.320007033 秒。
- 新层 6 次多项式精确商乘回、53 条原身份；必要 native 定义内部的原规则身份同样全部通过。
- stdout 8710 字节，SHA256 ba13a1a8d40820ad2831ef08913b9b23fd738b690dc506628f7c8f434900b971。
- 驱动在 2026-11-28 06:23:18.593278 UTC 真实 pull 到 ba9c766f01c2b90166a7f5c0b86c058e490f4a89，两份 README 均无变。

五个单位归一原二次的准确规模为：

| 原行 | $(\deg_e,\deg_k,\deg_s,\deg_f)$ | 总次数 | 项数 |
|---|---:|---:|---:|
| $EW$ | $(16,13,4,2)$ | 26 | 2001 |
| $E_B^{odd}$ | $(17,15,4,2)$ | 29 | 2550 |
| $N_1$ | $(19,17,4,2)$ | 32 | 3060 |
| native $NS$ 余式 | $(39,44,4,2)$ | 68 | 17729 |
| native $PS$ 余式 | $(39,44,4,2)$ | 68 | 17715 |

两个 native 余式的公共原分母只含已付权和 $\gamma$；其 profile 次数为 $(32,41,2,0)$、2784 项，SHA256 eaeeefed5ee1cf6b3783b41d0b27664b3c6b95bf61df1f807838982991873a37。该分母也已逐项支付，没有用“余式应当正则”代替实际原单位检查。

对应单位归一的 native NS、PS 二次分别具有 SHA256：
004e9bb57b7928b8b5765ccdb59eb8aa6ec44c0cef56c842993f53d218b14f1d，
7e8b9b3badf5a1286b1a177fd77ea24724f38996a9c81ca6b6818285eec16afc。
这些只是原源码再生结果的指纹，完整可重算系数未保存或传送。

## 7. 两条真正的新参数方程

两组实际 cofactor 的共同乘子因子相同，次数 $(e,k,s)=(7,6,1)$、总次数 11、72 项，SHA256 17b614f3d6bcbfa279a2cfb0b7e4059da1ba525b5ea6b3bc49c5c6e1969c3b13。源码并未把它当单位，而是将三个实际乘子逐一精除后重新乘回完整三列和原多项式。

最终只剥已付参数因子后：

| 固定组 | $(\deg_e,\deg_k,\deg_s)$ | 总次数 | 项数 | SHA256 |
|---|---:|---:|---:|---|
| $(EW,E_B^{odd},\widetilde R_{NS})$ | $(45,49,6)$ | 78 | 10623 | bdf2996192cafb3203b245484067f39c3b467098f0058feac239ae3b7dda25de |
| $(EW,E_B^{odd},\widetilde R_{PS})$ | $(45,49,6)$ | 78 | 10616 | 66240c45570eb2c0a9b542ad21ee558d169f62cab2b2b9a72005484905b9a0b8 |

剥除列表都是源码中的 $e,k,u^2,Q-1,\overline V,M_{\rm num},H_{\rm old},\ell_{\rm num},\gamma_{\rm num}^2$ 对应的实际已付多项式原子。这里按源码记录逐轮 gcd 精除；原子可能共享因子，列表不主张互异不可约因子的唯一分解。原未剥标量的次数均为 $(61,64,8)$、总次数 105。所有其它共同内容、首项和参数零面都保留。

因此它们是原 $I_6$ 中两个新参数标量，其来源是 (1)–(5) 与完整 cofactor 身份。虽然 $s$ 次数由此前正乘子 cubic 输入中的十次降为六次，权系数次数仍然较高；本条不据此预判任何后续消元必然完成。没有运行旧参数 determinant、旧十行二列或先前九二次的三个标量尾，也没有把两个必要方程作为充分条件。

源：[2026-11-28-unit211-W-gamma-native-five-quadratic-original-two-constants-8542.py](../notes/2026-11-28-unit211-W-gamma-native-five-quadratic-original-two-constants-8542.py)。

小回执：[2026-11-28-unit211-W-gamma-native-five-quadratic-original-two-constants-receipt-8542.json](../notes/2026-11-28-unit211-W-gamma-native-five-quadratic-original-two-constants-receipt-8542.json)。
