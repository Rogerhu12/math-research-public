# R44 到平圆领的固定完整度量 BVP：可运行适配

**状态：独立适配脚本已实现，参考闭合、完整边界二 jet、解析 Jacobian 已廉价核验。尚未运行空间非线性 BVP。**
程序为 `scripts/ruled_core_to_tail_bvp.py`，只导入稳定的 `core_to_tail_bvp.py`，不修改椭圆基线。
核心解析实现及坐标约定见 `ruled-core-port-interface-20261114.md`。

## 1. 固定的整段度量，而非每次重新设计

默认核心参数 $b=.24,s_0=.012$，位置入口准确为旧 R44 的
\[
X(0,\theta)=c(\theta)+s_0d(\theta),\quad
X_s(0,\theta)=d(\theta),\quad X_{ss}(0,\theta)=0.
\]
用旧 R44 原坐标 `rotation=0`，中央镜合使用 $A_y=\operatorname{diag}(-1,1,-1)$，与当前尾的 $(r\sin\theta,-r\cos\theta)$ 材料方向一致。

连接段物理参数记 $t\in[0,L]$，默认 $L=1$。
先取准确核心的旋转型半径及其可实现参考角
\[
a_{\rm core}(t)=q\sqrt{b^2+(s_0+t)^2},\qquad
\beta_{\rm core}(t)=\arccos\frac{q(s_0+t)}{\sqrt{b^2+(s_0+t)^2}}.
\]
默认在 $[0,.01]$ 保留该半径的准确整段公式，然后在 $[.01,.05]$ 用五次平坦 cutoff 将角接到长段母线。
整个局部角公式区间满足 $|a'_{\rm core}|<1$；程序会拒绝不满足此条件的参数。

长段角函数用原有五次步进、一个固定 `.8` 的奇 bump，以及一个标量闭合控制 $c$。
它在 $T=L-.03$ 之后恒为 $\pi$，所以最后 `.03` 的参考度量是真正开平圆领。
令 $w=1-S_5((t-.01)/.04)$，并在区间外作常值延拓；整段角为
\[
\beta=w\beta_{\rm core}+(1-w)\beta_{\rm long}.
\]
半径和参考高度定义为
\[
a(t)=a(0)+\int_0^t\cos\beta(\tau)d\tau,\qquad
z(t)=\int_0^t\sin\beta(\tau)d\tau.
\]
在所有公式交点拆段求积；末端平段直接积分。标量 $c$ 仅在建立参考时用于闭合 $a(L)=.28$，随后固定。

默认实际闭合控制为
\[
c=0.17934855056978544,
\]
本次数值闭合残差 $1.61\cdot10^{-15}$。
此浮点求积及根不是区间证书；输出明确保留这一限制，不把残差舍入为严格零。
数学上的固定参考由同一分段公式及所记录控制定义；当前执行统一使用 64 点分段 Gauss 求积。

空间求解器完全禁用度量系数：`metric_unknowns=0`。输出 `fixed_metric_identity` 记录整个参考的参数、控制、求积约定及坐标版本。
warm 加密必须保持这个字典逐项相同，只能改变空间离散化和尾端变量。

## 2. 准确位置端口与径向试探空间

入口在每个求解或审计角网格上直接解析计算，不使用核心 FFT 截断。
出口仍是原有准确 R128 产品可展尾；其截口半径 `.28`、内平区半径 `.26`、握持子盘半径 `.23`。
两端的完整位置二 jet 由 Hermite 场锁定，自由位置样条在两端的 $0,1,2$ 阶导数为零。
因此尾端的 $a'=-1,a''=0$ 与固定参考端口兼容；后续可以继续准确尾直到平盘，但整个组装的单射性仍待核验。

**区别：** 参考度量在 `[0,.01]` 准确等于 R44 的度量，不表示试探空间中的实际位置在该整段被强制为 R44；实际位置硬锁的是截口完整二 jet。
闭面中央另保留 $|s|\le s_0$ 的准确 R44 核心。

短段也进入空间离散化。默认五个径向自由基的内节点是
\[
.01,\ .05,\ .2875,\ .525,\ .7625.
\]
九基加密保留这五个节点，并插入长段中点；不是只增加求积点而不提高短段表示能力。
相同五次 B 样条空间的 warm 场按所记录旧节点投影，角模按原材料角匹配。

## 3. 已运行的廉价实现检查

命令：

```sh
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/ruled_core_to_tail_bvp.py \
  --check-only --check-jacobian \
  --out topics/visible-flex-new-mechanism/notes/ruled-core-tail-L10-interface-20261114.json
```

本次总运行约 1.6 秒，没有调用空间优化器。输出中：

- 准确核心段的 $a,a',a''$ 对照误差均为 0。
- 入口度量二 jet 误差均为 0；尾端半径误差 $1.61\cdot10^{-15}$，尾端两阶导数误差为 0。
- $X,X_s,X_\theta,X_{ss},X_{s\theta},X_{\theta\theta}$ 两端最大误差 $2.22\cdot10^{-16}$。
- 随机方向的完整残差 Jacobian 相对误差 $3.55\cdot10^{-11}$。
- 独立四阶有限差分核半径、高度一、二导数，相对误差不超过 $6.68\cdot10^{-9}$。

未优化初始场的细网格度量误差为 **1.7010**，所以当前没有准确连接候选。
这份 JSON 的 `solver.performed=false`，不能计为求解成功。
另以 `--check-only --warm` 从五基八模输入九基十二模，固定参考身份逐项保持、完整二 jet 再次通过；
输出 `ruled-core-tail-L10-warm-interface-20261114.json` 同样没有调用空间优化器。

## 4. 几何尺寸与 reach 预算的真实范围

圆参考的采样统计如下，仅用于设计输入：

| 量 | 本次值 |
|---|---:|
| 半径范围 | `.28` 至 `.801121` |
| 上半参考高度范围 | `0` 至 `.470689` |
| 参考尾平面高度 | `.3336925` |
| 镜合参考的球半径采样最大值 | `.891313` |
| 参考最大主曲率采样值 | `20.0417` |
| 固定度量的 $\max|K|$ 采样值 | `27.7595` |

不能继承这个圆参考的 reach：局部曲率已给参考 reach 上界约 `.04990`。
这不排除同一度量的不同第二基本形式；固定度量本身仅由采样 Gauss 曲率给必要上界
\[
\operatorname{reach}\le1/\sqrt{27.7595}\approx.18980,
\]
并没有给任何正 reach 下界。
程序不输出把半带参考直径当作完整曲面直径的归一化比值。

准确中央曲线的两个相对点已给完整曲面直径下界
\[
D\ge2(R+P+Q)=1.4197717952\ldots.
\]
若后续实际闭面能证明 $D\le2.0$，则本题要求 reach 至少 `.06`，握持直径至少 `.4`，像 Hausdorff 位移至少 `.6`。
半径 `.23` 的平握持子盘直径 `.46` 可支付这一条件预算，但必须先完成真实圆领及全曲面嵌入。
这里的 $D\le2.0$ 是待证预算，不是从参考网格自动得到的界。
静态 R44 原种子的宏观像位移也未证明达到该门槛；本 lane 先检验准确鞍核到圆领的可解性，不能以低残差单独收尾。

## 5. 下一批公开 Actions 命令

首轮固定度量求解：

```sh
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/ruled_core_to_tail_bvp.py \
  --length 1.0 --ruled-scale .24 --inlet-s .012 \
  --core-exact-length .01 --core-blend-length .04 --reference-flat-length .03 \
  --beta-wiggle .8 --radial-free 5 --modes 8 --angular 64 --radial-gauss 5 \
  --max-nfev 150 --out "$RUN_DIR/ruled-tail-L10-J5m8.json"
```

若该输出达到值得加密的误差，可使用同一完整度量：

```sh
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/ruled_core_to_tail_bvp.py \
  --length 1.0 --ruled-scale .24 --inlet-s .012 \
  --core-exact-length .01 --core-blend-length .04 --reference-flat-length .03 \
  --beta-wiggle .8 --radial-free 9 --modes 12 --angular 96 --radial-gauss 6 \
  --warm "$RUN_DIR/ruled-tail-L10-J5m8.json" --max-nfev 150 \
  --out "$RUN_DIR/ruled-tail-L10-J9m12.json"
```

第二条从 warm 文件载入同一个闭合控制，并检查整个参考身份；没有设计新的 $a$。
有限网格残差、曲率采样和标量闭合误差均仍须继续转成收敛及连续证据。
