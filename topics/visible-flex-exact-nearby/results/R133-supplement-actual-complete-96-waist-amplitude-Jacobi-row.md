# R133 补篇：实际完整96模腰振幅 Jacobi 行及浮点 proposal 的全空间误差

2026-11-14。**已证明并实际执行。** 主报告完成12个严格有理区间门；
独立 inverse-Gram 消费完成2个严格门。所有计算只消费已经公开的最终
完整腰向量，当前不需要失联的径向分片，也不声称 finite head BVP 已运行。

固定最终 candidate SHA256 为
\(\mathtt{ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413}\)，
保留原整个 \(|\eta|\le10^{-9}\)。
输出包括96个 nonmean cosine 方向和独立 mean 方向；
所有 odd \(u\) 方向的幅度导数准确为零。
这些是原物理 \(C_4\) 幅度的导数，不是 moving Fourier 第一行。

## 1. 数据和准确 Jacobi 行

输入仍为
[原腰23门报告](../notes/2026-11-13-R133-final-waist-amplitude-chart-rational.json)
的准确 \(\alpha\)、全部33个 \(V_j\) 和真实 \(a_0\) 区间，
其 SHA256 为
\(\mathtt{8066f501acc87d42e7d58f30377680aaa317be500471fa71bcceef336fc9357b}\)。
由 \(a'(0)=0\)，
\[
 m=-a_0+\alpha V_0<0,\quad
 f=4\psi=\sum_{j=1}^{32}\frac{\alpha V_j}{jm}\sin jx,
 \qquad x=4\phi.
 \tag{A.1}
\]
令 \(z=e^{ix}\) 只是本节的 Laurent 形式变量，不是后文的 mean 方向。
记
\[
 p=if=\sum_{j=1}^{32}p_j(z^j-z^{-j}),\qquad
 p_j=\frac{\alpha V_j}{2jm},
 \quad
 \tau=-\alpha V_1/m\in(0,1),
\]
\[
 e^p=\sum_{n\in\mathbb Z}a_nz^n .
 \tag{A.2}
\]
全部 \(a_n\) 为实，且这里的 \(p_{\pm j}\) 具有准确反射符号。
所有实际 tiny \(V_j\) 仍按准确 dyadic 值保留。

真实幅度为 \({\cal A}=2m^{-1}\langle\cos(x+f)\rangle\)。
对 physical 未 normalized 的方向 \(\cos jx\)，准确导数为
\[
 \boxed{\quad
 d_j:=D{\cal A}(v)[\cos jx]
   =-\frac{a_{j-1}-a_{-j-1}}{jm^2},
             \quad 1\le j\le96 .\quad}                \tag{A.3}
\]
证明由
\(G_\perp=8m^{-2}I\sin(x+f)\) 和
\(\sin(x+f)\) 的 sine 幅度
\(a_{j-1}-a_{-j-1}\) 得出。
\(I\sin4j\phi=-\cos4j\phi/(4j)\)；
再与 \(\cos4j\phi\) 配对产生 \(1/2\)。
因此 (A.3) 是函数方向值，**不是**梯度的 cosine 幅度；
后者为 \(2d_j\)。

对独立常数方向 \(h_2=1\)，所有 nonmean \(V_j\) 固定，
\(p\) 只通过 \(m^{-1}\) 变化。准确有
\[
 \boxed{\quad
 d_0=D{\cal A}(v)[1]
 =-\frac2{m^2}
 \left(a_{-1}+\sum_{j\ne0}p_j a_{-j-1}\right).\quad}    \tag{A.4}
\]
这里求和遍历全部 \(j=\pm1,\ldots,\pm32\)，
\(p_{-j}=-p_j\)。这个 mean 列没有省略相位对 mean 的依赖。

## 2. 整个 Bessel 主相位与完整 higher phase

分离
\[
 p=-\frac{\tau}{2}(z-z^{-1})+p_\epsilon,\qquad
 p_\epsilon=\sum_{j=2}^{32}p_j(z^j-z^{-j}) .
\]
主相位的完整展开是
\[
 e^{-\tau(z-z^{-1})/2}=\sum_{n\in\mathbb Z}b_nz^n,
\]
\[
 b_n=(-1)^nJ_n(\tau)\quad(n\ge0),\qquad
 b_{-n}=J_n(\tau)\quad(n>0).
 \tag{A.5}
\]
没有截掉主相位的未知 Bessel 高阶系数。

对所有需要的 \(0\le n\le929\)，使用
\[
 J_n(\tau)=
 \sum_{\ell=0}^{32}(-1)^\ell
       \frac{(\tau/2)^{n+2\ell}}{\ell!(n+\ell)!}
                    +E_n .
\]
令 \(t_{n,33}\) 为第一个未保留项的正上界，
则完整余项满足
\[
 |E_n|\le
 \frac{t_{n,33}}
 {1-\tau_+^2/[4\cdot34(n+34)]}.                       \tag{A.6}
\]
所有分母实际严格为正。
\(0<\tau<1\) 使交错项严格递减且 \(J_n(\tau)>0\)；
源码只凭这个已证明的符号将区间下端与0相交，
不是将一个数值误差任意删除。

higher phase 使用完整多项式
\[
 E_\epsilon=\sum_{\ell=0}^{26}p_\epsilon^\ell/\ell!,
 \qquad \deg E_\epsilon\le832 .
\]
若 \(\epsilon=\|p_\epsilon\|_{A^0}\)，则
\[
 \|e^{p_\epsilon}-E_\epsilon\|_{A^0}
 \le\frac{\epsilon^{27}}{27!}
              \frac1{1-\epsilon/28}.                 \tag{A.7}
\]
全部 \(j=2,\ldots,32\) 及正负两号实际参与非循环卷积。
预算严格检查 \(\epsilon<3/500\)。
完整主相位 Wiener 范数小于 \(e^\tau<3\)，
所以每个卷积系数额外支付三倍 (A.7)。
这里的 \(e<3\) 也直接由其正项阶乘级数得到，不使用浮点指数。

为 (A.3)–(A.4)，只需实际 \(a_n\) 的
\(-97\le n\le95\) 区间；每个这样的系数完整计算
\[
 a_n=\sum_{\ell=-832}^{832}
       (E_\epsilon)_\ell b_{n-\ell}
                        +\text{完整 (A.7) 余项}.      \tag{A.8}
\]
故所需 Bessel 最大阶恰为 \(832+97=929\)。
该系数选择没有将整个 \(e^p\) 当作有限 Fourier 多项式。

## 3. 实际有向算术和完整结果格式

所有带符号区间采用公共准确分母 \(S=2^{384}\)。
乘积的四个端点乘法先以 BigInt 准确计算，再分别向下/向上除以 \(S\)。
卷积先完整累加整数乘积，最后一次向外除法；
每项除以 \(\ell!\) 的递推和每个 Bessel 项也保留有向舍入。
没有二进浮点四则运算、角 quadrature 或 finite-grid alias 假设。

[完整96行报告](../notes/2026-11-14-R133-final-waist-complete-96-amplitude-row-rational.json)
保存：

- \(\texttt{exact_interval_denominator}=2^{384}\)；
- 每个 \(\texttt{rows[j-1]}\) 的真实物理频率 \(4j\)；
- \(\texttt{exact_interval_numerator_at_scale}=[L_j,U_j]\)；
- 独立 mean 的
  \(\texttt{exact_mean_interval_numerator_at_scale}=[L_0,U_0]\)；
- 全部12个已执行门、完整输入及级数尾。

所以 native 的真正区间是 \([L_j/S,U_j/S]\)。
十进显示仅为向外可读副本，后续有理消费应使用完整整数。
主报告 SHA256 为
\[
 \mathtt{c99e3f6c7fd4975ee8fd1de26fadad7f4e42c6c379a861830d6fa419046b052e}.
\]

几个实际列的向外显示如下：
\[
\begin{array}{c|c}
\text{真实方向}&D{\cal A}\text{ 的严格包络}\\ \hline
1&
[-1.276023677907614220,\,-1.276023581674613252]\\
\cos4\phi&
[-.616995919304690416,\,-.616995883004055568]\\
\cos8\phi&
[.186404739735458090,\,.186404752752572028].
\end{array}                                                   \tag{A.9}
\]
所有其它94个列完整保存在同一报告中，未以“高频可忽略”代替。
主报告实际检查第一 cosine 列和 mean 列严格落在此前完整未知
Wiener 球证书内，核对了原物理角、符号和 \(1/2\) 配对归一。
当前的新窄区间只属于 actual centre；它们不自动扩到整个
\(10^{-6}\) 未知 Wiener 球。

## 4. finite proposal 与真实无限维行的整体误差

对 \(0\le j\le96\) 取准确区间中点
\[
             \bar d_j=\frac{L_j+U_j}{2S}.
\]
其半径为 \(r_j=(U_j-L_j)/(2S)\)。
在归一 \(L^2_\phi\) 下，
\[
 \|h_2\|_2^2=|h_{2,0}|^2+
                \frac12\sum_{j\ge1}|h_{2,j}^{\cos}|^2.
\]
所以完整 head 行到中点行的对偶误差不是简单的未加权欧氏范数，而是
\[
 \rho_{\rm head}
 =\sqrt{r_0^2+2\sum_{j=1}^{96}r_j^2}
       <5.533516587648167172124970\,10^{-8}.           \tag{A.10}
\]
独立有理 consumer 用 BigInt 向上整数平方根实际计算了这个式子。
它包括真实 mean 的权1和每个 nonmean 的 inverse-Gram 权2。

若 proposal 进一步变为 binary64 \(\widehat d_j\)，
明确要求每项按一次准确 Fraction 中点转换，或直接核
\[
             |\widehat d_j-\bar d_j|\le2^{-52}.
 \tag{A.11}
\]
所有97个实际值绝对值小于2；正常一次正确舍入满足这个保守界。
若用分子、分母各自先转浮点再相除，仍须独立核 (A.11)，不能免费套用。
该量化误差的完整对偶 norm 不超过
\[
               \sqrt{193}\,2^{-52}<14\,2^{-52}.
\]

此前
[完整高尾篇](R133-supplement-complete-waist-high-amplitude-tail-and-mean-return.md)
已在同一 fixed centre 上实际支付
\(\|P_{\ge97}G_\perp\|_2<10^{-42}\)。
因此将 proposal 的高列设为0后，其与真实**全空间**幅度行之差仍满足
\[
 \boxed{\quad
 \|D{\cal A}(v_0)-\widehat{\cal A}_{96}\|_{(L^2)^*}
 <5.533516898510614067168801\,10^{-8}<6\,10^{-8}.
 \quad}                                             \tag{A.12}
\]
这里没有把 finite midpoint 当成某个未经证明的 true target 参数点。
(A.12) 对整个原 \(\eta\) 区间成立，并支付全部未保留高输入。

[独立 proposal 误差报告](../notes/2026-11-14-R133-final-waist-96-proposal-error-rational.json)
的2门已实际执行。它明确没有读取一个尚不存在的 finite head proposal；
(A.11) 是后来实际 producer 必须核的输入合同。
实际 whole-body \(\Gamma\)、其诱导的 mean 回传与高输入通道，
仍保留原高尾篇 W.15–W.16 的完整额外项。

## 5. 完整 Gram 下的左伴随行，无须未认证 SVD 规范

对实际有限 head，全部腰奇条件是
\(h_{1,j}(0)=0,\ 1\le j\le96\)，
另保留唯一真实幅度行
\[
 d_0h_{2,0}+\sum_{j=1}^{96}d_jh_{2,j}=0 .
\]
相应 body Hilbert 密度 \(\psi\) 的 mean 权为1、其它权为 \(1/2\)。
因 \(d_1\ne0\)，完整左伴随约束准确等价于
\[
 \lambda_{\rm amp}=\frac{\psi_{2,1}}{2d_1},\qquad
 \psi_{2,0}-\frac{d_0}{2d_1}\psi_{2,1}=0,
\]
\[
 \psi_{2,j}-\frac{d_j}{d_1}\psi_{2,1}=0
                       \quad (2\le j\le96).
 \tag{A.13}
\]
奇 Dirichlet 的 real sine 幅度乘子为 \(\psi_{1,j}/2\)。
mean 式中的2不能丢失；它与 nonmean 比值式不同。

若实际 finite producer 用 \(\widehat d_j\)，则同样公式只定义明确的
proposal 条件；真实差由 (A.12) 及完整边界消费者支付。
若取原 normalized 幅度行 \({\cal A}/\alpha\)，还须同步转换该行及其
乘子。本报告自身全部使用 physical 未 normalized 的 \({\cal A}\)。

完整未知方向的高幅度梯度、独立 mean 及其 body 回传，均不能因
(A.13) 是有限列表而消失。
上述列只关闭实际头部矩阵的真实腰边界规范，不授整个 head 或 high 逆、
\(\nu\) Schur、far regular 匹配或闭曲面存在性。

## 6. 可重算材料

主程序：
[scripts/fourfold_codazzi_waist_96_amplitude_row.mjs](../scripts/fourfold_codazzi_waist_96_amplitude_row.mjs)。

独立 inverse-Gram 消费：
[scripts/fourfold_codazzi_waist_row_proposal_budget.mjs](../scripts/fourfold_codazzi_waist_row_proposal_budget.mjs)。

~~~sh
node scripts/fourfold_codazzi_waist_96_amplitude_row.mjs \
  --out NEW_ROW.json
node scripts/fourfold_codazzi_waist_row_proposal_budget.mjs \
  --row notes/2026-11-14-R133-final-waist-complete-96-amplitude-row-rational.json \
  --out NEW_PROPOSAL_BUDGET.json
~~~

当前同一主函数和同一消费函数已在可用 V8 中实际执行；
12门与2门全部通过。Node 包装保持相同数学运算，并拒绝覆盖旧报告。
没有据此声称运行失联环境中的 Python、原径向 solver 或真正全补逆。
