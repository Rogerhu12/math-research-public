# 第115轮：第二原支撑上的奇形零 jet 控制与完整三共振搜索

作者：ChatGPT，GPT-6 Astra Pro（AI-assisted）  
日期：2026-11-15  
分类：**新标量族的算法设计、条件解析说明及 Actions 执行接口；尚无115数值结果。** 本文只引用实际114原读数。本地仅进行源码、AST、JSON字面量、SHA及脚本语法工作，不执行科学模块或新数值运算。

## 1. 实际114依据与新的设计对象

实际114为 [run 43687426018](https://github.com/Rogerhu12/math-research-public/actions/runs/43687426018)，source `dc032461bbd2f3f7515ea30e5495b50870a06f65`，compute job `132730710123`、report job `132730985417`。原摘要 86,389 B，SHA-256 `c4eca98c2bb83aba6708f8e88616bd052483836278df369ace6743e2443503ee`，不含日志分隔 LF；临时原 status 7,197,627 B，SHA-256 `4e7ee4fa7d570e2147041ba0bd3ea2769844ee8e6bdfa545f0b791b3ef34035f`。

八方向中七方向各二十档全拒，仅方向5的第14档接受，$\alpha=2^{-14}$。原未加权目标从 `6958.225762769883` 到 `6958.225762766608`；接受记录实际下降为 `3.2750904210843146e-9`。最终三参数和三单位方程为：

```json
{
  "parameters": [0.46303184038373296, -0.19282285521524933, 0.6316435963633119],
  "unit_equations": [-117.96801026238036, 0.008956935069351885, -0.00020359485484041056]
}
```

全部155个外试探都保留真实完整三式。接受点的内层误差为 `[-5.824339274762558e-12,-2.6822507077396696e-8]`，内层容差标志为 false，仍按原完整目标接受。另一方面，方向2的 $\alpha=1$ 校正误差为 `[-9.90295224295723e-11,8.238436946961941e-9]`，已经达到内层容差，但第一式为 `-118.14578807392797`，目标 `6979.21365998137` 高于基态而被拒。这些原件说明，不能只归因于未完成二维校正；它们也不证明局部极小、无根或普遍浮点底线。114的单位阈值、完整112行候选标志及非零 native/场的最终责任均未完成。

115固定增加一个函数形状，从上述真实三参数和**显式新引入的 $\theta=0$**开始。四参数搜索改变的是设计标量 $a(s;p_1,p_2,p_3,\theta)$，因此是**新 $g$ 族**。不把后续不同参数点称为同一固定 $g$，也不把第四函数的线性独立称为三共振响应补秩。原114源码、原三参数证据均不修改。

## 2. 六个运行文件、身份和来源闭包

| 文件 | bytes | SHA-256 |
|---|---:|---|
| `geometry_20261115_small_core_four_control_family.py` | 36157 | `9222390b73abbd2e8bc4a1f8e9d8b861cd66b4a927b21629deb2e6b70073dd11` |
| `geometry_20261115_small_core_four_control_curved_recipe.py` | 51709 | `3ca1bdf723e7c44f808ed786ccda854775c262d28ce92804fde2c8ca86cad160` |
| `root_20261115_small_core_four_control_curved_scalar_readout.py` | 18169 | `c0602e7ac54dd9bafefbedf7d0f52abf0b77324769be0cd9d29970c249e0269d` |
| `actual114-explicit-four-control-parameter-recipe.json` | 1490 | `becfe390c6f5a8a49905fb2269357a3bd16172492c4ed15e569489c2d1f9299f` |
| `public-small-core-four-control-request.json` | 29001 | `282d640e440f45e342e6e88d2abf88e19f614dc5d4a3e7c70016cb6447337360` |
| `visible-larger-public-small-core-four-control.yml` | 15665 | `f1615b4ee060059a175ce06e8dce9df9885e3fb90675877afab36e056701d003` |

前三个 Python 文件、recipe及request进入本课题 `computations/`；workflow进入 `.github/workflows/`。新独立触发路径为 `topics/visible-flex-larger-amplitude/computations/public-small-core-four-control-request.json`，concurrency为 `visible-larger-public-small-core-four-control`。没有 dispatch、未来run或未来结果的占位身份。

请求保留114原77个来源 pin，新增两个数学文件，合计79个主来源；另两件支持来源是新小读者和未修改的规则监控器 `3b8b6dd5…`。实际114 producer定义闭包为18件；新producer定义闭包为22件：旧18件，加明确列入闭包的原 `full_scalar_profile`、`prefix_controls_profile` 和两新数学文件。两原scalar源本来就在主77中，不重复计数。旧108/112/114只提供已冻结算法及来源基线，不执行它们的 `main`；3169 helper保持原15件定义闭包。

recipe不是原 status，只保存真实114 run/source、producer身份、原 status和summary的bytes/SHA、前三个原末参数，以及独立声明的第四坐标零。父原payload按规则15没有重新取入，旧J、残差、目标、FD均不复用。未来同入口续接可接受其自身真实producer、22件闭包及四个真实末参数的短recipe，不能冒用旧18件闭包或伪造 parent-status。

四原数学输入完整bytes/SHA保持：accepted `b4d2b98a…`，prepared `0f94dd88…`，真实T112零高尾anchor `e788a28d…`，tail config `01930f3b…`。完整路径和digest在request；缺失时仅从历史 `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复完整原件。公开78源恢复及 `VISIBLE_SOURCE_TOPIC` 约定原样保留。

## 3. 第四控制的定义、零 jet 与独立性

取原第二支撑（零基编号1）已经保存的左端 $\ell$、正宽 $w$，令 $x=(s-\ell)/w$，$P(x)=64x^3(1-x)^3$。保留三个原偶形控制，新增

$$
\psi(s)=
\begin{cases}
w^2P(x)(2x-1),&0<x<1,\\
0,&\text{其余},
\end{cases}
\qquad a_4(s;p,\theta)=a_3(s;p)+\theta\psi(s).
$$

对应完整三个scalar jet为

$$
\psi'=w\{P'(x)(2x-1)+2P(x)\},\qquad
\psi''=P''(x)(2x-1)+4P'(x).
$$

$P,P',P''$在0和1均为零，因此 $\psi,\psi',\psi''$在两端均为零；与外部零函数拼接得到 $C^2$ 控制。这里证明的是新增函数自己的零012 jet，不自动补齐原有限Gauss半径表达式与独立返回 $a',a''$ 的全局兼容证明。

在原三个分离支撑上，如果新增函数属于原三函数张成空间，在第一、第三支撑内分别迫使其系数为零。在第二支撑内部，除去非零原偶形 $w^2P(x)$ 后将得到 $2x-1$等于常数，矛盾。故新增函数独立于原三函数；这不保证映射 $p\mapsto(F_1,F_2,F_3)$ 的第四列独立、最小奇异值变大、横截性或根存在。

实现沿原 `ScalarBump` 的**stored width**。严格声明的端点是 $\ell$和 $\ell+w$；同时保存原binary64 `right`，不把二者作为精确有理数静默等同。新的标量表达式及Arb分支沿原完整breakpoints和stored-width定义。改变 $\theta$不会引入额外外部支撑或改变原cut处的零jet责任。

## 4. 三处真实接线与完整3×4响应

新的family文件同时覆盖原来只认三个控制的三个位置：

1. `FourControlProfile`提供实际四列 `control_jets`、完整三个scalar jet和四参数domain判断。原三个控制、base、tail/cut信息由原profile保留。
2. `CircleReference.evaluate`在原699节点和所有midpoint加入真实第四jet。后续原半径递推、三条完整2×2模态传播、原112×112零尾J以及完整112右端残差的公式保持。第一式到第三式均保留，不能把较小残差覆盖为零。
3. 新 `scalar_spec`、完整descriptor和 `ScalarExpression`包含真实四参数、第二支撑、stored width、奇形公式、所有原有限Gauss常数及完整来源。每次最终域包络对这个新identity重新做，不复用旧三参数域证书。

完整参数Jacobian是3×4，四列分别用原complex-step `1e-25`穿过**整个当前圆半径和模态传播**。在原合法光滑分支、不遇根号/分母/分支变化的条件下，该方法对应同一有限复延拓。浮点评价与complex-step本身不是区间导数证明。初末description保全部四列，在 `2e-5`、`1e-5`、`5e-6` 三个步长做完整原实差分，逐列误差和valid状态如实报告；无新增FD门。新报告同时给全3×4奇异值、旧前三列奇异值及完整第四列，全部只是实际数值读数，不能先宣称补秩。

初始 $\theta=0$在数学定义上退化为原三控制。入口还会从同一实际原件重新评价旧三模型，将所有返回数组的shape/dtype/完整bytes/SHA逐项与新模型比较，并保存实际 `all_recorded_arrays_byte_identical`。这个读回**不进入接受或执行条件**；未复用114旧残差/J。未来非零theta续接会另评相同前三参数上的theta零参考，不把这个参考冒作实际当前theta的状态。

## 5. 四维预测与二维法向弯曲路径

令 $u=(p_1,p_2,p_3,\theta)$，$r=F(u)\in\mathbb R^3$，$J\in\mathbb R^{3\times4}$。沿原相对参数尺度

$$
S=\operatorname{diag}(\max(1,|u_j|)),\quad v=Sz,
\quad\min_z\|JSz+r\|_2^2+\mu^2\|z\|_2^2,
\quad\|z\|_2\le\Delta.
$$

初半径0.1，最大1。$\mu>0$，增广矩阵是完整7×4；采用带列主元Householder QR和完整4×4三角解，无 `lstsq/rcond`、SVD截秩或法方程。正阻尼下界、64次上界寻址及64次几何细分继承原策略；此处仅固定线性模型中选阻尼，不额外探测非线性点。

取 $c=(F_2,F_3)$、$C=J_{\{2,3\},:}$。完整两行数值平衡后，对 $(CS)^T$做完整QR，得到 $N\in\mathbb R^{4\times2}$和余下两列 $T\in\mathbb R^{4\times2}$。两个法向和两个切向均保留；不选 $J_{33}$单图。

每档 $\alpha=2^{-j},j=0,\ldots,19$ 使用

$$
q(\alpha,w)=u+\alpha v+SNw,\qquad
c(q)=c(u)+\alpha Cv,\qquad w_{\rm initial}=0.
$$

在合法光滑有限模型中，如果 $C$真为当前导数且秩2，则 $CSN$可逆。因为 $N$张成 $\operatorname{range}((CS)^T)$，其与 $\ker(CS)$的交仅为零。对 $G(\alpha,w)=c(u+\alpha v+SNw)-c(u)-\alpha Cv$，有 $G(0,0)=0$、$G_w=CSN$、$G_\alpha=0$，故局部隐函数满足 $w(0)=w'(0)=0$，从而 $q(0)=u$、$q'(0)=v$，原完整目标的起点斜率为 $r^TJv$。这是条件解析结论，不把浮点框架/SVD读数当秩证书。

源码在 $\alpha=0$直接返回原点，不调用评价或校正。正alpha的内层最多12次完整2×2投影Newton，每次最多20档原模型试探，目标误差 `1e-8`仅为**内层停止阈值**。未达阈值的实际返回点仍按

$$
W(q)=\tfrac12\|F(q)\|_2^2\ \le\ W(u)+0.2\alpha r^TJv
$$

和原域条件裁定；完整三个真实残差永不被target替换。无效直线seed使该alpha失败，本轮不细分曲线绕过无效seed。校正后的实际参数位移可能超出预测半径，报告明确保存而不静默加拒绝门。内层两式target、误差、tol标志、真实三式、原目标、域异常、相对位移及两个切向漂移均保留。

最多八次完整方向，已接受或全拒方向都占一次。二十档全拒只把半径乘1/4，原接受点/J不变；下次重算完整四列预测。接受后的半径规则沿原108/112/114，原未加权full3斜率和`.2` Armijo保持。`1e-8`单位迭代早停与完整112行候选标志分开，不能用归一化量或内层目标代换。原native最终接受并未被这些候选标志支付。

## 6. 最终固定实际theta的完整平方检查

原 `AugmentedFlow`、`PhysicalTestBoundary`和 `CompleteResidual` 在 $M=T=112,K=3$ 时要求三个active参数。直接把4传入会破坏原平方结构。因此最终从真实四参数构造 `ThetaFrozenProfile`：

$$
a_{\rm base,\theta}=a_{\rm base}+\theta\psi,\qquad
a(s;p)=a_{\rm base,\theta}(s)+\sum_{j=1}^3p_jb_j(s).
$$

这里固定的是**当前实际theta**，没有把theta清零、增加边界条件或丢任何112尾行。共振模型仍使用原accepted的前三target；最终circle check则保持其原三项零核target，不冒非零大核目标。新的AugmentedFlow和PhysicalTestBoundary重新建立，完整FFT/node/mid/RMS及九项原物理切向检查在同一数学新scalar上实际执行。原circle reference仍是零核参考；非零native/finalJ/audit均尚未运行。

四参数circle和固定theta平方视图可能有不同binary64加法顺序，源码明确不声称逐位相同，并报告actual scalar node value/ap最大差。这个差不作额外门；原实际物理域/残差如实输出。reference保完整四参数spec、theta、三个active参数布局和新canonical identity。

最终Arb对新声明实表达式的 $a>0,|\mathrm{returned}\ a'|<1$作160bit、最大深度14的完整区间检查。它保持原独立returned-ap口径，不把它误当有限Gauss半径的解析导数；不覆盖literal binary64 roundoff、全局scalar导数兼容/$C^2$、圆的完整Frenet域、高109非共振或非零分支。上述未付责任各有false标志。

## 7. 可执行接口、schema和输出

```bash
python -u geometry_20261115_small_core_four_control_curved_recipe.py \
  --accepted ACTUAL_ACCEPTED --prepared ACTUAL_PREPARED \
  --tail-anchor ACTUAL_T112_ANCHOR --tail-config ORIGINAL_CONFIG \
  --parameter-recipe actual114-explicit-four-control-parameter-recipe.json \
  --parameter-recipe-sha256 becfe390c6f5a8a49905fb2269357a3bd16172492c4ed15e569489c2d1f9299f \
  --initial-relative-radius 0.1 --candidate-steps 8 --backtracks 20 \
  --normal-iterations 12 --normal-backtracks 20 --normal-target-tolerance 1e-8 \
  --candidate-resonance-tolerance 1e-8 --interval-bits 160 --interval-depth 14 \
  --out NEW_EMPTY_OUTPUT
```

Actions中由request解析四原路径；`NEW_EMPTY_OUTPUT`为 `$VISIBLE_OUT/small-core-four-control-curved`，不在调用前预写科学目录。新schema依次是：

| 对象 | schema |
|---|---|
| 短recipe | `R259-explicit-four-control-odd-shape-recipe-v1` |
| 临时 `four-control-curved-status.json` | `R259-four-control-full-three-two-normal-curved-trust-recipe-v1` |
| 完整scalar specification | `complete-prefix-three-even-plus-second-support-odd-control-v1` |
| 完整scalar descriptor | `complete-four-control-scalar-real-expression-v1` |
| 新circle reference | `R259-four-control-circle-full-three-resonance-family-v1` |
| 新完整scalar域报告 | `R259-four-control-complete-declared-scalar-domain-enclosure-v1` |
| 小标量readout | `request115-original-four-control-full3-curved-trust-scalar-readback-no-raw-retention-v1` |

reader只复制已完成的原字段：初末完整3×4 J、全部四参数、实际rank/FD读数、四维方向/QR/框架、完整外试探、原inner停止/误差、所有最终flags、真实来源和参数recipe。零theta数组对照表在短读数中用count及canonicalbytes/SHA保范围；完整临时status的bytes/SHA保留，不伪称以后仍有raw。超90,000B时先去可重复的大型/重复元数据，明确所省字段及其SHA；仍过大则输出诚实界限fallback，不能伪称已保全部外行。逐外试探stdout另保真实scalar记录。

## 8. 资源、发布及本地工作范围

Python `3.12.14`、NumPy `2.3.5`、SciPy `1.17.0`、python-flint `0.9.0`、BLAS单线程，原checkout/setup actions版本全部沿114。科学75min、compute90min，独立report10min。最多160外候选、38,560次seed/normal回溯评价、1,920次normal fresh-J；这些计数不含每个3×4 J的四个complex-step评价、初末FD及完整终检。预算中断必须按真实阶段报告，不冒二十档全拒、无根或终检完成。

源码仍只允许公开指定仓库Actions执行。规则监控器原3b8实现不变，在隔离镜像初次及每2700秒真实pull/rebase，双README绑定 `74c08a36…`/`bff8aea2…`；变更时停科学保partial。固定科学checkout不被监控器改动，H必须存在唯一规则行且不超过10KB。设置`merge.stat false`、关闭自动gc/maintenance。

规则15：无旧publisher、无artifact/Release上传，不把可重算raw、status、circle、trace或审计数据入Git。科学目录在always小读者后删除；独立report job通过 `GITHUB_OUTPUT`输出不超过90,000B的原scalar JSON及bytes/SHA，标记 `BEGIN_VISIBLE115_SCALAR_SUMMARY`/`END_VISIBLE115_SCALAR_SUMMARY`。主控随后仅登记脚本、参数、真实run/source/输出SHA及紧凑结论。未完成或无readout时明确缺失，不宣布成功。

本地已核新Python的AST、原circle半径/transfer/112行正文保持范围、原full3 Armijo/半径和完整2×2QR保留、新source和recipe的字面身份、workflow的Bash与inline-Python语法。未import科学模块、未执行constructor/FD/矩阵/标量域/试探，也不把静态核设成新的科学门。完整diff及静态回执仅为临时可重建材料，不要求按规则15保存这些计算/审阅产物。
