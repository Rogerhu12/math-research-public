# R133 补篇：最终腰部完整 mean 列及其伴随初值

2026-11-14。**已证明并实际执行 8 个准确有理门，全部通过。**

这里支付
[精确 mean 消去篇 M.17](R133-supplement-exact-mean-elimination-full-adjoint-and-nu-Schur.md)
所需的实际腰 mean 列，而非再用 \(\|D\mathcal A\|<7/2\) 的绝对值替代它。
同一最终中心、原全 \(|\eta|\le10^{-9}\)、含全部未知 Fourier 尾的
\(10^{-6}\) Wiener 球上，
\[
 \boxed{
 -1.276033052468980174799328
 <D\mathcal A(v)[1]
 <-1.276014207147490866328027.}
 \tag{W.1}
\]
因此真正 mean 列有固定负号。这里的方向是常函数 \(1\)，不是第一非mean模，
也不是尚未认证的 \(\nu\) 响应；(W.1) 不宣称全参数 Schur 非零。

## 1. 完整已付输入

完全消费
[最终腰坐标证书](R133-supplement-final-waist-amplitude-coordinate-and-mean-Schur.md)
及其原 23 门完整 JSON：

- candidate SHA256：
  \(\mathtt{ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413}\)；
- 原腰报告 Git blob：
  \(\mathtt{e8dc86bb152522507a606ebaec75a3929990f66c}\)；
- 原腰报告 SHA256：
  \(\mathtt{8066f501acc87d42e7d58f30377680aaa317be500471fa71bcceef336fc9357b}\)。

报告中的全部准确 \(V_0,\ldots,V_{32}\) 都保留。
未知偶扰动满足
\[
 \|v-v_c\|_{\mathcal A^0}\le10^{-6},\qquad
 v_c=-a_0+\alpha\sum_{j=0}^{32}V_j\cos(4j\phi).
\]
mean 独立变化，整个未知无限尾进入该范数；不假设扰动仍是32模。
原 whole-parameter 界给 \(m=\langle v\rangle<0\)，
\[
\begin{aligned}
 1.068731819999993868&<-m<1.068733840999993869,\\
 0.910562946674295055&<\tau:=-v_1/m<0.910566539949655033.
\end{aligned}
\tag{W.2}
\]
本篇不读取失联环境中的径向大分片，亦不从端点推出全体区证书。

## 2. 常 mean 方向的准确导数

令 \(x=4\phi\)、\(f(x)=4I(v-m)/m\)。真实物理振幅为
\[
 \mathcal A(v)=\frac2m\langle\cos(x+f(x))\rangle.
\]
对常 mean 方向 \(h=1\)，
\(Dm[h]=1\)、\(Df[h]=-f/m\)，所以
\[
 D\mathcal A(v)[1]
 =\frac2{m^2}\left\langle
    -\cos(x+f)+f\sin(x+f)\right\rangle .
 \tag{W.3}
\]
这个常方向确实影响物理相位；不能仅微分 \(1/m\) 而漏掉第二项。

把完整相位分成
\[
 f=-\tau\sin x+\varepsilon_8(x)+e(x),\quad
 \varepsilon_8=\sum_{j=2}^{8}\frac{\alpha V_j}{jm}\sin(jx).
 \tag{W.4}
\]
这里 \(m\) 仍在整个 (W.2) 上变化。原完整 \(V_j\) 和未知球给
\[
 \|e\|_\infty
 \le\frac{\alpha\sum_{j=9}^{32}|V_j|/j+10^{-6}/2}{m_-}
 <0.000000468308419978908296 .
 \tag{W.5}
\]
未知第一模已经进入 \(\tau\)，未知 mean 已经进入 \(m_\pm\)；
其余全部未知频率按 \(1/j\le1/2\) 支付，未截断。

令 \(P=i\varepsilon_8\)、\(L=i(-\tau\sin x+\varepsilon_8)\)。
它们的 Laurent 系数为**实有理区间**。用
\[
 E_4=\sum_{k=0}^{4}\frac{P^k}{k!},\qquad
 H=(1+L)E_4                                           \tag{W.6}
\]
在完整 Laurent 系数中卷积，不循环卷回或删中间模。
最高支持为 \(|j|\le40\)。

对任意整数 \(n\)，准确恒等式
\[
 \left\langle e^{i(x-\tau\sin x)}e^{inx}\right\rangle
       =J_{n+1}(\tau)
\]
给出有限和
\[
 \left\langle-\cos(x-\tau\sin x+\varepsilon_8)
   +(-\tau\sin x+\varepsilon_8)
                 \sin(x-\tau\sin x+\varepsilon_8)\right\rangle
 =-\sum_n H_nJ_{n+1}(\tau)+E_{\exp}.
 \tag{W.7}
\]
若使用真实指数替代 \(E_4\)，等号无余项。
负阶采用 \(J_{-k}=(-1)^kJ_k\)。

每个 \(J_k\) 取完整绝对收敛级数的前16项，
余项沿原腰证明 A.11 的准确几何上界支付。最大阶为41；
全部级数尾的最大上界小于
\[
 2.6551346914926044\,10^{-38}.                           \tag{W.8}
\]
这个费用没有因为高阶项很小就被置零。

令 \(e_8\ge\|\varepsilon_8\|_\infty\)。
真实角上 Taylor 积分余项满足
\[
 |E_{\exp}|
 \le(1+\tau_++e_8)\frac{e_8^5}{5!}
 <5.770043605148739\,10^{-14}.
 \tag{W.9}
\]
这里使用 \(|e^{it}|=1\) 的真实积分余项，不需要未付复域。
对 \(F_x(t)=-\cos(x+t)+t\sin(x+t)\)，有
\(|F_x'(t)|\le2+|t|\)。因此 (W.5) 的其余全部相位费为
\[
 (2+\tau_++e_8)\|e\|_\infty+\frac12\|e\|_\infty^2.
 \tag{W.10}
\]
(W.9)–(W.10) 合计的真实 mean integrand 误差小于
\(0.000001365453655644017269\)。
把完整有理区间和这个费用代入 (W.3)，再同时消费 \(m_\pm\)，得到 (W.1)。
整个过程没有用浮点积分、库 Bessel 或有限角样本。

## 3. 对真正 adjoint/head 消费的作用

若保留腰振幅行的伴随乘子为 \(\lambda_{\rm amp}\)，原输出
\(b_4\) 只作用外端，则 mean 消去篇中
\[
 c_0=-\lambda_{\rm amp}D\mathcal A(v)[1],\qquad
 \mu_{\rm body}(0)=\lambda_{\rm amp}D\mathcal A(v)[1].
 \tag{W.11}
\]
(W.1) 可以直接给这个实际初值的有向区间；
不能为了省掉 mean adjoint 而取零。
从该初值沿真正 scalar Green 传播仍须付完整径向闭盒、非mean trial、
真实接口与全外 mean 乘子。

若有限代码使用 normalized \((U,V)\) 和振幅行 \(\mathcal A/\alpha\)，
由于 \(\partial_{V_0}v=\alpha\)，对应 \(V_0\) 列也准确等于 (W.3)；
不会额外漏掉或多乘一次 \(\alpha\)。

## 4. 实际执行

源：
[scripts/fourfold_codazzi_waist_mean_adjoint_column.mjs](../scripts/fourfold_codazzi_waist_mean_adjoint_column.mjs)；

完整报告：
[8 门有理预算](../notes/2026-11-14-R133-final-waist-mean-adjoint-column-rational.json)。

完整计算函数已经在当前 V8 执行，全部8门通过。
源包装核原腰报告 SHA 后重放相同函数，并拒绝覆盖既有输出。
Node 包装尚未在失联运行时执行；这里的实际执行方式是上述 V8。
完整体区逆、\(\nu\) Schur 和 far label 方程均未由此端点列自动闭合。
