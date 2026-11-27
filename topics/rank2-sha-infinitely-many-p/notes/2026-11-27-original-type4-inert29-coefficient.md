# 原 type4 三维来源的固定惰性29低系数消费者

日期：2026-11-27。状态：唯一公开执行已返回，完整原系数行在模29下非零；范围限于本页所列固定输入。

本次只计算 R806 原 $B_4=\operatorname{im}P_{B_4}$ 的完整次数28系数行。
$P_{B_4}$ 沿 R798 的原三个半周期与绝对相位重建，保全部六列及其三维像；
不调用 CM13 fiber、main 或原算子重建，不扫描素数。
运行只在本公开仓库 Actions，使用 Python 与 python-flint 0.9.0，不保存输出文件。

## 1. 精确来源与完整递推

置 $u=z^6$，原 $b=1$ 模型 $y^2=x^3+1$ 的微分为 $dx/(2y)$。
写
$$
x(z)=z^{-2}A(u),\quad A(u)=1+\sum_{n\ge1}a_nu^n,\qquad
\log\frac{\sigma(z)}z=\sum_{n\ge1}f_nu^n.
$$
原微分方程给
$$
(A-3uA')^2=A^3+u,\qquad
a_1=-\frac17,\qquad
a_n=\frac{\sum_{i=1}^{n-1}a_i a_{n-i}}{(n-1)(6n+1)},\qquad
f_n=-\frac{a_n}{6n(6n-1)}.
$$
特别是 $a_1$ 的负号沿原 R817，而非换成另一条 $b$ 符号的曲线。
对 $p=29$、$m=p-1=28$，原第 $j$ 列
$\sigma^{34}x^{3j}$ 的最小次数为 $34-6j$，
故其完整系数准确为
$$
r_j=[u^{j-1}]\,\exp\left(34\sum_{n\ge1}f_nu^n\right)A(u)^{3j},
\qquad j=0,\ldots,5 .
$$
负指数系数为零，其余最大只到 $u^4$。指数递推为
$ne_n=34\sum_{k=1}^n kf_ke_{n-k}$。
源码同时在有理数域与 $\mathbf Z/29^2$ 中独立递推，并核完整椭圆方程窗；
所有实际分母须在该模数下可逆，不能先取浮点近似。

## 2. 全投影、原b17和阶乘

完整投影行是 $rP_{B_4}$，全部六列都保留。
同时计算原三个独立列基上的读数，核特征零和模29的秩恰3，
并在双坐标环
$$
(\mathbf Z/841)[\omega]/(\omega^2+\omega+1)
$$
独立核全矩阵幂等、全行回乘和确切约化。
惰性29没有 $\mathbf F_{29}$ 中的 $\omega$ 根，故不得用虚假的标量代入。

若 $\theta^6=17$，原 physical 基是
$17^{5-j}\sigma_{17}^{34}x_{17}^{3j}
=\theta^{-4}(\sigma_1^{34}x_1^{3j})(\theta z)$。
于是当前次数28的共同倍率准确为 $17^4$，再转 Hurwitz 行乘 $28!$；
源码保这两个完整整数以及模841的实际值，不把它们略去。

## 3. 一次实际执行的范围

入口：[脚本](../scripts/check-fixed-p29-original-type-four-pb4-row.py)，
请求名 rank2-original-type4-fixed-inert29-coefficient-v1，
复用既有 .github/workflows/rank2-sha-small-public-check.yml，
无共享workflow改动。原依赖为 R798 与其 R732 核；
两者源码哈希和本源码哈希由实际运行报告。

报告的 structural PASS 只指完整递推/投影/回乘这些确定恒等；
原行的零或非零另以观察布尔和精确读数如实输出，不预设非零。
尚不把这一次有限系数行称作原 $h_{j,29}$：
R1049 的原全部常数、toric/type4 比较以及小29的整格前提仍须另付。
它也不证明每条 eigenline 的非零、跨素数非零或通常全 $\Sha$ 结论。

实际 run、job、source、必要结果与全字节哈希在回执返回后补入；
可重算输出本身不入仓库。

## 4. 唯一公开回执与实际完整行

实际 [run46043135878](https://github.com/Rogerhu12/math-research-public/actions/runs/46043135878)，
job140655635855，source346dd26f5c8969b0b84664e568ce42b03b1e5dfa，
2026-11-27 17:36:20 UTC 返回。
原 PB4 在特征零及模29的秩均为3，原独立列为0、1、2。
完整次数28投影行准确为
$$
r_{28}P_{B_4}\bmod29=(20,27,7,20,23,21),
$$
全部 $\omega$ 坐标为零；其模841的完整返回为
$$
(803,665,819,832,429,688).
$$
故这个指定原三维来源上的系数 functional 非零，其精确最小29赋值为0。
原 $17^4\cdot28!$ 模841为260，完整 physical Hurwitz 投影行模841为
$$
(212,495,167,183,528,588).
$$
原有理递推与独立模841递推、全椭圆方程窗、全矩阵幂等与回乘均通过。
没有调用 CM13 main/fiber，也没有以删列代替三维原像。

### 原始回执标识

- 本源码10492B，SHA256 cab3239b165056f2adcb7ff11ac24c6575f4f2c7060c821d87c7987de2734598。
- R798源码SHA256 f6a1fe72d01b0c804059a06395c5a9c5d78e54d5742a6ca9af957febec9661b3。
- R732源码SHA256 d1b3c2f851e9ec6b6d6b6655141e36b4bb1108a30e57ff8365b5f583d880e469。
- 原stdout4974B，SHA256 178ad5340edfc621e1443e1e91f7923cd1aaa2d1143e2b2e681a4951e44163fa。
- 全job日志14176B，SHA256 db584df49865d4a4c937fffe1ae3e32bc270a652f2b9b42d7568a6e2bff27a1d。

必要的完整六列及来源在此消费；原stdout、矩阵表和日志均不另存文件。§3所列小29整格、全toric比较和跨素数范围仍保。
