# post43 连续 metric 外包：保全、复现接口及新全场适配边界

## 本条没有产生新的数值证书

本条静态接手旧 geometry 子线未推包，核对源码、已有输入散列和新接受
文件的结构，不执行新的几何数值计算。旧 `2026-11-14-geometry-resume-M96-continuous-metric.md`
中的实际运行属于前任工作区历史；不能把其 09:29 本地回执标成当前公开
仓库 Actions 的新证明。当前不恢复旧 fixed32 的 `.99` 求解分支。

已保全的完整历史交接见 `2026-11-14-geometry-post43-local-handoff.md`。
其另外三组是直接压圆四档失败、全材料六 jet 角谱诊断、compressed QR
逐位比较；它们都各有自身的输入与对象，不能据此宣告后续 fullDN 方法
失败，或将旧谱/旧 metric 证据转移到新候选。

## 已核源码与旧证明的准确结论

`computations/geometry_20261114_quintic_metric_interval.py` 当前字节与旧
执行冻结源码一致：

| 对象 | SHA256 |
| --- | --- |
| interval 源码，18183 字节 | `f19995bfd92bfdabd43fbf2f0fa6956788e74d18e68ceda77fb8405b17299a4a` |
| 旧 `.984` 接受输入，2613662 字节 | `3ac8c8efa20670342021487a197443f6e1b2ad60f35c7bf2864f355a06424b69` |
| 旧冻结二阶节点 jets，1195888 字节 | `ea653c839655b88cb0fabf50566f8cece44057c2bf81a4cc06fffdb5d380c9f9` |

保存的旧报告确为 `415/415` 区间全部执行，最小正余量
`1.8962168920738398e-08`，完整材料密度下界
`0.16546471387188874`。它证明的是明确的二进制有理共享节点 quintic
有限场，整个参数域上以下**三个归一化分量界**：

\[
\max\{|E-1|,\ |B|/(a\rho),\ |C/(a^2\rho^2)-1|\}<10^{-6},
\]

其中 $E=|F_s|^2$，$B=F_s\cdot F_\phi$，$C=|F_\phi|^2$，
$\rho=d\theta/d\phi>0$。由归一化 Gram 行列式
$>(1-\varepsilon)^2-\varepsilon^2=1-2\varepsilon>0$，有限场确为连续
浸入。二阶节点 jets 是有限对象的定义数据；不需要声称生成它们的
complex-step 导数本身是严格 ODE 导数。

三个分量各小于 $\varepsilon$ 一般只直接推出归一化度量误差的谱算子范数
小于 $2\varepsilon$。不能未经组合证明把本报告转写为 R241 所用的
`relative_metric_operator <= 1e-6`。这一区别不改变原报告已经明确写出的
分量结论，也不额外修改本题 README 的完成标准。

## 最小公开 Actions 原样复现命令

在当前公开仓库 Actions 的依赖环境中，从仓库根目录运行：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_quintic_metric_interval.py" \
  --input topics/visible-flex-larger-amplitude/notes/2026-11-14-geometry-resume-scaled-sphere-M96-normal-BVP-r1.json.gz \
  --second-jets topics/visible-flex-larger-amplitude/notes/2026-11-14-geometry-resume-M96-continuous-metric-second-jets.json.gz \
  --angles 1024 \
  --out "$VISIBLE_OUT/continuous-metric-old984-replay.json"
```

此命令只验证已经冻结的 `.984` 有限场，保留原节点二阶值，不进行 BVP
续算。不要加 `--max-intervals` 后仍称完整证明。程序报告中的 `passed`
必须为 `true`、`all_intervals_checked` 必须为 `true`，并在新公开回执中
保存输入/源码/second-jets 散列。源程序最后会正常退出而报告 `passed=false`
的失败包络，因此 workflow 若需据此判定成功，须读取报告字段，不能只看
进程退出码。旧资源记录约 1080 秒、104 MiB RSS 只是历史成本，不保证
新机器执行时长。

当前未安排该旧对象的重复运算；保留命令是为了履行原结果可复现交接，
不将它冒充新完整大核场的证书。

## 对当前接受前缀可复用哪些部分

已只读核对公开 run `43582043166` 的
`free3/attempt-03/run/stage-00/actual.json.gz` 原件：

- `success=true`，`status=0`，`M=96`，`N=1024`；
- 末端 `s=0.9974999999999999`，432 个节点，每行 290 列，即完整 `3M+2`
  状态；
- collocation RMS `7.019231465972388e-07`，边界残差
  `1.0842021724855044e-19`；
- 标量仍是旧 `FixedProfile` 的 `initial_law` 与 quintic `knots` 结构，
  418 个标量节点全都逐值出现在 BVP 的 mesh 中。

所以该文件能沿用本 interval 消费者的状态排列、完整 core 材料图、标量
构造及逐片 Bernstein 算法。将 `--input` 指向这个准确接受文件，
`--second-jets` 指向一个**新的**输出路径，程序会生成并冻结该场自己的
二阶数据；旧 `.984` 的 second-jets 文件不能移用。完整 431 片能否全部
通过，只有真实公开执行之后才能回答，BVP 接受或旧 `.984` 证书不预付
这个结论。

若将来标量节点不全在场 mesh 中，应在验证时以 de Casteljau 限制原场
多项式、按标量节点细分证明区间；不得移动节点或另拟场曲面。当前旧源码
只处理每个场区间落在一个标量片内的情形，新接受输入已满足这一接口。

## 为什么不能直接消费 complete fullDN

旧源在 `finite_jets` 中硬使用 `FixedProfile`，证明阶段也硬读
`geometry.knots`、`geometry.initial_law` 和旧 exact-coefficient 散列。
新的 `complete-controlled-scalar-profile-v1` 则冻结完整入口、
AngleConnector、coast、原 bridge 与全部已求得的 scalar controls。
它包含非多项式的 angle-connector 积分，以及六次的 control bumps。
仅把构造器换成 `exact_profile_formula` 还不足以修正 Bernstein 证明阶段。

后续适配应保留同一冻结公式、控制参数和标量分界。在多项式片上可以提高
Bernstein 次数并精确加入已冻结 bumps；在 connector 上可用原公式的
Taylor 多项式及严格余项或其他直接区间外包。这样的多项式仅作原函数的
**包络**，不能把它当成新定义的标量曲线，从而暗中更换固定度量 $g$。
目前未有通过 fullDN 的新全场，本条不创造该对象，也不移植旧证书。

## 归一化算子误差的最小组合不等式

这是一条可选的同一对象验证接口，用于准确衔接已有 R241 算子封套，
不增加本题完成标准。设 $A=a\rho>0$，

\[
G_\mathrm{norm}=\begin{pmatrix}E&B/A\\ B/A&C/A^2\end{pmatrix},
\qquad e=E-1.
\]

对给定 $\varepsilon>0$，严格算子界
$\|G_\mathrm{norm}-I\|_{\mathrm{op}}<\varepsilon$ 等价于
$\varepsilon I\pm(G_\mathrm{norm}-I)$ 都正定。以 $\operatorname{diag}(1,A)$
作合同变换，Sylvester 判据把它精确化为四个纯实标量正性条件：

\[
\begin{aligned}
p_-&=\varepsilon-e>0,\\
p_+&=\varepsilon+e>0,\\
q_-&=p_-\big[(1+\varepsilon)A^2-C\big]-B^2>0,\\
q_+&=p_+\big[C-(1-\varepsilon)A^2\big]-B^2>0.
\end{aligned}
\tag{1}
\]

证明为：两合同变换后的矩阵分别具有首主子式 $p_-,p_+$ 和行列式
$q_-,q_+$，故 (1) 正是其正定判据；正定性在可逆合同变换下保持。
反方向同理。这一写法完全避免对 $A$ 作区间除法，也不需要开方求特征值。
若只想验证非严格的 $\le\varepsilon$，可改用两矩阵的全部主子式非负；
不能把首主子式与行列式均非负单独当作半正定充分条件。

对现有 quintic 场和 quintic 标量片，$E,B,C$ 的径向次数分别为
$8,9,10$，$q_\pm$ 至多 18 次；真实物理角频率上限是 $8M$，因此若复用
区间 FFT 恢复这些乘积的全部角系数，全圆角数须严格大于 $16M$，
`M=96` 可用 `2048`。加入六次 scalar bumps 的多项式片可使径向次数
上升到 20，角频率不因此改变。非多项式 connector 的余项必须传播进
同一四个不等式；无需用另一个拟合标量取代原公式。

本条给出完整代数组合推导，尚未声称当前新接受前缀或未来 fullDN 全场
已通过 (1)。实际使用时也仍需把同一有限场、完整标量冻结定义和数值
舍入包络一并绑定。
