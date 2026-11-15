# R150 附录：原自然无穷远的十三个原始核与同一删输出投影的特征零长度 2

作者：Astra-ISP-789f / normal_annihilator。AI-assisted，GPT-6 Astra Pro。

## 1. 已完成结论

对既有原自然无穷远矩阵 $A^\infty(u)$，保持全部 $6188$ 个来源、$4367$ 个输出以及同一所选原输出集合 $I$。本次实际构造了完整十三维形式左核的一组原始基 $K(u)$，并得到

$$
\boxed{\lambda_{I,\mathbb Q}
=\operatorname{ord}_u\det K(u)[I^c,:]=2.}
$$

投影矩阵有十二个单位因子，唯一正指数为 $2$。这是一条真实的特征零结论，不是把有限域投影阶 $2$ 直接提升。

此外，全部归一化核条目都实际具有 $31$ 整系数、分母常项为 $31$ 单位的有理函数表示。因此同一 $K$ 也是
$\mathbb Z_{(31)}[[u]]$ 上的完整原始核基，并且其约模 $31$ 正是已完成有限域计算中的同一自由坐标归一基。

实际执行见
[原始小回执](../notes/r150-local-projection-session-789f/43736746064-original-characteristic-zero-free13-projection.json)，运行信息为：

| 项目 | 实际值 |
|---|---|
| run | 43736746064 |
| step | original-characteristic-zero-free13-projection |
| execution source | 8435a0f0958e1a61cd4d8093b243c73dddc29c78 |
| 数学时间 | 2.917069073 秒 |
| 外墙时间 | 3.073175079 秒 |
| exit code | 0 |
| 原临时回执 | 42557 B |
| 原临时回执 SHA256 | 6a987dbf91f27415ff81a075a01e94077b89b55cd822c93eb01a43c55a3db18d |
| 完整数学绑定 | bbd233b88adb5027bab3402aefe8c0116070aa99d8df55ea17cfe9289f32cda2 |

主线保存的外层小回执为 $52012$ B、SHA256
`2057846f5adb75ed84f20a144f4cb2da436f9b1db5674612ac376f9b4b503248`。
它与上表的原临时回执是两份明确不同的审计对象。

本条没有计算完整特征零无穷远 Smith 谱，也没有证明原所选大子式的最高系数是 $31$ 的单位。

## 2. 原自然图、原行比例及全部坐标运输

固定原自然参数 $u=1/s$，其方程是

$$
N^\infty(u,m)=Q(m)+u^{10}L(1/u)m,\qquad
\Gamma^\infty(u,m)=u^5\Gamma(1/u,m).
$$

这里的 $u$ 权定义原自然齐次图，不是从裸矩阵 $A(1/u)$ 出发的单位缩放。

在该自然图内部，使用真正的反转核 $K_\infty=R_6KR_6$、十一矩变量的常数反转以及原十一条 $N$/六条 $\Gamma$ 的相应常数行置换。之后做完整 co-moving 变换

$$
m_i^{\rm old}
=\sum_{j=0}^{10-i}\binom{10-i}{j}u^{10-i-j}z_j,
\qquad c=z_0,\quad d=z_1.
$$

反转与二项式平移都为多项式单位变换，在全部次数至多三的来源乘子与输出次数一至五的原空间上仍为单位。

本次由原 $K_\infty,J_2,J_3$ 重建全部物理方程的自然参数多项式，再与原 primitive 整方程逐条匹配唯一的非零**常数**比例。全部 $4433$ 个原参数系数及十七条完整多项式身份实际通过；没有用点值、旧行名称或未经核验的比例替代。

实际输入的原 primitive gzip 为 $65159$ B，SHA256 为

`44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe`，

解压 SHA256 为

`fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3`。

本次物理重建的实际 $J_2,J_3$ 哈希以及十七个完整行比例均保存在小回执中，所有原固定行比例均为 $31$ 的单位。

## 3. 真正的九维原线性块与三个有理函数核

在 co-moving 方程 $F_e$ 中记

$$
H_{ej}=[z_j]F_e,\quad
C_{ej}=[cz_j]F_e,\quad
D_{ej}=[dz_j]F_e,\quad
q_e=[d^2]F_e,\qquad 2\le j\le10.
$$

原九列线性块 $H$ 是 $17\times9$ 的完整多项式矩阵。本次分数无关选行实际得到零基原方程行

$$
(10,9,8,7,6,5,4,3,2).
$$

相应九阶原多项式块的行列式非零。通过精确 Bareiss–Montante 逆与全部 $81$ 个原块产品检查，构造

$$
Hr=-q,\qquad Hr_c=-Cr,\qquad Hr_d=-Dr.
$$

三个等式均在全部十七原方程行上精确乘回。

采用[原泛参数十三核定理](R150-appendix-rank-one-mean-generic-complete-critical-classification-and-finite-exception-set.md)中的泛函。十个纯泛函取出

$$
c,c^2,\ldots,c^5,\qquad d,cd,\ldots,c^4d.
$$

另外三个的非零支撑为

$$
\begin{aligned}
&\varphi_2(d^2)=1,\quad \varphi_2(z_j)=r_j,\\
&\varphi_c(cd^2)=1,\quad
\varphi_c(cz_j)=r_j,\quad \varphi_c(z_j)=(r_c)_j,\\
&\varphi_d(d^3)=1,\quad
\varphi_d(dz_j)=r_j,\quad \varphi_d(z_j)=(r_d)_j.
\end{aligned}
$$

本次实际构造这些有理函数。其在 co-moving 输出空间中的完整支撑含 $20$ 个纯单项式及 $135$ 个一次横向单项式；其他输出坐标严格为零。

## 4. 同一原自由块、完整乘回与原始性

使用已完成 full/G 计算的同一零基原输出字典：

$$
F=(3001,3002,4002,4003,4288,4289,4353,4354,4355,4363,4364,4365,4366),
$$

$$
I^c=(3001,3002,4002,4003,4288,4289,4354,4355,4362,4363,4364,4365,4366).
$$

程序由既成实际回执读取并核对这两个集合，连同全部十三个被删原输出的单项式 key。将十三个泛型核在 $F$ 上的真实有理函数矩阵求逆，并整体运输到原自由归一，实际验证了

$$
K[F,:]=I_{13}
$$

的全部 $169$ 个坐标。

全部 $155\times13$ 个 co-moving 有理函数条目约成互素分子、分母后，实际均在 $u=0$ 正则；极点列表为空。清除每列的一个 $u$ 单位分母之后，对原十七式乘全部 $364$ 个次数至多三的 co-moving 单项式，执行了

$$
6188\times13=80444
$$

个精确多项式产品检查，全部为零。

由于此来源基是完整原来源基的多项式单位变换，这些身份确实证明原 $A^\infty(u)^T K=0$。回执保留
`directUntransformed6188PolynomialMultiplicationPerformed=false`：
它没有把经单位运输的完整原身份冒称另一次未变换大矩阵直接相乘。

随后全部 $4367\times13$ 原输出坐标均实际运输并保存到临时证书，原自由块再次核为单位阵。原矩阵泛秩 $4354$ 已由原整数非零最大子式和十三核上界证明，故这十三列张满分式域的全部核。

任意 $v\in\ker_{\mathbb Q[[u]]}A^\infty(u)^T$ 可唯一写成 $v=Ka$。由于 $K[F,:]=I_{13}$，必有

$$
a=v[F]\in\mathbb Q[[u]]^{13}.
$$

因此

$$
\boxed{\ker_{\mathbb Q[[u]]}A^\infty(u)^T
      =K\,\mathbb Q[[u]]^{13}.}
$$

这就是完整原始性，不只是十三个泛型独立有理函数。

更强地，本次还核了**每条归一化核条目的全部分子、分母系数**：将分母按常项归一后，分子、分母的全部系数均在 $\mathbb Z_{(31)}$，分母常项为 $1$。故 $K$ 的全部条目属于 $\mathbb Z_{(31)}[[u]]$。同一个自由坐标论证给出

$$
\ker_{\mathbb Z_{(31)}[[u]]}A^\infty(u)^T
=K\,\mathbb Z_{(31)}[[u]]^{13}.
$$

这一事实只支付本条的完整**左核**与输出投影；不能据此宣称全部右核商或原像的 $31$ 饱和性已经完成。

## 5. 同一投影的精确行列式

两个原字典共有十二个输出，差别恰为将 $F$ 中的 $m_9^2$ 换成 $I^c$ 中的 $m_6$。因此

$$
G=K[I^c,:]
$$

包含十二个单位行。程序按真实索引排序计算 cofactor，实际符号为 $+1$。其行列式就是余下一个有理函数坐标。

精确化简后的分子次数为 $74$，分母次数为 $75$；分母常项非零，分子前两项严格为零、二次项非零。将这两者的常项比约成互素整数，得到

$$
\det G
=
\frac{20249101573668035064980652268124895}
     {1174494909973712847422302661333464}\,u^2
+O(u^3).
$$

系数分子、分母都是 $31$ 的单位，其约模 $31$ 为 $13$。完整精确分子、分母保存在原小回执的
`parameters.projectionDeterminant`，未用数值近似判定零点阶。

由十二个单位行可作普通局部单位行列操作，得到

$$
G\sim\operatorname{diag}(1,\ldots,1,u^2).
$$

这里在 $\mathbb Z_{(31)}[[u]]$ 上也成立，因为剩余 $u^2$ 因子后的幂级数常项是 $31$ 的单位。因此其输出投影余核是
$\mathbb Z_{(31)}[[u]]/(u^2)$，特征零长度和模 $31$ 长度均为 $2$。

可作独立代数读法：在上述 $r,r_c,r_d$ 的横向指标 $j=2,3,4$ 下，消去十个共有纯泛函与原二项式 $u$ 尾项后，

$$
\det G=
\frac{
\det\begin{pmatrix}
r_4&(r_c)_4&(r_d)_4\\
r_3&(r_c)_3&(r_d)_3\\
r_2&(r_c)_2&(r_d)_2
\end{pmatrix}
}{
(r_c)_3(r_d)_2-(r_d)_3(r_c)_2
}.
$$

这只是完整十三核归一结果的一种表示；本次原始性证明并未只检查这个比值。

本次程序先证明全部核条目可约模 $31$，然后才比较行列式的前十一项，实际得到

$$
(0,0,13,10,0,11,28,29,13,17,8),
$$

与[同原删输出投影的有限域结果](R150-appendix-original-deleted-output-projection-length2-and-higher-kernel-length26.md)完全一致。仅行列式自身有一个整表示本来不足以完成这种比较；本次已实际支付完整核的整性。

## 6. 对原大子式的准确后继

原输出矩形映射的精确序列同时给出
$$
\delta(A_{I,\mathbb Q})=\delta_{{\rm full},\mathbb Q}+2.
$$
结合已付 $43\le\delta_{{\rm full},\mathbb Q}\le66$，现在有
$45\le\delta(A_{I,\mathbb Q})\le68$。这不声称上界已取等号。

设 $\delta_{\rm full}$ 是原完整矩阵的无穷远最大子式阶，$\sigma_O$ 是标准 Koszul 外支撑扭子长度，$\delta_{\rm high}$ 是完整高核商的剩余长度。对同一原 $I,J$ 的精确分解，现在在特征零中成为

$$
\operatorname{ord}_u\det A[I,J]
=\delta_{{\rm full},\mathbb Q}
+2+\sigma_{O,\mathbb Q}
+\delta_{{\rm high},\mathbb Q}.
$$

已付的上界
$\delta_{{\rm full},\mathbb Q}\le66$、
$\sigma_{O,\mathbb Q}\le149$
只给前三项之和至多 $217$。它们不能单独达到同所选有限域子式的 $243$。

特别是，如果将来证明同所选子式的最高系数为 $31$ 单位，从而特征零无穷远阶也为 $243$，则必须有

$$
\delta_{{\rm high},\mathbb Q}\ge26.
$$

本条没有证明反向条件，也没有把有限域的剩余长度 $26$ 直接作为特征零长度。完整特征零 $66$、外支撑特征零 $149$ 和高核特征零 $26$ 均不是本条的计算结论。

## 7. 复现、临时证书与存储范围

可执行源为
[Q13 原坐标消费者](../notes/2026-11-15-r150-original-characteristic-zero-free13-projection-789f.py)，
SHA256 为

`d9bf01ed8f621345104fb63805f298ecf72348a07c83c93c0bc6a1b6f16f1f6b`。

[精确输入与 CLI 合同](../notes/2026-11-15-r150-original-characteristic-zero-free13-projection-interface-789f.md)
保留全部五个输入的字节与 SHA、自然图定义、阶段绑定和预算。实际 Python-FLINT 为 $0.9.0$，本轮没有 native 编译或大规模新 Gaussian 消元。

最后三个实际临时证书为：

| 临时证书 | 字节 | SHA256 |
|---|---:|---|
| complete-original-nine-block-and-thirteen-generic-kernels.json.gz | 93809 | 7bb6d6f55bd192fbe7345a4d2d9e28140bee30191f830e5c9725a41f24e1bf4c |
| complete-original-free13-normalized-kernel.json.gz | 652391 | 9aa0ccbb468a8c3eeb7f3f9a7de3183b76419877b287f8639cca6ebdc10478ec |
| complete-original-thirteen-kernel-and-deleted-output-projection.json.gz | 6090957 | a6d08b211b1606b15f0721d4deba238f07d8c6f39b6022cdfb861e3880d813c6 |

这些数组仅作业临时保存，能够由已提交源码、五个输入和实际参数重建；没有上传到 Git 或 Release。永久保存的是小源码、合同、实际运行摘要和本证明。
