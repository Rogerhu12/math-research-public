# R812：六个原 CM 运输均为单位与 split 素数的未筛配对非零

日期：2026-11-15。状态：**固定六种代数情形已在本公开仓库 Actions 准确完成；所有 \(p\ge41,\ p\equiv5\pmod{12}\) 的原未筛交替卷积非零。** 原本原标签、Legendre 权和规范高度的共同条件仍开放。

依赖[R812 原源与五端项证明](R812-original-apolar-source-and-Gaussian-Frobenius-low-moment.md)和[公开执行约定](../notes/R812-fixed-six-case-public-execution.md)。保持原 \(c=0\) sigma、原 \(F,G\)、原CM点和theta相位；没有新增有限素数窗口。

## 1. 实际公开运行和完整 IO

- source：2b7183a313ddb04eb67bea37107830674511c49a。
- [run 43713181015](https://github.com/Rogerhu12/math-research-public/actions/runs/43713181015)，job132809012911；计算和原wrapper.verify均成功。
- 实际Sage10.6、Python3.12.5，固定执行镜像为 sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb。
- wrapper记录47.33628934699999秒，包含拉取镜像和计算过程，不冒称为纯Sage算术时间。
- artifact14161102406为5909B，SHA256 751c71f30bf8ba76ea4330a0169701371b74a8a186e8664ccacb6124fb496ce9，到期2026-11-16 12:19:34 UTC。
- 8个ZIP成员、6个完整manifest条目已逐大小/SHA核验；源码、proof/workflow/request及实际run/source一致。只做IO复核，没有再次运行数学。

原程序准确核过函数域平移、六阶阶数、Heisenberg相位、标准本征基、三个Frobenius自动同构的乘法性、六个FG条目和整数Norm。六个结果实际全部非零；启动条件没有要求它们非零。

## 2. 实际有限代数数据

记R812(812.44)的六个数为 \(a_{\epsilon,j}\)，
\(\epsilon=\pm1,\ j=0,1,2\)。固定整数幂基为
\[
\alpha^a i^b(\sqrt3)^c,\qquad
0\le a<3,\quad0\le b,c<2,\quad\alpha^3=4.
\]

| 对象 | 实际幂基清分母 | 清分母后整数Norm的完整素因子分解 |
|---|---:|---|
| 每个 \(a_{\epsilon,j}\)，共六个 | \(121=11^2\) | \(2^{38}3^{12}5^{12}11^{24}\) |
| \(\det\widehat U\) | \(1771561=11^6\) | \(2^{32}3^{78}11^{60}\) |

\(\widehat U\)所有条目的实际公共分母为
\[
88=2^3\cdot11.
\]
特征值1本征线的归一化选第0个分量，没有六个独立相位。

完整坐标和原证书是可重算raw，不放Git/Release；脚本、固定参数及实际来源足以重现。原文件身份如下：

| 原文件 | bytes | SHA256 |
|---|---:|---|
| R812-six-case-result.json | 4576 | e3724808b873ca5bc9b82f3714139b4f0bbf22563aa0dd73ac36623f05815f7e |
| core-receipt.json | 1187 | 2354aeaa8c4fc2d2a0f676540dd6cd0072a96d096e732588b04335a8bc606424 |
| full-outputs-manifest.json | 1826 | 3d7e98fbe759e1bede1cc0e3c19998496a286fc4db37ef48e75e80bd87e4a156 |
| public-actions-input.json | 1485 | e0188f7370577401fcd2b3c17c89e5c115cd574c2eee8e2944ffd3a356a38e92 |
| public-actions-run.log | 5195 | ed90d2c3f359530360a67dacc11b646089eeb76f9d8875d039c2c14c0a3953be |
| run-receipt.json | 549 | 37d1d7ba14e1fd32d43a28fe88cbcfa292b76a3b2b56c703a6bd349c34024189 |
| runtime-image-receipt.json | 420 | cfd3476c47117b3929d592f353facd5b0aa1c2357d1add78b090c7f3e6328907 |
| full-outputs-manifest-reference.json | 349 | 9992f093390b76927d443722c7d6345b0998561d4ffed7d8142c789f27598887 |

canonical JSON SHA256为4e5af466568479c01a58744ae004fb7a71b2f77998740fc96b876c7dac75937d；与带缩进原文件SHA的差异仅来自序列化格式，均已核对。

## 3. 全部 split 素数的原未筛单位定理

令
\[
p=6N+5\ge41,\quad p\equiv5\pmod{12},\qquad
F=x\sigma^6=z^4\sum f_i z^{6i},\quad
G=-xy\sigma^6=z\sum g_j z^{6j},
\]
只取R770/R812已证明整的first-p原截断。

**定理。** 有
\[
\boxed{\quad
\sum_{j=0}^{N-1}(-1)^j f_{N-1-j}g_j\ne0
\quad\text{于 }\mathbf F_p.
\quad}
\tag{812C.1}
\]
因此至少一个 \(0\le j<N\) 满足 \(f_{N-1-j}g_j\ne0\)。

**证明。** 固定任意所用 \(p\)-adic嵌入，沿R812同一level-six代数覆盖评价于原CM点。

六个 \(a_{\epsilon,j}\) 均以 \(11^2\) 在整数幂基中清分母，所得是代数整数；其完整非零Norm没有 \(p\ge41\) 因子。故每个清分母元素在每个位于 \(p\) 上的素点都是单位。分母也是单位，所以六个 \(a_{\epsilon,j}\) 全为单位。此处同时使用整性和Norm，未将裸Norm非零误当局部单位。

\(\widehat U\)的公共分母88及 \(\det\widehat U\) 的清分母/Norm只含2、3、11，故
\[
\widehat U\in\operatorname{GL}_6(\mathcal O_{\mathfrak p}).
\]
原 \(d_0^{12}=-432\) 为单位，而共同尺度准确满足
\[
c^6=-d_0^{-16}/\det\widehat U.
\]
在包含该尺度的每个选定有限扩张素点亦有 \(v(c)=0\)。所以
\(c^{2-2p}\) 是单位；没有将其任意设成1。

所选Gaussian素数 \(\pi=m+ni\) 满足
\(m^2+n^2=p\)、\(m+\iota n=0\pmod p\)。
两个整数 \(m,n\) 非零且绝对值小于 \(\sqrt p\)，所以 \(m\bmod p\ne0\)。
Gaussian单位归一至 \(\pi\bmod6=1+2\epsilon i\) 时，依R812同步运输特征和相位，落入已经算出的两个 \(\epsilon\)。
十二次CM域中的实际Frobenius满足
\[
i^p=i,\qquad(\sqrt3)^p=-\sqrt3,\qquad
\alpha^p=\zeta^j\alpha
\]
的三个 \(j\) 之一，故六case已覆盖全部实际嵌入类型。

R812(812.34)、(812.41)、(812.44)在原FG条目给
\[
Q_{FG}(P_0)
=-\iota m^5d_0^{p-1}c^{2-2p}a_{\epsilon,j}\ne0,
\tag{812C.2}
\]
因为 \(Q_{\rm part}(P_0)=0\)，且右边每个因子均为单位。
这是同一代数对象的SS评价，没有把 \(\lambda\) 或任意解析q参数当成SS单位。

最后，R812(812.7)的原规范准确给
\[
Q_{FG}(P_0)
=(6B)^5\sum_{j=0}^{N-1}(-1)^j f_{N-1-j}g_j.
\tag{812C.3}
\]
原 \(B=DA(P_0)\ne0\)，且 \(p>3\)。除以单位 \((6B)^5\) 得(812C.1)。
各系数原在 \(\mathbf F_p\)，故有限扩域中核出的非零就是原剩余域中的非零。
全部单项积若为零则总和为零，故得到所述存在性。证毕。

## 4. 关闭的缺口与仍需完成的筛后问题

本定理排除split分支中原 \(F/G\) 的全部临界反对角项同时为零。它是所有 \(p\ge41,\ p\equiv5\pmod{12}\) 的结论，依据覆盖全部Frobenius类型的固定有限代数计算，没有从素数样本外推。

R770仍要求同一个
\[
h=6a+1,\qquad (h,p+1)=1,\qquad
P_{6a}(1/\sqrt{-3})f_{a-1}g_{N-a}\ne0.
\]
(812C.1)的权是原交替符号，没有本原指示函数或Legendre因子。
尚不能证明见证标签满足本原性或可见性，不能把未筛单位写成三因子共同单位。
\(p\equiv11\pmod{12}\)的Gaussian惰性/Eichler分支亦未被本次计算覆盖。

原规范高度、有限Bézout排零与Serre一致性完成标准仍开放；继续真实筛后配对和正在运行的原函数/高度输入。
