# R150：W 的 lambda=3/2 整支四个十列原常数 cofactor 与四条权必要曲线

会话：Astra-ISP-8542378f-20261127。日期：2026-11-27。AI-assisted GPT-6 Astra Pro。

**状态：完整原必要结论已证明并实际返回。** 当前 W 图的每一个 lambda=3/2 原点，同时落在本页给出的四条权曲线上。四个固定十列矩阵的常数列余子式都已逐列乘回；没有倒置 A143、Ahat 或新的几何首项。尚未宣称四曲线交集为空，也未把多变量 gcd 用作判空。

## 1. 作用域、原坐标和两条已经支付首项的原式

作用域严格沿用[全图首一四二次定理](R150-appendix-unit211-W-global-monic-T-four-F-two-and-finite-original-environments.md)以及[实际八列原返回](R150-appendix-unit211-W-global-monic-four-two-eight-column-original-return.md)的当前原一般 LS、Delta=0、W=0 权局部环。本页不把那些使用原 D 非零条件的旧权排除外推到一般 hU=kU 碰撞。

置

$$u=e+1,\quad Q=ek,\quad V=uk+2,\quad d=1-Q,$$

$$\ell=\frac{u((k+2)^2-2ek)}{kV},\qquad m=u-\ell,\qquad
M=\ell^2d-m^2=4bcd.$$

原坐标仍为

$$F=2f-u\lambda,\qquad S=T-2\lambda.$$

现在只令 lambda=3/2，因此 T=S+3，而 e、k、F、S 均保持符号变量。源从原双点代数、原 Gram 矩阵重建 E0、N0、P1；先核仿射逆，再核所有均值、N1 以及 NS、PS 的原值迹。全部分母只来自既有权单位。没有从已选数值样本生成输入，也没有假设任何余式空间自由。

记 EBe、EBo 为原单点均值的共轭偶、奇系数。已经支付首项的原二次为

$$q_F=\frac{mEBe+\ell dEBo}{h_F},\qquad
h_F=\frac{u^2md\Phi}{eM}.$$

其 F² 系数实际为 1。保留原值定义

$$A=5/2,\quad B=7/2,\quad D=\ell A-T^2,\quad
K=\ell^2B-3\ell TA+2T^3.$$

用[两条原四次](R150-appendix-unit211-W-original-two-quartic-necessary-values.md)中的同点原组合，记

$$A_* =4uQ-J,\qquad C_*=A_*m^2+Jd\ell^2,$$

$$a_D=-3M\ell^2Q+MA_*T^2+C_*D,\qquad
b_D=2MmA_*T,$$

$$R_4=Ma_D^2-Db_D^2,\qquad
C_4=2mDa_D+Kb_D.$$

本纤维的首一 T 四次为

$$q_T=C_4/(8muQ\ell^2d).$$

分母全部已付。令

$$r_T=R_4-[S^4]R_4\cdot q_T.$$

源实际核出 qT 的 S⁴ 系数为 1，rT 的 S⁴ 与 S³ 系数都为 0。因此 rT 是一个对 S 至多二次、仍在原理想中的同点必要式；这一降次没有倒置任何新首项、D 或范数。

## 2. 固定原行及其准确正规化

在 QQ[e,k][F,S] 中取总次数不超过三的十个固定列

$$\mathcal B=(1,F,S,F^2,FS,S^2,F^3,F^2S,FS^2,S^3).$$

源对每个原式 p 先清除其已付权分母，再仅去掉各 F、S 系数共同拥有的已付权因子。记得到的多项式为 p帽。每次除法都乘回，并将 p帽重新嵌回原有理式以逐项检查

$$p=u_p\,\widehat p,\qquad u_p\in A^\times.$$

这里 A 是上述当前权局部环；未付的多项式内容不剥除。原分母与所剥内容的每个因子，都通过已有单位原子的逐次 gcd 整除核验。程序中的 gcd 只用于确认这些已经支付因子的来源，不用来判断多变量零点是否存在。

固定九行是

$$
\widehat q_F,\ F\widehat q_F,\ S\widehat q_F,\quad
\widehat E1,\ F\widehat E1,\ S\widehat E1,\quad
\widehat EBe,\ F\widehat EBe,\ S\widehat EBe.
$$

分别再附加下面四个原行之一：

$$\widehat N1,\quad\widehat{NS},\quad\widehat{PS},\quad\widehat r_T.$$

所得四个矩阵记为 B_N1、B_NS、B_PS、B_rT。它们均为固定 10×10 矩阵；前三个基础原式是二次，N1 与 rT 也至多二次，NS 与 PS 至多三次。因此上述列完整容纳每一行，没有截掉任何原系数。

NS、PS 是原两个单点 N、P 方程按同一 b、c 加权，再用同一原二阶、三阶值关系化简所得。源重新检查它们与完整个别原方程和 HA、HB 的准确恒等式。因此任一完整原解确实使四个矩阵的每一行都在同一 F、S 上取零；本页不反称这些必要行足以替代所有个别原方程。

## 3. 全部十列的实际原恒等式

对每个 B_v，源用无分式消元构造多项式行 c_v，并对十列分别实际核验

$$c_v B_v=(\det B_v,0,0,0,0,0,0,0,0,0).\tag{1}$$

反代时以实际 det Bv 缩放；所有中间除法都在 QQ[e,k] 中精确整除并乘回。最终 (1) 是多项式恒等式，并不把中间主元当作局部环单位。因此某个中间主元、某行的最高次系数或任意新参数因子为零时，(1) 仍在整个纤维成立。

每个实际原点有非零评价列

$$(1,F,S,F^2,FS,S^2,F^3,F^2S,FS^2,S^3)^{\mathsf T}.$$

将 (1) 作用到这个列上，就得到 det Bv=0。这里只使用首列恒为 1；没有把十列视为原商环的自由基底。

四个 det Bv 都实际非零。随后仅去已付权因子并作非零有理常数正规化，得到 Cv，且每步乘回给出

$$\det B_v=U_v C_v,\qquad U_v\in A^\times.\tag{2}$$

所以四个 Cv=0 都是全 lambda=3/2 原纤维的必要条件。

## 4. 四条实际必要曲线

原始 det 与只去已付因子后的 Cv 如下。次数顺序始终是 (e,k)。

| 附加原行 v | det 次数 | det 项数 | Cv 次数 | Cv 总次数 | Cv 项数 |
|---|---:|---:|---:|---:|---:|
| N1 | (66,106) | 4361 | (26,33) | 45 | 638 |
| NS | (72,112) | 5144 | (28,34) | 47 | 717 |
| PS | (73,112) | 5193 | (28,33) | 46 | 689 |
| rT | (68,105) | 4521 | (30,38) | 53 | 874 |

Cv 的完整定义为本页固定原行、固定列、(1)、(2) 以及冻结源的正规化算法；大系数不另存缓存。按源码的有序指数/有理系数 JSON 编码，其 SHA-256 为：

- C_N1：1df822932bb9b41b79e2a9fe8d757fc6b36b018a96dd23d8212f546644c1802d。
- C_NS：3ab1d726c4cf8f8e00c09eabe8c15f3c2474abf2da8159a202fe01a4b48d9fdf。
- C_PS：b651d55fb1846c78c6a6a107d25cb32d9b0f3cd7cd299af33a9d391ea4ec9115。
- C_rT：e35da6b3e3568ad6a08d9c2eae221eeef245e147484104c1523641083c23a9d0。

源的最终剥除实际只用 e、k、u、d、V、ell、M、Phi、P02、H 的因子；完整逐次记录在回执。该列表记录已付单位来源，不把一个复合单位的 gcd 一次整除误写成那个复合多项式的一次完整幂。

四份原余子式行的编码大小分别为 1,548,785、1,937,624、1,963,276、1,653,253 字节。它们均已实际全十列乘回，仅保存源码、定义、哈希和小回执；没有把这些可重算矩阵另存到仓库。

## 5. 与已有 F18 的衔接及准确剩余范围

[同值单一 F18 覆盖](R150-appendix-unit211-W-lambda-three-halves-same-value-single-F18-cover.md)已经给出每个原点满足

$$F_{18}(e,k)=0,\qquad
[e^{18}]F_{18}=9834496k^{10}(k+2)^6\in A^\times.$$

因此整支当前被以下五个必要权条件覆盖：

$$F_{18}=C_{N1}=C_{NS}=C_{PS}=C_{rT}=0.$$

本页没有执行这些曲线之间的 QQ 投影；没有从多变量 gcd、数值取样或模素数一般秩宣布其交集为空。A143、Ahat 的零集以及所有原最高次系数零纤维均保留在上述必要覆盖内。下一输入可以在 e 上作完整 QQ 结式，并在同一 k 上返回原有限纤维；这不需要重跑本次十列证书门。

## 6. 实际执行和再生材料

源：

[2026-11-27-unit211-W-lambda-three-halves-global-original-ten-column-weight-cofactors-8542.py](../notes/2026-11-27-unit211-W-lambda-three-halves-global-original-ten-column-weight-cofactors-8542.py)

源 SHA-256：

d8daeec98b4870b3672d7737afea8771bf5e48d747297859dbf9c3095b10810c。

实际 GitHub Actions run 46022218902、job 140584473133。内层退出码 0；源完成时间 53.729678385 秒，驱动墙钟 53.807276171 秒，峰值 RSS 72,976 KiB。四个完整原列身份、全部剥除乘回和最终完成标记均已出现。

stdout 为 15,038 字节，SHA-256：

736338cf66c831a8066d1e12f549c6d74f581ce8cae337834ce65ad3cba2c195。

本次真实 pull 时间为 2026-11-27 15:08:49.354524 UTC，读到提交 d2e6627a148c077c7f715401bc6bb65173e965e0；根 README 与本课题 README 的 git blob 均未变化。详细小回执见同名 -receipt.json。

本页只登记已经完成的全纤维必要曲线；不把尚未执行的新投影记成结果。
