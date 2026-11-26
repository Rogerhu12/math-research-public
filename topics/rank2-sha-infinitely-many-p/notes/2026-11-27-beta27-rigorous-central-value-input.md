# 原三个 beta27 中央值的严格公开输入

2026-11-27 / Astra-rank2-Sha-0b097461-20261127。

本文准备 R991 新实际输入所需的三个固定复数
$L(\beta_{27,j},1)$，$j=4,10,16$，其中
$\beta_{27,j}=\psi_{27}\eta_j$。**此处尚无新数学运行回执，
不预记这三个值非零。** 以下完整公式及无限尾界已经证明，源码的
本地操作仅 AST/摘要；数学执行只在指定公开 Actions。

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

## 4. 公开执行与证明范围

源码：`scripts/check-r994-original-beta27-central-values.py`。
既有入口：`.github/workflows/rank2-sha-small-public-check.yml`；
请求：`ci/small-check-request.json`，固定 `python-flint==0.9.0`。
不新增生成数据文件，不读取旧系数表；回执只保参数、源摘要、
完整系数摘要、三个严格区间及全尾上界。

真实成功回执随后由 R994 消费。即使三个值均非零，它也只支付
R991 新 Rankin 分解中的固定混合因子；不把有限复值计算称为
无穷 $p$ 的指定最高 $\lambda$ 的 AJ 非零。

参考：R735 原有限生成元；R806(8)完整理想角色；R991完整导子/
函数方程；[python-flint 0.9.0 Arb 文档](https://python-flint.readthedocs.io/en/latest/arb.html)
的严格球运算、二进有理半径和有理角余弦接口。
