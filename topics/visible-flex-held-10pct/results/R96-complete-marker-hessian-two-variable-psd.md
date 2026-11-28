# R96：完整三重帽 Hessian 的全二维准确 PSD 界

状态：**已证明，两个独立准确实现均实际返回成功。** 本条只改进 R67/R89 同一个完整有理函数的导数界；未选择新的物理帽参数，未修改已有场、旧 target g 或旧构造器。

## 1. 结论及适用范围

单位盘内定义
$$
\phi(z)=(1-|z|^2)^3\operatorname{Re}\frac{z^3}{1-z^3/2},
$$
盘外为零。则这一完整、未截断谐波的函数为 C²，且
$$
\boxed{\|D^2\phi\|_{\rm op}\le \frac{23}{10}.}
$$

R89 已证明的同函数高度与梯度界仍可直接使用：
$$
|\phi|\le\frac1{15},\qquad |D\phi|\le\frac45.
$$
本条将 R89 的 Hessian 界 `17/2` 改进为 `23/10`。证明的是两个矩阵 `K I±D²φ` 的正定性，不是断言非零紧支撑函数本身的 Hessian 为正半定。

## 2. 完整角变量下的精确 Hessian

令
$$
r=|z|,\qquad c=\cos(3\theta),\qquad
D=4-4r^3c+r^6,
$$
$$
P=2r^3(1-r^2)^3(2c-r^3).
$$
对 `r>0`，原有理函数准确等于 `P/D`，并且
$$
D\ge (2-r^3)^2\ge1
\quad(0\le r\le1,\;-1\le c\le1).
$$
这里全部 `c∈[-1,1]` 对应全部角度，没有角采样或有限谐波截断。

用下标表示普通多项式偏导，定义
$$
U=P_rD-PD_r,\qquad V=P_cD-PD_c,
$$
$$
A=U_rD-2UD_r,\quad
W=V_cD-2VD_c,\quad Y=V_rD-2VD_r,
$$
$$
C=\frac{rUD+9(1-c^2)W-9cVD}{r^2},\qquad
T=-3\frac{rY-VD}{r^2}.
$$
这些分子准确可被 `r²` 整除；程序在多项式系数层检查该事实，因此 `C,T` 也是普通有理系数多项式。双次数分别为
$$
\deg A=\deg C=(22,3),\qquad \deg T=(19,1).
$$

在正交极坐标标架 `(e_r,e_θ)` 中，Cartesian Hessian 的矩阵为
$$
D^2\phi=
\frac1{D^3}
\begin{pmatrix}
A&\sin(3\theta)T\\
\sin(3\theta)T&C
\end{pmatrix}.
$$
确实，其三个分量分别为
$$
\phi_{rr},\qquad
\frac{\phi_r}{r}+\frac{\phi_{\theta\theta}}{r^2},\qquad
\frac{\phi_{r\theta}}r-\frac{\phi_\theta}{r^2},
$$
且 `∂θ=-3sin(3θ)∂c`、`∂θθ=9(1-c²)∂cc−9c∂c`，给出上述公式。正交标架变化保持算子范数。

原点附近 `φ(z)=Re(z³)+O(|z|⁵)`，所以 Hessian 连续趋于零；也可直接由上述三个分子在 `r=0` 准确为零确认。原 Cartesian 分母为正的多项式，故内部无奇点。在 `r=1`，因 `(1-r²)³` 的三重消失，位置、一阶和二阶 jet 都为零；源码还准确核验 `P,U,V,A,C,T` 在该边界的多项式恒等零。因而盘外零延拓确为 C²。

## 3. 四个准确正多项式

取 `K=23/10`，对两个符号分别定义
$$
L_\pm=KD^3\pm A,
$$
$$
Q_\pm=(KD^3\pm A)(KD^3\pm C)-(1-c^2)T^2.
$$
若四个多项式在整个闭矩形上严格为正，则 `K I+D²φ` 和 `K I−D²φ` 都有正的第一主子式与行列式，因此都正定。于是两个 Hessian 本征值都位于 `[-K,K]`，得所宣称的算子界。无需独立补一个 `C` 对角证明。

本次主程序以纯 `Fraction` 多项式运算形成这四个多项式，再用**整数分子/公共正分母**的 tensor Bernstein 系数证明正性。先作 `c=2u−1`，所有初始幂到 Bernstein 的转换准确；随后全部二分使用整数 de Casteljau 公式，没有浮点舍入。

具体地，对一方向次数 `n`、共同分母 `d`、整数系数 `a_i`，中点左右子段的新整数系数为
$$
a_i^L=2^{n-i}\sum_{k=0}^{i}\binom{i}{k}a_k,\qquad
a_i^R=2^i\sum_{k=i}^{n}\binom{n-i}{k-i}a_k,
$$
共同分母均为 `2^n d`。在另一方向转置后使用同式。全部 Bernstein 基函数非负、和为一，正的全部系数严格证明整个闭矩形上的正性。

实际全域只需以下 **8 个闭矩形**（内部互不相交，边界共同）：

| `r` 区间 | `c=cos(3θ)` 区间 |
|---|---|
| `[0,1/2]` | `[-1,1]` |
| `[1/2,1]` | `[-1,0]` |
| `[1/2,3/4]` | `[0,1]` |
| `[3/4,1]` | `[0,1/2]` |
| `[3/4,7/8]` | `[1/2,1]` |
| `[7/8,1]` | `[1/2,3/4]` |
| `[7/8,15/16]` | `[3/4,1]` |
| `[15/16,1]` | `[3/4,1]` |

共 15 次盒检查、7 次二分，最大树深度 7。每个矩形上，全部四个多项式的 Bernstein 系数都严格为正。全叶最小系数为：

| 多项式 | 双次数 | 全叶最小准确系数 |
|---|---|---|
| `L+` | `(22,3)` | `23/10` |
| `Q+` | `(44,6)` | `529/100` |
| `L−` | `(22,3)` | `6771674038660002462344969 / 265963680315218418435358720` |
| `Q−` | `(44,6)` | `51624412585843371279312825048978263726700646560042293 / 276516109783006832124137170349920747318902437131059200` |

全部系数数组由源码准确再生；逐叶记录只保留矩形、准确最小值和完整系数矩阵 SHA，科学数组不入 Git。主程序另准确检查全二叉叶分割坍缩为根，且面积和准确为 2。

## 4. 实际执行与独立交叉检查

主源 [unit_marker_full_hessian_psd.py](../scripts/resume_20261128/tail/unit_marker_full_hessian_psd.py)，SHA256 `18160306c11257d3a1a989192e6ed160e3122b6206ea708dde268c47b9e8e5ef`，真正 child exit0。证明内部耗时 `0.149767437s`，observer 墙钟 `0.267140087s`，child 峰 RSS `12672 KiB`。首次外层 `/usr/bin/time` 不存在，shell exit127，未启动数学程序；该工程记录保留，不当作证明失败或数学返回。

独立源 [check_unit_marker_full_hessian_psd.py](../scripts/resume_20261128/tail/check_unit_marker_full_hessian_psd.py)，SHA256 `fe335312ffe06815065ad49c77274905c5f1e040d2280a4e6122a0019da4232c`，也真正 exit0：

- 用 SymPy 1.14.0 的独立准确有理微分核 `A,C,T` 与主源完全相同；主证明本身不依赖 SymPy。
- 对实际 8 个矩形重新进行完整仿射幂展开→Bernstein 转换，**6512 个准确系数**逐项等于主程序整数中点细分结果。
- 用独立矩形扫线核完整径向/角域没有缝隙或重叠，不调用主程序的二叉树覆盖检查。

主 summary SHA256 为 `e9d04cd6bcdfac4db07964f4f76494266d6f7730e2eff83395ecc81db2e52bed`；完整逐叶记录 SHA256 为 `4dc913d997f420ad6b5b783e424ceb8e19fa5c1bea73f7e8aa785a8c7d40fa9a`。同名小 JSON 保留主证明、实际 observer 和独立检查的真实标量/来源。任何未完成或非正矩形都会返回未认证，不会保留该 Hessian 上界。

复现（输出均在 checkout 外）：

```bash
python topics/visible-flex-held-10pct/scripts/resume_20261128/tail/unit_marker_full_hessian_psd.py \
  --bound 23/10 --outdir "$NEW_UNIT_MARKER_PROOF_DIRECTORY"
python topics/visible-flex-held-10pct/scripts/resume_20261128/tail/check_unit_marker_full_hessian_psd.py \
  --certificate "$NEW_UNIT_MARKER_PROOF_DIRECTORY/summary.json" \
  --out "$NEW_UNIT_MARKER_PROOF_DIRECTORY/independent-check.json"
```

## 5. 对最终标记设计的准确作用

若在实际半径 `a` 的真平盘内选择 `0<r≤a`，令
$$
f(x,y)=\varepsilon\phi((x+iy)/r),
$$
则
$$
|f|\le\varepsilon/15,\quad
|Df|\le4\varepsilon/(5r),\quad
\|D^2f\|_{\rm op}\le\frac{23\varepsilon}{10r^2}.
$$
单独就曲率充分门而言，`ε≤(123/23)r²` 保证 graph 主曲率不超过 `123/10`；若仍给帽保留 `119/10` 的预算，则充分门是 `ε≤(119/23)r²`。这些只是新的**曲率充分条件**，不是任何具体新全图已经验收。

给定新场实际平盘高度 `0<Z−≤Z≤Z+`，仍须准确支付
$$
X\cdot n\ge
\frac{Z_- -13\varepsilon/15}
{\sqrt{1+(4\varepsilon/(5r))^2}},
\qquad
|X|^2\le r^2+(Z_++\varepsilon/15)^2,
$$
并验证正分子、真实平盘域、完整几何预算和共同两阶 jet。任何改变 `r,ε` 的具体帽都是最终固定 g 冻结前的另一个设计选择；旧 canonical/R86/R89 构造器的原门保持，不能用假标签绕过。

同一完整帽的 `B3=π ε r⁵/140` 随幅度线性变化，但更强的 Hessian 上界本身不提供新 `δE`、新 reach/D 或“距离按同倍数放大”的结论。实际最终 λ1 图仍按它自己的 source/H/mean/height/geometry 支付这些责任。
