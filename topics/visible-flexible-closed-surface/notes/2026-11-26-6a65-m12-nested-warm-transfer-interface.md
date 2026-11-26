# 原 M12 全半片的径向／角向暖转移及实际保存误差接口

日期：2026-11-26。会话：Astra-visible-flex-6a65e705。

本文件是 R196、R208、R223、R226、R236、R243 在当前全半片 Cartesian 场上的完整消费接口，**不另登记一个新的 Boehm 定理**。它完成准确嵌入、一次 binary64 保存误差的连续六 jet 预算和非零有限核。这里没有消费一个实际 M12 大场，也没有启动新场的求解；生产入口的物理身份检查仍须在下一同 job 中执行。

## 1. 固定对象和两类相等

原图为 R223 的同一中央到真平 cuff 的完整材料图，包含原 prefix、准确 bridge、有限尾与 deep collar。共同径向变量为 $z=q/T\in[0,1]$，中央角反参为 $\theta=U_0(u)$。源、准确目标 $g$、物理／材料区间、原始 payload、common-cut metadata、bridge、背景生成器和 tolerance 均保持原定义。

旧修正写成

$$
W(z,\theta)=\sum_{i,a}c_{ia}N_{i,5}(z)\beta_a(\theta).
$$

完整 clamped knot 在首尾各含六个 $0,1$；首尾各三个控制行固定为零。角通道恰为

$$
\beta_m(\theta)=(\cos m\theta,\sin m\theta,0),\quad m=3k+1,
\qquad
\beta_{3k}^{z}(\theta)=(0,0,\cos3k\theta).
$$

这是实系数的整个 $D_3$ 与 ambient 反射空间，不能替换成独立的少量角切片。允许新的 knot 多重集合包含旧集合，内结点重数至多三；因此新五次场至少 $C^2$。首批 h509 准备只插简单 knots，原求解器仍只消费这一简单情形。

准确 Boehm 插入采用 R236 已冻结的有理实现。全部旧 binary64 系数及 knots 先按其准确 dyadic 值读入；中间计算不转浮点。对每个旧角通道插入全部新增 knots，随后将新增角通道置准确零。由既有 Boehm 恒等式及 R243 的角通道嵌入，所得准确新系数 $c^*_{ia}$ 定义的场逐点等于原场。两边都是 $C^2$，故完整六个位置 jet 也处处相同；更高阶只在相应导数存在处作此断言。

由同一函数的端点两 jet 为零及 clamped 表示的端点三角关系，准确新表示的首尾三行仍为零。实现实际检查这些行，再作唯一一次 binary64 存储。舍入后仍是实系数并保持这些零行，因而全域 $C^2$、中央／真 cuff 两 jet 和上述两个空间对称均保留。准确嵌入的函数恒等式与保存后的字段不能混为一项：下面专门预算它们的实际差。

## 2. 保存后的连续六 jet 预算

令 $\widehat c_{ia}$ 为真正写入 NPZ 的 binary64 系数，并定义准确有理误差

$$
e_{ia}=\widehat c_{ia}-c^*_{ia}.
$$

这里直接把已保存浮点重新解释为准确 dyadic 后相减，不以通用浮点 epsilon 替代实际误差。令 $e^{(0)}=e$。对 degree $p$ 的当前 knot 向量，迭代

$$
e^{(d+1)}_{ia}=p\frac{e^{(d)}_{i+1,a}-e^{(d)}_{ia}}{t_{i+p+1}-t_{i+1}},
$$

每次删去首尾各一个 knot，并使 degree 减一。当前输入的内重数至多三，所用 active 支撑分母为正。设

$$
E_{dj}=\max_i\sum_a|e^{(d)}_{ia}|\,|m_a|^j,\qquad d+j\le2,
$$

其中零频的零阶权取 $0^0=1$。这些数全部用有理数计算。

**连续界。** 对所有节点、单元内部及所有角度，保存差 $V=\widehat W-W$ 满足

$$
|\partial_z^d\partial_\theta^jV|\le E_{dj},\qquad d+j\le2.
$$

证明直接消费 R226 的导数控制行公式：相应低次 B-spline 非负、构成单位分割；每个水平向量角模式的第 $j$ 导数长度不超过 $|m_a|^j$，每个竖直 cosine 同样。逐通道三角不等式后由非负分割取最大控制行。重数三时二导仍连续，所以界包含 knots 本身和左右迹。这是整个连续域的界，有限测试点并非其证明。

端点前三／后三准确控制行及保存误差行均为零，因此 $V,V_z,V_{zz}$ 在两个端点准确为零，所有含角导的端点两 jet 也准确为零。

## 3. 共同物理图中的误差

不新造材料坐标。按 R223、R226，$\partial_s=H^{-1}\partial_q$，其中 $H\ge H_*=171/250$、$|H_q|<60$；$T\ge T_->0$ 来自同一准确 bridge 下端点及原 frozen profile。原中央弧长定义给

$$
|\theta_u|\le U_1=a_+/J_*,\qquad |\theta_{uu}|\le U_2.
$$

这四个严格量从已绑定的实际旧 R226 回执和原 metadata 取出，不能以显示用 float 替代。程序另外准确核对 R223 的 $h>11/25$ 及 $3(3/2)/h+(711/500)^2\,24<60$。

链式法则于是给整个原物理／材料域

$$
|V|\le E_{00},\quad
|V_s|\le\frac{E_{10}}{T_-H_*},\quad
|V_u|\le U_1E_{01},
$$

$$
|V_{ss}|\le\frac{E_{20}}{T_-^2H_*^2}+\frac{60E_{10}}{T_-H_*^3},\quad
|V_{su}|\le\frac{U_1E_{11}}{T_-H_*},\quad
|V_{uu}|\le U_1^2E_{02}+U_2E_{01}.
$$

目标半径全域 $f\ge r_{\mathrm{cuff}}>0$，故

$$
\|dV\|_{g,F}\le |V_s|+|V_u|/r_{\mathrm{cuff}}.
$$

程序同时输出 $|V_{ss}|+2|V_{su}|/r_{\mathrm{cuff}}+|V_{uu}|/r_{\mathrm{cuff}}^2$；它是放缩的坐标二 jet 界，**不是**已经补偿 connection 的 covariant Hessian。原确定参考修正 $C$ 在这一步不变，因此 $C$ 没有被遗漏，也不应在纯保存差内再加一遍。新保存场自身的 R226、R230 几何和 R236 度量检查仍须实际重算。

以上只界定系数存储差；不包含浮点 basis 求值、源积分求积或原图数值反参误差，也不证明新的 nonlinear 方程已被解出。原完整相位作用下的精确嵌入与对称关系由同一函数恒等式传递，不以有限时间采样替代它。

## 4. 生产身份和明确拒绝条件

实现必须同时收到旧 field、旧 grid、旧完整 result、同场实际 R226 回执及新 grid。它检查：

- 旧 result 和 R226 中的 field／grid SHA 都与实际文件一致；R226 不得为 reference-only，必须认证连续全 knot／全角及端点两 jet；
- 原 payload、common-cut、bridge、完整 source、背景、tolerance、原两个长度定义和 true cuff 与新旧 grid 一致；
- 旧求解明示同原 $g$、全部内部接口自由、有限尾及 deep collar／true cuff 完整覆盖；
- metadata、bridge、tail manifest 和准确 Boehm 实现的实际 SHA 与回执一致；
- 完整系数形状、全部正负实际模式、knot 多重集合和端点零行完整，系数实且有限。

输出 schema 为 `6a65-M12-exact-nested-space-warm-transfer-v1`。其中明确分开 `exact_space_inclusion_before_binary_storage=true`、实际有理六 jet 保存预算、`new_nonlinear_solve_executed=false` 和 `exact_isometry_proved=false`。真实新场有自己的 field SHA。现有 R243 的纯角 warm reader 不接受这个 schema；后续必须用明确的新 reader 消费，不能伪装成其零误差格式。含重 knot 的生产求解器尚未连接，有限核对此不作扩张声称。

## 5. 源、复现和实际有限边界

生产源：[6a65-m12-exact-radial-angular-warm-transfer.py](../scripts/6a65-m12-exact-radial-angular-warm-transfer.py)，10,733 bytes，SHA256 `cd2eea7beba4f6902067ff0952487bf1e426e13790150690458fe6dcba3ed0ca`。

独立有限核：[6a65-m12-radial-angular-transfer-finite-check.py](../scripts/6a65-m12-radial-angular-transfer-finite-check.py)，6,363 bytes，SHA256 `410018472af719fa6081c52f683e98de455feea7abbe7748f5495064715a8b0a`。

使用已发表 R236 Boehm 源 SHA256 `f69035fe51642d30f2a1a5079c3e67f36c8cb05257df89be650cb5b015327db9` 和 R226 checker SHA256 `81003432a6823b3c86859be226c9a099012ed7fa21e46165ac12091d86727e80`。

实际执行命令：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flexible-closed-surface/scripts/6a65-m12-radial-angular-transfer-finite-check.py \
  --scripts topics/visible-flexible-closed-surface/scripts \
  --out "$M12_COLD_DIR/radial-angular-finite-check.json"
```

新报告路径必须不存在。2026-11-26 的实际运行自然 exit 0，脚本内计时 0.4544406219938537 s。临时完整报告 2,576 bytes，SHA256 `e06947ee2d8bb2bce9b1b5edc77b337e29a3192b554a3c11462e0ca6d6f36375`。报告可由此命令重生，按根规则 15 不提交。

输入含 55 个非零系数，由 $5\times11$ 扩至 $9\times17$。插入四个 knots（按重数计），其中旧 $1/2$ 再插两次，最大内重数三；六个新增角通道准确为零。独立有理 de Boor 求值器在所有相关 knot、端点和各单元中点，配合四个使三角函数值准确可表的角，实际比较 408 组完整 native 六 jets。真实保存舍入非零；每项误差平方都不超过其连续界平方，最大比例小于 0.142。端点全部两 jet 准确为零。

六项严格有理界的显示值依次为

| jet | 显示值，仅供阅读 |
|---|---:|
| $E_{00}$ | $1.8741804548278519\times10^{-25}$ |
| $E_{01}$ | $9.65712167143577\times10^{-25}$ |
| $E_{02}$ | $7.553770517577976\times10^{-24}$ |
| $E_{10}$ | $3.2607082857100016\times10^{-24}$ |
| $E_{11}$ | $1.7215363136318157\times10^{-23}$ |
| $E_{20}$ | $9.873529143971723\times10^{-23}$ |

严格端点是运行时 `upper_exact` 的有理数，上表不是向外舍入后的严格十进制端点。小核没有实际旧 M12 大场、没有执行生产 main 的 R226 物理绑定，也没有新场求解。它验证已明确的非零转移／保存路径，不能代替下一次真实同 $g$ 加密的实际 fullGram、全部祖先点、两组微窗、连续度量、全时间几何及 STL 回执。
