# R795：只补原普通 power6 的准确 q0–81 前缀

日期：2026-11-15。状态：**固定新计算方法；实际完成须由公开 Actions 的输出认证。**

本任务只做 R793 所需的 $V_6=H^0(Y_L,6\mathcal L)$ 准确短基。
原 $\deg\mathcal L=272$、$g(Y)=127$，故 $\dim V_6=1506$。
不生成 $M_{12}$ 的椭圆主部补方向，不求 $\mu_{33}$ 的坐标表，
不重算原 E1、M2、power2–5 或任何 Laurent 递推。

## 1. 固定实际输入

读取成功 R775 run43679160495 的
`R775-basis-power-6.json.gz`，SHA256
`05c5580b73eeba72b832e2a871221c19c482baf1c9656cab62a0c2c694ffafa1`。
它保存原顺序的1506条 recipe、实际 rank/minor 和 finite 系数。
全部实际 recipe 的幂次都是 $(1,5)$；核心仍逐条检查这一 schema。

每条 recipe 的两个因子直接读成功 R786 run43682100611 已认证的
`R786-exact-power-1-row-*.json.gz` 和
`R786-exact-power-5-row-*.json.gz`。
旧行保留全部原文件和原 SHA；计算仅消费其 $q_Y^0,\ldots,q_Y^{81}$。
旧 R786 的 M2/power5 输入 SHA 与新成功 R775 证书对应阶段的 SHA
逐项相等，故两个生产者使用同一原保存顺序，不以维数相等代替规范核验。

每个生产者的 run/source/core/manifest/cert 均绑定。
R786 的准确基 index、stages manifest 与实际行也逐项绑定。
首次下载之后，所需输入随本任务一日 bundle 转交续算；
不因旧 artifact 过期重新生成旧算术。

## 2. 只作一个新六次乘积

原因子的准确整数尺度分别为 $82^2$ 和 $82^{10}$。
所以本次相乘的结果恰为原六次截面的 $82^{12}$ 倍。
输出保留原 $q_Y$、原 $\xi_{41}$ 方向和原 factor recipe。

令每个系数使用 $1,\xi,\ldots,\xi^{39}$ 表示，
$\Phi_{41}(\xi)=0$。将双变量多项式编码为

$$
\sum_{n=0}^{81}\sum_{r=0}^{39}c_{n,r}Z^{79n+r}.
$$

一次 FLINT 整数多项式截断乘法即可得到所有新系数：
两个因子的 $\xi$ 指数和至多78，严格小于间隔79，故不会跨越
一个 $q_Y$ 块。每块先按 $\xi^{41}=1$ 折叠，再用
$\xi^{40}=-\sum_{r=0}^{39}\xi^r$ 约化。
最高只取 $q_Y^{81}$；未使用也不生成129至141的新尾项。

每条新行准确代入原 $\xi\mapsto538\pmod{739}$，并核

$$
\text{new coefficient}\equiv
82^{12}\,\text{retained R775 coefficient}\pmod{739}
$$

对全部82阶成立。旧 finite 系数只作绑定和比较，不将模739数据
当成特征零系数提升。

## 3. 同时保留原实圆分坐标

R793 已证明普通偶权的相同运输
$v=\xi^{-10}q_Y$。对本次新行的第 $n$ 项准确乘 $\xi^{10n}$，
逐项检查反演不变，然后用

$$
t=\xi+\xi^{-1},\qquad C_0=2,\ C_1=t,
\ C_r=tC_{r-1}-C_{r-2}
$$

转成 $1,t,\ldots,t^{19}$ 的整数坐标。
模数是 $1+\sum_{r=1}^{20}C_r$。
不取平均制造不变性。原 $q_Y,\xi$ 的40坐标和运输后 $v,t$ 的
20坐标同时存入每条新行，供后继固定 RR 乘法读取。

这是新 power6 行的坐标运输，不重新运输或重算旧 power1–5 行。

## 4. 完成判据与边界

R793 的二十 cusp 单轨道给 $20\cdot82>1632$，所以整个 $V_6$
到上述82项完整系数的限制单射。原1506条 recipe 已由 R775 的
真实非零 minor 证明为特征零基；本次不另做一次基选择。

只有原顺序1506行全部完成、每行 factor SHA、原尺度、mod739
比较和实圆分反演检查全部通过，才输出新完整证书。
断点只恢复同 core/proof/method/producer 配置下已完成的行，
不重算已完成新行。

完整证书不表示新 $\mu_{33}$、1116阶第二关系、极除子、
Jacobian 点或高度已经生成。后继实际 RR 线性代数仍须继续。
所有新算术只在公开仓库 Actions 执行；新行及输入 bundle 只在
当前一日 artifact 传递，不入 Git 或 Release。

依据：R775 原成功基、R786 原准确 power5 短基及
[R793](../results/R793-original-RR-pole-divisors-and-CM-local-algebra.md) §1。
