# q096 固定角图对高度均值的 convection 项：全部 28 模一致严格权重

日期：2026-11-13。这里补的是有限场连续比较中的一项精确角积分。没有读取 M28 场、没有新 BVP/尾求解，也不把法向速度的均值一并视为已付。

## 固定输入与准确对象

使用 actual q096 保存的同一角图：

\[
 \theta=\psi+b(s)A(\psi),\quad
 A=\frac{d_2}{2}\sin2\psi+\frac{d_4}{4}\sin4\psi,\quad
 B=A_\psi=d_2\cos2\psi+d_4\cos4\psi,
\]
\[
 d_2=-3c_2,\quad d_4=-15c_4,\quad
 c_2=0.09,\quad c_4=-0.006363961030678927,\quad
 L=3.1496673569886275.
\]

以上十进制只作可读展示；实际计算输入是保存 binary64 参数的精确有理数，与此前 chart transport 证书一致：

- c2 = 3242591731706757/36028797018963968；
- c4 = −7337147526749689/1152921504606846976；
- L = 7092420367637499/2251799813685248。

profile 和 reference chart 均不改变；\(b=1-S(s/L)\)，\(S(x)=10x^3-15x^4+6x^5\)。因此 \(0\le b\le1\)，
\[
 |b_s|\le \frac{15}{8L},\qquad |b_{ss}|\le \frac6{L^2}.
\]
第二个常数覆盖精确峰值 \(10/\sqrt3<6\)。这些是理想精确图的界，NumPy 实现的逐次浮点误差没有由此自动支付。

原 Frenet 程序在固定 ψ 下使用 \(V=V_{\rm normal}+vF_\psi\)，其中
\[
 v=\frac{b_sA}{1+bB}.
\]
ψ 上的等权均值没有额外 ρ 权。即使 A 和垂直导数都是奇函数，二者的乘积通常不为零，所以不能丢掉此项。

设两有限场的 vertical raw 系数差为 \(\Delta Y_j(s)\)，实际高度扰动为
\[
 \Delta Z=q\sum_{j=1}^{M}\Delta Y_j(s)\cos(2j\psi),\qquad q=0.09.
\]
q 是固定 gauge，已计入本条最终权重；使用权重时乘原 normalized 系数差，不能重复乘 q。

定义
\[
 C_j(b)=\frac1{2\pi}\int_0^{2\pi}
       \frac{A(\psi)\sin(2j\psi)}{1+bB(\psi)}\,d\psi.
\]
convection 对均值一阶差的准确贡献为
\[
 \Delta H'_{\rm conv}
 =-q\,b_s\sum_j(2j)\Delta Y_j C_j(b).
\]
其径向导数为
\[
 \Delta H''_{\rm conv}
 =-q\sum_j(2j)\left[
 b_{ss}\Delta Y_j C_j+
 b_s\Delta Y'_j C_j+
 b_s^2\Delta Y_j C'_j
 \right].
\]

## 全 b 区间的几何级数证书

令 \(r=|d_2|+|d_4|<1\)。对所有 \(b\in[0,1]\) 与所有 ψ，
\[
 \frac1{1+bB}=\sum_{k=0}^{K}(-bB)^k+
 \frac{(-bB)^{K+1}}{1+bB}.
\]
取 \(K=32\)，并以
\[
 A_{\max}=|d_2|/2+|d_4|/4
\]
作独立三角上界。于是
\[
 C_j(b)=\sum_{k=0}^{32}(-b)^k a_{k,j}+\epsilon_j(b),\qquad
 a_{k,j}=\langle A\sin(2j\psi)B^k\rangle,
\]
\[
 |\epsilon_j|\le R_0=
 \frac{A_{\max}r^{33}}{1-r},
\]
\[
 |\epsilon'_j|\le R_1=
 A_{\max}r^{33}
 \left(\frac{33}{1-r}+\frac{r}{(1-r)^2}\right).
\]
后一个式子直接求和 \(\sum_{k\ge33}kr^k\)，因此是对 b 的导数界，未漏一个 r 因子。全区间一致绝对收敛也使逐项微分合法。实际有理数计算给
\[
 R_0<9.382\times10^{-16},\qquad
 R_1<3.150\times10^{-14}.
\]
这些展示界留了向外余量；完整产物保存的是验证过的 96-bit dyadic 上界。

### 不作角采样的准确矩

令 \(z=e^{2i\psi}\)，写 \(B^k=\sum_n\beta^{(k)}_n z^n\)。系数是实有理数且 \(\beta_{-n}=\beta_n\)。初值 \(\beta^{(0)}_0=1\)；递推为
\[
 \beta_n^{(k+1)}
 =\frac{d_2}{2}(\beta_{n-1}^{(k)}+\beta_{n+1}^{(k)})
 +\frac{d_4}{2}(\beta_{n-2}^{(k)}+\beta_{n+2}^{(k)}).
\]
准确常数项就是
\[
 a_{k,j}=\frac{d_2}{4}
       (\beta_{j-1}^{(k)}-\beta_{j+1}^{(k)})
       +\frac{d_4}{8}
       (\beta_{j-2}^{(k)}-\beta_{j+2}^{(k)}).
\]
全部 924 个矩（33 个幂 × 28 个 vertical mode）均用 BigInt 有理数计算。每个 j 的有限 b 多项式及导数转成 Bernstein 系数，凸包加上 R0/R1 给 Cj、Cj′ 的全 [0,1] 上界，不是 b 网格峰值。

源码另用 \(x=\cos2\psi\)、Chebyshev U 和精确 arcsine 矩
\[
 \langle x^{2n}\rangle=\binom{2n}{n}/4^n,\qquad
 \langle x^{2n+1}\rangle=0
\]
对前 20 个矩作独立重算。每一幂还精确检查 z=1 和 z=−1 两端的 Laurent 求值。

## 可直接乘保存系数的权重

产物对每个 j 记录：

\[
 w_{1,j}=|q|(2j)\frac{15}{8L}\,\overline C_j,
\]
\[
 w_{2,j}=|q|(2j)\left[
 \frac6{L^2}\overline C_j+
 \left(\frac{15}{8L}\right)^2\overline{C'_j}\right].
\]
因此，只要从同一物理五次场证出
\(y_j\ge\sup_s|\Delta Y_j|\)、\(y'_j\ge\sup_s|\Delta Y'_j|\)，就有
\[
 |\Delta H'_{\rm conv}|\le\sum_jw_{1,j}y_j,\qquad
 |\Delta H''_{\rm conv}|\le\sum_j(w_{2,j}y_j+w_{1,j}y'_j).
\]

几个有向外余量的展示界：

| 物理频率 m | w1 上界 | w2 上界 |
| --- | ---: | ---: |
| 2 | 0.007573 | 0.008000 |
| 4 | 0.002558 | 0.003791 |
| 12 | 0.000022968 | 0.000066103 |
| 24 | 1.816e−9 | 5.166e−9 |
| 40 | 5.062e−14 | 3.137e−13 |
| 48 | 2.445e−15 | 5.130e−14 |
| 56 | 2.816e−15 | 5.913e−14 |

最后几模主要受统一几何级数余项限制；表中不主张它们的真实 Fourier 系数等于这些上界。

## 已执行状态与使用限制

独立源 computations/strong_q096_convection_mean_exact.js，依赖同目录 strong_mean_homotopy_exact.js 的有理数类，并严格核依赖 SHA。命令：

    node computations/strong_q096_convection_mean_exact.js --out <fresh-result.json>

本次在 functions JavaScript isolate 实际完成纯有理数计算，约 67.503 秒。10 组门全部通过：r<1、每幂双端 Laurent 恒等、全部矩的统一 integrand 界、20 个独立 arcsine 矩、k=0 的前两模及其余模精确值、两个正余项，以及所有发表 dyadic cap 向外。记录了完整矩流与每行的 SHA；精确生成代码可重建全部矩。0 Node 物理 worker、0 RHS、0 BVP；Node CLI 尚未执行。

本条只支付共同角图的 convection 均值算子。当前没有 M24/M28 的实际系数差界；法向速度均值仍需完整 a/P/W/判别式域及其连续差证书。要在既有 full-V 区间 AD 之外改用“normal-only + 本权重”的组合，须写显式组件入口和 provenance，不能悄悄把原工具的 v 输入设成零后仍报告 full mean。

原有限角平均、Gauss 高度值与精确均值之间的误差、exact knot 连续性、有限场到精确解的误差、闭曲面族、D、reach 均没有在此条支付。MJS 和实际求解门没有变化。
