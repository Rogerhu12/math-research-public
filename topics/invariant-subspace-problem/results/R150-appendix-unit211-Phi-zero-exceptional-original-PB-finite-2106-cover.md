# Phi=0 的判别式零权支：原 PB 补图与至多 2106 个有序基点

数据保存说明（2026-11-28）：可重算载荷已按根规矩8/15从main移除，相关旧链接只定位既有历史；当前保留生成源、参数定义、run与SHA，原数学及执行身份不变。


日期：2026-11-27（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 1. 范围与结论

本结果在 R150 的原 unit211、LS、物理 $D\ne0$ 范围内，保留已经支付的全部原单位。取 $\Phi=0$ 的有序特殊权支
$$
b=1,\qquad c=\frac12,\qquad \ell=\frac32,\qquad
u=\frac{3+\rho}{2},\qquad Q=1-\rho^2.
$$
另一个有序权支 $b=\frac12,c=1$ 由原 B/C 交换覆盖。此前的
[R150-appendix-unit211-Phi-zero-rho-discriminant-zero-original-necessary-curve.md](R150-appendix-unit211-Phi-zero-rho-discriminant-zero-original-necessary-curve.md)
已经证明，这两个支覆盖 $\Phi$ 的 $\rho$ 二次式判别式为零的全部原点；本稿不加入新的权重假设。

在第一个有序图内，全部原解的不同基点 $(\rho,\lambda)$ 至多有 **2106 个**。每个基点的原 $T$ 至多有六个候选值。这个计数保留所有临时消元首项为零的纤维。

第二个有序图获得同样的界；不能无说明把两个有序图的并集仍按 2106 计数。本稿没有排空这些有限点，也没有证明整个 $\Phi=0$ 面为空。

## 2. 已支付的同一点六维表示

记
$$
A_2=2\lambda^2-2\lambda+1,\qquad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_2-T^2,\quad
s_n=\ell B_3-A_2T,\quad
K=\ell^2B_3-3\ell T A_2+2T^3,
$$
$$
S_n=s_n+(3-2\lambda)D,\qquad Z=u s_n-2TD.
$$
这里 $S_n=DS$，$Z=2(u-\ell)D\zeta$。原 $D,S,\zeta,u-\ell$ 均非零，因此
$$
U=D S_n Z
$$
是实际原点上的单位。本权支的原矩关系在去掉已付 $\rho^2$ 后恰为
$$
2K^2-D^3=0.
$$
它关于 $T$ 的六次首项是常数 $9$。在这个首一六维商中，所有乘法都按原矩关系约化，保持同一个 $T$。几何分母只用显名的 $D$ 与 $S_n Z$；不把商代数范数或消元主元当单位。

原始均值、N1、个别 N/P 的构造及同一点恢复，引用已经发布的
[R150-appendix-unit211-Phi-zero-exceptional-original-mean-unit-six-F26-curve.md](R150-appendix-unit211-Phi-zero-exceptional-original-mean-unit-six-F26-curve.md)
及其原值前缀。此次新增的是含个别 PB 的六行输入，不重复旧 NB 六行矩阵或旧均值 T 闭包的七个行列式。

## 3. 新的原 PB 六行和完整目标返回

本次实际选定的六行是
$$
E_1,\quad E_{B,\mathrm{even}},\quad E_{B,\mathrm{odd}},\quad
N_1,\quad P_{B,\mathrm{even}},\quad P_{B,\mathrm{odd}}.
$$
even/odd 是原 B/C 两个共轭值的系数；两个原值方程都存在，且原 $\rho\ne0$，故这两个系数同时为必要零式。没有从单个形式商值为零擅自拆成系数为零。

每行在 $(1,T,\ldots,T^5)$ 中表达，构成实际 $6\times6$ 多项式矩阵 $M$。用同一点单位目标 $U^6$ 的六列向量 $v$ 作 Cramer 返回。记
$$
\Delta_M=\det M,\qquad
\Delta_i=\det(M\text{ 的第 }i\text{ 行换成 }v).
$$
程序以精确 QQ Bareiss 除法逐次乘回，并检查全部六个坐标：
$$
\Delta_M v=\sum_{i=1}^{6}\Delta_i M_i.
$$
实际 $\Delta_M$ 的 $(\rho,\lambda)$ 双次数为 $(37,92)$，共 3534 项。七项 $\Delta_M,\Delta_1,\ldots,\Delta_6$ 的完整公共因子 $g$ 双次数为 $(2,42)$，共 86 项。每个除法都完整乘回。于是有全多项式恒等式
$$
\frac{\Delta_M}{g}v
 =\sum_{i=1}^{6}\frac{\Delta_i}{g}M_i.
$$
这个等式在临时主元、行列式或因子的零点仍成立；没有要求它们在原点非零。

随后只剥除与已经支付的原单位相交的最大公因子。日志中的 `u-1:2,Q:1,T0:1` 是这些公因子的来源标签及剥除次数，不表示整个同名多项式以这些次数整除。每个实际剥除因子都是对应原单位的因子，且整除逐次乘回。

由原六行均为零而 $U^6\ne0$，得到一个新的必要多项式
$$
C_{31,50}(\rho,\lambda)=0.
$$
它双次数为 $(31,50)$，总次数 81，共 1632 项。三变量原表示的规范摘要为
`6e8945eebcbf4bd3c3f9a1ecab5fd30e96af153e11e6976b02b3ac0e72d0ae94`；
删除恒为零的 $T$ 指数后，精确二变量有理式摘要为
`3d850765f6c9338aa8f79af2b5889582cf8d4f45fd81ad90f4743fb5bebd5f6c`。

完整系数作为可恢复压缩 JSON 保存，且源内完成了压缩、解压、重建与完整多项式相等检查。后续计算不需要重做本六行行列式。

## 4. 与已存 F26 的真实 QQ 互素

旧均值 T 闭包的实际精确因子 $F_{26,26}$ 已经保存于
[2026-11-27-unit211-Phi-zero-exceptional-F26-exact-input-8542.json](https://github.com/Rogerhu12/math-research-public/blob/3b9cda56dfa6a1ae9d4ca2a35fa81798a5f156c9/topics/invariant-subspace-problem/notes/2026-11-27-unit211-Phi-zero-exceptional-F26-exact-input-8542.json)。
它双次数 $(26,26)$，总次数 52，共 729 项，规范多项式摘要为
`9057238c5d37c8cd9f62f3f512dcff1f6d2e385cd6c0e39250a571713f0aaac7`。

本次读取这份已完成的原输入，核对载荷摘要后重建；没有重做旧七个行列式。实际精确 QQ 计算给出
$$
\gcd_{\mathbb Q[\rho,\lambda]}(F_{26,26},C_{31,50})=1.
$$
所以两曲线没有公共曲线分量。尤其不存在某个复数 $\lambda_0$，使两者同时作为 $\rho$ 多项式恒为零；否则 $\lambda-\lambda_0$ 会是复系数公共因子，取其有理共轭乘积便与 QQ 互素矛盾。

## 5. 固定 57 阶原结式给出 2106 个不同基点

先用有理常数把两多项式变成整数系数。第二项所乘尺度为
$$
63398675155279049532452634624,
$$
第一项的尺度为 $1$。这不改变复零点。始终按原 $\rho$ 次数 26、31 构造固定 $57\times57$ Sylvester 矩阵，记
$$
R(\lambda)=\operatorname{Res}_{\rho}(F_{26,26},C_{31,50}).
$$
精确 QQ 互素保证 $R\ne0$。完整最大权匹配及对偶界已经逐项验证：31 个第一类行的 $\lambda$ 权为 26，26 个第二类行的权为 50，全部列权为零。因此
$$
\deg_\lambda R\le31\cdot26+26\cdot50=2106.
$$

这里还须保留每个固定 $\lambda_0$ 处多个不同 $\rho$ 根，而不只计不同 $\lambda$。假该纤维有 $r$ 个不同公共有限根 $\rho_1,\ldots,\rho_r$。固定原 Sylvester 矩阵的每一行是某个 $\rho$ 单项式乘原多项式的系数行，故
$$
(1,\rho_i,\ldots,\rho_i^{56})^{\mathsf t}
$$
是其右核向量。因为两多项式不同时恒为零，$r\le31<57$；Vandermonde 子式说明这 $r$ 个向量线性无关。因此该矩阵在 $\lambda_0$ 的秩缺陷至少为 $r$。

对一元多项式矩阵，行列式在 $\lambda_0$ 的消失阶至少等于特化矩阵的秩缺陷：作常数可逆行列变换把特化矩阵化成秩标准形，剩余每个零行至少含一个 $\lambda-\lambda_0$ 因子。这给出
$$
r\le\operatorname{ord}_{\lambda_0}R.
$$
对全部有限 $\lambda_0$ 求和便得到不同有序基点总数至多 2106。原 $\rho$ 首项在某纤维降阶时，固定矩阵仍保留这些右核列；因此这一步不丢首项零纤维。

源码中另报告的粗 Bézout 上界 $52\cdot81=4212$ 是正确的，但被上面的固定原矩阵论证加强为 2106，无需再次执行计算。

## 6. 模返回的准确限度与执行凭据

同一固定原结式在 1009 的实际完整约化次数是 2033，摘要为
`f4505a726a6c2691ac52b92ec424160f7cc748d6a9b17751ce8b2f9f3f0eaa85`。
本次 QQ 上界是 2106，仍相差 73；因此本稿没有把 2033 宣称为 QQ 精确次数，没有支付 QQ 首项在 1009 为单位，也没有用模计算排空复根。全部模系数另随精确输入载荷保存，供真正的新局部输入继续使用。

原源：
[2026-11-27-unit211-Phi-zero-exceptional-original-PB-complement-Gauss-input-8542.py](../notes/2026-11-27-unit211-Phi-zero-exceptional-original-PB-complement-Gauss-input-8542.py)

- Git blob：`cba3fbbcf9e401c9279961ac1a1db86c7bd2a2e4`。
- SHA256：`642badf026786097e228b2c7abf9c4d6ffd7554fac179394cf21afa3fb2b3baf`。
- 实际 run/job：46017740050 / 140569106733。
- 实际来源提交：`9dd3ec317b52ebe2fc4a99e320796ba8ef3d6592`。
- 内层退出码 0；11.963439749 秒；61048 KiB。
- stdout：85145 字节；SHA256 `0cb059cce3acfcbe05293e70cc60031d0bb0df8207314938b641606dd4f75704`。
- 执行前真实 pull 的两份 README blob 未变化；本次原 QQ Bareiss 除法乘回 385 项，另完成全部六坐标恒等式和精确 QQ gcd。

精确新 core、固定原模结式及小凭据随本结果保存。后续应在这些实际原输入上处理剩余有限点，不能把有限覆盖或模次数缺口当作已完成整支排除。
