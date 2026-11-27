# R150 unit211：h=k 上整个 J=Q 面的原方程排除

日期：2026-11-27。会话：Astra-ISP-8542378f-20261127（AI-assisted GPT-6 Astra Pro）。

## 结论与适用范围

在 [原四值 atlas](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md) 的 unit211 一般 LS 原系统中，**h=k 的整个 J=Q 面无解**。这里不引用旧 D≠0 值图上的 J=Q 权排除；h=k 本来使 D=0，两个互补的 Delta 图均在本碰撞参数上重建同一组原矩与 Gram 方程。

整个 T0=0 已由[独立碰撞证明](R150-appendix-unit211-equal-singleton-entire-T0-zero-original-exclusion.md)排除。因此在尚未排空的 h=k 图上，现可支付 Pf=T0(J−Q)≠0。本结论不排空整个 h=k，不排空 unit211，更不解决普通 ISP。

## 1. 原参数与本面的恒等式

沿用已支付的非零原权、u≠0,1、Q≠0、rho≠0、p=1+rho、q=1−rho、bc≠0，以及整个 S=0 的原排除。令

$$
 A=2\lambda^2-2\lambda+1,\quad B=4\lambda^3-6\lambda^2+3\lambda-1,
 \quad \xi=B/A,\quad \ell=A^3/B^2,\quad T=A^2/B.
$$

原 h=k 的二、三矩给 h=k=1+xi；h=k=1 不可能，故 A、B 非零。再令

$$
 d=\rho^2=1-Q,\quad u=bp+cq,\quad
 b=\ell/2+(u-\ell)\rho/(2d),\quad c=\ell/2-(u-\ell)\rho/(2d),
$$
$$
 S=2\xi+3-2\lambda,\quad \eta=\xi+3-2\lambda,\quad w=\lambda-1-T,
$$
$$
 V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
 J=2u(1-u)+\ell Q,\quad
 \Phi=T_0+4u-4+Q,
$$
$$
 P_{02}=(2-3u)V_2-Qu+2u^3,\quad
 G_0=\lambda P_{02}-(1-u)T_0,
$$
$$
 P_f=T_0(J-Q),\quad P_c=QP_{02}(\ell+T)-G_0T_0,
$$
$$
 N_F=(3-4\lambda)Q+J\xi\eta,\quad
 N_C=\eta(-G_0\xi+Qwu),\quad
 \Delta=\Phi N_F-S\xi P_f.
$$

保留的两个原仿射式恰为

$$
 P_c+P_f f+bcQ\Phi t=0,\qquad
 N_C+N_F f+bcQS\xi t=0. \tag{1}
$$

令 J=Q。若 ell=1，则 2u(1−u)=0，与原域矛盾，故 ell−1 在本面非零。直接原式化简得

$$
 Q=\frac{2u(u-1)}{\ell-1},\quad
 T_0=Q(1-2\ell),\quad P_{02}=2(1-u)T_0,\quad
 \Phi=-4(u-1)^2\ne0,\quad P_f=0,
$$
$$
 N_F=\frac{Q(1-2\lambda)(3\lambda^2-3\lambda+1)}{A^2},
 \qquad \Delta=\Phi N_F. \tag{2}
$$

这些是同一原参数恒等式，不是追加必要条件。第一原式给

$$
 t=-P_c/(bcQ\Phi). \tag{3}
$$

## 2. Delta=0：整个二次常数域、自由 f 的原返回

由 (2)，Delta=0 强迫 lambda=1/2 或 3lambda²−3lambda+1=0。lambda=1/2 已落入原 S=0 的完整排除；余者在

$$
 K=\mathbb Q[\lambda]/(\lambda^2-\lambda+1/3)
$$

整体处理。这个多项式不可约，两个复嵌入全部保留，没有选取数值根。其上原参数为

$$
 \ell=(11-9\lambda)/49,\quad T=(\lambda-2)/7,\quad
 \xi=-1-\lambda,\quad S=1-4\lambda,\quad \eta=2-3\lambda,\quad
 w=(6\lambda-5)/7.
$$

把 (3) 代回第二原式并除原单位 Q，所得恰为

$$
 \left(\frac{183}{259}-\frac{729}{518}\lambda\right)u
 -\frac37+\frac{12}{7}\lambda=0. \tag{4}
$$

系数等于 3(122−243lambda)/518，范数中
Nm(122−243lambda)=4921=7·19·37，故在整个 K 中为单位。由原式 (4) 唯一恢复

$$
 u=(58-70\lambda)/19,\quad
 Q=-3872/1083+(4188/361)\lambda,\quad
 \Phi=1348/1083+(2240/361)\lambda. \tag{5}
$$

全部实际使用的原系数分母逐个以 K 中扩展 Euclid 反演并乘回；没有倒 Delta 或 NF。保留自由原参数 f，以 (3) 的同一个 t 重建 E0、N0、P1、NV、所有原矩和两个孤立值的原目标，得到八行

$$
 E_1,E_{Be},E_{Bo},N_1,N_{Be},N_{Bo},P_{Be},P_{Bo}\in K[f]
$$

的 f 次数为 2,2,2,1,3,3,3,3。偶、奇系数的同时消失来自两条实际 B/C 原行及 rho≠0；没有从单条含 rho 方程擅自逐项置零。

仅前两行即给 K[f] 单位。为使小证书可独立定位，E1 的 f 升幂系数为

$$
 \frac{2151968-1878324\lambda}{206131},\quad
 \frac{250016-778878\lambda}{75943},\quad
 \frac{-1866+1566\lambda}{571}.
$$

EBe 的升幂系数为

$$
 \frac{14417246773}{2118614418}-\frac{1648953955}{353102403}\lambda,\quad
 \frac{239183}{2934369}-\frac{5894275}{978123}\lambda,\quad
 \frac{-2051687+2938554\lambda}{978123}.
$$

实际扩展 Euclid 返回一次多项式 a(f),b(f)∈K[f]，完整乘回

$$
 a(f)E_1(f)+b(f)E_{Be}(f)=1.
$$

两条 a,b 的所有有理数系数、原两行和常数域多项式保存在随文 receipt 的 fullCertificate 中，820 bytes，SHA256
b3a7c1690c80c19d9c4826b2f65138670e6c8ad6f1403e0d27ad761e8b95a827。
本次共 29 次真实常数逆与 4 次多项式除法，未拆分或丢弃任何常数根，故整个 Delta=0 面排空。

## 3. Delta≠0：未缩放的八原式与固定结式

此时 NF≠0，(1) 在同一原参数上给

$$
 f=\frac{S\xi P_c-\Phi N_C}{\Delta},\qquad
 t=-\frac{P_c}{bcQ\Phi}.
$$

直接以 H=1 的未缩放原矩重建八行；不是先除一条旧 D≠0 的 Gram 定理。源实际乘回两条 (1)、E0/N0/P1/NV 与两条孤立目标。仅除去已经支付的原单位后，QQ[lambda,u] 八个完整分子的次数如下。

| 原行 | lambda 次数 | u 次数 | 项数 |
|---|---:|---:|---:|
| E1 | 26 | 2 | 76 |
| EBe | 34 | 3 | 134 |
| EBo | 28 | 2 | 83 |
| N1 | 18 | 1 | 37 |
| NBe | 50 | 5 | 294 |
| NBo | 42 | 4 | 203 |
| PBe | 58 | 6 | 401 |
| PBo | 48 | 5 | 282 |

所有多项式的精确因子及已付原单位移除记录见 receipt。逐个分母审查只使用原 A、B、ell−1、d、bc 与本图 NF 等已付量；移除分子中的 T0、S、u−ell 等时，分别使用此前独立的完整碰撞证明。没有新首项被当成单位。

取 E1/EBo 的固定 4×4 Sylvester 行列式及 E1/N1 的固定 3×3 Sylvester 行列式。每个移位行逐项重建回原多项式；不除 u 最高项，因此最高项为零的 lambda 纤维仍被覆盖。它们在 QQ[lambda] 中的次数分别是 102、58。实际去掉仅由已付单位贡献的 gcd 因子后，得到必要多项式 R60、R33：

| 固定原投影 | 原次数 | 已付移除后次数 | 升幂系数 JSON SHA256 |
|---|---:|---:|---|
| Res_u(E1,EBo) | 102 | 60 | 704ecf1d842c5da0c51a9fdc624a4f0d512ef3dd8324fce2667665347a4ba9d4 |
| Res_u(E1,N1) | 58 | 33 | 60d8936db612136f5a538bae28ce8e13a02a45f881b6b70d37b1bb395f9c95bc |

R60 的移除标签依次为 A2:3、B3:4、ell−1:2、bc:2、NF:4；R33 为 A2:2、B3:2、ell−1:2、bc:1、NF:2。这里的数字是完整 gcd 除法循环次数，**不表示把标签对应多项式按这些次幂整块相除**。每步 pp=quotient·gcd 和最终原乘积均实际检查。

完整 QQ 扩展 Euclid 得

$$
 \gcd_{\mathbb Q[\lambda]}(R_{60},R_{33})=1.
$$

源返回每步 Bézout 乘积与累计两输入组合，最终常数 1。两个精确升幂系数数组均保存在小 receipt，源可直接重算单位证书。因任一原复解必须同时使 R60、R33 消失，矛盾。没有有限域抽样、单根代入或泛型头非零假设。得到单位后立即停止，未额外重放后续投影。

## 4. 实际执行与复现身份

两次任务均由真实公开 Actions 在部分克隆中实际 pull --rebase，并检查根/课题 README 差异；本次均无差异。使用 Python 3.12.14、python-flint 0.9.0、单线程。

| 原图 | 源 SHA256 | run / job | 驱动秒数 | 峰值 KiB | 源退出 |
|---|---|---|---:|---:|---:|
| Delta=0，完整 K[f] | f7c64310689e077bfb2b6aaea57bdefd724a9f01ca9b38b5266a72935f80e08c | 46013488114 / 140554634214 | 0.088397285 | 34568 | 0 |
| Delta≠0，完整 QQ 投影 | 57a419da9e60bd135f1a41943604889f1e62e67a16239d87c0c9560f84a8a92e | 46013953380 / 140556219747 | 0.349964772 | 41064 | 0 |

源：

- [Delta=0 完整二次原返回](../notes/2026-11-27-unit211-equal-singleton-JQ-Delta-zero-complete-quadratic-original-return-8542.py)。
- [Delta≠0 两参数完整原返回](../notes/2026-11-27-unit211-equal-singleton-JQ-nonzero-Delta-original-two-parameter-return-8542.py)。
- [两图实际小回执及完整小证书](../notes/2026-11-27-unit211-equal-singleton-entire-JQ-zero-original-exclusion-receipt-8542.json)。

Delta=0 源自身的 complementaryDeltaNonzeroFaceStillOpen 是该单次运行的适用范围，不覆盖第二次运行。本证明以第二次完整原返回封闭它。两图互补，且前置原退化面已付，故得到所述整个 J=Q 排除。剩余 h=k 的原 Gram 系统继续，不借此宣布任何更大分支已空。
