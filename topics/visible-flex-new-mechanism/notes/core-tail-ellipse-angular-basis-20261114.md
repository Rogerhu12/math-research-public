# 椭圆偏心角试探基与入口高 jet：表示诊断及可运行对照

**状态：解析换基与廉价实现检查已完成；没有运行新的非线性求解。**
`core_to_tail_bvp.py` 新增 `--angular-basis ellipse`，默认仍是 `material`。
`ellipse_core_continuation.py` 同名参数透传到底层求解器。下一批计算由本公开仓库的 Actions 执行。
这里没有构造精确半带，没有满足 [R3](../results/R3-mirrored-halfband-phase-family.md) 的条件。

## 1. 目标度量不换坐标，只有自由试探函数换基

沿用求解器的方向约定
\[
\gamma(\theta)=(A\sin\phi(\theta),-B\cos\phi(\theta),h_0),\qquad
a_0=\frac{2A}{\pi}E\bigl(1-(B/A)^2\bigr).
\]
偏心角由
\[
A E\bigl(\phi,1-(B/A)^2\bigr)=a_0\theta
\]
确定。令 $v^2=A^2\cos^2\phi+B^2\sin^2\phi$，则
\[
\phi_\theta=\frac{a_0}{v},\qquad
\phi_{\theta\theta}=-\frac{a_0^2(B^2-A^2)\sin\phi\cos\phi}{v^4}.
\]
自由场以 $1,\cos(k\phi),\sin(k\phi)$ 代替材料角三角函数，但所有残差仍在原 $\theta$ 坐标计算：
\[
f_\theta=f_\phi\phi_\theta,\qquad
f_{\theta\theta}=f_{\phi\phi}\phi_\theta^2+f_\phi\phi_{\theta\theta}.
\]
共同目标仍是 $ds^2+a(s)^2d\theta^2$；圆尾位置、二 jet 和材料对应关系也仍按原 $\theta$ 计算。
准确椭圆入口本来就在任意审计角网格上解析求值，**没有将入口截断到 12 模**。
被改变的是内部有限自由场的表示能力。

## 2. 为什么强椭圆需要这个对照

对 $A=1,B=.3$，以原材料角 Fourier 截断后，直接解析函数的最大向量尾误差如下。
最后一列是 $R=\rho n/a_0$，其中 $n$ 为平面内向单位法线，$\rho=1/\kappa$。

| 角模上限 | $\gamma$ | $\gamma_\theta$ | $\gamma_{\theta\theta}$ | $R$ |
|---:|---:|---:|---:|---:|
| 12 | $5.40\cdot10^{-3}$ | $8.13\cdot10^{-2}$ | $1.80$ | $2.32\cdot10^{-2}$ |
| 24 | $5.79\cdot10^{-4}$ | $1.65\cdot10^{-2}$ | $.565$ | $2.34\cdot10^{-3}$ |
| 48 | $1.66\cdot10^{-5}$ | $8.96\cdot10^{-4}$ | $5.21\cdot10^{-2}$ | $6.22\cdot10^{-5}$ |
| 96 | $3.64\cdot10^{-8}$ | $3.76\cdot10^{-6}$ | $3.99\cdot10^{-4}$ | $1.27\cdot10^{-7}$ |

这张表是有限试探空间的诊断，不能作为非线性残差的下界，也不证明基线必然失败。
但是入口正确 Cauchy jet 涉及 $R$，低材料角模可能很难校正它。
在偏心角中，$\gamma$ 恰是一模，而
\[
R=\left(
-\frac{(A^2+3B^2)\sin\phi+(A^2-B^2)\sin3\phi}{4Aa_0},
\frac{(3A^2+B^2)\cos\phi+(A^2-B^2)\cos3\phi}{4Ba_0},0\right)
\]
恰是一模加三模。这是直接展开 $v^2\sin\phi,v^2\cos\phi$ 得到的恒等式。
因而同样的自由度在核心附近有更合适的解析结构。
它不使原材料角圆尾变成有限偏心角模；边界仍由准确 Hermite 二 jet 硬性给定。

## 3. 设计度量时不能错误地锁死三阶项

下面仅讨论足够光滑的准确延拓，以便三、四阶展开合法；不将其当作任意 $C^2$ 场必须存在的高阶 jet。
令 $u=s/L$，且在圆柱入口
\[
a(u)=a_0+a_3u^3+a_4u^4+O(u^5),\quad
X(u,\theta)=\gamma(\theta)+Lu e_z+X_3(\theta)u^3+X_4(\theta)u^4+O(u^5).
\]
由 $|X_u|^2=L^2$ 的二、三次项，$X_3,X_4$ 都水平；由
$X_u\cdot X_\theta=0$ 的二、三次项，它们都沿 $n$。
再由 $|X_\theta|^2=a^2$ 的三、四次项及
$\gamma_\theta\cdot n_\theta=-a_0^2\kappa$，逐项得到
\[
\boxed{X_3=-a_3R,\qquad X_4=-a_4R.}
\]
当前五次 Hermite 桥与自由位置样条只硬锁位置二 jet，桥一般含人工三阶项。
固定参考度量的 $a_3=0$ 时，准确解须令该项归零；但**设计度量**的自由样条允许 $a_3\ne0$，不能把 $X_3=0$ 当作通用正确约束。
本次只新增换基，不修改这些既有边界条件。
`inward_gc4_collar_search.py` 是另一条固定度量、明确 $a_3=0$ 的四 jet 对照，不能直接替代本设计问题。

## 4. warm 数据身份与廉价验证

新 JSON 在 `discretization.angular_basis` 记录基名称。
旧 JSON 没有此字段时按 `material` 解释；同基可复用或径向投影系数，跨 `material` / `ellipse` 一律拒绝，要求显式场投影。
在椭圆延续中，轴比变化时同一偏心角系数随其基函数一起变化，这是延续种子，并不声称其表示同一个空间场。
driver 从外部 warm JSON 恢复时还检查周长及长度、核心柱高、母线族、圆尾尺寸、设计度量标记等固定参数。

可复现检查脚本：

```sh
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/ellipse_angular_basis_check.py \
  --out topics/visible-flex-new-mechanism/notes/core-tail-angular-basis-check-20261114.json
```

该脚本仅评估解析几何、有限差分和随机方向导数，不调用优化器；本次运行约 2.3 秒。
实际输出见 `core-tail-angular-basis-check-20261114.json`：

- 默认材料角基与显式旧公式误差均为严格浮点零；圆形时两基也相同。
- 偏心角链式一、二导数的独立四阶差分相对误差分别为 $1.23\cdot10^{-11}$、$1.01\cdot10^{-11}$。
- 随机自由系数下，端点 $X,X_s,X_\theta,X_{ss},X_{s\theta},X_{\theta\theta}$ 的最大误差为 $1.11\cdot10^{-16}$。
- 三个随机方向的完整残差 Jacobian 相对误差为 $3.28,4.69,3.92$ 乘 $10^{-11}$。
- 一加三偏心角模重建 $\gamma,R$ 的最大分量误差为 $7.11\cdot10^{-15}$。
- 两种跨基 warm 输入均被拒绝；同基及旧材料角输入接受。

## 5. Actions 对照输入

与已提交材料角基线相同的 L10 参数，仅增加 `--angular-basis ellipse`：

```sh
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/ellipse_core_continuation.py \
  --length 1.0 --h0 .23 --beta-wiggle .8 --radial-free 9 --modes 12 \
  --angular-basis ellipse --accept-metric 1e-4 --initial-step .125 \
  --min-step .0078125 --max-attempts 40 --max-nfev 250 \
  --out-dir "$RUN_DIR" --prefix ellipse-L10-phi
```

L11 只改 `--length 1.1 --h0 .25 --prefix ellipse-L11-phi`。
两个 `--plan-only` 输出已保存在 `ellipse-L10-phi-plan-summary.json`、`ellipse-L11-phi-plan-summary.json`。
这是同规模换基的可比较试验；设计通过后仍须真正冻结共同度量、加密审计及全曲面几何证书。
