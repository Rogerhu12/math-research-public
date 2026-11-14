# 同时控制 core 二型和外环的实际均值预测步

2026-11-12，constructive-route。除 §1 的逐点代数界外，本文数值均为
普通浮点有限样本；未构成精确 PDE 解、连续区间包络或闭合证明。

## 1. R37 的实际 $N<0$ chart 需要二 jet 门

固定一个 $C^2$ 浸入 $F$，令
$$
X=F_x,\quad Y=F_\theta,\quad C=Y\times X,\quad A=|C|,
\quad l=C\cdot F_{xx},\ m=C\cdot F_{x\theta},\
n=C\cdot F_{\theta\theta}.
$$
取实际几何改变量 $W$，即新图确为 $F+W$，而不是只取某条参数族的
线性导数。记
$$
q=|Y|\,|W_x|+|X|\,|W_\theta|+|W_x|\,|W_\theta|,
$$
$$
\begin{aligned}
r_l&=q|F_{xx}|+(A+q)|W_{xx}|,\\
r_m&=q|F_{x\theta}|+(A+q)|W_{x\theta}|,\\
r_n&=q|F_{\theta\theta}|+(A+q)|W_{\theta\theta}|.
\end{aligned}
$$
则新面积 $A_*$ 和新未归一化二型满足
$$
A_*\ge A-q,\qquad
|l_*-l|\le r_l,\quad |m_*-m|\le r_m,\quad |n_*-n|\le r_n.
$$
因此若 $q<A$ 且 $r_n<-n$，便严格保持浸入和 $N_*=n_*/A_*<0$。
又有
$$
\left|(l_*n_*-m_*^2)-(ln-m^2)\right|
\le |n|r_l+|l|r_n+r_lr_n+2|m|r_m+r_m^2.                 \tag{1.1}
$$
证明完全逐点：先展开
$C_*-C=Y\times W_x+W_\theta\times X+W_\theta\times W_x$
并用三角不等式，接着
$l_*-l=(C_*-C)\cdot F_{xx}+C_*\cdot W_{xx}$，
另两项同理，最后展开两个二次多项式。若这些右端采用了真正连续
上界，便是连续 $C^2$ 门；把它们只在网格上计算则仍只是采样诊断。
特别地，小 $C^0$ metric 残差不自动满足这个门。

对于 R37，$N<0$ 是所选径向 chart 的实际条件，而曲率型别由固定
目标 $K_0$ 决定。若还需真实曲面保持某一严格型别，则用 (1.1)
与相应的 $|ln-m^2|$ 正裕量比较。转折处没有这种正裕量，
还须另付根位置、简单性和非特征性，不能用 (1.1) 直接跨过零点。

## 2. 用同一真实 Schur 列建立线性二型约束

输入仍为 SHA256
63b5513befcf44ce907b047dbeb41a7e143431211d20e3cbb103a081cbef0a0e 的
data/fourfold_phase_m24n201_q256_checkpoint.npz，以及 SHA256
2c6e5eb5c17578baf08f43a3d6b39e1699b5fd7dd0c17aae02047f0ba2fd158a 的
data/fourfold_phase_m24n201_schur_directions.npz。

令 $\Delta=m^2-ln$。对一个实际 phase/mean 方向，其 $A,n,\Delta$
变分都从同一个有限原函数的真实二 jet 计算，而非径向平均替代。
准确微分公式为
$$
\delta N=\frac{\delta n}{A}-\frac{n\,\delta A}{A^2},
\qquad
\delta K=-\frac{\delta\Delta}{A^4}
          +\frac{4\Delta\,\delta A}{A^5}.                \tag{2.1}
$$
脚本 scripts/fourfold_phase_core_type_predictor.py 以此生成三个
实际参数列；所有列保留原 radius shift、$\delta\beta_4(0)=0$。
它们仍只是有限加权 Schur 方向，不是已证明的 PDE 切向。

最大 Gram 特征方向为
$$
v_{\max}=(-.05397638458,-.86761196435,-.49430358002).
$$
保持 $v_{\max}\cdot\delta\alpha=0$，并在
$[0,.3]$ 的121径向点、每点128角点上加入
$$
N+\sum_i\delta N_i\,\delta\alpha_i\le-\eta.
$$
另在 $[0,.2]$ 要求实际线性 $K\le-.02$，
在 $[.3,.6]$ 的181点要求同步目标线性 $K_0\ge.05$。
这比之前只控制外环的 LP 多了实际 core 门。

所有 $\eta=.02,.1,.2$ 的线性问题在 $|\delta\alpha_i|\le.1$ 内可行。
取 $\eta=.2$ 的最小 $\ell^\infty$ 步为
$$
\boxed{\delta\alpha=
(-.05992578105864573,-.002859469296679818,
 .011562705610855754).}                                \tag{2.2}
$$
其线性预测 core $N_{\max}=-.2$、inner $K_{\max}=-.16655578$，
外环目标 $K_{0,\min}=.05$。有限线性 metric 加权 $L^2$ 范数为
$1.1133092\,10^{-5}$。因此先前三个 mean 取最小范数但没有 core 门
导致的型别损坏，并不说明这三维均值空间内不存在合适方向；
负的第一 mean 自由度能同时改善二型。

完整 LP 列的重算入口和十二种约束组合结果见
2026-11-12-phase24-core-type-constrained-linear-predictor.json。
没有使用浮点 LP 的成功状态来宣称严格可行性。

## 3. 完整非线性预测图复核

严格按控制向量做
$v_* = v+\sum_i\delta\alpha_i d_i$，仍然**没有 Newton 修正**。
完整图另存为
data/fourfold_phase_m24n201_type_constrained_predictor.npz，SHA256：
bf8430db367ae5d328c953dc2ba631288f75f778ea720756811a72f01c1f2449。
新 mean 为
$(.7396093769906578,-.004942132891742137,-.049352132159964625)$。

真实全 body 1201径向点、每点256角点的复核给出：

- $[0,.3]$ 的实际 $N_{\max}=-.20445563$；全 $[0,3]$ 采样 $N<0$，
  尾端的最大值接近零，不能拿这个尾部浮点负号当连续证书；
- $x\le.235$ 的所有实际曲率样本都负，
  $x\ge.2425$ 直到3的所有实际曲率样本都正；
- 外环窗口 $[.3,.6]$ 的实际 $K_{\min}=.03888848$，
  同步目标 $K_{0,\min}=.06558625$；
- 目标只有一个正侧根 $.2383282434$，根处 $K_0'=59.17870585$；
- 128角点的实际中央根位于 $[.2367147753,.2413673475]$，
  根处实际 $K_x\in[21.96766,103.75445]$、
  $N\in[-3.44488489,-.47519945]$，
  非特征因子范围 $[.86972562,1.16489157]$。

这支持选用单个中央双曲分量的下一轮诊断，但连续简单性、唯一性、
完整转折正则性仍未证明，且有限 body 不等于带固定开帽的闭面。

原生1798径向点、每点256角点诊断进一步给出：

| 项目 | 当前完整预测图 |
|---|---:|
| metric operator 残差 | .000590341769 |
| 实际腰径向差 | .131483063857 |
| 两倍采样原点半径 $2R$ | 2.552410997548 |
| 腰差/$2R$ 代理 | .051513280574 |
| 采样最小支撑 | .901200819020 |
| 采样最大主曲率绝对值 | 7.408757283772 |
| 保持的 $\beta_4(0)$ | .20747484022400084 |

可见比、曲率及支撑在当前采样上有余量，metric 残差仍须修正；
这一点只是后续受约束 Newton 的新起点。不能把它命名为精确等距面。
新返回映射也必须由这个图或它后续的同一修正图重算，
不能复制原候选或旧 n101 图的返回数/作用量。

## 4. 重做命令

在仓库根：

    OPENBLAS_NUM_THREADS=1 python -u topics/visible-flex-exact-nearby/scripts/fourfold_phase_core_type_predictor.py \
      --checkpoint topics/visible-flex-exact-nearby/data/fourfold_phase_m24n201_q256_checkpoint.npz \
      --directions topics/visible-flex-exact-nearby/data/fourfold_phase_m24n201_schur_directions.npz \
      --out topics/visible-flex-exact-nearby/notes/2026-11-12-phase24-core-type-constrained-linear-predictor.json

    OPENBLAS_NUM_THREADS=1 python -u topics/visible-flex-exact-nearby/scripts/fourfold_phase_core_type_predictor.py \
      --checkpoint topics/visible-flex-exact-nearby/data/fourfold_phase_m24n201_q256_checkpoint.npz \
      --directions topics/visible-flex-exact-nearby/data/fourfold_phase_m24n201_schur_directions.npz \
      --out topics/visible-flex-exact-nearby/notes/2026-11-12-phase24-core-type-constrained-nonlinear-predictor.json \
      --evaluate-existing-report topics/visible-flex-exact-nearby/notes/2026-11-12-phase24-core-type-constrained-linear-predictor.json \
      --trial-checkpoint topics/visible-flex-exact-nearby/data/fourfold_phase_m24n201_type_constrained_predictor.npz

第二条不重复线性大采样，核对两个输入哈希后，使用第一条保存的精确
三参数增量重新生成原函数并完成全 body 二 jet 和型别复核。
