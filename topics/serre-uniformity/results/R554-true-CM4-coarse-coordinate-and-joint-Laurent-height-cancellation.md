# R554 — 两个真正 CM4 粗图的原坐标与高度可去极项

## 1. 已完成的结论和范围

在原 R228 有理超奇异 atlas 的两个真正椭圆粗图
SS_j36_06、SS_j36_02 上，保留原来的单位框架 \(f_c\) 和射影参数
\(z=Wc-W(P)c\)。本条实际计算六阶截面、四阶真实 \(j\) 映射及规范高度导数中
\(\eta_B\) 与 \(j-1728\) 的联合可去极项。两盘的 \(j'\) 都是单位。
R435 的清极截面在这里不为单位，不妨碍原 \(f_c\) 框架或原参数使用。

令 \(Q=47^4=4879681\)、\(q=47^3=103823\)。以 \(z\) 的升次序，实际数据为：

| 圆盘 | \(j_0,\ldots,j_4\bmod Q\) | \(\eta_B/dz-z^{-1}\) 的前三系数 \(\bmod q\) |
|---|---|---|
| SS_j36_06 | [1728,2172352,4443895,2141984,1865435] | [68620,60578,31122] |
| SS_j36_02 | [1728,2378879,65920,4590460,1771836] | [63048,18009,103107] |

完整 F2 导数中的以下组合在两盘均整且正规：

$$
\mathcal R_2(z)=
-4\frac{j''}{j'}+\frac83\frac{j'}j
+2\left(\frac{d}{dz}\log\frac{j-1728}{z}
-\left(\frac{\eta_B}{dz}-\frac1z\right)\right).
$$

| 圆盘 | \(\mathcal R_2\) 的前三系数 \(\bmod q\) | F3 对应组合 \(\mathcal R_2/2\bmod q\) |
|---|---|---|
| SS_j36_06 | [41435,88721,28106] | [72629,96272,14053] |
| SS_j36_02 | [42135,12464,91687] | [72979,6232,97755] |

这里没有单独对 \(j-1728\)、零清极截面或非单位取逆。本条完成的是实际局部接口；
未计算两盘的主函数 Norm、中心高度或全部 QC 根，不能把两盘计作已排除。
绝对 Serre 统一性仍为 OPEN。

## 2. 原坐标和实际椭圆粗参数

原 atlas 的 CM4 图为 chart 6，盘序为 SS_j36_06、SS_j36_02。
它们是 CM4 粗图的行 0、15，项链标签为 5、614。框架精确等于 \(f_c\)。
采用原全局导数矩阵 \(H\)，在这个框架中：

$$
W'(z)=\frac{V_3(W(z))H}{H_c(z)},\qquad
H_c(z)=V_3(W(z))Hc.
$$

两个 \(H_c(0)\) 分别为 \(2031625,1572500\bmod Q\)，模 47 分别为 \(3,21\)，
所以递推到六阶只使用单位逆和 \(1,\ldots,6\) 的逆。
所得 \(W,V_2,V_3\) 的零到三阶系数逐项等于原 atlas。
这证明计算没有换用其他同 \(j\) 项链点或改变原参数。

再用 R208 已认证的物理 CM4 粗族 \(A_{\rm phys}=1\)、\(u=B_{\rm phys}^2\)，
计算 \(z(u)\) 并作单位级数反演。其 \(u(z)\) 零到三阶与第 3 节的不变量公式一致；
全部 73 个物理截面在原框架中的组合也逐项一致。
最后，从同一 \(W/H_c\) 计算全部 54 个典范微分的零到二阶系数，
逐项等于原 tiny 文件。输入 SHA 链同时核实原 tiny、原 SS atlas 和全部 129 盘版本。

因此，后续主函数、Abel 常数和高度必须沿用这些同一坐标数据；
不能用栈参数 \(B_{\rm phys}\) 替换粗参数并遗漏二次分歧。

## 3. 清极截面的精确形式消去

采用已发布的原全局 Serre 清极数据 \(v,G\)，其中 \(G=v\delta(W)\)。
R208 的齐次不变量是

$$
\mathcal A=A_{\rm phys}v,\qquad
\mathcal B=B_{\rm phys}v^3
=\frac{v\,d\mathcal A[G]-\mathcal A(Gv)}6.
$$

这里 \(A_{\rm phys},B_{\rm phys}\) 表示与截面尺度相容的 Weierstrass 不变量；
\(\mathcal A,\mathcal B\) 是实际 \(W\) 中次数 3、6 的齐次截面。
在真正 CM4 粗中心，既有粗图构造给出精确消失阶

$$v=zV,\qquad \mathcal B=z^2\widetilde B,$$

而 \(V(0),\mathcal A(0),\widetilde B(0)\) 都是单位。本次在原图中实际重算这些系数
到六阶，并核实零系数和三个单位条件；消失阶的几何含义由原 CM4 粗族固定，
不是仅凭某个模 \(Q\) 的零值推断精确恒等式。

尺度不变的粗参数于是为

$$
u=\frac{B_{\rm phys}^2}{A_{\rm phys}^3}
=\frac{\mathcal B^2}{\mathcal A^3v^3}
=z\frac{\widetilde B^2}{\mathcal A^3V^3},
\qquad
j=\frac{6912}{4+27u}.
$$

右边全部分母都是单位。形式除以 \(z\) 或 \(z^2\) 只移除已经证明为零的首项，
没有除以 47。由上式计算的四阶 \(j\) 系数见第 1 节。
\(j'(0)\bmod47\) 分别为 \(12,21\)，所以 \(j-j(P)\) 是这两个粗图上的单位局部参数。
同时 \(j-1728=zJ(z)\)，其中 \(J(0)=j'(0)\) 为单位。

## 4. 真实第三类微分的 Laurent 消去

原已校准的 \(\eta_B\) 在全部 20 个真正 CM4 点有留数 \(+1\)，
其相反留数位于尖点支撑。本条使用该同一微分的真实分式

$$
\frac{\eta_B}{dz}
=\frac{N(z)}{D(z)H_c(z)},\qquad
N=V_3(W)s_B,\quad D=V_2(W)q_B.
$$

本次两盘均实际得到 \(D(0)=0\)、\(D'(0)\) 为单位。写 \(D=zD_1\)。
通过原校准的精确留数条件，级数

$$\beta(z)=\frac{N(z)}{D_1(z)H_c(z)}$$

的常数为 \(1\)。因此

$$
\frac{\eta_B}{dz}=\frac1z+\frac{\beta(z)-1}{z},
\qquad
\frac{d}{dz}\log(j-1728)=\frac1z+\frac{J'}J.
$$

两个极项精确抵消，留下

$$
-2\frac{\eta_B}{dz}+2\frac{j'}{j-1728}
=2\left(\frac{J'}J-\frac{\beta-1}{z}\right).
$$

这是同一真实微分及同一实际 \(j\) 函数的恒等式。
没有改写 \(\eta_B\) 的极点支撑，没有把真极点当成可通过换辅助分母移除的假极点，
也没有给两个单独发散的对数任意赋值。

原 F2 完整导数中的自正规项为 \(8r_z-4j''/j'\)。
保留 \(8r_z\) 在其原位置，把其余
\(-4j''/j'+(8/3)j'/j+2j'/(j-1728)-2\eta_B/dz\)
合成 \(\mathcal R_2\)，即得第 1 节公式。
F3 中这些系数同时减半，故使用 \(\mathcal R_2/2\)。
T2/T3 迹、固定连接、中心 Norm、规范纤维和同分量筛选均仍须实际完成。

## 5. 整性、尾界及独立核验

原单位框架给整的代数局部级数。\(H_c,j',j,J,D_1\) 的常数都是单位，
而 \(\beta-1\) 精确含因子 \(z\)。故整个联合项在该剩余盘上具有整系数，
没有引入新的负 47 赋值。这允许后续完整高度继续使用原移动连接的尾估计；
本条没有仅凭三项截断宣称完整高度或根已经求出。

两个引擎本次均已实际执行。独立核验器用 Python 整数复数对：

1. 从原模型矩阵重建七个系数层的 7336 个 \(V_2,V_3\) 分量。
2. 逐项重算 876 个原射影微分方程分量，验证全部 \(W_1,\ldots,W_6\)。
3. 对齐次截面作独立形式方向导数，重新生成 \(\mathcal A,\mathcal B\)，
   再计算三个单位、\(u(z)\) 和 \(j(z)\)。
4. 重新计算全部 54 个 tiny 微分、真实 \(\eta_B\) 分子分母、
   两个留数 \(1\)、极项抵消及第 1 节全部系数。

该独审以既有忠实模型作为输入，不声称重新生成 41 挠点、全局模型或长群链。
证明的输入、原数据和算术范围均在清单中明确保存。

| 文件 | SHA-256 |
|---|---|
| p41_true_CM4_regular_height_derivative47.json.gz | c21ddac95926d7b3c9ae77a1ddbf75eff990f6142ddf87fb9e3734f2d7c88220 |
| p41_true_CM4_regular_height_derivative47_independent.json | 7cf41823e8294fcd63546d99704ad2ae3351a5316a4ca9dbeefd6694a0c13b56 |
| 生成器 | 8a857b5a73152ede6e7f9632b6c1064603e830e2e7b195b9e10fb0da7dc01f6a |
| 独立整数核验器 | beeef41b3ca51348e2f87fc38afd831c2d791f7d8b34471ec5c426899ee06676 |

精确恢复命令如下；输出目录须先存在：

    OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
    python topics/serre-uniformity/scripts/p41_true_CM4_regular_height_derivative47.py \
      --script-dir topics/serre-uniformity/scripts \
      --work-dir /absolute/path/to/CM4-rebuild \
      --output /absolute/path/to/CM4-regular.json.gz

    OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
    python topics/serre-uniformity/scripts/verify_true_CM4_regular_height_derivative47.py \
      --script-dir topics/serre-uniformity/scripts \
      --certificate /absolute/path/to/CM4-regular.json.gz \
      --generator topics/serre-uniformity/scripts/p41_true_CM4_regular_height_derivative47.py \
      --output /absolute/path/to/CM4-independent.json
