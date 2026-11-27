# R150：整条 K7 权曲线的原理想三次平方与完整规范有限界

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

## 1. 定理与准确范围

沿用一般 LS、$\Delta=0$、$W=0$ 的当前已付原物理域。这里是已经登记的互异单值、$D_{\rm phys}\ne0$ 图，不外推到 $\Phi=0$ 或 $h_U=k_U$ 碰撞图。令

$$
K_7(e,k)=12e^2k^2-ek^3+8ek^2-k^3-4k^2-16k-16.
$$

**定理。** 在整条 $K_7=0$ 原图上，用已经证明完整双向覆盖的参数 $m$，有

$$
C_3(m)^2\in (E_1,E_{Be},E_{Bo},N_1,N_S,P_S),
\qquad C_3(m)=m^3-4m^2-6m+18,
\tag{1}
$$

其中理想取在按既有原权单位局部化的 $\mathbb Q[m,x,y,t]$ 中。式 (1) 是实际六项原组合，不是只在 $\mathbb Q(m)$ 上得到的泛型单位。

因此不同允许权点至多 $3$ 个；相应原均值点至多 $18$ 个；恢复 $\rho$ 和完整个别值后，固定规范七坐标

$$
(e,k,\rho,x,y,t,\zeta)
\tag{2}
$$

的不同原点至多 $36$ 个。保全部重数时，准确有限商环境的长度分别至多 $6,36,72$。

本稿给完整必要覆盖和有限界，**尚未排除三次式的三个整共轭纤维，也未排空整个 W**。

## 2. 整条曲线的参数与所有分母

[整 K7 参数定理](R150-appendix-unit211-W-entire-K7-rational-parameter-and-original-rho-cover.md)已证明

$$
A=m^2-6m+6,\quad B=m^2-4m+6,\quad
C=m^3-10m^2+36m-36,
$$

$$
k=\frac{2A}{m},\qquad e=\frac C{6A},\qquad
u=e+1,\quad Q=ek=\frac C{3m},\quad V=uk+2=\frac B3.
\tag{3}
$$

反向为

$$
\theta=\frac{24ke+k(8-k)}{k+4},\qquad
m=\frac{\theta+k+12}{4},\qquad
m^{-1}=\frac{k+12-\theta}{24}.
\tag{4}
$$

实际原身份是

$$
\theta^2=(k+12)^2-96,\qquad
A=\frac{km}{2},\qquad B=\frac{(k+4)m}{2}.
$$

故 $m,A,B$ 的逆由既有 $k(k+4)\ne0$ 和完整参数身份支付。没有删除判别式零点；共轭 $\theta\mapsto-\theta$ 对应 $m\mapsto6/m$，两支始终同等保留。每个有限当前原权点都给有限的 $m$，$m=0$ 和无穷远没有漏下另一原图。

本次只把原权单位逐一拉回这个整参数环。准确清单为

$$
m,A,B,\ e,k,u,Q,1-Q,V,\Phi,P_{02},bc,\ k+1,k+2,
$$

$$
H,\ 2e+1,\ \ell,\ell-u,Q-2,u-Q,T_0,J-Q,C_9,J_{19},D_{27},G_{36}.
\tag{5}
$$

这里 $H=4ek-k^2-4k-8$。每个量都是原有单位，所有拉回有理分母实际核为 $m,A,B$ 支持；没有从范数非零反推单支单位。

尤其 $C_9$ 和 $G_{36}$ 引用它们的**整原曲线排除**：

- [整 C9 排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-C9-complete-original-exclusion.md)，包括整二次扩张、156 次覆盖和全部低范数分支。
- [整 G36 排除](R150-appendix-unit211-W-G36-entire-original-exclusion-and-global-F-recovery.md)，包括完整 1198 次覆盖的高、低和最后两整纤维。

不是把早期两个泛型开图的条件改称全域单位。$J_{19}$、$D_{27}$ 同样沿用已发表完整零支结果。

## 3. 从同一原 Gram 直接建立新的单参数输入

原六式的定义与[完整原 C9 定理](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-C9-complete-original-exclusion.md)第 3 节相同；本次在构造 Gram **以前**代入 (3)，而不是再次求解旧双参数矩阵。

令 $\rho^2=1-Q$、$p=1+\rho$、$q=1-\rho$，

$$
b=\frac\ell2+\frac{u-\ell}{2(1-Q)}\rho,\qquad
c=\frac\ell2-\frac{u-\ell}{2(1-Q)}\rho,\qquad
X=x+y\rho,\quad Y=x-y\rho.
$$

$f,\lambda,T$ 仍由原 $E_0,N_0,P_1$ 的已付线性恢复给出。四条二次为原 $E_1,E_{Be},E_{Bo},N_1$，两条三次为加权原 $N_S,P_S$。源码从原迹乘法重建它们，完整核回 $E_0,N_0,P_1$、原均值、原极化 $N_1$，以及 $HA/HB$ 与加权个别 $N/P$ 的准确关系。

仅清 (5) 分母和 (5) 支持的公共内容后，六式的参数次数及项数实际为：

| 原式 | $m$ 次数 | 项数 |
|---|---:|---:|
| $E_1$ | 15 | 101 |
| $E_{Be}$ | 10 | 78 |
| $E_{Bo}$ | 10 | 72 |
| $N_1$ | 18 | 154 |
| $N_S$ | 25 | 415 |
| $P_S$ | 25 | 416 |

原四二次头以及所选两三次 overlap 头，在新整参数环中逐因子核由 (5) 支付。其实际首一规则给

$$
\mathcal B=(1,x,y,t,y^2,yt)^T.
\tag{6}
$$

所有六条原组合、三个变量乘六个单项式的 18 条真乘法、以及其中全部分母，均实际回乘。这里仅称六生成元，未假设自由基底或各乘法矩阵在自由模上交换。

## 4. 十六个真实原行与两个固定常数余子式

在 (6) 上实际建立 $S_i\in\mathbb Q[m]^6$，并保存六项原组合 $\tau_i$：

$$
S_i\mathcal B=\sum_{j=0}^5\tau_{ij}F_j,\qquad
(F_0,\ldots,F_5)=(E_1,E_{Be},E_{Bo},N_1,N_S,P_S).
\tag{7}
$$

输入行依次是 $N_S,P_S$、未用的第 1、3 个原 overlap、$yN_S,tN_S,yP_S,tP_S$，再加三个真实乘法交换子在 (6) 上的八个非零行。行 $0,\ldots,15$ 的实际 $m$ 次数为

$$
40,40,33,31,51,55,51,55,39,40,33,31,39,42,39,40.
\tag{8}
$$

每个交换子只作用于实际非零列 $\mathcal B$；它是原组合，不是把形式上的六列视为自由而强迫整个交换子矩阵为零。

在 $\mathbb Q(m)$ 中挑出独立原行只用于确定索引。最终选

$$
B_0=(S_0,S_1,S_2,S_3,S_4,S_5)^T,\qquad
B_1=(S_6,S_1,S_2,S_3,S_4,S_5)^T.
\tag{9}
$$

两个矩阵都在 $\mathbb Q[m]$ 中。所有固定行列式按多项式 Bareiss 恒等式求值，每次整除实际乘回；$B_0$ 的两侧伴随矩阵乘积共 72 项以及每个常数列余子式的六项乘积均核回。因此中间任何计算主元的零点都未被删除。

第一个完整行列式 $\det B_0$ 的次数为 242，升序 QQ 系数编码 43270 字节、SHA256

227825165445928be2c881acd6e381885bb76f3f809307433eb00d65377845d7。

剥掉且仅剥掉 (5) 所支持的因子后，第一个首一残式 $p_0$ 次数为 107，9890 字节、SHA256

116b0ea61acae8c24638e26cf55937e2f24b8906c21eb0274e5d941ffee3384a。

对 $B_1$ 同样清除已付因子得到 $p_1$。二者的精确定义是 (7)–(9) 和源码中的固定 paid stripping，不依赖另存大型系数。

## 5. 实际 Bézout 与原理想返回

源码实际求得一元 QQ Bézout 身份

$$
a(m)p_0(m)+b(m)p_1(m)
=m^6-8m^5+4m^4+84m^3-108m^2-216m+324
=C_3(m)^2.
\tag{10}
$$

全部未选行（包含第 6 行）的行向量乘 $\operatorname{adj}(B_0)$ 给出相应替换余子式；源码继续作完整 QQ gcd/Bézout 检查，gcd 不再下降，最终仍为 (10)。实际完整 QQ 因式乘回只有三次因子 $C_3$，重数为 2。

将两固定常数列余子式、(7) 中的真实原组合和 (10) 合并，源码最终形成六个有理多项式 $T_j(m,x,y,t)$，其分母全由 (5) 支持，并实际核回

$$
\sum_{j=0}^5T_jF_j=C_3(m)^2.
\tag{11}
$$

完整运算总计 1605 项 Bareiss 整除乘积。六项最终原迹的规范编码为 41158202 字节，SHA256

ff723c0603dbaef47653115020b6e39383e5c58a2c3d74a62a59b8ea90600390。

该 41 MB 可重算输出没有保存或传送；保留完整源码、(3)、(7)–(10) 的参数定义、实际运行号和小回执即可精确再生。结论不依赖保存大证书，也不以重新运行这次成功门作为后续登记条件。

## 6. 非约化有限商及完整规范点数

$C_3$ 的判别式为 $5076\ne0$，故不同允许 $m$ 至多 3 个。双向参数 (3)–(4) 给不同 $(e,k)$ 至多 3 个。

式 (11) 的**平方确实属于原理想**，因此在保重数时可取权环境

$$
A_0=\mathbb Q[m]/(C_3^2),
\qquad \dim_{\mathbb Q}A_0=6.
$$

对已付权量局部化只删除这个 Artin 环的分量，不增加长度。由 (6)，原均值代数是相应权环境上至多六生成的商，故其 QQ 长度至多 $36$。

加入首一 $\rho^2-(1-Q)$ 至多乘 2。个别值不需要再增加一个独立二次选择。记

$$
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,\quad
D=\ell A_2-T^2,
$$

$$
K_{\rm val}=\ell^2B_3-3\ell T A_2+2T^3,\quad
s=\frac{\ell\zeta-T}{u},\quad
M=\ell^2(1-Q)-(u-\ell)^2.
$$

完整两原矩等式给准确身份

$$
u^2(Ms^2-D)=\ell HA,
$$

$$
u^2\bigl(K_{\rm val}-2(u-\ell)Ds\bigr)
=\ell T\,HA+\ell^2HB.
\tag{12}
$$

当前原图的 $\ell,u-\ell,D$ 已付，所以在 $HA=HB=0$ 下

$$
\zeta=\frac{T+uK_{\rm val}/(2(u-\ell)D)}{\ell}
\tag{13}
$$

处处唯一。其余 Gram 和 $h_U,k_U$ 均由同一已刊规范恢复给出。因而固定完整规范原商的长度至多 $72$。包括物理 $D$ 在内的后续几何局部化发生在有限 Artin 代数中，只删除分量，不增加长度。

若只数不同复点，每个 $m$ 的均值纤维由六个单项式生成，故至多 6 点；$\rho$ 至多 2 选而 $\zeta$ 唯一，给

$$
3\cdot6\cdot2=36
$$

这一完整规范不同点界。这里没有把必要式的解全称为原解，也没有对未规范化矩阵、基变换或缩放轨道给点数界。

## 7. 源、真实运行与下一完整原返回

源：

[2026-11-28-unit211-W-entire-K7-rational-original-six-column-cofactor-return-8542.py](../notes/2026-11-28-unit211-W-entire-K7-rational-original-six-column-cofactor-return-8542.py)

小回执：

[2026-11-28-unit211-W-entire-K7-rational-original-six-column-cofactor-return-receipt-8542.json](../notes/2026-11-28-unit211-W-entire-K7-rational-original-six-column-cofactor-return-receipt-8542.json)

源 Git blob：85bc58c0b57c8e6250c1cc82c7521bcebfd35a5b，17866 字节，SHA256：

0f9413d3cee49a1feacf46992cfbefd91c3c3f1ff41e1954cd0bd9795b2e78bf。

唯一依赖为已刊原 C9 源，完整 SHA256 为 10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1。仅取原 Gram 定义 6015 字节和六规则构造 8441 字节，**代入新的整 $m$ 曲线后**构造；没有执行旧双参数余子式、旧投影或旧失败门。

真实 Actions：run 46075250765 / job 140761370773；source commit bd359ea13859b221a4add6695addf5dc7c6eaf46。源最终数学标记在 148.719700691 秒；驱动 148.816322780 秒、峰值子进程 RSS 242692 KiB、内层 exit 0。上限 180 秒、4 GiB。

stdout 8129 字节，SHA256：

7c285e3acb1815c82d81e69e92b51f50931c13b4373e73ea5cb46533ccd4b3c2。

真实 pull 在 2026-11-27 22:13:20.282297 UTC，从 bd359ea13859b221a4add6695addf5dc7c6eaf46 到 bf5f7e9708e3438b3c4f0435e1c908b0f95f933a；根和课题 README 均无差异。

后续准确输入是整个 $\mathbb Q[m]/(C_3)$ 上的同点原值与原 Gram 返回，保所有共轭嵌入和实际非单位分量。不得只挑一个数值根，也不需重算已完成的 242 次余子式或 107 次 Bézout。
