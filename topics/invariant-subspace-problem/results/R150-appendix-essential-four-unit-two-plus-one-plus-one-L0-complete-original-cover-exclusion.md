# R150：unit 2+1+1 的整个原 L=0 分支排除

日期：2026-11-27（台北时间）。会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

**状态：已证明整个原 L=0 分支为空。** 本稿合并原退化图的完整排除、原 C/X 结式的精确3352次覆盖、九因子在特征零中的1535次整除，以及1817次余覆盖的原一元 Gauss 返回。结论仅涉及 R150 unit 2+1+1 原 U 值图的整个 L=0 分支；一般 LS、其余秩/本质支撑、Bell 自然幂及普通 ISP 均不由本条关闭。

## 1. 原图与已经支付的全部边界

从[原 U 值覆盖](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)接续。L=0 只可能在三值互异图中。零/相等相反 singleton 配对、零 mean、P0=0 及 u=1 等原边界均已在该覆盖及结果索引登记；剩余图可用公共尺度 p+q=2，并保留完整二次代数的全部嵌入。

记原双点第二坐标为 w，原值均值为 lambda。L=0 参数 rho 满足
$$A=2\lambda^2-2\lambda+1,\quad B=4\lambda^3-6\lambda^2+3\lambda-1,\quad R_0=\lambda-1-w,$$
$$u=R_0/\rho,\quad V_2=A/\rho^2,\quad Q=(2A\rho-B)/(\rho^2R_0),\quad \ell=(2u-V_2)/Q.$$
rho、R0、Q、1−Q、bc、P0 等分母来自原物理条件；A 可能为零，从未倒置。

原 w=0 支由 P 的平移不变性排除；[整个 w=1 支](R150-appendix-essential-four-unit-two-plus-one-plus-one-U-value-L0-w1-exclusion.md)及[整个 ell=b+c=0 支](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-zero-weight-sum-exclusion.md)已有原全纤维证明。余图的 W 曲线、P1 双系数零支及 G/K/V 曲线也均独立全闭，来源见[原完整已付 rho 首项系统](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-full-original-paid-rho-leading-system.md)。故原 P1 可唯一恢复同一个 t，原 rho 五次首项已经支付。

[X 的整个 lambda 首项零面](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-X-lambda-leading-complete-exclusion.md)已闭，包括 w=−1、w=−1/2 及 H7 的全部根。本稿不倒置其他未经支付的投影首项。

## 2. 同一个原 Gram 的必要曲线与完整投影

[原八列 cofactor](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-eight-by-eight-original-parameter-curve.md)和[附加原子式](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-three-additional-original-parameter-curves.md)给出 C、C8、C5。全部八列系数身份及原行组合实际回乘，保留消元主元为零的纤维。X 来自同一原 E1/N1 的完整 rho 结式，只剥已付因子。

| 原曲线 | (lambda,w) 次数 | SHA256 |
|---|---|---|
| C | (39,53) | 6057a487720992327d9e065ec6b7ef5e54896637f1c756a28391fd734737b50c |
| C8 | (39,54) | 16720813d546e77a4847da2ab9777eb6d009ced33085a7164e9e78909f14c36b |
| C5 | (40,53) | e794abe1f3c03c6cbda5fa7474b4a7d3a4e5b70e6996c0ee19dc3e5cbeb0cb05 |
| X | (34,52) | 519fe7c69a0cf7c05283aa66833331b64e7654bb6ec0daec606c49b2c2a02f68 |

剩余原解必须满足 C=X=C8=C5=0。定义完整 QQ 结式
$$R=\operatorname{Res}_{\lambda}(C,X),\quad S_8=\operatorname{Res}_{\lambda}(X,C_8),\quad S_5=\operatorname{Res}_{\lambda}(X,C_5).\tag{1}$$
分别使用原完整 lambda 次数39/34、34/39、34/40。每个有限 lambda 原共同根都使对应结式为零，即使特殊化后次数下降。只用原必要条件排空即可；不声称交点均能恢复原 rho/t。

## 3. 精确3352次覆盖及1009整性

[完整原 C/X 次数证书](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-CX-exact-degree-3352-cover.md)在原73阶 Sylvester 矩阵上作2233次 QQ[w] 行操作，逐项回乘163009条身份，证明 deg R≤3352。同一完整行列式的模1009次数为3352，故
$$\deg R=3352.\tag{2}$$
原 C/X 系数都属于局部整环 $D=\mathbb Z_{(1009)}$，原 lambda 次数约化保持。因此完整模结式等于 $\bar R$，而(2)说明 $c=\operatorname{lc}(R)$ 是 D 中单位，得到
$$R/c\in D[w]\quad\text{且首一。}\tag{3}$$
首项保持来自特征零上界和模下界相合，不是仅凭模次数推断；旧超时的大 QQ 结式、Groebner 门及 PRS 均没有被视作成功。

## 4. 九因子及1535次特征零整除

以下 J 均取右侧整系数多项式的首一化：
$$
\begin{aligned}
J_{2a}&\doteq2w^2+4w+3,&J_{2b}&\doteq2w^2+2w+1,\\
J_3&\doteq4w^3+4w^2-w-3,\\
J_6&\doteq56w^6+160w^5+150w^4+32w^3+4w^2+5w-2,\\
J_{10}&\doteq32w^{10}-192w^9+128w^8+920w^7-138w^6\\
&\qquad-1773w^5-1124w^4-255w^3-8w^2-23w+3.
\end{aligned}
$$

| 首一因子 phi | 次数 | QQ整除指数 t | 完整模R中的实际指数 | degree(phi^t) |
|---|---:|---:|---:|---:|
| w | 1 | 815 | 815 | 815 |
| w−1 | 1 | 203 | 203 | 203 |
| w+1 | 1 | 63 | 63 | 63 |
| w+1/2 | 1 | 41 | 41 | 41 |
| J2a | 2 | 107 | 107 | 214 |
| J2b | 2 | 36 | 36 | 72 |
| J3 | 3 | 5 | 5 | 15 |
| J6 | 6 | 12 | 12 | 72 |
| J10 | 10 | 4 | 4 | 40 |

九因子两两 QQ 扩展 Euclid 的36条身份都实际乘回为1；各因子首一且1009整。因此
$$Q_*=w^{815}(w-1)^{203}(w+1)^{63}(w+\tfrac12)^{41}J_{2a}^{107}J_{2b}^{36}J_3^5J_6^{12}J_{10}^4\tag{4}$$
满足 deg Q*=1535、Q*∈D[w] 且 Q*整除 R。模指数只提供上界核对；特征零整除均由下一节独立支付，不把模重建候选当作 QQ 因式分解，也不假设 J 不可约。

[五条固定 w 整曲线](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-five-fixed-w-curves-complete-exclusion.md)已经在整个 QQ 商代数中完成原返回，覆盖每个 J 的全部复根。合并第1节四个线性边界，剩余原解必有
$$Q_*(w)\ne0.\tag{5}$$

## 5. 原特征零整除证书的范围

### 5.1 固定次数变换与完整幂提取

始终把 C/X 作为次数39/34的二元齐次形式。五个 J 使用固定多项式平移并逐项逆平移。w 因子使用固定 SL2 变换
$$\lambda=r(w)+\frac{z}{1+s(w)z},$$
$$r(w)=\tfrac12+w-4w^2+28w^3-248w^4+\tfrac{60048}{25}w^5,\qquad s(w)=-6w+24w^2.$$
它由平移、反转、平移、反转组成，矩阵为 $\left(\begin{smallmatrix}1+rs&r\\s&1\end{smallmatrix}\right)$，行列式1，所以保持完整二元结式。源码保留40/35个系数位置并逐系数反变换回原式；没有倒置 1+sz 或删去无穷远纤维。w+1 直接使用原矩阵。

对所得73阶矩阵 M，固定整数权 u_i、v_j，并逐项准确验证 $v_\phi(M_{ij})\ge u_i+v_j$，同时在完整匹配上核验等号。写
$$M_{ij}=\phi^{u_i+v_j}M'_{ij},\qquad
\det M=\phi^E\det M',\quad E=\sum_i u_i+\sum_jv_j.\tag{6}$$
每个 M'ij 都是实际多项式。负权只作有理函数域中的行列记账；每项实际乘法或整除均回乘。初始 E 对 w、w+1、J2a、J2b、J3、J6、J10 分别是810、63、72、28、4、9、2。

### 5.2 商代数核行和准确截断

目标指数为 t 时固定总精度 T=t+1，保持
$$R\equiv\phi^E\det M\pmod{\phi^T}.\tag{7}$$
每项模 phi^(T−E) 取余的商、余式及原项都回乘。对 K=QQ[w]/(phi)，正规表示把模 phi 行乘法变为73deg(phi)阶 QQ 矩阵。实际 QQ 核向量回乘为零，返回 K 后再次核验全部73列。每个规范化逆均由整个商代数中的 QQ 扩展 Euclid 支付；不需要 phi 不可约。

选中 k 条核行，在其所选列上恰是单位阵。把标准多项式代表同时替换到对应行，P=I+N 满足 N²=0；按选中/其余行列分块为 $\left(\begin{smallmatrix}I&A\\0&I\end{smallmatrix}\right)$。故 det P=1、P^(-1)=I−N 都是 QQ[w] 真身份。源码还逐项执行逆行恢复，并非只在商代数中断言可逆。

新 k 行每项都准确含 phi，逐项相除后 E增加k。以新精度 T−E 再截断，(7)保持；达到 E=t 即证 phi^t整除R。没有倒置未知参数函数主元。

w−1、w+1/2 则用完整 QQ 常数行操作：在对应有理点取值后高斯消元，把同一有理行操作施于完整 QQ[w] 矩阵并回乘，再从全部零值行提取线性因子。分别提到203、41；没有截去多项式项或逆参数函数。

原 C/X 的来源由已发布自含 Gram/cofactor 源固定，原整合源的六项成功返回也重新构造了同一 C/X；其余三项独立成功源逐一核验相同多项式的完整SHA身份。依赖和再生入口见第8节，不需要另一个单进程把所有已完子证重跑成功。

## 6. 1817次余项的原投影 Bézout

由(2)—(4)，
$$A_*=\frac{R}{cQ_*}\in D[w],\qquad A_*\text{首一},\quad\deg A_*=1817.\tag{8}$$
整性由首一 Q* 的 D 上长除法给出。原解由 R=0、Q*≠0 满足 A*=0。

自含源从原 Gram 重建 C、X、C8、C5，计算完整原 lambda 结式的模1009约化：

| 完整投影 | 原/模lambda次数 | 模w次数 | 模多项式SHA256 |
|---|---|---:|---|
| R | 39/34 | 3352 | 948491aa967651a95f7085d59c90324791a766da60f38e79a56c5ce2f3a51e28 |
| S8 | 34/39 | 3386 | 843f350613e3183167fcc6c472c45df79cb1b8d775b192c04116e308997983c1 |
| S5 | 34/40 | 3366 | 16bec1a91b02eeaf131d396d7a9b00a94b57bdc2abcc77b848c0946dafb0b92b |

准确剥去(4)的全部幂并回乘，得到
$$\bar U=\bar R/\overline{Q_*}=\bar c\,\overline{A_*},\qquad\deg\bar U=1817.$$
其SHA256为 e929d368dce4e082b9d0796210c34c0ae57c3eaeec80b0e2c2f19887e1364770。实际扩展 Euclid 给
$$a_1\bar U+b_1\bar S_8=g_6,\qquad a_2g_6+b_2\bar S_5=1.\tag{9}$$
g6次数6，两组系数次数分别(3379,1810)、(3365,5)。两个乘积与和都实际计算；再完整回乘合并身份
$$\boxed{(a_2a_1)\bar U+(a_2b_1)\bar S_8+b_2\bar S_5=1.}\tag{10}$$
三系数次数为6744、5175、5，联合SHA256为 02c301855bdc79bc5ab8f57dca69c6e7fea77f47fe8b56f9342209eedad93efe。这是完整原一元投影的身份，不是多变量模空性判断。

## 7. Gauss 返回与整个原 L0 排除

若有剩余原解，其 w0 同时满足 A*(w0)=S8(w0)=S5(w0)=0。A*首一非零，所以 w0 为代数数。令 m∈QQ[w] 为其首一最小多项式。m整除A*；由 D 的整闭性或首一 Gauss 引理，m∈D[w]，约化后仍是正次数首一多项式。m还在QQ[w]中整除 S8、S5；因为m首一且S8/S5系数1009整，长除法给出对应商也在D[w]。

故 bar m 同时整除 bar A*、bar S8、bar S5，也整除 bar U=bar c·bar A*，与(10)矛盾。补图不存在原解。第1节已覆盖全部余下原退化纤维，遂得
$$\boxed{\text{R150 unit }2+1+1\text{ 的整个原 }L=0\text{ 分支为空。}}$$

证明以原必要条件排空结束，无须把结果式根反向恢复成原解；没有把有限覆盖、模支持、首项非零图或单个复嵌入冒充整个分支。

## 8. 自含源、实际回执与冻结失败

九因子证明由下列已经实际完成的子证合成。完整源及固定参数见[成功子证清单](../notes/2026-11-27-L0-successful-factor-certificate-sources-8542/MANIFEST.json)，不保存可再生的大系数数据。

| 子证 | 实际来源/返回 | 执行范围 |
|---|---|---|
| w815、w+1 63、J2a107、J2b36、J3 5、J6 12 | 源2894780f；[六项完整返回](../notes/2026-11-27-unit211-L0-nine-original-resultant-factors-certificate-8542.json) | 从原Gram重建C/X；这六项均已完成，后续J10终止不被误记为整份成功 |
| w−1 的203重 | [源6a60a75c](../notes/2026-11-27-L0-successful-factor-certificate-sources-8542/L0_sylvester_linear_phi_local_rows_8542.py)、[实际小回执](../notes/2026-11-27-L0-successful-factor-certificate-sources-8542/linear_w_minus_1_successful_execution.json) | exit0，83.724159秒，完整QQ取值矩阵最终满秩 |
| w+1/2 的41重 | 同一源6a60a75c、[实际小回执](../notes/2026-11-27-L0-successful-factor-certificate-sources-8542/linear_two_w_plus_1_successful_execution.json) | exit0，12.107687秒，完整QQ取值矩阵最终满秩 |
| J10 的4重 | [源554f90b4](../notes/2026-11-27-L0-successful-factor-certificate-sources-8542/L0_translated_native_QQ_kernel_phi_probe.py)、[实际小回执](../notes/2026-11-27-L0-successful-factor-certificate-sources-8542/J10_successful_execution.json) | exit0，20.782464秒，371644KiB；正规表示两轮各提一重 |

线性源的建议模指数202、33只是记录，不是停止条件；实际一直算到完整余矩阵满秩，得到203、41。J10源使用固定平移及同一完整73阶矩阵，2→3→4的每次核行和除法都回乘。其原代码按执行时字节保存；旧setup还读取但未用于核行证明的Y/附加曲线/单位输入，其精确身份也在清单说明，未把它们伪装成新的证明前提。

两两互素及乘积另由[自含源49acb43e](../notes/2026-11-27-unit211-L0-nine-factor-product-Bezout-8542.py)实际付36条QQ Bézout、degree1535、首一和1009整性；exit0，源内0.018527秒、25544KiB，[小回执](../notes/2026-11-27-unit211-L0-nine-factor-product-Bezout-execution-8542.json)。Q*系数SHA256为2815302d3c784772217a5a4512c43363db76bf4e799ec4ca69c83ede4a4bf51c。

首个整合源2894780f实际37.123049秒signal9，释放Gram版本e1e225e6也实际58.841581秒signal9；两者只有上述六因子返回，最终RSS/外部原因未知，准确源、执行和部分小回执已冻结。既有独立J10及两个线性子证仍然有效。本定理没有把这两次运行改标成功，也没有把额外整套复现设置为完成证明后的登记门槛。

轻量顺序进程再生便利源2026-11-27-unit211-L0-nine-original-resultant-factors-fresh-processes-8542.py已提供但**未执行**，不用于上述数学证书或实际运行声明。
1817次余覆盖：[自含源](../notes/2026-11-27-unit211-L0-degree1817-remainder-original-Gauss-return-8542.py)。

- 源SHA256：6eb17f287a9efb4f8fc4365099aa8d23c6026e5c32f6fb97fc082600c58b7d6c，22836字节。
- 实际exit0，墙钟74.373804秒，峰值RSS114492KiB，源内74.241199秒完成。
- 配置300秒、外310秒、4GiB。
- stdout32475字节，SHA256为83aea1edba629f467a7440c66505c50867d2491a103c2295bad2ca0901093e29。
- [实际小回执](../notes/2026-11-27-unit211-L0-degree1817-remainder-original-Gauss-execution-8542.json)。

九因子源只证明QQ整除；余覆盖源明确引用该整除及精确3352次定理。合成定理同时使用三份证书与全部原边界，范围才是整个L0。

原S0/Lt0已另行全闭。继续一般LS的原零行列式与一般图，以及open.md的其余独立接口；本条不是普通ISP的完成声明。

