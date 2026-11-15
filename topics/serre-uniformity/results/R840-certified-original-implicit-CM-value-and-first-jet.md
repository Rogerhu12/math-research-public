# R840：原 CM 值、一阶导数及有限点准确表达式已成

日期：2026-11-15。状态：**公开计算实际成功。** 原 $p=41$、原 $f_4$、原 $P_1=\phi(c_1)$ 的分母 $B_0$ 已有真实非零约化证书，原 $y(P_1)$ 与 $y'(P_1)$ 已取得来源完整的准确表达式和518位模坐标。准确展开有理坐标仍未认证；本次不把候选送入旧 R792 成功入口，也未计算原 $\eta$ 或规范高度。

## 1. 原对象、来源和此次新内容

所有原归一化保持不变：
$$
f_4:X_1\longrightarrow C/L,\qquad C:y^2=x^3+b,\qquad
\deg f_4=1206,\quad f_4(c_0)=O,\quad c_1=4424,\quad z=a-1.
\tag{840.1}
$$
$P_1$ 与 R837 的固定 $P_0$ 不混用。原
$L=\mathbf Q(b,\zeta)$、$s=1+2\zeta$、$s^2=-3$；
模计算使用原整基 $B_{\rm fld}^i s^j$，其中
$B_{\rm fld}=\lambda b$、$0\le i<7$、$j=0,1$。

本次只消费原已成518位关系方向、R790 的146个准确 P1 值/首 jet、R775 的原乘积 recipes 和 R786 原基身份。四组实际旧输入共176件，未增加 Dixon 位数，未重算原 Schur 块、原 CM 迹、q 展开或旧关系。原正权基的每个 M2 输入已经包含6724，五次尺度是 $82^{10}=13744803133596058624$，不再补乘。

数学依据：
[原单位选行与准确表达式](../notes/R787-original-unit-chart-exact-expressions-and-CM-value-consumer.md)，SHA256
8d5b58a5f6e9748805af3c032de1bae955543b1855535b6c51f0ca9cd6947820；
实际接线见
[原 CM 消费接口](../notes/R787-implicit-CM-value-consumer-interface.md)，SHA256
9d10a5480841671bc33bcd0bcc5e9f01d4bab81037b5d9afc2a45c55ed0f4e3b。

公开 [run 43773420733](https://github.com/Rogerhu12/math-research-public/actions/runs/43773420733)，job132994211824；
source c3bcfc0dbbcd3a045349ec4500886100851a0d84。
核心实际35.797080241秒完成，最终时刻2026-11-15T23:13:31.419838+00:00；
run exit0、error null，全部246数学阶段已完成。

## 2. 准确响应与实际非零分母

原单位选行证明固定原2420阶矩阵 $M$、原右端 $r$、原 free1186方向，定义
$$
\xi=M^{-1}r.
\tag{840.2}
$$
其完整129阶原关系由真正28维核与已成单位选行子式证明，不由本次模数值猜测。四个准确响应为
$$
A_j=\ell_{A_j}\xi,\qquad
B_j=c_{B_j}+\ell_{B_j}\xi,\qquad j=0,1.
\tag{840.3}
$$
这里 $\ell_{A_j}=(e_j,0)$，
$\ell_{B_j}=(0,(e_jZ)_{P_S})$，
$c_{B_j}=(e_jZ)_{1186}$。原 $Z$ 的 pivot 整数行已经带负号，本次直接使用，没有再取负；也没有另行展开 $ZC$。

新算术准确完成原五次乘积的双数值和一阶导数，以及 $e_0Z,e_1Z$。双数乘法为
$$
(v,d)(w,e)=(vw,dw+ve).
\tag{840.4}
$$
R790 的 $a+b\zeta$ 准确换为 $(a-b/2)+(b/2)s$，不更换 $z$ 或插入新的 slash 相位。原值、首 jet、乘积与 $Z$ 的组合在特征零用准确有理数完成；之后才与同一个518位关系方向收缩。

在原 $\ell=1000000753$ 的全部十四个指定分支，实际 $B_0$ 约化均非零。例如原 branch0 的值是584148539。每个分支的源坐标、$B_{\rm fld}$ 根和 $s$ 根均在同一个原 selection 中，不拼接不同单位图。因此准确有
$$
\boxed{B_0\ne0,\qquad y_0=\frac{A_0}{B_0}\in L,\qquad
y'_0=\frac{A_1B_0-A_0B_1}{B_0^2}\in L.}
\tag{840.5}
$$
任意一个真实非零约化已足以证明特征零 $B_0\ne0$；本次实际还给出了整十四维模环所需的全部单位。

这些是唯一的原特征零表达式。可等价写
$$
\Delta(\ell,c)=
\det\begin{pmatrix}M&r\\-\ell&c\end{pmatrix}
=\det M\,(c+\ell M^{-1}r),\qquad
y_0=\frac{\Delta(\ell_{A_0},0)}
{\Delta(\ell_{B_0},c_{B_0})}.
\tag{840.6}
$$
本次保存原选行、源文件、准确局部行与该 solve/响应 recipe；没有声称已展开 $M^{-1}$ 或伴随矩阵。

## 3. 518位模值的实际完整认证

整体模环为
$$
(\mathbf Z/\ell^{518}\mathbf Z)[B_{\rm fld},s]/
(P_{B_{\rm fld}},s^2+3).
\tag{840.7}
$$
原 selection 的十四分支评价逆已完成，本次直接消费。先从模 $\ell$ 的十四个非零分母值取得原环逆，再按精度
$$
1,2,4,8,16,32,64,128,256,512,518
$$
作标量 Newton 递推。每个完成精度均保存，并在全部十四个坐标核
$B_0 B_0^{-1}=1$；没有做新的大矩阵逆。

本次已经实际核过
$$
B_0y_0=A_0,\qquad
B_0^2y'_0=A_1B_0-A_0B_1
\quad\bmod \ell^{518}
\tag{840.8}
$$
的全部十四个坐标。它们给准确表达式(840.5)在同一原模环的真实值，不是从另一个任意模解拼出的点。

两组各十四个坐标的一次严格有理重构都返回候选。候选仍未通过原 $L$ 中准确 bordered determinant 零证或准确行空间乘回；完整原曲线方程或共轭相容也不能单独替代这种身份认证。因此以下状态保持区分：

| 状态 | 实际结果 |
|---|---|
| 原准确关系的有源单位 solve | 已定义且认证 |
| 原有限 $y_0,y'_0$ 的准确表达式 | 已取得 |
| 原518位 $y_0,y'_0$ 全十四模坐标 | 已计算并乘回 |
| 每组十四个有理重构候选 | 已产生，仍仅候选 |
| 原准确展开坐标 | 未认证 |
| 旧 R792 展开坐标成功 recipe | 未产生 |
| 原完整 $\beta$、$\eta$、高度 | 未由本次计算完成 |

## 4. 实际成果身份

| 对象 | bytes | SHA256 |
|---|---:|---|
| 最终证书 | 5768 | 5de210b5ebb2a8a7fefcc8799888a68353c9c2ac10725fafa239d2bd1082d20c |
| 完整 manifest，254项 | 37636 | be2a58b2c87b6a79cb406d4cd1ecb04347f56f301373953e809d3bff68612642 |
| manifest reference | 184 | 37f5868226ce228bf98e9aa81feeea3fef35f9c66ef6ee3807ae119ce1e92444 |
| 完整246阶段 manifest | 14995 | cf1f7e44df29216524585e1e14475b722eb94e3ed5754441204a07b44ff23fae |
| 原准确五次 CM 值/首 jet 索引 | 10694 | 455eaf217279f7cda39f57cfb0774f72caa1e24d36ad369f964d9eceaef389a5 |
| 准确 eZ 索引 | 3981 | acd7adb6ba2972829b3be41e128356031b55c0457f0db9e3b270015c60392e5e |
| 原 A 两响应 | 39897 | f11343cc0f4841a5b31365715e19247f0cb586df4103543e921bcfcd64a1ebdd |
| 原 B 两响应 | 39844 | f79d45ac570da69559a6530065ac58d6aec0a2ec012969ca52d8f41210503460 |
| 十四分支单位见证 | 2465 | 758f53d27bbf30041f07d94e96a64c53976e39170c1f2afc0a306435eaa1c05d |
| 原准确表达式 | 72708 | 21cc66ed9a40a856edea495080ef2e375aefea6c6f17d6c26741b85e2f174342 |
| 518位原 y 与首 jet | 39796 | bfe1624cc3514d1b9bbf2252d4e70846c999c5112225fe4a306889d2210d52e5 |
| 仅候选的坐标重构 | 6302 | 0be79ee2811881b0cbfe80a5fe71bf5dac0d9fdbeeb0631b69fa8e45596780f1 |
| 核心回执 | 474 | d73832811e4817afbaddb6919db3b062362485aaf7d8a3d50c6f38ac34403cb7 |
| 运行回执 | 458 | 398e2ca7ac82fc0bdb47cce6362589ce350c7426140d15261ef4e8de9ba90648 |

数学配置 SHA256：
2a3bd8cee0b9db0e645ecd94b2db8651d046ac67ea5134e31ead7e77f9ff7829。
公开核心41678 bytes/SHA
d0e94bee98802169b9e1dfec186143deda7745bf2cdad420e683a75eb1969ddc；
包装35071 bytes/SHA
12727d7c002872c293f3eff2f161016eadb248e9de4429a7c68987ad98bc1bc4；
工作流5505 bytes/SHA
5a83c270ef22a64857100993e2c67152c6c775e91205599bcb1d1e7b69d20516。

artifact14185198226：
serre-global-R787-implicit-CM-value-43773420733-1；
96435463 bytes，ZIP SHA256
0ae63e2c65f2f45ac759bc948ea57203b36e1645899ebe409c38f0d879c39d94；
到期2026-11-16T23:13:32Z。

最小载体 R787-implicit-CM-retained-inputs.tar.gz 为89842923 bytes/SHA
e28a33f30ffcfa532610da729704e243f32c546514c4a4b11ce7956b253c6d1b，
只保本次四组176个必要输入。原大 $F$ 行和 R781 Laurent 文件不在这个数值子集；准确表达式已绑定其原 manifest 与逐项身份。未来准确零证必须从仍活跃的原来源取回这些实际文件，不能说本小载体已物化原大矩阵。

结束后本地仅做纯 IO：253个非载体输出、manifest/reference共255件；11次 Range、6630417 bytes，实际小输出6507588 bytes。全部选文件 SHA、真实 source/run/core/final、246阶段来源及表达式/候选状态已读取核对；未重新执行任何数学，也未重复下载89.84MB载体。

## 5. 立即接续的原输入

既有 [R791](R791-certified-original-Hom-descent-and-eta-inputs.md) 的(791R.16)已经给原消根公式；[R792](R792-original-beta-composition-and-Galois-cube-root.md) 的指定实嵌入证明有限原点的 $y_0^2-b\ne0$，且原切向 $h_0\ne0$。本次真实 $B_0\ne0$ 补齐有限性后，可以直接以准确四响应和已成 $h_0$ 构造原 $\beta_C=f_4(c_1)$ 的有源表达式。该公式不再重复登记为新定理。

原下降同源 $v$、$\kappa v^\dagger v$、原共轭和三同源尺度继续保留；不能把所选椭圆点或任意同源原像替换为原抽象 $A$ 上的点。原 $\eta$ 还需要完整全局除子/Picard 输入，原高度保第二类周期、Poincaré 规范、非 $p$ 项和刚性化。此固定层成果不改变全 $p$ 主目标的完成标准。
