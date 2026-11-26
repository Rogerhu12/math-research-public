# R994 — 原三个 beta27 中央值严格非零与新 Rankin 解析秩一

2026-11-27 / Astra-rank2-Sha-0b097461-20261127。

**已证明。** 保持 R991 的三个实际混合角色
$\beta_{27,j}=\psi_{27}\eta_j$，$j=4,10,16$，有
$L(\beta_{27,j},1)>0$。证明使用原完整理想角色、确定的快速收敛和及
包含全部无限尾的严格区间。公开 run `45907264125` 已真实成功；
没有在本地执行数学，没有用有限截断近似代替非零证明。

结合 R818 已证明的三个 $L'(\lambda_j,2)\ne0$，R991 的新实际
Rankin 输入在代数中心 $s=2$ 的解析阶准确为一。它的最高/混合
Chow 投影由 R995 给出。指定最高 AJ 的跨素数非零仍需继续证明。

## 1. 唯一主生成元给完整 Fourier 系数

固定 $K=\mathbf Q(\omega)$、$\omega^2+\omega+1=0$、
$\delta=1+2\omega$。R991 对实际 $E_{27}:y^2+y=x^3$ 给
$\mathfrak f_{\psi_{27}}=(3)$ 和
$\psi_{27}((\alpha))=\epsilon(\alpha)^{-1}\alpha$，其中
$\alpha\equiv\epsilon(\alpha)\pmod3$、$\epsilon\in\mu_6$。
类数为1，且 $\mu_6\to(\mathcal O_K/3)^\times$ 是双射。
因此每个素于3的整理想有唯一生成元

$$
\alpha=a+b\omega,\qquad a\equiv1\pmod3,\quad b\equiv0\pmod3,
\qquad \psi_{27}((\alpha))=\alpha.
$$

它的范数是 $n=a^2-ab+b^2$。所有素于原完整导子
$(34\delta^2)$ 的理想准确由上述条件再加 $(n,34)=1$ 给出。
这里没有把理想系数改成素数点数，也没有删掉惰性素数的偶次幂。

保持 R735/R806 的原嵌入：

$$
g_0=2+4\delta=6+8\omega\pmod{17},\qquad
g_0\leftrightarrow\zeta_{18}=e^{\pi i/9},\qquad
g_0^6=\omega,\quad\zeta_{18}^6=\omega.
$$

对 $\alpha$ 素于34，令 $k\in\{0,1,2\}$ 满足
$\alpha\bmod2=\omega^k$，并令 $e\in\mathbf Z/18$ 满足
$(\alpha\bmod17)^{16}=g_0^e$。R806(8)的原理想角色准确为

$$
\eta_j((\alpha))=\zeta_{18}^{6k-(j-9)e}.
$$

注意理想角色与 idèle 单位角色互逆；这里用的是前者。
令 $f_j=\theta(\beta_{27,j})=\sum_{n\ge1}a_{n,j}q^n$，于是

$$
\boxed{
a_{n,j}=\sum_{\substack{a^2-ab+b^2=n\cr
 a\equiv1,\ b\equiv0\ (3)\cr (n,34)=1}}
(a+b\omega)\zeta_{18}^{6k-(j-9)e}.}
$$

R991 已付的完整导子为
$N=|D_K|N_{K/\mathbf Q}(34\delta^2)=31212$，权为2，
全部坏 Euler 因子为1。该形式的 nebentypus 平凡，$a_{1,j}=1$。
共轭理想配对给 $a_{n,j}\in\mathbf R$。
系数还在 $\mathbf Z[\zeta_{18}]$ 中，$\zeta_{18}\mapsto\zeta_{18}^7$
固定 $\omega$ 并将三份 $l=j-9$ 按 $1\to7\to13\to1$ 循环。

源码在 $\mathbf Z[X]/(X^6-X^3+1)$ 的完整六坐标中作全部求和。
恒等式 $\omega=\zeta_{18}^3-1$ 给
$a+b\omega=(a-b)+b\zeta_{18}^3$。程序逐个完整系数核其共轭不变、
三份 Galois 循环及全部坏 Euler 零系数，随后才取实嵌入。

对于 $n\le M$，范数不等式
$a^2-ab+b^2\ge3a^2/4$ 及 $\ge3b^2/4$ 证明
$|a|,|b|\le2\sqrt{M/3}$。程序所用
$2\lfloor\sqrt M\rfloor+2$ 的方框包含这些全部点；primary 条件
给唯一代表，不按浮点角度选六次单位。

## 2. 函数方程给中央值的单个快速收敛和

R991 由全部2/3/17/无穷局部数据证明三个 $f_j$ 的完整 root number
均为 $+1$。权2的对应 Fricke 特征值为 $-1$，所以对 $y>0$

$$
f_j\!\left(\frac{i}{Ny}\right)=Ny^2 f_j(iy).
$$

在 $y=N^{-1/2}$ 处切分 Mellin 积分，并将下半段换元
$y=1/(Nu)$，两半完全相等。由 cusp 衰减及绝对收敛逐项积分，

$$
\boxed{
L(\beta_{27,j},1)
=2\sum_{n\ge1}\frac{a_{n,j}}{n}
\exp\!\left(-\frac{2\pi n}{\sqrt{31212}}\right).}
$$

这使用原完整 primitive 形式，未隐去坏 Euler 因子或 period。
所有正负号由 R991 的 root 表固定，没有因为预期非零另选符号。

## 3. 全部无限尾的显式统一界

范数为 $n$ 的理想数至多 $d(n)$，每个理想的
$|\beta_{27,j}(\mathfrak a)|=\sqrt n$。故

$$
|a_{n,j}|\le d(n)\sqrt n\le2n.
$$

置 $q=\exp(-2\pi/\sqrt{31212})$。对于任意截断 $M$，完整尾满足

$$
\left|L(\beta_{27,j},1)
-2\sum_{n=1}^{M}\frac{a_{n,j}q^n}{n}\right|
\le\frac{4q^{M+1}}{1-q}.
$$

指定 $M=4096$、Arb 精度256 bits。所有 $\pi,\sqrt N,\exp$、
代数余弦和求和都用包含真实值的 Arb 区间。
系数已准确为实数，因此其指定嵌入准确等于
$\sum_{r=0}^5 c_r\cos(\pi r/9)$，
$\cos(\pi r/9)$ 使用 `arb.cos_pi_fmpq` 的有理输入。

程序将先通过区间比较证明
$4q^{4097}/(1-q)<2^{-180}$，然后向包含全部舍入误差的有限和
加入闭区间 $[-2^{-180},2^{-180}]$。只有最终区间不含零时，
才返回该固定完整 $L$ 值非零。若任一条件失败，作业失败，
不会把浮点近似或单纯截断和记作结论。

## 4. 真实公开回执与严格非零结论

本次实际公开运行：

- source：`5ce57788fdf943376c908f815e42756f859dc0c7`；
- [run45907264125](https://github.com/Rogerhu12/math-research-public/actions/runs/45907264125)，job `140206875649`；2026-11-26 22:50:12–22:50:16 UTC，`success`；
- 脚本 `scripts/check-r994-original-beta27-central-values.py`，7353 bytes，SHA-256 `2cb869d7df36eac80fc3934c7eedfdd39a8be2e281bd060ef6d985783a2e0085`；
- `python-flint==0.9.0`，`--cutoff=4096 --precision=256`；完整数学运行约0.236秒；
- stdout 2284 bytes，SHA-256 `a04465aabc383fd7086bbb99cdb184b3861d0685c68933290a6931087a39cedb`；
- 完整 job log 10785 bytes，SHA-256 `0982a23ff0e401b398521f6dfecb0b92bd93854402c649875ab494f83cd8e6b3`。

完整枚举返回1236个素于导子的整理想。每份4096阶截断中有459个
非零 Fourier 系数，三份完整数组的共同摘要为
`1f63f8d6e0679edb637c26e5b706168ff5efefe788bfea3fd029643e58e2946f`；
完整理想计数摘要为
`197a27aea74f2b3ddc258474696fc12bf41d9948bed9a761c9c87cc99d92ab00`。
全部系数的精确实性、Galois 循环和坏 Euler 因子均通过。

真实区间计算给完整统一尾界

$$
\frac{4q^{4097}}{1-q}
\in[6.00236006726254931362949826943278864852424588\cdot10^{-62}
\ \mathbin{\pm}\ 4.18\cdot10^{-108}],
\qquad \frac{4q^{4097}}{1-q}<2^{-180}.
$$

将整个 $[-2^{-180},2^{-180}]$ 加到带所有舍入误差的部分和球之后，
得到下列完整值的严格有理开区间：

| 原嵌入 $j$ | 完整 $L(\psi_{27}\eta_j,1)$ 所在区间 |
|---|---|
| 4 | $(3.09536032325,\ 3.09536032327)$ |
| 10 | $(1.54464387169,\ 1.54464387170)$ |
| 16 | $(0.85665304997,\ 0.85665304998)$ |

这些宽于实际返回球的有理区间均严格位于正半轴，已足以证明非零。
结论不依赖显示更多小数，也不要求重跑其它截断或额外素数样本。
完整系数和日志只在公开 Actions 重算；仓库不存生成数组或 Release 数据。

## 5. 在新实际 Rankin 输入中的确切作用

R991 已逐处核定新 $E_{27}$ 输入的 toric Hom、有限2/3/17数据及
完整分解

$$
\mathcal L_{27,j}(s)=L(\lambda_j,s)L(\beta_{27,j},s-1),
\qquad \lambda_j=\psi_0^3\eta_j^{-1}.
$$

这里 $\mathcal L$ 是该 Rankin 形式按 R991 的代数中心坐标写出的
完整 $L$ 函数。R818 已证明
$\operatorname{ord}_{s=2}L(\lambda_j,s)=1$，而本篇给第二因子
在 $s=2$ 非零。因此准确得到

$$
\boxed{
\operatorname{ord}_{s=2}\mathcal L_{27,j}(s)=1,\qquad
\mathcal L'_{27,j}(2)=L'(\lambda_j,2)L(\beta_{27,j},1)\ne0
\quad (j=4,10,16).}
$$

这支付的是 R991 新输入的实际混合因子，不能用旧 R826 的不同
$\eta^{-2}\psi_0$ 替换；全部角色和 CM 定向保持。
R995 的严格最高投影可作用于实际新图族，但复解析秩一与投影存在
并不提供指定 $p$ 的 Abel–Jacobi 非零，更不自动给其跨素数非零。
本篇没有把该缺口省掉，也没有宣布 Sha 主目标完成。

## 依赖与 primary 来源

- R735、R806(8)：原有限生成元及完整理想角色；
- R991：实际三扭曲、完整导子、Fricke/root 数据及 Rankin 分解；
- R818：原三个最高 $\lambda_j$ 的完整复解析秩一；
- R995：实际 $I_9/I_3$ 曲面上的严格自伴最高 Chow 投影；
- [python-flint 0.9.0 Arb 文档](https://python-flint.readthedocs.io/en/latest/arb.html)：严格球运算、二进有理半径及有理角余弦接口。
